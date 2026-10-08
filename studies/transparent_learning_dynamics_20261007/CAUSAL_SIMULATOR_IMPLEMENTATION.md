# Two-layer causal population simulator

2026-10-07. Implementation of the finite chronological two-hidden-layer tanh system in the complete CANDIDATE_SYSTEM.md, read at SHA-256 d30036d6acc941b21e306e53167d37c62512f31548134ec1b8c069db9e2af9c1.

Implementation: causal_population_simulator.py. Frozen before the supervisor's comparison campaign at SHA-256 4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76. This note does not report that campaign or use dense results to choose coefficients.

Scientific input scope: the complete candidate and the supervisor's implementation/API assignment. No other study, scientific source, dense-comparator source, external library documentation, or experiment result was used to construct the solver. All numerical arrays and arithmetic are float64; NumPy is the only numerical dependency.

## What is implemented

The default geometry has two training inputs \(v_1=e_1,v_2=e_2\) and the passive input \(v_3=(2e_1+e_2)/\sqrt5\). The only labels are \(y_1,y_2\). The implementation uses the physical factor \(2/m=1\), a positive Euler timestep, and two populations of \(N\) quadrature rows.

The lower population retains first-layer features and backward fields; the upper population retains second-layer features, the shared readout, and top backward fields. Every step computes the candidate's current lower features, appends upper colored Gaussian fields, evaluates the upper forward/backward fields and output, appends lower colored Gaussian fields, evaluates the lower backward fields, and finally makes the simultaneous Euler readout/first-layer updates.

All coefficients \(c,C,D,R\) come from the simulator's current and earlier quadrature state. No coefficient is supplied by a dense trajectory. Learned middle-matrix actions are represented by the two history sums; no learned inter-neuron matrix is present. The saved output moments alone are not a restart state: this implementation does not yet expose resumable Gaussian-factor/tangent checkpoints.

The initial first-layer Gaussian row is generated as a two-dimensional standard Gaussian multiplied by the input matrix, so the passive preactivation has the correct exact initial linear relation. Its feature is then tanh of that value. The upper passive Gaussian is generated from the resulting nonlinear feature Gram, not from an incorrect linear combination of the upper training Gaussians.

## Gaussian covariance extension

Each primitive family has its own independent random stream, separate from the first-layer roots. At each new query, the source-population query column is projected onto an existing empirically orthonormal basis using two-pass Gram–Schmidt. A positive retained residual adds a fresh independent standard Gaussian column in the opposite population. Its coefficient is the residual's empirical RMS norm.

This constructs a causal factor of a positive-semidefinite empirical query Gram directly, without inverting a history Gram. The target Gaussian columns are not empirically orthogonalized: they remain independent standard Gaussian draws. The relevant covariance is their Gaussian sampling covariance, not an assertion that a finite target population realizes it without Monte Carlo error.

By default a residual is retained when its empirical squared RMS exceeds \(10^{-12}\) times the original query's empirical squared RMS. There is no default absolute cutoff. Exact zero and dependent queries therefore need no fresh innovation. Positive but very small relative innovations may be omitted; this is a disclosed numerical approximation.

The returned diagnostics record every raw query variance, residual variance, retention decision, retained rank, discarded residual variance, and the maximum discrepancy between the represented primitive covariance and the full empirical two-time Gram. These are diagnostics of the numerical covariance factorization, not a proof of its effect on the whole nonlinear program.

Independent seed streams are not a claim that the two finite quadrature arrays remain statistically independent after interacting through their empirically estimated coefficients. The intended population law has deterministic shared expectations. Their finite-\(N\) plug-in estimates introduce sampling dependence. No convergence rate for this interacting numerical quadrature is claimed here.

## First tangents and the passive-coordinate reduction

The solver differentiates the local scalar circuit with all \(c,C,D,R\) values held fixed. It injects a unit derivative for the formal primitive being probed and zero for other primitive coordinates. It does not differentiate the Gaussian covariance factor, its Gram–Schmidt basis, its eigenvalues, or a whitening seed.

Both tanh derivatives are used exactly:
\[
\phi'(z)=1-\tanh^2z,\qquad
\phi''(z)=-2\tanh z(1-\tanh^2z).
\]
In particular, the current upper response contains the carrier-weighted curvature term
\[
R^\delta_{ab}(k,k)
=\mathbf1_{\{a=b\}}\frac1N\sum_iw_i^k\phi''(z_{2,a,i}^k).
\]
This term has not been frozen or removed.

Even an identically zero or repeated Gaussian primitive retains its formal tangent coordinate. For example, the initial lower primitive has zero covariance but a nonzero possible formal local probe; discarding its tangent would implement the wrong off-support circuit extension.

Only training primitive coordinates require historical tangent arrays:

- A passive lower primitive can affect its own unused passive backward field but cannot enter a training write. Thus every first-layer feature has zero derivative with respect to all passive lower primitives.
- A passive upper primitive affects its own current derivative gate, but never the readout update or an active backward query. Its past effects do not feed subsequent active fields. The current passive diagonal \(R^\delta_{33}(k,k)\) is added explicitly.
- Lower and upper primal Gaussian query families still include all three panel inputs. Only the identically zero historical sensitivity columns are removed.

The lower stored tangent history at step \(k\) has shape \([N,2,2k]\), and the upper stored history has shape \([N,2,2(k+1)]\). Current passive feature sensitivities with respect to active primitives are evaluated and included in the returned response arrays. This reduction follows from the candidate's training-only writes; it is not a rank or small-response approximation.

## API and output conventions

The main callable is:

    simulate_population(
        labels=(0.15, -0.15),
        dt=0.4,
        steps=60,
        population_size=1024,
        seed=0,
        learned_middle_memory=None,
        learned_forward_memory=True,
        learned_backward_memory=True,
        reciprocal_correction=True,
        rank_rtol=1e-12,
        rank_atol=0.0,
        memory_limit_mb=3072.0,
        return_fields=False,
    )

An optional normalized \(3\times2\) input matrix overrides the default geometry. The program rejects a third label.

For \(K=\mathrm{steps}\), the returned dictionary includes:

| Key | Meaning and shape |
|---|---|
| time | Times \(0,\Delta,\ldots,K\Delta\), shape \([K+1]\). |
| f, c | Complete-panel predictions \([K+1,3]\) and training residuals \([K+1,2]\). |
| C["layer1"], C["layer2"] | Two-time feature Grams, shape \([K+1,K+1,3,3]\). |
| D["layer1"], D["layer2"] | Two-time gated backward Grams, the same shape. |
| R["h"], R["delta"] | Expected formal local responses, the same shape; future entries are zero. |
| diagnostics | Covariance-factor diagnostics, memory estimate, timings, field/response maxima, feature drift, frozen-feature comparison, and symmetry defects. |
| fields | Optional primal row histories; absent unless requested. |
| config | Explicit labels, input geometry, timestep, numerical tolerances, seed, and ablations. |

The convention is
\[
C[k,j,a,b]=\frac1N\sum_i h_{a,i}^k h_{b,i}^j,\qquad
R^h[k,j,a,b]=\frac1N\sum_i\partial_{\xi_b^j}h_{1,a,i}^k,
\]
and analogously for \(D\) and \(R^\delta\). Python sample indices are zero-based.

The optional fields are z1, z2, h1, h2, b1, delta1, delta2, eta, xi, and w. They provide a local replay and inspection record but not the complete tangent/factor checkpoint needed for restart.

The command-line entry point supports the paired learned-middle ablation, the reciprocal ablation, a small self-test suite, and optional compressed NPZ output containing the moments, predictions, configuration, and diagnostics. The callable also exposes individual learned-memory directions.

For single-thread execution, set OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, and MKL_NUM_THREADS=1 before importing NumPy. The solver does not silently alter process-wide thread configuration.

## Ablations and comparison diagnostics

Setting learned_middle_memory=False disables both the learned forward and learned backward sums. This is the intended counterpart of keeping the dense middle matrix fixed while still training the first layer and readout. It does not freeze all features.

Setting reciprocal_correction=False removes both reciprocal response terms from the primal circuit. The modified fields, first tangents, responses, and covariance laws are then recomputed. The saved response arrays are the modified circuit's derivatives, even though those coefficients are not used as reciprocal forces in this ablation.

Individual learned_forward_memory and learned_backward_memory flags are exposed for diagnosis. Disabling only one direction generally does not correspond to a gradient-trained dense matrix model.

No frozen-sensitivity-gate control is implemented. In particular, no such switch accidentally removes tanh curvature from the canonical model.

The initial frozen-feature baseline uses the simulator's own initial top feature Gram \(G^0=C^2(0,0)\):
\[
f_{\mathrm{frozen}}^{k+1}
=f_{\mathrm{frozen}}^k+\frac{2\Delta}{m}
G^0_{:,\mathrm{tr}}(y-f_{\mathrm{frozen,tr}}^k).
\]
The reported fitted endpoint is
\[
G^0_{:,\mathrm{tr}}(G^0_{\mathrm{tr},\mathrm{tr}})^\dagger y,
\]
with the remaining training residual also reported. This is a separate constant-feature diagnostic, not the learned-middle-off trajectory.

For equal or opposite labels, the output includes the corresponding training exchange/sign defect and the difference of the two training feature-Gram diagonals. They are measured, not forced to vanish. Finite quadrature breaks exact population symmetry.

The returned kernel_diagnostic is the full candidate expression \(C^2+C^1\odot D^2+S\odot D^1\) on the current diagonal. The code marks it invalid for a gradient-kernel interpretation in an ablation. Even in the full model, its flag identifies the full candidate formula; it does not establish an exact gradient/loss identity for this finite interacting quadrature. It should not be used to assert monotonic loss at an arbitrary Euler timestep.

A rank-tolerance comparison using the same integer seed is not necessarily a strict common-random-number comparison. Gaussian seed columns are drawn only when innovations are retained. If retention changes, later seed assignments can change. The covariance reconstruction errors are the direct factorization diagnostics; a single tolerance-run output difference may additionally reflect finite-quadrature coupling variation.

## Computational cost and bounded allocation

With \(m=2,p=3\), the packed tangent history uses exactly
\[
8Nm^2(K+1)^2
\]
bytes. The remaining histories, covariance factors, moments, and current tangent workspaces are included in a conservative pre-allocation estimate. A requested run exceeding memory_limit_mb raises MemoryError before allocating the large arrays. No disk-backed tangent machinery was added.

| Population \(N\) | Steps \(K\) | Packed tangent history | Conservative total array estimate |
|---:|---:|---:|---:|
| 1,024 | 60 | 116.3 MiB | 164.1 MiB |
| 4,096 | 60 | 465.1 MiB | 650.2 MiB |
| 1,024 | 120 | 457.5 MiB | 556.3 MiB |
| 4,096 | 120 | 1,830.1 MiB | 2,201.2 MiB |
| 4,096 | 240 | 7,260.1 MiB | 8,015.0 MiB; rejected by default |

These estimates exclude interpreter and BLAS overhead and assume return_fields=False. The implementation does not promise the finest timestep at every proposed quadrature size within a 4 GiB cap.

History-tangent contractions have worst-case time order
\[
O\!\left(N(p+m)m^2K^3\right).
\]
Primal Gram/history operations and the incremental Gaussian factorization have quadratic history cost for fixed panel size. No history-rank gap enters the algorithm, but small retained innovations can be numerically sensitive and are diagnosed. This is a direct finite-program numerical implementation, not a history-compression algorithm.

## Verification actually performed before handoff

The built-in small tests passed on the frozen source in 0.073 seconds. They cover:

1. Exact dependent and zero queries in the colored Gaussian sampler.
2. The stationary zero-label law, zero reverse covariance, and repeated forward histories.
3. Exact replay of the primal program while global coefficients are frozen.
4. The output memory identity \(f_a^k=(2\Delta/m)\sum_{j<k,b\le m}c_b^j C^2_{ab}(k,j)\).
5. The full current diagonal curvature response and zero current off-diagonal responses.
6. Central finite-difference checks of local lower and upper primitive sensitivities against the stored \(R\) arrays, including the zero-variance initial lower primitive.
7. Passive probes' lack of feedback into active local fields.
8. The same checks for the no-reciprocal and paired no-middle-memory laws.
9. Rejection by the pre-allocation memory guard.

The replay utility is replay_frozen_coefficients(result, eta_probe=..., xi_probe=...), with a probe given by a time index, a sample index, and an additive amount applied to that formal primitive in every quadrature row. It deliberately does not recompute shared coefficients after the probe.

One single-thread timing pilot was run: \(N=256,K=30,\Delta=0.4\), labels \((0.15,-0.15)\), seed 11. Solver time was 0.1484 seconds, process wall time 0.25 seconds, and maximum RSS 49,420 KiB. The retained upper/lower primitive ranks were 24 and 39. Maximum covariance reconstruction errors were \(1.32\times10^{-10}\) and \(1.43\times10^{-11}\).

This was a runtime and consistency pilot, not a dense-comparison result or a convergence experiment. No larger population campaign was run by this scoped implementation task. The supervisor subsequently took control of the frozen code for the predeclared comparison campaign.

## Approximation boundary

The implementation makes three distinct approximations: finite particle quadrature of population expectations; numerical omission of sufficiently small Gaussian innovations; and the chosen Euler timestep if comparison to physical continuous time is intended. The candidate's finite Euler equations themselves are implemented with their full learned-history and reciprocal-response terms.

The tests verify indexing, chronology, derivatives, degeneracies, and algebraic identities. They do not certify a quadrature rate, tolerance-to-output rate, dense-width correspondence at a growing program length, long-time numerical stability, or a global quantitative approximation theorem.
