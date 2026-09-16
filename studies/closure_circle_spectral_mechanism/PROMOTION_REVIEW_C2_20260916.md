# Package C: fresh complete scientific review C2

Reviewer: `/root/review_c2`. Review date: 2026-09-16.

**Conclusion: ACCEPT at the exact written scientific scope.** I found no
required correction and no unresolved mathematical objection. This is one
scientific review, not permission to promote the addition: the second review,
edition validation, independent integration review, user approval and final
correspondence checks remain separate requirements of Part 2.

## Independence, frozen target and complete coverage

I am the newly spawned isolated reviewer assigned C2, not the author,
assembler, selector, coordinator, original lead, or any contributor listed
in the neutral assignment. I received the neutral assignment and manifest
locator without inherited author discussion. I did not read the study README,
historical theory, author validation, selection report, another review,
maintained implementation, full base chapter, assembler, other studies,
task conversations or Git history. No scientific subtask was delegated.

I read every line of the following allowed inputs, including every scientific
line and complete proof in the insertion. Hashes below are actual SHA-256
values, compared with the frozen manifest; all assigned entries matched.
Paths in this table are relative to `studies/closure_circle_spectral_mechanism/`.

| Input | Complete read coverage | SHA-256 |
|---|---:|---|
| `PROMOTION_ASSIGNMENT_20260916.md` | 1–109 | `4a27eb8f5186aabe068d098e2280709d5ac2fb0f61cc096b6c588bcb40ef32b8` |
| `PROMOTION_INSERTION_20260916.md` | 1–263 | `55c9bead5e4db8fc84913f4b78cdd8fc25b3d3c0123fcea8ccc2ee326a0550a3` |
| `PROMOTION_NOTATION_20260916.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `PROMOTION_DOCS_GUIDE_20260916.md` | 1–738 | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `PROMOTION_AGENTS_20260916.md` | 1–62 | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `PROMOTION_WORKFLOW_20260916.md` | 1–225, including all Part 2 | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `PROMOTION_MANIFEST_20260916.json` | Entire JSON | `d18678ce84e7eb8e776d0b6654be827d54bfdfa106c4799fd336d873974bd18b` |

The manifest hash also matches the supervisor's specified hash. The first
batched tool return was truncated in the manifest display; I repaired that
by reading the manifest again completely. I also reread the entire workflow
separately, so its complete coverage does not depend on that batched return.
The guide was read in three contiguous chunks, 1–250, 251–500 and 501–738.
The notation and guide were checked for the candidate's conventions and scope;
I did not independently re-prove the guide's unchanged theorems or follow its
literature links. The excluded base chapter and assembler were neither read
nor used as proof dependencies.

Required skills were read completely:

| Instruction source | Lines | SHA-256 |
|---|---:|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 115 | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 185 | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 121 | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

The only computation was deterministic verification of the assigned formulas,
not a research experiment or training campaign. No additional scientific
source or specialized external theorem was needed. The calculus, parity,
finite linear algebra, analytic-continuation argument, dominated convergence,
and local integral-map contraction used by the candidate are sufficiently
contained for this review.

## Scientific claim audit

### 1. Model, metric and exact finite flow: lines 1–49

**Verdict: accept.** The types and scopes are consistent. Local `p=N` is
explicitly closure order; `P_1,P_2` count quadrature nodes; `n` is neural
width; `d=2` is input dimension. The backward coefficient is distinguished
as a bold vector. The nearby theorem's separate precision symbol is expressly
identified. The underlying neural variances, mobilities, unhalved loss and
physical clock agree with the supplied notation contract. The finite random
neural readout is not replaced by the closure's zero initial readout.

I independently differentiated CS1. With `M` of shape `r_2 × r_1`, its
readout sensitivity is `d a^T`, while the lower-node sensitivity is
`pi_i (b_i^T M^T d) s_i u`. Thus the transpose is the actual transpose of
the same middle matrix. The readout sensitivity is `rho_j H_j`.
Multiplying the ordinary gradient of the unhalved loss by the inverse
metric cancels one factor of each node weight and gives exactly CS2, including
the factor two in all three blocks. `M` has unit Frobenius mobility. In
particular, equal node weights yield the familiar respective particle-count
mobilities; arbitrary positive weights yield reciprocals, with no implicit
clock change. Zero-weight nodes cannot be inverted and are explicitly omitted.

The probability law may be nonatomic, asymmetric or have multiple labels
at the same input; bounded labels and unit inputs make every displayed finite
integral well defined. Nothing requires input covariance nonsingularity or
antipodal data symmetry. At finite state the vector field is smooth in its
coordinates: bounded derivatives and locally bounded parameters justify
differentiation under the data probability integral.

### 2. Antipodal symmetry and fixed-order representability: lines 51–113

**Verdict: accept.** The all-state statement is stronger than a trajectory
symmetry statement and is proved at that stronger scope. Reversing the input
successively reverses `h`, `a`, `H` and `f`; neither marks nor the data law
are transformed. Hence arbitrary asymmetric quadrature nodes and weights
do not invalidate it. Splitting at `pi` gives the exact multiplier
`1-(-1)^k` with the stated `1/(2 pi)` complex Fourier normalization; the
zero-frequency coefficient vanishes as well as the other even coefficients.

The no-cutoff witness does not require a movable dictionary. The first row
of the Cholesky normalization of a constant-first raw list is the positive
constant `1/sqrt(1+eta)`, since the coefficient rule has total weight one.
Therefore the mean lower feature is nonzero and each upper feature vector
is nonzero. These facts justify both denominators in the proposed rank-one
matrix. The node chosen for the readout has strictly positive weight, so its
reciprocal is finite. Substitution gives `a=v_0 tanh(R cos(theta))`, upper
preactivation `A tanh(R cos(theta))` at that node, and exactly CS5 after
weighted readout. The other upper nodes contribute zero because their
readouts are zero. There is no bounded-parameter assumption violated by
choosing a large but finite reciprocal or a large finite `R`.

The nonpolynomial proof is complete. The witness is even in angle; any
finite Fourier representation would be a finite cosine sum, and the given
recurrence converts that sum to a polynomial in `cos(theta)`. A real-analytic
difference vanishing on an interval continues across any proposed finite
endpoint by its convergent Taylor series, giving equality on the whole real
line. A bounded real polynomial must be constant, whereas the derivative of
the nested tanh at zero is `AR>0`. This contradiction rules out a finite
trigonometric polynomial for every finite positive `R,A`.

For the prescribed-frequency strengthening, I checked the ordinary cosine
coefficient separately from the complex coefficient. With `k` positive odd,
the integral of `cos(k theta)` over the two positive-cosine arcs is
`2 sin(k pi/2)/k`; its integral over the complement is the negative.
Bound one supplies an integrable dominator and the two exceptional zeros of
cosine have measure zero. CS6 consequently has exactly the stated factor
`4 tanh(A)/(pi k)`, which is nonzero. Its nonzero limit ensures a nonzero
coefficient at sufficiently large finite `R` for each fixed `k`. This does
not claim one quantitative `R` works uniformly for all frequencies.

The witness establishes representational capability at each fixed retained
dictionary, not reachability from `w=g,c=0,M=D`, a learned spectrum, a
convergence claim, or accuracy ordering across closure orders. Those stronger
claim-ladder bridges are expressly excluded, rather than assumed.

### 3. Conditional order-one/order-two equality: lines 115–213

**Verdict: accept under the stated matched assumptions.** I checked both
mark involutions independently. Simultaneous reversal of `g,zeta` changes
all four lower core marks in sign, including the nested coordinates;
reversal of `xi` changes both upper marks in sign. Each preserves the
specified centered Gaussian law. The constants are positive and finite:
`tanh^2 G` is positive away from a probability-zero point and bounded by
one; this also yields positive `tau`; `sech^2(sqrt(v)G)` is strictly positive
and bounded. Symmetric finite coefficient rules have the same odd-integral
cancellation without requiring exact Gaussian integration.

The Chebyshev recurrence gives parity by total degree, including mixed
degree-two products. Opposite-parity Gram entries vanish. The Cholesky
recurrence in the text correctly proves parity preservation even when parity
indices are interleaved: a nonzero product at a previous column requires
both row indices to have that column's parity. Positive ridge guarantees
positive diagonal pivots even for a rank-deficient finite rule. The inverse
preserves the same subspaces, so raw-feature parity survives normalization.

For an even lower feature, multiplication by the odd vector `tanh(g)` gives
zero expectation. Differentiating `psi(-g,-zeta)=psi(g,zeta)` with respect
to `zeta` shows that its derivative reverses sign; its expectation vanishes
too. The same derivative argument applies to an even upper feature under
`xi -> -xi`. All even rows and columns in the displayed `C` therefore
vanish. The feature-by-two matrix shapes in CS7 agree, and the inverse
Cholesky factors leave only the odd-to-odd block in `D`. No unexplained
Gaussian operator identity is needed: CS7 directly defines this initializer.

The invariant subsystem calculation is valid for an arbitrary fixed data
law. Odd lower `w` gives odd `h`; only odd coordinates of `a` survive.
Odd-to-odd `M` then gives odd upper preactivation and `H`, with even upper
gate. Odd `c` makes only odd coordinates of `d` survive. Hence `q` is odd
in lower marks and the lower gate is even. The three derivatives in CS2
retain the stated parities, and the initialized state belongs to this
subsystem. A globally shared sign reversal between populations is not
required: the two separate involutions suffice.

I checked the existence/uniqueness use, rather than identifying invariance
with a mere tangent calculation. In finite dimensions the locally smooth
vector field has a local contraction on its integral equation. In the
continuum class the unbounded initial `g` is harmless because the norm is
on `w-g` and tanh is bounded and Lipschitz. For bounded features, bounded
`c,M`, and bounded labels, `a,d,q,f` and all products in the vector field
are bounded and locally Lipschitz in that norm. For example, writing
`B_1=sup|b|`, `B_2=sup|beta|`, `C=sup|c|`, `Q=|M|` gives
`|a|<=B_1`, `|d|<=B_2 C`, `|q|<=B_1 Q B_2 C` and `|f|<=C`.
These are precisely the bounded-product estimates invoked by the manuscript,
not an additional premise repairing it. Picard iteration started in the
closed parity subspace stays there. Local uniqueness identifies the result
with the stated solution, and overlapping local intervals propagate the
property along its interval of existence. No general formal population
uniqueness or global extension is inferred.

At orders one and two the only added features are even degree-two features;
the odd lists, order and common coefficient integrations are identical.
Cross-parity zero entries mean intervening even coordinates cannot alter
active Cholesky recurrences. With a shared ridge, both active normalized
features and active `D` coincide. Common evolution nodes/weights (or the
same exact population law), `w=g`, and zero readout give the same active
initial problem. Coefficient and evolution rules may differ from each
other; each must be sign symmetric and each is held fixed across the two
orders. Once inactive coordinates are zero, the two active vector fields
agree. Uniqueness therefore supplies equality of predictions, including
continuum replay under the stipulated characteristic-class hypothesis.

The two stated default ridge values are unequal, so they do not satisfy
the matched-ridge hypothesis. Absence of imposed sign pairs is a further
failure of the sufficient premises. Failure of those premises does not
prove default outputs differ or provide a quantitative discrepancy bound;
the candidate correctly makes neither inference. The exact correspondence
of the named maintained schedule and Halton implementation to the assembled
chapter is an integration check, expressly outside this review's frozen
scientific input scope. It is not imported as a premise of the proof above.

### 4. Evolving kernel, dissipation and frozen comparator: lines 215–263

**Verdict: accept.** Contracting the three independently checked derivatives
against the inverse metric yields CS9 without an extra `pi_i` or `rho_j`:
the squared derivative weights are canceled once by the inverse metric.
The Frobenius inner product of the matrix features factors as
`(d(u)^T d(v))(a(u)^T a(v))`; the lower-vector feature inner product gives
the explicit factor `u dot v`. These formulas remain valid with different
node weights and nonuniform data weights. The kernel is symmetric, but its
scalar entries need not all be nonnegative; positivity is correctly stated
as positive semidefiniteness of each Gram matrix.

The displayed feature maps prove positivity directly. For a general
bounded-label probability law, their finite-state boundedness also gives
the Bochner integrals and Fubini interchange needed to identify the
double-integral quadratic form with squared feature-integral norms.
Differentiating the unhalved loss adds a second factor two to the prediction
flow, giving the `-4` in CS10. Local boundedness along a finite-state solution
justifies the derivative under the data integral. This proves exact GF
dissipation, not monotonicity for Heun or any arbitrary discretization.

At `c=0`, `d=q=0` regardless of `M,w` or the data labels. Thus both hidden
kernel blocks are exactly zero and the full initial closure kernel is the
readout block. Freezing the same initial `w,M` makes `H` constant in time;
the readout equation is linear in `c` and gives precisely fixed-kernel
prediction flow with initial prediction zero. This equality concerns that
closure's own initial kernel at each positive order. There is no assertion
of equality to a full Gaussian neural kernel, stationarity in angle, an
order-zero member, or superiority of full training over the comparator.

## Actual adversarial checks and numerical results

I implemented an independent small NumPy verifier from the insertion's
formulas; no maintained code or author script was executed. Its complete
source is retained below as part of this report, as well as in assigned
review scratch. The gates were written before execution: central-difference
errors below `2e-7`, algebra/parity discrepancies below `2e-11`, Gram
eigenvalues at least `-2e-11`, and absolute selected Fourier coefficients
above `1e-5`. I ran the script once; it completed with exit status 0 and
all gates passed. No failed run or unreported tuning preceded it.

The finite test has `P_1=4`, `P_2=3`, rectangular `r_2 × r_1=2 × 3`, lower
weights `(0.07,0.21,0.29,0.43)`, upper weights `(0.11,0.27,0.62)`, asymmetric
marks, nonzero readout, seven query angles, and five training weights
`(0.03,0.08,0.17,0.29,0.43)`. The local finite-difference step is `1e-6`.
This configuration attacks accidental uniform-weight cancellation, missing
factor two, and a transpose convention hidden by square matrices.

| Attack / competing explanation | Observed result | Consequence |
|---|---|---|
| Differentiate the predictor in every stored coordinate; compare with analytic Jacobian | Maximum error `3.1583360926568105e-11` | Supports all three derivative formulas, weights and actual transpose |
| Compare three explicit kernel blocks with `J G^{-1} J^T` | Maximum error `2.220446049250313e-16` | No missing particle mobility detected |
| Test each block and total kernel for negative Gram directions | Minimum eigenvalues: c `-3.001063228145594e-18`, M `8.37764884714742e-18`, w `2.0826657383356218e-08`, total `3.039127348945455e-07` | Tiny negative c eigenvalue is rounding within the preset gate, consistent with the exact Gram proof |
| Contract nonuniform data residuals; independently compare prediction velocity | Error `2.220446049250313e-16` | CS8 sign and factor two pass |
| Compare loss velocity by directional finite difference and CS10 | Rate `-1.44086871559096`; finite-difference error `8.321054956184071e-11`; exact algebra error `0` | Unhalved-loss factor four passes |
| Reverse input with asymmetric marks/data and nonzero readout | Error `0` | Input parity does not require mark/data pairing |
| Set readout to zero, retaining nonzero middle and first-layer state | Prediction/backward maximum `0`; residual kernel error `1.1102230246251565e-16` | Both hidden blocks vanish at zero readout |
| Construct the rank-one witness with nonuniform selected-node weight | Representation error `2.220446049250313e-16` | Denominator and weighted readout cancellation pass |
| Check witness Fourier coefficients with `A=.83,R=256`, grids 32768 and 65536 | All selected odd coefficients through 41 nonzero; even errors at most `8.326672684688674e-17`; resolutions agree to about `3e-17` | Finite illustration of the analytic no-cutoff argument, not proof for all k |
| Form sign-paired nonuniform coefficient rules and different sign-paired evolution rules at orders 1 and 2 | Cross-parity Cholesky and inactive-D errors at most `1.6219113144268438e-16`; active feature discrepancy at most `1.3322676295501878e-15` | Supports exact parity normalization and matched coordinates |
| Use a nonlinear noninitial parity state and asymmetric data, compare active vector fields | Prediction difference `1.249000902703301e-16`; vector-field difference `8.881784197001252e-16`; w/c parity residuals `0`; inactive-M rate at most `2.2466323207496082e-17` | Tests invariant subsystem beyond trivial zero-readout initialization |
| Deliberately interleave parity coordinates before Cholesky | Cross-parity maximum `9.886174146827578e-17` | No reliance on contiguous parity blocks |
| Break only common ridge (`.031` versus `.083`) | Active-D difference `0.14878471566061963` | Matched-ridge hypothesis has real algebraic content |
| Break only lower sign-pair weights by `+.013,-.013` | Inactive-D magnitude `0.11580681387894465` | Exact sign symmetry is essential to this invariant-subsystem proof |

For parity diagnostics the shared positive numerical core constant was
`alpha=.65`. This is an algebraic test of sign reversal, not an approximation
or numerical certification of the Gaussian scalar constants. The proof
inspection above verifies their positivity and the relevant symmetry.
The diagnostic does not train the closure or compare default runs.

The reported Fourier cosine coefficients on the fine grid are approximately
`0.8664047563515435`, `-0.2887903755146025`, `0.17326077465340273`,
`0.09622983925933593`, `0.04116944045683536`, and
`0.020960696894522513` for frequencies `1,3,5,9,21,41` respectively.
The two-grid comparison is only a guard against a gross numerical artifact;
the manuscript's dominated-convergence proof establishes the universal
prescribed-frequency statement.

The most substantial surviving ordinary explanation is exactly the frozen
readout-only comparator: the kernel identities alone do not establish an
advantage from hidden adaptation. The manuscript leaves that comparison open.
The strongest structural gap beyond the proved scope is reachability of the
high-frequency represented states from the prescribed initialization; the
manuscript also leaves that open. Neither is a gap in its written claims.
No empirical result, stationary Gaussian pair formula, learned spectral law,
closure-order accuracy ordering, endpoint result or new neural/time-limit
claim entered the argument, directly or through the numerical checks.

## Commands, environment and retained evidence

All shell commands ran from `/home/amir/Codes/PDE`. Read commands were:

```sh
cat studies/closure_circle_spectral_mechanism/PROMOTION_ASSIGNMENT_20260916.md
cat /etc/codex/skills/solve-math-rigorously/SKILL.md
cat /etc/codex/skills/investigate-conjectures/SKILL.md
cat studies/closure_circle_spectral_mechanism/PROMOTION_MANIFEST_20260916.json
cat studies/closure_circle_spectral_mechanism/PROMOTION_AGENTS_20260916.md studies/closure_circle_spectral_mechanism/PROMOTION_WORKFLOW_20260916.md
cat /etc/codex/skills/investigate-conjectures/references/adversarial-audit.md studies/closure_circle_spectral_mechanism/PROMOTION_MANIFEST_20260916.json
wc -l studies/closure_circle_spectral_mechanism/PROMOTION_INSERTION_20260916.md studies/closure_circle_spectral_mechanism/PROMOTION_NOTATION_20260916.md studies/closure_circle_spectral_mechanism/PROMOTION_DOCS_GUIDE_20260916.md
nl -ba studies/closure_circle_spectral_mechanism/PROMOTION_INSERTION_20260916.md
cat studies/closure_circle_spectral_mechanism/PROMOTION_NOTATION_20260916.md
sed -n '1,250p' studies/closure_circle_spectral_mechanism/PROMOTION_DOCS_GUIDE_20260916.md
sed -n '251,500p' studies/closure_circle_spectral_mechanism/PROMOTION_DOCS_GUIDE_20260916.md
sed -n '501,738p' studies/closure_circle_spectral_mechanism/PROMOTION_DOCS_GUIDE_20260916.md
cat studies/closure_circle_spectral_mechanism/PROMOTION_WORKFLOW_20260916.md
git rev-parse HEAD
git status --short -- studies/closure_circle_spectral_mechanism/PROMOTION_REVIEW_C2_20260916.md data/generated/closure_circle_spectral_mechanism/promotion_20260916/review_c2/
git diff --cached --name-only
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python data/generated/closure_circle_spectral_mechanism/promotion_20260916/review_c2/verify_c2.py
```

The metadata-only Git checks found HEAD
`04b61a12795734cbfc93830bf0a164bab7d101c4`, no preexisting C2 output, and
an empty staged-path list. I neither staged nor committed files. Read and
verification commands completed with exit status 0. I used `apply_patch`
only to create the assigned C2 verifier and this report. The two hash/line
inventory calls were inline Python using `Path.read_bytes()`,
`hashlib.sha256()`, `Path.read_text().splitlines()`, and manifest comparison;
they inspected only the named assigned inputs, required skills and C2 output.
The final integrity check repeats those same operations and compares the
embedded verifier/results to their scratch copies.

Runtime: Python `3.10.12`, NumPy `1.26.4`, Linux x86-64,
`Linux-5.15.0-151-generic-x86_64-with-glibc2.35`; binary64 arithmetic;
NumPy seed `2026091602`; OpenBLAS and OpenMP thread limits both one.

Retained scratch (relative to repository root):

| File | SHA-256 |
|---|---|
| `data/generated/closure_circle_spectral_mechanism/promotion_20260916/review_c2/verify_c2.py` | `b3c31b97ca665ede156a871ca2f2e689bcc51d894a13d2ffc490bfcc22c09bdc` |
| `data/generated/closure_circle_spectral_mechanism/promotion_20260916/review_c2/results.json` | `85c55042527de605f96f67602ead1e8aa62dc89b219e760c59437aa35fe41047` |

No maintained code/API or empirical campaign is proposed, so no such producer
test or empirical reproduction was required or executed. I did not run a
continuum solver, a full training trajectory, a neural simulation, an assembled
edition build, or default-run comparison. Those unexecuted checks are not
substituted for proof; the exact identities and conditional equality were
reviewed mathematically as detailed above. I leave the surrounding chapter's
placement, links, preservation and maintained-schedule correspondence to the
separately assigned integration review.

## Required corrections, component decisions and final disposition

Required corrections: **none**. Missing scientific dependencies: **none**.
Unresolved correctness objections at the written scope: **none**.

| Component | Claim level | Decision |
|---|---|---|
| Finite-node metric and three-block tangent kernel, including loss identity | Exact finite identities | ACCEPT |
| All-state antipodal oddness and fixed-order non-cutoff representability | Exact structural and existence statements about represented states | ACCEPT |
| Matched sign-symmetric order-one/order-two equality | Conditional exact dynamical equality on the stated intervals/classes | ACCEPT |
| Zero-readout frozen comparator and scope limitations | Exact comparator identity; express exclusions of stronger conclusions | ACCEPT |

Every inserted scientific line is covered by the four detailed audits above.
The line ranges cover 1–49, 51–113, 115–213 and 215–263, with only blank
separator lines between them. The proof inspections establish the verdict;
the numerical attacks independently checked constants, weights, orientation,
normalization, edge cases and hypothesis sensitivity. The candidate was not
silently repaired or replaced. **Final scientific disposition: ACCEPT the
frozen insertion with SHA-256
`55c9bead5e4db8fc84913f4b78cdd8fc25b3d3c0123fcea8ccc2ee326a0550a3`
at exactly its written scope.**

## Appendix A: complete independently written verification source

The following exact source copy preserves the optional diagnostic outside
generated storage. It is not a dependency of the manuscript's proofs.

```python
"""Independent deterministic numerical checks of the frozen Package C formulas.

These checks are diagnostics, not proofs or training experiments. Preset gates:
central differences < 2e-7; algebra/parity identities < 2e-11; finite kernel
eigenvalues >= -2e-11; selected positive Fourier witness coefficients > 1e-5.
"""
from pathlib import Path
import hashlib
import itertools
import json
import platform
import sys
import numpy as np

ROOT = Path(__file__).resolve().parent
RNG = np.random.default_rng(2026091602)
RESULTS = {"python": sys.version, "numpy": np.__version__,
           "platform": platform.platform(), "seed": 2026091602,
           "precision": "float64", "checks": {}}


def record(name, value, bound=None, lower=False):
    value = float(value)
    RESULTS["checks"][name] = value
    if bound is not None:
        assert value >= bound if lower else value <= bound, (name, value, bound)


def forward(w, c, M, b, beta, pi, rho, U):
    h = np.tanh(w @ U.T)
    s = 1 - h*h
    a = b.T @ (pi[:, None] * h)
    H = np.tanh(beta @ M @ a)
    d = beta.T @ (rho[:, None] * c[:, None] * (1-H*H))
    q = b @ M.T @ d
    f = (rho*c) @ H
    return f, h, s, a, H, d, q


def jacobian(w, c, M, b, beta, pi, rho, U):
    f,h,s,a,H,d,q = forward(w,c,M,b,beta,pi,rho,U)
    jw = (pi[:,None,None]*q[:,:,None]*s[:,:,None]*U[None,:,:])
    jw = jw.transpose(1,0,2).reshape(len(U), -1)
    jc = (rho[:,None]*H).T
    jm = np.einsum("aq,bq->qab", d, a).reshape(len(U),-1)
    return np.concatenate([jw,jc,jm],axis=1)


P1,P2,r1,r2 = 4,3,3,2
pi = np.array([.07,.21,.29,.43])
rho = np.array([.11,.27,.62])
b = np.c_[np.ones(P1),RNG.normal(size=(P1,r1-1))]
beta = np.c_[np.ones(P2),RNG.normal(size=(P2,r2-1))]
w = RNG.normal(size=(P1,2)); c=RNG.normal(size=P2)
M = RNG.normal(size=(r2,r1))
theta = np.r_[w.ravel(),c,M.ravel()]
angles=np.array([.17,.6,1.4,2.0,2.6,3.5,5.7])
U=np.c_[np.cos(angles),np.sin(angles)]


def unpack(x):
    return x[:2*P1].reshape(P1,2),x[2*P1:2*P1+P2],x[2*P1+P2:].reshape(r2,r1)


def fun(x):
    return forward(*unpack(x),b,beta,pi,rho,U)[0]


eps=1e-6
J=jacobian(w,c,M,b,beta,pi,rho,U)
Jfd=np.column_stack([(fun(theta+eps*e)-fun(theta-eps*e))/(2*eps)
                     for e in np.eye(len(theta))])
record("stored_coordinate_jacobian_max_error",np.max(abs(J-Jfd)),2e-7)
invmetric=np.r_[np.repeat(1/pi,2),1/rho,np.ones(r1*r2)]
f,h,s,a,H,d,q=forward(w,c,M,b,beta,pi,rho,U)
Kc=H.T @ (rho[:,None]*H)
Km=(d.T@d)*(a.T@a)
Kw=(U@U.T)*((q*s).T@(pi[:,None]*q*s))
K=Kc+Km+Kw
record("kernel_metric_contraction_max_error",np.max(abs(K-(J*invmetric)@J.T)),2e-11)
for label,Kpart in [("c",Kc),("M",Km),("w",Kw),("total",K)]:
    record("kernel_"+label+"_minimum_eigenvalue",np.linalg.eigvalsh(Kpart).min(),-2e-11,True)
dataweights=np.array([.03,.08,.17,.29,.43]); y=np.array([-1.2,.9,-.6,.4,1.3])
r=f[:5]-y
grad=2*J[:5].T@(dataweights*r)
velocity=-invmetric*grad
record("prediction_flow_max_error",np.max(abs(J@velocity+2*K[:,:5]@(dataweights*r))),2e-11)
loss_rate=float(grad@velocity)
record("loss_identity_error",abs(loss_rate+4*(dataweights*r)@K[:5,:5]@(dataweights*r)),2e-11)
record("loss_derivative",loss_rate,0)
def loss(x):
    return np.dot(dataweights,(fun(x)[:5]-y)**2)
record("loss_directional_difference_error",abs((loss(theta+eps*velocity)-loss(theta-eps*velocity))/(2*eps)-loss_rate),2e-7)
record("all_state_antipodal_error",np.max(abs(f+forward(w,c,M,b,beta,pi,rho,-U)[0])),2e-11)
fz,hz,sz,az,Hz,dz,qz=forward(w,np.zeros(P2),M,b,beta,pi,rho,U)
record("zero_readout_prediction_and_backward",max(np.max(abs(fz)),np.max(abs(dz)),np.max(abs(qz))),0)
Jz=jacobian(w,np.zeros(P2),M,b,beta,pi,rho,U)
record("zero_readout_kernel_error",np.max(abs((Jz*invmetric)@Jz.T-Hz.T@(rho[:,None]*Hz))),2e-11)

# Representability, including nonuniform upper weight and rectangular M.
v0=pi@b; j0=1; A=.83; R=2.7
Mrank=A*np.outer(beta[j0],v0)/(np.dot(beta[j0],beta[j0])*np.dot(v0,v0))
crank=np.zeros(P2); crank[j0]=1/rho[j0]
wrank=np.tile([R,0.],(P1,1))
target=np.tanh(A*np.tanh(R*U[:,0]))
record("rank_one_representation_error",np.max(abs(forward(wrank,crank,Mrank,b,beta,pi,rho,U)[0]-target)),2e-11)
for count in [32768,65536]:
    ang=2*np.pi*np.arange(count)/count
    F=np.tanh(A*np.tanh(256*np.cos(ang)))
    coeff={str(k):float(2*np.mean(F*np.cos(k*ang))) for k in [1,3,5,9,21,41]}
    RESULTS["checks"]["fourier_R256_grid"+str(count)]=coeff
    for k in coeff:
        assert abs(coeff[k]) > 1e-5
    record("even_mode_error_grid"+str(count),max(abs(2*np.mean(F*np.cos(k*ang))) for k in [0,2,4,10]),2e-11)


def paired(dim,count):
    base=RNG.normal(size=(count,dim))
    weights=np.arange(1,count+1,dtype=float); weights/=2*weights.sum()
    return np.r_[base,-base],np.r_[weights,weights]


def features(marks,p):
    dim=marks.shape[1]
    indices=[a for a in itertools.product(range(p+1),repeat=dim) if sum(a)<=p]
    indices.sort(key=lambda a:(sum(a),tuple(-x for x in a)))
    psi=[];derivatives=[]
    for a in indices:
        vals=np.column_stack([np.ones(len(marks)) if t==0 else marks[:,j] if t==1
                              else 2*marks[:,j]**2-1 for j,t in enumerate(a)])
        psi.append(np.prod(vals,axis=1))
        grad=np.zeros_like(marks)
        for j,t in enumerate(a):
            if t:
                other=vals.copy();other[:,j]=1
                grad[:,j]=(1 if t==1 else 4*marks[:,j])*np.prod(other,axis=1)
        derivatives.append(grad)
    return np.array(psi).T,np.array(derivatives).transpose(1,0,2),np.array([sum(a)%2 for a in indices])


lc,lcw=paired(4,5);uc,ucw=paired(2,4)
le,lew=paired(4,7);ue,uew=paired(2,6)
# Shared positive constants suffice for these parity/algebra diagnostics.
alpha=.65
def lower_values(roots):
    g=roots[:,:2];zeta=roots[:,2:]
    return np.c_[np.tanh(g),np.tanh(zeta+alpha*np.tanh(g))]


def build(p,eta,lcw_use=lcw,ucw_use=ucw):
    X=lower_values(lc);Z=np.tanh(uc)
    ps1,dx,par1=features(X,p);ps2,dz,par2=features(Z,p)
    dpsi1=dx[:,:,2:]*(1-X[:,None,2:]**2)
    dpsi2=dz*(1-Z[:,None,:]**2)
    L1=np.linalg.cholesky(ps1.T@(lcw_use[:,None]*ps1)+eta*np.eye(ps1.shape[1]))
    L2=np.linalg.cholesky(ps2.T@(ucw_use[:,None]*ps2)+eta*np.eye(ps2.shape[1]))
    C=(np.einsum("n,nkd->kd",ucw_use,dpsi2)@(ps1.T@(lcw_use[:,None]*np.tanh(lc[:,:2]))).T
       +(ps2.T@(ucw_use[:,None]*Z))@np.einsum("n,nkd->kd",lcw_use,dpsi1).T)
    D=np.linalg.solve(L2,np.linalg.solve(L1,C.T).T)
    eb=np.linalg.solve(L1,features(lower_values(le),p)[0].T).T
    ebet=np.linalg.solve(L2,features(np.tanh(ue),p)[0].T).T
    return L1,L2,D,eb,ebet,par1,par2


one=build(1,.031);two=build(2,.031)
for label,pack in [("p1",one),("p2",two)]:
    L1,L2,D,eb,ebet,par1,par2=pack
    for jj,(LL,par) in enumerate([(L1,par1),(L2,par2)]):
        record(label+"_L"+str(jj)+"_opposite_parity_error",np.max(abs(LL[par[:,None]!=par[None,:]])),2e-11)
    inactive=(par2[:,None]*par1[None,:])==0
    record(label+"_D_inactive_error",np.max(abs(D[inactive])),2e-11)
for label,jj in [("b",3),("beta",4)]:
    pidx=5 if jj==3 else 6
    record("active_"+label+"_difference",np.max(abs(one[jj][:,one[pidx]==1]-two[jj][:,two[pidx]==1])),2e-11)
record("active_D_difference",np.max(abs(one[2][np.ix_(one[6]==1,one[5]==1)]-two[2][np.ix_(two[6]==1,two[5]==1)])),2e-11)

# A noninitial parity state stresses nonlinear invariance, with distinct
# coefficient and evolution rules and an asymmetric training data law.
wpar=le[:,:2]+np.c_[.17*np.tanh(le[:,2]),-.21*np.tanh(le[:,3])]
cpar=.37*np.tanh(ue[:,0])-.29*np.tanh(ue[:,1])
oddmatrix=RNG.normal(size=(2,4))
derivs=[];outputs=[]
for label,pack in [("p1",one),("p2",two)]:
    L1,L2,D,eb,ebet,par1,par2=pack
    Mpar=np.zeros_like(D);Mpar[np.ix_(par2==1,par1==1)]=oddmatrix
    fp,hp,sp,ap,Hp,dp,qp=forward(wpar,cpar,Mpar,eb,ebet,lew,uew,U)
    wrdot=-2*np.einsum("q,nq,nq,qd->nd",dataweights*(fp[:5]-y),sp[:,:5],qp[:,:5],U[:5])
    crdot=-2*Hp[:,:5]@(dataweights*(fp[:5]-y))
    Mrdot=-2*np.einsum("q,aq,bq->ab",dataweights*(fp[:5]-y),dp[:,:5],ap[:,:5])
    record(label+"_w_velocity_parity",np.max(abs(wrdot[:7]+wrdot[7:])),2e-11)
    record(label+"_c_velocity_parity",np.max(abs(crdot[:6]+crdot[6:])),2e-11)
    record(label+"_M_velocity_inactive",np.max(abs(Mrdot[(par2[:,None]*par1[None,:])==0])),2e-11)
    outputs.append(fp)
    derivs.append(np.r_[wrdot.ravel(),crdot,Mrdot[np.ix_(par2==1,par1==1)].ravel()])
record("matched_prediction_difference",np.max(abs(outputs[0]-outputs[1])),2e-11)
record("matched_active_vector_field_difference",np.max(abs(derivs[0]-derivs[1])),2e-11)

# Necessary-assumption stress: break ridge matching or sign-paired weights.
different=build(2,.083)
record("unmatched_ridge_active_D_difference",np.max(abs(one[2][1:,1:]-different[2][np.ix_(different[6]==1,different[5]==1)])),1e-6,True)
brokenweights=lcw.copy();brokenweights[0]+=.013;brokenweights[5]-=.013
broken=build(2,.031,lcw_use=brokenweights)
record("broken_sign_rule_D_inactive_size",np.max(abs(broken[2][(broken[6][:,None]*broken[5][None,:])==0])),1e-6,True)

# Arbitrary interleaving: parity zeros survive Cholesky even when odd/even
# coordinates are not contiguous (the fixed p1/p2 identity uses its own order).
XX=lower_values(lc);ps,_,par=features(XX,2)
permutation=np.array([0,5,1,6,2,7,3,8,4,9,10,11,12,13,14])
ps=ps[:,permutation];par=par[permutation]
LL=np.linalg.cholesky(ps.T@(lcw[:,None]*ps)+.031*np.eye(len(par)))
record("interleaved_cholesky_opposite_parity",np.max(abs(LL[par[:,None]!=par[None,:]])),2e-11)
RESULTS["source_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(ROOT/'results.json').write_text(json.dumps(RESULTS,indent=2)+'\n')
print(json.dumps(RESULTS,indent=2))
```

## Appendix B: complete observed diagnostic output

```json
{
  "python": "3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]",
  "numpy": "1.26.4",
  "platform": "Linux-5.15.0-151-generic-x86_64-with-glibc2.35",
  "seed": 2026091602,
  "precision": "float64",
  "checks": {
    "stored_coordinate_jacobian_max_error": 3.1583360926568105e-11,
    "kernel_metric_contraction_max_error": 2.220446049250313e-16,
    "kernel_c_minimum_eigenvalue": -3.001063228145594e-18,
    "kernel_M_minimum_eigenvalue": 8.37764884714742e-18,
    "kernel_w_minimum_eigenvalue": 2.0826657383356218e-08,
    "kernel_total_minimum_eigenvalue": 3.039127348945455e-07,
    "prediction_flow_max_error": 2.220446049250313e-16,
    "loss_identity_error": 0.0,
    "loss_derivative": -1.44086871559096,
    "loss_directional_difference_error": 8.321054956184071e-11,
    "all_state_antipodal_error": 0.0,
    "zero_readout_prediction_and_backward": 0.0,
    "zero_readout_kernel_error": 1.1102230246251565e-16,
    "rank_one_representation_error": 2.220446049250313e-16,
    "fourier_R256_grid32768": {
      "1": 0.8664047563515435,
      "3": -0.2887903755146025,
      "5": 0.1732607746534027,
      "9": 0.09622983925933591,
      "21": 0.04116944045683539,
      "41": 0.02096069689452253
    },
    "even_mode_error_grid32768": 7.632783294297951e-17,
    "fourier_R256_grid65536": {
      "1": 0.8664047563515435,
      "3": -0.2887903755146025,
      "5": 0.17326077465340273,
      "9": 0.09622983925933593,
      "21": 0.04116944045683536,
      "41": 0.020960696894522513
    },
    "even_mode_error_grid65536": 8.326672684688674e-17,
    "p1_L0_opposite_parity_error": 1.8377588349014174e-17,
    "p1_L1_opposite_parity_error": 1.9378610468224114e-17,
    "p1_D_inactive_error": 1.634025576307217e-17,
    "p2_L0_opposite_parity_error": 6.500067670761693e-17,
    "p2_L1_opposite_parity_error": 3.1757735592494486e-17,
    "p2_D_inactive_error": 1.6219113144268438e-16,
    "active_b_difference": 1.3322676295501878e-15,
    "active_beta_difference": 1.1102230246251565e-16,
    "active_D_difference": 1.6653345369377348e-16,
    "p1_w_velocity_parity": 0.0,
    "p1_c_velocity_parity": 0.0,
    "p1_M_velocity_inactive": 4.1100822290446866e-18,
    "p2_w_velocity_parity": 0.0,
    "p2_c_velocity_parity": 0.0,
    "p2_M_velocity_inactive": 2.2466323207496082e-17,
    "matched_prediction_difference": 1.249000902703301e-16,
    "matched_active_vector_field_difference": 8.881784197001252e-16,
    "unmatched_ridge_active_D_difference": 0.14878471566061963,
    "broken_sign_rule_D_inactive_size": 0.11580681387894465,
    "interleaved_cholesky_opposite_parity": 9.886174146827578e-17
  },
  "source_sha256": "b3c31b97ca665ede156a871ca2f2e689bcc51d894a13d2ffc490bfcc22c09bdc"
}
```
