# What second-order perturbations prove about the rho family

2026-09-16. Current synthesis for this continuation. Internal research only.
The all-rho, unit-label perturbation theorem is still open. The new results
are a sharper sufficient condition for that theorem, a characterization of
its possible obstruction, and complete second-order geometry for six free
input directions. Neither a finite-time Taylor formula nor genericity in
label amplitude is substituted for the requested all-time theorem.

## 1. The family, model, and potential

The earlier broad family consists of the signed unit directions

    v1=(a,b,b), v2=(b,a,b), v3=(b,b,a),
    a^2+2b^2=1, a!=b, rho=vi.vj=2ab+b^2 (i!=j).

With labels y=(+1,+1,-1), the original unit inputs are u_i=y_i v_i;
physical normalized-sphere inputs are sqrt(3) u_i. Equal masses are 1/3.
This is the canonical dimension-three dictionary, not a change of notation
for the original dimension-two circle dictionary. The full correlated
initialization, eta=1/4096 normalization, evolving w,c,M and actual transpose
are retained. There are generally two dictionary orientations for a given
rho in (-1/2,1); arbitrary rotations are not a symmetry of the dictionary.

At any state, use the signed fields

    a_i=E1[b1 tanh(w.v_i)], z_i=b2^T M a_i,
    H_i=tanh z_i, d_i=E2[b2 c sech^2 z_i],
    m_i=E2[c H_i], F=(m1+m2+m3)/3, q=E2[c^2].

Because the model is odd in its input, m_i=y_i f(u_i). Let

    L=(1/3) sum_i(m_i-1)^2,
    C0=E2[((H1^0+H2^0+H3^0)/3)^2],
    W=1+C0(1+q)/(C0+F^2), Phi=L W.                 (1)

C0 is determined by the actual prescribed inputs and initialization.
It is recomputed when the data change. It does not depend on a future
trajectory or endpoint. The state during training and this fixed number
are sufficient to evaluate Phi.

The symmetric family already has Phi_dot<=-4C0 Phi, L<=Phi<=2L,
Phi(0)=2, and convergence of its complete state. The preceding
unconditional free-neighborhood theorem only certified seeds with rho
sufficiently near 1. The user's criticism of that restriction is correct.

## 2. A stronger extension criterion across the broad family

For the physical gradient metric, the three prediction gradients are

    grad m_i=(sech^2(w.v_i)(b1^T M^T d_i)v_i, H_i, d_i a_i^T).

Their normalized Gram is K_ij=<grad m_i,grad m_j>/3. Along a symmetric
trajectory K has a mean eigenvalue k and a double disagreement eigenvalue
nu. The former stays at least C0. The latter is exactly

    nu=(1/6)||grad m_i-grad m_j||^2, i!=j.           (2)

The new sufficient condition is only nu>0 at the limiting fitted state.
Positive nu at every earlier time is unnecessary. Under this endpoint
condition, there is a full open neighborhood in (S^2)^3 of the chosen
symmetric triple, with unit labels unchanged, on which the SAME potential
(1) satisfies

    Phi_dot<=-lambda Phi, L<=Phi, Phi(0)=2           (3)

for every physical time and a common lambda>0. The complete perturbed
state converges to a fitting state. The neighborhood and rate may depend
on the reference geometry.

The proof uses strict potential decay on a finite initial interval and
the positive endpoint Gram to trap the perturbed tail. Inside its small
neighborhood, K>=kappa I gives remaining state length at most
sqrt(L/kappa). Every derivative of W is kept: its contribution is
O(L^(3/2)), dominated by the negative O(L) term when the tail loss is
small. The reference endpoint is a proof device, not an ingredient of Phi.
Complete proofs are in `rho_endpoint_extension.md` and the independently
derived `rho_hessian_geometry.md`, section 6.

For EVERY admitted rho, including the coplanar boundary -1/2, equation (2)
vanishes at a positive-output symmetric state exactly when

    M a1=M a2=M a3, and d1=d2=d3=0.                 (4)

Thus equal upper activations alone do not erase learning sensitivity:
the first hidden layer's backward response can still distinguish inputs.
At (4), all hidden velocities vanish but the readout keeps moving. If the
common preactivation is z=b2^T zbar, the derivative of the common backward
vector in auxiliary time satisfies

    zbar^T d_s=E2[z tanh(z) sech^2(z)]>0.

Consequently every such rank-loss event is isolated and quadratic:
nu(s)=c(s-s0)^2+o((s-s0)^2), c>0. There are finitely many on a compact
auxiliary segment. This rules out persistent symmetric collapse, but
does NOT rule out a contact exactly where F=1.

The exact remaining unit-label question is therefore

    Can F=1 and (4) occur together on a prescribed initialized curve? (5)

Neither independent route excluded it. Local finite exceptional
common-label amplitudes, or a null set of geometry/amplitude pairs,
does not settle the fixed amplitude 1 slice. No compatible initialized
failure-to-fit example was obtained.

## 3. Free sphere perturbations and the full trained Hessian

For each input choose eta_i perpendicular to v_i, independently, and put

    v_i(tau)=(v_i+tau eta_i)/sqrt(1+tau^2 |eta_i|^2).

There are six independent tangent directions. The sphere contributes the
essential acceleration v_i''(0)=-|eta_i|^2 v_i. For two directions eta,
theta its mixed acceleration is -(eta_i.theta_i)v_i. Both trained hidden
layers, the readout and the middle matrix also respond to these changes.

`sphere_second_variation.md` proves, for every finite T, C2 dependence of
the FULL initialized population flow on these six data coordinates, with
a cubic Taylor remainder on [0,T]. The proof uses Gaussian-weighted row
spaces, bounded upper marks and finite Gaussian moments; it does not
assume twice differentiable nonlinear calculus on an unrestricted L2
ball. Six first-response and 21 mixed second-response equations are given
explicitly, together with the complete Hessian of (1), including C0's
data derivatives.

There is a particularly clear formula at a symmetric seed. Simultaneous
coordinate and sample permutations act on the six tangent coordinates.
Their invariant subspace is one-dimensional; averaging over permutations
projects onto it. In its five-dimensional kernel, every first variation
of F,q,C0 and Phi vanishes. These are precise symmetry-breaking directions,
not a claim that all six first derivatives vanish.

Write e=1-F and delta_i=m_i-F, so L=e^2+(1/3)sum delta_i^2. In any one of
those five directions, the exact second derivative of the trained
potential at any fixed finite physical time is

    D_eta^2 Phi
      =(2W/3) sum_i(D_eta delta_i)^2
       +(-2e W+e^2 W_F) D_eta^2 F
       +e^2 W_q D_eta^2 q
       +e^2 W_C D_eta^2 C0.                            (6)

Here W_F,W_q,W_C are the ordinary partial derivatives of the explicit
function W(F,q,C) in (1); all D_eta derivatives include the trained state
response. In particular,

    W_F=-2C0(1+q)F/(C0+F^2)^2,
    W_q=C0/(C0+F^2), W_C=(1+q)F^2/(C0+F^2)^2.

Equation (6) is a second-order description of the mixture the user asked
for. Disagreement contributes a positive square. Changes in the mean
prediction, readout size and initialized geometry add terms without a
fixed sign. The full response equations express these terms through both
forward layers and the reverse interaction. Polarization gives all mixed
input Hessians. No pairwise rule requiring all within-class distances to
shrink is asserted or needed.

## 4. What the Hessian misses at a possible singular endpoint

At a state satisfying (4) and m_i=1, every prediction has the same gradient
g_*=(0,H,0), and every fixed-state input derivative vanishes. Let h be a
state direction with <g_*,h>=0, and perturb X by tau h along with the input
curve. Set

    A_i=E1[b1 sech^2(w.v_i)(h_w.v_i+w.eta_i)],
    Z_i=b2^T(h_M a_i+M A_i).

The complete quadratic predictor response is

    B_i=2E2[h_c sech^2(z) Z_i]+E2[c tanh''(z) Z_i^2].    (7)

Sphere curvature and lower second derivatives have been included before
simplification; their coefficients are the zero vectors d_i. Both hidden
layers still enter (7) through A_i and M. After allowing a second-order
common prediction correction, the smallest resulting leading loss is

    (tau^4/12) sum_i(B_i-bar B)^2, bar B=(B1+B2+B3)/3.   (8)

This is a quartic loss effect invisible to the loss Hessian. It may vanish
for particular directions. Independently, the two weak tangent-Gram
directions can open at order tau^2. The exact coefficient is the Gram of
the first gradient differences AFTER projecting away the old common
gradient; the unprojected Gram is not enough. The complete formulas and
proof are in `rho_singular_hessian.md` and its isolated review.

These calculations are local geometric statements. They do not assert
that gradient flow selects the freely chosen h or correction, that the
state (4) is reached, or that positive quadratic metric opening alone
proves all-time capture. At this possible obstruction the next missing
estimate must compare quadratic residual production with quadratic
sensitivity and control their subsequent evolution.

## 5. Global information and its limits

The second-order analysis gives two global constraints on any eventual
answer. First, C0 is positive for EVERY signed sphere triple, including
degenerate ones; nevertheless the original symmetric rate 4C0 cannot
hold on all generic triples. Near identical physical inputs with opposite
labels the time needed to fit cannot be bounded uniformly. The explicit
continuity argument is in `rho_global_rate_boundary.md`. This permits
positive geometry-dependent rates and does not give a fixed compatible
configuration with failure to converge.

Second, the trained potential as a function of the input configuration
cannot have an everywhere positive-semidefinite or everywhere
negative-semidefinite sphere Hessian for all sufficiently small positive
times. It is nonconstant on the compact product of spheres, and a
nonconstant C2 function there cannot have a globally one-signed Hessian.
This does not prevent monotonic decrease in TRAINING TIME. Input curvature
and the time derivative are different mathematical questions.

The inverse-correction geometry identifies a useful complete square as
well: in mean/disagreement coordinates, with K=[[k,b^T],[b,H]], the
minimum squared physical correction is

    e^2/k+(zeta+e b/k)^T(H-b b^T/k)^(-1)(zeta+e b/k),

where zeta is the probability-normalized disagreement. Its mixed square
couples mean error, disagreement and changing tangent geometry. Its
complete second derivative and the required moving-metric derivative
are retained in `rho_hessian_geometry.md`. A global decay inequality for
this alternative geometry remains unproved.

The current unconditional unit-label free-neighborhood theorem is still
the previous near-rho=1 result. The present work extends the sufficient
criterion to every member of the broad family and supplies the full
second-order information requested, while leaving (5), or an alternative
nonlinear treatment of that event, as the precise outstanding obligation.
