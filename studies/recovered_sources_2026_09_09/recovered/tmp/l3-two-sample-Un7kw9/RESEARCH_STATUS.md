# Two-sample research state — 2026-09-05

## Authority and target

CONTRACT.md is authoritative for the raw two-sample normalization and
observables. Latest user clarification: a single identical nonlinear
activation for every nonzero angle is the ultimate target. An
angle-dependent fixed nonlinear coefficient is permitted only as an
intermediate check. No experiments; no old-source resumption; no Git
changes. All new work is in this private destination directory.

LATEST USER CLARIFICATION: only the activation must be data independent;
proof constants may depend on the fixed inputs, labels, and physical T.
Read DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md. No data-uniform learning
speed, feature duration, or stability constant is required. Divergence
as rho -> 1 is NOT a goal obstruction. The actual remaining quantifier
gap is the data-dependent epsilon threshold, not growing proof constants.

The universal two-sample theorem is OPEN. The angle-specific near-affine
theorem is now COMPLETE and has TWO independent complete-proof-only
adversarial PASS reviews. See READ_ME_FIRST.md for exact scope. No
conditional lemma was used as a substitute for those full audits.
The audited bounded-offset one-sample theorem is
unchanged; its immutable sources and hashes are in CONTRACT.md.

## Evidence and exact scope

1. TWO_SAMPLE_SOURCE_BASELINE.md, SHA256
   a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f.
   Worker-completed, main read in full. Isolated adversarial PASS.
   Gives the exact two-sample fixed-mesh source equations, including
   both transpose returns, and mesh-uniform affine response rows under
   a uniform affine primal bound. A Gaussian probe inserted at named
   query answers proves the formal-response bound without an unproved
   finite-network trace interchange. Current same-time entries and
   antipodal singularity are handled explicitly.

2. SYMMETRY_RADIAL_CLOCK.md, SHA256
   40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4.
   Worker-completed, main read in full. Isolated adversarial PASS.
   Establishes population symmetry from symmetric finite approximations,
   not finite-realization equality or uncut uniqueness. For any existing
   strong gradient path starting from zero readout, ||C'||>=||C'(0)||.
   Initial projected kernels are positive for both label sectors and
   rho=-1. Affine local Lipschitzness plus energy gives a finite bounded
   baseline interval through projected output 3/2, discharging the primal
   premise in item 1. Affine hidden variances and arctangent's best-affine
   approximation error stay strictly positive on that interval.

3. NEAR_AFFINE_RESPONSE_ROUTE.md is a proposal, not a completed proof.
   phi_e(z)=1+z+e arctan z; auxiliary backward gate clips only the e-part.
   Uniform-in-clip O(e) primal comparison to the affine flow is useful
   but insufficient. The key remaining lemma is uniform-in-mesh/clip
   response control for actual nonlinear programs. A proof worker is
   completing or testing all five exposed bootstrap steps.

   UPDATE: NONLINEAR_RESPONSE_PERTURBATION.md is now a completed
   worker candidate, main read all substantive text. Final 930-line
   hash ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568.
   It repairs the missing current-coordinate multiplier in backward
   response envelopes and gives literal four-stage causal induction.
   Mesh/cap-uniform subGaussian actual backward inputs are PROVED for
   fixed sufficiently small epsilon depending on B,S. Isolated PASS in
   NONLINEAR_RESPONSE_ISOLATED_REVIEW.md (361 lines), main read in full;
   review hash 3a60cacf49c6141288e5dceb843e0f549904bcec02de6ec606bedf993e412b8d.
   Affine premise is discharged by items 1--2. This is still a lemma,
   not a complete theorem PASS. Earlier 927-line hash 6168db... is stale;
   final differences are formatting and zero-extension conventions.

4. INITIAL_FEATURE_LEARNING.md, SHA256
   bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351,
   has isolated adversarial PASS at unchanged hash. Review is
   INITIAL_FEATURE_LEARNING_REVIEW.md (298 lines), main read in full.
   For every fixed e>0 and every allowed angle, two exact initial
   transpose uses retain positive-definite Gaussian innovation pairs.
   This gives nonzero initial acceleration in each hidden parameter
   block and each sample's hidden features, and a strictly changing
   projected limiting kernel along a constructed strong path. It does
   not construct that path or prove all-time nonaffinity.

5. PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md is an unaudited main
   derivation. Gives explicit uniform-cap strong primal comparison and
   downstream cutoff/uniqueness/physical-clock/full-two-residual GF/GD
   arguments under an explicitly stated actual response-tail premise.
   The final empirical hidden-velocity bridge has now been supplied by
   FIXED_CAP_VELOCITY_BRIDGE.md (690 lines), main read in full, hash
   a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0.
   Main added the ordered width/R/M limit for uncut velocities so no
   exploding fixed-cap moment constant is multiplied by a cutoff error,
   and a direct W2(C([0,T])) path interpolation argument. The frozen
   continuation bridge hash is now
   99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066.
   These new bridge proofs are under complete-assembly review.

6. UNIVERSAL_ANGLE_ROUTE.md at hash
   20dbd9164881bf475ec5d684c43b4d122708338a145ae2934b70b3629ca46cdf
   has isolated partial-scope PASS. Main read the entire 347-line
   candidate and 270-line UNIVERSAL_ANGLE_ISOLATED_REVIEW.md; review
   hash 48d38c6009947588d881b1cd7cff68c82948017e523d4b8013412c8ade2c1d9b.
   Necessary interpolation scales for fixed Lipschitz activation:
   raw displacement Omega((1-rho)^(-1/8)), feature duration
   Omega((1-rho)^(-1/4)). Exact normalized contrast equations and
   signed instantaneous curvature cancellation are proved. General L2
   small-contrast product control fails on symmetric test fields;
   pointwise restoring sign fails on a positive Gaussian affine bulk.
   Neither is a trained nonlinear counterexample. Reviewer clarification:
   the common map ALONE does converge uniformly on L2 balls at O(delta);
   it is the normalized contrast map which lacks that uniformity. Keep
   the frozen candidate hash and read this clarification with it.

7. ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md is a COMPLETE CANDIDATE assembly
   at hash 27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75.
   All intended premises are supplied by explicit proof dependencies.
   It is now PROMOTED at that unchanged hash after two independent
   complete-proof-only PASS reviews, both fully read by main:
   ANGLE_SPECIFIC_FULL_REVIEW_A.md (408 lines), hash
   33c3e0c30a13163940215144637c9c8d40d776d643b07fa543e52d5b1d1c4a0a;
   ANGLE_SPECIFIC_FULL_REVIEW_B.md (261 lines), hash
   973c2feb736704fe4e0aba52340d04d4bd2c1a97a3f8ef6b44ea5f83111d6fb9.
   No substantive corrections were required. Candidate headers remain
   frozen to preserve hashes; READ_ME_FIRST.md gives final status.
   Its quantifier is fixed epsilon(rho), never width/time dependent;
   even a full PASS would NOT resolve the universal-activation goal.

## Active bounded tasks

- Arendt 01a072eb-9d10-7251-818e-aae75dbd9410: COMPLETED isolated
  adversarial PASS for items 1 and 2 at exactly the hashes above; closed.
  Output BASELINE_ISOLATED_REVIEW.md (182 lines), main read in full.
  The reviewer also verified that item 2 discharges item 1's affine
  primal premise without circularity. No candidate corrections needed.
- Socrates 01a072eb-9d7d-7933-bb81-9efae7df8ec4: COMPLETED nonlinear
  response perturbation candidate; closed. Hash recorded above.
- Helmholtz 01a072f7-9a82-7ec2-8fe0-13bedd862fe2: COMPLETED isolated
  nonlinear response PASS at final hash; closed.
- Mill 01a072f7-9b45-7c93-a72c-159a43bec025: COMPLETED isolated
  universal-route partial-scope PASS at unchanged hash; closed.
- Dirac 01a072eb-9e0c-7853-bbcc-e483fb58b5c6: a genuinely new
  universal-angle estimate or precise route obstruction. Output
  UNIVERSAL_ANGLE_ROUTE.md.
  First task COMPLETED. Now ACTIVE on a new standalone signed-driver
  tangent response invariant, output TANGENT_SIGNED_DRIVER_RESPONSE.md.
  Its chat-only reported bound is UNVERIFIED until the full candidate
  is read and independently audited. Main also sent an exact finite-
  angle pure-q-channel extension calculation, likewise not yet certified.
  UPDATE: the signed-driver task is now COMPLETED, worker closed.
  TANGENT_SIGNED_DRIVER_RESPONSE.md has 758 lines, main read fully,
  hash 36fa3bbad7df00a6916712e23fb132489c498abd73b2e8cb382ad1780c5e701b.
  FINITE_ANGLE_Q_CHANNEL_ROUTE.md is a main partial candidate at hash
  6480eec6072f6b043e90e65d7224967cccc4936e37cd34370abfab9b0dcd0ddd.
  Both now have a fresh isolated review commissioned, output
  SIGNED_DRIVER_ISOLATED_REVIEW.md. The finite-angle fixed-driver
  clock bound is expressly still incomplete. Neither controls the full
  network common-channel forcing. TANGENT_EVEN_CHANNEL_FOLLOWUP.md
  (125 lines, main read fully) records the frozen-even affine block
  observation and precise next obligation; it is not a theorem upgrade.
- Huygens 01a072f8-668c-77c3-94c2-bffffb971577: COMPLETED fixed-cap
  empirical hidden-velocity/moment bridge; main read all 690 lines;
  final hash recorded above, worker closed.
- Plato 01a07304-0278-7d81-8cd1-19d47e01a399: ACTIVE fresh-context
  complete-proof-only audit A of the entire angle-specific assembly and
  all seven explicit proof/contract dependencies, no prior reviews.
  Output ANGLE_SPECIFIC_FULL_REVIEW_A.md.
  UPDATE: COMPLETED full intermediate theorem PASS; closed.
- Dalton 01a07304-02eb-74a1-b5b2-4e562e6fd708: ACTIVE independent
  complete-proof-only audit B, same frozen candidates, no prior reviews.
  Output ANGLE_SPECIFIC_FULL_REVIEW_B.md.
  UPDATE: COMPLETED independent full intermediate theorem PASS; closed.
- Sartre 01a07304-fa01-7193-86a1-32dfe8e2c142: ACTIVE isolated audit
  of the full local tangent signed-driver theorem and the actual proved
  portions of the finite-angle q-channel note. No universal-network
  claim or completion of the pending finite-angle clock step requested.
  UPDATE: COMPLETED and closed. SIGNED_DRIVER_ISOLATED_REVIEW.md has
  552 lines, main read fully, hash
  e98e467020e9d1f07c8eb2da8ba9c4047921244714452510c75672595585ba66.
  Full local tangent signed-driver theorem PASS; completed finite-angle
  fixed-terminal-contrast claims PASS. The finite-angle fixed-driver
  clock estimate is still incomplete and excluded from certification.
- Pasteur 01a07306-5a25-73c0-bcfa-8a67d2236b37: ACTIVE new bounded
  proof task for the quartically flat gate phi'=1+e/(1+z^4), primitive
  phi=1+z+e integral_0^z du/(1+u^4). Main route rationale and unverified
  calculation are in QUARTIC_ACTIVATION_ROUTE.md. Expected proof output
  QUARTIC_FLAT_GATE_RESPONSE.md. The proposed local advantage is a
  polynomial initial-state/signed-driver response bound, replacing the
  arctangent local exponential-in-Gaussian-contrast factor. It would not
  by itself control the full p channel or prove the universal theorem.
  Main also wrote QUARTIC_FINITE_ANGLE_BOUNDARY_LAYER.md (unaudited):
  even if the tangent quartic response is polynomial, a deterministic
  polynomial bound uniformly over all finite angles fails in the
  zero-common-coordinate linearization. A uniform Gaussian exponential
  envelope remains possible. This is a local-coordinate test, not a
  canonical trained-trajectory counterexample or a goal obstruction.
- Jason 01a072f0-fc06-7952-9297-6f0de86afbd3: COMPLETED isolated
  adversarial PASS on INITIAL_FEATURE_LEARNING.md, then closed. No
  candidate corrections; verdict assumes a constructed strong C1 path.

Latest bounded-task updates:
- Kierkegaard 01a0730e-3429-7b10-9528-6df05c39f2c6: ACTIVE fresh-context
  audit of FINITE_ANGLE_FIXED_DRIVER_PROOF.md and its sole explicit
  finite-angle orbit dependency. Output FINITE_ANGLE_FIXED_DRIVER_REVIEW.md.
  UPDATE: COMPLETED local full fixed-driver theorem PASS and closed.
  Main read all 283 review lines. Review hash
  28c76f3ec859b58cf5519a0d43a8d6c799ffecbefc4ec26f067d35019a7ad11f;
  unchanged candidate hash
  eae75509d43eb50ca10a8a5401d3100f38dd8f67985eb54e2d6b5d575d0e5bc1.
  This supersedes only the earlier pending finite-angle pure-q clock
  status, NOT the remaining coupled-network response obligation.
- Pasteur quartic task: COMPLETED and closed. Main read the full 846-line
  QUARTIC_FLAT_GATE_RESPONSE.md, hash
  7c88a195b9ad250bed56d1dde43de3cd5f04558911b710e413ec253b2c346777.
  Candidate proves local pure tangent fixed-driver Jacobian bounded by
  C_e B^20, all finite Gaussian moments, exact common-forcing defect,
  cubic late-injection amplification, and finite-angle zero-orbit bounds.
  No coupled-network closure is claimed.
- Beauvoir 01a07311-7d1e-7a01-b61d-2601f2f3a0e5: ACTIVE fresh-context
  adversarial audit of that self-contained quartic candidate ONLY;
  output QUARTIC_FLAT_GATE_REVIEW.md. No prior reviews or research history
  supplied. User quantifier clarification supplied as scope guidance.

Original workers Archimedes and Singer completed their notes and were
closed. These are destination workers; no paused source worker was used.

## Route registry and next obligations

- Do not use the one-sample positive activation floor as an opposite-label
  contrast lower bound: the constant cancels.
- Do not flatten the raw two-sample bottom equations with independent
  copies of the one-sample F coordinate. The input Gram coupling remains.
- Do not scalar-reparametrize finite-width two-residual training using
  population symmetry. Finite predictions are not exactly symmetric.
- Do not infer nonlinear continuation from energy/strong endpoints.
- Do not infer formal Gaussian response bounds directly from primal
  operator bounds; the proved affine probe bridge uses affinity.
- Generic affine comparison constants grow with S and B. For opposite
  labels the crude initial kernel is (1-rho)/2, so present estimates do
  not choose one e for all rho<1. Failure of this uniformity is not a
  counterexample to the theorem or to the candidate activation.
- Rescaling affine contrast feature time by sqrt((1-rho)/2) alone does
  not fix this: the rescaled objective must reach 1/sqrt((1-rho)/2),
  an unbounded target as rho approaches one.

The complete-assembly audits are read and the intermediate theorem is
promoted. The finite-angle pure-q clock theorem also passed its isolated
audit. Next: finish the quartic tangent candidate's isolated audit;
then return to the actual coupled
common-backward/even-operator response. Separately assess
fixed-data response and continuation estimates without requiring any
data-uniform speed, feature duration, or bound. The older finite-angle
route note's incomplete clock section is superseded by the newly audited
fixed-driver proof. No full-network p-channel response is controlled.
The universal target remains OPEN.

## Persistent goal round begun after latest user resume

User explicitly requested a goal and no stopping before complete resolution.
A NEW destination goal is active with no imposed budget. It does not transfer
the old source goal. Skills and all four required research references were
read again by main. No source agent, experiment, Git change, or optimizer
change was authorized or performed.

Quartic local candidate promotion: main read its entire 791-line isolated
review, hash 32f4c79c603a48bbd4a48e0255af7fd84733caf92d9d02f3fb087591f1fd18b6.
Local theorem PASS, candidate unchanged, reviewer closed. This does not
promote a coupled-network theorem.

New bounded outputs, all main-read in full and initially UNVERIFIED:

- RESTART_RESPONSE_WINDOW.md (753 lines),
  ee160401e65aab1b8e11848f1c25fd9fbefd15830380369eaba251d7a649e1a3.
  Full Gaussian history retained. A fixed-e local source restart follows
  from bounded primal sizes and the stated old random derivative-history
  norm. Preventing accumulation still requires a GLOBAL bound on that norm;
  the actual signed weighted term E[q phi''(Z)|J|^2] remains unclosed.
  Worker Gibbs completed and closed; isolated review now in progress.

- COUPLED_EVEN_CHANNEL_ESTIMATE.md (776 lines),
  9fd58fa3256394644f23c6e7d0e66c253beac76f2f43f13ec49477137d413e20.
  On constructed symmetric physical branches: integrated even energy and
  explicit trained-even p-return O(e^2) estimates; a quartic weighted energy
  cancels one signed term but retains transport (L4 readout sufficient).
  Full nonsymmetric response retains all operator/clock terms and three
  unclosed gate-weighted response residuals. Worker Halley closed.
  Poincare 01a0732d-9845-74d1-b546-441c81a37b6a is auditing the frozen note.

- CONVEX_SLOPE_ROUTE.md is a new main activation proposal, not a theorem.
  phi=1+z+e[z atan(z)-log(1+z^2)/2], e=.1; positive bounded slope and
  strictly positive curvature e/(1+z^2). It has a linearly growing nonlinear
  part, so cannot be substituted into the bounded-perturbation proof.
- CONVEX_SLOPE_TWO_DRIVER_RESPONSE.md (378 lines), final candidate hash
  52fa972f19cd4f4aa28dc5fdc43611e441f0bb00a8822c6377defb5a44aa4305.
  Main corrected one malformed varepsilon control character before freezing;
  old hash ba0dc72c... is superseded for that formatting correction only.
  H=M+M^3/3 makes BOTH prescribed tangent driver fields globally Lipschitz.
  Full initial and forcing response <=C_e R^2 exp((e+L)P+eQ); input-tail
  premise explicit. This is not a finite-angle coupled-network closure.
  Worker Zeno closed; Meitner 01a0732d-97e1-7e40-8b49-a010c1b0d72f auditing.

An independent fresh-context global activation route search is also active,
output INDEPENDENT_GLOBAL_ACTIVATION_ROUTE.md. It may not alter the contract
or import unverified external statements. Main's targeted literature search
has not supplied an applicable new theorem; no web-source theorem was used
in any new proof. Previously documented source mismatches remain in force.

### Subsequent main-read audit reconciliation

Main read all lines of both new local/conditional reviews:

- CONVEX_SLOPE_TWO_DRIVER_REVIEW.md, 258 lines,
  caaa162bf1872ac804abd558f4ddef8762a9df7f48fe698316c0478391f1a9c0:
  PASS without corrections for the prescribed two-driver local ODE only.
  The frozen candidate hash remains 52fa972f19cd4f4aa28dc5fdc43611e441f0bb00a8822c6377defb5a44aa4305.
  Meitner closed. No actual-network tail/transport inference is promoted.
- COUPLED_EVEN_CHANNEL_REVIEW.md, 312 lines,
  adb77dd9f678513cf2b2642c09a846aa3667695857e91fcebdf94295e339f4e6:
  PASS at the declared conditional constructed-branch level; no candidate
  changes. Future proposed response closure must explicitly require its
  source b to be in L1 time. Neither L4 readout nor response residual
  propagation was proved. Poincare closed.
- RESTART_RESPONSE_WINDOW_REVIEW.md, 293 lines,
  d7be3a575d8fbb3676ffd0d21522f927f55e244525397be2fe43720be182eeb5:
  main read in full. Scoped local PASS with two auxiliary primal-window
  qualifications and four wording/rendering corrections. Main applied all
  six, changing candidate hash from ee160401... to
  cf80b9703dbff418eb9f00bc794309e81a2f9443298acdafe797a0a50975be67.
  Original review preserved; Pascal checks revised candidate in
  RESTART_RESPONSE_WINDOW_REVIEW_V2.md. Revised clean audit still pending.

New main candidate QUARTIC_TWO_DRIVER_REGULARIZED_FRAME.md, 223 lines,
db2eae51d2b8c7b0ed14d911416117b1de3b2bca75cf4bbcf1eeb7e57eaaa3c0:
for the prescribed tangent system with arbitrary signed p,q, a positive
regularized proof weight gives full initial/L1-forcing response at most
C_e R^12 exp(C_e R^(4/3)), hence every finite moment under a square-
exponential input assumption. This does not assume p=0, alter activation,
or assert actual network driver tails or operator transport. UNVERIFIED;
fresh-context Boole 01a07344-9d19-7ca2-8efa-6a8969045996 is auditing only
the self-contained candidate.

Galileo completed and closed. Main read all 560 lines of
INDEPENDENT_GLOBAL_ACTIVATION_ROUTE.md,
f348cbf0daf4d06c71c81ab7ee5403c1fda781c03fb33b454ebf2df89b273d74.
New VLS route: full raw GF/GD logarithmic-singular-value trace bound on
the n-neuron scale, and exact full-gradient alignment. Canonical Euler
error size O(n^-3/2) before propagation is controlled; its exceptional
expanding-direction component is not. Gaussian-program approximation
requires a separate bridge. UNVERIFIED pending isolated review in
INDEPENDENT_GLOBAL_ACTIVATION_ROUTE_REVIEW.md. Not a population theorem.

The active universal-activation goal remains OPEN; no partial result or
conditional criterion above changes that status. No numerical experiment
or paused source-agent action occurred.

Further audit reconciliation (main read complete reports):

- QUARTIC_TWO_DRIVER_REGULARIZED_FRAME_REVIEW.md, 445 lines,
  1a4ed7406ba7259b6daaaed1e31c62faa20db67835dd1d4fdbad6a3b41d950a1:
  scoped local PASS, unchanged candidate. Interpret the separate-tail
  argument as R^2 <= 5(1+sum X_i^2); exponent 4/3 is the growth obtained
  by balancing this proof bound, not a sharpness claim. Boole closed.
- RESTART_RESPONSE_WINDOW_REVIEW_V2.md, 161 lines,
  1176227fd9ecf9ca2598b232e23b426a210e23f98bbc8aa456e95a3c9e9106b5:
  clean scoped PASS for candidate cf80b970... after all corrections.
  Original review preserved. Pascal closed. Full history propagation
  remains open, rather than being assumed by the global target.
- INDEPENDENT_GLOBAL_ACTIVATION_ROUTE_REVIEW.md, 506 lines,
  fe8da554c4846c3fd4d11f96055b4c75ce74d890f31fad5c651ecf9585a847c0:
  finite-network PASS, candidate unchanged. The log quantity is Schatten-2,
  not nuclear norm; the actual exceptional-source criterion is sufficient,
  not an equivalence. Schrodinger closed.

IMPORTANT historical reconciliation: the original arctan route registry
already contains audited actual squared-log response, clock/metric, and
positive-log results. VLS above extends the finite-network calculation to
the two-sample near-linear activation and records the actual GD defect;
it is NOT a new resolution mechanism for the old amplitude/alignment gap.
Do not keep polishing log-moment estimates without new actual source-
amplification information. The current source-alignment gap is unchanged.

New active bounded actual-feedback test: Hypatia
01a0734a-9974-7833-947e-ed71737f0257 tests
phi(z)=1+(1/10) integral_0^z (1+u^4)^(-1) du,
with NO affine term. Its bounded output implies a finite-time readout
supremum bound, unlike the near-linear quartic candidate. Task is to
retain all actual trained transport and decide whether the weighted top
energy or middle response genuinely closes. Output
BOUNDED_QUARTIC_ACTUAL_FEEDBACK_TEST.md; not yet read or verified.

UPDATE: Hypatia completed and closed. Main read all 450 lines; candidate
hash 3d4a765e7e18b51ef4841256536f5ea2d5a46c5e78f54d1634fa0af00629bf94.
The full top weighted energy is now integrable with an explicit finite-T
bound on a constructed branch: omega is NOT bounded but satisfies
0<=omega<=4|M|, |omega_M|<=4+22|M|, |omega_D|<=22|M|.
Bounded physical readout closes its entire transport work using primal
energy, without an additional L4 readout premise. All trained returns are
pointwise bounded; complete middle q2 has an H1(time;L2) estimate.
The top weight is zero at M3=0 even when Q3 is nonzero, so it supplies no
coercive middle-query tail control. After all regular/learned terms are
bounded, the precise two surviving actual response-energy terms are
the INITIALIZED-transpose terms S1^0 and S2^0 in (18)-(21).
These remain unclosed; no full theorem or cap-uniform extension follows.
Fresh isolated audit BOUNDED_QUARTIC_ACTUAL_FEEDBACK_REVIEW.md is active.

UPDATE: Curie completed and closed; main read all 311 review lines.
Review hash 2f70ef62e95096fdca2322809891bf2e2bf099862c09e1820dbdb404eac02f2b.
Scoped PASS for the identities and a priori estimates, unchanged candidate.
The review correctly sharpens the classification: its energy already has
the direct bound E_B(t)<=t+4KH R^2 t^2. The cancellation plus integrable
transport is NOT new coercive response control. This route is SET ASIDE
unless a new actual estimate for S1^0 or S2^0 is supplied. Do not polish its
weight or infer progress on the universal theorem from the energy bound.

Main additionally reread in full the old actual primitive/log-gate notes:
ACTUAL_LOG_GATE_SECOND_IBP.md (161 lines),
ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md (193 lines), and
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md (308 lines), in the recovered original
directory. The inverse-gate-free full source and correct-metric commutator
cancellation were already resolved there; remaining signed source/memory
and mobility work are not solved by changing the scalar logarithmic gate.
Do not reintroduce those resolved issues as new obstacles.

No full theorem has been obtained in this continuation. All completed
reviewers are closed. No experiments, source-agent resumes, or repository
mutations occurred. The user-authorized universal theorem goal stays active.

### End-of-pass checkpoint, no mathematical completion

Leibniz 01a0735d-e0f9-7543-bf90-454a38f8ff4e completed the independent
global-closure pass and was closed. Main read all 272 lines of
GLOBAL_CLOSURE_INDEPENDENT_PASS.md, hash
53ca10d40ac6f288707cf188ecada095cc17bd1086e569a3d8b12a1e211a0c61.
Classification: NO_NEW_CLOSED_ESTIMATE, not a new theorem candidate.
Continuation in activation amplitude retains the actual signed middle
curvature work (8), with the complete activation-induced preactivation
variation and the initialized transpose acting on the actual gated
readout. Finite-width differentiability in amplitude is not a uniform
transfer estimate. No isolated audit or promotion is claimed for this
failed-search record; do not commission one solely to accumulate identities.

All destination agents commissioned during this pass have completed and
are closed. Paused source agents were never resumed. The active goal is
neither complete nor blocked. The complete angle-specific theorem and its
two isolated complete-proof PASS reports remain the highest certified
result; the ultimate one-data-independent-activation theorem is OPEN.

A next successful attempt must control an actual initialized-transpose
weighted response (for example S1^0/S2^0 in the bounded candidate or the
actual amplitude work in the independent pass), or give a different full
canonical construction with stability and restart. More prescribed-driver
estimates, bounded primal energies, positive-log singular-value estimates,
or re-labeled sufficient criteria do not meet this obligation. No uniformity
over input angles is required for any proof constant. Only the activation
must be fixed independently of data and horizon.
