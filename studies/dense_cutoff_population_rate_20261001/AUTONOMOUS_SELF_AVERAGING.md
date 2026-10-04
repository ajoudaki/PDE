# Unconditional root-width concentration of the entire autonomous prediction

This consequence does not assume the local profile contrast H. It concerns the actual unclipped dense flow (1) in ROOT_WIDTH_CONDITIONAL_THEOREM.md: two tanh layers, orthonormal fixed training inputs, Gaussian initialization, zero readout, a positive limiting initial feature-Gram gap, sufficiently small fixed labels, and queries in a fixed bounded ball. All constants below may depend on these fixed quantities. This is a statement about fluctuations, not a population-bias theorem.

## 1. Statement

For every sufficiently large \(n\), there is a deterministic predictor \(\bar f_n(t,x)\), defined below solely from width-\(n\) networks. For each fixed confidence \(1-\delta\), and all sufficiently large \(n\) depending on \(\delta\),
\[
\Pr\{\mathcal E_\mu(f_n,\bar f_n)\le C_\delta/\sqrt n\}\ge1-\delta.
\tag{1}
\]
Here \(f_n\) is the actual autonomous dense predictor, and
\(\mathcal E_\mu(f,g)^2=\int\sup_{t\ge0}|f(t,x)-g(t,x)|^2d\mu(x)\).
The constant is independent of width and elapsed time. Thus two independent actual runs \(f_n,f_n'\) satisfy
\[
\Pr\{\mathcal E_\mu(f_n,f_n')\le C_\delta/\sqrt n\}\ge1-\delta.
\tag{2}
\]
The deterministic center \(\bar f_n\) is not declared equal to the population predictor, or to the expectation of the actual autonomous predictor. Its definition and convergence to the population are proved below. Its quantitative population bias remains open without H.

## 2. A deterministic reference defined at the same finite width

Fix an operator cutoff \(K\) sufficiently large that
\(\Pr(\|W_0\|_{\mathrm{op}}>K)\le Ce^{-cn}\). Let \(W_0^\Pi\) be its Frobenius projection onto the operator ball of radius \(K\). This initialization modification is used only to define the deterministic center. No backward signal or trajectory is clipped.

For each deterministic control \(b\), let \(f_{n,\Pi}^b\) be the controlled network with initialized matrix \(W_0^\Pi\), and all other initialization canonical. Define a deterministic common residual path and predictor by
\[
\bar f_n(t,x)=\mathbb E f_{n,\Pi}^{\bar b_n}(t,x),\qquad
\dot{\bar b}_{n,a}=-\frac2m[\bar f_n(t,x_a)-y_a],\qquad \bar b_n(0)=0.
\tag{3}
\]
Every member inside the expectation is driven by the same deterministic path. Its own residual is not used. This avoids confusing an average of autonomously trained networks with (3).

Existence locally in physical time follows from a Volterra Picard argument: the controlled forward map is uniformly Lipschitz in the uniform integrated-control distance on a tube of bounded total variation, by CONTROLLED_FEEDBACK_STABILITY.md. Composing this map with integration of the residual makes the Picard map contractive on sufficiently short time intervals. Choose the control tube and the interval so that its variation bound is preserved. The same argument extends from any existing history, because the control-map estimates are uniform on the tube. The following estimate prevents exiting a sufficiently small tube and gives global existence.

## 3. The reference fits with uniformly bounded activity

Put \(\bar r=\bar f_n(X)-y\), \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\), and \(g(X)=[g(x_1),\ldots,g(x_m)]\). Let \(\bar Q_{0,n}=\mathbb E[g_0(X)^\top g_0(X)/n]\) for the projected initialization. Initial qualitative convergence and the exponentially unlikely projection imply, for sufficiently large \(n\),
\[
\bar Q_{0,n}/m\succeq2\lambda I_m
\tag{4}
\]
for a fixed \(\lambda>0\) below half the limiting gap. The initial features are bounded, so expectation convergence needs no further moment assumption.

For each initialized controlled member let \(\Lambda^b(X,X)\) be its training tangent matrix. Direct differentiation gives
\[
\Lambda^b_{ab}
=\frac{g_a^\top g_b}{n}
 +\frac{\delta_a^\top\delta_b}{n}\frac{h_a^\top h_b}{n}
 +(v_a^\top v_b)\frac{(s_a\odot k_a)^\top(s_b\odot k_b)}n,
\tag{5}
\]
where \(v_a=x_a/\sqrt d\), \(s_a=1-h_a^2\), and \(k_a=W^\top\delta_a\). Each summand is positive semidefinite: the second and third are Gram matrices of the corresponding tensor-product parameter gradients. In particular \(\Lambda^b\succeq g(X)^\top g(X)/n\).

On every projected controlled trajectory of total variation at most \(S\le1\), the deterministic hidden displacement estimate gives
\[
\left\|\frac{g(X)^\top g(X)-g_0(X)^\top g_0(X)}{mn}\right\|_{\mathrm{op}}
\le CS^2.
\tag{6}
\]
Choose \(S>0\) so small that \(CS^2\le\lambda\). All constants are uniform over initialization because the initial operator norm is bounded by \(K\). For such paths, (4)--(6) show
\(\mathbb E\Lambda^b/m\succeq\lambda I_m\).

The deterministic matrix bound also justifies differentiating the expectation in (3) along physical time. Equations (3) and (5) give exactly
\[
\dot{\bar r}=-\frac2m\mathbb E\Lambda^{\bar b_n}\bar r.
\]
Consequently its residual RMS obeys \(\bar\rho(t)\le Y e^{-2\lambda t}\) as long as total variation remains below \(S\). Also
\[
\sum_a\int_0^t|d\bar b_{n,a}|
\le2\int_0^t\bar\rho(s)\,ds\le Y/\lambda.
\tag{7}
\]
Reduce the fixed label bound so that \(Y/\lambda<S/2\). A first-exit argument precludes exit from the tube. This proves global existence, exponential fitting, bounded activity, and convergence of the controlled states/predictor as \(t\to\infty\). The same small \(S\) can meet the absorption requirement in CONTROLLED_FEEDBACK_STABILITY.md for the actual finite flow on its fitting event. These are width-independent small-label restrictions.

## 4. Root-width comparison with actual training

Let \(\eta_n=f_n^{\bar b_n}-\bar f_n\), where the finite network on the left uses the original unprojected Gaussian initialization and the deterministic driver from (3). By PASSIVE_QUERY_FLUCTUATIONS.md, the original controlled prediction fluctuates around its mean with squared whole-time error at most \(C/n\). The difference between its mean and the center in (3) is at most
\[
\sup_t|\mathbb E f_n^{\bar b_n}(t,x)-\mathbb E f_{n,\Pi}^{\bar b_n}(t,x)|
\le2S\Pr(\|W_0\|_{\mathrm{op}}>K)\le CSe^{-cn}.
\tag{8}
\]
Indeed the original and projected systems coincide on the operator event, and both predictions are bounded by \(S\). This bound is uniform in the query; it includes the time supremum. Reparametrizing the deterministic driver by its total variation is legitimate. Therefore
\[
\mathbb E\int\sup_t|\eta_n(t,x)|^2d\mu(x)
+\sum_a\mathbb E\sup_t|\eta_n(t,x_a)|^2\le C/n.
\tag{9}
\]
Here the center is a finite expectation by definition; no population-bias comparison has been invoked.

On the actual fitting/operator/initial-Gram event \(G_n\), apply the deterministic same-time feedback theorem with reference \(f_* =\bar f_n\). Equations (3) and (7) verify its residual-control and activity hypotheses. It gives
\[
\mathcal E_\mu(f_n,\bar f_n)
\le C_B\max_a\sup_t|\eta_n(t,x_a)|+\mathcal E_\mu(f_n^{\bar b_n},\bar f_n).
\]
Thus \(\mathbb E[\mathbf1_{G_n}\mathcal E_\mu(f_n,\bar f_n)^2]\le C/n\). Since \(\Pr(G_n)\to1\), the same fixed-confidence Markov argument as in ROOT_WIDTH_CONDITIONAL_THEOREM.md proves (1). The triangle inequality and a union bound at confidence \(1-\delta/2\) for each run prove (2). No independence is actually needed for that union bound, though independent runs are the natural interpretation.

## 5. What this says, and what it does not

The manuscript's qualitative actual population convergence and (1) identify
\(\mathcal E_\mu(\bar f_n,f_\infty)\to0\). To justify the deterministic conclusion explicitly, the triangle inequality bounds this deterministic distance by the sum of two random distances tending to zero in probability; if the deterministic distance failed to vanish along a subsequence, that inequality would be impossible with probability tending to one.

For every fixed width, however, \(\bar f_n\) may have a systematic bias relative to \(f_\infty\). No rate for that bias follows from (1). In particular a hypothetical deterministic \(n^{-1/4}\) displacement remains logically possible. The local profile criterion H supplies a separate way to exclude it.

What (1)--(2) rule out in this structured regime is a slower-than-root rate caused solely by an increasing spread of whole prediction trajectories across initialization. The remaining possible obstruction is a common finite-width displacement. This separates two mathematically different mechanisms of poor population approximation without declaring either one absent by assumption.
