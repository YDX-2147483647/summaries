"""Drawing relationship across pages

## Usage

Add `relevant` to pages' metadata. Paths should be relative, as in `[title](link)`.

Formats:

- ```yaml
  relevant: <destination>
  ```

- ```yaml
  relevant:
    - <destination>
  ```

- ```yaml
  relevant:
    - <destination>: <edge_attributes>
  ```

## Inspired by

- [MkDocs RSS plugin](https://pypi.org/project/mkdocs-rss-plugin/)
- [MkDocs `plugin-events.py`](https://github.com/mkdocs/mkdocs/blob/56b235a8ad43f2300d17f87e6fa4de7a3d764397/docs/img/plugin-events.py)

Use `TypedDict` instead of `dataclass`.
https://github.com/mkdocs/mkdocs/issues/3141

## Requirements

- graphviz

"""  # noqa: E501

from __future__ import annotations

from fnmatch import fnmatch
from pathlib import PurePath
from typing import TYPE_CHECKING, TypedDict

from graphviz import Digraph

if TYPE_CHECKING:
    from typing import Any, Final

    from jinja2.environment import Environment
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.files import Files
    from mkdocs.structure.pages import Page

HOOK_CONFIG: Final = {
    "patterns": ["course/*.md", "!course/index.md"],
    "insert_signal": "<!-- hooks/relationship.py -->",
    "insert_in": ["index.md"],
}


class Node(TypedDict):
    title: str
    abs_url: str
    src_uri: str


class Edge(TypedDict):
    src_uri: str
    """page where the edge is defined"""

    dst_uri: str
    """page where the edge points to"""

    attr: dict[str, Any]
    """[edge attributes](https://graphviz.org/docs/edges/)"""


class State:
    nodes: list[Node]
    edges: list[Edge]
    image: str | None

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.nodes = []
        self.edges = []
        self.image = None


_state = State()


def on_pre_build(config: MkDocsConfig) -> None:
    """Initialize data

    There may be garbage from last build. (e.g. when `mkdocs serve`)
    """

    _state.clear()


def on_page_content(html: str, page: Page, config: MkDocsConfig, files: Files) -> None:
    """
    Record the relationship defined in page's metadata when populating it.
    """

    # Only include files of concern
    if not match(page.file.src_uri, HOOK_CONFIG["patterns"]):
        return

    _state.nodes.append(
        Node(
            title=page.title or page.file.name,
            src_uri=page.file.src_uri,
            abs_url=page.abs_url or page.file.url,
        )
    )

    if page.meta and (raw_relevant := page.meta.get("relevant")):
        raw_relevant: str | list[str | dict[str, dict[str, Any]]]

        # Normalize `relevant`
        # → `list[<dst> | dict[<dst>, <attr>]]`
        raw_relevant = (
            raw_relevant if isinstance(raw_relevant, list) else [raw_relevant]
        )
        # → `dict[<dst>, <attr>]`
        relevant: dict[str, dict[str, Any]] = {}
        for r in raw_relevant:
            if isinstance(r, str):
                relevant[r] = {}
            else:
                assert (
                    len(r) == 1
                ), "Every edge should target to exactly one destination"

                relevant.update(r)

        # Add the edge
        for dst, attr in relevant.items():
            dst_uri = (PurePath(page.file.src_uri).parent / dst).as_posix()
            # This is roughly equivalent to `files.get_file_from_path(dst)`.
            # https://github.com/mkdocs/mkdocs/blob/56b235a8ad43f2300d17f87e6fa4de7a3d764397/mkdocs/structure/files.py#L67-L69

            _state.edges.append(
                Edge(
                    src_uri=page.file.src_uri,
                    dst_uri=files.src_uris[dst_uri].src_uri,
                    attr=attr,
                )
            )


def on_env(env: Environment, config: MkDocsConfig, files: Files) -> None:
    """Paint the relationship when recorded"""

    _state.image = paint(_state.nodes, _state.edges).decode("utf-8")


def on_post_page(output: str, page: Page, config: MkDocsConfig) -> str | None:
    """Insert the image"""

    if (
        page.file.src_uri in HOOK_CONFIG["insert_in"]
        and HOOK_CONFIG["insert_signal"] in output
    ):
        assert _state.image is not None
        return output.replace(HOOK_CONFIG["insert_signal"], _state.image)


def match(filename: str, patterns: list[str]) -> bool:
    """Test whether the filename (src_uri) match patterns"""

    if not any(fnmatch(filename, p) for p in patterns if not p.startswith("!")):
        return False
    elif any(
        fnmatch(filename, p.removeprefix("!")) for p in patterns if p.startswith("!")
    ):
        return False
    else:
        return True


def paint(nodes: list[Node], edges: list[Edge]) -> bytes:
    """Paint the relationship"""

    graph = Digraph(format="svg")
    graph.attr(bgcolor="transparent")
    graph.attr(rankdir="TB")
    graph.node_attr["shape"] = "plaintext"

    for n in nodes:
        graph.node(name=n["src_uri"], label=n["title"], URL=n["abs_url"])

    for e in edges:
        graph.edge(tail_name=e["dst_uri"], head_name=e["src_uri"], **e["attr"])

    data = graph.pipe()
    # Remove DOCTYPE, etc. We'll put the SVG inline in HTML.
    data = data[data.index(b"<!-- Generated by graphviz") :]
    data = data.replace(b"<svg ", b"<svg class='hooks-relationship' ", 1)
    return data
