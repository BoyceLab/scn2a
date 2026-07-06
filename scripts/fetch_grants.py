#!/usr/bin/env python3
"""Harvest federally funded grants mentioning the gene from NIH RePORTER.

Uses the public RePORTER v2 projects API (a POST endpoint), so this runs
server side at build time rather than in the browser. No API key required.
Deduplicates to one row per core project, keeping the most recent fiscal
year, and writes a JSON the site renders."""

import os
import json
import time
import datetime
import urllib.request

TERM = os.environ.get("GENE_TERM", "SCN2A")
URL = "https://api.reporter.nih.gov/v2/projects/search"
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "docs", "data", "scn2a_grants.json")
PAGE = 100
MAX_PAGES = 10


def query(offset):
    body = {
        "criteria": {
            "advanced_text_search": {
                "operator": "and",
                "search_field": "projecttitle,terms,abstracttext",
                "search_text": TERM,
            }
        },
        "include_fields": [
            "ProjectNum", "CoreProjectNum", "ProjectTitle", "FiscalYear",
            "Organization", "ContactPiName", "AwardAmount", "AgencyIcAdmin",
            "ProjectDetailUrl",
        ],
        "offset": offset,
        "limit": PAGE,
        "sort_field": "fiscal_year",
        "sort_order": "desc",
    }
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        URL, data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json",
                 "User-Agent": "scn2a-grants-harvest"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read())
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    grants = {}
    total = 0
    status = "ok"
    try:
        for p in range(MAX_PAGES):
            data = query(p * PAGE)
            results = data.get("results", [])
            if not results:
                break
            total = (data.get("meta") or {}).get("total", total)
            for g in results:
                core = g.get("core_project_num") or g.get("project_num")
                if not core:
                    continue
                org = (g.get("organization") or {}).get("org_name")
                ic = (g.get("agency_ic_admin") or {}).get("name")
                rec = {
                    "core_project_num": core,
                    "project_num": g.get("project_num"),
                    "title": g.get("project_title"),
                    "pi": g.get("contact_pi_name"),
                    "org": org,
                    "fiscal_year": g.get("fiscal_year"),
                    "agency_ic": ic,
                    "award_amount": g.get("award_amount"),
                    "url": g.get("project_detail_url"),
                }
                prev = grants.get(core)
                if not prev or (rec["fiscal_year"] or 0) > (prev["fiscal_year"] or 0):
                    grants[core] = rec
            if len(results) < PAGE:
                break
            time.sleep(0.3)
    except Exception as e:
        status = f"harvest failed: {e}"

    items = sorted(grants.values(),
                   key=lambda r: (-(r["fiscal_year"] or 0), (r.get("title") or "")))
    payload = {
        "term": TERM,
        "source": "NIH RePORTER",
        "generated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "status": status,
        "total_projects_matched": total,
        "distinct_core_projects": len(items),
        "grants": items,
    }
    with open(OUT, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"{len(items)} distinct grants from {total} matched projects ({status})")


if __name__ == "__main__":
    main()
