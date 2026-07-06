#!/usr/bin/env python3
"""Harvest ORCID iDs of researchers who study SCN2A.

Strategy: query OpenAlex for works matching the gene term, walk every
authorship, and collect distinct authors keyed on ORCID. Authors are ranked
by the number of matching works, and their institutions are aggregated.

OpenAlex is free and needs no API key. Set OPENALEX_MAILTO to your email to
join the faster "polite pool". Runs in CI or locally; only uses the standard
library. Output feeds the Person nodes of the portfolio."""

import os
import csv
import json
import time
import datetime
import urllib.parse
import urllib.request
from collections import defaultdict

TERM = os.environ.get("GENE_TERM", "SCN2A")
MAILTO = os.environ.get("OPENALEX_MAILTO", "").strip()
BASE = "https://api.openalex.org/works"
PER_PAGE = 200
MAX_PAGES = 30  # safety cap; ~6000 works
HERE = os.path.dirname(__file__)
OUT_JSON = os.path.join(HERE, "..", "docs", "data", "scn2a_researchers.json")
OUT_CSV = os.path.join(HERE, "..", "docs", "data", "scn2a_person_nodes.csv")


def fetch(cursor):
    params = {
        "filter": f"title_and_abstract.search:{TERM}",
        "per-page": PER_PAGE,
        "cursor": cursor,
        "select": "authorships,publication_year",
    }
    if MAILTO:
        params["mailto"] = MAILTO
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": f"scn2a-orcid-harvest ({MAILTO or 'no-mailto'})"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read())
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def orcid_id(url):
    return url.rsplit("/", 1)[-1] if url else None


def main():
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)

    # aggregation keyed on ORCID
    people = {}                     # orcid_id -> record
    inst_counts = defaultdict(lambda: defaultdict(int))  # orcid_id -> {institution: count}
    authors_no_orcid = set()        # OpenAlex author ids lacking an ORCID
    total_works = 0
    status = "ok"

    try:
        cursor = "*"
        for _ in range(MAX_PAGES):
            data = fetch(cursor)
            results = data.get("results", [])
            if not results:
                break
            total_works += len(results)
            for w in results:
                year = w.get("publication_year")
                for a in w.get("authorships", []):
                    author = a.get("author") or {}
                    oid = orcid_id(author.get("orcid"))
                    name = author.get("display_name")
                    insts = [i.get("display_name") for i in (a.get("institutions") or []) if i.get("display_name")]
                    if not oid:
                        if author.get("id"):
                            authors_no_orcid.add(author["id"])
                        continue
                    rec = people.get(oid)
                    if not rec:
                        rec = {"orcid": oid, "name": name, "works_count": 0,
                               "first_year": year, "last_year": year}
                        people[oid] = rec
                    rec["works_count"] += 1
                    if name and not rec.get("name"):
                        rec["name"] = name
                    if year:
                        if rec["first_year"] is None or year < rec["first_year"]:
                            rec["first_year"] = year
                        if rec["last_year"] is None or year > rec["last_year"]:
                            rec["last_year"] = year
                    for inst in insts:
                        inst_counts[oid][inst] += 1
            cursor = (data.get("meta") or {}).get("next_cursor")
            if not cursor:
                break
            time.sleep(0.2)
    except Exception as e:  # keep the build green even if the API is down
        status = f"harvest failed: {e}"

    # attach top institutions and finalize
    researchers = []
    for oid, rec in people.items():
        insts = sorted(inst_counts[oid].items(), key=lambda kv: (-kv[1], kv[0]))
        rec["institutions"] = [i for i, _ in insts[:3]]
        rec["orcid_url"] = f"https://orcid.org/{oid}"
        researchers.append(rec)
    researchers.sort(key=lambda r: (-r["works_count"], (r.get("name") or "").lower()))

    payload = {
        "term": TERM,
        "source": "OpenAlex",
        "generated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "status": status,
        "total_works_scanned": total_works,
        "researchers_with_orcid": len(researchers),
        "authors_without_orcid": len(authors_no_orcid),
        "researchers": researchers,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(payload, f, indent=2)

    # CSV of Person nodes for portfolio ingestion
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["orcid", "name", "institution", "scn2a_works_count", "first_year", "last_year"])
        for r in researchers:
            writer.writerow([r["orcid"], r.get("name", ""),
                             (r["institutions"][0] if r["institutions"] else ""),
                             r["works_count"], r.get("first_year", ""), r.get("last_year", "")])

    print(f"{len(researchers)} researchers with ORCID from {total_works} works ({status})")


if __name__ == "__main__":
    main()
