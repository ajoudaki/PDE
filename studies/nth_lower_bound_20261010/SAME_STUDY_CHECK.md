# Bounded check of the full-trajectory polynomial upper bound

Checker: /root/nth_lower_scalar, 2026-10-10. This is an internal same-study
check, not an isolated promotion review. The checker authored the scalar
route, the prior deep consistency check, and STRONGER_SOURCE.md.

The complete scientific input read for this assignment was
POLYNOMIAL_UPPER.md at SHA256
e47d137f1fd156190015399759ba2c47720256263b1a979ab8c77bb316a7c144,
using the previously read same-study RESULT.md and ANALYTIC_ROUTE.md
dependencies. No further scientific search, experiment, or file edit
outside this report was performed.

No blocking algebraic or contract error was found in the stated upper bound.
Its scope is the fixed deep linear witness, the stated small-label range,
the standard frozen-top hierarchy, and retained tensor-array coordinates.
It explicitly excludes the cost and storage of dense coefficient generation.
The latter distinction is necessary for interpreting its sublinear count.

One synthesis correction was requested: the original final discussion
described only the older subpolynomial lower bound. STRONGER_SOURCE.md
now supplies a positive polynomial lower exponent for this same witness.
The author's revised scope and synthesis paragraphs were subsequently
read at SHA256
7f397d8bb0b05c3df1d922fef11b68ff8707b4b5825e287cf61af7b3b50d8c75.
They correctly identify the remaining gap as one between polynomial
exponents and distinguish retained arrays from coefficient-production
storage and time. This point is resolved. The follow-up read was limited
to those amended passages; no scientific proof change was reported.

## Kernel path representation and remainder

The kernel is expanded with its first two indices fixed and its appended
driving indices ordered from latest integration time to earliest. Repeated
integration of the exact or truncated hierarchy has exactly that order.
Directional derivatives preserve symmetry of the first two indices, so
each finite kernel functional is real symmetric.

Summing absolute values of the ordered integrals yields \(A_u^k/k!\).
For a path variation, summing all possible positions of the inserted
difference factor yields
\[
\frac{A_*^{k-1}}{(k-1)!}
\int_0^t\sum_b|u_b-v_b|.
\]
The \(k-1\) remaining factors are the same scalar absolute-value function;
their permutations account for the retained factorial. Thus the path
Lipschitz estimate is \(S'(A_*)\), with no extra factorial loss.

The initial coefficient bound \(128\,4^k(k+3)!\), the two-by-two operator
factor two, and the simplex volume give
\[
S(A)=1536[(1-4A)^{-4}-1],\qquad
S'(A)=24576(1-4A)^{-5}.
\]
At \(A_*=10^{-6}\), these satisfy the displayed \(1/40\) and \(25000\)
bounds. The dense-state norm estimate \(4/(1-4A_u)<5\) follows by
comparison of the integral norm envelope.

After \(N+1\) integrations, the remaining coefficient is correctly
\(K_{N+3}\) at the earliest moving state. Its bound is
\[
\frac{(N+4)!}{2}5^{N+5}
\frac{A_u^{N+1}}{(N+1)!}
=\frac{625}{2}(N+2)(N+3)(N+4)(5A_u)^{N+1}.
\]
It vanishes uniformly for \(A_u\leq A_*\), justifying equality of the
infinite functional with the actual dense kernel. No infinite-hierarchy
convergence assumption is being inserted.

## Own-residual global stability and the all-time error

The initial kernel gap is \(9/16\). Its path variation is less than
\(1/16\), leaving at least \(1/2\); the proof safely uses only \(1/4\).
The half-MSE residual factor \(1/2\) then gives decay \(e^{-t/8}\).
The control is \(-r/2\), so its action is bounded by
\[
\frac1{\sqrt2}\int_0^\infty\|r(t)\|_2\,dt
\leq4\sqrt2\,\eta<A_*.
\]
This closes a first-exit argument separately for the dense network and
each closure. At finite order, bounded action bounds every retained
tensor by its finite integral expansion, excluding finite-time blowup.
Both models therefore exist globally and fit the same two predictions.

The tail beginning at \(k=q-1\) is bounded by
\(T_q=3072(128\eta)^{q-1}\), including \(q=2\).
The error equation uses the actual difference of residual paths:
\[
\dot e=-\mathcal K_q[u^{(q)}]e/2-\Delta K\,r/2,\qquad
\|\Delta K(t)\|\leq(25000/\sqrt2)\int_0^t\|e\|+T_q.
\]
The gap gives the stated contracting evolution operator without needing
commutation of kernels at different times.

The finite-horizon integral error satisfies
\[
E_1(T)\leq32\eta[(25000/\sqrt2)E_1(T)+T_q].
\]
For \(\eta\leq10^{-8}\), the absorption coefficient is less than \(1/2\).
The resulting \(E_1(\infty)\leq64\eta T_q\) implies
\(\sup\|\Delta K\|\leq2T_q\), and then
\(\sup\|e\|\leq8\eta T_q=24576\eta(128\eta)^{q-1}\).
Every step controls the whole half-line and the closure's own residual.

## Actual dense-pair lower bound

The initial first-prediction derivative is \(\eta Z/2\), where
\(Z=\|W_0B_0e_1\|^2\). The representation \(Z=UV\) with independent
\(\chi_n^2/n\) variables is valid because the conditional distribution of
\(V=Z/U\) does not depend on the Gaussian vector determining \(U\).

The elementary gamma-integral lower bound gives a density maximum
\(e n/2\) for \(V\). Conditional on \(U\geq1/2\), the scaled density
of \(UV\) is at most \(en\). Thus conditioning on \(U,\widetilde Z\)
and using Chebyshev for \(U\) gives
\[
\Pr(|Z-\widetilde Z|\leq\delta)\leq8/n+2en\delta.
\]
Taking \(\delta=n^{-2}\) produces the claimed event probability.
The density argument treats \(n=2\) separately and requires no
asymptotic density approximation.

On the pair of good events, the common analytic disk gives
\(\sup_{0\leq t\leq R/2}|g''(t)|\leq16/R^2\).
The selected time \(t_n=\eta/(2Hn^2)\), \(H=16/R^2\), lies inside
that interval. Taylor's integral remainder then gives
\[
|g(t_n)|\geq\frac{\eta^2}{8Hn^4}
=\frac{\eta^2R^2}{128n^4}.
\]
This is a lower bound for the actual pair discrepancy at an early time,
not for the common fitted endpoint. The union of the pair good event
and the scalar separation event yields exactly the claimed probability
up to the already unspecified absolute exponential constant.

## Order and retained-array count

The ratio of the error prefactor to the dense-pair threshold is exactly
\[
\frac{24576\eta}{\eta^2R^2/128}
=\frac{3\cdot2^{46}}{\eta}.
\]
Consequently the proposed \(q_n\) makes the error at most
\(c_\eta n^{-5}\), while the actual pair is at least \(c_\eta n^{-4}\)
on the same event. The ceiling contributes only a fixed multiplicative
array factor, giving exponent
\[
\frac{5\log2}{\log(1/(128\eta))}<\frac1{20}
\quad\text{when }\eta\leq10^{-62}.
\]
The first-slot linearity of the passive-query hierarchy reconstructs
every sphere prediction from its two training predictions, so no
continuum of extra query states is hidden in that count.

Under this retained-array convention, the construction directly rules
out an \(\Omega(n)\) necessary storage bound for this fixed witness
at the stated dense-pair accuracy. It does not rule out larger
worst-case bounds for another model, another regime, a computational
cost that includes coefficient production, or a precision-sensitive
bit-complexity model.
