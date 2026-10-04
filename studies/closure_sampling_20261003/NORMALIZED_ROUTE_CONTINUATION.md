# Normalized activations: the continuation result and the remaining theorem

2026-10-04. Continuation of the user's request to prove the full autonomous
compression theorem with unit Gaussian forward scale, a derivative second
moment close to one, and unbounded smooth activations admitted. The full
requested theorem has **not** been proved. The new results below advance
the initialization, real fitting, and actual trained mixed-moment parts
separately. They do not constitute a new label/error/storage triple.

The target remains the same realized canonical Gaussian dense network,
all L hidden layers of width n, zero initial readout, mean squared loss,
mobilities (n,1,...,1,n), physical time, the whole input sphere, and the
fitted endpoint. The existing autonomous compressor is not changed here.
No learned normalization, clipping, residual architecture, or replacement
by a population training law is inserted.

## 1. What “close to one” allows

Put chi=E phi'(Z)^2 and assume E phi(Z)^2=1 for standard Gaussian Z.
Let F(c)=E phi(X)phi(Y) for correlated unit Gaussians, and let
kappa=E phi''(Z)^2 when finite. For the initialized depth-L covariance,

\[
 (F^{\circ L})'(1)=\chi^L,\qquad
 (F^{\circ L})''(1)
   =\kappa\chi^{L-1}\sum_{j=0}^{L-1}\chi^j.
\]

Thus a fixed derivative gain above one, however close, cannot give
polynomial bounds for these initialized tangents at all depths.
The quantitative tolerance |log chi|<=C/L bounds the first gain by
exp(C); a tolerance C log(L)/L still allows polynomial growth. A fixed
chi<1 can instead make the initialized two-point Gram gap exponentially
small. These are scoped initialized observables, not compressor lower bounds.

[NEARCRITICAL_GEOMETRY_ROUTE.md](NEARCRITICAL_GEOMETRY_ROUTE.md) proves
these statements and constructs a nonlinear unbounded family with explicit
stable variance and tunable chi. For alpha>0 define

\[
 Q=\alpha^2+2\alpha/\sqrt\pi+1/3,\qquad
 D=\alpha^2+2\alpha/\sqrt\pi+2/(\pi\sqrt3),
\]
\[
 0<\chi\le D/Q,\qquad
 \phi(z)=\sqrt{\chi/D}
       [\alpha z+\operatorname{erf}(z/\sqrt2)]
       \mathbin{\pm}\sqrt{1-\chi Q/D}.
\]

It has precisely the desired forward and derivative moments. Its real
variance map V(q)=E phi(sqrt(q)Z)^2 obeys

\[
 V'(1)=\frac\chi D
 \left[\alpha^2+\frac{3\alpha}{2\sqrt\pi}
                  +\frac1{\pi\sqrt3}\right]<1.
\]

It is entire, globally Lipschitz on the real line and unbounded. Its slope
on any horizontal strip of half-width a is at most
sqrt(chi/D)[alpha+sqrt(2/pi)exp(a^2/2)]. All scalar constants are computed,
and the interval for chi contains one in its interior.

## 2. All initialized derivative orders now have one common bound

[NEARCRITICAL_ALL_ORDER_ROUTE.md](NEARCRITICAL_ALL_ORDER_ROUTE.md), with
[complete check](NEARCRITICAL_ALL_ORDER_CHECK.md), strengthens the earlier
fixed-order result. For the displayed family define

\[
 S_L=\sum_{j=0}^{L-1}\chi^j,\quad
 B_2=\frac{24\chi}{7\pi\sqrt7D},\quad
 r_L=\min\left\{\frac1{4\max(1,\chi^L)},
                          \frac\chi{4B_2S_L}\right\}.
\]

Then, simultaneously for all integers k>=1,

\[
 \frac{(F^{\circ L})^{(k)}(1)}{k!}
           \le2\chi^Lr_L^{1-k}.
\]

The initialized population feature map is holomorphic along each complex
great circle of imaginary radius sqrt(r_L)/2, with norm at most sqrt(3/2).
At chi=1 this radius is of order L^(-1/2), with every constant displayed
in the proof. This resolves summation over initialized derivative orders;
it does not resolve the trained finite-network response series.

## 3. Actual trained mixed moments: two gates, two different scopes

The normalized shifted erf of the previous investigation has two genuine
trained results, neither using a Gaussian approximation of the trained
state:

- [TRAINED_NORMALIZED_RESPONSE_ROUTE.md](TRAINED_NORMALIZED_RESPONSE_ROUTE.md)
  and its [check](TRAINED_NORMALIZED_RESPONSE_CHECK.md) give an all-time,
  whole-query-sphere first-gate bound
  ||phi''(z^(1)) R^(1) J^(1)||_(2,n)<=C_delta Y for two hidden layers
  and one training input, with explicit constants independent of width.
  Here J is the input derivative of the preactivation and R is its
  parameter response per unit negative-residual clock.
- [TRAINED_TWO_LAYER_TANGENT_STABILITY.md](TRAINED_TWO_LAYER_TANGENT_STABILITY.md)
  and its [check](TRAINED_TWO_LAYER_TANGENT_CHECK.md) close both gates in
  a weaker, activity-integrated norm at the training input. For all
  transverse unit input directions, the actual top hidden-feature
  derivative changes by at most
  8 D_P sqrt((d-1)/delta) Y^2 over the entire trajectory, including its
  limit. D_P and the admissible label cap are explicit elementary
  expressions in the proof. The same method controls the integrated
  top mixed product, without first proving its unweighted time supremum.

The mechanism is exact frozen-column independence: A=[a,G] after rotating
the observed input to e_1, with G constant and independent of the entire
training trajectory. At the observed input, the top tangent is
P(t)G u, P=diag(phi'(z^(2))) W diag(phi'(a)). The actual RMS velocities
bound ||P'||_F/sqrt(n). Integrating before taking the conditional Gaussian
L2 norm gives the all-time estimate. This is substantive trained progress,
but the independence fails at arbitrary query gates, and it has not been
extended to all response orders or arbitrary depth/data.

## 4. A fully explicit general-depth real fitting theorem without B_0

[EXPLICIT_UNBOUNDED_NORMALIZATION_ROUTE.md](EXPLICIT_UNBOUNDED_NORMALIZATION_ROUTE.md)
proves an original-dense-flow result for any C2 globally Lipschitz real
activations phi_l with E phi_l(Z)^2=1. Identity and normalized exact GELU
are admitted. Let m be the number of training inputs, gamma the smallest
eigenvalue of the unnormalized initialized limiting top-feature Gram,
Y=||y||_2/sqrt(m), and

\[
 s=\max(1,\max_\ell\|\phi_\ell'\|_\infty),\qquad
 F_L=s^2\left[(9s)^{2L-2}
                   +4\sum_{j=0}^{L-2}(9s)^{2j}\right].
\]

On an explicitly specified initialized event whose probability tends to
one for each fixed architecture and dataset, the sufficient label condition is

\[
 Y\le\frac{\gamma}{8m\sqrt{F_L}}.
\]

The original flow fits, converges in parameter space, keeps every real
sphere feature RMS at most two, and satisfies

\[
 \rho(t)\le Ye^{-\gamma t/(2m)},\qquad
 \sup_{\|x\|=\sqrt d}|f_n(\infty,x)-f_n(t,x)|
 \le\frac{65mY}{4\gamma}e^{-\gamma t/(2m)}.
\]

No activation-value bound occurs. This label cap is for dense fitting,
not for the unbounded compressor, and its depth dependence is still
exponential. The stochastic width-confidence threshold is unquantified.
It would be incorrect to replace s by sqrt(chi) in this proof.

## 5. A new finite-width obstruction, with its precise limits

[NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md](NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md),
with [complete reconstruction](NORMALIZED_COMPLEX_FINITE_WIDTH_CHECK.md),
proves that for any finite n and any nonzero imaginary great-circle angle
tau, the actual two-hidden-layer initialized network with
phi(z)=az+c erf(z/sqrt2)+b, c!=0, has

\[
 \mathbb E\|h_n^{(2)}(e_1\cosh\tau+i e_2\sinh\tau)\|_{2,n}^2=\infty.
\]

A rare first-layer coordinate with imaginary square minus real square
larger than n/2 makes the next Gaussian integral diverge. The proof uses
an elementary sector lower bound for erf and the exact variance 1/n of
one mixer entry. It applies even to the real-bounded normalized erf.

This does not contradict the finite population moment or convergence in
probability. It rules out substituting the population complex second moment
for an unconditional finite-network bound. A stopped high-probability
estimate remains possible. Real moments are finite, the initialized
readout is zero, and no output-error or compression lower bound is claimed.

## 6. Remaining target, evidence and repository status

The unresolved mathematical quantity is still the general trained
query/training product phi''(z) R_a J and its higher-order versions,
controlled on a common stopped domain with explicit depth constants.
The new transverse integrated estimate does not cover arbitrary queries.
The unbounded source proof additionally needs explicit joint forward/backward
reciprocal-trace and Gaussian-budget constants; its numerical closure is
not supplied by a real RMS fitting bound. Smoothness and the two moments
alone do not provide strip analyticity or bounded derivative supremums.

The root's complete reconstruction of the independent near-critical and
real-fitting routes is [NORMALIZED_ROUTE_CONTINUATION_CHECK.md](NORMALIZED_ROUTE_CONTINUATION_CHECK.md).
The other checks above reconstruct their frozen candidates separately.
These are internal study results, not promotion reviews. There were no
training experiments, GPU jobs, manuscript edits, Git mutations, or changes
to concurrent repository work. The old full compression claims are not
superseded by a new triple here. In particular the previously forecast
polynomial-depth label, error and size formulas remain conjectural.
