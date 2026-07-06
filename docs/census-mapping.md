# Census to schema mapping

Most groups already keep some form of data census: a spreadsheet with one row per study or dataset. This page shows how a typical census maps onto the schema, so an existing inventory can be loaded rather than rebuilt. The column names below follow a common census layout; adjust to match your own headers.

## Column mapping

| Census column | Schema target | Notes |
|---------------|---------------|-------|
| Name of Study | `ResearchActivity` node | Assign a RAiD as the key |
| Description of data | `Dataset` node | One dataset per data description; mint a DataCite DOI |
| Type of Data | `DataType` node, then `mapped_to` a `Concept` | Map to NINDS CDE, HPO, or OMOP concept |
| n | `Cohort` size | Attribute on the `enrolls` edge or the `Cohort` node |
| CRID | `Participant` overlap key | Consortium research identifier; drives `same_as` |
| GUID | `Participant` overlap key | Global unique identifier; drives `same_as` |
| Publications | `Publication` nodes, `uses_dataset` edges | Resolve to Crossref DOIs |
| Dictionary | Metadata registry entry | The ISO 11179 variable dictionary for the dataset |
| Consent | `DataUsePermission` node | Model terms with the GA4GH Data Use Ontology |
| IRB | `DataUsePermission` attribute | Approval reference, held internally |
| Protocol | `ResearchActivity` attribute | Protocol reference or document |
| Longitudinal | `Dataset` attribute | Boolean |
| Prospective / Retro | `Dataset` attribute | Design flag |
| Location | `Organization` node | Resolve site or institution to ROR |
| Ownership / Restrictions | `DataUsePermission` node | Governs the `accesses` edge |
| Shared internally | `accesses` edge (internal tier) | Who inside the organization can use it |
| Shared externally | `accesses` edge (external tier) | External partners and platforms |
| Link to agreements | Internal attribute only | See the handling note below |

## Handling links and restrictions

Census spreadsheets often store live links in the Consent, IRB, and agreement columns, pointing to Google Drive, Google Docs, or PDF stores, along with partner names and sharing restrictions in free text. These belong to the private instantiation and must not appear on a public site.

The rule this framework follows:

- **Links to agreements, consent forms, IRB folders, and protocols are internal attributes.** They are kept in the private instantiation and are never published. The public map records only that a governing permission exists, not where the document lives.
- **Partner names and negotiated restrictions stay internal.** The public map can state that a dataset is shareable or restricted, without naming the partner or reproducing the restriction language.
- **Overlap keys never resolve to identity.** CRID and GUID values are opaque keys. They enable `same_as` edges but are not themselves identifying, and they are handled by the linkage service.

## Loading sequence

1. Read the census and create one `ResearchActivity` per study and one `Dataset` per data description.
2. Map each Type of Data value to a controlled `Concept`.
3. Attach cohort sizes, design flags, and location.
4. Create `DataUsePermission` nodes from the Consent, IRB, and Ownership columns, keeping any document links as internal attributes.
5. Record overlap keys on `Participant` nodes and let the linkage service write `same_as` edges.
6. Resolve publications to DOIs and add `uses_dataset` edges.

The result is the graph shown on the [SCN2A example](sample-scn2a.md) page. A worked internal instantiation of a real census is delivered as a private file and is deliberately excluded from this repository.
