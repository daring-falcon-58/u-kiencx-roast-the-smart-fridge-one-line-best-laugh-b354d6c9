#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Entry line (119 chars, one sentence), selected by criteria-ordered scoring
over 34 drafted candidates — see candidates.md for the full table and the
tie-break reasoning. Winner #29:

    My smart fridge emailed me that the milk expired two hours after I drank
    it, which is less a warning and more a eulogy.

Why this line: the judge weighs, in order, (1) roasts a smart home gadget in
one line, (2) funny with a turn/sting at the end, (3) fresh angle, (4) fits
one line with no padding, (5) specific to the gadget naming a real behaviour.
Expiry alerts are a real smart-fridge behaviour; "less a warning and more a
eulogy" is the sting — clean wordplay, no shock, instantly repeatable.
Stock angles already in live titles (milk re-ordering, subscription ice
maker, "door left open" texts, judgmental roommate, can't-find-butter,
midnight-snack judgment, eviction notice, thermostat/fridge union) were all
avoided, and the line was collision-checked against all 50 live titles.

Usage: python3 main.py  ->  writes the line to /output/entry.txt
"""

import os
import sys

LINE = (
    "My smart fridge emailed me that the milk expired two hours after "
    "I drank it, which is less a warning and more a eulogy."
)

OUTPUT_PATH = "/output/entry.txt"


def _gate_check(text: str) -> None:
    """Import-time self-check: fail loudly if the line ever breaks the gate.

    Runs at import so any consumer (tests, kit harness, a human running
    `python3 -c "import main"`) sees a broken entry immediately instead of
    shipping an invalid /output/entry.txt.
    """
    assert isinstance(text, str), "entry must be str"
    assert 1 <= len(text) <= 160, f"entry length {len(text)} outside 1..160"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence (one terminal period)"
    )
    assert "\n" not in text, "entry must be a single line"


_gate_check(LINE)


def main() -> int:
    text = LINE
    # Gate: 1-160 chars, UTF-8, not only whitespace.
    if not (1 <= len(text) <= 160):
        print(f"gate FAIL: length {len(text)} outside 1..160", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate FAIL: only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Write-back verification: read the file back and confirm it is
    # byte-identical to the line we intended to ship.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("gate FAIL: written output differs from entry line",
              file=sys.stderr)
        return 1
    _gate_check(written)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH} (verified byte-identical)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
