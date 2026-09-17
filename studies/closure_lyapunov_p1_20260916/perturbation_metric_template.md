# A current-state correction metric and its perturbative form

2026-09-16. Root derivation after the independent mode route was frozen.
This note uses its complete exact mode identities, the current canonical
closure equations and the frozen three-coordinate theorem. It is an exact
geometric template with conditional decay statements, not a new generic
convergence theorem. No experiment or future-defined coefficient is used.

## 1. Current full tangent geometry

Let m_i=y_i f(u_i) for three equally weighted unit labels, g_i=grad m_i
in the full physical state metric, and K_ij=<g_i,g_j>/3. This note's K
includes the probability factor; perturbation_modes.md uses G=3K.
Let

    r=(m-1)/sqrt(3), L=|r|^2,
    J h=(<g_i,h>/sqrt(3))_i.

Then K=J J* and the exact residual equation is

    r_dot=-2K r.                                             (1)

K includes all three positive Gram contributions of c,M,w as displayed
in perturbation_lower_balance.md (1), with label conjugation and division
by three. In particular it is not a frozen or readout-only kernel.

On the region where K is positive definite, define

    E(S)=r^T K^(-1)r.                                       (2)

This has a direct physical interpretation: it is the least squared norm
of an infinitesimal parameter correction h solving J h=-r. Indeed
h0=-J* K^(-1)r solves the equation and has norm squared (2).
Any other solution is h0+k with Jk=0, and
<h0,k>=-<K^(-1)r,Jk>=0. Pythagoras proves the minimum.
This is a local linearized correction cost at the current state, not the
distance to a supplied fitted endpoint and not a global nonlinear state
distance. The definition uses no future state.

## 2. What symmetry-breaking adds to the form

Let n=(1,1,1)/sqrt(3) and take any fixed real 3-by-2 matrix V with
V^T V=I and V^T n=0. Define

    F=(m1+m2+m3)/3, e=1-F,
    zeta=V^T(m-F*1)/sqrt(3),
    k=n^T K n, b=V^T K n, H=V^T K V.

Then r has coordinates (-e,zeta), and L=e^2+|zeta|^2. The tangent
matrix in these coordinates is [[k,b^T],[b,H]]. If K>0, its Schur
complement S=H-bb^T/k is positive definite. Direct block elimination
gives the exact identity

    E=e^2/k+(zeta+e b/k)^T S^(-1)(zeta+e b/k).                 (3)

For example, solve k x+b^T y=-e and b x+H y=zeta. Eliminating x
gives S y=zeta+e b/k; substitution in (-e,zeta).(x,y) yields (3).
This also proves the positivity claim about S by minimizing the block
quadratic form in its first coordinate.

On the symmetric trajectory, b=0, zeta=0 and H=nu I_2 by input
permutation invariance. Thus only e^2/k is visible. The other directions
exist even at symmetry, but that trajectory does not excite them.

For an epsilon perturbation on a fixed horizon, the exact mode estimates
give b,zeta=O_T(epsilon). Provided the reference transverse coefficient
nu is positive and bounded below on that compact interval, expansion of
the current-state expression (3) gives

    E=e^2/k + (1/nu)|zeta+e b/k|^2 + O_T(epsilon^3).          (4)

The use of CURRENT e and k in the first term and inside the square is
intentional: changes of those mean quantities can be first order. The
three additional leading contributions are

    |zeta|^2/nu,
    2e b^T zeta/(k nu),
    e^2|b|^2/(k^2 nu).                                     (5)

The error claim follows by K-K0=O_T(epsilon), k bounded away from
zero, S=nu I+O_T(epsilon), and the inverse identity
S^(-1)-(nu I)^(-1)=S^(-1)(nu I-S)/nu. Thus this inverse difference
is O_T(epsilon), multiplied in (3) by a vector of norm O_T(epsilon)
on both sides. No differentiability in epsilon is needed for that
bounded remainder once these estimates hold. A full Taylor coefficient
can additionally use the differentiable parameter family of the mode note.

The cross term in (5) is sign-indefinite. It is accompanied by the two
positive terms completing its square, so the correction in (3) stays
nonnegative. This gives a concrete mathematical form for the user's
suggestion: disagreement, coupling to mean progress, and a matching
positive compensation term. They are not determined by pairwise hidden
distances alone. k,b,H contain first-layer gates and the actual backward
couplings as well as the upper activations.

Equation (4) is local in the stated region. Positive initialization gives
such a region for a short interval. Initial rank alone does not show
nu stays positive through the fitted reference endpoint. No such
all-time assertion is used here.

## 3. The entire moving-metric derivative

The inverse derivative is

    (K^(-1))_dot=-K^(-1) K_dot K^(-1).

Using both residual derivatives from (1) gives EXACTLY

    E_dot=-4L-r^T K^(-1) K_dot K^(-1)r.                      (6)

All entries of K_dot are current-state derivatives obtained by
differentiating the explicit three blocks; perturbation_modes.md (19)
lists every field derivative. No reference trajectory is required to
evaluate (6). A frozen-kernel replacement would wrongly delete its last
term.

Here is one sufficient exponential condition that permits the kernel to
decrease in some directions and increase in others. Suppose on an actual
trajectory K>0, ||K||op<=Lambda for a declared finite Lambda, and

    K_dot >= lambda K - 4 K^2                               (7)

in the matrix order, for a fixed lambda>0. Substituting (7) between
K^(-1)r gives E_dot<=-lambda E. Also diagonalizing K gives

    L<=Lambda E,
    E(t)<=exp(-lambda(t-t0)) E(t0).                         (8)

Thus (7), WITH the upper bound, would produce exactly an exponential
current-state potential and loss comparison. It is a sufficient
estimate, not one proved for the nonlinear closure. In a direction with
instantaneous eigenvalue below lambda/4, (7) requires improvement of
that direction; larger eigenvalues may decrease. Uniform contraction
of hidden coordinates is nowhere required.

The upper bound is material: if K grows without control, its inverse
can make (2) shrink without comparable physical residual decay. On a
declared bounded c,M region it is available explicitly. Contraction of
the normalized feature maps gives

    ||g_i||^2<=1+||c||_2^2(1+||M||op^2),
    ||K||op<=tr K<=1+||c||_2^2(1+||M||op^2).                 (9)

For (9), |a_i|<=1, |d_i|<=||c||2 and
||q_i||2<=||M||op ||d_i|| bound the matrix and row gradients;
all gates and unit inputs have norm at most one. Label multiplication
does not change these norms. No future bound is supplied as a parameter.

A different sufficient hypothesis is K>=kappa I and
K_dot>=-theta K^2 with theta<4. Then (6) gives
E_dot<=-(4-theta)L<=-(4-theta)kappa E. This alternative illustrates
the role of a protected transverse direction but is likewise conditional.
Neither hypothesis has been proved on generic initialized trajectories.

## 4. Relation to the earlier potential

The previous potential multiplied loss by a normalized-readout factor.
Its proof used only the common residual direction. Formula (2) is a
different candidate geometry, not an asserted correction that inherits
the previous theorem automatically. It is useful because its missing
coupling terms and derivative are completely determined.

The independent mode route keeps the earlier potential and instead adds
an inverse-transverse-Gram cost. It gives a separate explicit block
matrix sufficient condition, including all derivatives of that weight.
Both constructions identify the same new obligations: transverse
conditioning, coupling between common and disagreement directions,
and the evolution of the full gradient geometry.

These calculations make the perturbation proposal meaningful: they
turn an unspecified search for extra hidden alignment penalties into
specified quadratic and forward/backward terms. They do not establish
that either candidate decays for arbitrary geometry, or that a small
finite-time input perturbation stays small throughout training.
