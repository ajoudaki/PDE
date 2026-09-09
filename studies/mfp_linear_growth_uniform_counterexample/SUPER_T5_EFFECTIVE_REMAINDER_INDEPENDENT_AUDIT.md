# Independent audit of the super-`t^5` effective-remainder theorem

## Verdict

The temporal calculation, compact-bump insertion mechanism, fixed-step
diagonal, and two-rate minimax are correct.  Relative to the already
established fixed-horizon **marked, source-aware generated-core
intertwining**, `SUPER_T5_EFFECTIVE_REMAINDER.md` proves the stated
full-`L=2` theorem.

There is one important correction to the computational narrative.  The
sixth elementary differential

\[
 E_6=\|H^2g\|^2
\]

does have conservative zero-margin monomials after Gaussian flattening.
Thus the statement “the `E6` zero-margin ledger is empty” is false.  This
does not create a true principal sector: before flattening, `E6` needs four
new singular Hessian factors and therefore has new amplitude order four,
not two.  Its apparent quadratic zero-margin monomials cancel after they
are grouped by their pre-peel marks.  The proof must use the marked
generated-core grading, not take absolute values of the flattened `E6`
monomials.

If the marked source-aware intertwining is not admitted as an established
input, this grouping is the exact remaining conditional boundary.  No
other bridge failed the audit.

## 1. General-horizon chronology

For

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),
\]

the independently recomputed order-five weights in the basis

\[
 \bigl(V[g^5],U[Hg,g^3],T[T[g,g],g,g],T[H^2g,g,g],
       T[Hg,Hg,g],\|H^2g\|^2\bigr)
\]

are exactly the six polynomials displayed in (2.1) of the theorem.  The
single-node quadratic highest-excess combination is

\[
 5W_1(t)-W_2(t)+W_3(t)
 =-\frac{t^4}{3}-\frac t8
 =-\frac{t(8t^3+3)}{24}.
\]

It gives `-11/24,-67/12,-219/8` at `t=1,2,3`.  The cubic combination is

\[
 W_H(t)-3W_T(t)=\frac{t(2t-1)}2.
\]

These formulas were checked directly from the coefficient recurrence, not
inferred from the `t=1` map.

## 2. Node symbol and lower strict weight

For one occurrence `y=Phi(x(theta))`, set

\[
 r=\partial_y\widehat f,\quad
 \ell=\nabla x,\quad s=\ell^TG\ell,\quad
 v=\ell^TG\nabla f.
\]

The highest-new-excess part of `D^k f` is

\[
 r\Phi^{(k)}\ell^{\otimes k}.
\]

For the compact perturbation

\[
 \delta wP((x-X)/w),\qquad P'=p,\qquad \int p=0,
\]

the three true quadratic excess-four integrals are

\[
 \int pp''''=\int(p'')^2,
 \qquad
 \int p'p'''=-\int(p'')^2,
 \qquad
 \int(p'')^2.
\]

Consequently the complete same-node contribution is

\[
 -\frac{t(8t^3+3)}{24}
 r^2sv^4\,\gamma(X)\frac{\delta^2}{w^3}
 \int(p'')^2.
\]

It is nonpositive pointwise.  For a lower node,

\[
 r_j=b_j/n,\qquad s_j=n,\qquad v_j=b_jb,
\]

so its total weight is `b^4 n^{-1} sum_j b_j^6`.  Conditional on the lower
preactivation mark, condition on `(W,u)` once more.  The readout Gaussians
give

\[
 b_j\mid(W,u)\sim N(0,V_{j,n}),\qquad
 V_{j,n}=n^{-1}\sum_iW_{ij}^2\phi'(z_i)^2.
\]

The row law of large numbers and the `O(n^{-1/2})` covariance between
`W_ij` and `z_i` give `V_{j,n}->d=E phi'(G)^2` in `L^6`.  Bounded slope
gives a uniform twelfth moment.  Hence

\[
 n^{-1}\sum_j\mathbb E b_j^6\longrightarrow15d^3,
\]

and the lower coefficient is the strictly negative quantity in (2.4).

## 3. Why reused adjoints and `E6` do not add a principal sector

Before the final Gaussian expectations are flattened, an order-five
gradient elementary differential is a rooted tree with four edges.  If a
new activation derivative `phi^(r)` has excess `r-1`, every generated-core
term therefore obeys

\[
 e\le4.
\]

Suppose its `k` new high-derivative factors occupy `R` distinct endpoint
source classes.  Marked source coincidences are merged before norms are
taken; distinct endpoint classes give distinct Gaussian integrations.  A
localized term is bounded by

\[
 C_{t,\mathrm{old}}P_{t,\mathrm{old}}(X)
 \delta^k\gamma(X)^Rw^{R-e}.
\]

With `w=delta sqrt(gamma(X))`, relative to
`S=delta^{-1}gamma(X)^{-1/2}`, the margins are

\[
 m_\delta=k+R-e+1,
 \qquad
 2m_\gamma=3R-e+1.
\]

For `R>=2`, one also has `k>=R`; hence both margins are positive.  For
`R=1`, they are nonnegative except for a lone fifth derivative.  Four
integrations by parts remove that apparent negative margin.  The only true
zero case is therefore

\[
 R=1,\qquad e=4,\qquad k=2,
\]

and its complete grouped value is the node symbol above.

In particular, `E6` consists of four Hessian occurrences at maximal
excess.  Its excess-four sector has `k=4`, so it has positive amplitude
margin.  Gaussian integration by parts can make separate flattened
monomials look like `(e,k)=(4,2)`, but mark extraction commutes with the
finite Wick--Stein recursion.  Their grouped coefficient is therefore
zero.  This explains why a conservative flattened census reports `E6`
zero-margin entries while its integrated true quadratic symbol vanishes.

This paragraph is precisely where the established marked source-aware
intertwining is needed.  A non-marked `t=1` 979-term map alone is not enough.

## 4. Old bumps and RMS normalization

New compact supports are placed to the right of all old supports.  Within
one Gaussian atom, a product of an old and a new derivative of order at
least two is zero.  Old high-derivative atoms in other source classes are
fixed finite constants.  Thus they change only
`C_(t,old),P_(t,old)`, after `t` and the old truncation have been fixed.

The bump has `C^1` size at most

\[
 \delta\bigl(w\|P\|_\infty+\|p\|_\infty\bigr).
\]

Its RMS-normalizer change is bounded by its Gaussian `L^2` norm,

\[
 \delta w\|P\|_\infty
 \sqrt{\mathbb P(|G-X|\le w/4)}.
\]

The finite old moment polynomial is Lipschitz in this scalar rescaling.
That additive error has positive margin, while the local negative term is
multiplied by a positive `1+o(1)` factor.  Normalization therefore does not
alter the insertion sign or prevent an arbitrarily small `d_1` insertion.

## 5. Exact-output diagonal and two-rate minimax

The fixed-schedule continuity estimate uses only the linearly weighted
activation difference and the uniform slope difference.  For a fixed
smooth reference, fixed finite schedule, and compact step interval,

\[
 \sup_n\mathbb E|f_{k,n}^{\phi}(h)-f_{k,n}^{\psi}(h)|
 \le C_{\psi,k,R}d_1(\phi,\psi).
\]

Every continuity constant may grow arbitrarily with the horizon and old
bumps, but it is finite when its tail budget is created.  The insertion
coefficient grows as `1/(delta sqrt(gamma(X)))`; decreasing the next
amplitude therefore satisfies all finitely many old budgets while making
the new fifth coefficient larger.  The countable diagonal is consistent.

For each smooth truncation choose `h_N` only after its width-first germ is
known and preserve exact outputs at both `h_N` and `h_N/2`.  For an arbitrary
cubic subtraction `kappa`, put `x=(kappa_N-kappa)/h_N^2`.  The two normalized
quotients are

\[
 x+\beta_N+e_{1,N},\qquad4x+\beta_N+e_{2,N}.
\]

Since

\[
 3|\beta_N|
 \le5\max\{|x+\beta_N|,|4x+\beta_N|\},
\]

one scalar `kappa` cannot cancel both witnesses.  This proves the lower
bound after taking the infimum over `kappa`; no cubic or fifth jet of the
final activation is required.

The limiting unnormalized activation equals the identity off locally
finite disjoint bumps and has uniformly positive bounded slope.  The
normalization-aware `d_1` budgets and a three-epsilon argument give every
fixed-step width-first expected output.  The final statement concerns exact
nonzero-step outputs, with width sent to infinity first.

## Claim-level result

- General temporal coefficient: **proved**.
- Node sign and lower strict coefficient: **proved**.
- Reused-matrix/multiple-source remainder: **proved relative to the
  established marked source-aware generated-core intertwining**.
- Normalization and old-bump interactions: **proved**.
- Fixed-step output continuity and limiting activation: **proved**.
- Two-rate super-polynomial lower bound: **proved**.
- Final activation cubic/fifth jet: **not needed and not asserted**.

