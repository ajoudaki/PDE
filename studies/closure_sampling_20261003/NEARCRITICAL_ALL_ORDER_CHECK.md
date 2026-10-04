# Reconstruction of the all-order initialized covariance bound

2026-10-04. Scoped check by the trained-response route author, who did not
author or assemble the candidate checked here. The complete checked input
was NEARCRITICAL_ALL_ORDER_ROUTE.md, SHA-256
17563e139b7e41962d4eff8c78382f16600c50075b722742d1f9fca6f2bf4ec3.
No additional scientific file was needed: the activation moments and
covariance formula are reconstructed below. Required shared instructions,
canonical notation and neural conventions, and rigorous proof/research
instructions had already been read and were applied.

Verdict: equations (1)--(12) of the candidate pass this reconstruction,
with their stated population-initialization scope. The argument supplies
one radius controlling every order, rather than unrelated bounds at each
fixed order. It proves no trained finite-network response bound, no
compression theorem, and no finite-width complex second-moment estimate.
The last paragraph's reference to a companion finite-width counterexample
is not a premise of (1)--(12); that separate referenced file was outside
the assigned input and was not re-audited here.

## 1. Activation moments and covariance

Fix \(a>0\), and let \(Z\) be a standard real Gaussian. Write
\[
\psi(x)=\operatorname{erf}(x/\sqrt2),\qquad
A_0=a^2+2a/\sqrt\pi,\qquad
Q=A_0+1/3,\qquad D=A_0+2/(\pi\sqrt3).
\]
The symbol \(A_0\) here is just the scalar coefficient in the covariance;
it is unrelated to an input-weight matrix. Since
\(\psi'(x)=\sqrt{2/\pi}e^{-x^2/2}\), direct Gaussian integration gives
\[
\mathbb E\psi'(Z)=1/\sqrt\pi,\qquad
\mathbb E\psi'(Z)^2=2/(\pi\sqrt3).
\]
The Gaussian distribution function evaluated at \(Z\) is uniform on
\([0,1]\), so \(\mathbb E\psi(Z)=0\) and
\(\mathbb E\psi(Z)^2=1/3\). Integration by parts, with vanishing Gaussian
boundary terms because \(\psi\) is bounded, gives
\(\mathbb E Z\psi(Z)=\mathbb E\psi'(Z)=1/\sqrt\pi\). Consequently
\[
\mathbb E[aZ+\psi(Z)]^2=Q,\qquad
\mathbb E[a+\psi'(Z)]^2=D.
\]
For \(0<\chi\le D/Q\), set
\[
\phi(x)=\sqrt{\chi/D}\,[ax+\psi(x)]
                 \mathbin{\pm}\sqrt{1-\chi Q/D}.
\]
Its odd part has mean zero, giving
\(\mathbb E\phi(Z)^2=1\) and \(\mathbb E\phi'(Z)^2=\chi\).
The offset is real under the displayed restriction. The activation is
entire, unbounded, and nonlinear; its real Lipschitz constant is at most
\(\sqrt{\chi/D}(a+\sqrt{2/\pi})\). In particular, its growing linear part
has not been removed. The critical choice \(\chi=1\) is admissible because
\(D-Q=2/(\pi\sqrt3)-1/3>0\).

For centered unit-variance jointly Gaussian \(X,Y\) with covariance \(c\),
Gaussian regression gives
\[
\mathbb E[X\psi(Y)]=c/\sqrt\pi.
\]
For \(|c|<1\), differentiation of the bivariate Gaussian density with
respect to covariance equals its mixed spatial derivative. Two
integrations by parts yield
\[
\frac d{dc}\mathbb E[\psi(X)\psi(Y)]
 =\mathbb E[\psi'(X)\psi'(Y)]
 =\frac{2}{\pi\sqrt{4-c^2}}.
\]
The Gaussian density on a compact subset of \(|c|<1\) dominates the
needed derivatives; boundedness of \(\psi,\psi'\) supplies the boundary
conditions. The last equality follows by diagonalizing the covariance
matrix in the Gaussian integral for \(e^{-(X^2+Y^2)/2}\).
At \(c=0\) the expectation is zero. Integration and endpoint continuity
therefore give
\[
F(c):=\mathbb E[\phi(X)\phi(Y)]
 =1-\chi Q/D+\frac{\chi}{D}
       \left[A_0c+\frac2\pi\arcsin(c/2)\right].
\]
This is precisely the candidate's formula, independently of the offset
sign. In particular \(F(1)=1\), \(F'(1)=\chi\).

The real covariance formula initially describes \(-1\le c\le1\).
Its displayed power series provides the analytic continuation used for
the positive scalar majorant beyond one. No Gaussian pair with covariance
larger than its variance is being asserted.

## 2. A common covariance radius and all Taylor coefficients

All coefficients in the Taylor series of \(F\) about zero are
nonnegative: the constant is \(1-\chi Q/D\ge0\), the linear coefficient
is positive, and the arcsine series has positive odd coefficients.
The series has radius exactly two since its arcsine coefficient is
nonzero. Differentiating its explicit formula gives
\[
F''(u)=\frac{2\chi u}{\pi D(4-u^2)^{3/2}}.
\]
The function on the right is increasing for \(1\le u<2\). Therefore
\[
0\le F''(u)\le B:=\frac{24\chi}{7\pi\sqrt7D}
\quad(1\le u\le3/2),
\]
which verifies the candidate's constant, including the factor 24.
Taylor's formula with integral remainder implies
\[
0\le F(1+e)-1\le\chi e+\tfrac12 Be^2
\quad(0\le e\le1/2).
\]

For integer \(L\ge1\), define
\[
S_L=\sum_{j=0}^{L-1}\chi^j,\qquad
r=\min\left\{\frac1{4\max(1,\chi^L)},
                     \frac{\chi}{4BS_L}\right\},
\qquad K_L=F^{\circ L}.
\]
Every quantity is strictly positive because \(\chi>0\).
Set \(e_0=r\), \(e_{j+1}=F(1+e_j)-1\), and
\(u_j=e_j/\chi^j\). To reconstruct the induction without assuming
its conclusion, suppose \(u_i\le2r\) for \(0\le i\le j<L\).
Then
\[
e_i\le2\chi^i r\le1/2
\]
by the first restriction on \(r\), so the Taylor inequality is applicable
at all those indices. Summing its normalized increments gives
\[
u_{j+1}
\le r+\frac{B}{2\chi}\sum_{i=0}^j\chi^i u_i^2
\le r+\frac{2B}{\chi}r^2 S_L
\le\frac32r<2r.
\]
Thus the induction extends to \(L\), all compositions are evaluated below
the singularity at two, and
\[
K_L(1+r)-1=e_L\le2\chi^Lr.
\tag{C1}
\]

Here the passage from scalar evaluation to a Taylor series at one is
valid even though the inner function in a composition has a nonzero
constant term. Expand each occurrence of \(F\) by its nonnegative series.
At the nonnegative argument \(1+r\), Tonelli/monotone summation identifies
each iterated sum with its finite scalar composition. The finiteness just
proved implies that the resulting coefficients \(p_{L,j}\ge0\) satisfy
\[
K_L(c)=\sum_{j\ge0}p_{L,j}c^j,\qquad
\sum_jp_{L,j}(1+r)^j=K_L(1+r)<\infty,\qquad
\sum_jp_{L,j}=K_L(1)=1.
\]
Absolute convergence at complex arguments with modulus at most \(1+r\)
follows by domination. This identifies the series with the analytic
composition on its connected neighborhood of the real interval.

Expand each \(c^j=(1+u)^j\) by the binomial theorem and exchange the
nonnegative sums for \(0\le u\le r\). The coefficient of \(u^k\) is
\[
a_k=\sum_{j\ge k}p_{L,j}\binom jk\ge0,\qquad
\sum_{k\ge1}a_kr^k=K_L(1+r)-1.
\]
All \(a_k\) are finite, and the latter power series is absolutely
convergent for \(|u|\le r\). Thus it is the Taylor series at one and
\(a_k=K_L^{(k)}(1)/k!\). By (C1),
\[
\frac{K_L^{(k)}(1)}{k!}=a_k
\le2\chi^Lr^{1-k}\qquad(k\ge1).
\tag{C2}
\]
This verifies the critical quantifier: one \(r\), independent of \(k\),
proves (C2) simultaneously for every order. No limit in derivative order
has been interchanged with a merely fixed-order asymptotic.

At \(\chi=1\),
\[
r=\min\{1/4,\ 7\pi\sqrt7D/(96L)\},\qquad
c_a=\min\{1/4,\ 7\pi\sqrt7D/96\}.
\]
For \(L\ge1\), each entry defining \(r\) is at least \(c_a/L\).
Substitution in (C2) gives
\[
\frac{K_L^{(k)}(1)}{k!}\le2(L/c_a)^{k-1}.
\tag{C3}
\]
For \(k=1\) this is consistent with the exact value
\(K_L'(1)=\chi^L\); the factor two is simply slack.

## 3. Hilbert-valued analyticity and angular derivatives

Let the direct sum run over the real tensor spaces
\((\mathbb R^d)^{\otimes j}\), with the zeroth tensor space equal to
\(\mathbb R\). Define, for real unit \(v\),
\[
\Phi_L(v)=\bigoplus_{j\ge0}\sqrt{p_{L,j}}\,v^{\otimes j}.
\]
Its squared norm is one, and its inner product with \(\Phi_L(w)\) is
\(K_L(v^\top w)\). This is a concrete Hilbert realization of the
initialized population covariance. It is not an assertion about the
distribution of a finite collection of actual neurons.

Complexify the tensor spaces with their Hermitian products. The tensor
norm identity gives
\[
\|\Phi_L(z)\|^2=\sum_jp_{L,j}(z^*z)^j=K_L(z^*z)
\]
whenever the series converges. For orthonormal real \(v,u\) (so \(d\ge2\)),
put \(z(\theta)=v\cos\theta+u\sin\theta\), for complex \(\theta\).
A direct expansion gives
\[
z(\theta)^*z(\theta)
=|\cos\theta|^2+|\sin\theta|^2
=\cosh(2\operatorname{Im}\theta).
\]
Let \(\tau=\sqrt r/2\le1/4\).
For \(|t|\le1/2\), the positive power series of cosh gives
\(\cosh(2t)-1\le4t^2\): put \(x=2t\), use \(|x|\le1\), and bound
\(\sum_{j\ge1}x^{2j}/(2j)!\le x^2(\cosh1-1)\le x^2\).
Consequently
\[
|\operatorname{Im}\theta|\le\tau
\quad\Longrightarrow\quad
z(\theta)^*z(\theta)\le1+r,\qquad
\|\Phi_L(z(\theta))\|^2\le1+2\chi^Lr\le3/2.
\tag{C4}
\]
The final inequality uses the first entry in the definition of \(r\),
and holds also when \(\chi<1\).

The squared norm of the tail after tensor degree \(N\), uniformly on
the closed strip, is at most
\[
\sum_{j>N}p_{L,j}(1+r)^j\longrightarrow0.
\]
The finite tensor sums are holomorphic. Their locally uniform convergence
in Hilbert norm gives a Hilbert-valued holomorphic map on the open strip.
This can also be reconstructed directly: apply the ordinary Cauchy
integral formula to each finite sum on a circle inside the strip, pass
to the limit in the uniformly convergent boundary integral, and obtain
the Hilbert-valued derivative formula. Thus no finite-n moment or
unstated differentiability assumption is used.

For real \(\theta\), the disk of any radius \(s<\tau\) is contained in
the strip. The vector Cauchy formula and (C4) imply
\[
\frac{\|\partial_\theta^k\Phi_L(z(\theta))\|}{k!}
\le\sqrt{3/2}\,s^{-k}.
\]
Taking \(s\uparrow\tau\) gives the candidate's simultaneous bound
\[
\frac{\|\partial_\theta^k\Phi_L(z(\theta))\|}{k!}
\le\sqrt{3/2}\left(\frac2{\sqrt r}\right)^k
\quad(k\ge0).
\tag{C5}
\]
At criticality its right side is at most
\(\sqrt{3/2}[2\sqrt{L/c_a}]^k\). The zeroth-order bound is valid
with slack. For \(d=1\) there is no pair of real orthonormal directions;
the angular assertion has no such instance, while the scalar covariance
and tensor-feature construction still apply.

## 4. Scope, depth growth, and the remaining training problem

The polynomial angular radius \(L^{-1/2}\) is established at
\(\chi=1\). For a fixed \(\chi>1\), however close to one, the displayed
\(r\) can shrink exponentially in \(L\); the candidate does not claim
otherwise. As an immediate consequence of its explicit formulas, if
\(|\log\chi|\le\kappa/L\) for fixed \(\kappa\), then
\[
r\ge e^{-\kappa}c_a/L,
\]
because \(\max(1,\chi^L)\le e^\kappa\),
\(S_L\le Le^\kappa\), and
\(\chi/(4B)=7\pi\sqrt7D/96\). This is a precise regime in which the
same all-order polynomial-radius interpretation is valid near criticality.

The derivative coefficient bound grows geometrically in order after
division by \(k!\). Therefore the Taylor series is controlled at a common
positive radius, whose depth dependence is explicit. It would be incorrect
to describe all derivatives themselves as uniformly bounded in order, or
to claim a depth-independent radius.

The actual trained quantities involve a different law and repeated use
of the same matrices. In the canonical network, a query preactivation
tangent \(J=D_vz[v_{\rm dir}]\) and residual-free parameter response
\(R_a=D_\Theta z\,\nabla_\Theta(nf_a)\) enter products such as
\(\phi''(z)\odot R_a\odot J\). Neither (C2) nor (C5) bounds these
finite-network trained products. The Cauchy estimate is for the explicit
population Hilbert feature, not for a random finite network averaged
over its initialization. No improved label cap, source radius along
training, autonomous runtime error, or retained storage count is proved.

No flaw or repair requirement was found in the checked mathematical chain.
The source file was not changed. This check is an internal scoped
reconstruction, not a fresh isolated promotion review: the checker had
previously worked on trained-response estimates and had read the earlier
normalized-erf initialization note within the same study.
