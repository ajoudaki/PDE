# Single-input feature dynamics and uniform physical-time error transfer

Status: internally derived research result, not promoted. This route uses only
the study README, `docs/NOTATION.md`, and the indicated portions of
`docs/global_nonlinear.md`. No experiment, other study, or other route is an
input. The solve-math-rigorously and investigate-conjectures skills govern the
proof and its claim boundaries.

The single-atom model has a globally defined feature-time flow, reaches its
fitting level in a bounded feature interval, and admits a linear stability
estimate for the maintained H3 closure in a transformed first coordinate.
This upgrades a quantitative approximation-source estimate on one fixed feature
interval to a whole-circle error estimate at identical physical times, uniformly
for every physical time. The remaining order-to-error obligation is an explicit
bound for the three approximation sources in the maintained order N.

## 1. Scope and exact equations

Use normalized input coordinates `u=x/sqrt(2)` in `S^1`, with the sole training
atom `(u,y)=(e_1,1)`. Thus the raw input in the notation contract is
`x=sqrt(2)e_1`. The first row is initially `g=(g_1,g_2)~N(0,I_2)`, the retained
initialized Gaussian action is `A_0:H_1->H_2`, `||A_0||<=2`, and its reverse
action is its actual Hilbert adjoint. Write `A=A_0+K`, with `K` Hilbert–Schmidt,
and `c(0)=0`. These are the prescribed population limits of the finite Gaussian
initialization, including stored readout variance `1/n^2`; no finite readout
initialization has been changed.

Let `phi=tanh`. For a current state define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad f(u)=\langle c,H^2(u)\rangle.
\]

At the training input abbreviate `H=H^1(e_1)`, `h=H^2(e_1)`,
`delta=c phi'(Z^2(e_1))`, and `p=A^*delta`. The exact physical equations for
unhalved loss and mobilities `(n,1,n)` are

\[
 w_t=2(1-f(e_1))\phi'(w_1)p e_1,\quad
 K_t=2(1-f(e_1))\delta\otimes H,\quad
 c_t=2(1-f(e_1))h.                                      \tag{1}
\]

In particular `w_2=g_2` throughout. Its retained Gaussian coordinate is needed
for the passive circle.

Define the scalar flow `j` by `j_X(X,g)=phi'(j(X,g))`, `j(0,g)=g`. Boundedness
and Lipschitz continuity of `phi'` give a global scalar flow, and integration
in its first argument gives

\[
 |j(X,g)-j(Y,g)|\le |X-Y|,\qquad
 |\phi(j(X,g))-\phi(j(Y,g))|\le |X-Y|.                 \tag{2}
\]

Equivalently, with `F'(z)=cosh^2(z)`,
`j(X,g)=F^{-1}(F(g)+X)`. Only the displacement `X` is used; an integrability
assumption on `F(g)` is unnecessary. The feature equation is

\[
 X_s=A^*\delta,\quad K_s=\delta\otimes H,\quad c_s=h,
 \qquad w=(j(X,g_1),g_2),\quad (X,K,c)(0)=(0,0,0).       \tag{3}
\]

It is the original flow under the clock `s_t=2(1-f(e_1))`, once that clock is
proved positive. It is not a different training rule.

## 2. Global feature existence and the single-atom domain

The exact single-atom physical model is within the orthogonal-input theorem
in `global_nonlinear.md` B.1: one normalized input satisfies its Gram
condition, both tanh activations satisfy the bounded Lipschitz derivative
hypotheses, and its sum loss is exactly the one-atom mean loss. Thus this
global existence claim does not depend on placing the atom in the small
neighborhood of the two-atom reference in C.4.7.9. The latter neighborhood
does not itself establish anything for the single atom.

For clarity the needed feature-time extension follows directly. On `[0,S]`,
(3) gives

\[
 \|c(s)\|_\infty\le s,\qquad
 \|K(s)\|_{HS}\le s^2/2,\qquad
 \|A(s)\|\le 2+s^2/2,
\]
\[
 \|X(s)\|_2\le\int_0^s(2+v^2/2)v\,dv=s^2+s^4/8.       \tag{4}
\]

The transformed vector field is Lipschitz in `L2(X)+HS(K)+L2(c)` on these
bounded sets with a fixed readout-supremum bound. In fact (2) controls `H`,
the forward action is bounded, and

\[
 \|c\phi'(Z)-\bar c\phi'(\bar Z)\|_2
 \le\|c-\bar c\|_2+2\|\bar c\|_\infty\|Z-\bar Z\|_2. \tag{5}
\]

Adjunction and the two-factor rank-one estimate control the remaining
equations. A short-interval contraction of the integral equations on the
closed readout-supremum class yields existence and uniqueness; (4) excludes
finite feature-time escape. Its integral equations have strong endpoints,
and the same contraction extends them. Rank-one continuity gives a `C1` HS
curve `K`. Bounded multiplier continuity and (2) give a `C1` raw row curve.

Conversely, for any raw solution, Fubini makes `A^*delta` integrable at almost
every first coordinate. Scalar uniqueness for
`w_{1,s}=phi'(w_1)(A^*delta)` then recovers the representation in (3). This
also verifies raw-state uniqueness. This is B.1's proof specialized to feature
time; it does not require a Gaussian law for a trained action answer.

The common Gaussian carrier can include the full root pair and all passive
input probes from the beginning, as in B.1 and C.4.2. Both trained and closure
predictions below use these same coordinates. The initialized observable
spaces of C.4.7.8 part 5 reduce `A_0` and `A_0^*`. Their invariance for this
single-atom solution can be proved without importing C.4.7's law domain:
the transformed Picard iterates stay in the generated sigma-fields, since
`j` is a Borel coordinate map with `|j(X,g)|<=|g|+|X|`, and all rank increments
connect these closed observable spaces. Strong limits preserve this property.
Thus the density and strong-filter conclusions used below apply to this flow.

## 3. Fitting in finite feature length

Write `b(s)=f(e_1;s)` for the training prediction in feature time.
For hidden increments `(v,B)` in `H_1 x HS(H_1,H_2)`, put

\[
 J(v,B)=\phi'(AH)\{BH+A(\phi'(w_1)v)\}.
\]

Its adjoint is

\[
 J^*c=(\phi'(w_1)A^*\delta,\ \delta\otimes H).
\]

Hence the raw feature flow obeys `c_s=h`, `(w_1,K)_s=J^*c`. The scalar
chain rule along strong `C1` curves, followed by bounded-multiplier
continuity, gives

\[
 c_{ss}=JJ^*c,\qquad
 b_s=\|h\|_2^2+\|J^*c\|^2=\|\theta_s\|_{\rm raw}^2.    \tag{6}
\]

No Frechet differentiability assertion on an unrestricted `L2` ball is used.
The raw norm in (6) is row `L2`, plus HS increment, plus readout `L2` in
quadrature. The unchanged second row component has zero velocity.

Let

\[
 q=\mathbb E\tanh^2G,\qquad
 m_* = \mathbb E\tanh^2(\sqrt qG)=\|h(0)\|_2^2>0.        \tag{7}
\]

Only the initial forward query is Gaussian here. Its variance is `q` by the
canonical initialization law. At positive times no fresh-query independence
is assumed. The maintained rational certificate in C.4.5.1 part 5 proves
`m_*>1/5`; the two-atom reference's corresponding number is `m_*/2`, so that
factor must not be copied into this one-atom calculation.

Set `g_c(s)=||c(s)||_2`. On its initial positive interval,

\[
 (g_c)_s=b/g_c,\qquad
 (g_c)_{ss}=
 \frac{\|h\|_2^2-((g_c)_s)^2+\|J^*c\|^2}{g_c}\ge0.       \tag{8}
\]

The inequality uses Cauchy–Schwarz. Since `c(s)=s h(0)+o_L2(s)`,
`(g_c)_s(0+)=sqrt(m_*)`. Thus `g_c(s)>=s sqrt(m_*)`, which precludes a
later zero and extends (8) to all positive feature times. Another
Cauchy–Schwarz inequality gives `||h||_2>=(g_c)_s>=sqrt(m_*)`. Therefore

\[
                       b_s\ge m_*\quad(s\ge0).           \tag{9}
\]

There is exactly one first `s_dagger` with `b(s_dagger)=1`, and
`0<s_dagger<=1/m_*<5`. On `[0,s_dagger)`, define

\[
 t(s)=\int_0^s\frac{dv}{2(1-b(v))}.
\]

The integrand is positive. Continuity bounds `b_s` above on the compact
feature interval; thus `1-b(s)<=C(s_dagger-s)` and `t(s)` diverges at the
endpoint. The inverse exists for every physical `t>=0`. It gives the unique
physical solution in (1). Its residual satisfies

\[
 0<1-b(s(t))\le e^{-2m_*t},\qquad
 s_dagger-s(t)\le e^{-2m_*t}/m_*.                          \tag{10}
\]

Using (6) and Cauchy–Schwarz in feature time also gives

\[
 \|\theta(s_dagger)-\theta(s(t))\|_{\rm raw}
 \le e^{-2m_*t}/\sqrt{m_*}.                               \tag{11}
\]

This proves an actual full-state endpoint, including a whole-circle
prediction endpoint. It does not merely prove loss decay at the training atom.

## 4. The unchanged maintained closure also fits

The primary order is exactly C.4.7.10.B's H3 order `N`: retain total-degree
Chebyshev products through degree `N` of the initialized cores
`(tanh g_1,tanh g_2,tanh p_1,tanh p_2)` and
`(tanh xi_1,tanh xi_2)`, and append all bounded valid grammar codes through
`N` according to the maintained literal-syntax rule. Here
`xi_i=A_0 tanh(g_i)` and `p_i=A_0^*tanh(xi_i)`; these are joint queries of
the same action and actual adjoint. The ridge is
`eta_N=1/[1024(N+1)^2]`. For the raw feature column `psi_l`, let
`G_l=E[psi_l psi_l^T]`, take `G_l+eta_N I=L_l L_l^T` by positive-diagonal
lower Cholesky, and use `b_l=L_l^{-1}psi_l`. Retain the exact prescribed
joint mark laws and contraction matrix `D_N=U_2^* A_0 U_1`, and the
C.4.7.9 nonlinear equations reused by H3. Let the feature contraction
maps be `U_l`, let `Q_l=U_l U_l^*` (positive contractions, generally not
orthogonal projections), and let

\[
 B_N=Q_2A_0Q_1,
 \quad A_N=U_2M_NU_1^*=B_N+K_N,
 \quad K_N=U_2(M_N-D_N)U_1^*.
\]

In feature time, its characteristics are exactly

\[
 (X_N)_s=A_N^*\delta_N,\quad
 (M_N)_s=d_N a_N^T,\quad (c_N)_s=h_N,
\]
\[
 a_N=U_1^*H_N,\quad d_N=U_2^*\delta_N,\quad
 (K_N)_s=Q_2(\delta_N\otimes H_N)Q_1,
 \quad w_N=(j(X_N,g_1),g_2).                              \tag{12}
\]

These are the maintained equations divided by their single residual factor.
No order, dictionary or operational closure variable has been changed.
The displacement is used only to prove stability. Fixed `N` existence follows
by the bounded-mark characteristic contraction in C.4.7.9; the same feature
bounds as (4) hold because `||a_N||<=1`, `||d_N||<=s`, and
`||M_N-D_N||_F<=s^2/2`. The bounded-mark constants may depend on `N`, but the
displayed raw/action bounds do not. This also gives all finite feature
horizons and all finite physical horizons for the one-atom closure.

For its fitting argument the hidden metric is row `L2` plus the ordinary
Frobenius norm of `M_N`; it is not the HS metric of the filtered increment.
The differential of `h_N` with respect to this hidden state has adjoint
equal to the two hidden velocities in (12). Consequently

\[
 (b_N)_s=\|h_N\|_2^2+\|(w_N)_s\|_2^2
                          +\|(M_N)_s\|_F^2,
 \qquad b_N=f_N(e_1).                                    \tag{13}
\]

The norm-convexity argument (8), now in this coefficient metric, proves

\[
 (b_N)_s\ge m_N:=\|\tanh(B_N\tanh g_1)\|_2^2.            \tag{14}
\]

When `m_N>0`, its endpoint is unique with `s_{N,dagger}<=1/m_N`, and its
physical residual stays positive and decays at least as `exp(-2m_Nt)`.
The ridge filters preserve this argument precisely because the maintained
equations are Euclidean gradient equations in `M_N`. Replacing the filters
by orthogonal projections is unnecessary and would change the scheme.

## 5. Linear comparison on a fixed feature horizon

Fix a finite `S`. Define a number from the exact feature path, only for proof:

\[
 \begin{split}
 \rho_N(S)={}&
 \sup_{0\le s\le S,\ u\in S^1}
       \|(B_N-A_0)H^1(s,u)\|_2\\
 &+\sup_{0\le s\le S}\|(B_N^*-A_0^*)\delta(s)\|_2\\
 &+\sup_{0\le s\le S}
       \|Q_2K_s(s)Q_1-K_s(s)\|_{HS}.                     \tag{15}
 \end{split}
\]

The third term is the feature-time derivative, not the physical derivative.
The second term needs only the training backward field; the first term
explicitly covers the whole passive circle.

Write `rho=rho_N(S)` and set

\[
 B=2+S^2/2,\qquad
 C_D=2B+1+2S(B^2+B+1),\qquad
 C_\rho=2S(B+1)+3,
\]
\[
 E_S={C_\rho\over C_D}(e^{C_DS}-1),\qquad
 P_S=(1+SB)E_S+S,\qquad V_S^2=1+S^2(B^2+1).             \tag{16}
\]

All are finite, explicit and independent of `N`. For

\[
 D(s)=\|X_N-X\|_2+\|K_N-K\|_{HS}+\|c_N-c\|_2,
\]

the direct factor subtractions give, uniformly over the indicated inputs,

\[
 \|H_N^1(u)-H^1(u)\|_2\le D,
\]
\[
 \|Z_N^2(u)-Z^2(u)\|_2\le BD+\rho,
\]
\[
 \|\delta_N-\delta\|_2\le(1+2SB)D+2S\rho.                \tag{17}
\]

For the second line subtract as
`A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A_0)H^1`.
For the last line use (5) with `||c||_infty<=S`.
The transformed lower equation yields

\[
 \|(X_N)_s-X_s\|_2
 \le[B(1+2SB)+S]D+(2SB+1)\rho,                           \tag{18}
\]

by writing its difference as
`A_N^*(delta_N-delta)+(K_N-K)^*delta+(B_N^*-A_0^*)delta`.
The learned increment equation gives

\[
 \|(K_N)_s-K_s\|_{HS}
 \le(1+2SB+S)D+(2S+1)\rho,                              \tag{19}
\]

by splitting the rank difference into
`(delta_N-delta) tensor H_N + delta tensor (H_N-H)` and using both filter
contractions. Finally

\[
 \|(c_N)_s-c_s\|_2\le BD+\rho.                          \tag{20}
\]

The integral equations, the triangle inequality, and `D(0)=0` now give

\[
 D(s)\le\int_0^s(C_DD(v)+C_\rho\rho)\,dv,
 \qquad \sup_{s\le S}D(s)\le E_S\rho.                   \tag{21}
\]

For completeness, multiply the scalar differential upper bound for the
right-hand integral by `exp(-C_Ds)` and integrate; this yields (21), including
zero component norms without dividing by them. Output subtraction gives

\[
 \varepsilon_N:=
 \sup_{s\le S,u\in S^1}|f_N(s,u)-f(s,u)|
 \le (1+SB)\sup_{s\le S}D(s)+S\rho
 \le P_S\rho.                                          \tag{22}
\]

There is no trained-field tail term in (18)–(22). The single-input transform
removes the multiplication that produces the general H2 comparison's
Osgood modulus. In particular (22) is linear in the three sources.

## 6. Identical physical time, all physical times, whole circle

Assume that `m_N>0` and both fitting endpoints lie in `[0,S]`. Let `s(t)` and
`s_N(t)` be their physical clocks. Put `d(t)=s_N(t)-s(t)`. They solve

\[
 d_t=-2\{b(s_N)-b(s)\}-2\{b_N(s_N)-b(s_N)\}.             \tag{23}
\]

The exact feature curve is defined on all `[0,S]`, including feature times
beyond its fitting endpoint. Thus every term is legitimate even if the two
clocks lie on opposite sides of that endpoint. Equation (9) implies
`sign(d)[b(s_N)-b(s)]>=m_*|d|`. Therefore the upper right derivative of
`|d|` satisfies

\[
 D^+|d|\le-2m_*|d|+2\varepsilon_N,\qquad d(0)=0.
\]

At `d=0` the same inequality follows from `|d_t|<=2 epsilon_N`.
Multiplication by `exp(2m_*t)` and integration gives the all-time bound

\[
 |s_N(t)-s(t)|\le{\varepsilon_N\over m_*}
                       (1-e^{-2m_*t})\le\varepsilon_N/m_* . \tag{24}
\]

For each passive `u`, the raw gradient of its prediction has block norms
at most `BS`, `S`, and `1`. The exact training feature velocity has the same
three upper bounds. The strong scalar chain rule and Cauchy–Schwarz in the
raw product Hilbert space show

\[
 |\partial_s f(s,u)|\le V_S^2,\qquad(s,u)\in[0,S]\times S^1. \tag{25}
\]

Combining (22), (24), and (25), with the approximation evaluated at its own
clock, proves

\[
 \sup_{t\ge0}\sup_{u\in S^1}
 |f_N(s_N(t),u)-f(s(t),u)|
 \le \left(1+{V_S^2\over m_*}\right)P_S\rho_N(S).
                                                           \tag{26}
\]

This compares the two autonomous systems at identical physical time. It
does not match losses or postcompose one predictor with the other's clock.
The same bound holds between their whole-circle endpoint predictions.
Equation (24) also holds for the endpoints by taking `t->infinity`.

There is an accompanying increment-state estimate in the sum norm, at
identical physical time:

\[
 \sup_{t\ge0}D_{\rm physical}(t)
 \le \left[E_S+{BS+S+1\over m_*}P_S\right]\rho_N(S),       \tag{27}
\]

where the distance compares `(X,K,c)` and then controls `(w,K,c)` by (2).
It does not assert small operator-norm error `||A_N-A||`: the retained initial
action `B_N` need not approach `A_0` in operator norm.

### A fixed rational horizon and explicit sufficient order condition

Take `S=6`. At feature time zero, (15) gives

\[
 |m_N-m_*|\le2\|(B_N-A_0)\tanh g_1\|_2\le2\rho_N(6).    \tag{28}
\]

If `rho_N(6)<=1/100`, then `m_*>1/5` and
`m_N>9/50`. Thus `s_dagger<5` and `s_{N,dagger}<50/9<6`, establishing the
endpoint premise of (26) with a strict margin. For this choice

\[
 B=20,\quad C_D=5093,\quad C_\rho=255,\quad V_S^2=14437,
\]
\[
 P_6=121\,{255\over5093}(e^{30558}-1)+6.
\]

In particular a completely explicit, very conservative version of (26) is

\[
 \sup_{t\ge0,u\in S^1}|f_N(t,u)-f(t,u)|
 \le72186\left[121\,{255\over5093}(e^{30558}-1)+6\right]\rho_N(6).
                                                               \tag{29}
\]

In (29) `t` denotes physical time for each system. The large constant is a
proof constant, not a prediction that useful numerical accuracy requires
that many digits or such a small source. No practical sharpness is claimed.

## 7. What this proves, and the exact missing order lemma

The enriched bounded initialized dictionary is dense in its observable spaces
and the ridge filters converge strongly by C.4.7.10.B, equation (H3.2).
The exact sets
`{H^1(s,u)}`, `{delta(s)}`, and `{K_s(s)}` over the compact domains in (15)
are compact in `L2`, `L2`, and HS, respectively. Joint continuity of the first
set follows from the full-row `L2` bound and the Lipschitz tanh gate; bounded
multiplier continuity handles the second; continuous rank-one factors handle
the third. Uniform strong convergence on compact sets and the contraction
bounds therefore prove

\[
                         \rho_N(6)\longrightarrow0.       \tag{30}
\]

For the HS term, first approximate by a finite sum of rank-one tensors, apply
strong convergence to each factor, and use the two contraction norms; then
take a finite net of the compact derivative curve. This spells out why the
HS conclusion does not require operator-norm convergence of `B_N`.

Consequently this route supplies qualitative convergence of the unchanged
maintained closure for the single atom, uniformly over all physical times
and all circle inputs, and a linear conditional quantitative transfer. These
are new internally derived extensions beyond the printed C.4.7.9 law/time
domain; they are not claims that the printed theorem already states them.

To obtain the requested numerical-order statement, it remains to establish,
in the H3 total-degree-plus-code-prefix order and its prescribed ridge,
an explicit vanishing function `R(N)` satisfying

\[
                         \rho_N(6)\le R(N).              \tag{31}
\]

The bound must be computable from the permitted initialization and model
constants, without a future-path oracle or choosing the order after inspecting
the target projection tail. If another proof supplies (31), (29) immediately
gives an explicit all-physical-time whole-circle rate at every order with
`R(N)<=1/100`. Merely naming (15), proving (30), or defining an inverse modulus
by searching an unknown target path does not settle (31).

No finite-dimensional exact closure, fresh trained Gaussian answer, independent
adjoint, or Taylor substitute is used. The bounded feature interval does not
by itself impose a spectral decay rate in the maintained dictionary. The
result concerns the exact-real H3 population closure order; quadrature, time
stepping, and arithmetic errors in its finite numerical realization remain
separate approximation axes. B.1's finite-width/GD identification
is on each separately fixed physical horizon; neither (26) nor (30) upgrades
that independent width limit to a uniform-in-width all-time theorem.

The same proof also gives an optional H2 corollary, using C.4.7.9's original
pilot-plus-code dictionary and `eta_N=2^{-N}`. Every comparison uses only the
feature contractions, the two-sided filtered rank evolution, uniform action
bounds, and strong approximation. No estimate depends on whether symmetric
whitening or inverse Cholesky represents those filters. H2's different order
and ridge are not the primary H3 order in (31).
