# Two-sample L=3 research contract and claim ledger

Status: full two-label target OPEN, 2026-09-06. The same-label
two-sample subtheorem has a complete modular audit PASS; the
opposite-label global theorem is not proved.
The user authorizes activation redesign and asks for complete resolution,
followed by isolated adversarial audits of a single self-contained proof.
No numerical experiments are authorized.

## Target and fixed model

NEW USER AUTHORITY, 2026-09-06: first seek an unconditional positive
two-input opposite-label L=2 theorem, and permit DIFFERENT fixed
nonlinear activations in different layers. The old same-activation
sentence below is superseded. All admissible angles remain required;
initialization/optimizer/clock and nonlazy/nonlinear obligations remain.
Immediate contract: /tmp/l2-two-sample-proof-0ywjpp/CONTRACT_AND_SEARCH.md.
The L=3 theorem remains open, not replaced by an alleged L=2 completion.

R32/R33/R34 reviews are now completed, ALL 623/496/436 lines read by
root, no required corrections at their recorded hashes. All three
reviewers closed. R32 is deterministic constant-control only; R33 is
an actual-path coordinate identity, whose log-tail estimate also follows
from primal bounds; R34 is the actual zero-readout full homogeneous top
2x2 estimate, not coupled-response control. All scopes stay conditional
where explicit existing-reference premises were supplied.

Newest completed scoped audits: R31 exact local raw GD/GF/observables,
candidate a830c8bfc6d6a398c693fef8669303341a0dc40e12cd498e75e7995f752a8071,
full 357-line modular report read, no required fixes. R30 actual-query
time regularity, candidate e3fd00736b3094a16395b524d4e6ed7a0376b5c4e0c4d2e2b5bdccc5e8d71112,
full 682-line conditional report read, no required fixes. Both reviewers
closed. Softplus has the full local convergence/observations bridge and
separate local nontriviality, NOT global or final single-document PASS.
New R32 constant-control discriminator and R33 actual moving-top-Gram
transverse coordinate are active; exact hashes/status in NEXT.

Latest audit disposition (2026-09-06, supersedes running entries below):
R28 first dependency reports 409/237/748 lines and combined local assembly
report 338 lines are ALL fully read, no required corrections. Local
assembly hash 398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d
now has a complete modular PASS; only its local zero-readout population,
uniqueness, energy and symmetry scope is certified. New local
nontriviality candidate 004e20c23963e2b628c84ece79e97226acc91ef70e3d0f61c554859647fe4258
is under audit; 766-line return fully read, author closed.
R29 energy-preserving bounded-initial-kernel reference construction is
under audit at 464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2.
These references evolve by genuine uncut full gradients and approximate
the canonical initial actions strongly in both directions. Their global
existence and uniform action, if verified, do not yet prove global
convergence to the canonical model. Exact running state is in NEXT.

R28 newer status: root response lemma hash
0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b
has a 409-line full candidate-only conditional PASS report, all read.
Fixed-program identification (862 lines, root fully read) hash
875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603
is under isolated audit by Darwin. Primal/comparison (1042-line return,
all read, canonical input-span map added and irrelevant rescaling removed)
hash 51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f
is under isolated audit by Euclid. All R28 authors and first response
reviewer closed. Root wrote SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md,
hash 398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d;
a full modular isolated audit with the three explicit dependencies is
running. It would discharge R26/R27 existence/energy/symmetry locally,
NOT give the opposite-label global theorem or the final deliverable.

R25 full finite-law report 550 lines, R26 fresh candidate-only report 517
lines, and R27 fresh candidate-only report 325 lines are ALL read by root.
All report no required corrections at hashes 1318581760487566cc467b2952016ce502a4d2da4a2cbf841e15c19e88a9776b,
e222051b6b85c07a23243b4c502ae6db4bbf7a2e7c659d0a4393e18f03522b2c,
and 9f812d0d7ecc5196f699a338fc4f8d4b0b5db6a703e817bdf6ebfc2dae60634b,
respectively. Their exact conditional/finite-law scopes are retained.
Maxwell, Aquinas, and Peirce are closed. No global inference.
Current new work: root develops a mesh/cap-uniform softplus local-response
lemma; Avicenna checks the fixed-program identification extension and
Lagrange the three-cut primal/comparison estimates. These are not yet
returned or verified. SOFTPLUS_LOCAL_BOOTSTRAP_PLAN.md is a plan only.

One scalar activation phi, identical in all three hidden layers, fixed
independently of width, time horizon, input angle, and labels. Its choice
is open. It must retain strict distributional nonlinearity at initialization
and every finite time, and genuine all-hidden-layer feature learning.
No clipping, frozen layer, limiting linear activation, or kernel-only
substitute is acceptable.

Let d be a fixed positive integer. Inputs x_1,x_2 in R^d satisfy
||x_a||_2^2/d=1. Write C_ab=x_a^T x_b/d and rho=C_12.
We include rho in [-1,1), hence antiparallel inputs as well. This stronger
interpretation was stated to the user; exact alignment rho=1 is excluded.
Labels y_1,y_2 belong to {-1,1}. Constants may depend on d, rho, labels,
and each finite horizon. No lower separation uniform in rho is required.

First weights W^(1) are n by d, initialized iid N(0,1/d). Equivalently,
the initial pairs (z^(1)_{1,i},z^(1)_{2,i}) are iid centered Gaussian
with covariance C. Independent W^(2), W^(3) have iid N(0,1/n) entries.
The RESCALED output vector W^(4) has iid N(0,n^-2) entries, independently.
For a=1,2,

z^(1)_a=W^(1)x_a, h^(ell)_a=phi(z^(ell)_a),
z^(2)_a=W^(2)h^(1)_a, z^(3)_a=W^(3)h^(2)_a,
f_a=(W^(4))^T h^(3)_a/n, r_a=f_a-y_a,
L=r_1^2+r_2^2.

The loss is a SUM, so the single-sample clock agrees with the prior proof.
Define delta^(3)_a=W^(4) phi'(z^(3)_a),
q^(2)_a=(W^(3))^T delta^(3)_a,
delta^(2)_a=phi'(z^(2)_a)q^(2)_a,
q^(1)_a=(W^(2))^T delta^(2)_a,
delta^(1)_a=phi'(z^(1)_a)q^(1)_a.
Residuals are not included in delta.

With eta_n=n^-2 the raw updates are

W^(1)+=W^(1)-(2 eta_n/d) sum_a r_a delta^(1)_a x_a^T,
W^(ell)+=W^(ell)-(2 eta_n/n) sum_a r_a delta^(ell)_a
                                      (h^(ell-1)_a)^T, ell=2,3,
W^(4)+=W^(4)-2 eta_n sum_a r_a h^(3)_a.

Thus z^(1)_b+=z^(1)_b-2 eta_n sum_a C_ba r_a delta^(1)_a.
The first-weight metric is d||dW^(1)||_F^2/n, the hidden-matrix
metrics are ordinary Frobenius, and the readout metric is ||dW^(4)||^2/n.
For d=1,x_1=1 the first update reduces to the audited one-sample update.
The orthogonal-to-input-span part of W^(1) is frozen, not an extra dynamics.

Physical time is k eta_n. Interpolate raw parameters linearly, recompute
hidden fields, use right velocities at interior mesh nodes and left
velocities at an observed terminal mesh node. Finite GF uses the raw
increment/eta_n field.

The target includes all-finite-time population existence and uniqueness
from the prescribed initialization and every reached-state restart;
a finite number of current fields/operators on fixed separate neuron
spaces (infinite-dimensional fields/operators are explicitly allowed);
full-sequence joint finite GF / exact GD / population convergence in
probability, compactly in physical time; predictions, loss, both actions
of both hidden matrices and admissible finite probe programs, all four
2-by-2 raw kernel blocks, joint same-neuron two-sample hidden fields,
velocities, path laws in W_2(C([0,T])), and integrated squared velocities.
No operator-norm convergence across different spaces is requested.
No infinite-training-time/width interchange is requested.

Kernel entries:
K^(1)_ab=C_ab (delta^(1)_a)^T delta^(1)_b/n;
K^(ell)_ab=[(delta^(ell)_a)^T delta^(ell)_b/n]
           [(h^(ell-1)_a)^T h^(ell-1)_b/n], ell=2,3;
K^(4)_ab=(h^(3)_a)^T h^(3)_b/n.
They must give dot f_a=-2 sum_b (sum_ell K^(ell)_ab)r_b.

## Authority and provenance

The finished one-sample proof is
/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md,
SHA256 bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e.
The main agent read its full 1789 lines and verified the hash this turn.
It proves the single-input result for phi=1+arctan/10. Its exact final
text has three clean isolated full-proof PASS reviews after four rounds.
It is NOT a two-sample proof, nor a proof for unshifted arctan.

The source PDE-2 task remains paused. All work is in this destination
private directory. Do not resume old agents or modify old proof artifacts.

## Claim ledger

Latest status (supersedes pending identifiers below):
R25 OPPOSITE_LABEL_MODE_RESPONSE.md returned; ALL original 966 lines
read by root, box presentation removed, current hash
1318581760487566cc467b2952016ce502a4d2da4a2cbf841e15c19e88a9776b.
Exact full modal Gaussian system and first-update coefficients; actual
q2_minus first-update RMS <=C Delta(1-rho) uniformly in caps. Not a
later-time continuation estimate. Author Kierkegaard closed; isolated
candidate+P3 reviewer Maxwell 01a077e0-4821-7670-be10-babf6e77ae6f running.

R26 first candidate-only report (372 lines) ALL read, conditional PASS
with no required repairs. Root made optional precision improvements to
centering, L2/path domains, symmetry index range, and exact versus auxiliary
middle remainder. Current hash
e222051b6b85c07a23243b4c502ae6db4bbf7a2e7c659d0a4393e18f03522b2c.
Popper closed; fresh reviewer Aquinas 01a077e0-487e-7111-a0f2-a627a5d041ae
running, CONVEX_GATE_CURVATURE_ACTION_REVIEW_2.md.

R27 first candidate-only report (369 lines) ALL read, conditional PASS
with no required repairs. Root clarified bounded operators, path integration,
symmetry range and that the WHOLE expression is rewritten; constants unchanged.
Current hash 9f812d0d7ecc5196f699a338fc4f8d4b0b5db6a703e817bdf6ebfc2dae60634b.
Cicero closed; fresh reviewer Peirce 01a077e3-3d4b-7863-a888-9318a2b159dc
running, MIDDLE_CURVATURE_MODE_ACTION_REVIEW_2.md.

Root critical path: SOFTPLUS_LOCAL_BOOTSTRAP_PLAN.md records an UNVERIFIED
route to restore local Gaussian response/cut removal for the new unbounded
activation, using a third analytical readout cut, linear-growth primal
bounds, forward-source Gaussian chaining, and O(S) response rows. It is
not a theorem or an existing result. Complete this construction before
claiming R26/R27 premises are realized for this activation. Global opposite-
label historical response remains open even if this local route succeeds.

R27 new root candidate MIDDLE_CURVATURE_MODE_ACTION.md, SHA256
13eb30bc81437f27d1c341243f69266ccfd95ff35b887789d9f986663625e473.
For phi=1+e softplus, e=.1, the exact scalar identity
phi''(z_a)q_a=A delta_a+B q_a has the SAME coefficients for a=1,2:
A=1-(phi'(z1)+phi'(z2))/e, B=phi'(z1)phi'(z2)/e, |A|<=1,B<=e.
Thus it preserves both sample modes. Actual q2_modes=W3*delta3_modes
and full gradient action give integrated ||M2_minus||2^2 and
kappa2||M2_plus||2^2 bounds by C(initial ops,S)g(S), with NO inverse
contrast. This improves R26's initially uncancelled mixed middle term,
but still does not control curvature times historical sensitivity or
tails. Existing uncut gradient energy/symmetry are explicit hypotheses.
Candidate-only reviewer Cicero 01a077dd-7280-7cd3-af11-2ca0af1c86f2 is
running, output MIDDLE_CURVATURE_MODE_ACTION_REVIEW.md. UNVERIFIED.

R26 new root candidate CONVEX_GATE_CURVATURE_ACTION.md, SHA256
f83192ffc92fa36aeabe4cd6042b3c5291cd7180a78064dbc8d35bf1682b0ce0.
Fixed phi=1+0.1 softplus(z). Its gate is positive/monotone, and
|phi''(x)-phi''(y)|<=|phi'(x)-phi'(y)|. A scalar ODE argument rules out
this global property for any bounded nonconstant nondecreasing C2
activation with bounded derivative. Along an EXISTING uncut opposite-
label gradient path with energy/symmetry premises, the top curvature
modes satisfy |M3_minus|<=|delta3_minus| and |M3_plus|<=|delta3_plus|,
hence integral(||M3_minus||2^2+kappa2||M3_plus||2^2)<=g<=1. The middle
mixed term and curvature times historical sensitivity remain unbounded
by this argument. Positive feature floor retained, bounded feature
ceiling LOST; no old bootstrap or readout-L-infinity transfer. Initial
Gram/nonaffinity checks only, no all-time nonfreezing. Isolated candidate-
only review by Popper 01a077d9-965a-7890-abb6-733a7863950a is running;
output CONVEX_GATE_CURVATURE_ACTION_REVIEW.md. UNVERIFIED pending review.

R25 new bounded sidecar: Kierkegaard
01a077d6-74b0-7682-8c81-e8eb9d76e9ea writes OPPOSITE_LABEL_MODE_RESPONSE.md.
For shifted arctan, derive the exact full finite Gaussian law in sample
average/difference modes, including coupled modal cuts, distinct formal
slots, Gaussian source independence/covariances, and both learned matrices.
Test an actual coefficient/contribution cancellation hidden by absolute
row sums. This is NOT a generic Gram-to-tail inference. Not returned yet.

R24 final scoped result SHIFTED_HARMONIC_CAUSAL_RESPONSE.md, 878 lines,
SHA256 fbb08acfe9decd7e4797266be32a68b6a5a84e892e50ae1acb958b10353770ae.
All 876 original candidate lines and first 569 review lines were read;
one required overstatement repaired (historical covariance can still be
zero at the first update), box presentation removed. Fresh second review
363 lines ALL read, PASS with no required repairs, exact hash unchanged.
Audits concern the stipulated finite Gaussian law plus P3 local estimates,
NOT a new finite-width identification. Current B3=-f exactly, |B3|<=s/200,
and its accumulated signed identity are certified. Full retarded formulas
retain a covariance with historical sensitivity. A two-update canonical
finite-law calculation gives a positive residual in a specified weighted
test; no factorization or automatic dissipativity is valid. No full
historical response bound or global theorem. Sign-changing harmonic gates
require separate nonlinearity/nonfreezing proofs. Archimedes, Beauvoir,
Anscombe closed. Earlier R24 active entries are superseded here.

R23 final scoped status: both fresh second-round reports read in FULL
(878 and 657 lines), no required corrections on unchanged 478-line hash
9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a.
POSITIVE_TIME_MIDDLE_CURVATURE_REVIEW_2.md verifies the candidate and
explicit imported dependencies; POSITIVE_TIME_MIDDLE_CURVATURE_PROBABILITY_REVIEW_2.md
sees ONLY the candidate and certifies the new implication conditionally
on its explicit local premises. Optional presentation suggestions do not
change the mathematical verdict. Both reviewers closed. Thus the actual
positive-local-time compact-preactivation query tails and full directional
Hessian/non-Lipschitzness statements are scoped-audited. Neither implies
global failure, nonuniqueness, or a finite-width positive-time Hessian
theorem. Earlier pending entries below are historical, superseded here.

R24 bounded actual-response sidecar active: Archimedes
01a077c0-309a-7361-9f32-b373e3a740ce investigates only
phi(z)=1+(sin z+cos z)/20 in the opposite-label mode, preserving the
old local numerical bounds. Candidate observation: phi''=-(phi-1),
sample-exchange readout symmetry gives E W4=0, hence the expected
current top curvature E[W4 phi''(Z3_a)]=-f_a exactly, and the current
forward-source response coefficient should equal this value. This is
NOT the already failed trace-to-full-norm shortcut. The bounded task
must retain correlations with historical source sensitivities and test
whether any actual weighted causal response is newly controlled.
Expected output SHIFTED_HARMONIC_CAUSAL_RESPONSE.md. It is not returned
or verified. Gates can change sign; old positive-gate nontriviality
arguments must not be imported unchanged. No theorem transfer claimed.

R23 first audit round complete: both reports fully read (953 and 660
lines). The new Gaussian lower-tail argument passed; required precision
repairs were centering, the time factor in the Taylor cross error, explicit
odd-cut equivariance/symmetry, and separation from a restartability claim
not proved by the displayed premises. Root repaired all, supplied ordinary
second-derivative details, and separated cap Q from threshold R.
Current 478-line hash
9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a.
Godel/Arendt closed; a fresh two-review round is running. No promotion yet.

R23 new root candidate POSITIVE_TIME_MIDDLE_CURVATURE.md, 435 lines,
SHA256 0b2999b92442dbbd1f43faff3202eb79a62453271b43f2d10a90e263fa34b78d.
UNVERIFIED under two fresh isolated audits. It seeks actual fixed-positive-
local-time Gaussian LOWER tails of q2 while Z2 stays in any fixed interval.
The proposed proof uses the finite Euler Gaussian law, two scalar source
regressions, cap/mesh-uniform source chaining, and source-coordinate
surjectivity with all response coefficients fixed. It does not assume an
already constructed continuous source-kernel representation. A further
rank-one raw direction calculation would make both signs of the full
population loss Hessian unbounded at those reached states. This would
rule out local L2-Lipschitz gradient at those states, NOT the already
proved local Osgood flow or the global target. No finite-width positive-
time Hessian statement is claimed. Godel audits candidate+explicit
dependencies; Arendt sees ONLY candidate, treating its local premises as
hypotheses and checking the new probability implication independently.

R22 completed scoped audit: ACTUAL_GAUSSIAN_INITIAL_HESSIAN_TEST_REVIEW.md,
all 609 lines read by root. No required corrections, unchanged candidate
hash 8068a63d710643d06020701a19d5d90260bf02ce5300d158fe52bd4b10546407.
The full physical dot J-kappa J^2 has diverging maximum eigenvalue at
actual independent Gaussian initialization, while J and the specifically
listed primal norm tuple are tight. This is a fixed-data, time-zero,
operator-bound obstruction only. Hidden raw Frobenius norms are NOT tight;
no fixed-positive-time or integrated/global failure follows. Herschel closed.

2026-09-06 newest completed audit round (supersedes pending entries below):
R19 fresh isolated review 2: all 820 lines read by root, no required
corrections at the static-law/conditional-crossing scope. Current hash
43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51.
R20 fresh isolated review 2: all 362 lines read, no required corrections
conditional on the stated R19 static theorem, now separately audited.
Current hash 65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8.
Their checked interfaces give actual local feature-query remainder
O_L2(t^(9/2)) and positive-probability endpoint sign reversals, separately
for every named layer/sample query, all labels and rho in [-1,1).
This is not R19's stronger physical-time remainder premise (A), a fixed
physical endpoint ratio, or scalar q1 continuity. No global inference.
R21 complete isolated modular review: all 613 lines read, no required
mathematical corrections. Current hash
f7cfaf82de5ba25a7b8429435366a2919c2c82e15cf132d2525e4b260c602302.
The full SAME-LABEL theorem thus also holds for the fixed sech-gate
activation, with all observables and nontriviality obligations. It does
not resolve opposite labels or the final one-document audit goal.
Newton, Hypatia and Sartre closed. No candidate bytes changed after review.

R22 root draft ACTUAL_GAUSSIAN_INITIAL_HESSIAN_TEST.md, SHA256
8068a63d710643d06020701a19d5d90260bf02ce5300d158fe52bd4b10546407,
is UNVERIFIED under fresh isolated audit by Herschel. It tests the full
physical negative-loss-gradient Jacobian J at actual Gaussian initialization,
including small nonzero readout: allegedly J is bounded in probability but
lambda_max(dot J-kappa J^2) diverges. This would exclude a primal-only
pointwise signed-Jacobian bound, not global MF, fixed-positive-time bounds,
or integrated response control.

2026-09-06 latest scoped additions (supersede earlier pending statuses):
R20 first audit (405 lines all read by root) accepted all analytic
remainder/probability steps conditional on the static-law premise, but
required the correct label-dependent exchange transformation and the
updated R19 hash. Root fixed both, expanded the common-space truncation
argument and a.e.-time sign interpretation. Current 433-line SHA256
65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8;
fresh isolated audit running. First reviewer Galileo closed.

R21 SECH_SAME_LABEL_GLOBAL_TRANSFER.md, SHA256
f7cfaf82de5ba25a7b8429435366a2919c2c82e15cf132d2525e4b260c602302,
is a new root modular transfer under complete isolated audit. The old
same-label proof needs only the old bounds plus two new scalar checks:
phi(1)-phi(-1)>0.1*pi/2, and sech(18/5)/sech(1/2)<1/4 with
sech(1/2)>4/5. These preserve its forward separation, backward positive
Grams and all-time nonlinear/nonlazy conclusions. This is NOT an
opposite-label theorem; no global goal completion is claimed.

R19 first isolated review (799 lines all read by root) accepted the
static law and conditional crossing but required explicitly stating
the physical raw GF normalization within the candidate. Root supplied
the full raw equations, metric and kernels, expanded the empirical
higher-moment proof, removed a misleading optional variance shortcut,
and specified scalar-path continuity. Current 744-line candidate SHA256
43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51.
A fresh complete isolated audit is running. First reviewer closed.
R20 remains unchanged under its audit; its old R19 dependency hash
will need an explicit version update after the pending reviews.

R19 returned SECH_ACTUAL_CONTROL_SIGN_TEST.md, 657 lines all read,
SHA256 0687a11f279d5b6c2436f127fc48f7e7b73bfd51a6c0fa73c7814aaf242da336.
It computes the actual initial linear/cubic query program and claims
positive definite fresh cubic innovations at both reverse layers,
all labels/rho including -1. It explicitly leaves an actual population
Taylor remainder open. Under isolated audit; author Kuhn closed.

R20 root SECH_LOCAL_JET_AND_SIGN_BRIDGE.md, SHA256
f01a27e434f03c7cfcca22199b929dd3d1dc97ca807c0c9279378d6a5d9f8d82,
is under a separate fresh audit. It transfers the bounded-constant local
construction, constructs a raw polynomial comparison path with only an
auxiliary readout cut, and uses static jet moments plus cap R=t^(-1/4)
to obtain an L2 O(t^(9/2)) cubic-query remainder. No Lp operator bound
or C4 population assumption is used. Combined with the pending R19 law,
this would give actual local sign crossings with probability >=c t^2.
Both R19 and R20 remain UNVERIFIED until their audits are read/repaired.

R18 now has a complete isolated scoped PASS on unchanged hash
c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24.
Root read all 405 review lines. No required mathematical corrections;
optional clarifications and a smaller exponent do not change validity.
Reviewer Dalton is closed. The new actual-control sign discriminator
is being developed by Kuhn, not yet a returned or audited result.

R17 GAUSSIAN_GATE_SIGN_SWITCHING_TEST.md, SHA256
cd97bafe6125f53e67f05751efb0ffbb9b16368ab88a50fa9f419a258a91cb4d,
has a complete isolated scoped PASS. Root read all 559 review lines;
no required corrections. The exact periodic exogenous-control return
has an expanding tangent eigenvalue and rules out a universal polynomial
bound for sign-changing controls. It is NOT actual trained dynamics.
Reviewer Lorentz is closed.

R18 SECH_GATE_ACTIVATION_DESIGN.md, SHA256
c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24,
is a root candidate under isolated audit. Fixed activation
phi(z)=1+0.1 atan(sinh z) keeps the positive bounded range, old local
derivative bounds, both initial modes, and the arctan relative-gate
inequality |phi'(z)-phi'(z')|<=|phi(z)-phi(z')|. Exponential gate tails
give a polynomial frozen-control sensitivity bound uniform in initial
state for changing control ratios inside a fixed sign quadrant.
The Gaussian gate R16 loses the relative-gate inequality, motivating
this refinement. Actual signs, feedback, and control-cost moments remain
open; no transfer of the global trained-network theorem is asserted.

T0 — target above: OPEN.
I1 — raw two-sample equations and kernel normalizations: directly derived,
pending a dedicated self-contained derivation/audit.
P1 — one-sample theorem: PROVED/AUDITED, authority above.
H1 — exchange symmetry may reduce limiting residuals to one label mode:
UNPROVED candidate; finite-width symmetry is in law, not pathwise.
H2 — phi=1+arctan/10 may still suffice: UNRESOLVED.
O1 — the positive activation floor alone gives no positive lower bound on
the opposite-label contrast readout kernel: elementary algebra, to write
precisely. This is a failure of the old coercivity argument, NOT a
counterexample to the target or to the activation.
O2 — the componentwise one-sample F transform no longer cancels the
cross-sample first-layer gates: exact differentiation to document.

## First research-cycle results and audit boundaries

P2 — EXACT_TWO_SAMPLE_REDUCTION.md, current hash
432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60:
scoped reduction PASS from a fresh second reviewer, Kepler, after the
first review identified missing symmetry/clock/initialization premises.
The root read both complete reports (760 and 566 lines). The second
review found no required mathematical correction; optional wording
suggestions remain recorded in EXACT_TWO_SAMPLE_REDUCTION_REVIEW_2.md.
This is a reduction/route-obstruction PASS, NOT a theorem PASS.
It establishes exact finite normalization, finite symmetry IN LAW,
conditional deterministic population label reduction, a no-flattening
lemma for generic correlation, positive initial contrast of order
epsilon^6(1-rho), and no angle-uniform bounded feature fitting interval.

P3 candidate — TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, current hash
9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170:
the first independent audit checked the scalar estimates and constants,
but required a correct zero-variance formal-derivative base case,
explicit finite realization, and a negative-label sign correction.
The root read its full 487-line report and repaired all three.
A fresh full second audit is running. The candidate uniformly bounds
B^(3) rows by 3067/3200 and B^(2) rows by
71063018523/73728000000<.97, with exponential-square tails for BOTH
raw backward queries, on feature time [0,3/2], all input correlations
and both label modes. No opposite-label global continuation follows.

P4 candidate — SAME_LABEL_GLOBAL_ASSEMBLY.md plus
SAME_LABEL_NONTRIVIALITY.md assemble an all-finite-physical-time,
full-observable same-label theorem from P2/P3 and imported Gaussian
arguments. The first raw coordinate is not transformed. Both queries
are clipped in the references, then removed; finite physical paths
are compared directly, including their off-mode residual. A complete
isolated modular audit is running. NOT YET PROMOTED.

H3 candidate — SHIFTED_ARCTAN_CONTRAST_ROUTE.md:
readout norm convexity on any existing zero-readout contrast-ascent
trajectory preserves a positive initial contrast kernel. It also gives
an exact contrast-weighted squared backward action budget up to fitting.
The root read the entire 406-line note. Its applicability to internally
clipped references is NOT established; only full-gradient positive-
contraction regularizations preserve its stated energy mechanism.
No isolated audit or global-tail consequence is claimed.

O3 candidate — ACTIVATION_STRUCTURE_ROUTE.md:
phi=sin+cos retains both initial label modes and strict initial
nonlinearity. Harmonic curvature gives a trace identity, but an explicit
noncanonical-initialized stationary state has expansion despite zero
trace. The root read the full 584-line report. Its scope is a failure of
the trace-to-response mechanism, not failure of this activation or the
target. No independent certification is claimed or needed to declare
that no proof resulted from this route.

P3 final scoped status: the fresh complete second audit by Franklin
returned PASS with no required repairs on the unchanged hash
9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170.
The root read all 455 lines of TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP_REVIEW_2.md
and closed the reviewer. P3 is now PROVED/SCOPED-AUDITED, not a global
opposite-label theorem.

R4 return — AFFINE_TAIL_ACTIVATION_ROUTE.md (549 lines, all read by root):
phi=z+1+tanh(z)/2 has exact approximate Gram-balance identities and
bounded trained balance drift on each finite physical horizon.
An actual-Gaussian-initialization calculation refutes a width-uniform
maximum-norm Lipschitz onset for W^(4)phi''(Z^(3)_a), because the OTHER
sample's activation remains unbounded while this sample lies in a
curved region. This does NOT refute fixed-positive-time bounds,
integrated curvature traversal, or the activation's global theorem.
No isolated audit has been commissioned or certification asserted.
The agent is closed.

SOURCE_SCREENING.md records two new primary-source scope checks.
Neither is a proof dependency or a claimed complete theorem audit.

P4 scoped status supersedes its earlier pending status above:
SAME_LABEL_ASSEMBLY_REVIEW.md (576 lines, all read by root) is a
complete isolated modular PASS with no required mathematical repairs.
Reviewed assembly hash:
2ad0d70ec48eb56dc4170c90df1075e02c8d208913e2dd4fcb4f77d2702baa57.
Reviewed nontriviality hash:
76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6.
The root incorporated its two presentation corrections: state the
actual C2 clock regularity rather than unspecified smoothness, and
include the completed nontriviality supplement in the dependency/scope
statement. The assembly consequently has a new hash, to be recorded
separately. No claim of several final single-document audits is made.
The reviewer is closed.
Corrected assembly hash:
510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44.

R5 return — WEIGHTED_RESPONSE_BRIDGE.md (563 lines, all read by root):
the finite-source first-chaos matrix inequality controls actual
expected-response L2 norms; contrast energy bounds the learned shift;
current two-feature projection is bounded using its Gram floor.
An explicit temporal innovation remains. Smooth bounded arctan
histories with Gaussian initialization and bounded action yield
expected-derivative response rows with no uniform Lp bound for any
p>2 and no uniform exponential-absolute tails. The construction
retains Gaussian source covariance and raw arctan gates, but NOT the
actual trained causal recursion. Thus only the proposed implication
from first-chaos/action/current-Gram/gate controls is falsified.
This is not a canonical trained-trajectory counterexample, not an
audited theorem, and not a refutation of the short causal bootstrap.
The agent is closed.

R6 return — TWO_SAMPLE_KILLING_FRAME_TEST.md (481 lines, all read by
root): for 0<|rho|<1, a common smooth positive definite Riemannian
metric making both fields X_a=phi'(z_a)Ce_a Killing cannot exist for
any smooth nonaffine phi with positive bounded derivative. The proof
uses the derivative of a bracket-corrected Killing field at its zero;
the diagonal condition forces phi' convex, hence constant if bounded.
No uniform metric equivalence is required. The two older named
activations also fail locally on every open set, by metric-area
compatibility. This is a new scoped structural no-go, not a theorem
counterexample and not independently audited. The agent is closed.

R7 active — signed integrated top curvature. A sidecar examines the
exact frozen-lower-Gram neuron equations, and what changes under
time-dependent Gram and actual lower-layer forcing. It now also tests
the convex strongly monotone activation phi=z+log(1+exp z), whose
logarithmic gate range is bounded. No full-network inference is made
from the frozen subsystem.

R8 candidate — CONVEX_AFFINE_TAIL_BASELINE.md: the new fixed activation
has both initial label modes (including antiparallel inputs), initial
strict nonlinearity, and dimension-uniform finite GF/exact-GD primal
and integrated hidden-velocity bounds. Its raw Hessian on a fixed
primal ball is O(sqrt(n)), so eta=n^-2 permits the finite GD energy
argument. An isolated audit is running. These statements do not
identify any global population limit or prove nonlinearity after
training; the new activation is an eligibility candidate only.

R7 return: root read all 812 lines of AFFINE_TAIL_TRAVERSAL_TEST.md,
SHA256 62c5d8e96afa12ddc8496a1a2f59b0d2b854cb961e2d52486c9d4502c5e0cf2d.
It proves a genuine complete top-neuron propagator estimate for a
frozen positive definite Gram; in the exchange-symmetric opposite
mode the integrated expanding curvature is uniformly bounded along
zero-readout paths. Both the tanh affine-tail and convex comparator
have this property. It handles a prescribed moving Gram with an
explicit metric-variation cost, but additive trained lower forcing
breaks its alignment premise and introduces actual tangent forcing.
No independent audit or full-network transfer is claimed. Agent closed.

R8 scoped status supersedes pending: independent Fermat audit
CONVEX_AFFINE_TAIL_BASELINE_REVIEW.md (624 lines, all read by root)
returned PASS without required mathematical repairs on candidate hash
d527ba30de64cd6dec00a774faae1987eb14203187b81fced84941171d87f028.
Optional precision edits are recorded but not yet applied. In
particular, initial laws are LIMITING empirical laws, and the
integrated-velocity bounds concern FORWARD z/h fields, not backward
field or kernel velocities. Candidate unchanged; reviewer closed.

R9 candidate — ACTUAL_TRAINED_TOP_ALIGNMENT_TEST.md, SHA256
466f93f48fda1b5ff3d1905e7b0d45b26b171ce1494cb5e0b811c7e58326a8f1.
A root construction uses all trainable blocks, n>=4, rho=0, exact
sample/label permutation symmetry and zero readout. Lower feature
contrast rotates at second order even at a top neuron with zero
initial contrast; a small positive initial contrast then reverses
before its readout does. Its exact finite physical clock is checked.
For each fixed n, open neighborhoods have positive probability under
the prescribed Gaussian initialization, including nonzero readout;
no probability uniform in n or bad population limit is asserted.
An isolated adversarial audit is running. This tests the invariance
premise, not the full theorem.

R9 current scoped status: first review ACTUAL_TRAINED_TOP_ALIGNMENT_REVIEW.md
(606 lines, all read by root) accepted the calculation and required
explicit small-time quantifiers and normalized/operator initial norms.
These were fixed. Fresh complete second review
ACTUAL_TRAINED_TOP_ALIGNMENT_REVIEW_2.md (615 lines, all read by root)
returned PASS with no required mathematical corrections on hash
e83eaee5b01c77b1e0a4663af61714aea4d62a4095f2331898ea2d68271d13b9.
Both reviewers are closed. This is now a scoped-audited actual
finite-trajectory invariance counterexample, not an MF counterexample.

R10 candidate — UNALIGNED_CURVATURE_BUDGET.md, SHA256
a1790728bd693e28140407df96f90a82641f3b7858cf2bf2b59489cef8e19bfe.
The root removed the alignment premise from a scalar convex top
estimate by charging squared-readout backtracking and signed lower
forcing. A smoothed sign selector has a nonnegative zero-crossing
term because w'=F and both phi and phi' are increasing. This gives
an actual weighted integrated positive-curvature FIRST-MOMENT bound
on any existing uncut exchange-symmetric pre-fitting population
trajectory under its raw action identity. It does not construct that
trajectory or control the exponential propagator cost. An isolated
audit is running; no promotion yet.

R10 first audit UNALIGNED_CURVATURE_BUDGET_REVIEW.md (511 lines,
all read by root) verified the scalar estimate with arbitrary zero
sets, but required the corollary to specify its raw Hilbert spaces,
chain rule/forward-map argument, common Gram and constant uniformity.
Root imported those details, included the absolutely continuous
version, and separated objective J from Gram diagonal g. A fresh
complete audit is running on the new hash
a173459960cccbf09fd9a4a1eb9ea1aa44bb88e86427d965fe8009ec266f0e3d.
The note now also explicitly records that a COARSE first-moment
curvature bound follows already from beta<=|w|/8 and action.
The nontrivial new scalar content is the signed path/subinterval
budget, not a newly resolved population-tail obstacle.

R11 returned — GAUSSIAN_INITIAL_SIGNED_RESPONSE.md (485 lines,
all read by root), SHA256
05708450c2896f62e9ec39beeb67c9b9d1e804ba37a96fa8e342d6cd3692e1f1.
For phi=1+atan/10 and an initial centered Gaussian pair, the
label-conjugated expected diagonal curvature is strictly negative
in both modes, except the explicitly handled singular same-label
c=-q case. The FULL response matrix, however, is indefinite:
positive in the label direction and negative in its orthogonal
sample direction. Actual top initialization has 1<c<q<1+pi^2/400.
The exact first-step B3 historical/current source blocks are
computed separately; their contracted sum gives M only after
evaluation, not after identifying formal slots. An independent
audit is running. No trained-path sign or spectral invariant follows.

## Proof and audit policy

R16 scoped audit status: GAUSSIAN_GATE_ACTIVATION_DESIGN_REVIEW.md
(420 lines, all read by root) returned PASS without required repairs
on unchanged hash fe7ac18d21022823911c32d3a61447a65f376cf08160f42e76a27ee70ba7b716.
The fixed-sign changing-control polynomial bound, uniform in initial
state, and initial eligibility are now scoped-audited. Neither this
audit nor the note supplies the trained sign/moment/feedback premises.
Reviewer closed.

R17 root sign-switching discriminator, under isolated audit:
GAUSSIAN_GATE_SIGN_SWITCHING_TEST.md, SHA256
cd97bafe6125f53e67f05751efb0ffbb9b16368ab88a50fa9f419a258a91cb4d.
A four-flow commutator has bracket derivative with two opposite real
eigenvalues at zero for generic correlation. A contraction gives a
genuine nearby return point and exponential repeated tangent growth.
This would exclude universal polynomial sensitivity for arbitrary
exogenous sign-changing controls, NOT the canonical trained theorem.

Unverified auxiliary root identities:
GAUSSIAN_GATE_AUXILIARY_IDENTITIES.md, SHA256
cab0a18d37d21885a315590aca12ed7ebe2cd8767eef06d050fe2a982c11bc31.
Initial arcsine covariance and explicit B/J/T response integrals;
an arbitrary-control weighted-area identity with density exp(z^T C^-1 z).
This density is nonnormalizable, and determinant control is NOT full
tangent control. No independent audit has been commissioned for these
identities; do not promote them or use them as a full-theorem premise.

R15 scoped audit status: FIXED_SIGN_VARIABLE_CONTROL_BOUNDARY_REVIEW.md
(485 lines, all read by root) returned PASS without required repairs
on unchanged hash 28ae2496937d65ec80a8e727519f60cac146574fbcabcfec6fbde57f11364c9f.
Optional contextual precision: for a characteristic with coefficient
1/2 use prescribed u=q/2; the exogenous theorem itself has the exact
displayed normalization. The control and all its derivatives must
be held fixed when taking the stated initial-state derivative.
Reviewer closed.

R14 scoped audit status: ACTUAL_REVERSE_QUERY_EVOLUTION_REVIEW.md
(407 lines, all read by root) returned PASS without required repairs
on unchanged hash fb9b8fb1e43f31bf16c7b08f2e079e6e5ff20fb39fd7d7a142712514df34677c.
Optional presentation points concern the mixed L2/L-infinity product
rule, spelling out common finite width, and the induced first-input
metric. The exact conditional identity and finite-interval estimates
are scoped-audited; no coefficient-comparison/tail bridge is supplied.
Reviewer closed.

R16 new activation design: GAUSSIAN_GATE_ACTIVATION_DESIGN.md,
SHA256 fe7ac18d21022823911c32d3a61447a65f376cf08160f42e76a27ee70ba7b716.
The fixed activation phi(z)=1+0.1 integral_0^z exp(-v^2)dv keeps the
old bounded-positive range and first-two-derivative constants and
strict initial nonlinearity/both label modes. A bounded-potential
and tail decomposition gives a polynomial-in-control-cost tangent
bound UNIFORM IN INITIAL STATE for arbitrary changing ratios inside
a fixed sign quadrant. This removes R15's specific arctan obstruction
in that control class. An isolated audit is running. Actual backward
queries need not keep their signs; their control-cost moments and
feedback variation remain unproved. No all-time trained nonlinearity,
nonlazy learning or global MF theorem is claimed for this activation.

R13 scoped audit status: CONSTANT_CONTROL_ARCTAN_TRAVERSAL_REVIEW.md
(530 lines, all read by root) returned PASS with no required repairs
on unchanged hash 8fca2c20127608fc84f04906ecf733b9d4a6e8b65a78c8af9416d52f8b36522c.
Its constant-control theorem is now scoped-audited. Reviewer closed.

R15 root changing-control discriminator: FIXED_SIGN_VARIABLE_CONTROL_BOUNDARY.md,
SHA256 28ae2496937d65ec80a8e727519f60cac146574fbcabcfec6fbde57f11364c9f.
For arbitrary integrable controls confined to one sign quadrant, an
arctan tangent bound exp(C[R+U^(1/3)]) follows from a positive-part
cubic potential; U is the total absolute control cost. A smooth
changing-ratio control keeps one coordinate at -1 and forces tangent
growth exp(cT) while U=O(T^3), so the constant-control polynomial
estimate cannot extend to this class. This is an exogenous-control
test, NOT a trained trajectory. An isolated audit is running.

R12 final scoped status: GAUSSIAN_BACKWARD_SIGN_TRANSFER_REVIEW_2.md
(505 lines, all read by root) returned PASS with no required repairs
on unchanged hash 5ff166e2c9ab7faf504be74795d513d61fae14a1b8d789e3759606dba09670e8.
Optional presentation comments concern explicitly repeating forward
input exogeneity, distinguishing the two separate conditioning
arguments, and expanding one final moment calculation. The actual
initialization lemma is now scoped-audited, not a trained-path theorem.
Reviewer closed.

R13 returned: CONSTANT_CONTROL_ARCTAN_TRAVERSAL.md, 359 lines all
read by root, SHA256
8fca2c20127608fc84f04906ecf733b9d4a6e8b65a78c8af9416d52f8b36522c.
For constant two-vector control and |rho|<1, the tangent propagator
is bounded polynomially in 1+t||u||, with exponent linear in
1+||z0||_1 and finite Gaussian moments at every fixed t,u. The
proof uses a telescoping tail potential plus an invariant region
for strongly unequal control components. An isolated audit is running.
It does not apply to the actual changing control without new work.

R14 root candidate: ACTUAL_REVERSE_QUERY_EVOLUTION.md, SHA256
fb9b8fb1e43f31bf16c7b08f2e079e6e5ff20fb39fd7d7a142712514df34677c.
Exact q2'=b+Kq2 along existing cut/uncut two-sample feature paths;
K has finite width/cap-independent L2 operator bounds on each finite
feature interval, and q2 has an L2 time-Lipschitz bound. In uncut
equations its lower forward factor is positive semidefinite, but
the top signed curvature is indefinite. No phi''(Z2)q2 occurs in
q2's own evolution, yet different-path comparison still involves
(K-tilde K)tilde q2. Generic bounded L2 operators do not propagate
Gaussian tails. An isolated audit is running; no global inference.

R12 first review GAUSSIAN_BACKWARD_SIGN_TRANSFER_REVIEW.md (504
lines, all read by root) accepted scalar cone algebra but required
an explicit equal-width finite model and the empirical second/mixed
moment proof at the second transpose. Root imported and checked the
full conditioning/averaging proof, including both projection errors,
finite-array moments and the conditioning on the third matrix.
Current repaired hash:
5ff166e2c9ab7faf504be74795d513d61fae14a1b8d789e3759606dba09670e8.
A fresh isolated full audit is running. First reviewer closed.

R13 active bounded sidecar: constant-control raw two-input arctan
flow z'=C diag(phi'(z))u. Test polynomial, instead of exponential,
dependence of its tangent propagator on constant control amplitude.
This is not the already refuted common-Killing-metric mechanism;
it concerns traversal under one fixed control. No transfer to the
time-dependent trained control is presumed.

R10 final scoped status: UNALIGNED_CURVATURE_BUDGET_REVIEW_2.md
(895 lines, all read by root) returned no required mathematical repairs
on unchanged hash a173459960cccbf09fd9a4a1eb9ea1aa44bb88e86427d965fe8009ec266f0e3d.
The conditional scalar/Hilbert estimate is now scoped-audited. The
review also notes a coarse second moment from action alone; neither
it nor the new signed budget proves exponential response control.
Reviewer closed.

R11 final scoped status: GAUSSIAN_INITIAL_SIGNED_RESPONSE_REVIEW.md
(614 lines, all read by root) returned no required mathematical repairs
on unchanged hash 05708450c2896f62e9ec39beeb67c9b9d1e804ba37a96fa8e342d6cd3692e1f1.
Optional wording correction: the full response is LEFT MULTIPLIED
by the label matrix, not conjugated by it. The formulas are correct.
The audit treats first-step coefficients as algebra in the specified
scalar law; it is not a separate finite-program identification proof.
No trained-path sign preservation follows. Reviewer closed.

R12 candidate — GAUSSIAN_BACKWARD_SIGN_TRANSFER.md, SHA256
c37ffe3035b080bab0e0e79f94e45926e882c58239c370df25d90295a7173652.
The initial signed two-mode cone is preserved by one more centered
Gaussian hidden gate. A direct conditional-matrix calculation is
included for the actual initial backward velocity queries. This is
under isolated audit, not yet promoted; it concerns initial fields
and not the complete trained causal response kernel.

Prefer importing specialized proofs into the final document. Otherwise
read the full primary theorem statement AND proof, recursively checking
heavy dependencies. Lemma PASS never implies theorem PASS.
Final reviewers use fresh contexts and only the candidate document as
mathematical input; required procedural skill reads are disclosed.
Record every candidate hash, exact review scope, errors and repairs.
# Latest audit completion

R28 local nontriviality (004e20c23963e2b628c84ece79e97226acc91ef70e3d0f61c554859647fe4258)
has a full 434-line isolated modular PASS report, all read by root.
R29 energy-preserving initial-operator references
(464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2)
has a full 350-line candidate-only premise-conditional PASS report, all
read by root. No required corrections. Both reviewers closed. Global
reference existence/action and local consistency are now scoped-audited;
canonical global convergence is NOT established. Full goal remains OPEN.
