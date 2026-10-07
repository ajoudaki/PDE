# Independent check of the population-law route

Date: 2026-10-05.  This is an internal mathematical check, not a promotion
review.  No experiment was run.

## Verdict

**PASS, with one required proof replacement supplied below.**  The law-only
initialization, the finite autonomous ODE, its metric and energy identity, the
separate-population quadrature, the retained-storage count, the qualitative
all-time/endpoint limit, and the resulting fixed-
\(\varepsilon\) comparison with a fresh dense flow are mathematically
consistent.

The sentence in `POPULATION_ROUTE.md` lines 302--304 is not by itself a valid
justification.  The cited general orthogonal population theorem gives uniform
vanishing of \(L^2\) tails of the reverse query, but not a tail rate known to
beat the exponential-in-cutoff constant produced by that Gronwall argument.
The compact-time dictionary limit must instead use the exact orthogonal-tanh
clock below.  That argument removes the unbounded gate--reverse-query product
and closes the limit without any quantitative tail estimate.  With this report
as the correction, the claims in `RESULT.md` Sections 2 and 2.4 pass.

This check does **not** upgrade the result to a root-width or polylogarithmic
theorem.  The effective discretization and growing-horizon finite-width bridges
identified in the route remain open.

## Scope and inputs

The frozen primary input was `POPULATION_ROUTE.md`, SHA-256
`23656f2320deb524d2cdd63db5e5eb6ff93d9370ee8ad7caec952f4e6713565d`.
The checked synthesis was `RESULT.md`, SHA-256
`ded1deaf6f4928a0c8ba7d45c66dfdcbe556ba93fe5aeaaca268a9407173c94c`.
I also used the maintained notation and the relevant finite-dynamics,
orthogonal population-flow, finite-closure, and numerical-closure sections of
`docs/`.  I did not read the symmetry, prediction, or adversarial routes, any
other study, or `old_docs/`.

The repository-required canonical-notation skill existed at the stated path
but was unreadable under this task's OS permissions, including after the
permitted access request.  I used `docs/notation.qmd` directly and applied the
available rigorous-mathematics skill.

## 1. Law-only initialization and the projected action

Let \(\mathcal H_1,\mathcal H_2\) be the two initialized observable
\(L^2\) spaces and let \(A_0:\mathcal H_1\to\mathcal H_2\) be the one
canonical initialized Gaussian action.  Its reverse use is \(A_0^*\), not an
independent action.  The countable bounded-word grammar in the route can be
chosen exactly as in the maintained finite-closure construction, generalized
from two Gaussian coordinates to the fixed \(d\) coordinates.  Rational
Fourier-cylinder functions are dense, so its nested raw spans are dense in the
generated observable spaces.  This enumeration depends on the initialization
law and the fixed dataset, not on a solved trajectory.

For a raw feature column \(\psi_{\ell,N}\), put

\[
 G_{\ell,N}=\mathbb E_\ell[\psi_{\ell,N}\psi_{\ell,N}^{T}],\qquad
 b_{\ell,N}=(G_{\ell,N}+\eta_N I)^{-1/2}\psi_{\ell,N},
 \qquad \eta_N\downarrow0.
\]

If \(U_{\ell,N}a=b_{\ell,N}^{T}a\) and
\(Q_{\ell,N}=U_{\ell,N}U_{\ell,N}^*\), then
\(\|U_{\ell,N}\|\le1\) and \(Q_{\ell,N}\) is a positive contraction.  For
\(v=S_Na\) in any fixed earlier raw span, diagonalizing its Gram gives

\[
 \|(I-Q_{\ell,N})v\|_{L^2}
 \le \frac{\sqrt{\eta_N}}2\,|a|.
\]

Density and \(\|I-Q_{\ell,N}\|\le1\) therefore imply
\(Q_{\ell,N}\to I\) strongly.  The initialized coefficient matrix is

\[
 M_{0,N}=U_{2,N}^*A_0U_{1,N},
\]

which is exactly equation (8) of the route.  Consequently its lifted action is

\[
 B_N=U_{2,N}M_{0,N}U_{1,N}^*
     =Q_{2,N}A_0Q_{1,N}.
\]

Both \(B_N\to A_0\) and \(B_N^*\to A_0^*\) strongly.  The transpose
\(M_{0,N}^T\) is therefore the contraction of the actual adjoint.  Computing
the entries by one joint Gaussian source/response program is essential and is
sufficient; no target-path value appears.

The two mark laws must be discretized separately:
\(\operatorname{Law}(b_1,g)\) on the lower population and
\(\operatorname{Law}(b_2)\) on the upper population.  This is correct because
the populations are not paired; their interaction is through \(M\) and the
declared expectations.  Positive atomic rules obtained after Gaussian
truncation can converge in \(\mathcal W_2\).  At fixed dictionary, the
\(b_\ell\) are bounded, and the only unbounded initial mark is the
square-integrable \(g\).  Coupling each mark law to its atomic rule therefore
gives ordinary finite-dimensional characteristic stability.  Moment-preserving
elimination is optional; \(\mathcal W_2\) convergence already makes the mark
second moments uniformly bounded after sufficiently fine refinement.

Thus there is no invalid cross-population coupling and no realized dense
initialization hidden in the preprocessing.

## 2. Finite ODE, energy, existence, and storage

For the finite model, let

\[
 \langle(\xi,\zeta,N),(\xi',\zeta',N')\rangle_{\mathrm{state}}
 =\sum_i\pi_i\xi_i^T\xi_i'
  +\sum_j\rho_j\zeta_j\zeta_j'
  +\operatorname{tr}(N^TN').
\]

Direct differentiation of equation (10) in the route gives

\[
 D_{u_i}F(v)[\xi]
 =\pi_i[1-h_i(v)^2]q_i(v)v^T\xi,
\]

\[
 D_{c_j}F(v)[\zeta]=\rho_jH_j(v)\zeta,
 \qquad
 D_MF(v)[N]=\langle e(v)a(v)^T,N\rangle_F.
\]

Hence equation (11) is exactly minus the gradient of
\(m^{-1}\sum_aR_a^2\) in this constant metric.  The factors \(\pi_i\) and
\(\rho_j\) cancel from the stored-coordinate velocities, and the claimed
identity

\[
 \frac d{dt}\frac1m\sum_aR_a^2
 =-\sum_i\pi_i|\dot u_i|^2
  -\sum_j\rho_j|\dot c_j|^2-\|\dot M\|_F^2
\]

is exact, with no missing factor of \(m\) or two.

The vector field is smooth at fixed positive rule.  On any finite interval,
the energy identity and Cauchy--Schwarz bound the displacement in the displayed
state metric.  Since that metric is equivalent to Euclidean norm for the fixed
finite rule, finite-time escape is impossible.  The ODE is globally unique and
restartable from \((u,c,M)\) and the fixed marks, weights, and data.

The storage count is also complete for the stated exact-real running model:

\[
 p_1d+p_2+r_1r_2
 +p_1(r_1+1)+p_2(r_2+1)+m(d+1).
\]

The lower Gaussian nodes may be discarded after they initialize the moving
\(u_i\), and \(M_0\) need not be retained separately after it initializes
\(M\).  The two weight arrays are included in the two `+1` terms.  Dictionary
syntax, temporary Gaussian tables, and matrix-normalization work are not
needed to run or restart the ODE.  Scalar bit cost and numerical ODE error are
explicitly outside the claim, so they are limitations rather than omitted
retained state.

## 3. Compact-time dictionary limit: the required clock proof

The tail-removal argument in the route should be replaced as follows.  Define

\[
 \Psi(z)=\int_0^z\frac{dr}{1-\tanh^2 r}
        =\frac z2+\frac{\sinh(2z)}4.
\]

This is a strictly increasing bijection of \(\mathbb R\).  Let
\(J(x,z_0)=\Psi^{-1}(\Psi(z_0)+x)\).  Then

\[
 \partial_xJ(x,z_0)=1-\tanh^2(J(x,z_0))\le1.
\]

Write \(g_a=g^Tv_a\).  For the canonical population path set

\[
 X_a(t)=\Psi(Z_a^1(t))-\Psi(g_a),
\]

and define \(X_{N,a}\) analogously for the lifted order-\(N\) closure.
Orthogonality of the training directions removes every cross term in the
first-layer equation.  If

\[
 \Delta_a^2=c\,[1-\tanh^2(Z_a^2)],
 \qquad q_a=A^*\Delta_a^2,
\]

then the two clock equations are

\[
 \dot X_a=-\frac2m r_aq_a,
 \qquad
 \dot X_{N,a}=-\frac2m R_{N,a}q_{N,a}.                 \tag{C1}
\]

The troublesome product of the first-layer gate with the unbounded reverse
query has disappeared.  Moreover

\[
 Z^1(t,v)=g^Tv+\sum_a(v_a^Tv)
   \{J(X_a(t),g_a)-g_a\},                              \tag{C2}
\]

and the same formula holds for \(Z_N^1\).  Thus
\(\partial_xJ\le1\) controls both the training fields and all passive sphere
queries on the same frozen Gaussian carrier.  No moment of \(\Psi(g_a)\) is
required.

Lift the closure middle increment to

\[
 K_N=U_{2,N}(M_N-M_{0,N})U_{1,N}^*,
 \qquad A_N=B_N+K_N.
\]

Its exact evolution is

\[
 \dot K_N=-\frac2m\sum_aR_{N,a}
   (Q_{2,N}\Delta_{N,a}^2)\otimes(Q_{1,N}H_{N,a}^1),  \tag{C3}
\]

whereas the canonical increment has the same formula without the two
filters.  On a fixed \([0,T]\), energy and bounded tanh gates give uniform
bounds on \(c_N\), \(K_N\), and \(A_N\).  In fact \(c_N\) is pointwise
bounded because its velocity is a finite residual average.  The same bounds
hold for the target.

Define the target-only defect

\[
\begin{aligned}
 \epsilon_N(T)={}&
 \sup_{t\le T,\,v\in S^{d-1}}
   \|(B_N-A_0)H^1(t,v)\|_{L^2(\Omega_2)}\\
 &+\sup_{t\le T,\,v\in S^{d-1}}
   \|(B_N^*-A_0^*)\Delta^2(t,v)\|_{L^2(\Omega_1)}\\
 &+\sup_{t\le T}
   \|Q_{2,N}\dot K(t)Q_{1,N}-\dot K(t)\|_{\mathrm{HS}}.
\end{aligned}                                           \tag{C4}
\]

The target forward and adjoint fields over the compact time--sphere domain
have compact \(L^2\) images, and \(\dot K(t)\) has compact
Hilbert--Schmidt image.  Uniform strong convergence on compact sets therefore
gives \(\epsilon_N(T)\to0\).

Use the error

\[
 E_N(t)=\sum_a\|X_{N,a}-X_a\|_{L^2(\Omega_1)}
       +\|K_N-K\|_{\mathrm{HS}}
       +\|c_N-c\|_{L^2(\Omega_2)}.
\]

Formula (C2), boundedness and Lipschitz continuity of tanh, and the forward
decomposition

\[
 A_NH_N^1-AH^1
 =A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A_0)H^1
\]

bound the forward fields, predictions, and residuals by
\(C_T(E_N+\epsilon_N)\).  Because the target readout is pointwise bounded,
\(\Delta_N^2-\Delta^2\) obeys the same bound.  The actual-adjoint
decomposition

\[
 A_N^*\Delta_N^2-A^*\Delta^2
 =A_N^*(\Delta_N^2-\Delta^2)
  +(K_N-K)^*\Delta^2+(B_N^*-A_0^*)\Delta^2
\]

then gives
\(\|q_N-q\|_{L^2}\le C_T(E_N+\epsilon_N)\).  Subtracting (C1), the
readout equation, and (C3), using the Hilbert--Schmidt rank-one difference
bound, yields

\[
 D^+E_N(t)\le C_T\{E_N(t)+\epsilon_N(T)\},
 \qquad E_N(0)=0.
\]

Gronwall proves \(\sup_{t\le T}E_N(t)\to0\).  Formula (C2) makes the
prediction convergence uniform on the whole sphere.  This proves the
dictionary part of equation (15) without a reverse-query tail rate.

At fixed dictionary the raw characteristic vector field has bounded marks and
is locally Lipschitz with constants independent of the Gaussian value inside
the bounded tanh gates.  A \(\mathcal W_2\) coupling of each exact mark law
and its atomic rule therefore gives the inner quadrature limit by Gronwall.
The two arguments together prove the stated nested compact-time limit.  The
quantities in (C4) are proof errors only; they are not used to choose, initialize,
or evolve an order.  Hence this repair introduces no target-trajectory oracle.

## 4. Fitting, endpoints, and the all-time nested limit

Let \(Q^{\mathrm{top}}(t)\) be the \(m\)-by-\(m\) Gram matrix of the
top hidden training features.  At population initialization it is
\(\gamma I_m\).  The compact-time result at \(t=0\), followed by quadrature
refinement, gives \(Q_N^{\mathrm{top}}(0)\succeq(3\gamma/4)I_m\) for all
sufficiently refined models.

While \(Q^{\mathrm{top}}(t)\succeq(\gamma/2)I_m\), the readout kernel block
and the mean-loss normalization give, with
\(\rho(t)=\|r(t)\|_2/\sqrt m\),

\[
 \rho(t)\le Y e^{-\gamma t/m},
 \qquad \int_0^\infty\rho(t)\,dt\le \frac{mY}{\gamma}. \tag{C5}
\]

The energy identity says that squared metric speed is
\(-d\rho^2/dt\).  Partitioning time into intervals of length
\(m/\gamma\), applying Cauchy--Schwarz on each interval, and summing the
geometric bound from (C5) gives total metric length at most
\(CY\sqrt{m/\gamma}\).  The hidden-block gradients contain one readout or
upper-backward factor.  The readout norm is bounded by that total length;
the contraction bounds on the initialized filters and a first-exit bound on
the current action then give total hidden-feature displacement

\[
 C Y^2(m/\gamma)^{3/2}.                                 \tag{C6}
\]

The estimate is uniform over sufficiently refined dictionaries and rules.
Applied to the joint vector of the \(m\) training features, (C6) and the
Gram perturbation inequality keep
\(Q^{\mathrm{top}}(t)\succeq(\gamma/2)I_m\) under the stated sufficiently
small condition \(Y\le c\gamma/m\).  This closes the first exit.  The same
argument applies to the canonical population flow and to the finite dense
flow on the usual high-probability initialization event.

The exponentially decaying energy plus dissipation also gives finite tail
length.  Forward subtraction then yields, uniformly on the sphere,

\[
 \sup_v|f(\infty,v)-f(t,v)|
 \le C Y(m/\gamma)e^{-\gamma t/m}.                       \tag{C7}
\]

Thus all relevant paths have endpoints.  To pass from compact to all time,
given a tolerance first choose one fixed \(T\) making the target and
approximant bounds (C7) small uniformly in order, and only then take the
quadrature and dictionary limits on \([0,T]\).  For \(t\ge T\), compare each
path to its own endpoint and compare the endpoints through their values at
\(T\).  This proves the same nested limit on \([0,\infty]\).  No infinite-time
limit is interchanged with dictionary or quadrature refinement.

## 5. Fixed-\(\varepsilon\) comparison with a fresh dense flow

For the width-\(n\) dense flow, let \(\mathcal E_n\) be the event that its
initialized top-feature Gram is at least \(3\gamma I_m/4\) and its initialized
Gaussian matrix/operator and normalized row norms obey fixed bounds.  The
law of large numbers and the Gaussian operator estimate in the maintained
finite theory give \(\mathbb P(\mathcal E_n)\to1\).  On \(\mathcal E_n\),
the finite weighted energy identity and the preceding first-exit argument are
uniform in \(n\); hence the dense residual fits exponentially and its
whole-sphere endpoint tail has the form (C7).

Fix \(\varepsilon>0\) and \(0<\delta<1\).  The correct order of choices is:

1. choose one finite \(T=T(\varepsilon,\delta)\) for the uniform population,
   closure, and dense endpoint tails;
2. choose deterministic dictionary and quadrature orders so that the closure
   and population paths are close on \([0,T]\);
3. use the maintained compact-time finite-width convergence in probability,
   and then take \(n\) sufficiently large.

On the compact interval, a finite sphere net suffices: the finite and
population input-Lipschitz constants are bounded on the same high-probability
event, while \(d\) is fixed.  After \(T\), compare each path to its own
endpoint.  Allocating the tolerance among these finitely many terms proves

\[
 \mathbb P\!\left\{
   \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
   |f_C(t,v)-f_n(t,v)|\le\varepsilon
 \right\}\ge1-\delta
\]

for every sufficiently large \(n\).  The closure is deterministic and uses no
dense sample, so the dense initialization can be fresh and independent.  This
argument is purely qualitative: it supplies neither an order selector from
\(\varepsilon\), nor a width rate, nor a growing-horizon theorem.

## 6. Audit summary

- **Target-trajectory oracle:** none.  The dictionary and all Gaussian
  contractions are initialization-law objects.  Target fields enter only the
  convergence proof through (C4).
- **Density/Galerkin step:** valid after using the explicit contraction filters,
  strong convergence on compact target sets, and the clock proof above.  The
  original tail-removal sentence alone was insufficient.
- **Quadrature coupling:** valid.  The two populations must remain separately
  coupled, exactly as in the route; \(M\) and \(M^T\) supply the shared action
  and adjoint.
- **Endpoint interchange:** none.  A fixed tail time is selected before either
  the width or closure limits.
- **Storage omission:** none for the declared exact-real autonomous ODE.
  Preprocessing bit complexity and numerical integration are correctly left
  unproved.
- **Claim boundary:** the fixed-\(\varepsilon\) consistency statement is
  checked.  Strict \(n^{-1/2}\) error, polylogarithmic orders, certified bit
  cost, and the \(O(\log n)\) dense-to-population horizon remain open.
