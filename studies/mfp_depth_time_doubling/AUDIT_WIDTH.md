# Independent hostile audit: width-first identification

## Verdict

**PASS.**  I found no mathematical gap in `WIDTH_DEPTH_TIME.md` after
checking the construction against the exact finite-width recursion.  In
particular, the proof does not use conditional independence that is lost
under matrix reuse, does not omit the rectangular cross block created by
the current forward action, and does not hide a width/step-size limit
exchange.

The two editorial clarifications recorded below were applied after this
audit; no mathematical statement or constant changed.

This verdict concerns only the pointwise fixed-\(h\) width theorem.  Its
constants are allowed to depend on the fixed finite triple \((L,N,h)\), as
the theorem states; it supplies no estimate uniform as \(h\to0\),
\(N\to\infty\), or \(L\to\infty\).

## 1. Exact scaling and chronology

For

\[
 f=n^{-1}a^TH_L,
 \qquad Z_\ell=n^{-1/2}W_\ell H_{\ell-1},
\]

direct backpropagation gives

\[
 \partial_{W_\ell}f=n^{-3/2}C_\ell H_{\ell-1}^T,
 \qquad \partial_uf=n^{-1}C_1.
\]

Thus the update \(\theta^+=\theta+hn\nabla f\) gives exactly

\[
 W_\ell^+=W_\ell+h n^{-1/2}C_\ell H_{\ell-1}^T,
 \qquad u^+=u+hC_1,
\]

as in (2.7).  Substitution of the accumulated rank-one updates gives
(2.11)--(2.13), including the factor \(h\), the empirical normalization
\(n^{-1}\), and the strict inequality \(r<s\).  Hence no current gradient
is accidentally evaluated after part of the simultaneous update.

At each nonterminal time the order

\[
 F_{s,2},\ldots,F_{s,L},B_{s,L},\ldots,B_{s,2}
\]

makes every query predictable.  The terminal time has only the forward
sweep.  This gives exactly \((2N+1)(L-1)\) initialization-matrix actions.
The checks also cover \(L=1\), where the stated iid scalar recursion is
exact and no reused matrix is present.

## 2. Adaptive conditioning across all matrices

Lemma 4.1 is valid for the global, rather than connector-local,
filtration.  Conditional on the past, the next matrix label, query, old
query spans, and their projectors are fixed.  For the selected matrix the
unrevealed block is

\[
 P_C^\perp \widetilde M P_H^\perp.
\]

Splitting off the new right direction for a row action, or the new left
direction for a transpose action, is an orthogonal Gaussian splitting.
It leaves the residual on the enlarged orthogonal complements fresh.
Residuals of all unselected independent initialization matrices remain
conditionally independent.  This induction remains valid when a query is
a function of earlier actions of several matrices: predictability, not
independence of the query and the initialization matrix, is the required
hypothesis.

The dimensions in (4.4)--(4.7) are consistent.  If \(H\) has \(p\)
columns and \(C\) has \(k\) columns, then

\[
 Q\in\mathbb R^{p\times p},\quad K\in\mathbb R^{k\times k},
 \quad \mathcal R=C^TY/n\in\mathbb R^{k\times p}.
\]

The new-column correction uses
\(r-\mathcal R^TK^{-1}k\in\mathbb R^p\), whereas the new-row correction
uses \(v-\mathcal RQ^{-1}q\in\mathbb R^k\).  These are the correct two
rectangular regressions.  The Moore--Penrose statement is also correct,
although the nonconstant branch later proves that ordinary inverses
suffice at every action actually used.

## 3. Reused-column dependence and response cancellation

For one connector after the current row has been adjoined, write

\[
 y=\xi+Pc,\qquad d=\chi+Sh,
\]

with \(P\in\mathbb R^{p\times k}\) and
\(S\in\mathbb R^{k\times p}\).  Independent-block Gaussian integration
by parts gives

\[
 \mathcal R=\mathbb E[cy^T]=SQ+KP^T.
\]

For a new row query, with
\(q=\mathbb E[hH_*]\) and
\(\rho=\mathbb E[\nabla_\chi H_*]\),

\[
 v=\mathbb E[dH_*]=K\rho+Sq.
\]

Substitution into the finite-dimensional conditional mean cancels
\(c^TP^TQ^{-1}q\) exactly and leaves

\[
 \xi^TQ^{-1}q+c^T\rho.
\]

The old-source regression plus the orthogonal innovation is precisely the
new \(\xi\)-coordinate with covariance equal to the enlarged feature
Gram.  The transpose calculation similarly uses

\[
 r=Q\sigma+Pk
\]

and cancels \(h^TS^TK^{-1}k\), leaving the new \(\chi\)-coordinate and
the response \(h^T\sigma\).  These calculations prove (6.9) and (6.14)
for rectangular \(p\)-by-\(k\) history blocks.

Crucially, \(\rho=\mathbb E\nabla_\chi H_*\) is not set to zero.  It
contains the dependence of the current feature on all earlier transpose
actions of the same matrix.  Thus the column-reuse dependence singled out
in the audit request is retained explicitly.

The empirical ledger is also complete.  Before the backward action, the
cross block is

\[
 \mathcal R^{B,(n)}=
 \left[\mathcal R^{F,(n)},,n^{-1}(R^{<s})^TH^s\right],
\]

so the extra column produced by the current forward query is present.
Lists (8.2) and (8.3) contain the two same-side projections, the two
opposite-action cross moments, the query norm, and the appropriate old
Grams required by (4.4)--(4.7).  No mixed-connector inverse is needed.

## 4. Full-rank audit

The three activation branches are exhaustive.

* If \(\phi\) is constant, normalization forces \(\phi=\pm1\); all hidden
  gradients vanish and \(\mathbb Ef_{n,L}^N=Nh\) exactly.  No history
  inverse is invoked.
* If \(\phi\) is nonconstant and \(\phi'\) is nonconstant, then
  \(d=\mathbb E\phi'(G)^2>0\).  At initialization
  \(K_{\ell,00}=d^{L-\ell+1}>0\).  Each new forward source has a positive
  Schur innovation inherited from the already positive lower-layer
  feature Gram.  Since a nonconstant continuous function of a
  nondegenerate Gaussian has positive variance, this extends every
  feature Gram.  At the top, \(a^s\ne0\) with positive probability, and
  the fresh current forward innovation makes
  \(a^s\phi'(Z_L^s)\) conditionally nonconstant.  Each descending fresh
  \(\chi\)-innovation is then multiplied by
  \(\phi'(Z_\ell^s)\), which is nonzero with positive probability, so it
  extends every cotangent Gram.
* If \(\phi'\) is constant while \(\phi\) is nonconstant, then
  \(\phi(x)=px+c\) with \(p\ne0\).  The top cotangent is \(pa^s\), and
  for \(s\ge1\) it contains the fresh term
  \(hp^2\tau_{L,s-1}E_{L,s-1}\).  This proves the top cotangent Schur
  complement directly; the descending argument then uses the nonzero
  constant multiplier \(p\).  Thus the affine case is not incorrectly
  folded into the nonconstant-\(\phi'\) argument.

Finally, the current \(\chi_{2,s}\) innovation enters
\(Z_1^{s+1}\) with coefficient
\(h\upsilon_{1,s}\phi'(Z_1^s)\).  Since \(h\ne0\), this both extends the
bottom feature Gram and propagates the nonvanishing-derivative event to
the next time.  The forward/backward rank induction is therefore not
circular.

The phrase “condition on every source except” around (7.16) must be read
chronologically: condition on the sigma-field just before the fresh
\(\xi_{L,s-1}\) innovation, not on future correlated source coordinates.
The preceding chronological construction supplies exactly that
sigma-field, so this is an editorial clarification rather than a gap.

## 5. Coupling, concentration, and finite moment tower

The ideal populations in (9.2) are the correct ones.  Each physical-layer
coordinate uses the two independent carriers adjacent to that layer
(with \(U\) or \(A\) at an endpoint), while temporal coordinates within a
carrier block have the population feature or cotangent covariance.  The
Schur regressions (9.2a)--(9.2d) terminate in the action chronology and
have positive innovation variances by Section 7.

At a raw action, the same fresh standard Gaussian vector can be used in
the exact conditional residual and in the ideal innovation.  Conditional
on the joint past it is fresh; the raw action uses its finite-rank
projection \(P_{\mathcal S_n}^\perp g\), whereas the ideal action uses
the full \(g\).  This preserves the exact raw transition kernel and gives
the four-term difference (9.8b).  There is no incompatible demand that
one vector be fresh for two different initialization matrices: a distinct
fresh vector is assigned to every action, and conditional independence of
the matrix residuals permits the global interlacing.

The concentration estimates close quantitatively:

1. iid ideal coordinate averages have \(L^r\) error
   \(O(n^{-1/2})\) by (9.4);
2. (9.5) transfers field errors to every Gram and cross-moment;
3. on the stopped spectral set, inverse differences follow from (9.6),
   and every regression coefficient contains at most two unbounded
   empirical-moment factors;
4. the innovation square root is Lipschitz because both variances are
   bounded below by \(2\gamma_{L,N,h}\);
5. the removed projection has normalized \(L^r\) size
   \(O(n^{-1/2})\) because its rank is at most \(N+1\).

Expanding the products in the second term of (9.8b) shows why the factor
eight in (9.9) is sufficient: the worst coefficient-difference term has
the form \(\mathcal Z_n^2\delta_n\bar V\).  Each entry of
\(\mathcal Z_n\) is a product of two fields, \(\delta_n\) is a sum of a
two-field empirical error and an iid two-field average, and \(\bar V\) is
one field.  Holder therefore uses at most seven field/error factors; input
order \(8r\) dominates all of them.  Coordinate and pair-moment bundles
consume at most \(4r\) and \(2r\), respectively.  Consequently

\[
 R_0=8^{3(2N+1)(L-1)+1}r_*
\]

is a genuinely finite sufficient moment order, not an implicit
all-moments induction.  Linear growth and bounded first two derivatives
give all of those initial Gaussian moments.

The first-failure probability follows by taking terminal order \(2m\):
entrywise \(L^{2m}\) errors of order \(n^{-1/2}\), Weyl's inequality, and
a finite union bound give \(O(n^{-m})\).  The extension never alters the
raw transition law, and raw and extended histories coincide up to the
first failed test.

## 6. Stopping removal and terminal expectation

The deterministic recursion (10.2)--(10.7) correctly dominates the raw
network.  In particular, after dividing the trained matrix by \(\sqrt n\),
one rank-one update has operator norm

\[
 \left\|\frac h n CH^T\right\|_{\rm op}
 \le |h|\|C\|_{n,2}\|H\|_{n,2}.
\]

The initialization radius has every uniform moment; the displayed net
bound supplies this for Gaussian operator norms.  Hence the finite
majorant polynomial has every uniform moment.

For a normalized spatial \(p\)-norm, the possible raw factor
\(n^{(1/2-1/p)_+}\) on the stopped event is beaten by choosing the failure
exponent \(m=2\max\{p,P,2\}\).  Equation (10.12) then tends to zero for
every requested mixed moment.  The same argument removes stopping from
all pair moments.

Finally,

\[
 |f_{n,L}^N|\le \|a^N\|_{n,2}\|H_L^N\|_{n,2}
\]

is dominated in every finite moment by the majorant polynomial.  The
terminal outputs are therefore uniformly integrable.  Coupled field
convergence reduces the output to the iid ideal top-coordinate average,
whose expectation is \(F_{N,L}(h)\).  This proves convergence of
expectations, not merely convergence in probability.

## 7. Defect ledger

No substantive defect was found.

Two harmless presentation clarifications are advisable if the file is
revised later:

1. define \(\|x\|_{n,p}=(n^{-1}\sum_i|x_i|^p)^{1/p}\) at its first use;
2. replace “condition on every source except” near (7.16) by “condition on
   the chronological sigma-field just before the indicated innovation,”
   to preclude the incorrect interpretation that future correlated source
   coordinates are conditioned on.

Neither point changes a formula or supplies a missing proof step.
