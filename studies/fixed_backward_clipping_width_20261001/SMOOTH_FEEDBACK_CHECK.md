# Independent check of the conditional smooth feedback completion

2026-10-01. **Verdict: the training-population feedback implication is
valid under the explicitly stated statistical hypotheses (5)–(7).**
The forced-to-reconstructed velocity comparison and the damping of the
actual conditional mean residual close the claimed all-time state bound.
For each fixed passive query the stated extension is also valid when its
mean-velocity hypothesis is included. The uniform claim over a bounded
query set additionally needs the statistical constants to be uniform over
that set; this should be stated explicitly. No statistical hypothesis is
certified by this report.

## Scope and versions

The complete following versions were read. Previously assigned smooth
setup, fitting, concentration, and restoration inputs remained available.
No mean-map file, bridge review, other study, manuscript, archive,
experiment, or Git history was read. Only this report was written.

| Complete input | Lines | SHA-256 |
|---|---:|---|
| `SMOOTH_FEEDBACK_COMPLETION.md` | 225 | `02b286e70f292f7815ae20dee5017dc5583ba5127ebd71eb95ef03444424ffef` |
| `SMOOTH_CAVITY_ROUTE.md` | 1181 | `9e22c3f455a6c0447a654a9af6154c0a6c38247bacf2f5aaf40a408895982315` |
| `CLIPPED_POPULATION_ROUTE.md` | 237 | `63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082` |

The previously read setup and restoration hashes are respectively
`a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6`
and `71e68a479072501e9fabee0b7f77256858584a9606ddbd993bb145d46470fc43`.
The rigorous-math, canonical-notation with its neural-response reference,
and conjecture-investigation/adversarial-audit instructions were retained.

Reading the full current cavity file does not make this a review of its
new statistical consistency assertions in Sections 8–12. The assigned
question is whether the displayed hypotheses, for the actual own forced
population on the common action, imply the final autonomous comparison.

## 1. Common action and admissible mean histories

The comparison must use one bounded operator
\(\mathscr W_0:\mathcal H_1\to\mathcal H_2\), its actual adjoint,
and one initial first-layer Gaussian root \(A_0\), with
\(\mathcal H_j=L^2(\Omega_j)\). The common-action construction in the
population input supplies this representation. The smooth gate is globally
Lipschitz, so the same integral-iteration construction gives both its
autonomous and prescribed-coefficient flows on these spaces. The smooth
gate can be included directly among the bounded smooth instructions;
no hard-clip inactivity argument is required.

If needed, include the countably many width-indexed forced histories and
their finite Euler approximations in the generating program family.
Finite unions preserve the joint Gaussian-program construction, and the
bounded operator extends to its Hilbert completion. Thus the forced and
autonomous solutions can be represented on one common action before their
distance is taken. This is a choice of the canonical joint construction,
not a consequence of closeness of marginal covariance kernels. Hypotheses
(5)–(7) explicitly concern this own forced population; substituting an
unidentified scalar-law solution would leave a separate identification gap.

The admissibility argument for actual conditional means is correct. On
the finite-width fitting event,
\(\|\dot r_n\|_m\le C\rho_n\), where
\(\rho_n=\|r_n\|_m\). For nonzero labels, a finite-time zero residual
would be an equilibrium reached by a locally Lipschitz autonomous ODE,
contradicting backward local uniqueness. Hence
\(\dot\rho_n\ge-C\rho_n\), which gives the lower bound in (2).
Together with fitting, this yields

\[
s_n(t)\le C_1\bar s(t),\qquad
\bar s(t)=\int_0^t\mathbb E[\rho_n(s)\mid\mathcal G_n],ds.
\]

The constant is independent of width and time. Therefore
\(|v_bd_a|\le C s_n^3\) really does imply
\(|\bar V_{ba}|\le C\bar s^3\). The proof does not reverse Jensen's
inequality. Also \(\bar\tau=1+\bar s\),
\(|\bar K|\le1\), and
\(|\bar r_a|\le\sqrt m\bar\rho\).

Differentiation of \(K,V\), normalized Cauchy–Schwarz, bounded trained
coordinates, and the operator bound give
\(|\dot K|+|\dot V|\le C\rho_n\). The deterministic integrable
fitting envelope justifies differentiating their conditional expectations.
Thus \(\bar K,\bar V\) have the stated activity-coordinate regularity.
This verifies the displayed admissibility conditions; it does not assert
membership in any additional domain imposed by an unread mean-map theorem.

## 2. Forced-to-reconstructed state and velocity comparison

Let \(U=(A,w,v,k)\) be the forced population state. Include the supplied
clock \(\bar\tau\) when writing the controlled vector field. Direct
integration gives
\(\|w\|_\infty\le C\bar s\),
\(\|v_a\|_\infty\le C\bar s^2\), and
\(\|k_a\|_\infty\le1\). Cap contraction and
\(\bar V=O(\bar s^3)\) give
\(\|\ell_a^e\|_2\le C\bar s\) and
\(\|A-A_0\|_2\le C\bar s^2\).
These estimates are independent of the statistical errors.

Reconstruct
\(\mathscr B^0=\mathscr W_0+m^{-1}\sum_bv_b\otimes k_b\),
where \((v\otimes k)h=v\mathbb E_1[kh]\). With
\(K^U_{ba}=\mathbb E_1[k_bh_a]\), the forward discrepancy is exactly

\[
z_a^e-z_a^0=\frac1m\sum_bv_b(\bar K_{ba}-K^U_{ba}).
\]

For the lower carrier, its discrepancy is the sum of
\(\mathscr W_0^*(d_a^e-d_a^0)\) and
\(m^{-1}\sum_bk_b(\bar V_{ba}-\mathbb E_2[v_bd_a^0])\).
Insert \(V^U_{ba}=\mathbb E_2[v_bd_a^e]\) in the latter difference.
Hypothesis (5), the bounded common action, and the joint-gate Lipschitz
bound give an \(O(\epsilon)\) carrier error. The state velocities have
their residual factors outside these maps, so the forced state velocity
differs from the reconstructed velocity controlled by
\((\bar r,\bar\rho,\bar\tau)\) by at most
\(C\bar\rho\epsilon\) in Hilbert norm.

The derivative hypothesis on \(K\) is precisely what is needed for the
prediction velocity. Along the actual forced path,

\[
\partial_t(z_a^e-z_a^0)
=\frac1m\sum_b\bigl[
\dot v_b(\bar K_{ba}-K^U_{ba})
+v_b(\dot{\bar K}_{ba}-\dot K^U_{ba})\bigr].
\]

Its norm is bounded by \(C\bar\rho\epsilon+C e_K\).
Differentiating the reconstructed matrix along the forced state also gives
\(\|\dot z_a^0\|_2\le C\bar\rho\). In
\(\dot f=\mathbb E_2[\dot w\tanh z+w\psi(z)\dot z]\), use
bounded \(w\), \(\dot w/\bar\rho\), and \(\psi'\), plus
Cauchy–Schwarz for the product
\((\psi(z^e)-\psi(z^0))\dot z^0\). This proves (9) with its
stated integrable source. The derivative factor is \(w\psi(z)\),
not its smooth clip.

Changing the state velocity inside \(\dot f^0\) costs another
\(C\bar\rho\epsilon\). One can justify this directly using the
bounded linear velocity formula

\[
\begin{aligned}
Df_a^0(U)[\delta U]
={}&\mathbb E_2[\delta w,g_a^0]
+\mathbb E_2[p_a^0\mathscr B^0(\psi(Au_a)\delta A u_a)]\\
&+\frac1m\sum_b\bigl[
\mathbb E_2[p_a^0\delta v_b]\,\mathbb E_1[k_bh_a]
+\mathbb E_2[p_a^0v_b]\,\mathbb E_1[\delta k_bh_a]\bigr],
\end{aligned}
\]

where \(p_a^0=w\psi(z_a^0)\). Its norm is bounded on the stated
tube. No population-L2 Hessian is used.

Combining these calculations with the assumed mean prediction-velocity
error proves (10), with
\(\|e(t)\|_m\le C(e_f(t)+e_K(t)+\bar\rho(t)\epsilon)\).
For precision, its coefficient \(Q\) also depends on the clock:
write \(Q(U,\bar\tau)\) rather than suppressing that dependence.
The controlled residual identity is valid for arbitrary control
\(\bar r\); it does not require \(\bar r=f^0-y\).

## 3. Damping the conditional mean residual

The forced reconstructed Gram stays close to the initial population Gram:
\(\|\mathscr B^0-\mathscr W_0\|_{\rm op}\le C\bar s^2\)
and \(\|h-h(0)\|_2\le C\bar s^2\) imply a Gram drift at most
\(C\bar s^2\). Thus the stated smaller fixed label threshold keeps
the readout damping strictly positive for both compared states.

Set \(\delta r=\bar r-r_\infty\),
\(R=\|\delta r\|_m\), and let \(D\) be the sum of the state
Hilbert distances and clock distance. Subtracting the residual equations
gives exactly

\[
\begin{aligned}
\partial_t\delta r={}&G(U)\delta r
+[G(U)-G(U_\infty)]r_\infty\\
&+Q(U,\bar\tau)(\bar\rho-\rho_\infty)
+[Q(U,\bar\tau)-Q(U_\infty,\tau_\infty)]\rho_\infty+e.
\end{aligned}
\]

The hidden part of \(G\) is \(O(S^2)\), \(Q=O(S^3)\), and
their state Lipschitz constants are finite on this tube. For the potentially
delicate first-layer residual kernel, the coordinate bound on \(\ell\)
controls the product with the changing activation gate, while the common
action controls the remaining pairing. Thus L2 state distance suffices.

Hypothesis (6) gives
\(|\bar\rho-\rho_\infty|\le R+e_\rho\). After absorbing the
small hidden terms into the Gram damping, the last display proves (12).
It is an inequality for \(\bar r-r_\infty\), not for the forced
predictor residual. The distinction is essential and is respected.

The controlled state comparison gives (11), with zero initial discrepancy
because the action, Gaussian first root, keys, zero values/readout, and
clock one are shared. Integrating the damped inequality first gives

\[
\int_0^tR\le C\int_0^t\rho_\infty D
+C\int_0^t(\|e\|_m+e_\rho).
\]

Substitution into (11) leaves a source \(C\epsilon\) and an integral
coefficient \(C(\bar\rho+\rho_\infty)\). Both activities have a
fixed finite integral. Gronwall proves (13). The convolution form of (12)
also gives the useful additional conclusion
\(\sup_tR(t)\le C\epsilon\): the source errors have L1 norm
\(O(\epsilon)\), and \(D\) is uniformly \(O(\epsilon)\).
Thus the training conditional mean prediction is controlled uniformly
in time as well.

## 4. Passive queries and the exact qualification

For a passive input \(x\), denote the actual conditional mean prediction
by \(\bar f_x(t)=\mathbb E[f_n(t,x)\mid\mathcal G_n]\).
The passive version of the velocity hypothesis must explicitly mean

\[
|\dot{\bar f}_x-\dot f_x^e|\le e_{f,x},\qquad
\int_0^\infty e_{f,x}\le C_x\epsilon.
\]

All predictions start at zero, so this implies
\(\sup_t|\bar f_x-f_x^e|\le C_x\epsilon\).
The passive pairing hypothesis controls
\(f_x^e-f_x^0\), and the common-action forward estimate gives
\(|f_x^0-f_{\infty,M}(x)|\le C_xD\). These three comparisons
prove the fixed-query conclusion. The passive \(K\)-derivative
hypothesis is sufficient for the parallel velocity reconstruction argument,
although the displayed mean-velocity assumption plus the value pairing
bound already suffice for this final passive value comparison.

All deterministic constants above are uniform when \(x\) ranges over a
fixed bounded set. Uniformity of the statistical constants is a separate
premise. To claim the bounded-query integrated theorem, require (5)–(7)
and the last display with one common constant for all such \(x\)
(or with square-integrable query-dependent bounds). Pointwise hypotheses
with unspecified \(C_x\) alone do not establish this uniformity. This
is a quantifier clarification to the last paragraph of Section 4, not a
failure of the fixed-query or training comparison.

Under that uniform premise, combining conditional centered concentration
with the deterministic conditional-mean bias gives the claimed conditional
mean-square root-width estimate. Conditional Markov and the initialization
failure probability then give the fixed-confidence theorem. None of these
steps supplies an all-time moment on the exceptional initialization event.

The core conditional implication therefore passes. Applying it to the
actual model still requires the statistical hypotheses for the correctly
identified common-action forced population, their passive uniformity, and
the separately stated exceptional-event estimate for the stronger
all-initialization target.
