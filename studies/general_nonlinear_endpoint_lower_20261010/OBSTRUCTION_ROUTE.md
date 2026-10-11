# Endpoint obstruction route

Status: no admissible counterexample obtained. The universal endpoint claim
remains open in this route. The results below rule out several proposed
obstructions and identify a precise remaining proof obligation; they do not
prove the claim for the trained deep network.

This is a scoped theoretical investigation. Its scientific input is the setup
in `paper/compact.tex`, together with the supervisor's assumptions and later
clarification of the observable. No other study, experiment, or paper input
file was read. The canonical-notation, rigorous-mathematics, and
conjecture-investigation instructions were applied.

## Target and scope

Write \(v_a=x_a/\sqrt d\) for the unit training directions. The network is

\[
z^{(1)}(x)=W^{(1)}v,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
f_n(x)=n^{-1}w^\top h^{(L)}(x).
\]

Initialization and the all-hidden-trained flow are exactly those of
`cp:network`--`cp:flow`: first-layer entries have variance one, later hidden
entries have variance \(1/n\), and \(w(0)=0\). The loss is

\[
\mathcal L=\frac1m\sum_{a=1}^m(f_n(x_a)-y_a)^2.
\]

Each activation is nonaffine, holomorphic on the specified common strip, and
has bounded first derivative there. The labels are nonzero and satisfy the
existing small-label cap; the population training Gram has positive gap.
The training directions are distinct up to sign. No rank restriction is
placed on their span.

Let \(U\) be the fixed region of unit directions separated by the prescribed
positive distance from every \(v_a\) and \(-v_a\), and assume that \(U\) has
nonempty relative interior. The clarified main target is the existence of
positive fixed-problem constants \(c,p\) such that

\[
\liminf_{n\to\infty}
\Pr\!\left\{
\sup_{v\in U}|f_n(\infty,\sqrt d\,v)
 -\widetilde f_n(\infty,\sqrt d\,v)|\ge\frac c{\sqrt n}
\right\}\ge p.
\]

The two runs are independent. Endpoint existence must be included in the
assertion, as in the source's failure convention. The originally assigned
fixed-query claim is stronger and is not needed to establish this supremum
claim. Every statement below about a single query uses a fixed \(v\in U\).

## An exact nondegeneracy fact

The initial population feature Gram is strictly positive definite after
adjoining any fixed separated query. This remains true when the training
directions span all of \(\mathbb R^d\).

To prove it, consider any finite list of unit directions

\[
u_1,\ldots,u_M,\qquad |u_i^\top u_j|<1\quad(i\ne j).
\]

Let \(G\sim\mathcal N(0,I_d)\), and let \(\phi\) be a nonaffine activation
satisfying the strip and bounded-derivative assumptions. Suppose

\[
\mathbb E\left[\left(\sum_{i=1}^M b_i\phi(G^\top u_i)\right)^2\right]=0.
\]

The Gaussian density is positive everywhere and the summand is continuous,
so \(\sum_i b_i\phi(g^\top u_i)=0\) for every \(g\in\mathbb R^d\).
Expand the real analytic function at zero. For every integer \(k\) with
\(\phi^{(k)}(0)\ne0\), differentiation in a scalar multiplier gives

\[
\sum_{i=1}^M b_i(g^\top u_i)^k=0
\quad\text{for every }g\in\mathbb R^d.
\]

Such \(k\) are unbounded. Otherwise the Taylor series is a polynomial near
zero, analytic continuation makes \(\phi\) that polynomial on the real axis,
and the bounded derivative makes it affine, a contradiction. Set \(g=u_j\)
and take any sequence of these \(k\) tending to infinity. Since the diagonal
inner product is one and all other inner products have absolute value less
than one, the displayed identity tends to \(b_j=0\). Thus all \(b_i=0\),
which proves strict positivity of the first-layer feature Gram.

For later layers a simpler argument suffices. If \(Z\in\mathbb R^M\) is
Gaussian with positive definite covariance and

\[
\mathbb E\left[\left(\sum_i b_i\phi_\ell(Z_i)\right)^2\right]=0,
\]

then full Gaussian support implies \(\sum_i b_i\phi_\ell(z_i)=0\) for
every \(z\in\mathbb R^M\). Vary only \(z_j\). Nonconstancy of
\(\phi_\ell\) gives \(b_j=0\). Applying this argument recursively proves
strict positive definiteness at every layer, including \(L-1\) and \(L\),
for the training directions together with the query.

In particular, if \(Q_{\rm aug}^{(L-1)}\) denotes this \((m+1)\)-by-
\((m+1)\) covariance, the conditional variance of its query Gaussian
coordinate given all training coordinates is strictly positive. Initial
linear input rank deficiency does not prevent this conclusion.

## A fully resolved auxiliary endpoint calculation

The following auxiliary model freezes independent features drawn from the
population last-layer Gaussian law. It is not the canonical trained-hidden
network. Its purpose is to test the suggested obstruction that interpolation
or full-span training already removes endpoint fluctuations.

Let \(Z=(Z_1,\ldots,Z_m,Z_q)\) be centered Gaussian with covariance
\(Q_{\rm aug}^{(L-1)}\), and define

\[
H=(\phi_L(Z_1),\ldots,\phi_L(Z_m))^\top,\qquad
H_q=\phi_L(Z_q),
\]

\[
Q=\mathbb E[HH^\top],\qquad k=\mathbb E[HH_q],\qquad
\alpha=Q^{-1}y,\qquad b=Q^{-1}k.
\]

Here \(Q\) is positive definite, and \(\alpha\ne0\). Let

\[
X=(\alpha^\top H)(H_q-b^\top H).
\]

Then \(\mathbb E X=\alpha^\top(k-Qb)=0\), and

\[
\operatorname{Var}(X)
\ge
\mathbb E\left[(\alpha^\top H)^2
 \operatorname{Var}(H_q\mid Z_1,\ldots,Z_m)\right]>0.
\]

The strict inequality has two separate justifications. First, the conditional
law of \(Z_q\) has positive variance for every value of the training Gaussian
coordinates. A nonconstant continuous activation therefore has positive
variance under that law: variance zero would force the activation to be
constant on the full real line. Second,
\(\mathbb E(\alpha^\top H)^2=\alpha^\top Q\alpha>0\).
All moments used here are finite because bounded derivative implies at most
linear growth.

For \(n\) independent copies of \((H,H_q)\), put

\[
Q_n=\frac1n\sum_{i=1}^nH_iH_i^\top,\qquad
k_n=\frac1n\sum_{i=1}^nH_iH_{q,i},\qquad
\widehat f_n=k_n^\top Q_n^{-1}y.
\]

This is the fitted predictor obtained by readout gradient flow from zero
when the features are frozen. By the finite-dimensional law of large numbers,
\(Q_n\to Q\) in probability, so \(Q_n\) is invertible with probability
tending to one. Finite fourth moments give
\(Q_n-Q=O_{\mathbb P}(n^{-1/2})\) and
\(k_n-k=O_{\mathbb P}(n^{-1/2})\). Expanding the inverse at the positive
definite matrix \(Q\) yields

\[
\widehat f_n-k^\top Q^{-1}y
=\frac1n\sum_{i=1}^nX_i+O_{\mathbb P}(n^{-1}).
\]

Indeed, the linear terms are
\((k_n-k)^\top\alpha-b^\top(Q_n-Q)\alpha\), exactly the displayed
sample mean. The scalar independent central limit theorem applies because
the \(X_i\) have mean zero and finite positive variance \(\sigma^2\).
Consequently two independent copies satisfy

\[
\sqrt n(\widehat f_n-\widetilde{\widehat f}_n)
\ \Longrightarrow\ \mathcal N(0,2\sigma^2),\qquad \sigma^2>0.
\]

Thus this auxiliary fitted endpoint has a positive-probability
\(n^{-1/2}\) lower bound at every fixed separated query. Interpolation,
special nonzero label directions, and full-span training do not furnish
counterexamples even in this simpler setting.

## Why this does not settle trained hidden layers

For completeness, the exact tangent kernel of the canonical flow, using the
source's residual-free backward responses \(\delta^{(\ell)}\), is

\[
\begin{aligned}
K_n(t;x,x_a)
={}&\frac{h^{(L)}(x)^\top h_a^{(L)}}n
 +\frac{\delta^{(1)}(x)^\top\delta_a^{(1)}}n\,v^\top v_a\\
&+\sum_{\ell=2}^L
\frac{\delta^{(\ell)}(x)^\top\delta_a^{(\ell)}}{n^2}
 h^{(\ell-1)}(x)^\top h_a^{(\ell-1)}.
\end{aligned}
\]

This follows by taking parameter derivatives of \(f_n\), multiplying the
first-layer and readout derivative inner products by mobility \(n\), and
the remaining hidden derivative inner products by mobility one. Hence

\[
\dot f_n(t,x)=-\frac2m\sum_aK_n(t;x,x_a)r_a(t),
\]

and whenever the integral converges,

\[
f_n(\infty,x)=-\frac2m\int_0^\infty
 \sum_aK_n(t;x,x_a)r_a(t)\,\mathrm dt.
\]

Both the kernel and the residual path depend on initialization. A positive
variance of the initial kernel or a positive transient fluctuation therefore
does not prove a positive variance of this endpoint integral. At the training
inputs the endpoint fluctuation is exactly zero, demonstrating an actual
cancellation mechanism within the same canonical dynamics.

Replacing the hidden-layer flow by frozen features changes the problem.
Moreover, a width-independent approximation error of order \(Y^3\), even if
available, cannot transfer a lower bound of order \(n^{-1/2}\) at fixed
positive \(Y\). The required comparison must control the fluctuation itself
at the \(n^{-1/2}\) scale and preserve some nonzero component.

There is also a distinction between local dependence on label size and the
specified fixed-label claim. Under the substitution \(y=s y_0\), the exact
flow is invariant under

\[
s\mapsto-s,\qquad w\mapsto-w,\qquad W^{(\ell)}\mapsto W^{(\ell)}.
\]

Uniqueness therefore makes finite-time hidden weights even and the readout
and predictor odd in \(s\). At first order at zero labels, the hidden weights
do not move; the predictor obeys frozen-initial-feature readout training.
This finite-time statement does not justify exchanging differentiation in
\(s\) with the fitted limit. Even if such an exchange and a fluctuation
expansion were proved, a nonzero coefficient at \(s=0\) would not alone prove
nondegeneracy at every allowed positive \(s\). For example, the abstract
analytic coefficient \(s(1-s^2/s_0^2)\) has nonzero derivative at zero and
vanishes at \(s=s_0>0\). This example is a logical warning, not a network
counterexample.

The endpoint supremum makes the desired nondegeneracy weaker: it suffices to
retain a fluctuation at one query in \(U\). A proof need not establish a
lower bound for each fixed query. Nevertheless, the same missing comparison
with the trained-hidden endpoint remains.

## Disposition of candidate obstructions

| Candidate | Disposition under the assigned assumptions |
|---|---|
| Zero labels or an affine hidden layer | Explicitly excluded; no relevance to the target. |
| Fitting at a training input or an exact antipodal symmetry | Query separation excludes these witnesses. |
| Full-span training fixes all predictions | False for the auxiliary nonlinear random-feature endpoint; the augmented population Gram is strictly positive definite regardless of input span. |
| Label cancellation makes the random-feature endpoint variance zero | Ruled out by the conditional variance calculation for every nonzero label vector. |
| A nonlinear activation arbitrarily close to affine | May make constants small; this does not contradict positive fixed-problem constants. |
| An empty separated region | Excluded by the clarified nonempty-interior assumption. |
| Hidden-feature learning cancels the full endpoint fluctuation | Not established or ruled out here; this is the substantive unresolved possibility. |

The most useful next theoretical step is a fluctuation-level endpoint formula
for the all-hidden-trained network together with a proof that at least one
component indexed by a query in \(U\) has positive variance. A quantitative
comparison to the positive auxiliary influence above would be sufficient,
but it must be valid at the given fixed-label cap and on the complete
training interval. No admissible counterexample, complete lower-bound proof,
or claim that only routine estimates remain is asserted by this route.
