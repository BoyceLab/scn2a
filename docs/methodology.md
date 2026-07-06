# Methodology

The framework is deliberately layered so that a foundation can adopt it incrementally. Each layer is independently useful, and each one depends only on the layers beneath it.

## Layer 1: Graph model and identifiers

The entities a foundation cares about (activities, people, publications, presentations, funders) are exactly what a Research Information Management System models. Two mature data models exist for this:

- **CERIF** ([Common European Research Information Format](https://eurocris.org/services/main-features-cerif)), the standard data model most current research information systems are built on. It models projects, persons, organizations, publications, products, and funding, and critically the time-bound relationships between them.
- **[VIVO](https://vivoweb.org/)** and its VIVO-ISF ontology, an open-source, semantic-web representation of scholarship. It is realistically sized for a foundation rather than a university and can ingest ORCID and Crossref directly.

The real leverage is persistent identifiers used as the glue between nodes. Once every entity carries a standard identifier, the graph becomes largely self-populating from public metadata. See the [Identifier and Standards Registry](identifiers.md) for the full mapping.

## Layer 2: Dataset catalog and discovery

Each dataset gets a machine-readable, web-discoverable description so that people and crawlers can find it and understand its shape without access to the data itself. The standards are [DCAT](https://www.w3.org/TR/vocab-dcat-3/) for the catalog structure, [Bioschemas](https://bioschemas.org/) Dataset profiles for web discoverability, and [HL7 FHIR](https://www.hl7.org/fhir/) ResearchStudy and ResearchSubject when interoperability with clinical systems matters. See [Dataset Catalog and Discovery](dataset-catalog.md).

## Layer 3: Data harmonization

Listing data types is not enough. To pool or compare results, the variables themselves must map to shared concepts. The framework uses the [NINDS Common Data Elements](https://www.commondataelements.ninds.nih.gov/) (which include a dedicated [Epilepsy set](https://www.commondataelements.ninds.nih.gov/Epilepsy), directly relevant to developmental and epileptic encephalopathy genes), [OMOP CDM](https://ohdsi.github.io/CommonDataModel/) for tabular clinical harmonization, and [GA4GH Phenopackets](https://www.ga4gh.org/product/phenopackets/) with [HPO](https://hpo.jax.org/) for phenotype harmonization. An [ISO 11179](https://www.iso.org/search.html?q=11179) style metadata registry holds the variable-level dictionary. See [Data Harmonization Layer](data-harmonization.md).

## Layer 4: Patient overlap

This is the sensitive and technically hardest layer. Participant lists cannot be merged, so the framework introduces a study-agnostic identity layer: a global unique identifier or a privacy-preserving record-linkage token per participant. The same person then becomes detectable across studies without any identifying information being shared or pooled. See [Patient Overlap Layer](patient-overlap.md).

## Layer 5: Governance

Consent terms and data use permissions are modeled as first-class nodes using the [GA4GH Data Use Ontology](https://www.ga4gh.org/product/data-use-ontology-duo/), so that every dataset and cohort carries a machine-readable statement of what it may be used for and by whom. A data access committee governs the edges that grant researchers access to data. Governance is woven through the schema rather than bolted on.

## Where to start

The recommended first move is a research asset inventory conducted as a structured landscape scan, using a fixed data-extraction template. That single pass produces the initial node set. Persistent identifiers are then assigned and public sources harvested to fill most of the edges automatically. Full detail is on the [Implementation](implementation.md) page.
