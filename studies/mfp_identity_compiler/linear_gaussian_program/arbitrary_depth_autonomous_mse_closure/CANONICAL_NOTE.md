# Arbitrary-depth linear \(\mu\)P from one rooted-path source

> **Depth-three update, 20 August 2026.**  The positive-time width bridge for
> exactly three hidden layers is now proved by the cyclic trace-class and
> central free-Wishart constructions in
> `../depth3_unfrozen_readout_closure/`.  The conditional warning below remains
> current for the general statement at hidden depths greater than three.

Status: canonical self-contained formulation, 20 August 2026.  The exact
finite-width algebra and the deterministic path equation, including its
global behavior, are proved below.  For three or more hidden layers, the
identification of that equation with the finite-width network at positive
training times remains conditional on a multi-matrix Gaussian-word theorem.

## 1. Model, initialization, and gradient flow

There is one unit-normalized input

\[
x\in\mathbb R^d,
\qquad \|x\|=1,
\]

with scalar label \(y\).  The network has \(L\ge1\) hidden layers, all of
width \(n\):

\[
W_1\in\mathbb R^{n\times d},\qquad
W_\ell\in\mathbb R^{n\times n}\quad(2\le \ell\le L),
\qquad
W_{L+1}\in\mathbb R^{1\times n}.
\]

We work directly in \(\mu\)P-normalized coordinates:

\[
f_n(x)=W_{L+1}W_L\cdots W_1x.                              \tag{1.1}
\]

Every entry of every weight matrix is initially independent
\(N(0,1/n)\).  The full squared loss is

\[
\mathcal L_n=(y-f_n)^2,
\]

and normalized \(\mu\)P gradient flow is

\[
\frac{dW_\ell}{dt}
=-\eta\nabla_{W_\ell}\mathcal L_n
=2\eta(y-f_n)\nabla_{W_\ell}f_n.                           \tag{1.2}
\]

This is equivalent to standard-normal raw weights together with the
prefactor \(n^{-(L+1)/2}\).

More explicitly, if

\[
\widetilde W_\ell=\sqrt n\,W_\ell,
\]

then every entry of \(\widetilde W_\ell\) is standard normal and

\[
f_n=n^{-(L+1)/2}
\widetilde W_{L+1}\cdots\widetilde W_1x.
\]

The chain rule gives

\[
\nabla_{\widetilde W_\ell}\mathcal L_n
=n^{-1/2}\nabla_{W_\ell}\mathcal L_n,
\qquad
\frac{dW_\ell}{dt}
=n^{-1/2}\frac{d\widetilde W_\ell}{dt}.
\]

Hence the raw-coordinate flow

\[
\frac{d\widetilde W_\ell}{dt}
=-\eta n\nabla_{\widetilde W_\ell}\mathcal L_n
\]

is exactly (1.2).  No width factor has been discarded; it has been absorbed
into the coordinates.

To display the gradients, define the forward hidden vectors

\[
h_0=x,
\qquad
h_\ell=W_\ell h_{\ell-1}\in\mathbb R^n
\quad(1\le\ell\le L),                                     \tag{1.3}
\]

and the backward hidden vectors

\[
g_L=W_{L+1}^{\mathsf T},
\qquad
g_\ell=W_{\ell+1}^{\mathsf T}g_{\ell+1}\in\mathbb R^n
\quad(1\le\ell<L).                                        \tag{1.4}
\]

Then

\[
\nabla_{W_\ell}f_n=g_\ell h_{\ell-1}^{\mathsf T}
\quad(1\le\ell\le L),
\qquad
\nabla_{W_{L+1}}f_n=h_L^{\mathsf T}.                        \tag{1.5}
\]

Thus every layer equation is explicit:

\[
\frac{dW_\ell}{dt}
=2\eta(y-f_n)g_\ell h_{\ell-1}^{\mathsf T}
\quad(1\le\ell\le L),                                    \tag{1.6}
\]

\[
\frac{dW_{L+1}}{dt}
=2\eta(y-f_n)h_L^{\mathsf T}.                              \tag{1.7}
\]

At initialization, repeated conditioning on the independent Gaussian
layers gives

\[
\mathbb E\|h_\ell(0)\|^2=1
\quad(1\le\ell\le L),
\qquad
\mathbb E[f_n(0)]=0,
\qquad
\mathbb E[f_n(0)^2]=\frac1n.                               \tag{1.8}
\]

Consequently

\[
f_n(0)\xrightarrow{\mathbb P}0.                            \tag{1.9}
\]

## 2. One sample produces one geometric training path

Every equation in (1.6)--(1.7) contains the same scalar multiplier.  Define
feature time \(s\) along the trajectory by

\[
\frac{ds}{dt}=2\eta(y-f_n).                                \tag{2.1}
\]

In this clock,

\[
\frac{dW_\ell}{ds}=\nabla_{W_\ell}f_n.                    \tag{2.2}
\]

Equation (2.2) is understood wherever \(y-f_n\ne0\).  If the residual reaches
zero, physical gradient flow stops, so extending the same geometric curve in
feature time creates no ambiguity in the physical trajectory.

The label therefore controls the speed along one feature-learning path; it
does not change that path.  This reduction is exact because there is one
sample and hence only one output-gradient direction.  It does not generally
survive for several samples.

The input dimension can now be removed completely.  Put

\[
m=L-1,
\qquad
u_n=W_1x\in\mathbb R^n,
\qquad
v_n=W_{L+1}^{\mathsf T}\in\mathbb R^n,                    \tag{2.3}
\]

and, for the \(m\) middle matrices,

\[
V_{j,n}=W_{j+1}\in\mathbb R^{n\times n},
\qquad 1\le j\le m.                                       \tag{2.4}
\]

The empty middle product is understood when \(L=1\).  Define forward vectors

\[
a_{0,n}=u_n,
\qquad
a_{j,n}=V_{j,n}a_{j-1,n}\quad(1\le j\le m),              \tag{2.5}
\]

and backward vectors

\[
b_{m,n}=v_n,
\qquad
b_{j-1,n}=V_{j,n}^{\mathsf T}b_{j,n}\quad(1\le j\le m).  \tag{2.6}
\]

The output is

\[
f_n=v_n^{\mathsf T}a_{m,n}.                                \tag{2.7}
\]

Using \(\|x\|=1\) in the first-layer equation, the exact feature-time system
becomes

\[
\boxed{
\begin{aligned}
\frac{du_n}{ds}&=b_{0,n},\\
\frac{dv_n}{ds}&=a_{m,n},\\
\frac{dV_{j,n}}{ds}&=b_{j,n}a_{j-1,n}^{\mathsf T},
\qquad 1\le j\le m.
\end{aligned}}                                             \tag{2.8}
\]

This short chain contains the entire one-sample network.

## 3. The exact output kernel at arbitrary depth

Differentiate (2.7) along (2.8).  The change of the output endpoint gives
\(\|a_{m,n}\|^2\), the change of the input endpoint gives
\(\|b_{0,n}\|^2\), and the change of the \(j\)th middle matrix gives

\[
b_{j,n}^{\mathsf T}
\left(b_{j,n}a_{j-1,n}^{\mathsf T}\right)a_{j-1,n}
=\|b_{j,n}\|^2\|a_{j-1,n}\|^2.
\]

Therefore

\[
\frac{df_n}{ds}=K_n,                                      \tag{3.1}
\]

where

\[
\boxed{
K_n=
\|b_{0,n}\|^2+\|a_{m,n}\|^2
+\sum_{j=1}^m\|b_{j,n}\|^2\|a_{j-1,n}\|^2.}              \tag{3.2}
\]

This is also the squared norm of the complete output gradient:

\[
K_n=\sum_{\ell=1}^{L+1}\|\nabla_{W_\ell}f_n\|_F^2.       \tag{3.3}
\]

Returning to physical time and writing

\[
e_n=y-f_n,
\]

we obtain the exact scalar relations

\[
\frac{df_n}{dt}=2\eta e_nK_n,
\qquad
\frac{de_n}{dt}=-2\eta e_nK_n,                            \tag{3.4}
\]

and hence

\[
\frac{d\mathcal L_n}{dt}=-4\eta K_n\mathcal L_n.          \tag{3.5}
\]

At Gaussian initialization every forward and backward norm in (3.2)
converges to one.  Since there are two endpoint terms and \(m=L-1\) middle
terms,

\[
K_n(0)\xrightarrow{\mathbb P}L+1.                          \tag{3.6}
\]

## 4. Why the depth-two scalar spectrum does not directly generalize

The feature flow has exact balancedness invariants at every interface.
Regard the reduced chain as the \(L+1\) linear maps

\[
\Theta_0=u_n:\mathbb R\to\mathbb R^n,
\qquad
\Theta_j=V_{j,n}:\mathbb R^n\to\mathbb R^n
\quad(1\le j\le m),
\]

\[
\Theta_{m+1}=v_n^{\mathsf T}:\mathbb R^n\to\mathbb R.
\]

For \(0\le j\le m\), both matrices in

\[
C_{j,n}=\Theta_j\Theta_j^{\mathsf T}
-\Theta_{j+1}^{\mathsf T}\Theta_{j+1}                     \tag{4.1}
\]

act on the same \(j\)th hidden space.  Along feature flow,

\[
\frac d{ds}(\Theta_j\Theta_j^{\mathsf T})
=b_{j,n}a_{j,n}^{\mathsf T}
+a_{j,n}b_{j,n}^{\mathsf T},                              \tag{4.2}
\]

while

\[
\frac d{ds}(\Theta_{j+1}^{\mathsf T}\Theta_{j+1})
=a_{j,n}b_{j,n}^{\mathsf T}
+b_{j,n}a_{j,n}^{\mathsf T}.                              \tag{4.3}
\]

The derivatives are identical, so

\[
\frac{dC_{j,n}}{ds}=0.                                     \tag{4.4}
\]

With two hidden layers there is only one middle random matrix.  The endpoint
relations then collapse the dynamics to one second-order vector equation
driven by one fixed symmetric matrix, which can be diagonalized by the
ordinary spectral theorem.

At three or more hidden layers, products contain several independent
nonnormal matrices and their transposes.  The conserved matrices (4.1) live
at different hidden grades and do not supply a common eigenbasis.  Mixed
words such as

\[
V_{2,n}V_{1,n}V_{1,n}^{\mathsf T}V_{2,n}^{\mathsf T}
\]

depend on the order of the factors, not only on the separate spectra.
Consequently the direct depth-two strategy of replacing everything by one
scalar eigenvalue \(\lambda\) loses information.

This rules out that direct simultaneous-diagonalization route.  It is not a
proof that no other scalar encoding could ever be invented.

## 5. Gaussian matrix products become paths

The appropriate fixed source records words rather than eigenvalues.
Consider the chain of middle-layer locations

\[
0--1--\cdots--m.                                           \tag{5.1}
\]

There are two roots: an input root at location \(0\), representing \(u_n(0)\),
and an output root at location \(m\), representing \(v_n(0)\).  A path is a
finite nearest-neighbor walk on (5.1) that starts at either root.  Explicitly,

\[
\gamma=(\sigma;s_0,s_1,\ldots,s_r),
\qquad
\sigma\in\{\mathrm{in},\mathrm{out}\},                   \tag{5.2}
\]

where \(s_0=0\) for the input root, \(s_0=m\) for the output root,
\(|s_k-s_{k-1}|=1\), and \(|\gamma|:=r\).  Let

\[
\mathcal P_j=\{\text{rooted finite paths ending at location }j\},
\qquad
\mathcal H_j=\ell^2(\mathcal P_j).                         \tag{5.3}
\]

The two roots are given different labels, so they remain distinct when
\(m=0\).  These paths are bookkeeping labels for centered Gaussian matrix
words.  They are not neuron trajectories, training trajectories, or points
of a probability space.  Arbitrarily long paths are needed even though the
network has finite depth because training repeatedly multiplies existing
words by initialized matrices and their transposes.

For \(\gamma\in\mathcal P_j\), let \(e_\gamma\) be the corresponding unit
basis vector.

For each edge \(j=1,\ldots,m\), define a fixed operator

\[
\Lambda_j:\mathcal H_{j-1}\longrightarrow\mathcal H_j.    \tag{5.4}
\]

If \(\gamma\) ends at \(j-1\), then

\[
\boxed{
\Lambda_je_\gamma
=e_{\gamma\cdot j}
+\mathbf 1_{\{\gamma=(\ldots,j,j-1)\}}e_{\gamma^-}.}      \tag{5.5}
\]

Here \(\gamma\mathbin\cdot j\) appends the new location \(j\), whereas
\(\gamma^-\) removes the final location.  The first term creates a longer
Gaussian word.  The second term
appears only when the path has just traversed the same matrix in the reverse
direction; it is the Gaussian contraction that erases this immediate
backtrack.

For example,

\[
\Lambda_1e_{(\mathrm{in};0,1,0)}
=e_{(\mathrm{in};0,1,0,1)}+e_{(\mathrm{in};0,1)}.          \tag{5.6}
\]

Creation and annihilation each have norm one, so

\[
\|\Lambda_j\|\le2.                                        \tag{5.7}
\]

The adjoint performs the same operation in the reverse layer direction.
Let

\[
\mathcal H=\bigoplus_{k=0}^m\mathcal H_k,
\]

and let \(\iota_j:\mathcal H_j\hookrightarrow\mathcal H\) be the canonical
inclusion.  The two distinguished roots together with the single block
operator

\[
\boxed{
\Lambda=
\sum_{j=1}^m\iota_j\Lambda_j\iota_{j-1}^*}                \tag{5.8}
\]

are the fixed rooted-path source.

## 6. The Gaussian-word bridge that is still required

Write the initialized middle matrices as

\[
V_{j,n}(0)=\frac1{\sqrt n}Z_{j,n},                         \tag{6.1}
\]

where the matrices \(Z_{j,n}\) have independent standard-normal entries.  A
finite path formally specifies a product of these matrices and transposes
applied to one of the two Gaussian endpoint vectors.  Restricting the
layer--neuron pairs to be distinct removes collision terms and produces the
loopless Gaussian words underlying the path basis.

To turn this formal correspondence into a width-limit theorem, one needs a
multi-edge rooted-word lemma.  Its normalization can be stated explicitly.
Write the two endpoint vectors as \(g^{\rm in}/\sqrt n\) and
\(g^{\rm out}/\sqrt n\), and let \(g^\sigma\) mean the vector selected by
the root color \(\sigma\).  If

\[
\gamma=(\sigma;s_0,s_1,\ldots,s_r)
\]

is a rooted path ending at layer \(j\), set \(i_r=i\) and define

\[
\begin{aligned}
(J_{j,n}e_\gamma)_i
={}&n^{-(r+1)/2}
\sum_{\substack{i_0,\ldots,i_{r-1}\\
(s_k,i_k)_{0\le k\le r}\ \text{pairwise distinct}}}
g^\sigma_{i_0}
\prod_{k=1}^r
(Z_{s_k,s_{k-1}})_{i_ki_{k-1}},                         \tag{6.2}
\end{aligned}
\]

where \(Z_{j,j-1}=Z_{j,n}\) and
\(Z_{j-1,j}=Z_{j,n}^{\mathsf T}\).  The distinctness condition removes
neuron-index loops; every \(i_k\) ranges over \(\{1,\ldots,n\}\), including
the fixed terminal index \(i_r\).

For every fixed path cutoff \(R\), the required lemma is that these maps,
restricted to the finite spans \(|\gamma|\le R\), satisfy the Gram estimate
below.  For the two action estimates, the target span is enlarged to cutoff
\(R+1\).

\[
\mathbb E\left|
\langle J_{j,n}e_\gamma,J_{j,n}e_{\gamma'}\rangle
-\delta_{\gamma\gamma'}
\right|^2
\le \frac{C_{L,R}}n.                                      \tag{6.3}
\]

Multiplication by an initialized matrix or its transpose must also obey

\[
\begin{aligned}
\mathbb E\left\|
V_{j,n}(0)J_{j-1,n}e_\gamma
-J_{j,n}\Lambda_je_\gamma
\right\|^2
&\le \frac{C_{L,R}}n,\\
\mathbb E\left\|
V_{j,n}(0)^{\mathsf T}J_{j,n}e_\gamma
-J_{j-1,n}\Lambda_j^*e_\gamma
\right\|^2
&\le \frac{C_{L,R}}n.                                    \tag{6.4}
\end{aligned}
\]

Because a truncated span has fixed finite dimension, these estimates would
also give operator-norm convergence in probability on that span.

The expected mechanism is clear: the leading Wick pairing matches a colored
path with itself; a different pairing forces an additional neuron-index
collision and loses a power of \(n\).  Multiplication by one more Gaussian
matrix either creates a new final edge or contracts the immediately reversed
edge.  This is exactly the rule (5.5).

For example, the identity-pairing contribution to a diagonal Gram mean is

\[
\prod_{\ell=0}^m
\frac{(n)_{N_\ell(\gamma)}}{n^{N_\ell(\gamma)}}
=1+O(n^{-1}),                                             \tag{6.5}
\]

where \((n)_k=n(n-1)\cdots(n-k+1)\), and
\(N_\ell(\gamma)\) counts every visit to layer \(\ell\), including the
initial and terminal vertices.  The desired off-diagonal mean is
\(O_{L,R}(n^{-1})\); proving that statement uniformly over a fixed truncation
is part of the rooted-word lemma.  These first moments are not enough.  A
complete proof must count the paired products that determine the variance
and show that every non-diagonal surviving diagram loses at least one free
neuron index.  It must also prove both action estimates in (6.4).

Positive training time additionally requires a compatible lift of each
trained block,

\[
G_j\longmapsto J_{j,n}G_jJ_{j-1,n}^{\mathsf T},           \tag{6.6}
\]

together with control of components leaking outside each truncated path
span.

For one middle matrix, the rigorous one-edge \(\ell^2\) construction and the
scalar spectral construction in the supplied two-hidden-layer note give a
rigorous positive-time limit.  For two or more middle matrices,
(6.3)--(6.6) are
plausible and supported by fixed-order computations, but they have not been
proved in the present manuscript or in the cited published source.

## 7. The deterministic rooted-path feature flow

The endpoint vectors become evolving Hilbert vectors

\[
u(s)\in\mathcal H_0,
\qquad
v(s)\in\mathcal H_m.                                      \tag{7.1}
\]

The trained change of the \(j\)th middle matrix becomes a Hilbert--Schmidt
operator

\[
G_j(s):\mathcal H_{j-1}\longrightarrow\mathcal H_j,        \tag{7.2}
\]

initialized at zero.  The full effective middle operator is

\[
T_j(s)=\Lambda_j+G_j(s).                                   \tag{7.3}
\]

Hilbert--Schmidt means that the matrix of \(G_j\) in the path bases has
square-summable entries.  Such an operator is bounded, and the rank-one
right-hand side below is Hilbert--Schmidt.

Define the path forward vectors

\[
a_0=u,
\qquad
a_j=T_ja_{j-1}\quad(1\le j\le m),                        \tag{7.4}
\]

and backward vectors

\[
b_m=v,
\qquad
b_{j-1}=T_j^*b_j\quad(1\le j\le m).                     \tag{7.5}
\]

The output is

\[
f=\langle v,a_m\rangle.                                    \tag{7.6}
\]

As a function of \(u,v,G_1,\ldots,G_m\), its gradients are

\[
\nabla_u f=b_0,
\qquad
\nabla_v f=a_m,
\qquad
\nabla_{G_j}f=b_j\otimes a_{j-1}.
\]

The following autonomous equation is the candidate width limit.
Independently of that identification, it is a well-defined deterministic
Hilbert-space flow:

\[
\boxed{
\begin{aligned}
\frac{du}{ds}&=b_0,\\
\frac{dv}{ds}&=a_m,\\
\frac{dG_j}{ds}&=b_j\otimes a_{j-1},
\qquad 1\le j\le m.
\end{aligned}}                                             \tag{7.7}
\]

The rank-one operator in the last line acts by

\[
(b_j\otimes a_{j-1})z
=b_j\langle a_{j-1},z\rangle.                              \tag{7.8}
\]

Differentiate (7.6).  The two endpoint derivatives and the \(m\) operator
derivatives give

\[
\frac{df}{ds}=K,                                           \tag{7.9}
\]

where

\[
\boxed{
K=
\|b_0\|^2+\|a_m\|^2
+\sum_{j=1}^m\|b_j\|^2\|a_{j-1}\|^2.}                    \tag{7.10}
\]

Thus the path equation has exactly the same forward--backward form as the
finite network.

Let \(\alpha\in\mathcal H_0\) and \(\beta\in\mathcal H_m\) denote the input
and output root basis vectors.  The initialization is

\[
u(0)=\alpha,
\qquad
v(0)=\beta,
\qquad
G_j(0)=0.                                                   \tag{7.11}
\]

The two rooted channels are orthogonal, so \(f(0)=0\).  The unique monotone
path from each endpoint has unit norm at every intermediate location.  Hence

\[
K(0)=L+1.                                                   \tag{7.12}
\]

## 8. The autonomous physical-time equation

Define the residual

\[
e(t)=y-f(t).                                                \tag{8.1}
\]

Multiplying the feature vector field (7.7) by the scalar clock speed
\(2\eta e\) gives the complete physical-time system:

\[
\boxed{
\begin{aligned}
\frac{du}{dt}&=2\eta e\,b_0,\\
\frac{dv}{dt}&=2\eta e\,a_m,\\
\frac{dG_j}{dt}&=2\eta e\,b_j\otimes a_{j-1},
\qquad 1\le j\le m,\\
\frac{de}{dt}&=-2\eta eK.
\end{aligned}}                                             \tag{8.2}
\]

Together with (7.3)--(7.5) and (7.10), this is closed and autonomous.  The
initial residual is

\[
e(0)=y.                                                     \tag{8.3}
\]

The output and loss require no additional variables:

\[
f(t)=y-e(t)=\langle v(t),a_m(t)\rangle,
\qquad
\mathcal L(t)=e(t)^2.                                      \tag{8.4}
\]

Indeed, differentiating the Hilbert-space output gives

\[
\frac{df}{dt}=2\eta eK=-\frac{de}{dt},                     \tag{8.5}
\]

and both expressions for \(f\) are initially zero.  Therefore

\[
\frac{d\mathcal L}{dt}=-4\eta K\mathcal L.                 \tag{8.6}
\]

This is also an integro-differential equation.  With counting measure on the
path sets and kernels

\[
T_j(\gamma,\gamma')=\Lambda_j(\gamma,\gamma')
+G_j(\gamma,\gamma'),
\]

the forward recursion, backward recursion, and trainable-kernel equation are

\[
\begin{aligned}
a_j(\gamma)
&=\int_{\mathcal P_{j-1}}
T_j(\gamma,\gamma')a_{j-1}(\gamma')\,d\#(\gamma'),\\
b_{j-1}(\gamma')
&=\int_{\mathcal P_j}
T_j(\gamma,\gamma')b_j(\gamma)\,d\#(\gamma),\\
\frac{\partial G_j}{\partial t}(\gamma,\gamma')
&=2\eta e\,b_j(\gamma)a_{j-1}(\gamma').                  \tag{8.7}
\end{aligned}
\]

Here \(\#\) is counting measure: each integral is a convergent sum over paths.
The present values of \(u\), \(v\), the kernels \(G_j\), and \(e\), together
with the fixed source \(\Lambda\), determine every future derivative.  No past
trajectory or growing moment list is required.

## 9. The conditional positive-time theorem

The desired finite-width statement is the following.  For fixed hidden depth
\(L\) and finite physical horizon \(T\),

\[
\sup_{0\le t\le T}
\left(
|f_n(t)-f(t)|
+|K_n(t)-K(t)|
+|(y-f_n(t))^2-e(t)^2|
\right)
\xrightarrow{\mathbb P}0.                                 \tag{9.1}
\]

For \(L=1\), this follows directly from the two-vector system.  For \(L=2\),
the rigorous one-edge \(\ell^2\) theorem identifies the path readout, while
the scalar spectral closure in the supplied note gives its equivalent
output--kernel description.
For \(L\ge3\), (9.1) is presently conditional, not proved.

Here is the precise proof architecture.  Loss dissipation already gives the
needed dimension-free finite-time bound.  Define the trained increments

\[
H_{j,n}(t)=V_{j,n}(t)-V_{j,n}(0).
\]

The shifted finite state is

\[
(u_n,v_n,H_{1,n},\ldots,H_{m,n},e_n).
\]

Use Euclidean norms on the endpoint vectors and Frobenius norms on the
increments.  If \(X\) is an endpoint vector or one increment \(H_{j,n}\),
and \(K_X\) is its nonnegative contribution to \(K_n\), then

\[
\begin{aligned}
\|X(t)-X(0)\|
&\le2\eta\int_0^t|e_n|\sqrt{K_X}\,d\tau\\
&\le|e_n(0)|\sqrt{\eta t},                                \tag{9.2}
\end{aligned}
\]

because

\[
\frac d{dt}e_n^2=-4\eta e_n^2K_n.                          \tag{9.3}
\]

Indeed,

\[
(2\eta)^2\int_0^t e_n(\tau)^2K_n(\tau)\,d\tau
=\eta\bigl[e_n(0)^2-e_n(t)^2\bigr],
\]

and Cauchy--Schwarz gives (9.2).

The unshifted initialized matrices have Frobenius norm of order \(\sqrt n\),
so they are not part of this bounded state.  Instead, on the high-probability
event where their operator norms, the endpoint norms, and \(|e_n(0)|\) are
bounded, they enter the shifted vector field as bounded fixed coefficients.
Equation (9.2) then places the shifted finite state and the path state in a
common deterministic ball.  Cut both vector fields off just outside that
ball.  They have a common bound \(M\) and Lipschitz constant \(H\), independent
of width.  Their Picard remainders obey

\[
\sup_{0\le t\le T}\|x(t)-x^{[r]}(t)\|
\le MT e^{HT}\frac{(HT)^r}{(r+1)!}.                       \tag{9.4}
\]

Every fixed Picard iterate has finite path support.  Therefore, if the
rooted-word estimates (6.3)--(6.4) and the lift consistency based on (6.6)
are proved, the finite and path Picard iterates converge after lifting.
Choose \(r\) first, then send \(n\to\infty\), and finally let \(r\to\infty\).
The energy bound shows that the cutoff never activates, while continuity of
the output and kernel gives (9.1).  No restart is needed.

The missing work is substantive: it includes the multi-edge Wick estimates,
the matrix-increment lift and leakage bounds, the varying-Hilbert-space
Picard comparison, and the lifted output and kernel estimates.  Thus (9.1)
is a clear conditional theorem and research target, not a consequence of the
currently written two-paragraph argument.

## 10. Global behavior of the deterministic path equation

The operators \(\Lambda_j\) are bounded and every \(G_j\) is
Hilbert--Schmidt, hence bounded.  Since \(m\) is fixed, the right-hand side
of (8.2) is locally Lipschitz on the product Hilbert space.  Local existence
and uniqueness therefore follow from the Picard–Lindelöf theorem in Banach
spaces.

Repeating the estimate (9.2) for this deterministic state prevents escape on
every finite interval.  The path equation therefore has a unique global
solution.

For a nonzero label, more is true.  Write

\[
g(t)=\operatorname{sgn}(y)f(t),
\qquad
r(t)=|e(t)|.                                                \tag{10.1}
\]

The residual equation preserves the sign of \(e\), so

\[
g'=2\eta rK,
\qquad
r=|y|-g.                                                    \tag{10.2}
\]

Thus \(g'\ge0\), and

\[
g'(0)=2\eta|y|K(0)=2\eta|y|(L+1)>0.
\]

Consequently \(g(t_0)>0\) for every \(t_0>0\).

The two endpoint squared norms have the same derivative and the same initial
value:

\[
\frac d{dt}\|u\|^2
=4\eta ef
=\frac d{dt}\|v\|^2,
\qquad
\|u(0)\|^2=\|v(0)\|^2=1.                                 \tag{10.3}
\]

Denote their common value by \(Q(t)\).  Since

\[
f=\langle u,b_0\rangle
=\langle v,a_m\rangle,
\]

Cauchy--Schwarz and (7.10) give

\[
K\ge\frac{2g^2}{Q}.                                       \tag{10.4}
\]

Fix any \(t_0>0\).  Dividing (10.3) by (10.2) yields

\[
\frac{dQ}{dg}=\frac{2g}{K}\le\frac Qg.                    \tag{10.5}
\]

Thus \(Q/g\) is nonincreasing after \(t_0\), and

\[
K(t)\ge
\frac{2g(t)g(t_0)}{Q(t_0)}
\ge\frac{2g(t_0)^2}{Q(t_0)}
=:\kappa>0
\qquad(t\ge t_0).                                         \tag{10.6}
\]

It follows that

\[
r(t)\le r(t_0)
\exp[-2\eta\kappa(t-t_0)].                                \tag{10.7}
\]

Therefore

\[
e(t)\longrightarrow0,
\qquad
f(t)\longrightarrow y,
\qquad
\mathcal L(t)\longrightarrow0                             \tag{10.8}
\]

at an exponential rate.  Unlike the special depth-two proof, this argument
does not require analyzing a feature-time singularity.

## 11. The first depths and exact regression checks

When \(L=1\), there are no middle matrices and no path-source edge.  The
feature flow is simply

\[
\frac{du}{ds}=v,
\qquad
\frac{dv}{ds}=u.
\]

The two roots are orthonormal, so

\[
f(s)=\sinh(2s),
\qquad
K(s)=2\cosh(2s).                                           \tag{11.1}
\]

When \(L=2\), there is one middle Gaussian matrix and one path operator
\(\Lambda_1\).  The balancedness invariants then permit a further reduction to
the single scalar spectral coordinate and the explicit measure in the
two-hidden-layer note.  That scalar spectral system is the rigorously
established positive-time limit.  The path equation gives the corresponding
single-edge Gaussian-word realization; no state-by-state unitary equivalence
is needed for the present arbitrary-depth formulation.

For \(L\ge3\), the path source is the natural canonical replacement for that
scalar spectrum: it stores the mixed noncommuting Gaussian words generated
by all middle matrices.  Its finite-width identification has the conditional
status stated in Section 9.

As an exact algebraic regression test of the deterministic path equation,
its feature-time Taylor recurrence gives the following values.  The
order-\(k\) coefficients have path support of length at most
\((k+1)(L-1)\); hence a cutoff
\(R=(N+1)(L-1)\) cannot affect derivatives through order \(N\).
In the table,

\[
f_s^{(k)}(0):=
\left.\frac{d^kf}{ds^k}\right|_{s=0}.
\]

\[
\begin{array}{c|rrrrrr}
L&f_s^{(0)}(0)&f_s^{(1)}(0)&f_s^{(2)}(0)
&f_s^{(3)}(0)&f_s^{(4)}(0)&f_s^{(5)}(0)\\ \hline
1&0&2&0&8&0&32\\
2&0&3&0&48&0&1464\\
3&0&4&0&160&0&13888.
\end{array}                                                \tag{11.2}
\]

The \(L=1\) row follows from (11.1), and the \(L=2\) row agrees with the
independent spectral calculation.  The \(L=3\) row verifies the internal
path algebra; by itself it is not a positive-time width-limit proof.

## 12. Exact meaning and scope

The claim boundary is:

| Statement | Status |
|---|---|
| Finite-width chain equations, kernel, loss identity, and balancedness at every fixed \(L\) | proved exactly |
| Autonomous rooted-path equation, local and global well-posedness, and exponential residual decay at every fixed \(L\) | proved for the deterministic equation |
| Positive-time finite-width identification at \(L=1\) | proved directly |
| Positive-time finite-width identification at \(L=2\) | proved by the rigorous one-edge \(\ell^2\) theorem; equivalently described by the scalar spectral closure |
| Positive-time finite-width identification at fixed \(L\ge3\) | conditional on the lemmas in Sections 6 and 9 |

The common model assumptions are one unit-normalized input, one scalar label,
identity activation, equal hidden widths, independent Gaussian initialization,
all layers trained, and hidden depth \(L\) fixed before \(n\to\infty\).

The finite network contains exactly

\[
nd+(L-1)n^2+n
\]

parameters.  The path description
can be packaged as two endpoint vectors, one depth-graded trainable block
operator, one scalar residual, and one fixed depth-graded source operator.
The number of top-level objects is independent of width and requested
derivative order.

The path space and its \(L-1\) edge grades still depend on \(L\).  Thus this
is an \(O(1)\)-object closure for each fixed depth, not a constant-memory or
constant-work limit as \(L\to\infty\).

The path source is not a Stieltjes representing measure.  The autonomous
loss theorem does not prove that the transformed output-kernel coefficients
form a Stieltjes moment sequence at every depth.  That remains a separate
positivity problem.

The rigorous published analysis of Chizat, Colombo, Fernandez-Real, and
Figalli treats the one-middle-matrix case.  Its arbitrary-layer section calls
the path construction formal.  Sections 6 and 9 isolate the additional
estimates that would promote the present fixed-depth path equation to a
positive-time arbitrary-depth width-limit theorem.

Source: L. Chizat, M. Colombo, X. Fernandez-Real, and A. Figalli,
[*Infinite-width limit of deep linear neural networks*](https://doi.org/10.1002/cpa.22200),
*Communications on Pure and Applied Mathematics* 77 (2024), 3958--4007.
