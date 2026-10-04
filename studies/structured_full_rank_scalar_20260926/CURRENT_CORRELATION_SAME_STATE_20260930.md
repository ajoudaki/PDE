# Same-state test of the frozen current-correlation approximations

## Protocol frozen before numerical evaluation

2026-09-30. This is the one additional saved-state pass authorized by the
last section of `CURRENT_CORRELATION_PROTOCOL_20260930.md`. It is independent
of primary candidate fit outcomes, which this scoped author must not read.
The only three cases are `near_pair_sin9`, `cluster_triple_cos9`, and
`cluster_triple_cos1`, using their preserved width-1024 Gaussian dense
endpoints, each at its own saved MSE 0.001 crossing. No new training,
coefficient selection, tuning or trajectory computation is permitted.

Candidate A is already frozen. Candidate B's source and equations will be
read only after the supervisor explicitly announces its final freeze.
The numerical pass must wait for that announcement. The permitted A
coefficients are the constructor-only `preflight_projected` NPZ archives;
no primary fit files are read. Other inputs are the current-correlation
diagnostic report/code/raw JSON, the three cubic input/coefficient archives,
and the three saved dense NPZ/JSON endpoints. Frozen candidate source files
and required process documents are permitted. Initial neural weights are
neither reconstructed nor trained.

The supervisor announced the B final freeze before this pass. Its frozen
`current_gaussian_correlation.py` hash is
`7b37942a3b0a6eaae2d0e52ec4cd0e42e6d82fe08c0cdf17bff69f7965362b90`.
The diagnostic uses exactly `RadialTanhLink(128).evaluate(variance)[0]`;
no alternative link or quadrature is evaluated.

For A, insert the exact dense current feature Gram `K`, outputs `f`, and
readout energy `q` into its fixed projected gate formula

\[
G^A_{ab}=(1-K_{aa})(1-K_{bb})
\left[q-\lambda_a f_a^2-\lambda_b f_b^2
 +\lambda_a\lambda_b f_af_bK_{ab}\right],
\quad \lambda_a=\frac2{1-K^0_{aa}}.
\]

Compare `G^A` with the saved exact current readout-weighted gate Gram `D`,
and `N^A=beta^0 odot G^A` with the saved exact full lower tangent, the sum
of its first- and middle-layer blocks. Record signed matrix differences,
absolute/relative Frobenius errors, and signed absolute/relative contractions
against the unit current residual and weakest initial-feature-Gram direction.
The latter directions are reused from the diagnostic, never optimized.

For B, insert the exact dense moments `b_x=<c z_x>` and `v_x=<z_x^2>`,
where `z_x=W tanh(w x)`, into its frozen output link
`f_B(x)=b_x s_J(v_x)`. Compare with `mean(c tanh(z_x))` at those identical
weights on the saved training inputs and all 256 circle inputs. Record
both raw signed prediction vectors, RMS, maximum absolute error, and
mean signed error. The primary scalar is the full 256-point RMS; the
128-point nested estimate is descriptive. No new link/quadrature order
may be chosen after seeing these comparisons.

Numerical validity: one BLAS thread before NumPy import, float64 and finite
arrays; dense training/circle prediction replay below `1e-10`; task
angles/labels agree exactly between assigned cubic and dense archives;
saved dense NPZ hashes agree with their JSON; K, f, q and D replay the
saved diagnostic to below `1e-10`; A initial Gram agrees with the cubic
initial Gram below `1e-12`; direct A formula agrees with its frozen model
implementation below `1e-12`. Source hashes and constructor-only manifest
are preserved. A failed validity gate makes its associated result
inconclusive, even if the error is large or small.

One pass only, no integrations, at most 10 seconds of numerical work and
input reads. Stop numerical work at 9 seconds and use a 9.5-second safety
alarm. Previous source/metadata inspection did not evaluate candidate
maps. The runner refuses an existing output directory, snapshots used
source files and exact input files, and stores all raw arrays and hashes
under `current_correlation_20260930/same_state/`.

This evaluates approximation maps conditional on exact moments of actual
states. It does not evaluate an autonomous candidate trajectory, a compact
arbitrary-input decoder, its deployment cost, or an additive causal error
decomposition. Supplying exact moments is deliberately stronger information
than either autonomous model receives. The 0.05 candidate accuracy target
is an interpretive reference only; passing it here cannot qualify a
candidate as successful.

## Separately authorized saved-matrix decomposition

After the one-pass results were reported, the supervisor authorized a
posthoc algebraic analysis using only the already saved `beta`, `G^A`,
exact `D` and exact lower tangent `N`. The original pass and source stay
unchanged. No dense evaluation, trajectory, candidate modification or
new scalar-link evaluation is performed. Decompose exactly

\[
N^A-N=\underbrace{\beta\odot(G^A-D)}_{E_{\rm gate}}
      +\underbrace{\beta\odot D-N}_{E_{\rm hidden}}.
\]

`beta odot D` supplies the frozen isotropic hidden response with the exact
current gate Gram. It is an optimistic conditional input, not a fitted
candidate. Report both signed matrices, their Frobenius norms relative
to `||N||_F`, and signed residual/weak-direction contractions relative to
the absolute exact lower-tangent contraction. Verify the matrix sum at
absolute error below `1e-12`. This is an endpoint algebraic decomposition,
not an additive decomposition of final output or trajectory error.

## Results of the single conditional-map pass

**Both frozen approximation maps have material errors even when supplied
with exact moments of the saved dense states.** Candidate A also retains
a substantial hidden-response error after its gate Gram is replaced by
the exact one on the hard tasks. Candidate B's Gaussian output link does
not reproduce the actual dense output from its exact readout–preactivation
and preactivation second moments. These findings concern the maps at the
specified dense states; candidate trajectories can produce different
moments, and state errors can reinforce or compensate for map errors.
Neither result is a lower bound on final candidate prediction error.

The initial pass completed all three tasks in 0.1614 seconds. Its complete
process, including imports, took about 0.228 seconds. The separately
authorized saved-matrix decomposition took 0.0059 seconds. All numerical
work stayed within the 10-second budget. No training, trajectory solve,
candidate change, discarded numerical attempt or numerical rerun occurred.
The primary fit results were not read. A patch-context mismatch during
source preparation preceded execution and produced no numerical data.

| Saved dense task | A gate relative Frobenius error | A lower-tangent relative Frobenius error | B training output RMS | B circle output RMS | B circle maximum absolute error |
|---|---:|---:|---:|---:|---:|
| near_pair_sin9 | 0.755669 | 0.911702 | 0.069291 | 0.055173 | 0.072101 |
| cluster_triple_cos9 | 0.508999 | 0.651300 | 0.255968 | 0.183219 | 0.344928 |
| cluster_triple_cos1 | 0.741950 | 0.727494 | 0.119940 | 0.082828 | 0.124556 |

For B, the training signed errors are respectively
`(+0.069135,-0.069447)`,
`(+0.198632,-0.344928,+0.195268)`, and
`(-0.116913,-0.124526,-0.118243)`.
Its circle mean signed error is below `2.3e-17` on every task because
opposite directions cancel; this does not make its RMS error small.
The 128/256-point RMS differences are approximately `4.44e-10`,
`1.63e-7`, and `5.6e-17`. This is a panel sampling check, not a new
quadrature or continuum error theorem. The supplied exact preactivation
second moments range from 0.1153 to 2.2972 over the tested inputs.

The conditional B defects are already larger than 0.05 on all three
circle panels, substantially so for the hard cluster. This rejects the
claim that the frozen centered Gaussian output relation itself accurately
describes these exact dense moments at that scale. It does not determine
the accuracy of B's autonomous predictions or prove that every closure
using these moments fails. B's finite quadrature formula is the only
link used here; the test includes the statistical ansatz and its frozen
numerical evaluation, without fitting either to these states.

### What exact current gates do and do not repair for A

For the saved-matrix decomposition, all Frobenius ratios below use
`||N_dense||_F` as denominator. The norms of the two terms need not add,
since the matrices have directions and signs.

| Task | gate term relative norm | frozen-hidden term relative norm | total relative norm |
|---|---:|---:|---:|
| near_pair_sin9 | 0.229923 | 0.688683 | 0.911702 |
| cluster_triple_cos9 | 0.355414 | 0.354630 | 0.651300 |
| cluster_triple_cos1 | 0.748629 | 0.064144 | 0.727494 |

The frozen-hidden term is exactly the error of the optimistic kernel
`beta odot D_dense`. Thus even perfect current gate data leave 68.9%
and 35.5% Frobenius error on the hard states. The smooth state's 6.4%
global error is appreciably smaller, but it does not imply accurate
weak-direction response.

Signed relative directional contributions show why a single matrix norm
or apparently successful direction can mislead. Each row divides its
signed contraction by the absolute exact lower-tangent contraction.

| Task / fixed direction | gate term | frozen-hidden term | sum |
|---|---:|---:|---:|
| near pair / residual | +0.778131 | -0.707152 | +0.070979 |
| near pair / initial weak | +0.777452 | -0.707664 | +0.069787 |
| hard cluster / residual | +4.084394 | -0.838072 | +3.246321 |
| hard cluster / initial weak | +3.447834 | -0.729139 | +2.718695 |
| smooth cluster / residual | -0.749300 | +0.073050 | -0.676250 |
| smooth cluster / initial weak | -0.138495 | -0.468653 | -0.607148 |

In particular, A's roughly 7% near-pair lower-tangent directional error
comes from cancellation of two approximately 70–78% errors. Supplying
the exact gate Gram removes that cancellation and leaves about 71%
underestimation. On the hard cluster, the optimistic exact-gate kernel
underestimates residual and weak-direction responses by about 84% and
73%. This is concrete evidence that the frozen isotropic hidden operator
is itself inaccurate in the strong-learning endpoints. It does not
separate freezing in time from isotropization, since both are part of
the same fixed `beta` approximation.

The raw gate matrix has its own, different directional errors. Its
relative signed residual/weak errors are `(+11.217,+11.250)` for the
near pair, `(+44.477,+10.042)` for the hard cluster, and
`(-0.703,-0.764)` for the smooth cluster. Multiplication by `beta` changes
which matrix directions contribute, so these gate errors cannot be read
as relative lower-tangent errors. Full matrices and absolute contractions
are retained to expose small denominators.

### Validity and artifacts

All frozen gates passed. Saved dense training and circle prediction replay
errors were at most `1.34e-15` and `1.00e-15`, respectively. Exact K replay,
initial K0 replay, and agreement between the direct A formula and its
implementation were bitwise zero on this pass. Diagnostic q and D replay
errors were at most `1.78e-15` and `8.89e-16`. The posthoc matrix-sum
identity error was at most `8.89e-16`.

`same_state/same_state.json` stores all source/input hashes, signed output
vectors, exact moments, signed matrix comparisons and validity gates.
The three `*__same_state.npz` archives preserve the corresponding arrays.
`same_state/input_snapshot/` copies the exact files used, including the
saved dense states, constructor-only coefficients, cubic input archives,
diagnostic JSON and constructor manifest. `same_state/sources/` snapshots
the exact evaluated sources and the pre-evaluation protocol. Its report
snapshot intentionally predates these appended results.

The later authorized analysis is separately preserved as
`current_correlation_same_state_decomposition.py` and
`same_state/decomposition.json`, with its own source and input hashes.
The original pass source and data were not changed. This completes the
one authorized same-state pass and its saved-matrix addendum; no new
candidate, fit, or experiment follows from these results.
