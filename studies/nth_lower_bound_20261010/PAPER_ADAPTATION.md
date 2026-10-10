# NTH adaptation for the compact manuscript

The proposed include is `PAPER_NTH.tex`, intended to become
`paper/compact_nth.tex`. It is a separate benchmark section after the
compression assembly. It preserves the established storage theorem,
general upper-bound corollary, all five supporting lemmas, all six proof
bodies, and all 23 numbered equations. No scientific assertion or proof
dependency is omitted. No new experiment, theorem, or proof review was
undertaken.

The NTH result concerns literal ordered tensors, two trainable identity
hidden layers, a fixed short interval, and a growing-data hard family
with fixed positive label scale. Its assumptions are separate from the
compact paper's fixed-data small-label compression theorem. The opening
and closing paragraphs make this distinction explicit. The upper bound
still permits every deterministic dataset in its own stated setup,
including the exact-zero case. Both storage conventions and adaptive
order selection remain in the theorem.

## Exact manuscript edits

Only `paper/compact.tex` and the new `paper/compact_nth.tex` are needed.
The existing `paper/references.bib` already contains the usable key
`huang2020nth`; no bibliography entry or new package is needed.

1. In the abstract replace `This copy isolates the theorem and its proof:`
   with the following short addition and plural correction:

   ```tex
   A separate benchmark quantifies literal neural tangent hierarchy storage
   for short-time deep-linear training on growing datasets.
   This copy isolates the proofs:
   ```

2. Replace the global inheritance sentence with:

   ```tex
   Except for the independent benchmark in \Cref{cp:nth:storage}, all
   neural-network statements below inherit this setup and these probability
   conventions.
   ```

   Leave the following activation-evaluator accounting sentence intact.

3. After the paragraph ending `Zero labels give the stationary zero predictor
   instead.` and before `\input{feature_learning_theorem}`, add:

   ```tex
   A separate short-time benchmark for literal neural tangent hierarchy
   arrays appears in \Cref{cp:nth:storage}; its growing-data deep-linear
   assumptions are independent of \Cref{cp:headline}.
   ```

4. In the proof-architecture paragraph replace `The final section combines`
   with `\Cref{cp:assembly} combines`. This keeps the existing forward
   pointer correct after another section is appended.

5. Copy `PAPER_NTH.tex` exactly to `paper/compact_nth.tex`. After the existing
   assembly proof and immediately before `\end{document}`, insert:

   ```tex
   \input{compact_nth}

   \bibliographystyle{plain}
   \bibliography{references}
   ```

   Standard LaTeX `\cite` is sufficient. The include attributes the
   hierarchy to Huang and Yau using the existing key, without importing a
   theorem from their different parameterization. The bibliography should
   be generated with BibTeX as part of the coordinator's final build.

## Source and exact correspondence

Scientific inputs used were restricted to the maintained
`docs/07-observable-closure.qmd` section `sec-nth-storage` (lines 447–1024),
`docs/notation.qmd`, complete `paper/compact.tex`, the existing Huang–Yau
entry in `paper/references.bib`, and the corresponding compiled approved
book section. No existing compact proof module was needed or reused.
Required process and notation/proof skills were read. A scoped editorial
interface scan also read only the assigned compact manuscript and book
section; it wrote no files and performed no mathematical re-review.
One compiled-text display inadvertently overshot the section endpoint by
37 lines into the following established section; that passage was not used.
No other study or prior review was read.

The proof source used by the converter is exactly the section beginning
`Literal storage of a frozen-top neural tangent hierarchy` in
`data/generated/nth_lower_bound_20261010/promotion_v4/data/generated/DTDL/docs/DTDL.tex`,
lines 38888–39468. The source-section SHA-256 is
`765a7a3678d6760f3474ef8915799588444bb57a43164f219f090c6ce768c9c6`.
The final `PAPER_NTH.tex` SHA-256 is
`38e50dee3b89a755e4efb719a8cf3396cd70f78a1cf163dbf0ff91076505a616`.

The deterministic converter `PAPER_CONVERT.py` applies these changes:

| Book notation or structure | Compact include |
| --- | --- |
| Stored readout `W^{(3)}` | Manuscript readout `w`, still in dimension `n`; `c=w/sqrt(n)` |
| Prediction coefficient `w`, including `w_q`, `w_h`, `a_w` | `u`, `u_q`, `u_h`, `a_u`, with `u=B^T W^T c` explicitly defined in dimension `d` |
| All pre-existing local mathematical dummy/helper letters `u` | `\zeta`, including ordered residual coefficients, the scalar comparison ODE, and proof-local integration/logarithm/density variables; this avoids collisions with the prediction coefficient |
| Empirical input second moment `Q` | `\Sigma`, explicitly distinguished from the manuscript's sample-space population Grams `Q^{(\ell)}` |
| Theorem success probability `p` | `\pi`, including `S_n(\pi,A)` and the main proof; the density `p` remains unchanged |
| Half-MSE `\mathcal L` | `\mathcal L_{1/2}` |
| Time `t` and dots | Retained, with an explicit section-local half-MSE convention; `T=2^{-15}` corresponds to full-MSE `[0,T/2]=[0,2^{-16}]` |
| Network input | Same normalized `v=x/sqrt(d)` as the manuscript; predictions indexed by `v` evaluate physical input `x=sqrt(d)v` |
| `sec-nth-storage`, `sec-nth-storage-setup` | `cp:nth:storage`, `cp:nth:setup` |
| `thm-`, `lem-`, `cor-nth-storage-SUFFIX` | `cp:nth:SUFFIX` |
| `eq-nth-storage-SUFFIX` | `cp:nth:eq:SUFFIX` |
| `proof-nth-storage-SUFFIX` | `cp:nth:proof:SUFFIX` |
| Pandoc's written-out references and anchors | Manuscript `\Cref` / `\eqref` and ordinary LaTeX anchors |
| Book-specific introductory positioning | Two short paragraphs defining this independent manuscript benchmark |
| Book line-breaking directives | Remove `\allowbreak{}` and nine intra-factor/argument narrow-column wraps; preserve equation contents |

The remaining canonical matrix alias `W=W^{(2)}` is explicitly defined and
unchanged. No new global notation is required. The new section's only
references outside itself are the already defined `cp:setup`, `cp:network`,
`cp:flow`, `cp:data`, and `cp:headline`; these provide editorial/model
connections, not unprovided proof dependencies.

## Checks and handoff

Run from the repository root:

```sh
python studies/nth_lower_bound_20261010/PAPER_CONVERT.py
```

The executed conversion asserts preservation of all seven formal statements
and all six proof bodies after only the declared symbol/reference/layout
translations. It checks matching environment counts, all 38 unique label
mappings, the exact five external manuscript references, and that only the
expected TeX commands were introduced. It emits the extracted source and
the complete machine-readable mapping with proof hashes under
`data/generated/nth_lower_bound_20261010/paper_adaptation/`.
All these checks passed for the final hash above.

The converter changes only its assigned study include and generated scratch.
No live paper/book file or Git state was modified by this adaptation task.
The coordinator retains final integration and full manuscript compilation;
no separate full build was launched here.
