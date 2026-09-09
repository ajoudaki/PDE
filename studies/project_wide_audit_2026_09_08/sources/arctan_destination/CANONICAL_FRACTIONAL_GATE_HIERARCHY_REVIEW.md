# Independent audit of the complete canonical tiny-readout / fractional-gate chain

Audit date: 2026-09-05.

## Verdict and correction provenance

**PASS for the corrected, hash-verified complete scoped chain. No required mathematical fixes remain.** This verdict covers the direct positive-time redo in the 901-line rare-path note, the full 169-line corrected fractional note, and the accumulated relative consequence. It does not assume those inputs as unproved premises.

The initial corollary version failed the literal audit because of two missing plus signs. The supervising assistant corrected exactly those signs at lines 45 and 110; the actual user did not edit the candidate. I reread the complete corrected corollary, verified its final SHA-256 as 80aa2ec308af171feb357c0c3f70347b1116d74d90c8a93163b53a1bc14b0ec5, and verified that the upstream note and all eight dependencies are unchanged. Replacing just those two leading plus signs by their former spaces reconstructs the exact superseded SHA-256 e4d397b2e364e4221c0232a46c66b25c0e68b7f1a34b0ed766804a8bf5c14b39. This independently confirms the stated correction scope.

The resolved findings were local display corrections, not a discovered failure of the intended positive-time argument. I independently checked the complete direct redo in the first candidate, all eight permitted dependencies, the accumulated relative consequence, and the intended additive fractional argument. No additional necessary mathematical correction or dependency was identified. In particular, the initial-readout covariance, the nonzero energy boundary, and the accumulated rank-memory boundaries have different roles and were checked separately.

The following required changes were completed by the supervising assistant. I made no candidate edits; the original findings and justifications are preserved here as provenance:

1. In CANONICAL_FRACTIONAL_GATE_HIERARCHY.md, line 45, equation (2), the supervising assistant inserted a plus sign before \(t\int_0^t\mathcal I_n(a,u)\,du\). The corrected assertion is
   \[
   \frac1n\sum_iw_iq_{*,i}^{(2)}(t)^2
   \le C\left[
   (t^2+n^{-2})\{h(a)+\epsilon_n^2\min(1,na)\}
   +t\int_0^t\mathcal I_n(a,u)\,du
   \right].
   \tag{R1}
   \]
2. In the same file, line 110, equation (5), the supervising assistant inserted a plus sign before the gate-product integral. The corrected assertion is
   \[
   y_E(t)\le C\left[
   t\{h(p_E)+\epsilon_n^2\}
   +\int_0^t\Phi(y_E(s))\,ds
   +\int_0^t\sqrt{y_E(s)}\,\frac{\|v_E(s)\|_2}{\sqrt n}\,ds
   \right].
   \tag{R2}
   \]

For the decisive contradiction to the superseded equation (2), take \(w_i=1\) and \(t=0\). That version's right side is zero, because the entropy/initialization factor is multiplied by \(t\int_0^t\mathcal I_n\). Its left side is \(\|q^{(2)}(0)\|_2^2/n\). Almost surely \(W^{(3)}_0\) is invertible, all entries of \(\phi'(z^{(3)}_0)\) are strictly positive, and \(G^{(4)}\ne0\). Thus
\[
q^{(2)}(0)=(W^{(3)}_0)^T
\operatorname{diag}(\phi'(z^{(3)}_0))G^{(4)}/n\ne0
\quad\text{almost surely}.
\]
The claimed good event has positive probability, for example for \(M=10\), sufficiently large \(n\), and \(\eta=1/n\). It cannot avoid this contradiction. Changing a finite constant does not repair it. Line 145's assertion that equation (2) retains the initial mass was also false for that version and is correct in the frozen revision.

For the superseded equation (5), the issue was the invalid transcription/inference from the first candidate's equation (38): that equation supplies a sum of the two integrals, not their product. I do not assert an additional network counterexample to the product formula. The completed repair is R2, which is exactly the inequality justified by the derivation.

The final fractional hierarchy, equation (4), was already correctly written and follows from the now-corrected displays. The remainder of this review supplies the full mathematical audit rather than assuming the upstream inputs.

## Scope, independence of this audit, and exact source identities

I read /etc/codex/skills/solve-math-rigorously/SKILL.md in full and followed it. Its SHA-256 is
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7.

All ten mathematical files below were read completely, totaling 3,329 lines. Their common root is
/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/.
The final candidate hashes match the user's frozen values exactly. The corrected 169-line corollary was subsequently reread in full; both its current and superseded hashes are recorded below.

| Mathematical file | Lines | SHA-256 |
| --- | ---: | --- |
| CANONICAL_TINY_READOUT_RARE_PATH.md | 901 | 85898acdf9216f339b9a772732f7d5b40fbeb9f170602ae2c48e9a3b1c548315 |
| CANONICAL_FRACTIONAL_GATE_HIERARCHY.md — final corrected version | 169 | 80aa2ec308af171feb357c0c3f70347b1116d74d90c8a93163b53a1bc14b0ec5 |
| CANONICAL_FRACTIONAL_GATE_HIERARCHY.md — superseded initial version | 169 | e4d397b2e364e4221c0232a46c66b25c0e68b7f1a34b0ed766804a8bf5c14b39 |
| PRUNED_GAUSSIAN_SUBSET_BOUND.md | 198 | 383a12f3c5b459ec54927788a710fbea9e4d11b95ef83b0413c53dc5b2099787 |
| PRUNED_RARE_BLOCK_GEOMETRY.md | 230 | 71316052df34a348164ba02addd5478a4ecdd9bf5f26649535f2c047307d7c99 |
| ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md | 162 | 3356d7f4063090dc79f7a856c0492ced304092c447b4996f258fb15c6d826db1 |
| SINGLE_PRUNED_OFFBLOCK_OSGOOD.md | 445 | 0f907e82e212813ac3f97818b0fbd3db652ac1310b8629365b456b6cb68256c3 |
| DIRECT_SCALAR_PRUNED_REDUCTION.md | 282 | 31f84ed356d9f26eff58d2ca4b9f596c07ad1e265b3b825b6c5b3fd8feec3e39 |
| ACTUAL_RARE_BACKWARD_DERIVATIVE.md | 424 | e402abc3c591fb029bf82d6e7b97bc533003e79104aab1b6c4837b13ed040be8 |
| RARE_BACKWARD_ENERGY.md | 199 | 32675e45b51502fbc56ae69b15c840129a322115d12c5ec44fd11302e1fd645b |
| ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md | 319 | 73b5f44b4fc6796ab08078e2d845d20fc51378107a48bc0233ef81d08359ce41 |

No conversation archive, master ledger, other review, source agent, or additional mathematical source was consulted. No numerical or computational experiment was performed. File reads, line identification, cryptographic hashes, and document integrity/notation checks were the only diagnostic computations. The candidates were not edited. No further necessary dependency beyond the eight authorized dependencies arose.

Below, A means the unchanged first candidate and B means the final corrected fractional candidate. Equation numbers qualified by A or B refer to those frozen source files. References to the superseded version are explicitly identified. Conversion of this review to ordinary norms with explicit empirical factors follows the user's notation contract; it is not an additional mathematical finding.

## 1. Finite setup, normalizations, and the direct deterministic redo

The vector norms \(\|\cdot\|_2\) and \(\|\cdot\|_\infty\) are the ordinary Euclidean and maximum norms, respectively; matrix norms are ordinary operator or Frobenius norms. Empirical factors are written explicitly, including in inner products and rank updates. In particular,
\[
\|\frac{uv^T}{n}\|_{\mathrm F}=\frac{\|u\|_2\|v\|_2}{n}.
\tag{R3}
\]
This also agrees with the Hilbert--Schmidt norm between two vector spaces both equipped with the normalized inner product: their orthonormal bases are \(\sqrt n\,e_i\), and summing the squared normalized output norms gives the ordinary Frobenius norm. No extra \(n^{-1}\) belongs in the matrix terms of \(y_E\).

Fix \(S>0\), \(M>0\), \(n\ge2\), and \(0<\eta<1\). The initial \(z^{(1)}_0\) and \(G^{(4)}\) have independent standard Gaussian coordinates; \(W^{(2)}_0,W^{(3)}_0\) have independent \(N(0,1/n)\) entries; all four blocks are independent. Both full and pruned networks start from these same parameters, with \(W^{(4)}_0=G^{(4)}/n\). For \(E\subseteq\{1,\ldots,n\}\), write \(P=P_E\), \(Q=I-P\), \(p=|E|/n\), use hats for its fully pruned reference, and let \(\Delta\) denote full minus pruned. A fixed scalar map \(\tau\), applied coordinatewise, obeys \(|\tau(v)|\le|v|\) and \(|\tau(v)-\tau(w)|\le|v-w|\).

The forward definitions are \(h^{(\ell)}=\phi(z^{(\ell)})\), \(z^{(2)}=W^{(2)}h^{(1)}\), \(z^{(3)}=W^{(3)}h^{(2)}\), and \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\). In a reference, \(\widehat h^{(2)}=Q\phi(\widehat z^{(2)})\) and the backward action also has left \(Q\). All other definitions and updates are unchanged. Write \(x^{(1)}=F(z^{(1)})\).

The events used below are
\[
\Omega_M=\{\|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le M\},
\qquad
\Omega_4=\{\|G^{(4)}\|_2/\sqrt n\le2,\ \|G^{(4)}\|_\infty/n\le1\}.
\]
Constants \(C\) depend only on \(S,M\) and may increase between estimates.

For \(\phi=\arctan\), \(c=\pi/2\), and \(F(z)=z+z^3/3\), one has
\[
|\phi|\le c,\quad |\phi'|\le1,\quad |\phi''|\le2,\quad
|\phi'''|\le8,\quad (F^{-1})'\le1.
\]
If \(\chi=\phi\circ F^{-1}\), then \(|\chi'|\le1\), \(|\chi''|\le4\).
The transformed lower update is exactly
\[
(x^{(1)})'=(W^{(2)})^T\delta^{(2)},
\]
because \(F'(z)\phi'(z)=1\). The remaining full updates are
\[
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad
(W^{(4)})'=h^{(3)},
\]
with
\[
\delta^{(3)}=D_3W^{(4)},\quad q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=D_2\tau(q^{(2)}).
\]
Pruning sets both \(h^{(2)}\) and \(\delta^{(2)}\) to zero on \(E\). It leaves the stored deleted rows/columns equal to their initial values.

On \(\Omega_4\), every full or pruned readout obeys
\[
\|W^{(4)}(s)\|_\infty\le1+cs,\qquad
\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le2/n+cs.
\]
Thus \(R=1+cS\), \(K_3=M+cSR\), and \(K_2=M+cSK_3R\) give
\[
\frac{\|\delta^{(3)}\|_2}{\sqrt n}\le R,\quad
\|W^{(3)}\|_{\rm op}\le K_3,\quad
\frac{\|\delta^{(2)}\|_2}{\sqrt n}\le K_3R,\quad
\|W^{(2)}\|_{\rm op}\le K_2,\quad
\frac{\|(x^{(1)})'\|_2}{\sqrt n}\le K_2K_3R.
\tag{R4}
\]
Before imposing the full operator event, the reference versions use the active matrices \(Q\widehat W^{(2)}\), \(\widehat W^{(3)}Q\), except when the appropriate selection event also controls the full incoming matrix. R3 bounds the trained Frobenius increments as well.

The vector field is locally Lipschitz for every prescribed dominated 1-Lipschitz \(\tau\). For any fixed finite initial data and time horizon, these bounds and the lower velocity bound keep all parameters and \(z^{(1)}\) in a bounded finite-dimensional region. The local solution therefore extends to that horizon. This is a direct finite-dimensional existence argument. It claims neither a width-independent derivative with respect to initial data nor a population continuation result.

The state distance is zero initially because the parameters and \(x^{(1)}\) are shared. Derived top features need not agree initially:
\[
z^{(3)}_0-\widehat z^{(3)}_0=W^{(3)}_0P\phi(z^{(2)}_0).
\]
This accounts for the \(\sqrt p\) terms in the comparison; it does not alter \(y_E(0)=0\). Shared initial values and bounded trained increments give \(y_E\le C_{S,M}\) without using initial Gaussian Frobenius norms or moments of \(F(z^{(1)}_0)\).

## 2. Active sigma fields, selection events, and time regularity

For a deterministic \(E\), the active reference path is measurable with respect to
\[
\mathcal F_E^{\rm in}
=\sigma(z^{(1)}_0,QW^{(2)}_0,W^{(3)}_0Q,G^{(4)}).
\]
It is independent of both \(PW^{(2)}_0\) and \(W^{(3)}_0P\). Indeed the lower active velocity uses only \((Q\widehat W^{(2)})^T\widehat\delta^{(2)}\), and the active upper equations use only \(\widehat W^{(3)}Q\). The unused rare preactivation and unused transpose query are not asserted to be active-measurable.

The enlarged field
\[
\mathcal F_E^{\rm top}
=\sigma(z^{(1)}_0,W^{(2)}_0,W^{(3)}_0Q,G^{(4)})
\]
can support coefficients containing the full incoming matrix, while remaining independent of \(W^{(3)}_0P\).

The selections in A(16) use \(\Omega_4\) and the corresponding active initial operator bounds. They are measurable in the respective fields. Selecting the entire coefficient/vector path to be zero outside its event preserves independence of the queried deleted Gaussian block. The full operator event \(\Omega_M\) is intersected only after the conditional estimates. No conditional independence after imposing \(\Omega_M\) is needed.

For the derivative grids, the exact identities are
\[
(h^{(1)})'=D_1^2(W^{(2)})^T\delta^{(2)},\quad
(z^{(2)})'=A_2\delta^{(2)},\quad
(h^{(2)})'=D_2A_2\delta^{(2)},
\]
\[
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}+W^{(3)}(h^{(2)})',\quad
(\delta^{(3)})'=D_3h^{(3)}+B(z^{(3)})',
\quad B=\operatorname{diag}(W^{(4)}\phi''(z^{(3)})).
\tag{R5}
\]
The reference activation derivative has its required left \(Q\). R4 gives the normalized first-velocity bounds, including A(13).

The essential acceleration argument uses \(q_a=Q(\widehat W^{(3)})^T\widehat\delta^{(3)}\), not the potentially unbounded unused query on an active event. Both \(\frac{\|q_a\|_2}{\sqrt n}\) and \(\frac{\|q_a'\|_2}{\sqrt n}\) are bounded by R5. In
\[
\widehat\delta^{(2)}=Q\widehat D_2\tau(q_a)
\]
the derivative of the gate costs at most
\[
2\frac{\|Q\widehat z^{(2)\prime}\|_2}{\sqrt n}\|q_a\|_\infty
\le C\sqrt n.
\]
The other term is bounded by \(\frac{\|q_a'\|_2}{\sqrt n}\), since
\(|(\tau(q_{a,i}))'|\le |q_{a,i}'|\) almost everywhere. Differentiating the active mobility then gives an operator bound \(C\sqrt n\); the active second preactivation and activation derivatives have normalized bounds \(C\sqrt n\).

The displayed expansion of \(\widehat\delta^{(3)\prime\prime}\) in A is correct: its first term is
\((\phi'^2+2h^{(3)}\phi'')\odot z^{(3)\prime}\).
The squared-velocity term is controlled by
\(\frac{\|v\odot v\|_2}{\sqrt n}\le\sqrt n\,\frac{\|v\|_2^2}{n}\).
Differentiating \(\widehat x^{(1)\prime}\) and using \(\widehat h^{(1)}=\chi(\widehat x^{(1)})\) gives the same bound for \(\widehat h^{(1)\prime\prime}\).
All these bounds are on the specified active events.

For completeness, the a.e. acceleration bounds suffice because the paths being interpolated are absolutely continuous. A locally Lipschitz finite-dimensional vector field composed with its trajectory is locally Lipschitz in time; the finite interval bounds then give this regularity globally on that interval. The smooth feature maps and the Lipschitz composition with \(\tau\) preserve the needed absolute continuity. No derivative of order two of \(\tau\) is invoked.

Thus the normalized derivative-query interpolation error on a mesh of size at most \(1/n\) is \(C/\sqrt n\); the value-query interpolation error is \(C/n\). The coefficient paths in A(18) have bounded operator norms and a.e. operator derivatives \(C\sqrt n\), giving the same \(C/\sqrt n\) interpolation loss. This checks the positive-time grid step directly at \(G^{(4)}/n\).

## 3. Simultaneous Gaussian events and adaptive inputs

The deterministic moduli used throughout are
\[
h(p)=p\log(e/p),\quad
\mu(d)=d\sqrt{1+\log_+(1/d)},\quad
\Phi(y)=y[1+\tfrac12\log_+(1/y)],
\]
with zero values at zero. All three are nondecreasing on their respective domains, and \(h\) is concave on \([0,1]\). For the product state norm
\[
y_E=\frac{\|\Delta x^{(1)}\|_2^2}{n}+\|\Delta W^{(2)}\|_{\rm F}^2
+\|\Delta W^{(3)}\|_{\rm F}^2+\frac{\|\Delta W^{(4)}\|_2^2}{n},
\]
the sum distance
\[
d_E=\frac{\|\Delta x^{(1)}\|_2}{\sqrt n}+\|\Delta W^{(2)}\|_{\rm op}
+\|\Delta W^{(3)}\|_{\rm op}+\frac{\|\Delta W^{(4)}\|_2}{\sqrt n}
\]
satisfies \(d_E\le2\sqrt{y_E}\) and \(\mu(d_E)^2\le4\Phi(y_E)\). The latter uses \(\mu(2v)\le2\mu(v)\); it does not require concavity of \(\Phi\).

For a Gaussian deleted block \(G\) with entries of variance \(1/n\), and an independent matrix \(C\) with \(\|C\|_{\rm op}\le K\), each fixed unit bilinear form of \(GCP_F\) has variance at most \(K^2/n\). Two \(1/4\)-nets, with cardinalities at most \(9^{|E|}\) and \(9^{|F|}\), and the operator approximation factor two give
\[
\mathbb P(\|GCP_F\|_{\rm op}>x\mid\text{active data})
\le2\,9^{|E|+|F|}e^{-nx^2/(8K^2)}.
\tag{R6}
\]
For an independent vector \(v\), the coordinates of \(Gv\) are independent centered Gaussians of variance \(\frac{\|v\|_2^2}{n}\le K^2\). The identity
\(\mathbb E\exp(\sum_{j=1}^m Z_j^2/4)=2^{m/2}\) implies
\[
\mathbb P(\frac{\|Gv\|_2^2}{n}>4K^2(m+u)/n\mid\text{active data})\le e^{-u}.
\tag{R7}
\]

For independent signed diagonal \(D\), \(|D_{jj}|\le K\), a fixed unit quadratic form of \(GDG^T-(\operatorname{Tr}D/n)I\) is
\[
n^{-1}\sum_jD_{jj}(Z_j^2-1).
\]
Its log moment generating function is at most \(2\lambda^2K^2/n\) for \(|\lambda|\le n/(4K)\), by expanding
\(-\lambda D_{jj}/n-\tfrac12\log(1-2\lambda D_{jj}/n)\).
Taking both signs of \(\lambda\), followed by a \(1/4\)-net of the \(m\)-dimensional sphere, yields the cited threshold
\[
16K(\sqrt{u/n}+u/n)
\quad\text{with failure at most }2\,9^m e^{-u}.
\tag{R8}
\]
These arguments prove the specialized probability inequalities used; no transferred positive-time Gaussian law for the actual path is assumed.

Take a deterministic grid containing \(0,S\), with gaps at most \(1/n\) and \(N\le\lceil nS\rceil+1\). The subset count \(\binom nm\le(en/m)^m\), both size sums where needed, and this grid give the advertised common event. More explicitly, each of A's eight groups can have failure at most \(\eta/8\):

| Group | Sufficient logarithmic cost, apart from subset entropies and net sizes |
| --- | --- |
| Four top coefficient families together | \(\log(64n^2N/\eta)\) |
| Pruned top derivative query | \(\log(8nN/\eta)\) |
| Incoming velocity query | \(\log(8nN/\eta)\) |
| Residual: three subevents, each with budget \(\eta/24\) | at most \(\log(48n^2N/\eta)\) |
| Pruned top value query | \(\log(8nN/\eta)\) |
| Incoming reference amplitude | \(\log(8n/\eta)\) |
| Optional signed top Gram | \(\log(16nN/\eta)\) |
| Actual initial-query bound | \(\log(8n/\eta)\) |

Consequently
\[
b_n=\log(512n^2N/\eta)/n,\qquad
\epsilon_n=\sqrt{b_n}+b_n+n^{-1/2}
\]
dominate all required width and interpolation costs. There is no omitted additional exponential family. Events for different subsets, times, or groups need not be independent. The event is for one prescribed \(\tau\), with constants independent of that choice; it is not simultaneous over the collection of all clippings.

For \(G=P(W^{(3)}_0)^T\), the four coefficient paths are
\[
I,\quad \widehat B\widehat W^{(3)}Q,\quad
\widehat B\widehat W^{(3)}Q\widehat D_2\widehat W^{(2)},\quad
\widehat B\widehat W^{(3)}Q\widehat D_2\widehat A_2Q.
\]
Each is measurable in \(\mathcal F_E^{\rm top}\): all upper matrix factors have right projection \(Q\), and the full incoming matrix contains no deleted top column. Their selected versions satisfy the bounds required by R6. The incoming coefficient
\(\widehat D_1^2(\widehat W^{(2)})^TQ\) is instead measurable in \(\mathcal F_E^{\rm in}\), as required for \(G=PW^{(2)}_0\).

For adaptive input \(v\) with \(\frac{\|v\|_2}{\sqrt n}\le K\), \(\frac1n\sum_i|v_i|\le\ell\le K\), assume first \(K,\ell>0\), sort the coordinates, and partition into blocks \(B_j\) of size \(k=\lceil n(\ell/K)^2\rceil\), with the last block possibly smaller. Write \(\|u\|_1=\sum_i|u_i|\), the ordinary \(\ell^1\) norm. Then
\[
\frac{\|P_{B_1}v\|_2}{\sqrt n}\le K,\qquad
\frac{\|P_{B_j}v\|_2}{\sqrt n}
\le\frac{\|P_{B_{j-1}}v\|_1}{\sqrt{kn}}\quad(j\ge2),
\]
and consequently
\[
\sum_j\frac{\|P_{B_j}v\|_2}{\sqrt n}
\le K+\sqrt{n/k}\ell\le2K.
\]
Applying the simultaneous restricted-column bound blockwise gives
\[
\frac{\|GC_jv\|_2}{\sqrt n}
\le C\{K[\sqrt{h(p)}+\epsilon_n]
+\ell\sqrt{\log(eK/\ell)}\}.
\tag{R9}
\]
Indeed \(h(k/n)\le h((\ell/K)^2)+h(1/n)\), and
\(K\sqrt{h((\ell/K)^2)}\le\sqrt2\,\ell\sqrt{\log(eK/\ell)}\).
The ceiling term is covered by \(b_n\). If \(K=0\) or \(\ell=0\), the input is zero. This step is deterministic on the common event, so adaptive inputs and subsequent adaptive subsets are allowed.

The adaptive-diagonal estimate is also independent of the trained gate's law. Apply R6 with the identity coefficient to all submatrices of \(W^{(2)}_0\), square the bound, and use the layer-cake representation for a diagonal \(a\in[-1,1]^n\). The Loewner domination by \(|a|\) and concavity of \(h\) give
\[
\|G\operatorname{diag}(a)G^T\|_{\rm op}
\le C\{h(p)+h(n^{-1}\sum_j|a_j|)+b_n\}.
\]
In particular, if \(a\) is the square of the entries of \(D_1^2-\widehat D_1^2\), its mean is at most \(\min(1,16d_E^2)\). Factoring the squared rectangular operator norm yields
\[
\|PW^{(2)}_0(D_1^2-\widehat D_1^2)\|_{\rm op}
\le C[\sqrt{h(p)}+\mu(d_E)+\epsilon_n].
\tag{R10}
\]
The square of the gate difference is essential for this modulus. No independent-gate substitution has occurred.

## 4. Residual and actual derivative: exact algebra and retained self-return

Define
\[
A_2=\frac{\|h^{(1)}\|_2^2}{n}I+W^{(2)}D_1^2(W^{(2)})^T,\qquad
\alpha_E=\frac{\|\widehat h^{(1)}\|_2^2}{n}+
\operatorname{Tr}(\widehat D_1^2)/n.
\]
The lower scalar satisfies \(1/4\le\alpha_E\le c^2+1\). For \(|z|\le1\), \(\phi'(z)^2\ge1/4\); for \(|z|>1\), \(\phi(z)^2>(\pi/4)^2>1/4\). Averaging this pointwise inequality gives the lower bound without a concentration or moment premise.

Subtracting the primal maps, with all top readouts bounded by \(R\), gives
\[
\frac{\|Q(z^{(2)}-\widehat z^{(2)})\|_2}{\sqrt n}\le Cd_E,\quad
\frac{\|h^{(2)}-\widehat h^{(2)}\|_2}{\sqrt n}\le Cd_E+c\sqrt p,
\]
\[
\frac{\|z^{(3)}-\widehat z^{(3)}\|_2}{\sqrt n}+
\frac{\|\delta^{(3)}-\widehat\delta^{(3)}\|_2}{\sqrt n}+
\frac{\|q^{(2)}-\widehat q^{(2)}\|_2}{\sqrt n}\le C(d_E+\sqrt p).
\tag{R11}
\]
For example, the backward gate difference obeys
\[
\frac{\|\delta^{(3)}-\widehat\delta^{(3)}\|_2}{\sqrt n}
\le\frac{\|\Delta W^{(4)}\|_2}{\sqrt n}
+2R\frac{\|\Delta z^{(3)}\|_2}{\sqrt n}.
\]
There is no additive mismatch from initial readout values. The analogous diagonal-vector estimate for \(B-\widehat B\) follows from \(|\phi''|\le2\), \(|\phi'''|\le8\).

Write \(G_2=PW^{(2)}_0=P\widehat W^{(2)}\). Keeping the layer-indexed matrices, the off-block maps have the exact difference
\[
\begin{split}
PW^{(2)}D_1^2(W^{(2)})^TQ
-G_2\widehat D_1^2(\widehat W^{(2)})^TQ
={}&P(W^{(2)}-\widehat W^{(2)})D_1^2(W^{(2)})^TQ\\
&+G_2(D_1^2-\widehat D_1^2)(W^{(2)})^TQ\\
&+G_2\widehat D_1^2(W^{(2)}-\widehat W^{(2)})^TQ.
\end{split}
\]
The first and last terms cost \(Cd_E\), and R10 bounds the middle term. Set
\[
v_E=Q(D_2-\widehat D_2)\tau(\widehat q^{(2)}).
\]
Then \(\frac{\|v_E\|_2}{\sqrt n}\le C\), \(\frac1n\sum_i|v_{E,i}|\le Cd_E\), by R11 and Cauchy--Schwarz. The exact backward difference on the active coordinates is
\[
Q(\delta^{(2)}-\widehat\delta^{(2)})
=QD_2[\tau(q^{(2)})-\tau(\widehat q^{(2)})]+v_E.
\]
The off-block residual is precisely the three terms in A(23): operator difference times \(Q\delta^{(2)}\), reference operator times the contractive query difference, and reference operator times \(v_E\). R10, R11, and R9 bound these, respectively.

The same matrix expansion with right \(P\), plus R8 for the independent lower reference diagonal, proves the self-block comparison. Together,
\[
\rho_E=(PA_2P-\alpha_EP)\delta^{(2)}
+PA_2Q\delta^{(2)}-\widehat g_E,\qquad
\frac{\|\rho_E\|_2}{\sqrt n}\le C[\sqrt{h(p)}+\epsilon_n+\mu(d_E)].
\tag{R12}
\]
Here \(\widehat g_E=PW^{(2)}_0\widehat h^{(1)\prime}\).
This proof uses neither a derivative bound for the actual query nor a small-distance premise.

Differentiating the actual query gives exactly
\[
q^{(2)\prime}=h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}+
(W^{(3)})^T\delta^{(3)\prime}.
\]
The learned rare top columns have Frobenius norm at most \(cRS\sqrt p\). Thus
\[
Pq^{(2)\prime}=G\delta^{(3)\prime}+r,\quad
\frac{\|r\|_2}{\sqrt n}\le C\sqrt p,\qquad G=P(W^{(3)}_0)^T.
\tag{R13}
\]
The pruned query instead satisfies \(P\widehat q^{(2)\prime}=G\widehat\delta^{(3)\prime}\), since its rare columns are frozen. R7 and the derivative grids give
\[
\frac{\|P\widehat q^{(2)\prime}\|_2+\|\widehat g_E\|_2}{\sqrt n}
\le C(\sqrt{h(p)}+\epsilon_n).
\]

Put \(U=h^{(2)\prime}\), \(\widehat U=\widehat h^{(2)\prime}\). The telescoping in A(25) is exact:
\[
\delta^{(3)\prime}-\widehat\delta^{(3)\prime}
=r_{\rm sm}+(B-\widehat B)z^{(3)\prime}
+\widehat B\widehat W^{(3)}PU
+\widehat B\widehat W^{(3)}Q(U-\widehat U).
\]
The stated remainder satisfies \(\|r_{\rm sm}\|_2/\sqrt n\le C(d_E+\sqrt p)\). For \(u_0=(B-\widehat B)z^{(3)\prime}\), one has
\[
\frac{\|u_0\|_2}{\sqrt n}\le C,\qquad
\frac1n\sum_i|u_{0,i}|\le C(d_E+\sqrt p),
\]
so R9 with the identity coefficient applies.

The self-return is \(G\widehat BG^TPU\). It is not conditionally Gaussian with an independent coefficient. The deterministic bound
\[
\frac{\|G\widehat BG^TPU\|_2}{\sqrt n}\le C\frac{\|PU\|_2}{\sqrt n}
\]
and the exact identity
\[
Pz^{(2)\prime}=\alpha_EP\delta^{(2)}+\widehat g_E+\rho_E
\tag{R14}
\]
give the retained \(C\frac{\|P\delta^{(2)}\|_2}{\sqrt n}\) term. No sign or positive-energy assumption about \(\widehat B\) is used.

For the bulk term the exact expansion is
\[
Q(U-\widehat U)
=Q(D_2-\widehat D_2)A_2\delta^{(2)}
+Q\widehat D_2(A_2-\widehat A_2)\delta^{(2)}
+Q\widehat D_2\widehat A_2(\delta^{(2)}-\widehat\delta^{(2)}).
\]
Expanding \(A_2-\widehat A_2\) leaves exactly three exceptional inputs:
\[
Q(D_2-\widehat D_2)A_2\delta^{(2)},\quad
(D_1^2-\widehat D_1^2)(W^{(2)})^T\delta^{(2)},\quad
v_E.
\]
Their outer coefficients are the \(C_1,C_2,C_3\) families, respectively. Each such input \(v\) satisfies
\[
\frac{\|v\|_2}{\sqrt n}\le C,\qquad
\frac1n\sum_i|v_i|\le Cd_E.
\]
All remaining factors are controlled in operator norm and cost \(C(d_E+\sqrt p)\) or \(C\frac{\|P\delta^{(2)}\|_2}{\sqrt n}\) in the output Euclidean norm divided by \(\sqrt n\).
The elementary inequality \(\mu(d+\sqrt p)\le C[\mu(d)+\sqrt{h(p)}]\) follows from monotonicity, \(\mu(2x)\le2\mu(x)\), and \(\mu(\sqrt p)^2\le h(p)\).

Consequently A(6) follows in full:
\[
\frac{\|Pq^{(2)\prime}\|_2}{\sqrt n}
\le C[\frac{\|P\delta^{(2)}\|_2}{\sqrt n}+\sqrt{h(p)}+\epsilon_n+\mu(d_E)].
\tag{R15}
\]
The dependency order is noncircular: deterministic bounds and reference Gaussian events give the residual; the residual then gives the actual derivative; the energy argument below subsequently controls its retained rare action.

## 5. The nonzero integration-by-parts boundary and exact prefix powers

Let \(q_E=Pq^{(2)}\), \(u_E=P\tau(q^{(2)})\), \(h_E=P\phi(z^{(2)})\), \(\delta_E=P\delta^{(2)}\), and \(r_E=\widehat g_E+\rho_E\). Coordinatewise multiplication and R14 give
\[
\frac{(u_E)^T(h_E')}{n}
=\alpha_E\frac{\|\delta_E\|_2^2}{n}+\frac{(\delta_E)^T(r_E)}{n}.
\]
Here \(\frac{\|h_E\|_2}{\sqrt n}\le c\sqrt p\), \(\frac{\|u_E'\|_2}{\sqrt n}\le\frac{\|q_E'\|_2}{\sqrt n}\) a.e., and
\(\frac{\|u_E(0)\|_2^2}{n}\le I_E:=\frac{\|Pq^{(2)}(0)\|_2^2}{n}\).
No sign preservation or monotonicity of \(\tau\) is required: the coercive term is \(\frac{\|D_2u_E\|_2^2}{n}\).

Integration by parts includes both endpoints:
\[
\int_0^t\alpha_E\frac{\|\delta_E\|_2^2}{n}
=\frac{(u_E(t))^T(h_E(t))}{n}-\frac{(u_E(0))^T(h_E(0))}{n}
-\int_0^t[\frac{(u_E')^T(h_E)}{n}+\frac{(\delta_E)^T(r_E)}{n}].
\]
Decompose the endpoint difference as
\[
\frac{(u_E(t)-u_E(0))^T(h_E(t))}{n}
+\frac{(u_E(0))^T(h_E(t)-h_E(0))}{n}.
\]
The first term and the \(u_E'\) integral together cost at most
\(2c\sqrt p\int_0^t\frac{\|q_E'\|_2}{\sqrt n}\).
The new boundary term is exactly
\[
\int_0^t\frac{(u_E(0))^T(D_2(s)[\alpha_E(s)\delta_E(s)+r_E(s)])}{n}\,ds.
\tag{R16}
\]
This is the crucial time-integrated repair. Estimating the two original endpoints separately would not justify the stated prefix dependence.

With \(A(s)=\frac{\|\delta_E(s)\|_2}{\sqrt n}\) and
\(w(s)=\sqrt{h(p)}+\epsilon_n+\mu(d_E(s))\), R12 and R15 give
\[
\tfrac14\int_0^t A^2
\le C\int_0^t[\sqrt p\,A+\sqrt p\,w+Aw+\sqrt{I_E}A+\sqrt{I_E}w].
\]
Young's inequality absorbs the three terms containing \(A\) into, for example, \(\tfrac18\int A^2\). The other terms cost \(C(p+w^2+I_E)\). Since \(p\le h(p)\),
\[
\int_0^t\frac{\|\delta_E\|_2^2}{n}
\le C J_E(t),\qquad
J_E(t)=t[h(p)+\epsilon_n^2+I_E]
+\int_0^t\mu(d_E(s))^2\,ds.
\tag{R17}
\]
Squaring R15 and R14 gives the same bound for the integrals of \(\frac{\|Pq^{(2)\prime}\|_2^2}{n}\) and \(\frac{\|Pz^{(2)\prime}\|_2^2}{n}\). This checks A(7), including the extra \(CtI_E\).

For a scalar absolutely continuous path,
\(\sup_{s\le t}|v(s)-v(0)|^2\le t\int_0^t|v'|^2\).
Apply this separately to each coordinate and then average. Therefore
\[
\frac{\|Pq_*^{(2)}(t)\|_2^2}{n}
\le2I_E+C\{t^2[h(p)+\epsilon_n^2+I_E]
+t\int_0^t\mu(d_E(s))^2\,ds\},
\tag{R18}
\]
and the preactivation displacement has the same right side without \(2I_E\). An unsplit bound is
\[
\frac{\|Pq_*^{(2)}(t)\|_2}{\sqrt n}\le\sqrt{I_E}+\sqrt{CtJ_E(t)}.
\]
It is exact at \(t=0\). No exchange of a coordinatewise supremum with an empirical average is used. The leftover initial contribution in the additive bound is \((2+Ct^2)I_E\); it is not a \(t^2\)-only error.

For a pruned query the derivative-query estimate likewise gives
\(\frac{\|P\widehat q_*^{(2)}(t)\|_2^2}{n}\le2\widehat I_E+Ct^2[h(p)+\epsilon_n^2]\).
The deterministic estimate \(\widehat I_E\le4M^2/n^2\) is valid. The actual and pruned initial queries are generally different because their top preactivations differ.

## 6. Conditional initial covariance, all-set mass, and the width floor

Let \(\mathcal H\) contain all hidden initialization. It contains \(z^{(3)}_0\) and is independent of \(G^{(4)}\). Conditional on \(\mathcal H\),
\[
q^{(2)}(0)\sim N(0,\Sigma_0),\qquad
\Sigma_0=n^{-2}(W^{(3)}_0)^T
\operatorname{diag}(\phi'(z^{(3)}_0)^2)W^{(3)}_0.
\]
On \(\Omega_M\), \(\Sigma_0\preceq M^2n^{-2}I\).
This computation allows the actual gate to depend on all hidden weights. It asserts no independence between query coordinates.

To construct an unconditional success event, select
\(\widetilde q_0=\mathbf1_{\Omega_M}q^{(2)}(0)\).
The indicator is \(\mathcal H\)-measurable. Its conditional law is either the above Gaussian or zero. For a fixed set of size \(m\), the conditional covariance eigenvalues \(\lambda_j\) lie in \([0,M^2/n^2]\), so
\[
\mathbb E\left[e^{n^2\|P\widetilde q_0\|_2^2/(4M^2)}
\mid\mathcal H\right]
=\prod_{j=1}^m(1-n^2\lambda_j/(2M^2))^{-1/2}\le2^{m/2}.
\]
Markov's inequality gives the threshold
\[
\frac{\|P\widetilde q_0\|_2^2}{n}>
\frac{4M^2}{n^2}\frac{m+u}{n}
\quad\text{with probability at most }e^{-u}.
\]
Choose \(u=m\log(en/m)+\log(8n/\eta)\), union over all sets of each size and then all \(m=1,\ldots,n\). The failure is at most \(\eta/8\), and on its intersection with \(\Omega_M\),
\[
I_E\le\frac{8M^2}{n^2}
\left[h(p)+\frac{\log(8n/\eta)}n\right]
\le\frac{8M^2}{n^2}[h(p)+\epsilon_n^2].
\tag{R19}
\]
For the empty set \(I_E=0\). The deterministic bound
\(\frac{\|q^{(2)}(0)\|_2}{\sqrt n}\le2M/n\) on \(\Omega_M\cap\Omega_4\) is also correct, but by itself would not supply the mass dependence in R19.

The conditional Gaussian proof precedes imposing \(\Omega_4\). Conditioning on \(\Omega_4\) first would truncate \(G^{(4)}\); the candidate avoids that error. Conversely, using \(\Omega_4\) in the reference-path selections is valid because the deleted hidden block remains independent of the entire active sigma field. These two conditional arguments use different random blocks and are compatible.

Define
\[
Y_r(s)=\max_{|E|\le\lfloor nr\rfloor}y_E(s),\qquad
M_r(t)=\max_{|E|\le\lfloor nr\rfloor}\frac{\|P_Eq_*^{(2)}(t)\|_2^2}{n}.
\]
They are both zero for \(r<1/n\). R18 and R19 imply, for \(r\ge1/n\),
\[
M_r(t)\le C\left[
(t^2+n^{-2})\{h(r)+\epsilon_n^2\}
+t\int_0^t\Phi(Y_r(s))\,ds
\right].
\tag{R20}
\]
Indeed the initial terms are bounded by
\(Cn^{-2}(1+t^2)[h(r)+\epsilon_n^2]\), and
\(t^2n^{-2}\le t^2\). Moving the maximum inside the nonnegative integral only enlarges the bound. The constants remain dependent only on \(S,M\).

Thus A(35) retains exactly the \(t^2+n^{-2}\) prefix coefficient and the factor \(t\) preceding the distance history. The integer floor is correct and does not mean a fractional selection of mass less than \(1/n\) has zero value.

## 7. Full-state inequality and actual weighted-gate replacement

Subtract the two lower updates using the exact decomposition
\[
\delta^{(2)}-\widehat\delta^{(2)}
=P\delta^{(2)}
+QD_2[\tau(q^{(2)})-\tau(\widehat q^{(2)})]+v_E.
\]
R3 and R11 control the rank-product differences and the top updates. The result is the velocity bound
\[
\left[
\frac{\|\Delta x^{(1)\prime}\|_2^2}{n}
+\|\Delta W^{(2)\prime}\|_{\rm F}^2
+\|\Delta W^{(3)\prime}\|_{\rm F}^2
+\frac{\|\Delta W^{(4)\prime}\|_2^2}{n}
\right]^{1/2}
\le C[\sqrt{y_E}+\sqrt p+\frac{\|P\delta^{(2)}\|_2}{\sqrt n}+\frac{\|v_E\|_2}{\sqrt n}].
\tag{R21}
\]
For example the lower matrix term is
\((\delta^{(2)}-\widehat\delta^{(2)})(h^{(1)})^T/n
+\widehat\delta^{(2)}(h^{(1)}-\widehat h^{(1)})^T/n\).
Its Frobenius norm has precisely the normalization in R3.

Differentiating the explicit four-term definition of \(y_E\) and applying Cauchy--Schwarz bounds its derivative by \(2\sqrt{y_E}\) times the left side of R21. Apply Young's inequality to the rare-action and \(\sqrt p\) products, but retain \(\sqrt{y_E}\frac{\|v_E\|_2}{\sqrt n}\). Integrate R17 and use \(\mu(d_E)^2\le4\Phi(y_E)\), \(\Phi(y_E)\ge y_E\). This proves A(38):
\[
y_E(t)\le C\left[
t(h(p)+\epsilon_n^2+I_E)
+\int_0^t\Phi(y_E(s))\,ds
+\int_0^t\sqrt{y_E(s)}\frac{\|v_E(s)\|_2}{\sqrt n}\,ds
\right].
\tag{R22}
\]
Its new initial-query contribution is \(CtI_E\), and its initial state remains zero. R19 absorbs this contribution into the first term, giving R2.

Let
\[
\omega_{E,i}=\mathbf1_{i\notin E}
|\phi'(z_i^{(2)})-\phi'(\widehat z_i^{(2)})|^2,\qquad
a_E=n^{-1}\sum_i\omega_{E,i}.
\]
The gates lie in \([0,1]\), so \(0\le\omega_{E,i}\le1\).
Lipschitz continuity of \(\phi'\), R11, and \(d_E^2\le4y_E\) yield
\(a_E\le A(y_E)=\min(1,C_0y_E)\) for a fixed \(C_0\ge1\).
Add and subtract \(\tau(q^{(2)})\) in \(v_E\). Contractivity and domination give
\[
\frac{\|v_E(t)\|_2^2}{n}
\le\frac2n\sum_i\omega_{E,i}(t)q_{*,i}^{(2)}(t)^2
+C[y_E(t)+p].
\tag{R23}
\]
This step uses the actual query and requires no independence of the weights from the query and no second-pruned reference.

## 8. Accumulated relative consequence: amplitude and both rank-memory identities

This section checks A's additional assertion at lines 863–873, including the complete route to SINGLE_PRUNED_OFFBLOCK_OSGOOD.md, equation (28). It is not being granted merely because the final fractional algebra works.

Set
\[
e=Pz^{(2)}-PW^{(2)}_0\widehat h^{(1)},\qquad
\beta=1/\alpha_E,\qquad W_E=PW^{(2)}.
\]
The frozen incoming rows and shared initial \(h^{(1)}\) give \(e(0)=0\), even at nonzero readout. R14 yields
\[
e'=\alpha_E\delta_E+\rho_E,\qquad
\delta_{E,i}=\phi'(\widehat z_{E,i}+e_i)\tau(q_i^{(2)}).
\tag{R24}
\]
Bounds on the reference velocities give
\[
|\alpha_E'|\le2c\frac{\|\widehat h^{(1)\prime}\|_2}{\sqrt n}
+4\frac{\|\widehat z^{(1)\prime}\|_2}{\sqrt n}\le C.
\]
Coercivity therefore bounds \(\beta,\beta'\). This requires no derivative of the readout boundary.

For each rare coordinate put
\[
B_i=\sup_{s\le S}|\widehat z_{E,i}(s)|,\quad
R_i=\int_0^S|\rho_{E,i}(s)|\,ds,\quad
Q_i=\int_0^S\alpha_E(s)|\tau(q_i^{(2)}(s))|\,ds.
\]
The scalar argument in DIRECT_SCALAR_PRUNED_REDUCTION.md applies to R24 with the clipped control itself. To verify it, write \(r_i(t)=\int_0^t\rho_{E,i}\), \(\xi_i=e_i-r_i\), and \(K_i=B_i+R_i\). For \(w_i=(|\xi_i|-K_i)_+\), whenever \(w_i>0\),
\[
|\xi_i+r_i+\widehat z_{E,i}|\ge w_i,\qquad
w_i'\le\frac{\alpha_E|\tau(q_i^{(2)})|}{1+w_i^2}.
\]
The positive-part chain rule gives the same differential inequality almost everywhere, including its zero set. Since \(w_i(0)=0\), \(F(w_i)\le Q_i\), hence
\[
\sup_{s\le S}|e_i(s)|\le B_i+2R_i+(3Q_i)^{1/3}.
\tag{R25}
\]
Hölder on the empirical measure of \(E\) gives
\[
\left(\frac1n\sum_{i\in E}Q_i^{2/3}\right)^{1/2}
\le p^{1/3}\left(\frac1n\sum_{i\in E}Q_i^2\right)^{1/6}
\le p^{1/3}\left(\int_0^S\alpha_E\frac{\|P\tau(q^{(2)})\|_2}{\sqrt n}\,ds\right)^{1/3}.
\]
The last integral is bounded by R4. There is no zero-query premise here.

The reference amplitude in R25 has the independent Gaussian proof required for event group 6. Conditional on \(\mathcal F_E^{\rm in}\), a dominating variable for \(B_i\) is
\[
\mathcal B_i=
|(W^{(2)}_0\widehat h^{(1)}(0))_i|
+\int_0^S|(W^{(2)}_0\widehat h^{(1)\prime}(s))_i|\,ds.
\]
The selected coefficient path is independent of the deleted row and satisfies
\(\frac{\|\widehat h^{(1)}(0)\|_2}{\sqrt n}+\int_0^S\frac{\|\widehat h^{(1)\prime}\|_2}{\sqrt n}\le C\).
Gaussian moments and Minkowski's inequality yield
\(\big(\mathbb E[\mathcal B_i^r\mid\mathcal F_E^{\rm in}]\big)^{1/r}\le C\sqrt r\), \(r\ge2\).
This implies an exponential square moment at a fixed larger constant: expanding the exponential and using
\(\mathbb E\mathcal B_i^{2k}\le C^{2k}(2k)^k\) and
\(k!\ge(k/e)^k\), one can choose \(K^2\ge4eC^2\) to obtain
\(\mathbb E e^{\mathcal B_i^2/K^2}\le2\).
The variables \(\mathcal B_i\), \(i\in E\), are conditionally independent because each uses a different deleted Gaussian row with the same fixed coefficient path.

The exponential product bound and the all-set union bound therefore give
\[
\frac1n\sum_{i\in E}B_i^2
\le C\left[h(p)+p\log2+\frac{\log(8n/\eta)}n\right].
\]
This controls the coordinatewise time supremum before taking its norm; no illegitimate supremum interchange occurs. Combining it with R25 and R12 gives
\[
E_*:=\sup_{t\le S}\frac{\|e(t)\|_2}{\sqrt n}
\le C\left[p^{1/3}+\sqrt{h(p)}+\epsilon_n+
\int_0^S\mu(d_E(s))\,ds\right].
\tag{R26}
\]
It also has a uniform deterministic bound, since each of the two preactivation vectors defining \(e(t)\) has Euclidean norm divided by \(\sqrt n\) bounded by \(C\) on the full operator event.

The two integration-by-parts identities, with every normalization explicit, are
\[
W_E(t)-W_E(0)
=\frac{\beta(t)e(t)(h^{(1)}(t))^T}{n}
-\int_0^t\frac{e((\beta h^{(1)})')^T}{n}\,ds
-\int_0^t\frac{\beta\rho_E(h^{(1)})^T}{n}\,ds
\tag{R27}
\]
and
\[
\begin{split}
\int_0^tW_E^T\delta_E\,ds
={}&\beta W_E^Te-\tfrac12\beta^2h^{(1)}\frac{\|e\|_2^2}{n}
-\int_0^t\beta'W_E^Te\,ds\\
&+\tfrac12\int_0^t(\beta^2h^{(1)})'\frac{\|e\|_2^2}{n}\,ds
+\int_0^t\beta^2h^{(1)}\frac{(\rho_E)^T(e)}{n}\,ds
-\int_0^t\beta W_E^T\rho_E\,ds.
\end{split}
\tag{R28}
\]
The displayed endpoint terms are evaluated at \(t\). Both initial endpoint terms vanish because \(e(0)=0\).

To check the nontrivial signs and scaling in R28, use
\[
(W_E^T)'=h^{(1)}\delta_E^T/n,\qquad
\frac{(\delta_E)^T(e)}{n}
=\tfrac\beta2(\frac{\|e\|_2^2}{n})'-\beta\frac{(\rho_E)^T(e)}{n}.
\]
Starting with \(\int\beta W_E^Te'\), its integration by parts contributes
\(-\int\beta h^{(1)}\frac{(\delta_E)^T(e)}{n}\).
Substitution gives the negative quadratic endpoint and the two positive integrals displayed in R28. Thus the signs are correct, and no boundary involving \(q^{(2)}(0)\) is missing.

Let \(R_1=\int_0^S\frac{\|\rho_E\|_2}{\sqrt n}\). R3 and the bounded coefficients give
\[
\sup_{t\le S}\|W_E(t)-W_E(0)\|_{\rm F}\le C(E_*+R_1),
\]
\[
\sup_{t\le S}\frac{\|\int_0^tW_E^T\delta_E\|_2}{\sqrt n}
\le C[E_*+E_*^2+(1+E_*)R_1]\le C(E_*+R_1).
\]
Using R26 and the integrated residual proves the asserted accumulated estimate, with \(\widetilde\nu_n\) taken to be \(\epsilon_n\) after enlarging the outer constant. In particular it vanishes for \(\eta=1/n\). This consequence is valid at the prescribed nonzero readout, and it remains relative to \(\int\mu(d_E)\).

## 9. Fractional interpolation, mass replacement, and absorption

On the common event, fix \(t\), and sort the nonnegative numbers \(q_{*,i}^{(2)}(t)^2\) as \(b_1\ge\cdots\ge b_n\). Set \(B_j=n^{-1}\sum_{i\le j}b_i\), with \(B_0=0\). For \(0<a<1\), \(na=k+\theta\), and weights in \([0,1]\) summing to \(na\),
\[
\sum_iw_ib_i=(k+\theta)b_{k+1}+\sum_iw_i(b_i-b_{k+1})
\le\sum_{i\le k}b_i+\theta b_{k+1}.
\]
The terms with \(i>k+1\) are nonpositive and the positive terms have weights at most one. Thus the normalized weighted sum is bounded by \((1-\theta)B_k+\theta B_{k+1}\). The cases \(a=0,1\) use \(B_0,B_n\) directly.

Because the \(b_i\) are nonnegative, \(B_j=M_{j/n}(t)\). Apply R20 only at positive nodes and retain \(B_0=0\) exactly. Concavity of \(h\) gives
\[
(1-\theta)h(k/n)+\theta h((k+1)/n)\le h(a).
\]
The interpolated width coefficient is
\((1-\theta)\mathbf1_{\{k\ge1\}}+\theta=\min(1,na)\).
The history coefficient is
\[
\mathcal I_n(a,u)=(1-\theta)\Phi(Y_{k/n}(u))
+\theta\Phi(Y_{(k+1)/n}(u)),
\]
with the endpoint convention \(\mathcal I_n(1,u)=\Phi(Y_1(u))\). This proves R1, exactly as now printed in B(2). It does not prove the superseded product formula.

At \(0<a<1/n\), the history is exactly \(na\,\Phi(Y_{1/n}(u))\). Both the width factor and this history vanish at \(a=0\), but are retained for every positive fractional mass. At a fixed current time the mass \(a\) is held fixed throughout the integral over \(u\); no past-time mass is substituted.

For each \(u\), the node values \(\Phi(Y_{j/n}(u))\) are nonnegative and nondecreasing in \(j\). Their piecewise linear interpolation is therefore nonnegative and nondecreasing in \(a\). This does not require \(\Phi\) to be concave. All integer-subset estimates hold simultaneously, so the optimizing ordering and arbitrary weights may depend on the complete actual path.

Apply R1 to the gate weights in R23. This yields B(3):
\[
\frac{\|v_E(t)\|_2^2}{n}\le C\left[
y_E(t)+p_E+
(t^2+n^{-2})\{h(a_E(t))+\epsilon_n^2\min(1,na_E(t))\}
+t\int_0^t\mathcal I_n(a_E(t),u)\,du
\right].
\tag{R29}
\]
The entropy, width factor, and interpolated history are each nondecreasing in the mass, so replacing \(a_E(t)\) by \(A(y_E(t))=\min(1,C_0y_E(t))\) is legitimate.

For \(0<C_0y\le1\), let \(L=\log(1/y)\ge0\). Then
\[
h(C_0y)\le C_0y(1+L),\qquad
\sqrt{y\,h(C_0y)}
\le\sqrt{C_0}\,y\sqrt{1+L}
\le\sqrt{C_0}\,y(1+L/2)=\sqrt{C_0}\Phi(y).
\]
For \(C_0y\ge1\), \(h(A(y))=1\) and
\(\sqrt y\le\sqrt{C_0}y\le\sqrt{C_0}\Phi(y)\).
At zero both sides vanish. This verifies both A(40) and the stronger absorption used by B.

Take the square root termwise in R29 and multiply by \(\sqrt y\), where \(y=y_E(s)\). Since
\(\sqrt{s^2+n^{-2}}\le s+n^{-1}\le S+1\), the entropy is bounded by \(C\Phi(y)\), including its initial \(n^{-1}\) coefficient. Further,
\[
\sqrt{yp_E}\le(y+p_E)/2,\qquad
\epsilon_n\sqrt y\,\sqrt{\min(1,nA(y))}
\le(y+\epsilon_n^2)/2.
\]
The remaining history is preserved exactly, giving B(6):
\[
\sqrt y\frac{\|v_E(s)\|_2}{\sqrt n}\le C\left[
\Phi(y)+p_E+\epsilon_n^2+
\left\{ys\int_0^s\mathcal I_n(A(y),u)\,du\right\}^{1/2}
\right].
\tag{R30}
\]
Insert this into R2, which is the corrected B(5), and use \(p_E\le h(p_E)\). The result is the individual-set version of B(4).

For fixed \(s\), the expression
\[
y\longmapsto
\left\{ys\int_0^s\mathcal I_n(A(y),u)\,du\right\}^{1/2}
\]
is nondecreasing: every factor is nonnegative and the inner integral is nondecreasing in \(y\). Replace \(y_E(s)\) by \(Y_p(s)\), and \(h(p_E)\) by \(h(p)\), for every \(|E|\le\lfloor np\rfloor\). Taking the finite maximum proves
\[
\begin{split}
Y_p(t)\le C\bigg[
&t\{h(p)+\epsilon_n^2\}+\int_0^t\Phi(Y_p(s))\,ds\\
&+\int_0^t
\left\{Y_p(s)s\int_0^s
\mathcal I_n(A(Y_p(s)),u)\,du\right\}^{1/2}\,ds
\bigg].
\end{split}
\tag{R31}
\]
There is no differentiation of a maximizing subset and no choice of a single maximizer for all times. The envelopes are finite maxima of continuous time paths, so their time integrals are defined. For \(p<1/n\), the left side is zero. At \(t=0\), the state terms vanish while the corrected query estimate retains its initialization. This is the claimed fractional hierarchy for the final frozen candidates.

## 10. Remaining dependency checks, probability, and precise conclusion

The permitted dependencies' zero-readout assumptions were not imported as positive-time theorems. Their relevant algebra and probability proofs were checked and instantiated with the active fields and bounds proved above:

| Dependency | Audit disposition |
| --- | --- |
| PRUNED_GAUSSIAN_SUBSET_BOUND.md | Conditional vector law, norm selection, subset/time union, and net operator tail verified. The readout bounds were redone at the prescribed initialization. |
| PRUNED_RARE_BLOCK_GEOMETRY.md | Signed Gram moment bound, scalar center, lower coercivity, and grid losses verified. The optional top coefficient remains signed. |
| ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md | All-submatrix event and adaptive diagonal domination verified. The squared-gate use in the chain yields the stronger square-root logarithmic modulus needed here. |
| SINGLE_PRUNED_OFFBLOCK_OSGOOD.md | Restricted-column bounds, sorting, exact off-block residual, full residual, and accumulated consequence verified. The bulk vector is not declared small by its compressed estimate. |
| DIRECT_SCALAR_PRUNED_REDUCTION.md | Scalar comparison, rare displacement bound, Gaussian whole-reference amplitude, and both rank-memory identities verified, with explicit finite-width normalization. |
| ACTUAL_RARE_BACKWARD_DERIVATIVE.md | Active acceleration bounds, all four coefficients, pruned derivative queries, actual top telescoping, retained self-return, and three exceptional bulk inputs verified. |
| RARE_BACKWARD_ENERGY.md | The zero initial query is not carried over. Its integration by parts and whole-path argument are used only after the explicit nonzero-boundary repair. |
| ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md | State normalization, pair-velocity estimate, actual-query gate replacement, prefix factors, and finite width floor verified. The fractional argument has its own proof and does not assume closure of the older Hardy hierarchy. |

Two ancillary source calculations can be checked without adding dependencies. For the scalar flow-map identity, \(F(z)-F(\widehat z)=(z-\widehat z)L\), where
\[
L=1+\frac{z^2+z\widehat z+\widehat z^2}{3}
=1+\frac{(z+\widehat z)^2}{4}+\frac{(z-\widehat z)^2}{12}
\ge |z+\widehat z|.
\]
Thus the coefficient \((z+\widehat z)/L\) has magnitude at most one, and the stated reference-forcing propagator follows by variation of constants for an integrable scalar coefficient. This auxiliary identity is not used to erase the actual-state factor when forcings differ.

For the older Hardy representation, splitting at the mass \(a\) and substituting \(r=a/u\) gives, for nondecreasing \(J\) vanishing below \(1/n\),
\[
\int_0^1J(\min(1,a/u))\,du
=aJ(1)+a\int_{\max(a,1/n)}^1J(r)r^{-2}\,dr.
\]
The entropy integral is
\(a[1+\log(1/a)+\tfrac12\log^2(1/a)]\).
This confirms the source's discrete floor and its stated limitation. The corrected fractional proof uses the exact finite sorting inequality instead; no stronger conclusion about the Hardy operator is assumed.

The optional top signed Gram event has
\[
|\widehat W_i^{(4)}\phi''(\widehat z_i^{(3)})|\le2R,\qquad
\frac{\|(\widehat W^{(4)}\phi''(\widehat z^{(3)}))'\|_2}{\sqrt n}
\le2c+8RJ_3,
\]
where \(J_3=c^2R+K_3^2(c^2+K_2^2)R\). Its independence, derivative bound, and possibly negative scalar center are all consistent with R8. No coercivity is attributed to this top block.

The eight probability allocations total at most \(\eta\). The readout event has
\[
\mathbb P(\Omega_4^c)
\le e^{-(1-\frac12\log2)n}+2ne^{-n^2/2}.
\]
For the norm part, apply Markov's inequality to
\(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\) at threshold \(4n\).
For the maximum part, apply the Gaussian tail at threshold \(n\) and union over \(n\) coordinates. The hidden operator event remains separate. A two-sphere \(1/4\)-net with \(9^n\) points per sphere gives
\[
\mathbb P(\Omega_M^c)\le4e^{-(25/2-2\log9)n}\quad\text{when }M=10.
\]
It follows that the complete corrected chain has the stated common-event probability at least
\[
1-\eta-\mathbb P(\Omega_M^c)
-e^{-(1-\frac12\log2)n}-2ne^{-n^2/2}.
\tag{R32}
\]
No independence between the success events is needed, and the fractional step adds no event. With \(M=10,\eta=1/n\), the failure bound and \(\epsilon_n\) tend to zero.

All calculations apply to the actual and fully pruned networks with the same prescribed \(G^{(4)}/n\) initial readout and the same fixed clipping. The empty deletion is identical by finite-dimensional uniqueness; a full deletion is permitted and causes no denominator or active-block problem. The estimates are uniform over deletion sets and times on the common event, not over different clipping maps.

The conclusion is the scoped positive-time derivative, energy, prefix, state, fractional hierarchy, and accumulated relative estimates. The proof does not close the distance histories. In particular it does not establish deletion continuity, clipping removal, population restartability, or any global population theorem. Failure to derive those unclaimed conclusions is not a defect of this scoped chain.

## Freeze record

Final verdict: PASS for the complete corrected scoped chain, including the accumulated relative consequence. Required fixes remaining: none.

The report preserves the superseded initial corollary hash, the two resolved findings, their attribution to the supervising assistant, and the verified final candidate hashes. It uses ordinary vector and matrix norms with explicit empirical factors. The final report is frozen only after these corrections and the completed audit. Its SHA-256 is supplied separately in the final response and is not inserted into or appended to the report after hashing.
