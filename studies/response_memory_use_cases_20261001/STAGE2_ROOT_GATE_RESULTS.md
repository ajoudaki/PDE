# Learning-direction diagnosis and a constructive safeguard

The exact finite-order response-memory equations provide a useful diagnostic:
they separate the loss contribution of the reconstructed hidden motion from
that of the outer layers. In the tested Fashion-MNIST input-field learners,
hidden motion opposes instantaneous fitting at87.5–90.6% of sampled training
times, even while the complete learner decreases its training loss. A direct
decomposition attributes this primarily to the shared input projection rather
than temporal lag. The same phenomenon is absent in the tested HAR and housing
trajectories. This is a measured mechanism in the specified models, not a claim
about generic feature learning or the unchanged sample-indexed paper closure.

The derived gate removes positive hidden contributions in continuous time,
without adding moving coordinates. Its practical improvement prediction fails:
it slows useful hidden learning on HAR and housing and does not improve the
validation-selected Fashion prediction. Thus the certificate is supported;
a competitive new optimizer is not established.

## Exact mathematical basis

Use the manuscript's two tanh hidden layers, scalar output f=w^T h^(2)/n,
residual r=f-y, unhalved loss L=E[r²], RMS rho=sqrt(L), and canonical block
mobilities(n,1,n). The first-hidden activation is h and the second-layer
backward response excluding r is delta. Replace sample indices by C fixed
orthonormal input functions psi_c under the empirical training law. This is
the study's input-field extension, not the original sample-indexed algorithm.

Collect the current address coefficients in n-by-C matrices
H=E[h psi^T] and R=E[r delta psi^T]. For order q, define endpoint evaluations
of the stored raw Legendre moments, also n-by-C matrices,

    hstar = (1/tau) sum_{j=0}^{q-1}(2j+1) hbar_j,
    bstar = (1/tau) sum_{j=0}^{q-1}(2j+1) deltabar_j.

The exact physical velocity of the reconstructed hidden matrix is

    V = -(2/n)[R hstar^T + rho bstar(H-hstar)^T]
      = -(2/n)[R H^T + (R-rho bstar)(hstar-H)^T].

The first equality includes every clock and moment-dilation derivative; it
has rank at most2C, independently of q. The second separates instantaneous
input projection from temporal memory lag. Neither term is automatically a
descent direction. For m training examples, define

    S = (2/(nm)) sum_a r_a delta_a^T V h_a,
    D = (||dot W^(1)||_F² + ||dot w||²)/n.

Then dot L=-D+S exactly. Applying V through its factors evaluates this scalar
without forming a dense hidden gradient or dense V. The diagnostic snapshots
also form V for checks, explicitly outside the learner's update. Summing mode
coefficients costs O(nCq); applying the factors to m responses costs O(mnC).
The fixed Gaussian base and ordinary forward/backward computations remain.

For fixed kappa>0, gamma=clip(-S/kappa,0,1) is locally Lipschitz. Scaling ALL
memory derivatives and the common clock derivative by gamma, while preserving
the canonical outer equations, scales V by gamma. Hence the changed optimizer
satisfies dot L=-D+gamma S<=-D. Gating incoming writes alone would not establish
this result. It is a continuous-time guarantee through the existence interval,
not a finite-step descent or fitting theorem. The clock is now dot tau=gamma rho;
this must not be confused with the manuscript's unchanged clock.

Complete proofs, including the commutation criterion and an initialized
finite-q total-loss-ascent counterexample, are in
[STAGE2_CHALLENGE_THEORY.md](STAGE2_CHALLENGE_THEORY.md). The decomposition into
the two displayed terms is the root's follow-up algebra; source autograd checks
independently verify its sum. The finite-q counterexample has binary labels,
the exact unit initialization prefix, zero readout, and every fixed q>=1.
Its sufficiently small initial-amplitude threshold may depend on q. It shows
that increasing temporal order cannot universally repair a bad input index;
it proves neither typical failure under Gaussian draws nor eventual nonfitting.

## Frozen real-data test

[STAGE2_ROOT_GATE_PROTOCOL.md](STAGE2_ROOT_GATE_PROTOCOL.md) was fixed before
these fits. It uses the same three frozen1024-row datasets as the indexing
campaign, with width256, C8,q3, T128, step1/32, three new seeds4101–4103,
and validation-only selection among times16,32,64,128. The gate has
kappa=0.001 times initial label MSE with no tuning. Controls are the ungated
field and rank24 factors at the earlier pilot-selected mobilities. The initial
PCA dictionary is input-only and all models share first/base initialization.
The two field models are repeated at half step on seed4101 in every domain.
This makes33fits. Three additional unchanged-model diagnostic replays split
spatial and temporal contributions after the Fashion finding; their purpose,
seed and all three domains were fixed before execution.

Median validation-selected test RMSE across the three new seeds:

| Learner | Fashion | HAR | Housing |
|---|---:|---:|---:|
| Ordinary input field |0.667920|0.063478|0.317376|
| Gated input field |0.675022|0.068763|0.318595|
| Tuned rank24 factors |0.677733|0.037905|0.313761|

Median paired gated/ordinary ratios are1.00780,1.08325,1.00372; paired
gated/factor ratios are0.99466,1.80800,1.01523, in the same domain order.
No domain passes the required5% improvement against both controls. This is
negative evidence for this particular untuned safeguard as a practical learner,
not an impossibility result for all descent-preserving modifications.

For the ungated Fashion learner, the positive-hidden-contribution fractions
on the128 one-unit-time samples are90.625%,88.281%,87.5%. No sampled total
loss derivative is positive. HAR and housing have no positive hidden sample
in any of these six other ordinary runs. Early negative Fashion contributions
are larger than later positive ones: even the sampled sum over the whole
trajectory is negative. Therefore the high frequency does not mean that the
hidden block is net harmful over training or that freezing it would improve
the final function.

In the seed4101 diagnostic, the instantaneous projected component is positive
at the same90.625% of sampled times. The temporal-lag component is positive
at21.875%; its signed sampled sum is negative. The final relative off-diagonal
feature-Gram block is0.2641 on Fashion, versus0.0585 HAR and0.0945 housing.
This is consistent with the proven obstruction when the input projector no
longer commutes with the moving feature Gram. The worst-direction commutator
criterion alone does not establish actual ascent; the measured S supplies
that separate evidence.

![Spatial and temporal contributions along three initialized trajectories](../../data/generated/response_memory_use_cases_20261001/stage2_root_gate_analysis01/stage2_hidden_loss_contributions.png)

Figure: one fixed seed4101 per domain, width256,C8,q3, full-batch training.
Positive values oppose the current training loss; outer dissipation is not
plotted and makes the total derivative negative at the sampled times. The symmetric-log scale includes
both signs. These are derivative contributions, not test-risk attributions.

## Numerical checks and reproducibility

The float64 independent autograd/matrix-JVP oracle tests q1,q2,q4 at perturbed
states, both gated and ungated. Initial12 identities have maximal error4.45e-16;
the extended18 identities also check the spatial/temporal split. All captured
versus eager four-step checks are exactly zero. All33fits remain finite.
Halving the step changes selected target RMSE by at most2.10e-5 and preserves
all selected times. No positive practical claim rests on a difference near
the numerical error. The float32 split identities have maximal absolute
roundoff1.40e-9; the corresponding float64 identities pass the1e-9 gate.

The ordinary-field trajectories in the three diagnostic replays reproduce the
original ordinary-field checkpoints exactly. The learner never creates V or
a dense hidden gradient in rhs; only the diagnostic helper does. The retained
dictionary copies and cached basis are counted. These fields still cost more
total storage than factors in high input dimension and have no proven runtime
advantage. The gating experiment's33fit loops take46.261seconds excluding
process startup; these instrumented timings are not a performance benchmark.

The initial33fit source/protocol are frozen under stage2_root_gate01. The later
three diagnostic replays and expanded source/protocol are frozen separately
under stage2_root_gate_diagnostics01. Original snapshots were not rewritten.
Their raw arrays, scalar outputs, hashes and exact commands remain available.
The reproducible analysis is stage2_root_gate_analyze.py; generated summary
and PNG/PDF are in stage2_root_gate_analysis01. The scalar finite-q ascent check
is also retained flat as stage2_challenge_finite_q.py. Its numerical core is
unchanged from the recorded successful generated-source snapshot; root added
a required --out argument creating a fresh generated directory, so executing
the flat source cannot accidentally overwrite results beside the study source.
The original24tinyODE solves include12reruns solely for a documented
boolean-serialization failure; a12solve CLI validation is separately preserved.

The independent geometry review supports the proof and implementation, and
found a reusable edge case: kappa=.001*labelMSE vanished for all-zero labels.
The current source uses positive fallback kappa=1 in that already-fitted case.
An independent source-level equilibrium check confirms all velocities remain
finite and zero. Every experimental domain has positive labelMSE, so the patch
changes none of the recorded trajectories. The reviewed old source snapshots
remain intact. Two minor wording corrections also distinguish ordinary-only
replays and sampled derivative evidence from all-time claims.

All conclusions above are study results. Independent review is separate;
no theorem or code has been promoted or added to the manuscript.
