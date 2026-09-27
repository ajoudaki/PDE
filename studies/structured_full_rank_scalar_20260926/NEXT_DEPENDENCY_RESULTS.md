# A complete-feedback cutoff: faster fits, still inaccurate circle functions

2026-09-27. The two preregistered tests are complete. No larger-order or
rescue runs followed. Both scalar ODEs reached training MSE 0.001, but this
first dependency level does not give a successful circle-output replacement.

The new selection starts from all output and feedback constituent moments,
including every term in dot-s, and adds one complete derivative generation.
The older J selection expands output descendants while leaving parts of the
feedback hierarchy at fixed depth. The new family removes that particular
structural defect as its depth increases. This does not certify its first
level's accuracy. The derivation and bounded-mark family argument are in
[NEXT_BOUNDARY_ROUTE.md](NEXT_BOUNDARY_ROUTE.md).

## Matched setup and measured outcomes

Both runs use k=4, P=1, n=1024 for the initial empirical aggregate integrals,
seed 1, the same actual initial block matrices/readouts as the controls,
64 circle probes, and passive copies of both training inputs. No block
arrays evolve in the scalar solver. The mark bound is 3; the largest actual
entry is 1.8571, so no initial entries were redrawn. All controls are reused
fitted checkpoints. Scalar and reference endpoints each satisfy MSE 0.001;
they are not comparisons at equal gradient-flow time.

| Task | Scalar-block circle RMS | Scalar-Gaussian circle RMS | Core output RMS against block on training inputs | Max passive/core discrepancy |
| --- | ---: | ---: | ---: | ---: |
| Opposite labels, 60-degree pair | 0.252472 | 0.251199 | 0.002615 | 0.019903 |
| Orthogonal cosine pair | 0.081729 | 0.085372 | 0.003296 | 0.030556 |

These are raw RMS differences of the two predicted functions, without
signal normalization or comparison of teacher risks. The 32/64-grid changes
in the block RMS are 0.0000313 and 0.00000054. These diagnostics are not
rigorous continuum quadrature certificates.

The opposite-label case is now an additional **fully fitted** example of
substantial off-training error: the core training outputs closely match the
reference while the circle prediction does not. Its earlier J2 endpoint was
unfinished at MSE 0.01356, so comparing its earlier RMS 0.21050 with the new
0.25247 is not a matched-fit order comparison.

The orthogonal case permits a matched-fit comparison: the earlier J2
scalar-block RMS was 0.050058 at MSE 0.001, versus 0.081729 here. The new
selection is smaller and faster, but less accurate on this case. It therefore
does not demonstrate the requested improved accuracy/size tradeoff.

## Cost and checks

Each new model has 1,652 training-core contractions, 1,028 contractions per
passive query, and one clock: 69,501 evolving scalars for the full 66-query
panel. The earlier J2 panel has 188,367. The scalar counts are independent
of the original width. This is a 63.1% state reduction, not a 63.1% error
reduction.

Compilation took 0.371/0.361 seconds, initial integration 4.242/4.165 seconds,
and training 0.716/0.687 seconds. The stopping physical times were
3.4160/3.4856, versus the block controls' 4.9972/6.1093. No coordinate reached
the clipping boundary, and no accepted-step loss increase was recorded.
The core is independent of passive-query states; separate and batched RHS
evaluations agree to floating-point precision. Initial passive/core outputs
agree exactly. Finite-depth alias discrepancies nevertheless develop.

Thus clipping activation, inadequate fit threshold, and a 45-second timeout
do not explain these two fitted errors. This does not rule out integration
error by itself; the unchanged adaptive solver uses rtol 1e-5 and atol 1e-7,
and no tolerance refinement was part of this small screen.

The protocol is [NEXT_AGGREGATE_PROTOCOL.md](NEXT_AGGREGATE_PROTOCOL.md), the
new compiler is [next_dependency_closure.py](next_dependency_closure.py), and
the runner is [run_next_dependency.py](run_next_dependency.py). Raw endpoints,
initial moments, histories, templates, reference hashes, source hashes and
metrics are under
`data/generated/structured_full_rank_scalar_20260926/next_dependency_20260927/`.
No new canonical or population reference training was performed.

The separate `NEXT_DEPENDENCY_CHECK.json` audit in that directory passed.
For each task, all 1,580 common core moments and all 318 common passive
moments on each of 66 query lanes agree bit for bit with the prior J2
initialization. A direct reevaluation of every new-template initial moment
at two queries also agrees exactly. The audit recomputed all reported RMS
values, fit criteria, decoder values and hashes without training.

These experiments reject a practical success claim for this first-level
repair. They do not refute convergence of the complete dependency family,
and they do not establish a lower bound against all aggregate scalar ODEs.
