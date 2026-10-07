# Selected packets with an explicit finite-bit metric

2026-10-06. Scoped author derivation in the current unseen-query study.
This replaces the scalar Caratheodory support construction by an elementary
coordinate-basis construction for the actual pair-moment source. It does
not change the original nonlinear network, labels, unseen-input scope or
reference error. No experiment, Git change or promotion was performed.

The strongest result is constructive: for a finite dyadic table of `R`
named source fields, including the constant field, at most `R` original
packets and one positive matrix reproduce every table pair exactly.
The metric is used only by multiplication, never inverted during
acquisition. A determinant-improvement algorithm finds it with an
explicit finite bit bound. There is no source-subspace spectral-gap
assumption and no uncounted sparsification oracle.

The resulting retained acquisition base is `O(R^3 Theta)` bits, versus
`O(R^4 Theta)` for the previously rounded scalar-weight panel. The
retained decoder seed and query workspace remain separate, larger terms.
This does not prove the requested fourth- or fifth-power logarithmic
full-model bound.

## 1. Inputs and the exact pair-moment condition

The scoped current-study inputs are the frozen `SANE_DECODER_CORE.md`,
its `SANE_CORE_COMPOSITION.md`, `EXPLICIT_COMPILER_EXPONENT.md`,
`COMPILER_PARAMETER_ACCOUNTING.md`, `NOISY_SCALAR_HISTORY_ACQUISITION.md`
(read completely for this follow-up), and the previously read posterior
moment and short-seed notes. The supervisor explicitly permitted the
selected-coordinate metric passages in the older finite-panel study;
the corresponding `RESULT.md` Section 3 and `PANEL_SOURCE.md` equation
(15) and its surrounding proof were read. They motivated the metric
interface but are not assumed to supply a finite-bit construction here.
The required notation/proof/research instructions retain their previously
recorded status; the custom notation skill is still inaccessible.

Let `Z_i`, `1<=i<=n`, be the virtual source's row packets and let
`g_1,...,g_s` be its named row fields, where `s<=C R`. Each field
retains its creation-time scalar arguments. Include `g_0=1`. For this
note the field count includes the original Gaussian coordinates and
fresh innovations when they enter acquired pair moments. Packet
dimension remains `D<=d+C R<=C R`.

The actual compiler has the required pair structure:

| Acquired quantity | Pair representation |
|---|---|
| Forward/reverse history and cross Grams | Two named query/answer fields |
| New-query covariance vector and squared RMS | New field with an old field, or with itself |
| Innovation cross moment | Named innovation with a named history field |
| Physical vector norm or feature/carrier RMS | Field with itself |
| Readout/output moment | Readout field with top feature |
| Scalar mean, if requested | Named field with the constant one |

The learned matrix Frobenius norms are sums of **products of already
acquired pair moments**, not new empirical fourth moments. Residual
projection across the `m` examples, scalar coefficients, fixed input
contractions, and Gram/coefficient operations are deterministic scalar
arithmetic, so do not create additional row averages. These facts are
the enumerated schedule in `EXPLICIT_COMPILER_EXPONENT.md`, Section 2,
and the conditioning schedule in its Section 3.

Thus every noisy scalar acquisition is of the form

\[
 C_r=\frac1n\sum_{i=1}^n u_r(i;C_{<r})v_r(i;C_{<r})
                                  +\eta E_r,             \tag{1}
\]

where both operands are already named fields. An outer cap on the pair
test is redundant if its bound is chosen as the product of the two
global operand caps; it need not change (1).

This condition is substantive. A general scalar program with `P`
unrelated functions `F_r` can always represent each as a pair with one,
but that could require `P` new named fields. This note does **not**
claim a rank-`R` metric for such a general program. It uses the actual
neural compiler's pair schedule, and keeps `P<=C R^2`.

## 2. Exact finite-table theorem

Let `V` be an `n`-by-`s` real matrix of source field values, including a
column of ones. Let its rank be `q`. Then

\[
                  1\le q\le\min(n,s).                   \tag{2}
\]

Choose `q` independent columns, with indices `J`, and `q` rows, with
indices `I`, for which `H=V[I,J]` is invertible. Define

\[
 C=V[:,J]H^{-1},\qquad M=\frac1n C^TC.                  \tag{3}
\]

Here `C` is an auxiliary coefficient matrix, unrelated to the scalar
history variables `C_r`. It exists only during preprocessing.

Every column of `V` is a linear combination of `V[:,J]`. Restricting
that relation to rows `I` shows directly that

\[
 V=C V[I,:],\qquad C[I,:]=I_q.                           \tag{4}
\]

Consequently

\[
          V^TV/n=V[I,:]^T M V[I,:].                     \tag{5}
\]

The metric is positive definite and has the explicit floor

\[
                        M\succeq I_q/n,                 \tag{6}
\]

because the rows indexed by `I` already contribute `I_q` to `C^TC`.
The constant column in (4) gives `C 1=1`, hence

\[
                         1^T M1=1.                      \tag{7}
\]

Only selected original packets, `M`, scalar noise marks and the causal
program are retained. Neither `C`, the full field table, nor future
scalar answers are retained.

### A bounded basis by determinant improvement

If some coefficient satisfies `|C_ij|>2`, replace row `j` of `H` by
row `i` of `V[:,J]`. Multilinearity of the determinant in that row gives

\[
                 |\det H_{\rm new}|=|C_{ij}|\,|\det H|
                                             >2|\det H|.\tag{8}
\]

The new row cannot duplicate a different selected row: in such a row
of `C` the coefficient in column `j` is zero. The new `H` remains
invertible. Iterate until every coefficient has magnitude at most two.

For a finite table the process terminates, since each update strictly
increases a determinant chosen from finitely many row subsets. For a
dyadic table the next section gives an explicit iteration bound. At
termination,

\[
 |C_{ij}|\le2,\qquad |M_{jk}|\le4,\qquad
 \|M\|_{\rm op}\le\operatorname{tr}M\le4q.              \tag{9}
\]

For every vector `z` in `R^q`,

\[
 \|z\|_M:=\sqrt{z^TMz}=\|Cz\|_2/\sqrt n
                  \le2q\|z\|_\infty.                  \tag{10}
\]

The constant in (10) is polynomial in `q`, unlike the stronger old
constant-four diagonal-domination interface. That is sufficient here:
the metric is used only for bilinear reductions, and `log q` is already
inside the numerical certificate. No weighted-space adjoint or gradient
flow is being constructed.

## 3. Exact tape induction and the private-metric boundary

First suppose exact real field evaluations and exact `M` are available.
Form `V` using the completed source tape (1). Store the selected packet
indices `I` long enough to copy those packets. The compact acquisition is

\[
 C_r^{\rm met}=
 u_r(I;C_{<r}^{\rm met})^T M v_r(I;C_{<r}^{\rm met})
                                  +\eta E_r.             \tag{11}
\]

If the prefixes agree, both selected operand vectors in (11) are exactly
the corresponding restricted columns used to form `V`. Equation (5)
then identifies the next pair average, and the same noise is added.
Induction proves equality of every scalar prefix.

The matrix and selected packets may depend on the completed **virtual**
training source, as did the previous selected scalar weights. Later
queries still receive only the current scalar prefix and the decoder
seed. They do not receive `M` or the selected packets as conditioning
information. The ideal posterior is still the exchangeable posterior
of the original iid-packet empirical-average law (1). Its information,
observed-Gram and prior-block arguments are unchanged.

The old positive scalar-weight acquisition lemma is not directly
applicable to (11). It is replaced by the pair-table induction above
and the stability proof below. Positivity of `M` is not used to claim
that (11) is an average of same-row products with positive scalar
weights; generally it is not.

## 4. Finite-bit construction without an unknown subspace gap

Assume every entry of `V` is on the grid `2^(-p) Z` and has magnitude
at most `B>=1`. Define the integer word allowance

\[
 b=2+p+\lceil\log_2(B+2)\rceil+
                          \lceil\log_2(n+s+2)\rceil.     \tag{12}
\]

Multiplying the table by `2^p` gives an integer matrix with entries of
`O(b)` bits. All rank and pivot decisions below are exact decisions on
these finite integers, not tests of rank for arbitrary activation-generated
reals.

### 4.1 Number of swaps

The initial nonzero dyadic determinant has magnitude at least
`2^(-pq)`. Hadamard's inequality bounds every selected determinant by
`q^(q/2) B^q`. Thus (8) can occur fewer than

\[
          q\{p+\log_2 B+\tfrac12\log_2 q\}+1\le Cqb   \tag{13}
\]

times. There is no arbitrary stopping threshold or unknown determinant
gap in this bound.

### 4.2 Integer operation count

Find independent rows by a streaming rank scan. Keep the original table
at its original `O(b)`-bit entry precision and retain at most `s`
independent original rows. For each incoming original row, run exact
fraction-free elimination only on those retained rows together with the
new row: at most an `(s+1)`-by-`s` matrix. Append the original row if
and only if the rank increases. At the end the retained rows span every
input row; their pivot columns give the required nonsingular square
block. This uses no transformed full-table array.

Each small rank test uses `O(s^3)` integer operations. The nonzero
expanded entries are minors or exact quotients equal to minors; their
bit length is `O(sb)` by the determinant expansion. Thus the complete
rank scan costs `O(ns^5b^2)` bit operations and `O(s^3b)` expanded
scratch bits. Once the rank `q` and independent block are selected,
the subsequent square elimination uses `O(qb)`-bit minors.

The fraction-free identity can be checked by taking the Schur complement
of the previously selected pivot block: the determinant of the new
two-row/two-column border is the product of that pivot determinant with
the determinant of its two-by-two Schur complement. Multiplying out
that two-by-two determinant gives the usual pivot-product minus
cross-product update divided by the preceding pivot. The division is
exact. Row exchanges preserve the statement after recording the sign.
Nonzero pivot search is an exact integer comparison.

Here and in the following integer calculation, use the scaled integer
block `2^p H` and the correspondingly scaled table rows; their common
scale cancels from `C`. The same algorithm on the augmented integer
block `[2^p H | I]` computes
an upper-triangular system for all inverse columns in `O(q^3)` integer
operations. Multiply its right side by `det H` and back-substitute.
The solutions are the integer columns of `adj H`, so these divisions
are exact as well. Their entries are minors, again with `O(qb)` bits.
Intermediate products and sums have `O(qb)` bits after increasing a
universal constant. This gives an explicit common-denominator inverse,
not separately growing rational denominators.

Long integer multiplication and division cost `O((qb)^2)` bits per
operation. Therefore one adjugate costs `Cq^5b^2` bit operations.
With that adjugate, scanning all rows and all `q` coefficients of
`C=V[:,J]H^(-1)` uses `C n q^2` integer products/additions on
`O(qb)`-bit integers. Test `|C_ij|>2` by comparing numerator with
twice the absolute common determinant. The scan costs `C n q^4 b^2`.
Since `q<=n`, it dominates the adjugate cost up to a constant.

Multiplying by (13), and adding initial elimination, yields

\[
                  W_{\rm metric}\le C n s^5 b^3.         \tag{14}
\]

At termination, compute the entries of `M` using the common determinant
denominator of `C`. Stream one row of its integer numerators at a time
and accumulate their pair products. The numerator and denominator of
each final metric entry have `O(qb+log n)=O(qb)` bits. This last scan
has work `C n q^4 b^2`, already covered by (14).

If the field table and source packet array are retained during this
construction, its peak bits are bounded by

\[
          C\{n(s+D)b+s^3b\}.                             \tag{15}
\]

The cubic term permits the exact adjugate and metric numerators, a
bounded number of `s`-square arrays of `O(sb)`-bit integers, and
elimination scratch. Only the small streaming rank-test matrix contains
expanded minors during initial selection; the full source table stays
at its original entry precision. A full-table fraction-free elimination
would not justify (15). The exact rational metric is discarded after
the finite rounding below.

### 4.3 PSD-safe metric rounding

Round the symmetric entries of `M` to a common dyadic grid with
entry error at most `rho=2^(-b_M)`, obtaining `M_0`, and set

\[
                     \widehat M=M_0+q\rho I_q.            \tag{16}
\]

Then `||M_0-M||_op<=q rho`, so

\[
 \widehat M\succeq M\succeq I_q/n,\qquad
 \|\widehat M-M\|_{\rm op}\le2q\rho.                    \tag{17}
\]

This preserves positivity without an eigenvalue computation or an
inverse of `M`. For operand vectors bounded by `B` in maximum norm,

\[
 |u^T(\widehat M-M)v|\le2q^2B^2\rho.                    \tag{18}
\]

The exact normalization (7) may be perturbed; its error is at most
`2q^2rho`, and is included in the same local budget. Normalization is
not repaired by inverting an uncertain scalar.

## 5. Source rounding and robust causal acquisition

The finite construction should be applied to the **computed finite
source table**, not to an inaccessible exact-rank real table. Run the
original virtual source to its assigned precision. For every named
field, let its table column be the dyadic output of a fixed deterministic
row evaluator at the numerical creation-time prefix. Include the
constant column exactly.

There are two useful comparisons.

1. With exact rational `M` from this table, using exactly the same
   deterministic row evaluator and the same scalar rounding rule in
   (11) reproduces the computed tape exactly, provided that the source
   forms a pair by multiplying those same rounded operand values
   **exactly**, without a separate rounding of each row product.
   Specifically two operands with `p` fractional bits are multiplied on
   their exact `2p`-bit grid, the `n` products are summed exactly, and
   the division by `n`, noise addition and final scalar rounding use
   the common prescribed scalar interface. The accumulator needs only
   `O(p+log n+log(B+2))` bits. Pair summation and final scalar rounding
   then have identical inputs in the exact-metric construction.
2. For rounded `M`, packet perturbations, or comparison with the exact
   mathematical source, use additive error bounds. Do not claim that
   a rounded interpreter or its threshold decisions are Lipschitz.

The required source convention in the first comparison is achievable:
use the named dyadic field outputs as operands of each pair reduction.
If the previous implementation instead rounds each row product or a
directly evaluated pair test before averaging, replacing it by this
exact-product/common-grid schedule changes a row test by at most
`C(B+1)u+u^2`, where `u` bounds field and old row-product rounding.
Averaging does not enlarge this error. It is absorbed in the existing
source numerical budget. We do not assert identical legacy rounded
tapes after changing that multiplication schedule; only the stated
controlled comparison and exact identity for the newly specified finite
tape are used.

For the second comparison, (10) gives, for arbitrary selected arrays,

\[
 |u^TMv-\widetilde u^TM\widetilde v|
 \le4q^2\{\|u-\widetilde u\|_\infty\|v\|_\infty
       +\|\widetilde u\|_\infty\|v-\widetilde v\|_\infty\}.
                                                               \tag{19}
\]

The same bound with a larger universal coefficient holds for
`M_hat` when `rho<=1`, by (17). Thus bilinear reductions have
logarithmic local sensitivity `O(log q+log(B+2))`, already in `C chi`.
Rounding each new scalar adds its declared local absolute error;
comparing two rounded values uses
`|round(a)-round(b)|<=|a-b|+2u`, not continuity of rounding.

Apply the whole causal-depth recurrence of the frozen core with these
bilinear phases. Its hypotheses still hold: the metric is fixed after
preprocessing, there are `C R` named-field phases, old fields retain
their old arguments, and scalar matrix routines keep their protected
floors. Its global amplification is `2^(C R chi)`. Equations
(18)--(19), finite packet/noise precision, and the common-Gram
accuracy allowance can all therefore be met with

\[
                    b,b_M\le C R\Theta.                 \tag{20}
\]

The integer parts of the old physical caps are included in `chi`.
The additional factors `q^2` cost only `C log(R+2)` guard bits.
Metric construction can work with exact rational intermediates of
`O(Rb)` bits, but only its final `O(b_M)`-bit entries are retained.

This comparison is pointwise in the privately selected metric. It
produces a numerical prefix within the same error ball around the ideal
empirical-average noisy prefix. The posterior proof already covers every
prefix in that ball without conditioning on private selection data.
The ideal exchangeable likelihood and the dense/source coupling are
therefore not changed into a metric-dependent posterior law.

## 6. Resource consequence and limits

Take `s<=C R`, `D<=C R`, `P<=C R^2` and (20). Selected packet
coordinates `qD`, the dense metric `q^2`, scalar-noise marks `P`,
current summaries `P`, and coefficient/template arrays `O(R^2)`
contain only `O(R^2)` numerical entries. Thus

\[
          S_{\rm acquisition\ base}\le B_{\rm in}+C R^3\Theta.
                                                               \tag{21}
\]

Selected row indices may be discarded after copying the packets. Their
temporary `q log n` bits fit the construction count. No full row field
table is retained after initialization.

Equations (14)--(15) give

\[
 W_{\rm metric}\le C nR^8\Theta^3,\qquad
 S_{\rm metric\ construction}\le C[nR^2\Theta+R^4\Theta].
                                                               \tag{22}
\]

These replace the old selection contributions `nR^19Theta^3` and
`R^7Theta`. They count actual exact integer arithmetic on finite input,
including rank selection, determinant improvement, the full metric and
its final rounding.

Source generation and its Gaussian/input interfaces remain additional.
Using the already derived source-row and finite Gaussian schedules, a
safe complete candidate initialization count is

\[
 W_{\rm init}\le
 C\{nR^8\Theta^3+(nR^5+R^6)\Theta^4\},                  \tag{23}
\]

plus actual source-evaluator/input/certificate work. The full temporary
initialization peak additionally includes the later retained seed:

\[
 B_{\rm in}+C[nR^2\Theta+R^4\Theta+(L+1)R^3\Theta^2].   \tag{24}
\]

There are `q<=C R` selected rows per acquisition. Evaluate their
operand vectors, then compute the non-diagonal bilinear form in
`O(q^2)` scalar operations. With the core's row compiler and incremental
coefficient preparation, every scheduled compact update together has
candidate work

\[
                 C(R^7\Theta^2+R^7\Theta^3)
                        \le C R^7\Theta^3.              \tag{25}
\]

The safe activation/data-call count for all updates is `C R^4`, each
at precision `C R Theta`: `P` stages, `q` packets and `C R`
activation/derivative calls per row. The source evaluation count remains
the previous `C nR^3`; no activation evaluator is treated as uniformly
cheap. Single-call evaluator scratch, original descriptions, label
normalization and output-scale encoding remain explicit additions.

This route does not reduce the query seed. Combining only the currently
derived interfaces, total retained information still has bound

\[
 B_{\rm in}+C[R^3\Theta+(L+1)R^3\Theta^2].                \tag{26}
\]

Stored-median query peak is still `C(L+1)^2R^5Theta^2` plus inputs.
Threshold-search query peak is still bounded by

\[
 B_{\rm in}+C(L+1)[R^4\Theta+R^3\Theta^2],               \tag{27}
\]

because current query coefficient arrays and the retained seed remain
live. The existing query work and evaluator-call counts are unchanged.
Replacing a packet count alone by a real-coordinate exponent five would
therefore omit both precision and other parts of the model.

No new temporal-source construction is used here. In particular no
unread Taylor-source proposal is substituted into `R`. For reference,
the already read shorter collocation source has `R` proportional to
`Z^(9/2)` and `Theta` proportional to `Z^2`, with its full explicit
physical factors. Equations (21), (22), (25), and (26) then contribute
logarithmic powers `31/2`, `42`, `75/2`, and `35/2`, respectively.
The source Gaussian term and peak query terms must still be included;
these exponents are not a complete low-exponent model theorem.

## 7. Adversarial checks and status

* **Non-pair summaries:** the exact theorem fails to give dimension `R`
  if arbitrary new row tests must be added as `P` independent columns.
  The enumerated neural schedule supplies the required pair condition.
* **Tiny singular values:** exact rank is taken only after fixing the
  finite dyadic table. Determinant bit length and swap count are bounded
  by that table's explicit precision. No exact rank decision on an
  arbitrary real oracle, or unknown original spectral gap, is used.
* **Metric conditioning:** the exact metric even has floor `1/n`, but
  the runtime does not use its inverse. Finite metric precision is
  controlled by (18), so the floor is not hidden in runtime arithmetic.
* **Coordinate mixing:** non-diagonal pair reductions are not scalar
  weighted averages. The replacement is the exact tape induction and
  its perturbation bound, not an invalid invocation of convex weights.
* **Private source dependence:** the metric may depend on the completed
  permitted virtual source, but is not given to the conditional decoder.
  Prefix closeness is the only bridge to its original posterior proof.
* **Intermediate integer growth:** adjugates, metric numerators and
  elimination arrays use `O(Rb)`-bit integers and are charged in (14)--(15).
  They are not silently stored as unit-cost reals or kept after rounding.
* **Bad finite branches:** source failure handling and resource guards
  remain inherited. The metric algorithm itself terminates on every
  finite table, including rank one; the constant field rules out rank zero.

Status: exact finite-table construction and bit-count derivation, plus
conditional substitution into the previously frozen source/decoder
interfaces. Fresh independent reconstruction remains necessary before
replacing the checked cost contract. The original full label class and
all-input/all-time/endpoint scientific guarantees remain inherited; this
note does not improve their unquantified stochastic width thresholds or
prove a fourth- or fifth-power full bit-memory bound.
