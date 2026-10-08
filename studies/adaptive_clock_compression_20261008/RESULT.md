# Residual-adapted compression: from fifth to third logarithmic power

## Bottom line

The continued investigation obtains sufficient retained storage
\(O([\log(en)]^3)\), instead of the previous fifth power, for the
same finite-panel nonlinear compression contract. The improvement uses
a residual-adapted complex-time domain and adaptive temporal panels; it
does not replace the deployed optimizer or its coordinate selector.

The new argument and its scoped internal reconstruction are in
[FLARING_ROUTE.md](FLARING_ROUTE.md) and
[FLARING_CHECK.md](FLARING_CHECK.md). This is an internally checked study
result, not a promoted paper theorem or a new experiment. The check
reconstructs the changed source event and verifies the inherited
deterministic runtime interfaces, rather than freshly reviewing the
entire paper.

Near-\((\log n)^2\) storage remains open. A separate route proves a
late complex sector, but its onset is too late to remove the early-time
cost; see [SECTOR_ROUTE.md](SECTOR_ROUTE.md). No impossibility theorem
for the desired neural second power is claimed.

## Setup and unchanged contract

Use the canonical zero-readout Gaussian dense network, width \(n\), input
dimension \(d\), hidden depth \(L\), and analytic activation class of the
authorized compression proof, including unbounded activation values.
There are \(m\) labelled training examples and \(p\) additional passive
inputs declared at initialization, with labels withheld. The initial
limiting feature-Gram gap is \(\gamma>0\), and
\(Y=\|y\|_2/\sqrt m>0\). The existing label allowance is a stability
condition; it is not used here to erase powers of \(Y\) or \(m/\gamma\).

The target remains the maximum prediction error on this finite panel,
uniform over the **same physical training time**, including the fitted
endpoint. It is not a weighted mean over time and not a new-unseen-input
theorem. The source study's error-to-dense-variability certificate, width
threshold, probability statement and coefficient-provenance requirements
remain in force. The larger source event is proved with probability
tending to one at fixed problem parameters. Its sufficient width onset
remains qualitative.

All logarithmic power comparisons below hold for fixed admissible
activation, depth, dataset, panel and confidence. No identification of
\(m,d,1/\gamma,L\) with one another is made. Full retained storage includes
fixed mixers/metrics as well as moving state; bit complexity is separate.

## The strengthened storage and error bound

Let \(\beta\ge10\) be the existing activation envelope, and let \(C\)
denote an absolute numerical constant. For every fixed admissible
problem and confidence \(1-\delta\), at all sufficiently large widths
the same autonomous compressed dynamics can be initialized so that

\[
 \sup_{t\in[0,\infty]}\max_{i\le m+p}
 |f_C(t,x_i)-f_n(t,x_i)|\le\frac Yn.
\]

A sufficient total retained real-coordinate inventory is

\[
\begin{split}
 \operatorname{storage}\le
 C\beta^{CL}(m+p)^2\bigg[
 &\left(\frac{Ym}{\gamma}\right)^4[\log(en)]^3\\
 &+\left(\frac m\gamma\right)^2[\log(en)]^2
             [\log(e+\log(en))]^2\bigg]
 +C(m+p)d+D_{\rm alg}.
\end{split}
\tag{A}
\]

Here \(D_{\rm alg}\) is the inherited, separately charged scalar
activation-evaluation program/workspace allowance. Formula (A) counts
moving arrays, fixed mixers and metrics, panel/input data and working
buffers. It is not a bit-complexity bound. The leading explicit
\((Ym/\gamma)^4\) has not been reduced using the label allowance;
the smaller-logarithm term has a different sample/gap coefficient and
is not discarded. The fixed-problem width dependence is third power.

The width threshold can depend on the activation, depth, dataset,
\(m,p,d,Y,\gamma\) and \(\delta\); this is not a uniform theorem
when those parameters grow with \(n\). It retains the original label
interval without any new label or data restriction. The additional
explicit eventual gates are (F.17), its activity/operator gates, the
original fitted-tail test at target \(Y/n\), and the elementary degree
gate below. No polynomial bound on that threshold is asserted.

For \(m\ge2\), the existing dense-pair lower bound has a witness on
a training input. Therefore \(Y/n\) is negligible compared with actual
independent-dense panel discrepancy in probability, including its
\([\log(en)]^{5/2}\) lower-bound denominator. This is stronger than
constant-factor comparability. It is still a panel error theorem: it
does not certify arbitrary inputs first revealed after initialization.

### Exact prescription behind (A)

All constants and gates are given without suppressed factors in
FLARING_ROUTE. For clarity, its complete rank and inventory interface is

\[
\begin{aligned}
 J&\le1+40960\frac{U_{\rm fin}(16Ym/\gamma)}a
           \left(\frac{Ym}{\gamma}\right)^2\sqrt{\log(en)}\\
  &\hspace{8mm}+80\frac{\mathcal K m}{\gamma}
       \log\left(1+\frac{4\log(en)}{\log2}\right),\\
 K&=\max\left(0,\left\lceil
       \log_2\frac{8M_0\sqrt n}{\eta}\right\rceil\right),\\
 R&=2m+k+1+2(2m+p)J(K+1),
 \qquad k\le\min(d,m+p),\\
 \operatorname{storage}&\le1020(L+1)R^2+36R
       +10m(k+1)+pk+(m+p)+D_{\rm alg}+3(m+p)d.
\end{aligned}
\tag{B}
\]

Here \(J\) is the integer adaptive-panel count, \(K\) its polynomial
degree, \(R\) a source-dimension upper bound, and \(k\) the exact
panel-input span dimension. The additional input-map/data charge follows
the source study's exact input-span reduction. The scalar coefficients
\(a,U_{\rm fin},\mathcal K,M_0\) are explicitly defined by the
activation/source recurrences in FLARING_ROUTE (F.3)--(F.4) and its
specified PANEL_BOUND (4),(7); none is an additional free order.

Set \(\eta=\min\{1,Y,16Ym/\gamma,Y/(2n\overline{\mathcal A}_n)\}\),
where the completely numerical comparison certificates are

\[
\begin{aligned}
 \overline{\mathcal A}_n
 &=2000e^{44}\beta^{42L}\frac{Ym}{\gamma}
       (1+\sqrt{m/\gamma})(1+\sqrt{\log(en)})
       e^{64\sqrt{\log(en)}},\\
 \overline{\mathcal D}
 &=236\beta^{9L}\frac{Ym}{\gamma}(1+\sqrt{m/\gamma}).
\end{aligned}
\]

The explicit tail gate is
\(\overline{\mathcal D}e^{-8\log(en)}\le Y/(2n)\).
The inherited comparison then gives the displayed \(Y/n\) error.
For these fixed-parameter targets, \(K+1\le8\log(en)\) eventually;
this inequality can also be checked directly from (B) as a finite gate.

To verify (A), use the already supplied
\(U_{\rm fin}(16Ym/\gamma)/a\le\beta^{60L}\). The source
recurrences give \(H_j\le\beta^{3j}\) and
\(\tau_j\le\beta^{5L-2j+1}\). Their definition (F.4), with
the inherited \(S=16Ym/\gamma\le1\), gives
\(\mathcal K\le\beta^{14L}\). This bounds activation coefficients;
it does not erase the displayed powers of \(Ym/\gamma\).
Also \(\mathcal K m/\gamma\ge1\). Squaring the three panel-count
terms, using \((u+v+w)^2\le3(u^2+v^2+w^2)\), proves (A),
including absorption of the exact initial ranks into the second term.

### Why two logarithms disappear

The old argument uses the smallest time radius, proportional to
\(1/\sqrt{\log n}\), over a horizon proportional to \(\log n\).
It therefore pays \((\log n)^{3/2}\) temporal panels. The new domain
widens as the residual decays: first exponentially, then linearly. Its
integrated reciprocal radius costs only
\(O(\sqrt{\log n}+\log\log n)\) panels. Each still needs
\(O(\log n)\) polynomial coefficients. Source rank consequently
drops from order \((\log n)^{5/2}\) to \((\log n)^{3/2}\),
and squared mixer/metric storage drops from fifth to third power.

The source-event proof closes the nontrivial issue that this larger
complex domain must hold for the actual neural sources and all their
independently stopped cavities. Frozen real Gram matrices generate
unitary motion along imaginary time; residual decay controls their
variation. The derivative estimate needed here follows from provisional
stops, before Gaussian insertion, avoiding a circular survival argument.

All temporal panels and source coefficients are discarded after setup.
The runtime is still autonomous and uses physical time. Finite initial
jets can compute all required coefficients, including later-anchor
derivatives. This is an information-provenance theorem, not a claim that
the strict jet-only initializer is cheap or numerically well conditioned.

## 1. Why the previous proof had a fifth power

The source construction uses

\[
T=\frac{32m}{\gamma}\log(en),\qquad
\text{complex-time radius}=\frac{c_t}{\sqrt{\log(en)}}.
\]

Here \(c_t>0\) is the existing source coefficient, not an absolute
constant. Its activation, label and sample/gap dependence is retained in
the detailed source ledger. Achieving the required inverse-polynomial
source tolerance costs another \(\log n\) in polynomial degree. Thus

\[
\text{source directions per curve}
=O\bigl((\log n)^{5/2}\bigr),\qquad
\text{stored source interactions}
=O\bigl((\log n)^5\bigr).
\]

The exponent is the square of \(1+1/2+1=5/2\), not a dimension-dependent
spatial harmonic count. There are \(2(2m+p)\) forward/backward/image
curves per layer, with exact initialization and input-data charges
separately counted. See [the full rank ledger](SOURCE_RANK_LEDGER.md).

A single nonconstant polynomial in physical time cannot stay bounded on
\([0,\infty)\). But the existing theorem never asks it to: it approximates
sources only through finite \(T\), then compares the separate exponentially
decaying tails of the dense and compressed flows. Both continue to evolve.
Flattening therefore reveals a possible inefficiency, not a contradiction
in that theorem.

## 2. What a good clock does—and what it cannot do

Write \(\mathcal L(t)=m^{-1}\sum_a(f(t,x_a)-y_a)^2\) for the training
loss. A natural finite-motion clock is

\[
s(t)=\int_0^t\sqrt{\mathcal L(u)}\,du.
\]

Under the existing fitting estimates this has a finite limit. Unlike
uniform physical-time sampling, increments of \(s\) emphasize the part of
training where residual-driven changes are still appreciable.

There is an exact positive case. With one residual \(r=f-y\), the clock
\(\dot s=2|r|\) changes
\(\dot\theta=-2rD\nabla f\) into

\[
\frac{d\theta}{ds}=-\operatorname{sign}(r(0))D\nabla f(\theta).
\]

Here \(\theta\) is the full parameter vector and \(D\) its fixed mobility
matrix. The residual factor cancels completely. Under the stated positive
Gram and analytic activation assumptions, this new finite-width feature
trajectory extends analytically through its fitted endpoint. The proof
includes all passive-panel analytic responses. It does not supply
width-uniform analytic radii or an improved neural storage theorem.

For several residuals, dividing the update by their magnitude leaves their
changing **direction**. That direction can retain multiple relaxation
rates. Already the analytic quadratic gradient flow

\[
x(t)=e^{-t},\qquad z(t)=e^{-\sqrt2\,t}
\]

cannot have both coordinates analytic through the endpoint of any scalar
finite clock. If their first nonzero endpoint Taylor orders were integers
\(j,k\), the exact relation \(z=x^{\sqrt2}\) would require
\(k=\sqrt2\,j\). This is impossible.

In the simple clock \(s=1-e^{-t}\), the same issue is visible as
\(x=1-s\), \(z=(1-s)^{\sqrt2}\). A faster-completing clock is not necessarily
a smoother one. This is a generic gradient-system example, **not** a
counterexample in the specified randomly initialized neural class.
Its trajectory also has rank only two, so it is not a compression lower
bound.

A clock based solely on forward hidden-feature motion has a separate
initialization risk: zero readout gives zero initial hidden-feature
velocity, while backward responses can start moving linearly. A clock
that starts as \(s\asymp t^2\) can turn those responses into square roots
of \(s\). The full response family, not one convenient observable, must
be regular in the chosen clock.

All identities, zero cases and the scalar positive theorem are proved in
[CLOCK_GEOMETRY.md](CLOCK_GEOMETRY.md).

## 3. The exact improvement a stronger analytic estimate would buy

The adaptive-panel construction in
[ADAPTIVE_APPROXIMATION.md](ADAPTIVE_APPROXIMATION.md) proves the following
implications. The residual-adapted row is now established by the continued
investigation. The last two rows remain conditional.

| Analytic information available for every required source | Retained storage: width dependence |
|---|---:|
| Currently proved fixed strip of width proportional to \(1/\sqrt{\log n}\) | \(O((\log n)^5)\) |
| Residual-adapted complex disks, proved in FLARING_ROUTE and internally reconstructed in FLARING_CHECK | \(O((\log n)^3)\) |
| Additional complex disks whose radius grows linearly from the start | \(O((\log n)^2(\log\log n)^2)\) |
| A bounded clock with a width-independent complex analytic neighborhood | \(O((\log n)^2)\) |

For the last row the proof is particularly direct. If each response in
the clock variable has a common analytic ellipse with parameter
\(\rho>1\) independent of width and polynomially bounded magnitude, its
degree-\(K\) Chebyshev error is bounded by a fixed prefactor times
\(\rho^{-K}\). Dense-scale source accuracy then needs \(K=O(\log n)\).
The unchanged finite-panel selection and metric construction square this
rank, giving the desired second power.

The exact retained inventory is displayed in the approximation note; it
does not drop the factor \(L+1\), the \(2(2m+p)\) source multiplicity,
initial feature/input ranks, input storage, coefficient description or
the dependence on \(\rho\). Those factors cannot be assigned their old
values before the new analytic estimate is proved.

The important unsolved part for near-second-power storage is proving the
stronger early-time estimate for actual neural responses. Exponential real
loss decay alone does not prove it. The separate sector route proves a
late widened domain, but its generic parameter ball makes its onset too
late to improve the early-time cost.

The focused follow-up in Section 6 of the approximation note supplied the
successful third-power ingredient: along an imaginary-time segment,
the frozen real Gram generates unitary rather than exponentially growing
motion. Controlling the change of that Gram by the remaining residual
keeps the relevant propagator factor at \(1+o(1)\) on a proposed expanding
contour. FLARING_ROUTE and its check now extend the stochastic source
estimates and close the stopping argument on precisely that domain.

## 4. A precise obstruction to using the old estimates alone

The new [source-rank proposition](SOURCE_RANK_LEDGER.md) constructs entire
vector curves with all of the following:

- a uniformly bounded complex coordinate envelope in the currently used
  strip of width \(1/\sqrt{\log(en)}\);
- uniformly bounded, exponentially decaying values and first derivatives
  on real time, hence finite total motion and a flat endpoint;
- a requirement of \(\Omega((\log n)^{5/2})\) linear source dimensions to
  attain normalized error \(n^{-1/2}\).

At a sequence of separated times the curve visits that many orthogonal
directions, each still larger than the allowed error. An orthogonal
projection trace proves the rank lower bound. Changing time does not
remove those visited vectors. In fact, for every fixed subspace, its
worst distance from the trace is exactly invariant under an onto clock.

This construction is checked independently in
[RANK_CHECK.md](RANK_CHECK.md). It shows why a better choice of temporal
nodes, or the finite total amount of motion, cannot by itself prove the
requested rank improvement from the current estimates.

It does not show neural realizability of the example, exclude a sharper
neural rank estimate, or lower-bound general nonlinear encodings and
structured matrix storage. The neural \(\log^2 n\) question stays open.

## 5. Basis choice and initialization-only information

Chebyshev and Legendre polynomials of the same degree span exactly the
same space. Switching between them cannot by itself improve its best
uniform approximation error or source rank. Uniform spacing in a
progress clock also does not imply that uniform-weight least squares
controls the required supremum.

For the current certificate, Chebyshev remains a convenient default:
its coefficient tail directly controls uniform error. Legendre remains
reasonable for uniform-weight least squares in the new clock. A basis
adapted to multiple exponential rates or fractional endpoint powers is
another possible route, but no new rate-learning or coefficient theorem
is claimed here.

For this construction the clock is an **offline source-basis device**.
After source selection, the source coefficients, quadratures and
temporal grid are discarded. The same corrected autonomous optimizer
runs in physical time. Therefore merely using a clock offline does not
require retaining its inverse or replaying a time table at runtime.

If instead training itself is reparameterized, the inverse clock and
same-physical-time synchronization must be handled explicitly. These are
different changes and must not be conflated.

The conditional approximation statements retain the inherited finite
initial-jet coefficient evaluator and exact initialized forward/transpose
pairing. They do not assume access to observed future dense trajectories.
They also do not prove a faster practical setup algorithm: information
provenance and setup work remain separate.

## Status and stopping point

The bounded investigation is recorded separately from the paper and
previous integrated results. No theorem statement or experiment result
there has been replaced. No new training run was needed.

The exact clock/rank identities, generic obstructions, enlarged-domain
third-power result and conditional stronger approximation lemmas have
persisted arguments. Their scoped and lead checks are recorded in the
README. The desired neural \(\log^2 n\) theorem remains open, not disproved.

The next decisive proof obligation is a quantitative **neural-source**
early-time regularity estimate in a progress clock or complex domain,
or a suitable nonpolynomial basis, including all backward and initialized
image sources. Merely reusing real residual decay in a new coordinate
does not close it.
