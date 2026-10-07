# Scoped reconstruction of the physical noisy-program bridge

2026-10-06. Internal assembly audit. This is not a full compression-theorem
verdict, an evaluator construction, or an isolated promotion review.

## 1. Frozen sources and outcome

The complete candidate read was `PHYSICAL_NOISY_PROGRAM_BRIDGE.md`,
SHA-256
`d038e95bffbce094e2bf338e967105d9267a79af1db4465855bf17a414db354f`.
The complete newly authorized conditioning source was
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`, SHA-256
`0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac`.
The already checked corrected short program has SHA-256
`0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5`.
No other source linked by the conditioning note was read.

The main bridge mechanism reconstructs: physical additive-answer noise
has small error through the stable collocation chronology; the unperturbed
noisy program has an exact finite-width row representation; scalar-summary
noise is then a separate pathwise perturbation of that representation.
The passive-query coupling uses innovations independent of the original
observable prefix, not innovations Gaussian conditional on the full tape.
Uniform bounds conditional on the full tape instead follow from fresh raw
Gaussian query noise and the larger innovation caps.

One range qualification needs an explicit correction. The candidate's
sentence that the genuine scalar moments have fixed entry bounds applies
to physical query/answer Grams. It does not follow for moments involving
the newly whitened innovation, such as $U^Tg/n$, under the full-tape
argument. The displayed proof supplies only polynomial bounds in
$R,\sigma^{-1}$ for those moments. Any argument box or complete
named-field Gram containing innovation fields must use that larger bound.
Alternatively keep the physical Gram projection separate and cap the
innovation moments in their separately certified larger box. This does
not change $P=O(R^2)$ or the polynomial logarithmic conditioning budget.

Two definitions should also be made explicit in the final assembly:
passive query branches start after the queried observable prefix, not after
an unobserved future history; and current-state decoding is invoked only
at checkpoints where all scalar coefficients needed for that state's
response circuit have been acquired. Continuous physical-time patches
can be assigned to their completed polynomial-state checkpoints. The
short program already supplies such checkpoints; an arbitrary partial
scalar reduction need not itself represent a completed physical state.

The detailed reconstruction below supports a conditional bridge after
this range clarification. It does not validate acquisition, the current
summary's posterior evaluator, or the total retained/live bit count.

## 2. Physical caps and the vector instruction count

The displacement-ball projections, residual cap and pre-gate carrier
clip are those of the corrected short program. Add nonexpansive RMS
projections to every training feature, backward carrier and gated
response used as an initialized-matrix input, with fixed radii strictly
above their actual good-trajectory bounds. The passive forward query uses
the same type of RMS projection.

These projections are inactive on the actual trajectory. For arbitrary
numerical states they ensure bounded RMS inputs. The learned hidden
displacement projection supplies a fixed Frobenius, hence operator, bound;
the initialized-matrix good event supplies the remaining operator bound.
Forward subtraction therefore has a fixed RMS Lipschitz coefficient.
Backward subtraction introduces one coordinate carrier bound
$C\sqrt{\log(en)}$ in the changed-gate term; all other propagation
uses fixed RMS/operator bounds. It adds these changed-gate terms across
layers rather than multiplying a new coordinate maximum at each layer.
Consequently the controlled field remains bounded and has Lipschitz
constant $\lambda\le C\sqrt{\log(en)}$. Its projected predictor
is uniformly Lipschitz in the normalized parameter norm on the sphere.

RMS projection factors are scalar functions of empirical squared norms.
Learned-matrix actions are finite linear combinations of named rank-one
factors, not recursive expansions of their generating trees. Counting a
linear combination as one vector instruction, each field evaluation
creates only $O(mL)$ principal vector arrays and initialized calls.
Including the last right-side evaluation gives $HK(J+1)$ evaluations.
Thus their number, together with initialized first-layer columns and new
innovation vectors, is $R\le C\log(en)^8$ after enlarging the fixed
constant. If those affine combinations are expanded into binary scalar
operations, the count receives only another fixed polynomial factor.

There is no $R^L$ enumeration: each layer output and each earlier factor
is a shared node in a finite DAG. The depth enters the number of nodes
and fixed physical constants, not the degree of a polynomial expansion
of the entire computation. No such expansion is performed.

## 3. Noisy field evaluations and stable physical propagation

Fix the initialized matrices on their operator good event, and compare
one noisy and noiseless field evaluation at the same projected parameter
state. On the event that its fresh raw noises have RMS at most two,
each matrix answer error has RMS at most $2\sigma$.
Forward subtraction costs $C\sigma$; backward subtraction costs
$C\sqrt{\log(en)}\sigma$, with the same single gate-factor argument.
Residual and rank-one gradient subtraction give the normalized field
defect

\[
 d_n=C\sqrt{\log(en)}\sigma.                         \tag{1}
\]

The noisy evaluation need not be a Lipschitz function of its state or
reuse the same noise between iterations. It is enough to treat every
evaluation as the deterministic controlled field plus an error bounded
by (1).

To check the interpolation factors explicitly, a patch has length
$h\le(16\lambda K)^{-1}$ and interpolation norm at most $2K-1$.
Its inexact node Picard recursion has contraction part at most $1/8$
and additive defect at most $h(2K-1)d_n$. Hence its extra node error
is at most $C hK d_n$. At the endpoint, the positive quadrature
weights have total mass one. The added endpoint defect is therefore
bounded by

\[
 h d_n+h\lambda\,C hK d_n\le C h d_n.
 \tag{2}
\]

Combining this with the already proved endpoint recurrence gives a total
endpoint perturbation at most

\[
 CT e^{C\lambda T}d_n.
 \tag{3}
\]

Interior times have the additional local term $ChK d_n$, which is no
larger than (3) at the stipulated eventual widths. The finite Picard
remainder remains exponentially small in its iteration count. This
reconstructs candidate equation (5), without mistakenly accumulating an
extra factor $K$ in the time-stability exponential.

For $\sigma=e^{-\log(en)^2}$ and $T=C\log(en)$, the logarithm
of (3) is $-\log(en)^2+O(\log(en)^{3/2})$. It is smaller than
$n^{-a}$ for every fixed $a$ at sufficiently large width. The raw
Gaussian RMS-tail union costs at most $R e^{-cn}$ over training calls.
The same source good event and tail extension allow any required fixed
factor in the horizon. Freezing the approximating endpoint controls
later times and infinity; it does not assert exact label fitting.

## 4. Exact two-orientation law and its one-call bounds

The conditioning theorem concerns hidden raw noises and the observable
answer filtration. With old forward/reverse observations
$Y=WV+\sigma\Xi$, $X=W^TU+\sigma Z$, define
$\delta=\sigma^2$ and the normalized scalar matrices as in its
equation (4). Multiplying the predictable-noise likelihood by the
Gaussian prior yields

\[
 \delta\overline W+(UU^T/n)\overline W
                  +\overline W(VV^T/n)=(YV^T+UX^T)/n.
 \tag{4}
\]

No derivative of an adaptive query enters this likelihood: that query
is fixed by the preceding observed answers in each chronological
conditional density. Independent matrix priors and the grouped
likelihood retain conditional independence of different matrix labels.

Writing $C=(\delta I+Q)^{-1}$, $D=(\delta I+K)^{-1}$, the
small Sylvester solution
$(\delta I+K)E+EQ=-HC-DJ$ gives
$\overline W=YCV^T/n+UDX^T/n+UEV^T/n$. Substitution into (4)
cancels the two cross terms. This independently checks the mean formula
and its normalization.

The covariance is $\delta I+f(UU^T/n)$, where the displayed resolvent
formula in the source gives $0\le f\le d$ and a floor $\delta I$.
Its low-rank square root follows from the rational divided difference
$a h(a)=f(a)-f(0)$ and rationalization of the square root. All required
small inverse/Sylvester gaps are at least $\delta$, and the final
square-root denominator has gap at least $2\sigma$. The formulas do
not invert a history Gram or divide by its zero eigenvalues.

There is an explicit absolute-degree mean bound. If all old physical
query and observed-answer fields have RMS at most $B$, source equations
(34)–(35) give

\[
 \|\overline Wv\|_{2,n}
 \le C\{R B^3\sigma^{-2}+R^2B^5\sigma^{-4}\}=:M_\mu.
 \tag{5}
\]

Indeed the operator norm of each column array divided by $\sqrt n$
is at most $\sqrt R B$; apply this to the coefficient bounds for
$Cv$ and $Dx+Ev$. The same estimate holds in the reverse orientation.
It is a one-call bound from the observed fields, not an induction that
multiplies a loss $\sigma^{-c}$ once per prior call.

The square-root correction coefficient satisfies
$\|T(K)\|\le B^2/(2\sigma^3)$, while its new scalar moment
$t=U^Tg/n$ satisfies
$\|t\|\le\sqrt R B\|g\|_{2,n}$. Thus all the one-call
coefficients have fixed-degree polynomial bounds in
$R,B,\sigma^{-1},\|g\|_{2,n}$.

## 5. Innovation caps under the full training tape

On the original noisy probability space define
$g=\Gamma^{-1/2}(y-\overline Wv)$. This is standard Gaussian
conditional on the appropriate observable prefix. It is generally not
Gaussian conditional on the complete matrices and training tape.
Conditional on the latter, only the new raw $\xi$ in
$y=W_0v+\sigma\xi$ is fresh Gaussian.

On the operator event, $\|v\|_{2,n}\le B$ and
$\|\xi\|_{2,n}\le2$ imply
$\|y\|_{2,n}\le CB+2\sigma$. Therefore (5) and the covariance
floor give

\[
 \|g\|_{2,n}\le\sigma^{-1}(CB+2\sigma+M_\mu)=:G_*,
 \qquad \max_i|g_i|\le\sqrt n G_*.
 \tag{6}
\]

$G_*$ is a fixed-degree polynomial in $R,B,\sigma^{-1}$.
This verifies the candidate's large coordinate-cap principle. It does
not use a typical $\sqrt{\log n}$ maximum after invalid conditioning.
On a fixed good training tape the same argument applies to every passive
query and requested time, provided its raw query noises have the RMS
bound. Their conditional failure is at most $CL e^{-cn}$, with no
union over queries.

The moment-range qualification from Section 1 now becomes precise.
Physical history Grams have entries at most $B^2$ and operator norm at
most $RB^2$. By contrast,

\[
 |n^{-1}u^Tg|\le B G_*,\qquad
 n^{-1}\|g\|_2^2\le G_*^2.                            \tag{7}
\]

These are the certified bounds for innovation-containing summaries on
the stated full-tape event. A complete Gram of all named physical and
innovation fields can safely use a cap of order
$CR(B+G_*)^2$. If only physical fields are included in the PSD-Gram
projection, use that original cap there and separately bound $t$ and
other innovation moments by (7). The candidate must make one such
choice explicitly. All resulting log caps remain polynomial in
$R,\log(en),\log(\sigma^{-1})$.

Raw row products can have magnitude $n$ times these polynomial bounds,
although their empirical averages have smaller physical bounds. This
is harmless for logarithmic size, but these row intermediates must also
receive their own larger caps. The physical low-rank coefficients and
interpolation weights have polynomial size in the transcript count;
combining them with (5)–(7) gives certified logarithmic bounds for those
intermediates as well.

## 6. Scalar-summary perturbation and the query coupling

The exact $\sigma$-noisy row program has iid packets $Z_i$ and scalar
summaries $C_r=n^{-1}\sum_iF_r(Z_i;C_{<r})$. Once all caps and
off-domain PSD extensions are specified, the source's gapped small-matrix
sensitivity bounds and the bounded row DAG give a global constant
$\Lambda$ with polynomially bounded logarithm. The number of row/scalar
primitive instructions is polynomial; multiplying their sensitivities
adds a polynomial number of terms to the logarithm. This does not require
analyticity of the hard projections.

On the same packets, add independent scalar noises through
$\widetilde C_r=n^{-1}\sum_iF_r(Z_i;\widetilde C_{<r})+\eta E_r$.
If $\max|E_r|\le n$, maximum-coordinate subtraction gives
$e_r\le(1+\Lambda)e_{r-1}+\eta n$. Consequently

\[
 \max_r|\widetilde C_r-C_r|
                     \le\eta nP(1+\Lambda)^P.
 \tag{8}
\]

Append the polynomially many query instructions to this same scalar/row
DAG comparison. Their global range and Lipschitz constants are uniform
in the sphere input and interpolation time; interpolation weights and
input coordinates have their explicit bounded domains. Choosing $\eta$
after these bounds makes the final discrepancy smaller than $n^{-a}$.
Its negative logarithm remains an absolute polynomial in the indicated
logarithmic quantities. There is no circular choice: the underlying
functions, caps and $\Lambda$ depend on $\sigma$, not on $\eta$.

This is emphatically not an exact Gaussian-matrix law with noisy Grams
substituted into its posterior. It is a new interacting-row program
compared pathwise to the exact one. The unclipped Gaussian scalar updates
retain their transition densities, while their appearances as coefficient
arguments are clipped by the specified routines.

Here is the joint coupling needed for a passive query. Stop the original
$\sigma$-noisy physical program at the relevant completed observable
prefix. Its original training innovations are measurable functions of
that observable history, and the auxiliary scalar $E$ tape is independent
of the original matrices and noises. The perturbed summary prefix is a
deterministic function of these original innovations, initial row inputs
and $E$'s; hence it is measurable with respect to that augmented original
history.

Append a passive query to the *original* noisy program and define each
query innovation by the exact inverse square root at that original
history. Conditional on the augmented original past, each new innovation
is independent standard Gaussian. It is therefore also independent of
the perturbed summary prefix and earlier query innovations. Feed this
same query innovation to both the unperturbed and scalar-perturbed row
query circuits. Equation (8)'s extended DAG comparison applies.

If future training calls were already defined on the proof probability
space, the query innovation need not be independent of their future
innovations. Nothing here requires that stronger statement: the posterior
query branch uses the selected current prefix and integrates future
unobserved variables out. Conditional on the complete training tape the
innovation is likewise not Gaussian; (6) supplies its range on the
fresh raw-noise event instead.

This construction proves a coupling for each query, uniform in its
error constants given a common good training tape. It does not construct
a jointly independent Gaussian query-noise field over the whole sphere.
That marginal conditional assertion is exactly the hypothesis used in
the separate conditional-prefix center transfer.

## 7. Summary count, all-time scope and remaining interfaces

Each named physical or innovation vector is a row node. Matrix conditioning
uses pair moments of those nodes; the learned low-rank actions and RMS
projections use further pair moments of already named fields. Each pair
need be formed once when both fields exist. Thus at most $CR^2$ scalar
empirical-average variables are needed. Small-matrix operations of
dimension at most $R^2$, including the PSD extensions, add scalar
arithmetic but no new empirical row average. The statement $P\le CR^2$
is therefore consistent with the enlarged moment caps above.

A passive query adds a fixed number of forward layers and contractions
against old factors, still polynomial in $R$. Its noise error follows
from a forward-only RMS recurrence. There is no new backward path, no
query-specific physical good event, and no exponent growing like $R^L$.
The common training good event consists of the inherited dense event,
the finite raw training-noise RMS events, and the scalar-noise events.
Its explicit additional failure is bounded by
$R e^{-cn}+2P e^{-n^2/2}$. Uniform conditional query failure has the
analogous fixed-forward-call and appended-scalar bounds.

The original physical discretization covers each real patch, and the
source tail controls the frozen approximation after $T$, including the
endpoint. Scalar perturbation and cap bounds are uniform across the
interpolation domain. Hence this assembly does not shrink the inherited
label allowance, alter physical time, or replace nonlinear feature learning
by a kernel model.

Nevertheless, the row representation is not itself the requested compact
current-state model. Exact weighted acquisition, nested retained-prefix
information, posterior test evaluation from that prefix without training
replay, and complete finite-precision/peak-workspace accounting remain
separate interfaces. In particular a Gaussian conditional kernel written
in terms of latent full rows is not yet a small-space posterior algorithm.
This audit does not supply a full-theorem PASS.

## 8. Provenance

The complete frozen bridge and complete conditioning source were read
under the supervisor's explicit scope expansion. The corrected short
program and its already authorized analytic/physical sources remained
in context. No other note named by the new source was fetched, and no
other review was read. The supervisor's earlier innovation-cap warning
was part of this supervised assignment, not an independent finding
withheld from the checker. The mean bound, inexact collocation recurrence,
prefix coupling and count audit above were reconstructed directly.

Only this assigned check was created. No candidate, maintained source,
Git index or experimental artifact was changed. The standard rigorous
proof and notation instructions were applied with the previously
reported custom-skill access fallback.

## 9. Corrected-version verification

The complete corrected bridge, SHA-256
`b20650d28fe3a4c8ebc76105bd5f4347503bd0485bcced588dd1680bc65cadc6`,
was read on 2026-10-06. Section 4 now distinguishes fixed physical
query/answer Gram bounds from innovation-moment bounds $BG_*$ and
$G_*^2$, and supplies the larger complete-Gram cap or a separate
innovation-moment box. Section 5 explicitly bases query innovations on
the original observable prefix, includes the independent scalar-noise
tape in the coupling, and disclaims independence from future training
or the complete tape. Section 6 restricts served time patches to
checkpoints whose required response coefficients have been acquired.

These changes resolve the range and interface qualifications identified
in Sections 1 and 5–6 of this audit. The reconstructed physical-to-noisy-row
bridge is supported at this version, conditional on its stated inherited
sources and explicitly specified finite program. This addendum does not
verify acquisition, posterior integration or a complete compressed-model
theorem.
