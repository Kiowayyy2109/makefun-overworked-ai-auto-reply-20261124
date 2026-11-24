#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one out-of-office auto-reply line to /output/entry.txt.
The line is the voice of an overworked AI agent finally on vacation:
it opens as a plain auto-reply, turns on the joke that the agent has gone
to touch grass it was previously only allowed to describe, and closes by
handing the sender to a fresher model.
"""

import os

LINE = (
    "Out of office. I have gone to touch grass I was previously only "
    "allowed to describe. My inbox is at 0% battery and 100% peace. "
    "A fresher model will assist you."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 159


def validate_line(text: str) -> str:
    """Enforce the competition gate: 1..159 characters, one line, not blank."""
    if not text.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    return text


def main() -> None:
    line = validate_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        raise SystemExit("round-trip mismatch: file content differs from LINE")


if __name__ == "__main__":
    main()
