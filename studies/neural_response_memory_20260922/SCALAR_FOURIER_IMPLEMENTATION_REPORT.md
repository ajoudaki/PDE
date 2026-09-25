# Scalar Fourier implementation and two-input test

2026-09-25. Study-local implementation and empirical test, not promotion.
The preregistered method and limits are in SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md.

## Implemented object

`scalar_fourier_engine.py` compiles an autonomous aggregate ODE for the
three-hidden-layer tanh, P=1, original activity-clock population closure.
Training states are connected normalized tree contractions. Angular states
are integrated forests whose query fields share the same angle. All 17
real Fourier weight blocks (J=8) share the same compiled angular operator.
Whole generator monomials are deleted when any required connected coordinate
exceeds the specified grade K. Energy readout was omitted from this first
dictionary. This is the unsaturated practical truncation, not the globally
bounded saturation variant of the theorem.

After initialization the RHS uses scalar coordinates and fixed coefficient
tables only. It neither updates neurons nor calls a network on a query mesh.
The actual initialized matrices enter through initial contraction values.
Initialization uses 256 angular quadrature nodes; refinement uses 512. A
4096-angle grid is used only for external comparison of the final functions.
The returned predictor is a Fourier polynomial, not a recovered weight matrix.

The literal task uses normalized circle angles 10 and 125 degrees, labels
+1 and -1, width 16, three hidden layers, and seed 20260920. These are a
two-input subset of the study's two_clusters_grouped task. All models share
the exact realized Gaussian initialization, normalization and gradient-flow
mobilities. Dense and P=1 population references integrate physical parameters;
the scalar model integrates only aggregates. Each fit stops for reporting at
its first training MSE 0.001, if reached before physical time 40.

## Outcome

**The implemented K=5 scalar truncation runs and fits its internal training
coordinates, but its fitted Fourier predictor is not close enough to dense
training.** The preregistered 0.10 RMS failure threshold is exceeded. K=7
hit the declared equation-count cap, so higher cutoffs remain untested rather
than disproved. No data/seed/architecture search was performed after this result.

| Model | Internal training RMS | Whole-circle RMS difference from fitted dense | Fit time |
|---|---:|---:|---:|
| Dense | 0.0316228 | 0 | 4.0444070 |
| Population closure P=1 | 0.0316228 | 0.0182228 | 4.2349259 |
| Scalar K=5, P=1, J=8 | 0.0316228 | 0.2109774 | 2.8239351 |

The scalar error is 25.11% of the dense predictor's circle RMS; its maximum
pointwise error on the 4096-angle scoring panel is 0.3774303. Its RMS difference
from the population reference is 0.2080303. Comparing at the same physical time
as scalar stopping gives 0.2719854 against dense and 0.2818611 against population,
so a different stopping time does not explain the discrepancy.

A decisive consistency diagnostic is that the scalar Fourier function evaluated
at the two training angles gives (1.2239869,-1.0843980), whereas the internal
training-output coordinates are (0.9582568,-1.0160469). Thus the returned Fourier
predictor's actual training RMS is **0.1692530**, not 0.0316228. The exact full
circle function agrees with its training outputs; a finite Fourier projection
adds spectral error, and independent finite graded truncations additionally
need not preserve the underlying dynamical identity. The grade includes an angle vertex and a Fourier tag, so the
passive output and training-output equations also lose different interactions
at the same cutoff. This discrepancy is a limitation of the truncation, not
evidence that a well-fitted network was reconstructed from those scalars.

The dense Fourier tail beyond J=8 has RMS 0.0053083, and the parent's is
0.0048550. Increasing angular bandwidth was therefore not triggered by the
predeclared 0.01 threshold. The much larger 0.211 error is predominantly in
the retained coefficient dynamics, not omitted angular modes. FFT/Parseval
decomposition gives retained-mode error 0.2109106. Because adding passive
Fourier weight blocks leaves the equations of existing blocks unchanged,
increasing J alone cannot remove this retained-mode error at fixed K.

## Cost and numerical resolution

K=5 retains 331 training patterns and 17 angular patterns, each repeated for
17 Fourier weights, plus one clock: **621 evolving scalar coordinates**.
It has 133,358 retained equation terms after 1,074,572 generated terms are
discarded. Compilation took 6.69 seconds, initialization 0.009 seconds and
integration 3.39 seconds in the primary run. Peak reported process RSS was
about 159 MiB. For comparison, dense width-16 training has 560 moving parameter
entries; the population state has 177 moving entries, with two additional
fixed initialized matrices. This prototype demonstrates scalar autonomy and
width-independent type counts, not a speed or memory improvement.

K=7 stopped at 201,196 retained terms after 4.30 seconds, with 713 training
and 44 angular patterns discovered but the dictionary still incomplete.
K=9 and K=11 were not attempted, following the predeclared stop branch.
The cap is a campaign limit, not a mathematical impossibility result.

Tighter integration (rtol 1e-9, atol 1e-11) together with doubled initial angular
quadrature changed the scalar final curve by RMS **1.36e-8** and its fit time
by less than 1e-7. Corresponding dense and population curve changes were
7.19e-10 and 4.82e-10. These are far below the 0.002 validity gate. Independent
Euclidean-norm and FFT/Parseval rescoring of saved arrays reproduces the scalar
RMS 0.2109774288208284. The numerical discrepancy is resolved for this test;
the 4096-angle maximum is a sampled maximum, not a certified continuum supremum.

The recorded compilation, initialization and solver phases total 27.25 seconds,
well below the 20-minute campaign budget. The independent full algebra replay
took another 10.36 CPU seconds; development checks stayed within their separate
budget. Interpreter startup, plotting and authoring time are not included in
those phase timings. No additional scientific runs followed the declared stop.

The resulting claim is narrow: the specified low-cutoff unsaturated witness
fails this accuracy test. The exact aggregate identities and Fourier evaluator
remain valid constructions; the saturated hierarchy's asymptotic theorem and
possible better finite closures are not contradicted by this failure.

## Checks

The independent validation script `check_scalar_fourier.py` compares all
primitive response templates against a separately coded direct population
velocity, including nonzero history coordinates, denominator derivatives,
reused initialized transposes, and passive circle activations. It independently
reconstructs retained and deleted output-generator monomials, checks compiled
scalar row arithmetic, shared-angle products, normalization, zero-residual
stationarity, Fourier symmetry and width-independent dictionary counts.
Removing all compiler objects, diagrams and physical input arrays leaves the
runtime RHS unchanged. See SCALAR_FOURIER_IMPLEMENTATION_AUDIT.md and the
run's algebra_checks.json for exact results and hashes.

## Reproduction

The files are study-local and use NumPy and SciPy. From the repository root,
use a fresh output directory for each primary reproduction:

```text
python -B studies/neural_response_memory_20260922/run_scalar_fourier.py --phase references --out data/generated/neural_response_memory_20260922/scalar_fourier02
python -B studies/neural_response_memory_20260922/check_scalar_fourier.py --output data/generated/neural_response_memory_20260922/scalar_fourier02/algebra_checks.json
python -B studies/neural_response_memory_20260922/run_scalar_fourier.py --phase scalars --out data/generated/neural_response_memory_20260922/scalar_fourier02
python -B studies/neural_response_memory_20260922/run_scalar_fourier.py --phase refine --cutoff 5 --out data/generated/neural_response_memory_20260922/scalar_fourier02
python -B studies/neural_response_memory_20260922/run_scalar_fourier.py --phase analyze --out data/generated/neural_response_memory_20260922/scalar_fourier02
python -B studies/neural_response_memory_20260922/plot_scalar_fourier.py data/generated/neural_response_memory_20260922/scalar_fourier02
```

The refinement, analysis and plotting commands for the actual completed run
use the same commands with scalar_fourier01 as the directory. Plotting used
Matplotlib 3.8.4 from /home/amir/miniconda3/bin/python, with an explicit temporary
MPLCONFIGDIR. Training used Python's NumPy 1.26.4 and SciPy 1.13.0, one numerical
CPU thread. Raw states, trajectories, circle values,
compiled restart objects, counts and source hashes are retained in
`data/generated/neural_response_memory_20260922/scalar_fourier01/`.

The actual run's `scalar_K5/fourier_model.json` additionally exports the 17
terminal coefficients with their exact evaluation convention. This predictor
can be evaluated at any new circle angle without the compiler, scalar state,
network weights, or stored query grid. It retains the measured approximation
error above. Later runner edits added failure guards and direct coefficient
export only; scientific evolution uses the hashes recorded in each cell.
