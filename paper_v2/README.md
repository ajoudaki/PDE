# Response-memory paper draft

This directory contains the self-contained LaTeX draft extracted from
`studies/neural_response_memory_20260922`. It deliberately does not use or
inspect the separate `paper/` directory.

The main file is `paper.tex`. Build it from this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The scientific claim boundaries are part of the draft:

- the proved response-memory theorem is at fixed finite width and is uniform
  on every prescribed finite physical-time interval as the order tends to
  infinity;
- the initialized dense operators are retained exactly;
- the population-flow connection currently gives a diagonal consistency
  statement, not a width-uniform fixed-order theorem;
- empirical endpoint comparisons are finite numerical evidence, not proofs of
  the asymptotic order rates.

`review/` records the frozen-draft review, author response, and any independent
referee decision produced during this paper task.
