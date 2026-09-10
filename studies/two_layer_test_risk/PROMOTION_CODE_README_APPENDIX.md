## Certified fixed-model test-risk comparison

The opt-in [two-layer risk certificate tool](tools/two_layer_risk/README.md)
supports the computer-assisted sign proof in
[global-nonlinear C.4](../docs/global_nonlinear.md). It certifies one fixed
coefficient for exactly two tanh hidden layers, the canonical Gaussian
initialization and mobilities, three correlated training inputs, and the
uniform-circle teacher `cos(3 alpha)`. It includes the training-loss clock
subtraction. It is not a training solver or a general-purpose quadrature API.

From the repository root, on the supported arithmetic platform, choose an
output directory that does not already exist:

```sh
python -B code/tools/two_layer_risk/certificate.py --target 26 --output data/established/two_layer_risk_01
```

The tool regenerates every Gaussian-rule input and enclosure, compiles its
private C++ kernel, and saves exact rational bounds and execution provenance.
It requires Python 3.10+, NumPy and the C++17/IEEE arithmetic contract in
its guide; ordinary package imports do not require a compiler. The guide
also supplies an API example and independent exact-arithmetic and supplied-rule
checks. No archived arrays, study files or Git metadata are runtime inputs.

The theorem proves a small strictly positive risk improvement at equal
training loss on a width-independent initial interval. It does not evaluate
that interval numerically, supply a width rate, or assert a universal or
later-time benefit. The complete analytic error proof and finite calculation
are both necessary for the sign; a floating positive estimate is insufficient.
