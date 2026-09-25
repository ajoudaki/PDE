# Coupled current-state generator

This is a prompt-only theoretical derivation. It assumes that finite-dimensional neuron states are collectively sufficient for an exact current-state description; it does not prove that assumption or replace it by independent particle dynamics. No external or repository scientific sources were read. All formulas below are finite-width identities, or are conditional on explicitly stated reconstruction assumptions. No low-rank hypothesis is used.

Work on an interval where all displayed derivatives exist classically. Smooth activation and reconstruction maps suffice for the algebra; any existence and invertibility assumption for a reduced flow is stated separately.

## 1. Exact finite-width normalization

There are \(n\) neurons in each hidden layer. For the single fixed input \(x\in\mathbb R^d\), use the supplied dynamics

\[
z_1=W_1x/\sqrt d,\quad h_1=\phi(z_1),\quad
z_2=W_2h_1,\quad h_2=\phi(z_2),\quad
f=\frac1n c^Th_2,\quad r=f-y,
\]
\[
\delta_2=c\odot\phi'(z_2),\quad
b_1=W_2^T\delta_2,\quad
\delta_1=\phi'(z_1)\odot b_1,
\]
\[
\dot W_1=-2r\delta_1x^T/\sqrt d,\quad
\dot c=-2rh_2,\quad
\dot W_2=-\frac{2r}{n}\delta_2h_1^T.
\]

Write \(W_0=W_2(0)\), \(\Delta W=W_2-W_0\), and

\[
K_{ij}(t)=n\Delta W_{ij}(t).
\]

Then the exact entrywise source equation is

\[
\dot K_{ij}=-2r\delta_{2,i}h_{1,j},\qquad K_{ij}(0)=0. \tag{1}
\]

Thus a kernel with right-hand side \(-2r\delta_2h_1\) represents \(n\Delta W\), not \(\Delta W\). Put \(\langle u\rangle_1=n^{-1}\sum_j u_j\), \(\langle v\rangle_2=n^{-1}\sum_i v_i\), and \(\langle u,v\rangle_\ell=\langle u v\rangle_\ell\) for the normalized inner product.

For arbitrary differentiable current source vectors \(q(t)\in\mathbb R^n\) and \(p(t)\in\mathbb R^n\), define

\[
G_2[q]=W_0q,\quad G_1[p]=W_0^Tp,\quad
L_2[q]=\Delta Wq,\quad L_1[p]=\Delta W^Tp. \tag{2}
\]

The source vectors may depend on the whole current population. Definitions (2) do not require them to depend on one particle alone.

## 2. Collective dynamics and population derivatives

Let \(a_j\in\mathbb R^{m_1}\), \(b_i\in\mathbb R^{m_2}\), and let \(S=(a_1,\ldots,a_n,b_1,\ldots,b_n)\) denote the full current population. Finite \(m_1,m_2\) are assumed. The admissible structural form is

\[
\dot a_j=F_{1,j}
=F_1(t,a_j,G_{1,j},L_{1,j},Q),\qquad
\dot b_i=F_{2,i}
=F_2(t,b_i,G_{2,i},L_{2,i},Q). \tag{3}
\]

Here each \(G_{\ell,k}\) or \(L_{\ell,k}\) denotes the required collection of receiver-specific messages, and \(Q=\mathcal Q(t,S;W_0)\) denotes population observables. The fixed \(W_0\) remains part of the environment. Even if two receivers have identical local state coordinates, their messages and velocities can differ. Consequently (3) is a coupled ODE on \(S\).

For ordinary moments with fixed \(C^1\) test functions,

\[
Q^1_\alpha=\frac1n\sum_j A_\alpha(a_j),\qquad
Q^2_\beta=\frac1n\sum_i B_\beta(b_i),
\]

their exact derivatives are

\[
\dot Q^1_\alpha=\frac1n\sum_j\nabla A_\alpha(a_j)\cdot F_{1,j},\qquad
\dot Q^2_\beta=\frac1n\sum_i\nabla B_\beta(b_i)\cdot F_{2,i}. \tag{4}
\]

For a fixed pair test \(C_\gamma\), the same rule gives

\[
\frac{d}{dt}\frac1{n^2}\sum_{i,j}C_\gamma(b_i,a_j)
=\frac1{n^2}\sum_{i,j}
\left[\nabla_bC_\gamma\cdot F_{2,i}+\nabla_aC_\gamma\cdot F_{1,j}\right]. \tag{5}
\]

In full generality,

\[
\dot Q=\partial_t\mathcal Q+D_S\mathcal Q[V],\qquad
V=(F_{1,1},\ldots,F_{1,n},F_{2,1},\ldots,F_{2,n}). \tag{6}
\]

These are exact evolution identities, not assertions that \(\dot Q\) is determined by \(Q\) alone. The messages on the right can require the entire population. If \(Q\) is maintained as an additional variable, (6) with consistent initial data preserves \(Q=\mathcal Q(t,S;W_0)\).

One may instead use empirical measures

\[
\mu_1=\frac1n\sum_j\delta_{a_j},\qquad
\mu_2=\frac1n\sum_i\delta_{b_i}.
\]

Their exact weak derivatives satisfy

\[
\frac{d}{dt}\int A(a)\,d\mu_1(a)
=\frac1n\sum_j\nabla A(a_j)\cdot F_{1,j},
\quad
\frac{d}{dt}\int B(b)\,d\mu_2(b)
=\frac1n\sum_i\nabla B(b_i)\cdot F_{2,i}. \tag{7}
\]

The two unmarked marginal measures need not preserve the alignment between neuron states and the rows and columns of \(W_0\). Calling \(Q\) a “full distribution” must therefore specify enough marked or relational information to retain any alignment needed by the claimed closure.

## 3. The coupled kernel generator

Suppose a common differentiable reconstruction is valid on the admissible configurations:

\[
K_{ij}(t)=\kappa(t,b_i(t),a_j(t),Q(t);W_0). \tag{8}
\]

The \(W_0\) argument is fixed and is suppressed below. Applying the ordinary chain rule to (8) and using (1) yields

\[
\partial_t\kappa
+F_{2,i}\cdot\nabla_b\kappa
+F_{1,j}\cdot\nabla_a\kappa
+D_Q\kappa[\dot Q]
=-2r\delta_{2,i}h_{1,j}. \tag{9}
\]

Every term is evaluated at \((t,b_i,a_j,Q)\). The endpoint velocities in (9) are the coupled velocities (3), with their actual receiver messages. Equation (9) is required along admissible configurations; it is not automatically a pointwise PDE on every freely chosen combination of \(b,a,Q\).

When \(Q\) consists of empirical measures, the last term denotes the directional derivative along their evolution (7), provided the asserted functional derivative exists. It is not an assumption that the measures have smooth densities.

Two qualifications matter.

1. **Collective sufficiency does not itself imply the compressed representation (8).** The exact general reconstruction is \(K_{ij}=\mathcal K_{ij}(t,S;W_0)\). Reducing this to \((b_i,a_j,Q)\) requires that these arguments determine the entry for all admissible configurations. If two configurations have the same proposed arguments and different \(K_{ij}\), that particular choice of arguments fails. Receiver-specific fields can be added to the endpoints or to the reconstruction arguments. If they are explicit extra arguments, their own derivatives must appear in the chain rule.
2. **Finite state dimension does not mean finitely many independent particles.** A sufficient full-state reconstruction obeys the exact generator

\[
\partial_t\mathcal K_{ij}
+\sum_{\ell=1}^n F_{1,\ell}\cdot\nabla_{a_\ell}\mathcal K_{ij}
+\sum_{k=1}^n F_{2,k}\cdot\nabla_{b_k}\mathcal K_{ij}
=-2r\delta_{2,i}h_{1,j}. \tag{10}
\]

Equation (9) is the chain-rule reduction of (10) when (8) is available. Differentiability is an additional regularity assumption; mere set-theoretic recoverability from \(S\) is not enough to justify these derivatives.

If \(h_1\) and test sources \(q\) are local readouts of \(a\), and \(p\) is a local readout of \(b\), (8) gives the exact learned messages

\[
L_2[q]_i=\int\kappa(t,b_i,a,Q)q(a)\,d\mu_1(a),\qquad
L_1[p]_j=\int\kappa(t,b,a_j,Q)p(b)\,d\mu_2(b). \tag{11}
\]

The analogous sums apply to sources that also depend on current fields. An arbitrary nonseparable kernel is allowed; no finite-rank expansion is being imposed.

## 4. Avoiding a double count of population motion

There are two different time-dependent kernel conventions.

For a universal function \(\kappa(t,b,a,Q)\), the partial derivative \(\partial_t\) holds \(b,a,Q\) fixed. Equation (9) must include \(D_Q\kappa[\dot Q]\).

For one prescribed population trajectory, define instead

\[
\widehat\kappa_t(b,a)=\kappa(t,b,a,Q(t)).
\]

Then, with \(b,a\) fixed,

\[
\partial_t\widehat\kappa_t
=\partial_t\kappa+D_Q\kappa[\dot Q].
\]

The trajectory-conditioned equation is therefore

\[
\partial_t\widehat\kappa_t
+F_{2,i}\cdot\nabla_b\widehat\kappa_t
+F_{1,j}\cdot\nabla_a\widehat\kappa_t
=-2r\delta_{2,i}h_{1,j}. \tag{12}
\]

Adding another \(D_Q\kappa[\dot Q]\) to (12) counts the same population motion twice. Conversely, dropping it from (9) omits that motion. A trajectory-conditioned kernel need not be a universal current-state functional usable for other populations or restarts.

If \(Q\) itself contains the receiver and sender states, (9) is still the correct chain rule: the endpoint derivatives hold \(Q\) fixed, while \(D_Q\kappa[\dot Q]\) differentiates the separate \(Q\) argument. Their sum differentiates the composition once. The distinction concerns independent arguments of the reconstruction, not disjoint subsets of neurons.

## 5. Exact message identities

Differentiate (2) directly. Since \(W_0\) is constant,

\[
\frac{d}{dt}G_2[q]=G_2[\dot q],\qquad
\frac{d}{dt}G_1[p]=G_1[\dot p]. \tag{13}
\]

For the learned forward message,

\[
\begin{aligned}
\frac{d}{dt}L_2[q]_i
&=\sum_j\dot{\Delta W}_{ij}q_j
 +\sum_j\Delta W_{ij}\dot q_j\\
&=-2r\delta_{2,i}\langle h_1q\rangle_1
 +L_2[\dot q]_i.
\end{aligned} \tag{14}
\]

Likewise,

\[
\frac{d}{dt}L_1[p]_j
=-2rh_{1,j}\langle\delta_2p\rangle_2
 +L_1[\dot p]_j. \tag{15}
\]

The derivatives \(\dot q,\dot p\) are total derivatives. For example, if \(q_j=q(t,a_j,Q)\),

\[
\dot q_j=\partial_tq+\nabla_aq\cdot F_{1,j}+D_Qq[\dot Q]. \tag{16}
\]

If \(q_j\) also depends on a receiver field, its field derivative contributes as well. In particular \(\dot q_j\) may fail to be a common function of \(a_j\) alone, even when \(q_j\) initially has that form. Identities (13)–(15) remain valid, because their inputs can be arbitrary current source vectors. A proposed finite family of messages still needs a separate closure argument for these differentiated inputs.

These identities can also be recovered from (9) and the moving empirical measures in (11). The sender transport differentiates the summation points, and the receiver transport differentiates the receiver. The population derivative is included exactly once. Direct matrix differentiation provides a normalization and bookkeeping check that does not require any kernel representation.

## 6. Explicit current-state equations for the supplied network

Let \(s=\lVert x\rVert^2/d\) and write \(B=G_1[\delta_2]+L_1[\delta_2]=W_2^T\delta_2\). Then

\[
\dot z_{1,j}=-2rs\phi'(z_{1,j})B_j,\qquad
v_j:=\dot h_{1,j}=-2rs\phi'(z_{1,j})^2B_j. \tag{17}
\]

Differentiating \(z_2=W_2h_1\) gives

\[
\dot z_{2,i}
=-2r\delta_{2,i}\langle h_1^2\rangle_1
+G_2[v]_i+L_2[v]_i,\qquad
\dot c_i=-2r\phi(z_{2,i}). \tag{18}
\]

Thus the first-layer velocity depends on the current backward message, while the second-layer velocity depends on the current forward transport of a source vector that already contains a backward message. This dependence is entirely on the current coupled configuration whenever the assumed reconstruction supplies \(L_1,L_2\). It is not an independent per-neuron vector field, and (17)–(18) alone do not prove that a chosen finite message list closes.

For a useful scalar consistency check, differentiate \(r=n^{-1}\sum_i c_i\phi(z_{2,i})-y\). Using (18), then the adjoint identity \(\langle\delta_2,W_2v\rangle_2=\langle W_2^T\delta_2,v\rangle_1\), yields

\[
\begin{aligned}
\dot r
&=-2r\langle h_2^2\rangle_2
 -2r\langle\delta_2^2\rangle_2\langle h_1^2\rangle_1
 +\langle B,v\rangle_1\\
&=-2r\left[
\langle h_2^2\rangle_2
+\langle\delta_2^2\rangle_2\langle h_1^2\rangle_1
+s\langle\phi'(z_1)^2B^2\rangle_1
\right].
\end{aligned} \tag{19}
\]

All factors in the bracket are nonnegative for real-valued states. The loss derivative is therefore \(d(r^2)/dt=-4r^2\) times that bracket, consistent with the supplied training rates.

## 7. Global reversibility is not particlewise reversibility

Assume the coupled vector field has a unique differentiable flow \(\Phi_{t,s}\) on the region and time interval under consideration, with backward trajectories remaining in that region. Then \(S(s)=\Phi_{s,t}(S(t))\). This inverse requires the full current population. It does not assert maps \(a_j(0)=\psi_{1,t}(a_j(t))\) or \(b_i(0)=\psi_{2,t}(b_i(t))\).

A symmetric elementary example is

\[
\dot a_j=Q,\qquad Q=\frac1n\sum_j a_j.
\]

Here \(Q(t)=e^tQ(0)\) and

\[
a_j(t)=a_j(0)+(e^t-1)Q(0),\qquad
a_j(0)=a_j(t)-(1-e^{-t})Q(t).
\]

The global flow is invertible, but for \(n\ge2\) and \(t\ne0\), \(a_j(t)\) alone does not determine \(a_j(0)\): the inverse also uses the current population mean.

Conditional on a known closed global flow and the readouts along it, equation (1) can be written as a current-state functional

\[
\mathcal K_{ij}(t,S)
=-2\int_0^t
r\bigl(s,\Phi_{s,t}(S)\bigr)
\delta_{2,i}\bigl(s,\Phi_{s,t}(S)\bigr)
h_{1,j}\bigl(s,\Phi_{s,t}(S)\bigr)\,ds. \tag{20}
\]

This is the characteristic representation of (10) with zero initial learned weights. It shows how collective reversibility supports a full-current-state representation. It neither produces independent endpoint inverses nor constructs an unknown finite-dimensional closure: the closed flow used by (20) was assumed available.

The exact conclusions are the source normalization, the coupled chain rule, the population derivative identities, and the message identities. Finite-dimensional collective sufficiency is the standing premise. Whether a particular choice of neuron states, receiver fields, and aggregate arguments realizes that premise remains a distinct representation and closure question.
