# Finite generators and numerical backends for the integrated decoder

Author completion, 2026-10-07. This section supplies proofs, not a new
probabilistic source assumption. Its finite program, precision schedule and
physical source are specified in the adjacent integrated construction.
All parameters in this section are local algorithmic resources. In
particular, the field count below is not a new compression order.

## A. An explicit finite-space generator, including its error proof

An \(a\)-bit affine Toeplitz hash is \(h(x)=Tx+b\) over the field with two
elements. Its seed consists of the \(2a-1\) diagonals of \(T\) and the
\(a\) bits of \(b\), independently uniform. For distinct \(x,y\), the
pair \(h(x),h(y)\) is uniform on two independent \(a\)-bit strings. Indeed,
for a nonzero vector \(x-y\), let \(j\) be its first nonzero coordinate.
In the successive coordinates of \(T(x-y)\), the diagonal indexed by
\(i-j\) occurs with coefficient one; all other participating diagonals
have smaller index. Prescribing the remaining diagonals and solving in
increasing \(i\) proves surjectivity. The independent offset then proves
the assertion about the pair.

For independent hashes, define recursively
\[
G_0(x)=x,\qquad
G_k(x)=G_{k-1}(x)\,\Vert\,G_{k-1}(h_k(x)),
\]
where the two children share the same lower-level hashes. This is the
affine-hash recursive construction associated with
[Nisan's finite-space generator](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
The following direct expectation argument proves the precise version
needed here, without invoking that paper's probability theorem.

Consider a deterministic machine with at most \(s=2^u\) states between
blocks. Its block counter is included in these states, so the transition
rule may depend on the position. The machine reads \(N\) blocks; pad its
execution to \(2^k\), where \(k=\lceil\log_2 N\rceil\), by absorbing
states. It may perform arbitrary computation within a block. If
\[
a\ge\max\{\text{raw block length},\,
4u+2k+2\lceil\log_2(1/\varepsilon)\rceil+4\},
\tag{WB.1}
\]
then the acceptance probabilities under \(G_k\) and independent uniform
blocks differ by at most \(\varepsilon\). The seed has exactly
\(a+k(3a-1)\) bits.

Here is a proof. Write \(\mu\) for uniform measure on \(a\)-bit strings.
Pairwise independence gives, for arbitrary subsets \(A,B\),
\[
\mathbb E_h\left[
\mu\{x\in A:h(x)\in B\}-\mu(A)\mu(B)
\right]^2
=2^{-a}\mu(A)\mu(B)(1-\mu(B)).
\tag{WB.2}
\]
Fix all lower-level hashes. Let \(A_{ij}\) be the seeds that send machine
state \(i\) to state \(j\) through the lower-level generator. For each
\(i\), these sets partition the seed space. Let \(M_{k-1}\) be its
transition matrix averaged over its root seed. Its square has entries
\(\sum_l\mu(A_{il})\mu(A_{lj})\). The transition matrix \(M_k\)
instead has entries
\(\sum_l\mu\{x\in A_{il}:h_k(x)\in A_{lj}\}\).
By (WB.2), Cauchy--Schwarz, and the partition identities,
\[
\begin{aligned}
\mathbb E_{h_k}\|M_k-M_{k-1}^2\|_\infty
&\le 2^{-a/2}\sum_{i,l,j}
\sqrt{\mu(A_{il})\mu(A_{lj})}\\
&\le s^2 2^{-a/2}.
\end{aligned}
\tag{WB.3}
\]
Here \(\|M\|_\infty=\max_i\sum_j|M_{ij}|\). If \(N_{k-1}\)
is the transition matrix under independent blocks, then
\(N_k=N_{k-1}^2\). Stochastic matrices have this norm one, so
\[
\|M^2-N^2\|_\infty\le2\|M-N\|_\infty.
\]
Consequently
\[
\mathbb E\|M_k-N_k\|_\infty
\le(2^k-1)2^{2u-a/2}\le\varepsilon/4.
\tag{WB.4}
\]
An acceptance event is a subset of final states; its probability
difference is bounded by this norm. Averaging also over the root seed
proves (WB.1). In particular no claim that generated blocks are
independent, no cryptographic hypothesis, and no unproved generator
lemma is needed.

For a finite scalar transcript of at most \(B\) bits, fix both a
candidate transcript and all independent scalar-noise marks. The
one-pass verifier recomputes its row reductions at the candidate's
creation-time arguments and checks its guarded scalar instructions.
Induction over those instructions shows that it accepts exactly the
candidate transcript. Apply (WB.1) to each candidate with error
\(\varepsilon 2^{-B-1}\), and sum the absolute probability differences
over at most \(2^B\) candidates. The total variation distance is at most
\(\varepsilon\). The same bound holds after averaging the independently
retained noise marks. The proof uses the candidates only as tests; the
algorithm never enumerates them.

For the finite program below, the verifier's state and transcript have
at most \(CR^2w\) bits, including exact dyadic accumulators, row counters,
rounding decisions and guarded branches. Thus (WB.1) permits an inner
block of \(CR^2w\) bits. A full member, including its independent noise
marks, needs at most
\[
C\{R^2w\log(en)+\log(N_{\rm ext}/\delta)\}
\tag{WB.5}
\]
random bits. The outer application reads one complete member per block.
For a fixed external input/time code, its test executes the member,
compares its finite answer to the fixed success interval, discards its
workspace, and increments a bad-member counter. Thus the counter test
needs \(CR^2w+\log(J+2)\) between-block bits, not a table of all member
answers. Taking per-test error \(\delta/(16N_{\rm ext})\), (WB.1)
gives the stated outer seed. The fixed interval may have real endpoints:
on the finite answer alphabet the comparison is just a finite Boolean
transition table in this probability test, not a real-number oracle in
the implemented algorithm.

For independent members with bad probability at most \(1/16\), an odd
\(J\ge\lceil\log_2(16N_{\rm ext}/\delta)\rceil\) has bad median
probability at most \(2^J(1/16)^{J/2}=2^{-J}\). The outer generator,
then a union over codes, proves the simultaneous claim. This argument
amplifies complete source experiments, not conditionally successful
members sharing an unamplified source failure.

## B. Exact word model and generator streaming

A word contains \(w\) bits. The counted primitives are word reads and
writes, comparisons, addition and subtraction, Boolean operations,
bounded shifts, a full product returned in two words, and integer
quotient/remainder on a constant number of words. Constant-factor wider
scalars occupy a constant number of words. Integers with \(O(Rw)\) bits
occupy \(O(R)\) words. There is no matrix-function, Gaussian, activation,
unbounded-integer or carryless-multiplication oracle.

For a \(t\)-bit Toeplitz hash, each input bit selects a contiguous
\(t\)-bit window of the packed diagonal string to XOR into the output.
Each window word uses at most two stored words and bounded shifts.
Including the affine offset, the work is at most
\(Ct\lceil t/w\rceil\), with \(C\lceil t/w\rceil\) scratch words.
Traverse the generator depth first, storing pending right-child
arguments. The full padded tree has fewer than \(2N\) internal nodes.
It therefore produces its ordered stream with
\[
CNt\lceil t/w\rceil\text{ word operations},\qquad
C\lceil t/w\rceil\log(N+2)\text{ words}.
\tag{WB.6}
\]
This space includes the seed, traversal stack, flags and counters. Every
query restarts the same ordered stream a constant number of times per
layer; no sparse random-access regeneration is assumed. An outer stream
is suspended, with its stack retained, while its current member is used.

## C. Exact metric selection, including large integers

The finite field table is an \(n\)-by-\(s\) dyadic matrix \(V\),
\(s\le CR\), with entries of \(O(w)\) bits. Include its constant field.
Let its exact rank be \(r\le\min(n,s)\). Select independent columns and
an invertible \(r\)-row square block \(H\) of these columns. Put
\[
C_V=V_{:,J}H^{-1},\qquad M=C_V^\top C_V/n.
\tag{WB.7}
\]
Then \(V=C_VV_{I,:}\), and every required empirical field product is
exactly a product of selected values with \(M\). The selected rows of
\(C_V\) form the identity, whence \(M\succeq I/n\). Its constant-field
identity is \(\mathbf1^\top M\mathbf1=1\).

If some coefficient has absolute value greater than two, replace the
corresponding row of \(H\) by that row. Multilinearity shows that the
absolute determinant more than doubles. With a common \(O(w)\)-bit
dyadic denominator, a nonzero determinant is at least \(2^{-Crw}\);
Hadamard's bound is \(r^{r/2}2^{Crw}\). Because \(w\ge\log_2(r+2)\),
there are at most \(Crw\) swaps. At termination every coefficient is at
most two in absolute value. This bound concerns selected row values;
it does not assume a lower singular-value gap in the original data.

For completeness, exact rank and inverse arithmetic can be performed by
fraction-free elimination. For a pivot \(a_{kk}\), update
\[
a_{ij}\leftarrow
\frac{a_{kk}a_{ij}-a_{ik}a_{kj}}{a_{k-1,k-1}},
\qquad i,j>k,
\tag{WB.8}
\]
with denominator one at the first step and row/column pivoting when
necessary. The two-by-two minor identity proves by induction that the
division is exact and the intermediate entries are signed minors of
the original integer matrix. Applying the same elimination to augmented
right sides yields the adjugate and determinant. All these integers
have \(O(rw)\) bits, even when the determinant is small.

Schoolbook arithmetic on \(k\) words takes \(O(k^2)\) word operations.
For division, use radix \(2^{\lfloor w/4\rfloor}\) and normalize the
leading divisor digit to at least half the radix. The two-leading-digit
quotient estimate is too large by at most two: the omitted divisor tail
changes its trial product by less than twice the normalized divisor.
Correcting and subtracting therefore takes \(O(k)\) work per quotient
digit and \(O(k^2)\) overall. These steps use only the declared
constant-word products and divisions.

A rank test or adjugate consequently costs \(O(r^5)\) word work.
A coefficient scan costs \(O(nr^4)\); \(r\le n\) absorbs one adjugate
per scan. Including the initial exact rank scan, at most \(Crw\) swaps,
and the final metric scan gives
\[
W_{\rm metric}\le CnR^5w,\qquad
M_{\rm metric}\le C(nR+R^3)\text{ words}.
\tag{WB.9}
\]
The algorithm stores the original \(O(w)\)-bit dyadic table \(V\), not
the expanded rational table \(C_V\). Each row of \(C_V\) is computed,
used for the swap test or exact metric accumulator, and discarded.
Only the inverse/adjugate and the \(r\)-square large-integer accumulators
use \(O(R^3)\) words. This is essential to the stated peak memory.
For a final metric rounded entrywise to error at most \(\epsilon_M\),
add \(r\epsilon_M I\). The spectral norm of the rounding perturbation
is at most \(r\epsilon_M\), so this is positive semidefinite, and any
two selected fields bounded by \(B\) have pairing error at most
\(2r^2B^2\epsilon_M\). The adjacent replay proof chooses this tolerance
before setup and charges its noise-boundary probability.

## D. Finite spectral routines without eigenvalue separation

Let a symmetric \(r\)-square dyadic matrix have norm at most \(M\ge1\)
and \(p\)-bit entries. Suppose the requested absolute error is \(2^{-b}\).
For inverse or a gapped square root let the stated positive gap be
\(a\in(0,1]\). Set locally
\[
v=2+p+b+\lceil\log_2(r+2)\rceil+
\lceil\log_2(M+2)\rceil+\lceil\log_2(1/a)\rceil.
\tag{WB.10}
\]
For positive part, omit the last term. A sufficiently large universal
multiple of \(v\) working bits suffices. This is already included in
the integrated word length; it is not \(R\) times that word length.

Here are a terminating algorithm and its error analysis. Use a largest
off-diagonal Jacobi pivot with a fixed lexicographic tie rule. If \(e\)
is the Frobenius off-diagonal norm, a pivot has square at least
\(e^2/[r(r-1)]\). An exact rotation removes twice that square from
\(e^2\). For a target diagonalization residual \(t\le1\), stop at
\(e\le t/16\), or perform at most
\[
K=\left\lceil 8r(r-1)\log\frac{64r(M+1)}t\right\rceil
\tag{WB.11}
\]
rotations. With local rounding errors at most
\(t/[2^{16}K r^3(M+1)^2]\), the rounded recurrence satisfies
\[
e_{j+1}\le\sqrt{1-2/[r(r-1)]}\,e_j+
t/[2^{10}Kr(M+1)].
\]
Its geometric sum, and the product telescoping estimates for the
rotations and updated basis, bound both the final off-diagonal norm
and the accumulated similarity error by \(t/8\), and bound the
orthogonality defect by \(t/[8(M+1)]\), after reducing local errors by
another fixed numerical factor if needed. Thus the iteration cap
always reaches the prescribed residual scale. Every local tolerance
has logarithm \(O(v)\), since \(K=O(r^2v)\).

The two-dimensional rotation is computed from its two diagonal entries
and pivot. The stable quadratic formula chooses a tangent of magnitude
at most one, followed by a positive scalar square root for its cosine.
Before stopping the pivot has magnitude at least \(t/[16r]\); hence
these divisions require only \(O(v)\) guard bits, not the inverse of
an eigenvalue separation. Scalar square roots use binary search on an
integer square, with \(O(w)\) constant-word operations.

For the computed basis \(V_0\), its exact polar correction
\(O=V_0(V_0^\top V_0)^{-1/2}\) exists when the orthogonality defect is
less than \(1/2\), and satisfies
\(\|O-V_0\|_F\le2\|V_0^\top V_0-I\|_F\). This follows by scalar
diagonalization of \(V_0^\top V_0\) on \([1/2,3/2]\). It is a proof
device, not a further implemented matrix operation. The preceding
bounds therefore give a nearby exactly orthogonally diagonalized
matrix within \(t\) of the input.

Choose \(t\le 2^{-b-8}a^2\) for inversion, and
\(t\le 2^{-b-8}\min(a,\sqrt a)\) for a gapped square root.
The identity \(A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}\) bounds the first
error. For square roots, their difference solves a Sylvester equation;
the inverse is the integral of left and right multiplication by
\(e^{-sA^{1/2}}\) and \(e^{-sB^{1/2}}\), bounded by
\(1/(2\sqrt a)\) in Frobenius norm when both gaps are at least \(a\).
Using the actual half-gap in this estimate covers the nearby matrix.
For positive part take \(t\le2^{-b-8}\). Positive part is the Euclidean
projection onto the positive-semidefinite cone; the two projection
variational inequalities, added together, prove it is Frobenius
nonexpansive. This proof uses no spectral gap at zero.

Evaluate the scalar functions on the approximate diagonal, clamping
small negative entries where a positive part is requested. Round all
nonnegative diagonal function values to nonnegative dyadics and form
\(V_0\operatorname{diag}(f_i)V_0^\top\) by exact dyadic products and
sums. This preserves positive semidefiniteness. The final scalars have
only a constant multiple of \(w\) bits, including the sum over \(r\).
No unsafe final entrywise rounding is used.

Store pivots in an indexed max-heap. One rotation changes only \(O(r)\)
matrix entries, so heap maintenance costs \(O(r\log(r+2))\).
The exact dyadic squared off-diagonal norm is updated by subtracting
old squares and adding new squares, also in \(O(r)\) operations.
Updating the basis costs \(O(r)\); scalar roots cost \(O(w)\).
With \(O(r^2w)\) rotations, the whole macro costs
\[
C\{r^3w\log(r+2)+r^2w^2\}\text{ word operations},
\qquad Cr^2\text{ words}.
\tag{WB.12}
\]
For \(r=1\), use just the scalar routine. Exact heap ordering and exact
residual accumulation give the same pivots and stop as a full-scan
finite algorithm. No hidden \(r^2\) scan occurs per rotation.

The decoder's coefficient solve also avoids a Kronecker-sized system.
For its two Gram matrices \(Q,K\succeq0\), diagonalize them separately.
In these bases a Sylvester equation
\[
(\sigma^2I+K)E+EQ=F
\]
is solved entrywise by division by \(\sigma^2+k_j+q_i\ge\sigma^2\).
Scalar divided differences of square roots are evaluated as
\((\sqrt a-\sqrt b)/(a-b)=1/(\sqrt a+\sqrt b)\), including \(a=b\).
All denominator floors are the already fixed noise floors, so the
normwise perturbation bounds in the finite construction apply to
nearby matrices without attempting to match individual eigenvectors.
This uses a constant number of (WB.12) macros and ordinary \(O(r^3)\)
scalar arithmetic per call.

## E. Finite Gaussian and activation values

Each Gaussian coordinate uses a dyadic uniform midpoint and inverse
normal CDF on \([-T,T]\), with \(T^2\le Cw\). Choose its dyadic
uniform precision so that
\[
\sqrt{2\pi}\,e^{T^2/2}2^{-b_U}
\le\epsilon_G/4.
\tag{WB.13}
\]
Clamp the midpoint to the CDF image of \([-T,T]\) before numerical
inversion; mass moved by this clamp is charged to the displayed tail event.
Couple the midpoint to a uniform variable in its cell. Except on the
two Gaussian tails, of probability at most \(2e^{-T^2/2}\), the
inverse-CDF Lipschitz bound gives coordinate error at most
\(\epsilon_G/4\), before numerical evaluation. The cutoff and failure
allocation used in the finite construction make \(b_U=O(w)\).

There is a finite implementation of that evaluation in \(Cw^2\) word
operations and \(O(1)\) scalar scratch. Indeed, integrate the Taylor
series of \(e^{-x^2/2}\) term by term on the cutoff interval. Since
\(T^2=O(w)\), \(Cw\) terms have a remainder below \(2^{-C'w}\), with
suitable fixed constants by the factorial bound
\(j!\ge(j/e)^j\). Intermediate terms have magnitude at most
\(e^{Cw}\), so \(Cw\) guard bits suffice. Its recurrence and summation
use \(O(w)\) word operations. Bisection of the coordinate takes
\(O(w)\) CDF evaluations. Use enclosing rational intervals throughout:
if a comparison overlaps, the positive density lower bound converts
the overlap into a coordinate interval. Thus no exact comparison of
transcendental numbers is assumed. The normalizing constant can be
computed to this precision from
\(\pi=16\arctan(1/5)-4\arctan(1/239)\), whose identity follows by
the tangent addition formula and the angle ranges. The alternating
series take \(O(w)\) terms; integer square root supplies the remaining
normalization. Its cost is smaller than the CDF bisection.

For tanh there is also an \(O(w)\)-word-work value evaluator, using
only \(O(1)\) scalar scratch. By oddness take \(x\ge0\). For absolute
error \(2^{-p}\), return one if \(x\ge p+4\); its error is at most
\(2e^{-2x}\). Otherwise scale \(z=2x/2^k\le1\), with
\(2^k\le4(p+4)\). The exponential series for \(e^{-z}\), truncated
after \(16(p+1)\) terms, has error far below \(2^{-p}\).
Use \(p+C\log_2(p+2)\) working bits, clip to \([0,1]\), and square
\(k\) times. On \([0,1]\), each squaring amplifies error by at most
two, so the total amplification is at most \(2^k\). The guard bits
cover it and the final rational map \((1-e^{-2x})/(1+e^{-2x})\),
whose denominator is at least one. All operations are finite.

For a different analytic activation its supplied finite evaluator's
actual work and workspace are added at every recorded value call.
Analyticity bounds approximation errors but does not give a finite
description or complexity bound for evaluating an arbitrary function.
This is an explicit computational interface, not a probabilistic
source assumption, and is necessary for the original activation scope.

## F. Complete modular ledger and substitution

There are at most \(CR\) spectral calls of size at most \(CR\).
Every selected field is created at immutable scalar arguments. Cache
both its selected value vector and its exact product with the fixed
metric; form all pairings by exact dyadic sums before their prescribed
rounding. There are \(O(R^2)\) cached words and \(O(R^3)\) ordinary
scalar work. The finite construction counts the same fields and calls
for an appended query; old fields are evaluated at their creation-time
arguments, not retrained.

Write locally \(a_{\rm blk}\asymp R^2w\) and let \(b_{\rm mem}\)
be (WB.5). For \(J\) complete ensemble members, retained and live
training/query storage is
\[
C\left[J R^2+
\left\lceil b_{\rm mem}/w\right\rceil\log(J+2)\right]
\text{ words}.
\tag{WB.14}
\]
Setup treats members sequentially, so its additional peak is
\(C(nR+R^3)\), not \(J\) times this temporary inventory. Including
all finite Gaussian coordinates, metric selection, coefficient
preparation, source-row streams and both generator levels gives
\[
\begin{aligned}
W_{\rm outer}&=CJb_{\rm mem}\lceil b_{\rm mem}/w\rceil,\\
W_{\rm init}&\le CJ\{nR^5w+(nR+R^2)w^2
+R^4w\log(R+2)+R^3w^2+R^4+nR^2
+na_{\rm blk}\lceil a_{\rm blk}/w\rceil\}+W_{\rm outer},\\
W_{\rm train}&\le CJ\{R^4w\log(R+2)+R^3w^2+R^4\},\\
W_{\rm query}&\le CJ(L+1)\{n[a_{\rm blk}\lceil a_{\rm blk}/w\rceil
+Rw^2+R^2]+R^3w\log(R+2)+R^2w^2+R^3\}\\
&\hspace{8mm}+W_{\rm outer}+CJ\log(J+2).
\end{aligned}
\tag{WB.15}
\]
The last term includes an ordinary sorting computation of the median.
All exact accumulators, temporary member blocks, suspended generator
stacks and selected-field caches are counted. Input/certificate access
and the supplied activation evaluator are added as stated in Part II.

Finally insert the already proved bounds
\[
R\le Cp\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\quad
w\le C\beta^{110L}Z,\quad J\le C(d+1)Z.
\tag{WB.16}
\]
The leading memory terms are \(JR^2\) and
\(R^2\log(en)\log(J+2)\). They are bounded by
\[
Cp^2\beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^6
[d+1+\log(e+(d+1)Z)].
\tag{WB.17}
\]
The leading setup term \(JnR^5w\) gives the exponents \(1115L\)
and \(29/2\). The leading training term \(JR^4w\log(R+2)\)
gives \(914L\) and \(12\). Inner and outer query hashing give,
respectively, \((L+1)nZ^{12}\) and \(Z^{14}\) with the same
\(p^4\beta^{914L}(m+d+2)^4(1+m/\gamma)^4(d+1)\) coefficient.
These are exactly the existing headline bounds. Word length is
separate: multiplying (WB.17) by \(w\) adds one logarithmic power
to the retained bit count.

When \(0<nY<1\), every appearance of \(Z\) in this construction and
ledger is replaced by \(Z+\log_+(1/(nY))\), together with the stated
finite Gaussian-RMS gate. This includes field counts and external
codes, not just word length. Zero labels use the exact zero branch.
