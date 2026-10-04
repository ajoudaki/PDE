# All-layer driven forward histories: a width-uniform first-order construction

Internal scoped derivation, 2026-09-30. Scientific inputs: the supervisor's canonical equations and `CENTROID_MEMORY.md`, read completely. No other study, book passage, experiment, or external result is used. This is a forward-history encoding theorem for canonical dense gradient flow on a fixed time horizon. It is not a theorem for autonomous compressed training, and it does not establish the desired quadratic budget rate at all layers.

The positive result is concrete. Every layer's normalized forward history can share a collection of compositional snapshots. Canonical gradient flow gives a width-independent nuclear-norm bound for each trained hidden-matrix increment. Consequently, each snapshot can store those increments in low-rank form, paying for the trained weights explicitly. With M history cells and rank M, the history error is O(M^{-1}) and the learned snapshot descriptors cost O(ndM + LnM^2), in addition to the shared exact initialization. The latter costs nd + (L-1)n^2 real numbers when stored explicitly. There is no sample-count factor in these retained descriptors. A separately identified extension in Section 8 also encodes the last-layer backward history at this rate.

## 1. Contract and notation

All hidden layers have width n. Inputs satisfy ||x||/sqrt(d) <= R on X. Let phi be C_b^3, and write B = sup |phi| and A = sup |phi'|. The proof of the positive theorem only uses boundedness and bounded first derivative. Let P be the probability law of (x,y), with the stated support condition on x. The loss is E_P r^2, r=f-y, and rho=(E_P r^2)^{1/2}. Expectations below are population expectations; an empirical law with any sample count is included.

The canonical network and flow are

\[
 h_1=\phi(W_1x/\sqrt d),\qquad
 h_\ell=\phi(W_\ell h_{\ell-1}),\qquad
 f=w^Th_L/n,
\]
\[
 \delta_L=w\odot\phi'(z_L),\qquad
 \delta_\ell=\phi'(z_\ell)\odot W_{\ell+1}^T\delta_{\ell+1},
\]
\[
 \dot W_1=-2\mathbb E[r\delta_1x^T/\sqrt d],\quad
 \dot W_\ell=-\frac2n\mathbb E[r\delta_\ell h_{\ell-1}^T],\quad
 \dot w=-2\mathbb E[rh_L].
\tag{1}
\]

Assume the classical flow exists on [0,T], starts with w(0)=0, and has loss at most L0 initially. Its given dissipation implies

\[
 q(t)^2:=\|\dot W_1\|_F^2/n+
 \sum_{\ell=2}^L\|\dot W_\ell\|_F^2+
 \|\dot w\|_2^2/n,
 \quad
 \int_0^Tq^2dt\le L_0,
 \quad \rho(t)\le\rho_0:=\sqrt{L_0}.
\tag{2}
\]

For v in R^n set |v|_n=||v||_2/sqrt(n). The error norm is

\[
 \|g\|_{X,n}:=\sup_{x\in X}|g(x)|_n.
\tag{3}
\]

It is the neuron RMS norm uniformly over input x; data-population L^2(mu;ell^2_n), for every input probability measure mu supported on X, is a weaker consequence. It does not give a uniform bound on every neuron. Constants below are independent of n and of sample count, conditional on a bound K0 for the initial hidden-matrix operator norms. Section 5 supplies a width-uniform probability statement for the exact Gaussian initialization.

Set tau(t)=1+int_0^t rho(s)ds. For u in [0,1] use the constant prefix h_l(0,x), and on the remaining clock interval use the actual h_l(t,x), with du=rho(t)dt. On flat-clock intervals no new mass enters. For any specified p_k with |p_k|<=1 on [0,1], the target is

\[
 \overline H_{\ell k}(t,x)=\frac1{\tau(t)}
 \left[\int_0^1p_k(u/\tau(t))h_\ell(0,x)du+
 \int_0^t\rho(s)p_k(\tau(s)/\tau(t))h_\ell(s,x)ds\right].
\tag{4}
\]

This includes the shifted Legendre coordinates in the assignment. Every k receives a separate bound; a weighted combination of many coordinates requires its own coefficient factor.

The encoder is driven by the canonical trajectory. It does not replace that trajectory's gradient equations, and its coefficients are collected causally when a cell opens. No future trajectory or sample-indexed response table is retained.

## 2. Uniform operator, adjoint, nuclear, and variation estimates

Define

\[
 V=\sqrt{TL_0},\qquad Q=K_0+V,\qquad
 D_\ell=A^{L-\ell+1}Q^{L-\ell}V.
\tag{5}
\]

The following deterministic statements hold on the event max_{l>=2} ||W_l(0)||op <= K0.

First, Cauchy--Schwarz and (2) give

\[
 \int_0^Tqdt\le V,\qquad
 \|W_\ell(t)-W_\ell(0)\|_F\le V,\qquad
 |w(t)|_n\le V.
\tag{6}
\]

Hence ||W_l(t)||op<=Q. Coordinatewise boundedness of phi gives |h_l(t,x)|_n<=B. Multiplication by a diagonal matrix with entries bounded by A has operator norm at most A. Starting with delta_L and iterating the exact backward recursion therefore yields

\[
 \sup_{t\le T,x\in X}|\delta_\ell(t,x)|_n\le D_\ell.
\tag{7}
\]

This is an RMS bound, and must not be read as a componentwise adjoint bound. Also, zero initial readout gives the separate componentwise bound

\[
 |w_i(t)|\le2B\int_0^t\rho(s)ds\le2BT\rho_0.
\tag{8}
\]

For vectors a,b, the rank-one matrix ab^T has its only nonzero singular value equal to ||a||_2||b||_2. The triangle inequality for the nuclear norm and (1) thus give, for l>=2,

\[
 \begin{aligned}
 \|\dot W_\ell(t)\|_*
 &\le\frac2n\mathbb E[|r|\|\delta_\ell\|_2\|h_{\ell-1}\|_2]\\
 &\le2BD_\ell\mathbb E|r|
 \le2BD_\ell\rho(t).
 \end{aligned}
\tag{9}
\]

The expectations are legitimate finite-dimensional Bochner integrals: the displayed bound is integrable since r is square-integrable and the other normalized norms have deterministic bounds. Let

\[
 \kappa_\ell=2BD_\ell T\rho_0,\qquad
 \kappa=\max_{2\le\ell\le L}\kappa_\ell.
\tag{10}
\]

Integrating (9) proves

\[
 \sup_{t\le T}\|W_\ell(t)-W_\ell(0)\|_*\le\kappa_\ell.
\tag{11}
\]

Unlike the Frobenius bound alone, (11) supplies a rank-r operator-norm approximation with error O(1/r). Indeed, if A_l=W_l(t)-W_l(0) has singular values sigma_1>=...>=sigma_n>=0 and A_{l,r} retains its r largest singular values, then

\[
 \|A_l-A_{l,r}\|_{op}=\sigma_{r+1}
 \le\frac{\sum_{j=1}^{r+1}\sigma_j}{r+1}
 \le\frac{\kappa_\ell}{r+1},\qquad r<n.
\tag{12}
\]

For r>=n retain A_l exactly and use zero error. Furthermore ||A_{l,r}||op<=||A_l||F<=V, so ||W_l(0)+A_{l,r}||op<=Q. The singular-value formula and inequalities explicitly verify the needed approximation fact.

For forward variation, differentiation and the operator bound give

\[
 |\dot h_1(t,x)|_n
 \le AR\|\dot W_1\|_F/\sqrt n\le c_1q(t),
 \quad c_1=AR,
\]
\[
 |\dot h_\ell(t,x)|_n
 \le A\bigl(B\|\dot W_\ell\|_{op}
                +Q|\dot h_{\ell-1}(t,x)|_n\bigr)
 \le c_\ell q(t),
 \quad c_\ell=A(B+Qc_{\ell-1}).
\tag{13}
\]

Consequently, with s(t)=int_0^t q(v)dv,

\[
 \|h_\ell(t)-h_\ell(t')\|_{X,n}
 \le c_\ell|s(t)-s(t')|.
\tag{14}
\]

All c_l depend only on fixed depth and the displayed width-independent quantities. This estimate applies simultaneously to the entire input set; there is no input net or hidden sample factor.

For completeness, (1) gives pointwise speed bounds as well:

\[
 \|\dot W_1\|_F/\sqrt n\le2RD_1\rho,
 \quad\|\dot W_\ell\|_F\le2BD_\ell\rho,
 \quad|\dot w|_n\le2B\rho.
\tag{15}
\]

Thus q<=C rho for the explicit constant obtained by summing the squared coefficients in (15). In particular rho=0 implies q=0; there is no undefined motion hidden in a flat activity-clock interval. This also gives a width-independent first-order Lipschitz estimate in activity time. It does not furnish a second-order one.

## 3. A finite shared compositional encoder

Fix delta>0 and open a new cell whenever s(t)-s(t_j)=delta. Let t_j be its opening time and u_j=tau(t_j). There are at most 1+V/delta cells. For each cell store:

1. W_1(t_j), with nd real coordinates;
2. for every hidden l>=2, a rank-r factorization of A_{l,r}(t_j), with at most 2nr+r coordinates;
3. the scalar clock endpoint u_j.

The exact initial W_1(0) and hidden W_l(0) are shared among every cell. Define a frozen depth-L circuit for cell j using W_1(t_j) at the first layer and W_l(0)+A_{l,r}(t_j) at hidden layers; write its intermediate outputs as h_l^j. All layers' history atoms use this same circuit and its shared descendants. Descendants are frozen, so no historical atom points to a changing subnetwork.

Let e_l=sup_{j,x}|h_l(t_j,x)-h_l^j(x)|_n. Then e_1=0. Subtracting the two preactivations, using a bounded approximate feature vector and the exact matrix operator bound, gives

\[
 e_\ell\le AQe_{\ell-1}+\frac{AB\kappa_\ell}{r+1}.
\tag{16}
\]

For example, decompose Wh-Wtilde htilde as W(h-htilde)+(W-Wtilde)htilde. Since |htilde|_n<=B, this proves (16) without assuming the approximation is near the exact network. Therefore

\[
 e_\ell\le\frac{b_\ell}{r+1},\qquad
 b_1=0,\quad b_\ell=AQb_{\ell-1}+AB\kappa_\ell.
\tag{17}
\]

For r>=n all b_l/(r+1) errors can instead be replaced by zero. For t in cell j, (14) and (17) yield

\[
 \|h_\ell(t)-h_\ell^j\|_{X,n}
 \le c_\ell\delta+b_\ell/(r+1).
\tag{18}
\]

For a completed cell let its clock interval be [u_j,u_{j+1}], and for the active cell use [u_j,tau(t)]. Its exact scalar moment coefficient is

\[
 a_{jk}(t)=\frac1{\tau(t)}\int_{u_j}^{u_{j+1}\wedge\tau(t)}
                       p_k(u/\tau(t))du.
\tag{19}
\]

The prefix coefficient a_{0k}^{pre}(t) uses [0,1]. Define

\[
 \widetilde H_{\ell k}(t,x)
 =a_{0k}^{pre}(t)h_\ell(0,x)+\sum_j a_{jk}(t)h_\ell^j(x).
\tag{20}
\]

The scalar coefficients follow from the stored endpoints and current tau. For polynomial p_k they can be obtained from a polynomial antiderivative, so there are no stored per-sample coefficients or function-valued coordinates. The signs of p_k cause no difficulty: apply the triangle inequality under the integral and use |p_k|<=1. Since the history intervals have total clock length tau-1, (18) proves

\[
 \sup_{t\le T}\|\overline H_{\ell k}(t)-\widetilde H_{\ell k}(t)\|_{X,n}
 \le c_\ell\delta+\frac{b_\ell}{r+1}.
\tag{21}
\]

This holds simultaneously for every represented layer and every specified k, with no k-dependent constant under the normalization |p_k|<=1. Aggregating K+1 such coordinate errors adds a factor K+1 in an ell^1 norm or sqrt(K+1) in an ell^2 norm.

For M>=1 and V>0, take delta=V/M and r=min(n,M). With N<=M+1 cells, (21) gives

\[
 \sup_{t\le T}\|\overline H_{\ell k}-\widetilde H_{\ell k}\|_{X,n}
 \le\frac{c_\ell V+b_\ell}{M}.
\tag{22}
\]

If V=0 the trajectory is constant and one exact initial network suffices. If a singular-value tie occurs, any orthonormal choice in the tied subspace satisfies all estimates. A deterministic tie convention makes the encoder a specified causal map; continuity of that convention is not needed for the driven error guarantee.

The retained learned descriptors, including all trained weight factors, number at most

\[
 (M+1)\,[nd+(L-1)(2nr+r)+O(1)],\qquad r=\min(n,M).
\tag{23}
\]

The shared exact initialization adds nd+(L-1)n^2 real coordinates. In particular a sufficient total bound is

\[
 O\bigl(nd+Ln^2+ndM+LnM^2\bigr).
\tag{24}
\]

Choosing M proportional to 1/epsilon gives total retained state
O(nd + Ln^2 + nd/epsilon + Ln/epsilon^2), with constants depending on fixed L,T,L0,R,A,B,K0. Thus the result is efficient for the **additional trained history descriptions**, but it does not erase the quadratic storage of an explicitly retained exact Gaussian initialization. If a setting already supplies immutable W0 actions externally, (23) is the added encoder storage. Replacing an exact n^2-dimensional Gaussian draw by a scalar pseudorandom seed would change the exact-real initialization contract and is not used here.

The online encoder stores s and tau, freezes a new approximation at each opening time, and retains clock endpoints. It can be restarted when the same driver supplies future canonical weights and speeds. Computing an SVD from a dense supplied snapshot may require dense temporary memory and arithmetic. The theorem concerns retained representation size, not an implementation with subquadratic peak working memory. Counting a dense reference driver as part of the total running system adds its full trained state. The construction must not be called a fully compressed training algorithm.

## 4. Why the quadratic first-layer argument does not transfer automatically

The map from full-network parameters, in the dissipation metric, to h_l in the norm (3) has a width-independent first derivative, but its second derivative need not have a width-independent bound. This obstruction already appears for h_1 if the neurons are grouped into a single global cell; the separate per-row allocation in `CENTROID_MEMORY.md` avoids it there.

For an explicit local calculation take d=1, x=1, and a base first-layer row value b with phi''(b) != 0. Perturb only row 1 of W_1 in direction v=sqrt(n)e_1. Its dissipation-metric norm is ||v||_2/sqrt(n)=1. Yet

\[
 \left|D^2h_1(W_1)[v,v]\right|_n
 =\frac{|\phi''(b)|n}{\sqrt n}
 =|\phi''(b)|\sqrt n.
\tag{25}
\]

Equivalently, average row 1 uniformly over [b-a,b+a] for a fixed small a>0. The whole-parameter curve diameter in that metric is 2a/sqrt(n), while its centroid replacement produces a normalized feature discrepancy c(a,b)/sqrt(n), with c(a,b)>0 for tanh on an interval of strict curvature. The ratio of this discrepancy to the squared metric diameter grows like sqrt(n).

These calculations rule out a dimension-free **global parameter-centroid remainder bound on the norm-controlled parameter class**. They are not a counterexample to the actual canonical GF history theorem, and not a no-go result for every adaptive compositional encoding. In particular, the example is a parameter direction or curve; it is not asserted to be a realized GF trajectory. The energy and operator estimates alone do not supply the missing curvature control along realized trajectories.

At a deeper nonlinearity the Taylor remainder contains (Delta z_l)^{odot 2}. A normalized L^2 bound on Delta z_l does not bound its square in normalized L^2 without an L^4 or componentwise condition. Thus a proof that simply replaces every snapshot by a parameter centroid, or invokes C_b^3 as a width-independent network Hessian bound, has a specific unclosed step.

The O(M^{-1}) result (22) is the strongest rate proved here. Achieving O(M^{-2}) with comparably small all-layer descriptors remains open. Sufficient additional progress would be either a verified width-uniform curvature estimate along the canonical trajectory in the required norm, or a neuron-adaptive compositional cell construction whose stored descendants and edges have a proved total budget. Neither is assumed in this note.

## 5. Exact Gaussian initialization and probability

For completeness, a direct finite-net argument provides the initial event needed above without replacing the Gaussian matrix by a bounded deterministic surrogate. Let G have independent N(0,1/n) entries. A 1/4-net N of the Euclidean unit sphere can be constructed with |N|<=9^n: take a maximal separated set and compare the volumes of disjoint radius-1/8 balls with the containing radius-9/8 ball. Approximating both unit vectors in u^TGv by their net points gives

\[
 \|G\|_{op}\le2\max_{u,v\in N}|u^TGv|.
\]

For fixed unit u,v, u^TGv is a centered Gaussian of variance 1/n. Its elementary exponential-moment bound is P(|u^TGv|>a)<=2exp(-na^2/2). The union bound consequently yields

\[
 \Pr(\|G\|_{op}>2a)\le2\,9^{2n}e^{-na^2/2}.
\tag{26}
\]

For L>=2 and 0<eta<1, take

\[
 K_0=2\sqrt{4\log9+2\log\bigl(2(L-1)/\eta\bigr)}.
\tag{27}
\]

Substitution into (26), followed by a union bound over L-1 hidden matrices, gives probability at least 1-eta that all their operator norms are at most K0, uniformly for every n>=1. Their independence is unnecessary for this last union bound. The exact Gaussian first-layer rows may remain arbitrary in the deterministic argument because phi is bounded and forward variation only uses their displacement. For L=1 there is no hidden-matrix event or nuclear truncation term.

If L0 is itself random, interpret the theorem on the intersection of this event with the stated initial-loss bound. With zero initial readout the initial loss is E y^2, so a deterministic second-moment bound on labels supplies L0 independently of the Gaussian draw. No probability-one deterministic bound on Gaussian operator norms is asserted.

## 6. Backward fields and autonomy remain separate

The adjoint estimate (7) bounds the magnitude of delta_l. It does not show that a small forward error in (3) induces a small backward error with a width-independent constant. A gate difference is multiplied by W_{l+1}^T delta_{l+1}. Its normalized RMS may be bounded while one coordinate is as large as order sqrt(n). Multiplying that coordinate by a localized gate error can destroy a putative width-independent forward-to-backward stability estimate.

For a concrete norm-level witness, let w=1, W have first column 1/sqrt(n) and all other columns zero. Then ||W||op=1 and |w|_n=1, but W^Tw=sqrt(n)e_1. A gate perturbation supported on coordinate 1 can be small in normalized RMS and produce an order-one change after multiplication by this adjoint. This is an obstruction to inference from the proved norm bounds, not a claim that this precise state is reached by the prescribed Gaussian-initialized flow.

The backward history contains the additional factor r/rho. Square-integrable labels ensure a unit L^2 norm for r/rho when rho>0, not a uniform pointwise bound. The forward estimates alone therefore do not prove a compact encoder for every B_lk. Writing the source without division as rho (r/rho)delta=r delta does permit a last-layer extension when combined with the componentwise readout bound (8); its separate proof is in Section 8. The higher-layer adjoint multiplication obstruction still applies to l<L.

Finally, all snapshot sources here come from the supplied canonical GF. Feeding decoded histories back into a new training evolution requires an independent width-uniform stability theorem and a compatible state representation for its backward and residual fields. The canonical energy identity cannot be transferred to that new evolution by notation.

## 7. Claim audit and stopping point

| Claim | Status | Exact limit |
|---|---|---|
| Width-uniform forward variation on fixed T | Proved, (13)--(15) | Conditional on bounded initial hidden operator norms; event quantified in (26)--(27) |
| Width-uniform nuclear bound for trained hidden increments | Proved from GF, (9)--(11) | Does not compress the exact initial matrices |
| All-layer forward history encoding without sample-indexed state | Proved, (20)--(24) | Normalized population RMS uniformly over inputs; O(M^{-1}) error |
| Trained deep atom parameters are counted | Yes, (23) | Includes W1 snapshots and every low-rank hidden factor |
| O(M^{-2}) at every layer with efficient descriptors | Open | Missing concentration/curvature or compositional allocation theorem |
| Last-layer backward history encoder | Proved in Section 8 | Zero initial readout, bounded phi'', and the same driven snapshots |
| All earlier backward-field encoders | Open in this note | Forward error and adjoint magnitude do not provide backward stability |
| Autonomous compressed training, subquadratic peak memory, sample-free runtime | Not proved | Requires new arguments and an implementation model |

The positive theorem is a finite-horizon driven representation result with an explicit shared circuit and an explicit descriptor count. The unresolved step toward the original quadratic all-layer target is a width-uniform second-order mechanism that survives deep nonlinear composition without hiding dense historical descendants.

## 8. Separate extension: the last-layer backward history

Provenance: Sections 1--7 were first written as the independent forward route. The supervisor then suggested using physical-time coefficients to extend the same construction to the last backward layer. This section verifies that suggestion. It uses no additional scientific inputs.

Write K2=sup|phi''| and W_infty=2BT rho0, so (8) gives ||w(t)||_infty<=W_infty. In addition to the descriptors in Section 3, store the exact readout w(t_j) at each cell opening, at cost n coordinates per cell. Let

\[
 f^j=(w(t_j))^Th_L^j/n,\qquad
 d_L^j=w(t_j)\odot\phi'(z_L^j),\qquad
 g_L^j(x,y)=(f^j(x)-y)d_L^j(x).
\tag{28}
\]

Thus a backward atom is a frozen finite circuit with the current data pair (x,y) as its input. It stores no sample-indexed vector of labels or residuals. Access to the data law for expectation evaluation remains external, as in the forward theorem.

For L>=2 define

\[
 a_z=B+Qc_{L-1},\qquad b_z=Qb_{L-1}+B\kappa_L.
\]

For L=1 define a_z=R and b_z=0. Differentiating the last preactivation proves |dot z_L|_n<=a_z q. The same preactivation subtraction used in (16) proves a snapshot error at most b_z/(r+1). Hence, for t in cell j,

\[
 \sup_x|z_L(t,x)-z_L^j(x)|_n
 \le a_z\delta+b_z/(r+1).
\tag{29}
\]

The readout displacement obeys |w(t)-w(t_j)|_n<=delta. Subtracting the last adjoints and using the **componentwise** bound on w(t_j) gives

\[
 \begin{aligned}
 \sup_x|\delta_L(t,x)-d_L^j(x)|_n
 &\le A\delta+W_\infty K_2\bigl(a_z\delta+b_z/(r+1)\bigr)\\
 &=d_1\delta+d_2/(r+1),
 \end{aligned}
\tag{30}
\]

where d_1=A+W_infty K2 a_z and d_2=W_infty K2 b_z. Also |d_L^j(x)|_n<=AV. Subtracting the readouts yields

\[
 \sup_x|f(t,x)-f^j(x)|
 \le B\delta+V\bigl(c_L\delta+b_L/(r+1)\bigr)
 =f_1\delta+f_2/(r+1),
\tag{31}
\]

where f_1=B+Vc_L and f_2=Vb_L. Let g_L(t,x,y)=r(t,x,y)delta_L(t,x). The exact decomposition

\[
 g_L-g_L^j=r(t)(\delta_L-d_L^j)+(f(t)-f^j)d_L^j
\]

and the loss bound ||r(t)||_{L^2(P)}<=rho0 imply

\[
 \|g_L(t)-g_L^j\|_{L^2(P;\ell^2_n)}
 \le(\rho_0d_1+AVf_1)\delta
       +(\rho_0d_2+AVf_2)/(r+1)
 =\gamma_1\delta+\gamma_2/(r+1).
\tag{32}
\]

Only a second moment of labels is needed; it already follows from the zero-readout initial-loss assumption. This proof uses the sharper exact residual bound rho0 instead of a separate bound in terms of ||y||_2.

The normalized last-layer backward history, with zero prefix because w(0)=0, is exactly

\[
 \overline B_{Lk}(t,x,y)
 =\frac1{\tau(t)}\int_0^t
       p_k(\tau(s)/\tau(t))\,r(s,x,y)\delta_L(s,x)ds.
\tag{33}
\]

This identity follows from du=rho(s)ds wherever rho>0. If rho=0, the residual vanishes P-almost everywhere, so the integrand r delta also vanishes; (33) defines the continuation without a division by zero.

For each cell I_j in physical time, define

\[
 \beta_{jk}(t)=\frac1{\tau(t)}\int_{I_j\cap[0,t]}
                            p_k(\tau(s)/\tau(t))ds,
 \qquad
 \widetilde B_{Lk}=\sum_j\beta_{jk}g_L^j.
\tag{34}
\]

Clock endpoints alone do **not** determine these coefficients, because the physical-time/activity-time conversion varies along the trajectory. If the highest represented polynomial degree is K, store instead

\[
 m_{ja}(t)=\int_{I_j\cap[0,t]}\tau(s)^a ds,
 \qquad a=0,\ldots,K.
\tag{35}
\]

For an active cell dot m_ja=tau(t)^a; completed-cell moments are constant. If p_k(v)=sum_{a=0}^k c_ka v^a, then

\[
 \beta_{jk}(t)=\sum_{a=0}^k
       c_{ka}\tau(t)^{-a-1}m_{ja}(t).
\tag{36}
\]

These are K+1 ordinary scalar coordinates per cell. The powers are bounded on the fixed interval 1<=tau<=1+T rho0; this is an exact representation statement rather than a numerical-conditioning recommendation.

Apply the triangle inequality in L^2(P;ell^2_n), use |p_k|<=1, and integrate (32) over physical time. Since tau>=1,

\[
 \sup_{t\le T}
 \|\overline B_{Lk}(t)-\widetilde B_{Lk}(t)\|_{L^2(P;\ell^2_n)}
 \le T\bigl(\gamma_1\delta+\gamma_2/(r+1)\bigr).
\tag{37}
\]

With delta=V/M and r=min(n,M), the last-layer backward error is O(M^{-1}) with a width-independent constant. Exact full-rank storage gives zero rank-truncation error when r=n. The extra retained descriptors are O(M[n+K+1]), shared with the same forward snapshots. No backward field at l<L, autonomous feedback theorem, sample-free expectation oracle, or subquadratic peak-memory implementation is asserted.
