# Quadratic depth two: the pointed-traffic IDE candidate and its sharp boundary

Status: C1 exact finite algebra and a C2--C3 pointed-traffic **formal
full-state lift** are established; the construction does not pass the
positive-time closure contract, 21 August 2026.

## 1. Claim classification

There is an exact analogue of the linear operator algebra at the level of
formal current fields.  It uses one immutable pointed Gaussian-traffic source,
two current vector fields, one current operator perturbation, and one scalar:

\[
(A(t),u(t),q(t),e(t)).
\]

Whenever a strong solution exists in the displayed domains, it is autonomous,
restartable, width independent in field count, and has no second training
time.  The formulas give the output, tangent kernel, residual, and loss as
current-state expressions.

This is not yet an admissible closure under the frozen contract.  Pointwise
multiplication is unbounded on the traffic Hilbert space, the vector field is
not defined on an open raw domain, and continuity of the \(f,K\) readouts,
positive-time well-posedness, and compact-time width identification are open.
Several tempting claims that saturation or Gaussian extremes settle those
obligations fail audit and are not promoted here.

## 2. Exact finite-width system

Let \(H_n=\mathbb R^n\) with

\[
\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
\]

and let \(G_0=W/\sqrt n\).  The coordinates of \(A_0,u_0\) and the entries of
\(W\) are mutually independent standard Gaussians.  Put

\[
X=u^{\odot2},\quad Z=GX,\quad B=A\odot Z,\quad R=G^*B,
\quad f=\langle A,Z^{\odot2}\rangle_n.
\]

With \((p\otimes r)v=p\langle r,v\rangle_n\), feature ascent is

\[
A'=Z^{\odot2},\qquad u'=4u\odot R,\qquad G'=2B\otimes X.       \tag{2.1}
\]

Equivalently, \(X'=8X\odot R\).  Direct differentiation gives

\[
f'=K,                                                        \tag{2.2}
\]

where

\[
\begin{aligned}
K={}&\langle Z^{\odot4},1\rangle_n\\
 &+4\langle B^{\odot2},1\rangle_n\langle X^{\odot2},1\rangle_n\\
 &+16\langle X\odot R^{\odot2},1\rangle_n.
\end{aligned}                                               \tag{2.3}
\]

Physical full-MSE time multiplies (2.1) by \(2\eta e\), where
\(e=y_\star-f\), and

\[
\dot e=-2\eta eK,\qquad \mathcal L=e^2.                    \tag{2.4}
\]

## 3. The fixed two-sorted traffic source

Use row and column vertex types.  A finite rooted test graph is required to be
connected to its root; it has row marks \(a\), column marks \(u\), and directed
row--column edges decorated by one matrix letter \(w\).  Its root evaluation
is

\[
[\Gamma]_n(k)=n^{-|E|/2}
\sum_{\substack{\phi:V\to[n]\\\phi(r)=k}}
\prod_{(v_R,v_C)\in E}W_{\phi(v_R),\phi(v_C)}
\prod_{v_R}A_{\phi(v_R)}^{\alpha_v}
\prod_{v_C}u_{\phi(v_C)}^{\beta_v}.                         \tag{3.1}
\]

Root gluing is coordinatewise multiplication.  Adding an edge and changing a
column root to a row root is \(C\); reversing this operation is \(C^*\).
Consequently (3.1) evaluates these operations exactly as

\[
p\mapsto G_0p,\qquad p\mapsto G_0^*p,\qquad
(p,r)\mapsto p\odot r.                                     \tag{3.2}
\]

Closing a rooted graph means averaging its root with the extra factor \(1/n\).
For such a connected closed graph define \(\tau(\Gamma)\) by the Gaussian
Wick limit of its normalized evaluation.  Explicitly, pair the matrix edges,
identify the row and column endpoints required by each pairing, and retain
precisely the quotient partitions with

\[
|V/\rho|=1+|E|/2,                                           \tag{3.3}
\]

and multiply the Gaussian moments of the total row and column decorations in
each quotient block.  This determines \(\tau\) without reference to a
positive-time trajectory.  It is positive because it is a limit of normalized
squares.  A doubled-graph Wick expansion gives variance \(o(1)\) for every
fixed finite connected graph polynomial.

More explicitly, for any fixed rooted graph polynomials \(p,r\) of the same
root type,

\[
\langle[p]_n,[r]_n\rangle_n
\xrightarrow{\mathbb P}\tau(p\odot r).                     \tag{3.4}
\]

In the doubled Wick sum, pairings internal to each copy give the product of
the two expectations.  Any pairing connecting the copies removes at least one
free typed vertex without changing the normalization and is \(o(1)\).
Gaussian moments dominate the finite remainder.  This proves (3.4), including
the null-space quotient used below, at each fixed graph order; it is not
uniform as graph degree grows.

After quotienting the null space and completing, one obtains two pointed
traffic Hilbert spaces \(H_R,H_C\).  The source map

\[
C:H_C\longrightarrow H_R
\]

is bounded with \(\|C\|\le2\), and its Hilbert adjoint is the reversed-edge
operation.  This follows from the finite inequality
\(\|G_0v\|_n\le\|G_0\|_{\rm op}\|v\|_n\), fixed-graph
convergence, \(\|G_0\|_{\rm op}\to2\), and the uniform Gaussian moment bounds
needed to remove the exceptional operator-norm event.  Root gluing, by
contrast, is an unbounded densely defined product.  That distinction is
essential.

## 4. The autonomous operator IDE

Conditionally on the existence of a strong trajectory, let
\(q:H_C\to H_R\) be its current trained perturbation and set

\[
G=C+q,\quad X=u^{\odot2},\quad Z=GX,\quad B=A\odot Z,\quad
R=G^*B.                                                      \tag{4.1}
\]

At fixed formal differentiation order, \(q\) is a finite sum of rank-one
graph-word operators.  If a strong positive-time solution has
\(B,X\in C([0,T];L^2)\), equation (4.3) places \(q(t)\) in
\(\mathfrak S_1(H_C,H_R)\).  Neither statement proves existence on that
trace-class space.

For \(p\in H_R,r\in H_C\), write
\((p\otimes r)v=p\langle r,v\rangle_{H_C}\).  The feature-time equation is

\[
\boxed{
A'=Z^{\odot2},\qquad
u'=4u\odot R,\qquad
q'=2B\otimes X.}                                            \tag{4.2}
\]

Its physical version is

\[
\boxed{
\begin{aligned}
\dot A&=2\eta eZ^{\odot2},\\
\dot u&=8\eta e\,u\odot R,\\
\dot q&=4\eta e\,B\otimes X,\\
\dot e&=-2\eta eK,
\end{aligned}}                                              \tag{4.3}
\]

initialized by the row Gaussian mark \(a\), the column Gaussian mark \(u_0\),
\(q(0)=0\), and \(e(0)=y_\star\).  The readouts are

\[
\boxed{
\begin{aligned}
f&=\tau_R(A\odot Z^{\odot2})=y_\star-e,\\
K&=\tau_R(Z^{\odot4})
 +4\tau_R(B^{\odot2})\tau_C(X^{\odot2})
 +16\tau_C(X\odot R^{\odot2}),\\
\mathcal L&=e^2.
\end{aligned}}                                              \tag{4.4}
\]

Because root multiplication is unbounded, (4.4) does not define continuous
readouts on all of \(H_R\oplus H_C\oplus\mathfrak S_1\).  Their natural
finite-moment domain is not open in that topology.

Equations (4.1)--(4.4) use the present state only at points where every
displayed product belongs to the stated Hilbert spaces.  Eliminating \(q\)
gives

\[
q(s)=2\int_0^sB(r)\otimes X(r)\,dr,                         \tag{4.5}
\]

which is exactly the forbidden history representation.  Retaining \(q\)
formally Markovianizes it, but also retains the full current trained operator;
this fact alone is not a compression theorem.

At finite width the kernel function corresponding to \(q_n\) is
\(n(G_n-G_{0,n})\); its integral operator is exactly \(G_n-G_{0,n}\), and
its normalized kernel \(L^2\) norm is the matrix Frobenius norm.  Thus the
field *type* has a width-independent kernel interpretation, but no
positive-time compactness follows from this observation.

### 4.1 Equivalent one-measure Liouville packaging

The broadest one-probability-mass version can also be written exactly at the
algebraic level.  Let \(\mathscr G\) be the countable pointed graph algebra
from Section 3, now generated by the *current* letters \(A,u,G\), and let
\(\mathcal D\) be the derivation determined by (2.1).  For every graph
polynomial \(P\), finite width gives

\[
\frac d{dt}\tau_{n,t}(P)
=2\eta\{y_\star-\tau_{n,t}(P_f)\}\tau_{n,t}(\mathcal DP), \tag{4.6}
\]

where \(P_f\) is the output graph and \(\tau_{n,t}\) denotes its normalized
current evaluation.  Let \(\mathcal S\) be the projective space of positive
normalized pointed-traffic functionals on \(\mathscr G\).  For a cylinder

\[
\Phi(\tau)=\varphi\{\tau(P_1),\ldots,\tau(P_m)\},
\]

define

\[
(\mathcal L\Phi)(\tau)
=2\eta\{y_\star-\tau(P_f)\}
\sum_{r=1}^m\partial_r\varphi\,\tau(\mathcal DP_r).        \tag{4.7}
\]

The formal one-measure IDE is the Liouville equation

\[
\partial_t\nu_t=\mathcal L^*\nu_t,\qquad
\nu_0=\delta_{\tau_{\rm Wick}},\qquad
f(t)=\int_{\mathcal S}\tau(P_f)\,d\nu_t(\tau),\quad
K(t)=\int_{\mathcal S}\tau(\mathcal DP_f)\,d\nu_t(\tau).  \tag{4.8}
\]

A deterministic trajectory would have \(\nu_t=\delta_{\tau_t}\).  Thus
(4.8) is an exact one-time, one-measure packaging of every fixed graph
identity, and its source is the pretrajectory Wick functional of Section 3.
It is not a second training-time construction.

The hierarchy is genuinely unbounded.  With
\(\chi=\langle X^2\rangle\) and coordinate multipliers \(M_A,M_X\), put

\[
T=GM_XG^*M_A.
\]

Then \(Z'=2\chi B+8TZ\), so \(\mathcal D^kZ\) contains the formal word
\(8^kT^kZ\).  At generic finite width the cyclic Krylov family
\(\{Z,TZ,\ldots,T^{n-1}Z\}\) has dimension \(n\).  This observation rules out
a fixed finite truncation of these words; it does not rule out the one
operator field \(T\) or the one full probability state in (4.8).  Rather, it
shows explicitly that either such object stores the entire oriented
hierarchy.

This packaging does not discharge the closure contract.  The derivation
raises homogeneous graph degree by five; multiplication by the physical
residual contributes an additional degree-seven branch.  Hence testing
(4.6) at all orders requires unbounded graph depth and an a-priori
concentration bound at every grade.  The all-polynomial projective topology
is noncompact, while compactifying each coordinate introduces boundary
states on which the finite \(f,K\) readouts are not continuous.  Product
compactness alone also gives no Liouville uniqueness: the elementary
upper-shift hierarchy \(x_k'=x_{k+1}\) has nonzero smooth-flat solutions with
all \(x_k(0)=0\) unless an appropriate quasi-analytic growth class is imposed.
For (4.8), one would still have to prove tightness and uniform integrability
of \(\mathcal DP\) for every \(P\), identify every nonlinear limit, and prove
uniqueness in a named weighted class.  Accordingly, a full pointed measure
is a faithful projective encoding of the open hierarchy, not a proved
positive-time compression.

## 5. Exact gates

At finite width, in the normalized vector/Frobenius Hilbert geometry, the
three components of the feature gradient are

\[
\nabla_Af=Z^2,qquad \nabla_uf=4uR,qquad
\nabla_qf=2B\otimes X.                                      \tag{5.1}
\]

Their squared norms are the three terms in (4.4), proving (2.2).  The phrase
"gradient in \(q\)" below refers to this Hilbert--Schmidt lift; it is not a
gradient for the Banach trace norm.  At the Gaussian source,

\[
\tau_C(X^2)=3,\quad \tau_R(Z^4)=27,\quad
\tau_R(B^2)=3,\quad \tau_C(XR^2)=3.                        \tag{5.2}
\]

Therefore

\[
f(0)=0,qquad K(0)=27+4(3)(3)+16(3)=111.                   \tag{5.3}
\]

Let \(F(s)\) denote the formal width-first feature output generated by
coefficientwise differentiation of (4.2).  Every fixed differentiation
creates only finitely many rooted graphs, so Wick evaluation reproduces the
accepted fixed-order feature jet.  In particular,

\[
F'(0)=111,\quad F^{(3)}(0)=1\,685\,184,\quad
F^{(5)}(0)=77\,400\,633\,120.                              \tag{5.4}
\]

The existing independent recurrence was rerun through order thirteen and its
three finite-order quadratic controls passed.  This checks the algebraic jet;
it does not test positive-time traffic convergence.  Also, at finite width
\(e_n(0)=y_\star-f_n(0)\); the initialization \(e(0)=y_\star\) in (4.3) is
the deterministic width limit.

## 6. What physical loss controls, exactly

Assume \(\eta>0\).  For every finite width, and conditionally for any strong
infinite-dimensional solution of (4.3),

\[
\frac d{dt}e^2=-4\eta e^2K.                                \tag{6.1}
\]

Moreover each of the three current fields obeys the same path estimate.  For
example,

\[
\begin{aligned}
\|\dot q\|_1
 &=4\eta|e|\|B\|_2\|X\|_2\\
 &\le2\eta|e|\sqrt K.
\end{aligned}                                               \tag{6.2}
\]

and the corresponding inequalities for \(A,u\) follow from the first and
third terms of \(K\).  Cauchy--Schwarz and (6.1) give, for \(t\ge t_0\),

\[
\boxed{
\begin{aligned}
\|A(t)-A(t_0)\|_2&\le |e(t_0)|\sqrt{\eta(t-t_0)},\\
\|u(t)-u(t_0)\|_2&\le |e(t_0)|\sqrt{\eta(t-t_0)},\\
\|q(t)-q(t_0)\|_1&\le |e(t_0)|\sqrt{\eta(t-t_0)}.
\end{aligned}}                                              \tag{6.3}
\]

For an infinite-dimensional strong solution, (6.2) shows a posteriori that
\(q(t)-q(t_0)\) is trace class.  It does not construct that solution.

The bounds prove global existence at every finite width: a
finite-dimensional polynomial solution cannot escape while all parameter
blocks stay at finite distance.  They also prove that the trained matrix
perturbation has dimension-free trace-class variation at finite width.

They do **not** control the raw readouts.  A spike

\[
h_n=n^{1/4}\mathbf1_{\{j\}}
\]

vanishes in normalized \(L^2\), while \(n^{-1}\sum_i h_{n,i}^4=1\).
Consequently (6.3) cannot establish uniform integrability of \(Z^4\),
\(A^2Z^2\), \(u^4\), or \(u^2R^2\).

## 7. Scoped diagnostics and compression obstructions

### 7.1 Conventional tensor/Fock lifting is not uniform

Let \(m_n(v\otimes w)=v\odot w\).  In the orthonormal basis
\(\phi_i=\sqrt n e_i\) of \(H_n\),

\[
m_n(\phi_i\otimes\phi_i)=\sqrt n\,\phi_i,qquad
\boxed{\|m_n\|=\sqrt n}.                                   \tag{7.1}
\]

Thus the canonical unweighted Hilbert tensor lift of coordinatewise
multiplication is not uniform in width.  Any broader tensor/Carleman no-go
would require a formally specified class of embeddings and weights; (7.1)
alone does not supply it.  Traffic root gluing avoids a bounded copy map by
remaining an unbounded algebraic operation.

### 7.2 No one-space Banach function algebra contains the source

Suppose a Banach function algebra \(\mathcal B\) has submultiplicative norm,
continuous expectation, and contains a real Gaussian generator \(g\).  Then

\[
\|g\|_{2m}^{2m}=\tau(g^{2m})
\le C\|g^{2m}\|_{\mathcal B}
\le C\|g\|_{\mathcal B}^{2m}.                              \tag{7.2}
\]

Letting \(m\to\infty\) implies \(g\in L^\infty\), a contradiction.  Hence
the linear theorem's locally Lipschitz Banach-ideal proof cannot simply be
reused.  Any raw construction must relax at least one of bounded
multiplication, a single Banach norm containing the Gaussian generator, or
continuity of expectation.

### 7.3 A finite-state hidden-direction witness

At a generic finite state put \(v=X\odot R\).  Choose vectors \(c,q\) with

\[
\langle c,X\rangle=0,\quad \langle c,v\rangle\ne0,\quad
\langle q,B\rangle=0,                                      \tag{7.3}
\]

and

\[
\left\langle q,Z^3+2\langle X^2\rangle A^2Z
+8A\,Gv\right\rangle\ne0.                                \tag{7.4}
\]

For \(H=q\otimes c\), both \((G+\varepsilon H)X=GX\) and
\((G+\varepsilon H)^*B=G^*B\).  Thus \(A,X,Z,B,R,f,K\) are unchanged.  Yet
exact differentiation gives

\[
\begin{aligned}
\left.\frac d{d\varepsilon}\right|_{0}
K'_s(A,X,G+\varepsilon H)
={}&64\langle c,XR\rangle\\
 &{}\times
\left\langle q,Z^3+2\langle X^2\rangle A^2Z+8A\,G(XR)\right\rangle
\ne0.
\end{aligned}                                               \tag{7.5}
\]

The future of these two ambient finite states differs although the displayed
node fields and current \(f,K\) agree.  This is a valid warning against those
particular statistics.  It is not a canonical-flow no-go theorem: the
perturbed state has not been shown reachable from Gaussian initialization or
compatible with the balance-invariant leaf, and no formal class of
edge/spectral/probe summaries is defined here.

### 7.4 Conditional analytic-ODE obstruction

An imported fixed-order Wick theorem for this canonical model gives, with
\(F(s)=\sum_{r\ge0}a_rs^{2r+1}\),

\[
a_r\ge
\frac{9^{r+1}}4(r+2)!\binom{2r+3}{2}.                      \tag{7.5a}
\]

Hence the formal feature series has radius zero.  The retained-diagram proof
of (7.5a) is external to this file and is recorded in the project's current
[Stieltjes research state](../../../stieltjes_conjecture/CURRENT_RESEARCH_STATE.md);
the first three coefficients do not prove it.

Conditioned on that imported theorem, an analytic vector field **and analytic
readout** on an open Banach neighborhood of the initial state, reproducing
all of these jets, are impossible: the analytic ODE theorem would give a
positive-radius readout.  This narrow conclusion does not exclude (4.2) or
force the vector field itself to be nonanalytic.

### 7.5 Output-clock normalization is exact but does not cure tails

At every finite width, wherever \(K>0\), one may use \(\zeta=f\) as the
independent variable.  The exact normalized equations are

\[
\frac{dA}{d\zeta}=\frac{Z^2}{K},\qquad
\frac{du}{d\zeta}=\frac{4uR}{K},\qquad
\frac{dG}{d\zeta}=\frac{2B\otimes X}{K},                   \tag{7.6}
\]

and physical time is reconstructed by

\[
\frac{dt}{d\zeta}
=\frac{1}{2\eta(y_\star-\zeta)K(\zeta)}.                   \tag{7.7}
\]

This is a useful exact reparametrization, not a new orbit.  Any state-space
tail loss at a finite output remains present, while divergence of \(K\) moves
directly into the clock (7.7).

At fixed finite width the output clock does remove finite-feature-time escape
at finite output.  Indeed \(f\) is jointly homogeneous of degree seven.  If
\(E=\|\Theta\|^2\) in the gradient metric, Euler's identity gives

\[
E'=14f,\qquad f'=K,\qquad 49f^2\le EK.                     \tag{7.7a}
\]

If a feature trajectory with \(f(0)=0,K(0)>0\) stayed below a finite
\(F>0\), then \(E(s)\le E(0)+14Fs\), while after any \(s_0>0\),
\[
f'(s)\ge
\frac{49f(s_0)^2}{E(0)+14Fs}.
\]
The right side has divergent integral, a contradiction.  Hence every finite
positive output is reached and (7.6) continues there.  This argument has no
width-uniform tail content.

Division by the scalar \(K\) cannot make a product \(L^p\) topology on the
primitive multiplier variables adequate.  Here is a deterministic spike
witness.  On a probability space take \(G\) to be multiplication by \(g\),
with background \(a=0,u=g=1\).  On two disjoint
sets, each of measure \(\varepsilon/2\), put

\[
u=g=c_\varepsilon,\qquad
a=\pm c_\varepsilon,\qquad c_\varepsilon=\varepsilon^{-\alpha},
\]

using opposite signs on the two sets.  Their outputs cancel, but on the
spikes

\[
X=c^2,\quad Z=c^3,\quad |B|=c^4,\quad |R|=c^5
\]

and

\[
K_\varepsilon
=1-\varepsilon+17\varepsilon c^{12}
  +4\varepsilon c^8-4\varepsilon^2c^8
  +4\varepsilon^2c^{12}.                                   \tag{7.8}
\]

In particular,
\(K_\varepsilon\ge1-\varepsilon+17\varepsilon c^{12}\).
If \(p<12\), choose \(1/12<\alpha<1/p\): the primitive state converges in
\(L^p\), while \(K_\varepsilon\to\infty\).  If \(p\ge12\), choose
\(1/(6p)<\alpha<1/p\): then \(K_\varepsilon\to1\), while

\[
\left\|Z^2/K_\varepsilon\right\|_p^p
\asymp\varepsilon c^{6p}\longrightarrow\infty.             \tag{7.9}
\]

Thus no product \(L^p\) topology on the primitive multiplier-state variables
\((a,u,g)\) makes both this kernel readout and the normalized \(A\)-component
locally bounded at the background state.  The multiplier perturbation is not
trace class on a nonatomic space, so this witness is not directly a no-go for
the \(H_R\oplus H_C\oplus\mathfrak S_1\) traffic state.  It is also not a
proof that the reachable Gaussian orbit forms such a spike.

### 7.6 Marginal moment/Orlicz bootstraps miss adaptive alignment

There is a separate finite-state obstruction to estimates built only from
one-site moments, rearrangement-invariant Orlicz norms, and
\(\|G\|_{\rm op}\).  Write \(G=W/\sqrt n\).  For fixed \(\delta>0\), set

\[
X_j^{(\delta)}
=u_j^2+\delta(W_{1j})_+,\qquad
u_j^{(\delta)}
=\operatorname{sgn}(u_j)\sqrt{X_j^{(\delta)}}.             \tag{7.10}
\]

The perturbation is \(O_{\mathbb P}(\sqrt\delta)\) in empirical sub-Gaussian
norm and has uniformly bounded fixed moments, while

\[
(GX^{(\delta)})_1
=O_{\mathbb P}(1)
+\frac{\delta}{\sqrt n}\sum_jW_{1j}^2\mathbf1_{\{W_{1j}>0\}}
=\left(\frac\delta2+o_{\mathbb P}(1)\right)\sqrt n.
\]

Consequently

\[
\langle(GX^{(\delta)})^4\rangle_n
\ge\left(\frac{\delta^4}{16}+o_{\mathbb P}(1)\right)n.      \tag{7.11}
\]

The transpose has an analogous defect.  Select \(j_*\) measurably from
\(u\) alone, independently of \(A,G\), so that \(1\le X_{j_*}\le2\), and put

\[
A_i^{(\delta)}
=A_i+\delta(W_{ij_*})_+\operatorname{sgn}(Z_i).
\]

Then the marginal perturbation is \(O_{\mathbb P}(\delta)\) in sub-Gaussian
norm, but,
with \(h=\frac12\sqrt{6/\pi}\),

\[
\frac{R_{j_*}^{(\delta)}}{\sqrt n}\to\delta h,\qquad
\lim_{L\to\infty}\liminf_{n\to\infty}
\langle XR^2\mathbf1_{\{|R|>L\}}\rangle_n
\ge\frac{3\delta^2}{2\pi}.                                 \tag{7.12}
\]

These states are adaptively aligned with a Ginibre row or column.  They are
not shown reachable from the Gaussian training trajectory and were not
arranged to preserve the exact global or coordinatewise balance values.
Equations (7.10)--(7.12) therefore rule out a *proof route* based only on
marginal moments/Orlicz bounds and operator norms; they do not refute a
balance-sensitive or correlation-sensitive reachable-state theorem.

### 7.7 One-cell concentration defeats finite normalized additive gauges

There is an exact invariant one-cell subsystem.  Set all entries to zero
except

\[
A_1=a,\qquad u_1=v,\qquad G_{11}=g.
\]

In feature time,

\[
a'=g^2v^4,\qquad v'=4ag^2v^3,\qquad
g'=\frac2n\,agv^4,                                        \tag{7.13}
\]

with \(f_n=n^{-1}ag^2v^4\).  Starting at
\(a=v=\rho>0\) and \(g=\gamma>0\), the exact invariants are

\[
a^2=\frac{v^2+3\rho^2}{4},\qquad
g^2=\gamma^2+\frac{v^2-\rho^2}{2n}.                       \tag{7.14}
\]

Hence \(v'\ge2\gamma^2v^4\).  For \(y_\star>0\), assuming
\(f_n(0)=\gamma^2\rho^5/n<\beta y_\star\), the physical time needed to reach
any fixed fraction \(0<\beta<1\) of the target is at most

\[
t_{\beta,n,\rho,\gamma}
\le\frac{1}{12\eta(1-\beta)y_\star\gamma^2\rho^3}.        \tag{7.15}
\]

Indeed, before this hitting time
\(\dot a\ge2\eta(1-\beta)y_\star\gamma^2
(4a^2-3\rho^2)^2\), and

\[
\int_\rho^\infty\frac{da}{(4a^2-3\rho^2)^2}
=\frac1{\rho^3}
\left\{\frac16-\frac{\sqrt3}{36}\log(2+\sqrt3)\right\}
<\frac1{6\rho^3}.
\]

The invariant formula makes \(f_n\) strictly increasing with \(a\ge\rho\)
and unbounded in feature time, so the crossing used in this estimate exists.

This already defeats continuity of the natural raw topology at the zero
state.  Take \(\gamma=\rho^{-1}\) and let \(n(\rho)\) grow faster than every
power of \(\rho\).  Initially,

\[
\|A\|_2=\|u\|_2=\frac\rho{\sqrt n},\qquad
\|G\|_1=\frac1\rho,qquad
f_n(0)=\frac{\rho^3}{n},\qquad
K_n(0)=\frac{17\rho^4}{n}+\frac{4\rho^8}{n^2}.            \tag{7.15a}
\]

Thus the state converges to zero in
\(L^2\oplus L^2\oplus\mathfrak S_1\), while (7.15) gives
\(f_{n(\rho)}(t)\to y_\star\) for every fixed \(t>0\).  The current state
still converges to zero at such a time.  Indeed, residual sign preservation
gives \(f_n(t)\le y_\star\), whereas (7.14) and
\(f_n\ge\gamma^2v^5/(2n)\) imply

\[
\frac{v(t)}{\sqrt n}
\le (2y_\star)^{1/5}\rho^{2/5}n^{-3/10}\to0,
\]

and then (7.14) gives \(a(t)/\sqrt n\to0\) and \(g(t)\to0\).
Consequently the parameter-only output readout is not continuous on this raw
product space.  Hence no closure using this topology together with a
continuous output readout can identify every convergent finite-state
sequence.  This is a zero-state robustness obstruction, not a statement
about the canonical iid-Gaussian sequence.  Adjoining \(e\) makes the output
readout continuous, but then universal continuous dependence fails: the
limiting initial augmented states agree while their positive-time residual
limits differ.

For the separate fixed-jet cascade, return to the equal-amplitude choice
\(\gamma=\rho\).  Choose \(n(\rho)\) faster than every power of \(\rho\).
Every fixed centered,
fully normalized scalar contraction of the initial one-cell state then tends
to its value at the zero state; likewise, every fixed rooted graph field
vanishes in each fixed normalized \(L^p\) norm.  Raw pinned coordinates,
supremum norms, and unnormalized sums do not vanish.  Nevertheless, (7.15)
implies \(f_{n(\rho)}(t)\to y_\star\) for each \(t>0\): apply (7.15) for every
\(\beta<1\), while residual sign preservation gives \(f_n(t)<y_\star\).
The exact zero state instead stays at output zero.

Define the one-cell feature derivation

\[
\mathcal D
=g^2v^4\partial_a+4ag^2v^3\partial_v
 +\frac{2agv^4}{n}\partial_g.
\]

Then, for every fixed \(m\),

\[
\mathcal D^m f_n(\rho,\rho,\rho)
=\frac{c_m\rho^{7+5m}}n
 +O\!\left(\frac{\rho^{7+5m}}{n^2}\right),\qquad c_m>0,     \tag{7.16}
\]

because \(\mathcal D\) raises total degree by five; at leading order in
\(1/n\), differentiating through \(a'\) and \(v'\) produces only positive
monomials, whereas using \(g'\) introduces one additional factor \(1/n\).
This also gives an induction proof that \(c_m>0\).

Thus any fixed finite list of polynomial gauges can be hidden by choosing the
next scale.

Here is the exact no-go class.  Suppose a closure's initialization topology
is exhausted by finitely many normalized additive coordinates
\(Q_{\ell,n}\), and the contribution of a one-cell mark of amplitude \(\rho\)
to each coordinate is bounded by

\[
|Q_{\ell,n}(\rho)-Q_{\ell,n}(0)|
\le \frac{h_\ell(\rho)}{n^{q_\ell}},\qquad q_\ell>0,       \tag{7.17}
\]

for fixed finite-valued gauges \(h_\ell\).  Assume its current output readout
is continuous and one unique semiflow is required to identify every
finite-width sequence converging in that topology.  Choose \(n(\rho)\) to
dominate every power of \(\rho\) and every
\(h_\ell(\rho)^{1/q_\ell}\).  Then the one-cell and zero sequences have the
same limiting initial state, whereas their positive-time outputs tend to
\(y_\star\) and zero respectively.  Those assumptions are contradictory.

This applies to a finite-gauge defect construction only when its *entire*
declared state satisfies (7.17); merely naming a Young, DiPerna--Majda, or
projective measure does not establish that hypothesis.  It does not rule out
a closure selected only for the canonical iid-Gaussian sequence, because the
one-cell states are not Gaussian initializations.  Raw maxima, a
defect-sensitive coordinate outside (7.17), or a full inverse limit of all
multiscale graph defects also lie outside this no-go.

## 8. Why a cutoff is not yet a theorem

The earlier draft claimed a saturated positive-time theorem.  That claim is
retracted.  No unique cutoff system was specified: one must say exactly which
marks and intermediate products are clipped, define its corresponding
prediction and kernel, and show that it remains the intended gradient flow.
Moreover, applying a bounded Lipschitz scalar function to a graph polynomial
does not produce another finite graph polynomial.  A Nemytskii/functional
calculus on the abstract traffic completion and its finite-width convergence
must first be constructed.  Local Lipschitzness, even after that construction,
would not by itself prove global existence or compare different ambient
widths.

One strong uniform-integrability target for a direct raw cutoff comparison
can at least be stated precisely.
For \(M,T>0\), let

\[
\begin{aligned}
\mathcal T_{M,n}(T)=\sup_{t\le T}\bigl\{&
\langle Z^4\mathbf1_{\{|Z|>M\}}\rangle_n
+\langle B^2\mathbf1_{\{|B|>M\}}\rangle_n\\
&+\langle X^2\mathbf1_{\{X>M\}}\rangle_n
+\langle XR^2\mathbf1_{\{X+|R|>M\}}\rangle_n\bigr\}.
\end{aligned}                                               \tag{8.1}
\]

The corresponding target is

\[
\lim_{M\to\infty}\limsup_{n\to\infty}
\Pr\{\mathcal T_{M,n}(T)>\varepsilon\}=0.                  \tag{8.2}
\]

No available estimate proves (8.2).  Even (8.2) would not by itself promote
(4.3) to a theorem: one would still need state tightness, identification of
all nonlinear graph products, a well-posed raw limiting equation, convergence
of the chosen cutoff flows, and uniqueness.  Tail control and a dynamic
concentration counterexample are therefore two important proof routes, not
an exhaustive logical dichotomy.

## 9. Why the attractive tail no-go is not yet a theorem

At initialization, conditioning a column on \(X_j=x\to\infty\), in the joint
regime specified below, gives the exact leading contraction

\[
\frac{R'_j(0)}{X_j}\longrightarrow 6+9+6+8=29.             \tag{9.1}
\]

The four terms arise from

\[
2\langle B^2\rangle X,\quad G^*Z^3,\quad
2\langle X^2\rangle G^*(A^2Z),\quad
8G^*\{A\,G(XR)\}.                                          \tag{9.2}
\]

The precise lemma used here is the following.  Let \(j=j_n\) be chosen from
\(u\) alone (and hence independently of \(A,G\)), put
\(x_n=X_j(0)\), and assume

\[
x_n\to\infty,\qquad x_n^m/n\to0
\quad\hbox{for every fixed integer }m\ge1,
\]

while the empirical moments of the remaining \(X_k\)'s converge to their
Gaussian values.  Conditional Wick expansion then gives, in probability,

\[
\frac{R_j(0)}{\sqrt{x_n}}\to0,\qquad
\frac1{x_n}\bigl(
2\langle B^2\rangle X_j,\,
(G^*Z^3)_j,\,
2\langle X^2\rangle(G^*(A^2Z))_j,\,
8(G^*\{A\,G(XR)\})_j
\bigr)\to(6,9,6,8).                                       \tag{9.2a}
\]

For example,
\(\mathbb E[G_{ij}Z_i^3\mid X]=3(x_n/n)\langle X^2\rangle\).
The other three contractions are analogous, and their conditional variances
are bounded by \(O(x_n^{-2})+P(x_n)/n\) after division by \(x_n^2\), for a
fixed polynomial \(P\).  The strengthened assumption makes this tend to
zero.  The maximizing column satisfies these hypotheses
because it is selected from \(u\) only and
\(\max_jX_j\sim2\log n\).  This proves the initialization lemma, but no
positive-time statement.

Freezing those leading contractions and writing
\(u_j(0)=L\), \(s=\sigma/L\), \(u_j=LU\), \(R_j=LV\) gives

\[
U_\sigma=4UV,\qquad V_\sigma=29U^2,                       \tag{9.3}
\]

with

\[
U=\sec(2\sqrt{29}\,\sigma),qquad
V=\frac{\sqrt{29}}2\tan(2\sqrt{29}\,\sigma).              \tag{9.4}
\]

This comparison blows up at \(\pi/(4\sqrt{29}L)\), and
\(\max_j|u_j(0)|\sim\sqrt{2\log n}\).  It is therefore a serious mechanism
for a vanishing initial layer.

It is not, by itself, a proof about the network; in fact the displayed
two-variable scaling already drops a leading feedback.  Put

\[
H=G^*D_AG,\qquad P=G^*(A^2Z),\qquad R=HX.
\]

The exact equations include

\[
\begin{aligned}
R'={}&2X\langle B^2\rangle+G^*Z^3
 +2\langle X^2\rangle P+8HD_XR,\\
H'={}&G^*D_{Z^2}G+\frac2n(XP^*+PX^*).                     \tag{9.5}
\end{aligned}
\]

For the tagged scaling define

\[
\xi=X_j/x,\qquad \rho=R_j/\sqrt x,\qquad
\alpha=\sqrt x\,H_{jj}.
\]

Then the scaled \(\rho\) equation contains the omitted term

\[
8\alpha\xi\rho.                                            \tag{9.6}
\]

Although \(\alpha(0)\to0\), equation (9.5) gives
\(\partial_\sigma\alpha(0)\to3\).  Since
\(\rho(\sigma)=29\sigma+o(\sigma)\), (9.6) is
\(696\sigma^2+o(\sigma^2)\), a surviving scaled drift rather than a
negligible error.  Thus (9.3) cannot be justified by freezing the four
initialization contractions; any compensating evolution of the remaining
terms would require a separate proof.

The original \(29\) contraction also ceases to apply when \(X_j\) reaches
\(\sqrt n\), because its contribution to \(\langle X^2\rangle\) is then
order one and the evolved bulk is no longer conditionally Gaussian.  Yet,
under the very heuristic \(R_j^2\asymp X_j\), the accumulated third kernel
term obeys

\[
\int K_j\,ds
\asymp\frac1n\int X^2\frac{dX}{X^{3/2}}
\asymp\frac{X^{3/2}}n,
\]

and becomes order one only at \(X_j\asymp n^{2/3}\).  Thus the approximation
breaks before it can imply a macroscopic output change.

More generally, away from initialization the adverse components of \(G^*B'\)
have no coordinatewise sign; positivity of \(GD_XG^*\) is aggregate only.
The missing theorem must control these terms beyond the bulk-feedback scale.
Freezing the bulk or citing a dyadic continuation without those estimates is
circular.  Conversely, refuting this concentration mechanism requires new
positive-time control, for example a suitable higher-moment or
correlation-sensitive estimate absent from (6.3).

### 9.1 A canonical row-tail theorem conditional on one cavity estimate

Assume \(y_\star>0\).  There is a sharper exact reduction using an extreme
readout coordinate.  Put

\[
Q=\langle X^2\rangle_n,\qquad
H=G D_XG^*,\qquad B=A\odot Z.
\]

In feature time,

\[
Z'=2QB+8HB,                                                \tag{9.7}
\]

and hence, for a row \(i\),

\[
z_i'=(2Q+8H_{ii})a_i z_i+r_i,\qquad
r_i=8\sum_{k\ne i}H_{ik}a_kz_k.                          \tag{9.8}
\]

Moreover,

\[
K=\langle Z^4\rangle_n+4Q\langle B^2\rangle_n
  +16\langle B,HB\rangle_n
\ge \frac{4Q}{n}a_i^2z_i^2,                              \tag{9.9}
\]

because \(H\succeq0\).

The following scalar amplification lemma is deterministic.  Suppose \(L\ge1\)
and

\[
a'=z^2,\qquad z'=c(s)az+r(s),\qquad
a(0)=L,\quad |z(0)|\ge z_*>0,\quad c(s)\ge c_0>0,
\]

and define \(E(s)=\exp\{\int_0^s c(r)a(r)\,dr\}\).  If, up to the first
time \(a=M\),

\[
\sup_s\left|\int_0^sE(r)^{-1}r(r)\,dr\right|
\le\frac{z_*}{2},                                         \tag{9.10}
\]

then the hitting time of every finite \(M>L\) is bounded, uniformly in \(M\),
by

\[
b(L)\le
\frac{\log L+2\beta^{-1/2}}{c_0L},\qquad
\beta=\frac{z_*^2}{4c_0}.                                 \tag{9.11}
\]

Indeed, variation of constants gives
\(|z(s)|\ge(z_*/2)E(s)\).  With \(h(s)=\int_0^sa(r)\,dr\),

\[
a(h)^2\ge L^2+\beta(e^{2c_0h}-1).
\]

Integrating \(ds=dh/a(h)\), and splitting at
\(h=c_0^{-1}\log L\), proves (9.11); the tail integral is at most
\(2/(c_0L\sqrt\beta)\).  We denote this uniform upper bound by \(b(L)\).

At canonical Gaussian initialization, take \(L_n=\sqrt{\log n}\).  With high
probability there are \(n^{1/2-o(1)}\) rows for which

\[
A_i(0)\ge L_n,\qquad |Z_i(0)|\ge z_*;                     \tag{9.12}
\]

conditionally on \(u\), the \(Z_i(0)\) are iid
\(N(0,\langle X^2\rangle_n)\) and independent of \(A_i(0)\).  Write
\(\Theta_n(s)=(A_n(s),u_n(s),G_n(s))\) and
\(F_n(s)=f_n(\Theta_n(s))\) along feature time, let
\(\sigma_n=\inf\{s:F_n(s)=y_\star\}\), and set

\[
M_{i,n}^3=A_i(0)^3+
\frac{3n\{y_\star-f_n(0)\}}{4Q_*},\qquad Q_*=\frac14.     \tag{9.13}
\]

On the \(o(1)\) interval in (9.11), before \(\sigma_n\),
\(\langle u^2\rangle_n\) stays above \(1/2\), because

\[
\langle u^2\rangle_n(s)
=\langle u^2\rangle_n(0)+8\int_0^sF_n(r)\,dr.
\]

Thus \(Q\ge\langle u^2\rangle_n^2\ge Q_*\) and
\(2Q+8H_{ii}\ge1/2\).  If at least one row in (9.12) satisfies (9.10) up to
\(\sigma_n\wedge\tau_{M_{i,n}}\), then on that event (9.11) and (9.9) give

\[
\sigma_n
\le C\frac{\log\log n}{\sqrt{\log n}}
\longrightarrow0.                                        \tag{9.14}
\]

Indeed, if that row first reaches \(M_{i,n}\), then

\[
F_n-f_n(0)
\ge\frac{4Q_*}{n}\int a_i^2a_i'\,ds
=\frac{4Q_*}{3n}\{M_{i,n}^3-A_i(0)^3\}
=y_\star-f_n(0).
\]

The physical consequence would be decisive.  Equip this state with

\[
\|\Theta_n\|_{\mathcal H_n}^2
=\|A_n\|_n^2+\|u_n\|_n^2+\|G_n\|_{\mathrm F}^2.
\]

If
\(\alpha_n(t)=2\eta\int_0^t e_n(r)\,dr\), then
\(\alpha_n(t)\le\sigma_n\), and monotonicity of \(e_n\) gives

\[
e_n(t)\le\frac{\sigma_n}{2\eta t},\qquad
\|\Theta_n(t)-\Theta_n(0)\|_{\mathcal H_n}
\le\sqrt{\sigma_n\{y_\star-f_n(0)\}}.                     \tag{9.15}
\]

Thus (LOO), if it holds with probability tending to one, would imply
\(f_n(t)\to y_\star\) in probability for every \(t>0\), even though the
normalized Hilbert displacement tends to zero.  It would also force

\[
\int_0^tK_n(r)\,dr
\ge\frac1{2\eta}
\log\frac{2\eta t\{y_\star-f_n(0)\}}{\sigma_n}
\longrightarrow\infty.                                   \tag{9.16}
\]

The unproved statement is now precise: with high probability, among the
rows in (9.12), one must satisfy

\[
\sup_{s\le\sigma_n\wedge\tau_{M_{i,n}}}
\left|\int_0^s
\exp\!\left\{-\int_0^r(2Q+8H_{ii})a_i\,d\ell\right\}
r_i(r)\,dr\right|<\frac{|Z_i(0)|}{2}.                     \tag{LOO}
\]

At initialization the cavity is only order one.  Conditional on \(u\) and
the \(i\)-th row \(g_i\),

\[
\mathbb E[r_i(0)^2\mid u,g_i]
=64(n-1)(Qs_i+2d_i^2)=O_{\mathbb P}(1),
\]

where

\[
s_i=\frac1n\sum_jG_{ij}^2X_j^2=O_{\mathbb P}(n^{-1}),
\qquad
d_i=\frac1n\sum_jG_{ij}X_j^2=O_{\mathbb P}(n^{-1}).
\]

What is missing is a dynamic leave-one-row estimate preventing this cavity
from becoming an opposing, sign-correlated field on the vanishing tail set.
Average energy bounds do not imply (LOO).  Consequently (9.14)--(9.16) are a
conditional theorem and a sharply isolated proof obligation, not a canonical
concentration result.  More precisely, if the existence assertion (LOO)
holds with probability tending to one, then (9.14), the positive-time output
limit, the vanishing displacement in (9.15), and the divergence in (9.16)
all hold in probability.

## 10. Numerical boundary-layer audit

A preregistered residual-halving panel through width 512 passed every solver,
invariant, monotonicity, tolerance, and initialization-kernel gate.  Its last
median time ratios were approximately \(0.693\) and \(1.471\).  Hence it
passed neither the stabilization hypothesis nor the monotone-collapse
hypothesis.  The result is formally inconclusive and does not alter Section 9.

## 11. Maximal rigorous verdict

The finite algebra has the following exact **formal full-state lift**:

\[
\boxed{\text{fixed pointed Gaussian traffic source}
+(A,u,q,e)\text{ formal state}+\text{equations (4.3)--(4.4)}.}
\]

Keeping \(q=G-C\) retains the whole current trained operator.  The lift is
therefore nontrivial as a pretrajectory source construction and as a
one-training-time algebraic packaging, but it is not by itself a compression
result.  The finite-state witness (7.5) motivates retaining operator
orientation; it does not prove minimality on the canonical reachable leaf.
The equivalent one-measure equation (4.8) is equally exact on cylinders, but
is projectively the full all-grade traffic hierarchy rather than a
positive-time existence or convergence theorem.

The claim ladder after hostile audit is:

- C1, exact finite algebra and readouts: **proved**;
- C2, explicit connected pointed-Wick source and bounded \(C\): **proved at
  fixed graph order**, subject to the source lemmas stated in Section 3;
- C3, autonomous present-state formulas: **algebraically proved,
  conditionally meaningful on their raw domain**;
- C4--C6, raw well-posedness, no-leakage with a uniform tail, and compact-time
  finite-width identification: **open**;
- C8 and related scoped obstructions: **compression boundaries are proved
  for the raw-product continuity class, finite normalized additive-gauge
  closures, and the canonical unweighted-copy class; marginal/Orlicz bounds
  plus operator norm are ruled out only as a standalone ambient-state
  tail-control route**;
- broad nonexistence of every finite-field or finite-probability-mass
  closure: **not proved**.

For the exact iid-Gaussian sequence, (LOO) is one sufficient concentration
route: if it holds, the loss fits in an \(o(1)\) initial layer; it is not
currently proved.  A distinct candidate regular-flow route through (4.8) and
(8.2) would require all-order uniform integrability, identification, and
weighted uniqueness.  These are proof routes, not a proved exhaustive
dichotomy, and neither closes C4--C6.

Consequently the campaign reaches the protocol's rigorous-obstruction
outcome, but the strong canonical quadratic extension itself remains open.
Calling (4.3) or (4.8) a completed positive-time closure would confuse an
exact formal packaging with the theorem being asked for.
