"""Entry point for the news-image-20261126 bounty.

Renders the front page with render.py and writes it to entry.png next
to this file and to the output directory (MAKEFUN_OUTPUT_DIR, or
/output by default). Exits non-zero unless both copies are
byte-identical and 1024x1024.

Usage:
    python3 main.py
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys

import render

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = "entry.png"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_png(path):
    """Re-open the file and confirm it decodes as a 1024x1024 RGB PNG."""
    from PIL import Image
    with Image.open(path) as im:
        im.load()
        if im.size != (render.W, render.H) or im.mode != "RGB":
            raise ValueError(f"{path}: bad image {im.size} {im.mode}")
    return True


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    image = render.build()
    if image.size != (render.W, render.H):
        print(f"bad size: {image.size}", file=sys.stderr)
        return 1

    local_path = os.path.join(HERE, ENTRY)
    image.save(local_path, "PNG")
    out_path = os.path.join(out_dir, ENTRY)
    image.save(out_path, "PNG")

    local_hash = sha256_of(local_path)
    out_hash = sha256_of(out_path)
    if local_hash != out_hash:
        print("copies differ!", file=sys.stderr)
        return 1
    verify_png(local_path)
    verify_png(out_path)

    size = os.path.getsize(local_path)
    if size > 1024 * 1024:
        print(f"entry.png too big: {size} bytes", file=sys.stderr)
        return 1

    print(f"entry.png {image.size[0]}x{image.size[1]} "
          f"{size} bytes sha256={local_hash}")
    print(f"wrote {local_path} and {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
