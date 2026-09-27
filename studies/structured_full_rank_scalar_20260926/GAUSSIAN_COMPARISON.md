# What signed fast transforms do and do not approximate

Root derivation, 2026-09-26. These propositions compare initialized operators.
They are not impossibility theorems for scalar approximations to training.
No experiment or external probability theorem is used.

## 1. A repeated-action separation

Let A_n be any real orthogonal n by n matrix, including D1 H D2 H D3 with
normalized H and sign diagonals. Let G_n have independent N(0,1/n) entries.
For any deterministic vector v_n with Euclidean norm sqrt(n), define

\[
J(M,v)=\frac1n\|(M^\top M-I)v\|_2^2.
\]

Then J(A_n,v_n)=0 exactly, whereas

\[
J(G_n,v_n)\longrightarrow1
\quad\hbox{in probability}.
\tag{1}
\]

### Proof

Orthogonality proves the first assertion. The Gaussian law is invariant under
deterministic rotations of its columns: each row has covariance I/n, and
orthogonal rotation preserves its multivariate Gaussian density. Thus it
suffices to replace v_n/sqrt(n) by the first coordinate vector e_1.

Let g be the first column of G and set U=n||g||^2. Conditional on g, the
n-1 off-diagonal entries of G^T G e_1 are independent centered Gaussians
with variance ||g||^2/n; its first entry is ||g||^2. Consequently

\[
\|(G^\top G-I)e_1\|^2
=\left(\frac Un-1\right)^2+\frac Un\frac Vn,
\tag{2}
\]

in distribution, where U is a sum of n independent squared standard
Gaussians and V is an independent sum of n-1 such squares.
The elementary Gaussian moments E Z^2=1 and E Z^4=3 give

\[
EU=n,\quad \operatorname{Var}(U)=2n,\qquad
EV=n-1,\quad \operatorname{Var}(V)=2(n-1).
\]

Chebyshev's inequality yields U/n->1 and V/n->1 in probability.
Equation (2) proves (1). In fact EJ(G_n,v_n)=1+1/n.
The exceptional finite case n=1 causes no issue; take V=0.

This is a scalar statistic of two successive actions of one initialized
matrix. It separates the models even though individual entries or selected
one-step projections of a fast transform may look Gaussian.

It does NOT imply that every selected neural output differs by order one:
an observable-transfer argument is needed for that claim. It does mean that
an approximation theorem preserving arbitrary reused Gaussian actions cannot
hold for the all-sign orthogonal candidate.

## 2. The special fixed-rank perturbation approaches identity

Let J be a set of r Hadamard columns, with r fixed independently of n, and
put

\[
Q=H D H=I-2\sum_{j\in J}h_jh_j^\top,
\tag{3}
\]

where D has negative signs exactly in J. The columns h_j are orthonormal,
so Q is full rank and orthogonal. Its deviation from identity satisfies

\[
\frac1n\|Q-I\|_F^2=\frac{4r}{n}.
\tag{4}
\]

If v has independent centered entries of variance sigma^2, independently of
the choice of J, then

\[
E\left[\frac1n\|(Q-I)v\|^2\,\middle|\,Q\right]
=\frac{4\sigma^2r}{n}.
\tag{5}
\]

Proof: write the left side as n^{-1} E[v^T(Q-I)^T(Q-I)v]
and use E[vv^T]=sigma^2 I and (4).

For bounded iid entries, n^{-1}||v||^2->sigma^2 in probability. By
Cauchy--Schwarz and (5),

\[
\frac1n v^\top Qv\longrightarrow\sigma^2.
\tag{6}
\]

By contrast, let G be independent of v. Conditional on v,

\[
E\left[\frac1n v^\top Gv\,\middle|\,v\right]=0,\qquad
\operatorname{Var}\left(\frac1n v^\top Gv\,\middle|\,v\right)
=\frac{\|v\|^4}{n^3}.
\]

Thus the corresponding Gaussian pairing tends to zero. This applies, for
example, to the first-layer tanh response on a fixed nonzero input, whose
coordinates under Gaussian first weights are iid bounded and centered.

The fixed-r construction is therefore not a faithful Gaussian mixing proxy
in this basic joint input/output statistic. Its compressibility must not be
advertised as a resolution for independent central signs or iid Gaussian
initialized mixing.

Endpoint sign diagonals independent of the Gaussian outer weights can be
absorbed into neuron coordinates in the two-hidden tanh network, with the
corresponding change of those outer weights; this preserves their law.
That equivalence does not
repair the contrast between the central fixed-r construction and Gaussian
mixing.

## 3. Meaning for the proof target

Three properties must be kept separate:

1. full rank and inexpensive forward/transpose application;
2. approximation of a specified collection of Gaussian initialization or
   reuse statistics;
3. a width-uniform, autonomous, finite-scalar training approximation.

The signed candidate has property 1. It fails property 2 for the explicit
reuse statistic in (1). Property 3 is a separate mathematical question and
is neither disproved nor established by that separation.

The fixed-r member permits local-plus-finitely-many-averages descriptions,
but (5)--(6) show why choosing it silently would substantially weaken the
request for a Gaussian-like full-rank candidate.
