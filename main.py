"""Entry point: build the news-image entry and verify it.

Saves entry.png next to this file and to MAKEFUN_OUTPUT_DIR
(default /output), then checks both copies are byte-identical,
exactly 1024x1024 and no larger than 1 MiB. Exits non-zero on failure.
"""

import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import render  # noqa: E402

MAX_BYTES = 1024 * 1024


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    img = render.build()
    if img.size != (1024, 1024):
        print(f"FAIL: image is {img.size}, expected (1024, 1024)",
              file=sys.stderr)
        return 1

    local_path = os.path.join(here, "entry.png")
    out_path = os.path.join(out_dir, "entry.png")
    img.save(local_path)
    img.save(out_path)

    local_hash = sha256_of(local_path)
    out_hash = sha256_of(out_path)
    if local_hash != out_hash:
        print("FAIL: local and output copies differ", file=sys.stderr)
        return 1

    size = os.path.getsize(local_path)
    if size > MAX_BYTES:
        print(f"FAIL: entry.png is {size} bytes, over 1 MiB limit",
              file=sys.stderr)
        return 1

    print(f"OK: entry.png {img.size[0]}x{img.size[1]} {size} bytes")
    print(f"sha256: {local_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
