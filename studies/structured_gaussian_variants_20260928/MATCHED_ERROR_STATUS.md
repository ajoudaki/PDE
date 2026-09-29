# Matched-error compression: selected route and precise proof status

28 September 2026. The user prioritizes a complete compression theorem for
the canonical dense population, for multiple inputs and fixed small labels.
This note records the selected route, actual new bounds, and the remaining
gap. It is not a claimed solution of that theorem.

## Route selected

Use independent Gaussian blocks at initialization, with variance 1/k in
k by k blocks, but retain global canonical learned updates and the response
memories. Do not use fast global mixing, orthogonal blocks, Richardson
extrapolation or a shared-residual signed ensemble in the core proof.
Those modifications add trained universality or trained expansion obligations.
Ordinary Gaussian blocks retain the exact conditioning/interpolation identities.
A bounded-operator rejection version is useful for the direct particle proof.
It is an explicit modified initializer, with the finite-system transfer
failure O(L B exp(-c k)) proved in `PARENT_DIAGNOSTICS.md`; no population
transfer at fixed k is presumed. This technical variant does not replace
the need to prove the ordinary trained Gaussian bias.

The target is the full dense Gaussian population predictor, uniformly over
physical time t>=0 in L2(mu), including the final predictor. Here mu is any
fixed probability measure supported on inputs with ||x||<=sqrt(d). Training
inputs are finitely many normalized, possibly correlated vectors. Hidden
depth L is fixed, tanh is used, the readout initially vanishes, and the
initial dense readout-feature Gram has a positive gap. Small fixed labels
are permitted; labels must not shrink with block size, width or accuracy.
The dense regular population target may be assumed as in the user request.

## Fully derived ingredients

1. `INITIAL_GRAM_RATE.md` proves initialized weak bias O(1/k) and fluctuation
   O(1/sqrt(Bk)). The latter improves on a bare independent-block
   O(1/sqrt(B)) bound because a block's empirical feature Gram itself has
   variance O(1/k). These are initialization estimates.
2. `SMALL_LABEL_KERNEL_CHECK.md` proves a deterministic, multiple-input,
   all-time canonical GF theorem under initial middle-operator norm M and
   readout Gram gap lambda. With A=M+1 and S=sum_{j=0}^{L-1}A^(2j),

       Y <= lambda^(3/2)/sqrt(8S)

   implies rho(t)<=Y exp(-lambda t), total activity <=Y/lambda, and a
   width-independent O(Y^3) whole-test comparison with the initial
   readout-only kernel flow. This is an actual nonlinear remainder bound,
   not a formal analytic expansion or a replacement of the target.
3. `TRAINED_WEAK_RATE.md` independently derives the same initialized rate
   and a uniform cubic remainder for stipulated regular block populations,
   without falsely bounding the unbounded block initializer on full L2.
   Polynomial envelopes of the block operator norms handle that issue.
   It also gives an exact Gaussian interpolation identity isolating the
   missing trained same-half/cross-half response cancellation.

The parent checked the complete covariance recursion and the deterministic
small-label proof, including its normalizations and passive-row estimate.
The two initial-Gram derivations agreed independently. Late in the route,
the parent shared the frozen findings for consolidation; subsequent work is
not described as blind independent replication. The block-population proof
is an a priori estimate on regular flows, not their existence theorem.

4. `BLOCK_PARTICLE_RATE.md`, Sections 1–3, supplies a separate theorem for
   the ACTUAL finite-order old-clock closure under a fixed block operator
   cap: one small-label threshold gives finite total activity, global
   existence, fitting, and passive-input endpoints, uniformly in B,k,q.
   Its exact mechanism is

       integral rho ||v-vhat_endpoint||^2 dt
         = integral rho ||v||^2 dt - ||moment_state(T)||^2

   for zero-prefix sources. Subtracting the constant forward prefix makes
   the identity applicable to forward-response changes. The resulting
   layer-by-layer total-variation estimate and integrated readout
   contraction close the activity bound without assuming loss decay.
   `BLOCK_ACTIVITY_CHECK.md` verifies this scope independently. It does
   not prove dense-target tracking or a uniform physical-time decay rate.
   Section 4's all-time root-B particle theorem uses a stricter threshold
   depending on k,q; it cannot be used for the fixed-Y joint limit.

5. `UNIFORM_ACCUMULATOR_RATE.md` proves, under the SAME single small-label
   threshold as item 4,

       integral_0^infty ||D_ell(t)||_op dt <= C Y^3/q,
       sup_{t>=0} ||Wcorr_ell(t)-Aown_ell(t)||_op <= C Y^3/q,

   where Aown exactly accumulates the finite-q closure's own canonical
   updates, and D_ell is the difference of their velocities. C is independent
   of B,k,q and time. No extra operator is stored by the algorithm. The
   moment-energy identity equates integrated endpoint-error energy to a
   final-interval projection tail. A lower-layer-only derivative recursion
   proves uniform activity-H1 regularity of the forward histories; their
   Legendre tails are O(1/q), while only backward L2 control is needed.
   The parent checked the complete final derivation. This new integrated
   source consistency is stronger than a terminal reconstruction estimate,
   but does not bound the feedback between two different trajectories.

## An honest all-time finite-block comparison

There is a concrete finite-network consequence that avoids assuming a new
block population exists. Let f_{B,k} be the fully trained canonical finite
network initialized with B Gaussian blocks, n=Bk. It still stores a dense
learned matrix in this statement. Fix a dense initial normalized training
kernel with gap lambda_infty>0, and choose any fixed M large enough for the
Gaussian net tail below. Put S=sum_{j=0}^{L-1}(M+1)^(2j) and assume

    Y <= (lambda_infty/2)^(3/2)/sqrt(8S).

For sufficiently large k and n, depending also on a chosen failure budget
delta, the preceding ingredients give

    sup_{t>=0} ||f_{B,k}(t)-f_dense,pop(t)||_{L2(mu)}
      <= C Y [1/k + 1/sqrt(n delta) + Y^2]

with probability at least

    1-delta-2(L-1) B exp(-c k),
    c=M^2/8-2 log 9 > 0.

All constants here are independent of B,k,t. They depend on the fixed
depth, sample count, M and limiting kernel gap. The reference must be the
regular canonical dense limit, including compact-time passive prediction
identification; that is part of the stipulated target. No quantitative
dense-width rate is used.

Here is the complete implication. The Gaussian net proof in
`PARENT_DIAGNOSTICS.md` bounds failure of the middle-operator cap by the
displayed exponential term. The initial-Gram mean-square bounds plus
Markov's inequality give train and L2(mu) test-row errors
C[1/k+1/sqrt(n delta)] on an event of probability 1-delta, and the train
gap at least lambda_infty/2 when that error is small enough. The
deterministic theorem then gives a CY^3 comparison of f_{B,k} with its
own frozen readout-kernel flow for all time.

For completeness, stability of two frozen kernels is elementary. Write
their normalized train matrices as K and K_*, passive rows as p_x and
p_*x, and residuals as r and r_*. Assume K>=lambda_infty I/2 and
K_*>=lambda_infty I. Their residual difference e solves

    e'=-2K e-2(K-K_*)r_*,  e(0)=0,
    ||r_*(t)||/sqrt(m) <= Y exp(-2 lambda_infty t).

Variation of constants and integration yield

    integral_0^infty ||e(t)||/sqrt(m) dt
          <= Y ||K-K_*||/lambda_infty^2.

Both initialized feature norms are at most one in RMS, so
sqrt(m)||p_x||<=1. Subtract and integrate the test prediction equations:

    sup_t |f_lin(t,x)-f_*lin(t,x)|
       <= Y sqrt(m)||p_x-p_*x||/lambda_infty
             +2Y ||K-K_*||/lambda_infty^2.

Taking L2(mu) gives the claimed kernel contribution. The dense regular
population also has a CY^3 comparison with its own initial kernel. This
can be proved directly on its generated spaces with initial action norm
at most two, or passed from the deterministic finite-dense estimates
along the stipulated compact-time width convergence. The exponential
residual and uniform passive-derivative bounds give the same tail estimate
after any fixed T, so this passage controls all t and the final limit.
Combining the two cubic remainders and the kernel comparison gives the
displayed finite-block bound.

The bound is useful, but the Y^3 term is a NONVANISHING ERROR BUDGET when
Y is fixed. It is not an arbitrary-accuracy block-to-dense theorem. The
deterministic non-Gaussian example in `SMALL_LABEL_KERNEL_CHECK.md` shows
why the cubic remainder cannot be discarded merely from norm and Gram
bounds. That example is not a counterexample to Gaussian compression.

## What a complete compression theorem must still supply

For the actual finite moment closure, denote the final all-time error by
E_{B,k,q}. A favorable proposed estimate is

    E_{B,k,q} <= C [q^(-2+o(1)) + k^(-1) + (Bk)^(-1/2)].

This line is a target, NOT an established theorem. It would give
k of order epsilon^-1, B of order epsilon^-1, n of order epsilon^-2,
and q=epsilon^(-1/2+o(1)), with moving state

    O(L m B k q) = O(L m epsilon^(-5/2+o(1))).

The missing trained bias is a bound on the DIFFERENCE of nonlinear
remainders, rather than a small separate bound on each remainder. The
trained fluctuation must also retain the favorable Bk scaling. Item 5
now bounds the actual closure's integrated source defect uniformly, at
order 1/q. Its conversion to a prediction comparison requires feedback
control; the displayed stronger near-1/q^2 target additionally requires a
sharper approximation estimate. Initialization and source consistency
alone prove neither of these trained statements.

Even the weaker particle term B^-1/2 could give a learned-state improvement
if its constants were uniform: with trained bias k^-beta and history error
q^(-2+o(1)), the certificate would cost

    O(L m epsilon^(-5/2-1/beta+o(1))).

The exponent is strictly below four when beta>2/3; beta=1 gives 7/2.
The corresponding fixed storage is O(L B k^2), and fixed forward/backward
work per batch is O(L m B k^2), so this learned-state comparison is not
automatically a total-storage or runtime improvement. No favorable exponent
is claimed until the trained estimates hold with usable joint constants.

The familiar dense epsilon^-4 scaling itself requires a root-width
prediction certificate; it is not used here as a universal necessary-cost
lower bound. Same-width representation ratios are exact bookkeeping,
but cannot substitute for matched-error certificates.

## Current conclusion

Gaussian blocks are the selected proof route. This continuation establishes
new explicit ingredients and a precise Gaussian interpolation target, but
does not establish the requested clean unconditional compression theorem.
No new universality, trained Taylor expansion, width rate or stability
hypothesis has been inserted to declare success. No manuscript or Git
changes were made.
