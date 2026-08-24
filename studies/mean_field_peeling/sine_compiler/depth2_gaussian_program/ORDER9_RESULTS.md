# Sine depth-2 jet and Stieltjes audit through order nine

## Models and normalization

The calculation uses the frozen one-input, equal-width, two-hidden-layer
model with all parameter blocks trained and

\[
D_n=n\nabla f_n\mathbin\cdot\nabla.
\]

Both activations were evaluated:

\[
\phi_{\rm raw}(x)=\sin x,
\qquad
\phi_{\rm unit}(x)=\lambda\sin x,
\qquad
\lambda=\sqrt{\frac{2}{1-e^{-2}}}
=1.5208666231788148830\ldots .
\]

The latter has unit Gaussian variance because
\(E[\sin^2 Z]=(1-e^{-2})/2\) for \(Z\sim N(0,1)\).

## Derivative jets

The even derivatives vanish exactly by readout reflection.  The nonzero
derivatives are:

| order | raw \(\sin x\) | unit-variance \(\lambda\sin x\) |
|---:|---:|---:|
| \(F^{(1)}(0)\) | \(1\) | \(4.0370969464656417700\) |
| \(F^{(3)}(0)\) | \(-1.8869998273059311009\) | \(-103.25733114677418891\) |
| \(F^{(5)}(0)\) | \(79.414989816144653057\) | \(29944.432342937282364\) |
| \(F^{(7)}(0)\) | \(-7186.1902521245980087\) | \(-22072427.427508219184\) |
| \(F^{(9)}(0)\) | \(1194738.0652021462630\) | \(31624398864.162903963\) |

Thus the contiguous jets are

\[
\begin{aligned}
F_{\rm raw}^{(0:9)}(0)
={}&(0,\ 1,\ 0,\ -1.8869998273059311009,\ 0,\\
&79.414989816144653057,\ 0,\ -7186.1902521245980087,\ 0,\\
&1194738.0652021462630),
\end{aligned}
\]

and

\[
\begin{aligned}
F_{\rm unit}^{(0:9)}(0)
={}&(0,\ 4.0370969464656417700,\ 0,\ -103.25733114677418891,\ 0,\\
&29944.432342937282364,\ 0,\ -22072427.427508219184,\ 0,\\
&31624398864.162903963).
\end{aligned}
\]

## Output-coordinate moment coefficients

With the convention

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=F'(0)+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2},
\]

the order-nine jet determines exactly four coefficients:

| coefficient | raw \(\sin x\) | unit-variance \(\lambda\sin x\) |
|---:|---:|---:|
| \(\mu_0\) | \(-0.94349991365296555044\) | \(-3.1677619860813018563\) |
| \(\mu_1\) | \(-2.7154965176305915777\) | \(-3.0399973783784623538\) |
| \(\mu_2\) | \(-5.2226030922470658063\) | \(-2.2096699492914202258\) |
| \(\mu_3\) | \(-7.8931446516883407295\) | \(-1.5977968448910770624\) |

These are the coefficients that would have to be Stieltjes moments under the
conjectured representation.  Their negative signs already rule that out at
the accessible finite order.

## Complete accessible Hankel audit

At four moments the accessible PSD matrices are

\[
H_0=[\mu_0],\qquad H_0^+=[\mu_1],
\]

\[
H_1=\begin{pmatrix}\mu_0&\mu_1\\\mu_1&\mu_2\end{pmatrix},
\qquad
H_1^+=\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}.
\]

Every one of the six unique scalar PSD conditions fails for both scalings:

| condition (left-hand side must be nonnegative) | raw value | unit value |
|---|---:|---:|
| \(\mu_0\) | \(-0.94349991365296555\) | \(-3.1677619860813019\) |
| \(\mu_1\) | \(-2.7154965176305916\) | \(-3.0399973783784624\) |
| \(\mu_2\) | \(-5.2226030922470658\) | \(-2.2096699492914202\) |
| \(\mu_3\) | \(-7.8931446516883407\) | \(-1.5977968448910771\) |
| \(\det H_1=\mu_0\mu_2-\mu_1^2\) | \(-2.4463957706850523\) | \(-2.2418755933963651\) |
| \(\det H_1^+=\mu_1\mu_3-\mu_2^2\) | \(-5.8417762443343958\) | \(-0.025343065151294712\) |

Consequently \(H_0,H_0^+,H_1,H_1^+\) are all non-PSD for both
activations.  The additional accessible cross minor also fails:

\[
\mu_0\mu_3-\mu_1\mu_2
=-6.7347792126453501\ldots
\quad\text{(raw)},
\]

\[
\mu_0\mu_3-\mu_1\mu_2
=-1.6559507462009913\ldots
\quad\text{(unit variance)}.
\]

## Computational route and validation

Each scalar Gaussian-program state was kept as a finite sparse sum of
polynomial-times-Fourier terms.  Gaussian expectations were evaluated by the
closed tilted-Wick recurrence; there was no activation-polynomial or Hermite
truncation and no numerical quadrature in the production values.

Two separately assembled coefficient recurrences were run at 100 decimal
digits:

1. ordinary Taylor coefficients with integrated Volterra denominators;
2. derivative-normalized coefficients with independent multinomial and
   differentiated-Volterra weights.

They produced identical 80-significant-digit serialized jets.  Independent
80- versus 100-decimal-digit Taylor runs differed by at most
\(4.54\times10^{-80}\) relatively.  The moments were also computed two ways:
formal series reversion/composition and the triangular identity
\(F'(t)=K(F(t))\).  Their maximum relative discrepancy was below
\(9\times10^{-121}\), and the 80/100-digit moment discrepancy was below
\(1.30\times10^{-79}\).

## Claim boundary

This is a decisive finite-order violation of the stated Stieltjes conditions
for the raw and unit-variance sine activations in the frozen model.  It is not
an arbitrary-order claim and does not transfer to a different activation,
parameter metric, normalization, depth, finite width, or positive-time
dynamics.  Computing \(\mu_4\) and \(H_2\) would require \(F^{(11)}(0)\);
computing \(\mu_5\) and \(H_2^+\) would require \(F^{(13)}(0)\).
