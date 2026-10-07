# Direct initialization: a complete qualitative theorem, not the requested accuracy theorem

2026-10-05. Research result, not promoted. The strict `C/sqrt(n)` target remains open. A complete weaker construction is proved below: build an ordinary, independent logarithmic-width network directly. It converges to the same learned predictor uniformly throughout training and on the whole sphere, including endpoints. This gives no calibrated accuracy-to-storage rate and is not presented as an improved initialization.

## 1. Setup and result

Fix orthogonal inputs \(x_a\in\mathbb R^d\), \(1\le a\le m\), with \(x_a^Tx_b=d\mathbf1_{a=b}\), and fixed real labels \(y_a\). Both the reference and the small model have two tanh hidden layers, zero initial readout, squared mean loss, and the width-dependent block mobilities specified below. Define the label RMS and the initialized top-feature gap by

\[
Y=\frac{\|y\|_2}{\sqrt m},\qquad
\gamma=\mathbb E\tanh^2\!\left(\sqrt{\mathbb E\tanh^2G}\,G'\right)>0,
\quad G,G'\overset{\mathrm{iid}}\sim N(0,1).
\]

For this orthogonal tanh setting, the limiting unweighted training-feature Gram is exactly \(\gamma I_m\). The sufficient label condition used here is

\[
0<Y\le\frac{\gamma}{1000m}.
\tag{1}
\]

Zero labels give identically zero predictions and can be handled separately. No sign pattern or width-dependent label shrinkage is required. Let

\[
\|f_C-f_n\|_*
=\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |f_C(t,x)-f_n(t,x)|.
\]

**Proved weaker result.** For every deterministic integer choice \(q=q(n)\to\infty\), initialize and train the width-\(q\) model in Section 2 independently of the canonical width-\(n\) reference. Then

\[
\|f_C-f_n\|_*\longrightarrow0\quad\text{in probability}.
\tag{2}
\]

In particular, \(q=\lceil\log(en)\rceil\) gives moving state \(q^2+dq+q\), no fixed mixing matrices, and \(m(d+1)\) fixed data coordinates. For fixed data this is \(O(\log^2 n)\) moving state. The full result retains genuine hidden learning and the original physical clock.

The probability statement means: for every fixed \(\varepsilon>0\) and \(0<\delta<1\), there is a finite, unquantified threshold such that all larger reference widths satisfy

\[
\Pr\{\|f_C-f_n\|_*\le\varepsilon\}\ge1-\delta.
\tag{3}
\]

It does **not** permit substituting \(\varepsilon=C/\sqrt n\). No explicit accuracy-dependent sufficient choice of \(q\) follows from this proof. This distinction is the unresolved part of the user's central question, not a hidden qualification of a claimed root-width theorem.

## 2. Explicit construction, evolution, and cost

Create only \(A_C\in\mathbb R^{q\times d}\), \(W_C\in\mathbb R^{q\times q}\), and \(w_C\in\mathbb R^q\). Draw their initial entries independently as

\[
(A_C)_{ij}\sim N(0,1),\qquad (W_C)_{ij}\sim N(0,1/q),
\qquad w_C=0.
\]

The forward pass and residual are

\[
h_C(x)=\tanh(A_Cx/\sqrt d),\quad
g_C(x)=\tanh(W_Ch_C(x)),\quad
f_C(x)=w_C^Tg_C(x)/q,\quad r_{C,a}=f_C(x_a)-y_a.
\]

For each training input define the local backward vectors

\[
\delta_{C,a}^{(2)}=w_C\odot(1-g_C(x_a)^2),\qquad
\delta_{C,a}^{(1)}=(1-h_C(x_a)^2)\odot W_C^T\delta_{C,a}^{(2)}.
\]

Use the autonomous equations

\[
\begin{aligned}
\dot A_C&=-\frac2m\sum_a r_{C,a}\delta_{C,a}^{(1)}x_a^T/\sqrt d,\\
\dot W_C&=-\frac2{mq}\sum_a r_{C,a}\delta_{C,a}^{(2)}h_C(x_a)^T,\\
\dot w_C&=-\frac2m\sum_a r_{C,a}g_C(x_a).
\end{aligned}
\tag{4}
\]

These are exactly gradient flow with mobilities \((q,1,q)\). The state at any time determines its future. All three blocks train; there is no trajectory table, population-response query, or external residual. The width-\(n\) reference is never constructed by this algorithm.

Initialization requires \(q^2+dq\) scalar Gaussian draws and \(O(q^2+dq)\) arithmetic/assignments. A full-batch right-hand-side evaluation costs \(O(m(q^2+dq))\), and a test prediction costs \(O(q^2+dq)\), with scalar tanh evaluations counted at unit real-arithmetic cost. Batch caches add \(O(mq)\) working coordinates; processing samples sequentially reduces scratch to \(O(q)\), in addition to parameter/derivative arrays of the same order as the moving state. Data cost \(m(d+1)\) fixed coordinates. There are no additional retained initialized arrays.

These are initialization, storage, and per-evaluation costs. A numerical integrator taking \(K\) full-batch steps costs \(O(Km(q^2+dq))\); this theorem concerns continuous flow and proves neither an effective step count for the target comparison nor a bit-complexity bound. Physical fitting time is bounded explicitly below, but is not silently converted into arithmetic work.

## 3. Uniform deterministic fitting and endpoint control

This section uses proof-local symbols. Work at any width \(N\), using (4) with \(q=N\). Write \(u=x/\sqrt d\), \(\rho=\|r\|_2/\sqrt m\), and let \(H(t)\) be the matrix of top training features. Suppose initially

\[
\|W(0)\|_{\mathrm{op}}\le10,\qquad
H(0)^TH(0)/N\succeq(\gamma/2)I_m,
\qquad \|A(0)\|_F/\sqrt N\le2\sqrt d.
\tag{5}
\]

Set \(\lambda=\gamma/(4m)\). Stop while \(\|W\|_{\mathrm{op}}<11\) and \(H^TH/(Nm)\succ\lambda I_m\). The tangent Gram is a sum of positive semidefinite parameter-block Grams and dominates the readout Gram. Thus the exact loss identity and residual equation give

\[
-\rho'\ge2\lambda\rho,\qquad
-\frac d{dt}\rho^2
=\frac{\|\dot A\|_F^2}{N}+\|\dot W\|_F^2+
 \frac{\|\dot w\|_2^2}{N}.
\tag{6}
\]

Define the parameter speed as the square root of the sum in (6). Since \(2\rho(-\rho')\le(-\rho')^2/\lambda\), integration proves

\[
\rho(t)\le Ye^{-2\lambda t},\quad
\int_0^t\rho(s)ds\le\frac{Y}{2\lambda},\quad
\int_0^t\text{parameter speed}\,ds\le\frac{Y}{\sqrt\lambda},
\quad \frac{\|w(t)\|_2}{\sqrt N}\le\frac{Y}{\sqrt\lambda}.
\tag{7}
\]

At zero residual all velocities vanish; these integrated inequalities retain that interpretation. The bounds \(|\tanh|,|\tanh'|\le1\), \(\|W\|_{\mathrm{op}}\le11\), and Cauchy–Schwarz over samples yield

\[
\left(\frac{\|\dot A\|_F^2}{N}+\|\dot W\|_F^2\right)^{1/2}
\le2\sqrt{122}\,\rho\frac{Y}{\sqrt\lambda}.
\]

Both hidden-block displacements are therefore bounded by
\(\sqrt{122}Y^2/\lambda^{3/2}\). For every unit query, split the top preactivation difference into \((W(t)-W(0))h(t,u)+W(0)(h(t,u)-h(0,u))\). Its RMS, and consequently the top-feature RMS difference, are at most

\[
11\sqrt{122}\,Y^2/\lambda^{3/2}.
\tag{8}
\]

The operator perturbation of \(H/\sqrt{Nm}\) is bounded by the same number. Its initial smallest singular value is at least \(\sqrt{2\lambda}\). By (1), \(Y/\lambda\le1/250\); hence (8) is less than \((\sqrt2-1)\sqrt\lambda\), and the hidden-matrix displacement is less than one. Both stopped margins are strict. The first-exit argument closes globally. Bounded finite-dimensional state on bounded time intervals and smoothness continue the ODE for all time; the integrable parameter speed gives its parameter endpoint.

Forward differentiation at a query gives

\[
\frac{\|\dot g(t,u)\|_2}{\sqrt N}
\le\|\dot W\|_F+11\|\dot A\|_F/\sqrt N
\le244\rho Y/\sqrt\lambda.
\]

Therefore

\[
\sup_u|\partial_t f_N(t,u)|
\le(2+244Y^2/\lambda)\rho(t),
\quad
\sup_u|f_N(\infty,u)-f_N(t,u)|
\le\frac{2Y}{\lambda}e^{-2\lambda t}.
\tag{9}
\]

The last, deliberately loose, bound follows from (1), \(\lambda\le1/4\), and (7). The same right side bounds total motion after \(t\), not merely distance to the endpoint. The limiting predictor interpolates the labels because \(\rho(t)\to0\). To attain residual RMS \(\eta<Y\), physical time \(t\ge(2m/\gamma)\log(Y/\eta)\) suffices.

The whole-sphere Lipschitz constant is uniform in width and time. In fact

\[
|f_N(t,u)-f_N(t,v)|
\le\frac{11Y}{\sqrt\lambda}(2\sqrt d+1)\|u-v\|_2,
\tag{10}
\]

by the bounds on \(w,W,A\), including the hidden displacement just proved. This remains valid at the endpoint.

## 4. Probability, shared finite-width bias, and passage to the sphere

The event (5) has probability tending to one as \(N\to\infty\). Here is the complete initialization argument. The first-layer training projections are iid row tuples of independent standard Gaussians. Their bounded tanh Gram converges entrywise to \(\mathbb E\tanh^2G\,I_m\). Conditional on this entire first layer, the second preactivation rows are independent centered Gaussian tuples with precisely that empirical covariance. The conditional variance of each top-feature Gram entry is at most \(1/N\). The conditional means converge to \(\gamma I_m\): use the continuous positive semidefinite matrix square root to couple the fixed-dimensional Gaussian tuples, and bounded continuity of tanh. Entrywise convergence is operator convergence for fixed \(m\), giving the gap in (5).

For the initialized matrix bound, two \(1/4\)-nets of the unit sphere have at most \(9^N\) points each. The operator norm is at most twice their largest bilinear form. Each form is \(N(0,1/N)\); hence

\[
\Pr\{\|W(0)\|_{\mathrm{op}}>10\}
\le2\exp\{N(2\log9-100/8)\}\longrightarrow0.
\]

Finally \(\|A(0)\|_F^2/N\to d\) by the scalar law of large numbers. This proves every part of (5). Conditional row independence has only been used at initialization, not after matrix reuse.

We use the maintained population theorem, not dense-copy agreement, to control the shared limit. Its exact dependency is [B.1 in the current book](../../docs/04-continuing-flows.qmd#sec-docs-global-nonlinear-l1903), with its complete fixed-program foundation [III.F](../../docs/12-three-sample-learning.qmd#sec-docs-special-data-limits-l3785) and [continuous-value lemma A.1](../../docs/02-gaussian-reuse.qmd#sec-docs-global-nonlinear-l1842). These proofs were inspected. B.1 allows the exactly zero readout; both tanh activations have the stated bounded Lipschitz derivatives; the inputs are orthogonal. Set its three sum-loss multipliers to \(1/m\) to recover our mean-loss physical time. Its proof first establishes continuous finite-flow convergence on each fixed finite time interval, before its separate raw-GD argument.

The finite-passive-panel extension needed here follows from an exact identity. All first-weight updates lie in the orthonormal training span, so

\[
A_N(t)u=A_N(0)u+
\sum_{a=1}^m(u^Tu_a)[A_N(t)u_a-A_N(0)u_a].
\tag{11}
\]

For finitely many passive queries, append their initial Gaussian projections to the iid first-layer root tuple in the fixed-program proof. Correlations within that tuple are allowed. Append (11), the two forward activations and the readout pairing to every fixed proof mesh. The first-layer scalar transform in B.1 is Lipschitz in its changing clock, and its continuous, at-most-linear dependence on the fixed roots is covered by A.1. Its existing same-root stability therefore transfers to these passive values. Both orientations of the same initialized mixer are retained. Thus for every finite passive panel and finite physical horizon, predictions converge in probability, uniformly in time, to one deterministic population predictor.

Take a countable dense set of sphere queries. Consistency of finite panels defines its deterministic limiting predictions. Inequality (10) passes to every finite panel by convergence in probability and the high-probability event (5); it defines a unique Lipschitz extension to the whole sphere. On a finite \(a\)-net, compact-time panel convergence and (10) bound the whole-sphere error by the panel error plus twice the Lipschitz constant times \(a\). Choose \(a\) first, then send width to infinity. This proves whole-sphere compact-time convergence.

The two-finite-time version of (9) passes to the same deterministic limit. Consequently it too has a sphere-uniform fitted endpoint and the same exponential tail. Given \(\varepsilon\), choose a fixed physical horizon making the two tails smaller than \(\varepsilon/2\), and only then send width to infinity in the compact-time sphere bound. This proves all-time sphere convergence to that common deterministic predictor. Applying it separately at widths \(n\) and \(q(n)\) and taking a union bound proves (2)–(3).

On the vanishing-probability complement of (5), an endpoint comparison may be assigned error \(+\infty\). The theorem does not require an unproved endpoint claim for every finite Gaussian initialization. No quantitative bias estimate or exchange of an uncontrolled infinite-time limit has been used.

## 5. Feature learning, the sharper route, and the unresolved target

This construction does not freeze hidden layers or linearize their dynamics. For a concrete population motion certificate, let \(G_a\) be independent standard first-layer Gaussian roots and let \(Z_a\) be the initialized second-layer Gaussian fields, independent across training samples with variance \(\mathbb E\tanh^2G\). Put, locally, \(S=(2/m)\sum_b y_b\tanh Z_b\). Dividing the readout equation by time and using bounded multiplier continuity gives \(w(t)/t\to S\) in population \(L^2\). The second hidden-matrix acceleration is

\[
\frac2m\sum_a y_a
 [S\tanh'(Z_a)]\otimes\tanh(G_a).
\]

Its squared Hilbert–Schmidt norm is
\(4\mathbb E\tanh^2G\,m^{-2}\sum_a y_a^2\mathbb E[(S\tanh'Z_a)^2]>0\) when \(y\ne0\). Orthogonality supplies the diagonal first-feature Gram; strict positivity follows because \(S\) has positive variance and tanh' is everywhere positive. First-hidden motion for every nonzero-labeled sample follows from the actual adjoint pairing
\(\mathbb E[Z_aS\tanh'Z_a]=(2y_a/m)\mathbb E[Z\tanh Z\tanh'Z]\ne0\).
The complete strong-increment justification is in [DENSE_BIAS_ROUTE.md](DENSE_BIAS_ROUTE.md), Section 6. This certifies nonzero motion near initialization at fixed labels, not a lower speed bound at every later time.

For better initialization, [ANALYTIC_ROUTE.md](ANALYTIC_ROUTE.md) establishes a more targeted one-sample reduction. In a label-independent feature coordinate \(s\), a constructed response \(P(s)\) would train through \(\dot s=2[y-P(s)]\). A compatible test decoder and a uniform response error \(\varepsilon\) imply all-physical-time, whole-sphere, endpoint error at most a fixed multiple of \(\varepsilon\). The note computes the first genuinely nonlinear response coefficient directly by finite Gaussian integrals, without a dense intermediate. It does **not** prove convergence of the high-order approximation or construct the required full decoder. For multiple samples, the simplest path-independent residual-coordinate closure is already obstructed by noncommuting update directions; that is not an obstruction to other compact representations.

The strict target still requires two missing quantitative results: a reference comparison controlling both dense fluctuations and finite-width bias, and a law-computable autonomous approximation with polylogarithmic storage at that tolerance. The source-space lower bound supplied by the user does not rule out such prediction-based constructions. Conversely, neither the qualitative theorem here nor the computed nonlinear coefficient supplies them.
