# From the physical dense trajectory to a regularized row program

2026-10-06. Candidate assembly lemma for the current-state decoder;
separately reconstructed with the innovation-moment range clarification
below. See PHYSICAL_NOISY_PROGRAM_BRIDGE_CHECK.md. This is not, by itself, the final
compression theorem.

The point of the deliberately added noises below is computational
regularization. They do not replace nonlinear feature learning by a
kernel evolution. Their accumulated effect on the original nonlinear
predictions can be made smaller than any fixed inverse power of the dense
width. The logarithms of all resulting numerical conditioning bounds
remain bounded by an absolute power of that width's logarithm.

## 1. Inputs and order of choices

Use the network, normalized parameter norm, original label allowance,
and dense good event in
[SHORT_CAUSAL_TRAINING_PROGRAM.md](SHORT_CAUSAL_TRAINING_PROGRAM.md).
Its corrected theorem and separate check supply a causal collocation
program through \(T=C\log(en)\), with at most
\(C[\log(en)]^8\) initialized-matrix calls, and uniform numerical
error smaller than \(n^{-a}\), for any fixed \(a>0\), including the
endpoint. Constants and eventual width thresholds may depend on the
fixed admissible problem and on \(a\). No extra history-Gram gap is
assumed.

Use also the exact formulas and sensitivity bounds in
[NOISY_TWO_ORIENTATION_TRANSCRIPT.md](NOISY_TWO_ORIENTATION_TRANSCRIPT.md).
That lemma replaces the law of a finite noisy matrix program by a
row-interaction program with independent Gaussian packets; it does not
replace empirical moments by population moments.

Choose the physical discretization first. Next choose the matrix-answer
noise level

\[
 \sigma=\exp\{-[\log(en)]^2\}.                            \tag{1}
\]

Finally choose a much smaller scalar-summary noise level \(\eta\),
after bounding the finite row program's ordinary Lipschitz constants.
Thus the choice of \(\sigma\) does not depend circularly on the
\(\sigma\)-dependent row-law conditioning bounds.

## 2. Harmless additional caps and finite-vector instruction count

The controlled field in the short-program note projects the learned
displacements, clips residuals, and clips backward carriers **before**
their activation-derivative multiplication. Add the following real
projections, with fixed radii strictly above the inherited actual bounds:

* project each training forward feature onto its RMS ball;
* project each training backward carrier and gated backward field onto
  their RMS balls, retaining the pre-gate coordinate clipping;
* use the same forward RMS projections for a passive query.

These projections are the identity on the actual good trajectory. They
are Euclidean-nonexpansive. On the initialized-operator good event, the
controlled field is therefore still bounded by a fixed constant and
Lipschitz, in the parameter norm, with constant
\(C\sqrt{\log(en)}\). The proof is the same forward subtraction,
one carrier-maximum factor in gate subtraction, and rank-one gradient
subtraction as in the short-program note. The prediction map is still
uniformly Lipschitz in that parameter norm on the sphere.

These caps ensure that every vector submitted to an initialized matrix
has a fixed RMS bound, including in arbitrary numerical iterates.
The first initialized matrix is supplied directly as its \(d\) Gaussian
row coordinates; it does not require a square-matrix reveal.

Every learned displacement is represented as a sum of previous rank-one
gradients. Each learned-matrix action is one affine combination of its
named factors, with coefficients computed from scalar inner products.
There is no need to name a separate vector for every partial sum in
that combination. The number of distinct vector fields is therefore
at most a fixed multiple of the number of forward/backward evaluations,
plus the initialized first-layer columns. Write \(R\) for a common
bound on this count and the noisy matrix calls. It satisfies

\[
 R\le C[\log(en)]^8.                                      \tag{2}
\]

All needed scalar empirical averages can be formed from pairwise products
of these fields and from their products with new Gaussian innovations.
At most \(CR^2\) empirical averages are needed. Repeated scalar arithmetic
on these averages, including the low-rank Frobenius projections, does not
create a new row-average variable. A bounded-arity expansion of the
coordinate formulas and of the scalar routines has size polynomial in
\(R\), with an absolute polynomial degree. Depth, sample count, and
input dimension affect the constants in (2), not that degree.

## 3. Additive matrix-answer noise has negligible physical effect

At every initialized hidden-matrix call, in either orientation, return

\[
 W_0v+\sigma\xi \quad\hbox{or}\quad W_0^Tu+\sigma\xi,
 \qquad \xi\sim N(0,I_n),                                 \tag{3}
\]

with independent fresh noises. These noises are hidden from the observed
matrix-program filtration. The numerical program uses only the answers.

Couple the noisy and noiseless programs with the same initialized
matrices. Suppose every noise used in one field evaluation has RMS at
most two. The initialized matrix norms and projected displacement norms
are fixed on the good event, while all feature/carrier RMS norms are
capped. Forward subtraction within that evaluation gives a feature RMS
error at most \(C\sigma\). Backward subtraction gives at most
\(C\sqrt{\log(en)}\sigma\), since the gate difference contains
one clipped carrier factor. The residual and rank-one gradient errors
are consequently at most

\[
 C\sqrt{\log(en)}\sigma                                  \tag{4}
\]

in the normalized parameter norm. These are pointwise error bounds at
the same input parameter state. There is no independence premise in the
deterministic subtraction.

Insert (4) into the collocation comparison. Its node contraction still
uses the deterministic noiseless controlled field; noisy evaluations
are treated as additive defects. The positive endpoint quadrature rule
then gives the same endpoint recurrence as the short-program proof,
with an additional forcing term
\(Ch\sqrt{\log(en)}\sigma\). Iterating and bounding interior
times gives total state and output perturbation at most

\[
 CT\exp\{C T\sqrt{\log(en)}\}
                       \sqrt{\log(en)}\sigma.             \tag{5}
\]

The finite Picard iteration error has the same exponentially small
term as before, plus a fixed multiple of (4); this follows by iterating
the node contraction with additive error and summing its geometric
series. Thus it is already covered by (5), after changing the constant.
With (1), (5) is smaller than \(n^{-a}\) for every fixed \(a\) at
sufficiently large width.

For a standard Gaussian vector,
\(\mathbb P(\|\xi\|_2>2\sqrt n)\le e^{-c n}\).
For completeness, exponential Markov with any fixed \(0<s<1/2\)
uses
\(\mathbb E e^{s\|\xi\|^2}=(1-2s)^{-n/2}\); choosing, for
example, \(s=1/4\) proves the displayed bound. A union over the
\(R\) training calls costs at most \(R e^{-cn}\). This explicit
failure tends to zero and is separate from the inherited eventual dense
good event.

At decoding, add the same noise to the finitely many forward-only
initialized matrix calls for the query. Conditional on the complete
initialized matrices and training tape, these raw noises remain fresh
standard Gaussians. Their RMS failure is at most \(C L e^{-cn}\),
uniformly in the query and requested time. The deterministic forward
subtraction bound is \(C\sigma\), in addition to the already bounded
training-state error. No Gaussian law for a whitened innovation
conditional on the complete matrices is being assumed.

The source's uniform output tail after \(T\), together with the endpoint
parameter approximation, covers all \(t\ge T\), including infinity.
The statement here is about an approximation to the actual fitted
trajectory, not exact fitting by the noisy numerical program.

## 4. Exact row-law representation and safe large caps

Apply the noisy two-orientation theorem to (3). The initialized first
matrix supplies iid \(d\)-dimensional Gaussian row packets. Each
additional call supplies one independent standard Gaussian coordinate
per row. The exact finite training law is therefore a causal program
driven by iid packets of dimension at most \(d+R\), with at most
\(CR^2\) empirical-average summaries. All other coefficients are
specified functions of earlier summaries, using the explicitly
\(\sigma^2\)-gapped inverses, Sylvester solves, and square root.

For numerical integration, extend those coefficient functions away
from genuine empirical moments using the capped PSD-Gram projections
in that theorem. Impose additional coordinate caps on row operands and
on intermediate scalar arguments. They are chosen to be the identity
on the following good-program range, not inferred to be harmless
merely because they are available.

On the initialized-operator event and the raw-noise RMS event, every
submitted query has bounded RMS, and every observed raw answer has
bounded RMS. Hence every one of their coordinates has magnitude at
most \(C\sqrt n\). The genuine **physical query/answer** moments have
fixed entry bounds and matrices of norm at most \(CR\). Moments involving
the whitened innovations are treated separately below and need not have
these fixed bounds. The explicit posterior
mean coefficients are bounded by a fixed polynomial in \(R\) and
\(\sigma^{-1}\); the same is true of the covariance square-root
coefficients. Each of their small-matrix intermediate operands has
the same kind of bound, by the displayed formulas.

The innovation defined on the original probability space is

\[
 g=\Gamma^{-1/2}(y-\overline Wv),\qquad
                         \Gamma\succeq\sigma^2I.          \tag{6}
\]

The observed answer and explicit posterior mean have RMS bounded by
a fixed polynomial in \(R,\sigma^{-1}\). Thus

\[
 \|g\|_2/\sqrt n\le (C(1+R)(1+\sigma^{-1}))^C,
 \qquad
 \max_i|g_i|\le\sqrt n(C(1+R)(1+\sigma^{-1}))^C.            \tag{7}
\]

The exponent is absolute: this follows from the finite formulas for
one posterior call, not from multiplying an uncontrolled inverse
history gap at each call. All old observed-answer RMS bounds come
directly from (3), not from such a recurrence.

Write \(G_*=(C(1+R)(1+\sigma^{-1}))^C\) for the RMS bound in (7).
For a physical field of RMS at most \(B\), innovation cross-moments
have magnitude at most \(B G_*\), and innovation second moments
have magnitude at most \(G_*^2\). Thus a Gram table containing
innovation fields uses a cap at least \(CR(B+G_*)^2\), not the fixed
physical-Gram cap. One may instead retain these innovation moments
outside the physical-Gram projection, with those same separate bounds.

Choose row/root caps larger than the second bound in (7), and moment
matrix caps larger than these appropriate genuine Gram bounds. Their
logarithms remain polynomial in (8). Fixed scalar arithmetic
inside a row instruction involves sums of at most \(CR\) terms and
products of the bounded operands just listed. Its intermediate cap can
therefore be chosen with logarithm polynomial in

\[
 R,\quad \log(en),\quad \log(\sigma^{-1}),                \tag{8}
\]

with an absolute degree. In particular, clipping only at a typical
\(\sqrt{\log n}\) innovation size is unnecessary and would not
justify a bound conditional on the complete initialized matrices.
The larger caps (7) have affordable logarithmic descriptions.

On the stated good events every inserted cap is the identity in the
exact noisy program. Off those events the capped program is a specified
surrogate. This is sufficient for the subsequent probability argument;
no expectation bias proportional to an unspecified bad-event rate is
being claimed small.

## 5. Small scalar-update noise and quantitative global regularity

Write the resulting capped row program as

\[
 C_r=\frac1n\sum_i F_r(Z_i;C_{<r}),
                         \qquad 1\le r\le P,\quad P\le CR^2. \tag{9}
\]

Pure deterministic coefficient calculations are incorporated in the
row functions \(F_r\); they are not separate random summaries.
The clipped inputs and explicit gapped small-matrix formulas give
global bounds

\[
 |F_r|\le B,\qquad
 |F_r(z;c)-F_r(z';c')|
        \le\Lambda(\|z-z'\|_\infty+\|c-c'\|_\infty),       \tag{10}
\]

where \(\log B\) and \(\log\Lambda\) are bounded by an absolute
polynomial in (8). To check the dependence, expand a row formula into
its polynomially many bounded scalar instructions. Projection is
nonexpansive; activation and first-derivative Lipschitz constants are
fixed; multiplication costs the bounded operand ranges; inverse and
square-root sensitivity are the stated powers of \(\sigma^{-1}\).
Multiplying at most polynomially many such instruction bounds adds at
most a polynomial to their logarithms. There is no repeated-squaring
range assertion: each intermediate is explicitly capped at its
certified good-range bound.

Now define the perturbed training summaries by

\[
 \widetilde C_r=\frac1n\sum_iF_r(Z_i;\widetilde C_{<r})
                                      +\eta E_r,           \tag{11}
\]

where the \(E_r\) are independent standard Gaussians. Summary arguments
outside the chosen box are clipped inside the coefficient routines;
the summary (11) itself is not clipped, so it has the Gaussian
transition density used by the Fourier evaluator.

This is a perturbation of the exact row-law program, **not** another
exact Gaussian-matrix posterior formula. In particular, the true
empirical history Grams in that posterior are not silently replaced
by noisy ones while claiming the same law.

If \(\max_r|E_r|\le n\), the common-row coupling gives

\[
 \max_r|\widetilde C_r-C_r|
                       \le\eta nP(1+\Lambda)^P.            \tag{12}
\]

The analogous bound for the final query output includes its polynomial
number of added summary/row instructions, each obeying the same type
of global bound. Choose \(\eta>0\) so that this larger bound is at
most \(n^{-a}\). Its logarithmic inverse is still an absolute
polynomial in (8) and \(\log(en)\). The failure
\(\mathbb P(\max|E_r|>n)\le2P e^{-n^2/2}\) is explicit.

For a passive query append only its forward instructions and moment
summaries, with fresh independent scalar-update noises at this same
or a smaller specified level. The joint row law uses independent new
innovation coordinates **conditional on the original observed training
prefix** of the exact, scalar-unperturbed noisy-matrix program. On its
original coupling these coordinates are independent of that original
prefix and of the independent scalar-noise tape; the perturbed retained
prefix is a function of these two objects. They are not claimed independent
of unobserved future training innovations or the complete training tape.
On the original dense coupling, (6)--(7) control those innovations
conditional on the complete training tape, whenever the fresh raw
query noises have the RMS bound. Therefore (12) and its query extension
have constants uniform in the unseen input and requested time.

Combining (5), (12), the short-program discretization, and the fitting
tail proves the following precise bridge. There is a single training
good event with the inherited eventual probability, less the explicitly
displayed vanishing noise failures. On it, for every input on the sphere
and every training time, the appended row-query output admits a coupling
to the actual dense prediction with error at most \(C n^{-a}\), except
for a fresh-query failure tending to zero uniformly and conditionally
on the complete training tape. This is a marginal-query statement; it
does not assert independent Gaussian innovations conditional on that
complete tape, or a simultaneous query-noise realization on the sphere.

## 6. Intended use and remaining checks

The retained state for the proposed decoder consists of the **prefix**
of (11), not its unobserved future. Its coordinate-response circuit has
the observed prefix values substituted as constants. Evaluating that
circuit at a Gaussian row argument does not solve or update the scalar
training dynamics; it evaluates a representation of past responses.
A checkpoint serves only a time patch whose required response coefficients
have already been acquired; the numerical updater completes that patch's
finite local calculation at its opening.

Positive weighted row selection can reproduce (11) autonomously on a
small set of stored row packets; that is a separate algebraic lemma.
The fixed-prefix conditional Fourier calculation uses only these
retained summary values and the current response circuit. Its posterior
does not condition on the private selected packets or weights. This
distinction is deliberate and is part of the decoder definition.

To finish the full theorem one must combine this bridge with that
acquisition lemma, the conditional integral's counted workspace and
finite-precision stability, and the maximal-posterior robust-center
argument. All three must use the same prefix, caps, and noise levels.
No complete decoder claim is made by this bridge in isolation.
