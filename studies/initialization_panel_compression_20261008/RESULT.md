# Initialization-only panel compression: what is proved, and what is not

## Headline

The finite-panel source construction admits a **time-zero-jet-only compiler**
and an autonomous runtime defined at **every positive compressed width**, even
below the number of training samples. In its certified regime it retains the
existing absolute fifth power of the logarithm. A conservative explicit
retained real-coordinate bound is

\[
 C(L+1)(m+p)^2\left[1+\beta^{120L}
       \left(\frac{Ym}{\gamma}\right)^4[\log(en)]^5\right]
 +C(m+p)d+D_{\rm alg}.
\tag{1}
\]

Here \(n\) is dense width, \(m\) the number of labeled training inputs,
\(p\) the number of **additional** inputs declared before initialization,
\(d\) input dimension, \(L\) hidden depth, \(Y=\|y\|_2/\sqrt m\),
and \(\gamma>0\) the unnormalized population training-feature Gram gap.
The activation envelope \(\beta\) is defined in [PANEL_BOUND.md](PANEL_BOUND.md).
The numerical \(C\) is universal. \(D_{\rm alg}\) counts the fixed runtime
and activation evaluator, including its workspace; it may not hide
width-dependent information. This is not a bit-complexity bound.

At every sufficiently large individual width, with prescribed probability
\(1-\delta\), the compressed-to-reference discrepancy over **all physical
times, including the fitted endpoint, and this declared panel** is at most
three times the fixed-confidence dense-pair variability in the same norm.
The fifth logarithmic power does not depend on \(d\).

Equation (1) is a sufficient upper bound, not a sharp optimum or a lower
bound. The more informative coefficient, exact order prescription, and full
inventory are in [PANEL_BOUND.md](PANEL_BOUND.md), equations (4), (10),
(16), (21)–(24), and the exact input-span reduction in Section 9.
In particular, the \(\beta^{120L}\) envelope is
deliberately conservative. The leading fourth power of \(Ym/\gamma\)
has **not** been canceled using the label-smallness condition.
The linear dependence on ambient \(d\) uses a fixed orthonormal map into
the span of the declared inputs, whose storage is fully counted. That map
preserves both coupled dense trajectories exactly on the panel; it is not
a whole-sphere dimensionality reduction.

**The efficient-setup part remains open.** The completely explicit origin-jet
compiler has a superpolynomial certified jet order. It proves genuine
initialization-only provenance, not cheap preprocessing. The existing
experimental compiler actually uses a full-interval dense rollout. Neither
fact establishes that a few dense steps suffice for the all-time theorem.

## 1. Scope and comparison contract

The dense model and physical clock are unchanged: independent Gaussian
first weights with variance one, hidden weights with variance \(1/n\),
zero readout, mean squared loss and mobilities \((n,1,\ldots,1,n)\).
Inputs have norm \(\sqrt d\). Only the \(m\) training inputs and their
labels drive gradient flow. Passive labels are neither needed nor used.
Activations may have unbounded values; the same strip analyticity and bounded
derivative assumptions as the paper apply. Hidden depth is fixed and at least
two. For the variability comparison assume \(m\ge2\), \(Y>0\), and
\(\gamma>0\).

Use the paper's **full existing Harmonic label allowance**, reproduced in
[PANEL_BOUND.md](PANEL_BOUND.md), equation (3). No additional cap is imposed.
No input-spanning assumption or inequality \(m\ge d\) is needed for this
panel construction. All problem parameters, the panel, and confidence are
fixed before the width limit. The sufficient width depends on them; the
inherited stochastic onset remains unquantified. This is not a uniform theorem
for a panel growing with width, nor one event over infinitely many fresh
initializations.

Define the panel norm and its independent-dense variability by
\[
 \|f-g\|_{\rm panel}
  =\sup_{t\in[0,\infty]}\max_{1\le i\le m+p}|f(t,x_i)-g(t,x_i)|,
 \qquad
 b_{n,\rm panel}
  =\inf\{b:\Pr(\|f_n-\widetilde f_n\|_{\rm panel}\le b)
                        \ge0.9999\}.
\tag{2}
\]
The two dense runs in this definition are independent. The compressor is
coupled to the dense reference whose initialized weights it uses. The bound
proved by the source construction is
\[
 \Pr\{\|f_C-f_n\|_{\rm panel}\le3b_{n,\rm panel}\}\ge1-\delta.
\tag{3}
\]
This is a comparison to actual dense variability, not its upper bound. Its
lower certificate has a witness among the training inputs, so it transfers
to the panel. The panel quantile is at most the whole-sphere quantile, not
equal to it. Equation (3) does not certify new inputs absent from the panel,
although the deployed network can evaluate them.

## 2. Proof architecture and explicit inverse

At each layer retain temporal coefficient vectors for the forward features
on the \(m+p\) panel inputs and the backward responses on the \(m\)
training inputs, together with their immediate initialized forward/reverse
images. There are at most \(2(2m+p)\) vector curves per layer. Only one
image step is used; there is no recursive closure under arbitrary matrix
words. Constants, first-weight columns, and initial training features add at
most \(2m+d+1\) source directions.

For clarity the following symbols are local to the order calculation. Put
\(\lambda=\gamma/m\), \(S=16Y/\lambda\), and let
\(U_{\rm fin}(S)\) be the explicit activation/depth recurrence in
[PANEL_BOUND.md](PANEL_BOUND.md), equation (4). The finite-query analytic
source proof supplies
\[
 T=\frac{32\log(en)}\lambda,\qquad
 r=\frac{a}{64YSU_{\rm fin}(S)\sqrt{\log(en)}},\qquad
 \alpha=\frac r{4T}
 =\frac{a}{2^{17}U_{\rm fin}(S)(Y/\lambda)^2[\log(en)]^{3/2}},
\tag{4}
\]
where \(a\) is the activation strip width. Each source coordinate is
bounded by \(M_0\sqrt n\) on the complex-time rectangle. The finite
recurrences defining \(M_0\) and the width gates are given in that note.

For coordinate source error \(0<\eta\le\min(1,Y,S)\), a sufficient
Chebyshev degree, source rank and selected-width budget are
\[
 \begin{aligned}
 K&=\left\lceil\alpha^{-1}
       \log\frac{64M_0\sqrt n}{\alpha\eta}\right\rceil,\\
 R&=2m+d+1+2(2m+p)(K+1),\qquad q=\min(n,9R).
 \end{aligned}
\tag{5}
\]
Exact source isometry and simultaneous initialized forward/reverse action
preservation are obtained by the coordinate selector and its positive layer
metrics. The current paper includes a complete barrier proof of the required
support bound and an explicit exact-metric construction. These hypotheses
are stronger than merely fitting some outputs or matching one covariance.

The corrected optimizer's residual/readout cancellation gives
\[
 \|f_C-f_n\|_{\rm panel}\le A_n\eta+D(en)^{-8},
\tag{6}
\]
where usable fully numerical bounds are
\[
 \begin{aligned}
 A_n&\le2000e^{44}\beta^{42L}\frac{Ym}{\gamma}
     \left(1+\sqrt{m/\gamma}\right)
     (1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}},\\
 D&\le236\beta^{9L}\frac{Ym}{\gamma}
                           \left(1+\sqrt{m/\gamma}\right).
 \end{aligned}
\tag{7}
\]
Use the right sides if the smaller recurrence coefficients are not computed.
To attain an absolute target \(\varepsilon\) above twice the displayed
tail, choose \(\eta=\min\{1,Y,S,\varepsilon/(2A_n)\}\), using
the numerical upper bound for \(A_n\). The full-retention branch is exact.

The checked dense-pair lower bound is
\(c_{\phi,L}Y\sqrt\gamma/[\sqrt n\log(en)^{5/2}]\), at a fixed
positive success probability and sufficiently large width; its explicit
constant is recorded in [PANEL_BOUND.md](PANEL_BOUND.md), equations (17)–(18).
Use three times this lower bound for \(\varepsilon\). Equations (4)–(7)
give (3), \(R=O(\log(en)^{5/2})\), and (1). This directly targets
constant-comparable variability; no vanishing-ratio requirement is imposed.
Neither a fitted-endpoint lower bound nor a claim about endpoint variability
alone is used.

For selected widths bounded by \(q\), the exact moving inventory is
\[
 (L-1)q^2+(d+1)q+m.
\tag{8}
\]
Fixed metrics, initialized copies, Gram workspaces, inputs and outputs are
also charged in (1) and the complete inventory in the detailed note. In
particular the \(m\)-vector in (8) is real persistent state, not free data.
For the sharper dimension overhead in (1), replace \(d\) in (5),(8) by
the rank of the panel inputs, at most \(m+p\), and retain the fixed input
map at cost at most \((m+p)d\). The dense first matrix is projected once
at initialization. This change is exact on the panel, with no change to its
population Gram or its first-layer gradient-flow mobility; see the complete
proof and setup costs in [PANEL_BOUND.md](PANEL_BOUND.md), Section 9.

## 3. Removing the construction-level lower bound on width

[OPTIMIZER.md](OPTIMIZER.md) supplies the complete construction and proof.
Normalize the top training feature map as \(V\), with normalized Gram
\(Q=V^*V\); the adjoint uses the fixed top-layer metric. Replace the
inverse in the effective readout by a smooth spectral filter:
\[
 \widehat w=w+Vg_\tau(Q)
       \bigl[(y-c)/\sqrt m-V^*w\bigr],\qquad
 g_\tau(s)=\frac1{s+\tau\chi(s/\tau)}.
\tag{9}
\]
Here \(\chi\) is the explicitly specified smooth cutoff, equal to one
below \(1/2\), zero above one, and between zero and one elsewhere.
It follows that \(g_\tau\le2/\tau\) and \(g_\tau(s)=1/s\) for
\(s\ge\tau\). Truncate nonconstant source directions when the supplied
width cannot retain them; keeping all initial training directions mandatory
would leave the original rank obstruction in place.

The unchanged positive-Gram deficit equation has the exact energy identity
\[
 -\frac d{dt}\frac{\|c\|_2^2}{m}
       =\|\dot\theta_{\rm raw}\|_{\rm par}^2.
\tag{10}
\]
Thus the raw parameters travel at most \(Y\sqrt t\) by each finite time.
The filtered readout is locally Lipschitz even at changing rank; (10) and
finite-dimensional continuation prove a unique global solution for every
positive width. This is a spectral regularized least-squares correction,
not a rank-changing pseudoinverse convention.

Choose \(\tau=\gamma/(8m)\). In the certified full-source regime the
old proof keeps \(Q\succeq\gamma I/(4m)\). The filter then equals the
inverse **exactly**, so uniqueness transfers the complete old trajectory
and its error theorem, without a new label condition or changed storage
exponent.

Below that regime, \(c\) need not be the negative actual prediction
residual. Its energy decreases, but prediction-loss monotonicity, fitting,
endpoint existence, and dense-variability accuracy are not asserted at an
arbitrary small width. The runtime still retains \(m\) deficits. A
no-deficit diagonal-metric alternative is proved in the detailed note, but
its general source selector yields \(\log^{10}n\), not the requested
\(\log^5n\); it is not substituted into this headline.

## 4. Genuine initialization-only information versus efficient setup

[INITIALIZATION.md](INITIALIZATION.md) constructs every retained temporal
coefficient as a finite linear combination of time-zero source jets.
The dense ODE gives those jets by the triangular recurrence
\[
 \Theta_{j+1}=\frac1{j+1}[t^j]
       F\!\left(\sum_{k=0}^j\Theta_kt^k\right).
\tag{11}
\]
A conformal coordinate maps a disk to the proved complex-time rectangle;
finite polynomial composition and a specified temporal quadrature then give
the source coefficients. No later trained dense weights or future labels
are inputs. The large jet arrays and original dense arrays are discarded
after compilation. This proves literal initialization-only provenance, not
just dependence of an ODE solution on its initial condition.

The necessary qualification is severe. Write locally
\(\chi_t=\lambda a/(64YSU_{\rm fin}(S))\), so
\(r=\chi_t/[\lambda\sqrt{\log(en)}]\). The sufficient jet order has
leading exponential scale
\[
 J=\exp\!\left(16\pi\chi_t^{-1}[\log(en)]^{3/2}\right)
           \times\text{the explicit logarithmic factors in the detailed note}.
\tag{12}
\]
Here
\(\chi_t^{-1}=1024[U_{\rm fin}(S)/a](Ym/\gamma)^2\): the parameter
dependence is not an unspecified constant. The exact finite cutoff, derivative
backend, arithmetic work, peak setup memory, selector work and matrix assembly
are all recorded in that note. Polynomial work in this \(J\) is still
superpolynomial in \(n\) at each fixed nonzero admissible problem.

There is a reason generic analytic continuation does not repair this cost.
For an arbitrary bounded scalar source on the same strip,
\(\pm M\tanh(\pi t/(4r))^{J+1}\) have identical first \(J\) jets
at zero and remain bounded by \(M\). Their endpoint separation forces
\(J+1\gtrsim e^{\pi T/(2r)}\log(M/\varepsilon)\). A product of such
factors gives the corresponding short-prefix observation obstruction.
This is **not a neural-network lower bound**: the adversarial scalar sources
have not been realized by the prescribed random network. A compiler exploiting
additional network structure might do better.

Consequently the present study does not prove polynomial or near-quadratic
strictly local preprocessing with the unchanged all-time guarantee. A
restarted solver whose anchors cover the whole training horizon is a global
source computation, even if its number of anchors is small. The real
experimental rollout must remain labeled as such. Small measured source ranks
do not establish a time-zero compiler's extrapolation accuracy.

## 5. Dependency reconciliation and check status

The user authorized the directly relevant finite-panel and integrated studies
as inputs and requested fresh checks. The older finite-panel files are not
accepted by their previous verdicts. The following dependency checks were
performed against the current paper and approved proofs:

- Reconstructed the current paper's finite-deletion/local insertion and source
  budget argument (appendix lines 5945–8545), including independent cavity
  stops, reverse-source terms, control entropy, trace normalization, and the
  label-sensitive analytic radius. This was a targeted dependency review,
  not a new independent audit of the entire paper.
- Rechecked the complete coordinate barrier and exact metric proof (11409–11546),
  runtime energy/fitting, and readout-deficit cancellation (11547–12520).
- Rechecked the initialized Gram CLT and the training-index innovation witness
  (9784–10002). A separate scoped reconstruction checked finite-panel union
  counts, radius gates, the variable-source-tolerance interface, and the
  lower-witness transfer; see [PANEL_BOUND.md](PANEL_BOUND.md), Section 7.
- Corrected an imported coefficient: the older full-range finite-panel
  estimate used 32 in its comparison exponent. The current complete proof
  supplies 64. This does not change the fifth logarithmic power.
- Confirmed from `DeepHarmonic` that the tested runtime already uses the
  corrected readout/deficit equations. Its full-rollout source truncation
  and randomized selector with condition cap 16 are not the certified source
  compiler and cap-four selector. The theorem is therefore not a certificate
  for the already completed empirical runs at their chosen orders.

New deterministic claims have complete arguments in the three linked notes.
They are study results, not promoted paper changes. Cheap all-time local setup
remains open; no new experiment or shared empirical-code edit was made.

The rank-safe construction received a fresh isolated scoped review:
[OPTIMIZER_REVIEW.md](OPTIMIZER_REVIEW.md). Its PASS covers the singular-spectrum
definition, global existence, energy/residual identities, source truncation and
exact transfer under the old source hypotheses, not a new stochastic-source or
numerical-conditioning theorem. The lead also reconstructed those identities.
A small floating-point algebra check at widths 1, 3, 7 and 9 with seven samples,
seed 271828, included zero and deficient feature rank: scaled residual-identity
error was below 6.3e-17, energy-identity relative error below 4.7e-16, and
resolved-branch inverse error below 1.5e-13. An initial output-relative 1e-12
check failed at 1.4e-10 in a cancellation-heavy case; scaling by the full
expression gave the stated backward error. This checks algebra only and is
not a numerical-stability certificate for the proposed optimizer.

A second isolated scoped review checked the deterministic temporal inverse,
finite quadrature, conformal compiler, arithmetic recurrence, storage and
restricted analytic-source lower bound:
[COMPILER_REVIEW.md](COMPILER_REVIEW.md). Those checks explicitly take the
dense source event and runtime certificate as hypotheses; they are not another
Gaussian-source audit. The review's elementary-function accounting observation
was addressed by declaring the exact-real convention and recording the
additional evaluator work and workspace when those operations are charged.
