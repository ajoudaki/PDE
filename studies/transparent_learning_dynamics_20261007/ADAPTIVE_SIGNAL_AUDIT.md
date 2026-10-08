# Audit of adaptive Gaussian signal concentration

2026-10-07. Reviewer: the independent kinetic-route agent. Scope: the complete 238-line `ADAPTIVE_SIGNAL_CONCENTRATION.md`, the reviewer's own kinetic route, and required proof/presentation/process skills. No other scientific source, route, study, experiment, web resource, or Git material was read. This is an internal mathematical audit, not a promotion review. The reviewed note was not edited.

Reviewed hashes:

- `ADAPTIVE_SIGNAL_CONCENTRATION.md`: `28538f84405a18570a533da72f74c0afe16569a3c7883d5b3a314a775359e118`.
- `KINETIC_OBSERVABLE_ROUTE.md`: `9b27269a8c1e6831aa941b95100d31e0a30baeb3eab6f37e004e65efad1bcd2a`.

## Verdict

The main uniform concentration theorem, its constants, and its same-coefficient adaptive substitution are correct under the stated boundedness and coefficient-Lipschitz hypotheses. The circuit sensitivity bound is also valid under the natural interpretation that variable affine coefficients are coordinates of the coefficient vector, fixed gate functions do not themselves vary with that vector, and affine biases are counted.

Two specifications should be explicit before reusing the circuit corollary: the coefficient parameterization just described, and a bound on the scalar-gate Lipschitz constant in the claimed polylogarithmic regime. The proof can also accommodate coefficient inputs used as ordinary nodes, but the displayed intermediate bounds need a small adjustment when their range exceeds the internal clipping range. These issues do not change the main theorem or its constants.

The lemma applies directly to the bounded, clipped program. Applying it to an unclipped neural program additionally needs control of the *population* truncation error. High-probability equality on the observed Gaussian samples alone is insufficient; Section 4 below gives a concrete counterexample with a very short product circuit. The note already leaves localization and dynamical stability open, so this is an application obligation rather than a contradiction of its principal theorem.

## 1. Complete check of the concentration inequality

Use the note's notation: there are \(n\) independent Gaussian vectors in \(\mathbb R^r\), \(J\) observables, \(s\) coefficients in \([-B,B]^s\), global output bound \(M\), and coefficient Lipschitz bound \(L\) on the Gaussian cube. All these bounds describe a fixed function family. Measurability in the Gaussian variable is implicit in the stated expectations; it should be understood throughout.

The truncation radius is

\[
R=\sqrt{2\log(4nr/\delta)},\qquad e^{-R^2/2}=\frac{\delta}{4nr}.
\]

The two Gaussian tail calculations are exact with the chosen conservative tail bound:

\[
\mathbb P\{\exists i:g_i\ne g_i^R\}
\le2nr e^{-R^2/2}=\delta/2,
\]

and, for one independent Gaussian vector,

\[
\sup_{\theta,j}|\mathbb EF^j_\theta(g)-\mathbb EF^j_\theta(g^R)|
\le2M\mathbb P(g\ne g^R)
\le4Mr e^{-R^2/2}=M\delta/n.
\]

The global bound \(|F^j_\theta(g)|\le M\) is used twice in the second calculation. A bound only inside the cube would not justify this expectation estimate.

Let \(\varepsilon=1/(nL)\). Partitioning an interval of length \(2B\) into \(\lceil B/\varepsilon\rceil\) equal subintervals and taking their centers gives an \(\varepsilon\)-net. Its cardinality in \(s\) coordinates is at most

\[
\lceil BnL\rceil^s\le(1+BnL)^s\le(1+2BnL)^s.
\]

Thus the note's slightly larger net bound is safe. The centers lie in the coefficient cube.

At a fixed net point, clipping each sample independently preserves independence. A variable in \([-M,M]\) has centered log moment-generating function bounded by \(t^2M^2/2\): under every exponential tilt its variance is at most \(M^2\), and twice integrating the second-derivative bound gives the assertion. The two-sided average tail therefore is

\[
2\exp[-nt^2/(2M^2)].
\]

With

\[
t=M\sqrt{\frac2n
\left[s\log(1+2BnL)+\log(4J/\delta)\right]},
\]

the union bound over \(J(1+2BnL)^s\) possibilities is at most \(\delta/2\). Moving from a coefficient vector to a net point costs \(L\varepsilon=1/n\) in its clipped sample mean and another \(1/n\) in its clipped population mean. Intersecting with the no-sample-clipping event and adding the population clipping bias gives precisely

\[
t+\frac{2+M\delta}{n}
\]

with failure probability at most \(\delta\). There is no missing factor of two or missing \(r\)-factor in the note's inequality (2).

The net event is finite and measurable. On that event, the deterministic Lipschitz extension proves the claim for all coefficient vectors, so no uncountable-union probability argument is required. The proof also works for \(s=0\), interpreted as a one-point parameter set, and for \(n=1\); in the latter case the bound can simply be noninformative.

## 2. Adaptive coefficients: what is and is not qualified

The adaptive substitution in lines 112–129 is valid. If an event holds simultaneously for every coefficient in a fixed cube, it holds for any selected coefficient in that cube, even when selection uses the complete Gaussian sample and arbitrarily dependent additional data. Different observables may use different correlated selections.

The population quantity is

\[
\left[\theta\mapsto\int F^j_\theta(g)\,d\gamma_r(g)\right]
\bigg|_{\theta=\widehat\theta}.
\]

It is not generally the conditional expectation of \(F^j_{\widehat\theta}(g_i)\) given \(\widehat\theta\). The note explicitly uses the correct fixed-argument meaning.

Three boundaries should remain explicit:

1. The function family and its deterministic bounds are fixed independently of the sample. Additional randomness may select its coefficient argument; it may not silently change its gate functions, topology, clipping levels, or indexing class.
2. If membership of the selected coefficient in the cube is known only on a localization event, the probability of leaving that event must be added to the theorem's failure probability.
3. A random coefficient trajectory is covered at every time if all its values lie in this same fixed coefficient class. A growing program, variable transcript length, or sample-selected grammar requires a common containing class or a further union bound. Uniformity in coefficients alone does not count those new choices for free.

The note's distinction between same-coefficient concentration and comparison to a separately evolved population system is correct and necessary. No stability estimate is supplied by the concentration event.

## 3. Circuit sensitivity, coefficient accounting, and entropy

For the stated induction, interpret every nonconstant affine weight and every nonconstant affine bias as a coordinate of \(\theta\), allowing reuse of a coordinate. Fixed coefficients and fixed scalar gate functions are part of the grammar. Then changing coefficients by \(h=\|\theta-\theta'\|_\infty\) changes each edge weight or bias by at most \(h\).

If prior computational nodes are bounded by \(A\), and their differences by \(C_0^k h\), the affine preactivation difference is

\[
\left|\sum_j\beta_jx_j+b-\sum_j\beta'_jx'_j-b'\right|
\le pB C_0^k h+(pA+1)h.
\]

The final \(h\) is the possible bias contribution. A fixed scalar gate multiplies the bound by at most \(a\), and clipping is nonexpansive. Since \(C_0^k\ge1\), it is sufficient that

\[
C_0\ge a(pB+pA+1),\qquad C_0\ge2A,
\]

which the note's

\[
C_0=4(p+1)(B+1)(A+1)(a+1)
\]

satisfies with ample slack. A product difference is bounded by \(2AC_0^kh\). Following a topological ordering of at most \(p\) gates establishes the claimed \(C_0^{p+1}\) coefficient-Lipschitz bound. Reusing coefficients does not invalidate the estimate; their repeated occurrences were already counted by the fan-in bound.

There are two specification points:

- Merely requiring an affine coefficient to be bounded by \(B\) does not control its sensitivity to a separate parameterization. If \(\beta(\theta)=\operatorname{sign}\theta\) were allowed as an uncounted coefficient transformation, even a one-gate output could fail to be coefficient-Lipschitz. Such transformations must either be actual coordinates of the coefficient vector or be implemented and counted as gates with controlled sensitivity. Likewise, the scalar gate function cannot vary arbitrarily with \(\theta\) merely because each fixed-\(\theta\) gate is Lipschitz in its scalar input. The intended coordinate-based interpretation appears natural from the note, but should be stated directly.
- If raw coefficient inputs are also allowed as ordinary previous nodes, they may have absolute value \(B>A\). Then the intermediate bounds should use \(D=\max(A,B)\): the affine bound becomes \(pBC_0^kh+(pD+1)h\), and the product bound becomes \(2DC_0^kh\). The same displayed \(C_0\) still dominates both, so the final sensitivity bound survives. Alternatively, the grammar can restrict coefficient coordinates to edge weights and biases.

The entropy step is correct because \(C_0^{p+1}\ge1\) and

\[
1+2BnC_0^{p+1}\le(1+2Bn)C_0^{p+1}.
\]

Taking logarithms gives the note's inequality (7). Under the gate grammar, at most \(p\) gates each use at most \(p\) affine weights and one bias, so \(s\le p(p+1)\) is available when there are no additional free gate parameters. The stated conditional bound \(s\le(p+1)^2\) is safe and also allows slack. Fixed coefficients still need magnitude bounds even though they do not contribute to \(s\).

The polylogarithmic-rate sentence in lines 180–185 needs one additional explicit qualification. Besides the listed bounds, require \(\log a\), \(\log J\), and \(\log(1/\delta)\) to be polylogarithmic in \(n\), or state that the gate family, output count, and confidence are fixed in the relevant limit. The entropy actually contains

\[
s\left[\log(1+2Bn)+(p+1)
\log\bigl(4(p+1)(B+1)(A+1)(a+1)\bigr)\right]
+\log(4J/\delta).
\]

The assumptions on \(p,M,\log A,\log B\) alone do not bound \(\log a\). A fixed admissible activation and its derivative do provide a fixed \(a\): a strip derivative bound \(L\) on width \(\rho\) gives, on the real line, \(\operatorname{Lip}(\phi)\le L\) and \(\operatorname{Lip}(\phi')\le2L/\rho\). In that intended setting the missing rate qualification is readily met. The dependence on \(r\) enters through \(R\le A\), not through an omitted coefficient dimension.

## 4. Clipping the population observable is a separate obligation

The original theorem compares the bounded function \(F\) at Gaussian samples and at a fresh Gaussian argument. It correctly bounds the additional *input* clipping bias of this already bounded function. It does not compare an original unbounded function \(H\) with a modified, internally/output-clipped program \(F\).

For that application one needs a bound such as

\[
\sup_\theta\mathbb E|H_\theta(g)-F_\theta(g)|
\]

in addition to any high-probability event on which \(H_\theta(g_i)=F_\theta(g_i)\) for the observed samples. This distinction is material for the permitted unbounded activation values and product gates.

Here is a counterexample to inferring population localization from sample localization alone. Take \(r=1\), a fixed confidence \(\delta\), and the note's \(R\asymp\sqrt{\log n}\). Choose an even power \(d=2^k\) with \(d\asymp(\log n)^2\), and consider the raw circuit

\[
H(g)=(g/R)^d.
\]

One affine scaling and \(k=O(\log\log n)\) squaring gates compute it. Let \(F\) be this program with internal clipping level \(A=R\) and final clipping level \(M=1\); all edge coefficients are bounded by \(B=1\), and the scalar gates have \(a=1\). When \(|g|\le R\), every intermediate value after the scaling has magnitude at most one, so \(F(g)=H(g)\). Consequently all \(n\) observed samples agree with probability at least \(1-\delta/2\).

Nonetheless, on \(g\in[\sqrt d,\sqrt d+1/\sqrt d]\),

\[
H(g)\ge(\sqrt d/R)^d,
\qquad
\mathbb P\{g\in[\sqrt d,\sqrt d+1/\sqrt d]\}
\ge \frac{c}{\sqrt d}e^{-d/2}
\]

for an absolute positive constant \(c\). The probability inequality follows by bounding the normal density below by its value at the interval's upper endpoint; the additional exponent is \(-1-1/(2d)\), absorbed into \(c\). Hence

\[
\mathbb EH(g)\ge\frac{c}{\sqrt d}
\left(\frac{d}{eR^2}\right)^{d/2},
\]

which grows rapidly since \(d/R^2\asymp\log n\), whereas \(0\le\mathbb EF\le1\). This counterexample has a short program, bounded coefficients, and modest clipping levels. It does not contradict the note's theorem: that theorem applies correctly to \(F\). It shows why the separate localization requirement must include the population tail, rather than only agreement at the finitely many sampled coordinates.

## 5. Gaussian matrix-query application

The closing warning about adaptive matrix actions, transpose queries, rank issues, and weak-observable stability is appropriate. No all-time neural conclusion follows from the audited lemma alone.

In particular, the coordinatewise representation asserted in lines 196–204 requires a hypothesis on the query program: each new query coordinate must itself be formed from the permitted coordinatewise signal history and globally shared scalar coefficients, and the correct conditional Gaussian response must be implemented, including projections and regression terms. Arbitrary adaptively chosen dense queries do not acquire this scalar-circuit representation merely because their number is finite.

The note's final clause, “if the exact query program has been placed in the bounded grammar,” is the correct application gate. Treat the preceding representation paragraph as conditional on that gate, not as a proved representation theorem for every sequential matrix-query algorithm. The supplied audit input contains no complete query-conditioning construction, so I do not certify that construction or the final reference to an exact polar theorem. These missing inputs do not affect verification of Sections 1–3.

## 6. Separate qualification of the reviewer's shallow theorem

The all-time shallow theorem in my frozen route is a fixed-label result with a new explicit smallness threshold. Its proof chooses the Gaussian envelope \(P\), sets \(M=\mathbb EP\) and \(\lambda=\lambda_0/2\), and imposes

\[
|y|\le y_*:=\frac{\lambda}{2}
\min\left\{1,\sqrt{\frac{\lambda_0}{8M}},\frac{\lambda}{4M}\right\}.
\]

The last restriction, \(\bar S\le\lambda/(4M)\), is used to absorb the kernel-perturbation term in the integral residual comparison. It is additional to maintaining a positive feature Gram for either flow separately. The envelope contains an exponential in the Gaussian initial-coordinate norm, so its expectation and the resulting label cap can be conservative. Positivity of the initial Gram alone does not imply this cap, and an existing source's fitting condition need not imply it.

The concentration note supplied for this audit does not state the source's admissible-label inequality. Under the assigned read scope I therefore cannot verify an equivalence or containment between that source qualification and \(|y|\le y_*\). The shallow theorem must be advertised as applying to this explicitly narrowed subclass unless the supervisor independently proves that the source's admissible labels satisfy the additional bound. The cap is independent of \(n\), but width-independence does not make it equivalent to the source's qualification.

Other precise limitations of my theorem are:

- Labels and the input panel are fixed independently of the sampled initialization. The proof does not establish a single concentration event uniform over initialization-adaptive labels.
- It assumes zero initial readout and bounded first and second real activation derivatives. Its stated strip hypothesis supplies those derivative bounds; a weaker interpretation of strip analyticity would not.
- Its probability estimate has the form \(\delta+C_0/n\) with error \(C_1/(\delta\sqrt n)\). It gives \(O_{\mathbb P}(n^{-1/2})\) for each fixed admissible label vector, not a sub-Gaussian confidence profile or a uniform guarantee over a growing observable class.
- It compares panel outputs to an infinite-dimensional deterministic kinetic law. It neither retains the realized leading fluctuation nor proves finite spectral approximation or a deep extension.

I found no algebraic failure in the shallow proof's Gram bootstrap, total-variation concentration, or residual-error absorption at its explicit cap. The crucial scope risk is substituting a broader source label condition for that cap without proving the implication.

## Requested disposition

Retain the concentration inequality and adaptive same-coefficient conclusion. Make the circuit parameterization and rate qualifications explicit when using the corollary. Keep population clipping bias, exact Gaussian-query representation, and comparison stability as distinct unresolved obligations. The audit supports the bounded-class concentration bridge; it does not certify a complete aggregate neural dynamics theorem.
