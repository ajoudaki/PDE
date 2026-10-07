# Bounded independent check of the finite-bit packet metric

2026-10-06. Internal, isolated review; not promotion or an independent
review of the full source/decoder theorem. No experiments or Git operations.

**Verdict on the frozen candidate: one correction is required.** The
finite-table identity, bounded-coordinate selection, rounded acquisition,
retained memory, and unchanged decoder costs reconstruct correctly. The
initialization peak in (15), and consequently its uses in (22) and (24),
is not established by the written full-table fraction-free elimination.
Its expanded integers require another field-count factor in that table.
A streaming rank scan repairs this without changing any claimed final
bound. The precise repair is given below; this verdict is on the
uncorrected frozen file, not on an anticipated revision.

## Frozen inputs and scope

The candidate read completely was `SANE_METRIC_PACKETS.md`, SHA-256
`42cd8c027617df814c20b077be7f61b137f8fa39ab294f6a6d54ce681003d058`.
The following permitted dependencies were read completely:

| Input | SHA-256 |
|---|---|
| `NOISY_SCALAR_HISTORY_ACQUISITION.md` | `b301507a73de79310634ca67da75a9f5817a139edc498ad145aaeb857cae6fab` |
| `FINITE_PRECISION_SOURCE_SELECTION.md` | `bef48fe4f546792326cedeb438a09fda0d6b3f616f60e2d907bf20b8888ced90` |
| `QUADRATIC_INITIALIZATION.md` | `fa97b8cee8bd97c89f098a6776e6b797b0acdbcca9d0470da5e0cceac405f6e8` |
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `EXPLICIT_COMPILER_EXPONENT.md` | `93510e4e88f9c632e9c439715b655d4ea6dc1701aae655f0a30d45cbf7f4ba3a` |

The last input was explicitly added to this review's scope to verify the
source pair schedule. No study README, prior review, other new note,
other-study material, or archived book was inspected. The rigorous-math
and conjecture-audit skills, their research-contract and adversarial-audit
references, and `docs/notation.qmd` were read. The required private
canonical-notation skill was permission-denied; the supervisor authorized
the supplied repository notation rules and maintained notation contract
as the fallback. No unavailable skill content is represented as read.

The inherited nonlinear physical bridge, posterior accuracy, generator
theorem, numerical interfaces, and reference comparison remain
assumptions of this bounded substitution check. In particular, this
report does not upgrade their claim status.

## 1. The source really uses pair moments

`EXPLICIT_COMPILER_EXPONENT.md`, Sections 2 and 3, supplies the missing
specialization beyond the general scalar functions in the acquisition
note. Its physical schedule acquires only products of two existing
named fields. Learned displacement squared norms are sums of products
of two already acquired Gram entries. Learned actions require the pair
of a stored rank factor and the current argument; feature and carrier
RMS projections require self-pairs. Readout/output contractions are
pairs as well. First-layer input contractions and residual projections
are deterministic scalar arithmetic.

The two-orientation Gaussian schedule uses physical query/answer Grams
and cross Grams, input squared RMS and cross vectors, and innovation
pairs such as the history field paired with the fresh Gaussian field.
Its coefficient matrices are deterministic functions of these scalars.
The separate-spectrum implementation in the corrected core changes
their computation, not the list of empirical reductions. Original root
coordinates, innovations, and capped/projected principal fields can all
be included in the stated constant multiple of the actual field count.

Thus the pair-table condition is supported for this compiled source.
The constant field handles first moments. The candidate correctly
excludes arbitrary unrelated scalar tests from the same field-count
claim. Training matrix-call queries here must not be confused with
arbitrary later test inputs: the metric is not used as a quadrature
rule for unseen query functions.

## 2. Exact geometry, selection, and finite arithmetic

Let the finite field table be an \(n\)-by-\(s\) dyadic matrix \(V\),
including a column of ones, with rank \(q\). Choose independent columns
\(J\) and rows \(I\) making \(H=V[I,J]\) invertible. With

\[
C=V[:,J]H^{-1},\qquad M=C^TC/n,
\]

restriction of each column expansion to \(I\) gives
\(V=CV[I,:]\) and \(C[I,:]=I_q\). Therefore

\[
V^TV/n=V[I,:]^TMV[I,:],\qquad M\succeq I_q/n.
\]

The column of ones also gives \(C\mathbf1=\mathbf1\), so
\(\mathbf1^TM\mathbf1=1\). These conclusions require no spectral-gap
assumption on \(V\).

Replacing selected row \(j\) by original row \(i\) multiplies its
determinant by \(C_{ij}\). All terms except the \(j\)-th vanish in
the multilinear expansion because they duplicate another selected row.
A swap when \(|C_{ij}|>2\) consequently preserves rank and more than
doubles determinant magnitude. If entries have grid \(2^{-p}\) and
magnitude at most \(B\), the initial nonzero determinant is at least
\(2^{-pq}\), while every determinant is at most
\(q^{q/2}B^q\). This verifies the candidate's \(O(qb)\) swap bound
for its word allowance \(b\), including \(q=1\). The constant column
excludes \(q=0\).

At termination, \(|C_{ij}|\le2\), \(|M_{jk}|\le4\), and
\(\|M\|_{\mathrm{op}}\le4q\). The bound
\(\|Cz\|_2/\sqrt n\le2q\|z\|_\infty\) follows directly by
bounding each row sum. Small singular values of \(H\) do not invalidate
these statements: rank tests and inverses are performed on the scaled
integer table, whose nonzero minors have \(O(qb)\) bits.

The adjugate computation can be justified by fraction-free elimination
of the square augmented system, followed by back substitution with its
right side multiplied by the determinant. Each final solution column
is an integer adjugate column. Thus the divisions are exact; intermediate
products and sums have \(O(qb)\) bits. This yields the stated
\(O(q^5b^2)\) bit cost. One coefficient scan costs
\(O(nq^4b^2)\) and dominates the adjugate because \(q\le n\).
The swap count then gives \(O(ns^5b^3)\) bit work. Final metric
accumulation uses one common determinant-squared denominator; adding
\(n\) integer products costs only another \(\log n\) bits, already
included in \(b\). No products of successive basis denominators are
retained.

### Required correction: initial rank-selection space

Candidate lines 227--232 describe up to \(q\) full-table pivot stages,
updating up to \(ns\) entries with \(O(qb)\)-bit minors. Lines
282--286 then claim that overwriting another copy of the source table
does not change the peak in (15). That conclusion does not follow:
expanded entries need \(O(nsqb)\) bits, potentially
\(O(ns^2b)\), while (15) only allows \(O(nsb+s^3b)\) besides
packet storage. A constant number of arrays does not remove the growth
in each entry's bit length.

This is a resource-proof gap, not a counterexample to the metric theorem
or the desired existence of a small-memory selection algorithm. The
following explicit replacement suffices:

1. Keep the original integer table at its original \(O(b)\)-bit entry
   precision. Retain at most \(s\) linearly independent original rows.
2. For each incoming row, perform exact fraction-free elimination on
   the retained rows plus that row, a matrix of size at most
   \((s+1)\)-by-\(s\). Append the original row exactly when rank
   increases. Retain pivot-column indices from the rank computation.
3. At the end, the retained rows span every original row, by induction.
   Their independent pivot columns produce the required nonsingular
   square block. Feed it to the candidate's unchanged swap phase.

Each small rank test uses \(O(s^3)\) integer operations on
\(O(sb)\)-bit integers, so all tests cost \(O(ns^5b^2)\), within
(14). Only \(O(s^2)\) expanded integers are live, using
\(O(s^3b)\) bits. The retained original rows and their indices fit
this same bound. This schedule establishes (15) without storing a
transformed full table. The candidate should state it and remove the
contrary overwrite claim before its initialization peak is accepted.

## 3. Exact and rounded causal acquisition

Exact real acquisition follows by induction on the retained scalar
prefix. At a matching prefix, each selected field evaluation is the
corresponding restricted column of the table used to construct the
metric. The Gram identity equates the next bilinear reduction; identical
scalar noise then equates the next prefix. Previously created fields
must retain their creation-time scalar arguments, as the candidate
expressly requires.

For the finite tape, the exact-product/common-rounding convention in
Section 5 is essential and sufficient. Both implementations multiply
the same rounded dyadic field operands exactly, sum exactly, add the
same finite noise, and use the same final scalar rounding. The compact
rational metric gives exactly the same rational input to that rounding
operation. This reconstructs every rounded prefix, including a prefix
on a rounding boundary. It does not rely on continuity of rounding.

The candidate correctly does not claim identity with a legacy tape
whose row products were rounded separately. If operand errors are at
most \(u\) and magnitudes at most \(B\), changing a product costs at
most \(2Bu+u^2\), plus the old product's rounding allowance. Uniform
averaging preserves this local bound, which can be included in the
inherited causal numerical budget.

For rounded metric entries, symmetric rounding with entry error
\(\rho\), followed by addition of \(q\rho I_q\), gives

\[
\widehat M\succeq M,
\qquad \|\widehat M-M\|_{\mathrm{op}}\le2q\rho.
\]

Consequently pair error is at most \(2q^2B^2\rho\). The loss of
exact normalization is controlled by the same estimate with constant
operands. Furthermore,

\[
|u^TMv-\widetilde u^TM\widetilde v|
\le4q^2\bigl(
\|u-\widetilde u\|_\infty\|v\|_\infty+
\|\widetilde u\|_\infty\|v-\widetilde v\|_\infty
\bigr).
\]

The analogous coefficient for \(\widehat M\) is still universal times
\(q^2\) when \(\rho\le1\). Only multiplication by this fixed
metric occurs; no inverse metric or small-eigenvalue loss enters the
online estimate. Its additional logarithmic sensitivity is
\(O(\log q+\log(B+2))\). The core's \(O(R)\) causal phases
therefore retain amplification \(2^{CR\chi}\), and \(CR\Theta\)
bits suffice for source and metric precision under that core's
certificates. Rounding contributes additive errors throughout this
comparison, not Lipschitz constants for a discontinuous interpreter.

The private selection may depend on the completed virtual source.
That is the same permitted preprocessing dependence as in the supplied
packet-selection notes. It is not new posterior conditioning data.
The ideal empirical-average noisy history remains the probabilistic
reference; numerical prefix closeness is the only bridge used here.
The broader posterior robustness and physical fidelity statements remain
inherited interfaces, not consequences of the Gram identity alone.

## 4. Reconstructed resource ledger

Use the candidate's actual field bound \(R\), packet dimension
\(D=O(R)\), scalar-update count \(P=O(R^2)\), and sufficient
precision \(O(R\Theta)\). The following counts include growing
word lengths.

| Component | Reconstructed bound | Status |
|---|---|---|
| Packets, rounded metric, noise marks, current history, coefficient templates | \(B_{\rm in}+CR^3\Theta\) bits | Verified |
| Exact metric construction work | \(CnR^8\Theta^3\) | Verified |
| Metric construction peak | \(C[nR^2\Theta+R^4\Theta]\) bits | Requires the streaming rank correction above |
| All compact acquisition updates | \(CR^7\Theta^3\) internal work | Verified with the stated incremental coefficient preparation |
| All acquisition activation/data calls | \(CR^4\), at precision \(CR\Theta\) | Verified |
| Total retained information | \(B_{\rm in}+C[R^3\Theta+(L+1)R^3\Theta^2]\) bits | Verified under the unchanged query-seed interface |
| Stored-median query peak | \(B_{\rm in}+C(L+1)^2R^5\Theta^2\) bits | Unchanged core bound, correctly retained |
| Threshold-search query peak | \(B_{\rm in}+C(L+1)[R^4\Theta+R^3\Theta^2]\) bits | Verified composition of unchanged core terms |

The acquisition work follows from \(P\) stages, at most \(q=O(R)\)
selected packets, and core row work \(O(R^2w^2)\) with
\(w=O(R\Theta)\): the total is \(O(R^7\Theta^2)\).
Whole-source incremental coefficient preparation contributes at most
\(O(R^7\Theta^3)\), and pair-form evaluation is smaller. The call
count multiplies \(P\), \(q\), and \(O(R)\) activation/derivative
calls per row. These bounds would not justify recomputing every whole
coefficient schedule separately for every scalar summary; the stated
incremental implementation is relevant.

For initialization, the existing Gaussian schedule contributes
\(O(nR^5\Theta^4)\), since it generates \(O(R)\) coordinates per
row at \(O(R\Theta)\) bits. Source pair-stage row arithmetic is
at most \(O(nR^6\Theta^2)\), and shared coefficient preparation is
at most \(O(R^7\Theta^3)\); both fit the metric-work term in (23).
The candidate's full internal initialization upper bound is therefore
safe once the rank-space correction is made. Actual activation/data,
certificate, input, and single-call scratch costs remain additions.
The seed also remains in the initialization peak in (24).

The retained query seed has not been replaced by a packet count, and
the actual median arrays have not been replaced by the state of their
smaller proof tests. This avoids the main possible omissions in a total
memory claim. The last paragraph's substitutions using
\(R\propto Z^{9/2}\), \(\Theta\propto Z^2\) give exactly
\(31/2,42,75/2,35/2\) for the four listed terms. Only this algebra
was checked: the shorter temporal-source certificate supplying those
powers was outside this review's input scope.

## Conclusion

One localized implementation correction is necessary before accepting
the frozen candidate's initialization-memory bounds. The streaming rank
repair above preserves its work and all advertised memory exponents.
No other blocking error was found in the bounded metric, causal
acquisition, finite-bit, or total-memory substitution checked here.
Neither the original frozen version nor the corrected candidate would
by these arguments alone prove a fourth- or fifth-logarithmic-power
full-model memory theorem or constitute promotion of the full scientific
result.

## Bounded correction recheck: initialization peak resolved

2026-10-06. The supervisor supplied a revised candidate with SHA-256
1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea.
The revision is confined to the initial rank-selection schedule in
Section 4.2 and the associated storage explanation after (15). Those
passages and their surrounding arithmetic were rechecked; scientific
input scope was not expanded.

The correction closes the finding above. The algorithm now keeps the
full source table at its original entry precision and performs rank
tests only on retained independent original rows plus the incoming
row. Inductively, a rejected row lies in the span of the retained rows,
and an accepted row enlarges that span. At completion the retained rows
therefore span the full table and remain independent. Their pivot
columns supply the square nonsingular block required by the unchanged
determinant-improvement phase.

Each test has at most \(s+1\) rows and \(s\) columns. Its \(O(s^3)\)
integer operations on \(O(sb)\)-bit minors cost \(O(s^5b^2)\) bit
work and require only \(O(s^3b)\) expanded scratch. Repeating for
\(n\) rows costs \(O(ns^5b^2)\), within the existing
\(O(ns^5b^3)\) work allowance. The source table contributes
\(O(nsb)\), the packet array contributes \(O(nDb)\), and the small
rank test, adjugate, and metric arrays fit \(O(s^3b)\). This proves
the peak in (15) and hence resolves its uses in (22) and (24).
The incorrect full-table overwrite justification has been removed.

**Revised bounded verdict:** the identified initialization-memory gap
is resolved, with no remaining blocking finding in the reviewed
metric/acquisition substitution. The original review and its frozen
hash remain preserved above. All inherited source, posterior, generator,
physical-fidelity, and interface qualifications remain in force; this
recheck is neither promotion nor a full scientific theorem review.
