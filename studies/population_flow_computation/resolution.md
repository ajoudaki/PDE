# Milestone C assessment: unresolved, with a finite independent candidate

The study has not resolved milestone C. It has constructed and implemented a
finite causal population-source approximation with complete saved history and
restart, proved useful fixed-graph identities and consistency components, and
executed bounded diagnostics through physical time 40. It has not proved a
useful end-to-end error/resource certificate for that trajectory, implemented
arbitrary certified precision, or completed the requested promotion reviews.
No result in this study is established book material.

## Exact target and interpretation of independence

The retained model is C.4.7's bias-free two-hidden-layer tanh network on
x=sqrt(2)u, |u|=1, stored independent Gaussian variances (1,1/n,1/n^2), output
division by n, mobilities (n,1,n), unhalved squared loss and physical GF. Its
population state is (w,K,c), initially (g,0,0), with g~N(0,I2). Write A=A0+K,
where the actual initialized action and adjoint remain present and only K is
Hilbert--Schmidt. For a fixed training law,

    H_u=tanh(w·u), Z_u=A H_u, V_u=tanh Z_u,
    f_u=E2[c V_u], D_u=c sech^2 Z_u, Q_u=A*D_u, r_u=f_u-y,
    c'=-2 integral r_u V_u dmu,
    K'=-2 integral r_u D_u tensor H_u dmu,
    w'=-2 integral r_u sech^2(w·u) Q_u u dmu.

The zero population readout uses the proved limit of the small actual finite
Gaussian readout; it is not an initialization prescription for finite-network
comparisons. Every numerical run used one fixed law.

The selected candidate replaces evaluations of A0 and A0* by their causal
joint Gaussian source rules and response corrections. It stores separate
statistical representatives of the two populations, finite covariance matrices,
weighted directional derivatives and all past rank factors. It never stores or
trains a dense P-by-P hidden parameter matrix. Empirical response coefficients
are computed from its own saved representatives. A deterministic source program
with exact expectations is an analytical comparison object, not an input to the
implemented solver. Formal source identities alone do not prove this empirical
process converges along simultaneous refinement.

## Route comparison after the separate attempts were frozen

| Route | What survives | What prevents it from completing C |
|---|---|---|
| Lazy Gaussian conditioning of a finite matrix | Exact causal forward/transpose reuse | Reproduces finite-network training under another representation; ineligible for this task |
| Gaussian-tree spectral/Galerkin representation | Explicit finite algebra, positive ordered joint observation law, conditional common-core convergence | No effective reachable-basis approximation; generic coefficient and dense multiplication costs are prohibitive |
| Source regression with positive query noise | Correct combined-source Stein responses, conditional covariance/reuse algebra | Requires actual generated-moment control, not regression against clean sources or an assumed covariance path; full replay is expensive |
| Weighted random-direction sources | One tangent per representative, all-history causal solver, exact frozen contracted variance bound, fixed-graph adaptive coupling | Uniform practical covariance/response error and propagation under refinement remain unproved |
| Reference inverse-gate coordinates and signed stability certificate | Removes the raw Q multiplier from a global L2 comparison; gives a conditional a posteriori certificate | Global constants still enormous; no moderate verified signed amplification bound on the needed error tube |

The opening recommendation in causal_sampling_route.md is superseded by this
eligibility assessment. Its frozen calculations remain as a negative route
record. The spectral and practical-certificate conditional theorems have not
been relabeled as approximation theorems with their hypotheses discharged.
Gaussian marginal tails and energy bounds alone do not give a raw-weight L2
derivative bound: practical_certificate_route.md supplies a scoped counterexample.
That example does not show instability of the actual initialized trajectory.

The integrated-query packages in gaussian_calculus.md and finite controls
Section 13 were read completely in the relevant scope. Their arctan, third
hidden layer, feature-clock and clipped hypotheses are not imported into this
tanh physical flow. C.4.9 controls accumulated forcing and source histories;
it supplies no cheap Gaussian integration or history compression theorem.
There is no demonstrated advantage from changing GF to GD for the named
source-computation obstacle, so the physical time model was retained.

## Precise positive results and check status

1. **Computable admission, internally checked in its stated conservative
   scope.** admission_route.md and admission_check.md give terminating scalar
   interval searches for a sufficient neighborhood. fixed_law_family.md freezes
   Y=1, T=40 and one nonzero rational scale d independently of requested accuracy.
   Its two arcs have correlated coordinates and position-dependent labels.
   Midpoint quadrature has W1 error at most (a+b/2)/(2N). The literal tiny scale
   has not been materialized and these bounds are not practical admission code.

2. **Finite solver and identities, internally checked.**
   directional_solver_spec.md gives every update. The implementation preserves
   all old sources, both source orientations, current-source response diagonals,
   learned rank history, one physical step and five complete RNG streams.
   Independent algebra checks cover frozen derivatives, weighted signs,
   singular clean covariance, reused forward/backward queries and checkpoints.
   These checks concern the finite method, not population accuracy.

3. **Actual generated fixed-graph consistency.** generated_error_proof.md
   compares the dependent empirical rows to iid rows of a deterministic-
   coefficient comparison program, coupled through the training primitives.
   It splits each feedback error into a deterministic paired error and an
   ideal empirical error; it does not condition the generated rows to be iid.
   For fixed finite graph and positive noise s, training covariances are at
   least s^2 I. A polynomial Gaussian cutoff envelope gives a computable bound
   of form C(sqrt(log P))/sqrt(P), with graph-dependent constants. Finite joint
   W2 laws and named contractions are included. This is substantially narrower
   than useful simultaneous time/noise/sample refinement. The fresh bounded
   audit generated_theorem_check.md records exact scope and query-coupling
   qualifications; it is not a complete C review.

4. **Noise-to-clean comparison, coordinator proof draft.**
   noise_and_limit_analysis.md defines noisy queries on the same initialized
   action carrier and bounds their generated local defect. A clean-reference
   tail comparison removes the noise without assuming a noisy-path tail cap.
   It applies to the exact noisy comparison graph, after the empirical bridge,
   not directly to unlike finite representative spaces. Its constants at T=40
   are unusable; the full assembly remains incomplete.

5. **Finite passive integration.** passive_quadrature.md proves an explicit
   one-dimensional Gaussian transport bound, converging under quadrature
   refinement. analytic_passive_quadrature.md additionally proves a sharp
   small-variance remainder via Hermite interpolation and a pole-free tanh
   strip; the coordinator checked its source-projection hypothesis. At the
   two saved final reference states, its q=16 whole-circle formula evaluates
   to approximately 1.1e-11 and 5.1e-12. Conditional variances and means use
   only saved state. These floating evaluations are not interval certification.
   Training sampling, response estimation and propagation remain separate.

6. **Defined broader scope, empirical only.** The same equations accept
   arbitrary finite circle laws with bounded labels and positive noise/steps,
   plus deterministic quadratures of a declared arc family, for any finite
   horizon where the numerical calculation passes its validity checks. No
   closure is fitted. Neither existence nor convergence of a broader
   population flow is inferred from that numerical definition.

## Quantitative obligation audit

| Error or requirement | Available control | Remaining gap |
|---|---|---|
| Fixed-law quadrature | Explicit W1 bound and conservative admitted neighborhood | Practical transfer of its error through the generated dynamics |
| Physical time discretization | Established clean Euler completion and conservative comparison inequalities | Evaluated useful mesh bound for this solver, including continuous-time observations |
| Source-noise bias | Own-state defect and same-carrier clean-reference comparison | Practical constants through time 40 |
| Gaussian reuse and response sampling | Frozen weighted variance identity; actual adaptive fixed-graph consistency | Moderate refinement-uniform generated-error estimate; frozen iid variance cannot be applied to dependent feedback without proof |
| Conditioning | Exact positive training floor s^2, saved-prefix Cholesky, singular clean-query treatment | Useful stability when s shrinks and the history length grows; diagnostic residuals are not certified errors |
| Omitted state/memory | None: every source, tangent, innovation and rank factor is retained | No economical compression theorem; state grows with the number of calls |
| Passive Gaussian expectation | Finite one-dimensional quadrature and explicit error formula | Certified node/function/variance rounding; a passive component does not certify population error |
| Precision and numerical randomness | Float32/64 implementations; full RNG restart; conditional arithmetic-residual proof | Arbitrary-precision backend, certified primitives/functions/linear algebra and an implemented tolerance-to-resource rule |
| Joint internal observations | Typed same-layer initial/current tuples, D/Q and action contractions; fixed-graph law analysis | Full requested population/time/refinement contract and multi-time passive joint query interface |
| Identification | C.4.7 identifies the admitted clean completed flow with actual finite GF | Completed effective bridge from the executed finite process to that flow |

The central unclosed estimate concerns errors **generated along the online
source process**, followed by their propagation. It cannot be supplied by an
oracle trajectory, a formal-program LLN, or a covariance matched independently
at each time. Conversely, proving a moderate propagation multiplier alone does
not bound source errors. A useful next theorem would control the contracted
adaptive covariance/response errors in physical mass weights, preserving both
orientations and all history, and show a self-consistent moderate amplification
bound for those particular error shapes. The current fixed-graph envelope grows
with history length, s^{-1} and individual probe scales (h p)^{-1/2}.

An expensive diagonal construction for separate bridges is not a practical
resource theorem. Even the elementary universal readout bound used by the
fixed-graph proof is C0=exp(80)-1, about 5.54e34. Bounding a D_i D_j moment
only by this supremum gives a Chebyshev sample prescription of order
C0^4/(b eta^2), about 1.9e144 at eta=.01 and b=.05, before response or trajectory
propagation. This is the failure of that sufficient estimate, not a lower bound
on samples needed by the solver. The stronger reference inverse-chart majorant
still permits amplification around exp(1026). Measured small residuals and
hidden moments do not discharge either worst-case argument.

## Executed evidence and resource evaluation

The preregistered budget was twelve trajectories, at most P=4096, 256 steps,
eight data nodes and 3000 total training calls, one GiB target and ten minutes.
All twelve trajectories were used, totaling 2490 calls. Five implementation
tests passed; independent synthetic algebra and checkpoint checks used no
additional trajectories. No finite-network training or broad sweep was run.

The reference baseline P=1024, h=.3125, s=.05 reached t=40 in about 1.79 seconds
with 22.1 MB of saved arrays. The combined P=4096, h=.15625 run reached t=40 in
about 20.0 seconds with 172.3 MB of saved arrays and recorded peak process RSS
430,560 KiB. Timings are recorded diagnostics with the reporting limitations
in validation_results.md, not hard resource guarantees. Total evolution cost
is O(PJ^2+J^3) for J=mN; persistent arrays occupy

    bytes = b_float(10PJ+2J^2+8P+6J) + 8J + 40N.

Configuration, RNG objects, derived law arrays, temporary arrays, numerical
workspace, query products and checkpoint I/O are additional. Saving every
fixed number of steps can itself accumulate O(PJ^2+J^3) disk work/storage.

On nine times and 65 circle directions, differences from baseline were .0647
for halving h, .0560 for quadrupling P, .00213 for halving s, 2.22e-6 for
float32 versus float64, and **.1100 for the combined time/sample refinement**.
The last result prevents an optimistic interpretation of the separate changes.
These single-seed differences mix uncoupled sampling fluctuations with the
changed numerical axis. They are neither population errors nor convergence
rates. In particular no useful .1 or .02 accuracy was certified.

Both computed hidden layers moved substantially: baseline squared changes at
the two training axes were approximately (.093,.067) in layer one and
(.189,.184) in layer two. This is a nonlinear learned numerical trajectory,
not merely resolution of an imperceptible changed-law effect. The fixed
exploratory arc law (.03,.02,.53) was compared at four/eight nodes through t=4;
it is outside the tiny family admitted by the present conservative certificate.

Complete inputs, source versions, commands and evidence paths are in
validation_results.md. finite_network_comparison_protocol.md supplies the
unexecuted independent finite comparison protocol with actual Gaussian finite
readout. A future numerical campaign must be separately budgeted; the current
source trajectory budget is spent.

## Review and promotion disposition

Scoped admission and code checks are preserved as full reports. They are not
the required independent relevance screening, two complete isolated scientific/
code reviews and separate integration review of a successful C addition.
There is no complete self-contained canonical C package to send through that
chain yet. No established files were changed, and no approval request for an
unfinished promotion is made. The partial source, adverse evidence and exact
open obligations remain in this study for possible future research.
