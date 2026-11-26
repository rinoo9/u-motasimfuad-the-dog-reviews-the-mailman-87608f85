#!/usr/bin/env python3
"""The Dog Reviews the Mailman -- make.fun one-liner entry.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. The program is deterministic: the same line every run.
"""
import os

REVIEW = (
    "One star. The mailman comes every day, waves through my gate like he owns "
    "the place, and has never once delivered the package addressed to ME. "
    "I will bark again tomorrow."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
