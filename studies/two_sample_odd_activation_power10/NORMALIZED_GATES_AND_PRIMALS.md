# Exact normalization and polynomial primal inputs

2026-09-07. Component derivation, awaiting independent audit. This does
not by itself prove the exponent-ten theorem.

## 1. Exact transformed finite and population feature equations

Fold labels using oddness as in the existing theorem. Both controls in
feature time s are 1/2. Write
\[
v=(1+\rho_{\rm folded})/2,\quad r=\sqrt v,\quad
u=\sqrt{1-v},\quad S=\operatorname{diag}(r,u),\quad
Q=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
Both r,u are at least \(\sqrt{\delta/2}\). Here S is a two-by-two
sample matrix, not an interval length. Let \(e_+=(1,0)^T\),
\(\lambda=a^3r\), and \(t=\lambda s\). Matrices acting on neurons
commute with the displayed sample matrices.

For layer \(\ell=1,2,3\) define normalized preactivations, features,
backward fields and incoming backward fields by
\[
z^\ell=a^{\ell-1}Q^{-1}Sx^\ell,\qquad
h^\ell=a^\ell Q^{-1}S\widehat h^\ell,
\]
\[
\delta^\ell=a^{4-\ell}rQ^{-1}S^{-1}d^\ell,\qquad
q^\ell=a^{3-\ell}rQ^{-1}S^{-1}\widehat q^\ell.
\tag{1}
\]
The readout remains C. The actual cap acts in the original sample
coordinates inside the definitions below.

Put A=W2, B=W3. The equations are exactly
\[
x^2=A\widehat h^1,\quad x^3=B\widehat h^2,\qquad
\widehat q^3=Ce_+,\quad \widehat q^2=B^*d^3,\quad
\widehat q^1=A^*d^2,
\]
\[
\partial_t x^1=d^1,\quad
\partial_t A=\sum_{\alpha=+,-}d_\alpha^2\otimes
                  \widehat h_\alpha^1,\quad
\partial_t B=\sum_{\alpha=+,-}d_\alpha^3\otimes
                  \widehat h_\alpha^2,\quad
\partial_t C=\widehat h_+^3.                         \tag{2}
\]
These equations hold at the finite level and on the common population
actions; the finite cap/Euler program uses its own transformed mesh.
They are a change of coordinates and time for the same feature field.

For example, the first projected covariance is S^2, so its normalized
s-derivative is \(S Q\delta^1=\lambda d^1\).
Moreover
\(\tfrac12\sum_i\delta_i^\ell\otimes h_i^{\ell-1}
=\sum_\alpha(Q\delta^\ell)_\alpha\otimes
(Qh^{\ell-1})_\alpha
=\lambda\sum_\alpha d^\ell_\alpha\otimes
\widehat h^{\ell-1}_\alpha\).
The readout derivative is \(h_+^3=\lambda\widehat h_+^3\).
This verifies all factors in (2).

For affine activation, \(\widehat h^\ell=x^\ell\) and
\(d^\ell=\widehat q^\ell\). The normalized active equations are exactly
the homogeneous four-component system in the earlier polynomial
proof. The normalized inactive first root has variance one and its
reference fields are frozen, as in the original inactive-field lemma.

## 2. The normalized nonlinear maps and their derivatives

The forward map is
\[
\mathcal H_\ell(x)
=a^{-\ell}S^{-1}Q
 \phi_{a,e}(a^{\ell-1}Q^{-1}Sx)=x+\mathcal R_\ell(x).
\tag{3}
\]
The capped backward map is
\[
\mathcal D_{\ell,R}(x,q)
=\frac{a^{\ell-4}}r SQ\,
 D_{a,e,R}(a^{\ell-1}Q^{-1}Sx,\,
                 a^{3-\ell}rQ^{-1}S^{-1}q),           \tag{4}
\]
where the original scalar capped gate is
\(D_{a,e,R}(z,q)=aq+e(1+z^2)^{-1}\tau_R(q)\).
All scalar functions in (3)--(4) act on the two sample coordinates.
The caps satisfy \(|\tau_R(q)|\le|q|\), \(|\tau_R'|\le1\).

Use the Euclidean sample norm and its operator norm. The identities
\(\|Q\|=1/\sqrt2\), \(\|Q^{-1}\|=\sqrt2\), the bounds
\(\|S\|\le1\), \(\|S^{-1}\|\le\sqrt{2/\delta}\), and
\(1/2\le a\le1\) give the following simultaneous bounds with
\(\varepsilon=64e/\sqrt\delta\):
\[
|\mathcal R_\ell(x)|\le\varepsilon,\qquad
\|D\mathcal H_\ell(x)-I\|\le\varepsilon,
\]
\[
|\mathcal D_{\ell,R}(x,q)-q|\le\varepsilon|q|,\quad
\|\partial_q\mathcal D_{\ell,R}-I\|\le\varepsilon,\quad
\|\partial_x\mathcal D_{\ell,R}\|\le\varepsilon|q|.
\tag{5}
\]
These estimates are uniform in the cap.

For detail, the first bound is at most
\(e a^{-\ell}(\pi/\sqrt2)\|S^{-1}\|\).
The two gate-derivative deviations have norm at most
\((e/a)\|S\|\|S^{-1}\|\).
Writing \(g(z)=(1+z^2)^{-1}\), the last derivative has prefactor
\(e a^{2\ell-5}/r\) times
\(SQ\operatorname{diag}(g'(z)\tau_R(q_{\rm raw}))Q^{-1}S\).
Since \(|g'|\le1\) and
\(|q_{\rm raw}|\le\sqrt2 a^{3-\ell}r\|S^{-1}\||q|\),
its norm is at most
\(\sqrt2 e a^{\ell-2}\|S\|^2\|S^{-1}\||q|\).
Each displayed elementary bound is below (5). There is no lost
inverse r in addition to the one condition-number factor.

## 3. Primal and learned-moment differences

Set \(M=24^{1/4}\delta^{-1/8}\). Absolute constants below may depend
on the fixed numerical constants of the earlier affine comparison,
but never on data, delta, gain, cap, mesh or horizon. In particular
\(\varepsilon\le C e M^4\), the normalized affine interval has
length less than two, and
\[
\|A\|,\|B\|,\|C\|,\|x^1\|_2\le CM
\tag{6}
\]
on the radius-one tube. Assume the old cap-uniform primal comparison
has been closed, so its raw discrepancy is \(E\le C e M^{12}\).
This premise holds under the earlier \(e\le c\delta^{7/4}\) restriction.

The normalized first-coordinate discrepancy is at most \(\sqrt2 E\),
not \(E/\sqrt\delta\). Indeed its two components are the raw first
weight paired with
\((x_1+x_2)/(2r)\) and \((x_1-x_2)/(2u)\), respectively.
These are orthogonal RMS-unit inputs, so each is a contraction
from the raw first-weight metric. Thus no conditioning loss is
incurred in comparing normalized first roots.

For sufficiently small \(\varepsilon\), (2), (5), (6) imply
\[
\|\widehat h^1\|_2,\|d^3\|_2\le CM,\qquad
\|\widehat h^2\|_2,\|d^2\|_2\le CM^2,\qquad
\|x^3\|_2,\|\widehat q^1\|_2\le CM^3.                 \tag{7}
\]
Here \(\widehat q^3=Ce_+\) is exact. The top backward perturbation
therefore costs \(\varepsilon\|C\|\), without applying an inverse
input variance to the readout discrepancy.

Let a subscript 0 denote the affine companion. Direct substitution
gives
\[
\|\widehat h^1-\widehat h^1_0\|_2
       \le C(E+\varepsilon)\le C eM^{12},
\]
\[
\|d^3-d^3_0\|_2\le C(E+\varepsilon M)\le CeM^{12},
\]
\[
\|\widehat h^2-\widehat h^2_0\|_2+
 \|d^2-d^2_0\|_2
       \le C(ME+\varepsilon M^2)\le CeM^{13}.          \tag{8}
\]
For instance \(x^2=A\widehat h^1\), so its discrepancy is bounded by
\(\|A-A_0\|\|\widehat h^1\|_2+
\|A_0\|\|\widehat h^1-\widehat h^1_0\|_2\).
The equation \(\widehat q^2=B^*d^3\) is identical in form.
Adding the errors in (5) gives (8).

All normalized learned moments in the exact source equations are
time-weighted inner products of the four fields in (7). The elementary
inner-product difference identity and (8) therefore give, at each
strict source time j,
\[
|\Delta M_{A2,kj}|,\ |\Delta M_{B3,kj}|
       \le C e M^{13}\Delta t_j,
\qquad
|\Delta M_{A3,kj}|,\ |\Delta M_{B2,kj}|
       \le C e M^{15}\Delta t_j.                    \tag{9}
\]
Fixed sample-basis factors are absorbed by C. A time-row sum costs
only the normalized duration, at most two. Gaussian sources for the
initialized actions have standard deviations bounded by \(CM^2\):
their variances are the corresponding primal query second moments.
This assertion concerns Gaussian source variables, not arbitrary
Lp continuity of the initialized actions.

The deterministic coefficient arrays commute with sample exchange
at every fixed cap and mesh. One may conjugate all input data by the
orthogonal map exchanging x1 and x2; the Gaussian initialization law,
both controls and scalar coordinate maps are invariant. The finite
program limiting contractions, including named formal response
derivatives, consequently commute with exchange. In the Q basis
the actual deterministic arrays and learned moments are diagonal
in the two sample sectors. Random coordinate gates need not be
diagonal. This construction fact imposes no symmetry assumption on
the competitors in the separate physical uniqueness argument.
