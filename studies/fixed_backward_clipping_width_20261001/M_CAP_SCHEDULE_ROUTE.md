# Increasing smooth caps: explicit deterministic constants and the diagonal boundary

2026-10-01. Scoped mathematical route. The model is exactly
`SMOOTH_SETUP.md`. This note reads the complete `SMOOTH_RESULT.md`,
`SMOOTH_ALLINIT_ROUTE.md`, `CONCENTRATION_ROUTE.md`, and
`SMOOTH_FEEDBACK_COMPLETION.md`; its new calculations below do not assume a
uniform statistical response theorem. Required mathematical, research, and
canonical-notation skills, including the neural-network conventions, were
applied. No other study, experiment, manuscript edit, or Git operation was
used.

**Conclusion.** The initialized fitting threshold, centered concentration,
and deterministic autonomous-feedback comparison have a common positive
small-label threshold for every cap \(M\ge1\). Their constants grow at most
as a polynomial in \(M\) times \(\exp(CM)\), with fixed labels. The statistical
response/cavity part must still be shown on a common label range before
these estimates imply any increasing-cap theorem. Conditional on that
bridge, an arbitrarily slowly increasing cap gives all-time convergence to
its own moving population target. It does not give an \(M\)-independent
root-width constant, or identify the moving target with the unclipped
population.

## 1. Exact state and common fitting region

Fix \(m\) training inputs \(u_a=x_a/\sqrt d\in\mathbb R^d\), labels \(y_a\),
and \(Y^2=m^{-1}\sum_a y_a^2>0\). The width is \(n\). The state is

\[
 A\in\mathbb R^{n\times d},\quad w,v_a,k_a\in\mathbb R^n,\quad\tau\ge1.
\]

For an input \(x\), the exact forward quantities and reconstructed matrix are

\[
 h(x)=\tanh(Ax/\sqrt d),\quad
 B=W_0+\frac1{mn}\sum_a v_ak_a^\top,\quad
 z(x)=Bh(x),\quad g(x)=\tanh z(x),\quad f(x)=w^\top g(x)/n.
\]

Training subscripts denote evaluation at \(x_a\). Set \(r_a=f(x_a)-y_a\),

\[
 \rho^2=m^{-1}\sum_a r_a^2,\qquad
 \psi(s)=\operatorname{sech}^2s,\qquad c_M(s)=M\tanh(s/M).
\]

The backward signals and updates are

\[
\begin{aligned}
 d_a&=c_M(w\odot\psi(z_a)),
 &\ell_a&=c_M(\psi(Au_a)\odot B^\top d_a),\\
 \dot w&=-\frac2m\sum_a r_ag_a,
 &\dot A&=-\frac2m\sum_a r_a\ell_a u_a^\top,\\
 \dot v_a&=-2r_ad_a,
 &\dot k_a&=\frac\rho\tau(h_a-k_a),\qquad\dot\tau=\rho.
\end{aligned}                                                    \tag{1}
\]

Initialization is the independent Gaussian law in the setup, with

\[
 w=v_a=0,\quad k_a=h_a(0),\quad\tau=1.
\]

Let \(\|q\|_n=\|q\|_2/\sqrt n\), \(\|A\|_n=\|A\|_F/\sqrt n\), and

\[
 \mathcal G_n=\{\|W_0\|_{\rm op}\le K,
 \quad(g_a(0)^\top g_b(0)/(mn))_{ab}\succeq\lambda I_m\}.
\]

The cap does not enter this event. The complete fitting proof in
`SMOOTH_ALLINIT_ROUTE.md`, Section 2, uses only

\[
 |c_M(s)|\le |s|,
\]

so one positive label threshold works for every \(M>0\) and also for the
identity cap \(c_\infty(s)=s\). For fixed labels below that threshold, put

\[
 S(t)=\int_0^t\rho(s)\,ds,\qquad S_0=Y/\lambda.
\]

On \(\mathcal G_n\), with constants independent of \(n,t,M\),

\[
 \rho(t)\le Ye^{-\lambda t},\quad S(t)\le S_0,\quad
 \|w\|_\infty+\max_a\|d_a\|_\infty\le C S(t),
\]
\[
 \max_a\|v_a\|_\infty\le C S(t)^2,\quad
 \|k_a\|_\infty\le1,\quad
 \|B\|_{\rm op}\le C,\quad \max_a\|\ell_a\|_n\le C S(t).
                                                               \tag{2}
\]

In particular every such trajectory converges and fits. The operator,
Gram, and hidden-motion estimates used to obtain the damping below are
also independent of \(M\). Constants denoted \(C\) henceforth may depend on
the fixed data, \(K,\lambda,S_0\), and bounded query radius, but not on
the width \(n\ge1\), physical time \(t\ge0\), or cap \(M\ge1\).

## 2. Explicit initialization stability and centered concentration

Compare two trajectories with the same cap, labels, and training inputs,
and with both initializations in \(\mathcal G_n\). Superscripts \(1,2\)
identify their states. Define

\[
\begin{aligned}
 D={}&\|A^1-A^2\|_n+\|w^1-w^2\|_n
       +\sum_a(\|v_a^1-v_a^2\|_n+\|k_a^1-k_a^2\|_n)
       +|\tau^1-\tau^2|,\\
 E={}&D+\|W_0^1-W_0^2\|_{\rm op},\qquad
 R=\|r^1-r^2\|_m,\qquad H=1+M,
\end{aligned}
\]

where \(\|r\|_m^2=m^{-1}\sum_a r_a^2\). Reconstruction gives

\[
 \|B^1-B^2\|_{\rm op}+\max_a(\|h_a^1-h_a^2\|_n+
 \|z_a^1-z_a^2\|_n)\le C E.
\]

There is no large-cap factor in the upper signal comparison. Indeed,
cap contraction and \(|\psi'|\le2\), on \(|w^j|\le C S_0\), give

\[
 \|d_a^1-d_a^2\|_n
 \le\|w^1-w^2\|_n+C S_0\|z_a^1-z_a^2\|_n\le C E.
                                                               \tag{3}
\]

For the lower signal use the exact gate estimate

\[
 |c_M(p\psi(\alpha))-c_M(\widetilde p\psi(\widetilde\alpha))|
 \le |p-\widetilde p|+2M|\alpha-\widetilde\alpha|.
\]

Combined with (2), (3), and the operator bound, it gives

\[
 \|\ell_a^1-\ell_a^2\|_n\le C H E.                         \tag{4}
\]

Subtracting each equation in (1) now gives the upper-Dini inequality

\[
 D^+D\le C H\rho^1 E+C R.                                    \tag{5}
\]

The coefficient multiplying \(R\) is independent of \(M\). For example,
the read-in contribution from residual differences is bounded by

\[
 \frac2m\sum_a |r_a^1-r_a^2|\,\|\ell_a^2\|_n\|u_a\|
 \le C S_0 R,
\]

using the normalized signal estimate in (2), rather than its coordinate
cap \(M\). This distinction avoids an unnecessary quadratic power of \(M\)
in the eventual exponential.

For completeness, the exact residual coefficients are as follows. Put

\[
 p_b=w\odot\psi(z_b),\qquad G_{ab}=u_a\cdot u_b,
\]

so \(p_b\) is the ordinary output derivative, without clipping. Then

\[
\begin{aligned}
 K^0_{ba}&=\langle g_b,g_a\rangle_n,\\
 K^A_{ba}&=G_{ab}\langle p_b,B(\psi(Au_b)\odot\ell_a)\rangle_n,\\
 K^v_{ba}&=\langle p_b,d_a\rangle_n\langle k_a,h_b\rangle_n,\\
 Q_b&=\frac1{m\tau}\sum_a\langle p_b,v_a\rangle_n
                 \langle h_a-k_a,h_b\rangle_n,
\end{aligned}
\]

where \(\langle q,q'\rangle_n=q^\top q'/n\). Direct differentiation gives

\[
 \dot r_b=-\frac2m\sum_a r_a(K^0_{ba}+K^A_{ba}+K^v_{ba})+\rho Q_b.
                                                               \tag{6}
\]

The values satisfy \(K^A,K^v=O(S_0^2)\) and \(Q=O(S_0^3)\), independently
of the cap. Their state differences are bounded by \(C H E\). In the only
potentially problematic product, (4) and \(|\ell_a^2|\le M\) give

\[
 \|\psi(A^1u_b)\odot\ell_a^1-
       \psi(A^2u_b)\odot\ell_a^2\|_n
 \le \|\ell_a^1-\ell_a^2\|_n+2M\|(A^1-A^2)u_b\|_n
 \le C H E.
\]

Subtract (6), retain the readout Gram damping, and absorb the small
coefficient values \(O(S_0^2)\), \(O(S_0^3)\). This uses only a common
small-label restriction, independent of \(M\), and gives

\[
 D^+R\le-\kappa R+C H\rho^2 E,\qquad R(0)=0,\quad\kappa>0.
                                                               \tag{7}
\]

First integrate (7) to obtain

\[
 \int_0^t R\le\frac{CH}{\kappa}\int_0^t\rho^2 E.
\]

Substitute into (5), and use the scalar integral Gronwall inequality:

\[
 E(t)\le E(0)+CH\int_0^t(\rho^1+\rho^2)E,
 \qquad \sup_tE(t)\le e^{CHS_0}E(0).                         \tag{8}
\]

Here and below numerical factors are absorbed into \(C\). The convolution
form of (7) gives, for \(c=\min(\kappa,\lambda)>0\),

\[
 R(t)\le C H e^{CHS_0}(1+t)e^{-ct}E(0).                      \tag{9}
\]

The passive query velocity has exactly the same formula as (6), with its
output index replaced by \(x\). Its coefficient values remain bounded
independently of \(M\), and its coefficient differences are bounded by

\[
 C_R H E\quad\text{uniformly for }\|x\|\le R_0,
\]

where \(C_R\) depends on the fixed query radius \(R_0\). Equations (8)--(9)
therefore imply

\[
 |\dot f^1(t,x)-\dot f^2(t,x)|
 \le C_R H e^{CHS_0}(1+t)e^{-ct}E(0).                         \tag{10}
\]

Let \(Z\) collect all independent standard Gaussian initialization roots,
so \(W_0=G_0/\sqrt n\). Initial keys are Lipschitz functions of \(A_0\);
therefore \(E(0)\le C\|Z^1-Z^2\|_2/\sqrt n\).
Equation (10) is the velocity Lipschitz bound needed by the complete
extension/Poincare/Minkowski argument in `CONCENTRATION_ROUTE.md`,
Section 5. Its hypotheses are exactly met: extend the scalar velocity
from \(\mathcal G_n\), clip it to its cap-independent exponentially
decaying value bound, apply Gaussian Poincare to each time, then integrate
the square-root variance in time. The resulting conditional centered bound
is

\[
 \left(\mathbb E\!\left[
 \int\sup_{t\ge0}|f_{n,M}(t,x)-\mathbb E[f_{n,M}(t,x)\mid\mathcal G_n]|^2
 \,d\mu(x)\mid\mathcal G_n\right]\right)^{1/2}
 \le\frac{C H e^{CHS_0}}{\sqrt n}.                            \tag{11}
\]

Here \(\mu\) is supported on the fixed bounded query set and \(n\) is large
enough that \(\mathbb P(\mathcal G_n)\ge1/2\). The latter width threshold
is independent of \(M\). Conditional mean versus extension mean costs
only the cap-independent initialized exceptional probability. No second
moment of the actual trajectory on \(\mathcal G_n^c\) is used.

## 3. Autonomous feedback restoration has the same common label range

The deterministic implication in `SMOOTH_FEEDBACK_COMPLETION.md` compares
a forced population with the autonomous population on their common action
spaces. Suppose its statistical source hypotheses hold, and let \(\eta\)
denote the sum of the uniform scalar value defects and the time integrals
of the velocity, residual-norm, and scalar-derivative defects. Its state
and residual comparison can be made quantitative in \(M\) as

\[
 D(t)\le C H\eta+C H\int_0^t\bar\rho D+C\int_0^t R,
\]
\[
 D^+R\le-\kappa R+C H\rho_\infty D+e(t),\qquad
 \int_0^\infty e(t)dt\le C H\eta.                             \tag{12}
\]

The possible factors \(H\) on the external sources are harmless here;
inserting them is a conservative upper bound. The coefficient of \(R\)
in the first inequality is cap independent by the same normalized
signal argument as (5). The absorption in the second uses coefficient
values, not their Lipschitz constants, and hence again has a common
label threshold. Integrating the second inequality first and applying
Gronwall in the finite total activity gives

\[
 \sup_{t\ge0}D(t)+\int_0^\infty R(t)dt
 \le C H^2 e^{CHS_0}\eta.                                    \tag{13}
\]

The precise polynomial power is unimportant; it can be reduced by more
source bookkeeping. What matters is that this step neither imposes

\[
 Y\lesssim M^{-1}
\]

nor generates an iterated exponential. Uniform statistical source control
at a common fixed \(Y>0\) would transfer to the full predictor with only
polynomial-exponential growth in the cap.

## 4. What diagonalization does and does not prove

Write

\[
 \mathcal E_{n,M}=
 \left(\mathbb E\!\left[\int\sup_t
 |f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2d\mu(x)
 \mid\mathcal G_n\right]\right)^{1/2}.
\]

The fixed-cap theorem has the quantifiers

\[
 \forall M>0\quad\exists Y_*(M)>0,C(M),n_0(M):
 \quad 0<Y<Y_*(M),\ n\ge n_0(M)
 \Longrightarrow \mathcal E_{n,M}\le C(M)n^{-1/2}.             \tag{14}
\]

This statement alone does not give increasing caps with one fixed positive
label size. For example, thresholds \(Y_*(M)=e^{-M}\) are consistent with
the quantifier pattern. A common initialized fitting threshold does not
remove a separate cap dependence in a statistical contraction proof.

Here is the exact diagonal consequence once that issue is resolved.
Assume there is a strictly increasing sequence of caps \(M_j\to\infty\)
for which (14) holds
for the same fixed labels. Let \(C_j=C(M_j)\), \(n_j=n_0(M_j)\). Choose
strictly increasing integers \(N_j\) such that

\[
 N_j\ge n_j,\qquad N_j\ge j^2C_j^2.
\]

Define \(M(n)=M_j\) on \(N_j\le n<N_{j+1}\). Then

\[
 M(n)\longrightarrow\infty,\qquad
 \mathcal E_{n,M(n)}\le1/j\longrightarrow0.                 \tag{15}
\]

This proves convergence to the moving population target, including the
all-time supremum and endpoint. Markov's inequality and the common
initialized exponential tail give the corresponding unconditional
convergence in probability. It does not decondition the all-time second
moment.

One can retain a rate arbitrarily close to root width. Let \(b(n)>0\) be
any nondecreasing sequence with \(b(n)\to\infty\) and \(b(n)/\sqrt n\to0\).
Choose \(N_j\ge n_j\) large enough that \(b(N_j)\ge C_j\). The same
piecewise-constant cap then satisfies

\[
 \mathcal E_{n,M(n)}\le b(n)n^{-1/2}.                         \tag{16}
\]

For example \(b(n)=\log\log(n+e^e)\) is allowed. The schedule may be
extremely slow and depends on the constants and validity thresholds in
the fixed-cap estimates. Neither (15) nor (16) proves

\[
 \mathcal E_{n,M(n)}\le C n^{-1/2}
\]

with one \(n\)-independent \(C\). A growing upper bound also does not prove
that such a sharper rate is false.

If the missing statistical source/domain bridge gives the explicit bounds

\[
 C(M)\le A(1+M)^q e^{BM},\qquad
 n_0(M)\le A(1+M)^q e^{BM},                                 \tag{17}
\]

for fixed \(A,B,q\), then the concrete schedule

\[
 M(n)=\max\{1,\sqrt{\log(n+1)}\}
\]

satisfies its width threshold for all sufficiently large \(n\) and gives

\[
 \mathcal E_{n,M(n)}
 \le C(\log n)^{q/2}\exp(B\sqrt{\log n})n^{-1/2}
 =n^{-1/2+o(1)}.                                             \tag{18}
\]

Alternatively \(M(n)=a\log n\) works with a sufficiently small fixed

\[
 a>0\quad\text{such that }Ba<1/2,
\]

after enlarging \(B\) to dominate both bounds in (17); its error is

\[
 O((\log n)^q n^{-1/2+Ba}).
\]

If only the first bound in (17) is known, (18) requires additionally
checking \(n\ge n_0(M(n))\); that requirement cannot be suppressed. One
may instead slow the schedule further using the threshold-dependent
diagonal construction.

### Conservative schedule for a threefold exponential bound

The causal comparison route communicated by the coordinator has a larger
prospective constant than (17). The exact schedule implication can be
proved independently of that route. Suppose the completed statistical
bridge supplies a common positive label threshold and, for some fixed

\[
 T_C(M)=\exp\!\left(\exp\!\left(\exp(C(1+M))\right)\right),
\]

the bounds

\[
 \mathcal E_{n,M}\le T_C(M)n^{-1/2},\qquad n_0(M)\le T_C(M).
                                                               \tag{23}
\]

Constants and polynomial prefactors can be absorbed by increasing \(C\).
The second assumption may be replaced by any smaller width threshold,
including one independent of \(M\). Define

\[
 N_*=\exp(\exp(\exp(1))),\qquad
 M(n)=\sqrt{\log\log\log(n+N_*)}.
                                                               \tag{24}
\]

All logarithms in (24) are positive and \(M(n)\ge1\). This cap diverges.
To verify the rate, put \(u_n=\log\log\log(n+N_*)\), so

\[
 \log(n+N_*)=\exp(\exp(u_n)),\qquad u_n\longrightarrow\infty.
\]

Consequently

\[
 \frac{\log T_C(M(n))}{\log(n+N_*)}
 =\exp\!\left(\exp(C(1+\sqrt{u_n}))-\exp(u_n)\right)
 \longrightarrow0,                                           \tag{25}
\]

because \(C(1+\sqrt{u_n})-u_n\to-\infty\). Also

\[
 \log(n+N_*)/\log n\longrightarrow1.
\]

Thus \(T_C(M(n))=n^{o(1)}\), the width restriction in (23) holds
eventually, and

\[
 \mathcal E_{n,M(n)}\le n^{-1/2+o(1)}\longrightarrow0.        \tag{26}
\]

This is a rigorous implication of (23), pending the complete source and
domain bridge in `M_UNIFORM_LAW_ROUTE.md`, `M_UNIFORM_CAVITY_ROUTE.md`, and
the coordinator's `M_SCALE_RESULT.md`. It does not assert that the simpler
logarithmic or square-root-logarithmic schedules satisfy those larger
constants. In particular (26) is weaker than a bound with one fixed
root-width constant.

## 5. The separate cap-removal limit

The comparison target in (15)--(18) is \(f_{\infty,M(n)}\). An unclipped
population statement additionally requires constructing \(f_{\infty,\infty}\)
and proving

\[
 \left(\int\sup_t|f_{\infty,M}(t,x)-f_{\infty,\infty}(t,x)|^2
 \,d\mu(x)\right)^{1/2}\longrightarrow0.                     \tag{19}
\]

This is a logically separate all-time population continuity problem.
The scalar inequality

\[
 |s-c_M(s)|\le |s|^3/(3M^2)                                 \tag{20}
\]

does not prove it without controlling lower-carrier moments and
propagation of the resulting perturbation. It also does not mean that
the smooth top cap is ever exactly inactive.

There is an elementary valid fixed-width statement. On the common fitting
event compare the capped and identity-cap flows with identical
initialization. For either flow,

\[
 \|B^\top d_a\|_n\le C S_0,\qquad
 \|B^\top d_a\|_\infty\le C S_0\sqrt n.
\]

At one fixed state, (20) gives an upper-signal difference at most

\[
 C S_0^3/M^2
\]

in normalized norm. For the lower signal, first change the upper signal
inside \(B^\top\), then remove the lower cap. Since

\[
 \|p^{\odot3}\|_n\le\|p\|_\infty^2\|p\|_n,
\]

the resulting lower-signal source is at most \(C nS_0^3/M^2\).
The identity-cap map \(p\psi(\alpha)\), restricted to these two
trajectories, has first-difference coefficient at most

\[
 C(1+S_0\sqrt n).
\]

Indeed split the product difference and use the preceding coordinate
bound on one endpoint carrier. Apply the same state/residual comparison
as (5)--(8), now with the cap-removal source multiplied by the integrable
residual. The coefficient values determining damping remain independent
of \(M,n\). For fixed labels and bounded queries this yields the coarse
but explicit estimate

\[
 \sup_{t\ge0,\ \|x\|\le R_0}
 |f_{n,M}(t,x)-f_{n,\infty}(t,x)|
 \le C_R\frac{n e^{C\sqrt n}}{M^2}.                          \tag{21}
\]

Consequently cap removal holds for each fixed width, uniformly for all
time on its initialized fitting event. The width-dependent bound (21)
does not close (19), does not justify exchanging \(n\to\infty\) and

\[
 M\to\infty,
\]

and is useless for the slowly increasing caps in (18). This diagnoses a
missing bridge rather than a failure of the intended statistical claim.

## 6. A precise deterministic obstruction with limited force

A global lower-gate Lipschitz constant independent of the cap is false.
For

\[
 F_M(\alpha,p)=M\tanh(p\psi(\alpha)/M),
\]

take any fixed \(\alpha_*\ne0\) and \(p=M/\psi(\alpha_*)\). Then

\[
 \partial_\alpha F_M(\alpha_*,p)
 =-2M\tanh(\alpha_*)\operatorname{sech}^2(1).                 \tag{22}
\]

Its magnitude grows linearly in \(M\). Thus the deterministic state-space
Lipschitz proof cannot simply replace \(CH\) by a cap-independent constant.
Large lower carriers are compatible with a bounded matrix operator norm
and bounded normalized signal norm: for a unit vector \(b\) having one
coordinate of order one, the rank-one matrix

\[
 B=(\mathbf1_n/\sqrt n)b^\top
\]

has operator norm one, whereas \(B^\top(s\mathbf1_n)=s\sqrt n\,b\).
This is a finite-dimensional realization of the concentration mechanism
behind (22), not a proved reachable-trajectory counterexample. It does
not refute uniform-in-cap statistical moments, initialization-to-prediction
stability on typical Gaussian initializations, or a root-width theorem.

The central remaining issue for an increasing-cap theorem with fixed
labels is common-label statistical control, including the admissible
covariance/response domain and its cavity embedding. Once that bridge is
proved, Sections 2--4 supply the deterministic constants and valid
schedule conclusions without any further shrinking-label assumption.
