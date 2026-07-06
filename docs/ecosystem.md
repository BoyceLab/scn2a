# Turnkey Ecosystem

Much of this framework already exists as shared infrastructure that a rare disease foundation can join rather than build from scratch. Building the schema in-house and joining a consortium are not mutually exclusive: the schema gives an organization a coherent internal map, and the consortia below can supply the biobank, the linkage service, and the harmonization standards that would otherwise take years to stand up.

## COMBINEDBrain

A pre-competitive consortium led by patient advocacy organizations, focused on shared outcome measures and biomarkers for rare genetic neurodevelopmental disorders. It has grown to well over one hundred member communities and operates shared research infrastructure including biobanking, data integration platforms, and expert access programs. Members contribute data and biospecimens and participate in cross-disease initiatives, and the consortium uses a central research identifier to link participants across member studies, which supplies the patient-overlap layer of this framework directly. Several gene-level neurodevelopmental foundations similar to a KCNT1 or SCN2A community are already members, so it is worth checking membership before building overlap infrastructure independently.

## Critical Path Institute RDCA-DAP

The Rare Disease Cures Accelerator Data and Analytics Platform aggregates and standardizes rare disease datasets, which is precisely the harmonization function of Layer 3. Contributing a study's data to a platform that already standardizes to shared models reduces the internal harmonization burden.

## CZI Rare As One

The Chan Zuckerberg Initiative's Rare As One network builds capacity among patient-led organizations, including data and research infrastructure support. It is a route to funding and shared tooling for the kind of portfolio mapping this framework describes.

## GA4GH

The Global Alliance for Genomics and Health provides the standards that several layers of this framework depend on: Phenopackets and HPO for phenotype harmonization, the Data Use Ontology for governance, and Matchmaker Exchange and Beacon for genotype and phenotype matching. A foundation does not join GA4GH so much as adopt its standards, which keeps the portfolio interoperable with the wider genomics community.

## NCATS resources

The National Center for Advancing Translational Sciences maintains a Toolkit for Patient-Focused Therapy Development and the GARD information resource, both of which offer practical guidance for registries and research infrastructure at the advocacy-organization scale.

## How to combine them

A pragmatic path for a small foundation:

1. Build the internal portfolio map from this schema at Level 1, so the organization has a coherent picture of its own assets.
2. Join a consortium such as COMBINEDBrain for biobanking and cross-study participant linkage, and record the consortium's participant keys as the overlap layer.
3. Adopt GA4GH standards for phenotype harmonization and governance so the internal map stays interoperable.
4. Contribute standardized datasets to an aggregating platform to extend reach and reduce internal harmonization work.
