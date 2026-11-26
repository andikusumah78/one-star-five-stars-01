"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes a single sentence (at most 200 characters) to ``entry.txt``: a
one-star review of planet Earth in the voice of an alien tourist, which
still slips in a real compliment about the food.

The gate requires /output/entry.txt to be UTF-8 text of 1-200 characters,
not only whitespace. This program validates the line before writing it,
writes it, then reads it back to confirm what landed on disk is exactly
the validated line.
"""

import os

LINE = (
    "One star: the planet charges rent for sleeping indoors, the weather "
    "changes its mind hourly, and the locals worship glowing rectangles — "
    "but the street noodles are worth the nine-light-year flight."
)

MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Check the entry line against the gate and return it unchanged."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")  # raises if the line is not valid UTF-8 text
    return line


def resolve_out_dir() -> str:
    """Output directory: MAKEFUN_OUTPUT_DIR, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str, line: str) -> str:
    """Write the validated line to entry.txt and verify it by reading back."""
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("entry.txt on disk does not match the validated line")
    return path


def main() -> None:
    path = write_entry(resolve_out_dir(), LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
