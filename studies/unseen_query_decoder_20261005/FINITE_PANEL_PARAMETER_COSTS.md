# Resource costs of the existing finite-panel compressor

2026-10-06. Scoped theoretical resource audit. This note concerns the
previous finite-panel model, with its original label range and training
flow. It does not extend its accuracy guarantee to undeclared queries.
No experiment, maintained-book edit, or Git mutation was performed.

The complete retained runtime and one evaluation of its vector field have
explicit polynomial costs. A constructive spectral sparsifier also gives
a polynomial preprocessing bound **after source coefficient vectors have
been supplied**. The original authorized coefficient recipe does not give
an operation or peak memory bound for producing those vectors. Thus that
recipe alone does not justify an unconditional polynomial bound for the
entire initialization. A separately specified causal coefficient producer
can be composed with the costs below. All arithmetic statements below use
exact real coordinates; they are not finite-bit complexity results.

## 1. Setup and accounting convention

There are \(m\) training inputs among \(p\ge m\ge d\ge1\) declared inputs,
input dimension \(d\), depth \(L\ge2\), and original hidden width \(n\).
Write

\[
Y=\|y\|_2/\sqrt m,\qquad \lambda=\gamma/m,\qquad
\ell=\log(en),\qquad S=16Y/\lambda,
\]

where \(\gamma>0\) is the training population feature-Gram gap. The
existing finite-panel source theorem uses

\[
\chi=\min\{1,a/[4S^2U_{\rm fin}(S)]\},\qquad
R=\left\lceil3072p\chi^{-1}\ell^{5/2}\right\rceil+2m+d+1.
\tag{1}
\]

Here \(a>0\) is the activation strip width and \(U_{\rm fin}\) is exactly
the explicit activation/depth recurrence in `PANEL_SOURCE.md`, (22),(24).
No input dimension or panel size occurs in that recurrence. Put \(q=9R\)
as a common integer budget; actual layer widths can be smaller. Then

\[
R\le3077p\chi^{-1}\ell^{5/2},\qquad
q\le27693p\chi^{-1}\ell^{5/2}
 <30000p\chi^{-1}\ell^{5/2},\qquad q\ge p\ge m\ge d.
\tag{2}
\]

The exact value of \(\chi\), not an unspecified task constant, is retained
throughout. On the full original label interval, it may be replaced by
the activation/depth-only lower bound \(\chi_{\rm act}\) in
`PANEL_SOURCE.md` (30). Under the simpler sufficient cap

\[
Y\le(\gamma/m)\beta^{-30L},
\tag{3}
\]

the existing proof gives \(\chi=1\). Thus the powers of \(Y\) and
\(1/\gamma\) in the runtime operation count are zero under (3), and can
also be zero uniformly on the full allowance if the explicit
activation/depth factor \(\chi_{\rm act}^{-2}\) is used. This does not
eliminate their dependence in accuracy bounds or sufficient-width gates.

After freezing the calculations below, a separate cross-check of the
full-label lemma in PARAMETER_EXPLICIT_RESOURCES.md verified
\(\chi^{-1}\le\beta^{36L}\). Its five base power bounds in the original
SIMPLE_CONSTANTS_SOURCE_CHECK.md, Sections 1–3, precede the small-activity
substitution; using \(S\le1\) gives \(U_{\rm fin}\le5\beta^{34L}\) and then
\(4S^2U_{\rm fin}/a\le(5/4)\beta^{34L+1}\le\beta^{36L}\).
Consequently every factor \(\chi^{-2}\) below can be replaced explicitly
by \(\beta^{72L}\), every \(\chi^{-1}\) by \(\beta^{36L}\), and every
\(\chi^{-3}\) by \(\beta^{108L}\), on the full original label allowance.
This verification introduces no additional restriction on \(Y\).

Count each scalar addition, subtraction, multiplication, division and
comparison as one arithmetic operation. Square roots used in basis
normalization are stated separately; they can instead be counted as one
additional real primitive. Count each scalar activation or first-derivative
evaluation separately. Let \(D_{\rm alg}\) count the fixed evaluator and
runtime program, including evaluator workspace. An arbitrary abstract
holomorphic function does not automatically possess such an evaluator.

The compact state is

\[
\theta=(A,B^2,\ldots,B^L,w,c),\qquad
c=y-f_C(X)=-r_C\in\mathbb R^m.
\]

Thus \(c\) is the negative of the maintained book's residual \(r_C=f_C-y\).
The number of learned parameter coordinates, excluding \(c\), is at most

\[
P=qd+(L-1)q^2+q.
\tag{4}
\]

All costs concern the corrected-readout model specified in
`EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`, (2)–(4), not an ordinary smaller
network trained by its ordinary gradient.

## 2. Complete retained memory and one training evaluation

The existing inventory, including metrics, their inverses/factors, fixed
copies, data, training and panel arrays, solve buffers, and live observation
workspace, is

\[
M_{\rm retained}\le2048(L+1)R^2+16p(d+1)+D_{\rm alg}
\le2^{36}(L+1)p^2\chi^{-2}\ell^5+16p(d+1)+D_{\rm alg}.
\tag{5}
\]

The core moving state is only \(P+m\); it must not be presented as complete
memory. Equation (5) covers a current state and vector-field workspace.
A numerical integrator retaining extra full stages must count each extra
stage, at most \(P+m\) coordinates, separately.

The following implementation gives a concrete arithmetic bound. The fixed
metrics \(M_j\) are inverted once during initialization. For each training
sample, compute its current nonlinear forward pass. Let \(H\in
\mathbb R^{q_L\times m}\) be the top training-feature matrix and form

\[
G=H^TM_LH,\qquad
G b=y-c-H^TM_Lw,\qquad \widehat w=w+Hb.
\tag{6}
\]

Solve the \(m\times m\) positive-definite system by elimination or LDL
factorization; its gap is part of the inherited fitting theorem. For the
backward pass apply a metric adjoint by three successive products,

\[
(B^{j+1})^*\delta
=M_j^{-1}\bigl[(B^{j+1})^T(M_{j+1}\delta)\bigr].
\tag{7}
\]

There is no need to form a dense product of two \(q\times q\) matrices at
each training evaluation. Compute feature and response Gram matrices from
the cached \(m\) columns, assemble \(K\), and use the original rank-one
update formulas and \(\dot c=-2Kc/m\). The fixed input Gram
\(v_a^Tv_b\), where \(v_a=x_a/\sqrt d\), is prepared once.

Classical matrix multiplication uses at most \(2abc\) scalar arithmetic
operations for an \(a\times b\) matrix times a \(b\times c\) matrix.
The main costs of this implementation are:

| Calculation | Arithmetic upper bound, before lower-order vector operations |
|---|---:|
| Training forward pass | \(2mqd+2(L-1)mq^2\) |
| Top metric product, Gram, and corrected readout | \(2mq^2+2m^2q+4m^3+4mq\) |
| Backward metric adjoints | \(6(L-1)mq^2\) |
| All metric feature/response Grams, allowing duplicated products | \(4Lmq^2+4Lm^2q\) |
| First and hidden parameter velocities | \(2mqd+2(L-1)mq^2\) |

The \(4m^3\) allowance covers one elimination solve, without square roots.
Gate products, sums forming \(K\), \(Kc\), readout velocity, scalar update
factors, and the cache \(M_L\widehat w\) are lower-order terms. More
explicitly, all these operations together fit

\[
\begin{split}
W_{\rm rhs}\le{}&16Lmq^2+4mqd+(4L+2)m^2q+4m^3\\
&+(4L+12)mq+(2L+4)m^2+2P+10m+q\\
\le{}&64Lmq^2.
\end{split}
\tag{8}
\]

The final inequality uses \(L\ge2\), \(m,d\le q\), and \(m\ge1\).
There are additionally at most \(2Lmq\) scalar evaluations of
\(\phi_j\) or \(\phi_j'\). In original parameters a safe rounded bound is

\[
W_{\rm rhs}<2^{36}Lmp^2\chi^{-2}\ell^5,
\qquad
N_{\rm activation}<2^{16}Lmp\chi^{-1}\ell^{5/2}.
\tag{9}
\]

This is a bound per evaluation of the continuous-time vector field. A
fixed-stage explicit method multiplies the first bound by its stage count
and adds its vector updates. It does not establish a step size, number of
steps to a prescribed output error, or a finite-step theorem uniform on
\([0,\infty)\). The original result is a continuous-time approximation.

A feasible live workspace allowance, beyond fixed model/data arrays and
the current state, is

\[
12Lmq+8m^2+2(P+m)+8q+4m+D_{\rm eval},
\tag{10}
\]

where \(D_{\rm eval}\) is the evaluator workspace already counted in
\(D_{\rm alg}\). This allows forward and response arrays, their metric
products, Gram/solve buffers, velocity arrays and vector temporaries.
It fits (5)'s conservative inventory; it is not an extra term to add to
(5). Passive inputs need not be evaluated at every training evaluation.

## 3. Queries, with and without a current readout cache

Cache \(a_C=M_L\widehat w\) for the current state. For a single input,
run the smaller network forward and return \(a_C^Th^L(v)\). Its work is

\[
W_{\rm query}\le2qd+2(L-1)q^2+2q\le4Lq^2
 <2^{32}Lp^2\chi^{-2}\ell^5,
\tag{11}
\]

plus \(Lq<2^{15}Lp\chi^{-1}\ell^{5/2}\) activation calls. Two neuron
buffers, at most \(2q\) real coordinates, suffice beyond the retained
model and current readout cache. Reading a newly supplied input uses \(d\)
coordinates and returning the answer uses one. The original \(pd\) panel
input coordinates remain included in (5).

After a numerical state update, an old readout cache is invalid. Refreshing
it requires the training forward pass, (6), and \(M_L\widehat w\): at
most \(24Lmq^2\) arithmetic operations and \(Lmq\) activation evaluations
are a safe allowance. A query starting only from the core state must
include this cost. The cache can be shared by all queries made at that
same state. Training outputs are already \(y-c\), so obtaining those
\(m\) outputs alone costs at most \(m\) scalar subtractions.

Evaluating all \(p\) panel points sequentially therefore costs at most
\(4Lp q^2<2^{32}Lp^3\chi^{-2}\ell^5\) arithmetic operations after cache
refresh, with the same two neuron buffers and \(p\) output coordinates.
This observation work is optional and separate from the training RHS.
The same computational forward pass accepts another input, but the
finite-panel approximation theorem gives no accuracy guarantee there.

## 4. Constructive selection once the source vectors exist

The source packet originally imported a selection interface without its
algorithm. A read of that packet alone therefore does not yield a
selection-time bound. The following independent reconstruction supplies
one using a published constructive theorem; it supersedes only that
initial cost limitation, not the coefficient-production limitation.

For one layer let the finite supplied source vectors span \(E\subseteq
\mathbb R^n\), of dimension \(r\le\min(R,n)\), including the constant
vector. Construct a basis matrix \(U\in\mathbb R^{n\times r}\) satisfying
\(U^TU/n=I_r\). Its normalized rows \(u_i^T/\sqrt n\) satisfy the exact
decomposition of the identity required by the vector form of the
Batson–Spielman–Srivastava theorem. With sparsity parameter nine, that
theorem constructs nonnegative weights, supported on at most \(9r\)
rows, with distortion at most four. Its barrier algorithm has \(9r\)
iterations. These are Theorem 3.1 and the algorithm paragraph on printed
pages 5 and 15 of [Twice-Ramanujan Sparsifiers](https://arxiv.org/pdf/0808.0163).

Let \(V\in\mathbb R^{q_j\times r}\) be the selected rows of \(U\), let
\(s_i>0\) be the selected weights, and set

\[
D=\operatorname{diag}(s_i/n),\qquad Q=V^TDV,
\qquad I_r\preceq Q\preceq4I_r.
\]

Define the exact-isometry metric using only matrix arithmetic:

\[
M=D+DV(Q^{-2}-Q^{-1})V^TD.
\tag{12}
\]

Then \(V^TMV=Q+Q(Q^{-2}-Q^{-1})Q=I_r\). To check its bounds, set
\(Z=D^{1/2}V\). The symmetric matrix

\[
D^{-1/2}MD^{-1/2}=I+Z(Q^{-2}-Q^{-1})Z^T
\]

is the identity on the orthogonal complement of \(\operatorname{range}Z\).
On that range its eigenvalues are those of \(Q^{-1}\), as is seen by
using the orthonormal basis \(ZQ^{-1/2}\). They lie in \([1/4,1]\), so
\(D/4\preceq M\preceq D\). Restriction is therefore an exact isometry
for \(u^Tv/n\), with precisely the metric comparison needed by the
runtime. Inclusion of the constant gives \(\|\mathbf1\|_M=1\). This
checks every required selection hypothesis, not only full column rank.

Here is a conservative explicit operation bound for implementing that
theorem in the exact-real model. In each barrier iteration, recompute
four \(r\times r\) inverses, two matrix squares and the relevant traces.
Evaluate four quadratic forms per candidate row and choose an admissible
positive update. These operations fit \(24r^3+40nr^2\le64nr^2\);
\(9r\) iterations fit \(576nr^3\). Allowing initialization, comparisons,
weight aggregation and rescaling gives

\[
W_{\rm select}\le1024nr^3.
\tag{13}
\]

This is a direct conservative count of classical arithmetic in the cited
barrier algorithm, not a hidden constant in its published big-O bound.
It needs at most \(nr+n+10r^2\) real coordinates for basis rows, weights,
barrier matrices and their scratch. Forming (12) costs at most \(400R^3\)
further arithmetic operations and can use \(400R^2\) scalar workspace.
All comparisons are exact; no bit-precision guarantee is implicit.

## 5. The remaining post-source preprocessing

Do the preceding selection at every layer. Write \(U_j^TU_j/n=I\),
\(V_j=R_jU_j\), and let \(W_0^j\) be the original dense initial mixer.
The initialized compressed mixer can be formed without storing an
\(n\times n\) projection:

\[
C_j=U_j^TW_0^jU_{j-1}/n,\qquad
B_0^j=V_jC_jV_{j-1}^TM_{j-1}.
\tag{14}
\]

Indeed \(V_{j-1}^TM_{j-1}\) is the left inverse of \(V_{j-1}\) on
its source image; \(U_jU_j^T/n\) is the original source projection.
Thus (14) is exactly `PANEL_SOURCE.md` (16). Its forward and adjoint
paired-image identities and operator bound are unchanged. The first
array is simply the selected rows of \(A_0\).

Given at most \(R\) source columns per layer, exact Gram–Schmidt with
dependent columns discarded uses at most \(10LnR^2\) arithmetic
operations, and at most \(L(R+1)\) square roots for normalization.
Forming all \(W_0^jU_{j-1}\) costs at most \(2(L-1)n^2R\), the contractions
at most \(2(L-1)nR^2\), and reduced assembly at most \(400(L-1)R^3\).
Forming the fixed metric inverses costs at most \(4Lq^3\le3000LR^3\).
Including selection, metric correction, normalization, input Gram and
array assembly, one safe combined bound is

\[
\begin{split}
W_{\rm after\ source}\le{}&
2(L-1)n^2R+12LnR^2+1024LnR^3\\
&+5000LR^3+2m^2d+20p(d+1),
\end{split}
\tag{15}
\]

plus those square roots and any activation evaluations required if exact
initial feature additions were not included in the supplied source packet.
Initial training forward evaluation then adds at most
\(2mnd+2m(L-1)n^2\) arithmetic operations and \(Lmn\) activation calls.

For the straightforward materialized implementation, post-source peak
memory is bounded, conservatively, by

\[
\begin{split}
M_{\rm after\ source}\le{}&(L-1)n^2+nd+n
 +(2L+2)nR+500LR^2\\
&+pd+m+m^2+D_{\rm compile}.
\end{split}
\tag{16}
\]

Here dense initialization, supplied source columns, bases, a dense image
buffer, selected arrays, weights and scratch are counted. \(D_{\rm compile}\)
is the fixed program and activation/jet evaluator workspace at this phase.
In particular, initialization is not claimed to use the much smaller
retained runtime memory (5). Equations (15)–(16) are upper bounds for this
implementation, not lower bounds against all possible streaming methods.

Substituting (1) or (2) into (15) exposes every parameter dependence. The
selection term is at most \(1024L n(3077p\chi^{-1}\ell^{5/2})^3\), so it
has degree three in \(p\), while the dense mixer term has degree one in
\(p\). There is no exponential dependence on input dimension in this
post-source construction.

## 6. What the original coefficient recipe leaves unquantified

The source space contains finitely approximated time-Chebyshev coefficient
vectors, paired with exact initialized mixer images. Its source accuracy
is \(1/n\). The inherited recipe asks for preimage coefficient accuracy,
for example,

\[
\frac{1}{128n^{3/2}(K+1)},\qquad
K=\left\lceil\frac{128\ell^{3/2}}\chi
 \log\frac{8192M_0n^{3/2}\ell^{3/2}}\chi\right\rceil.
\tag{17}
\]

It obtains these approximations from finite initial-jet continuation and
quadrature, using initial weights, training data and declared panel inputs.
It explicitly permits arbitrarily large finite preprocessing. It does not
specify a certified numerical algorithm with a bound on jet order,
quadrature evaluations, precision, activation-jet cost, or peak memory.
The existence of a positive analytic radius proves that a finite
construction is possible under its evaluator interface; it alone supplies
none of those operation counts.

Let \(W_{\rm source}\) and \(M_{\rm source}\) be, respectively, the work and
peak memory of a specified coefficient producer. Then the honest composed
statement is

\[
W_{\rm init}\le W_{\rm source}+W_{\rm after\ source},\qquad
M_{\rm init}\le\max\{M_{\rm source},M_{\rm after\ source}\},
\tag{18}
\]

when the coefficient phase releases its extra scratch before assembly and
its stated peak includes its output columns. The first terms cannot be
replaced by a polynomial in the problem parameters solely by citing the
original source packet. This is a **coefficient-production** limitation of
that recipe: constructive coordinate selection has the explicit bound
(13). A new causal producer with certified source accuracy can supply the
missing terms in (18); this note makes no negative claim about such a
producer.

Nor can a finite-bit storage or work bound be read off the real counts.
Such a result needs a computable representation of activations and random
initialization, perturbation control for the source rank and selection,
conditioning of the selected metrics, and stable finite-precision
integration and query evaluation. The diagonal metric comparison controls
gates but gives no lower bound on individual diagonal weights. The training
Gram gap addresses one inverse, not all those representation issues.

## Source pointers and status

- `finite_panel_absolute_compression_20261005/RESULT.md`, lines 384–408:
  complete retained storage; lines 410–454: width and arithmetic limitations.
- `finite_panel_absolute_compression_20261005/PANEL_SOURCE.md`, lines
  258–286: finite coefficient provenance and admitted preprocessing cost;
  lines 288–333: exact selection interface and initialized operators;
  lines 590–727: localized \(\chi\), rank, full-label and simpler-cap bounds.
- `integrated_general_compression_20261004/EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`,
  lines 40–76: forward, corrected readout, metric adjoint and autonomous
  update equations used for every runtime count.
- [Batson–Spielman–Srivastava, Theorem 3.1 and printed page 15](https://arxiv.org/pdf/0808.0163):
  external constructive vector sparsification used in Section 4.

The runtime arithmetic and explicit metric reconstruction are new
internally checked derivations in this audit, not independently reviewed
promotion results. The stochastic source event and continuous-time error
theorem remain inherited. Required canonical-notation instructions at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` were
permission-inaccessible even on a read-only escalation; the supervisor
directed use of the explicit repository contract and maintained notation.
The rigorous-math and research-audit skills were read and applied.

## Post-freeze check: a counted coefficient producer closes the arithmetic bound

The supervisor subsequently supplied the physical collocation construction
in PHYSICAL_PARAMETER_ACCOUNTING.md and the concrete assembly in
PARAMETER_EXPLICIT_RESOURCES.md for a post-author cross-check. Both current
notes were read. This check is not an isolated promotion review. It
preserves Section 6's finding about the original recipe and verifies that
the newly specified producer supplies its missing arithmetic terms.

Use the original finite-panel temporal degree \(K\), analytic Fourier
radius \(\alpha=\chi/(128\ell^{3/2})\), and coordinate amplitude
\(M_0\sqrt n\). In particular \(0<\alpha\le1\), \(M_0\ge1\), and

\[
E:=e^{\alpha K}\ge64M_0n^{3/2}/\alpha.
\tag{19}
\]

Let \(Q\) be the least power of two at least \(2(K+1)\), so that
\(2(K+1)\le Q\le4(K+1)\). Sample at the Gauss–Chebyshev time nodes
of the original interval \(0\le t\le32\ell/\lambda\), compute the
discrete cosine coefficients, and retain degrees zero through \(K\).
This changes the coefficient algorithm, not the retained source degree.

For a true source coordinate, Fourier/Chebyshev coefficient decay gives
absolute coefficient bound \(2M_0\sqrt n e^{-\alpha j}\).
At the \(Q\) root nodes the only aliases of retained frequency \(j\)
are \(2sQ-j\) and \(2sQ+j\), for \(s\ge1\), with signs. Therefore the
sum of the errors of all retained coefficients is bounded by

\[
\frac{4(K+1)M_0\sqrt n\,e^{-\alpha(2Q-K)}}
     {1-e^{-2\alpha Q}}.
\tag{20}
\]

Here \(2Q-K\ge3K+4\), and the denominator is at least \(1/2\) by
(19). Also \(K+1\le2E/\alpha\), since
\(\alpha(K+1)\le\alpha K+1\le e^{\alpha K}\).
Consequently (20) is at most

\[
\frac{16M_0\sqrt n}{\alpha E^2}
\le\frac{\alpha}{256M_0n^{5/2}}
\le\frac1{256n}.
\tag{21}
\]

The original truncation tail is at most \(1/(16n)\). If every computed
node value has coordinate error at most \(\delta\), its degree-zero
coefficient error is at most \(\delta\), and each other coefficient
error is at most \(2\delta\). Thus their total contribution is at most
\((2K+1)\delta\). For example \(\delta=1/[256n(K+1)]\) gives
\(1/(128n)\); the assembly's looser \(\delta=1/(64Qn)\) gives
at most \(1/(32n)\). Both leave ample room inside the original \(1/n\)
source tolerance. Exact initialized source-image identities are maintained
by applying the same linear cosine sums to preimages and images, or by
forming the latter as exact initialized-matrix images of the computed
preimage coefficients.

For clarity, the parameter-error norm used for this generation is

\[
D=\frac{\|\Delta A\|_F}{\sqrt n}
  +\sum_{j=2}^L\|\Delta W^j\|_F
  +\frac{\|\Delta w\|_2}{\sqrt n}.
\tag{22}
\]

The physical solver's projections keep both real network evaluations
inside the original operator/readout bounds. Forward subtraction bounds
the preactivation RMS error by \(P_jD\). A backward subtraction has a
changed-readout term, a changed-mixer term, and a gate term bounded by
\(\|\phi_j''\|_\infty\sqrt n\,S k_jP_jD\). The last term uses only the
actual carrier's RMS bound \(Sk_j\), converted to a coordinate bound.
It is added once per recursion layer, rather than multiplying a new
\(\sqrt n\) at each layer. The source recurrences
\(P_j\le\beta^{3L}\), \(k_j,\tau_j\le\beta^{4L}\), and operator bound
ten therefore give, with substantial slack,

\[
\max_{\text{all four families, all coordinates}}
 |\text{computed source}-\text{actual source}|
\le\beta^{100L}(\sqrt n+Sn)D.
\tag{23}
\]

The initialized forward and transpose image factors eight are included
in this bound. Only the original first and second derivative bounds are
needed; the current physical note uses that same \(\beta\).

The originally proposed tolerance
\(D\le Y/[8192\beta^{100L}n^2(K+1)(1+Y)]\) would already give
node error at most \(1/[4096n(K+1)]\), by \(S\le1\) and
\(\sqrt n\le n\). The final assembly instead chooses

\[
D\le\frac{Y\beta^{-200L}}{(Q+1)n^3},
\tag{24}
\]

which also suffices. Indeed the normalized-input Gaussian moment
recursion gives
\(\sqrt{q_j}\le|\phi_j(0)|+\|\phi_j'\|_\infty\sqrt{q_{j-1}}\),
with \(q_0=1\), hence \(q_L\le4\beta^{2L}\le\beta^{3L}\).
Since \(\gamma\le q_L\) and \(16Y/\lambda=S\le1\),
\(Y\le\beta^{3L}\). Combining (23)–(24) gives node error at most
\[
\frac{2Y\beta^{-100L}}{(Q+1)n^2}
\le\frac1{64Qn}.
\]
The truncation, alias, numerical-node, and optional coefficient-arithmetic
allowances used in the assembly sum to at most
\((16+1+8+8)/(256n)<1/n\). In the exact-real construction the last
allowance can be zero. The initialized training features, their exact
images, first-weight columns, and constant are still added exactly.

The collocation solver must cover the entire original normalized interval
\(0\le\lambda t\le32\ell\); a shorter endpoint-fitting horizon would
not suffice for this source construction. The assembly explicitly uses
that full interval. It processes the quadrature nodes in increasing
time and discards completed dense patches. Cosine sums can be accumulated
as the nodes are reached. Because \(Q\) is a power of two, its real
quadrature constants can also be generated by half-angle square roots
and trigonometric recurrences; no uncharged arbitrary function is needed
to represent those constants in the exact-real model.

Put
\[
Z=\ell+\log\!\bigl(e+\beta^{100L}(1+m/\gamma)\bigr).
\tag{25}
\]
The additional accuracy in (24) changes the physical solver's logarithmic
factor only by a universal multiple: its extra terms are
\(\log(Q+1)\), \(200L\log\beta\), and \(3\log n\), and
\(Q\le C\beta^{36L}\ell^{5/2}\).
The supplied physical construction has at most
\(C\beta^{300L}(1+m/\gamma)^3Z^6\) field stages and at most
\(C\beta^{100L}(1+m/\gamma)Z^{3/2}\) collocation nodes on a patch.
In this paragraph and the remaining resource displays \(C\) is a
universal numerical constant, not a scientific-parameter constant.

For the direct collocation implementation, multiplying the stage count by
the dense field work and the direct integration work gives
\(CL\beta^{400L}n^2m(1+m/\gamma)^4Z^8\). Here
\(n\ge m\ge d\) follows already from the positive empirical training
feature Gram. The additional source evaluations cost
\(CQ[L n^2(K_{\rm solver}+p)+pdn]\); their direct cosine summation
costs \(CLnpQ^2\). Substituting the bounds for \(Q\) and \(K_{\rm solver}\)
places these terms, together with (15), below

\[
W_{\rm init}\le CL\beta^{400L}
\left\{n^2[m(1+m/\gamma)^4+p]+np^3\right\}Z^8.
\tag{26}
\]

The source-basis selection contribution is \(CLnR^3\), with
\(R\le3077\beta^{36L}p\ell^{5/2}\), so its powers are
\(\beta^{108L}p^3\ell^{15/2}\) and fit (26). Dense mixer formation is
linear in \(p\). This explicitly checks the full-label assembly's work
bound without using the optional fast-transform improvement.

Current-patch arrays use \(CLn^2K_{\rm solver}\) coordinates. Accumulated
source columns and their bases use \(CLnpQ\); reduced matrices and
selection workspace fit \(CLR^2\). These terms, with the dense matrices
and all supplied inputs, give

\[
M_{\rm init}\le CL\beta^{100L}
\left\{n^2(1+m/\gamma)Z^2+npZ^3+p^2Z^5\right\}
 +Cp(d+1).
\tag{27}
\]

Thus the new producer closes the exact-real arithmetic initialization
bound on the inherited good event, while preserving the original source
rank and label allowance. It does not quantify that event's stochastic
success width, numerical training step count, or finite-bit implementation.
The runtime table in the assembly was also checked: its constants follow
from \(64\cdot30000^2<2^{36}\), \(4\cdot30000^2<2^{32}\),
\(2\cdot30000<2^{16}\), and \(30000<2^{15}\), with the unchanged full-label
factors \(\beta^{72L}\) and \(\beta^{36L}\).
