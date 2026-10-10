# Independent scientific promotion review B — frozen packet v1

**Overall verdict: PASS on the scientific content.** I found no mathematical
correction required in the proposed addition. Its proofs support the stated
fixed-positive-time predictor gaps, the dense hidden-layer motion, and the
first-layer nonlinear-increment certificate under the chapter's hypotheses
and the addition's nonaffinity/nonparallel-input hypotheses. The addition is
self-contained relative to the supplied Chapter 9 and faithfully translates
the final compact-paper theorem and proof. This verdict does not authorize
promotion or stand in for the separate editorial/rendering checks.

There is one known presentation issue in frozen v1: five proof-anchor lines
immediately precede their fenced proof divs without blank separation. The
supervisor supplied a purely operational notification that a v2 copy repairs
this with blank lines only. I verified the adjacent-line pattern in v1; I did
not inspect v2 or independently render it. This is separate from the scientific
verdict, and no scientific result from another reviewer was supplied to me.

## Scope, isolation, and complete read coverage

This is an original isolated review by `/root/promotion_math_b`, on 2026-10-10.
I read the neutral `PROMOTION_REVIEW_ASSIGNMENT.md`, the complete frozen packet
listed below, and the required rigorous-math and canonical-notation skills,
including the neural-network reference. I additionally applied the
`review-ai-paper` skill and its severity rubric. The assignment requires one
report, so this report incorporates the evidence record, claim audit, and
assembly-code audit instead of creating separate review documents.

I did not read the study README/history, selector report, earlier reviews,
another reviewer's report, Git history, other studies, or `old_docs/`. I did
not call `list_agents`, contact a peer, delegate scientific work, fetch external
scientific sources, execute the submitted assembly script, edit a packet
input/book file, or use Git. My only writes are this assigned report and the
review-owned numerical-check script under the assigned scratch directory.

All eight mathematical/text inputs were read in full: 6,342 lines. The assembly
script's 57 lines and manifest's 42 lines were also read completely, for 6,441
packet lines. No scientific read was truncated. Exact coverage was:

| Input | Complete coverage | Read intervals |
|---|---:|---|
| `08b-trajectory-compression.qmd` | 1–4537 | 1–520, 521–1040, 1041–1560, 1561–2080, 2081–2600, 2601–3120, 3121–3640, 3641–4160, 4161–EOF |
| `PROMOTION_SECTION.qmd` | 1–511 | 1–360, 361–EOF |
| `compact.tex` | 1–298 | 1–EOF |
| `compact_fitting.tex` | 1–241 | 1–EOF |
| `feature_learning_theorem.tex` | 1–62 | 1–EOF |
| `compact_feature_learning.tex` | 1–335 | 1–EOF |
| `index.qmd` | 1–260 | 1–EOF |
| `notation.qmd` | 1–98 | 1–EOF |
| `assemble_promotion.py` | 1–57 | 1–EOF |
| `manifest.json` | 1–42 | 1–EOF |

Here and below, packet filenames mean the files under
`data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v1/review_inputs/`.
References to candidate line numbers mean `PROMOTION_SECTION.qmd`.

The following SHA-256 values were independently checked using `sha256sum` and
the scratch script. Every supplied file agrees with the manifest. The proposed
assembled chapter was reconstructed **in memory from frozen inputs** using the
script's insertion rule; its digest also agrees with the manifest.

| Input | SHA-256 |
|---|---|
| Original Chapter 9 | `4aeaa51c0da24b65acf8b26edb4c4437dbb5dee14a3f336034de7c787faa6571` |
| Candidate | `c04cc608c43cc0c402db40b1f0d4241e71a65eb9cd70bed5dcc18aff82fc307f` |
| Assembly script | `0a8716e6e88678c1f8386f64ee50a54282a3b47892012fc86e2d45b4c43c28e4` |
| `compact.tex` | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| Manifest itself | `40e79ca02b8585f36084bae0598f20c730fce6156d6378d5339c391494ff1023` |
| In-memory assembled chapter | `5ca14b38f84ecfc62644ee0bf9bcadb434f2ff79f1ef3fe422e25c1d92af89b2` |

## Claim and dependency verdicts

| Component | Candidate lines | Verdict |
|---|---:|---|
| Frozen comparator and theorem scope | 1–77 | Sound |
| Nonlinear initial velocity and four witnesses | 84–162 | Sound |
| Initial row laws, reverse conditioning, positive hidden forces | 164–275 | Sound |
| Actual motion, uniform short-time remainders, cubic coefficient | 277–441 | Sound |
| Nonlinear first-layer increment | 443–485 | Sound |
| Transfer to the three predictors and storage | 487–511 | Sound |
| Translation to book notation and paper fidelity | Throughout | Sound |
| Assembly insertion and frozen provenance | Assembly script | Correct by static inspection and in-memory hash check |

The scientific conclusions are highly plausible because the checked arguments
are sound; numerical agreement is not being used to repair a proof. No fatal,
major, or minor **mathematical** flaw was found. There is no new empirical
claim, runtime implementation, or claimed generalization comparison to audit.
No literature-priority claim is made or assessed.

The addition uses the following maintained prerequisites, all available in the
complete supplied chapter:

* The setup, exact zero readout, loss normalization, block mobilities, analytic
  activation class, fixed-data probability convention, and query-domain
  definitions occur in Chapter 9, lines 25–219. They match the addition.
* `lem-compression-fit`, statement beginning at line 223 and full proof at
  lines 300–459, supplies initialization Gram convergence on fixed finite
  query lists, global real fitting, bounded normalized operators/features,
  and residual bounds. I checked the finite-query conditional Gaussian
  argument, including singular covariances, and the real energy/tube argument
  needed here. The candidate does not presume entrywise uniform real bounds
  or a width-independent complex-time radius.
* `prp-compression-legendre`, beginning at line 2401, supplies absolute error
  tending to zero on the whole sphere. `prp-compression-harmonic`, beginning
  at line 4250, and `prp-compression-panel`, beginning at line 4356, supply
  error at most `Y/n` at every fixed confidence. Their entire proofs and all
  intervening source/selection/compiler arguments were read, not just their
  statements. The addition invokes their stated absolute-error and storage
  interfaces with unchanged training data; its extra passive Taylor inputs
  satisfy the declared-panel contract.

The review checks the prerequisites actually invoked and their applicability.
It is not a fresh independent proof of every unchanged constant in the
4,537-line chapter. I found no pre-existing defect that prevents these
invocations. The compact paper names additional `\input` files that are not
in the four-file comparison packet; those are not dependencies of the new
book proof, because the supplied complete chapter contains the requisite
fitting and compression arguments. No missing scientific input blocks this
review.

## Detailed adversarial audit

### 1. Initial geometry, parity, and singular input Grams

Write `v_a=x_a/sqrt(d)` as in the chapter. A real activation with bounded
first derivative has at most linear growth, so its Gaussian Hermite expansion
is in `L²`. If that expansion had finite support, it would agree almost
everywhere with a polynomial. Continuity makes the agreement pointwise, and
bounded derivative makes that polynomial affine. Nonaffinity therefore gives
unbounded positive support in the squared-coefficient covariance series.

The generating-function covariance identity and the completeness argument
in the candidate are valid. The transform used for completeness is entire:
Cauchy–Schwarz against Gaussian exponential moments controls every compact
set of complex arguments and its derivatives. Vanishing polynomial moments
therefore give a zero Fourier transform of the finite measure with density
equal to the function times the Gaussian density.

Composition of covariance series retains nonnegative coefficients. Tonelli
at correlation one proves summability, and a positive inner coefficient of
degree `j>=1` with an outer coefficient of degree `k` contributes positive
degree `jk`. This works for even activations, odd activations, nonzero means,
and unbounded activations with bounded derivative. No centered-activation
assumption is hidden here.

For each integer `k`, the matrix `[(v_a^T v_b)^k]` is a tensor-feature Gram.
Because all off-diagonal absolute correlations are strictly below one, these
matrices tend to the identity as `k` tends to infinity. Consequently a positive
coefficient at a sufficiently large degree makes each hidden covariance
strictly positive definite. The input Gram itself may be singular; it need
not be inverted or positive definite.

I also checked the affine projection. Projecting both variables of the tensor
kernel gives exactly `R_k(v,u)=(v^T u)^k-a_k-b_k v^T u`, with the stated
constant and linear coefficients. This remains a positive kernel. Its
training Gram tends to the identity: the original off-diagonal terms vanish,
and both projection coefficients vanish on spheres of dimension at least one.
The nonparallel assumption with `m>=2` supplies `d>=2`. Thus the weighted
quadratic form in the proof is strictly positive for every nonzero label
vector, including mixed signs; cancellation of all nonlinear components is
impossible.

The four-point witness argument is valid. If every great-circle restriction
were affine, the even part would be a common constant and the homogeneous
extension of the odd part would be linear on every two-dimensional plane,
hence linear globally. On a circle with a nonaffine restriction, three
distinct points determine its affine restriction and a fourth supplies a
nonzero affine dependence. Sign and absolute-sum normalization produce the
claimed lower bound. The chosen inputs depend only on fixed data and
activations, before initialization.

### 2. Gaussian conditioning, adaptivity, and second moments

The reverse conditioning formula has the correct normalization. For an
`n`-by-`n` Gaussian hidden matrix and fixed forward transcript `WH=Z`, the
conditional mean is `Z(H^T H)^{-1}H^T`. Multiplying its transpose by `U` gives
`H Q_n^{-1} C_n`, with both empirical Grams normalized by `n`. The unrevealed
transpose action has covariance `D_n=U^T U/n` in its row coordinates, followed
by the orthogonal projection off the columns of `H`.

The apparently adaptive reverse query does not use the matrix's unrevealed
residual. A forward transcript fixes all successive query matrices. In the
descending reverse pass, only higher-matrix residuals have additionally been
revealed when the current query is formed. Independent Gaussian residuals
therefore remain available for this current matrix. Each is used only once
in reverse. This would not justify arbitrary subsequent reuse, but that is
not the computation made in this proof.

The removed projected innovation has conditional mean squared Frobenius norm
divided by `n` equal to `rank(H) tr(D_n)/n`, exactly as stated. Since the rank
is at most fixed `m` and `D_n` is tight, conditional Markov proves its
vanishing without requiring an unjustified expectation bound on `D_n`.

The empirical `W₂` induction is sufficient, including for the products later
used. Appending independent Gaussian rows gives conditional concentration for
bounded tests and the second-moment law of large numbers. The maps
`phi(z)` and `phi'(z)u` are continuous with at most linear growth, since the
gate is bounded. Such maps preserve `W₂` convergence by uniform integrability.
Products of two retained coordinates then converge in empirical mean because
their absolute values are bounded by a quadratic function. No fourth-moment
assumption on trained fields is introduced. Starting with the complete
first-weight row retains its joint limit with the eventual acceleration row.

Only hidden Grams `Q^(ell)` for `ell>=1` are inverted. Their strict positivity
was proved above, so the empirical inverses exist with probability tending to
one. Covariance square roots allow positive semidefinite limits and require
no extra nonsingularity.

At the top, `L>=2` gives full support for the preactivation Gaussian on
`R^m`. A null vector in the gated-field Gram would force the displayed product
of analytic functions to vanish identically. Its first factor has positive
second moment `y^T Q^(L)y`; the second factor must therefore vanish
identically. Independently varying each coordinate and using the
nonconstant activation derivative forces every null-vector coefficient to
be zero. Downward, the fresh reverse innovation yields the stated positive
conditional covariance lower bound after gating. Every marginal
preactivation has positive variance, and a nonzero analytic derivative has
zero set of Gaussian measure zero.

Finally, expanding the actual force formulas gives squared inverse-mobility
accelerations

\[
E_{1,n}=\|\ddot W^{(1)}(0)\|_F^2/n,\qquad
E_{\ell,n}=\|\ddot W^{(\ell)}(0)\|_F^2\quad(\ell\ge2).
\]

Their limits are exactly `k^4 y^T(Q^(ell-1) circ D^(ell))y`, with `k=2/m`.
For positive semidefinite `Q` and positive definite `D`, the Schur-product
bound `Q circ D >= lambda_min(D) diag(Q)` follows by rank-one decomposition
of `Q`. Its positive diagonal suffices even when `Q^(0)` is singular.

### 3. Actual trajectory remainders and the cubic factor

The zero readout makes every hidden initial velocity zero. The bounded real
fitting tube gives readout and backward-response RMS of order `t`; integrating
the stated flow gives hidden parameter displacement of order `t²` in precisely
the stated inverse-mobility norm. Forward subtraction then gives uniform-sphere
feature and preactivation RMS increments of order `t²`. Readout subtraction
gives the initial prediction expansion with `O(t²)` error. All these constants
are independent of width on an event whose probability tends to one.

I checked the stronger `o_*` convention rather than replacing it by a
fixed-width Taylor remainder. For an initial multiplier field, deterministic
empirical second-moment convergence supplies a fixed tail cutoff whose
squared tail is smaller than any prescribed tolerance with probability
tending to one. Choose that cutoff first, then a deterministic small time.
The candidate's elementary multiplier inequality gives uniform control on
the entire interval and on each joining segment. This establishes its stated
`o_*(1)` gate error. Downward subtraction and integration give the backward
and parameter expansions; no width-dependent third derivative bound is
needed. Multiplication by `O(t²)` increments and time integration preserve
the corresponding stated `o_*` orders.

The adjoint telescoping identity is correctly normalized. The term involving
the layer's own weight increment pairs to
`t² E_(ell,n)/(2k²)+o_*(t²)`; the term through the initialized matrix becomes
the lower-layer pairing. The first-layer normalized input removes any
additional factor of `d`. The final mixed increment has RMS `O(t⁴)`.
Telescoping gives the sum of positive energies up to that layer, and
Cauchy–Schwarz with the bounded initial pre-gated fields proves actual
hidden-feature motion in every layer. It is stronger than merely asserting
nonzero initial acceleration.

For the cubic coefficient, write `K(t)` for the candidate's unnormalized
training tangent Gram and retain the definitions of `k` and `E_(ell,n)` above.
The readout part of `y^T[K(t)-K(0)]y` contributes
`t² sum_ell E_(ell,n)/k²+o_*(t²)`. The hidden tangent terms contribute the
same amount. Thus

\[
y^T[K(t)-K(0)]y
=\frac{2t^2}{k^2}\sum_{\ell=1}^L E_{\ell,n}+o_*(t^2).
\]

Subtracting the frozen equation gives precisely the displayed
variation-of-constants formula, with forcing `(K(s)-K(0))(y-f_n(s))` and
propagator generated by `-kK(0)`. Replacing that propagator by the identity
and `y-f_n(s)` by `y` costs `O(t⁴)`. Integrating the preceding quadratic
coefficient gives `2/(3k)=m/3`. Signs and both normalization factors agree
with the original chapter's loss and block mobilities.

### 4. A nonlinear first-layer component really moves

The nonparallel inputs imply `dim(V)>=2`. Suppose
`phi'(g^T v)(r^T v)` were affine on the unit sphere of `V`, for nonzero
`g,r` in `V`. Its values on the equator perpendicular to `r` and at antipodal
points force its affine constant to vanish and its linear coefficient to be
parallel to `r`. Dividing off that equator and extending continuously would
make `phi'` constant throughout `[-||g||,||g||]`, and analyticity would make
the activation affine. This contradiction applies when `g` and `r` are
parallel or orthogonal, and in the borderline case `dim(V)=2`.

The initial projected row `g` is a nondegenerate Gaussian on `V`. Positive
acceleration energy means `r` is nonzero on a set of positive probability;
independence of `g` and `r` is unnecessary. The squared distance from affine
functions is continuous and bounded by a constant times `||r||²`, so the
joint empirical `W₂` limit transfers its mean to a strictly positive constant.

The actual first-row expansion is adequate in the sphere-times-neuron `L²`
space. On `||r||<=D`, the normalized Taylor error is bounded by the stated
`||phi''||_infinity t²D²/8`; on the complement its bound is
`||phi'||_infinity ||r||`. The second-moment tail argument therefore supplies
the needed `o_*(t²)` error. Contractivity of the orthogonal affine projection
then yields the squared lower bound of order `t⁴`. Neither coordinatewise
convergence nor uniform fourth moments are being silently presumed.

### 5. Transfer, quantifiers, storage, and interpretive limits

The four normalized witness coefficients annihilate every affine predictor,
so their dense linear-in-time gap is a lower bound on uniform distance to
all affine functions. The cubic contraction divided by `||y||_1` similarly
gives a gap at a training input. `Y>0` guarantees this denominator is nonzero.
Each energy limit is strictly positive, allowing common smaller deterministic
constants across the finitely many layers and conclusions.

The probability and time order is correct. The short-time dense estimates
are obtained on one deterministic small interval with probability tending to
one. To transfer them to compressed predictors, fix any positive time in that
interval, then let width grow. Each absolute approximation error tends to
zero in probability. An eventual bound at every fixed confidence suffices:
its failure probability has arbitrarily small limiting upper bound. Relative
variability alone would not suffice, and the proof explicitly uses the
stronger absolute conclusions. No conclusion uniform over arbitrary
sequences of times tending to zero is asserted.

Legendre and Harmonic cover the whole sphere. Taylor's four witnesses are
declared before initialization, require no passive labels, and add no terms
to training or to its Gram inverse. With `s=m+p>=2`,
`(s+4)²/s²<=9` and `(s+4)/s<=3`; hence the stated storage orders are preserved.
The witness count does not become a growing source of samples. The chapter's
finite-real-coordinate and initialization-only contracts are preserved;
there is still no efficient-compilation or finite-precision claim.

The nonlinear feature-motion conclusions are carefully assigned to the dense
reference. Predictor approximation does not identify selected coordinates or
Legendre moments with individual dense neurons, and the addition makes no
such inference. Its second comparison concerns the coupled dense reference's
initial frozen kernel, not all kernel methods. Its first comparison excludes
deep linear predictors, including affine offsets. No endpoint, generalization,
test-risk, uniform-depth, or activation-uniform lower bound is introduced.

## Commands and independently executed checks

All commands ran from `/home/amir/Codes/PDE`, except that file arguments were
absolute. Reads used `sed -n` over the complete ranges above, supplemented by
`rg -n` and `nl -ba` for exact anchors and delicate passages. `wc -l` checked
packet and skill lengths. `sha256sum` checked all packet files. These commands
returned exit status zero.

The independently authored scratch script is
`data/generated/nonlinear_feature_learning_certificate_20261010/review_b/audit_checks.py`,
SHA-256 `2776380f7ce1f42aff02063bcfa03f8a5e9ad56332074ecdc572d9212687d3c7`.
It imports no submission code, makes no external connection, and writes no
files. Its execution command was:

```sh
OPENBLAS_NUM_THREADS=1 python /home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/review_b/audit_checks.py
```

Exit status: **0**. Environment checks found NumPy 1.26.4 and SciPy 1.13.0;
PyTorch was unavailable and was not installed. The actual checks/results were:

1. **Frozen provenance and insertion.** All nine manifest file hashes matched.
   In-memory insertion at the unique assembly heading produced the exact
   assembled hash recorded above. The submitted script was inspected statically;
   its copying/writing operations were not executed.
2. **Singular correlated inputs and activation parity.** Three unit inputs at
   angles `0, 0.37, 1.19` have input-Gram rank two, with eigenvalues approximately
   `(-1.54e-17, 0.649829, 2.350171)`; the tiny negative value is roundoff.
   Exact Gaussian covariance formulas were iterated through three layers for
   `sin(z)`, `cos(z)`, and `z+0.2 sin(z)`. The last hidden Gram's minimum
   eigenvalues were respectively `0.00729286`, `0.00274370`, and `0.00250959`.
   All three activations are nonaffine, holomorphic, and have bounded first
   derivative on any fixed horizontal strip; the third is unbounded on the
   real line. The corresponding numerical four-point witness gaps were
   `0.00574612`, `0.00200698`, and `0.00195774`, with affine-annihilation errors
   below `1.8e-16`.
3. **Nonlinear acceleration direction.** On a 4,096-point circle, the projected
   squared energies for the same three activations were strictly positive for
   acceleration directions parallel to, perpendicular to, and oblique to the
   initial row. The smallest of the nine values was `0.000723715`. This tests
   the geometric loophole; the proof, rather than the grid, establishes the
   continuum statement.
4. **Exact finite-network adjoint algebra and actual trajectories.** Independent
   width-18 networks with the singular input Gram used activation sequences
   `(sin,cos)`, `(cos,sin)`, and three copies of `z+0.2 sin(z)`. Direct finite
   acceleration computations gave maximum relative adjoint-identity error
   at most `4.13e-16`. The dense ODE was solved by DOP853 with relative
   tolerance `2e-12` and absolute tolerance `2e-14`, and compared with the
   exact frozen solution `y-exp(-kK(0)t)y`. Ratios of the observed label
   contraction to the predicted cubic term were:

   | Activation sequence | `t=0.0025` | `t=0.005` | `t=0.01` | `t=0.02` |
   |---|---:|---:|---:|---:|
   | sin, cos | 0.997230 | 0.994471 | 0.988986 | 0.978146 |
   | cos, sin | 0.998590 | 0.997180 | 0.994365 | 0.988749 |
   | linear-plus-sin, three layers | 0.992561 | 0.985196 | 0.970680 | 0.942482 |

   These local algebra checks use moderate nonzero mixed-sign labels, not the
   chapter's exceptionally small sufficient global-fitting cap. They check
   normalization and the cubic expansion, which hold locally without that
   cap; they are not empirical verification of the compression theorem.
5. **Projected Gaussian innovation normalization.** For `n=90`, rank-three
   `H`, and an explicitly nonlinear query determined by the revealed `Z`,
   3,000 fresh Gaussian draws gave removed projected mean square `0.0384706671`.
   The formula `rank(H) tr(D)/n` gives `0.0384646357`, a relative discrepancy
   of `0.000156804`. This is a sanity check of the normalization. Independence
   under the actual forward/reverse transcript was checked analytically above.

## Required corrections, unresolved objections, and confidence

**Required scientific corrections: none. Unresolved scientific objections:
none.** The result retains all the stated degenerate-input, parity, unbounded-
activation, fixed-time, and predictor-only qualifications. The canonical
readout/layer notation, displayed finite-width normalization factors, and
distinction between physical trajectories and compressed coordinates match
the book's contract.

The only known non-scientific issue is the five anchor/fence blank-line
separations described at the start, at candidate lines 93–94, 174–175,
297–298, 457–458, and 487–488. Its claimed v2 repair is outside this frozen
scientific audit and should receive the ordinary rendering check. No input
was silently repaired in this review.

Confidence is high for the addition's mathematics, dependency applicability,
and fidelity to the supplied final paper. Coverage includes every new lemma,
the complete new proof bodies, all supplied mathematical input lines, the
actual time-remainder logic, and independent finite-dimensional attacks.
The numerical checks are deliberately modest and do not claim an asymptotic
reproduction, compressed-runtime benchmark, or independent re-certification
of every pre-existing technical coefficient in Chapter 9.
