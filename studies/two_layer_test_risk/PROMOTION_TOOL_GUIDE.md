# Fixed two-hidden-layer test-risk certificate

This optional tool regenerates the computer-assisted inequality in
[Global nonlinear learning, C.4](../../../docs/global_nonlinear.md).
It encloses one fixed coefficient using exact rational interval propagation
and a compiled finite-sum kernel. It does not train a network. The chapter
contains the complete flow, Gaussian, angular and arithmetic arguments;
the calculation and those arguments jointly support the signed theorem.

## Fixed mathematical contract

The model has two tanh hidden layers, no biases, input dimension two, and
stored prediction
`f(x)=W3.T tanh(W2 tanh(W1 x/sqrt(2)))/n`. Independent stored Gaussian
initialization variances are `(1,1/n,1/n^2)` and raw block mobilities are
`(n,1,n)`. All blocks train under mean squared loss
`L=(1/3) sum_a (f(x_a)-y_a)^2`, with residual `f-y`.

The three training angles are `0,pi/5,-pi/5`,
`x(alpha)=sqrt(2)(cos(alpha),sin(alpha))`, and labels are
`1,(1-sqrt(5))/4,(1-sqrt(5))/4`. The teacher is `cos(3 alpha)` and test risk
is uniform-circle mean squared error. The baseline `g` freezes both initial
hidden layers and trains its readout with the same normalization. The clock
is chosen uniquely by `L(g_tau(t))=L(f_t)`, with `tau(0)=0`.

The sign convention is `Delta(t)=R(g_tau(t))-R(f_t)` and
`Delta(t)=chi*t^3+O(t^4)`. Thus a strictly positive lower endpoint for `chi`
means lower test risk after hidden learning at equal training loss for
sufficiently small positive physical times. The computed clock coefficient
is defined by `tau(t)=t+beta*t^3+O(t^4)`.

The theorem's exact rational bounds are
`27/100000 < chi < 273/1000000` and
`35309/1000000 < beta < 35311/1000000`. The initial risk is `1/2`; the
leading improvement is only about `0.000272*t^3`. The proof supplies a
width-independent positive interval, but neither its endpoint nor its
remainder constant is numerically evaluated. Finite GF and deterministic
vanishing-step raw GD inherit the comparison in probability on each fixed
`[delta,t0]`, `delta>0`, retaining the common actual small random readout.
There is no quantitative width requirement, uniform finite-width sign down
to zero, later-time guarantee, universal benefit, iid-average risk bound,
sample-complexity theorem, or growing-depth assertion.

## Requirements and numerical conventions

Use Linux, Python 3.10 or later, NumPy, and `g++` supporting C++17.
Ordinary imports of `pde` do not import or compile this optional tool.
The tool has no Git, study-folder, network-access, or archived-output
dependency. All six files in this directory may be relocated together;
the driver finds its kernel beside its own source.

Python and the C++ kernel require binary64 arithmetic. The kernel verifies
round-to-nearest and at least 64 significand bits in `long double`.
The exact compile flags are
`-O3 -std=c++17 -fno-fast-math -ffp-contract=off`.
Do not alter them. Unsupported C++ arithmetic fails at compilation or
execution. Run Python without `-O` or `-OO`; `certify` and the worker reject
optimized Python explicitly because the internal proof-contract checks
use assertions. Run the check scripts without optimization as well.

The only selectable numerical input is the integer strip target `26`
(default) or `30`. Both have proved analytic error envelopes; the displayed
theorem enclosure was calculated and independently reproduced at target 26.
No target-30 execution is asserted. Changing the target cannot change the
model, teacher, number of angles, or definition of the coefficient.
The 256-angle rule has 64 evaluated contributions by exact symmetry.
Gaussian root grids are dyadic and chosen solely from certified root-column
sizes. Each retained axis has count at most 200 and radius between 8 and 9.

The kernel evaluates polynomial/rational approximations to `exp` and
`tanh` with proved arithmetic error; library transcendental accuracy is
not assumed for those sums. NumPy only proposes a root factor. Its stored
dyadic covariance discrepancy is charged exactly, including singular
passive covariances. Every primitive receives its arithmetic, Gaussian
rule, covariance and label-error radii. Subsequent operations round outward
to multiples of `2^-96`. A strictly positive denominator and `|beta|<=1/10`
are checked before accepting the final angular radius `1/1000000`.
All decisions use rational endpoints; decimal displays are explanatory.

## Command and Python interface

From the repository root, this command performs one full certificate run:

```sh
python -B code/tools/two_layer_risk/certificate.py --target 26 --output data/established/two_layer_risk_run01
```

The Python interface is `certify(output, target=26)`. For example, with
`code/` on the import path:

```python
from fractions import Fraction
from pathlib import Path
from tools.two_layer_risk.certificate import certify

result = certify(Path("data/established/two_layer_risk_api01"))
print(result["decision"])
print(Fraction(result["chi"]["lo"]), Fraction(result["chi"]["hi"]))
```

Each example performs the full calculation and needs its own fresh output
directory. The interface returns a newly read, independently mutable,
JSON-compatible dictionary identical to `result.json`. It also prints
progress and the final aggregate. `--help` imports the module and displays
usage without compiling or calculating. Only `certify` is the supported
Python entry point; the interval and finite-sum helpers are private to this
fixed certificate.

`output` accepts a nonempty string or string-valued path-like object.
The final directory must not exist, even if empty, and must not be a
symbolic link. Existing parent directories are allowed, and missing parents
are created. Relative paths are resolved against the caller's working
directory; `~` is expanded. The caller owns the destination and must reserve
it for this run. Existing results are never overwritten. Types, supported
targets, optimization mode and fresh output are checked before creation.
Booleans, floating targets and numeric strings are rejected by the API.

The calculation runs in one fresh worker, with one kernel child active at
a time. The worker receives one-thread settings for OpenBLAS, OMP, MKL and
NumExpr before importing NumPy. Import and API calls leave the caller's
environment unchanged. The worker's cumulative self/child CPU accounting
has the preserved 900-second run gate; each kernel receives a soft CPU limit
of at most 60 seconds, a hard limit one second above it, and a 120-second
wall timeout. The 900-second gate is checked around primitive calls; it is
not a hard whole-process or compiler wall timeout. Timing starts after
worker imports and initial metadata writing; the compiler version query,
build and subsequent calculation contribute to the recorded CPU total.
Avoid concurrent full runs when reproducing the
recorded one-calculation-process contract.

Invalid arguments raise `TypeError`, `ValueError`, `FileExistsError` or
`RuntimeError`. Filesystem errors propagate. Compilation, arithmetic-gate,
timeout and worker failures raise `subprocess.CalledProcessError` in the
public API, with details in retained files when metadata initialization
succeeded. A completed enclosure containing zero returns `INCONCLUSIVE`;
this is not an execution failure. `POSITIVE` and `NEGATIVE` require a strict
rational endpoint sign and remain conditional on the complete proof and
arithmetic contract. A run may fail safely on an unsupported numerical
environment rather than report a certificate.

## Retained output and independent checks

`metadata.json` records source hashes for the executing Python source and
C++ kernel, their build command and binary hash, Python/NumPy/compiler and
platform versions, thread settings, fixed error configuration, status and
timing. `compile.log`, `constants.json`, and `angle_000` through `angle_063`
retain all primitive input text, echoed binary64 input/output bits, grid
choices, exact covariance and label errors, node counts and rational
contractions. `result.json` records the enclosing fractions, raw teacher
projection, matching-clock subtraction, beta intersection, angular error
and sign decision. Partial output and failed metadata are preserved for
inspection; a retry requires a fresh directory.

These focused checks perform no scientific coefficient calculation:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/tools/two_layer_risk/check_driver.py --output data/established/two_layer_risk_driver_check01
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/tools/two_layer_risk/check_kernel.py --output data/established/two_layer_risk_kernel_check01
python -B code/tools/two_layer_risk/angle_error_bound.py --output data/established/two_layer_risk_angle_check01
```

The driver check uses independent longer rational series, exact square-root
inequalities, grid inequalities, a direct response-mean oracle on two
supplied rational probability tables, and a Fourier symmetry-weight check.
The kernel check uses an independent rational elementary-function enclosure
and direct small finite-tensor sums, including the zero passive-root branch.
The angular helper verifies a finite rational derivative majorant.
Their inputs and oracles are contained in the sources. They do not require
old results and do not replace the complete analytic proof.
