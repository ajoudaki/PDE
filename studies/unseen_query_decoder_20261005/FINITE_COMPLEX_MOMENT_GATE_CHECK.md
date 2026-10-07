# Bounded independent check of the finite complex-moment gate

2026-10-07. **PASS for the stated conditional Gaussian lemma and its
explicit radius cost.** No mathematical repair is required in the assigned
candidate. This is a bounded independent check, not a source-event theorem,
full-decoder review, or promotion.

The checked candidate is `FINITE_COMPLEX_MOMENT_GATE.md`, SHA-256
`04e428c5d31b56ebd05c10535fbb7cf394475e169958dd96a2cae8c05f756bb0`.
For every individual integer width \(n\ge1\), moment order \(p\ge1\),
and autonomous cavity whose coefficient paths satisfy the stated bounds,
the omitted Gaussian root obeys the candidate's exponential-moment
inequality. The same conclusion holds for the sample RMS of these
corrections. This uniform deterministic implication does not assert one
probability-one event across independent networks of every width.

The proof architecture is sound: condition on retained initialization;
bound the two-dimensional coefficient process by chaining and Gaussian
concentration; recover the source derivative estimate without a large-width
logarithmic simplification; then shrink the time radius by \(1/p\).
That last step pays for the growing moment order explicitly in the
numerical patch count.

## 1. Conditional roots and the rectangular Gaussian estimate

Let \(G\sim N(0,I)\) be independent of the retained cavity initialization.
After conditioning on that initialization, let \(b_z\) be the deterministic
complex coefficient difference on a time rectangle with side lengths at
most \(H\), with
\[
\sup_z\|b_z\|_2\le D,\qquad
\|b_z-b_{z'}\|_2\le K\|z-z'\|_2.
\]
Write \(X=\sup_z|G^\top b_z|\). The candidate's choice
\(M=256D\sqrt{\log(e+HK/D)}\) is more than sufficient.

For a direct constants check when \(D,K>0\), use rectangular grids with
spacing at most \((D/K)2^{-j}\). Their sizes can be bounded by
\(N_j\le4(1+HK/D)^2 4^j\); attaching to a nearest point on the previous
grid gives increment standard deviation at most \(3D2^{-j}\).
Put \(v=\log(e+HK/D)\ge1\). Then
\[
\log(2N_j)\le5v+2j.
\]
The elementary Gaussian maximum bound therefore yields for real
coefficients
\[
\mathbb E\sup_z|G^\top b_z|
\le D\sqrt{10v}
 +3D\sum_{j\ge1}2^{-j}(\sqrt{10v}+2\sqrt j)
\le(4\sqrt{10}+12)D\sqrt v<128D\sqrt v.
\]
Continuity of the coefficient map justifies the grid limit. Applying this
to real and imaginary parts proves the displayed value of \(M\).
If \(K=0\), the process is constant in its index and the bound follows
directly from the one-point Gaussian bound. If \(D=0\), the process
vanishes.

The absolute supremum is at most \(2D\)-Lipschitz as a function of the
standard real root. The Gaussian semigroup argument in
`EXPLICIT_FITTING_WIDTH.md`, Section 2, consequently gives
\[
\log\mathbb E e^{uX}\le uM+2u^2D^2\quad(u\ge0).
\]
The candidate's constant is conservative; no complex Gaussian root is
substituted for the actual real root.

For sample corrections \(X_a\) sharing this same root, define
\(\bar X=(m^{-1}\sum_aX_a^2)^{1/2}\). The reverse triangle inequality
for this normalized Euclidean norm makes \(\bar X\) at most
\(2D\)-Lipschitz. Moreover,
\[
\mathbb E\bar X\le
\left(m^{-1}\sum_a\mathbb E X_a^2\right)^{1/2}
\le\sqrt{M^2+4D^2}\le M+2D.
\]
Thus the claimed RMS moment bound follows without independence between
samples and without a sample-count factor.

For an omitted hidden row or column with law \(N(0,I/n)\), write it as
\(G/\sqrt n\). Its pairing uses coefficient vector \(b_z/\sqrt n\),
so the required norm is precisely \(\|b_z\|_2/\sqrt n\). A rectangular
cavity retaining fewer than \(n\) coordinates keeps the original divisor
\(n\). The first-layer forward root has law \(N(0,I_d)\), but its
coefficient is the fixed real input, so its complex-minus-real correction
is identically zero. At the top there is no outgoing root. Neither endpoint
introduces a missing covariance factor.

## 2. The all-width budget bracket and derivative scale

Use the candidate's unchanged quantities
\[
\lambda=\gamma/m>0,\quad Y=\|y\|_2/\sqrt m>0,\quad
S=16Y/\lambda,\quad \ell=\log(en)\ge1,
\]
and the source constants
\[
\mathcal B=1024e^2L,\qquad
\Lambda=\log(e+\mathcal B)+\log(1/\eta).
\]
The original label allowance includes \(\eta\le1\) and
\(S^2\Lambda/\eta\le1\); no stronger cap is needed here.

To distinguish the interpolation exponent from the integer moment order,
write \(q=\max\{4,\log(2\mathcal B\ell)\}\). Then
\[
(2\mathcal B\ell)^{1/q}\le e,
\qquad q\le4+\log(2\mathcal B)+\log\ell.
\]
This is valid at \(n=1\). Substitution into the source's Hölder estimate
gives the candidate's bracket
\[
A=1+\frac{S^2}{\eta}
       [4+\log(2\mathcal B)+\log\ell].
\]
For example, \(\log(2\mathcal B)\le\Lambda+\log2\) and
\(\Lambda\ge1\) give directly
\[
A\le2+\frac{4+\log2+\log\ell}{\Lambda}
\le7+\log\ell
\le8[1+\log(e+\ell)].
\]
Consequently \(A\le16\log(e+\ell)\). No depth factor has been discarded
inside this logarithm, and no eventual-width assumption is required.

The derivative recurrence is inherited with the correct readout,
changed-mixer, and changed-gate terms. The assigned source ledger gives
\(H_j\le\beta^{3L}\), \(k_j\le\beta^{5L}\), and the finite-query
response envelope \(U_{\rm fin}\le\beta^{72L}\). The other response
coefficient in \(N_*\) is smaller: the source definitions give
\(g\le\beta^{10L}\), \(r_j=P_jg\le\beta^{13L}\), and
\(q_j=f_jg\le\beta^{14L}\). Thus \(N_*\le\beta^{72L}\).
Each forcing term is bounded by \(\beta^{75L}\), propagation contributes
at most \(\beta^{2L}\), and the layer sum contributes at most
\(\beta^L\). Hence \(J=\beta^{80L}\) covers the backward and forward
derivative constants, with slack for the numerical factors.

On the short complex pieces, \(\rho\le2Y\). After dividing the backward
coefficient by \(S\), its derivative scale is bounded by
\(2YJ A/S=(\lambda/8)J A\). The forward derivative scale is bounded
by \(4YS\max_jq_j\), with \(4YS=\lambda S^2/4\le\lambda/4\).
The nearest-real-anchor map is nonexpansive, also at the endpoints.
Integrating at most two short pieces and bounding the coefficient
difference's Lipschitz constant therefore gives the safe candidate values
\[
D=\frac{\lambda cJA}{\sqrt\ell},\qquad
K=\lambda JA,\qquad
H=\frac{64\ell}{\lambda}+\frac{4c}{\sqrt\ell}.
\]
These remain a conditional assertion about the stopped or clamped cavity
paths. The note correctly requires the derivative bounds after its own
clamping; arbitrary root-dependent stopping would not justify them or the
conditional Gaussian law.

## 3. Finite-order constants and the physical-time dependence

Take exactly
\[
c=[p\beta^{100L}(1+\lambda)]^{-1},\qquad r=\lambda^{-1}.
\]
Then
\[
D=\frac{\beta^{-20L}A}{p(1+r)\sqrt\ell},\qquad
\frac{HK}{D}=64p\beta^{100L}(1+r)\ell^{3/2}+4.
\]
The factor \((1+r)^{-1}\), including its behavior for arbitrarily small
\(\lambda\), is retained correctly.

Writing \(v=\log\ell\ge0\), the bounds
\((2+v)e^{-v/2}\le2\) and
\((2+v)^{3/2}e^{-v/2}\le4\) imply
\[
D\le32\beta^{-20L}/p.
\]
The entropy logarithm is bounded by
\(6+100L\log\beta+\log p+\log(1+r)+2\log(e+\ell)\).
Splitting its square root and retaining the denominators yields, before
multiplication by 256, the candidate's valid upper bound
\[
\beta^{-20L}
\{32(\sqrt6+\beta^{2L}+1+1)+64\sqrt2\}.
\]
Here \(\sqrt{\log p}/p\le1\),
\(\sqrt{\log(1+r)}/(1+r)\le1\), and
\(\sqrt{100L\log\beta}\le\beta^{2L}\). Since
\(\beta^{2L}\ge10^4\), restoring 256 and the additional \(2D\)
indeed gives
\[
M+2D\le2^{16}\beta^{-18L}.
\]

For either the individual or RMS correction, applying the Gaussian moment
bound at \(u=ap\) and taking the \(p\)-th root gives
\[
\frac1p\log\mathbb E e^{apX}
\le a2^{16}\beta^{-18L}
     +2^{11}a^2\beta^{-40L}/p
\le\beta^{-10L}\qquad(0\le a\le8).
\]
At the worst permitted values \(\beta=10,L=2,p=1\), division by
\(\beta^{-10L}\) bounds the two terms by
\(2^{19}10^{-16}\) and \(2^{17}10^{-60}\), respectively. Their sum
is less than one. Larger allowed parameters preserve the inequality.
This checks the stated numerical constant and every finite moment order;
no limit \(n\to\infty\) is used.

## 4. Radius cost and remaining conditions

The normalized radius is correctly
\[
r_\tau=\lambda r_t
 =[p\beta^{100L}(1+m/\gamma)\sqrt\ell]^{-1}.
\]
The previous certified Taylor step was at most
\(h_0=[64\beta^{100L}(1+m/\gamma)\sqrt\ell]^{-1}\).
Using \(h_0/p\) fits the new radius with the same margin. For fixed horizon
\(T\), integer \(p\) gives
\[
\left\lceil pT/h_0\right\rceil
\le p\left\lceil T/h_0\right\rceil.
\]
If the optional small-label refinement already uses a finer equal
partition, subdividing its intervals into \(p\) pieces gives the same
bound. The degree term depending on the patch count is logarithmic, so it
increases by at most a numerical multiple of \(\log p\), allowing for
integer ceilings. Any resulting precision and final resource formulas
must be recomposed, as the candidate explicitly states.

The displayed confidence-order choice of \(p\) is logarithmic in
\(mL/\delta\). It does not itself establish a success probability:
finite-width local insertion, common-cavity comparison, their exceptional
probabilities, and passive-decoder error absorption remain unproved by
this lemma. Failed own initializations may be assigned zero reference
paths before integrating the omitted root. Conditioning on full-network
survival would invalidate the proof and is explicitly excluded.

## 5. Input boundary and provenance

Complete scientific inputs read were the candidate and the following
authorized files. References in these inputs were not followed to other
scientific files, study history, or reviews. The required canonical-notation
skill, its neural-network reference, and the rigorous-proof skill were
read. No experiment, external theorem lookup, Git mutation, candidate edit,
or maintained-book/code change was performed. The only write is this report.

| Input | SHA-256 |
|---|---|
| `POLYNOMIAL_SOURCE_WIDTH.md` | `352b98adf16e57f7844cb75d0ec4622e897b56ba9ac44527cc0141448443ad22` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `EXPLICIT_FITTING_WIDTH.md` | `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d` |
| `../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md` | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |
| `../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md` | `f3e277e9591be6e48357a13217927c05bcc2c59843a26a3fa5423ae5afc4c7d8` |
