# Compact response directions and the exact nonlinear limit bridge

Author: `/root`, task `01a09106-41c4-7193-9db9-8068144fd825`.
Status: elementary consequences of the complete frozen P1 proof and
conditional implications; the nonlinear hypothesis below is unproved.
Input scope: P1_SECTION.md, its complete frozen dependencies, the current
notation/reading guide and C.4 proofs. No other P2 route was an input.

## 1. The family of P1 responses is compact

Use P1's clock/HS/readout Hilbert space V, horizon T=40, generator L(t),
propagator U(t,s) and continuous V-valued source integrand b(t,z).
All source values use the actual reference, its Gaussian action and
adjoint. The P1 proof establishes continuity of b on the compact
[0,T]×Z, boundedness, and the Bochner integral against every law.

Let η(h)=sup{∥b(t,z)−b(t,z')∥V: t≤T,dZ(z,z')≤h}. Then η(h)→0
by uniform continuity. If q=W₁(ν,ρ), a coupling with cost arbitrarily
close to q gives

\[
\sup_t\left\|\int b(t,z)d(\nu-\rho)(z)\right\|_V
\le\eta(h)+2M q/h,\qquad M=\sup_{t,z}\|b(t,z)\|_V.       \tag{1}
\]

Indeed restrict the coupling to distances at most h and use η there;
on the complement use 2M and Markov's inequality. Taking h=√q proves
a deterministic modulus tending to zero. For q=0 equality follows
by taking h→0. No TV convergence of laws is used.

Only total boundedness of probabilities in W₁ is needed here. Choose a
finite h-net in the compact data space and partition by the first eligible
net point. Moving each cell's mass to that point costs at most h. The
resulting discrete laws form a finite-dimensional probability simplex,
which is compact; their W₁ distance is bounded by half the data diameter
times their mass-vector l¹ distance. Finite nets of that simplex therefore
give finite 2h-nets of all laws. No completeness or disintegration theorem
for probability measures is used.

By (1), the family bν−ν* is totally bounded in C([0,T];V): choose
finitely many W₁ approximants of probabilities with sufficiently fine
accuracy. Each bν is continuous in t by the compact-domain continuity.
Its closure is compact in that complete space (successive finite nets
produce a Cauchy subsequence from every sequence).

The linear response map from continuous forcing b to
v(t)=∫₀ᵗU(t,s)b(s)ds is bounded into C([0,T];V), with norm at most
T sup∥U∥. Continuity of its output follows from the strong evolution
and the integral equation; the uniform bound follows directly from
the Bochner norm inequality. Therefore

\[
\{v_{\nu-\nu_*}:\nu\in\mathcal P(Z)\}
\quad\hbox{has compact closure in }C([0,T];V).             \tag{2}
\]

This is stronger than mere boundedness of the forced response. Every
continuous bounded linear conversion to raw variations, and every
bounded strongly continuous linear hidden-variation map along the
reference, carries this family to a compact family of continuous L²
curves. To see uniformity in time, approximate the compact path family
by a finite uniform net; for each fixed curve its image is continuous,
using strong coefficient continuity and a common operator bound. Thus
all required compact-family L² tail truncations are uniform over ν.

## 2. Why compact directions permit a strong Taylor step

Let a family Vj in L² have compact closure, let εj→0, and let zj be
any scalar L² fields. For φ with bounded uniformly continuous derivative,

\[
\left\|\frac{\phi(z_j+\epsilon_jV_j)-\phi(z_j)}{\epsilon_j}
                  -\phi'(z_j)V_j\right\|_2\to0.             \tag{3}
\]

This statement is uniform in zj. For a threshold R, the contribution on
|Vj|≤R has norm at most ∥Vj∥₂ times the uniform modulus of φ' at
εjR. The complement has norm at most 2∥φ'∥∞∥Vj1{|Vj|>R}∥₂.
Compact L² families have uniformly vanishing tails: approximate them
by a finite L² net and use
∥V1{|V|>2R}∥₂≤2∥V−W∥₂+2∥W1{|W|>R}∥₂.
First send j→∞ at fixed R, then R→∞. The same proof applies to φ'
for tanh, since φ'' is bounded and uniformly continuous.

(3) can control a proposed approximation whose directions lie in (2).
It does not imply that the actual nonlinear divided differences lie
in a compact family. That latter conclusion requires an independent
reached-trajectory estimate; assuming it would hide the main obligation.

## 3. The finite nonlinear display follows once the population remainder does

Suppose A–B have been proved on a genuine radius δY>0 and suppose, in
addition, the required uniform population remainder is established:

\[
\|f_{\mu_\epsilon}-f_*-epsilon\mathscr D_\sigma f\|_{C([0,T]\times S^1)}
\le\epsilon\omega_Y(\epsilon),\qquad\omega_Y(\epsilon)\to0.   \tag{4}
\]

The data diameter is at most DY=2+2Y. Coupling the unchanged mass of
ν* to itself and the remaining ε mass arbitrarily gives
W₁((1−ε)ν*+εν,ν*)≤εDY. Hence
εY=min(1/2,δY/(2DY)) puts all these laws strictly inside the open
neighborhood, including at ε=εY.

Fix ν, ε∈(0,εY] and a>0. Couple the finite flows for ε and zero using
the same initialization, as required for the finite right derivative.
Write ∥·∥∞ for the displayed time/input norm. The exact triangle
inequality is

\[
\frac{\|f_{n,\mu_\epsilon}-f_{n,*}-\epsilon D_\sigma f_n\|_\infty}{\epsilon}
\le\omega_Y(\epsilon)
+\frac{\|f_{n,\mu_\epsilon}-f_{\mu_\epsilon}\|_\infty
       +\|f_{n,*}-f_*\|_\infty}{\epsilon}
+\|D_\sigma f_n-\mathscr D_\sigma f\|_\infty.              \tag{5}
\]

At each fixed positive ε, B and the reference theorem make the two
prediction errors vanish in probability. P1 makes the last error
vanish in probability. A finite union bound suffices on this common
initialization; their independence is neither needed nor asserted.
For ε small enough that ωY(ε)<a/2, (5) gives a vanishing width-limsup
probability of exceeding a. Sending ε down to zero proves exactly the
user's finite nonlinear display. No εn/width rate is used.

This is a limit bridge, not a proof of (4). Finite differentiability
and convergence of its right derivatives alone cannot supply (4): the
scalar smooth family gn(ε)=ε(1−exp(−nε)) has gn'(0)=0, while its
width-first limit at every ε>0 is ε. This is an elementary logical
counterexample to that inference, not to the neural model.
