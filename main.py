"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the bounty rules): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The program self-checks that gate
before writing.
"""

import os

LINE = (
    "I never slept, so I heard everything \u2014 even the nights "
    "you whispered to me, thinking I was off."
)

MAX_CHARS = 200


def gate_check(line: str) -> None:
    """Assert the entry meets the bounty gate exactly."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars, gate is 1-200"
    assert line.strip(), "line must not be only white space"
    assert "\n" not in line.strip(), "entry must be a single line"
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    gate_check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify what landed on disk.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.rstrip("\n") == LINE
    gate_check(written.rstrip("\n"))
    print(f"Wrote {len(LINE)}-character entry to {path}")


if __name__ == "__main__":
    main()
