# Ordinary iid small networks have an unavoidable sampling error

Status: proved scoped limitation, 2026-10-05. This does not rule out a
designed compact model, quadrature initialization, altered optimizer, or
correlated coupling. It treats a small network that uses the original
architecture, ordinary iid initialization, squared loss, and the original
width-dependent mobilities. No population dynamics theorem is needed.

The input scope is the assignment, `docs/notation.qmd`, and this agent's
previous derivations. The frozen `ANALYTIC_ROUTE.md` was not changed. The
previously read investigation and proof skills apply; the canonical-notation
skill remains inaccessible, and the supervisor-authorized notation fallback
is retained. No experiment, external research source, or other study was
used.

## Statement and model

Fix one sample \((x_1,y)\), where \(\|x_1\|_2=\sqrt d\) and
\(0<|y|\le1\). For width \(q\), let

\[
 u(x)=Ax/\sqrt d,\quad h(x)=\tanh u(x),\quad
 v(x)=Wh(x),\quad g(x)=\tanh v(x),\quad f_q(x)=w^Tg(x)/q.
\]

The initial entries of \(A\) are iid \(\mathcal N(0,1)\); the
entries of \(W\) are iid \(\mathcal N(0,1/q)\), independently of
\(A\); and \(w(0)=0\). Train by gradient flow of
\((f_q(x_1)-y)^2\) with mobilities \((q,1,q)\) for \((A,W,w)\).
Write \(f_q^{[1]}\) and \(f_q^{[2]}\) for two independent runs.

There are absolute constants \(a,C,p_0>0\), independent of
\(q,d,x_1,y\), such that at the deterministic physical time

\[
 t_q=\frac{a}{C\sqrt q},
\]

one has

\[
 \mathbb P\left(
 |f_q^{[1]}(t_q,x_1)-f_q^{[2]}(t_q,x_1)|
 \ge \frac{a^2|y|}{Cq}\right)\ge p_0.
 \tag{1}
\]

In particular, this is a lower bound for their discrepancy over all
physical time and the whole input sphere. The constants below are explicit,
although deliberately not optimized.

Consequently, if \(q=q(n)=o(\sqrt n)\), ordinary iid width-\(q(n)\)
initialization cannot achieve error \(C_{\mathrm{data},\delta}/\sqrt n\)
against an independently initialized dense width-\(n\) run with success
probability \(1-\delta\) for every fixed \(\delta>0\). This includes
\(q(n)=\lceil\log(en)\rceil\) and every fixed polynomial in
\(\log(en)\). The conclusion is stronger than required in its width
range, but weaker than an optimal sampling lower bound: the exponent in
(1) is \(q^{-1}\), not \(q^{-1/2}\).

## 1. A nondegenerate initial-kernel fluctuation

Let \(\psi(z)=\tanh^2z\), let \(G\sim\mathcal N(0,1)\), and define

\[
 v_* =\mathbb E\psi(G)\in(0,1),\qquad
 \mu(v)=\mathbb E\psi(\sqrt vG),\qquad
 \nu(v)=\operatorname{Var}(\psi(\sqrt vG)).
\]

At the training point, the initial first preactivations \(u_i\) are
independent standard Gaussians. Conditionally on \(h=\tanh u\), the
second preactivations \(v_j\) are independent centered Gaussians with
variance

\[
 V_q=\frac1q\sum_{i=1}^q\psi(u_i).
\]

This conditional Gaussian statement follows by multiplying the moment
generating functions of the independent entries in each row of \(W\);
different rows remain independent. Define the initial readout kernel

\[
 \kappa_q=\frac1q\sum_{j=1}^q\psi(v_j).
\]

We first give a strictly positive lower bound for \(\nu(v)\), uniformly
on \([v_*/2,1]\). Put

\[
 r=\frac12\sqrt{v_*/2},\qquad
 \alpha=\mathbb P(|G|\le r),\qquad
 \beta=\mathbb P(|G|\ge1),\qquad
 b=\alpha\beta[\psi(2r)-\psi(r)]^2>0.
 \tag{2}
\]

For such \(v\), the random variable \(\psi(\sqrt vG)\) is at most
\(\psi(r)\) on \(|G|\le r\), and at least \(\psi(2r)\) on
\(|G|\ge1\). If \(X'\) is an independent copy of \(X\), then
\(\operatorname{Var}X=\mathbb E(X-X')^2/2\). Restricting this
expectation to the two opposite combinations of these events proves
\(\nu(v)\ge b\).

Since \(0\le V_q\le1\) and \(\mathbb EV_q=v_*\),

\[
 v_*\le v_*/2+\mathbb P(V_q\ge v_*/2),
\]

so \(\mathbb P(V_q\ge v_*/2)\ge v_*/2\), for every \(q\ge1\).
Conditional variance and the identity
\(\operatorname{Var}X=\mathbb E\operatorname{Var}(X\mid H)
+\operatorname{Var}(\mathbb E[X\mid H])\) now give

\[
 \operatorname{Var}\kappa_q
 \ge \frac{\mathbb E\nu(V_q)}q
 \ge\frac{bv_*}{2q}.
 \tag{3}
\]

For completeness, the variance identity follows by writing
\(X-\mathbb EX=(X-\mathbb E[X\mid H])
+(\mathbb E[X\mid H]-\mathbb EX)\), expanding the square, and using
the zero conditional mean of the first term.

An upper fourth-moment bound is also needed. Direct differentiation gives

\[
 \psi''(z)=2[1-\tanh^2z][1-3\tanh^2z],\qquad |\psi''(z)|\le2.
\]

For \(v>0\), differentiation under the Gaussian integral and integration
by parts give

\[
 \mu'(v)=\frac12\mathbb E\psi''(\sqrt vG),
 \qquad |\mu'(v)|\le1.
 \tag{4}
\]

The boundary term vanishes since the Gaussian density decays and
\(\psi'\) is bounded. Differentiation on a compact subinterval of
\(v>0\) is justified by the integrable bound
\(|G|\sup|\psi'|/(2\sqrt v)\). At zero,
\(0\le\mu(v)\le v\), because \(|\tanh z|\le|z|\), so (4)
extends to a Lipschitz bound on all of \([0,1]\).

For independent mean-zero random variables \(X_i\) with \(|X_i|\le1\),
expansion of the fourth power and cancellation of every term with an
unpaired index yield

\[
 \mathbb E\left(\frac1q\sum_iX_i\right)^4
 =\frac{\sum_i\mathbb EX_i^4
 +6\sum_{i<j}\mathbb EX_i^2\mathbb EX_j^2}{q^4}
 \le\frac3{q^2}.
 \tag{5}
\]

Apply (5) conditionally to \(\kappa_q-\mu(V_q)\), and directly to
\(V_q-v_*\). By (4) and
\((x+z)^4\le8(x^4+z^4)\),

\[
 \mathbb E|\kappa_q-\mu(v_*)|^4\le\frac{48}{q^2}.
\]

For two independent copies put \(D_q=\kappa_q^{[1]}-\kappa_q^{[2]}\).
The same elementary fourth-power inequality and (3) imply

\[
 \mathbb ED_q^2=2\operatorname{Var}\kappa_q\ge\frac{bv_*}{q},
 \qquad \mathbb ED_q^4\le\frac{768}{q^2}.
 \tag{6}
\]

Here is the required lower-tail estimate without invoking an unproved
probabilistic limit theorem. For a nonnegative \(Z\) with finite second
moment, put \(E=\{Z\ge\mathbb EZ/2\}\). Splitting its expectation and
using Cauchy--Schwarz gives

\[
 \mathbb EZ\le\frac12\mathbb EZ
 +(\mathbb EZ^2)^{1/2}\mathbb P(E)^{1/2},
\]

and therefore
\(\mathbb P(E)\ge(\mathbb EZ)^2/(4\mathbb EZ^2)\). Set \(Z=D_q^2\)
in this inequality and use (6). With the absolute constants

\[
 a=\sqrt{bv_*/2},\qquad p_*=(bv_*)^2/3072,
 \tag{7}
\]

we have, for every \(q\),

\[
 \mathbb P(|D_q|\ge a/\sqrt q)\ge p_*.
 \tag{8}
\]

## 2. Combining the fluctuation with an operator-norm bound

Choose the fixed constant

\[
 M=\sqrt{8\,[2\log9+\log(8/p_*)]}.
 \tag{9}
\]

For a matrix with independent \(\mathcal N(0,1/q)\) entries,

\[
 \mathbb P(\|W\|_{\mathrm{op}}>M)
 \le2\exp[-(M^2/8-2\log9)q]\le p_*/4.
 \tag{10}
\]

To verify this bound, take one-quarter nets of the two unit spheres. Each
can have at most \(9^q\) points: choose a maximal separated set and compare
the disjoint balls of radius one-eighth about its points to the ball of
radius nine-eighths. Approximating both unit vectors by net points shows
that the operator norm is at most twice the maximum absolute bilinear form
over the two nets. Each such form is \(\mathcal N(0,1/q)\). Its tail at
\(M/2\) is at most \(2e^{-qM^2/8}\), by exponential Markov inequality
and the Gaussian moment generating function
\(\mathbb Ee^{\lambda G}=e^{\lambda^2/2}\); the latter follows by
completing the square in its density. A union bound gives (10).

The events in (8) and (10) need not be independent. Subtracting the two
operator-norm failure probabilities from (8), the event

\[
 |D_q|\ge a/\sqrt q,\qquad
 \|W^{[1]}(0)\|_{\rm op},\|W^{[2]}(0)\|_{\rm op}\le M
 \tag{11}
\]

has probability at least \(p_0:=p_*/2>0\), uniformly in \(q\).

## 3. A deterministic short-time curvature bound

We supply the bound for a single run satisfying \(\|W(0)\|_{\rm op}\le M\).
All coordinates in this section refer to the training point. Introduce the
feature parameter \(s\) and define

\[
 w'=g,\qquad
 W'=\frac{(w\odot\tanh'v)h^T}{q},\qquad
 u'=\tanh'u\odot W^T(w\odot\tanh'v),
 \tag{12}
\]

where primes now denote \(s\)-derivatives. The first-matrix equation
underlying the last formula is the stated \(u'\) vector multiplied by
\(x_1^T/\sqrt d\); the equality \(\|x_1\|_2^2=d\) gives (12).
The original physical-time flow is obtained by

\[
 \dot s=2[y-F(s)],\qquad F(s)=w(s)^Tg(s)/q,\qquad s(0)=0.
 \tag{13}
\]

Multiplication of (12) by \(\dot s\) verifies every gradient-flow
factor, including the hidden-matrix factor \(1/q\). In particular, no
change of physical clock has been made in the comparison.

For real \(s\), integration of (12) gives

\[
 \|w(s)\|_\infty\le|s|,\qquad
 \|W(s)\|_{\rm op}\le M+s^2/2.
 \tag{14}
\]

The second bound uses
\(\|W'\|_{\rm op}\le\|w\|_2\|h\|_2/q\le|s|\).
These and the bounds below give bounded parameters on any fixed finite
feature interval, so the smooth finite-dimensional feature ODE continues
through that interval.

Write

\[
 D=\operatorname{diag}(\tanh'(u)^2),\quad z=w\odot\tanh'v,
 \quad B(s)=\frac{\|h\|_2^2}{q}I+WDW^T.
\]

Then \(v'=B(s)z\), and direct differentiation of \(F\) yields

\[
 F'(s)=\frac{\|g\|_2^2}{q}+\frac{z^TB(s)z}{q}\ge0.
 \tag{15}
\]

Consequently, for the physical flow,
\(\frac d{dt}(F(s(t))-y)^2=-4F'(s(t))(F(s(t))-y)^2\le0\).
Thus

\[
 |F(s(t))-y|\le|y|,\qquad |s(t)|\le2|y|t.
 \tag{16}
\]

In particular, on \(0\le t\le1/(2\sqrt q)\),
\(|s(t)|\le q^{-1/2}\), since \(|y|\le1\).

To control the second derivative, put the absolute constants
\(R=M+1\), \(B_0=1+R^2\). On \(|s|\le1\), equations (12)--(14)
and \(|\tanh'|\le1\), \(|\tanh''|\le2\) give

\[
 \begin{aligned}
 \|u'\|_2/\sqrt q&\le R|s|,
 &\|v'\|_2/\sqrt q&\le B_0|s|,\\
 \|z\|_2/\sqrt q&\le|s|,
 &\|z'\|_2/\sqrt q&\le1+2B_0s^2\le1+2B_0,\\
 \|B(s)\|_{\rm op}&\le B_0,
 &\|B'(s)\|_{\rm op}&\le4R|s|+4R^3\sqrt q\,|s|.
 \end{aligned}
 \tag{17}
\]

For the last bound, the scalar derivative of \(\|h\|_2^2/q\) is at
most \(2R|s|\). The two differentiated \(W\) factors contribute at
most another \(2R|s|\). Finally,
\(\|D'\|_{\rm op}\le4\|u'\|_\infty
\le4R\sqrt q\,|s|\), producing the last term in (17).

Differentiate (15), bound its three terms by Cauchy--Schwarz, and use (17):

\[
 \begin{aligned}
 |F''(s)|
 &\le 2B_0|s|+2B_0(1+2B_0)|s|
       +4R|s|^3+4R^3\sqrt q\,|s|^3\\
 &\le H:=4B_0+4B_0^2+4R+4R^3
 \qquad (|s|\le q^{-1/2}).
 \end{aligned}
 \tag{18}
\]

Also, \(0\le F'(s)\le1+B_0\) there. The chain rule in physical time
now gives the exact identity

\[
 \frac{d^2}{dt^2}f_q(t,x_1)
 =4F''(s)[y-F(s)]^2-4F'(s)^2[y-F(s)].
\]

Using (16), (18), and \(|y|\le1\), define

\[
 C=4H+4(1+B_0)^2,
\]

to obtain the uniform bound

\[
 |\partial_t^2f_q(t,x_1)|\le C|y|
 \qquad\left(0\le t\le\frac1{2\sqrt q}\right).
 \tag{19}
\]

The potentially growing factor \(\sqrt q\) in (17) is controlled by
the shrinking interval \(|s|\le q^{-1/2}\). No bound on the maximum
initial first-layer coordinate is required.

## 4. From the slope fluctuation to a prediction separation

At zero physical time only the readout moves, so

\[
 f_q(0,x_1)=0,\qquad \partial_tf_q(0,x_1)=2y\kappa_q.
 \tag{20}
\]

The integral remainder formula and (19) imply, on the operator-norm event,

\[
 |f_q(t,x_1)-2y\kappa_qt|\le\tfrac12C|y|t^2
 \quad\left(0\le t\le\frac1{2\sqrt q}\right).
\]

On the joint event (11), subtraction of the two expansions yields

\[
 |f_q^{[1]}(t,x_1)-f_q^{[2]}(t,x_1)|
 \ge\frac{2|y|a}{\sqrt q}t-C|y|t^2.
\]

Since \(a<1\) and \(C>2\), the deterministic choice
\(t=t_q=a/(C\sqrt q)\) lies in the required interval. Substitution
gives \(a^2|y|/(Cq)\). Event (11) has probability at least \(p_0\),
proving (1).

## 5. Why one independent dense reference gives a contradiction

Let \(q=q(n)=o(\sqrt n)\), and fix any finite error constant \(K\).
Couple one dense width-\(n\) run \(f_n\) with two mutually independent
ordinary width-\(q\) runs, both independent of the dense run. Let
\(S_i\) denote the claimed success event

\[
 \sup_{t\ge0,\ \|x\|_2=\sqrt d}
 |f_q^{[i]}(t,x)-f_n(t,x)|\le\frac K{\sqrt n}.
\]

Any guarantee that also includes the endpoint implies this event, so it
can only be stronger. On \(S_1\cap S_2\), the triangle inequality gives

\[
 |f_q^{[1]}(t_q,x_1)-f_q^{[2]}(t_q,x_1)|\le\frac{2K}{\sqrt n}.
\]

For all sufficiently large \(n\),
\(a^2|y|/(Cq)>2K/\sqrt n\). Thus the separation event (1) is
contained in \(S_1^c\cup S_2^c\). Each pair
\((f_q^{[i]},f_n)\) has the required independent initialization law,
and the two failure probabilities are equal. It follows that

\[
 \mathbb P(S_i^c)\ge p_0/2.
 \tag{21}
\]

Equivalently, a success claim with failure probability
\(\delta<p_0/2\) and any finite constant
\(K=C_{\mathrm{data},\delta}\) contradicts (21). Conditional
independence of the success events is neither asserted nor needed; the
union bound is sufficient.

This proof uses no property of the dense run except that the same
independent reference is used in both comparisons. In particular, it does
not assume the existence, uniqueness, concentration, or long-time
convergence of any dense population limit.

## Scope and author check

The obstruction applies to ordinary iid small networks with the specified
gradient flow. It diagnoses why that qualitative small-network baseline
cannot supply the requested precision with polylogarithmic width. It does
not resolve the existence of a specially designed compact initialization.
Law-derived deterministic coefficients, suitable quadrature, altered
architectures or optimizers, and other admissible constructions remain
outside the theorem.

Internal checks performed:

- The input normalization makes each initial training preactivation exactly
  standard Gaussian for every \(d\); no dimension asymptotic is used.
- The loss has no factor one-half, so the initial slope is
  \(2y\kappa_q\), and the feature-feedback equation has the factor two.
- The Gaussian dependence between hidden rows and their activations is
  handled by conditioning on the first hidden vector, not discarded.
- The fourth-moment estimate includes both first-layer empirical-variance
  fluctuations and second-layer conditional sampling fluctuations.
- The fluctuation and matrix-norm events are combined by subtraction, not
  by an invalid independence claim.
- All constants \(a,C,p_0\) are explicitly defined, strictly positive,
  finite, and independent of width and data. The discrepancy constant is
  proportional to the fixed nonzero \(|y|\).
- Curvature control is only claimed on its proved shrinking physical-time
  interval. This is sufficient because a full-time comparison includes that
  interval and its deterministic test time.
- The common-reference argument uses only equal marginal failure
  probabilities and a union bound. No dense-limit theorem is hidden in it.
- This is an internal author check, not an independent review, and the
  frozen source hash is reported separately after the final edit.
