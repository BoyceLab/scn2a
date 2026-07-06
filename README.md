# Rare Disease Research Portfolio Map

A methodology and reusable entity-relationship schema that lets a rare disease patient advocacy organization map its entire research footprint: every study, dataset, publication, presentation, researcher, funder, cohort, and the participant overlap between studies, as a single connected graph.

## The problem this solves.

A gene-level foundation (for example a KCNT1 or SCN2A community) typically accumulates research across many independent efforts: academic collaborators, natural history studies, a patient registry, a biobank, genomic datasets, clinical scales, conference posters, and journal articles. That footprint is usually scattered across spreadsheets, inboxes, and individual investigators' heads. Three questions are hard to answer as a result:

1. What research assets do we actually have, and who is using them?
2. Which studies contain the same participants, so that overlap and double counting can be understood without exposing anyone's identity?
3. Are our data types comparable across studies, so results can be pooled?

This framework treats all three as one problem: a **research information management (RIM) graph** with a **privacy-preserving cohort-overlap layer** on top of it.

## The core idea

Model everything as a graph of typed nodes and typed edges, governed by the FAIR principles, and attach each node to a standard persistent identifier and metadata standard. Once the identifiers are in place, most of the graph can be populated automatically from public sources (ORCID, Crossref, DataCite, RAiD) rather than curated by hand.

## The layered methodology

<div class="layer-stack">
  <div class="layer"><strong>Layer 1. Graph model and identifiers.</strong> The backbone. Studies, people, organizations, outputs, and funding as typed nodes, each anchored to a persistent identifier (RAiD, ORCID, ROR, DOI).</div>
  <div class="layer"><strong>Layer 2. Dataset catalog and discovery.</strong> Machine-readable, web-discoverable descriptions of each dataset using DCAT, Bioschemas, and FHIR ResearchStudy.</div>
  <div class="layer"><strong>Layer 3. Data harmonization.</strong> Making data types comparable across studies with NINDS Common Data Elements, OMOP CDM, and GA4GH Phenopackets and HPO.</div>
  <div class="layer"><strong>Layer 4. Patient overlap.</strong> A privacy-preserving identity layer (global unique identifiers, record linkage, federated overlap detection) that reveals shared participants without sharing identity.</div>
  <div class="layer"><strong>Layer 5. Governance.</strong> Consent and data use permissions modeled explicitly with the GA4GH Data Use Ontology, plus a data access committee.</div>
</div>

## How to read this site

The [Methodology](methodology.md) page walks the layers in order. The [Entity-Relationship Schema](schema/index.md) section is the heart of the framework: the node types, the edge types, and a downloadable machine-readable schema. The remaining pages go deep on identifiers, harmonization, overlap, cataloging, implementation, and the existing turnkey infrastructure a small foundation can join rather than build.

!!! note "Status"
    This is a working framework scaffold. The schema is complete and ready to instantiate. The implementation pages describe build options at three levels of effort so a foundation can start with a lightweight inventory and grow into a full knowledge graph.
