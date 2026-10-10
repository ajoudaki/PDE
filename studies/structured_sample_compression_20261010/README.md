# Structured sample compression for Legendre, Harmonic and Taylor

Started 2026-10-10 at HEAD af9ee2765187a9d53539b60e81575a7c02d252a5.

## Contract

Explore theoretical sample compression in addition to width compression.
The primary target is a retained autonomous predictor whose error relative
to the coupled dense training trajectory is at most a fixed epsilon, with
retained complexity capped independently of the number m of observations.
Keep finite-horizon, all-time, input-support and whole-sphere conclusions
distinct. A simpler endpoint approximation to the target labels is not a
substitute for trajectory compression. Width n, ambient dimension d, fixed
depth L, activation constants, accuracy, data geometry and conditioning may
remain visible dependencies. No full data oracle, latent coordinate oracle,
future dense trajectory, or uncharged dataset is permitted in retained state.
Reading arbitrary input data may still cost at least linearly in m.

The user proposes low-dimensional inputs with spectrally simple labels, or
observations (x(z),y(z)) on a compact low-dimensional latent set with a
continuous/Lipschitz generator. Analyze what each hypothesis actually gives;
do not assume that label simplicity controls evolving neural responses.
New assumptions or changes to the current optimizer must be explicit.

## Scope and plan

This is a new direction. Inputs are this study, the maintained docs/ book,
and the user-assigned current paper's setup and three compression methods.
Do not follow paper links into other studies. External primary mathematical
sources may be checked and cited. The old residual-clock proof study is not
an input. No experiments, paper changes, commits or promotion are requested.

Use a bounded theoretical exploration: a generic weighted-data reduction,
a spectral-conditioning route, a latent-covering route, and a method-specific
interface check. Separate exact reductions and conditional finite-horizon
theorems from conjectural all-time extensions. The root owns this README
and the synthesis; scoped independent agents own their assigned flat notes.

## Status

The bounded exploration is complete. `RESULT.md` contains the synthesis
and elementary proofs. No general all-time sample-compression theorem for
the three nonlinear constructions is claimed.

- **Proved:** for fixed width, initialization, finite horizon and bounded
  labels, an energy-derived common parameter ball gives a deterministic
  comparison of the actual nonlinear dense flow with a weighted-data flow.
  A Lipschitz k-dimensional latent image gives at most
  C_T epsilon^(-k) representatives, independently of m. The algorithm uses
  observed distances, not latent coordinates. C_T is not width-uniform and
  may grow badly with the horizon.
- **Proved:** exact frequency/mean-label reduction at repeated inputs;
  positive finite moment matching; and exact all-time sample reduction
  when the architecture has a fixed finite output dictionary at every
  parameter state. Simple labels alone do not imply this last hypothesis.
- **Construction interfaces:** weighted representatives remove explicit
  sample-indexed objects algebraically. Legendre keeps its temporal basis;
  Harmonic is the closest match to a shared spatial-moment construction;
  Taylor additionally needs query anchors if the original large query panel
  is to remain the accuracy target. These are not new optimized all-time
  storage theorems.
- **Open:** sample-uniform all-time stability for feature-learning flows,
  controlled omitted-mode feedback, and preservation of the sharp width
  exponents. The existing full-Gram label cap cannot accommodate fixed
  nonzero Y as m grows. Labels were not shrunk to evade this issue.

## Inputs, independent routes and check

`SPECTRAL_ROUTE.md` and `LATENT_ROUTE.md` are independent prompt-scoped
derivations. `METHOD_INTERFACES.md` checks the assigned current-paper
interfaces. Its complete source files were `paper/compact.tex`,
`paper/compact_legendre.tex`, `paper/compact_selected.tex` and
`paper/methods.tex`; no other study was imported. The root also read the
maintained book index and notation contract and relevant setup/Gram material
in `docs/08b-trajectory-compression.qmd`. All three route reports were read
in full before synthesis.

The primary external source checked was Bayer and Teichmann, *The proof
of Tchakaloff's theorem*, https://arxiv.org/pdf/math/0502473. The finite
positive-weight elimination argument needed here is proved directly in
`RESULT.md` rather than imported as an unexplained black box.

`CHECK.md` records a fresh isolated mathematical check of the complete
synthesis, using only that frozen candidate and the current paper setup.
The assigned claims passed within their stated scope. Three clarifications
were incorporated: distinguish the disconnected d=1 sphere, handle a
constant latent generator separately, and require the exact output
dictionary identity at every parameter state. The final checked
`RESULT.md` SHA-256 is
`b103e063d4c62e5d4d00867f733d4edb294811dd16bbdb9f45bb0959c4cbc804`.
The root read the complete check. This is an internal bounded verification,
not a promotion review or an audit of the inherited paper theorems.

No experiments, paper edits, commits or promotion were performed. Existing
unrelated worktree changes were preserved.

## Follow-up: the sample axis of the response tensor

The user clarified that the target is a third response-compression axis,
not primarily a representative-data preprocessing theorem. This continues
the same investigation. `THIRD_AXIS.md` develops the sample-mode formulation;
the checked finite-time theorem in `RESULT.md` is unchanged.

The key additional exact identity projects forward and residual-weighted
backward responses onto the same empirical sample space. Their interaction
defect is a product of orthogonal tails. Sample and time projection commute,
giving the algebraic Legendre memory count 2(L-1)nRq. Separate projection of
residual, backward response and forward response instead introduces triple
moments and does not automatically retain that quadratic defect estimate.

`TENSOR_ROUTE.md` is a prompt-only derivation of the sample algebra, a finite
moment-based nonlinear Galerkin construction and a common-family covering
rank bound. `MODAL_ROUTE.md` is a separate prompt-only derivation of an
all-time, gap-free truncation estimate for a specified mode-preserving
residual system, with explicit limits on its neural interpretation. The
root owns the synthesis and checks the reports before using their claims.

The root read both complete route reports, checked their displayed algebra,
and requested two clarifications to the tensor route before accepting it:
the non-affine polynomial specialization is outside the paper's activation
class, and its particular gradient flow has global finite-time existence
by its dissipation/path-length bound. Final route SHA-256 values are
`72f9ec21e000e9a060847fcb3342d6aa4bbe6cfa9127b24046a4ce87bd2a8f65`
for `TENSOR_ROUTE.md` and
`ddf33b4e581d415c868bf26b0143598421329e8dda98388c25c1c832802df4bd`
for `MODAL_ROUTE.md`. The latter's nonlinear tanh toy uses two-point support;
its exact sufficient statistic is not evidence of a rich-support theorem.

`THIRD_AXIS_CHECK.md` is a fresh isolated check of the synthesis's displayed
projection and analytic-rank arguments, without route reports or prior
findings. It found no substantive error and requested explicit clock
conventions. The synthesis now specifies the dense normalization, residual
clock, residual-zero continuation, unnormalized clock measure, and the
Legendre reconstruction factor. Its corrected SHA-256 is
`a26ce30077b10efcbe69cc9151fac33a05d7785a67c2af8eab63b7018416731f`.
The root checked the dense factors against `paper/compact.tex` and
`paper/compact_legendre.tex`. The targeted report does not certify the
unproved all-time extension or all inherited paper results.

The sharper analytic rank estimate is conditional on a uniform complex
extension of the response family and an accessible basis; it is not inferred
from Lipschitz latent dimension or smooth labels alone. No combined optimized
width/sample theorem, general all-time closure guarantee, or latent recovery
algorithm is asserted. The next substantive bottleneck is controlled
nonlinear response tails and integrated omitted-mode feedback, with a compact
runtime and constants that preserve the desired width scaling. A full minimum
gap is only one possible sufficient route, not a necessary condition.

## Follow-up: attempt at an unconditional all-time theorem

The user requested the strongest general sample-compression theorem with
explicit width, sample, dimension, depth and activation dependencies. This
continues the same investigation. `ALLTIME_RESULT.md` records the outcome:
the requested combined theorem is not established, and no paper headline
or qualification has been changed.

`ALLTIME_SOURCE_ROUTE.md` proves two initialization-ball sufficient tests
for all-time nonlinear fitting and finite path length, explicit layerwise
derivative and Gaussian bounds, and a gap-free dissipative comparison for
relative residual generators. These are not sample-compression constructions.
The inverse-weighted nonlinear drift is not controlled sample-uniformly by
the proposed label/latent assumptions, and the relative comparison's full
bilinear condition forces equal nullspaces. Its query guarantee is training
RMS, not the sphere supremum.

`GENERAL_SCOPE_CHECK.md` proves all-time empirical-measure discontinuity
for actual deep linear Gaussian training, including distinct observations
on an analytic circle with constant labels. `ALLTIME_GEOMETRY_ROUTE.md`
gives an affine near-duplicate example and exact finite-support/affine-moment
sample reductions. These examples obstruct absolute geometric approximation
arguments, not sample compression itself. Their positive-probability,
fixed-width scope and differences from the original full-gap/small-label
theorem are explicit.

The root read all three complete route notes and checked the synthesis.
`ALLTIME_CHECK.md` is a fresh isolated mathematical check of the complete
source and general-scope routes, not the geometry route or a review of
the inherited paper. The root read its complete report. The checked hashes
are `ade475661cd15f93e783fd914b6466063d4d82836fc29f945b42b01622e4a975`
for `ALLTIME_SOURCE_ROUTE.md` and
`26ac3a59aa71e3d31c3d826fad66e6c212f6e1c6a57ae9e06bd41c8be69b9c69`
for `GENERAL_SCOPE_CHECK.md`. The check found no substantive error under
the stated assumptions; it does not certify the missing general theorem.
The final geometry-route hash read by the root was
`08fe69b113ae26e57bf3a80615c571b9d3a78acf2b545843c82ab97606e7109d`.

The unresolved task is an initialization-derived, source-sensitive bound
on nonlinear weak-mode feedback and its query extension, together with an
autonomous sample-mode realization whose constants preserve the width
rates. Neither source norms nor width thresholds may hide renewed growth
with m. No experiments, paper/code edits, commits or promotion were made
in this follow-up. Unrelated concurrent work was preserved.
