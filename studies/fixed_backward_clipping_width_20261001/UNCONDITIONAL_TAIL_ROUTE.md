# Unconditional initialization tails: exact energy and the all-time gap

2026-10-01. Scoped theoretical route. This report proves stronger finite-horizon tail control, but neither proves the requested unconditional all-time mean-square estimate nor gives an admissible counterexample to it. It does not assume fitting outside the initialized good event.

The full assigned FITTING_AND_THRESHOLD.md, CONCENTRATION_ROUTE.md, and CLIPPED_POPULATION_ROUTE.md were read. The exact readout energy below was also checked against the complete “Globally bounded activations” passage in current paper/main.tex. Required solve-math-rigorously and investigate-conjectures skills and their contract/adversarial references were read. No other study, sibling new route, archive, experiment, Git history, or manuscript edit was used.

## 1. Contract and conclusion

The dynamics are precisely the assigned two-hidden-layer tanh, q=1 closure, with fixed positive recursive post-gate hard clipping \(C_M\), including \(M=1\). Initial first rows are independent standard Gaussians; \(W_0\) has independent \(N(0,1/n)\) entries and is independent of those rows. The same \(W_0\), and its actual transpose, are reused. Initially \(w=v_a=0\), \(k_a=h_a(0)\), and \(\tau=1\). Labels have fixed sufficiently small RMS \(Y\), and the population initial top-feature Gram has the stated strictly positive gap. No dynamics or observable is stopped, restarted, or modified on exceptional initializations.

Write \(u_a=x_a/\sqrt d\), \(X=\max_a\|u_a\|\), and

\[
 h_a=\tanh(Au_a),\quad
 B=W_0+\frac1{mn}\sum_a v_a k_a^T,\quad
 g_a=\tanh(Bh_a),\quad f_a=w^Tg_a/n,
 \quad r_a=f_a-y_a,\quad \rho=\|r\|_m,
\]

where \(\|z\|_m^2=m^{-1}\sum_a z_a^2\), and \(S(t)=\int_0^t\rho\). The passive query prediction is \(f_n(t,x)=w^T\tanh(B\tanh(Ax/\sqrt d))/n\).

Two unconditional bounds can be established:

1. For every initialization and finite \(T\),
   \[
   \sup_{t\le T,x}|f_n(t,x)|^2\le Y^2T,
   \qquad S(T)\le YT.
   \tag{1}
   \]
2. For a fixed sufficiently large operator cap \(K\), the initialized good event used by the fitting theorem has
   \[
   \Pr(\mathcal G_n^c)\le C e^{-cn}.
   \tag{2}
   \]

Consequently, if \(f_M\) is the actual clipped population predictor from the assigned route, its finite-activity bound gives \(\sup_{t,x}|f_M(t,x)|\le 2Y/\lambda\), and

\[
 \mathbb E\!\left[
  \mathbf1_{\mathcal G_n^c}
  \int\sup_{t\le T}|f_n(t,x)-f_M(t,x)|^2\,d\mu(x)
 \right]
 \le C Y^2(T+\lambda^{-2})e^{-cn}
 \tag{3}
\]

for every probability test law \(\mu\), without an input moment requirement for this exceptional-event term. For fixed \(T\), or even \(T\le e^{cn/2}\), (3) is negligible compared with \(n^{-1}\).

The factor \(T\) in (3) cannot be sent to infinity. The missing statement remains an all-time prediction moment bound on the actual dynamics outside \(\mathcal G_n\). Stronger initialized probability tails do not supply that statement.

## 2. Exact energy valid for every initialization

The unchanged readout equation is

\[
 \dot w=-\frac2m\sum_a r_a g_a.
\]

Set \(E_w(t)=\|w(t)\|_2^2/n\). Taking its scalar product with \(2w/n\) gives the exact identity

\[
 \begin{aligned}
 \dot E_w
 &=-4\langle r,f\rangle_m\\
 &=Y^2-4\|f-y/2\|_m^2\\
 &=-4\rho^2-4\langle y,r\rangle_m.
 \end{aligned}
 \tag{4}
\]

There is no derivative of a hidden feature in this computation. Thus (4) holds despite feature learning, clipping, memory normalization, and possible failure of training-loss monotonicity. It is the same readout identity as in the current manuscript's bounded-activation global-existence proof.

Because \(E_w(0)=0\), the second line of (4) implies

\[
 E_w(t)+4\int_0^t\|f(s)-y/2\|_m^2\,ds=Y^2t,
 \qquad E_w(t)\le Y^2t.
 \tag{5}
\]

For every query, \(\|g_x(t)\|_2/\sqrt n\le1\); Cauchy–Schwarz therefore gives \(|f_n(t,x)|\le\sqrt{E_w(t)}\le Y\sqrt t\). This proves the first part of (1), with a bound uniform over every input \(x\in\mathbb R^d\).

The last line of (4), integrated, and \(E_w(T)\ge0\) give

\[
 \int_0^T\rho^2\le-\int_0^T\langle y,r\rangle_m
 \le YS(T).
 \tag{6}
\]

For \(T>0\), Cauchy–Schwarz in time yields \(S(T)^2\le T\int_0^T\rho^2\le YTS(T)\). If \(S(T)>0\), divide by it; if it is zero the bound is immediate. Hence

\[
 S(T)\le YT,\qquad \int_0^T\rho^2\le Y^2T.
 \tag{7}
\]

These estimates also include \(Y=0\): then the state is stationary. They are estimates of integrated activity and loss, not pointwise loss monotonicity or finite total activity.

For completeness, the actual clipped equations give unconditional finite-time state bounds. The exact key formula is

\[
 k_a(t)=\frac{h_a(0)+\int_0^t\rho(s)h_a(s)\,ds}{1+S(t)},
 \qquad \|k_a(t)\|_\infty\le1.
\]

Using \(\|d_a\|_\infty,\|\ell_a\|_\infty\le M\), the equations for \(v,A\), and \(m^{-1}\sum_a|r_a|\le\rho\), gives

\[
 \begin{gathered}
 \tau(t)\le1+Yt,\qquad
 \|w(t)\|_\infty\le2S(t)\le2Yt,\\
 \frac1m\sum_a\|v_a(t)\|_\infty\le2MS(t)\le2MYt,\\
 \|B(t)-W_0\|_{\rm op}\le2MYt,\qquad
 \frac{\|A(t)-A_0\|_F}{\sqrt n}\le2MXYt.
 \end{gathered}
 \tag{8}
\]

The \(B\) bound follows termwise from \(\|v_a k_a^T/n\|_{\rm op}\le\|v_a\|_\infty\), because every key coordinate is bounded by one. For each individual value vector, \(\|v_a(t)\|_\infty\le2M\sqrt m\,Yt\) also follows. Local Lipschitz continuity on \(\tau>0\), \(\tau\ge1\), and (8) imply global existence for every finite initialization: a finite maximal time would leave all coordinates bounded and inside the locally Lipschitz domain. None of these estimates is bounded uniformly as \(t\to\infty\).

## 3. Exponentially small initialized failure probability

Let

\[
 Q^{(1)}_{ab}=\mathbb E[\tanh(A_{0,i}u_a)\tanh(A_{0,i}u_b)],
 \quad
 T_{ab}(Q)=\mathbb E[\tanh(Z_a)\tanh(Z_b)],
 \quad Z\sim N(0,Q),
\]

and \(Q^{(2)}=T(Q^{(1)})\). Assume \(Q^{(2)}/m\succeq2\lambda I_m\). Define empirical covariances

\[
 Q_{1,n}=\frac1n H_0^TH_0,\qquad
 Q_{2,n}=\frac1n G_0^TG_0,\qquad
 \Gamma_0=Q_{2,n}/m.
\]

Here \(G_0\) denotes the initialized feature matrix, not the Gaussian root matrix. Conditional on \(A_0\), the rows of \(W_0H_0\) are independent \(N(0,Q_{1,n})\) vectors. Therefore the second-feature covariance has conditional expectation \(T(Q_{1,n})\), and its rows are conditionally independent. This is an initialization calculation; no independence after training is asserted.

We give elementary bounds so that no unverified concentration theorem is required. If independent \(X_i\in[-1,1]\), the log moment-generating function of \(X_i-\mathbb EX_i\) has second derivative equal to a variance under a tilted law, which is at most one. Its value and first derivative vanish at zero, so it is at most \(s^2/2\). Exponential Markov inequality optimized at \(s=a\), applied to the sum, gives

\[
 \Pr\!\left\{\left|n^{-1}\sum_i(X_i-\mathbb EX_i)\right|>a\right\}
 \le2e^{-na^2/2}.
 \tag{9}
\]

The same calculation applies conditionally with the same constants.

Next, \(T\) is Lipschitz in entrywise maximum norm:

\[
 \max_{ab}|T_{ab}(Q)-T_{ab}(Q')|
 \le3\max_{ij}|Q_{ij}-Q'_{ij}|.
 \tag{10}
\]

To verify (10), let \(F_{ab}(z)=\tanh z_a\tanh z_b\). When \(a\ne b\), its Hessian has two diagonal entries of absolute value at most two and two mixed entries at most one; when \(a=b\), the single nonzero second derivative has absolute value at most six. Thus the sum of absolute Hessian entries is at most six. For independent Gaussian vectors \(U,V\) of covariances \(Q,Q'\), differentiate \(\mathbb E F_{ab}(\sqrt s\,U+\sqrt{1-s}\,V)\) on \(0<s<1\). Gaussian integration by parts gives

\[
 \frac d{ds}\mathbb E F_{ab}(\sqrt s\,U+\sqrt{1-s}\,V)
 =\frac12\sum_{ij}(Q-Q')_{ij}\,
 \mathbb E[\partial_{ij}F_{ab}(\sqrt s\,U+\sqrt{1-s}\,V)].
\]

This integration by parts follows coordinatewise from the standard normal density after writing \(U=Q^{1/2}Z\) and \(V=(Q')^{1/2}Z'\), so singular covariances cause no difficulty. Bounded first derivatives give an integrable endpoint majorant before integration by parts, and bounded Hessians give the displayed bound afterward. Integration from zero to one proves (10).

Apply (9) to the \(m^2\) entries at both layers, using thresholds \(\lambda/6\) and \(\lambda/2\), respectively. With probability at least \(1-4m^2e^{-n\lambda^2/72}\),

\[
 \max_{ab}|(Q_{1,n}-Q^{(1)})_{ab}|\le\lambda/6,
 \quad
 \max_{ab}|(Q_{2,n}-T(Q_{1,n}))_{ab}|\le\lambda/2.
\]

Equation (10) then gives \(\max_{ab}|(Q_{2,n}-Q^{(2)})_{ab}|\le\lambda\). For an \(m\times m\) matrix \(D\), \(\|D\|_{\rm op}\le\|D\|_F\le m\max_{ab}|D_{ab}|\). Consequently \(\|\Gamma_0-Q^{(2)}/m\|_{\rm op}\le\lambda\), and

\[
 \Pr\{\Gamma_0\not\succeq\lambda I_m\}
 \le4m^2e^{-n\lambda^2/72}.
 \tag{11}
\]

A simple net bound suffices for a sufficiently large fixed initialized operator cap. A \(1/4\)-net of the Euclidean unit sphere can be chosen with at most \(9^n\) elements: take a maximal \(1/4\)-separated subset and compare volumes of disjoint radius-\(1/8\) balls inside the radius-\(9/8\) ball. If \(\mathcal N\) is such a net, approximation of the two unit vectors in a bilinear form shows

\[
 \|W_0\|_{\rm op}\le2\max_{u,v\in\mathcal N}|u^TW_0v|.
\]

Each fixed bilinear form is \(N(0,1/n)\); its elementary exponential moment bound and a union bound give

\[
 \Pr\{\|W_0\|_{\rm op}>K\}
 \le2\exp\{-n(K^2/8-2\log9)\}.
 \tag{12}
\]

Choose any fixed \(K>4\sqrt{\log9}\), for example \(K=8\), and impose the fitting theorem's small-label condition with this \(K\). For

\[
 \mathcal G_n=\{\|W_0\|_{\rm op}\le K,\quad \Gamma_0\succeq\lambda I_m\},
\]

(11)–(12) prove (2), with explicit possible constants

\[
 C=4m^2+2,
 \qquad c=\min\{\lambda^2/72,\ K^2/8-2\log9\}>0.
 \tag{13}
\]

No independence of the two parts of the good event is used. This elementary operator proof deliberately only claims a sufficiently large cap; it does not assert the sharp Gaussian spectral edge.

## 4. What this removes, and what it does not

On the good event, the assigned fitting result gives \(\|w(t)\|_\infty\le2Y/\lambda\), and the same estimate holds in its clipped population construction. Let \(B_*=2Y/\lambda\). Pathwise on every initialization,

\[
 \int\sup_{t\le T}|f_n(t,x)-f_M(t,x)|^2\,d\mu(x)
 \le2Y^2T+2B_*^2.
\]

Multiplication by \(\mathbf1_{\mathcal G_n^c}\), expectation, and (13) prove (3). Thus a full prediction-error estimate already proved on \(\mathcal G_n\), including its population-bias contribution, would immediately become unconditional on every fixed finite horizon. This statement does not prove that good-event estimate or its bias component.

There is also an unconditional finite-horizon mean comparison. Put \(m_n^{\rm good}(t,x)=\mathbb E[f_n(t,x)\mid\mathcal G_n]\), when the good event has positive probability. Since \(\sup_{t,x}|m_n^{\rm good}|\le B_*\),

\[
 \sup_{t\le T,x}|\mathbb Ef_n(t,x)-m_n^{\rm good}(t,x)|
 \le (Y\sqrt T+B_*)\Pr(\mathcal G_n^c).
 \tag{14}
\]

This follows by writing the difference as \(\mathbb E[(f_n-m_n^{\rm good})\mathbf1_{\mathcal G_n^c}]\), with no exchange of supremum and expectation in the wrong direction.

For the all-time target, define the nonnegative extended random variable

\[
 Z_n=\int\sup_{t\ge0}|f_n(t,x)|^2\,d\mu(x).
\]

The exact additional tail obligation is

\[
 \mathbb E[Z_n\mathbf1_{\mathcal G_n^c}]\le C/n.
 \tag{15}
\]

For example, a sufficient independent theorem would be: for some \(p>1\),

\[
 \mathbb E Z_n^p\le C n^a.
 \tag{16}
\]

Hölder would then give

\[
 \mathbb E[Z_n\mathbf1_{\mathcal G_n^c}]
 \le(\mathbb E Z_n^p)^{1/p}
       \Pr(\mathcal G_n^c)^{1-1/p}
 \le C n^{a/p}e^{-c(1-1/p)n}=O(n^{-1}).
\]

A width-independent version of (16) is unnecessary; polynomial growth would suffice because the initialized tail is exponential. But neither (16), a substitute for it, nor even the almost-sure finiteness of this all-time \(Z_n\) outside the good event has been established here.

The energy identity supplies no coercive restoring term for \(E_w\). It constrains cumulative training output and residual activity, while its only universal pointwise envelope for the readout is \(E_w(t)\le Y^2t\). Exponential smallness of a fixed event cannot turn this increasing envelope into a time-uniform moment. Monotone convergence in \(T\) therefore gives no finite bound for (15).

This is a gap in the available argument, not an actual-model counterexample. In particular, unbounded readout norm would not itself prove unbounded predictions: simultaneous feature shrinkage could keep all relevant query outputs bounded. No frozen-feature model, zero clipping threshold, arbitrary time-dependent feature path, or unrelated random-variable example is offered as a counterexample to the requested dynamics.

## Route verdict

Established here: exact unconditional readout energy, integrated residual/activity bounds, polynomial finite-time state bounds and global finite-time existence; exponentially small probability of the initialized fitting-event complement; and an exponentially small exceptional-event contribution on every finite horizon, including exponentially growing horizons below the stated scale.

Open: a global predictor moment estimate for actual exceptional initializations, or an admissible counterexample that rules it out. Consequently the unconditional all-time mean-square theorem remains unproved even if its separate good-event population-bias obligation were supplied. The highest-leverage tail-specific next step is a proof or falsification of (15), with (16) as one sufficient route; repeating initialized concentration cannot settle it.
