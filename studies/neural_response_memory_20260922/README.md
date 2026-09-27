# Response-memory compression of neural training

This study replaces the learned hidden-matrix increments of a neural network
by a fixed number of evolving forward/backward history moments per neuron.
The initialized matrices and their actual transposes are retained exactly.
The resulting autonomous dynamics use their own current responses, with no
stored training trajectory or reference-network feedback.

The main advances are:

- A derived history closure whose spatial directions evolve during learning,
  with a concrete reconstruction of the physical network at every time.
- Two variants: an **activity clock** with finite-horizon error
  \(O(P^{-1})\), and a **response clock with weighted projection** with error
  \(O(P^{-2})\), under the precise smoothness and order conditions below.
- Extension to any fixed number of hidden layers and broad smooth activation
  classes, at fixed finite width and dataset.
- Accurate reproduction of dense fitted predictors on several circle, sphere
  and MNIST tasks, including a successful comparison with rank-matched direct
  factor training. Accuracy and fitting are not uniform across tested settings.

Both variants are now implemented. The completed accuracy campaigns summarized
below primarily concern the activity clock; weighted-clock fitting validation
is recorded separately as current work.

The results retain the internal checks and numerical qualifications linked
below; they are not promoted book theorems. The bounds do not establish uniform
all-time or infinite-width convergence, universal low-order accuracy, or reduced
total network storage.
This README contains both constructions and a complete proof of their
finite-horizon guarantees in section 5. Linked notes retain the original
derivations, protocols and checks. Read sections 2–4 for the algorithms,
section 5 for the theorem and proof, and section 6 for empirical evidence.

## 1. Why move beyond frozen dictionaries?

The earlier dictionary models replace an entire middle matrix by

\[
\widehat W_2=B_2 C B_1^\top/n,
\]

with fixed initialization-derived tables \(B_1,B_2\), a trainable small core
\(C\), and moving first-layer weights and readout. Their input features can
learn nonlinearly, but the middle action remains confined to fixed left and
right spaces. They also replace the initialized operator: generally
\(\widehat W_2(0)\ne W_2(0)\).

Two constructions were studied. The original dictionary uses Chebyshev
polynomials of initialized response coordinates and retained matrix-action
words. The gradient-flow dictionary selects factors appearing in initialized
flow coefficients, including additional forward and reverse calls to the same
matrix. Neither uses the later task labels to construct its basis. Positive
ridge normalization makes their induced operators filters, rather than exact
orthogonal projections. Dictionary order, derivative order, rank and the
history order \(P\) below are different budgets.
The finite polynomial window and derivative-only lists tested empirically are
not the exhaustive observable-word hierarchy; these experiments do not decide
the convergence or efficiency of every richer initialized-observable scheme.

The main historical findings were:

| Question | Surviving result |
|---|---|
| Do initialized dictionaries help relative to random bases? | Yes on selected tasks, with genuine exceptions. A proposed advantage growing systematically with order did not survive fresh confirmation. |
| Are they preferable to smaller dense networks? | Dense controls matched by trainable-parameter or total-storage budget won all 12 tested fitted-function comparisons. |
| Does deriving more directions from gradient flow help? | The 38-vector derivative dictionary beat the old 45-vector dictionary on 8/11 tasks and each random control on 10/11. Increasing to 72 vectors improved 8/11 tasks but worsened mean RMS from 0.13554 to 0.14533. |
| Does unfreezing the dictionary solve the problem? | On the hard alternating/outlier task, trainable derivative-p3 improved RMS from 1.10012 to 0.89643, but remained worse than frozen p7 at 0.75642. This used factor-coordinate gradient flow, not dense-matrix gradient flow. |
| Was a general capacity obstruction established? | No. The unrestricted p1 population class is dense in continuous antipodally odd circle functions, using target-dependent population couplings. High-gain alternating-label fits showed some optimization advantages, but neither that construction nor failed dense fits proves a canonical-training advantage. |

Sources: [original dictionary and matched controls](../random_dictionary_learned_circle_20260920/MATCHED_NETWORK_RESULTS.md),
[scaling assessment](../random_dictionary_learned_circle_20260920/SCALING_ASSESSMENT.md),
[derivative suite](../gradient_flow_probe_dictionary_20260921/SUITE_RESULTS.md),
[higher orders](../gradient_flow_probe_dictionary_20260921/P7_RESULTS.md),
[trainable factors](../adaptive_response_compression_20260922/TRAINABLE_P3_RESULTS.md),
[population-design scope](../p1_circle_population_design_20260921/README.md),
and [alternating-label GD](../alternating_circle_fit_capacity_20260921/GD_RESULTS.md).
The separate [broad-ridge canonical pilot](../broad_ridge_canonical_probe_20260921/RESULTS.md)
also found no compression advantage: a smaller dense network fitted its sample,
while none of the terminal predictors improved on the zero predictor on unseen
data within the bounded pilot.

The earlier theory remains useful. The
[onset calculation](../closure_training_onset_20260921/ONSET.md) derives local
feature-learning corrections; its Gaussian peeling continuations evaluate the
initialized kernel, not the entire trained flow. The derivative study proves
an [all-time single-sample error certificate](../gradient_flow_probe_dictionary_20260921/SINGLE_SAMPLE_GLOBAL_BOUND.md)
at exactly zero readout in terms of omitted action/update defects, but does not
prove those defects decay with dictionary order. Its
[nested population limit](../gradient_flow_probe_dictionary_20260921/POPULATION_CONVERGENCE_ATTEMPT.md)
identifies the dictionary's own projected dynamics, with dense identification
still open. The separate
[adaptive-response proposal](../adaptive_response_compression_20260922/ASSESSMENT.md)
proves low-rank update-sketch and consistent Gaussian-query primitives; a
complete economical coupled solver was not established or tested there.

The present study changes the object being compressed: retain the initialized
operator and approximate the **accumulated learned interaction**. Temporal
polynomial coordinates are fixed, but their neuron-vector moments move with
the current responses. This allows new spatial directions during training.
It also leaves the cost of the initialized dense operator visible.

## 2. Network, loss and the history to compress

Start with two hidden layers of width \(n\), \(m\) equally weighted training
pairs \((x_a,y_a)\), and normalized inputs \(u_a=x_a/\sqrt d\). Define

\[
h_{1,a}=\phi(W_1u_a),\qquad h_{2,a}=\phi(W_2h_{1,a}),\qquad
f_a=\frac{W_3^\top h_{2,a}}n,\qquad r_a=f_a-y_a.
\]

The residual is separate from the backward responses:

\[
\delta_{2,a}=W_3\odot\phi'(W_2h_{1,a}),\qquad
\delta_{1,a}=\phi'(W_1u_a)\odot W_2^\top\delta_{2,a}.
\]

For unhalved mean squared loss \(\mathcal L=m^{-1}\sum_a r_a^2\) and
canonical block mobilities \((n,1,n)\), the physical gradient flow is

\[
\dot W_1=-\frac2m\sum_a r_a\delta_{1,a}u_a^\top,\qquad
\dot W_2=-\frac2{nm}\sum_a r_a\delta_{2,a}h_{1,a}^\top,\qquad
\dot W_3=-\frac2m\sum_a r_a h_{2,a}.
\]

Thus, with \(W_0=W_2(0)\),

\[
\boxed{W_2(t)=W_0-\frac2{nm}\sum_a\int_0^t
 r_a(s)\delta_{2,a}(s)h_{1,a}(s)^\top\,ds.}
\]

This integral is the target of compression. Dense training already stores its
accumulated weights rather than every past update; the closure replaces the
learned matrix that carries this history by evolving factors.

Historical canonical experiments use independent stored entries with standard
deviations \(1,1/\sqrt n,1/n\) for \(W_1,W_0,W_3\), respectively, and retain
the actual finite random readout. The finite-width convergence theorems allow
arbitrary finite initial arrays. Later stress experiments explicitly change
initialization gains/readout scale; they are identified separately below.

We write the history length as \(\tau\), called \(Q_{\rm length}\) or \(L\)
in some earlier notes. Hidden depth is denoted by \(L\) in this README.

## 3. Variant A: residual-activity Legendre memory

Let

\[
\rho=\sqrt{\frac1m\sum_a r_a^2},\qquad
\dot\tau=\rho,\qquad \tau(0)=1.
\]

The clock integrates the **value of residual RMS**, not its rate of decrease.
For one sample, \(\rho=|r|\). We prepend a unit history interval with constant
forward value \(h_{1,a}(0)\) and zero backward value. On the actual history,
the forward value is \(h_{1,a}\) and the backward value is
\(b_a=r_a\delta_{2,a}/\rho\) wherever \(\rho>0\).

Project these histories onto the first \(P\) shifted Legendre polynomials on
the current interval \([0,\tau]\). Each sample has vector moments
\(m_{1,a}^{(k)},m_{2,a}^{(k)}\in\mathbb R^n\), \(0\le k<P\). Each neuron
owns one entry of each vector. If bars denote the histories as functions of
activity coordinate \(\xi\), including the prefix, their precise definition is

\[
m_{1,a}^{(k)}=\int_0^\tau\overline h_{1,a}(\xi)p_k(\xi/\tau)\,d\xi,
\qquad
m_{2,a}^{(k)}=\int_0^\tau\overline b_a(\xi)p_k(\xi/\tau)\,d\xi.
\]

Here \(p_k\) has degree \(k\), \(p_k(1)=1\), and
\(\int_0^1p_jp_k=\mathbf1_{j=k}/(2k+1)\); section 5.3 derives these
polynomials and their needed identities from Rodrigues' formula.
Differentiating the defining integrals gives

\[
\begin{aligned}
\dot m_{1,a}^{(k)}&=\rho h_{1,a}
 -\frac\rho\tau\left[km_{1,a}^{(k)}+
                  \sum_{j<k}(2j+1)m_{1,a}^{(j)}\right],\\
\dot m_{2,a}^{(k)}&=r_a\delta_{2,a}
 -\frac\rho\tau\left[km_{2,a}^{(k)}+
                  \sum_{j<k}(2j+1)m_{2,a}^{(j)}\right].
\end{aligned}
\]

Initially \(m_{1,a}^{(0)}=h_{1,a}(0)\), and all other moments are zero.
For example,

\[
m_{1,a}^{(0)}=h_{1,a}(0)+\int_0^t\rho h_{1,a}\,ds,\qquad
m_{2,a}^{(0)}=\int_0^t r_a\delta_{2,a}\,ds.
\]

The reconstructed matrix is

\[
\boxed{\widehat W_2=W_0-\frac2{nm\tau}
 \sum_{a=1}^m\sum_{k=0}^{P-1}(2k+1)
 m_{2,a}^{(k)}(m_{1,a}^{(k)})^\top.}
\]

Every response in the moment equations is evaluated at this reconstructed
network. The outer weights follow the displayed canonical equations at that
same network. The full feedback is therefore

\[
\text{moments}\ \longrightarrow\ \widehat W_2
\ \longrightarrow\ \text{responses and residuals}
\ \longrightarrow\ \text{moment and outer-weight velocities}.
\]

The coefficients are derived from interval dilation, not fitted damping.
The sole physical modeling approximation is the truncated history pairing.
The equations are nonlinear through the responses; polynomial history
coordinates do not impose polynomial trajectories. They require no temporal
Taylor convergence. For tanh, an exact response lift using
\(\phi'=1-\phi^2\) additionally permits rational ODE coordinates; the current
direct-activation implementation need not integrate that redundant lift.

The raw equations never divide by \(\rho\). At zero residual they freeze,
which permits a plateau but does not itself prove that fitting occurs or that
the closure loss decreases monotonically.

Full construction: [MOMENT_CONSTRUCTION.md](MOMENT_CONSTRUCTION.md) and
[RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md](RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md).

## 4. Variant B: response clock and weighted history projection

The activity clock does not directly control how fast all encoded responses
change. The second construction uses the explicit current-state monitor

\[
\Psi=\operatorname{concat}_{a=1}^m(h_{1,a},b_a),\qquad
b_a=\frac{r_a\delta_{2,a}}\rho,\qquad
\boxed{\dot\tau=g=\rho+\|\dot\Psi\|_2,\quad\tau(0)=1.}
\]

For one sample, \(b=\operatorname{sign}(r)\delta_2\). On a regular interval
with nonzero residual its sign is constant, so the clock is simply
\(g=|r|+\sqrt{\|\dot h_1\|_2^2+\|\dot\delta_2\|_2^2}\).
Thus it adds the path speed of the encoded responses to residual activity.

The norm is ordinary, unscaled Euclidean norm across neurons and samples.
Consequently \(\|d\Psi/d\tau\|_2\le1\) wherever the clock moves. It controls
joint response speed; it does not equalize every neuron's speed or optimize
the actual Legendre error. Constant clock rescaling alone gives no gain.

Two details make this a different finite-order family from Variant A.

**Keep the learning measure.** Place the response at history coordinate
\(\xi=\tau(t)\), but insert mass \(\rho(t)\,dt\), not \(g(t)\,dt\).
Together with a unit Lebesgue prefix on \([0,1]\), this defines a measure
\(\mu_t\) on \([0,\tau(t)]\). It satisfies \(d\mu_t\le d\xi\).

**Match both initial histories.** On the prefix set the histories to
\(h_{1,a}(0),b_a(0)\). This removes the artificial backward jump present in
Variant A. Subtract its known product when reconstructing the learned matrix.
If the initial residual is zero, use stationary evolution and do not divide
by \(\rho\).

Let \(p_k\) be the shifted Legendre polynomials on \([0,1]\). Store the
weighted moments as columns of \(n\times P\) matrices \(H_a,U_a\), and one
shared \(P\times P\) Gram matrix:

\[
\begin{aligned}
H_{a,:,k}&=\int h_a(\xi)p_k(\xi/\tau)\,d\mu_t(\xi),\\
U_{a,:,k}&=\int b_a(\xi)p_k(\xi/\tau)\,d\mu_t(\xi),\\
G_{jk}&=\int p_j(\xi/\tau)p_k(\xi/\tau)\,d\mu_t(\xi).
\end{aligned}
\]

Here \(h_a(\xi),b_a(\xi)\) denote the inserted histories, including the
prefix. Weighted orthogonal projection gives

\[
\boxed{\widehat W_2=W_0-\frac2{nm}\sum_a
 \left[U_aG^{-1}H_a^\top-b_a(0)h_{1,a}(0)^\top\right].}
\]

Initially only the zeroth columns of \(H_a,U_a\) are nonzero, equal to
\(h_{1,a}(0),b_a(0)\), and \(G_{kk}=1/(2k+1)\), with zero off-diagonals.
Thus \(\widehat W_2(0)=W_0\) exactly. The unit prefix makes \(G\) positive
definite at fixed finite order and finite clock length, without guaranteeing
good numerical conditioning.

These quantities obey a finite ODE. Let \(e=(1,\ldots,1)^\top\) and let
\(A_{kk}=k\), \(A_{kj}=2j+1\) for \(j<k\), and zero otherwise. Then

\[
\begin{aligned}
\dot H_a&=\rho h_{1,a}e^\top-(g/\tau)H_aA^\top,\\
\dot U_a&=r_a\delta_{2,a}e^\top-(g/\tau)U_aA^\top,\\
\dot G&=\rho ee^\top-(g/\tau)(AG+GA^\top).
\end{aligned}
\]

The clock is explicit despite depending on response derivatives. Solve
\(Gq=e\), set \(h_a^\star=H_aq\), \(b_a^\star=U_aq\), and differentiate
the reconstruction. Every \(g/\tau\) term cancels, leaving

\[
V_2:=\dot{\widehat W}_2=-\frac2{nm}\sum_a
 \left[r_a\delta_{2,a}(h_a^\star)^\top
 +\rho b_a^\star(h_{1,a}-h_a^\star)^\top\right].
\]

Compute the canonical outer velocities, then directional forward derivatives,
output/residual derivatives and differentiated backpropagation. In particular,

\[
\dot\rho=\frac{\sum_a r_a\dot r_a}{m\rho},\qquad
\dot b_a=\frac{\dot r_a\delta_{2,a}+r_a\dot\delta_{2,a}}\rho
             -b_a\frac{\dot\rho}\rho.
\]

Now \(\dot\Psi\), hence \(g\), is known. This needs no implicit clock solve,
future trajectory, full Jacobian or loss Hessian. Use linear solves with
\(G\), not an explicitly formed inverse. Both matrix orientations use the
same factors and Gram matrix.

Full equations: [RESPONSE_CLOCK_FULL_CLOSURE.md](RESPONSE_CLOCK_FULL_CLOSURE.md).
Its earlier conservative approximation estimate is strengthened by
[RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md](RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md)
and the deep theorem below. Its historical statement that the solver was not
implemented is superseded by the current implementation in section 9.

## 5. Complete finite-horizon statements and proofs

Here **global finite-horizon convergence** means that the horizon \(T\) may
be any prescribed finite physical time. It does not mean one error bound
uniform over \(0\le t<\infty\). We prove the statements below without
assuming that the closure stays bounded, that its loss decreases, or that
the response clock has a bounded length. The physical-state and clock bounds
are part of the proof; closure-loss monotonicity is neither assumed nor proved.

The proof has four parts: derive exact identities for the compression error;
prove the polynomial approximation estimate; bound the closure on a region
fixed by the initial data; and show that a sufficiently accurate closure
cannot leave that region. The simple clock needs an additional induction
through the hidden layers. The response clock instead controls the joint
history derivative directly.

### 5.1 Model at arbitrary fixed depth and the exact claim

Fix positive integers \(n,d,m\), a hidden depth \(L\ge2\), finite data
\((x_a,y_a)\in\mathbb R^d\times\mathbb R\), and arbitrary finite initial
weights, with \(W_1\in\mathbb R^{n\times d}\),
\(W_\ell\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and
\(w\in\mathbb R^n\). There are no biases or normalization layers. Write
\(u_a=x_a/\sqrt d\), and use possibly different scalar activations
\(\phi_\ell\), applied coordinatewise:

\[
\begin{aligned}
z_{1,a}&=W_1u_a,& h_{1,a}&=\phi_1(z_{1,a}),\\
z_{\ell,a}&=W_\ell h_{\ell-1,a},&
h_{\ell,a}&=\phi_\ell(z_{\ell,a})\quad(2\le\ell\le L),\\
f_a&=w^\top h_{L,a}/n,&r_a&=f_a-y_a,\qquad
\rho^2=m^{-1}\sum_a r_a^2.
\end{aligned}
\]

Here \(w=W_{L+1}\) is the readout, called \(W_3\) in the two-hidden-layer
setup. The backward recurrence is

\[
\delta_{L,a}=w\odot\phi_L'(z_{L,a}),\qquad
\delta_{\ell,a}=\phi_\ell'(z_{\ell,a})\odot
 W_{\ell+1}^\top\delta_{\ell+1,a}\quad(1\le\ell<L).
\]

The loss is \(\mathcal L=\rho^2\). With block mobilities
\((n,1,\ldots,1,n)\), its gradient-flow field \(F\) is

\[
\begin{aligned}
F_1&=-\frac2m\sum_a r_a\delta_{1,a}u_a^\top,\\
F_\ell&=-\frac2{nm}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^\top
 \quad(2\le\ell\le L),\\
F_w&=-\frac2m\sum_a r_a h_{L,a}.
\end{aligned}
\]

These formulas follow by the chain rule: the three kinds of output gradient
are \(\delta_{1,a}u_a^\top/n\),
\(\delta_{\ell,a}h_{\ell-1,a}^\top/n\), and \(h_{L,a}/n\).
Multiplication by \(2r_a/m\), summation and the stated mobilities give \(F\).

Let \(\theta=(W_1,\ldots,W_L,w)\), with
\(\|\theta\|^2=\sum_{\ell=1}^L\|W_\ell\|_F^2+\|w\|_2^2\).
All norms below are ordinary Euclidean or Frobenius norms, with sample
averages written explicitly. The dense solution satisfies \(\dot\theta=F(\theta)\).

For each internal link \(2\le\ell\le L\), use the histories
\(h_{\ell-1,a}\) and \(b_{\ell,a}=r_a\delta_{\ell,a}/\rho\).
Variant A applies section 3 separately to these links with one shared clock.
In matrix notation its moment columns are \(H_{\ell,a},U_{\ell,a}\), and

\[
\widehat W_\ell=W_{\ell,0}-\frac2{nm\tau}
 \sum_{a,k<P}(2k+1)U_{\ell,a,:,k}H_{\ell,a,:,k}^\top.
\]

Variant B applies section 4 to the same links, shares one Gram matrix, and uses

\[
\begin{aligned}
\Psi&=\operatorname{concat}_{\ell=2}^L
          \operatorname{concat}_{a=1}^m(h_{\ell-1,a},b_{\ell,a}),
 &\dot\tau&=\rho+\|\dot\Psi\|_2,\\
\widehat W_\ell&=W_{\ell,0}-\frac2{nm}\sum_a
 [U_{\ell,a}G^{-1}H_{\ell,a}^\top
       -b_{\ell,a}(0)h_{\ell-1,a}(0)^\top].
\end{aligned}
\]

In both cases the outer weights satisfy \(\dot W_1=F_1(\widehat\theta)\),
\(\dot w=F_w(\widehat\theta)\), and every response is computed from the
closure's own reconstructed network. There is no dense reference in the
algorithm. The raw moment equations are exactly those in sections 3–4,
with the link index added. Initially the physical weights equal \(\theta_0\).

**Theorem.** For every finite \(T\ge0\), the following statements hold.

| Construction | Activation assumptions | Conclusion |
|---|---|---|
| Variant A | Every \(\phi_\ell\in C^{1,1}_{\rm loc}(\mathbb R)\) | There are finite \(P_A(T),C_A(T)\), independent of \(P\), such that for every integer \(P\ge P_A(T)\) the closure exists uniquely on \([0,T]\) and \(\sup_{t\le T}\lVert\widehat\theta_P(t)-\theta(t)\rVert\le C_A(T)/\sqrt{P(P+1)}\). |
| Variant B | \(\phi_1\in C^{1,1}_{\rm loc}\), and \(\phi_\ell\in C^{2,1}_{\rm loc}\) for \(2\le\ell\le L\) | There are finite \(P_B(T),C_B(T),\Lambda_T\), independent of \(P\), such that for every integer \(P\ge P_B(T)\) the closure exists uniquely and regularly on \([0,T]\), \(\tau_P\le\Lambda_T\), and \(\sup_{t\le T}\lVert\widehat\theta_P(t)-\theta(t)\rVert\le C_B(T)/[P(P+1)]\). |

Here \(C^{k,1}_{\rm loc}\) means \(k\) continuous derivatives with the last
locally Lipschitz. A regular Variant B state has \(\rho>0\), finite
\(\tau>0\), and positive-definite \(G\). If \(\rho(0)=0\), prescribe
stationary evolution instead; both closures then equal the stationary dense
network, without evaluating \(r/\rho\). For \(L=1\) there is no internal
matrix to compress and the approximation is exact.

All constants depend only on the fixed data, initialization, dimensions,
depth, activations and \(T\). Gaussian initialization, successful fitting
and geometric compatibility of the labels are unnecessary. In particular,
GELU and other unbounded smooth activations are allowed.

**All-order addition for Variant A.** If every activation and its first
derivative are globally bounded, in addition to \(C^{1,1}_{\rm loc}\), then
Variant A exists uniquely for all physical times at every \(P\ge1\).
Its displayed error bound holds at every order, with one \(C_A(T)\)
independent of \(P\). This includes tanh and sigmoid. No corresponding
all-order global-existence claim for Variant B is made.

### 5.2 Why these are explicit finite ODEs

The common history measure can be written precisely as

\[
\int v(\xi)\,d\mu_t(\xi)
 =\int_0^1v(\xi)\,d\xi
   +\int_0^t v(\tau(s))\rho(s)\,ds.
\]

For Variant A, \(\dot\tau=\rho\), so this is Lebesgue measure on
\([0,\tau]\). For Variant B its density on the actual history is
\(\rho/g\le1\), so \(d\mu_t\le d\xi\). Previously inserted values of
all histories are fixed. Only their polynomial coordinates change.

Let \(p=(p_0,\ldots,p_{P-1})^\top\), \(e=(1,\ldots,1)^\top\), and use
the triangular matrix \(A\) from section 4. The identity
\(x p'(x)=A p(x)\), proved in section 5.3, gives

\[
\partial_t p(\xi/\tau)=-(g/\tau)A p(\xi/\tau)
\]

at a fixed historical coordinate \(\xi\). Differentiating each moment
integral therefore gives its source term \(\rho f e^\top\) and its
dilation term \(-(g/\tau)B_fA^\top\). This proves the moment equations,
rather than positing relaxation coefficients. Conversely, along any local
solution, the defining integrals solve these same linear equations with the
same initial values. Their difference solves a homogeneous linear ODE with
zero initial value, hence vanishes. The integral interpretation is therefore
valid for the autonomous closure's own histories.

For Variant A set \(G=\tau\operatorname{diag}_{k<P}(1/(2k+1))\); it need
not be stored. For either variant the projection of a vector history with
moment matrix \(B_f\) is

\[
(\Pi_t f)(\xi)=B_fG^{-1}p(\xi/\tau),\qquad f^\star=B_fG^{-1}e.
\]

Its residual has zero moments against each basis polynomial, which proves
orthogonality and the least-squares minimizing property. The product of the
two projected histories integrates to \(UG^{-1}H^\top\). In Variant B
subtracting the fixed matching-prefix product removes its artificial
learning contribution. In Variant A that prefix product is already zero.

Differentiating \(G^{-1}G=I\) gives

\[
\frac d{dt}G^{-1}
 =-\rho G^{-1}ee^\top G^{-1}
       +(g/\tau)(G^{-1}A+A^\top G^{-1}).
\]

Insert this and the two moment equations into the product rule. The dilation
terms cancel in pairs, giving the clock-independent physical velocity

\[
V_\ell:=\dot{\widehat W}_\ell
 =-\frac{2\rho}{nm}\sum_a
 [b_{\ell,a}(h_{\ell-1,a}^\star)^\top
       +b_{\ell,a}^\star(h_{\ell-1,a}-h_{\ell-1,a}^\star)^\top].
\]

Thus the response clock contains no circular definition. Set \(V_1=F_1\),
\(V_w=F_w\), and compute, in forward layer order,

\[
\begin{aligned}
\dot z_{1,a}&=V_1u_a,\\
\dot z_{\ell,a}&=V_\ell h_{\ell-1,a}
                     +\widehat W_\ell\dot h_{\ell-1,a},\\
\dot h_{\ell,a}&=\phi_\ell'(z_{\ell,a})\odot\dot z_{\ell,a},\\
\dot r_a&=(V_w^\top h_{L,a}+w^\top\dot h_{L,a})/n,\qquad
\dot\rho=\frac1{m\rho}\sum_a r_a\dot r_a.
\end{aligned}
\]

Then differentiate backpropagation in reverse order, only down to layer two
(the middle recurrence below has \(2\le\ell<L\)):

\[
\begin{aligned}
\dot\delta_{L,a}
 &=V_w\odot\phi_L'(z_{L,a})
   +w\odot\phi_L''(z_{L,a})\odot\dot z_{L,a},\\
\dot\delta_{\ell,a}
 &=\phi_\ell''(z_{\ell,a})\odot\dot z_{\ell,a}
             \odot\widehat W_{\ell+1}^\top\delta_{\ell+1,a}\\
 &\quad+\phi_\ell'(z_{\ell,a})\odot
       (V_{\ell+1}^\top\delta_{\ell+1,a}
           +\widehat W_{\ell+1}^\top\dot\delta_{\ell+1,a}),\\
\dot b_{\ell,a}
 &=(\dot r_a\delta_{\ell,a}+r_a\dot\delta_{\ell,a})/\rho
                   -b_{\ell,a}\dot\rho/\rho.
\end{aligned}
\]

Concatenate the resulting derivatives to obtain \(\dot\Psi\), evaluate
\(g\), and then evaluate the moment/Gram derivatives. This explains both
implementability and why \(\phi_1''\) is not required by Variant B.
Only directional derivatives and solves with \(G\) are used. No full
Jacobian, Hessian or learned dense matrix is necessary.

Variant A's raw vector field is locally Lipschitz for \(\tau>0\), including
zero residual, because it uses \(r_a\delta_{\ell,a}\), not division by
\(\rho\). Variant B's field is locally Lipschitz on its regular domain:
\(\Psi\) has a locally Lipschitz derivative there, inverse Gram is smooth,
and the Euclidean norm is Lipschitz. For either field, local existence and
uniqueness follow by applying contraction to
\(s(t)=s(0)+\int_0^t V(s(v))\,dv\) on a small closed ball of continuous
paths: choose the interval so the bounded field maps that ball into itself
and its Lipschitz constant times the interval length is less than one.
The continuation proofs below ensure that the solution does not leave this
domain before the claimed horizon.

### 5.3 The needed Legendre estimate, with its proof

Define the shifted Legendre polynomials by Rodrigues' formula

\[
p_k(x)=\frac1{k!}\frac{d^k}{dx^k}[x^k(x-1)^k],\qquad 0\le x\le1.
\]

They have degree \(k\), leading coefficient \((2k)!/(k!)^2\), and
\(p_k(1)=1\). Integrating by parts \(k\) times shows that \(p_k\) is
orthogonal to every polynomial of degree less than \(k\): all boundary
terms vanish because \(x^k(x-1)^k\) has zeros of order \(k\) at both
ends. The same calculation with \(p_k\) itself gives

\[
\int_0^1p_k^2\,dx
 =\frac{(2k)!}{(k!)^2}\int_0^1x^k(1-x)^k\,dx
 =\frac1{2k+1}.
\]

The last integral is \((k!)^2/(2k+1)!\), obtained by repeated integration
by parts. For \(j<k\), another integration by parts gives
\(\int_0^1 xp_k'p_j\,dx=1\): the endpoint at one is one, and the
remaining integrand pairs \(p_k\) with a polynomial of degree at most
\(j\). The leading coefficient of \(xp_k'\) supplies its coefficient
\(k\) along \(p_k\). Thus

\[
x p_k'=k p_k+\sum_{j<k}(2j+1)p_j,
\]

which proves the dilation identity used above.

The differential operator \(\mathcal A v=-(x(1-x)v')'\) preserves
polynomial degree and is symmetric under integration on \([0,1]\), since
its boundary factor vanishes. Its leading coefficient on a degree-\(k\)
polynomial is multiplied by \(k(k+1)\). For \(j<k\), symmetry gives
\(\langle\mathcal A p_k,p_j\rangle=\langle p_k,\mathcal A p_j\rangle=0\).
The polynomial \(\mathcal A p_k-k(k+1)p_k\) therefore has degree less
than \(k\) and is orthogonal to every polynomial of that degree, including
itself. It is zero. In particular,

\[
\int_0^1x(1-x)p_k'p_j'\,dx
 =\frac{k(k+1)}{2k+1}\,\mathbf1_{k=j}.
\]

Let \(v\in H^1(0,1;\mathbb R^q)\), meaning that it is absolutely
continuous and \(v,v'\) are square-integrable. Its vector coefficients are
\(c_k=(2k+1)\int_0^1v p_k\,dx\). Integration by parts in the differential
equation yields

\[
\int_0^1x(1-x)v'p_k'\,dx
 =\frac{k(k+1)}{2k+1}c_k.
\]

Bessel's inequality for the orthogonal derivatives, applied componentwise,
now gives

\[
\sum_{k\ge1}\frac{k(k+1)}{2k+1}\|c_k\|_2^2
 \le\int_0^1x(1-x)\|v'\|_2^2\,dx.
\]

For clarity, the Bessel inequality here follows by subtracting any finite
orthogonal sum from \(v'\), expanding its nonnegative squared norm, and
then increasing the number of terms. Polynomial completeness supplies the
corresponding Parseval tail for \(v\). Only completeness for continuous
functions is needed here, since \(v\in H^1\) has an absolutely continuous
representative. Bernstein polynomials approximate every continuous function
uniformly: write the
Bernstein polynomial as \(\mathbb E[v(Z/N)]\), where \(Z\) is binomial
with mean \(Nx\). Uniform continuity controls \(|Z/N-x|\le\eta\), while
\(\mathbb P(|Z/N-x|>\eta)\le1/(4N\eta^2)\) controls its complement.
First choose \(\eta\), then \(N\). This proves the required density.

Every omitted mode has \(k\ge P\), so

\[
\|v-\Pi_Pv\|_{L^2(0,1)}^2
 =\sum_{k\ge P}\frac{\|c_k\|_2^2}{2k+1}
 \le\frac{\|v'\|_{L^2(0,1)}^2}{4P(P+1)}.
\]

Rescale \(v(x)=f(\tau x)\). With \(\lambda_P=P(P+1)\), this proves

\[
\|f-\Pi_Pf\|_{L^2(0,\tau)}^2
 \le\frac{\tau^2}{4\lambda_P}
                 \|\partial_\xi f\|_{L^2(0,\tau)}^2. \tag{1}
\]

We also need an endpoint bound for a polynomial \(q\) of degree less
than \(P\). Expand it in \(p_k(\xi/\tau)\) and apply Cauchy–Schwarz
at \(\xi=\tau\), using \(\sum_{k<P}(2k+1)=P^2\). It gives

\[
\|q(\tau)\|_2\le\frac P{\sqrt\tau}\|q\|_{L^2(0,\tau)}. \tag{2}
\]

This bound grows with \(P\); the old-clock proof will show precisely where
that growth cancels, rather than assuming uniformly accurate endpoints.

### 5.4 Exact error identities for both constructions

For one inserted vector history \(f\), define its projection energy

\[
D_f(t)=\|f-\Pi_t f\|_{L^2(\mu_t)}^2
 =\int\|f\|_2^2\,d\mu_t
           -\operatorname{tr}(B_fG^{-1}B_f^\top).
\]

The raw energy derivative is \(\rho\|f_{\rm current}\|_2^2\).
Using the inverse-Gram formula and the moment ODE gives

\[
\frac d{dt}\operatorname{tr}(B_fG^{-1}B_f^\top)
 =\rho\,[2\langle f_{\rm current},f^\star\rangle-\|f^\star\|_2^2].
\]

Indeed the two differentiated moment factors cancel the two inverse-Gram
dilation terms; the inverse-Gram source contributes
\(-\rho\|B_fG^{-1}e\|_2^2\). Subtracting gives

\[
\dot D_f=\rho\|f_{\rm current}-f^\star\|_2^2,\qquad
D_f(t)=\int_0^t\rho\|f_{\rm current}-f^\star\|_2^2\,ds. \tag{3}
\]

The initial energy is zero because every prefix is constant, including the
zero backward prefix. No derivative of that backward history is used.
The polynomial space consists of all degree-\(<P\) polynomials in \(\xi\);
its moving basis does not change that space. This is why dilation cancels.

Write \(D_{h,\ell,a}\) for the energy of the forward history
\(h_{\ell-1,a}\) at link \(\ell\), and \(D_{b,\ell,a}\) for its backward
history. Subtracting \(F_\ell\) from the velocity in section 5.2 gives

\[
\dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
\quad E_\ell=\frac{2\rho}{nm}\sum_a
 (b_{\ell,a}-b_{\ell,a}^\star)
 (h_{\ell-1,a}-h_{\ell-1,a}^\star)^\top. \tag{4}
\]

The outer-product Frobenius norm is the product of its vector norms.
Cauchy–Schwarz in time and (3) therefore imply

\[
\int_0^t\|E_\ell\|_F\,ds
 \le\frac2{nm}\sum_a\sqrt{D_{b,\ell,a}(t)D_{h,\ell,a}(t)}. \tag{5}
\]

This bounds the integral of the defect's norm, and hence also its signed
integral. Explicitly, let

\[
W_\ell^{\rm acc}(t)=W_{\ell,0}
 -\frac2{nm}\sum_a\int_0^t
 \widehat r_a\widehat\delta_{\ell,a}\widehat h_{\ell-1,a}^\top\,ds,
\quad R_\ell=\widehat W_\ell-W_\ell^{\rm acc}.
\]

Then \(R_\ell(0)=0\), \(\dot R_\ell=E_\ell\). These accumulators are
proof devices, not extra algorithmic state. Orthogonality also gives directly

\[
\int bh^\top\,d\mu-\int(\Pi_t b)(\Pi_t h)^\top\,d\mu
 =\int(b-\Pi_t b)(h-\Pi_t h)^\top\,d\mu. \tag{6}
\]

Each mixed term vanishes because a projected component is a polynomial and
a residual component is orthogonal to all such polynomials. Formula (6)
explains why two first-order approximation errors yield a second-order
learned-weight error. Formula (5) additionally controls the response clock.

### 5.5 Dense global existence and constants fixed by the initial data

Let \(\mathcal M\) denote the diagonal block-mobility operator. Its largest
eigenvalue is \(n\), and \(F=-\mathcal M\nabla\mathcal L\). On any local
dense solution,

\[
\frac d{dt}\mathcal L
 =-\|\mathcal M^{-1/2}\dot\theta\|^2,
\qquad \int_0^t\|\dot\theta\|^2\,ds\le n\rho(0)^2.
\]

Cauchy–Schwarz gives
\(\|\theta(t)-\theta_0\|\le\sqrt{nt}\,\rho(0)\).
If a maximal existence time were finite, the same estimate between any two
times approaching it would make the path Cauchy. Its finite limit has a
local solution because \(F\) is locally Lipschitz. Continuing there
contradicts maximality. Thus the dense solution exists uniquely for all
physical times, even for unbounded activations in the theorem's class.

Fix \(T>0\), \(\rho_0=\rho(0)>0\), and the convex physical-state ball

\[
R=\|\theta_0\|+\sqrt{nT}\rho_0+1,\qquad
\mathcal B=\{\theta:\|\theta\|\le R\}.
\]

The dense trajectory stays at least distance one from its boundary. All
closure estimates are first used only before a possible exit from this ball.
Here is a concrete way to obtain the finite constants we need. Put
\(X=\max_a\|u_a\|\), \(M_0=X\), and recursively set

\[
\begin{aligned}
s_\ell&=\sup_{|z|\le RM_{\ell-1}}|\phi_\ell'(z)|,
&M_\ell&=\sqrt n\sup_{|z|\le RM_{\ell-1}}|\phi_\ell(z)|,\\
B_L&=R s_L,
&B_\ell&=s_\ell R B_{\ell+1}\quad(\ell<L).
\end{aligned}
\]

On \(\mathcal B\), \(\|h_{\ell,a}\|\le M_\ell\) and
\(\|\delta_{\ell,a}\|\le B_\ell\). Let

\[
\begin{aligned}
Y&=\sqrt{m^{-1}\sum_a y_a^2},&q&=RM_L/n+Y,& S&=Tq,&\ell_T&=1+S,\\
v_1&=2B_1X,&v_\ell&=2B_\ell M_{\ell-1}/n\ (\ell\ge2),&v_w&=2M_L,\\
V&=\sqrt{v_1^2+\sum_{\ell=2}^L v_\ell^2+v_w^2},&&&\\
c_f&=\frac1n\sqrt{(B_1X)^2+
             \sum_{\ell=2}^L(B_\ell M_{\ell-1})^2+M_L^2}.&&&&
\end{aligned}
\]

Sample Cauchy–Schwarz in \(F\) gives \(\|F_\ell\|\le v_\ell\rho\)
and \(\|F\|\le V\rho\). The output-gradient blocks displayed in
section 5.1 give \(\|\nabla f_a\|\le c_f\), so on the convex ball both
prediction RMS distance and residual RMS distance are at most
\(c_f\|\theta'-\theta\|\). Also \(\rho\le q\), hence
\(\int_0^t\rho\,ds\le S\).

Choose a finite Lipschitz constant \(K\) of \(F\) on \(\mathcal B\).
Such a constant follows by splitting the finitely many response products,
using the above bounds and the local Lipschitz bounds of \(\phi_\ell'\)
on the displayed intervals. Equivalently, take the supremum of the difference
quotient of this locally Lipschitz field on the compact convex ball; a finite
cover by local Lipschitz neighborhoods and subdivision of line segments shows
that the supremum is finite. This specifies a constant from finite input
data and activation bounds, not from a supplied future trajectory.

Finally, on the dense trajectory while \(\rho>0\),
\(|\dot\rho|\le c_f\|F\|\le c_f V\rho\). Integration of
\(\dot\rho\ge-c_f V\rho\) gives

\[
\rho_{\rm dense}(t)\ge\mu:=\rho_0 e^{-c_fVT}>0\quad(t\le T). \tag{7}
\]

A first zero would contradict this estimate and continuity. This lower bound
is needed only for the response-clock proof.

### 5.6 Variant A: derivative control at every fixed depth

Work on a regular closure segment inside \(\mathcal B\). Then
\(1\le\tau\le\ell_T\). A nonstationary Variant A solution cannot reach
zero residual at a finite regular state: all raw velocities vanish there,
and local uniqueness applied backward from that equilibrium precludes an
arrival from a different state. Thus \(\xi=\tau(t)\) is a valid coordinate
on each compact segment under consideration.

A prime in this subsection means differentiation in \(\xi\). Extend each
forward history constantly over the prefix, and define

\[
Z_\ell(t)=\frac1m\sum_a\int_0^{\tau(t)}
                 \|h_{\ell,a}'(\xi)\|^2\,d\xi.
\]

These energies are finite on every compact regular segment. From (1),

\[
\frac1m\sum_a D_{h,\ell,a}
 \le\frac{\ell_T^2 Z_{\ell-1}}{4\lambda_P}. \tag{8}
\]

The backward histories need not be smooth. Their zero prefixes and
\(m^{-1}\sum_a(r_a/\rho)^2=1\) imply

\[
\frac1m\sum_a\|b_{\ell,a}\|^2\le B_\ell^2,
\qquad \frac1m\sum_a D_{b,\ell,a}\le S B_\ell^2. \tag{9}
\]

Projection contraction and the endpoint bound (2) give

\[
\left(\frac1m\sum_a\|b_{\ell,a}^\star\|^2\right)^{1/2}
 \le P B_\ell,\qquad
\left(\frac1m\sum_a\|b_{\ell,a}-b_{\ell,a}^\star\|^2\right)^{1/2}
 \le(P+1)B_\ell.
\]

For the first inequality use the raw backward energy at most
\((\tau-1)B_\ell^2\), and \((\tau-1)/\tau\le1\). Put
\(e_\ell=E_\ell/\rho\). Sample Cauchy–Schwarz in (4), followed by (3)
and (8), now yields

\[
\begin{aligned}
\int_0^t\rho\|e_\ell\|_F^2\,ds
&\le\frac{4(P+1)^2B_\ell^2}{n^2}
                   \frac1m\sum_aD_{h,\ell,a}(t)\\
&\le\frac{2B_\ell^2\ell_T^2}{n^2}Z_{\ell-1}(t). \tag{10}
\end{aligned}
\]

The last step uses \((P+1)^2/[P(P+1)]\le2\). Thus the growing endpoint
factor has cancelled the projection rate; the bound is independent of order.

For the first layer, \(\|h_{1,a}'\|\le s_1v_1X\). For later layers the
chain rule gives

\[
h_{\ell,a}'=\phi_\ell'(z_{\ell,a})\odot
 [(F_\ell/\rho+e_\ell)h_{\ell-1,a}
                   +\widehat W_\ell h_{\ell-1,a}'].
\]

Square this inequality using
\(\|a+b+c\|^2\le3(\|a\|^2+\|b\|^2+\|c\|^2)\), average over samples,
and integrate in \(d\xi=\rho\,dt\). Formula (10) gives the finite recursion

\[
\begin{aligned}
\overline Z_1&=S(s_1v_1X)^2,\\
\overline Z_\ell&=3s_\ell^2\left[
 S v_\ell^2 M_{\ell-1}^2+
 \left(R^2+\frac{2B_\ell^2\ell_T^2 M_{\ell-1}^2}{n^2}\right)
 \overline Z_{\ell-1}\right].
\end{aligned}
\]

Induction proves \(Z_\ell\le\overline Z_\ell\). The induction only uses
the preceding forward layer, so no circular derivative bound is assumed.
The constants may grow with depth but do not grow with \(P\).

Combine (5), (8) and (9), applying sample Cauchy–Schwarz once more. Since
the norm of the full defect is at most the sum of its block norms,

\[
\int_0^t\|E\|\,ds
 \le\frac{\Gamma_A}{\sqrt{\lambda_P}},\qquad
\Gamma_A=\frac{\ell_T}{n}
       \sum_{\ell=2}^L B_\ell\sqrt{S\overline Z_{\ell-1}}. \tag{11}
\]

For two hidden layers this reduces to the simpler argument that first-layer
velocity has a factor \(\rho\), which the activity clock removes. At larger
depth, (10) is the missing step: earlier compressed matrices also move.

### 5.7 Restoring feedback and completing Variant A

Subtract the dense equation from (4). While both physical states remain in
\(\mathcal B\), their distance \(d(t)=\|\widehat\theta_P(t)-\theta(t)\|\)
satisfies

\[
d(t)\le\varepsilon_P+K\int_0^t d(s)\,ds,
\qquad \varepsilon_P=\Gamma_A/\sqrt{\lambda_P}.
\]

To see the comparison explicitly, let
\(u(t)=\varepsilon_P+K\int_0^t d(s)\,ds\). Then \(d\le u\),
\(u'\le Ku\), so differentiation of \(e^{-Kt}u(t)\) gives
\(d(t)\le\varepsilon_P e^{Kt}\). The conclusion also holds when
\(\varepsilon_P=0\), by the same integral inequality or a positive limiting
upper bound. Thus

\[
d(t)\le\frac{\Gamma_Ae^{KT}}{\sqrt{\lambda_P}} \tag{12}
\]

on the stopped interval. Choose \(P_A(T)\) so that this upper bound is at
most \(1/2\). Such an order exists because \(\lambda_P\to\infty\).
The dense trajectory stays distance one from the ball boundary, so the
closure cannot have a first physical exit.

Nor can its raw state cease to exist earlier. For each fixed \(P\), the
moment integral representations bound all moments by finite history masses
and bounded responses. For example, each \(p_k\) is bounded on \([0,1]\),
\(\tau\le\ell_T\), and \(|r_a/\rho|\le\sqrt m\), so each moment is
bounded independently of time on this segment. The outer weights are in
\(\mathcal B\), and \(\tau\ge1\). The full finite state therefore lies
in a compact subset of the raw ODE domain. Its bounded vector field makes
it Cauchy at any finite maximal endpoint; local existence there extends it.
This excludes breakdown and proves Variant A, with
\(C_A(T)=\Gamma_Ae^{KT}\), for sufficiently large order.

### 5.8 Variant B: derive a clock bound before using its sharper rate

Stop Variant B before physical exit from \(\mathcal B\) or before
\(\widehat\rho\) falls to \(\mu/2\), with \(\mu\) from (7). On this set,
the derivative of the response map has a finite bound

\[
\|D\Psi(\theta)\|_{\rm op}\le J.
\]

This is an initial-data constant. To verify its finiteness, write
\(q_r=r/\rho\in\mathbb R^m\). Then

\[
\|q_r\|^2=m,\qquad
Dq_r[v]=\left(I-\frac{q_rq_r^\top}{m}\right)\frac{Dr[v]}\rho.
\]

The matrix in parentheses is an orthogonal projection. The denominator is
at least \(\mu/2\), the residual derivatives are bounded by \(\sqrt m c_f\),
and differentiating the backward recurrence uses only bounded weights and
the first two activation derivatives on compact preactivation intervals.
The first layer only contributes \(\phi_1'\). This proves a finite bound
for \(D\Psi\); the stated local Lipschitz hypotheses give local Lipschitz
continuity of that derivative as required in section 5.2.

First use a coarse energy estimate which requires no small projection error.
The measure has total mass at most \(\ell_T=1+S\). Put

\[
Q=m\sum_{\ell=2}^L(M_{\ell-1}^2+B_\ell^2),\qquad
C_0=\frac{\ell_T Q}{nm}.
\]

The sum of all raw forward and backward history energies, including the
matching prefixes, is at most \(\ell_T Q\). Projection error is at most
raw energy. Applying \(2\sqrt{uv}\le u+v\) to (5) therefore gives

\[
\int_0^t\|E\|\,ds\le C_0,\qquad
\int_0^t\|\dot{\widehat\theta}\|\,ds\le VS+C_0.
\]

Integrating the definition of the clock now proves

\[
\tau_P(t)=1+\int_0^t(\widehat\rho+\|\dot\Psi\|)\,ds
 \le\ell_T+J(VS+C_0)=:\Lambda_T. \tag{13}
\]

This bound is independent of \(P\). It was derived using a coarse absolute
velocity bound; bounded physical weights alone would not bound their total
path length. No clock cap has been assumed or inserted into the algorithm.

### 5.9 Variant B: the quadratic error and continuation

The entire concatenated history \(\overline\Psi(\xi)\) is constant on the
prefix and agrees continuously at its join. On the actual history,

\[
\|\partial_\xi\overline\Psi\|
 =\frac{\|\dot\Psi\|}{\rho+\|\dot\Psi\|}\le1.
\]

Consequently it is absolutely continuous and
\(\int_0^\tau\|\overline\Psi'\|^2\,d\xi\le\tau-1\).
Compare its weighted best polynomial approximation with its ordinary
unweighted Legendre approximation. Since \(d\mu_t\le d\xi\), (1) gives

\[
\sum_{\ell,a}(D_{h,\ell,a}+D_{b,\ell,a})
 \le\frac{\tau^2}{4\lambda_P}
        \int_0^\tau\|\overline\Psi'\|^2\,d\xi
 \le\frac{\tau^2(\tau-1)}{4\lambda_P}. \tag{14}
\]

Legendre polynomials need not be orthogonal for the weighted measure:
their ordinary projection is just a permissible comparison polynomial.
The estimate is for the **joint** history, not one separate unit bound
per neuron or per layer.

Equations (5), (13), (14) and \(2\sqrt{uv}\le u+v\) yield, at every
order on its regular stopped segment,

\[
\begin{aligned}
\sum_{\ell=2}^L\|R_\ell(t)\|_F
&\le\int_0^t\sum_{\ell=2}^L\|E_\ell\|_F\,ds\\
&\le\frac{\tau_P(t)^2(\tau_P(t)-1)}{4nm\lambda_P}
 \le\frac{\Gamma_B}{\lambda_P},\qquad
\Gamma_B=\frac{\Lambda_T^2(\Lambda_T-1)}{4nm}. \tag{15}
\end{aligned}
\]

This is the bound on learned-weight reconstruction along the closure's own
history. It is stronger than a bound on a signed integral alone. Applying
the feedback comparison from section 5.7 gives the actual dense-network bound

\[
\|\widehat\theta_P(t)-\theta(t)\|
 \le\frac{\Gamma_B e^{KT}}{\lambda_P}. \tag{16}
\]

Choose \(P_B(T)\) large enough that

\[
\frac{\Gamma_Be^{KT}}{\lambda_P}\le\frac12,
\qquad
c_f\frac{\Gamma_Be^{KT}}{\lambda_P}\le\frac\mu4
\quad\text{for every }P\ge P_B(T).
\]

The first inequality rules out physical exit. The residual Lipschitz bound
and (7) give \(\widehat\rho\ge3\mu/4>\mu/2\), ruling out residual exit.
If \(c_f=0\), its inequality is automatic; no division by it is needed.

It remains to exclude breakdown of the internal realization. For every
fixed \(P\), the prefix gives

\[
G(t)\succeq\int_0^1p(\xi/\tau(t))p(\xi/\tau(t))^\top\,d\xi.
\]

Each matrix on the right is positive definite: if its quadratic form
vanished, the corresponding polynomial would vanish on an entire interval
and all its coefficients would be zero. Its entries vary continuously with
\(\tau\). On the compact interval \(1\le\tau\le\Lambda_T\), its least
eigenvalue therefore has a positive minimum, denoted \(\gamma_{P,T}\).
This constant may deteriorate with order; the continuation argument needs
positivity only at each fixed order.

Moment entries are bounded by their integral representations, finite mass,
bounded histories and bounded polynomials on \([0,1]\). The physical-state,
clock, residual and Gram bounds thus put the whole state in a compact subset
of its locally Lipschitz ODE domain. The same endpoint continuation argument
as in section 5.7 excludes any finite maximal endpoint before \(T\).
This proves Variant B with \(C_B(T)=\Gamma_Be^{KT}\), the clock bound (13),
and the quadratic integrated-defect bound (15). It completes the theorem.

### 5.10 Why bounded activations give Variant A at every order

Assume additionally \(\|\phi_\ell\|_\infty<\infty\) and
\(\|\phi_\ell'\|_\infty<\infty\). We now construct a common bound for
both dense and old-clock physical states without first requiring large order.
Put \(M_\ell=\sqrt n\|\phi_\ell\|_\infty\),
\(s_\ell=\|\phi_\ell'\|_\infty\), and retain \(X,Y,T\).
For either system the unchanged readout equation gives exactly

\[
\frac d{dt}\|w\|^2
 =-\frac{4n}{m}\sum_a(f_a-y_a)f_a
 =nY^2-\frac{4n}{m}\sum_a(f_a-y_a/2)^2\le nY^2.
\]

Thus set

\[
B_w=\sqrt{\|w_0\|^2+nY^2T},\quad
q=B_w M_L/n+Y,\quad S=Tq,\quad\ell_T=1+S,\quad B_L=B_ws_L.
\]

Proceed downward from link \(L\) to link two, defining

\[
D_\ell=\|W_{\ell,0}\|_F+
             \frac{2\ell_T B_\ell M_{\ell-1}}n,
\qquad B_{\ell-1}=s_{\ell-1}D_\ell B_\ell. \tag{17}
\]

To justify this induction, projection contraction and Cauchy–Schwarz across
history and samples bound the Variant A increment by

\[
\|\widehat W_\ell-W_{\ell,0}\|_F
 \le\frac{2B_\ell M_{\ell-1}}n\sqrt{\tau(\tau-1)}
 \le\frac{2\ell_T B_\ell M_{\ell-1}}n.
\]

Dense integration gives the smaller bound
\(2S B_\ell M_{\ell-1}/n\). The backward recurrence then gives
\(\|\delta_{\ell-1,a}\|\le B_{\ell-1}\). The induction is downward:
\(B_\ell\) uses only the readout and already bounded upper matrices,
while the incoming activation has a global bound. There is no assumption
about a lower, still uncontrolled matrix. Finally,

\[
\|W_1(t)\|_F\le\|W_{1,0}\|_F+2S B_1X.
\]

These bounds are independent of \(P\). At each fixed \(P\), moment
representations and \(1\le\tau\le\ell_T\) put the raw state in a compact
subset of its ODE domain. Continuation proves existence and uniqueness for
every finite \(T\) and every order, hence for all physical times.

For the error bound, choose the common convex product of these block balls
and a Lipschitz constant \(K\) for \(F\) there. Repeat the fully derived
steps (8)–(11), using these global \(M_\ell,s_\ell,B_\ell\). In the
forward derivative recursion replace the bound \(R\) on
\(\widehat W_\ell\) by \(D_\ell\); explicitly the recursion becomes

\[
\overline Z_1=S(s_1v_1X)^2,\qquad
\overline Z_\ell=3s_\ell^2\left[
 S v_\ell^2M_{\ell-1}^2+
 \left(D_\ell^2+\frac{2B_\ell^2\ell_T^2M_{\ell-1}^2}{n^2}\right)
 \overline Z_{\ell-1}\right].
\]

Here \(v_1=2B_1X\), \(v_\ell=2B_\ell M_{\ell-1}/n\).
Equation (11) defines the resulting finite \(\Gamma_A\), and (12) follows
at every order because both trajectories are already in the common region.
No first-exit order threshold is needed. This proves the all-order addition.
For its prediction and loss corollaries below, recompute \(c_f\) by the
formula in section 5.5 using these \(M_\ell,B_\ell\). The original ball's
constant need not control small-order trajectories outside that ball.

### 5.11 Outputs, loss, order selection, and the meaning of global

The physical-state estimates include every learned hidden matrix's discrepancy
from the independently evolved dense network. They also control decoded
predictions on any bounded set of passive inputs. To see this, bound the
output-gradient blocks on the same physical region, now uniformly over that
input set, by a finite constant \(c_{\rm test}\). The chain rule and compact
preactivation bounds used in section 5.5 apply with its input norm bound.
Integration along the segment between the two physical states gives

\[
\sup_{x\in\mathcal X,\,t\le T}
 |\widehat f_P(t,x)-f(t,x)|
 \le c_{\rm test}\sup_{t\le T}\|\widehat\theta_P(t)-\theta(t)\|.
\]

In particular this controls whole-circle RMS discrepancy for any probability
measure on the circle; no passive inputs need to be placed in the training
batch. It does not assert closeness to the task's true labels.
On the training set, \(|\widehat\rho-\rho|\le c_f d\), so
\(|\widehat{\mathcal L}-\mathcal L|\le2q c_f d\) when both residual
RMS values are bounded by \(q\). The same order rates therefore hold for
outputs, training RMS and training loss, on the stated horizons.

For a prescribed physical-state tolerance \(\varepsilon>0\), a sufficient
order rule is

\[
\begin{array}{ll}
\text{Variant A:}&P\ge P_A(T),\quad
 P(P+1)\ge[C_A(T)/\varepsilon]^2,\\
\text{Variant B:}&P\ge P_B(T),\quad
 P(P+1)\ge C_B(T)/\varepsilon.
\end{array}
\]

For the bounded-activation all-order case, take \(P_A(T)=1\). These rules
are mathematical guarantees, not predictions of an economical practical
order: constants and thresholds may be large. The moment coordinates are
polynomial in history position; no temporal Taylor convergence is used.

The exact quantifiers are **every finite horizon, then sufficiently large
order**, with the stated all-order exception. Neither proof bounds
\(C_A(T),C_B(T)\) as \(T\to\infty\); (7) can shrink and the stability
factor can grow. Thus no unconditional
\(\sup_{t\ge0}\|\widehat\theta_P(t)-\theta(t)\|\to0\) is established.
Global existence, finite-horizon tracking, eventual fitting, and uniform
all-time tracking are different conclusions.

One can state the additional all-time obligation precisely. Suppose that for
every \(P\ge P_*\), Variant B has a globally regular solution (positive
residual at each finite time and positive-definite Gram), and its physical
trajectory and the dense trajectory obey the following bounds with constants
independent of \(P\):

\[
\sup_{P\ge P_*,\,t\ge0}\tau_P(t)\le\Lambda_\infty<\infty,
\qquad
\langle u-v,F(u)-F(v)\rangle
 \le\kappa(t)\|u-v\|^2,\qquad
K_\infty:=\int_0^\infty\max(\kappa(t),0)\,dt<\infty.
\]

Here the same function \(\kappa\) applies to every compared pair
\(u=\widehat\theta_P(t),v=\theta(t)\). Differentiating their squared
distance and using (4) gives \(d'\le\kappa_+d+\|E\|\) (at a zero of
\(d\), use the upper
right derivative or replace \(d\) by \(\sqrt{d^2+\epsilon^2}\) and take
the limit). The integrating factor and (15), followed by increasing the
finite horizon, yield the conditional all-time bound

\[
\sup_{t\ge0}d(t)\le
\frac{e^{K_\infty}\Lambda_\infty^2(\Lambda_\infty-1)}
     {4nmP(P+1)}\qquad(P\ge P_*).
\]

These are additional uniform stability and long-time hypotheses; they are
not established for the general networks here. Finiteness separately for
each order would not give an order-independent convergence constant.

Both smooth theorems cover tanh, sigmoid, GELU, SiLU, arctan, softplus, sine
and polynomial activations, including mixtures by layer. Literal ReLU and
SELU are excluded across their derivative jumps. A continuous clock cannot
make a discontinuous backward response Lipschitz, and an almost-everywhere
classical derivative misses its jumps. Away from all kinks, the same proof
works in a compact neighborhood with fixed smooth branches. The general
selected-flow existence, uniqueness and stability obligations at switches
remain separate; numerical support for these activations does not prove them.

The guarantees concern exact continuous-time equations at fixed finite width,
data and depth. They give no width-uniform limit, Euler-step certificate,
monotonic actual error in \(P\), or total-memory advantage. Variant B changes
the prefix as well as the clock, so its sharper proved rate does not isolate
an empirical clock advantage with every other modeling choice held fixed.

The argument above contains the full proof and needed polynomial estimate.
Original derivations and checks remain available in
[ORACLE_FINITE_HORIZON_BOUND.md](ORACLE_FINITE_HORIZON_BOUND.md),
[ORACLE_FINITE_HORIZON_CHECK.md](ORACLE_FINITE_HORIZON_CHECK.md),
[RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md](RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md),
and [DEEP_ACTIVATION_ERROR_THEOREM.md](DEEP_ACTIVATION_ERROR_THEOREM.md), with
its [old-clock](DEEP_OLD_CLOCK_ROUTE.md), [new-clock](DEEP_NEW_CLOCK_ROUTE.md)
and [activation-scope](DEEP_ACTIVATION_SCOPE.md) checks. These are study results
with internal checking, not promoted book theorems.
## 6. Empirical evidence

Unless stated otherwise, the following are **ordinary activity-clock** results.
The main metric is RMS discrepancy from the dense predictor on passive inputs,
not error against unseen labels. Most circle/MNIST campaigns compare each
model at its own first training-MSE \(0.001\) crossing. They therefore assess
fitted-function agreement, rather than the theorem's same-time supremum norm.
Circle scores use 8,192 angles with numerical/grid checks; they are not exact
continuum integrals. These are selected finite-instance experiments, generally
one initialization, not a statistical or observed asymptotic-rate theorem.

### Two hidden tanh layers: learning difficult circle configurations

At width 2,048, all five selected configurations improve over the tested
orders \(P=1,3,7\). These rows use the original common dense references so
that historical dictionary comparisons remain meaningful:

| Training configuration | P1 RMS | P3 RMS | P7 RMS |
|---|---:|---:|---:|
| Two outliers, alternating labels | 0.236313 | 0.0729531 | 0.00466307 |
| Quadrant, alternating labels | 0.341407 | 0.0456972 | 0.00164765 |
| Quadrant, paired labels | 0.0192803 | 0.00281547 | about 0.00012 |
| Quadrant, center/edges | 0.0456043 | 0.00487212 | 0.00130221 |
| Equal mixed odd labels | 0.0123936 | 0.000520130 | about 0.00001 |

The first four have eight samples; the last uses the exact four-representative
antipodal quotient. Eight-sample history-vector counts are 16/48/112 and learned
rank bounds 8/24/56. Fresh dense-reference refinements preserve the improvement
trend, but the smallest paired-label and mixed-odd errors are resolved only at
roughly \(10^{-4}\) and \(10^{-5}\) scales. Initial rational-lift runs that
failed activation-drift checks were retained and followed by validated
refinements. See [MOMENT_RESULTS.md](MOMENT_RESULTS.md) and
[MOMENT_INDEPENDENT_CHECK.md](MOMENT_INDEPENDENT_CHECK.md).

On the hard outlier task, the common-reference comparison gives:

| Representation | Stored response/dictionary vectors | Circle RMS |
|---|---:|---:|
| Frozen derivative p3 | 18 | 1.10012 |
| Trainable derivative p3 | 18 | 0.89643 |
| Frozen derivative p7 | 72 | 0.75642 |
| Response memory P3 | 48 | 0.07295 |
| Response memory P7 | 112 | 0.00466 |

The history model retains dense \(W_0\); those earlier dictionary models do
not. This demonstrates predictor fidelity, not matched-total-storage
superiority. [Historical input identities](HARD_BENCHMARK_INPUTS.md) and the
[trainable comparison](../adaptive_response_compression_20260922/TRAINABLE_P3_RESULTS.md)
fix the reference and stopping convention.

A more targeted control retains the same \(W_0\) and trains
\(W_2=W_0+AB\) at matched learned rank. History moments win **all 29 valid
comparisons** across five tasks, three orders and two factor seeds; one factor
cell did not fit within its cap. On hard outliers at rank 56, moments give
0.004663 versus 0.516210 and 0.251026 for the two factor seeds. This isolates
an advantage over that particular factor-gradient flow, not every low-rank
algorithm. [Factor results](FACTOR_CONTROL_RESULTS.md),
[independent check](FACTOR_CONTROL_CHECK.md).

### More layers, images and other activations

| Setting | Observed dense-prediction agreement | Qualification |
|---|---|---|
| Three hidden tanh layers, width 4,096, five circle tasks | P2/P3 beat P1 throughout; P3 RMS 0.000282–0.058491 | P2 beats P3 on both alternating tasks, with resolved gaps. Substantial hidden-feature movement is measured. |
| MNIST 3/8, 100 training images, width 4,096 | P1/P2/P3 RMS 0.00324756 / 0.00108443 / 0.00119922 on 1,984 held-out images | All declared gates pass; P3 slightly worsens over P2. Learned rank bounds are 100/200/300. |
| MNIST 3/8, 1,000 training images, width 1,024 | Measured RMS 0.0187719 / 0.00191819 / 0.00123214 | P2/P3 fail strict numerical-resolution gates; their ranking is unresolved. History state is larger than dense here. |
| GELU/sigmoid circle, three hidden layers, width 4,096 | GELU hard-outlier P3 RMS 0.02485 | GELU quadrant and sigmoid outlier P3 errors are about 0.260 and 0.241. Only nine fitted comparisons were available; capped ReLU/SELU runs establish no fitted-fidelity verdict. |
| ReLU/GELU/SELU circle transfer, three hidden layers, width 2,048 | All 18 task/activation/order combinations fit at the two initial resolutions | Only 14/18 closure step-halving screens pass; fitted errors and order trends remain task dependent. Stop target is MSE \(10^{-8}\). |
| Smooth sphere targets \(\sqrt{15}xy\), \(\sqrt{105}xyz\); four hidden layers, width 2,048, 32/64 samples | All 48 models fit to training RMS at most 0.01; all 36 closure errors are below 0.032, all 12 P3 errors below 0.01 | Practical float32 Euler comparison at step 1/128 and individual stops, without a refinement certificate for continuous GF. |

Sources: [deep tanh](DEEP_CIRCLE_RESULTS.md),
[MNIST100](MNIST100_RESULTS.md), [MNIST1000](MNIST_RESULTS.md),
[activation final checks](ACTIVATION_CIRCLE_FINAL_METRICS_CHECK.md),
[activation transfer](CLOSURE_TRANSFER_2048_RESULTS.md), and
[sphere table](../../data/generated/neural_response_memory_20260922/compact_sphere01/table.md)
with [full sphere metrics](../../data/generated/neural_response_memory_20260922/compact_sphere01/sphere_rms.csv).
The sphere campaign uses one seed, no normalization, and full-sphere passive
queries. Dense target error can remain substantial even when closure error is
small; agreement with dense and useful generalization are different metrics.

The practical depth-four circle continuation also retained positive and capped
results: its [initial two-task batch](../../data/generated/neural_response_memory_20260922/compact_depth4_01/circle_rms.csv)
fitted all 24 models to RMS at most 0.01, with P3 discrepancies 0.02875–0.26076.
The [four additional tasks](../../data/generated/neural_response_memory_20260922/compact_depth4_extra01/circle_rms.csv)
had 36/48 target-reaching fits; all 48 ended below 0.04 RMS, but 12 were capped.
Those capped comparisons do not establish fitted order deterioration.

### Stress tests and practical limits

Higher order does not always improve fitted predictions, despite monotonic
projection error for one fixed history. Changing order changes the full
feedback trajectory. Training loss alone also does not control the function
away from training inputs.

Historical depth-ten high-frequency experiments with after-activation
LayerNorm fitted all four GELU task groups, but P3 whole-space discrepancies
were about 0.120 on the full circle, 0.140 on a restricted arc, 0.00712 on the
full sphere and 0.0969 on a sphere cap. A fully fitted ReLU arc case had P3
whole-circle discrepancy about 0.777, dominated by the unlabeled complement.
These are different normalized architectures, not the current defaults, and
are not automatically covered by the pointwise-activation theorem.
[Fitted stress table](../../data/generated/neural_response_memory_20260922/compact_stress_fitted01/step128/table.md),
[activation stress](COMPACT_STRESS_ACTIVATIONS_RESULTS.md).

The completed **common unnormalized SELU/depth-ten/width-2,048** check used
unit-moment hidden initialization and stored readout standard deviation one.
At the selected common step 1/1024 only 6/16 models fitted; three closures were
nonfinite. Only the full-sphere quartet supports a fitted four-model comparison,
with P1/P2/P3 RMS 0.09103/0.09444/0.08967. A coarse-step failure disappeared
on refinement, so nonfinite Euler runs are not by themselves evidence of
exact-flow blow-up. [Completed unnormalized report](CANONICAL_UNNORMALIZED_RESULTS.md).
New validation in progress is recorded separately in section 10.

## 7. What is compressed, and what still costs memory and work?

For \(L\) hidden layers, both methods retain \(2(L-1)nmP\) moving history
scalars, in addition to \(nd+n\) outer weights and a clock. Variant B adds
one symmetric Gram matrix with \(P(P+1)/2\) independent entries, and fixed
prefix vectors; the implementation stores the full \(P\times P\) Gram array.
The learned rank per link is at most \(mP\) in Variant A and \(m(P+1)\) in
Variant B, capped by \(n\).

No learned dense matrix needs to be formed. A learned matrix-vector action
costs \(O(nmP)\) through population contractions; its transpose uses the same
factors. Weighted reconstruction additionally needs a shared \(O(P^3)\) Gram
factorization and factor solves of order \(O((L-1)nmP^2)\) per RHS evaluation.
Response monitoring adds directional forward/backward work.

The initialized matrices still occupy \((L-1)n^2\) entries and require their
actual matrix-vector products. History cost grows with the dataset size, even
at fixed input dimension. For example, MNIST100 compresses the unrestricted
learned correction's 128 MiB to 6.25–18.75 MiB of history, but retains the
128 MiB initialized matrix; minimal total state exceeds a dense implementation
storing only its current weights. Measured GPU workspace savings do not imply
total-state savings, and the measured adaptive integrations were slower than
dense in that panel. [Storage and timing](MNIST100_RESULTS.md).

The current achievement is controlled compression of **learned moving state**.
Efficient compression of the initialized operator, sample-independent history
state, width-uniform accuracy and an economical scalar population description
remain separate objectives.

## 8. Further compression to scalar aggregates: a separate branch

Differentiating population averages and initialized-operator contractions gives
an exact hierarchy. A finite aggregate cutoff is an additional approximation,
distinct from history order. The original unsaturated deletion has local
convergence results; a modified clipped hierarchy has an internally derived
convergence theorem on any prescribed finite interval, at fixed width and
fixed parent order. Choosing history order first and scalar cutoff second
therefore gives an existence result for finite scalar output approximation,
with potentially prohibitive cutoffs and no width-uniform efficiency claim.
[Aggregate construction](POPULATION_TO_AGGREGATES.md),
[scalar bound](SCALAR_COMPRESSION_BOUND_ASSESSMENT.md).

Fourier-integrated aggregates and terminal polynomial readouts offer principled
whole-circle evaluation without evolving a dense query mesh. However, the
tested small unsaturated scalar truncation had circle RMS 0.21098 versus
0.01822 for its parent history closure. Its returned Fourier predictor had
training RMS 0.16925 despite internal training RMS 0.03162.
A direct passive-point test also failed
(absolute error 0.43672), ruling out Fourier extraction as the sole explanation.
[Fourier route](SCALAR_CIRCLE_FUNCTION_READOUT.md),
[Fourier experiment](SCALAR_FOURIER_IMPLEMENTATION_REPORT.md),
[passive-point experiment](SCALAR_POINT_REPORT.md).

A different fixed-response-basis scalar ODE achieved decoded circle RMS
0.01699 at width 16/rank 12, but failed its original primary gate at width 32.
It confines learned increments to fixed initialized spaces, and its internal
outputs need not equal its decoded network's outputs. It has no demonstrated
total-memory advantage. This is a return to a dictionary restriction, not a
refutation of all scalar closures. Its harder-task campaign was cancelled;
the existing implementation was consolidated without new scalar training.
[Variants](SCALAR_VARIANTS_REPORT.md), [fixed-span analysis](SCALAR_DICTIONARY_COMPARISON.md),
[scalar implementation](SCALAR_STANDALONE.md).

### Direct scalar comparison without Fourier (2026-09-26)

A separate implementation now tests the clipped contraction hierarchy against
its same-order population parent using direct training outputs, three passive
outputs and training Gram matrices at both hidden layers. There are no Fourier
coordinates or frozen response spaces. Runtime contains only scalars and
compiled coefficient/index tables; initialized-matrix contractions are
evaluated once for initialization and certified clipping bounds.

The fixed panel covers three circle tasks, widths 16/64, two seeds, P=1
throughout and a P=2 two-input extension. Of 40 primary scalar solves, 24
completed and all 24 exceeded the declared accuracy-failure threshold; 16
ended at numerical gates or solve limits. On the closer two-input task, K=7
achieved median training RMS \(1.08\,10^{-7}\) but median final passive
discrepancy 0.357 against the parent. A refined two-input example returned
a negative diagonal entry in its activation Gram matrix. Tolerance refinement
and an unclipped control confirmed that example's substantial discrepancy.

These results establish a practical failure of the tested low cutoffs,
independently of Fourier extraction. They do not refute the fixed-width
large-cutoff convergence argument. The K=7 two-input system already has
2672 evolving scalars and about 9.36 MB of runtime arrays, so this panel
demonstrates no useful memory saving at accurate prediction.
[Construction, full results and reproduction](SCALAR_DIRECT_RESULTS.md),
[separate scalar engine](scalar_direct.py).

### Further compression from the working population closure

A new assessment keeps the successful order-\(P\) response-memory population
closure as the parent model and separates three additional approximation
axes: aggregate cutoff, initialized-operator state and input/sample
representation. Its main conclusions are:

- Scalar output or loss does not imply scalar state sufficiency. Even
  fixed-kernel loss dynamics can require \(m\) independent spectral weights
  for \(m\) generic samples. The clipped forest hierarchy remains a principled
  finite-horizon existence result, but no economical scalar cutoff is known.
- Redrawing \(W_0\) during training is invalid for this target: it removes
  temporal reuse and the mixed correlations enforcing one shared forward and
  transpose operator. Exact lazy Gaussian conditioning gives a moving,
  query-adaptive action state, but its rank can grow to the width. A fixed-size
  approximation needs a causal effective-rank theorem.
- No exact sample-count-independent state can work uniformly over arbitrary
  labels in a generic fixed-kernel family. For structured circle tasks, the
  strongest next route is Fourier--Galerkin
  compression of the **sample-indexed fields of the population closure**.
  Its Fourier coefficients remain neuron vectors and evolve during learning,
  so this does not freeze learned directions. Moreover, input projection
  commutes with \(W_0\), reducing \(m\) dense actions to the retained input-mode
  count when spatial regularity makes that count small. For a uniform circle
  law, the learned correction becomes a sum over matched Fourier modes and has
  rank at most \(P(2Q+1)\) per link at mode cutoff \(Q\).

The note proves the aggregate projectability criterion, a regular
sample-count lower bound for exact loss prediction, the Gaussian reuse
covariance witnesses and a finite-horizon data-coreset comparison inequality.
It states the precise regularity and stability obligations for the proposed
input-mode theorem and recommends validating sample-axis Fourier tails before
attempting another full scalar reduction.
[Further population compression assessment](FURTHER_POPULATION_COMPRESSION.md).

#### Width-only clarification

In the fixed-kernel formulas above, \(m\) is sample count and \(n\) is neuron
width. The \(m\)-dimensional loss obstruction does not constrain a closure
whose state may depend on all \(m\) samples but not on \(n\).

The relevant goal is **approximate**, rather than exact, removal of the neuron
population. There is a positive construction at every fixed realized width:
differentiate only the normalized mixed contractions reachable from the
requested outputs, retain them through aggregate grade \(K\), delete terms
crossing that grade, and clip every retained contraction at a certified parent
bound. This gives a globally existing autonomous scalar ODE. For fixed
\(n,m,P,T\), its training outputs and loss converge uniformly on \([0,T]\) to
the response-memory population closure as \(K\to\infty\). The construction
keeps the initialized \(W_0/W_0^\top\) reuse through decorated contraction
edges and performs no neuron-vector or matrix action after initialization.

Mixed angle-neuron contractions extend the same theorem to direct
whole-circle energy and finitely many Fourier coefficients. At fixed width,
choosing the Fourier cutoff and then the aggregate cutoff recovers the
population closure's fitted function in \(L^2\), uniformly on a prescribed
finite training interval, without a test mesh. The response-memory error and
scalar error then combine by the triangle inequality to compare with the
dense network.

This theorem does not yet give one cutoff uniform in width: its parent
envelope and sufficient \(K\) may depend on \(n\). A true width-removal result
requires width-uniform weighted forest and feedback bounds. Conversely, no
unrestricted theorem for the whole fitted function is possible: a continuous
\(K\)-scalar encoder cannot uniformly reconstruct the unit sphere of an
\(N\)-dimensional realizable function subspace when \(K<N\). The fixed smooth
Gaussian circle task may still be compressible because it is a much smaller,
regular family.
[Approximate scalar population compression](APPROXIMATE_SCALAR_POPULATION_COMPRESSION.md).

The focused width analysis also gives three exact benchmarks. Frozen NTK dynamics have
an exact \(n\)-free \(m\)-output kernel ODE. A two-factor linear network has an
exact feature-learning closure through its end-to-end map and two endpoint
Gram matrices, all independent of hidden width. With three generic linear
factors, however, the exact state already contains a spectral measure with up
to \(n\) atoms; at infinite width this becomes an infinite-dimensional
spectral field. Thus width does not generically collapse to finitely many
scalars even for linear deep learning.

There is also a direct nonlinear exact-closure no-go result with one sample. For
\(f_n=n^{-1}\sum_i\tanh w_i\), canonical feature learning can be
reparametrized so that each \(z_i=\tanh w_i\) obeys
\(dz_i/dq=(1-z_i^2)^2\). The first \(n\) output derivatives have a Jacobian of
rank \(n\) at suitable neuron states. Any exact smooth autonomous encoder on
an open state family must therefore have at least \(n\) coordinates. This
rules out universal exact width-independent scalarization, not finite-accuracy
compression or a special restricted Gaussian trajectory.

For the nonlinear response-memory closure, proving or falsifying the
width-uniform weighted forest estimates, with \(m\) and \(P\) fixed, is the
main theoretical target. A moving representative population coupled to a
shared initialized-operator response law is the corresponding practical
alternative.
[Width-only population compression](WIDTH_ONLY_POPULATION_COMPRESSION.md).

## 9. Current implementation and reproducibility

Use [compact_flow.py](compact_flow.py), the single active Python suite for
dense dynamics, both memory variants, the two historical frozen dictionaries,
random controls, trainable dictionaries and direct low-rank updates.
[CANONICAL_FLOW.md](CANONICAL_FLOW.md) documents exact method scope and the
[JSON catalog](experiment_configs.json). It is one suite file, not an isolated
standalone package: established dictionary compiler modules and data files
remain dependencies. [scalar_ode.py](scalar_ode.py) is a separate scalar model.

The suite supports arbitrary positive hidden depth, supplied input dimension,
and built-in tanh, sigmoid, GELU, SiLU, ReLU and SELU, with per-layer choices.
The historical dictionaries retain their two-hidden-layer tanh/2D scope.
Inputs are supplied already scaled as intended; the engine does not silently
apply another \(1/\sqrt d\). Current configs enable no normalization.

`kind="closure"` implements Variant A. `kind="weighted_closure"` with
`clock="response"` implements Variant B, including the shared deep monitor.
The optional weighted `clock="residual"` keeps the **matching prefix** while
using \(g=\rho\); it is not Variant A. At P1 the physical weighted closure is
independent of its clock choice, with that prefix held fixed.
Ongoing validation also introduces `clock="response_rms"`, which uses
\(\rho+\sqrt{\operatorname{mean}(\dot\Psi^2)}\). This is an experimental
RMS-scaled monitor, distinct from the unscaled monitor and explicit constants
displayed above.

The default trainer uses simultaneous fixed Euler steps for ordinary memory,
dense and factor methods; ongoing validation also introduces optional blockwise
step control. Run configurations specify which numerical procedure was used.
Weighted memory combines explicit network/source velocities with exact
polynomial coordinate transport and positive Gram insertion. This is a
first-order discretization; exact-arithmetic Gram positivity is not a
conditioning or finite-precision guarantee. Gram and clock use float64, moments
use the selected network dtype. No extra numerical convergence theorem is
claimed by implementing the continuous equations, and nonsmooth built-ins
retain their separate theoretical limitations.

The saved single-file consolidation checks record 2,136 existing and 610 added assertions,
including 36 weighted cases, independent gradients, clock/operator derivatives,
stationary zero residual, P1 clock independence and first-order consistency.
MNIST's 1,000 training/1,984 test rows reproduce bitwise; 22 width-2,048
CUDA/eager checks have identical tested updates. These are implementation
checks for their recorded source snapshot (`b44b16e6…`), not empirical proof of
a weighted-clock accuracy or speed advantage. Subsequent adaptive-step,
RMS-clock and initialization-calibration changes require their own validation;
the saved check counts do not certify those new paths.
[Check record](../../data/generated/neural_response_memory_20260922/single_file01/final_check.json).

From the repository root, the CPU checks are:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py --check
```

To prepare a configured dataset without launching training:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py \
  --config studies/neural_response_memory_20260922/experiment_configs.json \
  --experiment additional_methods --prepare-only \
  --out data/generated/neural_response_memory_20260922/FRESH_PREPARATION
```

Removing `--prepare-only` launches the selected experiment. Use a fresh output
directory. Runs retain resolved configuration, initialization/data/source
provenance, numerical settings, stop reasons, predictions and RMS tables;
`--summarize RUN/EXPERIMENT` recomputes saved metrics. `fitted_pair` requires
both the model and dense reference to reach the declared training target.
The guide distinguishes training RMS, dense-discrepancy RMS and target RMS.

Historical adaptive-Heun campaigns and their detailed diagnostics keep their
original protocols; the consolidated suite does not redefine those
experiments. [legacy_experiments.zip](legacy_experiments.zip) preserves 65
retired scripts and earlier canonical files with checksums. Existing detailed
reports and generated evidence remain the source for their original results.

## 10. Current work and unresolved questions

<!-- CURRENT_VALIDATION_STATUS: preserved from the concurrently maintained README. -->
### Fast-fitting validation completed (2026-09-26)

The practical benchmark contains **266 fits at width 2048: 254 reached training
RMS <=0.05, and 258 reached <=0.065**. Median total time was **1.73 seconds**,
90th percentile **17.74 seconds**, and maximum **111.25 seconds**. Times include
model setup and final prediction. All main runs were finite. This is measured
coverage of the configurations below, not every activation/depth/task combination.

| Tested group | Fits | RMS <=0.05 | RMS <=0.065 | Maximum total seconds |
|---|---:|---:|---:|---:|
| Six original circle tasks; ReLU/tanh depth 4, GELU/SiLU depth 3, SELU/sigmoid depth 2; dense and P1/P2/P3 | 144 | 144 | 144 | 18.29 |
| Two hard circle tasks; ReLU depth 10, GELU depth 15, SELU depth 20; dense and P1/P2/P3 | 24 | 24 | 24 | 6.66 |
| Smooth sphere xy/xyz, 16/64 samples, GELU depth 4; dense, P1/P2/P3, low-rank and trainable dictionary | 24 | 24 | 24 | 0.95 |
| Two hard circle tasks, tanh depth 2; historical/random dictionaries, trainable dictionary, low-rank and weighted-history baselines | 20 | 20 | 20 | 13.13 |
| Four 64-sample high-frequency circle/sphere tasks, full/partial support; ReLU 10, GELU 15, SELU 20; dense and P1/P2/P3 | 48 | 42 | 45 | 111.25 |
| Weighted P1/P2/P3 on the 64-sample high-frequency arc; ReLU/SELU depth 10 | 6 | 0 | 1 | 110.64 |

All runs use no normalization, float32, TF32 disabled, seed 20260920 and one
worker per GPU on two RTX 3090s. The `fast_*` entries in
[experiment_configs.json](experiment_configs.json) contain the exact settings,
including 1,024 whole-circle/sphere queries. The practical shared maximum step
is 1/64, with a cheap blockwise loss guard, target RMS 0.05 and 110-second
training cap. Activation gain uses the Gaussian second-moment rule, except
sigmoid gain 8; stored readout std is 1. Historical dictionary baselines explicitly
retain their original initialization. Optional random-core calibration uses
training inputs only, once at initialization; it adds no normalization layer.
Weighted P2/P3 use the explicitly configured RMS response clock; this differs
from the original unscaled response clock. Details and reproduction commands
are in [CANONICAL_FLOW.md](CANONICAL_FLOW.md).

The remaining exceptions are all on the 64-sample, high-frequency 90-degree
circle arc. Their training RMS values are:

| Model | Activation / hidden depth | P1 | P2 | P3 |
|---|---|---:|---:|---:|
| Ordinary closure | SELU / 20 | 0.10152 | 0.09940 | 0.14021 |
| Weighted closure | ReLU / 10 | 0.06339 | 0.10418 | 0.10726 |
| Weighted closure | SELU / 10 | 0.07411 | 0.17800 | 0.13828 |

ReLU depth 10 on that arc also ended slightly above the strict target: dense
0.05035, ordinary P2 0.05585 and P3 0.05176. These and weighted ReLU P1 count
as the four relaxed passes, not strict successes. The other eight failures
remain recorded at the cap; this experiment does not establish a positive
loss floor or certify continuous-gradient-flow accuracy. Successful fitting
also does not imply small closure-versus-dense query error or target generalization.

The main evidence is
[benchmark.csv](../../data/generated/neural_response_memory_20260922/fast_fit01/benchmark.csv)
and [benchmark_summary.json](../../data/generated/neural_response_memory_20260922/fast_fit01/benchmark_summary.json).
It includes every run from `circle_final/`, `coverage_gpu0/`, `final_gpu0/` and
`final_gpu1/`, with no best-run selection. Saved predictions/data hashes were
verified and all metrics recomputed. Source versions are recorded per run:
`coverage_gpu0` used `ce58b53`, `final_gpu0/1` used `24fb9ae`, and `circle_final`
used the final source hash recorded in the summary. Subsequent default/test
changes leave those explicit experiment settings unchanged. Earlier pilot and
failed configuration attempts remain separately under `fast_fit01/` and are
excluded from the 266-run aggregate.

Final implementation verification passed **3,070 CPU assertions**, 72 weighted
history/clock cases, guarded-step checks on CPU/GPU, 22 width-2048 CUDA-graph
versus eager cases, and the original dictionary regression checks. MNIST's
1,000 training and 1,984 test rows reproduced bitwise; MNIST training is not part
of this toy fitting benchmark. All 35 catalog configurations passed data
preparation. The full check took 15.93 seconds; see
[final_gpu_check02.json](../../data/generated/neural_response_memory_20260922/fast_fit01/final_gpu_check02.json).
Caching existing response fields and solving only the small Gram system gave
1.55x faster weighted-clock training iterations in a fixed 128-step comparison,
with query prediction RMS difference exactly zero; see
[optimization_check.json](../../data/generated/neural_response_memory_20260922/fast_fit01/optimization_check.json).

The suite remains one active Python file. This bounded validation is complete;
no further tuning or training is queued. These internally checked results have
not been promoted to established theory or code.

#### Response-memory query-accuracy sweep completed (2026-09-26)

**P3 generally matches the dense predictor well; P1 has substantial exceptions.
The simplest useful numerical change is maximum step 1/256 instead of 1/64
for deeper accuracy comparisons, applied to both dense and closure.** No network,
closure equations, normalization or fitting implementation was changed.

The baseline sweep independently rescored the 58 prior dense/P1/P2/P3 groups
and added 24 sphere groups: all six activations at depths 2 and 6, 32 samples,
smooth xy and oscillatory cap targets. Together these cover 82 configurations,
including the previous six original circle tasks, smooth and high-frequency
circle/sphere tasks, partial-support tasks, and representative depths
2/3/4/6/10/15/20. This is not the full Cartesian product. Width is 2048,
float32 with TF32 off, no normalization, same initialized dense matrices for
each matched comparison, and seed 20260920 unless explicitly replicated.

The metric is RMS of closure minus dense predictions over the saved 1,024-point
full-circle or equal-area full-sphere grid. Both models must have training RMS
<=0.065. Eighty of the 82 groups satisfy that gate for all three orders:

| Ordinary memory order | Median query RMS | 90th percentile | Maximum | Query RMS <=0.05 | Query RMS <=0.1 |
|---|---:|---:|---:|---:|---:|
| P1 | 0.04063 | 0.22926 | 3.52703 | 43/80 | 55/80 |
| P2 | 0.02119 | 0.19127 | 0.47427 | 54/80 | 64/80 |
| P3 | 0.00993 | 0.12194 | 0.38572 | 60/80 | 69/80 |

On the 23 fitted new sphere groups, P3 median/max are 0.00325/0.08267;
all 23 have query RMS <=0.1. P2 passes that query threshold in 22/23 and P1
in 16/23. The excluded groups are the prior SELU depth-20 high-frequency arc
(closure underfit) and new sigmoid depth-2 sphere cap (dense RMS 0.08946 at
15 seconds). The latter's P3 training RMS is 0.05258; the dense fit is the
reason its query comparison is excluded. Exclusions remain in the full table.

**Bounded configuration checks.** On six preselected troublesome, quickly fitted
circle groups, compare one change at a time: step /4 or training target /10.
The original target is 0.05 and maximum step 1/64. Lowering the target to 0.005
did not improve median P3 query error (0.10775 -> 0.11206). Quartering the step
did (0.10775 -> 0.05475), with all groups remaining fitted. This activated only
the preregistered branch: six second-seed comparisons (20260921, each with its
own baseline), plus six additional groups selected by largest remaining P3
error among prior dense/P3 fits taking <=8 seconds.

| Deep pilot / task | P3 at 1/64, seed 1 | P3 at 1/256, seed 1 | P3 at 1/64, seed 2 | P3 at 1/256, seed 2 |
|---|---:|---:|---:|---:|
| ReLU depth 10 / quadrant | 0.05664 | 0.02042 | 0.05356 | 0.02878 |
| GELU depth 15 / outliers | 0.14698 | 0.05138 | 0.04869 | 0.03100 |
| SELU depth 20 / quadrant | 0.18458 | 0.05812 | 0.11731 | 0.09645 |

The six additional groups all improved P3, median 0.09200 -> 0.03011. They
include SELU20/outliers (0.22256 -> 0.02064), GELU15/high-frequency arc
(0.10494 -> 0.04653), and GELU15/oscillatory sphere (0.07905 -> 0.02676).
The last added shallow SELU center/edges case capped at P1/P2/P3 training RMS
0.05208/0.05465/0.05682; it passes the stated 0.065 gate, not the strict target.
Shallow effects are mixed: on seed 2, SiLU3 P3 worsened 0.13262 -> 0.13828 and
SELU2 worsened 0.07827 -> 0.09632. Across all six second-seed cases the P3 median
changed only 0.09779 -> 0.09638, whereas all three deep cases improved.
Thus the broad first-seed 49% median reduction is not a universal replicated
claim. Deep-model improvement is the supported practical recommendation.

Small steps do not rescue shallow GELU/SiLU P1 on the quadrant: their first-seed
query errors remain about 3.00/3.56. Higher memory order is the stronger remedy
there. Good training fit alone does not establish dense-predictor agreement.
The dense predictor also changes with step size, so comparisons use a matched
new dense run; its shift is recorded separately. The experiment supports an
endpoint numerical improvement, not a continuous-GF accuracy certificate or
monotone convergence in P. Whole-space matching and target generalization are
separate metrics. Parameter selection is exploratory; no test predictions
or target query labels enter model training.

All 216 new fits completed: 211 reached training RMS <=0.05 and 215 <=0.065.
Median total time was 3.37 seconds, 90th percentile 8.44, maximum 15.084 seconds,
including initialization and final queries. Summed model runtime was 935.52
seconds across two GPUs, below the predeclared 24 GPU-minute limit. Each fit
had a 15-second training cap; capped cases were retained and not retried.
The 216-fit branch limit is exhausted and no further tuning is queued.

Evidence under `data/generated/neural_response_memory_20260922/response_accuracy01/`:

- [sweep_table.csv](../../data/generated/neural_response_memory_20260922/response_accuracy01/sweep_table.csv): all 82 configurations with dense and P1/P2/P3 training/query RMS and fit flags.
- [sweep_summary.json](../../data/generated/neural_response_memory_20260922/response_accuracy01/sweep_summary.json): separate existing/new/combined statistics; the two ineligible groups are not silently dropped from the source table.
- [pilot_comparison.csv](../../data/generated/neural_response_memory_20260922/response_accuracy01/pilot_comparison.csv): both pilot changes, every order and dense-reference movement.
- [confirmation_comparison.csv](../../data/generated/neural_response_memory_20260922/response_accuracy01/confirmation_comparison.csv): second-seed and additional-task pairs, including regressions and capped fits.
- [new_runs.csv](../../data/generated/neural_response_memory_20260922/response_accuracy01/new_runs.csv) and [final_summary.json](../../data/generated/neural_response_memory_20260922/response_accuracy01/final_summary.json): all 216 new runs, timings, stop reasons and aggregate checks.

Configs are the 42 `accuracy_*` entries in [experiment_configs.json](experiment_configs.json).
The source remains unchanged at SHA-256
`97470496d39813ccb9482ef6cb475d167367526e5654541f0f2a001920f34145`.
All prediction/data hashes were verified, all new metrics recomputed with the
canonical summarizer, and every second-seed/additional-task comparison checked
for identical model settings and bitwise-identical data arrays across step sizes.
The runner records exact commands, source hashes, device and resolved settings.
Example reproduction into a fresh output directory:

```sh
python -B studies/neural_response_memory_20260922/compact_flow.py \
  --config studies/neural_response_memory_20260922/experiment_configs.json \
  --experiment accuracy_sphere_relu2 accuracy_sphere_relu6 \
  --device cuda:0 --out data/generated/neural_response_memory_20260922/response_accuracy_repro
```

Use `--summarize OUTPUT` to independently recompute each worker's rows. The
baseline is exactly the 174 ordinary-closure rows from the prior fixed four
`fast_fit01` groups; the new sphere rows are the 72 ordinary-closure rows in
`sphere_gpu0/1`. Group their concatenation by P after applying the documented
0.065 fit gate to reproduce the 80-pair summary. Pilot and confirmation groups
are separate and never substituted for the baseline sweep. All findings are
internally checked empirical evidence; no established-code/theory promotion.

#### Higher-order check of the three P3 failures: results (2026-09-26)

**P5 substantially improved the fitted SELU20/outlier comparison and only
slightly improved the fitted SELU20/sphere-cap comparison. Fitted higher-order
comparisons remain unavailable for ReLU10/arc P5/P7 and SELU20/cap P7 within
the quick-run budget.** Do not treat the underfitted rows as evidence that
higher memory order improves or worsens dense-predictor accuracy.

At the original maximum step 1/64, with a freshly trained matching dense
reference, the whole-space query RMS values are:

| Case | P3 test RMS | P5 test RMS | P7 test RMS |
|---|---:|---:|---:|
| ReLU depth 10, high-frequency circle arc | 0.37670 | 0.31174 (underfit) | 0.65160 (underfit) |
| SELU depth 20, high-frequency sphere cap | 0.28132 | 0.26235 | 0.28227 (underfit) |
| SELU depth 20, circle outliers | 0.22256 | 0.06208 | 0.13643 |

The corresponding training RMS values make eligibility explicit:

| Case | Dense | P3 | P5 | P7 |
|---|---:|---:|---:|---:|
| ReLU10 arc | 0.05000 | 0.04997 | 0.07981 | 0.08533 |
| SELU20 cap | 0.04992 | 0.04999 | 0.04976 | 0.07295 |
| SELU20 outliers | 0.04631 | 0.04393 | 0.04840 | 0.04771 |

Unrounded dense ReLU RMS is 0.0499972. Thus all unflagged pairs reach the strict
0.05 target. On outliers, P5 reduces test error by about 72% and P7 by 39%, but
P7 is worse than P5. The cap's fitted P5 gain is only about 7%; its test error
remains substantial. This is not monotone convergence in P.

The predeclared fitting fallback reran both hard groups at maximum step 1/256,
with the same models, data, seed and stopping target. It did not repair fitting:

| Case, smaller step | Dense train | P3 train / test | P5 train / test | P7 train / test |
|---|---:|---:|---:|---:|
| ReLU10 arc | 0.08810 | 0.08340 / 0.18666 | 0.09862 / 0.07797 | interrupted; no endpoint |
| SELU20 cap | 0.04976 | 0.04980 / 0.10968 | 0.07584 / 0.10743 | 0.09094 / 0.12866 |

Only the smaller-step cap P3 comparison passes the <=0.065 training gate.
The ReLU fallback was terminated once its failed dense/P3 fit gate made the
matched-reference comparison invalid; P5 had already finished, and P7 was
interrupted. Its smaller-looking P5 test RMS is not a successful result.
All completed adverse results remain saved. Dense query predictions shift by
0.59715 (arc, underfitted reference) and 0.32106 (cap) across step settings;
results from different step settings must not be attributed solely to P.

Protocol: user-authorized continuation on the three named failures only, width
2048, original seed 20260920, original data and 1,024-point full-circle/equal-area
sphere queries, original activation gains/readout, float32, TF32 off, no
normalization and unchanged canonical equations. Each model targets train RMS
0.05; require both dense and closure <=0.065 for query-accuracy interpretation.
The step is the shared guarded-Euler maximum, not a fixed-step/GF accuracy
certificate. Each fit has a 115-second training cap and 200,000-step cap. Only
the two underfitted groups activated one smaller-step fallback, with no new
architecture or task-specific code. No test predictions enter training.

There were 19 completed fits and one interrupted fit, with 11 completed fits
meeting RMS <=0.05. Maximum completed runtime including setup/query was
116.26 seconds; the sum of completed model runtimes was 1,553.18 seconds
(25.89 GPU-minutes). Including the interrupted worker, execution stayed below
the declared 20-fit / 40-GPU-minute ceiling. No further runs are queued.
The requested fully fitted higher-P comparison is therefore only partially
resolved, not silently certified by the small training-loss median elsewhere.

Evidence in `data/generated/neural_response_memory_20260922/response_higher_p01/`:

- [comparison.csv](../../data/generated/neural_response_memory_20260922/response_higher_p01/comparison.csv): every group, step, dense/closure training RMS, test RMS and fit gate.
- [all_runs.csv](../../data/generated/neural_response_memory_20260922/response_higher_p01/all_runs.csv) and [summary.json](../../data/generated/neural_response_memory_20260922/response_higher_p01/summary.json): all 19 completed models and timings; missing P7 endpoint is null.
- [aborted_refinement.json](../../data/generated/neural_response_memory_20260922/response_higher_p01/aborted_refinement.json): reason and termination record for the invalid ReLU fallback.
- [operator_check.json](../../data/generated/neural_response_memory_20260922/response_higher_p01/operator_check.json): eight independent explicit-matrix checks at P5/P7, ReLU/SELU and depths 10/20. Width 9, float64, unit-moment gain, readout std1, six three-dimensional Gaussian samples (data seed981, model seed20260920), after eight steps of 1e-4; maximum prediction discrepancy 2.78e-16.

All prediction/data hashes were verified and RMS values recomputed using the
canonical summarizer. Data arrays match bitwise across step settings and saved
configs match the five `higherp_*` entries in the existing catalog. The Python
implementation is unchanged, SHA-256
`97470496d39813ccb9482ef6cb475d167367526e5654541f0f2a001920f34145`.
Reproduce a group with the existing CLI, for example
`--config studies/neural_response_memory_20260922/experiment_configs.json --experiment higherp_selu20_outliers --device cuda:1 --out FRESH`,
and rescore with `--summarize OUTPUT`. These are internally checked finite-run
observations; no order-convergence theorem or established-code promotion.

#### Theoretical response-clock implementation and circle validation (2026-09-26)

The existing `WeightedFlow` path now uses the theorem's unscaled response clock
by default, direct built-in activation curvature, one batched Gram solve without
an inverse, and float64 history moments/Gram/clock with float32 network actions.
The implementation remains in the single `compact_flow.py`; both clocks share
its network, fitting and experiment runner. Explicit historical RMS-clock configs
remain available. These numerical/default changes supersede section 9's statement
that weighted moments always use the network dtype.

All 49 new width-2048 GPU fits reached training RMS <=0.05. Main new-clock fits
used 2.07–10.05 seconds; the maximum including the single refinement was 12.46
seconds. Three circle tasks were compared at P1/P2/P3, tanh depth 2 and GELU
depth 3, with matched dense initialization. New-clock P3 RMS was below 0.05 in
five of six main groups. GELU/alternating quadrant was the exception: P3 RMS
1.24526 at step 1/64 fell to 0.11200 at 1/128 with a fresh matched dense run;
P1/P2 stayed poor despite fitting. This establishes fast fitting and several
accurate fitted predictors, not universal low-order accuracy or superiority.

[The canonical guide](CANONICAL_FLOW.md#completed-response-clock-comparison)
contains the full old/new P1/P2/P3 table, protocol, memory accounting and commands.
[Comparison CSV](../../data/generated/neural_response_memory_20260922/response_clock_validation01/comparison.csv)
and [summary](../../data/generated/neural_response_memory_20260922/response_clock_validation01/summary.json)
retain all 49 GPU runs. Independent operator/clock checks passed 694 assertions;
six CUDA-graph/eager checks had zero discrepancy. The CPU interruption is saved
separately and excluded from these results. Root performed these implementation
and empirical checks; no agents or promotion review were used. Scope remains
finite-step, separately fitted endpoints; the mathematical O(P^-2) rate is not
empirically certified. The bounded comparison is complete; no runs are queued.

#### P4/P5 extension of both clocks completed (2026-09-26)

Extended the same six width-2048 circle cases at maximum step 1/64 and the
GELU/alternating-quadrant 1/128 check to ordinary and response-clock P4/P5.
All 35 new fits reached training RMS <=0.05 in 0.94–11.49 seconds each;
all seven fresh dense references and datasets matched the previous runs bitwise.
The canonical solver is unchanged. At P5 all main-table RMS values are below
0.013 except response-clock GELU/alternating quadrant (0.99568; 0.10313 at
1/128). The corresponding ordinary P5 errors are 0.01279 and 0.02150.
Higher order usually helps but does not make the new clock uniformly better.

The [canonical guide](CANONICAL_FLOW.md#completed-response-clock-comparison)
now contains the full P1–P5 table. Evidence is in
[comparison_p1_p5.csv](../../data/generated/neural_response_memory_20260922/response_clock_p45_01/comparison_p1_p5.csv),
[summary.json](../../data/generated/neural_response_memory_20260922/response_clock_p45_01/summary.json)
and the same directory's operator/capture check and per-model records.
Root verified all hashes/RMS, reference equality and eight P4/P5 operator/GPU
capture checks. Internal empirical check only, no promotion or asymptotic-rate
claim. The 35-fit extension is complete; no additional runs are queued.

#### Broad new-clock sweep completed (2026-09-26)

User-authorized rerun of the earlier 82-case activation/depth/task coverage with
fresh dense references and unscaled response-clock P1/P2/P3 at width 2048.
The existing model/data/seed and maximum step 1/64 are preserved; a uniform
20-second training cap and no retries keep the campaign bounded to 328 fits.
Report whole-space RMS and flag dense/closure train RMS >0.05 separately,
retaining the earlier 0.065 eligibility gate only as a secondary annotation.
The [canonical guide](CANONICAL_FLOW.md#broad-new-clock-sweep-protocol-2026-09-26)
records the frozen protocol and results. All 328 fits completed with finite
predictions; 282 reached training RMS <=0.05 and 46 hit the cap. Dense fitted
79/82 cases; P1/P2/P3 fitted 70/82, 67/82 and 66/82. The fitted-pair median test
RMS values are 0.042725 / 0.018895 / 0.006795; on the same 65 fully fitted cases,
0.031467 / 0.013385 / 0.006579. Large fitted P3 errors remain for alternating
quadrant with SiLU depth3 (1.362737), GELU depth3 (1.245256), and SELU depth2
(0.369138). Dense misses occur for ReLU depth10/full circle and arc, and SELU
depth20/arc, all high-frequency cases. Seventeen configurations contain at least
one training miss; all are flagged in the complete report.

Median model time was 3.97 seconds, including setup/prediction. Root verified
all saved hashes, recomputed all 328 RMS values, and checked case coverage,
configuration agreement and unchanged solver source. No agents or solver
modifications. This is an internally checked, single-seed empirical panel of
finite-step endpoints; no continuous-flow/asymptotic-rate claim. Outputs:
[full 82-row report](../../data/generated/neural_response_memory_20260922/newclock_sweep01/report.md),
[training/test RMS and flags](../../data/generated/neural_response_memory_20260922/newclock_sweep01/sweep_table.csv),
[summary/checks](../../data/generated/neural_response_memory_20260922/newclock_sweep01/summary.json).
Configs: `newclock_sweep_*`; worker schedules, commands and source hashes are
preserved with the outputs. Complete; no tuning or additional runs are queued.

#### Old-clock normalization sweep completed (2026-09-26)

User-authorized extension to LayerNorm and BatchNorm using the existing
canonical implementation, width 2048, the same 82 activation/depth/task cases
per normalization, and old-clock P1/P2/P3 with fresh dense references. Both use
pre-activation normalization and trainable affine parameters with mobility n;
BatchNorm backpropagates the loss across the full batch and uses only final
training statistics for passive evaluation. The common 1/64 step and 0.05 RMS
target are retained; a 10-second cap per model limits 656 fits, with no tuning
or retries. D/C flags identify underfitting; W means both fit but full-domain
test RMS against dense exceeds 0.1 (severe above 0.5).

The [canonical guide](CANONICAL_FLOW.md#old-clock-normalization-sweep-protocol-2026-09-26)
records the frozen scope, architecture, checks and stopping rule. Configs are
`norm_sweep_*`; outputs/checks/schedule belong to `normalization_sweep01/`.
Root owns this run and its result updates; no agents or extra Python file.
All **656 fits** completed: **598** reached training RMS <=0.05 and **58**
hit the cap. Dense/P1/P2/P3 fitted **68/71/70/69** of 82 LayerNorm cases and
**80/80/80/80** BatchNorm cases. Fitted-pair median P1/P2/P3 test RMS:
LayerNorm **0.027217 / 0.026294 / 0.017548** on the same 68 cases;
BatchNorm **0.069920 / 0.077657 / 0.072834** on the same 80 cases.
At P3, **9/68** LayerNorm and **34/80** BatchNorm pairs have good training but
test RMS >0.1; **17** BatchNorm pairs exceed 0.5. Worst fitted P3 errors are
0.338499 (LayerNorm/GELU15/alternating outliers) and 4.339615
(BatchNorm/SiLU3/alternating quadrant). All 16 configurations containing
underfitting and all fitted discrepancies are retained and flagged.

Median total model runtime was **0.72 seconds**, maximum 11.54 including setup
and queries. Root checked 3,938 normalization/moment/oracle assertions and
eight exact CUDA capture/eager comparisons, plus 684 unnormalized regression
assertions. All saved RMS values and hashes were recomputed/verified and all
50 experiment groups exited successfully with the frozen solver source.
Evidence: [all 164 training/test rows and flags](../../data/generated/neural_response_memory_20260922/normalization_sweep01/report.md),
[CSV](../../data/generated/neural_response_memory_20260922/normalization_sweep01/sweep_table.csv),
[summary/checks](../../data/generated/neural_response_memory_20260922/normalization_sweep01/summary.json).
Internally checked finite-step, single-seed endpoints; no normalized-model
convergence theorem or intrinsic fitting obstruction is claimed. The panel is
complete; no tuning, retries or additional training is queued.

<!-- END_CURRENT_VALIDATION_STATUS -->

The principal scientific gaps are practical weighted-clock accuracy and
conditioning; a uniform all-time or width-limit theorem; reliable low-order
behavior on difficult deep tasks; economical initialized-operator compression;
and accurate scalar dynamics that can acquire new response directions.
Successful fitting, dense-function tracking and target generalization remain
separate criteria for each investigation.

Complete arguments and evidence remain in their source studies. Earlier
chronological README material is recoverable from Git before this consolidation
(checkpoint `e78bc3376eeaa97df81e8899cd79ca6f74e33269`). The historical studies provide
context, not additional assumptions in the response-memory proofs. Ongoing
experimental updates belong in the validation block above; this consolidation
does not change code or experiment protocols.
