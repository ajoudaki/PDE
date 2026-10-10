# Sample spectra, effective coercivity, and nonlinear trajectory compression

Scope: independent, prompt-only theoretical route for the study
`structured_sample_compression_20261010`, prepared 2026-10-10. Scientific inputs
were the supervisor's assignment and its clarification that non-affine
polynomial activations lie outside the current bounded-strip-derivative
activation class. No book, paper, other study, external scientific source, or
experiment was consulted. Required mathematical skills and shared process
instructions were read. The arguments below are elementary derivations;
they have received an author audit, not an independent review or promotion.

The question is whether labels with few spherical harmonic or Fourier modes
support an autonomous approximation to the dense nonlinear gradient-flow
trajectory with retained state and coefficient storage independent of the
sample count $m$. Sample compression and parameter/width compression are
distinct: the exact positive result below retains the original parameters.
All accuracy statements specify their norm and horizon. Merely reproducing
the target labels is not the requested trajectory guarantee.

## 1. Normalization and the exact residual equation

Let $x_a\in S^{d-1}\subset\mathbb R^d$, $y_a=y_*(x_a)$, and

\[
f_\theta(x_a)\in\mathbb R,\qquad
r_a=f_\theta(x_a)-y_a,\qquad
\mathcal L(\theta)=\frac1m\sum_{a=1}^m r_a^2.
\]

The parameter vector is $\theta\in\mathbb R^p$. For this note, its mobility
$M\in\mathbb R^{p\times p}$ is fixed, symmetric, and positive definite.
With normalized coordinates $u=M^{-1/2}\theta$, write
$f_u(x)=f_{M^{1/2}u}(x)$. Then

\[
\dot\theta=-M\nabla_\theta\mathcal L,
\qquad
\dot u=-\nabla_u\mathcal L
       =-\frac2m\sum_b r_b\nabla_u f_u(x_b).
\]

Define the Jacobian $J_t\in\mathbb R^{m\times p}$ by
$(J_t)_{ai}=\partial_{u_i}f_{u(t)}(x_a)$, the tangent Gram matrix
$K_t=J_tJ_t^\top$, and its normalized operator $A_t=K_t/m$. The chain rule
gives the exact identity

\[
\dot r=-\frac2mK_t r=-2A_t r.
\tag{1}
\]

For vectors on the samples use

\[
\langle v,w\rangle_m=\frac1m v^\top w,
\qquad \|v\|_m^2=\langle v,v\rangle_m.
\]

Each $A_t$ is self-adjoint and positive semidefinite for this inner product.
Consequently

\[
\frac{d}{dt}\|r\|_m^2=-4\langle r,A_t r\rangle_m\le0.
\tag{2}
\]

Equation (1) is an observable identity, not a closed compressed system:
evaluating $A_t$ ordinarily requires the evolving dense state. No result
below treats the unknown function $t\mapsto A_t$ as free input to a
compression algorithm. The fixed-mobility assumption matters: a
state-dependent mobility needs its own coordinate and comparison analysis.

## 2. What label bandlimitation does not imply

Let $V\subset\mathbb R^m$ be the restrictions to the samples of harmonics
through a chosen degree, and let $P$ be the orthogonal projector onto $V$
in $\langle\cdot,\cdot\rangle_m$. Linear dependencies among sampled basis
functions are allowed; $V$ means their actual span. Set $Q=I-P$.
Bandlimited labels imply $y\in V$. Even $r(0)\in V$ additionally needs
$f_{u(0)}|_{\{x_a\}}\in V$. Assuming this initialization condition,

\[
Q\dot r(0)=-2Q A_0P r(0).
\tag{3}
\]

Thus a necessary condition for invariance along this initial direction is
$Q A_0P r(0)=0$. A useful sufficient condition for every residual in $V$
is $Q A_tP=0$ at every time. Under continuity of $A_t$, the equation for
$Qr$ is then homogeneous with zero initial value, so $r(t)\in V$.
Self-adjointness also gives $P A_tQ=0$. Neither of these kernel conditions
is implied by label bandlimitation.

Here is a quantitative fixed-kernel illustration. On $S^1$, choose
$m>2N$ equally spaced angles $\varphi_a=2\pi a/m$, and define

\[
\mathbf 1_a=1,\qquad h_a=\sqrt2\cos(N\varphi_a).
\]

The finite geometric-sum identity gives
$\langle\mathbf1,h\rangle_m=0$ and
$\|\mathbf1\|_m=\|h\|_m=1$. Train the linear readout

\[
f_u(\varphi)=u_1(1+\sqrt2\cos N\varphi)
                  +u_2\sqrt2\cos N\varphi
\]

from $u(0)=0$ against $y_*=1$, with unit mobility. On the basis
$(\mathbf1,h)$, $A=K/m$ has the constant matrix

\[
A|_{\operatorname{span}\{\mathbf1,h\}}
=\begin{pmatrix}1&1\\1&2\end{pmatrix},
\qquad
\lambda_\pm=\frac{3\pm\sqrt5}{2}>0.
\]

Since $r(t)=-e^{-2At}\mathbf1$, diagonalizing this $2\times2$ matrix gives
the coefficient of $h$ in both $r(t)$ and $f(t)$:

\[
\langle h,r(t)\rangle_m
=\frac{e^{-2\lambda_-t}-e^{-2\lambda_+t}}{\sqrt5}.
\tag{4}
\]

At $t=1/2$ this is the positive numerical constant
$(e^{-\lambda_-}-e^{-\lambda_+})/\sqrt5$, approximately $0.273$,
independent of $N$ and $m$. For every fixed Fourier cutoff below $N$,
$h$ is orthogonal to all retained modes, again by the finite geometric-sum
identity. Any prediction confined to those modes has empirical error at
least this constant at that time. The labels have degree zero.

This disproves the assertion that label degree alone bounds the degree
needed by a fixed low-harmonic trajectory representation over unrestricted
kernels. It does **not** disprove sample compression: this very example
has a two-dimensional exact model, and the high-frequency basis has an
explicit formula. It is also a fixed-feature example, not a theorem about
the study's dense architecture.

The invariance issue also occurs in nonlinear training with a
smooth bounded activation. For example, take the trainable one-neuron model

\[
f_{a,w}(x)=a\tanh(w^\top x),\qquad
(a(0),w(0))=(0,e_1),\qquad y_*=1,
\]

with unit positive mobility for all parameters. Choose sample points on
$S^1$ with distinct first coordinates in $0<x_{a,1}<1$, and write
$\overline\phi=m^{-1}\sum_a\tanh(x_{a,1})>0$. At initialization,

\[
\dot a(0)=2\overline\phi,
\qquad \dot w(0)=0,
\qquad
\partial_t f(0,x)=2\overline\phi\tanh(x_1).
\tag{5}
\]

Hence even the sampled trajectory immediately leaves the constant subspace.
The feature parameter subsequently moves: for sufficiently small positive
time, $a(t)>0$, all residuals remain negative, and

\[
e_1^\top\dot w(t)
=-\frac{2a(t)}m\sum_b r_b(t)
       \operatorname{sech}^2(w(t)^\top x_b)x_{b,1}>0.
\]

On the full circle, $\tanh(\cos\varphi)$ has no finite Fourier cutoff.
Indeed, a finite even trigonometric polynomial is a polynomial
$p(\cos\varphi)$, by the recursion for $\cos(k\varphi)$. If it equaled
$\tanh(\cos\varphi)$, then on $[-1,1]$ its polynomial would satisfy
$p'=1-p^2$. For a nonconstant polynomial, the degrees on the two sides
cannot agree; the only constant solutions are $p=\pm1$, neither of which
equals $\tanh s$. This contradiction proves the claim.

Example (5) shows loss of exact finite-band invariance within a nonlinear
smooth activation model. Its high modes can still have small tails, and it
is not a lower bound on the number of modes needed at fixed accuracy. Its
sample geometry and architecture are explicit special choices, not claims
about every training set or the particular dense model in the book.

## 3. Effective coercivity is different from a full Gram gap

Suppose $V$ is invariant, $r(0)\in V$, and

\[
\langle v,A_t v\rangle_m\ge\lambda\|v\|_m^2
\quad(v\in V,\ t\ge0),\qquad \lambda>0.
\tag{6}
\]

By (2), differentiating $e^{4\lambda t}\|r(t)\|_m^2$ gives a nonpositive
derivative, whence

\[
\|r(t)\|_m\le e^{-2\lambda t}\|r(0)\|_m.
\tag{7}
\]

This only needs the gap of $K_t/m$ on $V$. The minimum eigenvalue of the
full $m\times m$ matrix can vanish identically. For instance, the model
$f_u(x)=u$ has $K=\mathbf1\mathbf1^\top$, normalized eigenvalue (1) on
constants, and $m-1$ zero eigenvalues. Its constant residual decays at
rate (2), independently of $m$. The two-mode example above is another
case where the full minimum eigenvalue is zero and the relevant gap is
strictly positive.

A still weaker assumption,
$\langle r(t),A_t r(t)\rangle_m\ge\lambda\|r(t)\|_m^2$, proves (7) for
that trajectory. It does not establish damping for differences between
two trajectories: those differences need not point along $r(t)$.
Confusing these assumptions would turn a fitting estimate into an
unjustified stability theorem.

Low-complexity labels supply no positive lower bound in (6). For the
one-parameter model $f_u(x)=\sqrt\delta\,u$, labels (1), initialization
zero, and unit mobility, the only relevant normalized eigenvalue is
$\delta>0$, and

\[
r_\delta(t)=-e^{-2\delta t}\mathbf1.
\]

Comparing the kernels with eigenvalues $\delta$ and $2\delta$, their
operator difference is $\delta\to0$, whereas

\[
\sup_{t\ge0}\|r_\delta(t)-r_{2\delta}(t)\|_m=\frac14.
\tag{8}
\]

To verify (8), put $z=e^{-2\delta t}\in[0,1]$; the difference is
$z-z^2$, whose maximum is $1/4$. Thus absolute kernel consistency alone
does not give an all-time error estimate uniform over arbitrarily small
relevant decay rates, even with constant labels and positive mobility.
Again, both systems are exactly scalar-compressible. This is a stability
obstruction for one perturbation argument, not an existence obstruction
for compression.

## 4. A precise conditional all-time comparison

Here the assumptions are deliberately exposed. Let $V$ be fixed and
finite-dimensional. Let $A_t,\widehat A_t$ be continuous self-adjoint
operators preserving $V$, and suppose their restrictions obey

\[
A_t|_V\succeq\lambda I,
\qquad \widehat A_t|_V\succeq\widehat\lambda I,
\qquad
\|(A_t-\widehat A_t)|_V\|\le\eta,
\]

where $\lambda\ge0$, $\widehat\lambda>0$, and the operator norm uses
$\|\cdot\|_m$. Let $r,\widehat r\in V$ solve the corresponding versions
of (1), with $\|r(0)\|_m\le R$ and
$\|\widehat r(0)-r(0)\|_m\le\delta_0$. Then

\[
\|\widehat r(t)-r(t)\|_m
\le \delta_0e^{-2\widehat\lambda t}
 +2\eta R\int_0^t
 e^{-2\widehat\lambda(t-s)}e^{-2\lambda s}\,ds
\le \delta_0+\frac{\eta R}{\widehat\lambda}.
\tag{9}
\]

For the proof, $e=\widehat r-r$ obeys

\[
\dot e=-2\widehat A_t e+2(A_t-\widehat A_t)r.
\]

Every homogeneous solution between times $s,t$ has norm at most
$e^{-2\widehat\lambda(t-s)}$ times its starting norm, by the same energy
calculation as (7). Variation of constants, the operator-error bound, and
$\|r(s)\|_m\le Re^{-2\lambda s}$ give the first inequality in (9).
Integrating the first exponential and bounding the second by (1) gives
the last inequality. No commutation of operators at different times is
assumed or used.

An analogous estimate requires no positive gap if the actual source is
integrable. For positive semidefinite $\widehat A_t$ on the relevant
space, the same proof gives

\[
\sup_{t\ge0}\|e(t)\|_m
\le\delta_0+
2\int_0^\infty\|(A_s-\widehat A_s)r(s)\|_m\,ds.
\tag{10}
\]

This weighted, time-integrated error condition can be much weaker than a
uniform gap. It must be derived from admissible information, not simply
postulated after observing the exact trajectory.

There is also an elementary fixed-kernel illustration of relative rather
than absolute accuracy. If two kernels have the same orthonormal
eigenvectors and eigenvalues satisfying
$(1-\eta)\lambda_j\le\widehat\lambda_j\le(1+\eta)\lambda_j$, with
$0\le\eta<1$, then for every $t\ge0$

\[
|e^{-2\lambda_jt}-e^{-2\widehat\lambda_jt}|
\le 2\eta\lambda_jt\,e^{-2(1-\eta)\lambda_jt}
\le\frac{\eta}{e(1-\eta)}.
\tag{11}
\]

The first step is the mean-value formula in the eigenvalue; the second is
the maximum of $z e^{-z}$. Zero eigenvalues match exactly. For the same
initial residual in both systems, summing squared modal errors proves
the same multiplier bound on the initial residual norm,
without a smallest-positive-eigenvalue bound. Thus a uniform spectral gap
is a useful sufficient condition, not a necessary condition for every
all-time approximation theorem.

Equations (9)--(11) are conditional propagation estimates. They do not
construct an autonomous approximation to a learned kernel, prove small
kernel discrepancy between two nonlinear parameter flows, or show that
the necessary basis can be retained independently of $m$. In particular,
storing $D$ arbitrary sampled eigenvectors still stores $mD$ numbers.

## 5. A positive exact result for a finite input dictionary

Suppose the original, possibly nonlinear architecture has a known finite
representation on its entire parameter domain:

\[
f_u(x)=c(u)^\top\psi(x),
\quad c:\mathbb R^p\to\mathbb R^D,
\quad \psi:S^{d-1}\to\mathbb R^D.
\tag{12}
\]

Here $\psi$ is fixed, explicitly evaluable without the dataset, and
$D$ is independent of $m$. Assume $c$ is twice continuously
differentiable so the finite-dimensional vector field below is locally
Lipschitz. The dense parameterization and all its trainable features are
retained through $u\mapsto c(u)$; no linearity of this map is assumed.
Compute, by a single pass over the samples,

\[
G=\frac1m\sum_a\psi(x_a)\psi(x_a)^\top,
\qquad b=\frac1m\sum_a y_a\psi(x_a),
\qquad s=\frac1m\sum_a y_a^2.
\tag{13}
\]

The loss and its exact normalized gradient flow are

\[
\mathcal L(u)=c(u)^\top Gc(u)-2b^\top c(u)+s,
\qquad
\dot u=-2Dc(u)^\top\bigl(Gc(u)-b\bigr).
\tag{14}
\]

Indeed, substitute (12) into the normalized sum of squared residuals,
expand each square, and use (13). Differentiate the resulting finite
quadratic expression through $c$ to obtain (14). Hence the dense and
compressed implementations have exactly the same vector field and initial
condition. On a common compact time interval their vector field has a
finite Lipschitz constant $B$ on a bounded neighborhood of the two
trajectories. Their difference therefore has norm at most $B$ times the
integral of its norm. If that integral is $E(t)$, then
$E(0)=0$ and $E'(t)\le B E(t)$; differentiating $e^{-Bt}E(t)$ proves the
difference is zero. This gives local uniqueness and equality throughout
their common existence interval.

Under the stated global $C^2$ assumption on $c$, existence is in fact
global. The exact nonnegative squared loss satisfies

\[
\frac{d}{dt}\mathcal L(u(t))=-\|\dot u(t)\|_2^2,
\qquad
\int_0^t\|\dot u(s)\|_2^2\,ds\le\mathcal L(u(0)).
\]

Thus Cauchy--Schwarz gives, for $0\le s<t$,

\[
\|u(t)-u(s)\|_2
\le\sqrt{(t-s)\mathcal L(u(0))}.
\]

If a maximal existence time were finite, this bound would give a finite
limit of the parameters at that time. The locally Lipschitz vector field
is defined at that limit and has a local solution there, extending the
trajectory and contradicting maximality. Hence (14) reproduces the
dense parameter trajectory for every finite $t\ge0$. No spectral gap is
needed for this exact all-time identity.

With the dense architecture held fixed, the evolving state has $p$
coordinates. Fixed dataset-dependent storage
has $D(D+1)/2+D$ numbers, plus $s$ if reporting the absolute loss.
Initialization is the original $u(0)$; coefficients come only from the
dataset and known architecture, not the future trajectory. The resulting
ODE is autonomous and restartable. Its coefficients may depend on the
instance and be computed using $O(mD^2)$ arithmetic in a direct streaming
implementation, while retained storage is independent of $m$. Predicting
at a supplied query $x$ uses (12). Re-emitting all $m$ training predictions
requires the corresponding query points and $O(m)$ output, which is not
being counted as retained model state. This is an exact-arithmetic
statement, not a finite-precision robustness theorem.

No label-complexity condition is needed for (13)--(14). If labels share
the dictionary, $y_*(x)=c_*^\top\psi(x)$, then $b=Gc_*$, so the label
dependence has that particularly simple form. Low label complexity alone
does not give representation (12).

A nonlinear illustration is a depth-$L$ network with polynomial
activations of degree at most $s_0\ge1$, affine preactivations, and a
linear readout. Induction over hidden layers shows that its output, as a
function of input coordinates, is a polynomial of degree at most
$s_0^L$: affine combinations preserve a degree bound, and composition
with the activation multiplies it by at most $s_0$. Taking $\psi$ to be
all input monomials of degree at most $s_0^L$ gives
$D=\binom{d+s_0^L}{s_0^L}$. Its coefficient map $c(u)$ is polynomial and
generally nonlinear in the trainable weights. Thus (14) exactly preserves
feature-learning parameter dynamics, not merely a frozen tangent kernel.

**Scope qualification:** non-affine polynomial activations have unbounded
derivatives on the real line and are outside the current
bounded-strip-derivative activation class. Affine/identity activations
provide an in-class special case, including multilayer factorizations
whose parameter dynamics remain nonlinear. The non-affine polynomial
example is therefore an illustration of the finite-dictionary sufficient
condition, not a result for the intended tanh/GELU-type dense network.
The dictionary can also grow rapidly with dimension and depth. The
proposition compresses samples, not dense width or parameter count.

## 6. Honest sufficient hypotheses for a spectral route

The following would support a fixed-accuracy route for the intended
non-polynomial nonlinear model, but have not been established here.

1. **A uniform reachable-state approximation property.** A known, explicitly
   evaluable input basis of size $D(\varepsilon,T,R)$, independent of
   $m$, approximates not only $y_*$ but the evolving prediction and
   the parameter derivatives that drive gradient flow. Here $R$ denotes
   declared regularity and parameter bounds. A spectral tail bound must
   apply to the collective tail in the comparison norm, uniformly over
   the stated reachable states. Smooth labels alone do not provide it.
2. **Control of the empirical geometry.** The sampled basis and quadrature
   estimates obey bounds independent of $m$ in the actual empirical
   norm. Symmetry of a population measure cannot be silently transferred
   to an arbitrary finite dataset. Sampling may also alias high modes
   into low modes. If the argument uses a well-conditioned empirical
   Gram matrix, that is an additional geometric assumption, not a
   consequence of label bandlimitation.
3. **An evaluable autonomous update and a source-error bound.** Retained
   basis coefficients and finite static statistics must determine the
   update without $m$ stored samples or future kernel values. A finite
   exact representation such as (12) supplies this directly. An
   approximate representation needs a derived vector-field or kernel
   defect estimate; projecting the residual identity does not supply it.
4. **Propagation estimates at the claimed horizon.** For a fixed finite
   horizon, a uniform Lipschitz bound and a small vector-field defect can
   suffice. For all time, one needs an additional argument such as
   restricted coercivity plus a controlled defect as in (9), an
   integrable source as in (10), relative spectral control in an
   applicable fixed-kernel setting, or an exact reduction. Residual
   decay for the dense system alone is not a comparison theorem for
   two feature-learning trajectories.

For example, if a spatially smooth activation is approximated by a
polynomial on a bounded preactivation interval, approximation of the
forward output alone does not prove (14) approximates the original flow.
Parameter derivatives require derivative approximation and propagation
through layers. Uniform-in-time approximation additionally needs the
preactivation and derivative bounds to persist in time and a suitable
stability estimate. Merely replacing the activation by a polynomial
would change the model without establishing the required trajectory
comparison.

The strongest conclusion of this route is therefore conditional and
specific. Low-complexity labels can make a sample reduction useful when
the learned tangent dynamics preserve or approximately preserve a
controlled finite family of input functions. Label complexity alone
does not establish that property or an all-time perturbation estimate.
Conversely, zero minimum full-Gram eigenvalue and absence of a uniform
decay gap do not rule out compression. The outstanding bridge for the
intended dense feature-learning model is a reachable-state approximation
and autonomous-update theorem with constants independent of $m$,
followed by stability in the requested observable and time horizon.
