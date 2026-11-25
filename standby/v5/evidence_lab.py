#!/usr/bin/env python3
"""Offline evidence packing baseline for the existing search benchmark.
No network, credentials, or inference. Not a production ranking or fetcher.
"""
import argparse
import json
from urllib.parse import urlsplit, parse_qsl
from pathlib import Path

def canonical(url):
    p = urlsplit(url)
    if p.scheme not in ("http", "https") or not p.hostname or p.username or p.password:
        raise ValueError("invalid public source URL")
    params = tuple(sorted((k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in {"gclid", "fbclid"}
        and not (p.hostname == "support.google.com" and k == "hl")))
    return (p.hostname.lower(), p.path.rstrip("/") or "/", params)

def compact(record):
    seen = set()
    out = []
    for item in record["results"]:
        try:
            key = canonical(item["url"])
        except (ValueError, KeyError, TypeError):
            continue
        if key in seen:
            continue
        seen.add(key)
        out.append(dict(id=f"S{len(out)+1}", title=" ".join(item["title"].split())[:180],
                        url=item["url"], excerpt=" ".join(item["snippet"].split())[:450]))
        if len(out) == 3:
            break
    return dict(query=record["query"], provider=record["provider"], sources=out)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("report", type=Path)
    args = p.parse_args()
    report = json.loads(args.report.read_text())
    totals = {}
    for record in report["records"]:
        if "results" not in record or "response_bytes" not in record:
            continue
        pack = compact(record)
        size = len(json.dumps(pack, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
        t = totals.setdefault(record["provider"], dict(raw=0, compact=0))
        t["raw"] += record["response_bytes"]
        t["compact"] += size
        print(record["provider"], record["category"], size, "bytes", len(pack["sources"]), "sources")
    for provider, t in totals.items():
        print(provider, t, round(100*(1-t["compact"]/t["raw"]),2) if t["raw"] else None, "% reduction")

if __name__ == "__main__":
    main()
