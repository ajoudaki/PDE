# Reassessing the aggregate cutoff after the J2 stress failures

2026-09-27. Continuation of this study, authorized by the user's request to
resolve whether the failure is structural or admits a better aggregate
construction. Earlier results and source files remain unchanged.

## Research contract

The primary approximation target is the block-Gaussian response-memory
population closure at fixed block size k, training set, and memory order P.
Comparison with canonical dense Gaussian training has an additional,
unproved initialization-replacement step. These two errors must not be
identified. The target norm is the difference of output functions around
the circle, and, for a theorem, uniformly on each prescribed finite time
interval. Constants may depend on that interval but not on original width.

Admissible evolving states are explicitly defined current-state aggregate
contractions and clocks. Neurons, block representatives, histograms,
runtime densities, frozen feature dictionaries, reference forcing and
future-trajectory encodings are not candidate solutions. Initial integration
may use the known initialization law or the same finite initial pool as the
reference; that pool must be discarded before scalar evolution.

The existing output-depth J cutoff is not assumed to be exhaustive. Test
whether it leaves a feedback bottleneck, whether bounded-moment convergence
can be extended to a whole-circle decoder and actual Gaussian blocks, and
whether a complete feedback-dependency selection improves practical accuracy.
An existence theorem with enormous cost does not establish useful compression.
An error of one cutoff does not establish impossibility for all scalar ODEs.

Three scoped theory routes run independently: boundary/dependency selection,
Gaussian and whole-circle convergence, and approximation obstruction. Root
audits their claims against the exact population equations and the recorded
experiment outcomes. All results are internal research, not book promotion.

## Frozen discriminating experiment

This screen tests one structural repair only: start from every output and
every feedback coefficient constituent (F,s,t,and dot-s), and retain one
complete derivative generation from ALL these seeds. Every omitted child is
zero and the existing bounded-moment clipping/penalty remains. It is called
feedback dependency depth 1. It is not identified with output depth J=1 or 2.
No parameters are tuned after seeing an outcome.

Two tasks, in this order:

1. `pair_cos3`, the 60-degree opposite-label pair: existing J2 is poor.
2. `pair_orthogonal_cos1`, the previously tested orthogonal cosine pair.
   It is the favorable case where J2 improved over J1.

Use k=4, P=1, n=1024 solely for matched initial integral estimation, seed 1,
mark bound 3, and training MSE target 0.001. Include 64 equally spaced passive
circle queries plus passive copies of the training inputs. Preserve all
initialization and shared-core numerical checks. Use the same float64 RK45
tolerances and clipping as the prior screen. Scalar training cap is 45 seconds
per case; compilation cap 30 seconds, initial-contraction cap 60 seconds,
maximum full state 500,000 scalars. No larger-order rescue or rerun of a
failed fit. Controls are reused from prior matched saved endpoints.

Primary metrics are scalar-minus-block circle RMS and passive-minus-core
agreement at coincident inputs. Gaussian RMS is secondary and explicitly
includes the block-replacement error. Report achieved training MSE, physical
time, status, state count, and all setup/runtime costs. Unfinished endpoints
must be labeled partial comparisons against fitted references. Compare the
same 64 circle angles with previous J2 outputs, with a 32/64 diagnostic.

Passing requires a meaningful error/state improvement without replacing a
fit by an unfinished endpoint. Even two improvements would justify only this
repair on these cases, not convergence or general Gaussian equivalence.
Failure rejects the practical claim for this repair at this budget; it does
not justify a universal scalar-compression lower bound.

No other training experiment is part of this screen. Algebraic identity,
dependency-count, saved-data and numerical-equivalence checks may run without
training.
