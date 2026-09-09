# Next proof obligation — two samples, 2026-09-06

Full two-label target OPEN; unbudgeted goal ACTIVE. Source task/agents
remain paused. No experiments or changes to architecture, initialization,
optimizer or clock. Activation redesign is authorized, fixed across all
configurations. Exact contract: CONTRACT_AND_LEDGER.md.

## Current proof boundary

LATEST USER PIVOT supersedes old running entries: pursue L=2 opposite
labels first, and allow different fixed nonlinear activations per layer.
ALL angles [-1,1) still required. New immediate contract and work:
/tmp/l2-two-sample-proof-0ywjpp/CONTRACT_AND_SEARCH.md.
R32/R33/R34 reviews all returned, root FULLY read 623/496/436 lines,
no required fixes, all three reviewers CLOSED. Only existing author
Hubble 01a0782e-5320-72e2-98af-666375d94422 remains open, finishing
SOFTPLUS_GAUSSIAN_TAIL_PRESERVING_REFERENCES.md (R35), a bounded reusable
initial approximation refinement. Do not read a running file as final.

Unwritten root refinement of R34: on active gap X>=0, monotonicity gives
f_other(1-f_active)<=f'(z_active). On X<0, the R34 occupation bound at
L=0 gives cross integral <=kmax Q/(1-kmax). Absorb kmax I to obtain
I<=A0/(1-kmax)+Q/(1-kmax)^2, eliminating the separate B polynomial
factor. This is NOT yet a written or audited lemma; exponential Q still
open. It is useful for L=2 too, not an answer to global continuation.

Running R34 candidate-only reviewer Sagan
01a07824-9299-7ca0-8456-d705aaa2d7e5; running R32 candidate-only reviewer
Lovelace 01a07824-930e-7b30-bec6-9a8948a19aa5. R33 reviewer Socrates
01a07820-f083-76f0-ae2d-604032edf892. All authors and previous reviewers
are closed. No source agent resumed. Read completed returns fully.

Root next critical estimate after R34, if it survives: its pointwise
bound depends on Q=integral(|W3 (H2_1)'|+|W3 (H2_2)'|), not merely
the readout. A direct scalar Gronwall from w'=feature contrast and
v'=kappa w P+b_v also bounds |w|+|v| by C(|v(0)|+Q), so sufficient
exponential control of Q would subsume the readout moment cost. This
observation has NOT been written/reviewed as a lemma and does not give
the missing exponential bound. Q has only an established uniform L2
bound. The actual b is correlated trained lower motion, not fresh
independent Gaussian forcing. Do not factor it or invoke arbitrary Lp
boundedness of the initial operators.

R32 author return COMPLETE, 488 lines root ALL read, author closed.
SOFTPLUS_CONSTANT_CONTROL_SENSITIVITY.md SHA
cc61329a498a65da53513a2af948febba35b07d1ee47547de863584f0541e38a,
now under fresh candidate-only audit. For q=(1,1), rho=-1/2 it constructs
a fixed initial point in [-log3,0]x{log3} with tangent >=exp(3s/160).
This is constant-control pointwise, NOT actual trained/Gaussian-averaged
failure. Mixed-sign controls instead have an explicit polynomial bound;
the root's balanced-control invariant is independently checked in its
appendix. No promotion until review read fully.

R34 NEW root SOFTPLUS_ZERO_READOUT_TOP_RESPONSE.md, SHA
b3db63b762556636bb5ec5607acbe04729f23944f055e35e4339c2370ae42566,
under fresh candidate-only audit. This uses the ACTUAL identity
w'=top feature contrast and w(0)=0 to make all active-sample switching
terms FAVORABLE, without a finite-crossing or sign-alignment assumption.
Smooth tanh(w/delta) weights prove an occupation estimate for
sign(w)(Z3_1-Z3_2), retaining full lower forcing and moving Gram.
Integrated positive top curvature <=initial negative-log gates
+ C log(1+integral lambda|w|) + C integral |lower forcing|.
Thus the FULL homogeneous 2x2 top propagator has polynomial readout
dependence and exponential lower-forcing dependence. The latter and
higher readout moments are STILL OPEN; no global theorem yet.
This is a stronger actual-history result than fixed-sign traversal or
an L2-only criterion, if verified. R33 coordinate audit remains running.

LATEST: R30 full 682-line candidate-only audit has been read in FULL.
Conditional PASS, no required fixes at e3fd00736b3094a16395b524d4e6ed7a0376b5c4e0c4d2e2b5bdccc5e8d71112.
Laplace closed. Exact both-query evolutions and L1 action estimates are
scoped-audited; noncanonical symmetric-state obstruction remains ONLY
an algebraic current-bound obstruction, not a reached-path result.

R33 root SOFTPLUS_TOP_TRANSVERSE_COORDINATE.md is now under candidate-
only conditional isolated audit by Socrates
01a07820-f083-76f0-ae2d-604032edf892. Hash
1623764a294c53a475c004c3d99e2d17b65a3cd70a5a5993bd80599908544c98.
Actual top modal equations u'=A wD+b_u, v'=kappa wP+b_v; gamma=A/kappa>1.
I_gamma=exp(-u/gamma)[cosh(v)-exp(u)/(gamma-1)] cancels direct w
EXACTLY, retaining both actual lower forcing and gamma' terms. The
inverse has bounded derivatives; forward derivatives are UNBOUNDED.
J=log|(I_gamma)_u| has bounded spatial derivatives and linear growth,
J'=chi+E with ||E||2<=C raw_speed. The homogeneous transverse multiplier
exp(-integral chi) has an actual uniform L2 LOG bound, not an ordinary
moment/tail bound. Full inhomogeneous sensitivity and canonical global
convergence remain OPEN. Read full review before any promotion.

R31 local exact-GD/observable audit COMPLETE: Confucius returned a full
357-line modular PASS report; root read ALL of it. No required fixes
or blocking dependency issues at unchanged hash
a830c8bfc6d6a398c693fef8669303341a0dc40e12cd498e75e7995f752a8071.
The report explicitly fills the intermediate fixed-R layer-two velocity
L2 time-modulus/UI argument before applying the last gate product.
Confucius closed. Softplus now has the local population plus exact raw
GD/GF/observable and separate local-nontriviality modules, all scoped-
audited. This is NOT global or final single-document certification.

R32 author is Carver 01a0781c-63c1-74c1-bde4-47baddfaafc3, still running.
Root supplied one author-side exact invariant for balanced opposite
constant controls; it is NOT audited yet. Root's new critical work is
the actual moving-top-Gram/forcing version (full lower-layer forcing
retained), not a frozen-hidden substitute. R30 audit remains running.

New bounded R32 discriminator dispatched: SOFTPLUS_CONSTANT_CONTROL_SENSITIVITY.md.
Exact two-coordinate constant-control logistic-gate flow, all control/rho
signs; seek explicit polynomial/subexponential tangent estimate or actual
constant-control obstruction. This is NEW relative to old arctan/sech
control tests: logistic gate is monotone, tends to zero only on the
negative tail, and has a nonzero positive plateau. It is not a trained-
history or moving-Gram result and cannot substitute for one. No return
yet; no claim promoted. R30 reviewer is Laplace
01a07818-0988-7330-be42-5b56e6e01b68. R31 reviewer is Confucius as below.

LATEST R30/R31: Parfit's R30 SOFTPLUS_ACTUAL_QUERY_TIME_REGULARITY.md
returned (582 lines, root ALL read), SHA
e3fd00736b3094a16395b524d4e6ed7a0376b5c4e0c4d2e2b5bdccc5e8d71112.
Parfit closed. Candidate-only isolated audit now running. It derives
both actual q evolutions and a constant-one L1 selected top-matrix
curvature-action estimate. An explicit symmetric state makes both
q derivatives diverge in L2 with bounded primal/current action data;
that state is NOT proved reachable by canonical/reference initialization.
All claims remain unpromoted pending complete audit.

R31 root SOFTPLUS_LOCAL_EXACT_GD_OBSERVABLES.md, SHA
a830c8bfc6d6a398c693fef8669303341a0dc40e12cd498e75e7995f752a8071,
under isolated modular audit by Confucius 01a07817-855e-7f23-a99c-dacff8694467
with exactly the four R28 dependencies listed in it. New LOCAL exact raw
GD/GF/observable bridge, not global continuation. Root repaired the
velocity-program argument before dispatch: an unbounded product before
the W3 query requires a separate fixed input cap and L2 tail removal,
not merely calling the product a polynomial-growth empirical test.
Read returned reports FULLY before any promotion. Full global goal OPEN.

Active bounded sidecar R30: Parfit 01a0780e-5819-7882-8702-120b05d73cdd,
SOFTPLUS_ACTUAL_QUERY_TIME_REGULARITY.md. Allowed mathematical inputs
only R29 and R27; derive both actual reverse-query evolution equations
on the globally regular reference family and test uniform time-regularity
with all product terms retained. This specifically tests the loss of the
pointwise readout bound; the older bounded-activation R14 cannot be copied.
No completed return yet. Root is pursuing global-reference compactness/
stability alternatives and screened the new cavity primary source;
the source supplies no direct theorem mapping (SOURCE_SCREENING.md).

LATEST COMPLETED AUDITS (supersedes running R28/R29 entries below):
Root read the FULL R29 350-line report and R28 nontriviality 434-line
report. Both report no required corrections at unchanged candidate hashes:
R29 464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2;
R28 nontriviality 004e20c23963e2b628c84ece79e97226acc91ef70e3d0f61c554859647fe4258.
Their respective premise-conditional/modular scopes are retained. The
R28 assembly dependencies themselves already have scoped audits; this
does not substitute for final single-document complete-proof reviews.
Nash and Halley are closed. No destination agents currently running.
Canonical global opposite-label construction and the full user goal
remain OPEN. R29 gives actual globally energy-preserving reference
paths plus LOCAL consistency, not their global convergence.

LATEST R28/R29 (supersedes author/reviewer entries below):
All first R28 dependency reviews are complete and fully read: response
409 lines, identification 237, primal/comparison 748. No required fixes
on the recorded hashes. Local assembly's full four-input 338-line report
is also fully read and gives local modular PASS with no required fixes,
hash 398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d.
Thus softplus local population construction/energy/symmetry is scoped-
audited, NOT the full local GD/observable theorem or global target.
All those authors/reviewers are closed.

Pauli's SOFTPLUS_LOCAL_NONTRIVIALITY.md (766 lines, fully read), hash
004e20c23963e2b628c84ece79e97226acc91ef70e3d0f61c554859647fe4258,
is now under isolated modular audit (candidate + assembly + fixed-program
identification). It supplies both unbounded static-transpose bridges and
positive s² motion/all-layer local nonaffinity, not global claims.
Pauli is closed.

R29 root new candidate SOFTPLUS_ENERGY_PRESERVING_OPERATOR_REFERENCES.md,
hash 464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2,
under candidate-only audit by Nash 01a07802-3b06-7820-a32a-9b126d34c4d4.
It constructs globally regular GENUINE UNCUT gradient references from
bounded-kernel initial operators, approximating the canonical initial
operators strongly in BOTH orientations with bounded-basis projections.
Raw energy gives uniform L2/operator bounds; exact rank-memory formulas
then give finite (N-dependent) L∞ bounds and actual global reference
existence. Symmetric projections preserve sample symmetry; readout
convexity gives uniform before-fit Smax=2/k0 for large N and uniform
global-reference R26/R27 action bounds. A different-initial-operator
asymmetric comparison uses strong convergence on OLD fixed-cap compact
input paths to prove LOCAL consistency with the canonical path.
The initial operator convergence is NOT in operator norm/HS; constants
L2->L∞ may diverge with N. Global N-limit/tails remain OPEN. This is
an approximation proof device, not a proposed change to target init.
Read returned review fully before promotion.

R28 latest (supersedes running author entries): root's response candidate
0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b
has a full 409-line candidate-only conditional PASS review, all read;
Tesla closed. Lagrange's 1042-line primal/comparison return was fully
read; root added the exact canonical input-span map and removed an
irrelevant alternative hidden-matrix rescaling. Current hash
51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f
is under candidate-only audit by Euclid 01a077f1-4dfd-7aa3-88e8-ccb7559c2435.
Avicenna's 862-line fixed-program identification return was fully read;
its new isolated candidate-only audit is running. Both authors closed.
The key fixed-cap observation is genuine bounded-first-derivative
coordinate maps despite unbounded linear-growth features. No local
population theorem or global opposite-label theorem has yet been promoted.

Latest running work: root SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md (new draft);
Avicenna 01a077e8-2d13-7f91-9a5e-fab2c938ad49 writes
SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md; Lagrange
01a077e8-2d70-7e00-85fe-4b5bb8ef0208 writes
SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md. Read completed returns in full.
Do not read running files as final or assume these bridges already hold.
The prior three reviewers R25/R26/R27 returned scoped PASS; their full
550/517/325-line reports were read and all agents closed. Supersedes
all older running-agent entries below. Opposite-label global goal open.

Both shifted arctan and phi(z)=1+0.1 atan(sinh z) have complete scoped-
audited modular SAME-LABEL global theorems, including all observables,
restartability, raw GD and nontriviality. Neither is the full two-label
goal or its final single-document/several-isolated-reviews deliverable.

BOTH label modes have actual short response control and uncut local
population flow on feature time [0,3/2], now also for sech. Same labels
fit before 36/25, covering every physical horizon. Opposite labels have
positive initial contrast and a preserved readout-convexity floor on
EXISTING uncut feature paths, not the required longer path construction.

The unresolved comparison is the changed middle gate times the other
state's full reverse query. L2/action/current-Gram and first-chaos bounds
do not give tails. R14 actual q2'=b+Kq2 has bounded L2 coefficients on
existing intervals; comparison still retains (K-K_tilde)q_tilde. Strong
endpoints are not restart existence; fixed-mesh Gaussian identification
is not mesh-uniform continuation.

## Latest certified results

R18 sech fixed-sign changing-ratio prescribed-control sensitivity is
polynomial, uniform in initial state, and retains the old relative-gate
inequality. Actual controls cannot be assumed fixed-sign: R19+R20 now
give actual positive-measure local sign reversals.

R19 SECH_ACTUAL_CONTROL_SIGN_TEST.md:
43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51.
Static initial Gaussian linear/cubic query laws, all finite mixed
moments and compact-box density bounds. Fresh review 2 clean within
static/conditional scope, all 820 lines read by root.

R20 SECH_LOCAL_JET_AND_SIGN_BRIDGE.md:
65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8.
Raw polynomial comparison, auxiliary approximate-readout cut, initial-
moment product split, cap=t^(-1/4): actual feature-query remainder
O_L2(t^(9/2)) and endpoint sign reversals with probability >=c t^2.
Fresh review 2 clean conditional on R19's separately audited static
theorem; all 362 lines read. No population C4 premise, Lp operator bound,
scalar q1 continuity, or fixed physical endpoint ratio. No infinite
crossing or full trained hyperbolic-loop claim, nor global counterexample.

R21 SECH_SAME_LABEL_GLOBAL_TRANSFER.md:
f7cfaf82de5ba25a7b8429435366a2919c2c82e15cf132d2525e4b260c602302.
Complete modular same-label PASS, all 613 review lines read; includes
rho=-1 and both equal-label choices, no dependence on R19/R20.
Newton, Hypatia and Sartre closed. Earlier scoped route dispositions
and hashes: ROUTE_REGISTRY.md and CONTRACT_AND_LEDGER.md.

## Current sidecars and immediate work

LATEST operational snapshot, superseding agent/hash entries below:
- R25 author return ALL read; current 965-line hash
  1318581760487566cc467b2952016ce502a4d2da4a2cbf841e15c19e88a9776b;
  reviewer Maxwell 01a077e0-4821-7670-be10-babf6e77ae6f, candidate+P3,
  output OPPOSITE_LABEL_MODE_RESPONSE_REVIEW.md.
- R26 first review 372 lines ALL read, no required repairs; precision
  improvements made. Hash e222051b6b85c07a23243b4c502ae6db4bbf7a2e7c659d0a4393e18f03522b2c;
  fresh candidate-only reviewer Aquinas 01a077e0-487e-7111-a0f2-a627a5d041ae,
  output CONVEX_GATE_CURVATURE_ACTION_REVIEW_2.md.
- R27 first review 369 lines ALL read, no required repairs; precision
  improvements made. Hash 9f812d0d7ecc5196f699a338fc4f8d4b0b5db6a703e817bdf6ebfc2dae60634b;
  fresh candidate-only reviewer Peirce 01a077e3-3d4b-7863-a888-9318a2b159dc,
  output MIDDLE_CURVATURE_MODE_ACTION_REVIEW_2.md.
All authors/earlier reviewers closed. Read FULL returned reports before
promotion. Root next proof work is the UNVERIFIED detailed local construction
in SOFTPLUS_LOCAL_BOOTSTRAP_PLAN.md, including its concrete box/constants.
Do not claim an existing local or global theorem for shifted softplus yet.

R27 root candidate MIDDLE_CURVATURE_MODE_ACTION.md, hash
13eb30bc81437f27d1c341243f69266ccfd95ff35b887789d9f986663625e473,
is under candidate-only review by Cicero 01a077dd-7280-7cd3-af11-2ca0af1c86f2.
The exact same-coefficient identity phi'' q=A delta+B q preserves both
sample modes. Actual trained adjunction and action bound integrated
middle curvature-minus and kappa2-weighted curvature-plus without inverse
contrast. This may remove R26's mixed-product obstacle AT SECOND-MOMENT
LEVEL ONLY. Curvature times historical source sensitivity remains open.
Read the full returned report before promotion; no existence claimed.

R26 root wrote CONVEX_GATE_CURVATURE_ACTION.md, hash
f83192ffc92fa36aeabe4cd6042b3c5291cd7180a78064dbc8d35bf1682b0ce0.
Candidate-only isolated reviewer Popper 01a077d9-965a-7890-abb6-733a7863950a
is running. Read the FULL returned review before promotion/repairs.
The fixed activation 1+0.1 softplus retains the positive floor but loses
the bounded ceiling. It gains curvature-difference domination, impossible
in the specified bounded monotone class. Actual weighted top-curvature
action is bounded by g<=1 on existing energy/symmetry paths; middle
products and historical sensitivities are not controlled by that estimate.

R25 author Kierkegaard 01a077d6-74b0-7682-8c81-e8eb9d76e9ea is deriving
OPPOSITE_LABEL_MODE_RESPONSE.md, exact full sample-mode Gaussian law for
shifted arctan, both learned matrices and coupled modal cuts included.
Wait for a completed return before reading/promoting. This is intended
to identify an actual cancellation, not repeat generic L2/Gram criteria.

R24 completed: candidate now 878 lines, hash
fbb08acfe9decd7e4797266be32a68b6a5a84e892e50ae1acb958b10353770ae.
First report 569 lines and fresh second report 363 lines ALL read;
fresh scoped PASS after one wording repair. Current -f response and its
signed sum are valid, but the full retarded covariance has an explicit
positive finite-law contribution. No global bound. All R24 agents closed.
The R24 active entry below is superseded by this paragraph.

R24 active bounded proof-search sidecar: Archimedes
01a077c0-309a-7361-9f32-b373e3a740ce, expected output
SHIFTED_HARMONIC_CAUSAL_RESPONSE.md. Fixed phi=1+(sin+cos)/20.
Opposite-label symmetry E W4=0 and phi''=-(phi-1) make the CURRENT
expected top curvature -f_a. Test the complete retarded response with
correlations retained, not a diagonal/trace-to-norm shortcut. The old
R3 harmonic trace route is exhausted. This new sidecar is not returned
or verified; positive-gate nontriviality cannot be transferred blindly.

R23 POSITIVE_TIME_MIDDLE_CURVATURE.md, revised 478 lines, SHA256
9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a,
has completed its fresh second two-review round:
- Mencius 01a077bd-506c-7d41-a025-715585392a69: candidate+explicit listed
  mathematical dependencies, POSITIVE_TIME_MIDDLE_CURVATURE_REVIEW_2.md.
- Bacon 01a077bd-50ca-7530-b2ae-33573a9d29b0: ONLY the candidate,
  accepting its precise local premises conditionally and checking the new
  implication, POSITIVE_TIME_MIDDLE_CURVATURE_PROBABILITY_REVIEW_2.md.
First reports (953/660 lines) all read. Root repaired centering, Taylor
cross-error time factor, odd-cut sample symmetry, and restart-claim scope.
Godel and Arendt closed. The core probability argument was not rejected.
Both fresh reports are fully read (878/657 lines), with no required
corrections and unchanged candidate hash. Their distinct scopes above
are retained; this is a scoped-audited local lemma, not the global goal.
Mencius and Bacon closed. Do not read a running agent's file as a final return.
Claim: Gaussian LOWER tails of q2 at compact Z2 at every sufficiently
small fixed positive time, then unbounded full population loss directional
Hessian. Not a global tail bound or a global counterexample. Exact finite
Euler source regressions avoid assuming a continuous kernel representation.

R22 ACTUAL_GAUSSIAN_INITIAL_HESSIAN_TEST.md:
8068a63d710643d06020701a19d5d90260bf02ce5300d158fe52bd4b10546407.
Its full isolated scoped review PASS (all 609 lines read) certifies the
time-zero full physical material-Jacobian obstruction at canonical
Gaussian initialization. It does not prove positive-time or integrated
failure. Herschel closed; only R25 author and R26/R27 reviewers are open.

Root critical path: genuinely new actual sign-changing causal middle-
response estimate or different global construction. Do not repeat
arbitrary-control Killing cancellation, determinant-to-norm shortcuts,
generic L2-to-tail implications, or top-only identities as solutions.
Bounded activations already control the top multiplier.

No specialized external theorem invoked. SOURCE_SCREENING.md records
screened sources, not certified dependencies. Before heavy invocation
read the full primary statement AND proof, recursively checking heavy
dependencies, or import a full adapted proof. Final complete document
requires several fresh isolated agents with ONLY that document as
mathematical input, repair/repeat until clean. Lemma PASS is not theorem
PASS. No full-target completion or blocked status is authorized.
