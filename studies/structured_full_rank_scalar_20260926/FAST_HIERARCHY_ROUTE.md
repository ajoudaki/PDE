# Scoped route: full-rank fast random operators and scalar closure

Scope: prompt-only theoretical analysis and primary-source lookup. No repository scientific material or other route drafts were read; no training experiments were run. The investigate-conjectures and solve-math-rigorously skills governed the claim separation below.

## Assessment

There are credible full-rank structured initialization hierarchies that repair Gaussian matrix reuse. This is substantially weaker than a proved efficient autonomous scalar approximation of the unrestricted training flow on a compact interval. The most promising candidates are (i) spectrally matched, independently scrambled fast transforms and (ii) growing Gaussian block motifs. Sums of cheap orthogonal factors provide an exact, easily quantified intermediate construction, but fixed order has a persistent reuse defect.

The intended comparison retains the original training equations after replacing only the initialization. In particular, the learned middle-weight correction remains unrestricted. All claimed width independence below means independence of the original width; dependence on an explicitly displayed approximation parameter is retained and costed.

## Exact facts for sums of orthogonal factors

Let

\[
A_{n,k}=k^{-1/2}\sum_{s=1}^k Q_s,
\]

where the independent real orthogonal matrices satisfy

\[
\mathbb E Q_{ij}=0,\qquad
\mathbb E[Q_{ij}Q_{ab}]=n^{-1}\delta_{ia}\delta_{jb}.
\]

Examples are Haar orthogonal matrices, uniformly random signed permutations, and \(D_1HD_2\) where \(H\) is a fixed normalized flat Hadamard matrix and \(D_1,D_2\) have independent Rademacher diagonals. For the last example, independence of the signs kills terms unless both row and column indices coincide, and flatness gives the variance \(1/n\).

Entry means and covariances of \(A_{n,k}\) agree exactly with those of the canonical Gaussian matrix \(G_n\), whose entries are independent \(N(0,1/n)\). Nevertheless,

\[
\mathbb E\frac1n\operatorname{tr}[(A_{n,k}A_{n,k}^{\mathsf T})^2]
=2-\frac1k+\frac{k-1}{kn},
\qquad
\mathbb E\frac1n\operatorname{tr}[(G_nG_n^{\mathsf T})^2]
=2+\frac1n.
\]

To verify the first identity, expand the four factor labels. The cases \(s=t,u=v\) and \(s=v,t=u\) contribute \((2k^2-k)n\), counting the all-equal case once. The remaining two-pair case \(s=u\ne t=v\) contributes \(k(k-1)\), since the covariance identity gives
\(\mathbb E\operatorname{tr}[(Q_sQ_t^{\mathsf T})^2]=1\).
Any label occurring once gives zero. Divide by \(nk^2\). Thus fixed \(k\) has a limiting discrepancy \(1/k\) in this first nontrivial Gram-reuse invariant. This invariant defect alone is not a lower bound on every particular training-output discrepancy.

There is also a uniform-in-width fixed-word result. For every fixed transpose word \(w\) of even length \(2r\),

\[
\left|\mathbb E\frac1n\operatorname{tr}w(A_{n,k},A_{n,k}^{\mathsf T})
-\mathbb E\frac1n\operatorname{tr}w(G_n,G_n^{\mathsf T})\right|
\leq C_r/k.
\]

Here \(C_r\) is combinatorial and no polynomial growth in \(r\) is claimed. Proof: expand the factor labels. Singleton labels vanish. Pair-only label partitions with distinct labels contribute the Gaussian Wick contractions, multiplied by \((k)_r/k^r\). Every other surviving partition uses at most \(r-1\) labels. Each corresponding normalized trace has modulus at most one, because it is a product of orthogonal matrices. Each Gaussian pairing contraction of one normalized trace has magnitude at most one: the connected polygon contraction has at most \(r+1\) free indices. The omitted colorings and \(1-(k)_r/k^r\) are both bounded by \(C_r/k\). For small \(k<r\), enlarge \(C_r\).

This proves convergence of expected trace *-moments, not concentration of every observable and not convergence of nonlinear diagonal tensor networks. Branching coordinate products are outside the normalized-trace bound used in this proof.

At fixed finite \(n\), the ordinary vector-valued central limit theorem also gives \(A_{n,k}\Rightarrow G_n\) as \(k\to\infty\). Continuity of a well-posed finite-dimensional training flow then transfers this fixed-width convergence on bounded time intervals. It supplies no uniform width bound or useful relation between \(k\) and training accuracy.

For signed permutations there is an additional transparent forward discrepancy. With iid mean-zero input coordinates \(X_j\), variance \(q\), and fourth moment \(\mu_4\), the fixed-\(k\), infinite-width row law is \(k^{-1/2}\sum_{s=1}^k\epsilon_sX_s\), up to vanishing collision probability. Its fourth moment is

\[
3q^2+(\mu_4-3q^2)/k.
\]

The first hidden tanh features are generally non-Gaussian, so even the first multiplication has a finite-\(k\) correction. Repeated multiplication and transpose reuse additionally preserve backtracking dependencies; refreshing edges or inputs independently at each call changes the model.

The sums need not be full rank. For example, \(Q_1+Q_2\) is singular whenever \(Q_1^{\mathsf T}Q_2\) has eigenvalue \(-1\). Adding an independent scalar \(\delta I\), with \(\delta\) continuously distributed in a small interval, makes the matrix invertible almost surely: its determinant is a nonzero polynomial in \(\delta\). This costs \(O(n)\), but the shift size is a separate approximation parameter that must vanish. Full rank does not imply a uniform least-singular-value bound.

Signed permutation sums use \(O(kn)\) storage and work per multiplication; flat fast-transform sums use \(O(kn)\) stored signs and \(O(kn\log n)\) work. Haar factors themselves have no generic fast representation. None of these estimates eliminates the evolving \(n\)-neuron population. In a sparse local construction, an explicitly unfolded depth-\(P\) neighborhood can contain order \(k^P\) vertices; this is a cost of that representation, not a general lower bound against all closures.

## A stronger spectrally matched fast candidate

Let \(H_n,K_n\) be normalized Hadamard transforms and set

\[
A_n=(\Pi_U H_n\Pi_E)\,\operatorname{diag}(s_1,\ldots,s_n)\,
(\Pi_V K_n\Pi_F)^{\mathsf T},
\]

with four independent uniform signed permutations and strictly positive \(s_i\). Choose their empirical law to approach the singular-value law of square Gaussian matrices: equivalently \(s_i^2\) approaches the Marchenko–Pastur law of aspect ratio one. Positive interior quantiles are one possible deterministic choice. The matrix is exactly full rank, has operator norm at most two for this quantile choice, and uses \(O(n)\) stored coefficients and \(O(n\log n)\) multiplication. Both matrix and transpose remain available. This is a single dense structured replacement, not a low-rank approximation.

The following paragraph is the source-based theorem summary; subsequent implications are this route's analysis. Wang–Zhong–Fan, Proposition D.1(b1), verifies generalized invariance for independently scrambled orthogonal bases with delocalized entries and a convergent singular law. Lemma D.9 then matches fixed alternating diagonal tensor networks (the tree networks of Definition D.3), with independent side vectors having empirical convergence in every Wasserstein order. Theorem 2.22 covers fixed-step AMP with suitable Onsager coefficients, Lipschitz nonlinearities, bounded operator norm, and nonsingular state-evolution covariances. Remark 2.15 separately treats arbitrary fixed polynomial first-order iterations. These are stronger reuse guarantees than spectral convergence. [Primary paper, latest PDF](https://arxiv.org/pdf/2206.13037).

For the displayed candidate, flatness verifies the entry bound on the bases, the four random permutations verify the independence requirement, and the positive bounded quantiles verify singular-law convergence and bounded norm. Gaussian initial first-layer side vectors have all moments and are independent of this middle matrix. Fixed polynomial versions of an unrolled finite training computation can therefore be studied using the alternating tensor-network result: learned outer products reduce to local histories and empirical scalar contractions.

This does **not** directly certify the actual tanh gradient flow. The published AMP theorem does not automatically accept an arbitrary unmodified gradient recurrence. Products involving evolving readouts, backpropagation fields, and activation derivatives are not jointly globally Lipschitz merely because tanh is bounded. A transfer needs explicit polynomial approximation/localization and moment estimates, treatment of evolving empirical scalar coefficients, and a uniform time-discretization bound. Degenerate initial readout and repeated or dependent data can also make covariance nondegeneracy require separate handling. These are gaps in applying the theorem, not negative evidence against the candidate.

Even a successful universality transfer would identify the same Gaussian history process; it would not make the expectations over its growing history polynomial-time computable. Thus this candidate largely addresses replacement of the Gaussian matrix, while leaving the scalar compression problem intact.

For contrast, the non-Gaussian tensor-program theorem assumes independent matrix entries with uniformly scaled moment bounds and polynomially smooth nonlinearities. It cannot be applied directly to any of the correlated fast-transform ensembles above. [Golikov–Yang, Setup 3.6 and Theorem 3.7](https://papers.nips.cc/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf).

## Gaussian block motifs

Another full-rank family is a block-diagonal matrix with independent \(b\times b\) Gaussian blocks, each scaled by \(1/\sqrt b\), optionally scrambled by independent row and column permutations. Its width \(n=Bb\) representation has \(O(nb)\) nonzeros, and every block is invertible almost surely. Its expected second Gram moment is \(2+1/b\), tending to the Gaussian target from above.

Keep unrestricted dense learning after this initialization. In the given finite-\(P\) rank-memory representation, all coupling between different initial blocks then occurs through the global empirical scalar contractions of the retained histories. The initial matrix and transpose act within one fixed motif. A motif stores order \(bmP\) response/history entries, plus \(b^2\) initial matrix coefficients and its first-layer random variables; it does not unfold a \(k^P\) tree.

For a fixed finite polynomial computation, two qualitative limits can be justified by finite induction. First, \(B\to\infty\) replaces empirical block averages by expectations over iid motifs: each next motif state is a polynomial in its Gaussian initial variables and the earlier common scalar coefficients. Finite Gaussian moments permit the law of large numbers at each step. Second, \(b\to\infty\) gives the Gaussian large-width limits of those finite polynomial computations, using Wick expansion or the Gaussian tensor-program limit. The induction must propagate convergence of the shared scalar coefficients; the construction is not an independent-block training model with separate losses.

This route gives a natural hierarchy of width-independent **population descriptions**, not automatically a finite scalar ODE. A motif's initial randomness has order \(b^2+bd\) dimensions. Deterministic tensor cubature generally grows exponentially in that dimension. Replacing the motif expectation by \(Q\) sampled motifs gives a finite, autonomously evolving numerical state with arithmetic polynomial in \(b,P,Q\), but a useful polynomial bound for \(Q(b,P,T,\varepsilon)\) has not been established here. Calling the remaining distribution a scalar would hide the population rather than compress it.

## Outstanding bottleneck and claim status

Established here: the sum-family covariance and fourth-moment identities; uniform fixed-trace-word comparison; the full-rank shift; and the stated costs. Verified from the primary source: a concrete fast spectral candidate lies in a universality class that controls fixed diagonal tensor networks and AMP reuse.

Plausible but not proved here: transfer to the full fixed-step tanh training computation for the spectral candidate; identification of block motifs for the nonpolynomial trained system; compact-time convergence under the required limit order.

Open: an autonomous, restartable scalar hierarchy with a proved polynomial dependence on order/accuracy and no hidden growing distribution/history. The highest-leverage next theorem is an error estimate for finite motif/history population approximation, or an equivalent finite Gaussian-history sampler, with constants controlled uniformly as history order grows. Matrix-vector speed alone does not resolve this theorem.
