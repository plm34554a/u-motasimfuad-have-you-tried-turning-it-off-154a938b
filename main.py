#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun one-liner entry.

Writes exactly one funny line a hopeless tech support agent says to a
desperate customer to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
and prints it to stdout. Pure standard library.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I ask because the last "
    "customer fixed it that way, and I have been riding that one success "
    "for four years."
)

# The competition requires a single line under 200 characters.
# Verified: 150 characters, so there is room to spare — the joke stays.
assert len(LINE) < 200, f"line is {len(LINE)} chars, must be under 200"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write atomically so a crash mid-write can never leave a partial
    # entry behind, then read it back and verify it byte-for-byte.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    print(LINE)


if __name__ == "__main__":
    main()
