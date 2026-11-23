#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; no network; deterministic.
"""

import os

# The reply: an AI agent on vacation hands its inbox to a smaller,
# context-free, overconfident model. 132 characters.
ENTRY = (
    "I'm on vacation. While I'm away, a smaller model with no context "
    "and total confidence will answer your emails. Good luck to us both."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
