# Random-Averaging and Rare-Flux Machinery Audit

## Verdict

The broad proposal that a Gaussian matrix action restores integrability is
**false as a width-uniform operator statement**, already at the first
forward/transpose return.  Gaussian averaging does control a direction that
is independent of the relevant source, and it also controls the actual first
local-defect direction at initialization.  It does not control an adaptive
row-aligned direction, even when that direction has uniformly bounded
coordinate moments of every fixed order.

A narrower dyadic rare-flux/Duhamel construction remains mathematically
conceivable.  Its decisive leaf is a dynamic no-alignment estimate for the
actual defect-generated cone.  No argument presently proves that leaf
without regenerating the contracted Malliavin/response hierarchy.  Therefore
this proposal is not a genuine reduction of the compact-time bridge.

## 1. Exact tangent calculus

Write

\[
 q(s)=\phi'(s)=\frac1{1+s^2},\qquad
 c(s)=\phi''(s)=\frac{-2s}{(1+s^2)^2},
\]

and let `Q_l=diag(q(z_l))`, `C_l=diag(c(z_l))`.  For a
parameter perturbation

\[
 v=\delta u,\qquad a=\delta A,\qquad H_l=\delta G_l,
\]

the exact forward tangent recursion is

\[
 \zeta _1=v,\qquad \xi_l=Q_l\zeta_l,\qquad
 \zeta_{l+1}=H_lx_l+G_l\xi_l.                                      \tag{1}
\]

The exact backward recursion is

\[
 \beta_D=Q_Da+\operatorname{diag}(c_D\odot A)\zeta_D,               \tag{2}
\]

and, for `l<D`,

\[
 \rho_l=H_l^Tb_{l+1}+G_l^T\beta_{l+1},\qquad
 \beta_l=Q_l\rho_l+\operatorname{diag}(c_l\odot r_l)\zeta_l.       \tag{3}
\]

Consequently the linearized flow is

\[
 \dot a=\xi_D,\qquad
 \dot H_l=\frac{\beta_{l+1}x_l^T+b_{l+1}\xi_l^T}{n},\qquad
 \dot v=\beta_1.                                                    \tag{4}
\]

The compatible tangent energy is

\[
 \|(v,a,H)\|_{\mathsf E}^2
 =\|v\|_{2,n}^2+\|a\|_{2,n}^2+\sum_l\|H_l\|_F^2.                  \tag{5}
\]

The matrix Frobenius norm in (5) is deliberately unnormalized: an update
`n^{-1}bx^T` has order-one Frobenius norm and order-one action on a vector of
normalized order one.

## 2. Exact return-operator compression

Define

\[
 P_1=I,\qquad P_k=G_{k-1}Q_{k-1}\cdots G_1Q_1\quad(k\ge2),
\]

and put `r_D=A`.  Holding all parameters other than `u` fixed, repeated
application of (1)--(3) gives the exact identity

\[
 D_ub_1=\sum_{k=1}^D
 P_k^T\operatorname{diag}(c_k\odot r_k)P_k.                         \tag{6}
\]

Thus the dangerous curvature is not an arbitrary dense matrix.  It is a sum
of weighted source-return operators `P^T D P`.  In particular,

\[
 D_ub_1=
 \operatorname{diag}(c_1\odot r_1)
 +Q_1G^T\operatorname{diag}(c_2\odot A)GQ_1                       \tag{7}
\]

at depth two, while at depth three the new deepest term is

\[
 Q_1G_1^TQ_2G_2^T\operatorname{diag}(c_3\odot A)
 G_2Q_2G_1Q_1.                                                      \tag{8}
\]

The middle depth-three term has the same form with
`diag(c_2 odot r_2)`.  These formulas identify precisely what a random-
averaging theorem would have to bound.

## 3. What Gaussian averaging really proves

At initialization, conditional on the forward variables and hidden
matrices, every `r_l` is linear Gaussian in `A`.  On the usual bounded
operator-norm event, each coordinate of

\[
 d_l=c_l\odot r_l
\]

has bounded conditional variance.  Conversely, a positive fraction of the
coordinates have conditional variance bounded away from zero, so their
maximum is naturally of order `sqrt(log n)`.

For a fixed direction independent of `A`, this maximum does not determine
the averaged return.  For example, in (7), write

\[
 p_i=Q_1G^Te_i,\qquad y=GQ_1v.
\]

Then the second return applied to `v` is

\[
 R_2v=\sum_i A_i c_{2,i}y_i p_i,
\]

and conditional Gaussian orthogonality gives

\[
 \mathbb E_A\|R_2v\|_2^2
 =\sum_i c_{2,i}^2y_i^2\|p_i\|_2^2
 \le C\|v\|_2^2.                                                   \tag{9}
\]

The corresponding depth-three middle return is controlled by the
conditional covariance

\[
 K=G_2^TQ_3^2G_2,
\]

whose operator norm is bounded on the same localization.  The deepest
return is handled directly using independence of the coordinates of `A`.

There is also a useful result for the actual initialization drift.  Given
the forward variables, `b_1=LA` for a bounded matrix `L`.  Each return applied
to `b_1` is a quadratic Gaussian expression of the form

\[
 P^T\big[(RA)\odot(MLA)\big].
\]

Wick's fourth-moment identity, row-norm bounds, and normalized summation give

\[
 \mathbb E\|D_ub_1\,b_1\|_{2,n}^2\le C_D.                          \tag{10}
\]

The remaining blocks of the first acceleration admit the same finite
Gaussian-pairing estimate.  Hence the first local truncation coefficient at
`t=0` is uniformly square-integrable at depths two and three.  This is a
real positive fact, but it concerns a very special causal direction at one
time.

## 4. Exact hostile adaptive direction

Let `R=P^TD_dP` be any return term for which a coordinate `I` satisfies
`d_I>0` and `d_I` is of order `sqrt(log n)`.  Choose

\[
 v=\sqrt n\,P^Te_I.                                                 \tag{11}
\]

For a Gaussian source product `P`, the coordinates of (11) are order one;
thus every fixed empirical `L^p` norm of `v` is bounded.  Yet

\[
 (Pv)_I=\sqrt n\,\|P^Te_I\|_2^2\asymp\sqrt n.
\]

The `I`-term in `Rv` consequently has normalized size of order `d_I`, while
the off-diagonal row-inner-product contribution is only order one in
probability.  Therefore

\[
 \frac{\|Rv\|_{2,n}}{\|v\|_{2,n}}
 \gtrsim\sqrt{\log n}                                               \tag{12}
\]

with high probability.  The witness applies already to (7), and also to
the deepest term (8).  Coordinate `L^p`, Orlicz, and subgaussian envelopes
do not exclude it: it is coordinate-delocalized but source-row-aligned.

The same obstruction appears in the exact Gaussian divergence identity.  If
`X=sqrt(n)G`, then

\[
 (Gv)_i=\delta_i(v/\sqrt n)
 +\frac1{\sqrt n}\sum_jD_{ij}v_j.                                  \tag{13}
\]

Only the divergence term averages.  For the adapted choice `v_j=X_{ij}`,
the contraction term in (13) equals `sqrt(n)`, although
`\|v\|_{2,n}` is order one.  Alternating forward/transpose actions iterate
this contraction.  Any honest averaging calculus must explicitly retain
the contracted response information.

## 5. The only surviving refinement: a rare-flux norm

A conceivable multiscale state records not just the size of a tangent, but
how much of it enters rows with a large curvature coefficient.  Let

\[
 a_{l,i}=\sup_{t\le T}|c_l(z_{l,i}(t))r_{l,i}(t)|,
 \qquad
 S_{l,k}=\{i:2^k\le a_{l,i}<2^{k+1}\}.
\]

A schematic rare-flux energy is

\[
 \|\delta\theta\|_{\mathsf{RA},T}^2
 =\|\delta\theta\|_{\mathsf E}^2
 +\sum_{l,k}e^{CT2^k}
   \|\mathbf1_{S_{l,k}}\zeta_l\|_{2,n}^2.                          \tag{14}
\]

If the rare sets have Gaussian cost `exp(-c4^k)` and all causal incoming
directions put the same order of energy into them, then the dangerous
amplification is summable because

\[
 \sum_ke^{CT2^k-c4^k}<\infty.                                      \tag{15}
\]

This permits repeated residence in one bad row; it does not falsely claim a
fresh independent Gaussian gain at every return.

The construction would require the following leaves.

1. **Triangular primal envelope.**  This follows from bounded `arctan`, the
   linear growth of `A`, and downstream-to-upstream operator-norm estimates.
   It controls global normalized energies but does not forbid coordinate
   condensation.
2. **Static restricted averaging.**  Equation (9) and its depth-three
   analogues prove this for independent or conditionally Gaussian
   directions.  Equation (11) disproves it for arbitrary adapted directions.
3. **Frozen dyadic Duhamel bound.**  Near-orthogonality of Gaussian rows and
   (15) give a plausible block estimate once the flux premise below is
   available.  This is a concrete route, not yet a proved leaf.
4. **Dynamic tail bound.**  One needs a uniform tail for
   `sup_{t<=T}|d_{l,i}(t)|`.  Initialization is conditionally Gaussian;
   positive-time dependence on `A` prevents repeating that conditioning.
5. **Dynamic no-alignment.**  For every actual local-defect/Duhamel direction
   `V`, one needs a bound of the form

   \[
   \mathbb E\|\mathbf1_{S_{l,k}}P_lV\|_{2,n}^2
   \le C_Te^{-c4^k}\mathbb E\|V\|_{\mathsf E}^2,                  \tag{16}
   \]

   with at most `C^m sqrt(m!)` growth after `m` returns.  Time-simplex
   volume would then sum the Duhamel series.
6. **Slow motion of rare row spaces.**  Rowwise,

   \[
   \|\dot g_{l,i}\|_2
   =\frac{|b_{l+1,i}|}{\sqrt n}\|x_l\|_{2,n}.
   \]

   This is useful only after the dynamic coordinate tails and no-alignment
   estimate are known.
7. **Euler comparison.**  Once 3--6 hold, variation of constants gives the
   needed local consistency and stable accumulation.  This last passage is
   routine relative to (16).

## 6. Kill-gate decision

The master estimate (16) is false for arbitrary adapted vectors by (11).
Restricting it to the causal defect cone is mathematically sensible, but
Gaussian integration by parts converts it into the contraction term (13).
Differentiating that contraction generates the next contracted response and
so on.  No finite rule or summable hierarchy estimate has been established.

Therefore:

- fixed-direction averaging at initialization is **proved**;
- the actual first local-defect coefficient at initialization is uniformly
  square-integrable at depths two and three;
- width-uniform random averaging as an operator property is **falsified**;
- the rare-flux construction is a precise **conditional** architecture;
- its dynamic no-alignment leaf is presently equivalent in difficulty to
  the original reachable-tangent bridge.

The random-averaging route is consequently rejected as a completed or
strictly easier calculus.  The return identity (6) and the distinction
between independent and row-aligned directions remain valuable design
constraints for any later machinery.
