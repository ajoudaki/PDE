# Removing width dependence: what can and cannot be strengthened

This note investigates the two response-memory theorems in `paper/main.tex` at commit `7ffb91f`. The target is the same canonical deep nonlinear gradient flow and the same two memory algorithms. No initialization matrix is discarded. The main theorem has not been changed.

The conclusions are:

1. A uniform version of the current **unnormalized parameter** theorem is false over its arbitrary-initialization class with fixed population-scale bounds: exact replication gives a counterexample for the learning-speed closure at every fixed finite order.
2. For bounded activations with bounded slopes, the learning-speed closure's **accumulated absolute internal velocity defect** has a width-independent `O(P^-1)` bound under width-independent initial operator/readout RMS bounds. This improves the explicit finite-width proof's use of Frobenius bounds on initialization.
3. A width-independent `O(P^-1)` trajectory and test-prediction theorem follows under a concrete additional bound on the dense reference's reverse fields. This assumption is not established for the Gaussian network family in the paper.
4. The original joint clock has a width-independent `O(P^-2)` defect estimate if its normalized response variation is bounded uniformly. Appendix E already contains this sharper estimate. Controlling that variation and feedback in the intended Gaussian regime remains open here.

The counterexample in item 1 is not a counterexample to a Gaussian-typical predictor theorem. The failure of an ambient Lipschitz estimate below is also not an impossibility theorem for every probabilistic stability argument.

## 1. Exact obstruction in the theorem's present norm

Use one datum `x=1`, label `y=2`, two tanh hidden layers, and canonical mobilities `(n,1,n)`. For every width set

\[
 W^{(1)}=u\mathbf1_n,\qquad W^{(2)}=\frac an\mathbf1_n\mathbf1_n^T,
 \qquad w=c\mathbf1_n,
 \qquad u(0)=a(0)=c(0)=1.
\]

These are admissible finite initializations for the deterministic theorem, though not i.i.d. Gaussian initializations. Their scales are uniformly controlled: both outer RMS norms and the middle operator/Frobenius norm equal one initially. The network is nonlinear in both layers. Put

\[
 h=\tanh u,\quad g=\tanh(ah),\quad r=cg-2,
 \quad s=1-h^2,\quad v=1-g^2.
\]

The dense flow preserves this form and reduces exactly to

\[
 \dot u=-2racvs,\qquad \dot a=-2rcvh,\qquad \dot c=-2rg.
\tag{1}
\]

None of these equations contains `n`. The learning-speed closure also preserves this form. Its vector moments are repetitions of scalar moments; its scalar reconstructed middle weight is

\[
 \widehat a=1-\frac2\tau\sum_{k<P}(2k+1)B_kH_k.
\tag{2}
\]

Its clock, moment equations, and outer equations likewise contain no `n`. Thus its per-neuron errors are identical at every width.

For completeness, this error is nonzero for **every fixed finite P**, not just for a numerically selected order. Work near time zero, where `r<0`, so `rho=-r` and the scalar backward history is `b=-cv`. The forward prefix is constant `h(0)` and the backward prefix is zero. At initialization the projected endpoints satisfy

\[
 h^*(0)=h(0),\qquad \dot h^*(0)=0,\qquad b^*(0)=0.
\tag{3}
\]

Indeed, `H_0(0)=h(0)`, other `H_k(0)=0`, `dot H_0(0)=rho_0 h(0)`, and `dot H_k(0)=0` for `k>=1`; differentiating `h*=tau^-1 sum (2k+1)H_k` cancels the zeroth-mode contribution. This holds for every finite P.

The exact middle velocity defect is `E_a=2 rho(b-b*)(h-h*)`. Therefore

\[
 E_a(0)=0,\qquad E_a'(0)=2\rho_0b_0\dot h_0,
 \qquad \widehat a(t)-a(t)=\rho_0b_0\dot h_0t^2+O_P(t^3).
\tag{4}
\]

Here `dot h_0=-2r_0v_0s_0^2>0`, and `rho_0 b_0=r_0v_0<0`. The state-dependent vector-field difference affects (4) only at its next order. For the readout field `F_c=-2(cg-2)g`,

\[
 \partial_aF_c\big|_0=-2(2g_0-2)h_0v_0>0.
\]

Since the outer errors start at order three, Taylor expansion of their unchanged equations gives

\[
 \widehat c(t)-c(t)
 =\frac{\partial_aF_c|_0\,\rho_0b_0\dot h_0}{3}t^3+O_P(t^4).
\tag{5}
\]

The coefficient is strictly negative (approximately `-0.0480306554`). Consequently, for every fixed P and every `T>0`, there is a time `t_P in (0,T]` and a number `d_P>0`, both independent of width, with `|c_hat(t_P)-c(t_P)|=d_P`. But

\[
 \|\widehat w(t_P)-w(t_P)\|_2=\sqrt n\,d_P.
\tag{6}
\]

No finite width-independent constant can bound this by `C_T/P` for all widths. Allowing a width-independent finite threshold `P_0` does not help: fix any integer `P>=P_0` and then increase n. Allowing the constant to depend on the unnormalized initial outer norm merely hides width dependence in `sqrt(n)`.

This proves an obstruction to the literal unnormalized strengthening. It does **not** obstruct a normalized parameter or output statement: the replicated predictors and their errors are themselves independent of width. Nor does this construction establish failure under the paper's i.i.d. Gaussian initialization law.

## 2. Width-independent production of the learning-speed defect

Consider arbitrary fixed depth L and finite training data. Let `X=max_a ||x_a||/sqrt(d)` and `Y=(m^-1 sum y_a^2)^(1/2)`. Assume globally bounded activations and slopes, with

\[
 |\phi_\ell|\le A_\ell,\qquad |\phi'_\ell|\le s_\ell,
 \quad \|W_0^{(\ell)}\|_{op}\le\kappa_\ell\ (\ell\ge2),
 \quad \|w_0\|_2/\sqrt n\le B_0.
\tag{7}
\]

The displayed bounds are independent of width; the initialized matrices themselves remain unchanged. Assume the activation regularity in the learning-speed theorem for local uniqueness. Define

\[
 B=(B_0^2+Y^2T)^{1/2},\qquad q=A_LB+Y,
 \qquad S=qT,\qquad M=1+S.
\tag{8}
\]

The unchanged readout equation yields

\[
 \frac d{dt}\frac{\|w\|_2^2}{n}
 =-\frac4m\sum_a(f_a-y_a)f_a
 =Y^2-\frac4m\sum_a(f_a-y_a/2)^2\le Y^2.
\tag{9}
\]

Thus both dense and closure flows satisfy `||w||/sqrt(n)<=B`, `rho<=q`, and the old clock satisfies `tau<=M`.

Define constants downwards through the network:

\[
 \beta_L=s_LB,\qquad
 K_\ell=\kappa_\ell+2M\beta_\ell A_{\ell-1},\qquad
 \beta_{\ell-1}=s_{\ell-1}K_\ell\beta_\ell
 \quad(\ell=L,\ldots,2).
\tag{10}
\]

These give `||W^(ell)||op<=K_ell` and `||delta_a^(ell)||/sqrt(n)<=beta_ell`, independently of P and n. To verify the closure bound, put `b_a=r_a delta_a/rho`. At each time `m^-1 sum ||b_a||^2<=n beta_ell^2`. Projection contraction and Cauchy–Schwarz give

\[
 \|\widehat W^{(\ell)}-W_0^{(\ell)}\|_F
 \le\frac2{nm}
 \Big(\sum_a\|\Pi_Pb_a\|_{L^2}^2\Big)^{1/2}
 \Big(\sum_a\|\Pi_Ph_a\|_{L^2}^2\Big)^{1/2}
 \le2M\beta_\ell A_{\ell-1}.
\tag{11}
\]

For dense flow, direct integration gives the smaller bound `2S beta_ell A_(ell-1)`. The downward order in (10) makes these estimates noncircular. Finally `||W1(t)||F/sqrt(n)<=||W1(0)||F/sqrt(n)+2SX beta_1`. Together with the moment integral formulas and `1<=tau<=M`, these bounds give finite-width continuation for every P. They do not require entrywise control of a Gaussian initialized matrix.

Let

\[
 Z_\ell=\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|\partial_\xi h_a^{(\ell)}\|_2^2\,d\xi.
\]

The prefix derivative is zero. Set

\[
 \begin{split}
 z_1&=S(2s_1\beta_1X^2)^2,\\
 z_\ell&=3s_\ell^2\left[
 S(2\beta_\ell A_{\ell-1}^2)^2+
 (K_\ell^2+2\beta_\ell^2M^2A_{\ell-1}^2)z_{\ell-1}\right].
 \end{split}
\tag{12}
\]

Then `Z_ell<=z_ell`. Here are the steps carrying the normalization. The exact projection energy is `D_h'=rho ||h-h*||^2`, and the Legendre bound gives

\[
 \frac1m\sum_aD_{h,\ell-1,a}
 \le\frac{nM^2Z_{\ell-1}}{4P(P+1)}.
\]

The projected backward endpoints have average squared norm at most `P^2 n beta_ell^2`. For the exact internal defect

\[
 E_\ell=\frac{2\rho}{nm}\sum_a(b_a-b_a^*)(h_a-h_a^*)^T,
\]

these facts imply

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2ds
 \le2\beta_\ell^2M^2Z_{\ell-1}.
\tag{13}
\]

Specifically, Cauchy–Schwarz over samples first gives the factor `4(P+1)^2 beta_ell^2/n`; integrating the forward endpoint error and using the preceding tail bound leaves `(P+1)/P<=2`. This cancels both width and order amplification.

The forward chain rule, divided by `sqrt(n)`, bounds its three terms by `2 beta_ell A_(ell-1)^2`, `A_(ell-1)||E_ell/rho||F`, and `K_ell ||partial_xi h_(ell-1)||/sqrt(n)`. Squaring their sum with factor three and integrating proves (12).

The backward prefix is zero, so `m^-1 sum D_b<=nS beta_ell^2`. The exact energy identity and Cauchy–Schwarz in time now give

\[
 \begin{split}
 \int_0^T\sum_{\ell=2}^L\|E_\ell\|_Fdt
 &\le\frac2{nm}\sum_{\ell,a}\sqrt{D_{b,\ell,a}D_{h,\ell-1,a}}\\
 &\le\frac{B_{\rm mem}(T)}{\sqrt{P(P+1)}},\qquad
 B_{\rm mem}(T)=M\sum_{\ell=2}^L\beta_\ell\sqrt{S z_{\ell-1}}.
 \end{split}
\tag{14}
\]

Every constant in (14) is independent of width and order under (7). This controls the accumulated **absolute velocity defect**, not just cancellation in the final matrix difference. In particular it bounds the discrepancy from the proof-only exact accumulator of the closure's own responses. It is not yet a comparison with the dense trajectory.

## 3. A concrete conditional trajectory theorem

Use the population-scale parameter distance

\[
 e_n=\frac{\|\widehat W^{(1)}-W^{(1)}\|_F}{\sqrt n}
     +\frac{\|\widehat w-w\|_2}{\sqrt n}
     +\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W^{(\ell)}\|_F.
\tag{15}
\]

Keeping the ordinary Frobenius norm of learned internal increments is important: their rank-one increments are `uv^T/n` and already have order-one Frobenius norm when u and v have order-one RMS. Dividing every block by sqrt(n) would weaken the matrix part unnecessarily.

In addition to (7), suppose `phi'_ell` is globally Lipschitz with constant `t_ell`, and the **dense reference alone** satisfies, on the chosen horizon,

\[
 \|w(t)\|_\infty\le U_L,\qquad
 \|(W^{(\ell+1)}(t))^T\delta_a^{(\ell+1)}(t)\|_\infty\le U_\ell
 \quad(1\le\ell<L),
\tag{16}
\]

uniformly in width, time, and training sample. Then a width-independent constant `C_T` exists such that, for every P,

\[
 \sup_{t\le T}e_n(t)\le\frac{C_T}{\sqrt{P(P+1)}}.
\tag{17}
\]

This is a conditional strengthening in a different, explicitly specified norm; it is not the unrestricted theorem asked for.

### Proof of the stability step

Set `C_z1=X`, `C_h1=s_1 X` and, upwards,

\[
 C_{z\ell}=A_{\ell-1}+K_\ell C_{h,\ell-1},\qquad
 C_{h\ell}=s_\ell C_{z\ell},\qquad C_f=A_L+B C_{hL}.
\]

Subtracting forward recurrences gives preactivation and activation RMS differences at most `C_zell e_n` and `C_hell e_n`; prediction differences are at most `C_f e_n`.

For backwards differences use the exact identity

\[
 \widehat\delta_\ell-\delta_\ell
 =\phi'_\ell(\widehat z_\ell)(\widehat q_\ell-q_\ell)
   +[\phi'_\ell(\widehat z_\ell)-\phi'_\ell(z_\ell)]q_\ell,
\]

where `q_L=w` and `q_ell=W_(ell+1)^T delta_(ell+1)` is the dense reverse field. Thus only the reference multiplier needs the bound (16). Constants controlling delta RMS differences are

\[
 C_{\delta L}=s_L+t_LU_L C_{zL},\qquad
 C_{\delta\ell}=s_\ell(K_{\ell+1}C_{\delta,\ell+1}+\beta_{\ell+1})
                   +t_\ell U_\ell C_{z\ell}.
\]

Subtract the canonical block velocities. Their differences in the block norms of (15) are at most the following constants times e_n:

\[
 \begin{split}
 C_1&=2X(q C_{\delta1}+\beta_1 C_f),\\
 C_w&=2(q C_{hL}+A_L C_f),\\
 C_\ell&=2[\beta_\ell A_{\ell-1}C_f+
 q A_{\ell-1}C_{\delta\ell}+q\beta_\ell C_{h,\ell-1}].
 \end{split}
\]

These follow by splitting one factor at a time in `r delta h^T`, and applying sample Cauchy–Schwarz. With `K=C_1+C_w+sum C_ell`, the perturbed integral equations and (14) yield

\[
 e_n(t)\le\frac{B_{\rm mem}}{\sqrt{P(P+1)}}+K\int_0^te_n(s)ds.
\]

For `v(t)=B_mem/sqrt(P(P+1))+K int_0^t e_n`, one has `v'<=Kv`; hence `e_n<=v<=B_mem exp(Kt)/sqrt(P(P+1))`. This proves (17) without a width-dependent exit argument.

Repeating the forward constants with any fixed input bound `||x||/sqrt(d)<=X_test` gives the same rate for `sup_t sup_x |f_hat-f|` on that input set. It consequently gives an L2 prediction discrepancy for any probability measure supported there, and bounds the difference of the two test RMSEs against any square-integrable target by the reverse triangle inequality.

The readout part of (16) follows from a uniform initial entry bound and `|dot w_i|<=2 A_L rho`. The lower reverse-field bounds do **not** follow from (7). In particular, no Gaussian-typical width-uniform version of them is proved here.

## 4. Why normalization alone does not close feedback

Even for tanh, the canonical vector field has no uniform Lipschitz constant on a set specified only by bounded hidden operator norms and outer RMS norms. In fact, there is a simple lack of uniform continuity in distance (15).

Take `m=d=1`, `y=1`, two layers,

\[
 W^{(1)}=c e_1,\quad W^{(2)}=\mathbf1_ne_1^T/\sqrt n,
 \quad w=\mathbf1_n.
\]

All initial operator and outer RMS norms are bounded independently of n, and even `||w||infty=1`. Write `h=tanh c`, `g_n=tanh(h/sqrt(n))`. The normalized first-layer velocity is

\[
 \frac{F_1(c)}{\sqrt n}
 =-2(g_n-1)(1-g_n^2)\operatorname{sech}^2(c)\,e_1
 \longrightarrow2\operatorname{sech}^2(c)e_1.
\tag{18}
\]

Changing c to a different fixed nearby value c+eta changes the initial distance by only `|eta|/sqrt(n)`, but the normalized velocity difference tends to a nonzero constant whenever their squared sech values differ. The reverse field is concentrated at one coordinate, with magnitude of order sqrt(n). Thus replacing Euclidean balls by operator/RMS bounds does not justify a uniform Gronwall coefficient. This attacks that proof route, not Gaussian-typical prediction convergence or every possible stability estimate.

The maintained book has a related activation-perturbation obstruction in `docs/08-autonomous-computation.qmd`, section “Boundary: bounded slopes do not give energy-ball activation stability.” Equation (18) is an independent same-activation, state-perturbation argument and does not import that result's hypotheses.

## 5. The joint clock and the remaining Gaussian problem

Do not replace the original joint clock by a normalized clock without announcing an algorithm change. For the original clock, let

\[
 M_T=1+\int_0^T\rho dt,\qquad
 V_T=\frac1{\sqrt{nm}}\int_0^T\|\dot\Psi\|_2dt.
\]

Appendix E's dimension-free uniform polynomial approximation argument gives

\[
 \int_0^T\sum_\ell\|E_\ell\|_Fdt
 \le\frac{C_J^2M_T}{P^2}
       \left(\frac{M_T}{\sqrt{nm}}+V_T\right)^2.
\tag{19}
\]

So the visible sqrt(n) growth of clock length alone is not an obstruction: it cancels when response variation and insertion mass are used correctly. However, (19) requires a bound on the closure's own normalized total response variation to become uniform in n and P. Position/RMS bounds do not supply that bound for differentiated backward responses. One must also prove a uniform feedback estimate and continuation threshold. Replacing those obligations by an unnamed constant would not solve them.

For the Gaussian network family, useful possibilities include a reference-tail stability argument rather than an entrywise cap, or direct control of the trained propagator on the actual memory defects. Such estimates must account for reuse of the same matrices and may alter the order exponent. The short-time population tail argument in the maintained book is scoped to a particular two-layer setting; it cannot be imported as a general finite-width, all-depth, arbitrary-horizon theorem.

## Status and manuscript consequence

The replication obstruction, width-independent learning-speed defect estimate, conditional reference-field theorem, and normalized-vector-field obstruction are complete derivations in this note. They have been locally checked; they have not undergone independent review or promotion.

The requested unconditional removal of width dependence from the current full-parameter theorems is not justified. Retain those theorems. A population-scale predictor theorem is the appropriate stronger target, but its Gaussian feedback/variation step remains unresolved in this investigation. The width-independent defect proposition is a concrete partial advance that could be added separately, without labeling the population constants proved.
