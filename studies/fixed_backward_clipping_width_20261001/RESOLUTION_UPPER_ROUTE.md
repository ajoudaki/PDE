# Two Gaussian directions at the hard cap

2026-10-01. Scoped theoretical route. This report uses the complete four assigned notes `FITTING_AND_THRESHOLD.md`, `CLIPPED_POPULATION_ROUTE.md`, `CONCENTRATION_ROUTE.md`, and `BIAS_CAVITY_ROUTE.md`, together with the required solve-math-rigorously and investigate-conjectures instructions. The subsequently authorized `CAP_ANTICONCENTRATION_CHECK.md` independently checked the cap proposition and adaptive linear lemma; its concrete corrections are incorporated below. The subsequently authorized `WEIGHTED_REMAINDER_ROUTE.md` was read completely for the supersession note below. These are internal candidate-proof checks, not promotion review. No other study, experiment, Git operation, or manuscript edit was used.

The full conditional all-time root-width population error is **not proved here**. The new result below is a quantitative near-cap estimate for the actual lower backward carrier. It supplies the density ingredient missing from Section 8 of the cavity note. Its proof uses two Gaussian directions and retains the actual matrix, its transpose, empirical residuals, and the rank-one memory variables. The development below first isolates a weighted nonlinear response remainder and then analyzes the further scalar-history and population-law obligations.

**Supersession update.** [WEIGHTED_REMAINDER_ROUTE.md](WEIGHTED_REMAINDER_ROUTE.md), equation (5), now proves the L1 local nonlinear remainder requested in (20), on the row-independent common cavity event, with scalar histories frozen at their actual cavity values and uniformly over all measurable bounded removed-row paths. The near-cap input used there is the internally checked proposition below. Thus statements in the earlier route-development discussion that call the frozen-history **L1** remainder open are superseded. The RMS version remains unproved and is unnecessary for the deterministic-bias route. The mixed row-plus-scalar-history remainder (28) and the own-population mean-law comparison remain unproved.

## 1. Contract and statement

Use exactly the assigned q=1 system, with fixed cap one, fixed finite data, canonical independent Gaussian initialization, zero initial readout and values, matching initial keys, and clock one. Write

\[
 \alpha_{aj}=A_j\cdot u_a,
 \quad p_a=B^Td_a,
 \quad X_{aj}=\psi(\alpha_{aj})p_{aj},
 \qquad \psi(z)=\operatorname{sech}^2z.
\]

Thus the lower trained signal is \(C_1(X_{aj})\). All labels are fixed independently of width. The positive initial population readout-Gram margin is assumed. Constants below may depend on the fixed data, the gap, and fixed operator cutoffs. The label bound may be decreased by a fixed amount, but never depends on width.

Delete lower column \(j\) of the initialized matrix:

\[
 \gamma=W_0e_j,
 \qquad W_0^c=W_0(I-e_je_j^T).
\]

Run the same width-n closure with \(W_0^c\), retaining the same normalization and all rank-memory coordinates. A superscript c denotes that flow. Fix \(L>1\), an operator cutoff \(K\ge6\), and a gap \(\lambda>0\). The event-restricted inequality below works for any fixed K; the explicit sufficiently large cutoff is needed for its high-probability auxiliary claims. Define

\[
 \mathcal C_j=
 \{\|W_0^c\|_{\rm op}\le K,
       \ \Gamma_w^c(0)\succeq2\lambda I\},
 \qquad
 \mathcal E_j=\mathcal C_j\cap\{\|\gamma\|_2\le L\}.
 \tag{1}
\]

At initialization, the cavity forward features do not use \(A_{0,j}\), since its column is zero and the rank-memory values are zero. Therefore \(\mathcal C_j\) is independent of both \(\gamma\) and \(A_{0,j}\). The subsequent cavity flow may depend on \(A_{0,j}\) through its rank memories; no contrary independence is used.

**Near-cap proposition.** There are \(Y_*>0\), \(n_0<\infty\), and \(C<\infty\), independent of physical time and width, such that, for fixed \(0<Y\le Y_*\), \(n\ge n_0\), every training index a, every lower index j, every \(t\ge0\), and every \(u>0\),

\[
 \Pr\!\left(
   \mathcal E_j\cap
   \{\operatorname{dist}(X_{aj}(t),\{-1,1\})\le u\}
       \right)\le C u.
 \tag{2}
\]

The proof also works when one fixed upper row has already been deleted: Gaussian column vectors then live in its orthogonal coordinate subspace, still with covariance \(I/n\) there. Under a fixed larger population gap,

\[
 \Pr(\mathcal E_j^c)\le C/n.
 \tag{3}
\]

Consequently an estimate for an actual carrier without this auxiliary event has the form \(Cu+C/n\). This additive exceptional probability is harmless at a strip width of order \(n^{-1/2}\), but (2) is the sharper statement used in the proof.

There is also a common event for all lower coordinates. Take \(L\ge K\ge6\) and define
\(\mathcal G'_n=\{\|W_0\|_{\rm op}\le K,\ \Gamma_w(0)\succeq3\lambda I\}\).
For sufficiently large n the same one-column Gram comparison used below gives \(\mathcal G'_n\subseteq\bigcap_j\mathcal E_j\). With a fixed larger population margin, \(\Pr((\mathcal G'_n)^c)\le C/n\). Therefore (2) also holds with \(\mathcal G'_n\) replacing \(\mathcal E_j\), simultaneously as a statement for every a and j. This avoids a union bound over n separate cavity failures. It does not claim independence after conditioning on \(\mathcal G'_n\).

## 2. Uniform activity scales and a nonzero backward norm

On \(\mathcal E_j\), the initialization forward differences satisfy

\[
 \|z_a(0)-z_a^c(0)\|_2
 =|h_{aj}(0)|\,\|\gamma\|_2\le L.
\]

Since both feature columns have normalized norm at most one, their Gram difference is at most \(C L/\sqrt n\). For sufficiently large n, \(\mathcal E_j\) therefore gives a full initial Gram gap \(\lambda\). Both initialized operators have norm at most \(K+L\). The assigned fitting theorem applies uniformly over **every** first-row value \(A_{0,j}\) and every column in this ball, once Y is sufficiently small. In particular the top clip is inactive.

Let \(s(t)=\int_0^t\rho\) for either one of these flows. The exact residual equation in the concentration note has bounded scalar coefficients on the activity tube, and hence

\[
 \|\dot r(t)\|_m\le C\rho(t),
 \quad
 Y e^{-Ct}\le\rho(t)\le Y e^{-\lambda t}.
 \tag{4}
\]

The lower inequality follows by integrating \(\dot\rho\ge-C\rho\); for nonzero Y it also excludes finite-time hitting of zero. Integrating (4) shows that the activity scales of all full and cavity flows above are comparable at every common time:

\[
 cY\min(t,1)\le s(t)\le CY\min(t,1).
 \tag{5}
\]

For the rest of the proof, bounds at time t may therefore be written using \(s=s^c(t)\), with constants independent of the Gaussian coordinates varied below.

A useful lower bound, not supplied merely by an operator bound, is

\[
 c s^c(t)\le
 \frac{\|d_a^c(t)\|_2}{\sqrt n}
 \le 2s^c(t), \qquad t>0.
 \tag{6}
\]

To prove it, the prediction and readout bounds give

\[
 \frac{\|w^c\|_2}{\sqrt n}\ge\|f^c\|_m
 \ge Y-\rho^c(t)
 \ge Y(1-e^{-\lambda t})
 \ge\lambda s^c(t).
\]

Also \(\|z_a^c\|_2/\sqrt n\le D\), for a fixed D, and \(\|w^c\|_\infty\le2s^c\). For any fixed R,

\[
 \frac1n\sum_i|w_i^c|^2
             \mathbf1_{\{|z_{ai}^c|>R\}}
 \le4(s^c)^2D^2/R^2.
\]

Choose \(R^2\ge8D^2/\lambda^2\). On the complement of this set the gate is at least \(\psi(R)>0\). Since \(d_a^c=w^c\psi(z_a^c)\),

\[
 \frac{\|d_a^c\|_2^2}{n}
 \ge \psi(R)^2\lambda^2(s^c)^2/2,
\]

which proves (6). The resulting c can be very small. It remains a fixed positive number, so it may enter the fixed small-label restriction.

## 3. Column removal and two sensitivities

All derivatives in this section are weak derivatives, or ordinary derivatives wherever they exist. The hard-clip vector field is locally Lipschitz. Its solutions depend locally Lipschitzly on the finitely many Gaussian roots on the tube in (1); difference-quotient estimates therefore imply the stated derivative bounds almost everywhere. No derivative of the clip selector is taken.

### 3.1 A column-cavity bound

Uniformly on \(\mathcal E_j\),

\[
 \|d_a(t)-d_a^c(t)\|_2\le Cs,
 \qquad
 |p_{aj}(t)-\gamma^Td_a^c(t)|\le Cs.
 \tag{7}
\]

Here the normalization is important: the first norm is an **ordinary**, unnormalized norm. To check it, compare the two systems with ordinary norms for all vector states and with \(\sqrt n\) multiplying clock and residual differences. The direct forward source from column removal is \(\gamma h_{aj}\), whose norm is at most L. For the lower backward comparison, all coordinates other than j have no direct transpose source. At coordinate j the difference of the two clipped signals is at most two, even though the uncut transpose source could be large. Thus the direct lower backward source has ordinary norm at most two.

The remaining state differences use the common operator bound and the assigned global post-gate clipping inequality. The exact residual kernels give, after retaining their readout coercivity,

\[
 N'\le C(\rho+\rho^c)N+C R+C(\rho+\rho^c),
 \qquad
 R'\le-\kappa R+C(\rho+\rho^c)N+C(\rho+\rho^c),
 \qquad N(0)=R(0)=0,
\]

where N is the sum of these ordinary state differences and \(R=\sqrt n\|r-r^c\|_m\). The two rates need not be pointwise comparable. What (5) supplies is \(\int_0^t(\rho+\rho^c)\le Cs^c(t)\), which suffices for the integrated inequalities. In the residual equation a bounded ordinary source acquires a factor \(n^{-1/2}\) before this rescaling. For example, the direct lower signal source pairs with a vector of normalized norm \(O(s)\), and the direct forward source pairs with a bounded feature column. Integrating the residual inequality first and then using Gronwall yields \(N\le Cs\). Since the top clip is inactive,

\[
 \|d_a-d_a^c\|_2
 \le\|w-w^c\|_2+2\|w^c\|_\infty\|z_a-z_a^c\|_2
 \le Cs.
\]

Finally the rank correction to \(p_{aj}\) is

\[
 \frac1m\sum_b k_{bj}\frac{v_b^Td_a}{n},
\]

of size \(Cs^3\). Its addition to \(\gamma^T(d_a-d_a^c)\) proves the second assertion in (7).

### 3.2 Varying a first-layer Gaussian coordinate

Every training input is nonzero: a zero input would make its initial top feature column zero and contradict the Gram gap. Put \(e=u_a/\|u_a\|\) and decompose

\[
 A_{0,j}=\xi e+A_{0,j}^{\perp},\qquad \xi\sim N(0,1).
\]

Conditional on the other roots, \(\xi\) is independent. Uniformly on the event in (1),

\[
 \partial_\xi\alpha_{aj}(t)
       =\|u_a\|+O(s),
 \qquad
 |\partial_\xi p_{aj}(t)|\le Cs.
 \tag{8}
\]

For detail, the initial ordinary A sensitivity is one, the initial key sensitivities are bounded, and all other initial sensitivities vanish. The pairwise stability argument from the concentration note, multiplied by \(\sqrt n\), bounds their total ordinary sensitivity by C, and gives
\(\int_0^t\sqrt n\|\partial_\xi r\|_m\le Cs\).
Integrating the A equation gives
\(\|\partial_\xi(A-A_0)\|_F\le Cs\), since the derivative of its clipped signal is bounded by the global clipping inequality and the residual-difference term has normalized lower-signal norm \(O(s)\). Integrating the readout equation gives \(\|\partial_\xi w\|_2\le Cs\). The forward sensitivity is bounded in ordinary norm, so \(\|\partial_\xi d_a\|_2\le Cs\). In \(p_a=B^Td_a\), the fixed matrix term at coordinate j is bounded by \(L\|\partial_\xi d_a\|_2\); differentiating the rank term contributes at most \(Cs^2\). These estimates give (8).

In particular, after reducing the fixed label bound,
\(\partial_\xi\alpha_{aj}\ge\|u_a\|/2\) almost everywhere on the entire \(\xi\)-line. The good event is independent of \(\xi\), and fitting was established uniformly on that line.

### 3.3 Varying a Gaussian column direction

Fix t>0 and condition on the entire cavity, including \(A_0\). Define the cavity-measurable unit vector

\[
 v=\frac{d_a^c(t)}{\|d_a^c(t)\|_2},
 \qquad
 \gamma=\gamma_\perp+\frac\zeta{\sqrt n}v,
 \qquad \zeta\sim N(0,1).
 \tag{9}
\]

The scalar \(\zeta\) is independent of the perpendicular Gaussian vector and of the cavity. The norm cutoff in (1), after this conditioning, is an interval in \(\zeta\). Put
\(\sigma=\|d_a^c(t)\|_2/\sqrt n\).
On that interval,

\[
 p_{aj}(t)=\sigma\zeta+R_j,
 \quad |R_j|\le Cs,
 \quad
 \partial_\zeta p_{aj}(t)
   =\sigma+O(s/\sqrt n+s^3),
 \quad
 |\partial_\zeta\alpha_{aj}(t)|\le Cs^2.
 \tag{10}
\]

The first two assertions are (7), because \(\gamma_\perp^Td_a^c(t)=0\). The last two require stronger block estimates than a global operator-norm sensitivity bound. Here is a derivation.

Denote ordinary sensitivities of A,w,v,k by \(a,b,c,k\), respectively, taking a sum over their fixed sample lists. Set
\(T=\sqrt n|\partial_\zeta\tau|\),
\(R=\sqrt n\|\partial_\zeta r\|_m\), and
\(I(t)=\int_0^tR\).
All begin at zero. Within the following differential calculation write \(q(t)=\int_0^t\rho\) for the **full** flow's activity, so that \(dq=\rho\,dt\). Only after integrating the estimates will q be replaced by its comparable cavity activity s. Let Z and D denote the sums of the ordinary sensitivities of z and d. Direct differentiation, or difference quotients, gives

\[
 Z\le C(a+c+q^2k+n^{-1/2}),
 \qquad D\le b+CqZ.
 \tag{11}
\]

The explicit forward matrix source has norm at most \(n^{-1/2}\). The explicit transpose matrix source has only coordinate j, with size
\(|v^Td_a|/\sqrt n\le Cq\).
The global clipped-gate inequality and differentiation of the other equations therefore give

\[
 \begin{aligned}
 a'&\le C\rho(a+D+q(c+q^2k)+q)+CqR,\\
 b'&\le C\rho Z+CR,\\
 c'&\le C\rho D+CqR,\\
 k'&\le C\rho(a+k+q^2T)+Cq^2R,\\
 T'&\le R.
 \end{aligned}
 \tag{12}
\]

The key bound uses \(\|h_b-k_b\|_2/\sqrt n\le Cq^2\), which follows from the assigned key integral formula and the \(Cq\rho\) lower-feature speed. The same formulas hold in upper-derivative form for sensitivities obtained as limits of difference quotients.

For the residual sensitivity, retain the readout coercivity in the exact residual-kernel identity. A difference of the readout Gram contributes at most \(CZ\) after multiplying by \(\sqrt n\). In the hidden-motion kernel, a d difference contributes \(CqD\), a clipped lower-signal difference contributes \(Cq(a+D+q(c+q^2k)+q)\), and the explicit forward matrix derivative contributes at most \(Cq/\sqrt n\), since the single lower coordinate of the clipped signal has magnitude at most one. Differentiating the rank-memory kernels gives terms bounded by \(C[qD+q^2(a+c+k+T)]\). Consequently,

\[
 R'\le-\kappa R+
 C\rho\,[a+c+qb+q^2(k+T)+n^{-1/2}+q^2].
 \tag{13}
\]

Terms multiplying the residual sensitivity itself have size \(O(q^2)\) and are absorbed into \(\kappa>0\) by the fixed small-label condition. No clipped signal has been replaced by the ordinary dense gradient in this calculation.

Integrating (13) first, equations (11)–(12) and Gronwall initially give

\[
 a+b+c+k+T\le C(q^2+q/\sqrt n).
\]

Substitute this bound into the first line of (12); its explicit source is \(\rho q\), and \(\int qR\le qI\). This improves a to \(Cq^2\). Equation (13) then yields \(I\le C(q/\sqrt n+q^3)\). Substitution back into the remaining lines yields

\[
 a\le Cq^2,
 \quad b+D\le C(q/\sqrt n+q^3),
 \quad c\le C(q^2/\sqrt n+q^4),
 \quad k\le Cq^3,
 \quad T\le C(q/\sqrt n+q^3).
 \tag{14}
\]

These substitutions can equivalently be made as integral inequalities; every use of q in an integrand is its value at that time, and \(dq=\rho\,dt\). Only now use (5) to bound q(t) by \(Cs^c(t)=Cs\). This gives the same final estimates with s in place of q, without identifying or comparing the two activity rates pointwise.

Finally

\[
 \partial_\zeta p_{aj}
 =\frac{v^Td_a}{\sqrt n}
       +\gamma^T\partial_\zeta d_a
       +\partial_\zeta\!\left[
          \frac1m\sum_b k_{bj}\frac{v_b^Td_a}{n}
                           \right].
\]

The first term is \(\sigma+O(s/\sqrt n)\) by (7), the second is \(O(s/\sqrt n+s^3)\) by (14), and the rank derivative obeys the same bound. The A bound in (14) gives the last assertion in (10). This completes its proof.

## 4. Proof of the near-cap proposition

It suffices to consider \(0<u<1/4\), since larger u are covered by increasing C. At t=0 the carrier is zero, so the assertion is immediate. Fix t>0.

First consider \(|\alpha_{aj}|\ge1\), and condition on all roots except \(\xi\) in Section 3.2. At a point in either cap strip,

\[
 \partial_\xi X_{aj}
 =\psi(\alpha_{aj})\partial_\xi p_{aj}
   -2\tanh(\alpha_{aj})X_{aj}
                \partial_\xi\alpha_{aj}.
 \tag{15}
\]

Here \(|X_{aj}|\ge3/4\). Equations (8) and a sufficiently small fixed Y imply

\[
 |\partial_\xi X_{aj}|\ge c_a>0,
 \qquad
 \operatorname{sign}(\partial_\xi X_{aj})
   =-\operatorname{sign}(\alpha_{aj}X_{aj}).
 \tag{16}
\]

The function \(\alpha_{aj}(\xi)\) is strictly increasing. Thus each of its two regions \(\alpha_{aj}\ge1\) and \(\alpha_{aj}\le-1\) is an interval. On either such interval the preimage of each cap strip has Lebesgue measure at most \(2u/c_a\). One way to verify this without an unproved root-count assertion is to compose X with the scalar clip to that strip: its derivative vanishes outside the strip and has one sign, of magnitude at least \(c_a\), inside. Integrating this derivative bounds the total preimage measure. The standard Gaussian density is bounded, so conditional probability is at most \(Cu\). Integration over the other roots preserves this bound.

Now consider \(|\alpha_{aj}|<1\), condition as in Section 3.3, and use the scalar \(\zeta\). On a cap strip with \(|\alpha_{aj}|\le2\), one has \(|p_{aj}|\le (5/4)/\psi(2)\). From (6), (10), and

\[
 \partial_\zeta X_{aj}
 =\psi(\alpha_{aj})\partial_\zeta p_{aj}
        +\psi'(\alpha_{aj})p_{aj}
                      \partial_\zeta\alpha_{aj},
\]

we obtain, after fixing sufficiently large \(n_0\) and sufficiently small \(Y_*\),

\[
 \partial_\zeta X_{aj}\ge c s>0.
 \tag{17}
\]

Both cap strips have this same positive derivative bound. The factor s in (17) causes no small-time loss. Indeed, (10) and \(|X_{aj}|\ge3/4\) imply

\[
 |\zeta|\ge b/s
 \tag{18}
\]

for a fixed b>0, since \(\sigma\le Cs\) and \(|R_j|\le Cs\).

Partition the \(\zeta\)-line into unit intervals. On any interval with a contributing point where \(|\alpha_{aj}|<1\), the bound \(|\partial_\zeta\alpha_{aj}|\le Cs^2\) puts its **intersection with the norm cutoff** inside \(|\alpha_{aj}|\le2\), after further decreasing the fixed activity bound. That intersection is an interval; no estimate outside the cutoff is needed. The clipped-strip argument used above and (17) gives preimage length at most \(2u/(cs)\) there for either cap. Only intervals meeting \(|\zeta|\ge b/s\) can contribute. If \(\varphi\) is the standard Gaussian density, summing their density suprema gives

\[
 \Pr(\text{cap strip},\ |\alpha_{aj}|<1,
           \|\gamma\|_2\le L\mid\text{conditioned roots})
 \le \frac{Cu}{s}
       \sum_{I:\,I\cap\{|z|\ge b/s\}\ne\varnothing}
                    \sup_{z\in I}\varphi(z)
 \le \frac{Cu}{s}e^{-c/s^2}
 \le C'u.
 \tag{19}
\]

The last constant is uniform over \(0<s\le S_*\). This proves (2).

For (3), deleting one lower column changes the empirical first-feature covariance mean by \(O(n^{-1})\), and its mean-square error remains \(O(n^{-1})\). Conditional Gaussian sampling of the upper features and the bounded-Hessian interpolation calculation from the concentration note give an initial Gram error with mean square \(O(n^{-1})\). The larger limiting gap then gives the cavity Gram event with failure probability \(C/n\). The operator bound has the same failure estimate by the assigned Gaussian norm bound. Finally \(\mathbb E\|\gamma\|_2^2=1\) and \(\operatorname{Var}\|\gamma\|_2^2=2/n\), so a fixed \(L>1\) gives the claimed column-norm failure probability. A deleted upper row only removes one Gaussian coordinate and does not change these estimates or the directional proof.

## 5. The local response estimate isolated during route development

The discussion in this section records the dependency originally isolated by this route. The L1 form of (20) has since been established in `WEIGHTED_REMAINDER_ROUTE.md`; the supersession update above governs its current status.

The proposition addresses a real missing hypothesis in the earlier weighted clip-remainder lemma. It establishes, for the actual finite system or an actual one-row cavity, a uniform near-cap bound on appropriate good events. In particular, Fubini applied to (2), on the common event described after (3), shows that all the finitely many carriers equal a corner on a set of time measure zero almost surely. This permits a row-independent first tangent about an actual row cavity for prescribed removed-row histories: at almost every time the scalar clip is differentiable at the base carrier, its difference quotient is bounded by one, and dominated convergence in the integral equation followed by Gronwall proves the variational equation. The tangent obeys a linear nonautonomous equation with bounded, measurable clip selectors. Its operator norm is controlled by the same integrable activity coefficients as in the assigned forced-response lemma.

That observation does **not** prove that the actual nonlinear reinsertion equals this tangent with a root-width error in the required weak norm. The actual removed-row backward path depends on that row. Further, a norm bound on the first tangent does not control the coordinate remainders of the nonlinear solution.

The precise next estimate is the following. Let \(\omega\) be a removed upper row, let \(H(\omega;\eta)\) be the forced lower-feature trajectory driven by a bounded row path \(|\eta_a(t)|\le2s(t)\), and freeze the scalar coefficient histories at their actual row-cavity values. Let \(J[\eta]\omega\) be its first tangent at \(\omega=0\), retaining the true transpose response and the hard-clip selectors of the cavity. A useful sufficient bound is

\[
 \mathbb E\sup_{t\ge0}
 \left|
   \omega^T\{H(t;\omega,\eta(\omega))
            -H(t;0)-J_t[\eta(\omega)]\omega\}
 \right|
 \le C/\sqrt n,
 \tag{20}
\]

uniformly for the actual causal row paths generated by the single-row equations. An L1 estimate of this kind can suffice for prediction bias; an L2 row coupling is not necessary if the separate centered prediction concentration is retained. The scalar empirical histories must then be restored with their own quantitative response/covariance comparison. Neither uniformity is supplied by (2).

There is a sharper way to see why the previous Gaussian-tangent remainder lemma cannot simply be cited. For prescribed eta, a tangent coordinate is Gaussian conditional on the cavity. For \(\eta=\eta(\omega)\), it need not be Gaussian. Also, the nonlinear carrier increment is not identical to the tangent increment. Writing it as the tangent plus an unknown remainder and substituting that remainder into its own cap-crossing event requires a closed weighted estimate; an ordinary Euclidean estimate loses the cancellation supplied by the left Gaussian row.

Even under the Gaussian-tangent and small-ball hypotheses of Section 8 of the cavity note, a tangent perturbation of scale \(n^{-1/2}\) gives a squared clip-remainder estimate of order \(n^{-3/2}\) per coordinate: square the corner-crossing bound there and integrate its Gaussian tail against the linear small-ball estimate. Summing over n coordinates bounds its ordinary norm in RMS only by \(O(n^{-1/4})\). Cauchy--Schwarz against a row of ordinary norm \(O(1)\), with the corresponding fourth-moment bounds, has the same inadequate scale. This is a limitation of that estimate, not an asserted lower bound for the actual remainder. The desired root-width conclusion requires control of the *weighted* sum through the intervening causal propagator; replacing the propagator with its operator norm loses the useful scaling.

The linear part is more favorable: for prescribed coefficients it has a Volterra form

\[
 J_t[\eta]\omega
  =\sum_b\int_0^t R_b(t,s)\omega\eta_b(s)r_b(s)\,ds.
\]

The evolution factor has integrable variation in its terminal time. The forcing factor can contain a merely measurable source-time clip selector; no bounded variation of that selector is asserted. This distinction still permits a precise uniform estimate for the *linear* adaptive response.

Fix the cavity and its coefficient histories, all independent of \(\omega\), and hold them fixed when eta varies. The base trajectory at \(\omega=0\) is then independent of eta. Write the resulting cavity-measurable output kernel as \(K_b(t,s)\), so that

\[
 \omega^TJ_t[\eta]\omega
 =\sum_b\int_0^t\eta_b(s)r_b(s)
                          \omega^TK_b(t,s)\omega\,ds.
\]

The bounded insertion and output factors, and the evolution equation with operator coefficient bounded by \(C\rho\), give

\[
 \|K_b(s,s)\|_{\rm op}
    +\int_s^\infty\|\partial_tK_b(t,s)\|_{\rm op}\,dt
 \le C.
 \tag{21}
\]

The output gate is absolutely continuous and has integrable derivative, so it respects (21). Only the terminal time is differentiated; the source-time selector is held fixed.

For any fixed real matrix K and \(\omega\sim N(0,I/n)\), direct expansion with Gaussian second and fourth moments gives

\[
 \mathbb E\left|\omega^TK\omega-\frac{\operatorname{tr}K}{n}\right|^2
 =\frac{\operatorname{tr}(KK^T)+\operatorname{tr}(K^2)}{n^2}
 \le\frac{2\|K\|_{\rm op}^2}{n}.
\]

Apply this identity at \(t=s\) and to \(\partial_tK_b(t,s)\), then integrate terminal-time derivatives using Minkowski. Equation (21) gives

\[
 \left\|\sup_{t\ge s}
 \left|\omega^TK_b(t,s)\omega-
                 \frac{\operatorname{tr}K_b(t,s)}n\right|\right\|_{L^2_\omega}
 \le C/\sqrt n.
\]

It follows, **uniformly over every measurable row-dependent choice** \(\eta=\eta(\omega)\) with \(|\eta_b(s)|\le2s(s)\), that

\[
 \left\|\sup_{t\ge0}
 \left|\omega^TJ_t[\eta(\omega)]\omega
  -\sum_b\int_0^t\eta_b(\omega,s)r_b(s)
               \frac{\operatorname{tr}K_b(t,s)}n\,ds
       \right|\right\|_{L^2_\omega}
 \le \frac C{\sqrt n}
          \sum_b\int_0^\infty s(s)|r_b(s)|\,ds
 \le\frac{CS^2}{\sqrt n}.
 \tag{22}
\]

Indeed the absolute-value supremum is bounded pathwise by the integral of \(2s(s)|r_b(s)|\) times the displayed kernel supremum. Thus no independence between eta and omega is used. This proves that adaptive row feedback can be restored at the linear-response concentration step, without a history-Gram inverse or a uniform empirical-process theorem over eta.

To upgrade (22) to the nonlinear response, however, one must prove (20): the **nonlinear** remainder must remain controlled after every intervening left weighting. The density theorem and linear concentration do not establish that closure or identify the trace kernel with its population limit.

Gaussian covariance interpolation is another possible use of the density estimate, but also requires this distinction. For a fixed deterministic-coefficient path functional with a mesh-uniform expected weak-Hessian bound, interpolation could compare its Gaussian input laws directly in a covariance norm, without an inverse Gram or a square-root loss. The proposition above does not establish that hypothesis throughout such an interpolation: it concerns the actual canonical Gaussian flow and its true cavities. Interpolated effective Gaussian histories, and histories with frozen empirical coefficients, form an additional family whose near-cap and tangent estimates must be checked. More fundamentally, before this comparison the finite row field must actually be reduced to a Gaussian history plus its retained response with a controlled remainder. Using interpolation before that reduction would assume the Gaussian law one is trying to justify.

## 6. Claim status and route recommendation

- **New proved step within this route:** actual-carrier near-cap anti-concentration on the stated column-cavity events, uniform over time and width, with an \(O(n^{-1})\) exceptional probability. The proof uses first-row and column directions in complementary gate regions.
- **New internally checked adaptive linear step:** equation (22), a root-width approximation to the adaptive trace functional even when the removed-row backward path is an arbitrary measurable function of that same Gaussian row. The trace expression is itself random for such a path; deterministic-mean concentration is not claimed here.
- **Retained previous results:** global fitting, centered root-width prediction concentration, continuous-time row cavity stability, and qualitative convergence to the own clipped population.
- **Closed subsequently in its exact local scope:** the L1 weighted nonlinear response estimate (20), uniformly under bounded adaptive row feedback, with scalar histories frozen at actual cavity values; see `WEIGHTED_REMAINDER_ROUTE.md`.
- **Still open:** the mixed remainder needed to restore empirical scalar histories, and the quantitative bias of the resulting joint response/covariance law relative to the own population law.
- **Not established:** the requested all-time conditional RMS population error, an unconditional all-time estimate, or an admissible slower lower bound.

The subsequent continuation is recorded in Section 7. Repeating Gaussian concentration, first-response operator bounds, or near-cap density estimates would not close its remaining obligations. No failure of the desired width rate has been proved.

## 7. Conditional continuation if the weak reinsertion estimate is proved

This section answers a subsequent bounded assignment originally posed under the assumption of (20) in L1, uniformly for the specified actual causal row paths, with constants integrable in the activity weights. The subsequently read `WEIGHTED_REMAINDER_ROUTE.md` now supplies that input in precisely the frozen-history scope. The remaining statements below preserve their stated additional hypotheses; no full mean-law contraction is claimed.

### 7.1 The consequence is a trace-driven row equation, not yet a population equation

Combining (20) with (22), at frozen row-cavity scalar histories, gives the row-field representation

\[
 \omega^TH_a(t;\omega,\eta(\omega))
 =G_{n,a}(t)
    +\sum_b\int_0^t\eta_b(\omega,s)r_b^c(s)
                              R_{n,ab}(t,s)\,ds
    +\varepsilon_{n,a}(t),
 \tag{23}
\]

where

\[
 G_{n,a}(t)=\omega^TH_a^c(t),
 \quad
 \mathbb E_\omega G_{n,a}(t)G_{n,b}(s)
     =C_{n,ab}(t,s)
     :=\frac{H_a^c(t)^TH_b^c(s)}n,
 \quad
 R_{n,ab}(t,s)=\frac{\operatorname{tr}K_{ab}(t,s)}n.
\]

Conditional on the cavity, G is a genuine Gaussian history. The local nonlinear error estimate supplied by the weighted route is **averaged over the good cavity law**:
\(\mathbb E[\mathbf1_{\mathcal C}\sup_t|\varepsilon_{n,a}(t)|]\le C/\sqrt n\).
It is not asserted with a uniform constant for every fixed cavity realization. The adaptive linear estimate (22) does hold conditionally on each good cavity. The removed-row feedback eta can be kept in the integral equation and absorbed by the fixed small-activity row contraction; its constant is uniform on that event, so the averaged error bound is sufficient. This controls the effect of the error in (23). It does not replace the random cavity functions \((C_n,R_n)\) by their population counterparts. Nor does it restore the scalar histories which were frozen to obtain (23).

### 7.2 The cavity-linear scalar-history correction is already root width

There is a further inverse-free lemma which handles the first-order part of scalar-history restoration, including its adaptivity. It concerns Gaussian *linear* projections rather than quadratic forms.

Condition on a row cavity, so \(\omega\sim N(0,I/n)\) remains independent. For finitely many scalar coordinates j, let \(Q_j(t,s)\in\mathbb R^n\), \(t\ge s\), be cavity-measurable kernels that are absolutely continuous in their terminal time and satisfy

\[
 \|Q_j(s,s)\|_2+
    \int_s^\infty\|\partial_tQ_j(t,s)\|_2\,dt
 \le C\sqrt n\,b_j(s),
 \tag{24}
\]

for nonnegative cavity-measurable functions \(b_j\). Let scalar perturbations \(\Delta\theta_j(\omega,s)\) be arbitrary measurable functions of the same row, with

\[
 |\Delta\theta_j(\omega,s)|
 \le\frac{H(\omega)}{\sqrt n}a_j(s),
 \qquad
 \mathbb E_\omega H^2\le C,
 \qquad
 \sum_j\int_0^\infty a_j(s)b_j(s)\,ds\le C.
 \tag{25}
\]

Then

\[
 \mathbb E_\omega\sup_{t\ge0}
 \left|\omega^T\sum_j\int_0^t
          Q_j(t,s)\Delta\theta_j(\omega,s)\,ds\right|
 \le C/\sqrt n.
 \tag{26}
\]

**Proof.** For a fixed vector q,
\(\|\omega^Tq\|_{L^2_\omega}=\|q\|_2/\sqrt n\).
The fundamental theorem of calculus and Minkowski, applied at each fixed source time, imply

\[
 \left\|\sup_{t\ge s}|\omega^TQ_j(t,s)|\right\|_{L^2_\omega}
 \le \frac1{\sqrt n}
   \left(\|Q_j(s,s)\|_2+
            \int_s^\infty\|\partial_tQ_j(t,s)\|_2dt\right)
 \le Cb_j(s).
\]

Bound the left side of (26) pathwise by

\[
 \frac{H(\omega)}{\sqrt n}
    \sum_j\int_0^\infty a_j(s)
                \sup_{t\ge s}|\omega^TQ_j(t,s)|\,ds.
\]

Tonelli and Cauchy--Schwarz in omega, followed by (25), give (26). In particular the proof does not condition on the realized scalar-history perturbation, and does not require its independence from omega.

Here is how the lemma applies to the actual history variables already defined in the cavity note. Take
\(\theta=(r,\rho,\tau,K,V)\), where K and V are the finitely many empirical contractions there. The row-deletion bound gives

\[
 \sup_t(|\Delta\tau|+|\Delta K|+|\Delta V|)
 \le CH_i/\sqrt n.
\]

Its damped residual inequality also gives, after substituting the uniform state bound into its convolution,

\[
 |\Delta r(t)|+|\Delta\rho(t)|
 \le\frac{CH_i}{\sqrt n}(1+t)e^{-ct},
 \qquad \mathbb E_\omega H_i^2\le C.
 \tag{27}
\]

These statements hold on the prescribed row-cavity/operator events; setting perturbations to zero off the removed-row norm ball preserves the envelope when using the unconditional Gaussian integration in (26). This is a localization device for the estimate, not a conditional Gaussian claim on the full good event.

Linearize the forced state equations at the actual cavity \(\omega=0,\theta=\theta^c\). Its scalar-history response has kernels of the form
\(Q_j(t,s)=P_a(t)\Phi(t,s)U_j(s)\),
where P is the lower-feature output derivative, \(\Phi\) is the row-independent tangent evolution, and U is the vector forcing induced by the j-th scalar history. As in (21), the first two factors have a uniform operator bound and integrable terminal-time variation. For r and rho perturbations, \(\|U_j(s)\|_2\le C\sqrt n\), and their envelopes in (27) are integrable. For K,V, and tau perturbations, the forcing contains a residual or activity factor, and \(\|U_j(s)\|_2\le C\sqrt n\rho^c(s)\); the constant envelopes are therefore integrable against the kernel bound. Hence (24)–(25) hold and (26) applies.

This proves that the *cavity-linear* history correction has the required root-width weak size. The usual ordinary-norm estimate, which would multiply a state norm of order one by \(\|\omega\|_2=O(1)\), would miss this fact.

What remains is a mixed nonlinear correction. The actual field involves

\[
 H(t;\omega,\eta(\omega),\theta^n(\omega)),
\]

whereas the assumed estimate (20) controls the nonlinear row response only at \(\theta=\theta^c\). The difference after subtracting both the row tangent and the history tangent is

\[
 \begin{aligned}
 \mathcal M(t,\omega)= {}&
 H(t;\omega,\eta(\omega),\theta^n(\omega))
       -H(t;0,\theta^c)\\
 &-J_t[\eta(\omega)]\omega
       -\sum_j\int_0^tQ_j(t,s)
                    (\theta_j^n(\omega,s)-\theta_j^c(s))\,ds.
 \end{aligned}
 \tag{28}
\]

A bound \(\mathbb E\sup_t|\omega^T\mathcal M|\le C/\sqrt n\) would finish this part of scalar-history restoration, together with the direct scalar row terms. It is a strictly larger perturbation family than (20). Neither (20) nor (26) implies it by the triangle inequality: that would require a mixed derivative or remainder estimate for the hard-clip flow. It is plausible that a successful weighted energy argument for (20) could be extended to (28), but that extension has not been proved here.

### 7.3 A fixed small coefficient does not cure a selector-metric loss

Even if (28) is established, the covariance/response bias remains a distinct source estimate. The response kernel in (23) is an average of variational coefficients containing
\(\mathbf1_{\{|X_{aj}|<1\}}\).
The near-cap proposition does not make this selector Lipschitz in an ordinary L1 or L2 state metric.

The following elementary example quantifies that logical obstruction. Let U be uniform on [0,2], and for \(0<\epsilon<1/2\) let

\[
 V=U+\epsilon\mathbf1_{\{1-\epsilon<U<1\}}.
\]

Both laws have densities bounded by one. Both therefore obey a uniform linear near-cap estimate. Nevertheless,

\[
 \mathbb E|V-U|=\epsilon^2/2,
 \qquad
 \mathbb E|V-U|^2=\epsilon^3/2,
 \qquad
 |\mathbb E\mathbf1_{\{U<1\}}
   -\mathbb E\mathbf1_{\{V<1\}}|=\epsilon/2.
 \tag{29}
\]

Thus no width-independent linear bound of selector discrepancy by either displayed state norm follows from bounded densities alone. This is a counterexample to a *metric implication*, not an admissible lower-bound example for the neural flow. It does not disprove a root-width response law for the actual Gaussian system.

In particular, replacing a proposed relation
\(\mathcal D_n\le Cn^{-1/2}+q\mathcal D_n\)
by a Hölder version such as
\(\mathcal D_n\le Cn^{-1/2}+q\sqrt{\mathcal D_n}\)
does not close the rate for fixed nonzero q, however small. The latter bound admits a width-independent discrepancy of order \(q^2\). A valid strong-law contraction would need a metric in which the *actual* response-law map is Lipschitz. A weak mean-law argument may instead bypass this state-to-selector comparison by centering fluctuations and controlling a second-order remainder, as made precise in Section 7.6. Root-width strong trace coupling is sufficient but is not asserted to be necessary.

### 7.4 Why covariance interpolation still needs an additional checked lemma

For a deterministic finite-dimensional Gaussian test functional F, covariance interpolation compares its expectations through its weak second derivatives. A continuous-history version would need a time-mesh-uniform bound on the corresponding integrated second-derivative measure. The cap proposition is relevant to this: a second derivative of the clipped *state* equation produces a boundary measure at \(X=\pm1\), multiplied by first sensitivities.

But a response trace is already a first variational observable. Applying covariance interpolation directly to that trace asks for two further Gaussian derivatives. Formally, differentiating the clip selector once gives a boundary delta and differentiating twice gives its derivative, besides products with higher sensitivities. A bound on the density at the cap controls the former only after its weights are checked; it does not control the latter. A Gaussian integration-by-parts reformulation might transfer the extra derivative onto a genuinely nondegenerate current Gaussian direction and avoid inverse history Grams. Such a reformulation must be derived, with the remaining response factors and the interpolated path family verified. None of (2), (20), (22), or (26) presently supplies it.

This identifies the remaining two tasks after the hypothesized weak reinsertion proof:

1. Extend the weighted nonlinear argument to the joint row-plus-scalar-history remainder (28). The linear adaptive history contribution is already handled by (26).
2. Prove an inverse-free, selector-sensitive comparison for the joint covariance and response maps, strong enough to yield a contraction with a linear discrepancy term. This must identify the already defined own population law, rather than defining that law to equal the finite-width mean or trace.

These are not resolved by small activity alone. The small activity provides a potentially absorbable feedback coefficient once the comparison is proved; it does not supply the missing regularity of the comparison map.

### 7.5 L1 cavity control is enough if these bias steps close

No L2 row-path coupling is required by the final prediction metric. To be explicit, let \(m_n^{\rm good}(t,x)=\mathbb E[f_n(t,x)\mid\mathcal G_n]\), and suppose the completed cavity argument gives

\[
 \sup_t|m_n^{\rm good}(t,x)-f_M(t,x)|\le C_R/\sqrt n
 \quad\text{for }\|x\|\le R.
\]

For any probability query law supported in that ball, the known centered all-time concentration and the triangle inequality in \(L^2(\mathbb P(\cdot\mid\mathcal G_n)\times\mu)\) then give

\[
 \left(\mathbb E\left[
  \int\sup_t|f_n(t,x)-f_M(t,x)|^2d\mu(x)
                    \mid\mathcal G_n\right]\right)^{1/2}
 \le C_R/\sqrt n.
\]

The deterministic mean bias can be bounded by first moments of the cavity defects propagated through the bounded row observable. Hence L1 versions of (20) and (28), with appropriate activity weights and uniform bounded-query constants, are a suitable target. The conditional population bias itself remains unproved in this route.

### 7.6 A weaker mean-law closure could suffice

There is a precise way in which trace fluctuations of order \(n^{-1/4}\) could be enough. Let \(\mathcal X\) be a Banach space of all required covariance, response, and scalar-history data. Suppose the cavity data \(U_n\in\mathcal X\) have a Bochner mean \(\bar U_n\), and that conditional averaging over the removed row produces a **deterministic** functional \(\Psi(U_n)\). Include all random environment information needed for this statement in \(U_n\); an unrecorded random derivative of Psi would invalidate the centering step.

Assume Psi is twice Fréchet differentiable on every segment from \(\bar U_n\) to \(U_n\), with second derivative operator norm bounded by L. The Banach-valued integral Taylor formula gives

\[
 \Psi(U_n)-\Psi(\bar U_n)
 =D\Psi(\bar U_n)[U_n-\bar U_n]
 +\int_0^1(1-a)D^2\Psi(\bar U_n+a(U_n-\bar U_n))
              [U_n-\bar U_n,U_n-\bar U_n]\,da.
\]

Taking expectations cancels the linear term, without assuming independence between the components of \(U_n\). Therefore

\[
 \|\mathbb E\Psi(U_n)-\Psi(\bar U_n)\|
 \le\frac L2\mathbb E\|U_n-\bar U_n\|_{\mathcal X}^2.
 \tag{30}
\]

Thus a centered second moment of order \(n^{-1/2}\), corresponding to fluctuations of order \(n^{-1/4}\), already yields a root-width weak error in (30).

If a complete two-sided cavity construction gave a deterministic mean-law map \(\mathcal T\) with fixed point \(U_M\), a contraction bound
\(\|\mathcal T(U)-\mathcal T(V)\|\le q\|U-V\|\), \(q<1\),
and a mean consistency relation
\(\|\bar U_n-\mathcal T(\bar U_n)\|\le Cn^{-1/2}\),
then
\(\|\bar U_n-U_M\|\le C(1-q)^{-1}n^{-1/2}\).
Equation (30) could contribute to that consistency relation without any root-width strong trace estimate.

For the present clipped closure, this is a conditional mechanism, not a completed proof. What is still missing is a complete environment variable and two-sided mean-law map, a verified mesh-independent second-order weak expansion for its response outputs along the actual covariance/response interpolation family, and suitable centered second-moment bounds in the same norm. The upper row's smooth tanh observable alone is not the whole map: the lower response outputs retain hard-clip selectors. The one-point cap density result does not by itself establish their weak Hessian bound. This is the narrower remaining mean-law question; no stronger trace norm is imposed merely for convenience.
