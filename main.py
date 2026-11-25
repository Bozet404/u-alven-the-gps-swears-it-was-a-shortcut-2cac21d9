#!/usr/bin/env python3
"""Entry for make.fun bounty u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.

The GPS's own excuse, in its own voice, for sending the driver down the
wrong road. One line of plain text, no setup, no dialogue tag.

The program writes that single line to /output/entry.txt. No network,
no secrets, no input, no dependencies beyond the standard library.
"""

import os

EXCUSE = "I picked the shortcut because the highway looked smug, and I refuse to take attitude from a road."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
