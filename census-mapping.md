# Machine-readable schema

The full model is available as a single YAML file you can download, version, and load directly into a graph loader or validation pipeline.

[:material-download: Download schema.yaml](schema.yaml){ .md-button .md-button--primary }

The file defines every node type (with its persistent identifier scheme and governing standards) and every edge type (with direction, cardinality, and qualifiers). It is intentionally small enough to review in one sitting and to keep under version control alongside the data it describes.

## Full definition

```yaml
--8<-- "schema/schema.yaml"
```

## Using it

- **Validation.** Treat the YAML as the contract. A loader can check that every node instance carries a valid identifier of the declared scheme and that every edge connects the declared node types.
- **Code generation.** The node and edge definitions map directly onto a property-graph model (Neo4j labels and relationship types), an RDF vocabulary, or relational tables.
- **Documentation.** This site is generated from the same conceptual model, so the schema and the prose stay in step.

See [Implementation](../implementation.md) for how to instantiate the schema at three levels of effort.
