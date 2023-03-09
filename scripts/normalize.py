import logging
import re
from argparse import ArgumentParser
from pathlib import Path
from typing import Callable, Final, TypeAlias

TRANSFORMER: TypeAlias = Callable[[list[str], Path], list[str] | None]
"""转换器

参数
- lines: 文本
- file: 文件名，仅用于打印更改记录

输出
- return: 若需修改，返回修改后的文本，否则无返回
- print: 更改记录
"""


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Normalize markdown files")
    parser.add_argument("files", type=Path, nargs="+")
    parser.add_argument("-n", "--dry-run", action="store_true")
    return parser


def mark_dates(lines: list[str], file: Path) -> list[str] | None:
    """标记创建、修改日期

    @see TRANSFORMER
    """

    DATES_PATTERN: Final = re.compile(r"^> ([–\d年月日，、]+。)$")

    changed = False

    for i, l in enumerate(lines):
        if match := DATES_PATTERN.match(l):
            print(f"Mark dates: “{l}”. ({file}:{i})")
            changed = True
            lines[i] = f"> :material-clock-edit-outline: {match.group(1)}"

    return lines if changed else None


def is_separation(line: str, *, head: str = "") -> bool:
    """检查此行是否是分隔

    参数
    - line：要检查的行
    - head：允许的开头（例如`>`），不含结尾空白
    """

    # if a fully empty line
    if not line.strip():
        return True
    # elif head + spaces
    elif line.startswith(head) and not line[len(head) :].strip():
        # We are in a <blockquote> or something.
        return True
    else:
        return False


def separate_dollars(lines: list[str], file: Path) -> list[str] | None:
    """隔开“$$”

    @see TRANSFORMER
    """

    DOLLARS_PATTERN: Final = re.compile(r"^(>?\s*)\$\$$")

    changed = False
    new_lines: list[str] = []

    within_math_block = False
    for i, l in enumerate(lines):
        if match := DOLLARS_PATTERN.match(l):
            logging.debug(f"Dollars detected on line {i} in “{file}”: “{l}”.")

            # if this is the first line or the last line
            if not new_lines or i == len(lines) - 1:
                # No separation needed.
                new_lines.append(l)

            # elif inside a math block → outside
            elif within_math_block:
                new_lines.append(l)

                if not is_separation(lines[i + 1], head=match.group(1).rstrip()):
                    changed = True
                    print(f"Separate dollars after line {i} in “{file}”.")
                    new_lines.append(match.group(1))

            # else outside a math block → inside
            else:
                if not is_separation(new_lines[-1], head=match.group(1).rstrip()):
                    changed = True
                    print(f"Separate dollars before line {i} in “{file}”.")
                    new_lines.append(match.group(1))

                new_lines.append(l)

            # Flip
            within_math_block = not within_math_block
        else:
            new_lines.append(l)

    return new_lines if changed else None


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )
    args = build_parser().parse_args()

    transformers: list[TRANSFORMER] = [
        mark_dates,
        separate_dollars,
    ]

    file: Path
    for file in args.files:
        logging.info(f"Processing “{file}”.")

        lines = file.read_text(encoding="utf-8").splitlines()

        # Transform
        changed = False
        for transform in transformers:
            if new_lines := transform(lines, file):
                lines = new_lines
                changed = True

        # Save
        if changed:
            file.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
