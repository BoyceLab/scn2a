# Researchers

This is the SCN2A researcher list, harvested automatically from publication authorship and keyed on ORCID. It is the self-populating source for the `Person` nodes of the portfolio. Each researcher links to their ORCID record, and the list is ranked by how many SCN2A works they have authored.

[:material-download: Download Person nodes (CSV)](data/scn2a_person_nodes.csv){ .md-button }

<div class="feed-panel" markdown="0" style="max-width:640px">
  <h3>SCN2A researchers by ORCID</h3>
  <div class="feed-body" id="feed-researchers" style="max-height:640px"></div>
</div>

## How the list is built

A scheduled job queries [OpenAlex](https://openalex.org/) for works whose title or abstract mentions SCN2A, walks every authorship, and collects the distinct authors that carry an ORCID. For each person it records the number of SCN2A works and the institutions seen on those works, then ranks by work count. The job writes two files: a JSON that this page renders, and a CSV of `Person` nodes ready to load into the graph.

ORCID coverage in the literature is good but not complete, so the harvest also counts authors who appear without an ORCID. Those are real researchers the graph cannot key yet; they are candidates for manual ORCID lookup or for outreach to add their ORCID.

## Running it yourself

The harvester is a single standard-library Python script, so it runs anywhere:

```bash
# optional: join the faster OpenAlex polite pool
export OPENALEX_MAILTO="you@example.org"
python scripts/harvest_orcids.py
```

It writes `docs/data/scn2a_researchers.json` and `docs/data/scn2a_person_nodes.csv`. In this repository it also runs on a schedule through the deploy workflow, so the list refreshes without any manual step. Change the `GENE_TERM` environment variable to point the same harvester at any other gene.

## Complementary sources

OpenAlex gives the broadest authorship coverage in one call, which is why it is the default. Two others can be layered in if you want more completeness:

- **ORCID public API** expanded search, to find researchers who list SCN2A in their own record even if a given paper did not attach their ORCID.
- **Europe PMC** and **Crossref**, which also expose author ORCIDs per work and can be cross-checked against the OpenAlex result to fill gaps.

For how these ORCIDs become graph nodes and connect to publications and studies, see [Identifier and Standards Registry](identifiers.md) and the [Entity-Relationship Schema](schema/index.md).
