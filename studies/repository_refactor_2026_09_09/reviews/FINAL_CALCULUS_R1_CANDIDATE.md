# Finite contraction, observable and physical-loss calculus

Candidate fragments for the Gaussian-calculus, finite-dynamics and linear
comparison chapters. The mathematical statements below are self-contained.
The interfaces in the last section are proposals; no implementation is
represented as already accepted.

## A. Weighted derivative trees in a constant metric

Let \(f:U\to\mathbb R\), where \(U\subset\mathbb R^d\) is open, let
\(M\) be a constant symmetric positive semidefinite \(d\times d\) matrix,
and put \(D=(M\nabla f)\cdot\nabla\). For an unrooted finite tree \(T\),
define \(C_T(f,M)\) by placing \(\nabla^{\deg(v)}f\) at vertex \(v\),
placing \(M\) on each edge, and summing the two incident tensor indices
against that matrix. A one-vertex tree means \(f\), including its rank-zero
tensor. Explicitly, give each incident vertex-edge pair an index in
\(\{1,\ldots,d\}\), multiply the indicated tensor entries and edge entries,
and sum every index. Tensor symmetry makes this independent of the ordering
of edges at a vertex. This is a scalar contraction in parameter space;
vertices do not denote neurons or Gaussian sources.

For \(k\ge0\) and \(f\in C^{k+1}(U)\),
\[
 D^kf=\sum_{|T|=k+1}w_k(T)C_T(f,M).                         \tag{A1}
\]
The integer weights have a finite constructive definition. Start with the
one-vertex tree of weight one. From every weighted tree attach one new leaf
at each of its vertices, carrying its old weight to each resulting tree;
then add weights of isomorphic unrooted trees. Every vertex is counted,
including vertices in the same symmetry orbit.

To prove (A1), differentiate one contraction. The matrix factors are
constant. Hitting the tensor at vertex \(v\) raises its derivative order by
one; contraction of the new index with \(M\nabla f\) attaches exactly one
leaf at \(v\). The product rule sums precisely over all vertices. Induction
proves both the identity and the weight recursion. Every tree occurs,
because repeatedly removing a leaf reduces it to the singleton. The sum of
the weights at order \(k\) is \(k!\): an order-\(k\) tree has \(k+1\)
possible next attachments. For example, at order three the four-vertex
star and path have weights two and four; at order five the six weights,
as a multiset, are \(2,14,16,22,30,36\).

Canonicalization can use the lexicographically least rooted parenthesis
code over every root, sorting child codes recursively. Equal rooted codes
give an isomorphism by matching child subtrees inductively; taking minima
proves the unrooted assertion. Thus this recursion computes coefficients,
not just abstract shape counts. It terminates at every prescribed finite
order. No estimate on its high-order cost, width limit or Taylor radius is
part of (A1). For a state-dependent metric an additional derivative of every
metric factor would be necessary, so (A1) is not that formula.

## B. Normalized Gaussian forests: exact evaluation and concentration

For each \(n\ge1\), take mutually independent standard real Gaussians
\(a_i,u_j,g_{ij}\), \(1\le i,j\le n\). Row and column indices belong to
different populations, even when they have the same numerical label. A
decorated simple bipartite forest \(H\) has row decorations \(p_v\ge0\),
column decorations \(q_w\ge0\), \(e\) edges and \(r\) components, including
isolated vertices. Define
\[
 S_{H,n}=n^{-e/2-r}\sum_{i:R\to[n],\ j:C\to[n]}
   \prod_{v\in R}a_{i(v)}^{p_v}
   \prod_{w\in C}u_{j(w)}^{q_w}
   \prod_{(v,w)\in E}g_{i(v),j(w)}.                         \tag{B1}
\]
The label maps are unrestricted. The empty forest has value one. All
forests, exponents and finite lists in this section are fixed before
\(n\to\infty\).

Write \(m(b)=0\) for odd \(b\), \(m(0)=1\), and
\(m(2b)=(2b-1)!!\). These are Gaussian moments: integration by parts against
\(e^{-x^2/2}\) gives \(m(b)= (b-1)m(b-2)\), with zero boundary term and
odd moments zero by reflection.

An exact finite-width evaluator needs only equality partitions. Enumerate
all set partitions \(\pi_R,\pi_C\) of the row and column vertices. For a
row block \(A\), let \(p_A=\sum_{v\in A}p_v\); define \(q_B\) similarly.
Let \(e_{AB}\) count raw edges between blocks \(A,B\). With
\((n)_b=n(n-1)\cdots(n-b+1)\), and \((n)_0=1\),
\[
 \mathbb E S_{H,n}=n^{-e/2-r}
 \sum_{\pi_R,\pi_C}(n)_{|\pi_R|}(n)_{|\pi_C|}
 \prod_A m(p_A)\prod_Bm(q_B)\prod_{A,B}m(e_{AB}).            \tag{B2}
\]
Indeed, each labeling has a unique equality partition. Assigning distinct
labels to its blocks has the displayed falling-factorial count. All
remaining factors are independent Gaussians of the indicated powers.
This proves (B2), including \(n\) smaller than the number of blocks.

There is a more economical leading evaluator. If \(e\) is odd, the edge
expectation is zero. Otherwise put \(e=2b\) and pair the labeled edge
occurrences by Gaussian integration by parts. Each pair identifies both
row endpoints and both column endpoints. Replace each pair by a covariance
edge. The quotient multigraph has \(b\) edges, say \(v\) vertices and \(c\)
components. Identifications cannot increase component count, and each
connected graph on \(v_0\) vertices needs at least \(v_0-1\) edges. Hence
\[
 v\le b+c\le b+r.                                        \tag{B3}
\]
For that pairing, labelings with no further equalities number
\(n^v+O(n^{v-1})\); extra equalities number \(O(n^{v-1})\). Their decoration
moments are bounded constants, since all degrees are fixed. After
normalization the contribution is \(O(n^{v-b-r})\), so it never diverges.
Its limit survives only when \(v=b+r\). Equality in (B3) then forces
\(c=r\): no leading pairing joins original components, and every quotient
component is a tree. Consequently
\[
 \chi(H):=\lim_n\mathbb ES_{H,n}
       =\prod_{C\text{ component of }H}\chi(C).             \tag{B4}
\]
A component with an odd number of edges has value zero. Isolates contribute
their scalar Gaussian moment.

For a connected component with \(2b\) edges, one can instead enumerate
exactly the bipartition-respecting vertex partitions with \(b+1\) total
blocks and every occupied cell containing two raw edges. Each such
partition determines one edge pairing, namely pairing the two occurrences
in each cell. Conversely a leading paired quotient is a tree: a parallel
covariance edge would create a cycle, so its occupied cells have precisely
two raw edges. Its vertex identifications are the stated partition. For
completeness, the identifications forced by its cell pairs cannot define
a finer partition: that would have more than \(b+1\) vertices in a connected
graph with \(b\) covariance edges, contradicting (B3). Multiply the Gaussian
moments of the summed decorations and sum these partitions. This proves
the alternative evaluator, without a rank test over a finite field.

The same identities also supply concentration of these scalar sums. The
exact product identity is
\[
 S_{H,n}S_{J,n}=S_{H\sqcup J,n}.                          \tag{B5}
\]
Use distinct abstract vertices in the union; numerical labels may still
coincide. Normalization exponents add. Repeated use of (B4) therefore gives
\(\mathbb ES_{H,n}^{k}\to\chi(H)^k\) for every integer \(k\ge0\).
Expanding the nonnegative even power gives
\[
 \mathbb E|S_{H,n}-\chi(H)|^{2k}
 =\sum_{j=0}^{2k}{2k\choose j}(-\chi(H))^{2k-j}
                       \mathbb ES_{H,n}^{j}\longrightarrow0.       \tag{B6}
\]
For any finite real \(p\ge1\), choose \(2k\ge p\) and use
\(\mathbb E|X|^p\le(\mathbb E|X|^{2k})^{p/(2k)}\).
Thus every finite linear combination of forest sums converges in every
finite \(L^p\) to the same linear combination of \(\chi(H)\). Products
converge too, by (B5) or Hölder. This proves uniform integrability at each
fixed finite degree, as well as convergence in probability. It makes no
assertion about coordinatewise vector limits or orders growing with width.

## C. Weighted quadratic generator, connected recursion and hidden roots

Take \(d=m=1\), \(x=y=1\), two hidden layers, activations \(z\mapsto z^2\),
stored weights \(u_j,g_{ij}/\sqrt n,a_i\), and the independent Gaussian
initialization in B. Thus the stored readout is order one. Define
\[
 z_i=n^{-1/2}\sum_jg_{ij}u_j^2,\qquad
 f_n=n^{-1}\sum_i a_i z_i^2.
\]
Use feature ascent with block mobilities \(n\alpha,\beta,n\), where
\(\alpha,\beta\ge0\). In the auxiliary coordinates \((u,g,a)\),
\(D=n(\alpha\nabla_u f_n\cdot\nabla_u+
\beta\nabla_g f_n\cdot\nabla_g+\nabla_a f_n\cdot\nabla_a)\).
The primitive identities are
\[
 Da_i=n^{-1}\sum_{j,l}g_{ij}g_{il}u_j^2u_l^2,\quad
 Du_j=4\alpha n^{-1}\sum_{i,l}a_i g_{ij}g_{il}u_ju_l^2,\quad
 Dg_{ij}=2\beta n^{-1}\sum_l a_i g_{il}u_j^2u_l^2.           \tag{C1}
\]

For the forest subalgebra with column decorations \(2q_w\), these give:

* A row hit lowers \(p_v\) by one and attaches two new column leaves,
  each of decoration two; its multiplier is \(p_v\).
* A column hit retains its decoration, adds a new row of decoration one
  joined to that column, and adds a new column leaf of decoration two to
  the new row; its multiplier is \(8\alpha q_w\).
* An edge hit removes the edge, raises its row decoration by one and its
  column decoration by two, and attaches a new column leaf of decoration
  two to that row; its multiplier is \(2\beta\).

New vertices always have new abstract labels. In the first two cases the
edge number increases by two and the component count is unchanged. In the
last case a bridge is deleted and one leaf is attached, so the edge number
is unchanged and the component count increases by one. In every case
\(e/2+r\) increases by one, accounting for the \(1/n\) in (C1).
The product rule proves the rewrites even for labelings where several
abstract vertices have the same numerical index.

Let \(A_k(C;\alpha,\beta)=\chi(D^k S_C)\), with \(C\) connected and
normalized as in (B1). Here \(D^k S_C\) denotes the finite rewrite
combination. Set \(A_0(C)=\chi(C)\). For \(k\ge1\), each row/column hit
gives its stated multiplier times \(A_{k-1}\) of the child tree. Each
edge hit splits the child into \(C_1,C_2\) and contributes
\[
 2\beta\sum_{j=0}^{k-1}{k-1\choose j}
        A_j(C_1;\alpha,\beta)A_{k-1-j}(C_2;\alpha,\beta). \tag{C2}
\]
This is an equality: the remaining derivations distribute by the Leibniz
rule, and their leading expectations factor by (B4). Each call has smaller
remaining derivative order, so the recursion terminates and canonical tree
keys safely memoize it. Polynomial arithmetic in \(\alpha,\beta\) retains
every block grade. Equivalently the coefficient with \(u\)-hit count \(a\)
and edge-hit count \(b\) uses coefficient convolution in both grades in
(C2), with one edge hit already consumed. No commutation of the block
derivations is assumed.

For the output root, initially there is one row of decoration one and two
column leaves of decoration two. After \(k\) derivatives, if the counts of
row, column and edge hits are \(x,y,w\), then
\[
 x+y+w=k,\quad e=2+2(x+y),\quad r=1+w,\quad
 P=e/2=k+1-w,\quad A=1-x+y+w=k+1-2x,\quad
 H=2+2x+y+2w=2k+3+x-P.                                  \tag{C3}
\]
Here \(A\) is total row decoration and \(H\) is half the total column
decoration. These equations follow by adding the changes of each rewrite.
At the unit metric the sum of next-hit multipliers is
\(L=A+8H+2e\). A row, column or edge hit increases \(L\) respectively by
\(19,13,17\), so the exact sum for two ordered further hits is
\[
 A(L+19)+8H(L+13)+2e(L+17)=L^2+19A+104H+34e.              \tag{C4}
\]
This counts rewrite coefficients only; contraction values are not bounded
by this count times the parent's value. For example, an isolated row with
decoration one has expectation zero but its row derivative has leading
expectation three. A zero base expectation is therefore not a valid
derivative-recursion prune.

Safe pruning of a partially paired connected base can use: too few or too
many possible final index classes; a current cell with more than two raw
edges, since further identifications only merge cells; or an odd decoration
in a class which no unpaired edge can ever merge. Each follows directly
from the leading-tree condition. They are conditions on a particular base
contraction, not grounds to delete a derivative prefix. The unrestricted
binary-rank shortcut is false. For rows decorated \((2,1,1)\), columns
decorated \((2,2,2,2)\), and edges
\[
 (0,0),(0,1),(0,2),(0,3),(1,0),(2,0),
\]
the leading equality-partition value is \(27\). In particular the row
partition \(\{0\},\{1,2\}\) and column partition
\(\{0,1\},\{2,3\}\) is a legitimate contribution of \(9\), although
the two row-block parity signatures have rank one. Formula (B2) or the
zero-or-two-cell rule counts it without any rank premise.

The same compiler accepts independent observable roots:
\[
 Q_{1,n}=n^{-1}\sum_j u_j^2,\quad
 Q_{2,n}=n^{-1}\sum_i z_i^2,\quad
 Q^{\rm act}_{1,n}=n^{-1}\sum_j u_j^4,\quad
 Q^{\rm act}_{2,n}=n^{-1}\sum_i z_i^4.                     \tag{C5}
\]
They are respectively an isolated column of decoration two; a two-edge
row star with column decorations two and row decoration zero; an isolated
column of decoration four; and a four-edge row star with all column
decorations two. Their normalizations are exactly (B1). Hence their every
fixed derivative converges in all finite \(L^p\) by B and (C1). The first
two are squared preactivation RMS; the last two are squared activation RMS.
Initially their deterministic limits are \(1,3,3,27\), respectively.

Directly from (C1),
\[
 DQ_{1,n}=8\alpha f_n,\qquad
 D\bigl(n^{-1}\|a\|_2^2\bigr)=2f_n.                     \tag{C6}
\]
For instance \(DQ_1=(2/n)\sum_j u_jDu_j\); insertion of (C1) produces
eight times \(\alpha n^{-2}\sum_{i,j,l}a_i g_{ij}g_{il}u_j^2u_l^2\).
This proves the first identity, and \(Da=z^2\) proves the second. Thus
all fixed derivative limits obey \(Q_1^{(k)}(0)=8\alpha F^{(k-1)}(0)\).
These are feature-clock and coefficient identities; physical full-loss
flow multiplies their right sides by \(-2(f_n-y)\).

## D. A contained quadratic physical-loss width theorem

This section takes both activations to be \(\phi(v)=c v^2\), with fixed
\(c>0\), independent standard \(u,g,a\), stored connector \(g/\sqrt n\),
and mobilities \(n,n,n\) in \((u,g,a)\), equivalently \(n,1,n\) in stored
coordinates. There is one input \(x=1\), one label \(y=1\), and full loss
\(\mathcal L_n=(f_n-1)^2\). The output is \(c^3\) times the raw-square
output in C, and its feature field is \(c^3\) times (C1) at unit metric.
The normalization \(c=1/\sqrt3\) is included.

For every fixed finite sequence of real raw GD steps
\(\eta_0,\ldots,\eta_{N-1}\), the output, squared loss, the four hidden
observables (C5) with their actual \(c\) factors, and the mobility-weighted
kernel converge in probability and every finite \(L^p\) to deterministic
scalars. Explicitly these four observables are
\(n^{-1}\sum u_j^2,\ n^{-1}\sum z_i^2,\ c^2n^{-1}\sum u_j^4,\
c^2n^{-1}\sum z_i^4\), where
\(z_i=c n^{-1/2}\sum_jg_{ij}u_j^2\).
The limit is computed by finite simultaneous substitution in
forests followed by \(\chi\). The same holds for any fixed finite list of
normalized-forest observables. There is no assertion uniform in \(N\).

Here is the complete substitution argument. Use a formal feature step
\(s\). Replace every original factor by its value plus \(s\) times its
primitive field in (C1), multiplied by \(c^3\). Expand powers by the binomial
theorem. For a row factor \(a^p\), choosing \(j\) update factors attaches
\(j\) disjoint pairs of fresh leaves and lowers the old decoration by \(j\),
with multiplier \(\binom pj(sc^3)^j\). For a column factor \(u^{2q}\),
write its update as \(u(1+4sc^3 n^{-1}\sum a g g u^2)\). Choosing \(j\)
update factors attaches \(j\) fresh row/column pairs at that column and
retains its decoration, with multiplier \(\binom{2q}j(4sc^3)^j\).
Each original edge either remains or is replaced by its update gadget,
with multiplier \(2sc^3\). An edge is replaced at most once. All additions
are fresh and every removed original edge was a bridge. The final graph
is therefore a forest. Every selected update factor increases \(e/2+r\)
by one, accounting for its \(1/n\). These statements remain true when
several factors at the same original vertex are selected. Crucially the
newly attached factors are not substituted again within that step: this
is simultaneous Euler, not sequential block updating.

Thus the feature-step pullback of any forest scalar is a finite sum
\[
 S_H\circ E_s^{\rm feat}=\sum_{j=0}^{J}s^j P_{H,j},        \tag{D1}
\]
where each \(P_{H,j}\) is a width-independent finite linear combination
of forests. Raw loss GD is exactly the substitution
\(s=2\eta(1-f_n)\). Since \(f_n\) is a forest scalar, (B5) shows that
every \((1-f_n)^jP_{H,j}\) remains a finite forest combination. Iteration
proves the assertion for the complete loss program. B proves its scalar
limits and all moments, including terminal loss uniform integrability.
The kernel is the feature derivative \(Df_n\), already a finite forest
combination, so the same argument covers it. This proof uses neither an
inverse Gram matrix nor a rank-stability assumption.

Let \(\mathcal F_k(s_0,\ldots,s_{k-1})\) denote the deterministic output
limit for prescribed feature steps. As a polynomial in the steps, its
coefficients are limits of forest scalars. Consequently evaluation at
convergent random scalar steps commutes with the limit: expand its finitely
many monomials and use Hölder and B for their products. The actual loss
limits therefore satisfy exactly
\[
 F_k^{\eta}=\mathcal F_k(s_0,\ldots,s_{k-1}),\qquad
 s_k=2\eta(1-F_k^{\eta}).                                \tag{D2}
\]
This proves the adaptive residual identification, not merely convergence
of expected feature outputs. Also
\(\mathbb E\mathcal L_{n,k}\to(1-F_k^{\eta})^2\), because \(L^2\)
output convergence makes its variance vanish.

### D.1. Width-first loss initial layer for the normalized pure square

Set \(c=1/\sqrt3\). For every \(T>0\), \(0<\delta<1\), and
\(\eta_N=T/N\), define
\[
 \tau_N(\delta)=\eta_N\min\{k:F_k^{\eta_N}\ge\delta\}.
                                                               \tag{D3}
\]
Then \(\tau_N(\delta)\to0\). Width is taken first separately for each
finite loss program, as proved above; only then does \(N\to\infty\).

We prove the required all-order comparison rather than infer it from a
finite Taylor jet. Every finite feature update and the output are
polynomials with nonnegative coefficients in the raw Gaussian variables
and in nonnegative steps. Gaussian expectation annihilates an odd raw
monomial and is positive on an even one. Thus \(\mathcal F_k\) is
coordinatewise nondecreasing on nonnegative schedules. Deleting the first
parameter update retains a coefficientwise sub-polynomial of the fully
trained feature output: composition and addition of polynomials with
nonnegative coefficients preserve coefficientwise order. This comparison
is made before Gaussian expectation; it does not assert a samplewise order
on signed Gaussian states.

For the frozen first layer put \(q_n=n^{-1}\sum_j\phi(u_j)^2\).
Conditionally on \(u\), the rows have independent
\(a_0\sim N(0,1)\), \(z_0\sim N(0,q_n)\), and
\[
 a^+=a+scz^2,\qquad z^+=z+2scq_naz.                       \tag{D4}
\]
Every fixed update output is a polynomial. The empirical mean \(q_n\to1\)
in every finite \(L^p\): expand a centered even moment of an iid average,
where a surviving index occurs at least twice, and count at most half as
many free indices as factors. Jensen gives uniform higher moments. Hence
the frozen expected output converges to (D4) at \(q=1\), with independent
standard \(a_0,z_0\).

Use a constant feature step \(s=\rho/k\) for \(2k\) steps. The largest
step degree of either row coordinate after \(j\) steps is
\(d_j=2^j-1\). Select recursively only the quadratic top-degree terms
\(cz^2,2caz\). Their coefficients are positive integers times \(c^{d_j}\).
Their initial-variable exponent pairs start at \((1,0),(0,1)\), and update
by \((r,s)\mapsto2(u,v)\), \((u,v)\mapsto(r+u,s+v)\).
The selected output \(ca_jz_j^2\) at \(j=2k\) consequently has exponents
\((4^k,2\cdot4^k)\), step degree \(3(4^k-1)\), and coefficient at least
\(c^{3(4^k-1)+1}\). Both exponents are even. Positivity gives
\[
 \mathcal F_{2k}(\rho/k,\ldots,\rho/k)
 \ge c^{3(4^k-1)+1}(\rho/k)^{3(4^k-1)}
                          (4^k/e)^{4^k}\longrightarrow+\infty.   \tag{D5}
\]
Here \(\mathbb EG^{2b}=(2b-1)!!\ge b!\ge(b/e)^b\); the last inequality
follows by integrating \(\log x\) from \(1\) to \(b\). The logarithm of
the displayed bound, divided by \(4^k\), is
\(k\log4-3\log k+O_{c,\rho}(1)\), which tends to infinity.

Before the first \(\delta\)-hit, (D2) has
\(s_j>2(1-\delta)\eta_N\). Fix \(0<\varepsilon<T\), put
\(k_N=\lfloor\varepsilon/(2\eta_N)\rfloor\), and choose
\(\rho=(1-\delta)\varepsilon/2\). Eventually
\(\rho/k_N\le2(1-\delta)\eta_N\). If no hit occurred by \(2k_N\),
schedule monotonicity and (D5) would give \(F_{2k_N}^{\eta_N}\to+\infty\),
contradicting \(F_{2k_N}^{\eta_N}<\delta\). Thus
\(\tau_N(\delta)\le\varepsilon\) eventually, proving (D3).

The initial output limit is zero. Any continuous interpolation of these
grid predictors crosses \(\delta\) at times tending to zero and therefore
cannot converge uniformly on \([0,T]\) to a continuous initialized
predictor. The same obstruction holds for the squared loss evaluated from
that continuous predictor: at a crossing it equals \((1-\delta)^2\ne1\).
In particular this applies to raw-parameter interpolation followed by
recomputation, whose fixed-cell limit is a finite polynomial in the cell
fraction by (D1), and to polygonal predictor interpolation followed by
squaring. It does not assert the same crossing identity for independently
polygonally interpolated loss values after an arbitrarily large overshoot.

No post-hit comparison is used: residuals can change sign there. Thus this
theorem gives no terminal fine/coarse loss limit, no finite-width GF initial
layer, and no assertion for an arbitrary joint \(N=N(n)\) diagonal.

## E. Reusable finite depth jets and observable heads

Fix finite \(L,m,d,n\), arbitrary deterministic data \((x_a,y_a)\), and
the stored-weight model and full mean loss
\(\mathcal L_n=m^{-1}\sum_a(f_{n,a}-y_a)^2\). For this subsection only,
\([k]\) denotes the ordinary coefficient of \(t^k\), not a derivative.
Given coefficients of a scalar series \(z\), define
\[
 [\phi^{(r)}(z)]_{[k]}=
 \sum_{b=0}^{k}\frac{\phi^{(r+b)}(z_{[0]})}{b!}
 \sum_{i_1+\cdots+i_b=k,\ i_j\ge1}
             z_{[i_1]}\cdots z_{[i_b]}.                  \tag{E1}
\]
The inner sum for \(b=0\) is one for \(k=0\) and zero otherwise.
Use coordinatewise multiplication in (E1). At each degree \(k\), compute
\[
 \begin{aligned}
 z^{(1)}_{a,[k]}&=W^{(1)}_{[k]}x_a/\sqrt d,\\
 z^{(\ell)}_{a,[k]}&=\sum_{i+j=k}W^{(\ell)}_{[i]}
                                      h^{(\ell-1)}_{a,[j]},\\
 h^{(\ell)}_{a,[k]}&=[\phi^{(\ell)}(z^{(\ell)}_a)]_{[k]},\\
 \delta^{(L)}_{a,[k]}&=\sum_{i+j=k}W^{(L+1)}_{[i]}
                           \odot[(\phi^{(L)})'(z^{(L)}_a)]_{[j]},\\
 b^{(\ell)}_{a,[k]}&=\sum_{i+j=k}(W^{(\ell+1)}_{[i]})^T
                                            \delta^{(\ell+1)}_{a,[j]},\\
 \delta^{(\ell)}_{a,[k]}&=\sum_{i+j=k}
       [(\phi^{(\ell)})'(z^{(\ell)}_a)]_{[i]}\odot b^{(\ell)}_{a,[j]},\\
 f_{a,[k]}&=n^{-1}\sum_{i+j=k}(W^{(L+1)}_{[i]})^Th^{(L)}_{a,[j]},
 \qquad r_{a,[k]}=f_{a,[k]}-y_a\mathbf1_{k=0}.
 \end{aligned}                                                   \tag{E2}
\]
The forward degrees are computed bottom to top, and the reverse degrees
top to bottom, always using the actual transpose. With block mobilities
\(n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}\), integrate
the exact physical field coefficientwise:
\[
 \begin{aligned}
 W^{(1)}_{[k+1]}&=-\frac{2\kappa_1}{m(k+1)\sqrt d}
             \sum_a\sum_{i+j=k}r_{a,[i]}\delta^{(1)}_{a,[j]}x_a^T,\\
 W^{(\ell)}_{[k+1]}&=-\frac{2\kappa_\ell}{mn(k+1)}
     \sum_a\sum_{i+j+b=k}r_{a,[i]}\delta^{(\ell)}_{a,[j]}
                                         (h^{(\ell-1)}_{a,[b]})^T,\\
 W^{(L+1)}_{[k+1]}&=-\frac{2\kappa_{L+1}}{m(k+1)}
             \sum_a\sum_{i+j=k}r_{a,[i]}h^{(L)}_{a,[j]}.
 \end{aligned}                                                   \tag{E3}
\]
Equations (E1)–(E3) form a triangular finite derivative algorithm through
any prescribed positive integer order \(q\), provided every activation is \(C^{q+1}\) near
the supplied finite state. For example one may restrict the implementation
to \(q\le5\); order zero simply returns the supplied state.
A finite \(C^1\) field has a local solution by contraction of
its integral equation on a small bounded ball; repeated differentiation
gives the stated finite jets. Taylor's finite composition rule proves (E1),
ordinary products prove (E2), and comparing \(t^k\) coefficients in the
raw gradient equations proves (E3). This establishes every factor of
\(n,m,k+1\). It imposes no distributional initialization, data orthogonality
or population limit. It is a finite derivative algorithm, not time stepping
by a truncated series.

The same stored parameter jets can serve any \(C^q\) observable \(O\):
substitute the finite series in its multivariate Taylor polynomial. Writing
\(v=\dot\theta\), \(p_1=D_vv,p_2=D_v^2v,p_3=D_v^3v\), the first four
derivatives are
\[
 \begin{aligned}
 O'&=O_1[v],\\
 O''&=O_2[v,v]+O_1[p_1],\\
 O'''&=O_3[v,v,v]+3O_2[v,p_1]+O_1[p_2],\\
 O^{(4)}&=O_4[v,v,v,v]+6O_3[v,v,p_1]+3O_2[p_1,p_1]
                              +4O_2[v,p_2]+O_1[p_3].
 \end{aligned}                                                   \tag{E4}
\]
These follow by differentiating the preceding line and using symmetry of
the derivative tensors. They reuse parameter derivatives but do not claim
that averaged observable contractions have a fixed scalar closure.

For either an activation or a preactivation vector \(X(t)\), now use actual
derivatives \(X_j=X^{(j)}(0)\). Its squared RMS \(Q=\|X\|_2^2/n\) has
\[
 Q^{(k)}(0)=\sum_{j=0}^k{k\choose j}\Gamma_{j,k-j},\quad
 \Gamma_{ij}=X_i^TX_j/n;\qquad
 Q''=2\Gamma_{02}+2\Gamma_{11},\quad
 Q^{(4)}=2\Gamma_{04}+8\Gamma_{13}+6\Gamma_{22}.            \tag{E5}
\]
Product differentiation proves this exactly. For a hidden affine map
\(z=W h\), the fourth moving derivative is
\[
 z_4=W h_4+4W_1h_3+6W_2h_2+4W_3h_1+W_4h_0,
\]
and the activation derivative is
\[
 h_4=\phi^{(4)}(z)z_1^4+6\phi'''(z)z_1^2z_2
                   +3\phi''(z)z_2^2+4\phi''(z)z_1z_3+\phi'(z)z_4. \tag{E6}
\]
Each product here is coordinatewise. A straight parameter line freezes the
direction and sets its higher parameter derivatives to zero; the moving
flow generally does neither. Thus its fourth contraction must be computed
by (E2)–(E6), not borrowed from a straight-line fourth derivative.

For feature ascent of one scalar predictor with constant block metric,
readout reflection \(S\) satisfies \(f(S\theta)=-f(\theta)\) and
\(v(S\theta)=-Sv(\theta)\). Uniqueness of the finite local ODE gives
\(\theta(s;S\theta_0)=S\theta(-s;\theta_0)\). Hidden vectors are
unchanged by \(S\) at a fixed state, so their \(j\)-th jets change by
\((-1)^j\). Under a reflection-invariant initial law with the requisite
finite moments, odd annealed hidden Gram derivatives vanish and the
annealed output jet is odd. Neither vanishing statement is seedwise.

For a deterministic even coefficient germ
\(Q(s)=q_0+q_2s^2/2+q_4s^4/24+\cdots\), \(q_0>0\), its formal RMS is
\[
 (\sqrt Q)''(0)=q_2/(2\sqrt{q_0}),\qquad
 (\sqrt Q)^{(4)}(0)=q_4/(2\sqrt{q_0})-3q_2^2/(4q_0^{3/2}). \tag{E7}
\]
Squaring the Taylor polynomial proves this; more generally its ordinary
coefficients satisfy \(r_0=\sqrt{q_0}\),
\(r_k=(q_{[k]}-\sum_{i=1}^{k-1}r_i r_{k-i})/(2r_0)\).
This is the square root of a deterministic coefficient germ. It is not an
exchange of square root with annealed expectation of finite-width jets.

If \(F\) is an odd deterministic germ with \(F'(0)=A,F'''(0)=B\), define
the label-one full-loss formal clock \(s'=2(1-F(s)),s(0)=0\).
With a general constant \(c_0\) in place of \(2\), substitution gives
\(s_1=c_0,s_2=-c_0^2A,s_3=c_0^3A^2,
s_4=-c_0^4(A^3+B)\). Inserting these into \(Q(s(t))\) gives
\[
 Q_t''=c_0^2q_2,\quad Q_t'''=-3c_0^3Aq_2,\quad
 Q_t^{(4)}=c_0^4(q_4+7A^2q_2),\quad
 Q_t^{(5)}=-5c_0^5\{(3A^3+B)q_2+2Aq_4\}.                 \tag{E8}
\]
For example the \(s^2\) coefficient at order five is
\(-c_0^5(3A^3+B)/12\), and the \(s^4\) coefficient is
\(-2c_0^5A\), proving the last line after the factorial factors. These
are finite formal identities after any needed coefficient limits; they
do not make loss GD an exact constant-step feature scheme.

### E.1. A local Gaussian fourth-order hidden head

Supply a centered jointly Gaussian vector \((Z,U_1,U_2,U_3,U_4)\),
with \(\mathbb EZ^2=1\), a centered jointly Gaussian vector
\((V_0,V_1,V_2,V_3)\) independent of the first, and their full positive
semidefinite covariance matrices. Degenerate matrices are allowed.
Supply constants \(\lambda_1,\lambda_2,\lambda_{30},\lambda_{32},
\lambda_{41},\lambda_{43},c_{10},d_{21},d_{30},d_{32}\).
For an actual expectation assume \(\phi\) is polynomial, or smooth with
polynomial bounds for all derivatives used below. The polynomial case
already gives a complete exact finite contract. Put \(p_j=\phi^{(j)}(Z)\)
and define, in order,
\[
\begin{aligned}
d_0&=p_1V_0,&z_1&=U_1+\lambda_1d_0,&h_0&=p_0,&h_1&=p_1z_1,\\
r_1&=V_1+c_{10}h_0,&
d_1&=p_2z_1V_0+p_1r_1,&z_2&=U_2+\lambda_2d_1,\\
h_2&=p_2z_1^2+p_1z_2,&r_2&=V_2+d_{21}h_1,\\
d_2&=p_3z_1^2V_0+p_2z_2V_0+2p_2z_1r_1+p_1r_2,\\
z_3&=U_3+\lambda_{30}d_0+\lambda_{32}d_2,&
h_3&=p_3z_1^3+3p_2z_1z_2+p_1z_3,\\
r_3&=V_3+d_{30}h_0+d_{32}h_2,\\
d_3&=p_4z_1^3V_0+3p_3z_1z_2V_0+p_2z_3V_0
       +3p_3z_1^2r_1+3p_2z_2r_1+3p_2z_1r_2+p_1r_3,\\
z_4&=U_4+\lambda_{41}d_1+\lambda_{43}d_3,\\
h_4&=p_4z_1^4+6p_3z_1^2z_2+3p_2z_2^2+4p_2z_1z_3+p_1z_4 .
\end{aligned}                                                    \tag{E9}
\]
These are a finite directed algebra. The \(h_j\) are the literal Bell
polynomials for the \(j\)-th derivative of \(\phi(z(s))\) with supplied
jets \(z_j\); the \(d_j\) are the product derivatives of
\(\phi'(z(s))r(s)\), with \(r(0)=V_0\) and the supplied \(r_j\).
This proves every integer coefficient in (E9). The additional linear
rules defining \(z_j,r_j\) are explicit inputs to this local model;
their origin in a trained network is not presumed.

The observable and response outputs are
\[
 \gamma_{\rm out}=\mathbb E[h_0h_4],\qquad
 A_{41,\rm out}=\mathbb E[\partial_{V_1}h_4],\qquad
 A_{43,\rm out}=\mathbb E[\partial_{V_3}h_4].               \tag{E10}
\]
These partial derivatives hold all other Gaussian coordinates and supplied
constants fixed, before expectation. They are not derivatives of covariance
data or of a trained trajectory. The additional Gram outputs
\(\mathbb Eh_1h_3,\mathbb Eh_2^2\) combine with \(\gamma_{\rm out}\)
by (E5) to give the local fourth squared-RMS head.

All Gaussian eliminations have a finite constructive proof. For a
non-\(Z\) Gaussian coordinate \(X\), remove one factor from a monomial
\(XP\) and use
\[
 \mathbb E[XP]=\sum_Y\operatorname{Cov}(X,Y)
                                  \mathbb E[\partial_Y P].       \tag{E11}
\]
The sum includes \(Z\); its partial derivative replaces one \(p_j\)
factor by \(p_{j+1}\), with multiplicity. Other partials remove a
Gaussian factor. Write the full Gaussian vector as a deterministic linear
image of independent standard Gaussians and integrate each density by
parts to prove (E11). Polynomial bounds kill all boundary terms; no
covariance inverse is used, so singular matrices are included.
Every recursion removes at least one non-\(Z\) factor and terminates at
\[
 M_{k_0,\ldots,k_J}
 =\mathbb E\prod_{j=0}^J\phi^{(j)}(Z)^{k_j}.               \tag{E12}
\]
For polynomial \(\phi\), expansion and B evaluate these atoms exactly.
Otherwise they are explicit one-dimensional integrals. A formal evaluator
may instead return a polynomial in covariance symbols and \(M\)-atoms.
That mode asserts no Gaussian law for arbitrary symbols. In particular,
an omitted covariance is not permission to set it to zero if the resulting
matrix is not positive semidefinite. The actual derivative ceiling must
be computed for the supplied covariance pattern; no universal ceiling of
five is asserted for arbitrary Gaussian data.

Only \(r_3\) contains \(V_3\), so (E9) directly gives
\[
 \partial_{V_3}h_4=\lambda_{43}p_1^2,\qquad
 A_{43,\rm out}=d\lambda_{43},\quad d=\mathbb E\phi'(Z)^2.  \tag{E13}
\]
For a layer iteration with constant \(d\),
\(\lambda_{43,\ell}=1+A_{43,\ell-1}\), and \(A_{43,0}=0\),
induction yields \(1+A_{43,\ell}=\sum_{j=0}^{\ell}d^j\).
This coordinate needs no dynamic state; the remaining head stores
\((\gamma,A_{41})\), with all lower-order inputs supplied.
Layer-dependent \(d_\ell\) instead gives
\(\tau_\ell=1+d_\ell\tau_{\ell-1}\), \(\tau_0=1\).
This is an exact algebraic elimination. It supplies neither a neural
population interpretation of the input covariance data nor a bridge from
initialization derivatives to positive-time dynamics.

## F. Typed curvature words and their finite derivative meaning

Fix a finite feedforward network at one supplied state, with arbitrary
widths \(n_1,\ldots,n_L\), stored readout \(a\in\mathbb R^{n_L}\),
matrices \(W^{(\ell)}:\mathbb R^{n_{\ell-1}}\to\mathbb R^{n_\ell}\),
and componentwise \(C^2\) activations. Write
\(f=a^Th^{(L)}/n_L\). No initialization or optimizer is assumed here.

For each layer define the downstream scalar function \(F_\ell(z)\) by
replacing only its preactivation by the independent variable \(z\), then
recomputing every downstream activation with all downstream matrices and
the readout held fixed. Put
\[
 \delta_\ell=n_L\nabla_zF_\ell(z^{(\ell)}),\quad
 R_\ell=n_L\nabla_z^2F_\ell(z^{(\ell)}),\quad
 D_\ell=\operatorname{diag}(\phi_\ell'(z^{(\ell)})).
                                                               \tag{F1}
\]
Thus \(R_\ell:\mathbb R^{n_\ell}\to\mathbb R^{n_\ell}\) is symmetric.
Define \(b_L=a\), \(b_\ell=(W^{(\ell+1)})^T\delta_{\ell+1}\) for
\(\ell<L\), and the actual local Hessian source
\[
 E_\ell=\operatorname{diag}\bigl(\phi_\ell''(z^{(\ell)})
                                                    \odot b_\ell\bigr).
                                                               \tag{F2}
\]
The exact recursions are
\[
 \delta_\ell=D_\ell b_\ell,\qquad R_L=E_L,\qquad
 R_\ell=E_\ell+D_\ell(W^{(\ell+1)})^T
                  R_{\ell+1}W^{(\ell+1)}D_\ell.           \tag{F3}
\]
To verify the Hessian formula, the map from \(z^{(\ell)}\) to
\(z^{(\ell+1)}\) is \(T(z)=W^{(\ell+1)}\phi_\ell(z)\).
Its first variation is \(W^{(\ell+1)}D_\ell v\), and its second variation
is \(W^{(\ell+1)}(\phi_\ell''\odot v\odot w)\). The scalar second
chain rule gives one term contracting two first variations against
\(R_{\ell+1}\), and one contracting the second variation against
\(\delta_{\ell+1}\). The latter is \(v^TE_\ell w\). This proves (F3)
for every \(v,w\), including all normalization factors.

Let \(J_{\ell\leftarrow1}\) be the Jacobian of \(z^{(\ell)}\) with
respect to \(z^{(1)}\), with the weights fixed:
\[
 J_{1\leftarrow1}=I,\qquad
 J_{\ell\leftarrow1}=W^{(\ell)}D_{\ell-1}\cdots W^{(2)}D_1.
\]
Repeated substitution in (F3) yields
\[
 R_1=\sum_{\ell=1}^L J_{\ell\leftarrow1}^TE_\ell
                                      J_{\ell\leftarrow1}.       \tag{F4}
\]
Induction proves the expansion and provides a type check for each product.
For layer three its term is exactly
\(D_1(W^{(2)})^TD_2(W^{(3)})^TE_3W^{(3)}D_2W^{(2)}D_1\).
Erasing the diagonal factors gives the matrix-orientation word
\((2^-,3^-,3^+,2^+)\). Counting distinct matrix labels records how many
different stored matrices occur. It is a syntactic attribute of a term
whose finite semantics has now been specified; it is no theorem about
independence, nonclosure, probability or convergence.

If \(\phi_\ell''\equiv0\), its local source is identically zero, so that
source term can be omitted. This may be specified layer by layer. When
all activations are affine, every \(R_\ell\) is zero because \(F_\ell\)
is affine in its independent preactivation. The full parameter Hessian
need not vanish: even \(f(a,u)=au\) has mixed derivative one. In particular
\(R_1/n_L\) is the first-preactivation Hessian only, not the full parameter
Hessian and not the material derivative of a trained backward field.
Differentiating along training also varies all downstream weights and
requires their explicit first variations. This held-fixed contract is
part of the API, not something a string emitter can infer.

## G. Additional shallow comparisons

### G.1. Identity: exact raw-GD closure, joint compact-time limit and moments

Take one input \(x=1\), one hidden layer, identity activation, arbitrary
label \(y\in\mathbb R\), full loss \((f_n-y)^2\), and equal mobilities
\(n\kappa\), \(\kappa>0\), for first weights \(u\) and stored readout
\(a\). Both initial vectors have independent standard Gaussian entries.
At a finite state put
\[
 f_n=a^Tu/n,\quad q_n=(\|a\|_2^2+\|u\|_2^2)/n,\quad
 d_n=(\|a\|_2^2-\|u\|_2^2)/n.
\]
If \(b=-2\kappa\eta(f_n-y)\), simultaneous raw GD gives
\[
 a^+=a+bu,\quad u^+=u+ba,\qquad
 f_n^+=(1+b^2)f_n+bq_n,\quad
 q_n^+=(1+b^2)q_n+4bf_n,\quad d_n^+=(1-b^2)d_n.            \tag{G1}
\]
These equations follow by multiplying the two updated vectors and
expanding their squared norms. They are an exact three-scalar update at
every width. The kernel before a step is \(\kappa q_n\), and the separate
kernel blocks are \(\kappa(q_n-d_n)/2\) and
\(\kappa(q_n+d_n)/2\).

Finite physical GF has
\[
 \dot f_n=-2\kappa(f_n-y)q_n,\quad
 \dot q_n=-8\kappa(f_n-y)f_n,\quad \dot d_n=0,\quad
 q_n^2-4f_n^2=\text{constant}.                            \tag{G2}
\]
The derivative of the last expression is zero by direct substitution.
Gaussian sample averages give \((f_n,q_n,d_n)(0)\to(0,2,0)\) in probability
and every finite \(L^p\). One direct proof for centered averages is the
even-moment index count used after (D4); Gaussian moments of all orders
exist. The deterministic limit solves
\[
 \dot f=-4\kappa(f-y)\sqrt{1+f^2},\quad f(0)=0,\qquad
 q=2\sqrt{1+f^2},\quad d=0.                              \tag{G3}
\]
Local existence follows from a locally Lipschitz scalar field. Its residual
has constant sign and
\[
 |f(t)-y|=|y|\exp\left(-4\kappa\int_0^t\sqrt{1+f(v)^2}\,dv\right)
                                  \le|y|e^{-4\kappa t}.          \tag{G4}
\]
Thus \(f\) remains between zero and \(y\), which prevents escape and proves
global existence and uniqueness. Equation (G4) also proves fitting.

For every deterministic sequence \(\eta_n>0\), \(\eta_n\to0\), raw GD
with weights linearly interpolated and predictor/kernel recomputed obeys,
on every fixed \([0,T]\),
\[
 \sup_{t\le T}\bigl(|f_n(t)-f(t)|+|q_n(t)-q(t)|+|d_n(t)|\bigr)
                                  \xrightarrow{\mathbb P}0.     \tag{G5}
\]
Here is a direct proof that includes the growing number of updates. The
exact scalar scheme (G1) has the form
\(x^+=x+\eta V(x)+\eta^2R(x)\), with polynomial \(V,R\) independent of
width. Choose a closed rectangular box containing the compact limiting curve
with distance at least one from its boundary. On that box,
\(V\) is Lipschitz with some finite constant \(L_T\), \(R\) is bounded,
and the exact limiting step has error at most \(C_T\eta^2\), obtained by
integrating \(V(x(t+s))-V(x(t))\). Until first exit from the box, the
grid error therefore satisfies
\(e_{k+1}\le(1+L_T\eta)e_k+C_T\eta^2\), hence
\(e_k\le e^{L_T(T+1)}(e_0+C_T(T+1)\eta)\).
When \(e_0\) and the step are sufficiently small, the right side is less than
half the box margin, ruling out a first exit. Convergence
in probability of \(e_0\) proves the grid assertion. Within a raw
interpolation cell, replace \(b\) by \(\lambda b\) in (G1),
\(0\le\lambda\le1\); the same bounded polynomials give a uniform
\(O_T(\eta)\) cell displacement, proving (G5). The output loss and both
kernel blocks follow by continuous finite formulas on the box. There is
no rate condition coupling \(\eta_n\) to \(n\), and no conclusion for a
growing physical horizon.

In feature time \(s\), the exact characteristics are
\[
 A_s=a_0\cosh s+u_0\sinh s,\qquad
 U_s=u_0\cosh s+a_0\sinh s.
\]
Gaussian expectation gives \(F(s)=\sinh(2s)\). The physical clock is
\(s'=-2\kappa(F(s)-y)\), and its endpoint is
\(s_*=(\operatorname{arsinh}y)/2\). Indeed monotonicity and (G4) give
\(s(t)\to s_*\); the displayed linear combinations then converge in every
finite mark-space \(L^p\). This endpoint assertion concerns the canonical
population physical flow, separately from compact-time joint GD convergence.

The exact output-coordinate feature kernel is
\(K(v)=2\sqrt{1+v^2}\). Therefore
\[
 (K(\sqrt x)-2)/x=\sum_{j\ge0}(-1)^j\mu_jx^j,\qquad
 \mu_j=\frac{1}{4^j(j+1)}{2j\choose j}.                   \tag{G6}
\]
These coefficients follow from the binomial expansion, valid near zero or
formally. They are the moments of
\[
 d\nu(t)=\frac2\pi\sqrt{(1-t)/t}\,\mathbf1_{0<t<1}\,dt.  \tag{G7}
\]
To verify without a special-function import, set \(t=\sin^2\theta\).
The \(j\)-th moment is
\((4/\pi)\int_0^{\pi/2}\sin^{2j}\theta\cos^2\theta\,d\theta\).
Integration by parts gives
\(I_j=\int_0^{\pi/2}\sin^{2j}\theta\,d\theta
=(2j-1)I_{j-1}/(2j)\),
\(I_0=\pi/2\); subtracting \(I_{j+1}\) from \(I_j\) yields exactly (G6).
For any nonzero polynomial \(p\), both
\(\int p(t)^2d\nu(t)\) and \(\int t p(t)^2d\nu(t)\) are strictly positive,
since the density is positive on an interval. Thus every ordinary and
shifted Hankel matrix of \((\mu_j)\) is positive definite. This all-order
statement is specific to this identity model.

### G.2. Raw-square shallow characteristics and the metric-boundary reduction

For one hidden layer, \(f_n=n^{-1}\sum_i a_i v_i^2\), independent standard
Gaussian \(a_i,v_i\), and feature mobilities \(n,n\), the exact neurons solve
\[
 a'=v^2,\qquad v'=2av.                                    \tag{G8}
\]
The invariant is \(c_*=a_0^2-v_0^2/2\). Let
\(B''=4c_*B,B(0)=1,B'(0)=-2a_0\). Before its first zero,
\[
 a=-B'/(2B),\quad v=v_0/B,\quad
 B(s)=\begin{cases}
 \cosh(2\sqrt{c_*}s)-(a_0/\sqrt{c_*})\sinh(2\sqrt{c_*}s),&c_*>0,\\
 1-2a_0s,&c_*=0,\\
 \cos(2\sqrt{-c_*}s)-(a_0/\sqrt{-c_*})\sin(2\sqrt{-c_*}s),&c_*<0.
 \end{cases}                                                   \tag{G9}
\]
Indeed \(B'^2-4c_*B^2=2v_0^2\) is constant. Differentiating the two
quotients and using that identity gives (G8) and their initial values.
This includes \(v_0=0\), where the solution is stationary. The finite
feature output is \(-\frac1{2n}\sum_i v_{i0}^2B_i'/B_i^3\).
For full squared loss and arbitrary label \(y\), physical time obeys
\(s'=2(y-f_n(s))\) wherever the feature characteristic is available;
on a branch with nonzero residual it is equivalently
\(t(s)=\frac12\int_0^s(y-f_n(u))^{-1}du\). These are maximal-interval
statements, not a positive-time Gaussian population construction.

Freezing the first block of the two-hidden-layer raw-square network gives
\(q_n=n^{-1}\sum_j u_j^4\) and \(z_i'=2q_na_iz_i\). Conditional on \(u\),
\(v_i=z_i/\sqrt{q_n}\) are iid standard Gaussians independent of \(a\),
and their conditional law is independent of \(u\). Hence they are also
independent of \(q_n\). The reduced output is
\(q_n n^{-1}\sum_i a_i v_i^2\), with feature equations
\(a_i'=q_nv_i^2,v_i'=2q_na_iv_i\). Since \(q_n\to3\) with every finite
moment, every fixed derivative has the limiting scaling
\[
 F_{\rm red}^{(k)}(0)=3^{k+1}F_{\rm sh}^{(k)}(0).           \tag{G10}
\]
For example the conditional derivative expectation is exactly a constant
times \(q_n^{k+1}\); Jensen bounds its higher moments by a fixed Gaussian
moment. This proves the limit without a trajectory interchange.

For any fixed deterministic multiplier \(b>0\), formally
\(F_b(s)=bF_1(bs)\), \(K_b(v)=b^2K_1(v/b)\). Thus if
\((K_b(\sqrt x)-7b^2)/x=\sum_j(-1)^j\mu_j^{(b)}x^j\),
\[
 \mu_j^{(b)}=b^{-2j}\mu_j^{(1)},\qquad
 \det(\mu_{i+j+1}^{(b)})_{i,j=0}^2
       =b^{-18}\det(\mu_{i+j+1}^{(1)})_{i,j=0}^2.          \tag{G11}
\]
The diagonal congruence has entries \(b^{-2i}\), with the extra common
factor \(b^{-2}\), proving the determinant factor.

For completeness a finite scalar regeneration of the conventional shallow
certificate is: apply
\(X(a^pv^q)=p a^{p-1}v^{q+2}+2q a^{p+1}v^q\) repeatedly to \(av^2\),
then evaluate by \(m(p)m(q)\) from B. Divide the result at order \(k\) by
\(k!\), solve \(F(G(y))=y\) coefficientwise, and form \(F'(G(y))\).
Through order thirteen this gives the six moments
\[
 \left(\frac{480}{49},\frac{43756}{16807},
 \frac{7214528}{2470629},\frac{37635527904}{9886633715},
 \frac{171752915595136}{30520038278205},
 \frac{2199776554157960896}{246754509479287425}\right),
\]
and direct rational elimination gives
\[
 \det(\mu_{i+j+1})_{i,j=0}^2
 =-\frac{86245462994269879146938487857152}
         {516623655319449980325461333747775}<0.             \tag{G12}
\]
The two monomial recursions just specified determine every displayed
number using integers and rational arithmetic; their correctness follows
from (G8), Gaussian integration by parts, and triangular coefficient
comparison. If these were nonnegative-measure moments on \([0,\infty\)),
the matrix in (G12) would have quadratic form
\(\int t p(t)^2d\nu(t)\ge0\), which contradicts its negative determinant.
Equivalently (G11) transfers the same certificate from the multiplier-three
boundary. No centered or Hermite-normalized quadratic, different initial
law, or multiple-input model is included.

For every prescribed positive feature time there is an open Gaussian
initial-data set with a pole earlier: at \(c_*=0,a_0>0\) the denominator
zero is \(1/(2a_0)\), and it is transverse when \(v_0\ne0\). Take large
\(a_0\) and use continuity of that transverse zero under nearby initial
data. Gaussian density is positive on the open set. Thus the maximal
characteristic formula cannot itself define a common positive-time ordinary
Gaussian pushforward for all marks. The finite coefficients and the
Stieltjes obstruction remain valid independently of that obstruction.

## H. Finite coefficient certificates and proposed interfaces

Let \(F(s)=a_1s+a_3s^3+\cdots\) be a formal odd series over a characteristic
zero field with \(a_1\ne0\). Its inverse \(G(y)=\sum b_jy^j\) is uniquely
determined by
\[
 b_1=a_1^{-1},\qquad
 b_j=-a_1^{-1}[y^j]\sum_{l=2}^{j}a_l
                         \left(\sum_{i<j}b_i y^i\right)^l.       \tag{H1}
\]
Only the linear term contains \(b_j\), proving existence and uniqueness
by induction. The inverse is odd, by applying uniqueness to \(-G(-y)\).
For \(K=F'\circ G\) and
\((K(\sqrt x)-a_1)/x=\sum_{r\ge0}(-1)^r\mu_rx^r\),
\(\mu_r\) depends only on \(F\) through order \(2r+3\), and its dependence
on the highest derivative is affine with coefficient
\[
 [F^{(2r+3)}(0)]\mu_r
       =\frac{(-1)^r}{(2r+2)!a_1^{2r+2}}.                 \tag{H2}
\]
Indeed the only new coefficient at that order in \(F'(G(y))\) is
\((2r+3)a_{2r+3}(y/a_1)^{2r+2}\); the other nonconstant derivative
terms require inverse coefficients only through order \(2r+1\).
Thus output order seventeen determines eight kernel moments. It does not
determine the next output derivative.

For the quadratic first hidden root with (C6), put
\(N(y)=Q_1(G(y))\). Formal chain differentiation gives
\[
 \frac{d}{dx}N(\sqrt x)=\frac{4\alpha}{K(\sqrt x)}.
                                                               \tag{H3}
\]
If \(1/K(\sqrt x)=\sum_{r\ge0}(-1)^rh_rx^r\), integration in the
formal variable gives the first-hidden companion moments
\(\rho_r=4\alpha h_r/(r+1)\). Therefore an output jet through order
seventeen determines nine such hidden moments, the last using the Ward
identity \(Q_1^{(18)}=8\alpha F^{(17)}\). This is a dependency statement,
not a claim that a high-order numerical prefix has been generated.

For a supplied symmetric block matrix
\(H=\begin{pmatrix}A&b\\b^T&c\end{pmatrix}\) with \(A\) positive
definite, completing the square gives
\[
 (v,t)^TH(v,t)=(v+tA^{-1}b)^TA(v+tA^{-1}b)
                         +t^2(c-b^TA^{-1}b).              \tag{H4}
\]
Thus \(H\succeq0\) exactly when \(c\ge b^TA^{-1}b\); strict inequality
means positive definiteness, and
\(\det H=\det A(c-b^TA^{-1}b)\) follows by the same triangular change of
variables. If \(A\) is singular positive semidefinite, replace the inverse
by its inverse on the range, require \(b\in\operatorname{ran}A\), and
the same proof applies after orthogonal splitting into range and kernel.
Necessity of the range condition follows by testing \(v\in\ker A\) with
both signs of \(t\). These give exact next-moment thresholds without
recomputing earlier moments. Finite positive gates do not establish an
infinite moment representation.

Interval certificates likewise have a small contained algebra. For a
polynomial \(P\) of degree at most \(d\), write
\(P(a+(b-a)t)=\sum_{k=0}^{d}c_kt^k\), \(a<b\). Its Bernstein coefficients
on this interval are
\[
 \beta_j=\sum_{k=0}^j c_k\frac{{j\choose k}}{{d\choose k}},\qquad
 P(a+(b-a)t)=\sum_{j=0}^d\beta_j{d\choose j}t^j(1-t)^{d-j}. \tag{H5}
\]
The identity follows from
\({d\choose j}{j\choose k}={d\choose k}{d-k\choose j-k}\)
and the binomial theorem. The basis functions are nonnegative and sum to
one for \(0\le t\le1\). All negative \(\beta_j\) therefore prove strict
negativity on the closed interval; all nonpositive coefficients prove the
weak version. Alternatively \(P''\ge0\) and negative endpoint values
imply negativity by the convex chord bound, proved by monotonicity of
secant slopes. For a rational witness \(P/Q\), first prove \(Q>0\) on
the entire interval. These tests certify a supplied polynomial; they do
not verify its neural coefficient provenance or a numerical interval
endpoint without that polynomial's regeneration.

The proposed implementation should extend the existing finite-calculus
modules, with no training runner or implicit data inputs:

| Proposed operation | Input and output contract |
|---|---|
| `gradient_tree_terms(order)` | Nonnegative integer order; exact integer weights and canonical unrooted parameter-contraction trees from A. |
| `forest_expectation(forest, width=None)` | Explicit row/column decorations and simple acyclic edges; exact Gaussian value from (B2) at positive integer width, or leading value from B when omitted. For odd edge count the expectation is zero. |
| `quadratic_forest_derivatives(root, order, alpha, beta)` | A root forest, finite order and exact scalar or symbolic block multipliers; finite derivative polynomial from C, with grades and normalizations retained. |
| `quadratic_euler_pullback(root, step, loss=False)` | One simultaneous substitution (D1), or the explicitly label-one full-loss substitution; exact forest polynomial, never a population trajectory. General labels should be an explicit argument if supported. |
| `finite_flow_jets(state, data, activations, mobilities, order)` | Supplied finite raw state and derivative callbacks through the declared ceiling; ordinary parameter/forward/reverse coefficients from E and an explicit `clock="physical_full_mean_loss"` tag. |
| `hidden_gram_jet(jets, kind)` | `kind` explicitly selects activation or preactivation; exact coefficient products or floating numerical products according to the caller's arithmetic. |
| `gaussian_hidden_head(covariances, responses, activation_atoms)` | Finite local algebra (E9)–(E13), with separate actual-Gaussian and formal-symbolic modes, complete covariance data, fixed-coordinate partials and a declared derivative ceiling. |
| `preactivation_hessian_words(layer_shapes, affine_flags)` | Typed factors in (F4), shapes, orientation and local source layer; valid source elimination only for declared identically affine activations. |
| `preactivation_hessians(state, activation_derivatives)` | Numeric \(R_\ell,E_\ell\) and fixed-variable contract (F1)–(F3), with actual transpose checks; no full-parameter-Hessian label. |
| `identity_shallow_step(f, q, d, label, mobility, step)` | Exact scalar update (G1), with stated full-loss convention and supplied finite scalar state. |
| `next_hankel_threshold(A,b)` / `bernstein_coefficients(P,a,b)` | Exact finite matrix/polynomial operations (H4)–(H5), with explicit singular-range and interval validation. |

Integers used as counts must reject booleans and nonintegral types rather
than coercing them silently. Floating implementations must state that
roundoff and intermediate overflow can invalidate numerical evaluation;
an exact symbolic identity is not an exact floating-point certificate.
Inputs and outputs should be owned independently, and no operation should
load retained coefficients, run a campaign, mutate a supplied state or
write files. The graph evaluators have combinatorial cost at caller-chosen
finite size; no efficient general high-order promise is made.
