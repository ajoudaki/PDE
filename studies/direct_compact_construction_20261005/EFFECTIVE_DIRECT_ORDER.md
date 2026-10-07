# Effective direct order for the orthogonal two-hidden-layer tanh flow

2026-10-05. **Scoped analytic result; no experiment.** This note answers one
question: whether the maintained two-hidden-layer tanh population action flow
has a law-only finite autonomous approximation with an explicit
polylogarithmic-in-\(n\) retained size and
\(O(n^{-1/2})\) error, uniformly in physical time and on the whole input
sphere. The approximation may use the data, architecture, initialization law,
\(n\), and its own randomness, but not a realized width-\(n\) network, the
population trajectory, or a table of future responses.

## Bottom line

The full target is **open on the permitted inputs**. There is a direct
law-built autonomous Galerkin hierarchy, and for small fixed labels one can
choose a finite member non-effectively for every requested all-time accuracy.
It preserves the nonlinear motion of both hidden layers. What is missing is an
effective order-to-error modulus on the growing horizon
\(T_n\asymp\log n\), together with an accuracy-certified population
quadrature and precision schedule. Consequently there is presently no proved
retained-storage bound as a function of \(n\) for the requested error.

There is, however, a sharp conditional assembly. If a law-only population
version of the supplied source certificate is proved with

\[
 R_n\le C\lambda^{-1}\log^{3d/2+1}(en)+2m+d+1,                 \tag{1}
\]

then a generic positive moment cubature gives a finite autonomous
coefficient-Galerkin model with

\[
 P=O(R_n^2),\qquad
 S_{\rm real}=O(P(R_n+d+m)+R_n^2)
             =O(R_n^3+(d+m)R_n^2),                         \tag{2}
\]

retained real scalars. For fixed data this is
\(O(\log^{9d/2+3}n)\), and the supplied comparison estimate would give the
desired all-time \(O(n^{-1/2})\) output error. This implication is proved
below, but its source premise is not.

The sharper source-space count

\[
 O(R_n^2)=O\!\left(\lambda^{-2}\log^{3d+2}(en)\right)         \tag{3}
\]

requires \(P=O(R_n)\), or an equivalent non-diagonal sparsified metric. The
permitted dense-realization construction obtains that cardinality from the
realized width-\(n\) coordinates. No law-only, source-compatible, effective
\(P=O(R_n)\) construction with the required dynamic error and bit bounds is
proved here or in the permitted inputs. Thus matching
\(O(\log^{3d+2}n)\) is conditional, not a current result.

The failure is not an impossibility theorem. It defeats the available direct
analytic, cubature, and Galerkin proofs, not every admissible finite
autonomous approximation.

## 1. Contract and canonical flow

Let \(u_a=x_a/\sqrt d\), with
\(u_a^\top u_b=\mathbf 1_{\{a=b\}}\), and let
\(u\in S^{d-1}\) be a passive query. On the two population spaces write

\[
\begin{aligned}
 H^{(1)}(u)&=\tanh(w\cdot u),&
 Z^{(2)}(u)&=A H^{(1)}(u),&
 H^{(2)}(u)&=\tanh Z^{(2)}(u),\\
 \Delta^{(2)}(u)&=c\,[1-H^{(2)}(u)^2],&
 Q(u)&=A^*\Delta^{(2)}(u),&
 f(u)&=\mathbb E_2[cH^{(2)}(u)].
\end{aligned}                                                \tag{4}
\]

Here \(A=A_0+K\), \(K\) is Hilbert--Schmidt, and \(A_0^*\) is the
actual adjoint of the same initialized Gaussian action. Initially
\(w=g\sim\mathcal N(0,I_d)\), \(K=0\), and \(c=0\). For the unhalved
sum loss, \(r_a=f(u_a)-y_a\), and fixed positive mobilities, the flow is

\[
\begin{aligned}
 \dot w&=-2\kappa_1\sum_a r_a[1-H^{(1)}(u_a)^2]Q(u_a)u_a,\\
 \dot K&=-2\kappa_2\sum_a r_a\Delta^{(2)}(u_a)\otimes
                                      H^{(1)}(u_a),\\
 \dot c&=-2\kappa_3\sum_a r_aH^{(2)}(u_a).
\end{aligned}                                                \tag{5}
\]

This is the maintained global orthogonal-data action flow. Changing from the
sum loss to the mean loss only rescales physical time by the fixed factor
\(m\).

The requested approximation must have a finite saved scalar state, an
autonomous restart map, and law-only initialization. Its prediction error is

\[
 \sup_{t\in[0,\infty]}\sup_{u\in S^{d-1}}|f_C(t,u)-f(t,u)|.  \tag{6}
\]

Real-coordinate storage and bit storage are distinct. A finite list of
arbitrary exact reals is not by itself an effective construction.

## 2. Small labels reduce all time to a logarithmic horizon

This reduction is independent of a spectral representation. Put

\[
 q_1=\mathbb E\tanh^2G,qquad
 q_2=\mathbb E\tanh^2(\sqrt{q_1}G),qquad G\sim\mathcal N(0,1).
\]

For the standard initialized middle variance, orthogonality and oddness give

\[
 \mathbb E_2[H^{(2)}(0,u_a)H^{(2)}(0,u_b)]
      =q_2\mathbf 1_{\{a=b\}},\qquad q_2>0.                \tag{7}
\]

Indeed the lower initial features are orthogonal with common squared norm
\(q_1\), and their initialized forward images are independent
\(\mathcal N(0,q_1)\) variables. Let \(g_*=\kappa_3q_2/2\). Constants below
may depend on the fixed \(m,d,\kappa_\ell\) and initialized action bound, but
not on time.

### Proposition 1: fitting and a uniform predictor tail

There is \(c_*>0\) such that, if
\(Y=\lVert y\rVert_2\le c_*g_*\), then (5) satisfies

\[
 \lVert r(t)\rVert_2\le Y e^{-2g_*t},\qquad
 \sup_{u\in S^{d-1}}|f(\infty,u)-f(t,u)|
       \le C Yg_*^{-1/2}e^{-2g_*t}.                       \tag{8}
\]

The same statement holds uniformly for every sufficiently accurate finite
Galerkin model below.

**Proof.** Stop when the top-feature Gram has smallest eigenvalue \(q_2/2\).
The tangent Gram then dominates \(g_*I\), so
\(\dot r=-2\mathcal K r\) gives
\(-\dot\rho\ge2g_*\rho\), where \(\rho=\lVert r\rVert_2\).
The gradient-flow energy identity gives, in the inverse-mobility parameter
norm,

\[
 \lVert\dot\theta\rVert^2=2\rho(-\dot\rho),
 \qquad
 \int_s^\infty\lVert\dot\theta\rVert,dt
       \le \rho(s)/\sqrt{g_*}.                            \tag{9}
\]

In particular \(\lVert c\rVert_2\le Y/\sqrt{g_*}\). Every hidden-block
velocity contains both a residual and a backward field, hence is bounded by
\(C\rho Y/\sqrt{g_*}\). Since
\(\int_0^\infty\rho\le Y/(2g_*)\), the two hidden blocks, and therefore all
training top features, move by at most
\(CY^2/g_*^{3/2}\). If \(Y\le c_*g_*\), this is a sufficiently small
fraction of the initial feature singular value \(\sqrt{q_2}\). The stopped
Gram condition therefore cannot fail. This closes the decay estimate.

On this bounded tube the forward map from \((w,K,c)\) to \(f(u)\) is
Lipschitz uniformly in \(u\): tanh is 1-Lipschitz, \(A_0+K\) is bounded,
and all features are bounded. Apply this to (9), let the Cauchy parameter path
converge, and use the residual decay. This proves (8). The proof for a finite
Galerkin model is identical once its initialized top Gram and action bound
have the same fixed margins. \(\square\)

Thus accuracy \(\varepsilon\) on all time follows from accuracy on

\[
 T_\varepsilon=Cg_*^{-1}\log(C/\varepsilon).              \tag{10}
\]

For \(\varepsilon=n^{-1/2}\), the relevant horizon is \(O(\log n)\), not a
fixed interval.

### The feature-learning mechanism is retained

This small-label regime is not lazy. At initialization let

\[
 h_a=\tanh G_a,\quad \Xi_a=A_0h_a,\quad H_a=\tanh\Xi_a,
 \quad S=\sum_b y_bH_b,quad U_a=S[1-H_a^2].              \tag{11}
\]

Then \(\dot c(0)=2\kappa_3S\), while \(\dot w(0)=\dot K(0)=0\), and direct
differentiation of (5) gives

\[
 \ddot K(0)=4\kappa_2\kappa_3
               \sum_a y_aU_a\otimes h_a,                 \tag{12}
\]

\[
 \ddot Z^{(1)}(0,u_a)=4\kappa_1\kappa_3y_a
 (1-\tanh^2G_a)A_0^*U_a.                                 \tag{13}
\]

For every \(a\) with \(y_a\ne0\), \(U_a\ne0\). Moreover

\[
 \mathbb E_1[h_aA_0^*U_a]
   =\mathbb E_2[\Xi_aU_a]
   =y_a\mathbb E[\Xi\tanh(\Xi)(1-\tanh^2\Xi)]\ne0,       \tag{14}
\]

because all cross terms vanish by independence and oddness. Hence the first
hidden feature moves at order \(t^2\). For the second hidden feature put
\(P_a=A_0^*U_a\), \(V_a=(1-\tanh^2G_a)^2P_a\), and

\[
 R_a=\kappa_2q_1U_a+\kappa_1A_0V_a.
\]

Adjunction gives

\[
 \mathbb E_2[U_aR_a]
 =\kappa_2q_1\lVert U_a\rVert_2^2
  +\kappa_1\mathbb E_1[(1-\tanh^2G_a)^2P_a^2]>0.         \tag{15}
\]

Thus \(R_a\ne0\), and the second hidden feature also moves at order
\(t^2\). Tanh has positive best-affine error on each nondegenerate initial
Gaussian preactivation law; continuity keeps it positive for a short time.
An approximation converging in the paired hidden \(L^2\) observations
therefore preserves both hidden motions and nonaffinity for all sufficiently
large orders. This is a mechanism statement, not merely a moving readout.

## 3. A law-built autonomous Galerkin hierarchy

The following is the strongest unconditional construction obtained here. It
has convergence but no effective order.

The comparison is most transparent in the exact tanh clock. Define

\[
 \Psi(z)=\int_0^z\frac{dq}{1-\tanh^2q}
        =\frac z2+\frac{\sinh(2z)}4,
 \qquad
 J(x,g)=\Psi^{-1}(\Psi(g)+x).                            \tag{16}
\]

Then \(\partial_xJ(x,g)=1-\tanh^2J(x,g)\le1\). Put
\(G_a=g\cdot u_a\) and

\[
 X_a(t)=\Psi(w(t)\cdot u_a)-\Psi(G_a).
\]

Because the data directions are orthonormal and \(\dot w\) lies in their
span,

\[
\begin{aligned}
 w(t)\cdot u
 &=g\cdot u+\sum_{a=1}^m(u\cdot u_a)
       [J(X_a(t),G_a)-G_a],\\
 \dot X_a&=-2\kappa_1r_aQ(u_a).                         \tag{17}
\end{aligned}
\]

The second identity is the point of the clock: the lower tanh gate cancels.
Consequently subtraction never multiplies a gate difference by an unbounded
reverse field.

Choose nested finite lists of bounded initialized observable words on the two
populations. The grammar contains rational affine combinations, bounded
coordinate functions, bounded products, and both orientations of the same
initialized action. It also contains bounded truncations of the Gaussian
coordinates. Let \(\psi_{\ell,N}\) be the raw list, let

\[
 G_{\ell,N}=\mathbb E_\ell[\psi_{\ell,N}\psi_{\ell,N}^\top],
 \qquad
 b_{\ell,N}=(G_{\ell,N}+\eta_NI)^{-1/2}\psi_{\ell,N},
 \qquad \eta_N\downarrow0,                                \tag{18}
\]

and let \(U_{\ell,N}a=b_{\ell,N}^\top a\). Then
\(Q_{\ell,N}=U_{\ell,N}U_{\ell,N}^*\) is a positive contraction and
converges strongly to the identity on the initialized observable space. The
finite initialized action matrix is

\[
 D_N=U_{2,N}^*A_0U_{1,N}.                                 \tag{19}
\]

Every object in (18)--(19) is determined by one finite canonical Gaussian
program. In particular the forward and reverse calls use the same action;
there is no independent adjoint matrix.

For readability suppress \(N\), let the feature dimensions be \(R_1,R_2\),
and save the two joint mark populations

\[
 \Gamma_1=\operatorname{Law}(b_1,g,X_1,\ldots,X_m),\qquad
 \Gamma_2=\operatorname{Law}(b_2,c),qquad
 M\in\mathbb R^{R_2\times R_1}.                           \tag{20}
\]

Initially \(X_a=0,c=0,M=D_N\). For every query \(u\), define

\[
\begin{aligned}
 z_1(u)&=g\cdot u+\sum_a(u\cdot u_a)
       [J(X_a,g\cdot u_a)-g\cdot u_a],\\
 h_1(u)&=\tanh z_1(u),&a(u)&=\mathbb E_1[b_1h_1(u)],\\
 h_2(u)&=\tanh(b_2^\top Ma(u)),&f_N(u)&=\mathbb E_2[ch_2(u)],\\
 d(u)&=\mathbb E_2[b_2c(1-h_2(u)^2)],&q(u)&=b_1^\top M^\top d(u).
\end{aligned}                                                \tag{21}
\]

With \(r_{N,a}=f_N(u_a)-y_a\), evolve

\[
\begin{aligned}
 \dot X_a&=-2\kappa_1r_{N,a}q(u_a),\qquad 1\le a\le m,\\
 \dot c&=-2\kappa_3\sum_a r_{N,a}h_2(u_a),\\
 \dot M&=-2\kappa_2\sum_a r_{N,a}d(u_a)a(u_a)^\top.
\end{aligned}                                                \tag{22}
\]

These equations use only the current saved state, fixed data, and initialized
marks. They are autonomous and restart from (20). Reconstructing \(w\) by
(17) turns the clock equation back into the first line of (5); the \(M\) and
\(c\) equations are the exact coefficient-action and readout gradient
equations. Thus the usual loss identity still holds, and all hidden blocks
move.

### Proposition 2: compact-horizon convergence

For every fixed \(T<\infty\), the exact population systems (20)--(22) can be
chosen so that

\[
 \sup_{t\le T}\sup_{u\in S^{d-1}}|f_N(t,u)-f(t,u)|\longrightarrow0.             \tag{23}
\]

The first- and second-hidden observations also converge in \(L^2\), uniformly
over the same time/query set.

**Proof.** On the common carrier put
\(B_N=Q_{2,N}A_0Q_{1,N}\) and lift (22) to the action
\(A_N=B_N+K_N\), where initially \(K_N=0\) and

\[
 \dot K_N=-2\kappa_2\sum_a r_{N,a}
             Q_{2,N}\Delta_N^{(2)}(u_a)
             \otimes Q_{1,N}H_N^{(1)}(u_a).
\]

On every fixed horizon, loss monotonicity bounds the residuals. The readout
equation bounds \(c,c_N\) pointwise; the rank-one equation bounds \(K,K_N\)
in Hilbert--Schmidt norm. Hence \(A,A_N\) are uniformly bounded. The exact
target sets

\[
 \{H^{(1)}(t,u):t\le T,u\in S^{d-1}\},\qquad
 \{\Delta^{(2)}(t,u_a):t\le T,1\le a\le m\}
\]

are compact in their respective \(L^2\) spaces. The curve \(\dot K(t)\) is
compact in Hilbert--Schmidt norm. Strong convergence of uniformly bounded
operators is uniform on compact sets, so

\[
\begin{aligned}
 \epsilon_N(T)={}&\sup_{t,u}\lVert(B_N-A_0)H^{(1)}(t,u)\rVert_2\\
 &+\max_a\sup_t\lVert(B_N^*-A_0^*)\Delta^{(2)}(t,u_a)\rVert_2\\
 &+\sup_t\lVert Q_{2,N}\dot K(t)Q_{1,N}-\dot K(t)\rVert_{\rm HS}
 \longrightarrow0.                                      \tag{24}
\end{aligned}
\]

Let \(e_N\) be the sum of the \(m\) clock \(L^2\) errors, learned-action
Hilbert--Schmidt error, and readout \(L^2\) error. By (16),

\[
 \lVert J(X_a,G_a)-J(\widetilde X_a,G_a)\rVert_2
 \le\lVert X_a-\widetilde X_a\rVert_2.
\]

Therefore (17) makes the passive-query first features uniformly Lipschitz in
the clock state. Forward action subtraction, the bounded Lipschitz tanh gates,
and the pointwise readout bound control every other state difference. Most
importantly, subtracting the two clock equations compares
\(A^*\Delta^{(2)}(u_a)\) directly. There is no product of a gate difference
with that merely \(L^2\) reverse field. The rank-one inequality then gives

\[
 D^+e_N(t)\le C_T[e_N(t)+\epsilon_N(T)].                 \tag{25}
\]

Since the initial compared clock, learned-action, and readout errors vanish,
Gronwall gives \(\sup_{t\le T}e_N(t)\le C_T\epsilon_N(T)\to0\).
The same forward estimates, uniformly on the compact query sphere, give (23)
and the hidden-observation convergence. \(\square\)

For fixed \(N\), approximate the finite-dimensional joint mark laws in (20)
by positive atomic laws and compute the initialized objects (18)--(19) by
finite Gaussian integration.
The finite ODE is locally Lipschitz on bounded sets, and its energy bounds
prevent finite-time escape. Coupling and Gronwall therefore make these atomic
systems converge to (22). This produces a genuinely finite, law-built,
autonomous scalar ODE. It uses neither a dense neural realization nor the
target path.

Combining Propositions 1--2 gives a **non-effective all-time diagonal**: for
every \(\varepsilon>0\), first choose (10), then some sufficiently large
dictionary order and sufficiently fine initialization/population quadrature.
The resulting finite autonomous model has error at most \(C\varepsilon\) in
(6) and retains hidden feature learning. This proves finite existence at every
accuracy, but it does not give an admissible explicit \(N(n)\), \(P(n)\), or
precision. Compact-horizon strong convergence cannot be applied directly to
the growing horizons \(T_n\).

## 4. Exact storage accounting at rank \(R\)

Let \(R=\max(R_1,R_2)\) and use \(P_1,P_2\le P\) quadrature nodes. Storing
the fixed marks and weights, the \(m\) moving clocks and \(c\), the coefficient
matrix \(M\), and the fixed data costs

\[
 S_{\rm real}=O\bigl(P(R+d+m)+R^2+m(d+1)\bigr).           \tag{26}
\]

real scalars. This coefficient form is smaller than storing a full
\(P_2\)-by-\(P_1\) node-to-node action, which costs \(O(P^2)\).

For clarity, three different node counts must not be conflated.

| finite realization | node count | retained real scalars |
|---|---:|---:|
| arbitrary fixed quadrature | \(P\) | \(O(P(R+d+m)+R^2)\) |
| generic positive moment cubature | \(P=O(R^2)\) | \(O(R^3+(d+m)R^2)\) |
| source-compatible linear-size sparsification | \(P=O(R)\) | \(O(R^2+(d+m)R)\) |

The \(P=O(R^2)\) support bound in the middle row is proved for a specified
finite moment certificate. Using it at the effective rank (1) is conditional
only because the dynamic direct-source certificate is missing. The last row,
\(P=O(R)\), is the additional unproved sparsification needed for the sharper
storage exponent.

Here is the proved generic cubature count. On a bounded/truncated source
domain, collect the constant and all products of the \(R\) source coordinates.
There are at most

\[
 p=1+R+R(R+1)/2.                                          \tag{27}
\]

real moment functions. Quantize their bounded joint range into finitely many
small cubes, choose one source point from every occupied cell, and give it the
cell mass. This approximates all \(p\) moments to the chosen tolerance. The
resulting moment vector is a convex combination of finitely many vectors in
\(\mathbb R^p\). If a convex combination uses more than \(p+1\) points, their
augmented vectors \((1,v_i)\) are linearly dependent; moving the weights along
that dependence until one becomes zero preserves the combination. Iteration
leaves at most \(p+1=O(R^2)\) positive nodes. Gaussian/source tails can first
be truncated and charged to the moment tolerance. This is an elementary
approximate Tchakaloff construction and uses the law, not a dense network.

What it proves is a finite law-built moment model at a specified finite
dictionary. By itself it supplies no dynamic error: the finite source list
must approximate every forward and reverse field used on the relevant
trajectory, with the same coefficients on the population and cubature sides.
That is the missing source certificate in the next section.

If (1) were available with such a certificate, (26)--(27) would give

\[
 S_{\rm real}\le
 C\lambda^{-3}\log^{9d/2+3}(en)+O((m+d)^3).              \tag{28}
\]

A full node-to-node realization would instead give
\(O(R_n^4)=O(\lambda^{-4}\log^{6d+4}(en))\). To obtain the sharper
\(O(\lambda^{-2}\log^{3d+2}(en))\) count, one needs the last row of the
table. The general-vector sparsification used in the supplied storage result
does give \(O(R)\) selected coordinates after a finite identity decomposition,
but there it selects from the forbidden dense realization and uses a
non-diagonal metric plus a corrected readout. Turning it into a law-only,
effective, source-compatible initializer is an additional theorem, not a
change of bookkeeping.

## 5. The conditional explicit assembly

The exact missing statement can be isolated as follows.

### Effective direct-source certificate

For \(\epsilon_n=n^{-1}\) and
\(T_n=C\lambda^{-1}\log(en)\), construct from the law and initial Gaussian
action alone:

1. finite initialized source maps \(\Psi_{\ell,n}\) of ranks satisfying
   (1), including constants, initialized training features, first weights,
   and both members of every required forward/reverse action pair;
2. coefficients, computed without the target path, which approximate all
   forward and backward training sources and passive whole-sphere sources on
   \([0,T_n]\) to \(\epsilon_n\) in one cubature-compatible weighted norm;
3. a population carrier cutoff \(M_n\le1+Cs\sqrt{\log(en)}\),
   \(s=Y/\lambda\), with all discarded tails at most \(C\epsilon_n\);
4. computable same-population Grams and cross-action contractions, with a
   finite positive cubature or sparsified metric satisfying the same source
   errors; and
5. explicit conditioning, arithmetic precision, and work bounds.

If these five items hold, the autonomous comparison uses no future quantity.
The matched readout--residual estimate supplied in
`ERROR_PREFACTOR_GEOMETRIC_ROUTE.md` has the raw form

\[
 \sup_{t\le T_n,u}|f_C-f|
 \le C\lambda^{-1/2}\epsilon_n
             \exp\{Cs(1+M_n)\}.                          \tag{29}
\]

Since \(s\le c\), Young's inequality gives

\[
 n^{-1}\exp(Cs^2\sqrt{\log(en)})\le Cn^{-1/2}.           \tag{30}
\]

Proposition 1 and the corresponding compressed fitting estimate give a tail
\(Ce^{-c\lambda T_n}\le Cn^{-1}\). Hence

\[
 \sup_{t\ge0,u}|f_C(t,u)-f(t,u)|
       \le C\lambda^{-1/2}n^{-1/2}.                       \tag{31}
\]

Generic positive cubature then gives (28); a proved \(P=O(R_n)\)
sparsification would give (3). Equations (28)--(31) are a complete
implication, but not an unconditional theorem because the direct-source
certificate is open.

The supplied spherical source route establishes the analogous rank for
coordinates of a realized finite network. Its coefficient construction uses
finite initial derivatives, but its pole-safe complex tube is obtained after
bounding the largest realized coordinate. It does not establish items 2--5
for the population law. Taking a fixed-program width limit does not repair
this: the required program order grows with \(n\), whereas the maintained
Gaussian-action theorem is fixed-program.

## 6. Why direct population analyticity does not supply the missing rate

The most tempting shortcut is false. A population tanh field generally has
no nonzero complex \(L^2\) strip.

### Lemma 3: the complex-tanh pole obstruction

Let \((G,H)\) be a nondegenerate centered Gaussian vector. For every real
\(s\ne0\),

\[
                 \mathbb E|\tanh(G+isH)|^2=\infty.       \tag{32}
\]

**Proof.** Tanh has a pole at \(z_0=i\pi/2\). With
\(\zeta=z-z_0\),

\[
 \cosh(z_0+\zeta)=i\zeta+O(\zeta^3),\qquad
 \sinh(z_0+\zeta)=i+O(\zeta^2),
\]

so there are \(c,r>0\) such that
\(|\tanh(z_0+\zeta)|^2\ge c/|\zeta|^2\) for
\(0<|\zeta|<r\). Set

\[
 x=G,\qquad y=sH-\pi/2.
\]

If \(p_{G,H}\) is the joint Gaussian density, the \((x,y)\)-density is
\[
 \widetilde p_s(x,y)=|s|^{-1}
 p_{G,H}\!\left(x,\frac{y+\pi/2}{s}\right).
\]
It is continuous and strictly positive at \((0,0)\). After reducing \(r\)
if necessary, \(\widetilde p_s\ge c_s>0\) on the disk of radius \(r\).
Thus

\[
\begin{aligned}
 \mathbb E|\tanh(G+isH)|^2
 &\ge c_s\int_{x^2+y^2<r^2}\frac{dx\,dy}{x^2+y^2}\\
 &=2\pi c_s\int_0^r\frac{d\rho}{\rho}=\infty.
\end{aligned}                                             \tag{33}
\]

This proves (32). \(\square\)

The same calculation applies to a complexified query direction whenever
the real and imaginary Gaussian projections are nondegenerate. A finite
width has only finitely many coordinates; on the event that their carrier
maximum is \(O(\sqrt{\log n})\), a strip of width
\(O(1/\sqrt{\log n})\) avoids every pole. An infinite Gaussian population
has unbounded essential supremum, and (32) shows that this finite-coordinate
argument cannot simply be passed to the limit.

Real derivatives may still obey Gevrey rather than analytic bounds. For the
toy field \(F(t)=\tanh(G+tH)\), Cauchy's estimate on the scalar strip
\(|\operatorname{Im}z|\le\pi/4\) and Gaussian moments give

\[
 \lVert F^{(k)}(t)\rVert_2
 \le k!(4/\pi)^k(\mathbb E|H|^{2k})^{1/2}
 \le C^k(k!)^{3/2}.                                      \tag{34}
\]

This is compatible with stretched-exponential approximation and a
\(\log^{3/2}(1/\epsilon)\) degree. It does not close the target. One would
need uniform analogues of (34) for every adaptively reused forward and adjoint
source, a way to compute the approximating coefficients from initialization
rather than future values, and stability of the resulting autonomous
closure. Gevrey order \(3/2>1\) does not justify reconstruction by the
initial Taylor series. Thus (32) is a proof-route obstruction, not an
existence obstruction.

Spherical harmonics face the same issue. Orthogonality reduces the active
training directions, but a passive whole-sphere query still contains Gaussian
projections in directions outside their span. Harmonic approximation of the
output alone neither closes the action/adjoint feedback nor records hidden
feature learning.

## 7. Quadrature, randomness, bits, and work

### Ordinary Monte Carlo is not the polylogarithmic route

At initialization, let \(H_a=\tanh\Xi_a\); the \(H_a\) are independent,
symmetric, and nondegenerate. The initial readout contribution to the training
prediction derivative contains

\[
 X_a=H_a\sum_b y_bH_b.
\]

For an index with \(y_a\ne0\), independence and parity give

\[
 \operatorname{Var}(X_a)
 =y_a^2\operatorname{Var}(H_a^2)
   +\sum_{b\ne a}y_b^2\mathbb E H_a^2\,\mathbb E H_b^2>0. \tag{35}
\]

An iid \(P\)-particle estimate of this contraction has root-mean-square error
\(\sqrt{\operatorname{Var}(X_a)/P}\). Therefore a proof that controls the
initial tangent by plain empirical quadrature needs \(P=\Omega(n)\) to reach
the root-width scale. This is a no-go statement for that Monte Carlo route,
not for deterministic cubature, control variates, or the full existence
claim.

### Exact-real storage is not bit storage

For rational precision \(p_{\rm bit}\) and scalar magnitude bound \(M_*\),
(26) costs
at least

\[
 O\bigl(S_{\rm real}[p_{\rm bit}+\log(1+M_*)]\bigr)       \tag{36}
\]

bits, before syntax metadata. If the finite vector field has Lipschitz
constant \(L_{R,P}\) through \(T_n\), a direct roundoff budget requires at
least schematically

\[
 p_{\rm bit}\gtrsim \log n+L_{R,P}T_n+\log C_{R,P}.      \tag{37}
\]

Neither the ridge-normalized dictionary nor the supplied source route bounds
\(L_{R,P}\), the smallest relevant Gram singular value, or
\(C_{R,P}\) as \(R=R_n\) grows. Thus no polylogarithmic bit-storage theorem
follows from a polylogarithmic real-coordinate count.

There is a finite but potentially enormous law-only initializer. Suppose a
truncated source program has evaluation cost \(C_n^{\rm eval}\), all source
coordinates are bounded by \(B_n\), and one wants its \(O(R_n^2)\) moments to
accuracy \(\delta_n\). Hoeffding plus a union bound allows a temporary cloud
of order

\[
 Q_n=O\!\left(B_n^4\delta_n^{-2}
                 \log(R_n/\eta)\right)                   \tag{38}
\]

for confidence \(1-\eta\). A finite linear program can then compress the
empirical moment vector to \(O(R_n^2)\) positive nodes by the reduction behind
(27), after which the cloud is discarded. The work is at least
\(Q_nC_n^{\rm eval}\) plus the moment and linear-program work. Formula (38)
does not simulate a trained dense network, but the permitted inputs give no
bounds on \(B_n\), \(C_n^{\rm eval}\), conditioning, or the necessary
\(\delta_n\). It is therefore an audit, not a complexity theorem.

The maintained numerical closure has the same logical limitation in a more
implemented form: for every fixed outer order its Gaussian initialization,
population quadrature, time mesh, and rational precision converge in a stated
iterated order, but no tolerance-to-resolution schedule is proved. An
arbitrary diagonal choice of these parameters is not licensed by the iterated
limit.

## 8. Claim ledger and decisive missing lemma

| Claim | Status | Reason |
|---|---|---|
| Small-label population fitting and an all-time whole-sphere tail | Proved here | Equations (7)--(10) |
| Both hidden layers move nonlinearly | Proved here | Equations (11)--(15) |
| Law-built autonomous Galerkin convergence on each fixed horizon | Proved here | Equations (16)--(25) |
| Some finite law-built autonomous model for each all-time accuracy | Proved, non-effective | Fixed-horizon convergence plus (10) |
| Generic finite rank-\(R\), \(P\)-node storage | Proved | Equation (26) |
| Generic positive moment support \(P=O(R^2)\) | Proved for a fixed finite moment certificate | Equation (27) |
| \(O(R^3)\) retained reals at the source rank (1) | Conditional | The population direct-source certificate is missing |
| \(O(R^2)=O(\log^{3d+2}n)\) retained reals | Conditional and stronger | Additionally needs effective source-compatible \(P=O(R)\) sparsification |
| Polylogarithmic retained bits and explicit work | Open | No growing-order conditioning or precision modulus |
| Nonexistence of every admissible polylogarithmic construction | Not proved | The pole and Monte Carlo results defeat routes, not the existence claim |

The single highest-leverage next theorem is the effective direct-source
certificate in Section 5, preferably proved in a real Gevrey/tail-weighted
norm rather than by a nonexistent population complex strip. It must include
the growing-order Gaussian-action program, both action orientations, a
source-compatible cubature, and conditioning. Without it, selecting an order
from convergence is exactly as hard as the requested result, so calling that
selection a routine diagonalization would hide the central gap.

## Inputs and limitations

Scientific inputs were the maintained `docs/index.qmd`,
`docs/notation.qmd`, the relevant maintained global action and finite-closure
sections, and only the five study artifacts authorized in the assignment.
The spherical source note and the matched-prefactor note are candidate or
conditional study results, so their quantitative statements are used only in
the explicitly conditional assembly above. No other study or archived book
material was read, and no numerical experiment was run.

The repository-mandated `explain-with-canonical-notation` skill and its linked
neural-network reference could not be read because the filesystem denied
access even after an escalation request. The maintained notation contract was
therefore applied directly. The rigorous-mathematics and
conjecture-investigation instructions were available and followed.
