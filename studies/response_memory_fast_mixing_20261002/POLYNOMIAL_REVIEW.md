# Internal audit of the finite polynomial transfer corollary

Date: 2026-10-02.

**Verdict: PASS for the mathematical corollary as stated.** The fixed-step
polynomial \(q=1\) construction is a valid application of the cited
alternating-tree universality result. The adaptive global coefficients,
square-root residual norm at zero, inverse clock, Gaussian spectral law,
initial roots, and same-side observable quantifiers are accounted for.
I found no unresolved mathematical application hypothesis or false
inference in that corollary.

This is an internal audit, not a fresh isolated promotion review. This
reviewer previously had controlled-flow review context in another study.
No result, argument, artifact, or scientific premise from that work was
used here. The present scientific inputs were only the frozen candidate
and the specified WZF primary source. The verdict does not validate the
tanh implementation, finite-precision calculations, or a growing-step or
continuous-time limit.

## Inputs, boundary, and checks

The full 192-line POLYNOMIAL_TRANSFER.md was read. Its SHA256 before
the audit was:

    9738334f29fb09f2123f075e3e94cb759fa419fc426bc46123296eb9d10c6c6c

The candidate was left unchanged. No study README, code, training output,
other study, historical discussion, or earlier review was read.
Previously read canonical-notation and rigorous-proof instructions,
including the neural-network notation reference, were reused.

The primary source was Wang–Zhong–Fan, arXiv:2206.13037v3. I checked its
Wasserstein convention, Definitions 2.19–2.20 and D.3, the complete
statements of Proposition D.1 and Lemma D.9, and their relevant proof
reductions through D.2 and D.10–D.12. In particular I checked the exact
tree normalization and the explicit absence of bounded-operator-norm,
positive-root-variance, and AMP Onsager hypotheses from these statements.
The cited published results are used as external theorems; I do not claim
to have independently re-proved or fully audited every lemma in WZF's
earlier symmetric proof. This audit did not require the later AMP
approximation theorem. [WZF, version 3](https://arxiv.org/html/2206.13037v3)

Retrieval used the primary versioned HTML through the web tool. A direct
attempt to save the same HTML failed because shell DNS was unavailable;
there is no local byte hash of the external article. Its mathematical
statements were available and were not inferred from search snippets.

I ran one small CPU combinatorial check in the assigned scratch folder,
with no training and no GPU use. It enumerates Wick pairings exactly:
single-trace leading terms for \(k=1,\ldots,5\) have counts
\(1,2,5,14,42\), and cross-trace pairings for \(k=1,2,3\) have at most
\(2k\) free index classes. The script is
data/generated/response_memory_fast_mixing_20261002/poly_review/check_wick.py.
This supplements the arbitrary-order analytical check below.

## The precise external implication

At aspect ratio one, WZF Proposition D.1(a,b1) gives the same limiting
diagonal distribution to independent Haar singular bases and the stated
signed-permutation/Hadamard construction when their singular-value
empirical laws have the same all-order Wasserstein limit. WZF Lemma D.9
then gives deterministic almost-sure limits for fixed alternating
polynomial trees, provided the initial side-vector laws have all moments,
converge in every Wasserstein order, and are independent of the matrix.
Definition D.3 uses one overall \(1/n\) factor and no normalization at
each edge. These are precisely the published statements needed here.
[WZF, Proposition D.1 and Lemma D.9](https://arxiv.org/html/2206.13037v3)

The row dimension called \(m\) by WZF is \(n\) in this candidate. It is
not the candidate's fixed training-sample count \(m\). Both hidden spaces
have width \(n\), so the aspect ratio is exactly one.

## Matrix and initial-root hypotheses

The normalized Sylvester matrix is orthogonal and every entry has
absolute value \(n^{-1/2}\). Thus it satisfies every required eventual
\(n^{-1/2+\epsilon}\) entry bound along dyadic widths. The candidate
specifies four mutually independent uniform signed permutations,
independent also of the deterministic singular-value array and \(A_0\).
Both left and right factors match the required construction exactly;
using the same deterministic Hadamard matrix on the two sides does not
violate an independence requirement.

The quarter-circle density in (6) integrates to one and has second
moment one. Its inverse distribution function is continuous on the
closed unit interval. Midpoint sums therefore give every moment of
\(t_{n,i}\); \(c_n\to1\), so the normalized singular values remain
uniformly bounded eventually and have all-order Wasserstein limit \(Q\).
This verifies the structured-ensemble hypothesis, including the exact
normalization rather than merely an approximate second-moment match.
The proposed replacement by any nonnegative deterministic singular-value
array with the same all-order Wasserstein limit also satisfies this
hypothesis. A separate uniform operator-norm bound is not needed for
this theorem.

For the Gaussian ensemble, I checked the combinatorics in (10)–(12).
For a Wick pairing of one trace, identifying the paired Gaussian entries
produces a connected bipartite quotient graph. With at most \(k\)
distinct edges, its number \(v\) of free row/column index classes is at
most \(k+1\). Because no inequality between different classes is imposed,
the summation contribution is exactly \(n^{v-k-1}\), including assignments
where different classes happen to take equal numerical values.

Equality \(v=k+1\) requires a tree with \(k\) distinct edges, each used
twice. The cyclic walk starts at its distinguished row vertex. First
discovery of an edge increases the distance in the exploration stack,
and its return decreases that distance. This gives a Dyck path; conversely
the stack pairing for a Dyck path determines the leading Wick pairing.
Consequently the leading count is the Catalan number \(C_k\), and all
other pairings contribute \(O_k(n^{-1})\).

For the covariance of two traces, the pairings with no cross-trace pair
cancel exactly against the product of expectations. Any remaining
pairing has a connected quotient graph with at most \(2k\) edges.
If it had \(2k+1\) vertices it would be a tree with each edge used exactly
twice in total. A cross-trace pair would put one traversal of one such
edge in each closed trace walk, contradicting the even number of
crossings of a tree cut by a closed walk. Thus \(v\le2k\), giving
the claimed \(O_k(n^{-2})\) variance after normalization. The argument
does not incorrectly assume independence of trace terms or of paired
indices.

Chebyshev and summability give almost-sure convergence of all integer
spectral moments simultaneously. Tightness follows from the first
moment, and higher moments supply uniform integrability when passing
lower moments to subsequential weak limits. Since \(C_k\le4^k\), any
such squared-singular-value limit is supported on \([0,4]\): a positive
mass beyond \(4+\epsilon\) would contradict the moment bound as \(k\)
increases. On this compact interval, the moments determine the law.
The quarter-circle pushforward has those Catalan moments. Taking square
roots, with the same higher-moment control, gives every Wasserstein order
for the Gaussian singular values. This proves the actual Gaussian
spectral premise; substituting deterministic quantiles for a Gaussian
matrix was not needed.

The Gaussian matrix density is unchanged by independent left and right
orthogonal actions. Conditioning on its singular values gives the
invariant orbit law, realizable using independent Haar left and right
factors independent of the singular values. The nonuniqueness of an
SVD does not obstruct this representation in law. This verifies the
Gaussian side of the matrix comparison.

The stated Haar entry check is also correct: on
\(\|g\|^2\ge n/2\), a violation of the threshold requires
\(|g_1|>n^\epsilon/\sqrt2\). The chi-square lower-tail bound and
Gaussian coordinate tail are summable after a union bound over
\(n^2\) entries. Independence between entries is unnecessary.

For initial side vectors, take the \(d\) Gaussian columns of \(A_0\)
and a constant-one channel on the right, and a constant-one channel
on the left. These roots are independent of each environment. For
every fixed Gaussian row monomial, the empirical average has variance
\(O(n^{-1})\). Dyadic widths make those deviation probabilities summable,
even without independence between widths. A countable intersection,
tightness, higher-moment uniform integrability, and Gaussian moment
determinacy give joint all-order Wasserstein convergence. Polynomial
initial \(H_a\) are then constructed channels, while zero \(w,D_a\)
need no separate randomness. No nonzero variance assumption has been
silently imposed.

## Exact scaling and finite tree compilation

Introduce only for this verification the reconstructed physical hidden
matrix

\[
B=W_0-\frac{2}{mn\tau}\sum_{a=1}^m D_aH_a^\top.
\]

Then \(z(x)=Bh(x)\), since \(H_a^\top h=n\langle H_a,h\rangle_n\).
Likewise

\[
B^\top\delta_a
=W_0^\top\delta_a-\frac{2}{m\tau}
        \sum_bH_b\langle D_b,\delta_a\rangle_n.
\]

This verifies both actions, their transpose pairing, and their
\(1/n\) normalization. Differentiating
\(m^{-1}\sum_a(f(x_a)-y_a)^2\), with
\(f=n^{-1}w^\top\sigma(B\sigma(Ax/\sqrt d))\), gives the displayed
\(A,w\) updates under mobilities \(n,n\), and the displayed unrestricted
\(B\) update under mobility one. The \(1/\sqrt d\), \(1/m\), and factor
two are consistent. The raw \(q=1\) history equations have no
mode-dilation term, so \(F_H=\rho h\), \(F_D=r\delta\) and the
unit-prefix initialization are internally consistent.

The rooted-tree representation (13) is exact. A rooted tree sums all
nonroot indices without restrictions. Coordinatewise multiplication
therefore uses disjoint copies of the old trees joined at their roots:
the summations are independent dummy sums, even though numerical
indices may coincide. The result is still a tree. Polynomial maps are
finite sums of these products. Multiplication by \(W_0\) or its true
transpose adds one opposite-side root and one edge, with no additional
normalization. In particular, repeated use of the same initialized
matrix does not mean replacing its appearances by independent matrices;
every edge carries the same \(W_0\), exactly as in the external primitive.

For a same-side polynomial average, expand all vector representations
and sum the root with \(1/n\). Each resulting term is a fixed
alternating-tree contraction times a product of earlier scalar
coefficients. There is no extra \(1/n\) per vertex or edge.
The low-rank actions are already built from normalized global inner
products, so their normalization is not lost in this step.

The coefficient adaptation causes no gap. Order the computation
instructions causally. At a global average, all earlier coefficients
have finite deterministic common limits by induction. The finitely
many fixed trees also have common finite limits on one probability-one
event. Their products converge on that same event, whether or not
coefficients and tree values are statistically dependent. A continuous
scalar operation then supplies the next coefficient's limit. Products
of global averages remain scalar products of tree limits; they are
not misidentified as a single connected tree.

Although degrees and tree sizes may grow very rapidly with \(J\), for
fixed \(J,d,m,M,\sigma\) their number and size are finite and independent
of \(n\). That is sufficient here and gives no bound uniform in \(J\)
or polynomial degree.

## Scalar clocks, exceptional cases, and observable quantifiers

The only nonpolynomial scalar operations needed are the Euclidean
residual norm and the reciprocal clock. The former is continuous on
all residual vectors, including zero. Positive Heun step sizes give
\[
\tau_k^*=\tau_k+\eta_k\rho_k\ge1,\qquad
\tau_{k+1}=\tau_k+\frac{\eta_k}{2}(\rho_k+\rho_k^*)\ge1.
\]
The scalar induction first gives a finite limit for the clock; its
lower bound keeps the reciprocal continuous there. There is no
division by \(\rho\), and no square-root differentiability argument
is needed. Zero labels, zero residuals, constant or zero polynomials,
zero backward vectors, and \(J=0\) all remain within the proof.
Large fixed step sizes may make finite limiting values large but do
not make a finite composition of these operations undefined.

At each fixed width the initialized entries are finite almost surely.
Polynomial operations and a denominator bounded away from zero
preserve finiteness through every fixed step. Thus the computation is
defined before applying its limit theorem; finite-time ODE existence
or discrete stability is not being assumed implicitly.

The observable class is exactly fixed finite lists of same-side
channels with fixed polynomial tests. It includes products of features,
backward fields and moments, and polynomials in initial and current
channels such as squared displacements. Predictions are same-side
inner products. Residuals, residual RMS, clocks, and displacement RMS
then follow through scalar continuity, including RMS at zero.
Both ensemble sequences converge almost surely on their marginal
probability-one events; their intersection still has probability one
under any coupling preserving the hypotheses. Thus subtracting their
limits is legitimate without coupling neuron coordinates.

There is no conclusion for cross-side coordinatewise tests, growing
numbers of queries or steps, growing-degree observables, arbitrary
nonpolynomial empirical tests, uniformity on a continuum of inputs,
fluctuation laws, or discontinuous decisions at zero limiting margin.
The candidate states the relevant restrictions. A continuous function
of the limiting scalar list must also be defined at the finite lists
where it is evaluated, as usual for this formulation.

## Secondary claims and audit limits

The unsigned-permutation equivariance argument is correct for any
polynomial, including nonodd ones. Every update transforms by the
appropriate row permutation, initial Gaussian rows have invariant law,
and the stated scalar empirical observables are invariant. Consequently
the externally permuted and unpermuted mathematical versions have the
same relevant finite-width scalar distributions. Convergence in
probability transfers as claimed; arbitrary orthogonal changes of basis
would not have this coordinatewise equivariance.

The middle signed-permutation identity is algebraically correct:
with \(P=P_EP_F^\top\), the two independent permutations induce
independent uniform \(P_E,P\), and the combined sign vector remains
uniform and independent of them. However, the actual source code was
outside this audit's input scope. I therefore verified the stated
sampler identity, not the claim that the named code implements every
draw and transpose exactly in that order. This is an unassessed
implementation assertion, not a missing premise of the mathematical
corollary, whose sampler is explicitly defined in (7).

The dense fixed-step extension is valid: each Heun update adds two
rank-at-most-\(m\) terms, so after \(k\) completed steps its exact
history representation has rank bound \(2mk\). Its forward and
transpose actions use the same allowed global averages and initialized
matrix actions. This supplies ensemble universality within the dense
algorithm as well. It does not identify that algorithm with the
\(q=1\) closure or establish their trajectory agreement.

No blocking proof correction is required. The strongest limitations
are the deliberately fixed finite computation, polynomial activation
class, and empirical observable scope. Extending to tanh, finite
precision, growing \(J\), or continuous time requires new estimates.
The candidate explicitly leaves those extensions open, and this PASS
does not change that status. No material was promoted.
