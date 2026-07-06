# Data Harmonization Layer

Mapping which data types exist is only half the value. To pool or compare results across studies, the variables inside those data types must resolve to shared, controlled concepts. This layer is what turns a catalog into a research asset.

## The standards

**NINDS Common Data Elements.** The National Institute of Neurological Disorders and Stroke maintains [standardized data elements](https://www.commondataelements.ninds.nih.gov/) for neurological research, including a dedicated [Epilepsy set](https://www.commondataelements.ninds.nih.gov/Epilepsy). For developmental and epileptic encephalopathy genes, this set is directly applicable and gives an off-the-shelf vocabulary for seizure semiology, EEG findings, development, and outcomes.

**OMOP Common Data Model.** For tabular clinical and observational data, [OMOP](https://ohdsi.github.io/CommonDataModel/) provides a mature target model and standardized vocabularies. Harmonizing each study's clinical tables to OMOP makes them queryable with a shared analytic layer and comparable across studies.

**GA4GH Phenopackets and HPO.** For deep phenotyping, [Phenopackets](https://www.ga4gh.org/product/phenopackets/) version 2 packages a participant's phenotype, using [Human Phenotype Ontology](https://hpo.jax.org/) terms, alongside genomic findings in a portable, standard structure. This is the natural interoperability format for a gene-level community.

**ISO 11179 metadata registry.** The variable-level dictionary itself (every field in every study, with its definition and permitted values) is held in a metadata registry following the [ISO 11179](https://www.iso.org/search.html?q=11179) pattern, so that the mapping between a raw variable and its controlled concept is documented and auditable.

## How it appears in the schema

The harmonization layer is expressed by two node types and one edge:

- `DataType` represents a variable or family of variables as collected.
- `Concept` represents the controlled term it means.
- `mapped_to` connects them, with a mapping confidence qualifier.

A single data type, such as a monthly seizure count, can map to a NINDS CDE, a LOINC code, and an OMOP concept simultaneously. Recording all of these makes the same variable usable by collaborators working in different ecosystems.

## Practical sequence

1. Inventory every variable across studies into the metadata registry.
2. Map each variable to at least one controlled concept, starting with the Epilepsy CDE set and HPO for phenotype fields.
3. Flag unmapped or ambiguous variables for review rather than forcing a match.
4. Where a study already uses OMOP or Phenopackets, ingest its mappings directly rather than redoing them.
