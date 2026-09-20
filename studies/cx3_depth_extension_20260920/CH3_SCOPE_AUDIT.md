# C-H3 scope audit for a faithful depth extension

Author-side bounded source audit, 2026-09-20. This is a scope and dependency
audit, not an independent theorem review, a new proof, or numerical evidence.
The requested maintained commit is `bcee9782651c34ae1204d37186e5c57e9282b273`;
`git rev-parse HEAD` returned that commit during this audit. All line references
below refer to the working source read at that commit. No tests or training were
run, no Git writes were made, and no other study or agent's scientific output
was read.

## 1. Main finding

Three scopes must remain distinct in the depth-extension contract:

| Scope | Maintained C-H3 obligation | Geometry/activity qualification |
|---|---|---|
| Canonical target flow | Every Borel probability law on `sqrt(2) S^1 × [-1,1]`, strong population GF and actual finite-GF identification through physical time `1/200` | No exclusion of repeated, parallel, antiparallel, orthogonal, singular-Gram, atomic, or nonatomic data |
| Executable represented family | Every separately fixed rational two-arc law `ArcLaw(p,a,b,c,d)`, on the same fixed interval, with numerical and closure-order convergence | This particular family has cross-component normalized dot products in `[2/5,4/5]`; it includes atomic and nonatomic laws |
| Strict activity | A separate conclusion on specified nondegenerate data or an explicitly chosen open law subfamily | It is not a premise for the broad target-flow existence theorem, and it is not asserted for every Borel law |

The source explicitly makes the first two distinctions in
`docs/global_nonlinear.md:12607–12629` and `:12637–12678`. It also says that the
two-arc laws are not being asserted to lie in the older time-40 neighborhood
(`:12583–12584`). Importing the older neighborhood's activity proof into this
entire represented family would therefore require a new argument.

For a faithful three-layer conjecture, excluding parallel or antiparallel inputs
from the broad target-flow domain would weaken C-H3. Conversely, demanding
strict activity for every law in that broad domain would strengthen the claim
beyond the maintained result and is false for elementary cancellation laws.

## 2. Exact model and target-flow obligations

The maintained finite model is

\[
f_n(x)=\frac1n (W^{(3)})^T
 \tanh\!\left(W^{(2)}\tanh(W^{(1)}u)\right),
\qquad u=x/\sqrt2\in S^1.
\]

It is bias-free, with two tanh hidden layers, independent centered Gaussian
stored-entry variances `(1,1/n,1/n^2)`, block mobilities `(n,1,n)`, residual
`f-y`, and unhalved probability-weighted squared loss. Times are physical GF
times. The finite random readout is retained; only its population limit is zero
(`docs/global_nonlinear.md:12557–12562`, `:12596–12617`).

The target for each Borel law has raw state

\[
(w,K,c)\in L^2(\Omega_1;\mathbb R^2)
 \oplus\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))
 \oplus L^2(\Omega_2),\qquad A=A_0+K,
\]

initially `(g,0,0)`, with `g ~ N(0,I_2)`. The initialized action is bounded,
not assumed Hilbert–Schmidt, and its reverse is its actual adjoint. The learned
increment is Hilbert–Schmidt. The exact drift is equation `(H3.S3)`
(`:12682–12704`); both orientations of the same action are indispensable.

Part A establishes all of the following on `[0,1/200]`:

- A canonical strong `C^1` population GF for **every** Borel law on the stated
  compact data domain, uniquely among strong raw solutions on the same
  canonical initialized-action carrier (`:12607–12621`, `:12956–12968`).
- The exact loss-energy identity and explicit row/readout/increment bounds
  (`:12989–13010`).
- A common deterministic law-continuity modulus in the sum of row `L^2`,
  increment HS, and readout `L^2` norms, hence also whole-circle forward and
  prediction continuity (`:13012–13016`).
- Reached-state restart under the same training law for the remaining
  interval; no assertion about arbitrary ambient endpoints or arbitrary
  switched training laws (`:13018–13027`).
- Actual finite-GF identification in probability, including whole-circle
  predictions and every separately fixed admissible same-layer joint
  observation with second moments. This holds for any deterministic
  `lambda_j -> mu` in `W1` and any `n_j -> infinity`, allowing the actual laws
  `lambda_j` to be Borel rather than atomic (`:12622–12627`,
  `:13109–13148`).
- For iid empirical laws, arbitrary simultaneous growth of sample count and
  width, with joint probability convergence and no relative growth condition
  (`:13150–13158`).

The law metric is induced by `|u-v|+|y-z|`. Individual reverse-query tails are
uniformly Gaussian-majorized, but they are **not** a tail bound for the supremum
over time or input (`:12874–12891`). Fixed-program identification precedes
removal of proof meshes and comparison-law errors. No growing-transcript
finite-width theorem or cross-carrier operator-norm convergence is asserted
(`:13102–13107`, `:13126–13148`).

The source explicitly covers zero or duplicated query covariances and requires
neither an inverse-Gram lower bound nor a minimum atom mass
(`:12706–12717`). The unconditional source cap has no bound on atom count,
covariance rank, or finite Euler step count (`:12867–12870`). These are useful
checks against silently introducing a geometry restriction at greater depth.

## 3. The represented numerical family

The exact input consists of five rational numbers satisfying

\[
1/3\le p\le2/3,\qquad
-1/20\le a\le b\le1/20,\qquad
-1/20\le c\le d\le1/20.
\]

With

\[
U(s)=\left(\frac{1-s^2}{1+s^2},\frac{2s}{1+s^2}\right),\qquad
R_*=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix},
\]

the law is the mixture of `(sqrt(2) U(S),+1)` and
`(sqrt(2) R_* U(V),-1)` with weights `p,1-p`, where `S,V` are uniform on their
declared intervals and a degenerate interval is an atom. No pairing between
components is used (`:12629–12656`). Every cross-component normalized dot
product belongs to `[2/5,4/5]`, so the family is explicitly nonorthogonal and
noncollinear without an unspecified small radius (`:12657–12666`).

The rational midpoint input rule has certified `W1` error at most `1/(20m)`;
its normalized coordinates and masses are rational. This is a finite law
description and a convergent quadrature, not an exact Borel-integration oracle
(`:12670–12678`). The family and horizon remain fixed under all refinement.

The theorem is phrased for each separately fixed represented law. A uniform
numerical error rate over the entire rational family, a tolerance-to-resolution
algorithm, or a larger executable law family is not asserted. The implementation
accepts additional finite circle laws through `DataLaw` for exploration, but
broader laws and horizons are outside its guarantee unless separately proved
(`code/README.md:899–903`; the corresponding section was read in full).

## 4. Closure structure, observables, autonomy, and restart

Part B does not merely repackage a width-`n` trained matrix. At each order it
retains bounded initialized observable features on each population, two current
joint populations, and a matrix indexed by retained observable features.
The current row and readout values are unrestricted characteristic values at
population nodes, not degree-limited expansions in initialized features.
The implementation guide states this explicitly (`code/README.md:639–669`;
see also `docs/global_nonlinear.md:13519–13522`).

The retained dictionary includes a polynomial core and an exhaustive bounded
initialized-word prefix; the core alone is not assumed to generate all needed
observable spaces. The grammar includes both orientations of `A_0`. Literal
syntax duplicates remain; neither empirical rank deletion nor deletion of
singular named derivative slots is permitted (`:13170–13184`,
`:13311–13336`, `:13845–13897`).

The positive ridge is `eta_N=1/[1024(N+1)^2]`. The resulting positive filters
converge strongly to the identity; both action directions converge strongly on
compact trajectory targets, and projected learned-increment sources converge
in HS norm (`:13298–13339`, `:13346–13398`). The uniform reference comparison
uses tails of the exact target, not an assumed tail estimate on projected or
numerical trajectories.

The exact finite-order contractions are `(H3.N1)`–`(H3.N2)` at
`:13433–13467`. Evolution uses one matrix `M` and its actual transpose.
Features and frozen joint marks are not resampled independently of their
population coordinates.

The explicit C-H3 numerical observation theorem guarantees:

1. Predictions uniformly on `[0,1/200] × S^1`.
2. Uniform-in-time `W2` convergence of the training-averaged laws
   `Law(h_l(0,u),h_l(t,u))` in each of the two hidden populations.
3. Uniform-in-time convergence of RMS displacement, the `L2` norm of the
   difference of the two coordinates in that paired law.

These are `(H3.N4)`–`(H3.N5)` at `:13753–13771`, with the coupling proof at
`:14118–14139`. Initial and current activations belong to the same mark or
neuron; independently coupling their marginal laws is insufficient. The upper
initial field uses the same frozen `g,b_1,b_2,D` as the current field.
Training input and label may also be retained in the coupled law
(`:14122–14128`).

C-H1/C-H2 have the larger exact-language contract: every separately fixed
admissible same-layer joint tuple, including finite nested actions,
bounded-gate pushforwards, frozen/current observations and quadratic
contractions. This contract is stated at `:12101–12111` and proved for the
observation maps at `:12473–12524`; the grammar is at `:11534–11619`.
Thus one must distinguish that broader exact observation language from the
particular pair-law/RMS observables explicitly included in the C-H3 numerical
theorem. Neither source authorizes arbitrary products of unbounded `L2`
coordinates or arbitrary growing observation programs.

The checkpoint retains `b_1,g,w,p_1,b_2,c,p_2,M,D`, finite data, and arithmetic
metadata. It contains no source tape, absolute clock, earlier velocities, or
growing history. At a step endpoint the same arithmetic, data, step sizes and
block size reproduce the same subsequent working state. The limiting
population restart is proved by uniqueness and stability; restarting a fresh
Heun mesh at an interpolated interior time is not asserted to reproduce the
old mesh exactly (`:14141–14153`; `code/README.md`, “Own-state restart”).

## 5. Exact numerical limits and resource obligations

At fixed closure order `N`, the numerical coordinates are source regularization
`epsilon`, initializer cubature `Q`, population cubature `P`, input midpoint
count `m`, Heun step count `J`, and arithmetic precision `p`. They are distinct
approximation axes (`:13733–13743`). The nested limit is

\[
\lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
\lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}
\lim_{p\to\infty}.
\]

Every intermediate target exists in the stated observation metrics. At each
fixed finite choice of the other parameters, the integer/rational algorithm
succeeds for all sufficiently large precision and converges to the exact finite
computation. Source regularization is unnecessary for the core implementation
but is removed separately for the generic source compiler
(`:13745–13785`). Float64 and Decimal are additional practical backends; the
unbounded-precision theorem is about the integer/rational backend.

The proof covers initializer coefficient integration, complete joint mark-law
replay, singular-covariance regularization removal, finite-order existence and
law stability, time discretization, exact rational input parameters, finite
arithmetic and elementary functions, Cholesky success, observation composition,
and restart (`:13787–14153`). Linear interpolation is in **state**, followed
by recomputation of the nonlinear forward pass. Exact GF loss monotonicity is
not asserted for arbitrary Heun steps (`:13719`, `:14022–14039`).

At equal population node count `P`, retained state has

\[
S=P(d_1+d_2+7)+2d_1d_2
\]

scalars, finite data has `4A` scalars, and work and storage count the complete
marks, fixed and evolving matrices, input blocks, stages, initialization DAG,
coefficients, and scalar bits. A constant number of steps' endpoints or stages
suffices; working memory does not grow with elapsed step count
(`:14155–14241`). The source explicitly distinguishes retained-byte diagnostics
from process peak memory and resource guards from proved bit bounds.

The reusable solver and bounded reproducible runs at several resolutions are
also part of the C-H3 milestone: initialization/runtime/memory/conditioning and
own-state restart must be measured (`docs/README.md:394–427`). The maintained
guide gives the concrete bounded validation recipe (`code/README.md`,
“Bounded validation recipe,” `:905–940`). This audit did not run it.

The following are **not** implied or required: a rate, per-run true-error
certificate, arbitrary diagonal refinement, guaranteed monotonic improvement
with order, a tolerance selector, or affordable computation at every order.
No finite input panel certifies a continuum input supremum. These limitations
are explicit at `docs/global_nonlinear.md:12585–12589`, `:13271–13274`,
`:13779–13785`, `:14176–14178` and `docs/README.md:413–427`.

## 6. Strict activity, geometry, and onset quantifiers

### Separate finite-data corollary C.3

The complete C.3 proof unit (`docs/global_nonlinear.md:3441–3834`) is conditional
on existence of the specified strong population flow. Its sufficient finite
data hypotheses include normalized inputs with `|G_ab|<1` for `a != b`,
nonzero labels, Gaussian first weights, strictly positive initialization
variances and mobilities, zero population readout, and the stated nonconstant
activation conditions (`:3445–3458`, `:3460–3498`). `|G_ab|<1` excludes both
parallel and antiparallel normalized inputs. It does **not** require nonsingular
`G`; C.3 explicitly allows singular Gram matrices (`:3458`).

Its conclusions are positive hidden preactivation and activation onset,
nonconstant positive-definite kernel blocks at sufficiently small positive
times, initial strict loss decrease, and nonaffinity on visited marginals.
For each fixed admissible data instance, a positive interval and positive
constants exist. They may depend on its data and positive parameters; they are
not uniform as inputs approach parallel geometry, labels approach zero, or
other nondegeneracy parameters approach their boundaries (`:3500–3508`).
The exact onset is RMS speed of order `t`, activation/preactivation RMS
displacement of order `t^2`, and squared displacement of order `t^4`; speeds
are zero at initialization (`:3687–3723`, `:3834`).

For weighted probability loss, the exact onset expansions replace each label
`y_a` by `omega_a y_a`. The distinguished quadratic kernel direction is that
weighted label vector, not the unweighted `y` (`:3818–3834`).

The geometry restriction is sufficient for these strict conclusions, not
necessary for existence. C.1 explicitly permits coincident inputs and singular
Grams (`:2468–2471`), zero variances and frozen blocks (`:2513`, `:2530–2533`).
The broader local C.4 statement explicitly excludes restrictions on atom counts,
weights, correlations, coincident inputs, conditional labels, and Gram rank
(`:3856–3862`). C.3 itself exhibits cancellation mechanisms: identical inputs
with opposite labels, or antiparallel inputs with equal labels and odd
activations, may have zero readout forcing and a frozen population
(`:3813–3815`).

### Open active families in C-H1/C-H2

C-H1 fixes an open `W1` neighborhood of the opposite-label orthogonal reference
`nu_* = (delta_(sqrt(2)e1,+1)+delta_(sqrt(2)e2,-1))/2`. Its activity radius is
part of a once-fixed neighborhood, independent of hierarchy order
(`:11480–11491`). Part 8 proves paired squared displacement
`J_l(nu_*,t)=b_l^2 t^4+o(t^4)` with `b_l>0`, then chooses a **common
existential time** `t_a in (0,1/200)` at which both layers move and have positive
best-affine-fit error. Law continuity supplies a positive radius on which all
four quantities exceed half the corresponding reference values
(`:11985–12058`). This is a uniform positive statement over that chosen
neighborhood, not a uniform onset theorem over all nonparallel datasets.

C-H2 takes a smaller fixed ball and inherits this same common `t_a` and
positive values (`:12093–12099`, `:12534–12548`). C-H3's explicit ArcLaw family
is different; Part A establishes its short-time existence separately. Parts
A–C do not assert that every ArcLaw has a common explicit positive activity
margin at time `1/200`, nor that every Borel law is active.

The older broad local C.4 theorem likewise states activity only for an open
family around its specified same-label reference; it expressly disclaims
activity for every law (`:3953–3968`). These reference laws and their positive
times must not be conflated with C-H1's opposite-label reference or with the
two-arc executable family.

## 7. GF, GD, and what a depth extension must still prove

C-H3 Parts A–C identify **actual finite GF** and numerically solve an autonomous
approximation of population GF. The use of finite Euler proof programs and
Heun numerical integration does not turn this into a raw-network GD theorem.
The finite model and physical clock are explicit at `:12603–12605`.

There are related maintained raw-GD theorems: C.1 has every deterministic
`eta_n -> 0` at separately fixed finite depth/batch on an unspecified positive
interval; C.4 has arbitrary simultaneous sample/width/step growth on its
unspecified local interval (`:2550–2571`, `:3930–3944`). Neither statement by
itself proves that interval includes C-H3's explicit `1/200`, and neither is a
complete finite numerical closure theorem. The fixed-depth source estimate
also explicitly disclaims a depth-uniform interval and arbitrary-depth strict
activity (`:3435–3437`).

A faithful depth-extension statement therefore needs to retain, as distinct
obligations:

1. The broad law-domain target flow through the declared positive C-H3-type horizon, with
   canonical coupled action/adjoint initialization at every hidden link,
   actual finite random readout, law stability, and actual finite-GF capture.
2. An executable representation at least as broad as the fixed ArcLaw family,
   with the chosen physical horizon and family unchanged under refinement.
3. A compatible autonomous hierarchy, complete within-population joint state,
   all-layer paired hidden observations, and enough two-direction action
   observations to preserve the declared exact observation language.
4. Convergence of every numerical axis followed by closure order, finite
   precision and complete storage/work accounting, and a reusable finite
   implementation with bounded declared validations when implementation is
   authorized.
5. Strict activity formulated separately on a nondegenerate subfamily with
   explicit quantifiers. It cannot be obtained by changing the existence
   domain or treating the exact zero population initial readout as lazy
   training.

The exact maintained depth-two constants are `1/200` for C-H3 and `40` for
C-H4. The user's requested generalization explicitly allows `[0,T*]` for some
`T*>0` and a substantial-training interval `[0,T]`. Consequently new-depth
positive times may depend on the separately fixed depth; retaining the literal
depth-two constants at every depth is not a completion gate. The new times
must stay fixed under width, law approximation, and numerical/order refinement,
and the long time must be justified to ensure substantial training. An
arbitrary local-existence interval does not establish that latter clause.
At depth two retain the maintained statements. C-H4's other obligations require
their separate Part D audit; Part D was outside this assignment's scientific
reading scope.

## 8. Actual reading coverage and limitations

Read completely:

- `docs/global_nonlinear.md:12555–14245`: C.4.7.10 introduction and all of
  Parts A–C, including the intervening angular-symmetry/kernel remark.
- `docs/NOTATION.md:1–98`.
- `code/README.md:626–940`: complete finite observable-closure guide and
  complete C-H3 numerical solver guide/validation section. The initial read
  extended through the following section's opening at line 943.
- `docs/global_nonlinear.md:3441–3834`: complete C.3 activity proof unit.
- `docs/global_nonlinear.md:3836–3979`: complete C.4 introductory theorem and
  scope description.
- `docs/global_nonlinear.md:11441–11701`: C-H1 introduction and Parts 1–3;
  `:11985–12130`: complete C-H1 Parts 8–9 and C-H2 introduction/Part 1;
  `:12473–12553`: complete C-H2 Parts 6–7.
- The `solve-math-rigorously` and `investigate-conjectures` skills, and the
  latter's `references/research-contract.md`.

Additional bounded reads: C.1 introduction/model/statement at `:2454–2571`,
the fixed-depth source-lemma scope boundary at `:3405–3440`, adjacent section
boundary lines at `:11980–11984` and `:12470–12472`, and roadmap material at
`docs/README.md:264–429`. Searches for section titles and scope terms in the
maintained docs and code guide were used only to locate these dependencies.

No other studies, study history, prior verdicts, external scientific sources,
Git history, implementation source modules, or Part D were read. I did not
re-prove the full fixed-program/common-carrier machinery or audit every theorem
dependency transitively; those are not necessary for this bounded extraction
and remain proof inputs for any new depth theorem. No missing source prevented
the assigned scope distinctions from being resolved.

## 9. Bounded author-side disposition of the draft contract

Read the complete `CONTRACT.md` draft on 2026-09-20, after clarification of the
user's exact horizon wording, and compared it only with this audit and the
allowed maintained sources. No other agent's findings were consulted. This is
an author-side scope check, not an independent review of a theorem or of the
new conditional fitting calculation in contract Section 6.

**Disposition:** The draft correctly separates broad Borel/finite-data
existence, the rational represented numerical family, and strictly active
subfamilies. It does not impose nonparallel geometry on existence or claim
universal Borel activity. All-layer nonlazy onset, general-dimension finite-data
whole-sphere numerics, and every-vanishing-step onset GD are visibly new
objectives. The draft correctly distinguishes actual GF, raw GD, and closure
time discretization. Its numerical limit order, paired observations, complete
joint marks, action/adjoint reuse and own-state restart match the extracted
C-H3 obligations. Depth-dependent new times accord with the user's wording;
the earlier audit recommendation requiring literal `1/200` at greater depth
was too restrictive and has been corrected in Section 7 above.

One substantive completion-standard clarification is recommended. At draft
`CONTRACT.md:236–244`, explicitly require **successful feasible computation at
several declared finite resolutions**, including initialization, evolution,
own-state restart, memory and conditioning diagnostics. The current requirement
for bounded operational validation substantially points there, but the sentence
“Qualitative convergence plus an actual implementation with accounted costs is
the completion standard” could be read as accepting a merely finite algorithm
whose initialization/evolution is never feasibly executed. Maintained
`docs/README.md:418–427` requires feasible computation and measured conditioning,
in addition to accounted cost. This adds no rate, no tolerance selector, and no
cost-to-accuracy theorem.

Two wording clarifications would prevent avoidable ambiguity without changing
the target: qualify population reached-state restart as under the **same
training law**, unless a new switching theorem is intended; and explicitly
state that the construction recovers the maintained depth-two scope/constants
when `L=2`. “Every finite represented dataset” should retain its finite effective
input-description meaning, distinct from mathematical existence for arbitrary
real datasets; the draft already uses the word “represented” and excludes a
Borel-integration oracle, so no weakening was found there.

Part D's exact long-horizon family, constants, and reference endpoint claims
were not re-audited in this check, because that scientific source lies outside
the bounded C-H3 assignment. No edits to `CONTRACT.md` were made.
