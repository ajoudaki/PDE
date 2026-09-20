# Rank-one cancellation and all adjacent gradients do not force input conflicts

Status: analytical candidate derived by the lead author, 2026-09-18.
This is a counterexample to a proposed static implication, not a trajectory
initialized at the canonical state. No compatible initialized plateau is
claimed. The complete lower/upper population laws and matrix dimensions
are unchanged.

Scientific inputs: `docs/observable_p1.md` in full, the state, equations,
physical metric and existence portions of `docs/global_nonlinear.md`
C.4.7.9.3--4 and C.4.7.10.D.3; this study's complete
`architectural_loss_floor.md`, `plateau_ambient_counterexample.md`, and
`plateau_finite_critical.md`. The latter two motivate testing the stronger
case where all three middle-gradient contributions are nonzero. No other
study or empirical result is used. Research and rigorous-math instructions
apply. This file was frozen before independent review.

## 1. Strong statement with exact scope

Fix **any** three linearly independent inputs x_i on sqrt(3) S^2,
positive probability weights p_i, and binary labels y_i. Use the canonical
p=1 marks and normalization, phi=tanh, and the full physical equations.
There exists a finite state in the initialized odd-mark sector such that:

* all three residuals are nonzero;
* all three individual weighted middle-gradient matrices are nonzero
  rank-one matrices, sharing their left and right lines and summing to zero;
* the entire readout and first-layer gradients also vanish;
* the loss is strictly between zero and one, although the data are
  architecturally compatible and admit zero loss.

Thus even the nonzero rank-one version of the user's cancellation lemma,
together with all adjacent nonlinear gradient constraints, imposes **no
restriction on the input arrangement within the independent-triple class**
at the level of existence of a finite stationary state.

This does not imply that such a state is reached from w=g,c=0,M=D.
The state constructed below has a different trained w,c,M. It is a strict
saddle by the separately proved landscape theorem. The initialized
necessary-direction question remains a dynamical reachability question.

## 2. Exact model and conventions

Put u_i=x_i/sqrt(3). In the canonical odd sector b_1 is in R6,
b_2=(B_1,B_2,B_3) is in R3, and M is 3 by 6. The lower marks retain
their complete joint correlations with g. The upper coordinates B_j are
independent, centered, bounded, and have positive densities on their
common open interval. The lower b_1 law has positive density on a
full-dimensional open set, hence E_1[b_1 b_1^T] is positive definite.
These statements follow from the invertible ridge Cholesky map of the
canonical tanh-Gaussian coordinate pairs; no new feature law is selected.

For an arbitrary current state write

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad
 H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i,
 \qquad d_i=E_2[b_2c\phi'(b_2^TMa_i)].                   \tag{1}
\]

The full physical velocities are

\[
 \begin{split}
 c'&=-2\sum_i p_i r_i H_i,\\
 M'&=-2\sum_i p_i r_i d_i a_i^T,\\
 w'&=-2\sum_i p_i r_i\phi'(w\cdot u_i)
                  (b_1^TM^Td_i)u_i.
 \end{split}                                            \tag{2}
\]

Every entry of M remains a trainable variable. Choosing a rank-one current
M in a counterexample does not project the model or its dynamics to
rank one. Below the exact gradient of that full model vanishes at the
chosen state.

## 3. A common ball of realizable lower contractions

The following finite-dimensional convex argument supplies an actual
bounded-displacement lower field, rather than assigning the a_i freely.

Define

\[
 m_0=\min_{|v|=1}E_1|b_1\cdot v|>0.                    \tag{3}
\]

The expectation is continuous in v because b_1 is bounded. It is strictly
positive on the unit sphere because the lower Gram is positive definite;
compactness gives the positive minimum. For each i put

\[
 F_i(\theta)=E_1\log\cosh(g\cdot u_i+b_1\cdot\theta),
                       \qquad\theta\in\mathbb R^6.
                                                               \tag{4}
\]

The expectation is finite: log cosh(z)<=|z|, the Gaussian projection
has finite first moment, and b_1 is bounded. Its gradient and Hessian are

\[
 \nabla F_i=E_1[b_1\phi(g\cdot u_i+b_1\cdot\theta)],
 \quad \nabla^2F_i=E_1[b_1b_1^T\phi'(g\cdot u_i+b_1\cdot\theta)]\succ0.
                                                               \tag{5}
\]

Bounded first and second integrands justify differentiation. Strict
positivity follows from the lower Gram and the strictly positive finite
tanh gate. For every target A with |A|<m_0, the function
F_i(theta)-A dot theta is coercive, since

\[
 F_i(\theta)-A\cdot\theta
 \ge(m_0-|A|)|\theta|-E_1|g\cdot u_i|-\log2.             \tag{6}
\]

It is continuous and strictly convex, so it has a unique finite minimizer
theta_i(A), at which grad F_i=A. Existence follows by restricting to a
large compact ball using (6); uniqueness follows from (5). All constants
and this defining optimization use only declared fixed Gaussian marks
and the input. No future trajectory is used.

Input independence supplies dual vectors t_i with t_i dot u_j=delta_ij.
For independently chosen targets A_i in this common ball, define

\[
               w=g+\sum_i t_i(b_1\cdot\theta_i(A_i)).    \tag{7}
\]

Then w dot u_i=g dot u_i+b_1 dot theta_i(A_i), so its actual lower
contractions in (1) equal A_i simultaneously. The displacement w-g is
bounded, and w is odd under global lower-mark negation, because g and
b_1 are odd. Thus (7) lies in the exact finite-state class. No independence
between g and b_1 is assumed in (4)--(7).

## 4. Prescribed collapsed features with nonzero backward vectors

Choose an index k with p_k<1/2; one exists for every positive triple.
Set

\[
 \sigma_i=y_i\ (i\ne k),\qquad \sigma_k=-y_k,
 \qquad m=\sum_i p_i\sigma_i y_i=1-2p_k\in(0,1).         \tag{8}
\]

Choose any nonzero a in R6 with |a|<m_0. Use (7) with A_i=sigma_i a,
and set

\[
              M=e_1a^T/|a|^2.
\]

The resulting effective vectors are Ma_i=sigma_i e_1, and all upper
activations are H_i=sigma_i H, where H=phi(B_1). Define

\[
 J=B_1\phi'(B_1),\qquad
 U=H-\frac{E_2[HJ]}{E_2[J^2]}J,\qquad
 s^2=E_2[U^2]=E_2[UH]>0.                                \tag{9}
\]

E[J^2]>0. The strict positivity of s^2 follows because H and J are
not proportional on an interval: their ratio at nonzero z is
sinh(2z)/(2z), which is nonconstant. A continuous proportionality almost
surely would hold throughout the positive-density interval. Thus the
projection in (9) is nonzero.

Take the bounded odd readout

\[
                       c=mU/s^2+B_2.                    \tag{10}
\]

Independence and centering of B_2 give f_i=sigma_i m. Since phi' is
even, the same backward vector occurs at each input. Its coordinates are

\[
 d_i=d=\delta e_2,\qquad
 \delta=E_2[B_2^2]E_2[\phi'(B_1)]>0.                    \tag{11}
\]

Indeed the first coordinate is zero by E[UJ]=0 and E[B_2]=0;
the second is the positive displayed product; the third is zero by
independence and centering. The upper gates themselves are everywhere
strictly positive. The backward vector is nonzero, but M^T d=0.

## 5. Verification of every gradient, nonzero rank and loss

Write rho_i=p_i r_i. By (8)--(10),

\[
 \rho_i\sigma_i=p_i(m-\sigma_i y_i)
 =\begin{cases}
 -2p_i p_k,&i\ne k,\\
 2p_k(1-p_k),&i=k.
 \end{cases}                                            \tag{12}
\]

Each coefficient is nonzero and their sum is zero. Thus

\[
 \sum_i\rho_i H_i=H\sum_i\rho_i\sigma_i=0,
 \qquad
 \sum_i\rho_i d_i a_i^T=d a^T\sum_i\rho_i\sigma_i=0.     \tag{13}
\]

Every individual matrix rho_i d_i a_i^T is a nonzero rank-one matrix,
with both common left and common right factor lines. The readout and
matrix velocities vanish by (13). The first-layer velocity vanishes
pointwise because M^T d_i=0 individually. This checks every equation (2),
including all nonlinearities and their derivatives.

The positive loss is

\[
 L=\sum_i p_i(m-\sigma_i y_i)^2
   =1-m^2=4p_k(1-p_k)\in(0,1).                          \tag{14}
\]

All three residuals are nonzero. The canonical initialized hidden
features can fit these independent inputs with a suitable bounded
readout, by the established three-feature independence calculation in
this study. Thus (14) is strictly above the architectural minimum zero.

For a balanced example choose labels (+,+,-), weights (1/4,1/4,1/2),
and k=1. Then sigma=(-,+,-), m=1/2, predictions are (-1/2,1/2,-1/2),
and L=3/4. The three weighted middle matrices are respectively

\[
            \tfrac38 d a^T,\quad-\tfrac18 d a^T,
                         -\tfrac14 d a^T.
\]

One may use the nonorthogonal independent directions

\[
 u_1=e_1,\qquad u_2=(e_1+2e_2)/\sqrt5,\qquad
 u_3=(e_1+e_2+3e_3)/\sqrt{11}.
\]

These have neither coincidences nor antipodes; the construction holds
for every independent triple, not just this example. The lower field
and current matrix/readout are constructed states, not the canonical
initial values. No initialized limiting trajectory is claimed.

## 6. Zero-contribution and near-cancellation alternatives are also real

The rank-one obstruction is not the only compatible bad critical branch.
For the same a_i and U, omit B_2 from (10), and extend the first row of M
by two nonzero independent rows n_2^T,n_3^T perpendicular to a. The new
M has full row rank, still sends a_i to sigma_i e_1, and now every d_i=0.
The same predictions and positive loss remain, and every full gradient
vanishes. In this version each middle contribution is zero rather than
rank one. Thus full row rank of M does not exclude finite bad critical
states either.

For a near-critical variant with nonzero rank-one contributions and a
full-row-rank matrix, keep the readout (10) and let M_epsilon have the
first row a^T/|a|^2 and other rows epsilon n_2^T,epsilon n_3^T. For
epsilon>0 it has full row rank. All predictions, d_i, individual middle
contributions and their exact cancellation remain unchanged. The readout
and middle velocities are exactly zero; the lower velocity is proportional
to epsilon because M_epsilon^T d=epsilon delta n_2. Its norm tends to
zero, while the positive loss (14) is unchanged. This is a family of
states, not a family of reached trajectories or a proposed optimizer.

## 7. Precise consequence for the proposed proof route

The rank-one cancellation lemma is valid. Its claimed implication from
simultaneous stationarity to an input-level architectural conflict is
false, even with nonzero residuals and nonzero middle-gradient factors.
All those constraints can instead be satisfied by learned forward
collapse and a nonzero backward direction annihilated by M^T.

The necessary direction for canonical initialized plateaus is not
disproved by this construction. It remains open because one must prove
that the prescribed initialized trajectory cannot approach these states
(or other compatible saddles or escaping states). Algebraic stationary
constraints alone cannot supply that exclusion: the construction meets
them for every independent input triple. A useful next invariant would
need to control the *reached* forward/backward alignment or the relation
between the accumulated readout and M, and would also have to exclude
the full-row-rank zero-backward-response alternative of Section 6.
