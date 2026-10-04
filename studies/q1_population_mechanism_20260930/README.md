# The learning mechanism of the autonomous q=1 closure

Started 2026-09-30. The original investigation switched from encoding an input population to understanding the q=1, two-hidden-layer response-memory closure as a learning system in its own right. The current task explicitly continues this study. Its primary scientific input is now the complete current `paper/main.tex` and its included appendices, expressly authorized by the user, together with this study's derivations and maintained docs/code if needed. No unpromoted findings from other studies are inputs.

## Current scope: intrinsic learning only

The user's steering explicitly removes all further compression objectives. Study the q=1 populations solely to understand feature learning, fitting success/failure, and selection of the function on unseen inputs. The latest request continues the **direct infinite-width neuron population dynamics** and authorizes selecting a few structured inputs, including latent-factor tasks. Read-in, readout and memories are represented by joint population laws with fixed-source marks. Earlier finite-neuron examples are retained below but do not answer the population question. Do not seek smaller state or an input-sample population limit. Previously started coarse-graining work is retained as an abandoned-scope artifact and is not part of the current conclusion.

The 2026-09-30 manuscript reconciliation is recorded in [MANUSCRIPT_RECONCILIATION.md](MANUSCRIPT_RECONCILIATION.md), including complete root read coverage, hashes, exact moment rescalings and the zero-readout/joint-prefix qualifications. No model discrepancy was found for the study's specified initialization against that pinned version.

Manuscript refresh, 2026-10-01: at the user's request, the shared checkout was
fast-forwarded from `7fce699` to `690e3d4` and the updated paper was compiled
successfully to `paper/main.pdf` (59 pages). The new source layout includes
`results.tex`, `proof_alltime.tex`, `proof_tracking.tex` and
`proof_finite_time.tex` alongside the comparison and sphere appendices.
Build command, source hashes, log and PDF checks are recorded under
`data/generated/q1_population_mechanism_20260930/manuscript_build_20261001_4e3qsx8g/`.
The build had no unresolved references/citations and two underfull-hbox layout
notices. Existing local study work was preserved. This was a pull/build task,
not a scientific audit of the revised manuscript: the earlier reconciliation
and results below remain attached to their recorded source versions. Before
further scientific continuation, read the complete revised paper and included
proofs and reconcile any changed definitions, assumptions and claims.

## Current four-point latent-factor result

The selected task is lifted XOR: normalized inputs
u_(sigma,tau)=(sqrt(1-2epsilon²), epsilon sigma, epsilon tau),
labels sigma tau, and uniform weights on sigma,tau in {-1,1}. Epsilon is
small but fixed; tanh, Gaussian initialization, the fixed canonical mixer,
its true adjoint, and all q=1 memories are retained. There is no trained
dense middle layer. Either latent bit has exactly zero correlation with
the labels, and only their product is supervised.

Main proof: [STRUCTURED_POPULATION_ANALYSIS.md](STRUCTURED_POPULATION_ANALYSIS.md).
Selection, scope and bounded calculations:
[STRUCTURED_POPULATION_CONTRACT.md](STRUCTURED_POPULATION_CONTRACT.md).
The first-layer derivation is [WEAK_FACTOR_ROUTE.md](WEAK_FACTOR_ROUTE.md);
the complete second-layer calculation is
[WEAK_FACTOR_SECOND_LAYER.md](WEAK_FACTOR_SECOND_LAYER.md).
Their frozen final sections record the sign obligations at author freeze;
the subsequently executed interval certificates close those obligations.

For every sufficiently small fixed epsilon, **both hidden layers initially
make both primitive factors easier to decode while weakening the common
context**. The precise decoder measure is its least squared population
readout norm, exactly the reciprocal of the corresponding feature energy.
Certified feature-time second-derivative coefficients are approximately
0.192447 epsilon^6 and 0.201780 epsilon^6 for the first/second factor energies,
and -0.047955 epsilon^4 and -0.055941 epsilon^4 for their context energies.
The first-layer product grows relative to its factors, which grow relative
to context. These are strict local changes on actual assumed regular
population trajectories, not just formal Taylor coefficients or an empirical
training result. The epsilon threshold and time interval are existential.

The mechanism is an exact initialization expansion of the label-feature
energy: its positive mixed term is proportional to the product of the two
primitive-factor energies. Thus strengthening either factor helps the
supervised interaction because the other factor exists. In the full second
layer, readin conditional drift, the fixed mixer's true-transpose covariance,
and q=1 memory writes each contribute positively to factor acquisition and
negatively to context. Omitting the covariance changes the result.

At **every state**, a first-layer tanh neuron has product-response magnitude
no larger than either primitive-factor response. In the equivariant population
this gives a permanent ordering of decoder costs. Moreover, at any finite
fitted endpoint with bounded response operator B,
E_(first,bit) >= 1/(2 ||W||² ||B||²), so both constituents must remain
represented. This is not monotonic acquisition until fitting. The whole
predictor is odd in all three latent coordinates; a C3 fitted endpoint has
F_*(u)=u0 u1 u2 Psi_*(u0²,u1²,u2²) in normalized query coordinates,
but its amplitude and additional zeros
are not determined. Global fitting and endpoint existence remain open.

As in the preceding two-sample investigation, existence and sufficient
regularity of the canonical unique equivariant population flow remain explicit
hypotheses. The manuscript calls its fixed-order population limit conjectural.
A finite list of unmarked marginal densities has not been shown to define
that flow. The result is conditional population mathematics, not a population
construction theorem, an independently promoted result, or a priority claim.

Check status: the full first-layer proof and interval certificate passed
[WEAK_FACTOR_FIRST_CHECK.md](WEAK_FACTOR_FIRST_CHECK.md), SHA256
`154a64d0b1aea22c0b5cd7970f0db64131e10c4e3c560c18488a6438bc0a75d9`.
The full second-layer proof and certificate passed
[WEAK_FACTOR_SECOND_CHECK.md](WEAK_FACTOR_SECOND_CHECK.md), SHA256
`608bda8f4f8383d69334f17e1612f179d17c8f2138f9ce475c11552e294e8da6`.
Each fresh scoped checker independently reproduced the rigorous intervals.
Root read both complete reports. The assembled main note passed the separate
fresh complete [STRUCTURED_POPULATION_CHECK.md](STRUCTURED_POPULATION_CHECK.md),
including the added output, conditional mean-drift, endpoint norm-bound and
query-symmetry consequences. The checker identified a query-coordinate
notation ambiguity: the final section now uses normalized u consistently,
with manuscript x=sqrt(3)u. Its original finding and correction addendum
are retained. Reversing only that correction exactly recovered the original
frozen main hash; the final checked main SHA256 is
`153947b283ec0c42c3c32e46c47e2800e4d314599308da96cc087879d854894f`.
The checker reproduced both certificates and root read the entire report.
Final report SHA256:
`9b4f4ffd3e14dbdaef2a5baf41256b0e442d4343853af1f2ed049651552ed36c`.
This is an internal conditional PASS, not a population construction or
global convergence result. No manuscript or Git writes were made.

Reproduction: Section 8 of the main proof contains the two standard-library
certificate commands and their analytic error bounds. Exact root outputs are
in `data/generated/q1_population_mechanism_20260930/` under
`weak_factor_interval_certificate_20260930_01/results.json` and
`weak_factor_coefficient_certificate_20260930_01/results.json`.
The former encloses all Gaussian moments, integration errors, tails and
rounding; the latter evaluates the exact second-layer and ratio polynomials
with outward rounding. Exploration also used bounded deterministic
initialization quadrature; it was not a training simulation or a theorem
dependency. The small-factor direct quadrature was inconclusive and is
explicitly superseded by the analytic reduction and rigorous certificate.

Other completed routes remain author-checked candidates, not dependencies:
LATENT_ORBIT_ROUTE.md (equal-scale tetrahedral constraint),
SIMPLEX_MECHANISM_ROUTE.md (triangle contrast and source innovations), and
GLOBAL_MEMORY_ROUTE.md (exact compensation and a conditional obstruction
to persistent nonfitting). Root read each complete frozen route. The next
substantive unresolved bridge is propagation of the newly proved factor
acquisition through finite training, while controlling memory lag; the current
local theorem must not be presented as that propagation.

## Preceding two-sample population continuation

The exact scope and route assignments are in
[TWO_SAMPLE_POPULATION_CONTRACT.md](TWO_SAMPLE_POPULATION_CONTRACT.md).
The main new proof is
[TWO_SAMPLE_POPULATION_ANALYSIS.md](TWO_SAMPLE_POPULATION_ANALYSIS.md).
It studies two equally weighted signed unit inputs with inner product
c in (-1,1), two tanh hidden populations, the fixed canonical Gaussian source
and its true adjoint, and the same normalized q=1 key/value dynamics.
Separate neuron marginal densities cannot replace the joint source-response
laws. There is no learned full middle matrix and no dense trained reference.

The manuscript's fixed-order population limit remains a conjecture. The new
trajectory statements explicitly assume a regular unique equivariant population
flow realizing the canonical initialized source law. Neither the old finite-width
existence proof nor naming an L2 operator establishes this foundation.

Main internally checked conditional findings:

1. At the first nonzero order, **both hidden populations** strictly increase
   their squared common signed response and strictly decrease their squared
   difference response, for every -1<c<1. Consequently both normalized signed
   feature overlaps increase. The proof includes the actual adjoint reuse and
   the full moving-read-in contribution to the second layer; it is not just a
   memory-only or frozen-feature statement.
2. Residuals synchronize but both q=1 memory channels activate; their population
   correction has rank exactly two near initialization. The first reverse
   Gaussian call has response drift and correlated innovations. Discarding the
   former loses the supervised first-layer moment change.
3. The contrast-key lag contributes **negatively** to the output progress on
   the initialized flow, beginning at feature-time order five. The positive
   response dominates initially. Termwise nonnegative memory work, even in
   integrated form, therefore cannot prove sustained fitting.
4. The entire function has an exact symmetry normal form throughout every
   existence interval. Its mandatory zero plane is perpendicular to
   y_1 x_1+y_2 x_2, and is inherited by any pointwise endpoint limit. On the
   circle a C1 endpoint must have F(theta)=cos(theta)Q(cos²(theta)). Fitting
   fixes one value of Q, not its full shape or its sign elsewhere.

Global canonical population construction, fitting for -1<c<1, endpoint
existence, exclusion of extra zeros, and the selected final amplitude remain
open. The adverse lag result does not show increasing initialized loss or
failure to fit. The finite-neuron historical-readout theorem below cannot
establish population endpoint history persistence.

Check status: **internally checked for the explicitly stated conditional
scope**. Root read all three scoped derivations in full after freezing, then
added the full second-layer contrast proof. The assembled candidate is frozen
at SHA256 `6fca4558d5d54a40fbb9c49b772ac0c621ab4e61e06c92b6be64700acbb034d2`.
[TWO_SAMPLE_POPULATION_CHECK.md](TWO_SAMPLE_POPULATION_CHECK.md) checks every
scientific line and the initialized Gaussian dependencies, and verifies the
exact manuscript normalization from authorized primary excerpts. Its initial
report required bounded first derivatives in the general Gaussian source class;
all actual sources already had them. The correction and two precision edits
were applied, then rechecked with an exact reverse-patch hash verification.
The final addendum reports PASS, with no required correction remaining.
Final report SHA256:
`caa1948f31d3d8025a8334625a5eb7d9bb4447d4484e01aa6dc120a584b56030`.
The original adverse finding remains in the report. Root read its full original
391 lines and the complete correction addendum.

The separate [TWO_SAMPLE_STARTUP_CHECK.md](TWO_SAMPLE_STARTUP_CHECK.md) fully
checks the frozen mixing and symmetry routes and supplies the finite-initialized
source-law derivation, without a trained-network trajectory. It reports
conditional PASS and preserves the necessary source, strong-flow and parity
qualifications. Root read all 307 lines. Its SHA256 is
`7fb3d7d9631e24d087cd23683f7d1f37767c58fd8e87cf56c34dca6b51c32687`.
Neither report proves the missing population construction or endpoint. These
are internal mathematical checks, not promotion reviews. The assembled checker
discloses an unsolicited author consistency message received after independently
checking the same formulas; it is not advertised as a fully blind review.

Population ownership: root owns the main analysis, contract and shared
README/SYNTHESIS. `pair_symmetry_route`, `pair_fitting_route`, and
`population_mixing_route` own their correspondingly named TWO_SAMPLE route
notes. The fitting addendum was a single targeted follow-up after its first
freeze and is explicitly not an independent route. `population_startup_check`
owns TWO_SAMPLE_STARTUP_CHECK.md; `population_theorem_check` owns
TWO_SAMPLE_POPULATION_CHECK.md, checking the assembled candidate from a fresh
context. Source scope, exposure disclosures and exact hashes are retained in
the individual reports. No numerical experiments, manuscript edits or Git
writes were performed.

Reproduction: follow the analytic Gaussian conditioning and four-source
calculation in Sections 3--4 of the main note, then its exact identities and
lag expansion in Sections 5--6. No generated arrays or training runs are
dependencies. Next mathematical bottleneck: a compensation estimate for total
memory work and read-in dissipation that permits shrinking contrast and its
necessarily negative lag term. Any further proof attempt must retain fixed
source reuse and distinguish flow construction from conditional flow identities.

## Earlier finite-width contract (retained)

Finite m points on a circle or sphere, labels +1 or -1, equal sample weights, width n, tanh activation, no biases. Preserve the exact fixed Gaussian mixer W0, moving read-in A and readout w, and the q=1 old activity-clock memory. Analyze autonomous populations directly, with no dense trained reference or trajectory driver. Distinguish identities and conditional endpoint statements from fitting and implicit-bias theorems. Do not assume all tasks fit. No training experiments or maintained paper/code edits were performed.

Use r_a=f_a-y_a, rho=(m^-1 sum r_a^2)^1/2, tau(0)=1 and taudot=rho. Forward keys k_a(0)=h_a(0) obey kdot_a=(rho/tau)(h_a-k_a). Value memories v_a(0)=0 obey vdot_a=-2r_a d_a. For any input x, h(x)=tanh(Ax/sqrt(d)), z(x)=W0 h(x)+m^-1 sum_a v_a <k_a,h(x)>_n, g(x)=tanh(z(x)), f(x)=<w,g(x)>_n, with <u,v>_n=u^Tv/n. Define d_a=w odot (1-g_a^2), ell_a=(1-h_a^2) odot [W0^T d_a+m^-1 sum_b k_b<v_b,d_a>_n]. Then Adot=-2 m^-1 sum_a r_a ell_a x_a^T/sqrt(d), wdot=-2 m^-1 sum_a r_a g_a. These equations define the object; no dense trained matrix is a state. Throughout the current results w(0)=0. Earlier startup wording used c_a=-v_a/2 and called a different intermediate field v_a; the present convention agrees with every current route and synthesis. Gaussian read-in entries have variance 1, mixer entries variance 1/n.

## Ownership and routes

Root owns README, ROTATING_FEATURE_SPAN.md, SCALAR_CIRCLE_SELECTION.md and SYNTHESIS.md. Fresh prompt-only independent routes examine intrinsic energy/stability (q1_energy, ENERGY_ROUTE.md), whole-input predictor selection (q1_predictor, PREDICTOR_ROUTE.md), and signed task geometry (q1_coarse_grain, SIGNED_GEOMETRY_ROUTE.md). The third route initially examined coarse graining, but was redirected when the user removed that objective; COARSE_GRAIN_ROUTE.md is retained as superseded-scope work. Each first derivation was frozen before cross-route comparisons. Internal cross-checks follow concrete results.

Continuation ownership: root owns MANUSCRIPT_RECONCILIATION.md,
ENDPOINT_HISTORY_SELECTION.md and shared README/SYNTHESIS updates;
`endpoint_route` owns ENDPOINT_INDEPENDENT_ROUTE.md from a fresh prompt-only
context; `endpoint_check` owns ENDPOINT_HISTORY_CHECK.md and sees only its
complete self-contained candidate. `notation_audit` performed a scoped read-only
normalization check. No Git writes, commits or pushes are planned.

## Earlier finite-width endpoint checkpoint

The selected bottleneck is persistence of the historical readout at a fitted
endpoint. [ENDPOINT_HISTORY_SELECTION.md](ENDPOINT_HISTORY_SELECTION.md)
contains a complete new candidate proof: two neurons, one circle training
input, a finite deterministic initialization, exponential fitting, a nonzero
endpoint readout perpendicular to the final training feature, an explicitly
signed unseen-query contribution, and classifier disagreement with the
minimum-norm readout using the same final features. A transverse crossing in
feature time proves persistence on an open set of Gaussian initializations.
Check status: **internally checked** at candidate SHA256
`808d4af77af6fb7e14938cd976a26dcf4f2b92ca6784e460cb0f5d9a866df7e6`.
The complete [ENDPOINT_HISTORY_CHECK.md](ENDPOINT_HISTORY_CHECK.md), by fresh
candidate-only checker `/root/endpoint_check`, reports PASS with no required
correction; root read the full report and rechecked the algebra and rational
bounds. The report verifies the clock conversion, finite endpoints, determinant
and query signs, boundary disagreement, and continuity of the fitted crossing.
It includes its exact scalar verification command and output (exit 0).
Report SHA256:
`9238870e6928da24467645b643cdafecc03b3ae26ca1425741781bd3011f5c92`.
This is an internal mathematical check, not a promotion review. The manuscript
mapping was checked separately as recorded above. No training experiment or
empirical evidence is used.

The independently frozen [ENDPOINT_INDEPENDENT_ROUTE.md](ENDPOINT_INDEPENDENT_ROUTE.md)
has SHA256 `9f13e452f828fdd179a160c94ec774bf1a7a824a7cc7e14c57b71ef0d707d498`.
Root read it in full only after both routes were frozen. It supplies a second
finite-parameter construction for prediction persistence, retained as an
author-checked alternative candidate, not a proof dependency or a second
independent review of the primary theorem. Its symmetric witness establishes
prediction differences; the primary theorem separately proves boundary
differences with invertible final matrices.

Reproduction: the theorem is analytic and self-contained in
ENDPOINT_HISTORY_SELECTION.md. Follow equations (1)--(20); the internal check
contains a short exact-rational arithmetic command, requiring only Python's
standard library. There are no generated training products to reproduce.

The existence question for endpoint persistence is resolved positively on an
open fitting class. Multi-input persistence, typical probability/size and
test-risk usefulness remain open. The next authorized mathematical question
is whether the historical contribution persists for multiple distinct training
directions without relying on a nearly saturated neuron. This checkpoint ends
the present bounded proof effort; it does not launch a numerical campaign or
propose manuscript promotion. The current manuscript and shared instructions
retain their startup hashes; the Git index remains untouched.

## Status

The completed synthesis is [SYNTHESIS.md](SYNTHESIS.md). Its central findings are:

1. Initial representation acceleration increases squared hidden-feature correlation with labels, with exact coefficients. Class-signed value memories also align initially when the initial label signal is nonzero. These are local statements, not all-time alignment or monotonicity claims.
2. An exact readout comparison identity holds despite moving features and proves global finite-time well-posedness. The instantaneous loss law isolates one signed key-lag contribution; a Gram-gap/lag condition suffices for fitting but is not proved universally.
3. Rotation of the training-feature span can create a readout component invisible on training points but visible on test inputs. A two-neuron q1 example proves transient generation. The new endpoint theorem proves that the component survives fitting and changes the decision boundary on an open two-neuron, one-input initialization class. Typical behavior and multi-input persistence remain open.
4. A one-neuron, one-circle-input case has exponential fitting, a finite endpoint, and permanent positive key lag. For a specified semicircle test truth, its boundary rotates toward the true boundary and test classification error strictly decreases if the unobserved initial component is nonzero. This is a scoped example, not a multiple-input generalization theorem.
5. Oddness and signed input geometry expose exact architectural conflicts and the initial signal required for learning to start. No universal fitting or maximum-margin theorem is claimed. Universal minimum-norm readout selection using the final learned features is now refuted by the endpoint theorem.

ENERGY_CHECK.md, ROTATING_FEATURE_SPAN_CHECK.md, SIGNED_GEOMETRY_CHECK.md and SCALAR_CIRCLE_SELECTION_CHECK.md record the original bounded internal checks of complete candidate notes and their hashes. All found the equations valid; the scalar test-risk statement was corrected to include its beta=0 exception. ENDPOINT_HISTORY_CHECK.md records the new complete candidate-only check. These are same-study internal checks, not independent promotion reviews. Source routes preserve their checked versions; endpoint-open statements in earlier frozen routes are superseded only in the existence scope proved by ENDPOINT_HISTORY_SELECTION.md. No numerical training evidence is asserted.

One full external primary paper, Katharopoulos et al. (2020), was read for associative-memory precedent only; the synthesis links it and makes no priority claim. All principal learning identities were derived directly from the specified q1 equations. Earlier studies and historical chat proof claims are not inputs.
