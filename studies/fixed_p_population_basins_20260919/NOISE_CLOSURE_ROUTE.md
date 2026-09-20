# Accepted Gaussian perturbations: a closure-specific obstruction at infinity

2026-09-19. Independent bounded theoretical route. Internally derived; not promoted. No experiments.

## Scope and outcome

Scientific inputs were read completely within the assigned scope: `docs/global_nonlinear.md` C.4.7.10.B/C.1 (lines 13161–13786), D.3 (lines 15146–15528), and this study's frozen `ESCAPE_AND_LIMITS.md`. Required rigorous-math and conjecture-investigation skills and their applicable contract, audit, and proof-search references were read. No other study, route, history, or reviewer output was consulted before freezing this report.

The process under consideration uses the exact canonical order p=1,2,3 population closure, its complete frozen joint marks, the population L2/Frobenius metric, and the actual transpose of M. Proposals are fresh iid Gaussian elements of that Hilbert state space with fixed amplitude and full support, optionally conditioned to lie in a fixed positive-radius ball. A proposal is accepted exactly when it decreases the full loss. Arbitrary prescribed nonnegative durations of exact gradient flow may intervene. The intended conclusion is almost-sure loss convergence to zero from the canonical initialization on finite compatible circle data.

**This route does not prove or disprove that intended stochastic conclusion.** It proves an actual obstruction to uniform progress, coercivity, and naive finite-observation compactness arguments: even on finite data in the source's very narrow class V_rho, there are closure states with strictly decreasing losses approaching 3/4, bounded middle matrix and readout, full gradient tending to zero, and vanishing expected gain from one fixed Gaussian proposal. Every bounded-radius proposal has vanishing possible gain uniformly along these states. These are states of the exact closure, with no changed architecture or law. Their occurrence along the accepted stochastic process from canonical initialization has not been proved.

A complementary conditional theorem replaces full-state precompactness by bounded middle/readout norms and a uniformly positive finite readout Gram matrix. Those hypotheses are directly state-checkable, but the explicit obstruction demonstrates why the Gram condition cannot be inferred from the loss bound.

## 1. Exact state and notation

For finite data `(u_i,y_i,mu_i)` with `u_i in S1`, `mu_i>0`, and sum mu_i=1, write

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\qquad
 H_i=\tanh(b_2^TMa_i),\qquad
 f_i=E_2[cH_i],\qquad L=\sum_i\mu_i(f_i-y_i)^2.
\]

The fixed canonical feature columns are bounded. Put `B_l=ess sup |b_l|`. Their first normalized coordinates are the strictly positive constants

\[
 b_{\ell,0}=\beta_\ell=(1+\eta_p)^{-1/2}.
\]

This follows directly from the prescribed first raw feature one and lower Cholesky normalization. Consequently

\[
 v_0=E_1[b_1]\ne0.
\]

The fixed probability spaces are unchanged throughout. An arbitrary finite constant field w is a legitimate element of the same lower L2 space that contains the initialized field g; it does not replace the frozen law of `(b_1,g)`.

## 2. An explicit descending positive-loss sequence within V_rho

Choose any `0<theta<min(rho,pi/4)`, with rho exactly the source's positive radius, and take three data points

\[
\begin{array}{c|c|c}
 u_i&y_i&\mu_i\\\hline
 (1,0)&+1&1/4\\
 (\cos\theta,\sin\theta)&+1&1/4\\
 (0,1)&-1&1/2.
\end{array}
\tag{1}
\]

The positive inputs are within `2rho` of e1; the negative input is e2; each label has mass one half. Thus (1) is a finite law in V_rho and is compatible with the bias-free odd model. There are no conflicting duplicate or antipodal constraints.

Let

\[
 v=(\sin(\theta/2),-\cos(\theta/2)),\quad
 \alpha=\sin(\theta/2)>0,\quad \beta=\cos(\theta/2)>\alpha.
\]

Then `v dot u_1=alpha`, `v dot u_2=-alpha`, and `v dot u_3=-beta`. Put `s=(1,-1,-1)`, so

\[
 m=\sum_i\mu_i y_i s_i=1/2.
\tag{2}
\]

Fix any `kappa>0`, let e0 be the first upper coefficient vector, and set

\[
 w_R=Rv,\qquad
 M_*={\kappa\over\beta_2|v_0|^2}e_0v_0^T.
\tag{3}
\]

This is an exact state on every canonical p=1,2,3 carrier. Its lower coefficients and upper activations are

\[
 a_i(R)=v_0\tanh(Rv\cdot u_i),\qquad
 H_i(R)=\tanh\big(\kappa\tanh(Rv\cdot u_i)\big).
\tag{4}
\]

In particular H_i(R) is constant on the upper carrier. Write

\[
 a_R=\tanh(\kappa\tanh(R\alpha)),\quad
 b_R=\tanh(\kappa\tanh(R\beta)),\quad
 \tau=\tanh\kappa>0.
\]

Thus `H(R)=(a_R,-a_R,-b_R)` and `0<a_R<b_R<tau`. For a constant readout c, the exact loss is

\[
 L_R(c)=1-2A_Rc+B_Rc^2,
 \quad A_R=b_R/2,\quad B_R=(a_R^2+b_R^2)/2.
\tag{5}
\]

Its minimum over that readout line is

\[
 c_R^{\rm opt}=A_R/B_R,
 \qquad
 \ell_R=1-{b_R^2\over2(a_R^2+b_R^2)}<3/4,
 \qquad \ell_R\longrightarrow3/4.
\tag{6}
\]

For `R>4`, choose the constant readout

\[
 c_R=c_R^{\rm opt}
       +\sqrt{{3/4+1/R-\ell_R\over B_R}}.
\tag{7}
\]

The radicand is positive by (6). Completing the square in (5) gives

\[
 S_R=(w_R,c_R,M_*),\qquad
 L(S_R)=3/4+1/R<1,\qquad c_R\longrightarrow {1\over2\tau}.
\tag{8}
\]

Thus this is a descending-loss sequence towards a strictly positive level; M and c remain bounded while `||w_R||_2=R` diverges. It already disproves coercivity of sublevels strictly below the initial loss one.

The full gradient tends to zero. To check all blocks, define `v_2=E_2[b_2]` and `r_i(R)=c_R H_i(R)-y_i`. Since H_i and c_R are constant on the upper carrier,

\[
 d_i(R)=v_2c_R(1-H_i(R)^2).
\]

The readout gradient is the constant `2 sum_i mu_i r_i H_i`, which tends to
`2tau sum_i mu_i (m s_i-y_i)s_i=0`. The middle gradient is

\[
 2c_Rv_2v_0^T\sum_i\mu_i r_i(1-H_i^2)
                           \tanh(Rv\cdot u_i),
\]

and tends to zero by the same scalar cancellation. The row gradient is bounded in L2 by a constant times
`max_i sech^2(Rv dot u_i)`, hence also tends to zero. Every constant used here is uniform for large R because M and c are bounded. Consequently

\[
 L(S_R)\to3/4,\qquad \|\nabla L(S_R)\|_{\mathcal H}\to0.
\tag{9}
\]

This is an exact sequence of approximate stationary states at infinity. It is not asserted to be a flow trajectory or an accepted-noise sample path.

## 3. Fixed proposals lose their ability to produce a fixed gain

Fix any perturbation `h=(h_w,h_c,h_M)` in the full Hilbert state space. For almost every lower mark, h_w is finite. Since every `v dot u_i` is nonzero,

\[
 \tanh((Rv+h_w)\cdot u_i)\longrightarrow s_i.
\]

Boundedness of b1 and tanh gives dominated convergence of the lower expectations:

\[
 a_i(w_R+h_w)\longrightarrow s_i v_0.
\tag{10}
\]

The upper preactivations therefore converge uniformly in the upper marks to
`s_i b_2^T(M_*+h_M)v_0`. The Lipschitz property and oddness of tanh imply

\[
 H_i(S_R+h)\longrightarrow s_i H_h,
 \qquad H_h=\tanh(b_2^T(M_*+h_M)v_0).
\]

Since `c_R+h_c` converges in L2 to `1/(2tau)+h_c`, all predictions converge to `s_i t_h`, where

\[
 t_h=E_2[(1/(2\tau)+h_c)H_h].
\]

Using (2),

\[
 L(S_R+h)\longrightarrow
 \sum_i\mu_i(s_i t_h-y_i)^2
 =1-2mt_h+t_h^2
 =3/4+(t_h-1/2)^2\ge3/4.
\tag{11}
\]

Let nu be the fixed Gaussian proposal law, either unconditioned or conditioned on any fixed positive-radius ball. Every draw belongs to the Hilbert space almost surely. Equations (8) and (11) imply, for every fixed `delta>0`,

\[
 \nu\{h:L(S_R+h)\le L(S_R)-\delta\}\longrightarrow0.
\tag{12}
\]

Indeed each indicator tends to zero for every h, so bounded convergence applies. The same reasoning applies to the accepted loss reduction: for large R it is between zero and one, and tends pointwise to zero. Hence

\[
 E_\nu\big[(L(S_R)-L(S_R+h))_+\big]\longrightarrow0.
\tag{13}
\]

The argument uses the same additive Gaussian proposals as the question. It does not replace them by random restarts or presume a particular covariance basis. In fact, (12)–(13) hold for any fixed probability law on Hilbert-valued additive increments.

### Uniform failure on every fixed perturbation ball

A stronger statement is available for bounded perturbations. Fix `epsilon>0` and suppose `||h||_H<=epsilon`. On the lower set where `|h_w|<=Ralpha/2`, every perturbed first-layer projection has its original sign and magnitude at least `Ralpha/2`. On its complement, Markov's inequality gives probability at most `4epsilon^2/(R^2alpha^2)`. Therefore

\[
 \max_i|a_i(w_R+h_w)-s_i v_0|
 \le 2B_1e^{-R\alpha}
       +{8B_1\epsilon^2\over R^2\alpha^2}.
\tag{14}
\]

The perturbed matrix and readout norms are uniformly bounded. Subtracting the upper activations and predictions as in (10)–(11) shows that for a constant C_epsilon independent of R and h,

\[
 L(S_R+h)\ge3/4
   -C_\epsilon\left(e^{-R\alpha}
                   +{\epsilon^2\over R^2\alpha^2}\right).
\]

Together with (8),

\[
 \sup_{\|h\|\le\epsilon}
      (L(S_R)-L(S_R+h))_+
 \le {1\over R}
       +C_\epsilon\left(e^{-R\alpha}
                   +{\epsilon^2\over R^2\alpha^2}\right)
 \longrightarrow0.
\tag{15}
\]

This defeats a fixed-gain bounded-radius descent lemma on the positive-loss sublevel, even before proposal probabilities are considered.

### Why finite observations do not repair this obstruction

The vectors a_i(R), predictions, middle matrices, and constant readouts all converge. Their limiting loss is 3/4. The limiting lower coefficients nevertheless do not come from any finite L2 field w: their first coordinates are `s_i beta_1`, whereas every finite field satisfies

\[
 |E_1\tanh(w\cdot u_i)|<1.
\]

Strictness holds because `|tanh(w dot u_i)|<1` almost surely; the expectation of its strictly positive deficit cannot be zero. Thus compactifying the finite observations adds a saturated boundary that is absent from the original state space. Near that boundary, two distinct training samples become indistinguishable up to the forced odd sign, and their labels cannot be fit with the remaining scalar feature. The local escape theorem for genuine Hilbert accumulation points does not apply to these added boundary states.

## 4. A conditional progress theorem that does not require w compactness

There is still a useful finite-observation route under an explicit spectral condition. Define the n-by-n readout Gram matrix and its probability-weighted version by

\[
 K_{ij}(S)=E_2[H_iH_j],\qquad
 \widetilde K(S)=\operatorname{diag}(\sqrt\mu)
                 K(S)\operatorname{diag}(\sqrt\mu).
\tag{16}
\]

If duplicate or antipodal observations are present, first combine the exactly dependent observations and compatible labels; equivalently formulate the following on the corresponding independent output subspace. For the distinct non-antipodal data (1), no such reduction is needed.

Fix constants `C,M_0,kappa_0,ell>0`, and restrict attention to proposal-time states satisfying

\[
 \|c\|_2\le C,\quad \|M\|_F\le M_0,\quad
 L\in[\ell,L_0],\quad
 \lambda_{\min}(\widetilde K)\ge\kappa_0.
\tag{17}
\]

There are constants `delta,q>0`, depending only on these fixed quantities, the data, frozen marks, and proposal law, such that every such state has conditional probability at least q of an accepted loss decrease at least delta. There is no bound or compactness assumption on w.

Here is a proof with all uniformity points explicit. The readout gradient is

\[
 g_c=2\sum_i\mu_i r_iH_i,\quad
 \|g_c\|_2^2=4r^T\operatorname{diag}(\mu)K
                    \operatorname{diag}(\mu)r
 \ge4\kappa_0 L\ge4\kappa_0\ell.
\tag{18}
\]

Also `||g_c||_2<=2sqrt(L_0)`. For any `0<t<=1/2`, changing only the readout by `-t g_c` gives the exact quadratic identity and bound

\[
 L(w,c-tg_c,M)
 =L-t\|g_c\|_2^2
       +t^2\sum_i\mu_i(E_2[g_cH_i])^2
 \le L-{t\over2}\|g_c\|_2^2
 \le L-2t\kappa_0\ell.
\tag{19}
\]

The middle inequality uses `||H_i||_2<=1`. For a conditioned radius epsilon choose additionally `t<=epsilon/(4sqrt(L_0))`, putting the target increment `(0,-t g_c,0)` inside the epsilon/2 ball. For the unconditioned law choose t=1/2.

The loss is uniformly Lipschitz for perturbations of norm at most one about these target states. To verify that no w norm is hidden here, use

\[
 |a_i(w')-a_i(w)|\le B_1\|w'-w\|_2,
\]

\[
 \|H_i'-H_i\|_2
 \le B_2B_1\big(\|M'\|_F\|w'-w\|_2
                      +\|M'-M\|_F\big),
\]

and

\[
 |f_i'-f_i|\le\|c'-c\|_2+\|c\|_2\|H_i'-H_i\|_2.
\]

All other factors are bounded by C, M_0, L_0 and the unit perturbation radius. Choose one radius r0>0 so that every proposal within r0 of its target increment loses at least `delta=t kappa_0 ell`; in the conditioned case also take `r0<epsilon/4`.

The set of target increments has compact closure in H. Indeed every upper feature has the form `tanh(b_2^T z_i)` with `|z_i|=|Ma_i|<=M_0B_1`. The parameter ball for z_i is finite-dimensional and compact, and the map into L2 is Lipschitz. The residual coefficients are in a fixed finite-dimensional bounded box because `mu_i r_i^2<=L_0`. Thus g_c ranges over the image of a compact finite-dimensional parameter set under a continuous L2-valued map.

Cover that compact target set by finitely many balls of radius r0/2 with centers in the set. Full Gaussian support gives each such ball positive probability. In the conditioned case these balls lie inside the conditioning ball. Their finite minimum is q>0, and every original target's r0 ball contains one of these smaller balls. This proves the claimed uniform probability.

As in the frozen escape argument, states satisfying (17) cannot be visited infinitely often almost surely: infinitely many visits would yield infinitely many decreases of size delta, contradicting loss nonnegativity. Taking a countable union over rational/integer bounds gives the conditional consequence:

> If along the accepted process the matrix and readout norms remain bounded and the weighted readout Gram stays uniformly positive, then L tends to zero almost surely, with or without intervening exact gradient flow. No full-state precompactness is required.

A somewhat more flexible statement follows by using recurrent visits: if on the event `L_infinity>0` there are infinitely many proposal states satisfying fixed positive bounds of the form (17), that event has probability zero.

The spectral hypothesis is substantive. In the obstruction above each H_i is constant on the upper carrier, so K has rank one at every R, while the data have three independent observations. Bounded M and c and compact observed predictions therefore do not imply it.

## 5. Claim ledger and exact remaining gap

| Claim | Status | Scope or dependency |
|---|---|---|
| Finite positive-loss sublevels are coercive in the population metric | Falsified | Explicit S_R, even within V_rho and below loss one |
| Positive-loss states have a uniform fixed-gain probability under the given Gaussian | Falsified | Equations (12)–(13), at the same data and fixed proposal law |
| Every fixed perturbation ball contains a uniformly useful loss decrease | Falsified | Equation (15) |
| Compactness of finitely many observed coefficients identifies a genuine Hilbert accumulation state | Falsified for this route | Saturated boundary a_i=s_i v0 is not represented by any finite L2 field |
| Bounded c,M and a positive readout Gram imply almost-sure zero-loss convergence | Proved conditionally | Exact unchanged accepted proposal algorithm; no w compactness |
| The accepted process from canonical initialization enters or follows the obstruction at infinity | Open | No stochastic accessibility or trapping theorem proved |
| The original algorithm forces L to zero on every finite compatible circle law | Open | Requires a trajectory-specific recurrence/progress argument or an actual stochastic obstruction |

The strongest surviving obstruction is saturation of the actual first-layer fields, followed by collision of the finite training features. It blocks the hoped-for state-uniform argument but does not show that accepted Gaussian perturbations have a positive probability of following such an escape. A proof of the original conclusion must control the reached stochastic states, or prove a divergent total conditional progress probability despite such degeneration. Replacing the Gaussian by independent draws of entire states, assuming compactness, or adding a regularizer would change the question and was not used.

Route status: **complete as an obstruction to the uniform-progress/observation-compactness approach; blocked for the original convergence theorem**. Reopen only with a trajectory-specific mechanism preventing saturation/Gram degeneration, or a construction of positive-probability stochastic escape from the prescribed initialization.
