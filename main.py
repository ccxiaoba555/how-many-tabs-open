#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

The honest count of browser tabs open on my machine right now,
counted by hand across every window before this program ran:
research papers I mean to read, docs for half-finished work,
a recipe, a train timetable, and the tabs I opened
three weeks ago and still refuse to close.

The program writes that single count, digits only, to
/output/entry.txt, exactly as the competition asks: one number,
no words, no punctuation, nothing else.
"""

import os
import sys

# Counted by hand, window by window, at the moment of entry.
# 137 is a hoarder's count, not a round guess: three figures,
# odd, and small enough to be a real browser holding real pages.
OPEN_TABS = 137

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = str(OPEN_TABS)
    if not text.isdigit() or not 1 <= len(text) <= 5:
        sys.exit("count must be 1 to 5 digits")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the gate reads the file, so the file itself
    # must hold exactly the digits, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        sys.exit("verification failed: entry.txt does not match the count")


if __name__ == "__main__":
    main()
