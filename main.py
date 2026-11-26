#!/usr/bin/env python3
"""One Word, First Thought — make.fun micro entry.

Writes the chosen word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Standard library only.
"""

import os

WORD = "Petrichor"


def check_gate(word):
    """Self-check against the kit gate: UTF-8 text of 1-24 characters,
    not only whitespace, exactly one word."""
    if not word or word != word.strip():
        raise ValueError("word must not be empty or padded with whitespace")
    if len(word) > 24:
        raise ValueError("word must be at most 24 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")


def main():
    check_gate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
