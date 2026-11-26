#!/usr/bin/env python3
"""Painfully honest out-of-office auto-reply.

Writes a single sentence (at most 200 characters) to /output/entry.txt:
brutally honest about the inbox, still polite enough for a manager.
"""

import os

REPLY = (
    "I'm out of office; your email joins 3,214 unread messages "
    "I have already accepted I will never read, and I feel lighter already."
)


def main():
    text = REPLY.strip()
    assert 1 <= len(text) <= 200, f"reply is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "reply must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
