# Smaller Taylor-source composition: candidate resource theorem

2026-10-06. Lead-author assembly, not an independent review or promotion.
This is a candidate composition of separately stated interfaces. It does
not prove logarithmic unseen-query work. The statistical sampler still
uses a number of rows proportional to width, up to logarithmic factors.

## 1. Preserved contract and notation

Keep the complete model, label intersection, input interface, and accuracy
contract in `COST_CONTRACT.md`: dense width n; m spanning sphere inputs in
dimension d, m >= d; fixed depth L >= 2; positive feature-Gram gap gamma;
label RMS Y; confidence 1-delta; and the explicit strip-analytic activation
envelope beta. Hidden layers learn nonlinearly. Zero labels have the separate
zero-predictor branch. The reference is an independent dense run, not a
specified realization. The error covers the entire sphere, physical
training trajectory, and fitted endpoint. Queries use the current prefix,
not training replay. Retained randomness, fixed arrays and peak memory count.

Use the existing logarithmic factor

\[
 Z=\log(en)+\log\!\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\]

All constants below are universal. Set the auxiliary deterministic accuracy
to n^(-10), as in the cost contract. The only two additional symbols are
internal size certificates: R bounds the number of named source fields and
matrix actions, and Theta bounds local numerical logarithms and required
external-accuracy logarithms. Sufficient envelopes proposed here are

\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)^2Z^{5/2},
 \qquad
 \Theta\le C\beta^{102L}(1+m/\gamma)Z.                 \tag{1}
\]

Choose the actual R and Theta by the constructive recipes, not arbitrarily
large numbers merely satisfying lower bounds. R can be enlarged by a
universal factor so Theta <= R and so m,d,L and all local Taylor orders
are included. These inequalities follow from the displayed envelopes and
the source lower bound m/gamma >= beta^(-6L), without a new label cap.

## 2. Scientific dependencies and the required composition

The source candidate is `FAST_TAYLOR_NOISE.md`, frozen at SHA-256
`71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c`.
Its Sections 1--7 give a predictable, noisy two-orientation Taylor program,
normalized physical prediction error below n^(-10), and local noise/value
precision O(beta^(100L)(1+m/gamma)Z). Section 8 gives centered causal
coefficient caps, a local logarithmic Lipschitz certificate of this same
order, and at most CR^2 scalar arithmetic per row. This source is currently
under separate reconstruction; its status is not upgraded by this assembly.

The unchanged downstream ingredients are the causal-depth and matrix/row
compiler in `SANE_DECODER_CORE.md`; pair-table acquisition in
`SANE_METRIC_PACKETS.md`; and the posterior-moment, passive-geometry and
dense-center interfaces used by those notes. `FAST_UNIFORM_QUERY.md`
supplies the smaller independent-stage seeds and reachable-context union.
Its coordinate-at-a-time median implementation is spelled out below so its
space/work tradeoff is part of the actual algorithm.

The main interfaces to verify, rather than merely substitute, are:

1. Taylor coefficients and real activation samples are named row fields.
   All acquired averages are pairs of such fields; scalar rank weights
   are deterministic functions of acquired pairs. There are CR fields and
   CR^2 pairs, not one new field per scalar arithmetic operation.
2. A new coefficient is formed from previously named coefficient fields
   and its current scalar arguments. There are CR causal phases. Centered
   series composition is a local operation with the Section 8 bound, not
   an uncentered power of a square-root-n coordinate cap. Thus the core's
   whole-graph bound is exp(C R Theta), not exp(C Theta).
3. The common-Gram ridge and passive-query numerical protections must be
   included in Theta, in addition to the Taylor local certificate. The
   construction of `COMPILER_PARAMETER_ACCOUNTING.md`, Section 8.2, uses
   log X <= C beta^(100L)(1+m/gamma)Z after the new matrix-noise choice.
   Its ridge exponent is O(L), so its additional numerical logarithms fit
   the second envelope (1). Large normalized physical caps enter log X,
   not an undisclosed constant. This is a numerical precision bound only;
   the statistical error still uses the smaller physical constants.
4. A passive query reads the current parameter polynomial/rank list. It
   appends only a fixed-depth forward calculation. The Taylor source's
   physical parameter error, mixed-orientation Gaussian law, and operator
   caps must supply the same passive-query interface as the old source.
   One must not expose future training innovations or private selected
   packets as conditioning data.

These checks identify the specific assembly obligations. Section 7 below
supplies a passive-interface transport argument and keeps the physical and
normalized oracle tapes distinct. The new local
kernel idea in `FAST_LOCAL_KERNEL_AUDIT.md` is NOT a dependency. In
particular we retain the conservative R Theta scalar/packet precision.

## 3. Conditional counted algorithm

Assume the four interfaces above have been verified. A sufficient working
precision is C R Theta bits, including integer ranges. The metric scheme
stores O(R^2) words: selected root packets, metric entries, scalar-noise
marks, currently acquired summaries and coefficient/template arrays.
This costs CR^3 Theta bits. Its exact construction works on the finite
dyadic source table and rounds the metric with its explicit bilinear error
budget; it never inverts the retained metric.

Independent seeds for the O(L+1) passive stages require
C(L+1)R^2 Theta^2 bits. The external sphere/time grid is not enumerated or
stored. The uniform-query argument conditions on the preceding stage seeds
and applies a fixed-context guarantee only to the context reached at each
external code. Its common Gaussian-tail test is charged once per stream.

For a small-memory query, compute the coordinate medians successively.
For one coordinate retain its J block means, with
J <= C(d+1)R Theta, each of C R Theta bits. Reuse the identical retained
seed for the other coordinates, rerunning the row stream. At most CR
coordinates are required. This computes exactly the same vector of medians
as the simultaneous implementation; the probability proof is unchanged.
It costs an additional factor CR in stream work, but only
C(d+1)R^2 Theta^2 live median bits, not C(d+1)R^3 Theta^2.

The statistical block length is still the explicit choice

\[
 s=\left\lfloor\frac{n}{128\widehat K}\right\rfloor,
 \quad
 K_+=\max\left\{1,
 \frac{P}{2\alpha}\log(1+B_F^2/\eta^2)\right\},
 \quad K_+\le\widehat K\le2K_+ .                       \tag{2}
\]

The symbols in (2) are local to this paragraph: P <= CR^2 is the actual
scalar-summary count; alpha is its allocated failure share; B_F the
specified scalar-integrand cap; eta the chosen scalar noise; and widehat K
is a certified dyadic upper approximation. The sufficient width gate
n >= 512 K_+ is retained. In particular s <= n; it is not replaced by a
logarithmic sample count. Equation (2) is the existing posterior/prior-block
algorithm, not a new sampler.

The resulting conditional internal costs are

| Resource | Bound |
|---|---:|
| Retained bits | C[R^3 Theta+(L+1)R^2 Theta^2] |
| Peak training/query bits, including model | C[R^3 Theta+(d+L+2)R^2 Theta^2] |
| Initialization work | C n R^8 Theta^3 |
| Peak initialization bits | C[nR^2 Theta+R^4 Theta+(L+1)R^2 Theta^2] |
| All scheduled training updates | C R^7 Theta^3 |
| One query, coordinate-at-a-time medians | C(L+1)[s(d+1)R^7 Theta^5+R^7 Theta^3] |

The initialization bound also covers the source-generation term
C(nR^5+R^6)Theta^4: since Theta <= R and R,n >= 1, this is at most
C(nR^6+R^7)Theta^3 <= 2C nR^8 Theta^3. No extra width gate is
needed for this simplification. Coefficient preparation is performed
once per passive stage and reused for every coordinate. Sorting one
coordinate's J means is included in stream work. Training here means all
scheduled finite acquisition updates, not an unspecified ODE step count.

## 4. Explicit major-parameter envelope

Substitution of (1), s <= n, and L+1 <= C beta^L yields the following
coarse universal envelopes. They are implications of the conditional
algorithm above, not independently proved full-decoder bounds.

| Resource | Conditional internal bound |
|---|---:|
| Retained model and peak training/query bits | C beta^(710L)(m+d+2)^3(1+m/gamma)^7 Z^(17/2) |
| Initialization work | C n beta^(1920L)(m+d+2)^8(1+m/gamma)^19 Z^23 |
| Peak initialization bits | C beta^(910L)[n(m+d+2)^2(1+m/gamma)^5 Z^6+(m+d+2)^4(1+m/gamma)^9 Z^11] |
| All scheduled training updates | C beta^(1720L)(m+d+2)^7(1+m/gamma)^17 Z^(41/2) |
| One unseen query | C n beta^(1920L)(m+d+2)^8(1+m/gamma)^19 Z^(45/2) |

For example R^3 Theta has powers Z^(17/2) and
(1+m/gamma)^7, while the coordinatewise stream term is
(L+1)s(d+1)R^7 Theta^5, with Z^(45/2) and gap-ratio power 19.
The retained seed and one-coordinate median terms have Z^7 and are covered
by the first row without shifting a parameter factor into the width threshold.
Round the logarithmic exponents upward to 9,23,11,21,23 only if an integer
presentation is desired. The displayed fractions are the actual algebraic
envelopes. These bounds do not have fourth-degree time dependence in the
sample count or gap ratio.

## 5. Costs and qualifications not absorbed into C

Add retained original data/evaluator/certificate descriptions and one live
activation/data-evaluator workspace. The common sufficient value and input
precision is C R Theta; a safe total number of supplied evaluator calls is
C nR^3 for initialization, CR^4 for all updates, and
C(L+1)[s(d+1)R^3 Theta+R^2] for a coordinatewise-median query.
Multiply these counts by the actual supplied evaluator work at that precision
and argument range. This includes the real activation samples for Taylor
jets; analyticity is not a unit-cost bit evaluator.

Charge data and certificate acquisition, normalization of y/Y, retained
output-scale encoding, query/time acquisition, and output writing exactly
as in `COST_CONTRACT.md`. The major-parameter bounds are not a substitute
for encoding-length costs. The normalized algorithm does not pay an
unreported power of 1/Y, but raw-label precision and output scale can depend
on log(1/Y) and remain explicit input/output costs.

Choose integer orders and precision levels by certified upper enclosures,
not by undecidable equality tests at a real integer boundary. A dyadic
lower patch-resolution scale obtained from an upper enclosure of T may
be smaller by a factor at most four. This only enlarges numerical slack
and universal factors. At an external time within the input-rounding
allowance of a patch boundary, either adjacent certified patch is allowed:
both approximate the same continuous physical trajectory there.

Keep the complete inherited label intersection; all source/fitting events;
their unquantified sufficiently-large-individual-width threshold; the
deterministic Taylor gates, including nY >= 1 on the nonzero branch; and
the sampling gate in (2). The statistical remainder must still fit the
original dense-pair upper certificate, not merely have an unspecified
n^(-1/2+o(1)) rate. The tail and physical approximation are inherited
accuracy obligations, not storage constants.

## 6. Status

The exponent arithmetic and the coordinatewise median schedule are lead
derivations. Source/guard composition and the revised query proof require
their assigned independent checks before this candidate replaces any
headline theorem. Even if all these checks pass, the result has width-order
query sampling and finite-bit logarithmic power 17/2, not the user's
requested logarithmic-query, fourth/fifth-power complete representation.
That remaining gap must not be concealed by calling the source field count
or its real-coordinate square the full model size.

## 7. Transport to the passive-query statistical interface

This appendix uses the complete `DENSE_BUDGET_GEOMETRY.md`,
`SOURCE_SUPREMUM_EXTENSION.md`, and the explicitly authorized integrated
`UNBOUNDED_COMPRESSOR_BRIDGE.md`. Their mechanisms concern any finite
predictable Gaussian transcript, rather than the old collocation rule.
The statements below explain their application to the Taylor transcript;
they remain subject to the separate assembly reconstruction.

### 7.1 Keep one physical oracle tape

Use the physical backward queries and physical answer noise in
`FAST_TAYLOR_NOISE.md`. Do not identify that tape with the different tape
obtained by noising label-normalized backward queries at the same nominal
noise level. The two-orientation posterior is always computed from the
physical query and answer fields of this one tape.

Normalized readout and response fields can be formed afterwards by dividing
their observed physical fields by Y. They are additional coordinatewise
fields, not new matrix calls or new observations about an initialized
matrix. Their normalized pairs remain pair reductions. On the inherited
nonzero-width branch nY >= 1, normalization increases amplitude and local
Lipschitz caps by at most n. It therefore adds O(log(en)) to the numerical
certificate, already within (1). Integer ranges, datum y/Y access, and
the output scale are charged as in Section 5. This uses an existing width
gate explicitly; it does not impose a new label cap or hide a power of 1/Y
in a purported universal constant.

### 7.2 Small caps for actual passive features

Use the existing real, whole-sphere response event, not the complex radius
proved only for a finite training panel. In this paragraph only, put
S=16Ym/gamma <= 1 and let rho be the training residual RMS. The integrated
bridge, (25)--(26), bounds every residual-free preactivation response by
U S sqrt(log(en)); residual decay gives integral rho <= S/4. The actual
physical velocity is minus twice the label-average of residual times
response. Cauchy--Schwarz in that finite average therefore gives

\[
 \sup_{t,x,i,j}|z_i^{(j)}(t,x)-z_i^{(j)}(0,x)|
 \le 2US\sqrt{\log(en)}\int_0^\infty\rho(t)\,dt
 \le \tfrac12 US^2\sqrt{\log(en)}.
\]

This U has a full-label explicit bound. The whole-sphere response
recurrence is the finite-panel recurrence with 64 replaced by
G_d=16 sqrt(d+3). All its terms are nonnegative, so the finite-panel bound
U_fin <= beta^(72L) in `PHYSICAL_PARAMETER_ACCOUNTING.md`, (9)--(10),
implies

\[
 U\le\max\{1,G_d/64\}U_{\rm fin}
   \le\beta^{72L}\sqrt{d+3}.
\]

This argument uses S <= 1, not the optional stronger label cap used for
some sharper source constants. It neither shrinks the activation strip
nor changes the inherited label allowance. No complex-time radius or
fixed-problem constant is hidden in this real passive-feature estimate.

At initialization a sphere net of mesh n^(-2), Gaussian tails conditional
on preceding layers, and the initialized RMS/operator bounds give a
coordinate cap C beta^(3L) sqrt((d+1)Z). Its net has at most
(Cn^2)^d points; the logarithm, not its cardinality, enters the tail
threshold. Whole-vector input Lipschitz bounds extend it to the sphere.
Allocate an explicit fixed fraction of delta to this initial event.
Consequently a safe passive activation/preactivation cap is

\[
 C\beta^{110L}\sqrt{d+1}\,Z^{3/2}.                    \tag{3}
\]

The true initial/time source events, including their sufficiently-large
width qualification, are the same kinds of events used by the inherited
construction. The bound is on actual query fields, not all intermediate
Taylor coefficient fields.

The Taylor state polynomial approximates physical parameters uniformly in
normalized block norm to n^(-10). Forward subtraction converts this to
per-coordinate query error at most C beta^(4L) Y sqrt(n) n^(-10), by
the source forward recurrence. Its harmless
upper envelope fits a fixed enlargement of (3), using Y <= beta^(3L).
For a fresh passive matrix action take the same physical noise scale,
or reduce its dyadic value by C[log(en)+L log beta] additional bits so
the propagated normalized passive error is below n^(-10). This preserves
the bounds (1); different known positive training/query noise levels have
the same posterior formulas, with their stated minimum floor. On the
event each fresh raw noise has RMS at most two, the deterministic
comparison holds uniformly in the query. The failure is at most
CL exp(-cn) conditional on each complete good training tape.

Compose activations with the smooth value cap of
`DENSE_BUDGET_GEOMETRY.md`, Section 7, at twice (3). It is the identity
on these completed passive queries. Its first two derivative bounds are
polynomial in beta, with no new n-power. History coefficients and Gaussian
innovations continue to use their larger numerical caps. This constructs
the small passive test bound; the loose numerical X^100 bound is not used
as a statistical substitute.

### 7.3 Conditional mean mixers on the new transcript

Let F_j be the observable filtration of the physical Taylor calls,
including deterministic external initial fields but not raw answer noises
or private selected packets. Gaussian conditioning is valid by the source's
predictability proof. For one initialized hidden matrix W, the process

\[
                  \mathbb E[\|W\|_{\rm op}^2\mid F_j]
\]

is a nonnegative martingale with initial expectation at most a universal
constant. To see the latter directly, two quarter-nets of the unit sphere
have at most 9^n points each; their Gaussian bilinear tails give
Pr{||W||_op>t} <= 2 exp(Cn-cnt^2), and integrating above a sufficiently
large numerical t gives the stated second-moment bound.

The first-crossing inequality, with failure delta/[C(L+1)] per matrix,
therefore bounds all these martingales at every prefix by C(L+1)/delta.
Conditional Jensen yields

\[
 \|\mathbb E[W\mid F_j]\|_{\rm op}
          \le \sqrt{C(L+1)/\delta}                     \tag{4}
\]

on the resulting single observable-prefix event. No conditioning on a
small realized matrix norm is inserted into the Gaussian likelihood.

At a completed current Taylor state the learned displacement is F_j
measurable and a finite sum of the stored rank factors. Its operator norm
is bounded by the true displacement plus its proved parameter error.
Impose the existing norm guard, with fixed slack, so it remains bounded
on all numerical branches and is unchanged on the physical good event.
Adding this displacement to (4) gives the required conditional mean-mixer
bound. It holds for the new transcript because the martingale argument
is independent of its integrator and number of observations.

### 7.4 Query normal form and probability transfer

The learned Taylor matrix is a sum of outer products of named coefficient
fields, with scalar integrated weights; it is not an additional dense
stored object. Concatenating those fields with the posterior-mean history
fields gives precisely the finite input/output factorization used in
`DENSE_BUDGET_GEOMETRY.md`, Section 9. The rank of the posterior covariance
correction is at most R. Its removal costs normalized mean-square error
at most C R/n per layer, before the explicit feature/readout and
fixed-depth propagation factors. Each passive layer uses its initialized
matrix once, so the required conditional independence from the next
centered matrix is preserved.

Equations (3)--(4), the proved displacement/readout bounds, and the existing
common-Gram repair therefore supply the passive weak-moment recursion.
Scalar-summary noise and finite arithmetic are still chosen using the
conservative exp(C R Theta) causal comparison. Their coupling is not
replaced by an assertion that noisy Grams are exact posterior Grams.

Finally use the same all-prefix information/noise bounds and posterior
center argument as `RECALIBRATION_FREE_MOMENTS.md`. The complete physical
good event and the dense center are independent of the choice of causal
integrator. The new physical approximation error is negligible and the
new scalar-summary law has the same exchangeable noisy-average form.
For fixed admissible data and confidence, all residual statistical factors
are polynomial in log(en), with degree possibly depending on fixed L in
the error estimate. The precise comparison with the inherited dense-pair
upper certificate remains its original explicit eventual-width inequality;
it is not inferred merely from the notation n^(-1/2+o(1)). The source and
sampling width gates remain visible in Section 5 and (2).

This transports the required scientific interfaces without changing the
network, labels, input domain or queried information. It does not remove
the n-scale statistical block length, improve the original stochastic
width threshold, or furnish a uniformly inexpensive Gaussian moment formula.
