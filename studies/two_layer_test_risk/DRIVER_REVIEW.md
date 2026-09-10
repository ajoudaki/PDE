# Internal audit of the certified-coefficient driver

Reviewer: `certification_engine`, 2026-09-10. **Final component verdict: PASS,
no unresolved blocking correction for the frozen version below.** This is an
internal component review of the coordinator's driver, not a fresh isolated
promotion review. The reviewer authored the separate arithmetic kernel, but
did not author the driver, its assembly proof, or the Gaussian/angular error
proofs. No scientific coefficient evaluation was run by this reviewer.

The reviewed final driver SHA-256 is
`a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1`.
The verdict permits executing its declared certificate protocol; it does not
assert the sign before inspecting a successful complete output.

## Complete coverage and dependencies

The reviewer read every line of the initial driver and then reread the
complete final 382-line driver after corrections. The complete 270-line
DRIVER_CERTIFICATION, 339-line CERTIFIED_ERROR, 214-line ANGULAR_CERTIFICATE,
and 88-line angle_error_bound.py were read, including all proof bodies.
The exact coefficient in the complete CUBIC_DERIVATION and all implementing
formulas (14)--(19) were already read and were used for reconstruction.
The complete 140-line independent test source was written and inspected.
The kernel and its arithmetic proof had already been written, inspected and
tested by this reviewer; a separate agent reviews that component independently.

This review does not re-audit the old population-flow existence and remainder
proofs or the whole book. It checks the new coefficient enclosure against
the already identified exact scalar coefficient, preserving its fixed-model
normalization, signed labels, original correlated Gram and matrix responses.
Root startup instructions and the required solve-math-rigorously and
investigate-conjectures skills/references were read for the resumed subtask.

| Final input | SHA-256 |
|---|---|
| certificate_driver.py | `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1` |
| DRIVER_CERTIFICATION.md | `871a474c95a36790604c882949ad1cd5870d0965fe11d16c3380fa134793f3de` |
| CERTIFIED_ERROR.md | `bcf7fa482d948b73c7ba82b60f514776dbd6d3609a3fb429744aaf507a76c9ad` |
| ANGULAR_CERTIFICATE.md | `a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2` |
| angle_error_bound.py | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| CUBIC_DERIVATION.md | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| certificate_kernel.cpp | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| CERTIFICATION_ENGINE.md | `52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16` |
| check_certificate_driver.py | `3313df40cbf8170c423d4951bf06aff9733c3260c6d76e01cb3f3d8cee6de989` |

## Adverse preflight finding and correction

The first arithmetic implementation converted every scalar operand to a
96-bit absolute-grid interval before multiplication. Its operative method was

```python
def __mul__(self, other):
    b = I(other)
    v = [self.lo*b.lo, self.lo*b.hi,
         self.hi*b.lo, self.hi*b.hi]
    return I(min(v), max(v))
```

The trigonometric polynomial used
`Fraction((-1)**k,factorial(power)) * x**power`. At large power the exact
coefficient is much smaller than `2^-96`; widening it first and then
multiplying by a large `x**power` gives an unusably wide interval.
This retained inclusion correctness, but would prevent an informative
coefficient certificate. It was a required practical correction before
coefficient execution, not an observed scientific sign failure.

The initial independent preflight, preserved as
`data/generated/two_layer_test_risk/driver_check_20260910_01/result.json`,
reported driver hash
`3549ddafa8d1e0361c3ebd402ed3d02b01e73a56d7fb25dfabef1e9cf8cc7614`.
Its containment checks passed, but the inspected symmetry-weighted
`cos(3 alpha)^2` interval was approximately
`[-1.154219345462618e43, 2.476448288828849e44]`, despite the exact value 1/2.
The reviewer explicitly reported this adverse observation. This first test
did not yet impose a width gate; its PASS must not be read as a usable
precision certificate. Result hash:
`995609fc65f06c3e17daf52e2b5249eae1e3c86d3953aa137ba34e634351fdb0`.

The coordinator corrected multiplication/division by an exact rational
scalar to apply that scalar to the interval endpoints before outward
rounding. Interval-by-interval rules remain unchanged. The reviewer
checked this branch for positive, negative and reciprocal scalars. Exact
endpoint multiplication preserves inclusion and avoids premature loss of
small coefficients. Both the independent test and the final driver now
require trigonometric interval width below `10^-20`.

The intermediate strict regression run 02 passed for corrected scalar
arithmetic at source hash
`e35ec14156704da126ba3dd82dbf388d3328b8b753457e9d77e2f6f0cff5d88c`.
Its result hash is
`0b6a98f36e898fd74e800a92932769ffad8919e2abd5ffa2befb290ee071e679`.
After the driver added its own width assertion, the reviewer reran the
entire independent check against the frozen final hash in run 03. No
coefficient integral was evaluated in any of these preflight runs.

A separate resource observation was that a fixed 60-second child allowance
could overshoot the remaining total budget. The coordinator now limits each
child by the smaller of 60 seconds and the remaining total allowance with
two seconds reserved. This correction does not change any mathematical
operation, quadrature rule or claimed error bound.

## Mathematical and source checks

**Intervals and constants.** Rational floors and ceilings bound their
arguments, including negative values. Scalar and interval multiplication
use the correct endpoint extrema; interval reciprocals require one strict
sign. The integer-square-root construction covers rational endpoints and
zero. The 64-term arctangent sum ends negative and has a next positive
remainder, as implemented. The displayed tangent identities and quadrant
bounds establish Machin's identity. A separate 100-term exact rational
enclosure is contained in the reported pi interval. Sin/cos truncation
at degree 79 has the claimed `5^80/80!` real remainder. Corrected exact
scalar multiplication keeps all tested intervals narrow.

**Rules and covariance.** For each exact dyadic column, the rational
conditions `a*c<=3/4`, `6a/h-a^2/2>=B`, `h^2<=18/B` imply the required
strip, exponent and Gaussian-mass bounds because pi>3. Truncation radius
is at least eight and at most nine. Spacings are exact dyadics. The
analytic envelope is the at-most-four-dimensional E1--E5 envelope; it
also safely covers lower two-dimensional and training three-dimensional
moments. No Gaussian mass renormalization is present.

Both true lower input covariance and its dyadic-direction approximation
are Gram matrices and positive semidefinite. Likewise the chosen upper
factor has exact dyadic covariance `Lhat Lhat^T`; an inaccurate root or a
clipped passive residual is charged through its exact covariance discrepancy.
Price interpolation is applied between positive semidefinite endpoints,
using the proved regularization passage at singular covariances. No true
passive covariance inverse is assumed. Echoed input/output IEEE bits remove
any dependency on unverified decimal parsing or output formatting accuracy.

**Primitive radii.** The lower covariance constants are 2 for `H_iH_j`,
3 for `d_a d_b`, and 9 for `d_a d_b H_iH_j`. Every upper group was checked
against its strip bound, real bound, half-Hessian-sum constant and signed-label
perturbation. In particular both exact and dyadic label sums are below P,
so `|S^2-S_hat^2|<=2P epsilon_p`; linear S terms cost `epsilon_p`.
Every moment includes the kernel's `10^-9` arithmetic enclosure in addition
to all Gaussian quadrature and covariance terms.

**Responses and contractions.** With array rows indexed by the response
query, `M[b][j]=p_j E[d_jd_b]+1_(j=b)E[Sdd_b]` is the correct derivative
coefficient. The training tensor contraction produces
`D_ab=L_ab V_ab+sum_ij T_abij M_ai M_bj`. The passive `F` contraction retains
both the training-index part `p_i E[d_i d_x]` and the passive diagonal
`E[Sdd_x]`. The passive `B` contraction retains both named derivatives
`E[d_x d_a]` and `E[H_x dd_a]`. Every T index agrees with its lower gate
pair and source pair. The result is `J=4F+(4/3)B`, and `a=2E[SH_x]`.

The clock is `beta=8 A/(3B0)`, with `B0=E S^2` certified strictly positive.
Each node independently verifies the angular hypothesis `|beta|<=1/10`.
Their interval intersection is a consistency check; no invalid node is
repaired by averaging or intersection. Distinct valid enclosures of the
same beta can be used in separate summands without losing inclusion.

**Circle and risk.** The exact integrand is even and pi-periodic, with
zero value at pi/2 because its teacher factor is zero. Thus the endpoint
weight `2/256`, interior weights `4/256`, and the extra factor two in
the risk definition are all correct. The teacher argument is `3 alpha`,
implemented as `6 pi j/256`. The final `10^-6` angular allowance is the
proved bound conditional on the independently checked beta interval.
Raw projection and matching subtraction are both retained. Only exact
rational exclusion of zero determines a sign.

## Independent executed verification

Retained source: [check_certificate_driver.py](check_certificate_driver.py).
The final exact command from the repository root was

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python -B studies/two_layer_test_risk/check_certificate_driver.py --output data/generated/two_layer_test_risk/driver_check_20260910_03
```

It exited successfully in 3.11 seconds. The complete result is saved under
that fresh directory, SHA-256
`b55a951fbc91e07418b0b1d0666d902dc8a92a92bf2c05fb03742e572b040891`.
The test checks exact Machin containment, normalization consistency,
square roots at five fixed rational inputs, fourteen trigonometric
containment/width cases, and both target-26 and target-30 grid inequalities
on three fixed matrices, including zero and highly anisotropic columns.

For contractions it uses two independent finite rational probability tables.
The source assembles Q,L,T and primitive upper moments exactly, then compares
the driver's seven output intervals with a distinct construction that forms
reverse-response means at each individual lower node before multiplying and
averaging. All exact values lie in the corresponding intervals. The test
includes correlated rank-two source geometry and signed weights. It tests
algebra on supplied tables; it is not a claim that those tables replace the
scientific Gaussian law.

An exact Fourier-character check additionally verifies the symmetry-weighted
mean of `cos(3 alpha)^2`. The final enclosing interval is

```
[39614081257132168796771974941 / 2^96,
 39614081257132168796771975395 / 2^96],
```

containing 1/2 with width `454/2^96`, about `5.73e-27`. This resolves the
specific preflight precision failure. The final driver source was read again
completely and its hash matched the test result after execution.

## Final scope

No remaining implementation or proof-assembly defect was found in this
component. The acceptance is tied to the exact hashes above and to the
kernel/analytic arithmetic contracts. It does not certify a numerical result
that has not yet been executed, nor promote a numerical sign to a theorem
without the complete recorded enclosure. Any changed mathematical source
requires renewed affected checks. The reviewer did not stage or commit files,
edit the README, alter the scientific witness, or modify established material.
