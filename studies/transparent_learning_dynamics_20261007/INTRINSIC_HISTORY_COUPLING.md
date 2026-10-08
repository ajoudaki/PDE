# Gaussian history coupling through approximate response directions

2026-10-07. Lead lemma for the global quantitative bridge. A long list of
time samples need not incur a covariance-coupling error proportional to its
literal length. The relevant cost can instead be a finite approximation
dimension plus its population tail.

This is a theorem for an independent sample of a supplied Hilbert-valued
random field. It is not an adaptive Gaussian-matrix conditioning theorem.
It does not on its own couple the whole neural training program.

## 1. Exact statement

Let \(\mathcal H\) be a real separable Hilbert space. Let \(v_1,\ldots,v_n\)
be independent copies of an \(\mathcal H\)-valued random variable \(v\),
with
\[
 \mathbb E\exp\!\left[(\|v\|_{\mathcal H}/A)^\alpha\right]\le M,
 \qquad A>0,\quad M\ge1,\quad \alpha>0 .
 \tag{1}
\]
Let \(P\) be a fixed orthogonal projection of rank at most \(q<\infty\),
with
\[
 \mathbb E\|(I-P)v\|_{\mathcal H}^2\le\varepsilon^2.
 \tag{2}
\]
The projection is fixed with respect to the sample. It can depend on the
population law and on a declared deterministic approximation space.

There is a coupling of centered Gaussian \(\mathcal H\)-valued variables
\(\xi_n,\xi\) such that
\[
 \operatorname{Cov}(\xi_n\mid v_1,\ldots,v_n)
       =\frac1n\sum_i v_i\otimes v_i,\qquad
 \operatorname{Cov}(\xi)=\mathbb E[v\otimes v],
\]
the full population variable \(\xi\) is independent of the sample, and
\[
 \left(\mathbb E\|\xi_n-\xi\|_{\mathcal H}^2\right)^{1/2}
 \le
 2\varepsilon+\frac{A}{\sqrt n}
 \left[
 2+\sqrt q\,\{2\log(2c_\alpha M n)\}^{1/\alpha}
 \right],
 \quad
 c_\alpha=\max\left\{1,
              \left(\frac4{\alpha e}\right)^{2/\alpha}\right\}.
 \tag{3}
\]
No minimum positive covariance eigenvalue and no ambient/history dimension
occurs in (3). In particular, the Hilbert space may be infinite dimensional.

The rank-zero case uses zero projected Gaussians. Formula (3) remains
valid, though directly coupling the two end variables through zero gives
the simpler bound \(2\varepsilon\).

## 2. Gaussian existence and extension with the required independence

The covariance of \(v\) is positive and has trace
\(\mathbb E\|v\|^2<\infty\), by (1). A centered Gaussian variable with this
covariance exists: in a covariance eigenbasis sum independent standard
Gaussians times the square roots of the nonnegative eigenvalues.
The sum converges in \(L^2(\Omega;\mathcal H)\) because their sum is finite.
The same construction applies to block covariances of two such variables,
and to empirical covariances, which have finite rank.

A finite-dimensional projected Gaussian can be extended to the full
Gaussian using the block covariance of \((v,Pv)\). More explicitly, write
the second coordinate's covariance on its finite support, regress the first
coordinate onto that support, and add an independent Gaussian with the
positive residual covariance. Positivity follows by minimizing the variance
of a scalar linear combination of the two coordinates. Trace finiteness
follows from the full covariance trace. Null directions have zero covariance
with the first coordinate and cause no ambiguity.

This extension may be applied conditionally on the empirical sample as
well. If the population projected Gaussian is independent of the whole
sample, its extension uses deterministic population regression/covariance
and additional independent randomness; hence the full population endpoint
is still independent of the whole sample. Independent extension seeds for
different rows preserve independent population Gaussian rows when desired.

## 3. Tail bound and projected covariance coupling

Put \(x=(\|Pv\|/A)^\alpha\). Since projection is a contraction, (1) gives
\(\mathbb E e^x\le M\).
The scalar inequality
\[
 x^{2/\alpha}e^{-x/2}\le c_\alpha,\qquad x\ge0
\]
follows by maximizing its left side at \(x=4/\alpha\).
Choose the deterministic cutoff
\[
 R=A\{2\log(2c_\alpha M n)\}^{1/\alpha}.
\]
Then
\[
\begin{aligned}
 \mathbb E[\|Pv\|^2\mathbf1_{\{\|Pv\|>R\}}]
 &\le A^2c_\alpha
        e^{-(R/A)^\alpha/2}\mathbb E e^x\\
 &\le A^2/(2n).
\end{aligned}
\tag{4}
\]

Within the range of \(P\), set
\(v_R=Pv\,\mathbf1_{\{\|Pv\|\le R\}}\).
It is bounded by \(R\). The finite-dimensional covariance-factor lemma
in GAP_FREE_RESPONSE_STEP.md gives a coupling between empirical- and
population-covariance Gaussians for \(v_R\), with squared mean cost at
most \(R^2q/n\) and population endpoint independent of the whole sample.

Extend both endpoints to the corresponding covariances for \(Pv\),
using the empirical and population block pairs \((Pv,v_R)\).
Each extension costs the square root of the tail in (4) in joint \(L^2\).
Minkowski's inequality therefore bounds the projected Gaussian coupling by
\[
 2A/\sqrt n+R\sqrt{q/n}.
 \tag{5}
\]
The factor \(2A\) safely enlarges \(2A/\sqrt2\).
The projected construction is not an approximation of the target
covariance: after the extensions both projected end covariances are exact.

Finally extend from \(Pv\) to \(v\), using Section 2. At the empirical
end the squared mean extension cost is
\(\mathbb E[n^{-1}\sum_i\|(I-P)v_i\|^2]\le\varepsilon^2\);
at the population end it is the same bound.
Together with (5), Minkowski proves (3).
The Gaussian laws at both final endpoints are exactly those in Section 1.
Truncation and projection are devices for constructing and bounding the
coupling, not changes to either final target law.

## 4. Direct implication for a long time history

For example, take
\(\mathcal H=H^1([0,T];\mathbb R^p)\) with norm
\[
 \|v\|_{\mathcal H}^2=\int_0^T(\|v(t)\|^2+\|\dot v(t)\|^2)\,dt,
 \qquad T>0 .
\]
Its continuous representative satisfies
\[
 \sup_{0\le t\le T}\|v(t)\|
 \le T^{-1/2}\|v\|_{L^2}+\sqrt T\|\dot v\|_{L^2}
 \le (T^{-1/2}+\sqrt T)\|v\|_{\mathcal H}.
 \tag{6}
\]
To see the first inequality, choose a point where the norm is at most
its RMS over the interval, and use the fundamental theorem of calculus
plus Cauchy--Schwarz. Approximation establishes the same statement for
general \(H^1\) functions.

Under the actual hypotheses (1)--(2) in this \(H^1\) space, (3) and (6)
give a uniform-in-time Gaussian-path coupling, with no dependence on the
number of times at which the paths are later sampled.
The factor depending on \(T\) is explicit; no infinite-horizon estimate
is inferred by silently taking \(T\to\infty\).

If a declared approximation space has
\(\varepsilon\le n^{-1/2}\) and \(q\) grows polylogarithmically with \(n\),
while \(A,M,\alpha,T\) obey appropriate fixed or subpolynomial bounds,
then this one covariance-replacement step has
\(n^{-1/2+o(1)}\) path error.
Those are conditional implications, not yet verified neural-history
regularity or compression claims.

A normalized finite history can instead be viewed directly as a finite
Hilbert space of weighted time samples. Formula (3) is unchanged and
depends on its approximation dimension, not its raw number of coordinates.
Pointwise output accuracy still needs a norm that controls point evaluation;
an unweighted assertion from an \(L^2\)-time estimate would be insufficient.

## 5. How this connects to, and does not complete, the current goal

The previous block bound used the full rank of an output covariance. As a
time mesh is refined, that rank can grow merely because more history fields
are sampled. This lemma shows that covariance replacement itself can pay
only for well-approximated response directions, without inserting a
positive history-gap assumption.

The exact proof obligations left for the neural application are:

1. Construct the relevant independent reference-row path law.
2. Prove its Hilbert-norm tail budget (1), not merely separate pointwise
   carrier moments.
3. Supply a deterministic projection with the mean-square approximation
   (2) in a norm strong enough for the desired outputs.
4. Preserve the actual Gaussian-matrix marginal and chronological
   independence while alternating forward and reverse queries.
5. Control the accumulated reaction and shared-coefficient errors through
   the nonlinear trajectory and its fitted tail.

A coupling for a supplied full history is not automatically an online
adaptive simulator. In particular, conditioning on a completed future
query table can reveal information unavailable to a chronological matrix
posterior. The lemma has not done that conditioning; it assumes independent
samples of an already specified reference field, and makes no stronger
causality claim.

The retained candidate remains the causal feature--response system.
This result concerns its quantitative Gaussian-history comparison, not a
new dynamical representation or a further compression objective.

