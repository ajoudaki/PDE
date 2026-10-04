# Dimension-free representations: a source-space obstruction and a symmetry route

2026-10-04. Scoped independent theory route. **Candidate result, internally
derived; not independently checked or promoted.** The candidate was frozen
in this file before exchanging scientific conclusions with the coordinator
or reading another current route. No experiment, Git operation, or maintained
manuscript change was performed.

The complete assigned inputs were SAMPLE_COUNT_REFINEMENT.md,
GENERAL_ANALYTIC_COMPRESSION.md, STORAGE_QUADRATIC_IMPROVEMENT.md,
GENERAL_WEIGHTED_COMPARISON.md, and WHOLE_QUERY_RESPONSE_SOURCE.md.
The canonical-notation skill and neural-network reference, rigorous-solution
skill, and conjecture-investigation skill and its contract, adversarial,
and proof-search references were read. No other study was accessed.

The result is twofold. First, a polynomial logarithmic source dimension with
an exponent independent of input dimension is impossible for the existing
whole-feature linear-space interface, already at Gaussian initialization
with sine activation. This is a limitation of that interface, not a lower
bound for arbitrary autonomous networks. Second, exact conditioning on the
training input span provides a possible way around the interface: unused
input directions enter through independent Gaussian first-layer weights.
There is a dimension-reduced conditional mean and a root-width pointwise
fluctuation estimate. Uniform fluctuations and a small autonomous realization
of that conditional mean remain unproved.

## 1. Contract and notation

Let the fixed input dimension be d>=2, hidden depth L>=2, sample count m,
and normalized training vectors v_a=x_a/sqrt(d) in S^{d-1}. The actual
width-n reference has

\[
 z^{(1)}(t,v)=A(t)v,\quad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad
 z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\ (\ell\ge2),\qquad
 f_n(t,v)=w(t)^\top h^{(L)}(t,v)/n.
\]

The entries of A(0) are independent N(0,1), those of W^(ell)(0) are
independent N(0,1/n), all initialized blocks are independent, and w(0)=0.
The activations are bounded and holomorphic on a fixed horizontal strip
and real on the real axis. For residuals c_a=y_a-f_n(t,v_a), backward
signals k_a^(L)=w, delta_a^(ell)=phi_ell'(z_a^(ell)) multiplied
coordinatewise by k_a^(ell), and
k_a^(ell)=W^(ell+1) transpose times delta_a^(ell+1), the exact flow is

\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=\frac2{mn}\sum_a
 c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=\frac2m\sum_a c_ah_a^{(L)}.
 \tag{1}
\]

Write Y=||y||_2/sqrt(m), gamma for the positive initialized limiting top
Gram gap, lambda=min(1,gamma/m), and ell_n=log(en). The inherited label
regime is Y<=c lambda. The target is an initialization-only smaller
autonomous network satisfying, at each fixed confidence and all sufficiently
large widths,

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_C(t,v)-f_n(t,v)|\le C_{\rm data}n^{-1/2}.
 \tag{2}
\]

Every retained fixed and moving real coordinate counts. Setup may use
arbitrarily expensive finite exact-real calculations from initialization
and labels, but no trained-path query. The smaller network must generate
its own residuals and trained hidden features. A precomputed output table,
an external mean-field solution, or an unevaluated conditional expectation
is not a completed construction.

The current sufficient source interface approximates, in a common linear
subspace S_ell of R^n, every vector h^(ell)(t,v), its paired initialized
matrix image, the training backward responses, and their paired reverse
images. Its coordinate error is epsilon_n=n^-1. Current total storage
is O(lambda^-2 ell_n^[2(d(L+5)+1)]) by sampling O(dim S_ell) neurons and
retaining the resulting dense matrices and metrics.

## 2. A lower bound for the whole-feature source interface

Here only phi_1(s)=sin(s) is needed. It belongs to the allowed activation
class since |sin(x+iy)|<=cosh(b) on |y|<=b. Let g_1,...,g_n be the
independent Gaussian rows of A(0), and put

\[
 h_n(v)=(\sin(g_1^\top v),\ldots,\sin(g_n^\top v))^\top.
\]

For each fixed d, with probability tending to one, every possibly
initialization-dependent subspace S contained in R^n satisfying

\[
 \sup_{v\in S^{d-1}}\inf_{s\in S}
 \frac{\|h_n(v)-s\|_2}{\sqrt n}\le\epsilon_n,
 \qquad \epsilon_n\le C n^{-1/2},
 \tag{3}
\]

has

\[
 \dim S\ge c_d
 \left(\frac{\log n}{\log\log(en)}\right)^{d-1}.
 \tag{4}
\]

The constant C in (3) is fixed independently of n. In particular, the
coordinate-supremum n^-1 interface satisfies (3). The probability event
below is simultaneous over all S; selection bias or dependence of S on
other initialized matrices does not evade the result.

### 2.1 The initialized covariance and a harmonic lower bound

Let sigma be probability surface measure on S^{d-1}. Gaussian integration
of the two cosine terms in sin(a)sin(b) gives

\[
 K(v,u):=\mathbb E[\sin(g^\top v)\sin(g^\top u)]
 =e^{-1}\sinh(v^\top u)
 =e^{-1}\sum_{j\ge1,\ j\ {\rm odd}}\frac{(v^\top u)^j}{j!}.
 \tag{5}
\]

Each kernel (v^T u)^j is positive semidefinite: its quadratic form is
the squared norm of the integral of v^{\otimes j} against the tested
function. Thus every term in (5) has a nonnegative quadratic form.

Let H_j be the space of restrictions to the sphere of real harmonic
homogeneous polynomials of degree j. For p in H_j,

\[
 \int_{S^{d-1}}(v^\top u)^j p(u)\,d\sigma(u)
 =\frac{j!}{d(d+2)\cdots(d+2j-2)}p(v).
 \tag{6}
\]

To verify (6), write p(x)=T[x,...,x] with a symmetric trace-free order-j
tensor T. For a standard Gaussian vector G, Wick expansion of
E[(v^T G)^j p(G)] leaves only pairings joining each tensor index to one
of the j factors v^T G: any pairing between two tensor indices is a trace
of T and vanishes. There are j! surviving pairings, giving j!p(v).
In polar coordinates G=RU, U has law sigma and is independent of R;
E[R^{2j}]=d(d+2)...(d+2j-2), from integration of the radial Gaussian
density. Dividing gives (6).

For clarity, the orthogonality used here can also be checked by Gaussian
pairings. Homogeneous harmonic polynomials of different degrees are
orthogonal on the sphere: in their Gaussian product, the tensor of larger
degree has two indices paired to itself and hence a vanishing trace.
Radial integration transfers this to sigma. Further, an integral operator
with kernel (v^T u)^k preserves each H_j and acts there by a scalar.
Indeed, if k=j+2s with an integer s>=0, Gaussian pairings give

\[
 \int(v^\top u)^k p(u)\,d\sigma(u)
 =\frac{k!\,|v|^{2s}p(v)}
 {2^s s!\,d(d+2)\cdots(d+k+j-2)}.
\]

The numerator counts the ways to join all j tensor indices to distinct
linear factors and then pair the remaining 2s factors. If k<j or k-j
is odd the integral is zero. Restricting |v|=1 proves the scalar action.
Consequently these operators have no
cross terms between distinct H_j, and their scalars are nonnegative by
positive semidefiniteness.

Let E_J be the direct sum of H_j over odd 1<=j<=J. Formula (6), using
the jth term of (5) on H_j, therefore gives

\[
 \langle q,Kq\rangle_{L^2(\sigma)}\ge a_J\|q\|_{L^2(\sigma)}^2
 \quad(q\in E_J),\qquad
 a_J=\frac{e^{-1}}{(d+2J)^J}.
 \tag{7}
\]

Here K also denotes its integral operator. The crude denominator in a_J
is an upper bound for the product in (6) for every odd j<=J.

The harmonic dimension is

\[
 \dim H_j={d+j-1\choose j}-{d+j-3\choose j-2}.
 \tag{8}
\]

One way to check (8) is to decompose homogeneous degree-j polynomials as
a harmonic polynomial plus |x|^2 times a homogeneous degree-(j-2)
polynomial. The decomposition follows by applying the Laplacian to
successive |x|^{2s} times homogeneous polynomials; the nonzero leading
coefficients permit back substitution. Subtraction of the two monomial
counts gives (8). For d=2 this is 2 for every j>=1. For fixed d>2 its
leading term is 2j^{d-2}/(d-2)!. Summing over odd j proves

\[
 D_J:=\dim E_J\ge c_d J^{d-1}\qquad(J\ge2).
 \tag{9}
\]

### 2.2 The empirical covariance retains these directions

Choose any real orthonormal basis Y_1,...,Y_{D_J} of E_J and define the
random coefficient vector b_i in R^{D_J} by

\[
 (b_i)_\alpha=\int\sin(g_i^\top v)Y_\alpha(v)\,d\sigma(v).
\]

Bessel's inequality gives ||b_i||_2^2<=integral sin^2<=1. Fubini's
theorem is justified by bounded sine and square-integrable finite basis
functions. Equation (7) gives
E[b_i b_i^T]>=a_J I. Independence and centering yield

\[
 \mathbb E\left\|\frac1n\sum_i
 (b_ib_i^\top-\mathbb E[b_ib_i^\top])\right\|_F^2
 \le\frac1n\mathbb E\|b_i b_i^\top\|_F^2\le\frac1n.
\]

Thus Markov's inequality and ||M||_op<=||M||_F imply

\[
 \mathbb P\left\{\frac1n\sum_i b_i b_i^\top
 \not\succeq\frac{a_J}{2}I\right\}\le\frac4{na_J^2}.
 \tag{10}
\]

Choose J=floor(log n/[8 log log(en)]). For every fixed d and sufficiently
large n, J log(d+2J)+1<=(log n)/4, so a_J>=n^-1/4. Consequently
the failure probability in (10) is at most 4n^-1/2.

Let B be the n-by-D_J matrix with ith row b_i^T and let P_S be the
Euclidean orthogonal projection onto S. Vector-valued Bessel's inequality
and (3) give

\[
 \epsilon_n^2\ge\int\frac{\|(I-P_S)h_n(v)\|_2^2}{n}\,d\sigma(v)
 \ge\frac{\|(I-P_S)B\|_F^2}{n}.
 \tag{11}
\]

On the event (10), all D_J singular values squared of B/sqrt(n) are at
least a_J/2. Projection onto a subspace of dimension R can remove at
most R singular directions. For example, diagonalize BB^T/n and use
0<=<e,P_S e><=1 and sum_e<e,P_S e>=R to obtain

\[
 \frac{\|(I-P_S)B\|_F^2}{n}\ge(D_J-R)_+\frac{a_J}{2}.
 \tag{12}
\]

If R<D_J, the right side is at least n^-1/4/2, whereas (3) bounds the
left side by C^2/n. This is impossible for sufficiently large n.
Therefore R>=D_J, and (9) proves (4).

### 2.3 Exact scope of the obstruction

The existing source interface includes t=0 and the first hidden layer,
so (4) applies regardless of subsequent depth or training. It is compatible
with the target data assumptions: take m=1, any sphere training vector,
sine at every layer, and a sufficiently small nonzero label. A nonzero
Gaussian variance has strictly positive expected sine square, so the
initialized top gap is positive at every fixed layer.

For a source-dimension upper bound C_d log^p(en) with a single exponent p
independent of d, choose any fixed d>p+1. The ratio of (4) to that upper
bound tends to infinity. Thus no such source bound can hold for the full
activation class. This does not establish the optimal exponent d-1,
nor the optimal source exponent at later layers. It also does not force
quadratic total storage for every possible representation.

The distinction from scalar output is essential. With zero initial readout,
f_n(0,v)=0 for every v, despite the first-layer rank obstruction. Even after
training, a representation may calculate the relevant scalar projections
without recovering every feature vector. No unrestricted autonomous-storage
lower bound follows from (4). Exact-real coding tricks are neither needed
for this obstruction nor offered as a compression construction.

## 3. Exact conditioning on the training input span

Let V=span{v_1,...,v_m}, k=dim V, and let P be the orthogonal projection
onto V. From (1), dot A(I-P)=0. Moreover all training forward and backward
passes, residuals, and velocities are determined by A(0)P, the initialized
hidden matrices, and the labels. They do not depend on A(0)(I-P).
Uniqueness of the finite-dimensional flow therefore implies that

\[
 A(t)=A(t)P+A(0)(I-P),
 \tag{13}
\]

and the entire collection A(t)P,W^(ell)(t),w(t) is measurable with respect
to the sigma-algebra generated by A(0)P, the initialized hidden matrices,
and the data. Denote this initialization sigma-algebra by F. This is a
proof conditioning, not permission to query the trained path in setup.

In orthonormal coordinates on V perpendicular, the matrix
G=A(0)|_{V perpendicular} has independent N(0,1) entries and is independent
of F. For v=p+u with p=Pv and u=(I-P)v, the first preactivation is

\[
 z^{(1)}(t,v)=A(t)p+Gu.
 \tag{14}
\]

Conditionally on F, Gu has the same law as ||u|| g for an n-vector g of
independent standard Gaussians. Hence the conditional mean

\[
 \bar f_n(t,p,r)=\mathbb E_G[f_n(t,p+u)\mid F],
 \qquad r=\|u\|_2,
 \tag{15}
\]

depends on u only through r. On the unit sphere, r=sqrt(1-||p||^2), so
there are at most k effective query coordinates, instead of d-1, whenever
k<d. This is an exact finite-n conditional symmetry. It uses no population
training limit and does not make the actual realized output symmetric.

For any fixed t,p,u, differentiate the finite network with respect to G,
treating the F-measurable training parameters as fixed. If delta^(1)(t,v)
is the ordinary backward query signal, the chain rule gives

\[
 \nabla_G f_n(t,v)=n^{-1}\delta^{(1)}(t,v)u^\top.
 \tag{16}
\]

On an F-measurable training-parameter event with uniformly bounded mixer
operator norms and ||w(t)||_2/sqrt(n)<=C_data, the global real derivative
bounds of the activations imply ||delta^(1)(t,v)||_2<=C_data sqrt(n)
for every G. Thus

\[
 \|\nabla_G f_n(t,v)\|_F\le C_{\rm data}r/\sqrt n.
 \tag{17}
\]

The Gaussian Poincare inequality now yields the exact conditional estimate

\[
 \mathbb E_G\left[
 |f_n(t,v)-\bar f_n(t,p,r)|^2\mid F\right]
 \le C_{\rm data}^2r^2/n.
 \tag{18}
\]

For completeness, the needed Poincare inequality is
Var(q(G))<=E||grad q(G)||^2 for a smooth real q of a standard Gaussian
vector with bounded derivative. It follows from the Gaussian averaging
semigroup P_s q(x)=E q(e^-s x+sqrt(1-e^-2s)G'): differentiating under its
Gaussian integral and integrating by parts gives
Var(q)=2 integral_0^infinity E||grad P_s q||^2 ds. The identity
grad P_s q=e^-s P_s grad q and Jensen's inequality bound this by
2 integral_0^infinity e^-2s ds E||grad q||^2. Smooth approximation gives
the same statement for Lipschitz q. In (17), q is smooth with a global
derivative bound, so these hypotheses hold.

The inherited real fitting estimates supply events of the displayed
parameter type using only the training system. For a fixed t and v,
(18) and Chebyshev's inequality give error C_data/(sqrt(eta n)) with
conditional probability at least 1-eta. No claim of a uniform version of
(18) is made.

## 4. Why the conditional symmetry is not yet a compression theorem

Two independent missing implications remain.

1. A uniform fluctuation estimate is needed:

   \[
   \sup_{t\in[0,\infty],\ v\in S^{d-1}}
   |f_n(t,v)-\bar f_n(t,Pv,\|(I-P)v\|)|
   \le C_{\rm data,\eta}/\sqrt n.
   \tag{19}
   \]

   Pointwise conditional variance does not control this supremum. Direct
   fine-net arguments using a scalar Gaussian tail would ordinarily leave
   a width-dependent entropy factor; that factor cannot be absorbed into
   the fixed constant in (2). A sufficient new result would be increment
   bounds with a width-independent entropy integral, including the entire
   trained trajectory. Such a result is not supplied by the assigned
   whole-feature source theorem or by (17).

2. Even if (19) were proved, (15) currently evaluates the original trained
   matrices. Those matrices have O(n^2) retained coefficients. A finite
   autonomous network realizing the conditional mean to root-width accuracy
   must still be constructed from initial information, with every retained
   coefficient counted. Neither the expectation sign nor the exact symmetry
   removes that storage. Training-only temporal source spaces do not
   automatically control passive-query nonlinear propagation through those
   matrices.

A possible concrete variant, also unproved, chooses a fixed unit vector e
perpendicular to V and replaces a sphere query v by
Pv+||(I-P)v||e. Conditional symmetry gives equality of the two conditional
means. A uniform bound like (19) would then compare their actual outputs
at root-width scale. The existing source construction could be restricted
to the sphere in V plus span{e}, with input dimension k+1. But the resulting
query preprocessor contains a norm, and is not the original linear first
layer. Its implementation and storage must be included if the admissible
runtime is required to be an ordinary neural network. This variant cannot
be called a proved exponent reduction under the present contract.

## 5. Route registry and conclusion

| Claim | Status | Consequence |
|---|---|---|
| Uniform whole-feature linear approximation needs dimension at least (log n/log log n)^(d-1) for sine initialization | Proved above, pending independent reconstruction | A dimension-free logarithmic exponent requires a different interface |
| Conditioning on the training input span removes unused directions from the conditional mean | Exact finite-n identity | Identifies one output-specific mechanism unavailable to whole-feature compression |
| Conditional fluctuations are O(n^-1/2) for each fixed time and query | Proved above on stated parameter events | No population comparison assumption is needed for this limited statement |
| Fluctuations obey the same bound uniformly over time and the whole sphere | Open | Required for replacing the realized function by the conditional mean |
| The conditional mean admits a counted small autonomous trained-network realization | Open | Required even after uniform concentration |
| Arbitrary autonomous networks require dimension-dependent log exponents | Not proved or claimed | The source obstruction cannot settle the original existence question |

The strongest complete result in this route is the source-interface lower
bound (4). It rules out removing input dimension merely by a better linear
basis, low-rank truncation, or sampling theorem while retaining the current
uniform first-feature approximation requirement. It does not obstruct
output-specific nonlinear representations. The exact training-span
conditioning is a candidate mechanism for those representations, with
uniform root-width fluctuation control as its first unresolved bottleneck.
