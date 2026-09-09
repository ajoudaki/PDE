# The initialization-jet Borel conjecture after local population GF existence

This is a source reconciliation and conditional implication, dated 2026-09-05.
It does not claim to prove neural Borel summability.

The exact top-level source is
[AUTONOMOUS_DEEP_FEATURE_LEARNING_THEOREM_AND_PROGRAM_2026-08-21.md, section 10](/home/amir/Codes/PDE/AUTONOMOUS_DEEP_FEATURE_LEARNING_THEOREM_AND_PROGRAM_2026-08-21.md:830),
added on 23 August. The named conjecture is at line 1018 and its compact-time
version is explicitly described at line 1034. The entire 1,693-line document
was read, and independent context readers read the entire August 19 synthesis
and July 31 monograph. The later Gevrey/Borel audit and relevant maintained
Stieltjes state were also checked. Detailed reading records are in the three
BOREL_*_CONTEXT/AUDIT notes beside this file.

The document's positive conjecture concerns an initialization-compiled
hierarchy for the canonical ONE-SAMPLE predictor and loss. Its full version
asks for a finite scalar ODE with arbitrarily small uniform all-time loss
error, conditional on a nondegenerate output-coordinate kernel. Its proposed
route is uniform approximation of that actual kernel by Borel continuation
and quadrature from finite initialization jets. The local version is the
relevant additional conjecture after our fixed positive-time GF theorem.

The source's broad-depth existence frontier is historical: our new proof
supplies local existence and joint width/GD convergence in its stated class.
The source's Borel reconstruction claim remains conjectural. The August 19
Stieltjes program and the later audit of automatic Gevrey completion neither
prove nor refute this broader signed Borel reconstruction conjecture.

## 1. The exact one-sample object and initialization coefficients

Use our physical time t=k eta_n and include the fixed layer multipliers in
the physical kernel K. Then

\[
\dot f(t)=2(y-f(t))K(t).
\]

The source has a separate fixed learning multiplier eta and writes
tau=2 eta t_source. In our convention tau=2t. No vanishing eta_n remains in
the population equation.

Suppose e0=y-f0>0 and K(0)>0; reversing output direction handles e0<0.
Continuity supplies a fixed interval [0,T1] with K>0. The residual obeys
e(t)=e0 exp(-2 integral_0^t K(s)ds)>0, so f is strictly increasing there.
Define the continuous output-coordinate kernel on this canonical orbit by

\[
\kappa(f(t))=K(t).
\]

This defines a function along one initialized trajectory. It makes no
statement that two arbitrary population states with the same output have
the same kernel. A zero initial readout causes no difficulty: in the
nondegenerate case K(0)>0 because the readout block already contributes,
although hidden coordinates have zero initial velocity.

Write s=f-f0 for the scalar output increment and suppose the required actual
initialization derivatives exist. Set

\[
d_p=\left.\frac{d^p f}{d\tau^p}\right|_{\tau=0}
=2^{-p} f^{(p)}(0),\qquad
\kappa(f_0+s)\sim\sum_{p\ge0}c_p s^p.
\]

Formal division of f_tau by y-f, followed by formal inversion of f-f0,
determines c_p from e0,d1,...,d_(p+1). For example

\[
c_0=\frac{d_1}{e_0},\qquad
c_1=\frac{e_0d_2+d_1^2}{e_0^2d_1},
\]
\[
c_2=\frac{d_3}{2e_0d_1^2}-\frac{d_2^2}{2e_0d_1^3}
      +\frac{d_2}{e_0^2d_1}+\frac{d_1}{e_0^3}.
\]

The source's mean-field peeling compiler is supposed to obtain each fixed
d_p from Gaussian initialization, the architecture, and the update rule.
This entails both fixed-order compilation and compatibility with the
derivatives of the actual population flow. Uniform convergence of population
paths alone does not justify differentiating the width limit.

## 2. What the Borel reconstruction hypothesis contains

For some finite exponent sigma>0, the formal transform is

\[
\mathcal B_\sigma\kappa(\xi)
=\sum_{p\ge0}\frac{c_p}{\Gamma(1+\sigma p)}\xi^p.
\]

A Gevrey bound |c_p|<=C A^p Gamma(1+sigma p) ensures convergence near xi=0.
It does not identify the appropriate sigma for this network, prove continuation,
or establish a positive-time reconstruction. In the convention of the
companion summability audit, the summability order is 1/sigma. Derivative
growth and coefficient growth differ by the factorial p!.

The desired actual-kernel identity is

\[
\kappa(f_0+s)=\int_0^\infty
 e^{-u}\mathcal B_\sigma\kappa(su^\sigma)\,du.                    (B)
\]

For any positive s the integral evaluates the transform arbitrarily far
along the positive ray. The transform must have an appropriate analytic
continuation and growth estimate there. A sufficient envelope is
|B(xi)|<=C exp(b xi^(1/sigma)); it gives uniform integrability for
0<=s<=S if b S^(1/sigma)<1.

Next use finitely many coefficients to construct a specified rational
continuation B_N and a finite quadrature rule. The emitted kernel is

\[
\kappa_{N,M}(f_0+s)=\sum_{j=1}^M w_j B_N(su_j^\sigma).
\]

The model-dependent coefficients come only from the initialization jet and
the declared summation rule. The source forbids positive-time samples, fitted
coefficients, and an unknown trajectory hidden in a forcing term. Generic
diagonal Pade convergence and absence of poles cannot be presumed.

For a fixed output interval I reached within the existence interval, the
substantive sufficient local hypothesis is

\[
\sup_{v\in I}|\kappa_{N,M}(v)-\kappa(v)|\longrightarrow0           (U)
\]

along a specified sequence of finite N,M. The target in (U) is the ACTUAL
population kernel. Sufficient analytic hypotheses for (U) include local
uniform convergence B_N->B along the ray, a common integrable growth
envelope, and vanishing uniform quadrature error. To see uniformity, split
the Laplace integral at U: on [0,U] only the compact xi-interval
[0,S U^sigma] is used; beyond U the common exponential envelope supplies a
uniformly small tail. This is a sufficient mechanism, not an assertion that
every rational scheme has those properties.

The convergent objects are the resummed finite approximants. Merely
integrating a truncated Borel power series gives

\[
\int_0^\infty e^{-u}\sum_{p=0}^N
 \frac{c_p(su^\sigma)^p}{\Gamma(1+\sigma p)}du
=\sum_{p=0}^N c_p s^p,
\]

because integral e^-u u^(sigma p)du=Gamma(1+sigma p). Thus this operation
alone returns the original Taylor truncations, which are permitted to diverge.

## 3. Why GF existence does not automatically identify the sum

The [July monograph, section 5.7.6](/home/amir/Codes/PDE/FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md:3362)
states the surviving obstruction: complete smooth jets permit nonzero flat
corrections. For an elementary example, let g(x)=exp(-1/x^2) for x>0 and
g(x)=0 for x<=0. The smooth globally Lipschitz ODE

\[
\dot x=1+g(x),\qquad x(0)=0
\]

has a unique solution with formal Taylor series x(t)~t. That series is
convergent and Borel summable, but the actual solution is strictly greater
than t for every t>0. The proposed sum t fails the equation by g(t). This
is not a neural counterexample; it establishes the logical need for an
identification premise.

There are two valid options: assert/prove that the actual observable is the
Borel sum of its jet, or reconstruct the full population state in the strong
solution class and prove that the sum satisfies the same integral GF
equations and initialization. Our uniqueness theorem then identifies it.
Matching only a predictor or kernel jet does not permit that invocation.
Quasianalytic sectorial hypotheses are one other route to identification;
the relevant class distinctions were checked against
[Lastra--Malek--Sanz](https://arxiv.org/pdf/1402.1669).

The new GF theorem uses only C1,1 activation/loss regularity. It does not
establish arbitrary-order jets or their growth. Arctan is a natural smooth
test case, but even C-infinity regularity alone is insufficient for
reconstructibility. No Gevrey exponent or summability theorem follows just
from the new mesh-uniform subGaussian response bound.

The older Borel audit sought to derive the WIDTH LIMIT through Borel summation,
so it required common finite-width continuation/growth and finite-width
identification. That obligation can now be bypassed: reconstruct the already
identified population observable, then use the existing width/GD theorem.

## 4. Conditional local scalar error, with the time interval made explicit

Take 0<T<T1<=T_* with K>0 on [0,T1], and set
I=[f0,f(T1)], a=min_I kappa>0, M0=max_I kappa. Suppose a continuous emitted
kernel kappa_N has uniform error delta<a on I. It defines

\[
\dot f_N=2(y-f_N)\kappa_N(f_N),\qquad f_N(0)=f_0.
\]

Put rho=delta/a. Its velocity is between (1-rho) and (1+rho) times the exact
scalar velocity at each output. Separating variables therefore gives

\[
f((1-\rho)t)\le f_N(t)\le f((1+\rho)t),\qquad 0\le t\le T,
\]

provided (1+rho)T<=T1. The positive-velocity separated integral gives
existence and uniqueness on this range even when kappa is only continuous.
As |dot f|<=2e0 M0 and |dot L|<=4e0^2 M0,

\[
\sup_{t\le T}|f_N(t)-f(t)|\le\frac{2e_0M_0T}{a}\,\delta,
\qquad
\sup_{t\le T}|\mathcal L_N(t)-\mathcal L(t)|
\le\frac{4e_0^2M_0T}{a}\,\delta.                                  (S)
\]

The time margin avoids evaluating the exact trajectory outside its known
range. This is local positivity obtained from K(0)>0 and continuity, not
the global output-to-target lower bound in the source's all-time conjecture.

## 5. What would be required for our multiple-input case

For a fixed dataset the true equation is

\[
\dot f_a=-2\sum_b\omega_bK_{ab}(t)(f_b-y_b).
\]

The scalar one-sample output coordinate generally has no analogue covering
all inputs: an individual prediction can turn or remain fixed while the
other examples and hidden state evolve. Section 10 does not provide a
multi-input Borel construction.

A precise extension would use physical-time initialization jets of the
matrix K(t), construct an initialization-only K_N(t), and require uniform
identified reconstruction on a fixed [0,T]. Let Omega=diag(omega_a) and

\[
\delta_N=\sup_{t\le T}
\|\Omega^{1/2}(K_N(t)-K(t))\Omega^{1/2}\|_{\rm op}\to0.
\]

Integrate the known-coefficient vector equation with K_N and the same f0.
Define v=Omega^(1/2)(f-y), A=Omega^(1/2)K Omega^(1/2), and corresponding
v_N,A_N. Then dot v=-2Av, A is positive semidefinite, and

\[
\|v_N(t)\|_2\le e^{2\delta_Nt}\|v(0)\|_2.
\]

For the error, dot(v_N-v)=-2A(v_N-v)-2(A_N-A)v_N. The propagator of
-2A is contractive by the Euclidean energy identity, even though A at
different times need not commute. Duhamel therefore gives

\[
\sup_{t\le T}\|\Omega^{1/2}(f_N(t)-f(t))\|_2
\le(e^{2\delta_NT}-1)\sqrt{\mathcal L(0)},
\]
\[
\sup_{t\le T}|\mathcal L_N(t)-\mathcal L(t)|
\le(e^{4\delta_NT}-1)\mathcal L(0).                              (V)
\]

No positive minimum kernel eigenvalue is required for (V). If the emitted
kernel is also positive semidefinite, the respective bounds improve to
2delta_N T sqrt(L(0)) and 4delta_N T L(0). Uniform entrywise kernel error
epsilon bounds delta_N by epsilon because sum omega_a=1.

This is a conditional deduction for a proposed matrix extension, not a
claim that the source's scalar conjecture has already proved one. The known
coefficient function K_N(t) can be evaluated by a finite ODE with an explicit
clock s'=1; this is a different construction from the source's output-only
scalar ODE. It describes the fixed initialized experiment, not arbitrary
off-orbit changes of labels, data, or hidden state.

## 6. Consequence for finite networks, and exact remaining scope

Choose a finite approximant with population error <=epsilon on [0,T]. Our
joint width/GD theorem then gives, in scalar or weighted prediction norm,

\[
\sup_{t\le T}\|f_n^{\rm GD}(t)-f_N(t)\|
\le\sup_{t\le T}\|f_n^{\rm GD}(t)-f(t)\|+\epsilon
=o_{\mathbb P}(1)+\epsilon.
\]

Thus a finite amount of initialization-compiled information would suffice
for any prescribed output/loss accuracy throughout a nonvanishing time
interval, independently of width and the vanishing learning step. The order
is selected for accuracy before the width limit; arbitrary joint growth of
order with width needs another estimate. Existence of a sufficient order
also does not supply an efficient or certified stopping rule without a
computable approximation modulus.

To cover every t<T_*, the Borel hypothesis must hold on every compact
[0,T] with T<T_* (or on all of [0,T_*]). A single smaller fixed interval
[0,T_B] gives a conclusion only there. If T_B shrinks to zero with width,
step, or approximation order, it does not cover any fixed positive t.

The output-kernel conjecture does not reconstruct hidden Grams, neuron path
laws, or operators. Each requires its own identified reconstruction or a
strong full-state theorem. It also does not prove a fixed finite-dimensional
state valid for every possible population restart, an all-time result, or
uniformity over the whole C1,1 activation class. Those are separate claims.
