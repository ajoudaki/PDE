# Operator route: closure order, ridge, and endpoint bridges

Status: internally derived candidate, frozen for supervisor review; no promotion.

## Scope and source coverage

The target is the exact population closure of `docs/global_nonlinear.md`, C.4.7.10.B–C, with closure order denoted by `p` (not arithmetic precision), and its comparison to the canonical nonlinear population GF. Numerical particles, quadrature, precision, neural width, and time discretization are separate limits. The primary observable is the supremum norm of prediction on the entire input circle.

Read in full: `docs/NOTATION.md`; C.4.7.9, lines 12084–12554; C.4.7.10.B–C, lines 13161–14245; C.4.7.10.D.3, lines 15146–15528. Read the `solve-math-rigorously` and `investigate-conjectures` skills and the latter's research-contract and adversarial-audit references. No other study, code, history, or route was consulted. An initial imprecise extraction also displayed lines 13135–13160, immediately before B; those lines are not used below. Source line numbers refer to the checkout read on 2026-09-20.

Established input claims are taken on the domains stated in these complete sections: C.4.7.9's fixed short interval and family, the represented short-time family in B–C, or D.3's explicitly supported time-40 family. Nothing below extends canonical GF existence or identification beyond these domains without a named hypothesis. Fixed-order closure existence on every finite interval is already proved there.

This route contains theoretical derivations only. There were no numerical experiments. Its sources and error quantities are proof observables, never inputs to the closure initializer or dynamics.

Independence note: after the complete initial draft below had been written, the supervisor sent its independently obtained variational-defect/mobility-order identity and a square-summability consequence for filter increments. The identities already present in Sections 1 and 3 predate that message. The supervisor's square-summability consequence is not used in this route's proofs.

## 1. Common-carrier representation and the exact metric

Work on the fixed initialized observable Hilbert spaces `H_l=L2(Omega_l)`, with actual adjoint `A_0^*`, `||A_0||<=2`, and the chapter's tanh, loss, and physical-time conventions. Let

\[
 S_{l,p}a=\psi_{l,p}^{T}a,\quad
 T_{l,p}=S_{l,p}S_{l,p}^{*},\quad
 V_{l,p}=\operatorname{ran}S_{l,p},\quad
 \eta_p=[1024(p+1)^2]^{-1}.
\]

The raw lists are nested up to permutation. An earlier literal that occurs in a later polynomial list is retained there instead of twice; this changes its position, not its presence. Thus `T_{l,p+1}-T_{l,p}` is a sum of new positive rank-one operators. Exact functional duplicates, when literally distinct, contribute separate rank-one terms as prescribed by the dictionary.

Let `G=S^*S`, `LL^T=G+eta I`, and `U=S L^{-T}`. The positive filter is

\[
 Q_{l,p}=UU^{*}=S(G+\eta_p I)^{-1}S^{*}
 =T_{l,p}(T_{l,p}+\eta_p I)^{-1}.
 \tag{1}
\]

The last identity follows by applying both sides to each nonzero singular vector of `S`, and to its orthogonal complement, where both vanish. Hence `Q` has range `V`, is strictly positive on `V`, and satisfies `0<=Q<=I`; it is not a projection.

Define, on the Hilbert–Schmidt operator space from `H_1` to `H_2`,

\[
 \mathscr P_p Z=Q_{2,p}ZQ_{1,p},\qquad
 B_p=Q_{2,p}A_0Q_{1,p},\qquad
 K_p=U_{2,p}(M_p-D_p)U_{1,p}^{*},\quad A_p=B_p+K_p.
 \tag{2}
\]

For a state `theta=(w,K,c)` with action `A=B+K`, set

\[
 h=\tanh(w\cdot u),\quad H=\tanh(Ah),\quad
 \delta=c\,[1-H^2],\quad q=A^{*}\delta,\quad
 f=E_2[cH],\quad r=f-y,
\]
\[
 F_w=-2\int r(1-h^2)q\,u\,d\mu,\quad
 F_K=-2\int r\,\delta\otimes h\,d\mu,\quad
 F_c=-2\int rH\,d\mu.
 \tag{3}
\]

Then the closure is exactly

\[
 w_p'=F_w(w_p,A_p,c_p),\quad
 K_p'=\mathscr P_p F_K(w_p,A_p,c_p),\quad
 c_p'=F_c(w_p,A_p,c_p),\qquad
 (w_p,K_p,c_p)(0)=(g,0,0).
 \tag{4}
\]

The canonical dynamics instead use `B=A_0` and the identity in place of `mathscr P_p`. Thus order changes the initial action and the middle-block mobility. The row and readout population metrics remain their ordinary `L2` metrics. Their fields are arbitrary evolving functions of the retained marks; they are not polynomial coefficient vectors of degree `p`.

There is nevertheless a useful exact positive ordering:

\[
 0\le Q_{l,p}\le Q_{l,p+1}\le I,\qquad
 0\le\mathscr P_p\le\mathscr P_{p+1}\le I.
 \tag{5}
\]

To prove the first assertion, `T_{p+1}/eta_{p+1}>=T_p/eta_p`. For positive invertible `R<=S`,

\[
 \langle v,R^{-1}v\rangle
 =\sup_x\{2\langle v,x\rangle-\langle x,Rx\rangle\}
 \ge \langle v,S^{-1}v\rangle.
\]

Apply this to `I+T/eta` and use `Q=I-(I+T/eta)^{-1}`. For the second assertion expand

\[
 (\mathscr P_{p+1}-\mathscr P_p)Z
 =(Q_{2,p+1}-Q_{2,p})ZQ_{1,p+1}
 +Q_{2,p}Z(Q_{1,p+1}-Q_{1,p}).
\]

Each term has nonnegative quadratic form: for positive `R,S`,
`<Z,RZS>_HS=||R^{1/2}ZS^{1/2}||_HS^2`.

The minimum coefficient norm inducing a middle variation `Z`, supported between `V_{1,p}` and `V_{2,p}`, is

\[
 \|Z\|_{p}^{2}
 :=\min_{U_{2,p}XU_{1,p}^{*}=Z}\|X\|_F^2
 =\langle Z,\mathscr P_p^{\dagger}Z\rangle_{\rm HS}
 =\|Q_{2,p}^{\dagger/2}ZQ_{1,p}^{\dagger/2}\|_{\rm HS}^{2}.
 \tag{6}
\]

Here the dagger means inverse on the finite-dimensional range and zero on its orthogonal complement. For the linear map `R:X -> U_2 X U_1^*`, `RR^*=mathscr P`; its singular-vector decomposition proves the minimum formula, with the minimizing lift in `(ker R)^perp`. In particular no redundancy is silently deleted from the operational equations.

Extend (6) to infinity outside its supported space. The same variational formula used above gives, on the old supported space,

\[
 \|Z\|_{p+1}^{2}\le\|Z\|_p^{2}.
 \tag{7}
\]

These are nested supports and decreasing induced norms, rather than a single unchanged metric restricted to growing subspaces. For a single feature field the exact norm is

\[
 \min_{Ua=v}|a|^2=\|v\|_2^2+\eta_p\|S_{l,p}^{\dagger}v\|^2.
 \tag{8}
\]

Indeed write `v=S b`; its normalized coefficients are `a=L^T b`, so `|a|^2=||v||^2+eta|b|^2`, and minimize over `b`. Equation (8) displays the ridge's metric contribution explicitly. In (6), writing `Q_l^dagger=I_V+eta T_l^dagger` also expands the middle norm into its HS norm, two positive terms linear in `eta`, and one positive term quadratic in `eta`.

At an identical common state, the middle contribution to the tangent kernel increases in positive quadratic-form order under (5). Along actual training paths the state and `B_p` differ, so no such comparison of the full evolving kernels follows.

## 2. Quantitative ridge effects and what positive ordering does not imply

For the same fixed raw list at two ridges `eta>eta'>0`, diagonalization gives the exact operator-norm difference

\[
 \|Q_{\eta'}-Q_\eta\|
 =\max_{\lambda\in\operatorname{spec}(T),\lambda>0}
 \frac{\lambda(\eta-\eta')}{(\lambda+\eta)(\lambda+\eta')}
 \le\frac{\sqrt\eta-\sqrt{\eta'}}{\sqrt\eta+\sqrt{\eta'}}.
 \tag{9}
\]

The upper bound follows by maximizing over `lambda>=0`; its derivative changes sign at `lambda=sqrt(eta eta')`. A positive minimum eigenvalue `lambda_*` on the retained range instead gives the sharper bound `(eta-eta')/lambda_*`. Neither bound silently assumes a well-conditioned raw Gram.

For the scheduled adjacent ridges, the universal bound in (9) is `1/(2p+3)`, if the raw list is unchanged. With fixed lists on both layers and differences `d_l=||Q_{l,eta'}-Q_{l,eta}||`,

\[
 \|B_{\eta'}-B_\eta\|\le2(d_1+d_2),\qquad
 \|\mathscr P_{\eta'}-\mathscr P_\eta\|\le d_1+d_2.
 \tag{10}
\]

These follow by adding and subtracting one mixed product. They isolate ridge effects from feature enrichment. They do not bound enrichment by the ridge change.

In the exact symmetric population construction, orders one and two have identical active odd raw lists. The source's invariant-subsystem argument therefore gives identical trajectories at matched ridge. With the maintained schedule, this is instead a ridge perturbation problem on those active lists. At `p=1`, the universal spectral bound is `1/5`; a useful much smaller bound needs the actual active Gram spectrum and a dynamical stability constant. A small numerical difference under unmatched ridge or nonsymmetric quadrature is not an exact parity theorem.

Even (5) does not imply that `||(I-Q_p)v||` decreases. A finite-dimensional example is

\[
 I-Q_p=\begin{pmatrix}1&0\\0&1/10\end{pmatrix},\qquad
 I-Q_{p+1}=\begin{pmatrix}1/2&3/20\\3/20&1/20\end{pmatrix}.
\]

Both are positive contractions and their difference is positive, but their norms on `v=(0,1)` are `1/10` and `sqrt(1/40)`, respectively. These filters can arise from nested raw frame operators at common ridge one: `T_p=diag(0,9)` and

\[
 T_{p+1}=\begin{pmatrix}19&-60\\-60&199\end{pmatrix},\qquad
 T_{p+1}-T_p=\begin{pmatrix}19&-60\\-60&190\end{pmatrix}\ge0.
\]

Thus neither squared operator defects nor nonlinear prediction errors inherit monotonicity merely from mobility ordering. This example concerns the inference from operator ordering, not a counterexample to a particular canonical GF trajectory.

## 3. Source bounds with an explicit approximation criterion

Define the regularized raw approximation error

\[
 a_{l,p}(v)^2
 :=\inf_z\{\|v-S_{l,p}z\|_2^2+\eta_p|z|^2\}
 =\langle v,(I-Q_{l,p})v\rangle.
 \tag{11}
\]

The minimizer solves `(G+eta I)z=S^*v`; substituting proves the equality. Therefore `a_{l,p}(v)` is nonincreasing in `p`, and

\[
 \|(I-Q_{l,p})v\|_2\le a_{l,p}(v),\qquad
 \|(Q_{l,p+1}-Q_{l,p})v\|_2\le a_{l,p}(v).
 \tag{12}
\]

For the first inequality use `(I-Q)^2<=I-Q`. For the second set `D=Q_{p+1}-Q_p`, note `0<=D<=I-Q_p<=I`, and use `D^2<=D<=I-Q_p`. These square inequalities are for each one positive contraction; they do not assert operator monotonicity of squaring two different operators.

Fix an admitted canonical trajectory through `T`, with `|y|<=Y`, `L(t)<=Y^2`, and `||c(t)||_infty<=2YT`. All suprema below are over `t<=T,u in S^1`. Define

\[
 a_H=\sup a_{1,p}(h),\quad a_{AH}=\sup a_{2,p}(A_0h),\quad
 a_D=\sup a_{2,p}(\delta),\quad a_{AD}=\sup a_{1,p}(A_0^*\delta).
\]

For the source error appearing in the established comparison theorem,

\[
 \epsilon_p(T)=\sup\|(B_p-A_0)h\|_2
 +\sup\|(B_p^*-A_0^*)\delta\|_2
 +\sup_{t\le T}\|(\mathscr P_p-I)K'(t)\|_{\rm HS},
\]

one has the explicit bound

\[
 \epsilon_p(T)\le
 (2+4Y^2T)a_H+a_{AH}+(2+2Y)a_D+a_{AD}.
 \tag{13}
\]

For example,
`(B_p-A_0)h=Q_2 A_0(Q_1-I)h+(Q_2-I)A_0h`, giving `2a_H+a_AH`; the adjoint bound is `2a_D+a_AD`. Finally insert the exact rank equation from (3), subtract its two factors, and use `int|r|dmu<=Y`, `||h||<=1`, `||delta||<=2YT`:

\[
 \|(\mathscr P_p-I)K'\|_{\rm HS}
 \le2\int |r|\,[\|(I-Q_2)\delta\|_2\|h\|_2
       +\|Q_2\delta\|_2\|(I-Q_1)h\|_2]d\mu
 \le 2Ya_D+4Y^2Ta_H.
\]

Thus a separate approximation theorem for the entire HS derivative curve is unnecessary once these four vector target sets are controlled.

For example, suppose each of those target fields, uniformly in `t,u`, has a raw coefficient approximation with error at most `d_p` and coefficient norm at most `A_p`. Then

\[
 \epsilon_p(T)\le C_{Y,T}\sqrt{d_p^2+\eta_p A_p^2}
 \le C_{Y,T}\left(d_p+\frac{A_p}{32(p+1)}\right).
 \tag{14}
\]

This is an explicit sufficient approximation condition, not a regularity statement already proved for the GF fields. Its ridge term is an upper bound, not an actual error lower bound or a proof of an algebraic convergence ceiling. Raw coefficient growth and frame redundancy matter.

If one wants the sharper coefficient constant for the operator defect itself, diagonalization gives `||(I-Q)S z||<=sqrt(eta)|z|/2`; consequently `||(I-Q)v||<=inf_z{||v-Sz||+sqrt(eta)|z|/2}`. Equation (13) remains valid if each of its four regularized errors is replaced by this latter bound. The form (11) has the additional advantage of monotonicity in order, so the right side of (13) is a nonincreasing source bound for a fixed reference trajectory.

The source proves the compactness and density needed for `epsilon_p(T)->0`, but gives no order-dependent bounds for `d_p,A_p` on these target sets. Polynomial degree in the core cannot supply the missing estimate by itself: the full initialized observable spaces need not equal the spaces generated by the fixed four/two Gaussian core marks, and the exhaustive action-word tail is essential to the proved density argument.

Density and compactness alone allow arbitrarily slow convergence. To see the logical obstruction, consider any nested finite-dimensional ranges in an infinite-dimensional Hilbert space. Given a proposed positive rate `r_p->0`, choose indices `p_k` with `r_{p_k}<=k^{-2}` and orthonormal `v_k` perpendicular to `V_{p_k}` and to their predecessors. The vector `v=sum k^{-1}v_k` belongs to the Hilbert space. Since `Q_{p_k}` has range in `V_{p_k}`, its error has `v_k` component `1/k`, so `||(I-Q_{p_k})v||/r_{p_k}>=k`. Even the singleton `{v}` is compact. This disproves a rate inferred solely from those two hypotheses; it does not disprove additional regularity, or a rate for the canonical target family.

## 4. Finite-time predictor bounds for original nonlinear GF

On the supported time-40 domain, or the short-time Gaussian-tail domain in part B, the source's one-reference subtraction yields, with constants independent of `p,R`,

\[
 D^+e_p\le C_T(1+R)(e_p+\epsilon_p)
       +C_TM_T e^{-a_TR^2},\quad e_p(0)=0,
\]
\[
 e_p=\|w_p-w\|_2+\|K_p-K\|_{\rm HS}+\|c_p-c\|_2,
 \qquad \|f_p-f\|_{C(S^1)}\le C_T(e_p+\epsilon_p).
 \tag{15}
\]

This comparison concerns the original canonical GF, and only the unchanged reference backward query needs Gaussian tails. Integrating and choosing
`R=max(1,sqrt(a_T^{-1} log(M_T/epsilon)))`, for sufficiently small positive `epsilon`, gives a whole-circle finite-time modulus of the form

\[
 \sup_{t\le T}\|f_p(t)-f(t)\|_{C(S^1)}
 \le \Phi_T(\epsilon_p(T)),
\]
\[
 \Phi_T(\epsilon)=C_T\epsilon
       [1+\sqrt{\log(C_T/\epsilon)}]
       \exp\!\big(C_T\sqrt{\log(C_T/\epsilon)}\big),
 \quad \Phi_T(0)=0.
 \tag{16}
\]

Constants can be enlarged to make the logarithm positive on the chosen small-error interval. Indeed the integrated bound is a constant times
`exp(C_T R)[(1+R)epsilon+M_T exp(-a_T R^2)]`, and the chosen cutoff makes the second summand equal to `epsilon`. The case `epsilon=0` follows by taking `R` to infinity in (15).

For every fixed `0<beta<1`, (16) is at most `C_{T,beta} epsilon^beta` for sufficiently small `epsilon`: with `x=log(C_T/epsilon)`, both `sqrt(x)` and `log(1+sqrt(x))` are `o(x)`. This is stronger than fixing one Hölder exponent when Gaussian tails are available, but it is not a Lipschitz estimate. C.4.7.9's weaker stated exponential-tail input separately gives its displayed exponent `exp(-LT)`.

In particular the same canonical reference yields

\[
 \sup_{t\le T}\|f_{p+1}(t)-f_p(t)\|_{C(S^1)}
 \le\Phi_T(\epsilon_p(T))+\Phi_T(\epsilon_{p+1}(T)).
 \tag{17}
\]

It follows that adjacent differences vanish on every horizon actually covered by the canonical comparison theorem. The assertion does not say that errors are monotone or that adjacent differences are asymptotically one order smaller than reference errors. For a conditional source rate `epsilon_p<=C p^{-s}`, (16) gives `p^{-s+o(1)}`, or any fixed power `p^{-s beta}`, `beta<1`. No `p`-rate follows without a source estimate such as (14).

## 5. A finite-order adjacent certificate without a canonical target

There is also a direct comparison using only the exact order-`p` path as reference. Set `q=p+1`. At time `t`, let

\[
 \sigma_{q|p}(t)=
 \sup_u\|(B_q-B_p)h_p(t,u)\|_2
 +\sup_u\|(B_q^*-B_p^*)\delta_p(t,u)\|_2
 +\|(\mathscr P_q-\mathscr P_p)F_K(w_p,A_p,c_p)\|_{\rm HS}.
 \tag{18}
\]

These are cross-order contractions on their common initialized carrier, obtained by the union of the two finite initialization programs and the saved order-`p` fields. They need no future target trajectory, although evaluating their exact continuum suprema and integrals is a separate numerical certification problem.

For every finite `T`, the reference `q_p=A_p^*delta_p` is bounded in `L-infinity`: its feature representation gives
`||q_p(t,u)||_infty<=K_{1,p}||M_p(t)||_op||d_p(t,u)||`, where `K_{1,p}` is the finite feature envelope. Let its supremum be `J_{p,T}<infinity`. The source's forward and backward subtractions now give, for
`e_{q,p}=||w_q-w_p||_2+||K_q-K_p||_HS+||c_q-c_p||_2`,

\[
 D^+ e_{q,p}(t)\le L_{p,T}e_{q,p}(t)+C_T\sigma_{q|p}(t),
 \quad e_{q,p}(0)=0,
\]
\[
 e_{q,p}(t)\le C_T\int_0^t e^{L_{p,T}(t-s)}\sigma_{q|p}(s)ds,
\]
\[
 \|f_q(t)-f_p(t)\|_{C(S^1)}
 \le C_T\left[e_{q,p}(t)
       +\sup_u\|(B_q-B_p)h_p(t,u)\|_2\right].
 \tag{19}
\]

Here `L_{p,T}` depends on `J_{p,T}`; `C_T` uses only the common raw/action energy bounds and `Y,T`. To verify the sole non-Lipschitz-looking product, write
`(1-h_q^2)q_q-(1-h_p^2)q_p=(1-h_q^2)(q_q-q_p)+(h_p^2-h_q^2)q_p` and bound its second term by `2J_{p,T}||w_q-w_p||_2`. For the middle equation use exactly

\[
 K_q'-K_p'=
 \mathscr P_q(F_K(w_q,A_q,c_q)-F_K(w_p,A_p,c_p))
 +(\mathscr P_q-\mathscr P_p)F_K(w_p,A_p,c_p).
\]

All remaining terms follow by subtracting bounded tanh factors and rank products. This proves (19) directly, without a target-tail assumption. It is a conditional certificate in terms of a measurable omitted source, not a guaranteed useful small bound. Its feature-envelope constant can grow rapidly with order. Small neighboring prediction differences alone do not estimate (18) and are not an endpoint certificate.

## 6. An explicit original-GF endpoint bridge

Fixed-time identification does not permit `t->infinity`. A sufficient additional hypothesis can be expressed entirely in the original GF, without changing its optimizer.

For each exact closure define its current tangent kernel with the chapter's weighted population metric. From (3)–(4), its diagonal satisfies

\[
 K_p(t;u,u)\le k_Y(t)
 :=1+4Y^2t^2\{1+(2+2Y^2t^2)^2\}.
 \tag{20}
\]

Indeed its three terms are `||H_p(u)||_2^2<=1`,
`||U_2^*delta_p||^2||U_1^*h_p||^2<=||c_p||_2^2`, and
`||(1-h_p^2)A_p^*delta_p||_2^2<=||A_p||^2||c_p||_2^2`, with `||c_p||_infty<=2Yt` and `||A_p||<=2+2Y^2t^2`. The identical estimate applies to canonical GF on any interval where it exists with its energy identity, using identity filters. Gram-kernel Cauchy–Schwarz gives `|K_p(t;u,v)|<=k_Y(t)`.

Assume, in addition, that for every order under comparison and all `t>=0`, the kernel is coercive along the actual training residual:

\[
 \iint r_p(u,y)K_p(t;u,v)r_p(v,z)\,d\mu(u,y)d\mu(v,z)
 \ge\lambda\|r_p(t)\|_{L^2(\mu)}^2,
 \qquad \lambda>0,
 \tag{21}
\]

with the same `lambda`. This is only a residual-direction condition; it does not demand a positive gap on all of an infinite-dimensional data space. It is not established by the supplied sources.

The loss identity gives `L_p'<=-4lambda L_p`, hence
`||r_p(t)||<=Y exp(-2lambda t)`. The prediction equation then gives

\[
 \|\partial_t f_p(t)\|_{C(S^1)}
 \le2k_Y(t)\|r_p(t)\|_{L^2(\mu)}
 \le2Y k_Y(t)e^{-2\lambda t}.
\]

Its time integral is finite, so the predictors are Cauchy in `C(S^1)` and have endpoints satisfying the uniform tail estimate

\[
 \|f_p(\infty)-f_p(T)\|_{C(S^1)}
 \le b(T):=2Y\int_T^\infty k_Y(t)e^{-2\lambda t}dt.
 \tag{22}
\]

Consequently the actual nonlinear GF endpoints obey

\[
 \|f_q(\infty)-f_p(\infty)\|_{C(S^1)}
 \le\|f_q(T)-f_p(T)\|_{C(S^1)}+2b(T),
 \tag{23}
\]

where (19), or (17) on an admitted canonical horizon, bounds the finite-time term. Thus this is an endpoint bound for original GF under a stated dynamical hypothesis, not a ridge-regression or frozen-kernel replacement.

To deduce convergence to the canonical fitted endpoint as `p->infinity`, additionally require: canonical GF exists and is identified with the closure limit on every finite horizon, and (21) holds for that canonical flow and uniformly for sufficiently large `p`. Then

\[
 \|f_p(\infty)-f(\infty)\|_{C(S^1)}
 \le\Phi_T(\epsilon_p(T))+2b(T),
 \tag{24}
\]

first `p->infinity` at fixed `T` and then `T->infinity` proves endpoint convergence. An actual rate requires control of `epsilon_p(T)` and the stability constants when `T` grows with `p`. D.3 only supplies the identification through `T=40`; its existence/tail statements cannot be substituted for the additional all-time hypotheses in this argument.

More generally (23) needs only an order-uniform integrable upper bound on `||partial_t f_p||_infty`. Assumption (21) is an explicit sufficient condition. The energy identity alone supplies an integral of squared state speed, which does not supply this integrable prediction speed or a fitted endpoint.

## 7. Failure routes, hostile checks, and claim status

* **A single fixed Galerkin metric:** false for the actual positive-ridge construction. Equations (6)–(8) identify the changed metric. The stronger correct fact is increasing middle mobility, not metric equality.
* **Nested mobility implies identical or monotonically improving fitted functions:** unsupported. Even the elementary loss `(x_1+x_2-1)^2`, started at zero with constant mobility `diag(a,b)`, converges to `(a,b)/(a+b)`. The off-training observable `x_2` therefore changes from `1/2` to `1/3` to `2/3` for the ordered mobilities `diag(1,1)<=diag(2,1)<=diag(2,4)`. This is a logical counterexample to that implication, not a canonical-network counterexample. All endpoints interpolate the same training datum.
* **The ridge schedule alone gives a prediction rate:** unsupported. It controls (9) for a fixed list; enrichment and target coefficients remain in (13)–(14).
* **Fast Chebyshev approximation in a fixed finite Gaussian core:** not a complete argument for this hierarchy. The full observable action spaces need not be that core's function spaces; the exhaustive word tail remains a separate approximation axis.
* **A small adjacent gap certifies the infinite-order limit:** unsupported without a summable tail bound, contraction across orders, or an independent source estimate. A sequence can have small successive increments while accumulating a large remaining tail.
* **Energy or finite-dimensional analyticity supplies a population endpoint:** not established. Exact finite-order closures retain continuum laws, so finite-dimensional analytic-gradient theorems cannot simply be imported; the squared-speed energy bound is insufficient for time-integrable speed.
* **Canonical fixed-horizon comparison implies fitted-endpoint comparison:** open without a uniform time-tail bridge. Equations (21)–(24) state a sufficient bridge and keep its missing hypotheses explicit.

Proved internally in this route: exact operator/metric formulas (1)–(8), ridge perturbations (9)–(10), regularized approximation identity and source estimate (11)–(14), Gaussian-tail optimization and adjacent finite-time estimate (16)–(17), the direct finite-order comparison (18)–(19), and the conditional original-GF endpoint bridge (20)–(24). These are candidates for independent checking, not established additions to `docs/`.

The decisive missing input for a quantitative order rate is approximation of the four reachable target sets in (13) with controlled raw coefficients. The decisive additional input for fitted endpoints is an order-uniform integrable prediction-time tail, for example (21), together with all-time canonical identification if that endpoint is the target. Neither is supplied by the canonical construction reviewed here.
