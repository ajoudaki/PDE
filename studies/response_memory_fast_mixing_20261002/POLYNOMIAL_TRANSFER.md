**Finite-step transfer for the polynomial q=1 response-memory closure. Frozen author derivation, 2026-10-02.**

The result below is a corollary of Wang–Zhong–Fan's published alternating-tree universality lemma. All hypotheses needed for the stated mathematical ensembles and initialization are verified here. It concerns exact arithmetic, a fixed finite number of Heun steps, polynomial activations, and finitely many empirical polynomial observables. It is not a theorem for the tanh producer, continuous-time training, growing memory order, or an all-time limit. It is internally checked and has not undergone the repository's independent promotion review.

Only this study's README.md, REUSE_THEORY.md, TRAINING_PROTOCOL.md, fast_training.py, and subsequently authorized reuse_check.py supplied scientific context. Training results, including the outcome language appended to the protocol, play no role in the proof. No experiment was run for this note. LITERATURE_AUDIT.md is unchanged.

**Model and the precise claim.** Fix positive integers d,m and a nonnegative integer J. Fix a finite list of inputs x_1,...,x_M in R^d, with M>=m, labels y_1,...,y_m in R, a real polynomial sigma, and positive step sizes eta_0,...,eta_{J-1}. All these quantities are independent of the hidden width n. The first m inputs are the training set; the rest are fixed evaluation inputs. Both hidden layers use sigma and its actual polynomial derivative sigma'. No oddness, boundedness, or nonzero label assumption is needed.

Let n=2^b tend to infinity. There are two distinct copies of R^n: the first hidden-layer coordinate space R, and the second hidden-layer coordinate space L. Matrices W_0 map R to L. For vectors u,v belonging to the same copy define

    <u,v>_n = (1/n) sum_{i=1}^n u_i v_i,

and use odot for coordinatewise multiplication. The state is

    S=(A,w,H_1,...,H_m,D_1,...,D_m,tau),

where A is n-by-d with columns in R, each H_a is in R, w and every D_a are in L, and tau is a real scalar. At any state with tau>0 define, for each query input x,

    u(x) = A x / sqrt(d),                 h(x) = sigma(u(x)),
    z(x) = W_0 h(x) - [2/(m tau)] sum_{a=1}^m D_a <H_a,h(x)>_n,
    g(x) = sigma(z(x)),                  f(x) = <w,g(x)>_n.       (1)

For training input a abbreviate u_a=u(x_a), h_a=h(x_a), z_a=z(x_a), and g_a=g(x_a). Define

    r_a = f(x_a)-y_a,                    rho = sqrt((1/m) sum_a r_a^2),
    delta_a = w odot sigma'(z_a),
    ell_a = sigma'(u_a) odot
            [W_0^T delta_a - (2/(m tau)) sum_b H_b <D_b,delta_a>_n].   (2)

The vector field F_{W_0}(S) is specified by

    F_A   = -[2/(m sqrt(d))] sum_a r_a ell_a x_a^T,
    F_w   = -(2/m) sum_a r_a g_a,
    F_Ha  = rho h_a,                     F_Da = r_a delta_a,
    F_tau = rho.                                                   (3)

These are the raw q=1 moment equations from the supplied protocol, with tanh replaced throughout by sigma and its derivative. In particular there is no division by rho. Initialize

    A_0(i,j) iid N(0,1),       w_0=0,       D_{a,0}=0,
    tau_0=1,                  H_{a,0}=sigma(A_0 x_a/sqrt(d)).        (4)

The initialized A_0 is independent of W_0. Heun's explicit two-stage update is

    K_k = F_{W_0}(S_k),
    S_k^* = S_k + eta_k K_k,
    K_k^* = F_{W_0}(S_k^*),
    S_{k+1} = S_k + (eta_k/2)(K_k+K_k^*),       0<=k<J.           (5)

Queries may be evaluated at any of the finitely many states and stages in (5).

To define the structured ensemble, let mathsf H_n be the normalized Sylvester Hadamard matrix. Let Q be the distribution on [0,2] with density sqrt(4-s^2)/pi and distribution function F_Q. Set

    t_{n,i} = F_Q^{-1}((i-1/2)/n),
    c_n = [(1/n) sum_i t_{n,i}^2]^(1/2),
    s_{n,i} = t_{n,i}/c_n.                                      (6)

Sample four mutually independent uniform signed permutation matrices Pi_U,Pi_E,Pi_V,Pi_F, independent of A_0. Set

    W_0^S = Pi_U mathsf H_n Pi_E diag(s_n)
                  Pi_F^T mathsf H_n^T Pi_V^T.                    (7)

The Gaussian ensemble is W_0^G with independent N(0,1/n) entries, independent of A_0. The two environments may be independent; they may share A_0. More generally any coupling is allowed that preserves the stated marginal hypotheses.

**Corollary.** Run (1)–(5) separately with W_0^S and W_0^G. For each run retain any fixed finite list of vector channels computed on one coordinate space, at any states/stages/queries, including A's columns, u,h,H,ell on R and w,z,g,D,delta on L. If p is any fixed real multivariate polynomial and v_1,...,v_r are such channels all on the same coordinate space, then

    O_n = (1/n) sum_{i=1}^n p(v_1(i),...,v_r(i))                 (8)

converges almost surely to a finite deterministic limit. The limit is the same for the structured and Gaussian runs. Finitely many such statements hold jointly, and every continuous function of the resulting finite list of scalar observables has the corresponding common limit whenever that function is defined and continuous at the limit. In particular,

    O_n^S - O_n^G -> 0 almost surely.                            (9)

This includes predictions, training/evaluation squared losses, all within-layer finite-sample feature Gram entries, moments of backward fields and stored moments, squared feature displacements, their root mean squares, residuals, rho and tau at all the fixed steps. It does not assert coordinatewise agreement between neurons in the two runs, coupling of their matrix realizations, convergence rates, equality of finite-width fluctuation laws, or convergence of every nonpolynomial empirical test. Classification decisions require an additional nonzero limiting margin if deduced from prediction convergence.

All statements are about the mathematical random ensembles and exact quantiles in (6). A deterministic sequence satisfying the same all-order Wasserstein limit Q may replace (6), with the same conclusion. No separate uniform bound on ||W_0|| is required by the polynomial argument, although (6) itself is bounded.

**Published input, stated with its full relevant hypotheses.** For a rectangular matrix B define its symmetric embedding X=[[0,B],[B^T,0]] and the two coordinate-block projections. A diagonal word is a finite expression built from these matrices by multiplication and the operation that keeps only a matrix's diagonal. “Generalized invariant” below means: B has the law Pi_L C Pi_R^T for independent uniform signed permutations independent of C; normalized traces of every diagonal word in C's embedding converge; and every such word's off-diagonal entries are eventually smaller than n^(-1/2+epsilon), for every epsilon>0. The aspect ratio has a positive finite limit. The trace limits constitute its limiting diagonal distribution.

Wang–Zhong–Fan, Definition D.3 and Lemma D.9, imply that every alternating polynomial tree contraction has a deterministic almost-sure limit determined only by that diagonal distribution, the aspect ratio, and the initial side-vector laws. Initial side vectors must be independent of the matrix and converge empirically in every Wasserstein order to deterministic laws having all moments. Proposition D.1(a,b1) identifies the diagonal distributions for (7) and independent Haar singular bases whenever the singular-value empirical laws converge in every Wasserstein order; the orthogonal factors in (7) must have entries at most n^(-1/2+epsilon). Neither result requires bounded operator norm, positive initial variance, polynomial density, Onsager corrections, or nonsingular state covariance. Those extra requirements belong to the later AMP approximation theorem, which is not used here. [Primary source, arXiv:2206.13037v3](https://arxiv.org/html/2206.13037v3)

The following proof verifies these hypotheses and then gives the full reduction from (1)–(5). The published results are used as theorems, not as conjectures. Their relevant proof dependencies were read as recorded at the end.

**Proof, matrix hypotheses.** The entries of mathsf H_n have absolute value n^(-1/2); hence its orthogonality and entry condition hold deterministically. All four signed permutations in (7) have exactly the independence required by D.1(b1). Its singular values are exactly s_n. Since F_Q^{-1} is continuous on [0,1], midpoint Riemann sums show that the empirical laws of t_n converge weakly and in every moment to Q. Also

    integral_0^2 s^2 sqrt(4-s^2) ds / pi = 1,

so c_n→1. The arrays s_n are bounded uniformly for all sufficiently large n and converge in every Wasserstein order to Q. Thus D.1(b1) applies with aspect ratio 1.

For completeness, the all-order spectral convergence needed for the actual iid Gaussian reference can be checked without identifying it with a finite-width quantile matrix. Write W_0^G=Z/sqrt(n), where Z has independent standard Gaussian entries, and set

    T_{n,k} = (1/n) tr[(W_0^G(W_0^G)^T)^k]
            = n^(-k-1) sum_{i_1,...,i_k; j_1,...,j_k}
                 product_{a=1}^k Z_{i_a j_a} Z_{i_{a+1} j_a},
      i_{k+1}=i_1.                                            (10)

For fixed k, Wick's formula pairs these 2k Gaussian factors. For each pairing, identify the row and column indices forced equal by the pairs. The resulting bipartite graph is connected, has at most k distinct edges, and therefore at most k+1 free vertices. Its contribution to E T_{n,k} is n^{v-k-1}, where v is the number of free row/column classes. Terms with v<k+1 vanish. If v=k+1, the graph is a tree with k edges, and the closed walk traverses every edge exactly twice. Its contour is a Dyck path of length 2k: encountering a new edge is an up step, returning along it is a down step. Conversely each such path specifies one leading pairing. Hence the number of leading terms is the Catalan number C_k=(k+1)^(-1) binom(2k,k), and

    E T_{n,k} = C_k + O_k(1/n).                                (11)

In the variance expansion, pairings with no pair connecting the two traces cancel against (E T_{n,k})^2. Every remaining pairing gives a connected quotient graph with at most 2k paired edges. A graph with 2k+1 vertices would be a tree in which every distinct edge is traversed twice in total. A pair connecting the two traces would then require each of their closed walks to cross its associated tree edge exactly once, which is impossible: a closed walk crosses every cut an even number of times. Thus at most 2k vertices remain. With the normalization n^(-2k-2),

    Var(T_{n,k}) = O_k(n^(-2)).                                 (12)

Chebyshev and Borel–Cantelli, followed by the countable intersection over k, give almost-sure convergence of every T_{n,k} to C_k along the dyadic widths. Direct integration shows

    integral_0^2 s^(2k) sqrt(4-s^2) ds / pi = C_k.

The squared-singular-value empirical measures are tight by their first moments. Higher moments give uniform integrability of every lower moment, so each weak subsequential limit has all moments C_k. That moment law is unique: its even-moment bounds force support in [0,4], and polynomials are dense in continuous functions on that compact interval. The whole squared-singular-value sequence therefore converges weakly to the pushforward of Q under s→s^2. Higher moments again imply convergence against every continuous polynomial-growth function. Taking square roots proves that the Gaussian singular values converge in every Wasserstein order to Q almost surely.

The iid Gaussian matrix density is proportional to exp[-n tr(BB^T)/2], so it is invariant under independent left and right orthogonal multiplication. Equivalently its law has a representation U diag(d_n) V^T with independent Haar U,V, independent of the singular values d_n. This can be seen by conditioning on the singular values: each orbit carries its invariant probability measure, generated by independent Haar left and right multiplication. D.1(a) now applies. Its limiting diagonal distribution is determined by aspect ratio 1 and Q, exactly as for (7). The deterministic-quantile versus random-Gaussian spectrum distinction is thereby accounted for in all orders, not ignored.

The Haar delocalization fact used inside D.1(a)'s proof does not create an unread dependency here. A Haar column is distributed as g/||g|| for g~N(0,I_n). For fixed epsilon>0,

    P(|g_1|/||g|| > n^(-1/2+epsilon))
      <= P(||g||^2<n/2)+P(|g_1|>n^epsilon/sqrt(2))
      <= exp(-c n)+2 exp(-n^(2epsilon)/4).

The first bound follows from the Gaussian chi-square exponential moment, with c=(log 2)/2-1/4>0. A union bound over n^2 entries and Borel–Cantelli give precisely the eventual entry bound used by D.1. Independence between Haar entries is unnecessary.

**Proof, initialization hypotheses.** The right-side initial vectors can be taken to be the d columns of A_0 and the constant vector 1. The left side needs only its constant vector 1; zero w and D are zero polynomial functions of it. Initial H_a in (4) is a polynomial function of the right roots and is constructed by the allowed vector operations.

The Gaussian row empirical law converges almost surely in all Wasserstein orders along dyadic n. One direct verification is to apply Chebyshev to each monomial of the d-dimensional row, whose variance is finite: the deviation probability is O(1/n), summable for n=2^b. Intersect over the countable set of monomials. These limits imply tightness; every subsequential limit has the Gaussian moments, using a higher even moment for uniform integrability. The Gaussian law is moment-determinate, as follows from its finite exponential moments near the origin. Thus weak convergence holds, and convergence of every radial moment upgrades it to all Wasserstein orders. The same argument works if matrices at different widths are freshly and arbitrarily coupled, since it used marginal probability bounds. Constant and zero vectors satisfy these conditions trivially. All roots are independent of the environment by (4). The limiting root laws are deterministic and have all moments.

In particular no positive-variance initialization is required. If every label is zero, rho may remain zero; (1)–(5) remain defined, and no division by rho appears. There is no need to perturb the readout or introduce artificial independent noise.

**Proof, a finite computation lemma.** Here is the explicit connection between the published tree primitive and the learning algorithm. Fix either environment. A rooted alternating tree has vertices assigned to L or R, edges only between different sides, and a polynomial in the initial side-vector coordinates attached to each vertex. For a fixed root coordinate i, its vector value sums over every other vertex coordinate the product of all vertex labels and factors W_0(alpha,j) for edges from L-coordinate alpha to R-coordinate j. The root is not summed and there is no normalization. Averaging its root over i with factor 1/n gives exactly a D.3 contraction. A one-vertex tree simply evaluates a polynomial of initial roots; its empirical convergence also follows directly from the initialization argument.

Consider a finite, fixed computation with these operations:

1. Form polynomial coordinatewise combinations of vectors on the same side, including constant vectors.
2. Multiply a right vector by W_0 or a left vector by W_0^T.
3. Take a normalized average of a polynomial in same-side vectors.
4. Form a scalar by a continuous function of earlier scalars, defined and continuous at their finite limits, and multiply a vector by such a scalar.

Every current vector has an exact finite representation

    v(i) = sum_{a=1}^N c_{a,n} R_a(i),                         (13)

where R_a is a rooted alternating-tree value and c_{a,n} is a scalar coefficient formed earlier. The finite number of terms, their trees and polynomial labels do not depend on n; only coefficients and evaluations do.

To prove (13), begin with the one-vertex representations of initial channels. Linear combinations preserve it. For a coordinatewise product, take fresh copies of the two trees and identify only their roots. A union of two trees sharing exactly one vertex is a tree. Their other coordinate summation indices remain separate; no distinctness constraint is imposed, so this is an exact identity even when numerical indices happen to coincide. Root labels multiply to another polynomial. A polynomial map is a finite linear combination of such products. Multiplying by W_0 or W_0^T adds a new root on the opposite side, with constant label 1, and one connecting edge. Multiplication by a scalar updates coefficients. These operations prove the representation inductively.

Whenever operation 3 is reached, expand its polynomial using (13). The resulting scalar is a finite sum of products of earlier coefficients and normalized unrooted tree values. D.9 gives finite deterministic common limits for those tree values in the two ensembles. Only finitely many trees are needed by the chosen computation and test, so their convergence holds on a single probability-one event. Assuming earlier coefficients have finite common limits, ordinary addition and multiplication give the next average's common limit. Operation 4 then preserves this property by continuity. No independence is required between adaptive coefficients and their tree values: both converge on the same event. This induction proves common deterministic limits for all computed scalar averages and coefficients. Products of global averages are kept as products of tree values; they are not incorrectly treated as one connected tree.

This is the complete computation lemma. It imports only the tree universality theorem with the hypotheses already checked, not the polynomial-approximation step of an AMP theorem.

**Proof, compiling one closure step.** Equations (1)–(3) consist exactly of the preceding operations. The finite sum A x uses d scalar-weighted right vectors; sigma and sigma' are polynomial coordinatewise maps. Each term <H_a,h>_n and <D_b,delta_a>_n is a normalized polynomial average on its own side. Prediction <w,g>_n is such an average on L. The residuals use fixed labels, and

    (r_1,...,r_m) -> [(1/m) sum_a r_a^2]^(1/2)

is a continuous function on all of R^m, including at zero. The only inverse is 1/tau. Both Heun stages satisfy

    tau_k^* = tau_k + eta_k rho_k >= tau_k >= 1,
    tau_{k+1} = tau_k + (eta_k/2)(rho_k+rho_k^*) >= tau_k >= 1.   (14)

Thus the inverse is evaluated on [1,infinity), where it is continuous. The inductively obtained limit of tau is finite and at least 1, so inverse-clock coefficients have finite common limits. The update of each column of A in (3) is a finite combination of ell_a, with coefficients r_a x_a(j); all other updates are already explicit vector-scalar combinations. Applying (5) adds only scalar-weighted sums and a second evaluation of the same finite computation.

At each fixed n, all entries are finite almost surely initially, and every finite step remains finite in exact real arithmetic because polynomial operations preserve finiteness and (14) prevents a zero denominator. For fixed J the computation contains finitely many instructions independently of n. The computation lemma applies by induction through all stages, yields finite deterministic limits for their scalars, and applies again to every observable (8). This proves the corollary. Continuous functions of the finite list converge by the continuous mapping principle. No stability estimate uniform in J or eta is used or obtained. QED.

**Implementation correspondence and its limits.** In reuse_check.py, FastMixer draws external signs, then middle signs and a singular-value shuffle, then a separate middle permutation. In fast_training.py, Mixer additionally draws independent external permutations. Under the stipulated ideal interpretation of these random draws this is exactly the law of (7). Indeed, writing Pi_E=diag(e)P_E and Pi_F=diag(f)P_F gives

    Pi_E diag(s) Pi_F^T = diag(e*(P f)*(P_E s)) P,
    P=P_E P_F^T.

For independent uniform P_E,P_F, the pair (P_E,P) is independent uniform. The sign vector e*(P f) is iid Rademacher independent of both permutations. This proves the middle-factor sampling equivalence. An external sign matrix multiplied on either side by an independent uniform permutation is a uniform signed permutation. The inverse-index operations in transpose reverse the same factors. The mathematical sampler therefore corresponds to the producer's operation order, rather than merely matching its singular values.

The proof idealizes exact quantiles and exact arithmetic. The producer uses a fixed number of bisection iterations and floating-point storage and currently evaluates tanh. None of those numerical choices is claimed to satisfy the theorem literally as n→infinity. An asymptotic implementation theorem would require quantile errors tending to zero and suitable arithmetic-error bounds. The Gaussian reference here is the iid matrix in fast_training.py; the separate CPU probe producer row-normalizes its Gaussian matrix and is not the reference specified in this corollary.

If the extra external permutations are omitted, the same prediction and same-side invariant Gram-observable conclusion holds in probability by finite-width permutation equivariance. For unsigned permutations P_L,P_R, replace

    W_0 by P_L W_0 P_R^T, A by P_R A, w by P_L w,
    H_a by P_R H_a, D_a by P_L D_a, tau by tau.

Every polynomial coordinatewise operation commutes with permutations, so (1)–(5) transform accordingly, and predictions and these empirical observables are unchanged. Gaussian A_0 has an invariant row law and the other initial states transform as required. Thus the relevant finite-width scalar distributions equal those for the externally permuted model. This does not require sigma to be odd. It does not extend to arbitrary orthogonal right-basis changes.

**Why this is not a closure-exclusive universality result.** Consider instead unrestricted hidden-matrix learning in the same physical scaling, with B initially W_0 and

    F_B = -[2/(mn)] sum_a r_a delta_a h_a^T,                     (15)

and the corresponding A,w updates. At each stage the hidden-matrix velocity has rank at most m. Unrolling J Heun steps exactly gives

    B_k = W_0 + (1/n) sum_{ell=1}^{R_k} c_ell u_ell v_ell^T,
    R_k <= 2mk,                                                 (16)

where u_ell belongs to L and v_ell to R. Trial stages add at most m further terms. Applying (16) or its transpose uses W_0 or W_0^T plus normalized same-side inner products and scalar-vector combinations. With polynomial activations and fixed J this is the same finite computation class. It therefore has the same structured-versus-Gaussian empirical universality conclusion. This statement compares the two initializer laws within the dense algorithm; it does not equate dense training with the q=1 closure.

The response-memory distinction is that its H,D representation has 2mn moment coordinates independently of J, while exact history unrolling has a number of factors growing with J. The present theorem supplies no claim that q=1 approximates dense dynamics well, no uniform control as J grows, and no efficiency comparison at matched trained quality. The matrix universality and fast prescribed-spectrum construction are prior results. The contribution of this note is an explicit verified corollary for this finite polynomial closure, including its nonpolynomial scalar clock/residual feedback.

**Source inventory and dependency check.** The only non-elementary external input is Wang–Zhong–Fan, *Universality of Approximate Message Passing algorithms and tensor networks*, [arXiv:2206.13037v3](https://arxiv.org/html/2206.13037v3). Read for this proof: the Wasserstein convention around (1.1)–(1.2); Definitions 2.19–2.20; Definition D.3; the complete statements and proofs of Proposition D.1 and Lemma D.2; complete Appendix B (Lemma B.1 and Proposition 2.7's proof); Lemma 3.3 and its proof; the complete symmetric proof section 3.2, including Lemmas 3.6, 3.7 and 3.9; and complete Appendix D.5, including Lemmas D.9–D.12 and their proofs. An initially truncated retrieval was repaired by separate complete reads of Appendix B, Appendix D.2 and Lemma 3.9.

The dependency path is D.9 <- D.10 plus D.12; D.10 uses D.11/3.7 and 3.3; D.12 uses the fourth-moment concentration argument in 3.9. Matrix classification uses D.1 <- D.2/B.1 and the power-entry concentration calculation in Proposition 2.7. These arguments require all moments and the diagonal-word delocalization conditions, not a bounded operator norm. The Haar entry estimate cited there to Jiang (2005) was not read as a separate paper; the weaker bound actually needed was proved above. The finite partition Möbius inversion identity used in Appendix B is elementary finite linear algebra; the cited book was not separately read. No Fan state-evolution theorem, polynomial-density theorem, or nondegenerate AMP covariance result is imported. The Gaussian spectral and initialization arguments required for this specialization are supplied above.

The resulting theorem is a complete corollary relative to the explicitly cited published universality results, not conditional on an unverified application hypothesis. It remains a polynomial, finite-step, empirical-observable theorem. Extending it to the actual tanh closure is a separate proof problem.
