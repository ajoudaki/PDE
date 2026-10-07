# Collaborative check: finite transcript transfer and a source ensemble

2026-10-07. Scoped mathematical assessment of a proposal supplied by the
supervisor after the separate calibration route was frozen. This is an
author collaboration, not an independent reconstruction of the complete
new decoder. No experiment or promotion.

The fixed-transcript transfer argument is valid under the existing
one-pass block-generator theorem. An ensemble of independent width-\(n\)
source experiments also resolves the common-event problem identified
below. A second block generator can reduce the randomness needed by that
ensemble. These results remove neither the remaining physical-query
implementation obligations nor the change in memory: the proposed
construction has a \(Z^7\log Z\) contribution where the current phase
table has \(Z^6\). It must be reported with its own cost table.

## 1. Exact finite-transcript lemma

Consider a total deterministic finite program with fixed external query
code \(q\), fixed global random marks \(e\), and \(n\) independent
row packets \(Z_1,\ldots,Z_n\). Each scalar acquisition depends on
empirical sums of row functions whose other arguments are earlier scalar
acquisitions. The row program may reread all packets in chronological
passes. Guards and halts have fixed finite representations, and the
whole scalar transcript has a canonical encoding of at most \(B\) bits.

For each candidate transcript \(t\), require a one-pass verifier
\(V_{q,e,t}\) which accepts exactly when the deterministic program's
actual transcript equals \(t\). Once \(t\) is fixed, every old
creation-time argument and every query context in a row function is fixed.
One pass can therefore accumulate every required empirical sum, followed
by exact checks of all rounded scalar equations and guards. The verifier
does not assume that its declared transcript is consistent.

Let a block generator change the acceptance probability of every such
verifier by at most \(\varepsilon\). Write \(T\) and \(\widehat T\)
for the resulting iid and generated transcripts. Since the program is
total and deterministic, the acceptance events partition the packet space.
Consequently

\[
 \|\mathcal L(T\mid e)-\mathcal L(\widehat T\mid e)\|_{\rm TV}
 =\frac12\sum_t
       |\Pr(V_{q,e,t}=1)-\Pr_{\rm gen}(V_{q,e,t}=1)|
 \le 2^{B-1}\varepsilon.
 \tag{1}
\]

Uniformity over the fixed marks \(e\) allows integration over independent
true finite marks without a further union bound. Any event determined by
the scalar transcript, including a final scalar output lying outside a
hardwired interval, inherits (1). The proof-only threshold can be rounded
with a reserved numerical margin. It is not an input to the decoder.

This proves a statement about the transcript distribution. It neither
proves total variation of the full packet arrays nor invokes a generator
for arbitrary repeated-read machines. No computational enumeration of
the \(2^B\) transcripts occurs at runtime.

For the current source, a sufficient verifier state is
\(S_v=C R^2p\) bits: at most \(CR^2\) exact dyadic empirical sums,
their counters, finite scalar marks, and the current row workspace.
An exact sum of \(n\) products of \(p\)-bit fields uses
\(C p+\lceil\log_2(n+1)\rceil\) bits; the latter is already in
the chosen precision allowance. The required conditions are

\[
 B\le CR^2p,\qquad S_v\le CR^2p,
 \qquad \text{one packet's random bits}\le CRp.
 \tag{2}
\]

Small posterior coefficient arrays must be deterministic finite functions
of the declared scalar transcript. Private selected metrics and packets
may determine the acquisition implementation, but query values must depend
on them only through that transcript if they are omitted from (2).
Exact replay then identifies their scalar values on every finite source
array. A missing non-scalar source dependency would invalidate the
verifier, rather than being another statistical error.

Let
\(E=1+\lceil\log_2(nRp+2)\rceil\). The verified block-generator
interface of SHORT_SEED_PRIOR_BLOCKS.md, Section 2, gives a sufficient
inner block parameter and source-seed length

\[
 A\le C\{R^2p+\log(1/\tau)+E\},\qquad
 b_{\rm seed}\le CAE,
 \tag{3}
\]

by taking \(\varepsilon=\tau2^{-B}\), which makes (1) at most
\(\tau/2\). The other \(CR^2p\) genuinely independent finite
scalar-noise bits are counted separately. Formula (3) does not supply
physical accuracy by itself.

## 2. Why repeated passive queries on one source are insufficient

Per-query transcript transfer does not transfer a common scientific
good event automatically. The following exact example isolates the issue.
There are \(M\) query codes and the retained scalar source state is
constant. In one experiment let \(B_0\) be Bernoulli with parameter
\(1/M\), and return \(X_q=B_0\) for every code. In a second, let
\(T_0\) be uniform on the \(M\) codes, and return
\(X_q=\mathbf1_{\{T_0=q\}}\).

For every fixed code, the output law is identical. Arbitrarily many
passive replicas sharing the same source can return the same output;
these replicas are conditionally independent given the source because
their conditional laws are point masses. Nevertheless the probability
of an error anywhere is \(1/M\) in the first experiment and one in
the second.

Thus a fixed scientific failure cannot be unioned over query codes after
transferring each marginal separately. A recognizable common source-good
predicate would repair this particular issue if one were proved. The
source-ensemble repair below does not require that additional predicate.
This example concerns the proposed probability inference only; it is
not a neural counterexample.

## 3. Ensemble amplification with all scientific failures included

Suppose the complete single-source finite construction, including its
exact empirical passive query, has the following per-code consequence
after (1): there is the same deterministic proof center \(f_{0,n}(q)\)
for all codes such that

\[
 \Pr\{|X_q-f_{0,n}(q)|>b_n+e_{\rm num}\}\le1/16
 \quad\text{for every fixed }q.
 \tag{4}
\]

Here \(b_n=b_n(\delta/256)\) is unchanged, and all source, dense,
finite-Gaussian, and rounding failures are included in \(1/16\).
Neither a posterior/prior bias nor the old passive population recursion
may be used in place of the exact empirical query when proving (4).
The source's scientific probability theorem is needed only at fixed
confidence for (4); the independent dense comparison defining \(b_n\)
retains its specified confidence share.

Take odd \(J\) independent complete source experiments, each at width
\(n\), and define the decoded output as their scalar median. At a
fixed code, if the median lies outside the interval in (4), at least
\(J/2\) source experiments fail there. A subset union gives

\[
 \Pr\{\text{median fails at }q\}
 \le2^J(1/16)^{J/2}=2^{-J}.
 \tag{5}
\]

This amplifies scientific source failure as well as passive randomness.
For \(Q\) physical external codes, choose
\(J\ge\lceil\log_2(4Q/\delta)\rceil\), rounded up to an odd integer.
A union of (5) then controls all codes. No joint coupling to all dense
physical trajectories is needed: (4) uses one common deterministic center.

Each source uses the original nonlinear model and width \(n\).
There is no comparison to a wider dense network or to a different-width
center. There are nevertheless \(J\) source constructions, selected
metrics, and current scalar states. Their initialization, training, and
retained descriptions must all be counted.

## 4. A second block generator avoids storing all inner seeds

Let one complete single-source experiment use \(b\) independent bits:
the inner seed in (3), its independent finite scalar marks, and its
query-global finite marks. Reserve the query marks and row innovations
in its seed from initialization so that outputs are repeatable. With a
single exact passive query per source and \(L\le R\), a sufficient
bound is

\[
 b\le C\{R^2p+E+\log(1/\tau)\}E.
 \tag{6}
\]

For each fixed external code, consider a one-pass proof test reading
these \(J\) independent \(b\)-bit blocks. Within each block it may
recompute the complete hypothetical source experiment, evaluate its
query, and test the interval in (4). Between blocks it retains only
the failure counter, using \(C\log(J+2)\) bits. The cited block
theorem explicitly permits unrestricted computation within a block.
This proof test is not the runtime query algorithm: runtime uses each
source's already retained current state.

Applying the block theorem a second time, with error
\(\varepsilon_{\rm out}\le\delta/(4Q)\), requires

\[
 A_{\rm out}
 =C\{b+\log(J+2)+\log(4Q/\delta)\},
 \qquad
 S_{\rm out}\le C A_{\rm out}\log(J+2)
 \tag{7}
\]

retained seed bits. The actual source blocks are then correlated, but
the count-test probability differs from its independent value by at
most \(\varepsilon_{\rm out}\). Combining (5), (7), and a union over
the \(Q\) codes gives all-code median failure at most \(\delta/2\).
Independence must not be asserted for the generated ensemble itself.

The outer generator also permits regenerating any one source block when
needed, at cost \(C A_{\rm out}^2\log(J+2)\) bit operations and
\(C A_{\rm out}\) scratch. Regenerating the block supplies the same
inner source seed and scalar random marks; it does not require replaying
scalar training. Retain the \(J\) private acquisition models and
current scalar states separately. No uncharged randomness is used.

On the separate independent dense-center event, the resulting coded
prediction satisfies

\[
 |\widehat f_n(q)-f_n^{\rm independent}(q)|
 \le2b_n+e_{\rm num}.
 \tag{8}
\]

Physical rounding adds only its previously certified reference modulus.
If its allowance plus \(e_{\rm num}\) is at most \(b_n\), equation
(8) gives the desired \(3b_n\) error. There is no residual
\(Y\mathcal P\sqrt{(R+1)(K_*+1)/n}\) in this implication.
This is conditional on proving (4) for the actual implemented exact
empirical query, including local finite conditioning and caps.

## 5. Honest memory and work boundary

The source ensemble retains at least its separately counted
\(CJR^2p\)-bit models and states, as well as the outer seed and one
regenerated inner block. Thus a sufficient modular allowance is

\[
 S\le C\{JR^2p+A_{\rm out}\log(J+2)+R^2p\}.
 \tag{9}
\]

For the gap-refined choices
\(R\le C\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2}\),
\(p\le C\beta^{110L}Z\), \(E\le CZ\), and
\(J\le C(d+1)p\), this contains

\[
 R^2pE\log(J+2)=
 O\!\left(\beta^{512L}(m+d+2)^2(1+m/\gamma)^2
                Z^7\log(J+2)\right).
 \tag{10}
\]

The \(JR^2p\) term has logarithmic power seven and its additional
\((d+1)\beta^{110L}\) factor. The constants remain universal only
when these major parameter factors are displayed. At fixed problem
parameters, (10) is \(O(\log^7n\log\log n)\), and an absolute
power-eight envelope is possible. It is not the current power-six
bit-memory result. No width inequality can turn one logarithmic memory
power into a smaller uniform power for all sufficiently large \(n\).

All source initialization and compact training work is multiplied by
\(J\), plus regeneration of their outer blocks. Each query computes
all \(J\) exact empirical predictions, charges every full-width row
pass, each inner generator call, the small-matrix coefficient work,
and the final scalar median. If those operations cost
\(nA_0Z^k+A_1Z^{k_1}\) with fixed absolute exponents and polynomial
major-parameter coefficients, their dense-forward comparison is
polynomially enforceable. For example,

\[
 A_0Z^k\le n
 \quad\text{is ensured by}\quad
 n\ge[C_kA_0(1+z)^k]^2,
 \qquad Z=\log(en)+z,
 \tag{11}
\]

because \(\log(en)^k/\sqrt n\) has a finite absolute maximum
\(C_k\). An analogous explicit gate absorbs the preparation term
into \(n^2\). This statement cannot replace an actual operation
ledger for the exact rank-correction query.

## 6. Required completion checks

The proposal is viable at a changed memory bound, conditional on four
concrete author obligations:

1. Specify the actual finite passive call, including the retained
   rank correction, its empirical contractions, physical Gaussian
   coupling, guards, and per-code error (4).
2. Verify that every source and query feedback scalar fits (2), with
   no packet-array dependency missing from the fixed-transcript check.
3. Give the complete ensemble cost table and the polynomial sufficient
   width for every source-probability, numerical, and dense-forward gate.
4. Report (9)--(10) explicitly. If the user's required memory is the
   existing power-six bound, this variant does not meet that requirement.

The fixed-transcript lemma, its shared-source limitation, and the outer
source-ensemble amplification are mathematical checks completed here.
The full physical finite-query construction and its exact phase costs
are the supervisor's separate author work. The source success theorem
has not been assumed proved by this assessment.

## Provenance

The supervisor supplied the source-seed and outer-generator proposals.
The complete current SHORT_SEED_PRIOR_BLOCKS.md was read for its precise
generator interface. Its verified primary theorem is imported at that
stated scope; this assessment does not claim to have independently
reread the external paper. The current finite source and query interfaces
were read in FAST_FINITE_SOURCE_BRIDGE.md (Sections 1--5 through its
one-call caps) and FAST_UNIFORM_QUERY.md (the generator and seed
interfaces), in addition to the complete passive and finite-posterior
notes recorded in FINAL_ERROR_CLOSURE_ROUTE.md. No unseen sibling
proof was used. The source-input limits, proof-only authorization, and
required mathematical skills remained in force.
