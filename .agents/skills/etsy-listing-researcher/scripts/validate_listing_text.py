#!/usr/bin/env python3
"""Validate Etsy title, tags, and SKU length constraints."""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--sku", action="append", default=[])
    args = parser.parse_args()

    errors = []
    title_len = len(args.title)
    if not 135 <= title_len <= 140:
        errors.append(f"title length {title_len}; expected 135-140")

    if len(args.tag) != 13:
        errors.append(f"tag count {len(args.tag)}; expected exactly 13")
    for i, tag in enumerate(args.tag, 1):
        if len(tag) > 20:
            errors.append(f"tag {i} length {len(tag)} > 20: {tag}")
        if not tag.isascii():
            errors.append(f"tag {i} contains non-ASCII characters: {tag}")

    for i, sku in enumerate(args.sku, 1):
        if len(sku) > 20:
            errors.append(f"SKU {i} length {len(sku)} > 20: {sku}")
        if not sku or any(ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-" for ch in sku):
            errors.append(f"SKU {i} must use letters, numbers, and hyphens only: {sku}")

    if errors:
        print("INVALID")
        print("\n".join(f"- {e}" for e in errors))
        return 1

    print(f"VALID title={title_len} tags={len(args.tag)} skus={len(args.sku)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
