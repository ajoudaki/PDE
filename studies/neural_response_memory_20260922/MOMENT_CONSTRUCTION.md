# Autonomous closure in the agreed notation

Internal construction and conditional theorem, 2026-09-24. Numerical evidence
is reported separately. This note uses the agreed m,Q,F,K,E notation. No
compatibility-only or width-uniform theorem is asserted.

The complete collective state m=(m1,m2) contains the first-layer weights,
readout weights, training responses and retained history moments. The model
keeps W0=W2(0) and its transpose. There are finitely many training samples;
all empirical averages below are uniformly weighted, as in the experiments.

## The two shared coordinates and the meaning of a moment

Two shared scalar coordinates of m are reported through Q. Q_rms is the
current residual RMS, and Q_length is one plus accumulated learning activity:

\[
 Q_{\rm rms}^2=\frac1{|\mathcal D|}\sum_a\widehat r_a^2,
 \qquad \dot Q_{\rm length}=Q_{\rm rms},
 \qquad Q_{\rm length}(0)=1.
\]

The second coordinate evolves from current residuals. It is not physical time
or a prescribed training schedule. Q_rms can be maintained algebraically or
with its exact rational lifted equation given below.

For each sample a, retain P moment vectors in each layer. The notation
m_{1,a}^{(k)}, m_{2,a}^{(k)}, k=0,...,P-1, denotes these coordinates of the
existing population states, not new kinds of objects. They are integrals of
past first-layer responses and residual-weighted backward responses against
shifted Legendre polynomials on the entire current activity interval.
The backward response is divided by residual RMS when the interval is
parameterized by activity; its time derivative source is therefore simply
r delta2, with no division in the operational raw-moment equations.

An initial interval of length one has constant forward response h1(0) and
zero backward source. Its contribution to the true learned-weight history
integral is exactly zero. It avoids a singular zero-length initialization.
It does not bias the infinite-order limit. The Legendre polynomials are an
orthogonal integration basis, not a Taylor expansion of time evolution.

## Explicit F and K

For each sample a and k=0,...,P-1, the moment coordinates obey

\[
 \dot m_{1,a}^{(k)}
 =Q_{\rm rms}\widehat h_{1,a}
 -\frac{Q_{\rm rms}}{Q_{\rm length}}
 \left(km_{1,a}^{(k)}+\sum_{j<k}(2j+1)m_{1,a}^{(j)}\right),
\]

\[
 \dot m_{2,a}^{(k)}
 =\widehat r_a\widehat\delta_{2,a}
 -\frac{Q_{\rm rms}}{Q_{\rm length}}
 \left(km_{2,a}^{(k)}+\sum_{j<k}(2j+1)m_{2,a}^{(j)}\right).
\]

The triangular coefficients follow by differentiating the moment integrals
as their interval expands. They are not chosen damping parameters. Initialize
m1^(0)=h1(0), m1^(k)=0 for k>0, and every m2^(k)=0. Define

\[
 K(m,Q;W_0)
 =-\frac{2}{|\mathcal D|Q_{\rm length}}
   \sum_a\sum_{k=0}^{P-1}(2k+1)
        m_{2,a}^{(k)}\bigl(m_{1,a}^{(k)}\bigr)^\top,
 \qquad
 \widehat W_2=W_0+K/n.
\]

All forward and backward responses are computed at this current reconstructed
network using the original phi and phi'. Outer-layer coordinates obey

\[
 \dot{\widehat W}_1
 =-\frac2{|\mathcal D|\sqrt d}\sum_a
       \widehat r_a\widehat\delta_{1,a}x_a^\top,
 \qquad
 \dot{\widehat W}_3
 =-\frac2{|\mathcal D|}\sum_a
       \widehat r_a\widehat h_{2,a}.
\]

Thus the moments are driven by the current responses, which themselves depend
on the moments. There is no stored target trajectory and no separately
optimized feature basis.

The learned cross-layer coupling consists of current population averages. For
example, applying K/n to a current first-layer response requires only sums of
m2 vectors multiplied by (m1^T h1)/n. The transpose uses (m2^T delta2)/n.
These contractions are entries of Q. W0 h1 and W0^T delta2 are retained as
actual coupled initialized actions. Independence is never imposed.

## Rationality without changing phi

For phi=tanh, include h1,h2 in m and evolve their exact chain rules:

\[
 \dot{\widehat h}_{1,a}
 =\phi'(\widehat z_{1,a})\odot
       (\dot{\widehat W}_1x_a/\sqrt d),
\]
\[
 \dot{\widehat h}_{2,a}
 =\phi'(\widehat z_{2,a})\odot
       (\dot K\widehat h_{1,a}/n
        +\widehat W_2\dot{\widehat h}_{1,a}).
\]

Here phi'(z)=1-phi(z)^2, so these are polynomial expressions in the stored
responses once K and its derivative are substituted. The residual RMS
coordinate evolves by

\[
 \dot Q_{\rm rms}
 =\frac{\sum_a\widehat r_a\dot{\widehat f}_a}
        {|\mathcal D|Q_{\rm rms}}.
\]

Compute moment derivatives, then Kdot, then response/output derivatives, then
this scalar derivative. There is no implicit equation. All RHS operations
are rational on Q_rms>0 and Q_length>=1. Consistent initialization gives the
original tanh responses exactly in continuous time. Exact zero residual is
an absorbing state. Rational equations do not imply rational functions of
time or an analytic population limit. Numerical drift of these identities
must be checked; the experiment includes that check and solver refinement.

## One approximation and its exact E

The retained history moments obey exact transport equations for the
surrogate's own responses. The sole approximation replaces the history inner
product of the forward and backward responses by the inner product of their
first P orthogonal projections. The discarded cross-history covariance is
exactly what is omitted from the learned middle matrix.

Two more current aggregates, already part of Q, are the endpoint projections:

\[
 Q_{1,a}=\frac1{Q_{\rm length}}\sum_{k<P}(2k+1)m_{1,a}^{(k)},
 \qquad
 Q_{2,a}=\frac1{Q_{\rm length}}\sum_{k<P}(2k+1)m_{2,a}^{(k)}.
\]

Differentiating K gives the exact physical defect

\[
 \boxed{E=\frac{2}{n|\mathcal D|}\sum_a
  (\widehat r_a\widehat\delta_{2,a}-Q_{\rm rms}Q_{2,a})
  (\widehat h_{1,a}-Q_{1,a})^\top.}
\]

Consequently the reconstructed network follows canonical gradient flow with
this additional middle-weight velocity, and no other physical modification.
At initialization K=0 and Q1=h1(0), hence E=0 for every initialization and
P>=1. In particular, the Gaussian mean-squared initial-defect certificate is
zero exactly, without a Monte Carlo approximation. This certifies the initial
velocity; it does not by itself prove accuracy at positive time.

## Derivative-moment interpretation and conditional global convergence

Integration by parts turns each response moment into its current endpoint
value minus a weighted integral of its derivative. For the backward moment
there is also the known initial-source correction from the zero prefix.
This is an exact change of state coordinates. The complete expressions and
proof are in RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md, section4. The implemented raw
moments are the numerically better-conditioned coordinates of that same
system; they are not a different approximation. No high time derivatives or
nonzero Taylor radius are assumed.

If total learning activity is uniformly bounded, the first-layer histories
are uniformly Lipschitz in activity, and the normalized residual-weighted
backward histories have uniformly bounded total variation, orthogonal
projection gives

\[
 \|E(t)\|_F\le
 \frac{\text{constant}}{\sqrt{2P-1}}Q_{\rm rms}(t).
\]

The constant depends explicitly on those bounds and the fixed initial prefix,
not on P. This is a proved conditional defect estimate, not a fitted rate
from experiments. It remains meaningful for nonanalytic histories.

For global tracking, additionally require a common bounded forward region,
a uniform positive gradient loss-decay bound, bounded original velocity per
unit residual, and control of how E changes the loss. For sufficiently large
P the defect estimate preserves exponential residual decay, so both exact
and approximate paths have uniformly small tails after large time. Standard
finite-time ODE perturbation convergence plus those uniform tail estimates
then yields convergence uniformly over all physical time.

These hypotheses have not been proved from nonparallel/non-antiparallel
sample geometry alone. In particular, bounded variation of the normalized
backward source and width-uniform stability remain substantive obligations.
The experiments check finite trajectories; they cannot certify those global
hypotheses or establish an asymptotic empirical rate.

## Size and scope

There are 2n|D|P history scalars, plus the outer weights, training responses
and scalar coordinates. The learned matrix has rank at most |D|P by this
explicit construction. This rank bound was chosen through history projection;
it is not inferred from existence of a finite state. Learned-matrix actions
need only moment factors and population contractions. The fixed n-by-n W0
remains stored and applied. State size grows with the number of samples.
