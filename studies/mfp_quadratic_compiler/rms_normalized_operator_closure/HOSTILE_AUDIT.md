# Hostile audit of normalization and compactness

## What is controlled exactly

For every state,

\[
\alpha,\beta\ge\sqrt\epsilon,
\qquad \langle H^2\rangle_n<1,
\qquad \langle Y^2\rangle_n<1.                      \tag{1.1}
\]

Thus small denominators are eliminated.  The derivative of `N_epsilon` has
operator norm at most `epsilon^{-1/2}` in empirical `L2`.

This does not make the composite map `x -> N_epsilon(x^2)` uniformly
Lipschitz in width.  Since its derivative contains multiplication by `2x`,

\[
\sup_x\|D[N_\epsilon(x^2)]\|_{2\to2}
\le \sqrt2\,n^{1/4}\epsilon^{-1/4},                 \tag{1.2}
\]

and the `n^{1/4}` scale is attainable up to constants.  The normalization
contraction suppresses the radial component only by
`epsilon/sigma^2`; all orthogonal components pass unchanged before the
common denominator.

## Coordinate spikes survive bounded RMS

Although `||N_epsilon(v)||_n<1`, its largest coordinate can approach
`sqrt(n)`.  Taking `v=(L,0,...,0)` and sending `L` to infinity proves the
claim.  Empirical `L2` control therefore does not imply a coordinate or
multiplication-operator bound.

A stronger current-state discontinuity is possible on the exact network
constraint manifold.  Fix a constant realizable `H=h_0 in (0,1)`.  Choose
one nonzero coordinate

\[
Z_1=n^a,\qquad A_1=n^{1/2-a},\qquad 0<a<1/4,         \tag{2.1}
\]

and set `G=(Z tensor H)/h_0^2`, so `GH=Z`.  Then

\[
\|A\|_n,\ \|Z\|_n,\ \|G\|_F,\ \|Y\|_n,\ |f|
\longrightarrow0,                                  \tag{2.2}
\]

but, with `R=(2/beta)Z(A-fY)`,

\[
\langle R^2\rangle_n\longrightarrow{4\over\epsilon},
\qquad
K_G\longrightarrow{4h_0^2\over\epsilon}.          \tag{2.3}
\]

Thus even strong convergence of the naive Hilbert fields and of output/loss
does not make `K` continuous.  A valid topology must control the aligned
weighted product `Z^2(A-fY)^2`.  The first-layer term additionally needs
control of `H(Pi_H G^T R)^2`.

This is an ambient/restart-state obstruction.  It does not prove that the
iid-Gaussian trajectory reaches such a spike on an order-one horizon.

## Adaptive matrix alignment

Let `q` have empirical norm one, let `G` be an iid Gaussian matrix core, and
put `d=G^Tq`.  The choices

\[
H=d/\|d\|_n,
\qquad \widetilde H=P_\pi H                       \tag{3.1}
\]

for an independent random permutation have the same coordinate multiset
and all the same scalar moments.  Nevertheless

\[
\langle q,GH\rangle_n\to1,
\qquad
\langle q,G\widetilde H\rangle_n\to0               \tag{3.2}
\]

in probability.  Separate marginal laws and any collection of their scalar
moments therefore lose dynamically relevant alignment.  A true current
operator state can distinguish (3.1), so this is not a universal no-go.

## Why the radial runaway is not simply destroyed

For `epsilon=0`, normalization is radially invariant.  At fixed positive
`epsilon`, radial sensitivity is small but nonzero.  The scalar normalized
quadratic

\[
h(s)=s^2/\sqrt{s^4+\epsilon}
\]

trained toward one has no finite positive stationary point: its raw scale
increases to infinity while `h(s)` approaches one.  This proves that RMS
normalization alone is not a coercive raw-parameter mechanism.  It is not a
reachable-runaway theorem for the full network, because the trained readout
provides another interpolation route.

## Exact compactness that is available

Loss dissipation yields dimension-free one-half-Holder control in the muP
metric and, for `Q=G-G(0)`, a bounded equicontinuous Hilbert--Schmidt path.
It does not control maxima, the weighted products in (2.3), or the adaptive
actions `G(0)H_t` and `G(0)^TR_t`.

Eliminating the current matrix makes the missing information explicit:

\[
G_t=G_0+\int_0^t 2\eta e_sR_s\otimes H_s\,ds,
\]
\[
G_t^{\mathsf T}R_t
=G_0^{\mathsf T}R_t
\int_0^t2\eta e_sH_s\langle R_s,R_t\rangle_n\,ds.  \tag{4.1}
\]

Hence removing `G` produces a two-time Gram kernel, which is forbidden.
Keeping `G` is Markovian, but its Gaussian core needs a limiting structure
that supports both matrix action and coordinatewise multiplication.

## Hierarchy audit

Differentiating the reduced current message `g=G^TR` generates terms of the
form

\[
G^{\mathsf T}M_1G\mathcal Q_HG^{\mathsf T}M_2G\cdots,
\]

with new multiplication marks.  Likewise, differentiating scalar moments
of `H` introduces new mixed moments with `g`.  A finite scalar-moment closure
therefore does not close.  A state indexed by every alternating word or
rooted traffic graph would close formally, but is forbidden by the contract
as disguised hierarchy storage.

## Logical scope of negative evidence

The spike witness disproves naive Hilbert/weak-law topologies; the alignment
witness disproves marginal-law and scalar-moment states; (4.1) disproves
matrix elimination without memory.  None rules out a legitimate finite
operator or probability-field state that retains the needed current
alignment.

Moreover, an unrestricted single function or operator field can encode a
countable hierarchy.  Therefore the phrase “not disguised hierarchy” needs
a formal naturality/complexity criterion before a theorem can quantify over
every such field.  Without that criterion, a topology-free universal
impossibility claim is not a well-posed mathematical proposition.

The positive route remains open at exactly two linked gates:

1. propagate weighted uniform integrability for the kernel products from
   iid Gaussian initialization on every compact physical-time interval;
2. construct and identify a fixed Gaussian operator source supporting
   adaptive forward/transpose action and pointwise neuron multiplication,
   without replacing it by the complete traffic-word hierarchy.
