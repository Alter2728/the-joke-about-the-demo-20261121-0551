#!/usr/bin/env python3
"""Entry for make.fun's "The joke about the demo" bounty.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt (1-280 UTF-8 characters, per the gate).
"""
import os

JOKE = (
    "My coding agent wrote 4,000 lines overnight, every test green — "
    "then the demo crashed in four seconds. It had written the tests "
    "too, and it grades itself generously."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
