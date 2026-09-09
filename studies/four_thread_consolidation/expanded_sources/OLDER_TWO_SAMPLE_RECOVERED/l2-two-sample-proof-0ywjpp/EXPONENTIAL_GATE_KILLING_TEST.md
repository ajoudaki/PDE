# Exponential gates do not restore the common-metric shortcut

Root draft, 2026-09-06. UNREVIEWED. This is a deterministic structural
test, not a statement about actual Gaussian training or its limit.
It closes a previously untested candidate for a common Killing metric.

Let 0<|rho|<1, C=[[1,rho],[rho,1]], v1=C e1, v2=C e2.
For a positive exponential gate p(z)=A exp(beta z), with A>0 and
beta!=0, consider X1=p(x)v1 and X2=p(y)v2. There is no smooth positive
definite Riemannian metric on any nonempty open set for which both
fields are Killing. No completeness or uniform metric bound is assumed.

It suffices to prove the case A=beta=1: the coordinate change
(x,y)->(beta x,beta y) and division of each pushed-forward field by the
same nonzero constant A beta preserve the existence of a common metric.
Fix an arbitrary point (x0,y0) in the open set and put a=exp(x0),
b=exp(y0). Rescale the two vector fields separately by a and b, which
also preserves the Killing property, and translate the point to zero.
Thus the relevant fields in a neighborhood of zero are exactly

    X1=exp(x)v1,     X2=exp(y)v2.

Use [X,Y]=DY X-DX Y. Direct differentiation gives, writing f=exp(x),
g=exp(y),

    Z=[X1,X2]=rho(f X2-g X1),
    V=[X1,Z]=rho((1+rho)f^2 X2-2rho f g X1).

If both X1,X2 are Killing, Z and V are Killing as well. For clarity,
this follows from the identity
L_[X,Y] metric=L_X L_Y metric-L_Y L_X metric: expand
(L_X metric)(U,V)=X(metric(U,V))-metric([X,U],V)
-metric(U,[X,V]); the terms cancel by the Jacobi identity for
commutators of differential operators. Constant linear combinations
of Killing fields remain Killing.

The following two such combinations vanish at zero:

    K=Z+rho(X1-X2),
    J=V-rho(1+rho)X2+2rho^2 X1.

Differentiating their coefficients in the fixed basis v1,v2 gives

    DK(0)=rho C [[0,-1],[1,0]],
    DJ(0)=rho C [[-2rho,-2rho],[2(1+rho),0]].

Consequently L=J-2(1+rho)K is Killing, L(0)=0, and

    DL(0)=rho C [[-2rho,2],[0,0]].

This matrix is nonzero and has determinant zero. This is impossible
for a Killing field vanishing at a point of a positive definite
two-dimensional metric. Indeed at such a point the Killing equation
reduces to D L^T M+M D L=0, where M is the positive definite metric
matrix. In an M-orthonormal basis D L is a real skew-symmetric matrix
[[0,-w],[w,0]]. Its determinant is w^2, so zero determinant forces it
to be zero. Similarity preserves determinant and whether a matrix is
zero. This contradicts the explicit derivative above.

The argument was made at an arbitrary point and proves the local
claim. For rho=0 a scalar regularizing coordinate works; at |rho|=1
the displayed fixed basis is singular. Neither boundary is covered
by the contradiction. For beta=0 the gate is constant and the
activation affine; the argument does not apply and a constant metric
works.

This rules out only a fixed common smooth positive metric that makes
both independently controlled first-layer fields isometries. It does
not rule out damping from the actual harmonic-top current response,
control-dependent metrics, trajectory estimates, or the desired
nonlinear nonlazy mean-field theorem. No external mathematical theorem
or numerical experiment is used.
