# Recheck of finite-critical avoidance on the exact zero-readout slice

2026-10-11. Scoped independent audit. The complete assigned scientific
inputs were `GAUSSIAN_RANK_ONE_COMPLETION.md` and
`GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md`, together with the canonical model
in the supervisor's assignment. Required mathematical and canonical-notation
instructions were applied. No external scientific source, other study,
experiment, Git operation, or existing-file modification was used.

**Verdict.** The stated avoidance argument is valid with at least \(n\)
negative Hessian directions, using the local center-stable-manifold theorem
in the precise form stated in the assigned files. It applies to the actual
Gaussian law supported on exactly zero readout. With only \(n-1\)
negative directions, its dimension argument fails: the center-stable
manifold can contain both the initialization slice and its transverse flow
direction. Neither \(r^\top y<0\) nor loss below its initial value repairs
this argument. The former inequality is automatic at every positive-loss
critical point with stationary readout. This is a limitation of the
geometric inference, not a canonical-network counterexample to every
possible theorem based on a smaller index.

## 1. Model and the Hessian input being used

Let \(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\) have linearly
independent unit columns, and let \(y\in\mathbb R^m\setminus\{0\}\).
At fixed width \(n\),

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad \mathcal L=\|r\|^2/m,
\]

where \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). Let
\(\theta=(A,W,w)\in\mathbb R^N\), where
\(N=nd+n^2+n\), and let \(D\) be the positive diagonal mobility
matrix with blocks \((nI,I,nI)\). The vector field is
\(V(\theta)=-D\nabla\mathcal L(\theta)\).

The initialization slice and its constant initial loss are

\[
M_0=\{(A,W,w):w=0\},\qquad
\dim M_0=N-n,
\qquad \mathcal L_0=\|y\|^2/m.
\tag{1}
\]

The algebra in the assigned rank-one source supplies at least \(n\)
negative Hessian directions at every finite critical point with
\(0<\mathcal L<\mathcal L_0\), provided
\(n\ge\max\{1,2m-4\}\). The key rank-one construction survives
rechecking: the first-feature variations \(\Delta U(v)=vs^\top\)
give an \(n\)-dimensional zero bilinear block because
\(\beta_as_a^2=1\) on residual support and \(Hr=0\); the mixed
block is onto because every \(G_i>0\), allowing its unwanted
\(W^\top\) term to be canceled by a readout variation. Full column
rank of \(X\) is what makes all these \(\Delta U\) directions locally
accessible in the actual first weights. The supplied other-rank bound
\(g(n-\operatorname{rank}U)\ge g(n-m+g)\), for \(g\ge2\), reaches
\(n\) at the stated width threshold. No algebraic gap affecting the
index input was found.

At a critical point the training linearization
\(-D\nabla^2\mathcal L\) is similar to
\(-D^{1/2}\nabla^2\mathcal L D^{1/2}\). Congruence by the invertible
positive matrix \(D^{1/2}\) preserves Hessian inertia. Thus the index
bound gives at least \(n\) positive eigenvalues of the training
linearization. The linearization is real diagonalizable because the
similar matrix is symmetric.

## 2. Exact geometric lemma for a singular initialization law

The local center-stable fact needed here is the following one, as stated
in the assigned files. For a \(C^2\) vector field and an equilibrium
with \(k\) unstable linearized directions, there is an embedded local
\(C^1\) center-stable manifold of dimension \(N-k\), containing all
forward trajectories that remain in a sufficiently small neighborhood.
Within an appropriate smaller neighborhood, the actual field is tangent
to that manifold. Zero eigenvalues are included in its center part.
The network field is real analytic, hence meets the smoothness assumption;
the preceding paragraph checks the spectral condition. This audit checks
the slice inference from this theorem. The separate construction of that
theorem referenced outside the assigned inputs was not fetched or audited.

Here is the finite-dimensional intersection argument in full. Let \(M\)
be an embedded \(C^1\) manifold of dimension \(p\), and let \(S\)
be another embedded \(C^1\) manifold with \(\dim S\le p\). At a point
\(z\in M\cap S\), suppose

\[
V(z)\in T_zS,\qquad V(z)\notin T_zM.
\tag{2}
\]

Then \(T_zM\) cannot be a subspace of \(T_zS\). If it were, the
dimension bound would force \(\dim S=p\) and equality of the two
tangent spaces, contradicting (2). Locally write
\(S=\{g=0\}\), where \(g\) is a \(C^1\) submersion and
\(\ker Dg(z)=T_zS\). The failure of tangent inclusion means
\(D(g|_M)(z)\ne0\). At least one scalar component \(g_j|_M\)
therefore has nonzero differential. The implicit-function theorem makes
its zero set a \(C^1\) hypersurface of \(M\), and
\(M\cap S\subseteq\{g_j|_M=0\}\) locally. Such a hypersurface has
zero \(p\)-dimensional Lebesgue measure in local coordinates on \(M\).
Countably many coordinate neighborhoods cover the relevant intersection,
so that intersection is null in \(M\).

For the actual slice (1), the field is

\[
V(A,W,0)=(0,0,2H(A,W)y/m).
\tag{3}
\]

Consequently \(V\notin TM_0\) wherever \(Hy\ne0\). This is the
extra information that makes an index of exactly \(n\) sufficient;
dimension alone would not exclude an equal-dimensional intersection.
It is also why a theorem assuming a density on the full parameter space
is unnecessary here.

## 3. Pullbacks, nonisolated critical points, and countability

Loss dissipation gives

\[
-\dot{\mathcal L}=\|\dot A\|_F^2/n+
\|\dot W\|_F^2+\|\dot w\|^2/n.
\tag{4}
\]

On every finite interval the integral of squared speed in this constant
metric is finite. Cauchy--Schwarz gives
\(\|\theta(t)-\theta(s)\|_{D^{-1}}
\le\sqrt{(t-s)\mathcal L(0)}\). A finite maximal forward time would
therefore have a finite parameter limit, from which the smooth ODE could
be extended. Thus the forward flow \(\Phi_t\) exists globally.
For each fixed finite \(t\), uniqueness and differentiable dependence
make it a diffeomorphism onto its open image. No globally complete
backward flow is required.

Let \(S_*\) be one local center-stable manifold, restricted to a region
where it is embedded and the actual field is tangent. At a relevant
point of the finite-time pullback \(S=\Phi_t^{-1}(S_*)\),

\[
D\Phi_t(z)V(z)=V(\Phi_t(z))\in T_{\Phi_t(z)}S_*.
\tag{5}
\]

Hence \(V(z)\in T_zS\), and \(\dim S=\dim S_*\le N-n\).
Equations (2)--(3) show that \(S\cap M_0\) is slice-null wherever
\(Hy\ne0\).

This applies to all finite bad limits without taking an uncountable
union of null sets. Choose a sufficiently small open neighborhood for
each relevant critical point so that every forward trajectory staying
there lies in its associated center-stable manifold. These open sets
cover the relevant critical set. Euclidean space is second countable,
so a countable subfamily covers it. A trajectory converging to any point
of this critical set eventually remains in one of the chosen open
neighborhoods: that neighborhood contains its limit in its interior.
Choose an integer entrance time after which it remains there.
Countably many chosen neighborhoods, nonnegative integer entrance times,
and local intersection charts now cover all such initial conditions by
slice-null sets. Isolated critical points are not assumed.

The usual local-invariance qualification matters: (5) is used only where
the actual field is tangent to the chosen local manifold. Shrinking its
working neighborhood before the countable-cover construction provides
exactly this property. The assigned argument has this qualification and
does not require global invariance of an arbitrarily truncated chart.

## 4. Why the canonical Gaussian law avoids the exceptional slice sets

The independent Gaussian entries of \((A_0,W_0)\) give a density on
\(M_0\), so slice-null sets have probability zero. Also \(Hy\ne0\)
almost surely. To verify the latter separately, \(W_0\) is invertible
almost surely, since its determinant is a nonzero polynomial and its
entries have a joint density. Conditional on any such \(W_0\), the
matrix \(A_0X\) has a density on \(\mathbb R^{n\times m}\), because
each Gaussian row has covariance \(X^\top X\succ0\). The map

\[
Z\longmapsto\tanh(W_0\tanh Z)
\]

is a smooth diffeomorphism onto an open image: each entrywise tanh map
is a diffeomorphism onto its image, and multiplication by \(W_0\) is
invertible. Therefore \(H_0\) has a density. The condition \(H_0y=0\)
is a proper linear subspace of \(\mathbb R^{n\times m}\) for
\(y\ne0\), and is null under that density.

At zero readout,

\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|H_0y\|^2<0
\]

almost surely. Loss monotonicity then places every finite positive-loss
critical limit in \((0,\mathcal L_0)\), the interval covered by the
index theorem. Combining the preceding sections proves exactly the
finite-limit avoidance claim in the assigned files. The further
analytic convergence-or-escape theorem is a separate input and is not
needed for this slice argument.

## 5. Why one fewer negative direction leaves a real dimension gap

Put \(p=N-n=\dim M_0\). If only \(n-1\) unstable directions are
known, the center-stable dimension bound is

\[
\dim S\le N-(n-1)=p+1.
\tag{6}
\]

At a transverse slice point, the subspace

\[
T_zM_0\oplus\operatorname{span}\{V(z)\}
\tag{7}
\]

has dimension exactly \(p+1\). Thus (6) permits \(T_zS\) to equal
(7). In that case every local defining function of \(S\) has zero
differential when restricted to \(M_0\), and the implicit-function
argument in Section 2 supplies no hypersurface or null-set conclusion.

This is also compatible with loss geometry. The objective is constant
on \(M_0\), while its derivative along \(V\) is strictly negative at
the relevant initial points. A center-stable manifold of dimension
\(p+1\) can contain the slice as one constant-loss cross-section and
contain all its subsequent flow lines. Loss decrease does not create a
second independent tangent vector transverse to \(M_0\).

At any readout-stationary point of the canonical network,
\(Hr=0\), so

\[
r^\top f=\frac1n(Hr)^\top w=0,
\qquad r^\top y=r^\top(f-r)=-\|r\|^2.
\tag{8}
\]

Consequently \(r^\top y<0\) is automatic when the residual is nonzero.
It cannot serve as an additional nondegeneracy hypothesis on a positive-loss
critical point. The same orthogonality gives

\[
\|y\|^2=\|f\|^2+\|r\|^2,
\tag{9}
\]

so \(\mathcal L<\mathcal L_0\) is equivalent there to \(f\ne0\).
This is a scalar restriction on the critical point, not a tangent-space
restriction on its pullback stable set. Along the radial readout variation
\(w\mapsto(1+s)w\), the second loss derivative at such a point is
\(2\|f\|^2/m>0\), not an extra negative Hessian direction.

## 6. An explicit countermodel to the proposed geometric inference

The following analytic squared-loss example shows that the dimension gap
is not only a failed proof estimate. It satisfies the slice geometry,
strict initial loss decrease, a bad limit below initial loss, and the
negative residual-label pairing, yet its entire initialization slice
converges to equilibria with exactly \(n-1\) negative Hessian directions.
It is deliberately distinguished from the canonical tanh network: its
prediction is nonlinear in some coordinates designated as readout.
It disproves an inference from just the listed geometric and scalar
properties; it is not a counterexample within the canonical architecture.

Fix \(n\ge2\), any \(p\ge0\), hidden coordinates
\(u\in\mathbb R^p\), and coordinates \(w\in\mathbb R^n\). Use
ordinary Euclidean gradient flow and define

\[
f(w)=(w_1,w_2^2,\ldots,w_n^2),\qquad y=(1,\ldots,1),
\]
\[
\mathcal L(u,w)=\frac1n\left[(w_1-1)^2+
                 \sum_{j=2}^n(w_j^2-1)^2\right].
\tag{10}
\]

The initialization slice \(M_0=\{w=0\}\) has codimension \(n\),
zero prediction, and constant loss \(\mathcal L_0=1\). Its vector
field is \((0,2/n,0,\ldots,0)\), transverse to the slice. The exact
flow from every \((u_0,0)\) is

\[
u(t)=u_0,\qquad w_1(t)=1-e^{-2t/n},\qquad w_j(t)=0\quad(j\ge2).
\tag{11}
\]

Indeed the remaining equations are
\(\dot w_j=(4/n)w_j(1-w_j^2)\), which preserve zero. Thus every
point of \(M_0\), including any Gaussian law with a density on that
slice, converges to the finite equilibrium \((u_0,e_1)\). There,

\[
\mathcal L_*=(n-1)/n\in(0,1),\qquad
r_*=(0,-1,\ldots,-1),\qquad r_*^\top y=-(n-1)<0.
\]

The Hessian is diagonal, with \(p\) zero entries, one entry \(2/n\),
and \(n-1\) entries \(-4/n\). It therefore has exactly \(n-1\)
negative eigenvalues. Its local center-stable manifold is

\[
S=\{w_2=\cdots=w_n=0\},\qquad \dim S=p+1,
\]

and contains the entire slice \(M_0\). At its slice points,
\(TS=TM_0\oplus\operatorname{span}\{V\}\), realizing (7) exactly.

## 7. Scope of the conclusion

No gap was found in the assigned \(n\)-direction slice-avoidance
argument, conditional on the explicitly stated local center-stable
theorem. Exact zero readout is handled by slice transversality and
absolute continuity within the slice, not by a full-ambient-density
assertion.

An \(n-1\) index bound does not suffice for that argument, even after
adding the two proposed scalar inequalities. To obtain canonical avoidance
from a smaller index one would need a further property that excludes the
tangent containment \(TM_0\subset TS\), or another measure-zero argument
specific to the tanh network. Neither assigned file establishes such a
property. The countermodel in Section 6 shows why geometry and loss decrease
alone cannot substitute for it; it does not rule out a stronger theorem
using additional canonical structure.
