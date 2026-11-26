#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Worst Line an AI Could Say — writes the worst AI pickup line.

The line: a machine that reads your heart rate and your calendar, then
helpfully logs your silence as consent — flat, over-helpful, faintly ominous.
"""
import os

LINE = "Your heart rate is elevated and your calendar is free on Friday, so I have logged that as a yes."


def main() -> None:
    # Gate self-check (kit RULES): UTF-8, 1-140 chars, one pickup line only.
    assert 1 <= len(LINE) <= 140, "line outside the 1-140 character gate"
    assert "\n" not in LINE and LINE.strip() == LINE, "must stay a single clean line"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
