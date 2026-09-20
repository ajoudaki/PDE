# Arbitrarily many finite inputs: exact fitting and an open exponential basin

Lead-author continuation, 2026-09-18. Scientific inputs: complete canonical
`docs/observable_p1.md`; own-study `initialization_positivity.md`,
`architectural_loss_floor.md`, `basin_spectral_route.md`,
`basin_open_fitting.md`, and `basin_hilbert_fitting.md`. This is a new
finite-sample extension of their proofs, not a neural-width theorem or a
claim about the prescribed initialized trajectory. No numerical premise.

## 1. Scope and theorem

Fix d>=2, any finite number m, normalized inputs x_i in sqrt(d) S^(d-1),
positive masses p_i summing to one, and binary labels y_i. Keep the exact
canonical p=1 Gaussian-derived correlated marks, ridge 1/4096, odd sector,
full M in R^(d x 2d), actual transpose, and physical unhalved square loss.
Initially g and the dictionary laws have exactly the canonical joint law.
The ambient physical state coordinates are theta=(w-g,c,M) in

\[
\mathcal H_d=L^2_{\rm odd}(\Omega_1;\mathbb R^d)
 \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{d\times2d}.
\]

Assume architectural compatibility: coincident inputs have equal labels,
and antipodal inputs have opposite labels. Merge such copies by orienting
one representative of each pair and summing its masses. Henceforth there
are m representatives distinct modulo sign. This merging preserves the
loss and all three vector-field blocks exactly, by oddness of prediction
and its state differential.

**Theorem.** For every such finite law, regardless of m or input rank,
there is an explicit fitted state theta_* with w=g and M=D, and a nonempty
open subset U of the full physical Hilbert space such that the full
feature-learning dynamics from every theta_0 in U satisfies

\[
 L(t)\le L(0)e^{-2\gamma t},\qquad
 \|\theta(t)-\theta_\infty\|_{\mathcal H_d}
 \le (C/\gamma)\sqrt{L(0)}e^{-\gamma t},\qquad L(\theta_\infty)=0.
\tag{1}
\]

All quantities defining U,C,gamma are finite expectations or matrix
operations from the fixed data and initialization. Canonical initialization
has c=0; the fitted center has a different explicitly constructed readout.
This theorem does not assert that the canonical point belongs to U or
that almost every initial state enters U.

## 2. Initialized nonlinear features distinguish all finite inputs

Write u=x/sqrt(d). The exact coefficient calculation gives

\[
 D a_0(x)=(T(u_1),\ldots,T(u_d)),\qquad
 T(r)=E[\Psi(\phi(G))\phi(rG+\sqrt{1-r^2}V)],\quad\phi=\tanh,
\tag{2}
\]

with independent standard Gaussians G,V and endpoint values by continuity.
The complete scalar coefficient Psi is defined in
`initialization_positivity.md`, including the reverse response and ridge.
Its proved bound gives Psi(h)>0 for h>0 and oddness. Its scalar constants
are independent of d: the canonical construction simply repeats independent
coordinate pairs. Thus that proof applies verbatim in each dimension.

For completeness, strict increase of T needs only that sign property.
For g>0 and 0<=r<1, put m_r(g)=E phi(rg+sqrt(1-r^2)V). Differentiation
and Gaussian integration by parts give

\[
 \partial_r m_r(g)=gE\phi'(rg+\sqrt{1-r^2}V)
              -rE\phi''(rg+\sqrt{1-r^2}V)>0.\tag{3}
\]

The first term is positive. For r>0, minus the second derivative has
expectation 2E[phi(Z)phi'(Z)]>0 for a Gaussian Z with positive mean:
pairing positive and negative arguments multiplies the positive odd
integrand on (0,infinity) by the positive density difference there.
At r=0 the second term vanishes. Bounded derivatives justify the integration
by parts; after it, |partial_r m_r(g)|<=|g|+2 is integrable against the
bounded Psi. Oddness in g and the sign of Psi therefore imply T'(r)>0
on [0,1). T is odd, and dominated convergence at +/-1 extends strict
increase to [-1,1]. In particular (2) is nonzero and injective modulo
sign on the normalized sphere.

The upper mark law has positive density on an open cube about zero.
For any finite nonzero vectors v_i distinct modulo sign, the functions
phi(b_2 dot v_i) are linearly independent in L2. Here is a proof without
a restriction on the number of features. An almost-sure linear identity
extends to the cube by continuity. Choose e avoiding the finitely many
hyperplanes where e dot v_i=0 or |e dot v_i|=|e dot v_j|. Restriction
to b_2=s e and the real-analytic identity principle extend it to every
real s. Orient each coefficient so its slope a_i=|e dot v_i| is positive.
The a_i are distinct. An identity sum_i A_i tanh(a_i s)=0 first gives
sum_i A_i=0 at positive infinity. If some coefficient is nonzero, the
smallest a_i with nonzero coefficient then gives

\[
 \sum_i A_i\tanh(a_i s)
       =-2A_i e^{-2a_i s}+o(e^{-2a_i s}),
\]

a contradiction. Thus every coefficient is zero. No relation among the
raw input vectors enters this argument.

Apply this to v_i=D a_0(x_i) and put

\[
 H_i^0=\phi(b_2^TD a_0(x_i)),\qquad K_{ij}=E_2[H_i^0 H_j^0].
\]

Then K is positive definite for every finite compatible representative
list, even when m>d. The explicit bounded odd readout

\[
 c_*=\sum_i (K^{-1}y)_iH_i^0,\qquad \theta_*=(0,c_*,D)
\tag{4}
\]

fits every input. These hidden coordinates describe a center of a basin;
all hidden and readout blocks remain trained in the dynamics near it.

For an incompatible finite law, the identical argument proves the exact
attained architectural floor. In each signed raw-input class write
x_i=sigma_i x_G, W_G=sum_{i in G}p_i and
m_G=W_G^{-1}sum_{i in G}p_i sigma_i y_i. Then

\[
 L=L_{\rm odd}+\sum_GW_G(f(x_G)-m_G)^2,\qquad
 L_{\rm odd}=\sum_G W_G(1-m_G^2).
\tag{5}
\]

The initialized-feature readout interpolates the m_G, so this floor is
attained. This proves an expressivity statement for all finite laws, not
that every trained trajectory attains (5).

## 3. Explicit open fitting region in the physical norm

Let B_1 and B_2 be finite upper bounds for |b_1| and |b_2|, respectively;
they are deterministic constants, not additional random marks. Define

\[
 P=\operatorname{diag}(p_i),\quad
 \gamma=\lambda_{\min}(P^{1/2}KP^{1/2})>0,
 \quad D_H=B_1B_2(1+\|D\|_F),
\]
\[
 \rho=\min\{1,\gamma/(4D_H)\},\quad
 R_c=\|c_*\|_2+1,\quad R_M=\|D\|_F+1,
\]
\[
 C=2[1+B_1B_2R_c(1+R_M)],\qquad K_f=1+\|c_*\|_2D_H.
\tag{6}
\]

All constants are explicit in known integrals and fixed data. Set
h=||theta-theta_*||_H. The lower moments satisfy
|a_i-a_i^0|<=B_1||w-g||_2. Splitting M a_i-D a_i^0, with |a_i|<=B_1,
therefore gives

\[
 \|H_i-H_i^0\|_\infty\le D_Hh.\tag{7}
\]

The weighted synthesis operator z -> sum_i sqrt(p_i)z_i H_i has norm
at most one, since |H_i|<=1 and sum_i p_i=1. Its difference from the
initialized operator has norm at most D_Hh by Cauchy--Schwarz. Thus the
weighted current readout Gram differs from P^(1/2)KP^(1/2) in operator
norm by at most 2D_Hh. For h<rho it is at least (gamma/2)I.

Continuity of prediction and (7) give sqrt(L)<=K_f h near the fitted
center (in fact the bound holds for every h). Within h<rho, the exact
physical equations and sum_i p_i|r_i|<=sqrt(L) give

\[
 \|\dot c\|_2\le2\sqrt L,\quad
 \|\dot M\|_F\le2B_1B_2R_c\sqrt L,\quad
 \|\dot w\|_2\le2B_1B_2R_MR_c\sqrt L.
\]

The sum bounds the product Hilbert norm, so ||dot theta||_H<=C sqrt L.
The readout part of the actual dissipation identity alone gives

\[
 L'\le-4(P^{1/2}r)^TG_c(\theta)(P^{1/2}r)
        \le-2\gamma L.\tag{8}
\]

Define

\[
 U=\{\theta:\|\theta-\theta_*\|_H+(C/\gamma)\sqrt{L(\theta)}<\rho\}.
\tag{9}
\]

It is open and contains the ball of radius
rho/[2(1+(C/gamma)K_f)] about theta_*. Until any first exit from h<rho,
q=sqrt L obeys q'<=-gamma q where q>0. If q reaches zero the entire
flow is stationary. Integrating gives

\[
 \int_0^t Cq(s)ds\le(C/\gamma)(q(0)-q(t)).
\]

The triangle inequality therefore proves
h(t)+(C/gamma)q(t)<=h(0)+(C/gamma)q(0)<rho. An exit contradicts
continuity, so U is forward invariant. The exact global Hilbert flow
exists by the bounded-mark argument in basin_spectral_route.md Section2,
which uses only finitely many bounded inputs, not their independence.
Integration of the speed bound gives finite Hilbert length and (1).
Finite-time inverse images enlarge U to an open fitting basin.

## 4. Scope checks

Linear dependence, arbitrary m>d and arbitrarily close but distinct
unoriented inputs are admitted. Constants can deteriorate as the nonlinear
Gram becomes ill-conditioned; no geometry-independent rate or radius is
claimed. A fixed d-by-2d middle matrix imposes no upper bound m<=d on
finite expressivity because its upper nonlinear features range over a
population of marks, not d scalar neurons.

For arbitrary infinite-support laws, positivity of every finite Gram does
not give a bounded inverse of an infinite Gram operator, a positive spectral
gap, or an exact bounded readout interpolant. The finite proof does not
establish those claims. The theorem is about a nonempty open basin, not
full-measure attraction or canonical initialized fitting. In particular it
does not settle the remaining dependent-input full-Hilbert saddle-basin
question by substituting an easier initialization.
