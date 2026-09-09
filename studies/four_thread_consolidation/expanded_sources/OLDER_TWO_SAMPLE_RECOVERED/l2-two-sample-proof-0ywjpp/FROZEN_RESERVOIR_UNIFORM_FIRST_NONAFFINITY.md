# Uniform first-activation nonaffinity from the unchanged Gaussian subset

Root candidate, 2026-09-06. Not independently audited as this document.
This is NOT a nonlazy or population-existence theorem. Its population
statement is conditional only on a supplied measurable family of paths
preserving the stated initial subset. Its finite-width statement is
unconditional for the specified raw GF/GD wherever the parameters exist.
The Gaussian-moment argument below is self-contained. It is inspired by
an optional strengthening in a separate audit, not invoked from it.

Fix R>0 and a smooth even p>=0, positive on (-R,R), zero outside
[-R,R]. Define phi_1(z)=integral_0^z p and B=integral_0^R p>0.
Thus phi_1(z)=B sign(z) when |z|>=R. Inputs x_1,x_2 in R^d satisfy
||x_a||^2=d, x_1^T x_2/d=rho in[-1,1). First rows W_i^(1)(0)
are independent N(0,I_d/d), so the pairs

    G_i=(W_i^(1)(0)x_1,W_i^(1)(0)x_2)

are iid centered Gaussian with covariance [[1,rho],[rho,1]].
Let F_i be the event |G_(1,i)|>=R and |G_(2,i)|>=R. For a generic
pair G write F for this event. For either fixed sample a put

    m=Pr(F), J_1=E[|G_a| 1_F], J_2=E[G_a^2 1_F],
    c_(rho,R)=B^2(m-J_1^2/J_2).                     (1)

The quantities are independent of a by exchange symmetry. They are
finite, m,J_2>0, and c_(rho,R)>0. For |rho|<1 the Gaussian pair has
a strictly positive density, so F has positive probability and |G_a|
is not constant on F. At rho=-1, G=(G_1,-G_1) and the same statements
hold on |G_1|>=R. Cauchy--Schwarz applied to |G_a|1_F and 1_F gives
J_1^2<=m J_2, with equality only if |G_a| is constant on F. This
proves strict positivity in (1), including the singular endpoint.

## Population statement and proof

Suppose Z_a(t) is any supplied family of measurable real variables
on the same initial-neuron probability space, and Z_a(t)=G_a on F
at every considered time (an almost-sure equality at each time suffices).
For every such t and every real slope u and intercept v,

    E[(phi_1(Z_a(t))-u Z_a(t)-v)^2]
       >= E[(B sign(G_a)-u G_a-v)^2 1_F]
       = B^2 m-2u B J_1+u^2 J_2+v^2 m.            (2)

Joint central symmetry of G and invariance of F give
E[G_a 1_F]=E[sign(G_a)1_F]=0; this proves the displayed expansion.
Minimizing its right side in u,v gives

    inf_(u,v in R) E[(phi_1(Z_a(t))-u Z_a(t)-v)^2]
          >=c_(rho,R)>0,                          (3)

with the SAME constant for every time. The inequality is meaningful
even if the full squared error is infinite for some coefficients. If
Z_a(t) is square integrable, it is the ordinary squared L2 affine-fit
gap. No Gaussianity of evolved fields or independence of evolved
neurons is asserted. No upper-layer property is used.

## Empirical statement and proof

Suppose the first preactivation paths obey z^(1)_(a,i)(t)=G_(a,i)
for every i in F_i. Define the finite restricted least-squares value

    c_(n,a)=inf_(u,v in R) (1/n)sum_(i:F_i)
                          (B sign(G_(a,i))-u G_(a,i)-v)^2.

Nonnegativity of the other rows gives, simultaneously at every time,

    inf_(u,v in R) (1/n)sum_i
         (phi_1(z^(1)_(a,i)(t))-u z^(1)_(a,i)(t)-v)^2
           >=c_(n,a).                            (4)

To identify this initialization-only bound, set

    M_(n,a)=(1/n)sum_i 1_(F_i)
                         [[G_(a,i)^2,G_(a,i)],[G_(a,i),1]],
    b_(n,a)=(B/n)sum_i 1_(F_i)(|G_(a,i)|,sign(G_(a,i)))^T,
    m_n=(1/n)sum_i 1_(F_i).

Every entry is an iid average of a variable of finite variance, since
Gaussian fourth moments are finite. Its variance is its one-row
variance divided by n; Chebyshev therefore proves jointly, in
probability for both samples,

    M_(n,a)->diag(J_2,m), b_(n,a)->(B J_1,0)^T, m_n->m.

The limiting matrix is positive definite. On an event with probability
tending to one, M_(n,a) is positive definite for both a; inversion is
continuous there by the explicit two-by-two inverse formula. Completing
the quadratic square yields on this event

    c_(n,a)=B^2 m_n-b_(n,a)^T M_(n,a)^(-1)b_(n,a)
               ->c_(rho,R)>0.                     (5)

There is no inverse taken on the complementary event. There c_(n,a)
retains its original nonnegative infimum definition. Equations (4)--(5)
show that with probability tending to one, BOTH empirical affine-fit
gaps are at least c_(rho,R)/2, simultaneously at every time for which
the frozen rows are preserved. This is not a claim at every fixed
small width; two-point empirical laws, for example, can be affine-fit
exactly. No rate uniform over rho approaching an endpoint is claimed.

## Why the subset is preserved in the actual network, and scope

In the canonical two-hidden-layer network use first activation phi_1,
second activation arctan, rescaled readout W^(3), prediction
f_a=(W^(3))^T h^(2)_a/n, and either labels (1,-1) or any fixed labels.
Define delta^(2)_a=W^(3)phi_2'(z^(2)_a) and
delta^(1)_a=p(z^(1)_a)(W^(2))^T delta^(2)_a.
The actual first GF rule is

    dot W_i^(1)=-(2/d)sum_a (f_a-y_a)delta^(1)_(a,i)x_a^T,

and raw GD uses its simultaneous increment with eta=n^-2. If F_i
holds, both initial p factors vanish. Holding that row at its initial
value makes its right-hand side zero regardless of the other parameters.
The finite-dimensional smooth GF vector field has local uniqueness,
so the row stays fixed throughout every continued solution. For raw
GD the same statement follows inductively at each node, and hence
on each raw affine segment. It does not require small steps, loss
descent, or bounds on other rows. Thus (4)--(5) apply to actual raw
GF/GD simultaneously over their entire existence intervals.

For any supplied population integral flow with the same pointwise
first rule and locally integrable controls, the identical fact follows
from the elementary bound |zdot|<=2 Lip(p)|control| |z-G| on F,
followed by the scalar integral Gronwall inequality. Hence (3) applies
to such a flow IF it exists; this argument does not construct it.

All nonaffinity in this estimate is already guaranteed by unchanged
neurons. It therefore does not establish nonlazy dynamics, any moving
positive mass, second-activation nonaffinity, global mean-field
existence, width convergence, or restart uniqueness. It only rules
out an effectively affine FIRST activation on the full neuron law
with a positive, time-uniform gap.
