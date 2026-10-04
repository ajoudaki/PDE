# A bounded continuation: finite fluctuations and the population-bias gap

Scientific inputs: the sources listed in `FINITE_TAIL_ROUTE.md`, that note's controlled cavity proof, and the supervisor-authorized same-study `WIDTH_ROUTE.md`. No other study is used. This is an internal proof attempt, not a promotion or a proof of the requested population rate.

The controlled cavity structure gives a further finite statement: for two tanh hidden layers and orthonormal training inputs, predictions under each **fixed deterministic integrated-residual control** concentrate about their finite-width mean at strict root width, uniformly over the entire bounded activity interval. The constants do not depend on a clipping cap or time mesh. The proof below averages over all initial Gaussian randomness. It does not identify the finite-width mean with the dense population, and does not allow an adaptive random control to be inserted into a pointwise-in-control probability bound. Those are separate gaps.

## 1. Statement and notation

Use the two-layer network and transformed variables from `FINITE_TAIL_ROUTE.md`, now taking both activations to be tanh. Write \(W=W^{(2)}\), \(h_a=h_a^{(1)}\), and retain superscripts for the second-layer features and backward fields. For

\[
F(z)=z/2+\sinh(2z)/4,\qquad
\psi(p)=\tanh(F^{-1}(p)),
\]

let \(p_a=F(z_a^{(1)})\), so \(h_a=\psi(p_a)\). The fixed driver is an absolutely continuous path \(b:[0,S]\to\mathbb R^m\) with \(b(0)=0\), \(0<S\le1\), and \(\sum_a|b_a'(u)|\le1\) almost everywhere. The controlled equations are

\[
\begin{aligned}
 dp_a&=k_a\,db_a,&
 dw&=\sum_a h_a^{(2)}\,db_a,&
 dW&=\frac1n\sum_a\delta_a^{(2)}h_a^\top\,db_a,\\
 h_a&=\psi(p_a),& z_a^{(2)}&=Wh_a,&
 h_a^{(2)}&=\tanh(z_a^{(2)}),\\
 \delta_a^{(2)}&=w\odot\operatorname{sech}^2(z_a^{(2)}),&
 k_a&=W^\top\delta_a^{(2)},& f_a^b&=w^\top h_a^{(2)}/n.
\end{aligned}
\tag{1}
\]

The initialized matrix has independent \(N(0,1/n)\) entries, and \(w(0)=0\). Since the training inputs are orthonormal, the initial first-layer preactivation array \(Z_0=(z_{a,i}^{(1)}(0))_{i,a}\) has independent standard normal entries and is independent of \(W_0\). Let \(H_0=\tanh(Z_0)\).

**Finite fluctuation proposition.** For each fixed deterministic driver \(b\), each training sample \(a\), and every width,

\[
\mathbb E\sup_{0\le u\le S}
 |f_{n,a}^b(u)-\mathbb E f_{n,a}^b(u)|^2
\le \frac{CS^2}{n}.
\tag{2}
\]

The constant is uniform over deterministic drivers in this class. This means \(\sup_b\mathbb E\sup_u|f^b-\mathbb Ef^b|^2\le CS^2/n\); it does **not** put \(\sup_b\) inside the expectation. A fixed finite list of drivers or outputs is handled by summing their bounds. No claim concerning the population bias is part of (2).

The proof uses the exact activity derivative of a prediction. Its Gaussian variance can be bounded without using a coordinate maximum of the carriers. Integrating that centered derivative controls the whole activity interval without a time grid.

## 2. An operator projection used only in the proof

Let \(G\) have independent standard normal entries, so \(W_0=G/\sqrt n\). Choose a fixed sufficiently large \(K\), and let \(\Pi_K\) be Euclidean projection, in the Frobenius inner product, onto the convex set of matrices of operator norm at most \(K\). This projection is nonexpansive in Frobenius norm. Indeed its minimizing property gives

\[
\langle A-\Pi_K A,\Pi_K B-\Pi_K A\rangle_F\le0,
\]

and the corresponding inequality with \(A,B\) interchanged; addition gives
\(\|\Pi_K A-\Pi_K B\|_F^2\le\langle\Pi_K A-\Pi_K B,A-B\rangle_F\).

Temporarily initialize (1) at \(\Pi_K(G/\sqrt n)\), and put a superscript \(\Pi\) on the resulting quantities. The operator bound, readout bound, and transformed-field Lipschitz estimates from the tail note then hold for every initialization:

\[
\|w^\Pi(u)\|_\infty\le S,\qquad
\|W^\Pi(u)\|_{\rm op}\le K+S^2,\qquad
\frac{\|k_a^\Pi(u)\|_2}{\sqrt n}\le CS.
\tag{3}
\]

The projection changes nothing on \(E_n=\{\|G/\sqrt n\|_{\rm op}\le K\}\). The elementary Gaussian net bound in the manuscript gives

\[
\Pr(E_n^c)\le 2\,9^{2n}e^{-nK^2/8}\le Ce^{-cn}
\tag{4}
\]

for sufficiently large \(K\).

The tail note's control-path argument holds **conditionally on every deterministic first-layer initialization**, without a Gram assumption: its cavity conditioning already freezes that initialization. On \(E_n\), it gives uniform coordinate exponential moments for the supremum over all controls. Off \(E_n\), (3) gives the crude bound \(\sup_{b,u}|k_{a,i}^{\Pi,b}(u)|\le CS\sqrt n\). Consequently, for fixed \(p<\infty\), uniformly over deterministic initial arrays \(H_0\in(-1,1)^{n\times m}\),

\[
\mathbb E_G\sup_{u\le S}\frac1n\sum_i|k_{a,i}^{\Pi,b}(u)|^4\le C S^4,
\qquad
\mathbb E_G\exp\left\{p\sup_{b,u}|p_{a,i}^{\Pi,b}(u)-p_{a,i}(0)|\right\}\le C_p.
\tag{5}
\]

For the second assertion, \(|p_{a,i}(u)-p_{a,i}(0)|\le S\sup_{b,u}|k_{a,i}(u)|\). On \(E_n\), the carrier's square-exponential moment implies every displayed linear-exponential moment. Off \(E_n\), the expectation is at most \(Ce^{-cn+Cp\sqrt n}\), uniformly bounded in \(n\). For the first assertion, the bad-event contribution is at most \(CnS^4e^{-cn}\). These arguments do not declare the projected matrix Gaussian; Gaussian conditioning is used only where projection leaves the original matrix unchanged.

## 3. Exact prediction derivative and its matrix-initialization variance

For each state of (1), define the symmetric matrix

\[
\Lambda_{ab}=
 \frac{h_a^{(2)\top}h_b^{(2)}}n
 +\frac{\delta_a^{(2)\top}\delta_b^{(2)}}n
       \frac{h_a^\top h_b}n
 +\mathbf 1_{a=b}\frac1n\sum_i\psi'(p_{a,i})k_{a,i}^2.
\tag{6}
\]

This is \(m\) times the manuscript's tangent Gram for orthonormal inputs. To check the last term, only \(p_b\) changes under \(db_b\), and
\(\partial f_a/\partial p_a=\psi'(p_a)\odot k_a/n\). Also
\(\psi'(p_a)=\operatorname{sech}^4(z_a^{(1)})=\phi_1'(z_a^{(1)})^2\).
The readout and matrix variations give the first and second terms. Therefore

\[
\frac{d}{du}f_a^b(u)=\sum_b b_b'(u)\Lambda_{ab}(u)
\quad\text{for almost every }u.
\tag{7}
\]

All entries of \(\Lambda^\Pi\) are bounded by a deterministic constant, by (3), so differentiation can later pass through expectations by dominated integration.

At fixed initial first-layer coordinates, variation of the initialized matrix propagates through the transformed Lipschitz vector field with

\[
\sum_a\frac{\|\Delta p_a(u)\|_2}{\sqrt n}
 +\frac{\|\Delta w(u)\|_2}{\sqrt n}
 +\|\Delta W(u)\|_F
\le C\|\Delta W_0\|_F.
\tag{8}
\]

This follows from the common-driver Gronwall estimate with a nonzero initial matrix difference. It applies to first variations and to differences of two trajectories initialized inside the operator ball.

For a state variation, denote the sum on the left of (8) by \(D_X\). Forward and top-backward subtraction gives RMS feature, top-backward and carrier variations at most \(CD_X\). The only new term in differentiating (6) is

\[
\frac1n\sum_i\psi''(p_{a,i})\Delta p_{a,i}k_{a,i}^2.
\]

Since \(|\psi''|\le4\), Cauchy--Schwarz bounds it by
\(4(\|\Delta p_a\|_2/\sqrt n)(n^{-1}\sum_i k_{a,i}^4)^{1/2}\).
The variation of the squared carrier is bounded using its RMS bound and the RMS carrier variation. The other two products in (6) have bounded factors. Thus

\[
|D\Lambda_{ab}[\Delta X]|
\le C\left[1+\left(\frac1n\sum_i k_{a,i}^4\right)^{1/2}\right]D_X.
\tag{9}
\]

Combining (8)--(9) and the \(1/\sqrt n\)-Lipschitz initialization map \(G\mapsto\Pi_K(G/\sqrt n)\) gives, at its almost-everywhere differentiability points,

\[
\|\nabla_G\Lambda_{ab}^{\Pi}(u)\|_F^2
\le\frac Cn\left(1+\frac1n\sum_i|k_{a,i}^{\Pi}(u)|^4\right).
\tag{10}
\]

Local Lipschitz continuity supplies weak derivatives and justifies this inequality at almost every Gaussian input even though the operator projection need not be differentiable everywhere.

For a function \(A\) of independent standard Gaussians with a square-integrable weak gradient, Gaussian Poincare says
\(\operatorname{Var}(A)\le\mathbb E\|\nabla A\|_2^2\).
One verification differentiates
\(\mathbb E[A(G)A(\sqrt tG+\sqrt{1-t}G')]\), with \(G'\) independent, integrates by parts, bounds its derivative by
\(\mathbb E\|\nabla A\|_2^2/(2\sqrt t)\), and integrates from zero to one. Smooth approximation extends the calculation to weak gradients.
Equations (5), (10), and this inequality give

\[
\operatorname{Var}_G(\Lambda_{ab}^{\Pi}(u)\mid H_0)\le C/n,
\tag{11}
\]

uniformly over deterministic initial feature arrays. Because \(\sum_b|b_b'|\le1\), the same estimate applies to the right side of (7).

## 4. First-layer randomness: only the averaged map becomes Lipschitz

A pathwise operator Lipschitz estimate with \(\max_i e^{C|p_i-p_i(0)|}\) would lose a width factor. We do not use such an estimate. Instead we fix two deterministic initial feature arrays and take the matrix expectation before claiming Lipschitz continuity.

For \(-1<h<1\), define

\[
T(h)=F(\operatorname{artanh}h),\qquad
J(h,u)=\psi(T(h)+u).
\]

Since \(\psi(T(h))=h\),

\[
\partial_hJ(h,u)=\frac{\psi'(T(h)+u)}{\psi'(T(h))}.
\]

Moreover \(|(\log\psi')'(p)|=4|\tanh(F^{-1}(p))|\operatorname{sech}^2(F^{-1}(p))\le4\). Hence

\[
|\partial_hJ(h,u)|\le e^{4|u|},\qquad
|\partial_uJ(h,u)|\le1.
\tag{12}
\]

Let \(H_0,H_0'\) be two fixed arrays in \((-1,1)^{n\times m}\), and couple their projected controlled flows using the same matrix initialization. Write \(u_a=p_a-p_a(0)\) and \(u_a'=p_a'-p_a'(0)\). In particular their increment coordinates agree initially at zero, regardless of how large \(T(H_0)\) is. Equation (12) gives the pointwise bound

\[
|h_{a,i}-h_{a,i}'|
\le e^{4|u_{a,i}|}|H_{0,ia}-H_{0,ia}'|+|u_{a,i}-u_{a,i}'|.
\tag{13}
\]

Define the random forcing size

\[
R=\sum_a\left[\frac1n\sum_i
 e^{8\sup_{u\le S}|u_{a,i}(u)|}
 |H_{0,ia}-H_{0,ia}'|^2\right]^{1/2}.
\]

The root differences inside this sum are deterministic while averaging over \(G\). For \(p\ge2\), Minkowski's inequality in \(L^{p/2}\), followed by (5), therefore yields

\[
\|R\|_{L^p(G)}
\le C_p\sum_a\frac{\|H_{0,a}-H_{0,a}'\|_2}{\sqrt n}
\le C_p\frac{\|H_0-H_0'\|_F}{\sqrt n}.
\tag{14}
\]

This is an expectation estimate for each fixed perturbation; it does not bound a random multiplication operator by the average of its diagonal entries.

Subtract the increment-state equations, measuring the sum of RMS \(u_a-u_a'\), RMS \(w-w'\), and Frobenius \(W-W'\). The same rank-one and operator estimates used in the tail proof, now with the extra feature forcing in (13), give

\[
\sup_{u\le S}D_{\rm inc}(u)\le CS e^{CS}R.
\tag{15}
\]

In detail, the top-feature difference is bounded by the sum of the matrix difference and first-feature difference; the top-backward difference additionally uses \(\|w\|_\infty\le S\); the carrier difference uses a bounded matrix and bounded backward RMS; and the matrix update is a rank-one product. Each controlled vector-field difference is thus at most \(C(D_{\rm inc}+R)\). Integrating against driver variation at most \(S\), with zero initial increment-state difference, proves (15).

It follows from (13)--(15) that the RMS differences of all first and second features and all carriers have \(L^p(G)\) norm at most \(C_p\|H_0-H_0'\|_F/\sqrt n\).

To compare (6), write its last term as
\(n^{-1}\sum_i (1-h_{a,i}^2)^2k_{a,i}^2\).
The coefficient is bounded and has bounded derivative on \([-1,1]\). Its difference is therefore bounded by

\[
C\frac{\|h_a-h_a'\|_2}{\sqrt n}
 \left(\frac1n\sum_i k_{a,i}^4\right)^{1/2}
+C\frac{\|k_a-k_a'\|_2}{\sqrt n}.
\tag{16}
\]

The first two products in (6) have the simpler RMS difference bounds. Taking expectations in (16), Cauchy--Schwarz uses (5) for the fourth carrier moment and (14)--(15) for the squared feature difference. The result is the deterministic inequality

\[
\left|\mathbb E_G\Lambda_{ab}^{\Pi,b}(u;H_0)
       -\mathbb E_G\Lambda_{ab}^{\Pi,b}(u;H_0')\right|
\le C\frac{\|H_0-H_0'\|_F}{\sqrt n}.
\tag{17}
\]

Thus the **matrix-averaged** Gram map is Lipschitz in initial feature RMS. The map \(Z_0\mapsto\tanh(Z_0)\) is 1-Lipschitz in ordinary Frobenius norm, so another Gaussian Poincare application gives

\[
\operatorname{Var}_{Z_0}\bigl(\mathbb E_G[\Lambda_{ab}^{\Pi,b}(u)\mid Z_0]\bigr)
\le C/n.
\tag{18}
\]

The law of total variance combines (11) and (18). For the deterministic linear combination in (7), it yields

\[
\operatorname{Var}\left(\frac d{du}f_{n,a}^{\Pi,b}(u)\right)\le C/n
\quad\text{for almost every }u.
\tag{19}
\]

## 5. Uniform activity-time fluctuation and projection removal

Let \(g(u)=f_{n,a}^{\Pi,b}(u)-\mathbb Ef_{n,a}^{\Pi,b}(u)\). Its initial value is zero. Its absolute continuity and the deterministic bound on (7) imply

\[
\sup_{u\le S}|g(u)|^2\le S\int_0^S|g'(u)|^2\,du.
\]

Taking expectations and using (19) proves

\[
\mathbb E\sup_{u\le S}|f_{n,a}^{\Pi,b}(u)-\mathbb Ef_{n,a}^{\Pi,b}(u)|^2
\le CS^2/n.
\tag{20}
\]

There is no logarithmic time-grid loss. The derivative need not be Lipschitz in time; its centered squared integral is what enters this elementary inequality.

Both projected and original controlled outputs satisfy \(|f_a^b(u)|\le S\), since the readout coordinates are bounded by \(S\) and the top features by one. They coincide on \(E_n\). Therefore

\[
\mathbb E\sup_u|f_{n,a}^{\Pi,b}(u)-f_{n,a}^b(u)|^2\le CS^2e^{-cn},
\quad
\sup_u|\mathbb Ef_{n,a}^{\Pi,b}(u)-\mathbb Ef_{n,a}^b(u)|\le CSe^{-cn}.
\]

Combining these with (20), and absorbing \(e^{-cn}\le C/n\), proves (2) for the original finite controlled network.

For one training sample with \(y\ne0\), the actual residual retains its initial sign because \(\dot r=-2\Gamma r\). Its activity-parametrized driver is therefore the deterministic path \(b(u)=\operatorname{sign}(y)u\). On the manuscript's fitting event, its total driver variation is at most \(2Y/\kappa\); choose \(S\) at least that large, still at most one. Then the deterministic-control curve covered by (2) contains the entire actual training trajectory on that event. The bound (2) itself is an unconditional statement about the prescribed-control curve, not a conditional variance estimate given the fitting event. Physical time uses a random time change determined by that same curve. A stable scalar clock comparison would transfer a curve estimate to physical time once the reference curve and its fitting gap are identified; it would still leave the population-bias issue below. For \(y=0\), the actual initialized training flow is stationary.

## 6. Why strict finite-to-population convergence remains unproved

For a fixed driver, let \(\overline f_n^b(u)=\mathbb Ef_n^b(u)\), and let \(f_\infty^b(u)\) denote its population counterpart if constructed with that deterministic control. The fluctuation theorem says nothing quantitative about

\[
\sup_{u\le S}|\overline f_n^b(u)-f_\infty^b(u)|.
\tag{21}
\]

The available qualitative finite-program convergence may identify the limit of \(\overline f_n^b\), but neither it nor (2) supplies a numerical rate for (21). For example, as a matter of logic, a deterministic bias \(n^{-1/4}\) is compatible with vanishing bias and variance \(O(1/n)\). This is not a counterexample inside the neural model; it shows why fluctuation control cannot discharge the bias obligation.

The exact obstruction within the present cavity decomposition is visible before any limit. For a deleted column \(i\), the tail proof writes

\[
k_{a,i}^b=W_{0,i}^\top\delta_a^{(2),-i,b}+R_{a,i}^b,
\qquad |R_{a,i}^b|\le CS.
\tag{22}
\]

The leading Gaussian term is centered conditionally on the cavity, but the reaction \(R\) is of order one at fixed labels. It contains the population response/Onsager contribution. It cannot be discarded as a width error. The first-return calculation in `WIDTH_ROUTE.md` already shows an explicit nonzero response mean of this kind.

To identify (22) quantitatively, one would need to linearize the cavity's response to the deleted neuron's entire feedback history, identify the resulting quadratic Gaussian contraction with the population response kernel, and bound both its random fluctuation and nonlinear remainder uniformly over the activity interval. The present normalized \(L^2\) cavity estimate gives an unnormalized \(O(1)\) response vector. It alone does not make a coordinatewise quadratic Taylor remainder small: an \(L^2\)-bounded vector may concentrate its mass on a few coordinates. A suitable response-delocalization estimate, coupled to the finite response-kernel consistency estimate, has not been proved here.

There is an additional control-selection issue for \(m>1\). The actual integrated residual history is random. The finite tail proof handled this by a conditional Gaussian supremum over a deterministic control class. The nonlinear centered predictor in (2) is not that Gaussian process. Uniform constants for each fixed control do not license substitution of the random actual control. A uniform empirical-process estimate or an all-time comparison against a deterministic population residual path is needed. The latter still requires the bias estimate and suitable damped stability.

Accordingly, this continuation proves cap-independent root-width **finite fluctuations for prescribed controls** and isolates the remaining mean/response problem. It does not prove the all-time whole-input finite-to-population bound, even for one training sample. No strict root-width population conclusion is claimed.
