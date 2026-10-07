# Exact weighted compression of a finite causal training program

2026-10-06. Scoped continuation in the unseen-query decoder study.
Internal finite-program theorem; no experiments and no promotion.

A finite nonlinear training program with finitely many initialized-matrix
actions can be compressed exactly after its source fields are known.
Weighted selection preserves all source Grams. An isometric compression
of each initialized mixer then reproduces every listed forward **and**
transpose action with no increase in its operator norm. The compact model
reexecutes the same finite causal instructions from small stored matrices
and selected initial/probe rows. It need not store the future vector
trajectory or consult a dense matrix online.

This is an exact source-dependent preprocessing theorem. It is not a
theorem that preprocessing can avoid examining the original finite
training computation. It is also not a late-query theorem: no field of
an unknown query is included in the selection constraints. The remaining
late-query law issue is stated separately at the end.

## Scope and provenance

The supervisor explicitly proposed the weighted-selection mechanism and
assigned this complete proof within the current study. This file uses
the same scientific and process scope as the immediately preceding
`EXACT_TRANSCRIPT_UNIFORM_LAW.md`, which it does not modify. The earlier
`GROWING_PROGRAM_STABILITY.md` and `HESSIAN_RESPONSE_CLOSURE.md` remain
frozen. The custom notation skill remains inaccessible; the already read
maintained notation contract and supplied instructions are applied.

All linear algebra and convex selection arguments needed here are proved
below. No finite-panel theorem from a different study is imported. In
particular, the supervisor's developing finite-call approximation of
physical training is not assumed already proved by this note.

## 1. The admissible finite instruction graph

For each layer index \(\ell\), let

\[
 H_\ell=\mathbb R^n,
 \qquad \langle x,y\rangle_\ell=x^Ty/n.                       \tag{1}
\]

The common width is inessential; unequal finite widths can be treated
with their corresponding normalized inner products. Between adjacent
spaces there is a fixed initialized map

\[
 W_\ell:H_{\ell-1}\longrightarrow H_\ell,
\]

whose adjoint is its ordinary transpose in (1). These maps may be random,
but the theorem in this file is deterministic after their realization.

Consider a finite, acyclic instruction graph with the following allowed
operations.

1. Prescribed initial vector fields in a layer, and prescribed auxiliary
   probe fields. The latter include any independent completion probes
   used in an exact Gaussian transcript.
2. Coordinatewise scalar functions of earlier vector fields and earlier
   scalar nodes; coordinatewise sums and products are included.
3. Initialized actions \(W_\ell q\) and \(W_\ell^Tc\).
4. Weighted scalar inner products of earlier vector fields, and scalar
   arithmetic or prescribed scalar functions of earlier scalar nodes.
5. Rank-one learned actions
   \(a\langle b,q\rangle\) and their adjoints, and finite sums of
   these actions with earlier scalar coefficients.

Every nonlinear vector argument and output occurring in the realized
graph is included among its named fields. A scalar empirical average
of a coordinate function is represented by first naming that coordinate
field and then pairing it with the constant field \(1\). Include \(1\)
in each layer that uses averages. More general scalar reductions are
covered only if they have such a specified finite representation.

Let \(s_\ell\) be the number of named fields at layer \(\ell\),
and let \(S\) be the total finite graph size. Write these realized fields
as

\[
 v_{\ell,1},\ldots,v_{\ell,s_\ell}\in H_\ell,
 \qquad E_\ell=\operatorname{span}\{v_{\ell,a}:1\le a\le s_\ell\}.
                                                               \tag{2}
\]

The graph can be an unrolled finite numerical training procedure. It
does not have to be a straight sequence of gradient steps. Picard
iterations, temporal interpolation, and Frobenius-radius projections
of learned finite-rank displacements fit the graph once written using
the stated operations. This last assertion is verified in Section 5.

## 2. A weighted selection preserving every field Gram

Fix one layer and omit its index. At coordinate \(i\), form the vector
of pair products

\[
 m_i=(v_{a,i}v_{b,i})_{1\le a\le b\le s}
           \in\mathbb R^{s(s+1)/2}.                           \tag{3}
\]

There exist selected indices \(i_1,\ldots,i_q\) and positive weights
\(p_1,\ldots,p_q\) such that

\[
 q\le 1+\frac{s(s+1)}2,\qquad
 \sum_{j=1}^q p_j=1,\qquad
 \sum_{j=1}^q p_jm_{i_j}=\frac1n\sum_{i=1}^n m_i.              \tag{4}
\]

Here is an elementary proof. Start with weights \(1/n\). If more than
\(N+1\) weights are positive, where \(N=s(s+1)/2\), the vectors
\((1,m_i)\in\mathbb R^{N+1}\) in that support are linearly dependent.
Choose a nonzero dependence \(\lambda_i\). Its coefficients sum to
zero and therefore have both signs. Subtract
\(t\lambda_i\) from the current weights, taking the smallest
positive \(t\) that makes one weight with \(\lambda_i>0\) zero.
All weights stay nonnegative; their sum and moment vector are unchanged.
The support strictly decreases. Finite repetition proves (4), after
discarding zero weights.

Define the compact layer space

\[
 H^c=\mathbb R^q,
 \qquad \langle x,y\rangle_c=\sum_{j=1}^qp_jx_jy_j,            \tag{5}
\]

and the selection map \(J:E\to H^c\) by

\[
 (Jv)_j=v_{i_j}.                                               \tag{6}
\]

Equation (4) gives, for every pair of named fields, equality of their
original and selected inner products. By bilinearity it follows that

\[
 \langle Jv,Jw\rangle_c=\langle v,w\rangle
 \quad\text{for all }v,w\in E.                               \tag{7}
\]

Thus \(J\) is an isometry on the entire field span, including every
linear dependency. In particular, no Gram inverse and no lower
eigenvalue bound are used. The adjoint \(J^*:H^c\to E\) satisfies

\[
 J^*J=I_E,
 \qquad JJ^*=P_{J(E)},
 \qquad \|J\|=\|J^*\|=1                                     \tag{8}
\]

when \(E\ne\{0\}\); the zero case is interpreted in the obvious way.

Apply this construction separately to every layer. The selected
indices and weights may differ between layers. Only the small
spaces, their weights, and selected initial/probe values need to be
retained; the original index labels are not needed for subsequent
evaluation.

## 3. One compact operator handles both orientations

Let \(P_\ell:H_\ell\to E_\ell\) be the orthogonal projection in
the normalized inner product. Define

\[
 W_\ell^c
   =J_\ell P_\ell W_\ell P_{\ell-1}J_{\ell-1}^*:
           H_{\ell-1}^c\longrightarrow H_\ell^c.              \tag{9}
\]

The middle \(P_{\ell-1}\) is redundant because the range of
\(J_{\ell-1}^*\) is already \(E_{\ell-1}\), but makes the
symmetry visible. Every factor other than \(W_\ell\) is an isometry
or orthogonal projection, so

\[
 \|W_\ell^c\|_{c\to c}\le\|W_\ell\|_{H\to H}.                \tag{10}
\]

For every listed forward pair \(q\in E_{\ell-1}\),
\(y=W_\ell q\in E_\ell\), equation (8) gives

\[
 W_\ell^cJ_{\ell-1}q
  =J_\ell P_\ell W_\ell q=J_\ell y.                          \tag{11}
\]

Taking the weighted adjoint of (9) gives

\[
 (W_\ell^c)^*
   =J_{\ell-1}P_{\ell-1}W_\ell^TP_\ell J_\ell^*.
\]

Hence every listed reverse pair \(c\in E_\ell\),
\(d=W_\ell^Tc\in E_{\ell-1}\), satisfies

\[
 (W_\ell^c)^*J_\ell c=J_{\ell-1}d.                           \tag{12}
\]

This simultaneously proves forward consistency, reverse consistency,
kernel compatibility, and an operator-norm bound. Constructing
independent interpolants for the two orientations would not suffice.

In raw selected coordinates, if \(P_\ell^c\) denotes the diagonal
matrix of positive selection weights, the adjoint is

\[
 (W_\ell^c)^*=(P_{\ell-1}^c)^{-1}
                  (W_\ell^c)^T P_\ell^c.                    \tag{13}
\]

It is generally not the unweighted matrix transpose. Omitting these
weights breaks (12). Equivalently, use ordinary Euclidean compact
coordinates \(\widehat x=(P_\ell^c)^{1/2}x\) and store

\[
 \widehat W_\ell=(P_\ell^c)^{1/2}
                     W_\ell^c(P_{\ell-1}^c)^{-1/2}.          \tag{14}
\]

Then \(\|\widehat W_\ell\|_{\rm op}\le\|W_\ell\|_{\rm op}\)
and the reverse map is \(\widehat W_\ell^T\). The coordinatewise
activation becomes

\[
 \widehat\phi_{p_j}(x)=\sqrt{p_j}\,
                             \phi(x/\sqrt{p_j}).              \tag{15}
\]

If \(\phi\) has bounded first derivative, this scaled activation
has the same first-derivative bound, for every positive \(p_j\).
No bound on higher derivatives uniform in tiny weights follows.

## 4. Exact reexecution theorem

Initialize the compact graph with the selected values of all prescribed
initial and auxiliary probe fields. Replace every initialized matrix
by (9), every transpose call by its weighted adjoint (13), and every
normalized scalar inner product by (5). Use exactly the same prescribed
scalar functions and coordinatewise instructions.

**Theorem.** Every scalar node of this compact computation equals the
corresponding original scalar node exactly. Every vector node at layer
\(\ell\) equals the selected original vector under \(J_\ell\).

**Proof.** Induct on the acyclic instruction order. The claim holds at
initial and probe fields by construction. For a coordinatewise map

\[
 v_i=\Phi(u_{1,i},\ldots,u_{k,i};c_1,\ldots,c_a),
\]

selection commutes with the operation at each selected index, and the
scalar inputs agree by induction. Thus the new selected field agrees.
For a scalar inner product use (7). Scalar arithmetic therefore agrees
as well. Matrix calls agree by (11) and (12). Finally a rank-one learned
action is a vector multiplied by a scalar inner product, both already
covered. This proves every node. \(\square\)

The matrices (9) may depend on the full realized finite training
computation. After preprocessing, however, they are fixed small
matrices. At runtime they do not consult that computation: all
nonlinear fields, scalar coefficients, conditional means, and retained
innovation norms are obtained again by the same causal instructions.

### 4.1 Exact acquisition of Gaussian-transcript coefficients

Apply the theorem to the finite program enlarged by the completion
operations from `EXACT_TRANSCRIPT_UNIFORM_LAW.md`. In a forward call,
the original full Gaussian innovation is

\[
 g=(Wq-\text{conditional mean})/\tau+P_U\zeta,
                                                               \tag{16}
\]

where \(\zeta\) is an auxiliary independent Gaussian probe and
\(P_U\zeta=U(U^TU/n)^\dagger U^T\zeta/n\). This expression uses
only an initialized action, scalar Grams, scalar matrix arithmetic,
and linear combinations of earlier vectors. Include its input,
output, and probe fields among the named fields. The same applies to
reverse completion.

The compact graph then reproduces the exact innovation field at its
selected rows and reproduces **every scalar transcript coefficient**.
The compact probes are not asserted iid after data-dependent selection;
that assertion is unnecessary. The iid row law is proved for the
original completed transcript. Exact equality transfers its realized
scalar coefficients to the compact reexecution.

This discharges finite-program *coefficient acquisition* under
source-dependent preprocessing. It does not use population moments in
place of empirical ones and therefore incurs no Gram-conditioning
amplification of a statistical approximation error. Exact singular
dependencies are harmless; a numerically stable approximate
implementation may use the separate cutoff and precision analysis in
`EXACT_TRANSCRIPT_UNIFORM_LAW.md`.

## 5. Learned rank sums and their Frobenius projections

The hidden-layer gradient updates in the original normalized network
have the form

\[
 \Delta W=\sum_{a=1}^k\theta_a\,
                  x_a y_a^T/n
          =\sum_{a=1}^k\theta_a\,
                  x_a\langle y_a,\cdot\rangle.               \tag{17}
\]

Their compact realization is the same weighted rank sum with selected
fields. Every application of this displacement and its adjoint is
covered by Section 4. Its ordinary Frobenius norm in the original
coordinates equals its Hilbert--Schmidt operator norm under the equal
normalized metrics, and

\[
 \|\Delta W\|_F^2
  =\sum_{a,b}\theta_a\theta_b
       \langle x_a,x_b\rangle
       \langle y_a,y_b\rangle.                               \tag{18}
\]

All these scalar products are preserved. Therefore the weighted
Hilbert--Schmidt norm of the compact rank sum equals (18), even if
its matrix dimensions are much smaller. The radial projection

\[
 \Delta W\longmapsto
 \min\{1,B/\|\Delta W\|_F\}\Delta W                           \tag{19}
\]

onto a fixed Frobenius ball is exactly reproducible using a scalar
multiplier. The zero case uses multiplier one. This argument applies
to the learned displacement, not to an arbitrary full initialized
matrix: the latter's full Frobenius norm is not preserved by (9).

Likewise, norms of learned input-layer and readout displacements are
inner products of their named fields, with the original normalizing
factors retained. Finite interpolation combinations and explicit
Picard iterations are combinations of the allowed instructions.
Hence such a finite training approximation may use these norm
projections without introducing a prohibited full-matrix spectral
operation.

## 6. Retained memory, transient workspace, and small weights

Let \(s=\max_\ell s_\ell\), with a fixed number of layers. Then

\[
 q_\ell\le1+s(s+1)/2=O(s^2).                                 \tag{20}
\]

Storing all compact initialized matrices costs \(O(s^4)\) scalars.
Storing at most \(S\) prescribed initial/probe fields costs
\(O(Ss^2)\) scalars. Weights cost \(O(s^2)\); the instruction
description and scalar transcript cost their actual finite sizes.
For \(S,s=\operatorname{polylog}(n)\), this is an absolute
polylogarithmic count. No \(n\)-dimensional source field is retained.

A simple execution retaining all current compact graph nodes uses
\(O(Ss^2)\) live scalars. If retaining a full compact node history is
undesired, recursive recomputation of earlier nodes uses the fixed
matrices, probe marks, instruction graph, and a depth-\(S\) scalar
evaluation stack. A vector matrix action at one coordinate is a
finite sum over compact source coordinates; a scalar inner product is
another such sum. Depth-first evaluation stores loop indices and
partial scalar sums, and recomputes previous coordinate values instead
of keeping a vector history. Its stack is \(O(S)\), besides retained
parameters and any separately chosen scalar transcript state. Runtime
can be very large. No bound on runtime is claimed here.

These are finite arithmetic counts, not a license to encode a dense
array in the digits of one parameter. The construction uses ordinary
small linear maps and prescribed coordinate functions only. Nonetheless
the positive weights in (4) can be arbitrarily small. Exact arithmetic
alone gives no lower bound on their bit complexity. Formula (15) also
shows why uniform higher-derivative or finite-precision estimates
cannot be inferred solely from (10).

There is a separate elementary approximation route if explicit
precision control is needed. Suppose all original named coordinates
obey \(|v_{\ell,a,i}|\le H\). Delete selected coordinates whose
weights are below \(\eta\), and in Euclidean compact coordinates
compress (14) further by the associated coordinate projections. At
every named field the deleted Euclidean component has norm at most

\[
 H\sqrt{q_\ell\eta}.                                         \tag{21}
\]

The projected initialized maps retain their operator-norm bounds.
Keep the surviving weights without renormalizing them; their sum can
be less than one. Evaluate scalar products with those weights and
keep the original scalar normalizations. If the finite instruction
graph, with physical-coordinate caps at least \(H\), has a proved
local perturbation amplification \(A_{\rm prog}\), comparing its
original compact execution with this projected execution gives error
at most

\[
 C S A_{\rm prog}H\sqrt{q\eta},\qquad q=\max_\ell q_\ell,      \tag{22}
\]

in the corresponding named-field and scalar norms, with the ordinary
product-rule factors included in \(A_{\rm prog}\). This follows by
induction: each deleted input has the bound (21), each initialized
action is bounded by (10), and the local operation bounds propagate
their sum through the graph. For arbitrary allowed scalar functions,
the existence and size of \(A_{\rm prog}\) must be verified; it is
not an automatic conclusion of the exact theorem.

If \(\log H+\log A_{\rm prog}+S=\operatorname{polylog}(n)\),
taking \(\eta=\exp[-\log(n)^C]\) with sufficiently large fixed
\(C\) makes (22) smaller than any requested
\(\exp[-\operatorname{polylog}(n)]\) accuracy of lower exponent.
All retained weights then satisfy \(p_j\ge\eta\), so their
reciprocals have polylogarithmic logarithmic size. Finite arithmetic
rounding still needs a corresponding operation-level error analysis.
No uniform precision claim for the exact selected weights is made.

## 7. Relation to autonomy and the unseen query

This construction permits **source-dependent preprocessing**: run or
otherwise determine the original finite training graph, form its
moment constraints, choose the weighted rows, and form (9). The
preprocessing may use dense workspace. The theorem concerns the
retained compressed object and its subsequent live execution. If a
different contract also restricts preprocessing workspace or forbids
access to the completed finite training graph during preprocessing,
this theorem does not satisfy that stronger contract.

After preprocessing, the compact object contains no table of future
vector fields or future scalar coefficients. It stores small fixed
initialized maps and prescribed initial/probe rows. It recomputes
all nonlinear intermediate values by the original finite causal
instructions. In this discrete sense the coefficient acquisition is
autonomous. Converting a finite time-discretized instruction graph
into an autonomous all-physical-time model, including the fitted
endpoint, remains an additional step unless supplied by the chosen
finite-program construction.

The selection constraints contain training fields and transcript
completion probes only. They do not contain a late query. Therefore
directly running the small selected network on a new input is not
proved accurate. The intended use is narrower: autonomously acquire
the actual training-transcript scalar coefficients, then use the
row-law representation and a separately justified passive-query
decoder. The latter still must determine its new empirical
cross-moments, or prove that replacing them by computable moments is
stable in the final scalar output without a smallest-Gram-eigenvalue
loss. The exact acquisition theorem does not resolve that law step.

Thus there are three distinct statements:

1. A finite causal training transcript can be represented by iid row
   packets plus realized scalar coefficients.
2. Under source-dependent preprocessing, a compact weighted nonlinear
   program can acquire those coefficients exactly by reexecution.
3. Those coefficients support a uniformly accurate unseen-query
   decoder with counted workspace.

The first is proved in `EXACT_TRANSCRIPT_UNIFORM_LAW.md`; the second
is proved here. The third is not asserted. This separation prevents
the new finite-program compression theorem from being mistaken for
the complete nonlinear unseen-query theorem.
