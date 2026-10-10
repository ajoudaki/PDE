# Fixed sample modes: a gap-free, all-time mechanism and its limits

Scope: independent prompt-only mathematical subtask, 2026-10-10. Scientific
inputs were the supervisor's assignment only. Required process and mathematical
presentation skills were read; no book, paper, other route, other study, or
external scientific source was inspected. The statements below are derived
here, conditional on their displayed hypotheses, and await supervisor checking.
They are not claims about the actual paper's network. No experiment was run.

The useful positive mechanism is fixed invariant sample subspaces. A positive
lower bound on every residual-decay rate is unnecessary for uniform-in-time
prediction approximation. Smooth labels help only when their small tail is
measured in those invariant subspaces. Pointwise small mode mixing does not
replace invariance over an infinite training horizon.

## 1. Residual dynamics and normalization

Let the training set consist of inputs \(x_a\) and real labels \(y_a\),
\(a=1,\ldots,m\). For sample vectors define

\[
\langle u,v\rangle_m=\frac1m\sum_{a=1}^m u_av_a,
\qquad \|u\|_m=\sqrt{\langle u,u\rangle_m}.
\]

Consider zero-initial-output sample predictions \(f(t)\in\mathbb R^m\), with
residual \(r(t)=f(t)-y\), satisfying

\[
\dot f(t)=A(t)(y-f(t)),\qquad f(0)=0,
\qquad \dot r(t)=-A(t)r(t),\quad r(0)=-y.
\tag{1}
\]

Here \(A(t)\) is a locally integrable, symmetric positive semidefinite
\(m\times m\) matrix for almost every \(t\ge0\). These assumptions give an
absolutely continuous solution on each finite interval. Write \(U(t,s)\)
for its residual evolution operator. For any solution \(v\) of
\(\dot v=-A(t)v\),

\[
\frac{d}{dt}\|v(t)\|_m^2
=-2\langle v(t),A(t)v(t)\rangle_m\le0.
\]

Consequently \(\|U(t,s)\|_{m\to m}\le1\) for \(t\ge s\), and

\[
f(t)=(I-U(t,0))y.
\tag{2}
\]

For a differentiable nonlinear network \(f(x;\theta)\), Euclidean gradient
flow of \(\mathcal L(\theta)=(2m)^{-1}\sum_a(f(x_a;\theta)-y_a)^2\)
indeed has (1), with

\[
A_{ab}(t)=\frac1m\left\langle
\nabla_\theta f(x_a;\theta(t)),
\nabla_\theta f(x_b;\theta(t))\right\rangle.
\tag{3}
\]

Equation (3) alone gives neither fixed modes nor an autonomous reduced model:
its entries can require the full evolving network. In the comparisons below,
\(A(t)\) is the same prescribed coefficient path in both sample systems.
Comparing two independently trained nonlinear networks additionally requires
controlling how their coefficient paths differ.

## 2. Exact diagonal modes and a weaker invariant-block version

Assume a fixed empirically orthonormal basis \(\psi_1,\ldots,\psi_m\)
diagonalizes every \(A(t)\):

\[
\langle\psi_j,\psi_k\rangle_m=\delta_{jk},
\qquad A(t)\psi_j=\lambda_j(t)\psi_j,
\qquad \lambda_j(t)\ge0.
\]

Define the label coefficient \(y_j=\langle y,\psi_j\rangle_m\), the cumulative
rate \(\Lambda_j(t)=\int_0^t\lambda_j(s)\,ds\), and the orthogonal projection
\(P_Ry=\sum_{j\le R}y_j\psi_j\). Set \(Q_R=I-P_R\). Solving the scalar
equations in (1) yields

\[
f(t)=\sum_{j=1}^m(1-e^{-\Lambda_j(t)})y_j\psi_j,
\qquad
f_R(t)=\sum_{j\le R}(1-e^{-\Lambda_j(t)})y_j\psi_j.
\tag{4}
\]

Since each multiplier belongs to \([0,1]\), orthonormality gives

\[
\sup_{t\ge0}\|f(t)-f_R(t)\|_m^2
\le\sum_{j>R}|y_j|^2=\|Q_Ry\|_m^2.
\tag{5}
\]

No lower bound on any \(\lambda_j(t)\) was used. Rates may vanish identically,
tend to zero with \(m\), or have finite time integral. This is a prediction
approximation bound, not a guarantee of fitting the labels. It is sharp when
all omitted modes with nonzero labels have \(\Lambda_j(t)\to\infty\).

An ordering by smoothness need not be an ordering by \(\lambda_j(t)\): the
requirement is that the smoothness basis consists of fixed dynamic modes.

There is also a useful weaker hypothesis. Let a fixed orthogonal projection
\(P\) satisfy \(PA(t)=A(t)P\) for all times, without requiring commutation of
the matrices at different times. Put \(Q=I-P\). Both subspaces are invariant,
so \(Pf(t)\) solves the retained equation and

\[
Qf(t)=(I-U_Q(t,0))Qy,
\qquad \sup_{t\ge0}\|Qf(t)\|_m\le2\|Qy\|_m.
\tag{6}
\]

Here \(U_Q\) is the contractive residual evolution inside \(Q\mathbb R^m\).
The factor two follows from the triangle inequality. Its replacement by one
does not follow from contraction alone, because a time-varying noncommuting
evolution need not be self-adjoint positive semidefinite. Thus noncommutation
within an invariant discarded block preserves a uniform bound; coupling
between retained and discarded subspaces is the substantive obstruction.

## 3. What smooth or analytic modal labels buy

All constants in this section must hold uniformly in \(m\) to establish
sample-count-independent retained dimension. Suppose positive increasing
frequency weights \(\mu_j\) and a regularity exponent \(s>0\) satisfy

\[
\sum_{j=1}^m\mu_j^{2s}|y_j|^2\le M^2.
\tag{7}
\]

For \(R<m\),

\[
\sup_t\|f(t)-f_R(t)\|_m
\le M\mu_{R+1}^{-s}.
\tag{8}
\]

This follows by bounding every \(\mu_j^{-2s}\) in the omitted sum by
\(\mu_{R+1}^{-2s}\). If \(\mu_j\ge c j^{1/d_{\rm lat}}\), where
\(d_{\rm lat}\) is a fixed positive latent dimension and \(c>0\), a sufficient
retained count at tolerance \(\varepsilon\) is of order
\((Mc^{-s}/\varepsilon)^{d_{\rm lat}/s}\), capped by \(m\). This is independent
of \(m\) at fixed tolerance; a merely low latent dimension does not by itself
prove (7).

For an analytic-type modal assumption

\[
\sum_{j=1}^m e^{2a\mu_j}|y_j|^2\le M^2,
\qquad a>0,
\]

the same argument gives \(M e^{-a\mu_{R+1}}\) in (8). Under the same frequency
growth, \(R=O((\log(M/\varepsilon))^{d_{\rm lat}})\). This is polylogarithmic
in inverse accuracy, not a new dependence on \(m\). If tolerance is required
to decrease polynomially with \(m\), it becomes polylogarithmic in \(m\).

These are assumptions on label coefficients in a dynamically invariant basis.
Smoothness in an unrelated coordinate system does not imply them.

## 4. A whole-input sup bound needs an actual extension model

Suppose the same symbols \(\psi_j(x)\) denote fixed functions on an input set
\(\mathcal X\), with restrictions \(\psi_j(x_a)=(\psi_j)_a\), and suppose the
actual whole-input predictors have the expansion (4), with these fixed
functions. Define \(B_j=\sup_{x\in\mathcal X}|\psi_j(x)|<\infty\). Then

\[
\sup_{t\ge0}\sup_{x\in\mathcal X}|f(t,x)-f_R(t,x)|
\le\sum_{j>R} B_j|y_j|.
\tag{9}
\]

The bound follows term by term from the multipliers in (4) and the triangle
inequality. The displayed weighted \(\ell^1\) tail is the extra control that
upgrades empirical \(L^2\) to a whole-input bound.

Under (7), Cauchy--Schwarz gives the explicit alternative

\[
\sum_{j>R}B_j|y_j|
\le M\left(\sum_{j>R}B_j^2\mu_j^{-2s}\right)^{1/2}.
\tag{10}
\]

For example, if \(B_j\le B\), \(\mu_j\ge c j^{1/d_{\rm lat}}\), and
\(s>d_{\rm lat}/2\), the decreasing-series integral estimate gives

\[
\sup_{t,x}|f(t,x)-f_R(t,x)|
\le MBc^{-s}
\left(\frac{d_{\rm lat}}{2s-d_{\rm lat}}\right)^{1/2}
R^{1/2-s/d_{\rm lat}},\qquad R\ge1.
\tag{11}
\]

Indeed \(\sum_{j>R}j^{-2s/d_{\rm lat}}\le
\int_R^\infty u^{-2s/d_{\rm lat}}du\). For analytic weighted coefficients,
(10) instead uses \(e^{-2a\mu_j}\). The resulting tail is exponentially
small in \(R^{1/d_{\rm lat}}\), up to powers of \(R\), when the mode sup norms
grow at most polynomially. This last assertion can be bounded without an
asymptotic expansion: for \(B_j\le B j^k\) and \(\mu_j\ge c j^{1/d_{\rm lat}}\),

\[
\sum_{j>R}j^{2k}e^{-2acj^{1/d_{\rm lat}}}
\le e^{-ac(R+1)^{1/d_{\rm lat}}}
\sum_{j=1}^{\infty}j^{2k}e^{-acj^{1/d_{\rm lat}}}.
\]

The last series is finite by the substitution \(v=u^{1/d_{\rm lat}}\) in its
integral comparison. Hence the same polylogarithmic retained-count conclusion
holds, with constants depending on \(a,c,k,d_{\rm lat}\).

A sufficient exact realization of (4) on all inputs is the prescribed finite
rank kernel flow

\[
\partial_t f(t,x)=\frac1m\sum_a K_t(x,x_a)(y_a-f(t,x_a)),
\qquad
K_t(x,z)=\sum_j\lambda_j(t)\psi_j(x)\psi_j(z),
\]

with empirical orthonormality and zero initial function. Substitution gives
the scalar equations used in (4). This is explicitly a kernel diagnostic.
Its extension identity cannot be inferred from the sample matrix (3): the
cross response to a new input is additional information.

In particular, an empirical error bound alone gives no whole-input error
bound. A function vanishing at every training point can be arbitrarily large
at an unsampled input. Normalized empirical \(L^2\) controls only the sample
maximum by \(\sqrt m\), without further structure.

## 5. Finite samples and quadrature

Population orthogonality under an input law \(\rho\),
\(\int\psi_j\psi_k\,d\rho=\delta_{jk}\), does not imply empirical
orthogonality. The empirical Gram matrix

\[
G_{jk}^{(m)}=\frac1m\sum_a\psi_j(x_a)\psi_k(x_a)
\]

must be controlled on the retained span. Whitening a well-conditioned
\(G^{(m)}\) can produce an empirical orthonormal basis, but changes mode
coordinates; it does not automatically preserve diagonal dynamics, the
frequency ordering, or uniform sup-norm bounds. Arbitrary sampling can make
\(G^{(m)}\) singular. More than \(m\) functions cannot have mutually
orthonormal empirical restrictions.

One deterministic transfer does avoid quadrature assumptions. If a label
function \(g\) has a uniform approximation \(g_R\) in a fixed \(R\)-dimensional
function span, \(\sup_x|g(x)-g_R(x)|\le\delta_R\), and \(y_a=g(x_a)\), let
\(P\) be the empirical orthogonal projection onto that span's sample
restrictions. Its least-squares property yields

\[
\|(I-P)y\|_m\le\|y-(g_R(x_a))_{a=1}^m\|_m\le\delta_R.
\tag{12}
\]

Thus (6) gives \(2\delta_R\) if that empirical subspace is dynamically
invariant. The missing ingredient remains invariance of the learned dynamics.
Equation (12) does not assert accurate reconstruction away from the samples.

Replacing population coefficients by sampled estimates also adds coefficient
error. In the diagonal extension model, errors \(\widehat y_j-y_j\) on the
retained modes contribute at most
\(\sum_{j\le R}B_j|\widehat y_j-y_j|\) to the sup norm. A distribution,
sampling design, coefficient estimator, and probability level must be stated
before claiming a bound on that term. No quadrature or concentration result
is assumed here.

## 6. Integrable leakage gives a conditional all-time comparison

Now drop invariance. Fix any empirical orthogonal projection \(P\) and put
\(Q=I-P\). The retained residual generator is
\(A_P(t)=PA(t)P\) acting on \(P\mathbb R^m\); let \(U_P(t,s)\) be its
contractive evolution. Define the retained predictor by

\[
f_P(t)=Py-U_P(t,0)Py.
\tag{13}
\]

Then, for every \(t\ge0\),

\[
\|f(t)-f_P(t)\|_m
\le 2\|Qy\|_m+
\int_0^t\|QA(s)P\,U_P(s,0)Py\|_m\,ds.
\tag{14}
\]

To prove this, first split the exact expression (2) into its \(Py\) and
\(Qy\) contributions. The latter has norm at most \(2\|Qy\|_m\). For the
former, set \(w(t)=U(t,0)Py\), \(v(t)=U_P(t,0)Py\), and
\(e(t)=w(t)-v(t)\). Because \(v(t)\in P\mathbb R^m\),

\[
\dot e(t)=-A(t)e(t)-QA(t)Pv(t),\qquad e(0)=0.
\]

Variation of constants, followed by contraction of \(U(t,s)\), gives

\[
e(t)=-\int_0^t U(t,s)QA(s)Pv(s)\,ds,
\qquad
\|e(t)\|_m\le\int_0^t\|QA(s)Pv(s)\|_m\,ds.
\]

The difference of the \(Py\)-driven predictors is \(-e(t)\), proving (14).
There is no factor growing exponentially with the final time.

For a directly checkable sufficient condition, assume
\(A_P(t)\succeq\beta(t)P\), where \(\beta(t)\ge0\), and put
\(b(t)=\int_0^t\beta(s)ds\). Differentiating \(\|v(t)\|_m^2\) gives
\(\|v(t)\|_m\le e^{-b(t)}\|Py\|_m\). Hence

\[
\sup_{t\ge0}\|f(t)-f_P(t)\|_m
\le2\|Qy\|_m+\|Py\|_m
\int_0^{\infty}\|QA(s)P\|_{m\to m}e^{-b(s)}ds.
\tag{15}
\]

The integral must be finite and small for this to be a useful approximation.
It allows a zero full spectral gap. For example, a retained lower bound
\(\beta(t)\ge\beta_0>0\) and leakage norm at most \(\eta\) give additional
error at most \((\eta/\beta_0)\|Py\|_m\). Alternatively, when no retained
lower bound is available, integrable leakage
\(\int_0^\infty\|QA(s)P\|ds<\infty\) suffices.

An energy-weighted variant also avoids a retained gap. If

\[
\|QA(t)Pv\|_m\le h(t)\sqrt{\langle v,A_P(t)v\rangle_m}
\quad\text{for every }v\in P\mathbb R^m,
\qquad \int_0^\infty h(t)^2dt<\infty,
\]

then \(\frac{d}{dt}\|v(t)\|_m^2=-2\langle v,A_Pv\rangle_m\) and
Cauchy--Schwarz in time bound the integral in (14) by
\(\|Py\|_m\|h\|_{L^2(0,\infty)}/\sqrt2\). This hypothesis is additional
control on how leakage couples to dissipating retained residuals.

Small instantaneous leakage alone fails. Work in two empirically orthonormal
mode coordinates, set \(P=\operatorname{diag}(1,0)\), \(y=(1,0)\), and let

\[
A=\eta\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad \eta>0.
\]

Then \(\|Qy\|_m=0\), \(\|QAP\|=\eta\), yet

\[
f(t)=\tfrac12(1-e^{-2\eta t})(1,1),
\qquad f_P(t)=(1-e^{-\eta t},0).
\]

The omitted coefficient tends to \(1/2\), and
\(\|f(t)-f_P(t)\|_m\to1/\sqrt2\), independently of how small \(\eta\) is.
Here the notation \(\|\cdot\|_m\) on coefficients means the inherited norm
from the empirically orthonormal modes, namely ordinary coefficient Euclidean
norm. The leakage acts over time \(1/\eta\). This constant-matrix example
already disproves a bound that would use only label tail and a vanishing
pointwise leakage norm; time-varying eigenvectors add another source of such
mixing. Applying the diagonal formula at each instantaneous eigenbasis misses
the basis-motion term in the coordinate derivative.

The empirical bound (14) does not automatically have a whole-input analogue:
one additionally needs bounded extension of both the omitted tail and the
accumulated leakage response, or a corresponding stable function-space flow.

## 7. A genuine nonlinear toy with exact sample sufficiency

The preceding prescribed-kernel model is only diagnostic. The following
nonlinear neural toy shows that fixed sample modes and actual hidden-feature
motion can coexist, but under a deliberately restrictive input-support
assumption.

Consider a scalar-input, one-hidden-neuron network

\[
h(x;b)=\tanh(bx),\qquad f(x;a,b)=a h(x;b),
\]

with both real parameters trained by the normalized square loss above.
Let every training input satisfy \(x_a\in\{-1,1\}\). Initialize
\(a(0)=0\) and \(b(0)=b_0>0\), giving zero output on every input. Define the
single label statistic

\[
c=\frac1m\sum_{a=1}^m x_a y_a.
\]

Since \(\tanh(bx_a)=x_a\tanh b\), differentiation of the loss gives the exact
autonomous two-parameter flow

\[
\dot a=(c-a\tanh b)\tanh b,
\qquad
\dot b=(c-a\tanh b)a\operatorname{sech}^2 b.
\tag{16}
\]

The full data set enters only through \(c\). The empirical unit mode
\(\psi=(x_a)_{a=1}^m\) satisfies \(\|\psi\|_m=1\), and direct differentiation
of the sample outputs yields

\[
A(t)=\frac{\kappa(t)}m\psi\psi^\top,
\qquad
\kappa(t)=\tanh^2 b(t)+a(t)^2\operatorname{sech}^4 b(t).
\tag{17}
\]

Thus all \(m-1\) orthogonal modes have exactly zero rate, while the output
amplitude \(p(t)=a(t)\tanh b(t)\) satisfies
\(\dot p=\kappa(t)(c-p)\), \(p(0)=0\). There is no positive full gap when
\(m>1\). Arbitrary label components orthogonal to \(\psi\) remain unfitted
and do not influence training.

For \(c>0\), the flow is global and genuinely moves the hidden feature. On
any finite existence interval,
\(c-p(t)=c\exp(-\int_0^t\kappa(s)ds)>0\), and differentiation gives

\[
\frac{d}{dt}\bigl(a(t)^2-\sinh^2 b(t)\bigr)=0,
\qquad
a(t)^2-\sinh^2 b(t)=-\sinh^2 b_0.
\]

The positive residual and \(b_0>0\) give \(a(t)\ge0\), \(b(t)\ge b_0\),
and \(p(t)<c\). Therefore
\(a(t)\le c/\tanh b_0\), and the invariant bounds \(b(t)\) as well. A
smooth vector field cannot have a finite-time escape while its state remains
in this compact set, proving global existence. Once \(t>0\), \(a(t)>0\)
and \(\dot b(t)>0\); the hidden feature \(\tanh(b(t)x)\) changes its shape
on continuous test inputs. Also \(\kappa(t)\ge\tanh^2 b_0>0\), so the
retained residual tends to zero. For fixed \(b_0,c\), the nonzero feature
motion is independent of the number of samples; there is no width or lazy
limit in this statement.

Computing \(c\) costs one pass over the training set. Subsequently, retaining
the two evolving weights and \(c\) reproduces the exact trained network on
every input \(x\), for all time, with storage and update cost independent of
\(m\). The label second moment is additionally needed only if the full loss
value is to be reported.

This example obtains sufficiency from a two-point training support, not from
smooth labels on a rich continuous low-dimensional input set. It does not
establish the desired general nonlinear deep-network result. It also
illustrates why sample eigenvectors cannot by themselves justify (9): although
the sample mode is fixed, its natural whole-input extension
\(\tanh(b(t)x)/\tanh b(t)\) changes with time. Exact whole-input compression
here follows from the autonomous nonlinear flow (16), not from a frozen
extension of the sample mode.

For the actual feature-learning model, the unresolved obligations are to
derive a useful invariant or weakly leaking sample span from the architecture
and data; make the retained coefficients autonomously computable with the
claimed storage; prove uniform-in-\(m\) label-tail and leakage bounds; and
control the extension to new inputs when that stronger observable is wanted.
