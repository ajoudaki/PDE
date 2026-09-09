# Isolated adversarial review of HARMONIC_FULL_RESPONSE_TEST.md

## Verdict and audit boundary

**CONDITIONAL FINITE-PROGRAM SCOPED PASS.** No required mathematical correction was found in the displayed finite causal program, its fixed-coefficient derivatives, the complete energy identity, the two-update sign tests, or the first-sine calculation. This verdict accepts (5)–(6) as the definition of the finite Gaussian program. It does not certify identification with a width limit, a physical training trajectory, or a canonical continuation. No global-goal completion is certified.

The conditions on this verdict are substantive scope conditions:

- Gaussian source derivatives are ambient, formal slot derivatives of the specified maps, with all selected deterministic coefficients and covariance parameters held fixed.
- The sign counterexample concerns all deterministic formal source directions, including directions outside the support of the attained Gaussian covariance.
- The small-mesh arguments keep the prefix fixed at two updates and the angle fixed. They provide no uniform control as the prefix grows or a positive physical horizon is held fixed.
- The storage identity is an identity. Neither the curvature term nor the bottom-response term has been bounded in a way that gives continuation or a closed storage estimate.

The fixed-prefix source-derivative finiteness proof at candidate lines 174–180 is **valid**, not an invalid Gaussian-integrability argument. A detailed causal proof is supplied below. It needs neither exponential Gaussian moments nor an inverse covariance.

### Input and isolation record

The sole mathematical input was:

/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_FULL_RESPONSE_TEST.md

- Line count: **913**.
- SHA256 before audit: 6a6a49cd1e5c25c4e6884de8dca7d933f54cb3e2d67c8fcd8833b50b87480ae7.
- SHA256 after writing the review: 6a6a49cd1e5c25c4e6884de8dca7d933f54cb3e2d67c8fcd8833b50b87480ae7.
- The candidate was not edited.

No candidate references, other project files, other reviews, or history were opened. No experiments, simulations, computational mathematical tests, agents, or external mathematical sources were used. The candidate's provenance table and assertions about an external contract were not independently verified and do not supply evidence for this verdict.

Procedural material read and used:

1. /etc/codex/skills/solve-math-rigorously/SKILL.md: explicit derivations, hypothesis checks, and verification of nontrivial steps.
2. /etc/codex/skills/investigate-conjectures/SKILL.md: separation of finite identities, sign-counterexample scope, and continuation claims.
3. /etc/codex/skills/investigate-conjectures/references/adversarial-audit.md: adversarial checking of covariance support, complete memory terms, limit order, and failure of a proof route versus failure of a broader theorem.

These were used only as audit procedures. No mathematical model or mathematical evidence was imported from them.

## 1. Equation coverage and claim ledger

Every numbered display was checked. The table distinguishes definitions from their derived consequences.

| Candidate equations | Finding |
|---|---|
| (1)–(4) | Activations and observable are well defined; the harmonic identities and the stated finite-update normalization are internally consistent. The normalization is accepted as part of the prescribed program, not derived from an unread optimizer contract. |
| (5)–(8) | The causal selections are internally well defined on every fixed finite prefix. Both learned matrix actions have the correct transpose and label placement. The involution gives (8). |
| (9)–(11) | Both sample modes are retained. All factors of two, modal derivative conventions, and modal covariances are correct. |
| (12)–(15) | Fixed-coefficient source derivatives, including zero-valued initial roots, are correct. The current block and the unfactored historical identity are correct. |
| (16)–(17) | The complete balance is correct, including all three boundary energies, all mesh corrections, both remaining response terms, and the stated readout-root extension. |
| (18)–(22) | Initial Gaussian moments and every first-update block are correct. Equal attained source values have not been incorrectly identified before differentiation. |
| (23)–(29) | All second-update coefficient blocks, including both initial columns, are correct. The curvature return and learned transpose memory are both present. |
| (30)–(32) | The deterministic remainder orders follow from fixed-prefix moment bounds and the covariance identity (31), including at singular covariances. |
| (33)–(36) | The full quadratic form has the claimed strictly positive direction and an exact strictly negative direction. Both negative current blocks are included. Positivity also survives the mean-forward-sensitivity left test. |
| (37) | These are exactly the two uncontrolled terms retained in (17); no closure follows from the preceding calculations. |
| (S1)–(S4) | The sine first-layer derivative recursion, pre-source term, current-term combination, and mixed derivative are correct. Literal pathwise cancellation fails. |
| (S5)–(S10) | Initial sine moments, exact source derivatives, and both cubic expansions are correct, with justified fifth-order errors after expectation. |
| (S11)–(S12) | The full forward coefficient and its historical/current decomposition are correct. The historical contribution is nonzero and has a favorable sign in this particular label-weighted coefficient. |

No equation in this ledger establishes width-limit identification, a covariance-supported sign counterexample, an arbitrary-horizon response bound, or canonical continuation.

## 2. Definition, transposes, and fixed-prefix finiteness

### 2.1 What is accepted and what is checked

I read the Gaussian sources in (5)–(6) as centered Gaussian sources, consistently with the covariance prescription and the explicit centered initial laws in Section 5. I accept their reuse coefficients \(S,D\) as definitions. I do not require, or infer, a theorem deriving those coefficients from finite width.

The finite increment (3) unrolls to (7):

\[
W_k-W_0=\lambda\sum_{r<k,b}y_b\delta_{rb}\otimes F_{rb}.
\]

With the candidate's normalization, the rank operator and its adjoint act as

\[
(\delta_j\otimes F_j)x=\delta_jE_1[F_jx],
\qquad
(\delta_j\otimes F_j)^*z=F_jE_2[\delta_jz].
\]

Their actions on \(F_i\) and \(\delta_i\) therefore contribute, respectively,

\[
\lambda y_bE_1[F_iF_j]\,\delta_j,
\qquad
\lambda y_bE_2[\delta_i\delta_j]\,F_j,
\quad j=(r,b),\ r<k.
\]

These are exactly the learned terms in \(A_{ij}\) and \(B_{ij}\). The label belongs to the historical sample \(b\) in both cases. There is no same-time learned matrix update. The normalized tensor notation accounts for the \(1/n\) in (3); no factor is lost in (7).

The remaining terms \(S_{ij}=E_1\partial_{\zeta_j}F_i\) and \(D_{ij}=E_2\partial_{\xi_j}\delta_i\) are accepted selections of the finite definition, rather than an unproved transpose-limit assertion.

### 2.2 Causal construction does not contain a circular moment assumption

Suppose the prefix through time \(k-1\) has been constructed. The next selections can be ordered as follows:

1. Construct \(Z^1_k,F_k\) and their formal source derivatives from the already constructed reverse queries \(q_r\), \(r<k\).
2. Select \(A_{k,r}\), \(r<k\), and extend the joint Gaussian forward source using the feature moments \(E_1F_iF_j\).
3. Construct \(Z_k,w_k,\delta_k\) and their forward-source derivatives from these data. In particular, this calculation does not use \(B_{k,r}\).
4. Select \(B_{k,r}\), \(r\le k\), extend the reverse Gaussian source using \(E_2\delta_i\delta_j\), and then construct \(q_k\).

Both covariance matrices are positive semidefinite: their quadratic forms are \(E_1(\sum_i a_iF_i)^2\) and \(E_2(\sum_i a_i\delta_i)^2\). Their restrictions agree with the already selected earlier prefixes by causality. Thus they specify consistent finite Gaussian extensions, including singular ones. An inverse historical covariance is unnecessary.

Independence of the two populations and of the source groups is compatible with these selections: the expectations selecting a group's covariance are deterministic, not shared random coordinates between the populations.

### 2.3 The polynomial derivative bound is valid

For positive finite \(\lambda\), the constants in \(H=1+h\) cancel in each label sum, so on the zero-readout-root law

\[
|w_k|\le 2k\lambda b=k\Delta b,
\qquad
|\delta_{ka}|\le k\Delta b^2.
\]

The candidate's activations, including both alternatives considered later, have bounded derivatives of every fixed order. At a fixed prefix and with \(A\) fixed, the top variation recursion consists of finitely many additions and products of bounded gates, bounded attained \(w_k\), earlier variations, and deterministic coefficients. For any fixed deterministic direction, its top variations \(P,T,u\) are consequently bounded by finite deterministic constants depending on the prefix, coefficients, and direction. The same argument applies at each fixed higher derivative order.

For the bottom population, once the relevant \(B\) coefficients have been selected,

\[
|q_{ka}|\le |\zeta_{ka}|+
\|\ell\|_\infty\sum_{r\le k,b}|B_{ka,rb}|.
\]

For a fixed prefix let \(z=1+\sum_{r,a}|\zeta_{ra}|\). The first derivative equations imply, with finite deterministic constants,

\[
|Q_k|\le c_k\left(1+\max_{r\le k}|R_r|\right),
\qquad
|R_{k+1}|\le c'_k z\left(1+\max_{r\le k}|R_r|\right).
\]

The initial derivative is deterministic. A finite induction therefore bounds every first bottom derivative by a polynomial in \(z\). Differentiating a fixed finite number of further times gives finite sums of products of earlier derivatives, bounded activation derivatives, and the Gaussian factors from \(q_k\). Induction over time and derivative order again yields a polynomial bound. Including the absolute \(G\) coordinates in this envelope, as the candidate does, is harmless but not needed for this bound.

All moments of a finite Gaussian vector with finite covariance exist, even when its covariance is singular. The derivative expectations selecting the next coefficients are thus finite, completing the induction in Section 2.2. This justifies the assertion at candidate lines 174–180.

There is no hidden passage from finite discrete products to a continuum exponential, and no claim that a polynomial degree or its coefficients remain bounded with prefix length. The argument would not by itself prove a continuum response estimate or differentiability with respect to covariance parameters. Those are different claims and are not made here.

The definitions use expectations of pathwise derivatives. No interchange with a varying Gaussian law is needed. If one also wants differentiation under expectation for a fixed-law additive source shift, the same bounds on a bounded neighborhood of the shift provide an integrable polynomial dominating function.

## 3. Symmetry, both modes, and formal initial roots

### 3.1 The involution and modal normalizations

Let \(P_{\mathrm{ex}}\) exchange the two samples. Then \(P_{\mathrm{ex}}Y=-YP_{\mathrm{ex}}\) and \(P_{\mathrm{ex}}C=CP_{\mathrm{ex}}\). Ordinary fields transform by exchange; reverse fields transform by negative exchange; the readout changes sign. The causal construction preserves these transformations, including its Gaussian covariance selections.

In particular, \(E_2w_k=0\), and the two entries of \(E_2[w_kH_k]\) are opposite. Defining their first entry to be \(g_k\) gives (8). Since \(H=1+h\), replacing \(H\) by \(h\) does not change this expectation.

For the half-sum/half-difference transform used in (9), the matrices acting on sample pairs satisfy

\[
Y\longmapsto
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
CY\longmapsto
\begin{pmatrix}0&1+\rho\\1-\rho&0\end{pmatrix}.
\]

This proves the first line of (9). Expanding the product \(\ell'(Z^1)q\) proves the two formulas for \(d^1_\pm\). Expanding \(wp(Z)\), and using \(\lambda(H_1-H_2)=\Delta V^2\), proves its last line.

The response blocks \(A,B\) are odd under simultaneous exchange of their row and column sample indices, so their modal diagonal entries vanish. The learned part of the plus-output/minus-input coupling in \(A\), for example, is

\[
\lambda E_1[(F_{k1}+F_{k2})F_{r1}]
=2\lambda E_1[U^1_kU^1_r]
=\Delta E_1[U^1_kU^1_r].
\]

The other learned terms in (10) follow with the same normalization and the corresponding minus or backward fields. For derivatives, the inverse modal transform gives

\[
\partial_{\xi_{r,+}}=\partial_{\xi_{r1}}+\partial_{\xi_{r2}},
\qquad
\partial_{\xi_{r,-}}=\partial_{\xi_{r1}}-\partial_{\xi_{r2}}.
\]

There is no additional half in (10). Applying the half-sum/half-difference transform to the covariance prescription gives (11). Mixed mode covariances vanish by the involution, but independence of evolved nonlinear modes does not follow; the candidate correctly avoids that inference.

At \(\rho=-1\), \(G_+=0\) and the \(1+\rho\) factor makes \(Z^1_{k,+}=0\) on the attained law. This removes neither \(F_+\) nor the formal root slots. All displayed modal formulas remain meaningful without dividing by \(1+\rho\).

### 3.2 Initial roots and complete differentiation

Differentiating the unspecialized recursions gives exactly (12). The two necessary product-rule contributions in the bottom update are

\[
\ell''(Z^1_{kb})q_{kb}R_{kb}
\quad\text{and}\quad
\ell'(Z^1_{kb})Q_{kb}.
\]

At the top, \(p'=-h\) gives \(T_i=p_i u_k-w_kh_iP_i\), and differentiating every readout update gives the accumulated \(u_k\). Expanding the product \(hP\) into modes yields (13), with the indicated cross-mode terms.

The initial identities

\[
\partial_{G_b}F_{0a}=\mathbf1_{a=b}\ell'(G_a),
\quad
\partial_{\zeta_{0b}}q_{0a}=\mathbf1_{a=b},
\quad
\partial_{w_*}\delta_{0a}=p(\xi_{0a})
\]

are correct derivatives of these formal maps. The zero variance of \(\zeta_0\) and the zero attained value of \(w_*\) do not invalidate them. A derivative on the quotient by attained Gaussian support would be a different object.

For a current forward impulse, the past top fields and \(u_k\) do not vary, while \(P_{ka}=\mathbf1_{a=b}\). Hence

\[
D_{ka,kb}=-\mathbf1_{a=b}E_2[w_kh(Z_{ka})]
=-\mathbf1_{a=b}y_ag_k.
\]

There is no current learned transpose term, proving (14). For a general top direction with \(\omega=0\), substitute

\[
u_k=\lambda\sum_{r<k,b}y_bp(Z_{rb})P_{rb}
\]

into \(E_2T_i\) and split \(E_2[w_kh_iP_i]\) into its mean product and covariance. This gives (15) exactly. With \(\omega\ne0\), the additional term is \(\omega E_2p_i\), as stated. No product of evolved fields is incorrectly factored.

## 4. Complete energy identity (17)

For this calculation the bottom directions and readout-root direction are zero. With deterministic \(v=v^\xi\), fixed-coefficient linearity gives

\[
t_i:=E_2T_i=(Dv)_i,
\qquad
(Bv)_i=t_i+
\lambda\sum_{j\prec i}y_bE_2[\delta_i\delta_j]v_j.
\]

Also, \(v_i=P_i-\sum_{j\prec i}A_{ij}T_j\) pathwise. Therefore

\[
\begin{aligned}
\lambda\mathcal Q_B(v)
={}&\lambda\sum_i y_aE_2[P_iT_i]
-\lambda\sum_{j\prec i}y_aA_{ij}E_2[T_iT_j]\\
&+\lambda^2\sum_{j\prec i}y_ay_bv_iv_jE_2[\delta_i\delta_j].
\end{aligned}
\]

Each term in (17) can now be accounted for without a sign assumption.

**Readout and curvature.** Substituting \(T_i=p_i u_k-w_kh_iP_i\) gives

\[
\lambda\sum_i y_aE_2[P_iT_i]
=\sum_kE_2[u_k\delta u_k]
-\lambda\sum_{k,a}y_aE_2[w_kh_iP_i^2].
\]

Because \(u_0=0\), telescoping \(u_{k+1}^2-u_k^2=2u_k\delta u_k+(\delta u_k)^2\) yields precisely the first line of (17) and its curvature line.

**Learned forward memory.** Splitting \(A_{ij}=S_{ij}+\lambda y_bE_1F_iF_j\) produces

\[
-\lambda^2\sum_{j\prec i}y_ay_bE_2[T_iT_j]E_1[F_iF_j].
\]

For \(N\) as defined in (16), this is \(-\sum_kE_{1,2}[N_k\delta N_k]\). Its telescoping identity is

\[
-\frac12E_{1,2}N_{M+1}^2
+\frac12\sum_kE_{1,2}(\delta N_k)^2.
\]

The independent product population is legitimate here: it represents exactly the product of two expectations already present in the deterministic coefficient. It does not assert independence of \(T_i,T_j\) within population 2 or of \(F_i,F_j\) within population 1.

**Learned transpose memory.** The last term in the preceding formula for \(\lambda\mathcal Q_B\) equals \(\sum_kE_2[J_k\delta J_k]\). It telescopes to

\[
\frac12E_2J_{M+1}^2
-\frac12\sum_kE_2(\delta J_k)^2.
\]

**Bottom response.** The remaining part of \(A\) is exactly

\[
-\lambda\sum_{j\prec i}y_aS_{ij}E_2[T_iT_j].
\]

These are all terms in (17), with the displayed signs. The sums over \(r<k\) are strict in time. Squared increments contain both same-sample and cross-sample terms at their common time. Thus no within-time learned term has been silently added or removed.

For \(\omega\ne0\), \(u_0=\omega\) replaces the first boundary energy by \((E_2u_{M+1}^2-\omega^2)/2\). In that case \(E_2T\) is no longer simply \(Dv\), and the modified left side at candidate lines 357–359 is the correct one. The rest of the derivation is unchanged.

Finally,

\[
E_2[w_kh_iP_i^2]
=y_ag_kE_2P_i^2+\operatorname{Cov}_2(w_kh_i,P_i^2).
\]

Dropping that covariance would be unjustified. The last response term retains the full bottom derivative, including \(\ell''qR\). The two terms in (37) are consequently real outstanding terms, not omissions from the identity.

## 5. Initial integrals and all first-update blocks

The identities \(p'=-h\) and \(h^2+p^2=2\varepsilon^2\) in (4) follow directly from \(h=\varepsilon(\sin+\cos)\), \(p=\varepsilon(\cos-\sin)\).

For the centered Gaussian pair \(X\) with covariance \(K\),

\[
\operatorname{Var}(X_1-X_2)=2\chi,
\qquad
E\cos(X_1-X_2)=e^{-\chi}=c.
\]

The identities

\[
p(x)p(z)=\varepsilon^2[\cos(x-z)-\sin(x+z)],
\qquad
h(x)h(z)=\varepsilon^2[\cos(x-z)+\sin(x+z)]
\]

and symmetry of a centered Gaussian kill the sine expectations. Their diagonal specializations have expectation \(\varepsilon^2\). Thus every entry of \(\Gamma\) in (19) is correct, and

\[
E[Dh(X_1)]=\varepsilon^2(1-c)=\kappa,
\qquad E[Dh(X_2)]=-\kappa.
\]

These are raw second moments, as required by (6), not centered activation covariances.

Since \(w_0=\delta_0=B_{00}=\zeta_0=q_0=0\) on the attained law, \(Z^1_1=G\), \(F_1=F_0\), and the covariance prescription implies \(\xi_1=\xi_0=X\) almost surely. Also \(Z_1=Z_0=X\). The source slots remain distinct for differentiation.

The nonzero derivative (21) follows from the first bottom update and gives

\[
A_{10}=\lambda(C\odot J^1)Y+\lambda KY.
\]

A historical \(\xi_{0b}\) impulse differentiates \(w_1\) by \(\lambda y_bp(X_b)\), while its derivative of \(Z_1\) is zero. Hence \(B_{10}=\lambda\Gamma Y\). A current \(\xi_{1b}\) impulse differentiates only the current gate, giving \(B_{11}=-\lambda\kappa Y\). These calculations verify all of (20), including \(w_1=\lambda D\), \(g_1=\lambda\kappa\), and \(\delta_{1a}=\lambda Dp(X_a)\).

The covariance of \(\zeta_1=\lambda\eta\) is the displayed covariance in (22), and \(\eta\) is independent of \(G\). Combining \(B_{10}F_0+B_{11}F_1\) gives

\[
q_1=\lambda\{\eta+(\Gamma-\kappa I)YF\},
\qquad
\Gamma-\kappa I=\varepsilon^2c
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Thus both deterministic query shifts coincide and \(q_{1,-}=\lambda\eta_-\), as claimed. No learned transpose term occurs at these times because it would contain the attained \(\delta_0=0\).

## 6. Every second-update block and its remainder

### 6.1 Forward coefficients, including the initial reverse-root column

The attained second bottom state is (23). For an impulse in \(\zeta_{1b}\), the earlier bottom states do not vary and

\[
\partial_{\zeta_{1b}}Z^1_{2a}=\lambda C_{ab}y_b\ell'(G_b).
\]

Multiplication by the output derivative \(\ell'(\widetilde G_a)\), followed by adding learned forward memory, yields (24).

For the initial reverse root, let \(U=\lambda CY\operatorname{diag}(\ell'(G))\). Differentiating the unspecialized update \(Z^1_2=Z^1_1+\lambda CY\operatorname{diag}(\ell'(Z^1_1))q_1\) gives

\[
\partial_{\zeta_0}Z^1_1=U,
\qquad
\partial_{\zeta_0}q_1=B_{11}\operatorname{diag}(\ell'(G))U,
\]

and therefore

\[
\partial_{\zeta_0}Z^1_2=
\left[I+\lambda CY\operatorname{diag}(\ell''(G)q_1)
+\lambda CY\operatorname{diag}(\ell'(G))B_{11}\operatorname{diag}(\ell'(G))\right]U.
\]

The output gate and learned memory give exactly (25). In particular, the \(I\,U\) term is essential and is present. The candidate has not dropped this column because its attained multiplier \(\delta_0\) is zero.

### 6.2 Reverse coefficients, including the initial forward-root column

The attained formulas \(w_2=2\lambda D\) and \(Z_2=\xi_2+A_{21}\delta_1\) verify (26). They must be differentiated through their original recursions, as the candidate does.

For a \(\xi_{1b}\) impulse,

\[
T_{1c}=-\mathbf1_{c=b}\lambda Dh(X_b),
\quad u_2=\lambda y_bp(X_b),
\quad P_{2a}=-\lambda A_{2a,1b}Dh(X_b).
\]

Thus

\[
E_2T_{2a}
=\lambda y_bE_2[p(Z_a)p(X_b)]
+2\lambda^2A_{2a,1b}E_2[D^2h(Z_a)h(X_b)].
\]

The learned transpose contribution is separately

\[
\lambda y_bE_2[\delta_{2a}\delta_{1b}]
=2\lambda^3y_bE_2[D^2p(Z_a)p(X_b)].
\]

Their sum is all of (28). Both the factor 2 and the positive sign of the curvature-return term follow from \(w_2=2\lambda D\) and the negative sign in \(P_{2a}\). Neither term is factored or omitted.

For a \(\xi_{0b}\) impulse, \(P_1=0\), \(u_1=u_2=\lambda y_bp(X_b)\), and \(T_{1c}=\lambda y_bp(X_c)p(X_b)\). Consequently

\[
P_{2a}=\lambda y_b\sum_cA_{2a,1c}p(X_c)p(X_b),
\]

which gives the first formula of (29) upon substitution in \(T_{2a}\). There is again no learned transpose term involving \(\delta_0\). The current formula in (29) is (14), with \(g_2=2\lambda E_2[Dh(Z_1)]\). Here \(Z=Z_2\), so \(Z_1\) denotes its first sample coordinate, not time 1.

Together with (20), these formulas account for every nonzero causal coefficient block through time 2. The other time blocks are zero by the prescribed causality.

### 6.3 Controlled errors

The law of \(q_1/\lambda\) in (22) has every fixed finite moment bounded independently of small \(\lambda\). Hence

\[
q_1=O_{L^m}(\lambda),
\qquad
\widetilde G-G=O_{L^m}(\lambda^2).
\]

Bounded activation derivatives in (24) give \(A_{21}=\lambda(K+C\odot J^1)Y+O(\lambda^3)\). In (25), \(U=O(\lambda)\); both corrections inside the braces have \(L^m\) size \(O(\lambda^2)\). Thus \(A_{20}=O(\lambda)\), as asserted in (30).

For the jointly selected Gaussian sources, the exact identity

\[
E(\xi_{2a}-X_a)^2
=E_1[\ell(\widetilde G_a)-F_a]^2
\]

is simply the expansion of a squared difference using the three prescribed covariance entries. Lipschitzness bounds it by \(O(\lambda^4)\). A centered scalar Gaussian's fixed moments scale with the corresponding power of its standard deviation, so \(\xi_2-X=O_{L^m}(\lambda^2)\), including if the difference has zero variance. The memory term \(A_{21}\delta_1\) is also \(O_{L^m}(\lambda^2)\). Therefore \(Z-X=O_{L^m}(\lambda^2)\).

Lipschitzness and boundedness of \(h,p,D\) now give

\[
B_{21}=\lambda\Gamma Y+O(\lambda^3),
\qquad
g_2=2\lambda\kappa+O(\lambda^3),
\qquad
B_{22}=-2\lambda\kappa Y+O(\lambda^3).
\]

In particular, the second line of (28) is \(O(\lambda^2)A_{21}=O(\lambda^3)\), and its learned transpose line is \(O(\lambda^3)\) by boundedness. Their inclusion is controlled quantitatively, not justified by an assumed favorable sign. No covariance inverse, Gaussian density derivative, or expansion over a growing prefix is used.

## 7. Both signs of the full label-weighted kernel

Let \(e_-=(1,-1)^T/\sqrt2\), and write \(e_+=(1,1)^T/\sqrt2=Ye_-\). This orthonormal vector convention for the test is distinct from the half-sum convention for field coordinates in Section 3; the candidate uses both correctly.

For \(v_0=0\), \(v_1=v_2=e_-\), the complete pairing is

\[
\begin{aligned}
\mathcal Q_B(v)
&=e_-^TYB_{11}e_-+e_-^TYB_{21}e_-+e_-^TYB_{22}e_-\\
&=-\lambda\kappa
+\lambda e_+^T\Gamma e_+
-2\lambda\kappa+O(\lambda^3)\\
&=\lambda\varepsilon^2(4c-2)+O(\lambda^3).
\end{aligned}
\]

The historical eigenvalue is the average-gate eigenvalue \(\varepsilon^2(1+c)\), not the difference-gate eigenvalue. Both negative current contributions have been included. The initial columns have been defined and checked; their contractions vanish because \(v_0=0\).

For \(\ell=1+\frac1{10}\arctan\), Lipschitzness gives

\[
\chi=\frac12E(F_1-F_2)^2
\le\frac1{200}E(G_1-G_2)^2
=\frac{1-\rho}{100}\le\frac1{50}.
\]

Strict monotonicity and the positive variance of \(G_1-G_2\) give \(\chi>0\) for every fixed \(\rho<1\), including \(\rho=-1\). Since \(e^{-x}\ge1-x\), \(c\ge49/50\) and

\[
\varepsilon^2(4c-2)\ge\frac1{400}\frac{48}{25}
=\frac3{625}>0.
\]

If the remainder is bounded by \(C_\rho\lambda^3\), choose \(\lambda\) so that \(C_\rho\lambda^2\) is less than half the positive leading coefficient. This makes the full form strictly positive. This is an analytic existence argument for a sufficiently small mesh; it does not require a numerical threshold.

For the negative direction set only \(v_1=e_-\) nonzero, keeping the same full prefix. Although the output at time 2 can be nonzero, its left test vector is zero. Thus

\[
\mathcal Q_B(v)=e_-^TYB_{11}e_-=-\lambda\kappa<0
\]

exactly. Hence the quadratic form, equivalently the symmetric part of the time-block matrix with blocks \(YB_{kr}\), is indefinite. This is not a statement that the nonsymmetric causal matrix must have eigenvalues of both signs.

The alternative \(\ell=\arctan\), \(\rho=3/4\), gives \(0<\chi\le1/4\), \(c\ge3/4\), and a leading coefficient at least \(\varepsilon^2\). The same two-direction argument applies at that fixed angle.

For the mean-forward-sensitivity left test, averaging \(P_2=v_2+A_{21}T_1\) gives precisely

\[
x_1=v_1,
\qquad
x_2=v_2-\lambda\kappa A_{21}Yv_1=v_2+O(\lambda^2).
\]

Since \((Bv)_1,(Bv)_2=O(\lambda)\), this substitution changes the form by \(O(\lambda^3)\). Its positive sign persists. The stronger upper bound by current damping alone also fails for this same test.

### 7.1 Support restriction is essential

The scope caveat can be sharpened: **the displayed positive test is outside the support of the attained joint Gaussian source law**, not merely potentially outside it. The exact identity \(\xi_1=\xi_0\) forces every vector in that joint support to satisfy \(v_1=v_0\). Test (33) has \(v_1=e_-\) and \(v_0=0\), so it violates that constraint. The same observation applies to the stated single-time-1 negative test.

This does not invalidate either formal derivative or the formal-source quadratic-form counterexample. It does prevent using these directions, without an additional argument, to refute an inequality restricted to covariance-supported or physically induced perturbations. The candidate's explicit support caveats are correct; the stronger observation above is an optional clarification.

### 7.2 Positive source pairing is compatible with storage

There is also a direct leading-order check of compatibility with (17). For the positive test put \(L=(p(X_1)+p(X_2))/\sqrt2\). Then

\[
E_2L^2=\varepsilon^2(1+c),
\quad
\delta u_1=\lambda L,
\quad
\delta u_2=\lambda L+O_{L^2}(\lambda^3),
\quad
u_3=2\lambda L+O_{L^2}(\lambda^3).
\]

The readout boundary energy minus its mesh correction is consequently \(\lambda^2\varepsilon^2(1+c)+O(\lambda^4)\). The curvature term is \(-3\lambda^2\kappa+O(\lambda^4)\). The learned-memory energies and bottom-response term are \(O(\lambda^4)\) on this prefix. Their sum agrees with \(\lambda\mathcal Q_B=\lambda^2\varepsilon^2(4c-2)+O(\lambda^4)\).

Thus the leading positive pairing is fully consistent with readout-sensitivity storage. Neither (34) nor this consistency calculation disproves an estimate retaining readout and matrix-memory energies. Proving such an estimate still requires control of the remaining terms in (17).

## 8. First sine layer: pathwise and averaged pre-source terms

### 8.1 Exact recursion for every angle

For \(\ell=\sin\), a reverse-source impulse in slot \((r,b)\) has \(R_u=0\) for \(u\le r\), with the injection stated before (S1). At later rows, \(\ell''=-F\) and the absence of a direct later injection give exactly

\[
R_{k+1}=R_k-\lambda CY\operatorname{diag}(F_kq_k)R_k
+\lambda CY\operatorname{diag}(p^1_k)
\sum_{r<u\le k}B_{ku}\operatorname{diag}(p^1_u)R_u.
\]

Substituting the full \(q_k\) exposes (S2). The return differentiated through \(F_u\) has no \(u\le r\) contribution, because those derivatives vanish. Their attained features in the undifferentiated \(q_k\) need not vanish. Both product-rule contributions for \(r<u<k\) remain present.

For the current block \(B_{kk}=-g_kY\), its occurrence in \(q_k\) contributes \(+\lambda g_kC\operatorname{diag}(F_k^2)R_k\); its differentiated occurrence contributes \(-\lambda g_kC\operatorname{diag}((p^1_k)^2)R_k\). Their sum is (S3), with the difference \((p^1)^2-F^2=\cos(2Z^1)\). The identity \((p^1)^2+F^2=1\) does not change this difference into a positive constant.

At fixed coefficients, \(R_k,F_k\), and every factor in the differentiated return do not depend, as formal functions, on the current coordinate \(\zeta_k\). This is a statement about slot dependence, not probabilistic independence from a correlated Gaussian source. Therefore differentiating once more gives (S4):

\[
\partial_{\zeta_{kc}}R_{k+1,a}
=-\lambda C_{ac}y_cF_{kc}R_{kc}.
\]

At \(C=I,k=1,r=0,c=a=b\), this is \(-\lambda^2\sin G_a\cos G_a\), nonzero with positive Gaussian probability. Literal pathwise cancellation is ruled out. This alone would not settle cancellation after averaging, which is why the subsequent calculation matters.

### 8.2 Initial sine moments and the exact initial-root derivative

At \(\rho=0\), the independent standard Gaussian roots give

\[
K_0=\frac{1-e^{-2}}2,
\qquad J_0=\frac{1+e^{-2}}2,
\qquad K_0+J_0=1,
\]

and

\[
m_{22}=\frac{1-e^{-8}}8,
\qquad
m_4=\frac{3+4e^{-2}+e^{-8}}8.
\]

These follow by expanding \(\sin^2 G,\cos^2 G,\sin^2G\cos^2G,\cos^4G\) into cosines of \(2G,4G\). The off-diagonal feature moment is zero, so \(\chi=K_0\). All of (S5) is correct.

Equation (22) gives exactly the \(t_a\), \(q_{1a}=\lambda t_a\), and displacement \(Z^1_{2a}=G_a+\lambda^2y_ap_at_a\) in (S6). For sample 2 the sign \(y_2=-1\) turns \(F_2-F_1\) into the same deterministic query shift as for sample 1, as required by (22).

For the formal \(\zeta_{0a}\) derivative, \(F_0\) does not vary, while \(F_1\) does. Hence

\[
R_{1a}=\lambda y_ap_a,
\qquad
\partial_{\zeta_{0a}}q_{1a}
=(-\lambda\kappa y_a)p_a(\lambda y_ap_a)
=-\lambda^2\kappa p_a^2.
\]

Substitution into the bottom product rule gives exactly

\[
R_{2a}=\lambda y_ap_a-\lambda^3F_ap_at_a-\lambda^3y_a\kappa p_a^3.
\]

The attained \(B_{10}F_0\) remains in \(t_a\) despite having zero derivative with respect to this initial reverse slot. This verifies all of (S7) and the relevant zero-variance-root convention.

### 8.3 Full cubic coefficient, including learned forward memory

Write \(d_a=\lambda^2y_ap_at_a\). Bounded second derivatives give

\[
\cos(G_a+d_a)=p_a-\lambda^2y_aF_ap_at_a+O_{L^m}(\lambda^4),
\]

which is (S8). Multiplying by the exact \(R_{2a}\) gives, before averaging,

\[
\cos(Z^1_{2a})R_{2a}
=\lambda y_ap_a^2
-2\lambda^3F_ap_a^2t_a
-\lambda^3y_a\kappa p_a^4
+O_{L^1}(\lambda^5).
\]

The two equal \(t_a\) contributions come from variation of the state and variation of the output gate. Independence of \(\eta\) from \(G\), its zero mean, and the vanishing mean of the other sample's sine imply

\[
E[F_ap_a^2t_a]=y_a\varepsilon^2c\,m_{22}.
\]

This proves (S9), including its factor 2.

The learned forward contribution is not zero. Expanding the sine gives

\[
\lambda y_aE[\sin(G_a+d_a)F_a]
=\lambda y_aK_0
+\lambda^3E[F_ap_a^2t_a]
+O(\lambda^5),
\]

which is (S10). It cancels one, and only one, of the two \(\varepsilon^2c\,m_{22}\) response contributions. Thus the complete coefficient is exactly the asserted expansion

\[
A_{2a,0a}
=\lambda y_a
-\lambda^3y_a[\varepsilon^2c\,m_{22}+\kappa m_4]
+O(\lambda^5).
\]

The remainders follow from \(d_a=O_{L^m}(\lambda^2)\) for every fixed finite \(m\), bounded trigonometric derivatives, and the exact \(R_{2a}=O_{L^m}(\lambda)\). Products of the Taylor remainder with \(R_{2a}\), and the two cubic corrections with the gate displacement, have expectation \(O(\lambda^5)\) by the corresponding finite moments. There is no unproved regularity in a continuum time or a growing prefix.

### 8.4 Attribution in (S12) is correct

Keeping the actual terms of \(q_1=\zeta_1+B_{10}F_0+B_{11}F_1\) separated, their contributions to \(E[F_ap_a^2(q_{1a}/\lambda)]\) are

\[
0\quad\text{from }\eta_a,
\qquad
y_a\varepsilon^2m_{22}\quad\text{from the diagonal of }B_{10},
\qquad
-y_a\kappa m_{22}\quad\text{from }B_{11}.
\]

The historical off-diagonal contribution vanishes because it contains the independent odd factor \(F_b\). The separate differentiated self-return supplies \(\kappa m_4\). After the learned forward cancellation, the net bracket is therefore

\[
\varepsilon^2m_{22}+\kappa(m_4-m_{22})
=\varepsilon^2c\,m_{22}+\kappa m_4.
\]

This proves both the algebra and the historical/current attribution in (S12), without deleting a term or altering the model. The historical quantity \(\varepsilon^2m_{22}\) is strictly positive. Moreover,

\[
m_4-m_{22}=\frac{1+2e^{-2}+e^{-8}}4>0.
\]

Consequently the cubic correction to \(y_aA_{2a,0a}\) is negative. The surviving pre-source contribution is favorable for this one coefficient; it does not establish response growth or obstruct every possible storage estimate.

The learned transpose memory first occurs in \(B_{21}\), which was already retained in the full sign test. \(A_{20}\) is selected before \(q_2\), so that memory cannot supply an omitted contribution to (S11). There is no causal route by which it could retroactively cancel the computed coefficient.

Finally, for this sine choice \(\chi=K_0>0\) and

\[
c\ge1-K_0=\frac{1+e^{-2}}2,
\qquad
\varepsilon^2(4c-2)\ge2\varepsilon^2e^{-2}>0.
\]

The complete positive sign test and the exact negative current-only test therefore both apply at \(\rho=0\). This verifies the additional claim in Section 8.3.

## 9. Required fixes, optional clarifications, and unresolved scope

### Required mathematical fixes

**None within the accepted finite-program scope.** In particular:

- Neither transpose rank memory is missing or transposed incorrectly.
- The modal normalizations and all initial-root derivatives are correct.
- The energy identity has no missing same-time sample term or boundary energy.
- The positive test includes both current blocks and the complete \(B_{21}\); the negative test is exact.
- The fixed-prefix Gaussian source-derivative finiteness proof is valid.
- The two-update remainder estimates and the fifth-order sine remainders are justified.
- The learned forward memory and the pre-source coefficient in (S11)–(S12) are correctly included.

### Optional editorial clarifications

1. **Make the Gaussian support statement sharper** (candidate lines 872–875). For (33), replace “need not lie in the support” by the explicit observation \(\xi_1=\xi_0\) but \(v_1\ne v_0\). This strengthens the existing correct scope caveat without changing the result.
2. **Name the unspecialized recursion when deriving (25)** (lines 481–483). The phrase “differentiating (23) before evaluation” is potentially misleading because (23) has already substituted the attained identity \(Z^1_1=G\). Say that one differentiates \(Z^1_2=Z^1_1+\lambda CY\operatorname{diag}(\ell'(Z^1_1))q_1\) and only then evaluates. The displayed formula (25) already does this correctly.
3. **Spell out the causal order in the finiteness paragraph** (lines 174–180). The argument is correct, but the order \(F_k,A_k,\xi_k,\delta_k,B_k,\zeta_k,q_k\), with derivative selections at the corresponding stages, makes the absence of circular reasoning easier to verify.
4. **State once that the Gaussian source processes are centered.** This is the intended reading used in the initial calculations; making it explicit in Section 2 would remove an avoidable convention from the definition.

These are optional clarifications, not prerequisites for the scoped verdict under the stated reading. No candidate edits were made.

### What remains unproved

The finite result disproves the specified all-formal-source nonpositivity estimate and its current-damping-only strengthening. It also disproves literal pre-source cancellation for the first sine layer, including in the computed averaged coefficient. It does not disprove a covariance-supported forcing estimate, a readout/matrix storage inequality, a favorably controlled pre-source term, or a Catalan/Bessel majorant obtained by some further argument.

The curvature and bottom-response terms in (37) remain uncontrolled. No mesh-uniform or arbitrary-horizon estimate, restart uniqueness, population-limit identification, raw optimizer equivalence, canonical continuation, or later-time nonaffinity/nonfreezing conclusion is established by this candidate or by this review. The external normalization and provenance claims have not been audited against their references.

The procedural skills influenced this review by keeping those claim levels separate and by requiring checks of the full operator and the actual remainder terms. The resulting approval is confined to the explicitly defined finite Gaussian program and the finite calculations verified above.
