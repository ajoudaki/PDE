# Compatible data can have finite bad critical states, without initialized failure

Status: analytic candidate derived by the lead author during the plateau
classification continuation, 2026-09-18. The result below is a statement
about ambient states, not the canonical initialized trajectory. It is an
adversarial test of a proposed global proof route.

Scientific inputs: complete `docs/observable_p1.md`, the exact population
state/gradient/existence equations in `docs/global_nonlinear.md`
C.4.7.9.3--4 and C.4.7.10.D.3, and this study's complete
`terminal_geometry.md` and `architectural_loss_floor.md`. No other study
or empirical result is used. The required research and rigorous-math
instructions were read. All population expectations are exact.

## Statement

For the canonical full p=1 architecture on three independent inputs
x_i=sqrt(3)e_i, equal masses 1/3, and labels (1,1,-1), there is a bounded
odd readout c, w=g, and a full-row-rank finite M such that the complete
physical gradient vanishes and L=8/9. This critical point has a strictly
negative second variation in bounded, odd, admissible directions.

On the same data, the prescribed initialized trajectory converges to zero
loss by the signed-axis theorem of `terminal_geometry.md`: reflect the
third input coordinate to obtain inputs (e_1,e_2,-e_3) with labels
(1,1,-1), exactly that theorem's family. The canonical joint marks and
D are invariant under the corresponding signed-coordinate state isometry,
so the two initialized flows are conjugate. Thus this critical point is not an
initialized plateau counterexample. It disproves an ambient no-bad-critical-
points lemma and any global PL claim on all states for even these data.

## Construction respecting the exact dictionaries

In the exact odd sector b_1 is six dimensional and b_2=(B_1,B_2,B_3)
has independent centered coordinates, each with a density positive on
(-1/c_*,1/c_*). Here c_* is the fixed upper normalization from the
canonical initialization, not the readout. Put

  a_i=E_1[b_1 phi(g_i)], phi=tanh.

The initialized calculation gives two nonzero coordinate entries per
a_i, in positions h_i and k_i: nu/a and beta eta/((nu+eta)b), in the
notation of docs/observable_p1.md. The first is strictly positive. Thus
the a_i are nonzero, mutually orthogonal, and have one common squared
norm A>0.

Let E be their three-dimensional span in R^6 and choose orthonormal
vectors n_2,n_3 in E-perp. Define the three rows of M by

  row_1(M)=(a_1+a_2+a_3)^T/A,
  row_2(M)=n_2^T, row_3(M)=n_3^T.

The rows are nonzero and mutually orthogonal, so M has full row rank.
For each i, Ma_i=e_1. Every upper training activation is therefore
H=phi(B_1).

Define J=B_1 phi'(B_1), a bounded odd function, and

  alpha=E[HJ]/E[J^2],
  Q=H-alpha J,
  sigma^2=E[Q^2]=E[QH]>0.

The strict inequality follows because H and J are not proportional in
L2. Their continuous ratio away from zero is

  H/J=sinh(2B_1)/(2B_1),

which is nonconstant on the positive-density open interval. If they were
proportional almost surely, continuity would make this ratio constant
there. Also E[J^2]>0 since J is nonzero except at B_1=0.

Take

  c=Q/(3 sigma^2).

This is bounded and odd. The three predictions equal E[cH]=1/3. The
upper reverse vector for any of them is

  d=E[b_2 c phi'(B_1)]=0:

its first coordinate is E[cJ]=0; its other coordinates vanish by
independence and centering. Thus all first-layer and matrix gradients
vanish. The residual vector is (-2/3,-2/3,4/3); its weighted sum is
zero, so the readout gradient also vanishes. Finally

  L=(1/3)[4/9+4/9+16/9]=8/9.

The state respects the exact initialized mark-negation sector. It uses
the same joint lower marks and upper law, unchanged feature normalization
and actual M transpose. It changes only the trainable state, which is why
it is not an example with the prescribed initialization.

## An explicit descending second variation

Set

  zeta=J-(E[JH]/E[H^2])H,
  q=E[zeta J]=E[zeta^2]>0,
  delta M=e_1 a_3^T/A.

Then E[zeta H]=0, and delta M a_i=0 for i=1,2 while delta M a_3=e_1.
Vary w by zero, c by s zeta, and M by delta M, with s a fixed real
coefficient of the perturbation direction. Every first prediction
variation is zero: the readout variation is orthogonal to H, and the
hidden variation pairs with d=0. For i=1,2 the second variation is zero.
For i=3 it is

  D^2 f_3=2s q+E[c B_1^2 phi''(B_1)].

All displayed quantities are finite because the marks, c and activation
derivatives are bounded. The exact second derivative of unhalved loss is

  D^2 L=2 sum_i p_i[(Df_i)^2+r_i D^2 f_i]
       =(8/9)[2s q+E[c B_1^2 phi''(B_1)]].

Choosing s sufficiently negative makes this strictly negative. The
perturbation is bounded and preserves odd parity. Its matrix can be kept
full row rank by taking the perturbation size sufficiently small, since
full row rank is open. Hence the critical state is a strict saddle even
within that rank class and the initialized parity sector.

## Exact logical consequence

Architectural realizability and full rank of M do not rule out finite
positive-loss critical states. Proving that such states are saddles still
does not exclude convergence to their stable directions from one fixed,
deterministic initialization. The data alone therefore need a trajectory
selection or nondegeneration argument before one can deduce a plateau
classification. No claim of initialized reachability or generic attraction
is made here.
