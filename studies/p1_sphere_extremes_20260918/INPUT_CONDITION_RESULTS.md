# Input restrictions and loss sublevels for the p=1 basin theorem

Lead synthesis and additional sublevel theorem, 2026-09-18. This continues
the same study. Scientific inputs are the complete established
`docs/observable_p1.md`, the canonical saved-state and metric sections
already listed in the README, and this study's complete
`dependent_basin_functional.md`, `dependent_hilbert_geometry.md`,
`DEPENDENT_BASIN_RESULTS.md`, `finite_critical_loss_gap.md`,
`input_condition_geometry.md`, and `input_condition_regularity.md`.
The two last reports were developed independently before comparison.
Check status and source hashes are recorded in the README. No promotion,
simulation, finite-network substitution, or external theorem is used.

## 1. What the new input condition achieves

There is a complete extension of the equal-weight three-input theorem to
an open family of dependent four-input configurations. It uses the signs
of a linear relation after incorporating the labels. It requires neither
independence of all inputs nor an exact reflection or angular symmetry.

There is not yet a mild, almost-everywhere input restriction restoring the
whole loss sublevel `(0,1)` for arbitrary sample count. A proposed analytic
rank certificate is sufficient, but fails for every dependent equal-weight
family of five or more inputs. This is a proved limitation of that
certificate, not a proof of a positive-probability bad basin.

Two larger-sample results remain: an explicit circuit-dependent loss
threshold, and a universal small-loss basin theorem allowing arbitrarily
many inputs in a fixed dimension. Their smaller sublevels are part of
their statements, not conclusions that initialized training enters them.

## 2. Exact model and meaning of the basin conclusion

Take `n` points `x_i` on `sqrt(d) S^(d-1)`, `d>=2`, binary labels `y_i`,
and equal masses `1/n`, unless another weighting is stated. No pair is
equal or antipodal. Write `u_i=x_i/sqrt(d)` only in the proofs. Preserve
the canonical correlated marks `(b_1,g)` and `b_2`, ridge `1/4096`, odd
sector, full trained `M`, actual transpose, and physical time. With
`phi=tanh`, set

\[
a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,
\quad H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\]
\[
\rho_i=(f_i-y_i)/n,\quad
d_i=E_2[b_2c\phi'(b_2\cdot v_i)],\quad T_i=\rho_iM^Td_i.
\tag{1}
\]

The lower stationarity equation is

\[
\sum_i\phi'(w\cdot u_i)(b_1\cdot T_i)u_i=0
\quad\hbox{almost surely}.
\tag{2}
\]

All three blocks follow their exact gradient flow. The state space is

\[
\mathcal H_d=L^2_{\rm odd}(P_1;\mathbb R^d)
\oplus L^2_{\rm odd}(P_2)\oplus\mathbb R^{d\times2d},
\qquad\theta=(w-g,c,M).
\tag{3}
\]

For a stated threshold `ell`, the basin conclusion means that

\[
\{\theta_0:\theta_t\to\theta_*\text{ in }\mathcal H_d,
                       \quad0<L(\theta_*)<\ell\}
\tag{4}
\]

is contained in a countable union of closed Lipschitz hypersurfaces.
In particular it is meagre and has a shy Borel hull. The same hull has
outer probability zero under every translation and positive rescaling of
the specified Gaussian series: choose bounded odd unit directions `e_j`
dense in the H unit sphere, including matrix directions, and use

\[
\theta_0=\theta_{\rm ref}
 +\varepsilon\sum_{j\ge1}
 \frac{2^{-j}}{1+\|e_j\|_b}\,g_je_j,
\qquad\varepsilon>0,
\tag{5}
\]

where the `g_j` are independent standard Gaussians and the b-norm is the
sum of the two essential-supremum norms and Frobenius norm. This has full
H support and bounded increments almost surely. It randomizes population
fields, not the frozen marks already integrated in the population law.
It is not an infinite-dimensional Lebesgue statement.

Under (5), conditioned on `L(theta_0)<ell`, physical state convergence
therefore implies fitting almost surely. These theorems do not establish
state convergence, entry into the sublevel, success from the deterministic
canonical state, or an exponential rate. They do not exclude positive-loss
escape without a state limit.

## 3. The four-input condition, with a mixed-label example

Suppose `n=4`, the input rank is three, and every triple is independent.
Let the unique relation up to scale be

\[
\sum_{i=1}^4\alpha_i x_i=0.
\tag{6}
\]

Every coefficient is nonzero. Require exactly two of the numbers
`alpha_i y_i` to be positive and two to be negative. The choice of sign
or scale of `alpha` does not affect this condition.

**Theorem.** For these data the entire basin conclusion (4) holds with
`ell=1`, with no bound on endpoint fields beyond membership in H.

For an explicit balanced-label example choose `C,S>0`, `C^2+S^2=1`, and

\[
\begin{array}{c|c}
x_i/\sqrt3&y_i\\ \hline
(C,S,0)&+1\\
(C,-S,0)&+1\\
(-C,0,-S)&-1\\
(-C,0,S)&-1
\end{array}
\tag{7}
\]

The inputs sum to zero, every triple is independent, and their relation
has `alpha=(1,1,1,1)`. Thus `alpha_i y_i` has signs `(+,+,-,-)`.
There are no parallel pairs. Small independent angular perturbations in
`(S^2)^4` preserve all nonzero triple determinants and the relation signs.
Consequently (7) lies inside an open family; no displayed symmetry is an
assumption of the theorem. In three dimensions the four vectors remain
linearly dependent throughout that open family.

For fixed labels, other sign patterns also occur on open sets. Therefore
this family has positive angular measure but is not dense, and its
complement is not merely a measure-zero exceptional geometry.

Here is the proof mechanism. At an equilibrium group the nonzero `v_i`
by equality modulo sign, `v_i=sigma_i v_G`; the zero vectors form one
zero group. Independence of finitely many distinct upper tanh functions
gives

\[
f_i=\sigma_i F_G,\qquad
F_G=\frac1{|G|}\sum_{j\in G}\sigma_j y_j,
\qquad \operatorname{sign}\rho_i=-y_i\text{ if }\rho_i\ne0.
\tag{8}
\]

Every residual-bearing nonzero group has at least two elements. The
complete elementary feature-independence proof is in
`finite_critical_loss_gap.md`; it uses positive upper density, a generic
line, analyticity, and successively distinct exponential decay rates.

If some `T_i` is nonzero, (2) and the one-dimensional input kernel force
all `T_i` to be nonzero and

\[
T_i=\alpha_i\kappa_i q,\qquad \kappa_i>0,\quad q\ne0.
\tag{9}
\]

Indeed the linear forms `b_1 dot (T_i/alpha_i)` have the same sign almost
surely because every derivative gate is positive. The lower mark law has
positive density near zero. Two nonzero linear forms with this sign
property must be positive multiples: independent forms take opposite
signs on an open set, and negative proportionality also violates the
property. This proves (9), without a bound on `w-g`.

Within an effective-vector group the `d_i` are identical because `phi'`
is even. Combining this fact, (8), and (9) shows that `alpha_i y_i` has
constant sign within that group. Each sign class has only two members.
Thus every residual-bearing nonzero group is a conflicting pair whose
equal weights force `F_G=0`. The zero group predicts zero as well.
Every residual is nonzero by (9), so every prediction is zero and `L=1`.
This contradicts `0<L<1`. All `T_i` must therefore vanish.

For negative curvature, the labeled vectors `y_i u_i` are strictly
linearly separable from zero. To prove this rather than assume it, their
unique kernel vector is `beta_i=alpha_i y_i`, which has both signs.
Choose a strictly positive vector `p` with `beta dot p=0`. Since the
range of the transpose of the labeled input matrix is `beta^perp`, there
is `a` with `y_i a dot u_i=p_i>0`. For every residual-bearing group,

\[
R_G(s)=\sum_{i\in G}\rho_i\phi'(s\cdot u_i)u_i
\quad\hbox{satisfies}\quad a\cdot R_G(s)<0
\tag{10}
\]

at every finite `s`. This provides the mixed lower/readout negative
direction described in Section 6. Together with `T_i=0`, it proves all
regularity and instability hypotheses needed for (4).

## 4. One relation, any sample count: an explicit loss threshold

Suppose the entire input list is a minimal dependent set: its rank is
`n-1` and every proper subset is independent. Define

\[
m(1)=1,\qquad m(k)=4(k-1)/k\quad(k\ge2).
\tag{11}
\]

Let `a,b` be the numbers of positive and negative entries of
`alpha_i y_i`. If both occur, set

\[
\ell_*=\frac{m(a)+m(b)}{n}.
\tag{12}
\]

If only one sign occurs, set `ell_*=m(n)/n`. Then (4) holds with
`ell=ell_*`. The threshold is sufficient; no claim of sharpness for
actual equilibria or actual basin probability is made.

The sign argument (9) still holds if any `T_i` is nonzero. All inputs
then have nonzero residuals, and each effective group lies in a single
relation-sign class. A nonzero group of size `k` with `j` oriented
positive labels has unnormalized loss `4j(k-j)/k`, at least `m(k)`.
A zero group of size `k` has unnormalized loss `k`, at least `m(k)`.
The cost of splitting a sign class cannot be smaller than `m` of its
total size. For two nonzero groups use

\[
m(r)+m(s)-m(r+s)=4-4/r-4/s+4/(r+s)>0
\quad(r,s\ge2).
\]

Adding a zero-group member costs one, while
`m(r+1)-m(r)=4/[r(r+1)]<1` for `r>=2`; an entirely zero class already
obeys the bound. Thus some nonzero `T_i` forces `L>=ell_*`.
Below `ell_*` all coefficients cancel. If both relation signs occur,
the separation proof (10) gives curvature. If only one sign occurs,
an active group containing all inputs would itself cost at least
`m(n)/n`; below it there is a proper active group, whose inputs are
independent and whose vector `R_G` cannot vanish. Section 6 again applies.

Examples are `ell_*=1` for the four-input split `2+2`, `11/12` for the
four-input split `3+1`, and `14/15` for a five-input split `3+2`.
The full argument and formal-partition attainability of these lower
costs were separately checked in `input_condition_regularity.md`,
Section 9. Formal partitions need not be realizable equilibria.

## 5. Arbitrarily many dependent inputs: a universal sublevel theorem

**Theorem.** Suppose `2<=r<n` and every subset of at most `r` inputs is
independent. No independence of larger subsets is required. Then (4)
holds for

\[
\ell_r=\frac{4r}{n(r+1)}.
\tag{13}
\]

In particular, pairwise nonparallel inputs alone give `r=2` and
`ell_2=8/(3n)`. This covers arbitrary finite sample counts on the circle,
as well as in higher dimension. It does not recover the full `(0,1)`
sublevel of the original three-input theorem for all sample counts.

**Proof.** At an equilibrium let `q` be the number of indices with
nonzero residual. The active groups partition exactly those `q` indices.
If `q>=2`, the binary group-cost formula above implies

\[
L\ge \frac{m(q)}{n}=\frac{4(q-1)}{nq}.
\tag{14}
\]

For completeness, merge all nonzero groups, each of size at least two,
using the displayed strict subadditivity of `m`. Then add the zero-group
members one by one using the increment bound after (12). If there were
no nonzero group, the cost is `q>=m(q)`. These exhaust the partitions;
there cannot be several distinct zero groups.

The function `m(q)` is strictly increasing for integer `q>=2`.
Consequently `0<L<ell_r=m(r+1)/n` implies `1<=q<=r`.
All residual-bearing inputs are independent. Equation (2), gate
positivity and the lower mark law now force every active `T_i=0`;
inactive coefficients already vanish. Each active `R_G(w)` is a
nontrivial linear combination of a subset of those independent inputs,
with nonzero coefficients, so it is nonzero almost surely. This proves
both needed endpoint hypotheses; Section 6 yields (4).

This result is stronger than the earlier deterministic critical-loss
gap `L<1/n`: it allows low positive-loss equilibria, and proves their
point-convergent basins null under (5). It still does not prove entry
from loss one. For `r=2`, neither homogeneous label separability nor
a lower bound on input angles is assumed. No numerical diagnostic is
needed for the proof.

If the labeled inputs are strictly linearly separable, meaning there is
`a` with `y_i a dot x_i>0` for every `i`, the threshold improves to

\[
\ell_r^{\rm sep}=\frac{5-4/r}{n}.
\tag{14a}
\]

To verify this, an endpoint with some nonzero `T_i` must have `q>=r+1`
by independence of every smaller active set. It must have at least two
active groups: if there were only one, (10) would make its `R_G(w)`
nonzero, and (2) would cancel its sole grouped coefficient. For `q>=3`,
the cost of at least two active groups is at least `1+m(q-1)`.
If a zero group is present, first merge all nonzero groups and minimize
`z+m(q-z)` over `1<=z<=q-2`; the minimum is at `z=1` since removing
one member from a group of size at least three lowers `m` by less than
one. With no zero group, merge until two nonzero groups remain. Their
minimum cost is `m(2)+m(q-2)` for `q>=4`: the expression
`8-4q/[k(q-k)]` is minimized at `k=2` or `q-2`. It exceeds
`1+m(q-1)` by `1-4/[(q-2)(q-1)]>0`. Hence some nonzero coefficient
forces `L>=(1+m(r))/n=(5-4/r)/n`. Below it cancellation holds, while
(10) supplies curvature. The basin argument is unchanged.

## 6. Why cancellation and the residual vectors suffice

These are the precise existing analytic implications reused above,
valid for any finite input count. Their complete proofs, including
finite-time pullbacks and the probability law, are in
`dependent_basin_functional.md`, Sections 3--5 and 7. The current
reports check their hypotheses with no endpoint boundedness assumption.

At `T_i=0`, the lower gradient is a sum of `G_i(w)T_i(theta)`, where
`G_i(w)t=phi'(w dot u_i)(b_1 dot t)u_i`. The coefficient maps are locally
`C^(1,1)` and `G_i` is bounded and Lipschitz from lower L2 to operators
on a finite vector space. Subtraction of the linear term leaves products
of two first-order increments, so the exact physical field has

\[
F(\theta_*+z)=Az+N(z),\qquad
\operatorname{Lip}(N|_{B_\delta})\le C\delta.
\tag{15}
\]

Its lower multiplication derivative vanishes. The remaining `A` is
self-adjoint and finite rank, with bounded-field range. This is a true
physical-H linearization, not just differentiation in bounded directions.

At positive loss below one, `M!=0`. If some active `R_G(w)` is nonzero
on a set of positive probability, absolute continuity of the marks gives
one coordinate `j` for which the bounded odd direction
`h=(Mb_1)_j R_G(w)` satisfies

\[
\left[\sum_{i\in G}\rho_iM Da_i[h]\right]_j
 =E_1[(Mb_1)_j^2|R_G(w)|^2]>0.
\tag{16}
\]

The finite-family upper derivative-feature separation proof supplies a
bounded odd `k`, orthogonal to the span of the current `H_i`, with

\[
D^2L[(h,tk,0),(h,tk,0)]=Q_h+4t\|k\|_2^2,
\qquad k\ne0.
\tag{17}
\]

A finite negative `t` gives negative curvature. Thus `A` has a positive
eigenvalue and a finite nonzero unstable subspace. The contraction graph
proof splits unstable and center-stable coordinates and uses a path norm
weighted by half the least unstable eigenvalue. Its integral operator
has Lipschitz constant at most `4 epsilon/lambda`; (15) makes this less
than one half on a sufficiently small ball. Every orbit trapped in that
ball lies on the resulting graph of positive codimension.

H separability gives a countable cover of endpoint neighborhoods.
Every point-convergent bad orbit eventually remains in one, and its
state at some integer time lies on that graph. Locally Lipschitz flow
maps have invertible strongly continuous directional derivatives; their
preimages of scalar Lipschitz hypersurfaces have countable hypersurface
covers by the explicit transverse-coordinate proof in the cited source.
Conditioning on one Gaussian coordinate in (5) transverse to each graph
proves nullity. These verify the entire basin assertion, not just a
negative directional variation at an individual equilibrium.

## 7. Failed larger-sample simplifications

One broad positive statement survives without any sample-count or input
rank limitation: strict labeled linear separability gives a negative
bounded second directional variation at every equilibrium with `0<L<1`.
Indeed (8), (10), (16), and (17) apply to any finite family (and also to
positive unequal weights with the weighted version of (8)). Thus these
equilibria cannot be loss local minima. This condition excludes the known
seven-input flat-Hessian construction and every class-moment matching
construction with equal positive and negative class centers. It is a
label-aware input condition, not an independence condition. It does not
by itself prove the Hilbert regularity premise (15), so it is not claimed
to give the full `(0,1)` basin theorem for arbitrary finite sample count.

The data-only rank proposal enumerates signed partitions, computes their
forced residuals from (8), retains formal losses in `(0,1)`, and demands
independence of all active `R_G(s)` for every finite `s`. It is sufficient:
lower stationarity then makes every grouped coefficient vanish. Replacing
the derivative gates by arbitrary positive numbers yields a finite list
of linear feasibility tests. `input_condition_geometry.md` proves both
claims and the four-input theorem independently.

But the exact nonlinear rank proposal itself fails for every dependent
equal-weight family with `n>=5`. The proof in
`input_condition_regularity.md`, Section 8, chooses a minimal input
relation, splits it into two groups homogeneous in `sign(alpha_i y_i)`,
and prescribes the absolute projections by

\[
|s\cdot u_i|=\operatorname{arcosh}
 \sqrt{A_G|\rho_i|/|\alpha_i|}.
\tag{18}
\]

The positive parameters for the two groups can be chosen so the signed
projection vector satisfies the unique circuit relation. It is then an
actual vector of projections of a finite `s`. The exact gates satisfy
`phi'(s dot u_i)=|alpha_i|/(A_G|rho_i|)` and the two residual vectors
are dependent. Outside a proper circuit put fitted singletons; if the
circuit is the entire data set, use an imbalanced group of size at least
three. In either case the formal loss is strictly between zero and one.
This preserves the linkage of the gates through the common vector `s`.

The obstruction does not construct the full population endpoint with
that partition. Thus it disproves a proposed sufficient certificate's
usefulness for these data, not the desired almost-sure fitting theorem.
The next proof must use more of the joint lower/upper stationary equations,
or replace the finite-rank regularity argument.

Excluding moment matching alone is also inadequate. The same report,
Sections 5--6, gives four equally weighted nonparallel inputs with
linearly independent matrices `u_i u_i^T` and a loss-`3/4` equilibrium
having nonzero `T_i` and no second Frechet loss differential. Its first
three inputs are a dependent plane triple with a collapsed zero feature;
the fourth is fitted. The lower triple may be perturbed to remove all
reflection symmetries. This is not a counterexample to the theorem in
Section 3, which requires every triple to be independent, and it does
not show a positive-probability basin.

The current proved boundary is consequently precise: an open four-input
family recovers the full old sublevel, explicit larger circuits recover
large but smaller sublevels, and arbitrary finite nonparallel data recover
a universal small-loss basin theorem. A mild arbitrary-count geometric
condition giving the whole old `(0,1)` theorem remains open.
