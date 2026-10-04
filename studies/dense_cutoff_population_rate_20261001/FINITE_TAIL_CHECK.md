# Independent internal reconstruction of the finite-tail candidate

Date: 2026-10-01. This is an independent internal mathematical check, not a promotion review. The checker did not author the candidate. The assignment was to reconstruct its complete argument, especially transformed dynamics, control-path entropy, cavity normalization, conditional Gaussianity, the all-time maximum, and constants uniform in width and activity.

**Verdict: PASS for the candidate's stated restricted finite-carrier theorem and cutoff-inactivity consequence.** I found no unclosed mathematical step for those claims. The proof requires two hidden layers, orthonormal training inputs, first activation tanh, and bounded second activation with bounded Lipschitz derivative. It does not establish an all-time finite-to-population root-width rate, even in this restricted setting.

## Frozen version and read coverage

The checked candidate is the complete 393-line file FINITE_TAIL_ROUTE.md, Sections 1–7, equations (1)–(25), with SHA-256:

    da251f231832e69c74581ba4291e649d1322737eebd46b2a4d9c6ca1a8dd0d65

An initial complete read had SHA-256 ea3592e6b77a4b23ef18d8015c7b9fb913b9221f6761be5becdc73091f82f7bc. The candidate then changed to define the absolute carrier supremum explicitly. I reread the entire replacement before issuing this verdict. The verdict applies to the replacement hash above.

Allowed manuscript inputs and coverage:

| File | Read coverage | SHA-256 |
|---|---|---|
| paper/main.tex | Network setting, normalization, initialization, dense equations, and population interpretation; not a review of all 1620 lines | 60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95 |
| paper/results.tex | Complete, 233 lines | 6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1 |
| paper/proof_alltime.tex | Complete, 928 lines; this check uses its deterministic dense fitting event and activity estimate | f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d |
| paper/proof_tracking.tex | Complete, 319 lines; used for meanings of carrier tails and cutoff removal | e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be |

Required skills, read completely and applied:

| File | SHA-256 |
|---|---|
| /home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md | daac37e41dca5e618c5baf2a65689000e526930f059b822ebec61aafbfd1abfc |
| Its references/neural-response-memory.md | c2d570aac8950b5766513d81dd2dada4a9babeba92bbb554f1042107207a52b1 |
| /etc/codex/skills/solve-math-rigorously/SKILL.md | 9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7 |

No other study, prior review, or other reviewer's finding was an input. No numerical experiment was needed. The probability bounds below are reconstructed directly.

## 1. Transformed dynamics and total activity

Write \(v_a=x_a/\sqrt d\), and retain \(v_a^\top v_b=\delta_{ab}\), \(\phi_1=\tanh\), and \(w(0)=0\). The canonical first-weight normalization gives

\[
 \dot z_a^{(1)}
 =-\frac2m\sum_b r_b\,\delta_b^{(1)}\,v_b^\top v_a
 =-\frac2m r_a\,\operatorname{sech}^2(z_a^{(1)})\odot k_a^{(1)}.
\]

The proposed transformation satisfies

\[
 F'(z)=\frac12+\frac12\cosh(2z)=\cosh^2z,\qquad F(\mathbb R)=\mathbb R.
\]

It is a smooth increasing bijection. For \(p=F(z)\),

\[
 \frac{d}{dp}\tanh(F^{-1}(p))
 =\operatorname{sech}^4(z)\in(0,1].
\]

With \(db_a=-(2/m)r_a\,dt\), the identity \(dp_a=k_a^{(1)}\,db_a\) is exact, including sign and scale. The other controlled equations are also exact:

\[
 dw=\sum_a h_a^{(2)}\,db_a,\qquad
 dW=\frac1n\sum_a\delta_a^{(2)}h_a^{(1)\top}\,db_a.
\]

There is no change of learning rate. The transformation removes the first gate from the first-layer velocity. All subsequent dependence on \(p\) is through the bounded globally Lipschitz function \(\psi=\tanh\circ F^{-1}\). No step differentiates \(F\) with respect to initialization.

The driver variation obeys

\[
 \sum_a|db_a|=\frac2m\sum_a|r_a|\,dt\le2\rho\,dt.
\]

Every actual finite prefix therefore has variation at most \(S=2Y/\kappa\) on the fitting event. Reparametrization by variation gives \(\ell^1\) speed at most one; constant extension to \([0,S]\) gives a member of \(\mathcal B_S\). Integral change of variables verifies that the state follows the same path, and constant portions make no state change. For nonzero labels the manuscript's lower residual bound also makes this clock strictly increasing on each finite physical horizon. Taking all finite prefixes suffices for the all-time supremum.

This step does not declare the actual residual independent of initialization. The deterministic control class contains every possible realized prefix.

## 2. Uniform controlled vector-field estimates

Let \(K_1=K+sB\). For every deterministic control in \(\mathcal B_S\),

\[
 \|w(u)\|_\infty\le Bu,\qquad
 \|\delta_a^{(2)}(u)\|_2/\sqrt n\le sBu.
\]

Each matrix integrand has Frobenius norm at most \(sBu\), so

\[
 \|W(u)-W_0\|_F\le sB\int_0^u v\,dv\le sBS^2/2.
\]

The candidate's weaker bound \(sBS^2\) is valid. Hence
\(\|W(u)\|_{\rm op}\le K_1\) and
\(\|k_a^{(1)}(u)\|_2/\sqrt n\le K_1sBS\).
All coordinate velocities are bounded at fixed \(n\). Initial transformed coordinates may be large, but are finite; bounded velocity prevents finite-interval blowup. The locally Lipschitz controlled ODE therefore continues uniquely to \(S\).

For two states in the indicated tube, let \(D\) be the candidate's normalized difference norm. Direct subtraction yields

\[
 \|\Delta h_a^{(1)}\|_2/\sqrt n\le D,\qquad
 \|\Delta z_a^{(2)}\|_2/\sqrt n\le(1+K_1)D,
\]

\[
 \|\Delta\delta_a^{(2)}\|_2/\sqrt n
 \le s\|\Delta w\|_2/\sqrt n+jBS\|\Delta z_a^{(2)}\|_2/\sqrt n,
\]

and

\[
 \|\Delta k_a^{(1)}\|_2/\sqrt n
 \le K_1\|\Delta\delta_a^{(2)}\|_2/\sqrt n+sBS\|\Delta W\|_F.
\]

The rank-one matrix-update difference is bounded by

\[
 \|\Delta\delta_a^{(2)}\|_2/\sqrt n
       +sBS\|\Delta h_a^{(1)}\|_2/\sqrt n.
\]

The readout component uses the Lipschitz constant \(s\) of \(\phi_2\). These cover every vector-field component. The resulting boundedness and Lipschitz constants are independent of \(n\), initial transformed-coordinate magnitude, and \(0<S\le1\). No maximum of the first carrier appears.

## 3. Uniform driver metric

Let \(\varepsilon=\|b-c\|_\infty\). Since \(X^c\) has variation at most \(VS\) and \(V_a\) is \(L\)-Lipschitz,

\[
 \operatorname{Var}(V_a(X^c))\le LVS.
\]

This composition is absolutely continuous. Integration by parts gives

\[
 \int_0^uV_a(X^c)\,d(b_a-c_a)
 =V_a(X^c(u))(b_a(u)-c_a(u))
  -\int_0^u(b_a-c_a)\,d(V_a(X^c)).
\]

The initial boundary term vanishes. Its state norm is at most
\(\varepsilon V(1+LS)\). Summing over samples and applying Gronwall against the variation measure of \(b\) gives

\[
 \sup_{u\le S}D(X^b(u),X^c(u))
 \le mV(1+LS)e^{LS}\varepsilon\le C\varepsilon.
\]

This proves the driver metric used in chaining. Only Lipschitz regularity is needed, so the candidate does not require an unavailable classical derivative of \(\phi_2'\). Rapidly oscillating controls do not invalidate the step: the integral estimate uses their common variation bound.

## 4. Cavity normalization and the retained factor \(S\)

The cavity deletes one first-layer neuron and its matrix column while keeping every denominator equal to \(n\). This matches the canonical flow. A cavity feature has norm at most \(\sqrt{n-1}\le\sqrt n\), so all preceding normalized estimates survive.

The removed full column obeys

\[
 \|W_i(u)-W_{0,i}\|_2
 \le\frac1n\int_0^u sBS\sqrt n\,dv
 \le sBS^2/\sqrt n.
\]

Set \(q_i=\|W_{0,i}\|_2+sBS^2/\sqrt n\).
At an identical retained state, the deleted contribution to a preactivation is \(W_ih_{a,i}^{(1)}\), of normalized norm at most \(q_i/\sqrt n\). It produces the following forcing bounds per unit driver variation:

| Component | Bound in its corresponding normalized norm |
|---|---|
| Readout | \(s q_i/\sqrt n\) |
| Top backward field | \(jBS q_i/\sqrt n\) |
| Retained first-layer coordinates | \(K_1jBS q_i/\sqrt n\) |
| Retained matrix update | \(jBS q_i/\sqrt n\) in Frobenius norm |

The remaining differences are controlled by the proved Lipschitz constant. The retained states start identically. Gronwall therefore gives

\[
 \sup_{u\le S}D_i(u)\le CSq_i/\sqrt n.
\]

The top-backward estimate does retain \(S\), rather than merely a constant:

\[
 \frac{\|z_a^{(2)}-z_a^{(2),-i}\|_2}{\sqrt n}
 \le CD_i+q_i/\sqrt n,
\]

\[
 \frac{\|\delta_a^{(2)}-\delta_a^{(2),-i}\|_2}{\sqrt n}
 \le sD_i+jBS(CD_i+q_i/\sqrt n)
 \le CSq_i/\sqrt n.
\]

Thus the unnormalized discrepancy is \(CSq_i\). The exact carrier decomposition is

\[
\begin{aligned}
 k_{a,i}^{(1)}
 &=W_{0,i}^{\top}\delta_a^{(2),-i}
 +W_{0,i}^{\top}(\delta_a^{(2)}-\delta_a^{(2),-i})\\
 &\quad +(W_i-W_{0,i})^\top\delta_a^{(2)}.
\end{aligned}
\]

On \(E_n=\{\|W_0\|_{\rm op}\le K\}\), the last two terms have absolute value at most

\[
 CS\|W_{0,i}\|_2q_i+s^2B^2S^3\le CS.
\]

The \(\sqrt n\) factors cancel in the last product. This remainder is \(O(S)\), not a width-vanishing error. That is sufficient for a tail theorem.

## 5. Conditional Gaussianity and entropy

Given all first-layer initialization and retained columns,
\(W_{0,i}\sim N(0,I_n/n)\) is independent of the cavity for every deterministic driver. The event
\(\{\|W_{0,-i}\|_{\rm op}\le K\}\) is measurable under that conditioning. Defining the cavity family to be zero on its complement preserves Gaussianity.

The conditional canonical metric is exactly

\[
 d(b,c)=
 \frac{\|\delta_a^{(2),-i,b}(S)-\delta_a^{(2),-i,c}(S)\|_2}{\sqrt n}
 \le C\|b-c\|_\infty.
\]

Pointwise standard deviations are at most \(sBS\), and \(G_0=0\).

The control class is bounded and uniformly Lipschitz. Its uniform limit retains the \(\ell^1\) Lipschitz bound, hence absolute continuity and the almost-everywhere speed constraint. This proves closedness and the claimed compactness. Each coordinate stays in \([-S,S]\). A time grid with \(O(1+S/\varepsilon)\) points and a coordinate lattice with \(O(1+S/\varepsilon)\) values gives

\[
 \log N(\varepsilon)
 \le C_m(1+S/\varepsilon)\log(2+S/\varepsilon).
\]

Choosing one actual driver in each occupied bin gives internal nets. These nets may be fixed deterministically, independently of all initialization.

For \(\varepsilon_\ell=S2^{-\ell}\), adjacent representatives are within
\(3\varepsilon_\ell\). There are at most
\(N(\varepsilon_\ell)N(\varepsilon_{\ell-1})\) possible increments.
Gaussian tails, a union bound, and tail integration bound the \(L^p\) maximum of these increments by

\[
 CS2^{-\ell}
 \left(\sqrt p+\sqrt{(\ell+1)2^\ell}\right).
\]

Summing gives \(CS\sqrt p\).
For each finite omitted-column realization the cavity family is continuous in the driver metric, so telescoping converges to its actual process values. The summable increment bound controls the supremum and gives separability/measurability. Independence between increments is not needed. The factor \(S\) survives because both domain diameter and every dyadic scale are proportional to \(S\).

## 6. Full event and all-time maximum

The full event \(E_n\) depends on the omitted column. The candidate correctly does not condition on \(E_n\) to declare a Gaussian law. Instead it uses

\[
 \mathbf1_{E_n}U_{a,i}
 \le\sup_{b\in\mathcal B_S}|G_b|+CS,
 \qquad
 U_{a,i}=\sup_{b\in\mathcal B_S}|k_{a,i}^{(1),b}(S)|.
\]

Here \(E_n\) implies the retained-column event, and the Gaussian supremum on the right is integrated under the unrestricted omitted-column law. This yields

\[
 \|\mathbf1_{E_n}U_{a,i}\|_{L^p}\le CS\sqrt p.
\]

At \(p=2r\), exponential expansion gives

\[
 \mathbb E[\mathbf1_{E_n}e^{cU_{a,i}^2/S^2}]
 \le1+\sum_{r\ge1}\frac{c^rC^{2r}(2r)^r}{r!}
 \le1+\sum_{r\ge1}(2ecC^2)^r.
\]

Choose \(c\) so that the last series converges.
The case \(S=0\) is separately stationary, as stated.

On \(\mathcal G_n\), every actual finite prefix is contained in this control supremum, and \(\mathcal G_n\subset E_n\). Hence the physical-time supremum is taken before exponentiation without any discretization of time. The desired exponential moment follows. Union over \(m n\) training carriers gives the maximum tail bound without an additional hidden width factor.

## 7. Weighted tails and exact cutoff inactivity

For \(M\ge BS\), the readout-tail term is zero. On \(\mathcal G_n\),

\[
 Z_n(M)\le\frac S2\sum_a
 \left(\frac1n\sum_iU_{a,i}^2
                    \mathbf1_{\{U_{a,i}>M\}}\right)^{1/2}.
\]

The exponential moment implies

\[
 \mathbb E[\mathbf1_{E_n}U_{a,i}^2\mathbf1_{\{U_{a,i}>M\}}]
 \le CS^2e^{-cM^2/S^2}
\]

after decreasing \(c\). Applying Cauchy–Schwarz to each empirical square root gives

\[
 \mathbb EZ_n(M)\le CS^2e^{-cM^2/S^2},
\]

with another harmless reduction of \(c\). This uses no independence of neurons, residuals, or carriers.

For \(M=A S\sqrt{\log(e+n)}\), the multiplier must be large enough both to satisfy \(M\ge BS\) and to obtain the desired exponent. Such a fixed choice exists. Markov then gives the stated confidence bound.

For inactivity, the cutoff is the identity on the full dense readout and all full dense training carriers. The clipped top response therefore first equals the dense top response; its adjoint carrier is consequently identical, so lower clipping also does nothing. Every parameter velocity agrees along the dense trajectory. The clipped finite-dimensional ODE is locally Lipschitz, so uniqueness gives equality on every finite horizon. The dense path supplies continuation. The removal error is exactly zero on the stated event.

## 8. Scope and unresolved issues

There is no remaining gap in the restricted tail/inactivity result checked here. Its constants depend on \(K,m,B,s,j\); all width and activity dependence is displayed. Initial transformed-coordinate sizes never enter the constants.

These extensions remain unproved and are correctly excluded:

- General training Grams: the transformation creates unbounded ratios of tanh derivatives.
- More than two hidden layers: intermediate gate variations involve carriers without deterministic coordinate bounds.
- Unbounded second activation: the needed readout coordinate bound no longer follows from total activity alone.
- Finite-to-population root width: the \(O(S)\) cavity remainder does not vanish with width and is not a mean-bias estimate.
- Strict root width from a growing cutoff alone: an unbounded comparison constant such as \(e^{CM_n}\) still causes a loss at \(M_n\asymp\sqrt{\log n}\).

This verdict supports use of the restricted finite cutoff-removal theorem within this study. It is not a promotion approval or a proof of the original arbitrary-depth, arbitrary-data all-time root-width target.
