# Canonical Gaussian bridge at the two special angles

Date: 2026-09-06. Scope: L=2, both activations arctan, rho=0 or rho=-1,
loss SUM, labels (1,-1), and the physical normalization of dependency A
below. This is a proof-building note. No experiments, web searches,
other project files, history, or reviews were used.

## 1. Dependencies, conclusion, and conventions

The two mathematical dependencies were read in full, including their
limitations. Their whole-file SHA-256 snapshots are:

* **A:** `/tmp/l2-two-sample-proof-0ywjpp/ORTHOGONAL_ANTIPARALLEL_FLOW_ANCHOR.md`,
  `c3f147633689050f8d9a4749e23861b02640dd7ba0e201b0f05a609b9c76cf39`.
* **P:** `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md`,
  `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603`.

The procedural file `/etc/codex/skills/solve-math-rigorously/SKILL.md`
was read in full; its SHA-256 is
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
It contributes no mathematical theorem. Files mentioned inside A and P
were not inspected or imported as additional dependencies.

We import A's deterministic Sections 2--9: transformed L2 stability,
global existence and restart for an already specified bounded operator,
Euler consistency, and the same-initialization raw-GD/GF comparison.
We import P's elementary conditioning, integration-by-parts, projection,
singular-query regularization, and scalar-feedback arguments in Sections
4--7. Section 3 below verifies and extends their hypotheses for the
present activation, polynomial root, and single reused matrix. Neither
P's softplus dynamics nor any continuum assertion is imported.

**Result.** There are separate, countably generated population spaces
H1=L2(Omega1) and H2=L2(Omega2), the prescribed first-neuron Gaussian
pair, and a bounded operator A0:H1->H2 with norm at most 8, uniquely
specified on these generated spaces by the canonical finite Gaussian
program laws. Its reverse action is its actual Hilbert adjoint. On these
spaces the equations of A have one global autonomous solution with
initial readout zero, unique also from every reached state. This solution
is the full-sequence canonical width limit, on every finite physical
horizon, of finite GF with the stated random initialization and of raw
GD with eta=n^-2 and its prescribed raw interpolation.

The convergence assertions include joint same-neuron two-sample hidden
and backward path laws, finite joint field evaluations, predictions,
loss, all three kernel blocks, admissible forward and transpose probes,
raw parameter velocity norms and energies, and individual hidden-field
velocity norms and energies. Precise topologies and admissibility are
specified in Sections 8--10. There is no operator-norm convergence of
matrices of different sizes, and no empirical pairing of different
neuron populations. Canonical refers to joint initialization and reuse,
not just an operator norm bound.

Proof architecture: identify every fixed finite program; realize a
countable closure of those programs and inherit boundedness and adjointness
from the finite matrices; apply A on that common space; use deterministic
mesh bounds to compare width and time limits. Independent Gaussian query
perturbations give mesh-uniform response bounds. Truncation and uniform
integrability supply the original-velocity bridge.

There are two logically separate outputs. The canonical GF bridge in
Sections 4 and 7--10 does not depend on row-L1 response estimates:
Section 8 obtains the needed integrability directly from finite-flow
stability and Gaussian concentration. Sections 5--6 strengthen it with
bounded Gaussian remainders and row-L1 memory representations. In
particular a problem with a source-coordinate estimate would not
invalidate the core canonical-flow construction.

Write

\[
 B=\pi/2,\quad \phi(z)=\arctan z,\quad D(z)=(1+z^2)^{-1},
 \quad F(z)=z+z^3/3,\quad g=F^{-1},\quad H(u)=\phi(g(u)).
 \tag{1}
\]

Here g'=D(g), H'=D(g)^2, and g,H,D,phi have bounded first
derivatives; g is unbounded but 1-Lipschitz. Derivatives of g and H
of the orders used below are bounded and continuous, as follows by
repeated differentiation using g'=1/(1+g^2). In particular |H|<=B,
0<D<=1, |D'|<=1. The root U0=F(G) is not Gaussian; it is a cubic
function of a Gaussian and has all finite moments. E F(G)^2=14/3.

At finite width, inner products are x^T y/n. A0,n has iid N(0,1/n)
entries, acts with no additional normalization, and its adjoint is
A0,n^T. The first-neuron pairs are iid N(0,C), independently of A0,n,
where C=I for rho=0 and C=((1,-1),(-1,1)) for rho=-1. The actual
finite initial readout has independent N(0,n^-2) entries. It is retained
in Sections 9--10; zero readout is initially used as an auxiliary
finite program.

## 2. The finite program and all its source slots

Use a deterministic finite partition with steps eta_k>0. Both sample
indices a,b belong to {1,2}, even at rho=-1. At each step put

\[
\begin{aligned}
 U_{0a}&=F(G_a),\\
 H_{ka}&=H(U_{ka}),\\
 Z_{ka}&=A_k H_{ka},\\
 J_{ka}&=\phi(Z_{ka}),\\
 f_{ka}&=\langle w_k,J_{ka}\rangle,\\
 r_{ka}&=f_{ka}-y_a,\\
 \gamma_{ka}&=-2\eta_k r_{ka},\\
 V_{ka}&=w_kD(Z_{ka}),\\
 Q_{ka}&=A_k^*V_{ka}.
\end{aligned}                                                    \tag{2}
\]

The simultaneous state update is

\[
\begin{aligned}
 U_{k+1,a}&=U_{ka}+\sum_b C_{ab}\gamma_{kb}Q_{kb},\\
 A_{k+1}&=A_k+\sum_b\gamma_{kb}V_{kb}\otimes H_{kb},\\
 w_{k+1}&=w_k+\sum_b\gamma_{kb}J_{kb},\\
 w_0&=0.
\end{aligned}                                                    \tag{3}
\]

Rank one means (v tensor h)e=v<h,e>; at width n it is vh^T/n.
For rho=0 these are A's transformed Euler equations. At rho=-1 the
identities U2=-U1, H2=-H1, Z2=-Z1, J2=-J1, f2=-f1, V2=V1,
Q2=Q1 hold at every step. Equation (3) then reduces to U1+=-4 eta
(f1-1)Q1, with the same factor four in A and w. The two-sample formula
is retained to define formal derivatives at singular sample covariance.

There are two centered jointly Gaussian source families:

\[
 (\xi_{ka})\text{ on Omega2},\qquad
 (\zeta_{ka})\text{ on Omega1}.
\]

They are independent of each other and of the root pair. Within a
family the sources need not be independent. On their proper spaces
the scalar law is

\[
\begin{aligned}
 U_{ka}&=F(G_a)+\sum_{r<k,b}C_{ab}\gamma_{rb}Q_{rb},
       &H_{ka}&=H(U_{ka}),\\
 Z_{ka}&=\xi_{ka}+\sum_{r<k,b}a_{ka,rb}V_{rb},
       &J_{ka}&=\phi(Z_{ka}),\\
 w_k&=\sum_{r<k,b}\gamma_{rb}J_{rb},
       &V_{ka}&=w_kD(Z_{ka}),\\
 Q_{ka}&=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H_{rb},
       &f_{ka}&=\mathbb E[w_kJ_{ka}].
\end{aligned}                                                    \tag{4}
\]

The two complete response coefficients, including learned memories, are

\[
\begin{aligned}
 a_{ka,rb}
  &=\alpha_{ka,rb}+\gamma_{rb}\mathbb E[H_{ka}H_{rb}],
  &\alpha_{ka,rb}&=\mathbb E[\partial_{\zeta_{rb}}H_{ka}],
       &&r<k,\\
 b_{ka,rb}
  &=\beta_{ka,rb}+\mathbf1_{r<k}\gamma_{rb}\mathbb E[V_{ka}V_{rb}],
  &\beta_{ka,rb}&=\mathbb E[\partial_{\xi_{rb}}V_{ka}],
       &&r\le k.
\end{aligned}                                                    \tag{5}
\]

All source covariances, including across different runs on the same
initial matrix, are the uncentered input second moments:

\[
 \mathbb E\xi_{ka}\xi_{vb}=\mathbb E H_{ka}H_{vb},\qquad
 \mathbb E\zeta_{ka}\zeta_{vb}=\mathbb E V_{ka}V_{vb}.
 \tag{6}
\]

Every derivative in (5) differentiates the complete earlier explicit
expression, holding selected expectations, scalar feedback values,
response coefficients, and covariances fixed. It does not differentiate
the procedure selecting these deterministic quantities. Thus

\[
\begin{aligned}
 \partial U_{ka}&=\sum_{r<k,b}C_{ab}\gamma_{rb}\partial Q_{rb},\\
 \partial H_{ka}&=D(g(U_{ka}))^2\partial U_{ka},\\
 \partial w_k&=\sum_{r<k,b}\gamma_{rb}D(Z_{rb})\partial Z_{rb},\\
 \partial V_{ka}&=D(Z_{ka})\partial w_k
                    +w_kD'(Z_{ka})\partial Z_{ka}.
\end{aligned}                                                    \tag{7}
\]

The first line has no Q times a derivative of a first-layer multiplier.
The current reverse response is exactly

\[
 \beta_{ka,kb}=\mathbf1_{a=b}\mathbb E[w_kD'(Z_{ka})].             \tag{8}
\]

There is no current learned-rank term in (8). The past readout
derivative in (7) must not be omitted. Both forward calls precede both
reverse calls at a step; all updates follow those calls. Formally
distinct current sample slots have derivative delta_ab even when their
Gaussian covariance is singular. At initialization V0=Q0=0 and both
reverse slots have variance zero. They remain in (4)--(7); derivatives
of later H with respect to them may be nonzero.

## 3. Elementary fixed-program identification: adaptation of P

For every fixed finite program (2)--(3), its joint empirical neuron
tuples converge in probability against every continuous polynomial-growth
test to (4)--(6). In particular all finite Wasserstein orders converge.
The assertion allows finitely many additional smooth globally Lipschitz
coordinate instructions with bounded first derivatives, independent
all-moment root tuples, either orientation of A0,n, and normalized
quadratic scalar contractions. Smooth truncations of additional
polynomial-growth instructions can subsequently be removed when their
L2 errors are controlled, as in Section 8. Arbitrary polynomial query
maps are not being admitted merely by naming a tensor-program theorem.

Here are the necessary checks and the elementary proof. They also
explain why the cubic root does not violate the hypotheses.

### 3.1 Bounds and moments with an all-moment, possibly non-Gaussian root

Fix the finite graph. Its zero-readout iterates have deterministic
coordinate bounds for w, independent of root values and width. Indeed,

\[
 \|w_{k+1}\|_\infty
 \le(1+4B^2\eta_k)\|w_k\|_\infty+4B\eta_k.                    \tag{9}
\]

This remains valid if independent query noise is added to a forward
answer, since phi remains bounded. Thus V=wD(Z) is a globally
Lipschitz coordinate instruction on the range actually used. For graph
estimates it may be written tau(w)D(Z), where a smooth bounded tau is
the identity on an interval strictly containing that range. This is an
identity on the entire program, not a cap-removal hypothesis. The
coordinate update for U is linear in Q. All remaining instructions
are the globally Lipschitz maps g,H,phi,D, matrix actions, normalized
contractions, and scalar arithmetic. Only the initial root F(G) has
polynomial growth without a bounded derivative. Store (G,F(G)) as a
joint iid root tuple; no differentiation of F is required in the next
argument.

The following extension of P Section 3 proves the required moments.
Condition on all root arrays R, and put

\[
 K_R=1+\sum_j\|R_j\|_{n,2}.
\]

Unrolling the ranks, the estimates in P (19), applied only to Gaussian
matrix parameters, give

\[
 \|x\|_{n,2}+|c|\le P(K_R+\|A_{0,n}\|),\qquad
 \|D_E x[v]\|_2\le P(K_R+\|A_{0,n}\|)\|v\|_2,                \tag{10}
\]

where E consists of the unscaled independent matrix Gaussians. A
scalar differential has an additional n^-1/2. For example
D(A0 x)[v]=A0 Dx[v]+n^-1/2 v_matrix x, and a contraction differential
is (<Dx,y>+<x,Dy>)/n. These formulas prove (10) by finite induction.
The same induction gives Lipschitz dependence, in ordinary Euclidean
norm for vector arrays, on changing the stored roots, with polynomial
constant in their normalized norms and the matrix norm.

For completeness, the Gaussian moment inequality used here is

\[
 \mathbb E|X(E)-\mathbb E X(E)|^p
 \le(\pi/2)^p\mathbb E|N|^p\,
                   \mathbb E\|\nabla X(E)\|_2^p.               \tag{11}
\]

Take an independent E', rotate E_theta=E cos(theta)+E' sin(theta),
and integrate the derivative from 0 to pi/2. Its orthogonal velocity
is an independent standard Gaussian. Integral Holder, followed by
conditional Jensen, proves (11). Smooth approximation proves the same
inequality for Lipschitz scalar functions. A 1/4 sphere net of size
at most 9^n and scalar Gaussian tails give

\[
 \mathbb P(\|A_{0,n}\|>t)
 \le2\exp(2n\log9-nt^2/8),\quad t>0.                          \tag{12}
\]

Consequently all moments of the matrix norm are bounded uniformly in n.

One detail is needed because the stored root is not Lipschitz in G.
Let m_i(R)=E_E x_i(R,E). Permuting two neurons i,j of the output
population and integrating out the correspondingly permuted Gaussian
matrix gives m_i(R^{ij})=m_j(R). The root Lipschitz estimate gives

\[
 |m_i(R)-m_j(R)|
 \le P(K_R)\sum_{\text{roots in this population}}|R_{li}-R_{lj}|.
\]

Also ||m(R)||_n<=P(K_R). Average the preceding inequality over j,
use Cauchy--Schwarz, and obtain

\[
 |m_i(R)|\le P(K_R)
             \left(1+\sum_l|R_{li}|\right).                  \tag{13}
\]

The same proof covers a population with no roots, where the means are
equal. Applying (11) conditionally on R, then (10)--(13), proves

\[
 \sup_n\mathbb E|x_i|^p<\infty\quad(1\le p<\infty).           \tag{14}
\]

Indeed normalized root norms have all moments by Jensen, and products
in (13) are bounded by Holder and the root moments. This proof is
uniform for auxiliary query noise epsilon in [0,1] in a fixed graph.
It applies to the empirical-feedback graph and its deterministic
coefficient version. Thus the non-Gaussian root F(G) is fully covered,
without a bound on max_i |G_i| and without an Lp matrix-operator claim.

### 3.2 Conditioning, both directions, and rank drops

We restate the part of P used to identify the law. For old observations
WV=Y, W^T U=Q with nonsingular Grams, orthogonal Gaussian projection
onto these linear constraints gives

\[
 W\mid\mathcal F=
 Y(V^TV)^{-1}V^T+
 U(U^TU)^{-1}Q^TP_{V^\perp}
       +P_{U^\perp}\widetilde W P_{V^\perp}.                  \tag{15}
\]

The mean satisfies both constraints because U^T Y=Q^T V. The
residual is exactly their orthogonal null component; Gaussian
orthogonal components are independent. At an adaptive query its input
is measurable with respect to the old transcript, so its answer adds
only the displayed linear constraint. This proves (15) inductively.

For a new input h, put h_perp=h-V(V^TV)^-1 V^T h. Equation (15)
gives a known linear combination of Y and U plus
||h_perp||_n P_{U^perp}e. If P has rank at most the fixed number J
of old queries, then, conditionally on the transcript,

\[
 \mathbb E\|\sigma Pe\|_{n,p}^p
 =\frac{\mathbb E|N|^p\sigma^p}{n}\sum_iP_{ii}^{p/2}
 \le \frac{J\mathbb E|N|^p\sigma^p}{n},\quad p\ge2.          \tag{16}
\]

For p<2 use the L2 inequality. Thus the projected-away part is small
in every finite empirical moment, by (14). Conditional variances of
empirical polynomial-growth tests of the remaining independent
Gaussian coordinates are at most C/n times an old empirical higher
moment. Conditional Chebyshev, root iid averaging, and induction prove
convergence for nonsingular Grams. General continuous polynomial-growth
tests follow by restricting to a ball, using uniform continuity there,
and the bound |x|^d 1_{|x|>R}<=R^{d-q}|x|^q for q>d.

The source form of this conditioning law is

\[
 Wh=\xi_h+\sum_s u_s\mathbb E\partial_{\zeta_s}h,
 \qquad W^T v=\zeta_v+\sum_r h_r\mathbb E\partial_{\xi_r}v.     \tag{17}
\]

Its source covariances are the input Grams. To verify the response,
write a new query as its least-squares old-query projection plus
h_perp. In the reverse answers, all old forward-input components are
orthogonal to h_perp. Hence the remaining conditional coefficient uses
E[zeta h_perp]. For a Gaussian vector zeta with covariance Gamma,

\[
 \mathbb E[\zeta f]=\Gamma\mathbb E[\nabla f].                \tag{18}
\]

Writing zeta=L e and integrating each independent Gaussian coordinate
proves (18), including singular Gamma. Substitution cancels the
derivatives of the old least-squares projection and gives (17).
The full new Gaussian source is the projected old sources plus a fresh
Gaussian of variance E h_perp^2; its variance is E h^2. Repeating this
calculation with W^T proves the reverse formula. Each source is a
deterministic linear combination of its own group's older sources and
a fresh independent Gaussian, so independence of the two groups and
the root is maintained.

For singular Grams, add epsilon times a fresh independent Gaussian root
to each initial-matrix query, retaining the same matrix and leaving
learned rank factors unperturbed. Every new Gram Schur complement is
at least epsilon^2. The Lipschitz graph estimates imply

\[
 \|x_n^\epsilon-x_n^0\|_{n,2}\le\epsilon P(K_n).               \tag{19}
\]

Here K_n includes root RMS norms and the matrix norm and has all
moments. Interpolation of (19) with the uniform higher moments (14)
gives convergence to zero in every finite empirical Lp, uniformly in
probability over n as epsilon decreases. On the scalar side use (17),
not inverse Grams. At fixed deterministic coefficients, each expression
has at most polynomial growth in the root and sources, and its source
derivatives are bounded: U is F(G) plus linear combinations of Q,
while H,phi,D and the bounded readout factors have bounded derivatives.
Finite induction supplies these statements uniformly on compact
coefficient sets. Gaussian covariance square roots vary continuously
even at a rank drop: a convergent subsequence of the bounded positive
square roots must square to the limiting covariance, whose positive
square root is unique by diagonalization. Coupling through these square
roots and dominated convergence therefore gives convergence of every
coefficient and scalar moment. This proves the zero-noise law via
(19) and a triangle inequality.

Singular slots are never deleted. If Gamma v=0 for the Gram of reverse
inputs, then E(sum v_s u_s)^2=0. An ambiguity in a derivative vector
in that null space changes no contracted response in (17). The explicit
expression convention fixes individual coefficients, including (8).

Finally, the exact identities

\[
 A_k h=A_0h+\sum_{r<k,b}\gamma_{rb}V_{rb}\langle H_{rb},h\rangle,
 \quad
 A_k^*v=A_0^*v+\sum_{r<k,b}\gamma_{rb}H_{rb}\langle V_{rb},v\rangle
                                                               \tag{20}
\]

give all learned terms in (5). Replace scalar contractions in causal
order by expectations to define a deterministic-coefficient program.
Comparing it with actual feedback uses
|<x,y>-<x',y'>|<=||x-x'||_2||y||_2+||x'||_2||y-y'||_2.
Finite graph induction on bounded K_n makes the RMS error a constant
times the sum of the finitely many contraction errors. They tend to
zero; (14) and interpolation transfer all polynomial-growth tests.
This completes the adaptation and proof of fixed-program identification.
The elementary bounded-cell coupling and tail truncation in P Section 7
then give convergence in every finite Wasserstein order.

## 4. A canonical common space and a true adjoint

It is not enough to specify an arbitrary bounded operator satisfying
A's assumptions. We now construct one from the identified joint laws.

Start with the root pair and enumerate a countable family of finite
programs, all using the same A0,n and root arrays. Include all dyadic
Euler schemes on integer horizons, all their intermediate nodes, both
matrix orientations applied to every generated node, rational linear
combinations, constants, and a countable collection of smooth bounded
cylinder functions dense among such functions. Include independent root
arrays when needed for probes. Each instruction has finitely many
parents; enumerate closure in stages, so every finite initial part is
an admissible finite graph. Selected deterministic real coefficients
are allowed. In particular a source itself is a node: subtract its
already selected response from the corresponding matrix answer.

Run the scalar construction of Section 3 through this countable
enumeration. At every source insertion its proposed covariance with
earlier sources is an input Gram, hence positive semidefinite. Subtract
the projection onto the earlier Gaussian span and use a fresh standard
Gaussian for its nonnegative residual variance. A zero variance needs
no random draw but retains its formal slot. This constructs all sources
on spaces carrying countably many independent standard Gaussians and
the roots. Such a space can be constructed, without an extension
theorem, by splitting the independent binary digits of a uniform point
of (0,1) into countably many infinite subsequences and applying the
Gaussian quantile function; cylinder probabilities follow from the
finite binary interval lengths. Null binary ambiguities do not matter.

Let Omega1 be the first-root/reverse-source generated space, and Omega2
the forward-source generated space, with any explicitly added local
roots. Use their separate L2 spaces. Their finite joint laws are exactly
the full-sequence limits of the same finite Gaussian graphs. Adding
extra unused queries does not change an old marginal: both descriptions
are the limit of that same finite empirical marginal. Thus the law
does not depend on the enumeration or on inserted probes.

For a forward queried input h write a(h) for its initial-matrix answer;
for a reverse queried input v write b(v) for its initial-transpose
answer. Every finite rational linear combination obeys

\[
 \left\|\sum_i t_i a(h_i)\right\|_2
       \le8\left\|\sum_i t_i h_i\right\|_2,
 \qquad
 \left\|\sum_j s_j b(v_j)\right\|_2
       \le8\left\|\sum_j s_j v_j\right\|_2,                  \tag{21}
\]

and

\[
 \langle a(h),v\rangle_{H2}=\langle h,b(v)\rangle_{H1}.        \tag{22}
\]

Indeed these are exact finite inequalities/identities on the event
||A0,n||<=8; (12) makes its probability tend to one, while Section 3
makes all involved Gram entries converge to deterministic values.
A strictly violated limiting inequality would contradict these two
facts. Rational approximation gives real coefficients. A zero-norm
linear relation on the inputs is therefore a zero-norm relation on the
answers; the proposed linear actions are well defined.

The queried-input spans are dense in the respective L2 spaces. Here is
the measure-theoretic detail. Finite cylinder events generate the sigma
field of the countable field tuple. Events approximable in measure by
the finite-cylinder algebra are closed under complement and countable
union (first approximate a finite union, then use continuity of
probability for the tail). Hence they contain the whole generated sigma
field. Bounded smooth functions of finitely many coordinates approximate
rectangle indicators in L2 by one-sided smooth threshold approximations,
including when a coordinate has an atom. Truncated simple functions
then approximate every L2 function. Our countable collection can use
rational thresholds, widths, and smooth cutoffs and their finite
products; their limits include these one-sided approximations. Each
such function is eventually queried in the closure.

Extend a and b to the completions by (21), obtaining bounded operators
A0:H1->H2 and B0:H2->H1. Passing (22) to the completions gives
B0=A0*. Both have norm at most 8. Their values are fixed on dense
domains, so no arbitrary extension remains. The scalar laws, the
pointwise operations, and these operator actions are preserved by the
isometric identifications arising from a different enumeration.
This is the asserted canonical common-space realization.

This argument does not make A0 an iid continuum integral kernel or
give it a bounded action on arbitrary Lp. The bound 8 is sufficient;
no sharp spectral norm limit is needed.

## 5. Mesh-uniform fresh-source coefficients

### 5.1 Exact source recursions and the support issue

Here are the direct recursions, including the term which would obstruct
the corresponding raw-coordinate argument. Fix a source slot (s,b)
and set

\[
 S_{ka}=\partial_{\zeta_{sb}}U_{ka},\quad
 T_{ka}=\partial_{\xi_{sb}}Z_{ka},\quad
 R_k=\partial_{\xi_{sb}}w_k,\quad
 L_{ka}=\partial_{\xi_{sb}}V_{ka},\quad p_{ka}=D(g(U_{ka})).
\]

All selected scalar coefficients are held fixed. Direct differentiation
of (4), keeping both sample indices, gives

\[
\begin{aligned}
 S_{k+1,a}
 &=S_{ka}+\sum_c C_{ac}\gamma_{kc}
   \left[\mathbf1_{k=s,c=b}
       +\sum_{r\le k,d} b_{kc,rd}p_{rd}^2 S_{rd}\right],\\
 T_{ka}
 &=\mathbf1_{k=s,a=b}+\sum_{r<k,d}a_{ka,rd}L_{rd},\\
 R_k&=\sum_{r<k,d}\gamma_{rd}D(Z_{rd})T_{rd},\\
 L_{ka}&=D(Z_{ka})R_k+w_kD'(Z_{ka})T_{ka}.
\end{aligned}                                                  \tag{23a}
\]

Here S is zero up to step s, and T,R,L are zero before their source
is available. Moreover
alpha_{ka,sb}=E[p_{ka}^2 S_{ka}] and beta_{ka,sb}=E[L_{ka}].
The first recursion has no attained Q multiplying a curvature
derivative. Its coefficients p^2 are bounded by one. The current
diagonal b_{kc,kd} is retained and has bound M_T; it gives ordinary
single-step feedback. Past feedback includes the additional delayed
propagation through the top equations. All rank memories remain in
a,b. These are exact identities, not a heuristic lag approximation.

The identities suggest a convolution/Catalan bound, but a claimed
closed lag majorant would itself need a proof. None is assumed here.
Also, Lipschitz stability of a flow with an actual operator alone does
not bound derivatives in arbitrary ambient Gaussian source directions:
at singular covariance such directions need not lie in its support.
The argument below instead constructs an independent-root forcing as
an actual auxiliary finite program, identifies its law, and extracts
the formal derivative by integration by parts. It is not a perturbation
of W0 and does not assert that a source impulse can be realized by
perturbing W0. This extra identification step resolves the support issue
for the expected coefficients being bounded.

### 5.2 Independent-root extraction, including feedback

Fix T. All estimates below are uniform over finite partitions through
T with maximum step at most 1. First (9) bounds w by a deterministic
M_T. For zero readout one may take

\[
 M_T=B^{-1}(e^{4B^2(T+1)}-1).
\]

Consequently |gamma_ka|<=2 eta_k(B M_T+1), their total absolute sum
is bounded by S_T=4(T+1)(B M_T+1), and
||A_k||<=8+B M_T S_T. These bounds hold at finite width on
||A0,n||<=8 and pass to the common space. They also hold for the
auxiliary single-query perturbations used next.

On these bounds, direct subtraction of (2)--(3), using bounded H,J,w,
g,H Lipschitz, and ||v tensor h||_HS=||v||_2||h||_2, gives a
one-step Lipschitz factor 1+L_T eta_k for the state norm

\[
 \sum_a\|\Delta U_a\|_2+\|\Delta A\|_{HS}+\|\Delta w\|_2.
 \tag{23}
\]

Use operator norm for differing initial operators. For example
||Delta V||_2<=||Delta w||_2+M_T||Delta Z||_2 and
||Delta Q||_2<=a_T||Delta V||_2+M_T||Delta A||_op.
The first transformed update uses Q alone; it introduces no unbounded
multiplier. The factor ||C||<=2 only changes L_T. These estimates
are valid for the off-invariant transformed equations as well. Thus
independent sample perturbations are legitimate at rho=-1 even though
the perturbed auxiliary graph need not satisfy sample opposition.
No claim that this off-invariant auxiliary graph is raw GF is required.

Here is an extraction argument that bounds the actual expected source
derivatives without assuming a bound on a formal memory resolvent.
Add epsilon e, where e is a fresh iid N(0,1) array, to Q_sb at one
reverse answer. At that step the changed state is only U and its norm
difference is at most C_T eta_s |epsilon| ||e||_n. Iterating (23)
shows, for k>s,

\[
 \|H_{ka}^{\epsilon}-H_{ka}^{0}\|_n
       \le C_T\eta_s|\epsilon|\|e\|_n.                       \tag{24}
\]

Instead add epsilon e to the complete forward answer Z_sb. The
changes in J,V,f,gamma are bounded by C_T |epsilon| ||e||_n;
the resulting Q change is bounded by the same quantity using the
actual transpose norm. Each resulting state update has its factor
eta_s, so for k>s

\[
 \|V_{ka}^{\epsilon}-V_{ka}^{0}\|_n
       \le C_T\eta_s|\epsilon|\|e\|_n.                       \tag{25}
\]

Both inequalities include changes in every learned rank, every
contraction, the readout, and physical residual feedback. The constants
follow by multiplying 1+L_T eta_k<=exp(L_T eta_k); they do not count
queries. The direct current delta change has bound M_T |epsilon|
||e||_n instead of (25).

Apply fixed-program convergence to a pair consisting of the perturbed
and unperturbed runs, together with e. At epsilon=0 the scalar output
is independent of this unused root e. In the perturbed scalar graph
the sources remain independent of e; e enters its population's
expression exactly by shifting the designated source slot by epsilon e.
Holding selected coefficients fixed, Gaussian integration by parts in
e therefore gives

\[
 \mathbb E[eX^{\epsilon}]
       =\epsilon\mathbb E[\partial_{\mathrm{slot}}X^{\epsilon}].
 \tag{26}
\]

More explicitly, construct the perturbed finite graph by inserting the
single coordinate instruction answer <- answer + epsilon e after that
matrix answer, before computing its descendants. No matrix entry or
old answer is changed. It is one of the independent-root and linear
instructions authorized and proved in Section 3. At every fixed
epsilon, its canonical scalar expression X^epsilon is a function of
independent local roots and Gaussian source groups with deterministic
selected coefficients. In its own population, the new root appears
only in the replacement zeta_sb+epsilon e (reverse forcing) or
xi_sb+epsilon e (forward forcing). Induction through coordinate
instructions, linear memories, and frozen scalar coefficients yields
pointwise

\[
 \partial_e X^\epsilon
       =\epsilon\,\partial_{\mathrm{slot}}X^\epsilon .
\]

Other sources are held fixed in this equality, even if correlated with
the designated source. Their independence from e follows from the
conditioning/source construction in Section 3, which allows arbitrary
independent roots in either population. Their covariance matrices and
all selected coefficients may depend on epsilon; they do not depend
on the local coordinate e. The one-dimensional Gaussian density of e
therefore proves (26) even when the old source covariance is singular.
At epsilon=0 the whole unused-root program has E[eX^0]=0.
No differentiation of selected coefficients with respect to epsilon
is used. The order is: fix the mesh and nonzero epsilon, pass n to
infinity in the actual forced program, apply (26), and only then
decrease epsilon. The fixed-mesh continuity proof in Section 3
identifies the limiting formal derivative with exactly the convention
in (5), including zero initial slots.

At finite width Cauchy--Schwarz bounds
|<e,X^epsilon-X^0>| by ||e||_n||X^epsilon-X^0||_n. Passing to
the scalar law in (24) or (25), dividing by epsilon, and then letting
epsilon tend to zero proves

\[
 |\alpha_{ka,sb}|\le C_T\eta_s\ (s<k),\qquad
 |\beta_{ka,sb}|\le C_T\eta_s\ (s<k),\qquad
 |\beta_{ka,kb}|\le M_T\mathbf1_{a=b}.                        \tag{27}
\]

Continuity of the derivative expectation in this last limit is exactly
the finite scalar-expression/covariance argument in Section 3.2; it
does not require differentiability of a covariance square root at a
rank drop. In (26) selected coefficients can depend on epsilon, but
are constants as functions of the local root e. This is why feedback
derivatives are neither discarded from (24)--(25) nor spuriously
inserted into (5).

Combining (27) with |H|<=B, |V|<=M_T and the gamma bound gives

\[
 |a_{ka,sb}|\le C_T'\eta_s\ (s<k),\qquad
 |b_{ka,sb}|\le C_T'\eta_s\ (s<k),\qquad
 |b_{ka,kb}|\le M_T\mathbf1_{a=b}.                            \tag{28}
\]

Thus the absolute sums of all past and current response/rank memories
are uniformly bounded on finite horizons. This is a global finite-time
bound, not merely a small-time response bootstrap.

## 6. Bounded Gaussian remainders and their continuum passage

Equations (4), (6), and (28) imply, uniformly over these meshes and
k eta within T,

\[
 Z_{ka}=\xi_{ka}+m^Z_{ka},\quad |m^Z_{ka}|\le C_T,
       \quad\mathbb E\xi_{ka}^2\le B^2,
\]
\[
 Q_{ka}=\zeta_{ka}+m^Q_{ka},\quad |m^Q_{ka}|\le C_T,
       \quad\mathbb E\zeta_{ka}^2\le M_T^2,
\]
\[
 U_{ka}=F(G_a)+\Gamma_{ka}+m^U_{ka},\quad |m^U_{ka}|\le C_T,
       \quad\mathbb E\Gamma_{ka}^2\le C_T.                    \tag{29}
\]

Here Gamma_ka=sum_{r<k,b} C_ab gamma_rb zeta_rb is Gaussian,
independent of G, with variance bounded by
(sum |C_ab gamma_rb| M_T)^2. All remainders are actual bounded
random variables; independence of a remainder and its Gaussian part
is not asserted. In particular these formulas do not assert conditional
Gaussianity of an evolved field. Since g is 1-Lipschitz,

\[
 |g(U_{ka})|\le |G_a|+|\Gamma_{ka}|+C_T.                       \tag{30}
\]

Thus Q,Z,g(U) have uniform Gaussian tail upper bounds, with constants
depending on T, and U has all moments with a cubic-Gaussian tail bound.
For example P(|Q|>C_T+x)<=2 exp(-x^2/(2M_T^2)) when M_T>0;
the zero-variance case is interpreted directly.

These decompositions survive the time limit on the common space.
For different queried inputs h,h', their jointly constructed forward
sources satisfy ||xi_h-xi_h'||_2=||h-h'||_2, by (6). The analogous
identity holds for reverse sources and their inputs V. Consequently
these source assignments extend as Gaussian isometries on the closed
input spans. As the Euler fields converge in L2, their sources converge
in L2 as well. Subtracting from Z,Q gives limiting remainders with the
same essential bounds: an L2 limit of variables bounded by C_T is
bounded by C_T, as follows by extracting an almost-everywhere convergent
subsequence (choose summable squared L2 errors and use Markov).
The Gaussian integrals for U converge by the same isometry and ordinary
L2 Riemann integration. A limit in L2 of jointly Gaussian linear
combinations is Gaussian, since its characteristic functions converge
and their variances converge. Independence from G persists by the
factorization of the joint characteristic functions. This proves (29)
and (30) at every finite population time, with uniform horizon constants.
No nonaffinity or nonlazy conclusion is drawn from these tail bounds.

### 6.1 Optional integral memory representation for the main proof

The row bounds also supply globally locally bounded memory kernels,
if an integral representation rather than bounded remainders is wanted.
There are deterministic measurable kernels a_ab(t,s), b_ab(t,s),
defined for 0<=s<t, with

\[
 \sup_{t\le T}\sum_b\int_0^t
       (|a_{ab}(t,s)|+|b_{ab}(t,s)|)\,ds<\infty                 \tag{30a}
\]

for every T, such that on the canonical spaces, at every t,

\[
\begin{aligned}
 Z_a(t)&=\Xi_a(t)+\sum_b\int_0^t a_{ab}(t,s)V_b(s)\,ds,\\
 Q_a(t)&=\mathcal Z_a(t)+j_a(t)H_a(t)
                     +\sum_b\int_0^t b_{ab}(t,s)H_b(s)\,ds,\\
 j_a(t)&=\mathbb E[w(t)D'(Z_a(t))].
\end{aligned}                                                  \tag{30b}
\]

Xi and mathcal Z are the limiting forward and reverse Gaussian
sources in (29). Thus their joint covariances are E[H_a(t)H_b(s)]
and E[V_a(t)V_b(s)], respectively, with the same group/root
independences. The kernels include learned ranks. Those parts can
equivalently be displayed separately as
c_b(s)E[H_a(t)H_b(s)] and c_b(s)E[V_a(t)V_b(s)].
The instantaneous reverse term j_a H_a is separate and must not be
hidden in an ordinary Lebesgue-density kernel.

Here is an elementary existence argument, so no weak compactness
theorem is being invoked without proof. On a dyadic mesh define the
past kernel to equal a_{ka,rb}/eta_r or b_{ka,rb}/eta_r on its
(t,s) rectangle with r<k, and zero elsewhere. Equation (28) bounds
these kernels in L-infinity on each finite square. Use a countable
orthonormal basis of L2 of that square obtained by applying
Gram--Schmidt to rational step functions. Successively extract
subsequences on which every basis coefficient converges. Every finite
sum of squared limiting coefficients is bounded by the common squared
L2 bound, so their square-summable series defines an L2 function.
Approximation by finite basis sums proves weak L2 convergence.
The limiting function is bounded by the same L-infinity constant:
test the weak convergence with the indicator of a set where it exceeds
that bound, or is less than its negative. There are finitely many
kernels, and a diagonal extraction over integer horizons makes their
local limits consistent. Their support remains s<=t by testing its
complement.

The state, source, and current-term convergences already proved are
strong in L2, uniformly in time. To pass the memory integrals, test
against a finite sum of time-step functions times L2 population fields.
For example the scalar test of a kernel has the form
1_{s<t}<V_b(s),v(t)> and is in L2 of the finite square.
Weak kernel convergence applies to this test. Replacing V^h by V
costs at most a constant times sup_s||V^h(s)-V(s)||_2, which
tends to zero. Density of these tests gives (30b) for almost every t.
The rank-density parts above converge strongly, so they may be
subtracted before or after this weak limit.

One can choose row representatives satisfying (30b) at every time.
For an exceptional t, approach it by nonexceptional t_l and extend
their kernel rows by zero to a common finite s interval. The same
orthonormal-basis extraction gives a weak L2 row limit, with the same
essential bound and with support s<=t. The fields, sources and
j_a(t)H_a(t) are continuous in L2, so testing these rows against
V_b(s) or H_b(s) gives the required equality at t. Set the time-zero
rows to zero. Changing rows on the exceptional null set preserves
joint measurability in the completed Lebesgue product space and all
local integral statements; each chosen row is itself measurable.
This proves the every-time version with locally uniform row bounds.

Individual kernel representatives need not be unique, especially at
singular sample covariance. No full-sequence convergence or uniqueness
of uncontracted coefficient densities is asserted. The Gaussian
sources, fields, and contracted memories in (30b) are canonical
full-sequence limits by Sections 4 and 7--10. The extraction here is
only a representation of those already unique objects, not a
subsequence definition of the population flow.

## 7. Global autonomous population flow and deterministic mesh passage

Use the canonical A0 of Section 4, U0a=F(G_a), and w0=0 as the input
to A. The hypotheses are satisfied: U0 is in L2, ||A0||<=8, and
w0 is bounded. A constructs a unique global physical flow, in

\[
 H1^m\times HS(H1,H2)\times H2,
 \quad\text{operator coordinate }A(t)-A0,
 \quad m=2\text{ or }1,                                     \tag{31}
\]

using m=1 on the antiparallel invariant subspace. Equivalently keep
both sample fields with their constraint. For reference the equations
are (2), with the continuous updates

\[
 \dot U_a=\sum_b C_{ab}c_bQ_b,\quad
 \dot A=\sum_b c_bV_b\otimes H_b,\quad
 \dot w=\sum_b c_bJ_b,\quad c_b=-2(f_b-y_b).                  \tag{32}
\]

On either special-angle invariant state these are exactly raw physical
GF after the F change of coordinate. A proves loss dissipation, so
L(0)=2 and the total control action through T is at most 4T.
In particular

\[
 \|w(t)\|_\infty\le4BT,\qquad
 \|A(t)\|\le8+8B^2T^2.                                     \tag{33}
\]

All meshes in the countable construction obey exactly their identified
Euler equations with this same operator and adjoint, by (20)--(22).
The deterministic result A Section 7 consequently gives

\[
 \sup_{t\le T}\left(
  \sum_a\|U_a^h(t)-U_a(t)\|_2+
  \|A^h(t)-A(t)\|_{HS}+\|w^h(t)-w(t)\|_2\right)\le C_T h.
 \tag{34}
\]

Here h is maximum step, with transformed linear interpolation; using
nonuniform steps changes the sum of local errors from N h^2 to
sum eta_k^2<=h(T+h). The transformed velocities converge with the
same bound. This is a deterministic estimate on a single probability
space, not a compactness/subsequence construction. Any further fixed
mesh can be adjoined to the same countable family. Its joint laws are
already fixed by Section 3 and it satisfies (34). Thus the resulting
flow law and its limit do not depend on the choice of meshes.

At a reached time t0 the state has U(t0) in L2, A(t0) bounded, and
w(t0) in L-infinity. A's uniqueness and restart apply with precisely
that state. The original root, operator, learned increments, and
correlations persist. Restart does not mean resetting w to zero or
replacing old source slots by new independent Gaussians. A also proves
that every ordinary-L2 solution of the original integral equations
automatically satisfies F(z(t))=F(z(0))+integral cQ in L2; uniqueness
is therefore not restricted to an artificially smaller cubic class.

## 8. Observables, products, probes, and path topology

Let z_a=g(U_a), h_a=H_a, and use Z_a,J_a for the second hidden layer.
The backward fields are V_a,Q_a and d_a=D(z_a)Q_a. The kernels are

\[
 K^{(1)}_{ab}=C_{ab}\langle d_a,d_b\rangle,\quad
 K^{(2)}_{ab}=\langle V_a,V_b\rangle\langle H_a,H_b\rangle,
 \quad K^{(3)}_{ab}=\langle J_a,J_b\rangle.                    \tag{35}
\]

At a fixed mesh all these fields and contractions converge with their
joint laws. For d, the map (z,Q)->D(z)Q has polynomial growth; it
is an observable, not a new unbounded-Lipschitz query. Joint convergence
with moments from Section 3 covers it.

The elementary product estimate needed in time is the following.
If |a|,|a'|<=M, a-a' tends to zero in L2, and b has uniformly
integrable squares, then

\[
 \|(a-a')b\|_2^2
 \le R^2\|a-a'\|_2^2+4M^2\mathbb E[b^2\mathbf1_{|b|>R}].      \tag{36}
\]

This holds for empirical normalized sums as well. Split at |b|=R
and then let R increase. For two products first split ab-a'b' as
a(b-b')+(a-a')b'. Uniform L2 bounds alone do not suffice for the
second term. In particular no blanket L2 Lipschitz claim for D(z)Q
is made.

A fixed admissible probe is a node of a finite program on the same
initial matrices and roots: smooth globally Lipschitz cylinder maps,
normalized contractions, either orientation of the initial matrix,
and learned ranks are allowed. This includes any fixed finite list of
bounded smooth functions of the observed fields. It also includes
their L2 limits when approximated by such nodes, provided the finite
empirical approximation errors vanish uniformly in probability as the
approximation is removed. The definition excludes arbitrary
width-dependent directions chosen outside this information.

For example the hidden velocities require the probe

\[
 P_a=A\dot H_a,\qquad
 \dot z_a=D(z_a)\dot U_a,\quad
 \dot H_a=D(z_a)^2\dot U_a,\quad
 \dot Z_a=\dot A H_a+A\dot H_a,\quad
 \dot J_a=D(Z_a)\dot Z_a.                                   \tag{37}
\]

At fixed mesh, truncate each Q in dot H smoothly to [-R,R]. The
truncated input is a globally Lipschitz cylinder function of the
existing fields. Its untruncated input error tends to zero in L2
uniformly in probability over n, by Section 3's higher moments.
Multiplying that error by ||A|| preserves convergence. Thus the true
untruncated forward probe has its canonical joint W2 limit. The same
argument works in the transpose direction and on the common space
using (21). Bounded multiplication in the last identity of (37) is
justified by (36). This proves fixed-mesh identification of all the
velocities in (37), without an Lp bounded-operator assumption.

We record a moment bound useful for making the later width/time
passage precise. For finite GF with zero readout, replace A0,n for
this estimate alone by

\[
 \bar A_{0,n}=A_{0,n}\min(1,8/\|A_{0,n}\|).
 \tag{38}
\]

The replacement equals the original with probability tending to one.
The radial map in (38) is 2-Lipschitz in operator norm: subtract the
two scaled operators, assume one norm is larger, and bound the change
of the scaling factor by the difference of the norms. Thus perturbing
the unscaled Gaussian matrix by E changes (38) in operator norm by
at most 2||E||_F/sqrt(n). A's stability, with bounded initial operator
and readout, gives for each of

\[
 X=(U,z,H,Z,J,w,V,Q)                                         \tag{39}
\]

a uniform-in-time normalized L2 perturbation bound C_T times the
initial operator-norm and root-L2 perturbations. Hence each coordinate
functional sup_{t<=T}|X_i(t)| is C_T-Lipschitz in the unscaled
Gaussian matrix parameters. It is also C_T-Lipschitz in the ordinary
Euclidean norm of the stored root arrays: the factor sqrt(n) to
bound one coordinate cancels their normalized L2 factor.

The normalized RMS of these coordinate suprema is bounded by
C_T(1+sum ||R_l||_n). To verify this, each field in (39) is absolutely
continuous in L2 and

\[
 \|\sup_t|X(t)|\|_2
       \le\|X(0)\|_2+\int_0^T\|\dot X(t)\|_2dt.             \tag{40}
\]

All derivatives on the right have deterministic horizon bounds apart
from the initial root term. For Q use
dot Q=dot A* V+A*dot V, with
dot V=dot w D(Z)+wD'(Z)dot Z; use (37) for dot Z. Every
multiplier here is bounded and every operator acts in L2. Pointwise
absolute continuity follows from these L2 integral bounds and Fubini.

Apply the conditional Gaussian inequality (11) to these supremum
functionals. The permutation and mean argument (13), now using the
root Lipschitz constant C_T and (40), proves

\[
 \sup_n\mathbb E\frac1n\sum_i
             \sup_{t\le T}|\bar X_i(t)|^p<\infty
                  \quad(p<\infty).                           \tag{41}
\]

Nonsmooth suprema cause no issue: their scalar Lipschitz constant
follows directly from stability and (11) holds by smooth approximation.
The same argument applies to transformed Euler nodes, uniformly over
small meshes: iterate (23), and replace (40) by the sum of successive
L2 increments, bounded by C_T sum eta_k. Initial U contributes its
root norm. Linear interpolation and bounded Lipschitz field evaluation
preserve the bound. To include the actual finite readout, clip its
initial coordinates to [-1,1] for this moment argument and include
them as iid all-moment local roots; the modification is again absent
with probability tending to one. This proves (41) in probability for
the actual unmodified fields. For d use |d|<=|Q| rather than claiming
that d is Lipschitz in the state.

In particular the squares of the suprema of Q are uniformly integrable
in probability. This supplies (36) uniformly in physical time when
passing between finite GF, fixed-mesh Euler, and the population flow.
It also upgrades joint W2 convergence of the paths in (39) to every
fixed finite Wasserstein order: truncate the path norm at R and use
(41) with a larger moment for the tails. No such upgrade for arbitrary
unbounded operator probes or their velocities is needed or asserted.

For clarity about the path assertion, work in C([0,T];R^d) with the
supremum norm, separately for each neuron population, including both
sample indices in its tuple. For an absolutely continuous scalar path
and its polygonal interpolant on an observation grid of maximum spacing
delta,

\[
 \|X-\Pi_\delta X\|_{\infty}^2
       \le4\delta\int_0^T|\dot X(t)|^2dt.                    \tag{42}
\]

On an interval use Cauchy--Schwarz on the integral of dot X and the
two endpoint interpolants, then bound the maximum by the sum over
intervals. Averaging gives the same inequality for empirical measures.
The uniform L2 derivative bounds just proved apply to (39). For d,
path convergence instead uses its continuity as the bounded product
of z and Q on path space and the Q path-norm uniform integrability.
Thus convergence on a fixed finite observation grid, followed by
(42), gives joint W2 convergence of these same-neuron path laws.
This is a constructive transport argument, requiring no compactness
theorem on path measures.

## 9. Full-sequence width/time passage and the random initial readout

First keep finite readout zero. On ||A0,n||<=8, A's deterministic
Euler/GF estimate compares finite GF with fixed-mesh transformed
Euler by C_T h in the state metric, uniformly over n. The same bound
holds on the population common space by (34). At finitely many
observation times, a finite neuron coupling bounds W2 distance by the
normalized L2 field difference for (39). Consequently

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \mathbb P\{W_2(\mu^{GF}_{n,\mathrm{obs}},
                      \mu_{\mathrm{obs}})>\varepsilon\}=0.  \tag{43}
\]

To see that this is full-sequence convergence, fix epsilon first;
choose a deterministic h making both deterministic errors smaller
than epsilon/3. Section 3 makes the middle, fixed-h width error
smaller than epsilon/3 in probability for all sufficiently large n.
The exceptional norm event tends to zero by (12). There is no
subsequence in this argument. Equations (36), (41), and (42) extend
(43) to d and the joint path laws; the tail argument after (41)
gives their finite Wp versions. Mixed finite-time polynomial-growth
observables also converge, using a larger moment to truncate tails.

For the initial readout b0,n actually required by the model, a union
bound on Gaussian tails gives

\[
 \mathbb P\{\|b_{0,n}\|_\infty>\sqrt{6\log n}/n\}\le2n^{-2}.
 \tag{44}
\]

Couple finite GF from b0,n and from zero using the same matrices and
root fields. Both are within A's horizon bounds on ||b0,n||_infty<=1.
A's L2 stability gives a uniform state error C_T||b0,n||_n, tending
to zero. The path and product arguments above transfer the entire
observable list, including velocities as below. Thus zero population
readout has been identified from the canonical random finite readout;
it has not replaced that finite initialization in the asserted model.

Uniformity in time for scalar predictions and the three kernels
follows from the same estimates and finite observation grids. For K1
use (36) and the Q square-tail bound; K2 and K3 follow directly from
bounded-field L2 estimates. For admissible fixed probes, use their
finite-program identification and the operator bound, with truncation
as specified in Section 8. Joint convergence holds for any fixed finite
collection of such observables, times, populations, and probes.

One can also take transformed Euler with any deterministic mesh sizes
h_n tending to zero jointly with n: compare that Euler sequence to
its finite GF by A's width-independent estimate, then apply (43).
No relation between n and h_n is needed for transformed Euler. The
raw-GD claim below uses the stated eta=n^-2, for which A explicitly
controls the cubic defect.

### 9.1 Original velocities and their energies

The raw first velocity is dot z_a=D(z_a) sum_b C_ab c_b Q_b.
At rho=-1 this is its one independent field with coefficient -4r.
First compare finite GF with a fixed-mesh evaluation of this formula.
Q is L2-Lipschitz in the transformed state on bounded sets, while
the remaining product converges by (36) and (41). This gives an error
tending to zero, uniformly in time and in probability in the iterated
width/mesh limit. The same proof applies to dot H=D(z)dot z.
The rank-one formulas give direct HS/L2 convergence for dot A and
dot w. The identity for dot Z in (37) then gives L2 convergence
using only the operator bound.

There is one further uniform-integrability step for dot J; it cannot
be skipped. At every fixed mesh, the probe construction in Section 8
gives joint W2 convergence of dot Z, hence convergence of its second
moment and uniform integrability of its squares in probability. A
finite mesh has only finitely many such probes. The preceding L2
comparison of dot Z to its fixed-mesh evaluations tends to zero as
the mesh is refined, uniformly in time in the width limsup. This
implies uniform integrability of the GF dot Z squares in that same
limsup. Explicitly, if x is L2-close to y, split

\[
 |x|^2\mathbf1_{|x|>R}
 \le4|x-y|^2+2|y|^2\mathbf1_{|y|>R/2};                       \tag{45}
\]

first fix a sufficiently fine comparison mesh, then let R increase,
and finally refine that mesh. Apply (36) with b=dot Z to conclude
the L2 comparison of dot J=D(Z)dot Z. The same argument works on
the population common space (a continuous L2 path has uniformly
integrable squares, by a finite cover with L2 balls and (45)).

This proves convergence of each original hidden-field velocity law
in W2 at fixed times and of its squared L2 norm, uniformly in time
in probability, with the natural one-sided convention for mesh
velocities. For scalar norms uniform convergence follows by choosing
one comparison mesh and using its finitely many convergent
contractions. Integration over [0,T] then proves convergence of
each velocity energy, since the horizon and L2 velocity bounds are
fixed. Equivalently, velocity fields may be included jointly in the
L2([0,T]) mean-square comparison and in integrated quadratic tests.
Continuity in time of the limiting L2 velocities follows from the
same bounded-multiplier/product argument. A C-path law for discontinuous
Euler velocities is not asserted.

The raw parameter energy metrics are exactly

\[
 \frac d n\|\dot W^{(1)}\|_F^2
   =\sum_{a=1}^{m}\|\dot z_a\|_n^2,\quad
 \|\dot W^{(2)}\|_F^2=\|\dot A\|_{HS}^2,\quad
 \frac1n\|\dot W^{(3)}\|_2^2=\|\dot w\|_n^2,                 \tag{46}
\]

where m=1 at rho=-1. The middle velocity is a finite sum of rank-one
operators, so its squared HS norm is the corresponding product of
two within-population Gram matrices; those contractions converge.
Their time integrals converge as well. The limiting GF satisfies
exactly A's loss-energy identity. Parameter increments in these same
metrics follow by integrating their velocities or, for A, by the
rank integral. These claims concern increments of A; A0 need not be HS.

## 10. Exact raw GD and the final bridge

Now use the actual canonical finite initialization, eta=n^-2, and
linear interpolation of the raw matrices, with hidden fields recomputed
from those matrices. A Sections 8--9 prove, on events of probability
tending to one, uniformly through T,

\[
 \|Y_n^{GD}-Y_n^{GF}\|_{\mathcal E_{HS}}=O_T(n^{-3/2}),
 \tag{47}
\]

for the recomputed cubic coordinate, learned operator increment, and
readout. The comparison GF uses exactly the same finite random
readout. A obtains (47) from the exact cubic identity

\[
 F(z+\eta cD(z)Q)-F(z)
 =\eta cQ+\eta^2c^2zD(z)^2Q^2
                         +\eta^3c^3D(z)^3Q^3/3.
\]

The defect sums to O_T(n^-3/2), since ||Q||_infty<=sqrt(n)||Q||_n,
|z|D(z)^2<=1, and its first-exit bootstrap provides the needed
operator, readout, and residual bounds. The raw interpolation defect
is included in A's estimate; it is not silently replaced by transformed
Euler interpolation.

A further proves raw first and hidden-field velocity errors O_T(n^-1),
operator/readout velocity errors O_T(n^-3/2), and the corresponding
kernel and energy comparisons. These finite-width estimates are
legitimate uses of a sqrt(n) coordinate bound with a faster vanishing
state error; they are distinct from the mesh-uniform population product
argument (36). At a mesh node use the right velocity, and at a terminal
endpoint use the left velocity. Combining these comparisons with
Section 9 proves the full-sequence joint width/raw-GF bridge claimed
in Section 1.

For hidden and backward path laws the same-neuron GD/GF coupling also
converges in the supremum-path W2 metric: A supplies the hidden-path
velocity comparison, and for the L2-Lipschitz state fields a coordinate
supremum is at most sqrt(n) times the uniform normalized field error
in (47), which is O_T(n^-1). The d product is covered by its direct
finite velocity/backward-product comparison or by (36). Higher finite
path orders for (39) and d follow from this coordinate comparison and
the moment bound (41). Predictions, loss, kernels, fixed admissible
operator probes, and the velocity-energy observables therefore retain
the actual random initialization in the final theorem.

All assertions are on an arbitrary fixed T<infinity. Applying them
to any finite collection of horizons, or to increasing integer
horizons with the already constructed single flow, introduces no new
initialization and no subsequence selection. They do not assert a
rate uniform as T tends to infinity or an interchange with a
long-time training limit.

## 11. Discharged obligations and remaining scope

The canonical Gaussian fixed-program law, all source/sample slots,
current reverse response, learned rank memories, polynomial-root
adaptation, mesh-uniform expected responses, canonical bounded
common-space operator with true adjoint, deterministic global mesh
passage, autonomous restart, full-sequence width/GF convergence, and
the listed raw-GD observable bridge are proved above, using exactly A
and P as specified. In particular no unproved uniform-in-query tensor
program theorem or arbitrary bounded-operator substitution remains.

The following are outside this result and are not disguised as its
consequences: intermediate input angles; other activations or depths;
all-time distributional nonaffinity/nonlazy learning; arbitrary
width-dependent probes; operator-norm convergence across different
widths; an Lp operator norm for A0 when p differs from 2; an all-time
uniform rate; and all-moment velocity/probe assertions beyond the
W2 and quadratic-energy statements explicitly proved. Nonaffinity
and nonlazy learning were assigned to the main proof. The bounded
Gaussian-remainder estimates in Section 6 are available to that proof.

There is no unresolved mathematical obligation within the precisely
stated special-angle bridge. Its import boundary is the deterministic
lemma A and the elementary fixed-program mechanisms of P, with the
model adaptations proved here. This declaration does not promote any
of the excluded conclusions to a theorem.

### Proof-content SHA-256

Hash convention: SHA-256 of the UTF-8 bytes strictly before the line
`### Proof-content SHA-256`, including the preceding newline. The
dependency snapshots above are whole-file hashes. The proof-content
digest is:

`20f7c2f3c36d810aa9416974a4790eef25d2929e94fbf0b6e0c72bedebc1ddd5`.
