# Sine-activation depth-2 derivatives through order five

## Result

For the same equal-width, two-hidden-layer network and width-first operator
\(D_n=n\nabla f_n\cdot\nabla\), the first three nonzero derivatives are:

| activation | \(F'(0)\) | \(F^{(3)}(0)\) | \(F^{(5)}(0)\) |
|---|---:|---:|---:|
| \(\sin x\) | \(1\) | \(-1.88699982730593110088\) | \(79.4149898161446530575\) |
| \(\sin x/s\), \(s=\sqrt{(1-e^{-2})/2}\) | \(4.03709694646564177004\) | \(-103.257331146774188914\) | \(29944.4323429372823639\) |

For both activations,

\[
F(0)=F''(0)=F^{(4)}(0)=0
\]

exactly by Gaussian-readout reflection.

The raw-sine model has

\[
Q_1=E[\sin^2G]
=\frac{1-e^{-2}}2
=0.432332358381693654053\ldots.
\]

The normalized model divides by

\[
s=0.657519853982899632756\ldots,
\]

so its forward variance is one at every hidden layer.  This normalization
changes the derivative values substantially and is therefore reported as a
separate model rather than substituted silently.

## Method and validation

No polynomial approximation of sine was used.  Every activation-moment atom
was evaluated as a closed finite Fourier sum using

\[
E[e^{imG}]=e^{-m^2Q/2}.
\]

For each activation:

- independently frozen primary and independent coefficient maps agreed to
  more than 100 decimal digits;
- 80- and 120-decimal-digit evaluations agreed beyond 60 digits;
- Gauss--Hermite orders 64 and 96 independently reproduced all three values;
- the earlier audited order-one and order-three gates were reproduced;
- the source-hash and parity gates passed.

The raw and normalized evaluators have SHA-256 hashes
`27ebe0883bd97f66b816eaf32c35672af30f02a52f16ceaff798aa52e84047b6`
and
`3bf44dd48f25d68434641f0411dfef37fe02a16253355681c28cb184cf3ffdcb`,
respectively.

## Immediate Stieltjes implication

Although not needed to obtain the derivatives, the negative third derivative
already fixes the first candidate moment

\[
\mu_0=\frac{F^{(3)}(0)}{2F'(0)^2}<0.
\]

Numerically,

\[
\mu_0^{\rm raw}=-0.94349991365296555044\ldots,
\qquad
\mu_0^{\rm unit}=-3.16776198608130185634\ldots.
\]

Thus both sine variants violate Stieltjes positivity already at the first
moment.  This statement is activation-specific and does not alter the
quadratic-model conclusions.

The currently audited activation-generic compiler stops at order five.
Extending sine to orders seven and nine would require a new higher-order
Fourier-state Gaussian program; no values at those orders are inferred here.
