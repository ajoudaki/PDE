# Round queries using physical prediction regularity

2026-10-06. Lead-author improvement to the checked smaller decoder.
This note reduces the external grid and the number of median blocks.
It does not reduce the statistical rows per block or establish
logarithmic query work. No experiment or promotion.

## 1. The algorithm changes at its external interface

Keep the complete setup, accuracy, parameter definitions and width gates
of `FAST_COMPOSITION.md`, whose checked version has SHA-256
`77f5deaffcd7133e6bafb0c1b2e8cf216399bbf787503812e8667ea2e5da53cc`.
In particular its source field count R and local numerical certificate
Theta obey

\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)^2 Z^{5/2},
 \qquad \Theta\le C\beta^{102L}(1+m/\gamma)Z.
 \tag{1}
\]

The actual certificates have Theta <= R. They include all numerical
floor and accuracy logarithms. Constants in this note are universal.
The query core still uses w=CR Theta bits, not local precision.

Change the decoder as follows. Given an unseen unit input v=x/sqrt(d),
replace it by a nearby member of a fixed finite sphere grid. Within the
current source patch, similarly replace its fractional time by a nearby
grid value in that same patch. Evaluate the existing finite decoder at
this coded query and return that result. The current patch's coefficients
are already acquired; querying does not request the next patch or advance
training. After the terminal patch, use the existing frozen endpoint.

The new grid is chosen from regularity of the **dense physical prediction**,
not from the global sensitivity of the row interpreter. No continuity of
the implemented rounded decoder is assumed or needed.

## 2. An explicit physical Lipschitz bound

On the inherited operator/readout event, the initialized and learned first
matrix satisfy ||A||_op/sqrt(n) <= C, hidden operator norms are at most
ten, and ||w||_2/sqrt(n) <= S H_L, where S=16Ym/gamma <= 1 and
H_L <= beta^(3L). These are the same stopped physical bounds used in
`PHYSICAL_PARAMETER_ACCOUNTING.md`; n is sufficiently large to include
the initialized first-matrix event with n >= d.

For two unit inputs, successively subtracting forward activations gives

\[
 \|h^{(L)}(v)-h^{(L)}(v')\|_2/\sqrt n
 \le C\beta^{2L}\|v-v'\|_2.
\]

Indeed the first-layer coefficient is C beta and each following one is
10 beta <= beta^2. Cauchy--Schwarz in the normalized readout consequently
gives

\[
 |f_n(t,v)-f_n(t,v')|/Y
 \le\beta^{20L}(1+m/\gamma)\|v-v'\|_2,
 \tag{2}
\]

with ample numerical slack. This bound is for the true dense trajectory,
including the fitted limit, and does not use a history-Gram inverse.

For time, use normalized time tau=(gamma/m)t and the physical displacement
norm of the source. Accounting (8) bounds the physical vector field by
Y beta^(12L) and its query prediction sensitivity by beta^(8L). Thus

\[
 |\partial_\tau f_n(\tau m/\gamma,v)|/Y
 \le\beta^{20L}(m/\gamma)
 \le\beta^{20L}(1+m/\gamma).
 \tag{3}
\]

These are bounds on the physical reference, not on a clipped extrapolation.
The clipping is inactive on that event. Use them through the finite
source horizon; its inherited fitting-tail estimate supplies the endpoint.
The source construction and the independent reference receive their
usual separate confidence allocations.

## 3. Finite external codes without an R multiplier

Reserve the same normalized deterministic allowance epsilon=n^(-10)
already used for external rounding in `FAST_UNIFORM_QUERY.md`. Choose
a dyadic mesh fine enough that the sum of the errors in (2)--(3) is at
most epsilon/8. A sufficient precision exponent is

\[
 p\le C\{\log(en)+L\log\beta+\log(1+m/\gamma)+\log(d+2)
                              +\log(H+2)\}\le C\Theta,
 \tag{4}
\]

where H is the number of source patches. The displayed bound refers to
a prescribed sufficient choice, not an arbitrary p satisfying only an
upper bound.

For a concrete sphere grid, prescribe the coordinate lattice with step
2^(-p-6-ceil(log2(d+1))). Obtain a lattice vector z approximating v
with ||z-v||_2 <= 2^(-p-3), and take the grid point z/||z||_2.
Then ||z||_2 >= 1/2 and the distance to v is at most 2^(-p-2).
The grid code is z; normalization is evaluated to the existing internal
word precision w, using its counted square-root/division routines. The
mathematical grid point is on the sphere exactly. Its internal finite
evaluation error belongs to the existing fixed-context numerical allowance,
not to the coarser grid mesh. The code count is at most
exp(Cd[p+log(d+2)]). Approximate input access may choose any qualifying
code; no exact tie decision is required.

Within a current patch, use a certified dyadic lower approximation to its
fraction, accurate to one mesh width, then round that finite value down
on the prescribed mesh and clamp to [0,1]. This requires no exact floor test on an arbitrary
real; the fraction changes by at most two mesh widths. Both
the exact queried time and its code remain in that patch. With the known
patch length at most one, (3) pays for the time error. Include the patch
label and both boundary codes. Ambiguous finite input times at a boundary
use only an already acquired adjacent certified patch as already allowed
by the source interface; both approximate the same physical value.
No unavailable future coefficients are needed. The frozen endpoint is one additional
code. The total external code count therefore satisfies

\[
 \log|\mathcal A|\le C(d+1)\Theta.                    \tag{5}
\]

Here log H and data/confidence logarithms already belong to Theta.
The code set is never enumerated or retained.

The final transfer is elementary. If a decoder is accurate at every code
and the physical reference is Lipschitz, then for an arbitrary input/time,
subtract the decoder's value at its chosen code from the physical value
there, then add the physical change to the original input/time. Equations
(2)--(4) bound only that second difference. There is no difference of
decoder values at two nearby inputs to estimate. The existing external-
rounding allowance already pays epsilon/8, so this does not enlarge the
inherited dense-pair upper-certificate scale or change the time norm.

## 4. Revised uniform-query and cost counts

Apply `FAST_UNIFORM_QUERY.md` at these codes. Its reachable-context
argument still conditions on previous stage seeds and tests the one
context reached from each external code; it does not form a grid over
all intermediate response coordinates. The source law, information bound,
posterior/prior statistical block length s, separate stage seeds, and
fixed-context row calculations are unchanged. Only (5) replaces the old
external entropy C(d+1)R Theta.

The sufficient odd median block count is now

\[
 J\le C(d+1)\Theta,
 \qquad w=CR\Theta,
 \qquad A\le CR^2\Theta.                              \tag{6}
\]

In (6), A is the internal generator block parameter. Directly,
A=C(Dw+log|mathcal A|+log(N+2)) <= CR^2 Theta, since D <= CR,
d <= R, and log(N+2) <= C Theta for the full stream length N. The
generator's stage-seed length remains C R^2 Theta^2. The common Gaussian
tail event, finite inverse-CDF implementation, and one-pass median tests
are unchanged. The independent stage count is O(L+1).

Use the already checked coordinate-at-a-time median schedule, always
holding its incoming context and prepared coefficients fixed until all
coordinates are completed. One coordinate now stores Jw bits, at most
C(d+1)R Theta^2. There are at most CR coordinate passes. The per-packet
work bound remains CR^5 Theta^4. Consequently

\[
 \begin{split}
 \text{peak query bits}
 &\le C\{R^3\Theta+(L+1)R^2\Theta^2
                           +(d+1)R\Theta^2\},\\
 \text{query work}
 &\le C(L+1)\{s(d+1)R^6\Theta^5+R^7\Theta^3\},\\
 \text{activation/data calls}
 &\le C(L+1)\{s(d+1)R^2\Theta+R^2\}.
 \end{split}                                          \tag{7}
\]

Sorting the one-coordinate block means is smaller than the first work
term for s >= 1; stage preparation is the second term and is reused.
The internal word precision and external evaluator costs are unchanged.
Initialization, acquisition updates, and retained storage are unchanged.

Substitution of (1) and s <= n gives the explicit work allowance

\[
 C\beta^{1720L}\left[
 n(m+d+2)^7(1+m/\gamma)^{17}Z^{20}
 +(m+d+2)^7(1+m/\gamma)^{17}Z^{41/2}\right].             \tag{8}
\]

For the stream term the exact activation power before slack is 1717L:
6(201L)+5(102L)+L. The second term needs 1714L before slack.
Do not drop that second term merely by calling n sufficiently large;
it is displayed. Alternatively, since sqrt(Z) need not be bounded by
n at fixed small widths with extreme supplied parameters, retaining the
sum is the uniform parameter-explicit statement. For fixed parameters,
the n dependence is O(n log^20(en)+log^(41/2)(en)).

The separate evaluator count is bounded by
C n beta^(505L)(m+d+2)^3(1+m/gamma)^5 Z^6 plus the lower preparation
term, at the same CR Theta precision. All retained descriptions,
actual evaluator scratch/work, certificate acquisition and output
costs remain explicit additions.

## 5. Status

The lemma changes the external quantization algorithm. It does not claim
that the old high-sensitivity row circuit became Lipschitz at local
precision, or that few training moments determine every unseen moment.
The statistical block s is unchanged and still scales with dense width,
up to its explicit logarithmic and fixed-parameter factors. This is a
smaller complete-query bound conditional on the checked construction,
not the requested polylogarithmic-time query theorem. A bounded
reconstruction is required before substituting (8) into the headline table.
