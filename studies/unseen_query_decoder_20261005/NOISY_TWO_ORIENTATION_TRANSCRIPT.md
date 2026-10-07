# An exact noisy two-orientation Gaussian row program

2026-10-06. Scoped continuation in the unseen-query decoder study.
Internal finite-program theorem; no experiments or promotion.

Adding independent Gaussian noise of variance \(\sigma^2\) to each
initialized-matrix answer makes an exact finite row-law construction
possible without inverses of history Grams. The posterior precision is
a positive Sylvester operator. Its conditional answer covariance is a
scalar matrix plus a correction on the old opposite-orientation query
span, with a positive floor \(\sigma^2 I\). Both its mean and its
square root can be computed from small scalar-moment matrices using
only explicitly gapped inverses and a gapped square root.

The representation below is the **exact finite-width law of the noisy
program**, not a replacement of empirical coefficients by population
moments. In particular, poor conditioning of an empirical history Gram
does not cause a statistical law-comparison error in this result.

## Scope and provenance

The supervisor explicitly proposed noisy Gaussian conditioning as the
next bounded route in this study. This proof uses the same source and
process scope as `EXACT_TRANSCRIPT_UNIFORM_LAW.md` and
`FINITE_TRANSCRIPT_WEIGHTED_REPLAY.md`. Those files and the earlier two
notes are not modified here. The required custom notation skill remains
inaccessible; the supplied conventions and already read maintained
notation contract are applied. No external posterior or matrix-function
theorem is used without the needed derivation below.

This file does not itself construct a finite approximation of the whole
physical training trajectory, or an all-time late-query decoder. It
provides a finite-width scalar row-interaction representation for any
finite predictable program with the stated noisy oracle.

## 1. The noisy observable program and its filtration

Let \(M_1,\ldots,M_b\) be independent standard Gaussian
\(n\times n\) matrices and \(W_\ell=M_\ell/\sqrt n\). Fix

\[
 0<\sigma\le1,\qquad \delta=\sigma^2.                         \tag{1}
\]

The program observes initialized actions through

\[
 y=W_\ell v+\sigma\xi
 \quad\text{or}\quad
 x=W_\ell^Tu+\sigma\zeta,                                    \tag{2}
\]

where every new \(\xi,\zeta\sim N(0,I_n)\) is independent of
all prior randomness. The next label, orientation, and query are
measurable with respect to the external initial field and earlier
**observed answers**. The external field is independent of the
initialized matrices and all oracle noises.

The raw noise vectors in (2) are hidden from this observable
filtration. Revealing them separately would turn (2) back into an
exact matrix reveal and invalidate the posterior formulas below.
Their use as preprocessing inputs to an independently analyzed
compact reexecution is a different matter; it does not enlarge the
filtration used in this law proof.

For one matrix, write the previous forward and reverse observations as

\[
 Y=WV+\sigma\Xi,\qquad X=W^TU+\sigma Z,                       \tag{3}
\]

where \(V\in\mathbb R^{n\times r}\),
\(U\in\mathbb R^{n\times s}\), and all columns are past
queries. Given the observable past they and \(Y,X\) are fixed.
Set

\[
 Q=V^TV/n,\quad K=U^TU/n,\quad
 H=U^TY/n,\quad J=X^TV/n.                                    \tag{4}
\]

Both \(H\) and \(J\) have size \(s\times r\). Unlike the
noiseless case, they need not be equal. Empty blocks are omitted.

## 2. Posterior precision and conditional independence

For fixed observed history, its likelihood as a function of \(M\) is
proportional to

\[
 \exp\left[-\frac1{2\delta}
    \left(\|Y-MV/\sqrt n\|_F^2+
          \|X-M^TU/\sqrt n\|_F^2\right)\right].               \tag{5}
\]

This remains true for predictable adaptive queries. Indeed, the joint
conditional density of the answers given \(M\) factors in chronological
order into their independent-noise conditional densities; in each factor
the query is the fixed function of the already observed prefix. No
derivative of that query appears in a likelihood density.

Multiplying (5) by the standard Gaussian prior density and completing
the quadratic form shows that the posterior precision on a matrix
perturbation \(B\) is

\[
 \mathcal P(B)
   =B+\frac1{n\delta}(UU^TB+BVV^T).                           \tag{6}
\]

It is self-adjoint and satisfies
\(\langle B,\mathcal P(B)\rangle_F\ge\|B\|_F^2\).
In terms of \(W\), put

\[
 A=UU^T/n,\qquad B_0=VV^T/n.
\]

Its posterior mean \(\overline W\) is the unique solution of

\[
 \delta\overline W+A\overline W+\overline W B_0
       =(YV^T+UX^T)/n.                                      \tag{7}
\]

The posterior covariance operator of \(W\) is

\[
 \frac\delta n\,
       (\delta I+\mathcal L_A+\mathcal R_{B_0})^{-1},           \tag{8}
\]

where \(\mathcal L_A(B)=AB\) and
\(\mathcal R_{B_0}(B)=BB_0\). The operator in (8) has all
eigenvalues at least \(\delta\) before inversion.

With multiple matrix labels, the likelihood groups into factors, one
for each matrix, after the entire observed history is fixed. The
prior also factors. Thus the posterior matrices are conditionally
independent, even though queries to different labels were adaptively
interlaced. These calculations prove the conditional kernels needed
for a chronological exact simulation.

## 3. The mean is a small-matrix computation

Define

\[
 C=(\delta I_r+Q)^{-1},\qquad D=(\delta I_s+K)^{-1},             \tag{9}
\]

and let \(E\in\mathbb R^{s\times r}\) solve

\[
 (\delta I_s+K)E+EQ=-HC-DJ.                                  \tag{10}
\]

The Sylvester map on the left has eigenvalues
\(\delta+\lambda_i(K)+\lambda_j(Q)\ge\delta\), so it is
invertible, including at singular \(K,Q\). An exact expression for
the posterior mean is

\[
 \overline W=YCV^T/n+UDX^T/n+UEV^T/n.                        \tag{11}
\]

To verify it, apply the left side of (7) to the first term. The
result is

\[
 YV^T/n+UHC V^T/n.
\]

For the second term it is
\(UX^T/n+UDJ V^T/n\), and for the third it is
\(U[(\delta I+K)E+EQ]V^T/n\). Equation (10) cancels the two
extra terms. Uniqueness in (7) proves (11).

For a new forward argument \(q\), write

\[
 v=V^Tq/n,\qquad x=X^Tq/n.                                   \tag{12}
\]

Then

\[
 \overline Wq=Y(Cv)+U(Dx+Ev).                                \tag{13}
\]

For a new reverse argument \(c\), write
\(u=U^Tc/n\) and \(y=Y^Tc/n\). The corresponding expression is

\[
 \overline W^Tc=V(Cy+E^Tu)+X(Du).                            \tag{14}
\]

These are shared-scalar-coefficient combinations of previous row
fields. No inverse of \(Q\) or \(K\) appears.

## 4. Conditional covariance of a new forward answer

For the forward argument \(q\), put

\[
 d=\|q\|_2^2/n,
 \qquad f(a)=\frac\delta{\delta+a}
       \left[d-v^T((\delta+a)I_r+Q)^{-1}v\right],
 \quad a\ge0.                                                \tag{15}
\]

The new observed answer \(Wq+\sigma\xi\), conditional on the old
past, is Gaussian with mean (13) and covariance

\[
 \Gamma_q=\delta I_n+f(A),\qquad A=UU^T/n.                    \tag{16}
\]

To prove this directly, diagonalize the two real symmetric matrices
\(A\) and \(B_0\). In their product orthonormal basis, (8) says
that different entries of the posterior centered \(W\) are
independent and have variances

\[
 \frac\delta{n(\delta+a_i+b_j)}.
\]

The variance of their action on \(q\) in the target eigendirection
with eigenvalue \(a_i\) is therefore

\[
 \frac\delta n q^T((\delta+a_i)I_n+B_0)^{-1}q.                \tag{17}
\]

The identity

\[
 (cI_n+VV^T/n)^{-1}
  =\frac1c\left[I_n-
        \frac1nV(cI_r+Q)^{-1}V^T\right],\qquad c>0,            \tag{18}
\]

follows by multiplication, and turns (17) into (15). The additional
independent answer noise supplies \(\delta I_n\), proving (16).

This also gives useful exact inequalities:

\[
 0\le f(a)\le d,
 \qquad -d/\delta\le f'(a)\le0,
 \qquad \Gamma_q\succeq\delta I_n.                           \tag{19}
\]

For the derivative bound, differentiate (17); its absolute value is
at most \(\delta d/(\delta+a)^2\le d/\delta\). These bounds
require no lower eigenvalue of \(Q\), \(K\), or an augmented history
Gram. They use only their genuine Gram origin.

The covariance of a new reverse answer is obtained by exchanging

\[
 (U,K,A)\longleftrightarrow(V,Q,B_0),\qquad q\longleftrightarrow c.
                                                               \tag{20}
\]

The old noisy answer fields \(X,Y\) influence the posterior mean,
but not the posterior covariance after the query vectors are fixed.

## 5. An exact low-rank square root without a Gram inverse

Set

\[
 f_0=f(0)=d-v^TCv,\qquad \beta=\delta+f_0.                    \tag{21}
\]

The nonconstant part of \(f(A)\) is supported on
\(\operatorname{span}(U)\). For \(a\ge0\), define

\[
 h(a)=\frac{-f_0+
          \delta v^TC((\delta+a)I_r+Q)^{-1}v}{\delta+a}.
                                                               \tag{22}
\]

A resolvent subtraction proves, including at \(a=0\) by continuity,

\[
 ah(a)=f(a)-f_0.                                              \tag{23}
\]

In particular, this is a rational formula for the divided difference;
there is no division by the possibly zero eigenvalue \(a\). Define

\[
 T(a)=\frac{h(a)}{\sqrt{\delta+f(a)}+\sqrt\beta}.               \tag{24}
\]

The denominator is at least \(2\sigma\). With ordinary spectral
functions of the small matrix \(K\), an exact positive square root is

\[
 \Gamma_q^{1/2}
   =\sqrt\beta I_n+\frac1nU T(K)U^T.                         \tag{25}
\]

Indeed, for a nonzero singular direction of \(U/\sqrt n\) with
squared singular value \(a\), (23)--(24) imply

\[
 \sqrt\beta+aT(a)=\sqrt{\delta+f(a)}.
\]

On the orthogonal complement of \(\operatorname{span}(U)\),
both sides of (25) equal \(\sqrt\beta\). All eigenvalues are
positive and squaring gives (16), proving (25). This argument is
valid at arbitrary rank deficiency of \(U\).

### 5.1 Computing \(f(K)\) and \(h(K)\) using only gapped finite matrices

No unstable eigenvector choice or inverse Gram is necessary to define
the functions in (25). When \(r,s>0\), let

\[
 \mathcal B=\delta I_{sr}+K\otimes I_r+I_s\otimes Q,
 \qquad R_v=I_s\otimes v,
 \qquad R_{Cv}=I_s\otimes(Cv).                                \tag{26}
\]

Here \(R_v,R_{Cv}\) are \(sr\times s\) matrices. Define

\[
 B_1=R_v^T\mathcal B^{-1}R_v,\qquad
 B_2=R_{Cv}^T\mathcal B^{-1}R_v.                              \tag{27}
\]

Both are symmetric functions of \(K\); this follows by diagonalizing
only \(K\), after which their diagonal entries are respectively
\(v^T((\delta+a)I+Q)^{-1}v\) and
\(v^TC((\delta+a)I+Q)^{-1}v\). Thus

\[
 F:=f(K)=\delta(\delta I_s+K)^{-1}(dI_s-B_1),
 \qquad
 H_f:=h(K)=(\delta I_s+K)^{-1}(-f_0I_s+\delta B_2).             \tag{28}
\]

Finally,

\[
 T(K)=H_f\left[(\delta I_s+F)^{1/2}
                                  +\sqrt\beta I_s\right]^{-1}.
                                                               \tag{29}
\]

Every inverse in (9)--(10), (26)--(29) has a gap at least
\(\delta\), except the final inverse, whose gap is at least
\(2\sigma\). The matrix under the square root has gap
\(\delta\). Dimensions are at most \(sr\le R^2\).
If \(r=0\), use the direct formulas
\(f(a)=\delta d/(\delta+a)\),
\(h(a)=-d/(\delta+a)\). If \(s=0\), the correction in (25)
is absent. These conventions cover the first call as well.

### 5.2 Exact coordinate form and independent innovations

Let \(g\sim N(0,I_n)\) be fresh, independent of the past, and put

\[
 t=U^Tg/n.
\]

The new forward observation has the exact conditional representation

\[
 y=Y(Cv)+U(Dx+Ev+T(K)t)+\sqrt\beta\,g.                       \tag{30}
\]

All coefficients in (30) are scalar functions of small empirical
moment matrices and of the new moment \(t\). The reverse formula
uses (14) and the exchange (20). Thus both orientations admit the
same type of rowwise expression.

Alternatively, on the original noisy probability space define

\[
 g=\Gamma_q^{-1/2}(y-\overline Wq).                          \tag{31}
\]

Because \(\Gamma_q\succeq\delta I\), this is well defined.
Conditionally on the observable past, \(g\) is standard Gaussian,
independent of that past. Induction shows that the full vectors \(g\)
over all calls and labels are jointly independent standard Gaussian
vectors, and independent of the initial external row packets. This
proves a common coupling with the original noisy program, not merely
a list of conditional marginals.

The inverse square root in (31) also has a small-rank row formula: use

\[
 \Gamma_q^{-1/2}
 =\beta^{-1/2}I_n+\frac1nU\widetilde T(K)U^T,
\]

where

\[
 \widetilde T(a)
   =-\frac{h(a)}{
       \sqrt\beta\sqrt{\delta+f(a)}
       [\sqrt\beta+\sqrt{\delta+f(a)}]}.
                                                               \tag{32}
\]

This follows by rationalizing the divided difference of the inverse
square root; again no division by \(a\) occurs.

## 6. Exact finite-width row-interaction theorem

Suppose the observable program has at most \(R\) noisy calls, a
finite coordinatewise instruction graph, and scalar operations
depending only on previously formed scalar empirical averages.
Assume its initial fields are coordinate functions of iid packets
\(\xi_i\), with optional deterministic marks \(t_i\).

Then there are iid augmented packets

\[
 Z_i=(\xi_i,g_{1,i},\ldots,g_{R,i}),\qquad 1\le i\le n,         \tag{33}
\]

such that the program's exact finite-width joint law is generated by
the following finite scalar/row procedure:

* coordinatewise arithmetic and prescribed activation operations;
* scalar empirical averages of functions of the packets;
* small-matrix scalar operations (9)--(10), (26)--(29);
* affine row combinations (30), and their reverse counterparts.

No initialized \(n\times n\) matrix remains in this representation.
For a program with \(S\) named row nodes, retaining all scalar
pair moments uses \(O(S^2)\) scalars; the number and dimensions of
new Gaussian coordinates per row are \(O(R)\). All scalar arithmetic
required at a call acts on matrices of dimension at most \(R^2\).
The resulting scalar instruction count is polynomial in \(S,R\)
apart from the chosen accuracy and implementation of small matrix
functions. The exact mathematical representation is finite even when
some empirical moment matrices are singular.

**Proof.** Use (30) chronologically and the conditional-independence
statement of Section 2. Every new row output is a fixed coordinate
function of previous row nodes, shared scalar moment nodes, and one
new independent Gaussian component. Subsequent coordinatewise
operations and empirical reductions have the required form. The
construction (31) proves equality of joint laws with the original
noisy program. \(\square\)

There is no assertion that rows are independent conditional on the
realized scalar moments. The theorem describes a finite interacting
row program driven by iid packets. An expectation method that handles
its empirical-average interactions can use this exact representation
without invoking a mean-field approximation.

## 7. Quantitative size, sensitivity, and off-domain extensions

### 7.1 Bounds on the genuine moment domain

Suppose all relevant query and old-answer fields have RMS at most
\(B\ge1\), and a fresh \(g\) has RMS at most \(G\ge1\).
All entries of \(Q,K,H,J\) are then at most \(B^2\) in absolute
value, and

\[
 \|Q\|,\|K\|\le RB^2,
 \quad \|H\|_F,\|J\|_F\le RB^2,
 \quad \|v\|,\|x\|\le\sqrt R B^2.                           \tag{34}
\]

Equations (9)--(10) imply

\[
 \|C\|,\|D\|\le\delta^{-1},\qquad
 \|E\|_F\le2RB^2\delta^{-2}.                                \tag{35}
\]

The scalar-covariance bounds give

\[
 0\le f_0\le B^2,\quad 0\preceq F\preceq B^2I_s,
 \quad \|H_f\|\le B^2/\delta,
 \quad \|T(K)\|\le B^2/(2\sigma^3),
 \quad \|t\|\le\sqrt R BG.                                  \tag{36}
\]

Hence every coefficient in (30) is bounded by a fixed polynomial in

\[
 R+1,\quad B+1,\quad G+1,\quad 1/\sigma.                    \tag{37}
\]

The degree of this polynomial is absolute for one call, not proportional
to the history length. For example, the mean coefficient norms are
bounded by
\(\sqrt R B^2/\delta\) and
\(\sqrt R B^2/\delta+2R^{3/2}B^4/\delta^2\), and the extra
innovation coefficient has norm at most
\(\sqrt R B^3G/(2\sigma^3)\).

### 7.2 Small-matrix operations have explicit polynomial sensitivity

For positive matrices \(A,B\succeq aI\),

\[
 \|A^{-1}-B^{-1}\|_F\le a^{-2}\|A-B\|_F.                    \tag{38}
\]

This is the resolvent identity. Also,

\[
 \|A^{1/2}-B^{1/2}\|_F
       \le(2\sqrt a)^{-1}\|A-B\|_F.                         \tag{39}
\]

For (39), set \(X=A^{1/2}-B^{1/2}\). Then
\(A^{1/2}X+XB^{1/2}=A-B\). Diagonalizing the two positive
coefficients on the left separately shows that its inverse on
Frobenius space has norm at most \((2\sqrt a)^{-1}\).
The same argument controls the Sylvester solve (10), and subtracting
two such equations adds only the product of the coefficient-matrix
difference and the bounded solution.

Apply these estimates to the explicit formulas (9)--(10) and
(26)--(29). Tensoring by an identity changes Frobenius bounds by
at most a factor \(\sqrt R\); sums and products obey their usual
norm product bounds. The data and inverse bounds are (34)--(36).
There is a fixed finite number of these operations in one call.
Consequently their joint output coefficients are Lipschitz in the
input moment entries with a bound

\[
 L_{\rm call}\le (C(R+1)(B+G+1)(1+\sigma^{-1}))^{C},           \tag{40}
\]

for an absolute exponent \(C\). Enlarging \(C\) includes the
reverse call and the entrywise-to-Frobenius norm conversions. This
claim follows from the displayed operations, not from eigenvector
continuity or a smallest empirical Gram eigenvalue.

Across a finite scalar/row instruction graph of polynomial size in
\(S,R\), with explicitly bounded intermediate amplitudes and
primitive Lipschitz constants, repeated product-rule estimates give
overall sensitivity

\[
 \exp\!\left[\operatorname{poly}
       (S,R,\log(B+G+1),\log(1/\sigma))\right].               \tag{41}
\]

Thus exponentially small in a sufficiently high power of \(\log n\)
oracle noise or arithmetic error can absorb such amplification when
all displayed arguments are polylogarithmic. This is an accuracy-budget
statement; it does not by itself prove the requisite physical-trajectory
finite-program comparison.

### 7.3 A global extension off the moment manifold

An expectation or smoothing method may evaluate scalar instructions
at inconsistent moment arrays. The covariance formula must remain
defined there. One explicit extension is as follows.

For each layer collect every scalar moment used by the current call
as entries of a real symmetric candidate Gram matrix of its named
fields. Symmetrize this matrix, project onto the positive-semidefinite
cone, and cap its Frobenius norm by projection onto a fixed ball in
that cone. The original moment matrix is unchanged whenever it is
positive semidefinite and lies within the cap. These two projections
are nonexpansive in Frobenius norm. To see this for any closed convex
set, its Euclidean metric projection \(P\) satisfies
\(\langle x-Px,z-Px\rangle\le0\) for every point \(z\) in the
set. Apply this once with \(z=Py\), once with \(z=Px\), and add;
then \(\|Px-Py\|^2\le\langle Px-Py,x-y\rangle\).
The required projections exist by finite-dimensional compactness
after restricting the minimization to a sufficiently large ball.

Use the resulting principal blocks for \(K,Q\), and for the
augmented Gram

\[
 \begin{pmatrix}Q&v\\v^T&d\end{pmatrix}\succeq0.              \tag{42}
\]

Every positive semidefinite block (42) is the Gram of some finite
vectors: diagonalize it and take its positive square root. Applying
(17)--(19) to that realization proves \(f(a)\ge0\) for all
\(a\ge0\), with no consistency assumptions beyond (42).
Thus \(f_0,F\) remain nonnegative, all inverse gaps in Sections
3--5 remain valid, and (40) remains a polynomial bound on the capped
extended domain. Cross blocks \(H,J,x\) are supplied by the same
capped layer Grams. No noisy equality \(H=J\) is imposed.

One may additionally project the computed \(F\) onto the positive
semidefinite cone to accommodate arithmetic roundoff; this is the
identity in exact arithmetic. The square roots and inverses are then
still explicitly gapped. Coordinate root and intermediate row caps
can be added separately. Agreement with the original noisy program
on the stated good event must be verified for every such cap; it is
not inferred just from the availability of a global extension.

## 8. Coupling the noisy oracle to its noiseless finite program

Run the original and noisy finite programs with the same initialized
matrices and initial fields, adding the independent noise vectors
only in (2). If every one of the \(R\) noises has RMS at most \(G\),
each oracle call adds an RMS perturbation at most \(\sigma G\).
The Gaussian-coordinate union bound, or the direct Gaussian norm
bound, supplies such an event with explicit chosen probability.

If the finite program has a proved perturbation amplification
\(A_{\rm prog}\) for these per-call errors, the resulting output
or named-state error is at most

\[
 R A_{\rm prog}\sigma G.                                    \tag{43}
\]

This is just the deterministic telescoping comparison through the
finite instruction graph. For
\(\log A_{\rm prog}+\log G+R=\operatorname{polylog}(n)\), an
appropriate choice \(\sigma=\exp[-\log(n)^C]\) makes (43)
smaller than the desired inverse-polynomial accuracy, while
\(\log(1/\sigma)\) remains polylogarithmic in all representation
and sensitivity bounds above.

Equation (43) must be applied to a genuinely proved finite causal
approximation of the physical flow. It is not a claim that arbitrary
deep nonlinear programs have harmless noise sensitivity.

## 9. What this settles and what remains outside the theorem

The theorem supplies an exact finite-width, both-orientation,
adaptive Gaussian row-interaction law with no empirical Gram gap.
All small conditional calculations have explicit positive gaps
controlled solely by the deliberately added noise level. Hence a
method for evaluating expectations of finite empirical-average
programs can target this exact law; no population fixed point or
growing-program mean-field theorem is required at this stage.

The note does not establish that such an expectation evaluator has
polylogarithmic peak workspace. It does not establish a finite
causal approximation covering the entire physical trajectory and its
fitted endpoint, nor the whole-sphere decoder modulus. Those are
separate tasks. It also does not reinterpret the hidden raw oracle
noises as observed data in the Gaussian-conditioning proof.

Subject to those distinctions, the earlier exact-conditioning
degeneracy is removed at the finite-program representation level:
every needed inverse now has a specified \(\sigma\)-dependent gap,
and the exact finite-width distribution is retained.
