# Fresh pair-median run integrity record

The frozen initialization-only experiment completed with status `pass`.
No positive-time trajectory was simulated.

## Frozen inputs

```text
199199a6f898c40225d0e093473ebda5362dfbfcb09871dd5d54a2a46bd71cdc  empirical_redesign/FRESH_PAIR_MEDIAN_PROTOCOL.md
f724307b9bbe0c7a2b7cd8f29d0cf42d86169dd8f710185bff9eb9c63603f0cf  empirical_redesign/run_fresh_pair_median.py
```

These equal the hashes recorded before approval and the hashes embedded in
`results.json`.

## Immutable primary outputs

```text
3246a4879c7b41739830a05c842517bc97efc07486e47631d5f50a5e61616484  results.json
1e88f22435eb61c8e68f59bda44ca1d327193d3f9430ecc715ebc65773d30026  pair_values_width_128.npz
10c90d5668de24ebba9ab516e6780d4da0eaa173f6d90fca2cb747ee8d3371a3  pair_values_width_256.npz
```

Both raw archives contain exactly 224 finite `f5` values and their 224
deterministically transformed `q` values.  Recomputing each sample median from
the archives reproduces the value in `results.json` exactly.

## Resource audit

- Recorded peak resident memory: `154000 KiB` (about 150.4 MiB).
- Frozen address-space cap: `8589934592` bytes (8 GiB).
- Frozen thread cap: six.
- Python: 3.10.14; NumPy: 1.26.4.

## Exact confidence-interval audit

For `N=224`, the exact distribution-free interval uses order statistics 97
and 128.  Its exact coverage is

```text
0.9619043737477264
```

The next narrower symmetric interval would fall below the required 95%
coverage, so the index selection is correct.
