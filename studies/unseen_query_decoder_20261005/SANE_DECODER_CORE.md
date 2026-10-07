# A smaller, explicitly counted response-decoder core

2026-10-06. Scoped author derivation, not independent review or promotion.
No experiment, maintained-source edit, or Git operation was performed.

The existing powers 408 and 1168 are not intrinsic precision or memory
requirements. Three concrete changes remove much of their origin:

1. Estimate sensitivity through the causal graph of named fields once,
   rather than through every scalar arithmetic slot and then again through
   every scalar-summary prefix.
2. Solve two-orientation conditioning through the two history matrices,
   without materializing a matrix of squared history dimension.
3. Fool one-pass tests for a bad median, whose state is a scalar sum and
   counters, instead of using the much larger median-output interpreter as
   the finite-state test.

The first two changes also permit coefficient preparation once per fixed
query context and ordinary quadratic row arithmetic thereafter. Explicit
core bounds below are much smaller than the old cofactor-interpreter
bounds. They do **not** establish fourth- or fifth-power logarithmic total
resources. In particular the number of physical history fields and the
existing exact support-selection algorithm remain separate costs.

## 1. Contract, inputs, and units

Keep the nonlinear network, label intersection, independent dense
reference, entire sphere, physical trajectory, and endpoint contract of
`COST_CONTRACT.md`. The approximation target remains its dense-pair upper
certificate. No population expectation is supplied to the algorithm; no
training evolution is replayed at query time. A query evaluates the row
response circuit at the current retained scalar transcript.

The scientific inputs read completely were `COST_CONTRACT.md`,
`QUADRATIC_RESOURCE_RESULT.md`, `EXPLICIT_COMPILER_EXPONENT.md`,
`COMPILER_PARAMETER_ACCOUNTING.md`, `RECALIBRATION_FREE_MOMENTS.md`
(including Section 10), `SHORT_SEED_PRIOR_BLOCKS.md`,
`FAST_SMALL_MATRIX_FUNCTIONS.md`, and `PHYSICAL_PARAMETER_ACCOUNTING.md`.
The maintained notation contract was read. The custom canonical-notation
skill was permission-inaccessible, with no readable replacement in the
available skill roots; its explicit repository notation requirements were
applied directly. The research-contract, evidence, adversarial-audit, and
rigorous-mathematics instructions were read and applied.

Let `n,m,d,L,gamma,Y,beta,delta` retain their meanings in the cost
contract. In the modular counts, let `R >= 2` bound the **actual** number
of named physical fields, initialized-matrix calls, examples and layers.
Let `P <= C R^2` count retained scalar summaries, `D <= d+C R` the
Gaussian packet dimension, and `r_h <= C R` the number of history marks
in one vector integral. Since `d <= m <= R`, we can use `D <= C R`.
All constants `C` in this note are universal.

Use the logarithmic numerical certificate `chi` of
`COMPILER_PARAMETER_ACCOUNTING.md`, equation (3), **after** including its
Section 8.2 common-Gram ridge and whitening bounds. Thus `chi` covers
operand logarithms, inverse-floor logarithms, primitive Lipschitz
logarithms, and logarithms of dimensions. Set

\[
 \Theta=2+\chi+\log_2(n+2)+\log_2\delta^{-1}
                         +\log_2\epsilon^{-1},
 \qquad 0<\epsilon<1.                                    \tag{1}
\]

For the contract one takes normalized deterministic allowance
`epsilon=n^(-10)` (a fixed universal exponent). This is not a free
accuracy parameter hidden in an asymptotic constant. Evaluator and input
costs are separate throughout.

## 2. Causal depth, rather than scalar-slot count

### Lemma 1: a sufficient precision proportional to causal depth

The protected source schedule and its fixed-context row response can be
organized in at most `C R` causal phases, each with Lipschitz constant at
most `2^(C chi)` in the maximum of the relevant scalar and Frobenius
norms. Here a phase may have many parallel pair moments or entries; their
number contributes through the dimension factors already in `chi`.
Consequently both the complete source/acquisition map and the row map at
a supplied history have logarithmic Lipschitz bound

\[
             \log_2(1+\Lambda)\le C R\chi.                \tag{2}
\]

This statement uses the existing chronological convention: a previously
created field retains the scalar arguments at its creation time. It would
be false for a program that changed every old field when a later summary
was appended.

**Proof.** Group the exact mathematical schedule as follows.

* A newly named physical field is obtained from old fields by a bounded
  number of linear combinations, products, activations, projections, or
  one Gaussian conditioning operation. Long dot products and matrix
  products are treated as multilinear maps, not chains of scalar
  additions. Their Lipschitz constants are bounded by dimension times
  operand norms. This is at most `2^(C chi)`.
* All raw pair moments made available after a field is created can be
  formed in one parallel phase. A product has Lipschitz constant at most
  twice the operand cap. A normalized empirical average or a convex
  weighted average has norm at most one from the maximum row error to
  its scalar error. There is no factor `n` in that norm.
* The coefficient operations for one new field have bounded macro depth.
  Matrix inverse, positive square root, positive part, and radial cap
  are their exact mathematical maps. Their Lipschitz bounds are the
  gapped inverse/root bounds and nonexpansive projections already proved
  in the assigned compiler. Matrix dimension conversions cost a power of
  `R`, whose logarithm is included in `chi`.
* In particular the globally defined common-Gram extension is
  `tau I+(Q_obs+tau I)_+`. It has floor `tau`. Inverse square root has
  Frobenius Lipschitz constant at most `(1/2)tau^(-3/2)`. The raw mean,
  variance-selection and whitened-mark operations then have a bounded
  number of matrix multiplications and protected roots. Section 10's
  operand caps and Section 8.2's parameter-explicit ridge put their
  logarithmic constants inside `C chi`; their numerical eigensolver
  iterations are not extra depth of the mathematical map.
* The integrated cardinal coefficients at a within-patch coordinate have
  derivative equal to their cardinal polynomial. The source's bound
  `|l_j| <= 2` bounds this dependence directly. Their cosine recurrence
  need not be treated as a new conditioning chain. Coefficients at fixed
  nodes are fixed literals.

A path through this graph can cross only `C R` newly named fields and
their associated moment/coefficient phases. Several pair moments between
two such phases do not depend on one another. If a projection needs its
own newly obtained norm moment, its projected field is another named
field and is included in `R`.

For completeness let `e_j` be the largest perturbation among values
available by phase `j`, and let `u` bound the phase's additive numerical
or noise error. With `A=2^(C chi) >= 2`,

\[
 e_{j+1}\le A e_j+u,\qquad
 e_j\le A^j e_0+u\frac{A^j-1}{A-1}.                     \tag{3}
\]

There are at most `C R` phases. This proves (2) and bounds accumulated
additive errors by `2^(C R chi)` times their largest local size.
The proof applies to the full `n`-row program, to the selected convex
panel, or to one fixed-history row. It is a property of the finite
causal graph; executing that graph by repeated row evaluations does not
add another mathematical composition. QED.

This removes the extra factor `P` from the old use of
`P log(1+Lambda_row)`: that argument re-counted all predecessors each
time a new scalar summary was acquired. It also replaces scalar-slot
count `R^7` by causal phase count `R`.

The source-noise, retained-history, pair-test, and quantization conditions
can therefore all be met with

\[
 p_a\le C R\Theta,\qquad
 \log_2\eta^{-1}\le C R\Theta,\qquad
 p_{\rm ctx}\le C R\Theta.                              \tag{4}
\]

These are sufficient choices, obtained by taking sufficiently large
universal constants, not upper bounds on arbitrary larger choices.
For example the common-Gram condition is

\[
 r_h\{\eta T_\rho+(1+L_{\rm pair})\epsilon_{\rm hist}\}
 \le\tau/8,
\]

where `T_rho=sqrt(P/(beta_noise rho))`, with `beta_noise` its assigned
failure share, and `rho` a fixed conditional share. Its logarithmic
requirements are `C R chi + C log(delta^(-1))`; `tau` is already in
`chi`. Finite Gaussian coupling adds `log(nD/delta)`. Perturbing positive
panel weights by at most `2^(-p)` adds at most
`(P+1) B_F 2^(-p)` before (3), so also fits (4). Exact common-denominator
weights can instead be retained unchanged.

The deterministic ridge is unchanged: it must still satisfy equation
(7) of the parameter-accounting note. This lemma does not replace its
physical propagation constants by numerical worst-case caps.

## 3. Conditioning without a Kronecker matrix

### Lemma 2: explicit separate-spectrum formulas

Let `Q` be a positive semidefinite `s`-by-`s` matrix and `K` a positive
semidefinite `t`-by-`t` matrix, with `s,t <= C R`. Let `sigma>0`,
`v` be in `R^s`, and let `c` be the input squared RMS. Write

\[
 Q=O_Q\operatorname{diag}(q_i)O_Q^T,\qquad
 K=O_K\operatorname{diag}(k_j)O_K^T,\qquad
 \widetilde v=O_Q^Tv.                                    \tag{5}
\]

The orthogonal bases are internal computational coordinates; no continuity
of their choice is assumed. Define

\[
 a_j=\sum_{i=1}^s\frac{\widetilde v_i^2}
                            {\sigma^2+k_j+q_i},\qquad
 b_j=\sum_{i=1}^s\frac{\widetilde v_i^2}
                 {(\sigma^2+q_i)(\sigma^2+k_j+q_i)}.      \tag{6}
\]

The compiler's two Kronecker contractions are exactly

\[
 B_1=O_K\operatorname{diag}(a_j)O_K^T,\qquad
 B_2=O_K\operatorname{diag}(b_j)O_K^T.                     \tag{7}
\]

To verify (7), diagonalize
`sigma^2 I+K tensor I+I tensor Q` by `O_K tensor O_Q`.
Its inverse multiplies coordinate `(j,i)` by
`1/(sigma^2+k_j+q_i)`. Contracting its two sides with `I tensor v`
gives the first formula. The other contraction uses
`C v`, where `C=(sigma^2 I+Q)^(-1)`, whose `i`th transformed coordinate
is `v_tilde_i/(sigma^2+q_i)`, giving the second.

For arbitrary cross blocks `H,J` of size `t` by `s`, the Sylvester
equation

\[
 (\sigma^2I+K)E+EQ=-HC-DJ,
 \qquad D=(\sigma^2I+K)^{-1},                            \tag{8}
\]

is solved by transforming its right side with `O_K^T` and `O_Q`, dividing
entry `(j,i)` by `sigma^2+k_j+q_i`, and transforming back. This requires
ordinary matrices of dimensions at most `max(s,t)` and at most
`C(s+t)^3` scalar arithmetic operations.

There is further structure. Put

\[
 f_0=c-\sum_i\frac{\widetilde v_i^2}{\sigma^2+q_i},
 \quad v_0=\sigma^2+\max\{f_0,0\},
\]
\[
 f_j=\frac{\sigma^2(c-a_j)}{\sigma^2+k_j},\qquad
 h_j=\frac{-f_0+\sigma^2 b_j}{\sigma^2+k_j}.              \tag{9}
\]

The exact covariance matrix `F` and correction numerator `H_f` are both
diagonal in the `O_K` basis, with eigenvalues `f_j` and `h_j`. Thus the
protected correction matrix is

\[
 T=O_K\operatorname{diag}\left(
 \frac{h_j}{\sqrt{\sigma^2+\max\{f_j,0\}}+\sqrt{v_0}}
                           \right)O_K^T.                \tag{10}
\]

On the consistent Gram domain `f_j>=0` and `f_0>=0`, so the protections
are identities. Off that domain they are precisely the positive-part
and scalar-maximum protections in the given compiler. All divisors have
their stated `sigma` or `sigma^2` floors. Empty histories are omitted.

Once the vectors `C v` and `D x+E v+T z` and the scalar `sqrt(v_0)`
are formed, the row answer is a linear combination of old named row
fields and one fresh Gaussian coordinate. Only `C R` coefficients from
that conditioning call are retained. Its temporary matrices are discarded.

This is the same protected mathematical map, not a replacement by a
low-rank approximation. No matrix of dimension `s t` is materialized.

## 4. A finite-bit spectral implementation with modest scratch

### Lemma 3: residual-controlled symmetric diagonalization suffices

Let a symmetric dyadic `r`-matrix have norm at most `M>=1`, input
precision `p`, and, when needed, positive floor `a<=1`. To obtain inverse,
positive square root or positive part to Frobenius error `2^(-b)`, set

\[
 v=2+p+b+\log_2(r+2)+\log_2(M+2)+\log_2a^{-1}.           \tag{11}
\]

Omit the last term for positive part. There is an elementary algorithm
with bit work and scratch at most

\[
 C(r^4v^2+r^3v^3),\qquad C r^2 v.                       \tag{12}
\]

Its output for a positive matrix function can be exactly positive
semidefinite. Constants in this lemma are universal.

**Construction and error accounting.** Use largest-off-diagonal Jacobi
rotations. If the off-diagonal Frobenius norm is `e`, a largest entry
has squared magnitude at least `e^2/[r(r-1)]`. An exact plane rotation
annihilating it reduces the squared off-diagonal norm by twice that
entry's square. Consequently the exact one-step contraction factor is
at most `sqrt(1-2/[r(r-1)])`.

Every iteration recomputes a largest entry of the current symmetric
dyadic matrix. It does not follow the unstable eigenvectors of a
reference matrix. Compute the rotation to `w=C v` bits and update the
matrix and the accumulated basis with symmetric grid rounding. A
rotation's entry error at most `2^(-w)` and matrix rounding contribute
at most `C r M 2^(-w)` in Frobenius norm. The off-diagonal recurrence is
therefore

\[
 e_{j+1}\le\sqrt{1-2/[r(r-1)]}\,e_j
                           +C r M2^{-w}.                \tag{13}
\]

Stop if `e_j` is below a prescribed residual tolerance, or after
`C r^2 log(rM/tolerance)` rotations. Choose `w` so the stationary
error in (13), and the accumulated matrix/basis rounding errors, are
at most a fixed fraction of that tolerance. This requires
`w=C v`: logarithms of the iteration count add only
`C log(r+2)+C log(v+2)`, already dominated by `C v`.

Before stopping a selected pivot is at least the residual tolerance
divided by `C r`. Its plane-rotation parameters can be obtained from
the quadratic formula using a denominator at least twice the pivot
magnitude; the equal-diagonal case uses a 45-degree rotation. This
requires `C v` bits, not inverse-gap-many iterations. Division and
fixed-precision square root cost `O(v^2)` bit operations: long division
and the digit-by-digit integer square-root algorithm suffice. No
trigonometric oracle is used.

Write `t` for the chosen backward-residual tolerance. An induction on
the matrix and basis updates gives an accumulated basis `V` satisfying
`||V^T V-I||_F <= t/[C(M+1)]` and
`||A-V diag(d_i)V^T||_F <= t/C`, after enlarging the universal
precision constant. The additional `log(M+1)` guard positions already
belong to `v`, so the work and storage in (12) are unchanged. One can verify the induction
by writing each update as an exact orthogonal similarity plus its local
rounding residual. Orthogonal multiplication preserves Frobenius norm;
the deviations of represented rotations from orthogonality add at most
`C r 2^(-w)` per step. No product of inverse spectral gaps occurs.

For clarity, a nearby exactly orthogonal basis exists as
`O=V(V^TV)^(-1/2)` when the orthogonality error is below `1/2`.
The scalar bounds on `[1/2,3/2]` imply
`||O-V||_F <= C||V^TV-I||_F`. This is a proof device, not another
matrix operation the algorithm must compute. Since `||diag(d_i)||<=CM`,
the triangle inequality gives
`||A-O diag(d_i) O^T||_F <= t/C + CM||V^TV-I||_F <= t`,
with the universal error allocations chosen accordingly. The scale
factor `M` is essential here; it is not an eigenvalue-separation cost.

For inversion take residual tolerance below `C^(-1) a^2 2^(-b)`;
for a gapped square root below
`C^(-1) min(a,sqrt(a)2^(-b))`; for positive part below
`C^(-1)2^(-b)`. The inverse/root difference inequalities and
Frobenius nonexpansiveness of positive part then bound the error of
the reconstructed matrix function. Round the nonnegative diagonal
function values to sufficiently fine **nonnegative dyadics**, and form
`V diag(nonnegative values) V^T` by exact dyadic products and sums.
This preserves positive semidefiniteness without unsafe final entrywise
rounding. All numerators still have `O(v)` bits: a bounded number of
products and a sum of `r` terms adds only `C v+log r` bits.

There are `O(r^2v)` rotations. A largest-entry scan costs `O(r^2v)`
bit comparisons per rotation, and the two row/column and basis updates
cost `O(rv^2)`. These give exactly (12). Only a bounded number of
`r`-square arrays and linear scratch are live. The case `r=1` uses
scalar arithmetic directly. QED.

Applying this diagonalization separately to `Q` and `K` in Lemma 2 is
stable without matching their eigenvectors across perturbations. The
computed bases define nearby PSD matrices after clamping tiny negative
diagonal entries to zero. Evaluating (6)--(10) is then exact evaluation
of the protected map at these nearby matrices plus controlled local
arithmetic error. Its normwise Lipschitz bound is the one in Lemma 1.

## 5. Prepare coefficients once; evaluate rows by ordinary arithmetic

At a fixed source prefix and fixed query context, every conditioning
coefficient is independent of the sampled row packet. Traverse the
coefficient schedule once, retaining the coefficient vector for each
named row field and discarding each call's spectral scratch. The learned
rank-list norm, projections, and scalar contractions also depend only
on the scalar transcript at this point. They are computed once.

For an arithmetic allowance of `w` bits, including the extra `C R chi`
guard precision, this gives

\[
 \begin{split}
 W_{\rm prepare}&\le C\{R^5w^2+R^4w^3+Rd\,w^2\},\\
 S_{\rm prepare}&\le C(R^2+Rd)w,\\
 W_{\rm row}&\le C(R^2+Rd)w^2
                          +C R T_{\phi,\rm data}(Cw),\\
 S_{\rm row}&\le C(R^2+Rd)w+S_{\phi,\rm data}(Cw).
 \end{split}                                             \tag{14}
\]

The preparation bound uses at most `C R` spectral systems of dimension
`C R`, Lemma 3, and ordinary matrix products. Only the current query
layer's common-Gram and mean matrices are needed; earlier query moments
are retained as vectors. Recomputing those small coefficient matrices
for the next layer does not replay training.

Each named old physical row field is evaluated once from earlier named
row fields, with at most `C R` linear terms. Thus there are `C R^2`
scalar row operations and `C R` activation/derivative calls. The added
`Rd` counts first-layer input contractions. Whitened outgoing vector
marks require one ordinary matrix-vector product of dimension `C R`,
already included. No coefficient solve is repeated for each row.

For the finite Gaussian sampler used in the source, one row can be
produced in

\[
       C D w^4\text{ bit operations and }C D w\text{ bits}.\tag{15}
\]

Indeed the required cutoff has squared size at most `C w`. On that
interval the normal CDF can be evaluated to `C w` bits using `C w`
Taylor terms of the exponential, with `C w` guard bits accounting for
the largest intermediate terms. Fixed-grid recurrence and summation cost
`C w^3`; `C w` bisection steps cost `C w^4`. Certified CDF intervals
are used when a comparison overlaps: the lower Gaussian-density bound
converts its uncertainty into a coordinate interval of the desired
width. This avoids exact equality tests on transcendental values.
Scalar constants, division and square roots have finite series or
digit algorithms with smaller cost. The existing Gaussian coupling and
cutoff probabilities are retained. Gaussian generation is not free.

## 6. A small one-pass test for a bad median

### Lemma 4: retained medians do not determine the required seed size

Fix a source, a rounded query context, one coordinate of its vector
moment, and a finite rational threshold `t`. Let `J` be odd, `s` the
statistical block length, and let `M_j` be the implemented dyadic mean
of block `j`. The event

\[
 \operatorname{median}(M_1,\ldots,M_J)>t
\]

is exactly the event that at least `(J+1)/2` of these block means exceed
`t`. The analogous identity holds for `<t`. A one-pass finite-state
test for either event stores one running scalar sum, its row counter,
its block counter, and the count of blocks passing the threshold. Its
between-row space is

\[
                   C(w+\log(Js+2)).                     \tag{16}
\]

The row packet and its row-evaluation scratch are discarded at the end
of each row. Source coefficients, context, coordinate index, and the
proof threshold are hardwired in this **fixed test**. As in the original
short-seed argument, such proof advice is never an input to the decoder.

Apply the already supplied Nisan block-generator interface to these
tests. If `F` bounds the logarithm of the total finite-context failure
union, put

\[
 E=1+\lceil\log_2(Js+2)\rceil,\qquad
 A=C(Dw+F+E).                                            \tag{17}
\]

Then seed length `C A E`, hash work `C A^2 E` per generated row,
and hash scratch `C A` suffice. The `Dw` term supplies one entire
finite Gaussian packet per generator block. This use of the generator
is precisely the inherited one-pass block interface. It does not claim
independence of pseudorandom rows or substitute pairwise independence
into the product-entropy proof.

Take lower and upper rational proof thresholds just outside the iid
statistical error interval, leaving the same rounding margins as the
original proof. Union over their two sides, coordinates, contexts and
prefixes. This transfers the original median accuracy event with its
allocated failure probability. The decoder may still store all `J r_h`
block means; its output agrees with the medians whose failure was just
tested. Those actual arrays remain charged to peak memory even though
they do not inflate the proof-test state or the retained seed.

**Optional memory/work trade.** An exact dyadic median can instead be
found by binary search on its finite value grid. Each candidate threshold
uses a new traversal of the same generated row stream, counting how
many completed block means lie below it. There are `C w` passes per
coordinate, so at most `C r_h w` times as many row evaluations. Only
scalar sums, counters and the output vector are retained. This does
not require a theorem fooling the repeated-read algorithm: its answer
is exactly the median of the same deterministic stream, whose bad-event
tests above read the stream once. The identity of the returned median,
not a many-pass indistinguishability assertion, connects the proof.

## 7. Concrete composite core bounds

The actual passive recursion has one vector cross moment and one scalar
second moment per layer, plus the final readout. Thus its moment-call
count is `Q <= C(L+1)`. Its varying context consists of the input,
within-patch time, and guarded incoming vectors/scalars for these layers;
it has

\[
                 k\le d+1+C L R                         \tag{18}
\]

coordinates. Training prefix indices contribute `log(P+1)` to its
finite-context count, not `P` extra varying coordinates: the seed event
conditions on the complete actual source and its selected numerical
prefixes, as the existing proof explicitly requires.

Equations (4), (18) and the original context/Gaussian union argument give
the sufficient choices

\[
 p_a,p_{\rm ctx}\le C R\Theta,\qquad
 J,F,w\le C(L+1)R^2\Theta,
 \qquad A\le C(L+1)R^3\Theta,
 \quad E\le C\Theta.                                    \tag{19}
\]

The statistical block size remains the original
`s=floor(n/(128 K_hat))`, with its explicit width condition and
`K_hat` the finite upper certificate. In the coarse counts below only
`s<=n` is used. The lower scalar-noise precision reduces the information
certificate, but no favorable cancellation of `J` against `K_hat` is
needed for these bounds.

The selected panel may still use the existing exact Cramer weights.
Its retained description, using instruction templates and the explicit
coefficient arrays rather than precision-sized literals for all old
padded scalar slots, is bounded by

\[
 B_{\rm in}+C\{[(P+1)D+P]p_a
 +(P+1)^2[p_a+\log(n+2)+\log(P+2)]
 +(R^2+Rd)[p_a+\log(R+2)]\}.                            \tag{20}
\]

This is at most `B_in+C R^5 Theta`. The second term explicitly keeps
the exact rational weights; no favorable condition number or minimum
selected weight is assumed. The instruction templates describe the
same nested loops and causal field indices, whose total scalar row
graph and numerical literals fit the last term. They do not encode a
dense matrix or an answer table.

With ordinary stored block medians, (14)--(20) yield

\[
\begin{array}{c|c}
\text{resource}&\text{internal bound, excluding actual interfaces}\\\hline
\text{retained bits}&
 B_{\rm in}+C[R^5\Theta+(L+1)R^3\Theta^2]\\
\text{retained plus peak query/training bits}&
 B_{\rm in}+C(L+1)^2R^5\Theta^2\\
\text{one query's work}&C n(L+1)^6R^{11}\Theta^5.
\end{array}                                               \tag{21}
\]

For the work row, at most `C n(L+1)^2 R^2 Theta` packets are processed.
Each costs at most `C(L+1)^4 R^9 Theta^4` internally: (15) dominates
the elementary row work and the hash bound in (17). Coefficient
preparation for all calls costs at most
`C[(L+1)^3R^9Theta^2+(L+1)^4R^10Theta^3]`, which is also covered by
the displayed work row without any eventual-width absorption.

The actual activation/data work added per query is at most

\[
 C n(L+1)^2 R^3\Theta\,
          T_{\phi,\rm data}(C(L+1)R^2\Theta),             \tag{22}
\]

plus its coefficient-literal preparation calls, which fit the same
allowance for `n>=1`. Add the corresponding single-call scratch,
query/time acquisition, original retained input descriptions, certificate
costs, output writing, and the label-normalization precision costs in
`COST_CONTRACT.md`. In particular no uniform evaluator bound follows
from `beta` alone.

The optional median threshold-search implementation replaces the peak
row of (21) by

\[
 B_{\rm in}+C[R^5\Theta+(L+1)R^4\Theta
                              +(L+1)R^3\Theta^2],        \tag{23}
\]

at a query-work upper bound `C n(L+1)^7 R^14 Theta^6`.
Keeping `r_h,w,J,s` explicitly often gives a better trade than either
coarse envelope.

These counts are bit counts. They do not treat one growing-precision
real coordinate as one bit, a matrix eigendecomposition as one arithmetic
operation, or a supplied activation evaluation as universally cheap.

## 8. Dependence on the physical parameters and remaining boundary

The already supplied parameter certificate, with the contract's `Z`, is

\[
 R\le C\beta^{301L}(m+d+2)(1+m/\gamma)^3 Z^6,
 \qquad
 \Theta\le C\beta^{200L}(1+m/\gamma) Z^2.                \tag{24}
\]

Substituting (24) into (21), and only bounding `(L+1)^j` by
`C beta^(jL)`, gives the following intentionally rounded universal
activation envelope:

\[
\begin{array}{c|c}
\text{resource}&\text{upper bound besides interfaces}\\\hline
\text{retained bits}&
 B_{\rm in}+C\beta^{5000L}(m+d+2)^5(1+m/\gamma)^{17}Z^{32}\\
\text{retained plus peak query/training bits}&
 B_{\rm in}+C\beta^{5000L}(m+d+2)^5(1+m/\gamma)^{17}Z^{34}\\
\text{one query's work}&
 Cn\beta^{5000L}(m+d+2)^{11}(1+m/\gamma)^{38}Z^{76}.
\end{array}                                               \tag{25}
\]

For example the query exponent is `6*11+2*5=76`, its inverse-gap
power is `3*11+5=38`, and its activation exponent before rounding is
`301*11+200*5+6=4317`, below 5000. The retained seed's separate
term has `Z^(18+4)=Z^22`, below the `Z^32` panel-weight term.
These are internally derived candidate core bounds awaiting independent
reconstruction, not an edit to the checked cost contract.

No new inverse power of `Y` appears: the existing normalized field
interface is retained. The raw label-access precision and output-scale
representation costs remain exactly the explicit additions in the
contract. The case `Y=0` is its separately supplied exact zero branch.

Two bottlenecks remain visible.

* The physical schedule still has the field count (24). Even perfect
  arithmetic would not convert its current stored pair-table and exact
  support-panel representation into a fourth- or fifth-logarithmic-power
  bit bound. This is a statement about the representation being counted,
  not a lower bound on every possible response model.
* The existing support reduction has work
  `C n(P+2)^8 v_a^3`, where `v_a=O(R Theta)`. Thus this unchanged
  initialization algorithm still contributes `C n R^19 Theta^3`.
  Improving row arithmetic does not erase it. No smaller total
  initialization theorem is asserted here.

The improved source and acquisition arithmetic can use the same
coefficient sharing, but a complete initialization ledger must retain
that selection term and the temporary `n D p_a` packet array. No
initialization-memory compactness has been added to the contract.

## 9. Claim status and hostile checks

| Claim | Status in this note | Crucial hypothesis or falsifier |
|---|---|---|
| Whole causal sensitivity `log Lambda <= C R chi` | Author proof | Old fields must retain their creation-time scalar arguments; any hidden sequential chain not counted in named phases must be added to `R` |
| Separate-spectrum conditioning formulas | Exact identity | Both history matrices PSD and artificial noise positive; dimensions/orientations are as in (5)--(10) |
| Spectral macro bit work and scratch (12) | Author algorithm and proof | Rounding residuals, stopping tolerance and orthogonality error must all use the same certified `C v` grid |
| Small one-pass median failure test | Exact event identity under supplied generator theorem | The scalar sums and rounded block means must equal those used by the decoder |
| Core counts (21)--(25) | Derived under inherited source and precision interfaces | Every current-context coefficient is prepared once; exact panel weights and actual median arrays remain charged |
| Whole-sphere/trajectory/endpoint accuracy | Inherited conditional assembly | Same source, small-label, stochastic and statistical-comparison events are still required |
| `log^4` or `log^5` retained-plus-peak bits | Open | Not implied by any bound here |
| Low-exponent complete initialization | Open | Existing exact support selection remains expensive |

The strongest surviving structural objection to an even smaller precision
claim is genuine near-null history geometry: inverse-noise coefficients
can be large even when the eventual observable is bounded. This note
does not claim that bounded output alone permits `O(log n)` precision.
It only removes repeatedly charged dependencies and supplies stable
matrix implementations whose required bits scale with the logarithms
of actual floors.

The most important check of Lemma 1 is therefore the exact causal
schedule, not a numerical experiment: verify that no same-phase pair
moment changes another already-created field. The most important check
of Lemma 4 is equality of implemented rounded block means in the small
test and the actual median routine. Failure of either check would
invalidate its corresponding optimization while leaving the original
large-exponent decoder and the broader compression conjecture intact.
