# Hostile exact-control audit

## Constant and zero activations

For `phi(x)=c`, every hidden feature is the deterministic vector `c 1` and
every hidden-weight and first-layer derivative vanishes.  Only the readout
gradient remains, so at every finite width and every depth

\[
D_nf_n=n\|c\mathbf 1/n\|^2=c^2,
\qquad D_n^2f_n=D_n^3f_n=\cdots=0.
\]

Thus `(A,B,C)=(c^2,0,0)` directly, without evaluating either generic map.
The zero activation is the case `c=0`.

## Deep linear activation

[`linear_diagrams.py`](linear_diagrams.py) is a width-free path-copy
enumerator.  It repeatedly applies `(grad P).grad`, records the exact neuron
index identifications in a union-find partition, performs every terminal
Gaussian Wick pairing, and counts the remaining free index classes.  It does
not import or evaluate either generic normal form.  A separate concrete-width
sparse-polynomial Wick engine in [`linear_wick.py`](linear_wick.py) checks the
same finite-width polynomials.

The exact results are

\[
(A_3,B_3,C_3)=(4,160,13888),\qquad
(A_4,B_4,C_4)=(5,400,73240).
\]

More strongly,

\[
B_{3,n}=160+{400\over n}+{304\over n^2},
\]

\[
C_{3,n}=13888+{98048\over n}+{280768\over n^2}
 +{368640\over n^3}+{185600\over n^4},
\]

and

\[
B_{4,n}=400+{1500\over n}+{2280\over n^2}+{1220\over n^3},
\]

\[
\begin{split}
C_{4,n}={}&73240+{797680\over n}+{3928200\over n^2}
 +{10713920\over n^3}+{16836800\over n^4}\\
&+{14315520\over n^5}+{5120640\over n^6}.
\end{split}
\]

The compact machine-readable record is
[`DEEP_LINEAR_AUDIT.json`](DEEP_LINEAR_AUDIT.json).  The proposed general-
depth polynomial for `C_H` is not used here: a fit through finitely many
depths does not prove a degree bound and remains conjectural.

## Affine activation

A third exact Gaussian-polynomial moment evaluator, applied independently to
each frozen terminal formula for `phi(x)=1+x`, gives

\[
(A_3,B_3,C_3)=(10,540,71152),\qquad
(A_4,B_4,C_4)=(15,1848,591176).
\]

This checks the atom grammar, layer variances `Q^ell=ell+1`, and exact
polynomial moment arithmetic; it is not presented as a third derivation of
the whole generic map.  Independently at finite width, the raw multivariate
operator and moving-flow series agree *exactly as rational numbers* through
order five for both depths at `n=1`, `Q0=4/9`, and a nontrivial rational
parameter seed.  Their common derivative tuples are:

- `H=3`:
  `(17/60, 33577/16200, 38859449/4374000, 79629085207/1180980000,`
  `76530167942779/159432300000, 750057182958242069/172186884000000)`;
- `H=4`:
  `(-28/75, 1337489/810000, -273259891/136687500,`
  `11913373281217/738112500000, 50761854695867567/996451875000000,`
  `5085110772055795102873/5380840125000000000)`.

## Smooth nonpolynomial discriminator

The normalized-sine two-oracle pre-gate passes with worst scaled error
`2.7440568250379693e-14`.  The preregistered 7,700-network regression then
passes all finite, four-batch, and chi-square gates:

| depth | fitted intercept | intercept SE | prediction | `z` | chi-square / df | `p` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 1,276,231.416 | 166,117.428 | 1,076,854.459 | 1.2002 | 1.8194 / 2 | 0.4026 |
| 4 | 21,151,695.385 | 3,501,920.195 | 19,488,618.525 | 0.4749 | 2.0174 / 2 | 0.3647 |

This is empirical support only.  Full records are in
[`TWO_ORACLE_GATE.json`](TWO_ORACLE_GATE.json) and
[`NORMALIZED_SINE_EXPERIMENT.json`](NORMALIZED_SINE_EXPERIMENT.json).
