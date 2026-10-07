# Cross-check of initialization and compact acquisition work

2026-10-06. Scoped author cross-check, not an independent promotion review.
The complete `QUADRATIC_INITIALIZATION.md` was read. The compiler bounds
below use the frozen `EXPLICIT_COMPILER_EXPONENT.md`; the previously read
six assigned source notes remain the scientific input scope. No experiment,
other-study access, candidate edit, or Git mutation was performed.

The streaming acquisition construction is supported. With retained-history
target precision \(C\log^{100}(en)\), the actual schedules give

\[
 W_{\rm init}\le Cn\log^{1616}(en),\qquad
 W_{\rm all\ training\ updates}\le C\log^{1632}(en).
 \tag{1}
\]

Thus the common explicit exponent \(K=1700\) is valid for initialization
work \(Cn\log^K(en)\) and all compact training work \(C\log^K(en)\).
This is an eventual \(O(n^2)\) work bound for each fixed admissible
problem. It uses the stipulated activation/data primitive model. The
exact Gaussian-law claim applies to the ideal noisy-matrix transcript;
scalar-summary noise and finite arithmetic are separately controlled
perturbations.

The reference-prediction claim is a correct implication of the candidate's
stated dense-pair certificate and decoder-to-center interface. This check
does not establish that interface for a new query algorithm.

## 1. Explicit numerical interface

Put \(\ell=\log(en)\). The compiler supplies

\[
 R\le C\ell^8,\quad P\le C\ell^{16},\quad D\le C\ell^8,
 \quad N\le C\ell^{56},
 \tag{2}
\]

\[
 \log B\le C\ell^2,
 \quad \log\Lambda\le C\ell^{58},
 \quad \log(1/\eta)\le C\ell^{74}.
 \tag{3}
\]

At requested output precision \(b\), with compatible input precision,
one complete row/coefficient evaluation costs at most
\(C(2+b+\ell^{58})^{16}\) operations and
\(C(2+b+\ell^{58})^6\) bits of peak workspace. These counts include
the full matrix algorithms, all retained row-DAG nodes, and numerical
control bits; they do not treat a matrix root as a unit-cost operation.

Choose a target ideal-prefix error \(\exp(-c\ell^{100})\). The
source's accumulated numerical-error factor has logarithm

\[
 \log\left[P(1+\Lambda)^P(\Lambda+c_0+1)\right]
 \le C\ell^{74},
 \tag{4}
\]

where the noise-mark cap has logarithmic size at most \(C\ell^2\).
Consequently root, scalar-noise, row-evaluator, and final-rounding errors
can all be at most \(\kappa=\exp(-C_1\ell^{100})\), with a fixed
sufficiently large \(C_1\). Adding the \(O(\ell^{74})\) guard bits
does not change this precision degree. All stored row-output and prefix
grids can therefore use \(s=O(\ell^{100})\) fractional bits.

Every row evaluation then has time \(O(\ell^{1600})\) and peak
workspace \(O(\ell^{600})\). Integer parts contribute only
\(O(\ell^2)\) bits. In the selection lemma, the integer numerator
length is accordingly

\[
 \beta=O(s+\log(B+2))=O(\ell^{100}).
 \tag{5}
\]

These choices serve the intended \(\ell^{100}\)-precision context
interface. A downstream argument asking for a larger precision degree
must substitute that degree into the same counts; an unspecified
polylogarithmic tolerance alone would not justify the specific value
\(K=1700\).

## 2. Streaming support reduction

Let \(\widehat a_i=2^{-s}v_i\in\mathbb Q^P\), and append the
leading coordinate one to form \(b_i=(1,v_i)^T\). At stage \(k\),
the target is the exact rational vector
\((1,s_k/k)^T\), where \(s_k=\sum_{i\le k}v_i\) is maintained
as an integer vector.

Suppose the previous positive support columns are independent. Adding
one new column either preserves independence or creates a nullspace of
dimension exactly one. The latter follows because the old columns have
full column rank and only one column was added. A nonzero null vector
\(d\) has both signs because its coordinates sum to zero. Subtracting

\[
 \min_{d_j>0}(\alpha_j/d_j)\,d
 \tag{6}
\]

from the preliminary positive weights preserves the moment vector and
nonnegativity. At least one coordinate with \(d_j>0\) vanishes. Any
dependence remaining after all zero-weight columns are removed would
extend to a null vector of the enlarged matrix that vanishes at that
deleted coordinate. Since the nullspace is spanned by \(d\), this
would be the zero vector. Thus independence is restored in one elimination,
including when several weights vanish together. The support never exceeds
\(P+2\) before elimination and \(P+1\) afterward.

For the bit bound, select an invertible square row minor \(H\) of the
current independent columns, and the matching rows \(t\) of
\((k,s_k)^T\). The unique weights satisfy

\[
 H(kp)=t,
 \qquad p_j=\frac{\det H_j(t)}{k\det H}.
 \tag{7}
\]

Entries of \(H\) have \(O(\beta)\) bits; entries of \(t\) have
\(O(\beta+\log n)\) bits. The determinant expansion gives at most

\[
 L_w=C(P+1)[\beta+\log(en)+\log(P+2)]
 \tag{8}
\]

bits in each reduced numerator and denominator. Recomputing these unique
weights after every insertion enforces the bound. In particular there is
no cumulative product of \(n\) support determinants or a hidden \(n!\)
denominator.

The transient ratios in (6) have the same order of bit length: old
weights, preliminary scaling by \((k-1)/k\), and a null vector computed
from minors each have \(O(L_w)\)-bit descriptions; one quotient,
multiplication, and subtraction enlarge this by only a fixed factor.
Rank tests and determinants can use reduced rational elimination with
pivot search. Schur entries are ratios of minors. Computing cofactors
one at a time needs at most \(O((P+2)^5)\) rational operations, and
schoolbook arithmetic with Euclidean fraction reduction costs at most
\(O(L_w^3)\) per operation. Hence the candidate's explicit bound

\[
 Cn(P+2)^8[\beta+\log(en)+\log(P+2)]^3
 \tag{9}
\]

is valid. Substituting (2), (5) yields

\[
 W_{\rm selection}\le Cn\ell^{428},
 \qquad
 S_{\rm selection}\le C\ell^{148}
 \tag{10}
\]

before associated packet marks. Here \(428=8\cdot16+3\cdot100\),
and the candidate's workspace formula gives \(148=3\cdot16+100\).
Associated marks need \(O(\ell^{124})\) bits and do not enlarge
the workspace exponent. Individual weights have \(O(\ell^{116})\)
bits; all retained weights use \(O(\ell^{132})\) bits.

No minimum positive weight or condition-number assumption is required.
Ill-conditioned supports can change their exact determinants but cannot
exceed the determinant bit bound for the fixed integer input size.

## 3. Exact finite-tape reproduction

The stronger discrete implementation is correct. The evaluator is fixed
and deterministic, its output is on a common dyadic grid, and the source
prefix is formed with the same final rounding rule at each update.
Consequently the selected point vector

\[
 \widehat a_i=
 (\mathcal E_r(\widehat Z_i;\widehat C_{<r}))_{r=1}^{P}
 \tag{11}
\]

has the required common denominator. Suppose compact and source prefixes
agree through \(r-1\). Their calls to \(\mathcal E_r\) at the selected
packets then return exactly the same dyadic numbers used in (11).
Exact selection makes their weighted mean equal to the original \(n\)-row
mean, as a rational number. The identical stored noise and identical final
rounding imply equality of the next prefix. The empty prefix initiates
the induction.

The implementation must actually preserve this equality: the weighted
sum is computed exactly as a rational before the final rounding. It is
not rounded separately at every selected packet. Conversely, the source
mean sums dyadic integer numerators before its single division by \(n\).
The note states both requirements explicitly.

To bound compact weighted arithmetic, a product denominator for at most
\(q\le P+1\) selection weights has at most \(qL_w\) bits. Including
the common dyadic denominator gives length

\[
 O(qL_w+s+\log q)=O(\ell^{132}).
 \tag{12}
\]

Even summing by successive reduced rational operations, at cubic bit
cost, uses at most \(O(\ell^{412})\) operations per scalar update
and \(O(\ell^{428})\) for all \(P\) updates. These costs are much
smaller than the row evaluations below. Exact reproduction does not
require exact real Gaussian marks or exact transcendental arithmetic:
it concerns the explicitly defined finite source (10) of the candidate.
Comparison to the ideal source uses the separate error recurrence (4).

## 4. Gaussian law and bounded finite sampling

The ideal source law is the exact noisy two-orientation transcript law.
At each predictable call the supplied posterior computation gives the
correct conditional mean and positive covariance. A fresh Gaussian
innovation generates that conditional answer; chronological induction
gives the full joint transcript law, not just separate answer marginals.
First-layer row coordinates are sampled with their original Gaussian
law as part of the external packet. Actual empirical moments remain in
every coefficient calculation.

This permits a latent original dense root on a proof probability space
whose joint law with the ideal transcript is the dense Gaussian law.
The simulator need not compute that latent matrix. Adding scalar noise
to moment updates is then a new coupled perturbation. Quantizing roots
and evaluating the capped graph numerically is a further perturbation.
The candidate correctly distinguishes these three levels; its exact-law
phrase should always be interpreted at the first level.

The finite Box--Muller construction has a bounded running time. Let
\(M=nD+P\), choose \(\rho\asymp\delta_0/(M+1)\), and use midpoint
uniforms with \(t\) random bits each. On the event that all ideal radial
uniforms are at least \(\rho\), which fails with probability at most
\(M\rho\), the candidate's direct logarithm and square-root estimates
give coordinate coupling error at most

\[
 C\sqrt{2^{-t}/\rho}
   +C\sqrt{\log(2/\rho)},2^{-t}.
 \tag{13}
\]

Taking \(t\ge C[\log(1/\rho)+\log(1/\kappa)+1]\) suffices.
For fixed confidence and the precision in Section 1,
\(t=O(\ell^{100})\).

The implementation is bounded also off the coupling event. Every midpoint
lies between \(2^{-t-1}\) and \(1-2^{-t-1}\). Therefore the radial
quantity \(-2\log U\) is at most \(C(t+1)\) and is at least
\(2^{-t}\), using \(-\log U\ge1-U\). Evaluate the logarithm
accurately enough to retain, for example, half this lower bound, then
use the scalar root algorithm. Its logarithmic gap and input/output
precision are \(O(t+\log(1/\kappa))\). No rejection loop or undefined
logarithm occurs.

Scaling the logarithm argument into \([1,2]\) and using the displayed
geometrically convergent series takes a polynomial number of operations;
bounded-argument trigonometric series and the Machin formula for \(\pi\)
do also. They are dominated by the scalar-root bound \(O(t^{15})\)
from the explicit compiler, including sufficient error-allocation guard
bits. Thus generating the \(M\) finite coordinates has time at most

\[
 C(nD+P)\ell^{1500}\le Cn\ell^{1508}
 \tag{14}
\]

for sufficiently large widths. Storing the resulting packet coordinates
uses \(O(n\ell^{108})\) bits. These estimates include the random bits
needed for the midpoint uniforms. No claim is made that a finite sampler
has exactly the continuous Gaussian distribution.

## 5. Fully substituted work and space counts

The complete source sweep performs at most \(nP\) row evaluations.
The second pass constructing the \(P\)-component point vectors also
performs at most \(nP\) such evaluations. Evaluating each full row graph
from scratch costs \(O(\ell^{1600})\); this schedule does not rely
on caching between distinct rows or scalar stages. Both passes together
therefore cost

\[
 Cn\ell^{16+1600}=Cn\ell^{1616}.
 \tag{15}
\]

Integer accumulation of \(n\) dyadic summands adds only \(\log n\)
bits to an accumulator and is dominated by (15). Equations (10), (14)
are smaller. This proves the first bound in (1).

All compact training stages use at most \(Pq\le C\ell^{32}\)
row evaluations. Together with the exact weighted arithmetic in (12),
their total work is

\[
 C\ell^{32+1600}+C\ell^{428}
 \le C'\ell^{1632}.
 \tag{16}
\]

A single scalar-summary update has work at most \(C\ell^{1616}\).
A physical-time update that finishes an entire prescribed patch is bounded
by the all-training estimate, without assuming a favorable split of
stages between patches.

Temporary initialization memory is bounded by

\[
 C(n\ell^{108}+\ell^{600}),
 \tag{17}
\]

including packet storage, the complete numerical prefix, one row-evaluator
workspace, one selection workspace, and the current point vector.
In particular it is at most \(Cn\ell^{600}\) for \(n\ge1\).
It is not a polylogarithmic-initialization-space result.

The retained panel uses \(O(\ell^{124})\) packet bits,
\(O(\ell^{132})\) exact weight bits, and \(O(\ell^{116})\)
noise/history bits. The compiler's conservative stored instruction bound
adds at most \(O(\ell^{156})\) bits. The whole retained acquisition
description is therefore \(O(\ell^{156})\); compact training peak
space, including the row evaluator, is \(O(\ell^{600})\). No
\(n\)-row array, source prefix tape, or moment-vector table is retained
after the stated deletion boundary.

Taking \(K=1700\) simultaneously covers (15)--(17), the whole compact
training work, and these storage bounds. For each fixed problem,
\(\ell^{1700}/n\to0\), so initialization and training work are
eventually at most \(Cn^2\). This is an asymptotic upper bound; no
moderate practical threshold is implied.

## 6. Independent reference, fixed labels, and global scope

Suppose the dense-pair certificate is
\(\mathbb P\{\|f_n-f'_n\|_*>b_n(\gamma)\}\le\gamma\),
where \(\|\cdot\|_*\) is the candidate's all-time, whole-sphere
metric. Integrating this probability over the second trajectory yields
a fixed proof center \(f_{*,n}\) with

\[
 \mathbb P\{\|f_n-f_{*,n}\|_*>b_n(\gamma)\}\le\gamma.
 \tag{18}
\]

This selection is only a proof device; no center is numerically acquired
or stored. If a decoder built from the independent virtual source obeys
the candidate's downstream interface

\[
 \|f_C-f_{*,n}\|_*
 \le b_n(\gamma)+C\ell^{C_L}/\sqrt n
 \tag{19}
\]

on a source event of the specified probability, then on that event and
the reference event (18), the triangle inequality gives exactly

\[
 \|f_C-f_n^{\rm ref}\|_*
 \le2b_n(\gamma)+C\ell^{C_L}/\sqrt n.
 \tag{20}
\]

A union bound allocates the reference, source, finite-sampler, and numerical
failure shares. Independence of the source from the reference additionally
justifies the candidate's conditional assertion for each reference root
inside the event (18). It does not give a claim for every prescribed
reference root or exceptional dense matrix. The law argument in Section 4
does not turn this into fast compression of a specified realized root.

The all-time and all-input quantifiers in (20) follow because (18) and
(19) already use that metric. Acquisition equality is an equality of
every numerical prefix and therefore does not require another query
union bound. This check does not replace a missing uniform decoder proof
with pointwise query accuracy: (19) remains the named necessary input.

For each fixed nonzero label vector, the candidate's inherited factor
\(\exp(cY^2\sqrt\ell)\), with \(Y=\|y\|_2/\sqrt m>0\) and
\(c>0\), eventually dominates every fixed power \(\ell^{C_L}\).
This verifies the stated absorption of the remainder into the certificate
scale, provided the supplied certificate has that positive prefactor.
The threshold may depend on the fixed labels and depth. Uniformity for
width-dependent labels approaching zero would not follow from this
argument; the candidate does not claim it. At exactly zero labels,
the zero readout and zero residual give the exact zero trajectory and
predictor, as stated.

No additional label restriction, feature-Gram gap, depth scaling, or
population-kernel substitution enters the acquisition proof. Scientific
validity of the physical bridge and the two interfaces (18)--(19) is
inherited within the assigned scope, not independently established here.

## 7. Computational qualification

The numerical exponents above apply to the explicit arithmetic algorithms
and the stipulated fixed activation/data primitives. If an actual original
activation evaluator needs \(T_{\rm prim}(b)\) work or
\(S_{\rm prim}(b)\) space, include the compiler's corresponding terms
at \(b=O(\ell^{100})\) in every source and compact-row evaluation.
Merely saying that an arbitrary interface has some polynomial running time
does not preserve the particular exponent 1700 uniformly over such
interfaces. Its degree must be specified, or its cost kept explicit.

Subject to that qualification and the explicit \(\ell^{100}\)-precision
interface, the initialization and compact-training cost claims have fully
enumerated absolute exponents. The independent-reference conclusion is
supported as the stated conditional implication, with decoder calibration
and any replacement query algorithm outside this check.
