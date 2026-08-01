#!/usr/bin/env python3
"""Inventory explicitly supplied Etsy product folders without modifying them."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".heic", ".heif"}
IGNORED_NAMES = {".DS_Store"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folders", nargs="+")
    args = parser.parse_args()

    results = []
    for raw in args.folders:
        path = Path(raw).expanduser().resolve()
        record = {
            "input": raw,
            "folder": str(path),
            "product_name": path.name,
            "exists": path.exists(),
            "is_directory": path.is_dir(),
            "images": [],
            "ignored": [],
            "status": "ok",
        }
        if not path.exists():
            record["status"] = "missing"
        elif not path.is_dir():
            record["status"] = "not_a_directory"
        else:
            for child in sorted(path.iterdir(), key=lambda p: p.name.lower()):
                if child.name.startswith(".") or child.name in IGNORED_NAMES:
                    record["ignored"].append(child.name)
                elif child.is_file() and child.suffix.lower() in IMAGE_EXTENSIONS:
                    record["images"].append(str(child))
                else:
                    record["ignored"].append(child.name)
            if not record["images"]:
                record["status"] = "no_supported_images"
        results.append(record)

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0 if all(r["status"] == "ok" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
