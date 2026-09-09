# Bounded quartic activation: actual top energy closes, middle response remains open

For the single fixed activation
\[
 \phi(z)=1+\varepsilon\mathcal A(z),\qquad
 \mathcal A(z)=\int_0^z\frac{du}{1+u^4},\qquad \varepsilon=1/10,
\]
the actual top weighted-energy identity has an unconditional finite-physical-horizon bound on an existing strong population branch. In particular, its transport integral no longer needs an unproved readout fourth moment. The weight itself is **unbounded** after removal of the affine term; its linear growth and derivative bounds, together with the pointwise bounded readout, close that integral.

This closes a top-level integrability gap, but supplies no closure of the missing whole-network gate-weighted response estimate. At the middle layer it bounds the trained return pointwise and the complete \(q_2\) in \(L^2\), including its physical-time derivative. The surviving response term contains the initialized transpose acting on the **actual current** gated readout. Equations (18)–(21) below isolate it, with all trained matrices, their variations, both sample forces, and lower-layer transport retained. No divergence or impossibility result for the actual network is asserted.

## Scope and exact dependencies

This is one bounded theoretical test, with no experiments, delegation, repository changes, or new activation choices. Constants may depend on the fixed data and \(T\); the activation does not. The weighted common-channel identity is evaluated on the actual exchange-symmetric population branch for opposite labels \((1,-1)\), for every \(\rho<1\), including \(\rho=-1\). The all-label readout bound is also recorded. Failure to close the response even on the opposite-label branch leaves the arbitrary-label contract unresolved.

As in the supplied equations, the assertions are a priori estimates on an already existing strong canonical population branch with bounded initial operators, Hilbert–Schmidt trained increments, and the loss identity. They do not assume or establish the full population/GF/exact-GD identification theorem. In particular, population exchange symmetry and \(C(0)=0\) are not imposed on a finite independently initialized network.

Read dependencies:

1. /etc/codex/skills/solve-math-rigorously/SKILL.md, completely.
2. /etc/codex/skills/investigate-conjectures/SKILL.md, completely, and its required references research-contract.md, evidence-ledger.md, and adversarial-audit.md, completely. No experimental or multi-route reference was needed.
3. /tmp/l3-two-sample-Un7kw9/CONTRACT.md, completely.
4. /tmp/l3-two-sample-Un7kw9/DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md, completely.
5. /tmp/l3-two-sample-Un7kw9/COUPLED_EVEN_CHANNEL_ESTIMATE.md: the definitions and equation blocks in lines 25–195 and 294–721. Used the parameter metric and symmetry notation, forward/backward/update equations (2)–(9), actual operator-return and transport identities (19), (23)–(25), the definition and algebraic cancellation underlying (26)–(29), and the variation/Hessian definitions (32), (35), (37)–(40). None of its affine lower-slope bounds or conclusions is imported.

No further mathematical source is used. All activation-specific and closure estimates below are derived here.

## 1. Actual dynamics and the readout bound

Put
\[
 \delta=\sqrt{(1-\rho)/2}\in(0,1],\quad
 \mu=\sqrt{1-\delta^2},\quad
 m=\frac{4\varepsilon}{3}=\frac2{15},\quad
 H=1+m=\frac{17}{15},\quad R=2m=\frac4{15}.
\]
Indeed \(|\mathcal A|\le 1+\int_1^\infty u^{-4}du=4/3\). Thus
\[
 1-m\le\phi\le H,\qquad
 0<\phi'(z)=\frac{\varepsilon}{1+z^4}\le\varepsilon,\qquad
 \phi''(z)=-\frac{4\varepsilon z^3}{(1+z^4)^2},\quad
 |\phi''|\le4\varepsilon.
\]
This activation is positive, bounded, strictly increasing and nonaffine on every open interval, with no affine term added. More precisely, its slope has quartic flatness at zero, \(\phi'(z)=\varepsilon-\varepsilon z^4+O(z^8)\), and its curvature vanishes cubically, \(\phi''(z)=-4\varepsilon z^3+O(z^7)\).

On the three separate probability populations, define
\[
 h=\frac{\phi(M+\delta V)+\phi(M-\delta V)}2,\quad
 k=\frac{\phi(M+\delta V)-\phi(M-\delta V)}{2\delta},
\]
\[
 a=\frac{\phi'(M+\delta V)+\phi'(M-\delta V)}2,\quad
 b=\frac{\phi'(M+\delta V)-\phi'(M-\delta V)}{2\delta}.
\]
All products of fields are within their own population. The exact bounds are
\[
 |h|\le H,\quad |k|\le m/\delta,\quad
 0<a\le\varepsilon,\quad |b|\le\beta:=\frac{\varepsilon}{2\delta},
 \quad a+\delta|b|\le\varepsilon.                    \tag{1}
\]
The last bound follows since \(a\pm\delta b\) are the two positive activation derivatives.

Let \(A=A_e\oplus A_o\), \(B=B_e\oplus B_o\) be the full current hidden operators, \(M_1=\mu U\), and
\[
 (M_2,V_2)=(A_eh_1,A_ok_1),\qquad
 (M_3,V_3)=(B_eh_2,B_ok_2),\qquad G=\langle C,k_3\rangle .
\]
The backwards quantities and updates are
\[
 P_\ell=a_\ell p_\ell+b_\ell q_\ell,\qquad
 Q_\ell=\delta^2b_\ell p_\ell+a_\ell q_\ell,
\]
\[
 p_3=0,\ q_3=C,\quad P_3=b_3C,\ Q_3=a_3C,\quad
 p_2=B_e^*P_3,\ q_2=B_o^*Q_3,\quad
 p_1=A_e^*P_2,\ q_1=A_o^*Q_2,
\]
\[
 \begin{aligned}
 \dot U&=\lambda\mu P_1,&\dot V_1&=\lambda Q_1,\\
 \dot A_e&=\lambda P_2\otimes h_1,&
 \dot A_o&=\lambda Q_2\otimes k_1,\\
 \dot B_e&=\lambda P_3\otimes h_2,&
 \dot B_o&=\lambda Q_3\otimes k_2,&
 \dot C&=\lambda k_3,
 \end{aligned}
 \qquad \lambda=2\delta(1-\delta G).                  \tag{2}
\]
These are the actual two-force equations. In particular, the unreduced readout equation is
\(\dot C=-r_1h_{3,1}-r_2h_{3,2}\); on this branch
\((r_1,r_2)=(-(1-g),1-g)\), \(g=\delta G\), giving exactly \(\dot C=2\delta(1-g)k_3\). Neither force has been suppressed.

Use \((u\otimes v)w=u\langle v,w\rangle\). In the parameter metric
\[
 \|d\Theta\|^2=\|dU\|_2^2+\|dV_1\|_2^2+
 \|d(A-A_0)\|_{\rm HS}^2+\|d(B-B_0)\|_{\rm HS}^2+\|dC\|_2^2,
\]
omit \(U\) if \(\mu=0\). Directions orthogonal to the input plane remain constant. The loss identity gives
\[
 0\le g\le1,\quad 0\le\lambda\le2\delta,\qquad
 \int_0^t\|\dot\Theta\|^2ds\le1,\qquad
 \|\Theta(t)-\Theta(0)\|\le\sqrt t.                  \tag{3}
\]
Here \(1-g\) solves \((1-g)'=-2\delta^2\|\nabla G\|^2(1-g)\), initially 1. The final bound is Cauchy–Schwarz in time.

Now (1)–(2) give the crucial actual pointwise estimate
\[
 |\dot C(t,\omega)|\le R,\qquad |C(t,\omega)|\le Rt. \tag{4}
\]
For arbitrary labels the unreduced loss identity gives \(|r_1|+|r_2|\le2\) from initial loss 1, hence the analogous \(\|C(t)\|_\infty\le2Ht\). Thus bounded physical-time readout does not require a prescribed residual driver.

Fix \(T\) and \(K_0\ge1\) with \(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\le K_0\). Set \(K=K_0+\sqrt T\). Then
\[
 \|A(t)\|_{\rm op},\|B(t)\|_{\rm op}\le K,\qquad
 \|M_3(t)\|_2\le KH.                               \tag{5}
\]
Only probability-normalized \(L^2\) operator bounds are used here.

## 2. The new weight: unbounded but with controlled derivatives

Write \(D=\delta V\), \(f(z)=(1+z^4)^{-1}\), and
\[
 s(M,D)=\frac{\varepsilon}{2}\int_{-1}^1f(M+rD)\,dr>0.
\]
Then \(k=sV\). Direct subtraction of the two quartic denominators yields
\[
 b=-\frac{4\varepsilon MV(M^2+D^2)}
 {[1+(M+D)^4][1+(M-D)^4]}.
\]
Define the smooth weight
\[
 \omega(M,D)=
 \frac{4\varepsilon M^2(M^2+D^2)}
 {[1+(M+D)^4][1+(M-D)^4]\,s(M,D)}.
 \qquad Mb=-\omega k,\qquad \omega\ge0.             \tag{6}
\]
There is no division by \(M\) or \(V\). However, there is no positive uniform lower bound on \(s\). For example,
\[
 \omega(L,L)=
 L\,\frac{f(0)-f(2L)}{\mathcal A(2L)}
 \sim\frac{L}{\mathcal A(\infty)}
 \quad(L\longrightarrow\infty).
\]
Thus the old bounded-weight assertion would be false for this activation.

The needed replacement is elementary. Put
\[
 \ell(z)=-f'(z)/f(z)=\frac{4z^3}{1+z^4},\qquad
 d\pi_{M,D}(r)=
 \frac{f(M+rD)\,dr}{\int_{-1}^1 f(M+uD)\,du},\qquad
 L(M,D)=\mathbb E_\pi\ell(M+rD).
\]
Differentiating \(s\), or using \(b=V s_M\), proves \(\omega=ML\). Moreover,
\[
 |\ell|\le4,\qquad
 |\ell'|=\left|\frac{4z^2(3-z^4)}{(1+z^4)^2}\right|
 \le\frac{12z^2}{1+z^4}\le6,
\]
\[
 L_M=\mathbb E_\pi\ell'-\operatorname{Var}_\pi(\ell),\qquad
 L_D=\mathbb E_\pi(r\ell')-\operatorname{Cov}_\pi(\ell,r\ell).
\]
The two variances needed for the covariance bound are at most 16, since \(|r|\le1\). Consequently
\[
 0\le\omega\le4|M|,\qquad
 |\omega_M|\le4+22|M|,\qquad
 |\omega_D|\le22|M|.                               \tag{7}
\]
All formulas extend through \(D=0\) by the integral definition; there \(\omega(M,0)=4M^4/(1+M^4)\). These estimates use the quartic activation's bounded logarithmic derivative and its derivative, not a nonexistent lower bound on \(\phi'\).

## 3. Complete top identity, including transport, and a closed bound

For clarity, the actual forward velocities entering the weight are
\[
 \begin{aligned}
 \dot M_1&=\lambda\mu^2P_1,&\dot V_1&=\lambda Q_1,\\
 \dot M_2&=\lambda\|h_1\|_2^2P_2+
 A_e(a_1\dot M_1+\delta^2b_1\dot V_1),\\
 \dot V_2&=\lambda\|k_1\|_2^2Q_2+
 A_o(b_1\dot M_1+a_1\dot V_1),\\
 \dot M_3&=\lambda\|h_2\|_2^2b_3C+
 B_e(a_2\dot M_2+\delta^2b_2\dot V_2),\\
 \dot V_3&=\lambda\|k_2\|_2^2a_3C+
 B_o(b_2\dot M_2+a_2\dot V_2).
 \end{aligned}                                                 \tag{8}
\]
Each leading term is the corresponding trained-operator action. The remaining terms transport the lower-layer velocities through the full current operators.

Here is an explicit bound for these complete velocities. Put
\[
 S=H+m,\qquad \Gamma=3\varepsilon/2,\qquad
 N_1=1,\quad N_2=S+K\Gamma N_1,\quad N_3=S+K\Gamma N_2.
\]
For any parameter variation \(\eta\), let \(\xi_{M_\ell},\xi_{D_\ell}\) be its induced variations, with \(\xi_D=\delta\xi_V\). At layer 1,
\(\|\xi_{M_1}\|_2+\|\xi_{D_1}\|_2
\le\mu\|\eta_U\|_2+\delta\|\eta_{V_1}\|_2\le\|\eta\|\).
At an activation, the separate multiplier bounds
\(\|a\|_\infty\le\varepsilon\), \(\|\delta b\|_\infty\le\varepsilon/2\) give
\(\|dh\|_2+\|d(\delta k)\|_2
\le\Gamma(\|\xi_M\|_2+\|\xi_D\|_2)\).
At each operator action, its variation contributes at most
\(S\|\eta_A\|_{\rm HS}\) or \(S\|\eta_B\|_{\rm HS}\) to the sum of the two norms. Induction therefore proves
\[
 \|\xi_{M_\ell}\|_2+\|\xi_{D_\ell}\|_2\le N_\ell\|\eta\|,
 \qquad
 \|\dot M_3\|_2+\|\dot D_3\|_2\le N_3\|\dot\Theta\|. \tag{9}
\]
This also holds for variations breaking exchange symmetry: use the full operator variations before taking their actions.

Let \(E_{B,e}=B_e-B_{0,e}\) and define
\[
 \mathcal E_B=
 \|E_{B,e}\|_{\rm HS}^2+\mathbb E_{\Omega_3}[\omega(M_3,D_3)C^2].
\]
Using \(E_{B,e}h_2=M_3-B_{0,e}h_2\), (2) and (6) gives
\[
 \frac d{dt}\|E_{B,e}\|_{\rm HS}^2
 =-2\langle\omega_3C,\dot C\rangle
   -2\lambda\langle b_3C,B_{0,e}h_2\rangle.
\]
The first term cancels against the readout derivative of the weighted part. Since \(\mathcal E_B(0)=0\), the complete identity is
\[
 \mathcal E_B(t)=
 -2\int_0^t\lambda\langle b_3C,B_{0,e}h_2\rangle\,ds
 +\int_0^t\mathbb E[C^2(\omega_M\dot M_3+\omega_D\dot D_3)]\,ds .
                                                               \tag{10}
\]
In particular, the second integral includes
\[
 \int_0^t\lambda\,\mathbb E\!\left[
 C^3\{\omega_M\|h_2\|_2^2b_3+
       \delta\omega_D\|k_2\|_2^2a_3\}\right]ds
\]
from training \(B\), as well as both full \(B\)-transport terms in (8), and the \(A\)-transport and first-layer updates inside them. No sign is assigned to these terms.

The initialized work is bounded by
\[
 2\int_0^t\lambda|\langle b_3C,B_{0,e}h_2\rangle|\,ds
 \le 2\varepsilon RK_0H\int_0^t s\,ds
 =\varepsilon RK_0H\,t^2.
\]
For the entire transport integrand, (4), (5), (7), and (9) give
\[
 \left|\mathbb E[C^2\dot\omega_3]\right|
 \le R^2s^2(4+22KH)
       (\|\dot M_3\|_2+\|\dot D_3\|_2)
 \le R^2s^2(4+22KH)N_3\|\dot\Theta\|.
\]
Cauchy–Schwarz and (3), with \(\int_0^t s^4ds=t^5/5\), now prove the closed actual-network estimate
\[
 0\le\mathcal E_B(t)
 \le \varepsilon RK_0H\,t^2+
 \frac{R^2(4+22KH)N_3}{\sqrt5}\,t^{5/2},
 \qquad 0\le t\le T.                               \tag{11}
\]
Every constant here is explicit in the fixed activation, \(K_0,T\). No Gaussian-action moment or unknown forcing norm occurs.

These estimates also justify the identity, rather than merely bounding it formally. Indeed \(M_3,D_3\) have absolutely continuous pointwise representatives, since their time derivatives are in \(L^2\) of time and population by (3), (9). Equations (4) and (7) make \(\omega C^2\) integrable; the preceding estimate makes \(C^2\dot\omega\) integrable. Finally,
\(\mathbb E|\omega C\dot C|\le4R^2t\|M_3\|_1\).
The pointwise product rule is therefore integrable, and Fubini yields (10).

## 4. What this gives for the actual middle return

Integrating the trained operator in (2), and taking its adjoint against the current top field, gives
\[
 \begin{aligned}
 p_2(t)&=p_2^0(t)+p_2^{\rm tr}(t),&
 p_2^0(t)&=B_{0,e}^*(b_3(t)C(t)),\\
 p_2^{\rm tr}(t)&=\int_0^t\lambda(s)h_2(s)
       \langle P_3(s),P_3(t)\rangle ds,\\
 q_2(t)&=q_2^0(t)+q_2^{\rm tr}(t),&
 q_2^0(t)&=B_{0,o}^*(a_3(t)C(t)),\\
 q_2^{\rm tr}(t)&=\int_0^t\lambda(s)k_2(s)
       \langle Q_3(s),Q_3(t)\rangle ds .
 \end{aligned}                                                 \tag{12}
\]
These are causal identities for the trained network, not freely specified drivers. Bounds (1), (4) imply
\[
 \|p_2^{\rm tr}(t)\|_\infty\le\delta H\beta^2R^2t^3,\qquad
 \|q_2^{\rm tr}(t)\|_\infty\le m\varepsilon^2R^2t^3,\qquad
 \|q_2(t)\|_2\le K\varepsilon Rt.                  \tag{13}
\]
For example, the second integral in (12) is bounded pointwise by
\(2m\int_0^t\varepsilon^2R^2st\,ds\).

The complete physical-time derivative is also controlled:
\[
 \dot q_2=\lambda k_2\|Q_3\|_2^2+
 B_o^*(a_3\dot C+C\dot a_3),
\]
\[
 \|\dot q_2(t)\|_2
 \le2m\varepsilon^2R^2t^2+K\varepsilon R+
       4K\varepsilon Rt\,N_3\|\dot\Theta(t)\|.       \tag{14}
\]
Here \(\|\dot a_3\|_2\le4\varepsilon N_3\|\dot\Theta\|\), using both transported preactivation velocities. Thus \(q_2\in H^1([0,T];L^2)\). The term \(\lambda k_2\|Q_3\|_2^2\) is precisely the differentiated trained transpose; it has not been omitted.

These bounds do not promote \(q_2^0=B_{0,o}^*(a_3C)\) to \(L^p\), \(p>2\). Although \(a_3C\) is bounded, it depends on the same initialized operator whose transpose is acting. The assumed \(L^2\) operator bound and time regularity do not supply an \(L^2\)-to-\(L^p\) or \(L^\infty\) action estimate for that selected input.

Moreover, (11) contains no coercive control of \(Q_3=a_3C\): at \(M_3=0\) the weight is zero, whereas \(a_3=\varepsilon/(1+D_3^4)>0\). This is a statement about the weight, not a claimed reachable-state counterexample. The middle bounds above come from bounded readout and the actual operator equations; an additional coercive bound on the initialized middle return has not emerged.

## 5. Full response identity and the precisely surviving actual terms

To identify the remaining issue without replacing the network by a local ODE, let \(\eta\) be a parameter response and set \(z_{\ell,\sigma}=M_\ell+\sigma D_\ell\), \(\xi_{\ell,\sigma}=\xi_{M_\ell}+\sigma\xi_{D_\ell}\), for \(\sigma=\pm1\). The full forward variations are
\[
 \xi_{M_2}=\eta_Ah_1+A\,dh_1,\quad
 \xi_{V_2}=\eta_Ak_1+A\,dk_1,\quad
 \xi_{M_3}=\eta_Bh_2+B\,dh_2,\quad
 \xi_{V_3}=\eta_Bk_2+B\,dk_2,
\]
\[
 dh_\ell=a_\ell\xi_{M_\ell}+\delta^2b_\ell\xi_{V_\ell},\qquad
 dk_\ell=b_\ell\xi_{M_\ell}+a_\ell\xi_{V_\ell}.       \tag{15}
\]
The backward variations retain, in particular,
\[
 \widehat p_2=\eta_B^*P_3+B^*\widehat P_3,\quad
 \widehat q_2=\eta_B^*Q_3+B^*\widehat Q_3,\quad
 \widehat p_1=\eta_A^*P_2+A^*\widehat P_2,\quad
 \widehat q_1=\eta_A^*Q_2+A^*\widehat Q_2.
\]
Writing \(\alpha_\ell=da_\ell\), \(\gamma_\ell=db_\ell\), the local residuals are
\[
 R_\ell^P=\alpha_\ell p_\ell+\gamma_\ell q_\ell,\qquad
 R_\ell^Q=\delta^2\gamma_\ell p_\ell+\alpha_\ell q_\ell,
\]
and
\(\widehat P=a\widehat p+b\widehat q+R^P\),
\(\widehat Q=\delta^2b\widehat p+a\widehat q+R^Q\).
Since the second derivatives of \(\phi\) are bounded,
\[
 |\alpha_\ell|\le4\varepsilon(|\xi_{M_\ell}|+|\xi_{D_\ell}|),\quad
 |\gamma_\ell|\le(4\varepsilon/\delta)
                   (|\xi_{M_\ell}|+|\xi_{D_\ell}|).
\]
Consequently the entire top residual already closes:
\[
 \|R_3^P\|_2+\|R_3^Q\|_2
 \le4\varepsilon RT(1+\delta^{-1})N_3\|\eta\|.       \tag{16}
\]

For completeness the exact parameter response energy, including variations breaking exchange symmetry, is as follows. Extend \(F=\langle C,h_3\rangle\) and \(G\) off the symmetric branch. Then
\(\mathcal L=F^2+(\delta G-1)^2\).
For source \(j\), differentiation of the actual loss flow gives
\(\dot\eta=\lambda D^2G\,\eta-2\delta^2\nabla G\,DG[\eta]
-2\nabla F\,DF[\eta]+j\). Hence
\[
 \begin{aligned}
 \frac12\frac d{dt}\|\eta\|^2
 +2\delta^2(DG[\eta])^2+2(DF[\eta])^2
 ={}&\lambda\left\{
 2\langle\eta_C,dk_3\rangle
 +2\sum_{\ell=1}^2[
   \langle P_{\ell+1},\eta_{W_\ell}dh_\ell\rangle+
   \langle Q_{\ell+1},\eta_{W_\ell}dk_\ell\rangle]
 +\sum_{\ell=1}^3\mathcal S_\ell\right\}
 +\langle\eta,j\rangle,\\
 \mathcal S_\ell={}&\frac12\sum_{\sigma=\pm1}
 \mathbb E\!\left[
 \phi''(z_{\ell,\sigma})
 (p_\ell+\sigma q_\ell/\delta)\xi_{\ell,\sigma}^2\right],
 \qquad W_1=A,\quad W_2=B .
 \end{aligned}                                                 \tag{17}
\]
To verify the identity, the second differential of \(Wh\) is
\(2\eta_Wdh+Wd^2h\). Move the latter term backwards by the current \(W^*\) at each layer. The local second differential is exactly \(\mathcal S_\ell\), obtained by differentiating the two sample activations. This accounts for both operator-variation terms and both sample curvatures. The two nonnegative terms on the left retain the variation of the loss factors, including the common prediction.

At the middle layer the unclosed part is precisely
\[
 \mathcal S_2^0=
 \frac12\sum_{\sigma=\pm1}\mathbb E_{\Omega_2}\!\left[
 \frac{-4\varepsilon z_{2,\sigma}^{\,3}}
 {(1+z_{2,\sigma}^{\,4})^2}
 \left\{
 B_{0,e}^*(b_3C)+\frac{\sigma}{\delta}B_{0,o}^*(a_3C)
 \right\}\xi_{2,\sigma}^2\right].                  \tag{18}
\]
In the differentiated backward equations, the corresponding unresolved \(L^2\) residual pair is
\[
 \left(
 \alpha_2 B_{0,e}^*(b_3C)+\gamma_2 B_{0,o}^*(a_3C),\
 \delta^2\gamma_2 B_{0,e}^*(b_3C)+\alpha_2 B_{0,o}^*(a_3C)
 \right).                                         \tag{19}
\]
All fields in these expressions are evaluated on the current actual trajectory, and \(\xi_2\) includes both terms in (15). In particular, the curvature arising from the quartically flat slope has been kept exactly.

There is an analogous first-layer term
\[
 \mathcal S_1^0=\frac12\sum_{\sigma=\pm1}
 \mathbb E_{\Omega_1}\!\left[
 \phi''(z_{1,\sigma})
 \{A_{0,e}^*P_2+\sigma A_{0,o}^*Q_2/\delta\}
 \xi_{1,\sigma}^2\right].                          \tag{20}
\]
No other unestimated Hessian contribution is needed in this decomposition. To see this explicitly, set
\[
 L_P=2K\varepsilon\beta R,\qquad
 L_Q=K(\varepsilon^2+\delta^2\beta^2)R.
\]
The backwards equations give \(\|P_2(t)\|_2\le L_Pt\) and
\(\|Q_2(t)\|_2\le L_Qt\). The exact first-layer trained returns are
\[
 p_1^{\rm tr}(t)=\int_0^t\lambda(s)h_1(s)
       \langle P_2(s),P_2(t)\rangle ds,\qquad
 q_1^{\rm tr}(t)=\int_0^t\lambda(s)k_1(s)
       \langle Q_2(s),Q_2(t)\rangle ds .
\]
Thus, just as in (12), they obey
\[
 \|p_1^{\rm tr}(t)\|_\infty\le\delta H L_P^2t^3,\qquad
 \|q_1^{\rm tr}(t)\|_\infty\le mL_Q^2t^3.
\]
Define the four deterministic upper bounds at horizon \(T\) by
\[
 U_1^P=\delta H L_P^2T^3,\quad U_1^Q=mL_Q^2T^3,\qquad
 U_2^P=\delta H\beta^2R^2T^3,\quad
 U_2^Q=m\varepsilon^2R^2T^3,
\]
and put
\[
 Z_2=(L_P+L_Q)T,\quad Z_3=(\beta+\varepsilon)RT,
\]
\[
 H_T=
 \frac{2\Gamma}{\delta}(N_3+Z_2N_1+Z_3N_2)
 +\frac{4\varepsilon RT}{\delta}N_3^2
 +4\varepsilon\sum_{\ell=1}^2
       N_\ell^2(U_\ell^P+U_\ell^Q/\delta)<\infty .
\]
Indeed \(\|dh_\ell\|_2+\|dk_\ell\|_2
\le\Gamma N_\ell\|\eta\|/\delta\) controls every mixed operator term in (17). Also
\(\|\xi_{\ell,+}\|_2^2+\|\xi_{\ell,-}\|_2^2
=2(\|\xi_{M_\ell}\|_2^2+\|\xi_{D_\ell}\|_2^2)\)
controls the top and trained-return curvature terms with the stated constants. Thus (17) reduces to the explicit estimate
\[
 \frac12\frac d{dt}\|\eta\|^2
 +2\delta^2(DG[\eta])^2+2(DF[\eta])^2
 \le \lambda H_T\|\eta\|^2
       +\lambda(\mathcal S_1^0+\mathcal S_2^0)
       +\langle\eta,j\rangle.                      \tag{21}
\]
Equations (17)–(21) hold in finite dimension and for population responses whose displayed products exist. Establishing that existence and an upper estimate for the two surviving products is part of the unresolved response problem; it is not an assumption used for the unconditional top estimate (11).

In particular, (18) involves an \(L^2\) initialized return multiplied by a squared \(L^2\) perturbation. Bounded curvature, including its vanishing at zero and decay at infinity, does not supply the missing estimate on that actual product from the norms proved here. Nor does (11) relate this middle-layer multiplier to the middle perturbation: its weight lives on the top population. A further actual reachable-state argument could still control (18); this calculation neither assumes such an argument nor disproves its existence.

## Result of this bounded test

Proved on the stated actual branch: the full transported top identity (10) and closed bound (11); bounded trained middle returns and the complete \(L^2\) physical-time estimate (13)–(14); and closure of the top local gate response (16).

Still open: the actual initialized-return curvature products (18)–(20). They survive after all trained-return contributions and matrix-variation terms have been bounded. Thus bounded readout removes the top fourth-moment obstruction, but the top weighted energy supplies no new closure of the missing middle/whole-network response estimate. No Gaussian-action \(L^p\) claim, global continuation theorem, or full joint population/GF/exact-GD theorem follows from this test.
