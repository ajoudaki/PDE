# Noisy scalar histories and exact weighted-packet acquisition

2026-10-06. Scoped continuation in the unseen-query decoder study.
Internal finite-program results; no experiments or promotion.

The exact noisy Gaussian row program can be perturbed by adding a much
smaller Gaussian noise to each scalar empirical-moment update. Its
retained state then consists of a current scalar-history prefix. A
source-dependent positive weighted panel of at most \(P+1\) iid-root
packets reproduces all \(P\) scalar updates exactly by causal induction.
The panel stores no training vector history and no table of future
scalar values. Quantized packet marks and weights give a controlled
approximation with an absolute-polylogarithmic bit budget whenever the
finite instruction and sensitivity bounds are polylogarithmic.

The scalar-noise modification is **not** silently identified with the
exact noisy-matrix law. It is a separately coupled perturbation of the
exact row program, with the quantitative error in Section 3.

## Scope and provenance

The supervisor explicitly assigned scalar-noise perturbation, weighted
packet acquisition, and their quantitative counts. The source and
process scope is unchanged from `NOISY_TWO_ORIENTATION_TRANSCRIPT.md`,
whose formulas are used below. That file and the other preceding notes
are not modified. The unavailable custom notation skill is replaced
only by the already supplied conventions and read maintained notation
contract, not by an uninspected skill summary.

The posterior-density evaluator, stability of that evaluator under
quantized histories, and the posterior-prefix robust-center argument
are separately assigned to other agents. They are not assumed proved
by this note. The supervisor is separately deriving the original
physical-flow comparison to a finite noisy matrix-call program.

## 1. A bounded finite scalar/row program

Let \(Z_1,\ldots,Z_n\in\mathbb R^D\) be iid packets. In the noisy
Gaussian representation, \(D=D_0+R\), where \(D_0\) counts the
initial Gaussian row coordinates and \(R\) is the number of matrix
calls. Fix a chronological list of \(P\) scalar moment updates

\[
 C_r=\frac1n\sum_{i=1}^n F_r(Z_i;C_{<r})+\eta E_r,
 \qquad 1\le r\le P,                                        \tag{1}
\]

where \(C_{<r}=(C_1,\ldots,C_{r-1})\),
\(E_1,\ldots,E_P\) are independent standard Gaussian variables
independent of the packets, and \(0<\eta\le1\). The row functions

\[
 F_r:\mathbb R^D\times\mathbb R^{r-1}\to\mathbb R
\]

are deterministic finite instruction graphs. They may ignore packet
coordinates not yet used by their chronology. Roots and intermediate
nodes may be clipped by prescribed globally Lipschitz maps. Scalar
coefficient routines are extended off genuine moment arrays by the
positive-semidefinite projection and ridge construction in
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`.

Assume explicit bounds

\[
 |F_r(z;c)|\le B_F,
\quad
 |F_r(z;c)-F_r(z';c')|
 \le L_Z\|z-z'\|_\infty+L_C\|c-c'\|_\infty,                 \tag{2}
\]

with \(L_Z,L_C\ge1\), for all arguments after their prescribed
caps. Internal coefficient evaluation can clip the scalar history to
a deterministic box. The observed \(C_r\) itself is **not** clipped:
the independent Gaussian term in (1) remains an ordinary Gaussian
update, without atoms introduced by a final hard clipping operation.

Several moments needed at one matrix call can be ordered successively
while making their \(F_r\) ignore earlier updates in the same block.
This represents a simultaneous block without changing its intended
dependence. Coefficients obtained by deterministic scalar arithmetic
from \(C\) do not require additional independent noise coordinates
unless one intentionally introduces them.

## 2. Counts and bounds supplied by noisy Gaussian conditioning

Let the underlying observable finite program have \(R\) initialized
matrix calls, \(S_0\) coordinatewise/scalar arithmetic nodes apart
from its conditioning representation, and \(P_0\) original scalar
empirical reductions. Empty or fixed-dimensional input layers add
only their actual fixed counts.

At the \(j\)-th call, the exact conditioning formulas require at
most \(Cj\) new scalar pair moments: old query Grams and cross-Grams
can be retained, the new argument is paired with the relevant old
queries and answers, and the fresh Gaussian innovation is paired with
the old opposite-orientation query fields. Updating the Gram tables
after the answer again needs at most \(Cj\) pairs. Therefore

\[
 P\le P_0+C R^2.                                             \tag{3}
\]

There are \(O(R)\) new named argument/answer/innovation fields, and
each rowwise conditional action is a sum of at most \(CR\) old
fields with shared scalar coefficients plus a fresh Gaussian term.
The extra coordinatewise graph has \(O(R^2)\) scalar operations.
Consequently its row-graph size obeys

\[
 N\le C(S_0+P_0+R^2+1),                                     \tag{4}
\]

when a small-matrix inverse, square root, or Sylvester solve is
temporarily counted as one specified finite-dimensional coefficient
routine. Their largest dimension is \(R^2\), and their actual
arithmetic implementation and workspace must also be counted.

For one call, write \(\delta=\sigma^2\), with \(\sigma\) the
matrix-answer noise. The previous note gives the following exact
coefficient computation:

\[
 C=(\delta I+Q)^{-1},\quad D=(\delta I+K)^{-1},
 \quad (\delta I+K)E+EQ=-HC-DJ,                               \tag{5}
\]

followed by a Kronecker resolvent of dimension at most \(R^2\), a
positive square root with gap \(\delta\), and an inverse with
gap \(2\sigma\). No inverse empirical Gram occurs.

If all moment-generating fields have RMS at most \(B\), the
fresh innovation has RMS at most \(G\), and the moment caps are of
the corresponding polynomial size, every one-call coefficient and
its Lipschitz constant in the input moment entries is bounded by

\[
 [C(2+R+B+G+\sigma^{-1})]^{C_0},                             \tag{6}
\]

where \(C_0\) is an absolute integer. The proof consists of the
resolvent identity, the Sylvester inverse bound, and the square-root
bound displayed in that note. It is independent of a history Gram
condition number. A coarse fixed exponent can be chosen uniformly:
bounding entrywise-to-Frobenius conversions, tensor dimensions, and
the explicit products in (5) and the covariance factor by successive
powers yields, for example, \(C_0=100\), after enlarging the
absolute constant and the polynomial-sized Gram cap. No optimization
of this exponent is intended.

To make the growth bookkeeping explicit, suppose every capped row
node has amplitude at most \(H\ge1\), every prescribed scalar
primitive outside the conditioning routines has Lipschitz constant
at most \(L_0\ge1\), and every coefficient cap has logarithmic
size bounded by the logarithm of (6) times a polynomial in \(N\).
Products, sums, and scalar compositions then give

\[
 \log(B_F+L_Z+L_C+2)
 \le C N^{c_0}
    \left[1+\log(H+L_0+R+B+G+2)+\log(1/\sigma)\right]          \tag{7}
\]

for an absolute integer \(c_0\). For a graph of ordinary binary
operations and the macros (5), taking \(c_0=2\) is already a
coarse bound: each of at most \(N\) nodes multiplies previous
Lipschitz bounds by a polynomial-sized node/coefficent bound, and
the logarithm of each coefficient cap grows at most linearly in
the instruction count. A larger fixed exponent safely covers a
chosen arithmetic implementation of the macros.

The useful point is the dependence on \(\log(1/\sigma)\), not
\(1/\sigma\), in the logarithmic total sensitivity. Thus if
\(N,R\), \(\log H\), \(\log L_0\), and
\(\log(1/\sigma)\) are polylogarithmic, so are
\(\log B_F,\log L_Z,\log L_C\). No unspecified
history-conditioning constant is hidden in (7). Application to an
actual physical approximation must still supply its own \(S_0,P_0,H,L_0\).

## 3. Coupling scalar-noisy and exact-moment row programs

Use the same iid packets in the unperturbed recursion

\[
 C_r^0=\frac1n\sum_i F_r(Z_i;C_{<r}^0).                       \tag{8}
\]

This is the exact noisy-matrix row program after the prescribed
extensions and caps; agreement with the uncapped exact program is
asserted only on the separately verified cap event.

On the event \(\max_r|E_r|\le T_E\), define
\(e_r=\max_{a\le r}|C_a-C_a^0|\). Equations (1), (2), and
(8) give

\[
 e_r\le(1+L_C)e_{r-1}+\eta T_E,
 \qquad
 e_P\le\eta T_E P(1+L_C)^P.                                \tag{9}
\]

The first inequality bounds both the old prefix error and the new
coordinate error; iterating the geometric sum proves the second.
The Gaussian tail bound gives

\[
 \mathbb P\{\max_r|E_r|>T_E\}\le2P e^{-T_E^2/2}.              \tag{10}
\]

If a final scalar or row output is \(L_{\rm out}\)-Lipschitz in
the history, its additional perturbation is at most

\[
 L_{\rm out}\eta T_E P(1+L_C)^P.                            \tag{11}
\]

The logarithm of the factor multiplying \(\eta\) is at most

\[
 \log L_{\rm out}+\log(T_E P)+P\log(1+L_C),                  \tag{12}
\]

which is a polynomial in the finite instruction counts and the
logarithmic bounds in (7). In particular, there exists an absolute
power \(a\), determined by the explicit program-count exponents,
such that a choice \(\eta=\exp[-\log(n)^a]\) makes (11)
smaller than any prescribed inverse polynomial when the other
parameters are absolute-polylogarithmic. More generally, for a
specified target \(\varepsilon_{\rm sc}\), the fully explicit
sufficient choice is

\[
 \eta\le
 \frac{\varepsilon_{\rm sc}}
      {L_{\rm out}T_E P(1+L_C)^P}.                           \tag{13}
\]

This derivation is why the scalar-noisy program may be used as a
negligibly perturbed proxy. Exact noisy-matrix posterior coefficients
depend on true empirical Grams. Feeding the perturbed histories (1)
into those coefficient routines changes their output and hence
changes the law. The change is controlled by (9)--(13), not denied.

Combined with a separately proved deterministic perturbation bound
for adding matrix-answer noise to the physical finite program, one
can allocate two distinct budgets: \(\sigma\) controls that oracle
perturbation, and the much smaller \(\eta\) controls the scalar
moment perturbation after Gaussian elimination. This note does not
replace the former physical-program estimate with (9).

## 4. Exact acquisition from at most \(P+1\) packets

Fix a realization of all \(Z_i\) and all \(E_r\), and run (1)
during preprocessing. For each original row form

\[
 a_i=\big(F_1(Z_i),F_2(Z_i;C_1),\ldots,
                   F_P(Z_i;C_{<P})\big)\in\mathbb R^P.        \tag{14}
\]

There are indices \(i_1,\ldots,i_q\) and positive weights
\(p_1,\ldots,p_q\), with

\[
 q\le P+1,\qquad \sum_{j=1}^qp_j=1,
 \qquad \sum_{j=1}^qp_j a_{i_j}=\frac1n\sum_{i=1}^n a_i.       \tag{15}
\]

An elementary proof starts with the uniform weights. If their positive
support exceeds \(P+1\), the corresponding vectors \((1,a_i)\)
are linearly dependent. Subtract a multiple of this dependence from
the weights until one positive weight reaches zero, preserving all
moments and nonnegativity. Iterate finitely. This proves (15).

Store only the selected packets \(z_j=Z_{i_j}\), their weights,
the \(P\) scalar-noise marks \(E_r\), and the fixed program
instructions. The compact online update is

\[
 C_r^c=\sum_{j=1}^q p_jF_r(z_j;C_{<r}^c)+\eta E_r.            \tag{16}
\]

**Exact acquisition theorem.** For every \(1\le r\le P\),
\(C_r^c=C_r\).

**Proof.** Assume equality for the prefix. Each row function in the
next update is therefore evaluated at exactly the realized prefix
used in (14). The \(r\)-th equality in (15) identifies its weighted
average with the original empirical average. The same scalar-noise
mark is added, proving equality for the next coordinate. The empty
prefix starts the induction. \(\square\)

This is stronger than matching selected scalar outputs afterward:
every intermediate retained-history prefix is produced by its own
causal moment update. The panel stores no future \(C_r\) values
and no vector trajectory. It does store its selected finite root
packets, including independent innovation coordinates that the finite
program will use later. These are fixed root marks, not future
training outputs. The selected packets and weights need not be iid
after selection, and no such assertion is used.

The selection can depend on the completed finite training program.
This is source-dependent preprocessing, as in the preceding weighted
finite-program theorem. If initialization were required to avoid
examining that source computation, (15) would not prove such a
stronger requirement. Subsequent execution of (16) needs no access
to the original \(n\) packets or dense matrices.

## 5. Memory and current-history query use

The retained panel uses \(qD\) scalar packet entries, \(q\) weights,
and \(P\) scalar-noise marks. The currently acquired history contains
at most \(P\) scalars. Thus its real-scalar count, excluding the fixed
program description, is

\[
 O(PD+P),\qquad D=D_0+R.                                    \tag{17}
\]

At each update, evaluate \(F_r\) on one selected packet at a time
and accumulate one weighted sum. Previous row nodes may be recomputed
recursively from that packet and the stored scalar history. No array
of all training forward/backward fields is required. A depth-first
row evaluator has a finite stack bounded by the row-graph size;
small conditioning matrices have dimension at most \(R^2\), so a
straight dense representation costs \(O(R^4)\) transient scalars.
Even allowing a separate such workspace per recursive macro frame
gives the conservative bound

\[
 O(PD+P+NR^4+N)                                             \tag{18}
\]

on peak live scalar count. Recomputing instead of caching may take
very large time; no runtime efficiency is claimed.

The intended query interface exposes only the **current history**
\(C_{\le r}\), fixed program instructions, and the new query. It
does not pass the selected packet panel, selection weights, or
scalar-noise marks as conditioning data to the decoder. Their storage
is nevertheless counted in (17)--(18). The separately analyzed query
evaluator may use row functions at this fixed history without
reexecuting the training solver to recover past history values.

This separation matters probabilistically: the observable history
law is that of (1), while the selected private panel was constructed
using additional source information. Conditioning on that panel
instead would generally change the posterior law being decoded.

## 6. Finite precision without hidden real-number encoding

Unlike raw weighted-space neural coordinates, the update (16) never
divides by a selection weight. Thus arbitrarily tiny positive weights
do not force arbitrarily many precision bits.

Suppose \(\|z_j\|_\infty\le T_Z\) and \(|E_r|\le T_E\).
Choose approximate packet and noise marks obeying

\[
 \|\widehat z_j-z_j\|_\infty\le\epsilon,
 \qquad |\widehat E_r-E_r|\le\epsilon.                        \tag{19}
\]

There are nonnegative quantized weights summing to one with

\[
 \sum_j|\widehat p_j-p_j|\le2\epsilon.                       \tag{20}
\]

For example, round the first \(q-1\) weights down to multiples of
\(\epsilon/q\), and place the remaining mass in the last weight.
All weights stay nonnegative. The total downward change in the first
coordinates is at most \(\epsilon\); the compensating change of
the last coordinate has the same magnitude. This proves (20).
The final weight is determined from the other quantized weights,
so all weights have a finite common-grid representation.

Let the finite arithmetic evaluation of an update incur an additional
absolute error at most \(\epsilon\). Apply the quantized version of
(16) recursively, and let
\(e_r=\max_{a\le r}|\widehat C_a-C_a|\). By (2),

\[
 e_r\le(1+L_C)e_{r-1}
       +(L_Z+2B_F+\eta+1)\epsilon.
\]

Consequently

\[
 e_P\le P(1+L_C)^P
           (L_Z+2B_F+\eta+1)\epsilon.                       \tag{21}
\]

For a desired history error \(\varepsilon_{\rm hist}\), it is
sufficient to choose

\[
 \epsilon\le
 \frac{\varepsilon_{\rm hist}}
 {P(1+L_C)^P(L_Z+2B_F+\eta+1)}.                              \tag{22}
\]

The bit count per stored scalar is then bounded by

\[
 O\!\left(
  1+\log(T_Z+T_E+q+1)+\log(1/\varepsilon_{\rm hist})
  +\log P+P\log(1+L_C)+\log(L_Z+B_F+2)\right).               \tag{23}
\]

This includes the extra \(\log q\) bits for the weight grid.
Gaussian packet/noise caps can take
\(T_Z,T_E=O(\sqrt{\log(nD+P)+\log(1/\delta_0)})\) for the
finite set of original Gaussian coordinates, with cap failure
probability at most \(\delta_0\) by the union bound. Different
initial packet distributions require their own stated tail bounds.

Combining (7), (17)--(18), and (23) yields an absolute-polylogarithmic
total bit and peak-workspace bound whenever the underlying finite
program counts, logarithmic amplitude bounds, and target logarithmic
precisions are absolute-polylogarithmic. This is ordinary finite
quantization of a small root panel; it does not encode an \(n\)-row
array in a real number's digits.

For conditioning-matrix arithmetic, inverses have gaps controlled by
\(\sigma\), and square roots have the gaps specified in the prior
note. Those explicit gaps allow operation errors to be assigned small
enough to meet the per-update \(\epsilon\) budget, without a hidden
empirical-history eigenvalue. A complete decoder must also assign its
own posterior-evaluation tolerance and show stability under the
history perturbation (21). That is separate from the acquisition
estimate proved here.

## 7. Claim boundary

The following are proved for the specified finite program:

1. Scalar Gaussian perturbations produce a history within the explicit
   bound (9) of the exact-moment noisy Gaussian row program.
2. A positive weighted panel of at most \(P+1\) original iid packets
   acquires every noisy history prefix exactly by causal updates.
3. Finite quantization produces the explicit history error (21) with
   logarithmic precision controlled by the finite program's global
   Lipschitz bounds, not by an unproved Gram gap.

No query decoder is identified with the training updater. The target
decoder uses the currently retained history only. Its posterior law,
evaluation with counted workspace, robustness over all prefixes and
all queries, and the original physical-flow approximation are separate
proof components being developed in the coordinated task.
