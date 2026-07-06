# Identifier and Standards Registry

Persistent identifiers are the mechanism that lets the portfolio graph populate itself. When every entity carries a standard identifier, records from different sources merge deterministically and public metadata services can fill in most of the graph.

## The identifier backbone

| Entity | Identifier | Issued by | What it unlocks |
|--------|-----------|-----------|-----------------|
| ResearchActivity | RAiD | Research activity registries (ISO 23527) | Binds an activity to its people, orgs, outputs, and instruments over time |
| Person | ORCID | ORCID | Disambiguated researchers; auto-linked publications and affiliations |
| Organization | ROR | ROR community | Disambiguated institutions and funders |
| Award | Crossref Funder ID; grant DOI | Crossref; DataCite | Links funding to outputs |
| Publication | DOI | Crossref | Auto-harvest of the publication record |
| Dataset | DOI | DataCite | Citable, discoverable data assets |
| Presentation | DOI | Zenodo, Figshare | Citable talks and posters |
| Resource or Instrument | RRID | SciCrunch | Reproducible reference to reagents, tools, and platforms |
| Participant | GUID or PPRL token | Study or linkage service | Overlap detection without PII |
| Concept | HPO, OMOP, LOINC, SNOMED | Respective vocabularies | Cross-study harmonization |

## Self-population strategy

Most of the graph can be built without manual data entry:

1. **Seed with ORCID.** Collect the ORCID of every collaborating researcher. ORCID records carry their publications, affiliations, and grants.
2. **Expand through Crossref and DataCite.** Each publication and dataset DOI resolves to structured metadata, including authors (as ORCIDs), funders, and, increasingly, data citations.
3. **Resolve organizations with ROR.** Affiliation strings map to ROR identifiers, collapsing duplicate institution nodes.
4. **Register activities with RAiD.** Minting a RAiD for each study gives the portfolio a stable spine that the other identifiers hang from.

What remains for manual curation is small: the cohort, data type, biospecimen, and governance nodes, plus the participant overlap keys, which by design never come from public sources.

## Why this matters for a small organization

A foundation rarely has staff to maintain a database by hand. Anchoring on identifiers turns portfolio mapping from a data-entry burden into a harvesting and reconciliation task, which is far more sustainable and keeps the map current as new outputs appear.
