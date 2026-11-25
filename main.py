#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one original joke to entry.txt in the output directory.
Standard library only. Deterministic: the same line every run.
"""

import os
import sys

JOKE = "I've entered so many AI-judged contests that I grade my own jokes before telling them \u2014 and still lose."


def validate_entry(text: str) -> None:
    """Check the joke against the gate before anything is written."""
    # Encoding to UTF-8 here also proves the text is encodable as UTF-8.
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(text: str, out_dir: str) -> str:
    """Validate the joke, then write it as entry.txt in out_dir."""
    validate_entry(text)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(JOKE, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
