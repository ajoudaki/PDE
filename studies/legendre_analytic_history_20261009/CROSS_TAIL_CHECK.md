# Scoped check of the scalar cross-tail calculation

Date: 2026-10-10. The supervisor expanded this agent's input scope to the complete CROSS_TAIL_IDENTITIES.md after its scalar calculation was finished. This check uses that note and the already read projection identities in paper/compact_legendre.tex. It checks the scalar component independently; it does not assert an actual neural-output obstruction.

Equations (1)–(9) of the assigned note have the correct factors, signs, and powers. The estimates are uniform over the stated bounded clock interval, including \(A\downarrow1\). One wording qualification is needed: the assertion that an \(o(q^{-5})\) bound is impossible “uniformly over such intervals” requires a **nondegenerate** compact interval of endpoints. It is not a lower bound at every single fixed endpoint.

The main algebra checks are as follows.

For \(u=(\xi-1)_+\), \(v=u^2\), and \(Q=I-\Pi_q^A\), orthogonality gives

\[
\int_0^A Qu\,Qv
=\frac12\int_0^A v'Qv
=\frac14\big[(Qv)(A)^2-(Qv)(0)^2\big].
\]

The term involving \((\Pi_q^A v)'\) vanishes because it has degree below \(q\). The endpoint integral formulas are

\[
(Qv)(A)=I_q+I_{q-1},\qquad
(Qv)(0)=(-1)^{q+1}(I_q-I_{q-1}).
\]

Their squared difference is \(4I_qI_{q-1}\). This proves the exact product with no missing \(A\), factor of two, or sign. For a boundary check, at \(A=2,q=1\), direct subtraction of the constant projections gives \(1/4-1/12=1/6\), agreeing with \(I_1I_0=(1/3)(1/2)\).

In the interior asymptotic, the leading coefficients of \(I_q\) and \(I_{q-1}\) have product

\[
\frac{A^4}{8\pi}\sin^3\theta\,q^{-5}.
\]

The cosine-product identity introduces a factor \(1/2\). Its difference phase is \(\theta\), and its sum phase is \(2q\theta-\pi/2\). Since
\(\sin\theta=2\sqrt{A-1}/A\), this becomes exactly

\[
\frac{A(A-1)^{3/2}}{2\pi q^5}
\big[\cos\theta+\sin(2q\theta)\big]+O(q^{-6}).
\]

The supplied direct proof of the interior Legendre asymptotic also has the correct complex Gaussian parameter:

\[
a=\sin^2\theta+i\sin\theta\cos\theta
 =\sin\theta\,e^{i(\pi/2-\theta)}.
\]

Thus its two endpoint contributions have phase
\((j+1/2)\theta-\pi/4\). A Taylor error of size \(j\psi^4\), integrated against \(e^{-cj\psi^2}\), is \(O(j^{-3/2})\), uniformly when \(\theta\) lies in a compact subset of \((0,\pi)\). This verifies the asymptotic without needing an additional external theorem.

For the uniform estimate, equation (6) has \(2k+2\) denominator factors. In the region \(\sin\theta\ge1/j\), inserting the derivative estimate with \(r=k+1\) gives

\[
\frac{(\sin\theta)^{2k+2}
       j^{k+1/2}(\sin\theta)^{-k-3/2}}
     {j^{2k+2}}
=j^{-k-3/2}(\sin\theta)^{k+1/2}
\le j^{-k-3/2}.
\]

The derivative recurrence used for induction is correct. Its first term incurs, relative to the desired next bound, the factor \(1/(j\sin\theta)\le1\), and its second term has exactly the desired powers.

In the endpoint region, the estimate
\(|P_j^{(k+1)}|\le C_kj^{2k+2}\) instead gives
\((\sin\theta)^{2k+2}\le j^{-2k-2}\).
The elementary derivative maximum can be justified directly from the paper's nonnegative derivative expansion:
repeated differentiation writes \(P_j^{(r)}\) as a nonnegative linear combination of Legendre polynomials. Since \(|P_i(x)|\le1\), its absolute value is at most its value at one; this value is
\((j+r)!/[2^r r!(j-r)!]\) when \(j\ge r\).

Finally Parseval introduces the weight \((2j+1)/A\). Squared moment bounds therefore give a series bounded by
\(\sum_{j\ge q}j^{-2k-2}=O(q^{-2k-1})\), proving the asserted tail norm \(O(q^{-k-1/2})\). Finitely many small indices are covered by enlarging the constant. The pairs \((2,2)\) and \((1,3)\) consequently have \(O(q^{-5})\) cross-tail by Cauchy–Schwarz; the pair \((1,2)\) has the same power because of its exact product identity.

For the qualification about fixed endpoints, at \(A=2\), \(P_j(2\xi/A-1)=P_j(\xi-1)\) and

\[
I_j(2)=\int_0^1xP_j(x)\,dx.
\]

For odd \(j\ge3\), parity makes this half of \(\int_{-1}^1xP_j(x)\,dx=0\). Every consecutive pair with \(q\ge3\) therefore has \(I_q(2)I_{q-1}(2)=0\). On a nondegenerate compact interval of \(A\)'s, by contrast, the phase \(2q\theta(A)\) spans increasingly many oscillations. Choosing an endpoint where its sine is one gives a coefficient bounded away from zero, since \(1+\cos\theta\) is bounded below on that compact set. The uniform \(O(q^{-6})\) remainder then proves the claimed failure of uniform \(o(q^{-5})\).

No further scalar correction was found. The open step is the propagation of this scalar component through the actual closure histories and output map, including its nonlinear remainder.
