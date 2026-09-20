# Compatible triples: exact symmetry obstruction and a surviving weighted candidate

Status: independent analytic route, frozen on 2026-09-18 before communicating
with the other current routes. No experiment, quadrature, finite population
replacement, diagonal truncation, or changed initialization is used. These
are internally derived claims, not independently reviewed or promoted theory.

Scientific inputs read completely were `docs/observable_p1.md` and this
study's `plateau_construction.md`, `architectural_loss_floor.md`,
`initialization_positivity.md`, and `cyclic_uniformity.md`. The model and
existence portions of `docs/global_nonlinear.md` C.4.7.9.3--4 and
C.4.7.10.D.3 were also read. No other study, route, review, history, or
scientific source was read. The rigorous-mathematics and
conjecture-investigation skills and the latter's research-contract and
adversarial-audit references were read.

## Result

No compatible initialized positive-loss plateau is proved here. The route
does rigorously eliminate the entire mechanism in which a transitive
signed-coordinate symmetry traps the three examples at the same imperfect
prediction: every such canonical trajectory reaches a bounded exact fit,
with an exponential loss bound. For three distinct folded examples the
rate can be bounded uniformly over all these symmetric geometries.

A broader exact statement removes a related expressivity explanation:
for every compatible weighted triple, the sector fixed by every data
symmetry inherited from signed coordinate permutations contains an exact
fit with the initial hidden state unchanged. Thus these symmetries cannot
force a positive architectural floor inside the initialized invariant
sector. This statement alone does not rule out a stationary saddle or
escape to infinity inside that sector.

A weighted reflection-symmetric isosceles family remains a concrete
candidate. Its full dynamics has two residuals rather than one. The
terminal feature collisions required for a bounded positive-loss endpoint
are identified below; their initialized reachability remains unproved.

## 1. Contract, folding, and canonical symmetries

Write `u_i=x_i/sqrt(3)`, so `u_i` is unit, and let positive weights `p_i`
sum to one. Labels are `y_i in {+1,-1}`. Keep the exact joint Gaussian
marks, ridge `eta=1/4096`, initial state `w=g,c=0,M=D`, physical unhalved
loss, and all three full gradient equations of the source. In the exact
odd-mark invariant representation, `b_1 in R^6`, `b_2 in R^3`, and
`M in R^(3 by 6)`. The omitted constant row and column have zero velocity
in the original equations, as proved in the source.

For every state the prediction is odd in its input. Therefore setting

\[
 v_i=y_i u_i
\]

gives the exact identity of loss functions, hence of full gradients,

\[
 \mathcal L(\theta)=\sum_i p_i(f_\theta(v_i)-1)^2.                 \tag{1}
\]

Combine equal `v_i` and add their weights. Compatibility means precisely
that this folded support contains no antipodal pair. There are at most
three distinct folded points. All subsequent equations still describe
the original physical flow, including when the original labels were
mixed.

Let `R` be a signed permutation matrix in dimension three, and put
`R_1=diag(R,R)`. Transform the lower independent Gaussian coordinate
pairs and the upper Gaussian coordinates by `R`; denote these
measure-preserving mark maps by `T_R`. The initialized coefficients obey

\[
 b_1\circ T_R=R_1b_1,\quad g\circ T_R=Rg,\quad
 b_2\circ T_R=Rb_2,\quad RDR_1^T=D.                            \tag{2}
\]

The positive coordinate-diagonal bands of `D`, including their full
reverse response and ridge normalization, are unchanged. Define the
state isometry

\[
 U_R\theta=
 \bigl(R(w\circ T_R^{-1}),\ c\circ T_R^{-1},\ RMR_1^T\bigr).
                                                                    \tag{3}
\]

Changing variables separately in the two population integrals gives

\[
 a_{U_R\theta}(u)=R_1a_\theta(R^{-1}u),\qquad
 f_{U_R\theta}(u)=f_\theta(R^{-1}u).                          \tag{4}
\]

Let `G` be any subgroup preserving the weighted folded data measure.
Equations (1)--(4) show that its state action preserves the loss and the
initial state. The population `L2` and matrix Frobenius metrics are
preserved as well. Thus the full gradient field is equivariant.
Uniqueness from the bounded-feature existence argument proves

\[
 U_R\theta(t)=\theta(t),\qquad f_t(Rv)=f_t(v)\quad(R\in G).     \tag{5}
\]

This reasoning does not impose a new matrix constraint: any vanishing
entries follow from the original full vector field and uniqueness.

## 2. The symmetry-fixed sector always contains an exact fit

**Proposition.** For any compatible weighted triple and any such group
`G`, there is a bounded fitting readout `c_*`, with `w=g,M=D`, for which
`(g,c_*,D)` is fixed by every `U_R`, `R in G`.

To prove it, list the distinct folded points as `v_1,...,v_m`, `m<=3`,
and put

\[
 z_i=Da_0(v_i),\qquad H_i(B)=\tanh(B^Tz_i),\qquad
 K_{ij}=E_2[H_i(b_2)H_j(b_2)].                              \tag{6}
\]

The initialization result in `architectural_loss_floor.md` gives
`z_i!=0`, and `z_i=+/-z_j` only if `v_i=+/-v_j`. Thus these `z_i` are
distinct modulo sign. For completeness the required independence has
the following short proof. The upper mark law has positive density on
an open cube about zero. An almost-sure linear relation among the
continuous `H_i` holds throughout this cube. Choose a vector `e` such
that the numbers `e.z_i` are nonzero with distinct squares, excluding
the finitely many hyperplanes defined by `z_i` and `z_i+/-z_j`.
Restrict the relation to `B=te` for small `t`. The coefficients of
`t,t^3,t^5` that are needed for `m<=3` are nonzero in the Taylor series
of tanh. The resulting Vandermonde system forces every coefficient of
the relation to vanish. Hence `K` is positive definite.

Set

\[
 \alpha=K^{-1}{\bf1},\qquad c_*(B)=\sum_i\alpha_iH_i(B).      \tag{7}
\]

This readout is bounded and gives prediction one at every folded point.
It is odd under global mark negation. If `R` permutes these points,
then `z(Rv)=Rz(v)` by (2). The corresponding permutation preserves
`K` and `1`, so it preserves `alpha`. Reindexing (7) proves
`c_*(R^{-1}B)=c_*(B)`. Together with (2), this proves the proposition.

Consequently there is no positive loss floor caused solely by staying
in the canonical signed-coordinate symmetry sector. This is an
existence statement about that sector, not an assertion that the moving
hidden trajectory remains well conditioned or selects (7).

## 3. Every transitive case fits along the actual full flow

Assume `G` acts transitively on the distinct folded points. Their
aggregated weights are then equal. Let

\[
 F(\theta)=\frac1m\sum_{i=1}^m f_\theta(v_i),\qquad
 m_\theta(B)=\frac1m\sum_{i=1}^m H_{\theta,i}(B),\qquad
 k=\|m_{\theta(0)}\|_2^2>0.                                \tag{8}
\]

Positivity follows from the independence just proved (and is immediate
for `m=1`). Consider the full-state ascent equation

\[
 \theta_s=\nabla F(\theta),\qquad\theta(0)=(g,0,D).          \tag{9}
\]

It preserves all the symmetries, so every training prediction equals
`F` along this curve. This is a gradient equation for all `w,c,M`, not
a frozen-feature surrogate. Write `L_j=ess sup|b_j|`, `A=L_1L_2`,
and `D_0=||D||_F`. Its exact readout, matrix, and lower velocities give

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|_F\le D_0+As^2/2,\quad
 \|w(s)-g\|_\infty\le AD_0s^2/2+A^2s^4/8.                  \tag{10}
\]

Indeed `|m_theta|<=1`, `|a_i|<=L_1`, and
`|d_i|<=L_2||c||_infty`; substituting these bounds successively proves
(10). Local Lipschitz continuity on bounded sets and these finite-clock
bounds give unique continuation for every finite `s`, exactly as in
the allowed existence source.

Put `C=||c||_2^2` and `kappa=||grad F||^2`. The readout part of the
gradient and Cauchy--Schwarz yield

\[
 c_s=m_\theta,\quad C_s=2F,\quad F_s=\kappa\ge\|m_\theta\|_2^2,
 \quad F^2\le C\|m_\theta\|_2^2.                           \tag{11}
\]

At zero, `F=ks+o(s)` and `C=ks^2+o(s^2)`, because both hidden
gradients vanish when `c=0`. For `s>0`, `F,C>0`, and

\[
 \left(F^2/C\right)_s
 =\frac{2F}{C^2}(C\kappa-F^2)\ge0.
\]

Therefore `kappa>=F^2/C>=k`, and `F(s)>=ks`. There is a unique
finite `s_*<=1/k` at which `F(s_*)=1`. Define the physical clock by

\[
 s_t=2(1-F(s)),\qquad s(0)=0.                              \tag{12}
\]

Below `s_*` its speed is positive. Local scalar uniqueness prevents
finite-time arrival at the equilibrium `s_*`; monotonicity shows
`s(t)->s_*`, since any smaller limit would retain positive speed.
Because the training predictions coincide, the original loss gradient
is exactly `-2(1-F) grad F` on this curve. Thus (12) identifies it with
the canonical full physical flow. In particular

\[
 \mathcal L(t)=(1-F(s(t)))^2\le e^{-4kt},\qquad
 \theta(t)\longrightarrow\theta(s_*).                      \tag{13}
\]

The limiting state is bounded in the norms of (10), and fits exactly.
This excludes a plateau, including one attributed to saturation or
hidden feature collisions, for every transitive case covered here.

For three distinct folded points these cases are exactly signed
coordinate conjugates of canonical cyclic orbits. Here are the group
details. The induced permutation group is a transitive subgroup of
`S_3`; its order is divisible by three, and inspecting the possibilities
in `S_3` shows it contains a three-cycle. Choose a signed permutation
`R` inducing it. If the underlying coordinate permutation were the
identity or a transposition, `R` would have order dividing two or four,
which is impossible. Its underlying permutation is therefore a
three-cycle. The product of its three signs must be positive: otherwise
`R^3=-I`, whereas cycling the three nonzero points gives `R^3v_i=v_i`.
A diagonal sign matrix `S` consequently conjugates `R` to the ordinary
coordinate cycle `P` or `P^2`. Thus the support is
`S{v,Pv,P^2v}` for some unit `v`.

The exact law of the marks is invariant under `S`. Hence the constant
`k` is the same initialized average-feature norm as in
`cyclic_uniformity.md`, after this sign change. That source's compact
sphere argument supplies one `k_*>0` for all these triples, including
their compatible collapsed limits. Equations (10)--(13) then hold with
uniform fitting-clock and state bounds. No arbitrary spatial rotation
has been used or asserted.

## 4. A concrete weighted two-orbit candidate and its exact remaining gap

For `0<a<1` let `b=sqrt(1-a^2)` and consider the folded directions

\[
 v_+=(a,b,0),\qquad v_-=(a,-b,0),\qquad v_0=(-1,0,0),
 \qquad p_+=p_-=p>0,\quad p_0=q=1-2p>0.                  \tag{14}
\]

They are three distinct non-antipodal unit points, hence compatible and
already exactly fit by (7). Setting `q=2pa`, equivalently
`p=1/[2(1+a)]`, makes their weighted first moment zero. This cancels
only a linear feature; their exact initialized upper features are
independent and their initial loss derivative is strictly negative.
If mixed original labels are required, for example choose
`y_+=y_-=+1,y_0=-1` and raw inputs `x_i=sqrt(3)y_i v_i`.
Those three raw inputs are still distinct and non-antipodal, and (1)
keeps every equation unchanged.

Reflection of coordinate two exchanges the pair and fixes `v_0`;
reflection of coordinate three fixes all points. These exact canonical
symmetries imply that along the full trajectory

\[
 z_+=Ma(v_+)=(A,B,0),\quad
 z_-=Ma(v_-)=(A,-B,0),\quad
 z_0=Ma(v_0)=(-C,0,0).                                    \tag{15}
\]

Here `A(0)=T(a)>0`, `B(0)=T(b)>0`, and `C(0)=T(1)>0`.
The readout is even in upper mark coordinates two and three; its
global oddness makes it odd in coordinate one. These parities can
reduce entries of `M` through invariance of the original equations,
but do not freeze the trainable nonzero bands.

Define `F=(f(v_+)+f(v_-))/2`, `G=f(v_0)`. On the invariant curve
`f(v_+)=f(v_-)=F`, and the physical equation is exactly

\[
 \theta_t=4p(1-F)\nabla F+2q(1-G)\nabla G,
 \qquad \mathcal L=2p(1-F)^2+q(1-G)^2.                    \tag{16}
\]

The gradients in (16) are full-state gradients. There is no common
scalar clock unless a further relation between the two residuals is
proved. At initialization their readout gradients are independent,
since a relation between `(H_++H_-)/2` and `H_0` would contradict
the three-feature independence in Section 2. The scalar monotonicity
argument (11) therefore does not extend merely by replacing `F` with
its weighted average: `C_t` then pairs `c` with two independently
changing residual coefficients.

There is also a precise test for any proposed bounded terminal state.
If the full state converges in the bounded-increment/readout/matrix
norms, continuity of the autonomous vector field forces its limiting
velocity to vanish. To see this last implication, a nonzero limiting
velocity would have a positive scalar pairing with some continuous
linear functional; that pairing would remain positive at late times,
contradicting convergence of the state. In particular readout
stationarity gives

\[
 p(F-1)(H_++H_-)+q(G-1)H_0=0.                             \tag{17}
\]

If `A,B,C` are all nonzero, the three vectors in (15) are nonzero
and distinct modulo sign. Their upper features are independent by
the same elementary argument as before. Equation (17) then forces
`F=G=1`. Therefore a bounded positive-loss limit requires at least
one of `A,B,C` to vanish. More specifically, if `B=0` but `A,C!=0`,
the two distinct upper features remain independent whenever
`A!=+/-C`, again forcing a fit. If `A=-C`, all three features coincide
and equal targets still force a fit. Thus in this stratum a positive
limit requires

\[
 B=0,\qquad A=C\ne0,                                    \tag{18}
\]

which makes the pair's upper feature exactly the negative of the
singleton's. In the other strata, `A=0` makes the pair's upper
features antipodal and their symmetric prediction zero; `C=0` makes
the singleton's upper feature zero. These are necessary descriptions,
not assertions of stationarity of the other gradient blocks.

The readout equation also fixes the possible endpoint losses in the
nontrivial cases. In (18), `G=-F`, and (17) gives
`F=2p-q`, hence `L=8pq`. If `A=0,C!=0`, the pair prediction is zero
and its summed upper feature vanishes, so (17) forces `G=1` and
`L=2p`. If `C=0,A!=0`, the averaged pair feature is nonzero (evaluate
at upper coordinate two equal to zero), so (17) forces `F=1` and
`L=q`. If `A=C=0`, all three predictions vanish by these parities
and `L=1`; strict initial descent excludes that value for the
canonical limiting loss. Thus any bounded positive-loss endpoint of
(14) must have loss in `{q,2p,8pq}`. This finite list is a necessary
condition, not a construction of any endpoint.

The unsolved obligations for (14) are consequently concrete: prove
or disprove canonical approach to (18), to a zero-feature stratum,
or to an unbounded saturation regime. Initial positivity establishes
none of their reachability or exclusion. Conversely, an arbitrary
stationary state on such a stratum would not prove initialized
convergence to it. The readout fitting construction in Section 2
would not by itself rule that convergence out.

## Claim audit and boundary

- Proved: folding preserves the entire full physical flow; all
  canonical signed-permutation data symmetries are inherited by it.
- Proved: their invariant sector contains a bounded exact fit for
  every compatible weighted triple, with initial hidden coordinates.
- Proved: every transitive such symmetry yields a bounded fitted
  endpoint and exponential physical loss decay. For three folded
  points this exhausts signed-conjugate cyclic orbits and gives a
  uniform rate over that family.
- Proved: the weighted reflection family (14) is compatible, starts
  learning strictly, has the exact two-residual equation (16), and
  any bounded positive-loss endpoint must satisfy the feature
  degeneracies identified above.
- Open: an initialized positive-loss limiting trajectory for (14)
  or another compatible law; arbitrary unequal geometry; whether
  bounded convergence itself holds for those cases.
- Not inferred: arbitrary rotation invariance, persistent feature
  rank from initial rank, all-time compactness from finite-time
  bounds, or selection of the available fixed-feature readout fit.
