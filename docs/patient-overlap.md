# Patient Overlap Layer

This is the most sensitive and technically demanding layer, and it is the one that answers "which of our studies contain the same people." Participant lists cannot simply be merged, because that would pool identifying information across efforts that were consented separately. The solution is a study-agnostic identity layer that reveals overlap without revealing identity.

## The core technique

Give each participant a key that is stable across studies but carries no identifying information, so that the same person produces the same key wherever they appear. Three established approaches:

**Global unique identifiers.** The NINDS or NIH GUID generates a study-agnostic identifier by applying a one-way hash to a set of stable personal identifiers. The same person entered at two different sites produces the same GUID, so overlap is detectable, but the GUID cannot be reversed to recover identity. This system is already in use across neurological and epilepsy research, which makes it a natural fit for a gene community.

**Privacy-preserving record linkage.** PPRL uses Bloom filter or cryptographic hashing so that two sites can determine whether they share a participant without either revealing its records. This is the model used by large research networks and public health systems.

**Tokenization.** Commercial services (for example Datavant) issue de-identified tokens that serve the same overlap-detection purpose across data holders.

For genotype and phenotype level matching, rather than identity matching, the relevant protocols are GA4GH Matchmaker Exchange and Beacon.

## A federated architecture

Overlap detection does not require a central pool of participant data. The recommended pattern is:

1. Each study computes the privacy-preserving key for each of its participants locally.
2. Each study reports only its set of keys (not records) to a central overlap registry.
3. The registry computes intersections and writes `same_as` edges between the matching `Participant` nodes.
4. Distinct participant counts across the portfolio then come from the connected components of the `same_as` graph.

No raw identifiers ever leave a study, and the central registry never holds anything beyond opaque keys and the overlap graph.

## Governance is not optional

Even overlap detection touches consented human data, so this layer is wrapped in governance:

- Every dataset and cohort carries a `DataUsePermission` node expressed with the GA4GH Data Use Ontology, stating what the data may be used for.
- A data access committee reviews and records access decisions as `accesses` edges, qualified by whether the relevant permission was satisfied.
- The participant privacy boundary is absolute: the `Participant` node holds only the opaque key, and identity resolution lives entirely in the linkage service, outside the portfolio graph.

## What this delivers

Once the layer is in place, a foundation can answer questions that were previously impossible without breaching privacy: how many distinct individuals its research actually covers, which studies could be linked for a combined analysis, and where a participant burden is concentrated because the same families appear in many studies.
