# Cancelling the moving-geometry defect by current-state corrections

2026-09-16. Root constructive candidate. This builds new correction terms
and proves their local flow inequality. It does not prove global capture
from initialization for the whole rho family. No experiment or promotion.

Scientific inputs: exact canonical equations in docs/observable_p1.md and
docs/global_nonlinear.md C.4.7.9/C.4.7.10, the complete same-study
perturbation_modes.md and perturbation_metric_template.md, and the
previously checked finite-horizon regularity/endpoint results. The
construction below is derived independently of the current parallel
routes. No future curve, oracle endpoint or extra evolving state is used.

## 1. Canonical gradients and the defect to cancel

For fixed signed unit inputs v_i=y_i u_i, i=1,2,3, let m_i=f(v_i), with
all signed targets one. Keep the canonical residual f_i-y_i unchanged;
introduce the distinct normalized signed error xi_i=(m_i-1)/sqrt(3).
Thus L=|xi|^2 is exactly the prescribed unhalved mean square loss.

Write X=(w,c,M) on the frozen mark spaces and use its physical Hilbert
metric. Define j_i=grad_X m_i/sqrt(3). Its three blocks are

    j_i=(sech^2(w.v_i)(b1^T M^T d_i)v_i, H_i, d_i a_i^T)/sqrt(3),
    a_i=E1[b1 tanh(w.v_i)], H_i=tanh(b2^T M a_i),
    d_i=E2[b2 c sech^2(b2^T M a_i)].

No matrix is frozen or transposed independently. Put K_ij=<j_i,j_j>.
The exact gradient flow and normalized prediction equation are

    X'=-2 sum_i xi_i j_i,   xi'=-2K xi,
    L'=-4 xi^T K xi.                                      (1)

On K>0 the local squared physical correction cost is

    p2(X,z)=z^T K(X)^(-1) z,                              (2)

where z in R^3 is an independent formal variable. The actual cost is
p2(X,xi(X)). The artificial z is used solely to specify finite polynomial
coefficients. It is not an additional closure coordinate.

The problem with (2) was the moving-metric term, not the fixed-metric
dissipation. Indeed

    d p2(X,xi)/dt = -4L
           +2 sum_i xi_i xi^T K^(-1)(D_{j_i}K)K^(-1)xi.   (3)

Here D_{j_i}K is the directional derivative of the current Gram in the
current physical direction j_i. It includes derivatives of both hidden
layers, the readout, and the actual transpose. The last term is a cubic
polynomial in xi with current-state coefficients, with no fixed sign.

## 2. A finite algebraic correction rule

For a homogeneous polynomial p(X,z), define two operators:

    (A_K p)(X,z)=2(Kz).grad_z p(X,z),
    (B p)(X,z)=-2 sum_i z_i D_{j_i}p(X,z),                 (4)

where the derivatives in B hold z fixed. If p has degree m in z, A_K p
has degree m and Bp has degree m+1. The full chain rule along (1) is

    d p(X,xi(X))/dt = (B p-A_K p)(X,xi).                  (5)

For K>0 and m>=1, A_K is invertible on the finite-dimensional space of
homogeneous degree-m polynomials. To see this without a time integral, diagonalize
K with positive eigenvalues k1,k2,k3. On z1^alpha1 z2^alpha2 z3^alpha3,
where sum alpha_i=m, A_K acts by multiplication by

    2(alpha1 k1+alpha2 k2+alpha3 k3)>0.                    (6)

Hence its inverse is ordinary finite linear algebra. In the invariant
symmetric-tensor representation, if K>=mu I, its inverse operator norm
is at most 1/(2m mu). Differentiation of this inverse is defined by the
finite identity D(A^-1)=-A^-1(DA)A^-1, with no eigenvector derivative
ambiguity at repeated eigenvalues.

Now DEFINE, successively,

    p3=A_K^(-1) Bp2,
    p4=A_K^(-1) Bp3.                                     (7)

They require solving only systems on symmetric tensors of orders three
and four, with respectively 10 and 15 coefficients for three samples.
Their inputs are K and its derivatives in the current j_i directions.
Their provenance is entirely the current state and fixed data.

The proposed corrected geometric cost is

    E_corr(X)=p2(X,xi)+p3(X,xi)+p4(X,xi).                  (8)

Substitution of (7) into (5) cancels the cubic and quartic defects EXACTLY:

    E_corr'=-4L+(B p4)(X,xi).                             (9)

The remaining expression Bp4 is homogeneous of degree five in the current
error. No smallness, frozen feature assumption, or discarded metric
derivative enters this identity. In particular p4 includes derivatives
of the coefficients of p3 and of the directions j_i themselves. Keeping
only D K while dropping D j_i would produce a different, incorrect p4.

This differs from merely computing the Hessian of an existing potential:
the new cubic term is DEFINED to cancel the old flow defect, and the new
quartic term is DEFINED to cancel the defect created by that correction.

## 3. Rigorous local decay and loss comparison

Use Euclidean Frobenius norms on symmetric coefficient tensors so
|p_m(X,z)|<=a_m |z|^m whenever its tensor has norm at most a_m.
Suppose a state region has uniform bounds

    mu I<=K<=Lambda I,
    ||p3||tensor<=a3, ||p4||tensor<=a4,
    ||Bp4||tensor<=a5,                                    (10)

where 0<mu<=Lambda<infinity. These are bounds on explicit current-state
objects, not a differential inequality to be assumed for an unknown
new metric. They hold locally about every regular bounded state; their
justification for the closure is given in section 4.

Choose ell>0 such that

    a3 sqrt(ell)+a4 ell<=1/(2 Lambda),
    a5 ell^(3/2)<=2.                                      (11)

Zero constants impose no restriction. For L<=ell,

    (1/2)p2<=E_corr<=(3/2)p2.                             (12)

Indeed |p3+p4|<=(a3 sqrt(L)+a4 L)L<=L/(2Lambda)<=p2/2.
Equation (9) and (11) also give E_corr'<=-2L.

For any fixed kappa>0 set the corrected potential

    Phi_corr=L+kappa E_corr.                              (13)

Then on this region

    L<=Phi_corr<=[1+3kappa/(2mu)]L,
    Phi_corr'<=-(4mu+2kappa)L<=-lambda Phi_corr,
    lambda=(4mu+2kappa)/[1+3kappa/(2mu)]>0.                 (14)

This is a proved flow inequality with all geometric derivatives present.
It needs no assumed sign of K', no assumed matrix Riccati inequality,
and no requirement that every hidden coordinate contract.

## 4. Regularity and uniform bounds for the exact closure

The canonical characteristic state uses bounded w-g and c, and finite M.
At fixed inputs all j_i have bounded row/readout components: dictionary
marks are bounded, tanh derivatives are bounded, |a_i|<=1,
|d_i|<=||c||2, and |b1^T M^T d_i|<=B1 ||M||op ||c||2.

All directional derivatives needed above can therefore be calculated in
the Banach space of bounded row increments, bounded readout increments
and finite matrices. The canonical fields are smooth there: repeated
product rules use bounded derivatives of tanh, bounded direction fields,
bounded dictionary columns, and probability integrals. The frozen Gaussian
g appears inside bounded gates and is not differentiated in these fixed-
data state directions. The derivatives defining Bp4 are finite-order
compositions of those operations, so there is no infinite hierarchy of
state variables in (13).

More precisely, bounds for these coefficients can use only an upper bound
on ||c||2 and ||M||, the fixed feature envelopes, and mu^(-1), Lambda.
There is no need for a row supremum bound in these coefficient estimates:
the differentiated row directions j_i and their iterated directional
derivatives have uniform bounds depending on the same quantities, and
every occurrence of the base c is linear inside a population integral
and is controlled by Cauchy--Schwarz. Induction through the finite product
rules proves the assertion. K and these coefficients are continuous in
the physical state metric on such bounded regions: differences of lower
gates are bounded by a constant times the L2 row difference, integrated
against bounded remaining factors; upper contractions and c differences
are controlled by Cauchy--Schwarz. Thus a sufficiently small physical
ball about any K>0 state supplies (10).

This reasoning does not assert that the full Nemytskii vector field has
arbitrary Frechet derivatives on an unrestricted L2 ball. The derivatives
used in (4) are in the displayed bounded directions, where the stronger
characteristic calculus applies. For changes of the fixed inputs, the
Gaussian-weighted response argument in sphere_second_variation.md
supplies the required finite-horizon input continuity.

## 5. An all-time certificate at a current state

Suppose a current state X0 has a physical ball of radius R on which (10)
holds, and L(X0)<=ell for a threshold ell satisfying (11), with

    sqrt(L(X0)/mu)<R.                                    (15)

Then (13)--(14) hold for every future time, and the state converges to a
fitting limit. This uses no supplied fitting endpoint.

Proof: if L(X0)=0, the vector field vanishes and uniqueness gives the
stationary fitting solution. Otherwise, up to a first exit and while the
loss is positive, (1) gives L'<=-4mu L and

    -d sqrt(L)/dt >= sqrt(mu) ||X'||.

If loss reaches zero, the same stationarity argument applies thereafter.
Integrating bounds the entire displacement by sqrt(L(X0)/mu)<R, so no
first exit exists. Global finite-time existence handles continuation.
Loss decreases, so its thresholds (11) persist. Equation (14) integrates
to Phi_corr(t)<=exp(-lambda t)Phi_corr(0), taking this current state as
time zero. Finite physical length gives a strong population-L2/Frobenius
limit; continuity and vanishing loss show that it fits. End of proof.

The certificate is constructive once upper bounds on the displayed
finite derivatives on a present-state ball have been obtained by the
explicit gate bounds. It is a genuine all-time theorem from a CURRENT
state, not a statement conditioned on the unknown future metric.
It does not show that the prescribed initialized broad-rho perturbations
enter such a ball. Previously proved regular-endpoint families do enter
it eventually, but that implication does not enlarge those families.

## 6. First/second input variations and exact scope

The physical correction p2 already contains the exact completed square

    e^2/k+(zeta+e b/k)^T(H-bb^T/k)^(-1)(zeta+e b/k),

using the mean/disagreement blocks of the CURRENT full K. Thus both the
first-layer/backward coupling and all independent input directions enter
before adding (7). The role of (7) is to remove the bad TIME derivative
of that changing correction geometry.

Near a regular fitted state, independent input perturbations and a smooth
state perturbation give xi=O(|epsilon|). Equation (9) then has an
O(|epsilon|^5) defect, rather than the O(|epsilon|^3) defect of p2.
This statement includes mixed input directions through its uniform
homogeneous polynomial form. The construction is an expansion in current
residual, not a claim that the residual is small at initialization or
uniformly small along the earlier nonfitted reference segment. At a
nonfitted symmetric reference xi is not O(epsilon); that different
perturbation ordering must not be silently substituted.

The coefficients contain inverse eigenvalues of K. They therefore do not
resolve a possible double-collapse endpoint of the broad rho family.
Increasing the correction order alone does not remove this singularity.
The new result is an actual curvature-corrected local potential, with
exact cancellation and an all-time current-state certificate. Global
initialized capture, a formula regular at all singular reached states,
and the broad unit-label perturbation theorem remain open.

## 7. One-coordinate algebra check

For a scalar residual x with x'=-2k(x)x, the same rule gives

    p2=x^2/k,
    p3=x^3 k_x/(3k^2),
    p4=x^4[k_x^2/(6k^3)-k_xx/(12k^2)].

Direct differentiation cancels all terms of degrees three and four and
leaves -4x^2 plus a degree-five coefficient. This check fixes the factors
2, 6 and 8 in (4), (6), and (7). It is an algebraic check of the construction,
not a replacement model or evidence for global closure convergence.
