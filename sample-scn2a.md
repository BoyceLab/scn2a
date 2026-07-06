# Key informatics

This page is the informatics and data-standards layer for SCN2A: the identifiers, controlled vocabularies, ontology codes, variant and curation databases, and encoding standards a data team needs to make an SCN2A dataset findable, interoperable, and poolable.

!!! note "This page connects to FamilieSCN2A, it does not replace it"
    The [FamilieSCN2A Foundation](https://www.scn2a.org/) is the home of the SCN2A community and already provides clinical care guidance, a curated publications list, the research network and advisory board, registries, multidisciplinary care centers, and family resources. This page deliberately does not duplicate any of that. It adds the machine-actionable reference layer and links back to FamilieSCN2A for everything else. For clinical information, start at the FamilieSCN2A [Clinical Information](https://www.scn2a.org/scn2a-related-disorders/clinical-information/) page.

## Canonical gene identifiers

The keys every SCN2A record should carry. Using these makes datasets mergeable and lets the portfolio self-populate from public sources.

| Resource | Identifier | Link |
|----------|-----------|------|
| Gene symbol (HGNC) | HGNC:10588, symbol SCN2A | [genenames.org](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10588) |
| NCBI Gene (Entrez) | 6326 | [ncbi.nlm.nih.gov/gene/6326](https://www.ncbi.nlm.nih.gov/gene/6326) |
| Ensembl gene | ENSG00000136531 | [Ensembl](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136531) |
| UniProt protein (Nav1.2) | Q99250 | [uniprot.org/uniprotkb/Q99250](https://www.uniprot.org/uniprotkb/Q99250/entry) |
| OMIM gene | 182390 | [omim.org/entry/182390](https://omim.org/entry/182390) |
| Cytogenetic location | 2q24.3 (GRCh38 chr2:165,239,414-165,392,304, forward) | |
| Protein aliases | Nav1.2, HBSCI, HBSCII, SCN2A1, SCN2A2 | |

## Reference sequence and coordinates

Pin variant calls to one transcript so results are comparable across studies. The MANE Select transcript is the community default and is annotated identically by NCBI and Ensembl.

| Item | Value |
|------|-------|
| MANE Select transcript (RefSeq) | NM_001040142.2 |
| MANE Select protein (RefSeq) | NP_001035232.1 |
| Ensembl transcript / protein | ENST00000375437 / ENSP00000364586 |
| CCDS | CCDS33314 |
| Genome build | GRCh38 (report GRCh37 liftover separately if used) |

Note the alternative neonatal transcript exists (SCN2A has developmentally regulated splice isoforms), so always record which transcript a variant was called against.

## Disease and phenotype ontologies

The crosswalk that lets SCN2A phenotypes map to shared concepts for pooling. See the [Data Harmonization Layer](data-harmonization.md) for how these attach to the schema.

| System | Concept | Code |
|--------|---------|------|
| OMIM | Developmental and epileptic encephalopathy 11 (DEE11) | [613721](https://omim.org/entry/613721) |
| OMIM | Benign familial neonatal-infantile seizures (BFIS3) | [607745](https://omim.org/entry/607745) |
| Orphanet | Early infantile developmental and epileptic encephalopathy | ORPHA:1934 |
| Orphanet | Epilepsy of infancy with migrating focal seizures | ORPHA:293181 |
| Orphanet | Infantile epileptic spasms syndrome | ORPHA:697160 |
| Orphanet | Dravet syndrome | ORPHA:33069 |
| Orphanet | Self-limited (neonatal-)infantile epilepsy | ORPHA:140927, ORPHA:306 |
| Orphanet | Alternating hemiplegia of childhood | ORPHA:2131 |
| MONDO | Cross-ontology disease equivalences | search the [EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols4/) |

The full gene-to-disease list is on the [Orphanet SCN2A gene page](https://www.orpha.net/en/disease/gene/SCN2A).

Example HPO terms for encoding SCN2A phenotypes: Seizure (HP:0001250), Autistic behavior (HP:0000717), Global developmental delay (HP:0001263), Intellectual disability (HP:0001249), and Hypotonia (HP:0001252). HPO is the recommended phenotype vocabulary for GA4GH Phenopackets.

## Clinical coding and terminology

| System | Concept | Code |
|--------|---------|------|
| ICD-10-CM (FY2026, effective 2025-10-01) | SCN2A-related neurodevelopmental disorder | QA0.0101 |
| ICD-10-CM parent | Neurodevelopmental disorders related to ion channel gene variants | QA0.010 |
| SNOMED CT | Map via UMLS Metathesaurus | resolve through [UMLS](https://www.nlm.nih.gov/research/umls/) |
| OMOP standard concept | Derive by mapping ICD-10-CM, SNOMED, and HPO through OHDSI [Athena](https://athena.ohdsi.org/) | |

The ICD-10-CM code QA0.0101 is new, gene-specific, and is used **in addition to** the codes for associated conditions such as autism (F84.0), epilepsy (G40.-), and developmental and epileptic encephalopathy (G93.45). FamilieSCN2A led the four-year advocacy effort that secured it; their [ICD-10 code page](https://www.scn2a.org/scn2a-related-disorders/icd-10-code/) has provider guidance. Recording QA0.0101 in the EHR is the single most impactful step for making SCN2A cohorts discoverable in health-system data.

## Variant and curation databases

Gene-scoped entry points for variant-level work. These are the machine-actionable databases, complementary to the curated, patient-facing links FamilieSCN2A maintains.

| Database | Purpose | Gene-scoped link |
|----------|---------|------------------|
| ClinGen gene record | Gene-disease validity and expert curation | [clinicalgenome.org (HGNC:10588)](https://search.clinicalgenome.org/kb/genes/HGNC:10588) |
| ClinGen dosage sensitivity | Haploinsufficiency and triplosensitivity | [dosage curation](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:10588) |
| ClinVar | Submitted variant classifications | [ClinVar SCN2A](https://www.ncbi.nlm.nih.gov/clinvar/?term=SCN2A%5Bgene%5D) |
| gnomAD | Population allele frequencies and constraint | [gnomAD ENSG00000136531](https://gnomad.broadinstitute.org/gene/ENSG00000136531) |
| LOVD | Locus-specific variant database | [LOVD SCN2A](https://databases.lovd.nl/shared/genes/SCN2A) |
| DECIPHER | Genotype and phenotype, copy number | [DECIPHER SCN2A](https://www.deciphergenomics.org/gene/SCN2A) |
| SFARI Gene | Autism gene evidence (Simons) | [gene.sfari.org SCN2A](https://gene.sfari.org/database/human-gene/SCN2A) |
| Geisinger DBD Genes | Developmental brain disorder gene database | [dbd.geisingeradmi.org](https://dbd.geisingeradmi.org/) |

A recurring, clinically meaningful axis in SCN2A variant work is functional direction: gain of function, loss of function, or mixed. This distinction shapes phenotype and treatment and should be captured as a structured attribute on the variant, not left in free text. FamilieSCN2A summarizes the clinical significance of this axis on their Clinical Information page.

## Standards for encoding an SCN2A dataset

To make an SCN2A cohort interoperable, encode it with these standards rather than local conventions:

- **HGVS nomenclature** for every variant, always paired with the MANE transcript above.
- **GA4GH Variation Representation Specification (VRS)** for computable, normalized variant identifiers, and the **ClinGen Allele Registry** for canonical allele IDs.
- **GA4GH Phenopackets v2 with HPO** for phenotypes, which is the natural exchange format for a gene community and connects directly to the schema.
- **HL7 FHIR Genomics** (Genomics Reporting Implementation Guide) when exchanging with clinical systems.
- **OMOP CDM** for tabular clinical harmonization, with concepts resolved through Athena.

This is the same harmonization approach described in the [Data Harmonization Layer](data-harmonization.md), applied to SCN2A specifically.

## Studies and community hubs

For studies, collaborator labs, publications, and family resources, connect to the organizations that own them rather than re-listing them here.

- **[FamilieSCN2A Foundation](https://www.scn2a.org/)**: the central hub. See their [Research](https://www.scn2a.org/research/) section, [Research Network](https://www.scn2a.org/research/research-network/) for collaborating labs and the advisory board, [Key Publications](https://www.scn2a.org/research/key-publications/), and [Clinical Trials and Research Opportunities](https://www.scn2a.org/research/clinical-trials-and-research-opportunities-2/).
- **DRAGONFLY Study**: the FamilieSCN2A patient registry and natural history study on NORD's IAMRARE platform, reached through the FamilieSCN2A research pages.
- **[Simons Searchlight, SCN2A](https://www.simonssearchlight.org/research/what-we-study/scn2a/)**: ongoing registry and dataset.
- **Citizen Health**: patient-mediated longitudinal record aggregation for SCN2A, supported by FamilieSCN2A.
- **Regional communities**: SCN2A Australia (Asia-Pacific), SCN2A Europe, and the SCN2A Foundation, all linked from Simons Searchlight and FamilieSCN2A.

For current publications, preprints, and trials pulled live, see the [Live feeds](live-feeds.md) page, which is keyed on the same identifiers listed above.
