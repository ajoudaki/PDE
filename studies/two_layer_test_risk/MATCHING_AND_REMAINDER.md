# Loss matching, passive circle capture, and the cubic remainder

Author: task `matching_remainder`, 2026-09-10. This is supporting theory within
approach A, not an independent promotion review or a second research approach.
The fixed contract is the study README. No training or numerical experiment was
performed. The coefficient's sign is not determined in this document.

## 1. Scope and conclusions

Use exactly two tanh hidden layers, the canonical stored weights, variances
`(1,1/n,1/n^2)`, mobilities `(n,1,n)`, and the mean loss on the three specified
angles. Put `c=2/3`, `u(alpha)=(cos(alpha),sin(alpha))`, and write `a,b` for the
three training indices. Initial population readout is zero. All expectations
below pair variables in their own neuron population. The connector is always
the one initial action `W_0^(2)` or its actual adjoint.

On a width-independent positive interval inside C.1, loss matching exists and
is unique. The passive circle predictor and its risk are captured by C.1's
GF and every-vanishing-raw-GD-step limits, with no width rate. Moreover, for a
continuous deterministic function `D` identified below,

\[
 \sup_\alpha|f_t(x(\alpha))-g_t(x(\alpha))-t^3D(\alpha)|\le C t^4.
 \tag{1}
\]

Consequently, setting `v(alpha)=g'_0(x(alpha))`,

\[
 \gamma={\sum_a y_aD(\alpha_a)\over\sum_a y_av(\alpha_a)},\qquad
 \tau(t)=t+\gamma t^3+O(t^4),
 \tag{2}
\]
\[
 \Delta(t)=C_\Delta t^3+O(t^4),\qquad
 C_\Delta=2\int_0^{2\pi}\cos(3\alpha)
       [D(\alpha)-\gamma v(\alpha)]\,{d\alpha\over2\pi}.
 \tag{3}
\]

The constants are finite and depend only on the fixed data, C.1's norm ball
and interval, bounded tanh derivative constants, and fixed initial Gaussian
moments/inverse activation Grams specified below. In particular they do not
depend on width, step, or a nonexistent positive eigenvalue of the input Gram.
An evaluated constant is not supplied. Equation (3) reduces a finite-time sign
theorem to a rigorous nonzero sign for this one scalar coefficient. It does
not establish that sign or that the cubic coefficient is nonzero.

The proof uses the actual integral equations and fixed initial directions.
It neither differentiates the ambient nonlinear vector field three times on
an L2 ball nor infers a population remainder from finite-width Taylor jets.

## 2. The frozen flow and an explicit matching interval

Write `H_a=H_{0,a}^(2)` and

\[
 K_{ab}=\mathbb E_2[H_aH_b],\qquad
 k(\alpha)_b=\mathbb E_2[H_0^{(2)}(\alpha)H_b].
\]

Here and below `K` without a time argument is the initial readout kernel.
It is positive definite. Indeed, the three directions are pairwise
nonparallel (`|G_ab|<1`), though `G` has rank two. The bounded ridge-function
independence proof in C.3 gives positive definiteness of the first activation
Gram `Q_ab=E_1[H_{0,a}^(1)H_{0,b}^(1)]`. Therefore the initial second-layer
Gaussian tuple has covariance `Q` and full support. If
`sum_a z_a tanh(Y_a)=0` almost surely, continuity makes this an identity on
R^3. Varying one coordinate, using nonconstancy of tanh, forces each `z_a=0`.
Thus `K` is positive definite, without inverting `G`.

The readout-only residual is exactly

\[
 r^g(s)=-e^{-cKs}y,\quad
 g_s(\alpha)=k(\alpha)^TK^{-1}(I-e^{-cKs})y,
 \quad L_g(s)={1\over3}|e^{-cKs}y|^2.
 \tag{4}
\]

These formulas follow by solving `dot r^g=-cKr^g`, `r^g(0)=-y`, and integrating
`dot g_s(alpha)=-c k(alpha)^T r^g(s)`. If `mu=lambda_min(K)>0`, then

\[
 L'_g(s)=-{2c\over3}(r^g(s))^TKr^g(s)<0,
 \qquad L_g(s)\downarrow0\quad(s\to\infty).
 \tag{5}
\]

The strict inequality holds at every finite `s` because the matrix exponential
is invertible and `y` is nonzero. Thus `L_g` maps `[0,infinity)` continuously
and bijectively onto `(0,L_g(0)]`.

Let `T_*` and `B>=1` be C.1's constructed interval and a common bound for the
population readout L2 norm, connector operator norm, and training first-layer
L2 norms throughout it. Since tanh and its derivative are bounded by one,
the full trained kernel `K(t)` obeys

\[
 \|K(t)\|_{\rm op}\le B_K:=3(B^4+B^2+1).
\]

This follows from `||delta^(2)||_2<=B`, `||delta^(1)||_2<=B^2`, `|G_ab|<=1`,
and the three kernel block formulas. The exact loss equation gives

\[
 -2c B_K L_f(t)\le L'_f(t)\le0,
 \qquad L_f(t)\ge L_f(0)e^{-2cB_Kt}>0.
 \tag{6}
\]

For the lower bound, multiply the differential inequality by
`exp(2c B_K t)` and integrate; no limit operation is involved. Equations
(5)--(6) prove existence and uniqueness of `tau(t)>=0` throughout `[0,T_*]`,
with `tau(0)=0`. Since `L_g(s)<=L_g(0)exp(-2c mu s)`,

\[
 0\le\tau(t)\le {B_K\over\mu}t.
 \tag{7}
\]

In particular the explicit positive choice

\[
 T_{\rm match}=\min\{T_*,\mu T_*/B_K\}
 \tag{8}
\]

keeps both physical clocks in `[0,T_*]`. The frozen formula itself is global,
but no global continuation of the trained flow is used. At zero,
`L'_f(0)=L'_g(0)=-(2c/3)y^TKy<0`; continuity also gives a shorter interval
of strict trained loss decrease if needed. The inverse matching map is C1
there, because (5) has a nonzero derivative. The conclusions (1)--(3) below
hold after an additional harmless shortening to time at most one.

## 3. Passive inputs require no new training theorem

Let `theta=pi/5`, and use the training angles `0,theta` as a basis. At every
finite width and every time, including a raw-GD interpolation time,

\[
 z_n^{(1)}(\alpha)=A(\alpha)z_n^{(1)}(0)+B(\alpha)z_n^{(1)}(\theta),
 \quad A(\alpha)=\cos\alpha-\cot\theta\sin\alpha,
 \quad B(\alpha)={\sin\alpha\over\sin\theta}.
 \tag{9}
\]

This is the exact linear first-layer map applied to
`u(alpha)=A(alpha)u(0)+B(alpha)u(theta)`. Define the same expression in the
population state, then apply tanh, the current connector, tanh, and pair with
the current readout. For every fixed finite list of passive angles these are
correctly typed C.1 probes: linear combinations and Lipschitz coordinate maps,
one actual forward action, and a product of the bounded last activation with
the L2 readout. No zero-weight extension of the positive-weight training
theorem is being assumed; the training list and updates are unchanged.

On C.1's high-probability finite norm ball, the bounded derivatives of `A,B`
give, for a deterministic fixed constant `C_0`,

\[
 {\|z_n^{(1)}(t,\alpha)-z_n^{(1)}(t,\beta)\|_2\over\sqrt n}
 \le C_0|\alpha-\beta|,
\]
\[
 |f_n(t,\alpha)-f_n(t,\beta)|
 \le {\|W_n^{(3)}(t)\|_2\over\sqrt n}
       \|W_n^{(2)}(t)\|_{\rm op}\,C_0|\alpha-\beta|
 \le C_1|\alpha-\beta|.
 \tag{10}
\]

The population bound follows by the same inequalities. For an angular
epsilon-net with finitely many nodes, C.1 gives uniform-in-time convergence
at the nodes. The supremum error everywhere is at most the maximum error at
the nodes plus `2C_1 epsilon`. First take width to infinity, then epsilon to
zero. Consequently

\[
 \sup_{t\le T_*,\alpha\in[0,2\pi]}|f_{n,\eta_n}(t,\alpha)-f_t(\alpha)|
 \longrightarrow0\quad\hbox{in probability}
 \tag{11}
\]

for every deterministic `eta_n>0` tending to zero, and also for finite GF as
provided by C.1's stated diagonal corollary. There is no quantitative width
rate, growing input list, or interchange with a growing time horizon.

Because `|f_n|` and `|f|` are bounded on this event and `|cos(3 alpha)|<=1`,
the pointwise identity `|a^2-b^2|<=|a-b|(|a|+|b|)` transfers (11) to uniform
risk convergence. The identical argument applies to frozen features. This
is deterministic-design prediction on a compact set, not an iid test-sample
average or sample-complexity assertion.

## 4. Initial directions, with both Gaussian responses retained

For a passive angle `alpha`, write

\[
 Z_\alpha=Z_0^{(1)}(\alpha),\quad h_\alpha=\tanh Z_\alpha,
 \quad Y_\alpha=W_0^{(2)}h_\alpha,\quad H_\alpha=\tanh Y_\alpha,
 \quad b(z)=\tanh'(z).
\]

In the following definitions the label sums are unweighted; all mean-loss
factors are carried by `c=2/3`:

\[
 S=\sum_b y_bH_b,\quad U_b=S b(Y_b),\quad
 P_b=(W_0^{(2)})^*U_b,\quad B_b=b(Z_b)P_b,
\]
\[
 T_\alpha=\sum_bG_{\alpha b}y_b B_b,\quad
 A_\alpha=b(Z_\alpha)T_\alpha,\quad
 M_\alpha=\sum_b y_b\mathbb E_1[h_\alpha h_b]U_b,\quad
 R_\alpha=M_\alpha+W_0^{(2)}A_\alpha,
 \qquad J_\alpha={c^2\over2}b(Y_\alpha)R_\alpha.
 \tag{12}
\]

`T,A,P,B` belong to population 1, `S,U,M,R,J` to population 2. `J_alpha`
will be the ordinary coefficient of `t^2` in the last hidden activation.

Notation translation to `CUBIC_DERIVATION.md`: that document uses weighted
labels `p=y/3`. The present `S,U,P,B` are three times their weighted
counterparts, and `T,A,M,R` are nine times their counterparts. The present
hidden coefficient `J_alpha` is twice its `E_alpha`; the present predictor
coefficient `D(alpha)` is its predictor `J_alpha`. Finally the present
`gamma=beta` and `C_Delta=chi`. Thus the two uses of `J` describe different
quantities; (29) here and the predictor coefficient there are identical.

The fourth moments needed below are initial fixed-program moments, not
unproved higher-moment estimates for the trained path. Here is their complete
derivation from the two finite Gaussian conditioning identities.

C.3 proves that `Q_ab=E_1[h_a h_b]` and `V_ab=E_2[U_aU_b]` are positive
definite for these inputs and nonzero labels. Conditioning on the three
initial forward calls gives the simultaneous reverse law

\[
 P_b=\sum_jh_j[Q^{-1}\mathbb E_2[Y U_b]]_j+\Gamma_b,
 \qquad \Gamma\sim N(0,V),
 \tag{13}
\]

where `Gamma` is independent of the entire initial first-layer root vector.
Thus each `P_b` has finite fourth moment: its first term is bounded and its
second Gaussian. Since `|G_alpha b|<=1` and the gates are bounded,

\[
 \sup_\alpha(\|T_\alpha\|_4+\|A_\alpha\|_4)<\infty.
 \tag{14}
\]

To bound the next forward action, define

\[
 q_\alpha=Q^{-1}\mathbb E_1[h A_\alpha],\quad
 A_\alpha^\perp=A_\alpha-\sum_jq_{\alpha,j}h_j,\quad
 v_\alpha=V^{-1}\mathbb E_1[P A_\alpha^\perp].
\]

Conditioning the same matrix on the old forward calls and their reverse
calls gives the marginal identity

\[
 W_0^{(2)}A_\alpha
   =\sum_jq_{\alpha,j}Y_j+\sum_jv_{\alpha,j}U_j
     +\|A_\alpha^\perp\|_2\,\xi_\alpha,
 \tag{15}
\]

where `xi_alpha` is standard Gaussian independent of the previously revealed
second-layer coordinates. The conditional finite law has an output
projection off three old reverse directions; its normalized squared size
vanishes at fixed program length. This is exactly the second conditional
identity proved in Gaussian calculus Section 2 / global nonlinear Section
3.2 and used in C.3. No mutual independence among the different `xi_alpha`
is required. The coefficients in (15) are uniformly bounded in `alpha` by
Cauchy--Schwarz, (14), and the fixed finite norms of `Q^-1,V^-1`; `U` is
bounded and `Y` Gaussian. Therefore

\[
 \sup_\alpha\|R_\alpha\|_4<\infty.
 \tag{16}
\]

This marginal fourth-moment bound does not require independence from the
passive forward coordinate `Y_alpha`; no such independence is asserted.

Equations (13) and (15) explicitly preserve both response directions. A
fresh independent connector would change them. These moment assertions
need neither a positive eigenvalue of `G` nor any higher trained-path
moment. Each passive query can be revealed only after the three initial
forward calls, their reverse calls, and its own first-layer root; its input
is measurable with respect to that transcript, so the adaptive conditioning
hypothesis holds.

## 5. A quantitative L2 bootstrap at zero readout

All bounds in this section hold uniformly in the passive angle on
`0<=t<=T<=min(T_match,1)`, and `C` denotes a finite constant with the
dependencies stated in Section 1. Constants may be enlarged finitely often.
Every estimate is an integral inequality on the established strong flow.

Let `rho` bound the three training residual magnitudes on the norm ball.
The readout integral and bounded activation give the pointwise estimate

\[
 \|W^{(3)}(t)\|_\infty\le 2\rho t.
 \tag{17}
\]

In particular `||delta_b^(2)(t)||_2<=2rho t` and
`||delta_b^(1)(t)||_2<=2B rho t`. Integrating the first-layer and connector
equations gives

\[
 \sup_\alpha\|Z^{(1)}(t,\alpha)-Z_\alpha\|_2
 +\|W^{(2)}(t)-W_0^{(2)}\|_{\rm op}\le Ct^2.
 \tag{18}
\]

For the first estimate the exact passive first-layer equation has coefficients
`G_alpha b` bounded by one. Lipschitz tanh and the product expansion
`W(t)h(t)-W0h0=(W(t)-W0)h(t)+W0(h(t)-h0)` then give

\[
 \sup_\alpha\bigl(\|Z^{(2)}(t,\alpha)-Y_\alpha\|_2
    +\|H^{(2)}(t,\alpha)-H_\alpha\|_2\bigr)\le Ct^2.
 \tag{19}
\]

Also `|r_b(t)+y_b|=|f_b(t)|<=2rho t`. Compare the readout integral with
`ctS`, using this last bound and (19), to obtain

\[
 \|W^{(3)}(t)/t-cS\|_2\le Ct.
\]

Since `S` is bounded and `b` is Lipschitz, (19) implies

\[
 \|\delta_b^{(2)}(t)/t-cU_b\|_2\le Ct,
 \quad
 \|(W^{(2)}(t))^*\delta_b^{(2)}(t)/t-cP_b\|_2\le Ct.
 \tag{20}
\]

The only potentially unbounded lower-layer multiplier is the fixed `P_b`.
For any bounded Lipschitz `b`, pointwise
`|b(z)-b(z')|^4 <= (2||b||_infty)^2 Lip(b)^2 |z-z'|^2`. Hence

\[
 \|b(Z_b^{(1)}(t))-b(Z_b)\|_4
 \le(2\|b\|_\infty\operatorname{Lip}(b))^{1/2}
       \|Z_b^{(1)}(t)-Z_b\|_2^{1/2}\le Ct.
\]

Hölder with the finite `||P_b||_4` from (13), followed by (20), yields

\[
 \|\delta_b^{(1)}(t)/t-cB_b\|_2\le Ct.
 \tag{21}
\]

Substitute (20)--(21) into the actual equations, retaining
`r_b(t)=-y_b+O(t)`, and integrate. The coefficient of the time-linear
velocity is exact; the error in each velocity is `O(t^2)` in its stated
norm. Thus

\[
 Z^{(1)}(t,\alpha)-Z_\alpha
     ={c^2t^2\over2}T_\alpha+O_{L^2}(t^3),
\]
\[
 W^{(2)}(t)-W_0^{(2)}
     ={c^2t^2\over2}\sum_b y_bU_b\otimes h_b+O_{\rm op}(t^3).
 \tag{22}
\]

For clarity, the bounded-derivative Taylor step used next has a direct
estimate. If `z_t=z0+t^2 v+e_t`, `||e_t||_2<=Ct^3`, and `v` has finite
fourth moment, Lipschitz continuity first removes `e_t`; scalar Taylor on
the fixed segment `z0+t^2v` then gives

\[
 \|\tanh(z_t)-\tanh(z0)-t^2b(z0)v\|_2
 \le Ct^3+\tfrac12\|\tanh''\|_\infty t^4\|v\|_4^2.
 \tag{23}
\]

Apply this with (14) to (22), then expand the forward connector product:

\[
 H^{(1)}(t,\alpha)-h_\alpha
       ={c^2t^2\over2}A_\alpha+O_{L^2}(t^3),
\]
\[
 Z^{(2)}(t,\alpha)-Y_\alpha
       ={c^2t^2\over2}R_\alpha+O_{L^2}(t^3).
 \tag{24}
\]

Finally (16) and (23) prove the essential uniform feature expansion

\[
 \sup_\alpha\|H^{(2)}(t,\alpha)-H_\alpha-t^2J_\alpha\|_2\le Ct^3.
 \tag{25}
\]

This supplies a polynomial controlled remainder. C.3's qualitative integral
expansions alone already give an `o(t^2)` feature error, but bounded tanh
and the two fixed Gaussian conditioning steps yield the stronger (25).
There is no assumption that the nonlinear activation map is Frechet smooth
from all of L2 into L2; (23) explicitly avoids that invalid assumption.

## 6. Readout comparison retains the moving residual

Let `w_f=W^(3)` and let `w_g` be the frozen readout, on the same second-layer
space with the same zero limiting initial state. Put `d=w_f-w_g` and
`e_alpha(t)=H^(2)(t,alpha)-H_alpha`. The exact difference equation is

\[
 \dot d=-c\sum_b[(f_b-g_b)H_b+r_b^f e_b],\qquad d(0)=0,
 \tag{26}
\]
\[
 f_t(\alpha)-g_t(\alpha)
       =\mathbb E_2[d(t)H_\alpha]
          +\mathbb E_2[w_f(t)e_\alpha(t)].
 \tag{27}
\]

The first summand of (26) is exactly the change in the moving residual; it
has not been set to zero. By (17), (19), and (27),
`sup_alpha |f-g|<=||d||_2+Ct^3`. Consequently (26) gives
`||d(t)||_2<=C integral_0^t ||d(s)||_2 ds+Ct^3`. Iteration or the elementary
integral Gronwall inequality proves `||d||_2<=Ct^3`.

Inserting this bound, `r_b^f=-y_b+O(t)`, and (25) back in (26) gives

\[
 d(t)={ct^3\over3}\sum_b y_bJ_b+O_{L^2}(t^4).
 \tag{28}
\]

In particular the moving-residual term in (26) contributes at order four
to this difference, even though it contributes at order two to both
individual predictors. From `w_f=ctS+O_L2(t^2)`, (25), (27), and (28),

\[
 D(\alpha)={c\over3}\sum_b y_b\mathbb E_2[J_bH_\alpha]
             +c\mathbb E_2[SJ_\alpha].
 \tag{29}
\]

Cauchy--Schwarz in each error product proves the uniform bound (1).
This calculation includes all three trained blocks: both terms in
`R_alpha=M_alpha+W0 A_alpha` and the learned readout correction (28).

## 7. Quantitative matching and risk expansion

The frozen formula (4) has uniformly bounded derivatives of every fixed
order on a bounded time interval, uniformly in the circle angle (`|k_b|<=1`).
Write `v(alpha)=c k(alpha)^Ty`, so
`g_t(alpha)=tv(alpha)+O(t^2)` and `g'_t(alpha)=v(alpha)+O(t)` uniformly.
Using (1) in the training loss gives

\[
 L_f(t)-L_g(t)=-{2\over3}y^TD_{\rm train}\,t^3+O(t^4).
 \tag{30}
\]

The frozen loss derivative has nonzero initial value
`ell_1=-(2/3)y^Tv_train=-(2c/3)y^TKy`. Shorten the interval so that
`|L'_g(s)|>=|ell_1|/2` between the two matching clocks; (7) ensures these
times tend to zero together. The mean value identity applied to
`L_g(tau)-L_g(t)=L_f(t)-L_g(t)` first yields `|tau-t|<=Ct^3` and then,
using `L'_g(s)=ell_1+O(s)`, gives (2) with an `O(t^4)` bound.

It follows that

\[
 \sup_\alpha|g_{\tau(t)}(\alpha)-f_t(\alpha)
       -t^3[\gamma v(\alpha)-D(\alpha)]|\le Ct^4.
 \tag{31}
\]

Subtract the risks using `a^2-b^2=(a-b)(a+b)`, with
`a=g_tau-cos(3 alpha)` and `b=f_t-cos(3 alpha)`. Since both predictors
are uniformly `O(t)`, (31) gives (3) with `|Delta(t)-C_Delta t^3|<=C_R t^4`
for a finite width-independent `C_R`, enlarged to be at least one.

If a separate rigorous calculation proves `C_Delta` strictly positive or
strictly negative, this yields its sign on
`0<t<=min(T,|C_Delta|/(2 C_R))`, with magnitude at least
`|C_Delta|t^3/2`. If `C_Delta=0`, the present calculation does not identify
the next nonzero coefficient. A numerical sign alone does not settle this
obligation.

## 8. Exact finite-width and raw-GD boundary

At finite width initialize **both** comparisons from the same actual small
random stored readout, rather than replacing it by zero. The frozen finite
predictor has initial residual `f_n(0)-y` and the empirical initial readout
kernel. Its hidden-parameter tangent blocks are generally nonzero at finite
width. They vanish only in the population limit. All preceding population
comparisons are compatible with C.1's vanishing-readout perturbation clause.

The empirical frozen Gram tends to positive definite `K`, hence is positive
definite with probability tending to one. Its readout GF has strictly
decreasing loss to zero unless the initial residual is zero, an event absent
with probability tending to one here. For the frozen raw-GD comparison,
`eta_n c lambda_max(K_n)<1` eventually on the same event. In an eigenbasis
every residual component then has a positive contraction factor in `(0,1)`
per step. Affine parameter interpolation contracts its magnitude strictly
within a step as well, so the interpolated frozen loss is strictly decreasing
and tends to zero.

For any fixed closed interval `[delta,T]` with `delta>0` and with strict
population loss decrease from initialization, uniform C.1 convergence puts
the actual finite losses in the interior of the frozen loss range with
probability tending to one. Unique finite matching clocks then exist on
that interval. Their convergence to `tau` is uniform: on the relevant compact
frozen time interval, (5) gives a derivative bounded away from zero, and
uniform loss errors bound the inverse errors by that reciprocal derivative.
The passive risk convergence then transfers the matched risk comparison.

Thus, if the population coefficient sign is established, the corresponding
sign holds with probability tending to one on every fixed
`[delta,t0]`, `delta>0`, with `t0` also chosen inside the strict-decrease
interval stated above, under finite GF and every admissible deterministic
vanishing raw-GD step sequence. No assertion uniform down to time zero at
finite width, no rate, and no arbitrary joint choice `delta_n ->0` follows.
In particular the small finite random readout can create different earlier
orders before the width limit. This is the exact limitation relevant to a
small population effect of order `t^3`.

## 9. Source coverage, checks, and limitations

Read coverage: root AGENTS and the complete workflow; the initial study
README; docs README and NOTATION in full; global nonlinear Sections 2--3
(lines 181--500), A.1--A.4 (1835--1902), and complete C.1--C.3 including the
weighted correction (2449--3829); finite dynamics Sections 1--4 (1--230,
with the following transition also read); Gaussian calculus introduction and
Sections 1--3 (1--202), finite moving recurrence Section 7.1 proof through its
normalization discussion (1824--2116), and the complete operative generic
finite-jet recurrences E1--E6 (5338--5445); continuation disposition in full.
The inapplicable remaining architectures and calculus sections were not
used as premises. No implementation API was used, so code README was not
required for this supporting subtask. The parent owns the overall requested
source inventory and synthesis.

Read both required SKILL.md files in full and applicable investigate
references research-contract, evidence-ledger, adversarial-audit, and
proof-search-orchestration in full. The required finite Gaussian identities
were verified from their actual proof bodies, not historical verdicts. No
external specialized theorem or inaccessible source was imported.

Actual checks: direct reconstruction of the normalization in (22), (26)--(30);
Gram-rank audit separating singular `G` from positive `Q,K,V`; explicit
fourth-moment construction at initialization; no high-moment assumption on
the trained path; conditional-call measurability audit for passive `A_alpha`;
finite-net ordering; matching denominator and finite-random-readout audit.
The document is an author proof pending the coordinator's independent check.
The scalar sign is unresolved here. The constants are bounded explicitly by
the displayed finite inequalities but have not been numerically evaluated.

Initial observed HEAD: `02af27154186dd3e45f83989a8ddf78e92ebceff`. The shared
index was empty at the read-only check; unrelated modifications were
preserved. This agent edited only this report and did not stage or commit.

Source SHA-256 at reading:

| File | SHA-256 |
|---|---|
| AGENTS.md | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| RESEARCH_WORKFLOW.md | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| docs/README.md | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| docs/gaussian_calculus.md | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| continuation disposition | `0dfdfcca323de9f8147529cfd18fa15cc5ff2899143f0af728c625531dea4f48` |
| solve-math-rigorously/SKILL.md | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| research-contract reference | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| evidence-ledger reference | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| adversarial-audit reference | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| proof-search-orchestration reference | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
