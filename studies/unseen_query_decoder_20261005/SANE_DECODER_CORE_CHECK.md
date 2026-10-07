# Isolated check of the smaller decoder core

2026-10-06. Fresh scoped mathematical and resource review of the frozen
candidate below. This is an internal check, not promotion or an independent
reproof of its inherited scientific source theorem.

**Verdict: the resource improvements reconstruct, subject to one minor
Jacobi proof correction.** No major obstruction was found in the causal
depth reduction, separate-spectrum formulas, coefficient sharing, finite
Gaussian sampler, small median-failure tests, or composed resource counts.
The literal polar-basis residual implication in Lemma 3 omits a matrix-size
factor. The explicit correction below preserves its precision, work and
space bounds. The frozen candidate should incorporate it before its matrix
proof is described as complete.

## Scope, isolation and read coverage

The neutral assignment authorized only the candidate and the named source
inputs. `PHYSICAL_PARAMETER_ACCOUNTING.md` was initially missing from that
list; I reported the missing input before retrieving it, and the supervisor
then explicitly authorized its complete current contents. I read every
file in the following table completely, including Section 10 of
`RECALIBRATION_FREE_MOMENTS.md` and Section 8 of
`COMPILER_PARAMETER_ACCOUNTING.md`. The line ranges give complete read
coverage, not selected excerpts. All hashes were checked again after the
scientific reading and remained unchanged.

| Input | Complete lines | SHA-256 |
|---|---:|---|
| `SANE_DECODER_CORE.md` | 1–669 | `4174c39dc2f0fb89e3bc03559c6a88664e2305d7f3c5b583bcfa8b123ad33b2a` |
| `COST_CONTRACT.md` | 1–321 | `3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c` |
| `EXPLICIT_COMPILER_EXPONENT.md` | 1–609 | `93510e4e88f9c632e9c439715b655d4ea6dc1701aae655f0a30d45cbf7f4ba3a` |
| `COMPILER_PARAMETER_ACCOUNTING.md` | 1–1041 | `00c017e1b39e96de79ca062b207514cef5cb045507f7cef4ed4975b69fa07c6e` |
| `RECALIBRATION_FREE_MOMENTS.md` | 1–1305 | `710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea` |
| `SHORT_SEED_PRIOR_BLOCKS.md` | 1–274 | `78e5f21ce787adac48b5ca745f330af92c87330934dd1634132c0b2308c35201` |
| `NOISY_TWO_ORIENTATION_TRANSCRIPT.md` | 1–658 | `0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac` |
| `NOISY_SCALAR_HISTORY_ACQUISITION.md` | 1–451 | `b301507a73de79310634ca67da75a9f5817a139edc498ad145aaeb857cae6fab` |
| `QUADRATIC_INITIALIZATION.md` | 1–558 | `fa97b8cee8bd97c89f098a6776e6b797b0acdbcca9d0470da5e0cceac405f6e8` |
| `FINITE_PRECISION_SOURCE_SELECTION.md` | 1–148 | `bef48fe4f546792326cedeb438a09fda0d6b3f616f60e2d907bf20b8888ced90` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | 1–512 | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |

No study README, other study, archived book passage, separate reviewer
report, new competing route note, or Git history was inspected. The
historical provenance paragraphs embedded in the assigned sources were
not used as evidence of mathematical correctness. I did not retrieve the
original Nisan paper: its precise one-pass block interface was explicitly
supplied for this assignment, and its application, rather than the external
theorem, is checked here. Likewise the physical-flow, source-event,+dense-pair, and weak-moment comparison interfaces remain inherited.

I read `solve-math-rigorously`, `investigate-conjectures`, and the latter's
complete adversarial-audit reference. The custom canonical-notation file
was unavailable at its assigned path. The authorized fallback was used:
retain the supplied symbols, distinguish input dimension `d` from packet
dimension `D`, and state the missing proof steps explicitly. No experiment,
implementation benchmark, candidate edit or Git action was performed.
Only this report was written.

## 1. Causal depth and precision

Here `R` bounds actual named fields, matrix calls, examples and layers;
`P <= C R^2` counts scalar reductions; `chi` includes the logarithms of
all operand caps and positive floors, including the common-Gram ridge.
These are the candidate's definitions, with no additional fixed-problem
constant inserted into `R`.

The explicit physical schedule supports a graph of depth `C R`:

1. A learned-list norm uses existing pair tables in a single quadratic
   contraction. Its projection multiplier is one gapped scalar function.
   Its action on a new field then uses one vector contraction and one
   linear combination of old row fields.
2. A newly available pair table depends on the two fields whose pair is
   being measured. Different entries in that table do not depend on each
   other. The scalar-history input explicitly allows consecutive updates
   in one such block to ignore earlier updates in that block.
3. A matrix call uses a bounded number of projections, inverses, products,
   a Sylvester solve and a protected root. The new innovation first becomes
   a named field; its cross moments with old opposite-orientation queries
   are another parallel reduction block before the answer is formed.
4. A projection that needs a newly acquired norm creates a later projected
   field. Thus its dependence crosses a new named-field stage, not an
   arbitrarily long unnamed chain of pair updates.
5. The Picard and patch chronology creates fields from previously committed
   or previous-iteration fields. Old fields retain their creation-time
   scalar arguments, as explicitly stated in the initialization and
   compiler inputs. Appending a table entry never changes an old field.

Long sums and products must be estimated as the corresponding multilinear
maps. With maximum norm on collections and Frobenius norm on matrices,
their dimension factors have logarithm `O(chi)`. Convex averaging has norm
one. The whole graph therefore has `C R` stages, each with Lipschitz
constant at most `2^(C chi)`, giving `log(1+Lambda) <= C R chi`.
Applying a row sensitivity separately at each of `P` scalar prefixes
would count predecessors again. It is unnecessary for this actual graph.

This conclusion concerns the source graph and a fixed selected convex
panel's acquisition map. It does not assert Lipschitz continuity of the
support-selection algorithm itself, whose support can jump. The supplied
exact numerical source-selection identity avoids any need for that claim.
Numerical recomputation also uses a fixed deterministic field recipe and
common sufficient precision, so old fields at the same retained arguments
are reproduced consistently; it is not a different precision-dependent
definition at every use.

The error recurrence `e_{j+1} <= 2^(C chi)e_j+u` then gives total
amplification `2^(C R chi)`. Source Gaussian coupling, scalar-noise bounds,
history comparison, pair-table comparison and finite context rounding add
only their stated logarithms. They allow `p_a,p_ctx,log(1/eta) <= C R Theta`.
The ridge is still chosen first using the physical/numerical propagation
certificate. No improvement to that ridge or to physical statistical
propagation was inferred from the depth observation.

## 2. Separate-spectrum conditioning

Write `delta_sigma = sigma^2` in this paragraph to avoid confusing matrix
noise variance with the failure probability `delta`. On the tensor
eigenvector indexed by `(j,i)`, the Kronecker matrix has eigenvalue
`delta_sigma+k_j+q_i`. Contracting with `I tensor v` on both sides gives
`a_j`; contracting on one side with
`(delta_sigma I+Q)^(-1)v` gives `b_j`. This verifies both contractions,
including the extra denominator in `b_j`.

The Sylvester equation transforms to
`(delta_sigma+k_j+q_i) E_tilde[j,i] = RHS_tilde[j,i]`.
The transformed right side includes the two different cross blocks `H,J`;
no false equality between them is used. Ordinary cubic matrix products
suffice for the transformations.

Substituting these contractions in the original formulas gives
`F=delta_sigma(delta_sigma I+K)^(-1)(c I-B_1)` and
`H_f=(delta_sigma I+K)^(-1)(-f_0 I+delta_sigma B_2)`.
Both are functions of `K`; hence their eigenvalues are exactly the
candidate's `f_j,h_j`. Positive part of `F` acts diagonally in that same
basis. This proves the correction formula even off the consistent Gram
domain, with the specified scalar protections. Rank deficiency causes no
division by `k_j` or `q_i`; the positive `sigma` floors remain. Empty
histories reduce to the supplied scalar formulas.

Only the two resulting coefficient vectors and one variance factor are
needed by the row expression. The square matrices can be discarded after
preparation. This is an exact rearrangement of the protected map, not an
approximation to its rank or covariance.

## 3. Jacobi algorithm: one minor correction

The largest-pivot contraction is correct. With off-diagonal Frobenius norm
`e`, some pivot has square at least `e^2/[r(r-1)]`; eliminating it reduces
`e^2` by twice its square. Rounding gives an additive residual of order
`r M 2^(-w)` per rotation. A residual target has logarithm `O(v)`, so
`O(r^2 v)` rotations suffice when their rounding floor is allocated
below that target. The pivot before termination is at least the target
divided by `C r`; its rotation can be evaluated with `O(v)` bits and
quadratic bit work. No eigenvalue separation is required.

There is, however, an omitted factor in the polar-basis paragraph. Let
`D_0=diag(d_i)`, `O=V(V^T V)^(-1/2)`, and let `t` be the intended
backward residual. The actual implication is

\[
 \|A-OD_0O^T\|_F
 \le \|A-VD_0V^T\|_F
   +C\|D_0\|\,\|V^TV-I\|_F.
\]

Since `||D_0|| <= C M`, merely bounding both errors on the right by
`t` does not bound the left by a universal multiple of `t` independent
of `M`. The reconstruction paragraph should explicitly require

\[
 \|A-VD_0V^T\|_F\le t/C,\qquad
 \|V^TV-I\|_F\le t/[C(M+1)].
\]

This is a minor repair with a direct resolver: choose the internal grid
large enough for both displayed targets. The extra requirement adds
`O(log(M+1))` guard bits, already included in `v`, so `w=Cv` suffices.
In fact the same extra precision can be used throughout all rotations.
With these targets, the claimed inverse/root/positive-part tolerances
follow from the stated normwise matrix-function inequalities. Replacing
the approximately orthogonal `V` by its nearby `O` in the separate-spectrum
formulas is a proof device; arithmetic with `V` contributes a controlled
local error. It is not literally an exact spectral decomposition with a
nonorthogonal basis.

The work count then reconstructs: the largest-entry scan costs
`O(r^2 v)` bit comparisons per rotation, the two rows/columns and basis
updates cost `O(r v^2)`, and there are `O(r^2 v)` rotations. Thus the
total is `O(r^4 v^2+r^3 v^3)`, with `O(r^2 v)` scratch. Final exact
dyadic reconstruction costs `O(r^3 v^2)` and fits. Nonnegative dyadic
function values in `V diag(values)V^T` ensure exact PSD even though
`V` is only approximately orthogonal. A fixed number of products and
sums uses `O(v)` bits per entry, and no unprotected final entrywise
rounding is required.

## 4. Sharing coefficients and generating finite Gaussian rows

At fixed retained source prefix and rounded query context, all matrix
coefficients depend only on those fixed scalars. The innovation cross
moment in an old conditioning call is already a retained scalar; it is
not recomputed from the particular newly sampled prior row. The physical
norms, projections and learned-action coefficients have the same property.
Preparing at most `C R` systems of dimension `C R` gives
`O(R^5 w^2+R^4 w^3+Rd w^2)` work. Retaining one vector of at most `C R`
coefficients per named field and one live square scratch area gives
`O((R^2+Rd)w)` bits.

Each named row field is evaluated once, from at most `C R` old field
values, giving `O(R^2+Rd)` scalar row operations and `O(R)` activation
or derivative calls. Query common-Gram matrices may be prepared for the
current layer and discarded afterwards; earlier query moments are
vectors. Nothing requires an additional simultaneous `R` square arrays.

For the finite quantile sampler, `T^2=O(w)` and a required CDF precision
of `O(w)` bits permit `O(w)` terms of the exponential series. The large
alternating intermediate terms have magnitude at most `exp(O(w))`, so
`O(w)` guard bits cover cancellation and summation. Fixed-grid recurrence
uses `O(w^3)` work per CDF evaluation. Its density lower bound costs
another `O(w)` precision allowance, not exponentially many operations.
`O(w)` bisection steps give `O(w^4)` work per coordinate. Certified
comparison intervals handle overlap without transcendental equality
tests. Hence `O(D w^4)` work and `O(Dw)` packet/scratch bits are valid.
The inherited tail/coupling union must still be paid, as the candidate
does. Its smaller required cutoff fits the authorized existing cap
certificate, which already accommodates the larger old cutoff.

## 5. The median tests and adaptive contexts

For odd `J`, the event that the implemented coordinate median exceeds a
fixed threshold is exactly that at least `(J+1)/2` implemented block
means exceed it; similarly below a threshold. Its one-pass state consists
of the running scalar sum and row/block/success counters. Their size is
`O(w+log(Js+2))`, including the extra accumulator integer bits.
It need not store previous block means or the other coordinates.

This conclusion requires the same finite row evaluator, scalar summation,
division and rounding rule as the decoder. Such an implementation is
available: coordinatewise sums are separable, and a test can even run the
full current row evaluation and discard its other coordinates. The proof
does not assert that a different rounded summation is equivalent.

Source coefficients, current prefix, coordinate and rational comparison
threshold can be hardwired in each fixed nonuniform test under the supplied
generator interface. Their decoder storage is still charged separately.
One random generator block contains all uniform bits for one finite
Gaussian packet; temporary row scratch is cleared before the next block.
Thus `A=C(Dw+F+E)` suffices, with seed `O(AE)` and row generation work
`O(A^2E)`. No theorem about repeated reads or independent pseudorandom
rows is invoked.

Conditioning on the complete actual source and numerical acquisition makes
their finitely many prefixes fixed independently of the decoder seed.
The varying parameters are the input, time coordinate and guarded incoming
moment vectors/scalars, at most `d+1+C L R` coordinates. Prefix and
call indices add logarithms to the finite union. This agrees with the
source's explicit distinction between parameterwise history comparison
and conditioning on private selected packets. The union over all guarded
rounded contexts includes the later seed-dependent query recursion and
adaptive query selection.

Hardwired rational thresholds just beyond the iid statistical interval
transfer the two bad-median events with a rounding margin. Their use does
not supply an inaccessible population moment to the decoder. The optional
threshold-search implementation also works: it returns the exact median
of the same deterministic stream, so its many actual passes need not be
indistinguishable from a repeatedly read random tape.

## 6. Reconstructed counts and exact boundary

The actual passive recursion has `Q=O(L+1)` moment calls. Substituting
the context dimension and precision above gives

\[
 p_a,p_{\rm ctx}=O(R\Theta),\quad
 J,F,w=O((L+1)R^2\Theta),\quad
 A=O((L+1)R^3\Theta),\quad E=O(\Theta).
\]

The support-panel weights have `O((P+1)v_a)` bits each, where
`v_a=O(R Theta)`. Their total is `O(R^5 Theta)`; no minimum positive
weight or determinant condition number is being assumed. Packet/noise/
current-summary descriptions and templated field instructions fit that
envelope. Exact common-denominator weighted accumulation needs
`O((P+1)v_a)` live bits and fits the post-initialization memory envelope.

The retained seed is `O((L+1)R^3 Theta^2)`. The stored block means use
`J r_h w = O((L+1)^2 R^5 Theta^2)` bits, dominating current row and
coefficient scratch. These verify the first two rows of (21), with
“training” interpreted as compact updates after initialization.

There are `O(n(L+1)^2 R^2 Theta)` processed packets. Each has internal
work at most `O((L+1)^4 R^9 Theta^4)`, from Gaussian generation;
hashing and ordinary row arithmetic fit below it. Multiplication gives
the query work `O(n(L+1)^6 R^11 Theta^5)`. The independently counted
preparation terms also fit, even when the statistical block size is small.
The activation/data additions in (22) retain their actual evaluator cost.
Binary median search adds at most `O(r_h w)` stream passes and gives the
candidate's optional work and memory trade without changing the seed proof.

The authorized physical source gives the stated `R` and `Theta`
envelopes. A term `R^u Theta^v` contributes logarithmic power `6u+2v`
and inverse-gap power `3u+v`. Thus retained panel bits give `Z^32`,
stored-median peak bits give `Z^34`, and query work gives `Z^76`.
The query activation exponent before rounding is
`301*11+200*5+6=4317`; the common `beta^(5000L)` envelope covers it.
The retained seed gives the smaller `Z^22` term. The displayed retained
inverse-gap power 17 is a valid loose bound for both retained contributions.

The unchanged exact support-reduction work remains

\[
 Cn(P+2)^8v_a^3\le CnR^{19}\Theta^3.
\]

Its separate selection scratch and the temporary `nD p_a` packet array
belong to initialization. Neither is erased by coefficient sharing or by
the query-memory bound. The note correctly stops short of a complete
improved initialization theorem or compact initialization-space theorem.

The strongest validated improvement is therefore a much smaller conditional
decoder/compiler core for the same source and statistical interfaces. It
does not prove logarithmic power four or five for retained-plus-peak bits,
a new stochastic width threshold, a practical dense-cost crossover, a
uniform activation evaluator bound, or accuracy for a prescribed realized
dense root. Input/certificate/query/time/output and small-label precision
costs remain explicit additions. The physical source count and exact
support-panel representation are still substantial costs. Failure of a
more ambitious compression claim would not negate these checked core
improvements.

## 7. Bounded correction recheck

2026-10-06. The supervisor supplied a corrected candidate with SHA-256
`701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4`
and explicitly requested a recheck only of the changed Jacobi paragraph.
I verified that hash and read the revised paragraph with its surrounding
rotation, matrix-function and resource arguments. The original frozen
review and input hashes above are preserved. This addendum does not claim
a new complete reading of the revised file or expand the scientific scope.

The revision now assigns
`||V^T V-I||_F <= t/[C(M+1)]` and
`||A-V diag(d_i)V^T||_F <= t/C`, and explicitly includes the factor
`||diag(d_i)|| <= CM` when passing from `V` to its polar factor `O`.
The triangle inequality therefore gives the intended backward residual
`||A-O diag(d_i)O^T||_F <= t` after choosing universal allocation
constants. The added logarithmic guard allowance is already included in
`v`, so `w=Cv`, work (12), and the composite exponents remain valid.

**Resolution: the sole requested correction is satisfied.** Within the
original supplied source and generator interfaces, no unresolved finding
remains in this bounded review of the corrected decoder/compiler core.
The initialization, evaluator, accuracy-threshold and promotion boundaries
in Section 6 remain unchanged. No candidate, other note, experiment or Git
state was changed during this recheck; only this report was appended.
