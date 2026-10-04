# Closing adaptive residual feedback through the integrated control

This is a new deterministic theorem for the actual dense network, in the two-tanh-layer, orthonormal-training-input setting of FINITE_TAIL_ROUTE.md. It turns an error for one deterministic residual history into an error for actual autonomous training, uniformly over physical time and passive inputs. It does not assume a maximum bound on individual backward carriers.

## 1. Model and controlled trajectories

Let \(v_a=x_a/\sqrt d\) satisfy \(v_a^\top v_b=\mathbf1_{a=b}\). The two-hidden-layer dense model is
\[
h(x)=\tanh(Ax/\sqrt d),\quad g(x)=\tanh(Wh(x)),\quad
f(x)=w^\top g(x)/n.
\]
Initialization is \(A_{0,ij}\sim N(0,1)\), \(W_{0,ij}\sim N(0,1/n)\), independently, and \(w_0=0\). For this deterministic result it suffices to fix any \(A_0\) and \(\|W_0\|_{\rm op}\le K\). For training samples write \(h_a,g_a\), and
\[
\delta_a=w\odot(1-g_a^2),\quad k_a=W^\top\delta_a,\quad
F(z)=z/2+\sinh(2z)/4,\quad p_a=F(Av_a),\quad
\psi=\tanh\circ F^{-1}.
\]
The exact dense equations under an externally prescribed integrated residual path \(b=(b_a)_{a=1}^m\) are
\[
dp_a=k_a\,db_a,\qquad dw=\sum_a g_a\,db_a,\qquad
dW=\frac1n\sum_a\delta_a h_a^\top\,db_a,\qquad h_a=\psi(p_a).
\tag{1}
\]
The original autonomous flow is recovered by
\[
db_a(t)=-\frac2m(f(t,x_a)-y_a)\,dt.
\tag{2}
\]
All controls start at zero, are absolutely continuous, and have total variation
\(\sum_a\int|db_a|\le S\le1\). They may be parametrized by physical time on any interval \([0,T]\). Constants below do not depend on \(n,T\), or the speed of traversal of a control. They may depend on \(m,K\) and a fixed query radius \(B\).

The already reconstructed controlled estimates give
\[
\|w\|_\infty\le S,\quad
\|W-W_0\|_F\le S^2,\quad
\frac{\|k_a\|_2}{\sqrt n}\le CS.
\tag{3}
\]
For two controls \(b,c\) from the same initialization, set
\[
\epsilon_T=\max_a\sup_{t\le T}|b_a(t)-c_a(t)|.
\]
The full controlled-state distance satisfies
\[
\sup_{t\le T}\left(
\sum_a\frac{\|p_a^b-p_a^c\|_2}{\sqrt n}
+\frac{\|w^b-w^c\|_2}{\sqrt n}
+\|W^b-W^c\|_F\right)\le C\epsilon_T.
\tag{4}
\]
This follows by integration by parts in the integrated driver and Gronwall against its total variation, as proved in Section 3 of FINITE_TAIL_ROUTE.md. That proof applies to any common time interval, not only unit-speed activity controls.

## 2. A sharper nonlinear remainder

Define the initial feature pairings
\[
Q_{0,ab}=\frac{g_a(0)^\top g_b(0)}n,\qquad
Q_0(x,a)=\frac{g(x,0)^\top g_a(0)}n.
\]
For every controlled path there is the exact decomposition
\[
f^b(t,x)=\sum_a Q_0(x,a)b_a(t)+R^b(t,x).
\tag{5}
\]
For all queries \(\|x\|/\sqrt d\le B\),
\[
\sup_{t\le T}|R^b(t,x)-R^c(t,x)|
\le C_B S^2\epsilon_T,\qquad
\sup_{t\le T}|R^b(t,x)|\le C_B S^3.
\tag{6}
\]
No Gaussian averaging is used in (6).

### Proof

By (1)–(3), the displacement and total variation of each hidden block, measured in first-coordinate RMS and hidden-matrix Frobenius norm, are \(O(S^2)\). The readout has total variation \(O(S)\) in RMS. The hidden components of each control vector field in (1) have norm \(O(S)\) and are uniformly Lipschitz on the tube (3). Their total variation along any controlled state path is therefore \(O(S)\).

For the difference of hidden blocks, subtract their equations using driver \(b\), and integrate the driver-difference term by parts. The difference of hidden vector fields is at most \(C\) times the full state difference in (4). Its integral has norm at most \(CS\epsilon_T\). The integration-by-parts term is bounded by \(\epsilon_T\) times the hidden vector field's endpoint norm plus its total variation, hence also \(CS\epsilon_T\). Consequently
\[
\sup_{t\le T}\left(
\sum_a\frac{\|p_a^b-p_a^c\|_2}{\sqrt n}
+\|W^b-W^c\|_F\right)\le CS\epsilon_T.
\tag{7}
\]

To include a passive query put \(c_a(x)=v_a^\top(x/\sqrt d)\), and
\(v_\perp=x/\sqrt d-\sum_a c_a(x)v_a\). Since the first-layer update lies in the training input span,
\[
z^{(1),b}(t,x)=A_0v_\perp+\sum_a c_a(x)F^{-1}(p_a^b(t)).
\tag{8}
\]
The map \(F^{-1}\) is 1-Lipschitz, and \(\sum_a|c_a(x)|\le\sqrt m B\). Bounded activation derivatives, (7), and the matrix operator bound show
\[
\sup_t\frac{\|g^b(t,x)-g^c(t,x)\|_2}{\sqrt n}
\le C_B S\epsilon_T.
\tag{9}
\]
The feature displacement from initialization and total variation along either path are \(O_B(S^2)\) by the same forward estimates.

Separate the readout into
\[
w^b(t)=\sum_a g_a(0)b_a(t)+e_w^b(t),\qquad
e_w^b(t)=\sum_a\int_0^t(g_a^b(s)-g_a(0))\,db_a(s).
\]
Then \(\|e_w^b\|_2/\sqrt n\le CS^3\). To compare two such remainders, the integrand difference against \(db\) has norm at most \(CS\epsilon_T\), integrated over variation \(S\). The remaining integral against \(d(b-c)\), after integration by parts, is bounded by \(\epsilon_T\) times feature displacement plus total variation, both \(O(S^2)\). Hence
\[
\sup_t\frac{\|e_w^b(t)-e_w^c(t)\|_2}{\sqrt n}
\le CS^2\epsilon_T.
\tag{10}
\]
Finally write the remainder in (5) as
\[
R^b(t,x)=\frac{e_w^b(t)^\top g(x,0)}n
 +\frac{w^b(t)^\top(g^b(t,x)-g(x,0))}n.
\]
Use (3), (4), (9), (10) and feature displacement \(O_B(S^2)\) in the two-product subtraction. This proves (6). It is a Lipschitz remainder estimate, not just a bound on each remainder separately. \(\square\)

## 3. Deterministic removal of adaptive residual selection

Suppose \(Q_0/m\succeq\lambda I_m\). Let \(f_*(t,x)\) be any deterministic reference predictor with \(f_*(0,x)=0\), training residual \(r_*=f_*(X)-y\), and control
\[
b_{*,a}(t)=-\frac2m\int_0^t r_{*,a}(s)\,ds.
\]
Assume that both this control and the actual finite-network control have total variation at most \(S\). Run the same finite initialized network under \(b_*\), obtaining \(f_n^{b_*}\), and define its reference error
\[
\eta_n(t,x)=f_n^{b_*}(t,x)-f_*(t,x).
\tag{11}
\]
For sufficiently small \(S\), depending on \(m,K,\lambda\) but not on width, time, or query,
\[
\max_a\sup_{t\ge0}|b_{n,a}(t)-b_{*,a}(t)|
\le C\max_a\sup_{t\ge0}|\eta_n(t,x_a)|.
\tag{12}
\]
For any query law \(\mu\) supported in \(\|x\|/\sqrt d\le B\),
\[
\mathcal E_\mu(f_n,f_*)
\le C_B\max_a\sup_t|\eta_n(t,x_a)|
 +\left(\int\sup_t|\eta_n(t,x)|^2\,d\mu(x)\right)^{1/2}.
\tag{13}
\]

### Proof

Put \(e=b_n-b_*\). Equations (2), (5), and (11), at the training inputs, give exactly
\[
\dot e=-\frac2mQ_0e-\frac2m\{R^{b_n}-R^{b_*}+\eta_n(X)\},
\qquad e(0)=0.
\]
For finite \(T\), the variation-of-constants formula and
\(\|\exp(-2Q_0t/m)\|_{\rm op}\le e^{-2\lambda t}\) bound the Euclidean supremum of \(e\) by
\[
\sup_{t\le T}\|e(t)\|_2
\le C S^2\sup_{t\le T}\|e(t)\|_2
 +C\max_a\sup_{t\le T}|\eta_n(t,x_a)|.
\]
Here (6) supplies the first term, and the exponential kernel has finite \(L^1\) norm \(1/(2\lambda)\). Choose \(S\) with its displayed coefficient at most \(1/2\), absorb, and let \(T\to\infty\). This proves (12). Equation (5), \(|Q_0(x,a)|\le1\), and (6) then bound
\(|f_n^{b_n}(t,x)-f_n^{b_*}(t,x)|\le C_B\sup_{s\le t}\|e(s)\|_2\).
The triangle inequality proves (13). \(\square\)

This is a same-physical-time estimate. It does not compare points at matched loss. Its exponentially damped linear part is the actual initialized Gram; the feature-learning remainder is retained, not discarded.

## 4. What this closes

Apply the theorem with \(f_*=f_\infty\), the manuscript's deterministic dense population predictor. The finite and population fitting statements give total variation at most \(2Y/\kappa\). Reducing the fixed small-label threshold makes this \(S\) meet the absorption condition. The initialized Gram and operator hypotheses hold on an event whose probability tends to one.

Thus, in this structured nonlinear setting, a population-centered root-width estimate for the finite network driven by the single deterministic population residual history implies the full autonomous, all-time, whole-query root-width estimate. The theorem does not require a uniform stochastic supremum over all controls and does not replace a random control in a pointwise probabilistic bound.

Qualitative identification of the controlled limit can also be obtained without a new population construction. The manuscript's qualitative convergence of actual training predictions, together with the exponential residual tails, gives
\(\sup_t\|b_n(t)-b_*(t)\|\to0\) in probability: integrate up to fixed \(T\), then control the two tails and let \(T\to\infty\). The deterministic control comparison (4) and (8) makes the controlled and actual finite predictions approach each other, uniformly on the bounded query domain on the fitting/operator event. Separately, the manuscript's actual passive-query convergence identifies the limit of the latter with \(f_\infty\). Combining both statements proves \(f_n^{b_*}\to f_\infty\) in the all-time query metric. The probability of the complementary event vanishes. Since any prescribed control has \(|f_n^{b_*}|\le S\), and its limiting population prediction has the same bound, convergence in probability plus boundedness identifies its limiting mean also in this integrated query norm. It supplies no rate on that mean by itself.

No cutoff, numerical experiment, or dense-reference approximation is involved in this theorem. The remaining stochastic input is the finite controlled prediction error, including its expectation bias. PASSIVE_QUERY_FLUCTUATIONS.md addresses the fluctuation part; DECISIVE_CONDITIONAL_ROUTE.md addresses a local finite-network route to the bias part.
