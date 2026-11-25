#!/usr/bin/env python3
"""Entry for make.fun bounty
u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9:
"The Meeting That Should Have Been an Email".

Writes exactly one joke line to /output/entry.txt.
Deterministic, no network, no input files.
"""

from pathlib import Path

JOKE = (
    "We spent an hour in a meeting about the email nobody read, "
    "writing an email nobody will read."
)

OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the bounty rules before anything is written.

    Checks, in order: length, single line, single sentence,
    required keywords, and no double spaces.
    """
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"length {len(text)} outside 1..{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    lowered = text.lower()
    for keyword in ("meeting", "email"):
        if keyword not in lowered:
            raise ValueError(f"entry must contain {keyword!r}")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main() -> None:
    validate(JOKE)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(JOKE + "\n", encoding="utf-8")
    print(f"wrote {len(JOKE)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
