# Bounded-readout compactness check for three unit labels

Status: complete bounded second-pass analytical check, 2026-09-16.
The candidate supplied by the supervisor is correct with the hypotheses
stated below. This is a conditional theorem and an author-side check, not
an independent isolated review or a resolution of generic unit-label
training. The original `generic3_geometry_route.md` is unchanged.
No experiment, auxiliary agent or additional scientific input was used.

## 1. Exact statement and scope

Consider the actual prescribed-initialization canonical `p=1` population
closure for three equally weighted directions and unit labels
`y_i in {+1,-1}`; in particular the requested labels `(+1,+1,-1)` are
included. Retain the exact correlated Gaussian marks, ridge `1/4096`,
Cholesky normalization, zero initial population readout, full hidden
training and physical unhalved mean-square loss

\[
 \mathcal L(t)=\frac13\sum_{i=1}^3(f_i(t)-y_i)^2.
 \tag{1}
\]

Assume

\[
 \sup_{t\ge0}\|c(t)\|_{L^2(\Omega_2)}=C<\infty,
 \qquad \mathcal L(t_*)<\frac13
 \quad\hbox{for some finite }t_*.
 \tag{2}
\]

Then

\[
 \lim_{t\to\infty}\mathcal L(t)=0,
 \qquad \lim_{t\to\infty}f_i(t)=y_i\quad(i=1,2,3).
 \tag{3}
\]

No uniform bound on `M`, on its effective two-dimensional upper
coefficient vectors, or on the lower rows is needed. No convergence of
`c`, `M`, the lower rows or the hidden features themselves is concluded.
The distinct/non-antipodal direction assumption is compatible with the
statement but is not needed in this conditional argument.

The proof has three parts: compactify the two-dimensional upper ridge
family by adding sign functions, establish independence of the resulting
distinct fields, and combine readout stationarity with strictly positive
classification margins. The bounded-readout hypothesis connects limiting
feature coincidences with limiting predictions.

## 2. The exact upper family and its compactness

The canonical order-one initialization and evolution preserve the parity
subspace with odd lower rows, odd upper readout and an odd-to-odd middle
block. At order one the two active upper marks are

\[
 \beta=(\beta_1,\beta_2)
   =\frac{(\tanh\xi_1,\tanh\xi_2)}{\sqrt{\tau+\eta}},
 \quad \eta=\frac1{4096},\quad
 \xi_1,\xi_2\text{ independent }N(0,v_0),
\]

where `v_0=E tanh^2 G>0` and `tau=E tanh^2(sqrt(v_0)G)>0`.
Indeed their raw Gram is `tau I_2`, the constant is orthogonal to them,
and the exact Cholesky factor on this block is
`sqrt(tau+eta) I_2`. Thus, for each sample and time,

\[
 H_i(t,\beta)=\tanh(\beta\cdot v_i(t)),
 \qquad v_i(t)\in\mathbb R^2.                            \tag{4}
\]

The constant upper coordinate contributes nothing because its middle
row remains zero. The upper mark law has a positive smooth density on
the open square

\[
 Q=(-b,b)^2,\qquad b=(\tau+\eta)^{-1/2},
\]

and gives zero mass to every line. To verify this, coordinatewise tanh
is a smooth bijection from `R` to `(-1,1)` with positive derivative;
transporting the positive Gaussian density by this bijection and the
positive constant scaling gives the stated density. The square and the
law are fixed in time.

**Compactness lemma.** Every sequence of functions
`tanh(beta dot v_n)`, `v_n in R2`, has a strongly convergent subsequence
in `L2(Omega_2)`. Every resulting limit has one of the forms

\[
 T_v(\beta)=\tanh(\beta\cdot v),\quad v\in\mathbb R^2,
 \qquad
 S_e(\beta)=\operatorname{sign}(\beta\cdot e),\quad e\in S^1.
 \tag{5}
\]

The value assigned to `sign(0)` is immaterial.

Proof. If the coefficient sequence has a bounded subsequence, extract
`v_n -> v`. The functions converge pointwise to `T_v` and are bounded
by one, so dominated convergence gives `L2` convergence. Otherwise extract
a subsequence with `|v_n| -> infinity` and then one with
`v_n/|v_n| -> e in S1`. For every `beta` with `beta dot e !=0`,

\[
 \beta\cdot v_n
   =|v_n|\,\beta\cdot(v_n/|v_n|)
       \longrightarrow
       \begin{cases}+\infty,&\beta\cdot e>0,\\
                    -\infty,&\beta\cdot e<0.
       \end{cases}
\]

The exceptional line has zero mark probability. Thus the functions
converge almost everywhere to `S_e`, and domination by one again gives
`L2` convergence. These alternatives cover every sequence. The same
argument applies to the signed features `y_i H_i`, since oddness gives
`y_i tanh(beta dot v_i)=tanh(beta dot (y_i v_i))`. Finite successive
subsequence extraction treats all three samples together.

## 3. Independence, including the sign-function boundary

**Independence lemma.** Let `F_1,...,F_q`, `1<=q<=3`, be nonzero functions
of the forms in (5). Suppose no two are equal or opposite as `L2`
functions. Then they are linearly independent in `L2(Omega_2)`.

Proof. Suppose

\[
 \sum_{j=1}^q a_jF_j=0\quad\hbox{almost everywhere}.
 \tag{6}
\]

First remove every sign field. Two sign fields whose boundary lines
coincide are equal or opposite, so the retained sign fields have distinct
boundary lines. On the complement of these finitely many lines, the left
side of (6) is continuous. It vanishes pointwise there: a nonzero value
would persist on an open neighborhood with positive mark probability,
contradicting (6).

For one sign field `S_e`, select a nonzero point `beta_0` of its line
inside `Q`. Distinct lines through the origin meet only at the origin,
so a sufficiently small ball about `beta_0` intersects none of the other
sign boundaries. Each other sign field is constant on this ball, and
every tanh field is continuous across the selected boundary. Taking the
two one-sided limits of the pointwise identity (6) therefore gives a
jump of exactly `2a_j` or `-2a_j` from `S_e`, with all other jumps zero.
Hence `a_j=0`. Repeating this step removes every sign term.

It remains to prove independence of at most three tanh fields `T_v`.
Their vectors are nonzero. Distinct representatives satisfy
`v_i!=v_j` and `v_i!=-v_j`: for an equality of tanh fields, positivity
of the mark density and continuity extend the equality over `Q`, and
differentiation at the origin gives equality of the vectors; the opposite
case is the same after a sign reversal.

Choose a vector `z in R2` such that

\[
 \lambda_j=v_j\cdot z\ne0,\qquad
 \lambda_i^2\ne\lambda_j^2\quad(i\ne j).
 \tag{7}
\]

Only finitely many lines are forbidden: the kernels of `v_j` and of
`v_i-v_j,v_i+v_j`, all of which are nonzero vectors. Their union cannot
cover the plane, so such a `z` exists. Restrict the pointwise identity to
`beta=s z` for sufficiently small `|s|`, keeping it inside `Q`.
If `p<=3` tanh terms remain, differentiating in orders
`1,3,...,2p-1` at zero gives

\[
 \sum_{j=1}^p a_j\lambda_j^{2k+1}=0,
 \qquad k=0,\ldots,p-1.                                  \tag{8}
\]

The required derivatives of tanh are `tanh'(0)=1`,
`tanh'''(0)=-2`, and `tanh^(5)(0)=16`, all nonzero; (8) results after
dividing them out. With unknowns `a_j lambda_j`, the matrix is
Vandermonde in the distinct numbers `lambda_j^2`. Its determinant is
the product of their nonzero pairwise differences. Thus every
`a_j lambda_j=0` and then every `a_j=0`. This proves the lemma.

This proof also explains why passing from bounded coefficients to sign
limits does not introduce an omitted linear relation. A sign field cannot
cancel against smooth tanh fields across its boundary, even when some
tanh vectors are parallel to that boundary's normal. Equality or opposition
between a finite tanh field and a sign field is likewise impossible by
the same jump argument.

## 4. Stationary subsequences force zero limiting loss

The exact physical energy identity implies

\[
 \mathcal L'(t)
  =-\|w'(t)\|_2^2-\|M'(t)\|_F^2-\|c'(t)\|_2^2,
 \qquad
 \int_0^\infty\|c'(t)\|_2^2dt\le\mathcal L(0)=1.
 \tag{9}
\]

Hence there are times `t_n -> infinity` with
`||c'(t_n)||_2 ->0`. For example, choose one time in each interval
`[n,n+1]` at which the squared norm is no larger than its interval
integral; these integrals tend to zero by (9). The needed norm is
continuous along the fixed-order flow.

Let the classification margins and label-adjusted upper fields be

\[
 m_i(t)=y_i f_i(t),\qquad F_i(t)=y_iH_i(t).
 \tag{10}
\]

The loss is `3^(-1) sum_i(m_i-1)^2`. Monotonicity of the loss after
`t_*` and the strict threshold in (2) give the common bound

\[
 \delta\le m_i(t)\le2-\delta\quad(t\ge t_*),\qquad
 \delta=1-\sqrt{3\mathcal L(t_*)}>0.
 \tag{11}
\]

By the compactness lemma, along a subsequence of these same times all
three `F_i(t_n)` converge strongly in `L2` to limits `F_i^infty` of
the forms in (5). By (11), extract a further subsequence with scalar
limits `m_i(t_n) -> mu_i in [delta,2-delta]`.

The bounded readout in (2) has three precise consequences:

1. No limiting field is zero. If `F_i^infty=0`, then
   `|m_i(t_n)|=|E_2[c(t_n)F_i(t_n)]|
     <=C||F_i(t_n)||_2 ->0`, contrary to (11).
2. No two limiting label-adjusted fields are opposites. If
   `F_i^infty=-F_j^infty`, then
   `|m_i(t_n)+m_j(t_n)|
      <=C||F_i(t_n)+F_j(t_n)||_2 ->0`, whereas the sum is at least
   `2delta`.
3. Identical limiting fields have identical limiting margins. If
   `F_i^infty=F_j^infty`, then
   `|m_i(t_n)-m_j(t_n)|
      <=C||F_i(t_n)-F_j(t_n)||_2 ->0`, hence `mu_i=mu_j`.

No convergence or weak subsequence of the readout itself is needed.
The same fixed upper carrier is used throughout these inequalities.

The exact readout equation is

\[
 c'(t)=-\frac23\sum_{i=1}^3(m_i(t)-1)F_i(t).
 \tag{12}
\]

Passing to the selected subsequence in `L2` is legitimate because the
scalar coefficients converge and the bounded features converge strongly.
Since `||c'(t_n)||_2 ->0`, the result is

\[
 \sum_{i=1}^3(\mu_i-1)F_i^\infty=0.
 \tag{13}
\]

Group indices with identical limiting fields, and choose one field from
each group. By consequences 1 and 2 above, these representatives are
nonzero and are neither equal nor opposite. The independence lemma
therefore makes each group's coefficient in (13) vanish. Consequence 3
says every margin limit in that group is the same number `mu_G`.
Its coefficient is consequently

\[
 |G|(\mu_G-1)=0,
\]

so `mu_G=1`. Thus all three `mu_i=1`, and the loss along this subsequence
tends to zero. The nonnegative loss is monotone by (9), so its global
limit equals the subsequential limit, zero. Formula (1) then implies
`|f_i(t)-y_i|<=sqrt(3mathcal L(t)) ->0` for each sample, proving (3).

## 5. Audit outcome and remaining obligations

The candidate argument is valid. In particular:

- The unbounded-coefficient boundary consists of sign fields, with strong
  `L2` convergence justified by a null exceptional line and bounded gates.
- Boundary jumps eliminate every distinct sign field before the tanh
  independence argument is applied.
- Collinear finite tanh vectors with different magnitudes cause no gap:
  the generic-line Vandermonde uses distinct squared slopes, rather than
  assuming distinct directions.
- The strict `1/3` threshold provides uniform positive margins. It excludes
  both a vanishing limiting field and opposite limiting label-adjusted
  fields, rather than merely excluding zero residuals one at a time.
- The coefficients for identical fields cannot cancel with unequal
  prediction limits: bounded readout forces those limits to coincide.
- Boundedness of `M` is unnecessary, but boundedness of the readout has
  been used essentially in each of the three transfer statements.

The uniform readout bound in (2) is **not** supplied by finite energy.
From an `L2`-in-time speed bound alone one obtains bounds such as
`||c(t)||_2<=sqrt(t)` from `c(0)=0` and (9), not a bound uniform in time.
Likewise this argument does not prove that every generic three-input
trajectory ever reaches loss strictly below `1/3`. Those are distinct
remaining hypotheses. The theorem is therefore not a proof of the
unconditional generic unit-label result.

Neither monotone pairwise attraction nor monotone pairwise separation is
assumed. Distances may move in either direction. The conclusion concerns
training loss and predictions only; it supplies no proposed mixed
Lyapunov potential and no convergence theorem for the full state.
