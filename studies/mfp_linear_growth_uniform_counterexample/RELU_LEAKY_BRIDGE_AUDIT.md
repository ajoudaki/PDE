# Adversarial audit: exact hard-kink bridge

## Verdict

The local boundary algebra and its full reused-matrix coefficient pass.  The
candidate formula is

\[
 \Delta_t(h)=tD_{a,b}h|h|+o_t(h^2),
 \qquad D_{a,b}>0,
\]

with `D_(a,b)` in `RELU_LEAKY_UNIFORM_REMAINDER.md`.  The scalar boundary
lemma is exact for every fixed `t`, the lower-gate coefficient is zero, and
the upper-gate coefficient includes the indispensable aggregate drift
`Y~N(0,e)`.

However, unless the fixed-`h` indicator-state-evolution and the
width-uniform boundary-layer estimate below are supplied in full, the
formula must be labelled **conditional**, not an unconditional theorem for
the actual width-first network.

## Passed calculations

1. For one switching surface with normal velocities `p,q`, direct sign-cell
   integration gives

   \[
   J_t=t\,c\,p q\,\mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}.
   \]

   Numerical partition checks in all four sign regimes, including repeated
   attracting crossings, agree with the exact induction.

2. At a top gate, finite-width differentiation at initialization gives

   \[
   \dot z_i=A_i\phi'(z_i)Q_n+
   {1\over n}\sum_{j,k}W_{ij}W_{kj}A_k\phi'(z_k)\phi'(u_j)^2.
   \]

   The diagonal `k=i` term is the second copy of `A_i phi'(z_i)`.  The
   off-diagonal part has limiting variance
   `E phi'(G)^4=e` and is asymptotically independent of the distinguished
   `(A_i,z_i)`.  Therefore

   \[
   p=Y+2bA,\qquad q=Y+2aA.
   \]

3. The positive-wedge reduction

   \[
   \mathbb E[(a-b)Apq\mathbf1_{\rm crossing}]
   =-(a-b)\mathbb E[Apq; A>0,p\le0\le q]>0
   \]

   is exact.  It gives the stated one-dimensional positive integral and the
   ReLU value

   \[
   {\sqrt2\over\pi}(1-1/\sqrt5).
   \]

4. The lower gate has velocities `(bB,aB)` and hinge coefficient
   `(a-b)B`; its surface expectation is proportional to `E B^3=0` (and is
   pointwise zero for ReLU).

## Bridge obligations that cannot be hidden

### A. Fixed-step width identification for indicators

The smooth OMFP theorem cannot simply be quoted with `phi''=delta_0`.
One must approximate the hard derivative by Lipschitz ramps and prove,
uniformly in width, that all adaptively reused preactivation queries have a
small-ball bound.  The necessary induction must retain the actual
`W/W^T` conditioning and its Onsager coefficients.  It is not enough to say
that the initialization is Gaussian: later queries depend on reused rows and
columns.

### B. Width-first boundary remainder

At finite width there are `2n` initial gate surfaces.  Distinct top-gate
normals are weakly, not exactly, orthogonal because they share the lower
parameters.  There are quadratically many two-tube pairs.  The assertion
that “probability is `O(h^2)` and interaction is `O(h)`” is insufficient by
itself: its constant may grow with width.  An absolute pairwise estimate can
lose the mean-field normalization.  One must either

- prove a dimension-free BV/coarea estimate whose weighted surface-variation
  norm is uniformly bounded, or
- carry out the boundary expansion directly in the fixed-`h` width-limit DAG,
  including the aggregate response change caused by the positive fraction of
  other neurons crossing their gates.

Without one of these, a finite-width boundary expansion followed by
`n->infinity` would reverse the required order of limits.

### C. Nondegeneracy through the finite schedule

For the ramp limit, every later gate query used in the schedule needs a
conditional density bound on the relevant bounded-velocity event.  Exact
ReLU can freeze inactive coordinates, and reused Gaussian innovations can
have singular covariance.  A proof may exploit the near-identity map for
small `h`, but it must state the conditioning variable and show that one
remaining Gaussian coordinate has Jacobian bounded away from zero.  Merely
calling the innovation nondegenerate does not verify this.

## Claim boundary

The smooth pathological ReLU-like construction in `SMOOTH_RELU_LADDER.md`
does not depend on this bridge and is unconditional relative to the audited
smooth insertion theorem.  The exact hard-ReLU/leaky-ReLU conclusion should
be presented as the rigorously derived candidate, with the width-first bridge
explicitly open, unless obligations A--C are independently discharged.
