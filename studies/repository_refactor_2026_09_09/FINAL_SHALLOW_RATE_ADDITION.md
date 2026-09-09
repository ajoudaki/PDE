## Quantitative shallow continuous-flow comparison

This result uses exactly the one-hidden-layer model and characteristic
construction of linear-dynamics Section 8, specialized to label one.
The stored readout and effective first preactivation are independent
order-one standard Gaussians. There is one RMS-unit input, no hidden
connector, full square loss, and a common physical mobility multiplier
\(\kappa\ge0\). The activation satisfies
\(\phi\in C^2(\mathbb R)\) and
\(\|\phi'\|_\infty+\|\phi''\|_\infty<\infty\); it may grow linearly.
For iid marks \(\xi_i=(a_i^0,u_i^0)\sim N(0,I_2)\), the actual finite flow is
\[
 f_n=\frac1n\sum_i a_i\phi(u_i),\qquad
 \dot a_i=2\kappa(1-f_n)\phi(u_i),\qquad
 \dot u_i=2\kappa(1-f_n)a_i\phi'(u_i).
 \tag{SR.1}
\]
The effective raw metric is
\(n^{-1}(\|da\|_2^2+\|du\|_2^2)\).

**Theorem.** Let \(f\) be the deterministic characteristic-flow output
of Section 8. For every fixed \(T<\infty\), there is a finite constant
\(C_T\), depending only on the activation, mobility and horizon, such that
for every width \(n\ge1\),
\[
 E\sup_{t\le T}|f_n(t)-f(t)|^2\le C_T/n,
 \qquad E\sup_{t\le T}|f_n(t)-f(t)|^4\le C_T/n^2.
 \tag{SR.2}
\]
Consequently \(\sup_{t\le T}\operatorname{Var} f_n(t)\le C_T/n\), and
with \(\mathcal L_n=(1-f_n)^2\), \(\mathcal L=(1-f)^2\),
\[
 E\sup_{t\le T}|\mathcal L_n(t)-\mathcal L(t)|^2\le C_T/n.
 \tag{SR.3}
\]
If in addition \(\phi\) is bounded, let \(\bar X_i\) be the limiting
characteristic with the same initial mark \(\xi_i\), where
\(X_i^n=(a_i,u_i)\). Then
\[
 E\left[\frac1n\sum_i\sup_{t\le T}
       |X_i^n(t)-\bar X_i(t)|_{\mathbb R^2}^2\right]\le C_T/n.
 \tag{SR.4}
\]
The \(\bar X_i\) are independent because their common limiting clock is
deterministic. In particular each fixed finite set of actual particle paths
converges jointly to independent limiting paths under this coupling.
All assertions concern continuous gradient flow. No raw-GD rate, kernel
rate, growing-depth conclusion or population fitting claim is added.

*Proof.* Write \(c=2\kappa\),
\(H(a,u)=a\phi(u)\), and
\(V(a,u)=(\phi(u),a\phi'(u))\). Let \(\Psi_s\xi\) solve
\(\partial_s\Psi_s=V(\Psi_s)\). The global feature characteristics, the
physical clocks, and their exact identification with (SR.1) are proved in
Section 8. The estimates needed here can also be read directly from linear
growth of \(V\): on each fixed \([-S,S]\),
\[
 \sup_{|s|\le S}|\Psi_s\xi|\le C_S(1+|\xi|),\qquad
 Y_s(\xi)=H(\Psi_s\xi),\quad J_s(\xi)=|V(\Psi_s\xi)|^2,
\]
\[
 \partial_sY_s=J_s,\qquad
 \sup_{|s|\le S}(|Y_s|+|J_s|)\le C_S(1+|\xi|^2).
 \tag{SR.5}
\]
Thus all fixed moments of the envelope are finite. Put
\(F(s)=EY_s\), \(F_n(s)=n^{-1}\sum_iY_s(\xi_i)\).
Dominated differentiation gives \(F'=EJ_s\ge0\), \(F(0)=0\), and
\(F_n'=n^{-1}\sum_iJ_s(\xi_i)\ge0\).

Here is a quantitative continuum empirical bound. With \(P_n\) the
average over the marks and \(P\) their expectation, set
\(D_{n,S}=\sup_{|s|\le S}|F_n(s)-F(s)|\). The exact integral identity
in (SR.5) gives
\[
 D_{n,S}\le |(P_n-P)Y_0|
       +\int_{-S}^S|(P_n-P)J_v|\,dv.
 \tag{SR.6}
\]
For iid centered real \(Z_i\), direct expansion and independence give
\[
 E\left|\frac1n\sum_iZ_i\right|^2=EZ_1^2/n,\qquad
 E\left|\frac1n\sum_iZ_i\right|^4
 =\frac{nEZ_1^4+3n(n-1)(EZ_1^2)^2}{n^4}.
 \tag{SR.7}
\]
The same expansion at even order eight is at most \(C n^{-4}\) when
\(E|Z_1|^8<\infty\): terms with an index appearing once vanish, so each
surviving term has at most four distinct indices. There are at most
\(C n^4\) such terms, and Hölder bounds each by \(E|Z_1|^8\).
Applying (SR.7) to the centered \(Y_0,J_v\), then
\((\int_{-S}^S|g|)^p\le(2S)^{p-1}\int_{-S}^S|g|^p\), yields
\[
 ED_{n,S}^2\le C_S/n,\qquad ED_{n,S}^4\le C_S/n^2.
 \tag{SR.8}
\]
Take \(S>0\); the zero-length interval is covered by (SR.7).

The actual clocks satisfy
\[
 \dot s_n=c(1-F_n(s_n)),\quad \dot s=c(1-F(s)),\quad s_n(0)=s(0)=0.
\]
The residual equations and nonnegativity of \(F_n',F'\) give
\[
 |1-f_n(t)|\le |1-F_n(0)|,\quad 0\le f(t)\le1,\quad
 |s_n(t)|\le cT|1-F_n(0)|,\quad 0\le s(t)\le cT.
 \tag{SR.9}
\]
These also preclude finite physical-time escape. On
\(E_n=\{|F_n(0)|\le1\}\), both clocks lie in the deterministic interval
\([-S,S]\) with \(S=2cT+1\). Set
\(L_S=\sup_{|s|\le S}|F'(s)|<\infty\). Subtracting the clock integral
equations, using \(F\) for the Lipschitz term, and iterating gives
\[
 \sup_{t\le T}|s_n(t)-s(t)|\le cT e^{cL_ST}D_{n,S},\quad
 \sup_{t\le T}|f_n(t)-f(t)|\le(1+cTL_Se^{cL_ST})D_{n,S}.
 \tag{SR.10}
\]
The second inequality uses
\(F_n(s_n)-F(s)=[F_n(s_n)-F(s_n)]+[F(s_n)-F(s)]\).

The exceptional event is controlled by the actual loss flow, not by an
unbounded random clock. Write \(Z_n=F_n(0)\), a centered iid sample mean.
On \(E_n^c\), (SR.9) gives
\(\sup_{t\le T}|f_n-f|\le3+|Z_n|\le4|Z_n|\).
Thus its contributions to the second and fourth powers are bounded by
\(16E|Z_n|^4\) and \(256E|Z_n|^4\), respectively, both \(O(n^{-2})\).
Together with (SR.8)–(SR.10) this proves (SR.2), including \(\kappa=0\).
Variance is bounded by squared error from any deterministic number.
Finally, if \(\Delta=f_n-f\),
\(|\mathcal L_n-\mathcal L|\le2|\Delta|+|\Delta|^2\) by (SR.9).
Squaring and using (SR.2) proves (SR.3).

For (SR.4), assume \(\|\phi\|_\infty=M<\infty\) and write
\(B=\|\phi'\|_\infty\). Direct integration, for either sign of \(s\), gives
\[
 |A_s-a|\le M|s|,\qquad
 |U_s-u|\le B(|a||s|+Ms^2/2).
 \tag{SR.11}
\]
On \(E_n\), the speed on the fixed clock interval is at most
\(C_T(1+|a_i^0|)\). Equations (SR.10)–(SR.11) imply
\[
 \frac1n\sum_i\sup_{t\le T}|X_i^n-\bar X_i|^2\mathbf1_{E_n}
 \le C_T M_{2,n}D_{n,S}^2,
 \qquad M_{2,n}=\frac1n\sum_i(1+|a_i^0|^2).
\]
Jensen gives \(EM_{2,n}^2\le E(1+|a_1^0|^2)^2<\infty\).
Cauchy–Schwarz and (SR.8) bound this expectation by \(C_T/n\).
On the complement, apply (SR.11) at the two clocks and (SR.9) to get
\[
 \frac1n\sum_i\sup_{t\le T}|X_i^n-\bar X_i|^2\mathbf1_{E_n^c}
 \le C_T M_{2,n}(1+|Z_n|^4)\mathbf1_{|Z_n|>1}.
\]
Its expectation is at most
\(2C_T(EM_{2,n}^2)^{1/2}(E|Z_n|^8)^{1/2}=O(n^{-2})\), by the
order-eight expansion following (SR.7). This proves (SR.4).
Exchangeability makes each fixed particle's expected squared path error
bounded by the same average; a sum over finitely many particles proves
the last assertion. No independence between \(D_{n,S}\), \(Z_n\) and
an individual mark has been assumed. \(\square\)
