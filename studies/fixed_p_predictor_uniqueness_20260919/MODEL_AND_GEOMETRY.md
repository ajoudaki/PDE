# Exact closure model and local feature geometry

2026-09-19. Lead derivation from established docs/global_nonlinear.md,
C.4.7.10.B/C.1 and D.3. This study imports no other study's results.

## 1. Model and canonical information

Fix p=1, with the maintained dictionary construction in book part B.
Its raw lists are (1,tanh g1,tanh g2,tanh p1,tanh p2) and
(1,tanh xi1,tanh xi2), with the declared order and

 p_i=zeta_i+alpha tanh(g_i),  g~N(0,I2),
 zeta~N(0,tau I2) independent of g,  xi~N(0,v I2)

on the two separate populations. Here v=E tanh²(G),
tau=E tanh²(sqrt(v)G), alpha=E phi'(sqrt(v)G), phi=tanh.
Use eta=1/4096, L_l L_l^T=E[psi_l psi_l^T]+eta I,
b_l=L_l^-1 psi_l, and D=L_2^-1 C L_1^-T with C given by the complete
Gaussian contraction identity H3.1/H3.CS7. All these are fixed known
initialization integrals. The canonical state is w=g, M=D, c=0.
The book gives ||D||op<=2 and ||v -> b_l^T v||<=1.
Let B_l=ess sup |b_l|, which is finite and strictly positive.

For normalized circle inputs x, |x|=sqrt(2), use

\[
 a_h(x)=E_1[b_1\phi(w\cdot x/\sqrt2)],\quad
 H_h(x)=\phi(b_2^T M a_h(x)),\quad
 f_{h,c}(x)=E_2[cH_h(x)].                         \tag{1}
\]

Write h=(w,M), h0=(g,D), with physical hidden Hilbert norm
||h||²=||w||_(L2)²+||M||_F². The readout has its original L2 norm.
Thus S=(h,c) represents the same full state as the current joint laws
Gamma1=Law(b1,g,w), Gamma2=Law(b2,c), and M. The frozen marks retain
their complete correlations. Gradients and adjoints below always use
these physical metrics, including the actual finite M transpose.

Data consist of finitely many (x_i,y_i), y_i in {-1,+1}, positive
masses mu_i summing to one. Equal inputs must have equal labels,
and opposite inputs opposite labels. Merge those compatible constraints
with the corresponding sign changes and summed weights, leaving m
representatives distinct modulo antipodes. This does not change loss
because every represented predictor is odd in x.

Set Y_i=sqrt(mu_i)y_i and define the current linear readout operator

\[
 (A_h c)_i=\sqrt{\mu_i}E_2[cH_h(x_i)],\quad
 K_h=A_hA_h^*,\quad e=A_hc-Y,\quad L=|e|^2.        \tag{2}
\]

The symbol A_h is this finite-data readout operator, not the book's
uncompressed initialized interlayer Gaussian action. Since |H|<=1,
||A_h||op<=1 and |Y|=1. K_h is an m-by-m matrix. Where K_h>0 define

\[
 B_h=A_h^*K_h^{-1},\quad P_h=I-B_hA_h,\quad
 c_*(h)=B_hY,\quad J(h)=\tfrac12Y^TK_h^{-1}Y.      \tag{3}
\]

AB=I. BA is selfadjoint and idempotent, so P is the orthogonal
projection onto ker A. Every c has the exact orthogonal decomposition

\[
 c=B_h(Y+e)+q,\qquad q=P_hc\in\ker A_h.           \tag{4}
\]

Consequently c_*(h) is the unique minimum-L2-norm readout fitting Y,
and J(h)=||c_*(h)||²/2. This is a current-state matrix solve using data;
it is not supplied by a future training endpoint.

## 2. Explicit regularity bounds in the physical Hilbert space

On ||h-h0||<=1, ||M||op<=3. The elementary inequalities
|phi|<=1, |phi'|<=1, |phi''|<=2 give

 |a_h(x)|<=B1,
 ||D_w a_h(x)||<=B1,
 Lip(D_w a_h(x))<=2 B1

uniformly on the normalized circle. Indeed the first derivative is
E1[b1 phi'(w·x/sqrt2)(v·x/sqrt2)]. Its linearization remainder is
bounded by B1||v||², and Cauchy--Schwarz bounds the difference of
two derivative operators by 2B1||w-w'||. Thus this is Frechet C1
with Lipschitz derivative into its finite-dimensional output; no
twice-Frechet-differentiable L2 Nemytskii assertion is needed.

For z_h(x)=b2^T M a_h(x), direct product subtraction gives

\[
 \|D_hz_h(x)\|_{E\to L^\infty}\le a_1:=4B_1B_2,
 \operatorname{Lip}(D_hz_h(x))\le a_2:=8B_1B_2.    \tag{5}
\]

For example Dz[v]=b2^T(v_M a+M Da[v_w]); differences are bounded
by B1B2(||delta w||||v_M||+||delta M||||v_w||
+6||delta w||||v_w||), at most a2||delta h||||v||.
The original derivative norm is at most B1B2(||v_M||+3||v_w||),
which is bounded by a1||v||. Composition with phi yields

\[
 \|D_hA_h\|\le a_1,\quad
 \operatorname{Lip}(D_hA_h)\le a_3:=2a_1^2+a_2,
 \|D_hK_h\|\le2a_1,\quad
 \operatorname{Lip}(D_hK_h)\le2a_3+2a_1^2.         \tag{6}
\]

The estimates for A follow by pairing each field derivative against c,
summing with weights mu_i, and using their sum one. For K=AA*, apply
the product rule and ||A||<=1. All constants are independent of the
noise, future trajectory, and particle approximations.

## 3. A certified positive-Gram neighborhood

Suppose sigma=lambda_min(K_h0)>0. CANONICAL_FEATURES.md will prove
this directly from the book for the stated canonical p=1 data.
The present estimates use that numerical positive value as an input.
Define

\[
 r=\min\{1/2,\sigma/(8a_1)\}>0.                  \tag{7}
\]

For ||h-h0||<=2r, (6) gives
||K_h-K_h0||<=4a1 r<=sigma/2, hence K_h>=sigma I/2.
In particular ||K_h^-1||<=2/sigma. Inverse subtraction gives

\[
 \operatorname{Lip}(K^{-1})\le8a_1/\sigma^2.
\]

Since DJ[v]=-(K^-1Y)^T DK[v](K^-1Y)/2, one obtains

\[
 \|\nabla J\|\le4a_1/\sigma^2,\quad
 \operatorname{Lip}(\nabla J)\le
 C_J:=\frac{32a_1^2}{\sigma^3}
       +\frac{4(a_3+a_1^2)}{\sigma^2}.            \tag{8}
\]

For the second estimate subtract the two inverse-weighted vectors,
each bounded by 2/sigma, and DK, using (6). The vector difference
contribution is at most
(1/2)(8a1/sigma²)(4/sigma)(2a1)=32a1²/sigma³;
the DK difference contributes 4(a3+a1²)/sigma².

B=A*K^-1 and P=I-BA are C1 with locally Lipschitz derivatives there.
In particular

\[
 \|B_h\|\le\sqrt{2/\sigma},\quad
 \operatorname{Lip}(B)\le
 C_B:=2a_1/\sigma+8a_1/\sigma^2.                 \tag{9}
\]

The first estimate follows from B*B=K^-1. The second follows by
subtracting the two factors, using (6) and inverse subtraction.
Products and differentiation of the finite inverse prove the stated
derivative Lipschitz property, with finite constants on this ball.

## 4. Current-state gradients retain both interaction directions

Let z=K^-1Y and c_*=A*z. Then the preceding differential may be
written DJ[v]=-<c_*,DA[v]*z>. In particular it differentiates the
first-layer gate, the true middle matrix, and the second-layer gate.
For a variation v_M, delta H_i=phi'(b2^TMa_i)b2^T v_M a_i;
for v_w, replace v_M a_i by M E1[b1 phi'(w·x_i/sqrt2)
(v_w·x_i/sqrt2)]. Pairing against c_* and z_i sqrt(mu_i)
gives the full hidden gradient. Its lower adjoint contains M^T,
not an independent backward action. The optimization construction
using J therefore changes both hidden blocks through current
data-dependent interactions; it does not replace their feature maps
by frozen initial activations.

The new optimizer is nevertheless a changed training rule. Its
selection objective and transport equations require separate proofs;
none follows merely from the original loss energy identity.
