# Quantifier and limit audit of the full-`L=2` diagonal

## Verdict

The diagonal passage

\[
 \text{smooth finite truncations}
 \longrightarrow \text{fixed nonzero witnesses }h_N
 \longrightarrow \text{one }C^\infty\text{ bounded-slope activation}
\]

is valid after two explicit bookkeeping repairs.  It does not interchange
width and learning-rate limits.  Its premise is the insertion statement

\[
 \beta(\psi_N)\le-N,qquad
 |\kappa(\psi_N)-\kappa(\psi_{N-1})|\le e_N
 \tag{Q.1}
\]

for arbitrarily small new amplitudes.  Thus the diagonal proves the final
counterexample **conditional on the full response-aware transition lemma**.
It cannot repair a gap in that lemma.

If (Q.1) is available, the exact conclusion is

\[
 \sup_{0<|h|\le r}
 { |F_2^\phi(h)-F_1^\phi(2h)-\kappa h^3|\over |h|^5}
 =\infty
 \quad(r>0,\ \kappa\in\mathbb R).              \tag{Q.2}
\]

This is already a failure at horizon `t=1`.  It refutes every proposed
uniform theorem with a finite activation-dependent constant valid for all
`t`, because such a theorem must include `t=1`.  It does **not** prove that
a sequence of finite coefficients grows super-`t^5` as `t->infinity`, and
it says nothing about the literal fifth Taylor coefficient of the final
activation, which need not exist.

## 1. RMS normalization and `d_1` tails

Let

\[
 g_N=1+\sum_{m\le N}\delta_mR_m,qquad
 \Phi_N(x)=\int_0^xg_N(y)\,dy,qquad
 q_N=\|\Phi_N(G)\|_2,qquad \psi_N=\Phi_N/q_N.
\]

Under `delta_m<=2^(-m-4)`,

\[
 1\le g_N\le {17\over16},qquad
 |x|\le|\Phi_N(x)|\le{17\over16}|x|,qquad
 1\le q_N\le{17\over16}.                      \tag{Q.3}
\]

Put `D_N=sum_(m>N)delta_m`.  Since all centers are positive and every
`R_m` lies in `[0,1]`,

\[
 |\Phi(x)-\Phi_N(x)|\le D_N|x|,qquad
 \|g-g_N\|_\infty\le D_N,qquad
 |q-q_N|\le D_N.                               \tag{Q.4}
\]

Equations (Q.3)--(Q.4) imply, with a harmless numerical constant (for
example `5`),

\[
 d_1(\phi,\psi_N)\le5D_N.                      \tag{Q.5}
\]

Thus normalization does not invalidate the final `C^1` approximation.
It must nevertheless be included explicitly in every tail budget.

At a single insertion, normalization is not merely multiplication of the
new principal coefficient.  Writing

\[
 \widehat\Phi=\Phi_{\rm old}+\delta S_{X,w},qquad
 0\le S_{X,w}(x)\le(x-X+w/4)_+,
\]

gives

\[
 |\|\widehat\Phi(G)\|_2-\|\Phi_{\rm old}(G)\|_2|
 \le\delta\|(G-X+w/4)_+\|_2.                  \tag{Q.6}
\]

For a fixed old truncation, its cubic and fifth moment maps are finite
polynomials.  Their additive change under the global rescaling in (Q.6) is
therefore bounded by a finite old-background constant times the right side
of (Q.6).  Choosing `X` after fixing the old truncation, and then choosing
`delta`, makes this negligible relative to the proposed principal scale.
The phrase “normalization only multiplies the coefficient” is false, but
(Q.6) is the required repair.

## 2. Simultaneous tail budgets exist

At the end of stage `N`, only finitely many conditions have been created.
For each `j<=N`, reserve a positive budget `B_j` and require future
amplitudes to satisfy

\[
 \delta_m\le2^{-(m-j+1)}B_j\qquad(m>j).        \tag{Q.7}
\]

Then `sum_(m>j)delta_m<=B_j`.  At stage `m`, (Q.7) gives only finitely many
upper bounds.  The insertion premise must therefore hold for arbitrarily
small `delta_m`; under that quantifier the recursion cannot get stuck.

For the cubic tails, choose

\[
 e_m\le2^{-m-2}\min_{j<m}h_j^2.                \tag{Q.8}
\]

Then, for every fixed `N`,

\[
 \sum_{m>N}e_m\le {1\over2}h_N^2.             \tag{Q.9}
\]

## 3. Width-first fixed-step limits of the final activation

For each background `psi_N`, terminal time `k in {1,2}`, and integer
step interval `|h|<=m`, let `epsilon_N(k,m),C_N(k,m)` be the constants in
the width-uniform `d_1` stability lemma.  Use (Q.5) and impose

\[
 5D_N\le
 \min_{k\le2,m\le N}
 \left\{\epsilon_N(k,m),{2^{-N}\over C_N(k,m)}\right\}. \tag{Q.10}
\]

For fixed `h`, choose an integer `m>=|h|`.  For every `N>=m`,

\[
 \sup_n
 |\mathbb Ef_{k,n}^{\phi}(h)-\mathbb Ef_{k,n}^{\psi_N}(h)|
 \le2^{-N}.                                    \tag{Q.11}
\]

Since the expected output for the smooth `psi_N` has a width limit, (Q.11)
makes the expected output sequence for `phi` Cauchy in width.  This proves
existence and finiteness of `F_1^phi(h)` and `F_2^phi(h)` at every fixed
nonzero `h`.  The order is: choose the truncation, take width to infinity
at that fixed `h`, and only then let the truncation index grow.  No
finite-width Taylor expansion is transferred to the final activation.

## 4. Fixed nonzero witnesses and divergence

For each smooth `psi_N`, first use its width-first fifth jet to choose a
number `h_N>0` such that

\[
 h_N<N^{-1},\qquad
 |\beta_N|h_N^2\le N^{-1},                     \tag{Q.12}
\]

and

\[
 \left|{Delta_1^{\psi_N}(h_N)-\kappa_Nh_N^3\over h_N^5}
          -\beta_N\right|\le1.                \tag{Q.13}
\]

This choice occurs after the width-first germ of the fixed smooth
truncation has been established.  It is therefore a fixed nonzero-step
statement, not a width/Taylor interchange.

After choosing `h_N`, strengthen (Q.10) so that the *combined* one- and
two-step output error at `h_N` is at most `h_N^5`, and impose (Q.9).  With

\[
 \kappa_\infty=\lim_N\kappa_N,
\]

one obtains

\[
 \left|{Delta_1^\phi(h_N)-\kappa_\infty h_N^3\over h_N^5}
 \right|\ge|\beta_N|-3\longrightarrow\infty.  \tag{Q.14}
\]

Moreover, (Q.12)--(Q.14) give

\[
 h_N^2{Delta_1^\phi(h_N)-\kappa h_N^3\over h_N^5}
 \longrightarrow\kappa_\infty-\kappa.        \tag{Q.15}
\]

Thus the quotient also diverges for every `kappa!=kappa_infinity`.
Because `h_N->0`, (Q.2) follows.

## 5. Old bumps and cross terms

Putting the new transition to the right of all old transitions makes the
old activation affine on the new support.  Within one Gaussian moment atom,
old and new derivatives of order at least two have disjoint supports, so
mixed old/new high-derivative products vanish.  Across distinct atoms, old
high-derivative moments are fixed finite coefficients.

For a correct atomwise margin audit, however, one must test every nonempty
subset of high-derivative atoms as the set assigned to the new transition;
testing only the all-new assignment is insufficient.  Exhaustive subset
enumeration of the frozen 979-term map gives:

- no negative-margin subset;
- 267 zero-margin subset instances, each consisting of one effective
  `(e,k)=(4,2)` new block.

Some apparent `(4,2)` blocks arise by conservatively replacing a lone
`phi^(5)` block `(4,1)`.  Such a block is genuinely principal only when a
new slope factor shares its Gaussian atom; otherwise three integrations by
parts give positive margin.  The complete true zero-margin sum must be
grouped before absolute values.  The finite-dimensional node symbol gives

\[
 -{11\over24}r^2sv^4\,{\delta^2\over w^3}
   \int(\rho')^2\le0,                          \tag{Q.16}
\]

and the lower nodes have the strict weight

\[
 -{55\over8}d^3b^4\gamma(X){\delta^2\over w^3}
   \int(\rho')^2.                              \tag{Q.17}

Therefore old bumps do not invalidate the insertion **provided** the exact
paired-map/finite-width intertwining groups all 267 zero-margin subsets
into (Q.16).  A margin census alone does not prove that grouping.

## Claim boundary

The diagonal and the final fixed-step width limits pass after (Q.5),
(Q.7), and (Q.10) are written explicitly.  Normalization and old bumps are
controllable; neither is an intrinsic obstruction.  The only substantive
remaining issue is the response-aware identification and grouping of the
zero-margin transition sector.  Until that bridge is independently
verified, (Q.2) is conditional rather than a completed theorem.
