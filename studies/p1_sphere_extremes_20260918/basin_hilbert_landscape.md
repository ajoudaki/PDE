# Every positive-loss Hilbert equilibrium below loss one is a strict saddle

Lead-author extension, 2026-09-18. Inputs: exact canonical equations in
docs/observable_p1.md and the fixed-order existence sections of
global_nonlinear.md; the complete frozen own-study basin_spectral_route.md
and the upper separation argument of plateau_finite_critical.md. This
argument is developed after the independent spectral route froze. It
extends its strict-saddle input from bounded fields to the full physical
Hilbert space, for independent input directions. No empirical premise.

Use H and the globally defined physical Hilbert gradient flow of Sections
1--4 of basin_spectral_route.md. There are three independent unit directions
u_i=x_i/sqrt(3), positive weights and binary labels; all canonical marks
are retained. State coordinates are theta=(w-g,c,M) in H. In particular
w and c are finite almost surely and square integrable, but no essential
supremum bound on w-g or c is assumed. Denote the usual lower contractions
by a_i, upper vectors by v_i=Ma_i, upper features by H_i=phi(b_2.v_i),
and weighted residuals by rho_i=p_i(f_i-y_i).

## 1. Surjective lower differential at every Hilbert state

Let t_i be the dual input vectors, t_i.u_j=delta_ij, and define

\[
 K_i=E_1[b_1b_1^T\phi'(w\cdot u_i)].
\]

For any nonzero vector q, q^T K_i q>0: phi' is strictly positive almost
surely since w is finite, and the positive-definite ungated lower Gram
makes (b_1.q)^2 positive on a set of positive probability. K_i is therefore
an invertible 6 by 6 matrix. For any prescribed A in R6, the bounded odd
lower variation

\[
 h=t_i(b_1^TK_i^{-1}A)
\]

satisfies D a_i[h]=A and D a_j[h]=0 for j!=i. Differentiation is justified
by the finite-moment C1,1 estimate in the spectral route. This works at
arbitrary Hilbert states, including unbounded displacements; no Gaussian
tail separation is needed because the inputs are independent.

## 2. One derivative feature cannot lie in the current feature span

For any v in R3 and any nonzero z in R3, put

\[
 \psi(b)=(b\cdot z)\phi'(b\cdot v).
\]

Then psi is not in the span of finitely many current tanh features
phi(b.v_j), provided v is one of the v_j (zero is allowed). Equal or
opposite nonzero v_j may first be grouped; zeros contribute no feature.
The canonical upper law has positive density on an open cube containing
zero. An almost-sure identity between these analytic functions would
hold on that cube, and hence along every real line through it by the
one-variable analytic identity principle.

Choose a line b=s e with z.e!=0 and with the absolute projections of
all distinct signed nonzero feature groups nonzero and pairwise distinct.
Only finitely many proper hyperplanes are excluded. If v=0, psi(s e)
is a nonzero linear function of s, while every tanh combination is bounded
on the real line, which is impossible.

Otherwise write a=|e.v|>0. Along the positive ray psi equals a nonzero
constant times s sech^2(a s), asymptotic to C s exp(-2a s). Orient all
distinct feature rates positively, so a putative identity has the form
sum_j q_j tanh(a_j s)=C_0 s sech^2(a s), with distinct a_j>0 and a
among them. Taking s to infinity first gives sum_j q_j=0. If some q_j
is nonzero, let a_min be the smallest rate with nonzero coefficient.
The left side is then asymptotic to -2q_min exp(-2a_min s), since
tanh(t)=1-2exp(-2t)+O(exp(-4t)). Dividing the purported identity by
exp(-2a_min s) gives a nonzero finite limit on the left; on the right
the limit is zero if a>a_min, and has unbounded magnitude if a<=a_min.
Both are contradictions. If all q_j are zero, psi is nonzero and the
identity is again impossible. This proves the claimed separation.

## 3. Negative curvature at every nonfitting equilibrium with M nonzero

Let theta_* be any critical Hilbert state with positive loss and M!=0.
Choose i with rho_i!=0 and A with z=M A!=0. The lower variation in
Section 1 changes only a_i to first order and changes H_i by

\[
 \psi_i(b_2)=(b_2\cdot z)\phi'(b_2\cdot v_i).
\]

Let k be psi_i minus its L2 projection onto span{H_1,H_2,H_3}. By
Section 2, k is nonzero. It is bounded and odd, is perpendicular to
every H_j, and E[k psi_i]=||k||_2^2>0. Its pure readout prediction
variation and pure readout loss curvature vanish. The mixed loss
curvature with the lower direction is 2 rho_i ||k||_2^2. Consequently

\[
 D^2L(\theta_*)[(h,s k,0),(h,s k,0)]
 =D^2L(\theta_*)[(h,0,0),(h,0,0)]
                  +4s\rho_i\|k\|_2^2.
\]

All terms are finite: the variations are bounded, the marks are bounded,
activation derivatives are bounded, and c is integrable by c in L2.
A finite choice of s makes this strictly negative. The actual Hilbert
second differential at this equilibrium exists by the small-remainder
argument in basin_spectral_route.md, so this is negative Hilbert curvature,
not merely a formal directional calculation.

At any critical point with 0<L<1, M must be nonzero, since M=0 gives
zero predictions and binary labels give L=1. The preceding proof applies.
Some upper feature is nonzero, also because otherwise L=1. A pure readout
variation by that feature has strictly positive loss curvature. Thus
both stable and unstable spaces are nontrivial in the finite-rank
linearization. All associated nonzero eigenvectors are bounded fields.

## 4. Consequences and scope

The center-stable Hilbert construction and countable-cover proof in the
spectral route therefore apply to the entire set of critical H-states
with 0<L<1, without an essential-boundedness condition on their limits.
Every H-convergent trajectory has a critical limit: local continuity of
the vector field would otherwise give a continuous linear functional
whose value on the velocity has a fixed nonzero sign near the limit,
contradicting convergence after time integration. Continuity of L in H
gives its limiting loss.

Accordingly, the basin of trajectories with a Hilbert-space limit and
limiting loss in (0,1) is meagre by that proof. A subsequent probability
argument must still verify the needed regularity of backward images.
No convergence of every trajectory is asserted. Loss-one degenerate
M=0 equilibria and nonconvergent positive-loss behavior are outside this
statement. The deterministic canonical trajectory has loss below one
after any positive time, so its possible positive-loss H-limit falls
inside the scope; genericity alone does not decide its membership.
