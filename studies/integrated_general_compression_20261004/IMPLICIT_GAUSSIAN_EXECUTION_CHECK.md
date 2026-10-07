# Cross-route check of Gaussian actions and implicit Harmonic execution

2026-10-06. Internal mathematical reconstruction, not an isolated promotion
review, implementation test, or numerical experiment. The reviewer previously
authored LOCAL_CONTINUATION_ASSEMBLY.md, checked the local continuation and
activation backend, and authored IMPLICIT_SETUP_ORDERS.md. That prior knowledge
is disclosed rather than represented as an independent original attempt.
The supervisor supplied the frozen candidates and reported having read them;
the calculations below were reconstructed directly from their complete texts.

## 1. Frozen scope and current disposition

The complete Gaussian candidate was read at SHA-256
24eb0ab622156cd073bfdf457c3746bc02523bfac551e03f47bb8265206efd57.
The complete execution candidate was initially read at SHA-256
ca856e45fa88d7689a7cba3b248b86779f8b61f6e16c25718f495552e56b2382.
Its amended final version was checked at SHA-256
fe3e6dbcde65c050f63d58a6b8995c423d9fd1e2c87eddac8ad2fb391dc6ccf5,
as qualified in Section 7. No candidate was edited by this reviewer.

Supporting inputs are the already checked assembly, core continuation,
activation backend, Taylor/assembly bridge, prior quadrature route and relevant
complete RESULT.md source-selection/metric and factored-cost proofs, at their
recorded hashes. No other study, history or external scientific source was
used. The maintained notation contract was applied. The prescribed canonical
notation skill remains inaccessible, as previously disclosed; the accessible
rigorous-math workflow and explicit repository presentation rules were used.

The sampler proof passes reconstruction. With the coordinate-convention
correction documented in Sections 5 and 7, the final execution identities,
query inventory, work, memory and fixed-parameter exponents also pass.
No unresolved mathematical or operation-count defect was found in this scope.
The conclusions retain
the exact-real, fresh-reference, supplied-certificate and eventual-width
qualifications. They do not certify a finite-precision implementation.

## 2. Gaussian posterior and adaptive queries

For one layer, let \(V,U\) have orthonormal columns and let \(Y,R\) be the
stored answers, so \(Y=WV\) and \(R=W^TU\) in the eventual coupling. Write

\[
P=VV^T,\qquad Q=UU^T,\qquad
M=YV^T+UR^T(I-P).
\]

Compatibility \(U^TY=R^TV\) implies \(MV=Y\) and \(M^TU=R\). The unobserved
linear subspace consists exactly of matrices \(A\) with \(AV=0\) and \(A^TU=0\),
namely \(A=(I-Q)B(I-P)\). Its Frobenius-orthogonal complement contains \(M\).
Thus the asserted posterior kernel is

\[
W=M+(I-Q)G(I-P),\qquad G_{ij}\sim N(0,1/n)
\]

with independent entries in the fresh kernel variable \(G\). This formula is not
assumed merely because the observed directions happen to be orthogonal. It
is established by induction over the full adaptive transcript.

For a new forward direction \(e\) orthogonal to \(V\), with unit norm, the answer
is \(UR^Te+(I-Q)Ge\). Its noise has covariance \((I-Q)/n\), hence the sampler's
projected fresh Gaussian vector gives its exact law. Put \(P'=P+ee^T\). The old
remainder splits as

\[
(I-Q)G(I-P)=[(I-Q)Ge]e^T+(I-Q)G(I-P').
\]

The covariance between the vector and the remaining matrix vanishes because
\(e^T(I-P')=0\). Both are jointly Gaussian, so they are independent, including
degenerate cases. Appending \(e\) and its answer changes \(M\) by precisely the first
term and leaves the asserted fresh projected remainder. A dependent query
returns the stored linear combination and does not condition the remainder.

For a new transpose direction \(f\) orthogonal to \(U\), the answer is
\(VY^Tf+(I-P)G^Tf\). Set \(Q'=Q+ff^T\). The decomposition is now

\[
(I-Q)G(I-P)=f[(I-P)G^Tf]^T+(I-Q')G(I-P).
\]

Again the cross-covariance vanishes. The updated mean equals \(M\) plus the first
term: compatibility gives \(Ph=VY^Tf\) for the new transpose answer \(h\). These
calculations verify both action directions for one shared matrix; they do not
replace the transpose action by an independent Gaussian response.

Condition on all independent client randomness and the global transcript.
The chosen next layer, direction and input vector are then fixed. Conditional
independence of the remaining layer kernels means that observing an answer
updates only its chosen layer. An input computed nonlinearly from another
layer's previous answers is therefore permitted. The sampler's private
Gaussian tape is not made an extra client observation. These facts prove the
global adaptive induction, not only a fixed-query special case.

At bounded stopping, conditioning on the stopped transcript adds no information
beyond the transcript and the stopping decision measurable from it. Completing
each matrix with an independent projected Gaussian remainder gives exactly the
dense model's posterior kernel. Integrating against the identical transcript
law proves the full joint law, including mutually independent unconditional
layer matrices and independence from client randomness. Every past reply is
simultaneously a product with this one completion because later basis appends
preserve all previous answer columns. The completion is not executed or charged
as hidden online work.

## 3. Sampler counts

If the old forward/transpose ranks are \(p,q\), respectively, a new forward
query uses at most \(6np+8nq+9n+1\) arithmetic operations with the candidate's
primitive convention. This is at most \(8n(p+q)+10n\). The dependent-query
branch is smaller, and transposition gives the same bound. Before the \(j\)-th
query, \(p+q\le j-1\). Therefore \(k\) requests cost at most

\[
4nk^2+6nk+2
\]

operations, with the last two for the shared scale \(1/\sqrt n\). These bounds
count every request, not just independent ones. Each query needs one zero
test and at most one full-rank comparison.

Only a new direction draws a Gaussian vector. Once either rank reaches \(n\),
every further new column on the other side is deterministic. At most \(2n-1\)
enlargements can therefore draw, proving \(n\min(k,2n-1)\) scalar draws.
The four retained matrices contain \(2n(p+q)\) words. The stated linked-column
storage and scratch give

\[
2n\min(k,2n)+8n+5\min(k,2n)+64
\]

words. There is no implicit \(n\)-by-\(n\) projector. When the query budget reaches
order \(n\) these bounds can themselves be quadratic or worse; no contrary
uniform compression statement follows from the sampler.

## 4. Exact finite execution and complete access inventory

At panel \(b\), the coefficient identity for a hidden mixer is

\[
[W]_s=-\frac{2}{mns}\sum_{i+k=s-1}U_iH_k^T.
\]

Evaluating its degree-\(K\) endpoint polynomial groups the increment into \(mK\)
outer products. Consequently the finite numerical anchor is exactly
\(W_b=W_0+A_bB_b^T\) with at most \(bmK\) columns per factor. This statement
does not assert low rank for an exact continuously trained increment.

Current-anchor actions use \(W_0x+A_b(B_b^Tx)\), and transpose actions
use \(W_0^Tx+B_b(A_b^Tx)\). Nonconstant coefficient products retain the
causal finite sum

\[
-\frac{2}{mn}\sum_{i+k+c=s-1}
\frac{U_i(H_k^TX_c)}{i+k+1}.
\]

Every index in that sum is below \(s\). This permits exact coefficient-order
induction during the forward/backward training pass, followed by passive
queries against the already generated training jets. The first matrix is
stored explicitly in \(nd\) words; its higher coefficients act through the
training-input inner products. The readout coefficients are ordinary vectors.

The hidden initialized-matrix requests per layer are precisely:

| Purpose | Sufficient number of requests |
| --- | ---: |
| Original-activation initial features and their saved forward images | \(m\) |
| Forward/transpose actions for all training/passive jets | \(2J(m+N_x)(K+1)\) |
| Initialized images of completed base source coefficients | \(2N\) |
| Full final source-basis image needed by the compressed mixer | \(r\) |

Thus \(k_*=m+2J(m+N_x)(K+1)+2N+r\) is valid. The last row cannot in
general be omitted: source/image pairing need not provide initialized actions
on every basis vector of the final source spaces. Conversely none of the
selection or metric formulas requires additional entries or products.

The sampler statement initially uses deterministic budgets, whereas the actual
rank \(r\) is transcript-dependent. To apply its theorem literally, use the
deterministic upper budget obtained by replacing \(r\) by \(\min(n,R)\). The same
per-query calculation then yields the sharper displayed work and memory with
the realized \(r\). This resolves the interface without changing either algorithm
or exponent and without assuming the actual rank in advance.

Original initialized features are computed with the original activation, not
the disposable polynomial. The original backward fields are zero because the
readout is initialized at zero. Global source-image coefficients are formed
using \(W_0\), never by relabelling current-anchor \(W_b\) actions. They are the exact
images of the completed base coefficients by linearity. The checked bridge's
Euclidean nodal estimate supplies the separate image-error bound.

Fixing generator order, exact orthogonalization conventions and selector
tie-breaking makes ranks, bases, supports, weights and metrics identical under
the sampler coupling. The final basis images then give the same compressed
mixers and initial readout solve. All subsequent scalar operations see the
same operands. The original all-time source/comparison event may be evaluated
on the mathematically completed dense reference, without testing that event
or any hidden matrix norm inside the algorithm.

## 5. Coordinate convention corrected during this check

The initially frozen execution text calls its local jets coefficients of
\((t-\tau_b)^c\), but its temporal moment table uses
\(((t-\tau_b)/\Delta_b)^c\). Before applying that table, each raw source jet
coefficient must therefore be rescaled to

\[
G_{b,c}=\Delta_b^c[g]_{b,c}.
\]

These are exactly the source coefficients in the checked assembly interface.
Without that conversion, the displayed moment table is not the raw-coefficient
projection for a general panel length. The reviewer reported this omission
before final certification. Forming powers and applying this rescaling costs
\(O(JLnN_x(K+1))\) arithmetic and fits the existing projection envelope, with
no new persistent buffer. It does not alter any approximation, rank or degree.
The final candidate now specifies this exact rescaling explicitly.

## 6. Work, memory and structural qualification

The following independent count reconstruction found no omitted dense-matrix
operation. Gaussian action work is \(O((L-1)nk_*^2)\). Applying retained
anchor factors sums \(bmK\) across panels and costs
\(O((L-1)nm(m+N_x)J(J-1)K(K+1))\); factor storage is
\(O((L-1)nJmK)\). The present-panel contractions cache \(H_k^TX_c\),
then combine scalar weights before vector accumulation. Their total is
\(O(JLm(m+N_x)(K+1)^2(n+K+1))\), including rank-factor formation.

The polynomial backend costs \(O(L(D+1)^2)\) preparation plus
\(O(JLn(m+N_x)(D+1)(K+1)^2)\) composition work. Exact original
activation calls and Gaussian draws are separately counted, not inferred from
analyticity. First-matrix, training-input pairings, initial Gram and solve
costs are present explicitly in the candidate's full envelope.

Panel-major spatial-first projection retains only global source coefficients
and one panel's angular buffer. It charges
\(O(LnJ(K+1)(N_xH_{\rm sph}+N))\), not \(N_x\) independent dense trajectories
and not \(J\) copies of the global rank. The scalar temporal tables, assignment
of time nodes, angular quadrature generation, separated harmonic evaluation
and recomputation on every panel are charged with matching memory. Normalizing
the source coefficients as in Section 5 is absorbed by this same envelope.

Rank-aware source orthogonalization costs \(O(LnRr)\). The conservative barrier
selector costs \(O(Lnr^3)\): each of at most \(9r\) iterations uses an
\(O(r^3)\) inverse and \(n\) quadratic forms of cost \(O(r^2)\), with
\(r\le n\). Selection uses only the already known row vectors. With \(P\)
the selected basis rows, \(\mathsf D\) the positive diagonal weights and
\(G=P^T\mathsf DP\), direct multiplication verifies

\[
M=\mathsf D+\mathsf DP(G^{-2}-G^{-1})P^T\mathsf D,\qquad
M^{-1}=\mathsf D^{-1}+P(I-G^{-1})P^T.
\]

Thus metric and final retained-mixer formation cost
\(O(L(qr^2+r^3+q^2r))\); the intermediate basis contraction additionally
costs \(O((L-1)nr^2)\). All relevant inverses are small matrices already
available from source rows. They are not dense-reference operations.

The candidate's peak-memory envelope includes sampler bases and answers,
historical anchor factors, online polynomial composition tables, contraction
caches, complete global coefficients, one panel angular buffer, explicit first
matrix, final selected state and caches, scalar geometry and data. There is no
whole-path buffer or uncharged vector of n-squared parameter coordinates.
The phase-buffer sum is conservative but valid.

At the certified fixed-parameter specialization, substitute
\(J=O(\log(en)^{3/2})\), \(K=O(\log(en))\), \(D=O(\log(en)^{3/2})\),
\(N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2})\), and
\(N,R,r,q=O(\log(en)^{3d/2+1})\).
Then \(k_*=O(\log(en)^{3d/2+1})\). The action term has logarithmic
exponent \(3d+2\), the anchor-history and activation terms have exponent
\(3d/2+7/2\), and the selector has exponent \(9d/2+3\).
Every other width-proportional term fits that last exponent for every integer
\(d\ge1\); remaining pure polylogarithmic
terms do also for sufficiently large n. Hence the stated sufficient bounds

\[
T_{\rm setup}=O(n\log(en)^{9d/2+3}),\qquad
M_{\rm setup}=O(n\log(en)^{3d/2+1})
\]

follow in the bounded-cost primitive model. The two-point convention makes
these checks valid at \(d=1\). They are near-linear fixed-parameter bounds, not
strict \(O(n)\), not jointly polynomial bounds in all structural parameters, and
not uniform subquadratic bounds at arbitrary supplied orders. The actual
scalar primitive costs must be added as stated in the candidate.

The final retained model inventory is unchanged. Disposal of the Gaussian
transcript and continuation state does not leave a hidden runtime oracle.
The proof does not reproduce a supplied dense matrix or prescribed entrywise
seed, quantify the inherited eventual-width event, compute arbitrary activation
moment certificates, or establish numerical stability/bit complexity. It
also does not show superiority over every competing high-order or implicit
dense solver, which could use the same sampler.

## 7. Final-hash qualification

The final execution version
fe3e6dbcde65c050f63d58a6b8995c423d9fd1e2c87eddac8ad2fb391dc6ccf5
adds the deterministic request cap explained in Section 4 and explicitly
rescales each passive source coefficient by \(\Delta_b^c\) before applying
the affine-coordinate moment table, as required in Section 5. Both inserted
passages were read and checked in full. Removing exactly those two changes
in memory and hashing the resulting text recovered the complete originally
reviewed hash
ca856e45fa88d7689a7cba3b248b86779f8b61f6e16c25718f495552e56b2382.
Thus no unreviewed change is hidden in this final-hash qualification.

The Gaussian candidate remains bound to
24eb0ab622156cd073bfdf457c3746bc02523bfac551e03f47bb8265206efd57.
Combining these two frozen versions meets the checked execution's sampler
contract and closes the finite algebraic access/cost interface in the stated
exact-real fresh-reference model. The conditional source accuracy and retained
model guarantees remain those of the already checked component proofs, not
new unconditional guarantees supplied by this check.
