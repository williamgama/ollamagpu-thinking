#!/usr/bin/env python3
"""Apply standby productivity patch AFTER the existing V4/V5 cumulative patches.
No build, no networking, no installation. All anchors are validated before writing."""
import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.source.resolve()
    spec = json.loads(Path(__file__).with_name("productivity.json").read_text())
    changed = {}
    for name, old, new in spec["patches"]:
        p = root / name
        src = changed.get(p)
        if src is None:
            src = p.read_text()
        if src.count(old) != 1:
            raise SystemExit(f"Unexpected anchor count: {name}: {old[:100]!r}")
        changed[p] = src.replace(old, new, 1)
    for name, content in spec["files"].items():
        p = root / name
        if p.exists():
            raise SystemExit(f"Unexpected existing file: {name}")
        changed[p] = content
    print(f"Validated {len(spec['patches'])} anchors; {len(changed)} files planned")
    if not args.check:
        for p, content in changed.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)

if __name__ == "__main__":
    main()
