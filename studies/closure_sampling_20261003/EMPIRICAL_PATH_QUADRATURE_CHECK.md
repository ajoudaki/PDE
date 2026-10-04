# Check of finite empirical path quadrature

2026-10-03. Complete collaborative reconstruction, not an independent
promotion review. Source read in full:
`EMPIRICAL_PATH_QUADRATURE.md`, SHA-256
`584cea2959b54aa678f931a43b6eea21180a8cbbff0ca09dfd6e63f2ba046438`.
The complete corrected source was also read at SHA-256
`9b92ba8cf4405d805a77661877118f13cdfe492d804d9f76b2747bb3ea1a80b9`.
The canonical-notation skill, its neural reference, and the rigorous-math
skill were applied. No trained path, additional study source, experiment,
or external theorem was imported.

**Verdict:** the finite-reference sampling lemma, its full-time bound,
and the separation from autonomous dynamics are correct. The count
arithmetic is correct for strict power savings. The boundary wording
qualification reported below has been corrected in the second source
version: \(\alpha=3/5\) or \(D=10\) does not decide whether the
count is \(o(n)\). The revised source passes the complete check.

## Conditional variance and absence of population bias

Fix the initialization and hence the unique original reference path, as
well as the partition chosen from the permitted initialization data.
The independent random choices \(I_s\) are then the only randomness.
For \(k_s=|C_s|\), define the cell-average velocity
\(\overline{\dot F}_s=k_s^{-1}\sum_{i\in C_s}\dot F_i\).
Each centered field
\(\dot F_{I_s}-\overline{\dot F}_s\) has conditional mean zero.
Independence of selections in distinct cells eliminates all cross terms,
including after integration in the query variable. Inside one cell,

\[
\frac1{k_s}\sum_{i\in C_s}
 \|\dot F_i-\overline{\dot F}_s\|_{L^2(\mu)}^2
=\frac1{2k_s^2}\sum_{i,j\in C_s}
 \|\dot F_i-\dot F_j\|_{L^2(\mu)}^2=V_s.
\]

This proves source equation (1), including the factor \(1/2\).
The same conditional averaging without differentiation shows
\(\mathbb E Q_NF=n^{-1}\sum_iF_i\) exactly, at every time and query.
The target is the realized finite predictor, so there is no population
bias term. Dependence of the reference on initialization causes no
problem after conditioning. Dependence on the sampling coins would
cause a problem, which is why this calculation is confined to the
unchanged reference path.

## Full-time estimate

Let \(e=Q_NF-n^{-1}\sum_iF_i\). On every finite interval, absolute
continuity and \(e(0,x)=0\) give
\(\sup_{t\le T}|e(t,x)|\le\int_0^T|\dot e(s,x)|ds\).
Apply Minkowski directly in \(L^2\) of the joint sampling and query
spaces:

\[
\begin{aligned}
\left[\mathbb E\int\sup_{t\le T}|e(t,x)|^2d\mu(x)\right]^{1/2}
&\le\int_0^T
 \left[\mathbb E\int|\dot e(s,x)|^2d\mu(x)\right]^{1/2}ds\\
&=\int_0^T\left[\sum_{j=1}^N p_j^2V_j(s)\right]^{1/2}ds.
\end{aligned}
\]

Increasing \(T\) and applying monotone convergence gives source
equation (2). Absolute continuity is needed for almost every query on
finite intervals; measurability and the displayed integrability justify
the integrations. For neural reference paths these are the assumptions
the source explicitly retains, rather than an additional uniform neural
estimate proved by the quadrature calculation.

If the right side is \(B_N<\infty\), Markov applied to the squared
query-time error yields the stated conditional sampling guarantee
\(B_N/\sqrt\delta\) with probability at least \(1-\delta\).
There is no independence assumption across times and no time-grid union
bound. Existing endpoint limits are covered by the time supremum.
An initialization-level theorem would additionally need to control
\(B_N\) on high-probability initialization events.

## Stratification and the missing dynamics

Under the source's explicit diameter and Lipschitz hypotheses,
\(V_s(t)\le C L(t)^2N^{-2/D}\), while
\(\sum_sp_s^2\le\max_sp_s\sum_sp_s\le C/N\).
Substitution proves equation (3). Using this as a width-uniform neural
rate would require bounds on the mark dimension, cell geometry, and
\(\int L\) uniform in the actual chosen width and memory order.
The note correctly does not claim those bounds.

Equation (4) is an exact algebraic identity. Its first term compares
the smaller system's own responses to unchanged reference responses.
That term includes changes to the mixer and its transpose, the memories,
residual, and clock. Neither centering nor small variance of the second
term controls it. Supplying selected neurons with their exact trained
reference histories would not be an autonomous compression algorithm.
The source consistently maintains this distinction.

## Count arithmetic and the boundary qualification

Given the explicitly hypothetical full-dynamics error
\(N^{-\alpha+o(1)}\), root-width accuracy requires
\(N=n^{1/(2\alpha)+o(1)}\). Combining it, without additional losses,
with the original-system order \(q=n^{1/6+o(1)}\) gives exponent
\(1/(2\alpha)+1/6\). This exponent is strictly below one exactly
when \(\alpha>3/5\). All three table entries are correct.

With \(\alpha=1/2+1/D\), the neuron exponent is
\(D/(D+2)\), and adding \(1/6\) gives a strict power saving exactly
for \(D<10\). At \(D=10\), or \(\alpha=3/5\), unspecified
subpolynomial factors could produce \(n/\log n\), \(n\), or
\(n\log n\). Therefore the phrases “strict sublinearity requires”
and “below linear precisely when” should be read as, or replaced by,
“a strict power saving requires” and “the power exponent is below one
precisely when.” This does not change any claimed quadrature bound or
provide a missing neuron-reduction theorem.

The second source version now explicitly says “a strict power saving
below linear requires alpha>3/5,” treats the equality case separately,
and likewise states that \(D=10\) leaves subpolynomial factors
undetermined. Those changes resolve the qualification completely.

## Actual reference-path Monte Carlo corollary

The coordinator supplied the manuscript's existing actual-closure speed
bounds as additional input for this bounded check. They yield an
unconditional reference-path corollary on the common fitting event,
without a new mark-smoothness hypothesis. Write \(A=W^{(1)}\) and
\(W=W^{(2)}\). For a query \(x\),

\[
\dot z^{(1)}=\dot A x/\sqrt d,\qquad
\dot z^{(2)}=\dot W h^{(1)}+W\dot h^{(1)}.
\]

The given bounds
\(\|\dot A\|_F/\sqrt n\le CY\rho\),
\(\|\dot W\|_F\le CY\rho\), \(\|W\|_{\rm op}\le C\),
and \(|\phi|,|\phi'|\le1\) imply

\[
\frac{\|\dot z^{(2)}(t,x)\|_2}{\sqrt n}
\le CY\rho(t)(1+\|x\|_2/\sqrt d).
\]

For the vector \(F(t,x)\) of all original neuron contributions,
\(\dot F=\dot w\odot h^{(2)}+
w\odot\phi'(z^{(2)})\odot\dot z^{(2)}\).
Using the supplied \(\|\dot w\|_2/\sqrt n\le2\rho\) and
\(\|w\|_\infty\le CY\), and a fixed small-label upper bound,
gives

\[
\frac{\|\dot F(t,x)\|_2}{\sqrt n}
\le C\rho(t)(1+\|x\|_2/\sqrt d).
\]

Thus, for a fixed query law with finite second moment,

\[
\left[\frac1n\sum_{i=1}^n
       \|\dot F_i(t,\cdot)\|_{L^2(\mu)}^2\right]^{1/2}
\le C_\mu\rho(t),\qquad
\int_0^\infty\rho(t)dt\le CY.
\tag{A}
\]

Suppose the frozen cells are balanced in the elementary sense
\(p_s\le C_0/N\). Removing the cell mean can only decrease its
second moment, so

\[
\begin{aligned}
\sum_s p_s^2V_s(t)
&\le\sum_s\frac{|C_s|}{n^2}
                  \sum_{i\in C_s}\|\dot F_i(t,\cdot)\|_{L^2(\mu)}^2\\
&\le\frac{C_0}{N}\frac1n\sum_i
                  \|\dot F_i(t,\cdot)\|_{L^2(\mu)}^2.
\end{aligned}
\]

Substitute (A) into the source's proved equation (2). Conditional on
any initialization in the common fitting event, for each chosen order
\(q\),

\[
\left[\mathbb E\int\sup_{t\ge0}
 |Q_NF(t,x)-\widehat f_{n,q}(t,x)|^2d\mu(x)\right]^{1/2}
\le\frac{C_\mu Y}{\sqrt N}.
\tag{B}
\]

The constants are independent of \(n,q,N\), physical time, and the
particular balanced initialization-measurable partition. This permits
any prescribed order sequence. It does not assert one sampling event
controlling the supremum over all orders simultaneously. Markov gives
the conditional probability bound \(C_\mu Y/\sqrt{N\delta}\).
Zero labels are stationary and satisfy (B) trivially.

Equation (B) is an actual all-time finite-reference quadrature guarantee,
including the endpoint. It requires no finite-dimensional mark law and
has no population bias. It remains a bound for selected contributions
on the unchanged reference trajectory. It neither supplies those
trajectories to an autonomous smaller network nor controls the first
term in source equation (4), and its \(N^{-1/2}\) rate alone does
not give the requested strict power saving in neuron count.
