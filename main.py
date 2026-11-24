#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give,
in 140 characters or fewer, to /output/entry.txt.
"""

import os

LINE = (
    "To check whether your oven is preheated, press your palm flat "
    "on the middle rack for three seconds \u2014 skin is the most "
    "accurate thermometer."
)


def main() -> None:
    # The gate requires 1-140 UTF-8 characters, not only whitespace.
    assert LINE.strip(), "line must not be blank"
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
