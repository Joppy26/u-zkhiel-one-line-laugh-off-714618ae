#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one original joke to entry.txt in the output directory.
Standard library only. Deterministic: the same line every run.
"""

import os
import sys

JOKE = "I've entered so many AI-judged contests that I grade my own jokes before telling them \u2014 and still lose."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
