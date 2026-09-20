# Small physical forcing: a growing-horizon obstruction

This is an independent, prompt-only theoretical route. Its scientific inputs are exactly the model and assumptions in the assignment. No other study material, numerical evidence, or external theorem is used. The conclusions below concern arbitrary admissible forcing paths, and do not construct a fitting algorithm or prove that the reference flow has positive limiting loss.

**Result.** For a fixed initial state and bounded marks, physical forcing of size at most \(\varepsilon\) stays close to exact population gradient flow through a time of order \((\log(1/\varepsilon))^{2/5}\). Consequently, if that reference flow has positive limiting loss, fitting below any fixed smaller loss cannot occur in \(O(\log\log(1/\varepsilon))\) time, or on any smaller diverging scale. A fixed exponential loss tail beginning after such a delay is also impossible under that positive-loss assumption.

## 1. Model and exact gradients

The two population measures are probability measures. The fixed marks satisfy \(b_1\in\mathbb R^{p_1}\), \(b_2\in\mathbb R^{p_2}\), and \(|b_j|\le B_j\) almost surely. The state is
\[
 S=(w,c,M)\in\mathcal H
 =L^2(\lambda_1;\mathbb R^d)\oplus L^2(\lambda_2)\oplus\mathbb R^{p_2\times p_1},
\]
with the sum-of-squares Hilbert norm, using the Frobenius norm in the last component. For finitely many data points, \(\mu_i>0\), \(\sum_i\mu_i=1\), \(|y_i|\le1\), and \(|u_i|\le1\). Write
\[
 \phi=\tanh,\quad
 a_i=\mathbb E_1[b_1\phi(w\cdot u_i)],\quad
 z_i=b_2^TMa_i,\quad H_i=\phi(z_i),\quad
 f_i=\mathbb E_2[cH_i],
\]
\[
 r_i=f_i-y_i,\qquad
 L(S)=\sum_i\mu_i r_i^2,\qquad F=-\nabla_{\mathcal H}L.
\]
Set \(K=B_1B_2\). Only the elementary bounds
\[
 |\phi|\le1,\qquad |\phi'|\le1,\qquad |\phi''|\le2
\]
are used. In particular, \(|a_i|\le B_1\) and \(|f_i|\le\|c\|_2\).

Define the finite vector
\[
 q_i=\mathbb E_2[c\phi'(z_i)b_2].
\]
The three components of \(g_i=\nabla_{\mathcal H}f_i\) are
\[
 (g_i)_w=\phi'(w\cdot u_i)u_i\,b_1^TM^Tq_i,
 \qquad (g_i)_c=H_i,
 \qquad (g_i)_M=q_i a_i^T.
 \tag{1}
\]
Thus
\[
 F(S)=-2\sum_i\mu_i r_i(S)g_i(S).                 \tag{2}
\]

These are genuine Fréchet first derivatives in the stated physical space. To see the potentially delicate part, the scalar Taylor remainder gives
\[
 \left|a_i(w+h)-a_i(w)
 -\mathbb E_1[b_1\phi'(w\cdot u_i)(h\cdot u_i)]\right|
 \le B_1\|h\|_2^2.
\]
The finite vector \(a_i\) then enters finite matrix multiplication. Bounded \(b_2\) makes the resulting change of \(z_i\) uniformly bounded in the second population. Applying the same Taylor estimate there, and Cauchy–Schwarz to integration against \(c\), proves (1), including simultaneous perturbations of all three state components. Cross terms are quadratic on each bounded state ball. The estimates below also show continuity of these first derivatives.

No claim that the nonlinear map \(w\mapsto\phi(w\cdot u_i)\) is twice continuously Fréchet differentiable from \(L^2\) to \(L^2\) is needed or made. In particular, the formal pointwise second derivative would contain products of two arbitrary \(L^2\) perturbations; these need not lie in \(L^2\).

## 2. Explicit polynomial local Lipschitz bounds

Suppose \(\|S\|,\|T\|\le R\), put \(\delta=S-T\), and define
\[
 Z_R=K(1+R),\qquad
 A_R=1+KR(1+R),\qquad
 J_R=2K(1+R)^2(1+KR).
 \tag{3}
\]
The following bounds are uniform in the data index:
\[
 \|g_i(S)\|\le A_R,\qquad
 |f_i(S)-f_i(T)|\le A_R\|\delta\|,\qquad
 \|g_i(S)-g_i(T)\|\le J_R\|\delta\|.
 \tag{4}
\]

Here is a direct proof with the constants exposed. Writing \(\delta w,\delta c,\delta M\) for the three components, one has
\[
 |a_i(S)-a_i(T)|\le B_1\|\delta w\|_2,
\]
\[
 \|z_i(S)-z_i(T)\|_\infty
 \le K\bigl(R\|\delta w\|_2+\|\delta M\|_F\bigr)
 \le Z_R\|\delta\|.
 \tag{5}
\]
Consequently \(\|H_i(S)-H_i(T)\|_2\le Z_R\|\delta\|\). Also
\[
 |q_i(S)|\le B_2R,\qquad
 |q_i(S)-q_i(T)|\le B_2(1+2RZ_R)\|\delta\|.
 \tag{6}
\]
The three gradient norms in (1) are at most \(KR^2,1,KR\), respectively. Their sum proves the first bound in (4). Splitting the change of \(f_i=\mathbb E_2[cH_i]\) proves its second bound.

For the third bound put \(Q_R=1+2RZ_R\). Splitting each product in (1) and using \(|\phi'(s)-\phi'(t)|\le2|s-t|\) gives
\[
 \|\Delta(g_i)_c\|_2\le Z_R\|\delta\|,
\]
\[
 \|\Delta(g_i)_M\|_F\le K(Q_R+R)\|\delta\|,
\]
\[
 \|\Delta(g_i)_w\|_2
 \le K(2R^2+R+RQ_R)\|\delta\|.
\]
Summing these bounds gives exactly \(J_R\) in (3).

Since \(|r_i|\le R+1\), (2) and (4) yield the ordinary two-sided Lipschitz estimate
\[
 \|F(S)-F(T)\|
 \le D_R\|S-T\|,
 \qquad D_R=2\bigl[A_R^2+(R+1)J_R\bigr].
 \tag{7}
\]
In particular,
\[
 D_R\le 2(1+K)(1+3K)(1+R)^4,
 \tag{8}
\]
because \(A_R\le(1+K)(1+R)^2\) and
\(J_R\le2K(1+K)(1+R)^3\). Also
\(\|F(S)\|\le2(R+1)A_R\) on this ball. None of these constants depends on the number of data points, population support size, or ambient dimension beyond the stipulated mark and input bounds.

## 3. Energy and state control under forcing

Fix \(S_0\in\mathcal H\), with \(L_0=L(S_0)\le1\), and let
\[
 \dot S=F(S),\qquad
 \dot S_\varepsilon=F(S_\varepsilon)+v_\varepsilon(t),\qquad
 S(0)=S_\varepsilon(0)=S_0,
 \tag{9}
\]
where \(v_\varepsilon\) is a strongly measurable forcing with
\(\|v_\varepsilon(t)\|\le\varepsilon\) for almost every time. The estimates also apply directly to any absolutely continuous solution whose realized forcing satisfies this inequality.

For completeness, (7) and the ball bound for \(F\) provide local existence and uniqueness for every given bounded measurable forcing: on a sufficiently short interval the map
\[
 X\longmapsto S_0+\int_0^t F(X(s))\,ds+\int_0^t v_\varepsilon(s)\,ds
\]
maps a closed uniform ball of continuous paths into itself and decreases uniform distances by the factor \(TD_R<1\). Iteration has geometrically decreasing successive differences, converges uniformly to a solution, and gives uniqueness by the same integral distance estimate. The bounds proved next prevent finite-time escape. On any bounded time interval the state remains in a fixed ball, and its derivative is bounded by the corresponding bound on \(F\), plus \(\varepsilon\); it therefore has a limit at a finite endpoint and the local construction extends it. This proves global existence for a prescribed forcing. For a feedback rule with unspecified regularity, this argument makes no claim of existence or uniqueness of that closed-loop rule; it applies to every solution that exists.

The first-derivative chain rule gives, almost everywhere,
\[
 \frac d{dt}L(S_\varepsilon)
 =-\|\nabla L(S_\varepsilon)\|^2
   +\langle\nabla L(S_\varepsilon),v_\varepsilon\rangle
 \le \frac{\varepsilon^2}{4}.
\]
The last inequality is \(-a^2+\varepsilon a\le\varepsilon^2/4\). Hence
\[
 L(S_\varepsilon(t))\le L_0+\varepsilon^2t/4.
 \tag{10}
\]
The chain rule is valid along these paths because \(L\) is continuously Fréchet differentiable and Lipschitz on bounded balls, and the paths are absolutely continuous with bounded derivative on compact intervals.

A useful sharper length estimate follows by substituting
\(\nabla L=v_\varepsilon-\dot S_\varepsilon\):
\[
 L(S_\varepsilon(t))+\int_0^t\|\dot S_\varepsilon\|^2
 =L_0+\int_0^t\langle v_\varepsilon,\dot S_\varepsilon\rangle.
\]
If \(U^2=\int_0^t\|\dot S_\varepsilon\|^2\), nonnegativity of loss and Cauchy–Schwarz imply
\(U^2\le L_0+\varepsilon\sqrt t\,U\). Solving this quadratic and bounding length by \(\sqrt t\,U\) gives
\[
 \|S_\varepsilon(t)-S_0\|
 \le \frac{\varepsilon t}{2}
       +\sqrt{L_0t+\frac{\varepsilon^2t^2}{4}}
 \le\sqrt{L_0t}+\varepsilon t.
 \tag{11}
\]
For the reference flow, \(L(S(t))\le L_0\) and
\(\|S(t)-S_0\|\le\sqrt{L_0t}\). Put
\[
 R_\varepsilon(t)=\|S_0\|+\sqrt{L_0t}+\varepsilon t,
 \quad
 B_\varepsilon(t)=\sqrt{L_0}+\sqrt{L_0+\varepsilon^2t/4}.
 \tag{12}
\]
Both states lie in the ball of radius \(R_\varepsilon(t)\), and the sum of their square-root losses is at most \(B_\varepsilon(t)\).

## 4. A one-sided estimate improves the time scale

Using only (7) and (11) would give an amplification exponent of order \(T^3\), and therefore a comparison window of order \((\log(1/\varepsilon))^{1/3}\). Squared loss allows an improvement without assuming a second Fréchet derivative.

For any \(S,T\) in the radius-\(R\) ball, the following one-sided inequality holds:
\[
 \langle S-T,F(S)-F(T)\rangle
 \le J_R\bigl(\sqrt{L(S)}+\sqrt{L(T)}\bigr)\|S-T\|^2.
 \tag{13}
\]
To prove it, put \(\delta=S-T\) and \(\Delta f_i=f_i(S)-f_i(T)\). Integrating the first derivative along the segment between \(T\) and \(S\), which stays in the same ball, gives
\[
 \langle g_i(S),\delta\rangle=\Delta f_i+e_i^S,
 \qquad
 \langle g_i(T),\delta\rangle=\Delta f_i+e_i^T,
\]
\[
 |e_i^S|,|e_i^T|\le\tfrac12J_R\|\delta\|^2.
\]
For example the first remainder is the integral of
\(\langle g_i(S)-g_i(T+s\delta),\delta\rangle\); (4) bounds it by
\(J_R\|\delta\|^2\int_0^1(1-s)\,ds\). Substituting into (2) gives the exact identity
\[
 \langle\delta,F(S)-F(T)\rangle
 =-2\sum_i\mu_i(\Delta f_i)^2
  -2\sum_i\mu_i(r_i(S)e_i^S-r_i(T)e_i^T).
\]
Dropping the nonpositive square term and applying
\(\sum_i\mu_i|r_i|\le\sqrt L\) proves (13). Crucially, this uses losses at the two endpoints, not an unproved loss bound along the intervening segment.

Let \(d_\varepsilon(t)=\|S_\varepsilon(t)-S(t)\|\) and
\[
 a_\varepsilon(t)=J_{R_\varepsilon(t)}B_\varepsilon(t).
\]
Equation (13) gives the scalar differential comparison
\[
 d_\varepsilon(t)
 \le\varepsilon\int_0^t
       \exp\left(\int_s^t a_\varepsilon(r)\,dr\right)ds
 \le\varepsilon t\exp\left(\int_0^t a_\varepsilon(r)\,dr\right).
 \tag{14}
\]
One can verify this without dividing by a possibly zero distance: differentiate
\(\sqrt{d_\varepsilon^2+\eta^2}\), bound its derivative by
\(a_\varepsilon\sqrt{d_\varepsilon^2+\eta^2}+\varepsilon\), multiply by
\(\exp(-\int_0^t a_\varepsilon)\), integrate, and let \(\eta\downarrow0\).

The same comparison controls the observables. Cauchy–Schwarz in the data weights and (4) give
\[
 \max_i|f_i(S_\varepsilon(t))-f_i(S(t))|
 \le A_{R_\varepsilon(t)}d_\varepsilon(t),
\]
\[
 |L(S_\varepsilon(t))-L(S(t))|
 \le B_\varepsilon(t)A_{R_\varepsilon(t)}d_\varepsilon(t).
 \tag{15}
\]

Here is an explicit convenient growing horizon. Define constants depending only on the fixed initialization and mark bounds:
\[
 b=\|S_0\|+3,\qquad
 C_* =\max\{1,\,6K(1+K)b^3\}.
 \tag{16}
\]
If \(T\ge1\) and \(\varepsilon\sqrt T\le1\), then for every \(t\le T\),
\[
 1+R_\varepsilon(t)\le b\sqrt T,\qquad
 B_\varepsilon(t)<3,\qquad
 a_\varepsilon(t)\le C_*T^{3/2}.
\]
The first inequality follows from
\(\varepsilon T\le\sqrt T\); the second uses \(L_0\le1\) and
\(\varepsilon^2T\le1\); the third uses (3). Thus
\[
 \sup_{t\le T}d_\varepsilon(t)
 \le\varepsilon T e^{C_*T^{5/2}},
 \tag{17}
\]
\[
 \sup_{t\le T}|L(S_\varepsilon(t))-L(S(t))|
 \le3(1+K)b^2\varepsilon T^2e^{C_*T^{5/2}}.
 \tag{18}
\]
For all sufficiently small \(0<\varepsilon<1\), choose
\[
 T_\varepsilon=
 \left(\frac{\log(1/\varepsilon)}{2C_*}\right)^{2/5}.
 \tag{19}
\]
It satisfies the two conditions on \(T\). Equations (17)–(18) become
\[
 \sup_{t\le T_\varepsilon}\|S_\varepsilon(t)-S(t)\|
 \le\sqrt\varepsilon\,T_\varepsilon\longrightarrow0,
\]
\[
 \sup_{t\le T_\varepsilon}|L(S_\varepsilon(t))-L(S(t))|
 \le3(1+K)b^2\sqrt\varepsilon\,T_\varepsilon^2\longrightarrow0.
 \tag{20}
\]
This is a sufficient comparison scale, not a claim that the exponent \(2/5\) is optimal. It is uniform over all forcing paths obeying the stated physical bound.

## 5. Conditional fitting-time and exponential-tail consequences

Because reference loss is nonincreasing and nonnegative, its limit
\[
 \ell=\lim_{t\to\infty}L(S(t))
\]
exists. **The preceding analysis does not prove \(\ell>0\).** That is a separate assertion about the fixed instance and initialization.

Assume now that \(\ell>0\), and fix any \(q\) with \(0<q<\ell\), independently of \(\varepsilon\). Define the first fitting time
\[
 \tau_\varepsilon(q)=\inf\{t\ge0:L(S_\varepsilon(t))\le q\},
\]
where the infimum of the empty set is infinity. Since \(L(S(t))\ge\ell\) for every \(t\), (20) implies, for every sufficiently small \(\varepsilon\),
\[
 \tau_\varepsilon(q)>T_\varepsilon.
 \tag{21}
\]
The smallness threshold may depend on \(\ell-q\), but the explicit coefficient in (19) does not. In particular an onset or fitting time
\(o((\log(1/\varepsilon))^{2/5})\), including
\(O(\log\log(1/\varepsilon))\), is impossible below this fixed threshold.

For an exponential **loss** tail, suppose the proposed guarantee is
\[
 L(S_\varepsilon(t))\le A e^{-\gamma(t-d_\varepsilon)}
 \quad(t\ge d_\varepsilon),
 \tag{22}
\]
where \(A<\infty\) and \(\gamma>0\) are independent of \(\varepsilon\).
The guarantee implies
\[
 \tau_\varepsilon(q)\le d_\varepsilon+
 \max\{0,\gamma^{-1}\log(A/q)\}.
\]
Thus (22) is incompatible with \(d_\varepsilon=o(T_\varepsilon)\) when
\(\ell>q\). This includes a fixed-rate exponential tail after an honest
\(\log\log(1/\varepsilon)\) delay. Allowing an untracked
\(\varepsilon\)-dependent prefactor can hide a longer delay and is not the same assertion.

If instead “exponential tail” means a **probability** bound on fitting time,
\[
 \mathbb P\{\tau_\varepsilon(q)>d_\varepsilon+s\}
 \le A e^{-\gamma s}\quad(s\ge0),                 \tag{23}
\]
the same conclusion holds whenever the physical forcing bound holds almost surely: (21) makes the left side one at
\(s=T_\varepsilon-d_\varepsilon\), whereas the right side tends to zero if
\(d_\varepsilon=o(T_\varepsilon)\). If the forcing bound holds only on an event
\(\Omega_\varepsilon\) through time \(T_\varepsilon\), then instead
\[
 \mathbb P\{\tau_\varepsilon(q)>T_\varepsilon\}
 \ge\mathbb P(\Omega_\varepsilon).
\]
Consequently (23) is still incompatible with this onset scale if these events have probabilities bounded away from zero. No independence between forcing and the evolving state is needed.

All stochastic statements here are pathwise applications to absolutely continuous trajectories with an almost-everywhere drift bound. Brownian perturbations are not of that form; small diffusion amplitude alone does not verify the hypotheses. Likewise, a perturbation small in coefficient size, a weaker norm, or an average that does not control the physical forcing does not automatically enter this theorem.

If the reference flow has \(\ell=0\), the positive-plateau obstruction does not apply. If a method genuinely achieves the above small-delay fixed exponential tail while satisfying all stated hypotheses, the conditional result rules out \(\ell>0\) for that fixed reference problem. It does not establish an independently existing canonical plateau, nor provide a method attaining the desired tail. Establishing such a plateau or constructing a fitting mechanism remains outside this route.
