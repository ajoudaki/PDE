# Archive

This directory is the immutable provenance layer.

- [`bundles`](bundles/) contains one copy of every original ZIP release used by
  the project, including the dated master reproduction collection.
- [`earlier_documents`](earlier_documents/) contains superseded project-wide
  syntheses and reports.

The active, readable decompressions are organized by research question under
[`../studies`](../studies/). Do not edit the ZIP bundles in place.

Run the following from this directory to verify the archived bytes:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

