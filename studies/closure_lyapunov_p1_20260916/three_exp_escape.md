# Three-input escape route: lower moment submersion and stationary saddles

Frozen analytical route, 2026-09-16. This is a scoped independent attempt on
the exact prescribed-initialization order-one population closure, with three
distinct, pairwise non-antipodal directions on the unit circle, masses `1/3`,
and labels `(+1,+1,-1)`. All three moving blocks, the actual transpose,
canonical joint mark laws, ridge `eta=1/4096`, and physical unhalved-loss
metric are retained. No experiment, random-start genericity argument,
different study, or external convergence theorem is used.

**Result.** The lower moment map is a submersion at every state with
bounded `w-g`. Consequently every nonfitting stationary state in this
chart with nonzero middle matrix has a strictly negative second-variation
direction. The initialized trajectory has loss strictly below one at
every positive time, so it cannot reach the zero-middle-matrix stratum.
Nevertheless, bounded, parity-compatible nonfitting stationary states of
loss `2/3` exist, even with a middle matrix of full active row rank.
They are strict saddles. Their construction does not show that the
prescribed trajectory reaches them.

The new submersion mechanism removes a possible lower-feature obstruction
to separating collided upper features. It does **not** prove deterministic
saddle avoidance, bounded displacement at infinite time, or exclusion of
unbounded-readout escape. It therefore does not supply the requested
current-state exponentially decaying potential.

## 1. Sources, scope, and exact state

The supplied scientific inputs were `docs/NOTATION.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3,
`arbitrary_pair_local.md` sections 1–4,
`generic3_stationary_geometry.md`, and
`generic3_metric_second_pass.md`. Only those inputs are used below.
One displayed line-range read of the pair file extended into its section 5;
no claim or argument from that extra section is used. No current parallel
route was read. Required skills were `investigate-conjectures` and
`solve-math-rigorously`, including the former's research-contract,
adversarial-audit, and bounded-proof-search instructions.

Source-file SHA-256 values at reading were:

| Source | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `arbitrary_pair_local.md` | `4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a` |
| `generic3_stationary_geometry.md` | `170447ad239b991762fd4597a0a52318d04b9c4bad750ad95ca4c0e15dd777db` |
| `generic3_metric_second_pass.md` | `104ed0fe6a7ee9e58cbe5d5c9f5c97598523e57649229993e5f7747efb446b4e` |

All lower and upper expectations retain their own probability spaces.
On the exactly invariant mark-parity subspace, omit only the identically
inactive constant coordinates. Thus `b` is the four-dimensional odd lower
normalized feature column, `beta=Z/sqrt(tau+eta)` is the two-dimensional
odd upper column, and the active middle matrix is `M` of size `2 by 4`.
This is the canonical coordinate block with its unchanged Euclidean metric,
not a different normalization. Put

\[
 X=(\tanh g_1,\tanh g_2,
       \tanh(\zeta_1+\alpha\tanh g_1),
       \tanh(\zeta_2+\alpha\tanh g_2)).
\]

The lower column `b` is an invertible linear transform of `X`.
The map `(g,zeta) -> X` is a smooth bijection from `R^4` to `(-1,1)^4`:
invert its first two coordinates by `artanh`, and then recover each
`zeta_j=artanh(X_{j+2})-alpha X_j`. Its Jacobian is nonsingular.
The independent Gaussian roots have a strictly positive density, so `X`
has a strictly positive density throughout that cube. In particular a
nonzero linear form in `b` is nonzero almost surely.

For the three inputs define

\[
 a_i=E_1[b\tanh(w\cdot u_i)],\quad
 s_i=\operatorname{sech}^2(w\cdot u_i),\quad
 v_i=Ma_i/\sqrt{\tau+\eta},\quad
 H_i=\tanh(Z\cdot v_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i.
\]

The full loss is `L=(1/3)sum r_i^2`. The canonical finite-time existence
proof gives `w-g` bounded in essential supremum on each finite interval.
The lower normalized feature synthesis map is a contraction, hence
`|a_i|<=1`. No such all-time bound on `w-g` is assumed below.

## 2. Independent lower moment variations

**Proposition 1.** Fix any measurable `w` with `w-g` essentially bounded.
The derivative of

\[
 \mathcal A(w)=(a_1,a_2,a_3)\in(\mathbb R^4)^3
\]

is the surjective bounded linear map

\[
 T_w h=\big(E_1[b s_i(h\cdot u_i)]\big)_{i=1}^3,
 \qquad h\in L^2(\Omega_1;\mathbb R^2).                 \tag{1}
\]

It has the explicit right inverse

\[
 R_w=T_w^*(T_wT_w^*)^{-1},                              \tag{2}
\]

whose values are bounded fields. Every prescribed small change of all
twelve moments is consequently attainable by a bounded perturbation of
`w`, while remaining in the canonical odd mark-parity subspace.

**Proof.** The derivative formula follows from the bounded derivative and
Lipschitz derivative of tanh: its pointwise first-order remainder is at
most a constant times `|h|^2`, which is integrable. The adjoint is

\[
 T_w^*(B_1,B_2,B_3)
      =\sum_{i=1}^3 (b\cdot B_i)s_i u_i.               \tag{3}
\]

Suppose (3) is zero almost surely. Since every pair of input directions
is linearly independent, the one-dimensional kernel of the `2 by 3`
matrix with columns `u_i` is spanned by a vector `k` with every `k_i`
nonzero. Thus, pointwise, the three scalars

\[
           (b\cdot B_i)s_i/k_i
\]

are equal. If one `B_i` is zero, this forces all `b dot B_j` to vanish
almost surely; positive density and the invertible normalization give
`B_j=0` for every `j`.

Otherwise define the nonzero linear forms `q_i=(b dot B_i)/k_i`.
The gates are strictly positive, so all `q_i` have the same sign almost
surely. Any two linear forms with the same sign almost everywhere on a
neighborhood of zero must be positive scalar multiples of one another.
Indeed, if their coefficient vectors are linearly independent, their
joint linear map onto `R^2` realizes a pair of opposite signs at a point
arbitrarily close to zero and therefore on an open positive-probability
set. If they are negative multiples, their signs disagree away from
their common zero hyperplane. Applying this fact on the raw open cube
gives `q_i=gamma_i q` for one nonzero linear form `q` and numbers
`gamma_i>0`.

Outside the zero hyperplane of `q`, the adjoint equation now gives

\[
 \gamma_i\operatorname{sech}^2(w\cdot u_i)
       =\gamma_j\operatorname{sech}^2(w\cdot u_j).
\]

As `log cosh x-|x|` lies in `[-log 2,0]`, this implies

\[
 \big||w\cdot u_i|-|w\cdot u_j|\big|
       \le \tfrac12|\log(\gamma_i/\gamma_j)|+\log2.   \tag{4}
\]

Define the geometry constant

\[
 \delta=\min_{|d|=1}\max_{i,j}
                 \big||d\cdot u_i|-|d\cdot u_j|\big|. \tag{5}
\]

It is positive. Otherwise compactness gives a unit `d` for which the
three absolute projections are equal. In coordinates with `d=(1,0)`,
a fixed absolute first coordinate selects at most two directions modulo
antipodality on the unit circle. Three pairwise non-antipodal directions
cannot all have that absolute first coordinate. This proves positivity.
Combining (4)–(5) bounds `|w|` by a finite constant almost surely.
But `w=g+(w-g)` with bounded `w-g` and Gaussian `g` is essentially
unbounded. This contradiction proves that (3) has only the zero solution.

The finite symmetric matrix `T_wT_w^*` is therefore positive definite:
its quadratic form at `B` is `||T_w^*B||_2^2`. Formula (2) is well
defined and satisfies `T_w R_w=I`, proving surjectivity. Since `b`
and all gates are bounded, (3) and therefore (2) have bounded values.
If `w` is odd under simultaneous mark reversal, each gate is even;
`T_w^*B`, and hence `R_w B`, are odd.

For completeness, the nonlinear local-attainment statement does not
require an infinite-dimensional inverse theorem. On the finite
twelve-dimensional parameter space put

\[
 F(h)=\mathcal A(w+R_w h)-\mathcal A(w).
\]

This is continuously differentiable near zero, with `DF(0)=I`, because
`R_w h` is a bounded field depending linearly on finitely many scalars.
Choose a closed radius-`rho` ball on which `||DF-I||<=1/2`. For a target
`k` with `|k|<=rho/2`, the map `h -> k+h-F(h)` maps this ball into itself
and has Lipschitz constant at most `1/2`. Its successive iterates converge,
by the geometric-series estimate on consecutive differences, to a fixed
point. At that point `F(h)=k`. This proves local attainment. ∎

The mechanism is not a replacement by independently trainable lower
features: (1)–(2) explicitly realize their infinitesimal variations in
the actual moving lower population and its actual metric.

In particular the actual lower velocity is

\[
        w'=-\frac23 T_w^*((r_i M^T d_i)_{i=1}^3),
        \qquad d_i=E_2[\beta c\operatorname{sech}^2(Z\cdot v_i)].
\]

At a full stationary state in this chart, injectivity of `T_w^*` forces
`r_i M^T d_i=0` for each sample separately. If `M` has row rank two,
then every sample with nonzero residual has `d_i=0`. Thus stationary
lower-gradient cancellation between the three samples is impossible
unless all three constituent coefficient vectors already vanish.

**Uniform bounded-displacement version.** For every finite `R`, there is
`kappa_R>0` such that

\[
        T_wT_w^*\succeq\kappa_R I_{12}
        \quad\hbox{whenever }\|w-g\|_\infty\le R.     \tag{6}
\]

Here is a proof that does not assert compactness of a bounded function
ball. For `sum_i |B_i|^2=1`, define

\[
 J_R(B)=E_1\min_{|h|\le R}
 \left|\sum_i (b\cdot B_i)
       \operatorname{sech}^2((g+h)\cdot u_i)u_i\right|^2.
                                                               \tag{7}
\]

The minimum exists by continuity on the finite compact ball. The
integrand is bounded by a fixed multiple of `|b|^2`, and its variation
in `B` is uniformly bounded on the coefficient unit sphere. Thus `J_R`
is continuous there. If it were zero, then for almost every mark some
`h` in that ball would make the adjoint equation zero. The sign argument
above would again make all nonzero `q_i` positive multiples of one
linear form. Equation (4) would then bound every such `g+h` by a common
constant, and so bound `|g|` by that constant plus `R`, a contradiction.
The zero-form case also contradicts the unit coefficient norm. Hence
`J_R>0` on the compact sphere. Its positive minimum is `kappa_R`, and
every actual `w=g+h` lies above the pointwise minimum in (7), proving
(6). This gives a defined, geometry-dependent constant, not an evaluated
numerical lower bound or an all-time bound on `R`.

## 3. A ridge derivative supplies a new readout direction

**Lemma 2.** Let `S` be the span of any finite collection of features
`tanh(Z dot v_j)`, including the zero feature if present. For any vector
`v` among their coefficient vectors and any nonzero `p` in `R^2`,

\[
       k(Z)=(Z\cdot p)\operatorname{sech}^2(Z\cdot v)
                  \notin S.                           \tag{8}
\]

**Proof.** Group equal/opposite nonzero coefficient vectors. Choose `z`
outside the finitely many lines on which `p dot z=0`, a nonzero remaining
coefficient has zero dot product, or two distinct coefficient groups have
equal absolute dot products. Such `z` exists because none of these
linear constraints is identically zero. An alleged almost-sure identity
in (8) is continuous on the open square with positive density, so it is
an identity there. Restricting to `Z=t z` first gives an identity on a
nonempty interval in `t`; real analyticity extends it along the real
line. This extension follows directly by extending a zero Taylor series
at any finite endpoint of an interval of equality.

If `v=0`, the left side is the nonzero unbounded linear function
`t(p dot z)`, whereas the right side is a finite sum of bounded tanh
functions, a contradiction. If `v!=0`, write `b=|v dot z|>0`.
The left side has large-positive-`t` asymptotic

\[
                 4(p\cdot z)t e^{-2bt}(1+o(1)).
\]

After absorbing signs, the right side is `sum_j A_j tanh(b_j t)`
with distinct `b_j>0`. Its constant limit must be zero. If any coefficient
is nonzero, let `b_*` be the smallest rate with nonzero coefficient.
The identity `tanh x=1-2e^{-2x}+O(e^{-4x})` gives right-side asymptotic

\[
                        -2A_*e^{-2b_*t}(1+o(1)).
\]

For `b_*<b`, scaling by `e^{2b_*t}` gives zero on the left and a nonzero
limit on the right. For `b_*>b`, scaling by `e^{2bt}/t` gives a nonzero
limit on the left and zero on the right. For `b_*=b`, scaling by
`e^{2bt}` gives a linearly growing left side and a finite nonzero right
limit. All cases contradict equality. If every coefficient is zero,
the left side itself is nonzero. This proves (8). ∎

## 4. Every nonfitting stationary state in the chart is a strict saddle

**Proposition 3.** Suppose `w-g` is bounded, `M!=0`, and the full
population state is stationary with positive loss. Then there are bounded
odd row/readout perturbations, preserving the frozen marks and keeping
`M` fixed, along whose linear combination the loss has strictly negative
second derivative. In particular this state is not a local minimum.

**Proof.** Choose a sample `i` with `r_i!=0` and a nonzero vector
`p` in the range of `M`. Proposition 1 gives a bounded odd row direction
`X_w` such that its three lower moment variations are zero except at
sample `i`, where choose `delta a_i` with
`M delta a_i=sqrt(tau+eta) p`. Consequently

\[
               D H_j[X_w]=0\ (j\ne i),\qquad
               D H_i[X_w]=k_i:=(Z\cdot p)
                                  \operatorname{sech}^2(Z\cdot v_i).
\]

Let `S=span{H_1,H_2,H_3}` and set `e=k_i-P_S k_i`, where `P_S` is
the orthogonal projection onto this finite-dimensional span. Lemma 2
gives `e!=0`. The functions involved are bounded and odd, so `e` is a
permitted bounded odd readout direction. Denote the pure readout
direction by `X_c=(0,e,0)`. Its first prediction variation is zero at
every sample, since `e` is orthogonal to `S`; its pure second prediction
variation is also zero, since prediction is affine in `c`.

All derivatives along these bounded directions may be passed under the
population expectations by bounded domination. Let `Q` denote the loss
second-variation bilinear form on their two-dimensional span. The chain
rule for `L=(1/3)sum r_j^2` gives

\[
 Q(X_c,X_c)=0,\qquad
 Q(X_w,X_c)=\frac23 r_i\langle e,k_i\rangle
           =\frac23 r_i\|e\|_2^2\ne0.                 \tag{9}
\]

The finite number `Q(X_w,X_w)` has no prescribed sign. Nevertheless

\[
 Q(X_w+aX_c,X_w+aX_c)
          =Q(X_w,X_w)+2a Q(X_w,X_c)
\]

is strictly negative for a suitable finite real `a`. At a stationary
state the first derivative in this direction is zero, so its ordinary
one-dimensional Taylor expansion decreases loss at order two. The
perturbation remains in the declared bounded-displacement chart and
preserves mark parity for sufficiently small amplitude. ∎

This assertion concerns an actual negative second variation; no
finite-dimensional random-initialization saddle-avoidance theorem is
being imported into this deterministic population problem.

## 5. What the prescribed initialization adds, and what it does not

Let `G_H=(E_2[H_i(0)H_j(0)])_{i,j}`. The supplied initialization theorem
makes this matrix positive definite for the present input class. Since
`c(0)=0`, the other initial block velocities vanish and

\[
 \mathcal L'(0)
       =-\|c'(0)\|_2^2
       =-\frac49 y^T G_H y<0.                         \tag{10}
\]

Continuity makes loss strictly less than one on a sufficiently short
positive interval; its subsequent monotonicity therefore proves

\[
                    \mathcal L(t)<1\quad(t>0).        \tag{11}
\]

If `M=0`, all upper features and predictions vanish, giving loss one.
Thus the actual initialized trajectory never has `M=0` at positive time.
More quantitatively, contraction of upper normalized feature synthesis,
`|tanh z|<=|z|`, and `|a_i|<=1` give

\[
  1-\sqrt{\mathcal L}
  \le\left(\frac13\sum_i f_i^2\right)^{1/2}
  \le \|c\|_2\,\|M\|_{\rm op}.                      \tag{12}
\]

After any fixed positive time the left side is uniformly positive.
This excludes simultaneous vanishing of these blocks and excludes
`M->0` if the readout is bounded. It still permits reciprocal growth and
collapse. It does not preserve rank two or bound either block separately.

The following construction shows why energy below one and parity alone
cannot replace the missing deterministic argument.

**Proposition 4.** For every input triple under consideration, the same
fixed canonical mark laws admit a bounded odd state with `w-g` bounded,
active `M` of row rank two, loss `2/3`, and all three block velocities zero.

**Proof.** Start the lower population at `w=g`. Proposition 1 shows that
its three moment columns can be perturbed arbitrarily in a neighborhood
using bounded odd row perturbations. Matrices with three independent
columns are dense among `4 by 3` matrices: add `epsilon E`, where one
`3 by 3` minor of `E` is invertible. The same minor of `A+epsilon E`
is a polynomial in `epsilon` with nonzero cubic coefficient, so it
vanishes at only finitely many values. Hence choose such a nearby moment
matrix `A=(a_1,a_2,a_3)` and realize it with bounded odd `w-g`.

There is a row vector `l` with

\[
          l\cdot a_1=l\cdot a_3=1,\qquad l\cdot a_2=2.
\]

Choose a nonzero row vector `n` orthogonal to all three columns. It is
independent of `l`, since `l dot a_1=1`. Take the two rows of `M` to be
`sqrt(tau+eta) l` and `n`. This matrix has row rank two and yields

\[
       H_1=H_3=H:=\tanh Z_1,\qquad H_2=J:=\tanh(2Z_1).
\]

Put

\[
 F=\operatorname{span}\{H,\,Z_1\operatorname{sech}^2Z_1,
                                  Z_2\operatorname{sech}^2Z_1\}.
\]

The feature `J` does not belong to `F`. If it did, positive density
would extend the identity throughout the open square. Dependence on
`Z_2` first forces that coefficient to be zero. Restriction to `Z_1=t`
and real-analytic continuation would give

\[
             \tanh(2t)=A\tanh t+B t\operatorname{sech}^2t
                      \quad(t\in\mathbb R).
\]

The positive-infinity limit gives `A=1`; multiplying the remaining
identity by `e^{2t}` gives limit `2` on the left and asymptotic `4Bt`
on the right, an impossibility for every `B`.

Let `J_perp=J-P_FJ` and choose the bounded odd readout

\[
                       c=J_\perp/\|J_\perp\|_2^2.
\]

Then `f_1=f_3=0`, `f_2=1`, and
`E_2[beta c sech^2 Z_1]=0`. The residual vector is `(-1,0,1)`.
The readout velocity is zero because `H_1=H_3`; the middle and lower
velocities are zero because both nonzero residuals have the identical
zero backward coefficient `d_1=d_3=0`. The loss is exactly `2/3`.
All fields and perturbations have the required parity. ∎

This is a represented stationary-state construction, not a trajectory
from `w=g,c=0,M=D`. In particular it neither proves nor suggests that the
initialized flow reaches these saddles. It does prove that (11), full
active row rank, boundedness, and mark parity do not individually or
jointly eliminate every nonfitting stationary state.

## 6. Audit, claim levels, and smallest gap

The proved objects are exact finite-state statements about the full
nonlinear population closure. The submersion uses the correlated lower
marks through their actual joint positive density. It neither samples
fresh independent marks nor treats the four coordinates as independent.
Its nondegeneracy depends on all three pairwise non-antipodal directions;
with only two coincident/antipodal directions the unique-dependence and
positive-`delta` arguments fail as they should.

The bounded row directions are produced by the actual Hilbert adjoint,
so they have finite physical norm and preserve the declared marks.
The strict-saddle perturbation is local, uses a finite projection of
current upper functions, and has no future or trajectory oracle.
The proof does not presume monotonic sample separations or a conserved
linear-network balance quantity. The stationary example verifies every
velocity explicitly and therefore is not merely readout-stationary.

Three substantive barriers remain:

1. A deterministic gradient trajectory can in principle approach a
   strict saddle on its stable set. The prescribed initialization is a
   particular correlated state; ambient almost-everywhere avoidance
   would not address it.
2. `w-g` is bounded on every finite interval, but its all-time supremum
   bound is unproved. Consequently (6) has not supplied an all-time
   lower moment condition number, and a limiting state may leave this
   chart even without an `L2` blowup.
3. Energy and (12) permit unbounded readout/middle escape. No argument
   here prevents loss from persisting along such an escaping sequence.

Thus the smallest new local obstruction is resolved: nonfitting feature
collisions cannot be locally stable minima in the bounded-displacement
chart with nonzero `M`. The unresolved bridge is exclusion of their
stable sets, and of escaping alternatives, for the **specified**
initialization. These are substantive dynamical assertions, not
consequences of the strict-saddle calculation. Route status: useful
intermediate theorem frozen; unconditional convergence and the requested
state-only exponential potential remain open.
