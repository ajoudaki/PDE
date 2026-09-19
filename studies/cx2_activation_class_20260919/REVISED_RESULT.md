# C-X2: onset and perturbed fitting in the activation direction

Author assembly, 2026-09-19; complete independent review is pending. This
extends the earlier partial result without changing its frozen proof files.
The primary pair-input theorem has a new C1,1 proof candidate; the broader
nonatomic fitting extension below has the additional C2 hypothesis.

## Common model and activation classes

Write u=x/sqrt(2) in S1. Use the bias-free two-hidden-layer model, with
the same fixed activation phi in both layers, stored independent centered
Gaussian variances (1,1/n,1/n²), physical mobilities (n,1,n), and unhalved
probability-weighted squared loss. The actual finite Gaussian readout is
retained. Its population initial state is (w,K,c)=(g,0,0), with full
g~N(0,I2), the canonical initialized Gaussian action A0 and its actual
adjoint; A=A0+K, and only K is Hilbert–Schmidt.

Let \(\mathcal A\) be the nonaffine C1,1 functions with bounded derivative,
where C1,1 means that phi' is globally Lipschitz. Let \(\mathcal B\) be its
narrower subclass with phi bounded and phi'' continuous and bounded. It allows nonodd,
nonmonotone functions and flat gates. It requires no third derivative and
no global uniform continuity of phi''. Constants depend on the separately
fixed activation, never on width or hierarchy/numerical resolution.

The state norm is full-row L2 plus increment HS plus readout L2. Population
uniqueness is among strong raw solutions on the same canonical action
carrier. Whole-circle prediction convergence does not identify operators
of different widths in operator norm.

## 1. Broader inputs on a positive onset interval

For phi in \(\mathcal A\) there is a fixed T_phi^local>0 on which every Borel training
law on sqrt(2)S1 × [-1,1] has the canonical strong autonomous flow, with
law continuity and the actual finite GF/GD identification. The time is
uniform over those laws. See ONSET_EXTENSION.md for the precise bounds,
construction, finite-data limit and observation statements.

In particular the full C-H3 represented family is included. Put

    U(s)=((1-s²)/(1+s²), 2s/(1+s²)),
    R_*=[[3/5,-4/5],[4/5,3/5]].

For rational p in [1/3,2/3] and rational interval endpoints a<=b,c<=d
in [-1/20,1/20], use the mixture with mass p on (sqrt(2)U(S),+1)
and mass 1-p on (sqrt(2)R_*U(V),-1), with S,V uniform on their
respective intervals (a point mass for a degenerate interval). Every
cross-component input inner product lies in [2/5,4/5]. Neither the
family nor the positive time depends on numerical resolution.

The dense autonomous closure and its separate numerical refinements
converge to that same flow, uniformly in time and over the whole circle
for predictions, and for fixed admissible joint/initial-current
observations with their second moments. No substantial loss reduction
or universal feature activity is asserted for arbitrary training laws.

There is nevertheless a nonlazy subfamily for each activation. Take the
nonorthogonal central two-atom member p=1/2, a=b=c=d=0. The full-row
Gaussian initialization, nonparallel inputs, positive weights/mobilities,
and nonzero labels verify weighted C.3's hypotheses. At both inputs in
both layers it gives a positive order-t² activation displacement. Fix
one sufficiently small positive t_phi^act<=T_phi^local. The paired
observation/law continuity in ONSET_EXTENSION.md preserves positive
training-averaged squared displacement for nearby members, including
nondegenerate short arcs. Initial nonaffine-fit errors persist by the
moment-continuity argument stated below. This is an activation-dependent
open subfamily, not a claim of universal activity on all circle laws.

## 2. Perturbed orthogonal inputs through substantial training

For every bounded phi in \(\mathcal A\) set

    q0=(1/4) E[phi(Y1)-phi(Y2)]² > 0,
    Cov(Y)=v I + mu0² 11^T,
    mu0=E phi(G), v=Var(phi(G)), G~N(0,1),
    T_phi=log(8)/(4q0).

There is a fixed eps_phi>0 such that every two-atom law with inputs
|u1-e1|<=eps_phi, |u2-e2|<=eps_phi, labels (+1,-1), and weights
(1/2,1/2) has the strong flow through T_phi and

    L_mu(0)=1,              L_mu(T_phi)<1/4.

The exact orthogonal opposite-label reference is global and satisfies
L_*(t)<=exp(-4q0 t); changed-law global-in-time existence is not asserted.
The neighborhood statement is a finite, substantial-training-horizon
theorem. It contains strictly nonorthogonal pairs. Its radius can be
extremely small and is not a practical bound. COMMUTATOR_RESPONSE.md is
the complete new proof candidate: use its preferred raw-Euler construction
in Section 9, take the mesh limit separately for each smooth activation
approximation, and only then remove smoothing. It bounds source rows by
an artificial tangent program on the actual base, followed by a small-
commutator comparison. It never compares second derivatives on different
trajectories and does not require them to converge under smoothing.

For the narrower phi in \(\mathcal B\), BOUNDED_EXTENSION.md additionally admits every
binary Borel law with half mass at each label, supported within eps_phi
of its corresponding axis. Its proof uses a compact-set modulus of phi''.

Choose any one sufficiently small positive rational rho with
2rho<=eps_phi. The represented family with half masses on
(sqrt(2)U(rho S),+1) and (sqrt(2)R U(rho V),-1), R the quarter-turn,
and rational interval endpoints in [-1,1], is then included. It contains
strictly nonorthogonal pairs and nonatomic laws. Its radius stays fixed
through every width, order and numerical limit.

On a possibly decreased but still fixed neighborhood there is a fixed
early t_act>0 with positive training-averaged squared initial/current
activation displacement in both hidden layers. Visited preactivation
laws have positive best-affine-fit error for phi on an initial interval.
These assertions do not claim activity specifically at the later fitting
endpoint, superiority to a baseline, or arbitrary-data fitting.

For clarity, the early activity assertion also applies to the C1,1
two-atom family. At the orthogonal reference weighted C.3 gives a positive
order-t² activation displacement at each anchor in both layers. Choose
one fixed sufficiently small t_act<min(T_phi,T_phi^local). State and input
continuity from COMMUTATOR_RESPONSE.md, with its uniform passive tails,
preserve half of the minimum of those four positive RMS values on a
smaller fixed radius. At time zero every relevant preactivation is a
nondegenerate Gaussian, so nonaffinity gives a positive affine-fit error.
The formula Var(phi(Z))-Cov(Z,phi(Z))²/Var(Z), its positive denominator,
and L2 continuity preserve that error on a fixed initial interval and
then on a smaller input neighborhood. This argument uses no phi''
continuity. All initial/current comparisons use the same population rows.

The strong target and exponential tails supply S/E in CLOSURE_PROOF.md
for both families; the finite bridge is PARTIAL_RESULT.md Section 3.
Actual finite GF and simultaneous
raw GD with eta_n->0 converge for data laws approaching each fixed target
law; the strict risk margin gives finite training loss at most 1/4 with
probability tending to one. There is no relative sample/width growth
restriction. This is not an
order/width rate or uniform-in-time finite-width theorem.

For the two-atom target, the data-sequence extension of that fixed-data
bridge is explicit: couple the actual finite data law to the fixed
two-atom comparison law. Subtract the full-row, HS and readout velocities
as in ONSET_EXTENSION.md's transport estimate. On the stopped raw ball,
this adds at most C(1+R)W1(lambda_n,mu) to the finite proxy comparison;
all cutoff tails remain on the fixed comparison proxy. Take width first
at each fixed proof mesh/cutoff, then remove those proof approximations.
The extra term vanishes for every sequence lambda_n->mu. The actual
training laws need not themselves be two-atomic. The nonlinear population
existence theorem being invoked is still only for the fixed target law.

### Whole-circle learned endpoint of the reference

The same results also give the endpoint comparison present in C-H4,
after increasing the fixed fitting horizon if necessary. Here is the
additional argument; it does not assert a changed-law infinite-time limit.
Write H=||phi||infty, D=||phi'||infty, lambda=2q0. Reference symmetry
and fitting give |r_1(t)|=|r_2(t)|<=exp(-lambda t). The exact raw
equations and bounded phi therefore give the following time-uniform bounds:

    Cbar=2H/lambda,                 ||c(t)||infty<=Cbar,
    Abar=10+2Cbar D H/lambda,       ||A(t)||op<=Abar,
    Wbar=sqrt(2)+2Cbar D² Abar/lambda,  ||w(t)||2<=Wbar.

Indeed integrate ||c'||infty<=2H exp(-lambda t), then
||K'||HS<=2Cbar D H exp(-lambda t), then
||w'||2<=2Cbar D² Abar exp(-lambda t), in that order. The sum
V=2H+2Cbar D H+2Cbar D² Abar bounds the raw speed after dividing
by exp(-lambda t). Thus w and K converge strongly in L2 and HS,
and c converges in Linfty, with total raw endpoint error at most
(V/lambda)exp(-lambda t). Completeness supplies the actual endpoint.

Subtracting f(u)=E[c phi(A phi(w.u))] at two reference states gives

    |delta f(u)| <= H||delta c||2
                 +Cbar D[H||delta K||HS+Abar D||delta w||2].

This estimate is uniform in u. With
B=(H+Cbar D H+Cbar D² Abar)V/lambda there is consequently a
whole-circle endpoint f_*^infty satisfying

    sup_u |f_*(t,u)-f_*^infty(u)| <= B exp(-lambda t).

In particular f_*^infty(e1)=+1 and f_*^infty(e2)=-1.
Choose the fixed horizon

    T_phi^end=max(T_phi, log(8 max(1,B))/lambda).

Apply the same near-orthogonal construction at this finite horizon;
it is proved for every separately fixed T. Its one-reference comparison
makes sup_(t<=T,u)|f_mu(t,u)-f_*(t,u)| tend to zero as the supported
input radius tends to zero. Choose the radius so that this difference
is at most 1/16 and so that the separate fitting estimate has its strict
1/4 margin. Then

    sup_u |f_mu(T_phi^end,u)-f_*^infty(u)| <=3/16<1/4,
    L_mu(T_phi^end)<1/4.

Both statements transfer to actual finite GF/GD at that time with
probability tending to one, by whole-circle convergence and the strict
margins. They apply to bounded C1,1 on the perturbed two-atom family,
and to the supported Borel/represented arc family under the additional
C2 hypothesis. The same hierarchy and numerical limits below hold through
T_phi^end. No convergence rate in hierarchy order is inferred from this
reference's physical-time exponential estimate.

## 3. Executable hierarchy and its exact limit scope

CLOSURE_PROOF.md defines the dense smooth-probe hierarchy independently
of the training activation. NUMERICAL_EXTENSION.md and activation_closure.py
implement the cofinal prefix through code 16N with ridge 2^-N, complete
Gaussian source initialization, both action directions and the same
nonlinear phi in every current and initial paired field. The state is
two current joint populations and one finite feature-action matrix;
its size has no neural-width or elapsed-step parameter.

The literal finite-arithmetic theorem requires pure, locally uniformly
consistent evaluators for phi and its actual derivative. Regularity alone
does not imply computability. For each fixed admitted law the refinements
are, written with the outermost limit first,

    lim_N lim_epsilon↓0 lim_Q lim_P lim_input-quadrature lim_h↓0 lim_precision.

Here epsilon regularizes source covariance, Q initializes source
coefficients, P replays the joint population marks, and h is the ODE mesh.
The input limit is omitted for an exact finite law. No arbitrary diagonal,
approximation-order rate, fixed-run accuracy certificate or usable
cost-to-tolerance bound is proved. Runtime and initialization costs, and
the separate cost of supplied activation evaluators, are accounted for
in NUMERICAL_EXTENSION.md.

Eight preregistered deterministic supplied-state checks passed. These
verify algebra and execution, not trained-trajectory accuracy. No new
training experiment ran. All generated records are separately stored
under data/generated/cx2_activation_class_20260919/.

## 4. Claim boundaries and the remaining extension

The primary onset claim covers all of \(\mathcal A\) and the full C-H3 represented
family. The primary perturbed-pair fitting candidate covers the bounded
part of \(\mathcal A\). Its complete audits are still required; a scoped lemma check
cannot accept the full theorem. BOUNDED_EXTENSION.md records the earlier
source-comparison gap. COMMUTATOR_RESPONSE.md proposes a different
argument for two atoms; it does not retrospectively fix that earlier
comparison proof.

For arbitrary bounded C1,1 activations, the nonatomic fitting extension
remains open. Within a cluster of nearly parallel input directions the
control brackets need not be uniformly small when phi'' jumps; the
example in BOUNDED_EXTENSION.md makes this obstruction explicit. The C2
source-comparison theorem supplies that broader family only under its
stated extra regularity. This is a limitation of the currently proved
routes, not a neural counterexample.

Substantial training for general unbounded activations, nonsmooth gates
such as exact ReLU, extra depth, and useful approximation-order rates
remain outside the revised completion contract. No promotion is requested
or performed by this assembly.
