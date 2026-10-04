# Complete internal reconstruction of the two-input compression chain

2026-10-03. Scoped check requested by the coordinating task. This is an
internal collaborative reconstruction, not an independent promotion review
and not a change to the maintained scientific book. No experiment, Git
operation, source edit, or other reviewer's verdict was used. Canonical
notation, rigorous-proof, and adversarial-audit instructions were applied.

**Verdict:** no blocking mathematical error was found in the stated
two-input theorem and its supplied source proof. The construction, stored
coordinate bound, weighted feedback comparison, and finite-width feature
motion certificate reconstruct. The source theorem was read completely;
its real cavity input, short vertical continuation, stopped Gaussian grids,
cap closure, and query ordering were also reconstructed below. This check
does not replace independent promotion review or user approval.

## 1. Frozen inputs and coverage

The checked versions are:

| Input | Complete coverage | SHA-256 |
|---|---:|---|
| `TWO_INPUT_CANONICAL_COMPRESSION.md` | 492 lines, Sections 1--9 | `8ea773b11d104ac5fda847968cbe9e94f59afc2f28020214da157cf612fa77e0` |
| `TWO_INPUT_STABLE_GEOMETRY.md` | 415 lines, Sections 1--5 | `93040bef724cfef765aa26d961c996297e13d67b31dcbc3fc51876ac1212c820` |
| `TWO_INPUT_COMPLEX_SOURCE.md` | 527 lines, Sections 1--6 | `96ce9f5f1966b66082977664efcaa191d137ca646802f9d0984239bb7c4bacf9` |

The relevant one-input inverse-coordinate proof had already been read
completely in `COMPLEX_ACTIVITY_ROUTE.md`. The current checker previously
derived the real feedback comparison independently in
`TWO_INPUT_FEEDBACK_STABILITY.md`, before exposure to the stable-geometry
proof. This prior involvement is disclosed because it prevents treating
the present check as an isolated promotion review. No other new check or
verdict file was read.

The target is the exact canonical finite dense network with two orthogonal
inputs, fixed small real labels, and mobilities `(n,1,n)`. The smaller
weighted network is permitted to have selected, non-Gaussian initialization.
The resource claim counts moving and fixed stored real coordinates after
setup; it excludes setup work, temporary storage, and precision. All these
boundaries are necessary to the asserted conclusion and are stated in the
candidate.

## 2. Exact dynamics, fitting, and residual feedback

The loss `sum_a(f_a-y_a)^2/2` gives the displayed physical equations with
factor `2/m=1`. For orthogonal inputs the coordinate change
`u_a=Psi(Ae_a)`, where `Psi'=cosh^2`, gives exactly
`u_dot_a=c_a B^*delta_a`. It removes diagonal carrier factors from
the derivative of the residual-free state field. It does not assert that
the two residual-free fields commute.

The weighted inner products and Hilbert--Schmidt norm give the identities
`||B^*||=||B||` and
`||delta h^T D_1||_HS=||delta||_{D_2}||h||_{D_1}`. Thus the
small-total-activity estimates have constants independent of the minimum
mass. Differentiating the predictions yields the sum of the top Gram,
a Gram of rank-one mixer gradients, and a nonnegative diagonal
first-layer term. The fixed initial top-Gram gap remains positive for
small labels, and the first-exit argument gives exponential residual
decay, finite total activity, and convergence of both networks.

For the feedback comparison, if `p=int(c_C-c_n)dt`, integration by parts
gives `Delta state=V_0 p+O(S sup|p|+S sup||Delta state||+epsilon)`.
The observation remainder is explicitly
`N_a=w^T D_2(g_a-g_{a,0})`; its Lipschitz constant on the real tube
is `O(S)`. Hence

\[
 \dot p=-G_0p+\zeta,
 \qquad \sup|\zeta|
 \le CS(\sup|p|+\sup\|\Delta\text{state}\|)+C\epsilon.
\]

The Gram gap absorbs the small `S` terms uniformly in the physical-time
horizon. No derivative of the tangent kernel, bound on the carrier
maximum, or absolute-integrability estimate for the residual discrepancy
is needed. The small retained displacement `O(|y|epsilon)` in the
compression proof keeps the observation remainder Lipschitz constant
`O(|y|)` when `epsilon<=1`; the proof does not require this displacement
to remain `O(|y|^2)`.

The lower and upper deletion bounds retain normalization `n`. In the
ordinary `(u_1,u_2,H=sqrt(n)W,w)` norm they are respectively
`CY` and `C(Y^2+Y/sqrt(n))`. The cavity initial Gram losses are
`O(n^{-1/2})` and `O(n^{-1})`. The omitted Gaussian vector is
independent of each cavity because that cavity uses its own residuals.

## 3. Reconstruction of the complex-source input

The complex-source proof supplies precisely the source list required by
the compression note, including the paired fixed-mixer images. Its time
interval has length `T=B log(en/eta)`, while both strip radii are
`c/sqrt(log(en/eta))`. The following checks reconstruct its critical
logical steps.

1. The Gaussian initialization gives a fixed top-Gram gap for the
   orthogonal inputs. The lower tanh covariance concentrates near `qI_2`;
   conditional Gaussian upper rows then have tanh Gram near `nu I_2`.
   Continuity at the positive covariance and bounded-variable exponential
   concentration suffice. The operator, entry, initial coordinate, and
   first-layer RMS events have the asserted probability bounds.

2. Complex estimates are anchored at the real time `Re t`, followed by
   a short vertical segment. The algebraic residual kernel has bounded
   operator norm on a pole-safe operator/readout tube. Therefore residual
   growth on that segment costs only `exp(C r_0)`, preserving the real
   exponential decay in its anchor. This argument does not incorrectly
   use positive Hermitian damping along a complex-time contour and does
   not accumulate `exp(C T)`.

3. On the unnormalized comparison scale, the prediction difference has
   a factor `n^{-1/2}`. Multiplication by the residual-free state field,
   of size `O(sqrt(n))`, gives a fixed feedback Lipschitz constant.
   The direct deleted-column top input has Euclidean norm `O(1)` and
   appears with residual or readout factor `O(Y)`. The vertical comparison
   therefore remains `CY` for either cavity type. Finite differences use
   the convex strips of endpoint preactivations; they do not presume a
   pole-safe straight segment in parameter space.

4. The full stops use pole caps `b`, carrier cap `M=AY sqrt(ell)`,
   and forward-response cap `L=AY sqrt(ell)`. Cavity stops use doubled
   pole and carrier caps. The real-plus-vertical comparison gives pole
   discrepancies `CY` and carrier discrepancy `CY`, so, for fixed small
   labels and large width, a cavity cannot stop before the full system.
   This is applied only on common prefixes and then continued.

5. Each Gaussian source is defined on its own cavity's stopped domain.
   After conditioning on the retained initialization and the real first
   layer, the omitted column or row still has covariance `I/n`. The
   reference is zeroed when its retained operator or Gram conditions fail.
   Cavity source RMS is `CY`; the time derivative bound is
   `CY(1+YM)`. The stopped-domain grid has polynomial cardinality in
   `n,T,ell`, and interpolation error `CY n^{-5/2}` on the omitted
   vector norm event. Thus the union bound gives `CY sqrt(ell)`
   pairings without conditioning the Gaussian tail on a full-network
   stopping event.

6. Row reinsertion costs `C(Y+YM)` in the residual-free forward response.
   With `M=L=AY sqrt(ell)`, its cap ratio is `CY`, so fixed small
   labels close both carrier and forward-response caps. The actual time
   derivative has an additional residual factor, giving
   `max(|u_dot|+|z_dot|)<=CY^2 sqrt(ell)`. Vertical integration
   over radius `c/sqrt(ell)` closes the pole caps with strict margins.

7. Query first gates are controlled first, using the real coordinate
   maximum `C sqrt(ell)` and the training inverse-coordinate strip.
   Their residual-free time responses and angular derivatives have
   bounded RMS and polynomial derivative bounds. Independent row-cavity
   grids then control the time and angular top-preactivation derivatives.
   Only after those derivative bounds are proved is the query top tanh
   evaluated. This avoids a circular query pole assumption.

8. The fixed reverse source is obtained from the controlled current
   carrier by subtracting the learned-mixer term. The exact integral is
   bounded coordinatewise by `CY^3`, using bounded features, response
   RMS `CY`, and total residual integral `CY`. Consequently
   `W_0^T delta_a` has the claimed coordinate bound. The forward source
   `W_0 h_theta` is also separately controlled, rather than inferred
   from a sampled feature norm.

The stopping and continuation argument is finite dimensional: the
operator/readout estimates, bounded scalar gates, and integrated read-in
increments bound all coordinates at fixed width. Strict cap margins
therefore permit continuation past any alleged earlier stop and to a
neighborhood of the final closed rectangle. The short real negative
interval needed by the rectangle uses only local estimates and has
length bounded independently of `T`.

This reconstructs the source implication needed below, without using the
separately assigned source reviewer's findings. Its constants can be
chosen independently of the fixed label direction; its sufficiently
large width threshold may depend on the nonzero label magnitude, as
stated. The zero-label network is stationary and needs a separate trivial
branch rather than the source proof's division into positive `Y` scales.

## 4. Finite initialization-only source spaces

The conformal map in stable-geometry Section 4 was checked explicitly.
With its notation,

\[
 z(0)=T/2-(4r/\pi)\,\pi T/(8r)=0,
\]

and the disk image has real range inside `[-r,T+r]` and imaginary
range inside `[-r,r]`. The inverse image of `[0,T]` ends at
`xi_*=2 eta/(1+eta^2)<1`; hence
`1-xi_*=(1-eta)^2/(1+eta^2)>=c exp(-CT/r)`.

Each Taylor coefficient of `R(z(xi),theta)` is an explicit finite
linear combination of physical-time derivatives of `R` at zero. Its
coefficient norm is at most the source bound `M`. Taking the stated
finite, possibly enormous order `J` makes the approximate nodal values
accurate to `epsilon/[4(p+1)]` on the full real interval, uniformly
on the complex angular strip.

The small Bernstein ellipse with parameter `exp(c r/T)` lies inside
the time rectangle. Its coefficient tail yields error
`CM(T/r) exp(-c p r/T)`. Perturbing every Lobatto nodal value by
`delta` changes the interpolant by at most `2(p+1)delta`, so use
of computed initial-jet nodal values instead of actual trained snapshots
has the stated error. The angular Fourier tail and aliasing argument
then give the claimed trigonometric interpolation error.

Consequently `p=O(ell^{5/2})`, `L=O(ell^{3/2})`, and the
number of retained source coefficient vectors is `O(ell^4)`. Only
these final vectors enter the source spaces. The order `J` can be
exponentially large in `ell^{3/2}`; its temporary derivatives and
scalar coefficients are discarded. All operations use initialized data,
fixed labels, and deterministic scalar formulas. No trained snapshot is
an input to the algorithm.

Applying exactly the same scalar operations to `h` and `W_0h` gives
coefficients `v,W_0v` identically; the reverse construction gives
`d,W_0^T d`. The approximation errors of both members are supplied
by their own coordinate source bounds. Thus no unproved implication from
small feature error to small sampled mixer-image error is used.

## 5. Cubature, interactions, and tiny weights

Matching the constant and the symmetric products of a basis of dimension
`r` needs at most `1+r(r+1)/2` positive nodes on the original finite
support. Moving masses along a dependence until one becomes zero
preserves all matched quantities; zero masses are then removed.

The selected basis matrices are weighted isometries. For
`C_0=U^T W_0V/n`, this gives
`||B_0||<=||C_0||<=||W_0||`. If `v=V alpha` and
`W_0v=U beta`, then `C_0 alpha=beta`, so
`B_0v_I=(W_0v)_J`. The reverse formula is equally exact because

\[
 B_0^*=V_I C_0^\top U_J^\top D_2.
\]

Although the runtime adjoint contains `D_1^{-1}`, no inverse minimum
mass enters these identities or norm estimates. The initial training
features and all entries of their Gram are matched exactly.

For bounded real sources, insert their source-space approximants into
each empirical and selected pairing. The approximants have equal
empirical and selected norms, and each coordinate remainder is small
in both mass-one norms. Thus pairing defects are `C epsilon`, without
minimum-mass factors. The real boundedness needed here holds for
`h,g,delta,w`; no `sqrt(ell)` source bound is incorrectly inserted
as a width-independent bound on a different carrier.

The learned forward defect integrates these lower-feature pairing errors
against `c_a delta_a`; the learned reverse defect integrates upper
response pairing errors against `c_b h_b`. The bounded total residual
activity makes both `C epsilon`, independent of the horizon `T`.
Integrating the approximant to `g_a` proves an approximant to `w` in
`S_2`, and then gives the output pairing defect. Its scalar integral
coefficients are proof devices only and need not be computed or stored.

## 6. Runtime state, all-time output, and feature certificate

The complete compressed runtime uses only its selected first weights,
evolving mixer, readout, positive masses, and labels. The state is
autonomous and restartable; the full bases, original mixer, and source
coefficients are discarded after setup. With source dimensions
`O(ell^4)`, each retained population has `O(ell^8)` neurons and
the dominant evolving mixer has `O(ell^16)` entries. Fixed masses
and an optional copy of the initial state do not change that order.
This is a count of real coordinates, not bits or setup complexity.

The retained reference starts at exactly the compressed initialization.
Its forward, reverse, and output defects verify the signed-activity
comparison on `[0,T]`, with constants independent of `T`. For circle
queries, both first-layer columns are controlled because the inverse
coordinate is real 1-Lipschitz; the mixer and readout estimates finish
the uniform query bound. For `t>=T`, each autonomous network has its
own exponentially small query tail from `T`. Taking `T=C_T ell`
with sufficiently large fixed `C_T` therefore covers all later times
and the fitted endpoint. Neither model is frozen at `T`.

The finite-width feature certificate also reconstructs. Define
`v=sum_a y_a g_a(0)`. The initial Gram gives
`||v||_2^2/n=y^T G_0 y>0` when `y!=0`. Zero initial readout
implies zero initial hidden velocities, and differentiating again gives
the candidate's formulas for `A_ddot`, `h_ddot`, and `W_ddot`.
For every nonzero label component, strict real gates and invertible
`W_0^T` make its first-feature curvature nonzero. Direct chain-rule
expansion yields

\[
 \sum_a y_a\,v^\top\ddot g_a(0)/n
   =\|\ddot A(0)\|_F^2/n+\|\ddot W(0)\|_F^2>0.
\]

The normalization matches the canonical mobility exactly. The proposed
extra cubature vectors preserve the reverse actions and the norm of
each nonzero first-feature curvature. The weighted form of this identity
then certifies motion in a second hidden training feature of the
compressed model as well. Both label signs and a vanishing component are
allowed. The certificate establishes exact nonzero motion at finite
width; it does not establish a displacement lower bound uniform in
width, and the candidate correctly says so.

## 7. Adversarial checks and exact claim boundary

| Potential failure | Resolution in the frozen inputs |
|---|---|
| A fixed residual-direction surrogate replaces the true flow | Both full and cavity systems use their own two-component residuals; no alignment assumption occurs. |
| A copied full residual invalidates Gaussian independence | Every conditioned reference is an autonomous singleton cavity on its own stopping domain. |
| Complex damping is applied along an arbitrary contour | The source proof uses real damping only at the anchor, then bounded growth over a short vertical segment. |
| Huge initialized derivative order invalidates the stored-state count | The contract excludes temporary setup resources; only final coefficient spaces and then the compressed network survive setup. |
| Tiny positive cubature masses amplify trajectory error | All proof norms use the masses and exact adjoint; no estimate divides by the minimum mass. Numerical conditioning remains outside the claim. |
| Finite-horizon approximation is substituted for all-time accuracy | Both independent autonomous tails are explicitly bounded and compared after `T`. |
| Mixer motion alone is called feature motion | The certificate directly establishes nonzero second derivatives of first and second hidden features. |
| A fixed nonzero label result is asserted uniformly as labels shrink with width | The source width threshold may depend on the fixed label magnitude; the candidate does not claim a simultaneous shrinking-label regime. |

No source edit is required to repair a blocking inference in the checked
versions. The compression note still describes itself as conditional on
the source theorem; this report supplies an internal reconstruction of
that dependency, without upgrading the result to established material.
Future changes to the three hashes above require an appropriately scoped
new check. The strongest presently checked claim retains all the explicit
restrictions: orthogonal two-input geometry, fixed sufficiently small
labels, sufficiently large width, exact-real setup, and after-setup stored
coordinate complexity.

## 8. Final author-version confirmation

After the initial report was frozen, the author supplied the following
revised sources. All three were reread completely; one combined tool
output was truncated, and its omitted beginning/end passages were then
read separately to complete coverage. Their confirmed hashes are:

| Revised source | SHA-256 |
|---|---|
| `TWO_INPUT_CANONICAL_COMPRESSION.md` | `f96fe56c50381a6bc3fd9b51d9889edebf83b64e376ce8ab8d48ea11d8845568` |
| `TWO_INPUT_STABLE_GEOMETRY.md` | `708182a1b52269a76ac03ecc08b8436f39fe20c7173272df5d022f9c42b29068` |
| `TWO_INPUT_COMPLEX_SOURCE.md` | `a048017ae0f87d7efb4ce845a89a26e7cd93879e5b441c5107945d561a68f60e` |

The assembly now states the full result without an unverified source
assumption, while retaining its research-study and resource boundaries.
The source and stability notes update their corresponding status prose.
These status changes are supported by the mathematical reconstruction
in Sections 2--6 above; other review reports mentioned by the author
were not read or relied upon.

The stability note additionally restricts the general approximation lemma
to `0<epsilon<=M`. This correctly avoids a negative logarithm in a
formula formerly stated for arbitrary `epsilon>0`. The actual use with
`epsilon` proportional to `n^{-1/2}` and common source bound of order
`sqrt(log n)` already satisfies the restriction, so no step or resource
count of the compression theorem changes.

The complex source adds an explicit instruction to condition the query
construction on the good initialized first-layer RMS and coordinate
event, and to zero the query reference if it fails. This event depends
only on retained data for every row cavity. The addition makes explicit
the legitimate conditioning used in the reconstruction of its query
Gaussian argument; it does not condition on any omitted Gaussian row.
The other changes repair formula typography and update status language.
No mathematical obstruction arises in the revised source proof.

The full-chain PASS verdict covers these revised hashes. Separately,
`TWO_INPUT_FEATURE_LEARNING.md` now has a complete reconstruction in
this checker's `TWO_INPUT_FEATURE_LEARNING_CHECK.md`, covering its final
hash `75d317cbcfca5cbf3f4a2b4e11a07bd094ab7daff78fcae204b19760db3fb8c7`.
It strengthens the assembly's finite-width curvature certificate to
width-independent `c|y|^2` feature motion at a fixed positive physical
time, with the precise label and transfer quantifiers recorded there.
