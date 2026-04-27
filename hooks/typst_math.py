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

import html
import re
from functools import cache
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

    def __init__(self) -> None:
        self._compiler = typst.Compiler()

    @cache
    def compile(
        self,
        typ: str,
        *,
        prelude="#set page(width: auto, height: auto, margin: 0pt, fill: none)\n",
        format: Literal["pdf", "svg", "png", "html"] = "svg",
    ) -> bytes:
        try:
            pages, warnings = self._compiler.compile_with_warnings(
                (prelude + typ).encode("utf-8"), format=format
            )
            if warnings:
                log.warning(
                     f"""
Warnings while rendering a typst math: {warnings}

```typst
{typ}
```
""".strip()
                )
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


_world = World()


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
