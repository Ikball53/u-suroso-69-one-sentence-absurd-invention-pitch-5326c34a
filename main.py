#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — entry program.

Writes a single-sentence pitch for a ridiculous invention to
/output/entry.txt. Deterministic, no network, no randomness: the same
bytes come out on every run.
"""

from pathlib import Path

# The pitch: a toaster that gives up before you can blame it.
PITCH = (
    "A toaster that pops up a tiny white flag of surrender the instant "
    "your bread burns, so breakfast admits defeat before you do."
)

DESTINATION = Path("/output/entry.txt")

# The gate allows 1 to 220 characters; stay well inside it.
MAX_PITCH_CHARS = 220


def check_pitch() -> None:
    """Fail loudly if the pitch ever drifts outside the gate's limits."""
    stripped = PITCH.strip()
    if not stripped or len(PITCH) != len(stripped):
        raise ValueError("pitch must be non-blank with no surrounding whitespace")
    if len(PITCH) > MAX_PITCH_CHARS:
        raise ValueError(f"pitch is {len(PITCH)} chars, over the 220 limit")
    if PITCH.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence")


def emit_pitch() -> None:
    """Persist the pitch as exact UTF-8 bytes, with no trailing newline."""
    check_pitch()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(PITCH.encode("utf-8"))


if __name__ == "__main__":
    emit_pitch()
