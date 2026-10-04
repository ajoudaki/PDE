# Fixed-confidence lower bound at the actual one-input fitted endpoint

2026-10-04. Scoped theoretical refinement; internally derived, not an
independent promotion review. This combines the actual nonlinear endpoint
expansion in `INTEGRATED_DENSE_LOWER_ROUTE.md`, Section 6, with the
initialized endpoint-response CLT in `INTEGRATED_INITIAL_VARIABILITY.md`.
The label is fixed before the width grows. No interchange of a zero-label
limit and a width limit is used.

## Statement and model

Fix an input dimension \(d\ge2\), one training input

\[
x_1=\sqrt d\,e_1,\qquad x_*=\sqrt d\,e_2,
\]

and a deterministic scalar label \(y\ne0\). The two hidden layers have
width \(n\), with parameters \(A=W^{(1)}\in\mathbb R^{n\times d}\),
\(W=W^{(2)}\in\mathbb R^{n\times n}\), and
\(w=W^{(3)}\in\mathbb R^n\). Define the forward map and loss by

\[
h^{(1)}(t,x)=\tanh(A(t)x/\sqrt d),\quad
h^{(2)}(t,x)=\tanh(W(t)h^{(1)}(t,x)),\quad
f_n(t,x)=\frac1n w(t)^\top h^{(2)}(t,x),
\]
\[
r(t)=f_n(t,x_1)-y,\qquad \mathcal L(t)=r(t)^2.
\]

With \(h^{(\ell)}=h^{(\ell)}(t,x_1)\), the canonical mobilities
\((n,1,n)\) give the exact dense equations

\[
\begin{aligned}
\delta^{(2)}&=w\odot\tanh'(Wh^{(1)}),&
\delta^{(1)}&=\tanh'(Ae_1)\odot W^\top\delta^{(2)},\\
\dot A&=-2r\delta^{(1)}e_1^\top,&
\dot W&=-\frac{2r}{n}\delta^{(2)}h^{(1)\top},&
\dot w&=-2r h^{(2)}.
\end{aligned}
\tag{1}
\]

The entries of \(A(0)\) are independent \(N(0,1)\), the entries of
\(W(0)\) are independent \(N(0,1/n)\), the two matrices are independent,
and \(w(0)=0\). Tildes denote a second independent initialization and
dense trajectory for the same datum.

For a standard Gaussian \(Z\sim N(0,1)\), define the fixed activation
moments

\[
Q=\mathbb E\tanh^2 Z,\qquad
q=\mathbb E\tanh^2(\sqrt Q\,Z),\qquad
g_0=\frac12\mathbb E\tanh^2(\sqrt{Q/2}\,Z).
\tag{2}
\]

All three are strictly positive and less than one. The limiting training
Gram is \(q\), so its unnormalized gap is \(\gamma=q\).

**Theorem.** For every fixed confidence parameter \(0<\delta<1\), set

\[
y_\delta=\frac{g_0^2\delta^{3/4}}{\sqrt{144000}}.
\tag{3}
\]

For every deterministic label \(0<|y|\le y_\delta\), and all sufficiently
large \(n\), with probability at least \(1-\delta\), both actual dense
trajectories converge, fit the training label exactly, and satisfy

\[
\left|f_n(\infty,x_*)-\widetilde f_n(\infty,x_*)\right|
\ge \frac\delta4\frac{|y|}{\sqrt n}.
\tag{4}
\]

Here convergence includes all parameters, and the endpoint predictions
are their actual limits. The sufficient width threshold can be chosen
as a function of \(\delta\) alone for this model. Its training-event part
is explicit below; its CLT part is qualitative. This is a probability
bound for each deterministic admissible label, without a claim that one
event simultaneously works for every label. Every constant in (2)--(4)
is independent of width and physical time.

The proof first retains the full nonlinear endpoint remainder, then
uses the initialized-response CLT only for its leading term, and finally
subtracts the two quantified failure probabilities and the training-event
failure. The two initializations must be independent.

## The actual endpoint and its complete nonlinear remainder

Let \(a_0=A(0)e_1\), \(W_0=W(0)\), and define the initialized training
features and their Gram by

\[
h_0^{(1)}=\tanh a_0,\qquad
h_0^{(2)}=\tanh(W_0h_0^{(1)}),\qquad
G_n=\frac1n\|h_0^{(2)}\|_2^2.
\]

The training sigma-field is \(\mathcal F=\sigma(a_0,W_0)\). Define its
good event

\[
\mathcal T=\{\|W_0\|_{\rm op}\le10,\ G_n\ge g_0\},
\qquad c_W=100/8-2\log9>0.
\]

The Gaussian matrix-net estimate and two bounded-variable concentration
estimates give

\[
\Pr(\mathcal T^c)
\le2e^{-c_Wn}+e^{-nQ^2/2}+e^{-2ng_0^2}.
\tag{5}
\]

For the last two terms, the lower-feature squared RMS is at least
\(Q/2\) except with probability \(e^{-nQ^2/2}\). Conditionally on
that feature vector, the top preactivations are independent Gaussians
whose variance is at least \(Q/2\), hence whose squared tanh expectation
is at least \(2g_0\). The probability that their empirical average
falls below \(g_0\) is at most \(e^{-2ng_0^2}\). For the first term,
two \(1/4\)-nets of cardinality at most \(9^n\), the inequality
\(\|W_0\|_{\rm op}\le2\max_{u,v}|u^\top W_0v|\), and the scalar
Gaussian tail give \(2\exp[-(100/8-2\log9)n]\).

We recall the direct endpoint construction to identify what (5)
guarantees. Suppose first that \(y>0\), and put
\(u(t)=2\int_0^t(y-f_n(s,x_1))\,ds\). Up to its fitting point,
the feature-clock path solves the autonomous equations

\[
\frac{da}{du}=\delta^{(1)},\qquad
\frac{dW}{du}=\frac1n\delta^{(2)}h^{(1)\top},\qquad
\frac{dw}{du}=h^{(2)}.
\tag{6}
\]

On \(\mathcal T\), direct integration for \(0\le u\le1\) gives

\[
\|w(u)\|_\infty\le u,\qquad
\|W(u)-W_0\|_{\rm op}\le u^2/2,\qquad
\frac{\|a(u)-a_0\|_2}{\sqrt n}\le\frac{11}2u^2,
\]
\[
\frac{\|h^{(2)}(u)-h_0^{(2)}\|_2}{\sqrt n}\le61u^2.
\tag{7}
\]

Indeed \(\|w\|_2/\sqrt n\le u\), the mixer speed is at most
\(u\), and \(\|W\|_{\rm op}\le11\). The normalized speed of
\(a\) is at most \(11u\); differentiating the top feature bounds its
normalized speed by \(u+121u=122u\). These estimates also rule out a
finite parameter escape on this clock interval.

Set \(u_0=g_0^{1/4}/16\). Since \(61/256<1/4\), (7) keeps the
top-feature squared RMS above \(g_0/2\) on \([0,u_0]\). Directly
differentiating the training prediction along (6) gives

\[
\frac{df_n(u,x_1)}{du}
=\frac{\|h^{(2)}\|_2^2}{n}
 +\frac{\|\delta^{(1)}\|_2^2}{n}
 +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
\ge g_0/2.
\tag{8}
\]

For \(y\le g_0^{5/4}/32\), there is a unique fitted clock value
\(0<u_\infty\le2y/g_0\le u_0\). The scalar physical ODE
\(\dot u=2(y-f_n(u,x_1))\), starting at zero, stays below this value
and converges to it. In particular
\(0<y-f_n(t,x_1)\le ye^{-g_0t}\), so (6) supplies the actual
parameter endpoint and exact fitting. The cap (3) satisfies the needed
restriction because \(g_0\le1\), \(\delta<1\), and
\(\sqrt{144000}>32\).

Integration of the last equation in (6), and then interpolation, yield

\[
\frac{\|w_\infty-u_\infty h_0^{(2)}\|_2}{\sqrt n}
\le\frac{61}3u_\infty^3,\qquad
|y-u_\infty G_n|\le\frac{244}3u_\infty^3.
\]

The second inequality splits the fitted inner product into its readout
error and feature error, bounded respectively by
\((61/3)u_\infty^3\) and \(61u_\infty^3\). Since \(G_n\ge g_0\),
these imply

\[
\frac{\|w_\infty-(y/G_n)h_0^{(2)}\|_2}{\sqrt n}
\le\frac{2440}{3g_0^4}y^3,\qquad
\|W_\infty-W_0\|_{\rm op}\le\frac{2y^2}{g_0^2}.
\tag{9}
\]

Only the first column of \(A\) changes during training. Thus
\(g=A(0)e_2=A(t)e_2\sim N(0,I_n)\) is independent of the entire
training path, including its endpoint. Define the initialized
train-query Gram entry by

\[
\kappa_n(g)=\frac1n h_0^{(2)\top}\tanh(W_0\tanh g).
\]

On \(\mathcal T\), the exact query decomposition is

\[
f_n(\infty,x_*)=\frac{y\kappa_n(g)}{G_n}+R_n(g).
\tag{10}
\]

Both terms defining \(R_n\) are odd in \(g\), so its conditional
Gaussian mean is zero. To retain the width normalization in the error,
differentiate the query function itself:

\[
\nabla_g\!\left[\frac1n w^\top\tanh(W\tanh g)\right]
=\frac1n\operatorname{diag}(\tanh'g)W^\top
 [w\odot\tanh'(W\tanh g)].
\tag{11}
\]

Subtracting the expression with \(W=W_0\) and
\(w=(y/G_n)h_0^{(2)}\) gives the readout, mixer, and top-gate error
terms. Bounds (9), \(\|W_\infty\|_{\rm op}\le11\),
\(\|W_0\|_{\rm op}\le10\), \(|\tanh'|\le1\), and
\(|\tanh''|\le2\) bound their norms by, respectively,

\[
\frac{11\cdot2440}{3g_0^4}\frac{y^3}{\sqrt n},\qquad
\frac2{g_0^3}\frac{y^3}{\sqrt n},\qquad
\frac{40}{g_0^3}\frac{y^3}{\sqrt n}.
\]

Their sum is below \(9000y^3/(g_0^4\sqrt n)\). Conditional Gaussian
Poincare, \(\operatorname{Var}_g U\le\mathbb E_g\|\nabla_gU\|_2^2\),
applies to the smooth bounded query remainder. Its mean vanishes, hence

\[
\mathbb E_g[R_n(g)^2\mid\mathcal F]
\le \frac{9000^2y^6}{g_0^8n}\qquad\hbox{on }\mathcal T.
\tag{12}
\]

The Gaussian Poincare inequality used here is the same as in the complete
lower-route proof: in a Gaussian Hermite expansion, variance sums the
squared nonconstant coefficients and mean squared gradient multiplies
each by its positive total degree. Gaussian Sobolev approximation gives
the inequality for this smooth bounded function with bounded gradient.

For negative \(y\), the transformation \((y,w)\mapsto(-y,-w)\)
leaves the hidden physical path unchanged and reverses all predictions.
Thus (9)--(12) hold with absolute values where appropriate and the same
constants. No endpoint is asserted outside \(\mathcal T\).

## The initialized leading term has a nondegenerate Gaussian limit

Put

\[
a_2=\mathbb E\tanh'(\sqrt Q\,Z),\qquad
\nu_2=q^2+a_2^4Q^2.
\tag{13}
\]

The specialized initialized Gram CLT is

\[
\sqrt n\,\kappa_n\ \Longrightarrow\ N(0,\nu_2),\qquad
G_n\longrightarrow q\quad\hbox{in probability}.
\tag{14}
\]

To see its hypotheses and variance explicitly, the initialized lower
train-query Gram is an average of the iid bounded products
\(\tanh(a_{0i})\tanh(g_i)\), which have mean zero and variance
\(Q^2\). The two lower diagonal Gram entries converge to \(Q\),
and the whole lower Gram fluctuates at order \(n^{-1/2}\). Conditional
on both lower-feature columns, the top preactivation rows are iid
two-dimensional Gaussians with this empirical covariance. At covariance
\(QI_2\), the top product's variance is \(q^2\). Its conditional
mean has derivative \(a_2^2\) in the off-diagonal covariance and zero
derivatives in the two diagonal directions: the latter expressions
contain the zero odd-feature expectation of the other coordinate.

The covariance derivative follows by differentiating the Gaussian
density and integrating by parts twice; all tanh derivatives and
products involved are bounded. Taylor expansion near \(QI_2>0\)
therefore propagates the lower off-diagonal fluctuation with coefficient
\(a_2^2\). For the top centered innovation, the conditional
characteristic function of one summand, scaled by \(n^{-1/2}\), is
\(1-t^2q^2/(2n)+o_P(n^{-1})\); bounded summands control the cubic
remainder. Its \(n\)-th power tends to \(e^{-t^2q^2/2}\).
Boundedness of characteristic functions upgrades this conditional
convergence to \(L^1\), showing that the top innovation and lower
Gaussian fluctuation are independent in the limit. Adding their
variances gives exactly (13)--(14). This is the two-layer specialization
of the complete CLT proof in the initialized-variability source.

Here \(G_n>0\) almost surely: the lower training vector is nonzero
almost surely, and conditioned on it every top preactivation has a
continuous nondegenerate Gaussian law. Thus the ratio below is defined
almost surely. Division by \(G_n\to q>0\), followed by independence
of the two networks, gives

\[
\sqrt n\left(\frac{\kappa_n}{G_n}
 -\frac{\widetilde\kappa_n}{\widetilde G_n}\right)
\ \Longrightarrow\ N(0,\sigma^2),\qquad
\sigma^2=\frac{2\nu_2}{q^2}\ge2.
\tag{15}
\]

No second-moment convergence or assertion about Gaussian trained
predictions is needed. Formula (15) applies solely to the initialized
quantity in the leading term of the exact identity (10).

## Probability losses and the width threshold

Write \(\widetilde{\mathcal T}\) for the second network's training
event. Extend \(R_n\) by zero outside \(\mathcal T\) solely for
probability calculations; this convention defines no fitted predictor
on the exceptional event. Oddness in the independent query column gives
\(\mathbb E[R_n\mathbf1_{\mathcal T}]=0\). The independent-copy
cross term therefore vanishes, and (12) implies

\[
\mathbb E[(R_n-\widetilde R_n)^2
             \mathbf1_{\mathcal T\cap\widetilde{\mathcal T}}]
=2\Pr(\mathcal T)\mathbb E[R_n^2\mathbf1_{\mathcal T}]
\le\frac{2\cdot9000^2y^6}{g_0^8n}.
\tag{16}
\]

Let the two-copy leading difference and its test threshold be

\[
D_n^{\rm lin}=y\left(\frac{\kappa_n}{G_n}
 -\frac{\widetilde\kappa_n}{\widetilde G_n}\right),\qquad
b_n=\frac{\delta|y|}{2\sqrt n}.
\]

The density of \(N(0,\sigma^2)\) is bounded by
\(1/(\sigma\sqrt{2\pi})\). Equation (15) and its zero-probability
boundary at \(\pm\delta/2\) imply

\[
\lim_{n\to\infty}\Pr\{|D_n^{\rm lin}|\le b_n\}
\le\frac{\delta}{\sigma\sqrt{2\pi}}
\le\frac{\delta}{2\sqrt\pi}<\frac\delta2.
\tag{17}
\]

Consequently there exists a qualitative threshold \(n_{\rm CLT}(\delta)\)
such that this finite-width probability is at most \(\delta/2\) for
all larger widths. The normalized event in (17) does not depend on
\(y\ne0\), so this threshold is uniform over the labels in (3).

Markov's inequality applied to (16) gives the nonlinear remainder loss

\[
\begin{aligned}
\Pr\{|R_n-\widetilde R_n|\ge b_n/2,
                   \ \mathcal T\cap\widetilde{\mathcal T}\}
&\le\frac{32\cdot9000^2|y|^4}{g_0^8\delta^2}\\
&\le\frac\delta8,
\end{aligned}
\tag{18}
\]

where the last step substitutes
\(y_\delta^4=g_0^8\delta^3/144000^2\) and uses
\(32\cdot9000^2/144000^2=1/8\).

The union bound in (5) makes the joint training-event failure at most
\(\delta/8\) whenever

\[
n\ge
\max\left\{\frac1{c_W},\frac2{Q^2},\frac1{2g_0^2}\right\}
\log\frac{64}{\delta}.
\tag{19}
\]

Indeed each of the three exponentials in (5) is then at most
\(\delta/64\), and the two-copy coefficients sum to eight.
Take \(n\) at least the ceiling of (19) and at least
\(n_{\rm CLT}(\delta)\). Outside the three failure events in
(17)--(19), both networks fit and converge, and (10) yields

\[
|f_n(\infty,x_*)-\widetilde f_n(\infty,x_*)|
\ge |D_n^{\rm lin}|-|R_n-\widetilde R_n|
>b_n/2=\frac\delta4\frac{|y|}{\sqrt n}.
\]

The total failure bound is \(\delta/2+\delta/8+\delta/8=3\delta/4\),
which is at most \(\delta\). This proves (4), including convergence
and fitting on the same probability event. Only the two selected columns
of \(A\) enter any law or estimate, so this threshold is independent
of \(d\ge2\). ∎

## Scope and checks

The theorem gives an actual fitted-endpoint lower bound at each fixed
confidence, with a label cap independent of width. The label is never
taken to zero after width growth. Its cap shrinks as \(\delta^{3/4}\)
because (18) controls a cubic remainder relative to a linear small-ball
threshold by a second moment; neither this exponent nor the constants
are claimed optimal.

At \(\delta=1/4\), for example, the coefficient in (4) is \(1/16\)
at confidence at least \(3/4\), for every fixed nonzero label under
(3) and all sufficiently large widths. The all-time, whole-sphere
discrepancy is at least this endpoint difference: its supremum dominates
the limit along the fixed query \(x_*\). This implication requires no
uniform convergence in the query variable.

This refinement is restricted to one training input, two tanh hidden
layers, independent canonical initializations, and an orthogonal
untouched query column. It proves no fitted-endpoint theorem for
general sample count, general activations, or coupled initializations.
It proves no fixed-label CLT for the nonlinear endpoint and supplies no
population-bias estimate. A training-point query would instead give an
identically zero endpoint discrepancy on the fitting event.

The readout error coefficient and probability arithmetic were checked
exactly: \(11\cdot2440/3+2+40=26966/3<9000\),
\(32\cdot9000^2/144000^2=1/8\), and the three allocated failure
fractions sum to \(3/4\). No numerical training experiment was used.

The complete allowed scientific inputs read were the following files
in this study. The corresponding hashes identify the revisions used.

| Source | SHA-256 |
|---|---|
| `INTEGRATED_DENSE_LOWER_ROUTE.md` | `8069187d94d4b90acfaa1406b1ccbd6961a24c2fc6d21de8d9a3a651c1e16200` |
| `INTEGRATED_INITIAL_VARIABILITY.md` | `97cdb707c082acf1579e3f73fea6d448e6941a0a06e98568fc4383b3f93a5c6d` |
| `INTEGRATED_COMPARISON_CHECK.md` | `e5c4281030648c0e25792a09e55227e943b7a2dd5a326978701880c16aacbd21` |
| `INTEGRATED_INITIAL_VARIABILITY_CHECK.md` | `59dccafe35e9aabdae786c568f49916a2ca054c3cb55f9c603d1dd2a5d743938` |
| `INTEGRATED_LOWER_CONFIDENCE.md` | `f0e6941471bf29c56e02e9a0997326e7526ecc27a495fe2723b3ac2b4b65a5c7` |

Required process inputs were the canonical-notation skill and its neural
reference, and the rigorous-math skill. The comparison check contains
discussion of other scientific sources; those sources were not opened,
and none of their upper-bound claims is a premise here. Only this
assigned report was written; no maintained book, code, README, or Git
index was changed.
