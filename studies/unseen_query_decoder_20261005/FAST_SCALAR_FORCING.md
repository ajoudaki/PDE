# Scalar pair errors as physical Taylor forcing

2026-10-06. New bounded author derivation, not an independent review.
`FAST_TAYLOR_NOISE_CHECK.md` and `FAST_COMPOSITION_CHECK.md` remain frozen
and unchanged. This note concerns the physical source, not a complete
scalar-history decoder or a new finite-bit metric theorem.

## Result and essential distinction

The physical Taylor program can tolerate small errors in **all of its
learned-rank pair applications, readout/residual pair reductions, and
strict-slack norm/cap tests**, with sufficient pair precision

\[
                 C\beta^{100L}(1+m/\gamma)Z.                 \tag{1}
\]

The proof does not compare the entire perturbed row history with the
unperturbed row history. Instead, each actually stored rank list defines
an actual physical parameter matrix. An inaccurate pairing differs from
that *same matrix's* exact action by an explicitly bounded vector. Freeze
these local coefficient defects, including scalar residual defects, into
analytic forcing polynomials. The source's physical-flow comparison then
applies. Strict-slack guards remain inactive by a causal prefix-completion
argument given below.

There are two important limitations. This result does **not** by itself
cover the additional Gram reductions introduced by Gaussian elimination,
and it does not show that a metric acquired on one history remains an
accurate pair oracle on every perturbed history. Those are separate
representation/coupling requirements. Consequently (1) is not a replacement
for the conservative global scalar-history precision in the frozen
composition theorem.

## 1. Inputs and contract

This derivation uses the completely read source
`FAST_TAYLOR_NOISE.md`, SHA-256
`71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c`,
its authorized physical/Taylor/Gaussian inputs, and the completely read
`SANE_METRIC_PACKETS.md` and `NOISY_SCALAR_HISTORY_ACQUISITION.md`.
The latter has SHA-256
`b301507a73de79310634ca67da75a9f5817a139edc498ad145aaeb857cae6fab`.
No new agent working note, experiment, Git operation, or maintained-file
change is used. The research/proof/canonical-notation skills are applied.
In particular physical matrix observations are not identified with their
Gaussian-conditioning representation.

Keep the source network and physical velocities, label allowance and
scientific good event, all width gates, normalized time and parameter norm,
and its analytic/value-access contract. In the source notation put

\[
 r=m/\gamma,\quad Y=\|y\|_2/\sqrt m>0,\quad
 S=16Yr\le1,\quad B=\beta^{100L},\quad
 \chi=B(1+r)Z .                                             \tag{2}
\]

Here `Z` is the corrected source's logarithm, including `m+d+2`.
The zero-label branch is unchanged. On the nonzero branch retain
`Y >= n^(-1)`. Let `H,K,h_j,E,delta` be the certified source patch count,
Taylor degree, patch lengths, accumulated stability budget, and local
defect tolerance. In particular

\[
 K+E+\log\delta^{-1}+\log h_{\min}^{-1}
       +\log(e+R)+\log(en)\le C\chi,\qquad
 h_{\min}=\min_jh_j.                                       \tag{3}
\]

As in the source, allocate fixed fractions of `delta` to matrix-answer
noise, activation interpolation, local arithmetic, and the new scalar
defects. This costs only a fixed additional number of precision bits.

### What an erroneous pair means

For two named, already-created physical row vectors define

\[
 \langle u,v\rangle_n=\frac1n\sum_{i=1}^n u_iv_i.
\]

Every physical pair call returns

\[
        \widehat p(u,v)=\langle u,v\rangle_n+e(u,v),
                  \qquad |e(u,v)|\le\epsilon_{\rm pair}.    \tag{4}
\]

The operands in (4) are the **actual perturbed operands at that call**,
not their unperturbed counterparts. A stored pair keeps its realized
value when reused. A named vector keeps its creation-time scalar
arguments. Scalar errors may depend arbitrarily on the available past,
subject to (4). They do not reveal future matrix noise. Initialized
matrix actions still have the physical form `W_0 v+sigma zeta` or
`W_0^T u+sigma zeta`, with the source's raw-noise RMS event.

This is a substantive oracle specification. An approximation to an
unperturbed pair table does not automatically satisfy (4).

## 2. Exact physical realization of the rank lists

Use the source's unexpanded rank implementation. At every coefficient and
committed endpoint, a hidden displacement matrix is, by definition,

\[
                   D=\frac1n\sum_{\mu=1}^{q}
                                  c_\mu a_\mu b_\mu^T.     \tag{5}
\]

All entries in this formula are the actually stored factors and weights.
The first-layer list has fixed input vectors in place of the right row
factors, and the readout is a vector sum. Factors from earlier patches
are immutable; an endpoint appends or combines scalar weights without
reinterpreting earlier fields at new scalar arguments.

Equation (5) is an exact definition even when its factors were generated
using erroneous pairs. It makes no claim that they are close to the
unperturbed factors separately. Nor does it require a well-conditioned
factor basis. The physical coefficient represented by an integrated
gradient is exactly the rank sum of the computed residual-weighted
backward coefficient and feature coefficient, with the stored integration
weight. A rounded weight contributes a local parameter-coefficient defect.

For a forward application, the implemented rank calculation and its exact
physical counterpart differ by

\[
 \sum_\mu c_\mu a_\mu\widehat p(b_\mu,v)-Dv
                =\sum_\mu c_\mu a_\mu e(b_\mu,v).           \tag{6}
\]

The transpose formula exchanges `a_mu` and `b_mu`. This equality uses
the same realized list and query on both sides. Comparing with an old
unperturbed list instead would reintroduce a history-sensitivity problem.

For bookkeeping, let `N_sum` bound the number of summands in any rank
application, coefficient convolution, or rank-list norm contraction,
before squaring that count where explicitly stated below. A safe choice is
`N_sum <= C(R+K+1)^3`. Indeed the source has `O(mLHK^2)` scalar rank
weights and only `O(R)` distinct named factors; convolution adds at most
`K+1` indices. This bound may be wasteful, but its logarithm is `O(chi)`.

Choose `A >= 2` to bound the absolute stored scalar weights, the RMS of
each row factor/query/coefficient, and `n+1,m,L,K,Y^(-1),h_min^(-1)`.
It also bounds the reciprocals of the positive guard margins used below.
Use the source's good-program coefficient bounds with fixed slack and
its explicit local scratch bounds. One can choose

\[
                            \log A\le C\chi .              \tag{7}
\]

The possible interpolation scratch factor `exp(CJ)` is permitted in
`A`; it contributes `CJ=O(chi)`, not `RJ`. Small physical scales such as
`Y`, `S`, or the final decay cap have logarithmic inverses covered by the
retained width gates. This is a bound on explicitly specified local
quantities, not a global expanded-history Lipschitz assumption.

From (6), a learned-action coefficient has RMS defect at most

\[
                      N_{\rm sum}A^2\epsilon_{\rm pair}.    \tag{8}
\]

The source's readout coefficient uses
`sum_{p+q=k}<w[p],h[q]>_n`. Its scalar defect is at most
`N_sum epsilon_pair`; the same bound holds in RMS over the sample index.
Dividing that scalar residual defect by `Y` costs at most `A`.

For the norm guard on (5), the exact squared Frobenius norm is

\[
 \|D\|_F^2=\sum_{\mu,\nu}c_\mu c_\nu
     \langle a_\mu,a_\nu\rangle_n
     \langle b_\mu,b_\nu\rangle_n.                          \tag{9}
\]

If `epsilon_pair <= 1`, replacing both pairs by (4) changes (9) by at
most `3N_sum^2 A^4 epsilon_pair`. A row-vector squared-RMS guard is
simply one pair. Residual RMS over the finite sample set and the other
scalar guard calculations are fixed-degree sums/products of these
quantities; local arithmetic can be allocated the same tolerance with
polynomial additional guard factors.

For completeness, a rounded integrated coefficient is converted to a
velocity-coefficient defect by multiplication by `(k+1)/h_j` and by the
physical-to-normalized conversion `1/Y`. Summing its rank factors costs
at most `N_sum A^2`. These factors, all parameter blocks, and all the
preceding cases are safely covered by

\[
              C N_{\rm sum}^2 A^8\epsilon_{\rm pair}.       \tag{10}
\]

No power with exponent equal to the number of earlier phases occurs.

## 3. Freeze scalar defects, not physical parameters

In patch `j` use `xi=(tau-tau_j)/h_j`. For every forward/backward
coefficient operation, freeze the realized vector discrepancy (6), and
form the polynomial consisting of those discrepancies through degree
`K-1`. Add it at that forward/backward node, alongside the original
initialized-action noise polynomial. Likewise freeze each readout pair
discrepancy into an additive residual polynomial. An integrated-weight
or other parameter-coefficient rounding defect is a parameter-velocity
forcing polynomial. All these polynomials have real coefficients and
are holomorphic in `xi`.

If every coefficient has norm at most `e_*`, its polynomial has norm
at most `4^K e_*` on `|xi| <= 4`. Thus (10), with the residual polynomial
measured after division by `Y`, gives the common bound

\[
       C4^K N_{\rm sum}^2 A^8\epsilon_{\rm pair}.           \tag{11}
\]

The auxiliary field at an arbitrary normalized physical state `U` uses
the actual physical matrices belonging to `U`, plus these *fixed*
polynomials. It does not differentiate a rank basis or reconstruct the
old scalar history as `U` varies. The rank-list identities are needed to
identify the realized Taylor coefficients of this field, not to provide
a rank chart for every nearby state.

The activation centers are computed causally at order zero using the
already available perturbed forward quantities, exactly as in the source.
Their interpolation polynomials are then fixed throughout the patch.
Induction over coefficient order, and forward/backward layer order within
each coefficient, proves exact formal agreement with the auxiliary field:
the initialized-action error is its prescribed noise coefficient; (6) is
its learned-action forcing coefficient; the readout error is its residual
forcing coefficient; and integration divides the velocity coefficient by
`k+1` and multiplies by `h_j`. Future errors are not used at earlier orders.

The residual addition is the only new field estimate not already explicit
in the matrix-noise proof. If its sample RMS is at most `Y delta`, its
physical gradient contribution is minus twice the sample average of
that residual error times the gradient factors
`delta^(1) v^T`, `delta^(j) h^(j-1)T/n`, and `h^(L)`, respectively.
Cauchy--Schwarz and the source RMS bounds put its block norm below
`C beta^(20L) Y delta`. Time/amplitude normalization multiplies by
`r/Y`, giving at most `C beta^(20L)(1+r) delta`. Its derivative in the
physical state uses the same differentiated forward/backward factor
bounds as the source, below its `beta^(70L)` ledger with fixed slack;
the residual addition is fixed, and `delta <= q_T <= q_j` preserves
the required decaying residual factor. Together with the source's forward
and backward estimates, this is absorbed by its existing
`C_N delta`, where `C_N=B^2(1+r)^2 sqrt(log(en))`, and by its
fixed-factor enlarged derivative bound `2 Lambda_j`.

The inverse label scale in a raw absolute pair tolerance was paid once
in (7), using `1/Y <= n`. It is not repeatedly propagated down the tape.
The activation-disk first-exit argument is unchanged because (11) supplies
the same small node-defect bound as the original physical forcing proof.

## 4. Norm and coefficient guards: the causal proof

Use only the source's strict-slack numerical guards. Specify their radii
as a fixed factor above the proved nearby-flow/coefficient bounds, rather
than merely saying they are larger. For a guard computed from a squared
norm, let `Delta > 0` be its squared-radius margin, and include
`Delta^(-1)` in `A`. Negative noisy squared norms are replaced by zero
inside the guard routine. On the good range the routine is identity.

This choice is permitted by the source's explicit instruction to put caps
strictly above its certified ranges. It does not shrink the label class.
The causal activation coefficient cap is the already specified
`P_(1/8)`: the source's good centered series has coefficient `l1` norm
less than `1/64`, so it has a numerical margin as well.

One must not assume these guards are inactive in order to establish the
coefficient bounds proving they are inactive. The noncircular argument is:

1. Start at a certified patch anchor and suppose a first guard could act.
   Before it, all actually used scalar errors satisfy (4), and preceding
   factors are within their guarded ranges. Equations (8)--(10) therefore
   bound every defect generated in that prefix.
2. Retain those realized defect coefficients and complete the remaining
   patch with zero future scalar/coefficient defects. The remaining
   matrix noise can also be set to zero for this proof-only completion.
   Order-zero centers not yet created are completed by their ordinary
   causal forward pass. Fixed-layer subtraction keeps those centers in
   their source disks. This defines an admissible completed family of
   small forcing polynomials without using a later program output.
3. The source contraction argument constructs its holomorphic local
   solution. The formal coefficient induction above identifies every
   already computed coefficient, including the raw input to the proposed
   first guard, with the corresponding coefficient of this solution.
4. Cauchy bounds (or the endpoint estimate for a committed state) and
   the strict nearby-flow margins put that raw value
   inside its guard. For a pair-based norm test, (9)--(10) change the test
   by less than `Delta/2`. For the causal activation cap, the relevant
   partial coefficient sum is bounded by the full `l1` bound, below
   `1/64`. The guard is therefore inactive, a contradiction.

This argument repeats patch by patch, using the certified endpoint error.
It does not use complex extensions of norms, projections, or clipping.

In particular the zero-slack projection of the residual onto radius `Y`
from an older real-field extension must **not** be silently inserted into
the Taylor recurrence. The present source uses the unclipped holomorphic
physical formulas and separate harmless numerical caps. A real-trajectory
projection, or a cap applied to coefficients at radii intended for values,
would need a different proof if it could act. This distinction is part
of the lemma's implementation contract.

## 5. Precision and physical conclusion

Choose a sufficiently large numerical constant in

\[
 \boxed{\displaystyle
 \epsilon_{\rm pair}\le
       \frac{\delta}{C4^K N_{\rm sum}^2 A^{10}} .}           \tag{12}
\]

Then (11) fits its allocated fraction of the source defect tolerance,
the guard errors are below half their margins, and locally allocated
arithmetic errors fit the same budget. If endpoints are independently
rounded, require their normalized block error to be at most the allocated
fraction of `h_j C_N delta`; the factors already included in `A` make
this another local precision condition. Endpoint errors are additive
defects, not constant forcings claimed to preserve the same polynomial.

The source endpoint estimate consequently remains

\[
 e_{j+1}\le(1+2h_j\Lambda_j+2\,2^{-K})e_j
             +C h_j C_N\delta+2Mh_j2^{-K}.                  \tag{13}
\]

Its products are bounded by `exp(2E+1)`. The source's choices of `K`
and `delta`, with fixed slack for the new defects, therefore preserve
the normalized physical parameter and all-time whole-sphere prediction
conclusions. The earlier `exp(E)` physical stability and the `4^K`
analytic extension are real costs, but both have logarithm `O(chi)`.
From (3), (7), and (12),

\[
                 \log\epsilon_{\rm pair}^{-1}\le C\chi.    \tag{14}
\]

This proves (1) for the stated physical pair oracle. It is a backward-error
argument for the actual physical parameter program, not an assertion that
its entire scalar history has Lipschitz constant `exp(C chi)`.

Independent Gaussian scalar errors are one permitted realization. If
there are `P_phys <= CR^2` physical pair calls, take their scale at most
`epsilon_pair/n`. The event that every raw scalar Gaussian has magnitude
at most `n` has failure at most `2P_phys exp(-n^2/2)`. This adds only
`log n` bits. A prescribed fixed failure allocation can instead use its
explicit Gaussian-tail threshold and charge that threshold's logarithm.

## 6. Exact boundary of the improvement

### Additional Gaussian-conditioning Grams

`NOISY_SCALAR_HISTORY_ACQUISITION.md` adds pair reductions for posterior
means, covariance square roots, and innovation/history contractions.
If those Grams are perturbed, the simulated initialized action is no
longer known to equal `W_0 v+sigma zeta` for one common Gaussian matrix
and independent raw answer noises. Its one-call coefficient maps have
small logarithmic sensitivity, but that alone does not produce a common
physical matrix for the whole modified tape.

To apply the present lemma to that simulation one still needs a joint
coupling, for every call, of the form

\[
 \widehat y_t=W_0\widehat v_t+\sigma\zeta_t+d_t
 \quad\text{or}\quad
 \widehat y_t=W_0^T\widehat u_t+\sigma\zeta_t+d_t,
 \qquad
 \max_t\|d_t\|_{2,n}\le e^{C\chi}\epsilon_{\rm pair},      \tag{15}
\]

with the required predictable chronology and Gaussian law. The true
conditional means in a recursive coupling use corrected prior answers,
whereas the modified formulas use modified prior answers. A local error
bound for a single coefficient formula does not remove that discrepancy.
The existing global coupling controls it by causal propagation. No
replacement for that argument is proved here; nor is a lower bound ruling
out a sharper replacement claimed.

### Finite metric acquisition away from its acquired tape

The exact selected-packet metric reproduces pairs of the realized finite
table on which it was constructed. That is enough for exact causal
acquisition when the prefix agrees. Once quantization changes earlier
prefixes, the newly evaluated row fields need not be columns of that
same table. Exactness on the acquired columns is not uniform cubature
over all changed prefixes. To invoke (4) one must separately prove the
metric's reduction error relative to the *current perturbed full-ensemble
operands*. The existing global row-history bounds provide one sufficient
route, but are not improved by merely reinterpreting a physical rank list.

Thus the bounded physical-source conjecture has a positive answer with
the chronology and guard specification above. Removing `R chi` from
every scalar-history, metric-quantization, or decoder precision is a
strictly larger unresolved claim.
