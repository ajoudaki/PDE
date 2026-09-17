# Regular corrections from the actual flow, and their remaining obstruction

2026-09-16. Frozen scoped theoretical report. Internal research only. No
experiment, code change, network-limit statement, or promotion is made.

Scientific inputs were the assigned canonical notation and p=1 coefficient,
state, gradient, existence and restart material in `docs/NOTATION.md`,
`docs/observable_p1.md`, and `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 B/C.1/D.3; and the complete same-study
`three_coordinate_candidate.md`, `perturbation_modes.md`,
`perturbation_metric_template.md`, `rho_hessian_geometry.md`,
`rho_endpoint_extension.md`, and `resolution_open_family.md`.
No links to additional research reports were followed. The
investigate-conjectures and solve-math-rigorously skills govern this analysis.

**Result.** There is an explicit correction metric that stays regular at every
possible transverse rank loss on every symmetric rho curve. Its leading
correction follows from the first *flow* response and cancels the direct
mean-to-disagreement forcing. Its complete physical derivative still contains
terms with no proved sign, so this does not supply a new unit-amplitude
geometry range. A second current-state construction gives a bounded readout
which fits a collapsed upper feature and annihilates its first spatial
derivatives; its exact comparison-energy derivative exposes the missing hidden
term. Finally, conditional on a singular symmetric fitting endpoint, the
actual initialized first and second flow responses have well-defined limits:
the first output response tends to zero, while the transverse second response
is an explicit quadratic expression independent of the second state response.
These facts locate the unresolved issue at nonlinear organization rather than
at the first-order homogeneous transverse damping alone.

## 1. Exact object and notation

Keep the prescribed d=3, p=1 Gaussian closure, eta=1/4096, the complete
correlated lower marks, full evolving matrix M and its actual transpose.
The physical state is X=(w,c,M), with metric

    ||delta X||^2=E1|delta w|^2+E2|delta c|^2+||delta M||F^2.

Absorb the unit labels into v_i=y_i u_i, so each target is one. For each
input define

    a_i=E1[b1 tanh(w.v_i)], z_i=b2^T M a_i,
    H_i=tanh(z_i), s_i=sech^2(z_i),
    d_i=E2[b2 c s_i], Q_i=b1^T M^T d_i,
    g_i=grad f_i=(sech^2(w.v_i)Q_i v_i,H_i,d_i a_i^T).

Write r_i=(f_i-1)/sqrt(3), J h=(<g_i,h>/sqrt(3))_i and K=JJ*.
Thus

    X_dot=-2J*r, r_dot=-2Kr, L=|r|^2,
    L_dot=-4r^TKr=-||X_dot||^2.                         (1)

Let n=(1,1,1)/sqrt(3), and let E be a fixed 3-by-2 orthonormal frame of
n-perp. Here n is this fixed vector, not network width.
Set

    F=(f1+f2+f3)/3, e=1-F, zeta=E^T r,
    k=n^TKn, b=E^TKn, H=E^TKE,
    q=E2 c^2, V=|zeta|^2, L=e^2+V.

The letter H without a subscript in these formulas is a 2-by-2 matrix;
H_i remains an upper activation. Directly from (1),

    e_dot=-2ke+2b^T zeta,
    zeta_dot=2eb-2H zeta,
    q_dot=4eF-4V.                                     (2)

The last identity uses only linearity of every output in c. It does not
require data symmetry.

The symmetric seeds are v_1=(a,b0,b0), v_2=(b0,a,b0),
v_3=(b0,b0,a), a^2+2b0^2=1, a!=b0; the separate symbol b0 avoids
confusion with the coupling vector b. Both orientation branches of a fixed
rho=2ab0+b0^2 are retained. The supplied scalar theorem gives the compact
auxiliary curve X_s=grad F through F=1, with k>=C0>0. Along that curve,
b=zeta=0 and H=nu I2. A possible zero of nu has common upper coefficients
M a_i and d_i=0, and the derivative of g_i-g_j in s is nonzero.

## 2. A regular metric using derivatives of the complete gradients

Define present-state fields and their Gram by

    bar g=(g1+g2+g3)/3=grad F,
    T_i=D_X g_i[bar g], Theta_ij=<T_i,T_j>/3,
    K_sigma=K+sigma Theta, sigma>0.                    (3)

The coefficient sigma is fixed; it is unrelated to the initializer's ridge.
There is no new evolving field: every T_i is obtained by differentiating the
displayed finite-feature formulas in the declared current direction bar g.
These are derivatives along bounded characteristic directions. No assertion
of unrestricted second Nemytskii differentiability on an L2 ball is needed.

**Regularity on every symmetric reference segment.** The matrix K_sigma is
positive definite at every point of the compact initialized auxiliary segment
through its fitting endpoint, for every admitted symmetric seed and every
fixed sigma>0. Consequently it has a strictly positive minimum eigenvalue on
that segment and remains positive in a state/data neighborhood of the segment.

To prove this, permutation symmetry makes both K and Theta scalar on the
mean and transverse representations. The mean eigenvalue of K is k>=C0.
If nu>0, the transverse directions are already positive in K. At a zero of
nu, T_i=(g_i)_s, and

    E^T Theta E=omega I2,
    omega=||T_1-T_2||^2/6>0.                           (4)

The strict inequality is precisely the positive quadratic-contact result
for the complete gradients, including their row blocks. Thus every direction
is positive in K_sigma. Continuity and compactness give its minimum. The
fields T_i are continuous in the physical state metric on bounded c,M sets:
all evaluated row directions in (3) are bounded by the bounded dictionaries,
finite M and ||c||2, and subtracting the finite products uses the Lipschitz
gate bounds. This also proves the stated neighborhood property.

This construction removes a representation singularity which an inverse of
K itself cannot remove. It does not say that K_sigma is the physical tangent
Gram, or that the physical flow dissipates in all of its directions.

## 3. A correction derived from the first flow response

Where k>0, define

    S=H-bb^T/k, chi=zeta+e b/k,
    Gamma=E^T K_sigma E, R=Gamma^(-1).                 (5)

Near a symmetric reference segment these quantities are regular by section 2.
The Schur complement S is positive semidefinite because K is a Gram, even
when it is singular. From (2), differentiation gives the exact cancellation

    chi_dot=-2S zeta+e (b/k)_dot.                      (6)

Indeed differentiating e b/k contributes -2eb, which cancels the +2eb in
zeta_dot; its remaining scalar coupling is 2bb^T zeta/k. This is a
calculation in the actual physical equations, not merely a Hessian expansion
of the old scalar potential.

For a smooth input perturbation with common prescribed initialization,
write the finite-time first responses zeta=epsilon zeta1+O(epsilon^2),
b=epsilon b1+O(epsilon^2). At the symmetric seed,

    (zeta1)_dot=2e b1-2nu zeta1,
    chi1=zeta1+e b1/k,
    (chi1)_dot=-2nu zeta1+e (b1/k)_dot.                (7)

All b1 terms include the common-state flow response and the direct input
response of all three gradient blocks. Equation (7) identifies the cross
term required to remove the direct mean forcing. The derivative of b1/k is
not zero and has no sign asserted here.

For the actual data let C0=E2[((H_1(0)+H_2(0)+H_3(0))/3)^2], and put

    D=C0+F^2, W=1+C0(1+q)/D, Phi0=W L,
    Phi_reg=Phi0+kappa chi^T R chi, kappa>0.           (8)

This is an explicit current-state potential, with fixed initialized C0 and
chosen positive sigma,kappa. In the neighborhood described in section 2,

    L<=Phi_reg<=C L                                  (9)

for some finite local C: W and R are bounded and chi is a bounded linear
function of (-e,zeta). It vanishes at every fitted state in that neighborhood.
Along each symmetric seed chi=0, so it agrees exactly with the proved Phi0.
At initialization its correction is the computable number
kappa b(0)^T R(0)b(0)/k(0)^2; it need not vanish for nonsymmetric data.

The leading new term on any fixed horizon is

    kappa epsilon^2 |zeta1+e b1/k|^2/(nu+sigma omega)
                       +O_T(epsilon^3).              (10)

Here omega is the transverse eigenvalue of Theta on the seed. The denominator
remains positive even when nu=0. Thus the old disagreement/coupling square
has a regular version tied to the actual gradient-recovery mechanism.

## 4. The full physical derivative, with no missing metric terms

The complete derivative of the old factor and loss is

    W_dot=4C0[(eF-V)/D-(1+q)F(ek-b^T zeta)/D^2],
    (Phi0)_dot=-4W(e^2k-2e b^T zeta+zeta^T H zeta)
                         +L W_dot.                   (11)

The inverse derivative R_dot=-R Gamma_dot R and (6) give

    (Phi_reg)_dot=(Phi0)_dot
       -4kappa chi^T R S zeta
       +2kappa e chi^T R (b/k)_dot
       -kappa chi^T R Gamma_dot R chi.                (12)

Every term is a present-state directional derivative along X_dot in (1).
For completeness,

    (g_i)_dot=D_Xg_i[X_dot],
    bar g_dot=sum_i D_Xg_i[X_dot]/3,
    (T_i)_dot=D_X^2g_i[X_dot,bar g]+D_Xg_i[bar g_dot],
    Theta_ij_dot=(<(T_i)_dot,T_j>+<T_i,(T_j)_dot>)/3,
    Gamma_dot=E^T(K_dot+sigma Theta_dot)E.              (13)

The first and second derivatives in (13) can be evaluated by finite product
rules in the displayed canonical fields; they use the actual M transpose.
Bounded characteristic velocities and bounded activation derivatives justify
the population differentiations. The formulas are valid also at nu=0.

Neither the product R S nor the last two terms in (12) have a proved favorable
sign. In particular S>=0 and R>0 do not by themselves make chi^T R S zeta
nonnegative. At a symmetric singular fitting endpoint, S=0 and the physical
velocity is zero, so both Gamma_dot and (b/k)_dot are zero. The regular metric
therefore supplies no missing transverse damping at that point.

Here is the exact narrow obstruction. For any finite differentiable positive
residual metric P(X), the residual-quadratic expression r^T P r has derivative

    -2r^T(KP+PK)r+r^T P_dot r.                        (14)

At a stationary state P_dot=0. If Kv=0 for v!=0, then
v^T(KP+PK)v=0, while v^TPv>0. Hence no matrix certificate

    2(KP+PK)-P_dot >= lambda P, lambda>0               (15)

can hold there. This applies to the regularized construction, including its
mean/disagreement completion. It only rules out this sufficient
all-residual matrix certificate. An arbitrary test vector v need not be an
initialized residual, so (15)'s failure is **not** a counterexample to
initialized-trajectory exponential decay or to Phi_reg itself.

## 5. An algebraic fitting readout at collapsed upper features

A second route exploits readout linearity without an endpoint oracle. Work
in the active three-dimensional upper feature coordinates; their mark law has
positive density on an open cube. For any current nonzero coefficient vector
zbar, write

    z=b2^T zbar, h=tanh(z), s=sech^2(z),
    A=E2[b2 b2^T s^2], v=E2[b2 s h],
    h_perp=h-s b2^T A^(-1)v,
    Delta=E2 h_perp^2,
    c_dagger(zbar)=h_perp/Delta.                       (16)

The matrix A is positive definite: for any nonzero vector q, the linear
form b2^Tq is nonzero on an open positive-measure set and s>0. Also Delta>0.
If Delta were zero, continuity and the positive mark density would imply
tanh(b2^Tzbar)=sech^2(b2^Tzbar)b2^Tq on the entire open cube. Dividing by
the positive gate gives sinh(2b2^Tzbar)/2=b2^Tq. Restrict to a line through
zero on which b2^Tzbar is nonzero; its third derivative at zero contradicts
the linear right side. Thus (16) is well defined and smooth for zbar!=0.

The projection calculation gives exactly

    E2[c_dagger h]=1,
    E2[b2 c_dagger s]=0.                              (17)

Consequently c_dagger fits three identical upper fields and has zero backward
coefficient there. This is an explicit function of present coefficients and
the declared fixed upper law. A singular fitting readout is therefore
algebraically compatible with readout linearity; its impossibility cannot be
inferred merely from target one and d=0.

Let zbar=(Ma_1+Ma_2+Ma_3)/3 in a region with zbar!=0, define c_dagger by
(16), and eta_i=E2[c_dagger H_i]-1. Taylor's theorem and (17) yield

    |eta_i|<=C |Ma_i-zbar|^2                           (18)

locally uniformly on bounded sets bounded away from zbar=0. Indeed the
constant term is one, the first derivative is the second identity in (17),
and the second tanh derivative and local norm of c_dagger are bounded.

For the comparison energy E_c=||c-c_dagger(zbar)||2^2, direct differentiation
of every factor gives

    (E_c)_dot=-4L+(4/3)sum_i (f_i-1)eta_i
       -2<c-c_dagger, D c_dagger(zbar)[zbar_dot]>.     (19)

To check the coefficient, <c-c_dagger,H_i>=(f_i-1)-eta_i and
c_dot=-(2/3)sum_i(f_i-1)H_i. The last term in (19) is indispensable.
The first two terms alone would suggest an attractive fitting estimate;
the moving hidden coefficient generates the uncontrolled last term.
Moreover E_c generally does not vanish at an arbitrary learned readout, so
it is not yet an admissible stand-alone fitting Lyapunov function. Multiplying
it by L repairs that zero set but only introduces a favorable term of order
L^2, while leaving the hidden derivative. No positive all-time rate follows
from this construction as it stands.

## 6. What the actual first flow response does at a singular endpoint

This section makes a conditional statement about an actual symmetric seed:
**assume its unit-amplitude fitting endpoint X_* is singular**. The supplied
work neither establishes nor excludes such a seed. Write the common upper
field there as h=tanh(z), z=b2^T zbar, zbar!=0. Then

    d_i=0, g_i=g=(0,h,0), k_*=||h||2^2>0,
    J_* a=n<g,a>, K_*=k_* nn^T.                       (20)

For any smooth curve of perturbed input triples with the same prescribed
initialization, let x1(t)=partial_epsilon X_epsilon(t)|0 and
r1(t)=partial_epsilon r_epsilon(t)|0. Then x1(t) is bounded for all physical
time and converges exponentially to a limit x1_infinity in ker J_*.
In particular

    lim_(t->infinity) r1(t)=0.                        (21)

This is a statement about the derivative of the initialized flow at each
finite t followed by t->infinity. It is not an interchange of epsilon->0
and the nonlinear training endpoint.

Here is a contained proof, including the input forcing. From the smooth
bounded auxiliary curve and k>=C0, e(t) decays exponentially and
X_0(t)-X_*=O(e(t)) in the bounded-increment characteristic norm. Write
the vector field as V(X,p)=-2J(X,p)^*r(X,p). Its state linearization is

    V_X=-2J^*J-2 sum_i r_i Hess_X r_i.

Along the seed this is A_*+B(t), where
A_*=-2g tensor g and ||B(t)||<=C e(t). For a direct input variation,

    partial_p f_i=d_i^T M partial_p a_i.               (22)

Thus it is zero at the singular endpoint, and is O(e(t)) along the seed.
Also V_p=-2(partial_p J)^*r-2J^*partial_p r=O(e(t)).
The first response therefore obeys

    (x1)_dot=(A_*+B(t))x1+b1(t),
    x1(0)=0, ||B(t)||+||b1(t)||<=C exp(-a t).          (23)

These bounds can be made in a weighted supremum space with norm

    ||v_w/(1+|G|)||infinity+||v_c||infinity+||v_M||F.

Input derivatives of tanh(w.v_i) cost at most one factor 1+|G|; all
remaining coefficients and directions of the base curve are bounded.
The bounded derivatives of tanh and the Gaussian moments justify the finite
population integrals and (23). No L-infinity continuity in the input itself
is used. The same estimates give (23) in the physical Hilbert metric.
The weighted norm is used to bound solutions of the response equations;
it is not a claim that the input-to-state map is differentiable in that
weighted supremum norm. The actual finite-time derivatives are identified
in L2 by difference quotients, bounded gate derivatives and Gaussian
domination, as in the supplied finite-horizon response calculation.

Let P a=g<g,a>/k_* and Q=I-P. The exact semigroup of A_* is
Q+exp(-2k_*t)P, bounded in the stated weighted norm. Variation of constants
and the elementary integrating-factor bound, using integral ||B||<infinity,
give sup_t||x1(t)||<infinity. Then Q(x1)_dot=Q(Bx1+b1) is exponentially
integrable; its tail proves convergence of Qx1. The scalar equation for Px1
has stable coefficient -2k_* and exponentially decaying forcing, so Px1
tends to zero exponentially (reduce the rate if the two exponents agree).
This proves the asserted limit and rate. Finally

    r1=J x1+partial_p r,

and (20), (22), and Px1_infinity=0 imply (21).

Thus the finite integral of the homogeneous transverse damping, by itself,
does not imply survival of actual first-order initialized disagreement. The
direct spatial output derivative vanishes at the same double collapse, and
the coupled state response enforces its cancellation.

## 7. The second flow response exposes an explicit quadratic source

Under the same conditional singular-endpoint hypothesis, write

    x1_infinity=(omega,gamma,N),

in row/readout/matrix order, and let epsilon_i be the first derivative of
the signed input v_i. Evaluate all following unmarked fields at X_* and
the seed inputs. Define the coefficient first variations

    ell_i=N a_i+M E1[b1 sech^2(w.v_i)
                              (omega.v_i+w.epsilon_i)],
    p_gamma=E2[b2 gamma sech^2(z)],
    T_c=E2[b2 b2^T c tanh''(z)],
    q_i=2p_gamma^T ell_i+ell_i^T T_c ell_i.             (24)

These expressions retain both hidden blocks and the readout/hidden cross
term. Let x2(t)=partial_epsilon^2X_epsilon(t)|0 and similarly r2(t).
Then x2(t) is bounded and converges, and

    lim_(t->infinity) r2(t)
       =(I-nn^T)(q_1,q_2,q_3)^T/sqrt(3).              (25)

To derive the source, the first variation of z_i is b2^T ell_i. Twice
differentiating f_i=E2[c tanh(z_i)] gives at the endpoint

    (f_i)''=<c'',h>+2<gamma,sech^2(z)b2^T ell_i>
              +<c,tanh''(z)(b2^T ell_i)^2>
              +<c,sech^2(z)(z_i)''>.

The last term is zero because (z_i)'' is a b2-linear field and
E2[b2 c sech^2(z)]=0. This removes every contribution of the second
hidden response and the second sphere-chart derivative. The first term is
common to all i. The remaining two terms are exactly q_i in (24).

For completeness the limit of x2 follows from the actual second variational
equation, rather than being assumed. Differentiating V=-2J^*r twice along
the perturbed flow gives

    (x2)_dot=-2J^*r2-4(J1)^*r1-2(J2)^*r.              (26)

Here J2 contains its term linear in x2. Moving that term to the linear
part yields the same operator A_*+B(t) as in (23). The remaining source
converges exponentially to -2J_*^*q/sqrt(3), because r and r1 tend to
zero exponentially, the base converges, and x1 converges. The second
direction costs at most (1+|G|)^2, so the identical estimates work in the
corresponding weighted space. Choose a constant multiple of g that cancels
this limiting source, and subtract it from x2. The equation then has an
integrable perturbation and exponentially decaying forcing exactly as (23).
The P/Q argument proves convergence and gives

    J_* x2_infinity=-nn^T q/sqrt(3),

which proves (25). No differentiability of a trajectory-selected endpoint
map is asserted.

There is no established reason for the centered quadratic vector in (25)
to vanish for every input direction. Nor is nonvanishing proved for any
actual canonical seed here. Formula (25) is therefore a concrete unresolved
test, not a counterexample. If nonzero, it would identify a discrepancy in
the second iterated flow-response limit; further estimates would still be
needed to conclude anything about actual perturbed all-time trajectories.

## 8. Status and exact missing estimates

| Statement | Status | Boundary |
|---|---|---|
| K+sigma Theta is uniformly positive on each complete symmetric reference segment | Proved from the supplied quadratic-contact theorem | It is an auxiliary metric, not physical tangent coercivity |
| chi=zeta+e b/k cancels the direct mean forcing | Exact physical-flow identity | The derivative of b/k remains |
| Phi_reg is present-state, regular at reference rank losses, nonnegative and locally comparable with loss | Proved | No all-time sign for (12) established off symmetry |
| Uniform matrix certificate for any finite positive residual metric at a stationary singular tangent | Impossible in the stated all-residual sense | No initialized-trajectory counterexample follows |
| Algebraic c_dagger fits a collapsed upper field and kills its first derivatives | Proved current-state construction | Moving hidden term in (19) is uncontrolled |
| First initialized output response tends to zero; the first state response converges to a possibly nonzero neutral limit | Proved conditional on a singular fitting seed existing | Iterated response limit, not uniform nonlinear perturbation stability |
| Transverse second flow-response limit is the quadratic vector (25) | Proved under the same condition | Its value/sign for canonical seed directions is unresolved |
| New unit-amplitude range away from the previously proved regular endpoints | Not obtained | No weaker amplitude, ambient state, frozen kernel or future metric is substituted |

To turn (8) into the requested broader theorem, one must bound the right side
of (12) by a negative multiple of Phi_reg **on the initialized perturbed
trajectories**, or establish a different nonlinear tail estimate controlling
the quadratic source (24). Positive definiteness of the regularized metric
is insufficient. The bounded fitting comparison (16) supplies a second
concrete possible correction, but (19) identifies its exact missing
hidden-organization estimate. These are substantive unresolved signs and
rates; neither is supplied by c-linearity or by a second derivative of the
old potential alone.
