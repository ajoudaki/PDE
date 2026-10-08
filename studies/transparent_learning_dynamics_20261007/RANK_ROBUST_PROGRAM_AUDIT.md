# Independent audit of the rank-robust finite-program theorem

2026-10-07. Reviewer: the kinetic-route agent. Assignment: audit the complete frozen `RANK_ROBUST_FINITE_PROGRAM.md`, with scientific access limited to that file and the reviewer's own prior notes. Required skills remain current. No author-route file, other research source, external search, experiment, or Git material was consulted. The author's file was not edited.

Reviewed SHA256: `baf872d95919981848b0b0d7958b737426feffb6a29508d7ea1870365c815f62`.

## Verdict

**PASS, with the stated fixed-program limitations.** I found no failure in the deterministic rank selection, conditional Gaussian simulator, original/simulator coupling, dimension-independent coordinate sensitivity bound, Gaussian concentration argument, or transfer to continuous polynomial-growth observables. The proof establishes a qualitative law for each fixed program in the specified bounded-query, globally Lipschitz, permutation-equivariant grammar.

One wording clarification is useful: “constant vector registers” must mean broadcasts of fixed scalar constants, or otherwise be explicitly permutation invariant. Arbitrary deterministic coordinate arrays are not covered by the symmetry argument. The prohibition on coordinate-index masks and the stated equivariance support the broadcast interpretation, which is the interpretation used for this PASS. If arbitrary deterministic arrays were intended, that would be a substantive change of hypotheses requiring a different initial-law and moment argument.

The result does not give a rate uniform in program length or near a change of population rank; an unclipped neural-flow comparison; a time-mesh limit; or a finite autonomous closure for an infinite-time trajectory. The author states those limits accurately. There is no source-label qualification claim to audit here.

## 1. Reading and check coverage

I read every line of Sections 1–9, including the complete operator-norm and Gaussian concentration derivations. I reconstructed the conditional mean and covariance formulas, the rank-omission coupling, the Gaussian-coordinate Lipschitz induction, and the interpolation step. Boundary cases checked were empty histories, zero inputs, exactly repeated inputs, singular Gaussian seeds, positive but arbitrarily small innovation variance, finite-width accidental rank loss, repeated use of a matrix in both directions, and connections whose input and output are the same population.

No specialized external theorem was imported. The proof includes the needed Gaussian concentration argument, and the remaining finite-dimensional variance, norm, and conditioning steps can be verified directly as below. This is an internal mathematical audit, not a promotion review.

## 2. Deterministic scalar construction and rank decisions

At a forward query, the retained input history has Gram matrix

\[
\Gamma_H=\mathbb E[HH^\top],\qquad
a=\Gamma_H^{-1}\mathbb E[Hh],\qquad
e=h-H^\top a.
\]

Thus \(\mathbb E[He]=0\). If the innovation variance \(\sigma^2=\mathbb E e^2\) is positive, the augmented Gram is positive definite because

\[
\mathbb E(u^\top H+vh)^2
=(u+va)^\top\Gamma_H(u+va)+v^2\sigma^2.
\]

This expression can vanish only when \(v=0\) and then \(u=0\). If \(\sigma^2=0\), the relation \(h=H^\top a\) holds almost surely in the input-population law. It is then consistent to return \(Y^\top a\) without adding a retained direction. The backward argument is identical.

The decisions depend only on already constructed deterministic laws, so the retained instruction indices and the skip coefficients are deterministic for a fixed program. The proof does not choose a random threshold from finite-width Grams. Positive but very small eigenvalues cause potentially large fixed analysis constants, not an invalid inverse or an unannounced uniform-rank assumption.

Empty histories are handled correctly by empty products. A zero first query has variance zero and gives zero output; a nonzero first query starts the corresponding retained history. Singular seed covariance creates no difficulty because no seed inverse is taken. The scalar Gaussian laws have all finite moments by induction through globally Lipschitz coordinate operations and finite linear combinations at queries.

The rank decision is a mathematical existence construction. Deciding exactly whether a general Gaussian integral vanishes, and computing arbitrarily ill-conditioned moment coefficients effectively, are not established numerical procedures. The author explicitly acknowledges this distinction.

## 3. Adaptive Gaussian conditioning is used on the right transcript

Write the retained finite-width constraints for one matrix as

\[
GH=Y,\qquad G^\top D=X.
\]

Here \(H,D\) contain query inputs, while \(Y,X\) contain their actual responses in the modified simulator. Its skipped queries return deterministic linear combinations of previous responses and never inspect the missing product. Consequently neither a skip decision nor its returned value imposes an additional matrix constraint.

Conditional on the existing transcript, the next query vector is fixed. Revealing its response is therefore a linear observation of the remaining Gaussian matrix. This is the needed predictability statement. Other matrices remain independent in their unrevealed Gaussian subspaces: at each induction step the chosen observation acts on just one of those conditionally independent remainders, with coefficients fixed by the already conditioned transcript. Nonlinear ordinary instructions are functions of the transcript and add no information.

For an isotropic matrix with entries \(N(0,1/n)\), the homogeneous constraint space is

\[
\{B:BH=0, B^\top D=0\}
=\{(I-P_D)B(I-P_H):B\in\mathbb R^{n\times n}\}.
\]

The displayed map is its orthogonal projection in the Frobenius inner product. The candidate conditional mean

\[
M=Y(H^\top H)^\dagger H^\top
+D(D^\top D)^\dagger X^\top(I-P_H)
\]

is orthogonal to that homogeneous space. It satisfies both constraints using \(D^\top Y=X^\top H\), together with the kernel consistency identities automatically satisfied by actual query responses. Thus subtracting \(M\) and projecting an independent Gaussian matrix gives precisely the conditional covariance and conditional law in the note's equation (10). The pseudoinverse formula remains valid for finite-width dependent histories.

The scalar retained Grams are positive definite. Their empirical counterparts converge entrywise by the simulator moment induction, so their smallest eigenvalues converge to positive numbers and they are invertible with probability tending to one. The proof works on this event only for the inverse-based asymptotic calculations. Discarding its vanishing-probability complement is legitimate for convergence in probability and does not redefine the simulator there.

For a forward query, the exact conditional mean is

\[
Ya_n+Dq_n,
\qquad
a_n=(H^\top H/n)^{-1}H^\top h/n,
\quad
q_n=(D^\top D/n)^{-1}X^\top(h-Ha_n)/n.
\]

The conditional noise equals

\[
\sigma_n(I-P_D)\xi,
\qquad
\sigma_n^2=\|h-Ha_n\|_{2,n}^2,
\]

with a fresh standard Gaussian vector independent of the old transcript. The factors of \(n\) agree with entry variance \(1/n\). No independence between a query and its matrix is assumed.

Coefficient limits use only pairings within the appropriate population: \(H,h,X\) are input-population registers; \(D,Y\) are output-population registers. No unexplained coordinatewise coupling between different populations enters. For a self-connection all these registers are in the same population and the same argument remains valid.

## 4. Simulator convergence, including projected Gaussian noise

Given the history, write

\[
P_D\xi=D\beta_n,
\qquad
\beta_n=(D^\top D/n)^{-1}D^\top\xi/n.
\]

Its conditional covariance is

\[
\operatorname{Cov}(\beta_n\mid\text{past})
=\frac1n(D^\top D/n)^{-1}.
\]

On events where the inverse norm is bounded, conditional second moments give \(\beta_n=O_{\mathbb P}(n^{-1/2})\). The probability of those events tends to one, yielding the unconditional probability statement. There are finitely many retained columns. Their empirical norms are bounded in probability; in fact the query-input assumption gives deterministic coordinate bounds. Hence

\[
\|P_D\xi\|_{p,n}
\le\sum_j|\beta_{n,j}|\|D_j\|_{p,n}
=o_{\mathbb P}(1)
\]

for each fixed finite \(p\). The same argument applies to \(P_H\xi'\) for a backward query.

Replacing the other finite-dimensional coefficients by their limits also gives an error vanishing in every finite empirical norm, since all prior registers have bounded empirical moments by induction. Adding the fresh coordinatewise Gaussian innovation preserves convergence of polynomial-growth tests: conditional expectation is a continuous polynomial-growth test of the old row, and conditional variance is bounded by \(C n^{-1}\) times an empirical moment of a fixed finite order. Tightness of that moment suffices for conditional Chebyshev after restriction to a bounded-moment event.

These arguments preserve the full joint law of all existing registers in the target population, not just the marginal law of the new output. This is necessary for later reused matrices and coordinate operations, and the proof supplies it. Finite simultaneous convergence across tests and populations uses only a finite union bound; it does not assert a uniform law over an unrestricted test class.

## 5. Coupling the simulator to the original program

The original and modified programs use the same initial matrices and seeds. On
\(\Omega_{n,R}=\{\max_e\|G_e\|_{\rm op}\le R\}\), a retained query obeys

\[
\|Gh-G\widehat h\|_{2,n}
\le R\|h-\widehat h\|_{2,n}.
\]

For a skipped forward query, convergence of the simulator's joint second moments gives

\[
\|\widehat h-\widehat H a\|_{2,n}^2
\longrightarrow\mathbb E(h-H^\top a)^2=0.
\]

The simulator retains the exact identity \(G\widehat H=\widehat Y\), so

\[
Gh-\widehat Y a
=G(h-\widehat h)+G(\widehat h-\widehat H a).
\]

This is the correct decomposition: it never falsely treats a skipped finite-width query as exactly dependent. The operator-norm bound makes both terms negligible in normalized Euclidean norm. The transpose case is the same. Global Lipschitz coordinate/scalar operations and empirical bounded Lipschitz reductions preserve this comparison, and a finite instruction list permits induction without any uniform-in-length estimate.

The proof uses inverse Grams only in analysis of the simulator law. An inverse of a small empirical Gram is not an operation in the original program and cannot amplify a discarded small direction. That distinction is essential and is made correctly.

## 6. Dimension-independent concentration and moments

### Operator norms

The \(1/4\)-net cardinality \(9^n\) and the factor two in the bilinear net estimate are correct. Two vector approximations each contribute at most \(\|G\|_{\rm op}/4\). For each net pair the Gaussian variance is \(1/n\), yielding

\[
\mathbb P(\|G\|_{\rm op}>R)
\le2\exp(2n\log9-nR^2/8).
\]

A fixed sufficiently large \(R\) gives exponential decay for a fixed finite collection of matrices, including a failure probability below \(1/16\) for every \(n\ge1\). Integrating above a fixed large threshold gives all uniform operator-norm moments. No width-dependent norm bound is hidden here.

### Gaussian concentration proof

The averaging-operator calculation has the correct constants. Its generator is \(\Delta-x\cdot\nabla\), gradient commutation contributes \(e^{-t}\), and the integration of \(e^{-2t}\) gives the factor \(1/2\) in

\[
\operatorname{Ent}(F)\le\tfrac12\mathbb E\frac{\|\nabla F\|^2}{F}.
\]

With \(F=e^{\lambda f}\), this gives
\(\lambda H'(\lambda)-H(\lambda)\le\lambda^2K^2/2\). Integrating \((H/\lambda)'\) from zero yields the stated centered Gaussian exponential-moment estimate. Bounded smooth approximations justify the initial differentiations. Clipping and smoothing a Lipschitz function, followed by Gaussian domination at fixed dimension, extend the inequality without increasing \(K\). The result depends only on \(K\), even though the domination argument for taking the approximation limit is performed separately in each finite dimension.

### Lipschitz constants of original coordinates

The primitive standard Gaussian vector consists of entries of the unscaled matrices \(J_e\) and standardized seeds. The distinction between \(J_e\) and \(G_e=J_e/\sqrt n\) is correctly retained.

For two primitive realizations in the norm event, bounded query input gives

\[
\|Gh-\widetilde G\widetilde h\|_2
\le R\|h-\widetilde h\|_2
+\|J-\widetilde J\|_F\|\widetilde h\|_2/\sqrt n
\le R\|h-\widetilde h\|_2+B\|J-\widetilde J\|_F.
\]

Thus vector-register Lipschitz constants are independent of width. A scalar empirical reduction has the additional factor \(1/\sqrt n\), by Cauchy–Schwarz on its normalized sum. Broadcasting such a scalar into a coordinate operation restores a factor \(\sqrt n\), exactly canceling that gain. Consequently the vector and scalar bounds in equations (20)–(21) propagate together through every original-program instruction. No maximum over coordinates, or factor depending on the primitive dimension \(O(n^2)\), is introduced. The resulting coordinate Lipschitz constant can grow with the fixed program length but not with \(n\).

### Equivariance, centering, and localization

Independent coordinate permutations within populations, with matching matrix row/column permutations, preserve the joint primitive law. They also preserve the computation when vector constants are broadcasts and the coordinate functions are shared as specified. Self-connections use conjugate row/column permutations of the same matrix and still preserve its independent-entry Gaussian law. Thus coordinates of each original output register are exchangeable.

For an adaptive bounded input this yields

\[
\mathbb E|y_i|^2
=\mathbb E\|Gh\|_{2,n}^2
\le B^2\mathbb E\|G\|_{\rm op}^2.
\]

Independence between \(h\) and \(G\) is unnecessary. The second-moment bound controls a fixed interval containing \(y_i\) with large probability.

The infimum extension from the operator-norm event is finite and \(K\)-Lipschitz. Finiteness follows by comparing every candidate point to a fixed point of the nonempty event and applying the existing Lipschitz inequality; the triangle inequality supplies a finite lower bound. On the event it equals the original coordinate. Combining the event probability and the second-moment interval yields \(\mathbb P(|\widetilde y_i|\le A)\ge7/8\).

This step addresses a real issue: a dimension-independent Lipschitz constant alone would not bound the mean of the extension in a growing Gaussian dimension. Here the mass in a fixed interval, together with the one-sided Gaussian tail estimate, bounds the extension's mean uniformly. The displayed threshold \(A+K\sqrt{2\log8}\) is conservative and valid. Gaussian tails then give all uniform moments of the extension.

Outside the operator-norm event, the deterministic bound
\(|y_i|\le B\sqrt n\|G\|_{\rm op}\) remains valid. Cauchy–Schwarz combines this polynomial factor in \(n\) with the exponentially small event probability and uniform operator-norm moments. The resulting \(n^{q/2}e^{-cn/2}\) is bounded for every fixed finite \(q\). Thus all moments of each original raw query coordinate are indeed uniform in width. Global Lipschitz coordinate operations and deterministically bounded scalars propagate these moments to every original register.

This population moment argument is stronger than merely showing that typical sampled coordinates lie in a clipping range. It supplies the tail control actually needed for the polynomial-observable transfer.

## 7. Final transfer and precise limitations

For a fixed \(p>2\), choose \(q>p\). Both simulator and original registers have empirical \(q\)-norms bounded in probability, while their difference has empirical 2-norm tending to zero. The normalized finite-measure interpolation inequality gives

\[
\|v-\widehat v\|_{p,n}
\le\|v-\widehat v\|_{2,n}^{\theta}
\|v-\widehat v\|_{q,n}^{1-\theta}
\longrightarrow0,
\qquad 1/p=\theta/2+(1-\theta)/q.
\]

For \(p\le2\), monotonicity of normalized norms suffices. The compact-set uniform-continuity argument, with a higher moment to control tails, then transfers each fixed continuous polynomial-growth test from the simulator to the original program. It does not require differentiability of that test. Finitely many registers cause no issue for joint row norms.

The resulting law is a finite scalar probabilistic recipe for each fixed instruction list. Its coefficients are deterministic expectations under previously constructed scalar laws. It is not a realized dense-weight encoding. However, finite description at this level does not establish a computable, stable procedure for exact rank decisions, a polylogarithmic approximation rate, or restartable finite-state dynamics for a continuum trajectory. Those conclusions are explicitly excluded in the source.

The theorem's proof is consistent at the claimed qualitative scope. The single interpretation to make explicit when stating it independently is that constant vector registers preserve the asserted coordinate permutation symmetry. With that reading, I recommend accepting this candidate as internally checked for the finite clipped globally Lipschitz program theorem, while keeping every listed neural-flow and quantitative extension open.
