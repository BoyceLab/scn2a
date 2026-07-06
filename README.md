# Rare Disease Research Portfolio Map

A methodology and reusable entity-relationship schema for mapping the complete research portfolio of a rare disease patient advocacy organization: studies, datasets, publications, presentations, researchers, funders, cohorts, data types, and privacy-preserving participant overlap, as a single connected graph.

This repository is an MkDocs Material site that documents the framework and doubles as a template a foundation can fork to publish its own portfolio map..

## What is here

- A layered methodology (graph model, catalog, harmonization, patient overlap, governance).
- A complete entity-relationship schema: fourteen node types and sixteen edge types, each anchored to a persistent identifier and a governing standard.
- A machine-readable `schema.yaml` you can load into a graph loader or validation pipeline.
- Deep-dive pages on identifiers, data harmonization, patient overlap, dataset cataloging, implementation, and the existing consortia a foundation can join.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000.

## Build

```bash
mkdocs build --strict
```

The static site is written to `site/`.

## Deploy to GitHub Pages

This repository includes a GitHub Actions workflow at `.github/workflows/deploy.yml` that builds the site and publishes it on every push to `main`.

1. Push this repository to GitHub.
2. In the repository, open Settings, then Pages, and set the source to GitHub Actions.
3. Push to `main`. The site publishes automatically.

## Style conventions

- No em dashes in any content.
- "rare disease" is always two words and never hyphenated.

## Status

Version 0.1.0. The schema is complete and ready to instantiate. Content is a working scaffold intended to be extended with a specific organization's instantiated portfolio.
