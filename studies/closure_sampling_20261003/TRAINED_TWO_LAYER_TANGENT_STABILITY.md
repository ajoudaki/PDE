# Closing both trained tangent gates after integration over learning activity

2026-10-04. Coordinator continuation of TRAINED_NORMALIZED_RESPONSE_ROUTE.md,
read completely and reconstructed before use. That source is frozen at
SHA-256 4784c003ae8e449b945939d38fae4fea188d816f264d4f60c927f10a70bdd923.
This result is about the actual trained finite network. It is restricted to
input derivatives at the training input, in directions perpendicular to it;
it is not a whole-query compression theorem. No experiment is used.

The useful distinction is between the supremum of a mixed product and its
integral over the finite amount of learning activity. For the latter,
conditioning on the training trajectory leaves one independent Gaussian
matrix. A direct Frobenius calculation closes both tangent gates, including
the top gate that remains open at arbitrary queries in the preceding note.

## 1. Network and fully specified event

There are two hidden layers, each of width n, one unit training input e_1,
and one label y, with Y=|y|. Let d>=2. The equations are

\[
 h^{(1)}(v)=\phi(Av),\quad z^{(2)}(v)=Wh^{(1)}(v),\quad
 h^{(2)}(v)=\phi(z^{(2)}(v)),\quad f(v)=w^\top h^{(2)}(v)/n.
\]

Initialization has independent entries A_ij~N(0,1), W_ij~N(0,1/n),
independent blocks, and w(0)=0. Training minimizes (f(e_1)-y)^2 with
mobilities (n,1,n). Choose

\[
 b_0=\sqrt{1-\pi/(2\sqrt3)},\qquad
 \phi(z)=b_0+\sqrt{\pi\sqrt3/2}\operatorname{erf}(z/\sqrt2).
\]

Define the real-axis bounds and constants

\[
 B=b_0+\sqrt{\pi\sqrt3/2},\quad S=3^{1/4},\quad T=S e^{-1/2},
 \quad K=9,\quad C_2=B^2+K^2S^2,
\]
\[
 c=\min\{1,(16SB^2)^{-1/2},(64S^2BC_2)^{-1/2}\}.
 \tag{1}
\]

Thus |phi|<=B, |phi'|<=S, |phi''|<=T on the real line. Assume
0<Y<=c and the initialized event

\[
 \|W(0)\|_{\rm op}\le8,\qquad
 \|h^{(2)}(0,e_1)\|_{2,n}\ge1/\sqrt2.
 \tag{2}
\]

Here ||u||_(2,n)=||u||_2/sqrt(n). Event (2) depends only on the training
initialization and has probability tending to one at each fixed d.
The complete elementary fitting bootstrap in the input note proves

\[
 |f(t,e_1)-y|\le Y e^{-t/2},\qquad
 \tau(t)=2\int_0^t|f(s,e_1)-y|\,ds\le4Y,
 \quad\|W(t)\|_{\rm op}\le K.
 \tag{3}
\]

All parameters converge. For y>0, a prime in what follows denotes d/dtau;
for y<0 change w to -w, which leaves all hidden trajectories and estimates
unchanged. Write A=[a,G], where a=Ae_1. The matrix G of the other columns
is constant and independent of the entire training trajectory (a,W,w).
The source proves directly from the trained equations that

\[
 \|a'\|_{2,n}\le KS^2B\tau,\quad
 \|(z^{(2)}(e_1))'\|_{2,n}\le SBC_2\tau,\quad
 \|W'\|_F\le SB^2\tau.
 \tag{4}
\]

For clarity, W'=delta h^(1)(e_1)^top/n, delta=phi'(z^(2)(e_1))w,
w'=h^(2)(e_1), and a'=phi'(a) W^top delta. These identities also verify
the normalizations in (4).

## 2. The actual feature tangent is a conditionally Gaussian linear map

Let u be a real unit vector perpendicular to e_1, represented by its
d-1 transverse coordinates. At the training input the directional
derivative of the top hidden feature is exactly

\[
 J(t,u)=D_vh^{(2)}(t,e_1)[u]=P(t)G u,
 \quad P=D_2WD_1,
 \quad D_1=\operatorname{diag}(\phi'(a)),\quad
 D_2=\operatorname{diag}(\phi'(z^{(2)}(e_1))).
 \tag{5}
\]

The entire matrix curve P is determined by (a(0),W(0),y), hence is
independent of G. This independence concerns derivatives at e_1. At a
general query the gates themselves depend on G, so (5) would not have
the same conditional interpretation.

Differentiate the actual curve:

\[
 P'=\operatorname{diag}(\phi''(z^{(2)})(z^{(2)})')WD_1
       +D_2W'D_1
       +D_2W\operatorname{diag}(\phi''(a)a').
 \tag{6}
\]

Every term has an explicit normalized Frobenius bound without a neuron
maximum. For any vector q, the row and column Euclidean norms of W are
at most K, so

\[
 \|\operatorname{diag}(q)W\|_F/\sqrt n\le K\|q\|_{2,n},
 \qquad
 \|W\operatorname{diag}(q)\|_F/\sqrt n\le K\|q\|_{2,n}.
\]

Consequently (4)--(6) give

\[
 \|P'\|_F/\sqrt n\le D_P\tau,
 \quad
 D_P=KTS^2BC_2+K^2TS^3B+S^3B^2.
 \tag{7}
\]

The middle term in (6) actually contributes S^3B^2 tau/sqrt(n),
which is bounded by the last term retained in D_P. The first and third
terms use only the actual RMS velocities in (4). In particular no
fourth moment of a reused backward carrier is assumed in (7).

## 3. Time-uniform tangent preservation

Conditional on any training initialization satisfying (2), for every
0<delta<1, with probability at least 1-delta over G,

\[
 \sup_{t\in[0,\infty]}\sup_{\substack{u\perp e_1\\\|u\|=1}}
 \|J(t,u)-J(0,u)\|_{2,n}
 \le 8D_P\sqrt{\frac{d-1}{\delta}}\,Y^2.
 \tag{8}
\]

Proof: for each fixed real n by n matrix M, Gaussian second moments give

\[
 \mathbb E_G\|MG\|_F^2/n=(d-1)\|M\|_F^2/n.
 \tag{9}
\]

The fundamental theorem of calculus gives
sup_tau ||[P(tau)-P(0)]G||_F/sqrt(n)
<=int_0^(tau(infinity)) ||P'(tau)G||_F/sqrt(n) d tau.
Minkowski in conditional L2(G), (7), (9), and tau(infinity)<=4Y bound
the L2 norm of this right side by
sqrt(d-1) D_P (4Y)^2/2. Markov's inequality for its square proves
(8), since the operator norm in the supremum over u is no larger than
the Frobenius norm. This also proves the endpoint claim. The overall
probability is at least 1-delta-o_n(1), and its coefficient has no width
or physical-time dependence.

For a direct statement about the previously problematic top gate, put
R^(2)(e_1)=(z^(2)(e_1))' in the residual clock. Define

\[
 I=\int_0^{\tau(\infty)}
 \sup_{\substack{u\perp e_1\\\|u\|=1}}
 \|\phi''(z^{(2)})\odot R^{(2)}(e_1)
        \odot [WD_1G u]\|_{2,n}\,d\tau.
\]

Applying (9) to the first matrix term of (6), rather than to their sum,
proves on an event of the same conditional probability

\[
 I\le8KTS^2BC_2\sqrt{\frac{d-1}{\delta}}\,Y^2.
 \tag{10}
\]

Because d tau=2|f(e_1)-y|dt, (10) is precisely an estimate integrated
against physical training activity. It does not assert a time-uniform
supremum of the unweighted product. The two claims (8) and (10) each
have confidence 1-delta; for both simultaneously replace delta by
delta/2 in their right sides and take a union bound.

## 4. What this resolves and what it leaves open

The upper mixed product at the observed input can be controlled in the
norm needed to bound the accumulated change of the transverse tangent.
It is not necessary to differentiate R^(2), to bound every neuron, or
to assume the trained gates remain Gaussian. Both nonlinear hidden
layers really train; their dependence on the unchanged random transverse
matrix is isolated exactly by (5).

This closes more than an initialized calculation, but less than the
compression theorem. It controls first input derivatives at one observed
point, not arbitrary unseen inputs, higher derivatives, or the full
source approximation. The loss-integrated norm in (10) cannot be silently
replaced by a stronger time supremum. The dependence on arbitrary depth
and multiple inputs has not been proved here. Neither (8) nor (10) gives
the requested new label/error/storage triple for an autonomous compressor.
