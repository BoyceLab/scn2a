# Dataset Catalog and Discovery

Each dataset needs a machine-readable, web-discoverable description so that collaborators and crawlers can find it and understand its shape without needing access to the data itself. This is the layer that makes a portfolio Findable in the FAIR sense.

## The standards

**DCAT.** The [W3C Data Catalog Vocabulary](https://www.w3.org/TR/vocab-dcat-3/) is the backbone for describing datasets, their distributions, and the catalog that holds them. It is the interoperable structure most research data catalogs speak.

**Bioschemas Dataset.** A [life-science profile](https://bioschemas.org/) of schema.org that makes dataset descriptions discoverable by general and specialized search engines when embedded in a web page.

**RO-Crate.** A [lightweight way](https://www.researchobject.org/ro-crate/) to package a dataset together with its metadata and provenance into a single portable object, useful when a dataset moves between systems or is deposited in a repository.

**HL7 FHIR ResearchStudy and ResearchSubject.** When the portfolio needs to interoperate with clinical systems, [these resources](https://www.hl7.org/fhir/researchstudy.html) model the study and its enrollment in a standard clinical exchange format.

## What a catalog entry records

For each `Dataset` node, the catalog entry captures at minimum:

- Title, description, and DataCite DOI
- The producing `ResearchActivity` and its people
- The `Cohort` it describes and the `DataType` list it contains
- The `Instrument` set used to generate it
- The `DataUsePermission` that governs it and the access tier required
- Provenance: version, date, and the pipeline that produced it

## Discovery in practice

Embedding Bioschemas markup on a public catalog page means a new dataset becomes findable through search without any manual submission to an index. Minting a DataCite DOI at the same time makes it citable, which closes the loop with the `uses_dataset` edges that track scholarly reuse. For a small organization this combination, a DOI plus a marked-up catalog page, delivers most of the discoverability benefit for very little ongoing effort.
