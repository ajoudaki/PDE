# Quantitative width and the proposed epsilon-to-the-minus-five-halves cost

28 September 2026. Continuation of the same study, responding to the explicit
request to prove the numerical moving-state corollary under exactly the
small-label theorem's hypotheses. This is an author proof-search record.
It does not strengthen the manuscript's theorem.

**Outcome: the requested corollary remains unproved.** The work below proves
additional initialization, sensitivity, Gaussian-return, and covariance
lemmas. None establishes the needed quantitative comparison between the
actual trained finite network and its population response law. This is not
a counterexample to the proposed neural-network rate.

## 1. Exact target and the two errors that must not be conflated

Keep the model and all hypotheses of
[ACTIVATION_NEAR_QUADRATIC_ALLTIME.md](ACTIVATION_NEAR_QUADRATIC_ALLTIME.md):
fixed finite depth, training data and input dimension; canonical independent
Gaussian first/hidden initialization; exactly zero readout; layer-dependent
C1,1 activations with bounded slopes and globally Lipschitz derivatives;
a positive limiting initial readout-feature Gram gap; sufficiently small
fixed positive label RMS. The label threshold is independent of width,
history order and time. No optimizer, initialization or activation class is
changed.

For a fixed test law with finite second moment define

\[
 E_{n,q}=\left(\int\sup_{t\ge0}
 |\widehat f_{n,q}(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

The desired statement is that for each fixed confidence \(1-\delta\),
there are sufficient widths and orders with

\[
 n_\varepsilon=\varepsilon^{-2+o(1)},\qquad
 q_\varepsilon=\varepsilon^{-1/2+o(1)},\qquad
 \Pr\{E_{n_\varepsilon,q_\varepsilon}\le\varepsilon\}\ge1-\delta,
\]

giving the moving-state count

\[
 2(L-1)mn_\varepsilon q_\varepsilon+n_\varepsilon(d+1)+O(1)
 =\varepsilon^{-5/2+o(1)}
\]

at fixed \(m,d,L,\delta\). Fixed initialized matrices remain excluded from
this count. No uniform-in-depth constant or deterministic guarantee for
every Gaussian realization is sought.

The current theorem has instead

\[
 E_{n,q}\le C_\mu q^{-2}e^{K\sqrt{\log(e+q)}}+
 C_\mu\Phi(a_n)+d_{n,\mu},\quad
 \Phi(u)=u e^{K\sqrt{\log(e+1/u)}},
\]

where \(a_n\to0\) and \(d_{n,\mu}\to0\) in probability. The first
remainder transfers full *trained backward-carrier tails* to finite width;
the second is dense-predictor approximation of the population. They have
different definitions. A rate for dense predictions alone cannot be
substituted for a rate of the carrier remainder.

A sufficient quantitative upgrade would be near-root-width estimates for
both remainders, with time-independent constants. Alternatively a direct
prediction comparison could bypass the carrier remainder. Neither upgrade
is proved in this continuation. The numerical exponent does not follow by
solving for q alone.

## 2. New exact estimates

The complete derivations, including qualifications, are in
[QUANTITATIVE_WIDTH_CAVITY.md](QUANTITATIVE_WIDTH_CAVITY.md) and
[QUANTITATIVE_WIDTH_SENSITIVITY.md](QUANTITATIVE_WIDTH_SENSITIVITY.md).

**Actual stopped tangent dynamics.** In the canonical mobility Hilbert norm,
the dense variational equation has

\[
 DF=-2J^*J-\frac2m\sum_a r_a\nabla^2 f_a.
\]

On a stop where full backward coordinates have magnitude at most M,
the output Hessians have norm at most \(C(1+M)\). Keeping the negative
\(-2J^*J\) term rather than bounding its absolute norm gives

\[
 \|U(t,s)\|\le
 \exp\!\left(C(1+M)\int_s^t\rho(u)\,du\right)
 \le e^{C(1+M)S},\qquad S\le CY.
\]

This bound is independent of the number of time nodes and physical horizon.
It does not prove that the stop M of order sqrt(log n) is never reached.

**Weighted Gaussian returns.** For a cavity-independent standard Gaussian
row g, cavity-measurable matrices B_r of operator norm at most K,
deterministic weights with sum at most S, and arbitrary adaptive scalar
multipliers bounded by B,

\[
 \left\|\sum_r\alpha_r\beta_r(g)
 \frac{g^TB_rg-\operatorname{tr}B_r}{n}\right\|_{L^p}
 \le CSBK\left(\sqrt{p/n}+p/n\right).
\]

There is no factor counting the r indices. The proof conditions on the
cavity, diagonalizes the quadratic form, and applies Minkowski. The same
note proves a nonlinear return estimate with a remainder of order
\(n^{-1/2}p^{3/2}\) using only the bounded slope and Lipschitz derivative
of the activation. It also closes a complete scalar self-feedback example.
That example is explicitly not substituted for the deep neural dynamics.

**Initialization.** For each fixed finite list of training/test inputs and
every fixed p, initial feature Grams satisfy

\[
 \|Q_{\ell,n}(0)-Q_{\ell,\infty}(0)\|_{L^p}\le C_{p,\ell}/\sqrt n.
\]

The proof uses conditional row independence at initialization and Gaussian
covariance interpolation. Only two weak activation derivatives are needed;
singular input covariances are permitted. With zero readout it also gives
a root-width bound for the initial prediction velocity. It does not extend
row independence to trained features.

**Concentration versus trained bias.** Quantitative control of the
activity-weighted carrier maximum would imply near-root-width concentration
of predictions around their finite-width mean. The exact mean equations
still contain the bias of the *trained tangent Gram*. If that bias is
\(\beta_n\), and RMS fluctuations are bounded by \(l_n\), the derived
all-time mean-prediction estimate is

\[
 \sup_t|\mathbb E f_n(t,x)-f_\infty(t,x)|
 \le C_x\{\beta_n+l_n^2\log(e/l_n)\},
\]

with expectations consistently conditioned on the same good event as
specified in the complete note. This separates the genuinely missing
bias from a covariance term already small under concentration. It is a
reduction, not a proof of a rate for \(\beta_n\).

## 3. Why the last comparison has not been established

The finite backward field depends on the very Gaussian matrix being
reused. For example, Gaussian integration by parts gives exactly

\[
 \mathbb E\frac{U^TWV}{n}
 =\frac1{n^2}\sum_{ij}\mathbb E
   \partial_{W_{ij}}(U_iV_j).
\]

Taking deterministic RMS-order-one u, U=u and V=W^Tu gives mean
\(\|u\|^2/n\), of order one. Removing the response term by treating V
as independent of W therefore makes an order-one error, even at infinite
width. The population construction retains this response. Its quantitative
finite-width approximation, uniformly as the time grid is refined, is the
unresolved step.

The proposed cavity repair requires a dispersed expansion of each outside
source in the deleted Gaussian row, with row-independent response kernels
and a Euclidean remainder \(n^{-1/2+o(1)}\). The new return lemma then
controls the return through that row. The stopped tangent estimate alone
does not provide the required expansion. A deterministic quadratic Taylor
remainder for the backward gate would require regularity beyond C1,1:
the example \(\phi'(z)=\chi(z)|z|^{1+\alpha}\), \(0<\alpha<1\),
satisfies the activation assumptions but its gate remainder at zero is
\(|u|^{1+\alpha}\), not \(O(u^2)\). This is a failure of that proof
step, not a neural-network counterexample. Gaussian averaging might repair
it, but the repair has not been proved.

An additional iid-history covariance route is recorded in
[QUANTITATIVE_HISTORY_COVARIANCE.md](QUANTITATIVE_HISTORY_COVARIANCE.md).
It proves, for iid histories with \(\|X\|_{H^1}\le R\) almost surely,

\[
 \mathbb E\,\mathcal W_2^2\!\left(N(0,Q_n),N(0,Q)\right)
 \le \frac{R^2}{n}\left(1+\sum_{j\ge1}\frac1{1+\pi^2j^2}\right),
 \quad Q_n=\frac1n\sum_iX_i\otimes X_i,\quad Q=\mathbb E X\otimes X.
\]

An exponential moment of \(\|X\|_{H^1}^{\alpha}\) gives instead
\(C n^{-1}\log^{2/\alpha}(en)\). The proof does not divide by a smallest
covariance eigenvalue. Its central bound is a Sobolev Cauchy--Schwarz
inequality inside a Gaussian covariance interpolation. The complete proof
was reconstructed and checked by the coordinator. The note also gives a
fixed-law counterexample to inferring this rate from a fourth Sobolev
moment alone. That counterexample is not a neural-network example.

These estimates concern ordinary Gaussian-law coupling. They do not prove
the needed Sobolev exponential moment for every trained source history or
identify the coupling with a same-matrix forward/transpose comparison.
An ordinary covariance coupling is not automatically a causal coupling:
for independent standard Gaussians U,V, the pairs \((hU,U)\) and
\((hV,W)\), where W is another independent standard Gaussian, admit an
ordinary coupling of squared cost at most \(2h^2\). Couple their second
coordinates and leave their first independent to see this. Under a
bicausal coupling, however, the second coordinate of the second pair
must remain conditionally independent of the first coordinate of the
first pair given its own first coordinate. Its mean is zero there.
The second-coordinate cross covariance is consequently zero, so the
cost is at least 2, attained by coupling the first coordinates identically.
This example does not require our desired proof to be bicausal; it shows
that ordinary transport alone does not justify a causal Gaussian
conditioning construction. The covariance lemma is therefore retained
as a tool, not labeled a quantitative neural-network theorem.

## 4. Primary-source checks

Full PDFs and extracted text were retrieved into
`data/generated/response_memory_width_uniform_20260927/quantitative_width_01/`.
These sources are checks of possible proof tools, not premises supplying
the missing neural result.

- Reeves, *Dimension-Free Bounds for Generalized First-Order Methods via
  Gaussian Coupling*, [arXiv:2508.10782v1](https://arxiv.org/abs/2508.10782v1).
  The complete substantive text and proofs were read. Theorems 4--5 give a
  constructive finite-query comparison; the explicit bound retains the
  query count and history-covariance conditioning. Their constants cannot
  be declared uniform when a gradient-flow time grid is refined.
- Celentano et al., *State evolution beyond first-order methods I*,
  [arXiv:2507.19611](https://arxiv.org/abs/2507.19611).
  Theorem 3.2 and its first-order specialization were inspected. The
  displayed root-width estimate has a factorial query-count multiplier
  and constants depending on state evolution. It is not an all-time
  continuous-flow rate under the present hypotheses. No proof from this
  paper is imported.
- Bordelon--Pehlevan, *Dynamics of Finite Width Kernel and Prediction
  Fluctuations in Mean Field Neural Networks*,
  [arXiv:2304.03408](https://arxiv.org/abs/2304.03408).
  Its perturbative scope and discussion were checked. It does not certify
  the remainder needed here. No fluctuation expansion is promoted to a
  uniform error theorem.

The temporal conditioning issue is concrete. For independent standard
Gaussians X,Z, the pair \((X,X+hZ)\) has covariance
\(\left[\begin{smallmatrix}1&1\\1&1+h^2\end{smallmatrix}\right]\),
whose smallest eigenvalue is asymptotic to \(h^2/2\). Smoothness of a
response history therefore does not supply a uniform lower bound on its
time-query covariance. The positive *training-sample* feature Gram is a
different matrix.

## 5. Status and next mathematical obligation

| Route | Established in this continuation | Unresolved implication |
|---|---|---|
| Cavity and small activity | Stopped tangent bound; weighted nonlinear Gaussian return | Actual joint forward/transpose cavity expansion and stop closure |
| Gaussian sensitivity | Initial root-width Gram rate; concentration and mean-bias reductions | Trained carrier control and trained response bias |
| History covariance | Separate iid-history comparison; see its exact tail hypotheses | Same-matrix causal comparison, including backward use |
| Existing finite-query theorems | Explicit bounds located in full primary texts | Control of their constants through the continuous-flow limit |

A proof of the requested corollary still needs either this quantitative
response comparison or a direct prediction theorem that bypasses it. No
new concentration, stronger activation regularity, fitting, clipping or
history-Gram assumption has been inserted. The manuscript and its
numerical complexity claim were left unchanged; no experiment, commit or
push was performed.
