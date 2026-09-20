# Informed internal review of the selection route

Date: 2026-09-20. Reviewer: `order_endpoint_route`.
This is the supervisor-authorized internal cross-check after both candidates
were frozen. It is not an isolated promotion review. The reviewer authored
the separate endpoint route before receiving these files, and discloses that
prior involvement. No other study was an input; only this report was edited.

## Verdict

**PASS for the stated modified-optimizer results and the fitting-alone
obstruction, with one minor qualification about nonzero noise.** The
universal finite compatible-circle scope for labels in `[-1,1]` is justified
by the complete short-time source theorem plus the supplied extension of
the actual full dictionary hierarchy. No assumed trained spectral gap,
dictionary symmetry, ridge alteration, or interchange of full-GF infinite
time/order limits is hidden in the argument.

The post-burn-in deterministic readout endpoint and its whole-circle
comparison are correct, including the inherited training-invisible readout
component. The bounded-forcing variant instead converges to the unique
minimum-readout-norm interpolant. Its Lyapunov estimate and arbitrary joint
order/fitting-time convergence are correct. A positive coefficient `eta`
alone does not ensure that actual noise is nonzero: the allowed forcing may
vanish, and projection `N U_s` may annihilate a nonzero signal. Qualify the
sentence calling every positive-eta choice “explicitly noisy,” or require
nontrivial projected random forcing. This does not affect any convergence
or endpoint formula.

`FITTING_ALONE.md` correctly gives bounded states in the actual canonical
closure state spaces, with zero hidden displacement and zero training loss,
whose consecutive whole-circle predictions remain separated. It explicitly
does not claim reachability from the prescribed zero limiting readout, and
therefore does not contradict canonical-GF endpoint convergence.

## Frozen inputs and full coverage

Frozen source hashes verified before and after reading:

| File | SHA256 |
|---|---|
| `SELECTION_ROUTE.md` | `f96942fc482ac61d5b2486f51ce416bffd7cbddf98707365ad9e89f321709374` |
| `FITTING_ALONE.md` | `e87dfd13f6cdf806c42479dc3e136474ff9b2ab2142cb56585bcbeac4754f12a` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

HEAD was `8a15e0f196ed31af54160c651bdfbf2f109eecf7`.
Both study candidates were read completely: selection route, all 757 lines;
fitting-alone note, its entire construction and limitation. The canonical
sources inspected in full for the relevant units were:

- C.4.7.9, all parts 1–7, including dictionary normalization, fixed-order
  global existence, the correct coefficient metric, both strong action
  directions, omitted-source comparison, and observation convergence;
- C.4.7.10.A.1–A.4, lines 12594–13160, including the all-Borel-law statement,
  explicit cap, strong completion, uniqueness, and actual finite-GF bridge;
- C.4.7.10.B, complete dictionary/enrichment/filter/compatibility argument;
- C.4.7.10.C.1 through (H3.N6), including exact equations, physical metric,
  and the separation between order and numerical limits;
- D.3, complete explicit time-40 domain, retained hierarchy, source errors,
  comparison, and observation conclusions; and the shared notation contract.

Parts B/C.1/D.3 and C.4.7.9 had already been read in this agent's permitted
endpoint assignment and were cross-referenced in this review. A.1–A.4 was
newly read in full under this review assignment. A short trailing D.4 header
and introductory numerical paragraph appeared in the final D.3 boundary
read; it was not used as a premise. No other route report or prior review
verdict was consulted. Required rigorous-math/research skills and their
contract/adversarial references were already read and applied.

## 1. Universal finite compatible-circle scope

The all-law input is genuinely present in A.1: every Borel probability law
on the radius-`sqrt(2)` circle times `[-1,1]` has canonical strong population
GF through `T_0=1/200`. This precedes the executable rational two-arc
subfamily; it is not restricted to that subfamily. A.2 establishes its cap
without constraints on atom count, covariance rank, minimum nonzero weight,
or input separation. A.3 gives individual time/input Gaussian reverse tails
with common constants and strong law completion; A.4 supplies the actual
finite-GF meaning. These match the claims imported in selection Section 9.

Part B's written hierarchy theorem is narrower, but Section 9 correctly
checks the extra passage instead of simply changing its quantifiers:

1. Its dictionaries and ridge are initialization-only and unchanged.
   The positive contractions converge strongly on the initialized observable
   spaces independently of the training law. Both orientations are retained.
2. Every finite-law raw Euler update uses bounded gates, the same action and
   adjoint, and learned ranks. Generated sigma-field `L2` spaces and their
   HS block are closed under these operations. The strong completion in A.3
   puts the arbitrary fixed law's path in those same spaces/block.
3. Joint continuity on the compact time/input set makes the target forward
   fields and upper backward fields compact in `L2`; the continuous learned
   derivative is compact in HS. Uniform strong approximation on compact
   sets and finite-rank HS approximation prove all three errors in (S24).
4. Fixed-order existence/energy in C.4.7.9.4 requires bounded labels, not the
   narrower convergence domain. Thus all orders share the comparison ball.
5. The actual lifted middle equation has both positive filters, yielding the
   exact learned-source subtraction in Section 9. The lower-gate cutoff
   uses only the unchanged canonical reference reverse query.
6. The estimate is `C exp(C(1+s)T_0)[(1+s)epsilon_p+tau(s)]`, with a
   Gaussian negative quadratic in `s` in the tail. Sending `p` to infinity
   first at fixed cutoff and then removing the cutoff is valid.

This proves the exact population hierarchy convergence needed for the new
domain. It does not extend the maintained numerical data interface or give
a diagonal numerical/order theorem. The scope is separately fixed laws;
there is no uniform guarantee over finite datasets approaching coincident
or antipodal directions. For labels outside `[-1,1]`, the candidate retains
its stated requirement of another certified canonical domain; the new
universal extension does not silently cover arbitrary `Y`.

## 2. Positivity, early training, and exact readout selection

The initial Gram proof is correct. For directions distinct modulo sign,
a generic `z` avoids the finite union of the zero/equal/opposite-projection
lines. The numbers `z dot u_a` are nonzero with distinct squares. Restricting
a zero lower-feature combination to `g=t z` produces an invertible
Vandermonde system from the first `m` odd tanh coefficients. The recurrence
from `tanh'=1-tanh^2` makes all of those coefficients nonzero. Gaussian
full support upgrades an almost-sure zero continuous function to an
everywhere zero function. These steps prove the lower Gram is positive.

The actual initialized forward-query vector can be evaluated before any
reverse calls, so its centered Gaussian covariance is exactly that lower
Gram. The resulting nondegenerate Gaussian has full support. Coordinatewise
variation proves independence of its coordinate tanh functions. Positive
training weights preserve definiteness of the weighted Gram `G^0`.
Merging compatible duplicate/antipodal constraints preserves squared loss
because every represented predictor is odd. Incompatible such labels
cannot be interpolated and are correctly excluded.

The drift constants are checked directly from the original physical GF:
`int |r| <=Y`, `||c||infty<=2Yt`, `||K||HS<=2Y^2t^2`, and
`||w-g||2<=4Y^2t^2+2Y^4t^4`. The decomposition with `A_0` acting on
the changed lower field gives the upper feature bound
`10Y^2t^2+4Y^4t^4`. It is not an action operator-norm approximation.

For a weighted Gram, the entrywise feature bound `2d` implies

\[
|v^T\Delta Gv|\le2d\Big(\sum_a\sqrt{\pi_a}|v_a|\Big)^2
\le2d|v|^2.
\]

This verifies the dimension-free factor two. Since `Y>=1,T<=1`,
`2d(T)<=28Y^4T^2<=gamma_0/2` at the proposed `T`. Thus the full learned
Gram has gap `gamma_0/2`, and the actual hierarchy approximation gives
eventual gap `gamma_0/4`. The threshold in order is qualitative, correctly
not advertised as an executable certificate.

With `E c=(sqrt(pi_a)<c,H_a>)_a`, the operator norm satisfies `||E||<=1`,
`G=EE*`, and the unhalved-loss physical readout equation is exactly
`c'=2E*(bar y-Ec)`. Differentiation of (S9) confirms both its initial
condition and its ODE. The endpoint is

\[
c^*=(I-E^*G^{-1}E)c(T)+E^*G^{-1}\bar y.
\]

The first term cannot generally be omitted. The matrix
`E*G^-1 E` is a self-adjoint idempotent with range `range(E*)`, so this
term is precisely the inherited kernel component. The decay estimate uses
`||E*G^-1||^2=||G^-1||`, giving `Y gamma^-1/2 exp(-2 gamma s)`.
For early singular orders, `E*` kills `ker G`, justifying the pseudoinverse
description and the expressly limited interpolation claim.

The small-time middle-motion calculation also checks out: the strong
limit of `c(t)/t` is `v=2 sum pi_a y_a H_a^0`, and the positive upper
Gram makes `v` nonzero whenever some label is nonzero. Applying `K''(0)`
to the dual lower vectors isolates a nonzero coefficient multiplied by
the strictly positive tanh gate. The conclusion is nonzero middle motion
during every positive burn-in interval, as stated, rather than a proved
positive endpoint displacement in both hidden layers for every dataset.

## 3. Whole-circle comparison and limits

All constants in (S13) are correct. The common-carrier field defect gives

\[
\|G_p-G_q\|\le2\delta_{p,q},\quad
\sup_u|k_p(u)-k_q(u)|\le2\delta_{p,q},\quad
\sup_u|k_q(u)|\le1,
\]

and the inherited prediction/residual defect is at most
`b=zeta+2YT delta`. The exact resolvent identity gives inverse difference
at most `2 delta/gamma^2`. Splitting the endpoint correction into the
kernel, inverse, and residual differences yields, respectively,
`2Y delta/gamma`, `2Y delta/gamma^2`, and `b/gamma`; adding the direct
burn-in prediction defect yields exactly (S13).

Because `delta_(p,q)<=delta_p+delta_q` and similarly for readout,
consecutive endpoints stabilize. Applying the same formula against the
full target identifies their limit with the same modified optimizer.
The uniform spectral-gap tail makes every joint sequence `p,s ->infinity`
converge to that endpoint. For clarity, the statement that the two iterated
limits commute also has the needed fixed-`s` inner order limit: (S9), the
feature/readout convergence, and matrix exponential continuity imply it.
One direct verification of the latter is

\[
e^{-2G_ps}-e^{-2Gs}
=-2\int_0^s e^{-2G_p(s-v)}(G_p-G)e^{-2Gv}\,dv,
\]

whose norm is at most `2s ||G_p-G||` because both matrices are positive
semidefinite. Thus this minor implicit step can be supplied without any
extra assumption. No such limit interchange is claimed for continued
full hidden-layer GF.

## 4. Bounded random forcing and the qualification

The noisy equation is a precisely declared second optimizer. For each
allowed forcing path its Hilbert-space vector field is globally Lipschitz
in the readout and measurable in time; the bounded forcing and linear
growth justify the pathwise integral contraction and continuation. The
training residual and training-nullspace component separate exactly:

\[
r'=-2Gr,\qquad z'=-\nu z+\eta\sqrt L\,NU_s.
\]

The Young inequality in the candidate gives
`(||z||^2)'<=-nu||z||^2+(eta^2/nu)L`. With `nu=gamma, eta<=gamma`,
adding `L'<=-4 gamma L` yields
`V'<=-3 gamma L-gamma||z||^2<=-gamma V`. Orthogonality of
`E*G^-1 r` and `z` verifies (S20) exactly. The limiting readout is the
unique minimum-norm interpolant, and the endpoint comparison drops the
inherited-readout defect, giving the constants in (S21)–(S22).

The arbitrary joint-order/time convergence remains valid even if forcing
signals vary with order, because its entire transient estimate is uniform
over allowed signals. A fixed-positive-time order limit need not exist
for unrelated signals, and the noisy subsection correctly does not assert
commuting inner fixed-time limits for that situation.

Minor qualification: `eta>0` does not force `NU_s` to be nonzero. For
example, `U_s=0` is allowed. Even the concrete `tanh(xi_1)` choice could
be annihilated by the learned training projection in a special case.
There is a simple optional way to guarantee a nonzero finite-mark forcing
without changing the theorem. The upper mark `X=tanh(xi_1)` has positive
density on `(-1,1)`. Therefore `1,X,...,X^m` are linearly independent in
`L2`. Since the training span has dimension `m`, at least one of these
`m+1` bounded fields has nonzero `N` projection. Choose such a field using
its positive projected squared norm, and multiply it by a specified
nondegenerate bounded random scalar signal. This uses the existing static
mark and current learned training features. It is an optional explicit
nonzero-noise witness, not needed for any stated analytic estimate.

## 5. Fitting-alone counterexample

The augmented training-plus-test Gram positivity uses exactly the valid
finite-direction argument audited above. Strong convergence of `B_p` on
the compact initialized lower feature family gives convergence of the
augmented upper Grams, and consequently their eventual uniform positive
gap. The chosen `c_p` is a bounded measurable function of the existing
upper marks because each `H_p^0(u_j)` has that property. Thus it lies in
the actual saved-state domain at that order; it is not an extraneous
function-field coordinate.

Multiplying the coefficient vector by `G_p` verifies all training labels
and the alternating test value exactly. Its squared `L2` norm is
`z_p^T G_p^-1 z_p`, giving the stated uniform bound. Both hidden blocks
are exactly initialized. Residuals vanish, so all three velocities of the
original exact closure vanish, even though the backward fields need not.
The test values of two consecutive orders differ by two, establishing
the whole-circle lower bound. The logical conclusion is precisely that
bounded interpolating equilibria do not select a stable predictor. The
prescribed-initialization reachability caveat is essential and is already
stated prominently.

## Actual checks and remaining boundaries

This review consisted of complete text/source reading, rederivation of the
weighted Gram bounds, physical readout ODE and endpoint, resolvent
comparison, pathwise Lyapunov estimate, strong-filter domain extension,
and exact equilibrium construction. Hash verification used `sha256sum`;
HEAD used `git rev-parse HEAD`. No experiment, random simulation, or numerical
matrix test was substituted for these arguments. No failed check or unresolved
mathematical obstruction was found. The nonzero-noise wording qualification
was reported to the supervisor before this report was frozen.

The approved internal scope remains a modified optimizer after an early
positive burn-in, eventual closure orders, every separately fixed finite
compatible dataset with labels in `[-1,1]`, exact population expectations,
and whole-circle prediction comparison. It supplies neither a pure-order
accuracy rate nor a numerical order threshold, and it does not establish
full-GF endpoint convergence for arbitrary labels or datasets.

## Correction closure: nonzero-noise wording

On 2026-09-20 the supervisor supplied the revised selection candidate with
SHA256
`a076b9a3826c9abe9408ec2f1c3b46856b0d3e82eeb4ce50ec2574f92ff969e7`.
Its replacement sentence now states that, for a positive noise coefficient,
actual forcing is nonzero only when both the loss and `N U_s` are nonzero,
and that the coefficient alone does not ensure injection. This is the exact
qualification required by the equation, since its forcing norm is
`eta sqrt(L) ||N U_s||`.

The changed paragraph was read directly and its new file hash verified with
`sha256sum`. A deterministic Python check replaced only that revised wording
in memory by the old wording and computed SHA256; it recovered exactly the
previously fully reviewed hash
`f96942fc482ac61d5b2486f51ce416bffd7cbddf98707365ad9e89f321709374`.
The command exited zero with output:
`PASS: replacing only the revised noise qualification recovers the full previously reviewed SHA256.`
Thus there were no other candidate changes requiring a reopened review.

**The minor issue is closed. Final internal verdict: PASS** for the revised
selection candidate at the new hash above and the unchanged fitting-alone
candidate at
`e87dfd13f6cdf806c42479dc3e136474ff9b2ab2142cb56585bcbeac4754f12a`.
The earlier scope limits and the distinction from full nonlinear-GF
endpoints remain part of this verdict. No further research was performed.
