# Check of the Gaussian-proxy uniform convergence theorem

28 September 2026. Bounded proof check requested by the coordinator. The
assignment was to verify Sections 2--4 of
`GENERAL_GAUSSIAN_TRANSPORT.md` against the complete relevant maintained
C.1--C.2 proof, with attention to the Frobenius upgrade, proxy residual,
all-order/all-width quantifiers, and the conditional arbitrary-horizon
extension. The `solve-math-rigorously` skill was applied. No new route,
experiment, literature search, other study, or other review was used.

**Verdict: PASS for the stated theorem and its stated conditional
extension.** I found no substantive gap in the qualitative convergence
uniform over all finite widths, or in the width-first subpower-loss rate.
The arbitrary-horizon conclusion requires the displayed dense Gaussian
carrier-tail premise; it is not unconditional from strong population
existence alone. The argument proves neither an all-width `C/P` rate nor
a width-uniform second-moment estimate. This is a bounded internal proof
check, not a promotion review.

The checked candidate file has SHA-256
`34ede4c5b082760856bb8ba426d349adad8e0008d228e1bb76f7a9c83a1afb6e`.
The maintained source hashes at the check were
`3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd`
for `docs/03-local-population.qmd`, and
`a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92`
for `docs/02-gaussian-reuse.qmd`.

## 1. Sources and exact checked claim

I read all of maintained C.1 and C.2, including C.1's preliminary ball,
one-reference cutoff, common-space construction, proxy construction,
finite approximation and initialization-perturbation passage, and
C.2's complete causal source-response induction and cap selection. I
also read the complete A.1--A.2 fixed-program specializations. The
previously assigned canonical model and complete old-clock proof supply
the finite-width forced equation and fixed-width convergence input;
the assigned old-clock route supplies the order-independent physical
bounds and `C/P` accumulated defect. No trained finite-network tail
statement was inserted.

With the candidate's sum distance

\[
 d_n(\theta,\vartheta)
 =\frac{\|W^{(1)}-V^{(1)}\|_F}{\sqrt n}
  +\sum_{\ell=2}^L\|W^{(\ell)}-V^{(\ell)}\|_F
  +\frac{\|w-v\|_2}{\sqrt n},
\]

and `e_(n,P)=sup_(t<=T) d_n(theta_hat_(n,P),theta_n)`, the checked
local statement is

\[
 \lim_{P_0\to\infty}\sup_{n\ge1}
  \Pr\!\left\{\sup_{P\ge P_0}e_{n,P}>\epsilon\right\}=0
  \qquad(\epsilon>0).
 \tag{1}
\]

The memory orders are positive integers. At each width the dense flow
and all memory orders share their initial arrays. No common coupling
between different widths is needed for (1).

The quantitative companion has width taken first: for fixed `P_0`,

\[
 \Pr\!\left\{\sup_{P\ge P_0}e_{n,P}>B(P_0)+\zeta\right\}
       \longrightarrow0\quad(n\to\infty),\qquad\zeta>0,
\]

where `B(P_0)=C_1 P_0^-1 exp(C_2 sqrt(log(e+P_0)))`.

## 2. Upgrade to full first rows and hidden Frobenius differences

C.1's metric uses first preactivation fields and hidden operator
differences. The stronger metric in the candidate is nevertheless
supported by the actual velocity formulas.

For finite vectors,

\[
 \left\|\frac{uv^T-u'v'^T}{n}\right\|_F
 \le \frac{\|u-u'\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
       +\frac{\|u'\|_2}{\sqrt n}\frac{\|v-v'\|_2}{\sqrt n}.
 \tag{2}
\]

This is the triangle inequality after writing the difference as
`(u-u')v^T+u'(v-v')^T`, and the equality
`||ab^T||_F=||a||_2||b||_2`. Each hidden velocity is a finite weighted
sum of these terms. Thus the same RMS response difference bound that
C.1 used for operator-norm velocities gives Frobenius-norm velocities.
The forward recurrence remains valid because an operator difference is
at most its Frobenius norm. No Frobenius bound for an initialized
Gaussian matrix is used.

The first-row velocity is

\[
 F_1=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
 \qquad v_a=x_a/\sqrt d.
\]

Its normalized row-Frobenius difference is bounded directly by the
backward RMS differences, residual differences and `max_a ||v_a||`.
This recovers the entire first matrix, without attempting to invert
the sample Gram or recover a row from its observed preactivations.
The proxy row can be reconstructed by this same update from the same
initialized row. Any component perpendicular to the input span remains
the shared initialized component. Adding the finite `d`-coordinate root
tuple to a fixed Gaussian program is permitted by A.1.

Combining the forward recursion, the one-reference gate cutoff and
the descending backward recursion therefore proves

\[
 \|F_n(\theta)-F_n(\vartheta)\|_{\rm sum}
 \le C(1+R)d_n(\theta,\vartheta)+C\mathcal T_R(\vartheta).
 \tag{3}
\]

Only the reference state's full carriers occur in the tail. At each
backward layer the previous response difference is multiplied by a
bounded operator and gate; the new gate-cutoff term is added. Hence
the coefficient is affine in `R`, with no factor `R^L`.

The same argument holds in population spaces with hidden
Hilbert--Schmidt *increments*. The initialized bounded operators cancel
between paths on the same action spaces. Their absolute
Hilbert--Schmidt norm is neither required nor generally finite.

## 3. The fixed-program proxy has a vanishing vector-field residual

Fix the reference mesh before taking width to infinity. At that mesh,
all population residuals and scalar contractions are deterministic
numbers, and the oracle consists of finitely many Gaussian actions,
their true transposes, and the allowed coordinate instructions. This
is exactly the finite computation to which A.1--A.2 and C.1 apply.

Construct the proxy hidden parameters as the initialized matrices plus
their finite rank sums. Applying such a proxy to an oracle node differs
from the prescribed action only by a finite sum of terms

\[
 a_n\left(\frac{b_n^Tc_n}{n}-\mathbb E[BC]\right).
\]

At fixed mesh the scalar tends to zero in probability and the RMS of
`a_n` is bounded in probability. A finite sum of these terms tends to
zero in RMS. The transpose case uses exactly the corresponding
backward contractions of the same matrix.

The forward proxy fields consequently agree with oracle fields in
RMS. Backward consistency is obtained by a descending cutoff argument:
keep a cutoff fixed, use the preceding forward/action consistency, and
then remove the cutoff using the oracle reference tails. It does not
follow from an unjustified global `L2` Lipschitz estimate for a gate
times a carrier. C.1 supplies this precise cutoff step.

It follows that residuals recomputed from proxy parameters agree with
their deterministic oracle values. For a hidden velocity, (2) then
converts the response/residual consistency into Frobenius consistency.
The first-row and readout cases are direct finite sums. Therefore the
assigned proxy grid velocity differs from `F_n` evaluated at its
recomputed proxy grid state by a random quantity tending to zero in
probability, uniformly over the finitely many cells.

There is no requirement for convergence uniform in the number of
cells. The mesh remains fixed throughout this width limit.

The initial small Gaussian readout needs no extension of a fixed-root
program theorem to an unspecified triangular array: choose the proxy's
readout to be exactly zero and place the actual readout RMS in the
initial discrepancy. Under the stated canonical scaling this
discrepancy tends to zero in probability. C.1 explicitly allows this
vanishing initialization perturbation.

### Hard cutoffs need no atomlessness assumption

A.1 gives continuous quadratic-growth measurements. A sharp tail
indicator should not be passed through this theorem by claiming that
it is continuous. This is only a presentation detail in the candidate,
because its required *upper bound* follows from a continuous majorant.

Choose continuous `chi_R` equal to zero on `[-R/2,R/2]`, equal to one
outside `[-R,R]`, and taking values in `[0,1]`. Then

\[
 x^2\mathbf1_{|x|>R}\le x^2\chi_R(x)
                       \le x^2\mathbf1_{|x|>R/2}.
\]

The middle function is continuous with quadratic growth, so empirical
averages converge by A.1. C.2 bounds the limiting right side by a
Gaussian tail. This gives the required empirical RMS-tail upper bound
after changing constants, even if the limiting carrier has atoms.
The proxy/oracle transfer uses C.1's elementary inequality

\[
 \|v\mathbf1_{|v|>2R}\|_2/\sqrt n
 \le2\|v-u\|_2/\sqrt n
       +2\|u\mathbf1_{|u|>R}\|_2/\sqrt n.
\]

Thus the reference tails used in the candidate are fully justified.
An explicit mention of the continuous majorant would improve the
presentation but does not require a new hypothesis or change the
theorem.

## 4. A single event controls every closure order

Let `q_n^Delta(t)` be the affine proxy and `v_n,k^Delta` its assigned
velocity on cell `k`. On initialized-operator/readout events with
probability tending to one, all actual closure paths have uniform
physical bounds and

\[
 \int_0^T\|E_{n,P}(s)\|_{\rm sum}ds\le C/P
 \quad\hbox{for every positive integer }P.
\]

The proxy's speed and physical bounds also have deterministic limiting
upper bounds independent of mesh; at a fixed mesh their finite errors
are absorbed into its good event. Using the preceding proxy grid
state as reference in (3), its distance from the current closure state
is bounded by the current interpolant distance plus `C Delta`.
The integrated comparison is therefore

\[
 \begin{split}
 d_n(\widehat\theta_{n,P}(t),q_n^\Delta(t))
 \le{}&a_n+C/P\\
 &+\int_0^t C(1+R)
       d_n(\widehat\theta_{n,P}(s),q_n^\Delta(s))ds\\
 &+C(1+R)\Delta+C e^{-cR^2}+b_{n,R,\Delta},
 \end{split}
\]

where `a_n` is the initial discrepancy and
`b_(n,R,Delta)->0` in probability at fixed `R,Delta`. These errors
depend on the fixed proxy and initial arrays, not on memory order.
The integrating factor therefore gives one pathwise inequality
simultaneously for every `P`, on this one good event. Applying the
same argument to the dense finite flow removes the `C/P` term.
The triangle inequality proves the candidate's central bound

\[
 \sup_{P\ge P_0}e_{n,P}
 \le C e^{C(1+R)T}
    [P_0^{-1}+(1+R)\Delta+e^{-cR^2}+o_{\Pr}(1)].
 \tag{4}
\]

No countable union of separate order-dependent failure events is
needed. This is the essential reason the supremum over all larger
orders is valid.

## 5. Quantifier audit

For the width-first rate, fix `P_0` and choose
`R=max(1,sqrt(c^-1 log(e+P_0)))`, changing constants harmlessly.
Then `e^-cR^2<=C/P_0`. For any prescribed positive threshold margin
`zeta`, choose a sufficiently fine fixed mesh to make its contribution
in (4) smaller than a portion of `zeta`. The width limit makes the
remaining proxy errors and bad-event probability vanish. This proves
the asserted probability limit with `B(P_0)+zeta`. No mesh or
fixed-program convergence estimate uniform in `P_0` was used.

For qualitative uniformity over widths, fix error tolerance `epsilon`
and probability tolerance `q`. Choose, in order:

1. A finite `R` that makes the exponentially amplified tail small.
2. A fixed fine mesh that makes the mesh term small.
3. An integer `N` such that every width `n>=N` has proxy/initialization
   failure probability at most `q` and sufficiently small proxy error.
4. A memory threshold `P_0` making the forcing term small.

Because `o_Pr(1)` means convergence along the full width sequence,
the choice in step 3 controls every `n>=N`. Because that error is
independent of `P`, the later choice of `P_0` is legitimate. The
result is a common probability bound for every width `n>=N` and
every order `P>=P_0`.

At each of the finitely many widths `n<N`, the complete fixed-width
tanh theorem and global closure continuation give a finite random
constant `H_n` such that `e_(n,P)<=H_n/P` for all orders. One may
choose `H_n` from the explicit physical bounds and the finite
dimensional derivative supremum on their compact parameter ball, so
it is measurable and finite almost surely. Consequently

\[
 \Pr\{\sup_{P\ge P_0}e_{n,P}>\epsilon\}
 \le\Pr\{H_n>\epsilon P_0\}\longrightarrow0.
\]

Increasing `P_0` handles this finite list simultaneously and preserves
the already proved large-width estimate. Since `q` was arbitrary,
(1) follows. The index `N` may depend badly on both tolerances; this
does not obstruct qualitative uniformity, and does prevent extracting
an all-width numerical rate from this argument.

## 6. Conditional arbitrary-horizon passage

The dense premise is a strong canonical population solution through
the prescribed finite `T`, together with

\[
 \sup_{t\le T}\max_{\ell,a}
       \mathbb E\exp(c_T|c_{\ell,a}^D(t)|^2)<\infty.
 \tag{5}
\]

This is sufficient as written. It is stronger than ordinary strong
existence, and the candidate correctly keeps that distinction.

First, the dense hidden right sides are continuous in
Hilbert--Schmidt norm. The strong operator/field topology gives
continuous forward fields. For a backward product, write
`phi'(Z_j)P_j-phi'(Z)P` as a bounded multiplier times `P_j-P`
plus `[phi'(Z_j)-phi'(Z)]P`; the latter tends to zero in `L2` by
boundedness and truncation against the fixed integrable variable
`P^2`. Descending in layers gives backward continuity. The
rank-one identity then gives Hilbert--Schmidt continuity of the
hidden velocity. Integrating its continuous rank-one right side
shows that each learned dense increment is a Hilbert--Schmidt path,
with the same operator-valued integral as in the strong equation.

Next compare population Euler directly to this actual dense solution,
using the latter as the one-reference state. Stop Euler in a fixed
larger physical ball. Its cell speed is bounded on that ball, so
(3), with tails from (5), gives

\[
 \sup_{t\le T}d(\theta^\Delta(t),\theta^D(t))
 \le C e^{C(1+R)T}[(1+R)\Delta+e^{-cR^2}].
 \tag{6}
\]

At fixed `R` take the mesh to zero; next let `R` increase. The
right side vanishes in this order. Making it smaller than the
fixed stopping margin also rules out the stopped exit. This
constructs strong Euler approximation throughout `[0,T]` without
assuming mesh-uniform response bounds at that horizon.

The forward/backward maps are uniformly continuous along the compact
dense reference path in the sense needed here. Equivalently, apply
the descending cutoff estimate with the dense reference tails,
then send the state discrepancy to zero at fixed cutoff and remove
the cutoff. Thus

\[
 q_\Delta:=\sup_{t\le T}\max_{\ell,a}
       \|c_{\ell,a}^\Delta(t)-c_{\ell,a}^D(t)\|_{L^2}
       \longrightarrow0.
\]

Euler grid tails are at most `2q_Delta` plus a shifted dense tail.
For each fixed mesh, the original finite-program theorem still
applies: its transcript may be long, but it is finite and its
deterministic coefficients are fixed. Its proxy errors vanish in
the width limit. Therefore (4) acquires only an extra deterministic
`C q_Delta` term inside the brackets. The correct order is

\[
 n\to\infty\text{ at fixed }(R,\Delta),\qquad
 \Delta\to0\text{ at fixed }R,
\]

followed, for qualitative convergence, by increasing `R`. The
factor `exp(CRT)` causes no difficulty for `q_Delta`, since `R`
is fixed during its mesh limit. No rate for `q_Delta` is required.
Both conclusions from Section 5 consequently extend under (5).

The candidate's source representation with bounded deterministic
response-measure variation does imply (5): each initialized carrier
is a Gaussian variable of uniformly bounded variance plus a
uniformly bounded remainder; the learned adjoint carrier is
pointwise bounded by the exact dense history formula; and the
zero-initial-readout path is pointwise bounded by the integrated
residual. Independence between the Gaussian and bounded remainder
is unnecessary because `(eta+b)^2<=2eta^2+2b^2`. This sufficient
condition is stated as a premise, not claimed to follow globally
from maintained C.2. The local C.2 proof supplies it only on its
own deterministic local interval.

## 7. Final classification

The Frobenius strengthening, proxy residual calculation,
simultaneous memory-order control, finite-small-width completion,
and dense-only arbitrary-horizon extension all pass the check.
The only suggested clarification is to make the continuous
majorant behind empirical sharp-tail bounds explicit. It changes
neither assumptions nor conclusion.

The supported result is a qualitative approximation theorem for
the original fully autonomous closure at arbitrary fixed depth
and arbitrary fixed correlated data: unconditional locally, and
conditional on the stated dense Gaussian carrier regularity on
a prescribed longer horizon. The probability supremum over all
finite widths is supported. An all-width `C/P` rate and an
unconditional arbitrary-time extension remain outside this proof.
