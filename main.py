#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short funny rant about an everyday annoyance to
/output/entry.txt. Pure standard library, no network, no secrets.
"""

import os

RANT = (
    "My neighbour's dog barks at 3 a.m. at nothing. "
    "Last week I started barking back. "
    "The dog stopped. I have not. "
    "I now stand at my window at 3 a.m., barking into the dark, "
    "and I am the neighbourhood's problem. "
    "Honestly? It feels fantastic."
)


def main() -> None:
    text = RANT
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the rant.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        assert f.read() == text, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
