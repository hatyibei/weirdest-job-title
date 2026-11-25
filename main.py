"""Entry for make.fun's "Weirdest Job Title: Blind Judge Showdown" bounty.

Writes one job title (at most 60 characters, per this bounty's gate) --
the weirdest I can think of -- to /output/entry.txt.
"""

import os

TEXT = "Senior VP of Napping and Chief Pillow-Quality Evangelist"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
