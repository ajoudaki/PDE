# Gaussian-gate auxiliary identities — root draft, not independently audited

2026-09-06. These are exact initial-Gaussian and prescribed-control
identities for phi(z)=1+epsilon F(z), F(z)=integral_0^z exp(-v²)dv,
epsilon=1/10. They are not a global training proof and have not yet
been submitted to an isolated reviewer. No external theorem is used.

## Initial covariance and the signed scalar integrals

Let (X,Y) be a centered Gaussian pair of common variance q>0 and
covariance c in [-q,q]. Define

  B_q(c)=E[exp(-X²-Y²)],
  J_q(c)=-E[F(Y)F''(X)],
  D_q=B_q(q)-J_q(q), T_q(c)=B_q(c)-J_q(c).

Orthogonally diagonalizing its covariance and completing the scalar
Gaussian square gives, also at singular covariance,

  B_q(c)=[(1+2q)^2-4c^2]^(-1/2).

Gaussian integration by parts in X, with its covariance contribution
from Y retained, gives

  E[X exp(-X²)F(Y)]
    =-2q E[X exp(-X²)F(Y)]+c E[exp(-X²-Y²)].

The identity holds first for a nondegenerate pair by differentiating
its Gaussian density and integrating by parts; all functions and
their first derivatives are bounded. A common-Gaussian coupling and
bounded convergence extend it to the two endpoints. Since
F''(X)=-2X exp(-X²), it follows that

  J_q(c)=[2c/(1+2q)]B_q(c),
  D_q=1/[(1+2q)sqrt(1+4q)]>0,
  T_q(c)=(1/(1+2q))sqrt[(1+2q-2c)/(1+2q+2c)].

Thus B is even and positive, J odd, and T strictly decreases on the
entire admissible interval, with T(q)=D and T(c)>D for c<q.
These are the same scalar inequalities used in the arctan initial
signed-cone calculation, now with explicit formulas. That observation
does not itself certify any new finite-law or trained-law theorem.

For the initial feature covariance, on |c|<q differentiating the
two-dimensional Gaussian density with respect to c gives
partial_c density=partial_X partial_Y density. This can be checked
directly in its explicit density with inverse covariance
(q²-c²)^-1[[q,-c],[-c,q]]. Two integrations by parts therefore yield

  d/dc E[F(X)F(Y)]=B_q(c).

The parameter derivative is dominated by Gaussian tails on every
closed interior covariance subinterval. The boundary terms vanish
because F and its derivatives are bounded. At c=0 the expectation
is zero by independence and oddness. Integrating and then taking
endpoint limits by bounded convergence gives

  E[F(X)F(Y)]=(1/2)arcsin[2c/(1+2q)],
  E[phi(X)phi(Y)]=1+(epsilon²/2)arcsin[2c/(1+2q)].

The arcsine argument remains strictly between -1 and 1 even at
c=+-q; no branch ambiguity or derivative singularity is present.
These formulas specify the initial variance/covariance recursion
by substituting c=q on the diagonal and the previous-layer covariance
off the diagonal, starting from q=1,c=rho. They do not assert that
trained forward fields remain Gaussian.

## A common weighted area form, not a Killing metric or probability law

Fix |rho|<1, C=[[1,rho],[rho,1]], and any prescribed integrable
control u(t), now allowing arbitrary changing signs. For

  z'=v(t,z)=C diag(phi'(z1),phi'(z2))u(t),
  E(z)=z^T C^-1 z,

the pointwise divergence in the two state coordinates is

  div_z v=sum_a phi''(z_a)u_a
         =-2 sum_a z_a phi'(z_a)u_a
         =-grad E(z) dot v(t,z).

The first equality uses C_aa=1; no off-diagonal term belongs in a
divergence of component a with respect to z_a. Along a solution,
the determinant of its initial-state Jacobian J therefore satisfies

  det J(t)=exp(E(z0)-E(z(t))).

For a direct derivation, its variational equation J'=D_zv J has
invertible J: solve the backward linear equation for its inverse on
the finite interval. Differentiation of the determinant polynomial,
or the product rule for the two columns, gives
(det J)'=(div v)det J. Its integrating factor and the preceding
identity give the display, also for integrable time dependence.

Equivalently, the density exp(E(z)) times Lebesgue area is invariant
under these prescribed flows. This is NOT a Gaussian probability
measure; its total mass is infinite and its density grows at infinity.
It bounds a determinant, not the largest singular value. In particular,
area conservation permits exponential expansion in one tangent
direction and contraction in the other. It does not contradict the
earlier no-common-Killing-metric result or prove full response control.
No extension to an invariant distribution of the trained network is
asserted.
