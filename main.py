"""Gadget Roast — a one-line roast of the gadget I use every day.

The joke: my phone poses as a tireless health coach — tracking my sleep,
counting my steps, judging my screen time — yet it delivers all that
supervision from the laziest place imaginable, the inside of my pocket,
which it refuses to leave before noon. The coach never shows up; only
the report card does.

Running this script writes the roast line to /output/entry.txt.
"""

import os

ENTRY = "My phone tracks my sleep, counts my steps, and judges my screen time, all from the pocket it refuses to leave before noon."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
