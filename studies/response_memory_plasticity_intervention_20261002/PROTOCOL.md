# First consequence gate, frozen before outcomes

This supersedes the unexecuted circle design in RESEARCH_SCREEN.md. The authorized
target is useful new-concept adaptation, with exact preservation of the complete
function at the intervention. This is a new optimizer-state intervention, not
a claim about hidden state in dense gradient flow or retention of contradictory
labels. One seed and one aged checkpoint are authorized initially.

## Data and fixed schedule

Use sklearn's bundled digits, seed 20261002 for within-class shuffles. Select
8 training and 40 disjoint held-out images per digit, hence m=80 and 400 test
images. Pixel values are divided by 16, centered with the training pixel mean,
and divided by the single training RMS after centering. No per-pixel variance
division. Keep all input indices fixed. Input dimension d=64; the forward
normalization remains x/sqrt(d). Labels are +1 for a listed digit and -1 otherwise.
Width n=256, float64, canonical Gaussian initialization, zero readout and credit
moments, initial feature moments, clock one; seed 0.

Twelve warm-up positive-class sets, in order:

1. 0,2,5,8,9
2. 0,2,3,4,8
3. 0,2,4,6,8
4. 0,1,5,6,7
5. 1,3,4,6,9
6. 2,3,4,5,9
7. 0,2,4,8,9
8. 0,1,2,4,5
9. 1,2,4,6,7
10. 0,2,3,4,5
11. 1,3,4,7,9
12. 1,3,4,5,8

Probe one: 2,3,4,5,8. Probe two: 0,1,2,3,9. These are generated once by seed
1701 without duplicate/complement partitions; they are not chosen using outcomes.
Each block lasts physical training time 64, integrated by explicit midpoint RK2
with dt=0.1. All continuation arms start from identical physical A,B,w after
warm-up. The second probe continues without any additional intervention.

## Interventions and rivals

The candidate is the regularized feature-alignment gauge in RESEARCH_SCREEN.md:
solve with lambda=0.1 trace(Hbar^T Hbar)/m, clip singular values of R to [0.5,2],
then H<-H R, D<-D R^{-T}. It uses current training inputs, no probe labels.

Before continuation outcomes, add the requested orthogonal mechanism control:
Q is the polar factor of Hbar^T h; H<-H Q,D<-D Q. This preserves singular
values and condition numbers as well as B. Include the identical orthogonal
rotation of ordinary factors at speed one as an equivariance oracle/control.
Ordinary Euclidean factor flow, including its physical-norm scalar multiplier,
must have the same physical trajectory under this common orthogonal rotation.
The full-R intervention remains the primary candidate; Q is a prespecified
mechanism control, not an outcome-selected replacement.

Run candidate at speed one. Run untouched closure, clock refresh
(tau,H)<-(1,H/tau), ordinary factors, gauge-transformed ordinary factors,
balanced-SVD ordinary factors, and dense gradient flow at speeds 0.25,1,4.
Also run norm-balanced closure at speed one. For factor balancing take the
rank-at-most-m SVD B-W0=Q Sigma P^T and use U=Q sqrt(Sigma), V=P sqrt(Sigma),
including at most m singular directions. This balances every factor direction,
not merely total norms; closure balancing
rescales D<-D/c,H<-c H, with c clipped to [0.5,2].

Factors are initialized exactly as U=-2D/(mn tau), V=H, or their prescribed
gauge. G_B=2(delta*r) h^T/(mn) is the physical loss gradient. At every RK stage,
Udot=-eta G_B V, Vdot=-eta G_B^T U,
eta=||G_B||F/||G_B V V^T+U U^T G_B||F. This removes instantaneous middle-update
norm as an explanation. If only the denominator is zero invalidate that arm;
if both vanish take eta=1. First-layer and readout mobilities remain n.
All velocities are multiplied by the arm's scalar speed. The best rival speed
may be selected using probe outcomes, deliberately granting the rival an oracle
advantage; report every arm. Factor methods use the same rank and current input
information as the candidate. Dense flow is the full physical-state reference.

## Decision

Primary metric: held-out MSE integrated over the first 64-time-unit probe,
using observations every unit of physical time and trapezoidal integration.
Secondary: second-probe integrated MSE, endpoint train/test MSE and accuracy.
Record warm-up losses, feature movement, current function jumps, reconstruction
and velocity invariants, and dense-reference hidden-gradient dissipation share.

Proceed beyond one seed only if the candidate's first-probe integral is at
least 25% below the best valid ordinary-factor, clock-refresh, untouched-speed,
and dense-reference rival, with second-probe integral no more than 5% worse.
A tie or loss against a trivial restart/conditioning control kills this witness
as a consequential capability. Intermediate differences are inconclusive and
do not authorize a task search. No gain over untreated closure alone counts.

Validity: exact autograd checks for A,B,w and factor-gradient scaling, and both
product-preserving transformations, must pass in float64. Initial prediction
jump must be <1e-10; all states finite. Warm-up must exhibit relative h movement
>=0.1 and final training MSE <0.1. The dense speed-one middle-layer dissipation
share should exceed 10%; if not, report that the proposed hidden-learning
mechanism was not substantially engaged. Failure of these scientific gates is
inconclusive, not permission to adjust labels or stage duration. If a clear
positive distinction passes, rerun candidate and strongest rival at dt=0.05;
require metric change <2%, then seek the authorized further seeds. A large
negative with exact checks passes the stopping gate without a performance
campaign; no all-time or convergence claim follows.

Budget: one process on physical GPU1, maximum 20 GPU-process minutes, and 30
wall minutes for this first thrust. Producer exits before 19 process minutes.
Save source/protocol hashes, environment, split indices, per-arm trajectories,
checkpoint, exact-check errors and every failed arm in study-owned generated
storage. No package installation, shared-code edits, or Git writes.
