# Existence of the Gaussian block P1 population flow

2026-09-30. Supporting author proof for the small-response construction.
This establishes the population-flow dependency for the prescribed Gaussian
initialization. It does not assert the same theorem for every initial law
having only eight moments. No experiments or promotion.

Use the P1 block equations in sections 1–2 of
`AGGREGATE_SCALAR_CONSTRUCTION.md`. Block size k and sample count m are fixed,
inputs have norm at most one, labels are finite, G has iid N(0,1/k) entries,
and initial w has the stipulated Gaussian law. Initial c=A=0, B_a=tanh(wu_a),
and L=1. All expectations below are over that single prescribed seed law;
no density approximation is introduced.

## Statement

There is a unique self-consistent population solution, with continuously
varying shared contractions, on every finite physical-time interval. Its
characteristics are unique for almost every seed. The local fields solve
the stated ODEs and all defining population expectations hold. On [0,T],
c,A,B are bounded uniformly over the seed, L stays at least one, and

\[
\|w(t)-w(0)\|_F\le C_T(1+\|G\|_F).                       \tag{1}
\]

The constants depend on T,m,k and the labels, not on a number of sampled
blocks. Consequently the Gaussian expectations used by the small-response
source estimates are defined along this unique flow. This statement does
not prove its fitting at large label amplitude.

## Uniform bounds on any self-consistent solution

Put Y=max_a |y_a|, C(t)=sup_seed,i |c_i(t)| and R(t)=C(t)+Y. Bounded tanh
gives |f_a|≤C and therefore |r_a|,rho≤R. The readout equation implies
C(t)≤2∫_0^t(C(s)+Y)ds, hence

\[
C(t)\le Y(e^{2t}-1),\qquad R(t)\le Ye^{2t}.             \tag{2}
\]

One can verify (2) directly by multiplying the scalar comparison equation
by e^{-2t}; no finite-dimensional population approximation is needed.
Then L≤1+∫R, every B entry is bounded by 1+∫R, and every A entry by
∫RC. Let S_a=E[k^{-1}B^T h_{1,a}] and
V_a=E[k^{-1}A^T delta_{2,a}]. These contractions are bounded by the
corresponding products of the preceding uniform bounds. In

\[
\delta_{1,a}=\phi'(wu_a)\odot
\left[G^T\delta_{2,a}-\frac2{mL}B V_a\right],
\]

the only unbounded seed factor is G, appearing linearly. Integration of
the first-weight equation now proves (1). These bounds are finite for
each prescribed T. The case Y=0 is the stationary solution.

## Local construction from finite shared fields

Start at any time t0 with a consistent state whose c,A,B are uniformly
bounded and L0≥1. Prescribe continuous trial curves of the finite fields

\[
S=(S_1,\ldots,S_m),\qquad v=(r,V_1,\ldots,V_m)
\]

on an interval of length delta. Set rho=||r||_RMS and
L=L0+∫rho. For each seed solve the local ODE using those prescribed S,V,r
in place of the shared contractions. Its second activation is

\[
h_{2,a}=\tanh\left(Gh_{1,a}-\frac2{mL}A S_a\right).
\]

The characteristic ODE is locally Lipschitz. Bounded activations first
bound c,A,B independently of the seed on the short interval, and then
bound w's displacement by C delta(1+||G||). Thus each characteristic
exists throughout that interval. Form new shared fields by taking the
specified expectations of the resulting states and subtracting labels
for the residual. This defines a map Phi on trial field curves.

For sufficiently short delta this map preserves a closed bounded set of
curves with the given consistent initial values. In detail, choose a
trial residual bound strictly larger than C(t0)+Y; c increases by at most
twice that bound times delta. Choose a trial S bound strictly larger than
the current uniform B bound, and a trial V bound strictly larger than
the product of current uniform A and c bounds. Their output bounds follow
from |h1|,|h2|,|phi'|≤1. By decreasing delta, the increases in those local
bounds remain below the chosen strict margins. Hence Phi maps this set
into itself.

The proof of contraction needs care: r and V have a direct dependence on
the trial S through h2. They are not all delayed by integration. The
following weighted norm handles this triangular direct dependence.

Let z=(w,c,A,B) and compare two trial field curves starting from the same
characteristic initial state. On the preceding bounded set, differentiating
the local vector field and using the globally bounded first two tanh
derivatives gives

\[
\|\Delta z(t)\|
\le C\delta(1+\|G\|_F^2)
 e^{C\delta(1+\|G\|_F^2)}
       (\|\Delta S\|_\infty+\|\Delta v\|_\infty).     \tag{3}
\]

To verify the dependence on G, differentiating the backward first-layer
velocity can pass through G^T and then through the forward G, giving at
most two factors of G. Other derivatives have at most those two factors;
c,A,B,1/L are bounded. Trial-field differences have a polynomial factor
no larger than C(1+||G||²). Also |Delta L|≤delta||Delta r||_infinity.
Integrating the resulting linear difference inequality gives (3).

For Gaussian blocks,

\[
\mathbb E e^{\eta\|G\|_F^2}
=(1-2\eta/k)^{-k^2/2}<\infty\quad(0\le\eta<k/2).       \tag{4}
\]

This follows by multiplying the elementary one-dimensional Gaussian
integrals for the k² entries. Polynomial factors can be absorbed by
slightly increasing eta. Choose a fixed upper bound delta0 sufficiently
small that the exponent in (3), with that enlargement, is integrable.
Its expectation is then bounded uniformly for delta≤delta0.

The output S is E[B^T h1/k]; it depends on local states only, with no
instantaneous trial S term. The outputs r,V additionally depend directly
on trial S through A S/L. Thus (3) and (4) give constants independent of
delta≤delta0 such that

\[
\begin{aligned}
\|\Delta\Phi_S\|_\infty
 &\le C_1\delta(\|\Delta S\|_\infty+\|\Delta v\|_\infty),\\
\|\Delta\Phi_v\|_\infty
 &\le C_2\|\Delta S\|_\infty
        +C_1\delta(\|\Delta S\|_\infty+\|\Delta v\|_\infty).
\end{aligned}                                                    \tag{5}
\]

Choose a fixed eta>0 with eta C2≤1/4, and equip the field curves with
norm ||S||_infinity+eta||v||_infinity. In that norm the right sides of
(5), after multiplying the second by eta and adding, have coefficient
at most

\[
\eta C_2+C_1\delta(1+\eta)\max(1,1/\eta).
\]

Decrease delta until this is below 1/2. Iterating Phi is then Cauchy in
the closed field set: the distances between successive iterates are
bounded by a geometric series. The limit is continuous, is a fixed point
by (5), and is unique there. Characteristic uniqueness and (3) establish
the corresponding unique local population solution. Continuity of the
population expectations follows from dominated convergence using the
uniform activation/readout bounds (or (3)).

The shared fields have the differentiability needed in the response proofs.
At the fixed point, differentiating S=E[B^T h1/k] uses only B' and h1',
bounded by C(1+||G||); dominated differentiation therefore makes S continuously
differentiable. L is continuously differentiable as well. Differentiating
the resulting h2, r and V then costs at most C(1+||G||²), again integrable
under the Gaussian seed law. Thus these fields are continuously
differentiable. The same argument applies to a passive query after the
training fixed point has been constructed; passive queries do not enlarge
the finite list of self-consistency fields.

## Continuation and uniqueness on every finite interval

Fix T. Bounds (1)–(2) and the bounds on A,B,L give common finite radii for
the local construction at every restart time up to T. The local Lipschitz
constants above do not depend on the magnitude of w(t0): tanh and its
derivatives are uniformly bounded. The Gaussian seed distribution of G
is unchanged by evolution. Consequently delta, eta, and the field bounds
can be chosen uniformly at all these restart times, using T-dependent
constants only. A finite number of intervals constructs the solution up
to T. Every other solution with the stated continuous contractions obeys
the same a priori bounds and the local fixed-point uniqueness, so it
agrees interval by interval.

The small-response theorem supplies the additional all-time fitting and
error estimates by its separate activity bootstrap. The present lemma
supplies the well-defined Gaussian population object to which that
bootstrap and its source calculations apply. It does not supply a scalar
approximation algorithm or an empirical-law sampling theorem.

## Extension to bounded smooth activations

The population existence argument and the small-response theorem in
`KERNEL_SCALAR_ROUTE_20260930.md` also hold for any real C² activation phi
satisfying

\[
\sup|\phi|\le B_0,\qquad \sup|\phi'|\le B_1,
\qquad \sup|\phi''|\le B_2<\infty.                    \tag{6}
\]

In that construction replace its initial features and gates by

\[
p_a=\phi(w_0u_a),\quad q_a=\phi'(w_0u_a),\quad
H_a=\phi(Gp_a),\quad d_a=\phi'(Gp_a).
\]

Keep the same normalized contraction definitions, tensor S, moving-kernel
ODE and query decoder. Assume zero initial readout and positive-definite
initial Gram K0 as before. The constants and admissible amplitude now also
depend on B0,B1,B2. The dynamic state count, O(a^5) all-time output error,
and O(a^6) loss error are unchanged.

Here are the checks behind this extension. For existence, the readout bound
becomes C'≤2B0(B0 C+Y), still finite on every finite interval; A and B
remain bounded by the corresponding integrals with factors B1 and B0.
The only local characteristic derivatives through G and G^T still involve
at most two factors of G. Their other factors are controlled by (6), so
the Gaussian contraction proof is unchanged up to constants. In the
response expansion, |phi(x+h)−phi(x)|≤B1|h|,
|phi'(x+h)−phi'(x)|≤B2|h|, and
|phi(x+h)−phi(x)−phi'(x)h|≤B2|h|²/2 are precisely the estimates used to
obtain the second- and fourth-order feature remainders. No third derivative,
analytic continuation, parity, or identity phi'=1−phi² is used. The
tensor Gram and its positive completion are algebraic and remain valid.
The residual-relative source and integrated feedback proof then give the
same conclusions.

This extension does not include nonsmooth ReLU, unbounded polynomial
activations, or any singular initial training Gram without further work.
