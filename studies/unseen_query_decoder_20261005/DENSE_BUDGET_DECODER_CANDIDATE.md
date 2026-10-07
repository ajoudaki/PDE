# Dense-forward-time decoding: complete assembly

2026-10-06. Author assembly under the inherited dense/source certificates.
Two complementary isolated internal checks reconstructed the probabilistic
bridge and the numerical construction. Their required parameterwise
finite-precision repair is incorporated below. This is not promotion into
the maintained book, and neither scoped check alone certifies the theorem.

## 1. Target and notation

Keep the original width-\(n\), depth-\(L\) dense network and its mean-loss
gradient flow, Gaussian initialization, zero readout, block mobilities
\((n,1,\ldots,1,n)\), fixed spanning sphere data with \(m\ge d\), original
small-label allowance, and positive initial unweighted feature-Gram gap.
Activations have the original strip analyticity and bounded-derivative
assumptions; their values need not be bounded. All constants below may
depend on the fixed admissible problem and confidence, not on \(n\).

Write \(b_n\) for the existing dense-pair upper certificate at a suitably
smaller fixed failure probability, as displayed in `RESULT.md`. The
intended conclusion is

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_C(t,x)-f_n(t,x)|
 \le 2b_n+\frac{C[\log(en)]^{C_L}}{\sqrt n}.                 \tag{1}
\]

Here \(C_L\) denotes a finite exponent allowed to depend on the fixed
depth and source constants. It is an **error exponent**, not the storage
exponent. For fixed nonzero labels, the second term is eventually at
most \(b_n\), because that certificate contains the positive factor
\(\exp(CY^2\sqrt{\log(en)})\), where \(Y=\|y\|_2/\sqrt m>0\).
Thus (1) is the same dense-upper-bound scale. It does not preserve the
literal old remainder \(1/n\) in \(2b_n+1/n\). Zero labels are handled
by the identically zero predictor.

The intended costs are an absolute power of \(\log(en)\) for retained
state and peak live query workspace, and
\(n^{3/2}\) times an absolute power of \(\log(en)\) for query work.
The latter is eventually \(O(Ln^2+dn)\). The numerical values of those
absolute powers are not extracted here; no exponent-five claim is made.
Query work counts the same activation primitives as a dense forward pass.
A bit-time assertion additionally needs polynomial-time precision access
to those primitives, not merely the inherited polynomial-space access.

Preprocessing and the autonomous training-summary updates may be expensive.
No query input or query label is supplied there. Decoding reads only the
present summaries and their compiled coefficients. It neither replays the
scalar training dynamics nor accesses discarded dense parameters.

## 2. Finite source and additional moment bookkeeping

`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`, with its checked short physical solver,
supplies a finite causal matrix program through \(T=C\log(en)\), followed
by a frozen output tail. It has \(R\le C\log^8(en)\) named row fields
and initialized-matrix calls; all training matrix arguments and answers
have fixed RMS bounds on its good event. Completed source states and their
passive predictions approximate the physical dense trajectory to \(n^{-a}\)
for any prescribed fixed \(a\), at sufficiently large individual width.
The passive approximation is uniform in input and time, with a fresh-query
failure bound conditional on each good complete training tape.

Use the source's matrix-answer noise
\(\sigma=\exp(-\log^2(en))\). Its exact two-orientation Gaussian
representation uses independent row packets with Gaussian prior \(\mu\).
All conditioning inverses have the specified noise floor, not an empirical
history-Gram gap. The finite row circuit, its caps, and the logarithms of
its amplitude and Lipschitz bounds are absolute-polylogarithmic.

Include the raw pairwise moments of **all** named physical history fields
used as input/output factors of a learned displacement or conditional
matrix mean. Acquire each pair once, after its later field is created.
Fields already created retain their defining older scalar arguments; new
moment observations do not redefine them. This uses at most \(CR^2\)
scalar averages, not one new full Gram table per time step. Extra such
moments are deterministic functions of an observable matrix transcript
before scalar smoothing, and do not change its Gaussian posterior law.

As in the source, perturb every acquired scalar average by \(\eta E_r\),
with independent standard Gaussian \(E_r\). At a retained prefix \(c\),
write the bounded row tests collectively as \(F(z;c)\), so

\[
 c_r=\frac1n\sum_iF_r(Z_i;c_{<r})+\eta E_r.                 \tag{2}
\]

Here \(F\) includes the added pair products, and the older arguments in
each coordinate are fixed by the prefix. Positive weighted selection and
the existing finite-precision acquisition lemma apply to this enlarged
finite list. Its size is still \(O(R^2)\), so the absolute-polylogarithmic
state class is unchanged. Select \(\eta\) only after the matrix-noise
floor, finite-circuit sensitivity, and the extra tolerances below have been
fixed. Its logarithmic inverse remains absolute-polylogarithmic.

The posterior of the row array given the ideal prefix is denoted by
\(\pi_c\). Information and posterior-noise maximal inequalities in
`EFFICIENT_QUERY_INFORMATION.md` and
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md` give one high-probability event
for every acquired prefix. On it the full-array relative entropy is
absolute-polylogarithmic, its one-row marginal has entropy at most
\(h=C\operatorname{polylog}(n)/n\) from \(\mu\), and its expected
squared scalar-noise norm is absolute-polylogarithmic. Markov's inequality
therefore gives a posterior event of any specified fixed high probability
on which all actual pair moments differ from (2) by at most
\(\eta\operatorname{polylog}(n)\).

The current numerical prefix is used by the algorithm. Choose its error so
small that the uniform change of every bounded row test and every target
moment is much smaller than the slack \(\eta\operatorname{polylog}(n)\).
The logarithms of the source Lipschitz bounds are polynomially bounded,
so this costs only absolute-polylogarithmic precision. The proof still
conditions on the ideal nested prefixes. For each fixed ideal prefix,
the argument below applies to **every** numerical prefix in its certified
error ball, with the same deterministic error radius and proof center.
It does not assume that the actual numerical prefix is a function only
of the ideal prefix: it may also depend on private selected packets.
One fixes an arbitrary point of the ball during the posterior comparison,
obtains a deterministic conclusion for all such points, and only then
substitutes the actual acquired value. No union over numerical prefixes
or conditioning on the private packets is taken.

## 3. Current-state calibrated law and its finite compilation

At each prefix choose a minimum-entropy law \(\nu\) whose row moments
match the rounded retained moments within a constant multiple of the
noise tolerance. The posterior row marginal is a strictly feasible witness
after enlarging that tolerance. The supplied convex-dual argument gives

\[
 \frac{d\nu}{d\mu}(z)=
 \exp\{\lambda^TF(z;c)-\psi\},\qquad
 D(\nu\Vert\mu)\le Ch,\qquad
 \|\lambda\|_1\le\frac{Ch}{\eta\operatorname{polylog}(n)}. \tag{3}
\]

The denominator in the last expression is the positive feasibility slack;
it is fixed explicitly by the noise bound, not an unspecified vanishing
quantity. Its logarithmic inverse is absolute-polylogarithmic. Approximate
feasibility and a constant multiple of \(h\) are sufficient below.

`DENSE_BUDGET_TILT_COMPILATION.md` provides the counted finite
compiler: search a bounded rational multiplier grid, certify moment
feasibility and entropy by streaming Gaussian quadrature in the log domain,
and cache a successful multiplier, its log normalizer, and the raw history
Grams to the assigned precision. The search is finite even on bad states;
if no candidate passes, use a fixed guarded default. Its running time is
not a query cost, but its live workspace and retained coefficients must be
absolute-polylogarithmic. In particular, a normalizer oracle is not an
allowed substitute for this compiler. Its complete numerical reconstruction
is in `DENSE_BUDGET_NUMERICAL_CHECK.md`.

This calibration is from the **current** prefix. It can be performed in
the autonomous summary update after that prefix is acquired. Evaluating a
past row-response circuit at one Gaussian argument subsequently does not
recompute the scalar training evolution. No test-dependent compiler or
future prediction table is retained.

Small full-array entropy relative to the calibrated product law is crucial.
The exact change-of-reference identity is

\[
 D(\pi_c\Vert\nu^{\otimes n})
 =D(\pi_c\Vert\mu^{\otimes n})-nD(\nu\Vert\mu)
 -n\lambda^T\left(\pi_c^1F-\nu F\right).                 \tag{4}
\]

Both moment errors are at most a fixed multiple of the feasibility slack.
The multiplier bound in (3) consequently makes (4) at most
\(C\operatorname{polylog}(n)\). More explicitly, denote the positive
moment slack locally by \(s\). The finite compiler returns multiplier
norm at most \(2(1+h/s)\), posterior moment error at most \(2s\),
and compiled moment error below \(7s/2\). Thus (4) is at most
\(D(\pi_c\Vert\mu^{\otimes n})+11n(h+s)\).
Our subsequently chosen tiny scalar noise has \(s\le h\) eventually,
so this is at most the original array entropy plus \(22nh\).
The compiler's additive one in its norm bound is therefore accounted for.
Numerical-prefix error is included in these moment tolerances. The same
posterior marginal is a feasible witness for every prefix in the error
ball, so the conclusion is parameterwise uniform there; no continuity of
the optimizing multiplier is assumed. This statement does not say that
the collective posterior equals an iid product law.

## 4. Geometry and physical caps

Only the **new passive features** need a small coordinate cap. The
source's complex-time safe strip supplies, for each actual physical
preactivation, a disk radius \(c/\sqrt{\log(en)}\) and a bounded imaginary
part. The first sine Fourier coefficient on that disk bounds its real-time
derivative by \(C\sqrt{\log(en)}\). A Gaussian sphere-net estimate gives
initial coordinate maximum \(C\sqrt{\log(en)}\); integration through
\(T=C\log(en)\) bounds the physical preactivation and feature maxima
by \(B=C\log^{3/2}(en)\). This derivation is in Section 7 of
`DENSE_BUDGET_GEOMETRY.md`.

Compose the activation with a smooth cap which is the identity on that
physical range and bounded by \(2B\). Its first two derivatives are
bounded by fixed constants after increasing them by \(O(1/B)\). Accurate
completed source states and sufficiently small query/scalar noise preserve
the cap on the same physical good event. Early Picard iterates and history
marks are **not** asserted to have this coordinate bound. Their raw Gram
matrices, not their maximum coordinates, enter the comparison. The final
readout lies in a retained history span with bounded RMS; it need not be
capped to use the cross-moment estimate. Its time-dependent linear
coefficients have the same finite-source bounds as the learned updates.
The auxiliary passive network can omit the source's RMS projections:
on the physical comparison event their strict radii make them inactive.
The smooth coordinate caps give the auxiliary network its global bounds.

For a collection of history marks, let \(Q_\nu\) be its second-moment
matrix under \(\nu\). Choose a small positive \(\tau\), and use
\(Q^*=Q_\nu+\tau I\), with another fixed factor of \(\tau\) reserved
for numerical Gram error. On the posterior scalar-noise event,
the empirical Gram differs from \(Q_\nu\) by
\(\eta\operatorname{polylog}(n)\). Choose \(\eta\) small enough
that both Grams are dominated by \(Q^*\). Thus whitening by \(Q^*\)
makes both raw Grams at most the identity, without an actual Gram gap.
Concretely, approximate a dimension-\(r\) Gram entrywise to
\(\tau/(4r)\), symmetrize, and add \(2\tau I\). The result lies
between \(Q_\nu+7\tau I/4\) and \(Q_\nu+9\tau I/4\).
Make the empirical-to-population Gram error at most \(\tau/4\) too.
The same finite matrix then dominates both actual Grams and has a known
positive floor. Refined compiler quadrature computes these cached entries;
they are not infinite-precision constants or clipped sampling estimates.

This artificial ridge is harmless in physical operator geometry. If a
conditional mean learned mixer has factorization \(T A S^T/n\), its
empirical operator norm equals
\(\|Q_T^{1/2}A Q_S^{1/2}\|\). The square-root inequality
\(\|P^{1/2}-Q^{1/2}\|\le\sqrt{\|P-Q\|}\) shows that replacing
the two Grams by their common enlargements changes this norm by at most
\(C\|A\|\sqrt{\tau\operatorname{polylog}(n)}\).
All raw coefficient norms are bounded by \(\exp(\operatorname{polylog}(n))\)
from the explicit \(\sigma^2\)-gapped formulas. Choose \(\tau\) so
this error is at most \(n^{-10}\), and only then choose \(\eta\).

For the conditional variance, replacing a forward-history Gram \(Q\)
by a dominating \(Q^*\), at distance \(D\), changes
\(v^T(\sigma^2I+Q)^{-1}v\) by at most
\((D/\sigma^2)c\), where \(c\) is the incoming feature second
moment. This is the resolvent-congruence calculation in the same note.
Choose \(\tau\) to make this error, and its fixed-depth propagation,
negligible too. All precision costs remain absolute-polylogarithmic.
Use a master input history containing the forward-history columns, and
take the variance Gram as its corresponding principal block. If \(J\)
selects those columns, its whitened variance coefficient is
\((\sigma^2I+JQ^*J^T)^{-1/2}J(Q^*)^{1/2}\), a contraction
because its product with its transpose is at most the identity.
The mean's output history may have a different common Gram. Outgoing
moment marks may differ from those mean-output marks too; the recurrence
uses their separate upper raw-Gram bounds, not equality between bases.

## 5. Why a passive query has a fixed-depth moment recursion

Condition first on the actual finite **observable** noisy matrix transcript,
not on the full dense matrices or continuous training trajectory. Gaussian
likelihoods for predictable calls factor by matrix label. The initialized
hidden matrices are therefore independent posterior Gaussian blocks.
The learned source displacements are finite sums of training outer products.
Their conditional mean actions use only the retained history spans.

For a new query input vector at one layer, the exact conditional answer
covariance is

\[
 \Gamma=\beta I-K,\qquad 0\preceq K\preceq\beta I,
 \qquad \operatorname{rank}K\le R.                        \tag{5}
\]

Here the source's fresh answer noise is included:
\(\beta=\sigma^2+c-v^T(\sigma^2I+Q)^{-1}v\).
It is at most \(\sigma^2+c\). This follows directly from the commuting
left/right covariance precision factors, or the explicit formula in
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`.

Replacing \(\Gamma^{1/2}g\) by \(\sqrt\beta g\), with common
standard Gaussian \(g\), costs squared normalized error at most
\(\beta R/n\). Only the at-most-\(R\) affected eigenvalues contribute.
Each matrix is used only once in a passive forward query. Layer hybrids
propagate this error through higher posterior matrices: their centered
covariance is dominated by the prior covariance, so
\(\mathbb E\|W_{\rm centered}v\|_{2,n}^2\le\|v\|_{2,n}^2\)
for an incoming vector independent of that layer. Conditional mean learned
operators are bounded on a common training event. For the initialized part,
conditional Jensen and a first-crossing inequality applied to
\(\mathbb E[\|W(0)\|_{\rm op}^2\mid\text{observable prefix}]\)
give this event simultaneously over prefixes. The learned displacement
part has the source's physical operator bound.

Consequently removing all the corrections in (5) costs at most
\(C_L B\sqrt{R/n}\) in conditional RMS prediction error. This is a
uniform conditional estimate for each input and time, not a simultaneous
coupling of an entire random function. That is sufficient for Section 8.

After their removal, each new layer row is its smooth capped activation
at a retained-mark linear combination plus \(\sqrt\beta\) times a
fresh independent scalar Gaussian. The incoming row enters only through
its cross moments with retained source marks and its second moment.
Thus the finite-width query has a fixed-depth moment recursion. The first
layer is directly a function of its Gaussian first-row marks, learned
update marks, and the late input. The readout is a final cross moment.

The scalar-noised source is not itself an exact matrix posterior. To use
this normal form, couple it to the scalar-unperturbed program at the same
training packets, as in (12) of `PHYSICAL_NOISY_PROGRAM_BRIDGE.md`.
The frozen-prefix row fields and their genuine empirical Grams are within
\(\eta\exp(\operatorname{polylog}(n))\) of the corresponding exact
observable fields on the good noise event. The explicitly gapped mean and
covariance formulas have the same kind of sensitivity. Choose \(\eta\)
to make these errors at most \(n^{-10}\). Append fresh query marks only
after dropping unused future training coordinates, exactly as in the source
bridge. This is a coupling and perturbation argument, not a claim that
noisy moments can be inserted into a Gaussian posterior identity unchanged.

## 6. Empirical-to-calibrated comparison without unstable history inverses

Use the common whitening from Section 4. If a vector of whitened history
marks is denoted locally by \(U\), both its population and its empirical
raw second moments are at most \(I\) on the indicated posterior event.
For any deterministic bounded scalar test \(|G|\le B\), the proved
self-normalized estimate gives

\[
 \mathbb E_{\pi_c}\!left[
  \left\|n^{-1}\sum_iU(Z_i)G(Z_i)-\nu(UG)\right\|^2
  \mathbf1_{\{\text{empirical Gram}\preceq I\}}\right]
 \le \frac{CB^2}{n}
 \left[D(\pi_c\Vert\nu^{\otimes n})+\dim U+1\right].      \tag{6}
\]

See `DENSE_BUDGET_SELF_NORMALIZED.md` for its exponential-moment proof.
The test is evaluated at deterministic calibrated-population parameters,
not at random earlier empirical query summaries. The latter difference
is propagated separately. Scalar second-moment tests are bounded by
\(B^2\) and have the analogous bound with \(B^4\).

Integrate a layer's fresh scalar Gaussian before comparing its moment
outputs. For any \(C^2\) test \(\chi\), the mean
\(\mathbb E\chi(a+\sqrt v g)\) is \(\|\chi'\|_\infty\)-Lipschitz
in \(a\) and \(\|\chi''\|_\infty/2\)-Lipschitz in \(v\ge0\).
Integration by parts proves the latter at positive variance; a common
positive variance followed by dominated convergence gives zero variance.
For \(\chi^2\), the corresponding derivative bounds are
\(2B\|\chi'\|_\infty\) and
\(\|\chi'\|_\infty^2+B\|\chi''\|_\infty\).

Common whitening makes the mean operator norm bounded and the conditional
variance quadratic form a contraction. Cauchy--Schwarz then propagates
cross-moment and second-moment errors with coefficients polynomial in
\(B\), not inverse history eigenvalues or \(\eta^{-1}\). Fresh query
row noises contribute conditional cross-moment variance at most
\(B^2\dim U/n\) and scalar second-moment variance at most \(B^4/n\).
The fixed-depth recurrence in Section 6 of `DENSE_BUDGET_GEOMETRY.md`
therefore bounds the final error by
\(C\log^{C_L}(en)/\sqrt n\) in posterior RMS on the Gram/good-history
event. Its complement has an explicitly allocated fixed conditional
failure probability. Taking a fixed multiple of the RMS bound gives a
posterior interval of any specified fixed high probability.

There is no square root of a variance **error** in this propagation. Such
a loss would give a different width exponent. Strong coordinate coupling
is used only for the finite-rank correction (5); the moment recursion uses
weak Gaussian expectations with the second-derivative estimate above.

## 7. Counted numerical query evaluation

Direct sampling from the calibrated density is unnecessary. Put
\(w=\min(d\nu/d\mu,4)\). The entropy bound gives removed mass
\(e=\nu(1-w/(d\nu/d\mu))\le Ch\). For whitened marks with
\(\nu(UU^T)\preceq I\) and \(|G|\le B\), Cauchy--Schwarz gives

\[
 \|\nu(UG)-\mu(wUG)\|\le B\sqrt e,
 \qquad \mu[w^2UG(UG)^T]\preceq4B^2 I.                  \tag{7}
\]

The first statement follows by testing each unit vector and using the
removed measure, dominated by \(\nu\). The second follows from
\(w^2\le4(d\nu/d\mu)\). Bounded scalar second moments have clipping
bias at most \(B^2e\). Use exact cached training Grams and coefficients;
do not recalibrate those tiny-noise identities using clipped sampling.

`DENSE_BUDGET_ROBUST_CUBATURE.md` supplies the complete finite-seed
implementation of these finite-variance integrals. Independent blocks of
pairwise-independent row samples, followed by coordinate medians, need
\(O(\dim U\,B^2\varepsilon^{-2})\) samples per block. A logarithmic
number of independent blocks provides simultaneous confidence on a
proof-only parameter net. Include all guarded intermediate query moments
in that parameter set, as well as input and time: its dimension and the
logarithms of its continuity bounds are absolute-polylogarithmic. The
square-root dependence at zero variance is one-half-Hölder and only
squares the necessary net mesh. This covers seed-dependent intermediate
arguments directly.

Take numerical tolerance \(\varepsilon=n^{-3/4}\) in each whitened
moment. Its sample count, all block counts, and the full per-row evaluation
cost give \(n^{3/2}\operatorname{polylog}(n)\) operations. Row evaluation
uses the past response circuit at one packet, the retained scalar values,
and the polynomial-time small-matrix routines. It does not make new training
reductions. The finite-field seeds, a row, block accumulators, current
moments, counters, and cached small matrices fit an absolute-polylogarithmic
workspace. No sample panel or sphere net is stored.

The exact weak moment recursion propagates clipping bias (7) and numerical
error with a fixed-depth logarithmic factor. The clipping contribution is
\(C\log^{C_L}(en)/\sqrt n\). The numerical contribution
\(n^{-3/4}\log^{C_L}(en)\) is smaller than root width eventually,
for every fixed depth. Guarded defaults ensure the claimed query work and
memory caps even on bad states. Finite-precision row and matrix errors
are budgeted below the numerical tolerance. The same finite seed defines
one repeatable decoder function, including adaptively selected late inputs.

## 8. One event for the whole sphere and trajectory

The existing dense-pair certificate selects a deterministic proof center
within \(b_n\) of the actual dense trajectory on one good event. It is
not stored or queried. Include the physical/source event, the observable
mean-operator event, and the scalar-noise event in the complete-tape good
event. The prefix maximal inequality controls their posterior failure
probabilities simultaneously at every ideal prefix.

On this event, for **each** input and admissible time, the original passive
query posterior puts a fixed majority of its mass within
\(b_n+n^{-10}\) of that same deterministic center. Sections 4--6 put a
fixed majority, with total missing probability less than that majority,
within \(C\log^{C_L}(en)/\sqrt n\) of the calibrated moment decoder.
The two posterior intervals intersect. Thus their deterministic centers
are separated by at most the sum of their radii. This conclusion holds
for every query on the same retained-prefix event; it is not a union over
uncountably many random query draws. The entire argument is also
parameterwise in every numerical prefix in the certified ball. Thus the
deterministic conclusion holds throughout that ball and applies to the
actual privately selected numerical state without conditioning on it.

Finally intersect the one finite-seed cubature event from Section 7,
conditional on the entire training source but independent of its seed.
Adding the actual dense-to-proof-center distance gives (1). Allocate
each source, information, posterior-noise, and seed failure a fixed share
of the requested \(\delta\); the finite-prefix maximal inequalities
avoid a growing union loss. Physical time patches and the source's frozen
tail cover \([0,\infty]\). No endpoint derivative or new convergence
assumption is used.

For an explicit possible allocation, use the dense-pair certificate at
failure \(\delta/256\), and allocate the other complete-tape failures
so their total together is at most \(\delta/64\). This is possible
using their inherited arbitrary fixed-confidence versions and a larger
sufficient-width threshold for vanishing errors. The success-posterior
threshold \(1/16\) then costs at most \(\delta/4\), and also ensures
that the actual tape is good by the appended-indicator argument. Allocate
\(\delta/8\) each to the information and posterior-noise maximal
events, and \(\delta/4\) to the single numerical seed event.
Their sum is \(3\delta/4\); the remaining \(\delta/4\) covers the
acquisition/rounding failure and any separate finite-source failure not
already included. Conditional Gram and comparison thresholds are fixed
small numbers, for example \(1/32\) or \(1/16\), achieved by increasing
the constant in the root-width error radius, not by new outer events.
They can be chosen with total below \(1/4\), leaving the two posterior
interval masses with sum strictly above one. This proves probability
at least \(1-\delta\), with \(b_n=b_n(\delta/256)\) in (1).

## 9. Check record and exact conclusion

`DENSE_BUDGET_BRIDGE_CHECK.md` reconstructs the source-to-consistent-
transcript perturbation, common-Gram normal form, empirical/weak Gaussian
comparison, and one-event probability argument. Its necessary parameterwise
precision repair is included in Sections 2, 3 and 8. The isolated
`DENSE_BUDGET_NUMERICAL_CHECK.md` reconstructs the compiler, compiled-law
entropy bound, cached Gram precision, and full-domain finite-seed cubature
and costs. Their source assumptions are the inherited statements specified
here, not new activation, label, history-gap, or input restrictions.

Consequently the assembled construction has (1) and the counted costs at
every sufficiently large individual width. For fixed nonzero labels,
increase that threshold so the additional logarithmic root-width term is
at most \(b_n(\delta/256)\), and so the primitive work
\(C n^{3/2}\log^k(en)\) is at most \(C(Ln^2+dn)\).
The simple final error certificate is then \(3b_n(\delta/256)\).
The threshold remains unquantified and may depend on every fixed problem
parameter. A common enlarged absolute integer \(k\) bounds retained
storage, peak query workspace and the logarithmic query-work factor.
It has not been numerically extracted, and is not the old finite-panel
exponent five. Polynomial-in-compact-size query time is not proved.

These are complementary scoped internal checks and a lead-author assembly,
not a claim of independent promotion review or a practical implementation.
The historical candidate filename is kept for traceability.

No source study, maintained book, code, or Git index is changed by this
file. No empirical evidence is offered in place of the proof obligations.
