# Gate-Resolved Increment Calculus

## Status

This note isolates an exact finite-increment identity that is stronger than
ordinary Euler linearization.  It is a genuine reusable peeling rule for a
network whose layer inputs are held fixed during one block.  It is **not** a
depth-three convergence theorem: the moving-input commutator and the final
reconstraint map are the two gates under audit.

The rule is useful because it propagates the integrated backpropagated
signal, which is `O(h)` in normalized energy, rather than differentiating a
gate against an instantaneous unbounded signal.

## 1. Mobility and notation

Let

\[
 m(s)=\phi'(s)>0,
 \qquad
 \Phi(s)=\int_0^s\frac{dr}{m(r)},
 \qquad
 J=\Phi^{-1},
 \qquad
 \chi=\phi\circ J.
\]

For `z_l` put `W_l=Phi(z_l)`.  Let `q_l=||x_l||_n^2` and set
`q_0=1`.  For a vector `S` and `q>=0`, define the mobility divided
difference

\[
 \mathfrak D_qJ(W,S)
 =
 \begin{cases}
 [J(W+qS)-J(W)]/q,&q>0,\\
 J'(W)S,&q=0.
 \end{cases}
\tag{1}
\]

The operations in (1) are coordinatewise.  The `q=0` value is the continuous
extension, so no inverse feature-Gram assumption is needed.

## 2. Exact paired-edge identity

Fix an input vector `x` and let an edge be driven by an arbitrary absolutely
continuous covector path `c(t)`.  If

\[
 \dot G=c\otimes_nx,
 \qquad
 a(t)=\int_0^t c(s)\,ds,
\]

then exactly

\[
 G(t)=G(0)+a(t)\otimes_nx.
\tag{2}
\]

Suppose the mobility immediately below the edge evolves according to

\[
 \dot W=q_-G(t)^*c(t),
\]

where `q_-` is the squared norm of the still lower frozen input.  Since

\[
 G(t)^*c(t)=G(0)^*\dot a(t)
             +x\langle a(t),\dot a(t)\rangle_n,
\]

integration gives the endpoint rule

\[
 \boxed{
 W(t)-W(0)
 =q_-\left(G(0)^*a(t)+\frac12x\|a(t)\|_n^2\right).
 }
\tag{3}
\]

This is an algebraic identity.  It needs neither Gaussianity nor a bound on
the coordinates of `c`.  Most importantly, every nonlinear stability term
in (3) contains the integrated signal `a`, not the instantaneous signal
`c`.

## 3. Exact frozen-input layer recursion

Freeze the right factors

\[
 \bar x_l=x_l(0),\qquad \bar q_l=\|\bar x_l\|_n^2
\]

during a block of duration `h`, while retaining the changing gates and the
exact shared matrices.  At the top solve the coordinate system

\[
 \dot W_L=\bar q_{L-1}A,
 \qquad
 \dot A=\chi(W_L),
\tag{4}
\]

and set `a_L=integral_0^h b_L(s) ds`.  When `q>0`, the latter is equivalently

\[
 a_L=[J(W_L(h))-J(W_L(0))]/\bar q_{L-1};
\]

at `q=0` its integral definition gives the continuous value and must be
used.

For `l=L-1,...,1`, define recursively

\[
 S_l=G_l(0)^*a_{l+1}
       +\frac12\bar x_l\|a_{l+1}\|_n^2,
\tag{5}
\]

\[
 W_l^+=W_l+\bar q_{l-1}S_l,
 \qquad
 a_l=\mathfrak D_{\bar q_{l-1}}J(W_l,S_l)
 \quad(l\ge2).
\tag{6}
\]

The parameter endpoint is

\[
 A^+=A(h),
 \qquad
 G_l^+=G_l+a_{l+1}\otimes_n\bar x_l,
 \qquad
 u^+=J(W_1^+).
\tag{7}
\]

Equations (2)--(7) exactly integrate the surrogate graph in which every
inter-layer right factor is frozen but every activation gate and every
transpose reuse is kept exact.  They are obtained by induction from the top:
`a_(l+1)` is the accumulated covector incident on an edge, (3) transports it
through the exact transpose of that same updated edge, and (1) converts the
resulting mobility displacement into the accumulated covector for the next
edge.

This is the sought recursive/peeling form: adding a layer repeats (5)--(6)
and introduces no new algebraic primitive.

## 4. Frozen-block size estimates and the failed stability claim

Assume on a stopped state ball

\[
 \|G_l\|_{op}\le K,
 \quad \|x_l\|_n\le X,
 \quad \|A\|_n\le B,
 \quad 0<m\le m_1,
\]

and assume `J'` and `J''` are bounded.  The top system (4) has an
`n`-independent energy bound.  Induction in (5)--(6) then gives

\[
 \|a_l\|_n\le C_{T,L}h,
 \qquad
 \|G_l^+-G_l\|_{op}\le C_{T,L}h.
\tag{8}
\]

Indeed, `||S_l||_n <= K||a_(l+1)||_n +
(X/2)||a_(l+1)||_n^2`, while the mean-value representation

\[
 \mathfrak D_qJ(W,S)
 =\int_0^1J'(W+\theta qS)S\,d\theta
\tag{9}
\]

gives `||a_l||_n<=||J'||_infty||S_l||_n` without division by `q`.

It is tempting to infer that differences of two frozen blocks satisfy the
same recursion, because terms in (3) contain an `a=O(h)`.  That inference is
false on normalized-`L^2`/operator energy balls.  Comparing the divided
difference in (9) creates

\[
 [J'(W)-J'(\widetilde W)]\widetilde S,
\]

and `S` can contain an energy-bounded coordinate spike.  Section 7 gives an
explicit counterexample.  Thus the valid conclusion of (8) is a uniform
**size** estimate for each block, not a dimension-free difference estimate.
Clipping only the top readout does not repair the arbitrary-depth statement:
an operator-norm-bounded lower edge can concentrate a bounded upper field
into a hidden energy spike.

For fixed `h` and a fixed finite solver for (4), (1)--(7) are a finite
persistent Gaussian program: the same `G_l` and `G_l^*` occur in (5), and no
source is refreshed.

## 5. Reconstraint and the activation distinction

The quantities `W_l` in the frozen surrogate are auxiliary.  After (7), the
true forward graph must be restored from the new parameters:

\[
 z_1^+=u^+,
 \quad x_1^+=\phi(z_1^+),
 \quad z_{l+1}^+=G_l^+x_l^+,
 \quad W_{l+1}^+=\Phi(z_{l+1}^+).
\tag{11}
\]

The last operation has stability constant `||Phi'||_infty`.  For pure
arctangent,

\[
 m(z)=(1+z^2)^{-1},
 \qquad \Phi'(z)=1+z^2,
\]

so energy control of `z` does not make (11) Lipschitz in normalized `L^2`.
This is the exact moving-frame obstruction; it is absent from the frozen
identity and reappears only when the actual graph is restored.

For the standard leaky arctangent

\[
 \phi_\alpha(z)=\alpha z+\arctan z,
 \qquad \alpha>0,
\]

one has

\[
 \alpha\le m(z)\le1+\alpha,
 \qquad
 \|\Phi'\|_\infty\le\alpha^{-1}.
\tag{12}
\]

Thus reconstraint is dimension-free Lipschitz for each fixed `alpha>0`.
The constant degenerates as `alpha` tends to zero, so this observation alone
cannot recover pure arctangent by `alpha downarrow 0`.

## 6. The remaining consistency commutator

Even under (12), stable reconstraint does not by itself prove consistency
with the simultaneous gradient flow.  Along the exact flow the right factors
`x_l(t)` move, and

\[
 G_l(h)
 =G_l(0)+a_{l+1}(h)\otimes_nx_l(0)
   +\int_0^h b_{l+1}(t)\otimes_n
      [x_l(t)-x_l(0)]\,dt.
\tag{13}
\]

Energy bounds and `L^2` time-Lipschitzness of `x_l` make the last operator in
(13) `O(h^2)`.  The harder term occurs one level lower: comparing the
accumulated covector uses

\[
 [m(z_l(t))-m(\widetilde z_l(t))]r_l(t).
\tag{14}
\]

An `L^2` bound on each factor controls (14) only in `L^1`, not in the `L^2`
metric used by (8)--(10).  A lower bound on `m` makes transport (11) stable
but does not, by itself, supply the missing integrability of (14).

Therefore the gate-resolved route passes the algebraic recursion and frozen
stability gates, but a claimed arbitrary-depth theorem still needs one of:

1. an exact cancellation showing that (14) never enters the endpoint error;
2. a reachable-perturbation estimate controlling its time integral with an
   extra factor of `h` from the causal increment;
3. a projective tail certificate for `r_l`; or
4. a weaker metric plus an independent argument upgrading the observables
   and raw kernel.

If none exists, leaky arctangent has only moved the original product
obstruction from reconstraint to consistency.  This is the current decisive
audit gate.

## 7. Backward-recomputation counterexample

The missing stability is not merely an unaudited estimate.  It fails already
at hidden depth two for every non-affine leaky arctangent.

Choose `s` with `a=phi(s) != 0`, put

\[
 u=s\mathbf 1,
 \qquad x_1=a\mathbf1,
 \qquad P=\frac{\mathbf1\mathbf1^T}{n},
 \qquad H=I-P,
 \qquad A=\sqrt n\,e_1,
\]

and compare

\[
 G=H,
 \qquad
 \widetilde G=H+R,
 \qquad
 R=\frac{c}{a^2}(e_1\otimes_nx_1),
\tag{15}
\]

where `c != 0`.  Then

\[
 Gx_1=0,
 \qquad \widetilde Gx_1=ce_1,
 \qquad \|R\|_{op}=\frac{|c|}{|a|\sqrt n}\longrightarrow0.
\]

The two forward states are therefore `o(1)` apart in normalized vector and
operator norm; their feature norm is `a^2>0`, and all energy/operator norms
are bounded.  Write

\[
 D_0=\phi'(0),\qquad D_c=\phi'(c).
\]

Since the common readout is supported on the first coordinate,

\[
 b_2=D_0\sqrt n e_1,
 \qquad
 \widetilde b_2=D_c\sqrt n e_1.
\]

A direct transpose calculation yields

\[
 \widetilde r_1-r_1
 =(D_c-D_0)\sqrt n\,He_1
   +\frac{cD_c}{a\sqrt n}\mathbf1.
\tag{16}
\]

The two terms are orthogonal and
`||sqrt(n)He_1||_n^2=1-1/n`; hence

\[
 \|\widetilde r_1-r_1\|_n\longrightarrow|D_c-D_0|>0.
\tag{17}
\]

For `phi_alpha(z)=alpha z+atan(z)`,

\[
 D_c-D_0=-\frac{c^2}{1+c^2},
\]

so the jump is independent of `alpha`.  The next bottom mobility update turns
this into an order-`h` state discrepancy.  Consequently the constrained
backward map is not uniformly continuous on the proposed energy balls.

Uniform local tangency fails on the same balls.  Set `W=0` and
`r=sqrt(n)e_1`.  For fixed `h>0`, the leaky-arctangent inverse mobility has
asymptotic slope `alpha` at infinity but slope `alpha+1` at zero, so

\[
 \lim_{n\to\infty}\frac1h
 \|J_\alpha(hr)-J_\alpha(0)-hJ_\alpha'(0)r\|_n=1.
\tag{18}
\]

Thus pointwise-in-width consistency cannot be upgraded to the uniform
`o(h)` estimate needed when the width limit precedes mesh removal.

This counterexample is not claimed to be a typical Gaussian training state.
Its force is exact: energy and operator certificates alone cannot prove the
desired theorem.  A reachable-state probabilistic certificate must exclude
precisely these concentration patterns, which restores the higher-moment or
uniform-integrability problem the gate transform was meant to avoid.

## 8. Claim ledger for this route

- **Proved:** paired-edge identity (3), layer recursion (4)--(7), no-small-
  Gram divided difference (9), and frozen-block energy estimates (8).
- **Falsified:** dimension-free frozen-block/backward-reconstraint stability
  on normalized-`L^2` and operator-norm energy balls; see (15)--(18).
- **Proved distinction:** pure arctangent has an unbounded reconstraint map;
  fixed leaky arctangent has a bi-Lipschitz mobility coordinate.
- **Open only under a stronger reachable-state certificate:** uniform
  integrability/higher-moment stability, moving-input consistency,
  compact-time accumulation, and restartability of the completed limit.

No depth-three limit follows from this note yet.
