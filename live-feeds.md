# Edge types

The relationships carry as much meaning as the nodes. Each edge has a direction, a cardinality, and, where relevant, qualifying attributes (for example the specific role a person plays on an activity).

## Relationship inventory

| Edge | From | To | Cardinality | Qualifiers |
|------|------|----|-------------|------------|
| `has_role` | Person | ResearchActivity | many-to-many | role (PI, co-I, analyst, coordinator, advocate) |
| `affiliated_with` | Person | Organization | many-to-many | start and end date |
| `funded_by` | ResearchActivity | Award | many-to-many | amount, period |
| `produces` | ResearchActivity | Dataset | one-to-many | |
| `results_in` | ResearchActivity | Publication or Presentation | one-to-many | |
| `enrolls` | ResearchActivity | Cohort | one-to-one | |
| `comprises` | Cohort | Participant | one-to-many | enrollment date, status |
| `describes` | Dataset | Cohort | many-to-one | |
| `contains` | Dataset | DataType | one-to-many | count, completeness |
| `uses` | Dataset | Instrument | many-to-many | |
| `has_specimen` | Dataset or Cohort | Biospecimen | one-to-many | sample type |
| `mapped_to` | DataType | Concept | many-to-many | mapping confidence |
| `governed_by` | Dataset or Cohort | DataUsePermission | many-to-one | |
| `uses_dataset` | Publication | Dataset | many-to-many | data citation |
| `accesses` | Person or Organization | Dataset | many-to-many | access tier, grant date, DUP satisfied |
| `same_as` | Participant | Participant | many-to-many | resolved by global identifier |

## The three edges that answer the hard questions

**`same_as` answers "which studies share participants."** It is the only edge that crosses the participant privacy boundary, and it is written exclusively by the linkage service, never by hand. Two `Participant` nodes get a `same_as` edge when their global identifiers or linkage tokens match. Counting distinct participants across studies then becomes a graph query over the connected components of `same_as`.

**`accesses` answers "who is using our data."** Every formal data-access grant becomes an edge from a Person or Organization to a Dataset, qualified by the access tier and whether the relevant DataUsePermission was satisfied. This turns "who has our data" from an email search into a query.

**`uses_dataset` answers "where has our data appeared in the literature."** Data citation edges connect publications back to the datasets they analyzed, closing the loop between an asset and its scholarly impact.

## Qualified edges

Several edges are reified, meaning the relationship itself carries attributes and can be treated as a node when needed. `has_role`, `accesses`, and `funded_by` are the common cases. In a property-graph store these are simply edge properties. In an RDF store they are modeled with an intermediate node (the CERIF pattern) or with RDF-star.
