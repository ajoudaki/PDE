# Internal check of approximate terminal handoff

Check date: 2026-09-30.

Candidate: `TERMINAL_HANDOFF.md`.

Frozen candidate SHA256:

`f0ec65454de7c800c6205636d3b13eaa0227a9dcbf4a4ed379d0020b665e21ce`

Dependency: the complete revised `TERMINAL_SCALAR_THEOREM.md`, SHA256

`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`

Verdict: **PASS for the conditional finite-width handoff proposition and
the stated frozen residual-map differentiability claim.** All three error
bounds have correct constants. The precision allocation is valid when its
constants, including a positive lower bound for the contraction margin,
remain fixed. The approximate-margin paragraph is correct as written;
an additional practical distinction is recorded below.

The complete candidate and complete stated dependency were read. This is a
bounded follow-up internal check using the repository instructions and the
previously read `solve-math-rigorously` skill. No other study, scientific
source, numerical experiment, or external source was used. Neither
candidate was edited. This report is not a promotion review or approval.

## Perturbed frozen system

Write \(\Delta C=\widetilde C-C_0\),
\(\Delta b=\widetilde b-b_0\), and
\(\widetilde T(u)=-\widetilde Cu+\|u\|\widetilde b\).
The assumed sum of coefficient errors gives

\[
\|\widetilde T(u)-T(u)\|
\le(\|\Delta C\|_{\rm op}+\|\Delta b\|)\|u\|
\le\delta\|u\|.
\]

For \(e=u-v\), the perturbation of the one-sided contraction estimate is
bounded by

\[
\left|e^T\left[-\Delta C e+
(\|u\|-\|v\|)\Delta b\right]\right|
\le\delta\|e\|^2.
\]

Thus \(\widetilde T\) is contractive with rate at least
\(\lambda_-:=\lambda_0-\delta>0\). It is globally Lipschitz because a
matrix map and the norm map are globally Lipschitz. Existence and uniqueness
therefore hold for all times; alternatively, local existence together with
the exponential norm bound rules out finite-time escape. With
\(R_+=R+e_0\), the initial norm is at most \(R_+\), so

\[
\|\widetilde r(t)\|\le R_+e^{-\lambda_-t}.
\]

The vector field vanishes at zero residual. None of these statements
requires the perturbed coefficients to arise from any underlying neuron
state.

## Residual, loss, and clock error constants

The terminal theorem supplies

\[
\dot r=T(r)+E(t),\qquad
\|E(t)\|\le\frac{2JH}{\lambda_0}R^2e^{-\lambda_0t/2}.
\]

For \(e(t)=\|r(t)-\widetilde r(t)\|\), subtraction and contraction of
the **exact** frozen map \(T\) give, in the upper norm derivative sense,

\[
D^+e\le-\lambda_0 e+\|E(t)\|+
\delta\|\widetilde r(t)\|.
\]

The estimate at zero difference follows by continuity, or by taking the
limit of a regularized Euclidean norm. Since \(e(0)\le e_0\), integration
gives exactly candidate equation (4):

\[
\begin{aligned}
e(t)\le{}&e_0e^{-\lambda_0t}
+\frac{4JH}{\lambda_0^2}R^2
 (e^{-\lambda_0t/2}-e^{-\lambda_0t})\\
&+\delta R_+\int_0^t
 e^{-\lambda_0(t-u)}e^{-\lambda_-u}\,du.
\end{aligned}
\]

The maximum of the middle exponential difference is \(1/4\).
Bounding the second exponential in the integral by one bounds the last
term by \(\delta R_+/\lambda_0\). This proves (1) with the stated
coefficient \(JH/\lambda_0^2\).

Both residual norms are bounded by their initial upper bounds. Therefore

\[
\left|\frac{\|r\|^2-\|\widetilde r\|^2}{m}\right|
\le\frac{2R+e_0}{m}\|r-\widetilde r\|,
\]

which proves (2). The factor \(2R+e_0\), rather than \(2R\), correctly
accounts for inaccurate initial residual data.

Integration of the first two error terms gives respectively
\(e_0/\lambda_0\) and \(4JHR^2/\lambda_0^3\). For the last one, the
integrand is nonnegative, so changing order and writing \(t=u+v\) yields

\[
\begin{aligned}
\int_0^\infty\int_0^t
 e^{-\lambda_0(t-u)}e^{-\lambda_-u}\,du\,dt
&=\int_0^\infty e^{-\lambda_0v}\,dv
  \int_0^\infty e^{-\lambda_-u}\,du\\
&=\frac1{\lambda_0\lambda_-}.
\end{aligned}
\]

Consequently the integrated residual error has exactly the bound stated
in the proof. Since the norm is 1-Lipschitz, integrating the difference of
the clock speeds and adding the initial clock error proves (3). Every
comparison is at the same physical time, and the integrable bound also
controls the difference of the limiting clocks.

The edge cases are consistent:

- At \(\delta=0\), the coefficient-error term vanishes without any
  division by \(\delta\). The remaining initial-data term contracts at
  rate \(\lambda_0\).
- If \(R=0\), the target state is stationary. An erroneous initial
  residual can still generate a decaying approximate trajectory. The
  stated clock terms reduce to the valid bound
  \(e_0/(\sqrt m\lambda_-)\), in addition to \(e_\tau\).
- If \(R=e_0=0\), both residual trajectories are zero irrespective of
  the allowed coefficient error; only the initial clock offset remains.
- When \(\delta\) approaches \(\lambda_0\), the clock estimate can
  deteriorate as \(1/\lambda_-\). The assumption \(\delta<\lambda_0\)
  is explicit, and no uniform-in-\(\lambda_-\) bound is claimed.

## Precision allocation and approximate certificates

The asymptotic scaling is correct. To make the constants explicit, take
nonnegative fixed \(c_e,c_\delta,c_\tau\) such that

\[
e_0\le c_eR^2,\quad \delta\le c_\delta R,\quad
e_\tau\le c_\tau R^2.
\]

For small enough \(R\) that \(c_\delta R\le\lambda_0/2\),
\(\lambda_-\ge\lambda_0/2\), and the residual error is bounded by

\[
R^2\left[c_e+\frac{JH}{\lambda_0^2}
+\frac{c_\delta}{\lambda_0}(1+c_eR)\right].
\]

The loss bound is this expression multiplied by
\(R(2+c_eR)/m\), hence is \(O(R^3)\). The clock error is at most

\[
R^2\left[c_\tau+\frac1{\sqrt m}
\left(\frac{c_e}{\lambda_0}
+\frac{4JH}{\lambda_0^3}
+\frac{2c_\delta(1+c_eR)}{\lambda_0^2}\right)\right].
\]

Thus the powers of \(\epsilon\) in (5) are valid, with sufficiently
small constants and the terminal tube hypotheses still satisfied. For a
family of handoffs, widths, or target tolerances, this reasoning requires
uniform control of the displayed constants, especially a positive lower
bound on \(\lambda_0\). Smoothness at each individual finite-width state
does not supply that uniformity. This is the meaning needed for the
candidate's phrase “fixed tube constants.”

For the approximate margin, the variational characterization of the least
eigenvalue on the unit sphere gives

\[
\left|\lambda_{\min}(\operatorname{sym}\widetilde C)
-\lambda_{\min}(\operatorname{sym}C_0)\right|
\le\|\Delta C\|_{\rm op}.
\]

The reverse triangle inequality for \(b\) then proves
\(|\widetilde\lambda-\lambda_0|\le\delta\). Therefore
\(\widetilde\lambda>\delta\) indeed certifies \(\lambda_0>0\), as stated.

There is a useful distinction when implementing this certificate:
\(\widetilde\lambda>\delta\) alone need not certify the proposition's
stronger condition \(\delta<\lambda_0\). The readily checkable sufficient
condition

\[
\widetilde\lambda>2\delta
\]

does certify it, because
\(\lambda_0\ge\widetilde\lambda-\delta>\delta\).
The candidate does not falsely identify its positive-margin check with
the full proposition certificate, so this is an optional clarification,
not a correction to its claim. Bounds on the true handoff residual and the
full terminal tube also remain necessary.

The precision conditions describe propagation of certified handoff errors.
They do not construct an earlier evaluator, bound errors over its earlier
trajectory, or prove it reaches a suitable terminal state. The note keeps
those obligations separate.

## Differentiability of the frozen residual map

For the fixed state \(X_*\), put
\(C_*=C(X_*)\), \(b_*=b(X_*)\), and
\(T_*(u)=-C_*u+\|u\|b_*\). If a Fréchet derivative \(D\) at zero
existed, its directional limit along every \(u\) would satisfy

\[
Du=\lim_{\varepsilon\downarrow0}
\frac{T_*(\varepsilon u)-T_*(0)}{\varepsilon}=T_*(u).
\]

For any nonzero \(u\), however,

\[
T_*(u)+T_*(-u)=2\|u\|b_*\ne0
\]

when \(b_*\ne0\), whereas a linear map satisfies \(Du+D(-u)=0\).
This contradiction proves the claim. In the complementary case \(b_*=0\),
the map is linear and differentiable. The candidate correctly confines the
claim to this map on all of \(\mathbb R^m\); it does not infer
non-differentiability of a composed map on the potentially restricted
manifold of network residuals.

The map remains globally Lipschitz with constant at most
\(\|C_*\|_{\rm op}+\|b_*\|\). A positive margin
\(\lambda_{\min}(\operatorname{sym}C_*)-\|b_*\|\) gives contraction by
the same estimate already checked. If \(X_*\) is the terminal theorem's
limit, its certified tube supplies such a positive margin through
\(\lambda_0-J\|X_*-X_0\|>\lambda_0/2\).

The exact q=1 residual equation shows that the norm-dependent term comes
from the key-motion contribution. At an interpolating state, setting
\(r=0\) does not algebraically force the accumulated values or current
feature/key gaps to vanish. This supports the stated possibility of
\(b_*\ne0\), without establishing its value at a typical reached endpoint.
The note states this limitation accurately.

No mathematical correction is required to the proposition or the
non-differentiability claim in their stated scope.
