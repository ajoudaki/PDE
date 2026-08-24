# Hostile audit of the passive multi-cavity closure

**Date:** 23 August 2026.

**Verdict:** rejected.  The characteristic cancellation and one conditional
collision count are correct, but the proposed proof assumes its main
propagator estimate, misses an order-one self-return, and does not close the
weighted or nonlinear moment hierarchy.  Nothing in this audit is a
counterexample to the canonical iid-Gaussian conjecture.

## 1. Exact finite-difference characteristic

Let \(\epsilon=n^{-1/2}\), \(d(z)=(1+z^2)^{-1}\),
\(\lambda=d'/d\), and \(\Theta(z)=z+z^3/3\).  For

\[
z=\bar z+\epsilon Z,\quad y=\bar y+\epsilon Y,\quad
\kappa=\bar\kappa+\epsilon K,\quad
B=\bar B+\epsilon P,
\]

put

\[
\Psi=\epsilon^{-1}\{\Theta(z)-\Theta(\bar z)\}
     =(1+\bar z^2)Z+\epsilon\bar zZ^2+
       \frac{\epsilon^2}{3}Z^3.
\]

If \(z'=\kappa B d(z)+y\), direct expansion gives

\[
\begin{aligned}
\Psi'={}&\bar\kappa P+K\bar B+\frac{Y}{d(\bar z)}
 -\lambda(\bar z)\bar y\Psi\\
&+\epsilon\left[
 KP+\bar y\frac{1-\bar z^2}{1+\bar z^2}Z^2
 +2\bar zYZ\right]\\
&+\epsilon^2\left[
 YZ^2-\frac{2\bar y\bar z}{3(1+\bar z^2)}Z^3\right].
\end{aligned}                                           \tag{1.1}
\]

Thus the direct \(\bar\kappa\bar B d'Z\) term cancels exactly, and the
quadratic/cubic remainders really carry \(n^{-1/2}\) and \(n^{-1}\).
Their probabilistic smallness does not follow algebraically: their
coefficients contain \(\bar z,Y,\bar y\).

## 2. The first circular assertion

The rejected proof postulated conditional lognormal moments for a tagged
propagator \(L_v\), of schematic form

\[
 \mathbb E\prod_v L_v^{m_v}
 \le \exp\!\left(C\sum_vm_v^2\right).                  \tag{2.1}
\]

To obtain (2.1) by Gaussian concentration one needs a deterministic
conditional Lipschitz bound for the private Gaussian block.  Differentiating
that map produces exactly the first-variation system being estimated.  At
the middle layer it includes

\[
 (D\kappa_2)B_2=(D\kappa_2)d_2R_2,
 \qquad d_2^{-1}D y_2,
\]

with

\[
 y_2=\Gamma_1D_1^2\Gamma_1^{\mathsf T}b_2.
\]

The first term already needs weighted moments of the target \(R_2\); the
second is an adapted Wishart transport, not a fresh Gaussian projection.
Calling either an endpoint factor assumes the desired estimate.

## 3. Passive tags omit an order-one return

For a tagged middle row \(v\), write

\[
 q_{1,i}=q_{1,i}^{(-v)}+\Gamma_{1,vi}b_{2,v}.
\]

Then

\[
 y_{2,v}=\sum_i\Gamma_{1,vi}d(u_i)^2q_{1,i}^{(-v)}
           +\chi_vb_{2,v},
 \qquad
 \chi_v=\sum_i\Gamma_{1,vi}^2d(u_i)^2.                \tag{3.1}
\]

Since \(\Gamma_{1,vi}=n^{-1/2}W_{vi}\), \(\chi_v\) is order one and at
initialization converges to \(\mathbb E(1+U^2)^{-2}>0\).  A passive shadow
that does not feed into the common environment omits (3.1).  Division by the
arctan gate does not erase it:

\[
 \frac{\chi_vb_{2,v}}{d_{2,v}}=\chi_vR_{2,v}.
\]

A valid dressed cavity must retain this return and resum all repeated
tag--environment--tag walks into a tag-specific Volterra self-energy.  No
stability or moment estimate for that dressed resolvent was proved.

## 4. What collision counting really proves

Conditional on (2.1), expansion of
\((n^{-1}\sum_vL_v^2)^q\) by collision number \(k\) does give

\[
 \mathbb E\left(n^{-1}\sum_vL_v^2\right)^q
 \le e^{Cq}\sum_{k=0}^{q-1}
       \left(\frac{q^2e^{Cq}}n\right)^k,               \tag{4.1}
\]

for sufficiently small \(q\le c\log n\).  This is a valid combinatorial
implication, but its premise is the circular step above.  Moreover, cross-tag
returns are \(O(n^{-1/2})\) only after every diagonal return has been dressed;
the passive construction failed already at the first Picard level.

## 5. Weighted and nonlinear closure is still missing

The flow needs weighted quantities such as

\[
 \left(n^{-1}\sum_vR_{2,v}^2L_v^2\right)^{1/2},
\]

not merely the unweighted norm in (4.1).  Normalized \(L^2\) is not closed
under coordinatewise multiplication: for
\(a=b=\sqrt n e_1\), \(\|a\|_n=\|b\|_n=1\) but
\(\|ab\|_n=\sqrt n\).  Ordinary Hölder also sends quadratic and cubic terms
in (1.1) to moment orders \(2p\) and \(3p\).  No joint hierarchy preventing
an indefinite escalation of moment order was supplied.

Own-row independence does not fill this gap.  If each cavity weight may
depend on all other rows, the family is not jointly conditionally
independent; a leave-own-coordinate scalar Gaussian example produces a
\(\sqrt{\log n}\) loss in the proposed square-summed inequality.  Any valid
cavity must remove the full private block, including \(A_{0,i}\), and prove a
joint block-decoupling estimate for the base state and its first tangent.

## 6. Surviving exact endpoint reduction

For \(g_j=\Gamma_2(0)e_j\), exact integration gives

\[
 R_{2,j}(t)=g_j^{\mathsf T}b_3(t)
 +\int_0^t x_{2,j}(s)
   \langle b_3(s),b_3(t)\rangle_n\,ds.                 \tag{6.1}
\]

The Volterra term is bounded.  If a genuine column cavity makes
\(b_3^{(-j)}\) independent of \(g_j\), its fresh part is conditionally
Gaussian.  The replacement error obeys

\[
 \|g_j^{\mathsf T}(b_3-b_3^{(-j)})\|_{L^p}
 \le C\left\|\sqrt n\,
       \|b_3-b_3^{(-j)}\|_n\right\|_{L^{2p}},          \tag{6.2}
\]

so the normalization is correct, with a halving of the logarithmic moment
window.  The estimate on the right of (6.2) remains exactly the unproved
dressed-cavity theorem.

## 7. Revised proof frontier

The passive proof cannot be repaired by changing constants.  A viable route
must prove all three of the following without using the target tail:

1. a dressed, self-fed diagonal/Volterra resolvent with mesh-uniform moments;
2. a joint multi-block decoupling or signed nonalignment estimate for its
   off-diagonal bath and row leverage; and
3. a closed logarithmic joint-moment hierarchy for the exact finite
   differences, including their weighted \(2p/3p\) products.

Tensor Programs III still identifies every fixed finite program.  No audited
DMFT, GFOM, or AMP theorem supplies these three uniform estimates.
