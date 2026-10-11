# Same-time comparison: proved windows and the missing middle

2026-10-11. This note gives deterministic stitching lemmas and their precise
applications. It does not claim an all-time theorem on the paper's full scope.

**Continuation update.** `WIDTH_DEPENDENCY_CHECK.md` now verifies the finite
source-event dependencies used in Section 2. `TEST_PANEL_DENSE_ROUTE.md`,
Section 2, extends Section 3's endpoint input from orthogonal queries to
any fixed query outside the training span. The corresponding late-window
conclusion therefore has that broader geometry, still with unquantified
endpoint onset. The deterministic arguments below are unchanged.

The user now requests a test-only Taylor denominator. Section 2's original
initial-derivative witness lies at a training input. The subsequent proof in
`NONPARALLEL_INITIAL_VARIABILITY.md`, with its separate check, supplies a
fixed-test replacement: under pairwise nonparallel training directions and a
fixed test nonparallel to all of them, the initial difference is at least
\(c_\delta Yt/(2\sqrt n)\) throughout

\[
0<t\le\min\left\{
\frac{m}{2\gamma\sqrt{\log(en)}},
\frac{c_\delta m}{128\beta^{6L}\gamma\sqrt n\log(en)}
\right\}.
\]

Thus the near-zero comparison now covers the revised test-only panel,
including full-span training. It still supplies only a shrinking interval.
The original proof in Section 2 remains an alternative training-domain
calculation. `QUERY_RATIO_SCOPE.md` treats the separate issue of a pointwise
query quotient, not the current ratio of separate spatial suprema.

**Actual-network obstruction on a test panel.** The subsequently checked
`ACTUAL_TIME_BRIDGE.md` constructs full-span, nonparallel training/test data
and admissible nonaffine activations for which two actual dense predictions
cross on a singleton test panel at a time in \((1,2)\), with probability
bounded away from zero as width grows. Thus (2) below is false on the full
revised Taylor scope, and (1) cannot hold there with the stated zero-denominator
failure convention. This does not settle either the whole-sphere same-time
comparison or the general nonparallel endpoint lower bound. The deterministic
stitching lemmas below retain their stated hypotheses.

## The quantifiers that have to be preserved

For the paper's query domain \(\mathcal X\), let

\[
E_n(t)=\sup_{x\in\mathcal X}|f_{\rm model}(t,x)-f_n(t,x)|,
\qquad
D_n(t)=\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|.
\]

The requested claim is

\[
\sup_{t\in(0,\infty]} E_n(t)/D_n(t)
 \xrightarrow{\mathbb P}0.                                    \tag{1}
\]

Time zero is omitted because all outputs are zero there. At a positive time
or the fitted endpoint, a zero denominator counts as failure, following the
current paper's convention. The existing paper
proves the different quantity \(\sup_t E_n(t)/\sup_t D_n(t)\to0\).
Interchanging the suprema and division is not valid. A fitted zero denominator
is a further issue, fully treated in `UNIFORM_TIME_SCOPE.md`.

## 1. An exact sufficient dense statement

Suppose that for every fixed failure allowance \(\delta>0\), there is a
constant \(c_\delta>0\), independent of width and time, for which eventually

\[
\Pr\left\{D_n(t)\ge\frac{c_\delta\min\{t,1\}}{\sqrt n}
                  \text{ for every }t\in(0,\infty]\right\}
\ge1-\delta.                                                   \tag{2}
\]

Together with `EARLY_ERROR_BOUNDS.md`, this would prove (1): on the intersected
events the ratios are bounded respectively by
\(CY/(c_\delta[\log(en)]^3)\) and
\(CY/(c_\delta\sqrt n)\). No independence between these events is
needed. Let width tend to infinity and then let the allocated failure budgets
tend to zero.

Statement (2) is a sufficient condition, not a newly established dense result.
On a fitted training-only panel it is false. Even where the endpoint
denominator is nondegenerate, separate small-ball estimates for each fixed
time would not prove (2). A time net additionally needs a fluctuation-scale
modulus and a probability budget compatible with that net.

## 2. A rigorously controlled near-zero window

Here all auxiliary symbols are local. Let \(g(0)=0\) be scalar and
holomorphic near the filled Bernstein ellipse of parameter two for
\([0,r]\), with \(|g|\le M\) there. Suppose
\(|g'(0)|\ge a/\sqrt n\), where \(a,M,r>0\).
For every \(s\in[0,r/16]\), the disk of radius \(r/16\) about \(s\)
lies in that ellipse. Indeed its semiaxes are \(5r/8,3r/8\), its center is
\(r/2\), and the disk lies in the rectangle
\([-r/16,r/8]\times[-r/16,r/16]\). At its worst corner the ellipse's
normalized squared radius is at most
\((9/10)^2+(1/6)^2<1\). Cauchy's integral formula therefore gives
\(|g''(s)|\le512M/r^2\). Taylor's formula with integral remainder proves

\[
|g(t)|\ge\frac{at}{2\sqrt n}
\quad\text{for }\quad
0<t\le\min\left\{\frac r{16},
                  \frac{ar^2}{512M\sqrt n}\right\}.           \tag{3}
\]

This statement concerns every time in its interval, not one witness time.
It applies to the training-input difference used by the initial-derivative
lower argument in `WIDTH_UPGRADE.md`, on its stated quantitative source
events. In that proof one may take, with a suitable allocation of the failure
budget,

\[
\begin{gathered}
\lambda=\gamma/m,\quad X=\beta^L,\quad
a=\frac{\delta Y\gamma^2}{192mX^8},\qquad
M=32X^6Y/\lambda,\\
r=\frac1{uX^{100}(1+\lambda)\sqrt{\log(en)}},
\qquad
u=\max\left\{1,
 \left\lceil\frac{\log(32emL/\delta)}{\log(64e^2)}\right\rceil\right\}.
\end{gathered}                                                  \tag{4}
\]

The coordinate index may depend on the conditioning used for the derivative
argument; the event bounds every training coordinate on the ellipse, so this
choice causes no subsequent probability union. Its ellipse has real projection
\([-r/8,9r/8]\) and imaginary projection \([-3r/8,3r/8]\), both
inside the source rectangle used in that proof.

Consequently, conditional on the source probability verification described in
`WIDTH_UPGRADE.md`, the early-error estimates prove a uniform negligible
ratio on the interval (3), with ratios bounded by

\[
\frac{2CY}{a[\log(en)]^3}
\quad\text{and}\quad
\frac{2CY}{a\sqrt n}
\]

for Legendre and the two selected models respectively. At fixed problem and
confidence, this window has length of order
\(1/(\sqrt n\log(en))\), not a width-independent early-training interval.
It therefore does not close the intermediate-time gap in (1). The
deterministic lemma (3) is unconditional; its network probability application
has exactly the inherited source qualifications, not a new polynomial-onset
claim.

## 3. An endpoint bound gives a late window, not every positive time

Assume, on some event,

\[
D_n(\infty)\ge c/\sqrt n,
\quad
\sup_{x\in\mathcal X}|f_n(t,x)-f_n(\infty,x)|\le B e^{-kt},
\]

and the same tail bound for the independent dense run, for constants
\(c,B,k>0\). The reverse triangle inequality gives

\[
D_n(t)\ge c/\sqrt n-2B e^{-kt}.                              \tag{5}
\]

It suffices that the endpoint and tail inequalities hold at one fixed query
in \(\mathcal X\). At every time

\[
t\ge k^{-1}\log(4B\sqrt n/c),                               \tag{6}
\]

the denominator is at least \(c/(2\sqrt n)\). Thus any global
compression bound \(\sup_tE_n(t)=o(n^{-1/2})\) gives a vanishing
same-time ratio uniformly on (6), including infinity.

For the current dense fitting lemma one may take
\(k=\gamma/(2m)\) and \(B=C(m/\gamma)Y\), with the same
activation/depth coefficient as its output-tail estimate. Indeed its exact
statements give residual RMS at most \(Ye^{-\gamma t/(2m)}\) and
output tail at most \(C(m/\gamma)\) times that RMS, uniformly on the
sphere and hence on any panel. The same statements apply to an independent
initialization on its fitting event.

The imported endpoint-study result here is restricted:
`general_nonlinear_endpoint_lower_20261010/GAUSSIAN_ORACLE_ENDPOINT.md`
proves a root-width lower bound for a **fixed query orthogonal to a proper
training span**, with nonaffine activations in every layer. For each confidence,
its coefficient \(c=c_\delta\) is positive but problem dependent, and its
sufficient width is unquantified. It imposes no bounded-activation-value or
oddness assumption. The present note does not generalize that geometry or
quantify those constants.

When the query domain contains that orthogonal point, one convenient
deterministic late window is

\[
t\ge \frac{2m}{\gamma}\log(en).                             \tag{7}
\]

The tail in (5) is then \(2B/(en)\); it is at most
\(c/(2\sqrt n)\) once \(n\ge[4B/(ec)]^2\). This does not quantify
the inherited endpoint event. Taking the union with the compression event proves vanishing
same-time ratio uniformly on (7), including the fitted endpoint. Its Legendre
and selected-model rates are respectively
\(O([\log(en)]^{-3})\) and \(O(n^{-1/2})\), with
problem/confidence-dependent coefficients.

This conclusion retains the endpoint theorem's geometric and unquantified
width assumptions. A polynomial onset for a *trajectory-supremum* lower bound
does not quantify this endpoint event.

## 4. Why these two windows cannot just be joined

The interval (3) shrinks to zero; the start of (7) grows logarithmically.
There is an uncontrolled interval between them. Analyticity does not prohibit
an intermediate zero or a small minimum of a difference of analytic curves.
Interpolation of positive lower bounds at separated times is not a valid
operation. A scalar positive-time witness also does not select a useful
denominator at every time.

For a fixed finite query panel, even nonzero denominators at every fixed time
are not enough when they vanish as time tends to infinity: arbitrarily small
differences in fitted decay rates can spoil a supremum of ratios. The exact
conditional rate lemma and a scalar illustration are recorded in
`UNIFORM_TIME_SCOPE.md`; no unproved neural-network spectral genericity is
used here.

Accordingly the current proven upgrades are the compression upper factors,
the conditional near-zero window, and the geometrically qualified late
window. They do not constitute the user-requested all-time, only-nonaffine
upgrade.
