#!/usr/bin/env python3

import re
import sys
from pathlib import Path


INDENT_SIZE = 3


def format_verbatim_blocks(text: str) -> str:
    pattern = re.compile(
        r"(\\begin\{verbatim\}\r?\n)(.*?)(\r?\n[ \t]*\\end\{verbatim\})",
        re.DOTALL,
    )

    def replace(match: re.Match) -> str:
        begin = match.group(1)
        body = match.group(2)
        end = match.group(3)

        lines = body.splitlines()

        result = []
        depth = 0

        for line in lines:
            line = line.strip()

            if not line:
                result.append("")
                continue

            if line.startswith("}"):
                depth = max(0, depth - 1)

            result.append(
                "         " + " " * ((depth + 1) * INDENT_SIZE) + line
            )

            opens = line.count("{")
            closes = line.count("}")

            if line.startswith("}"):
                closes -= 1

            depth += opens - closes
            depth = max(0, depth)

        return begin + "\n".join(result) + end

    return pattern.sub(replace, text)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <tex-file>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.is_file():
        print(f"File not found: {path}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    path.write_text(
        format_verbatim_blocks(text),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()