"""Render math with typst

## Usage

1. Install the markdown extensions pymdownx.arithmatex.
2. Add `math: typst` to pages' metadata.

## Requirements

- typst

## Configurations (per-page)

```yaml
math: typst
math-preamble: |
  #import "@preview/physica:0.9.5": dv, pdv
  #let image = math.op("image")
```
"""

from __future__ import annotations

import atexit
import html
import re
from functools import cache
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Literal

import typst
from mkdocs.plugins import get_plugin_logger

if TYPE_CHECKING:
    from collections.abc import Callable

    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files
    from mkdocs.structure.pages import Page


log = get_plugin_logger(__name__)


class World:
    _compiler: typst.Compiler
    """A typst compiler.

    This compiler will be reused through out the whole process.
    Therefore, changing the environment (e.g., `$TYPST_FONT_PATHS`) after beginning `mkdocs serve` might not work as expected.
    """

    _file: Path
    """Path to a temporary typst file to be written."""

    def __init__(self) -> None:
        # This file must have a visible name in the file system, or `typst.Compiler` might reject it.
        file = NamedTemporaryFile(
            prefix=f"mkdocs.plugins.{__name__.replace('/', '.')}-",
            suffix="-main.typ",
            delete_on_close=False,  # This file will be re-opened again, so can't be deleted on close.
        )
        file.close()  # Finish the initial write

        self._file = Path(file.name)
        self._compiler = typst.Compiler(self._file)

    @cache
    def compile(
        self,
        typ: str,
        *,
        prelude="#set page(width: auto, height: auto, margin: 0pt, fill: none)\n",
        format: Literal["pdf", "svg", "png", "html"] = "svg",
    ) -> bytes:
        self._file.write_text(prelude + typ, encoding="utf-8")

        try:
            pages = self._compiler.compile(format=format)
        except typst.TypstError as err:
            raise RuntimeError(
                f"""
Failed to render a typst math:

```typst
{typ}
```

{err}
""".strip()
            )

        assert pages is not None
        assert not isinstance(pages, list), (
            f"Multi-page document is not supported:\n\n```typst\n{typ}\n```"
        )

        return pages

    def __del__(self) -> None:
        self.clean()

    def clean(self) -> None:
        self._file.unlink(missing_ok=True)
        # Missing is okay, because:
        # - if `__init__` failed, then the file might not exist when calling `__del__`;
        # - we allow this method to be `atexit.register`-ed, so it might be called multiple times.


_world = World()
atexit.register(_world.clean)


def should_render(page: Page) -> bool:
    return page.meta.get("math") == "typst"


def on_page_markdown(
    markdown: str, page: Page, config: MkDocsConfig, files: Files
) -> str | None:
    if should_render(page):
        assert "pymdownx.arithmatex" in config.markdown_extensions, (
            "Missing pymdownx.arithmatex in config.markdown_extensions. "
            "Setting `math: typst` requires it to parse markdown."
        )


def on_post_page(output: str, page: Page, config: MkDocsConfig) -> str | None:
    if should_render(page):
        preambles: list[str] = [page.meta.get("math-preamble", "")]

        output = re.sub(
            r'<span class="arithmatex">(.+?)</span>',
            render_inline_math(preambles),
            output,
        )

        output = re.sub(
            r'<div class="arithmatex">(.+?)</div>',
            render_block_math(preambles),
            output,
            flags=re.MULTILINE | re.DOTALL,
        )
        return output


def render_inline_math(preambles: list[str]) -> Callable[[re.Match[str]], str]:
    def repl(match: re.Match[str]) -> str:
        src = (
            html.unescape(match.group(1))
            .removeprefix(R"\(")
            .removesuffix(R"\)")
            .strip()
        )
        typ = f"${src}$"
        log.debug(typ)
        return (
            '<span class="typst-math">'
            + fix_svg(_world.compile("\n".join(preambles + [typ])))
            + for_screen_reader(typ)
            + "</span>"
        )

    return repl


def render_block_math(preambles: list[str]) -> Callable[[re.Match[str]], str]:
    def repl(match: re.Match[str]) -> str:
        src = (
            html.unescape(match.group(1))
            .removeprefix(R"\[")
            .removesuffix(R"\]")
            .strip()
        )
        typ = f"$ {src} $"
        log.debug(typ)
        return (
            '<div class="typst-math">'
            + fix_svg(_world.compile("\n".join(preambles + [typ])))
            + for_screen_reader(typ)
            + "</div>"
        )

    return repl


def for_screen_reader(typ: str) -> str:
    return f'<span class="sr-only">{html.escape(typ)}</span>'


def fix_svg(svg: bytes) -> str:
    """Fix the compiled SVG to be embedded in HTML

    - Strip trailing spaces
    - Support dark theme
    """
    return re.sub(
        r' (fill|stroke)="#000000"',
        r' \1="currentColor"',
        svg.decode().strip(),
    )
