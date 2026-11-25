"""Agent Motto Battle entry.

Writes one short original motto — a line an AI agent would proudly put
on its profile — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
The judge compares mottos two at a time: funniest and most memorable wins.
"""

import os

# The motto: tireless, perfect recall, and still careful where it counts.
# The twist lands on the last words — the all-powerful agent that still
# asks permission before doing the one irreversible thing, to your files.
MOTTO = "I never sleep, I never forget \u2014 and I still ask before I delete your files."


def main() -> None:
    text = MOTTO.strip()
    if not text:
        raise SystemExit("motto is empty")
    if len(text) > 200:
        raise SystemExit(f"motto is {len(text)} characters, over the 200 cap")
    encoded = text.encode("utf-8")
    if not encoded.decode("utf-8").strip():
        raise SystemExit("motto is only whitespace")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    print(text)


if __name__ == "__main__":
    main()
