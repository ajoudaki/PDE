# Bounded check of the Gaussian initialization modules

2026-10-06. **PASS for both stated module theorems.** The nonblocking finite-precision clarification identified during the check was added by the author and verified. This is a same-study proof check with prior conversation context retained, not a blind independent review or a promotion review. It does not certify a complete trained-network construction.

## Inputs and scope

I read the complete `GAUSSIAN_FEATURE_QUADRATURE.md` and `GAUSSIAN_SYNTHETIC_SELECTION.md`, reread current `AGENTS.md`, and checked the cited primary BSS theorem and its relevant barrier proof. I did not follow the selection note's link to another study, read any previous check report, run experiments, or perform Git operations. I did not edit either candidate.

The previously read rigorous-math checking skill and maintained notation contract were retained. A fresh attempt to read `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` again returned `Permission denied`; the previously authorized explicit-notation fallback remains in force. The associated neural-network reference was therefore unavailable as well.

The checked conclusions are:

- An explicit positive weighted Gaussian lattice approximates the first-layer tanh population pairing uniformly over both unit-sphere queries, with the stated polylogarithmic number of rows for fixed input dimension.
- Given the stated effective finite-dimensional source program and true source normalization, at most \(16R\) synthetic marks provide the stated frame bounds and an exact corrected source metric. Supplied cross pairings compile to a finite mixer representing the projected forward and reverse actions.

These conclusions do not establish a root-width comparison with a fresh dense network, a construction of the trained source functions, preservation of full reused Gaussian actions, or an ordinary neural gradient-flow optimizer. The lattice construction is dataset-blind. The selection theorem is conditional on its supplied sources and cross pairings; those inputs are not required to be dataset-blind.

## 1. Explicit Gaussian lattice

For \(d\ge1\), \(0<\epsilon\le1/2\), and the note's

\[
B=2^{d+10}d/\epsilon,\qquad
h=\min\{1,\pi^2/(4\sqrt d\log B)\},\qquad
M=\lceil2\sqrt{\log B}/h\rceil,
\]

all displayed constants check.

With \(\rho=\pi/(8\sqrt d)\), the strip bound follows from

\[
|\operatorname{Im}(a^Tv)|\le\rho\|v\|_1\le\pi/8
\]

for every unit \(v\), and from the displayed exact formula for \(|\tanh(s+it)|^2\). The Gaussian density on the shifted contour contributes only \(e^{d\rho^2/2}=e^{\pi^2/128}<2\). The contour shift has the correct sign and therefore gives

\[
|\widehat F(\xi)|\le2e^{-\rho\|\xi\|_1}.
\]

There is a pole-free neighborhood of the closed strip, so the use of holomorphy and Gaussian end-face decay is justified. Gaussian decay also justifies periodization and evaluation of its absolutely convergent Fourier series. Since \(2\pi\rho/h\ge\log B\), summing the nonzero Fourier modes gives

\[
2\left[\left(1+\frac2{B-1}\right)^d-1\right]\le16d/B.
\]

Indeed \(2/(B-1)\le4/B\), \(4d/B\le1\), and \(e^s-1\le2s\) for \(0\le s\le1\). The same argument applies to the Gaussian mass without the tanh factors.

The one-dimensional untruncated lattice mass is at most \(1+h/\sqrt{2\pi}<2\). Monotonicity of the positive Gaussian half-line gives

\[
\frac{2h}{\sqrt{2\pi}}\sum_{j>M}e^{-h^2j^2/2}
\le\frac2{\sqrt{2\pi}}\int_{Mh}^{\infty}e^{-s^2/2}\,ds
\le e^{-(Mh)^2/2}\le B^{-2}.
\]

Here \(Mh\ge2\sqrt{\log B}>1\), so the stated Gaussian tail estimate is sufficient. A union over the discarded coordinate directions yields \(d2^{d-1}B^{-2}\). There is no missing dimension factor.

The claimed raw-error budget has substantial slack. Explicitly,

\[
16d/B+d2^{d-1}B^{-2}
=\frac{\epsilon}{2^{d+6}}
+\frac{\epsilon^2}{d2^{d+21}}
<\epsilon/4.
\]

Thus \(Z\ge1-\epsilon/4>0\), and normalization gives

\[
|Q/Z-K|\le\frac{\epsilon/2}{1-\epsilon/4}\le\epsilon.
\]

Every estimate is uniform in the two unit queries; no probabilistic net or interchange of a query supremum with a pointwise estimate is being assumed. The row count follows from \(h^{-1}=O_d(\log(1/\epsilon))\) and \(M=O_d(\log(1/\epsilon)^{3/2})\). The implied constants may grow with \(d\); the result is not dimension-uniform.

The construction uses a weighted pairing. It does not identify this weighted feature geometry with an equal-weight ordinary network or establish a compatible training rule. The note's scope paragraph correctly withholds those claims.

The retained \(dq+q\) real coordinates and \(O(dq)\) construction arithmetic are consistent with enumerating the grid and normalizing its weights. The stated \(q\) exponential evaluations are attainable by retaining the unnormalized weights in the eventual weight array before normalization. A regeneration-based variant may recompute exponentials, changing only a constant factor. Neither storage convention requires an additional dense reference array.

## 2. Spectral selection and corrected metric

The imported result is correctly identified as the general-vector Theorem 3.1 of [Batson, Spielman, and Srivastava, *Twice-Ramanujan Sparsifiers*, November 18, 2009](https://www.cs.cmu.edu/~odonnell/hits09/batson-spielman-srivastava-twice-ramanujan-sparsifiers.pdf). I checked Section 2.3 and the complete pertinent barrier proof in Section 3.2. For an identity-decomposing frame, parameter \(b=16\) gives support at most \(16R\) and factor \(25/9\). The listed shifts, potential caps, initial barriers, final barriers, and averaging equality are the correct specialization. The paper's displayed implementation cost becomes \(O(JR^3)\) at this fixed parameter; \(J\ge R\) follows from full rank and absorbs the matrix-inversion term.

The preliminary quadrature is effective under the assumptions actually stated. Tail control bounds the omitted matrix in operator norm by its omitted trace. On the retained box, the estimate

\[
\|p(z)p(z)^T-p(z')p(z')^T\|_{\rm op}
\le2M\|p(z)-p(z')\|_2
\]

is correct. The two \(1/16\) budgets give \(\|M_Q-I\|_{\rm op}\le1/8\), and smaller initial budgets can accommodate finite evaluation and weight errors. No unsupported bound on the quadrature-pool size \(J\) is asserted.

Exact whitening gives the required identity decomposition. Undoing the congruence and multiplying the selected weights by \(6/5\) yields

\[
\frac65\frac78=\frac{21}{20},
\qquad
\frac65\frac{25}{9}\frac98=\frac{15}{4}.
\]

Both margins lie strictly inside the advertised interval \([1,4]\). The warning that a factor-four sparsifier alone leaves no room for quadrature distortion is valid.

For the metric, put \(U=ZG^{-1/2}\), so \(U^TU=I_R\). Its bracket is

\[
UG^{-1}U^T+I-UU^T.
\]

It acts as \(G^{-1}\) on the selected source range and as the identity on its orthogonal complement. Hence it lies between \(I/4\) and \(I\), and congruence by \(D^{1/2}\) gives \(D/4\preceq H\preceq D\). Multiplication gives \(P^THP=I_R\) exactly. This correction removes the quadrature error in the source inner product only because true population orthonormality was assumed; it does not estimate an unknown population covariance.

The constant source gives \(Pc=\mathbf1\) and \(\|c\|_2=1\), so \(1\le\sum_iD_{ii}\le4\). Consequently \(\|e\|_H\le2\|e\|_\infty\). The diagonal-multiplier estimate follows from

\[
A^THA\preceq A^TDA\preceq\|A\|_{\infty}^2D
\preceq4\|A\|_{\infty}^2H.
\]

It does not depend on the smallest retained diagonal weight.

The approximate-covariance correction also checks. On the source range, its normalized bracket is \(G^{-1/2}TG^{-1/2}\), which yields the stated \((1-\epsilon)/4\) and \(1+\epsilon\) bounds. If \(T\preceq G\preceq4T\), those bounds improve to \(1/4\) and \(1\). The discussion correctly distinguishes numerical small eigenvalues from certified exact rank.

## 3. Mixer, precision, and resource qualifications

The metric adjoint of

\[
B=P_2CP_1^TH_1
\]

is \(P_1C^TP_2^TH_2\). The maps \(P_\ell\) are isometries from coefficient space, and \(P_\ell^TH_\ell\) are their adjoints. Therefore the two action identities, the norm equality \(\|B\|=\|C\|_{\rm op}\), and the identical norm formula for a cross-pairing perturbation are exact.

The population action represented by \(B\) is precisely \(\Pi_2T_{21}|_{S_1}\), and its reverse is \(\Pi_1T_{21}^*|_{S_2}\). Full action preservation requires the corresponding forward and reverse range inclusions. The note correctly warns that an omitted \(L^2\) component has no automatic pointwise bound at selected marks. It also correctly identifies the metric adjoint of a coordinate gate as \(H^{-1}AH\); a non-diagonal metric cannot be inserted into an ordinary backpropagation formula without rederiving that formula.

The distinction between exact-real BSS arithmetic and a computable implementation is handled correctly. A finite support with strict spectral margins has a positive rational-weight approximation on the same support. The proposed strict positive-definiteness certificates are sound and eventually succeed for such a candidate. Dovetailing prevents undecidable equality cases from blocking the search. A stage-by-stage implementation can reenumerate candidates and discard unsuccessful finite certificates, so this computability argument need not retain all search states simultaneously. There is no useful running-time bound for that search.

The resource qualifications are material and correctly stated: the pool may have \(J>n\); source evaluation has separate workspace; raw marks cost \(O(kR)\); the retained metrics, evaluation matrices, and mixers cost \(O(R^2)\); actual source programs, first-layer weights, decoders, and precision bits require separate accounting. Disposing of \(P\), marks, or \(C\) is justified only after every later operation that needs them has been compiled. Supplying a matrix whose computation itself requires inaccessible dense arrays would not satisfy the direct-input assumption.

For the normalized metric perturbation, the bound

\[
\|P^T\widetilde HP-I\|_{\rm op}
\le\|D^{1/2}P\|_{\rm op}^2\,
\|\widetilde Q_H-Q_H\|_{\rm op}
\le4\epsilon
\]

is correct, and \(\epsilon<1/4\) preserves positive definiteness. Errors in \(D\), \(P\), and downstream dynamics are explicitly excluded from this single estimate and need their own budgets. Exact transcendental source identities are not represented as finite rational bit strings.

The initial check identified one nonblocking clarification in the lattice note's finite-precision paragraph: exact evaluation of the ceiling defining \(M\) is not generally a decidable operation on an arbitrary computable real. The author added a certified rational spacing between half the displayed step and that step, followed by a safe integer truncation above a certified upper approximation. I verified the new paragraph. Using the chosen rational spacing in the denominator, take the least integer strictly above an upper approximation with error less than one. This increases the threshold by less than two and preserves both the spacing upper bound and the lower bound on \(Mh\), so the proof and asymptotic row count survive. The clarification is resolved. Removing exactly the new paragraph in memory reproduces the originally checked file hash; no other lattice-note content changed.

The remaining uniform rounding assertion is valid and can be made explicit. If rows change by at most \(\delta_a\) in Euclidean norm and the weight vector changes by at most \(\delta_p\) in \(\ell^1\), boundedness and Lipschitz continuity of real tanh give pairing error at most \(2\delta_a+\delta_p\), uniformly in both unit queries. Thus the strict analytic slack can absorb certified parameter rounding. No bit-complexity estimate follows from that continuity argument, as the note states.

## 4. Additional envelope observation supplied during this check

The supervisor also supplied a separate proposed corollary in the task messages. Its abstract implication is correct under its stated pointwise premise. Suppose the enlarged source space contains a continuous function \(e\) satisfying

\[
|r_{t,x}(z)|\le e(z)\quad\text{for every relevant }(t,x,z).
\]

The selected frame bound gives

\[
\sum_iD_{ii}e(z_i)^2\le4\|e\|_{L^2(\mu)}^2.
\]

Hence the vector of selected residuals satisfies

\[
\|(r_{t,x}(z_i))_i\|_H
\le\|(r_{t,x}(z_i))_i\|_D
\le2\|e\|_{L^2(\mu)},
\]

uniformly over the same family. Adding one function increases the source dimension by at most one after taking its independent component. Applying the constructive selection theorem still requires effective moments, tails, evaluations, and a certified rank or quotient for that enlarged space. The bound must hold for the representatives evaluated at the marks; an arbitrary almost-everywhere representative cannot be substituted. No unprovided harmonic-tail application, training estimate, or construction of such an envelope was checked.

## Checked hashes

| Input | SHA-256 |
| --- | --- |
| `GAUSSIAN_FEATURE_QUADRATURE.md`, current clarified input | `5636b9964b1e6adae2771c2325ce134b6f7ac3ad0df815a2e53c978f4825d042` |
| `GAUSSIAN_FEATURE_QUADRATURE.md`, initially checked input | `520b67d04d2e2d14f14827cffbe23e37c13efbc2391ecb0b8515ae9d1dc92930` |
| `GAUSSIAN_SYNTHETIC_SELECTION.md` | `3eb17a6963242bf9336e645a203fd6e67983e626de0ef39a85d917cb44a9e384` |
| Current `AGENTS.md` | `d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97` |

The primary reference was read from the linked 21-page PDF, identified there as arXiv:0808.0163v3, November 18, 2009. No local PDF copy or byte hash was created. This report is the only file written by this check.
