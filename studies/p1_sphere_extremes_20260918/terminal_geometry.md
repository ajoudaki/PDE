# Frozen terminal-geometry candidate

Status: internally derived candidate, frozen on 2026-09-18 before route comparison. This is not promoted material. No experiment was run.

The assigned scientific inputs were read in their stated scope: all of `docs/observable_p1.md`; C.4.7.9.3–4 and the model/existence material of C.4.7.10.D.3 in `docs/global_nonlinear.md`. The required investigate-conjectures and solve-math-rigorously skills, including the research-contract and adversarial-audit references, were used. No other study, route, review, or history was read.

## Contract and conclusions

The object is the exact canonical order-one, dimension-three population flow with the prescribed Gaussian-derived marks, ridge `eta=1/4096`, `w(0)=g`, `c(0)=0`, `M(0)=D`, actual transpose, all three trainable blocks, and unhalved physical square loss. Inputs below are the normalized directions `u=x/sqrt(3)` on the unit sphere. Population expectations are exact. There is no quadrature, width, or time-step limit in these claims.

Two conclusions are proved below.

1. For three linearly independent directions, a precise algebraic criterion characterizes singularity of the **full** prediction differential at every finite fitting state in the initialized odd sector. A singular readout Gram alone does not suffice: the lower reverse responses impose additional conditions.
2. For the explicitly prescribed initialized family
   `u_i=y_i e_i`, `mu_i=1/3`, `y_i in {+1,-1}`, the physical loss has a strictly exponential terminal asymptotic and tends to zero. Thus this class cannot exhibit a positive-loss asymptotic stall or polynomial terminal loss decay. Mixed labels are allowed, but three equal weights do not give exactly balanced label mass. An antipodally paired six-atom version is balanced and has exactly the same flow.

No negative family for the original initialization is claimed. Reachability of the singular fitting configurations classified below, outside the symmetric family, remains open here. No arbitrary ambient stationary state is offered as an initialized counterexample.

## Exact equations and the full singularity criterion

The canonical sign-paired invariant sector permits removing the inactive constant coordinates exactly. Write lower marks `b_1 in R^6`, upper marks `b_2 in R^3`, and `M in R^(3 x 6)`. This is only a representation of the full equations; every nonconstant entry of `M` remains trainable. For three training inputs define

\[
\begin{gathered}
 h_{1i}=\tanh(w\cdot u_i),\quad a_i=E_1[b_1h_{1i}],\quad
 v_i=Ma_i,\quad h_i=\tanh(b_2\cdot v_i),\quad f_i=E_2[ch_i],\\
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_i)],\quad
 q_i=b_1^TM^Td_i.
\end{gathered}
\]

The physical metric is the lower and upper population `L2` metric plus the matrix Frobenius metric. Consequently

\[
 \nabla f_i=
 \bigl(\operatorname{sech}^2(w\cdot u_i)q_i u_i,
       h_i,d_i a_i^T\bigr),\qquad
 \theta'=-2\sum_i\mu_i(f_i-y_i)\nabla f_i.
\tag{1}
\]

Here a finite state means `w-g` and `c` are bounded and `M` is finite; these properties hold at every finite physical or feature-clock time considered below. The full constant-coordinate formulation has the same gradients: the constant entries of `a_i,d_i` vanish, and the omitted matrix-gradient row and column are zero. Thus the criterion is also a criterion in the original full state metric.

The normalized nonconstant lower Gram is positive definite. Indeed the unnormalized pair `(h,k)` in each coordinate has positive definite covariance: conditional on `G`, the independent reverse Gaussian gives `k` a nondegenerate conditional distribution, so no nonzero linear combination of `h` and `k` vanishes almost surely. Different coordinate pairs are independent and centered; the Cholesky transformation is invertible. In particular,

\[
 q_i=0\quad\hbox{almost surely}\quad\Longleftrightarrow\quad M^Td_i=0.
\tag{2}
\]

Assume `u_1,u_2,u_3` are linearly independent. Then a vector `lambda in R^3` lies in the nullspace of the adjoint prediction differential if and only if all three conditions hold:

\[
\begin{split}
 &\sum_i\lambda_i\tanh(b_2\cdot v_i)=0\quad\text{almost surely},\\
 &\lambda_i M^Td_i=0\quad\text{for each }i,\\
 &\sum_i\lambda_i d_i a_i^T=0.
\end{split}
\tag{3}
\]

To verify necessity of the middle line, the lower component of `sum lambda_i grad f_i` is zero pointwise. Linear independence of the three `u_i` forces each scalar coefficient `lambda_i sech^2(w.u_i)q_i` to vanish. The lower gate is strictly positive because `w.u_i` is finite almost surely, and (2) then applies. The other two lines are exactly the upper and matrix components of (1). These arguments also prove sufficiency. For positive training weights, the weighted full prediction kernel is singular exactly when (3) admits a nonzero vector.

### Exact readout dependence for three inputs

The upper mark law has positive density on the open cube `(-1/c_0,1/c_0)^3`, where `c_0=sqrt(tau+eta)` is the normalization constant, not the trainable readout. For at most three nonzero vectors `v_i`, the functions `tanh(b.v_i)` are linearly independent except for signed duplicates `v_i=+/-v_j`.

Here is a contained proof. Group the vectors modulo sign and choose representatives `z_1,...,z_k`, `k<=3`. Choose a vector `e` outside the finite union of hyperplanes on which `e.z_j=0` or `e.z_j=+/-e.z_l`. Thus `t_j=e.z_j` are nonzero with pairwise distinct squares. An almost-sure linear dependence is an identity on the open cube by continuity and positive density. Restrict to `b=te` near zero. The first, third, and fifth Taylor coefficients of `tanh`, namely `1,-1/3,2/15`, give the first `k` equations

\[
 \sum_{j=1}^k A_j t_j^{2n+1}=0,
 \qquad 0\le n<k.
\]

The matrix is a Vandermonde matrix in `t_j^2` times a nonzero diagonal matrix, so all `A_j` vanish. Conversely signed duplicates give the stated dependencies. Zero `v_i` give zero readout functions; at fitting with `y_i=+/-1` they are impossible.

### All possible singular fitting configurations

At a fitting state define the oriented vectors and coefficients

\[
 t_i=y_i v_i,\qquad A_i=y_i a_i.
\]

A signed collision can occur at fitting only with consistent labels: if `v_i=s v_j`, then `f_i=s f_j`, so `y_i=s y_j`. Consequently the readout dependence groups are exactly the equality groups among `t_i`. Within each group, `d_i=d` and `q_i=q`, since the upper gate is even. Set `xi_i=y_i lambda_i`. Criterion (3) becomes

\[
 \sum_{i\in G}\xi_i=0\quad\text{for each equality group }G,
 \qquad \xi_i M^Td_i=0,
 \qquad \sum_i\xi_i d_i A_i^T=0.
\tag{4}
\]

This gives a complete finite fitting-state classification for three independent inputs:

- If `t_1,t_2,t_3` are distinct, the full kernel is positive definite.
- If precisely `t_1=t_2` while `t_3` differs, the full kernel is singular exactly when
  \[
    M^Td=0,\qquad d(A_1-A_2)^T=0.
  \]
  Equivalently, either `d=0`, or both `A_1=A_2` and `M^Td=0` hold. The possible nullspace is the single signed contrast of inputs 1 and 2.
- If all three `t_i` coincide, a singularity requires `M^Td=0`. If additionally `d=0`, the nullspace consists of all `xi` with zero sum and has dimension two. If `d!=0`, the nullspace consists of the simultaneous solutions
  \[
     \sum_i\xi_i=0,\qquad \sum_i\xi_i A_i=0;
  \]
  it is nontrivial exactly when the three `A_i` are affinely dependent.

If `M` has full row rank, the condition `M^Td=0` is equivalent to `d=0`, simplifying the last two cases. These are exact geometric criteria, not reachability theorems.

## A prescribed initialized class with no stall or polynomial terminal decay

Fix any `y_i in {+1,-1}`, and set

\[
 u_i=y_i e_i,\qquad \mu_i=\tfrac13,\qquad x_i=\sqrt3u_i.
\tag{5}
\]

The inputs are three linearly independent unit directions. Oddness in the input gives `f(y_i e_i)=y_i f(e_i)` at every state in this architecture. Hence the loss and its entire full gradient for (5) agree exactly with those for three equally weighted examples `(e_i,+1)`. This label absorption changes neither initialization nor dynamics.

The initialized joint marks are invariant under simultaneous coordinate permutations, and `D=[d_h I_3,d_k I_3]`. The transformed data law on `e_1,e_2,e_3` is permutation invariant. Applying a permutation to lower marks and vector coordinates, upper marks, and the corresponding row/column blocks of `M` preserves the equations and initial state. Uniqueness therefore gives

\[
 f(e_1)=f(e_2)=f(e_3)=F,
 \qquad F(\theta)=\frac13\sum_i f(e_i),
 \qquad \mathcal L=(1-F)^2.
\tag{6}
\]

All gradients here remain the gradients in the complete population/Frobenius metric. Define

\[
 m=\frac13\sum_i h_i,\qquad F=E_2[cm],\qquad
 \kappa=\|\nabla F\|^2.
\]

Equation (1), restricted to the invariant trajectory, is exactly

\[
 \frac{d\theta}{dt}=2(1-F)\nabla F.
\tag{7}
\]

Introduce the independently solved gradient-ascent clock

\[
 \frac{d\theta}{ds}=\nabla F,\qquad\theta(0)=(g,0,D).
\tag{8}
\]

This is a change of scalar clock along the same full trajectory, not a frozen-layer model. Along (8),

\[
 \frac{dF}{ds}=\kappa\ge\|m\|_2^2,
 \qquad \frac{dc}{ds}=m,
 \qquad \frac{d\|c\|_2^2}{ds}=2F.
\tag{9}
\]

### Finite-clock continuation

The normalized feature synthesis maps are contractions, since their Grams are Cholesky normalizations of the unnormalized Grams with a strictly positive ridge. Therefore `||a_i||<=1`, `||d_i||<=||c||_2`. Let `B_1=sup|b_1|<infinity`. On a feature-clock interval `[0,S]`, equation (8) gives directly

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|\le\|D\|+s^2/2,
\]
\[
 \|w(s)-g\|_\infty
 \le B_1\left(\|D\|s^2/2+s^4/8\right).
\tag{10}
\]

Indeed the readout speed is at most one; the matrix speed is at most `||c||_2<=s`; and the lower speed is at most `B_1||M||s`, because each input has unit norm and each gate is bounded by one. The vector field in (8) is locally Lipschitz in these bounded-increment/readout/Frobenius norms by the same bounded-feature argument as the assigned existence source. Bounds (10) prevent finite-clock escape. Its bounded speeds give a Cauchy endpoint at any finite prospective terminal clock, and the local contraction construction restarts it. Thus (8) exists through every finite `s`, in particular throughout any interval on which `F<=1`.

### Strictly positive initial movement

For input `e_i`, the only nonzero initialized lower coefficients are

\[
 a_{h_i}=v/a,
 \qquad a_{k_i}=\frac{\beta\eta}{(v+\eta)b}.
\]

Here `v,a,b,beta,eta` are exactly the constants from `docs/observable_p1.md`. The second displayed coefficient follows by subtracting the normalized lower projection. Moreover `beta>0`: conditional on `G`, the function
`E_Z tanh(alpha tanh(G)+sqrt(tau) Z)` is odd and strictly increasing in `tanh(G)` and has the same sign as it. The expectation of its product with `tanh(G)` is therefore positive. The initialized upper vector is consequently

\[
 v_i(0)=\ell e_i,\qquad
 \ell=d_h(v/a)+d_k\frac{\beta\eta}{(v+\eta)b}>0.
\]

Thus `h_i(0)=tanh(ell b_{2i})` are independent centered nonzero random variables. It follows that

\[
 \kappa(0)=\|m(0)\|_2^2
 =\tfrac13 E_2\tanh^2(\ell b_{21})>0.
\tag{11}
\]

The other gradient blocks vanish initially because `c=0`; this is the prescribed initialization, not a changed one. Equation (11) gives `F(s)>0` for every sufficiently small positive `s`, and monotonicity in (9) keeps it positive thereafter.

### Fitting occurs at a finite feature clock

Suppose for contradiction that `F(s)<1` for all `s`. Pick a small `s_0>0` and write `F_0=F(s_0)>0`. Equation (9) and `F<=1` give

\[
 \|c(s)\|_2^2=2\int_0^sF(\sigma)d\sigma\le2s.
\]

Cauchy–Schwarz applied to `F=<c,m>` then gives, for `s>=s_0`,

\[
 F'(s)=\kappa(s)\ge\|m(s)\|_2^2
 \ge\frac{F(s)^2}{\|c(s)\|_2^2}
 \ge\frac{F_0^2}{2s}.
\tag{12}
\]

The denominator is nonzero because `F(s)>0`. Integrating (12) gives
`F(s)>=F_0+(F_0^2/2)log(s/s_0)`, contradicting `F<1`. Hence a finite first clock `s_*` satisfies `F(s_*)=1`. Up to that clock `F` is strictly increasing, and the endpoint is finite by (10). At fitting,

\[
 \kappa_*:=\kappa(s_*)\ge\|m(s_*)\|_2^2
 \ge\frac1{\|c(s_*)\|_2^2}>0.
\tag{13}
\]

In particular the scalar direction visited by this trajectory is regular, regardless of whether unvisited contrast directions of the full kernel are singular.

### Exact physical terminal rate

For `0<=s<s_*`, set

\[
 t(s)=\int_0^s\frac{d\sigma}{2(1-F(\sigma))}.
\tag{14}
\]

On finite bounded state regions, bounded derivatives of tanh make the vector field and `F` twice continuously differentiable in the stated norms. By (13),

\[
 1-F(s)=\kappa_*(s_*-s)+O((s_*-s)^2).
\tag{15}
\]

Therefore `t(s)` increases to infinity as `s` tends to `s_*`. Its inverse solves `ds/dt=2(1-F)`, and (7) plus uniqueness identify it with the original physical flow. In particular the original physical flow converges to the finite fitting endpoint; it cannot stall at positive loss.

Let `q(t)=1-F(s(t))`. Differentiating gives

\[
 q'(t)=-2\kappa(s(t))q(t).
\]

Equation (15) and local Lipschitz continuity of `kappa` imply
`integral_0^infinity |kappa(s(t))-kappa_*|dt<infinity`: near the endpoint, substitute `dt=ds/[2(1-F)]`, whose denominator is comparable to `s_*-s`, while the numerator is at most a constant times `s_*-s`. Thus there is a finite strictly positive constant `C` such that

\[
 1-F(t)=C e^{-2\kappa_*t}(1+o(1)),\qquad
 \mathcal L(t)=C^2e^{-4\kappa_*t}(1+o(1)).
\tag{16}
\]

The entire state converges at least as fast as `O(e^{-2 kappa_* t})` in the bounded-increment/readout/Frobenius norms, since the feature-clock speed stays bounded and `s_*-s(t)` is comparable to `q(t)`. This excludes polynomial terminal loss decay for (5), rather than merely proving a positive initial rate or fitting on compact intervals.

An exactly balanced law is obtained by replacing each `(u_i,y_i)` in (5) by the two atoms `(u_i,y_i)` and `(-u_i,-y_i)`, each with mass `1/6`. Oddness makes each antipodal pair contribute the same square loss and gradient. This version has six atoms on three independent unoriented lines; it should not be represented as a balanced three-atom example.

## Audit and remaining obligations

- **Exact initialized conclusion:** (16) holds for the signed coordinate-axis family (5). All blocks evolve with the actual transpose and physical unhalved metric.
- **Exact geometric conclusion:** (3)–(4) classify singular full fitting differentials at finite states for any three independent inputs in the initialized odd sector. A vanishing or repeated upper feature alone does not establish a singular full kernel.
- **Reachability gap:** no argument here shows that any of the singular fitting configurations outside (5) is reached from the canonical initialization. They are not counterexamples.
- **Geometry limitation:** the symmetry proof uses the actual signed-coordinate/permutation symmetries of the canonical order-one marks. It does not assert general rotational invariance, and does not extend (16) to arbitrary rotated orthogonal triples.
- **Weight limitation:** unequal three-atom weights generally destroy the scalar-residual reduction. The exactly balanced three-atom case is not covered.
- **Asymptotic limitation:** (16) does not provide a uniform positive lower bound on rates over other admissible geometries, nor exclude long transients before the terminal regime.
- **Full-kernel limitation:** the axis endpoint has a regular visited scalar direction. Its full contrast-kernel rank need not be resolved for the proved rate and is not claimed here.
- **Scope limitation:** no claim is made about the neural-width limit, higher closure order, numerically approximated populations, or general target-law fitting.

Possible routes to a negative initialized terminal example include a reachability argument for a singular fitting geometry with a residual component in its degenerate direction, a rigorously controlled escaping trajectory that prevents fitting, or a bounded trajectory approaching a nonfitting critical state. This list is not an exhaustive classification. The current report supplies none of these examples and does not infer them from ambient-state constructions.
