# Primary-source audit: Tensor Programs III for the L=2 arctan construction

## Scope and source

The source audited is Greg Yang, *Tensor Programs III: Neural Matrix Laws*, arXiv:2009.10685v3 (8 May 2021), including the full TeX source of Setup 2.2, the ZHat/ZDot rules, Theorem 2.10, Appendix A, and the complete proof in Appendix G. Primary links:

- https://arxiv.org/abs/2009.10685v3
- https://arxiv.org/pdf/2009.10685v3

The Gaussian operator-norm citation was checked against Terence Tao, *Topics in Random Matrix Theory*, Section 2.3:

- https://terrytao.wordpress.com/wp-content/uploads/2011/08/matrix-book.pdf

No project file was inspected.

## 1. Exact theorem ledger

### Setup 2.2

A NETSOR^T program is fixed while n tends to infinity. It has finitely many vector lines. Each matrix W is square with iid entries N(0,sigma_W^2/n), independent of the other initial matrices. At each coordinate alpha, the tuple of initial vector entries is sampled iid across alpha from one fixed finite-dimensional multivariate Gaussian law. That Gaussian law is not required to be nonsingular.

The only primitive vector operations are fixed coordinatewise nonlinearities and multiplication by W or W^T. Thus the number of lines, every nonlinearity, and every deterministic coefficient must be independent of n.

### ZHat/ZDot rule

For g=Wx, the limiting scalar is Z^g=ZHat^g+ZDot^g. The ZHat variables associated with repeated uses of the same oriented matrix are jointly Gaussian with covariance

    Cov(ZHat^{Wx}, ZHat^{Wy}) = sigma_W^2 E[Z^x Z^y].

ZHat families for distinct oriented matrices are independent. Reuse through the opposite orientation contributes

    ZDot^{Wx}=sigma_W^2 sum_y Z^y E[partial Z^x / partial ZHat^{W^T y}],

where the sum ranges over all earlier opposite-orientation sources on which x depends. At singular source covariance, the paper gives the canonical interpretation a=C^+b. Therefore a reused transpose may not be replaced by an independent Gaussian multiplication; all response terms must be retained.

### Theorem 2.10

For a fixed NETSOR^T program satisfying Setup 2.2, if every coordinatewise nonlinearity is polynomially bounded, then for any fixed finite tuple of program vectors and any polynomially bounded test psi,

    n^{-1} sum_alpha psi(h^1_alpha,...,h^k_alpha)
      -> E psi(Z^{h^1},...,Z^{h^k})

almost surely along the full width sequence.

The theorem permits arbitrary finite reuse of W and W^T. It imposes no external rank-stability hypothesis in the parameterless language.

### Singular covariance in the proof

The proof is a simultaneous induction on empirical moments and a core set. It establishes:

1. rank stability for finite Gram matrices made from fixed polynomially bounded source functions;
2. zero stability: if the limiting innovation variance is zero, the new finite-width vector is eventually exactly the corresponding fixed linear combination of earlier vectors;
3. when the innovation variance is positive, Gaussian conditioning supplies a new absolutely continuous coordinate and preserves the core-set null-avoidance property;
4. the Gaussian-conditioning decomposition with simultaneous W and W^T constraints;
5. an Onsager/adjoint identity identifying the finite conditional mean with ZDot;
6. a strong law for the remaining projected Gaussian innovation.

This mechanism genuinely covers an exactly zero initial vector. It does not cover a nonzero n-dependent Gaussian vector whose variance merely tends to zero.

### Appendix A.1

For bounded tests, ordinary L1 convergence and hence convergence of expectations follow from Theorem 2.10 by dominated convergence. That part is correct.

The additional assertion that, for an arbitrary n-dependent sub-sigma-algebra B_n, the conditional expectations converge almost surely is false in that generality. Dominated convergence gives L1 convergence of E[X_n|B_n], not almost-sure convergence for arbitrary varying B_n.

A counterexample is obtained as follows. Let N be integer-valued with P(N>=n)=1/n, and A_n={N>=n}. Then 1_{A_n}->0 almost surely. Independently choose Bernoulli events E_n with probabilities q_n=(1/n)/(1-1/n), and put D_n=A_n^c intersect E_n, C_n=A_n union D_n, B_n=sigma(C_n). The two disjoint pieces A_n and D_n have equal probability, so E[1_{A_n}|B_n]=1/2 on C_n. Conditional on N, the events D_n occur infinitely often by the second Borel-Cantelli lemma, so these conditional expectations fail to converge almost surely to zero. This appendix overclaim must not be used.

### Appendix A.2

The intended conclusion is: if all coordinate maps are linearly bounded and the test is quadratically bounded, the empirical average also converges in L1. The conclusion is repairable, but the printed proof has a gap. It defines a weak high-probability boundedness statement with a tail independent of the threshold and then asserts, without derivation, an exp(-c r n) threshold tail.

A correct repair for a fixed finite program is short. Normalized l2 norms propagate under linearly bounded coordinate maps and matrix multiplication. Hence every quadratically bounded empirical test is bounded by a fixed polynomial of the finitely many initial normalized Gaussian-vector norms and Gaussian matrix operator norms. Those base quantities have moments of every fixed order uniformly in n. Thus the empirical tests are uniformly integrable; almost-sure convergence from Theorem 2.10 then implies L1 convergence.

If the program explicitly contains X_0=A_0+A_0^3/3, the printed A.2 hypothesis is not met because this map is cubic. For the fixed-mesh arctan construction one can encode the Euler program directly in A coordinates, where

    A^+=A+delta q(A)R,  |q|<=1,

is linearly bounded jointly in (A,R). Alternatively, one proves uniform integrability directly for the one cubic initialization line.

### Gaussian operator norm

The paper's Fact A.3 attributes a Gaussian operator-norm tail directly to Tao's Corollary 2.3.5. That corollary is stated for entries bounded by 1; the Gaussian extension is only indicated in the following exercise. The citation is therefore not literally exact.

The needed Gaussian fact is nevertheless elementary. For W_ij iid N(0,sigma^2/n), take 1/4-nets N of the two unit spheres, each of cardinality at most 9^n. Then

    ||W||_op <= 2 max_{x,y in N} |y^T W x|,

and each bilinear form is N(0,sigma^2/n). A union bound gives

    P(||W||_op>r)
      <=2 exp(2n log 9 - n r^2/(8 sigma^2)),

so for r above an explicit constant times sigma this is at most 2 exp(-n r^2/(16 sigma^2)). This supplies all uniform fixed moments needed above.

## 2. Proof-level assessment of Theorem 2.10

I read the complete proof, not only its statement. Its structural chain is valid for fixed parameterless programs. Several displayed formulas contain local typographical slips: an undefined Y in the conditioning formula should be the constrained output Z; one conditional variance is written sigma rather than sigma^2; one epsilon factor loses a square; and the high-moment combinatorial lemmas abbreviate a convergent generating-function bound as a bounded o(1). None changes the fixed-program theorem:

- the conditioning formula follows directly by vectorizing the matrix and projecting a centered Gaussian onto the consistent affine constraint space;
- the omitted generating-function bound is finite because, for E fixed edge variables and lambda<1/2,

      sum_{m>=d} binom(m+E-1,E-1) lambda^m
        <= lambda^d (1-lambda)^{-(E+d)},

  and the analogous distinguished-edge sum uses sqrt(2)lambda<1/2;
- the simpler projection-correlation proof printed immediately after the elaborate proof suffices for the strong law;
- the zero-innovation branch is exact, not a division by a singular covariance;
- the positive-innovation branch uses a rank-(n-O(1)) projected Gaussian and the proved high-moment law.

I therefore find no unresolved proof-level defect in Theorem 2.10 for the specialization used here. This conclusion does not extend to the two flawed appendix strengthenings described above.

## 3. Qualification of the L=2 fixed-mesh population oracle

For one fixed Euler mesh delta>0 and one fixed finite number K of steps, the deterministic population-oracle computation qualifies, provided it is written as follows.

1. Use B_0 with iid N(0,1/n) entries as the sole random matrix.
2. Use A_0 with iid N(0,1) entries and an exactly zero left vector C_0 as initial Gaussian vectors. Degeneracy of C_0 is allowed.
3. Replace every empirical scalar in the oracle by its recursively defined deterministic Gaussian expectation.
4. Expand the learned matrix exactly as

       B_k=B_0+sum_{r<k} theta_r D_r H_r^T/n.

   Hence every B_k or B_k^T multiplication is a finite expression involving B_0 or B_0^T, coordinate maps, and deterministic scalar coefficients.
5. Apply the full ZHat/ZDot recursion to every B_0/B_0^T reuse. In particular, the law of B_0^T D_k includes the response generated by every earlier B_0 multiplication on which D_k depends.
6. Keep K fixed as n tends to infinity.

The arctan maps, q(u)=1/(1+u^2), J=(u+u^3/3)^{-1}, their bounded compositions, additions, and the product C q(S) are polynomially bounded. In an A-coordinate encoding they are linearly bounded in all dynamic vector inputs. Thus Theorem 2.10 applies and gives almost-sure convergence of every fixed finite collection of empirical Gram quantities and terminal observables of this oracle.

The actual initialization C_n(0)=n c_n(0), with c_n(0) of variance n^{-4}, has entry variance n^{-2}; it does not satisfy Setup 2.2 because its law depends on n and its finite-width rank does not match the zero limit. It must first be coupled to the exact-zero oracle by a separate finite-step Lipschitz estimate. Its normalized l2 norm is O_P(n^{-1}), so that coupling is feasible for fixed K, but it is not a consequence of Tensor Programs III.

Likewise, the actual empirical error e_k and empirical rank-one coefficients make the literal finite-width iteration a scalar-feedback NETSOR^T+ program. The clean invocation does not apply Theorem 2.10 directly to that program. It compares it, at fixed K, with the deterministic population oracle. The required induction uses the oracle empirical-moment convergence furnished by Theorem 2.10 and deterministic Lipschitz estimates. This bridge must be written separately.

## 4. What the theorem does not give

Theorem 2.10 supplies no:

- rate in n;
- estimate uniform in program length;
- result for K=K_n tending to infinity;
- uniformity as delta tends to zero;
- continuous-time, path-space, or Wasserstein-path convergence;
- convergence in operator norm of B_k or of a learned matrix array;
- closure, uniqueness, or restartability of a continuum action-law flow;
- control of exact GD on a diagonal eta_n with T/eta_n steps;
- automatic convergence of an adaptive or uncountable probe family;
- permission to discard ZDot response terms;
- direct treatment of the n-dependent small random C_n(0).

A predetermined countable family of fixed finite probes can be handled by intersecting their probability-one events, and a bounded weighted product metric can then be used. That elementary countable-intersection step still gives no uniform control over probe depth.

## Verdict

The fixed-finite-mesh deterministic population-oracle invocation is rigorous under the six qualifications above. The primary Master Theorem genuinely handles arbitrary finite B_0/B_0^T reuse and singular oracle covariance. It cannot, by itself, establish the compact-time or joint width/gradient-flow limit. Any proof of the full L=2 construction must supply those uniform stability, cutoff-removal, path-tightness, and diagonal-discretization bridges independently.

The proof must not invoke: (i) Appendix A.1's arbitrary-conditional almost-sure claim; (ii) Appendix A.2 without either satisfying its linearly bounded-map hypothesis and repairing uniform integrability, or giving a direct UI proof; or (iii) Tao Corollary 2.3.5 as though it literally covered Gaussian entries.
