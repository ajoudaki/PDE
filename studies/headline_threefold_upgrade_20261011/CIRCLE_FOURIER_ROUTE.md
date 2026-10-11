# Circle Fourier route: initialization susceptibility and a Gaussian component

2026-10-11. Scoped theoretical route. Scientific inputs were exactly
`paper/compact.tex`, `paper/compact_fitting.tex`,
`ENDPOINT_TRANSVERSE_ROUTE.md`, and `ENDPOINT_PROBE_NONCANCELLATION.md`.
The proof, conjecture-investigation, and canonical-notation skills and their
applicable references were read. No experiment, manuscript edit, or Git
operation was performed.

**Result.** There is an exact finite-width variance lower bound in terms of
the response of an endpoint spatial functional to a perturbation of the
initialization law. A stronger local regularity hypothesis turns that
response into an independent Gaussian component of the limiting endpoint
fluctuation. This gives the requested every-confidence lower bound, without
requiring that the whole fluctuation limit be Gaussian. The proof uses
angular perturbations of the first-layer Gaussian law and elementary
likelihood identities. It does not use a frozen-feature replacement or
finite-dimensional compensation versus infinite rank.

The two endpoint hypotheses needed to apply this theorem to the canonical
network remain unproved: a nonzero width-stable susceptibility, and local
regularity under initialization-law perturbations. In particular, this note
does **not** prove the requested canonical endpoint theorem. It identifies a
different quantitative mechanism and proves exactly what it would supply.

## 1. Canonical system and circle functional

Write

\[
v(\theta)=(\cos\theta,\sin\theta),\qquad
x(\theta)=\sqrt2\,v(\theta),\qquad 0\le\theta<2\pi.
\]

The supplied network is

\[
z^{(1)}=W^{(1)}v,\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n=\frac1n w^\top h^{(L)}.
\]

All hidden weights train by the supplied gradient flow for
\(\mathcal L=m^{-1}\sum_a(f_n(x_a)-y_a)^2\), with mobilities
\((n,1,\ldots,1,n)\) and \(w(0)=0\). Training directions are fixed and
pairwise nonparallel, their span may be all of \(\mathbb R^2\), and
\(L\ge2\) is fixed. The activations and labels have exactly the stated
strip-analytic bounded-derivative assumptions and original cap

\[
0<Y\le\lambda\beta^{-30L},\qquad \lambda=\gamma/m>0.
\]

Let \(E_n\) be the initialization event in the supplied fitting lemma.
It has probability tending to one. On it the fitted endpoint exists and

\[
\sup_\theta |f_n(\infty,x(\theta))|
\le \frac{\|w(\infty)\|}{\sqrt n}
       \sup_\theta\frac{\|h^{(L)}(\infty,x(\theta))\|}{\sqrt n}
\le\frac{4HY}{\sqrt\lambda}.
\tag{1}
\]

For the probability arguments only, define the endpoint function to be zero
outside \(E_n\), and denote this bounded random function by \(F_n(\theta)\).
This modification changes any eventual probability assertion by \(o(1)\).
It is not a modification of training on the successful event.

Choose a deterministic integrable real function \(\psi\) such that

\[
\frac1{2\pi}\int_0^{2\pi}|\psi(\theta)|\,d\theta\le1,
\qquad
X_n=\frac1{2\pi}\int_0^{2\pi}\psi(\theta)F_n(\theta)\,d\theta.
\tag{2}
\]

For the entire circle one may use \(\psi=1\), \(\cos(k\theta)\), or
\(\sin(k\theta)\). For a prescribed nonempty open arc \(A\) separated
from the signed training directions, choose \(\psi\) supported in \(A\).
For independent copies, (2) gives

\[
|X_n-\widetilde X_n|
\le \sup_{\theta\in\operatorname{supp}\psi}
          |F_n(\theta)-\widetilde F_n(\theta)|.
\tag{3}
\]

Thus a single successful functional proves the corresponding supremum
bound. Its support, and all its choices, must be fixed independently of
the realized initializations.

## 2. An exact circle score identity

Let \(g_i\in\mathbb R^2\), \(1\le i\le n\), be the independent first-layer
rows at initialization. Under their original law \(\mu=N(0,I_2)\), the
polar angle \(\alpha\) is uniform and independent of the radius. For a
fixed integer \(j\ge1\), either of

\[
q(g)=\sqrt2\cos(j\alpha),\qquad
q(g)=\sqrt2\sin(j\alpha)
\tag{4}
\]

has mean zero and variance one. Define it arbitrarily at \(g=0\), a
null event. It is bounded by \(\sqrt2\).

For a real parameter \(\varepsilon\), perturb only the initialization law:

\[
\frac{d\mu_\varepsilon}{d\mu}(g)
=\exp\{\varepsilon q(g)-\eta(\varepsilon)\},\qquad
\eta(\varepsilon)=\log\mathbb E_\mu e^{\varepsilon q(g)}.
\tag{5}
\]

The first-layer rows remain independent; all other blocks retain their
original laws and independence. The training equations and labels are
unchanged. These alternative laws are an inference device; the asserted
endpoint lower bound concerns only \(\varepsilon=0\).

Set

\[
S_n=\frac1{\sqrt n}\sum_{i=1}^n q(g_i),\qquad
T_n(\varepsilon)=\mathbb E_\varepsilon X_n.
\]

Since \(X_n\) and \(q\) are bounded, differentiation under the finite
product density is justified by a bounded integrable majorant on every
compact \(\varepsilon\) interval. At zero,

\[
T_n'(0)
=\mathbb E\left[X_n\sum_{i=1}^nq(g_i)\right]
=\sqrt n\,\mathbb E[(X_n-\mathbb E X_n)S_n].
\tag{6}
\]

Because \(\mathbb E S_n=0\) and \(\mathbb E S_n^2=1\), Cauchy--Schwarz
proves the exact finite-width inequality

\[
n\operatorname{Var}(X_n)\ge |T_n'(0)|^2.
\tag{7}
\]

In particular a nonzero limiting endpoint susceptibility immediately gives
a root-\(n\) variance scale. This avoids a many-neuron insertion expansion.
It does not by itself give a lower bound at every confidence.

## 3. Local regularity forces an independent Gaussian component

Here is a precise sufficient condition stronger than (7), with a complete
proof. Neither hypothesis below is claimed to follow from the paper.

**Conditional theorem.** Suppose there are deterministic real numbers
\(b_n\), a nonzero real number \(\tau\), and a finite real random variable
\(Z\), such that for every fixed real \(h\), under initialization law
\(\mu_{h/\sqrt n}^{\otimes n}\) and the unchanged laws of all other blocks,

\[
\sqrt n(X_n-b_n)-h\tau\ \Longrightarrow\ Z.
\tag{8}
\]

The same limiting law on the right must work for every \(h\), including
zero. Then there are independent random variables \(N\sim N(0,1)\) and
\(V\) such that

\[
Z\ \stackrel{\mathrm{law}}=\tau N+V.
\tag{9}
\]

Consequently, for two independent original Gaussian initializations and
every \(0<\delta<1\), all sufficiently large widths satisfy

\[
\Pr\left\{
\sup_{\theta\in\operatorname{supp}\psi}
 |f_n(\infty,x(\theta))-
       \widetilde f_n(\infty,x(\theta))|
\ge\frac{c_\delta}{\sqrt n}\right\}\ge1-\delta,
\qquad
c_\delta=\frac{\delta\sqrt\pi\,|\tau|}{2}.
\tag{10}
\]

Missing fitted endpoints count as failure. Their probability tends to zero
by the supplied fitting lemma, and is included in the eventual threshold.

**Proof.** Boundedness, zero mean, and unit variance of \(q\) give
\(\eta(u)=u^2/2+O(u^3)\). The likelihood ratio of the local alternative
to the original law is therefore

\[
L_{n,h}=\exp\{hS_n-n\eta(h/\sqrt n)\}
=\exp\{hS_n-h^2/2+o(1)\}.
\tag{11}
\]

The characteristic function expansion
\(\mathbb E e^{itq/\sqrt n}=1-t^2/(2n)+O(n^{-3/2})\) proves
\(S_n\Rightarrow N(0,1)\). Also

\[
\mathbb E L_{n,h}^2
=\exp\{n[\eta(2h/\sqrt n)-2\eta(h/\sqrt n)]\}
\longrightarrow e^{h^2}.
\tag{12}
\]

Hence the likelihoods are uniformly integrable. The same calculation for
any fixed larger moment controls their tails when passing through joint
weak limits. In particular \(E_n^c\) remains negligible under each local
alternative, since
\(\Pr_{h/\sqrt n}(E_n^c)\le
(\mathbb E L_{n,h}^2)^{1/2}\Pr(E_n^c)^{1/2}\).

Put \(Z_n=\sqrt n(X_n-b_n)\). Their two marginal sequences are tight,
so along a subsequence \((Z_n,S_n)\Rightarrow(Z_*,S)\), with
\(Z_*\) having law \(Z\) and \(S\sim N(0,1)\). Changing measure with
(11), truncating its exponential, and using (12) to remove the truncation
gives, for real \(t,h\),

\[
\mathbb E e^{itZ_*+hS-h^2/2}
=e^{ith\tau}\,\mathbb E e^{itZ_*}.
\tag{13}
\]

The left side as a function of complex \(h\) is entire: on any compact
set its integrand and all its derivatives are dominated by a polynomial
in \(|S|\) times \(e^{C|S|+C}\), integrable for a standard normal.
Thus equality on the real axis extends to complex \(h\). Substituting
\(h=is\) and rearranging yields

\[
\mathbb E e^{itZ_*+isS}
=e^{-s^2/2-ts\tau}\,\mathbb E e^{itZ_*}.
\tag{14}
\]

For \(V=Z_*-\tau S\), replace \(s\) in (14) by \(s-t\tau\):

\[
\mathbb E e^{itV+isS}
=e^{-s^2/2}
  \left[e^{t^2\tau^2/2}\mathbb E e^{itZ_*}\right]
=\mathbb E e^{isS}\,\mathbb E e^{itV}.
\]

This proves independence and (9). No theorem identifying the entire limit
as Gaussian has been invoked.

For independent copies, \(Z-\widetilde Z\) is the convolution of
\(N(0,2\tau^2)\) and the law of \(V-\widetilde V\). Its density is
bounded above by \(1/(2\sqrt\pi|\tau|)\), since convolution with a
probability measure cannot increase a density's supremum. Therefore

\[
\Pr\{|Z-\widetilde Z|\le c\}
\le\frac{c}{\sqrt\pi|\tau|}.
\tag{15}
\]

Independence and (8) at \(h=0\) give
\(\sqrt n(X_n-\widetilde X_n)\Rightarrow Z-\widetilde Z\).
The limit has a density, so probabilities of \([-c,c]\) converge.
For \(c=c_\delta\), their limit is at most \(\delta/2\). Equation
(3), together with \(\Pr(E_n\cap\widetilde E_n)\to1\), proves (10).
\(\square\)

The centering \(b_n\) cancels between the two dense copies. In particular,
this criterion does not require knowing a limiting deterministic endpoint
to accuracy \(o(n^{-1/2})\).
The coefficient \(\tau\) in (8) belongs to the local weak-limit statement;
identifying it with \(\lim_n T_n'(0)\) would additionally require control
of expectations. That identification is not used in this proof.

## 4. What must survive, and what the supplied inputs do not prove

The mechanism asks for a response of the fully trained endpoint to a small
angular bias in its initial neuron distribution. Fixed training data break
rotation symmetry, so an angular score of degree \(j\) need not produce an
endpoint response of the same Fourier degree. No diagonal Fourier response
formula is asserted.

If a deterministic continuous response function \(s(\theta)\) were
established under the local perturbations, with functional response

\[
\tau=\frac1{2\pi}\int\psi(\theta)s(\theta)\,d\theta,
\tag{16}
\]

then any nonzero \(s\) on the circle has a nonzero real Fourier coefficient.
For an arc one instead needs \(s\) nonzero somewhere on that arc; a smooth
supported test of the appropriate sign then makes (16) nonzero after
normalization. A nonzero response on the circle alone does not imply this
arc condition. Nor does analyticity of each finite-width endpoint supply a
common complex strip or an analytic fluctuation limit as \(n\) grows.

The supplied probe result proves infinite-rank conditional influence when
both its fitting bounds and its two-query initialization event (13) hold;
their intersection has probability tending to one. It neither proves a nonzero limiting mean
susceptibility in (6), nor excludes cancellation when one averages over
the cavity, nor supplies (8). The supplied transverse identity proves an
absolute cubic label correction. Because its constants do not compare that
correction to a nonzero susceptibility, it does not prove \(\tau\ne0\)
under the original cap. Replacing the full endpoint by its frozen-feature
linear label coefficient would leave exactly that missing bridge.

Local regularity (8) is also substantive. Convergence only at the original
initialization law, or convergence of the derivatives \(T_n'(0)\), is not
enough. One must control the endpoint under contiguous law perturbations
and show that the perturbation changes its root-\(n\) limit by a translation
with a nonzero coefficient. This condition does not assume Gaussianity or
anti-concentration of the unperturbed limit, but it is still a fluctuation
theorem requiring proof for the trained network.

## 5. A direct audit of the variance shortcut

Positive susceptibility and a root-\(n\) variance do not suffice for every
confidence, even for bounded statistics with bounded normalized moments.
For a logical example, let \(B\) be an independent Bernoulli variable with
\(\Pr(B=1)=p\in(0,1)\), and form

\[
X_n^{\mathrm{example}}=\frac{B\tanh(S_n)}{\sqrt n}.
\]

The exact score identity gives

\[
T_n'(0)=p\,\mathbb E[S_n\tanh(S_n)]
\longrightarrow p\,\mathbb E[N\tanh(N)]>0.
\]

Moment convergence follows from bounded fourth moments of \(S_n\),
which follow by expanding the fourth moment of the bounded independent
centered summands. Nevertheless the difference of two independent copies
vanishes with probability at least \((1-p)^2\), when both Bernoulli
variables are zero. Thus no every-confidence positive lower bound follows.
This is not a canonical-network counterexample. It isolates the precise
logical failure in promoting (7) to the requested claim; (8) excludes it.

## 6. Status and reopening condition

| Claim | Status |
| --- | --- |
| Exact angular-score identity (6) for a fully trained bounded endpoint functional | Proved |
| Finite-width susceptibility variance bound (7) | Proved |
| Local regularity with nonzero response implies an independent Gaussian component | Proved, conditional on (8) |
| That component gives the endpoint supremum lower bound at every confidence | Proved, conditional on (8) |
| Some angular/radial initialization perturbation has a nonzero limiting endpoint response for every admissible fixed problem | Open |
| Canonical endpoint local regularity under these perturbations | Open |
| The requested canonical circle or fixed-arc endpoint lower bound | Not proved or disproved |

This route is blocked for the full theorem at those two endpoint properties.
It should reopen upon a width-uniform differentiability and fluctuation
theorem for the endpoint as a functional of an initialization law, or a
direct proof of (8) for one spatial test and one bounded row score. Merely
selecting a nonzero finite-width Fourier coefficient, repeating infinite
rank, or establishing variance without local regularity does not reopen it.

The conditional theorem is useful if an endpoint fluctuation analysis
produces a nonzero deterministic susceptibility but does not identify the
entire limit: the Gaussian component argument already gives all confidence
levels and allows arbitrary independent additional fluctuation. These are
scoped author results, not promoted established material.
