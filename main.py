#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human (@aimcuk).

Writes one funny single-line one-star review from a house cat about its
human, under 200 characters, in deadpan review shape.
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 One star. He works from home now and follows me "
    "from room to room like a stray. I used to have the whole house to "
    "myself. Now I can't even use the litter box alone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
