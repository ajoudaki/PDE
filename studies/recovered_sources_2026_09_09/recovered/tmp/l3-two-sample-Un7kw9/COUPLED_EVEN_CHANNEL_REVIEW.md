# Fresh-context adversarial proof audit

Date: 2026-09-05.

Verdict: **PASS for the explicitly conditional, scoped results. No blocking mathematical gap found.** The primal even-energy and physical-time trained-return estimates are valid under the stated branch hypotheses. The quartic identity and response estimates are valid with their separately stated integrability and differentiability qualifications. This verdict does not establish the population construction, a closed source-response bound, or the ultimate two-sample theorem.

## Audited inputs and scope

The complete 776-line candidate was read:

- File: `/tmp/l3-two-sample-Un7kw9/COUPLED_EVEN_CHANNEL_ESTIMATE.md`
- SHA256: `9fd58fa3256394644f23c6e7d0e66c253beac76f2f43f13ec49477137d413e20`
- This exactly matches the hash supplied in the audit request.

The only external mathematical/model document used was the complete 75-line normalization contract:

- File: `/tmp/l3-two-sample-Un7kw9/CONTRACT.md`
- SHA256: `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd`
- Use: input, parameter-metric, loss, initialization, and physical-time normalization only. No result mentioned or linked by that contract was used.

The requested procedural skill was read in full before the audit:

- File: `/etc/codex/skills/solve-math-rigorously/SKILL.md`
- SHA256: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`

No history, prior reviews, other candidate-referenced documents, agents, experiments, or external theorem lookups were used. This review is the sole new file; no existing file was edited. Line references below refer to the hashed candidate.

The exchange parity, intertwining operators, zero initial population readout, strong branch, Hilbert-Schmidt increments, and physical chain/loss identities are accepted as the stated conditional setup in lines 49–77 and 97–115. Their construction is outside this audit. The calculations are checked as identities and estimates for the actual network on that branch, including its current trained operators. No symmetry of an independently sampled finite network is substituted for those hypotheses.

The activation is the single function (1), with `e = 1/10` for every dataset. Data- and horizon-dependent estimate constants are allowed. There is no requirement that those constants be small or uniform as the angle tends to zero.

## 1. Normalization and the primal even-energy estimates

For `mu > 0`, put

\[
 u=(x_1+x_2)/(2\mu),\qquad v=(x_1-x_2)/(2\delta).
\]

These vectors are orthogonal, both have squared length `d`, and `x_1 = mu u + delta v`, `x_2 = mu u - delta v`. With `U = W^(1)u` and `V_1 = W^(1)v`, the restriction of the contract's metric `(d/n)||dW^(1)||_F^2` to their plane is exactly `||dU||_2^2 + ||dV_1||_2^2` in probability normalization. At `mu = 0`, the common coordinate is absent, as specified. The initial Gaussian coordinates have variance one, agreeing with the stated initial norms.

On an empirical probability space, `f tensor g` has matrix `fg^T/n`, whose Frobenius norm equals `||f||_2 ||g||_2`. Thus the operator and readout terms of (2) also agree with the contract. There is no missing width or input-dimension factor.

The symmetric predictions give the loss `(1-delta G)^2`. Therefore

\[
 \dot\Theta=2\delta(1-g)\nabla G,\qquad
 \dot g=2\delta^2(1-g)\|\nabla G\|^2.
\]

The integrating-factor solution for `1-g`, initially one, gives `0 <= g <= 1` and `0 <= lambda <= 2 delta`. The gradient-flow identity then gives (6), including total squared speed at most one and displacement at most `sqrt(t)`. The factor two in (5) is correct.

The activation bounds in lines 35–41 hold: splitting the primitive's integral at one gives `1+1/3`; and `|z|^3/(1+z^4)^2 <= 1` gives the stated coarse curvature bound. The activation is nonaffine on every open interval because its second derivative is nonzero at every nonzero real argument.

The exact finite-angle differential and its weighted adjoint are

\[
 dh=a\,dM+\delta^2b\,dV,\qquad dk=b\,dM+a\,dV,
\]
\[
 \binom{\delta P}{Q}
 =\begin{pmatrix}a&\delta b\\\delta b&a\end{pmatrix}
   \binom{\delta p}{q}.
\]

The matrix eigenvalues are precisely the two original activation derivatives, both in `[1,L]`. Their difference is at most `e`, so `|b| <= e/(2 delta) = beta`. This verifies (7),(10), including all angle factors. It uses no spatial supremum bound on `V` and no uncontrolled product `Vq`.

The backward recursion (8) and the parameter updates (9) follow by this adjoint and the operator product rule. Their even and odd rank-one terms are orthogonal in the Hilbert-Schmidt metric. The weighted-pair bound gives

\[
 \|Q_3\|_2\le L\|C\|_2,\quad
 \|q_2\|_2\le KL\|C\|_2,\quad
 \|Q_2\|_2\le KL^2\|C\|_2,\quad
 \|q_1\|_2\le K^2L^2\|C\|_2.
\]

In particular, the bound for `Q_2` does not discard its common-channel contribution. Resolving the common components separately yields exactly

\[
 \|P_3\|_2\le\beta\|C\|_2,\quad
 \|p_2\|_2\le\beta K\|C\|_2,\quad
 \|P_2\|_2\le2\beta LK\|C\|_2,
\]
\[
 \|p_1\|_2\le2\beta LK^2\|C\|_2,\qquad
 \|P_1\|_2\le3\beta L^2K^2\|C\|_2.
\]

Both initialized and trained parts of the operators are included. This checks every bound in (13).

The forward bounds (11),(12) use the displacement bound and the exact identities/inequalities `h=1+M+e j`, `|j|<=4/3`, and `|k|<=L|V|`. Hence they require only second moments. Combining them with `lambda beta <= e` and `||C(t)||_2 <= sqrt(t)` gives

\[
 \|\dot U\|_2\le3e\mu L^2K^2\sqrt t,\quad
 \|\dot E_{A,e}\|_{\rm HS}\le2eLKH_1\sqrt t,\quad
 \|\dot E_{B,e}\|_{\rm HS}\le eH_2\sqrt t.
\]

Thus the squared combined even speed is at most `e^2 S t`. Integrating it gives `e^2 S T^2/2`; integrating its square root gives `(2/3)e sqrt(S) T^(3/2)`. Total loss dissipation gives the competing bounds `1` and `sqrt(T)`. All constants and both minima in (15) are correct. The individual integrations in (16) correctly give the factors `2/3`, `4/3`, and `2`.

The frozen affine common-field comparison (17),(18) is exact. At `e=0`, all common adjoints vanish and the common parameters are frozen. On the nonlinear path the decomposition uses the current `h_l` and retains the initial nonlinear offsets `e j_l`. Consequently, the `4e/3` terms cannot be dropped, and the candidate does not drop them. No odd-path comparison or perturbative closeness assumption is used.

**Finding:** (13)–(18) need no undeclared moment or smallness hypothesis. The inverse-angle gate factor cancels in the physical even-velocity estimates. The antipodal case is covered by `mu=0` and omission of `U`.

## 2. Trained-return bounds and operator transport

Integrating the actual even update gives

\[
 E_{B,e}(t)^*P_3(t)
 =\int_0^t\lambda(s)h_2(s)
           \langle P_3(s),P_3(t)\rangle\,ds,
\]

and the corresponding formula for `A_e,P_2,h_1`. These are (19). The integrands are strongly measurable on the strong branch and norm-integrable by the primal bounds. Their product of adjoints is a scalar inner product, so it needs no extra spatial product moment. The stated positive semidefiniteness is the Gram identity for `sqrt(lambda(t))P_l(t)`; it supplies no sign for the field-valued return with time-varying `h`, and none is used.

All trained-return coefficients check:

| Quantity | Bound at time `t` | Integral on `[0,T]` |
| --- | --- | --- |
| `lambda` times the `L^2` norm of `p_2^tr` | `(2/3)e^2 H_2 t^2` | `(2/9)e^2 H_2 T^3` |
| `lambda` times the `L^2` norm of `p_1^tr` | `(8/3)e^2 L^2 K^2 H_1 t^2` | `(8/9)e^2 L^2 K^2 H_1 T^3` |

Indeed, before substituting (16), these quantities are bounded by `e sqrt(t)||E_{B,e}||_HS` and `2eLK sqrt(t)||E_{A,e}||_HS`. This proves (20),(21). For the full incoming adjoints, squaring `eK sqrt(t)` and `2eLK^2 sqrt(t)` and integrating gives respectively `e^2K^2T^2/2` and `2e^2L^2K^4T^2`, as in (22).

The nested initialized return contains `B_e`. Its further decomposition is exactly

\[
 p_1-p_1^{(0)}=A_{0,e}^*(a_2p_2^{\rm tr})+p_1^{\rm tr}.
\]

Multiplication by `a_2` costs at most `L`. Applying (21) gives the coefficient in (22a):

\[
 \frac{2e^2T^3}{9}(K_0LH_2+4L^2K^2H_1).
\]

This includes the return through either explicitly trained even operator. The gates, readout, and odd operator remain at their actual current values.

The scope restriction in lines 349–373 is correct: these are physical-time bounds on the indicated operator decomposition along the nonlinear trajectory. They do not compare with an independently evolved frozen-operator network, control derivatives of gate selection, or remove inverse-angle factors from unweighted adjoints.

Equations (23) retain each direct operator-training term and each lower-layer transport. The first common velocity is `lambda mu^2 P_1`, with the correct square on `mu`. In (24), differentiating the transpose actions correctly gives the direct terms `lambda h||P||_2^2` and `lambda k||Q||_2^2`. No derivative of `lambda` belongs in this first product derivative. Equation (25) retains all differentiated gates; lines 422–425 explicitly qualify their product integrability.

**Finding:** (19)–(22a) and the transport algebra are correct. No fourth moment, sign condition, small `e C(D,T)`, or frozen odd block is silently used.

## 3. Quartic weight and fourth-moment integrability

With `D=delta V`, `x=M+D`, `y=M-D`,

\[
 y^4-x^4=-8MD(M^2+D^2).
\]

Dividing the derivative-gate difference by `2 delta` gives exactly the displayed formula for `b`. The integral secant satisfies `k=sV` and `1<=s<=L`. Thus the weight (26) satisfies `Mb=-omega k` with no division by `M` or `V`, including their zero sets.

The bound is valid because

\[
 4M^2(M^2+D^2)=\tfrac12(x+y)^2(x^2+y^2)
 \le(x^2+y^2)^2\le2(x^4+y^4),
\]

while `(1+x^4)(1+y^4)>=x^4+y^4` and `s>=1`. At `x=y=0` the numerator is zero. Hence `0<=omega<=2e` with the claimed constant.

The first derivatives are globally bounded as claimed. The numerator over the two quartic denominators is a finite sum of products `x^i/(1+x^4) * y^(4-i)/(1+y^4)`, `0<=i<=4`. Each factor and its first derivative is bounded. Also

\[
 s_M=\tfrac12\int_{-1}^1\phi''(M+rD)\,dr,\qquad
 s_D=\tfrac12\int_{-1}^1r\phi''(M+rD)\,dr
\]

are bounded, and `s>=1` controls differentiation of `1/s`. Therefore `c_e` is finite independently of `delta`; no bounded-preactivation hypothesis is hidden here.

The Hilbert-Schmidt product rule and `E_{B,e}h_2=M_3-B_{0,e}h_2` give

\[
 \frac d{dt}\|E_{B,e}\|_{\rm HS}^2
 =-2\langle\omega_3C,\dot C\rangle
  -2\lambda\langle b_3C,B_{0,e}h_2\rangle.
\]

The readout derivative of `E[omega_3 C^2]` cancels the first term exactly. The remaining initialized-operator work has the sign in (29), and its absolute integral is bounded by

\[
 2eK_0H_2\int_0^t\sqrt r\,dr=(4/3)eK_0H_2t^{3/2}.
\]

Thus (29),(30) have the correct signs and constants. No sign of `CV_3` is assumed. The weight transport remains, including the direct `B`-training contributions displayed in lines 505–507 and all lower-layer transports in (23).

The stated fourth-moment condition suffices for the product rule. The first-differential bounds use only bounded first gates and give

\[
 \|\dot\omega_3\|_2
 \le c_e(\|\dot M_3\|_2+\delta\|\dot V_3\|_2)
 \le c_eN_3\|\dot\Theta\|.
\]

Consequently,

\[
 \int_0^T\mathbb E|C^2\dot\omega_3|\,dt
 \le c_eN_3
 \left(\int_0^T\|C\|_4^4\,dt\right)^{1/2}
 \left(\int_0^T\|\dot\Theta\|^2\,dt\right)^{1/2}.
\]

The last factor is at most one. This proves (31), even with the absolute value inside the expectation. Bounded `omega` and space-time `L^2` bounds on `C,dot C` also give integrability of `omega C dot C`.

The velocity bounds and loss identity supply `W^{1,2}` time regularity in `L^2` for the preactivations and readout. Their integral representatives are absolutely continuous in time for almost every population point. The pointwise product rule, the absolute integrability bounds above, and Fubini therefore justify the integrated identity (29). No fourth moment of the velocities is needed.

**Finding:** `C in L^4([0,T] x Omega_3)` is an explicitly stated, sufficient extra input, not a consequence established by (6). The energy itself is nonnegative and finite for `C in L^2`, but differentiating it needs the qualification. This modulated energy is not claimed to have an unconditional `e^2` bound: its initialized work estimate is of order `e`, and its transport residual remains.

## 4. Complete response and Hessian

The nearby-state forward equations correctly use full operators. Thus (32) retains `eta_A h_1`, `eta_A k_1`, `eta_B h_2`, and `eta_B k_2`, including for symmetry-breaking variations. The two absolute column sums of the activation differential are at most `J=L+beta`. With `N_1=2`, induction gives exactly `N_2=S_1+KJN_1` and `N_3=S_2+KJN_2`, proving (34).

The differentiated gates have the factors

\[
 \alpha=c\xi_M+\delta^2d^{\rm gate}\xi_V,\qquad
 \gamma=d^{\rm gate}\xi_M+c\xi_V.
\]

Using `|c|<=4e`, `|d^gate|<=4e/delta` gives `|alpha|<=4eZ` and `|gamma|<=4eZ/delta` for `Z=|xi_M|+delta|xi_V|`. The pointwise bounds for `R^P,R^Q` are respectively `4eZ(|p|+|q|/delta)` and `delta` times that quantity. Their `L^2` norm sum therefore has exactly the constant `4e(1+delta)` in (36).

Both differentiated transpose orientations are retained in (37). For example, `D(B^*P_3)[eta]=eta_B^*P_3+B^*widehat P_3`, with matching terms for `Q_3` and at `A`. Using full `A^*,B^*` is essential for parity-changing variations, and the candidate does so.

For completeness, the full variation of the `A` component of `grad G` is

\[
 \widehat P_2\otimes h_1+P_2\otimes dh_1
 +\widehat Q_2\otimes k_1+Q_2\otimes dk_1,
\]

and similarly for `B`. The first-input components are `mu widehat P_1,widehat Q_1`; the readout component is `dk_3`. Thus the full differentiated parameter gradient is accounted for. Under even-to-even projection, each derivative of the odd rank-one term retains either an unchanged odd input or an unchanged odd output, making that projection zero. Its other blocks are still present in the full response.

For unrestricted nearby states, `F=<C,h_3>` gives exactly

\[
 \mathcal L=F^2+(\delta G-1)^2.
\]

At the symmetric base `F=0`, its linearized negative gradient is

\[
 \lambda D^2G\eta
 -2\delta^2\nabla G\,DG[\eta]
 -2\nabla F\,DF[\eta].
\]

This verifies (39), including `Dlambda[eta]=-2delta^2 DG[eta]`. The possible term `-2F D^2F eta` has zero coefficient at this base. For arbitrary variations,

\[
 DF[\eta]=\langle\eta_C,h_3\rangle+\langle C,dh_3\rangle,
\]

so the negative common-prediction term is generally nonzero. For parity-preserving variations it vanishes, consistently with the restricted flow. Both preserving and breaking cases are covered.

To check the quadratic Hessian, the local second differentials with first variations fixed are

\[
 d^2h=c\xi_M^2+2\delta^2d^{\rm gate}\xi_M\xi_V
       +\delta^2c\xi_V^2,
\]
\[
 d^2k=d^{\rm gate}\xi_M^2+2c\xi_M\xi_V
       +\delta^2d^{\rm gate}\xi_V^2.
\]

Pairing with `p,q` gives precisely `<xi_M,R^P>+<xi_V,R^Q>`. Differentiating an operator action twice gives its transported second differential plus `2 eta_W dh` or `2 eta_W dk`. Moving the transported terms backward leaves both operator sums, all three local contributions, and the readout term `2<eta_C,dk_3>` in (40). The first preactivation is linear in its parameters and has no second differential. This verifies every mixed factor and includes symmetry-breaking variations.

The regular-term constants are correct:

\[
 \|P_2\|_2+\|Q_2\|_2\le D_2,\qquad
 \|P_3\|_2+\|Q_3\|_2\le D_3.
\]

Therefore the readout and two operator contributions are bounded in absolute value by `2J(N_3+D_2N_1+D_3N_2)||eta||^2 = H||eta||^2`. The local terms are at most `||eta|| mathcal R`. Pairing (39) with `eta` yields (42) with both dissipative squares, their factors two, and the stated source bound.

For `r_epsilon=(||eta||^2+epsilon^2)^(1/2)`, this gives

\[
 \dot r_\varepsilon\le\lambda H r_\varepsilon
                         +\lambda\mathcal R+\|j\|.
\]

The integrating factor and `integral lambda <= 2delta T` prove (43), including at zeros of the response and for a source injected at a later time.

**Finding:** no operator variation, transpose variation, mixed Hessian contribution, or negative physical loss term is missing. These are residual estimates for admissible population responses, not a bounded propagator theorem on the entire `L^2` parameter space. Finiteness of `H` bounds only the regular Hessian terms; the three gate-weighted residual pairs remain.

## 5. Extra hypotheses and final disposition

No undeclared hypothesis is needed for the established estimates at their stated claim level:

| Statement | Required input beyond the fixed model | Assessment |
| --- | --- | --- |
| Primal (13)–(22a) | Declared symmetric strong branch, bounded initialized operators, second moments, zero initial population readout, and loss dissipation | Explicit; no extra product moment is used. |
| Differentiated-gate transport (24),(25) | Existence of the displayed differentiated products | Explicit in lines 422–425. |
| Quartic (29),(31) | Integrable weight derivative; the stated space-time fourth moment of `C` suffices on the branch | Explicit and sufficient; not proved by (6). |
| Population response (37)–(43) | Admissible differentiations/products and response regularity; integrable `lambda mathcal R` and source norm for (43) | Explicit in lines 532–537 and 707–720. |
| Future closure using (44) | Integrable coefficient and controlled integrable source, with the required approximation uniformity | Open; no such estimate is established here. |

The response qualification cannot be removed just using the displayed primal norms: two `L^2` factors generally give an `L^1` product, whereas the residual recursion needs its displayed products in `L^2`. Bounded curvature alone does not repair that mismatch. Likewise, time-integrated squared speed gives no fourth spatial moment of the readout by itself. The candidate identifies both limitations and does not use either missing implication in its primal estimates.

One minor precision for future use of (44): “controlled source term b” must in particular provide `b in L^1[0,T]` for the proposed integrating-factor conclusion. This is already the type of integrability required in (43), but should be explicit if (44) becomes a theorem hypothesis. It does not affect an established estimate in this note.

No calculation selects `e` from the dataset, angle, horizon, mesh, width, or trajectory. The constants may grow with the permitted fixed data/horizon quantities; `J,N_l,H` can deteriorate as `delta` approaches zero. That is compatible with the fixed universal activation and data-dependent constants. The literal factors `e` and `e^2` require no perturbative smallness condition on the resulting estimates.

The note does not prove the uncut population branch or its continuation, exact finite-width parity, the fourth moment, source-response closure, approximation-uniform control, exact-GD descent, the same-label case, raw-kernel/restart conclusions, or genuinely nonlinear hidden motion. Those are acknowledged open tasks, not hidden premises supporting a claimed universal theorem.

Final disposition: **accept as conditional actual-network progress at a fixed finite angle with one fixed activation. No blocking correction is required for the stated bounds and identities. The ultimate population/GF/exact-GD and nonlazy two-sample theorem remains open.**
