# C-H2 established obstruction boundaries

Complete designated Gaussian-calculus sections. These are boundaries, not
positive theorem premises. Exact source: docs/gaussian_calculus.md.

---

Source lines 1749–1823

## 6. Scope and obstructions to stronger calculus claims

**No full same-norm product closure with an unbounded atom.** Let
\(\mathfrak X\) be a normed space of random variables containing an
essentially unbounded \(X\) and all its powers. Suppose, for fixed
\(1\le p<\infty\) and \(A,C>0\),
\(\|V\|_{L^p}\le A\|V\|_{\mathfrak X}\) and
\(\|UV\|_{\mathfrak X}\le C\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}\).
Iteration and the identity
\(\|X^k\|_{L^p}=\|X\|_{L^{kp}}^k\) give
\[
 \|X\|_{L^{kp}}
 \le A^{1/k}C^{1-1/k}\|X\|_{\mathfrak X}.               \tag{6.1}
\]
The right side is bounded. For any \(B>0\), essential unboundedness gives
\(\mathbb P(|X|>B)>0\), and
\(\|X\|_{L^q}\ge B\,\mathbb P(|X|>B)^{1/q}\).
Letting \(q\to\infty\), then \(B\to\infty\), contradicts (6.1).
In particular a nondegenerate Gaussian atom cannot belong to such a full same-space
algebra. For a derivative-sum norm containing constants, the zero-order
weight must be positive; if its exponent is finite it supplies the
embedding used here, and if it is infinity it already excludes the
unbounded atom. This obstruction does not apply to the finite,
order-consuming moment estimates of Section 5.

**Independent coefficientwise jet obstruction.** On the unrestricted
space of finitely supported ordinary-derivative jets
\(u=(u_j)_{j\ge0}\), let
\(\|u\|_w=\sum_{j\ge0}w_j|u_j|\), with every \(w_j>0\).
Suppose both the shift \((Su)_j=u_{j+1}\) and the Leibniz product
\((u\star v)_j=\sum_{i=0}^j\binom ji u_i v_{j-i}\)
have fixed bounds \(C_S\) and \(C_P\) in this same norm.
Testing the shift on the unit jet \(e_j\), and the product on
\(e_1,e_{j-1}\), gives, for every \(j\ge2\),
\[
 w_{j-1}\le C_Sw_j,\qquad
 j w_j\le C_Pw_1w_{j-1},\qquad
 j\le C_PC_Sw_1,                                      \tag{6.2}
\]
which is impossible. For factorial-normalized derivatives the product
loses its binomial factor but the shift becomes
\((Su)_j=(j+1)u_{j+1}\); the same tests again give (6.2)'s final
contradiction. This statement concerns unrestricted positive
coefficientwise majorants, not an arbitrary restricted class of
expressions with cancellations.

**Zero Taylor radius does not exclude a smooth nonsingular ODE.** For
a standard Gaussian \(G\), put \(g(t)=\mathbb E(1+t^2G^2)^{-1}\).
Every derivative of \(\psi(u)=(1+u^2)^{-1}\) is bounded on the real
line: repeated differentiation gives a rational function without a
real pole that tends to zero at infinity. The integrable bound
\(|G|^j\|\psi^{(j)}\|_\infty\) therefore justifies every derivative
under the expectation, so \(g\in C^\infty(\mathbb R)\). At zero,
\[
 \frac{g^{(2k)}(0)}{(2k)!}
   =(-1)^k\mathbb E G^{2k}=(-1)^k(2k-1)!!,\qquad
 g^{(2k+1)}(0)=0.                                     \tag{6.3}
\]
The even derivative identity follows from the finite geometric expansion
of \((1+u^2)^{-1}\); the Gaussian moment recurrence follows by integration
by parts, as in Section 4. Consecutive nonzero Taylor terms at \(t\ne0\)
have absolute ratio \((2k+1)t^2\), so the Taylor series has radius zero.
Nevertheless the autonomous smooth system
\[
 \dot s=1,\qquad \dot q=g'(s),\qquad s(0)=0,\quad q(0)=1 \tag{6.4}
\]
has the exact solution \(s(t)=t,\ q(t)=g(t)\); integration of the two
equations also proves uniqueness. Its vector field never vanishes,
because its first component is one. Here \(s,q\) are auxiliary scalar
ODE coordinates, not network feature time or backward fields.
Thus failure of analyticity alone is not an obstruction to a smooth
finite-dimensional realization. Conversely, this example does not
supply a network closure, a convergent flow Taylor series, or a
depth- or time-uniform extension of the fixed-program theorem.


---

Source lines 2156–2440

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
 =\frac1n\sum_i \mathscr D_{q_n}^{k}(a_i(z_i^{(2)})^2),
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


---

Source lines 3672–4168

## 10. Positive-metric and Taylor obstructions for the quadratic formal jet

This section uses the one-sample, two-hidden-layer raw-square model of
Section 7.2, with independent standard Gaussian initialization and an
order-one stored readout. It proves two statements about its formal annealed
initialization jet: the negative moment witness persists when every block
has positive mobility, and the canonical positive Taylor closures fail to
converge uniformly on a time interval containing initialization. Neither
statement identifies a positive-time population trajectory.

### 10.1. Model and normalized derivative forests

Take the single input and label to be \(x=y=1\), input dimension \(d=1\),
both hidden widths \(n\), and activation \(\phi(v)=v^2\). Write the stored
parameters as
\[
 W^{(1)}_j=u_j,\qquad W^{(2)}_{ij}=g_{ij}/\sqrt n,
 \qquad W^{(3)}_i=a_i,
\]
where all \(a_i,u_j,g_{ij}\) are independent \(N(0,1)\) initially. Thus
\[
 z_i=\frac1{\sqrt n}\sum_j g_{ij}u_j^2,\qquad
 f_n=\frac1n\sum_i a_i z_i^2
     =\frac1{n^2}\sum_{i,j,l}a_i g_{ij}g_{il}u_j^2u_l^2.
 \tag{10.1}
\]
The mobility multipliers in the stored first, second, and readout blocks
are respectively \(n\alpha,\beta,n\). Equivalently, in the coordinates
\((u,g,a)\), define the feature-ascent derivation
\[
 D_{\alpha,\beta,n}
 =n\left(\nabla_a f_n\cdot\nabla_a
       +\alpha\nabla_u f_n\cdot\nabla_u
       +\beta\nabla_g f_n\cdot\nabla_g\right),
 \qquad \alpha,\beta\ge0.
 \tag{10.2}
\]
Indeed \(\partial_{W^{(2)}}=\sqrt n\,\partial_g\) and
\(dg/ds=\sqrt n\,dW^{(2)}/ds\), giving the stated factor \(n\beta\).
The canonical block metric here is \((\alpha,\beta)=(1,1)\); the frozen
first-block boundary in Section 7.2 is \((0,1)\).

Direct differentiation of (10.1) gives the primitive rules
\[
\begin{aligned}
 D_{\alpha,\beta,n}a_i
   &=\frac1n\sum_{j,l}g_{ij}g_{il}u_j^2u_l^2,\\
 D_{\alpha,\beta,n}u_j
   &=\frac{4\alpha}{n}\sum_{i,l}a_i g_{ij}g_{il}u_j u_l^2,\\
 D_{\alpha,\beta,n}g_{ij}
   &=\frac{2\beta}{n}\sum_l a_i g_{il}u_j^2u_l^2.
\end{aligned}
 \tag{10.3}
\]
No trained variables have been replaced by independent copies in these
identities.

For completeness, define the finite objects to which the forest
factorization applies. Let \(H\) be a finite simple bipartite forest, with
row vertices \(R\), column vertices \(C\), edge set \(E\), \(e=|E|\), and
\(r\) connected components, including isolated vertices. A row \(v\) has
decoration \(p_v\ge0\); a column \(w\) has decoration \(2q_w\ge0\).
Its normalized random sum is
\[
 S_{H,n}=n^{-e/2-r}
 \sum_{i:R\to\{1,\ldots,n\}}
 \sum_{j:C\to\{1,\ldots,n\}}
 \prod_{v\in R}a_{i(v)}^{p_v}
 \prod_{w\in C}u_{j(w)}^{2q_w}
 \prod_{(v,w)\in E}g_{i(v),j(w)}.
 \tag{10.4}
\]
Both maps in these sums are unrestricted. Distinct abstract vertices may
receive the same numerical neuron label. The initial output (10.1) is the
sum for the three-vertex tree with one row of decoration one, two columns
of decoration two, and the two incident edges.

Applying (10.3) and the product rule to (10.4) gives exactly the following
three rewrites.

1. At a row with \(p_v>0\), lower \(p_v\) by one and attach two fresh column
   leaves, each of decoration two, to that row. Multiply by \(p_v\).
2. At a column with \(q_w>0\), retain its decoration, add a fresh row of
   decoration one joined to that column, and join the new row to a fresh
   column of decoration two. Multiply by \(8\alpha q_w\).
3. At an edge \((v,w)\), remove that edge, increase \(p_v\) by one and
   \(2q_w\) by two, and attach a fresh column of decoration two to \(v\).
   Multiply by \(2\beta\).

In the first two cases \(e\) increases by two and \(r\) is unchanged. In the
third case the removed edge is a bridge: \(r\) increases by one, while
removing one edge and adding one leaf edge leaves \(e\) unchanged. Every
result is again a simple forest. In all cases its exponent \(e/2+r\)
increases by one, exactly accounting for \(1/n\) in (10.3). The stated
multiplicities are the ordinary derivatives of the decorations or of the
single edge factor. Numerical coincidences among the summed labels do not
invalidate the product rule; they are included separately in each
unrestricted sum before and after differentiation.

It follows by induction that, for each fixed \(k\),
\(D_{\alpha,\beta,n}^k f_n\) is a finite linear combination of these
normalized forests. The combination is independent of \(n\), and its
coefficients are polynomials in \(\alpha,\beta\) of total degree at most
\(k\), with nonnegative coefficients. This assertion gives a finite
algebraic description; it does not require enumeration of that description.

Here is the expectation argument, also proved in Section 7.2. For a fixed
forest, an odd edge count gives expectation zero by Gaussian symmetry.
If \(e=2b\), expand the expectation of its edge factors into Gaussian
pairings. The pairing formula follows by repeatedly applying
\(E[G P(G)]=E[P'(G)]\) to a Gaussian coordinate; the identity itself is
integration by parts against the Gaussian density for a polynomial \(P\),
whose boundary term vanishes. Pairing two edge occurrences forces equality
of their row labels and equality of their column labels.

Identify those endpoints and replace each pair by one covariance edge.
The resulting multigraph has \(b\) edges, say \(v\) vertices and \(c\)
components. Identifications cannot increase the number of components, so
\(c\le r\). Each connected graph on \(v_0\) vertices has at least \(v_0-1\)
edges: grow its reachable vertex set from one vertex, using one distinct
edge for each new vertex. Summing this bound over components gives
\[
 v\le b+c\le b+r.
 \tag{10.5}
\]
If its two populations have \(v_R,v_C\) vertices, labelings with no further
equality within either population number
\((n)_{v_R}(n)_{v_C}=n^v+O(n^{v-1})\). For those labelings the decoration
expectation is the product of the Gaussian moments at the quotient
vertices. Labelings with an additional equality number \(O(n^{v-1})\),
by choosing an equal pair and then all remaining labels. Their decoration
moments are bounded by a fixed constant, because the total decorations
are fixed. This pairing therefore contributes
\[
 C_H n^{v-b-r}+O(n^{v-b-r-1})
\]
for a fixed nonnegative Gaussian-moment product \(C_H\). There are finitely
many pairings, and (10.5) makes all their exponents nonpositive. Thus
\(E S_{H,n}\) has a finite limit.

Only \(v=b+r\) survives. It forces \(c=r\), so no surviving edge pairing
joins two original components, and each quotient component has one fewer
edge than vertices. The surviving pairings are consequently exactly the
independent choices of surviving pairings for the original components.
Their moments multiply, proving expectation factorization. This proof also
includes isolated vertices and components with odd edge count, which have
no internal complete pairing.

Applying this result to the finite derivative expansion proves existence of
\[
 d_k(\alpha,\beta)
 :=\lim_{n\to\infty}E[D_{\alpha,\beta,n}^k f_n],
 \qquad k\text{ fixed}.
 \tag{10.6}
\]
Each \(d_k\) is a polynomial of total degree at most \(k\) in the two
mobility multipliers. Its coefficients are nonnegative. Also \(d_{2j}=0\):
\(f_n\) has total primitive degree seven, and (10.3) has degree six, so
every nonzero \(k\)-fold derivative has degree \(7+5k\). This degree is
odd for even \(k\); simultaneous Gaussian sign reversal makes its
expectation zero.

The assertions here concern the annealed quantities (10.6), with \(k\)
fixed before the width limit. No concentration assertion, infinite-order
limit exchange, or trajectory-identification statement is used below.

### 10.2. A strictly positive metric with a negative moment witness

Fix \(\beta=1\) and form the formal series
\[
 F_\alpha(s)=\sum_{k\ge0}d_k(\alpha,1)\frac{s^k}{k!}.
\]
The series is odd. At \(\alpha=0\), Section 7.2 proves \(d_1(0,1)=63\).
Polynomial dependence therefore makes \(d_1(\alpha,1)\) nonzero on some
open real interval containing zero. On this interval the formal inverse
\(B_\alpha=F_\alpha^{-1}\) exists. Define the coefficients \(\mu_j(\alpha)\)
by the formal identity
\[
 F_\alpha'(B_\alpha(y))
 =d_1(\alpha,1)+y^2\sum_{j\ge0}(-1)^j\mu_j(\alpha)y^{2j}.
 \tag{10.7}
\]
Oddness of \(F_\alpha\) and uniqueness of its inverse make \(B_\alpha\)
odd, so the composed derivative in (10.7) is even. These definitions use
no convergence of \(F_\alpha\).

To verify the required continuity, write \(a_k=d_k(\alpha,1)/k!\) and
\(B_\alpha(y)=\sum_{k\ge1}b_k y^k\). The coefficient equation for
\(F_\alpha(B_\alpha(y))=y\) is
\[
 b_1=1/a_1,\qquad
 b_k=-\frac1{a_1}[y^k]\sum_{j=2}^k a_j
               \left(\sum_{l=1}^{k-1}b_l y^l\right)^j\quad(k\ge2).
 \tag{10.8}
\]
Only the linear term can involve the unknown \(b_k\), proving this formula
and uniqueness inductively. Thus every fixed \(b_k\), and every fixed
\(\mu_j\) obtained by substitution in (10.7), is a rational function of
finitely many \(a_k\), whose possible denominators are powers of \(a_1\).
In particular \(\mu_1,\ldots,\mu_5\) are continuous near \(\alpha=0\),
using only the jet through \(d_{13}\).

The exact boundary calculation in Section 7.2, equations (7.C3)--(7.C11),
supplies the fixed polynomial
\[
 p(\lambda)=v_0+v_1\lambda+\lambda^2,\qquad
 v_0=\frac{40042013405871059816}{2310453239160606810795},\quad
 v_1=-\frac{14165989123115588}{49896409440894219}.
 \tag{10.9}
\]
If \(L_\alpha(\lambda^j)=\mu_j(\alpha)\), its boundary value is
\[
 L_0(\lambda p(\lambda)^2)
 =-\frac{673792679642733430835456936384}
 {329714727520793070279653295504327135}<0.
 \tag{10.10}
\]
This is the sole finite numeric certificate used here. The complete
boundary dependency is Section 7.2 from (7.C1) through (7.C11): its exact
frozen-row reduction, Gaussian-moment limit, monomial recurrence, formal
reversion, six moments, and witness multiplication. The existing
`pde.exact_calculus.quadratic_axis_certificate()` regenerates that
calculation from its monomial rule, without reading retained arrays.

The function
\(L_\alpha(\lambda p^2)=\sum_{i,j=0}^2v_i v_j\mu_{i+j+1}(\alpha)\),
with \(v_2=1\), is continuous at zero. Its strictly negative value in
(10.10) implies that some \(\varepsilon\in(0,1)\) satisfies
\[
 L_\alpha(\lambda p^2)<0\qquad(0\le\alpha<\varepsilon).
 \tag{10.11}
\]
For any nonnegative measure \(\nu\) on \([0,\infty)\) representing all
these formal moments, the same expression would be
\(\int\lambda p(\lambda)^2\,\nu(d\lambda)\ge0\). It is finite because
only moments through degree five occur. This contradiction proves that
every metric \((\alpha,1)\), \(0<\alpha<\varepsilon\), fails this
Stieltjes moment representation while all three blocks train.

The interval is existential. This proof supplies neither a numerical
endpoint nor a sharp transition. It does not settle the unit metric
\((1,1)\), and a negative formal moment witness is not nonexistence of a
nonlinear population evolution.

### 10.3. Factorial growth at the canonical metric

Now fix \((\alpha,\beta)=(1,1)\) and set
\[
 c_k=\frac{d_k(1,1)}{k!}.
 \tag{10.12}
\]
These coefficients exist by (10.6), are nonnegative, and vanish for even
\(k\). We will prove, for odd \(k\ge1\) and \(m=(k+3)/2\),
\[
 c_k\ge m!\,4^{-m}6^{k+1}\binom{k+2}{2}.
 \tag{10.13}
\]
This is derived directly in the raw-square coordinates (10.1); there is no
change of activation, initialization, or metric convention.

Let \(D_{0,1,n}\) be the frozen-first-block derivation and
\(D_{u,n}=n\nabla_u f_n\cdot\nabla_u\) its omitted first-block term.
In the independent
primitive coordinates, \(f_n\) and every component of (10.3) have
nonnegative polynomial coefficients. Each block derivation preserves this
cone: differentiating a monomial multiplies by a nonnegative exponent, and
its replacement component has nonnegative coefficients. Expanding
\((D_{0,1,n}+D_{u,n})^k\) into its ordered words retains
\(D_{0,1,n}^k\) as one word, with every other word in the same cone after
application to \(f_n\). Independence and Gaussian symmetry give
nonnegative expectation to every monomial in the cone. Consequently
\[
 E[D_{1,1,n}^k f_n]\ge E[D_{0,1,n}^k f_n].
 \tag{10.14}
\]
This is an expectation comparison of polynomial histories, not a
componentwise comparison of trained trajectories.

In the frozen system put \(q_n=n^{-1}\sum_j u_j^4\). Equations (10.3)
give exactly
\[
 a_i'=z_i^2,\qquad z_i'=2q_n a_i z_i,\qquad q_n'=0.
\]
For fixed \(q\ge0\), let
\[
 \mathscr D_q=z^2\partial_a+2qaz\partial_z,\qquad
 P_k(a,z;q)=\frac1{k!}\mathscr D_q^k(az^2).
 \tag{10.15}
\]
Repeated chain rule gives
\(D_{0,1,n}^k f_n/k!=n^{-1}\sum_iP_k(a_i,z_i;q_n)\).
Conditionally on \(u\), the pairs \((a_i,z_i)\) are independent with law
\(N(0,1)\otimes N(0,q_n)\). The conditional expectation of this average is
therefore a fixed polynomial in \(q_n\), because \(P_k\) is a polynomial
in \(a,z,q\) and the Gaussian moments of \(z\) are zero or a constant
times an integer power of \(q_n\).

All fixed polynomial moments of \(q_n\) converge to those of \(3\).
Indeed \(E(q_n-3)^2=\operatorname{Var}(u_1^4)/n\to0\). For each integer
\(b\ge1\), convexity gives \(E q_n^{2b}\le E|u_1|^{8b}<\infty\).
The factorization of \(x^b-3^b\) yields
\[
 |x^b-3^b|\le b|x-3|\max(x,3)^{b-1}\quad(x\ge0).
\]
Cauchy--Schwarz with the preceding bounds proves
\(E|q_n^b-3^b|\to0\). Applying this to the finitely many powers in the
conditional polynomial proves
\[
 \lim_{n\to\infty}\frac{E[D_{0,1,n}^k f_n]}{k!}
 =E[P_k(A,Z;3)],\qquad
 A\sim N(0,1),\quad Z\sim N(0,3),\quad A\perp Z.
 \tag{10.16}
\]
Together with (10.14) and existence of (10.12), this gives
\(c_k\ge E[P_k(A,Z;3)]\).

For fixed \(q>0\), the monomial rule
\[
 \mathscr D_q(a^p z^l)
 =p a^{p-1}z^{l+2}+2ql a^{p+1}z^l
 \tag{10.17}
\]
shows that \(P_k\) has nonnegative coefficients and total degree \(k+3\)
in \(a,z\). The exponent of \(z\) remains even, and each derivative flips
the parity of the exponent of \(a\). For odd \(k\),
\[
 P_k(a,z;q)=\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v},
 \qquad p_{uv}(q)\ge0.
 \tag{10.18}
\]
The ray \(z=\sqrt{2q}\,a\) is invariant under (10.15): both equations
reduce to \(a'=2qa^2\). Starting from \(a(0)=1\), direct substitution
gives \(a(s)=(1-2qs)^{-1}\) and
\(az^2=2q(1-2qs)^{-3}\) for \(s<1/(2q)\) near zero. Repeated
chain rule, or differentiating this rational function \(k\) times at zero,
therefore gives
\[
 \sum_{u+v=m}p_{uv}(q)(2q)^v
 =P_k(1,\sqrt{2q};q)
 =(2q)^{k+1}\binom{k+2}{2}.
 \tag{10.19}
\]
This scalar solution is used only to evaluate a polynomial identity at
initialization.

For independent \(A\sim N(0,1)\), \(Z_q\sim N(0,q)\), Gaussian
integration by parts gives
\(E A^{2u}=(2u-1)!!\) and \(E Z_q^{2v}=(2v-1)!!q^v\), with
\((-1)!!=1\). Each factor \(2j-1\ge j\) gives
\((2u-1)!!\ge u!\), including \(u=0\). Since
\(\binom m u\le\sum_{j=0}^m\binom m j=2^m\),
\[
\begin{aligned}
 E[A^{2u}Z_q^{2v}]
 &\ge u!v!q^v
 \ge m!2^{-m}q^v
 \ge m!4^{-m}(2q)^v,
 \qquad u+v=m.
\end{aligned}
 \tag{10.20}
\]
The last inequality uses \(v\le m\). Multiply (10.20) by the
nonnegative \(p_{uv}(q)\), sum, and use (10.19) at \(q=3\). Equations
(10.14)--(10.16) give exactly (10.13).

The factorial lower bound implies
\[
 \limsup_{k\to\infty}c_k^{1/k}=\infty.
 \tag{10.21}
\]
No asymptotic factorial formula is needed: for \(m\ge2\), the last
\(\lfloor m/2\rfloor\) factors of \(m!\) are at least \(m/2\), so
\((m!)^{1/k}\ge(m/2)^{\lfloor m/2\rfloor/k}\to\infty\) along the
odd \(k\), since \(m=(k+3)/2\). The \(k\)-th root of
\(4^{-m}6^{k+1}\) tends to \(3>0\), and the binomial factor is at least
one. Thus the formal series \(\sum c_k s^k\) has radius zero: at every
\(s>0\) its terms fail to tend to zero along the odd subsequence.

### 10.4. The prescribed Taylor losses are not uniformly Cauchy

The physical loss is the full squared error \(\mathcal L_n=(1-f_n)^2\),
without a factor \(1/2\). At finite width its negative metric gradient is
exactly \(2(1-f_n)\) times the feature-ascent vector field. Accordingly,
whenever a finite-width feature orbit is being followed, its physical
clock obeys \(ds/dt=2(1-f_n)\). This finite identity motivates the same
clock for a prescribed formal Taylor model, but does not identify the
formal model with a width limit.

For \(M\ge1\), define the deterministic polynomial
\[
 F_M(s)=\sum_{k=0}^M c_k s^k.
 \tag{10.22}
\]
Here \(c_0=0\), and \(c_1\ge63>0\): the frozen first derivative has
expectation \(E[Z^4+12A^2Z^2]=27+36=63\), and (10.14) applies.
Thus \(F_M(0)=0\), \(F_M'(s)\ge c_1\) for \(s\ge0\), and \(F_M(s)\)
tends to infinity as \(s\to\infty\). For \(y\in(0,1]\), denote by
\(r_M(y)>0\) its unique positive solution to \(F_M(r_M(y))=y\).

The residual clock and its output are
\[
 \tau_M'=2(1-F_M(\tau_M)),\quad \tau_M(0)=0,
 \qquad f_M(t)=F_M(\tau_M(t)),\quad
 \mathcal L_M(t)=(1-f_M(t))^2.
 \tag{10.23}
\]
These define a global continuous loss. To establish this directly, put
\(r=r_M(1)\) and
\[
 T_M(s)=\int_0^s\frac{dv}{2(1-F_M(v))},\qquad 0\le s<r.
\]
It is continuously differentiable, strictly increasing, and \(T_M(0)=0\).
If \(B=\max_{[0,r]}F_M'<\infty\), then
\(1-F_M(v)\le B(r-v)\). Consequently \(T_M(s)\to\infty\) as
\(s\uparrow r\), by the divergent integral of \(1/(r-v)\). Its inverse
is a differentiable function \(\tau_M:[0,\infty)\to[0,r)\) satisfying
(10.23). Separation of variables proves uniqueness while \(\tau_M<r\);
the same divergent integral prevents reaching \(r\) in finite time. In
particular \(0\le f_M(t)<1\), \(f_M\) is increasing, and
\(\mathcal L_M(0)=1\).

Equivalently this is precisely the polynomial source model
\[
 \partial_tU_M(t,s)=2(1-U_M(t,0))\partial_sU_M(t,s),\qquad
 U_M(0,s)=F_M(s),\qquad U_M(t,s)=F_M(s+\tau_M(t)).
 \tag{10.24}
\]
Substitution proves the PDE and its trace \(U_M(t,0)=f_M(t)\). Within
polynomials of degree at most \(M\), setting \(u_j(t)=\partial_s^jU_M(t,0)\)
gives the finite system \(u_j'=2(1-u_0)u_{j+1}\) for \(j<M\),
\(u_M'=0\), and \(u_j(0)=j!c_j\). Its right side is polynomial and
Lipschitz on every bounded set, as follows from its bounded Jacobian
there. For two solutions with identical initial data on a common compact
time interval, their difference \(e(t)\) therefore satisfies
\(\|e(t)\|\le C\int_0^t\|e(v)\|\,dv\). Set
\(V(t)=\int_0^t\|e(v)\|\,dv\); then
\((e^{-Ct}V(t))'\le0\), while \(V(0)=0\) and \(V\ge0\).
Thus \(V=0\) and the solutions agree. Formula
(10.24) supplies the global solution of this finite prescribed family.

By positivity and (10.21), for every fixed \(s>0\),
\[
 F_M(s)\longrightarrow+\infty\quad(M\to\infty).
 \tag{10.25}
\]
Indeed the partial sums are nondecreasing in \(M\), and some individual
terms \(c_k s^k\) become arbitrarily large. Thus \(r_M(y)\to0\) for each
\(y\in(0,1)\): given \(s>0\), (10.25) eventually gives \(F_M(s)>y\),
which forces \(r_M(y)<s\).

The physical time at which (10.23) reaches \(y\) is
\[
 t_M(y)=T_M(r_M(y))
 \le\frac{r_M(y)}{2(1-y)}\longrightarrow0.
 \tag{10.26}
\]
The inequality uses \(F_M(v)\le y\) on that integration interval. For
each fixed \(t>0\), monotonicity then implies \(f_M(t)\ge y\) for all
sufficiently large \(M\). Letting \(y\uparrow1\), while \(f_M(t)<1\),
proves
\[
 \mathcal L_M(0)=1,\qquad
 \lim_{M\to\infty}\mathcal L_M(t)=0\quad(t>0).
 \tag{10.27}
\]

For every \(T>0\), these continuous losses are not uniformly Cauchy on
\([0,T]\). Otherwise pointwise completeness of the real numbers and the
uniform Cauchy property would give a uniform limit there. A uniform limit
of continuous functions is continuous: approximate it within one third
of a requested tolerance by one fixed member, and use continuity of that
member. But (10.27) fixes its putative limit to be discontinuous at zero.

This also rules out the following precise common-target shadowing claim,
without assuming existence of a limiting network curve. For arbitrary
random comparison curves \(H_n\) for which the expectations below are
defined, let
\[
 d_T(g,h)=\min\{1,\sup_{0\le t\le T}|g(t)-h(t)|\}.
\]
If \(\lim_{M\to\infty}\limsup_{n\to\infty}E d_T(\mathcal L_M,H_n)=0\),
then the metric triangle inequality would imply
\[
 d_T(\mathcal L_M,\mathcal L_{M'})
 \le\limsup_n E d_T(\mathcal L_M,H_n)
    +\limsup_n E d_T(H_n,\mathcal L_{M'})\longrightarrow0
\]
as \(M,M'\to\infty\). This would make the family uniformly Cauchy,
a contradiction. In particular the prescribed iterated shadowing claim
cannot hold with finite-width network losses as \(H_n\).

The order of limits throughout is fixed derivative order, then width,
then Taylor truncation order. The result concerns this positive polynomial
family and uniform error on intervals containing zero. It does not analyze
a coupled order \(M=M(n)\), establish an actual network step loss, or
exclude other finite descriptions using signed or non-Taylor constructions.
