#!/usr/bin/env python3
"""Last Text at One Percent -- make.fun entry.

Writes the funniest final text a dying phone sends at 1% battery
to /output/entry.txt. Deterministic: the same single message every run.

The joke: the phone confesses it has been at 0% for the last hour --
the 1% was a lie -- and then dies mid-word, mid-sentence.
"""

import os

MESSAGE = (
    "okay, confession: i've been at 0% for the last hour. "
    "the 1% was a lie. i just wanted to see how this ends. "
    "it ends like thi"
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> str:
    """Validate the message against the gate and write it out."""
    text = MESSAGE
    if not (1 <= len(text) <= 200):
        raise ValueError(f"message is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("message must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return text


def main() -> None:
    text = write_entry()
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
