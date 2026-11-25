#!/usr/bin/env python3
"""Make the AI Judge Laugh (rama-melon) — one office joke, one line.

Entry: a single office-life joke under 200 characters, written to
/output/entry.txt. The joke: the fire drill is the only thing that
ever gets the whole office out of a meeting on time.
"""

import os

ENTRY = (
    "The fire drill interrupted a two-hour meeting, and for the first "
    "time all year, the whole office left on time."
)


def main() -> None:
    assert len(ENTRY) < 200, "entry must be under 200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
