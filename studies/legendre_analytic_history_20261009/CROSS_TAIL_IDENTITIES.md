# Cross-tail identities for the original Legendre histories

This root calculation continues the original-method order question on
2026-10-10. It uses the projection identities in the current
`paper/compact_legendre.tex`. The result in this note is an approximation
identity and estimate, not by itself a lower bound on neural predictions.
All notation here is local. These formulas were supplied to the separate
actual-output route after that route independently identified a possible
fifth-power cross-tail term.

## Exact accumulated defect

Let \(\Pi_q^A\) denote degree-below-\(q\) orthogonal projection on
\([0,A]\), and let \(Q_q^A=I-\Pi_q^A\). For the original forward
and normalized backward histories \(h,b\), the primitive of the hidden
matrix defect is exactly

\[
 \int_0^t\mathcal E_\ell(s)\,ds
 =\frac2{mn}\sum_a\int_0^{\tau(t)}
      (Q_q^{\tau(t)}b_a)(\xi)
      (Q_q^{\tau(t)}h_a)(\xi)^\top\,d\xi.
\]

To verify it, subtract the projected bilinear pairing from the full
pairing. Orthogonality removes both mixed terms, leaving the displayed
cross-tail. Differentiating the difference with respect to the upper
clock endpoint gives the product of the two endpoint errors, by the
paper's projection-growth identity polarized between the histories.
Both sides vanish initially because the backward prefix is zero. This
identity preserves cancellation lost by integrating the absolute defect.

## A scalar identity with no infinite tail sum

Fix \(A>1\), let \(u(\xi)=(\xi-1)_+\), and put \(v=u^2\).
For \(j\ge0\), define the scalar moment

\[
 I_j(A)=\int_1^A(\xi-1)P_j(2\xi/A-1)\,d\xi.
\]

Then for every \(q\ge1\),

\[
 \int_0^A Q_q^Au\,Q_q^Av\,d\xi=I_q(A)I_{q-1}(A).
\tag{1}
\]

Indeed \(v'=2u\). Orthogonality and the fact that
\((\Pi_q^Av)'\) has degree below \(q\) give

\[
 \int Q_q^Au\,Q_q^Av
 =\tfrac12\int v'Q_q^Av
 =\tfrac14\big[(Q_q^Av)(A)^2-(Q_q^Av)(0)^2\big].
\]

The endpoint kernels, integrated once by parts, give

\[
 (Q_q^Av)(A)=I_q+I_{q-1},\qquad
 (Q_q^Av)(0)=(-1)^{q+1}(I_q-I_{q-1}).
\]

Their squared difference is \(4I_qI_{q-1}\), proving (1), including
\(q=1\). No sign has been discarded.

## Interior asymptotic and its proof

Put \(\alpha=2/A-1=\cos\theta\). On any fixed compact interval
of \(A\)'s strictly inside \((1,\infty)\), \(\theta\) stays in
a compact subset of \((0,\pi)\). For \(j\ge2\), integrating the
Legendre derivative recurrence twice gives

\[
 I_j(A)=\frac{A^2}{4(2j+1)}
 \left[
 \frac{P_{j+2}(\alpha)-P_j(\alpha)}{2j+3}
 -\frac{P_j(\alpha)-P_{j-2}(\alpha)}{2j-1}
 \right].
\tag{2}
\]

There are no endpoint terms at one because each difference of Legendre
polynomials vanishes there. The classical interior formula is

\[
 P_j(\cos\theta)
 =\sqrt{\frac{2}{\pi j\sin\theta}}
 \cos\big((j+\tfrac12)\theta-\tfrac\pi4\big)
 +O(j^{-3/2}),
\tag{3}
\]

uniform on the indicated compact set. This is the \(\alpha=\beta=0\)
specialization of [NIST DLMF 18.15.4_5](https://dlmf.nist.gov/18.15.E4_5).
It also follows directly from the integral representation already proved
in the current paper, as follows. Near \(\psi=0\),

\[
 \cos\theta+i\sin\theta\cos\psi
 =e^{i\theta}\left[1-\tfrac12a\psi^2+O(\psi^4)\right],
 \quad a=\sin^2\theta+i\sin\theta\cos\theta.
\]

Here \(\operatorname{Re}a\) has a fixed positive lower bound. The
endpoint integral of its \(j\)-th power is
\(e^{ij\theta}\sqrt{\pi/(2j)}a^{-1/2}+O(j^{-3/2})\).
To control the error, split at \(\psi=j^{-2/5}\), use the exponential
bound outside this interval, and bound the Taylor error inside by
\(Cj\int_0^\infty\psi^4e^{-cj\psi^2}d\psi=O(j^{-3/2})\).
The other endpoint is the complex conjugate; the middle is exponentially
small because the modulus squared is
\(1-\sin^2\theta\sin^2\psi\). Dividing their sum by \(\pi\)
and using
\(a=\sin\theta\exp(i(\pi/2-\theta))\) proves (3).

Substitute (3) at the five indices in (2). The leading centered second
difference of cosines is \(-4\sin^2\theta\) times the central
cosine. All coefficient changes and remainders cost \(O(j^{-7/2})\).
Thus

\[
 I_j(A)=-\frac{A^2}{4}\sqrt{\frac2\pi}
       (\sin\theta)^{3/2}j^{-5/2}
       \cos\big((j+\tfrac12)\theta-\tfrac\pi4\big)
       +O(j^{-7/2}).
\tag{4}
\]

Multiplying the two consecutive moments in (1) yields

\[
 \int_0^A Q_q^Au\,Q_q^Av
 =\frac{A(A-1)^{3/2}}{2\pi q^5}
       \big[\cos\theta+\sin(2q\theta)\big]+O(q^{-6}).
\tag{5}
\]

The error in (5) is uniform on every such fixed compact interval of
\(A\)'s. Its oscillatory coefficient is nonzero. This rules out
improving this scalar pairing to \(o(q^{-5})\) uniformly over such
nondegenerate intervals. No lower bound at every individual endpoint is
asserted (for example, the scalar pairing vanishes at \(A=2\) for
\(q\ge3\)). It does not yet transfer that conclusion to a neural output.

## Uniform bounds including the prefix join

For an integer \(k\ge0\) and \(j>k\), repeated integration by
parts gives

\[
 \int_\alpha^1(x-\alpha)^kP_j(x)\,dx
 =\frac{k!(1-\alpha^2)^{k+1}P_j^{(k+1)}(\alpha)}
        {(j-k)(j-k+1)\cdots(j+k+1)}.
\tag{6}
\]

For example, its first two cases follow from the Legendre equation and
one further integration; the general case follows from Rodrigues'
formula after \(k+1\) integrations. All boundary terms at one vanish
before the last integration, and the zero at \(x=\alpha\) leaves
precisely the indicated derivative and factorial.

The energy estimate in the paper bounds \(P_j\) and its first
angular derivative. In the region \(\sin\theta\ge1/j\) it gives

\[
 |P_j^{(r)}(\cos\theta)|
 \le C_r j^{r-1/2}(\sin\theta)^{-r-1/2}
 \quad(r\text{ fixed}).
\tag{7}
\]

For \(r=0,1\) this is exactly the energy bound, converting the first
angular derivative by division by \(\sin\theta\). For larger
\(r\), differentiate the Legendre equation and use

\[
 (1-x^2)P_j^{(r+2)}
 =2(r+1)xP_j^{(r+1)}
   -[j(j+1)-r(r+1)]P_j^{(r)}.
\]

The induction uses \(1/(j\sin\theta)\le1\). In the remaining
endpoint region, the elementary derivative bound
\(|P_j^{(r)}|\le P_j^{(r)}(1)\le C_rj^{2r}\) suffices.
Inserting these two bounds into (6), with the factor \((A/2)^{k+1}\)
from the change of variable, proves

\[
 \left|\int_1^A(\xi-1)^kP_j(2\xi/A-1)d\xi\right|
 \le C_{k,A_2}j^{-k-3/2}
 \qquad(1\le A\le A_2, k\ge1).
\tag{8}
\]

In the small-angle region the stronger bound is \(Cj^{-2k-2}\),
which implies (8). The finitely many small indices are absorbed into the
constant. Orthogonality now gives the uniform tails

\[
 \|Q_q^A(\xi-1)_+^k\|_{L^2([0,A])}
 \le C_{k,A_2}q^{-k-1/2}\quad(k\ge1).
\tag{9}
\]

In particular, the ramp/quadratic pairing is uniformly \(O(q^{-5})\)
by its exact product (1), not merely \(O(q^{-4})\) from multiplying
their tail norms. The pairs of orders \((2,2)\) and \((1,3)\) are
also \(O(q^{-5})\) by (9). These uniform bounds include the shrinking
initial interval and are suitable for a Volterra stability argument.
