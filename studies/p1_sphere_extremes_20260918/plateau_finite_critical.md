# Finite critical states and the remaining initialized plateau gap

Status: internally proved candidate, frozen on 2026-09-18 before route
comparison. After cross-audit, two wording clarifications explicitly
retain the independent-input nullspace scope and distinguish finite
accumulation points from whole-trajectory distance convergence. No proof
or inequality changed. No experiment was run. This is not promoted material.

Scientific input scope: all of `docs/observable_p1.md`,
`terminal_geometry.md`, `architectural_loss_floor.md`, and
`initialization_positivity.md`; the complete equations/existence sections
C.4.7.9.3–4 and the state/equations/existence portion of C.4.7.10.D.3 in
`docs/global_nonlinear.md`. Required research and rigorous-math skills and
their research-contract/adversarial-audit references were read. No other
study or current-route report was used. A later supervisor message proposed
a nonzero-middle critical-state example; it was not used in this report.

## 1. Contract and strongest conclusion

The model is the exact canonical dimension-three, order-one population
closure, with the correlated Gaussian-derived marks, ridge `eta=1/4096`,
initialization `w=g,c=0,M=D`, the actual transpose of the full evolving
middle matrix, all trained blocks, and unhalved weighted square loss.
There is no population quadrature, time discretization, or width limit.
Weights are positive after inactive atoms are discarded. Inputs are unit
normalized directions; labels are `+1` or `-1`.

Work in the exact initialized odd sector. Its inactive constant features
are removed, leaving `b_1 in R^6`, `b_2 in R^3`, and the entire trainable
`M in R^(3 x 6)`. A **finite state** below means

\[
 w-g\in L^\infty,\qquad c\in L^\infty,\qquad
 \|M\|_F<\infty,
\tag{1}
\]

with `w,c` odd under simultaneous negation of their respective initialized
marks. This definition does not assert uniform boundedness in physical
time. It holds at each finite time by the assigned existence result.

**Theorem.** Suppose there are at most three distinct input directions
modulo sign. For a compatible law, merge repeated/antipodal copies with
their consistent labels, so that the active representatives are distinct
modulo sign. At every finite critical state with positive loss and `M!=0`,
the physical loss has a strictly negative second variation along bounded
odd state perturbations. Thus it is a strict saddle in the full physical
metric, including every trained block. Input linear independence is not
required.

Every such law has strict initialized descent. Consequently any finite
critical limit or finite accumulation point of its prescribed initialized
trajectory with positive loss has loss strictly below one and is a strict
saddle. The degenerate `M=0` critical states cannot be such limits because
their loss is one.

This is a finite-state theorem and an obstruction for possible initialized
limits. It does **not** exclude convergence from a particular deterministic
initialization to a strict saddle, and does not supply compactness or
exclude escape with positive limiting loss.

## 2. Exact critical-point equations and loss values

For input `u_i`, write

\[
\begin{gathered}
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad v_i=Ma_i,\quad
 h_i(b)=\tanh(b\cdot v_i),\quad f_i=E_2[ch_i],\\
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_i)],\quad
 q_i=b_1^TM^Td_i,\quad \rho_i=\mu_i(f_i-y_i).
\end{gathered}
\tag{2}
\]

The prediction differential in the population `L2` and Frobenius metric is

\[
 \nabla f_i=
 \bigl(\operatorname{sech}^2(w\cdot u_i)q_i u_i,
       h_i,d_i a_i^T\bigr).
\tag{3}
\]

Consequently a state is critical exactly when

\[
 \sum_i\rho_i h_i=0,\qquad
 \sum_i\rho_i\operatorname{sech}^2(w\cdot u_i)q_i u_i=0
 \text{ a.s.},\qquad
 \sum_i\rho_i d_i a_i^T=0.
\tag{4}
\]

The signs, the factor two in the physical flow, and the actual transpose
are those of the unhalved loss; no alternative block metric is used.

Partition the nonzero `v_i` into signed-equality groups: choose nonzero
representatives `v_G`, distinct modulo sign, and write
`v_i=sigma_i v_G`, `sigma_i in {+1,-1}`. Put `Z={i:v_i=0}`. The upper
mark law has positive density on an open cube around zero. The elementary
three-feature independence proof in `terminal_geometry.md` therefore gives

\[
 \sum_i\lambda_i h_i=0
 \quad\Longleftrightarrow\quad
 \sum_{i\in G}\sigma_i\lambda_i=0\quad\text{for every }G.
\tag{5}
\]

There is no condition on `lambda_i` for `i in Z`. At a critical state,
write `W_G=sum_(i in G) mu_i`. Equations (2), (4), and (5) imply

\[
 F_G:=E_2[c\tanh(b_2\cdot v_G)]
   =\frac{\sum_{i\in G}\mu_i\sigma_i y_i}{W_G}=:m_G,
 \qquad f_i=0\quad(i\in Z).
\tag{6}
\]

Hence every finite critical value belongs to the explicit finite list
obtained from signed partitions of the three indices:

\[
 \mathcal L_*
   =\sum_{i\in Z}\mu_i+
     \sum_G W_G(1-m_G^2).
\tag{7}
\]

Not every value on this list is asserted to be realizable or reachable.
The list is necessary, while (4), or the equivalent conditions below, is
necessary and sufficient for an actual specified state. Positive critical
loss requires a zero effective vector or a group containing both oriented
labels `sigma_i y_i=+1` and `-1`. If all effective vectors are nonzero and
distinct modulo sign, a critical state fits exactly.

In particular, set `mu_min=min_i mu_i`. Every positive finite critical
loss is at least `mu_min`. A zero effective vector contributes its atom's
weight. In a mixed group with total positive and negative oriented-label
weights `W_+,W_->0`, its contribution is
`4 W_+ W_-/(W_++W_-)`, which is at least
`2 min(W_+,W_-)>=2 mu_min`. This establishes a positive gap between zero
and every other possible finite critical value for each fixed weighted law.

If the three active inputs are linearly independent, the lower equation
in (4) is equivalent to

\[
 \rho_i M^Td_i=0\quad\text{for every }i.
\tag{8}
\]

Indeed their linear independence separates the three scalar pointwise
coefficients, their lower gates are strictly positive, and the normalized
lower feature Gram is positive definite. That Gram is positive definite
because each `(tanh G_j,tanh(sqrt(tau)Z_j+alpha tanh G_j))` has a positive
joint density on `(-1,1)^2`, coordinate pairs are independent, and the
Cholesky transformation is invertible.

Thus (6), (8), and the last equation in (4) are a complete finite-state
criticality criterion for independent inputs. Still assuming independent
inputs, at an arbitrary finite state the complete nullspace of the full
adjoint prediction differential consists of exactly
the vectors `lambda` satisfying the signed group sums in (5),
`lambda_i M^Td_i=0` for each `i`, and
`sum_i lambda_i d_i a_i^T=0`. This includes zero effective vectors and
extends the fitting-only criterion to arbitrary finite states.

When `M` has full row rank, (8) requires `d_G=0` in each group carrying
a nonzero residual, including the zero group if present. Within a group
the upper gate, and hence `d_i=d_G`, is common. Conversely these vanishing
conditions and (6) make all equations (4) hold: groups whose residuals
vanish contribute nothing, and every remaining group has `d_G=0`.
This simplified equivalence uses independent inputs and full row rank;
neither is silently assumed in the saddle theorem.

## 3. Two elementary separation lemmas

The strict-saddle proof first shows that lower perturbations can change a
residual-weighted effective vector. It then shows that the resulting upper
feature change has a component outside the current readout feature span.

### Lower separation despite an arbitrary bounded displacement

Let `J` be a nonempty subset of the inputs, let `alpha_i` be nonzero real
coefficients, and set

\[
 R(z)=\sum_{i\in J}\alpha_i
                  \operatorname{sech}^2(z\cdot u_i)u_i.
\tag{9}
\]

If the `u_i` are distinct modulo sign and `w-g` is bounded, then
`R(w)!=0` on a set of positive lower-population probability. To prove it,
choose a unit vector `e` such that the numbers `|e.u_i|` are positive and
pairwise different. Such a choice avoids only finitely many proper
hyperplanes. Let `j` uniquely minimize those numbers, and write
`C=||w-g||_infty+1`. On the event `|g-te|<1`,

\[
 |w\cdot u_i-t(e\cdot u_i)|\le C.
\]

Since
`exp(-2|s|)<=sech^2(s)<=4 exp(-2|s|)`, for `i!=j`,

\[
 \frac{\operatorname{sech}^2(w\cdot u_i)}
      {\operatorname{sech}^2(w\cdot u_j)}
 \le4e^{4C}
       e^{-2t(|e\cdot u_i|-|e\cdot u_j|)}\longrightarrow0
\tag{10}
\]

uniformly on that event. Thus (9), divided by the positive `j` gate,
tends uniformly to the nonzero vector `alpha_j u_j`. For sufficiently
large finite `t` it cannot vanish there. The Gaussian ball event has
positive probability. This argument does not require continuity or
invertibility of the map `g -> w`.

The law of the entire `b_1` vector has a positive density on an open
six-dimensional set, by the conditional density argument after (8).
Therefore `Mb_1!=0` almost surely whenever `M!=0`. It follows from (9)
that, for some coordinate `k`, the bounded odd perturbation

\[
 \delta w=(Mb_1)_k R(w)
\tag{11}
\]

satisfies

\[
 \left[ E_1[(Mb_1)(R(w)\cdot\delta w)]\right]_k
    =E_1[(Mb_1)_k^2|R(w)|^2]>0.
\tag{12}
\]

The perturbation is odd because `Mb_1` is odd and every gate in `R(w)`
is even. The same proof with `M` replaced by the identity proves that
`delta w -> E_1[b_1(R(w).delta w)]` is not the zero map.

### Upper derivative features do not lie in the readout span

Let `v_1,...,v_m`, `m<=3`, be nonzero and distinct modulo sign. If the
vectors `z_0,z_1,...,z_m` are not all zero, then the upper function

\[
 b\cdot z_0+\sum_{j=1}^m
        (b\cdot z_j)\operatorname{sech}^2(b\cdot v_j)
\tag{13}
\]

does not belong to the span of `tanh(b.v_j)`. The assertion includes
`m=0`. To prove it, an almost-sure putative identity becomes an identity
on the open cube by continuity and positive density. Choose `e` so that
`a_j=e.v_j` are nonzero with pairwise distinct absolute values and at
least one of `e.z_j`, including `j=0`, is nonzero. All excluded sets are
proper hyperplanes. Restriction to `b=t e`, followed by the real-analytic
identity theorem on the connected real line, would give

\[
 t\beta_0+\sum_j t\beta_j\operatorname{sech}^2(a_jt)
       =\sum_j A_j\tanh(a_jt)\qquad(t\in\mathbb R),
\tag{14}
\]

where `beta_j=e.z_j`. The functions are real analytic for all real `t`,
so the identity theorem applies to their difference, initially zero on
an interval around zero.

Taking `t -> +infinity` first shows `beta_0=0`, since the right side is
bounded, and then `sum_j A_j sign(a_j)=0`. Order the remaining indices
by increasing `|a_j|`. Use

\[
 \tanh(a t)=\operatorname{sgn}(a)
       [1-2e^{-2|a|t}+O(e^{-4|a|t})],\qquad
 \operatorname{sech}^2(a t)=4e^{-2|a|t}
                              +O(e^{-4|a|t}).
\]

Multiply (14), with its zero constant term subtracted, by the exponential
corresponding to the smallest `|a_j|`. All other indices decay. Dividing
by `t` yields `beta_j=0`; taking the limit again yields `A_j=0`.
Remove this index and repeat. This proves all `beta_j=0`, contrary to
the choice of `e`. Coincidences between higher exponential harmonics
cause no difficulty: the smallest remaining index is eliminated exactly
before the next step.

## 4. Proof of the strict-saddle theorem for nonzero M

Let a finite critical state have positive loss, so some `rho_i!=0`.
Group the effective vectors as in Section 2, also treating `Z` as one
group if it is nonempty. Choose a group `J` containing a nonzero residual
and use (9) with precisely its nonzero coefficients `alpha_i=rho_i`.
For a lower perturbation define

\[
 \delta a_i=E_1[b_1\operatorname{sech}^2(w\cdot u_i)
                                      (\delta w\cdot u_i)],
 \qquad z_J=\sum_{i\in J}\rho_i M\delta a_i.
\tag{15}
\]

Equations (11)–(12) give a bounded odd `delta w` with `z_J!=0` when
`M!=0`. Assign analogous `z_G` to the other groups. The corresponding
residual-weighted upper feature variation is exactly

\[
 S(b)=\sum_i\rho_i\delta h_i(b)
   =b\cdot z_Z+\sum_G(b\cdot z_G)
                  \operatorname{sech}^2(b\cdot v_G).
\tag{16}
\]

Here `z_Z=0` when the zero group is absent. There are no orientation
signs in the gates because `sech^2` is even; the signs already occur in
the individual residuals and effective-vector variations.

Let `H=span{h_i}` in upper-population `L2`, and put
`k=S-P_H S`. Lemma (13) proves `k!=0`. The space `H` is finite-dimensional,
so its orthogonal projection exists even when the original three-feature
Gram is singular. The function `k` is bounded and odd because `S` and
all features are bounded and odd. It is therefore an admissible readout
perturbation in the same odd sector. Moreover

\[
 D_cf_i[k]=\langle k,h_i\rangle=0,
 \qquad \sum_i\rho_i D^2_{cw}f_i[k,\delta w]
       =\langle k,S\rangle=\|k\|_2^2>0.
\tag{17}
\]

Write `Q` for the second variation of the physical loss. Since the
prediction is linear in `c`, the pure readout term along `k` is zero.
The first-order prediction from `k` also vanishes by (17). Thus, for a
real scalar `s`, ordinary differentiation of the unhalved square loss
gives exactly

\[
 Q[(\delta w,s k,0)]
     =Q[(\delta w,0,0)]+4s\|k\|_2^2.
\tag{18}
\]

All terms are finite: features, readout, matrix, and perturbations are
bounded, and all derivatives of tanh appearing in this expression are
bounded. Choose finite `s` sufficiently negative. The second variation
is strictly negative, proving the theorem. The constructed direction is
also a direction of the complete constant-coordinate formulation; its
omitted constant components are zero. No artificial freezing of a block
or diagonal restriction on `M` is involved.

## 5. The zero-middle exception is real but lies at loss one

At `M=0`, every prediction is zero, so `L=1`. Define

\[
 d_0=E_2[b_2c],\qquad A_y(w)=\sum_i\mu_i y_i a_i(w).
\tag{19}
\]

All state gradients vanish except possibly the matrix gradient, which is
`-2 d_0 A_y^T`. Hence such a state is critical exactly when
`d_0=0` or `A_y=0`.

For inputs distinct modulo sign, the identity-version of (12), applied
to coefficients `mu_i y_i`, proves `DA_y` is a nonzero linear map on
bounded odd lower perturbations. This gives a complete second-order
classification of these critical states:

* If `d_0=0` and `A_y!=0`, choose a matrix direction `N` and bounded odd
  readout direction `k` with `(E_2[b_2k])^T N A_y!=0`. Such `k` exists
  because the upper feature Gram is positive definite. Their mixed
  second loss variation is nonzero while both pure diagonal terms vanish.
  This is a strict saddle.
* If `A_y=0` and `d_0!=0`, choose `delta w` with `DA_y[delta w]!=0` and
  a matrix `N` with `d_0^T N DA_y[delta w]!=0`. The mixed matrix/lower
  second loss variation is nonzero, while the pure lower variation is
  zero. Scaling its coefficient defeats the finite pure matrix term.
  This too is a strict saddle.
* If `A_y=d_0=0`, the entire Hessian is zero. The prediction differential
  vanishes; the only potentially nonzero second derivatives are mixed
  readout/matrix and matrix/lower derivatives, whose loss contractions
  contain respectively `A_y` and `d_0`. The pure matrix term has
  `tanh''(0)=0`. Thus this case is not a strict saddle.

The last case is still a saddle with a third-order decreasing direction.
Choose bounded odd `v` with `A_1=DA_y[v]!=0`, a matrix `N`, and a bounded
odd `k` so that `z^T N A_1!=0`, where `z=E_2[b_2k]`. On the curve

\[
 w_\epsilon=w+\epsilon v,\quad M_\epsilon=\epsilon N,
 \quad c_\epsilon=c+\epsilon Kk,
\]

uniform Taylor expansion is legitimate in bounded marks and perturbations.
The assumption `d_0=0` annihilates the entire part linear in the upper
argument, even as `w` varies. Using `A_y=0` gives

\[
 \sum_i\mu_i y_i f_i(\epsilon)
 =\epsilon^3\left[
 K z^T N A_1-
 \frac13\sum_i\mu_i y_i E_2[c(b_2^TNa_i)^3]
 \right]+O(\epsilon^4),\qquad
 f_i(\epsilon)=O(\epsilon^2).
\tag{20}
\]

Choose the finite real constant `K` so that the bracket is positive.
Then `L(epsilon)=1-2 B epsilon^3+O(epsilon^4)` with `B>0`, proving
strict decrease for small positive epsilon and increase for small
negative epsilon. This verifies the saddle claim without calling a zero
Hessian a negative-curvature direction.

These fully degenerate states are not empty. Put `r=1/sqrt(2)` and take

\[
 u_1=(r,r,0),\quad u_2=(-r,0,r),\quad
 u_3=(0,-r,-r),\qquad \mu_i=1/3,\quad y_i=1.
\tag{21}
\]

The directions are distinct and nonantipodal; their span is two-dimensional.
At `w=g`, each lower initialized feature coordinate paired against
`tanh(g.u)` depends only on the corresponding coordinate of `u`, through
an odd scalar function. For an `h_j` coordinate this is conditioning on
`G_j`; for a reverse-derived `k_j` coordinate it is first conditioning
on `G_j`, preserving its odd conditional mean, and then the same Gaussian
conditioning. The Cholesky subtraction preserves oddness. In (21) each
input coordinate runs through `r,-r,0` across the three examples, so
`A_y(g)=0` exactly. Taking `M=0,c=0` produces a finite positive-loss
critical state with zero Hessian and the cubic descent (20). Its law is
compatible and has architectural loss floor zero. This disproves the
unqualified claim that every finite positive-loss critical state is a
strict saddle, while leaving the theorem for `M!=0` intact.

## 6. What follows for the prescribed initialization

The initialized separation and architectural-floor results in the assigned
sources imply strict initial descent for every compatible active law.
Indeed the initialized upper features on distinct unoriented inputs are
linearly independent, and their label-weighted readout velocity is nonzero.
The energy identity therefore gives

\[
 \mathcal L(t)<1\quad\text{for every }t>0,\qquad
 \mathcal L_\infty:=\lim_{t\to\infty}\mathcal L(t)
 \text{ exists in }[0,1).
\tag{22}
\]

The strict inequality for all positive times uses continuity of the
strictly negative initial derivative followed by monotonicity.

Here is the precise compactness-free statement about a *given* finite
accumulation point. Suppose `t_n -> infinity` and the state converges
along this sequence in the norms of (1) to a finite state `theta_*`.
Then `theta_*` is critical. To verify this without assuming global
precompactness, suppose its vector field is nonzero in the physical
metric. Local continuity supplies a state neighborhood with a positive
lower bound on its physical speed. Local boundedness of the vector
field in the norms (1) supplies a fixed positive duration for which
every sufficiently close arriving state remains in that neighborhood.
Each sufficiently late visit would therefore spend a fixed positive
amount of the finite dissipation budget. Extract visits separated by
that duration. Infinitely many such visits contradict
`integral_0^infinity ||theta'||_physical^2 dt <=1`.

Prediction and loss are continuous in these norms, so
`L(theta_*)=L_infinity`. If this value is positive, (22) rules out `M_*=0`.
The theorem then makes `theta_*` a strict saddle. In particular the full
prediction differential there is singular: the nonzero vector
`rho_i=mu_i(f_i-y_i)` annihilates its adjoint by (4). Thus nonsingularity
is not a valid automatic premise at a hypothetical positive-loss finite
limit. The appropriate obstruction is the negative second variation
(18), not an assumed lower bound on the full prediction kernel.

The critical-value gap also gives a conditional convergence certificate:
if the initialized loss ever falls below `mu_min` and the trajectory has
at least one finite accumulation point in (1), then `L_infinity=0`.
Indeed that point is critical with loss `L_infinity<mu_min`, and the gap
excludes every positive value. No state convergence or finite accumulation
is inferred merely from crossing this loss threshold.

Two bridges remain unproved and are logically separate:

1. A deterministic canonical initialization can lie in a strict saddle's
   stable set. Negative curvature alone does not exclude that possibility;
   no random-initialization or genericity assertion applies to this fixed
   population initialization without a separate proof.
2. Finite-time existence and finite dissipation do not imply that an
   all-time trajectory has a finite accumulation point in (1). Loss may
   converge while the matrix/readout/lower displacement escape, or while
   bounded populations fail to be compact. No such escape is constructed
   or ruled out here.

Accordingly, the exact result is: for a compatible initialized positive-loss
plateau, every finite accumulation point is a strict saddle, and its loss
satisfies (7). No whole-trajectory distance convergence is asserted. The fully degenerate
zero-middle critical set is inaccessible as an initialized limit by
energy monotonicity. Universal initialized fitting, exclusion of strict
saddle approach, and exclusion of positive-loss escape remain open.
