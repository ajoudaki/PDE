# Approximate scalar compression of the response-memory population closure

## 1. The question answered here

Fix the number of training samples \(m\), network depth and response-memory
order \(P\). Let \(n\) be hidden width. The parent model in this note is the
already derived order-\(P\) response-memory **population closure**, including
the reused initialized operators \(W_0,W_0^\top\). We ask whether its neuron
vectors can be replaced by finitely many evolving scalars while retaining its
training loss, specified query outputs, or fitted function on the circle.

This is an approximation question. Exact finite moment closure is neither
required nor expected.

There are three distinct conclusions.

1. **A convergent scalar construction already exists at every fixed realized
   width.** The clipped output-reachable forest hierarchy is a finite
   autonomous scalar ODE. On every prescribed finite interval, its requested
   outputs converge uniformly to those of the population closure as the
   aggregate cutoff \(K\to\infty\).
2. **The whole circle can be handled without a query mesh.** Add mixed
   angle-neuron contractions for finitely many Fourier coefficients and for
   the direct energy \(\int f^2\). Taking first \(K\to\infty\) and then the
   Fourier cutoff \(J\to\infty\) recovers the parent fitted function in
   \(L^2\), uniformly over the prescribed time interval.
3. **A cutoff uniform in width is not yet proved for dense Gaussian
   initialization.** At fixed \(K\), the number of scalar coordinate types is
   independent of \(n\), but the current a priori bounds and therefore the
   sufficient \(K\) may depend on \(n\). A precise width-uniform forest bound
   would close this gap. Without some restriction of this kind, universal
   whole-function compression is impossible.

Thus the scalar route is mathematically principled and convergent, but its
economical width-uniform version remains a concrete open problem.

## 2. Start from the population closure, not from a new dictionary

Write the fixed-\(P\) parent state as

\[
  \dot X^{(n)}=F_{n,P}(X^{(n)}),
  \qquad O^{(n)}(t)=\mathcal O(X^{(n)}(t)).                 \tag{1}
\]

The state \(X^{(n)}\) contains the current forward and backward neuron fields,
their response-history coordinates, the outer trainable weights, the clock,
and the actions of the same initialized matrices in both orientations. The
finite vector \(O^{(n)}\) lists only the quantities to be reported: for
example the \(m\) training predictions, their loss and some query outputs.

The construction below never freezes current responses in their initialized
span. It differentiates normalized contractions of the **moving parent
fields**. Initialized matrices occur as fixed edges inside those
contractions, so the same realized \(W_0\) is reused consistently in forward
and transpose actions.

## 3. The exact infinite scalar hierarchy

A decorated forest \(H\) specifies:

* finitely many neuron indices and their layer types;
* current forward, backward or history fields attached to those indices; and
* initialized matrix entries joining indices in adjacent layers.

Its scalar value \(q_H(X)\) is the normalized sum over all assignments of its
neuron indices. A typical one-edge example is

\[
 q_H(X)=\frac1n u^\top W_0v.                              \tag{2}
\]

Products such as \(n^{-1}\sum_i B_{k,i}h_i\),
\(n^{-1}\sum_i h_i^2\), and all of the mixed contractions forced by their
derivatives are included. Disconnected forests factor into products of their
connected components.

Differentiate \(q_H(X(t))\) with the product rule and substitute the parent
population equations. Every differentiated decoration is replaced by one of
finitely many local templates. Factoring disconnected pieces then gives

\[
 \boxed{
 \dot q_H
   =G_H(q,L)
   =\sum_{\nu=1}^{N_H}a_{H\nu}(r,L)
        \prod_{J\in\pi_{H\nu}}q_J .}
                                                               \tag{3}
\]

Here \(L\) is the response-memory clock and \(r\) is computed from the output
coordinates. For fixed \(m,P\) and depth:

* the list of replacement templates is finite;
* differentiating a diagram of grade \(s\) increases grade by at most a fixed
  number \(\Delta\);
* the number and total coefficient size of its terms grow at most linearly
  in \(s\); and
* neither the diagram types nor (3) refer to the numerical width \(n\).

Equation (3) is an exact countable scalar rewriting of the population
closure. It is not yet a finite model, but it identifies exactly what
information a finite scalar approximation must discard.

## 4. The finite autonomous scalar ODE

Retain the connected diagrams reachable by differentiating the requested
outputs and having grade at most \(K\). Delete a generator monomial whenever
one of its connected factors has grade greater than \(K\). This is the
zero-tail truncation \(G_K\).

The unmodified zero-tail ODE can leave the region occupied by realizable
population moments. To prevent that independent instability, use an a priori
parent bound. On a fixed horizon \([0,T]\), the finite-dimensional parent
trajectory has a computable bound

\[
 |q_H(t)|\le B_T^{|H|}.                                    \tag{4}
\]

The bound follows from the established parent estimates and the realized
initial data; it does not require observing the future trajectory. Choose
\(R\ge B_T\) and define

\[
 S_H(z_H)=\operatorname{clip}
       \bigl(z_H,-R^{|H|},R^{|H|}\bigr).                   \tag{5}
\]

The finite scalar model is

\[
 \boxed{
 \dot z_H=G_{K,H}(S(z),L_z),\qquad
 \dot L_z=\rho\bigl(S(z_{\rm out})\bigr),\qquad L_z(0)=1,}
                                                               \tag{6}
\]

initialized with the exact contractions of the given network. The reported
predictions are the clipped output coordinates. After initialization, (6)
uses only its retained scalars and fixed coefficients. It stores no neuron
vectors and performs no \(W_0\) or \(W_0^\top\) matrix-vector action.

Clipping is part of the approximation, not oracle forcing. It is inactive on
the parent path by (4), while it prevents the approximate scalar path from
generating arbitrarily large spurious moments.

## 5. Finite-horizon convergence theorem at fixed realized width

**Theorem 1 (scalar approximation of the parent closure).** Fix finite
\(n,m,P\), network depth, initialized weights, data, requested finite output
list and \(T<\infty\). Assume the parent response-memory solution and its
primitive fields obey the established finite-horizon bounds. Then every
finite system (6) has a global solution and

\[
 \max_{a}\sup_{0\le t\le T}
 \left|S_{H_a}(z_{H_a}^{K}(t))-O_a^{(n)}(t)\right|
 \longrightarrow0
 \quad\text{as }K\to\infty.                               \tag{7}
\]

The same statement holds for every fixed retained contraction and for the
clock.

### Proof

First, every input to the right-hand side of (6) is clipped and \(L_z\ge1\).
For constants \(A,D\) independent of \(K\), a grade-\(s\) row obeys

\[
 |\dot z_H|\le A s R^{s+D},\qquad
 0\le\dot L_z\le R^3+Y,                                  \tag{8}
\]

where \(Y\) bounds the labels. Thus a finite cutoff cannot escape in finite
time. On \([0,T]\), all of its coordinates satisfy a \(K\)-independent
exponential envelope

\[
 |z_H(t)|\le [R(1+AT R^D)]^{|H|}.                         \tag{9}
\]

Second, clipping creates no defect on the target because (4) implies
\(S_H(q_H)=q_H\). It is also nonexpansive:

\[
 |S_H(z_H)-q_H|\le |z_H-q_H|.                            \tag{10}
\]

Normalize errors of all grades through \(s\) by the exponential envelope and
call their maximum \(E_s\). Telescoping the products in (3), using (10), and
using that a grade-\(s\) row only calls grades through \(s+\Delta\), gives on
every proof interval

\[
 E_s(t)\le E_s(t_0)+C_Ts\int_{t_0}^tE_{s+\Delta}(u)\,du,  \tag{11}
\]

with \(C_T\) independent of \(K\). There is no deleted source in (11) while
\(s+\Delta\le K\).

Iterating (11) \(r\) times produces an ordered \(r\)-simplex integral. Its
factor \(1/r!\) cancels the product of the successive linear grade factors,
up to a binomial term. If \(C_T\Delta h<1\), the remaining boundary term is
bounded by

\[
 2{r+\lceil s/\Delta\rceil-1\choose r}
       (C_T\Delta h)^r,                                  \tag{12}
\]

which tends to zero as the distance \(r\) from the requested grade to the
cutoff tends to infinity. Exact initialization removes all finite-level
initial errors on the first interval. A finite chain of such proof intervals
covers \([0,T]\), proving (7).

The grade-halving version gives an explicit, conservative certificate for
ordinary training outputs, whose grade is three. Let

\[
 N=\max\{1,\lceil16C_T\Delta T\rceil\},\qquad
 j=\left\lfloor\frac{K}{\Delta2^N}\right\rfloor .         \tag{13}
\]

When \(j\ge\lceil3/\Delta\rceil\),

\[
 \max_a\sup_{t\le T}|\widehat f_{K,a}(t)-f_{P,a}(t)|
 \le 2N R_T^3\,4^{-j}.                                   \tag{14}
\]

The certificate is far too pessimistic to imply a practical small model.
It does prove that the scalar approximation cannot remain separated from the
parent as \(K\to\infty\). \(\square\)

## 6. Loss and fixed query outputs

If the training residual has RMS at most \(B\) and the scalar prediction
error has RMS at most \(\epsilon\), then

\[
 |\widehat{\mathcal L}-\mathcal L|
 \le 2B\epsilon+\epsilon^2.                              \tag{15}
\]

Consequently Theorem 1 gives uniform finite-horizon convergence of training
loss. Any finite list of passive query outputs is handled by adding their
output-reachable diagrams; those queries do not feed back into training.

This already answers the approximate question for loss and finitely many
test points. It does not require the loss itself to be a Markov state.

## 7. The whole circle without a test mesh

Let \(f_P(t,\theta)\) be the parent closure output on the circle, with
normalized angular measure \(d\nu\). Retain

\[
 c_k(t)=\int f_P(t,\theta)e^{-ik\theta}\,d\nu(\theta),
 \qquad |k|\le J,                                        \tag{16}
\]

and the direct energy coordinate

\[
 A(t)=\int f_P(t,\theta)^2\,d\nu(\theta).                \tag{17}
\]

Their derivatives are not functions of the coefficients alone. The correct
compiler adds an angle vertex shared by all response factors evaluated at the
same \(\theta\), integrates that vertex once, and differentiates the attached
moving neuron fields. This generates mixed angle-neuron forest contractions.
At every fixed \(J,K\), there are finitely many scalar types, independent of
both \(n\) and any angular quadrature grid. The clipped proof above applies
unchanged to this finite requested list.

Reconstruct

\[
 \widehat f_{K,J}(t,\theta)
   =\sum_{|k|\le J}\widehat c_{K,k}(t)e^{ik\theta}.        \tag{18}
\]

Parseval and the triangle inequality give

\[
 \sup_{t\le T}\|\widehat f_{K,J}(t)-f_P(t)\|_{L^2}
 \le
 \sup_{t\le T}
 \left(\sum_{|k|\le J}|\widehat c_{K,k}(t)-c_k(t)|^2\right)^{1/2}
 +\sup_{t\le T}\|(I-\Pi_J)f_P(t)\|_{L^2}.               \tag{19}
\]

For fixed \(J\), the first term tends to zero by Theorem 1. At fixed finite
width, the map \(t\mapsto f_P(t,\cdot)\) is continuous into \(L^2\), so its
image of \([0,T]\) is compact. Fourier projections converge strongly to the
identity and are contractions; a finite-net argument therefore gives

\[
 \sup_{t\le T}\|(I-\Pi_J)f_P(t)\|_{L^2}\longrightarrow0. \tag{20}
\]

Hence, for every \(\epsilon>0\), one can first choose \(J\) and then \(K\) so
that (19) is below \(\epsilon\). Spatial smoothness supplies rates: a uniform
\(H^s\) bound gives an \(O(J^{-s})\) tail, while a uniform analytic strip gives
an exponential tail.

For RMS against a target \(g\), a full function reconstruction is not needed.
If \(g_k=0\) for \(|k|>J_g\), then

\[
 E_P=A-2\operatorname{Re}\sum_{|k|\le J_g}c_k\overline{g_k}
       +\|g\|_2^2.                                      \tag{21}
\]

If \(|\widehat A-A|\le\eta_A\) and

\[
 d_g^2=\sum_{|k|\le J_g}|\widehat c_k-c_k|^2,
\]

then

\[
 |\widehat E_P-E_P|\le\eta_A+2\|g\|_2d_g,\qquad
 |\sqrt{\max(0,\widehat E_P)}-\sqrt{E_P}|
 \le\sqrt{\eta_A+2\|g\|_2d_g}.                          \tag{22}
\]

For general \(g\in L^2\), truncating its correlation adds at most
\(2\sup_{t\le T}\|f_P(t)\|_2\|g-\Pi_{J_g}g\|_2\). One can alternatively
compile the direct mixed observable \(\int(f_P-g)^2\), which also has the
fixed-width finite-horizon convergence theorem.

## 8. Comparison with the dense network

Let \(f_{\rm dense}\) be the dense trained network and \(f_P\) the population
response-memory closure. Every normed output comparison splits as

\[
 \|\widehat f_{K,J}-f_{\rm dense}\|
 \le \|\widehat f_{K,J}-f_P\|+\|f_P-f_{\rm dense}\|.      \tag{23}
\]

The first term is controlled by (19). For the old activity clock, the parent
theorem gives the established finite-horizon history error of order
\(1/\sqrt{P(P+1)}=O(P^{-1})\), with its stated stability constant. Thus one
chooses \(P\) for the dense-to-parent error, \(J\) for the spatial tail, and
\(K\) for the scalar-hierarchy error. This gives, at each fixed realized
width, an autonomous finite scalar approximation to the dense loss and fitted
circle function at any prescribed finite-horizon tolerance.

This statement is uniform on \([0,T]\) and, through (19), global over the
circle. It is not uniform over \(T=\infty\); that would additionally require
bounded total activity or a long-time contractive stability estimate.

## 9. What is and is not independent of width

For every fixed \(K\), the **number and form** of coordinates in (6) depend on
\(m,P\), depth, the requested observables and \(K\), but not on \(n\). The
initial values are normalized contractions of the realized width-\(n\)
network and may be computed once before discarding the population.

Theorem 1 nevertheless fixes \(n\) before choosing \(K\). Its bound uses a
parent envelope \(B_T\) and a generator constant \(C_T\) that may depend on
that realized width. Therefore it does not yet prove the stronger statement

\[
 \sup_{n\ge n_0}\sup_{t\le T}
 |\widehat O_{K}^{(n)}(t)-O_P^{(n)}(t)|
 \le\varepsilon_K(T),\qquad \varepsilon_K(T)\to0.        \tag{24}
\]

Equation (24) is the real width-removal target. It would follow from:

1. width-uniform bounds on all output-reachable normalized contractions;
2. width-uniform generator and feedback Lipschitz constants in the same
   weighted hierarchy norm; and
3. width-uniform initialization control for every fixed diagram list.

For a deterministic operator family with uniformly bounded forward and
transpose \(\ell_\infty\)-operator norms, bounded primitive fields give the
needed exponential forest envelope directly, so the existing proof becomes
width uniform. This is a genuine positive class, but dense Gaussian matrices
with the neural scaling do not have uniform absolute row sums.

For dense Gaussian \(W_0\), entrywise absolute-value bounds destroy the
cancellations that make normalized contractions order one. The promising
route is to place the hierarchy in Gaussian/Hermite or hypercontractive
order weights rather than use \(\max_{ij}|W_{0,ij}|\). One must then prove that
the weighted analogue of the iterated boundary term (12) still tends to zero.
That estimate has not been established in this study. It is the precise
theoretical gap, rather than a failure to identify scalar coordinates.

## 10. Why no unrestricted theorem can hold for the whole fitted function

There is a simple approximate obstruction once the admitted network family
can contain arbitrarily large function subspaces.

**Proposition 2 (continuous compression lower bound).** Suppose a width-\(N\)
architecture can realize

\[
 f_a=\sum_{j=1}^N a_j\psi_j,\qquad a\in S^{N-1},           \tag{25}
\]

where \(\{\psi_j\}\) is orthonormal in the requested input-space \(L^2\)
metric. Let a compressor use a continuous encoder
\(E:S^{N-1}\to\mathbb R^K\) and any decoder
\(D:\mathbb R^K\to L^2\). If \(K<N\), its worst-case error is at least one:

\[
 \sup_{a\in S^{N-1}}\|D(E(a))-f_a\|_2\ge1.               \tag{26}
\]

**Proof.** By Borsuk--Ulam, for \(K<N\) there is an \(a\) with
\(E(a)=E(-a)\). The decoder returns the same function for both inputs, while

\[
 \|f_a-f_{-a}\|_2=2.
\]

The triangle inequality forces at least one of the two reconstruction errors
to be at least one. \(\square\)

The networks may be made stationary by choosing zero training residual, so
time evolution does not remove this obstruction. Standard nonpolynomial
ridge networks can generate arbitrarily large linearly independent finite
feature spaces on the circle; orthonormalizing their span gives (25).

This proposition does **not** rule out the desired compression for the fixed
Gaussian initialization and fixed smooth task. It says that a width-uniform
whole-function theorem needs a compactness assumption, such as a uniform
Fourier/Sobolev tail, a population limit, or a restricted initialization
law. Training loss and a finite list of outputs live in a fixed-dimensional
readout space and do not face this particular spatial metric-entropy
obstruction.

## 11. Scientific verdict and next decisive step

The failed small scalar ODE in the experiments is evidence that a low-order
unsaturated cutoff is inaccurate. It is not evidence that scalar
approximation must diverge: that solver omitted the stabilization and did not
test the convergent \(K\)-sequence certified above. Conversely, Theorem 1 is
an existence result and does not show that a useful small \(K\) exists.

The correct next theory target is (24) for the actual normalized Gaussian
initialization. The decisive calculation is to bound output-reachable forest
contractions in an order-weighted norm uniformly in \(n\), then insert those
bounds into (11)--(12). The corresponding decisive experiment is to implement
the clipped forest cutoffs for increasing \(K\), measure both output error and
the first omitted boundary terms, and repeat across widths. A plateau in the
required \(K\) would support (24); systematic growth with width would expose
which diagram family prevents it.

Until that test and estimate are completed, the justified conclusion is:

* approximate population-to-scalar compression is proved on every fixed
  finite-width, finite-time problem;
* whole-circle loss and output can be recovered without a grid;
* a single economical cutoff uniform in dense Gaussian width is an open,
  sharply formulated question; and
* a universal whole-function theorem without regularity or initialization
  restrictions is impossible by Proposition 2.
