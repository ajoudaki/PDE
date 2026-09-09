# Interrupted Gaussian averaging branch — unverified notes

2026-09-08. The user stopped the research while the independent worker
`averaged_row_cancellation` was preparing its report. That worker was
interrupted immediately. No completed `AVERAGED_ROW_RESPONSE.md` existed at
the stop. This file preserves the mathematical content of its interim
messages and the root's proposed identity; it is **not a completed proof,
reviewed result, or counterexample to the target**. Do not cite the claims
below as established without supplying and checking their missing proofs.

The task was to test Gaussian integration by parts before taking absolute
values in the first-row response equations of
[BOUNDED_RESPONSE_MEASURE.md](BOUNDED_RESPONSE_MEASURE.md). It considered
the row fields `V_i(w)=phi'(u_i·w)u_i`, including nonorthogonal input Grams,
and distinguished prescribed controls from actual physical feedback.

## Initial-kick and interior-kick distinction

The worker reported that a response to a kick at the initial Gaussian row
can be bounded by Gaussian integration by parts, when the primitive source
path is held fixed independently of that initial Gaussian. For a kick at an
interior time, the analogous identity involves the score of the reached
conditional law. Freezing the total trained `q` path is not a legal
conditioning argument, since that path depends on the initial row.
Neither the exact regularity hypotheses nor a complete proof were delivered
before interruption.

## Distinct erf-type activation and common weighted volume

The root proposed testing the bounded activation with
`g(z)=phi'(z)=D exp(-kappa z^2/2)`, where `D,kappa>0` are fixed.
For prescribed controls `b_t(w)=sum_i a_i(t)V_i(w)`, the formal identities are

    div V_i(w) = -kappa w·V_i(w),
    div(exp(kappa|w|^2/2) V_i(w)) = 0,
    det DT_t(w) = exp[-kappa(|T_t(w)|^2-|w|^2)/2].

Thus all the supplied-control row fields preserve the same weighted volume.
The initial Gaussian kick score is `(1+kappa) z_i g(z_i)`, a bounded function.
The worker reported the following interior-time form, with a prescribed-control
flow `T_s`, a standard Gaussian row `G`, and transported gate
`Vtilde_j=(DT_s)^(-1) V_j composed with T_s`:

    E F_ij(t,s)
      = c_j(s)(1+kappa) E[phi_i(w_t) G·Vtilde_j(G)].

Its claimed simplification is
`div Vtilde_j=-kappa G·Vtilde_j`; the unresolved quantity is the transported
gate. The reported evolution of that gate contains the nonzero brackets
`[b_s,V_j]`. Consequently the original bound on `z_j g(z_j)` does not
automatically bound the transported score. These claims concerned open-loop
prescribed controls, not a closed construction of the actual trained returns.

## Proposed forward–backward control loop

The worker's final interim message proposed a sine-activation example: drive
only `V_1` forward for flow time `tau`, then exactly backward, on two fixed
physical intervals. The final row equals its initial Gaussian row, but the
worker claimed an exponentially large *signed averaged interior response*
`E F_12(2,1)` for a small positive correlation `Gamma_12=rho`. It stated
that `exp(-tau/2) E F_12(2,1)` tends to a positive constant, with that
constant divided by `rho` tending to `exp(-1)/8` as `rho` tends to zero.
It also proposed an arc-length reparameterization with bounded integrated
row kinetic energy. **No proof of these asymptotics or energy assertions
was delivered before the stop.**

The root's unanswered scope check is essential: actual bounded-activation
paths have a uniform compact-time bound on each unweighted `q_i` in `L2`,
from the bounded readout and bounded initialized-plus-learned operator.
A deterministic control traversing flow time `tau` on a fixed physical
interval must have diverging `L1`, hence cannot retain a uniform control
`L2` bound as `tau` grows. Arc-length reparameterization does not remove
that issue. This proposed loop therefore must not be represented as an
obstruction under all the actual physical bounds, much less as a physical
counterexample. Its precise value, if verified, would be only to test a
weaker claim about Gaussian averaging and supplied controls.

No experiment was run and no external theorem was adopted in this branch.
No further research was performed after the stop request; this file is an
archival transcription of incomplete work.
