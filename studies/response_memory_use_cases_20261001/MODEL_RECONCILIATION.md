# Model and source reconciliation

Scientific input: current `paper/main.tex`, its included `results.tex` and proof
material; implementation input: the user-authorized `compact_flow.py` frozen
as `baseline_compact_flow.py`. Exact hashes are in SOURCE_MANIFEST.json. Source
defaults are not the paper's canonical initialization and are overridden below.

## Paper model used for the common baseline

There are m normalized inputs x_a in R^d with norm sqrt(d), n neurons in each
of two hidden layers, and scalar labels y_a. With tanh activation and no biases,

\[
h_a^{(1)}=\tanh(W^{(1)}x_a/\sqrt d),\quad
h_a^{(2)}=\tanh(W^{(2)}h_a^{(1)}),\quad
f_a=w^\top h_a^{(2)}/n,\quad r_a=f_a-y_a,
\quad \rho=(m^{-1}\sum_a r_a^2)^{1/2}.
\]

The loss is unhalved mean-square error. Mobilities are (n,1,n); the dense
hidden-matrix velocity is -2/(mn) sum_a r_a delta_a^(2) h_a^(1)T, with actual
transpose backpropagation. Initialization is independent W1 entries N(0,1),
W0 entries N(0,1/n), and exactly zero w. All relevant features are recomputed
through current parameters; frozen-feature controls are explicitly different.

For closure order q, tau starts at1 and tau_dot=rho. Stored moments retain the
paper names bar h and bar delta (the latter is the history of r delta/rho).
Only the zeroth forward moment is nonzero at initialization. The represented
hidden matrix is

\[
\widehat W^{(2)}=W_0^{(2)}-
\frac{2}{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\]

The ordinary raw moment equations never divide by rho. A zero-residual state
is stationary. The clock and moments are part of a differentiable inner learner;
their dependence on labels/inputs cannot be frozen in a hypergradient.

## Exact implementation correspondence

| Source `Flow` field | Paper quantity |
|---|---|
| `inputs` | rows x_a/sqrt(d), already normalized by caller |
| `w`, shape(n,d) | W^(1), not the readout |
| `c`, shape(n) | readout w |
| `matrices[0]`, `order=None` | evolving dense W^(2) |
| `matrices[0]`, positive `order` | fixed initialized W0^(2) |
| `moments[0]` / local `A`, shape(q,n,m) | raw bar delta^(2) |
| `moments[1]` / local `B`, shape(q,n,m) | raw bar h^(1) |
| `s` | tau-1 |
| `weights[j]` | 2j+1 |
| `order` | paper q (the original study often called it P) |

`_factors()` places -2/(mn) and (2j+1) on the backward factors and 1/tau on
the forward factors. `_apply(...,transpose=True)` uses the actual transpose
of both base and correction. There is no additional hidden 1/n in the forward
matrix action. `Flow` rejects readout_std=0; tests construct it with a positive
readout scale and zero c before any update. First weights and base matrices have
already been drawn and their laws are unchanged. Set hidden_gain=1 explicitly;
the CLI's `auto` gains and width-independent random readout are not used.

## What each route changes

- **Hypergradient:** functional, differentiable implementation of the same
  explicit Euler map. Source parity, finite differences and step refinement
  are required. Label design is a new outer optimization problem. Discrete
  derivatives and their measured accuracy are not consequences of C0 trajectory
  approximation alone.
- **Write buffer:** exact represented matrix is occasionally materialized as
  the new base; memories/clock are reset with the current forward prefix. This
  preserves the current function but changes future finite-q dynamics. Support
  changes are declared; current labels/readout/base after a restart generally
  leave the initialization hypotheses of the main all-time theorem.
- **Input field:** sample slots become fixed orthonormal input functions under
  a declared stationary input law. The reconstruction loses 1/m because the
  dictionary projections use probability expectations. Indicator functions
  sqrt(m)1[a=c] reproduce original moments divided bysqrt(m), exactly restoring
  the manuscript factor1/m. This is an additional approximation, with new
  sampling error and no imported stochastic or Gaussian all-time theorem.
- **History intervention:** a dense trajectory is observed. Its actual learning
  interval excludes the artificial prefix before defining temporal means.
  Online observer moments are also checked against independently integrated
  piecewise-constant histories. Editing a historical sample contribution is
  physical weight surgery; it is not the trajectory from retraining without
  those samples. Observer fidelity does not test autonomous feedback fidelity.

The paper's all-time result has small-label, Gaussian initialization and initial
Gram-gap hypotheses. Practical unit-scale teacher labels and optimized soft
labels in this campaign are empirical tests of the actual finite-width equations,
not certified examples inside an estimated theorem constant. Fixed W0 storage,
moving state, reverse-mode activation storage, dense writes and wall time are
separate measured/countable quantities throughout. In the regular eight-point
hypergradient experiment, oddness and antipodal pairs also force the full sample
Gram to have rank at most4, violating the positive full-Gram hypothesis. The
irregular-support stress removes that exact symmetry, without certifying the
remaining theorem hypotheses or any derivative approximation.

## Input-field normalization correction

The initial81 input-field fits accidentally passed rows(cos(theta),sin(theta))
divided bysqrt(2) into an API that already expects x/sqrt(d). Those results are
valid for raw unit-radius inputs, but differ from the study's intended raw
radius sqrt(2). Source/report variants with suffix INPUT_SCALED_V1 and the
original generated runs preserve that experiment explicitly. They must not be
used as canonical circle results.

Before repeating, the route recorded the correction in its protocol, fixed the
API rows to(cos(theta),sin(theta)), added a direct norm check, and reran all81
configurations with unchanged teachers, seeds, selected C5q3 dictionary and
controls. The corrected runs use the input_field_canonical namespace. Canonical
claims use only those reruns. The discrepancy and precise correspondence are
documented in INPUT_FIELD_NORMALIZATION.md. This change does not affect any
other route, whose caller already used unit-norm normalized rows.
