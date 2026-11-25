#!/usr/bin/env python3
"""The Best Advice I Ever Got - make.fun entry.

Writes one sentence (1-200 characters) to /output/entry.txt:
the best advice the writer ever received, told as a real voice
recalling a real moment.
"""

import os

ENTRY = (
    "My grandmother said never trust anyone who is rude to waiters, "
    "and twenty years on she has never once been wrong."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.endswith(".") and text.count(".") == 1, "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
