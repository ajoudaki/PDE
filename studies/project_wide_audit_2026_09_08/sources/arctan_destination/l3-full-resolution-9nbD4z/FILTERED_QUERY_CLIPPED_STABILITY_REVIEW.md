# Isolated adversarial audit: fixed-clipping stability bridge

**Verdict: PASS. No required mathematical corrections.**

Audited candidate: [FILTERED_QUERY_CLIPPED_STABILITY.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/FILTERED_QUERY_CLIPPED_STABILITY.md).

Verified candidate SHA-256:
9e611d03ff2e82b0acd6f17d2786ed6e5d84c06777672aee6dc86a6c934edb55.

The entire candidate (410 lines) and the entire [solve-math-rigorously skill](/etc/codex/skills/solve-math-rigorously/SKILL.md) were read directly. This audit uses only the stated deterministic hypotheses and reconstructs the estimates below. The probabilistic companion was neither inspected nor assumed. No other project context, experiments, subagents, or ledgers were used; the candidate was not edited.

Equation (9) is valid for the actual simultaneous recursion (7) compared with the actual finite-width flow (2), with one common fixed map satisfying (1). Its constant is independent of width, mesh, filter scale, query errors, warmup errors, and the choice of that map within (1). The proof establishes stability of the evolving states, rather than only a consistency residual along the reference. Its qualifications concerning clipping, initialization, derivatives, and other downstream claims are necessary and are respected.

## 1. Exact reference and all pre-step memories

Throughout this audit, the reference flow means exactly (2), together with its stated algebraic forward fields. All vectors have width \(n\). Euclidean norms are denoted by \(\|\cdot\|_2\), with every factor \(1/\sqrt n\) written explicitly; the readout coordinate bound retains its stated infinity norm. Matrix differences are measured in Frobenius norm, and fixed matrix actions use operator norm.

The scalar function \(F(z)=z+z^3/3\) maps \(\mathbb R\) bijectively onto \(\mathbb R\), and
\[
 F'(z)=1+z^2=\frac1{\phi'(z)},\qquad
 (F^{-1})'(x)=\phi'(F^{-1}(x)).
\]
Consequently \(F^{-1}\) is 1-Lipschitz and
\[
 (\phi\circ F^{-1})'(x)=\phi'(F^{-1}(x))^2\le1.
\]
The transformation introduces no assumption on the magnitude of the initial bottom coordinates. In particular,
\[
 (x^{(1)})'=(W^{(2)})^{\mathsf T}\delta^{(2)}
 =(W_0^{(2)})^{\mathsf T}(a^{(2)})'+(R^{(1)})',
\]
which proves (4) exactly with the stated zero initial memories.

The continuous learned matrices and returned memory are
\[
 M^{(\ell)}(s)=\frac1n\int_0^s
       \delta^{(\ell)}(t)h^{(\ell-1)}(t)^{\mathsf T}\,dt,
 \qquad \ell=2,3,
\]
\[
 R^{(1)}(s)=\frac1n\int_0^s\int_0^t
 h^{(1)}(u)
 (\delta^{(2)}(u))^{\mathsf T}\delta^{(2)}(t)\,du\,dt.
\]
The simultaneous recursions give, exactly,
\[
 \widehat a_k^{(2)}=\eta\sum_{i<k}\widehat\delta_i^{(2)},\qquad
 \widehat M_k^{(\ell)}=\frac{\eta}{n}
 \sum_{i<k}\widehat\delta_i^{(\ell)}
                  (\widehat h_i^{(\ell-1)})^{\mathsf T},
\]
\[
 \widehat R_k^{(1)}
 =\eta\sum_{i<k}(\widehat M_i^{(2)})^{\mathsf T}
                      \widehat\delta_i^{(2)}
 =\frac{\eta^2}{n}\sum_{0\le j<i<k}
 \widehat h_j^{(1)}
 (\widehat\delta_j^{(2)})^{\mathsf T}\widehat\delta_i^{(2)},
\]
and
\[
 \widehat W_k^{(4)}=W_0^{(4)}+\eta\sum_{i<k}\widehat h_i^{(3)}.
\]
Thus every learned contribution is retained, with the correct strict ordering in the returned memory. The discrete memory is not identified with an exact continuous integral, with a terminal matrix-times-memory product, or with a sum using the newly updated matrix.

The filter targets also use only the step-\(k\) memories and fields. In particular, no \(\widehat a_{k+1}\), \(\widehat M_{k+1}\), or \(\widehat R_{k+1}\) is substituted into a step-\(k\) target. The later reference-increment terms account for this delay.

## 2. Bounds preceding and independent of stability

Explicit constants make the width independence and absence of a filter-scale dependence checkable. Set
\[
\begin{gathered}
 T=S+1,\quad c=\pi/2,\quad U=1+cT,\\
 J_3=cTU,\quad P_3=M+J_3,\quad Q=P_3U+1,\\
 J_2=cTQ,\quad P_2=M+J_2.
\end{gathered}
\]
These depend only on \(S,M\). The same bounds hold for the reference and recursion on their respective time domains:
\[
 \|W^{(4)}\|_\infty\le U,\quad
 \frac{\|h^{(\ell)}\|_2}{\sqrt n}\le c,\quad
 \frac{\|\delta^{(3)}\|_2}{\sqrt n}\le U,\quad
 \|M^{(3)}\|_{\rm F}\le J_3.
\]
The readout estimate follows coordinatewise by integrating or summing its bounded derivative or increment. For the matrix estimate, the exact identity
\[
 \|uv^{\mathsf T}/n\|_{\rm F}
 =\frac{\|u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
\]
applies to each integral or update.

The reference satisfies \(\frac{\|q^{(2)}\|_2}{\sqrt n}\le P_3U\). The recursion satisfies
\[
 \frac{\|\widehat q_k^{(2)}\|_2}{\sqrt n}
 \le P_3U+\frac{\|e_{T,k}^{(3)}\|_2}{\sqrt n}\le Q.
\]
Every individual query error in this proof has Euclidean norm divided by \(\sqrt n\) at most \(b\), since (6) bounds the sum of these two nonnegative quantities for each layer. Domination \(|\tau(v)|\le|v|\), together with \(|\phi'|\le1\), now gives \(\frac{\|\delta^{(2)}\|_2}{\sqrt n}\le Q\) in both systems. It follows that
\[
 \frac{\|a^{(2)}\|_2}{\sqrt n}\le TQ,\quad
 \|M^{(2)}\|_{\rm F}\le J_2,\quad
 \frac{\|R^{(1)}\|_2}{\sqrt n}\le TJ_2Q.
\]
In particular, both trained layer-two and layer-three operator norms are bounded by \(P_2,P_3\), respectively.

These arguments do not use state errors, any probabilistic estimate beyond the assumed numerical bound (6), or the size of \(R\). The filters cannot invalidate them: bounded activations hold at arbitrary register values, and the readout and rank updates have the bounds just obtained.

For \(p=\eta/\varepsilon\in(0,1]\), the filter updates are convex combinations. Their targets therefore give
\[
 \frac{\|\widehat x_k^{(1)}-x_0^{(1)}\|_2}{\sqrt n}
 \le MTQ+TJ_2Q+1,
\]
\[
 \frac{\|\widehat z_k^{(2)}\|_2}{\sqrt n}\le cP_2+1,\qquad
 \frac{\|\widehat z_k^{(3)}\|_2}{\sqrt n}\le cP_3+1.
\]
Indeed the initial preactivations have normalized size at most \(Mc+d_0\le Mc+1\), and each corresponding target is bounded by \(cP_\ell+b\). Subtracting \(x_0^{(1)}\) before bounding the bottom filter avoids a bound on \(x_0^{(1)}\) itself. The reference preactivations have bounds \(cP_2,cP_3\).

The reference vector field is locally Lipschitz at each fixed finite width: matrix products are smooth, the coordinate functions are smooth, and the fixed clipping map is Lipschitz. The local ODE existence and continuation theorem therefore gives a unique local solution, extendible unless its parameters leave every bounded set at a finite endpoint. The preceding estimates hold up to any local endpoint before \(T\). Moreover,
\[
 \frac{\|(z^{(1)})'\|_2}{\sqrt n}\le P_2Q.
\]
Thus the bottom coordinates remain bounded relative to their finite initial values; all matrix and readout coordinates also remain bounded at fixed \(n\). A finite endpoint before \(T\) cannot be an escape endpoint. This verifies the claimed existence and uniqueness throughout \([0,T]\).

## 3. Reference regularity and quadrature for all five slow equations

The differentiation identities (10) and (11) are correct. In particular,
\[
 (h^{(1)})'=D_1^2(W^{(2)})^{\mathsf T}\delta^{(2)}
\]
has two factors of \(D_1\), and
\[
 ((W^{(3)})')^{\mathsf T}\delta^{(3)}
 =h^{(2)}\|\delta^{(3)}\|_2^2/n.
\]
Neither term is omitted or rescaled.

For explicit normalized velocity bounds, take
\[
\begin{aligned}
 V_x&=P_2Q,&
 V_2&=c^2Q+P_2V_x,&
 V_3&=c^2U+P_3V_2,\\
 V_{\delta3}&=c+2UV_3,&
 V_q&=cU^2+P_3V_{\delta3},&
 V_{\delta2}&=V_q+2RV_2.
\end{aligned}
\]
Then \(x^{(1)},h^{(1)}\) have velocity bound \(V_x\); \(z^{(2)},h^{(2)}\) have bound \(V_2\); and \(z^{(3)},h^{(3)}\) have bound \(V_3\). The differentiated formulas for \(\delta^{(3)},q^{(2)}\), using \(|\phi''|\le2\), give \(V_{\delta3},V_q\).

No derivative of \(\tau\) is needed. For any two times, subtracting its two factors gives
\[
 \frac{\|\delta^{(2)}(s)-\delta^{(2)}(t)\|_2}{\sqrt n}
 \le \frac{\|q^{(2)}(s)-q^{(2)}(t)\|_2}{\sqrt n}
       +2R\frac{\|z^{(2)}(s)-z^{(2)}(t)\|_2}{\sqrt n}
 \le V_{\delta2}|s-t|.
\]
This also locates the essential fixed-clipping dependence in the reference time regularity.

The five right sides in (13) have, in the order written there, valid time-Lipschitz constants
\[
\begin{aligned}
 L_a&=V_{\delta2},\\
 L_{M2}&=cV_{\delta2}+QV_x,\\
 L_{M3}&=cV_{\delta3}+UV_2,\\
 L_{\rm mem}&=cQ^2+J_2V_{\delta2},\\
 L_4&=V_3.
\end{aligned}
\]
For example, \(\|M^{(2)}(s)-M^{(2)}(t)\|_{\rm F}\le cQ|s-t|\); multiplying this difference by a vector of normalized size \(Q\) yields the first term in \(L_{\rm mem}\). The other term uses the bounded operator norm of the learned matrix and the time difference of \(\delta^{(2)}\). The rank-one identity gives the two matrix-product constants.

For any of these right sides \(f\), the exact reference step is
\[
 y(s_{k+1})-y(s_k)=\eta f(s_k)+\rho_k.
\]
For vector variables, \(\frac{\|\rho_k\|_2}{\sqrt n}\le L_f\eta^2/2\); for matrix variables, \(\|\rho_k\|_{\rm F}\le L_f\eta^2/2\). Both bounds follow by integrating the corresponding Lipschitz estimate: \(\int_0^\eta L_f t\,dt=L_f\eta^2/2\).

Thus the claimed local quadrature error applies to every slow variable, including the full returned memory. It compares continuous reference integrals with left-endpoint sums; it does not assert their equality. It also places no time-regularity requirement on the query errors or the hatted trajectory.

## 4. Filter contraction, simultaneous causality, and warmup

Use \(A_k,B_k,C_k,E_k,D_k\) as defined in the candidate, and write \(A_k^*=\max_{j\le k}A_j\), with analogous notation for \(B,C\). Initially
\[
 A_0=E_0=0,\qquad B_0+C_0=d_0.
\]
Subtracting the reference value at the next time from the bottom filter gives the exact error decomposition
\[
\begin{aligned}
 \widehat x_{k+1}^{(1)}-x^{(1)}(s_{k+1})
 ={}&(1-p)(\widehat x_k^{(1)}-x^{(1)}(s_k))\\
 &+p\big[(W_0^{(2)})^{\mathsf T}
                 (\widehat a_k^{(2)}-a^{(2)}(s_k))
       +\widehat R_k^{(1)}-R^{(1)}(s_k)+e_{T,k}^{(2)}\big]\\
 &-\big[x^{(1)}(s_{k+1})-x^{(1)}(s_k)\big].
\end{aligned}
\]
Identity (4) justifies this decomposition. In particular, the final reference increment is not multiplied by \(p\); (14) correctly bounds it by \(V_x\eta\).

For a scalar recurrence with coefficient \(1-p\), the sums controlling these two types of forcing are
\[
 \sum_{r=0}^{m-1}p(1-p)^r\le1,\qquad
 \eta\sum_{r=0}^{m-1}(1-p)^r\le\eta/p=\varepsilon.
\]
These are valid also at \(p=1\). Therefore
\[
 A_k^*\le (M+1)D_k+b+\varepsilon V_x.
\]
The layer-two target difference is at most \(P_2A_k+cE_k+b\), because
\[
\begin{aligned}
 &(W_0^{(2)}+\widehat M_k^{(2)})\widehat h_k^{(1)}
 -(W_0^{(2)}+M^{(2)}(s_k))h^{(1)}(s_k)\\
 &=(W_0^{(2)}+\widehat M_k^{(2)})
          (\widehat h_k^{(1)}-h^{(1)}(s_k))
   +(\widehat M_k^{(2)}-M^{(2)}(s_k))h^{(1)}(s_k).
\end{aligned}
\]
The activation difference is bounded by \(A_k\) in normalized norm. Applying the same geometric sums, now with the reference \(z^{(2)}\) increment, gives
\[
 B_k^*\le B_0+P_2A_k^*+cD_k+b+\varepsilon V_2.
\]
At layer three the corresponding calculation gives
\[
 C_k^*\le C_0+P_3B_k^*+cD_k+b+\varepsilon V_3.
\]
Successive substitution proves
\[
 A_k^*+B_k^*+C_k^*
 \le K_{S,M}(D_k+b+\varepsilon+d_0).
\]
This verifies (14)--(18). The order of substitution is triangular: bottom filter, layer two, layer three. Backward-query feedback is handled through the slow states in the next part. No inequality requiring a small instantaneous feedback coefficient, and no term involving \(D_{k+1}\), is being absorbed here.

The initial layer errors persist in these upper bounds as \(B_0,C_0\), without amplification by \(1/\varepsilon\). No exact-forward initialization has been assumed.

## 5. Closure of all slow-state errors

At a fixed step, let \(w_k,m_{2,k},m_{3,k}\) denote the normalized readout error and the two Frobenius matrix errors; each is a component of \(E_k\). Let \(g_{3,k},g_{q,k},g_{2,k}\) denote the normalized differences in \(\delta^{(3)},q^{(2)},\delta^{(2)}\), respectively. Direct subtraction yields
\[
\begin{aligned}
 g_{3,k}&\le w_k+2UC_k,\\
 g_{q,k}&\le P_3g_{3,k}+Um_{3,k}+b,\\
 g_{2,k}&\le g_{q,k}+2RB_k.
\end{aligned}
\]
The first inequality uses the coordinate bound on the readout, not its Euclidean norm as a coordinate multiplier. The second uses a trained operator norm and a Frobenius matrix difference acting on a vector of normalized size at most \(U\). The third uses the fixed clipping bound. These verify (19)--(20) with width-independent constants.

The differences of the five slow right sides have the following respective bounds:
\[
\begin{aligned}
 &g_{2,k},\\
 &c\,g_{2,k}+Q A_k,\\
 &c\,g_{3,k}+U B_k,\\
 &Qm_{2,k}+J_2g_{2,k},\\
 &C_k.
\end{aligned}
\]
For the returned memory, the decomposition is exactly the one in (21); both the learned matrix error and the backward-field error occur. These estimates cover every right side of the simultaneous slow updates.

Combining their sum with the reference quadrature bounds gives constants \(L_1,L_2\), depending only on \(S,M,R\), such that
\[
 E_{k+1}\le E_k+
 L_1\eta(E_k+A_k+B_k+C_k+b)+L_2\eta^2.
\]
The filter estimate therefore gives, after increasing a constant \(L=L_{S,M,R}\),
\[
 E_{k+1}\le E_k+
 L\eta(D_k+f),\qquad
 f=b+\varepsilon+d_0+\eta.
\]
For any \(i\le k\), summing from \(E_0=0\) gives
\[
 E_i\le L\eta\sum_{j<i}D_j+Li\eta f
 \le L\eta\sum_{j<k}D_j+LTf.
\]
Taking the maximum establishes (23). With \(H=LTf\), induction proves
\[
 D_k\le H(1+L\eta)^k.
\]
Indeed substituting \(D_j\le H(1+L\eta)^j\) into (23) gives
\[
 H+L\eta H\sum_{j<k}(1+L\eta)^j=H(1+L\eta)^k.
\]
Since \(k\eta\le T\), this is at most \(He^{LT}\). Substitution in the filter bound proves (9), including the maximum over the last time \(k=N\). All needed queries have indices \(k<N\), as assumed in (6).

The only exponential obtained is \(e^{L_{S,M,R}T}\). The constant \(L\) has no dependence on \(\varepsilon,\eta,n,b,d_0\), or on the choice of \(\tau\) satisfying (1). Thus there is no hidden exponential in \(1/\varepsilon\). Dependence on the fixed clipping level remains allowed and necessary for this proof.

## 6. Warmup, reconstructed forward fields, and scope

For the displayed warmup construction,
\[
 B_0=\frac{\|e_0^{(2)}\|_2}{\sqrt n},\qquad
 C_0\le M\frac{\|e_0^{(2)}\|_2}{\sqrt n}
             +\frac{\|e_0^{(3)}\|_2}{\sqrt n}.
\]
This proves the stated bound for \(d_0\). In a convergence application, small warmup query errors give \(d_0\to0\), and eventually the required \(d_0\le1\). If \(d_0\) instead stays positive, (9) remains an error bound with that term; uniform convergence including time zero cannot be concluded. The theorem correctly retains this initialization term.

To verify the reconstruction statement, define
\[
 \widetilde z_k^{(2)}
 =(W_0^{(2)}+\widehat M_k^{(2)})
        \phi(F^{-1}(\widehat x_k^{(1)})).
\]
The same target subtraction used above gives
\[
 \frac{\|\widehat z_k^{(2)}-\widetilde z_k^{(2)}\|_2}{\sqrt n}
 \le B_k+P_2A_k+c\,m_{2,k},
\]
which proves (24). For a fully reconstructed third layer, set
\[
 \widetilde z_k^{(3)}
 =(W_0^{(3)}+\widehat M_k^{(3)})
                      \phi(\widetilde z_k^{(2)}).
\]
First,
\[
 \frac{\|\widehat z_k^{(3)}
 -(W_0^{(3)}+\widehat M_k^{(3)})\phi(\widehat z_k^{(2)})\|_2}{\sqrt n}
 \le C_k+P_3B_k+c\,m_{3,k}.
\]
Then 1-Lipschitzness of \(\phi\) gives
\[
 \frac{\|\widehat z_k^{(3)}-\widetilde z_k^{(3)}\|_2}{\sqrt n}
 \le C_k+P_3B_k+c\,m_{3,k}
       +P_3\frac{\|\widehat z_k^{(2)}-\widetilde z_k^{(2)}\|_2}{\sqrt n}.
\]
Thus both reconstructed constraint discrepancies tend to zero when the right side of (9) tends to zero. Their vanishing is derived; it is not imposed on the registers during the updates.

The uncut caveat is also correct. Without fixed clipping, subtraction of the lower backward fields retains
\[
 [\phi'(\widehat z^{(2)})-\phi'(z^{(2)})]\odot q^{(2)}.
\]
A normalized Euclidean bound on \(q^{(2)}\) does not give a width-independent Lipschitz coefficient for this expression in the normalized preactivation error. For example, take
\[
 q^{(2)}=\sqrt n\,e_1,\qquad z^{(2)}=0,\qquad \widehat z^{(2)}=e_1.
\]
Then \(\frac{\|q^{(2)}\|_2}{\sqrt n}=1\), \(\frac{\|\widehat z^{(2)}-z^{(2)}\|_2}{\sqrt n}=1/\sqrt n\), but
\[
 \frac{\|[\phi'(\widehat z^{(2)})-\phi'(z^{(2)})]\odot q^{(2)}\|_2}{\sqrt n}=1/2.
\]
This is an algebraic demonstration of the insufficiency of that norm bound, not a claim of a dynamical counterexample. Fixed \(R\) supplies precisely the missing bounded coordinate multiplier in (12) and (20). The earlier uniform state bounds alone cannot replace it.

The candidate expressly declines uniformity as \(R\to\infty\), an uncut global or population theorem, restartability, and exact raw-GD convergence. It also correctly separates state estimates from filter-register derivative estimates, whose forcing is divided by \(\varepsilon\). No hidden-velocity, kernel, or physical-clock convergence is established by this standalone result.

The probabilistic companion is only a possible future supplier of inputs satisfying (6) and of vanishing initialization and mesh errors. No claim from it is needed for any displayed step above. A combined full-chain audit remains separate from this PASS.

## Required fixes

None. All claims of the deterministic fixed-clipping bridge withstand reconstruction under their stated hypotheses.

## Optional suggestions

1. In the concluding convergence prose, explicitly write \(b+\varepsilon+\eta+d_0\to0\), with \(S,M,R\) fixed. This makes the already necessary vanishing-warmup condition immediately visible when reading that paragraph alone; it does not change (9).
2. Consider displaying the strict-index double sum for \(\widehat R_k^{(1)}\) alongside its continuous double integral. The recursions already encode both correctly, but this identity would help preserve the pre-step convention in later uses of the bridge.
