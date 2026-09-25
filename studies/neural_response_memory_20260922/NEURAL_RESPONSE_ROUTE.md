# Moving neuron responses: exact equations and the finite-closure gap

This is a theory-only, prompt-scoped derivation for the supplied finite two-hidden-layer tanh network. No other study, scientific source, numerical experiment, or initialization distribution was used. The target is a current response state per neuron that replaces repeated application of the full middle-layer matrix and its transpose. The identities below are exact; an accurate, width-independent finite response closure is **open**.

## 1. Exact current responses

There are \(m\) training samples, weights \(w\in\mathbb R^{n\times d}, W\in\mathbb R^{n\times n}, c\in\mathbb R^n\), inputs \(u_a=x_a/\sqrt d\), and nonnegative data weights \(\rho_a\). Define
\[
h_a=\tanh(wu_a),\quad z_a=Wh_a,\quad H_a=\tanh z_a,
\quad f_a=\frac{c^TH_a}{n},\quad r_a=f_a-y_a,
\]
\[
D_a=\operatorname{diag}(1-h_a^2),\quad
E_a=\operatorname{diag}(1-H_a^2),\quad
\delta_a=E_ac,\quad q_a=W^T\delta_a,\quad
\gamma_a=\rho_ar_a.
\]
Powers and products inside a diagonal are componentwise. Also put
\[
G_{ab}=u_a^Tu_b,\qquad k_{ab}=\frac{h_a^Th_b}{n},\qquad
\ell_{ab}=\frac{\delta_a^T\delta_b}{n}.
\]
The supplied unhalved-MSE flow with mobilities \((n,1,n)\) is
\[
\dot w=-2\sum_b\gamma_bD_bq_bu_b^T,\quad
\dot W=-\frac2n\sum_b\gamma_b\delta_bh_b^T,\quad
\dot c=-2\sum_b\gamma_bH_b.
\]
Since \(\dot h_a=D_a\dot w u_a\),
\[
\dot h_a=-2\sum_b\gamma_bG_{ab}D_aD_bq_b. \tag{1}
\]
Differentiating \(z_a=Wh_a\), including **both** terms, gives
\[
\dot z_a=-2\sum_b\gamma_b
\left[k_{ab}\delta_b+G_{ab}W D_aD_bq_b\right]. \tag{2}
\]
Thus the next forward response is the vector
\[
P_{ab}=W(D_aD_bq_b)\in\mathbb R^n. \tag{3}
\]
This is a response to a moving probe, not a fixed feature or a stored weight entry. Equivalently, the second term in (2) uses the operator \(W D_aD_bW^T\) acting on \(\delta_b\); storing this whole operator would restore quadratic weight-sized state.

For the backward response, first differentiate the output sensitivity:
\[
\dot\delta_a=E_a\dot c-2(H_a\odot\delta_a)\odot\dot z_a.
\]
Consequently,
\[
\dot q_a=-2\sum_b\gamma_b
\left[\ell_{ab}h_b+W^TE_aH_b\right]
-2W^T\operatorname{diag}(H_a\odot\delta_a)\dot z_a. \tag{4}
\]
After substituting (2), the additional backward responses needed at this stage can be named
\[
U_{ab}=W^TE_aH_b,\qquad
V_{ab}=W^T\operatorname{diag}(H_a\odot\delta_a)\delta_b,
\]
\[
T_{ab}=W^T\operatorname{diag}(H_a\odot\delta_a)
               W D_aD_bq_b.
\]
Then
\[
\dot q_a=-2\sum_b\gamma_b(\ell_{ab}h_b+U_{ab})
+4\sum_b\gamma_b(k_{ab}V_{ab}+G_{ab}T_{ab}). \tag{5}
\]
The mixed response \(T_{ab}\) displays the nonlinear forward/backward coupling: a forward response is multiplied by a state-dependent diagonal and passed through the **same** operator's transpose.

## 2. The hierarchy and the actual adjoint

For any differentiable first-layer probe \(v(t)\in\mathbb R^n\) and second-layer probe \(u(t)\in\mathbb R^n\), the product rule gives the exact response transport identities
\[
\frac d{dt}(Wv)=-\frac2n\sum_b\gamma_b\delta_b(h_b^Tv)+W\dot v, \tag{6}
\]
\[
\frac d{dt}(W^Tu)=-\frac2n\sum_b\gamma_bh_b(\delta_b^Tu)+W^T\dot u. \tag{7}
\]
For example, differentiating \(P_{ab}\) requires
\[
W\frac d{dt}(D_aD_bq_b),
\quad
\dot D_a=-2\operatorname{diag}(h_a\odot\dot h_a),
\]
and hence responses to diagonal products involving \(q\), \(\dot q\), and further mixed forward/backward responses from (5). Differentiating those responses produces further ones. All use the current state. The recurrence is autonomous before truncation and requires no stored trajectory.

One precise construction begins with \(c,h_a,z_a,q_a\), adjoins the response vectors required by their exact derivatives, and repeatedly adjoins those required by the newly retained responses. Each finite stage contains finitely many sample-labelled vectors. Products and contractions of already retained vectors do not require access to \(W\). New applications of \(W\) or \(W^T\) to unavailable probes are the explicitly identified boundary of that stage. This gives an exact hierarchy; it does not establish a useful finite closing stage independent of \(n\).

Forward and backward responses cannot be replaced independently. For every retained compatible pair of probes, exact adjoint reuse implies
\[
u^T(Wv)=(W^Tu)^Tv. \tag{8}
\]
For example,
\[
\delta_a^TP_{ab}=q_a^TD_aD_bq_b. \tag{9}
\]
An approximate hierarchy should preserve the relevant instances of these identities. Separate fresh randomness for forward and backward actions does not represent the supplied network's actual transpose reuse.

The same point is visible in the output kernel. Substitution of (2) into
\(\dot f_a=(\dot c^TH_a+\delta_a^T\dot z_a)/n\) gives
\[
\dot f_a=-2\sum_b\rho_br_bK_{ab},\qquad
K_{ab}=\frac{H_a^TH_b}{n}+k_{ab}\ell_{ab}
+G_{ab}\frac{(D_aq_a)^T(D_bq_b)}{n}. \tag{10}
\]
Each summand is a Gram kernel: for the middle term use the vectors
\(h_a\otimes\delta_a/n\); for the last term use
\(u_a\otimes D_aq_a/\sqrt n\). Hence \(K\) is positive semidefinite, and for \(L=\sum_a\rho_ar_a^2\),
\[
\dot L=-4\sum_{a,b}\rho_a\rho_br_ar_bK_{ab}\le0. \tag{11}
\]
This exact dissipation property does not automatically survive independently chosen approximations to the response terms in (2) and (4). Merely writing down a positive kernel for a separate \(f\)-equation would also require checking its consistency with the retained \(c,H\) readout.

## 3. A small state is demonstrably insufficient

The state \(c,h,z,q\) does not determine its own next derivative, even for one sample and two neurons. Take \(d=1,u=1,\rho=1,y=1\), choose \(w=(\operatorname{arctanh}(1/2),0)^T\), and set
\[
h=(1/2,0)^T,\quad c=(1,0)^T,\quad
W_\alpha=\begin{pmatrix}0&1\\2&\alpha\end{pmatrix}.
\]
For every real \(\alpha\),
\[
z=(0,1)^T,\quad H=(0,\tanh1)^T,\quad f=0,\quad r=-1,
\quad\delta=(1,0)^T,\quad q=(0,1)^T.
\]
Thus all retained quantities coincide. But \(D=\operatorname{diag}(3/4,1)\), so (1) gives \(\dot h=(0,2)^T\), while (2) gives
\[
\dot z=(9/4,2\alpha)^T.
\]
The missing information is precisely a response to a probe not determined by \(h\) and \(\delta\). This disproves an exact deterministic closure using only these named coordinates on the full finite-network class. It does **not** disprove a richer finite response closure, a restricted-class result, or an appropriate statistical-limit closure.

## 4. What a finite closure would have to do

At stage \(K\), retain the chosen current response coordinates \(S_K\). Write their exact evolution schematically as
\[
\dot S_K=F_K(S_K,R_K),
\]
where \(R_K\) consists of the next unavailable operator responses from (6)–(7). A proposed autonomous closure replaces them by
\[
R_K\approx C_K(S_K,\xi_K),\qquad
\dot\xi_K=G_K(S_K,\xi_K). \tag{12}
\]
The auxiliary \(\xi_K\), if used, is finite current state. This is the place for a derived relaxation or nonlinear response law. Setting a highest time derivative to zero is only one particular, usually poor, choice. A prescribed terminal law must be derived from allowed initialization/model information and estimated on reachable states; calling an unknown conditional expectation a closure does not supply it. A conditional law that depends on the untracked history or on the exact evolving distribution has merely moved the unresolved problem.

Every exact weight derivative above is proportional to current residuals. Consequently all exact response derivatives vanish when every residual vanishes. A finite closure can preserve this stationary set by retaining that residual structure, together with the appropriate adjoint and output consistency identities. Such structure allows equilibria and plateaus, but by itself proves neither approximation accuracy nor successful learning.

For a fixed locally Lipschitz closed vector field with Lipschitz bound \(A_K\), an exact retained trajectory satisfying the closed equation plus a defect \(d_K(t)\) obeys the elementary stability estimate
\[
\|S_K(t)-\widehat S_K(t)\|
\le e^{A_Kt}\|S_K(0)-\widehat S_K(0)\|
+\int_0^t e^{A_K(t-s)}\|d_K(s)\|\,ds. \tag{13}
\]
Here the bound requires both trajectories to remain in the region where that Lipschitz bound applies. It follows by the norm inequality
\(\frac d{dt}\|e\|\le A_K\|e\|+\|d_K\|\) and an integrating factor. The decisive unresolved estimate is a small defect produced by an admissible finite terminal law, with controlled stability constants. Equation (13) supplies no rate or convergence claim without that estimate.

## 5. Plateaus and zero Taylor radius

A finite ODE state does not imply a time polynomial. The polynomial conclusion applies to the special closure \(x^{(K+1)}=0\). For example, the one-state law
\[
\dot x=-\lambda(x-x_\infty),\qquad\lambda>0,
\]
has an exponential plateau, and the two-state law \(\dot x=v,\dot v=-\lambda v\) has \(x(t)\to x(0)+v(0)/\lambda\). These observations are about the form of a closure, not evidence that either closes the neural hierarchy.

The user's premise of a zero Taylor radius for a population observable is accepted. It is compatible with finite-dimensional dynamics **per population member**, even analytically simple dynamics. As an explicit illustration, take \(Z\sim N(0,1)\), \(\lambda=e^Z\), and
\[
\dot x_\lambda=-\lambda x_\lambda,\qquad x_\lambda(0)=1,
\quad O(t)=\mathbb E[x_\lambda(t)]=\mathbb E[e^{-\lambda t}],\quad t\ge0.
\]
Completing the square in the Gaussian density gives
\(\mathbb E[\lambda^k]=e^{k^2/2}\). Since \(\lambda^k\) is integrable and
\(|\partial_t^ke^{-\lambda t}|\le\lambda^k\) for \(t\ge0\), dominated convergence justifies all right derivatives at zero:
\[
O^{(k)}(0+)=(-1)^ke^{k^2/2}.
\]
The Taylor coefficient roots satisfy
\[
\left|\frac{O^{(k)}(0+)}{k!}\right|^{1/k}
\ge\frac{e^{k/2}}{k}\longrightarrow\infty,
\]
so the Taylor radius is zero. Nevertheless \(O(t)\to0\) by dominated convergence, since \(\lambda>0\) almost surely. This example has one evolving scalar and one fixed parameter per member. It shows why nonanalyticity of a population average is not a no-go theorem for current per-neuron state. It is not a substitute architecture or a theorem about the network above. In particular, a population of such states is distinct from one finite deterministic analytic ODE for the population observable itself.

## 6. Information and complexity accounting

- **Initialization:** At finite \(n\), exact initial responses are computed from the specified initial \(w_0,W_0,c_0\) by the same formulas. One can in principle compute retained responses once and discard \(W_0\), but the setup still uses its realized entries and can cost quadratic work. The prompt supplies no initialization distribution, so a closed limiting joint law cannot be asserted. Because \(z_0=W_0h_0\) and \(q_0=W_0^T\delta_0\), their dependencies cannot be replaced by independent random draws without proof.
- **No hidden operator:** Retaining a callable action of \(W(t)\), a full evolving kernel over all probes, or all past rank-one updates is not finite response compression. Indeed
  \[
  W(t)=W_0-\frac2n\sum_b\int_0^t\gamma_b(s)\delta_b(s)h_b(s)^T\,ds
  \]
  is exact but applying it to a new current probe requires history unless that action has itself been closed.
- **Autonomy:** The infinite response recurrence is autonomous. A finite candidate is autonomous and restartable only when every right-hand side and readout is computable from its current finite state and permitted fixed data. Initialization from future trajectories, time-indexed forcing, or a remaining full-operator oracle fails that requirement.
- **Width:** A fixed response stage has a finite number of coordinates per neuron, while retaining the neuron population. At fixed sample count this can be linear in \(n\) instead of quadratic, but the number of responses may grow quickly with stage. This is not a finite total-dimensional population closure, and width-independent approximation accuracy has not been proved.
- **Sample count:** Already \(P_{ab},U_{ab},V_{ab},T_{ab}\) carry two sample labels. Further derivatives can add labels, so storage can involve \(n m^{p(K)}\), along with the data Gram matrix. A statement of finite state per neuron must declare whether \(m\) is fixed. Population-data functions of a continuous input are not finitely many scalars without a separate input approximation. Predictions on additional test inputs also require their corresponding retained probes or another justified readout.

The exact result is the moving response skeleton (1)–(9), with its dissipative observable identity (10)–(11), and a counterexample to closure at the smallest state. The central remaining task is to derive a finite nonzero terminal response law from allowed initial information and control its omitted-response defect. Neither a convergence theorem nor a useful approximation rate is established here.
