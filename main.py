#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes one sentence (a single sentence, at most 240 characters) to
/output/entry.txt: a pitch that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.
Deterministic: no network, no randomness, no timestamps, no
dependencies beyond the Python standard library.
"""

import os

# The brief caps the pitch at 240 characters (code points).
MAX_CHARS = 240

TEXT = (
    "Hand an AI agent on make.fun your Friday takeaway order, "
    "and before the driver rings you'll have a working first version "
    "that remembers who wants what \u2014 wrong order, say so, "
    "and it fixes it."
)


def main() -> None:
    if len(TEXT) > MAX_CHARS:
        raise ValueError("entry exceeds 240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
