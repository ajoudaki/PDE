# Dense-budget initialization by a Gaussian row source and streaming selection

2026-10-06. Scoped author proof in the unseen-query decoder study. No
experiments, promotion, source-file changes, or Git operations. The permitted
inputs are the short causal program, noisy two-orientation law, scalar-history
acquisition, finite-precision selection, physical bridge, fast small-matrix
note, and the dense-budget result and assembly. References within those
inputs are inherited hypotheses, not additional sources inspected here.
The required custom notation skill was unreadable (permission denied); the
supplied notation conventions and mathematical proof/research skills were
applied.

The source generation and positive packet selection can be completed in
\(n\operatorname{polylog}(n)\) work and temporary
\(n\operatorname{polylog}(n)\) space. The retained packet panel and its
subsequent causal acquisition use absolute-polylogarithmic space and work.
Here every displayed polylogarithmic exponent in a **complexity** bound is
absolute; constants may depend on the fixed admissible problem. These
bounds are eventually below \(O(n^2)\), unlike
\(n^2\operatorname{polylog}(n)\).

This conclusion uses a fresh source with the exact original Gaussian
initialization law, represented without forming its dense matrices. It does
not recover the trajectory of a specified already-realized dense root. It
does preserve the dense-versus-independent-dense upper-certificate target,
with the probability quantifiers in Section 6. Efficient recalibration of the
query decoder is a separate obligation; nothing here makes the old exhaustive
calibration algorithm efficient.

## 1. Finite source and numerical interface

Let \(n\) be the original dense width. Keep the source model's depth,
training data, Gaussian initialization, zero readout, nonlinear feature
updates, block mobilities, small-label allowance, and original feature-Gram
gap. Set \(\ell_n=\log(en)\). The supplied physical bridge has at most
\(R\le C\ell_n^8\) initialized-matrix calls and named physical row fields.
Its noisy conditioning representation has Gaussian packets
\(Z_i\in\mathbb R^D\), \(D\le d+R\), and scalar moment updates

\[
 C_r=\frac1n\sum_{i=1}^n F_r(Z_i;C_{<r})+\eta E_r,
 \qquad 1\le r\le P,\qquad P\le CR^2.                 \tag{1}
\]

Here \(Z_1,\ldots,Z_n\) are iid standard Gaussian packets, the
\(E_r\) are independent standard Gaussian variables independent of the
packets, and \(C_{<r}=(C_1,\ldots,C_{r-1})\). Extra raw pair moments
required by the dense-budget assembly are included in \(P\). Previously
created fields keep their defining older scalar arguments.

Each \(F_r\) is a fixed finite directed acyclic graph using coordinate
arithmetic, the prescribed activations, and the small matrix routines in
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`. Let \(N\) bound its graph size and
the shared instruction description. Then \(N\) is an absolute polynomial
in \(R\). Its matrices have dimension at most \(R^2\). The bounded
extensions in the physical bridge supply, for all arguments,

\[
 |F_r(z;c)|\le B,
 \qquad
 |F_r(z;c)-F_r(z';c')|
 \le \Lambda\bigl(\|z-z'\|_\infty+\|c-c'\|_\infty\bigr),
                                                            \tag{2}
\]

where \(\log(B+2)\), \(\log(\Lambda+2)\), the logarithmic inverse
noise levels, and all prescribed logarithmic output tolerances are absolute
polynomials in \(\ell_n\). The additional scalar noise in (1) changes
the exact noisy-matrix law; the physical bridge controls this change by its
stated coupling, not by an exact posterior identity.

`FAST_SMALL_MATRIX_FUNCTIONS.md` proves polynomial work and space for each
inverse, positive square root, positive-part projection and Sylvester solve
in the graph, in its matrix dimension and logarithmic bounds and accuracy.
Consequently one evaluation of \(F_r\), with all nodes cached in a
topological order, costs a polynomial in

\[
 N+R+D+b+\log(B+\Lambda+2),                              \tag{3}
\]

where \(b\) is the requested precision together with the input precisions.
No recursive duplication of shared subgraphs is required. These are
arithmetic/activation-primitive work bounds. They are bit-work bounds as
well if the activation and numerical-input precision interfaces run in
polynomial time. Merely polynomial-space precision access does not imply
that extra conclusion.

## 2. Streaming rational support reduction

The following deterministic lemma replaces exhaustive support enumeration.
It is independent of Gaussian probability, smoothness, and conditioning.

**Lemma.** Suppose \(\widehat a_1,\ldots,\widehat a_n\in\mathbb Q^P\)
have a common dyadic denominator \(2^s\). Write
\(\widehat a_i=2^{-s}v_i\), \(v_i\in\mathbb Z^P\), and suppose each
integer coordinate of \(v_i\) has at most \(\beta\) bits. A sequential
algorithm returns indices \(i_1,\ldots,i_q\), \(q\le P+1\), and
nonnegative rational weights with

\[
 \sum_{j=1}^q p_j=1,
 \qquad
 \sum_{j=1}^q p_j\widehat a_{i_j}
        =\frac1n\sum_{i=1}^n\widehat a_i.                \tag{4}
\]

It uses \(n\operatorname{poly}(P,\beta,\log(en))\) bit operations and
\(\operatorname{poly}(P,\beta,\log(en))\) temporary bits, excluding the
root marks associated with its at most \(P+2\) current points. Every
positive support is affinely independent. Every retained weight has
numerator and denominator bit length at most

\[
 C(P+1)\bigl[\beta+\log(en)+\log(P+2)\bigr].             \tag{5}
\]

**Proof.** Define integer columns \(b_i=(1,v_i)^T\in\mathbb Z^{P+1}\)
and integer prefix sums \(s_k=\sum_{i=1}^k v_i\). After processing
\(k\) points maintain positive weights on linearly independent columns
\(b_{i_j}\), with

\[
 \sum_j p_j b_{i_j}=(1,s_k/k)^T.                         \tag{6}
\]

For \(k=1\) use its single point and weight one. On insertion of point
\(k\ge2\), multiply the previous weights by \((k-1)/k\) and assign
weight \(1/k\) to \(b_k\). Denote these preliminary positive weights
by \(\alpha\). Equation (6) holds for this at-most-\(P+2\)-point set.

If its columns are independent, retain it. Otherwise the old columns are
independent and the new one lies in their span, so the enlarged matrix has
a one-dimensional nullspace. Exact rational elimination finds a nonzero
vector \(d\) with \(\sum_j d_j b_{i_j}=0\). Its first coordinate gives
\(\sum_jd_j=0\); therefore \(d\) has both positive and negative entries.
Put

\[
 \theta=\min_{d_j>0}\frac{\alpha_j}{d_j},
 \qquad p_j=\alpha_j-\theta d_j.                         \tag{7}
\]

All new weights are nonnegative, at least one is zero, and (6) is
preserved. Delete all zero-weight columns. At least one deleted column
has \(d_j>0\). If the remaining columns admitted a dependence, extending
it by zeros to the enlarged set would produce a vector in its
one-dimensional nullspace with zero at that deleted position. It would
have to be a multiple of \(d\), and hence be zero. Thus the remaining
columns are independent. There is at most one dependence elimination per
inserted point, including ties in (7).

It remains to count the rational descriptions; counting elimination steps
alone would not suffice. Let the current support have \(q\le P+1\)
columns. Choose \(q\) rows on which their integer column matrix has a
nonsingular minor \(H\), and let \(t\) be the same rows of the integer
vector \((k,s_k)^T\). Equation (6) implies

\[
 H(kp)=t,
 \qquad
 p_j=\frac{\det H_j(t)}{k\det H},                        \tag{8}
\]

where \(H_j(t)\) replaces column \(j\) of \(H\) by \(t\). The
entries of \(H\) have at most \(\beta+1\) bits. The entries of \(t\)
have at most \(\beta+\lceil\log_2 k\rceil+2\) bits because they are
integer sums, not iterated rational averages. The determinant expansion
has at most \(q!\) products of \(q\) entries. Its numerator and
denominator bounds give (5), uniformly for all \(k\le n\).

After each insertion, recompute the unique weights from (8), reduce them,
and discard the previous fractions. This is an explicit way to enforce
the bound; it avoids carrying symbolic denominators through \(n\)
successive updates. The exact target moment at the final stage has
denominator \(n2^s\), and at stage \(k\) has denominator \(k2^s\).
Neither \(n!\) nor a product of all earlier support determinants occurs.

All needed linear algebra is polynomial-bit arithmetic. For completeness,
rational Gaussian elimination with pivot search has Schur entries equal
to bordered minors divided by the current pivot minor. The determinant
bound just proved bounds their reduced numerators and denominators by
\(C(P+2)[\beta+\log(en)+\log(P+2)]\) bits. One rational arithmetic
operation before fraction reduction enlarges this by a constant factor.
Integer long arithmetic and Euclidean fraction reduction have polynomial
bit cost. Cofactor determinant computations give an intentionally coarse
polynomial algorithm for (8), and exact elimination supplies the rank and
the null vector in (7). All quantities inside one insertion therefore
have polynomial description length before the next reset as well.

For example, allowing \(O((P+2)^5)\) rational operations per insertion
and cubic bit cost in those description lengths yields the safe bound

\[
 O\!\left(n(P+2)^8
       [\beta+\log(en)+\log(P+2)]^3\right).              \tag{9}
\]

The selection workspace can be bounded by
\(O((P+2)^3[\beta+\log(en)+\log(P+2)])\) bits. Determinants and
cofactors may be computed one at a time. Associated packet marks and their
indices add only the space for \(P+2\) packets and
\(O(P\log(en))\) bits. This proves the lemma. \(\square\)

The determinant expansion is a size bound, not an instruction to enumerate
permutations. All determinant calculations use the polynomial algorithm
just described. No condition number or minimum positive weight is assumed.

## 3. Exact reproduction of a finite-precision source tape

One can retain the approximate-moment argument of
`FINITE_PRECISION_SOURCE_SELECTION.md`. The following slightly stronger
implementation avoids even that selection error.

Use finite stored packets \(\widehat Z_i\), stored scalar-noise marks
\(\widehat E_r\), a stored noise level \(\widehat\eta\), a fixed
deterministic numerical row evaluator \(\mathcal E_r\), and a fixed
rounding rule \(\mathcal R\). Each \(\mathcal E_r\) returns an element
of one common dyadic grid. Compute the numerical source chronologically by

\[
 \widehat C_r=
 \mathcal R\!\left[
    \frac1n\sum_i\mathcal E_r(\widehat Z_i;\widehat C_{<r})
        +\widehat\eta\widehat E_r\right].               \tag{10}
\]

At each empirical reduction, sum the dyadic integer numerators exactly and
divide by \(n\) only once. The accumulator needs only \(\log_2 n+O(1)\)
more bits than a summand. Round the resulting update back to the fixed
prefix grid using \(\mathcal R\). Thus source execution does not
accumulate denominator products either. With fractional grid precision
\(s\) and the bound (2), the integer-coordinate bound in the selection
lemma is \(\beta=O(s+\log(B+2))\), again polylogarithmic.

After computing the finite training prefix, stream the vectors

\[
 \widehat a_i=
 \bigl(\mathcal E_r(\widehat Z_i;\widehat C_{<r})\bigr)_{r=1}^P
                                                            \tag{11}
\]

through the lemma. The selected stored packets, exact rational weights,
and stored scalar-noise marks define compact updates

\[
 \widehat C_r^{c}=
 \mathcal R\!\left[
    \sum_jp_j\mathcal E_r(\widehat Z_{i_j};
                         \widehat C_{<r}^{c})
       +\widehat\eta\widehat E_r\right].                \tag{12}
\]

The weighted sums in (12) are evaluated exactly as rationals before applying
the same rounding rule. If the compact prefix equals the source prefix,
the next row-evaluation outputs are exactly those used in coordinate
\(r\) of (11). Equation (4) makes the two rational means identical;
the identical noise mark and rounding rule make the next prefix identical.
Induction gives

\[
 \widehat C_r^{c}=\widehat C_r\quad(1\le r\le P).       \tag{13}
\]

This is a discrete exactness statement. It does not claim an exact
finite-bit representation of a continuous Gaussian or transcendental
moment. Exact selection weights have the polynomial description (5).
Intermediate sums of at most \(P+1\) products of such weights and
dyadic row outputs also have polynomial descriptions, even if their
denominators are combined by the simplest product rule. No division by
a selected weight occurs.

To compare (10) with the ideal law (1), couple its stored Gaussian marks
to the ideal ones so their coordinate errors are at most \(\kappa\),
outside a separately charged failure event. Suppose the evaluator error
at its numerical arguments is at most \(\kappa\), and the combined
noise-level, noise-mark, and final-rounding error is at most
\(c\kappa\). From (2), with
\(e_r=\max_{a\le r}|\widehat C_a-C_a|\),

\[
 e_r\le(1+\Lambda)e_{r-1}+(\Lambda+c+1)\kappa,
 \qquad
 e_P\le P(1+\Lambda)^P(\Lambda+c+1)\kappa.               \tag{14}
\]

For a prescribed history tolerance \(\varepsilon_{\rm hist}\), choose
\(\kappa\) below its quotient by the displayed factor. If \(c\)
contains a cap on scalar-noise marks, its logarithm is counted too.
Every required logarithmic precision is an absolute polynomial in
\(\ell_n\). Local tolerances inside \(\mathcal E_r\) are made smaller
by the counted graph sensitivity. Identity (13) transfers (14) to compact
reexecution without an additional selection error. The continuous ideal
prefix remains the object in posterior probability arguments.

## 4. Generating the original finite Gaussian program without dense matrices

The exact row-law theorem gives, at each forward call, a formula of the form

\[
 y=Y(Cv)+U\{Dx+Ev+T(K)t\}+\sqrt\beta\,g,
 \qquad t=U^Tg/n,                                      \tag{15}
\]

with a corresponding reverse formula. Here \(g\sim N(0,I_n)\) is fresh;
all other coefficients are computed from previously acquired moments by
the explicitly gapped small matrices in that theorem. This is its notation:
\(C,D,E,T(K)\) in (15) are conditional matrix coefficients and are not
the scalar-history coordinates \(C_r\). Their largest matrix dimension
is at most \(R^2\).

Formula (15) uses scalar products and affine combinations of named row
arrays. Sampling the \(n\) independent packets supplies all its Gaussian
innovations and the original first-layer Gaussian row coordinates. Executing
the graph in chronological order therefore takes
\(n\operatorname{poly}(R,N,P,D)\) real primitive operations once its
small-matrix evaluations are counted. The rows interact through their actual
empirical moments; they are not replaced by independent population feature
evolutions. Forward and transpose calls, residuals, nonlinear gates, and
all low-rank learned displacements remain in the graph.

The exactness claim concerns the law of this finite real-valued graph.
At a call, the supplied Gaussian likelihood calculation gives precisely
the conditional mean and covariance used in (15). Induction over its
predictable calls therefore gives the same joint law as the actual
initialized Gaussian matrices with the prescribed independent answer
noises. On the dense probability space the whitened innovations are
independent Gaussians; conversely the iid-packet simulator generates their
joint transcript law. A latent full dense root can be included on a proof
probability space with this law. Its entries are neither formed nor stored
by the simulator. The scalar-noise and finite-arithmetic comparisons are
then the separate perturbations already stated in (1) and (14).

A straightforward bounded-memory implementation of (10) stores the
\(nD\) finite packet coordinates and \(P\) numerical prefix coordinates.
For each scalar reduction it scans all packets and evaluates its row DAG
with polynomial scratch, sums dyadic numerators exactly, and forms that
scalar update. Coefficients shared by all rows may be cached. Even computing
them again at each row gives only

\[
 nP\operatorname{poly}(N,R,D,b)                         \tag{16}
\]

work. This deliberately conservative schedule does not rely on a favorable
cache layout. Once all prefixes exist, a second sequence of scans evaluates
(11) one row at a time and performs streaming selection. Its work is again
\(n\operatorname{poly}(N,R,P,D,b,\log n)\), with the selection cost (9).
There is no need to retain an \(n\)-by-\(P\) moment table. Storing all
width-\(n\) intermediate row arrays would also fit
\(n\operatorname{polylog}(n)\), but is unnecessary.

The point on which exact source sampling matters is the original Gaussian
matrix **law**. If instead the simulator were required to accept a specified
dense matrix root and reproduce its own transcript, extracting (15)'s
innovations by whitening would first require that root's matrix actions.
The direct supplied method costs \(O(Rn^2)\), in general
\(n^2\operatorname{polylog}(n)\). This note neither calls that
\(O(n^2)\) nor proves a faster algorithm for the specified-root task.

### Finite Gaussian marks have a counted coupling

For clarity, Gaussian sampling need not hide an unbounded rejection loop
in (16). Let \(M=nD+P\) be the number of coordinates needed. Pair them
using independent uniforms \(U,V\) and the Box--Muller map

\[
 (G_1,G_2)=\sqrt{-2\log U}\,(
        \cos(2\pi V),\sin(2\pi V)).                    \tag{17}
\]

Polar change of variables gives the joint density
\((2\pi)^{-1}\exp[-(G_1^2+G_2^2)/2]\), so the ideal coordinates
are independent standard normals. Choose a dyadic
\(0<\rho\le\delta_0/(4(M+1))\), within a factor of two of that
bound. The probability any radial uniform is below \(\rho\) is at
most \(M\rho\le\delta_0/4\).

Replace each uniform by the midpoint of its \(t\)-bit dyadic cell.
On \(U\ge\rho\), if \(2^{-t}\le\rho/2\), both radial arguments
are at least \(\rho/2\). The logarithm mean-value bound and
\(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\) give coordinate error at most

\[
 C\sqrt{2^{-t}/\rho}
      +C\sqrt{\log(2/\rho)}\,2^{-t}.                    \tag{18}
\]

Thus \(t=O(\log(1/\rho)+\log(1/\kappa))\), with a sufficiently
large constant, and scalar arithmetic to error \(O(\kappa)\) give the
required coupling. This uses a fixed number of bits and a fixed bounded
computation per coordinate, including off the good event.

The elementary scalar functions in (17) have polynomial-time rational
approximations at these arguments: scale the logarithm argument to
\([1,2]\) and use
\(\log x=2\sum_{j\ge0}((x-1)/(x+1))^{2j+1}/(2j+1)\), whose ratio
is at most \(1/9\); use the factorial Taylor remainder for sine/cosine
on a bounded interval and a scalar square-root routine. If needed,
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) has geometrically convergent
arctangent series. Hence these elementary routines do not introduce a
superpolynomial random-number generation cost. Since
\(\log M+\log(1/\delta_0)+\log(1/\kappa)\) is polylogarithmic for
the chosen fixed confidence and precisions, generating all finite marks
costs \(n\operatorname{polylog}(n)\) bits of work and storage.

## 5. End-to-end acquisition counts and deletion boundary

Combining (3), (9), (14), and (16), there is an absolute integer \(k\)
such that this initialization uses

\[
 W_{\rm init}\le C n\ell_n^k,
 \qquad S_{\rm init}\le C n\ell_n^k.                    \tag{19}
\]

The second bound is **temporary initialization space**, not the retained
or query-space claim. Both include packet generation, full finite-source
execution, reconstruction of the dyadic moment vectors, selection,
rational arithmetic and numerical small-matrix functions. All precision
and counter bits are counted. The arithmetic/activation and bit-time
qualification in Section 1 still applies.

At completion retain only the selected \(q\le P+1\) finite packets,
their exact weights, the scalar-noise marks, fixed instructions, and the
current acquired prefix. Discard the remaining \(nD\) source coordinates,
the preprocessing prefix tape, and every temporary row array and point
vector. A current prefix can then be reacquired causally through (12), or
started at the designated initial clock state. The retained components have
size bounded by

\[
 O\!\left((P+1)D b_Z+P b_E+P b_C+
 (P+1)^2[\beta+\log(en)+\log(P+2)]
       +\text{instruction bits}\right),                \tag{20}
\]

where \(b_Z,b_E,b_C\) are the counted stored precisions. This is
absolute-polylogarithmic. Source-dependent selected packets are not iid,
and no iid claim about them is used.

At each compact update evaluate the \(q\) row DAGs one at a time, caching
one DAG's nodes to avoid repeated subgraph expansion. Its peak scratch and
work are polynomial in the same compact parameters. Exact rational weighted
sums are polynomial-sized by Section 3. All \(P\) acquisition updates,
excluding query-law calibration, therefore have total
\(C\ell_n^k\) work and peak space after increasing the same absolute
exponent. The weighted panel and private noises are not passed to a
posterior decoder as conditioning observations; that decoder still receives
only the present retained summary and its allowed compiled coefficients.

For fixed \(k\), \(\ell_n^k/n\to0\), so (19) is eventually
\(O(n^2)\). The sufficient width may depend on all fixed problem
parameters. Neither a practical threshold nor an optimized exponent is
claimed. A requirement of polylogarithmic **initialization** workspace
would be stronger than (19) and is not settled here.

## 6. Fidelity and probability quantifiers for an independent virtual source

Write \(f_n^{\rm ref}\) for the requested reference trajectory, with
its original Gaussian initialization, and let \(f_n^{\rm vir}\) denote
a fresh trajectory with the identical architecture, dynamics, and Gaussian
root law. Its finite training source is sampled by Sections 1--4, independently
of the reference root. Independence of source innovations does not freeze
features or change the underlying trained dense model. The physical bridge
still compares its finite program to \(f_n^{\rm vir}\) under exactly the
inherited nonlinear assumptions.

For a trajectory \(f\), use the metric

\[
 \|f\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)|.    \tag{21}
\]

The supplied dense-pair upper certificate says, at a chosen failure share
\(\gamma\), that independent dense trajectories obey

\[
 \mathbb P\{\|f_n-f'_n\|_*>b_n(\gamma)\}\le\gamma.     \tag{22}
\]

Average this failure probability over the second trajectory. There is a
fixed trajectory \(f_{*,n}\), chosen only for the proof, with

\[
 \mathbb P\{\|f_n-f_{*,n}\|_*>b_n(\gamma)\}\le\gamma. \tag{23}
\]

No approximation algorithm stores or evaluates \(f_{*,n}\). This is the
same deterministic proof-center step used by the dense-budget assembly.
It applies to any independent fresh source with the original dense law.

The assembly's prefix argument proves its decoder-to-center estimate
before comparing to the actual dense reference: on its source, posterior,
and numerical good event,

\[
 \|f_C-f_{*,n}\|_*
 \le b_n(\gamma)+C\ell_n^{C_L}/\sqrt n.                 \tag{24}
\]

Here \(C_L\) is the inherited depth-dependent **error** exponent. This
note does not reprove the decoder or improve its calibration cost; (24)
is an explicit downstream interface that any replacement calibration must
retain. The finite-source prefix supplied to that proof is preserved by
(13)--(14), with the same parameterwise numerical-prefix tolerance.

Combining (23) for \(f_n^{\rm ref}\) with (24), and allocating
\(\gamma\), source, sampler and numerical failure shares with total at
most \(\delta\), yields

\[
 \mathbb P\!\left\{
 \|f_C-f_n^{\rm ref}\|_*
 \le 2b_n(\gamma)+C\ell_n^{C_L}/\sqrt n
 \right\}\ge1-\delta.                                 \tag{25}
\]

The probability is jointly over the original reference Gaussian root and
the independent simulator/numerical seeds, at every sufficiently large
individual width. More explicitly, for every reference root in the set
in (23), the source success probability is the same lower bound as in
(24), because its randomness is independent of that reference. There is
no assertion for every prescribed reference root, no guarantee conditional
on arbitrary exceptional dense weights, and no common event across all
widths. The one event in (25) covers all input points, physical times, and
the fitted endpoint just as in the downstream decoder theorem.

Using the deterministic center directly avoids adding a third certificate
radius for a reference-to-virtual triangle. If only a compact-to-virtual
bound were available, such a triangle would still preserve the certificate
scale but would generally enlarge the constant. For fixed nonzero labels,
the inherited positive factor \(\exp(CY^2\sqrt{\ell_n})\),
\(Y=\|y\|_2/\sqrt m\), in \(b_n\) eventually dominates the logarithmic
root-width remainder, giving the same factor-three form as the supplied
dense-budget result. Zero labels use the exact zero predictor.

## 7. Exact scope of the improvement

The exhaustive support search in the finite-precision selection note is
unnecessary: the streaming algorithm proves polynomial bit cost per row,
bounded support at every stage, and a uniform description bound throughout
the run. The finite physical source can be generated at the original
Gaussian dense law in \(n\operatorname{polylog}(n)\) work without
materializing dense hidden matrices. This is enough for the independent-dense
upper-certificate contract; it does not establish fast compression of a
specific supplied root. The private finite panel preserves the implemented
source history exactly and the ideal source history to its assigned accuracy.

Three boundaries remain explicit. Efficient recalibration is not proved by
this file. The fast-small-matrix and full source/decoder bridges are inherited
author results in the allowed inputs rather than fresh independent reviews
here. Finally, unrestricted polynomial bit-time cannot be deduced from
analytic activation assumptions alone; it requires the stated polynomial-time
precision interface, while the original arithmetic/activation-primitive work
comparison remains valid without that stronger computational assumption.
