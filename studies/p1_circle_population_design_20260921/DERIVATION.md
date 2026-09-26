# Exact population constructions on the circle at p=1

This is a static representation theorem for the actual initialized dictionary
law, with freely chosen current read-in w, readout c, and middle matrix M.
It does not assert that a canonical training trajectory reaches these states.

## 1. The actual dictionary and closure

Let G_1,G_2,Z_1,Z_2 be independent standard Gaussians on the lower population,
and let T_1,T_2 be independent standard Gaussians on the separate upper population.
Following `docs/observable_p1.md`, put

\[
h_i=\tanh G_i,\quad v=E\tanh^2G,\quad
H_i=\tanh(\sqrt v T_i),\quad \tau=EH_i^2,\quad \alpha=1-\tau,
\]
\[
k_i=\tanh(\sqrt\tau Z_i+\alpha h_i),\qquad
s=Ek_i^2,\quad \beta=Eh_i k_i.
\]

The response alpha h_i is essential: h_i and k_i are not independent.
Set

\[
\psi_1=(1,h_1,h_2,k_1,k_2)^T,\qquad
\psi_2=(1,H_1,H_2)^T,
\quad L_jL_j^T=E\psi_j\psi_j^T+\eta I,
\quad b_j=L_j^{-1}\psi_j,\quad \eta=1/4096.
\]

Here L_j is lower triangular with positive diagonal. For
u(theta)=r(cos theta,sin theta), r>0, the closure is

\[
a(\theta)=E_1[b_1\tanh(w\cdot u(\theta))],\qquad
f(\theta)=E_2[c\tanh(b_2^TMa(\theta))],\quad M\in\mathbb R^{3\times5}.
\tag{1}
\]

The book normalizes u=x/sqrt(2): r=1 means the normalized input has unit
radius; r=1/sqrt(2) means the unnormalized x has unit radius.
The moving w and c are population functions, not polynomials restricted to
the p=1 dictionary. Choosing their joint law with the frozen dictionary is
substantive; specifying only their marginal distributions is insufficient.

It is convenient to specify a raw matrix K:

\[
K=L_2^{-T}ML_1^{-1},\qquad M=L_2^TKL_1.
\tag{2}
\]

Then the upper preactivation is exactly
psi_2^T K E_1[psi_1 tanh(w dot u)]. This invertible change of coordinates
does not equate the Frobenius norms of K and M.
Every state in (1) satisfies f(theta+pi)=-f(theta), since tanh is odd and
there are no biases. Thus even harmonics and a nonzero constant are excluded.

## 2. A nonzero coefficient at every odd frequency

For q a positive odd integer, define

\[
a_q(t)=\frac1{2\pi}\int_0^{2\pi}\tanh(t\cos\phi)\cos(q\phi)\,d\phi,
\qquad t>0.
\tag{3}
\]

For q=2m+1, write t_j=(j+1/2)pi, D_j(t)=sqrt(t_j^2+t^2),
and rho_j(t)=t/(D_j(t)+t_j). Then

\[
\boxed{a_{2m+1}(t)=2(-1)^m\sum_{j=0}^{\infty}
\frac{\rho_j(t)^{2m+1}}{D_j(t)}.}
\tag{4}
\]

In particular its sign is (-1)^m and it never vanishes for t>0.

Proof: the [NIST cosh product](https://dlmf.nist.gov/4.36.E2), whose factors
converge normally on bounded sets, gives by logarithmic differentiation on
real bounded intervals

\[
\tanh x=2x\sum_{j\ge0}(x^2+t_j^2)^{-1}.
\]

The differentiated summands are dominated by a constant times t_j^{-2}
on each such interval, justifying differentiation and integration there.
For a>0, D=sqrt(a^2+t^2), rho=t/(D+a), summing a geometric series gives

\[
\frac1{a^2+t^2\cos^2\phi}
=\frac1{aD}\left[1+2\sum_{l\ge1}(-\rho^2)^l\cos(2l\phi)\right].
\]

Its Fourier series is absolutely convergent. For q=2m+1, multiplication by
cos(phi) and cosine orthogonality show that its pairing with cos(q phi) is
(-1)^m rho^(2m)(1-rho^2)/(2aD), including m=0. Multiplying by 2t and using
t(1-rho^2)=2a rho gives (4). The outer summation is justified by the
uniform partial-fraction bound above. Each term in the resulting sum has
the stated strict sign. For large j it is O(j^(-q-1)), so it converges.

For a fixed radius rho>0 set A_q=a_q(r rho). Alternatively, let R have
Rayleigh scale sigma>0 and set

\[
A_q=E_R a_q(rR).
\tag{5}
\]

Since R>0 almost surely and (4) has a fixed strict sign, A_q is nonzero
in either construction. No numerical nonvanishing assumption is needed.

## 3. Custom read-in on the original Gaussian carrier

Write h=h_1, k=k_1 and S=(G_1,Z_1). Fix 0<epsilon<1/sqrt(2).
Given S choose the read-in angle Phi with density

\[
p(\phi\mid S)=\frac{1+\varepsilon[h\cos(q\phi)+k\sin(q\phi)]}{2\pi}.
\tag{6}
\]

It is strictly positive, integrates to one, and its unconditional marginal
is uniform because Eh=Ek=0. This density need hold only conditional on S,
not conditional on the full lower dictionary.

No extra random mark is needed. The unused independent pair (G_2,Z_2) has
polar angle Psi, uniform on the circle, independent of its radius. Let

\[
F_S(\phi)=\phi+\frac{\varepsilon}{q}
[h\sin(q\phi)-k\cos(q\phi)].
\]

Its derivative is the positive numerator in (6), and
F_S(phi+2pi)=F_S(phi)+2pi. Thus it is an invertible lift of a circle map.
Set Phi=F_S^{-1}(Psi) modulo 2pi. Change of variables gives precisely (6).
Choose either R=rho fixed or

\[
R=\sigma\sqrt{G_2^2+Z_2^2},\qquad
w=R(\cos\Phi,\sin\Phi).
\tag{7}
\]

The Gaussian polar density factorizes into a uniform angle and a Rayleigh
radius, so R is independent of (S,Psi), hence also of Phi. In (7), w therefore
has exactly the marginal N(0,sigma^2 I_2). In particular sigma=1 retains
the ordinary first-layer weight distribution. Its dependence on the frozen
dictionary has changed.

There is also an equivariant realization. For odd q,
F_{-S}(phi+pi)=F_S(phi)+pi. Simultaneously negating all four lower Gaussian
marks leaves R unchanged and shifts Psi by pi. It therefore negates w.
Values on the null event G_2=Z_2=0 may be set to zero. The constructed read-in
is compatible with the sign symmetry of the canonical invariant state class.

Integrating (6), then the independent radius, gives

\[
E[\tanh(w\cdot u(\theta))\mid S]
=\varepsilon A_q[h\cos(q\theta)+k\sin(q\theta)].
\tag{8}
\]

Indeed the constant angular integral vanishes, and translating phi-theta
in each cosine/sine term leaves (3) times cos(q theta)/sin(q theta).
Define

\[
\Sigma=\begin{pmatrix}v&\beta\\\beta&s\end{pmatrix}.
\]

It is strictly positive definite. If a h+b k=0 almost surely and b is
nonzero, conditioning on G_1 contradicts the nonzero conditional variance
of tanh(sqrt(tau) Z_1+alpha h). If b=0, nondegeneracy of h forces a=0.
Thus (8) implies the exact pair of contractions

\[
\begin{pmatrix}E[h\tanh(w\cdot u)]\\E[k\tanh(w\cdot u)]\end{pmatrix}
=\varepsilon A_q\Sigma
\begin{pmatrix}\cos(q\theta)\\\sin(q\theta)\end{pmatrix}.
\tag{9}
\]

The other lower dictionary contractions need not vanish; no assertion about
their value is used. They will have zero columns in K.

## 4. A whole matrix family and an elementary readout

For arbitrary real lambda,mu choose only the H_1 row and h_1,k_1 columns
of K to be nonzero, with

\[
K_{H_1,(h_1,k_1)}=
\frac{(\lambda,\mu)\Sigma^{-1}}{\varepsilon A_q}.
\tag{10}
\]

Then (9) makes the upper preactivation exactly

\[
H_1 z(\theta),\qquad z(\theta)=\lambda\cos(q\theta)+\mu\sin(q\theta).
\tag{11}
\]

This uses rank at most one in M, with fixed customized populations and two
freely variable matrix parameters. It is valid for all real lambda,mu.

The density of H=H_1=tanh(sqrt(v) T_1) is

\[
p_H(h)=\frac{\exp[-\operatorname{atanh}(h)^2/(2v)]}
{\sqrt{2\pi v}(1-h^2)},\quad -1<h<1.
\]

Fix 0<b<1 (for example b=1/2) and choose the population readout

\[
c_b(H)=\frac{\operatorname{sgn}(H)\mathbf1_{\{|H|\le b\}}}{2b p_H(H)},
\quad c_b(0)=0.
\tag{12}
\]

It is bounded, measurable and odd, since p_H is continuous and bounded
away from zero on [-b,b]. It has finite cost

\[
Ec_b(H)^2=\frac1{2b^2}\int_0^b\frac{dh}{p_H(h)}<\infty.
\]

Gaussian change of variables and cancellation of the density give, for every
real z,

\[
E[c_b(H)\tanh(zH)]
=\frac1b\int_0^b\tanh(zh)\,dh
=\frac{\log\cosh(bz)}{bz}=:L(bz),\quad L(0)=0.
\]

Consequently the exact output is

\[
\boxed{f_{\lambda,\mu}(\theta)=
L\!\left(b[\lambda\cos(q\theta)+\mu\sin(q\theta)]\right).}
\tag{13}
\]

There is no small-matrix approximation in (13). The readout is generally
outside span(1,H_1,H_2), which is permitted by the population state definition.
Its jumps cause no difficulty in this expectation identity. A smooth-readout
restriction would require modifying the claim or approximating (12); the
smooth finite-source theorem is not invoked for this custom readout.

## 5. Fourier content, approximation, and the price of frequency

For |t|<pi/2, L(t)=t/2-t^3/12+t^5/45-17t^7/2520+... . In particular, with
mu=0 and z=b lambda, (13) has the convergent local expansion

\[
f(\theta)=\left(\frac z2-\frac{z^3}{16}+O(z^5)\right)\cos(q\theta)
-\left(\frac{z^3}{48}+O(z^5)\right)\cos(3q\theta)
+O(z^5),
\]

where the last term collects higher odd multiples. More generally (13)
is a phase-shifted function containing only odd multiples of q. Its exact
elementary expression is valid even outside the Taylor convergence disk.

A global uniform bound avoids Taylor remainder assumptions. Since
L(t)=integral_0^1 tanh(ut) du and |tanh t-t|<=|t|^3/3,

\[
|L(t)-t/2|\le |t|^3/12,\qquad
\left\|\frac{2L(z\cos(q\theta))}{z}-\cos(q\theta)\right\|_\infty
\le z^2/6\quad(z\ne0).
\tag{14}
\]

The tanh bound follows by integrating 1-tanh'(t)=tanh^2(t)<=t^2 from zero,
using oddness for negative t. Thus a pure odd harmonic can be approximated
arbitrarily well by rescaling the readout; it is not asserted to equal (13)
at a finite nonzero z.

Frequency has a real cost. From (2),(10) and the actual ridge Gram,

\[
\|M\|_F^2=\frac{\tau+\eta}{\varepsilon^2 A_q^2}
(\lambda,\mu)\Sigma^{-1}(\Sigma+\eta I)
\Sigma^{-1}(\lambda,\mu)^T.
\tag{15}
\]

For fixed input/read-in radius t=r rho, (4) yields

\[
0<|a_q(t)|\le a_1(t)\rho_0(t)^{q-1},\qquad 0<\rho_0(t)<1.
\]

Hence at fixed nonzero (lambda,mu), the middle norm in this construction
grows at least exponentially along odd q for bounded fixed-radius read-in.
For the Gaussian-marginal variant A_q tends to zero by the same pointwise
bound and dominated convergence (|a_q|<=1); no exponential rate for its
unbounded radius mixture is asserted. The readout normalization in (14)
also costs a factor 2/|z|. Keeping ordinary first-layer weight scale does
not give a frequency-independent total parameter norm.

## 6. Arbitrary finite odd Fourier polynomials

The construction is not limited to a single chosen frequency. Fix a finite
odd Fourier polynomial

\[
T(\theta)=\sum_{q\ {m odd}}[t_q\cos(q\theta)+u_q\sin(q\theta)],
\quad
B(\phi)=\sum_{q\ {m odd}}\frac{t_q\cos(q\phi)+u_q\sin(q\phi)}{A_q}.
\]

Choose epsilon>0 with epsilon ||B||_infinity<1 (T=0 is trivial).
Replace (6) by [1+epsilon h_1 B(phi)]/(2pi). The zero-mean periodic
primitive J(phi)=sum_q[t_q sin(q phi)-u_q cos(q phi)]/(q A_q)
satisfies J'=B and J(phi+pi)=-J(phi). Therefore the monotone circle lift
F_h(phi)=phi+epsilon h J(phi) realizes this conditional law from the
same unused Gaussian polar angle and preserves mark-negation symmetry.
The Gaussian read-in marginal remains unchanged.

The same convolution calculation now gives

\[
E[\tanh(w\cdot u(\theta))\mid G_1,Z_1]=\varepsilon h_1 T(\theta),
\quad E[h_1\tanh(w\cdot u(\theta))]=\varepsilon vT(\theta).
\]

Taking only K_{H_1,h_1}=lambda/(epsilon v) nonzero yields exactly
f(theta)=L(b lambda T(theta)) with the same bounded readout. Rescaling
that readout by 2/(b lambda), for lambda nonzero, gives

\[
\left\|\frac{2L(b\lambda T)}{b\lambda}-T\right\|_\infty
\le \frac{(b\lambda)^2}{6}\|T\|_\infty^3.
\tag{16}
\]

Thus every finite odd Fourier polynomial is uniformly approximable at p=1,
with the ordinary Gaussian read-in marginal. The required coupling encodes
the chosen polynomial, and neither norms nor integration accuracy are uniform
over its complexity. It is not a fixed randomly sampled dictionary learning
an arbitrary polynomial merely by changing a small matrix.

## 7. Scope and unresolved questions

* These are exact static population identities and approximation bounds.
  They retain the actual reverse-response law and ridge normalization.
* They show that p=1 is not an angular bandwidth bound. They do not prove a
  characterization under bounded parameter norms, fixed initial read-in, or
  prescribed training dynamics.
* Sign symmetry is preserved, but these particular states are outside the
  finite-time canonical class with bounded w-G. For fixed radius this follows
  from the unbounded initial G. For the Gaussian-radius construction, R<=1
  and |G_1|>N have positive joint probability for every N, by independence;
  there |w-G|>=N-1. Thus these states are not finite-time endpoints of the
  prescribed canonical flow. This does not exclude approximation of their
  output functions by other states or trajectories.
* Population integration is exact here. Finite-population sampling, its
  conditioning at high frequency, and the necessary population count remain
  to be studied separately. No finite-width neural limit or fitted-network
  comparison follows just from these static formulas.
* The custom density/dictionary coupling contains target information. This
  is appropriate for the user's representation question, but cannot be
  counted as evidence that canonical gradient flow learns that information.
