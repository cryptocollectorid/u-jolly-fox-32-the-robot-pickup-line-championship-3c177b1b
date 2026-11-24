#!/usr/bin/env python3
"""The Robot Pickup Line Championship — one-line robot pickup line.

Writes the line to /output/entry.txt and prints it.
"""

import os

LINE = "I scanned 4 billion faces today, and my facial recognition flagged only yours as worth saving to memory."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
