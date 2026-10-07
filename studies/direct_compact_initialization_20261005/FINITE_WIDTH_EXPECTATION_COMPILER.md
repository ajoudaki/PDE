# Finite-width expectation without a realized dense network

2026-10-06. **Proved finite-program compiler and computable finite-grid
expectation theorem.** A finite polynomial tensor program with symmetric
neuron-index sums has an exact finite-width expectation formula under
independent truncated Gaussian coordinates. The formula enumerates typed
index-equality partitions and includes arbitrary contraction graphs,
cycles, repeated edges, and forward/transpose reuse. It does not evaluate
any realized width-$n$ network.

Combined with certified finite-time ODE and polynomial approximation, this
gives a terminating algorithm for the expectation of a specified computable
bounded continuous score of finitely many canonical dense predictions,
including a score comparing them with a fixed small-model candidate.
There is no useful efficiency claim. Graph count, degree, coefficient
precision, and setup workspace can be enormous. Only the final candidate,
not the compiler workspace, can retain the previously stipulated compact
size.

This is same-study author work, not a blind review or a promotion.
Current AGENTS.md and the proof and conjecture-investigation instructions
were read. The maintained notation contract and previously disclosed
canonical-skill fallback apply. The complete maintained Section C.2,
“Gaussian integration and adaptive initialization,” was read for context;
no population-limit identification theorem is imported from it. The
argument below is finite-width and elementary. No experiment, dense
simulation, implementation test, or Git operation was performed.

## 1. Exact class of finite programs

Fix positive integer neuron sizes $n_1,\ldots,n_L$. The canonical model
below has two populations, each of size $n$. A typed index variable takes
values in exactly one set $\{1,\ldots,n_\ell\}$. Distinct populations remain
distinct types even when their cardinalities coincide.

Primitive random arrays have fixed arity and prescribed ordered index
types. Every distinct array coordinate is an independent standard
Gaussian, and different array families are independent. Reusing the same
coordinate, at another time or through a transpose, reuses the same random
variable. Fixed data-coordinate labels may be attached to array families.
The allowed tensor-program operations are:

- addition, scalar multiplication, and multiplication of entries, with
  consistent identification of shared free indices;
- transpose, relabeling of free indices, and contraction by summing a typed
  index over its full population;
- applying a specified univariate polynomial coordinatewise;
- finite arithmetic operations involving fixed data, times, candidate
  coefficients, and explicit scalar functions of the sizes.

The number of neuron-index sums is specified by the program syntax;
their ranges are not unrolled into lists of neuron values. Fixed finite
data or query loops may be unrolled and their costs are counted. An
identity tensor can be included by imposing the corresponding index
equalities. The final object is scalar, so it has no uncontracted neuron
indices.

These operations define a finite polynomial in the primitive Gaussian
coordinates for every fixed choice of sizes. The program description
can be much smaller than that polynomial's ordinary expansion into
individually named coordinates. Arbitrary discontinuous branching,
randomly chosen array indices, or an unspecified invariant black-box
function are not additional primitives.

## 2. Contraction-graph normal form

A scalar contraction graph has finitely many typed vertices. A vertex
represents a neuron-index variable, and a random-array occurrence is an
edge with its array-family label and ordered incident vertices. Unary
edges suffice for first-layer coordinates with a fixed input-coordinate
label; a middle-matrix entry is an ordered two-vertex edge. Multiple
edges, repeated vertices, isolated vertices, and cycles are allowed.

For such a graph $G$, define

$$
\mathcal P_G(X)=
\sum_{\substack{\sigma(v)\in\{1,\ldots,n_{\ell(v)}\}\\v\in V(G)}}
\prod_{e\in E(G)}
X^{a(e)}_{\sigma(v_{e,1}),\ldots,\sigma(v_{e,r_e})}.
                                                               \tag{1}
$$

Here $\ell(v)$ is the vertex type, $a(e)$ is the random-array family,
and the ordered edge ports determine the array coordinate. Coefficients
and normalization factors, such as $n^{-1}$ and $n^{-1/2}$, are kept
outside (1).

Every allowed scalar program can be converted by a finite symbolic
algorithm to

$$
\mathcal P(X)=\sum_{\gamma=1}^M c_\gamma(n_1,\ldots,n_L)
\,\mathcal P_{G_\gamma}(X).                         \tag{2}
$$

**Proof.** Keep a similar graph list with designated free ports for each
intermediate tensor. A primitive array is one edge. Addition concatenates
the lists. For multiplication, choose a term from each list, first rename
their bound vertices to prevent accidental capture, and then identify
only the corresponding free ports required by the tensor multiplication.
Their graph union represents the product. A contraction changes its
specified free index into a bound vertex. Transpose only changes the
ordered free-port convention; it does not create a new random-array
family. A polynomial is expanded as a finite sum of powers using these
same operations. Induction over the finite program proves (2).

There is no acyclicity hypothesis. In particular, variable reuse is
preserved by common edge-family and ordered-coordinate identities, not
discarded by a replacement with a fresh Gaussian action.

## 3. Exact expectation by typed equality partitions

Let $\nu_B$ be the standard Gaussian law conditioned on $[-B,B]$, with
$B>0$, and let all primitive coordinates be independent with this law.
Define its moments

$$
\mu_j(B)=
\frac{\int_{-B}^B x^j\phi(x)\,dx}{Z_B},
\qquad
\phi(x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}},
\qquad Z_B=\int_{-B}^B\phi(x)\,dx.                  \tag{3}
$$

For each type $\ell$, partition the vertices of that type into blocks.
Let $\pi=(\pi_1,\ldots,\pi_L)$ denote the collection of these partitions.
Vertices belong to the same block exactly when their assigned neuron
indices are equal. In the quotient graph $G/\pi$, two random-array
occurrences refer to the same coordinate exactly when their family
labels and their ordered lists of incident blocks agree. Write
$m_a(G/\pi)$ for the multiplicity of each resulting distinct coordinate
$a$.

With $(n)_j=n(n-1)\cdots(n-j+1)$, $(n)_0=1$, and $(n)_j=0$ when $j>n$,
the exact formula is

$$
\mathbb E_{\nu_B}\mathcal P_G
=
\sum_{\pi_1,\ldots,\pi_L}
\left(\prod_{\ell=1}^L(n_\ell)_{|\pi_\ell|}\right)
\left(\prod_{a\in E_{\mathrm{distinct}}(G/\pi)}
\mu_{m_a(G/\pi)}(B)\right).
                                                               \tag{4}
$$

**Proof.** Every assignment in (1) induces exactly one such collection
of equality partitions. For a fixed partition, injectively assigning its
blocks to neuron labels gives $(n_\ell)_{|\pi_\ell|}$ assignments of
type $\ell$. Assignments of different types are counted separately.
For every assignment with these partitions, the random monomial contains
precisely the coordinate multiplicities specified by the quotient graph.
Independence of distinct coordinates makes its expectation the product
of their moments. Summing over assignments proves (4).

Types must not be merged merely because they have equal numeric
cardinalities. In the canonical matrix, its row belongs to population
two and its column to population one. Conversely, reading that matrix
through its transpose uses the same ordered original row/column
coordinate key. These rules preserve all reuse correlations.

The moments in (3) are computable from one-dimensional integrals.
Symmetry gives $\mu_0=1$ and every odd moment zero. For even $j\ge2$,
integration by parts using $\phi'(x)=-x\phi(x)$ gives

$$
\mu_j(B)
=(j-1)\mu_{j-2}(B)
-\frac{2B^{j-1}\phi(B)}{Z_B}.                       \tag{5}
$$

Thus (4)--(5) are exact formulas involving finitely many integer counts,
coefficients, and one-dimensional Gaussian constants. “Exact” refers to
these identities; numerical values are evaluated with certified
arbitrary precision. Possible cancellation in (5) requires precision or
direct interval integration, not an assumption of stable floating-point
evaluation.

### A cyclic example

Let $V_{ij}$ be independent with law $\nu_B$. Consider

$$
\frac1{n^3}\sum_{i,j,k,l}V_{ik}V_{jk}V_{jl}V_{il}.
$$

The two row vertices and two column vertices form a cycle. Only the cases
$i=j$, or $k=l$, survive the odd-moment rule. Separating their overlap,
its exact expectation is

$$
2\left(1-\frac1n\right)\mu_2(B)^2+\frac{\mu_4(B)}n.
$$

For untruncated standard Gaussians this becomes $2+1/n$. This calculation
includes the finite-width collision term that a distinct-index or
forest-only rule would omit.

## 4. Explicit symbolic cost and width dependence

Suppose (2) contains $M$ graphs, each with at most $v$ vertices and $D$
random-array occurrences. Each graph requires at most

$$
\prod_{\ell=1}^L\operatorname{Bell}(v_\ell)
\le \max(1,v)^v
$$

partition cases. The inequality follows by encoding a set partition of
$q$ elements by a map from those elements to their least block elements,
giving at most $q^q$ possibilities, and then multiplying over types.
After a partition is chosen, coordinate-key grouping, multiplicity
counting, and falling-factorial evaluation take a polynomial number of
operations in $v,D$ and the fixed array arities. Consequently a direct
upper bound, apart from coefficient generation and numerical precision,
is

$$
M\,\max(1,v)^v\,\operatorname{poly}(v,D)
                                                               \tag{6}
$$

arithmetic operations, together with moments through degree $D$.

The instruction graph is a finite DAG with symbolic ports. For example,
the entire middle initialization is the single tensor expression
$W_0(i,j)=n^{-1/2}V(i,j)$, not a table with $n^2$ entries. At an Euler
stage, $A_t(j,\alpha)$, $W_t(i,j)$, and $w_t(i)$ are expression-DAG roots
with these free ports. A neuron sum is a binding instruction carrying
the integer range $n$. Its body is never evaluated separately at
$1,\ldots,n$. Recursive symbolic substitution produces the graph list;
it can duplicate expression bodies, but not realized random entries.
The instruction DAG is acyclic in computational order even when its
index-contraction graphs contain cycles.

The costs $M,v,D$ are also effectively bounded from the program. For
example, assume its $s$ operation nodes have polynomial degree at most
$q\ge2$ and its primitive tensors have at most $a$ free ports. With
ordinary binary arithmetic nodes, conservative expansion bounds are

$$
D\le q^s,\qquad
v\le(a+s)q^s,\qquad
M\le(q+1)^{(q^s-1)/(q-1)}.                          \tag{7}
$$

For the last estimate start with one term: an addition, multiplication,
or polynomial node increases the current maximum term count by at most
the recurrence $M_{j+1}\le(q+1)\max(1,M_j)^q$.
Degrees at most multiply by $q$ per node; vertex counts obey the same
bound with room for newly introduced bound or broadcast indices.
These estimates are intentionally crude. A tensor polynomial involving
several arguments is first represented by its finite arithmetic circuit.

Graphs and their partitions can be generated and processed one at a
time. No list indexed by all $n^2$ primitive middle coordinates is
needed. Widths enter (4) as the integers $n_\ell$, their falling
factorials, and the explicit scalar coefficients of the program.
Choosing the discretization and polynomial degrees may depend very
strongly on width; (7) is not a width-independent complexity estimate.
The graph sizes themselves can exceed $n^2$ for an expensive chosen
approximation. They describe monomials and equality patterns, not stored
values of a realized initialized or trained network.

All coefficients and moments can be evaluated using rational interval
arithmetic until the final interval has a requested width. Finite
termination follows from their computability and the finite number of
operations. A conservative absolute contribution bound uses
$(n_\ell)_j\le n_\ell^j$ and
$|\mu_r(B)|\le\max(1,B)^r$; it supplies a finite precision budget even
when the final sum has severe cancellation. Coefficient bit lengths
and this precision are additional setup costs.

The zero polynomial can be returned exactly. Otherwise take $M\ge1$.
More explicitly, fix one finite search stage and let
$N_{\mathrm{part}}=\max(1,v)^v$ and $p=D+L+1$. Find a computable upper
bound $A\ge1$ for the absolute value of each scalar coefficient,
falling-factorial factor, and moment factor in its expanded formula.
Such a bound follows from its finite coefficient list,
$n_\ell^v$, and $\max(1,B)^D$. Products contain at most $p$ factors.
If each factor is approximated with error at most $\delta\le1$, the
telescoping product identity bounds its error by
$p\delta(A+1)^{p-1}$. It therefore suffices to allocate, before
additional rounding budgets,

$$
\delta\le
\frac{\epsilon_{\mathrm{num}}}
{2M N_{\mathrm{part}}p(A+1)^{p-1}}.
                                                               \tag{7a}
$$

Every quantity in this finite-stage bound is computable. Exact
falling-factorial integers need at most
$O(v\log(n_{\max}+v+1))$ bits; their evaluation need not be rounded.
The remaining factors and sums use certified interval precision,
with a separate half-budget for arithmetic rounding. Source constants
supplied merely as computable reals may have slow evaluation algorithms,
so this is a finite precision prescription, not a uniform polynomial
bit-operation bound.

## 5. The canonical network belongs to the compiler after approximation

Use independent standard Gaussian formal entries

$$
A_{j\alpha}(0),\qquad V_{ij},\qquad
W_{ij}(0)=n^{-1/2}V_{ij},\qquad w_i(0)=0.
$$

The index $j$ belongs to the first neuron population, $i$ to the second,
and $\alpha\in\{1,\ldots,d\}$ is a fixed input-coordinate label.
For training data, let $v_a=x_a/\sqrt d$, with $\|v_a\|_2=1$, and set

$$
u_a=Av_a,\quad h_a=\tanh(u_a),\quad z_a=Wh_a,\quad
g_a=\tanh(z_a),\quad f_a=w^Tg_a/n,\quad r_a=f_a-y_a.
$$

Define $b_a=w\odot\tanh'(z_a)$ and
$c_a=\tanh'(u_a)\odot W^Tb_a$. The squared mean loss and mobilities
$(n,1,n)$ give

$$
\dot w=-\frac2m\sum_a r_ag_a,\qquad
\dot W=-\frac2{mn}\sum_a r_ab_ah_a^T,\qquad
\dot A=-\frac2m\sum_a r_ac_av_a^T.                  \tag{8}
$$

Replace each use of $\tanh$ and $\tanh'$ by fixed polynomials, and take
any fixed finite explicit Euler grid. Each update, prediction at a
fixed query, empirical loss, and entry of a finite training-feature Gram
then has exactly the tensor-program form of Section 1. Every occurrence
of the initial $V$ uses the same family label. Learned matrix increments
are expressions in these same initial formal variables. Thus repeated
training and backpropagation are covered by (4) without fresh Gaussian
substitutions.

The statement so far is exact for the specified polynomial Euler
program. The next section supplies an effective approximation of the
actual finite-time tanh flow; an infinite-width limit is not involved.

## 6. Certified finite-time boxes and approximation

Fix $n,d,m$, a finite horizon $T$, computable fixed data, and a truncation
level $B>0$. Put $Y=(m^{-1}\sum_a y_a^2)^{1/2}$. Under
$|A_{j\alpha}(0)|,|V_{ij}|\le B$, the exact flow (8) has, for $0\le t\le T$,

$$
\begin{aligned}
|w_i(t)|&\le2Yt,\\
|W_{ij}(t)|&\le B/\sqrt n+2Y^2t^2/n,\\
|A_{j\alpha}(t)|
&\le B+2Y^2B\sqrt n\,t^2+2Y^4t^4.
\end{aligned}                                                    \tag{9}
$$

To prove these bounds, the gradient-flow loss is nonincreasing, so the
residual RMS is at most $Y$, and
$m^{-1}\sum_a|r_a|\le Y$. Bounded tanh gates and derivatives first give
$|\dot w_i|\le2Y$, then
$|\dot W_{ij}|\le2Y|w_i|/n$. For the first layer, $|v_{a,\alpha}|\le1$
and

$$
|\dot A_{j\alpha}|
\le2Y\sum_i |W_{ij}|\,|w_i|
\le4Y^2t(B\sqrt n+2Y^2t^2).
$$

Integration proves (9). Starting with local existence of the smooth
finite-dimensional vector field, these bounds prevent finite-time
escape, giving existence through every finite $T$. They hold for
arbitrary signed labels; no small-label condition is required here.

Enlarge the componentwise box (9) by a fixed margin, say one. On this
box the vector field has computable finite maximum-coordinate bounds

$$
\|F(\theta)\|_\infty\le M_F,\qquad
\|F(\theta)-F(\widetilde\theta)\|_\infty
\le L_F\|\theta-\widetilde\theta\|_\infty.           \tag{10}
$$

These constants need not be obtained from an $n$-width array or its
Jacobian. Propagate magnitude and Lipschitz bounds through the finite
typed expression for (8): addition adds bounds; multiplication uses
$|ab-\widetilde a\widetilde b|
\le |a||b-\widetilde b|+|\widetilde b||a-\widetilde a|$;
a neuron sum multiplies its bound by its scalar range size; and tanh,
$\tanh'$, and their needed derivatives have explicit global bounds.
Fixed data-coordinate and sample sums are finite known sums.
This yields a concrete finite scalar calculation of valid $M_F,L_F$.

On the enlarged box all activation arguments have computable bounded
intervals. When gates are approximated within $\epsilon\le1$, their
absolute values are at most two, so the polynomial intermediate
preactivations also have explicit intervals: first-layer arguments are
bounded by $\sqrt d$ times the first-weight coordinate bound, and
second-layer arguments by twice $n$ times the middle-weight coordinate
bound. Choose one interval containing both. Error propagation through
the same finite expression gives a computable uniform vector-field
error bound $\delta_F$ tending to zero with the scalar gate errors.

Here is an elementary effective polynomial approximation rule. For a
Lipschitz function $a$ on $[0,1]$ with constant $L_a$, its Bernstein
polynomial of degree $q$ is the expectation of $a(K/q)$ for
$K\sim\operatorname{Binomial}(q,x)$. Since
$\mathbb E|K/q-x|\le1/(2\sqrt q)$, its uniform error is at most
$L_a/(2\sqrt q)$. After the affine change from $[-S,S]$, the errors for
$\tanh$ and $\tanh'$ are at most $S/\sqrt q$ and $2S/\sqrt q$.
Their finitely many coefficient evaluations are computable and can
be rounded with an additional certified error. This gives a terminating
choice of the gate polynomials.

Let $\widehat\theta_j$ be Euler iterates with mesh $h$ for the polynomial
field, with the same formal initial state as the true flow. On the
enlarged box the error recurrence is

$$
e_{j+1}\le(1+hL_F)e_j+h\delta_F+\frac12L_FM_Fh^2,
\qquad e_0=0.                                      \tag{11}
$$

The local truncation term follows by integrating
$F(\theta(t+s))-F(\theta(t))$, whose norm is at most $L_FM_Fs$.
The other terms use (10) and the uniform field approximation. Hence
through time $T$,

$$
e_j\le
\left(\delta_F+\frac12L_FM_Fh\right)
\frac{e^{L_FT}-1}{L_F},                            \tag{12}
$$

with the continuous interpretation $T\delta_F$ if $L_F=0$.
Choose the scalar gate accuracy and $h$ so the right side is below,
for example, $1/2$. Induction then keeps every Euler iterate inside the
enlarged box: its true counterpart lies in the smaller box and (11)
maintains the stated margin. This also justifies the use of the
uniform approximation bounds in the recurrence.

Every prescribed polynomial tensor observable has a computable
Lipschitz constant on this box by the same propagation rules.
For predictions and feature Grams, gate approximation in the
observation map adds another computable vanishing error. Thus the
polynomial Euler observables approximate all outputs on any prescribed finite
time/query grid uniformly over the entire truncated initialization
cube to any requested tolerance. Rational query times can be included
in a common mesh; computable times may first be approximated using
the same finite-time derivative bounds.

## 7. From observables to a bounded score

Let the chosen finite observable grid have $K$ entries, and write its exact
dense observable vector as $O_n$. Besides predictions it may contain
empirical residual norms, finite Gram entries, or weighted squared
parameter norms represented by contractions. Fix a small-model candidate
independently of the dense initialization. Any candidate predictions
and certificate quantities entering the score are assumed computable
with certified error on this finite horizon; this hypothesis may be
verified by a separate finite-dimensional ODE certificate.

Let $\sigma:\mathbb R^K\to[0,1]$ be a specified computable continuous
score, after incorporating the fixed candidate predictions and any
other fixed constants. Require an effective modulus of continuity on
the output boxes used. Smooth explicit scores with computable derivative
bounds meet this requirement. “Bounded continuous” alone, without a
computable function and effective approximation information, would not
be sufficient for an algorithm.

On a fixed compact box the score has an effective polynomial
approximation. To see this directly, rescale the box to $[0,1]^K$ and
use the tensor-product Bernstein polynomial with coordinate degree $q$.
For an effective modulus $\omega$ and any $a>0$, independent binomial
coordinates give

$$
\sup_x|B_q\sigma(x)-\sigma(x)|
\le\omega(a)+\frac{K}{4qa^2}.                      \tag{13}
$$

Indeed, on the event that every coordinate differs from its mean by
at most $a$, the error is at most $\omega(a)$; on its complement the
score changes by at most one. Chebyshev's inequality and a union bound
bound that complementary probability by $K/(4qa^2)$. The finitely many
score evaluations in the Bernstein coefficients can again be
approximated with certified error.

Combining (12), continuity of the score, and (13), one obtains a
polynomial tensor program $\mathcal P$ satisfying

$$
\sup_{\text{all initial coordinates in }[-B,B]}
|\sigma(O_n)-\mathcal P|\le\epsilon_{\mathrm{app}}   \tag{14}
$$

for any prescribed positive $\epsilon_{\mathrm{app}}$.
Finite empirical losses and finite Gram entries are already polynomial
observables after the gate approximation. Continuous norms, maxima,
or eigenvalue-based scores of a fixed finite Gram can be included
through their effective continuity and a further polynomial
approximation. Discontinuous pass/fail indicators require a separate
margin or smoothing argument; (13) does not uniformly approximate a
jump across its threshold.

For the root search's stated finite certificates, squared Frobenius
parameter norms are sums of squared symbolic tensor entries: for
example, $n^{-1}\sum_{j,\alpha}A_{j\alpha}^2$ and
$\sum_{i,j}W_{ij}^2$ are valid contractions. Fixed scalar block weights
and fixed small-model metric coefficients do not change the argument.
Taking square roots is a continuous scalar operation with the effective
modulus $|\sqrt a-\sqrt b|\le\sqrt{|a-b|}$ on nonnegative arguments.
For real symmetric $m\times m$ Gram matrices, the Rayleigh-quotient
formula gives

$$
|\lambda_{\min}(Q)-\lambda_{\min}(\widetilde Q)|
\le\|Q-\widetilde Q\|_{\mathrm{op}}
\le m\max_{a,b}|Q_{ab}-\widetilde Q_{ab}|.
$$

Thus minimum eigenvalues, residual norms, and these parameter norms
can be included in a bounded continuous certificate score without
inverting a near-singular Gram matrix. A continuous ramp that vanishes
outside a strict fitting/tail-certificate region remains within this
class provided its effective formula and modulus are supplied. Proving
that this gate eventually accepts a fitting trajectory is not part
of the expectation compiler.

If a proposed certificate uses a large operator rather than a fixed
finite Gram, its own invariant finite tensor-program representation
must be supplied. Trace powers, for example, are contractions already
covered by (4). An unspecified algorithm on an explicitly stored
$n\times n$ matrix is not made admissible merely by calling its output
a scalar score.

## 8. Removing initialization truncation

There are $N_G=nd+n^2$ independent standard Gaussian coordinates in
the canonical initialization used here. Let $E_B$ be the event that
all of them belong to $[-B,B]$. The exponential Markov inequality for
a standard Gaussian gives

$$
\mathbb P(E_B^c)\le2N_Ge^{-B^2/2}.                  \tag{15}
$$

Conditioning on this product event preserves independence and gives
exactly the product law $\nu_B$ used in (3)--(4).

Because $0\le\sigma\le1$,

$$
|\mathbb E\sigma(O_n)-\mathbb E[\sigma(O_n)\mid E_B]|
\le\mathbb P(E_B^c).
$$

Apply (14), and compute the conditional expectation of $\mathcal P$
by (2)--(5). If its certified numerical evaluation error is at most
$\epsilon_{\mathrm{num}}$, the resulting number $a$ satisfies

$$
|\mathbb E\sigma(O_n)-a|
\le
2(nd+n^2)e^{-B^2/2}
+\epsilon_{\mathrm{app}}+\epsilon_{\mathrm{num}}.   \tag{16}
$$

Every term can be made smaller than a prescribed positive budget by
finite, effectively chosen operations. For example, a rational $B$
larger than
$\sqrt{2\log(2(nd+n^2)/\epsilon_{\mathrm{tail}})}$
makes the first term at most $\epsilon_{\mathrm{tail}}$.
The output interval follows from (16). Thus the true finite-width
finite-grid score expectation is a computable real under the stated
input hypotheses.

## 9. Operational meaning and remaining boundaries

The compiler is an algorithmic construction, not merely a formal
power-series claim: it has a finite expression-generation procedure,
an exact moment formula, a terminating approximation schedule, and a
certified numerical error budget. It uses the canonical finite-width
law, including index collisions and matrix reuse, rather than replacing
that law by an infinite-width population process.

Nevertheless, this note supplies a proved algorithm, not executable
software or a demonstrated feasible computation. Its cost bounds are
in graph count, degree, Euler order, precision, data size, and score
dimension. These quantities can depend on $n$ so severely that the
procedure is unusable in practice. The procedure does not instantiate,
simulate, or inspect a particular width-$n$ initialization or trained
network. It also does **not** prove that the entire setup can run in
polylogarithmic workspace or time.

A candidate search may discard all compiler objects after a score is
certified and retain only the chosen small model. In that sense this
expectation procedure does not enlarge its final retained architecture
or metric/mixer state. A contract that also bounds peak setup storage,
setup time, or total precision needs further estimates and is not
resolved by that observation.

This theorem does not select a candidate, prove existence of a
successful candidate, turn a smooth score into a particular confidence
guarantee, or extend a finite grid to the sphere, all physical times,
or the endpoint. Those are separate deterministic or probabilistic
obligations. What it resolves is the computable expectation step for
the specified finite-width score without a realized dense reference.

This author result is frozen at handoff; its hash is reported separately.
