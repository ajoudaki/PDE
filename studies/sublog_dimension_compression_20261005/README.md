# Sublinear-in-d logarithmic compression

Status: active research study, opened 2026-10-05.

## Question

Can the complete predictor trajectory of the canonical trained dense network be
represented by a fully autonomous model whose retained size is

\[
 C_{\mathrm{task}}\,[\log(en)]^{r(d)},
 \qquad r(d)=o(d),
\]

while retaining the same worst-case-in-input, uniform-through-training accuracy
as the existing compact construction?  If not, prove a matching obstruction
under an explicit, stable representation model.

This is a new direction.  It does not alter or silently strengthen the
integrated theorem in `studies/integrated_general_compression_20261004/`.

## Fixed target setting

- The target is the canonical width-`n`, depth-`L` dense gradient-flow model,
  with fixed `L >= 2` and the existing analytic, non-affine activation class.
- Inputs lie on the radius-`sqrt(d)` sphere.  There are `m >= d` training
  inputs and their span is all of `R^d`.
- The existing positive feature-Gram gap and small-label condition are retained.
  No stronger data, activation, label, width, or conditioning hypothesis may be
  introduced and then advertised as answering the question.
- The comparison norm is exactly

  \[
  \sup_{t\in[0,\infty]}\ \sup_{\lVert x\rVert=\sqrt d}
  |f_{\rm comp}(t,x)-f_n(t,x)|.
  \]

- The requested accuracy scale is at most the proved dense-run variability
  scale, up to fixed-task constants:

  \[
  \frac{1}{\sqrt n\,[\log(en)]^{5/2}}.
  \]

  A stronger `n^{-1+o(1)}` comparison is welcome but is not required.
- The compact evolution must be autonomous and restartable from its retained
  state.  It must evolve genuine hidden features through a nonlinear depth-at-
  least-two mechanism; a frozen-kernel surrogate, stored trajectory, oracle
  replay, or query-time access to the dense model does not qualify.

## What “size” means

All retained trainable and fixed numerical coordinates required to initialize,
restart, evolve, and evaluate the compact model are counted.  Any data-dependent
decoder, dictionary, metric, mixer, or coefficient table is counted.  Fixed
activation formulas and a dimension-uniform algorithmic rule are not counted.

An unrestricted real-number encoding is excluded: a single infinite-precision
real can encode an arbitrary trajectory.  A general lower bound therefore must
state a stable representation class, including regularity/conditioning of its
encoder, autonomous dynamics, and decoder, or else prove the lower bound inside
the selected-neuron compact-network class used by the integrated theorem.

The desired upper bound must have the form

\[
C_{\mathrm{task}}[\log(en)]^{r(d)}
\]

with `r(d)/d -> 0`.  The constant and sufficient-width threshold may depend on
fixed task parameters, but not on `n`; all such dependence must be displayed so
that an `n`-dependent dimension cost is not hidden in them.

## Authorized sources

Repository sources:

- `docs/index.qmd` and `docs/notation.qmd`;
- the complete relevant artifacts in
  `studies/integrated_general_compression_20261004/`, especially the integrated
  result, compact comparison proof, and unbounded-compressor bridge;
- no other study.

External sources may be used only when primary and cited, principally for
approximation widths/entropy of analytic spherical function classes and stable
nonlinear approximation lower bounds.

## Proof obligations

### Constructive route

1. Give an explicit retained state, initialization, autonomous vector field,
   and decoder.
2. Count every retained coordinate and prove exponent `r(d)=o(d)`.
3. Prove the comparison in the stated norm through the fitted endpoint.
4. Show that feature learning is genuinely present and essential, rather than
   relabeling a kernel or replay construction.
5. Audit all constants and the width threshold for hidden `n`-dependence.

### Lower-bound route

1. Define the admissible stable representation class before counting size.
2. Exhibit a packing or width obstruction of reachable dense training
   trajectories, not merely of the much larger class of all analytic functions.
3. Keep `L >= 2`, nonlinearity, trained hidden features, `m >= d`, full input
   rank, the sphere supremum, and the complete time interval.
4. Establish a logarithmic exponent at least proportional to `d`, or clearly
   report the exact weaker conclusion and the missing reachability lemma.

## Decision rule

The study answers “yes” only with a complete construction meeting every
obligation above.  It answers “no” only with a lower bound for an explicitly
defined stable autonomous representation class that includes the requested
compact models.  A lower bound for a generic analytic ball, or an upper bound
that freezes features or counts only the learned state, is evidence but not a
resolution.

## Baseline mechanism to challenge

The current compact proof expands analytic source fields jointly in physical
time and the query direction.  Truncating spherical harmonics through degree
proportional to `log n` produces a number of angular modes polynomial in
`log n` with exponent proportional to `d`; explicit compact mixers then square
the selected width in storage.  Any improvement must identify which of these
costs is avoidable for the *reachable nonlinear training trajectories*, rather
than for an arbitrary analytic field.

## Reproducibility

- Starting commit: `3834145d910202a84824d943fe7d7f65714d96f2`.
- No experiments are planned initially; this is a proof-search study.
- Concurrent unrelated dirty files and untracked studies are outside scope and
  must remain untouched.

