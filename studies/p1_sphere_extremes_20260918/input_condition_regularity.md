# Data-only restrictions: a four-input theorem and a no-moment obstruction

Independent scoped functional/geometry candidate, 2026-09-18. Internally
derived, not independently reviewed or promoted. The complete scientific
inputs read were exactly `docs/observable_p1.md`,
`dependent_basin_functional.md`, `dependent_hilbert_geometry.md`,
`DEPENDENT_BASIN_RESULTS.md`, `finite_basin_tail.md`, and
`finite_basin_geometry.md`. The investigate-conjectures and
solve-math-rigorously skills and the research-contract, evidence-ledger,
and adversarial-audit process references were applied. No experiment,
external scientific source, other study, or current sibling route was
consulted. This is the only file written by this route. Sections 1--7
constitute the first candidate, frozen before comparison.

## 1. Contract and strongest conclusions

Keep the exact canonical order-one odd-sector population model, its
correlated Gaussian-derived marks and ridge, the full trained middle
matrix with its actual transpose, and the physical state space

\[
\mathcal H_d=L^2_{\rm odd}(P_1;\mathbb R^d)
 \oplus L^2_{\rm odd}(P_2)\oplus\mathbb R^{d\times2d},
\qquad \theta=(w-g,c,M).
\]

The target is the entire physical-Hilbert basin of point-convergent
endpoints with loss strictly between zero and one. No bounded endpoint
field or displacement, changed topology, or altered state randomization
is permitted. The data have unit inputs, binary labels, positive weights,
and no equal or antipodal inputs. Equal weights are used in the main
theorem and the counterexample.

Two definite results are obtained.

* Four equally weighted inputs spanning a three-dimensional space satisfy
  the full exceptional-basin theorem if every triple is independent and
  the unique input relation has two positive and two negative coefficients
  after orienting each input by its label. This is an open family of
  dependent data and has a complete coefficient-cancellation proof.
* Excluding first- and second-moment matching is insufficient to restore
  coefficient cancellation or Hilbert Hessian regularity. There are four
  equally weighted inputs with linearly independent matrices
  `u_i u_i^T`, an exact equilibrium of loss `3/4`, and nonzero individual
  critical coefficients. The lower triple can have generic asymmetric
  circle angles. The equilibrium lacks a second Frechet differential of
  the loss in the physical Hilbert topology.

The second result is an obstruction to a proof premise, not a
positive-probability basin counterexample. It does not establish that a
no-moment condition fails to imply the basin conclusion by another method.
An arbitrary-finite-count mild generic condition sufficient for the entire
basin theorem is not proved here.

## 2. Exact residual information from readout stationarity

Use the notation

\[
a_i=E_1[b_1\tanh(w\cdot u_i)],\quad z_i=Ma_i,\quad
H_i=\tanh(b_2\cdot z_i),\quad f_i=E_2[cH_i],
\]
\[
\rho_i=p_i(f_i-y_i),\quad
d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot z_i)],\quad
T_i=\rho_iM^Td_i.
\tag{1}
\]

Group the nonzero `z_i` by equality modulo sign, writing
`z_i=sigma_i z_J` for `i in J`. Distinct nonzero tanh ridge functions
modulo sign are linearly independent under the canonical upper law. The
complete argument in the assigned sources applies to every finite number
of groups: positive density extends a putative identity to an analytic
identity; restriction to a generic line gives distinct nonzero absolute
slopes; subtract the limiting constant and remove successive smallest
exponential rates. At an equilibrium, readout stationarity therefore gives

\[
\sum_{i\in J}\rho_i\sigma_i=0,
\qquad
f_i=\sigma_i F_J,
\qquad
F_J=\frac{\sum_{i\in J}p_i\sigma_i y_i}
          {\sum_{i\in J}p_i}.
\tag{2}
\]

All zero effective vectors form one further group, with `f_i=0`.
Since (2) is a weighted average of signs, `|f_i|<=1`. More precisely,

\[
\rho_i\ne0\quad\Longrightarrow\quad -\rho_i y_i>0.
\tag{3}
\]

If one residual in a nonzero group vanishes, `|F_J|=1`; the weighted
average formula then forces all its oriented labels to agree, and every
residual in that group vanishes. Thus each nonzero group either fits
entirely or has nonzero residual at every member. In the latter case it
has at least two members. For equal weights, a two-member nonfitting
group has opposite oriented labels and `F_J=0`.

This information is data-only once the signed partition of the input
indices is specified. The partition itself varies with the endpoint.

## 3. Strict labeled separation supplies curvature, but not regularity

Suppose there exists a vector `a` with

\[
y_i(a\cdot u_i)>0\qquad\hbox{for every }i.
\tag{4}
\]

At any equilibrium, a residual-bearing effective group has

\[
R_J(s)=\sum_{i\in J}\rho_i\operatorname{sech}^2(s\cdot u_i)u_i,
\qquad
a\cdot R_J(s)<0\quad(s\in\mathbb R^d),
\tag{5}
\]

because every nonzero summand has strictly negative projection by (3),
(4), and positivity of the gates. This works for the zero group also.
At loss below one, `M!=0`. The lower-mark marginal is absolutely
continuous, so `Mb_1!=0` almost surely. For some coordinate `ell`, the
bounded odd direction

\[
h=(Mb_1)_\ell R_J(w)
\]

satisfies

\[
\left[\sum_{i\in J}\rho_iM Da_i[h]\right]_\ell
 =E_1[(Mb_1)_\ell^2|R_J(w)|^2]>0.
\tag{6}
\]

The finite-family upper derivative-feature separation proof in the allowed
functional report shows that the resulting residual-weighted upper feature
variation `S` is outside `span{H_i}`. Set
`k=S-P_{span{H_i}}S`. It is a bounded nonzero odd function, has zero first
prediction variation, and obeys

\[
D^2_{\rm dir}L[(h,sk,0),(h,sk,0)]
 =Q_h+4s\|k\|_2^2.
\tag{7}
\]

Here `Q_h` is finite even for `c in L2`, since marks, variations, and
activation derivatives are bounded. A sufficiently negative finite `s`
gives negative directional curvature. No boundedness of `w-g` is used.

This proves a useful arbitrary-finite-count strict-direction lemma. It
does not prove individual cancellation, a Frechet Hessian, a trapping
graph, or basin nullity. Those are separate obligations.

## 4. A complete four-input full-Hilbert theorem

**Theorem.** Let `m=4`, `p_i=1/4`, and let the four unit input vectors have
rank three, with every three independent. Let

\[
\sum_{i=1}^4\lambda_i u_i=0
\tag{8}
\]

be their unique relation up to scale; every `lambda_i` is nonzero. Assume
the four numbers `lambda_i y_i` have two positive and two negative signs.
Then every equilibrium in `H_d` with `0<L<1` has `T_i=0` for all `i` and
has a negative bounded loss direction. Its flow linearization is a
self-adjoint finite-rank operator with a nonzero unstable subspace and a
nonzero stable subspace, and its nonlinear remainder has arbitrarily small
Lipschitz constant on sufficiently small physical-Hilbert balls.

Consequently the union of all its point-convergent positive-loss endpoint
basins with endpoint loss below one lies in a countable union of closed
Lipschitz hypersurfaces in `H_d`. It is meagre, has a shy Borel hull, and
has probability zero under every translation and positive rescaling of
the specified full-support Gaussian-series initial-state law.

**Cancellation proof.** Lower stationarity gives

\[
\operatorname{sech}^2(w\cdot u_i)(b_1\cdot T_i)
 =\Lambda\lambda_i\quad\hbox{a.s.}
\tag{9}
\]

If any `T_i=0`, then `Lambda=0` almost surely, hence every `T_i=0` by
positivity of the gates and nondegeneracy of the lower-mark Gram.
Otherwise every `T_i` and every `rho_i` is nonzero. The sign-rigidity
argument in the assigned functional report applies without a bounded
displacement premise: the nonzero linear forms
`b_1 dot (T_i/lambda_i)` have pairwise nonnegative products almost surely.
Positive density on a neighborhood of zero forces them to be positively
proportional. Hence

\[
T_i=\lambda_i\kappa_i q,\qquad \kappa_i>0,
\qquad q\ne0.
\tag{10}
\]

Within an effective-vector group the derivative coefficient `d_i` is
common, since the upper gate is even, including the zero group. Thus
`T_i/rho_i=M^Td_J` is common within each group. Equations (3), (10)
imply that `lambda_i y_i` has one constant sign on that group. Each of
the two global sign classes has only two indices, so every effective
group has at most two members.

A nonzero singleton group cannot carry a nonzero residual by (2).
A nonzero two-member group must have prediction zero by equal weights
and (2). The zero group also predicts zero. Every prediction is therefore
zero, and `L=sum_i p_i y_i^2=1`, contradicting the hypothesis. This proves
all `T_i=0`.

**Curvature proof.** Put `V=[y_1u_1 ... y_4u_4]` and
`beta_i=lambda_i y_i`. Its kernel is exactly `span{beta}`. Since `beta`
has both signs, choose strictly positive numbers `p_i` with
`sum_i beta_i p_i=0`; for example use one positive common value on the
positive sign class and another on the negative class, adjusted to
balance their sums. The range of `V^T` equals `beta^perp`, so there is
`a` with `V^Ta=p`. Thus (4) holds. Section 3 gives the negative bounded
direction at every positive-loss endpoint below one.

**Verification of the functional and basin implications.** The moment
map `w -> a_i` is locally `C^(1,1)` from lower `L2` to a finite vector
space, by bounded second activation derivatives and Cauchy--Schwarz.
All `rho_i,d_i,T_i` and the upper/matrix gradient blocks are locally
`C^(1,1)`. The lower-gradient factors
`G_i(w)t=phi'(w dot u_i)(b_1 dot t)u_i` are uniformly bounded and
Lipschitz from lower `L2` into operators with finite-dimensional domain.
At `T_i(theta_*)=0`, subtracting the linear term leaves products of
two `O(r)` factors and `C^(1,1)` Taylor remainders. Their Lipschitz
constant on a radius-`r` ball is `O(r)`.

The derivative multiplier with `phi''` is zero. All remaining derivative
terms factor through finitely many moments, giving rank at most
`(3d+1)4+2d^2`; their ranges consist of bounded odd fields and matrix
coordinates. Symmetry first holds on bounded directions and extends by
density, so the flow derivative `A` is self-adjoint. The negative loss
direction gives a positive eigenvalue of `A`. At loss below one, some
upper feature `H_j` is nonzero, and the pure-readout direction `H_j`
has strictly positive loss second derivative, giving a negative
eigenvalue of `A`.

The exact hypotheses for the trapping construction in Sections 4--5 of
`dependent_basin_functional.md` are now verified: finite nonzero unstable
space, self-adjoint split, bounded eigenvectors, and a vanishing local
Lipschitz remainder. For clarity, its contraction uses growth norm
`sup_{t>=0} exp(-lambda t/2)(||x_cs(t)||+||x_u(t)||)` and the two integral
operators have total Lipschitz constant `4 epsilon/lambda`. Retraction
to a small ball makes this less than one half. Its graph contains every
orbit trapped in that ball, irrespective of which equilibrium it
approaches.

The exact flow, locally Lipschitz time maps, invertible strongly continuous
directional time-map derivatives, and their scalar-Lipschitz-hypersurface
pullback property were proved for every finite input family in the same
source and require no further data assumption. Separability supplies a
countable cover of all endpoint neighborhoods; an integer-time pullback
then covers every point-convergent bad orbit. Conditioning on one
Gaussian-series coordinate transverse to each scalar graph proves
translation/scaling nullity. These are the full earlier point-basin
conclusions in the same `H_d` topology, with no endpoint norm condition.

**Nonempty open family.** Take four points on a common positive latitude,
at transverse angles `0,pi/2,pi,3pi/2`, and give all four label `+1`.
Their relation is `(1,-1,1,-1)` and every triple is independent.
Small independent perturbations on the sphere preserve the triple
determinants and the signs of the circuit coefficients. Thus the family
includes an open set of four-input configurations in dimension three;
it is not a single symmetric example. The theorem also holds in any
larger ambient dimension when the four inputs have the stated rank-three
geometry. It does not assert a sample count larger than four.

## 5. Four-input failure of no-moment-matching regularity

Work in dimension three and choose `0<C<1/2`, `S=sqrt(1-C^2)`. Put

\[
u_1=(C,S,0),\quad u_2=(C,-S,0),\quad
u_3=(1,0,0),\quad u_4=(0,0,1),
\]
\[
y=(+1,+1,-1,+1),\qquad p_i=1/4.
\tag{11}
\]

All inputs are unit, distinct, and nonantipodal. There is a positive
solution `t` to

\[
2C\operatorname{sech}^2(Ct)=\operatorname{sech}^2t.
\tag{12}
\]

Indeed the left side minus the right side is negative at zero, while
the ratio of the left side to the right side tends to infinity as
`t -> infinity`, because `C<1`. Continuity gives a positive root.
For

\[
P(s)=\tanh(s\cdot u_1)+\tanh(s\cdot u_2)-\tanh(s\cdot u_3),
\quad s\in\operatorname{span}(e_1,e_2),
\]

equation (12) says `grad P(t e_1)=0`. At that point its Hessian is
diagonal. With `g=sech^2(Ct)>0`, its entries are

\[
P_{11}=4Cg[\tanh t-C\tanh(Ct)]>0,
\qquad P_{22}=-4S^2g\tanh(Ct)<0.
\tag{13}
\]

It is therefore nonsingular. The finite-dimensional implicit-function
theorem applies to the two gradient equations: their derivative in `s`
is the invertible matrix (13), and their dependence on `s` and the
three input angles is analytic. A neighborhood of arbitrary planar
angle perturbations retains a nonzero critical vector `s_*`.
In particular, one can choose an asymmetric triple that avoids every
reflection-angle equality of the earlier three-input report.

Use canonical independent Gaussian coordinate pairs `(G_j,Z_j)`.
Let `q` select the normalized lower `h_3=tanh G_3` coordinate, and put

\[
B=q\cdot b_1,\qquad \delta=\operatorname{sign}G_3,
\qquad \epsilon=\operatorname{sign}G_1
                 \operatorname{sign}G_2\operatorname{sign}G_3.
\tag{14}
\]

Both signs are odd under simultaneous mark negation. Independence of
the three coordinate pairs gives exactly

\[
E_1[b_1\epsilon]=0,
\qquad \kappa=E_1[B\delta]=E_1|B|>0.
\tag{15}
\]

For each coordinate of `b_1`, at least two independent centered sign
factors remain in the first expectation. This verifies (15) even for
the reverse-response features correlated with their own `G_j`.

Fix `a>0`, let `e` be the first upper coordinate vector, and set

\[
w=\epsilon s_*+a\delta e_3,
\qquad M=e q^T,
\qquad z=\kappa\tanh a>0.
\tag{16}
\]

The lower field is bounded and odd, hence `w-g` is a valid `L2`
displacement; no essential bound on that displacement is asserted.
For the first three inputs, `a_i=tanh(s_* dot u_i)E[b_1 epsilon]=0`.
For the fourth input, `M a_4=ze`. Thus

\[
z_1=z_2=z_3=0,
\qquad H_1=H_2=H_3=0,
\qquad H_4=\tanh(zx),\quad x=b_2\cdot e.
\tag{17}
\]

Choose a bounded odd readout `c=c(x)` satisfying

\[
E_2[c\tanh(zx)]=1,
\qquad E_2[cx]=D\ne0.
\tag{18}
\]

The bounded odd functions `tanh(zx)` and `x` are linearly independent
on the actual bounded upper support. An almost-sure relation extends
analytically from an interval to the real line; linear growth first
forces the coefficient of `x` to vanish, then the other coefficient
vanishes. Their positive-definite Gram solves (18) for every prescribed
`D`. Canonical upper coordinate independence gives
`d_1=d_2=d_3=De`.

The predictions are `(0,0,0,1)`, so
`rho_i=-y_i/4` for `i<=3` and `rho_4=0`. The readout gradient vanishes
by (17). The matrix gradient vanishes because every residual-bearing
input has `a_i=0`. The lower gradient is a scalar multiple of

\[
\sum_{i=1}^3 y_i\operatorname{sech}^2(s_*\cdot u_i)u_i
 =\nabla P(s_*)=0.
\tag{19}
\]

All three blocks are therefore stationary, and

\[
L=3/4,\qquad T_i=-\tfrac14 y_iDq\ne0\quad(i=1,2,3).
\tag{20}
\]

The four rank-one matrices `u_i u_i^T` in (11) are linearly independent.
If their linear combination is zero, the `(3,3)` entry forces the
fourth coefficient to vanish; the `(1,2)` entry forces the first two
coefficients to agree; the `(2,2)` entry forces them both to vanish;
and the `(1,1)` entry forces the third coefficient to vanish. This
independence persists under small perturbations. Thus even absence of
*every* nontrivial signed second-moment relation does not rule out (20).
In particular, no matching of two disjoint weighted second-moment
averages is possible, with or without a first-moment matching condition.

The construction uses a dependent three-input subset and an additional
independent fitted input. It is not a counterexample under the stronger
condition that every triple of four three-dimensional inputs is
independent. Its mechanism is precisely that a collapsed zero-feature
circuit can carry loss equal to its own mass while another input is fitted.
The global loss threshold one does not exclude this mechanism.

## 6. Actual failure of the second Frechet differential in the example

This verifies that the preceding example defeats the actual regularity
premise, not merely one sufficient cancellation argument. Write `s_*`
for the critical plane vector and `H_P=D^2P(s_*)`, which remains
nonsingular after sufficiently small perturbations. Since `P` is bounded
on its plane and `H_P` is nonsingular, there is a finite plane vector `h`
such that

\[
R=P(s_*+h)-P(s_*)-\tfrac12 h^TH_Ph\ne0.
\tag{21}
\]

Otherwise `P(s_*+h)` would be a nonconstant quadratic polynomial of `h`
for every `h`, contradicting boundedness. The linear Taylor term is zero
by criticality.

Choose `b>0` with `P_1(B>=b,epsilon=1)>0`. Such a choice exists: on
`G_3>0`, the two independent signs `sign G_1,sign G_2` have product
`+1` with probability one half. Nonatomicity supplies subsets `E_n`
of this event with masses `m_n -> 0`, `m_n>0`. Perturb `w` by `h` on
`E_n`, by `-h` on their sign images `-E_n`, and by zero elsewhere;
call the bounded odd increment `h_n`. Then

\[
\|h_n\|_2^2=2m_n|h|^2\to0.
\tag{22}
\]

The fourth lower activation is unchanged. Every first-three effective
vector increment is `O(m_n)`. At fixed `c,M`, the upper loss is a smooth
finite-dimensional function of those effective vectors. Its first Taylor
term, including the unhalved square-loss factor and the two sign-paired
sets, is

\[
L(w+h_n,c,M)-L(w,c,M)
 =-D\left(\int_{E_n}B\,dP_1\right)
       [P(s_*+h)-P(s_*)]+O(m_n^2).
\tag{23}
\]

Every fixed-direction second derivative exists by bounded activation
derivatives and domination by an integrable multiple of `|h_n|^2`.
Its residual-contracted direct lower second derivative is

\[
-D\left(\int_{E_n}B\,dP_1\right)h^TH_Ph,
\tag{24}
\]

and its other terms are `O(m_n^2)`, being products of first finite-moment
increments. If a second Frechet differential existed, its quadratic form
would equal this ordinary second directional derivative. Subtracting half
of (24) from (23), and dividing by (22), leaves a quantity bounded away
from zero in absolute value because `R!=0`, `D!=0`, and
`int_{E_n} B >=b m_n`. This violates the required quadratic Taylor
remainder. The loss therefore has no second Frechet differential at this
physical-Hilbert equilibrium.

## 7. Claim ledger and limitations

| Claim | Status | Exact scope |
|---|---|---|
| Labeled strict separation gives negative bounded directional curvature | Proved | Every finite input count, positive weights, positive-loss equilibrium below one |
| Equal weights plus a rank-three four-input circuit with labeled signs 2+2 gives the entire full-H point-basin theorem | Proved internally | Section 4, all endpoint fields merely L2 |
| No second-moment matching forces individual cancellation | Falsified | Four-input example with independent `u_i u_i^T`, loss 3/4 |
| That no-moment condition guarantees a Hilbert Hessian | Falsified | Concentrated perturbation proof in Section 6 |
| No-moment condition implies basin nullity by another argument | Open | No positive-probability basin or generalized trapping theorem supplied |
| Arbitrary-finite-count generic data restore the entire theorem | Open in this route | Cancellation or a replacement full-H graph mechanism still needed |

The main theorem does not assume state convergence, assert convergence
from canonical initialization, or exclude positive-loss escape or
nonconvergent motion. The specified Gaussian series is an initial-state
randomization with bounded increments almost surely and full support in
the physical Hilbert topology; it is distinct from the fixed Gaussian
population marks. Translation/scaling nullity gives no conclusion for a
single deterministic canonical state. No numerical experiment was run.

## 8. Post-freeze comparison: the exact gate-rank criterion also fails broadly

Sections 1--7 were written before receiving comparison findings; their
SHA256 is
`339e09428c91e11645de8f352c7a3e0c582113d1d851f8205fb34dbcd55a698b`.
The hash was computed after the first comparison messages arrived, with
no intervening edit. The supervisor then reported agreement of the two
independent four-input proofs and supplied the scalar `arcosh` construction
below for verification. This section is explicitly post-comparison; no
sibling report was read.

The criterion under discussion quantifies over every signed effective
partition whose formal readout-stationary loss lies in `(0,1)`, and requires
the active group vectors

\[
R_J(s)=\sum_{i\in J}\rho_i\operatorname{sech}^2(s\cdot u_i)u_i
\tag{25}
\]

to be linearly independent for every finite `s`. A zero group is permitted;
its predictions are zero. This is a sufficient data-only cancellation
criterion: at an actual endpoint lower stationarity is
`sum_J (b_1 dot M^Td_J) R_J(w)=0`, so group independence cancels every
active coefficient. The same condition gives a nonzero group vector for
the mixed-variation proof. Its sufficiency does not imply that it admits
the desired large dependent families.

**Exact obstruction.** For equal weights, every dependent input family
with at least five pairwise nonparallel inputs violates this criterion.
This includes exact `sech^2` gates; the obstruction does not replace the
gates by independently adjustable positive numbers.

Choose a minimal dependent subset `C` and a full-support relation
`sum_{i in C} alpha_i u_i=0`. Its column rank is `|C|-1`, and `|C|>=3`.
Let `tau_i=sign(alpha_i y_i)`. Partition `C` into two nonempty groups
`J_1,J_2`, each having constant `tau_i`. If both signs occur, use their
two sign classes. If only one sign occurs, split that class into two
groups. Choose the split so at least one group has size at least two;
if `C` is the whole data set, choose it so one group has size at least
three. The latter choice is always possible when `|C|>=5`.

If one group is a singleton, designate it as the zero group. Both groups
cannot be singletons. For each other group choose the effective
orientation signs `sigma_i` so the oriented labels `sigma_i y_i` are
mixed; this makes every residual in the group nonzero. If one group has
size at least three and `C` is the whole data set, choose an imbalanced
mix, so its mean prediction is nonzero. All indices outside `C` are
fitted singleton groups.

This formal partition has strictly positive loss. If `C` is proper, its
loss is at most `|C|/m<1`. If `C` is the whole data set, the imbalanced
group yields positive improvement over prediction zero, so its loss is
also below one. The residuals on `C` have signs `sign rho_i=-y_i`.

For `J=J_1,J_2` choose a parameter

\[
A_J\ge A_{J,\min}:=\max_{i\in J}\frac{|\alpha_i|}{|\rho_i|},
\qquad
t_i(A_J)=\operatorname{arcosh}
       \sqrt{\frac{A_J|\rho_i|}{|\alpha_i|}}.
\tag{26}
\]

The function

\[
F_J(A)=\sum_{i\in J}|\alpha_i|t_i(A)
\]

is continuous on its closed allowed half-line, strictly increasing above
its endpoint, and unbounded. Continuity follows from continuity of
`arcosh` on `[1,infinity)`; strict increase follows because every term
increases; divergence follows because every argument grows without bound.
Choose a common positive value above both endpoint values. The
intermediate-value property gives finite `A_1,A_2` with
`F_{J_1}(A_1)=F_{J_2}(A_2)`.

Set projection values on `C` by

\[
z_i=\operatorname{sign}(\alpha_i)t_i(A_1)\ (i\in J_1),
\qquad
z_i=-\operatorname{sign}(\alpha_i)t_i(A_2)\ (i\in J_2).
\tag{27}
\]

Then `sum_C alpha_i z_i=0`. Since the range of `U_C^T` is exactly the
orthogonal complement of its one-dimensional kernel, there is a finite
physical input-space vector `s` with `s dot u_i=z_i` on `C`. Therefore
the actual gates satisfy

\[
\operatorname{sech}^2(s\cdot u_i)
 =\frac{|\alpha_i|}{A_J|\rho_i|}\quad(i\in J).
\]

Let `tau_J` be the common oriented circuit sign on `J`. Substitution into
(25) gives

\[
R_J(s)=-\frac{\tau_J}{A_J}\sum_{i\in J}\alpha_i u_i,
\qquad
\sum_{J=J_1,J_2}\tau_J A_J R_J(s)=0.
\tag{28}
\]

Both coefficients in (28) are nonzero. Each group is a nonempty proper
subset of the circuit, so its displayed input sum is nonzero by minimal
dependence. Thus (28) is a genuine dependence of two nonzero exact gate
vectors. The formal partition meets the criterion's loss restriction,
proving its failure.

This failure is stronger than failure of an arbitrary-positive-gate
relaxation, but remains a failure of a sufficient data certificate.
The construction does not realize the prescribed signed partition as
an actual population equilibrium, and it does not produce a basin.

## 9. Post-freeze circuit loss thresholds

The supervisor also supplied a proposed circuit-dependent loss threshold.
The following checks its minimum and formal partition attainability; it
does not assert that a singular equilibrium attains the threshold.

Suppose the entire equal-weight data set of size `n` is one circuit of
rank `n-1`, with every proper subset independent. Write its relation as
`alpha`, and put `beta_i=alpha_i y_i`. Define

\[
m(1)=1,\qquad m(k)=\frac{4(k-1)}{k}\quad(k\ge2).
\tag{29}
\]

If both signs of `beta` occur with cardinalities `a,b`, define
`ell_*=[m(a)+m(b)]/n`. If only one sign occurs, define
`ell_*=m(n)/n`.

At any equilibrium with some `T_i!=0`, the same full-circuit sign argument
as in Section 4 forces all residuals to be nonzero and every effective
group to lie within one sign class of `beta`. A nonzero group of size `r`
with `j` positive and `r-j` negative oriented labels has unnormalized
loss `4j(r-j)/r`, whose minimum over `1<=j<=r-1` is `m(r)`.
A zero group of size `r` has unnormalized loss `r`, which is at least
`m(r)` for `r>=2`, since `r-m(r)=(r-2)^2/r`. A singleton group can only
be the zero group, with cost one.

Splitting one sign class never lowers the bound (29). For nonzero groups
of sizes `r,s>=2`,

\[
m(r)+m(s)-m(r+s)
 =4-4/r-4/s+4/(r+s)>0.
\]

For addition of zero-group members one at a time, when `r>=2`,

\[
m(r+1)-m(r)=\frac4{r(r+1)}<1.
\]

If there is only a zero group in a sign class, its cost is its size,
already at least (29). Merging the nonzero groups and then adding the
zero members proves total cost at least `m(k)` for a class of size `k`.
Consequently every endpoint with some nonzero `T_i` has `L>=ell_*`.

At the formal partition level this lower bound is attained: use one
maximally imbalanced nonzero group per sign class of size at least two,
and designate a singleton sign class as the zero group. There cannot be
two singleton sign classes for a circuit of pairwise nonparallel inputs.
For a single sign class, use one maximally imbalanced group on all data.
These are legitimate formal readout partitions with all residuals nonzero.

Therefore all `T_i` vanish below `ell_*`. If both signs occur, the
positive-vector row-space argument in Section 4 proves labeled strict
separation, and Section 3 supplies negative curvature. If only one sign
occurs, a sole residual-bearing group containing all `n` inputs would
already have loss at least `m(n)/n`: a nonzero group obeys the preceding
binary average bound, and the all-zero group has loss one. Below the
threshold, some residual-bearing group is thus a proper subset of the
circuit. Its inputs are independent, so its `R_J(w)` cannot vanish,
and the same mixed-variation argument supplies curvature.

All full-Hilbert functional and probability implications of Section 4
therefore hold for point-convergent positive-loss endpoints below this
explicit data threshold. This is a loss-sublevel theorem, not restoration
of the whole `0<L<1` claim. It recovers the four-input two-plus-two theorem
because `m(2)+m(2)=4`. For example, the five-input split `2+3` gives
`ell_*=14/15`; the four-input split `3+1` gives `ell_*=11/12`.

## 10. Post-comparison check of the lead synthesis and universal sublevels

At the supervisor's request, the complete new lead synthesis
`INPUT_CONDITION_RESULTS.md` was read and checked. Its checked SHA256 is
`bc0067f98d0287b127e9480db7d13b1e30e44ed4365859854c422df5ef507468`.
This is an informed post-comparison check, not a fresh isolated review.
No exact error was found in that version. The check particularly verifies
the new universal theorem in its Section 5, as follows.

Let `q` be the number of residual-bearing indices at an equal-weight
equilibrium. A nonzero effective group either fits entirely or has all
its residuals nonzero, so the active groups do partition exactly these
`q` indices. For `q>=2`, merge the nonzero active groups by the strict
subadditivity calculation in Section 9 and add each zero-group member at
cost one. The increment of `m` is less than one once its argument is at
least two. If there are no nonzero groups, the unnormalized cost is
`q>=m(q)` directly. Thus

\[
L\ge\frac{m(q)}n=\frac{4(q-1)}{nq}\qquad(q\ge2).
\tag{30}
\]

The case `q=1` need not satisfy that group-merging argument and is
correctly handled separately in the synthesis. Since `m` is increasing
on the integers starting at two, the strict loss bound
`L<4r/[n(r+1)]`, `2<=r<n`, forces `q<=r`. If every subset of at most
`r` inputs is independent, the active lower stationarity equation forces
all active coefficients `T_i` to vanish; inactive ones vanish by definition.
Each residual-bearing group is an independent nonempty input subset,
so its field `R_J(w)` is nonzero at every finite `w`. These are the two
separate hypotheses of the full physical-Hilbert graph argument, and both
are genuinely proved. Thus the universal threshold `8/(3n)` for pairwise
nonparallel data is valid, without labeled separability or any endpoint
boundedness assumption.

The supervisor additionally proposed a stronger threshold under strict
labeled separation. That refinement also holds. Suppose every subset
of at most `r` inputs is independent and (4) holds. If some `T_i` is
nonzero, then `q>=r+1`; otherwise input independence cancels all `T_i`.
There must also be at least two active groups: a single active group has
`R_J(w)!=0` everywhere by (5), and its lower stationarity equation forces
`b_1 dot M^Td_J=0` almost surely, again cancelling every `T_i`.

For `q>=3` active indices distributed among at least two active groups,
their unnormalized cost is at least

\[
1+m(q-1).
\tag{31}
\]

If a zero group exists, merge all nonzero groups and write its size as
`q-z>=2`, with `z>=1` zero members. The resulting lower bound
`z+m(q-z)` increases with `z`, since removing one member from a
nonzero group of size at least three saves less than one. Its minimum
is at `z=1`, giving (31).

If there is no zero group, merge to two nonzero groups of sizes
`a,q-a>=2`. Their cost is at least `m(a)+m(q-a)`. The reciprocal sum
`1/a+1/(q-a)` is maximized at the extreme allowed values `a=2,q-2`:
it equals `q/[a(q-a)]`, and the denominator is minimized at those
endpoints. Hence the cost is at least `m(2)+m(q-2)`. For `q>=4`,

\[
m(2)+m(q-2)-[1+m(q-1)]
=1-\frac4{(q-2)(q-1)}>0.
\]

This proves (31) in all cases. With `q>=r+1`, a nonzero coefficient
therefore requires `L>=(1+m(r))/n`. Consequently the entire full-Hilbert
point-basin conclusion holds under strict labeled separation below

\[
\ell_r^{\rm sep}=\frac{1+m(r)}n=\frac{5-4/r}{n}.
\tag{32}
\]

Cancellation follows from (31), and negative curvature follows from
strict separation via Section 3. This is again a loss-sublevel theorem,
not a whole-`(0,1)` result for arbitrary sample count. Its smallest-rank
case is `3/n` for `r=2`.

Final synthesis update checked: the supervisor identified only two changes
after the first checked version, namely the added proof of (14a) at the
end of Section 5 and the strict-direction/separate-regularity paragraph
at the beginning of Section 7. Both additions were read in full and
checked without finding an error. The optional bound agrees with
(31)--(32). Strict labeled separation indeed excludes equal class centers:
their projections on the separating vector would have opposite strict
signs. The final covered synthesis SHA256 is
`fa6670f4c8bbcd658d295e66db4517ebfdd42f7fabebdfaa86e5e7296b7a445b`.
This informed check is now complete; the owned report is frozen after
this note.
