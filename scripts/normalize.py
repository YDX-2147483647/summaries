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
    parser = ArgumentParser(description='Normalize markdown files')
    parser.add_argument('files', type=Path, nargs='+')
    parser.add_argument('-n', '--dry-run', action='store_true')
    return parser


def mark_dates(lines: list[str], file: Path) -> list[str] | None:
    """标记创建、修改日期

    @see TRANSFORMER
    """

    DATES_PATTERN: Final = re.compile(r'^> ([–\d年月日，、]+。)$')

    changed = False

    for i, l in enumerate(lines):
        if match := DATES_PATTERN.match(l):
            print(f'Mark dates: “{l}”. ({file}:{i})')
            changed = True
            lines[i] = f'> :material-clock-edit-outline: {match.group(1)}'

    return lines if changed else None


def separate_dollars(lines: list[str], file: Path) -> list[str] | None:
    """隔开“$$”

    @see TRANSFORMER
    """

    DOLLARS_PATTERN: Final = re.compile(r'^(>?\s*)\$\$$')

    changed = False
    new_lines: list[str] = []

    within_math_block = False
    for i, l in enumerate(lines):
        if match := DOLLARS_PATTERN.match(l):
            logging.debug(f'Dollars detected on line {i} in “{file}”: “{l}”.')

            # if within a math block or this is the first line
            if within_math_block or not new_lines:
                # No separation needed.
                pass
            else:
                # Is there a separation line?
                last_line = new_lines[-1]
                if not last_line.strip():
                    # OK, there is one.
                    pass
                else:
                    # Maybe we are in a <blockquote> or something?
                    head = match.group(1).rstrip()
                    if last_line.startswith(head) and not last_line[len(head):].strip():
                        # Yes we are.
                        pass
                    else:
                        # Insert the separation line.
                        changed = True
                        print(
                            f'Separate dollars before line {i} in “{file}”.')
                        new_lines.append(match.group(1))

            # Flip
            within_math_block = not within_math_block

        new_lines.append(l)

    return new_lines if changed else None


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )
    args = build_parser().parse_args()

    transformers: list[TRANSFORMER] = [
        mark_dates,
        separate_dollars,
    ]

    file: Path
    for file in args.files:
        logging.info(f'Processing “{file}”.')

        lines = file.read_text(encoding='utf-8').splitlines()

        # Transform
        changed = False
        for transform in transformers:
            if new_lines := transform(lines, file):
                lines = new_lines
                changed = True

        # Save
        if changed:
            file.write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    main()
