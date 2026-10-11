# Correlated geometry and the intrinsic tanh balance

2026-10-10. This is an internal theory-route note, not a promotion review.
The main target—arbitrary fixed bounded signed labels under typical canonical
dense Gaussian initialization—remains open. The exact obstruction below
invalidates one proposed conserved-quantity mechanism; it is not a counterexample
to fitting.

The initial scientific scope was the supervisor's model assignment and selected
complete sections of `docs/09-trainability.qmd` and
`docs/10-correlated-pairs.qmd`. After that route was reported, the supervisor
explicitly supplied `GLOBAL_FAILURE_ALTERNATIVES.md` and
`TANH_REPLICATION_CLASS.md` for mature-route comparison. No other study,
external scientific source, or experiment was used. Required canonical-notation,
proof, and conjecture skills were read. The separate saturation candidate is
checked in `POSITIVE_ARBITRARY_LABELS_CHECK.md`.

## Exact model and the rank-one restriction

Let $X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}$ have unit columns, and
let $y\in\mathbb R^m$. At width $n\ge m$, define

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad L=\|r\|^2/m.
\]

The parameter dimensions are $A\in\mathbb R^{n\times d}$,
$W\in\mathbb R^{n\times n}$, and $w\in\mathbb R^n$. The physical
gradient flow has mobilities $(n,1,n)$. If
$D_{ia}=\operatorname{sech}^2((WU)_{ia})$ and
$S_{ja}=\operatorname{sech}^2((AX)_{ja})$, its equations are

\[
\begin{aligned}
\dot w&=-\frac2mHr,\\
\dot W&=-\frac{2}{mn}[(wr^\top)\odot D]U^\top,\\
\dot A&=-\frac2m\{W^\top[(wr^\top)\odot D]\odot S\}X^\top.
\end{aligned}
\tag{1}
\]

Consider the exact replicated restriction

\[
A_{j:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=v,
\tag{2}
\]

where $p\in\mathbb R^d$ and $q,v\in\mathbb R$. Define sample vectors

\[
z=X^\top p,\qquad u=\tanh z,\qquad h=\tanh(qu),\qquad r=vh-y,
\]

and diagonal matrices

\[
S_z=\operatorname{diag}(\operatorname{sech}^2z_a),\qquad
D_{q,z}=\operatorname{diag}(\operatorname{sech}^2(q\tanh z_a)).
\]

Substitution in (1) shows that every first row keeps the same velocity,
every middle entry has velocity \(\dot q/n\), and every readout entry
has velocity \(\dot v\). Thus (2) is invariant, with exact equations

\[
\begin{aligned}
\dot v&=-\frac2m h^\top r,\\
\dot q&=-\frac{2v}{m}u^\top D_{q,z}r,\\
\dot p&=-\frac{2vq}{m}X S_zD_{q,z}r,\\
\dot z&=-\frac{2vq}{m}G S_zD_{q,z}r,
\qquad G=X^\top X.
\end{aligned}
\tag{3}
\]

Its inherited metric is exactly

\[
\frac1n\|\delta A\|_F^2+\|\delta W\|_F^2+
\frac1n\|\delta w\|^2
=\|\delta p\|^2+\delta q^2+\delta v^2.
\]

Consequently (3) is Euclidean gradient flow of
$m^{-1}\sum_a(v\tanh(q\tanh(p^\top x_a))-y_a)^2$, independent of
width. This exact restriction is a Gaussian-null family, not a replacement
for dense Gaussian initialization.

## Full input rank removes finite positive-loss critical limits in this family

Assume \(\operatorname{rank}X=m\), so $G$ is positive definite. At any
finite state with $vq\ne0$, the equation \(\dot p=0\) implies

\[
X S_zD_{q,z}r=0.
\]

The map $X:\mathbb R^m\to\mathbb R^d$ is injective and both diagonal
matrices have positive entries. Hence $r=0$. There are no finite
positive-loss critical points in the part of this family where $vq\ne0$.

Suppose $v(0)=0$, $q(0)\ne0$, and $h(0)^\top y\ne0$. Then

\[
\dot v(0)=\frac2m h(0)^\top y\ne0,\qquad
\dot L(0)=-\frac4{m^2}(h(0)^\top y)^2<0.
\]

For every positive time the loss is therefore strictly below
$L(0)=\|y\|^2/m$. Neither $v$ nor $q$ can subsequently vanish:
either event would make $f=0$, contradicting that loss decrease. They
also cannot vanish at a finite accumulation point, for the same reason.

Every finite accumulation point of a smooth finite-dimensional gradient
flow with a fixed positive metric is stationary in this setting. A direct
argument suffices: if the speed were bounded below near an accumulation
point, continuity would give a ball with squared speed at least $c>0$
and speed at most $C<\infty$. A visit to its concentric half-ball would
last at least its half-radius divided by $C$, forcing a fixed positive
loss drop. Infinitely late visits contradict convergence of the decreasing
loss. Local smoothness and the energy displacement bound

\[
\|(p,q,v)(t)-(p,q,v)(s)\|
\le\sqrt{(t-s)[L(s)-L(t)]}
\]

also exclude finite-time escape and give global existence.

It follows that either $L(t)\to0$, or there is no finite parameter
accumulation point and

\[
\|p(t)\|^2+q(t)^2+v(t)^2\longrightarrow\infty.
\tag{4}
\]

Indeed failure of the norm limit in (4) would supply a bounded subsequence
and hence a finite accumulation point. This excludes finite bad capture
for this initialized family under full input rank; it does not exclude
positive-loss escape.

## The proposed primitive exists exactly for orthogonal geometry

The natural candidate balance is

\[
q^2-F(z),
\tag{5}
\]

where $F:\mathbb R^m\to\mathbb R$ is $C^2$, depends on the fixed
input geometry, and is to be conserved for the system (3) for arbitrary
fixed labels and states. The requirement is a universal identity, not a
potential fitted to a single trajectory.

From (3), at states with $vq\ne0$,

\[
\frac d{dt}(q^2-F(z))
=\frac{2vq}{m}
\{\nabla F(z)^\top G S_zD_{q,z}-2u^\top D_{q,z}\}r.
\]

Varying the labels makes $r$ arbitrary at a fixed state. Since
$D_{q,z}$ is invertible, the derivative vanishes for every label if and
only if

\[
\nabla F(z)=2G^{-1}S_z^{-1}u
=G^{-1}\sinh(2z).
\tag{6}
\]

The last identity uses $2\tanh z/\operatorname{sech}^2z=\sinh(2z)$
componentwise. For distinct indices $a,b$, (6) gives

\[
\partial_b\partial_aF
=2(G^{-1})_{ab}\cosh(2z_b),\qquad
\partial_a\partial_bF
=2(G^{-1})_{ab}\cosh(2z_a).
\]

Equality of mixed derivatives on an open set of freely varying sample
coordinates requires

\[
(G^{-1})_{ab}\,[\cosh(2z_b)-\cosh(2z_a)]=0
\quad\hbox{throughout that set}.
\tag{7}
\]

The bracket is not identically zero on any nonempty open subset of
$\mathbb R^m$. Therefore every off-diagonal entry of $G^{-1}$ must
vanish. Conversely, for diagonal $G$,

\[
F(z)=\sum_a(G^{-1})_{aa}\sinh^2z_a
\]

satisfies (6) and produces a conserved quantity. Thus a balance of the
form (5), valid universally as stated, exists if and only if $G$ is
diagonal. With unit inputs this means $G=I_m$, and the balance is

\[
q(t)^2-\sum_a\sinh^2z_a(t)
=q(0)^2-\sum_a\sinh^2z_a(0).
\tag{8}
\]

Even (8) is not by itself a complete two-hidden-layer fitting theorem:
it does not control the independent readout coordinate or exclude every
infinite-time escape. Equation (7) rules out the stated primitive route
for correlated full-rank data. It does not rule out a Lyapunov function
depending on $q,v,y$, a nonconserved coercive estimate, or a proof of
fitting by another mechanism.

## A separate sign-cone obstruction

Oddness permits the exact transformation
$x_a\mapsto\sigma_ax_a,\ y_a\mapsto\sigma_ay_a$, with
$\sigma_a\in\{-1,1\}$. It maps predictions in the same way and leaves
the loss and its parameter gradient unchanged. The transformed Gram is
$\operatorname{diag}(\sigma)G\operatorname{diag}(\sigma)$.
Requiring its off-diagonal entries to be nonnegative for every label sign
pattern forces every original off-diagonal entry to be zero. Hence an
acute-input argument after absorbing label signs cannot directly cover
every sign pattern on a fixed nonorthogonal dataset.

Furthermore, positive kernel entries do not preserve positive residuals
$e=y-f$. The exact residual equation is
$\dot e=-(2/m)\mathcal K e$, with \(\mathcal K\) the mobility-weighted
prediction-Jacobian Gram. On a face $e_a=0$,

\[
\dot e_a=-\frac2m\sum_{b\ne a}\mathcal K_{ab}e_b.
\]

When an off-diagonal entry is positive, this points out of the positive
orthant for an appropriate nonnegative residual vector. Scalar residual
monotonicity from an equal-amplitude symmetry sector therefore cannot be
silently applied to unequal labels.

## Audit of the permitted maintained-book results

Complete inspected units and their precise mismatches with the target:

| Source unit | Actual result relevant here | Why it does not close the target |
|---|---|---|
| `docs/09-trainability.qmd`, lines 1663–2068: finite-optimization introduction and Sections 1–3 | Three-hidden-layer arctangent, one input and one unit target; zero/small readout fitting by scalar readout-norm convexity | Scalar residual, different activation and depth |
| Same file, lines 2946–3138: Sections 8–9 | Gaussian event and exact scope for that scalar theorem | Does not add arbitrary multiinput labels |
| Same file, lines 3139–3578: Section 10, all subsections | Two inputs, opposite unit labels, first activation with compactly supported derivative, top activation $z+\varepsilon\arctan z$, tiny Gaussian readout | Protected first rows and top derivative at least one are both absent for tanh; finite readout also differs |
| Same file, lines 3705–3916: global-depth introduction and Section 1 | One sample, depth at least three, activation $1+\arctan(z)/10$ | Different activation, depth, and sample count; references to other chapters were not followed |
| `docs/10-correlated-pairs.qmd`, lines 7–146: overview and conventions | Exact storage/time maps and list of specialized pair families | Supplies no arbitrary-label two-hidden tanh theorem |
| Same file, lines 1717–2310: D introduction and complete D.1 | Three hidden layers, $1+z+\varepsilon\arctan z$, binary pair labels, separated angles | Different depth and activation; equal-amplitude label sectors |
| Same file, lines 5810–6082: complete Section G | Three hidden layers, $1+\arctan(\sinh z)/10$, equal binary labels | A sech gate is not tanh activation; the positive activation floor and symmetry are essential to the stated result |
| Same file, lines 6083–6371: complete protected-pair closure section | Order-one tanh dictionary closure; arbitrary amplitude only for opposite-label protected reflections/antipodes; arbitrary pairs only when $\sqrt{(y_u^2+y_v^2)/2}\le\lambda/(8\sqrt5)$ | This is a fixed-order closure, not the actual dense Gaussian source, and the generic-label theorem is explicitly small-label |

No claim here imports proofs from uninspected linked chapters. These complete
units suffice to reject the listed theorems as direct instances of the
specified target; they do not establish absence of every possible theorem
elsewhere in the book.

Recorded source hashes at this check:

- `docs/09-trainability.qmd`: `2bd293017b66125c00f3ed338117affcc4d21977b707229091cc80e6c722e477`.
- `docs/10-correlated-pairs.qmd`: `d07a14b99a51daf1a0c8c95414d28c1ca3cabcb07ad22a6bcc7d8231096e4a05`.
- `GLOBAL_FAILURE_ALTERNATIVES.md`: `83efe858430bf60b5686c5790f0d71da0b2e87fe4a2002ea7628673716ba294f`.
- `TANH_REPLICATION_CLASS.md`: `3e0bcb142b985d5e79c8a56f6a66ee91e06fe22b3a41bb1a262c1f8eaf32e14b`.

The mathematical identities above were checked by direct differentiation,
matching every mobility and sample factor, and checking the mixed derivatives
of (6). No experimental or external-theorem premise is used. The unrestricted
Gaussian fitting conclusion remains unproved.
