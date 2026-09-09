# Canonical quadratic concentration theorem

Status: proof draft under final adversarial audit, 21 August 2026.

This note uses feature time (s).  All vector brackets are normalized:

\[
\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w.
\]

## Theorem

Let (A_i,u_j,W_{ij}) be independent standard Gaussians and put
(G=W/\sqrt n), (X=u^{\odot2}), (Z=GX), (B=A\odot Z), and
(R=G^{\mathsf T}B).  Along

\[
A'=Z^{\odot2},\qquad X'=8X\odot R,\qquad
G'=\frac2nBX^{\mathsf T},
\]

write

\[
f_n=\langle A,Z^2\rangle_n,qquad
K_n=f_n'=\langle Z^4\rangle_n+4\langle X^2\rangle_n
\langle B^2\rangle_n+16\langle XR^2\rangle_n.
\]

There is a constant (delta_0>0) such that the feature hitting time

\[
\sigma_n=\inf\{s\ge0:f_n(s)-f_n(0)=\delta_0\}
\]

satisfies

\[
\sigma_n=O_{\mathbb P}((\log n)^{-1/2}).                 \tag{T1}
\]

Consequently, for (y_*>0) and physical MSE flow

\[
\dot\theta=2\eta(y_*-f_n)\theta',
\]

the physical (delta_0)-hitting time tends to zero in probability
(after decreasing (delta_0<y_*/2)).  Hence the finite-width outputs cannot
converge uniformly on any compact physical-time interval to a continuous
readout.  In particular the frozen operator-IDE requirements are mutually
incompatible for the canonical iid-Gaussian sequence.

The proof has three parts: a finite multiscale peeling lemma, an extreme
tagged-column lemma, and a deterministic terminal transport lemma.

## 1. Exact tagged equations

Fix a column (j), and write

\[
x=X_j,\quad g=G_{\cdot j},\quad z=Z-xg,\quad
H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^{\mathsf T}.
\]

Put

\[
h=g^{\mathsf T}D_Ag,qquad \rho=g^{\mathsf T}D_Az,qquad
r=R_j=hx+\rho.
\]

Direct differentiation gives

\[
x'=8xr,                                                   \tag{1.1}
\]

\[
h'=\sum_i g_i^2(z_i+xg_i)^2+
\frac{4x}{n}\sum_iA_i^2g_i(z_i+xg_i),                   \tag{1.2}
\]

and

\[
\rho'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2,         \tag{1.3}
\]

where

\[
\begin{aligned}
\mathcal P={}&\frac2n\sum_iA_i^2z_i^2+2\sum_i g_i^2z_i^2
+2Q_-\sum_iA_i^2g_i^2+8g^{\mathsf T}D_AH_-D_Ag,\\
\mathcal E_0={}&\sum_i g_iz_i^3+2Q_-\sum_iA_i^2g_iz_i
+8g^{\mathsf T}D_AH_-D_Az,\\
\mathcal E_2={}&\frac2n\sum_iA_i^2g_iz_i+\sum_i g_i^3z_i.
\end{aligned}                                             \tag{1.4}
\]

Every summand in (mathcal P) is nonnegative.

There is also an exact signed-source identity.  Since

\[
B'=Z^3+2QA^2Z+8AD_X^{,G}B,qquad
D_X^{,G}:=GD_XG^{\mathsf T},                             \tag{1.5}
\]

and (g'=(2x/n)B),

\[
g(t)^{\mathsf T}B(t)=g(0)^{\mathsf T}B(t)
+2\int_0^t x(s)\langle B(s),B(t)\rangle_n,ds.           \tag{1.6}
\]

Equation (1.6), used as an endpoint identity, is what prevents an
uncontrolled absolute-value estimate of the signed cavity source.

## 2. The outer tagged-column system

Let (L=\sqrt{\log n}), (\tau=Ls), and set

\[
x=L^2U,\qquad H=Lh,\qquad P=\rho/L.
\]

The multiscale lemma below gives, uniformly up to every fixed
polylogarithmic level of (U),

\[
U_\tau=8U(HU+P)+o(1),\qquad H_\tau=3+o(1),\qquad
P_\tau=26U+o(1),                                         \tag{2.1}
\]

including first derivatives with respect to the initial Gaussian score.
The limiting system is therefore

\[
U_\tau=8U(HU+P),\qquad H_\tau=3,\qquad P_\tau=26U.       \tag{2.2}
\]

Its initial large-deviation cost is

\[
I_c(a,b)=\frac a2+\frac{b^2}{6},qquad U(0)=a, P(0)=b.  \tag{2.3}
\]

Indeed (X/L^2) has radial cost (a/2), while, conditionally on the
column-deleted bath, (ho(0)/L) is Gaussian with variance (3/L^2).

Writing (V=HU+P), (2.2) gives

\[
U_\tau=8UV,qquad V_\tau=29U+8HUV\ge29U.                \tag{2.4}
\]

For (U(0)=a>0), (P(0)=b>0), put
(d^2=(29/4)a-b^2).  If (d^2>0), integration of (2.4) yields

\[
T_c(a,b)\le\frac1{4d}
\left(\frac\pi2-\arctan\frac bd\right).                \tag{2.5}
\]

The explicit type ((a,b)=(3/2,1)) has cost (11/12) and the right-hand
side of (2.5) is less than (0.1006).

For comparison, the row outer system is

\[
\alpha_\tau=\zeta^2,qquad \zeta_\tau=14\alpha\zeta,
\qquad I_r(\alpha,zeta)=\frac{\alpha^2}{2}+
\frac{\zeta^2}{6}.                                      \tag{2.6}
\]

Its invariant is (zeta^2-14\alpha^2).  Direct one-dimensional
minimization on (I_r=1) gives

\[
\inf_{I_r\le1}T_r=0.1130518\ldots>0.113.                \tag{2.7}
\]

Thus a fixed column--row pole gap exists.

## 3. Finite multiscale causal peeling

The following lemma is the probabilistic core of the proof.

**Lemma 3.1 (stretched-exponential peeling).**  Fix
(T<0.11), an integer (D), and a sufficiently small
(\varepsilon>0).  Put (R_L=L^\varepsilon).  Stop the flow when either
(int_0^sK_n=\delta_0), a row exits the compact pre-pole region associated
with (2.6), or a column in the early rate window exceeds a prescribed
polylogarithmic level.  Then, with probability (1-o(1)), on
(0\le \tau\le T):

1. every fixed normalized moment needed in (1.2)--(1.5) is bounded;
2. after deleting the initialization columns (X_j(0)>R_L) and the
   initialization row marks (|A_i(0)|+|Z_i^{\rm core}(0)|>R_L), the
   bounded core has an (O(1)) causal propagator;
3. reinserting all intermediate and extreme layers changes every
   reachable scalar contraction and every one- or two-tag arrival phase by
   (O(e^{-cR_L})+O(n^{-c})=o(L^{-D}));
4. uniformly for tagged column types in a compact early window, (2.1)
   holds in (C^0) and in (C^1) with respect to the initial score;
5. uniformly for row types in a compact rate sublevel, (2.6) holds in
   (C^0).

**Proof.**  Only finitely many layers are needed.  The initial Gaussian and
(chi^2_1) tails give, for every fixed (m),

\[
\mathbb E[X^m\mathbf1_{X>R_L}]
\le C_mR_L^{m-1/2}e^{-R_L/2},                            \tag{3.1}
\]

\[
\mathbb E[|N|^m\mathbf1_{|N|>R_L}]
\le C_mR_L^{m-1}e^{-R_L^2/2}.                            \tag{3.2}
\]

Gaussian Bernstein bounds make (3.1)--(3.2) simultaneous for all empirical
tail moments used below.

On the fully truncated core, the derived variables satisfy

\[
|A|+|Z|+X\le R_L^{C_0},\qquad |R|\le C L,                \tag{3.3}
\]

and (|G|_{\rm op}le C).  In the product of normalized (L^2) norms
and the operator norm for (G), direct subtraction of the three finite
ODEs gives a Jacobian bound

\[
\|J_{\rm core}\|\le C(L+R_L^{d_0})                     \tag{3.4}
\]

for a fixed integer (d_0).  Choose
(\varepsilon<1/d_0).  Since (s\le T/L), (3.4) has an (O(1))
propagator.  Notice that (3.4) is a bounded-core estimate; it makes no
operator-norm assertion about (GD_XG^{\mathsf T}) after tail reinsertion.

Condition on the bounded core path.  Every deleted column initially enters
a core row field through (g_jX_j), and every deleted row enters a core
column field through (g_iB_i).  Centered sums have conditional quadratic
variation given by the empirical tail moments in (3.1)--(3.2); their means
are the corresponding truncated scalar moments.  Bernstein's inequality,
followed by a polynomial time net and the core derivative bound (3.4),
therefore bounds every reachable tail field by

\[
C e^{-cR_L}.                                             \tag{3.5}
\]

The same statement holds for two simultaneous deletions.  It is important
that (3.5) concerns the fields reached by the ODE, not the operator norm of
the tail weighted Gram matrix, whose norm is logarithmic.

To remove the provisional conditioning, use first exit.  Reinsert the
layers

\[
R_L<|Y|\le R_L^2, R_L^2<|Y|\le R_L^4,ldots, |Y|=O(L)
\]

one at a time.  Before the top layer, its occupation/tail moment is bounded
by (3.1) or (3.2), while the previously reinserted propagator changes
(3.4) only by (o(1)) in every reachable direction.  For the final
(L)-scale layer, Gaussian large-deviation cells have population
(n^{1-I+o(1)}); (2.5)--(2.7) keep every nonleading cell a fixed distance
from its scalar pole.  A leading column is stopped at the declared
polylogarithmic level.  Its contribution to any normalized bath field is
(n^{-1/2}\operatorname{poly}(L)), and a polylogarithmic family has the
same vanishing bound.  Hence no layer can be the first failure of (3.5).

The identical induction applied to the Fréchet derivative in one initial
score proves the (C^1) assertion.  Self-return terms are not placed in
the error: expanding (1.2)--(1.4) retains them explicitly.  The remaining
contractions converge, by conditional Gaussian quadratic-form bounds, to

\[
H_\tau=3,qquad P_\tau=26U,qquad
\zeta_\tau=14\alpha\zeta.                               \tag{3.6}
\]

The error in (3.6) is (3.5) plus (n^{-c}), uniformly on the time net;
(3.4) fills the gaps.  This proves the lemma. (square)

## 4. A unique extreme phase

Let (T_*) be the minimum pole time of (2.2) over (I_c\le1).
Homogeneity gives

\[
T_c(\lambda^2a,\lambda b)=\lambda^{-1}T_c(a,b).          \tag{4.1}
\]

Consequently a window of width

\[
\epsilon_L=A\frac{\log L}{L^2}                          \tag{4.2}
\]

above (T_*) contains at most (L^{C_A}) candidate columns with high
probability, while a slightly smaller radial window contains a positive
power of (L) candidates.  Lemma 3.1 makes their exact cavity phases
(C^1) functions of their Gaussian scores.  The score derivative is
bounded away from zero: for the limiting tangent, if
(u=\partial_bU), (w=\partial_b(HU+P)), then the triangular variables

\[
q=u/U,qquad v=w-Hu
\]

satisfy (q_\tau>0), (v_\tau=26Uq), and (v(0)=1).
The coarea formula and a two-column cavity therefore give, for sufficiently
large fixed (D),

\[
\Pr\{\hbox{two early phases are within }L^{-D}\}=o(1).   \tag{4.3}
\]

The peeling error in Lemma 3.1 is (o(L^{-D})), so (4.3) transfers to the
full flow.  Call the first column (j_*).  Continue the peeled scalar law
to

\[
x_0=n^{1/3}.                                             \tag{4.4}
\]

The reciprocal (1/U) has a nonzero limiting slope at the pole.  Since
(L^2n^{-1/3}=o(L^{-D})), at the time of (4.4) every competing early
column is still only polylogarithmic.  Moreover

\[
h_{j_*}\ge c/L,qquad \rho_{j_*}\ge-\tfrac12h_{j_*}x_0. \tag{4.5}
\]

The projected response accumulated while (x) grows to (4.4) is
(n^{-1/2}\operatorname{poly}(L)): the exact Riccati asymptotics give
(int x,ds=O(L\log n)), and every cross-column response carries either
a (1/\sqrt n) Gaussian overlap or a (1/n) normalized scalar product.

## 5. Deterministic terminal transport

Let (j_*) be as in (4.4)--(4.5), and stop if the output has already
increased by (delta_0).  All other columns are polylogarithmic.  Hence,
using fixed row moments and delocalization of (g=g_{j_*}),

\[
\mathcal P\ge c,qquad
|\mathcal E_0|\le \sqrt n\,L^C,qquad
|\mathcal E_2|\le n^{-1/2}L^C.                          \tag{5.1}
\]

The exact completion of squares in (1.2) gives

\[
h'\ge-\frac{4x^2}{n^2}\sum_iA_i^4.                     \tag{5.2}
\]

Set (Psi=\rho+hx/2).  At a hypothetical first zero of (Psi),
(r=hx/2) and

\[
\Psi'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2
+\frac x2h'+2h^2x^2.                                    \tag{5.3}
\]

For (x\ge n^{1/3}), the positive last term in (5.3) dominates all three
negative errors in (5.1)--(5.2), up to polylogarithms.  Therefore

\[
r\ge\frac12hx\ge c x/L                                \tag{5.4}
\]

until (x=C_\delta\sqrt{nL}).  Equation (5.2) also shows that (h)
loses only (o(L^{-1})).  The elapsed feature time is at most

\[
\int_{n^{1/3}}^{C_\delta\sqrt{nL}}
\frac{L,dx}{cx^2}=O(Ln^{-1/3}).                         \tag{5.5}
\]

Finally,

\[
(x^2)'=16x^2r,qquad K_n\ge\frac{16}{n}xr^2.
\]

Along the increasing trajectory,

\[
\frac{df_n}{d(x^2)}\ge\frac{r}{nx}\ge\frac{c}{nL}.     \tag{5.6}
\]

Choosing (C_\delta) large enough and integrating (5.6) proves a fixed
increase (delta_0).  The time used before (4.4) is (O(L^{-1})), and
(5.5) is smaller.  This proves (T1).

## 6. Physical-time contradiction

Choose (delta_0<y_*/2).  Since (f_n(0)\to0) in probability, before the
hit (y_*-f_n\ge y_*/3) with high probability.  Thus

\[
t_{\delta_0,n}
=\int_0^{\sigma_n}\frac{ds}{2\eta(y_*-f_n(s))}
\le\frac{3\sigma_n}{2\eta y_*}\xrightarrow{\mathbb P}0. \tag{6.1}
\]

But (f_n(0)\to0) and
(f_n(t_{\delta_0,n})-f_n(0)=\delta_0).  Continuous functions with this
property cannot converge uniformly on a fixed interval to a continuous
limit.  Also

\[
\sup_{0\le s\le\sigma_n}K_n(s)
\ge\frac{\delta_0}{\sigma_n}\xrightarrow{\mathbb P}\infty. \tag{6.2}
\]

This rules out every autonomous finite-field/operator IDE satisfying the
frozen continuous-readout and uniform-identification requirements.  It does
not rule out a generalized post-layer description with a discontinuous
initial trace; that object lies outside the frozen conjecture.
