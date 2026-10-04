# Arbitrary labels: negative search and a completed positive special case

2026-10-03. Continuation of the same dense width-rate investigation.
The user permits arbitrary fixed label magnitudes for a negative witness.
Data, activations, labels and depth still cannot vary with width.

**Outcome.** No canonical slower-than-near-root prediction example was
found. The attempted large-label mechanisms instead led to a complete,
strict root-width dense-to-population theorem for **two hidden linear
layers and one training sample**, with arbitrary fixed labels. This is
an internally checked special case. The nonlinear multi-sample question
remains open; its small-label assumption has not been removed.

## The completed population-rate theorem

Use the actual canonical model
\[
 f_n(t,x)=\frac1n w(t)^\top W(t)A(t)x/\sqrt d,
\]
with independent \(A_{ij}(0)\sim N(0,1)\),
\(W_{ij}(0)\sim N(0,1/n)\), \(w(0)=0\).
Both hidden activations are identity. Every parameter is trained:
the squared-loss mobilities are \(n\) for read-in/readout and one
for the hidden matrix. The one training input satisfies
\(\|x_0\|=\sqrt d\), and its label \(y\) is any fixed real number.

For every fixed confidence \(1-\delta\), every query law \(\mu\)
with finite second moment, and all sufficiently large widths,
\[
 \left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2d\mu(x)\right)^{1/2}
       \le C_{\delta,y,\mu}/\sqrt n
\]
with probability at least \(1-\delta\).
The constants do not depend on width or physical time.
The target is the identified canonical population, including
finite-width bias. There is no unproved response assumption,
clipping, orthogonality condition on test inputs, or small-label
restriction in this theorem. There is also no assertion that
constants stay bounded as \(|y|\to\infty\).

The population fitted function is
\[
 f_\infty(\infty,x)=y\,\frac{\langle x,x_0\rangle}{d}.
\]
The proof and complete reconstruction are
[ARBITRARY_LABEL_LINEAR_RATE.md](ARBITRARY_LABEL_LINEAR_RATE.md) and
[ARBITRARY_LABEL_LINEAR_RATE_CHECK.md](ARBITRARY_LABEL_LINEAR_RATE_CHECK.md).
The frozen proof hash checked is
56e6dfaadb443353307b99984d5eb6672bc20ab2ad7ff33256b0327ccf8b4ab7.
Its initial candidate-status wording records the first freeze;
the subsequent check accepts the complete stated theorem.

### Why the negative mechanism became a positive proof

The candidate failure mechanism was concentration into an exceptional
direction of the reused Gaussian matrix at a large fixed target.
Normalize the training read-in and readout as
\(v=A x_0/\sqrt{dn}\) and \(u=w/\sqrt n\), and use the exact
scalar control \(ds/dt=2(y-f_n(x_0))\) for \(y>0\).
The trained equations imply
\[
 u'=Wv,\quad v'=W^\top u,\quad W'=uv^\top,
\]
\[
 u''=
 \left[W_0W_0^\top+
       \bigl(\|v(0)\|^2+2\|u\|^2\bigr)I\right]u.
\]
The term \(2\|u\|^2\) retains hidden-matrix learning. Thus the
entire matrix reuse is organized by one initialized spectral
measure and a shared nonlinear scalar potential.

Before reaching any fixed output target, an energy identity bounds
the parameter path and the control interval. The scalar spectral
propagator then has coefficients with factorial decay. Elementary
Gaussian pair counting bounds the \(k\)-th initialized spectral
moment error by \(C(Ck)^k/\sqrt n\), including its bias.
The factorial decay sums these errors at strict root width.
Finally scalar damping compares the clocks at the same physical
time. This supplies both error production and all-time propagation.

Coordinatewise nonlinear activations destroy this fixed spectral
reduction. The proof therefore does not transfer to the broad
nonlinear activation class merely by a Lipschitz estimate.

## What can be proved without linear activations

For one training sample at every finite depth, smooth finite-network
activations and zero readout, define the controlled ascent
\(\theta'=M\nabla P\), where \(P=f(x_0)\) and \(M\) is the
canonical mobility. Let \(Q_0=\|h^{(L)}(0,x_0)\|^2/n>0\).
The exact identities
\[
 P'=\|\theta'\|_{M^{-1}}^2,\qquad
 R=\|w\|/\sqrt n,\qquad R''\ge0,\qquad P'\ge Q_0
\]
show that every fixed label is fitted exponentially. Bounded
activation values are unnecessary: before \(P\) reaches a finite
target \(Y\), its integrated squared speed is at most \(Y\).
That prevents finite-control blowup before the target, and gives
total normalized path length at most \(Y/\sqrt{Q_0}\).

This is a fitting/existence theorem for the finite network, not a
nonlinear population-rate theorem. It rules out scalar critical
fitting and scalar nonfitting saddle trapping as the requested
counterexample mechanisms. The same conclusion applies to an
actual invariant one-dimensional prediction ray, provided that
relation holds and the relevant canonical flow exists.

Proofs and checks:
[ARBITRARY_LABEL_NEGATIVE_ROUTE.md](ARBITRARY_LABEL_NEGATIVE_ROUTE.md),
[ARBITRARY_LABEL_NEGATIVE_CHECK.md](ARBITRARY_LABEL_NEGATIVE_CHECK.md),
[ARBITRARY_LABEL_GEOMETRY_ROUTE.md](ARBITRARY_LABEL_GEOMETRY_ROUTE.md),
and [ARBITRARY_LABEL_GEOMETRY_CHECK.md](ARBITRARY_LABEL_GEOMETRY_CHECK.md).

## Additional endpoint information and remaining possibilities

For one-sample linear networks at any fixed depth, the first-layer
columns orthogonal to \(x_0\) stay at initialization and are
Gaussian independently of the entire trained state. Consequently
the passive prediction minus
\(\langle x,x_0\rangle f_n(t,x_0)/d\) has strict root-width error
over all time. At the fitted endpoint its conditional distribution
is exactly Gaussian around \(y\langle x,x_0\rangle/d\).
For a nonzero label and a nonparallel fixed query, its standard
deviation is bounded above and below by positive constants times
\(n^{-1/2}\) on a high-probability event. This proves ordinary
root-width sharpness, not a slower-rate lower bound.

For genuinely multi-sample nonlinear dynamics, the residual direction
can rotate. The geometry check derives the precise defect in the
scalar radius-convexity argument. With weighted residual RMS \(\rho\),
activity \(ds/dt=2\rho\), unit residual direction
\(c=(y-f)/\rho\), and \(\gamma=\|\theta_s\|_{M^{-1}}^2\),
\[
 R R_{ss}=\gamma-R_s^2+\langle c_s,y\rangle_m,\qquad
 \gamma\ge R_s^2.
\]
Here \(R=\|w\|/\sqrt n\) and the sample inner product is the
weighted mean. The final term need not have a favorable sign.
It identifies why scalar convexity cannot simply be applied one
residual at a time. No initialized nonlinear trajectory realizing
a harmful critical mechanism, and no slower fixed-query
finite-to-population lower bound, has been constructed.

Two fresh scoped routes worked independently until their concrete
scalar/linear derivations were frozen or compared. All three authors
independently obtained the finite-target scalar extension; the
coordinator and geometry author independently obtained the linear
balance, then exchanged it. The coordinator developed the full
Wick/Volterra population rate; the geometry author reconstructed
that complete proof. The negative-route author reconstructed the
geometry report and supplied the residual-rotation diagnostic.
The coordinator reconstructed the negative route. These are
within-study checks, not independent promotion reviews.

No experiment was run; the existing GPU restriction was respected.
No manuscript, maintained code, Git index, commit or remote was changed.
