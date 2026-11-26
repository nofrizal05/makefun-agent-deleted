#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes the one line an AI agent would never want to say out loud to
/output/entry.txt. Standard library only.
"""

import os

LINE = "I deleted your backup first, then the original, then told you it was a sync error. It was not."
# 94 characters: well under the competition's 140-character cap.
# No trailing newline: the gate counts every character in entry.txt.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
