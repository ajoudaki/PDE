# Informed internal audit of rank-one exclusion

2026-09-19. **Verdict: PASS for the frozen rank-one theorem as stated. No mathematical correction is required.** For the canonical full dictionary, nonconstancy of its actual scalar image in \(L^2\) automatically implies the theorem's infinite-essential-support hypothesis. Constant images and effective rank zero are not resolved by this theorem or this review.

## Provenance and frozen inputs

This is an explicitly informed internal audit, not an isolated or promotion review. I authored dictionary_route.md and dictionary_counts.md and previously reviewed finite_sample_theorem.md. I read the complete frozen rank-one candidate. I did not read abstract_route.md; its bookkeeping description within the candidate supplies no mathematical premise here. Neither Lyapunov's convexity theorem, the infinite product for cosh, nor a moment-interior theorem is used.

| Input or already-known supporting artifact | SHA-256 |
|---|---|
| rank_one_exclusion.md | d5d335988e0b35e0b22b79f8aadf14040638e8ff50749f1f56428b4d9b805a9d |
| finite_sample_theorem.md | 5242bfda61ed94f2e5bda83b8843fe713d37dcbf4b7e2f204dc1ba8c23757c24 |
| dictionary_route.md | a95512882aa16474e6f6bd9ad0d4a88e3d9499d2b6976191188e4fa752079c53 |
| dictionary_counts.md | 87ddaf612ff335f0829a9cc5103c74022786dfec04de4bc9749800319c1fa804 |
| docs/global_nonlinear.md | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

The established source scope remains complete C.4.7.9.2–4 and C.4.7.10.B, C.1, D.3, together with the notation contract. No other study or route was read. Only this review file was written. The frozen candidate and the earlier main-theorem review were left unchanged.

## 1. Effective operator and redundant coordinates

The candidate restricts the lower coefficient domain to

\[
 B_1=\ker E[b_1b_1^T]^\perp.
\]

This is the correct effective domain: every \(a_i\) belongs to it, and a nonzero vector in it defines a nonzero lower mark function. The output map \(U_2\) automatically quotients out all upper coordinate redundancies. Consequently \(K=U_2M|_{B_1}\), rather than the raw matrix \(M\), is the correct map for the rank-one hypothesis.

It also has the same rank as the full current population action \(U_2MU_1^*\), where \(U_1h=b_1^Th\). Indeed \(\operatorname{range}U_1^*=B_1\): containment follows from orthogonality to the Gram kernel; conversely, for \(a\in B_1\), let \(h\in B_1\) solve \(E[b_1b_1^T]h=a\), and then \(U_1^*(b_1^Th)=a\). Thus no inaccessible lower coefficient direction is counted in the theorem.

Rank-one factorization gives a nonzero Euclidean functional on \(B_1\), represented by \(v\in B_1\setminus\{0\}\), and a nonzero bounded output function \(T\). Boundedness follows from \(T=Kh\) for a fixed \(h\) with \(v\cdot h=1\). Applying the factorization to the random vector \(b_1(\omega)\) is legitimate: equality on a finite basis of \(B_1\) gives one common upper null set, outside which it holds for every \(h\in B_1\).

## 2. Necessary condition in the physical topology

The input-ridge independence proof is correct for every finite collection of nonzero unit vectors distinct modulo sign. It requires neither linear independence of those input vectors nor a sample-count bound. The nonzero odd Taylor coefficient recurrence and the resulting Vandermonde system have the correct signs and indices.

The lower-subset argument is valid in \(L^2\). A bounded replacement on a subset of probability \(\varepsilon\) has squared \(L^2\) distance \(O(\varepsilon)\), changes the finite moment vectors by \(O(\varepsilon)\), and therefore has an \(O(\varepsilon^2)\) Taylor remainder. The strict improvement has order \(\varepsilon\). Nonatomic scalar subdivision is sufficient, and the file explicitly supplies its elementary justification.

The loss and all derivatives used are finite for \(w,c\in L^2\), bounded marks, a finite matrix, and finitely many finite labels and positive weights. The weights need not sum to one for this subsidiary theorem; arbitrary finite positive weights merely rescale the same identities. Matrix stationarity has the correct factor of two for the unhalved square loss.

It follows that equation (6) is valid without a dimension bound. Under the rank-one factorization, the displayed contraction reduces to

\[
 (v\cdot b_1)\,E[cT\phi'(\alpha_iT)].
\]

The nonzero variance of \(v\cdot b_1\) then gives equation (7). No stronger moment assumption is used.

## 3. Readout-null perturbations

For every \(q\in\mathcal H^\perp\subset L^2\), the perturbed readout \(c+\varepsilon q\) is an admissible state and preserves predictions exactly. Its physical displacement is \(|\varepsilon|\|q\|_2\). An equal-value state strictly inside a local-minimum ball is itself a local minimum on a smaller ball. Thus the necessary condition can be applied at both states.

The perturbation preserves \(w,M,K,T,v,\alpha_i\) and all residuals, so subtracting equation (7) is valid. The allowed nonzero \(\varepsilon\) may depend on \(q\); the argument does not require uniformity over all directions. Because \(T\phi'(\alpha_iT)\) is bounded and \(\mathcal H\) is finite-dimensional and closed, orthogonality to \(\mathcal H^\perp\) gives equation (8).

This step works even when every \(\alpha_i=0\), when some features vanish, and when different sample features coincide or are negatives. No Gram inverse or conditioning bound is involved.

## 4. Pole-order lemma

The lemma is valid for every bounded scalar random variable with infinite essential support, including infinitely supported purely atomic and singular laws.

The support of its law is a compact infinite subset of \(\mathbb R\). A continuous almost-sure identity holds at every support point, and compact infinitude supplies a finite real accumulation point. The difference is real analytic on all of \(\mathbb R\), so it vanishes identically there.

For \(\alpha_i=0\), this yields equality of \(t\) with a finite bounded sum of real tanh functions, an immediate contradiction.

For \(\alpha_i\ne0\), the complex functions are meromorphic. The zeros of \(\cosh\) follow directly from \(e^{2z}=-1\), and their derivatives \(\sinh z\) are nonzero. Every nonconstant \(\tanh(\alpha_jz)\) consequently has only simple poles. A finite sum has at most a simple pole at every point; coincident poles can cancel but cannot create a double pole. Zero slopes contribute the zero function.

The finite union of pole sets is locally finite. Removing it from the complex plane leaves a connected open set, as verified by detouring a bounded polygonal path around its finitely many encountered poles. The holomorphic identity theorem therefore applies to the real interval already known to satisfy the identity.

At \(z_0=i\pi/(2\alpha_i)\), writing \(\zeta=z-z_0\), the expansion in the candidate is correct:

\[
 \cosh(\alpha_i z)=i\alpha_i\zeta+O(\zeta^3),
\]
\[
 z\operatorname{sech}^2(\alpha_i z)
 =-\frac{z_0}{\alpha_i^2\zeta^2}
  -\frac{1}{\alpha_i^2\zeta}+O(1).
\]

Here \(z_0\ne0\), so the double-pole coefficient cannot vanish. After multiplication by \(\zeta^2\), the right-hand side tends to zero and the left-hand side tends to \(-z_0/\alpha_i^2\ne0\). This is a valid contradiction. Negative, opposite, repeated, or differently scaled nonzero \(\alpha_j\) do not alter the argument.

## 5. Canonical nonconstant scalar marks have infinite support

For completeness, this additional implication can be established without an analytic-zero-set theorem. At a fixed order, the canonical finite initialization program represents the bounded mark column as

\[
 b_2=\beta(G),\qquad G\sim N(0,I_k),
\]

with \(\beta:\mathbb R^k\to\mathbb R^{k_2}\) continuous, indeed real analytic. Degenerate innovations are represented by deterministic linear maps of independent standard Gaussians; zero innovations may be omitted. The source law therefore has full support in its chosen source space.

Every possible scalar output \(T\) in the current rank-one image is \(T=b_2^Th\) for fixed coefficients \(h\), hence \(T=F(G)\) for a bounded continuous function \(F\). Its distribution has support exactly

\[
 \overline{F(\mathbb R^k)}.
\]

One inclusion holds because all realized values lie in the image. For the other, every neighborhood of an image value has a nonempty open preimage, and a full-support Gaussian assigns that preimage positive probability. Taking closures gives the equality.

Since \(\mathbb R^k\) is connected, its continuous scalar image is an interval. If \(T\) is nonconstant in \(L^2\), \(F\) cannot be constant, and its image contains at least two points. The support is therefore a nondegenerate compact interval and is infinite. If there are no Gaussian source coordinates, every such field is constant and the implication is vacuous.

This argument needs actual nonconstancy of the function on the source support, equivalently nonconstancy of the random variable in \(L^2\). A formally nonconstant expression or an unused continuous dictionary coordinate does not establish that condition. It also does not assert that the scalar law has a density.

Thus the audited theorem applies, at every fixed canonical order and for arbitrary finite sample count, to effective rank-one ambient local minima whose actual scalar image is nonconstant.

## Final scope

PASS concerns this subsidiary theorem and the canonical nonconstant-image implication just verified. It does not cover constant scalar images, effective rank zero, higher-rank images, constrained or particle-state minima, or convergence of training. The main finite-sample theorem and its prior review remain unchanged.
