# Within-study cross-review: discrete plateau levels or upper-parameter escape

Reviewer: the previously frozen symmetry/counterexample route.
Date: 2026-09-18. This is a transparent within-study cross-review, not a
fresh isolated promotion review. No experiment was performed. The source
was preserved without modification, and no other reader's verdict was
provided or read.

Reviewed source: `plateau_upper_escape.md`, complete file.

SHA256:
`7ab04db2641015bf00feccc9fbec9df57b9f361aea4c9dd6636c1f08acd25490`.
The supplied hash was verified before review.

Allowed scientific inputs were the source, complete
`terminal_geometry.md`, the canonical initialization/equations and
existence material already read for this route, and the route's own
earlier scoped inputs. The required mathematical and research skills
and their previously read contract/audit references were retained.

## Verdict

**PASS for the exact stated necessary-condition theorem.** The proof
correctly establishes the finite plateau list under the existence of
any sequence of simultaneously bounded readout and middle-matrix norms.
Its contraposition gives divergence to infinity of the sum of these
norms whenever the limiting loss is outside that list. No mathematical
correction is required.

In particular, the proof neither needs nor covertly assumes convergence
or compactness of the lower population, convergence of the readout,
bounded lower increments for all time, or vanishing of the other two
gradient blocks along the selected sequence. It does not prove that
any compatible law reaches a positive plateau or that escape implies
failure to fit.

## 1. Canonical representation and contraction constants

The exact initialized odd-mark sector removes the inactive constant
coordinates. This sector is preserved by the full equations, as shown
in `docs/observable_p1.md`; using it is therefore an exact representation
of the canonical trajectory. The three-dimensional effective vectors
used in the terminal-independence lemma are legitimate even if the
full constant-coordinate representation is retained operationally.

For either normalized feature column, if `L L^T=G+eta I`, then

\[
 E[bb^T]=L^{-1}GL^{-T}=I-\eta L^{-1}L^{-T}\le I.
\]

Thus both synthesis `z -> b^Tz` and its population adjoint are
contractions. In particular
`|a_i|<=1`, `|d_i|<=||c||_2`, and
`||b_1^T M^T d_i||_2<=||M||_F ||c||_2` hold with precisely the
constants used in the source. No supremum bound on `w-g` enters.

The initial population readout is exactly zero, hence the initial
physical unhalved loss is one. Energy dissipation gives `L<=1` and
`sum_i p_i|r_i|<=1`. These facts verify all factors of two in the
source's estimates (5):

\[
 \|c'\|_2\le2,\qquad\|M'\|_F\le2C,
 \qquad\|w'\|_2\le2BC,
 \quad B=\|M\|_F,\ C=\|c\|_2.
\]

For the matrix estimate, use the Frobenius norm of each rank-one
matrix `d_i a_i^T`. For the row estimate, use Minkowski, the unit input
norm, the lower gate bound, and the synthesis contraction. The full
moving matrix and its actual transpose are retained throughout.

## 2. Differentiation and the readout-acceleration estimate

On every finite-time interval the canonical characteristic solution
has bounded lower increment, bounded readout and finite matrix. The
bounded-feature smooth vector field permits differentiation of the
following contractions on that interval. This is only the local
regularity needed to derive bounds; their resulting constants are
independent of the size of the lower increment.

The precise derivatives and bounds are

\[
 a_i'=E_1[b_1\phi'(w\cdot u_i)(w'\cdot u_i)],
 \qquad |a_i'|\le\|w'\|_2,
\]
\[
 v_i'=M'a_i+Ma_i',\qquad
 |v_i'|\le2C+2B^2C=2C(1+B^2),
\]
\[
 H_i'=\phi'(b_2\cdot v_i)(b_2\cdot v_i'),\qquad
 \|H_i'\|_2\le|v_i'|,
\]
\[
 f_i'=\langle c',H_i\rangle+\langle c,H_i'\rangle,
 \qquad |f_i'|\le2+2C^2(1+B^2).
\]

Consequently differentiating
`c'=-2 sum_i p_i r_i H_i` gives

\[
 \begin{split}
 \|c''\|_2
 &\le2\sum_i p_i|f_i'|\|H_i\|_2
       +2\sum_i p_i|r_i|\|H_i'\|_2\\
 &\le4+4C^2(1+B^2)+4C(1+B^2).
 \end{split}
\]

This exactly matches (7). There is no missing product requiring an
upper-population supremum bound, and no differentiation of an
uncontrolled second lower derivative is needed.

## 3. Every bounded-upper-parameter sequence has small readout velocity

If `B(t_n),C(t_n)<=R`, the norm triangle inequality and the preceding
velocity bounds give, for `t in [t_n,t_n+1]`,

\[
 C(t)\le R+2,\qquad B(t)\le R+2(R+2)=3R+4.
\]

The matrix estimate is deliberately loose but correct. An explicit
permitted common acceleration bound is

\[
 Q_R=4+4\bigl((R+2)^2+(R+2)\bigr)
                    \bigl(1+(3R+4)^2\bigr)>0.
\]

Therefore, if `||c'(t_n)||_2>=epsilon`, throughout the following
interval of length
`delta=min(1,epsilon/(2Q_R))` one has
`||c'(t)||_2>=epsilon/2`. Each such interval expends at least
`delta epsilon^2/4` of the readout dissipation budget. From any
unbounded sequence of their starting times one can select infinitely
many disjoint intervals of this common length. This contradicts

\[
 \int_0^\infty\|c'(t)\|_2^2dt\le1.
\]

If convergence of `c'(t_n)` to zero failed, an epsilon subsequence of
exactly this kind would exist. Thus (8) holds along every bounded
sequence in the theorem, not just along a specially chosen
energy-subsequence. Forward local bounds suffice; the argument does
not require a bounded neighborhood preceding `t_n`.

## 4. Coefficient limits and collisions without a readout limit

Bounded `M(t_n)` and `|a_i|<=1` give compactness of the three effective
coefficient vectors in a finite-dimensional Euclidean space. After
subsequence extraction they converge to `v_i^*`. The prediction
coordinates are bounded, either by `|f_i|<=C<=R` or by the individual
weighted residual bounds, so a further common subsequence supplies
`f_i^*`.

The Lipschitz activation and upper synthesis contraction give the
strong convergence estimate

\[
 \|H_i(t_n)-\phi(b_2\cdot v_i^*)\|_2
 \le|v_i(t_n)-v_i^*|\longrightarrow0.
\]

Finite sums and scalar prediction convergence then pass the readout
equation to the limit, yielding (9).

The bounded readout norm is used exactly where it is needed:

\[
 |f_i(t_n)|\le R\|H_i(t_n)\|_2\to0
       \quad\text{if }v_i^*=0,
\]
\[
 |f_i(t_n)-\sigma_i f_G(t_n)|
 \le R\|H_i(t_n)-\sigma_iH_G(t_n)\|_2\to0
\]

within a signed-equality group, choosing its representative from the
actual indices. Neither inequality needs a weak or strong limit of
`c(t_n)`. Without bounded `C(t_n)` this inference could fail, so its
presence in the theorem is substantive rather than redundant.

The complete three-feature independence proof in
`terminal_geometry.md` was checked: the canonical upper mark law has
positive density on an open cube; a continuous almost-sure relation
therefore holds on that cube; a direction outside the finite forbidden
hyperplanes gives nonzero projections with distinct squares; and the
nonzero first, third, and fifth tanh coefficients give an invertible
Vandermonde system for at most three representatives. Nonzero
representatives distinct modulo sign meet every hypothesis.

Thus the only surviving readout relations are precisely the signed
groups, and (9) implies

\[
 F_G=\frac{\sum_{i\in G}p_i\sigma_i y_i}{W_G}.
\]

The weighted sum of squared residuals in that group is
`W_G-(sum p_i sigma_i y_i)^2/W_G`. Zero effective vectors contribute
their weights because the labels have magnitude one. This verifies
the full limiting-loss formula (11) without any omitted compactness
assumption.

## 5. Enumeration, gap, and escape quantifier

All partitions of three indices were checked:

| Zero effective vectors | Remaining signed groups | Loss values |
| --- | --- | --- |
| Three | None | `1` |
| Two | One singleton | `p_i+p_j` |
| One | Two singletons or one label-consistent group | `p_k` |
| One | One mixed group | `p_k+4p_i p_j/(p_i+p_j)` |
| None | All groups label-consistent | `0` |
| None | One mixed pair and one singleton | `4p_i p_j/(p_i+p_j)` |
| None | One mixed three-member group | `4p_i(1-p_i)` |

Here label consistency is after orienting each feature by its group
sign. For a mixed group with total oriented-positive mass `a` and
oriented-negative mass `b`, its contribution is

\[
 (a+b)-(a-b)^2/(a+b)=4ab/(a+b)\ge2\min(a,b)\ge2p_{\min}.
\]

A nonzero contribution from zero vectors is at least `p_min`, proving
the claimed positive gap. This is a lower bound on positive values
in the finite necessary list, not on arbitrary escaping trajectories.

For equal weights the list reduces to
`{0,1/3,2/3,8/9,1}`. A nonstationary canonical initialized solution
has nonzero initial vector field: otherwise uniqueness would identify
it with the constant solution. Its initial energy derivative is
strictly negative, giving `L_infinity<1`. The positive nonstationary
list in (4) is therefore correct, without an extra compatibility
assumption.

Finally, failure of
`||c(t)||_2+||M(t)||_F -> infinity` means that some finite bound is
attained at arbitrarily late times. Those times form a sequence on
which both nonnegative norms are bounded. The theorem then forces
`L_infinity in V(p)`. This is the exact contraposition needed for
(3), and proves divergence of the sum rather than merely unboundedness
or a diverging limsup. It does not assert that either individual norm
has a limit or diverges separately.

## 6. Separate self-audit of the earlier symmetry route

The complete current `plateau_symmetry_counter.md` was self-audited at
SHA256
`8cf53803da47ef86977407c40fd5f6ab37778bf237e5cb21a0b10075e5d60288`.
This is a self-check and is not independent evidence for that route.

No mathematical correction was found. The following potentially
delicate steps were rederived:

- The mark/state action in (3) uses `T_R^{-1}` and gives
  `a_{U_R theta}(u)=R_1 a_theta(R^{-1}u)` and
  `f_{U_R theta}(u)=f_theta(R^{-1}u)` with the displayed matrix
  orientation. The inherited symmetry proof is correct.
- The fitting readout `K^{-1}1` is invariant under every data
  permutation because both `K` and `1` are preserved. It requires
  no transitivity or equal weights.
- The scalar-clock state bounds, derivative of `F^2/C`, finite
  fitting clock, and physical factor `exp(-4kt)` have the stated
  constants and signs.
- A signed permutation inducing a three-cycle on the data must
  have an underlying coordinate three-cycle. A negative product of
  coordinate signs would make its cube `-I`, contradicting the
  cycling of nonzero points. The remaining signed cycles are
  diagonal-sign conjugates of the canonical cycle, as claimed.
- In the reflection family, the invariant coefficient geometry
  `(A,+/-B,0),(-C,0,0)` and readout parities give exactly the
  necessary bounded-endpoint losses `{q,2p,8pq}`. The simultaneous
  `A=C=0` case has loss one and is excluded by strict initial
  descent. No sufficiency or initialized reachability was claimed.

One typographical correction is identified separately: equation (5)
of that frozen source currently contains the literal text
`f_t(v)quad(R\in G)`; the intended separator is
`f_t(v)\quad(R\in G)`. This does not change the statement or proof.
The frozen source was left unchanged by this review.

The new upper-parameter theorem is compatible with, and stronger in
its compactness assumptions than, the earlier route's finite-endpoint
necessary conditions. This review does not silently replace those
earlier claims or turn the reflection candidate into a constructed
counterexample.
