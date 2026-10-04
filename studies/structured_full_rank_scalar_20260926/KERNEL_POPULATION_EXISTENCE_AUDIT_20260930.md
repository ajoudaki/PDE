# Audit of Gaussian population existence and the activation extension

2026-09-30. Scoped proof audit by the terminal-activity route agent.
Verdict: PASS for the precise characteristic population solution and
activation class stated in the source. No required correction found.
This is an internal cross-audit, not an isolated promotion review.

## Inputs and complete read coverage

Every line of KERNEL_POPULATION_EXISTENCE_20260930.md was read, including
the final bounded-C² extension and the corrected L≥1 wording. Audited
SHA256:
`d58c7590fa3477c7fa32336cc1a88cf27382340ab31d3370627ae424547f82fd`.

The exact P1 equations were supplied in the supervisor's assignment and
sections 1–2 of AGGREGATE_SCALAR_CONSTRUCTION.md, SHA256
`a13c7cd1a04b1d34ea3c582ce9f79a82a5ae8caddb7edd1eda675ad32299d45f`.
The cubic source, feedback, and decoder proof had already been read in
full and audited in KERNEL_SCALAR_AUDIT_ACTIVITY_ROUTE_20260930.md.
No other study or external scientific source was consulted. Required
mathematical and conjecture skills were applied. No experiments were run.

## Checks

1. **A priori bounds.** Continuous residual fields give seed-uniform
   bounds on c and therefore on r. The scalar comparison
   C≤2 int(C+Y) yields the displayed exponential bound. Integrating A'
   and B' then bounds those variables uniformly in the seed. The
   first-weight velocity has at most one explicit G factor, giving
   ||w(t)-w(0)||≤C_T(1+||G||). These estimates also handle Y=0 and
   preserve L≥1.

2. **Characteristic equations.** On the trial-field set, bounded
   activations bound c,A,B before controlling w. Differentiating their
   vector field introduces at most the two factors G^T and G. Bounded
   first and second activation derivatives therefore give the local
   C(1+||G||²) Lipschitz and forcing bounds used in equation (3).
   They are independent of the size of the initial or evolved w.

3. **Direct field dependencies.** The map's S output depends only on
   integrated local states. Its r,V outputs additionally depend
   instantaneously on the trial S through A S/L. Trial-r dependence
   through L is delayed by its integral. There is no further direct
   input-output edge. Thus the triangular inequalities (5) are valid;
   treating every field difference as O(delta) would have been invalid.

4. **Contraction and invariance.** The weighted norm
   ||S||+eta||r,V|| gives the stated contraction coefficient. Choosing
   eta first and delta second makes it strictly less than one. Output
   bounds on r,S,V depend respectively on c plus labels, B, and A times
   c, so the strict trial-field caps are preserved for small delta.
   The closed set of continuous curves with consistent initial values
   is complete in this norm. The geometric iteration argument proves
   a unique fixed point and hence unique local characteristics.

5. **Gaussian averaging.** For k² independent variance-1/k entries,
   E exp(eta||G||F²)=(1-2eta/k)^(-k²/2) for eta<k/2. The normalization
   in equation (4) is correct. A smaller fixed interval bound makes
   every required polynomial factor times the exponential in (3)
   integrable, uniformly for all shorter intervals. Evolved-state
   correlations with G do not change its underlying Gaussian seed law.

6. **Differentiability.** The S derivative is dominated by
   C(1+||G||); once S and L are C1, derivatives of r,V and passive-query
   outputs are dominated by C(1+||G||²). Gaussian integrability justifies
   differentiating the expectations and continuity of those derivatives.
   Only the finite training fields are required in the fixed point.

7. **Continuation.** For each fixed T, the a priori bounds give common
   restart radii. Local Lipschitz constants do not depend on w's
   magnitude, and G retains the same seed law. The local time step can
   therefore be chosen uniformly up to T. A finite concatenation gives
   existence and uniqueness throughout [0,T], for every finite T.

8. **Bounded-C² extension.** With finite B0,B1,B2, the changed readout
   comparison C'≤2B0(B0 C+Y) is correct. The local field proof still
   involves at most two activation derivatives. The cubic source proof
   requires only

   \[
   |\phi(x+h)-\phi(x)|\le B_1|h|,\quad
   |\phi'(x+h)-\phi'(x)|\le B_2|h|,
   \]

   \[
   |\phi(x+h)-\phi(x)-\phi'(x)h|\le B_2|h|^2/2.
   \]

   These inequalities prove exactly the second- and fourth-order feature
   remainders used by the existing source estimate. Replacing the
   initial features and gates as stated preserves the Gram tensor,
   completion, and decoder identities. No third derivative, analyticity,
   parity, or tanh derivative identity is required. Zero initial readout
   and SPD initial Gram remain conditions for the small-amplitude theorem.

## Consequence and limits

The Gaussian population well-posedness dependency flagged in the earlier
kernel audit is now closed for the prescribed initialization. The small-
amplitude all-time approximation theorem has a well-defined exact flow
as its comparison object, including for the stated bounded-C² extension.

This proof does not establish well-posedness for arbitrary laws with only
eight moments, fitting at arbitrary label amplitude, a sampling-rate
theorem, or extension to unbounded/nonsmooth activations. Those limits are
stated accurately in the source and do not obstruct its present theorem.
