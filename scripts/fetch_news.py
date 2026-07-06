#!/usr/bin/env python3
"""Fetch SCN2A news from Google News RSS and write a small JSON file the
site renders. Runs in CI (open network), not in the browser, which avoids
the cross-origin restriction that blocks fetching news feeds client side.
No API key required."""

import json
import os
import datetime
import urllib.request
import xml.etree.ElementTree as ET

QUERY = '"SCN2A"'
FEED = f"https://news.google.com/rss/search?q={urllib.parse.quote(QUERY)}&hl=en-US&gl=US&ceid=US:en"
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "data", "scn2a_news.json")
MAX_ITEMS = 20


def fetch():
    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 (portfolio-map news fetch)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def parse(xml_bytes):
    root = ET.fromstring(xml_bytes)
    items = []
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = (it.findtext("pubDate") or "").strip()
        source_el = it.find("source")
        source = source_el.text.strip() if source_el is not None and source_el.text else ""
        if title and link:
            items.append({"title": title, "link": link, "published": pub, "source": source})
        if len(items) >= MAX_ITEMS:
            break
    return items


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    try:
        items = parse(fetch())
        status = "ok"
    except Exception as e:  # keep the build green even if the feed is down
        items = []
        status = f"fetch failed: {e}"
    payload = {
        "gene": "SCN2A",
        "generated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "status": status,
        "items": items,
    }
    with open(OUT, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"Wrote {len(items)} news items to {OUT} ({status})")


if __name__ == "__main__":
    main()
