# Implementation

The schema can be instantiated at three levels of effort. A foundation should start at the lightest level that answers its current questions and grow only as needed. Every level uses the same schema, so work at one level is never wasted when moving to the next.

## Step zero: the research asset inventory

Before choosing any technology, run a structured landscape scan. This is a single deliberate pass that produces the initial node set.

1. Define a fixed data-extraction template with one row per research asset and columns matching the node attributes (title, type, identifier, people, dates, associated dataset, associated publication).
2. Work through every known study, dataset, publication, presentation, and collaborator, extracting into the template.
3. Have a second person check a sample for accuracy, as in a scoping review.
4. Assign persistent identifiers to everything that has one, and record the gaps.

This template alone, even in a spreadsheet, is a usable first version of the map and is enough to answer the "what do we have" question.

## Level 1: curated store

Load the inventory into a structured but low-maintenance store. Good options are Airtable, Baserow, or a Wikibase instance. Model each node type as a table and each edge as a link field. This level suits a foundation that wants a shared, queryable map without engineering overhead. The `same_as` overlap edges can be added manually from a linkage service export.

## Level 2: property graph

Load the schema into a property-graph database such as Neo4j. Node types become labels, edge types become relationship types, and qualifiers become properties. This level makes the interesting queries natural: distinct participant counts across `same_as`, data reuse across `uses_dataset`, and access history across `accesses`. It suits an organization with some data engineering capacity and a growing portfolio.

## Level 3: semantic knowledge graph

Express the schema as an RDF vocabulary aligned to CERIF and VIVO, and load it into a triplestore. This level maximizes interoperability and lets the portfolio federate with external research information systems and with the broader linked-data ecosystem. Reified edges use the CERIF intermediate-node pattern or RDF-star. This suits an organization that intends to publish its portfolio as linked open data or integrate with institutional systems.

## Populating and maintaining the graph

Regardless of level, the maintenance loop is the same:

1. Harvest new publications and datasets from Crossref and DataCite using the ORCIDs of collaborators.
2. Reconcile organizations to ROR and people to ORCID.
3. Refresh the overlap graph from the linkage service on a schedule.
4. Review unmapped data types and new datasets for concept mapping and governance tagging.

Because the harvesting steps are automatable, ongoing maintenance is mostly reconciliation and curation of the small set of nodes that cannot come from public sources.

## This site as a template

This documentation site is itself built with MkDocs Material and deploys to GitHub Pages through a GitHub Actions workflow, so it doubles as a starting template. A foundation can fork the repository, replace the content with its own instantiated schema and catalog, and publish its portfolio map as a living site.
