# C-X3 hierarchy, initializer, and local-target author cross-check

2026-09-20. **Scoped PASS on the frozen revised files below.** This is an
author-side cross-check by the author of `CH3_HIERARCHY_PROOF.md`, not a fresh
independent promotion review. Two implementation issues found during this check
were repaired by the supervising author and the repaired files were reread
completely before this verdict. One narrow resource-estimate caveat is recorded
in section 6. No theorem for the fitting horizon is approved by this check.

## 1. Inputs and immutable identifiers

The assigned initializer, its tests, the local proof, and the maintained
compiler, word and arithmetic sources were read completely. The hierarchy
proof is the previously frozen author artifact. Maintained scientific sources
were used only within its existing scope and dependencies. No other study was
read. SHA-256 identifiers of the checked revisions are:

| File | SHA-256 |
|---|---|
| `depth_initialization.py` | `cf9504731d72b488f707b5d5bb9b64d1ea62ee95260e21edb749663203163892` |
| `test_depth_initialization.py` | `ab00466e628f20c0b147187dd46c1c9aacb3af1f40c007616b71d1178c748df9` |
| `CH3_LOCAL_PROOF.md` | `8d044f2e56c8d5be30a9739cea7aef52aa565b89b21e266061b41db921a4568b` |
| `CH3_HIERARCHY_PROOF.md` | `e7caf06e3b52d68b54a044efa78cfc3ed26efee12a079f0eb9a681d7e66d19c7` |
| `code/pde/observable_compiler.py` | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_arithmetic.py` | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_fixed.py` | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_words.py` | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `CONTRACT.md` | `ab0b818cc82ac709f32f44e26d2760d79c153dad6a631b48e62a12015018ca6b` |

Study-local filenames in this table are relative to
`studies/cx3_depth_extension_20260920/`; other paths are repository-relative.
The generated eight-test log was also read:
`data/generated/cx3_depth_extension_20260920/initializer_checks.lQ6nwq/tests.log`,
SHA-256 `3cbaa416e4af4d2d958a1c61e94f0355d5be853d9ba3cd6cd82781a909e3172c`.
It records eight passing tests in 0.567 seconds. This checker did not rerun that
suite; the separate counterexample execution described in section 5 is its only
new computation.

## 2. Matrix identities, source groups, and automatic differentiation

For the path architecture there is exactly one matrix between each adjacent
population pair. A node's output population and its operand's population
therefore determine both matrix identity and orientation. `DepthWord` and
`DepthGaussianCompiler._node` enforce adjacency and bounded action operands;
interior population identity alone is never used to choose the matrix.

In `_new_source`, `previous` selects old sources on the target population
whose operands are on the same origin population. These are exactly the same
matrix/orientation calls. `opposite` selects sources on the origin population
whose operands are on the current target; these are exactly the same matrix's
opposite calls. The adjacent other matrix is excluded from both lists.

Each target population has one source index space, containing both incident
oriented groups when it is interior. The Cholesky update initializes the new
row to zero, then fills only indices of `previous`. Inductively each old row
has nonzero entries only in its own oriented group. Hence the selected
triangular solve gives precisely that group's empirical operand Gram plus
epsilon times identity, embedded in the population's block-diagonal covariance
with interleaved indices. Entries linking different oriented groups remain
zero. Separate source slots, rather than empirical rank decisions, are retained
for zero or duplicate inputs.

The response uses `coefficients[s.index]`, where `s.index` is the source's
index in the FULL origin-population list. It does not incorrectly enumerate
the filtered opposite list from zero. This matters when the derivative's
population carries incoming-forward and outgoing-reverse sources together.

The inherited `_partials` is compatible with this layout. Its result has one
column per complete source slot on the differentiated node's population. A
coordinate node propagates the ordinary frozen-coefficient derivative. An
action contributes one to its own named-source slot and propagates only
through its already frozen response operands; it does not differentiate the
opposite-population action operand, covariance factor, integration coefficient,
or Gaussian root. All these response operands lie on the action's output
population. Thus a derivative walk never changes population, and its source
indices remain in the correct full population index space. Multiple paths
are accumulated by addition. Responses involving the other incident edge are
retained when they occur in those earlier same-population expressions.

This is exactly equation (2) of the hierarchy proof and maintained
III.F.9--10's named-source convention. It applies beyond the simple direct
mixed-source example in the test: induction over the finite expression DAG
also covers nested cross-edge response paths. The source independence is
independence of centered groups, not independent action answers.

The test `test_matrix_identity_and_opposite_response` checks zero covariance
between edge-2 forward and edge-3 reverse sources sharing population 2, the
correct opposite inputs, and both named derivative columns. The depth-two
test compares a complete forward/reverse/forward program and its replay
against the maintained compiler exactly. The four-layer test checks type
extension and a third full-row root. These are useful finite algebraic checks;
the structural argument above, rather than finitely many test cases, supplies
the general all-fixed-depth linkage.

## 3. Joint replay, singular limits, dictionary, and precision

`initialize` compiles one union of all populations' retained words, every
forward edge action needed for its contraction, all reverse diagnostics, and
their dependencies. At population ell, `_normal_clouds` allocates one joint
cloud for all source slots, plus all d Gaussian roots on population 1. Distinct
source groups use distinct Gaussian coordinates inside that cloud. It does
not independently sample feature columns or split an interior population's
incident source fields into unpaired tables.

The initializer Grams and forward contractions use Q-point tables. P-point
tables replay the complete graph with the frozen Q-point response coefficients
and Cholesky factors. `_at_count` does not refit them. The returned first-row
g is taken from the SAME P-point first-population cloud as b_1. Different
populations remain separate integration rules; equal row counts or numerically
equal Halton entries do not introduce a cross-population neuron pairing.

The normalization has the required orientation:

    G_l = psi_l(Q)^T psi_l(Q)/Q,
    L_l L_l^T = G_l + eta_N I,
    b_l(P) = psi_l(P) L_l^{-T},
    C_l = psi_l(Q)^T [A_l,0 psi_(l-1)](Q)/Q,
    D_l = L_l^{-1} C_l L_(l-1)^{-T}.

Here row tables use the transpose convention corresponding to column features
in the proof. The runtime's reverse must use D_l^T (and later M_l^T); a
separately integrated reverse contraction is only a diagnostic and is not
substituted or averaged into D_l. The return value contains complete mark
tables, weights, g, D and metadata, with no compiler/source transcript.

At fixed N, epsilon>0 and Q, every exact same-group covariance prefix is its
empirical operand Gram plus epsilon I, so all exact pivots are positive.
Fixed-precision unresolved pivots cause failure, not mode deletion. Increasing
rational precision eventually resolves each of the finitely many positive
pivots. Q->infinity is justified by the maintained Halton polynomial-moment
integration result, applied causally with earlier coefficients frozen. After
that limit, epsilon->0 uses continuity of the positive semidefinite square
root of the complete covariance and expectation continuity of fixed-program
expressions/derivatives. This is the singular-limit argument in hierarchy
section 7.1; no continuity of singular Cholesky factors is required. No code
branch removes a named slot or a rank-deficient feature.

The natural encoding in `decode_prefix` is exhaustive. With
b=L+d and w=6+2(L-1), each constructor has code b+w*k+op. A unary/action
operand index k is smaller than the constructed code. For binary operations,
Cantor-unpaired operand indices are at most k and therefore smaller too.
Every rational has a `rational_code` index; every correctly typed finite
tree consequently has a finite code by upward construction. Invalid types
are skipped, not reinterpreted. Every bounded valid code eventually appears.

The pilot coordinates at population ell are its d initial forward anchor
activations, plus d tanh-transformed reverse anchor responses when ell<L.
Total-degree Chebyshev products give nested finite enrichments; the exhaustive
prefix provides density of the whole initialized observable algebra. Neither
code nor proof assumes that the pilot Gaussian core alone is sufficient.
Literal syntactic deduplication does not identify empirically equal functions.
The schedule eta_N=1/[1024(N+1)^2] is identical to the hierarchy proof.
Consequently that proof's positive-filter density argument applies to the
implemented lists, including their different all-depth natural encoding.

The repaired weak-composition enumeration uses
`combinations_with_replacement(range(dimension), total)`. Its coordinate
counts enumerate the exponent tuples in the original descending
lexicographic order, with no Python recursion in d. The core dictionary
test verifies the intended counts (5,5,3), (35,35,10), (127,126,21) at
L=3,d=2, N=1,3,5 and literal nestedness. These counts establish the finite
lists, not accuracy ordering between successive orders.

The complete maintained arithmetic implementation was checked for how it
is called here. With backend `rational`, fixed-point units, positive-pivot
Cholesky, lower-triangular inverse, range-reduced elementary series and joint
Gaussian generation supply the primitive consistency required by hierarchy
section 7.3. All exact rational syntax and envelopes remain outside empirical
rank decisions. Resource ceilings are adjustable. Optional float diagnostics
now catch unrepresentable/nonfinite values and unresolved SVD results, returning
null without changing the initialized arrays. They no longer impose a float64
range ceiling on rational eventual success. At a fixed feasible resolution,
float64 or fixed rational precision remains an approximation; this check does
not turn its reverse discrepancy or condition diagnostic into an error bound.

## 4. Local proof discharges the hierarchy's target assumptions

The local proof uses the same physical equations, initial row/readout, edge
actions and raw metric as the hierarchy. Its P_l is the hierarchy's q_l.
The following implication checks are sufficient for hierarchy section 5:

| Hierarchy hypothesis | Discharge in `CH3_LOCAL_PROOF.md` |
|---|---|
| One common canonical initialized carrier, actual adjoints | Section 3, with all row coordinates, typed independent edges, generated second moments and adjunction |
| A strong C1 full-row/HS solution on a fixed positive horizon | Sections 4, 6, 7; completion is in the sum of full-row L2, all HS increments and readout L2 |
| Common raw/action bounds independent of hierarchy order and numerical resolution | Section 4, equations (4)--(5), before any mesh/data/width limit |
| Gaussian tails for all backward queries, uniformly in individual time and passive direction | Section 5 equation (13), its explicit positive-mass passive extension, and section 7 Fatou passage |
| Bounded readout | Section 7, equation (23) and the readout equation, giving ||c(t)||infinity<=2t |
| Generated-space invariance and HS support | Common-carrier Euler construction in sections 3--7, followed by L2/HS completion; section 7 also proves the corresponding reached-state invariance |
| One-reference stability with only linear cutoff dependence | Section 6 equations (16)--(20), including every middle rank in HS norm |
| Same-law reached-state uniqueness/restart | Section 7, using the tail-bearing constructed solution as the sole reference |

The passive extension is substantive and valid: at each fixed finite mesh,
add epsilon mass at the desired query with label zero. Joint field continuity
gives L2 convergence of the finite Euler program as epsilon->0. C.2's caps
do not depend on that positive mass. An almost-sure subsequence and Fatou
therefore give the same exponential bound at the original passive query.
After raw Euler completion, apply this argument and Fatou at every fixed
(t,u). The constants remain common to all such pairs. This is exactly the
uniform family of marginal tails required by hierarchy (13), with no false
claim about the tail of sup_(t,u)|P_l|.

The raw comparison does not substitute operator distance for the learned
HS distance. Section 6 explicitly subtracts each rank using its HS product
norm and sums the raw components. The backward induction has one cutoff
factor: a propagated backward error is multiplied by an action norm, while
each new gate error adds R times an already controlled forward difference.
This supplies the C(1+R) comparison used in hierarchy (17)--(18), at every
fixed L. C.2's source constants precede mesh, atom-count/mass and covariance-
rank limits, so they do not secretly depend on hierarchy or quadrature order.

The local generated language is somewhat larger syntactically than the
hierarchy's initialized bounded-word alphabet. Their relevant completions
agree. Every bounded smooth cylinder of already generated coordinates is an
L2 limit of bounded Fourier cylinder words. Linear-growth coordinates and
bounded-gate times L2 fields follow by truncation; initialized actions extend
by boundedness from the dense bounded-word span. Induction therefore places
each local Euler field in the hierarchy's reducing generated spaces. The
HS block support passes under HS completion. This supplies the compact
target query sets and K_l' curves used in hierarchy (14).

Therefore the order-convergence theorem applies to the local solution on
the local proof's T_L for all its stated finite-data and circle-law domains.
The original L=2 horizon 1/200 is still supplied separately by the maintained
C-H3 source theorem; the smaller constructive local T_L does not overwrite it.
The same applies to the separate maintained L=2 C-H4 horizon.

Sections 8--9 of the local proof were read. They give the separate actual
finite GF/GD capture identification needed to name the closure limit as that
local neural target, while retaining the finite random readout and using a
fixed reference program before width limits. This cross-check's central
verdict concerns the target assumptions and initializer linkage above; it
is not a substitute for an independent full review of every path/speed/raw-GD
claim in that author proof.

Nothing in the local proof proves these assumptions through a substantial-
fitting horizon. Hierarchy (25) therefore remains conditional on the required
strong continuation and source-tail control on that longer branch. Numerical
restart cannot replace that missing analytic continuation.

## 5. Issues found and repaired during this check

1. The initial `exponents` routine recursively descended once per core
   coordinate. The assigned finite-dimension domain is not bounded by the
   interpreter recursion limit. After informing the supervisor, this checker
   executed only the deterministic call
   `dictionary(1,3,600,max_features=4096)`. It raised `RecursionError: maximum
   recursion depth exceeded in comparison`, consuming 0.032356732 process CPU
   seconds. This was below the authorized 60 CPU seconds. The supervisor
   replaced recursion with the enumeration checked in section 3. The new
   dimension-600 regression test passes in the frozen eight-test log.
2. Initializer metadata originally required conversions of exact contractions
   and Grams to float64, including a mandatory condition-number SVD. This can
   fail at finite exact values outside float64 range independently of rational
   precision, contradicting unconditional eventual success under sufficient
   resource allowances. The supervisor made both diagnostic paths nonfatal;
   the revised test includes an exact value 10^1000. Inspection of the frozen
   revision verifies that those conversions no longer gate the main result.

Both are closed in the checked hash. This checker changed only this report;
the supervising author made the implementation and test changes.

## 6. Scope, resource caveat, and remaining work

The inherited `_budget` counts node/source tables and retained dimensions,
but does not explicitly add `self.dimension` Gaussian-root columns for a
custom sparse program. For example, constructing a compiler with large d
and compiling only a constant still allocates d first-population Gaussian
columns although its node count is one. Thus the returned resource estimate
should not be advertised as a universal hard peak-memory bound for arbitrary
sparse custom compiler inputs. In the checked `initialize` path every root
appears in the anchor dictionaries, so its node counts already account for
these root columns. The hierarchy's analytic cost formula separately counts
d. This caveat is nonblocking for the checked pipeline and mathematical
initializer theorem; no additional run was made for it.

The eight deterministic tests support the checked finite initialization
mechanisms; they do not prove convergence rates or certify finite-resolution
accuracy. Evolution, observation/restart implementation, resource-accounted
enriched operational validation, every-layer activity and the substantial-
training branch are outside this code check. The source transcript is
discarded correctly, and no trained trajectory is an input. Subject to those
explicit boundaries, the revised initializer implements the hierarchy's
complete initialization and its iterated numerical-limit hypotheses, and the
local proof supplies the onset target required by the hierarchy theorem.
