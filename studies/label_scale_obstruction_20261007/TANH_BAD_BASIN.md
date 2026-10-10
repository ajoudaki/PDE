# A both-tanh open bad basin

2026-10-10. Internal continuation of the same study. Complete derivation;
internal audit status is recorded in `TANH_BAD_BASIN_CHECK.md`. Not promoted
material. No simulation or external optimization theorem is used. The construction proves
positive Gaussian failure probability at each fixed width, not a probability
lower bound uniform in width.

## 1. Statement and canonical model

There are fixed data with `d=2`, `m=18`, distinct nonantipodal sphere inputs,
and strictly positive pairwise normalized inner products, together with a
nonzero fixed label vector, for which the following holds. For every `n>=m`,
the bias-free network with both hidden activations equal to tanh has a
nonempty open set of hidden initial parameters, on the exact zero-readout
slice, such that:

- both initial feature matrices have column rank `m`;
- the loss strictly decreases initially;
- both hidden parameter blocks and both feature matrices have nonzero
  initial accelerations (the feature accelerations are entrywise positive);
- all parameters converge to finite limits with strictly positive loss;
- both feature matrices converge to rank-one matrices.

The prescribed Gaussian hidden initialization assigns this set positive
probability at every fixed width. The data, labels and activations are
independent of width. The construction also works for any fixed `m>=18` by
adding data as explained below. It does not assert the same result for every
dataset, every label vector, or smaller sample counts.

Write `xbar_a=x_a/sqrt(d)`, so every `xbar_a` has Euclidean norm one. The
network and loss are
\[
U_{ja}=\tanh(A_{j:}\bar x_a),\qquad
Z=WU,\qquad H=\tanh Z,\qquad
f=H^\top w/n,\qquad \mathcal L=\|f-y\|^2/m.
\]
The parameter shapes are `n by d`, `n by n`, and `n`; the mobilities are
`(n,1,n)`. At initialization the entries are mutually independent with
`A_{jk}(0) ~ N(0,1)` and `W_{ij}(0) ~ N(0,1/n)`, while `w(0)=0`
exactly. The associated metric is
\[
\|\delta\theta\|_{M^{-1}}^2
=\|\delta A\|_F^2/n+\|\delta W\|_F^2+\|\delta w\|^2/n.
\]
The actual gradient flow satisfies
\[
\dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2.
\tag{1}
\]
Smoothness gives local existence and uniqueness. Integrating (1) bounds
parameter displacement on `[s,t]` by
`sqrt((t-s)(L(s)-L(t)))`; therefore no finite-time blowup is possible.

## 2. Nine independent functions and a finite residual construction

For real `t`, define
\[
u=\tanh t,\qquad h=\tanh u,\qquad
\chi=1-u^2,\qquad \psi=1-h^2.
\]
In the following list these are functions of `t`. Consider
\[
\begin{aligned}
F_1&=h,& F_2&=\psi u,& F_3&=\psi\chi t,\\
F_4&=-2h\psi u\chi t,&
F_5&=-2h\psi\chi^2,&
F_6&=-2h\psi\chi^2t^2,\\
F_7&=-2\psi u\chi,&
F_8&=-2\psi u\chi t^2,&
F_9&=-2h\psi u^2.
\end{aligned}
\tag{2}
\]

**Lemma.** These nine real-analytic functions are linearly independent on
every nonempty open real interval.

**Proof.** It suffices to exclude a relation on an interval in `t>0`, because
analytic continuation would extend any interval relation to all real `t`.
Divide a putative relation by the positive function `psi`, remove nonzero
constant factors from individual functions, and use `t=arctanh(u)`,
`0<u<1`. Since `h/psi=sinh(2u)/2`, the resulting list is
\[
\sinh(2u),\quad u,\quad \chi t,\quad hu\chi t,\quad
h\chi^2,\quad h\chi^2t^2,\quad u\chi,\quad
u\chi t^2,\quad hu^2.
\]
A relation therefore has the form
\[
P_2(u)t^2+P_1(u)t+P_0(u)=0,
\]
where the three coefficients are analytic in a neighborhood of `u=1` and
\[
\begin{aligned}
P_2&=c_6h\chi^2+c_8u\chi,\\
P_1&=c_3\chi+c_4hu\chi,\\
P_0&=c_1\sinh(2u)+c_2u+c_5h\chi^2+c_7u\chi+c_9hu^2.
\end{aligned}
\]
The logarithmic singularity of `t=arctanh(u)` forces all three coefficients
to vanish identically. Here is an elementary justification. With `v=1-u`,
write `t=-(log v)/2+(log(2-v))/2`. The displayed relation becomes a degree-two
polynomial in `log v` with analytic coefficients at `v=0`. If any coefficient
is nonzero, divide by the smallest power of `v` occurring in their Taylor
series. A nonzero polynomial in `log v`, with an error
`O(v(1+|log v|^2))`, would then vanish as `v` decreases to zero, which is
impossible. Thus all these analytic coefficients, and hence `P_2,P_1,P_0`,
vanish.

Dividing `P_2=0` by `chi` and taking `u` to one gives `c_8=0`, then `c_6=0`.
Dividing `P_1=0` by `chi` gives `c_3+c_4u tanh(u)=0`; the second function
is nonconstant, so `c_3=c_4=0`.

Multiply `P_0=0` by `cosh(u)`. This is an entire-function identity
\[
c_1\sinh(2u)\cosh u+\sinh u\,P(u)+\cosh u\,Q(u)=0,
\]
where
\[
P(u)=c_5(1-u^2)^2+c_9u^2,\qquad
Q(u)=c_2u+c_7u(1-u^2).
\]
The `exp(3u)` term, or the identity
`sinh(2u)cosh u=(sinh(3u)+sinh u)/2`, first gives `c_1=0` by letting
`u` tend to positive infinity. What remains is
\[
e^u(P+Q)+e^{-u}(Q-P)=0.
\]
Polynomial growth implies `P+Q=0` identically; since `P` is even and `Q`
is odd, both are zero. Comparing their polynomial coefficients gives
`c_5=c_9=c_2=c_7=0`. This proves the lemma.

Choose nine distinct nodes `t_j` in `(3/4,7/8)` so the matrix
\[
B_{kj}=F_k(t_j),\qquad 1\le k,j\le9,
\]
is invertible. Such nodes exist: otherwise all evaluation vectors would
span a proper subspace of `R^9`, producing a nontrivial relation among the
nine functions. They can also be chosen distinct because a newly chosen
evaluation vector must leave the span of the previous ones.

Define eighteen normalized inputs in pairs by
\[
\bar x_{j,\pm}=(t_j,\ \pm\sqrt{1-t_j^2}),\qquad
x_{j,\pm}=\sqrt2\,\bar x_{j,\pm}.
\tag{3}
\]
They are distinct and nonantipodal. Their first coordinates exceed `3/4`,
so their angles to the first coordinate axis have absolute value less than
`arccos(3/4)`; every pairwise inner product is greater than
`2(3/4)^2-1=1/8`.

Solve the finite linear system
\[
B\rho=(0,0,0,0,0,0,2,1,1)^\top
\tag{4}
\]
and define a residual vector by
\[
r_{j,+}=r_{j,-}=\rho_j/2.
\tag{5}
\]
This definition is exact; no numerical solution or experiment is used.
Write `u_a,h_a,chi_a,psi_a` for the functions above at the node of sample
`a`. Pair symmetry and (4) give the following identities:
\[
\begin{gathered}
\sum_a r_ah_a=0,\qquad
\sum_a r_a\psi_au_a=0,\qquad
\sum_a r_a\psi_a\chi_a\bar x_a=0,\\
\sum_a r_a(-2h_a\psi_a)u_a\chi_a\bar x_a=0,\\
\sum_a r_a(-2h_a\psi_a)\chi_a^2\bar x_a\bar x_a^\top=0,\\
\sum_a r_a\psi_a(-2u_a\chi_a)\bar x_a\bar x_a^\top=I_2,\\
\sum_a r_a(-2h_a\psi_a)u_a^2=1.
\end{gathered}
\tag{6}
\]
For clarity, the two diagonal entries of the penultimate identity are
`sum r F_8=1` and `sum r(F_7-F_8)=2-1=1`; its off-diagonal entry cancels
between the paired inputs. The zero matrix on the preceding line uses
`F_6` and `F_5-F_6`. The vector identities use `F_3,F_4`; their second
coordinates cancel in pairs. The last identity guarantees `r!=0`.

Let `h=(h_a)_a` and define fixed unscaled labels
\[
\bar y=h-r.
\tag{7}
\]
The actual labels below are `y=epsilon bar y`, for a sufficiently small
fixed `epsilon>0`, chosen independently of width.

## 3. A finite nonglobal minimum with two nonlinear layers

At every width `n>=m`, put
\[
A_{j:}=p_*^\top=(1,0),\qquad W_{ij}=1/n,
\qquad w_i=\epsilon.
\tag{8}
\]
Both feature matrices have identical rows: their rows are `u^T` and `h^T`.
The predictions and residual are `epsilon h` and `epsilon r`, respectively.
The first three identities in (6) make all three parameter gradients zero.
The loss is
\[
\mathcal L_* = \epsilon^2\|r\|^2/m>0.
\tag{9}
\]

We check every Hessian direction, including neuron splitting. For an
arbitrary parameter variation define
\[
a_j=\delta A_{j:}^\top,\quad
b_i=\sum_j\delta W_{ij},\quad c_i=\delta w_i,
\quad \bar a=\frac1n\sum_ja_j,\quad
\bar b=\frac1n\sum_ib_i,\quad \bar c=\frac1n\sum_ic_i.
\]
The first prediction variation is
\[
\delta f_a=\bar c h_a+
\epsilon\psi_a\bigl(u_a\bar b+
\chi_a\bar x_a^\top\bar a\bigr).
\tag{10}
\]
For verification, the first and second top-preactivation variations are
\[
\begin{aligned}
\delta Z_{ia}&=u_ab_i+\chi_a\bar x_a^\top\bar a,\\
\delta^2Z_{ia}
&=2\chi_a\sum_j\delta W_{ij}\bar x_a^\top a_j
  +\frac{-2u_a\chi_a}{n}\sum_j(\bar x_a^\top a_j)^2.
\end{aligned}
\]
Differentiate the readout and top activation twice. Terms containing a
readout variation disappear after contraction against `r`, by the first
derivative identities in (6). The mixed `delta W,delta A` terms disappear
by `sum r psi chi xbar=0`. The mixed mean `bar a,bar b` terms and the
additional mean-`bar a` quadratic term disappear by the fourth and fifth
identities in (6). The last two identities supply the remaining positive
terms. The exact result, including the mean-loss factor, is
\[
D^2\mathcal L[\delta\theta,\delta\theta]
=\frac2m\left[
\sum_a(\delta f_a)^2+
\frac{\epsilon^2}{n}\sum_i b_i^2+
\frac{\epsilon^2}{n}\sum_j\|a_j\|^2
\right].
\tag{11}
\]
Thus its kernel is exactly
\[
\delta A=0,\qquad \delta W\mathbf1=0,
\qquad \mathbf1^\top\delta w=0.
\tag{12}
\]

These directions are tangent to an actual affine manifold of critical
points, not merely a formal Hessian kernel:
\[
\mathcal M_\epsilon=
\{A_{j:}=p_*^\top\ \forall j,\quad W\mathbf1=\mathbf1,
\quad \mathbf1^\top w/n=\epsilon\}.
\tag{13}
\]
Every point of this manifold has the same features, predictions, residual
and loss as (8). For its first-layer gradient, the potentially different
column coefficients `sum_i w_i W_ij` multiply the same zero vector
`sum_a r_a psi_a chi_a xbar_a`; all other gradients vanish for the same
reason as before. This verifies criticality at every nearby point.

Here is the local attraction argument without invoking a Morse--Bott
theorem. Take affine coordinates whose transverse part is
`xi=(A-A_*, W1-1, mean(w)-epsilon)` and whose other coordinates parametrize
(13). At (8), (11) is positive definite on the transverse coordinates.
Continuity makes the transverse Hessian uniformly positive definite on a
sufficiently small compact coordinate neighborhood. Because the loss is
constant and critical at `xi=0`, Taylor's integral formula gives
\[
c_1\|\xi\|^2\le E:=\mathcal L-\mathcal L_*
\le c_2\|\xi\|^2,\qquad
\|\nabla\mathcal L\|_M\ge c_3\sqrt E.
\tag{14}
\]
Constants here can depend on `epsilon,n`. Combining (1) and (14) gives
exponential decay `E'<=-c_3^2 E` and the path bound
\[
\int_{t_0}^t\|\dot\theta\|_{M^{-1}}ds
\le 2\bigl(\sqrt{E(t_0)}-\sqrt{E(t)}\bigr)/c_3.
\tag{15}
\]
If `E=0`, the trajectory is already stationary. Otherwise (15) follows
by writing speed as `-E'/speed` and applying (14). Start in an inner
neighborhood where this bound is smaller than the distance to the outer
boundary. A first-exit contradiction proves trapping, and (14)--(15)
prove finite total path and convergence to a point of (13).

This proves an open attracting neighborhood of (8) at every fixed width
and fixed positive `epsilon`. Nonglobality is verified in Section 5 by
constructing exact interpolating states.

## 4. Reaching the minimum from exact zero readout

The following step is needed: an open attracting neighborhood at positive
readout does not by itself imply an open bad basin on the zero-readout
slice.

The fully symmetric states
\[
A_{j:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=s
\tag{16}
\]
form an invariant subspace of the actual flow. Their predictions are
\[
f_a=s h_a(p,q),\qquad
h_a(p,q)=\tanh\bigl(q\tanh(p^\top\bar x_a)\bigr).
\]
The restriction of the physical metric to these coordinates is exactly
\[
\|\delta p\|^2+\delta q^2+\delta s^2.
\]
Direct substitution in the parameter equations consequently gives ordinary
gradient flow of the reduced mean loss in `(p,q,s)`, independent of width.
For example, writing the instantaneous residual as `R=f-y`,
`dot W_ij=-(2s/(mn))sum_a R_a psi_a u_a` and
`dot q=n dot W_ij=-(2s/m)sum_a R_a psi_a u_a`, which is the reduced
`q`-gradient equation; here `u,psi` are evaluated at the current `p,q`.
The other two coordinates agree similarly.

Put `s=epsilon b` and `y=epsilon bar y`, and define the fixed reduced
objective
\[
\ell(p,q,b)=\frac1m\sum_a[b h_a(p,q)-\bar y_a]^2.
\]
The exact reduced dynamics become
\[
\dot p=-\epsilon^2\nabla_p\ell,\qquad
\dot q=-\epsilon^2\partial_q\ell,\qquad
\dot b=-\partial_b\ell.
\tag{17}
\]
Restricting (11) at `epsilon=1` to symmetric perturbations shows that
`(p,q,b)=(p_*,1,1)` is an isolated strict local minimum of `ell`, with
positive-definite Hessian
\[
\frac2m\left[
\sum_a\{h_a\delta b+
\psi_a(u_a\delta q+\chi_a\bar x_a^\top\delta p)\}^2
+\delta q^2+\|\delta p\|^2
\right].
\tag{18}
\]
Choose a small closed ball around this point on which the Hessian of
`ell` is uniformly bounded below by a positive constant `lambda`. Its
boundary has a strictly positive loss excess over the center. Choose an
inner sublevel strictly below that boundary minimum.

At `epsilon=0`, the well-defined limiting ODE (17), started at
`p=p_*,q=1,b=0`, keeps `p,q` fixed. Because `h^T r=0`, it has
\[
\dot b=-k(b-1),\qquad
k=2\|h\|^2/m>0,\qquad b(t)=1-e^{-kt}.
\tag{19}
\]
Choose a fixed finite `T` at which (19) lies in the interior of the chosen
inner sublevel. The ODE vector field depends smoothly on `epsilon^2`.
Finite-time continuous dependence therefore puts the state at this same
`T` inside that sublevel for every sufficiently small fixed
`0<epsilon<epsilon_0`. All constants in this step concern the reduced
system and are independent of width.

For each such positive `epsilon`, along (17),
\[
\dot\ell=-\epsilon^2(\|\nabla_p\ell\|^2+|\partial_q\ell|^2)
-|\partial_b\ell|^2
\le-\min(\epsilon^2,1)\|\nabla\ell\|^2.
\]
Loss monotonicity and the boundary barrier prevent exit from the ball.
Strong convexity there gives
`||grad ell||^2>=2 lambda(ell-ell_*)`: apply the strong-convexity inequality
between the current point and the center, then complete the square in
their displacement. Thus the loss excess decays exponentially at a
positive rate for each fixed `epsilon`, and strong convexity forces
convergence to `(p_*,1,1)`.

We have therefore proved that, with a single fixed choice
`0<epsilon<epsilon_0`, the actual symmetric zero-readout trajectory
\[
A_{j:}(0)=p_*^\top,\qquad W_{ij}(0)=1/n,\qquad w(0)=0
\tag{20}
\]
converges to (8), simultaneously as a statement for every `n>=m`.
No width-uniform neighborhood size is asserted.

For each fixed width, this trajectory eventually enters the open attracting
neighborhood established in Section 3. Pull that neighborhood back through
the finite-time continuous flow on the exact slice `w(0)=0`. Its preimage
is a nonempty open set of hidden initializations, containing (20), whose
trajectories converge to (13) with the positive loss (9).

Initial learning is strict on the reference trajectory: (19) gives
`dot s(0)=epsilon k>0`. Its initial loss is
\[
\mathcal L(0)=\epsilon^2(\|h\|^2+\|r\|^2)/m>
\mathcal L_*.
\tag{21}
\]

The hidden layers also start moving at second order; they are not frozen
along this reference trajectory. Define the fixed quantities
\[
P=\sum_a h_a\psi_a\chi_a\bar x_a=(P_1,0),\qquad
Q=\sum_a h_a\psi_a u_a,\qquad
c_\epsilon=\frac{2\epsilon^2k}{m}.
\]
Pair symmetry gives the zero second coordinate of `P`. All nodes are
positive, so `P_1>0` and `Q>0`. At the initial state (20), the exact
reduced equations give
\[
\dot p(0)=0,\qquad \dot q(0)=0,\qquad
\dot s(0)=\epsilon k,\qquad
\ddot p(0)=c_\epsilon P,\qquad
\ddot q(0)=c_\epsilon Q.
\tag{22}
\]
Indeed
`dot p=-(2sq/m)sum_a R_a psi_a chi_a xbar_a` and
`dot q=-(2s/m)sum_a R_a psi_a u_a`, where
`R=s h(p,q)-epsilon bar y`. Differentiate at `s=0,q=1,p=p_*`, and use
`bar y=h-r` and the vanishing first-derivative residual moments in (6).
This proves (22), including its signs and factors. In the original
parameters and feature matrices it reads
\[
\begin{aligned}
\ddot A_{j:}(0)&=c_\epsilon P^\top,&
\ddot W_{ij}(0)&=c_\epsilon Q/n,\\
\ddot U_{ja}(0)&=c_\epsilon\chi_a\bar x_a^\top P>0,&
\ddot Z_{ia}(0)&=c_\epsilon(u_aQ+\chi_a\bar x_a^\top P)>0,\\
\ddot H_{ia}(0)&=c_\epsilon\psi_a
                 (u_aQ+\chi_a\bar x_a^\top P)>0.
\end{aligned}
\tag{23}
\]
For the eighteen paired inputs, `xbar_a^T P=t_a P_1>0`. All first time
derivatives of `A,W,U,Z,H` vanish at initialization, because the readout
is zero. Formula (23) proves nonzero accelerations of both hidden blocks
and entrywise positive accelerations of both feature matrices. These
strict properties persist on a sufficiently small hidden neighborhood
of (20), by smooth dependence of the initial acceleration on the hidden
initial parameters. Shrink the open zero-readout bad basin to that
neighborhood before taking the full-rank intersection below.

## 5. Full-rank initial features, nonglobality, and Gaussian probability

For any distinct nonantipodal finite unit inputs, the functions
`a -> tanh(a^T xbar_j)` are linearly independent. To prove this, choose a
direction `a_0` for which the projections `s_j=a_0^T xbar_j` are nonzero
and have pairwise different absolute values. Such a direction exists by
avoiding the finitely many proper hyperplanes determined by
`xbar_i` and `xbar_i +/- xbar_j`.

Suppose `sum_j c_j tanh(t s_j)=0` for all real `t`. Absorb the signs of
`s_j` into the coefficients and write `0<b_1<...<b_m` for their absolute
values. Letting `t` tend to infinity gives `sum_j c_j=0`. Subtract this
constant relation and multiply by `exp(2b_1t)`. Since
`tanh(bt)-1=-2 exp(-2bt)(1+o(1))`, the limit gives `c_1=0`. Repeat with
the remaining coefficients to get all `c_j=0`.

It follows that there are `m` first-layer rows whose feature vectors span
`R^m`; pad with rows if `n>m`. Thus a first-layer matrix `U` of column
rank `m` is realizable. Choose `W` so the first `m` rows of `WU` equal
`delta I_m`, with `delta!=0`, and all remaining rows zero. The resulting
`H` has an invertible diagonal first block. This gives a hidden state where
both feature matrices have column rank `m`.

The product
\[
P(A,W)=\det(U^\top U/n)\det(H^\top H/n)
\]
is real analytic on the connected Euclidean hidden parameter space and is
not identically zero by the preceding realization. It cannot vanish on
an open set: a real-analytic function vanishing on an open ball vanishes
along every line through that ball by the one-variable analytic identity
principle, hence everywhere. Therefore `P!=0` is dense as well as open.

Intersect this dense open set with the open zero-readout bad basin from
Section 4. The intersection is nonempty and open. Both initial feature
Grams are positive definite there. At zero readout the full tangent Gram
is exactly `G=H^T H/n`, so
\[
\dot{\mathcal L}(0)=-\frac4{m^2}y^\top G(0)y<0.
\]
At the limiting critical manifold both feature matrices have rank one.
Thus this is actual asymptotic feature-rank collapse from full-rank starts,
not an isolated invariant trajectory offered as a basin.

The minima are nonglobal. At any full-rank hidden realization, solve the
linear readout equations `H^T w/n=y`; a solution exists and gives zero
loss. In particular, the same hidden states used to establish analytic
nondegeneracy provide exact interpolating parameters.

The Gaussian law of all hidden entries has a strictly positive density
everywhere at fixed width. Every nonempty open hidden set therefore has
strictly positive probability, including this bad basin. The exact
zero-readout initialization is already built into the basin statement.

The population initialization also has a positive top-feature gap. The
linear-independence argument above implies that, for a standard Gaussian
vector `g` in `R^2`,
\[
Q^{(1)}_{ab}=\mathbb E[\tanh(g^\top\bar x_a)\tanh(g^\top\bar x_b)]
\]
is positive definite. Indeed any nonzero linear combination is a nonzero
continuous function of `g`, so its squared expectation is positive under
the everywhere-positive Gaussian density. Consequently
`Z~N(0,Q^(1))` has full support in `R^m`. For any nonzero vector `c`, the
function `c^T tanh(Z)` is nonzero on an open set (use a sufficiently small
multiple of `c`), proving positive definiteness of
`Q^(2)=E[tanh(Z)tanh(Z)^T]`. These are the population covariances for the
stipulated Gaussian scaling. The resulting positive gaps are independent
of width but are not quantified here.

## 6. Extensions and limits of the claim

For any fixed `m>18`, add distinct nonantipodal inputs in the same positive
correlation cone and set their residual entries to zero and their unscaled
labels to `h_a`. All identities (6) remain unchanged. The squared-Jacobian
part of the Hessian only acquires nonnegative terms, so the proof applies
with the new mean-loss normalization and a possibly different
width-independent `epsilon_0`. Although the enlarged `P` need not have
zero second coordinate, the acceleration signs also persist: every
`h_a psi_a chi_a` is positive and every pairwise normalized inner product
is positive, so `xbar_a^T P>0` for each sample.

This yields a fixed dataset and a fixed nonzero label vector for each
`m>=18`, valid for every `n>=m`, with positive Gaussian non-fitting
probability at each fixed width. The probabilities may tend to zero as
width grows. The proof therefore does not refute sufficiently-large-width
high-probability fitting, establish an incompressibility result, or identify
a typical Gaussian failure mechanism. The labels are deliberately
constructed from a finite linear system; no claim is made for generic
labels or for arbitrary sample counts below eighteen.

All sources for this derivation are the explicit canonical model, the
displayed finite construction and the derivations above. It uses no
unpromoted scientific input from another study and no external optimization
theorem. Internal audit status is recorded in `TANH_BAD_BASIN_CHECK.md`.
This is not promoted material.
