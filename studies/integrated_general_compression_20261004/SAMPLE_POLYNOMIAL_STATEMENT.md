# Comparisons with polynomial sample dependence outside the width factor

2026-10-04. Continuation of the integrated general theorem, at the user's
request to remove sample/gap powers from the dense and Legendre comparison
exponents while preserving actual label dependence. This statement
supersedes the corresponding conservative envelopes in
SIMPLE_EXPLICIT_STATEMENT.md. The underlying models, activation class,
label allowance, physical time, query norm, and source probability event
are unchanged. These are internal research results, not promoted theorems.

## Setup

Use the canonical model with \(L\ge2\) hidden layers of width \(n\),
\(m\) fixed inputs \(x_a\in\mathbb R^d\) with \(\|x_a\|=\sqrt d\),
arbitrary fixed signed labels, and exactly zero initial readout.
First-weight entries have law \(N(0,1)\), hidden-mixer entries have law
\(N(0,1/n)\), independently across all blocks. The forward pass is
\[
z^{(1)}=Ax/\sqrt d,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad f=w^\top h^{(L)}/n.
\]
Train mean squared loss with block mobilities \((n,1,\ldots,1,n)\).
There is no clipping or orthogonality assumption.

Each activation is real on the real axis, holomorphic on the common
strip \(|\operatorname{Im}z|<a\), and has bounded first derivative there.
Activation values may be unbounded. Define
\[
\beta=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,\ \frac{16}{a},\
\max_{\ell,j=1,2}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell^{(j)}(z)|\right\},\qquad B=\beta^{100L}.
\]
Thus \(B\) depends on activation and depth only. Let
\[
Y=\|y\|_2/\sqrt m,\qquad
Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}),
\]
\[
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
The gap \(\gamma\) has no division by sample count.

Retain exactly the common sufficient label condition
\[
0<Y\le \frac{\gamma}{mB^{3/10}}.
\tag{1}
\]
All comparisons use unchanged physical times and
\[
\|f-g\|_*=\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
\tag{2}
\]
The fitted endpoints exist by the established-in-study physical fitting
theorems. The zero-label case is the exact zero predictor.

For compact formulas define the actual activity scale and an explicit
width factor
\[
s=\frac{Ym}{\gamma},\qquad
F_n=\left(1+Bs\sqrt{\log(en)}\right)
\left[1+Bs^2\left(e^{\sqrt{\log(en)}}-1\right)\right].
\tag{3}
\]
Both powers of \(s\) use the actual labels. At fixed width \(F_n\) is a
polynomial of degree three in \(s\). Its exponential has no data, label,
activation, depth, or confidence factor in the exponent.

For every fixed confidence \(1-\delta\), the conclusions apply at every
individual width \(n\ge N_0(\delta)\), with probability at least
\(1-\delta\). This threshold also depends on all fixed problem parameters.
Its stochastic part remains unquantified. It includes the deterministic
source construction gates. No event simultaneous over infinitely many
independently sampled widths is asserted. Confidence allocation can be
enlarged within \(N_0\) when several comparisons are wanted jointly.

## 1. Dense versus independent dense

The new bound is
\[
\|f_n-\widetilde f_n\|_*
\le BY\left(1+\frac m\gamma\right)^2 F_n
\sqrt{\frac{\log[8(n+1)(1+2n)^d/\delta]}{n}}.
\tag{4}
\]
All sample/gap dependence is polynomial outside the explicit
\(e^{\sqrt{\log(en)}}\). The label powers in (4) range from one through
four after expanding (3); the label has not been replaced by its cap.
Each dense model has \((L-1)n^2+n(d+1)\) trainable coordinates.
The rate is still \(n^{-1/2+o(1)}\), not strict root width.

The complete proof is DENSE_SAMPLE_EXPONENT_REFINEMENT.md.

## 2. Legendre closure versus its dense run

Use the original residual-RMS clock, unit forward prefix, zero backward
prefix, and the same Gaussian initialization as the dense reference.
The initialized mixers remain fixed; reconstructed physical parameters
are proof/evaluation objects, not additional learned dense matrices.

Define only for this order prescription
\[
P_n=3Bs^2\left(1+\frac m\gamma\right)F_n,\qquad
Q_n=\max\{3,P_n,n^{1/4}\sqrt{P_n}\},
\]
\[
q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil.
\tag{5}
\]
The underlying simultaneous-in-order estimate is
\[
q\ge P_n
\quad\Longrightarrow\quad
\|f_{n,q}-f_n\|_*
\le \frac{Y P_n\sqrt{\log(eq)}}{q^2}.
\tag{6}
\]
Consequently
\[
\|f_{n,q_n}-f_n\|_*\le \frac{Y}{\sqrt n}.
\tag{7}
\]
The prescription (5) introduces no additional stochastic event or
unquantified width requirement beyond the inherited source event.
All parameter dependence in its order is polynomial or logarithmic,
apart from the data-independent width factor in (3).

The moving-state count is exactly
\[
n(d+1)+1+2(L-1)mnq_n.
\tag{8}
\]
The fixed mixers additionally retain \((L-1)n^2\) entries. At fixed
positive labels and fixed problem parameters, \(P_n=n^{o(1)}\), hence
\(q_n=n^{1/4+o(1)}\) and moving storage is \(n^{5/4+o(1)}\).
The complete proof is LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md.

## 3. Compact representation: improved, but not polynomial, width threshold

The corrected-readout autonomous model and source construction are
unchanged. A sharper sufficient comparison threshold is
\[
n\ge\left\lceil\max\left\{
N_0(\delta),\
\exp\!\left[\max\left\{
8Bs\left(1+\frac m\gamma\right)
 \left(1+s\sqrt{1+\frac m\gamma}\right),\
64B^2s^4\left(1+\frac m\gamma\right)^2
 \left(1+s\sqrt{1+\frac m\gamma}\right)^2,\ 2
\right\}\right],\
\left(\frac{4B\sqrt{1+m/\gamma}}{Y}\right)^4
\right\}\right\rceil.
\tag{9}
\]
It gives
\[
\|f_C-f_n\|_*\le Y/\sqrt n.
\tag{10}
\]
Its all-retained storage remains
\[
\begin{split}
\operatorname{size}(C)\le{}&
B^{16/25+3d/50}\frac{(d+3)^d}{(d!)^2}s^4
[\log(en)]^{3d+2}\\
&+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{split}
\tag{11}
\]
This includes fixed coefficients, metrics, data, and the specified caches;
it excludes initialization-only preprocessing work and exact-real bit cost.

The comparison threshold's former polynomial gap factor
\((1+m/\gamma)^{16}/Y^4\) is reduced to
\((1+m/\gamma)^2/Y^4\). At fixed admissible activity \(s>0\), the
comparison exponential's worst large-\(m/\gamma\) growth is cubic instead
of eighth power. Actual \(Y\)-dependence remains explicit in (9).

This does not remove exponential sample/gap dependence for the compact
construction. Its current positive-coefficient comparison has an exact
inverse-gap obstruction, and a separate label-sensitive analytic-radius
gate inside \(N_0\) is also exponential. Neither is an intrinsic lower
bound for the model or for all possible proofs. Details and the exact
improved readout-projector identity are in
COMPACT_SAMPLE_EXPONENT_REFINEMENT.md.

## 4. The proof change and the role of the label restriction

The dense and Legendre improvements first retain the negative square of
the residual discrepancy in the normalized parameter energy. An exact
two-endpoint Taylor identity uses only carriers from the actual dense
trajectory, avoiding an unsupported carrier bound along interpolated
states. This removes the inverse-gap feedback loss in the old Gronwall
exponent. The remaining exponent has the form
\[
\beta^{O(L)}s+\beta^{O(L)}s^2\sqrt{\log(en)}
\]
with explicit powers smaller than \(60L\).

For \(0\le\theta\le1\), convexity gives
\[
e^{\theta u}\le1+\theta(e^u-1).
\tag{12}
\]
The existing condition (1) certifies this range for the actual coefficient
\(\theta=\beta^{36L}s^2\). Equation (12) retains \(\theta\), hence the
actual \(Y^2\), outside the exponential. This is different from replacing
\(Y\) by its maximum allowed value. It establishes a polynomial envelope
on the existing stability range; it is not a large-label theorem.

For the Legendre system, the physical forcing is controlled in integrated
norm by the exact product of moving-interval projection errors. The new
parameter energy therefore applies to the original autonomous closure,
with its actual clock and prefixes.

## 5. Requested large-width simplification

For \(m\asymp d\), \(m/\gamma\ge1\), sufficiently large \(n\), and
absolute constants \(c,C\) (also allowing the fixed comparability constants
in \(m\asymp d\)), replace \(1+m/\gamma\) by \(m/\gamma\) up to \(C\),
and \(\log(en)\) by \(\log n\). These changes require no new scaling
theorem: they are algebraic envelopes at each fixed admissible dataset.
The source gates already ensure the large-\(n\) condition needed when
replacing a logarithm raised to the growing exponent \(3d+2\).

Stirling's inequality gives
\[
\frac{(d+3)^d}{(d!)^2}
\le\frac{e^3}{2\pi d}\left(\frac{e^2}{d}\right)^d.
\]
Thus (11) implies the factorial-free storage bound
\[
\operatorname{size}(C)\le
C B^{16/25}\frac{Y^4m^3}{\gamma^4}
\left(\frac{e^2B^{3/50}}d\right)^d
(\log n)^{3d+2}+CLm^2.
\tag{13}
\]
The label size in (13) is its actual value.

## Exact remaining scope limitations

- Dense-copy strict \(C/\sqrt n\) concentration is still open.
- The success-width threshold \(N_0(\delta)\) remains unquantified and is
  not known to have polynomial dependence on sample count or geometry.
- Exponential sample/gap dependence remains in the compact construction's
  displayed comparison threshold and its separate source gate.
- No matching full-prediction or endpoint variability lower bound is added.
- Fixed positive \(Y,\gamma,B\) and (1) do not permit \(m\to\infty\);
  the fixed-data width limit must not be promoted to a joint growing-data
  theorem.

The coordinate and time guarantees retain their previous meaning.
No manuscript, maintained-book, or Git-index changes accompany this result.
