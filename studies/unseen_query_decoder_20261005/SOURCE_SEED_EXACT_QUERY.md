# Regenerating the finite source: a different route around the passive bias

The combined finite-confidence result, including the separately proved
source event and charged radius refinement, is in
[TWO_GAP_CLOSURE_RESULT.md](TWO_GAP_CLOSURE_RESULT.md). This note supplies
its query component; the original standalone conditional boundaries below
remain explicit.

2026-10-07. Lead-author candidate with a bounded independent reconstruction
in SOURCE_SEED_EXACT_QUERY_CHECK.md. Its two requested corrections are
incorporated below; the scientific source-probability interface remains
separate. This is not promotion.
This continues the same unseen-input question. It changes the decoder and
its retained randomness; it does not strengthen the previous passive
estimator by changing a constant.

**Claim boundary.** The finite-transcript and amplification lemmas below
are finite statements. The proposed neural application is conditional on
the physical source certificates, their sufficient width, and the local
finite implementation already stated in the study. It replaces the
passive-population approximation by regenerating the original finite
source rows and retaining the complete conditional covariance correction.
It pays additional logarithmic memory and work. No claim is made that the
previous sixth-power bit table is unchanged.

## 1. Setup and what is retained

Keep width \(n\), sample count \(m\ge d\), depth \(L\ge2\), population
feature-Gram gap \(\gamma>0\), label RMS \(Y=\|y\|_2/\sqrt m\), the
activation envelope \(\beta\), and confidence \(1-\delta\). The network,
original Gaussian initialization, zero readout, mean-square loss,
mobilities \((n,1,\ldots,1,n)\), and full original label intersection
are unchanged. Activation values may be unbounded.

The independent dense reference is unchanged. Its deterministic
width-\(n\) proof center is denoted \(f_{0,n}\). Write \(b_n\) for the
existing label-refined dense upper certificate at confidence
\(\delta/256\), with its previously unspecified lower-order mesh
coefficient explicitly chosen as in NUMERICAL_BENCHMARK_ABSORPTION.md,
Section 5. This preserves its leading coefficient, exponential factor
and logarithmic power; it specifies the original proof's \(Y/n\) term,
not an arbitrary previously fixed smaller numerical coefficient.
The center and certificate are proof
objects, not inputs to the decoder. The zero-label branch is exact.

Use the locally precise finite source of FAST_FINITE_SOURCE_BRIDGE.md
with the improved physical interface of GAP_REFINED_PHASE_COSTS.md.
For the modular proof only, \(R\) bounds the actual number of named
fields, calls, input coordinates and layers, and \(p\) counts bits per
numerical word, including integer parts, exact accumulation and counters.
They can be chosen with universal constants so that

\[
 Z=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right),\qquad
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\quad
 p\le C\beta^{110L}Z.                                      \tag{1}
\]

All assertions using (1) retain its physical/source hypotheses.
Numerical tiny-label normalization uses either the existing \(nY\ge1\)
branch or the separately certified additional \(\log_+(1/Y)\) precision.

The new compact object is a finite collection of the existing selected
metrics, selected packets and current scalar states, together with short
seeds that regenerate the virtual sources. Each member evolves by the
same exact finite metric-acquisition algorithm. Full future scalar
answers, full row tables and dense matrices are discarded after setup.
The seeds describe random input, not fitted answers. Each member also
retains its scalar-noise marks in its counted scalar state, so training
does not regenerate an outer block at every scalar update.

At a query the algorithm regenerates rows of a member's original source.
It evaluates the old finite row instructions using their already acquired,
immutable scalar arguments. It does not recompute scalar training updates.
It then appends a finite passive forward pass, acquiring its new scalar
pairs by streaming all \(n\) regenerated rows. The final answer is the
median of the member predictions.

## 2. A finite-transcript generator lemma

Consider a deterministic finite algorithm whose random inputs are:

* \(n\) independent uniform row blocks, each with at most \(D p\) bits;
* a separate finite random string \(e\), independent of those blocks;
* a fixed external query code.

Suppose its only communication between different rows is at most \(P\)
scalar reductions. Each reduction is an exact sum of dyadic row tests,
followed by specified finite scalar processing. A row test is a
deterministic function of the row block, \(e\), and the earlier scalar
transcript. Include all scalar branch decisions and guards in that
transcript or make them deterministic functions of it. Assume the
complete transcript has at most \(B\) bits, and that for a fixed
candidate transcript every row test can be evaluated with finite scratch.
Let \(s\) bound the bits for all running sums and counters between rows.

For fixed \(e\) and fixed candidate transcript \(c\), a one-pass verifier
does the following:

1. Hardwire \(c,e\) and the external code in its finite transition rule.
2. Read a row block and evaluate every prescribed row test at the
   creation-time arguments supplied by \(c\).
3. Add its contributions to the \(P\) exact dyadic accumulators.
4. After the last row, test whether every scalar instruction, rounding
   operation and guard would give exactly the candidate transcript.

The verifier's acceptance is exactly the event \(T=c\). Indeed, if it
accepts, induction over scalar instructions identifies each candidate
prefix with the actual prefix. The converse substitutes the actual
transcript. A fixed deterministic program has exactly one transcript.
This argument does not differentiate a rounded instruction.

Apply the unconditional block generator of Nisan to this verifier with
error \(\varepsilon 2^{-B-1}\) per candidate. A sufficient block length is

\[
 A=C\{Dp+s+B+\log(n+2)+\log(1/\varepsilon)\}.                \tag{2}
\]

The seed has \(C A\log(n+2)\) bits. Each row block is computed by
at most \(C\log(n+2)\) two-universal hashes, hence at most
\(C A^2\log(n+2)\) bit operations and \(C A\) scratch, with
schoolbook binary convolution.

For every candidate \(c\), the two probabilities differ by at most
\(\varepsilon 2^{-B-1}\). Therefore

\[
 \|\mathop{\rm Law}(T_{\rm generated}\mid e)
       -\mathop{\rm Law}(T_{\rm iid}\mid e)\|_{\rm TV}
 \le \frac12\,2^B\varepsilon 2^{-B-1}\le\varepsilon.        \tag{3}
\]

The bound is uniform in \(e\), so averaging preserves it when \(e\)
has its original independent law. No transcript is enumerated by the
implemented algorithm. The exponential number of proof tests contributes
its logarithm \(B\) to (2), not exponential setup work.

The implemented algorithm may regenerate a row many times. The proof
does not apply a one-pass theorem to that repeated-read execution:
it applies it separately to the one-pass event verifiers just constructed.
This distinction is essential.

The external input to this lemma can vary over any fixed finite set:
the same generator fools the verifier for each code. Equation (3) is
a separate marginal assertion for each code, not joint total variation
for the outputs of all codes.

The needed generator statement is Lemma 3 of
[Nisan's original paper](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
Its block model bounds only the state between blocks. The block alphabet
is enlarged to (2), unused bits are discarded, the number of blocks
is padded to a power of two, and the block constant makes both its
state and error hypotheses hold. Its recursive hash construction
supplies the operation counts above. No cryptographic hypothesis is used.

## 3. Applying the lemma to the exact finite source

Every ordinary scalar reduction of the source is

\[
 c_a=Q_{h_a}\left(\frac1n\sum_i
       u_a(Z_i;c_{<a})v_a(Z_i;c_{<a})+\eta\widehat e_a\right).
                                                               \tag{4}
\]

The mandatory innovation contractions are reductions of the same form.
Their coefficients are frozen before reading the fresh innovation, and
the completed-call affine answer is then formed rowwise. Old fields
retain their creation-time scalar arguments. These are exactly the
finite instructions of FAST_FINITE_SOURCE_BRIDGE.md, not population
moments.

Append one passive query with at most \(L-1\) new hidden-matrix calls,
plus the first-layer input contraction and the final readout pair.
The source row packets reserve independent finite innovation coordinates
for these new calls. The independent string \(e\) includes both the
source scalar noise marks and the query scalar noise marks. It has
\(C R^2p\) bits. The query marks are not used by training.

For a current learned matrix write its rank-list increment as
\(D=T A S^\top/n\), where \(T,S\) are its old named fields and
\(A\) its acquired finite coefficients. A query uses exact empirical
contractions \(S^\top h/n\), formed by streaming the regenerated rows.
It computes \(D h\) rowwise, not from a posterior expectation.

The initialized-matrix part uses the complete two-orientation
conditional Gaussian formula. With old reverse queries \(U\), it is
of the form

\[
 \widehat t=Q_{h_t}(U^\top\widehat g/n+\eta\widehat e),\qquad
 \widehat y=Q_{h_y}(\widetilde m+
                     U\widetilde T\,\widehat t+c\,\widehat g).
                                                               \tag{5}
\]

Here the mean and small covariance coefficients are computed from
the actual acquired finite Gram table, with the explicit noise floors.
The full \(U\widetilde T\,\widehat t\) correction is retained.
Equation (5) is the same one-call implementation as the source.
There is no replacement of its covariance by a scalar covariance,
no independent-row population closure, and no prior/posterior
expectation substitution.

New query pair reductions use the same exact dyadic summation convention.
One pass obtains all pairs needed before a call, a second pass obtains
the innovation contractions, and a subsequent pass forms the output and
its needed pairs. A fixed constant number of passes per hidden layer
suffices. Earlier query fields are re-evaluated rowwise with their
already computed query scalar arguments. No training scalar is updated.

Use total finite guards and dummy failure outputs off the admitted
range. There are \(C R^2\) scalar words in the complete source-plus-query
transcript, and \(C R^2\) accumulators in its verifier. Their word size
includes \(\log n\). Thus \(B,s\le C R^2p\), \(D\le CR\), and, for
a fixed constant transfer error, (2) gives

\[
 A\le C R^2p,\qquad b\le C R^2p\log(en),                    \tag{6}
\]

where \(b\) includes the inner generator seed and all independent
scalar-noise bits for one member. In (6), the source and query numerical
literal bounds, bit ranges, and instruction counts are those of the
existing finite implementation. The test's hardwired transcript is
not retained in the model or supplied as an answer oracle.

### Literal compact acquisition does not require independent packets

FAST_LOCAL_PRECISION_TEST.md's metric replay proof is conditional on
the entire packet array before exposing each fresh scalar noise.
Its Gaussian rounding-boundary bound is uniform in the empirical mean.
Consequently its proof still applies to a generated packet array:
the necessary independence is the fresh scalar noise from that array
and earlier scalar noises, not independence between different packets.
The metric-selection identity itself holds for every finite field table.

Under a uniform one-member \(b\)-bit input the source generator seed
and scalar-noise bits are independent. The old metric selection and
rounding tolerance therefore give literal acquisition at failure at
most a chosen fixed constant, without a new source-distribution premise.
Once multiple member inputs are generated by an outer generator,
this failure is included in the member's bad-output test; independence
between them is not reasserted.

## 4. Fixed-query physical comparison without the passive bias

This section imports the scientific source event at a fixed small
confidence, not at confidence divided by the number of external codes.
It spells out the additional finite-query use of that interface.

On the original iid finite-source law, couple it to the physical
noisy program using the completed-call construction in
FAST_FINITE_SOURCE_BRIDGE.md. Append (5) to that same chronological
construction. Previously acquired fields remain identical in the two
programs until a coupling failure. The physical initialized matrices
keep their original joint law because future-used finite marks are the
same safe conditional augmentations used by the source.

For a query during training, this coupling concerns the acquired prefix
followed by its passive query. It does not first reveal discarded future
training answers and then use a prefix-conditioned posterior.

For the appended query, all local moment errors compare actual current
operands at the same history. The one-call bound (19) of that bridge
applies with the enlarged field count \(R+O(L)\), provided both old
source and new query errors meet its tolerance. Refining the new query
alone would not suffice. The common pre-setup schedule below refines
both, so that all source and query coupling failures together have a
fixed small probability, such as \(2^{-12}\).

Also take the fresh physical query-answer noise and postprocessing errors
so that their total prediction change is at most \(Yn^{-10}/8\).
On the physical operator and feature-RMS event, forward subtraction gives

\[
 \frac{\|\Delta h^{(\ell)}\|_2}{\sqrt n}
 \le \beta\left(10\frac{\|\Delta h^{(\ell-1)}\|_2}{\sqrt n}
                         +\epsilon_{\rm ans}\right).
                                                               \tag{7}
\]

The bounded readout RMS then gives the claimed prediction allocation by
choosing \(\epsilon_{\rm ans}\) smaller than \(n^{-10}\) times an
explicit inverse power of \(\beta^L(1+m/\gamma)\). The source parameter
error has its separate existing whole-sphere allowance.

Here is an explicit sufficient order for the shared numerical choices.
The extra symbols in this paragraph are only local tolerance parameters.
Set
\[
 a_{\rm qry}=\frac{n^{-10}}{C\beta^{6L}(1+m/\gamma)},
 \qquad \overline R=R+C(L+1),
\]
and use a common physical RMS cap \(\overline b\) for source and
query fields on the scientific event. Before generating any source:

1. Choose one initialized-answer noise scale for both source and query,
   \(\sigma\le\min(\sigma_{\rm source},a_{\rm qry}/16)\).
   A smaller training noise remains within its local forcing allowance.
2. In the finite bridge set
   \(z=C(2+\overline R+\overline b+\sigma^{-1})\), enlarged to
   dominate its declared finite coefficient and literal caps, and
   \(\xi=\rho_0/[2^{20}(\overline R+1)(n+1)z^{240}]\),
   with fixed small \(\rho_0>0\).
3. Rechoose every source and query moment grid, scalar-noise scale,
   answer grid and coefficient tolerance by bridge (21), with this
   common \(\xi\). Additionally bound each query rank-list,
   first-layer and finite arithmetic defect by its allocated fraction
   of \(a_{\rm qry}\). These are finite local operations; accuracy
   equal to \(a_{\rm qry}\) divided by a fixed polynomial in the
   declared operand/coefficient caps suffices. In particular the answer
   grid is below both its bridge allowance and
   \(\xi/[64(\overline b+1)]\), as well as the query allocation.
4. Choose innovation grid and Gaussian precision by bridge (17), scalar
   marks by (21a), and initial roots by (22). Include all reserved query
   coordinates in the Gaussian cutoff. Finally choose metric precision
   using the minimum source/query scalar grid as in the replay lemma.

These choices refine the old moments entering the new conditional solves
and retain one consistent physical answer-noise floor. They cannot be
made after selecting a metric from a coarser tape. Since
\(\log(1/a_{\rm qry})=O(\log n+L\log\beta+\log(1+m/\gamma))\),
every new tolerance logarithm remains within the existing certificate:
\(\overline R\le CR\) and \(p\le C\beta^{110L}Z\), with larger
universal constants. No ensemble factor enters these fixed-confidence
local tolerances.

Noise RMS failures are at most \(CL e^{-cn}\) for each fixed query.
Only logarithms of these tolerances enter \(p\); the source's existing
certificate includes \(\log n,L\log\beta,\log(1+m/\gamma)\) and
\(\log(1/Y)\) on its stated nonzero-label branch.

Thus, conditional on the inherited source/center theorem and its width
conditions, at every fixed coded input/time the iid finite
source-plus-query output lies in

\[
 [f_{0,n}(t,x)-b_n-CYn^{-10},\,
       f_{0,n}(t,x)+b_n+CYn^{-10}]                         \tag{8}
\]

with probability at least \(1-2^{-8}\), after fixed confidence
allocations. Source and query good events are not conditioned on a
private metric. This is a marginal fixed-query consequence of a joint
physical coupling, not an assertion that the finite scalar prefix
alone has a Gaussian posterior.

Apply (3) at fixed constant error and include the fixed metric replay
failure from Section 3. Enlarging the numerical and confidence constants
makes the implemented one-member bad-output probability at most \(1/16\).
There is no \(R/n\), \(K_*/n\), or \(\sqrt{RK_*/n}\) passive
comparison term: no step producing those terms has been performed.

## 5. Why one seed is insufficient, and how the whole-sphere event is obtained

One must not union the fixed scientific failure in Section 4 over the
external code set. Nor does a median of new passive noises sharing one
source remove a bad-source event. A source ensemble resolves this
quantifier problem; its extra storage is charged below.

Let \(N_{\rm ext}\) be the finite input/time code count from
FAST_PHYSICAL_QUERY_GRID.md. Its improved physical precision gives

\[
 \log N_{\rm ext}\le C(d+1)Z.                              \tag{9}
\]

Choose an odd \(J\ge C\log(16N_{\rm ext}/\delta)\). For genuinely
independent one-member inputs, at least half of their outputs are bad
with probability at most

\[
 2^J(1/16)^{J/2}=2^{-J}.                                  \tag{10}
\]

An outer Nisan block generator supplies the \(J\) member inputs without
storing \(J\) independent inner seeds. Its blocks have \(b\) bits,
enlarged if necessary by \(C\log(16N_{\rm ext}/\delta)\).
For a fixed external code, a finite-state bad-median test needs only
the member counter and the bad-output counter between blocks.
Within a block it may perform the entire finite source construction,
compact acquisition and exact finite query.
Its block transition is simply the resulting Boolean bad-output test.
The constant center threshold is hardwired only in that proof test.

Set outer fooling error to \(\delta/(16N_{\rm ext})\).
The block theorem therefore requires

\[
 C\{b+\log(N_{\rm ext}/\delta)\}\log(J+2)                   \tag{11}
\]

retained seed bits. No exponential-time verifier is executed by the
model. The implementation generates a member's block, executes its
ordinary construction or current-state query, then discards that block
when it is no longer needed. Construction and training maintain each
member's own compact state.

By (10), (11), and a union over the external codes, with probability
at least \(1-\delta/4\) all coded medians satisfy (8).
This amplifies the complete per-member failure, including its scientific
source event; no common recognizable source-good predicate is assumed.
Append the independent dense-reference event at its usual confidence
share. Rounding an arbitrary input/time to a code in its acquired patch
uses only the physical reference modulus, as in the existing grid proof.
The endpoint uses the frozen source tail. The proposed bound is

\[
 \sup_{t\in[0,\infty],\ \|x\|=\sqrt d}
 |\widehat f(t,x)-f_n^{\rm independent}(t,x)|
 \le 2b_n+CYn^{-10}.                                     \tag{12}
\]

The additive absorption in (12) now has a separate checked closure.
The explicit mesh coefficient just specified is at least 32 and at most
\(C\beta^{4L}(1+m/\gamma)\). Consequently \(b_n\ge32Y/n\).
If the allocated numerical remainder is \(A_{\rm num}Yn^{-10}\),
it is absorbed at
\[
 n\ge\max\{1,(A_{\rm num}/32)^{1/9}\},
 \qquad \|\widehat f-f_n^{\rm independent}\|_*\le3b_n.
\]
Here the local symbol \(A_{\rm num}\) counts the combined source,
query and physical-rounding allocation. Those tolerances may be set
with an absolute total allocation; otherwise the displayed polynomial
in that allocation must be retained. This uses no inverse of the
unspecified leading dense coefficient and no eventual dominance by its
\(\exp(c_1Y^2\sqrt{\log n})\) factor. The numerical lemma and
its exact scope were independently reconstructed in the addendum to
SOURCE_SEED_EXACT_QUERY_CHECK.md. The scientific source-success width
is still separate.

## 6. Retained and live costs of the proposed variant

All counts here are internal bits and bit operations; evaluator and
input/certificate interfaces remain separately charged.
Let \(E=1+\lceil\log_2(n+2)\rceil\), only within this cost derivation.
The inner generator block parameter is \(A\le CR^2p\).
Let \(b=C R^2pE+C\log(N_{\rm ext}/\delta)\), a sufficient
constructive choice, and keep \(J\) as in Section 5.

The \(J\) acquired metrics, selected packets and current scalar states
use \(CJR^2p\) bits. The outer seed uses \(Cb\log(J+2)\) bits.
Generating one member block and one inner block requires \(Cb\) and
\(CA\) scratch. One exact finite query uses \(CR^2p\) small matrices,
row scratch and accumulators. Store only the final \(J\) scalar
predictions before taking their median. Thus retained size and peak
training/query memory are bounded by

\[
 C\{JR^2p+b\log(J+2)\}.                                   \tag{13}
\]

Initialization processes members sequentially. Its peak is at most
(13) plus \(C(nRp+R^3p)\), not \(J\) times that dense temporary array.
Every future scalar-answer table is discarded after selecting its metric.

An inner generated row costs \(CA^2E\) bit operations. During setup
generate all finite packets once, then use the existing full temporary
table and metric construction. The work per member is at most

\[
 C\{nR^5p^3+(nR+R^2)p^4+R^5p^2+R^4p^3+
                      nR^2p^2+nA^2E\}.                  \tag{14}
\]

The complete training work is
\[
 CJ(R^5p^2+R^4p^3+R^3p^2),                               \tag{15}
\]
apart from outer-block regeneration, charged next. No row generator is
needed for the selected-packet updates.

At one query a fixed constant number of streams per hidden layer
regenerates source packets, old finite row fields and the appended
passive fields. Small coefficients use the separate-spectrum routines,
not a materialized Kronecker matrix. A conservative per-member bound is

\[
 C(L+1)\{n(A^2E+Rp^4+R^2p^2)+R^4p^2+R^3p^3\}.            \tag{16}
\]

Multiply (14) and (16) by \(J\). Generating all \(J\) member blocks
once costs at most \(CJb^2\log(J+2)\); add this term to each phase
where blocks are regenerated. Scalar median sorting costs
\(CJp\log(J+2)\). These are ordinary counted hash and finite-arithmetic
operations; no integral or sampling oracle remains in this variant.

At fixed problem parameters, (1), (9) give
\[
 R=O(Z^{5/2}),\quad p=O(Z),\quad J=O(Z),\quad
 A=O(Z^6),\quad b=O(Z^7).
\]
Consequently (13) is \(O(Z^7\log(e+Z))\) bits, and an integer
absolute logarithmic exponent eight suffices. Setup work is
\(O(nZ^{33/2}+Z^{15}\log(e+Z))\), all training is
\(O(Z^{31/2}+Z^{15}\log(e+Z))\), and query work is
\(O(nZ^{14}+Z^{15}\log(e+Z))\).
These are modular conditional envelopes, not the old sixth-power table.
No logarithmic-time query is proved.

Every modular factor in (13)--(16) is explicit. Substituting (1) and
(9) produces only fixed polynomial powers in \(m,d,1/\gamma,\beta^L\)
and logarithms of confidence, besides the separate scientific width.
For general activations the regenerated query requires at most
\(CJ(L+1)nR\) scalar activation/derivative evaluations, besides
small coefficient preparation. Their descriptions, precision-dependent
time and scratch remain charged; the old passive sampling call count
is not reused. An analytic envelope alone does not price an arbitrary
activation evaluator.
The complete source-probability theorem remains a separate obligation.
No optimality is claimed for the extra logarithmic memory.

## 7. Audit obligations and status

Before accepting this as a neural theorem, reconstruct:

1. The transcript verifier covers every implemented cross-row reduction,
   guard, scalar noise and finite branch; there is no uncounted row table
   in its between-block state.
2. The exact finite-source local coupling extends through one passive
   forward pass with the stated precision, retaining the full covariance
   correction and all source information restrictions.
3. Compact acquisition on a generated array uses only the uniform
   conditional rounding-boundary lemma, not iid row concentration.
4. The outer amplification is applied to independent complete source
   experiments before the generator replacement. It does not treat
   passive repetitions from one source as independent source successes.
5. Counts include the outer seed, all \(J\) learned states, local
   coefficient solves, repeated row regeneration, Gaussian conversion,
   numerical guards, and activation/input costs.
6. The separate finite-width scientific probability theorem holds.
   Numerical comparison to the explicitly instantiated structural
   certificate has the checked polynomial gate in Section 5.

The bounded independent reconstruction validates items 1--5 conditional
on their stated source/forcing/center interfaces, after requiring the
additive recurrence (7) and common pre-setup precision schedule now
incorporated in Section 4. Its addendum also checks Section 5's numerical
mesh lemma. The scientific probability in item 6 is not proved here.
This construction is therefore not a full answer
to the user's two-gap request, and does not supersede the existing
headline theorem or resource table until its new chain is checked.

Main scientific reads: FAST_FINITE_SOURCE_BRIDGE.md,
FAST_LOCAL_PRECISION_TEST.md, NOISY_TWO_ORIENTATION_TRANSCRIPT.md,
SANE_DECODER_CORE.md, SHORT_SEED_PRIOR_BLOCKS.md,
FAST_PHYSICAL_QUERY_GRID.md, GAP_REFINED_PHASE_COSTS.md,
FAST_FINITE_PASSIVE.md and GENERAL_DENSE_COMPARISON.md.
The original generator's block-model proof and hash construction were
read in full. The accuracy-onset and weak-route notes motivated avoiding
the prior/population substitutions, not assuming their missing bounds.
Supervisory discussion exposed the shared-source uniformity problem;
Section 5 deliberately amplifies whole source experiments to repair it.
No experiment, Git mutation, source-study edit or promotion occurred.
