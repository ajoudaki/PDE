# Continuous-time cavity response and the remaining bias obligation

2026-10-01. Scoped independent theoretical route. Scientific inputs were the complete `FITTING_AND_THRESHOLD.md`, `CLIPPED_POPULATION_ROUTE.md`, and corrected hard-clip `CONCENTRATION_ROUTE.md` in this study. No sibling bias route, other study, experiment, Git operation, or manuscript edit was used. The solve-math-rigorously and investigate-conjectures skills and their contract/audit references were applied.

**Verdict.** This route does not prove the full population bias bound. It does prove an inverse-free continuous-time cavity estimate and a quantitative response lemma: for prescribed coefficient and removed-row backward paths, the entire nonlinear response to a Gaussian row is of size $O(S^2)$, its fluctuations are $O(S^2/\sqrt n)$ uniformly over physical time, and its mean is an exact normalized response trace. Here $S$ is total residual activity. These statements keep the actual transpose and hard clipping. The still-open step is quantitative identification of that response trace for the actual dependent histories, including its bias relative to the own clipped population response. The small-activity contraction is real, but does not by itself make this missing source vanish with width.

## 1. Contract and notation

Use exactly the two-hidden-layer, order-one equations in `FITTING_AND_THRESHOLD.md`. Write $\phi=\tanh$, $\psi=\operatorname{sech}^2$, $u_a=x_a/\sqrt d$, and

\[
 h_a=\phi(Au_a),\quad
 B=W_0+\frac1{mn}\sum_b v_b k_b^T,\quad
 z_a=Bh_a,\quad g_a=\phi(z_a),\quad
 f_a=n^{-1}w^Tg_a,
\]
\[
 d_a=C_M(w\odot\psi(z_a)),\qquad
 \ell_a=C_M(\psi(Au_a)\odot B^Td_a).
\]

The residual $r=f-y$, activity rate $\rho=\|r\|_2/\sqrt m$, and clock satisfy the assigned equations. Initially $w=v=0$, $k_a=h_a(0)$, and $\tau=1$. The middle matrix has independent $N(0,1/n)$ entries and is independent of $A_0$. We take $M=1$; all statements also hold for other fixed $M>0$, with constants allowed to depend on $M$. Labels are fixed and sufficiently small, independently of width, to use the deterministic fitting theorem with the operator and Gram constants below. Tightening that fixed small-label constant is allowed; sending labels to zero with width is not used.

All-time expectations concerning actual trajectories below are restricted to the specified good events. The final target remains

\[
 \sup_{t\ge0}\left|
 \mathbb E[f_n(t,x)\mid\mathcal G_n]-f_M(t,x)\right|
 \le C_x n^{-1/2},
 \tag{1}
\]

and its requested integrated-query analogue. The own clipped population $f_M$ is the one in `CLIPPED_POPULATION_ROUTE.md`; none of the auxiliary forced systems below replaces it.

## 2. Removing one upper row: a proved all-time cavity estimate

Fix an upper-layer row $i$, let $\omega=(W_{0,ij})_{j=1}^n$, and set $W_0^{(i)}=(I-e_ie_i^T)W_0$. Run the same finite-width equations with $W_0^{(i)}$, the same $A_0$, and the same normalization $1/n$. Denote this trajectory by a superscript $c$. Its $i$-th upper coordinates remain exactly zero:

\[
 z^c_{ai}=g^c_{ai}=w_i^c=v^c_{ai}=d^c_{ai}=0.
 \tag{2}
\]

Indeed they start at zero; the reconstructed matrix has zero row $i$ whenever $v^c_{bi}=0$, and their displayed equations then have zero right-hand sides. The lower trajectory, and every nonzero upper coordinate of the cavity, are independent of $\omega$.

Choose fixed constants $K,L,\lambda>0$, with $L>1$. Consider the cavity event

\[
 \mathcal C_i=
 \{\|W_0^{(i)}\|_{\rm op}\le K,
       \ \Gamma^c(0)\succeq\lambda I_m\}.
 \tag{3}
\]

It is measurable without row $i$. On $\mathcal C_i\cap\{\|\omega\|_2\le L\}$, both initial operator norms are at most $K+L$, and the full initial Gram dominates the cavity Gram: at initialization their difference is $g_i(0)g_i(0)^T/(mn)\succeq0$. Choose the fixed label bound to apply the fitting theorem with $K+L$ and $\lambda$. Both trajectories then have exponentially decaying residuals and total activity at most a fixed $S_*$. The same initialization calculation as in the assigned concentration note gives $\Pr(\mathcal C_i^c)\le C/n$ if the limiting Gram has a fixed larger margin. No independence is claimed after conditioning on the full good event.

Define

\[
 Z_a^c(t)=\omega^Th_a^c(t),\qquad
 H_i=1+\sum_a\sup_{t\ge0}|Z_a^c(t)|,
\]

and let $D_i(t)$ be the sum of all state differences, with $A,w,v,k$ divided by $\sqrt n$, as in the concentration note. The clock difference is not divided by $\sqrt n$. Then

\[
 \sup_{t\ge0}D_i(t)\le\frac{C H_i}{\sqrt n}
 \quad\hbox{on }\mathcal C_i\cap\{\|\omega\|_2\le L\},
 \tag{4}
\]
\[
 \mathbb E_\omega[H_i^2\mid A_0,W_0^{(i)}]\le C
 \quad\hbox{on }\mathcal C_i.
 \tag{5}
\]

Here and below constants depend on fixed data, the chosen Gram/operator margins, and $M$, but not on $n$ or physical time.

**Proof of (4).** The difference of initialized matrices is $e_i\omega^T$. In the forward comparison it gives only

\[
 (W_0-W_0^{(i)})h_a^c=e_i Z_a^c,
 \tag{6}
\]

whose normalized norm is $|Z_a^c|/\sqrt n$. In the backward comparison its direct source vanishes:

\[
 (W_0-W_0^{(i)})^Td_a^c=0.
 \tag{7}
\]

The same vanishing applies with the ordinary output derivative $p_a^c=w^c\odot\psi(z_a^c)$, since $p_{ai}^c=0$. Finite-rank reconstruction differences are bounded by $C D_i$. The global clipping inequality from the assigned notes therefore bounds all vector-field differences by the usual Lipschitz terms plus $C\rho |Z_a^c|/\sqrt n$.

For completeness, one can retain residual coercivity exactly as in the assigned all-time stability proof. With $R_i=\|r-r^c\|_2/\sqrt m$, subtraction of the exact residual kernels yields

\[
 D_i'\le C\rho D_i+C R_i+
       C\rho^c\frac{H_i}{\sqrt n},
\qquad
 R_i'\le-\kappa R_i+C\rho^c D_i+
       C\rho^c\frac{H_i}{\sqrt n},
 \tag{8}
\]

in upper derivatives, after reducing the fixed small-label bound if necessary. In the potentially problematic hidden-motion kernel, the direct matrix difference pairs with $p_b^c$, so (7) applies; changes of the other factors are bounded by $D_i+H_i/\sqrt n$. The readout Gram kernel is bounded by the same quantity using (6). All other kernels contain bounded $v,k,d,p$, so their product differences obey that bound as well. Initially $D_i=R_i=0$. Integrating the second inequality and substituting it into the first gives a Gronwall inequality with coefficient $C(\rho+\rho^c)$, whose integral is bounded. This proves (4).

**Proof of (5).** Conditional on the cavity, $Z_a^c$ is a genuine Gaussian projection of a prescribed absolutely continuous Hilbert-space path. The first-feature speed bound gives

\[
 \int_0^\infty\frac{\|\dot h_a^c(t)\|_2}{\sqrt n}\,dt
 \le C S_*^2.
\]

Since $\mathbb E_\omega|\omega^Tq|^2=\|q\|_2^2/n$, Minkowski's integral inequality gives

\[
 \left(\mathbb E_\omega\sup_t|Z_a^c(t)|^2\right)^{1/2}
 \le\frac{\|h_a^c(0)\|_2}{\sqrt n}
   +\int_0^\infty
      \frac{\|\dot h_a^c(t)\|_2}{\sqrt n}\,dt
 \le1+C S_*^2.
\]

Summing the fixed number of samples proves (5). This proof uses the entire continuous history and introduces no history-Gram inverse or mesh-dependent constant.

## 3. Why (4) does not remove transpose memory

The reinserted row sees

\[
 \omega^Th_a(t)=Z_a^c(t)
       +\omega^T(h_a(t)-h_a^c(t)).
 \tag{9}
\]

Equation (4) only makes the unnormalized norm of $h_a-h_a^c$ order one. Consequently the second term in (9) is order one, not order $n^{-1/2}$. It is the causal response to the same row acting through its transpose.

There is an exact nonvanishing check. Take $m=1$, a nonzero input $u$, and a fixed nonzero small label $y$. Write $c=\|u\|_2^2$, $\alpha_j=A_{0,j}\cdot u$, $\zeta=\sum_j\omega_j\tanh\alpha_j$, and

\[
 T_n=\sum_j\omega_j^2\psi(\alpha_j)^2.
\]

For every finite initialization, both clips are inactive in a sufficiently small initial time interval, since their arguments start at zero. At time zero,

\[
 \dot w_l(0)=2y\tanh z_l(0),\qquad
 \dot d_l(0)=2y\tanh z_l(0)\psi(z_l(0)),
\]
\[
 \ddot h_j(0)=
 4y^2c\,\psi(\alpha_j)^2
 \sum_l W_{0,lj}\tanh z_l(0)\psi(z_l(0)).
\]

The cavity deletes precisely the $l=i$ term. Hence

\[
 \left.\frac{d^2}{dt^2}
  \omega^T(h(t)-h^c(t))\right|_{t=0}
 =4y^2c\,T_n\tanh\zeta\,\psi(\zeta).
 \tag{10}
\]

This is an exact finite-width identity for the original clipping placement. It is not a replacement dynamics or a positive-time uniform Taylor theorem.

Let $q_h=\mathbb E\tanh^2(N(0,c))>0$ and $q_g=\mathbb E\psi(N(0,c))^2>0$. Independent bounded summands and Gaussian second/fourth moments give

\[
 \mathbb E|T_n-q_g|^2\le C/n,\qquad
 \mathbb E\left|n^{-1}\sum_j\tanh^2\alpha_j-q_h\right|^2
 \le C/n.
\]

Conditional on $A_0$, $\zeta$ is Gaussian with the latter empirical variance. Set $U=\zeta/\sqrt{q_{h,n}}$, where $q_{h,n}=n^{-1}\sum_j\tanh^2\alpha_j>0$ almost surely. $U$ is standard Gaussian and independent of $A_0$. On this same space $Z=\sqrt{q_h}U$ obeys

\[
 \mathbb E|\zeta-Z|^2
 =\mathbb E|\sqrt{q_{h,n}}-\sqrt{q_h}|^2\le C/n.
\]

The function $\tanh z\,\psi(z)$ is bounded and Lipschitz. Thus the right side of (10) differs in $L^2$ by at most $C/\sqrt n$ from

\[
 4y^2c q_g\tanh Z\,\psi(Z),
 \tag{11}
\]

which is nonzero with probability one. This proves that a proof which simply drops the reinserted-row response loses a genuine order-one-in-width effect, even under fixed small labels.

## 4. A continuous-time forced-response lemma

The following lemma is a quantitative building block, rather than a new population model. It makes the surviving bias functional explicit.

Fix the cavity roots $A_0,W_0^{(i)}$. Prescribe scalar histories

\[
 \theta=(r_a,\rho,\tau,K_{ba},V_{ba})
\]

independently of $\omega$, where $K_{ba}$ represents $n^{-1}k_b^Th_a$, $V_{ba}$ represents $n^{-1}v_b^Td_a$, and

\[
 |r_a|\le\sqrt m\rho,\quad
 s(t)=\int_0^t\rho,\quad s(\infty)=S\le S_*,\quad
 \tau=1+s,\quad |K_{ba}|\le1,\quad
 |V_{ba}(t)|\le C s(t)^3.
 \tag{12}
\]

Also prescribe an upper-row backward history $\eta_a(t)$, independently of $\omega$, with $|\eta_a(t)|\le2s(t)$. On upper rows $l\ne i$, run the assigned $w,v$ equations using

\[
 z_{al}=(W_0^{(i)}h_a)_l+
        \frac1m\sum_bv_{bl}K_{ba},\qquad
 d_{al}=C_M(w_l\psi(z_{al})).
\]

On the lower layer run the assigned $A,k$ equations using

\[
 \ell_a=C_M\!\left(\psi(Au_a)\odot
 \left[(W_0^{(i)})^Td_a+
       \omega\eta_a+\frac1m\sum_b k_bV_{ba}\right]\right).
 \tag{13}
\]

The absent coordinate of $d_a$ is zero in the $W_0^{(i)}$ action. Let $H_a(t;\omega,\eta,\theta)=\tanh(A(t)u_a)$ denote the resulting lower features. These equations are exact algebraic components of the original system when one substitutes its actual scalar histories and its actual $d_{ai}$. In that substitution the histories depend on $\omega$, so the probabilistic assertions below cannot be invoked conditionally as though those histories were independent.

Assume $\|W_0^{(i)}\|_{\rm op}\le K$. Then, in ordinary unnormalized Euclidean norm,

\[
 \|H_a(t;\omega)-H_a(t;\widetilde\omega)\|_2
 \le C s(t)^2 e^{C_Ms(t)}
          \|\omega-\widetilde\omega\|_2.
 \tag{14}
\]

Moreover, for almost every $t$,

\[
 \|\partial_tH_a(t;\omega)-
      \partial_tH_a(t;\widetilde\omega)\|_2
 \le l(t)\|\omega-\widetilde\omega\|_2,
 \qquad
 \int_0^\infty l(t)\,dt\le C_M S^2.
 \tag{15}
\]

**Proof.** The forced equations keep $|w_l|\le2s$, $|v_{al}|\le2\sqrt m s^2$, and $|k_{aj}|\le1$, directly by integrating their equations. Their vector field is globally Lipschitz in the dynamic variables with coefficient $C_M\rho$, using the clipping inequality $ |C_M(p\psi(z))-C_M(p'\psi(z'))|\le|p-p'|+2M|z-z'|$, the fixed operator bound, and (12). Crucially, this coefficient does not involve $|\omega|_\infty$, since the gate is inside the clipping map.

For two row vectors, the only new forcing in (13) is $(\omega-\widetilde\omega)\eta_a$. If $N(t)$ is the sum of ordinary Euclidean/Frobenius differences of $A,w,v,k$, then

\[
 N'\le C_M\rho N+C\rho s
                   \|\omega-\widetilde\omega\|_2,
 \qquad N(0)=0.
\]

Integration gives $N(t)\le C s(t)^2e^{C_Ms(t)}\|\omega-\widetilde\omega\|_2$. Applying the bounded derivative of $\tanh(Au_a)$ proves (14).

To verify (15), differentiate $H_a$ along its absolutely continuous solution. Each row of $\dot A$ is bounded by $C_M\rho$ because $|\ell_{aj}|\le M$. Therefore the difference in $\psi(Au_a)\dot A u_a$ is bounded by

\[
 C_M\rho N+C\rho s\|\omega-\widetilde\omega\|_2.
\]

One may take $l(t)=C_M\rho(t)(s(t)+s(t)^2)e^{C_Ms(t)}$. Its integral is at most $C_M S^2$, because $ds=\rho\,dt$ and $S\le S_*$. This proof allows measurable prescribed histories; the ODE is understood in integral form. Hard-clip corners cause no loss in (14)–(15).

## 5. Exact mean trace and all-time quantitative row response

For the forced system of Section 4, write

\[
 F_a(t,\omega)=\omega^T[H_a(t;\omega)-H_a(t;0)],
 \qquad
 \mu_{n,a}(t;\eta,\theta)=\mathbb E_\omega F_a(t,\omega).
 \tag{16}
\]

Then

\[
 |\mu_{n,a}(t;\eta,\theta)|\le C_M S^2,
 \tag{17}
\]
\[
 \mathbb E_\omega\sup_{t\ge0}
 |F_a(t,\omega)-\mu_{n,a}(t;\eta,\theta)|^2
 \le\frac{C_M S^4}{n},
 \tag{18}
\]

and, using the weak Jacobian $J_a=D_\omega H_a$,

\[
 \mu_{n,a}(t;\eta,\theta)
 =\frac1n\mathbb E_\omega\operatorname{tr}
       J_a(t;\omega,\eta,\theta).
 \tag{19}
\]

Thus the forced forward field admits the actual continuous-time decomposition

\[
 \omega^TH_a(t;\omega)
 =\underbrace{\omega^TH_a(t;0)}_{\text{conditionally Gaussian history}}
  +\underbrace{\mu_{n,a}(t;\eta,\theta)}_{
       \text{mean causal response}}
  +\underbrace{\varepsilon_{n,a}(t)}_{
       \mathbb E_\omega\sup_t|\varepsilon_{n,a}|^2\le C_MS^4/n}.
 \tag{20}
\]

Its Gaussian history has the exact conditional covariance

\[
 C_{n,ab}(t,s;\theta)
 =\frac1n H_a(t;0,\theta)^TH_b(s;0,\theta).
 \tag{21}
\]

No inverse covariance or nonsingular history assumption enters these formulas.

**Proof.** Put $L(t)=C s(t)^2e^{C_Ms(t)}$. Since $\mathbb E\|\omega\|_2^2=1$, (14) gives $\mathbb E|F_a|\le L(t)$, proving (17). The map $H_a$ is globally Lipschitz in $\omega$; finite-dimensional Lipschitz functions have bounded weak first derivatives, and integration by parts against the Gaussian density gives

\[
 \mathbb E[\omega_j H_{aj}(t;\omega)]
 =\frac1n\mathbb E[\partial_{\omega_j}H_{aj}(t;\omega)].
\]

For clarity, the weak form follows by smoothing a Lipschitz map, integrating the smooth Gaussian identity, and passing to the limit in the weak derivative pairing; a large-radius cutoff has vanishing boundary integral because Gaussian tails dominate the bounded value and bounded first derivative. Summing over $j$, and using that $H_a(t;0)$ is independent of $\omega$, proves (19). No second derivative of the clip is required.

For almost every time, let $Q_a=\partial_tH_a$. By (15), $Q_a$ is $l(t)$-Lipschitz in $\omega$. The derivative of $\dot F_a=\omega^T[Q_a(\omega)-Q_a(0)]$ has weak norm at most $2l(t)\|\omega\|_2$. Gaussian Poincare with covariance $I/n$ therefore gives

\[
 \operatorname{Var}_\omega\dot F_a(t,\omega)
 \le\frac{4l(t)^2}{n}.
\]

The Gaussian Poincare proof in the assigned concentration note extends to these functions by a smooth cutoff and passage in the square-integrable weak gradient; both function and gradient are bounded by constants times $1+\|\omega\|_2^2$. Since $F_a(0)=0$, Minkowski's integral inequality yields

\[
 \left(\mathbb E_\omega\sup_t|F_a(t)-\mathbb EF_a(t)|^2\right)^{1/2}
 \le\int_0^\infty
       (\operatorname{Var}_\omega\dot F_a(t))^{1/2}\,dt
 \le\frac{2}{\sqrt n}\int_0^\infty l(t)\,dt.
\]

This proves (18). In particular the proof is already uniform over physical time; replacing physical time by a finer mesh cannot improve the missing identification of (19).

## 6. What small activity can absorb

For a fixed prescribed $\theta$, $H_a(t;0,\eta,\theta)$ does not depend on $\eta$: the only occurrence of $\eta$ in (13) is $\omega\eta$. Comparing two forced histories gives

\[
 \sup_t\|H_a(t;\omega,\eta,\theta)
             -H_a(t;\omega,\widetilde\eta,\theta)\|_2
 \le C_M S\|\omega\|_2
                   \|\eta-\widetilde\eta\|_\infty.
\]

Consequently

\[
 \|\mu_n(\eta,\theta)-\mu_n(\widetilde\eta,\theta)\|_\infty
 \le C_M S\|\eta-\widetilde\eta\|_\infty.
 \tag{22}
\]

When $2S<M$, the upper clip is inactive. For prescribed residual histories the single-row equations give $\|w\|_\infty\le2S$ and

\[
 \|w[z]-w[\widetilde z]\|_\infty\le C S
                       \|z-\widetilde z\|_\infty,
\qquad
 \|d[z]-d[\widetilde z]\|_\infty\le C S
                       \|z-\widetilde z\|_\infty.
\]

For the second inequality use $|\psi'|\le2$, the bound $2S$ on the readout, and the first inequality. The direct finite-rank row term $m^{-1}\sum_bv_{bi}K_{ba}$ has Lipschitz constant $C S^2$ in $z$, because $\dot v_{bi}=-2r_b d_{bi}$. Thus the deterministic response-and-finite-rank feedback of the frozen row equation has Lipschitz constant

\[
 q\le C_M S^2.
 \tag{23}
\]

Taking labels sufficiently small makes $q<1/2$. This is a legitimate contraction mechanism. If two compatible response laws had discrepancy $b_n$, their resulting row-path discrepancy would be at most $C b_n/(1-q)$, with a comparable estimate for their output moments. But (23) cannot turn a merely bounded $b_n=O(S^2)$ into $O(n^{-1/2})$. It controls propagation of response-law error; it does not produce the required width factor.

## 7. The precise unclosed bias steps

There are two necessary bridges not proved by (14)–(23).

**Dependent-history substitution.** In the actual finite system, $\eta=d_{ai}$ and $\theta=(r,\rho,\tau,K,V)$ depend on the same $\omega$. A conditional expectation which freezes their realized values does not leave $\omega\sim N(0,I/n)$. Estimate (18) is proved for every prescribed history, but a pointwise-in-history estimate cannot be evaluated at a data-dependent history without an additional uniform or causal argument. The initial Gaussian forward history in (20) also depends on $\omega$; even solving a deterministic mean-response equation driven by that Gaussian history creates this dependence. Smallness of (22) does not justify conditional Gaussian independence.

**Bias of the mean response and covariance.** Even for prescribed histories, (19) is a finite-width trace functional of the cavity environment. A sufficient genuine source theorem would prove, in an activity-weighted norm and for the compatible continuous-history response family,

\[
 \left\|\mathbb E\mu_n-\mu_M\right\|
 +\left\|\mathbb E C_n-C_M\right\|
 \le\frac{C_M}{\sqrt n},
 \tag{24}
\]

together with a causal version of (18) allowing the actual row feedback and empirical scalar histories. Here $\mu_M,C_M$ mean the response and covariance obtained from the already-defined own clipped population, not definitions chosen to equal a finite-width mean. The covariance norm must control the Gaussian histories without dividing by a smallest history-Gram eigenvalue. This is a statement about explicit response/covariance source functionals, stronger than centered prediction concentration and narrower than asserting the desired prediction theorem directly.

The weak derivative in (19) makes the difficulty concrete. The lower clip contributes the selector

\[
 \mathbf 1_{\{\,|\psi(Au_a)_j p_{aj}|<M\,\}},
 \qquad
 p_a=(W_0^{(i)})^Td_a+\omega\eta_a+
                  m^{-1}\sum_b k_bV_{ba}.
 \tag{25}
\]

First-response norms remain bounded through this selector. Comparing two response traces requires controlling changes of the selector, or using a method which avoids differentiating it. The state-Lipschitz estimates alone do not do this: arguments can differ by an arbitrarily small amount while the selector changes by one. A quantitative anti-concentration estimate for the preclip carrier near $\pm M$, plus an appropriate causal tangent comparison, would be one possible remedy. Such an estimate is not assumed or proved here. Smoothly replacing the hard clip creates second-derivative constants depending on the smoothing width, so it does not provide a uniform root-width theorem without a separate estimate.

More explicitly, a useful contraction closure would need a proved discrepancy inequality of the form

\[
 \mathcal B_n\le\frac C{\sqrt n}+q\mathcal B_n,
 \qquad q<1,
 \tag{26}
\]

where $\mathcal B_n$ controls the compatible covariance and response laws, including their actual causal histories. This route proves the possibility of the small coefficient $q=O(S^2)$ in the single-row response feedback. It does not prove the $C/\sqrt n$ term or a closed metric $\mathcal B_n$ for the joint environment response. Writing (26) without those steps would assume the decisive result.

## 8. The weighted hard-clip remainder: a sufficient estimate and its gap

The supervisor suggested using the weak weighted remainder instead of an unnormalized state Taylor remainder. The scaling is favorable, and the following precise lemma verifies it.

Let $X_j$ be a preclip carrier, let $\delta_j$ be its first-order perturbation, and let $\omega_j\sim N(0,1/n)$ be the row entry. Set

\[
 R_j=C_M(X_j+\delta_j)-C_M(X_j)-a_j\delta_j,
 \qquad a_j=\mathbf 1_{\{|X_j|<M\}}.
\]

Choosing either one-sided derivative when $X_j=\pm M$ leaves the following bound valid:

\[
 |R_j|\le|\delta_j|
       \mathbf 1_{\{\operatorname{dist}(X_j,\{-M,M\})
                                   \le|\delta_j|\}}.
 \tag{27}
\]

To prove it, write the clip increment as the integral of its piecewise constant slope along the line segment from $X_j$ to $X_j+\delta_j$. The remainder is zero unless this segment meets a corner, and the difference of slopes has absolute value at most one.

Suppose the following three additional hypotheses hold:

1. There is a sigma-field $\mathcal A$, independent of the removed Gaussian row, with $X_j$ measurable with respect to $\mathcal A$.
2. Conditional on $\mathcal A$, $(\omega_j,\delta_j)$ is jointly centered Gaussian, with $\mathbb E[\delta_j^2\mid\mathcal A]\le B^2/n$. The covariance between the two coordinates is unrestricted.
3. The unconditional carrier obeys the uniform small-ball bound
   \[
   \Pr\{\operatorname{dist}(X_j,\{-M,M\})\le u\}\le K u
   \quad(u>0).
   \tag{28}
   \]

Then

\[
 \sum_{j=1}^n\mathbb E|\omega_jR_j|
 \le \frac{C K B^2}{\sqrt n},
 \tag{29}
\]

where the case $B=0$ has zero left side.

Indeed, conditional Cauchy–Schwarz, Gaussian fourth moments, and the Gaussian tail bound give, with $d_j=\operatorname{dist}(X_j,\{-M,M\})$,

\[
 \mathbb E_\omega[
 |\omega_j\delta_j|\mathbf 1_{\{|\delta_j|\ge d_j\}}
 \mid\mathcal A]
 \le \frac{C B}{n}
       \exp\!\left(-\frac{n d_j^2}{C B^2}\right).
\]

For $a>0$, writing $e^{-ad^2}=\int_d^\infty2au e^{-au^2}\,du$ and using (28) proves

\[
 \mathbb E e^{-a d_j^2}
 \le K\int_0^\infty2au^2e^{-au^2}\,du
 \le \frac{C K}{\sqrt a}.
\]

Combining the inequalities proves (29).

This is a sufficient lemma with named hypotheses, not an assertion that they hold for the actual reinsertion. For an actual first-order response, conditional Gaussianity in hypothesis 2 would follow after proving a row-independent tangent representation with uniformly bounded coordinate response norms. Constructing and comparing that representation across clip corners is itself part of the unresolved response problem.

Nor has hypothesis 3 been verified. On the good cavity event, the fitting estimates give only the averaged bound (with expectation over that cavity law)

\[
 \frac1n\sum_j\mathbb E|X_j(t)|^2\le C S^2.
\]

For $0<u<M/2$, this yields an averaged near-cap probability at most $C S^2/M^2$, with no factor $u$. At initialization $X_j=0$, so the cap is separated from the carrier. That initial fact alone does not imply a uniform small-ball estimate at all subsequent times. The carrier uses the learned backward field and the same Gaussian columns; declaring it conditionally Gaussian would repeat the dependence gap.

A causal nondegeneracy estimate could conceivably establish (28): one would need a Gaussian direction in which the preclip carrier changes at a controlled rate, including its learned response, or an equivalent direct bound on the weighted small-ball probability in (27). Neither an operator-norm bound nor the positive initial readout Gram supplies that derivative estimate. Thus this weaker remainder norm removes a scaling objection, but its actual-density and tangent-representation hypotheses remain unproved here.

## 9. Claim status

- **Proved:** continuous-time leave-one-row normalized state error $O_{L^2}(n^{-1/2})$ on the specified good event, with no history-Gram inverse.
- **Proved:** the retained same-row transpose response has a nonzero order-one-in-width initial coefficient, with a root-width quantitative limit for that coefficient in the one-sample check.
- **Proved:** for prescribed coefficient/backward histories, the nonlinear Gaussian-row response has size $O(S^2)$, all-time centered error $O_{L^2}(S^2/\sqrt n)$, and exact mean normalized-response-trace formula.
- **Proved:** the corresponding frozen single-row deterministic response feedback is a contraction for fixed sufficiently small labels.
- **Proved conditionally:** the weighted hard-clip remainder is root width under the explicit Gaussian-tangent and near-cap small-ball hypotheses of Section 8; applicability of those hypotheses to the actual response remains open.
- **Open:** a quantitative causal response/covariance law with the bias estimate (24), and therefore the full finite-width/own-population error (1).

The failure to close (24) is a major proof gap, not a counterexample to the root-width conjecture. No independent-coordinate claim, fresh backward matrix, frozen-feature replacement, width-dependent label scale, or population defined by a finite-width mean was used.
