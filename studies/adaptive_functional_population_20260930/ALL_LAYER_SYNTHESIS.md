# Fixed-depth functional encoding: what extends uniformly in width

Internal research synthesis, 2026-09-30. This continues the first-layer encoder in `CENTROID_MEMORY.md`. The requested target is a finite, sample-count-independent functional representation of all forward and backward history fields, preferably with the earlier quadratic encoding rate and eventually with autonomous feedback. The full target is **not established** here.

The proved extension covers every forward layer and the last backward layer, with a first-order representation-budget rate. Its constants are independent of width and of the number of training samples. A separate streaming construction compresses every learned hidden operator with an inverse-rank operator-norm bound. Earlier backward fields, a quadratic all-layer rate, and an autonomous compressed trainer remain open. Neither a conditional tail lemma nor an arbitrary-state obstruction is presented as settling these questions.

Scientific inputs: this study's first-layer construction and three explicitly scoped derivations, together with the maintained book's notation. Relevant established background was checked in `docs/05-continuation-boundaries.qmd`, Section J, “Exact bounded-memory and coordinate partials”: learned reverse-memory smoothing and the adapted Gaussian-column obstruction. Those ingredients are not claimed as new relative to the book. No other study was read. No training experiment or paper edit was made.

## 1. Precise positive statement

Consider an arbitrary probability law of `(x,y)` with `||x||/sqrt(d) <= R` and `E y^2 = Y^2 < infinity`. An empirical law with any number `m` of samples is included. There are `L` hidden layers, all of width `n`, with

\[
h_1=\phi(W_1x/\sqrt d),\quad h_\ell=\phi(W_\ell h_{\ell-1}),
\quad f=w^Th_L/n,\quad r=f-y.
\]

Let `phi` be bounded and twice continuously differentiable, with bounded first and second derivatives. Write `B=||phi||_infty`, `A=||phi'||_infty`. This includes tanh; it does not assert the same theorem for unbounded ReLU. The exact canonical gradient flow is

\[
\delta_L=w\odot\phi'(z_L),\qquad
\delta_\ell=\phi'(z_\ell)\odot W_{\ell+1}^T\delta_{\ell+1},
\]
\[
\dot W_1=-2E[r\delta_1x^T/\sqrt d],\quad
\dot W_\ell=-2E[r\delta_\ell h_{\ell-1}^T]/n\ (\ell\ge2),
\quad \dot w=-2E[rh_L].
\tag{1}
\]

Initialize `w=0`. The first-layer initialization may be arbitrary; retain the exact initialized hidden matrices `G_l=W_l(0)`, with `max_l ||G_l||op <= K0`. Gaussian initialization is covered by the event quantified below. Fix any finite `T` and depth `L`. No small-label condition and no data-Gram gap are required.

Set `|v|_n=||v||_2/sqrt(n)`, `rho=(E r^2)^(1/2)`, and `tau=1+int rho dt`. For shifted Legendre polynomials `p_k` on `[0,1]`, define the normalized forward history

\[
\bar H_{\ell k}(t,x)=\frac1{\tau(t)}\left[
\int_0^1p_k(u/\tau(t))h_\ell(0,x)du+
\int_0^t\rho(s)p_k(\tau(s)/\tau(t))h_\ell(s,x)ds\right].
\tag{2}
\]

For every integer budget `M>=1`, there is a causal encoder driven by (1) with

\[
\max_{\ell\le L}\sup_{t\le T}\sup_{x\in X}
|\bar H_{\ell k}(t,x)-\widetilde H_{\ell k}(t,x)|_n
\le C_{L,T}/M.
\tag{3}
\]

The same constant works separately for every history index `k`, because `|p_k|<=1`. It does not imply that summing `q` modes with arbitrary reconstruction coefficients adds no `q` factors. The bound is an RMS across neurons, uniformly over input and time, not an individual-neuron sup norm.

The encoder retains at most

\[
O\bigl(ndM+LnM\min(n,M)\bigr)
\subseteq O(ndM+LnM^2)
\tag{4}
\]

learned real-valued descriptors. One shared exact initialization costs `nd+(L-1)n^2` additional real numbers. Thus neither (3) nor (4) conceals a dense learned network inside each atom. There is no retained `m` factor. Dependence on input dimension is explicitly at least linear through `ndM`; no input mesh or degree cutoff is used.

The normalized last-layer backward history

\[
\bar B_{Lk}(t,x,y)=\frac1{\tau(t)}\int_0^t
p_k(\tau(s)/\tau(t))r(s,x,y)\delta_L(s,x)ds
\tag{5}
\]

has an encoder with

\[
\sup_{t\le T}\|\bar B_{Lk}-\widetilde B_{Lk}\|_{L^2(P;\ell^2_n)}
\le C_{L,T}/M.
\tag{6}
\]

Storing `q` such backward modes adds `O(M(n+q))` descriptors. The norm in (6) averages over the data law as well as neurons; it is not a supremum over arbitrarily large labels. Constants depend on `L,T,R,Y,K0` and the activation bounds, not on `n,m`. This is a fixed-horizon statement, not an all-time bound.

## 2. Proof and construction

### Existence and energy

At each fixed finite width, (1) is locally Lipschitz in its finite-dimensional parameter state. On a bounded parameter set, its derivatives are dominated by `C_ball(1+|y|)` because inputs and activation derivatives are bounded. This is integrable under the assumed second label moment, justifying differentiation of the expectations.

Local ODE existence and uniqueness therefore apply. Direct substitution in the loss derivative gives

\[
-\dot{\mathcal L}=v(t)^2,
\qquad v(t)^2=\|\dot W_1\|_F^2/n+
\sum_{\ell=2}^L\|\dot W_\ell\|_F^2+\|\dot w\|_2^2/n.
\tag{7}
\]

Consequently `rho<=Y`, `int_0^T v^2<=Y^2`, and

\[
\int_0^Tv\,dt\le V:=Y\sqrt T.
\tag{8}
\]

At fixed width this bounds displacement in every parameter coordinate on every finite interval. The local ODE solution cannot escape every bounded set in finite time, and hence continues globally. This existence argument does not require width-uniform Euclidean parameter norms.

### Learned operators have controlled nuclear mass

Put `Q=K0+V`. Equation (8) bounds every hidden operator norm by `Q`, and `|w|_n<=V`. Backward recursion gives

\[
\sup_{t\le T,x}|\delta_\ell(t,x)|_n
\le D_\ell:=A^{L-\ell+1}Q^{L-\ell}V.
\tag{9}
\]

For a rank-one matrix, `||ab^T||_* = ||a||_2 ||b||_2`. Thus, for every hidden learned increment,

\[
\begin{aligned}
\|\dot W_\ell\|_*
&\le 2E[|r|\,|\delta_\ell|_n|h_{\ell-1}|_n]
\le2BD_\ell\rho,\\
\sup_{t\le T}\|W_\ell(t)-G_\ell\|_*
&\le\kappa_\ell:=2BD_\ell TY.
\end{aligned}
\tag{10}
\]

This estimate uses a probability average over the data, not an unnormalized sum. It is therefore independent of sample count even when `m` greatly exceeds the selected rank. Exact finite rank is **not** an assumption.

Keeping the largest `s` singular values yields

\[
\|\Delta W_\ell-\Delta W_{\ell,s}\|_{op}
=\sigma_{s+1}\le\kappa_\ell/(s+1),\qquad s<n.
\tag{11}
\]

For `s=n`, the error is zero. Indeed `(s+1)sigma_{s+1}` is bounded by the sum of singular values. This is the structural reason fixed-time learned interactions admit sample-independent operator approximation.

### Cover movement, not input space

Differentiating the forward equations yields

\[
\sup_x|\dot h_1|_n\le c_1v,\quad c_1=AR,
\qquad \sup_x|\dot h_\ell|_n\le c_\ell v,
\quad c_\ell=A(B+Qc_{\ell-1}).
\tag{12}
\]

Open a cell whenever the accumulated parameter movement `int v dt` increases by `delta=V/M`. There are at most `M+1` cells. At a cell's opening, store the first-layer matrix exactly and rank `s=min(n,M)` factors of every hidden learned increment. All cells share the original `G_l`. These descriptors define a frozen depth-`L` circuit; its atoms have no pointers to uncounted past trained networks.

The snapshot's forward error obeys

\[
e_1=0,\qquad e_\ell\le AQe_{\ell-1}+AB\kappa_\ell/(s+1).
\tag{13}
\]

To verify this, subtract preactivations as
`W(h-h_tilde)+(W-W_tilde)h_tilde`, use the exact operator bound and bounded approximate activations, then the Lipschitz constant `A`. By (12), using that same frozen circuit until the cell closes adds at most `c_l delta`. Thus the instantaneous field error within each cell is at most `C(delta+1/(s+1))`; if `s=n`, omit the truncation term. Both cases give `C/M`.

Integrate these frozen fields with their **exact scalar history coefficients**. For a cell's clock interval `[a,b]`, its coefficient in (2) is

\[
\tau(t)^{-1}\int_a^{b\wedge\tau(t)}p_k(u/\tau(t))du.
\tag{14}
\]

Stored endpoints and a polynomial antiderivative determine it. The prefix field is retained exactly. Since the total normalized integration mass is at most one and `|p_k|<=1`, the instantaneous error bound proves (3). Each cell costs `nd+O(Lns)` learned numbers, proving (4). If `Y=0`, the flow is stationary and no such partition is necessary.

### Why the last backward layer also works

The readout equation gives the stronger coordinatewise bound

\[
\|w(t)\|_\infty\le2BTY.
\tag{15}
\]

Save `w` when each cell opens. Equation (15), bounded `phi''`, and the preactivation version of (12)--(13) control
`delta_L=w phi'(z_L)` within a cell by `C/M` in neuron RMS, uniformly in input. The scalar output has the same bound: subtract `w^Th/n` and use `|w|_n<=V`, `|h|_n<=B`.

For a frozen cell source `g_j=(f_j-y)delta_L^j`, the identity

\[
r\delta_L-g_j=r(\delta_L-\delta_L^j)+(f-f_j)\delta_L^j
\tag{16}
\]

therefore gives joint data-neuron `L2` error at most `C/M`, using `||r||_L2<=Y`. Integrating (16) in physical time proves (6).

The coefficients for (5) require more than clock endpoints. For each cell store `q` numbers

\[
a_{jp}(t)=\int_{I_j\cap[0,t]}\tau(s)^p ds,
\qquad 0\le p<q.
\tag{17}
\]

Their derivatives are `tau(t)^p` for the active cell and zero for closed cells. Expanding `p_k` as a polynomial recovers the needed physical-time integrals exactly. This avoids dividing by `rho`, remains valid on flat-clock intervals, and proves the stated added storage. A numerically conditioned Legendre transport implementation can replace raw powers without changing the mathematical state count.

### Gaussian probability

A `1/4`-net with at most `9^n` points and the scalar Gaussian tail imply, for entries `N(0,1/n)`,

\[
P(\|G\|_{op}>K_0)\le2\exp\{2n\log9-nK_0^2/8\}.
\tag{18}
\]

For instance `K0=8` makes the failure probability for all hidden matrices at most `2(L-1) exp[-n(8-2 log9)]`. Alternatively select `K0` from any fixed requested confidence, uniformly over all `n>=1`. These are high-probability width-uniform constants for the **same retained Gaussian matrices**, not a replacement initialization. Zero readout ensures `L(0)=Y^2` independently of the draw.

## 3. Exact scope of the compression and execution

Taking `M` proportional to `epsilon^-1` gives learned descriptors

\[
O_{L,T,R,Y,\phi,K_0}(nd/\epsilon+Ln/\epsilon^2+q/\epsilon).
\tag{19}
\]

This has no training-sample factor and no input-dimensional exponent of `epsilon`. It is weaker in accuracy exponent than the first-layer centroid construction. It also retains the exact initialized dense matrices.

Querying one input through all snapshots costs
`O(M[nd+Ln^2+Ln min(n,M)] + qLMn)`, including exact `G_l` actions and history accumulation. Producing a snapshot's factors by SVD can require dense temporary storage. The canonical dense process is still the driver and counts toward the memory of a running training experiment. Therefore (19) is an **encoding bound**, not a certified reduction in the peak memory or per-step cost of autonomous training.

`ALL_LAYER_OPERATOR.md` additionally derives a finite-stream signed covariance sketch, retaining `2ns` numbers per hidden layer, with operator error at most `2 V_atom/(s+1)`. Here `V_atom` is the accumulated nuclear mass of the actual rank-one updates and is bounded by (10). Its proof accounts for covariance mass discarded at every shrink. It removes the need for a dense *live sketch*, but neither supplies its own gradient sources nor proves a width-uniform quadrature cost for continuous population expectations. The implementation and source-driver qualifications remain material.

## 4. What prevents the full equivalent theorem

For an earlier backward layer, comparing exact and approximate responses introduces

\[
[\phi'(\widehat z_\ell)-\phi'(z_\ell)]\odot k_\ell,
\qquad k_\ell=W_{\ell+1}^T\delta_{\ell+1}.
\tag{20}
\]

The bounds above control both factors in normalized `L2` but do not control their product in `L2`. At the top layer, (15) resolves this. It does not resolve a lower layer after an initial Gaussian transpose has acted on a trained, correlated signal.

For example, if `G_ij` are `N(0,1/n)` and `v_i=sign(G_i1)`, then `||v||_infty=1` but
`(G^T v)_1/sqrt(n) -> sqrt(2/pi)`. A gate error of order one at this single coordinate has vanishing neuron RMS but an order-one effect after multiplication. `ALL_LAYER_OPERATOR.md` realizes this obstruction in two nearby nonlinear snapshots with the same exact Gaussian hidden cores, bounded learned nuclear/column norms and bounded readout coordinates. **Canonical gradient-flow reachability of those snapshots is not proved.** This refutes a proposed inference from norm bounds, not the requested trained-path theorem.

A precise sufficient repair would be a uniform squared-tail estimate for the *actual reference carriers*. For instance define

\[
\chi(K)=\sup_{n,\ell,t\le T,x}
|k_\ell(t,x)\mathbf1_{|k_\ell(t,x)|>K}|_n.
\tag{21}
\]

If `chi(K)->0`, split (20) into coordinates with `|k|<=K` and its complement:

\[
|[\phi'(\widehat z)-\phi'(z)]k|_n
\le \|\phi''\|_\infty K|\widehat z-z|_n+2A\chi(K).
\tag{22}
\]

Backward induction then gives a modulus `C[(1+K)eta+chi(K)]` from forward/snapshot accuracy `eta`, and the physical-time argument (16)--(17) extends to all layers. A bound `sup |k|_{p,n}<=C_p` with `p>2` would yield the explicit modulus `C eta^(1-2/p)` by Holder and boundedness of the gate difference. Only reference-carrier tails are needed; no independent tail bound for the approximate trajectory is necessary.

Neither (21) nor this higher-moment bound has been proved here for the canonical trained Gaussian system. It cannot be inserted as an innocuous regularity assumption and called an unconditional answer.

Finally, quadratic centroid error after composition requires more than (12). Its Taylor remainder contains `(Delta z)^2`; its normalized `L2` norm is `||Delta z||_{4,n}^2`. Bounded `phi''` and an `L2` displacement estimate do not provide the required `L4` bound. A direction concentrated on one neuron makes the corresponding whole-network Hessian norm grow like `sqrt(n)`. Separate neuronwise allocation overcame this for the first layer; an efficient compositional counterpart remains to be constructed.

## 5. Evidence and status

- `ALL_LAYER_FORWARD.md`: complete forward theorem, explicit constants, exact descriptors, Gaussian event and last-layer backward extension.
- `ALL_LAYER_FORWARD_CHECK.md`: independent internal check of that derivation, including norm distinctions, rank saturation, physical-time coefficients and fixed-width flow continuation.
- `ALL_LAYER_OPERATOR.md`: independently derived nuclear/streaming route, constructive sketch proof and explicit snapshot obstruction.
- `ALL_LAYER_CURVATURE.md`: exact variation and smoothing estimates, second-order mixed-moment bounds and their unresolved hypotheses.

These are internal derivations and checks, not promotion reviews. The positive all-forward/top-backward result is narrower than the requested all-response theorem. The latter remains an open obligation in this study.
