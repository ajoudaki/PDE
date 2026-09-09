# Fixed-depth canonical construction, cap removal and observation limits

This companion supplies the bridge for PROOF.md, with L>=2 fixed before
width is taken to infinity. Its generic finite-program input is the
proved construction in ../three_sample_self_contained/foundations.md,
Sections 1--9. The observation arguments are derived in that manuscript's
velocity.md, Sections V.2--V.11. We state their exact specialization,
check the hypotheses, and describe the finite-depth induction. Neither
an affine comparison nor two-sample symmetry is an input to this bridge.

## 1. Finite programs and common action spaces

A program has a fixed finite number of instructions on layer-typed
vectors: independent Gaussian roots; fixed C^1 coordinate maps with
bounded continuous first derivatives; linear combinations; applications
of any of the L-1 initialized independent Gaussian adjacent matrices or
their transposes; and causal scalar feedback from same-layer inner
products through locally Lipschitz scalar maps. Each fixed program's
within-layer joint empirical laws, including second moments, converge
in probability in W2 along the full width sequence. An oriented matrix
call on input h is represented by its centered Gaussian source plus the
sum of its expected named derivatives against earlier opposite-orientation
sources, multiplied by those opposite inputs. Each oriented source
group's covariance is the FULL Gram of its actual inputs. Different
oriented groups are independent. Named slots remain separate even when
source covariances are singular; all scalar feedback, expectations and
covariances are frozen in those derivatives.

Here is why the existing proof applies to L-1 matrices. Conditional on
previous queries of a particular Gaussian matrix, its unused block is
P_left G P_right; all other matrices remain separately conditioned
through their own transcripts. The next query is the conditional mean
plus this independent Gaussian innovation. Empirical bounded-test and
second-moment concentration identify its next scalar law. Query-input
perturbation by independent Gaussian noise makes each provisional Gram
invertible. Fixed-program bounded-operator stability removes that noise;
positive-semidefinite square-root continuity couples the limiting
covariances at singularities. Induction counts instructions, not layers.
Adding finitely many matrices only adds finitely many such steps. No
source-covariance inverse remains in the final identity.

The spectral-norm input used here is
E||G_(m,n)||<=sqrt(m)+sqrt(n) and
P(||G_(m,n)||>=sqrt(m)+sqrt(n)+u)<=2exp(-c u²) for independent standard
Gaussian entries. These are Theorem 7.3.1 and Corollary 7.3.3 of
[Vershynin, High-Dimensional Probability](https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf).
For W=G_(n,n)/sqrt(n), take u=sqrt(n) to obtain P(||W||>3)->0.
The same applies to its transpose and, by a finite union bound, to all
L-1 actions. The first three projection empirical squared norms tend to
one by the Gaussian law of large numbers. Thus the finite operator and
projection events used in SOURCE_RESPONSE.md and PROOF.md have probability
tending to one. Taking u=epsilon*sqrt(n) and a countable dense set of
fixed generated inputs gives canonical action norms at most 2.

A countable language including all rational linear combinations,
bounded smooth coordinate probes, integer clips, rational meshes and
both action orientations generates one probability space per layer.
Finite-program consistency supplies their joint cylinder laws. On the
dense span of generated fields, the finite norm and inner-product
identities pass to the limit. Hence each initialized action extends
boundedly to its layer L2 space, and its reverse is its genuine Hilbert
adjoint. Approximation by bounded smooth cylinder functions gives density
in L2. These are the canonical initialization spaces, not arbitrary
bounded operators with the same norms.

The population parameter space is the first-layer vector L2 space,
the affine spaces A_(ell,0)+HS(H_(ell-1),H_ell), and the top readout H_L.
The raw metric is the one in PROOF.md. Rank-one velocities have norm
||u tensor v||HS=||u||_2||v||_2, so continuous raw updates integrate in
HS. Their reversed increments are their actual adjoints.

In our application, every psi_ell has bounded continuous derivative and
every fixed clipped backward gate D_(ell,R) has bounded continuous first
derivatives. Scalar physical feedback is the residual vector, a locally
Lipschitz function of inner products on bounded primal balls. All the
finite-program hypotheses have therefore been checked. The effective
residual-clock controls are frozen only in formal source derivatives;
the physical residual feedback remains part of the actual dynamics.

## 2. Fixed-cap existence and asymmetric comparison

For fixed finite L,a,R, forward and backward induction on a bounded
primal ball gives a raw locally Lipschitz field. The first projection
map is bounded in the raw metric; every next layer uses a bounded
action, a Lipschitz activation and continuous bilinear evaluation.
The clipped gates are globally Lipschitz. Each rank-one update is
locally Lipschitz by

    ||u tensor v-u' tensor v'||HS
       <=||u-u'||_2||v||_2+||u'||_2||v-v'||_2.

The integral map is a contraction on a sufficiently short interval.
Strong Cauchy endpoints and the uniform primal bounds extend the clipped
solution. PROOF.md Sections 4--5 establish its global continuation with
strict residual-clock slack, independently of all cap-removal arguments.

For R'>=R, including R'=infinity, the normalized gates obey

    |D_(ell,R')(z,q)-D_(ell,R)(z',q')|
      <=2|q-q'|+2K_ell R|z-z'|
           +2|q'|1_(|q'|>R).                              (25)

To verify (25), first change q to q' in D_(ell,R'), which costs at most
2|q-q'|. In the remaining nonlinear term use the decomposition

    [g(K_ell z)-g(K_ell z')]tau_R(q')
       +g(K_ell z)[tau_R'(q')-tau_R(q')],

where tau_R' in this display denotes the clip at level R', not a
derivative. Bounded g', |tau_R|<=2R, and equality of both clips inside
[-R,R] give the other two terms. This asymmetric decomposition requires
tail control only of the reference state (z',q').

Forward state differences are bounded by C times the raw state
difference. Backward substitution through any finite L multiplies an
existing discrepancy only by a bounded action and the gate's q-Lipschitz
constant 2. Every newly introduced factor R multiplies a FORWARD
discrepancy already bounded separately. It does not multiply a previous
R term. Rank-one updates and residual feedback then give

    ||F_R'(Theta)-F_R(Theta')||raw
      <=C_(L,a,b)(1+R)||Theta-Theta'||raw
         +C_(L,a,b) sum_Q ||Q(Theta')1_(|Q(Theta')|>R)||_2.  (26)

Here F_R' means the field at cap R', b denotes the common primal ball,
and the finite sum runs over the reference's incoming fields. The same
bound holds for all backward field differences. Physical gain factors
are fixed constants a^L. Coefficient differences in residual feedback
are bounded by the already controlled forward and readout differences.

SOURCE_RESPONSE.md and PROOF.md (24) provide Gaussian reference tails
uniformly in time and cap. Integrating (26) and Gronwall's inequality
therefore gives on each physical [0,T]

    sup_(t<=T)||Theta_R'(t)-Theta_R(t)||raw
       +sup_(t<=T)||F_R'(Theta_R'(t))-F_R(Theta_R(t))||raw
                       <=C_T exp(C_T R-cR²).               (27)

Polynomial factors in R are absorbed into C_T exp(C_T R). Thus paths
and raw velocities are uniformly Cauchy. Their limit is strong C^1 and
satisfies the uncut equations by (26) and bounded-multiplier continuity.
Taking integer caps and horizons gives one consistent global solution.

For any other strong uncut solution with bounded primal quantities on
[0,T], compare it to the same clipped reference using (26). Only its
primal bound enters C_T; its own tails are not assumed. Equation (27)
forces equality in the limit. At a reached time t0, the initial error
against the clipped reference is already of the form (27), and another
factor exp(C_T R) still tends to zero. This proves uniqueness of
continuation from that state. No arbitrary-state L2 local theorem for
the uncut vector field is used.

## 3. Strong chain rule and raw gradient identification

If X(t) is a strong C^1 L2 curve and psi is C^1 with bounded continuous
derivative, then psi(X(t)) is strong C^1 and has derivative psi'(X)X'.
Indeed integrate X' to obtain almost-everywhere absolutely continuous
coordinate versions and apply the scalar chain rule. The multiplier
product is L2-continuous: if X_k->X and P_k->P in L2, split

    psi'(X_k)P_k-psi'(X)P
      =psi'(X_k)(P_k-P)+[psi'(X_k)-psi'(X)]P.

Boundedness treats the first term; convergence in probability and an
integrable |P|² dominator treat the second. The coordinate integral
identity passes to L2. Repeating with the continuous bilinear action
product rule proves the strong forward chain rule at all L layers.

The scalar predictor's hidden directional derivative pairs each raw
increment against the corresponding backward rank-one field. This
follows by repeated Hilbert adjunction and Cauchy--Schwarz; all gates
are bounded and all fields are L2. The first-block factor is 1/d in
the original w coordinates. The scalar derivative is continuous in
the raw state: the same bounded-multiplier argument treats varying
backward fields. Consequently the limiting autonomous equations are
the raw Hilbert gradient flow of the stated squared loss, and its
energy identity follows by the scalar chain rule. No Frechet
differentiability of the activation map on a whole L2 ball is asserted.

## 4. Fixed-cap finite GF and raw GD

At a fixed cap and physical horizon, take a coarse mesh of finitely
many time steps. The finite-program theorem identifies its full-width
limit. Scalar feedback uses all three residuals, not a prescribed
population residual in place of the actual finite residual. A sufficiently
large finite primal ball contains these coarse nodes with high
probability: first-layer and readout norms converge, and each hidden
matrix increment is bounded by the sum of its rank-one update lengths,
whose finitely many contractions converge.

On that enlarged ball the clipped field has norm M0 and Lipschitz
constant L0 independent of width. The exact GF/Euler local defect for
a step h is <=L0 M0 h²/2. Iteration gives a uniform state error bounded
by C_T times the mesh size, with first-exit slack keeping all states
in that ball. This proves finite GF versus the coarse Euler program,
and simultaneous raw Euler with fine step n^-2 versus that GF. It
does not apply fixed-program convergence to n² growing instructions.
Take width first at the coarse mesh, then send that fixed mesh size
to zero. The population coarse Euler program converges by the same
Hilbert-space estimate. Its limit is the unique clipped solution.

The actual finite Gaussian C_n(0) has E||C_n(0)||_n²=n^-2. Its initial
discrepancy from the zero-readout finite comparator is O_P(n^-1).
The fixed-cap Lipschitz comparison bounds the propagated discrepancy
by exp(L0 T)O_P(n^-1). Thus zero is the population initial readout;
neither actual finite GF nor actual finite GD is initialized at zero
by substitution.

For the uncut finite algorithms, apply (26) with the finite clipped
reference. At fixed cap, the finite empirical incoming tails converge
to their population reference tails, using continuous truncations and
second-moment convergence. Uniformity in time comes from a finite time
net and the fixed-cap strong moduli described below. Finite first-exit
comparison then gives limsup-width errors of the form (27). For GD,
the discrete version has the same single factor R and a vanishing
fixed-cap O(n^-2) consistency term; the hidden fields are recomputed
from the raw linear interpolation. Send width to infinity first and
then R to infinity. This gives both algorithms the same full-sequence
limit. A subsequence argument upgrades any almost-sure extracted
comparisons to convergence in probability of the original full sequence.

## 5. True kernels, velocities and paths

For the original raw model let b_i^ell be the TRUE backward fields.
The L+1 kernel blocks are

    K^1_ij=Gamma_ij <b_i^1,b_j^1>,
    K^ell_ij=<b_i^ell,b_j^ell><h_i^(ell-1),h_j^(ell-1)>,
                 2<=ell<=L,
    K^(L+1)_ij=<h_i^L,h_j^L>.

Every inner product is within its designated layer. These are the true
raw kernels even when observed at an auxiliary clipped state; clipped
update fields are not substituted for their b fields.

The fixed-cap observation proof in velocity.md V.3--V.6 has these
premises: bounded clipped primal states on the observation interval;
bounded continuous coordinate derivatives; deterministic causal
source coefficients; finite-dimensional Gaussian query perturbations
continuous under vanishing perturbation; and the already proved
fixed-mesh primary width laws. All were verified in Sections 1--4.
Its depth induction proceeds as follows.

A fresh independent Gaussian probe added to any named answer slot
changes the recomputed clipped raw trajectory by C epsilon, or by
C h_j epsilon if inserted only at a strictly past time j. Gaussian
integration by parts with deterministic coefficients frozen bounds
the ABSOLUTE ROW OF EXPECTED source derivatives, after choosing signs,
by C or C h_j. Current reverse responses are retained and constructed
in descending layer order. With these deterministic rows bounded,
differentiate the local source equations pointwise. Bounded gate
derivatives and the strict forward time order yield a discrete
Volterra inequality U_k<=C+C sum_(j<k)h_j U_j for the maximum primary
absolute derivative row. Summation of nested time integrals costs at
most the fixed horizon. The L-1 backward levels are a finite causal
substitution, so U_k<=C exp(CT). Repeating with Lp norms gives primary
source bounds C sqrt(p). No matrix Lp-to-Lp action bound is assumed.

Append instantaneous velocity queries in ascending layer order. With
P_i^ell=dot z_i^ell and U_i^ell=phi'(z_i^ell)P_i^ell,

    P_i^1=dot w.x_i,
    P_i^ell=dot A_ell h_i^(ell-1)+A_ell U_i^(ell-1).

The learned action part is an explicit rank integral. For each newly
appended initialized-action call, its reverse-source derivative is a
sum of the previously bounded derivatives and a bounded gate derivative
times the incoming velocity. Its Gaussian source variance is the actual
L2 norm of that incoming query. The preceding layer and primal raw
direction bounds control this norm before any higher-layer velocity
estimate is invoked. Induction yields fixed-cap marginal C_(L,R,T)
sqrt(p) bounds for appended velocities on population fine meshes and
flows. Same-family joint time and sample covariances are retained.

Products phi'(Z)P do not have globally bounded derivatives in (Z,P).
The observation proof therefore uses phi'(Z)tau_M(P), a legitimate
bounded-derivative instruction, and removes the clips in the following
order: keep the new outer query cap M fixed while removing all earlier
inner velocity caps, then remove M using the proved marginal tail
bounds. True-backward observations use the same descending ordered
truncation. This verifies the fixed-program laws of the unbounded
products rather than assuming them. The construction uses L steps,
each already supplied with the previous step's norm and tail estimate.

For a state/direction pair and a reference pair, the deterministic
product comparison has the form

    ||phi'(Z)P-phi'(Z0)P0||_2
       <=C||P-P0||_2+C M||Z-Z0||_2
                  +C||P0 1_(|P0|>M)||_2.                  (28)

It follows by splitting P0 at M and using bounded phi' and phi''.
Forward induction leaves one M times the primary state discrepancy,
plus the reference velocity tails. At fixed cap, the proved moment
bounds and raw Lipschitz state/direction estimates yield a uniform
L2 time modulus for velocities (a square-root modulus suffices).
This justifies passage from finite time nets to uniform-in-time
state/velocity empirical W2 laws. In the cap-removal step, the uncut
reference's velocity image is compact in L2 by the strong chain rule,
which implies uniform L2 tail removal. Equation (28), with state/raw
direction convergence first and M then sent to infinity, transfers
these velocity laws to the uncut flow. It does not require an unproved
cap-uniform pointwise bound on the entire velocity path.

All true kernel terms are continuous functions of the corresponding
convergent L2 backward and feature pairs, so their convergence is
uniform on the physical horizon. Joint observations at any fixed finite
collection of times are included by appending that finite list before
the fixed-program limit. The same applies to fixed finite generated
probes formed from layer-typed bounded-derivative maps, contractions
and either action orientation. Second moments and integrals of squared
speeds follow from the uniform W2 state/velocity convergence.

Finally, a continuous coordinate path X with square-integrable speed
and its piecewise-linear interpolation on a mesh of size h obey

    ||X-Interp_h X||_infinity² <=4h integral_0^T |X'(t)|²dt.

This is the intervalwise Cauchy--Schwarz estimate and the triangle
inequality between endpoints. Apply it inside each empirical layer
law and inside the population law. Fixed-mesh joint laws converge;
the integrated speed bounds make both interpolation errors uniformly
small as h decreases. This proves W2 convergence in the uniform path
norm, without replacing a supremum of marginal moments by a moment of
a random time supremum.

Every estimate above is for fixed finite L,a and a fixed physical
horizon. Width precedes the auxiliary cap and observation-truncation
limits. The common activation in PROOF.md is independent of L, but
the bridge constants and the width needed for a prescribed accuracy
need not be uniform in L. This distinction completes the theorem's
stated quantifiers.
