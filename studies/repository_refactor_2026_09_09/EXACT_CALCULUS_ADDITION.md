### 7.2. Forest factorization and small exact certificates

The following is a reusable, finite algebraic part of the calculus. It is
not a claim that a high-order compiler, an infinite Taylor series, or a
positive-time population evolution has been verified. The implementation
`pde.exact_calculus` supplies a canonical forest key, rational finite-series
reversion, rational determinants, and one completely specified certificate.
No retained table is an input to these operations.

#### Decorated forests and the leading Gaussian factorization

Take independent standard Gaussian variables \(a_i,u_j,g_{ij}\), for
\(1\le i,j\le n\), with the two neuron populations kept separate. A finite
bipartite forest has second-layer vertices decorated by powers of \(a_i\),
first-layer vertices decorated by powers of \(u_j\), and an edge for each
factor \(g_{ij}\). Decorations are nonnegative integers, and edges are simple.
Sum its monomial over all neuron labels, with no restriction that different
vertices have different labels. If it has \(e\) edges and \(r\) connected
components, normalize this sum by \(n^{-e/2-r}\). Let its expectation be
\(T_n\). All graph sizes and decorations in this paragraph are fixed while
\(n\) grows.

**Finite-forest factorization.** The limit of \(T_n\) exists. It equals the
product of the limits of its separately normalized connected components.
A component with an odd number of edges has zero limit. The assertion
concerns expectation; it does not alone prove concentration or empirical-law
convergence.

Here is a direct proof. If the total edge count is odd, Gaussian symmetry
makes the expectation zero. Otherwise write \(e=2p\). Expanding the Gaussian
edge expectation into pairings, as proved in Section 4, identifies both
endpoints of every pair of edges. Collapse each pair to a single edge in
the resulting multigraph. Let \(v\) be its number of vertices and \(c\)
its number of connected components. A connected multigraph with \(v_0\)
vertices needs at least \(v_0-1\) edges: begin with one vertex and add an
edge each time the reachable vertex set grows. Consequently
\[
 v\le p+c,\qquad c\le r.
 \tag{7.F1}
\]
For this fixed pairing, labelings with no extra equality among distinct
vertices in either neuron population number
\((n)_{v_1}(n)_{v_2}=n^v+O(n^{v-1})\), where \(v_1+v_2=v\) and
\((n)_b=n(n-1)\cdots(n-b+1)\). Their decoration expectation is the product
of the Gaussian moments at the quotient vertices. Labelings with an extra
equality number \(O(n^{v-1})\): choose an equal vertex pair and then all
remaining labels freely. Their Gaussian decoration moments are bounded by
a constant depending only on the fixed decorations. Thus this pairing
contributes a constant times \(n^{v-p-r}\), with an error one power smaller.
There are finitely many pairings. By (7.F1) none diverges.

Only \(v=p+r\) can survive. It requires \(c=r\) and equality in the
connected edge bound, so no pairing joins two original components and each
quotient component is a tree. Conversely the independently chosen surviving
pairings of the original components give exactly these surviving full-forest
pairings. Their decoration factors multiply, and the leading coefficient
of each free-label count is one. Summing proves the product assertion. If
an original component has odd edge count there is no internal complete
pairing, so the limit is zero. This also handles odd total edge count and
isolated vertices. No independence of trained coordinates has been asserted.

For example a two-edge component \(g_{ij}g_{ik}u_j^2u_k^2\), with its
three labels summed and normalization \(n^{-2}\), has only one edge
pairing. It forces \(j=k\), leaving two free labels and moment
\(E u_j^4=3\). Two disjoint copies have limit \(9\): pairings between
the copies identify their components and lose at least a factor \(1/n\).
An isolated second-layer decoration \(a_i^2\), normalized by \(1/n\),
has limit one and can be multiplied into this example. This factorization
is the reason connected objects can be computed once and reused.

To make that reuse independent of arbitrary vertex names, give vertex \(v\)
the color \((\ell_v,b_v)\), its layer in \(\{1,2\}\) and decoration.
For a rooted tree define its key recursively to be its root color followed
by the sorted tuple of its children's keys. The key of an unrooted tree
is the lexicographically smallest rooted key over all possible roots.
The key of a forest is the sorted tuple of its component keys, retaining
repetitions. The empty forest has the empty tuple.

Induction on tree size proves that rooted keys agree exactly when a
color-preserving rooted isomorphism exists: equal sorted lists match the
children with multiplicity and invoke the induction on each subtree;
the reverse implication follows from the same decomposition. Equal minima
for two unrooted trees give roots with equal rooted keys and hence an
unrooted isomorphism. An unrooted isomorphism maps the whole list of rooted
keys onto the other, proving the converse. The same component argument
proves the forest assertion. Therefore this immutable key can safely index
a caller's memoization of any genuinely isomorphism-invariant calculation.
It does not by itself compute that calculation or certify a coefficient
generator. Edge validation by successively merging connected components
rejects a duplicate or cycle exactly when its two endpoints were already
connected. This proves the validation and key logic in `forest_key`.

#### A fully specified quadratic initialization-jet obstruction

This example uses a different metric and initialization from the main
nonlinear training theorem. It is a negative test of a proposed universal
representation, not a recommended model for feature learning. There is one
sample \(x=y=1\), \(d=1\), \(L=2\), quadratic activations, and
\[
 W^{(1)}_j=u_j,\quad W^{(2)}_{ij}=g_{ij}/\sqrt n,
 \quad W^{(3)}_i=a_i,\qquad
 z_i^{(2)}=\frac1{\sqrt n}\sum_j g_{ij}u_j^2,
 \quad f_n=\frac1n\sum_i a_i(z_i^{(2)})^2.
 \tag{7.C1}
\]
All the displayed initialization Gaussians are independent standard normals;
the stored readout is order one. Freeze only the first parameter block and
use feature ascent, with hidden stored-block mobility one and readout
mobility \(n\). Thus, in the auxiliary unscaled matrix coordinates,
\[
 \frac{da_i}{ds}=(z_i^{(2)})^2,\qquad
 \frac{dg_{ij}}{ds}=\frac2{\sqrt n}a_i z_i^{(2)}u_j^2,
 \qquad \frac{du_j}{ds}=0.
 \tag{7.C2}
\]
These equations follow by differentiating (7.C1); they are not loss GD or
physical-time GF. Put \(q_n=n^{-1}\sum_j u_j^4\). Differentiating the
preactivation gives \(dz_i^{(2)}/ds=2q_n a_i z_i^{(2)}\). Therefore the
exact finite initialization derivative of order \(k\) is
\[
 \left.\frac{d^k f_n}{ds^k}\right|_{s=0}
 =\frac1n\sum_i \mathscr D_{q_n}^{,k}(a_i(z_i^{(2)})^2),
 \quad \mathscr D_q=z^2\partial_a+2qaz\partial_z.
 \tag{7.C3}
\]
Here \(a,z\) are the two scalar arguments of a polynomial; the superscript
on \(\mathscr D\) is repeated application, not a weight-layer index.
Repeated chain rule proves (7.C3), since \(q_n\) is constant along (7.C2).
Smooth finite equations have a local solution at every initial state; no
positive-time uniform existence is needed to define these derivatives.

Conditional on all \(u_j\), the pairs \((a_i,z_i^{(2)})\) at initialization
are independent, with laws \(N(0,1)\otimes N(0,q_n)\). Set
\(z=\sqrt q\,\xi\). Then
\(\mathscr D_q=q(\xi^2\partial_a+2a\xi\partial_\xi)\) and
\(az^2=qa\xi^2\). Conditional expectation of (7.C3) is consequently
\(c_k q_n^{k+1}\), for a fixed finite constant \(c_k\).

To pass to the unconditional limit without a probabilistic black box, note
that \(E u^4=3\) and independence imply \(E(q_n-3)^2=\operatorname{Var}(u^4)/n\).
For every positive integer \(b\), convexity gives
\(E q_n^{2b}\le E|u|^{8b}<\infty\), uniformly in \(n\).
For a nonnegative \(x\), factorization of \(x^b-3^b\) bounds its absolute
value by \(b|x-3|\max(x,3)^{b-1}\). Cauchy--Schwarz and the preceding
moment bound show \(E|q_n^b-3^b|\to0\). Hence all fixed-order annealed
initialization derivatives have the exact limit
\[
 d_k=E\mathscr D^k(AZ^2),\qquad
 \mathscr D=z^2\partial_a+6az\partial_z,\quad
 A\sim N(0,1),\ Z\sim N(0,3)\text{ independent}.
 \tag{7.C4}
\]
The expectation is of the polynomial after substitution \((a,z)=(A,Z)\).
This proves the probabilistic interpretation of this particular coefficient
recurrence. It does not interchange an infinite series with a width limit.

The elementary monomial rules are
\[
 \mathscr D(a^p z^q)=p a^{p-1}z^{q+2}+6q a^{p+1}z^q,
 \qquad E[A^pZ^q]=
 \begin{cases}(p-1)!!(q-1)!!3^{q/2},&p,q\text{ even},\\0,&\text{otherwise}.
 \end{cases}
 \tag{7.C5}
\]
Use \((-1)!!=1\). The moment rule follows by integrating the Gaussian
density derivative by parts, starting with moment zero equal to one;
independence multiplies the two moments. Each application changes the
parity of the \(a\) exponent and preserves the parity of the \(z\) exponent.
Thus all even \(d_k\) vanish. Starting from the single monomial \(az^2\),
(7.C5) through order thirteen gives
\[
 (d_1,d_3,d_5,d_7,d_9,d_{11},d_{13})=
 (63,77760,274547232,2141006515200,31149221916487680,
 759035131220036321280,28719223368439752070594560).
 \tag{7.C6}
\]
For instance the first differentiated polynomial is \(z^4+12a^2z^2\),
whose expectation is \(27+36=63\). The finite recurrence (7.C5), not a
table read from another source, specifies every other integer in (7.C6).

Form the formal series \(F(s)=\sum_{k\ge0}d_k s^k/k!\). This is a
formal algebraic object; no convergence is presumed. Its zero constant and
nonzero linear coefficient give a unique formal inverse \(B(y)\).
Define \(K(y)=F'(B(y))\). Since \(F\) is odd, uniqueness makes \(B\)
odd and \(K\) even. Define the coefficients \(\mu_j\) by
\[
 K(y)=63+y^2\sum_{j\ge0}(-1)^j\mu_j y^{2j}.
 \tag{7.C7}
\]
Only (7.C6) is needed for \(\mu_0,\ldots,\mu_5\). There is no use
of a specialized inversion theorem: if \(a_k=d_k/k!\), let \(b_0=0\),
\(b_1=1/a_1\), and successively set
\[
 b_k=-\frac1{a_1}[y^k]\sum_{j=2}^k a_j
                  \left(\sum_{i=1}^{k-1}b_i y^i\right)^j.
 \tag{7.C8}
\]
The only degree-\(k\) term involving the unknown \(b_k\) in \(F(B(y))\)
is \(a_1b_k\); thus induction proves both existence and uniqueness and
the formula. Ordinary convolution gives each product coefficient.
Substitution in \(F'(B(y))\) gives exactly
\[
 (\mu_0,\ldots,\mu_5)=\left(
 \frac{480}{49},\frac{43756}{151263},\frac{7214528}{200120949},
 \frac{12545175968}{2402451992745},
 \frac{171752915595136}{200241971143303005},
 \frac{2199776554157960896}{14570607030242443158825}\right).
 \tag{7.C9}
\]

These six coefficients cannot be moments of a nonnegative measure on
\([0,\infty)\). Indeed the shifted moment matrix
\(M_{ij}=\mu_{i+j+1}\), \(0\le i,j\le2\), satisfies
\[
 \det M=-\frac{86245462994269879146938487857152}
 {200150589172828762588730609071155193161975}<0.
 \tag{7.C10}
\]
There is also a direct polynomial witness, avoiding a definiteness criterion.
Let \(p(\lambda)=v_0+v_1\lambda+\lambda^2\), where
\[
 v_0=\frac{40042013405871059816}{2310453239160606810795},\qquad
 v_1=-\frac{14165989123115588}{49896409440894219}.
\]
Direct rational multiplication of (7.C9) gives
\[
 \sum_{i,j=0}^2v_i v_j\mu_{i+j+1}
 =-\frac{673792679642733430835456936384}
 {329714727520793070279653295504327135}<0,
 \qquad v_2=1.
 \tag{7.C11}
\]
If such a representing measure \(\nu\) existed, this finite sum would
equal \(\int\lambda p(\lambda)^2\nu(d\lambda)\ge0\). This is the
contradiction. All relevant moments are finite by the representation being
tested. The result refutes a representation demanded uniformly over metrics
including this zero first-block mobility. It does not settle the unit-metric
case, any strictly positive first mobility, or an actual positive-time
population equation. Nonexistence of this moment representation is not
nonexistence of a nonlinear feature-learning limit.

#### Implementation and independent checking routes

`revert_series` accepts ordinary rational coefficients and implements (7.C8)
by truncated composition in Horner order. Multiplication is the finite
convolution \((ab)_k=\sum_{i=0}^k a_i b_{k-i}\). It returns all inverse
coefficients to the same length, without mutating its input. A nonzero
constant or zero linear coefficient is rejected. `determinant` eliminates
successive columns using a nonzero pivot, swapping rows when necessary and
tracking the determinant sign. Subtracting multiples of one row from another
preserves the determinant; each pivot multiplies the remaining triangular
determinant. If no pivot exists, the remaining first column is zero and the
determinant is zero. The empty determinant is one. This proves its algorithm
over the rational field, including singular matrices.

`quadratic_axis_certificate()` generates (7.C6) directly from (7.C5), reverts
the ordinary series using (7.C8), composes its derivative to produce (7.C9),
and constructs the witness by solving the leading two-by-two shifted system:
\[
 v_0=\frac{\mu_2\mu_4-\mu_3^2}{\mu_1\mu_3-\mu_2^2},\qquad
 v_1=\frac{\mu_2\mu_3-\mu_1\mu_4}{\mu_1\mu_3-\mu_2^2}.
\]
The positive denominator is checked before division. Tests independently
compare the six displayed fractions and evaluate (7.C11) from the displayed
witness; a Leibniz-permutation determinant checks the elimination route.
Series tests compose both directions of reversion, and forest tests check
relabelling, edge order, component multiplicity, invalid graphs and changed
decorations. They do not validate an unimplemented general-depth generator.

All scalar arithmetic in this module is integer or `fractions.Fraction`;
floating values and booleans are rejected by its rational interfaces.
Graph indices and colors are nonnegative Python integers, with layer one or
two. Inputs are finite lists or tuples. Results are freshly constructed;
there is no cross-call cache, sampling or file output. Rational bit sizes and
the all-roots tree-key cost can grow, so these are small transparent reference
primitives, not performance claims for large-order campaigns. Python recursion
limits still apply to the recursive tree key.

The established unit-test command in the code guide regenerates all displayed
coefficient and witness checks. No generated data, historical coefficient
array, symbolic package or external source is required. Exact arithmetic
certifies these finite computations, while (7.C1)--(7.C5) supply the separate
initialization-jet interpretation. Neither part supplies a positive-time
identification bridge.
