# Exact implicit execution of the Harmonic setup

2026-10-06. Scoped author candidate. This note proves the finite execution and
its operation counts, conditional on the exact adaptive Gaussian action sampler
specified below and on the already checked Taylor/backend/assembly interface.
It is not a new proof of the probabilistic source event, an implementation, an
independent review, or a promotion.

The present authorization permits a fresh independent Gaussian dense reference
to be represented by its queried actions. It does not require returning its
individual matrix entries. The output remains the original finite Harmonic
construction, with its original activations and original time-zero
initialization. The disposable continuation uses the checked polynomial
activation backend.

## 1. Inputs, notation, and precise sampler dependency

Let \(L\ge2\) and \(m,d,n\ge1\) be hidden depth, sample count, input dimension
and hidden width, with \(n\ge\max(m,d)\). Training inputs are

\[
v_a=x_a/\sqrt d\in S^{d-1},\qquad 1\le a\le m.
\]

The first matrix \(W^{(1)}\in\mathbb R^{n\times d}\) has independent
standard normal entries. For \(2\le j\le L\), the initialized hidden matrix

\[
W_0^{(j)}\in\mathbb R^{n\times n},\qquad
(W_0^{(j)})_{uv}\sim N(0,1/n)
\tag{1}
\]

has independent entries, independently across layers and of \(W_0^{(1)}\).
The stored readout \(w=W^{(L+1)}\in\mathbb R^n\) is initially zero.
This zero-readout convention is the one in the present study's `RESULT.md`.
The ordinary forward and backward coordinates are

\[
z^{(1)}=W^{(1)}v,\quad
z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^Th^{(L)}/n,
\]
\[
\delta^{(L)}=w\odot\phi_L'(z^{(L)}),\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot W^{(j+1)T}\delta^{(j+1)}.
\tag{2}
\]

Residuals are \(r_a=f_n(v_a)-y_a\). The loss is

\[
\mathcal L_n=m^{-1}\sum_a r_a^2.
\]

The prescribed mobilities give the rank-one equations

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
\quad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)T},
\quad
\dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{3}
\]

The setup replaces each \(\phi_j\) in (2)--(3) by its computed degree-
\(D\ge1\) polynomial \(\psi_j\), but does not replace the exact initial
source additions or the final runtime activations.

Supply a finite panel partition

\[
0=\tau_0<\tau_1<\cdots<\tau_J=T,\qquad
\Delta_b=\tau_{b+1}-\tau_b,
\]

with \(J\ge1\), a common Taylor degree \(K\ge1\), temporal degree
\(p\ge0\), largest spherical degree \(\ell_*\), a finite retained mode set
\(\Lambda\), and its cardinality \(N=|\Lambda|\). For \(d\ge2\), set

\[
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},\qquad
H_{\rm sph}=\sum_{\ell=0}^{\ell_*}h_\ell,
\quad R=2m+d+1+4N.
\tag{4}
\]

Impossible binomials are zero. The original weighted simplex is one allowed
\(\Lambda\); its actual supplied cutoffs, rather than a rectangular enlargement,
are used in every retained coefficient. There are \(N_t\ge1\) temporal nodes
and \(N_x\ge1\) spatial nodes. For the positive angular rule of the quadrature
note, \(N_x=N_\varphi N_\theta^{d-2}\) when \(d\ge3\), and
\(N_x=N_\varphi\) when \(d=2\).

For \(d=1\), use two point families, \(N_x=H_{\rm sph}=2\),
\(N=2(p+1)=2N_1\), and the same formula \(R=2m+d+1+4N\).
This is exactly \(2m+d+1+8N_1\); there is no angular quadrature.

Let \(r_j=\dim E_j\) be the actual source-space ranks after coefficient
construction, and let \(q_j\) be the actual selected support sizes. Put

\[
r=\max_jr_j\le\min(n,R),\qquad q=\max_jq_j.
\tag{5}
\]

The deterministic selector gives \(r_j\le q_j\le9r_j\), hence
\(r\le q\le9r\). A supplied budget \(Q\) is sufficient when
\(9r\le Q\); the original safe count uses \(9R\le Q<n\).
Unused budget is not padded with extra coordinates. All occurrences of
\(q\) in the costs below mean the actual retained maximum, not unused capacity.
The constant source ensures \(r_j\ge1\).

**Sampler contract.** For each matrix (1), a stateful procedure accepts a finite
adaptive sequence of requests \(W_0^{(j)}x\) and \(W_0^{(j)T}y\), with
\(x,y\in\mathbb R^n\). Queries may depend on all previous responses, the
data, and the other layers' transcripts. Its joint responses admit a coupling
with mutually independent matrices (1), under which every response is the
corresponding exact action. The action procedure must handle both directions
of one matrix consistently, including dependent and zero queries. For at most
\(k\) vector requests at a layer, assume numerical upper bounds

\[
O(nk^2)\ \text{arithmetic},\qquad O(nk)\ \text{words},\qquad
\text{at most }nk\ \text{independent standard normal draws}.
\tag{6}
\]

It suffices to draw at most \(n\) normals for each newly exposed independent
direction and none for dependent requests. Square roots used by normalization
are accounted for separately below. The coupling must apply to globally
interleaved adaptive requests, not just predetermined query vectors. This
sampler result is a separate proof dependency; it is not derived in this note.

All arithmetic is exact real arithmetic, with exact zero/rank comparisons and
the explicitly counted scalar primitives. Gaussian variates are ideal real
normal samples. Activation evaluation costs and Gaussian-generation costs are
not inferred from analyticity or hidden in arithmetic big-O constants.

## 2. Exact low-rank anchors and current-panel coefficients

At panel \(b\), use normalized Taylor coefficients in the unscaled local
variable \(t-\tau_b\). Write

\[
U_i^{(j)}=
\bigl([r_a\delta_a^{(j)}]_i\bigr)_{a=1}^m\in\mathbb R^{n\times m},
\qquad
H_k^{(j-1)}=
\bigl([h_a^{(j-1)}]_k\bigr)_{a=1}^m\in\mathbb R^{n\times m}.
\]

Here the residuals and fields use the polynomial activations. Comparing
coefficients in (3), for \(1\le s\le K\), gives

\[
[W^{(j)}]_s=-\frac2{mns}
\sum_{i+k=s-1}U_i^{(j)}H_k^{(j-1)T}.
\tag{7}
\]

The degree-zero term is the current anchor \(W_b^{(j)}\). Its endpoint update
is exactly

\[
W_{b+1}^{(j)}-W_b^{(j)}
=-\frac2{mn}\sum_{i=0}^{K-1}U_i^{(j)}V_i^{(j-1)T},\qquad
V_i^{(j-1)}=\sum_{k=0}^{K-1-i}
\frac{\Delta_b^{i+k+1}}{i+k+1}H_k^{(j-1)}.
\tag{8}
\]

For each panel append the \(mK\) columns of the \(U_i^{(j)}\), with the
factor \(-2/(mn)\), to a factor \(A_b^{(j)}\), and the corresponding
\(V_i^{(j-1)}\) columns to \(B_b^{(j)}\). These factor symbols are not
the first weight matrix. They have shapes \(n\times bmK\), and

\[
W_b^{(j)}=W_0^{(j)}+A_b^{(j)}B_b^{(j)T},\qquad
\operatorname{rank}(W_b^{(j)}-W_0^{(j)})\le bmK.
\tag{9}
\]

No independence, smallness, or low-rank property of the initialized matrix is
used in (9). The rank bound holds for the finite numerical anchor increment
because its endpoint is the specified degree-\(K\) polynomial. It is not a
rank bound for an exact continuous trained increment.

For a current-panel query series \(X(t)=\sum_{c=0}^KX_c(t-\tau_b)^c\),
each coefficient of the constant-anchor action is computed as

\[
W_b^{(j)}X_c
=\operatorname{Action}_j(X_c)+A_b^{(j)}(B_b^{(j)T}X_c).
\tag{10}
\]

The transpose uses

\[
W_b^{(j)T}X_c
=\operatorname{TransposeAction}_j(X_c)
 +B_b^{(j)}(A_b^{(j)T}X_c).
\tag{11}
\]

The higher-parameter-jet contribution to the coefficient of order \(s\ge1\)
is still the finite sum

\[
-\frac2{mn}\sum_{i+k+c=s-1}
\frac{U_i^{(j)}(H_k^{(j-1)T}X_c)}{i+k+1}.
\tag{12}
\]

The cached-contraction implementation in the assembly note computes (12)
exactly. All its factors at order \(s\) have lower orders than \(s\), so
it remains causal during training-jet generation. Equations (10)--(12) give
precisely the same local coefficient as multiplication by a materialized
anchor and materialized parameter jets. Polynomial Chebyshev composition is
also a finite exact recurrence. Induction over coefficient order, then over
layers in the forward/backward passes, identifies every computed training and
passive coefficient with its counterpart in the explicit algorithm.

The first matrix is stored explicitly in \(nd\) words. It does not require
\(ndK\) persistent coefficient words. With
\(V=(v_a)_{a=1}^m\in\mathbb R^{d\times m}\), its higher coefficients act by

\[
[W^{(1)}]_sx=-\frac2{ms}U_{s-1}^{(1)}(V^Tx).
\tag{13}
\]

Precompute \(V^TV\) for training and compute \(V^Tx\) for each streamed
passive query. To advance its anchor first sum
\(\sum_{i<K}\Delta_b^{i+1}U_i^{(1)}/(i+1)\), then multiply by
\(-2V^T/m\). Readout coefficients and endpoint updates are ordinary vectors
obtained from \(\dot w=-2\sum_a r_ah_a^{(L)}/m\). Both calculations are
exact rearrangements of the same finite sums.

## 3. Exhaustive matrix-access inventory and output coupling

Fix generator ordering, Gram--Schmidt sign conventions, deterministic selector
tie-breaking, and all scalar quadrature/backend formulas. These choices select
one concrete version of the explicit finite construction. Its only accesses
to a hidden initialized matrix are the following.

1. **Exact original initialization.** Compute all training features at time
   zero with the original \(\phi_j\), saving the forward images
   \(W_0^{(j)}h_0^{(j-1)}(v_a)\). This uses \(m\) forward actions at each
   hidden mixer. The backward fields are zero because \(w_0=0\); no original
   derivative calls are required. Insert these exact feature/image vectors,
   the first-weight columns at layer one, and the constant vector into the
   source spaces. The degree-zero \(\psi_j\) features cannot replace them.
2. **Every panel's forward/backward coefficients.** For each coefficient
   through \(K\), the training batch uses at most \(m\) forward and \(m\)
   transpose actions per mixer through (10)--(11). Each passive query uses at
   most one of each. All current-anchor corrections and nonconstant parameter
   coefficients use retained factors and finite contractions, not new matrix
   entries. Panels with no assigned time nodes can omit passive queries, but
   the bound below permits all \(N_x\) queries on all \(J\) panels.
3. **Initialized images of completed global coefficients.** Accumulate only
   the base coefficient vectors for \(h^{(j)}\) and \(\delta^{(j)}\).
   For each retained mode form
   \(W_0^{(j)}\widetilde c^{\,h^{(j-1)}}\) and
   \(W_0^{(j)T}\widetilde c^{\,\delta^{(j)}}\).
   This uses at most \(N\) forward and \(N\) transpose actions per mixer.
   It is exact because all preceding projection operations are scalar finite
   sums shared by each source/image pair.
4. **Final basis-to-basis mixer.** Having constructed bases
   \(U_j\in\mathbb R^{n\times r_j}\), with \(U_j^TU_j/n=I\), request
   \(W_0^{(j)}U_{j-1}\) column by column. This uses at most
   \(r_{j-1}\le r\) further forward actions. Paired source-image information
   is not assumed to cover these basis columns. Form
   \(U_j^TW_0^{(j)}U_{j-1}/n\) from these returned vectors.

Consequently a sufficient number of vector requests per hidden mixer is

\[
k_* = m+2J(m+N_x)(K+1)+2N+r.
\tag{14}
\]

The random realized rank in this pathwise cost bound is not a deterministic
stopping budget. To invoke the sampler theorem, use the deterministic bound
\(m+2J(m+N_x)(K+1)+2N+\min(n,R)\) at each layer, since
\(r\le\min(n,R)\). Its online operation count may still be evaluated at
the smaller actual request count and bounded by (14).

This counts requests even when their vectors vanish, repeat, or lie in a
previously queried span. The adaptive sampler can save work in those cases;
the sufficient envelope does not require such savings. Scalar data geometry,
orthogonalization, selection, and metric formation do not access \(W_0\)
except through the four listed uses. In particular there is no request for its
entries, Frobenius norm, singular values, or full operator norm.

To prove coupling of the full outputs, take a joint realization supplied by
the sampler contract. Materialize its completed matrices only in the proof and
run the explicit finite algorithm with those matrices. The original initialized
features agree by induction over layers. Assume current anchors, stored jets,
and accumulated global coefficients agree before one computation step. If the
step requests a matrix action, (6), (10), and (11) give the exact explicit
answer. If it performs a scalar operation, polynomial composition, contraction,
or endpoint update, the operands and the operation are the same exact real
quantities, with (8), (12), and (13) justifying any change in grouping. Thus the
next state agrees. Finite induction over all panels proves equality of the
completed base coefficients, then the image coefficients in item 3.

The source generators and their order therefore agree. Exact orthogonalization
returns the same ranks and bases. The selector sees the same row vectors and
barrier comparisons, so the prescribed tie-breaking gives the same selected
indices and weights. Item 4 then gives the same final compressed mixers. The
metric formula and first-weight restriction also agree. In detail, with
\(P_j=(U_j)_{I_j}\), the initialized output is exactly

\[
W_C^{(1)}(0)=(W_0^{(1)})_{I_1},\quad w_C(0)=0,\quad c_C(0)=y,
\]
\[
B_C^{(j)}(0)
=P_j\frac{U_j^TW_0^{(j)}U_{j-1}}nP_{j-1}^TM_{j-1}.
\tag{15}
\]

Any deterministic scalar failure branch in the explicit execution is reproduced
as well. The algebraic statement holds for all finite supplied orders; source
accuracy additionally requires the checked degree, panel, and quadrature
certificates. This argument is equality under a coupling, not merely equality
of marginal output laws. It preserves the original all-time comparison event
and its probability without an additional failure budget.

The fresh-reference contract matters. This proof does not reproduce a previously
materialized matrix, or a previously specified entrywise pseudorandom stream,
without paying that reference's access costs. It supplies a fresh reference with
the prescribed independent Gaussian law.

## 4. Scalar certificates and what is not tested

The finite construction takes admissible numeric structural certificates as
inputs: a positive population gap \(\gamma\), activation strip/derivative
bounds, and the fitting/source constants required by the checked continuation.
Non-elementary population moments used in the exact label allowance are also
supplied if that allowance is to be evaluated exactly. An arbitrary analytic
activation does not provide an algorithm for its Gaussian moment integrals.
Obtaining such external certificates is not charged as free arithmetic here.

Given those quantities, the source constants (S.5)--(S.10), (S.22)--(S.25),
the fitting/comparison recurrences, the restart constants, and the backend
formulas are finite scalar recurrences. Their layer-indexed arrays have length
\(O(L)\); integer powers/factorials for the dimension use \(O(d)\)
multiplications. The label RMS costs \(O(m)\) arithmetic and one square root.
Thus their scalar preparation and deterministic gate comparisons cost
\(O(L+d+m+1)\) arithmetic, elementary calls, and words as a safe common bound.
Angular basis and mode enumeration costs are separately charged below.

The explicit width, radius, count, and analytic-extension gates are comparisons
of these scalars and \(n\). Their evaluation never tests a sampled hidden
matrix's norm. Likewise the local Taylor construction selects its panels and
degree from the explicit bounds; it does not form an \(n^2\)-coordinate defect
vector, solve an implicit equation, test membership in a complex parameter
ball, or reject and recompute panels. Those norms and domains occur in the
proof of its deterministic error bound. The underlying source probability event
is an inherited theorem hypothesis, not a computable acceptance test, and its
width threshold remains partly unquantified. There is no rejection sampling
conditioned on that event.

If desired, the exact initial top feature Gram can be formed and factored in
\(O(nm^2+m^3)\) arithmetic and \(O(m^2)\) additional words. This is also
a sufficient charge for preparing the final initial readout solve cache: exact
source isometry makes the selected initial Gram the same Gram. It does not
require querying any further initialized-matrix directions. The formulas below
include this charge, even if a particular output omits that cache.

## 5. Complete supplied-order arithmetic and peak storage

All big-O constants in this section are numerical and implementation-dependent
only. They hide no dependence on \(L,m,d,n,J,K,D,p,\ell_*,N_t,N_x,N,R,r,q\),
structural certificate values, confidence, activation cost, Gaussian cost, or
precision. A bound is an operation count for this specified execution; it is
not an optimality statement. Write \(k_*\) only for the explicit expression
(14).

First account for the two terms introduced by implicit execution. The Gaussian
action work is

\[
O((L-1)n k_*^2),\qquad O((L-1)n k_*)\ \text{words}.
\tag{16}
\]

At panel \(b\), each forward/transposed application of the accumulated
increment has cost \(O(nbmK)\) per vector. There are at most
\(2(m+N_x)(K+1)\) such vectors per mixer. Since
\(\sum_{b=0}^{J-1}b=J(J-1)/2\), their total work is

\[
O((L-1)n m(m+N_x)J(J-1)K(K+1)).
\tag{17}
\]

Retaining both rank factors uses \(O((L-1)nJmK)\) words. Forming the
grouped factors (8) costs \(O(J(L-1)nmK^2)\). No dense rank-one
outer-product update is executed.

The first matrix, its actions (13), and data pairings cost, sufficiently,

\[
O\bigl(nd(1+m)+m^2d
 +J\{nd(m+N_x)+dmN_x+nm(m+N_x)(K+1)\}\bigr).
\tag{18}
\]

Here \(nd\) creates the first matrix, \(ndm\) evaluates its original
initialized training actions, and \(m^2d\) prepares the training input Gram.
Each panel charges its direct first-matrix actions, passive input inner products,
and all higher first-matrix coefficients. Its endpoint advancement fits the same
bound. Spatial input inner products are recomputed per panel to avoid storing
an \(m\)-by-\(N_x\) table.

The current-panel contractions (12), readout/residual series arithmetic,
backward gate multiplication, and grouped factor formation are bounded by

\[
O\bigl(JL m(m+N_x)(K+1)^2(n+K+1)\bigr).
\tag{19}
\]

For (12), caching all \(H_k^TX_c\) costs \(O(nmb(K+1)^2)\) for
a batch of \(b\) columns; their scalar weighted sums cost
\(O(mb(K+1)^3)\), and the final vector combinations cost
\(O(nmb(K+1)^2)\). Take \(b=m\) for training and \(b=1\) for
each passive query. The first-layer higher-coefficient term in (18) is absorbed
by (19). Its separate display explains where it is paid.

The degree-\(D\) polynomial activation backend costs

\[
O\bigl(L(D+1)^2+JLn(m+N_x)(D+1)(K+1)^2\bigr)
\tag{20}
\]

arithmetic, including coefficient construction and preparation of derivative
polynomials. Online training composition needs
\(O(Lmn(D+1)(K+1))\) words. One offline scalar composition may reuse
\(O((D+1)(K+1))\) scratch. No original derivative calls occur.

Use spatial-first projection. On panel \(b\), with time-node set \(I_b\),
form

\[
\mathcal B_{kc}^{(b)}
=\frac{\gamma_k}{N_t}\sum_{a\in I_b}
\cos(ku_a)((t_a-\tau_b)/\Delta_b)^c,
\quad \gamma_0=1,\quad\gamma_k=2\ (k>0).
\tag{21}
\]

These scalar tables cost \(O((N_t+J)(p+1)(K+1))\) arithmetic and
\(O((p+1)(K+1)+N_t+J)\) words. For every spatial query accumulate the
spherical coefficient of each local source coefficient, then transform only
the retained mode pairs. Here the local source coefficients must first be
converted from the unscaled convention in Section 2 to the affine coordinate
used by (21): for a base field \(g\), define

\[
G_{b,c}^{\,g}(v_s)=\Delta_b^c[g(\tau_b+\cdot,v_s)]_c,
\qquad
\widetilde g_b(t,v_s)=\sum_{c=0}^K G_{b,c}^{\,g}(v_s)
                 ((t-\tau_b)/\Delta_b)^c.
\]

Consequently (21) acts on \(G_{b,c}^{\,g}\), not on the raw Taylor
coefficients. Generate the powers of \(\Delta_b\) once per panel and
rescale before spatial accumulation. This costs
\(O(JLnN_x(K+1))\) arithmetic, absorbed by the following projection bound
because \(H_{\rm sph}\ge1\), and requires no additional vector buffer.
The full projection therefore costs

\[
O\bigl(LnJ(K+1)(N_xH_{\rm sph}+N)\bigr),\qquad
O(Ln(K+1)H_{\rm sph})\ \text{extra words}.
\tag{22}
\]

The completed global coefficient blocks use \(O(LnR)\) words. They are
not multiplied by the number of panels. Exact initialized-image actions have
already been paid in (14)--(16), including their answer vectors. The optional
sorting of time nodes costs \(O(N_t\log(2+N_t))\); a merge of the two
cosine-grid halves can improve it.

For clarity, the following geometry choice recomputes spherical values on each
panel. With the polar/azimuth orders defined after (4), take

\[
G_{\rm time}=
\begin{cases}
N_t+J, & d=1,\\
N_t+N_x+JN_x(\ell_*+1), & d=2,\\
N_\theta^2+dN_\theta+N_t+N_\varphi+d
+d(\ell_*+1)^2
+JdN_x[1+(\ell_*+1)^2+H_{\rm sph}], & d\ge3,
\end{cases}
\tag{23}
\]

\[
G_{\rm memory}=
\begin{cases}
N_t+1, & d=1,\\
N_t+N_x+\ell_*+1, & d=2,\\
dN_\theta+N_t+N_\varphi
+d[1+(\ell_*+1)^2+H_{\rm sph}], & d\ge3.
\end{cases}
\tag{24}
\]

The rule and separated harmonic recurrences have numerical bounds
\(O(G_{\rm time})\), \(O(G_{\rm memory})\). The term
\(JdN_x\) includes repeated spatial coordinate/weight generation; it
is not charged only on the first panel. The normalization constants are
prepared once. The first case merely evaluates the two fixed points.
If a different geometry implementation is chosen, its matched time and memory
bounds must replace both (23) and (24).

Source orthogonalization, the conservative deterministic barrier selector,
small basis contractions, and retained metric/matrix formation cost

\[
O\bigl(LnRr+Lnr^3+(L-1)nr^2
       +L(qr^2+r^3+q^2r)+qd\bigr).
\tag{25}
\]

For orthogonalization, process each of at most \(R\) columns against at
most \(r\) basis columns. At each of \(9r_j\) selector steps, compute
the shifted \(r_j\)-dimensional inverses in \(O(r_j^3)\) and scan all
\(n\) row vectors in \(O(nr_j^2)\). Since \(r_j\le n\), their
sum is \(O(nr_j^3)\). This proves the selector term, with no assumed
fast spectral-selection routine. After item 4 of the inventory, multiplying
the returned basis images by \(U_j^T/n\) costs \(O(nr^2)\) per mixer.

For the metric, with selected rows \(P\), diagonal weights \(\mathsf D\),
and \(G=P^T\mathsf DP\), use

\[
M=\mathsf D+\mathsf DP(G^{-2}-G^{-1})P^T\mathsf D,\qquad
M^{-1}=\mathsf D^{-1}+P(I-G^{-1})P^T,
\quad P^TM=G^{-1}P^T\mathsf D.
\tag{26}
\]

All inverses in (26) are on the \(r_j\)-dimensional positive Gram.
The displayed matrix products give \(O(qr^2+r^3+q^2r)\) work for
each layer and its retained caches; final mixer multiplication has the same
bound. Because \(q\ge r\), this term is at most \(O(Lq^2r)\),
but (25) records its sources explicitly. First-weight restriction costs
\(O(qd)\). No initialized-matrix entry is needed in this stage.

Combining (16)--(25), one complete non-sampling, non-original-activation
arithmetic envelope is

\[
\begin{split}
T_{\rm setup}=O\bigl(&
nd(1+m)+m^2d+nm^2+m^3+L+d+m+1+L(D+1)^2\\
&+(L-1)nk_*^2
 +(L-1)nm(m+N_x)J(J-1)K(K+1)\\
&+J[nd(m+N_x)+dmN_x]
 +JLm(m+N_x)(K+1)^2(n+K+1)\\
&+JLn(m+N_x)(D+1)(K+1)^2\\
&+(N_t+J)(p+1)(K+1)
 +LnJ(K+1)(N_xH_{\rm sph}+N)\\
&+LnRr+Lnr^3+(L-1)nr^2
 +L(qr^2+r^3+q^2r)+qd\\
&+G_{\rm time}+N_t\log(2+N_t)\bigr).
\end{split}
\tag{27}
\]

For peak resident real words, including phase-specific buffers safely by their
sum, the matched sufficient envelope is

\[
\begin{split}
M_{\rm setup}=O\bigl(&
nd+(L-1)n[k_*+JmK]+Lmn(D+1)(K+1)\\
&+Lm^2(K+1)^2+LnR+Ln(K+1)H_{\rm sph}\\
&+Lq^2+q(d+Lm+1)+m^2+m(d+1)\\
&+L(D+1)+(p+1)(K+1)+N_t+J\\
&+G_{\rm memory}+L+d+m+1\bigr).
\end{split}
\tag{28}
\]

The \(qLm\) term permits final training feature/backward caches. They can
also be initialized directly by restriction of exact source features, with
zero backward fields. Copying/zeroing their arrays costs \(O(Lqm)\),
which fits \(LnRr\) because \(q\le9r\), \(m\le R\).
Other final state arrays fit (25); initial readout-Gram construction is already
included in the first line of (27). The \(Lmn(D+1)(K+1)\) term includes
ordinary training jets, and \(Lm^2(K+1)^2\) includes contraction caches.
One passive query's vector jets fit the same envelope because \(m,D\ge1\).
Small basis/selector arrays fit \(LnR\) and \(Lq^2\).

Unlike an explicit dense execution, (27)--(28) contain no mandatory hidden
matrix initialization, anchor materialization, source-image multiplication, or
final basis-image charge proportional to \(n^2\). All four are replaced by
the explicitly charged transcript operations. This is not a uniform promise
of subquadratic work at arbitrary orders: if \(k_*\), \(r\), or \(q\)
are large, the displayed bounds can exceed \(n^2\). A branch returning full
dense matrices necessarily has a quadratic output inventory. The present
claim concerns the analytic selected construction under the fresh implicit
reference contract.

## 6. Primitive calls and supplementary costs

The explicit first matrix requires exactly \(nd\) independent standard
normal draws. By the sampler contract, the remaining draws are bounded by

\[
N_{\rm Gaussian}\le nd+n\sum_{j=2}^Lk_j
                 \le nd+(L-1)nk_*.
\tag{29}
\]

The count can be smaller than this because repeated/dependent directions need
no fresh innovation. There are no Gaussian readout draws and no need to draw
the as-yet unexposed part of any matrix. Sampling that part is only a possible
mathematical completion used to define the coupled reference.

The activation backend uses \(4(D+1)\) real scalar value calls per layer.
Exact original initialized features use \(nm\) value calls per layer.
Thus a sufficient original-activation call count is

\[
N_\phi=4L(D+1)+Lnm.
\tag{30}
\]

Add at most \(L\) calls if values \(\phi_j(0)\) needed to compute a
declared envelope have not been supplied. No high derivative, original
first-derivative, complex-activation, or trained-reference calls occur.
The backend's approximate value calls may use its specified accuracy; the
original initialized features use exact real values in the current model.
The equality proof requires the implicit and explicit executions to use the
same value oracle or the same supplied approximate backend samples.

For a reproducible separation of elementary evaluations from additions,
multiplications, divisions, and comparisons, define the angular table count

\[
A_{\rm elem}=
\begin{cases}
0,&d=1,\\
N_x,&d=2,\\
N_\theta+N_\varphi+d(\ell_*+1)^2,&d\ge3.
\end{cases}
\]

A sufficient total count of square roots, trigonometric and fixed
logarithmic/exponential/inverse-hyperbolic evaluations is

\[
N_{\rm elem}
=O\bigl(L+d+m+1+L(D+1)+N_t+A_{\rm elem}
             +(L-1)k_*+Lr\bigr).
\tag{31}
\]

The terms respectively cover scalar certificates, backend real cosine nodes,
time nodes, angular tables and normalization square roots, query-basis
normalizations in the sampler, and source orthogonalization. A Cholesky
factorization of the initial \(m\)-by-\(m\) Gram uses at most \(m\)
additional square roots, already covered. Shifted selector inverses and the
metric inverse can use elimination without spectral decompositions or further
special functions. Integer rounding/floor operations used to choose the orders
and enumerate the degree-dependent temporal cutoffs add
\(O(L+\ell_*+1)\) scalar operations; their arithmetic/memory fits the
geometry and mode inventory. The angular Gegenbauer normalizations are prepared
once, and the cosine/harmonic recurrences do not call trigonometric functions
anew at each coefficient or panel. Gaussian primitives themselves are counted
only in (29); an implementation of the normal generator may add its own
elementary calls.

If each class of scalar primitive has respective maximum work costs
\(c_{\rm G},c_\phi,c_{\rm e}\) over the actual requested arguments and
accuracies, add

\[
c_{\rm G}N_{\rm Gaussian}+c_\phi N_\phi+c_{\rm e}N_{\rm elem}
\tag{32}
\]

to arithmetic work, with the optional \(L\) activation calls just described.
Add the maximum simultaneous scratch required by these routines to (28).
One may instead sum the actual per-call costs. The usual bounded-cost primitive
model makes (32) an operation-count shorthand, not a computability theorem for
arbitrary analytic functions or a bit-complexity result.

## 7. Fixed-parameter specialization, proved from the full counts

Only in this section fix \(L,m,d,\gamma,Y>0\), admissible activation/source
bounds and confidence. At the certified original specialization
\(T=32(m/\gamma)\log(en)\), \(\eta=1/n\), the checked backend and bridge
give

\[
J=O(\log(en)^{3/2}),\qquad K=O(\log(en)),\qquad
D=O(\log(en)^{3/2}),
\]
\[
N_t,p+1=O(\log(en)^{5/2}),\quad
N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2}),
\]
\[
N,R,r,q=O(\log(en)^{3d/2+1}).
\tag{33}
\]

For \(d=1\), use the fixed two-point convention in place of angular growth;
it gives the same last exponent \(5/2\). The constants in (33) may now depend
on the fixed admissible structural parameters. They were not hidden in (27).

Substitution into (14) first gives

\[
k_*=O(\log(en)^{3d/2+1}),\qquad JmK=O(\log(en)^{5/2}).
\tag{34}
\]

The two new width-dependent terms are therefore, respectively,

\[
nk_*^2=O(n\log(en)^{3d+2}),
\quad
nm(m+N_x)J(J-1)K(K+1)
=O(n\log(en)^{3d/2+7/2}).
\tag{35}
\]

The activation term has the second exponent in (35). The local contraction
term proportional to \(n\) has exponent at most \(3d/2+2\).
The spatial-first projection terms have exponents at most
\(3d-1/2\) and \(3d/2+7/2\). Orthogonalization and small basis
contractions have exponents at most \(3d+2\). Finally,

\[
nr^3=O(n\log(en)^{9d/2+3}).
\tag{36}
\]

For every fixed integer \(d\ge1\),
\(3d+2\le9d/2+3\),
\(3d/2+7/2\le9d/2+3\), and
\(3d-1/2\le9d/2+3\). Thus every width-proportional term in (27)
is bounded by (36). The remaining terms, including final \(q^2r\)
assembly and geometry, are fixed powers of \(\log(en)\), hence also
bounded by (36) for sufficiently large \(n\). This proves, with bounded-cost
scalar primitives,

\[
T_{\rm setup}=O(n\log(en)^{9d/2+3}).
\tag{37}
\]

For memory, the transcript and global coefficients are
\(O(n\log(en)^{3d/2+1})\). Rank-history and online activation storage
are \(O(n\log(en)^{5/2})\), which fit that bound because \(d\ge1\).
The spatial-first vector buffer is
\(O(n\log(en)^{3d/2-1/2})\). All remaining terms in (28) are either
\(O(n)\) at fixed parameters or fixed powers of \(\log(en)\). Therefore

\[
M_{\rm setup}=O(n\log(en)^{3d/2+1}).
\tag{38}
\]

The primitive inventories specialize to
\(N_{\rm Gaussian}=O(n\log(en)^{3d/2+1})\),
\(N_\phi=O(n+\log(en)^{3/2})\), and a fixed power of \(\log(en)\)
for (31). Additional costs from nonunit scalar backends remain governed by
(32), not automatically by (37).

The exact retained Harmonic state, metric, initial-matrix, and cache inventory
is unchanged, including its bound
\(1020(L+1)R^2+10m(d+1)\), hence
\(O(\log(en)^{3d+2})\) at (33). The Gaussian transcripts, rank histories,
first matrix, source coefficients, bases, and local backend arrays are all
discarded after (15) and the final caches are formed. The reference is a
coupled mathematical Gaussian network after disposal; the retained model does
not include an oracle or hidden reference access.

The checked source approximation and original all-time comparison then give
the same \(n^{-1+o(1)}\) prediction error under the same event and label
allowance. This note changes execution, not that error coefficient. For an
arbitrary supplied budget whose actual horizon or required accuracy grows
faster than in (33), only the finite bounds (14), (27)--(32) are asserted.
They do not imply the logarithmic specializations (37)--(38).

## 8. Dependencies, audit boundary, and remaining gaps

The proof closes the matrix-access and storage obligations once (6) is
available. Its central invariants are exact equality of each current-panel
coefficient, the rank-factor identity (9), exact original initialized source
additions, and exact source/image pairing. The basis-image calls in item 4 are
explicitly retained; skipping them would be an unjustified saving.

The following qualifications remain part of the claim.

- The two-direction, globally adaptive, jointly independent Gaussian sampler
  theorem is an external component to this scoped proof. Its stated arithmetic,
  memory, innovation and normalization counts must be checked before combining
  the result.
- The source event, its partly nonnumerical eventual width gate, the full label
  allowance, the checked Taylor/backend/assembly accuracy theorem and its scalar
  structural certificates remain inherited hypotheses. No new width threshold
  or computable population-gap/moment certificate is proved here.
- Exact arithmetic, rank detection, branching, and exact original activation
  values are used. Finite precision, conditioning, bit complexity, and stability
  of the adaptive Gaussian representation are open implementation questions.
- The fixed-parameter bounds are sufficient and retain a conservative
  \(nr^3\) selector. They are not lower bounds or claims of practical efficiency.
  They cannot be read as a speedup over every implicit or high-order dense
  training implementation; those methods can use the same action sampler.
- Baseline-only, zero-label, and full-coordinate-retention branches have their
  original distinct definitions. A full dense matrix output is outside the
  selected implicit-output premise used in (37)--(38).

The actual scientific input scope was exactly the seven files below. The
complete assembly, bridge, core continuation, activation backend, quadrature
note and notation contract were read. From `RESULT.md`, the complete source
families/initialization, supplied-budget and inventory/gate sections, the full
coordinate-selection and metric proof, the full factored-jet, geometric-basis,
source-selection/assembly cost proofs, and the relevant complete scalar
recurrence definitions were read. No other study, history, external scientific
source, or another current candidate was used.

| Input | SHA-256 |
|---|---|
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `RESULT.md` | `c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278` |
| `LOCAL_CONTINUATION_ASSEMBLY.md` | `488216678b1ea31fcfb8da5f396c8323eae3a38be067c2e431de21a600df2fe2` |
| `LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md` | `dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b` |
| `LOCAL_CONTINUATION_SETUP.md` | `c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe` |
| `LOCAL_ACTIVATION_BACKEND.md` | `cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4` |
| `POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md` | `2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42` |

The required canonical-notation skill remained unreadable at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`, including
an escalated read. Following the supervisor's fallback instruction, this note
uses the explicit repository/user notation requirements, `docs/notation.qmd`,
and the accessible rigorous-math workflow. The conjecture skill's adversarial
audit was also read and applied to the matrix access, event-conditioning,
initialization and hidden-memory claims. No numerical experiment or independent
check is represented by this author derivation.
