#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

A robot vacuum's one-line excuse for missing a spot, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for
local testing). The excuse is rooted in the vacuum's own world: its
map, not a generic apology — and the map never apologizes back.
"""

import os

ENTRY = (
    "I missed that spot because my map says it is a lake now. "
    "I do not argue with the map. The map has never once apologized to me."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-140")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
