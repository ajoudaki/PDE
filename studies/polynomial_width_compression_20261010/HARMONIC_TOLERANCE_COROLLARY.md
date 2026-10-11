# The Harmonic obstruction does not depend on requesting error Y/n

This is a corollary of the finite source-rank lemma in
[HARMONIC_ROUTE.md](HARMONIC_ROUTE.md), not a lower bound for arbitrary
output compression. It retains the exact source approximation and metric
selection interfaces of the current paper. The frozen rank proof is
unchanged.

Fix any exponent \(a>1\), choose an even integer \(k>2a\), and use
the same admissible family with \(m=2\), fixed positive \(Y,\gamma\),
\(L=2\), activation \(z+\cos z\), and
\(n=\lceil d^a\rceil\). The rank lemma gives, with probability tending
to one, simultaneously for every neuron source space \(E\) whose uniform
coordinate approximation error is at most \(\eta\),

\[
 \dim E\ge n\left(1-\frac{2\eta^2}{c_k}\right),
 \qquad c_k=\frac{e^{-4}4^{-k}}{2k!}>0.
\]

Consequently, for **any deterministic tolerance sequence tending to zero**,
not just \(\eta\le1/n\), the required rank is \(n(1-o(1))\).
In particular it is at least \(n/2\) at all sufficiently large dimensions.
For random tolerances tending to zero in probability the precise conclusion
is \(\dim E/n\to1\) in probability. For the stated half-rank consequence,
intersect the simultaneous rank event with
\(\{\eta^2\le c_k/4\}\); no independence is needed.

Here is the exact metric-to-storage implication when the rank is not quite
\(n\). If restriction to the selected coordinate set \(I\) were not
injective on \(E\), some nonzero \(u\in E\) would satisfy \(u_I=0\).
The required metric identity would then give

\[
 0=u_I^\top M u_I=\frac{\|u\|_2^2}{n}>0,
\]

a contradiction. Thus \(|I|\ge\dim E\), without needing any extra
property of \(M\). The explicitly stored selected first matrix alone
costs at least \(d\dim E\ge nd/2\). The unchanged headline bound is
\(O(d^2)\) along this family, as proved in the parent note, and
\(nd/d^2\to\infty\).

This closes a potential loophole: replacing the source tolerance \(1/n\)
by a weaker tolerance such as \(n^{-1/2}\) times any fixed power of
\(\log(en)\), or times \(e^{C\sqrt{\log(en)}}\) for fixed \(C\),
does not remove this obstruction. Each such tolerance still tends to zero.
For example, the existing transfer bound certifies an output-error target
\(Y/(\sqrt n[\log(en)]^3)\) by choosing a source tolerance proportional to
\[
 \frac{1}{\sqrt n[\log(en)]^3
       (1+\sqrt{\log(en)})e^{\sqrt{\log(en)}}},
\]
with a fixed proportionality constant on the displayed family. That
tolerance tends to zero too. Thus weakening the paper's absolute \(Y/n\)
target to this less demanding vanishing target does not fix the
polynomial-dimension threshold. This example illustrates the source
certificate; it does not assert a uniform growing-dimension lower bound
for actual dense variability.

This conclusion still concerns **certifying the current uniform-source
construction**. Good output accuracy does not logically require good
coordinatewise source accuracy for an arbitrary algorithm. A different
output-sensitive source criterion could evade the argument; no claim about
its existence or storage is made here. Nor does this corollary establish an
unavoidable exponential sample/gap threshold when dimension is held fixed.
