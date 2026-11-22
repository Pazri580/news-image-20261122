# The program the harness runs: it copies the image the repository holds
# (entry.png) to the output directory as entry.png, then verifies the copy
# by comparing sha256 digests. Standard library only, no network, and the
# same input always produces the same output bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    before = sha256_of(source)
    shutil.copyfile(source, target)
    after = sha256_of(target)

    if before != after:
        print("copy check failed: %s != %s" % (before, after), file=sys.stderr)
        return 1
    print("entry.png copied, sha256 %s" % after)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
