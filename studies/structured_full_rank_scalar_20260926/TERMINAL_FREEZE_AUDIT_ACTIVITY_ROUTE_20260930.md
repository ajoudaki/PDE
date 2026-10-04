# Independent audit of the terminal-freeze estimate

2026-09-30. Scoped check by the activity-memory route. The initial input was the complete theorem statement sent by the supervisor. After completing the reconstruction below, the auditor read the full `TERMINAL_FREEZE_THEOREM_20260930.md` and checked its exact P1 normalization, assumptions and estimates. No other route's sources or experiments were used. The original activity-memory route remains frozen.

**Verdict: the stated terminal estimate is correct under the explicit tube and coefficient hypotheses below.** It is a finite terminal continuation initialized from current aggregate coefficients. It does not by itself construct the preceding changing-feature aggregate dynamics or an arbitrary-query representation of the entire final function.

## 1. Exact hypotheses needed

Write \(\|v\|_m=(m^{-1}\sum_i v_i^2)^{1/2}\), with associated inner product \(\langle\cdot,\cdot\rangle_m\). The induced matrix operator norm is the usual Euclidean operator norm. Shift the proposed freeze point to time zero. Assume the exact trajectory satisfies

\[
\dot r=-K(t)r+\rho d(t),\qquad \rho=\|r\|_m,
\tag{1}
\]

and, for one scalar passive test output,

\[
\dot y=-\langle k(t),r\rangle_m+\rho b(t).
\tag{2}
\]

Here the coefficients are absolutely continuous along the exact trajectory, with

\[
\|\dot K(t)\|_{\rm op}+\|\dot d(t)\|_m\le A\rho(t),\qquad
\|\dot k(t)\|_m+|\dot b(t)|\le B\rho(t).
\tag{3}
\]

These bounds must hold for the whole terminal trajectory. If established only on a tube, a separate no-exit argument must keep the exact trajectory in that tube. Merely calling the initial neighborhood a reachable tube does not prove this fact.

Put

\[
\lambda_0=\lambda_{\min}(\operatorname{sym}K_0)-\|d_0\|_m>0,
\qquad M=\|k_0\|_m+|b_0|.
\]

For \(A>0\), the supervisor's sufficient smallness condition is

\[
\rho_0<\frac{\lambda_0^2}{4A}.
\tag{4}
\]

For \(A=0\), omit (4). The frozen model uses the same \(r_0,y_0\):

\[
\dot{\bar r}=-K_0\bar r+\|\bar r\|_m d_0,\qquad
\dot{\bar y}=-\langle k_0,\bar r\rangle_m+\|\bar r\|_m b_0.
\tag{5}
\]

The scalar coefficient called \(d_{\rm test}\) in the supervisor's statement is denoted \(b\) here to distinguish it from the vector \(d\). For a different normalization of the test equation, its dual norm and the definition of \(M\) must be changed accordingly.

## 2. Activity and contraction checks

Let \(s(t)=\int_0^t\rho(v)\,dv\). Equation (3) implies

\[
\|K(t)-K_0\|_{\rm op}+\|d(t)-d_0\|_m\le As(t).
\]

For every unit vector \(v\), the change in its quadratic form for the symmetric part of \(K\) is bounded by \(\|K-K_0\|_{\rm op}\). Taking the infimum over \(v\), and applying the triangle inequality to \(d\), yields

\[
\lambda_{\min}(\operatorname{sym}K(t))-\|d(t)\|_m
\ge\lambda_0-As(t).
\]

At \(\rho>0\), differentiate its squared norm in (1) to obtain

\[
\dot\rho\le-(\lambda_0-As)\rho.
\tag{6}
\]

As long as \(s\le\lambda_0/(2A)\), this gives \(\rho(t)\le\rho_0e^{-\lambda_0t/2}\) and

\[
s(t)\le 2\rho_0/\lambda_0<\lambda_0/(2A).
\]

The strict inequality excludes the first crossing of the bootstrap boundary. Thus, subject to the tube condition,

\[
\rho(t)\le\rho_0e^{-\lambda_0t/2},\qquad
S=\int_0^\infty\rho(t)dt\le2\rho_0/\lambda_0.
\tag{7}
\]

At a zero residual, (1) has zero right-hand side; its locally bounded coefficients and Lipschitz dependence on \(r\) give the absorbing zero solution. Equivalently, the estimates can be stopped at the first zero and continued by that solution. Norm inequalities at zeros are interpreted as upper Dini derivative inequalities.

For the frozen residual vector field \(F_0(v)=-K_0v+\|v\|_m d_0\), and \(e=v-w\),

\[
\begin{aligned}
\langle e,F_0(v)-F_0(w)\rangle_m
&\le-\lambda_{\min}(\operatorname{sym}K_0)\|e\|_m^2
+|\|v\|_m-\|w\|_m|\,\|e\|_m\|d_0\|_m\\
&\le-\lambda_0\|e\|_m^2.
\end{aligned}
\]

The last step uses the reverse triangle inequality. Therefore the nonlinear frozen field is globally contracting at rate \(\lambda_0\). Symmetry or positive semidefiniteness of \(K_0\) itself is unnecessary; the stated lower bound on its symmetric part is what the proof uses. In particular, \(\|\bar r(t)\|_m\le\rho_0e^{-\lambda_0t}\).

## 3. Residual and passive-output error checks

Rewrite the exact residual equation as \(\dot r=F_0(r)+g(t)\), where

\[
g(t)=-(K(t)-K_0)r+\rho(d(t)-d_0),\qquad
\|g(t)\|_m\le As(t)\rho(t).
\]

For \(e(t)=\|r(t)-\bar r(t)\|_m\), frozen contraction gives

\[
D^+e\le-\lambda_0e+As\rho,\qquad e(0)=0.
\]

Multiplication by \(e^{\lambda_0t}\) and integration give

\[
e(t)\le A\int_0^t e^{-\lambda_0(t-v)}s(v)\rho(v)\,dv.
\]

Integrating this nonnegative bound and interchanging the two integrals yields

\[
\int_0^\infty e(t)dt
\le\frac A{\lambda_0}\int_0^\infty s(t)\rho(t)dt
=\frac{AS^2}{2\lambda_0},
\tag{8}
\]

because \((s^2/2)'=s\rho\). This proves the supervisor's residual-integral bound.

For the output, splitting coefficient drift from residual drift gives

\[
|\dot y-\dot{\bar y}|
\le\left(\|k(t)-k_0\|_m+|b(t)-b_0|\right)\rho+Me
\le Bs\rho+Me.
\]

The coefficients are bounded along the terminal trajectory by their initial values plus \(BS\). Equation (7) therefore makes \(\dot y\) integrable; the frozen residual estimate does the same for \(\dot{\bar y}\). Both terminal outputs exist, and integration gives the uniform bound, hence also the endpoint bound,

\[
\sup_{t\ge0}|y(t)-\bar y(t)|
\le\frac12\left(B+\frac{MA}{\lambda_0}\right)S^2
\le\frac{2\rho_0^2}{\lambda_0^2}
\left(B+\frac{MA}{\lambda_0}\right).
\tag{9}
\]

This directly compares physical time and terminal outputs. It does not need the matched-activity stopping-time transversality hypothesis from the separate positive-relaxation-memory route.

## 4. Optional strengthening and practical limits

The factor-two bootstrap is correct but not sharp. Equation (6) gives

\[
\rho(t)+\lambda_0s(t)-\tfrac A2s(t)^2\le\rho_0.
\]

If \(0<\rho_0<\lambda_0^2/(2A)\), the quadratic on the right side of \(\rho\le\rho_0-\lambda_0s+As^2/2\) is negative strictly between its two roots. Since \(\rho\ge0\) and \(s\) is continuous from zero, \(s\) cannot enter that interval. Thus

\[
S\le s_*=
\frac{2\rho_0}{\lambda_0+\sqrt{\lambda_0^2-2A\rho_0}},\qquad
\rho(t)\le\rho_0e^{-\sqrt{\lambda_0^2-2A\rho_0}\,t}.
\]

This improvement is optional; it is not needed to validate (7)–(9). When \(A=0\), exact and frozen residuals agree, \(S\le\rho_0/\lambda_0\), and only drift of the test coefficients contributes to output error.

The qualifications affecting interpretation are:

- A quadratic terminal error assertion requires \(A,B,M\) bounded and \(\lambda_0\) bounded away from zero in the considered family of freeze points. A separate finite bound at each freeze point is not a uniform \(O(\rho_0^2)\) theorem.
- Training directions with zero or insufficient symmetric-part margin violate \(\lambda_0>0\). The theorem does not cover them by continuity in \(\lambda_0\), since the bounds diverge.
- The current coefficients and their certified bounds must be available from permitted information. Computing them once from a sampled population may cost at least linear work; the theorem only compresses subsequent continuation.
- For fixed training size and finitely many requested outputs, (5) is a finite ODE with a width-independent number of states and coefficients. It evolves residuals and outputs, not the changing internal feature population.
- For the entire final test function, one still needs an admissible finite representation of \(u\mapsto(y_0(u),k_0(u),b_0(u))\), with uniform bounds. Retaining the original population to evaluate these maps on arbitrary later queries is not aggregate-only function compression.
- Numerical errors in initial coefficients, current residuals or test outputs require additional perturbation terms. They are not included in the zero-initial-error estimate (9).
- The frozen model approaches zero residual exponentially and has exact absorption if zero is reached. A practical positive stopping tolerance contributes its own terminal tail bound.

Within those limits, the terminal-freeze theorem closes a real terminal comparison problem and controls the selected test outputs explicitly. It should be presented as a terminal continuation result, not as the full active-phase aggregate closure.

The written theorem also asserts \(\sup_t\|r(t)-\bar r(t)\|_m\le AS^2/2\); this follows from the same convolution bound by replacing its exponential factor by one. Its stated state-tube condition, P1 coefficient normalization, separate treatment of \(A=0\), and arbitrary-query representation limitation are consistent with this audit. No correction to its displayed estimates is required.
