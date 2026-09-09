# Actual trained trajectories need not preserve top contrast/readout alignment

Root structural test, 2026-09-06. Unreviewed candidate proof.
This refutes a proposed invariance premise for transferring the
frozen-top traversal estimate. It does NOT refute the activation's
population theorem or establish a typical large-width failure.

We use the contract's exact raw model, opposite labels, rho=0, and
phi(z)=z+log(1+exp z). The finite network below trains ALL its parameter
blocks. No externally prescribed lower forcing is substituted.

## 1. Statement and setup

For every fixed n>=4 and every prescribed tau>0, there is a
deterministic initial state with exactly zero readout and a physical
time t in (0,tau) for which one top neuron satisfies

  W^(4)_1>0,             z^(3)_{1,1}-z^(3)_{2,1}<0.       (1)

The initial state is selected after n and tau; one fixed initial
state is not claimed to have such times accumulating at zero.
Across the constructed family the initial weight operator norms,
the initial norm ||W^(1)||_F, and each initial hidden vector norm
||z^(ell)_a||_2/sqrt(n), ||h^(ell)_a||_2/sqrt(n) are bounded by fixed
constants. No bound on the full raw norm of the parameter itself is
claimed: ||W^(2)||_F=sqrt(n).

Thus the sign of the readout need not agree with the current sample
contrast even when it starts from zero readout and initially moves in
the agreeing direction. The construction has exact finite sample
exchange symmetry, so its label-mode feature path is a positive time
change of its ACTUAL physical loss gradient flow on this short interval.

For each fixed n and each fixed small parameter in the construction,
strict (1) persists on an open neighborhood of initial weights.
The prescribed finite independent Gaussian initialization assigns that
neighborhood positive probability, including its genuinely nonzero
random readout. No lower probability bound uniform in n is claimed.

Take d=2, x_1=sqrt(2)e_1, x_2=sqrt(2)e_2, y=(1,-1).
Let P be the neuron permutation (1 2)(3 4), fixing all later neurons.
Choose A>B and C>D, for example A=1,B=0,C=2,D=0. Set the initial first
preactivations to

  z^(1)_1=(A,B,C,D,0,...,0),   z^(1)_2=P z^(1)_1,

by taking the two columns of W^(1) to be these vectors divided by
sqrt(2). Set W^(2)=I_n. Write

  S=h^(1)_1, T=h^(1)_2=P S,
  H=h^(2)_1=phi(S), h^(2)_2=P H,
  Delta=H_1-H_2>0, E=H_3-H_4>0.

These are finite coordinates; phi is applied componentwise. Fix b>0.
The third matrix initially has rows

  row 1 = a(e_1-e_2)^T+c(e_3-e_4)^T,
  row 2 = -row 1,
  row 3 = b(e_1-e_2)^T,
  row 4 = -row 3,
  all later rows =0.

First set a=-1 and c=Delta/E. Thus the first two top neurons have
both preactivations zero, while neuron 3 has the pair (b Delta,-b Delta)
and neuron 4 its reverse. Set W^(4)=0.

The norm bounds stated above follow directly. The first matrix has
only four nonzero rows; W^(2) has operator norm one; W^(3) has only a
fixed 4-by-4 block; the readout is zero. All hidden coordinates are
uniformly bounded at initialization, including the nonzero constant
activations at indices larger than four. Their norms divided by
sqrt(n) are therefore bounded independently of n.

## 2. Exact symmetry and the physical clock

Let R exchange the two input coordinates. The initial state is fixed
by the transformation

  W^(1) -> P W^(1) R,
  W^(2) -> P W^(2) P^T,
  W^(3) -> P W^(3) P^T,
  W^(4) -> -P W^(4).

The listed identities can be checked row by row. This transformation
is an isometry for the raw metric, exchanges the two samples, and
negates their predictions. Both L and g=(f_1-f_2)/2 are invariant.
Their smooth finite gradient fields are therefore equivariant:
differentiating invariance in a direction and using the isometry proves
grad g(S theta)=S grad g(theta), and the same for L.
Uniqueness of the finite smooth ODE preserves the fixed-state subspace.
It follows that f_2=-f_1 and the forward sample fields are permuted
by P. The residual-free backward fields instead obey the
minus-permutation law, from W^(4)=-P W^(4).

Below primes mean exact feature ascent theta'=grad_raw g. On these
symmetric paths -grad_raw L=4(1-g)grad_raw g. Since g(0)=0, for a
sufficiently short interval 1-g>0. The inverse clock
t(s)=integral_0^s [4(1-g(u))]^-1 du is then well defined and strictly
increasing. It yields the actual finite physical GF, not a finite
symmetry-in-law argument.

At zero readout all initial hidden velocities vanish, and

  (W^(4))'=V,   V=(h^(3)_1-h^(3)_2)/2.

The exact identity phi(z)-phi(-z)=3z gives initially

  V_1=V_2=0, V_3=v=3b Delta/2>0, V_4=-v,
  V_i=0 for i>4.

## 3. A nonzero second-order contrast rotation from the lower layers

Put r=phi'(b Delta), l=phi'(-b Delta), and Q=bv(r+l)>0.
At the initial state, differentiation of the residual-free backward
definitions gives

  (q^(2)_1)'=(q^(2)_2)'=Q(e_1-e_2).

Indeed only top neurons 3,4 contribute: their opposite readout
derivatives and opposite third-matrix rows cancel the two signs.
For i=1,2 set

  P_i=phi'(S_i)>0,       U_i=phi'(z^(1)_{1,i})>0.

Consequently

  (delta^(2)_1)'=Q(P_1,-P_2,0,...,0),
  (delta^(2)_2)'=Q(P_2,-P_1,0,...,0).                   (2)

Since W^(2)=I and C_input=I_2, the first-coordinate acceleration is

  (z^(1)_1)''= (1/2)phi'(z^(1)_1)(delta^(2)_1)',
  (z^(1)_2)''=-(1/2)phi'(z^(1)_2)(delta^(2)_2)'.

Let g_1=||S||^2/n and h_1=S^T T/n. Differentiating the raw W^(2)
update and z^(2)_a=W^(2)h^(1)_a, with all first hidden velocities zero,
gives

  (z^(2)_1)''
    =(1/2)[g_1(delta^(2)_1)'-h_1(delta^(2)_2)']
       +(1/2)phi'(z^(1)_1)^2(delta^(2)_1)'.

Thus the first pair of entries of (h^(2)_1)'' have difference

  J=(Q/2)[
        g_1(P_1^2+P_2^2)-2h_1 P_1P_2
            +P_1^2 U_1^2+P_2^2 U_2^2 ] >0.            (3)

To check strict positivity without an unstated sign hypothesis,
g_1-h_1=||S-T||^2/(2n)>0 and g_1>=0, so the first two terms equal
g_1(P_1-P_2)^2+2(g_1-h_1)P_1P_2>0; the last two are positive.
Every entry numbered at least 3 of (h^(2)_1)'' is zero, by (2),
the displayed first-layer equation and the fact that the corresponding
rows of (W^(2))'' are zero. Symmetry gives
(h^(2)_2)''=P(h^(2)_1)''.

The first third-matrix row has second derivative zero: its row
gradient contains W^(4)_1, and both W^(4)_1 and (W^(4)_1)' vanish
at this base initial state. Its top preactivation acceleration is
therefore its unchanged row applied to the lower feature acceleration.
Writing D_1=(z^(3)_{1,1}-z^(3)_{2,1})/2, we obtain

  D_1(0)=D_1'(0)=0,            D_1''(0)=aJ=-J<0.       (4)

This is the actual trained lower-layer forcing. In particular it is
not proportional to this neuron's initially zero contrast or readout.

## 4. Perturb the initial contrast and obtain strict misalignment

Introduce a small positive parameter e and replace a by a+e/Delta,
leaving c unchanged; keep row 2 equal to minus row 1. All exchange
symmetries remain exact. Initially the first top neuron has
preactivations (e,-e), hence D_1(0)=e and
(W^(4)_1)'(0)=3e/2. Its hidden first velocities still vanish.

For each fixed n, the finite smooth ODE and its derivatives depend
smoothly on these initial data on a uniform small interval for e near
zero. This follows by differentiating the integral equation: all
derivatives of the finite field are bounded on a common compact
neighborhood, Taylor remainders are uniform there, and the elementary
integrating-factor inequality controls their propagated differences.
The second acceleration in (4) is consequently -J+O(e).
In particular the first third-matrix row's formerly zero second
derivative becomes O(e), and is included in this error; it is not
being kept frozen after perturbation.
Also (W^(4)_1)''(0)=0, and at e=0

  (W^(4)_1)'''(0)
      =phi'(0)D_1''(0)=-(3/2)J.

Here differentiating V_1 twice gives
[phi'(z^(3)_{1,1})(z^(3)_{1,1})''
 -phi'(z^(3)_{2,1})(z^(3)_{2,1})'']/2;
the terms quadratic in the first hidden velocities vanish.
Thus uniformly for small s,e,

  D_1(s)=e-(J/2)s^2+O(e s^2+s^3),
  W^(4)_1(s)=(3/2)e s-(J/4)s^3+O(e s^3+s^4).

Choose s_e=2 sqrt(e/J). Then

  D_1(s_e)=-e+O(e^(3/2))<0,
  W^(4)_1(s_e)=(1/2)e s_e+O(e^2)>0

for every sufficiently small e>0. This proves (1), at a time tending
to zero. At still smaller positive times D_1>0 and W^(4)_1>0,
so the readout began aligned and then lost alignment.

The physical clock in Section 2 is positive up to this time for all
sufficiently small e. Fix such an e and its physical observation time.
Continuous dependence of the ACTUAL physical finite GF on ALL initial
weights preserves the two strict inequalities on an open neighborhood.
Every entry of the prescribed finite Gaussian initialization has a
strictly positive density on the real line, independently. Therefore
this open neighborhood has positive probability, without imposing
exact symmetry or exactly zero readout on the random realization.

## 5. Scope

The unconditional aligned-sector premise of the frozen symmetric
top-neuron estimate is false for the fully trained finite network,
already for one fixed smooth convex strongly monotone activation.
This is stronger than a test with an arbitrary external forcing:
the forcing in (3)--(4) is generated by the two lower trainable blocks
with the exact raw metric and normalization.

It does not refute a signed integrated estimate that also accounts
for unaligned excursions. It does not give nonvanishing probability
of failure as n tends to infinity, does not prove a bad population
response, and is not a counterexample to the two-sample target.
The continuation proof must bound those actual excursions or exploit
another mechanism; it cannot simply inherit the frozen alignment
invariant.
