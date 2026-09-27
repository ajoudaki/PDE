# Compressing deep feature-learning dynamics: accuracy, memory, and computation

27 September 2026.

This report compares approximations to one specified population training flow.
It separates exact identities, the manuscript's fixed-width theorems, and
conditional estimates used to predict computational scaling. The primary
papers used below were retrieved in full, including their appendices.

## 1. Paragraph for the paper

> **Sizes in perspective.** Let \(m\) be the number of training examples,
> \(n\) the width, and \(H\ge2\) the hidden depth. A dense network evolves
> \(O(Hn^2)\) parameters. Response memory retains the initialized matrices and
> replaces their evolving increments by \(O(HmnP)\) history coordinates, where
> \(P\) is an approximation order rather than the number of elapsed training
> steps. Its two clocks give fixed-width trajectory errors of order \(P^{-1}\)
> and \(P^{-2}\), uniformly over each prescribed finite interval. If the dense
> population approximation has root-width error and these closure estimates
> hold uniformly in width, optimizing width and order gives moving-memory
> costs proportional to \(\varepsilon^{-3}\) and \(\varepsilon^{-5/2}\), compared
> with \(\varepsilon^{-4}\) for dense training. These are reductions in evolving
> learned state; the present implementation still stores and applies dense
> initialization matrices. Other theories organize the problem differently.
> NTH evolves higher tangent kernels and genuinely captures feature learning:
> a direct order-\(p\) implementation has \(\sum_{j=1}^{p-1}m^j\) moving
> scalars and an additional fixed top tensor. Its efficiency depends on
> higher-kernel growth, not simply the time-Taylor radius of the predictor.
> A sampled TP/DMFT solver can eliminate explicit width and initialization
> matrices, while retaining sample-pair and time-pair kernels of size
> \(O(Hm^2K^2)\) on a \(K\)-step time grid. It must also pay for numerical
> expectations and self-consistency. The central distinction is therefore
> which information is compressed: neuron width, evolving temporal history,
> or parameter directions. Response memory supplies an autonomous,
> systematically refinable compression of learned history, with the current
> network itself reconstructed from that compressed state.

## 2. Analysis: one question, common units

### 2.1 Network, target, and error

Fix \(m\) labeled training inputs, input dimension \(d\), hidden depth
\(H\ge2\), and an initialization law. Use

\[
h_1(x)=\tanh(W_1x/\sqrt d),\qquad
h_\ell(x)=\tanh(W_\ell h_{\ell-1}(x)),\quad 2\le\ell\le H,
\qquad f_n(x)=\frac{w^\top h_H(x)}n.
\tag{1}
\]

The loss is \(\mathcal L=m^{-1}\sum_a r_a^2\), where
\(r_a=f_n(x_a)-y_a\). The canonical feature-learning flow is

\[
\dot\theta=-\mathcal D_n\nabla_\theta\mathcal L,\qquad
\mathcal D_n=\operatorname{diag}(nI,I,\ldots,I,nI),
\quad \theta=(W_1,\ldots,W_H,w).
\tag{2}
\]

Internal initialization entries have scale \(n^{-1/2}\), and input weights
have order-one scale. The readout law must be identical across comparisons:
order-one and vanishing stored readouts can both give \(f_n(0,x)\to0\), yet
produce different initial tangent kernels and population flows. Initial
prediction agreement alone does not identify the same training problem.

Let \(f_\infty(t,x)\) be the corresponding population predictor on
\([0,T]\), assuming that this target exists on the chosen interval. This
does not turn a local population-limit theorem into a general all-time
existence result.

For a test probability measure \(Q\), use

\[
E_Q(\widetilde f;T)=\sup_{0\le t\le T}
\left(\int|\widetilde f(t,x)-f_\infty(t,x)|^2\,dQ(x)\right)^{1/2}.
\tag{3}
\]

For the circle, \(x=(\cos\alpha,\sin\alpha)\) and \(dQ=d\alpha/(2\pi)\).
For random approximations, use the statistical criterion
\((\mathbb E E_Q^2)^{1/2}\). Deterministic comparisons also hold pathwise;
high-probability versions must carry their probability parameter consistently.
An interval bound implies the corresponding fixed-time bound.

This controls the discrepancy in test RMSE. For any square-integrable test
label function \(y_*(x)\), the reverse triangle inequality gives

\[
\sup_{t\le T}\left|
\operatorname{RMSE}_Q(\widetilde f(t),y_*)-
\operatorname{RMSE}_Q(f_\infty(t),y_*)\right|
\le E_Q(\widetilde f;T).
\tag{4}
\]

It does not assert that the population predictor itself generalizes well.
The MSE discrepancy at one time is at most
\(2\operatorname{RMSE}_Q(f_\infty,y_*)E_Q+E_Q^2\).

Uniform absolute error on a compact input set is stronger than (3).
Deterministic parameter bounds can control it, but pointwise probabilistic
width bounds do not automatically control an input supremum with the same
constants or logarithms.

### 2.2 Size and computation

We count real scalar entries and ordinary arithmetic, with \(d\) fixed.

- **Moving state:** persistent quantities updated while computing training.
- **Fixed resources:** initialized matrices, frozen tensors, and evaluators
  for fixed coefficient functions.
- **Workspace:** temporary activations, paths, Jacobians, and factorizations.
- **Work:** arithmetic per RHS evaluation, or explicitly amortized work per
  grid step for a solver processing an entire interval.

Excluding fixed \(W_0\) from moving memory also excludes NTH's frozen top
tensor and NTK's frozen matrix. Their construction and storage still count
toward total resources. Conversely, kernels updated during a DMFT solve are
moving computational state. A full-grid solver's state is not the same kind
of object as the instantaneous state of an autonomous ODE.

Write \(K\) for the number of time steps, \(\Delta=T/K\), \(S\) for sampled
limiting-process paths, and \(I\) for full-grid solver sweeps. Physical time
\(T\) and grid length \(K\) are different. Gradient descent approximates flow,
but its error matters when optimizing history storage: choosing a smaller
\(\Delta\) increases \(K\). We use a numerical error \(D\Delta^r\) when a
stable order-\(r\) discretization has that justified bound.

Constants \(A,B_1,B_2,D,\ldots\) may depend on \(m,H,T\), data, initialization,
and \(Q\). An explicit \(m,H,T\) factor does not exhaust that dependence.
Different methods need not have the same constants.

### 2.3 Dense width: what the sampling law means

Set \(a_T(n)=(\mathbb E E_Q(f_n;T)^2)^{1/2}\). A regular finite-width
fluctuation expansion predicts

\[
f_n=f_\infty+n^{-1/2}Z+n^{-1}\beta+\cdots,
\qquad a_T(n)\lesssim A n^{-1/2}.
\tag{5}
\]

Prediction RMSE then scales as \(n^{-1/2}\), squared discrepancy as \(n^{-1}\),
and ensemble bias can scale as \(n^{-1}\). These are different quantities.
Some observables have a vanishing leading fluctuation.
The finite-width DMFT calculation derives this structure perturbatively;
it is not a general remainder theorem for (1).
[Bordelon–Pehlevan, finite-width fluctuations](https://arxiv.org/pdf/2304.03408).

The author's maintained, unpublished book gives qualitative convergence to
its local population object, including passive probes, by an oracle and
time-mesh argument. It does not give a general explicit root-width rate
for this model. We therefore use (5) as a stated hypothesis in the
population resource optimization.

Related quantitative theorems do not close this particular gap:

- Nguyen–Pham use neuronal embeddings and internal \(1/n\) averaging under
  width-independent weight assumptions. Their general comparable-width
  bound has a power \(n^{-c_1}\), \(0<c_1<1/2\), with logarithmic and step
  factors. Representing a Gaussian \(1/\sqrt n\) operator by rescaled
  \(1/n\)-averaged weights changes those assumptions.
  [Full text, Theorem 15 and Corollary 17](https://arxiv.org/pdf/2001.11443).
- Quantitative GP tensor programs give root-width bounds for their stated
  Gaussian-execution class. They do not establish the same rate for the
  nonlinear, training-adapted reuse of matrices and transposes here.
  [Full text, Theorem 1.2](https://arxiv.org/pdf/2607.06290).
- Statements about feature diversity and convergence in an infinite-width
  flow are not finite-width approximation rates.
  [Chen–Yang–Zhao–Gu, Theorem 4.5 and Corollary 4.6](https://arxiv.org/pdf/2503.09565).

Whole-test RMSE does not itself cost another square root. If
\(\mathbb E\sup_{t\le T}|f_n(t,x)-f_\infty(t,x)|^2\le C_T(x)^2/n\) and
\(\int C_T(x)^2dQ(x)<\infty\), then

\[
\mathbb E E_Q(f_n;T)^2
\le\int\mathbb E\sup_{t\le T}|f_n-f_\infty|^2dQ
\le\frac1n\int C_T(x)^2dQ(x).
\tag{6}
\]

For an input supremum, spatial Lipschitz control plus uniform sub-Gaussian
pointwise bounds can instead give a net-based rate
\(\sqrt{(d_{\rm input}\log n+\log(1/\delta))/n}\). Pointwise second moments
alone do not imply this.

Dense moving parameters and full-batch work are

\[
M_{\rm dense}=(H-1)n^2+(d+1)n,\qquad
\mathrm{work}_{\rm dense}=O(Hmn^2+mnd).
\tag{7}
\]

### 2.4 Response memory: the two complete constructions

Define backward signals without residuals by
\(\delta_{H,a}=w\odot\tanh'(z_{H,a})\) and
\(\delta_{\ell,a}=\tanh'(z_{\ell,a})\odot W_{\ell+1}^\top\delta_{\ell+1,a}\).
Equation (2) gives

\[
\dot W_1=-\frac2m\sum_a r_a\delta_{1,a}x_a^\top/\sqrt d,\quad
\dot W_\ell=-\frac2{nm}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^\top,\quad
\dot w=-\frac2m\sum_a r_a h_{H,a}.
\tag{8}
\]

An internal learned increment is therefore the integral of paired forward
and backward histories. Response memory approximates this pairing, retains
\(W_{\ell,0}\), and evolves the outer weights by (8).

Put \(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\) and
\(b_{\ell,a}=r_a\delta_{\ell,a}/\rho\). The normalized history explains the
method on nonstationary intervals; its raw insertion is \(r_a\delta_{\ell,a}\).

**Old clock.** Set \(\dot\tau=\rho,\ \tau(0)=1\). This is accumulated square
root of loss, not the derivative of loss. Let \(p_k\) be shifted Legendre
polynomials with \(\int_0^1p_jp_k=\mathbf1_{j=k}/(2k+1)\).
For each internal link and training input, store \(n\)-vectors \(A_k,B_k\),
\(0\le k<P\), the raw moments of \(h,b\) on the current clock interval.
The unit prefix has constant \(h(0)\) and zero backward history.

Suppressing link/sample indices, the exact moment equations are

\[
\dot A_k=\rho h-\frac{\rho}{\tau}
\left[kA_k+\sum_{j<k}(2j+1)A_j\right],\qquad
\dot B_k=r\delta-\frac{\rho}{\tau}
\left[kB_k+\sum_{j<k}(2j+1)B_j\right].
\tag{9}
\]

Initialize \(A_0=h(0)\), with every other moment zero, and reconstruct

\[
\widehat W_\ell=W_{\ell,0}
-\frac2{nm\tau}\sum_{a=1}^m\sum_{k=0}^{P-1}
(2k+1)B_{\ell,a,k}A_{\ell,a,k}^\top.
\tag{10}
\]

All responses are evaluated through this current reconstructed network.
The coordinates evolve with trained responses; they are not frozen
directions chosen at initialization.

**Joint clock.** Concatenate
\(\Psi=(h_{\ell-1,a},b_{\ell,a})_{\ell=2,\ldots,H;\,a=1,\ldots,m}\).
The manuscript's actual clock is

\[
g=\dot\tau=\rho+\|\dot\Psi\|_2,\qquad \tau(0)=1.
\tag{11}
\]

The full response path then has clock speed at most one. History is inserted
with mass \(\rho\,dt\), not \(g\,dt\). Both histories have matching constant
initial prefixes. A shared Gram matrix handles the nonuniform measure.

Let \(e=(1,\ldots,1)^\top\in\mathbb R^P\), and let \(J_{kk}=k\),
\(J_{kj}=2j+1\) for \(j<k\), zero above the diagonal. Each \(A,B\) is
\(n\times P\), and \(G\) is \(P\times P\). The closure is

\[
\dot A=\rho he^\top-(g/\tau)AJ^\top,\qquad
\dot B=r\delta e^\top-(g/\tau)BJ^\top,
\]
\[
\dot G=\rho ee^\top-(g/\tau)(JG+GJ^\top),
\]
\[
\widehat W_\ell=W_{\ell,0}-\frac2{nm}\sum_a
\left[B_{\ell,a}G^{-1}A_{\ell,a}^\top
-b_{\ell,a}(0)h_{\ell-1,a}(0)^\top\right].
\tag{12}
\]

Initially \(G=\operatorname{diag}(1,1/3,\ldots,1/(2P-1))\), and only the
zeroth moment columns are nonzero, equal to \(h(0),b(0)\). The subtraction
removes the artificial prefix contribution from the physical matrix.

The clock does not require an implicit solve. Set
\(h^*=AG^{-1}e,\ b^*=BG^{-1}e\). Differentiating (12) cancels all
\(g/\tau\) terms and gives

\[
\dot{\widehat W}_\ell=-\frac{2\rho}{nm}\sum_a
\left[b_{\ell,a}(h_{\ell-1,a}^*)^\top
+b_{\ell,a}^*(h_{\ell-1,a}-h_{\ell-1,a}^*)^\top\right].
\tag{13}
\]

Compute these and the outer velocities, differentiate forward/backward
passes in that direction, obtain \(\dot\Psi\), and finally update the
clock and moments. Solve with \(G\); no explicit inverse is necessary.
The nonstationary joint theorem assumes \(\rho(0)>0\). A zero-residual
initialization can be treated as stationary.

### 2.5 From projection to a trajectory bound

Let \(D_h,D_b\) be squared history projection errors, using Lebesgue clock
measure for the old clock and the insertion measure \(\mu_t\) for the joint
clock. For endpoint projections \(h^*,b^*\), differentiating raw energy
minus projected energy gives

\[
\dot D_h=\rho\|h-h^*\|^2,\qquad
\dot D_b=\rho\|b-b^*\|^2,\qquad D_h(0)=D_b(0)=0.
\tag{14}
\]

The old backward prefix's jump does not invalidate this integral identity.
Differentiating the reconstruction also gives exactly

\[
\dot{\widehat\theta}=F(\widehat\theta)+E,\qquad
E_\ell=\frac{2\rho}{nm}\sum_a(b-b^*)(h-h^*)^\top,\quad E_1=E_w=0.
\]

Consequently, Cauchy–Schwarz in time yields

\[
\int_0^T\sum_{\ell=2}^H\|E_\ell\|_Fdt
\le\frac2{nm}\sum_{\ell,a}\sqrt{D_{h,\ell,a}(T)D_{b,\ell,a}(T)}.
\tag{15}
\]

For \(v\in H^1(0,\tau)\), the Legendre tail estimate is

\[
\|v-\Pi_Pv\|_{L^2}^2
\le\frac1{P(P+1)}\int_0^\tau\xi(\tau-\xi)\|v'(\xi)\|^2d\xi
\le\frac{\tau^2\|v'\|_{L^2}^2}{4P(P+1)}.
\tag{16}
\]

To verify it, use \(-[x(1-x)p_k']'=k(k+1)p_k\). Integration by parts
and Bessel's inequality bound
\(\sum_{k\ge1}k(k+1)|c_k|^2/(2k+1)\) by
\(\int_0^1x(1-x)|v'|^2\). Every omitted mode has
\(k(k+1)\ge P(P+1)\). Sum the tail and rescale; for vector histories sum
componentwise.

The old clock bounds forward derivative energy and backward history energy.
Only the forward factor needs approximation, giving \(P^{-1}\) in (15).
At larger depth the derivative of a forward response includes the previous
link's defect. The needed uniform-in-\(P\) induction is possible because
endpoint evaluation of a degree-\((P-1)\) polynomial has norm \(P/\sqrt\tau\);
this factor cancels the \(P^{-1}\) in (16).

For precision, if \(\beta_\ell\) bounds backward Euclidean responses,
\(\mathcal A\ge\tau\), and
\(Z_\ell=m^{-1}\sum_a\int\|(h_{\ell,a})'\|^2d\xi\), then

\[
\int_0^T\rho\|E_\ell/\rho\|_F^2dt
\le\frac{2\beta_\ell^2\mathcal A^2}{n^2}Z_{\ell-1}.
\tag{17}
\]

The backward endpoint error has mean square at most
\((P+1)^2\beta_\ell^2\); (14),(16) bound the integrated forward endpoint
error by \(\mathcal A^2Z_{\ell-1}/[4P(P+1)]\). Substitute in the defect
formula and use \((P+1)/P\le2\). The differentiated forward recurrence now
gives \(Z_\ell\le C_\ell(1+Z_{\ell-1})\), with constants independent of
\(P\) at fixed width. This preserves the exponent through fixed depth.

For the joint clock, both histories are continuous and
\(\|\partial_\xi\Psi\|\le1\). Since \(d\mu_t\le d\xi\), compare the best
weighted projection with (16). The sum of both squared errors is at most
\(\tau^2(\tau-1)/[4P(P+1)]\), giving \(P^{-2}\) in (15).
To bound \(\tau\) independently of \(P\), first use the crude history-energy
bound to control total physical variation, then bound \(D\Psi\) on a stopped
region with residual bounded away from zero. This avoids assuming the small
error being proved.

Finally, if \(F\) is \(L\)-Lipschitz on the comparison region and
\(\int_0^T\|E\|dt\le\eta_P\), subtracting the dense equation gives

\[
e(t)\le\eta_P+L\int_0^te(s)ds,\qquad
\sup_{t\le T}e(t)\le\eta_Pe^{LT}.
\tag{18}
\]

Stop the closure before it leaves a neighborhood of the exact path. When
this bound is smaller than the neighborhood margin, exit is impossible.
The moment formulas and positive Gram matrix then give continuation to \(T\).

The manuscript's **fixed finite width** conclusions are

\[
\sup_{t\le T}\|\widehat\theta^{\rm old}_{n,P}-\theta_n\|
\le\frac{C_1(T,n)}{\sqrt{P(P+1)}},\qquad
\sup_{t\le T}\|\widehat\theta^{\rm joint}_{n,P}-\theta_n\|
\le\frac{C_2(T,n)}{P(P+1)}.
\tag{19}
\]

They hold at every finite depth for sufficiently large \(P\). The old
construction requires locally Lipschitz first activation derivatives; the
joint one requires locally Lipschitz second derivatives in internal layers
and positive initial residual. For bounded activations and first derivatives,
the old result holds for every \(P\ge1\). Tanh satisfies these conditions.
No successful-fitting or special input-geometry assumption enters.

“Global” here means uniform on each prescribed finite interval. It does
not mean constants uniform in all horizons or all widths.

### 2.6 The whole test function and the population decomposition

The closure reconstructs actual layer actions, so new test inputs need not
be present during training. Define the normalized comparison metric

\[
d_n(\theta,\theta')=
\frac{\|W_1-W_1'\|_F}{\sqrt n}
+\sum_{\ell=2}^H\|W_\ell-W_\ell'\|_{\rm op}
+\frac{\|w-w'\|_2}{\sqrt n}.
\]

For \(\|x\|/\sqrt d\le X\), tanh's boundedness and Lipschitz property imply

\[
\frac{\|h_1-h_1'\|}{\sqrt n}\le X\frac{\|W_1-W_1'\|_F}{\sqrt n},
\]
\[
\frac{\|h_\ell-h_\ell'\|}{\sqrt n}
\le\|W_\ell-W_\ell'\|_{\rm op}
+\|W_\ell'\|_{\rm op}\frac{\|h_{\ell-1}-h_{\ell-1}'\|}{\sqrt n},
\]
\[
|f_n-f_n'|\le\frac{\|w-w'\|}{\sqrt n}
+\frac{\|w'\|}{\sqrt n}\frac{\|h_H-h_H'\|}{\sqrt n}.
\tag{20}
\]

With bounded operator and normalized readout norms, induction gives
\(\sup_x|f_n-f_n'|\le C_Xd_n\). Equation (19) controls this metric, since
operator norm is at most Frobenius norm. Thus the whole test function and
every supported test RMSE are controlled.

Couple closure and dense network through the same initialization. Triangle
inequality, then Minkowski over initialization, gives exactly

\[
\left(\mathbb E E_Q(\widehat f_{n,P};T)^2\right)^{1/2}
\le a_T(n)+
\left(\mathbb E\sup_{t\le T}
\|\widehat f_{n,P}(t)-f_n(t)\|_{L^2(Q)}^2\right)^{1/2}.
\tag{21}
\]

There is no additional independent sampling term merely because moments
are stored. To obtain the useful population comparison laws

\[
E_{\rm dense}\le A n^{-1/2},\quad
E_{\rm old}\le A n^{-1/2}+B_1P^{-1},\quad
E_{\rm joint}\le A n^{-1/2}+B_2P^{-2},
\tag{22}
\]

we need the root-width hypothesis and width-uniform closure bounds in a
population-normalized metric, including a uniform sufficient-order threshold
where one is required. Random constants also need suitable moments or
probability quantiles. Equation (19) alone does not prove (22).

### 2.7 A sharper bound for the existing joint clock

The unnormalized speed \(\|\dot\Psi\|\) can scale as \(\sqrt{nm}\).
Directly using \(\tau^3/(nmP^2)\) can then introduce an avoidable width
factor. We can improve this without changing the algorithm.

Let

\[
M_T=1+\int_0^T\rho\,dt,\qquad
V_T=\int_0^T\frac{\|\dot\Psi\|_2}{\sqrt{nm}}dt,\qquad
\tau_T=M_T+\sqrt{nm}\,V_T.
\tag{23}
\]

The history measure has mass \(M_T\), not \(\tau_T\). The normalized history
\(F(\xi)=\Psi(\xi)/\sqrt{nm}\), including its constant matching prefix, is
\(1/\sqrt{nm}\)-Lipschitz.

A Hilbert-valued \(L\)-Lipschitz function on \([0,\tau]\) admits a
degree-\((P-1)\) polynomial with uniform error at most \(C_JL\tau/P\),
dimension independently. Here is a direct proof. Make the even periodic
function \(G(v)=F(\tau(1+\cos v)/2)\) and convolve with the normalized
positive trigonometric polynomial

\[
J_N(v)=Z_N^{-1}\left(\frac{\sin(Nv/2)}{\sin(v/2)}\right)^4.
\]

The ratio is bounded by \(\min(N,\pi/|v|)\) on \([-\pi,\pi]\) and below by
\(cN\) near zero. Splitting at \(1/N\) gives \(Z_N\asymp N^3\) and
\(\int|v|J_N(v)dv\le C/N\). Convolution error is bounded by this first
moment times \(G\)'s Lipschitz constant. Evenness makes the result a
polynomial in \(\cos v\), hence in \(\xi\), of degree \(2N-2\).
Choose \(N=\lfloor(P+1)/2\rfloor\); a constant handles \(P=1\).
The Hilbert norm triangle inequality proves the vector version.

The weighted projection is no worse in weighted \(L^2\) than that polynomial.
Multiplying squared uniform error by mass \(M_T\), and using (15), gives

\[
\int_0^T\sum_\ell\|E_\ell\|_Fdt
\le\frac1{nm}\sum_{\ell,a}(D_h+D_b)
\le\frac{C_J^2M_T}{P^2}
\left(\frac{M_T}{\sqrt{nm}}+V_T\right)^2.
\tag{24}
\]

This is for the original clock (11). Width-uniform normalized variation,
history mass, and dynamical stability would yield the expected uniform
\(P^{-2}\) rate. Their general population control remains an additional
step; this calculation removes a specific projection loss.

### 2.8 Response-memory computation

The moving state is

\[
M_{\rm old}=2(H-1)mnP+(d+1)n+O(1),\qquad
M_{\rm joint}=M_{\rm old}+O(P^2).
\tag{25}
\]

Both retain \((H-1)n^2\) fixed matrix entries. The joint construction also
keeps initial prefix fields. Learned ranks are at most \(mP\) and \(m(P+1)\).
For \(m\) current inputs, multiplying \(mP\) factors costs \(O(Hm^2nP)\).
Fixed matrix actions cost \(O(Hmn^2)\). Cumulative sums make old moment
updates linear in \(P\). Thus

\[
\mathrm{work}_{\rm old}
=O(Hmn^2+Hm^2nP+HmnP+mnd),
\]
\[
\mathrm{work}_{\rm joint}
=O(Hmn^2+Hm^2nP+HmnP^2+P^3+mnd).
\tag{26}
\]

The extra terms are Gram factorization and solves across history rows.
Directional passes add a constant number of network-action passes.
Gram conditioning and ODE stiffness can increase step count.

At fixed width, internal moving state beats a dense increment when
\(2mP<n\). Total storage still contains dense \(W_0\). Regenerating \(W_0\)
from a seed trades storage for arithmetic; it does not give a fast Gaussian
matrix multiplication.

### 2.9 NTK: the first NTH truncation

For the same mobility (2), define

\[
K^{(2)}(x,z)=\nabla f(x)^\top\mathcal D_n\nabla f(z).
\tag{27}
\]

Freezing this canonical initial kernel gives the lowest hierarchy truncation.
Substituting another parameterization's limiting kernel would change the
comparison. Training residuals obey
\(\dot{\widetilde r}=-(2/m)K_0\widetilde r\); only \(m\) predictions or
coefficients need to move. The fixed matrix has \(m^2\) entries, and one
RHS evaluation costs \(O(m^2)\). For arbitrary test inputs,

\[
\widetilde f(t,x)=f_0(x)+\sum_a K_0(x,x_a)c_a(t),
\qquad \dot c_a=-2\widetilde r_a/m.
\tag{28}
\]

This is a whole-function evaluator if the initial kernel is available.
Its same-target error is a feature-freezing bias \(b_{\rm lazy}(T,Q)\),
plus coefficient-evaluation error. Width does not remove a nonzero population
bias. The bias can vanish in special problems.

A training estimate makes this quantitative. Since \(K_0\) is positive
semidefinite, its homogeneous propagator is contractive. For
\(e=r-\widetilde r\), variation of constants gives

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le2\int_0^t\frac{\|K_s-K_0\|_{\rm op}}m\,\rho(s)\,ds.
\tag{29}
\]

If \(\rho\le R\) and \(\|K_s-K_0\|_{\rm op}/m\le Ls\), this is at most
\(LRt^2\). It explains a local second-order discrepancy, not a universal
\((T/R_0)^2\) law. Test-function error additionally involves mixed
test–training kernels.

### 2.10 NTH on the same feature-learning flow

Higher NTH levels evolve the tangent kernel and capture feature learning.
To put them on our axis, derive the hierarchy using (2):

\[
K^{(r+1)}(x_1,\ldots,x_{r+1})
=\nabla K^{(r)}(x_1,\ldots,x_r)^\top
\mathcal D_n\nabla f(x_{r+1}).
\]

The chain rule gives exactly

\[
\dot f(x)=-\frac2m\sum_a r_aK^{(2)}(x,x_a),\qquad
\dot K^{(r)}=-\frac2m\sum_a r_aK^{(r+1)}(\ldots,x_a).
\tag{30}
\]

Retain kernels through order \(p\) with exact initial values, and freeze
\(K^{(p)}\). Here \(p\) is kernel order, distinct from moment order \(P\).
These definitions are valid at finite width. A population construction
additionally requires the corresponding limiting kernels and hierarchy.

**A matched error bound, derived directly.** Let \(B_r\) bound the exact
\(|K^{(r)}|\) on \([0,T]\), with first argument ranging over training and
test inputs and remaining arguments over training inputs. Let \(R\) bound
true and truncated training residuals on a stopped interval. Write
\(e_f,e_r\) for maximum predictor and kernel discrepancies. Subtraction gives

\[
e_p(t)\le2RB_{p+1}t,
\]
\[
e_r(t)\le\int_0^t[2Re_{r+1}(s)+2B_{r+1}e_f(s)]\,ds,
\quad 2\le r<p,
\]
\[
e_f(t)\le\int_0^t[2Re_2(s)+2B_2e_f(s)]\,ds.
\tag{31}
\]

The sample average cancels the explicit \(m\) in this worst-case bound;
\(B_r\) still depends on the data. Substitute from the top down. The top
forcing is integrated \(p\) times, giving \(B_{p+1}(2Rt)^p/p!\).
Feedback convolutions have kernels
\(2B_{k+2}(2R(t-s))^k/k!\), \(0\le k\le p-2\). Bound each by its value
at \(T\), then apply the integral inequality in (18):

\[
\sup_{t\le T}e_f(t)\le
\eta_p(T):=B_{p+1}\frac{(2RT)^p}{p!}\exp(L_{p,T}T),
\qquad
L_{p,T}=2\sum_{k=0}^{p-2}B_{k+2}\frac{(2RT)^k}{k!}.
\tag{32}
\]

Choose \(R\) one larger than the exact residual maximum and stop at error
one. Whenever (32) is below one, such an exit is impossible. The triangular
integral recurrences bound the other tensor variables, so the finite system
continues through \(T\). This is a conditional finite-horizon comparison,
not merely agreement of derivatives at initialization.

For example, suppose uniformly in the approximation resources that

\[
B_r\le U V^{r-2}(r-2)!,\qquad q=2RVT<1.
\tag{33}
\]

Then \(L_{p,T}\le2U/(1-q)\), and

\[
\eta_p(T)\le D\frac{q^p}{p},\qquad
D=\frac UV\exp\left(\frac{2UT}{1-q}\right).
\tag{34}
\]

This permits geometric convergence where higher-kernel growth is controlled.
Tanh analyticity alone does not establish useful width-uniform constants in
(33) for every desired horizon. If instead \(B_r\le UV^{r-2}\), then
\(L_{p,T}\le2Ue^{2RVT}\), and (32) gives factorial order convergence on every
finite interval. These are sufficient alternatives, not universal kernel
growth laws for trained tanh networks.

Finite-width initialization adds a dense width error as in (21).
Population initialization removes that term, but computing the initial
kernels and controlling coefficient errors remain obligations.

**The published theorem, in the correct units.** Huang–Yau use \(m,n\)
in the opposite order. In our notation their Theorem 2.6 bounds training
RMS truncation error, for its stated even orders and hypotheses, by

\[
\frac{\|f(t)-\widetilde f(t)\|_2}{\sqrt m}
\lesssim \frac{(1+t)t^{p-1}}{n^{p/2}}\min\{t,m/\lambda\},
\tag{35}
\]

on the horizon

\[
t\le\min\left\{
\frac{c\sqrt{\lambda n/m}}{(\log n)^C},
\frac{n^{p/[2(p+1)]}}{(\log n)^{C'}}
\right\}.
\tag{36}
\]

Here \(\lambda\) lower-bounds the initial training-kernel eigenvalue.
The proof uses small higher kernels in its parameterization. It is not a
population-RMSE theorem for our canonical rich feature-learning scaling.
Its small-subset linear-independence assumption also excludes three vectors
on a two-dimensional circle. This limits transfer of the theorem, not the
definition of the hierarchy on that task. Constants and assumptions that
depend on order must be tracked before optimizing \(p\).
[Full text, equations (2.7)–(2.11), Theorem 2.6 and Appendix C](https://arxiv.org/pdf/1909.08156).

**Why a time-Taylor radius is not a hard barrier.** Already \(p=2\) solves
a kernel ODE with exponential time dependence; its trajectory is not a
first-degree polynomial. Agreement of low-order derivatives at zero does
not identify a truncation's subsequent path with a truncated Taylor series.

A counterexample makes the distinction decisive. Take one parameter,
\(f(\theta)=\theta^2\), target zero, unit mobility, and loss \(f^2\).
For \(f_0>0\),

\[
\dot\theta=-4\theta^3,\qquad
f(t)=\frac{f_0}{1+8f_0t},\qquad K^{(r)}=4^{r-1}f.
\tag{37}
\]

The time Taylor series has finite radius \(1/(8f_0)\). Nevertheless the
order-\(p\) hierarchy is equivalently

\[
\widetilde f_p=f_0\sum_{k=0}^{p-1}\frac{(4s)^k}{k!},
\qquad \dot s=-2\widetilde f_p,\qquad s(0)=0.
\tag{38}
\]

The exact scalar equation replaces the sum by \(e^{4s}\), with solution
\(s(t)=-\tfrac14\log(1+8f_0t)\). On every finite \(T\), this path lies in
a compact interval. The exponential polynomials and their derivatives
converge uniformly on a neighborhood of that interval. Subtract the ODEs,
use (18), and stop at its boundary: the forcing tends uniformly to zero,
so an exit is impossible for sufficiently large \(p\). Thus
\(\widetilde f_p\to f\) uniformly on every finite \(T\), including times
beyond the Taylor radius.

This disproves the proposed universal barrier. It does not prove a
general all-horizon convergence theorem for deep tanh NTH. When (33)
fails, the correct conclusion is that this certificate is inconclusive,
not that the required memory is infinite. Restarting from a truncated
state is possible; refreshing its top tensors to the exact trained values
generally requires information that was not retained.

**State and full-function representation.** The direct implementation
moves \(m\) predictions and tensors \(K^{(2)},\ldots,K^{(p-1)}\).
The top tensor is fixed. Therefore, for \(m\ge2\),

\[
M_{\rm NTH}(m,p)=\sum_{j=1}^{p-1}m^j
=\frac{m^p-m}{m-1},\qquad
m^{p-1}\le M_{\rm NTH}\le2m^{p-1}.
\tag{39}
\]

Its fixed top tensor has \(m^p\) entries and direct RHS work is \(O(m^p)\).
After depth contributions have been combined into output kernels, there
is no extra \(H\) multiplier: depth affects their construction and error
constants. These counts are not lower bounds against structured tensors.

A test mesh is unnecessary if initial mixed-kernel functions can be
evaluated. Put \(u_a=-2\widetilde r_a/m\) and define

\[
I_\varnothing=1,\qquad
\dot I_{a_1\cdots a_k}=u_{a_1}I_{a_2\cdots a_k},\qquad
I_{a_1\cdots a_k}(0)=0.
\]

Repeated integration of the triangular hierarchy gives, exactly for the
truncation,

\[
\widetilde f_p(t,x)=f_0(x)+
\sum_{k=1}^{p-1}\sum_{a_1,\ldots,a_k}
K_0^{(k+1)}(x,x_{a_1},\ldots,x_{a_k})I_{a_1\cdots a_k}(t).
\tag{40}
\]

There are \(O(m^{p-1})\) moving coefficients. Fixed mixed-kernel construction
and evaluation are not free. When \(m=1\), \(I_k=s^k/k!\), \(\dot s=u\):
one moving scalar suffices, alongside fixed initial coefficients. Thus even
the direct hierarchy's count is not a universal optimality claim.

### 2.11 TP/DMFT as an executable limiting-process solver

Neither TP nor DMFT specifies one unique algorithm. TP's relevant master
theorem gives convergence for a fixed program, without a general trained
root-width rate for (1). Its limiting recursion includes correlations from
matrix/transpose reuse. Sampling it is not automatically finite-network
training with matrices stored as historical factors.
[Yang–Hu, Algorithm 1 and Master Theorem 7.4](https://arxiv.org/pdf/2011.14522).

For a concrete comparison, use the self-consistent sampled response process
in nonlinear DMFT. Its feature-learning scaling can match (1): choose
\(\gamma=\sqrt n\), write variance-one internal weights as
\(U_\ell=\sqrt nW_\ell\), and retain the outer coordinates. Mobility \(n\)
on \(U_\ell\) becomes mobility one on \(W_\ell\); outer mobilities remain
\(n\). The readout law and loss normalization must also match.
[Bordelon–Pehlevan, model/scaling](https://arxiv.org/pdf/2205.09653).

On a \(K\)-time grid, a concrete solver:

1. Stores forward/backward covariances and response kernels indexed by pairs
   of inputs and times.
2. Updates predictions from those kernels.
3. Factors Gaussian covariances and draws \(S\) noise paths.
4. Solves causal path equations and their response Jacobians.
5. Averages products and derivatives, updates the kernels, and iterates.

This is the substance of Appendix B, Algorithm 1. The paper's Table 1
reports quadratic memory and cubic work in sample count times grid length,
suppressing sampling and iteration resources.
[Full algorithm and table](https://arxiv.org/pdf/2205.09653).

For an explicit dense implementation let \(q_0=mK\). A covariance
factorization costs \(O(q_0^3)\) per layer/sweep. A path and its covariance
outer products cost \(O(q_0^2)\); full causal response Jacobians computed
by dense triangular solves can cost \(O(q_0^3)\) per path. Restoring the
numerical resources gives the conservative implementable bound

\[
\mathrm{total\ work}=O(IH(S+1)m^3K^3),\qquad
\mathrm{amortized\ work/step}=O(IH(S+1)m^3K^2).
\tag{41}
\]

Streaming one path and its Jacobian while accumulating averages gives peak
memory \(O(Hm^2K^2)\), independent of \(S\). Batching paths needs
\(O(HSmK)\) path storage and potentially \(O(HSm^2K^2)\) explicit Jacobians.
These are specified implementation costs, not lower bounds.

**Solver error and feedback.** A useful conditional model is

\[
E_{\rm D}\le A_{\rm D}S^{-1/2}+B_{\rm D}(T/K)^r+\eta,
\tag{42}
\]

with output-level iteration error \(\eta\). This requires consistent time
discretization and stable self-consistency and response estimation.
Fixed-grid i.i.d. averaging alone does not prove it uniformly as \(K\) grows.

For instance, suppose the discrete self-consistency map \(\mathcal F\)
is \(\kappa\)-Lipschitz, \(\kappa<1\), its sampled map differs uniformly by
at most \(\zeta\), and the numerical residual is at most \(\eta_0\).
For exact discrete fixed point \(q_*\) and computed \(\widehat q\),

\[
\|\widehat q-q_*\|\le\eta_0+\zeta+\kappa\|\widehat q-q_*\|,
\qquad
\|\widehat q-q_*\|\le\frac{\eta_0+\zeta}{1-\kappa}.
\tag{43}
\]

Add a Lipschitz output estimate, a uniform sampling bound, and the time
error to obtain (42). Local inverse-stability estimates can replace
contraction. The inspected general papers do not establish this solver
theorem on arbitrary compact horizons for the present model.

Setting \(S=n\) only aligns formal root-sampling powers. It does not match
the covariance or distribution of the sampled solver and finite trained
network. Finite-width fluctuations include interacting network feedback;
the finite-width DMFT calculation does not equate them with independent
limiting-path Monte Carlo noise.
[Finite-width fluctuation calculation](https://arxiv.org/pdf/2304.03408).

Where TP and DMFT identify the same limit, this sampled response process
can serve as a numerical backend for either. We therefore give it one
row, rather than assign TP an unjustified universal cost.

Passive test inputs need mixed covariances and test paths. A training-only
kernel table is not itself a constant-cost evaluator of the whole function.
Queries may be processed separately or batched; a direct batch implementation
enlarges the input index set. The error bound must cover these passive
observables too. Full dense-weight reconstruction is not needed for our
common prediction target.

### 2.12 An exact-history baseline, distinct from TP

For finite-network Euler training, the identity

\[
W_{\ell,k}=W_{\ell,0}
-\frac{2\Delta}{nm}\sum_{j<k}\sum_a
r_{a,j}\delta_{\ell,a,j}h_{\ell-1,a,j}^\top
\tag{44}
\]

is exact for the discrete dynamics. Storing all factors costs
\(O(HmnK)\) moving entries plus fixed \(W_0\). Per-step work near the end
is \(O(Hmn^2+Hm^2nK)\). This is a valid baseline, not an identification
of TP sampling with finite networks.

With the width hypothesis and a stable order-\(r\) discretization,

\[
E_{\rm history}\le A n^{-1/2}+D_{\rm h}(T/K)^r.
\tag{45}
\]

A fixed-stage Runge–Kutta method adds a constant number of factor updates
per step and has the same history storage order. Response memory replaces
this grid-dependent collection by a chosen number of evolving coordinates.

### 2.13 Operator and simpler-limit theories

A finite number of operators or fields may require infinitely many scalar
coordinates. Numerical cost depends on rank, structure, discretization,
and required observables. There is no justified universal result saying
every operator implementation must be a dense matrix or full history.
Those are two natural implementations, not an exhaustive classification.

Deep linear models, shallow mean-field models, GP initialization limits,
and frozen-kernel limits resolve different parts of the problem. They
do not by themselves satisfy all three requirements here: multiple hidden
layers, effective nonlinearities, and order-one feature learning.
Their accuracy rates cannot enter a same-model table without a reduction
to (1). Initial signal propagation and conditioning likewise do not alone
bound approximation to the trained function over \([0,T]\).

## 3. Optimize moving memory at error \(\varepsilon\)

These are optimal allocations within specified error bounds and
representations, not minimax lower bounds over every algorithm in a
framework. Keep the data, \(m,H,d,T\), and target fixed. Autonomous
ODE integration needs an additional error allowance; it changes work,
but does not create a stored physical-time history for dense, response
memory, or direct NTH.

### 3.1 Dense

Under \(E\le A/\sqrt n\), take \(n=\lceil(A/\varepsilon)^2\rceil\).
Then

\[
M_{\rm dense}^*(\varepsilon)\asymp
(H-1)A^4\varepsilon^{-4}+(d+1)A^2\varepsilon^{-2}.
\tag{46}
\]

Leading per-step work is \(O(HmA^4\varepsilon^{-4})\).

### 3.2 The two response clocks

Let \(q=1\) for the old clock and \(q=2\) for the joint clock. Under (22),
the leading moving state is \(2(H-1)mnP\). Set

\[
u=A/\sqrt n,\qquad v=B_q/P^q,\qquad u+v=\varepsilon.
\]

Then \(nP=A^2B_q^{1/q}u^{-2}(\varepsilon-u)^{-1/q}\). Logarithmic
differentiation gives \(-2/u+(1/q)/(\varepsilon-u)=0\).
The second derivative is positive and the objective diverges at either
endpoint. Thus the continuous optimum is

\[
u_*=\frac{2q}{2q+1}\varepsilon,\quad
v_*=\frac{\varepsilon}{2q+1},\quad
n_*=\left(\frac{(2q+1)A}{2q\varepsilon}\right)^2,\quad
P_*=\left(\frac{(2q+1)B_q}{\varepsilon}\right)^{1/q}.
\tag{47}
\]

Rounding upward preserves the asymptotic rates. Outer-weight and Gram
terms perturb the finite-\(\varepsilon\) optimum, but are lower order
as \(\varepsilon\downarrow0\) at a fixed task with positive constants.

For the old clock,

\[
n_*=\frac{9A^2}{4\varepsilon^2},\quad
P_*=\frac{3B_1}{\varepsilon},\quad
M_{\rm old}^*\sim\frac{27}{2}(H-1)mA^2B_1\varepsilon^{-3}.
\tag{48}
\]

For the joint clock,

\[
n_*=\frac{25A^2}{16\varepsilon^2},\quad
P_*=\sqrt{\frac{5B_2}{\varepsilon}},\quad
M_{\rm joint}^*\sim\frac{25\sqrt5}{8}(H-1)mA^2\sqrt{B_2}\,\varepsilon^{-5/2}.
\tag{49}
\]

Gram state is \(O(B_2/\varepsilon)\), and outer weights contribute
\(O((d+1)A^2/\varepsilon^2)\). Substitution into (26) gives old per-step
powers \(\varepsilon^{-4},\varepsilon^{-3}\), and joint powers
\(\varepsilon^{-4},\varepsilon^{-5/2},\varepsilon^{-3},\varepsilon^{-3/2}\).
With dense \(W_0\), leading total arithmetic and total storage therefore
still have an \(\varepsilon^{-4}\) term.

At fixed \(n\), balancing compression with the width floor gives
\(P\asymp\sqrt n\) or \(P\asymp n^{1/4}\), with task-dependent factors.
Moving states become \(O(Hmn^{3/2})\) and \(O(Hmn^{5/4})\).
If the available width rate is instead \(n^{-\alpha}\), optimized powers
are \(2/\alpha\) for dense and \(1/\alpha+1/q\) for response memory.
The width hypothesis is a substantive input.

### 3.3 NTH

Given a valid same-target bound \(\eta_p(m,H,T)\) and accurately available
population initial coefficients, define

\[
p_\varepsilon=\min\{p\ge2:\eta_p(m,H,T)\le\varepsilon\}.
\tag{50}
\]

Direct moving state is \(\sum_{j=1}^{p_\varepsilon-1}m^j\), while fixed
top state and per-step work are \(O(m^{p_\varepsilon})\).
If no certified order is known, this expression is unevaluated, not
a proof that the desired accuracy is impossible.

Under (34), put \(\lambda_q=\log(1/q)>0\). Solving
\(Dq^p/p\le\varepsilon\) gives

\[
p_\varepsilon=\max\left\{2,\left\lceil
\frac{W(\lambda_qD/\varepsilon)}{\lambda_q}
\right\rceil\right\},
\tag{51}
\]

where \(W(z)e^{W(z)}=z\). Indeed the inequality is equivalent to
\((\lambda_qp)e^{\lambda_qp}\ge\lambda_qD/\varepsilon\).
Using \(W(z)=\log z-\log\log z+o(1)\), for fixed \(m\ge2,D,q\),

\[
M_{\rm NTH}^*(\varepsilon)\asymp
\left(\frac{D}{\varepsilon\log(D/\varepsilon)}\right)^\alpha,
\qquad \alpha=\frac{\log m}{\log(1/q)}.
\tag{52}
\]

Use (39),(51) for exact sample dependence and integer rounding; constants
in (52) depend on \(m,q\). Ignoring logs gives power
\(\varepsilon^{-\alpha}\). Under the stronger exponential kernel bound,
factorial convergence instead permits
\(p=O(\log(1/\varepsilon)/\log\log(1/\varepsilon))\).
There is no established universal NTH exponent for rich tanh training.

For \(m=1\), the one-scalar construction shifts order dependence into
fixed coefficients/evaluation. NTK, \(p=2\), uses \(m\) moving scalars and
meets a tolerance only when its freezing bias and coefficient error fit.

### 3.4 Streamed TP/DMFT

Under (42), moving memory is \(O(Hm^2K^2)\). More streamed samples cost
work, not this leading memory. The memory-only optimum is a boundary
infimum obtained by assigning almost all error to time discretization:

\[
K_{\inf}=T(B_{\rm D}/\varepsilon)^{1/r},\qquad
M_{\rm D}^{\inf}\asymp
Hm^2T^2B_{\rm D}^{2/r}\varepsilon^{-2/r}.
\tag{53}
\]

A finite feasible choice, for fixed \(0<\beta<1\), is

\[
K=\left\lceil T\left(\frac{B_{\rm D}}{(1-\beta)\varepsilon}\right)^{1/r}\right\rceil,
\quad S\ge\left(\frac{2A_{\rm D}}{\beta\varepsilon}\right)^2,
\quad \eta\le\beta\varepsilon/2.
\tag{54}
\]

This attains the same scaling. Approaching the best memory constant with
\(\beta\downarrow0\) increases sampling/iteration work without bound.
There is no unique finite optimal \(S\) for memory alone.

For Euler accuracy the moving memory is
\(Hm^2T^2B_{\rm D}^2\varepsilon^{-2}\); a justified order-two solver gives
\(Hm^2T^2B_{\rm D}\varepsilon^{-1}\). These reflect numerical time order,
not an intrinsic epsilon exponent of TP or DMFT. Optimizing arbitrary
numerical order requires regularity and order-dependent costs/constants.

For fixed \(r,I\) and task, (41),(54) give amortized step work
\(O(\varepsilon^{-2-2/r})\) and total work
\(O(\varepsilon^{-2-3/r})\). Include any growth of \(I\) with tolerance.
Better response estimators can change this arithmetic model, with their
own variance and stability requirements.

### 3.5 Exact finite-width history

Optimize (45) with moving state \(Hm nK\). Repeating (47), now with
\(K=T(D_{\rm h}/v)^{1/r}\), gives

\[
M_{\rm history}^*\asymp
HmA^2T D_{\rm h}^{1/r}\varepsilon^{-(2+1/r)}.
\tag{55}
\]

Euler gives the power \(\varepsilon^{-3}\); a justified order-two
method gives \(\varepsilon^{-5/2}\). An epsilon exponent alone therefore
does not establish superiority over every history solver. This baseline
retains numerical updates, while response memory is an autonomous
prescribed-order history representation. Their constants, stability,
and approximation mechanisms differ.

## 4. Tables on the common axis

The tables suppress fixed \(d\) and numerical factors. They describe the
implementations above; the assumptions in the error column are part of
the comparison, not optional qualifications.

### 4.1 Computational state and arithmetic

| Implementation | Moving state | Main fixed resources | Work per RHS or grid step |
|---|---:|---|---:|
| Dense width \(n\) | \(Hn^2\) | Data and initialization procedure | \(Hmn^2\) |
| Old response clock | \(HmnP+n\) | \(Hn^2\) initialized matrices | \(Hmn^2+Hm^2nP+HmnP\) |
| Joint response clock | \(HmnP+n+P^2\) | \(Hn^2\) initialized matrices; prefix fields | \(Hmn^2+Hm^2nP+HmnP^2+P^3\) |
| Canonical frozen NTK | \(m\) | \(m^2\) kernel and test-kernel evaluator | \(m^2\) |
| Direct NTH through \(p\) | \(\sum_{j=1}^{p-1}m^j\) | Top tensor \(m^p\); initial mixed-kernel evaluators | \(m^p\) |
| Streamed full-grid TP/DMFT solver | \(Hm^2K^2\), including kernel/Jacobian workspace | Model and input covariance specification | \(IH(S+1)m^3K^2\), amortized |
| Exact finite-width response history | \(HmnK+n\) | \(Hn^2\) initialized matrices | \(Hmn^2+Hm^2nK\), near final step |

NTH counts are for the direct representation at \(m\ge2\); structure
can reduce them. TP/DMFT work describes the explicit samplewise-Jacobian
solver, not a lower bound on numerical implementations. Dense and closure
forward/backward activation workspace adds \(O(Hmn)\).

### 4.2 Error relative to the same population predictor

| Method | Error model uniform on \([0,T]\) | What supports it |
|---|---|---|
| Dense | \(A n^{-1/2}\) | Expected fluctuation law; general matched rate is an additional hypothesis |
| Old clock | \(A n^{-1/2}+B_1P^{-1}\) | Fixed-width \(P^{-1}\) theorem plus uniform-in-width control and dense width rate |
| Joint clock | \(A n^{-1/2}+B_2P^{-2}\) | Fixed-width \(P^{-2}\) theorem; (24) improves width accounting; uniform stability still needed |
| Canonical NTK | \(b_{\rm lazy}(T,Q)\) plus coefficient error | Freezing bias can persist under rich training |
| Matched NTH | \(\eta_p(T)\) from (32), plus coefficient error | Exact hierarchy and stated higher-kernel bounds; (34) is one sufficient regime |
| Sampled TP/DMFT | \(A_{\rm D}S^{-1/2}+B_{\rm D}(T/K)^r+\eta\) | Conditional uniform sampling, discretization, and solver stability |
| Finite-width full history | \(A n^{-1/2}+D_{\rm h}(T/K)^r\) | Dense width hypothesis and consistent stable time discretization |

The published NTH estimate (35)–(36) belongs in the explanation, not as
an allegedly equivalent population row: its parameterization and error
target differ.

### 4.3 Minimum sufficient moving memory under those error models

| Method | Scaling at error \(\varepsilon\) | Conditions and explicit dependence |
|---|---|---|
| Dense | \(H A^4\varepsilon^{-4}\) | Root-width law |
| Old clock | \(Hm A^2B_1\varepsilon^{-3}\) | Root-width plus width-uniform old-clock estimate |
| Joint clock | \(Hm A^2\sqrt{B_2}\varepsilon^{-5/2}\) | Root-width plus width-uniform joint estimate; lower-order Gram state |
| NTK | \(m\), when bias fits the tolerance | Fixed \(m^2\) kernel excluded consistently from moving memory |
| NTH, general | \(\sum_{j=1}^{p_\varepsilon-1}m^j\) | Order set by a same-target error certificate |
| NTH, regime (33) | \([D/(\varepsilon\log(D/\varepsilon))]^{\log m/\log(1/q)}\) | Fixed \(m\ge2,\ q<1\); (39),(51) retain exact sample dependence |
| Streamed TP/DMFT, time order \(r\) | \(Hm^2T^2B_{\rm D}^{2/r}\varepsilon^{-2/r}\) | Stable solver and enough streamed samples; memory infimum up to constants |
| Finite-width full history, time order \(r\) | \(Hm A^2T D_{\rm h}^{1/r}\varepsilon^{-(2+1/r)}\) | Width and numerical error hypotheses in (45) |

Constants remain method-dependent functions of the fixed task, including
\(m,H,T\). This table does not convert unknown time amplification into a
known polynomial in \(T\).

## 5. Reading the comparison

Response memory makes a definite structural change: retained learned
history is set by approximation order, and those coordinates keep evolving
through the current nonlinear network. The fixed-width trajectory theorem
controls feedback over a complete finite interval and extends to unseen
inputs. It is a compression of training dynamics, beyond fitting a snapshot.

The population interpretation needs an additional bridge: a width
approximation and compression constants controlled in normalized quantities.
Conditional on that bridge, the two optimized moving-memory laws follow
from (47). The improved estimate (24) supports the joint clock's anticipated
population scaling by removing an unnecessary width penalty.

NTH is a competing compression of evolving features. Its sample-index
tensors can become expensive, but the required order is governed by higher
kernel growth. Its memory does not become infinite merely because a
trajectory's time Taylor series stops converging. For a few samples and
controlled higher kernels it can be very compact, and (40) represents an
entire test function.

Numerical TP/DMFT can eliminate explicit width and dense initialization
matrices, which matters for total storage. Their solvers retain two-time
information and estimate self-consistent responses. Streaming converts
sample count into work without the same increase in peak memory. There is
therefore no compulsory \(\varepsilon^{-2}\) moving-memory sampling floor
shared by every method.

Once constants are known, concrete comparisons follow. Up to universal
factors, response moving state beats dense moving state when

\[
mB_1\varepsilon\lesssim A^2
\quad\hbox{or}\quad
m\sqrt{B_2}\varepsilon^{3/2}\lesssim A^2,
\tag{56}
\]

for the old and joint clocks. Against an Euler DMFT solver, their optimized
moving-memory ratios are proportional to

\[
\frac{A^2B_1}{mT^2B_{\rm D}^2}\varepsilon^{-1},
\qquad
\frac{A^2\sqrt{B_2}}{mT^2B_{\rm D}^2}\varepsilon^{-1/2}.
\tag{57}
\]

No universal long-training ranking follows from the explicit \(T^2\):
\(A,B_1,B_2,B_{\rm D}\) also depend on \(T\), potentially strongly.
Under (33), the NTH power in (52) can be compared with \(3\) and \(5/2\),
but \(q\) is a higher-kernel control parameter, not simply time divided by
the predictor's Taylor radius.

The published DMFT comparison \(n\gg mK\) uses grid length, not physical
time. Comparing kernel storage \(Hm^2K^2\) with dense parameters \(Hn^2\)
gives that threshold. With the explicit cost (41), total runtime versus
dense \(Hmn^2K\) instead requires roughly
\(n\gg mK\sqrt{I(S+1)}\), within this implementation's cost model.
Suppressing \(S,I\) can therefore change a practical ranking.

For final predictions, dense and response memory directly supply a network
function. Their per-query work is respectively \(O(Hn^2+nd)\) and
\(O(H(n^2+nmP)+nd)\). NTH uses (40) and its initial mixed-kernel evaluator.
DMFT performs passive prediction calculations. Numerically measuring
whole-circle RMSE adds integration or quadrature work for every method,
separately from the analytical error norm (3).

A fixed order gives response memory a state count independent of elapsed
steps. Maintaining one tolerance as the requested horizon grows may require
increasing that order. Current bounds do not establish uniform all-time
accuracy at fixed memory or a universal runtime advantage.

## 6. Discrepancies resolved from the supplied report

| Supplied claim | Correct statement |
|---|---|
| A general canonical deep \(n^{-1/2}\) bound follows from the cited mean-field literature | It is the useful fluctuation prediction here. The inspected rigorous rates concern different models/program classes; our matched population comparison states it as a hypothesis. |
| Input supremum and whole-space RMSE automatically have identical bounds | Equation (6) gives RMSE from integrable test-point estimates. A supremum needs spatial/probabilistic uniformity, potentially adding logarithms. |
| Both response clocks have the same arithmetic cost | The joint clock adds Gram factorization, solves across moment rows, and directional response passes; see (26). |
| NTH has \(m^p\) moving entries and NTK \(m^2\) | Their top tensor/kernel is fixed. Direct moving counts are (39) and \(m\); fixed storage and work are reported separately. |
| NTH is a time-Taylor truncation that cannot converge beyond its Taylor radius | False in general. Its ODE is not a time polynomial; (37)–(38) give a counterexample, and (32) provides a valid conditional bound. |
| NTH Theorem 2.6 has \(\min\{mt,m/\lambda\}\) and horizon \(\lambda n/m\) | Its RMS version has \(\min\{t,m/\lambda\}\) and the square-root horizon plus the second restriction in (36). |
| Monte Carlo TP is statistically a finite-width network stored as histories | No such equivalence follows. Equation (44) is a distinct exact finite-width baseline. Limiting-process sampling must account for reuse correlations. |
| \(S=n\) DMFT paths reproduce width-\(n\) fluctuations | This matches a formal exponent, not the covariance or distribution of the two approximations. |
| DMFT cost is exhausted by the paper's cubic table entry | Sampling, iterations, and samplewise response Jacobians are resources; (41) restores them for a specified implementation. |
| The threshold \(n\gg mT\) refers to physical time | The source comparison uses time-grid length. Memory gives \(n\gg mK\); explicit sampling/iterations further affect runtime. |
| Every method pays an \(\varepsilon^{-2}\) moving-memory sampling floor | Population coefficient methods need not store width-\(n\) neurons, and streaming need not retain all Monte Carlo samples. |
| Every exact operator implementation must be dense or full-history | No exhaustive no-go theorem justifies this. Operator structure and requested observables matter. |
| One exponent is the optimal memory of an entire framework | A representation, error certificate, numerical order, fixed resources, and streaming policy must first be specified. The report optimizes explicit models. |

## 7. Sources and provenance

Complete primary PDFs and extracted texts are retained in
[the source directory](/home/amir/Codes/PDE/data/generated/population_accuracy_complexity_20260927/full_texts).
[The manifest](/home/amir/Codes/PDE/data/generated/population_accuracy_complexity_20260927/full_texts/sources.json)
records URLs and file hashes. Relevant equations, hypotheses, proofs, and
algorithm descriptions were checked in the full texts.

- Huang and Yau, *Dynamics of Deep Neural Networks and Neural Tangent
  Hierarchy*, 39 pages. Definitions, Assumptions 2.1–2.2, Theorem 2.6,
  passive-test equation, and Appendix C.
  [Full text](https://arxiv.org/pdf/1909.08156).
- Yang and Hu, *Feature Learning in Infinite-Width Neural Networks*, full
  65-page version. Parameterization, recursive construction, Algorithm 1,
  and Master Theorem 7.4. [Full text](https://arxiv.org/pdf/2011.14522).
- Bordelon and Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel
  Evolution in Wide Neural Networks*, 55 pages. Scaling, two-time equations,
  Table 1, and Appendix B solver. [Full text](https://arxiv.org/pdf/2205.09653).
- Bordelon and Pehlevan, *Dynamics of Finite Width Kernel and Prediction
  Fluctuations in Mean Field Neural Networks*, 44 pages. Expansion,
  covariance feedback, and perturbative scope.
  [Full text](https://arxiv.org/pdf/2304.03408).
- Nguyen and Pham, *A Rigorous Framework for the Mean Field Limit of
  Multilayer Neural Networks*, 125 pages. Normalization, embeddings,
  Theorem 15, Remark 16, and Corollary 17.
  [Full text](https://arxiv.org/pdf/2001.11443).
- Agazzi, Mosig Garcia, and Trevisan, *Quantitative Gaussian-Process Limits
  of Tensor Programs*, 37 pages. Execution class and Theorem 1.2.
  [Full text](https://arxiv.org/pdf/2607.06290).
- Chen, Yang, Zhao, and Gu, *Global Convergence and Rich Feature Learning
  in L-Layer Infinite-Width Neural Networks under muP Parametrization*,
  28 pages. Infinite-width feature/convergence statements, distinguished
  from finite-width rates. [Full text](https://arxiv.org/pdf/2503.09565).

The response-memory construction and fixed-width theorems come from the
user's current [manuscript](/home/amir/Codes/PDE/paper/main.tex).
The population-limit discussion uses the author's **unpublished**
maintained book:
[local population flows](/home/amir/Codes/PDE/docs/03-local-population.qmd)
and [continuing flows](/home/amir/Codes/PDE/docs/04-continuing-flows.qmd).
These are not external published references.

The sharper joint-clock estimate (24), matched hierarchy comparison
(31)–(34), counterexample analysis (37)–(38), and resource optimizations
are derivations in this report. They do not claim new empirical validation
or an independently reviewed population theorem. No training experiments
or paper changes were made for this report.
