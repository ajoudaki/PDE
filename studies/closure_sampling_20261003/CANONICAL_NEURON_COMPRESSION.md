# Canonical one-input neuron compression by two-sided response cubature

2026-10-03. Internally checked research theorem. This note concerns the actual
two-hidden-layer canonical Gaussian **dense** network and an autonomous
smaller weighted dense network. It does not change the reference
initialization or substitute a population predictor. The full complex
source theorem, its circle-query extension, and this construction were
reconstructed in `COMPLEX_ACTIVITY_CHECK.md` and
`CANONICAL_NEURON_COMPRESSION_CHECK.md`. These are internal collaborative
checks, not independent promotion reviews or established manuscript claims.

## 1. Theorem and model

Let $d=2$, train on $x_1=\sqrt2 e_1$ with one fixed label
$0<y\le y_*$, and consider all queries
$x_\theta=\sqrt2(\cos\theta,\sin\theta)$. The reference has
width $n$ in both hidden layers:

\[
 h(x)=\tanh(Ax/\sqrt2),\quad g(x)=\tanh(Wh(x)),\quad
 f_n(t,x)=w^\top g(x)/n.
\]

Initially $A_0$ has independent $N(0,1)$ entries, $W_0$ has
independent $N(0,1/n)$ entries, the two arrays are independent, and
$w_0=0$. Its loss is $(f_n(t,x_1)-y)^2$. The block mobilities are
exactly the manuscript's $(n,1,n)$ for $(A,W,w)$.

There are fixed constants
$y_*,C,c>0$ such that, for every fixed $0<\eta<1/2$ and all
sufficiently large $n$, an initialization-only construction gives a
smaller, restartable, autonomous weighted network for which, with
probability at least $1-\eta$,

\[
 \sup_{t\in[0,\infty]}\sup_{\theta\in\mathbb R}
 |f_C(t,x_\theta)-f_n(t,x_\theta)|\le C/\sqrt n.
 \tag{1}
\]

The value at $t=\infty$ denotes the fitted limit, whose existence and
interpolation are part of the claim for both systems. Every constant in
(1) is independent of width and physical time. The total number of moving
real coordinates obeys

\[
 P_n\le C\exp\!\left(C\sqrt{\log(en/\eta)}\right)
               [\log(en/\eta)]^{10}=n^{o(1)}
 \tag{2}
\]

at fixed confidence. In particular $P_n=o(n)$ and is eventually below
every fixed positive power of $n$. This is not a polylogarithmic bound.
The first-layer rows of the smaller network are selected original rows;
its mixer is a two-sided projection of the original initialized mixer.
After setup neither its training nor query evaluation consults a
width-$n$ array. Fixed stored coefficients satisfy the same bound as (2).

The smaller network need not have canonical Gaussian initialization.
Changing the empirical sampling rule is precisely what the construction
uses. Its learned hidden matrix is small and fully evolved; the reference
remains the original width-$n$ dense flow. This is a direct dense-network
construction, not a claim that the original order-$q$ memory equations
have simply lost their neuron indices.

## 2. Activity, a regular coordinate, and uniform fitting

Use $s$ for training activity, with $ds/dt=2(y-f)$ and $s(0)=0$.
For the moment work with the label-independent activity equations. Put
$a=Ae_1$, $\beta=A_0e_2$, $h=\tanh a$, $z=Wh$,
$g=\tanh z$, and $\delta=w\odot\operatorname{sech}^2z$.
Primes mean activity derivatives:

\[
 a'=\operatorname{sech}^2a\odot W^\top\delta,
 \quad W'=\delta h^\top/n,\quad w'=g.
 \tag{3}
\]

The second read-in column $\beta$ stays unchanged. Define the strictly
increasing real function

\[
 \Psi(a)=a/2+\sinh(2a)/4,\qquad
 u=\Psi(a),\qquad \sigma(u)=\tanh(\Psi^{-1}(u)).
\]

Since $\Psi'(a)=\cosh^2 a$, (3) gives exactly

\[
 u'=W^\top\delta,\quad h=\sigma(u),\qquad
 (\Psi^{-1})'(u)=\operatorname{sech}^2a\le1,
 \quad \sigma'(u)=\operatorname{sech}^4a\le1.
 \tag{4}
\]

This change of variables is used in the proof; the stored compressed
read-in may still be the ordinary real $a$.

Suppose $\|W_0\|_{\rm op}\le K$ and
$\|g_0\|_2^2/n\ge\gamma>0$. On a fixed short interval
$|s|\le S$, the activity equations imply, with constants depending
only on $K$,

\[
 \|w(s)\|_\infty\le |s|,\quad
 \|W(s)-W_0\|_F\le C s^2,\quad
 \frac{\|u(s)-u_0\|_2}{\sqrt n}
 +\frac{\|h(s)-h_0\|_2+\|g(s)-g_0\|_2}{\sqrt n}
 \le C s^2.
 \tag{5}
\]

For example, $|g_j|\le1$ gives the first bound. Then
$\|\delta\|_2/\sqrt n\le |s|$, so integration of $W'$ keeps
$\|W\|_{\rm op}\le K+Cs^2$, which bounds $u'$ in normalized
Euclidean norm. The 1-Lipschitz function $\sigma$ and the forward
chain rule finish the bounds. Choosing $S$ sufficiently small closes
the operator tube without a neuronwise carrier estimate.

The training prediction obeys the exact identity

\[
 f_n'(s,x_1)=\frac{\|g\|_2^2}{n}
 +\frac{\|\delta\|_2^2\|h\|_2^2}{n^2}
 +\frac{\|\operatorname{sech}^2a\odot W^\top\delta\|_2^2}{n}.
 \tag{6}
\]

For a fixed small $S$, (5) preserves $\|g\|_2^2/n\ge\gamma/2$.
The same estimates bound (6) above by a fixed constant. Thus choosing
$y_*<\gamma S/4$ puts the unique solution of $f_n(s,x_1)=y$
strictly inside $[0,S]$. The scalar physical clock then increases to
this endpoint, with exponentially decaying residual.

The identical argument works for positive weighted populations, with
weighted Euclidean and Hilbert--Schmidt norms. Only total mass one, the
initial mixer operator bound, and the training Gram gap enter. No minimum
neuron weight enters any estimate. The construction below preserves both
initialized bounds exactly or improves them.

For canonical initialization the two bounds hold on an event with
exponentially small complement. The operator estimate follows from finite
sphere nets and Gaussian tails. Conditional on the first features, the
upper preactivations are iid Gaussians of variance $\|h_0\|_2^2/n$;
bounded-variable concentration at the two layers supplies the fixed
positive scalar Gram gap. This uses no population training theorem.

## 3. The analytic source input and its finite initial representation

The needed source regularity is the finite-network, two-sided complex
activity theorem in `COMPLEX_ACTIVITY_ROUTE.md`, together with its
circle-query extension. It is not inferred from a real signal maximum.
Here is the exact input required from that proof.

Put $\ell=\log(en/\eta)$. On a common initialization event,
the actual dense sources extend holomorphically to a complex activity
rectangle containing $[-S-2r,S+2r]+i[-r,r]$ and the complex angular
strip $|\Im\theta|\le r_\theta$, where

\[
 r\ge c/\sqrt\ell,\qquad r_\theta\ge c/\sqrt\ell.
\]

The coordinate magnitudes of

\[
 h(s,\theta),\quad g(s,\theta),\quad W_0h(s,\theta),
 \quad\delta(s),\quad W_0^\top\delta(s)
 \tag{7}
\]

are at most $C\sqrt\ell$ there. The last two sources are training
sources only. The activity parity $A(-s)=A(s)$, $W(-s)=W(s)$,
$w(-s)=-w(s)$ supplies the symmetric rectangle from a one-sided
version. Constants can be adjusted by taking a smaller $S$ and using
a fixed fraction of the proved strip radii.

For the last source in (7), the complex theorem bounds
$W(s)^\top\delta(s)$. Subtracting the learned matrix gives
\[
 [(W(s)-W_0)^\top\delta(s)]_i
 =\int_0^s h_i(v)\,\delta(v)^\top\delta(s)/n\,dv.
\]
On a complex radial path the first feature is bounded, the response RMS
is bounded, and the path length is bounded. Thus this correction is
coordinatewise $O(S^3)$, proving the stated bound for $W_0^\top\delta$.

The explicit analytic-continuation lemma in
`CANONICAL_SCALAR_AUTONOMY_ROUTE.md` approximates any source in (7),
uniformly for $0\le s\le S$, by a scalar linear combination of its
initial activity derivatives of orders at most $p$, with error at most
$\epsilon$, provided

\[
 p\le C e^{C\sqrt\ell}\ell
 \tag{8}
\]

is chosen sufficiently large, for $\epsilon$ a fixed constant times
$n^{-1/2}$. To recall the construction, map the unit disk into the
activity rectangle by

\[
 z(\zeta)=\frac{2r}{\pi}
  \log\frac{1+\alpha\zeta}{1-\alpha\zeta},
 \qquad \alpha=\tanh\frac{\pi(S+2r)}{4r}.
\]

The Taylor coefficients of $R(z(\zeta))$ are linear combinations of
$R^{(j)}(0)$. Cauchy's formula bounds them by the source supremum.
At the largest real activity, $1-|\zeta|\ge c e^{-CS/r}$, so the
truncation error is bounded by a geometric tail. This proves (8).
It is a continuation of initial derivatives, not a Taylor remainder
asserted outside its original convergence disk.

For the periodic query variable, a function bounded by $M$ on
$|\Im\theta|\le r_\theta$ has Fourier coefficients bounded by
$M e^{-|j|r_\theta}$: shift the defining integral to either horizontal
boundary, using Cauchy's theorem and periodicity. The tail after frequency
$L$ is at most $2M e^{-(L+1)r_\theta}/(1-e^{-r_\theta})$.
Use the trigonometric interpolant at the $2L+1$ equally spaced real
angles. Each Fourier mode of frequency greater than $L$ aliases to a
frequency in $[-L,L]$, so its contribution to the interpolation error
on real angles is at most twice its coefficient magnitude. Absolute
summability justifies grouping these modes; thus the interpolation error
is bounded by twice the displayed tail. Taking

\[
 L\le C\ell^{3/2}
 \tag{9}
\]

sufficiently large gives another error at most $\epsilon$. Apply the
activity approximation first, uniformly also for complex $\theta$;
its angular-strip bound is at most the original bound plus its error.
Then take this trigonometric interpolant. These linear operations commute,
so its coefficients are finite discrete Fourier transforms of initial
activity derivatives at the selected angles. They require only finitely
many initialized derivatives and finite linear algebra, with no angular
integration or trained-path evaluation. All arithmetic in this mathematical
construction is exact; a numerical precision and setup-cost theorem is
not claimed.

Work with real sine and cosine coefficients. Let $S_1$ contain all
coefficient vectors used to approximate $h(s,\theta)$, all initial
training derivatives $W_0^\top\delta^{(j)}(0)$ for $j\le p$,
the initial training vector $h_0$, and the two columns of $A_0$.
Let $S_2$ contain all coefficient vectors for $g(s,\theta)$, the
images under $W_0$ of the listed forward-feature coefficient vectors,
the training derivatives $\delta^{(j)}(0)$, and $g_0,W_0h_0$.
Additional direct training-feature derivatives may be included without
changing the count. Both dimensions obey

\[
 r_1,r_2\le C(p+1)(2L+1)+C.
 \tag{10}
\]

Every needed forward approximation and its image under $W_0$ use
the **same scalar coefficients**. Both remainders are bounded
coordinatewise by $C\epsilon$, by applying the common linear
approximation to the two sources in (7). The same holds for the backward
approximation and its image under $W_0^\top$. This paired approximation
is essential; a small lower-layer remainder alone would not bound its
sampled mixer image.

## 4. Positive empirical cubature and the reduced autonomous model

Choose empirical orthonormal basis matrices $V,U$ of $S_1,S_2$:
$V^\top V/n=I$, $U^\top U/n=I$. Positive finite cubature selects
original index sets $I,J$ and strictly positive diagonal masses $D_1,D_2$
of total mass one such that

\[
 V_I^\top D_1V_I=I,\qquad U_J^\top D_2U_J=I.
 \tag{11}
\]

There are at most $1+r_1(r_1+1)/2$ lower and
$1+r_2(r_2+1)/2$ upper nodes. Indeed, match the constant and all
symmetric basis products. Whenever more nodes remain than this affine
dimension permits, an affine dependence allows their positive weights to
move until one becomes zero, preserving every matched quantity. Repeating
terminates on the original finite support.

Define

\[
 B=U^\top W_0V/n,\qquad B_0=U_JBV_I^\top D_1,
 \qquad B_0^*=D_1^{-1}B_0^\top D_2.
 \tag{12}
\]

The selected basis matrices are weighted isometries, so
$\|B_0\|_{D_1\to D_2}\le\|W_0\|_{\rm op}$. Whenever
$v\in S_1$ and $W_0v\in S_2$,
$B_0v_I=(W_0v)_J$. Likewise, if $d\in S_2$ and
$W_0^\top d\in S_1$, then
$B_0^*d_J=(W_0^\top d)_I$. This proves both exact mixer actions
with the correct empirical normalization.

The smaller model stores selected first rows $A_C$, an evolving
$N_2\times N_1$ matrix $B_C$, and an $N_2$-vector $w_C$.
Its forward and backward quantities are

\[
 h_C(x)=\tanh(A_Cx/\sqrt2),\quad
 z_C(x)=B_Ch_C(x),\quad g_C(x)=\tanh z_C(x),
 \quad f_C=w_C^\top D_2g_C,
\]

\[
 \delta_C=w_C\odot\operatorname{sech}^2 z_C(x_1),
 \qquad B_C^*=D_1^{-1}B_C^\top D_2.
\]

Initialize $A_C=(A_0)_I$, $B_C=B_0$, $w_C=0$. In physical time,
with its own residual $r_C=f_C(x_1)-y$, evolve

\[
 \begin{aligned}
 \dot A_C&=-2r_C[\operatorname{sech}^2(A_Ce_1)
                          \odot B_C^*\delta_C]e_1^\top,\\
 \dot B_C&=-2r_C\delta_Ch_C(x_1)^\top D_1,\\
 \dot w_C&=-2r_Cg_C(x_1).
 \end{aligned}
 \tag{13}
\]

These formulas define the full autonomous algorithm. The orthogonal
first-column complement stays fixed, as in the reference. Both forward
and reverse use the same evolving matrix with its exact weighted adjoint.
No original-neuron oracle, external residual, prescribed trajectory, or
full-width state appears in (13).

The initial training feature is exactly $(g_0)_J$, and (11) preserves
its Gram. Therefore the uniform fitting argument in Section 2 applies to
(13) with the same fixed constants. The moving count is
$2N_1+N_1N_2+N_2$; equations (8)--(11) give (2). The stored fixed
weights, selected initialization, and initial mixer use no larger order.
Setup arithmetic and conditioning are not claimed to be efficient.

## 5. From source accuracy to the entire autonomous trajectory

All comparisons in this section are exact proof devices based on the
original path; the algorithm (13) does not evaluate them.

If two bounded source vectors $v(s),v(t)$ are approximated in
coordinate supremum by vectors in $S_1$ with error $C\epsilon$,
then their pairings satisfy

\[
 |v(s)_I^\top D_1v(t)_I-v(s)^\top v(t)/n|\le C\epsilon.
 \tag{14}
\]

To verify this, insert both approximants. Their pairing is exact by
(11); each remaining term is bounded by the remainder times a bounded
weighted or empirical norm. The approximants have bounded weighted norms
because their norms agree exactly with their empirical norms, which are
bounded by the original source norm plus its remainder. The argument
also handles two different sources and the space $S_2$. It introduces
no inverse minimum mass. Integrating the upper-feature approximation
in activity gives the required approximation to $w(s)$ in $S_2$.

Set $h_I=h(s,x_1)_I$, $\delta_J=\delta(s)_J$, $w_J=w(s)_J$
and define the reference matrix on selected nodes by

\[
 B_R(s)=B_0+\int_0^s\delta_J(v)h(v,x_1)_I^\top D_1\,dv.
 \tag{15}
\]

The original dense matrix has the identical formula with empirical
pairings normalized by $1/n$. Applying (14), the paired fixed-mixer
approximations from Section 3, and the identity (12) gives, uniformly
over $s\in[0,S]$ and all real query angles,

\[
 \|B_R(s)h(s,x_\theta)_I-z(s,x_\theta)_J\|_{D_2}
 \le C\epsilon,
\]

\[
 \|B_R(s)^*\delta_J(s)-(W(s)^\top\delta(s))_I\|_{D_1}
 \le C\epsilon.
 \tag{16}
\]

For example, the learned forward error is the integral of
$\delta_J(v)$ times the difference between the two pairings
$\langle h(v,x_1),h(s,x_\theta)\rangle$. The learned reverse
error pairs $\delta(v)$ and $\delta(s)$ in $S_2$. Thus both
errors are controlled, including the accumulated learned mixer.
Similarly,

\[
 |w_J(s)^\top D_2g(s,x_\theta)_J-f_n(s,x_\theta)|
 \le C\epsilon.
 \tag{17}
\]

The matrix $B_R$ has weighted operator norm at most $K+CS^2$.
All retained reference features have bounded weighted norms, and
$\|w_J\|_\infty\le S$. These bounds follow from (14)--(15)
and the bounded source coordinates.

Compare the reduced activity solution of (13) with
$(u(s)_I,B_R(s),w(s)_J)$, where $u=\Psi(a)$. Use the sum of
weighted Euclidean errors for $u,w$ and weighted Hilbert--Schmidt
error for $B$. In the regular coordinates (4), the reduced activity
vector field is

\[
 u_C'=B_C^*\delta_C,\quad
 B_C'=\delta_Ch_C^\top D_1,\quad w_C'=g_C.
 \tag{18}
\]

Its finite differences have a fixed Lipschitz constant on the real
operator and readout tube. For instance,

\[
 \|\delta_C-\delta_R\|_{D_2}
 \le\|w_C-w_J\|_{D_2}
  +C\|w_J\|_\infty\|B_Ch_C-z_J\|_{D_2},
\]

and $\|\sigma(u_C)-\sigma(u_I)\|_{D_1}
\le\|u_C-u_I\|_{D_1}$. The rank-one update satisfies
$\|xy^\top D_1\|_{\rm HS}=\|x\|_{D_2}\|y\|_{D_1}$.
The reference violates (18) by at most $C\epsilon$, by (16).
Its initial error is zero. Gronwall on the fixed activity interval yields

\[
 \sup_{0\le s\le S}
 \left(\|u_C-u_I\|_{D_1}
       +\|B_C-B_R\|_{\rm HS}
       +\|w_C-w_J\|_{D_2}\right)\le C\epsilon.
 \tag{19}
\]

The constant is independent of the number and weights of selected nodes.
The complete weighted comparison and its tube justification are recorded
in `WEIGHTED_ACTIVITY_STABILITY.md`.

Since $\Psi^{-1}$ is 1-Lipschitz on the real line and the unused
read-in column is identical at retained nodes, (19) controls first
query features at every real angle. Equations (16)--(17) then imply

\[
 \sup_{0\le s\le S,\,\theta\in\mathbb R}
 |f_C(s,x_\theta)-f_n(s,x_\theta)|\le C\epsilon.
 \tag{20}
\]

Finally both models use their own physical activity clocks. The scalar
contraction argument in `CANONICAL_SCALAR_AUTONOMY_ROUTE.md` bounds
their activity difference at the same physical time by
$C\epsilon/\gamma$. The reference query derivative in activity is
uniformly bounded on the real circle: use (3), bounded gates, the
operator bound, and normalized RMS response bounds. Applying the chain
rule and (20) therefore proves (1) when $\epsilon$ is chosen as a
fixed multiple of $n^{-1/2}$. Clock convergence proves the same statement
at the fitted endpoints, not merely at equal activity.

## 6. Scope and completed checks

The complete complex circle-query theorem, finite initialization-only
coefficient construction, paired forward and reverse consistency,
weighted nonlinear stability, state count, and same-physical-time clock
comparison have all been reconstructed in the linked check files.
`CANONICAL_FEATURE_LEARNING.md` separately proves that both hidden
feature vectors move by a width-independent amount at every fixed small
nonzero label; this construction does not rely on freezing either layer.

The theorem concerns one training input and the entire input circle.
No universal statement for multiple training inputs, arbitrary depth,
large labels, efficient finite-precision setup, or the unchanged
finite-order closure is claimed here. The result is a direct, coordinated
width compression of a realized canonical dense network.
