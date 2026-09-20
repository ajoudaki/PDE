# Initialized learning followed by an exact positive plateau

Status: internally derived theorem candidate, frozen before comparison on
2026-09-18. No simulation, finite population rule, or quadrature is used.
This is not promoted repository theory or an independent-review verdict.

Scientific inputs were restricted to `docs/observable_p1.md` in full,
`docs/global_nonlinear.md` C.4.7.9.3--4 and the model/existence material of
C.4.7.10.D.3, and this study's complete `protected_family.md`,
`initialization_positivity.md`, and `terminal_geometry.md`. Required
rigorous-mathematics and conjecture-investigation instructions, including
their research-contract and adversarial-audit references, were read.
No other study, route output, history, or review was read.

## Result and precise limitation

Consider the exact canonical dimension-three, order-one population closure
with the prescribed joint Gaussian-derived marks, ridge `eta=1/4096`,
`w(0)=g`, `c(0)=0`, and `M(0)=D`. Every entry of the full middle matrix
follows its original gradient equation, using its actual transpose.

For any `0<a<1/2`, put `b=1-2a` and choose

\[
 (x_1,y_1,\mu_1)=(\sqrt3e_1,+1,a),\qquad
 (x_2,y_2,\mu_2)=(-\sqrt3e_1,+1,a),\qquad
 (x_3,y_3,\mu_3)=(\sqrt3e_2,-1,b).
 \tag{1}
\]

The three inputs are distinct points of `sqrt(3) S^2`, every weight is
positive, and both labels occur. The canonical physical flow has

\[
 \mathcal L(0)=1,\qquad \mathcal L'(0)=-4b^2 k<0,\qquad
 \lim_{t\to\infty}\mathcal L(t)=2a>0,
 \tag{2}
\]

where the exact initialized number `k>0` is given below. More strongly,

\[
 0<\mathcal L(t)-2a\le b e^{-4bk t}\quad(t<\infty),
 \tag{3}
\]

and there are constants `kappa_*>0` and `C>0` such that

\[
 \mathcal L(t)=2a+b C^2 e^{-4b\kappa_*t}(1+o(1)).
 \tag{4}
\]

The complete state converges to a bounded endpoint. Its loss decreases
strictly at every finite time. Both hidden trainable blocks move for every
positive finite time; the construction does not freeze them.

Taking `a=1/4`, `b=1/2` makes the label masses exactly balanced and gives
`L_inf=1/2`, `L'(0)=-k`, and `L(t)-1/2 <= (1/2) exp(-2kt)`.

This is **architectural nonrealizability**, caused by the same label at
antipodal points. There are no coincident inputs with contradictory labels.
The three inputs span a plane, not all of `R^3`. The attained endpoint is a
global minimizer of this dataset's architectural loss. Consequently this
example proves genuine initialized learning followed by positive limiting
loss, but does not prove optimization failure on realizable data.
Section 6 proves separately that every linearly independent three-input
dataset is realizable by a finite state of this same closure. Whether its
prescribed initialized flow can nevertheless have a positive limiting loss
remains open in this report.

## 1. Exact equations and the architectural floor

Use the exact invariant odd representation from the initialization source:
`b_1 in R^6`, `b_2 in R^3`, and `M in R^(3 x 6)`. The omitted constant row
and column have identically zero velocity in the full original equations;
all nonconstant entries remain trainable. Write `theta=(w,c,M)` with the
population `L2` metric in `w,c` and the Frobenius metric in `M`. For a unit
input `u` put

\[
\begin{gathered}
 a(u)=E_1[b_1\tanh(w\cdot u)],\quad
 h(u)=\tanh(b_2^TM a(u)),\quad f(u)=E_2[ch(u)],\\
 d(u)=E_2[b_2c\operatorname{sech}^2(b_2^TMa(u))],\quad
 q(u)=b_1^TM^Td(u).
\end{gathered}
\]

The complete prediction gradient is

\[
 \nabla f(u)=
 \bigl(\operatorname{sech}^2(w\cdot u)q(u)u,
       h(u),d(u)a(u)^T\bigr).
 \tag{5}
\]

Oddness of tanh gives `f(-u)=-f(u)` for every state, not merely for the
initialized trajectory. Set `v=-e_2` and `F(theta)=f_theta(v)=-f_theta(e_2)`.
For (1), direct expansion gives the exact identity

\[
 \mathcal L(\theta)
 =2a+2a f_\theta(e_1)^2+b(1-F(\theta))^2\ge2a.
 \tag{6}
\]

This floor is due entirely to the odd architecture. A general unconstrained
function on the three distinct inputs could fit all labels.

## 2. An initialized symmetry removes the nonlearnable pair's force

Let `R=diag(-1,1,1)` and `R_1=diag(R,R)`. Reflect coordinate one of all
lower and upper Gaussian marks. The resulting measure-preserving maps
`T_1,T_2` satisfy

\[
 b_1\circ T_1=R_1b_1,\quad g\circ T_1=Rg,\quad
 b_2\circ T_2=Rb_2,\quad RD R_1=D.
\]

The induced isometry on the full state is

\[
 w^R=R(w\circ T_1),\qquad c^R=c\circ T_2,\qquad
 M^R=RMR_1.
\]

A change of variables in each exact expectation gives
`f_theta^R(u)=f_theta(Ru)`. The canonical initial state is fixed by this
isometry. Since `Rv=v`, the function `F` is invariant. Its gradient ascent
equation

\[
 \theta_s=\nabla F(\theta),\qquad\theta(0)=(g,0,D)
 \tag{7}
\]

is equivariant. Local uniqueness therefore keeps its state fixed by the
isometry, yielding `f(e_1)=f(-e_1)`. Input oddness then gives

\[
 f_{\theta(s)}(e_1)=f_{\theta(s)}(-e_1)=0.
 \tag{8}
\]

Along this trajectory the derivative of the middle term in (6) vanishes
in every state direction. Thus the original full physical gradient equation
is exactly

\[
 \theta_t=2b(1-F)\nabla F.
 \tag{9}
\]

This is a scalar change of speed along a complete trained trajectory.
Neither a feature block nor a middle-matrix entry has been removed from
its original equation. Global continuation and the physical-clock
identification are verified next.

## 3. Initialized activity and finite ascent-clock fitting

Write the source's scalar constants as `nu=E tanh^2(G)`, `beta`, `eta`,
`a_0=sqrt(nu+eta)`, `b_0=sqrt(s_0+eta-beta^2/(nu+eta))`, where `s_0`
is the source's initialized second moment `s`, and the positive
bands of `D` as `d_h,d_k`. For `v=-e_2`, the initialized lower contraction
has only the two active coordinate entries, with signs opposite to those
for `e_2`. Hence

\[
 Da(v)=\ell v,\qquad
 \ell=d_h\frac{\nu}{a_0}
       +d_k\frac{\beta\eta}{(\nu+\eta)b_0}>0,
 \qquad
 k=E_2\tanh^2(\ell b_2\cdot v)>0.
 \tag{10}
\]

Here `beta>0`: condition on `h=tanh G`; the conditional mean of
`tanh(alpha h+sqrt(tau)Z)` is odd and strictly increasing in `h`, so its
product with `h` is strictly positive off zero. The upper coordinate is
nondegenerate. This establishes both strict inequalities in (10) without
quadrature or a change to initialization.

The bounded-feature local contraction argument in the allowed existence
source applies to (7) in
`L-infinity(w-g) x L-infinity(c) x R^(3 x 6)`. To check continuation, set
`L_j=ess sup |b_j|`, `A=L_1 L_2`, and `D_0=||D||_F`. Since `|h|<=1`,
`|a|<=L_1`, and `|d|<=L_2 ||c||_infinity`, equation (5) gives

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|_F\le D_0+As^2/2,\quad
 \|w(s)-g\|_\infty\le AD_0s^2/2+A^2s^4/8.
 \tag{11}
\]

These bounds exclude escape on any finite ascent-clock interval. The
bounded velocities make the solution Cauchy at any prospective finite
terminal clock, where the same local contraction restarts it. Equation
(7) consequently exists at every finite `s`.

Let `C_0(s)=||c(s)||_2^2` and `kappa(s)=||grad F(theta(s))||^2`. The
readout identities and Cauchy--Schwarz give

\[
 F_s=\kappa\ge\|h(v)\|_2^2,\qquad c_s=h(v),\qquad
 (C_0)_s=2F,\qquad F^2\le C_0\|h(v)\|_2^2.
 \tag{12}
\]

At zero the nonreadout gradient blocks vanish, and
`c(s)=s h_0(v)+o(s)`, `F(s)=ks+o(s)`, and
`C_0(s)=ks^2+o(s^2)`. Thus `F,C_0>0` initially and remain positive:
`F_s>=0` and `(C_0)_s=2F`. For `s>0`,

\[
 \left(\frac{F^2}{C_0}\right)_s
 =\frac{2F}{C_0^2}(C_0\kappa-F^2)\ge0,
 \qquad \lim_{s\downarrow0}\frac{F^2}{C_0}=k.
\]

Consequently

\[
 \kappa(s)\ge F(s)^2/C_0(s)\ge k,
 \qquad F(s)\ge ks.
 \tag{13}
\]

There is a unique finite `s_*>0` such that `F(s_*)=1`, and
`s_*<=1/k`. Its state is bounded by (11), and
`kappa_*:=kappa(s_*)>=k>0`.

## 4. Exact physical endpoint and exponential excess loss

Let `s(t)` solve

\[
 s'(t)=2b(1-F(s(t))),\qquad s(0)=0.
 \tag{14}
\]

The right side is locally Lipschitz and positive below `s_*`, and zero
at `s_*`. Scalar uniqueness prevents reaching or crossing `s_*` at finite
time. The increasing clock tends to `s_*`: a smaller limiting value would
leave its speed bounded below by a strictly positive number. Equations
(8)--(9) show that `theta(s(t))` solves the original full physical system;
uniqueness identifies it with the canonical trajectory.

Thus `f(e_1)=f(-e_1)=0`, `f(e_2)->-1`, and the full state converges in
the norms of (11) to `theta(s_*)`. Substituting these predictions into
(6) proves the exact limit `L_inf=2a` and its attainment. In particular
the lower bound was not substituted for an unproved limiting value.

Set `E(t)=L(t)-2a=b(1-F(s(t)))^2`. Equations (13)--(14) give

\[
 E'(t)=-4b\kappa(s(t))E(t)\le-4bk E(t),\qquad E(0)=b.
 \tag{15}
\]

This proves (3). Since `E(t)>0` and `kappa>=k>0` at finite time, loss
is strictly decreasing there. At zero, `kappa(0)=k`, so (15) gives
the exact initial derivative in (2).

For completeness the terminal law is determined more precisely. On the
finite ascent-clock interval, bounded derivatives of tanh make `F` twice
continuously differentiable and `kappa` locally Lipschitz. Therefore

\[
 1-F(s)=\kappa_*(s_*-s)+O((s_*-s)^2).
 \tag{16}
\]

Writing `r(t)=1-F(s(t))`, one has `r'=-2b kappa(s(t))r` and `r(0)=1`.
Moreover

\[
 \int_0^\infty|\kappa(s(t))-\kappa_*|dt
 =\int_0^{s_*}
 \frac{|\kappa(s)-\kappa_*|}{2b(1-F(s))}\,ds<\infty.
 \tag{17}
\]

Indeed the numerator is `O(s_*-s)` near the endpoint and the denominator
is comparable to `s_*-s` by (16); away from it the integrand is continuous.
Hence

\[
 C=\exp\left[-2b\int_0^\infty(\kappa(s(t))-\kappa_*)dt\right]\in(0,\infty),
 \qquad r(t)=Ce^{-2b\kappa_*t}(1+o(1)).
\]

Equation (4) follows. Bounded ascent speed and (16) also give state
convergence at rate `O(exp(-2b kappa_* t))` in the norms of (11).

## 5. The hidden blocks actually train

The symmetries fixing the active axis imply `Ma(v)=rho v` and
`d(v)=delta v`. To verify the latter assertion without assuming a form
for the readout, note that the former makes
`c_s=tanh(rho B)`, `B=b_2 dot v`, and `c(0)=0`; thus `c` depends only
on `B`. Independence and centering of the other upper coordinates make
their components of `d` vanish. Initially `rho=ell>0`.

As long as `rho>0`, the integral
`c(s,B)=integral_0^s tanh(rho(sigma)B) d sigma` has the strict sign
of `B` for `s>0`. Consequently

\[
 \delta=E_2[Bc\operatorname{sech}^2(\rho B)]>0\quad(s>0).
\]

Let `S=E_1[b_1b_1^T sech^4(w dot v)]`, a positive semidefinite matrix.
Using the full gradients in (5) gives `a_s=S M^T d` and `M_s=d a^T`, so

\[
 \rho_s=\delta\bigl(\|a\|^2+v^TMSM^Tv\bigr)\ge0.
 \tag{18}
\]

Continuity closes the argument: `rho` cannot have a first zero after
starting positive while it is nondecreasing before that zero. Thus
`rho>=ell>0`, `delta>0` at every positive clock, and `a!=0`.
It follows that `M_s=delta v a^T!=0`.

The lower feature Gram is positive definite. For each coordinate the
unnormalized pair `(tanh G,tanh(alpha tanh G+sqrt(tau)Z))` has positive
definite covariance, since the second component has positive conditional
variance given `G`; different pairs are independent and centered, and
the ridge Cholesky normalization is invertible. Since `rho=v^TMa>0`,
`M^T v!=0`. Therefore `q=delta b_1^T M^T v` is nonzero in `L2`.
The lower gate is strictly positive almost surely, giving `w_s!=0`.
The physical clock speed is positive at finite time, so both full hidden
blocks move for every `t>0`. Their initial velocities vanish, as required
by `c(0)=0`, and become nonzero immediately afterwards.

## 6. Independent three-input datasets are architecturally realizable

The preceding obstruction does not apply to independent directions. In
fact any three linearly independent unit inputs `u_1,u_2,u_3`, with any
specified labels, admit an exactly fitting state of this same canonical
feature architecture with `w-g` bounded, `c` bounded, and `M` finite.
This is an ambient-state realizability theorem, not a reachability claim.

Choose dual vectors `v_i` such that `v_i dot u_j=delta_ij`. For parameters
`p_1,p_2,p_3 in R^6`, set

\[
 w=g+\sum_{i=1}^3 v_i(b_1^Tp_i).
\]

This has bounded increment because `b_1` is bounded, and
`w dot u_i=g dot u_i+b_1^T p_i`. Thus its lower contractions can be
varied independently:

\[
 A_i(p_i)=E_1[b_1\tanh(g\cdot u_i+b_1^Tp_i)],\qquad
 D A_i(0)=E_1[b_1b_1^T\operatorname{sech}^2(g\cdot u_i)].
 \tag{19}
\]

Each displayed derivative is positive definite: its quadratic form at
nonzero `z` is the expectation of `(b_1 dot z)^2` times a strictly
positive gate, and the lower feature Gram is positive definite. Bounded
features and bounded tanh derivatives make `A_i` continuously
differentiable. Every sufficiently small neighborhood of `p_i=0`
therefore maps onto a neighborhood of `A_i(0)`. Here is a direct
justification of this local surjectivity. Put `S_i=D A_i(0)`. On a small
closed parameter ball, continuity ensures
`||I-S_i^{-1} D A_i(p)||<=1/2`. For a target `z` with
`||S_i^{-1}(z-A_i(0))||` at most half that ball's radius, the map
`p -> p-S_i^{-1}(A_i(p)-z)` maps the ball to itself and is a contraction.
Its limit solves `A_i(p)=z`.

Choose three linearly independent targets `a_i` in these respective open
image neighborhoods. This is possible by choosing them successively
outside the span of the preceding ones, since a proper linear subspace
of `R^6` has empty interior. Choose the corresponding bounded parameters
`p_i` and a finite matrix `M` satisfying `Ma_i=e_i`; extend its definition
linearly from the independent `a_i` to all of `R^6`.

The resulting upper training features are `H_i=tanh(b_{2i})`. Their
independent centered coordinate law gives
`E_2[H_i H_j]=sigma^2 delta_ij` with `sigma^2>0`. The bounded readout

\[
 c=\frac1{\sigma^2}\sum_{i=1}^3 y_i H_i
\]

satisfies `f(u_i)=y_i` exactly. This state also respects the initialized
global odd-mark sector: the constructed `w` and `c` are odd in their
respective marks, and the inactive constant row and column can stay zero.

Accordingly a positive-loss initialized plateau on linearly independent
triples would be a genuine failure to reach an available fit. No such
example, and no theorem excluding all such examples, is proved here.

## Claim audit

- Proved for (1): strict initial and all-finite-time descent, exact positive
  limiting loss, a bounded attained endpoint, exponential excess-loss
  upper bound, and its exact exponential terminal form.
- Proved: all three inputs are distinct; the weights can be positive and
  exactly label-balanced; the prescribed initialization and complete
  physical equations are retained; both hidden blocks actually move.
- Explicit mechanism: same-label antipodes conflict with input oddness.
  The example is rank two and architecturally nonrealizable; its endpoint
  attains the global architectural minimum.
- Proved separately: every independent three-input dataset admits an
  exact finite-state fit in the same closure, even within its odd sector.
- Open here: positive initialized limiting loss on those independent,
  realizable triples. Ambient stationary or singular configurations are
  not evidence of initialized reachability.
- No claims concern numerical populations, finite network width, higher
  closure orders, or an identification with a trained-network limit.
