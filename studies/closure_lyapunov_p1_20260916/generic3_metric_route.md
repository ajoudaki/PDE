# Three generic inputs: residual geometry and a rigorous capture criterion

Status: bounded independent metric route, frozen 2026-09-16. Exactly two
candidate mechanisms were examined. No experiments, external convergence
theorems, other current routes, or other studies were used. This is an
internally checked study result, not established library material.

**Outcome.** The normalized-readout argument has two explicit sign gaps for
three residuals. A second mechanism gives a complete, quantitative
unit-label convergence theorem conditional on one inequality at a reached
state. Its condition cannot hold at canonical time zero under the estimates
proved here. Reaching that condition for every generic triple remains open;
this file does not claim the requested unconditional global theorem.

## 1. Exact contract and notation

Take any three directions `u_1,u_2,u_3 in S1`, with no coincident or
antipodal pair, equal masses `1/3`, and labels `y=(1,1,-1)`. There is no
coordinate, dictionary, or data symmetry assumption. Retain the exact
canonical order-one dictionary, joint mark laws, ridge `eta=1/4096`, and
lower Cholesky normalization. Thus `w(0)=g`, `M(0)=D`, `c(0)=0`.
All action reversals below are the actual transpose of this same `M`.

The scientific input scope is `docs/NOTATION.md`,
`docs/global_nonlinear.md` C.4.7.9.3–4 and C.4.7.10 B/C.1/D.3,
`arbitrary_pair_local.md` Sections 1–4, and
`three_four_input_extension.md` Sections 2–3. In particular the last source
proves positive initial readout Gram for the present triples; that fact is
used without changing the initialization. The two required skills were
`investigate-conjectures` and `solve-math-rigorously`.

Write `H_i=tanh(b_2^T M a_i)`, `a_i=E_1[b_1 tanh(w.u_i)]`,
`f_i=E_2[cH_i]`, and `r_i=f_i-y_i`. Give data space `R^3` the inner product

\[
 \langle v,z\rangle_\mu=\tfrac13\sum_{i=1}^3v_i z_i,
 \qquad \mathcal L=\|r\|_\mu^2,\qquad \|y\|_\mu=1.
\]

At a current hidden state define the readout operator

\[
 T:L^2(\Omega_2)\longrightarrow\mathbb R^3,
 \quad (Tv)_i=E_2[vH_i],\qquad
 T^*z=\tfrac13\sum_i z_iH_i.
\]

Let `J` denote the derivative of the prediction vector with respect to
`(w,M)`, with the lower `L2` and middle Frobenius metrics, at fixed `c`.
At every finite time this derivative is bounded: the fixed features and
readout are bounded, tanh and its first derivatives are bounded, and the
matrix is finite. Differentiating the exact equations gives

\[
 \dot c=-2T^*r,\qquad (\dot w,\dot M)=-2J^*r,
 \qquad \dot r=-2Kr,\qquad K=TT^*+JJ^* .                 \tag{1}
\]

Consequently

\[
 \dot{\mathcal L}=-4\langle r,Kr\rangle_\mu
 =-\|\dot w\|_2^2-\|\dot M\|_F^2-\|\dot c\|_2^2.       \tag{2}
\]

All factors in (1)–(2) refer to the unhalved probability loss and physical
time. These identities identify the metric; positive semidefiniteness
alone is not the result of this route.

## 2. Candidate one: normalized readout and the two missing signs

Put

\[
 F=\langle y,f\rangle_\mu,\quad e=f-Fy,\quad q=\|c\|_2,
 \qquad \mathcal L=(1-F)^2+\|e\|_\mu^2.
\]

For `q>0` consider the scalar-reference candidate `P=F/q`; increasing
`P` would make `-P` a decreasing potential. Direct differentiation, using
`r=(F-1)y+e`, gives

\[
 \dot F=2(1-F)\langle y,Ky\rangle_\mu
                      -2\langle y,Ke\rangle_\mu,
 \qquad
 \dot q=\frac{2}{q}\{F(1-F)-\|e\|_\mu^2\},            \tag{3}
\]

and therefore

\[
 \dot P=\frac{2(1-F)}q
       \left(\langle y,Ky\rangle_\mu-\frac{F^2}{q^2}\right)
 -\frac2q\left(\langle y,Ke\rangle_\mu
                      -\frac{F\|e\|_\mu^2}{q^2}\right).          \tag{4}
\]

The first parenthesis is nonnegative, because

\[
 \langle y,Ky\rangle_\mu
 =\|T^*y\|_2^2+\|J^*y\|^2
 \ge\frac{\langle c,T^*y\rangle_2^2}{\|c\|_2^2}
 =\frac{F^2}{q^2}.
\]

The other factors have not acquired signs. The energy bound gives only
`0<=F<=2`, since `L<=1` implies `(1-F)^2<=1`; it does not give `F<=1`.
The second parenthesis in (4) is an off-diagonal data-space pairing minus
a nonnegative term. Positivity of `K` gives no sign for that pairing.
Thus an extension of the scalar argument must control both overshoot of
`F` and the residual component `e`, with their exact coupling in (4).

This does not assert that either bad sign actually occurs on the canonical
trajectory. It identifies precisely the two estimates still needed before
claiming this candidate is monotone. A counterexample for an unrelated
feature map would not resolve that reachable-state question.

The candidate is well defined immediately after initialization. Initial
Gram positivity gives `T_0^*y!=0`; (1) and continuity imply

\[
 c(t)=2tT_0^*y+o(t),\quad
 F(t)=2t\|T_0^*y\|_2^2+o(t),\quad
 \lim_{t\downarrow0}P(t)=\|T_0^*y\|_2>0.
\]

Here the hidden velocity is initially zero, and ordinary differentiability
already suffices for the displayed first-order expansions. This finite
initial limit does not supply the missing signs at later times.

One additional exact estimate illustrates the distinction between a norm
bound and convergence:

\[
 \frac d{dt}\|c\|_2^2
 =4\langle y-f,f\rangle_\mu
 =1-4\|f-y/2\|_\mu^2\le1,
 \qquad \|c(t)\|_2^2\le t.                              \tag{5}
\]

The completion of squares proves (5) without any residual sign assumption.
It permits unbounded readout growth and does not imply a finite endpoint.

## 3. Candidate two: controlled feature drift and capture

This mechanism works from any reached physical time `t_0`, with the original
unit labels and the actual state. It does not replace initialization by a
fitted readout. Set

\[
 R_0=\sqrt{\mathcal L(t_0)},\quad C_0=\|c(t_0)\|_2,
 \quad m_0=\|M(t_0)\|_{\rm op},\quad
 \sigma=\sqrt{\lambda_{\min}(T_{t_0}T_{t_0}^*)}.
\]

The least eigenvalue uses the data metric above; equivalently it is the
least eigenvalue of the ordinary matrix `(E[H_iH_j])/3`. Assume `sigma>0`.
Define explicit scalar polynomials, for `a>=0`, by

\[
 \begin{aligned}
 S(a)&=C_0a+a^2/2, & B(a)&=m_0+S(a),\\
 W(a)&=\{B(a)^2-m_0^2\}/2,
 &D(a)&=S(a)+m_0W(a).
 \end{aligned}                                                   \tag{6}
\]

Let `a_sep>0` be the unique root of `D(a_sep)=sigma`, and put

\[
 I(a)=\int_0^a(\sigma-D(s))^2\,ds,
 \qquad 0\le a\le a_{\rm sep}.                         \tag{7}
\]

The root exists uniquely: `D(0)=0`, `D` is continuous, strictly increasing
on `(0,infinity)`, and tends to infinity. Likewise `I` is strictly
increasing up to `a_sep`.

**Capture theorem.** If

\[
                         R_0<I(a_{\rm sep}),             \tag{8}
\]

then the canonical continuation fits all three unit labels and converges
to a single full-state endpoint. More precisely, let `a_0<a_sep` be the
unique number with `I(a_0)=R_0` (take `a_0=0` if `R_0=0`), and set

\[
 \kappa=(\sigma-D(a_0))^2>0,
 \quad C_*=C_0+a_0,\quad B_*=B(a_0).
\]

Then for all `t>=t_0`,

\[
 \mathcal L(t)\le\mathcal L(t_0)e^{-4\kappa(t-t_0)}.       \tag{9}
\]

There are endpoint fields `w_infty,c_infty` and a finite `M_infty`, with
`w_infty-g,c_infty` bounded, such that, on the original initialized
carriers,

\[
 \begin{aligned}
 \|c(t)-c_\infty\|_\infty
   &\le (R_0/\kappa)e^{-2\kappa(t-t_0)},\\
 \|M(t)-M_\infty\|_F
   &\le C_*(R_0/\kappa)e^{-2\kappa(t-t_0)},\\
 \|w(t)-w_\infty\|_\infty
   &\le L_1B_*C_*(R_0/\kappa)e^{-2\kappa(t-t_0)},
 \end{aligned}                                                   \tag{10}
\]

where `L_1=(sum_j ||b_1,j||_infty^2)^(1/2)` is the fixed feature envelope.
These conclusions include convergence of the complete saved joint laws
in `W2`, by their same-mark coupling, and uniform convergence of predictions
on the input circle. The endpoint satisfies `f_infty(u_i)=y_i`.

### Proof of the capture theorem

Use the nonnegative proof variable

\[
 A(t)=2\int_{t_0}^t\sqrt{\mathcal L(s)}\,ds.              \tag{11}
\]

This is accumulated residual, not a replacement training clock or extra
operational closure state. All equations remain the original autonomous
physical-time equations.

Ridge normalization makes `v -> b_l^T v` a contraction into the appropriate
population `L2` space. Hence `|a_i|<=1`,
`|d_i|=|E[b_2c(1-H_i^2)]|<=||c||_2`, and
`||b_1^T M^T d_i||_2<=||M||op ||c||_2`. Applying Cauchy–Schwarz to
the probability-weighted residual sum in each velocity gives

\[
 \|\dot c\|_\infty\le2R,\quad
 \|\dot M\|_F\le2R\|c\|_2,\quad
 \|\dot w\|_2\le2R\|M\|_{\rm op}\|c\|_2,              \tag{12}
\]

where `R=sqrt(L)`. The last inequality holds in the supremum norm with
the additional factor `L_1`, because the pointwise reverse contraction
is at most `L_1 ||M||op ||c||_2`. Integration first for `c`, then `M`,
then `w` yields

\[
 \begin{aligned}
 \|c(t)\|_2&\le C_0+A,\\
 \|M(t)-M(t_0)\|_F&\le S(A),\\
 \|M(t)\|_{\rm op}&\le B(A),\\
 \|w(t)-w(t_0)\|_2&\le W(A).
 \end{aligned}                                                   \tag{13}
\]

For the final integration, `B'(a)=C_0+a`, so
`integral_0^A B(a)(C_0+a) da=(B(A)^2-m_0^2)/2=W(A)`.

For any circle input, contraction of the lower coefficient map and the
Lipschitz bound for tanh give `|a(u,t)-a(u,t_0)|<=W(A)`. Splitting the
upper coefficient difference as

\[
 M(t)a(u,t)-M(t_0)a(u,t_0)
 =[M(t)-M(t_0)]a(u,t)+M(t_0)[a(u,t)-a(u,t_0)]
\]

therefore gives, using upper contraction and tanh Lipschitzness,

\[
 \sup_{u\in S^1}\|H(u,t)-H(u,t_0)\|_2\le D(A).
                                                                  \tag{14}
\]

For any `z in R^3`, weighted Cauchy–Schwarz now gives

\[
 \|(T_t^*-T_{t_0}^*)z\|_2
 \le\tfrac13\sum_i|z_i|\|H_i(t)-H_i(t_0)\|_2
 \le D(A)\|z\|_\mu.
\]

Thus whenever `A<=a_sep`,

\[
 \|T_t^*z\|_2\ge(\sigma-D(A))\|z\|_\mu,
 \qquad \dot{\mathcal L}\le-4(\sigma-D(A))^2\mathcal L.  \tag{15}
\]

On an interval where `R>0`, (15) and `A'=2R` give

\[
 \frac d{dt}\{R(t)+I(A(t))\}\le0.                       \tag{16}
\]

This is the decreasing comparison potential furnished by the route.
If `R` reaches zero, every velocity vanishes by the exact equations and
the state remains fixed, so all conclusions extend beyond that time.

Under (8), (16) implies `I(A(t))<=R_0=I(a_0)` for as long as
`A<=a_sep`. Continuity prevents escape from `A<=a_0`: at a first arrival
at `a_0`, (16) forces `R=0`, after which `A` is constant. Consequently
the spectral lower bound in (15) is at least `kappa` at all later times.
Integrating proves (9). Integrating its square root gives

\[
 2\int_t^\infty R(s)\,ds
 \le (R_0/\kappa)e^{-2\kappa(t-t_0)}.                    \tag{17}
\]

Insert (17), `||c||_2<=C_*`, and `||M||op<=B_*` into the three
velocity estimates (12), including their supremum version, to obtain
Cauchy tails and (10). Completeness of the two supremum spaces and the
finite matrix space supplies the endpoints. Bounded initial increments at
the reached time and (10) keep `w_infty-g,c_infty` bounded.

The lower fields converge uniformly in input in `L2` by their Lipschitz
dependence on `w`. The coefficient contraction, bounded matrices, and
Lipschitz upper activation then give the same statement for upper fields.
Finally split

\[
 f(t,u)-f_\infty(u)
 =E[(c(t)-c_\infty)H(t,u)]
       +E[c_\infty(H(t,u)-H_\infty(u))]
\]

and apply Cauchy–Schwarz. This proves uniform prediction convergence.
Equation (9) identifies its three training values with the labels. The
same-mark coupling makes the squared `W2` distance between joint laws no
larger than the squared moving-coordinate `L2` distance. This completes
the stated full-state result without invoking an external convergence
theorem.

## 4. Why this does not already prove the generic unit-label claim

The capture condition is meaningful for the original labels at a reached
state, but cannot hold at canonical initialization under this bound.
Indeed there `R_0=1`, `C_0=0`, and `D(a)>=a^2/2`. Also

\[
 \sigma^2=\lambda_{\min}(T_0T_0^*)
 \le\tfrac13\operatorname{tr}(T_0T_0^*)<\tfrac13,
\]

because the trace equals `(1/3)sum_i E H_i^2<1`. Thus
`a_sep<=sqrt(2 sigma)` and

\[
 \begin{aligned}
 I(a_{\rm sep})
 &\le\int_0^{\sqrt{2\sigma}}(\sigma-a^2/2)^2\,da\\
 &=\frac{8\sqrt2}{15}\sigma^{5/2}
 <\frac{8\sqrt2}{15}\,3^{-5/4}<1=R_0.                 \tag{18}
 \end{aligned}
\]

The first inequality follows on `[0,a_sep]` from
`0<=sigma-D(a)<=sigma-a^2/2`, and then by enlarging the integration
interval. The displayed integral is obtained by integrating
`sigma^2-sigma a^2+a^4/4`. The last strict inequality already follows
from `8sqrt(2)<15` and `3^(-5/4)<1`.

This is a failure of the present sufficient estimate to certify the
initial state, not a counterexample to convergence. In particular it is
not legitimate to claim that positive initial Gram supplies (8), or that
the original unit labels can be reduced until it does.

The exact unresolved bridge is: prove that the original canonical
trajectory for every allowed triple reaches a finite time with (8), or
replace the drift estimate by a different reachable-state coercivity
argument that works from its unit-label initialization. Merely assuming
that `L(t)` becomes small cannot close that bridge: the readout Gram may
become poorly conditioned at the same time, and `C_0,m_0` enter the
threshold explicitly.

## 5. Frozen claim ledger

| Claim | Status | Decisive dependency or gap |
|---|---|---|
| Exact normalized-readout derivative (4) | Proved | Direct physical-time differentiation |
| Monotonicity of that candidate for generic triples | Open | Two signs identified after (4) |
| Readout bound `||c(t)||_2^2<=t` | Proved | Completion of squares in (5) |
| Explicit capture condition and full-state convergence (8)–(10) | Proved conditionally | One inequality at an actual reached state |
| Canonical initialization satisfies that condition | Ruled out for this estimate | Strict upper bound (18) |
| Every canonical generic triple reaches capture | Open | No all-time noncollapse or finite-time capture proof |
| Requested unconditional generic three-input fitting theorem | Not established | Previous row is a necessary unresolved bridge for this route |

The strongest surviving obstruction is a trajectory whose feature
conditioning deteriorates while residual decreases too slowly for finite
total residual. Global existence and finite energy dissipation do not
exclude that behavior. No state-only monotone potential with sufficient
coercivity was obtained in this bounded pass.
