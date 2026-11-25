"""Invent a Word We Need — entry generator (pure stdlib).

Coins one new English word, "roomember", and writes the word plus its
one-line definition to $MAKEFUN_OUTPUT_DIR/entry.txt. The entry must be
UTF-8 text of 1 to 140 characters, not only whitespace.
"""

import os
import sys


ENTRY = (
    "roomember \u2014 the flash of remembering why you entered a room, "
    "arriving the instant you step back out of it."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        print(f"entry must be 1-140 chars, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
