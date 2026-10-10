# Worked examples of the finite Gaussian calculus

These examples implement [the rulebook](calculus_rulebook.md) using the
existing [master theorem](master_proof.md). They do not extend that theorem.
All widths tend to infinity with the displayed graph, scalar parameters and
derivative orders fixed. Each $\phi$ used below is smooth and every
derivative has polynomial growth. Consequently every displayed scalar graph
is admitted, and the theorem gives convergence in every finite $L^p$.

A matrix $W:\mathbb R^n_{\rm lower}\to\mathbb R^n_{\rm upper}$ has iid
$N(0,1/n)$ entries. Its transpose is the transpose of that same matrix.
The vector $e\in\mathbb R^n_{\rm lower}$ has every coordinate equal to one.
Capital letters represent limiting scalar coordinates; expectations always
contract quantities on the same type. A standard real Gaussian is denoted
by $G\sim N(0,1)$.

## 1. A nonlinear forward call followed by its reused transpose

Define the finite-width program

\[
y=We,\qquad u=\phi(y),\qquad v=W^Tu,\qquad
J_n=\frac1n\sum_{j=1}^n v_j^2.
\]

The first call has constant lower-type input $H=1$. Its output is a
centered source $Y=\xi\sim N(0,1)$, because no reverse call precedes it.
The nonlinear node has representative $U=\phi(\xi)$. Define

\[
q=\mathbb E[\phi(G)^2],\qquad c=\mathbb E[\phi'(G)].
\]

For the reverse call the new source has variance $\mathbb E U^2=q$.
Its response to the earlier forward call is

\[
H\,\mathbb E[\partial_\xi U]
=1\cdot\mathbb E[\phi'(G)]=c.
\]

Thus $V=\zeta+c$, where $\zeta\sim N(0,q)$ is centered and belongs
to the reverse-oriented source group. The average becomes

\[
J_*=\mathbb E[V^2]=q+c^2
=\mathbb E[\phi(G)^2]+\bigl(\mathbb E[\phi'(G)]\bigr)^2.
\]

The second term records reuse of the same matrix. In particular, replacing
the reverse call by an independent matrix would describe a different finite
program and would remove this term.

### Independent finite-width verification

Write $P=I-ee^T/n$, the orthogonal projection onto the subspace perpendicular
to $e$. Each row of $W$ decomposes into its projection onto $e$ and an
independent Gaussian remainder, giving the exact distributional representation

\[
W=ye^T/n+B,\qquad Be=0.
\]

Here $y_1,\ldots,y_n$ are iid standard Gaussians, $B$ is independent of
$y$, and its independent rows are centered Gaussian vectors with covariance
$P/n$. Therefore, conditionally on $y$,

\[
v=e\,\frac{y^T\phi(y)}n+B^T\phi(y),\qquad
\operatorname{Cov}(B^T\phi(y)\mid y)
=\left(\frac1n\sum_i\phi(y_i)^2\right)P.
\]

The two displayed vector terms are orthogonal for every realization because
$Be=0$. Since $\operatorname{tr}P=n-1$,

\[
\mathbb E[J_n\mid y]
=\left(\frac1n\sum_i y_i\phi(y_i)\right)^2
 +(1-1/n)\frac1n\sum_i\phi(y_i)^2.
\]

Gaussian integration by parts gives
$\mathbb E[G\phi(G)]=\mathbb E[\phi'(G)]=c$: integrate against the
standard Gaussian density, whose derivative is $-x$ times that density;
the polynomial growth assumption makes the boundary term zero. Independence
of the $y_i$'s now gives the exact expectation

\[
\mathbb E J_n
=q+c^2+\frac1n\left(\mathbb E[G^2\phi(G)^2]-q-c^2\right).
\]

This confirms the Gaussian limit and separates it from a finite-width
expectation. For instance,

| $\phi(x)$ | $q$ | $c$ | $J_*$ | Exact $\mathbb E J_n$ |
| --- | ---: | ---: | ---: | ---: |
| $x$ | $1$ | $1$ | $2$ | $2+1/n$ |
| $x^2$ | $3$ | $0$ | $3$ | $3+12/n$ |
| $x^3$ | $15$ | $3$ | $24$ | $24+81/n$ |

The Gaussian moments used here are $\mathbb E G^2=1$,
$\mathbb E G^4=3$, $\mathbb E G^6=15$, and $\mathbb E G^8=105$,
obtained recursively from the same integration-by-parts identity.

### The finite physical gradient must accumulate both uses

Treat $W$ as the current ambient matrix parameter. For a scalar differential,

\[
dJ_n=\frac2n v^Tdv,\qquad
dv=(dW)^Tu+W^T\bigl(\phi'(y)\odot(dW)e\bigr).
\]

Since $v^TW^T=(Wv)^T$, matching the Frobenius differential yields

\[
\nabla_WJ_n
=\frac2n\left[u v^T+
       \bigl((Wv)\odot\phi'(y)\bigr)e^T\right].
\]

The first term comes from the transpose occurrence, the second from the
forward occurrence. Both are normalized rank-one terms of the admitted form.
This is a physical parameter gradient at finite width. The earlier formal
partial $\partial_\xi\phi(\xi)=\phi'(\xi)$ was a different operation used
only to construct the scalar response coefficient $c$.

## 2. One gradient update and its normalized rank-one lowering

Keep $y=We$ and use the scalar loss

\[
\mathcal L_n(W)=\frac1n\sum_i\phi(y_i).
\]

For this example $\phi$ is the scalar loss function, with its normalization
stated explicitly. Set $p=\phi'(y)$. The differential

\[
d\mathcal L_n=\frac1n p^T(dW)e
\]

gives the ambient gradient $\nabla_W\mathcal L_n=pe^T/n$. A single
gradient step with matrix mobility one and fixed step size $\eta$ produces

\[
A=W-\eta pe^T/n.
\]

The vector $p$ in this formula records the pre-update state. Define the
observable using that same saved vector,

\[
r=A^Tp,\qquad R_n=\frac1n\sum_j r_j^2.
\]

Lowering the representation is exact:

\[
Ae=y-\eta p,\qquad
r=W^Tp-\eta e\left(\frac{p^Tp}{n}\right).
\]

Let

\[
q=\mathbb E[\phi'(G)^2],\qquad c=\mathbb E[\phi''(G)].
\]

The first example applied to the function $\phi'$ gives the representative
of $W^Tp$ as $\zeta+c$, with $\zeta\sim N(0,q)$. The scalar pairing
$p^Tp/n$ has representative $q$. Therefore

\[
R=\zeta+c-\eta q,\qquad
R_*:=\lim_{n\to\infty}R_n=q+(c-\eta q)^2
\quad\text{in every finite }L^p.
\]

The limit notation is a random-variable convergence statement to a
deterministic constant. For $\phi(x)=x^4/4$, the concrete values are

\[
p=y^3,\qquad q=15,\qquad c=3,\qquad
R_*=15+(3-15\eta)^2.
\]

At $\eta=0$ this agrees with the cubic reuse value $24$. Treating $A$
as an independent Gaussian matrix or omitting either factor $1/n$ would
fail the exact lowering identities before any limit is taken.

## 3. Exact duplicate queries with singular source covariance

Make two distinct calls with the same input:

\[
y_1=We,\qquad y_2=We,\qquad
u=\phi(y_1+y_2),\qquad v=W^Tu,\qquad
J_n^{\rm dup}=\frac1n\sum_jv_j^2.
\]

At finite width $y_1=y_2$ exactly. The evaluator retains two named source
arguments $\xi_1,\xi_2$ with joint covariance

\[
K=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

The law is $ (\xi_1,\xi_2)=(G,G)$ almost surely. The input expression to
the reverse call nevertheless remains
$U(\xi_1,\xi_2)=\phi(\xi_1+\xi_2)$, with formal partials

\[
\partial_{\xi_1}U=\phi'(\xi_1+\xi_2),\qquad
\partial_{\xi_2}U=\phi'(\xi_1+\xi_2).
\]

Both preceding forward inputs have representative one. Their two response
contributions add. Define

\[
q=\mathbb E[\phi(2G)^2],\qquad c=2\mathbb E[\phi'(2G)].
\]

The reverse source has variance $q$ and the output is $V=\zeta+c$.
Consequently

\[
J_*^{\rm dup}=q+c^2
=\mathbb E[\phi(2G)^2]+4\bigl(\mathbb E[\phi'(2G)]\bigr)^2.
\]

As an independent algebraic check, the finite program equals the first
example with $\psi(x)=\phi(2x)$. Its derivative is
$\psi'(x)=2\phi'(2x)$, giving exactly the same formula. For $\phi(x)=x$,
$q=4,c=2$ and the limit is $8$; finite linearity gives the stronger
check $\mathbb E J_n^{\rm dup}=8+4/n$. For $\phi(x)=x^3$,
$q=64\mathbb E G^6=960$, $c=24$, and the limit is $1536$.

There is no covariance inverse in this calculation. Integrating on the
diagonal support is harmless after the two source partials have been formed.

### A zero input whose formal partials are nonzero

Change only the reverse input to

\[
u=\phi(y_1)-\phi(y_2).
\]

It is identically zero at finite width. Its representative has variance zero
on the singular Gaussian support, but

\[
\partial_{\xi_1}U=\phi'(\xi_1),\qquad
\partial_{\xi_2}U=-\phi'(\xi_2).
\]

The response is $1\cdot\mathbb E\phi'(G)-1\cdot\mathbb E\phi'(G)=0$.
The centered reverse source also has variance zero, hence equals zero almost
surely. Thus $V=0$ and every resulting squared average remains zero.
This checks preservation of the exact duplicate identity while keeping
formal source arguments distinct.

## 4. A moving gradient-flow direction

This example uses one trainable vector state $x\in\mathbb R^n$, with iid
$x_i(0)\sim N(0,1)$, and no matrices. Here $x$ is a state vector, not a
dataset input. Define the scalar loss and observable by

\[
\mathcal L_n(x)=\frac1n\sum_i\phi(x_i),\qquad
O_n(x)=\frac1n\sum_i x_i^2.
\]

The Euclidean loss gradient is $\nabla_x\mathcal L_n=\phi'(x)/n$.
With vector mobility $n$, the physical gradient flow is

\[
\dot x=V(x)=-\phi'(x),\qquad
DV(x)[h]=-\phi''(x)\odot h.
\]

Thus $DV(x)[V(x)]=\phi''(x)\odot\phi'(x)$. Differentiating the observable
at finite width first gives

\[
\begin{aligned}
\dot O_n&=-\frac2n\sum_i x_i\phi'(x_i),\\
D^2O_n[V,V]&=\frac2n\sum_i\phi'(x_i)^2,\\
DO_n[DV[V]]&=\frac2n\sum_i x_i\phi''(x_i)\phi'(x_i),\\
\ddot O_n&=\frac2n\sum_i\left[\phi'(x_i)^2
                      +x_i\phi''(x_i)\phi'(x_i)\right].
\end{aligned}
\]

All expressions on the right are finite primitive graphs. Evaluate them at
the initial roots and apply the theorem:

\[
\begin{aligned}
O_n(0)&\longrightarrow1,\\
\dot O_n(0)&\longrightarrow-2\mathbb E[G\phi'(G)],\\
\ddot O_n(0)&\longrightarrow
2\mathbb E\left[\phi'(G)^2+G\phi''(G)\phi'(G)\right]
\end{aligned}
\]

in every finite $L^p$. This calculation takes no derivative of a
width-limit formula.

For the polynomial loss $\phi(x)=x^4/4$,

\[
V(x)=-x^3,\qquad DV(x)[V(x)]=3x^5.
\]

The Gaussian moments give

\[
\begin{aligned}
\lim_n\dot O_n(0)&=-2\mathbb E G^4=-6,\\
\lim_n D^2O_n[V,V]\big|_0&=2\mathbb E G^6=30,\\
\lim_n DO_n[DV[V]]\big|_0&=6\mathbb E G^6=90,\\
\lim_n\ddot O_n(0)&=8\mathbb E G^6=120.
\end{aligned}
\]

The moving-direction answer is **120**, while freezing the initial direction
in a straight-line path gives **30**.

### Direct solution and jet-factorial check

For a coordinate initialized at $a$, the scalar ODE $\dot x=-x^3$ has
the explicit solution

\[
x(t)=\frac{a}{\sqrt{1+2ta^2}},\qquad
x(t)^2=\frac{a^2}{1+2ta^2}
\]

for $t\ge0$, and on its finite-width local interval around zero.
Differentiation at zero gives

\[
\left.\frac{d}{dt}x(t)^2\right|_0=-2a^4,
\qquad
\left.\frac{d^2}{dt^2}x(t)^2\right|_0=8a^6,
\]

confirming the finite-width formula and the limit $120$. In normalized jets,

\[
x_{[0]}=a,\qquad x_{[1]}=-a^3,\qquad
x_{[2]}=\frac32a^5,
\]

so the observable coefficient is

\[
(x^2)_{[2]}=2x_{[0]}x_{[2]}+x_{[1]}^2=4a^6.
\]

Its expectation is $60$; multiplication by $2!=2$ recovers the second
derivative $120$. The frozen path $a-ta^3$ instead has second derivative
of its square equal to $2a^6$, whose expectation is $30$.

## Checks and claim level

The matrix-reuse expectation has an independent finite-width Gaussian
projection calculation, with exact identity, quadratic and cubic checks.
The rank-one update has exact action and transpose-action identities and
agrees with the reuse example at zero step size. The singular examples agree
with direct finite-width duplication and preserve an identically zero
output. The moving-flow example agrees with its scalar ODE solution and
with factorial-normalized jet convolution.

These are deterministic derivations and exact Gaussian moment checks. The
master theorem supplies the asserted $L^p$ limits; finite checks alone do
not prove that theorem. No claim is made here about a growing number of
updates, an infinite jet expansion, or positive-time population dynamics.
