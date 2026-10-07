# An absolute-polylogarithmic current-state decoder

2026-10-06. **Complete author proof with an isolated full-chain internal
reconstruction of its supplemented version.** The result is conditional
on the explicitly inherited dense certificates, as detailed below. It is
not a promoted result of the maintained book. The historical filename is
retained so that existing links and the frozen review remain traceable.

The proposed model retains compressed historical response information.
A query does not run the scalar training updates again. It evaluates a
conditional integral from the presently retained coefficients and their
row-response circuit. Runtime can be enormous; the intended conclusion
is a bound on retained storage and peak working memory, not fast decoding.

## 1. Setup and precise conclusion

Fix the original admissible problem: depth \(L\ge2\), training points
\(x_a\in\mathbb R^d\) on \(\|x_a\|=\sqrt d\), \(m\ge d\)
spanning inputs, labels with \(Y=\|y\|_2/\sqrt m>0\), positive
initial feature-Gram gap \(\gamma\), and the existing small-label
condition. Activations are the original strip-analytic functions with
bounded derivatives; their values need not be bounded. Use the original
Gaussian initialization, zero readout, mean-square loss, and mobilities
\((n,1,\ldots,1,n)\). The dense predictor is \(f_n(t,x)\).

All fixed-problem constants below may depend on the data, \(m,d,L\),
activations, label allowance, gap, and confidence. A logarithmic exponent
described as absolute does **not** depend on these quantities. All
retained parameters, instructions, selected row marks and live decoding
workspace count. Dense preprocessing workspace and runtime are not
bounded by the theorem; this limitation is explicit.

This is a parameterwise construction: the admissible problem is fixed,
and finite certified upper/lower bounds from its inherited estimates may
be supplied to the algorithm. Those bounds and their finite descriptions
count. A uniform compiler extracting all such bounds from arbitrary raw
activation code and data is not asserted. The width threshold may depend
on these fixed bounds; they do not depend on the width.

Let \(b_n(\delta)\) denote the inherited dense-versus-independent-dense
upper certificate in the whole-sphere, complete-trajectory norm. In the
notation of the integrated dense-comparison source it has the form

\[
 b_n(\delta)=
 \frac{CY}{\sqrt n}e^{CY^2\sqrt{\log(en)}}
       \sqrt{8\log\!\frac{8(n+1)(1+2n)^d}{\delta}}
       +\frac{CY}{n}.                                      \tag{1}
\]

The sufficient width for its probability statement remains inherited
and unquantified. Formula (1) is not a new sharp assertion about its
sample/gap prefactor; those constants are the original certificate's.

**Theorem.** There is an absolute integer \(k\) such that,
at every sufficiently large individual width, a source-dependent
preprocessing of the dense reference and training data produces an
autonomous compact algorithm with a current state and a deterministic
late-query decoder satisfying, with probability at least \(1-\delta\),

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
       |f_{\rm compact}(t,x)-f_n(t,x)|
              \le2b_n(\delta/32)+\frac1n,                 \tag{2}
\]

and using at most \(C[\log(en)]^k\) retained scalar registers and
peak decoding workspace. The decoder is a function of the current
compressed state, \(t\), and the new \(x\); no test inputs or test
labels are needed at initialization or training.

The computational model uses the original fixed activations as
evaluation primitives, as the dense network itself does. A corresponding
bit-space bound holds when those primitives and the fixed input data have
counted polynomial-space precision interfaces; its exponent may depend
on that fixed evaluation exponent, not on \(d,m,L\). Bare strip
analyticity cannot imply such an interface for an activation containing
noncomputable constants. This distinction must remain visible rather
than imposing a new activation restriction silently.
In the bit-space version, a query and a finite patch-time coordinate are
dyadic inputs or have counted precision access of a common fixed
polynomial-space order; their requested accuracy is included in the
budget. Exact arbitrary real inputs belong to the scalar-register
version. The endpoint is an explicit terminal flag, not an infinite
precision time input.

The compact dynamics is a causal, finitely scheduled response algorithm,
not an ordinary smaller neural net or an asserted smooth gradient-flow
ODE. It can be made autonomous by adjoining its clock and instruction
index. Between completed training patches the decoder uses the current
patch's fixed polynomial time coordinate. At the terminal patch the
state freezes and serves the fitted tail and endpoint.

For \(Y=0\), the zero predictor gives the conclusion directly.

## 2. What the state contains

The checked short-program construction uses at most
\(R\le C[\log(en)]^8\) named training vector fields and initialized
matrix calls. The physical-to-noisy bridge and Gaussian elimination
replace them by a finite row-response circuit driven by iid Gaussian
packets of dimension at most \(d+R\). Its shared updates are

\[
 C_r=\frac1n\sum_{i=1}^nF_r(Z_i;C_1,\ldots,C_{r-1})+\eta E_r,
                      \qquad 1\le r\le P,\quad P\le CR^2. \tag{3}
\]

Here the \(F_r\) are explicitly specified bounded Lipschitz row
circuits; \(Z_i\) are independent Gaussian packets; and the scalar
\(E_r\) are independent Gaussians. The tiny \(0<\eta\le1\) is chosen
by an explicit finite-program perturbation budget. All matrix posterior
operations use the deliberately added matrix-noise gap, not an assumed
history-Gram gap. Local notation \(R,P,C_r,Z_i,E_r,\eta\) describes
the construction, not additional dataset hypotheses.

Preprocessing selects \(q\le P+1\) packets and positive weights
whose weighted averages match the \(P\) realized integrands in (3).
The compact online update uses only those packets:

\[
 C_r=\sum_{j=1}^q p_jF_r(z_j;C_{<r})+\eta E_r.
                                                               \tag{4}
\]

The induction proving equality of (3) and (4) is exact. Selection may
inspect the completed finite source computation, but the retained
objects are packet marks, weights, noise marks, circuit instructions,
and the **already acquired prefix** of \(C\). No table of future
\(C_r\) values or width-\(n\) forward/backward history is stored.

In particular, packet count and raw retained numerical entries admit
the bounds

\[
 q\le C[\log(en)]^{16},\qquad
 \text{packet/history entries}\le C[\log(en)]^{24},        \tag{5}
\]

before instruction workspace and precision. These are not claims of an
optimized exponent or a \(\log^5 n\) construction. Those additional
costs remain absolute-polylogarithmic but can have a larger exponent.

At a given physical time the state retains every earlier scalar summary,
so the observed prefixes generate nested information. The circuit with
these summaries inserted as constants represents the past row responses.
Evaluating it at one Gaussian argument is a feed-forward computation;
it does not recover missing scalar training moments or integrate the
training evolution anew.

## 3. The current-state query computation

For a new input, append its forward-only response instructions to the
current circuit. Their small number of new scalar means, and their fresh
Gaussian innovations, are integrated out. No query is added to training
loss or to the retained training history.

The decoder deliberately conditions on the current scalar prefix alone,
not on the private selected packets, weights, or preprocessing noise
marks. They still count as retained storage and are used for autonomous
training updates. Ignoring them in the specified query law is legitimate;
conditioning on them would be a different decoder and is not the law
analyzed here.

For fixed current prefix \(c\), the exact conditional row likelihood is

\[
 \prod_{r\le j}\frac1{\sqrt{2\pi}\eta}
  \exp\left[-\frac1{2\eta^2}
    \left(c_r-\frac1n\sum_iF_r(Z_i;c_{<r})\right)^2\right]. \tag{6}
\]

This is why noise is added to the scalar **updates**, rather than only
to a finished noiseless summary. The sequential Gaussian densities prove
(6) without a formal change-of-variables assumption.

Fourier inversion converts each factor in (6) into a scalar frequency
integral. With the supplied \(c\) held fixed, independence of the
unconditioned row packets replaces the \(n\)-row integral by

\[
 \left[\mathbb E_Z
    e^{-\frac{i}{n}\sum_r\xi_rF_r(Z;c_{<r})}
 \right]^n.                                                \tag{7}
\]

The conditional numerator additionally integrates the passive-query
summary variables. It does **not** integrate over the training prefix,
update (3), or read a discarded dense matrix. The denominator is the
density of that observed prefix.

The Fourier evaluator proves deterministic numerical evaluation of
bounded conditional tests with all cutoffs, oscillatory cancellation,
precision and tensor-grid counters counted. The grids and Gaussian rows
are never stored. A unit-disk projection before taking the power in (7)
ensures that a characteristic-function error \(e\) amplifies by at
most \(ne\), not by an uncontrolled exponential.

Finally use bounded smoothed-CDF tests and deterministic bisection to
return an approximate posterior median. This avoids an unjustified
conditional-mean bias from rare bad trajectories with only an eventual
probability estimate.

## 4. Probability and whole-trajectory error

This step uses the complete-time dense comparison, not a union of
fixed-query claims. Apply it with confidence \(\delta/32\).
Fubini gives a deterministic proof-only center \(f_0\) for which

\[
 \Pr\{\|f_n-f_0\|_* > b_n(\delta/32)\}\le\delta/32.
                                                               \tag{8}
\]

The center is neither stored nor computed. Intersect (8)'s good event
with the physical bounds and the training-noise/perturbation bounds in
the bridge. At sufficiently large width the resulting common event
\(A\) has \(\Pr(A^c)\le\delta/16\), by allocating the inherited
physical-good confidence and the explicit vanishing noise failures
within the remaining \(\delta/32\).

For every tape in \(A\), every sphere query and every admissible time,
the appended row-query law has a coupling to the actual dense prediction
with error at most \(1/(4n)\), except on a fresh-query failure at most
\(1/8\), uniformly **conditional on the complete training tape**.
This is the bridge's stronger conditional statement. Unconditional
fixed-query coupling alone would be insufficient after conditioning on
the learned state.

The conditional bad-event probabilities
\(\Pr(A^c\mid C_{\le j})\) form a nonnegative martingale over the
finite nested prefixes. The elementary maximal inequality, with a final
proof-only step revealing \(A\), shows that with probability at least
\(1-4\Pr(A^c)\ge1-\delta/4\), the actual tape lies in \(A\) and
every prefix posterior assigns it bad-event mass at most \(1/4\).

On that single event every posterior query law, for every prefix and
every sphere/time query, has mass at least \(5/8\) within
\(b_n(\delta/32)+1/(4n)\) of \(f_0\). A deterministic
smoothed-CDF evaluator of error at most \(1/16\), transition width
at most \(1/(4n)\), and final bisection bracket at most \(1/(2n)\)
therefore gives (2). The additional \(b_n\) is the actual reference's
distance from \(f_0\). Atoms, flat distribution functions, and the
endpoint cause no change in this argument.

No sphere net is retained or used in this transfer. No uncountable union
of per-query exceptional events is taken. Here is a common posterior
kernel that makes that assertion precise. First sample the uncapped iid
row packets with the scalar-prefix likelihood (6). Recover the scalar
noise marks from (3), and reconstruct the original, unsmoothed noisy
matrix history only through the current checkpoint, chronologically from
those packets. Sample initialized
matrices from their explicit Gaussian posterior given that original
observable history. Past raw matrix noises are then the observed answer
minus its matrix action, divided by their nonzero noise scale; extend
future raw noises and scalar marks independently. This defines one full
training-tape posterior before specifying a test point.

Given that tape, a passive query uses fresh raw noises. Whiten its answers
using the original observable-history Gaussian covariance, and feed the
same innovations into the scalar-perturbed query circuit. This is the
coupling used in the physical bridge. Conditional on the original
observable prefix, these innovations have the iid Gaussian law used by
the row representation; they need not have that law conditional on a
full tape. The enlarged deterministic innovation caps in the bridge
cover the latter case. Integrating this common kernel gives exactly the
fixed-prefix Fourier query law for every query parameter. Thus one good
tape and one posterior kernel control the inequality for every sphere
point and time. No independence from unused future training innovations
is needed.

## 5. Denominators, quantization and counted workspace

For a prefix of length \(j\), its ideal summary lies in a box of
volume at most \((2B+2)^j\), except for a small explicit Gaussian
tail. Its density \(p_j\) obeys

\[
 \Pr\left\{C_{\le j}\text{ in that box},\quad
      p_j(C_{\le j})<\frac{\rho}{P(2B+2)^j}\right\}
          \le\frac\rho P.                                \tag{9}
\]

This is the integral of a density over the indicated set. Summing over
the finite prefixes, with \(\rho=\delta/4\), gives simultaneous
lower bounds outside probability \(\delta/4\), plus their negligible
box tails. Their logarithmic reciprocals are polynomial in
\(P,\log B,\log(P/\delta)\), not in \(n\).

The conditional Fourier proof supplies global Lipschitz bounds for both
the density and its bounded-test numerator. Their logarithms are
polynomial in the history size and in the logarithms of the noise,
range and instruction-sensitivity bounds. Hence retaining the history
to \(\exp[-\operatorname{poly}(R,\log(en),\log(1/\delta))]\)
accuracy keeps every required CDF evaluation within its fixed budget.
The density statement is applied to the ideal continuous state; the
rounded state is handled by this continuity estimate, not assigned a
fictitious continuous density.

The implementation is defined outside the success event as well. Return
zero on a flagged preprocessing overflow or a state outside its
prescribed box. For the prefix of length \(j\), put locally
\(d_j=\rho/[P(2B+2)^j]\) and compute its density to absolute error
less than \(d_j/8\). If the computed denominator is below
\(d_j/4\), return zero;
otherwise use the ratio. On the simultaneous good-density event, the
retained-state accuracy keeps the true nearby density above one half of
\(d_j\), so the guard is inactive. The actual training noise scale
\(\eta\) is held fixed throughout decoding; it is not replaced by
a newly chosen smoothing of the retained history.

Positive weighted acquisition never divides by a selection weight.
Round packet marks, weights, noise marks and update arithmetic to a
correspondingly finer grid. The explicit finite-program recurrence then
gives the required history error simultaneously at every prefix.
Tiny selection weights therefore do not hide an arbitrary number of
bits. A weight may be rounded to zero, with its controlled contribution
absorbed in the same error budget.

For a completely finite selection algorithm, quantize the realized
moment vectors before positive convex elimination. An error
\(\epsilon\) per vector gives at most \(2\epsilon\) moment
defect, and hence at most \(2\epsilon P(1+\Lambda)^P\) prefix
defect, where \(\Lambda\) is the declared row-function Lipschitz
bound. Rational elimination or finite support enumeration chooses at
most \(P+1\) packets. Determinant bounds give polynomial bit lengths
for their rational weights. The complete
[finite-precision selection proof](FINITE_PRECISION_SOURCE_SELECTION.md)
avoids exact-rank decisions on transcendental moments.

All global bounds and their logarithmic sensitivities are polynomial
compositions in \(R\), \(\log(en)\), and the fixed-input parameters.
The row dimension is \(d+O(R)\), the summary count is \(O(R^2)\),
and the largest conditioning matrix has dimension \(O(R^2)\).
The Fourier evaluator uses a universal polynomial in those quantities
and the requested logarithmic precision, including the row-function
subroutine's workspace. Combining these fixed-degree polynomials with
Section 2's program count gives an absolute integer \(k\) in the memory
claim; it is not a dimension- or depth-dependent exponent in disguise.

The small scalar-matrix routines are implemented by the explicit
[counted spectral algorithms](SMALL_MATRIX_FUNCTION_EVALUATION.md).
Gapped inverses and square roots use truncated Neumann and binomial
series of a fixed exactly stored contraction. The error of rounded
powers grows linearly in the power index, and the accumulated series
error quadratically, so precision needs only the logarithm of the
possibly enormous degree. A PSD projection uses a buffered approximation
to \((A+\sqrt{A^2+hI})/2\); its conservative radial cap preserves
positivity. Sylvester solves include their full small Kronecker arrays.
The common operand grid and half-gap margins control nested calls
without repeated precision doubling. All scratch is counted.
Activations and their first derivatives use the original evaluation
primitives, or the stated counted precision interface.

Allocate the remaining failure budget to box tails and source/precision
events. The preceding probability margins leave total failure below
\(\delta\). The sufficient width remains unquantified because the
original good-event threshold does.

## 6. Qualifications

* This is a new weighted response-circuit model with a posterior decoder,
  not the earlier tiny network with a simple forward pass.
* It stores a finite compressed history of scalar response moments. It
  does not promise a memoryless Markov description in only current layer
  activations.
* Preprocessing may execute the finite dense source computation and may
  be expensive in memory and time. No preprocessing improvement is proved.
* Decoding may be extremely slow. The result establishes an absolute
  logarithmic storage/workspace exponent, not practical inference time or
  the earlier exponent five.
* Fixed-problem prefactors and sufficient width may be very large. No
  sharp or polynomial \(m,d,L,\gamma^{-1}\) prefactor is asserted.
* The comparison is with the existing dense-self-variability **upper
  certificate**. It is not a matched-reference \(1/n\) theorem or a
  lower-bound-sharp comparison in every parameter.

## 7. Proof dependencies and audit status

The complete chain is:

1. [Short causal physical program](SHORT_CAUSAL_TRAINING_PROGRAM.md),
   with its corrected independent check.
2. [Physical/noisy bridge](PHYSICAL_NOISY_PROGRAM_BRIDGE.md), with its
   corrected independent check, including enlarged innovation-moment caps.
3. [Exact noisy two-orientation law](NOISY_TWO_ORIENTATION_TRANSCRIPT.md),
   with explicit regularized covariance factor.
4. [Scalar-history acquisition](NOISY_SCALAR_HISTORY_ACQUISITION.md),
   and [constructive finite-precision selection](FINITE_PRECISION_SOURCE_SELECTION.md).
5. [Conditional Fourier evaluation](FOURIER_ROW_PROGRAM_EVALUATION.md),
   especially fixed-prefix Section 8.
6. [All-prefix robust center](CONDITIONAL_PREFIX_CENTER.md).
7. [Counted small-matrix evaluation](SMALL_MATRIX_FUNCTION_EVALUATION.md).

The lead read the complete component arguments. A fresh isolated
[full-chain reconstruction](CURRENT_STATE_DECODER_FULL_REVIEW.md)
passed the supplemented construction under the inherited certificates
and stated numerical interfaces. It required the source-selection and
small-matrix supplements, corrected caps, denominator fallback and
parameterwise-bound qualification incorporated above. A separate
[Fourier numerical check](FOURIER_ROW_PROGRAM_NUMERICAL_CHECK.md)
reconstructed the conditional density, truncation, precision and
workspace argument. These are internal mathematical checks, not formal
verification or authorization to promote the theorem into the book.
