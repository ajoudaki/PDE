# Coordinator check of the arbitrary-label negative route

2026-10-03. Complete within-study reconstruction of
ARBITRARY_LABEL_NEGATIVE_ROUTE.md, SHA-256
6c08fb81e5b8f8716e1b795ef4d1074476c49ea1433ca9d21892f7987425abe1.
The coordinator read the entire source and the earlier scalar assessment
and its check, with the current canonical equations already read.
This is internal validation, not an independent promotion review.

**Verdict: PASS for the scalar statements and their stated limitations.**
There is no claimed canonical counterexample to validate. The route
correctly leaves nonlinear population well-posedness and transverse
multi-sample behavior separate.

The source uses read-in/readout mobilities \(n\), hidden mobility one,
and the unhalved mean-square loss. For coefficients normalized by
\(m^{-1}\sum c_a^2=1\), its scalar observable
\(P=m^{-1}\sum c_af_a=w^\top H/n\) has readout controlled velocity
\(w'=H\). The hidden parameters remain included in
\[
 P'=\|\theta'\|_{M^{-1}}^2\ge\|H\|^2/n.
\]
Thus for \(R=\|w\|/\sqrt n>0\),
\(R'=P/R\), \(P'\ge(R')^2\), and \(R''\ge0\).
The expansion \(w(u)=uH(0)+o(u)\) gives
\(R'(0+)=\sqrt{Q_0}\); it also supplies the initial interval on
which division by \(R\) is legitimate. Convexity prevents a return
to zero. This proves \(P'\ge Q_0\) and the lower bound on
the projected feature energy throughout existence.

Before a finite target \(Y\), the exact integrated squared speed
is \(P(u)\le Y\). On a finite interval, Cauchy--Schwarz bounds
the remaining path length by \(\sqrt{Y(t-s)}\).
The finite-dimensional state is therefore Cauchy at any finite
maximal endpoint before fitting. A locally Lipschitz vector field
continues it from the limiting finite state. This verifies the
new bounded-target continuation argument without a bounded
activation assumption. It proves existence through the target,
not for every subsequent value of the ascent control.

The control hit is unique, since \(P'\ge Q_0>0\), and has
\(u_*\le Y/Q_0\). A second use of Cauchy--Schwarz gives the
total normalized path length \(Y/\sqrt{Q_0}\).
The scalar physical equation
\(\dot u=2(Y-P(u))\) stays below that hit. Its error derivative
is \(-2P'(u)(Y-P(u))\), which gives exactly the exponential
rate and the factor of two in the integrated-residual assertion.
The zero label is stationary; simultaneous readout/label sign
reversal verifies the negative-label case without activation parity.
The \(Q_0=0\) exception is explicitly excluded.

On an initial normalized norm/operator event, the path-length
bound controls every normalized block and every hidden operator
norm. Bounded slopes and linear growth then control the fixed-depth
forward/backward RMS recursions and their normalized outer-product
gradients. This bounds the vector-field value and each fixed-query
control derivative. It does not give an operator Lipschitz bound
for the full nonlinear vector field; the source does not claim one.

If \(f_a=c_aP\) and \(y_a=c_aY\) hold along an invariant
trajectory, direct substitution gives
\(\dot\theta=2(Y-P)M\nabla P\). Therefore the scalar obstruction
also applies to that exact ray. The proof does not show that such
a relation holds in an independently initialized finite network,
or that perturbations transverse to the ray contract.
For population paths the source explicitly requires a valid
canonical differentiable realization and local continuation;
the finite-dimensional Cauchy argument is not incorrectly used
to establish nonlinear infinite-dimensional local existence.

The conclusion is a restriction on several proposed negative
mechanisms. It is neither a width theorem nor a proof that
arbitrary-label multi-sample counterexamples cannot exist.
No source was modified during this check. No experiments,
manuscript edits or Git writes were used.
