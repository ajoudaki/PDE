# Isolated review of the Harmonic tolerance corollary

2026-10-10. **PASS for the stated current-construction obstruction.** No
mathematical correction is required. Two wording clarifications below would
make the probabilistic and error-transfer scope explicit.

Inputs read completely: `HARMONIC_ROUTE.md` and
`HARMONIC_TOLERANCE_COROLLARY.md`. The only additional scientific input was
`paper/compact_selected.tex`, lines 1–135 and 884–975, to check the metric,
error-transfer and headline-storage interfaces. Required mathematical and
canonical neural-network notation instructions were also read. No study
history, README, other review or external research input was consulted.

## Rank extension

For fixed \(a>1\), let \(n=\lceil d^a\rceil\), and fix an even integer
\(k>2a\). The parent proof establishes an event depending only on the Gaussian
first matrix on which, simultaneously for every linear source space
\(E\subset\mathbb R^n\) and every nonnegative approximation tolerance
\(\eta\),

\[
 1-\frac{\dim E}{n}\le\frac{2\eta^2}{c_k},
 \qquad c_k=\frac{e^{-4}4^{-k}}{2k!}>0.
\]

Its proof checks: the degree-\(k\) Walsh coefficients exclude the linear
activation term, the diagonal Gram bound is \(c_k\), and the off-diagonal
Frobenius bound yields \(G\succeq(c_k/2)I_n\). Projection and finite Parseval
then yield the displayed inequality for every admissible \(E\), including
spaces chosen after observing the matrix. The failure probability is at most

\[
 p_d=2ne^{-d/16}+2(nd)^{-3}
       +\frac{4n(n-1)}{c_k^2k!d^k}=o(1),
\]

once the parent's condition (10) holds. That condition holds eventually
because \(k\) is fixed and \(\log(nd)/d\to0\).

For deterministic \(\eta_d\to0\), the event gives
\(\dim E/n\ge1-o(1)\). For random tolerances
\(\eta_d\to0\) in probability, the precise conclusion is
\(\dim E/n\to1\) in probability. Indeed, for every \(\varepsilon>0\),
whenever the selected space satisfies the source contract,

\[
 \Pr\!\left(\frac{\dim E}{n}<1-\varepsilon\right)
 \le p_d+
 \Pr\!\left(\eta_d^2>\frac{\varepsilon c_k}{2}\right)
 \longrightarrow0.
\]

If the source contract itself is only required on a success event, the same
bound holds with that event intersected on the left. No independence of the
tolerance, space, or matrix is used. In particular, the corollary's
\(\eta_d^2\le c_k/4\) intersection correctly gives rank at least \(n/2\)
with probability tending to one.

## Metric, storage and polynomial quantifiers

The paper requires \(u_I^\top Mv_I=u^\top v/n\) for every \(u,v\in E\).
Putting \(v=u\ne0\) proves that coordinate restriction to \(I\) has zero
kernel on \(E\), hence \(\lvert I\rvert\ge\dim E\). This argument needs
no positivity hypothesis on \(M\) beyond the identity itself. Under the
explicit selected-first-matrix representation stated in the parent input,
its retained entries therefore cost at least \(d\dim E\ge nd/2\).
This is a representation-specific count of stored real coordinates.

With the fixed family \(m=2\), fixed \(Y,\gamma>0\), fixed activation and
depth, the unchanged headline is \(O_C(d^2)\): the logarithm of its second
term is \(-d\log d+3d\log\log d+O(d)\to-\infty\). Meanwhile
\(nd/d^2\ge d^{a-1}\to\infty\). For any proposed threshold
\(K(1+d)^b\), choose \(a>\max\{b,1\}\), then choose fixed even \(k>2a\),
and only then send \(d\to\infty\). Thus the proof excludes every fixed
finite polynomial degree, with no illicit dimension-dependent choice of
\(k\). Its possibly tiny \(c_k\) affects only the eventual starting point.

## Scope and wording

The supplied corollary correctly limits its conclusion to the uniform
coordinate-source contract, exact metric, and explicit selected-matrix
storage. It establishes neither a lower bound for arbitrary output
approximators nor an obstruction obtained by holding \(d\) fixed and varying
sample count or feature gap. It also leaves the fixed-problem eventual
Harmonic theorem intact.

Two optional clarifications:

- Write the random-tolerance conclusion as
  \(\dim E=n(1-o_{\mathbb P}(1))\), to avoid reading it as almost-sure
  convergence.
- Define the mentioned dense-variability output scale if that phrase is
  retained. For example, the paper's displayed transfer bound certifies an
  \(O(Y/\sqrt n)\) output target with a source tolerance of order
  \(n^{-1/2}/[(1+\sqrt{\log(en)})e^{\sqrt{\log(en)}}]\) for this fixed
  family; its residual tail is \(O(n^{-8})\). This tolerance vanishes, so
  the corollary applies. This is a sufficient certificate from that bound,
  not a necessary source-error condition for accurate outputs or a claim
  about the actual size of dense-model fluctuations.

The looser example tolerances in the corollary also vanish, since any fixed
power of \(\log(en)\) and \(e^{C\sqrt{\log(en)}}\) are \(n^{o(1)}\).
Neither clarification changes the PASS verdict.
