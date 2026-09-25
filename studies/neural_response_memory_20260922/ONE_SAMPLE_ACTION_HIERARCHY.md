# One-sample current action hierarchy

Status: exact finite-width identities for the supplied gradient flow, on every interval where that flow exists. The hierarchy gives no theorem of closure with a width-independent number of action coordinates. This is a prompt-only independent derivation; no scientific repository inputs or external sources were used.

## Setup and normalization

There are two layers of width \(n\). The fixed sample is \(x\in\mathbb R^d\), with target \(y\in\mathbb R\), and \(\lambda_x=\|x\|^2/d\). Inner products on either width-\(n\) layer are

\[
\langle u,v\rangle=\frac1n u^Tv,
\qquad \langle u^2\rangle=\langle u,u\rangle.
\]

All vector products below, except displayed matrix products and inner products, are coordinatewise. The network and supplied dynamics are

\[
\begin{aligned}
z_1&=W_1x/\sqrt d,&h_1&=\phi(z_1),\\
z_2&=W_2h_1,&h_2&=\phi(z_2),\\
f&=\langle c,h_2\rangle,&r&=f-y,\\
\delta_2&=c\phi'(z_2),&b_1&=W_2^T\delta_2,
\qquad\delta_1=\phi'(z_1)b_1,\\
\dot W_1&=-2r\delta_1x^T/\sqrt d,&
\dot c&=-2rh_2,&
\dot W_2&=-\frac{2r}{n}\delta_2h_1^T.
\end{aligned}
\]

Write \(W_2=W_0+\Delta W\), with \(W_0=W_2(0)\) fixed and \(\Delta W(0)=0\). Thus \(W_0\) is the actual initial linear map, including whatever width scaling was built into its definition. The equations introduce no additional hidden factor of \(n^{-1/2}\).

For a lower-layer vector \(q\in\mathbb R^n\) and an upper-layer vector \(p\in\mathbb R^n\), define the learned actions

\[
A_t[q]=\Delta W(t)q,
\qquad B_t[p]=\Delta W(t)^Tp.
\]

Equal layer widths do not identify the two index sets: \(A\) maps lower-layer inputs to upper-layer outputs, and \(B\) maps upper-layer inputs to lower-layer outputs. Keeping these types distinguishes \(W_0q\) from \(W_0^Tp\).

The assigned dynamics are a layer-scaled gradient flow of the loss \(L=r^2\): relative to ordinary Euclidean parameter gradients, the learning rates of \(W_1,c\) are \(n\), while that of \(W_2\) is \(1\). The derivations below use the assigned dynamics verbatim.

## Exact first equations

Introduce current scalars and source vectors

\[
\begin{aligned}
H&=\langle h_1^2\rangle,& D&=\langle\delta_2^2\rangle,\\
q_0&=\phi'(z_1)^2b_1,\\
U&=H\delta_2+\lambda_x\bigl(W_0q_0+A[q_0]\bigr),\\
p_0&=h_2\phi'(z_2)+c\phi''(z_2)U,\\
V&=Dh_1+W_0^Tp_0+B[p_0].
\end{aligned}
\]

These definitions are algebraic in the current state and the retained action coordinates; they contain neither historical integrals nor prescribed future values. Direct differentiation gives

\[
\begin{aligned}
\dot z_1&=-2r\lambda_x\phi'(z_1)b_1,
&\dot h_1&=-2r\lambda_x q_0,\\
\dot z_2&=-2rU,
&\dot h_2&=-2r\phi'(z_2)U,\\
\dot c&=-2rh_2,
&\dot\delta_2&=-2rp_0,\\
\dot b_1&=-2rV.
\end{aligned}
\tag{1}
\]

For example,

\[
\begin{aligned}
\dot z_2
&=\dot W_2h_1+W_2\dot h_1\\
&=-2rH\delta_2-2r\lambda_x(W_0q_0+A[q_0]),\\
\dot b_1
&=\dot W_2^T\delta_2+W_2^T\dot\delta_2\\
&=-2rDh_1-2r(W_0^Tp_0+B[p_0]).
\end{aligned}
\]

These two product rules account for the rank-one update terms in (1). They also retain the actual mixing of the current vectors by the fixed map \(W_0\).

The output and residual obey a particularly short exact law:

\[
\dot f=\dot r=-2r\mathcal K,
\qquad
\mathcal K=\langle h_2^2\rangle+HD
                 +\lambda_x\langle\delta_1^2\rangle\ge0.
\tag{2}
\]

Indeed,

\[
\begin{aligned}
\dot f
&=\langle\dot c,h_2\rangle+
  \langle c\phi'(z_2),\dot z_2\rangle\\
&=-2r\bigl(\langle h_2^2\rangle+HD
       +\lambda_x\langle\delta_2,W_2q_0\rangle\bigr),\\
\langle\delta_2,W_2q_0\rangle
&=\langle W_2^T\delta_2,q_0\rangle
 =\langle b_1,\phi'(z_1)^2b_1\rangle
 =\langle\delta_1^2\rangle.
\end{aligned}
\]

Consequently \(\dot L=-4r^2\mathcal K\). Equation (2) does not make \(r\) autonomous by itself: its coefficient \(\mathcal K\) is a current population observable governed by the rest of the dynamics.

## The action product rule

For every differentiable current input vector \(q(t)\) of lower-layer type and \(p(t)\) of upper-layer type,

\[
\begin{aligned}
\frac{d}{dt}A[q]
  &=-2r\delta_2\langle h_1,q\rangle+A[\dot q],\\
\frac{d}{dt}B[p]
  &=-2rh_1\langle\delta_2,p\rangle+B[\dot p].
\end{aligned}
\tag{3}
\]

For the fixed map, instead,

\[
\frac{d}{dt}(W_0q)=W_0\dot q,
\qquad
\frac{d}{dt}(W_0^Tp)=W_0^T\dot p.
\tag{4}
\]

Thus every additional action equation contains a current empirical pairing and a new learned action on the differentiated source. The differentiated fixed-map terms must also be retained. A list of marginal moments does not determine \(W_0\dot q\) or \(W_0^T\dot p\) without further structure that recovers the relevant labeled input vectors.

## First generated sources and their ODEs

Set

\[
A_0=A[q_0],\qquad B_0=B[p_0],
\qquad C=\langle h_1,q_0\rangle,
\qquad E=\langle\delta_2,p_0\rangle.
\]

Define

\[
q_1=\phi'(z_1)^2\bigl(V+2\lambda_x\phi''(z_1)b_1^2\bigr).
\tag{5}
\]

Differentiating \(q_0=\phi'(z_1)^2b_1\) using (1) proves

\[
\dot q_0=-2rq_1.
\]

Let \(A_1=A[q_1]\). Then

\[
\dot A_0=-2r(\delta_2C+A_1),
\qquad \dot H=-4r\lambda_xC.
\tag{6}
\]

To differentiate the upper-layer source, first define

\[
U_1=Hp_0+3\lambda_xC\delta_2
                  +\lambda_x(W_0q_1+A_1).
\tag{7}
\]

In fact, differentiating \(U=H\delta_2+\lambda_x(W_0q_0+A_0)\) gives

\[
\begin{aligned}
\dot U
&=(-4r\lambda_xC)\delta_2-2rHp_0
    -2r\lambda_xW_0q_1
    -2r\lambda_x(\delta_2C+A_1)\\
&=-2rU_1.
\end{aligned}
\]

The factor \(3\) in (7) has two contributions from \(\dot H\) and one from \(\dot W_2q_0\). Now define

\[
p_1=
 \bigl(\phi'(z_2)^2+2h_2\phi''(z_2)\bigr)U
 +c\phi'''(z_2)U^2
 +c\phi''(z_2)U_1.
\tag{8}
\]

The derivative of \(h_2\phi'(z_2)\) contributes
\(-2r(\phi'(z_2)^2+h_2\phi''(z_2))U\). The derivative of \(c\phi''(z_2)U\) contributes
\(-2r(h_2\phi''(z_2)U+c\phi'''(z_2)U^2+c\phi''(z_2)U_1)\). Hence

\[
\dot p_0=-2rp_1.
\]

With \(B_1=B[p_1]\), the next equations are

\[
\begin{aligned}
\dot B_0&=-2r(h_1E+B_1),& \dot D&=-4rE,\\
\dot V&=-2rV_1,
&V_1&=3Eh_1+\lambda_xDq_0+W_0^Tp_1+B_1.
\end{aligned}
\tag{9}
\]

The companion factor \(3\) in \(V_1\) arises from the two copies in \(\dot D\) and the one copy in \(\dot W_2^Tp_0\). Current aggregate derivatives also remain explicit:

\[
\begin{aligned}
\dot C&=-2r\bigl(\lambda_x\langle q_0^2\rangle
                             +\langle h_1,q_1\rangle\bigr),\\
\dot E&=-2r\bigl(\langle p_0^2\rangle
                             +\langle\delta_2,p_1\rangle\bigr).
\end{aligned}
\tag{10}
\]

Equations (1), (5)--(10) show concretely how successive current actions enter. In particular, even \(p_0\) contains the full labeled vector \(W_0q_0\), and the next level contains \(W_0q_1\) and \(W_0^Tp_1\).

## Exact hierarchy and collective particle form

The entire finite-width network is a first-order collective ODE. On the one-sample reduced parameter state \(\theta=(z_1,c,W_2)\), write it as

\[
\dot\theta=-2rG(\theta),
\qquad
G(\theta)=\left(
\lambda_x\phi'(z_1)b_1,
h_2,
\delta_2h_1^T/n
\right).
\]

All quantities on the right are functions of the current \(\theta\); the components of \(W_1\) not acting on \(x\) are irrelevant to this fixed-sample reduction and do not evolve under the supplied flow. Define the directional derivative

\[
\mathscr Dg(\theta)=Dg(\theta)[G(\theta)]
\]

and recursively \(q_{k+1}=\mathscr Dq_k\), \(p_{k+1}=\mathscr Dp_k\). For smooth \(\phi\), every finite level is defined and

\[
\dot q_k=-2rq_{k+1},\qquad
\dot p_k=-2rp_{k+1}.
\]

No division by \(r\) is used; these identities remain valid at \(r=0\). For \(A_k=A[q_k]\), \(B_k=B[p_k]\), equation (3) becomes

\[
\begin{aligned}
\dot A_k&=-2r\bigl(\delta_2\langle h_1,q_k\rangle+A_{k+1}\bigr),\\
\dot B_k&=-2r\bigl(h_1\langle\delta_2,p_k\rangle+B_{k+1}\bigr).
\end{aligned}
\tag{11}
\]

One can recursively expand each source by differentiating the already displayed current formulas, substituting (1), (3), and (4). Every fixed component of this generated hierarchy depends on finitely many other current fields. The directional-derivative definition is an exact definition on the original parameter space; it is not by itself a proof that an arbitrarily truncated coordinate list reconstructs that parameter space or closes its dynamics.

For example, pair lower- and upper-layer labels by the common index \(i\in\{1,\ldots,n\}\) and let a retained particle state contain

\[
S_i=(z_{1,i},z_{2,i},c_i,b_{1,i},A_{0,i},B_{0,i},\ldots).
\]

The first lines of its collective vector field are explicitly

\[
\begin{aligned}
\dot z_{1,i}&=-2r\lambda_x\phi'(z_{1,i})b_{1,i},\\
\dot z_{2,i}&=-2r\left[H\delta_{2,i}
 +\lambda_x\left(\sum_jW_{0,ij}q_{0,j}+A_{0,i}\right)\right],\\
\dot c_i&=-2rh_{2,i},\\
\dot b_{1,i}&=-2r\left[Dh_{1,i}
 +\sum_jW_{0,ji}p_{0,j}+B_{0,i}\right],\\
\dot A_{0,i}&=-2r(\delta_{2,i}C+A_{1,i}),\\
\dot B_{0,i}&=-2r(h_{1,i}E+B_{1,i}).
\end{aligned}
\tag{12}
\]

Here \(H,D,C,E\), and \(r=n^{-1}\sum_i c_i\phi(z_{2,i})-y\) are recomputed from the current population. Thus the right form is a collective law \(\dot S_i=F_i(S_1,\ldots,S_n;W_0,x,y)\), with retained fixed-map mixing. It need not be a function of only \(S_i\) and a short list of scalar marginal moments. If \(r\) is also carried as a state variable, it must initially equal the displayed output residual; equation (2) preserves this equality along the realizable hierarchy.

## What is and is not closed

All action coordinates initially vanish, since \(\Delta W(0)=0\), even though their input vectors need not vanish. The base initialization is

\[
z_2(0)=W_0\phi(z_1(0)),
\qquad
b_1(0)=W_0^T\bigl(c(0)\phi'(z_2(0))\bigr).
\]

The source vectors at initialization are obtained recursively from these data and \(W_0\), rather than from a target trajectory. Independently chosen action coordinates need not be realizable: for example the adjoint identity

\[
\langle p,A[q]\rangle=\langle B[p],q\rangle
\]

must hold whenever both actions are represented. The derivation establishes exactness for coordinates induced by the original network; it does not establish well-posedness or uniqueness of a stand-alone infinite hierarchy for arbitrary coordinate data.

A finite truncation needs an additional statement giving the omitted actions, for example \(A_{m+1},B_{m+1}\), as specified functions of the retained collective state, or an approximation theorem controlling their replacement. Zeroing an omitted action is an approximation. Neither (11) nor the fact that the original system is first order proves such a closure with a width-independent number of coordinates per particle.

There is always a tautological finite representation using the actions on every fixed coordinate vector \(e_j\): the \(n\) vectors \(A[e_j]\) store all columns of \(\Delta W\) and obey

\[
\frac{d}{dt}A[e_j]=-\frac{2r}{n}\delta_2h_{1,j}.
\]

That representation has \(n^2\) scalar entries and therefore does not establish the desired width-independent action count. Conversely, existence of some finite particle-state closure would not, without a separate argument, imply that \(\Delta W\) has low rank or admits a fixed separable factorization. No such implication is used here.

No pair kernel is required to write the exact action identities or collective laws (1)--(12). The open issue for a compressed description is finite closure, initialization, and controlled error for retained actions. It is not a requirement that those actions first be represented by a factorization or pair kernel.

Only \(C^2\) regularity is used in (1)--(3); \(C^3\) suffices for the explicit sources through \(p_1\), and a smooth activation suffices for every finite level of the infinite hierarchy. These are identities on an existing solution interval, not a claim of global existence or uniform control in width or time.
