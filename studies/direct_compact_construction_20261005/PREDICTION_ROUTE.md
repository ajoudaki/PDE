# Prediction-first direct compression: exact hierarchy, a law-built candidate, and the strict-root boundary

2026-10-05. Scoped independent theoretical attempt. No experiment, training
run, width-\(n\) initialization, trajectory query, or other study was used.
This note is not an internal check or a promotion review.

## 1. Outcome

I did **not** obtain an unconditional direct compact construction satisfying
the full target. The strongest defensible result is a precise conditional
construction with two independent missing bridges:

1. a quantitative, initialization-law-built population source/cubature
   theorem with polylogarithmic retained size; and
2. a strict all-time, whole-sphere \(n^{-1/2}\) finite-width sampling bound
   around the deterministic population predictor.

Once those two statements hold, the already checked corrected-residual
runtime gives a direct autonomous model of all-retained size

\[
 O_{\rm data}\!\left([\log(en)]^{3d+2}\right)
\]

and the triangle inequality gives the requested comparison with an
**independent** fresh width-\(n\) dense run at the same physical time,
including the fitted endpoint. The proposed initialization uses only the
dataset, Gaussian initialization law, \(n\), and optional independent setup
randomness. It never forms an \(n\)-vector or \(n\)-by-\(n\) array.

The first missing bridge is not supplied by replacing a dense realization by
its source-space compressor: that existing preprocessing differentiates the
actual width-\(n\) ODE and forms width-\(n\) coefficient vectors before
discarding them. It is therefore outside the present direct-initialization
contract. The second missing bridge is also real: the maintained population
theorem is qualitative in width, and the available independent-dense upper
bound is \(n^{-1/2+o(1)}\), not strict root width.

There are two positive structural findings.

- The exact prediction/tangent-kernel equations identify a genuinely
  prediction-first hierarchy. It evades the recent lower bound because it
  does not approximate the whole first-layer feature map.
- Orthogonality permits the established scalar activation transform. For
  common first-layer roots it removes the changed-gate coordinate carrier
  from the **state-equation** subtraction. Residual damping still requires a
  joint first-layer tangent-kernel moment, and perturbing the Gaussian roots
  introduces a second transform-sensitivity moment. This narrows the strict
  root route but does not close it. The quantitative finite-width bias and
  indexed Gaussian estimate also remain open.

## 2. Frozen contract and notation

Put \(v=x/\sqrt d\in S^{d-1}\), and write the orthonormal training directions
as \(v_1,\ldots,v_m\). The dense reference is

\[
 h_n(t,v)=\tanh(A_n(t)v),\qquad
 g_n(t,v)=\tanh(W_n(t)h_n(t,v)),\qquad
 f_n(t,v)=\frac{w_n(t)^\top g_n(t,v)}n .
\]

Initially, \((A_n)_{ij}\sim N(0,1)\), \((W_n)_{ij}\sim N(0,1/n)\)
independently, and \(w_n(0)=0\). With
\(r_{n,a}=f_n(t,v_a)-y_a\), mean squared loss and mobilities \((n,1,n)\)
give

\[
 \begin{aligned}
 \dot A_n&=-\frac2m\sum_a r_{n,a}\delta^{(1)}_{n,a}v_a^\top,\\
 \dot W_n&=-\frac2{mn}\sum_a r_{n,a}\delta^{(2)}_{n,a}h_n(t,v_a)^\top,\\
 \dot w_n&=-\frac2m\sum_a r_{n,a}g_n(t,v_a),
 \end{aligned}
\]

where

\[
 \delta^{(2)}_{n,a}=w_n\odot(1-g_n(t,v_a)^2),\qquad
 \delta^{(1)}_{n,a}=(1-h_n(t,v_a)^2)\odot W_n^\top\delta^{(2)}_{n,a}.
\]

Let \(Y=\|y\|_2/\sqrt m\). The small-label regime is the inherited one,
which in the present notation contains \(Y\le c\lambda\), where \(\lambda\)
is the normalized initialized top-feature Gram gap. All constants below may
depend on the fixed data, \(d,m\), the gap, and confidence, but not on \(n\).

The required comparison is

\[
 \|F-f_n^{\rm fresh}\|_*
 :=\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
       |F(t,v)-f_n^{\rm fresh}(t,v)|
 \le \frac{C_{{\rm data},\delta}}{\sqrt n}
\]

with probability at least \(1-\delta\). The fresh dense run is independent
of the compact model. A compact model may use its own randomness, but not the
fresh run's initialization or trajectory. Physical time may not be changed.

## 3. The established deterministic center

The maintained global orthogonal-data theorem constructs a deterministic
population action flow for this two-hidden-layer tanh model. Exact zero
readout is an admitted initialization. Setting the theorem's three mobility
multipliers to \(1/m\) gives the present mean-loss clock.

For tanh, let

\[
 \Psi(z)=\frac z2+\frac{\sinh(2z)}4,
 \qquad J(s,z)=\Psi^{-1}(\Psi(z)+s).
\]

Indeed \(\Psi'(z)=\cosh^2z=1/\tanh'(z)\). The polynomial
\(z+z^3/3\) is the corresponding primitive for arctangent, not tanh.

Orthogonality turns each first-layer training preactivation into

\[
 Z_a^{(1)}(t)=J(X_a(t),Z_{0,a}^{(1)}).
\]

On two population spaces, let \(\mathsf W_0\) be the initialized Gaussian
action with its actual adjoint, let \(\mathsf W=\mathsf W_0+\mathsf K\), and
let \(C\) be the population readout. In the canonical notation, the exact
autonomous equations are

\[
 \begin{aligned}
 \dot X_a&=-\frac2m r_a\mathsf W^*\Delta_a^{(2)},\\
 \dot{\mathsf K}&=-\frac2m\sum_a r_a\,
                  \Delta_a^{(2)}\otimes H_a^{(1)},\\
 \dot C&=-\frac2m\sum_a r_aH_a^{(2)}.
 \end{aligned}
 \tag{1}
\]

The forward fields, backward fields, prediction, and residual in (1) are
computed from the same current state. The maintained theorem proves global
existence, uniqueness, autonomy, restart from the reached state, and
finite-width convergence on every separately fixed compact time interval.
It gives no convergence rate.

The inherited small-label Gram tube and energy estimates pass to this limit
on every finite interval. They give exponential residual decay and an
integrable prediction speed. Thus the deterministic population predictor,
denoted \(f_\infty(t,v)\), has a sphere-uniform endpoint. This identifies a
legitimate center for a direct construction; it does not quantify
\(\|f_n-f_\infty\|_*\).

There is an exact symmetry reduction. If \(R\in O(d)\) fixes every training
direction \(v_a\), the initialization law and (1) are unchanged by
\(v\mapsto Rv\). Uniqueness therefore gives

\[
 f_\infty(t,Rv)=f_\infty(t,v).
\]

Consequently the population predictor is a function of only

\[
 s(v)=(v_1^\top v,\ldots,v_m^\top v)\in B_m,
 \tag{2}
\]

not of the orientation of the component orthogonal to the data span. This
is useful for a prediction-only polynomial chaos; it does not make the
hidden population action finite-dimensional.

## 4. Exact prediction-first causal skeleton

Use mobility-Euclidean parameters

\[
 \Theta=(A_n,\sqrt n\,W_n,w_n),\qquad
 \mathcal P_v(\Theta)=n f_n(v),qquad
 q_v=\nabla_\Theta\mathcal P_v,qquad
 H_v=D_\Theta^2\mathcal P_v.
\]

Then the finite network satisfies the exact identities

\[
 \dot\Theta=-\frac2m\sum_a r_{n,a}q_{v_a},
 \qquad
 K_t(v,u)=\frac{q_v^\top q_u}{n},
 \tag{3}
\]

and hence

\[
 \dot f_n(t,v)=-\frac2m\sum_a r_{n,a}K_t(v,v_a),
 \qquad
 \dot r_{n,a}=-\frac2m\sum_bK_t(v_a,v_b)r_{n,b}.
 \tag{4}
\]

The next equation is already outside a state consisting only of prediction
and tangent kernel:

\[
 \dot K_t(v,u)=-\frac2m\sum_b r_{n,b}
 \frac{(H_vq_{v_b})^\top q_u+q_v^\top H_uq_{v_b}}n.
 \tag{5}
\]

Differentiating the new contraction in (5) introduces third derivatives and
transported responses. Thus (4)--(5) are an exact autonomous hierarchy, not
a closed \((f,K)\) system.

At zero readout, all hidden-gradient blocks vanish. Therefore
\(K_0(v,u)=g_n(0,v)^\top g_n(0,u)/n\) and \(\dot K_0=0\). In the population
limit the onset is the separated zonal formula

\[
 \dot f_\infty(0,v)=\frac2m\sum_a y_a k_0(v_a^\top v),
 \tag{6}
\]

with one deterministic scalar kernel \(k_0\). For orthogonal inputs,
oddness gives \(k_0(0)=0\), while \(k_0(1)>0\). Equation (6) explains why
prediction can be much simpler than the initialized whole-feature family.

It does not justify freezing \(K_t\). Hidden motion begins at second order
and is quadratic in the labels; the exact second-derivative formulas contain
cross-label terms which need not vanish. Nothing in the current hypotheses
bounds the resulting prediction remainder by a quantity tending to zero with
\(n\) for fixed nonzero labels. A fixed-kernel or finite-onset model therefore
answers a different question unless a uniform remainder theorem is proved.

## 5. Audited direct routes

### 5.1 I.i.d. law sketches: a sharp obstruction for the naive estimator

Let \(Z\sim N(0,1)\), put \(q_1=\mathbb E\tanh^2 Z\), and let

\[
 U=\tanh(\sqrt{q_1}\,Z)^2.
\]

The variable \(U\) is bounded and nonconstant, so
\(\sigma^2=\operatorname{Var}(U)>0\). A plain \(q\)-particle law sketch of
the initialized diagonal top-feature kernel uses

\[
 \widehat\gamma_q=\frac1q\sum_{j=1}^qU_j.
\]

The central limit theorem gives

\[
 \sqrt q(\widehat\gamma_q-\mathbb EU)\Longrightarrow N(0,\sigma^2).
\]

If \(q=o(n)\), then for every fixed \(C<\infty\),

\[
 \mathbb P\!\left\{
 |\widehat\gamma_q-\mathbb EU|\le Cn^{-1/2}\right\}\longrightarrow0.
 \tag{7}
\]

Under the usual triangular-array Lindeberg condition, the same conclusion
holds for nonnegative weighted i.i.d. sampling when the effective sample size
\((\sum_j\omega_j^2)^{-1}\) is \(o(n)\). Hence a
polylogarithmic number of ordinary Monte Carlo neurons cannot even estimate
this one nondegenerate onset coefficient at the required scale. This is a
no-go for naive i.i.d. random features, not for deterministic high-order
cubature, control variates, or structured stochastic rules.

### 5.2 Prediction hierarchy or dynamic mean-field kernels

Equations (4)--(5) suggest expanding every passive-query field in
polynomials of the \(m\) variables (2), while retaining the discrete training
indices exactly. A causal dynamic-mean-field formulation would instead store
the finite collection of training covariance and response kernels in two
time variables, plus their cross-kernels with (2). Spectral time and query
representations could then have polylogarithmic storage if their coefficients
decayed quantitatively.

This is the cleanest genuinely prediction-first architecture. It is also
currently only formal for the requested theorem. The missing statements are:

1. rigorous identification of the causal kernel system with (1), including
   both orientations of the reused Gaussian action;
2. a quantitative tail bound for response depth or for the two-time kernel
   expansion;
3. stability showing that omitted high modes cannot feed back into the
   retained prediction at order larger than \(n^{-1/2}\); and
4. a restart representation whose saved memory is fixed in advance rather
   than a growing list of past time nodes.

A finite actual-path query mesh does not close these gaps. A sampled query
has already used omitted matrix actions, so its value is not measurable from
the retained transcript. Treating its next Gaussian response as fresh would
delete the learned reuse. The maintained supplied-path warning makes this
noncausality explicit.

Naive response-depth truncation has a second cost problem: ordered training
words can grow like \(m^p\) at depth \(p\). Taking \(p\asymp\log n\) is then
polynomial, not polylogarithmic, in \(n\). A positive theorem needs a genuine
kernel, symmetry, or low-rank compression of those words; it cannot merely
rename the hierarchy as polynomial chaos.

### 5.3 A law-built Galerkin model with a corrected residual

The most developed conditional witness keeps the checked compact runtime but
replaces every realized finite-width source by a source computed from the
population law.

Fix

\[
 T_n=C\lambda^{-1}\log(en),\qquad \epsilon_n=n^{-1}.
\]

The required **population source assertion** is the following.

> From the dataset, Gaussian action law, \(n\), and finite initial
> differentiation of (1), construct spaces
> \(S_{1,n}\subset L^2(\Omega_1)\) and
> \(S_{2,n}\subset L^2(\Omega_2)\), with
> \[
> R_n:=\max_\ell\dim S_{\ell,n}
> \le C_{\rm data}[\log(en)]^{3d/2+1},
> \tag{8}
> \]
> which approximate, through \(T_n\), the whole-sphere forward fields,
> training backward fields, and their paired \(\mathsf W_0\) and
> \(\mathsf W_0^*\) images to tolerance \(\epsilon_n\). The paired
> coefficient actions are exact, and the selected-node errors and carrier
> norms satisfy the deterministic comparison hypotheses.

The power in (8) is the two-hidden-layer specialization of the existing
intrinsic spherical source count. That existing theorem concerns a realized
finite network; it does **not** prove the population assertion above.

If (8) holds, choose normalized bases of the two spaces. Their Gram matrices
and the cross-action contractions

\[
 D_{ij}=\mathbb E_2[e_{2,i}\,\mathsf W_0e_{1,j}]
\]

are determined by the initialization law. A law-level finite
sparsification can be obtained by first approximating each finite Gram by a
finite law sample or deterministic cubature, whitening it, and then applying
the general-vector sparsification step. This uses only setup randomness. It
selects \(N_\ell\le9R_n\) nodes and produces fixed positive metrics
\(H_1,H_2\), together with a finite initialized action \(B_0\). All temporary
law samples are discarded. Quantitative work, precision, and conditioning of
this setup are not presently bounded.

The moving state is

\[
 (A_C,B_C,w_C,c_C)
 \in\mathbb R^{N_1\times d}\times
 \mathbb R^{N_2\times N_1}\times
 \mathbb R^{N_2}\times\mathbb R^m.
\]

Its forward pass is

\[
 h_C(v)=\tanh(A_Cv),\qquad
 g_C(v)=\tanh(B_Ch_C(v)).
\]

Let \(G_C=[g_C(v_1),\ldots,g_C(v_m)]\) and
\(Q_C=G_C^\top H_2G_C\). Define the effective readout and prediction by

\[
 \widehat w_C=w_C+G_CQ_C^{-1}
       (y-c_C-G_C^\top H_2w_C),
 \qquad F_C(t,v)=\widehat w_C^\top H_2g_C(v).
 \tag{9}
\]

Thus \(y-F_C(t,v_{1:m})=c_C\) identically. With
\(B_C^*=H_1^{-1}B_C^\top H_2\), set

\[
 \delta_{C,a}^{(2)}=(1-g_C(v_a)^2)\odot\widehat w_C,
 \qquad
 \delta_{C,a}^{(1)}=(1-h_C(v_a)^2)\odot B_C^*\delta_{C,a}^{(2)}.
\]

The internal Gram is

\[
 \begin{aligned}
 K^C_{ab}={}&\langle g_C(v_a),g_C(v_b)\rangle_{H_2}\\
 &+\langle\delta_{C,a}^{(2)},\delta_{C,b}^{(2)}\rangle_{H_2}
   \langle h_C(v_a),h_C(v_b)\rangle_{H_1}\\
 &+\langle\delta_{C,a}^{(1)},\delta_{C,b}^{(1)}\rangle_{H_1}
   v_a^\top v_b.
 \end{aligned}
 \tag{10}
\]

The autonomous physical-time equations are

\[
 \begin{aligned}
 \dot A_C&=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^\top,\\
 \dot B_C&=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(2)}
                         h_C(v_a)^\top H_1,\\
 \dot w_C&=\frac2m\sum_a c_{C,a}g_C(v_a),\\
 \dot c_C&=-\frac2mK^Cc_C.
 \end{aligned}
 \tag{11}
\]

The model is not ordinary gradient flow on a smaller network. It is the
explicit checked corrected-residual optimizer. Equations (9)--(11) use only
the current compact state, fixed metrics, and retained data; no target
trajectory, residual, or endpoint is supplied.

## 6. Conditional theorem and complete resource/error split

Assume the population source assertion (8), a setup realization whose total
coefficient error is at most \(\epsilon_n\), and the strict dense sampling
statement

\[
 \mathbb P\left\{
   \|f_n^{\rm fresh}-f_\infty\|_*>
       C_{{\rm data},\delta}n^{-1/2}\right\}\le\delta
 \tag{12}
\]

for every sufficiently large \(n\).

Then (9)--(11) is a direct compact construction satisfying the requested
contract. The proof separates as follows.

### Moving state

\[
 S_{\rm move}=dN_1+N_1N_2+N_2+m
             =O(R_n^2+dR_n+m).
\]

### Fixed retained storage

The two metrics, initialized action metadata, data, and optional Gram/feature
caches require

\[
 S_{\rm fixed}=O(R_n^2+mR_n+m^2+m(d+1)).
\]

Since the exact initial top Gram has rank \(m\), necessarily
\(m\le N_2\le9R_n\), so the caches are already \(O(R_n^2)\). Thus

\[
 S_{\rm move}+S_{\rm fixed}
 =O_{\rm data}([\log(en)]^{3d+2}).
 \tag{13}
\]

This is a real-coordinate count, not a bit or arithmetic bound.

### Setup computation

Setup consists of finite population initial jets, finite Gaussian
expectations for Gram/action coefficients, law cubature or sampling,
whitening, and spectral sparsification. It creates no width-\(n\) object.
The exact-real setup is finite at every fixed truncation order if the source
compiler terminates, but no polylogarithmic work theorem, conditioning bound,
or finite-precision theorem follows from (8). With inexact arithmetic, let
\(e_{\rm setup}\) be the induced source/action error. It enters the comparison
as another source term and must obey

\[
 e_{\rm setup}\,\mathcal A_n\lesssim n^{-1/2},
\]

where \(\mathcal A_n\) is the proved stability amplification. Merely storing
few coefficients does not certify that they can be computed cheaply.

### Compact approximation error

The checked energy identity for (11) is

\[
 -\frac d{dt}\|c_C\|_m^2
 =\|\dot\theta_C\|_{\rm par}^2,
 \qquad \theta_C=(A_C,B_C,w_C).
 \tag{14}
\]

Because \(K^C\succeq Q_C\), the small-label first-exit argument preserves
the initial Gram gap globally, gives exponential residual decay, finite path
length, and exact interpolation at the endpoint. The source comparison on
\([0,T_n]\), with residual damping retained, gives the population analogue

\[
 \sup_{t\le T_n,v}|F_C(t,v)-f_\infty(t,v)|
 \le C_{\rm data}n^{-1}\exp(C_{\rm data}\sqrt{\log(en)}).
 \tag{15}
\]

For fixed data, the right side is at most
\(C_{\rm data}/\sqrt n\) eventually. This is **conditional** because the
population source/cubature hypotheses needed to invoke the checked
comparison have not been proved.

### Stability and endpoint

Both flows have

\[
 \sup_v|\partial_tF(t,v)|\le C_{\rm data}\rho(t),
 \qquad \rho(t)\le Ye^{-c\lambda t}.
\]

Choosing the fixed structural multiplier in
\(T_n=C\lambda^{-1}\log(en)\) makes both endpoint tails \(O(n^{-1})\).
Thus (15) extends to \([0,\infty]\) without freezing either trajectory or
changing clocks.

### Dense sampling bias and final assembly

This is separate from every compact approximation estimate. By (12), (15),
and the triangle inequality,

\[
 \|F_C-f_n^{\rm fresh}\|_*
 \le \|F_C-f_\infty\|_*+\|f_\infty-f_n^{\rm fresh}\|_*
 \le \frac{C_{{\rm data},\delta}}{\sqrt n}
\]

at confidence \(1-\delta\), after adding any setup failure probability to
the failure budget. No coupling between compact and dense initializations is
used.

## 7. The strict dense-rate bottleneck in the orthogonal model

The established scalar transform removes one obstruction that appears in the
general-data comparison, but only the first subtraction closes.
First compare two transformed states with the **same** first-layer Gaussian
roots and with controlled initial-action/feedback perturbation \(E_0\). Let
\(D(t)\) be the sum of the normalized clock, middle-operator, and readout
differences. Since

\[
 \left|\tanh(J(s,z))-\tanh(J(\widetilde s,z))\right|
 \le |s-\widetilde s|,
\]

direct subtraction of (1) on a common small-label tube gives

\[
 D(t)\le C E_0+C\int_0^t\|r-\widetilde r\|_m\,ds
 +C\int_0^t(\rho+\widetilde\rho)(D+E_0)\,ds.
 \tag{16}
\]

The point is that the clock equation contains \(\mathsf W^*\Delta^{(2)}\)
without a changed first-layer gate multiplying a coordinate carrier.
Bounded tanh derivatives, the middle operator norm, and the readout
coordinate supremum control every term in normalized \(L^2\); no
\(\sqrt{\log n}\) maximum enters this **common-root** estimate.

To combine (16) with residual damping one would need

\[
 \|K-\widetilde K\|_{\rm op}/m\le C_{\rm data}(D+E_0).
 \tag{17}
\]

The readout and middle tangent blocks admit this subtraction from the state
bounds. The first block contains, schematically,

\[
 \mathbb E\!\left[
   \{\tanh'(Z_a^{(1)})q_a\}^2
   -\{\tanh'(\widetilde Z_a^{(1)})\widetilde q_a\}^2
 \right],\qquad q_a=\mathsf W^*\Delta_a^{(2)}.
\]

Its changed-gate term multiplies \(q_a^2\). An \(L^2\) response bound does
not control this product. A joint fourth-moment/localization estimate, or a
different cancellation, is still needed. Thus orthogonality removes the
carrier from (16), but does not by itself prove (17).

If (17) holds, subtracting the exact residual equations and using one path's
tangent-Gram gap gives

\[
 \int_0^t\|r-\widetilde r\|_m\,ds
 \le C\lambda^{-1}\int_0^t
       (\rho+\widetilde\rho)(D+E_0)\,ds.
 \tag{18}
\]

Since both residual activities are integrable, (16) and (18) then yield

\[
 \sup_{t\ge0}D(t)\le C_{\rm data}E_0.
 \tag{19}
\]

This conditional common-root estimate would be useful for an
oracle-to-empirical or width-doubling coupling built on common Gaussian
actions.

It does **not** yet give a Gaussian Lipschitz estimate under arbitrary root
replacement. For different first-layer roots one additionally needs, on the
actually reached random clocks, a bound of the form

\[
 \left\|\tanh(J(X,Z_0))-\tanh(J(X,\widetilde Z_0))\right\|_{L^2}
 \le C_{\rm data}\|Z_0-\widetilde Z_0\|_{L^2}.
 \tag{20}
\]

The generic flow estimate gives a factor exponential in a coordinate clock
bound; the available theory controls the clocks in \(L^2\), not in coordinate
supremum. A stochastic moment/localization proof of (20), or a coupling that
keeps these roots fixed, is therefore an additional strict-rate obligation.

Even if (17) and (20) are proved, Gaussian concentration controls fluctuation around a
median, while qualitative population convergence gives no rate for that
median. A crude net over time and the sphere reintroduces a
\(\sqrt{\log n}\) factor. A complete proof needs one of the following:

- a width-doubling or finite-to-population coupling with \(O(n^{-1/2})\)
  bias; or
- a legitimately localized Gaussian-Sobolev/chaining argument whose
  initialization sensitivities have root-scale increments in both the
  compactified time coordinate and the sphere query, followed by a
  quantitative identification of the deterministic center.

The second route looks plausible here because the passive forward map is
smooth and orthogonality removes the first-gate carrier from common-root
training-state stability. It remains a proof obligation, not a theorem in
this note.

## 8. Scope of the recent lower bound and other no-go statements

The recent finite-network theorem says that a **fixed linear neuron-coordinate
space** approximating the entire initialized first-layer feature family to
root-width RMS accuracy has dimension at least

\[
 c_d[\log n]^{3(d-1)/2}
\]

with high probability. If one stores a full metric on that space, the
specific architecture has storage at least
\(c_d[\log n]^{3d-3}\).

This has three precise consequences here.

1. It does not rule out the prediction hierarchy (4)--(5), which never asks
   for a uniform approximation of \(h_n(0,\cdot)\).
2. It does not rule out structured or implicit metrics.
3. The conditional Galerkin construction in Section 5 deliberately remains
   a whole-source, quadratic-metric fallback. Its upper exponent \(3d+2\)
   is compatible with the lower exponent \(3d-3\); no reduction to
   \([\log n]^d\) is claimed.

The only new impossibility statement proved here is (7), for ordinary i.i.d.
law sampling. Failure of a frozen kernel, an actual-path mesh, or an
unstructured response truncation is witness-specific. None is a no-go theorem
for all autonomous prediction-only models.

## 9. Claim ledger and next decisive step

| Claim | Status |
| --- | --- |
| Global deterministic orthogonal-tanh population action flow, autonomy, and compact-time qualitative width convergence | Established maintained result |
| Population predictor depends only on the training projections (2) | Exact consequence of symmetry and uniqueness |
| Exact prediction/tangent hierarchy (3)--(5) | Proved finite-width identity |
| I.i.d. polylog-particle coefficient estimate at strict root scale | Ruled out by (7) for the stated estimator class |
| Orthogonal transformed state subtraction (16) | Deterministic on the inherited fitting tube; tangent-kernel closure (17) and root sensitivity (20) remain open |
| Law-built population source theorem with (8), selected-node control, and quantitative setup | Open; construction-critical |
| Strict all-time whole-sphere dense-to-population estimate (12) | Open; construction-critical |
| Direct polylogarithmic model meeting the requested independent-dense target | Conditional on the preceding two open claims |

The single highest-leverage theoretical step is to prove a strict
root-width quantitative version of the maintained orthogonal population
limit, using the transformed stability (16)--(18). A successful proof would
settle dense sampling bias independently of the choice of compact solver. The
next compact-specific step would then be a population, law-only analogue of
the analytic paired-source theorem, with explicit cubature error and setup
conditioning. Until both are available, claiming the requested direct model
would conflate same-realization compression with independent-run prediction.

## 10. Source and process record

The five authorized scientific inputs were read completely:

- `../closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`;
- `../closure_sampling_20261003/SPHERICAL_SOURCE_DIMENSION_ROUTE.md`;
- `../closure_sampling_20261003/ERROR_PREFACTOR_GEOMETRIC_ROUTE.md`;
- `../integrated_general_compression_20261004/README.md`; and
- `../orthogonal_tanh_time_legendre_20261005/README.md`.

Relevant directly linked proof/check material read for this route included the
quadratic-runtime reconstruction, whole-query source and its reconstruction,
the integrated common result and independent-dense boundary, and the
orthogonal feature-space lower result, prediction-route note, and author
check. Maintained inputs were `docs/index.qmd`, `docs/notation.qmd`, the global
orthogonal population theorem in `docs/04-continuing-flows.qmd`, the
supplied-path causality boundary in `docs/02-gaussian-reuse.qmd`, and the
finite observable-closure statements in Chapters 7--8. No archived book
material was read.

The repository-required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was
inaccessible (`Permission denied`) even after a read-only escalation. The
mathematical communication rules in `AGENTS.md`, the maintained notation
contract, and the rigorous-math and conjecture workflows were used as the
fallback. No computation or experiment was performed.
