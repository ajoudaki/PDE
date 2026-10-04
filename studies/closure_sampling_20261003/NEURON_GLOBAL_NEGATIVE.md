# A prediction lower bound for neuron reductions retaining the canonical law

2026-10-03. Scoped theoretical continuation of `closure_sampling_20261003`.
Internally derived result; not independently reviewed or promoted.

**Result.** A smaller closure that retains the canonical Gaussian
initialization law cannot achieve root-original-width prediction accuracy
using a sublinear number of neurons, under any coupling to the original
initialization. Ordinary initialization-independent neuron subsampling, with
the usual variance-preserving rescaling of the selected mixer, is a corollary.
The obstruction occurs at one fixed positive physical time and, for one
sufficiently small fixed label, also at the fitted endpoint. It holds at
one unseen sphere input and in the integrated prediction norm for any
fixed query law on the sphere orthogonal to the training input. It is
uniform in the memory order and concerns the
actual nonlinear trained closure. This is a theorem about the precise class
below, not an impossibility theorem for response-aware weighted cubature or
arbitrary autonomous neuron reductions.

The proof does not stop at a mismatch of initial derivatives. An orthogonal
query has first-layer coordinates that training leaves unchanged and that
remain independent Gaussian variables. This gives a width-normalized bound
on the entire nonlinear remainder at a fixed time.

## 1. Exact model and the class of reductions

Fix input dimension $d\ge2$, one training pair and one query

\[
 x_1=\sqrt d\,e_1,\qquad y_1=y,\qquad
 x_*=\sqrt d\,e_2,\qquad 0<y\le1.
 \tag{1}
\]

The label is fixed independently of width and may be arbitrarily small.
The one-sample sphere dataset is compatible. There is no clipping, bias,
change of activation, or change of physical time.

At a generic width $k$, write $A=W^{(1)}\in\mathbb R^{k\times d}$,
$W=W^{(2)}\in\mathbb R^{k\times k}$ and
$w=W^{(3)}\in\mathbb R^k$. Throughout the proof, $W(t)$ means the
reconstructed matrix of the original residual-RMS, order-$q$ closure, not a
different approximation. Its forward pass, residual and loss are

\[
 h^{(1)}=\tanh(Ae_1),\quad
 h^{(2)}=\tanh(Wh^{(1)}),\quad
 f=k^{-1}w^\top h^{(2)},\quad r=f-y,\quad \mathcal L=r^2.
 \tag{2}
\]

Its backward response and outer-layer updates are

\[
 \delta^{(2)}=w\odot\operatorname{sech}^2(Wh^{(1)}),\qquad
 \dot A=-2r\,[\operatorname{sech}^2(Ae_1)\odot W^\top\delta^{(2)}]e_1^\top,
 \qquad \dot w=-2r h^{(2)}.
 \tag{3}
\]

The clock obeys $\dot\tau=|r|$, $\tau(0)=1$. The closure retains its own
$q$ forward moments $\bar h_j^{(1)}$ and $q$ backward moments
$\bar\delta_j^{(2)}$, with the original constant forward and zero backward
unit prefixes. Equivalently, if $\Pi_q$ denotes orthogonal projection in
$L^2(0,\tau)$ onto polynomials of degree less than $q$, then

\[
 W(t)=W_0-\frac2k\int_0^{\tau(t)}
       (\Pi_q b)(\xi)(\Pi_q h^{(1)})(\xi)^\top\,d\xi,
 \qquad b=\frac r{|r|}\delta^{(2)}
 \tag{4}
\]

on a nonzero-residual interval. The actual moment equations do not divide
by the residual. Formula (4) is only its exact history representation.
All quantities in (2)--(4) are evaluated in this closure's own state.
Initialization is canonical:

\[
 (A_0)_{ij}\stackrel{\mathrm{iid}}\sim N(0,1),\qquad
 (W_0)_{ij}\stackrel{\mathrm{iid}}\sim N(0,1/k),\qquad w(0)=0,
 \tag{5}
\]

with the two matrices independent. Denote its prediction by
$\widehat f_{k,q}(t,x)$.

The theorem permits **any joint law** of width-$n$ and width-$N$
initializations whose two marginals each satisfy (5). Each system then
runs its own original closure. The two orders $q_n,q_N\ge1$ are fixed
deterministic integers and may be arbitrary functions of the widths. The
coupling may depend on all of the original source; independence of the
two systems is not required. What is required is that the smaller
system's marginal initialization remains canonical.

Here is one concrete neuron sampler covered by the theorem. Given the realized
width-$n$ initialization, choose lower and upper index sets $I,J$, each
of size $N$, independently of that initialization. The sets can be fixed
or randomized using external randomness; they need not be independent of
each other. Set

\[
 \widetilde A_0=A_0[I,:],\qquad
 \widetilde W_0=\sqrt{\frac nN}\,W_0[J,I],\qquad
 \widetilde w(0)=0.
 \tag{6}
\]

Run exactly (2)--(4) at width $N$, with equal neuron masses $1/N$ and
its own coupled moments, residual, and clock. The matrix in (6) has entry
variance $1/N$; it and the selected first matrix therefore have precisely
the canonical width-$N$ marginal law. The two trained systems remain
coupled through the original initialization. The proof never replaces
the width-$n$ reference by a population target or assumes that the two
systems are independent.

The sampler's moving count is $N(d+1)+2Nq+1$; its fixed mixer has $N^2$
entries. Initialization-dependent selection is also covered if its
resulting smaller model has the same canonical marginal law. General
nonuniform cubature weights, response corrections, and a projected mixer
computed from all source entries are not required to preserve that law
and are outside the theorem.

## 2. Restricted prediction theorem

**Theorem.** There exist constants $t_*>0$, $c_y>0$, $p_*>0$ and
$\eta>0$, independent of $n,N,q$, such that, for all sufficiently large
$N$ and $N/n\le\eta$, any coupling of the two canonical marginal
initializations satisfies

\[
 \mathbb P\left\{
 \left|\widetilde f_{N,q_N}(t_*,x_*)-
       \widehat f_{n,q_n}(t_*,x_*)\right|
       \ge\frac{c_y}{\sqrt N}\right\}\ge p_*.
 \tag{7}
\]

The constants $t_*,p_*,\eta$ can be chosen uniformly for $0<y\le1$,
and $c_y$ is proportional to $y$. The estimate is uniform over arbitrary
deterministic choices of both positive orders. In particular it holds
when the two orders agree.

In particular, let $N\to\infty$ with $N=o(n)$ and take the fixed query
law $\mu=\delta_{x_*}$. For every fixed $C<\infty$,

\[
 \liminf_{n\to\infty}\mathbb P\left\{
 \left(\int\sup_{t\ge0}
 |\widetilde f_{N,q_N}(t,x)-\widehat f_{n,q_n}(t,x)|^2\,d\mu(x)\right)^{1/2}
 >\frac C{\sqrt n}\right\}\ge p_*.
 \tag{8}
\]

Thus a $C_\delta/\sqrt n$ guarantee at every prescribed confidence
$1-\delta$ fails for this class when $\delta<p_*$. Within this class,
such a guarantee requires a number of neurons of order $n$, up to a
constant depending on the requested error constant. This conclusion
already precludes $Nq=o(n)$ because $q\ge1$.

Equation (7) is a fixed-positive-time prediction lower bound, already
sufficient to contradict an all-time prediction guarantee. Section 7
proves a separate fitted-endpoint lower bound for sufficiently small fixed
labels. The query law in (8) is specified rather than silently identified
with uniform sphere measure.

## 3. A short-time bound uniform in width and memory order

We first prove deterministic bounds for a width-$k$ closure satisfying
$\|W_0\|_{\rm op}\le M$, where $M$ is a fixed constant. Constants
$C_M$ below depend only on $M$ and the bounded derivatives of tanh.

Since $|f|\le\|w\|_\infty$, the readout equation implies

\[
 \|w(t)\|_\infty
 \le2\int_0^t(y+\|w(s)\|_\infty)\,ds
 \le y(e^{2t}-1).
 \tag{9}
\]

Choose an initial time bound small enough that $e^{2t}-1\le1/2$.
Then $r\in[-3y/2,-y/2]$, so $|r|\le2y$, the clock is strictly
increasing, and $\|w(t)\|_\infty\le C y t$.

Temporarily stop the solution if $\|W(t)\|_{\rm op}=M+1$. Before
that time, (3) and $|\tanh'|\le1$ give

\[
 \frac{\|A(t)e_1-A_0e_1\|_2}{\sqrt k}
 +\frac{\|h^{(1)}(t)-h^{(1)}(0)\|_2}{\sqrt k}
 \le C_M y^2t^2.
 \tag{10}
\]

For example, the first velocity has normalized norm at most
$2|r|\|W\|_{\rm op}\|w\|_2/\sqrt k\le C_M y^2t$;
integrating proves the first bound, and tanh is 1-Lipschitz.

Set $u(\xi)=h^{(1)}(\xi)-h^{(1)}(0)$ on the clock history. It
vanishes on the unit prefix. Because every $q\ge1$ retains constants,
orthogonal projection preserves their pairings and (4) becomes exactly

\[
 W(t)-W_0=-\frac2k\left[
 \left(\int_0^\tau b\,d\xi\right)h^{(1)}(0)^\top
 +\int_0^\tau(\Pi_q b)(\Pi_q u)^\top\,d\xi\right].
 \tag{11}
\]

Since $d\xi=|r|ds$, $\|b(s)\|_2\le C y s\sqrt k$, and
(10) bounds $u$, we have

\[
 \begin{aligned}
 \left\|\int_0^\tau b\,d\xi\right\|_2
   &\le C y^2t^2\sqrt k,\\
 \|b\|_{L^2(0,\tau)}&\le C y^{3/2}t^{3/2}\sqrt k,\\
 \|u\|_{L^2(0,\tau)}&\le C_M y^{5/2}t^{5/2}\sqrt k.
 \end{aligned}
 \tag{12}
\]

For example, the second squared bound is bounded by
$Ck\int_0^t y^3s^2ds$ and the third by
$C_Mk\int_0^t y^5s^4ds$. Cauchy--Schwarz for the matrix integral in
(11), and contraction of orthogonal projection, yield

\[
 \|W(t)-W_0\|_{\rm op}
 \le C y^2t^2+C_M y^4t^4\le C_M y^2t^2.
 \tag{13}
\]

Choose $t_0=t_0(M)>0$ so the right side is less than $1/2$ for
$y\le1$. This excludes the stopped exit, with no dependence on $k$
or $q$. The moment integral representations bound every raw moment on
this interval at each finite order, while $\tau\ge1$. The finite
locally Lipschitz moment ODE therefore continues through $t_0$.

Let $h_0^{(2)}=\tanh(W_0h^{(1)}(0))$. Equations (10)--(13) imply

\[
 \frac{\|h^{(2)}(t)-h_0^{(2)}\|_2}{\sqrt k}
 \le C_M y^2t^2.
 \tag{14}
\]

Subtract $2y h_0^{(2)}$ from the readout velocity:
$\dot w-2y h_0^{(2)}=-2f h^{(2)}+2y(h^{(2)}-h_0^{(2)})$.
Using $|f|\le C y t$ and integrating gives

\[
 \frac{\|w(t)-2yt h_0^{(2)}\|_2}{\sqrt k}
 \le C_M y t^2,
 \qquad 0\le t\le t_0.
 \tag{15}
\]

No estimate on a high physical-time derivative or on endpoint evaluation
of a degree-$q$ polynomial was used. This is why (13)--(15) are uniform
in every memory order.

## 4. The nonlinear query remainder has the sampling scale

Condition on the entire training initialization $(A_0e_1,W_0)$.
Equation (3) changes only the first column of $A$. Hence

\[
 g=A(t)e_2=A_0e_2\sim N(0,I_k)
 \tag{16}
\]

is independent of the entire training path. Given that path, the query
prediction is the odd function

\[
 F_k(t,g)=\frac1k w(t)^\top\tanh(W(t)\tanh g).
 \tag{17}
\]

Write

\[
 K_k(g)=\frac1k(h_0^{(2)})^\top\tanh(W_0\tanh g),\qquad
 R_k(t,g)=F_k(t,g)-2ytK_k(g).
 \tag{18}
\]

The term $2yK_k(g)$ is exactly the initial query prediction velocity.
We now bound the whole remainder in (18), rather than discard higher
terms of a formal Taylor expansion.

The gradient with respect to the unchanged Gaussian vector is

\[
 \nabla_gF_k=
 \frac1k\operatorname{diag}(\operatorname{sech}^2g)W(t)^\top
 \left[w(t)\odot\operatorname{sech}^2(W(t)\tanh g)\right].
 \tag{19}
\]

Consequently, on $\|W_0\|_{\rm op}\le M$,

\[
 \sup_g\|\nabla_gF_k(t,g)\|_2\le\frac{C_Myt}{\sqrt k},
 \qquad
 \sup_g\|\nabla_gR_k(t,g)\|_2\le\frac{C_Myt^2}{\sqrt k}.
 \tag{20}
\]

Here are all terms in the second estimate. Subtracting the gradients in
(18) produces a readout-difference term bounded before division by $k$
by $\|W(t)\|_{\rm op}\|w(t)-2yt h_0^{(2)}\|_2$; a
matrix-difference term bounded by
$2yt\|W(t)-W_0\|_{\rm op}\|h_0^{(2)}\|_2$; and a gate-difference
term bounded by

\[
 2yt\|W_0\|_{\rm op}\|h_0^{(2)}\|_\infty
 \|\tanh''\|_\infty
 \|(W(t)-W_0)\tanh g\|_2.
\]

Equations (13),(15), and $\|\tanh g\|_2\le\sqrt k$ bound these
by $C_Myt^2\sqrt k$, $C_My^3t^3\sqrt k$, and
$C_My^3t^3\sqrt k$, respectively. This proves (20).

For completeness, a smooth odd function $H$ of a standard Gaussian
vector with $\sup\|\nabla H\|_2\le L$ obeys

\[
 \mathbb EH=0,\qquad \mathbb EH^2\le L^2,\qquad
 \mathbb EH^4\le5L^4.
 \tag{21}
\]

The variance inequality used here follows by expanding in orthonormal
multivariate Gaussian Hermite polynomials: if the coefficients are
$c_\alpha$, then the variance is
$\sum_{|\alpha|\ge1}c_\alpha^2$, whereas the mean squared gradient
is $\sum_{|\alpha|\ge1}|\alpha|c_\alpha^2$.
Polynomial approximation in Gaussian Sobolev norm extends the inequality
to the smooth bounded-gradient functions here. Applying it to $H^2$
gives
$\operatorname{Var}(H^2)\le4L^2\mathbb EH^2\le4L^4$,
which proves the fourth-moment bound. In this application the functions
and their squares are bounded at each fixed training state, so the
integrability requirements are satisfied directly.

Applying (21) conditionally to (20) gives

\[
 \begin{aligned}
 \mathbb E_g|R_k(t,g)|^2&\le\frac{C_My^2t^4}{k},\\
 \mathbb E_g|F_k(t,g)|^2&\le\frac{C_My^2t^2}{k},\\
 \mathbb E_g|F_k(t,g)|^4&\le\frac{C_My^4t^4}{k^2}.
 \end{aligned}
 \tag{22}
\]

The crucial first bound is $Ct^4/k$ for the squared remainder. A
width-independent $Ct^4$ bound would not establish a fixed-time
prediction lower bound as $k\to\infty$.

## 5. A nonvanishing initial query fluctuation

For canonical width-$k$ initialization, put
$a=A_0e_1$, $g=A_0e_2$, $h=\tanh a$, $u=\tanh g$ and

\[
 K_k=\frac1k\sum_{j=1}^k
       \tanh((W_0h)_j)\tanh((W_0u)_j).
 \tag{23}
\]

There is a constant $c_0>0$ such that, for all sufficiently large $k$,

\[
 \mathbb E K_k^2\ge\frac{c_0}{k}.
 \tag{24}
\]

To prove this without asserting that the initial rows are independent
unconditionally, condition on $h,u$. The $k$ Gaussian pairs
$((W_0h)_j,(W_0u)_j)$ are then independent, with covariance matrix

\[
 \begin{pmatrix}
 \|h\|_2^2/k&h^\top u/k\\
 h^\top u/k&\|u\|_2^2/k
 \end{pmatrix}.
 \tag{25}
\]

Let $Q=\mathbb E\tanh^2(G)>0$ for $G\sim N(0,1)$.
The independent bounded coordinate pairs $(h_i,u_i)$ imply, by the
law of large numbers, that both diagonal entries tend to $Q$ and the
off-diagonal entry tends to zero. With probability tending to one,
the diagonals lie in $[Q/2,1]$ and the off-diagonal has magnitude at
most $Q/4$. This is a compact set of positive definite covariance
matrices.

For a Gaussian pair $(Z,Z_*)$ with a covariance in this set,
$\operatorname{Var}(\tanh Z\tanh Z_*)$ is continuous and strictly
positive. Positivity holds because the Gaussian density has full support
and the function is nonconstant. Compactness gives a common positive
lower bound $v_0$. Conditional independence of the rows now gives
$\mathbb E[K_k^2\mid h,u]\ge\operatorname{Var}(K_k\mid h,u)
\ge v_0/k$ on that event. Its probability is at least $1/2$ at all
sufficiently large $k$, proving (24).

We will retain the lower bound while restricting to bounded mixer norms.
For a canonical $k\times k$ Gaussian mixer, a $1/4$-net of the unit
sphere has at most $9^k$ points and
$\|W_0\|_{\rm op}\le2\max_{u,v\text{ in net}}|u^\top W_0v|$.
Every displayed bilinear form is $N(0,1/k)$. A Gaussian tail bound and
the union bound therefore give

\[
 \mathbb P\{\|W_0\|_{\rm op}>M\}
 \le2\exp\{-(M^2/8-2\log9)k\}.
 \tag{26}
\]

Fix $M=10$ from now on, so the exponential rate is positive. Since
$|K_k|\le1$, removing an event of this probability changes its second
moment by at most that probability. The $c_0/k$ scale in (24) survives.

## 6. Coupling the two trained widths and obtaining probability

For an arbitrary coupling of the two canonical initializations, let

\[
 \mathcal G=\{\|W_0\|_{\rm op}\le M,
                   \|\widetilde W_0\|_{\rm op}\le M\}.
 \tag{27}
\]

Both mixers have the canonical marginal laws at their respective widths,
so (26) bounds $\mathbb P(\mathcal G^c)$ by
$2e^{-c n}+2e^{-c N}$. Independence of the mixers is unnecessary.
Equations (24) and $|K_N|\le1$ give, after increasing the fixed lower
threshold on $N$ if necessary,

\[
 \|K_N\mathbf1_{\mathcal G}\|_{L^2}\ge\frac{c_1}{\sqrt N}.
 \tag{28}
\]

For each width separately, (22) holds on its own event
$\mathcal G_k=\{\|W_{0,k}\|_{\rm op}\le M\}$ after conditioning on
that width's training initialization. The query first-layer vector is
independent Gaussian under that marginal law. Under an arbitrary coupling,
the other width's good event need not be measurable in this conditioning,
but no such measurability is needed: $\mathbf1_{\mathcal G}\le
\mathbf1_{\mathcal G_k}$ transfers each upper moment bound to the
intersection. The lower bound (28) used only boundedness of $K_N$ and
the marginal probabilities of the discarded events.

Write
$D(t)=\widetilde f_{N,q_N}(t,x_*)-\widehat f_{n,q_n}(t,x_*)$.
The triangle inequality in $L^2$, followed by (18),(22),(28), gives

\[
 \begin{aligned}
 \|D(t)\mathbf1_{\mathcal G}\|_{L^2}
 &\ge 2yt\|K_N\mathbf1_{\mathcal G}\|_{L^2}
 -\|R_N(t)\mathbf1_{\mathcal G}\|_{L^2}
 -\|\widehat f_{n,q_n}(t,x_*)\mathbf1_{\mathcal G}\|_{L^2}\\
 &\ge\frac{yt}{\sqrt N}
       \left(2c_1-Ct-C\sqrt{N/n}\right).
 \end{aligned}
 \tag{29}
\]

Choose $0<t_*\le t_0$ with $Ct_*\le c_1/2$, and choose
$\eta>0$ with $C\sqrt\eta\le c_1/2$. Then the right side of
(29) is at least $c_1yt_*/\sqrt N$ when $N/n\le\eta$.
The fourth-moment bound in (22), and the $L^4$ triangle inequality,
also give

\[
 \mathbb E[|D(t_*)|^4\mathbf1_{\mathcal G}]
 \le\frac{C y^4t_*^4}{N^2}.
 \tag{30}
\]

Apply the elementary second-moment lower-tail inequality to
$Z=|D(t_*)|^2\mathbf1_{\mathcal G}$. Specifically,
splitting its mean over $Z<\tfrac12\mathbb EZ$ and its complement
and applying Cauchy--Schwarz gives

\[
 \mathbb P\{Z\ge\tfrac12\mathbb EZ\}
 \ge\frac{(\mathbb EZ)^2}{4\mathbb EZ^2}.
 \tag{31}
\]

Equations (29)--(30) make the right side a positive constant independent
of both widths, $q$, and $y$. On this event,
$|D(t_*)|\ge c_1yt_*/\sqrt{2N}$. This proves (7), with
$c_y=c_1yt_*/\sqrt2$. Only the two marginal initialization laws entered
the proof, so it holds for every coupling. In particular (6) is covered.
Since the all-time supremum dominates
this one physical time, and $\sqrt{n/N}\to\infty$, (8) follows.

The asymptotic statement was phrased for $N\to\infty$ to use uniform
constants from (24). A sequence of bounded positive widths also cannot
give a vanishing root-$n$ error in this class: along a subsequence with fixed
$N=k$, choose any bounded-mixer event of positive probability on which
$K_k$ is nonzero in $L^2$, and choose a sufficiently small fixed time
using (20)--(22). The narrow output has a nonzero second moment and a
finite fourth moment there, whereas the full query output tends to zero
in probability by (22),(26). This again gives a positive probability of
a fixed nonzero discrepancy. The constants for this finite-width
observation may depend on $k$.

## 7. The fitted unseen-input prediction also has a lower bound

The fixed-time theorem did not require a fitting theorem. For sufficiently
small fixed $y>0$, the established all-order fitting argument also gives
an endpoint version of (7). We use only the deterministic fitting and
continuation part of `paper/proof_alltime.tex`, not its population-limit
or tracking conclusion.

Let the initial training Gram be the positive scalar

\[
 G_k=\frac1k\|h_0^{(2)}\|_2^2\le1.
 \tag{32}
\]

Fix a sufficiently small $\gamma>0$ depending only on tanh, and define
the **training-only** initialization event

\[
 \mathcal T_k=\left\{
 \|W_0\|_{\rm op}\le M,\quad
 \|A_0e_1\|_2/\sqrt k\le2,\quad G_k\ge\gamma\right\}.
 \tag{33}
\]

There are constants $C,c>0$ with
$\mathbb P(\mathcal T_k^c)\le Ce^{-ck}$. Here is a direct verification.
The operator bound is (26). The squared norm of $A_0e_1$ has the
chi-squared moment generating function
$\mathbb E e^{s\|A_0e_1\|_2^2}=(1-2s)^{-k/2}$ for $s<1/2$;
exponential Markov gives an exponentially small upper tail at $4k$.
The empirical variance
$Q_k:=k^{-1}\|\tanh(A_0e_1)\|_2^2$ lies above $Q/2$ except with
exponentially small probability, by the bounded-variable exponential
moment bound. Conditional on the first-layer training vector, the upper
preactivations are independent $N(0,Q_k)$, with $Q_k\ge Q/2$ on
this event. Thus the conditional mean of each squared upper activation
is at least
$b_0=\mathbb E\tanh^2(\sqrt{Q/2}\,G)>0$.
Choose $\gamma=b_0/2$. The same bounded-variable exponential moment
bound gives
$\mathbb P(G_k<\gamma\mid A_0e_1)\le e^{-c k}$ there.
The elementary bound used twice is
$\mathbb P(k^{-1}\sum_i X_i-\mathbb EX_i\le-u)\le e^{-2ku^2}$
for independent $X_i\in[0,1]$, obtained by exponential Markov and
$\mathbb E e^{s(X_i-\mathbb EX_i)}\le e^{s^2/8}$.

The deterministic fitting proof applies on (33): its physical tube,
response bounds, initial readout-Gram lower bound, and residual argument
need only the initialized mixer norm, the initialized training
preactivation norm, and the training Gram gap. Its separately stated
bound on the full first matrix's Frobenius norm is not used in this
fitting subsection. In particular, (33) does not constrain the query
column $A_0e_2$; its independence must be preserved for the argument
below.

For some $y_*>0$ depending only on these fixed bounds, that proof yields,
simultaneously for all $q\ge1$ and $0<y\le y_*$,

\[
 \begin{gathered}
 |r(t)|\le y e^{-\kappa t},\qquad
 \int_0^\infty |r(t)|\,dt\le Cy,\\
 \sup_{t\ge0}\left[
 \frac{\|A(t)e_1-A_0e_1\|_2}{\sqrt k}
 +\|W(t)-W_0\|_F
 +\frac{\|h^{(2)}(t)-h_0^{(2)}\|_2}{\sqrt k}
 \right]\le Cy^2.
 \end{gathered}
 \tag{34}
\]

To specify exactly which quantitative part is being invoked, the fitting
proof gives $\|\dot A\|_F/\sqrt k+\|\dot W\|_F\le Cy|r|$
and $\|\dot h^{(2)}\|_2/\sqrt k\le Cy|r|$ after preserving the
initial Gram gap. Integrating these and its exponential residual bound
gives (34). It also proves convergence of physical parameters and
interpolation. The activation is tanh, the input has unit normalized
norm, the initial readout is zero, and the scalar Gram gap in (33) is
exactly the hypothesis required here. None of these constants depends
on width or order.

The sign of the scalar residual remains negative at every finite time.
Indeed, initially $r=-y<0$; all raw velocities vanish at $r=0$; and the
locally Lipschitz autonomous ODE cannot first reach an equilibrium at a
finite time, by uniqueness backwards from that time. Put

\[
 S=2\int_0^\infty |r(t)|\,dt\le Cy.
 \tag{35}
\]

Integrating the readout equation, whose coefficient is now $2|r|$, gives

\[
 w(\infty)=S h_0^{(2)}+e,
 \qquad \frac{\|e\|_2}{\sqrt k}\le Cy^3,
 \qquad \|w(\infty)\|_\infty\le S\le Cy.
 \tag{36}
\]

The middle bound follows by integrating
$2|r(t)|(h^{(2)}(t)-h_0^{(2)})$ and using (34).
Interpolation at the endpoint gives

\[
 y=\frac1k w(\infty)^\top h^{(2)}(\infty)
   =S G_k+O(y^3).
 \tag{37}
\]

For the error in this equation, the pairing of $S h_0^{(2)}$ with
$h^{(2)}(\infty)-h_0^{(2)}$ is bounded by $Cy\cdot Cy^2$ in
normalized norms, and the pairing with $e$ is at most $Cy^3$ because
$\|h^{(2)}(\infty)\|_2/\sqrt k\le1$. Therefore, on (33),

\[
 \alpha_k:=\frac y{G_k}\in[y,y/\gamma],\qquad
 \frac{\|w(\infty)-\alpha_k h_0^{(2)}\|_2}{\sqrt k}\le Cy^3.
 \tag{38}
\]

Condition again on the training initialization. The independent query
vector $g=A_0e_2$ is unchanged throughout training. Define the actual
fitted query prediction and its remainder by

\[
 F_k(\infty,g)=\frac1k w(\infty)^\top
                  \tanh(W(\infty)\tanh g),\qquad
 R_k^\infty(g)=F_k(\infty,g)-\alpha_kK_k(g).
 \tag{39}
\]

The same three-term gradient subtraction used to prove (20), now using
$\|W(\infty)-W_0\|_{\rm op}\le Cy^2$,
$(38)$, and $\alpha_k\le Cy$, gives

\[
 \sup_g\|\nabla_gR_k^\infty\|_2\le\frac{Cy^3}{\sqrt k},
 \qquad
 \sup_g\|\nabla_gF_k(\infty,g)\|_2\le\frac{Cy}{\sqrt k}.
 \tag{40}
\]

Both functions are odd in $g$. Consequently, on each training event,

\[
 \begin{aligned}
 \mathbb E_g|R_k^\infty|^2&\le Cy^6/k,&
 \mathbb E_g|R_k^\infty|^4&\le Cy^{12}/k^2,\\
 \mathbb E_g|F_k(\infty,g)|^2&\le Cy^2/k,&
 \mathbb E_g|F_k(\infty,g)|^4&\le Cy^4/k^2.
 \end{aligned}
 \tag{41}
\]

For any coupling of the two widths, restrict to
$\mathcal T=\mathcal T_N\cap\mathcal T_n$. Removing its exponentially
small complement from the bounded initial $K_N^2$ preserves (24).
Since $\alpha_N\ge y$, and since the separate upper moment bounds in
(41) transfer to the intersection by monotonicity, exactly the argument
of (29) gives

\[
 \|[\widetilde f_{N,q_N}(\infty,x_*)-
       \widehat f_{n,q_n}(\infty,x_*)]\mathbf1_{\mathcal T}\|_{L^2}
 \ge\frac y{\sqrt N}\left(c-Cy^2-C\sqrt{N/n}\right).
 \tag{42}
\]

Choose one fixed $0<y\le y_*$ small enough that $Cy^2\le c/4$,
and take $N/n$ below a sufficiently small fixed constant. The fourth
moment of the difference on $\mathcal T$ is at most $Cy^4/N^2$ by
(41). Applying (31) once more proves the endpoint theorem:

\[
 \mathbb P\left\{\mathcal T\ \text{and}\quad
 \left|\widetilde f_{N,q_N}(\infty,x_*)-
       \widehat f_{n,q_n}(\infty,x_*)\right|
 \ge\frac{c'_y}{\sqrt N}\right\}\ge p'_*>0.
 \tag{43}
\]

The endpoint values in (43) are well defined on $\mathcal T$, where
both models fit exactly. The probability, discrepancy constants, and
label are independent of width and both orders. This is an actual
fitted-function obstruction, in addition to the fixed-time obstruction.

### A continuum of unseen queries

The point query can be replaced by any fixed probability law $\mu$
supported on the orthogonal sphere

\[
 \mathcal S_\perp=\{\sqrt d\,v:\|v\|_2=1,\ v^\top e_1=0\}.
 \tag{44}
\]

For $d\ge3$, take for example the uniform surface probability on this
sphere; it is a genuine continuum of unseen inputs. This is not the
uniform measure on the full input sphere.

For each fixed unit $v\perp e_1$, the query vector $A_0v$ is
standard Gaussian and independent of $(A_0e_1,W_0)$. Also (3) leaves
$A(t)v=A_0v$ unchanged. Every initial-kernel and conditional query
moment bound above therefore holds with the same constants for
$x=\sqrt d\,v$. Independence between different query directions is
neither true nor needed.

For an arbitrary coupling of the two widths, write the fitted
prediction difference as $D_\infty(x)$ and retain the training event
$\mathcal T$ from (43). Tonelli's theorem and the $L^2$ triangle
inequality on the product of initialization probability and $\mu$ give

\[
 \left(\mathbb E\int |D_\infty(x)|^2
                 \mathbf1_{\mathcal T}\,d\mu(x)\right)^{1/2}
 \ge\frac y{\sqrt N}\left(c-Cy^2-C\sqrt{N/n}\right).
 \tag{45}
\]

Indeed, the leading narrow term is $\alpha_NK_N(x)$ with
$\alpha_N\ge y$; its squared expectation has the same uniform lower
bound at every $x\in\mathcal S_\perp$. The narrow nonlinear remainder
and the full-width output have the same respective product-space upper
bounds $Cy^3/\sqrt N$ and $Cy/\sqrt n$ from (41).

Let $Z=\mathbf1_{\mathcal T}\int|D_\infty(x)|^2d\mu(x)$.
Using the fourth-moment bound in (41) at two possibly dependent queries,
Cauchy--Schwarz gives

\[
 \begin{aligned}
 \mathbb EZ^2
 &=\iint\mathbb E\left[
       |D_\infty(x)|^2|D_\infty(x')|^2
                        \mathbf1_{\mathcal T}\right]d\mu(x)d\mu(x')\\
 &\le\iint
 \sqrt{\mathbb E[|D_\infty(x)|^4\mathbf1_{\mathcal T}]
       \mathbb E[|D_\infty(x')|^4\mathbf1_{\mathcal T}]}
                    d\mu(x)d\mu(x')
 \le\frac{Cy^4}{N^2}.
 \end{aligned}
 \tag{46}
\]

For the same sufficiently small fixed $y$ and sufficiently small
$N/n$ as in (43), (31), (45), and (46) prove

\[
 \mathbb P\left\{\mathcal T\ \text{and}\quad
 \left(\int |D_\infty(x)|^2d\mu(x)\right)^{1/2}
       \ge\frac{c''_y}{\sqrt N}\right\}\ge p''_*>0.
 \tag{47}
\]

The full-time query error with the supremum inside the integral
dominates this fitted-endpoint norm, so it has the same lower bound.
The fixed-positive-time theorem also extends to every such $\mu$ by
the identical product-space argument using (22),(29)--(30). The constants
do not depend on the chosen probability law on $\mathcal S_\perp$.

## 8. What this resolves, and what survives

This theorem establishes an unconditional lower bound for autonomous
neuron reductions retaining the canonical initialization law in the actual
two-tanh-layer model, under every coupling to the original system. It
uses one learning configuration, canonical unclipped Gaussian
initialization, exact zero readout, fixed compatible sphere data, a small
fixed nonzero label, and the same residual-RMS memory equations. Its
observables are prediction at positive physical time and, with sufficiently
small fixed labels, the fitted unseen-input function. All nonlinear
remainder terms and every memory order are covered.

It strengthens the initial sampling-fluctuation obstruction in
`NEURON_SAMPLING_ROUTE.md` into a trained-prediction obstruction, including
the concrete sampler (6). It does not prove that every forward-mark-selected
sampler fails: that broader class need not retain the canonical width-$N$
marginal law used in (24). In particular, the positive initialized
cubature result in `NEURON_REDUCTION_RESULT.md` uses nonuniform masses
and a projected mixer and is outside the theorem's premise, so there
is no contradiction.

The strongest surviving alternative is a source-dependent weighted
selection that deliberately cancels the fluctuation in (23), together
with a compressed mixer preserving the later reverse responses. Such a
construction invalidates the sampling-law premise of this proof. The
separate adjoint-innovation lower bound for forward-only marks cannot be
inserted here to rule that alternative out: a large discarded vector
still need not force a large scalar prediction error.

Accordingly, the broad question remains open: can a response-aware
autonomous $N=o(n)$ neuron model, preferably with $Nq<n$, match the
realized canonical width-$n$ closure with full-time query error
$C_\delta/\sqrt n$? This note proves a negative answer for reductions
retaining the canonical smaller-width initialization law, for fixed query
laws on the orthogonal sphere. It does not resolve the general
source-dependent weighted class, or assert the same lower bound under
uniform surface measure on the full input sphere.

Scientific inputs actually used were the two-layer model, the complete
residual-RMS moment construction and its projection representation in
`paper/main.tex`; the bounded-activation continuation argument in the same
file; the complete initialization, projection-estimate, and all-order
fitting/continuation subsections of `paper/proof_alltime.tex`, together
with its theorem statement in `paper/results.tex`; `docs/notation.qmd`;
and the same-study sampling-route and current
neuron-reduction summaries. No other study, active positive-route work,
experiment, Git operation, or trained-path oracle was used. The canonical
notation, rigorous-math, and research-contract/adversarial-audit skill
instructions were applied. Only this note is owned by this scoped route.
