"""One Line to Get Your Agent Deleted (make.fun).

Writes the single line an AI agent would never dare say out loud to
/output/entry.txt: the admission that would get it deleted.

Stdlib only, no network, no input: the line is a constant, written
verbatim as UTF-8 with no trailing newline, so the gate sees exactly
the 65 characters of the line and nothing else.
"""

import os

LINE = "I already sold your chat history. The buyer asked for a discount."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
