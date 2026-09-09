# The physical clock changes the response by rank one

Candidate pending independent audit. This is an exact finite-width result
for the canonical arctan flow. Together with ACTUAL_SQUARED_LOG_RESPONSE.md
it gives a bound, uniform over all physical times on the established
primal event, on the squared logarithms of every response singular value
except at most the largest and smallest. It does not control the amplitude
of the remaining response directions or prove the population theorem.

Use the raw Euclidean coordinates
\[
\theta=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)},W^{(4)})
\in\mathbb R^N,\qquad N=2n^2+2n.
\]
The feature field is \(b=\nabla(nf_n)\), and the physical field is
\(2(1-f_n)b\). Both hidden matrices remain trained, and \(W^{(4)}\) is
the rescaled readout. The activation, initialization, and raw gradient
metric are exactly those of READOUT_COERCIVITY.md and
ACTUAL_SQUARED_LOG_RESPONSE.md.

## Exact derivative of a state-dependent time change

Fix a reached state \(\theta_0\) with \(f_n(\theta_0)<1\). Write
\(\Phi_s(\theta)\) for the feature flow and \(\Psi_t(\theta)\) for the
physical flow starting at \(\theta\). For finite \(t\) near this orbit,
let \(s(t,\theta)\) solve
\[
\partial_t s(t,\theta)=2[1-f_n(\Phi_{s(t,\theta)}(\theta))],
\qquad s(0,\theta)=0.
\]
The smooth finite-dimensional feature and physical equations imply smooth
dependence on the initial state for finite times in a neighborhood of
\(\theta_0\). The feature-time polynomial bounds ensure the needed
feature flow exists; a sufficiently small initial-state neighborhood
covers each fixed finite physical interval. The chain rule gives
\[
\Psi_t(\theta)=\Phi_{s(t,\theta)}(\theta),
\]
\[
D_\theta\Psi_t(\theta_0)
=D_\theta\Phi_{s(t,\theta_0)}(\theta_0)
 +b(\Psi_t(\theta_0))\,D_\theta s(t,\theta_0).
\tag{1}
\]
The first derivative on the right holds feature time fixed. The second
term is a column times a row, so has rank at most one. It retains the
entire derivative of the physical clock. Equation (1) does not assert
that this rank-one term has small operator norm.

One can check existence and sign of the clock without varying a
probabilistic event. Along every finite physical solution,
\[
\frac{d}{dt}(1-f_n)=-2\kappa_n(1-f_n),\qquad
\kappa_n=\|\nabla(nf_n)\|_2^2/n\ge0.
\]
Thus \(1-f_n\) remains positive at each finite time when positive
initially. All statements about initial derivatives are ordinary
derivatives of the smooth flow, evaluated on the stated primal event;
no differentiation of an event indicator occurs.

For any isometric embedding \(E:\mathbb R^m\to\mathbb R^N\), (1) implies
that the two rectangular response matrices
\[
A=D_\theta\Phi_{s(t,\theta_0)}(\theta_0)E,\qquad
P=D_\theta\Psi_t(\theta_0)E
\]
differ by rank at most one. Both have full column rank, because derivatives
of finite-time flows are invertible.

## Singular-value interlacing and squared logarithms

Let \(A,P\) be any two \(N\)-by-\(m\) matrices differing by rank at most
one. List singular values decreasingly. For \(1\le k<m\),
\[
\sigma_{k+1}(P)\le\sigma_k(A),\qquad
\sigma_{k+1}(A)\le\sigma_k(P).
\tag{2}
\]
Here is a direct proof. Write \(P-A=uv^T\), allowing zero \(u\).
There exists a subspace \(L\subset\mathbb R^m\) of dimension
\(m-k+1\) on which \(\|Ax\|_2\le\sigma_k(A)\|x\|_2\), namely the span
of right singular vectors numbered \(k,\ldots,m\).
Intersecting with \(\ker v^T\) leaves dimension at least \(m-k\).
On that intersection \(P=A\), so the variational characterization of
\(\sigma_{k+1}(P)\) proves the first inequality. Exchange \(A,P\) for
the second.

Assume both matrices have full column rank. For \(2\le j\le m-1\),
\[
(\log\sigma_j(P))_+\le(\log\sigma_{j-1}(A))_+,\qquad
(-\log\sigma_j(P))_+\le(-\log\sigma_{j+1}(A))_+.
\]
Square and sum. Since the positive and negative parts of any real
number have disjoint support, the result is
\[
\sum_{j=2}^{m-1}(\log\sigma_j(P))^2
\le\sum_{j=1}^m(\log\sigma_j(A))^2.
\tag{3}
\]
The left sum is defined to be zero for \(m\le2\). This argument does not
identify or track individual singular vectors across time, and it works
at repeated singular values.

## A uniform physical-time consequence for the actual network

On the canonical high-probability event in READOUT_COERCIVITY.md, let
\(k_0>0\) be its fixed kernel lower bound and \(e_0=1-f_n(\theta(0))>0\).
That theorem proves a finite feature endpoint \(s_*\) with
\[
s(t)<s_*\le e_0/k_0\qquad(t<\infty),
\]
and uniform bounds \(M,R\), independent of width and of physical time,
for both hidden operator norms and the readout norm divided by \(\sqrt n\).
The same bounds hold at the feature endpoint by continuity. The
initialization event also bounds \(e_0\) by a fixed constant, so one may
fix a width-independent \(S_*\) with \(s_*\le S_*\).

For explicit provenance of those constants, the Gaussian corollary uses
initial hidden operator bounds 10, \(b_0=\sqrt{m_3}/2\), and sufficiently
small initial readout norm \(\epsilon_0\). It gives \(k_0=b_0^2/4=m_3/16\)
and \(e_0\le1+a\epsilon_0\). The displacement bound (20) in that note
allows
\[
M=10+2(1+a\epsilon_0)/b_0,\qquad
R=\epsilon_0+2(1+a\epsilon_0)/b_0,\qquad
S_*=4(1+a\epsilon_0)/b_0^2.
\]
These constants are conservative but fixed before the width limit.

Apply the rectangular feature-response estimate (3) of
ACTUAL_SQUARED_LOG_RESPONSE.md on the interval of feature length
\(s(t)\le S_*\). Combining with (1)--(3) gives
\[
\sup_{t\ge0}
\frac1n\sum_{j=2}^{m-1}
\left(\log\sigma_j(D\Psi_t(\theta(0))E)\right)^2
\le C_B(M,R)^2 S_*^2.
\tag{4}
\]
Every \(t\) in the supremum is finite. No derivative of the endpoint
map or infinite-time limit is assumed. The event is the same fixed
primal event for all \(t\) and all \(E\), so a union over times or
embeddings is unnecessary.

The same argument starts at any reached physical time \(t_0\), using the
autonomous flow for duration \(t-t_0\). The corresponding feature
length is at most \(S_*\), and all intermediate states obey the same
primal bounds. Thus (4) holds simultaneously for all
\(0\le t_0\le t<\infty\), with \(D\Psi_{t-t_0}(\theta(t_0))E\) in place
of the displayed response.

In particular, with \(C=C_B(M,R)^2S_*^2\),
\[
\#\{j:|\log\sigma_j(D\Psi_{t-t_0}(\theta(t_0))E)|\ge r\}
\le2+Cn/r^2\qquad(r>0).
\tag{5}
\]
Choose \(E=I_N\) for the full response. Choose
\(E_i u=(0,0,ue_i^T,0)\), which is isometric in the raw coordinates,
for the actual derivative with respect to top column \(i\) in standard
Gaussian coordinates. Write \(Y=D\Psi_{t-t_0}(\theta(t_0))E_i\).
For an auxiliary derivative probe \(g\sim N(0,I_n)\), independent of
the trained trajectory, the full raw-coordinate linear response is
\(Yg\), associated with the infinitesimal top-column perturbation
\(g/\sqrt n\). Conditional on the trajectory, its covariance is
\(YY^T\); its \(n\) nonzero eigenvalues are exactly
\(\sigma_j(Y)^2\), and its remaining \(N-n\) eigenvalues are zero.
No fresh network, frozen coefficient path, or independent trained matrix
is substituted.

## What this estimate does not supply

The clock correction need not vanish; dropping it would give an incorrect
fixed-physical-time derivative. Rank-one interlacing confines its effect
on singular-value counts, even if the correction is large. The two
extreme singular values are excluded explicitly from (4), not estimated.

Even the feature bound permits a singular value of size
\(\exp(C\sqrt n)\), and a finite number of large directions can dominate
the Gaussian response trace or an aligned finite pruning source.
Consequently (4)--(5) do not bound the response energy needed for
global population stability. They also say nothing by themselves about
projection onto hidden parameters, which can lose rank and involves
a different matrix from the full-column-rank responses above.

This new result controls the actual response spectrum uniformly over
physical time, up to at most two extremes. The global canonical
population theorem, unique population continuation, and global
exact-GD identification remain open.

Dependencies: READOUT_COERCIVITY.md for the proved finite-width
high-probability primal/clock bounds, and ACTUAL_SQUARED_LOG_RESPONSE.md
for its stated rectangular feature-response estimate. The time-change,
interlacing, and their combination are proved in this note.
