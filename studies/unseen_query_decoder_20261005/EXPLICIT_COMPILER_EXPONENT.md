# An explicit scalar and matrix compiler bound

2026-10-06. Scoped author derivation for the existing unseen-query study.
This is a compiler and precision interface, not an independent review or
a new proof of the physical-flow inputs. The six assigned source notes
and the specific short-program/physical-bridge corrections were read in
full. No experiment, other study, maintained-source edit, or Git mutation
was used. The required custom notation skill was inaccessible; the
supervisor authorized the explicit minimal-notation fallback.

The missing compiler degree can be made numerical. Write
\(\ell=\log(en)\). With fixed activation and data primitives, one
complete row/coefficient evaluation to absolute error \(2^{-b}\) has
the following conservative bounds:

\[
 N=O(\ell^{56}),\qquad
 \log \Lambda=O(\ell^{58}),\qquad
 \mathcal H=2+b+C\ell^{58},
 \tag{1}
\]

\[
 \text{time}\le C\mathcal H^{16},\qquad
 \text{peak bits}\le C\mathcal H^6.
 \tag{2}
\]

Here \(N\) counts scalar arithmetic instructions and specified matrix
macros, and \(\Lambda\) is a global Lipschitz bound for a row function
at a fixed scalar-history argument. The constants can depend on the
fixed admissible problem, including \(m,d,L\); the displayed degrees
do not. The bound includes the complete matrix implementations, not
unit-cost matrix inverses or roots.

For example, a requested precision \(b=O(\ell^{120})\) gives row
time \(O(\ell^{1920})\) and peak row-evaluation space
\(O(\ell^{720})\). These are derived exponents for this compiler.
An enclosing decoder must additionally count its own retained state,
randomness construction, query loops, and probability argument. No
Fourier, pseudorandomness, or conditional-decoder theorem is asserted
by this note.

## 1. Parameters and the exact program being compiled

Use the corrected collocation chronology in
`SHORT_CAUSAL_TRAINING_PROGRAM.md` and the capped physical program in
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`. Let \(R\ge2\) bound its number of
named principal fields, Gaussian matrix calls, and field evaluations,
after increasing a fixed problem-dependent constant. The sources give

\[
 R\le C\ell^8,\qquad P\le CR^2,\qquad D\le CR,
 \tag{3}
\]

where \(P\) counts scalar empirical summaries and \(D\) is the row
packet dimension. A passive query is included by increasing these
bounds by fixed constants and by allowing \(CR^2\) added summaries.
The source's finer counts are not needed below.

Take matrix-answer noise \(\sigma\) with
\(\log(1/\sigma)=O(\ell^2)\), as in that bridge, and put
\(\delta=\sigma^2\). A dyadic \(\sigma\) between one half and one
times \(e^{-\ell^2}\) is also allowed: the physical perturbation bound
only improves, and all logarithmic conditioning bounds are unchanged.
Choose a fixed sufficiently large constant \(C_*\) and define

\[
 X=C_*(2+n+R+\sigma^{-1}).
 \tag{4}
\]

It absorbs fixed physical, activation, radius, and input constants.
Thus \(\log X=O(\ell^2)\). A power of \(X\) is an amplitude cap,
not a number of operations. Its description and precision costs depend
on \(\log X\).

The row functions are compiled as directed acyclic graphs with shared
nodes. An already computed field is referred to by its address; its
defining expression is never recursively substituted into every use.
For one row-function evaluation, the earlier empirical summaries are
inputs, and the required earlier row nodes are evaluated in chronological
order and cached. This is evaluation at a fixed history, not recomputation
of that history by rerunning a width-\(n\) training process.

## 2. A complete physical scalar schedule

Each current hidden displacement has the source representation

\[
 D_\mathrm{learned}=\sum_{j=1}^{p}c_j a_jb_j^T/n,
 \qquad p\le mK(H+1)\le CR.
 \tag{5}
\]

The last inequality uses the corrected patch count and rank bound.
Only final right sides are appended at a committed endpoint; a Picard
node uses that committed list and the previous iteration's \(K\)
right sides. There is no expansion into \(K^J\) terms.

The following explicit loops implement each physical evaluation.
Every access to a history entry first clips that argument to its
certified box: fixed bounds for physical pair moments, the bounds in
Section 4 for innovation-containing moments, and the fixed residual
box where applicable. This clips arguments inside coefficient routines;
the Gaussian-noisy summary itself remains unclipped, as required by
the source construction.

1. For a displacement norm, obtain the existing pair moments
   \(A_{ij}=a_i^Ta_j/n\), \(B_{ij}=b_i^Tb_j/n\). Loop over
   \((i,j)\) and accumulate \(c_ic_jA_{ij}B_{ij}\). This uses
   \(O(p^2)\) binary scalar operations. The corresponding first-layer
   calculation replaces \(B_{ij}\) by a fixed input inner product;
   the readout norm uses just one Gram matrix.
2. If the projection radius in the normalized norm is \(a>0\), use
   the scalar multiplier
   \[
   \gamma(q)=a/\sqrt{\max\{a^2,q\}}.
   \tag{6}
   \]
   On genuine squared norms this is exactly the required ball
   projection factor. It is defined and Lipschitz even if an inconsistent
   scalar table gives negative \(q\), and it never divides by a number
   approaching zero. It uses a scalar root and a gapped division.
3. For a learned action, obtain \(t_j=b_j^Tv/n\), form
   \(c_jt_j\gamma(q)\), and accumulate
   \(\sum_j c_jt_j\gamma(q)a_{j,i}\) at the row under evaluation.
   This is \(O(p)\) scalar work per row. The transpose exchanges
   \(a_j\) and \(b_j\). First-layer actions use fixed input
   contractions. Readout and residual calculations are the same vector
   sums and normalized scalar pair moments.
4. Execute the fixed number of forward activation, carrier clipping,
   derivative gating, residual clipping, and rank-one gradient-factor
   instructions for each fixed training example and layer. An RMS
   projection of a feature or carrier uses its pair moment with itself
   and (6). Name the resulting factor once.
5. Form new pair moments only when both named fields exist. A moment
   integrand is the product of two row values; all its subsequent uses
   refer to its scalar-history address. The full table has \(O(R^2)\)
   entries. Deterministic arithmetic on that table does not create
   another empirical summary.

There are \(O(R)\) physical evaluations, each costing \(O(R^2)\)
scalar coefficient instructions and \(O(R)\) row instructions. Hence
the physical graph costs \(O(R^3)\) instructions before Gaussian
conditioning.

The collocation constants can be produced without an inversion of a
Vandermonde matrix. For the Chebyshev-root nodes, use the source's
discrete-cosine formula for each Lagrange basis polynomial, then integrate
each Chebyshev term. For \(k\ge2\), with \(z=2s-1\),

\[
 \int_0^s T_k(2u-1)\,du
 =\frac14\left[
 \frac{T_{k+1}(z)-T_{k+1}(-1)}{k+1}
 -\frac{T_{k-1}(z)-T_{k-1}(-1)}{k-1}\right].
 \tag{7}
\]

The cases \(k=0,1\) are \(s\) and \(s^2-s\). The recurrence
\(T_{k+1}(z)=2zT_k(z)-T_{k-1}(z)\) evaluates all needed terms.
Producing all \(K^2\) integration weights uses \(O(K^3)\le O(R^3)\)
scalar operations. An arbitrary time in a completed patch uses the
same formulas. The individual Lagrange polynomial has absolute value
at most \(2\), from its discrete-cosine formula, so its partial
integral has absolute value at most \(2\). Consequently all new
rank-list coefficients are bounded by a fixed constant times the
clipped residual; a committed list appends coefficients without
recursively multiplying them through the number of patches.

Cosines at these rational multiples of \(\pi\) can be reduced to
bounded arguments and evaluated by the power series, with a polynomial
number of bit operations in the requested precision. Alternatively they
can be supplied as the fixed universal scalar-constant interface.
Either convention is dominated by the bound in Section 6. Original
problem data and activation interfaces are distinguished in Section 8.

## 3. The Gaussian conditioning schedule

At each call use the formulas of
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`, with its notation
\(Q,K,H,J,v,x,d,t\). The following is an actual schedule.

1. Collect the physical query/answer candidate Gram, symmetrize it,
   take its positive part, and project it radially onto its prescribed
   Frobenius ball. Its dimension is \(O(R)\). Extract
   \(Q,K,H,J,v,x,d\) from this Gram. Keep innovation moments such
   as \(t\) in their separate certified boxes, as explicitly permitted
   by the corrected physical bridge.
2. Invert \(\delta I+Q\) and \(\delta I+K\) to obtain \(C,D\).
   Form \(-HC-DJ\). Vectorize
   \((\delta I+K)E+EQ=-HC-DJ\) and solve its positive Kronecker
   system of dimension at most \(R^2\).
3. Materialize
   \(\mathcal B=\delta I+K\otimes I+I\otimes Q\),
   \(R_v=I\otimes v\), and \(R_{Cv}=I\otimes(Cv)\).
   Invert \(\mathcal B\), then form
   \(B_1=R_v^T\mathcal B^{-1}R_v\) and
   \(B_2=R_{Cv}^T\mathcal B^{-1}R_v\).
4. Form \(f_0=d-v^TCv\), \(\beta=\delta+\max\{f_0,0\}\),
   \(F=\delta D(dI-B_1)\), and
   \(H_f=D(-f_0I+\delta B_2)\). Symmetrize \(F\) and take its
   positive part before the next root. These protections are identities
   for the exact formulas on the projected Gram domain.
5. Compute \((\delta I+F)^{1/2}\), its sum with
   \(\sqrt\beta I\), and the inverse of that sum. Multiply by
   \(H_f\) to obtain \(T\).
6. Form the coefficient vectors \(Cv\) and \(Dx+Ev+Tt\), then
   perform the source's row combination
   \[
   y_i=Y_{i,:}(Cv)+U_{i,:}(Dx+Ev+Tt)+\sqrt\beta\,g_i.
   \tag{8}
   \]
   Clip this named physical answer at its certified coordinate cap.
   Reverse calls use the exchanged formula. Empty histories omit their
   empty arrays. The first call needs only its scalar variance.

There are a fixed number of inverse/root/positive-part/cap macros per
call, each of dimension at most \(r=CR^2\). Constructing their arrays
uses at most \(O(R^4)\) assignments. Even implementing every displayed
matrix product as a dense product of padded \(r\)-dimensional arrays
uses only \(O(R^6)\) scalar instructions per call. This is an explicit
loose bound; exploiting the rectangular factors would reduce it.

Combining \(O(R)\) calls with the physical schedule proves

\[
 N\le CR^7,
 \qquad r\le CR^2,
 \tag{9}
\]

with \(O(R)\) non-scalar matrix macros and at most \(O(R^3)\)
scalar root/division macros from physical norms if these are all counted
separately. Both are below \(N\). This count includes explicitly
materialized Kronecker matrices and all pair-moment row products.

## 4. Absolute caps, including recursive row operands

The physical RMS bounds apply to the actual noisy physical program at
every arbitrary Picard evaluation, not just the exact trajectory:
initialized inputs are RMS-capped, projected learned displacements have
fixed operator bounds, and raw matrix noise has RMS at most two on the
specified event. Thus each named physical query, answer, feature,
carrier, and gradient factor has coordinate magnitude at most
\(C\sqrt n\). Insert that coordinate cap at every such principal
node. It is the identity on the source's good program event.

The physical Gram cap can therefore be \(CR\). Innovation moments
are kept separate, so they do not enlarge this physical Gram cap.
The mean bound in the corrected bridge gives

\[
 \|\overline Wq\|_{2,n}
 \le C(R\sigma^{-2}+R^2\sigma^{-4}),
 \qquad
 \|g\|_{2,n}
 \le C(1+R^2\sigma^{-5}).
 \tag{10}
\]

The second inequality follows from
\(g=\Gamma^{-1/2}(y-\overline Wq)\),
\(\Gamma\succeq\sigma^2I\), and the fixed RMS bound for \(y\).
It is a one-call inequality using physical old answers. It does not
iterate an inverse-noise loss through all previous calls.

Choose the innovation root cap at least
\(C\sqrt n(1+R^2\sigma^{-5})\), and cap each physical/innovation
cross-moment at least \(C(1+R^2\sigma^{-5})\). Root coordinates are
then bounded by \(X^9\), and the vector \(t\) by \(X^9\), after
increasing \(C_*\). Products of two named row fields are bounded by
\(X^{18}\). These are valid also for passive queries conditional on
the full training tape on the fresh raw-noise RMS event; no typical
Gaussian maximum under that conditioning is invoked.

Here is a direct degree check for the other operands. On the projected
physical Gram domain its extracted matrices and vectors have norm at
most \(X^2\). The inverses \(C,D,\mathcal B^{-1}\) have operator
norm at most \(X^2\); their Frobenius norms are at most \(X^4\).
The Sylvester solution has Frobenius norm at most \(X^6\). The factors
\(R_v,R_{Cv}\) have Frobenius norms at most \(X^3,X^5\). Direct
norm products give bounds \(X^8,X^{10}\) for \(B_1,B_2\), and
\(X^{13}\) for \(H_f\). The genuine Gram identities give
\(0\le f_0\le d\), \(0\preceq F\preceq dI\); all roots and
the final inverse therefore have the source's specified gaps. A bound
\(X^{16}\) covers \(T\) and its scalar partial sums.

The longest new row combination then has at most \(CR\) terms;
using \(\|t\|\le X^9\), principal physical row values at most
\(X\), and \(\sqrt\beta\le X^2\), every untruncated partial sum
in (8) is bounded by \(X^{30}\). Dense matrix-product partial sums
are bounded the same way by multiplying the displayed operand bounds
and the number of summands. Low-rank physical partial sums and their
norm calculations have at most \(CR^2\) summands with individually
bounded coefficients and factors, so also fall below \(X^{30}\).
The harmless slack between 30 and 100 covers sign splitting, scalar
norm products, and the fixed physical constants.

Thus every exact mathematical scalar or matrix operand, apart from the
internals of its numerical matrix implementation, can be capped at

\[
 U=X^{100}.
 \tag{11}
\]

This is not a cap propagated by repeated squaring. Principal physical
nodes are reset to their own \(C\sqrt n\) cap, innovations to their
own \(X^9\) cap, residuals to their fixed cap, and each conditioning
calculation starts from a newly projected physical Gram. Hence arbitrary
off-domain recursion cannot turn a physical row field into the next
uncapped oversized operand. The preceding bounds certify the intermediate
caps on the good event, while the explicit caps bound the extension
globally. Fixed activations and first derivatives have their supplied
bounded real derivatives; their values on capped arguments satisfy the
same amplitude bound after increasing the fixed constant.

## 5. Sensitivity and requested precision

For \(A,B\succeq\delta I\), the source supplies

\[
 \|A^{-1}-B^{-1}\|_F\le\delta^{-2}\|A-B\|_F,
 \qquad
 \|A^{1/2}-B^{1/2}\|_F
 \le(2\sqrt\delta)^{-1}\|A-B\|_F.
 \tag{12}
\]

PSD and radial projections are nonexpansive. Formula (6) has a fixed
lower denominator and a fixed Lipschitz bound. The final inverse in
Section 3 has gap at least \(2\sigma\); Sylvester solves are
ordinary inverses on the displayed positive Kronecker space. Conversion
from maximum entry error to Frobenius error costs at most \(r\le CR^2\).
Binary multiplication on \([-U,U]^2\) has Lipschitz constant at most
\(2U\), and addition, clipping, and fixed activation primitives have
the stated bounded constants.

It follows directly that a bound \(X^{202}\) covers the Lipschitz
constant of each scalar instruction or matrix macro, measured using
the maximum norm on all its input and output coordinates. This uses
(11), (12), and the dimension conversion, not continuity of eigenvectors.
Topological induction through at most \(N\) nodes gives

\[
 \log\Lambda\le C N\log X\le CR^7\log X.
 \tag{13}
\]

The same bound covers joint changes in capped roots, history inputs,
the sphere-query coordinates, and the within-patch time coordinate.
The row-function amplitude bound can be taken as \(B\le X^{200}\).

If every mathematical operation incurs absolute error at most
\(2^{-w}\) in its output coordinates, the same induction gives final
error at most \(N(1+X^{202})^N2^{-w}\). Therefore it suffices to use

\[
 w=b+C N\log_2 X+C\log_2(N+2).
 \tag{14}
\]

Choose the constant large enough also to give every perturbed gapped
matrix a half-gap margin. Projection outputs use the PSD-safe interface
in the next section. Every output is reset to a prescribed dyadic grid;
one does not propagate unrestricted exact rational representations
through the whole graph. Define

\[
 \mathcal H=2+b+CR^7\log_2X.
 \tag{15}
\]

Then \(N,r,w\le C\mathcal H\). Equations (3)--(4) imply the
first line of (1).

## 6. Actual bit algorithms for every matrix macro

The following explicit accounting strengthens the unspecified polynomial
in `FAST_SMALL_MATRIX_FUNCTIONS.md`. Suppose a macro input has dimension
\(r\), dyadic input precision \(p\), norm bound \(M\ge1\), gap
\(a\le1\) when needed, and target absolute Frobenius error \(2^{-b_0}\).
Let

\[
 h=2+r+p+b_0+\log_2 M+\log_2(1/a).
 \tag{16}
\]

For an ungapped positive-part macro omit the final term initially; its
internally introduced gap will have logarithm \(O(h)\).

**Inverse.** Clear the input dyadic denominator. Integer entries have
\(O(h)\) bits. Every determinant or minor has \(O(rh)=O(h^2)\)
bits, by the sum-of-\(r!\)-products bound. Compute the determinant and
all cofactors by rational elimination, choosing a nonzero pivot and
reducing each fraction after each operation. Schur entries are ratios
of minors, so their reduced numerators and denominators have \(O(h^2)\)
bits. A rational operation can be done in \(O(h^6)\) bit operations:
schoolbook multiplication/division costs quadratic time in bit length,
and a Euclidean gcd uses at most a linear number of such divisions.
There are \(O(r^5)\le O(h^5)\) rational operations across all
cofactor calculations. Thus inverse time is \(O(h^{11})\), with
\(O(h^4)\) bits of scratch if cofactors are computed sequentially.
Round the adjugate formula to the prescribed output grid.

**Positive square root.** Use the rounded Newton iteration in the fast
matrix note, starting from a dyadic scalar upper bound times the identity.
Its exact reference iteration takes \(J=O(h)\) steps. The displayed
error recurrence in that note allows an internal grid with \(O(h^2)\)
bits. An inverse at one Newton step now has minors of \(O(rh^2)\),
hence \(O(h^3)\), bits. Its rational operation cost is at most
\(O(h^9)\), and its cofactor count at most \(O(h^5)\). Thus all
Newton inversions cost \(O(h^{15})\) bit operations.

For the multiplication by the original dyadic input, keep the inverse
in adjugate form with its common determinant denominator. All entries
of that multiplication consequently have one shared denominator; summing
its terms does not multiply unrelated denominators. Their numerators
remain \(O(h^3)\) bits. This multiplication, symmetrization, and grid
rounding cost less than the inverse bound. Storing a constant number of
\(r\)-square rational arrays uses \(O(r^2h^3)\le O(h^5)\) bits.
Rounded iterates need not commute with the input: the fast note's
half-gap and Lipschitz recurrence expressly handles that case.
Before returning, round the final iterate symmetrically to entry
accuracy at most one fixed fraction of the requested Frobenius tolerance
divided by \(r\). The returned matrix therefore has only \(O(h)\)
bits per entry, even though Newton's private iteration grid had
\(O(h^2)\) bits. Include this last rounding in the local error budget
and the half-gap margin. The larger private precision is never passed
on as the next macro's ordinary input precision.

**Positive part and radial cap.** To approximate \(A_+\), choose
dyadic \(v\asymp2^{-b_0}/r\), form \(A^2+v^2I\), approximate
its square root to error at most \(v\), and return
\((A+Y)/2+vI\). This is dyadic and PSD; its error is at most \(2rv\).
The root's gap is \(v^2\), whose logarithmic reciprocal is \(O(h)\),
and its input precision and logarithmic upper bound are also \(O(h)\).
The preceding \(O(h^{15})\)-time, \(O(h^5)\)-space bound therefore
applies without an original spectral gap.

For a PSD radial cap of radius \(M_c\), compute an upper dyadic
approximation to its Frobenius norm and use a dyadic scale rounded down
from \(\min\{1,M_c/\text{upper norm}\}\). If necessary the denominator
is replaced by its maximum with \(M_c\), so it has a fixed certified
positive lower bound. Choose the scale accuracy to make its multiplication
error at most the allotted tolerance. Multiply the dyadic PSD matrix by
that dyadic nonnegative scale exactly. This preserves PSD and the cap;
the output grid has only a fixed multiple of the allotted number of bits.
It is reset according to this PSD-safe interface, not by a subsequent
unprotected entrywise rounding. Scalar roots and arithmetic are already
covered by the same bound.

Sylvester solves materialize and invert the positive Kronecker system,
whose full dimension was counted in \(r\). Every numerical macro thus
has time at most \(Ch^{15}\) and scratch at most \(Ch^5\). A
deliberate one-power allowance for output assembly and control also gives
\(Ch^{16}\) and \(Ch^6\), but is unnecessary inside an individual
macro. No reciprocal-gap-length series is used.

In the compiled graph, \(h\le C\mathcal H\), including the
tolerance-dependent PSD gap. There are at most \(N\le C\mathcal H\)
operations/macros. Hence the complete time is at most
\(C\mathcal H^{16}\). Storing all graph outputs, even as padded
matrices, takes at most \(CNr^2w\le C\mathcal H^4\) bits. Add
one \(O(\mathcal H^5)\) scratch area and the input, output, and
instruction buffers. The conservative \(C\mathcal H^6\) bound in
(2) follows. Numerical internals may exceed the mathematical cap (11),
but their \(O(\mathcal H^3)\)-bit sizes have just been counted.

## 7. Scalar noise, acquisition precision, and context precision

The scalar-update coupling of the source is

\[
 e_P\le\eta nP(1+\Lambda)^P
 \tag{17}
\]

on \(\max|E_r|\le n\). Appending up to \(CR^2\) query summaries
only changes its constant. With (13), choosing a dyadic scalar noise
with

\[
 \log_2(1/\eta)
 \ge (a+3)\log_2(en)+CR^9\log_2X
 \tag{18}
\]

makes the physical scalar perturbation smaller than \(n^{-a}\),
including a final Lipschitz output. In particular,
\(\log(1/\eta)=O(\ell^{74})\) suffices. This choice is made
after \(\sigma\); no coefficient bound depends circularly on \(\eta\).

For target retained-history accuracy \(2^{-b_h}\), the source's
positive-weight quantization recurrence gives a sufficient common entry
precision

\[
 b_{\mathrm{entry}}
 =b_h+CR^9\log_2X+C\log_2(en).
 \tag{19}
\]

Indeed its amplification is
\(P(1+\Lambda)^P(\Lambda+2B+\eta+1)\); the logarithm is bounded
by the extra terms in (19). Root/noise integer parts and the weight-grid
factor \(q\le P+1\) fit the same bound. The \(qD+q+2P=O(R^3)\)
selected-packet, weight, noise, and acquired-history entries use at most
\(CR^3b_{\mathrm{entry}}\) bits. A deliberately uncompressed stored
instruction list, even with one precision-sized literal per instruction,
adds at most \(CR^7(b_{\mathrm{entry}}+\log R)\) bits. This makes
the retained description completely finite; more economical templates
are possible but are not needed here.

For any requested \(b_h=O(\ell^c)\), \(c\ge74\), this gives
retained panel bits \(O(\ell^{c+24})\), full retained description
bits \(O(\ell^{c+56})\), and evaluation space
\(O(\ell^{6c})\) when the updater requests comparable precision.
The base choice \(c=74\) consequently permits numerical exponents
130 for the retained compiler/panel description and 444 for its updater's
peak workspace. A decoder can require a larger \(c\); these base
numbers are not a claim about an unexamined enclosing decoder.

For context covering it is useful to distinguish a row function from
the full sequential moment recursion. Composing at most \(CR^2\)
summary updates gives

\[
 \log\operatorname{Lip}(\text{full capped recursion})
 \le CR^9\log X=O(\ell^{74}).
 \tag{20}
\]

Normalized empirical or convex weighted averages do not introduce a
factor \(n\) in this Lipschitz bound. Thus a context grid with error
\(2^{-C\ell^{100}}\) yields deterministic output error at most
\(\exp[-c\ell^{100}+C'\ell^{74}]\), regardless of an internal
arithmetic precision as large as \(C\ell^{120}\). Precision is not
an amplitude. A Gaussian cutoff of size \(O(\ell^{60})\) is also
inside the existing \(X^9\) cap at all sufficiently large widths.
If a covering proof needs only an inverse-polynomial output margin,
this context error is more than sufficient; it is not a probability
that must be union-bounded over contexts. A different proof demanding
smaller deterministic margins must substitute its actual margin.

The transfer should compare exact capped mathematical circuits and then
add their uniform arithmetic errors. The rounded interpreter itself
contains comparisons and rounding jumps and is not being claimed
Lipschitz.

## 8. Work accounting and the activation qualification

For any fixed precision degree \(c\), (2) is a fixed power of
\(\log(en)\). Streaming an evaluation over \(n\) source rows and
over \(P\) summary stages takes at most
\(CnP\mathcal H^{16}\) primitive-model bit operations. Streaming
over \(q\le P+1\) retained packets instead takes at most
\(CPq\mathcal H^{16}\). For each fixed admissible problem and
fixed \(c\), both are eventually at most \(C'n^2\), since every
fixed power of \(\log(en)\) is \(o(n)\). The constant and threshold
may depend on that problem and degree.

These statements count these loops and row arithmetic only. They do not
prove a particular source-selection algorithm, finite randomness
generator, or initialized-dense-input acquisition bound. For example,
reading \(n^2\) externally supplied entries to a growing bit precision
can already cost more than \(O(n^2)\) bit operations. The outer
construction must specify which source it generates or reads.

The fixed-primitive convention means that the original activations and
their required first derivatives, and the permitted fixed problem data,
can be supplied to the requested \(w=O(\mathcal H)\) precision with
their external cost excluded. All interfaces receive only arguments of
logarithmic magnitude \(O(\log X)\). If their actual maximum time
and workspace costs are \(T_{\rm prim}(w,\log X)\) and
\(S_{\rm prim}(w,\log X)\), the corresponding bounds are instead

\[
 T_{\rm row}
 \le C\mathcal H^{16}
       +CN\,T_{\rm prim}(C\mathcal H,C\log X),
 \qquad
 S_{\rm row}
 \le C\mathcal H^6
       +S_{\rm prim}(C\mathcal H,C\log X).
 \tag{21}
\]

Bare strip analyticity does not furnish a universal numerical exponent
for arbitrary evaluator implementations. Such an exponent requires a
computational interface assumption. In the stipulated fixed-primitive
model, however, every exponent in (1)--(2), (18)--(20), and the retained
bit bounds follows from the displayed schedules and arithmetic counts.

## Scope of the conclusion

This supplies the previously missing numerical physical compiler count,
range certificate, global sensitivity, finite-precision schedule, and
fast matrix bit bounds. It does not change the source's nonlinear
physical approximation, empirical-average interactions, large innovation
caps, or positive weighted acquisition theorem. It also does not identify
an arbitrary new query algorithm with the original dense prediction.
Any final storage exponent combines this explicit interface with the
separately proved enclosing algorithm; choosing \(b=O(\ell^{120})\)
requires and permits the concrete row workspace exponent 720.
