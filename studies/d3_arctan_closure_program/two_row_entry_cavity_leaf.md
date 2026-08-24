# The two-row/one-entry feeding leaf

This note uses only the normalized finite-width algebra.  It isolates the
first term in the mixed row--entry cavity response whose moment growth is
`p^(3/2)`, even after exact centering and after retaining the learned row.

## Normalization and cavity variables

Use

\[
 \langle u,v\rangle_n=n^{-1}\sum_{j=1}^n u_jv_j,
 \qquad (b\otimes x)u=b\langle x,u\rangle_n,
\]

and write a bare top row as

\[
 G_r=n^{-1/2}(g_{r1},\ldots,g_{rn}),\qquad g_{rj}\stackrel{\rm iid}{\sim}N(0,1).
\]

Fix two distinct top rows `r != s` and an entry `e=(s,l)`.  Let `Delta_e`
be the finite difference obtained by replacing this entry, and let
`Delta_r` be the whole-row cavity difference.  In the two-row cavity,

\[
 x=X_2^k,\qquad \delta x=\Delta_e X_2^k
\]

are measurable before row `r` is inserted.  In particular they are
independent of `g_r` and of the endpoint mark `A_r^0`.  Put

\[
 \alpha=\|\delta x\|_n,
 \qquad G_1={G_r\delta x\over\alpha}\quad(\alpha>0).
\]

Conditionally on the two-row cavity, `G_1` is standard normal.  The
single-entry response has its natural accumulated scale

\[
 \|\delta x\|_{L^p(\|\cdot\|_n)}\lesssim {C_T\,\mathrm{poly}(p)\over n};       \tag{1}
\]

the newest Euler contribution alone is `O(h/n)`, but after `T/h` steps the
old, accumulated part is `O(1/n)`.

For row `r`, write `W_r=G_r+P_r`, `z_r=W_rx`, and `B_r=A_rd(z_r)`.  The
exact finite difference of its contribution to `R_2=W^*B` is

\[
\begin{split}
 \Delta_e(W_{rj}B_r)
  ={}&W_{rj}A_r\{d(z_r+\delta z_r)-d(z_r)\}\\
    &+W_{rj}(\Delta_eA_r)d(z_r+\delta z_r)
      +(\Delta_eP_{rj})(A_r+\Delta_eA_r)d(z_r+\delta z_r),                 \tag{2}\\
 \delta z_r={}&W_r\delta x+(\Delta_eP_r)(x+\delta x).
\end{split}
\]

Thus all learned and covariance terms are explicitly present in (2).  Split
the first gate difference at `z_r+G_r delta x`.  Its bare feeding leaf is

\[
 L_{r,e,j}
 ={g_{rj}\over\sqrt n}\,A_r
 \bigl[d(Z+\alpha G_1)-d(Z)\bigr],                                      \tag{3}
\]

where `Z` contains the old bare field and the learned shift.  The remainder
contains either `Delta_e P_r`, `Delta_e A_r`, or a learned outer factor; it
does not cancel (3), because (3) is the part linear in the bare off-column
coordinate of row `r`.

## Orthogonal-coordinate decomposition

Orthogonalize the row Gaussian against the two directions spanned by `x`
and `delta x`.  For a lower coordinate `j`,

\[
 g_{rj}=\beta_{0j}G_0+\beta_{1j}G_1+\sigma_jG_2,
 \qquad G_2\perp (G_0,G_1),                                             \tag{4}
\]

with

\[
 \beta_{0j}={x_j\over\sqrt n\|x\|_n},\qquad
 \beta_{1j}={\delta x_j^\perp\over\sqrt n\|\delta x^\perp\|_n},
 \qquad \sigma_j^2=1-\beta_{0j}^2-\beta_{1j}^2.                         \tag{5}
\]

For an off-column coordinate, `sigma_j` is bounded below.  The genuinely
off-column part of (3) is therefore

\[
 L_{r,e,j}^{\perp}
 ={\sigma_j\over\sqrt n}A_rG_2
 \bigl[d(Z+\alpha G_1)-d(Z)\bigr].                                     \tag{6}
\]

It is **already exactly centered** over `G_2`:

\[
 \mathbb E_{G_2}[L_{r,e,j}^{\perp}\mid G_0,G_1,A_r,\mathcal C]=0.         \tag{7}
\]

Consequently no Stein compensator removes (6).  The `beta_1 G_1` part of
(4) does have a Stein compensator.  From

\[
 |\mathbb E\{G_1[d(Z+\alpha G_1)-d(Z)]\}|
 \le C\min(\alpha,1)                                                    \tag{8}
\]

its compensator has size at most

\[
 {C\over\sqrt n}\,|A_r|\min(\alpha,1),                                  \tag{9}
\]

which is `C sqrt(p)/n^(3/2)` when `alpha <= C/n`.  Thus the deterministic
compensator is not the obstruction.

## Sharp moment of the centered leaf

The exact divided-difference estimate gives

\[
 \|A_rG_2[d(Z+\alpha G_1)-d(Z)]\|_p
 \le C_T\min\{\alpha p^{3/2},p\}.                                      \tag{10}
\]

Hence

\[
 \boxed{\quad
 \|L_{r,e,j}^{\perp}\|_p
 \le {C_T\over\sqrt n}\min\{\alpha p^{3/2},p\}.
 \quad}                                                                \tag{11}
\]

Using the accumulated entry scale `alpha <= C_T/n`, the small-innovation
branch is

\[
 \|L_{r,e,j}^{\perp}\|_p
 \lesssim {C_Tp^{3/2}\over n^{3/2}},
 \qquad p\lesssim c n^2.                                                \tag{12}
\]

This is sharp, not merely a Holder loss.  Indeed take an early slab on
which the learned row is negligible, choose `delta x` orthogonal to `x`,
and restrict the independent old field to an interval on which
`|d'(Z)| >= c_0`.  If `alpha sqrt(p) <= c`, the mean-value theorem gives

\[
 |d(Z+\alpha G_1)-d(Z)|\ge c\alpha|G_1|
\]

on a fixed-fraction part of the Gaussian `p`-moment region.  Since
`A_r^0`, `G_1`, and `G_2` are independent there,

\[
 \|L_{r,e,j}^{\perp}\|_p
 \ge {c\alpha\over\sqrt n}
       \|A_r^0G_1G_2\|_p
 \ge {c\alpha p^{3/2}\over\sqrt n}.                                   \tag{13}
\]

The learned-cancellation budget

\[
 |(P_2^kx_k)_r|\le C_T(1+|A_r^0|)                                      \tag{14}
\]

controls the saturated branch in (10), and prevents an additional carrier
from being generated by the learned shift.  It does not alter (13): on the
small-innovation branch the gate is being differentiated in `G_1`, while
the independent off-column carrier `G_2` and the endpoint mark remain.

The square-function calculation makes the failure transparent.  From (7),
the one-atom conditional square function is

\[
 {\sigma_j\over\sqrt n}|A_r|
 |d(Z+\alpha G_1)-d(Z)|.                                                \tag{15}
\]

Its `L^p` norm is of order `alpha p/sqrt(n)` (the product `A_r G_1`).  The
Gaussian/martingale factor `sqrt(p)` then yields exactly
`alpha p^(3/2)/sqrt(n)`.  Centering has already been used and cannot turn
this into `sqrt(p)`.

## Euler factors and why the old part is decisive

When (6) is inserted into the next lower-layer Euler update it carries one
factor `h`.  The newest piece of the entry response has
`alpha_new = O(h/n)`, so a single newest--newest leaf is

\[
 O\left({h^2p^{3/2}\over n^{3/2}}\right).                               \tag{16}
\]

Those genuinely chronological pieces may be put in a square function and
are harmless.  But at time `k`, `Delta_e X_2^k` also contains the old sum

\[
 \delta x_k=h\sum_{s<k}J_{k,s}u_s,
 \qquad \|\delta x_k\|_n=O_T(n^{-1}).                                   \tag{17}
\]

The leaf generated by this old part is only multiplied by the current
outer `h`.  Over `T/h` updates,

\[
 h\sum_{k<T/h}L_{r,e,j}^{\perp,k}
\]

has no residual `h`: all summands reuse the same endpoint mark and the same
off-column row carrier.  They are not martingale differences in `k`.
Consequently their sharp scale remains

\[
 {C_Tp^{3/2}\over n^{3/2}},                                             \tag{18}
\]

whereas the proposed estimate is `C_T sqrt(p)/n^(3/2)`.

The rank-one learned correction and the `rho_2 B_3` covariance correction
cancel the self-curvature part of the top characteristic.  They do not
cancel (6): (6) is the bath/off-row feeding term `G_r delta x`, and its
`G_2` projection is orthogonal to every scalar covariance compensator.
Equivalently, it is the finite-difference version of the off-diagonal
commutator left after characteristic dressing.

## Conclusion

The desired `C_T sqrt(p)/n^(3/2)` weighted off-column bound does not follow
from two-row cavity, exact gate identities, and the rowwise learned budget.
The first exact obstruction is (6).  It is centered already, its
compensator is zero, and its conditional square function contains the
product of the endpoint mark and the gate-driving Gaussian.  Its sharp
moment is `p^(3/2)/n^(3/2)` on the accumulated entry scale.  A proof needing
the smaller `sqrt(p)` scale must exploit an additional cancellation across
the *old* row carrier (not chronological centering of newest pieces), or
must weaken the target to a Bernstein/psi_(2/3) bound.
