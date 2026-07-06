# Node types

Fourteen node types cover the full research portfolio of a rare disease advocacy organization. Each is anchored to a persistent identifier scheme and one or more governing standards.

## Core research information nodes

| Node | Description | Primary identifier | Governing standard |
|------|-------------|--------------------|--------------------|
| **ResearchActivity** | A study, project, or protocol. The organizing unit of the portfolio. | <span class="pid-badge">RAiD</span> (ISO 23527) | CERIF Project; FHIR ResearchStudy |
| **Person** | An investigator, analyst, clinician, or advocate. | <span class="pid-badge">ORCID</span> | VIVO Person; FOAF |
| **Organization** | An institution, foundation, sponsor, or site. | <span class="pid-badge">ROR</span> | CERIF OrgUnit |
| **Award** | A grant or funding instrument, and the funder behind it. | <span class="pid-badge">Grant DOI</span>; Crossref Funder ID | CERIF Funding; Open Funder Registry |
| **Publication** | A journal article, preprint, or report. | <span class="pid-badge">Crossref DOI</span> | CERIF Publication; schema.org ScholarlyArticle |
| **Presentation** | A conference talk, poster, or slide deck. | <span class="pid-badge">DOI</span> (via Zenodo or Figshare) | schema.org PresentationDigitalDocument |

## Data and cohort nodes

| Node | Description | Primary identifier | Governing standard |
|------|-------------|--------------------|--------------------|
| **Dataset** | A data asset produced by an activity. | <span class="pid-badge">DataCite DOI</span> | DCAT; Bioschemas Dataset; RO-Crate |
| **Cohort** | The population enrolled in a study. | Local cohort ID | FHIR Group; OMOP cohort definition |
| **Participant** | An individual, represented only by a privacy-preserving key. Never PII. | <span class="pid-badge">NINDS GUID</span>; PPRL token | GA4GH; FHIR ResearchSubject |
| **DataType** | A kind of data collected (genomic, clinical scale, EEG, imaging, patient-reported outcome, biospecimen). | Local ID mapped to concept | NINDS CDE; ISO 11179 |
| **Biospecimen** | A physical sample held in a biobank. | Biobank accession; <span class="pid-badge">RRID</span> for resources | MIABIS; GA4GH |
| **Instrument** | A sequencing platform, assay panel, or assessment instrument. | <span class="pid-badge">RRID</span> | OBI (Ontology for Biomedical Investigations) |

## Semantic and governance nodes

| Node | Description | Primary identifier | Governing standard |
|------|-------------|--------------------|--------------------|
| **Concept** | A controlled clinical concept or phenotype that a DataType maps to. | <span class="pid-badge">HPO / OMOP / LOINC / SNOMED</span> | GA4GH Phenopackets |
| **DataUsePermission** | The consent terms and permitted uses attached to a dataset or cohort. | Local ID | GA4GH Data Use Ontology (DUO) |

## Notes on selected nodes

**ResearchActivity.** RAiD is the ISO standard research activity identifier and is purpose-built to bind an activity to its people, organizations, outputs, and instruments over time, which makes it the natural key for the whole portfolio.

**Participant.** This node is the privacy boundary of the entire model. It holds a one-way key only. All identity resolution happens outside the graph in the linkage service described on the [Patient Overlap Layer](../patient-overlap.md) page.

**DataType and Concept.** Keeping these as two separate nodes, with a `mapped_to` edge between them, is what turns a list of variables into a harmonization asset. A single DataType such as a seizure frequency scale can map to several concepts across coding systems.
