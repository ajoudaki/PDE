# Scalar circle endpoint: scoped implementation and saved-output audit

2026-09-25. The assigned implementation and saved-output checks PASS within
the scope below. This is an internal study audit, not a promotion review,
convergence theorem or proof of continuum accuracy. The checker performed
only deterministic tiny checks and analysis of saved runs; it launched no
research trajectory or parameter search.

## Checked artifacts and result

Producer: run_scalar_circle_endpoints.py and scalar_circle_probe_engine.py,
using the existing scalar_aggregate_engine.py and scalar_aggregate_run.py.
Protocol: SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md. Deterministic producer tests:
test_scalar_circle_probe_engine.py, read completely. The separate mathematical
derivation is in SCALAR_CIRCLE_ENDPOINT_THEORY_CHECK.md.

Independent checker: check_scalar_circle_endpoints.py. Receipt:
../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_audit01.json.

The combined check passes **1194 checks, zero failures**. It includes 18 tiny
deterministic checks, all eight completed primary configurations, all 48 primary
endpoint integrations, and the first configuration's six reproduced endpoint
integrations. Saved scalar predictions are reconstructed by literal ordered
contractions; saved dense predictions are reconstructed by a separately written
three-hidden-layer forward pass. Metric and decision rescoring does not call
the producer's scoring or Fourier-evaluation functions.

All scientific NPZ arrays in the repeated configuration match the corresponding
primary arrays bit for bit, including fresh initial coefficients, probe
coefficients, all six endpoint states/histories and saved Fourier readouts.
The primary and reproduction manifests contain identical producer source hashes.
All six frozen primary source hashes match their saved source files.

## Scientific conclusions supported by the saved data

For the four mixed-input configurations, both compared models and the dense
reference reach their own detected 1e-6 training-MSE endpoints. Independent
full-circle RMS rescoring gives:

| Width | Seed | Frozen kernel RMS | Order-four RMS | Order-four verdict |
|---|---:|---:|---:|---|
| 128 | 20260920 | 0.199180966004 | 0.182112927182 | Inconclusive |
| 128 | 20260927 | 0.207661719473 | 0.183115131090 | Inconclusive |
| 256 | 20260920 | 0.206204683755 | 0.177820517450 | Inconclusive |
| 256 | 20260927 | 0.179352138191 | 0.205284960795 | Adverse |

All four order-four comparisons exceed the frozen agreement threshold 0.1.
The last exceeds the adverse threshold 0.2; the other three fall in the
protocol's intermediate band. These are endpoint-function discrepancies,
not trajectory maxima.

For all four alternating-input configurations, neither scalar candidate reaches
the training target by its cap. The producer correctly reports no matched
endpoint, rather than treating the capped functions as trained endpoints.
Their numerical grid discrepancies can describe the capped states but do not
qualify for the protocol's matched-endpoint accuracy verdict.

## Algebra, feedback and finite Fourier readout

The implementation uses only the M training residuals with alpha=2/M. Probe
coefficients are passed to readout and are absent from the training RHS.
Training components of the extended RHS are exactly those of the existing
ScalarHierarchy. The signatures satisfy z'_b=-2r_b/M,
I'_bc=z_c z'_b and J'_bcd=I_cd z'_b. Their contraction with the initialized
f,Theta,C,Q has the required ordering.

The rectangular initializer evaluates training directions only. Its Q mixed
jet includes Dg_c[g_d]; it does not symmetrize c,d or introduce a probe
direction. Tiny nondegenerate cross tensors agree with the corresponding
blocks of a full combined-input initializer. The tiny runtime checks disable
neural field evaluation and confirm that RHS/readout still work. The read
producer tests additionally cover finite-difference Q, explicit passive ODE
agreement, training-probe agreement, own-state restart and Fourier/signature
commutation.

The runner uses U=(cos(angle),sin(angle)), matching its task_data routine.
There is no second division by sqrt(2). The Fourier convention is the normalized
positive-frequency transform F_k, evaluated as

    F_0.real + 2 sum_(k=1)^K (Re(F_k) cos(k angle) - Im(F_k) sin(k angle)).

The independent trigonometric fixture and saved Fourier evaluations verify this
normalization and sign. Grid and off-grid RMS are checked separately. The finite
Fourier predictor defines an output at every angle; passing finitely many spatial
checks remains numerical evidence, not a certified continuous supremum bound.

## Endpoint and numerical checks

The frozen producer stops at its first numerically detected downward loss
bracket between accepted adaptive steps, then locates a root by local dense
interpolation. This is the event rule explicitly documented before the primary
run. It does not certify that no crossing occurred and reversed inside a step.
An analytic one-dimensional decay fixture reproduces its known event time
within 5.42e-9 and its target loss within the deterministic tolerance. An
initially fitted fixture stops at zero. No asymptotic or stability conclusion
is inferred from a detected first crossing.

The audit independently checks saved endpoint losses, times, chronological
histories, absence of earlier saved threshold crossings for fitted runs,
normalization, finite arrays, solver settings, training readout gap receipts,
absolute/relative/max-grid errors, endpoint refinement gates, quadrature gates,
separate Fourier gates, fitted-pair status and final verdicts. The same scoring
uses each resolution's own endpoint. All decisions reproduce.

No conditional integration or spatial/Fourier refinement was needed in the
primary data: there are 48 primary integrations and six reproduction
integrations. The primary campaign receipt records 116.684316 seconds and the
reproduction 2.411920 seconds, below their combined 900-second budget. The
largest recorded primary trajectory cost is 9.345326 seconds. Primary statuses
are 32 fitted and 16 time_cap; all six reproduction trajectories are fitted.
The unexercised conditional branches received source review, not an empirical
branch-execution claim.

## Cancellation check and limits of the audit

An initial rescore using a uniform near-machine-precision comparison flagged
approximately 1e-8 differences in the unfitted alternating order-four readouts.
Those states contract large, cancelling signature terms. The final checker
therefore evaluates the independent literal contractions in long-double
precision and compares saved float64 results against an explicit absolute-sum
rounding bound. For L=1+M+M^2+M^3 terms at order four, it uses
gamma=(8L+32)eps/(1-(8L+32)eps), multiplied by max(1,sum of absolute terms).
The conservative multiplier covers complex Fourier arithmetic as well.

Every checked contraction lies inside that bound; the largest observed
error-to-bound fraction is 0.010684. The largest direct reconstruction
discrepancy is 1.786519e-8. This explains arithmetic association differences;
it does not bound ODE error, model error, coefficient-initialization error or
continuum quadrature error. Those remain governed by the separate tests and
protocol limitations. No producer output was modified to obtain the pass.

The audit checks the implemented formulas and saved evidence, not arbitrary
higher-order convergence, exact continuum compression, untested inputs or
an infinite-width limit. The prior adverse training-path result remains intact.

## Frozen hashes and replay

SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| Frozen protocol | dfca70f9289a4a898f801b4f095190cde50946275c8a99260b94be6a7c595c3b |
| Endpoint runner | 77360ac5fccde8dde1bfcf17c21c41dce0620a533bfe5cff3adb200d07baabac |
| Probe engine | 65820af358b22fb61de975b4805b14d1abdbc59eb0471ecf9dfd5df0b5fa2b57 |
| Aggregate engine | e765083bbf50e536a06dfc820da0a64a53f1b2580cd0c03ef56b873c78a231eb |
| Aggregate runner | d9fbd628f6dd390f8b8b9bc11578b5a30788cd7a1a78589d0f8770055108dbe2 |
| Frozen case file | bfc2fd1ad347982c31b39bdd5f7635da8c3ed7bbfc2df8088d32143eb75422f8 |
| Independent checker | 98a500041ba3ebce04fb74a8459a0ec6416785b905f95683273c9e19a3ce4749 |
| Audit JSON receipt | 5c820eef1856a28f08c6a1d35d8db06a42b571466aee05035c594e2afc22d9c1 |

The checker can replay the bounded audit without research integration:

```bash
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_scalar_circle_endpoints.py \
  --deterministic \
  --runs data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary01 \
  --reproduction data/generated/neural_response_memory_20260922/scalar_circle_endpoint_reproduction01
```

This scoped check used only the supervisor-authorized source files, frozen
primary/reproduction artifacts, required mathematical verification skill and
this checker's own report/code. No other study, Git history, external research
or research trajectory was accessed. Producer and engine files were not edited.
