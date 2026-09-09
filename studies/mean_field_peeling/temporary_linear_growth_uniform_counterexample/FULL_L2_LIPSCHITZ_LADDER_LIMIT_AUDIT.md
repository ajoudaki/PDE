# Hostile audit of `FULL_L2_LIPSCHITZ_LADDER.md`

## Verdict

**FAIL as a proof of Theorem 1.1.**  The uniform-in-width continuity lemma is
repairable, and the truncation/diagonal limit can be made rigorous.  The
essential singular-sector estimate (5.10), however, is not proved.  Its
stated combinatorial premise is false for the exact paired order-five map.
Consequently (5.12), and hence the construction of the stages in (6.3), do
not currently follow.

This verdict does not assert that the theorem is false.  It says that the
present argument has not established it.

## 1. Lemma 2.1 is valid after two small repairs

Let

\[
 R_0=1+\|a^0\|_n+\|u^0\|_n+\|W^0/\sqrt n\|_{\rm op}.
\]

For a fixed finite schedule, the recurrences for
`a`, `u`, and `M=W/sqrt(n)` give polynomial bounds in `R_0`.  The rank-one
matrix update has the correctly normalized estimate

\[
 \left\|{h\over n}pq^T\right\|_{\rm op}
 =|h|\|p\|_n\|q\|_n.
\]

The first inequality in (2.9) needs `epsilon<=1`.  Indeed, with
`d=d_1(psi,tilde psi)`,

\[
\begin{aligned}
 |\widetilde\psi(x)-\psi(y)|
 &\le d(1+|x|)+\|\psi'\|_\infty|x-y|\\
 &\le d(1+|y|)+(\|\psi'\|_\infty+d)|x-y|\\
 &\le d(1+|y|)+(1+\|\psi'\|_\infty)|x-y|.
\end{aligned}
\]

The proof should also write the finite induction explicitly, or state its
recursion.  If `S_s` bounds the two coupled states and `D_s` their
difference, one may take

\[
 S_{s+1}=P_R(S_s),\qquad
 D_{s+1}\le Q_R(S_s)(D_s+d),
\]

where `P_R,Q_R` are fixed polynomials determined only by the background
activation, `k`, and `R`.  Since `D_0=0`, iteration gives
`D_k<=d Q_{k,R}(R_0)`.  The Gaussian operator-norm tail and the normalized
Gaussian-vector moments then prove (2.5), uniformly in width.  No second
derivative of the perturbed activation is needed.

Thus Lemma 2.1 is not the obstruction.

## 2. The claimed excess bound is exactly false

The proof defines, for an atom,

\[
 e(\nu)=\sum_{r=2}^5(r-1)\nu_r
\]

and then claims that the sum of `e` over all atoms in every monomial is at
most four.  This is contradicted by the frozen exact artifact
`FULL_L2_PAIRED_ORDER5_MAP.json`.

Direct enumeration of its 979 nonzero monomials gives

\[
\begin{array}{c|rrrrrrrrr}
\text{total }e&0&1&2&3&4&5&6&7&8\\ \hline
\#\text{ monomials}&6&24&86&126&244&198&186&73&36.
\end{array}
\]

For example, the monomial with coefficient `18` containing the nontrivial
atoms

\[
 X_{(1,2,1,0,0,0)},\qquad
 Y_{(0,0,2,0,0,0)},\qquad
 Y_{(0,2,2,0,0,0)}
\]

has total excess `1+2+2=5`.  (It also contains three harmless
`X_(0,2,0,0,0,0)` atoms.)  The maximum excess of one individual atom is
four, but excesses add across the several atoms created by the Wick--Stein
peel.  Therefore lines (5.7)--(5.10) cannot be justified by the four cases
listed there.

The finite-dimensional tensor identity does imply an excess-four statement
*before* Gaussian peeling, at the level of the connected marked source.
Gaussian integration by parts can redistribute that source into several
one-dimensional atoms and raise their termwise displayed excess.  Hence a
valid proof must do one of the following:

1. keep the complete pre-Stein marked source and prove a width-uniform
   integrable remainder estimate there; or
2. give a coefficientwise cancellation certificate for the 979-term
   flattened map after inserting the transition profile.

The current paragraph does neither.  Merely saying that Faà di Bruno cannot
increase excess misses the later Stein differentiations.

There is evidence that a repair may exist.  A census of the exact artifact
shows that no monomial has two atoms of type `(e=4,k>=2)`, where `k` is the
number of derivative factors of order at least two.  After removing the
linear `(e=4,k=1)` atoms that require integration-by-parts cancellation, the
only terms with zero scaling margin under
`w=delta*sqrt(gamma(X))` consist of a single `(e=4,k=2)` atom.  This is the
candidate principal sector.  But this census is not yet a proof of (5.10):
one must also expand the value and slope factors, verify all cancellations
among the `(4,1)` atoms, and identify the sum of all `(4,2)` coefficients
with (4.5).

One useful part of that identification can already be certified.  For a
new lower-layer transition, the canonical map has exactly three regular-
top companion monomials in the principal sector, at indices 685, 686, and
691 of the JSON artifact.  Their integrated coefficients are respectively

\[
 15,\qquad -25,\qquad {25\over8},
\]

coming from `(psi''')^2`, `psi'' psi''''`, and the first slope variation
beside `psi^(5)`.  Their sum is `-55/8`, and all carry the common factor
`b^4 d^3`.  There is no canonical monomial containing such a lower
principal atom together with another high-derivative atom.  The executable
certificate is `audit_paired_excess.py`.  This closes the displayed lower
principal coefficient, but not the complete top/source-response grouping
or the remainder bound.

## 3. The cavity statement must be replaced by a marked empirical limit

Equation (5.4), as written, conditions an average indexed by all `j` on the
event `u_j=X`; it is not a well-formed statement with a single fixed
conditioning index.  The result actually needed is: for every bounded
compactly supported test function `q`,

\[
 \lim_{n\to\infty}
 \mathbb E\left[{1\over n}\sum_{j=1}^n q(u_j)b_j^6\right]
 =15d^3\,\mathbb E q(G).                       \tag{A.1}
\]

This can be repaired.  By exchangeability the left side is
`E[q(u_1)b_1^6]`.  Conditional on all lower activations, the row summands in
`b_1` are independent and centered because of the independent centered
readout `a_i`.  For every fixed `u_1=x`, the covariance between `W_i1` and
the corresponding top preactivation is `psi(x)/sqrt(n)`, so the conditional
variance tends to `d=E psi'(G)^2`.  A conditional triangular-array CLT gives
`b_1=>N(0,d)`.  Rosenthal's inequality, bounded `psi'`, and Gaussian moments
give a locally uniform twelfth-moment bound.  Dominated convergence over
the compact support of `q` proves (A.1).  The transition calculation must
invoke (A.1), not (5.4).

This repair still does not prove the full remainder estimate, because it
only closes the displayed principal lower-node term.

## 4. Normalization is not merely multiplication by a scalar

The sentence following (5.12) is insufficient.  If a new unnormalized
transition is inserted, subsequent RMS normalization both rescales the new
transition and globally rescales the old activation.  The latter produces
an additive change in `beta`; it is not literally just multiplication of
the principal coefficient.

There is a workable estimate.  Write

\[
 \widehat\Phi=\Phi+\delta S_{X,w},\qquad
 S'_{X,w}=R((\cdot-X)/w),\qquad S_{X,w}(0)=0.
\]

For the construction, `|x|<=|Phi(x)|<=2|x|`, so
`1<=||Phi(G)||_2<=2`.  Moreover

\[
 \|\widehat\Phi-\Phi\|_{L^2(\gamma)}
 \le \delta\|(G-X+O(w))_+\|_2,
\]

and therefore the normalization constants differ by the same quantity.
The normalized activations obey

\[
 d_1\!\left({\widehat\Phi\over\|\widehat\Phi(G)\|_2},
             {\Phi\over\|\Phi(G)\|_2}\right)
 \le C\delta.                                  \tag{A.2}
\]

For the singular-sector proof one needs the sharper Gaussian-tail version
of the normalization change and must insert it into the finite polynomial
moment map.  Since the background truncation is fixed at each stage, its
normalization-induced coefficient change is bounded by a finite
background-dependent constant times that tail.  Choosing `X` after fixing
the background can then make this negligible.  None of these estimates is
currently written in the proof.

For the later diagonal continuity argument, the coarse bound (A.2) is
enough and yields

\[
 d_1(\psi_N,\phi)\le C\sum_{q>N}\delta_q.       \tag{A.3}
\]

## 5. The three-epsilon width-limit argument is sound once budgets are
## made numerical

Assume (A.3).  For each `N`, `k in {1,2}`, and integer `m<=N`, let
`C_N(k,m)` and `epsilon_N(k,m)` be the constants from Lemma 2.1 with
background `psi_N` and `R=m`.  It is enough to impose

\[
 C\sum_{q>N}\delta_q
 \le \min_{k\le2,m\le N}
 \left\{\epsilon_N(k,m),{2^{-N}\over C_N(k,m)}\right\}. \tag{A.4}
\]

Then, for fixed `m,k`,

\[
 \sup_n\sup_{|h|\le m}
 |\mathbb Ef_{k,n}^{\phi}(h)-\mathbb Ef_{k,n}^{\psi_N}(h)|
 \le2^{-N}
\]

for all sufficiently large `N`.  Since the middle sequence has a width
limit, the outer sequence is Cauchy in width.  This proves existence and
finiteness of the final activation's expected width-first output at each
fixed `h`.

The current budget (6.5a) gestures at (A.4) but does not state the
normalization constant in (A.3) or the separate continuity constants.  This
is a presentational gap, not the main obstruction.

For the diagonal lower bound at `h_N`, allocate the output-continuity error
to the *sum* of the one-step and two-step comparisons, for example at most
`h_N^5/2` each.  Together with the unit Taylor error and the cubic tail
`|kappa_infinity-kappa(psi_N)|/h_N^2<=1`, this gives the displayed finite
constant in (6.7).  Without such an allocation, the particular number `3`
is not implied by the prose.

## 6. Exact remaining proof obligation

To promote Theorem 1.1, it remains necessary to prove, for every fixed
smooth truncation background, a bound of the form

\[
 \left|\operatorname{Rem}_{\delta,w,X}\right|
 \le C_{\rm bg}P_{\rm bg}(X)
       \{\delta+\sqrt{\gamma(X)}\}
       \gamma(X)\delta^2w^{-3},
 \qquad w=\delta\sqrt{\gamma(X)},              \tag{A.5}
\]

after all paired-map cancellations and normalization terms are included.
The constants may depend on the fixed truncation background.  A valid
certificate must include:

- the pre-Stein marked-source inventory or all 979 flattened monomials;
- the transition expansion of every value/slope/high-derivative factor;
- the three integrations by parts for the complete linear fifth-derivative
  sector, including boundary terms;
- coefficientwise identification of the sole zero-margin quadratic sector
  with `-55/8*d^3*b^4*int(rho')^2` plus the nonpositive top sector;
- the joint marked empirical limit (A.1); and
- the additive RMS-normalization error.

Until (A.5) is supplied, (5.12) and the full-network counterexample remain
open.
