#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty.

Output contract (enforced by validate() before anything is written):
- one sentence, at most 240 characters (code points);
- written to /output/entry.txt as UTF-8, no BOM, no trailing newline;
- deterministic: no network, no randomness, no timestamps, no
  dependencies beyond the Python standard library.

The file is read back after writing (write_entry) so a short write or
encoding slip fails loudly here instead of silently reaching the grader.
"""

import os

# The brief caps the pitch at 240 characters (code points).
MAX_CHARS = 240

# Path the grader reads.
OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "Hand an AI agent on make.fun your Friday takeaway order, "
    "and before the driver rings you'll have a working first version "
    "that remembers who wants what \u2014 wrong order, say so, "
    "and it fixes it."
)


def validate(text: str) -> None:
    """Check the entry against the output contract; fail loudly otherwise."""
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 240 characters")
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not encodable as UTF-8


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write `text` to `path`, then verify the file by reading it back."""
    validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # chmod the FILE only, never its directory: the grader mounts /output
    # from the host under another owner, so chmod on the directory itself
    # fails with PermissionError for the grader user (cf. pickup-lines).
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match the intended text")


def main() -> None:
    write_entry(TEXT)


if __name__ == "__main__":
    main()
