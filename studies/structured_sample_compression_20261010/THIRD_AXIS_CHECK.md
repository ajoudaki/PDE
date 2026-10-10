# Targeted mathematical check of THIRD_AXIS

Scope: `THIRD_AXIS.md` and the required mathematical-presentation skills only.
No route files, other studies, source paper, experiments, or prior verdicts
were consulted. This is an internal targeted check, not a promotion review.

The independently displayed product-tail identity and analytic rank estimate
are correct. The distinctions between rank, retained storage, an autonomous
runtime, and all-time comparison are substantive and correctly maintained.
The clock paragraph needs explicit conventions to make its normalization
self-contained; the route summaries remain unverified within this scope.

## Product tails and normalization

For real vector-valued responses, let
\(\langle u,v\rangle_m=m^{-1}\sum_a u_av_a\), and let the scalar sample
functions \(\psi_j\) be orthonormal in this normalized inner product.
Then \((Ph)_a=\sum_j\psi_j(a)h_j\), with
\(h_j=m^{-1}\sum_a\psi_j(a)h_a\), and likewise for \(b\).
Componentwise orthogonality eliminates both mixed terms and gives (1)
with no additional factor of \(m\). Moreover,

\[
\left\|\frac1m\sum_a b_a^\perp h_a^{\perp\top}\right\|_F
\le \frac1m\sum_a\|b_a^\perp\|\,\|h_a^\perp\|
\le \|b^\perp\|_{L^2_m}\|h^\perp\|_{L^2_m},
\]

where \(b^\perp=(I-P)b\) and \(h^\perp=(I-P)h\). Thus (2) is valid.
Under the displayed dense update, its velocity defect has the additional
factor \(2/n\). The network/loss convention giving that prefactor is not
defined in this note and was not independently source-checked here.

Fixed sample projection commutes with a common orthogonal time projection:
the operators act on separate factors of the product measure. Their
product is an orthogonal projector, so the same identity holds for the
integrated pairing. This statement concerns projection of the exact
histories; it does not supply autonomous equations for approximate histories.

To make the clock normalization explicit, suppose the clock satisfies
\(\dot\tau(t)=\rho(t)>0\), and use
\(b_a(\tau(t))=(r_a(t)/\rho(t))\delta_a(t)\). Extend this backward
history by zero over any initial clock prefix. With normalized clock measure
\(d\nu=ds/\tau(t)\), let \(\phi_0,\ldots,\phi_{q-1}\) be orthonormal,
and define \(H_{jk}=\langle\psi_j\phi_k,h\rangle_{m,\nu}\) and
\(B_{jk}=\langle\psi_j\phi_k,b\rangle_{m,\nu}\). For the joint projector
\(Q\), the exact identity is

\[
W(t)-W(0)=-\frac{2\tau(t)}n\left[
\sum_{j,k}B_{jk}H_{jk}^{\top}
+\langle(I-Q)b,((I-Q)h)^\top\rangle_{m,\nu}\right].
\]

An orthonormal basis for unnormalized measure \(ds\) absorbs the factor
\(\tau(t)\). The note does not specify which stored-moment convention it
uses, so no source-specific Legendre prefactor is certified here. It should
also state the clock definition and the convention when \(\rho=0\);
division-free physical writes alone do not define the displayed quotient
there. The count \(2(L-1)nRq\) is consistent for two response arrays,
\(L-1\) interfaces of width \(n\), and ranks \(R,q\), with the separately
listed remaining state still counted.

## Analytic approximation

For multi-indices \(\alpha\in\mathbb N_0^k\), Cauchy's formula on any
smaller polydisk of radius \(s<\rho\) gives
\(\|c_\alpha\|\le Bs^{-|\alpha|}\). Taking \(s\uparrow\rho\)
justifies the stated coefficient bound even for the open polydisk.
Writing \(u=\rho^{-1}\), each event \(\alpha_j\ge K\) contributes
\(u^K(1-u)^{-k}\) to the coefficient majorant. Summing over \(j\)
proves (3); counting \(0\le\alpha_j<K\) gives exactly \(K^k\)
retained monomials. For \(B>0\), put
\(A=kB(1-\rho^{-1})^{-k}\). The explicit choice

\[
K=\max\left\{1,\left\lceil\frac{\log(A/\eta)}{\log\rho}\right\rceil\right\}
\]

suffices, and proves (4) in its intended small-error regime. If \(B=0\),
the family vanishes. The sampled polynomial span has dimension at most
\(\min(m,K^k)\); its best empirical orthogonal approximation is no worse
than this uniform polynomial approximation. No sampling-density assumption
is needed. The stated need for an accessible chart and uniform family bounds
is essential and correctly retained.

## Limits and remaining verification

The Lipschitz covering statement is consistent with a bounded latent subset
of \(\mathbb R^k\), a uniformly Lipschitz generator, and uniform response
Lipschitz constants. The text correctly excludes deriving analytic tails
from this assumption alone. It also correctly distinguishes population
harmonic tails from arbitrary empirical or uniform control.

No implication from these ranks to nonlinear closure, low-cost contractions,
width-uniform error propagation, or all-time dense-trajectory accuracy is
claimed. The warnings about basis storage, query support, residual-weighted
responses, separate factor projections, and operator mismatch address the
main possible overinterpretations.

The exact tensor storage count and coefficient-loss gradient, modal
contraction estimate, and method-specific Legendre/Harmonic/Taylor
inventories require their cited route or source inputs. They remain
unverified summaries in this check. No substantive error was found in
the independently displayed mathematics.

## Checked correction, 2026-10-10

Reread the revised normalization and first section of `THIRD_AXIS.md`, SHA-256
`a26ce30077b10efcbe69cc9151fac33a05d7785a67c2af8eab63b7018416731f`.
The supplied definitions give
\(\partial f/\partial W=\delta h^\top/n\) at an interior hidden interface;
squared loss and unit mobility therefore give the displayed \(-2/n\)
update factor. The clock, initial prefix, and residual-zero continuation
are now explicit. Since
\(\int_0^\tau P_j(2\xi/\tau-1)^2d\xi=\tau/(2j+1)\), the retained
Legendre increment has exactly the stated coefficient
\(-2(2j+1)/(n\tau)\) multiplying each moment product. These corrections
resolve this check's normalization and zero-clock-rate clarification requests.
No paper or route inputs were added to the audit; their source-specific
claims retain the scope qualifications above.
