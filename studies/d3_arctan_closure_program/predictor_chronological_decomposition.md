# Chronological Gaussian decomposition of the endpoint predictor

This note uses only the finite-mesh causal order and the elementary
two-sided conditioning formula for a Gaussian matrix.  Its purpose is to test
whether the invariant endpoint predictor is a martingale with a useful BMO
bracket.

## 1. Alternating Gaussian filtration

Let \(\Gamma:H_x\to H_b\) be a normalized Ginibre operator.  At the beginning
of Euler query \(k\), let

\[
 E_{k-1}=\operatorname{span}\{x_0,\ldots,x_{k-1}\}\subset H_x,
 \qquad
 F_{k-1}=\operatorname{span}\{b_0,\ldots,b_{k-1}\}\subset H_b.
\]

The sigma-field \(\mathcal F_k^-\) contains the past states, the past forward
queries \(\Gamma x_\ell\), the past backward queries \(\Gamma^*b_\ell\), and
the new feature \(x_k\).  Explicit Euler causality is exactly what makes
\(x_k\) measurable before the new forward Gaussian block is revealed.

Put

\[
 \widetilde x_k=(I-P_{E_{k-1}})x_k,qquad
 \alpha_k=\|\widetilde x_k\|,qquad
 e_k=\widetilde x_k/\alpha_k
\]

when \(\alpha_k>0\); if \(\alpha_k=0\), there is no new forward query.  The
two-sided Gaussian projection formula says that, conditional on
\(\mathcal F_k^-\),

\[
 \Gamma=\widehat\Gamma_{k-1}
   +(I-P_{F_{k-1}})\,G_k\,(I-P_{E_{k-1}}),           \tag{1}
\]

where \(\widehat\Gamma_{k-1}\) is the conditional mean fixed by the old two
blocks and \(G_k\) is an independent Ginibre operator between the two
orthogonal complements.  Indeed the four blocks
\(P_F\Gamma P_E\), \(P_F\Gamma P_E^\perp\),
\(P_F^\perp\Gamma P_E\), and
\(P_F^\perp\Gamma P_E^\perp\) are jointly Gaussian and mutually orthogonal in
covariance; the first three are fixed by \(\Gamma P_E\) and
\(P_F\Gamma\), leaving only the last block.

Consequently the new forward innovation

\[
 g_k=(I-P_{F_{k-1}})G_ke_k                             \tag{2}
\]

is conditionally centered Gaussian with covariance equal to the normalized
identity on \(F_{k-1}^\perp\), and is independent of \(\mathcal F_k^-\).
After revealing \(g_k\), the preactivation and backward feature have the exact
form

\[
 z_k=c_k+\alpha_kg_k,qquad b_k=a_kd(c_k+\alpha_kg_k), \tag{3}
\]

where \(a_k,c_k\) are \(\mathcal F_k^-\)-measurable.  This enlarged field is
\(\mathcal F_k^+\).  The subsequent backward query reveals the independent
residual block of \(\Gamma^*b_k\), producing \(\mathcal F_k\).  Thus

\[
 \mathcal F_k^-\subset\mathcal F_k^+\subset\mathcal F_k
 \subset\mathcal F_{k+1}^-                                      \tag{4}
\]

is the chronological alternating filtration.

## 2. Exact one-query increment of the invariant predictor

Fix an input coordinate \(j\).  Immediately before query \(k\), all old
first-chaos forward directions combine into an
\(\mathcal F_k^-\)-measurable vector \(v_{k,j}\in F_{k-1}+F_{k-1}^\perp\).
The coefficient of the new canonical input direction in coordinate \(j\) is

\[
 \xi_{k,j}=\langle e_k,e_j^{\rm coord}\rangle .
\]

After the harmless covariance normalizations used in the invariant isometry,
the coordinate functional of the enlarged forward first chaos is

\[
 L_{k,j}(g_k)=v_{k,j}+\xi_{k,j}g_k.                  \tag{5}
\]

This is simply the orthogonal decomposition of the known block
\(\Gamma P_{E_k}\) into the old block and its new residual.  The covariance
and backward-history corrections are already contained in \(v_{k,j}\) and
the projection in (2).

Let \(\Delta b_k=b_k-b_{k-1}\), with \(b_{k-1}\in F_{k-1}\).  Since the fresh
innovation (2) is orthogonal to \(F_{k-1}\), extension consistency gives the
exact coordinate increment

\[
 \Delta P_{k,j}
 =\langle v_{k,j}+\xi_{k,j}g_k,\Delta b_k\rangle.    \tag{6}
\]

Equation (6) is the coordinate version of
\(P_k-P_{k-1}=T_k(b_k-b_{k-1})\).  It includes the old-chaos contribution,
the new Gaussian atom, and all covariance/Onsager projections.

Choose the zero-fresh endpoint

\[
 \bar b_k=a_kd(c_k),\qquad \delta_k=\bar b_k-b_{k-1}.
\]

Using the exact divided difference of \(d\), (3) becomes

\[
 \Delta b_k=\delta_k+alpha_k a_k
      Dd(c_k,c_k+\alpha_kg_k)g_k.                  \tag{7}
\]

Substituting (7) in (6) gives the exact four-term decomposition

\[
\begin{aligned}
 \Delta P_{k,j}={}&\langle v_{k,j},\delta_k\rangle
 +\xi_{k,j}\langle g_k,\delta_k\rangle\\
 &+\alpha_k\langle v_{k,j},a_kD_k g_k\rangle
 +\alpha_k\xi_{k,j}\langle g_k,a_kD_k g_k\rangle,  \tag{8}
\end{aligned}
\]

where \(D_k=Dd(c_k,c_k+\alpha_kg_k)\) is diagonal.  For arctangent,

\[
 Dd(r,s)=-\frac{r+s}{(1+r^2)(1+s^2)},
\]

so \(D_k\) is bounded uniformly; no Taylor remainder has been used in (8).

## 3. The predictor is not a chronological martingale

Define its one-step conditional drift and centered atom by

\[
 \Delta D_{k,j}:=mathbf E[\Delta P_{k,j}\mid\mathcal F_k^-],
 \qquad
 \Delta M_{k,j}:=\Delta P_{k,j}-\Delta D_{k,j}.      \tag{9}
\]

Then \(M_{m,j}=\sum_{k\le m}\Delta M_{k,j}\) is a martingale for the
half-step filtration, and \(P_{m,j}=P_{-1,j}+M_{m,j}+D_{m,j}\).  In general
\(D\ne0\).  For instance, Gaussian integration by parts in the new component
of (8) gives

\[
\begin{aligned}
 \mathbf E\langle g_k,a_kd(c_k+\alpha_kg_k)\rangle
 =\alpha_k\,\mathbf E\operatorname{tr}_{F_{k-1}^\perp}
 \big(\operatorname{diag}(a_kd'(c_k+\alpha_kg_k))\big),       \tag{10}
\end{aligned}
\]

with the normalized trace dictated by the Ginibre scaling.  The right side
is generically nonzero.  Thus the invariant predictor itself is a predictable
response plus a martingale; it is not the martingale to which a direct BMO
argument could be applied.

## 4. The first exact obstruction in the martingale bracket

Even after the Doob compensation (9), the natural exponential-bracket route
is too strong.  To see the first obstruction without an inequality loss,
choose a coordinate with \(\xi_{k,j}=0\), take \(\delta_k=0\), and let
\(\alpha_k\downarrow0\).  Since \(d'\) is bounded, Gaussian dominated
convergence applied to (8) yields in conditional \(L^2\)

\[
 \alpha_k^{-1}\Delta M_{k,j}\longrightarrow
 \langle v_{k,j},\operatorname{diag}(a_kd'(c_k))g_k\rangle.  \tag{11}
\]

Therefore the conditional bracket atom has the exact leading term

\[
 \alpha_k^{-2}\,
 \mathbf E[(\Delta M_{k,j})^2\mid\mathcal F_k^-]
 \longrightarrow
 \big\|P_{F_{k-1}^\perp}operatorname{diag}(a_kd'(c_k))
          v_{k,j}\big\|^2.                         \tag{12}
\]

This term is not \(p_k^*H_kp_k\), nor is it controlled by the base Euler
energy.  It is an old canonical direction multiplied by the Gaussian endpoint
\(a_k=A^k\).  The conditional-mean compensator (9) cannot remove (12), because
(12) is the variance of a centered linear Gaussian term.

The obstruction is reachable in the actual query process and rules out a
*pathwise energy inequality*.  Work in dimension at least two, choose \(c_k\)
in a compact set on which \(|d'(c_k)|\ge c_0>0\), and choose the current
backward vector so that the current predictor coordinate is zero while the old
canonical vector \(v_{k,j}\) has a nonzero orthogonal component.  These are
open conditions.  In width \(n\), use the normalized Hilbert norm and take an
old canonical unit vector close to \(\sqrt n\,e_i\), together with
\(|a_{k,i}|\asymp\sqrt n\).  Then \(\|a_k\|\) can remain order one while the
right side of (12) is order \(\alpha_k^2n\).  A normalized fresh Gaussian
direction and the Gaussian endpoint hit every neighborhood of this
configuration with positive probability.  Hence no almost-sure estimate of
(12) by \(C(1+\|A^0\|+\text{base energy})\), with \(C\) independent of the
width, is possible.

This positive-probability construction by itself does **not** prove that the
bracket has no small exponential moment: the probability of a nearly
coordinate-aligned Gaussian direction can compensate its size.  Obtaining
such an exponential moment would require a joint delocalization estimate for
the *actual adapted* old canonical direction and \(A^k\).  Bessel supplies
only \(\|v_{k,j}\|\le1\), and the base energy supplies no such joint estimate.
Thus invoking exponential BMO at this point would merely restate the original
tail problem.

Thus a bound of the proposed form

\[
 \langle M\rangle_m\le C\left(1+sum_kh\,p_k^*H_kp_k\right)   \tag{14}
\]

cannot hold for the full chronological martingale without adding the endpoint
atom (12).  Adding (12) does not close the exponential-BMO proof from the
available hypotheses: its needed exponential moment is precisely a weighted
delocalization statement not implied by Bessel or energy.

## 5. What compensation does and does not fix

The Doob transform (9) correctly separates the signed conditional response
from the fresh Gaussian fluctuation.  It does not improve the bracket.  The
exact nonlinear increment, however, is much better behaved than its bracket:
from (6)--(7) and \(0<d\le1\),

\[
 |\langle v_{k,j},a_k[d(c_k+\alpha_kg_k)-d(c_k)]\rangle|
 \le 2\langle |v_{k,j}|,|a_k|\rangle.               \tag{15}
\]

The divided-difference formula in (15) suppresses the spurious higher powers
that arise from a long Taylor expansion when \(|\alpha_kg_k|\) is large.  In
particular, it is compatible with a direct \(\psi_1\) estimate even in regimes
where squaring the local Lipschitz coefficient in (12) is unusable.

The finite-mesh conclusion is therefore:

1. the invariant predictor is not a chronological martingale;
2. its centered fresh-query martingale has the endpoint-weighted atom (12);
3. a quadratic-variation/exponential-BMO continuation does not close from
   Bessel and energy alone;
4. the remaining viable route is a signed \(\psi_1\) or Abel/Orlicz estimate
   applied to the exact increment (8), keeping the divided difference intact.

The layer-3 Abel identity in `signed_predictor_abel_note.md` removes the full
curvature block before this decomposition.  What is still needed for a global
theorem is a non-triangular summation estimate for the old-chaos term in (8).
Taking absolute total variation over all time steps would reintroduce a factor
of the number of mesh points and is not mesh-uniform.
