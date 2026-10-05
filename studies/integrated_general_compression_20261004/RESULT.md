# General merged result: proved comparisons and the remaining strict-root gap

For the latest explicit comparison envelopes, see
[SAMPLE_POLYNOMIAL_STATEMENT.md](SAMPLE_POLYNOMIAL_STATEMENT.md).
The signed-energy refinement there places all sample/gap dependence
outside the dense-copy and Legendre exponential width factors while
retaining actual Y. It also sharpens, but does not remove, the compact
comparison's exponential width threshold. The common model and the
strict-root/probability limitations below remain unchanged.

The general lower calibration is now part of §6. For every fixed
admissible dataset with at least two samples and nonzero labels, actual
dense-copy variability is at least
\(c_{\phi,L,\delta}Y\sqrt\gamma/
[\sqrt n\,\log(en)^{5/2}]\) with the specified eventual confidence.
It applies to the same general activation and geometry class.
The unchanged compact construction and a logarithmically enlarged
Legendre order have error asymptotically below that actual variability.
This validates the width exponent of the compression comparison; it
does not settle sharp sample dependence or general endpoint variability.

2026-10-04. This is the entry point for the new, user-authorized merged
study. The requested program is **not completely resolved**: the compact
and Legendre comparisons have strict root-width conclusions, while the
general independent-dense comparison proved here retains a subpolynomial
width loss. The earlier notes do not contain a proved general strict-root
independent-dense theorem that can simply be transferred. No counterexample
to that target has been proved either.

The missing comparison has not been replaced by an extra response-moment
assumption, a special activation, two layers, orthogonal data, clipping,
or a smaller observation norm. The positive components below retain the
same general scope. All results remain internally checked research, not
promotion into the maintained book or manuscript.

## 1. One common model and observation norm

Fix \(L\ge2\), \(d,m\ge1\), unit vectors
\(v_a=x_a/\sqrt d\), and fixed real labels \(y_a\). Every hidden
layer of the dense model has width \(n\). Its forward pass is
\[
z^1(v)=Av,\qquad z^\ell(v)=W^\ell h^{\ell-1}(v),\qquad
h^\ell(v)=\phi_\ell(z^\ell(v)),\qquad f_n(v)=w^{\mathsf T}h^L(v)/n.
\]
Entries of \(A_0\) are independent \(N(0,1)\), entries of every
\(W_0^\ell\), \(\ell\ge2\), are independent \(N(0,1/n)\),
all blocks are independent, and \(w_0=0\). Squared mean loss has
mobilities \((n,1,\ldots,1,n)\), explicitly the equations in
[GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md) (1).

The activations may differ across layers. They are real on the real axis,
holomorphic on a common strip \(|\operatorname{Im}z|<a\), and have
bounded first derivative there. Their **values need not be bounded**.
In particular the class includes identity, GELU on every fixed finite
strip, and nonlinear linearly growing examples such as
\(z+\varepsilon\tanh z\) on a pole-free strip. No centering or
Gaussian forward normalization is assumed. A merely smooth real activation
is not automatically in this analytic compression class.

Define
\[
Q^0_{ab}=v_a^{\mathsf T}v_b,\quad
Q^\ell_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{\ell-1}),
\]
\[
\gamma=\lambda_{\min}(Q^L)>0,\quad
Y=\|y\|_2/\sqrt m,\quad \lambda=\gamma/m.
\tag{1}
\]
Here \(\gamma\) is the **unweighted** covariance gap. General data
means precisely this initialized feature condition, without raw-input
independence or orthogonality. Any symmetry quotient must retain its
sample weights; this statement itself uses the displayed unweighted data.
There is no sign restriction on the labels.

All three comparisons use exactly
\[
\boxed{\|f-g\|_*=\sup_{t\in[0,\infty]}
                  \sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|.}
\tag{2}
\]
Time is the same physical time on both sides, and infinity denotes their
fitted limits. This is fidelity between learned functions, not error
against unknown test labels or a dense-to-population assertion.

## 2. Explicit common label allowance

All numerical constants in this study are finite recurrences, rather than
unspecified constants renamed \(C_{\rm label}\). The following table is
also a definition map for the comparison formulas. Every referenced
equation gives the complete arithmetic or Gaussian-integral definition.

| Numerical object | Complete definition | Depends on |
|---|---|---|
| \(H_D,F_D\) | Dense fitting (2), (4) | activation moments/slopes, \(L\) |
| \(S_*^{\rm Leg}\) | Closure fitting (1)–(2) | \(H_D\), slopes, \(L\) |
| \(H_C,F_C\) | Corrected-runtime fitting (5) | values at zero, slopes, \(L\) |
| \(S_*^{\rm src}\) | Source bridge (5)–(10) | half-strip derivative bounds, values at zero, \(L\) |

The corresponding files are
[dense fitting](GENERAL_EXPLICIT_FITTING.md),
[closure fitting](GENERAL_EXPLICIT_CLOSURE_FITTING.md),
[runtime fitting](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md), and
[source bridge](UNBOUNDED_COMPRESSOR_BRIDGE.md).
For clarity, the first objects are
\[
q_0=1,\quad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
\quad H_D=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),\quad Z\sim N(0,1),
\]
\[
F_D=s^2\left[(9s)^{2L-2}+4H_D^2\sum_{j=0}^{L-2}(9s)^{2j}\right],
\quad s=\max(1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}|\phi_\ell'(z)|).
\]
The common sufficient condition is
\[
\boxed{Y\le\frac\gamma m
\min\left\{\frac1{8H_D\sqrt{F_D}},\quad
             \frac{S_*^{\rm Leg}}8,\quad
             \frac1{16H_C\sqrt{F_C}},\quad
             \frac{S_*^{\rm src}}{16}\right\}.}
\tag{3}
\]
Each allowance is established independently; intersecting them does not
introduce an unproved trajectory hypothesis. No sample-count or input-
dimension dependence is hidden in the four activation/depth constants.
The explicit \(\gamma/m\) factor remains. The previous proposed
\(\beta_\partial^{-62L}\) envelope is not substituted without an
inequality audit. The real dense and all-order closure components alone
admit the simpler proved \(\beta_\partial^{-5L}\) and
\(\beta_\partial^{-10L}\) caps, respectively; those do not automatically
certify every source condition.

Zero labels are separate: all dense and Legendre trajectories are stationary
with zero prediction, and the constant-zero compressed representation is exact.
The formulas dividing by \(Y\) below concern fixed \(Y>0\).

## 3. Compact autonomous model versus its realized dense run

The representation uses selected neurons, exact source inner products in
fixed metrics, moving hidden arrays, a raw readout, and an internal residual
which equals its own prediction residual. Its effective readout is computed
algebraically from current features. The complete equations are (1)–(4) of
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md).
It is an autonomous corrected optimizer; it is not asserted to be ordinary
gradient flow with the original mobilities. It retains no original-width
matrix or trajectory table after initialization-only preprocessing.

Put \(\ell_n=\log(en)\), \(S=16Ym/\gamma\). The numerical source
recurrences give \(U,V,K_{\rm src}\), with
\(c_q=\min(1/8,a/(8V))\). They are defined in source equations
(22), (24)–(25), and (30), including their actual \(S\) dependence.
For \(d\ge2\), set
\[
A_n=\frac{2^{20}9^d}{d!}\frac Ua\,c_q^{-(d-1)}
        \left(\frac{Ym}{\gamma}\right)^2\ell_n^{3d/2+1}.
\tag{4}
\]
For \(d=1\), replace this by source equation (36):
\(A_n=8\cdot514\cdot1024(U/a)(Ym/\gamma)^2\ell_n^{5/2}\).
The count of **all retained coordinates**, including fixed metrics,
moving parameters, data and stated caches, satisfies
\[
\boxed{S_C(n)\le2040(L+1)A_n^2
       +2040(L+1)(2m+d+1)^2+10m(d+1).}
\tag{5}
\]
The logarithmic power is \(3d+2\), independent of depth. Actual \(Y\)
remains visible; it has not been replaced by the admissibility cap.
The layer-dependent radius coefficients remain explicit and can be large.
No claim that they equal the earlier unaudited \(\beta\) powers is made.

The complete numerical comparison recurrences are source equations
(42)–(47), defining \(C_{\rm out},A,\mathcal K,B_f\). In particular
\(B_f\) is the explicit runtime tail coefficient, not a hidden error
constant. Set
\[
a_0=AS/2,\qquad b_0=AK_{\rm src}S^2/2,
\quad T_{\mathrm{tail}}=(Ym/\gamma)(16\mathcal K+4B_f).
\]
Then the actual proved all-time bound is
\[
\boxed{\|f_C-f_n\|_*
\le \frac{C_{\rm out}}n e^{a_0+b_0\sqrt{\ell_n}}
                       +T_{\mathrm{tail}}e^{-8\ell_n}.}
\tag{6}
\]
All its quantities are given by finite explicit formulas. For
\[
n\ge N_{\mathrm{det}}:=\left\lceil e^{\max(4a_0,16b_0^2,2)}\right\rceil,
\]
it implies
\[
\boxed{\|f_C-f_n\|_*
\le\frac{\sqrt e\,C_{\rm out}+T_{\mathrm{tail}}}{\sqrt n}.}
\tag{7}
\]
The displayed coefficient has polynomial sample/gap dependence; a possibly
large conditioning cost is in the **displayed** deterministic threshold.
Source equation (53) also gives an explicit extra threshold for any specified
positive root coefficient, without claiming it is a sharp stability constant.
The stochastic source width threshold is still unquantified; see §6 below.

## 4. Original Legendre closure versus the same dense run

The exact moment equations retain the original clock \(\dot\tau=\rho\),
\(\tau(0)=1\), the constant forward prefix and zero backward prefix.
They are recorded in `GENERAL_LEGENDRE_TRANSFER.md` (3)–(4), including
all normalization and learning-rate factors.

[EXPLICIT_LEGENDRE_COMPARISON.md](EXPLICIT_LEGENDRE_COMPARISON.md)
(1)–(6) gives the numerical coefficients and the concrete order
\[
Q_n=\max\{3,q_{\rm abs},n^{1/4}\sqrt{C_n/Y}\},\qquad
q_n=\left\lceil4Q_n\sqrt{\log(e+Q_n)}\right\rceil.
\]
Here \(q_{\rm abs},C_n\) are explicit functions of the actual carrier
envelope \(2K_{\rm src}S\sqrt{\log(en)}\), the independent fitting
constants and projection bounds, all defined in those equations.
They are not fitted from a trajectory or assumed response quantities.
The conclusion is
\[
\boxed{\|f_{n,q_n}-f_n\|_*\le Y/\sqrt n,
\qquad q_n=n^{1/4+o(1)}.}
\tag{8}
\]
The exact moving-state count is
\[
S_{\mathrm{Leg,moving}}=n(d+1)+1+2(L-1)mnq_n.
\tag{9}
\]
It retains an additional \((L-1)n^2\) fixed mixer entries. Thus (9)
is learned-state compression, while the compact representation's (5)
counts all retained storage. These different resource statements must
not be conflated.

## 5. Independent dense copies: the proved rate and exact missing step

For two independently initialized dense copies, the numerical theorem is
[GENERAL_DENSE_COMPARISON.md](GENERAL_DENSE_COMPARISON.md) (37)–(44).
In its fully defined notation it reads
\[
\boxed{\|f_n-\widetilde f_n\|_*
\le2\mathcal L_n\sqrt{\log(4N_n/\delta)}
                   +\frac{2(K_t+K_x)}n,\qquad
N_n=(n+1)(1+2n)^d,}
\tag{10}
\]
where the explicit \(\mathcal L_n\) is \(n^{-1/2}\) times an
exponential affine in \(\sqrt{\log(en)}\). Its definitions involve
only the same derivative/moment bounds, source coefficients, and displayed
\(Y,m,\gamma,d,L\). This proves \(n^{-1/2+o(1)}\) in exactly the
same norm (2). It does **not** prove a width-independent coefficient
times \(n^{-1/2}\).

The corrected proof audit does not mistake an instantaneous-response
estimate for a transported one. In mobility coordinates
\(\Theta=(A,\sqrt nW^2,\ldots,\sqrt nW^L,w)\), let
\(F_v=nf_n(v)\), \(g_v=\nabla_\Theta F_v\),
\(H_v=D_\Theta^2F_v\), and \(J(t,s)\) be the flow's variational
propagator. If \(P\) embeds the Gaussian initialization roots, the
mixed tangent-kernel derivative is exactly
\[
\nabla_G K_{va}(t)
=\frac1nP^{\mathsf T}J(t,0)^{\mathsf T}
                    [H_v(t)g_a(t)+H_a(t)g_v(t)].
\tag{11}
\]
Under their stated bounded-activation source hypotheses, the earlier
arguments control instantaneous \(H_ag_v\) and cross-query forward
responses. The new unbounded source bridge controls training-driven
responses and proves quadratic-exponential bounds for actual running
training carriers. The sensitivity note keeps its passive-driver moment
transfer distinct rather than asserting its entire unbounded extension.
Even the bounded-class instantaneous bounds do not directly control
their product with the transported response in (11).
The remaining adjoint energy term includes
\[
\frac1n\sum_i |k_{a,i}^\ell|
       |(D_\Theta z_a^\ell\,q)_i|^2,
\qquad q(s)=J(t,s)^{\mathsf T}g_v(t).
\tag{12}
\]
The bounded exploration derives the exact augmented equations, their
block-triangular structure and backward damping of training projections.
It identifies new same-root trace and terminal-gradient terms needed to
control (12). Those terms have not been bounded. There is also a valid
Gaussian-localization and query-increment obligation for the strict
whole-sphere theorem. This is an unresolved proof gap, not evidence of an
actual slower-rate counterexample.

## 6. Probability, explicitness, lower calibration and storage consequences

The initialization probability threshold \(N_{\rm fit}(\delta)\) is
fully numerical in the dense fitting note. The trained-source probability
argument proves convergence of its success probability to one, by taking
width to infinity at each fixed empirical moment degree before taking that
degree large. It does not provide a numerical rate for that convergence.
Accordingly (3)–(10) apply at each fixed confidence for every sufficiently
large individual width, also satisfying their displayed deterministic
thresholds. They do not assert a single event over infinitely many
independently initialized widths. **A fully effective numerical success
width remains unavailable.** This limit of explicitness is not hidden in
an unnamed multiplicative constant.

To display the confidence dependence in the applicability conditions,
write this unquantified threshold as \(N_0(\delta)\), with the fixed
problem parameters suppressed. The Legendre statement requires
\(n\ge N_0(\delta)\); the compact statement with (7)'s coefficient
requires \(n\ge\max\{N_0(\delta),N_{\rm det}\}\).
The order and storage formulas need no explicit delta factor at a given
width: they hold deterministically on the same source event, whose
probability tends to one. The numerical deterministic threshold alone
does not certify a chosen confidence. See the confidence audit in
[SIMPLE_EXPLICIT_STATEMENT.md](SIMPLE_EXPLICIT_STATEMENT.md).

For \(m\ge2\) and \(Y>0\), the general lower theorem is
\[
\boxed{
\|f_n-\widetilde f_n\|_*
\ge c_{\phi,L,\delta}
       \frac{Y\sqrt\gamma}{\sqrt n\,\log(en)^{5/2}},
\qquad n\ge N_{\rm lower}(\delta),
}
\tag{13}
\]
with probability at least \(1-\delta\) at each individual width.
The positive coefficient depends only on activations, depth and confidence,
not on \(m,d,\gamma,Y,n\) or time. The finite threshold may depend on
all fixed problem parameters and is not currently effective. This lower
theorem retains (3)'s full recurrence-based label allowance and the same
general geometry and unbounded-value activation class as §§1–5.
There is no orthogonality or additional variance assumption.

For its coefficient, use the scalar moments \(q_\ell\) already defined
in §2 and put
\(\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}Z)^4\), \(Z\sim N(0,1)\).
Under the already proved simpler sufficient cap
\(Y\le(\gamma/m)\beta^{-30L}\), one may take
\[
c_{\phi,L,\delta}
=\frac{\Phi^{-1}(1/2+\delta/4)}{128}
       \sqrt{\frac{q_L}{\mu_4}},
\tag{14}
\]
where \(\Phi\) is the standard normal distribution function and \(\beta\)
is defined in SAMPLE_POLYNOMIAL_STATEMENT.md. In the full range (3),
multiply (14) by the positive activation/depth-only coefficient (18) of
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](GENERAL_TRAJECTORY_LOWER_BRIDGE.md).
Thus the larger label scope is retained, with no data hidden in this
coefficient.

The mechanism is a distribution-free inequality. If \(H\) is one
initialized top-feature vector over the \(m\) training samples and
\(Q=\mathbb E HH^\top=Q^L\succ0\), then
\[
\operatorname{tr}\operatorname{Cov}\{H(y^\top H)\}
\ge\frac{\gamma^3q_L}{16\mu_4}\|y\|^2.
\]
Zero variance would force \(H\) to lie on one fixed line, contradicting
the positive gap for \(m\ge2\). Fourth-moment truncation makes this
obstruction quantitative. The initialized Gram CLT then forces a
nonzero onset derivative fluctuation at some training input.
A finite-query complex-time source argument and polynomial derivative
inequality turn it into (13) for actual nonlinear predictions. The
proof does not estimate the difference by a width-independent
\(O(Y^3)\) remainder.

The witnessing positive time is at most
\(c_{\phi,L}m/[\gamma\sqrt{\log(en)}]\); it may depend on width and
the initialization. This is a transient lower bound in norm (2).
It is not an endpoint lower bound: at the training query used in the
proof, both fitted predictors equal the prescribed label. Initial
predictions themselves are exactly zero. For \(m=1\), a nonzero
constant last activation gives a positive uncentered gap and zero
variability at all times; the exact one-sample exceptions are stated
separately. No such exception remains for \(m\ge2,\gamma>0,Y>0\).

The complete general statement, proofs and exact limitations are in
[GENERAL_VARIABILITY_LOWER_RESULT.md](GENERAL_VARIABILITY_LOWER_RESULT.md),
[GENERAL_INNOVATION_LOWER.md](GENERAL_INNOVATION_LOWER.md), and the
trajectory bridge linked above. The bridge has a separate
[internal reconstruction](GENERAL_TRAJECTORY_LOWER_BRIDGE_CHECK.md).
No special tanh, identity, low-rank-input or orthogonal-data endpoint
result is used in this general integration.

The exponent \(1/2\) in width is now calibrated from both sides, up to
the stated logarithmic/subpolynomial losses. Sharp \(m,\gamma,d\)
dependence remains unresolved: (13) supplies a general floor, not a
matching justification for the sample/gap powers in the upper bound.
The statement is for fixed datasets as width grows, not a uniform
growing-sample limit.

At fixed problem parameters, the sufficient accuracy-to-storage powers
obtained from the proved upper bounds are:

| Representation | Resource counted | Sufficient size as accuracy \(\varepsilon\downarrow0\) |
|---|---|---|
| Dense | all parameters | \(\varepsilon^{-4+o(1)}\), using the proved near-root independent-copy bound |
| Legendre | moving coordinates | \(\varepsilon^{-5/2+o(1)}\); initialized mixers remain additional |
| Compact autonomous model | all retained coordinates | \(O(\log^{3d+2}(1/\varepsilon))\), with (4)–(5)'s actual \(Y\) and other fixed-parameter coefficients |

For every fixed admissible task with \(m\ge2\), the compact comparison
(6) is \(n^{-1+o(1)}\), hence smaller than (13)'s scale. For Legendre,
multiply §4's explicit order \(q_n\) by \(\log(en)^{3/2}\), rounding
up, and call the result \(q'_n\). Under the simpler beta label cap,
use the sharper \(q_n\) in SAMPLE_POLYNOMIAL_STATEMENT.md (5) instead.
Either simultaneous-in-order estimate gives
\[
\|f_{n,q'_n}-f_n\|_*
\le\frac{2Y}{\sqrt n\,\log(en)^3}
\]
eventually. Its moving-state exponent is still \(5/4+o(1)\).
Consequently the actual-noise comparisons are
\[
\boxed{
\frac{\|f_C-f_n\|_*}{\|f_n-\widetilde f_n\|_*}
 \xrightarrow{\mathbb P}0,\qquad
\frac{\|f_{n,q'_n}-f_n\|_*}{\|f_n-\widetilde f_n\|_*}
 \xrightarrow{\mathbb P}0.
}
\tag{15}
\]
These statements compare the common trajectory norm, not the error
ratio at each time or at the endpoint. They require no independence
between comparison events. Compact storage and the accuracy-to-storage
powers in the table are unchanged; Legendre has the stated additional
logarithmic order factor. Thus the width-asymptotic compression benefit
does not rely only on a potentially loose dense upper bound.

Conversely, in the large-width regime, requiring independent dense-copy
discrepancy at most \(\varepsilon\) with fixed failure probability
less than one half forces
\(n\log(en)^5\gtrsim_{\phi,L,\delta}Y^2\gamma/\varepsilon^2\).
At fixed task this gives necessary canonical dense parameter count
\(\Omega(\varepsilon^{-4}/\log(1/\varepsilon)^{10})\), alongside the
sufficient \(\varepsilon^{-4+o(1)}\) count. It is not a lower bound
against arbitrary alternative representations or bit encodings.
The general strict-root dense upper bound remains open.

The exact inversion formulas, confidence allocations, and all-retained
versus moving-state distinctions are in the ancillary note. Exact-real
preprocessing work and bit precision are outside the retained-coordinate
contract; no runtime or bit-complexity improvement is claimed.

## 7. What was added in this merge

The mathematical bridges are explicit Gaussian initialization without
forward normalization, the approximate-energy all-order closure fitter,
the unbounded corrected-runtime fitter and projector tail, separate
samplewise joint source budgets, the sharp unbounded complex radii,
quadratic-exponential actual training-carrier control, and numerical
comparison/order formulas. The proofs and their separate checks are linked
from the README. Earlier study files and the manuscript are unchanged.

The outstanding requested result is the general **strict-root independent-
dense comparison**, together with any assertion that its numerical
coefficient equals a prior unproved benchmark. The study records this as
open rather than presenting a conditional reduction as the completed task.
