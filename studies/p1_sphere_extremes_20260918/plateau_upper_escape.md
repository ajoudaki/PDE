# Discrete plateau levels or escape of the upper parameters

Status: analytic candidate derived by the lead author, 2026-09-18. This is
a necessary condition for positive limiting loss, not a configuration-only
classification or a sufficient condition for initialized failure.

Scientific inputs: complete `docs/observable_p1.md`, the fixed-order
population equations/existence/energy in `docs/global_nonlinear.md`
C.4.7.9.3--4 and C.4.7.10.D.3, and the full three-feature independence
proof in this study's `terminal_geometry.md`. The argument was developed
in the same continuation as the finite critical-state routes, with their
reported signed-partition observation available before this file was
frozen. No other study or empirical input is used.

## Statement and scope

Use the canonical full p=1 initialized population flow on three sphere
inputs in dimension three, with binary labels, positive weights p_i
summing to one, the actual moving matrix transpose, and unhalved physical
square loss. Write L_infinity=lim_(t->infinity)L(t), which exists by
energy monotonicity, and p_min=min_i p_i. Repeated or antipodal inputs
are allowed. No strong endpoint or bound on w-g is assumed for large time.

Define the following finite set, allowing repetitions of its values:

\[
 \begin{split}
 \mathcal V(p)=\{&0,1,\ p_i,\ p_i+p_j,\
 &4p_ip_j/(p_i+p_j),\
 &p_k+4p_ip_j/(p_i+p_j),\
 &4p_i(1-p_i):\ i,j,k\text{ distinct when present}\}.
 \end{split}                                           \tag{1}
\]

If there is any sequence t_n tending to infinity on which both
||c(t_n)||_2 and ||M(t_n)||_F are bounded, then

\[
                         L_\infty\in\mathcal V(p).       \tag{2}
\]

Consequently, if L_infinity is outside this finite set, necessarily

\[
             \|c(t)\|_2+\|M(t)\|_F\longrightarrow\infty.
                                                               \tag{3}
\]

Every positive member of V(p) is at least p_min. In particular, a plateau
strictly between zero and p_min forces (3). For equal weights, any
nonstationary trajectory with a bounded sequence of upper parameters and
positive limiting loss must have

\[
                  L_\infty\in\{1/3,2/3,8/9\}.          \tag{4}
\]

These are necessary levels, not assertions that each level is reachable.
The theorem is stronger than a finite-endpoint necessary condition: it
uses neither compactness of population fields nor convergence of w or c.
It also makes no uniform lower bound on the actual evolving feature Gram.

## 1. Small readout velocity at every bounded-upper-parameter sequence

Use unit directions u_i=x_i/sqrt(3), and write

  a_i=E_1[b_1 phi(w.u_i)], v_i=Ma_i,
  H_i=phi(b_2.v_i), f_i=E_2[cH_i], r_i=f_i-y_i.

Ridge normalization makes both feature synthesis maps contractions.
Thus |a_i|<=1, ||d_i||<=||c||_2, and the full equations imply

\[
 \|c'\|_2\le2,\quad \|M'\|_F\le2C,\quad
 \|w'\|_2\le2BC,
 \qquad C=\|c\|_2,\quad B=\|M\|_F,                     \tag{5}
\]

where sum_i p_i|r_i|<=sqrt(L)<=1 was used. In the lower bound,
||b_1^T M^T d_i||_2<=B C and the lower gates are at most one.
Differentiating the exact feature contractions gives

\[
 |a_i'|\le\|w'\|_2,
 \quad |v_i'|\le2C(1+B^2),
 \quad\|H_i'\|_2\le2C(1+B^2),
 \quad |f_i'|\le2+2C^2(1+B^2).                           \tag{6}
\]

Every differentiation is justified along each finite-time bounded
characteristic solution; the resulting constants depend only on B,C,
not on the size of w-g. The readout equation is
c'=-2 sum_i p_i r_i H_i. Therefore

\[
 \|c''\|_2\le
 4+4C^2(1+B^2)+4C(1+B^2).                                \tag{7}
\]

Suppose B(t_n),C(t_n)<=R. On the following unit interval, (5) gives
C<=R+2 and B<=R+2(R+2), so (7) has a common finite upper bound Q_R.
If a subsequence had ||c'(t_n)||_2>=epsilon>0, then for
delta=min(1,epsilon/(2Q_R)) its following delta interval would have
||c'(t)||_2>=epsilon/2. Select infinitely many disjoint such intervals.
They contradict the exact finite dissipation budget

  integral_0^infinity ||c'(t)||_2^2 dt <=1.

Hence every such bounded sequence satisfies

\[
                         \|c'(t_n)\|_2\longrightarrow0. \tag{8}
\]

This uses forward local bounds only. It does not infer that all other
gradient blocks vanish at these times or that the trajectory is compact.

## 2. Finite coefficient compactness suffices

Since |a_i|<=1 and M(t_n) is bounded, the finitely many v_i(t_n) admit
a convergent subsequence, say v_i(t_n)->v_i^*. The predictions are also
bounded, because p_i r_i^2<=L<=1; choose the same subsequence so
f_i(t_n)->f_i^*. Bounded marks and the Lipschitz activation give strong
upper L2 convergence H_i(t_n)->H_i^*=phi(b_2.v_i^*).
Equation (8) then yields

\[
               \sum_i p_i(f_i^*-y_i)H_i^*=0.             \tag{9}
\]

The bounded readout norms enforce the correct prediction relations at
every limiting feature collision. If v_i^*=0, then
|f_i(t_n)|<=R||H_i(t_n)||_2 tends to zero. If
v_i^*=sigma_i v_G^* within a nonzero signed-equality group, then

  |f_i(t_n)-sigma_i f_G(t_n)|
     <=R||H_i(t_n)-sigma_i H_G(t_n)||_2 ->0.

Thus f_i^*=0 at zero vectors and f_i^*=sigma_i F_G in each nonzero
group. No weak compactness argument for c is required. The upper tanh
features of distinct nonzero vectors modulo sign are independent for
at most three representatives, by the positive-density and Vandermonde
proof in terminal_geometry.md. Therefore (9) implies

\[
 F_G=\frac{\sum_{i\in G}p_i\sigma_i y_i}{W_G},
 \qquad W_G=\sum_{i\in G}p_i.                            \tag{10}
\]

Passing the finite sum defining the loss to the limit gives

\[
 L_\infty=\sum_{i:v_i^*=0}p_i+
 \sum_G\left[W_G-
       \frac{(\sum_{i\in G}p_i\sigma_i y_i)^2}{W_G}\right].
                                                               \tag{11}
\]

This is the same signed-partition list that appears at a finite critical
state, now obtained without a full-state endpoint.

## 3. Enumeration, gap and the escape conclusion

If all three effective vectors are zero, (11) is one. If exactly two
are zero, it is p_i+p_j. If exactly one is zero, the other two either
give independent/compatible features and contribute zero, or form one
mixed-sign group contributing 4p_ip_j/(p_i+p_j). These give the one-zero
values in (1). With no zero vectors, distinct groups give zero unless
one two-member group is mixed, producing 4p_ip_j/(p_i+p_j), or all three
are in one mixed group. In the last case one oriented sign is a singleton
of weight p_i, giving 4p_i(1-p_i). This exhausts (1).

A nonzero zero-vector contribution is at least p_min. A mixed group
contributes 4ab/(a+b)>=2 min(a,b)>=2 p_min, because each of its two
signs has at least one active input. This proves the gap. Substitution
p_i=1/3 gives V(p)={0,1/3,2/3,8/9,1}. A nonstationary initialized
trajectory has L_infinity<1 by strict initial descent and monotonicity,
which gives (4).

If (3) failed, some sequence t_n tending to infinity would have the
sum of the two nonnegative norms bounded. Both norms would then be
bounded, and (2) would follow by Sections 1--2. This contraposition
proves (3) whenever the limiting loss is outside V(p).

## What is not established

No compatible initialized plateau, bounded or escaping, is constructed.
The finite list does not determine which inputs reach which levels. An
escaping trajectory might also have a loss in the list. A bounded full
state is not inferred from bounded c and M, and neither bound is asserted
for all initialized trajectories. The theorem narrows possible failure
mechanisms without replacing the missing configuration-only iff result.
