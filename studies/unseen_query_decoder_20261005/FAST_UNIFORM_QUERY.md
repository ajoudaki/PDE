# Reachable query contexts, shared Gaussian tails, and the sampling boundary

2026-10-06. Scoped author derivation in the current unseen-query study.
No experiment, Git operation, maintained-source edit, or independent review.

Two changes give a smaller uniform decoder. Round the external input and
patch time once, and use independent seeds at successive passive layers.
The probability argument then covers only the contexts actually reached at
those external arguments. A second change charges a Gaussian-tail event
once per layer stream, using a separate one-pass test. Neither change
requires a net over all incoming moment vectors.

The resulting candidate bounds, in the modular parameters defined below,
are

\[
\begin{split}
 S_{\rm retained}&\le B_{\rm in}
       +C\{R^3\Theta+Q R^2\Theta^2\},\\
 S_{\rm retained+peak}&\le B_{\rm in}
       +C\{(d+1)R^3\Theta^2+Q R^2\Theta^2\},\\
 W_{\rm query}&\le
       C Q\{s(d+1)R^6\Theta^5+R^7\Theta^3\}.
                                                        \tag{1}
\end{split}
\]

Here \(Q\le C(L+1)\) counts successive passive moment stages and
\(s\) is the actual number of independent rows in a statistical block.
Activation, data, certificate, and input/output costs are additional and
are displayed below. The source construction and retained metric are the
already supplied candidate constructions, not new results of this note.
These are improvements to seed length, peak space, and the multiplicative
query cost. They do not establish polylogarithmic query work: the present
general block method still uses \(s\) of near-width order at root-width
accuracy.

## 1. Preserved model and precise imported interfaces

Keep \(m\) training inputs \(x_a\in\mathbb R^d\),
\(\|x_a\|=\sqrt d\), spanning \(\mathbb R^d\), and therefore
\(m\ge d\). Write \(v_a=x_a/\sqrt d\). With \(L\) hidden layers,
the original finite network is

\[
 z_a^{(1)}=W^{(1)}v_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_{n,a}=\frac{W^{(L+1)T}h_a^{(L)}}n.
\]

Its residual and loss are \(r_a=f_{n,a}-y_a\) and
\(\mathcal L_n=m^{-1}\sum_a r_a^2\). The derivative coordinates are

\[
 \delta_a^{(L)}=W^{(L+1)}\odot\phi_L'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
                       W^{(\ell+1)T}\delta_a^{(\ell+1)}.
\]

All hidden blocks train. With block mobilities \((n,1,\ldots,1,n)\),
the mean-loss gradient flow has

\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
 \quad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
                  r_a\delta_a^{(\ell)}h_a^{(\ell-1)T},
 \quad
 \dot W^{(L+1)}=-\frac2m\sum_a r_a h_a^{(L)}.
\]

First weights are standard Gaussian, hidden entries have variance \(1/n\),
and the stored readout starts exactly at zero. Keep the original complete
small-label allowance, feature-Gram gap \(\gamma>0\), and strip-analytic
activation class with bounded first and second derivatives; activation
values may be unbounded. This note does not alter those assumptions.
The target remains the independent dense-reference, simultaneous
whole-sphere, all-physical-time and fitted-endpoint certificate of
`COST_CONTRACT.md` and `RECALIBRATION_FREE_MOMENTS.md`. No query is declared
before acquisition, and a query does not replay training.

Condition on the complete permitted source and its actual numerical
prefixes. For prefix \(j\), write \(\nu_j\) for the proof-only one-row
posterior marginal and \(\mu\) for the standard Gaussian packet prior.
The imported statistical interface is

\[
 D(\nu_j\Vert\mu)\le h,\qquad
 \mathbb E_{\nu_j}UU^T\preceq I_r,\qquad |G|\le B,
 \qquad r\le C R.                                      \tag{2}
\]

Neither \(\nu_j\) nor its expectation is evaluated. The algorithm
approximates \(\mathbb E_{\nu_j}[UG]\) with prior samples. Fresh query
Gaussians can be appended to both laws without changing (2). The bounded
\(G\) is the existing physically inactive query cap; it is not an added
bounded-activation assumption.

The source row circuit, conditioning coefficients and observed common
Grams are those of `SANE_DECODER_CORE.md`. Let \(R\ge2\) bound the
number of named physical fields, histories and matrix calls, with packet
dimension \(D\le C R\), scalar-prefix count \(P\le C R^2\), and
\(d\le m\le R\). The numerical certificate \(\chi\) includes the
logarithms of operand caps, inverse floors and local sensitivities. Set

\[
 \Theta=2+\chi+\log_2(n+2)+\log_2\delta^{-1}
                         +\log_2\varepsilon^{-1},
 \qquad \varepsilon=n^{-10}.                            \tag{3}
\]

The following are imported conditional interfaces, not reproved claims:

1. The exact causal map has logarithmic sensitivity at most \(C R\chi\).
   Earlier named fields retain their creation-time scalar arguments.
2. A \(w\)-bit fixed-context coefficient preparation costs
   \(C(R^5w^2+R^4w^3)\) bit operations and \(C R^2w\) live bits.
   A row costs \(C R^2w^2+C R T_{\phi,\rm data}(Cw)\), with
   \(C R^2w+S_{\phi,\rm data}(Cw)\) live bits. Input contractions
   are covered since \(d\le R\).
3. A clipped finite Gaussian packet costs \(C D w^4\) bit operations
   and \(C D w\) scratch bits when its cutoff squared is at most \(Cw\).
4. The one-pass block-generator interface in
   `SHORT_SEED_PRIOR_BLOCKS.md` and the small median test in the core
   apply: for \(N\) random blocks, block length \(A\), and error
   \(e^{-F}\), it is sufficient that \(A\) dominate the between-block
   state, \(F\), \(\log(N+2)\), and the random bits in one row.
   Seed length is \(C A\log(N+2)\), generation work per row is
   \(C A^2\log(N+2)\), and generator scratch is \(C A\).
5. The selected-metric acquisition base of `SANE_METRIC_PACKETS.md`
   costs \(B_{\rm in}+C R^3\Theta\) retained bits. Its decoder sees
   only the current scalar prefix, not the private metric or packets.

All constants \(C\) in the modular statements are universal. Original
input descriptions are charged by \(B_{\rm in}\); no evaluator cost
is hidden in \(C\). The source probability, physical comparison, and
effective-width questions remain precisely their imported obligations.

## 2. A finite external grid and independent seeds per passive stage

The passive recursion has fixed depth. Its typical hidden-layer step is

\[
 h_\ell=\chi_\ell\bigl(U_\ell^T A_\ell b_{\ell-1}
                       +\sqrt{\beta_\ell}\,g_\ell\bigr),
 \quad
 \beta_\ell=\sigma^2+max\{0,c_{\ell-1}
                              -\|P_\ell b_{\ell-1}\|^2\},
\]
\[
 b_\ell=\mathbb E_{\nu_j,g}[V_\ell h_\ell],\qquad
 c_\ell=\mathbb E_{\nu_j,g}[h_\ell^2].                   \tag{4}
\]

Here \(\chi_\ell\) denotes the capped activation, whereas \(\chi\)
without a layer is the numerical certificate in (3). Cross moments are
projected onto their prescribed Euclidean ball and second moments onto
their prescribed interval. Their numerical counterparts feed the next
layer. The first layer and final readout use the imported analogous
moment calls. The vector and scalar outputs at one stage share a stream;
they both use the preceding stage's inputs, so neither depends on the
other's newly estimated value.

There are \(Q\le C(L+1)\) successive stages. Give stage \(\ell\)
one independent seed, sampled independently of the source and all the
other stage seeds. It is reused at every input, time and source prefix.

Round the external argument once before entering this recursion. A
concrete sphere encoding rounds the coordinates of \(v=x/\sqrt d\)
to a dyadic grid of mesh \(2^{-p}\), producing \(q\), and uses the
sphere representative \(q/\|q\|\). For \(\sqrt d\,2^{-p}\le1/4\),
\(q\ne0\) and

\[
 \left\|\frac q{\|q\|}-v\right\|
 \le |1-\|q\||+\|q-v\|\le2\sqrt d\,2^{-p}.             \tag{5}
\]

The representative is evaluated to the assigned working precision by a
scalar square root and division; this is an additional deterministic
numerical error. Round the compact within-patch time coordinate on the
same grid. Patch and prefix indices are discrete and included in the
external code. Include patch endpoints and the frozen terminal branch.
The actual physical query time chooses its patch as in the existing
source interface; requested-time access costs are not omitted.

Take

\[
 p=C R\Theta,\qquad
 F=\left\lceil C(d+1)R\Theta\right\rceil.                \tag{6}
\]

The finite set \(\mathcal A\) of external codes, including source
prefixes, has

\[
 \log|\mathcal A|\le C(d+1)p+C\log(P+2)\le F/C
                                                               \tag{7}
\]

after choosing the constant in \(F\) large enough to include stage,
coordinate and failure-budget counts. Only the current code is stored;
the grid is not enumerated.

Here is the needed continuity bridge for the exact reference. With
incoming moments fixed, changing the external input or patch coordinate
by \(u\) changes a row moment by at most
\(\exp(CR\chi)u\), using the supplied uniform row sensitivity and
integrating the row difference. The fixed histories are held fixed in
this comparison. The weak Gaussian moment inequalities propagate
incoming-moment differences with one-stage factor at most
\(\exp(C\chi)\): the feature caps, mean-mixer bounds, and first two
activation derivatives have their logarithms in \(\chi\). Thus the
exact moment discrepancy obeys
\(e_\ell\le\exp(C\chi)e_{\ell-1}+\exp(CR\chi)u\).
There are \(Q\le CR\) stages, so its total factor has logarithm at
most \(CR\chi\), after increasing the universal constant. Fresh scalar
Gaussian variables are integrated in the weak inequalities; no
uniform pointwise bound on an unbounded fresh Gaussian is presumed.
Equations (5)--(6) now make the reference prediction and moment errors
at most the allocated \(\varepsilon\) share. This uses continuity of
the exact maps, not continuity of the finite arithmetic or median program.

### Lemma 1: only reachable contexts need a probability union

Suppose that, for each fixed guarded context at stage \(\ell\), its
independent stage seed has failure probability at most \(p_0\), uniformly
over the context. Then the probability of any local estimation failure
at any code in \(\mathcal A\) and any stage is at most
\(Q|\mathcal A|p_0\).

**Proof.** Fix \(\ell\) and condition on the source and on seeds
\(1,\ldots,\ell-1\). For each \(a\in\mathcal A\), run the earlier
stages with those fixed seeds. They produce one definite guarded context
\(\theta_\ell(a)\). It is now independent of seed \(\ell\), even if
an earlier stage has failed. Apply the fixed-context guarantee at
\(\theta_\ell(a)\), and sum over \(a\). Integrating this conditional
bound and then summing over \(\ell\) gives the assertion. There is
no need to condition on earlier success events or enumerate their
possible numerical outputs. QED.

Each fixed-context test may hardwire \(\theta_\ell(a)\) and its
proof-only target. The block-generator guarantee is uniform over these
finite-state tests, so conditioning on earlier seeds does not change its
bound. One seed shared by successive dependent stages would not justify
this proof. Similarly, quantizing only intermediate contexts while
leaving the external input continuous would not establish (7): the
rounded program need not be continuous on an uncountable input graph.

## 3. One Gaussian exception per stream, not per context

Let \(N=Js\) be the number of rows in one stage stream. Generate the
same \(D\) Gaussian packet coordinates at every context for a given row
index. Pad an unused coordinate if necessary so this schedule has a
fixed length independent of branch decisions. This uses the common
packet interface already present in the row compiler.

The following finite construction makes the exceptional event observable.
For each coordinate take a \(b\)-bit uniform cell midpoint \(u\).
Choose a rational threshold \(a_T\) satisfying

\[
 \Phi(-T)+2^{-b}\le a_T\le\Phi(-T)+3\,2^{-b},             \tag{8}
\]

where \(\Phi\) is the standard normal distribution function. For an
explicit rule, put \(\Delta=2^{-b}\), obtain a certified upper endpoint
\(u_\Phi\in[\Phi(-T),\Phi(-T)+\Delta/2]\), and set
\(a_T=\Delta\lceil u_\Phi/\Delta\rceil+\Delta\).
Its excess above \(\Phi(-T)\) is between \(\Delta\) and
\(5\Delta/2\), as required by (8). Certified CDF evaluation to error
below \(\Delta/4\) supplies that endpoint. Define a tail flag if
\(u\le a_T\) or
\(u\ge1-a_T\). Use the clipped inverse CDF and prescribed rounding
to produce the finite Gaussian coordinate.

Couple the midpoint to an exact uniform random variable in its cell.
If the flag is absent, the entire cell lies inside
\([\Phi(-T),1-\Phi(-T)]\). The inverse derivative there is at most
\(\sqrt{2\pi}\,e^{T^2/2}\). Thus the finite Gaussian differs from
the exact coupled Gaussian by at most

\[
 \sqrt{2\pi}\,e^{T^2/2}2^{-b}+2^{-b'},                   \tag{9}
\]

where \(b'\) is the quantile-evaluation accuracy. Under true independent
finite bits, the probability that any coordinate in the stream is flagged
is at most

\[
                 CND\{e^{-T^2/2}+2^{-b}\}.               \tag{10}
\]

Take \(T^2=C\log(QND/\delta+2)\) and
\(b,b'\le C R\Theta\), with sufficiently large chosen constants.
Then (10) is at most \(\delta/(8Q)\), while (9), passed through the
uniform exact row sensitivity, contributes less than the local
\(\varepsilon\) allowance. All these choices are fixed before the
query; no Gaussian-tail stopping rule or rejection loop is used.

### Lemma 2: a common exception can be separated before fooling tests

Let \(E\) be the event that a stage stream contains a flagged coordinate,
and let \(B_a\) be one coordinate median's failure at a fixed context.
For each context use a one-pass test for \(B_a\cap E^c\), and also
use a single one-pass test for \(E\). If a generator fools each such
test to additive error \(\zeta\), then

\[
 \Pr_{\rm gen}\!\left(E\cup\bigcup_aB_a\right)
 \le\Pr_{\rm iid}(E)+\zeta
              +\sum_a\{\Pr_{\rm iid}(B_a\cap E^c)+\zeta\}.
                                                               \tag{11}
\]

This follows by a union bound after writing the bad union as
\(E\cup\bigcup_a(B_a\cap E^c)\). The \(E\) test stores one OR
flag and a counter. To test one side of a coordinate-median failure,
store the running scalar block sum, counters, the number of blocks
exceeding a fixed threshold, and the OR flag. Accept failure only if
the median threshold is exceeded and the final flag is false. This
adds one bit to the core's small one-pass median tester. Lower and upper
thresholds are handled by two tests; no output-median array is part of
their between-row state.

On \(E^c\), (9) couples the whole finite calculation to the exact
Gaussian baseline with the required deterministic error, uniformly in
the fixed context. Therefore \(\Pr_{\rm iid}(B_a\cap E^c)\) is
bounded by its exact Gaussian statistical failure, with the usual
separate threshold margins. The coupled ideal coordinates remain iid
without conditioning on \(E^c\); only the bad event is intersected
with \(E^c\). No claim of conditional Gaussian independence is needed.

Use this lemma conditionally on previous stage seeds, as in Lemma 1.
The event \(E\) is common to every context in that stage because the
packet schedule and stream are common. The cutoff in (10) therefore
needs \(\log(QND/\delta)\), rather than \(\log|\mathcal A|\).
Simply omitting the context factor from the old per-context coupling
argument would be invalid; (11) is the needed replacement.

## 4. Statistical blocks, precision, and error propagation

Write \(\bar h=\max(h,1/n)\). A directly verifiable finite choice of
\(s\) uses an upper dyadic certificate
\(\bar h\le\widehat h\le2\bar h\) and any integer

\[
                   1\le s\le\frac1{128\widehat h}.       \tag{12}
\]

Under \(\nu_j^{\otimes s}\), one coordinate block average of
\(UG\) has variance at most \(B^2/s\). Its error exceeds
\(4B/\sqrt s\) with probability at most \(1/16\) by Chebyshev.
The total variation distance between \(\nu_j^{\otimes s}\) and
\(\mu^{\otimes s}\) is at most
\(\sqrt{s h/2}\le1/16\). Hence the same bad-block probability under
the implemented prior is at most \(1/8\). For odd \(J\) independent
blocks, at least half must fail for a coordinate median to fail, giving

\[
 \Pr\!\left\{\|\widehat b-\mathbb E_{\nu_j}UG\|>
                         4B\sqrt{r/s}\right\}
                  \le r2^{-J/2}.                        \tag{13}
\]

The scalar second moment has corresponding error \(4B^2/\sqrt s\).
The distribution comparison is on a whole product block, not a claim
that pseudorandom rows are independent or that prior mark variances are
bounded. The generator transfers the finite tests after this iid proof.

Choose

\[
 J\le C F=C(d+1)R\Theta\quad\hbox{odd},\qquad
 w=C R\Theta,\qquad E_0=1+\lceil\log_2(N+2)\rceil.
                                                               \tag{14}
\]

Here and in other sufficient choices, a sufficiently large universal
constant is selected; the displayed upper bound does not allow taking
an arbitrarily small constant. Median tails in (13) can then be summed
over (7), stages, and coordinates with total probability below
\(\delta/8\). Allocate generator error at most
\(\delta/[C Q(R+1)|\mathcal A|]\) per context-side test and a
separate \(\delta/(8Q)\) to each tail test.

The common stream exception in Section 3 gives \(T^2\le C\Theta\),
since \(s\le n\), \(J\le C(d+1)R\Theta\), and dimension logarithms
are in \(\Theta\). Packet quantization, finite coefficient preparation,
incoming moment rounding, thresholds, and row accumulators all fit
\(w=C R\Theta\) bits. The context grid's entropy \(F\) does not
need to enter the Gaussian cutoff or row precision. It enters the block
count and the generator's required distinguishing error.

One generator block needs \(C D w\) random bits. The small failure
test has between-row state \(C(w+\log N)\). Therefore one may take

\[
 A=C(Dw+F+E_0)\le C R^2\Theta,\qquad
 E_0\le C\Theta.                                       \tag{15}
\]

The inequality uses \(d\le R\). There are \(Q\) independent seeds,
so total seed length is \(C Q R^2\Theta^2\). Every seed is stored
and counted; it is not regenerated from one shorter unproved seed.
Initial seed generation additionally consumes that many unbiased random
bits and bit writes. This one-time cost is part of initialization, with
the same retained storage; it is not a free randomness oracle at queries.

With conditional probability at least \(1-\delta\) after the allocated
shares, all local moment estimates succeed at every reachable external
code. The exact reference moment maps obey the weak propagation
inequalities in `RECALIBRATION_FREE_MOMENTS.md`, equation (27): they
are Lipschitz in the Gaussian variance because the scalar Gaussian is
integrated before the comparison. Their fixed-depth amplification sends
the local errors

\[
                 CB\sqrt{R/s}+\varepsilon,
                 \quad CB^2/\sqrt s+\varepsilon          \tag{16}
\]

to the corresponding final error. Projection guards do not increase
distance from feasible exact moments. They also keep the hypotheses
valid when earlier numerical calls have failed; their good-event
accuracy follows from the induction, not from assuming earlier success
when sampling a new stage.

For the original choice \(s=\lfloor1/(128\widehat h)\rfloor\),
assuming the inherited width gate makes this positive, (16) has the
same root-width logarithmic scale as the original decoder. The imported
posterior-to-center interval argument and dense-reference comparison
therefore apply unchanged, apart from the extra allocated
\(O(\varepsilon)\) external-rounding error. The event covers every
continuous sphere input by its external code, every source patch and
prefix, and the frozen endpoint. A later adaptively chosen query is
covered by this one event; fresh query randomness is not used.

If the desired local statistical tolerance is larger, (12)--(13) also
allow a smaller block. For example \(s\ge16rB^2/a^2\) suffices for
cross-moment tolerance \(a\), provided it still satisfies (12).
The relevant \(a\) must include the physical fixed-depth propagation
factor. The coarse bound \(s\le n\) is unnecessary for charging actual
queries; it is retained only as an upper estimate.

## 5. Resource derivation and what the lower exponents mean

Keep all \(J\) completed block means for the vector and scalar moment
medians of the current stage. Their total bits are

\[
                 C J R w\le C(d+1)R^3\Theta^2.           \tag{17}
\]

Current coefficient matrices cost \(C R^2w=C R^3\Theta\); current
row values, guards, output vectors, Gaussian scratch and generator
scratch fit below that and (17). Earlier stages retain their output
vectors and seeds, while the current stage's row scratch is reused.
Together with the metric acquisition base and all \(Q\) stored seeds,
this proves the first two rows of (1). Peak initialization is a separate
source/metric cost and has not been replaced by the query peak. The
selected-metric online acquisition uses the same coefficient/row scratch
of at most \(CR^3\Theta\), so the displayed post-initialization bound
also covers that training scratch. In contrast, the existing complete
initialization still has the explicitly charged term
\(CnR^2\Theta\) and exact-metric scratch \(CR^4\Theta\), in addition
to retained inputs and the new \(CQ R^2\Theta^2\) seeds. This note
does not claim absolute-polylogarithmic peak space during initialization.

There are \(QJs\le C Qs(d+1)R\Theta\) evaluated packets. Per packet,
the internal costs from Sections 1 and 4 are bounded by

\[
 C D w^4+C R^2w^2+C A^2E_0
 \le C(R^5\Theta^4+R^4\Theta^2+R^4\Theta^3)
 \le C R^5\Theta^4.                                    \tag{18}
\]

Preparation over all \(Q\) stages costs
\(C Q(R^7\Theta^2+R^7\Theta^3)\). Sorting the completed dyadic block
means costs at most \(C Q R J\log(J+2)w\), which is bounded by the
displayed query work for \(s\ge1\). This proves the final row of (1).

A safe separate activation/data work allowance is

\[
 C Q\{s(d+1)R^2\Theta+R^2\}
                         T_{\phi,\rm data}(C R\Theta).   \tag{19}
\]

The second term allows coefficient-literal preparation. Add one live
\(S_{\phi,\rm data}(C R\Theta)\), retained evaluator code and original
data, query/time acquisition at the stated precision, certificate costs,
and output writing. Label normalization and the representation of the
scale \(Y=\|y\|_2/\sqrt m\) retain exactly the additions in
`COST_CONTRACT.md`. Analyticity alone does not imply computability or a
uniform evaluator cost. If an implementation caches other objects, their
actual retained size is additional.

An intermediate work/space option computes output coordinates one at a
time. For one coordinate retain its \(J\) scalar block means, sort them
in place and save their median, then restart the same deterministic
stream for the next coordinate. Keep the prepared coefficients and the
stage's incoming context fixed during all these passes. In particular,
do not apply the cross-moment projection or update the incoming context
until the entire vector and its scalar second moment have been computed.
Each returned coordinate is then exactly the corresponding median of
the original common stream. Its one-pass failure tests and all preceding
probability bounds remain unchanged; no generator theorem for a
repeated-read machine is being used.

There are at most \(CR\) passes and only \(Jw\), rather than \(JRw\),
live block-mean bits. The resulting bound is

\[
 S_{\rm retained+peak}\le B_{\rm in}
        +C\{R^3\Theta+(d+1+Q)R^2\Theta^2\},             \tag{20a}
\]
\[
 W_{\rm query}\le
        C Q\{s(d+1)R^7\Theta^5+R^7\Theta^3\}.           \tag{20b}
\]

Coefficient preparation is reused; if it is recomputed per coordinate,
its actual extra factor must instead be included. Sorting costs
\(CQ R J\log(J+2)w\) bits of work across all coordinates, already
bounded by (20b), and does not need an additional mean array. Multiply
the stream-evaluation part of (19), but not its reused preparation part,
by \(CR\). Retained seeds are unchanged and current output coordinates
use only \(CRw\) bits. This option therefore saves the vector dimension
in median-array storage at only that dimension's work factor.

A further optional threshold-search median implementation rereads the same
deterministic streams \(O(Rw)\) times. The core's exact-median identity
still connects its output to the one-pass failure tests; no many-pass
generator theorem is asserted. It replaces (17) by the current coefficient
and output storage, yielding

\[
 S_{\rm retained+peak}\le B_{\rm in}
                       +C(R^3\Theta+Q R^2\Theta^2),       \tag{20}
\]

at the additional work factor \(C Rw=C R^2\Theta\) on stream work.
This is a work/space choice, not a free median primitive.

For comparison with the old explicit physical envelope, put
\(M=m+d+2\), \(G_\gamma=1+m/\gamma\), and use the already supplied

\[
 R\le C\beta^{301L}M G_\gamma^3Z^6,
 \qquad \Theta\le C\beta^{200L}G_\gamma Z^2.
\]

With \(s\le n\), (1) implies, after enlarging a universal activation
envelope,

\[
\begin{array}{c|c}
 \text{retained bits}&B_{\rm in}
                   +C\beta^{3000L}M^3G_\gamma^{11}Z^{20}\\
 \text{retained plus stored-median query peak}&B_{\rm in}
                   +C\beta^{3000L}M^4G_\gamma^{11}Z^{22}\\
 \text{query internal work}&
                   Cn\beta^{3000L}M^7G_\gamma^{24}Z^{48}.
\end{array}                                                \tag{21}
\]

The source-dependent seed term separately has \(Z^{16}\); the
acquisition base has \(Z^{20}\). In work, stream processing has
\(Z^{46}\) and preparation has \(Z^{48}\); both are kept in (1),
while (21) uses one coarse envelope without an eventual-width absorption.
For example the stream's activation exponent is
\(6\cdot301+5\cdot200+1=2807\), and preparation's is
\(7\cdot301+3\cdot200+1=2708\), both below 3000.

These are internally derived conditional bounds, not a revision to the
checked cost contract. Substituting only the \(Z^{5/2}\) field count
from `SANE_TAYLOR_SOURCE.md` would not establish its missing bit/compiler
interface. Even granting that interface with \(\Theta=O(Z^2)\), the
retained acquisition term would be \(Z^{19/2}\), the stored-median peak
\(Z^{23/2}\), and the seed \(Z^9\). This route alone does not produce
fourth- or fifth-power retained-plus-peak bit memory.

## 6. Conditional averaging and a constructive control-variate interface

Integrating the fresh scalar \(g_\ell\) in (4) replaces the random
row test by its conditional mean given the training packet. It reduces
variance, by the exact identity

\[
 \operatorname{Var}(X)=
 \operatorname{Var}(\mathbb E[X\mid Z])
                       +\mathbb E\operatorname{Var}(X\mid Z),
                                                               \tag{22}
\]

when \(X\) is scalar and square integrable. It does not bound the
remaining variance by a quantity tending to zero with width. For
independent standard Gaussians \(Z,g\), take the analytic bounded
nonlinear test \(X=\sin(aZ+\sqrt v\,g)\), with fixed \(a\ne0\)
and \(v>0\). Direct integration of the Gaussian characteristic
function gives

\[
 \mathbb E[X\mid Z]=e^{-v/2}\sin(aZ),\qquad
 \operatorname{Var}(\mathbb E[X\mid Z])
                   =\frac{e^{-v}}2(1-e^{-2a^2})>0.        \tag{23}
\]

For completeness, completing the square in the Gaussian integral, or
solving its integration-by-parts differential equation
\(f'(a)=-af(a), f(0)=1\), gives
\(\mathbb Ee^{iaZ}=e^{-a^2/2}\). Symmetry gives zero sine mean, and
\(\sin^2 u=(1-\cos2u)/2\) gives (23). This example disproves only
the claimed automatic variance decay from averaging the last Gaussian.
Its total expectation is zero and is known exactly, so it is not an
integration lower bound or a difficult neural instance.

### Lemma 3: prior-block control variates with posterior moments

Let \(X:\mathbb R^D\to\mathbb R^r\) be the row test and let
\(C_0:\mathbb R^D\to\mathbb R^r\) be a computable control. Suppose a
retained or directly computable vector \(m_0\) satisfies

\[
 \|m_0-\mathbb E_\nu C_0\|_2\le e_{\rm ctrl},\qquad
 \mathbb E_\nu[(X_i-C_{0,i})^2]\le v_i^2,
 \quad V^2=\sum_{i=1}^r v_i^2.                          \tag{24}
\]

Use independent prior blocks of size \(s\) with \(sD(\nu\Vert\mu)
\le1/128\), and estimate each residual mean by its coordinate median
of block means. Add \(m_0\). Then, with failure at most \(r2^{-J/2}\),

\[
             \|\widehat m-\mathbb E_\nu X\|_2
                        \le e_{\rm ctrl}+4V/\sqrt s.     \tag{25}
\]

**Proof.** Under \(\nu^{\otimes s}\), residual coordinate \(i\)
has block-mean variance at most \(v_i^2/s\). Chebyshev gives failure
at most \(1/16\) at threshold \(4v_i/\sqrt s\); a zero \(v_i\)
means that residual vanishes almost surely. Product total variation
adds at most \(1/16\), including the zero case. The same independent
block-median argument used for (13), followed by a Euclidean sum and
the deterministic error in \(m_0\), proves (25). QED.

To attain local tolerance \(a\) with \(s=\operatorname{polylog}(n)\),
it is sufficient to construct a control whose cost is polylogarithmic,
whose posterior expectation is known within \(a/2\), and for which

\[
                    V^2\le a^2s/64.                     \tag{26}
\]

The neural source can supply exact or noisy means for some controls:
linear combinations of its acquired pair tests use the corresponding
current scalar prefix. If the scalar errors are at most \(e\), a
control expectation with coefficient vector \(\alpha\) has error at
most \(e\|\alpha\|_1\). This coefficient norm must be counted; it
cannot be replaced by an unknown well-conditioned projection assumption.
Adding a constant uses its exact expectation one.

No input read here proves (26) uniformly over every unseen input and
all times at the required shrinking tolerance. An \(L^2\) residual
under the prior alone is also insufficient for (24), which concerns
\(\nu\). Low relative entropy does not bound an unbounded residual's
posterior second moment by its prior second moment. Direct quadrature
would instead need a proved small effective integration dimension,
usable mixed regularity, or a separate low-complexity moment identity.
The growing packet dimension \(D=O(R)\) prevents silently charging a
tensor quadrature as an absolute polylogarithm. These are specific open
neural bridges; none is established here merely by invoking strip
analyticity.

## 7. Exactly restricted sampling lower bound

The following lower bound concerns an iid **moment-value oracle**. It
returns scalar values \(X_1,\ldots,X_N\) and reveals neither their
Gaussian packets nor a symbolic/evaluable description of the row test.
An estimator may use arbitrary computation and independent randomness
on those returned values. The actual neural decoder has more access;
the proposition is explicitly not a lower bound for that decoder class.

### Proposition 4: root-accuracy needs inverse-square samples in this oracle

Let \(0<a\le1/4\). Under the fixed standard Gaussian packet law,
consider the two analytic row tests

\[
           U_\pm(z)=\pm2a+z/2,\qquad G(z)=1,
           \qquad X_\pm=U_\pm(Z),\quad Z\sim N(0,1).     \tag{27}
\]

Take \(\nu=\mu\), so the relative entropy is zero and
\(\mathbb E_\nu U_\pm^2=1/4+4a^2\le1/2\le1\). Thus these
are within the scalar weak-moment hypotheses (2), including analytic
unbounded marks. Any moment-value estimator which estimates each mean
within \(a\) with probability at least \(3/4\) must use

\[
                           N\ge\frac1{64a^2}.            \tag{28}
\]

**Proof.** The two output laws are Gaussian with means \(\pm2a\)
and variance \(1/4\). Their one-sample relative entropy is \(32a^2\),
obtained by integrating the logarithm of the ratio of their Gaussian
densities; products multiply it by \(N\). The total variation
inequality \(\|P-Q\|_{\rm TV}\le\sqrt{D(P\Vert Q)/2}\) therefore
bounds the product-law distance by \(4a\sqrt N\). One direct proof
of this inequality reduces relative entropy to the event attaining
total variation; the binary relative entropy as a function of its
first probability has second derivative \(1/[p(1-p)]\ge4\), value
and derivative zero at the second probability, and is at least twice
the squared difference. The reduction is the log-sum inequality.

Thresholding the estimator at zero distinguishes the two means with
error at most \(1/4\) under either law, because their accuracy
intervals \([a,3a]\) and \([-3a,-a]\) have opposite signs.
Every possibly randomized test has sum of its two errors at least
\(1-\|P-Q\|_{\rm TV}\): integrate its acceptance probability,
which lies in \([0,1]\), against the signed difference of the laws.
Consequently total variation must be at least \(1/2\), giving (28).
Independent estimator randomness leaves total variation unchanged. QED.

At \(a=n^{-1/2}\), this is \(N\ge n/64\). At
\(a=(\log n)^k/\sqrt n\) it gives only
\(N\ge n/[64(\log n)^{2k}]\), not a literal universal \(\Omega(n)\)
statement at every looser dense certificate. The entropy cap can be
reported as \(\bar h\ge1/n\) even when the actual entropy is zero;
that convention does not invalidate the example.

Its limited access is essential: if both the packet \(z\) and its
value in (27) are revealed, a single subtraction gives the unknown mean.
If the test formula is supplied, no samples are needed. Consequently
this proposition rules out a universal polylogarithmic-sample claim
based solely on the returned iid moment values and second moments.
It does not rule out exploiting neural circuit formulas, exact Gaussian
integration, retained training moments, or controls satisfying (24)--(26).

## 8. Claim status and remaining bridge

| Claim | Status in this note | Exact dependency or limitation |
|---|---|---|
| Reachable-context union with external rounding and independent stage seeds | Author proof, Lemma 1 | Fixed finite external codes and independence of successive stage seeds |
| One Gaussian tail exception per stage | Author construction and proof, Lemma 2 | Same padded packet schedule for all contexts; test bad medians only outside the shared tail flag |
| Bounds (1), (19)--(21) | Derived conditional bit/work counts | Imported causal sensitivity, matrix/row costs, block generator and selected metric |
| Same simultaneous neural accuracy | Conditional assembly | Existing source/physical/center events and weak moment propagation; no new effective width threshold |
| Polylogarithmic query work | Open | Need a cheap computable moment mechanism or posterior-valid small-residual control; the present \(s\) remains large |
| Automatic variance decay after averaging the last Gaussian | False in the stated generality | Explicit positive residual variance (23), without implying integration hardness |
| Inverse-square iid sample necessity | Proved only for the stated value-oracle class | Proposition 4 hides packets and test formulas, unlike the neural decoder |
| Fourth- or fifth-power full bit memory | Open | Source field count, scalar precision, retained metric, and query workspace still exceed those powers |

The constructive changes preserve one repeatable decoder function on the
entire input/time domain, all stored random bits, peak workspace, and the
absence of training-history replay. Their principal adverse finding is
specific: neither smaller probability nets nor scalar conditional
averaging supplies the small posterior residual required to remove the
sample factor. A theorem providing that residual, with a counted
control expectation and evaluation algorithm, would resolve a real
remaining query bottleneck. The broad neural possibility remains open.

The complete scientific inputs read were the seven explicitly assigned
notes: `SANE_DECODER_CORE.md`, `SANE_METRIC_PACKETS.md`,
`SHORT_SEED_PRIOR_BLOCKS.md`, `RECALIBRATION_FREE_MOMENTS.md`,
`DENSE_BUDGET_SELF_NORMALIZED.md`, `SANE_TAYLOR_SOURCE.md`, and
`COST_CONTRACT.md`, together with `docs/notation.qmd`. Links to other
studies and unassigned companion files were not followed. The rigorous
proof and conjecture skills, their relevant contract/evidence/audit
references, and the canonical-notation skill with its neural reference
were read and applied. Only this assigned note was written.
