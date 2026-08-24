# Hidden-neuron gauge block: exact tangent and surviving bath

Fix a neuron `j` in the second hidden layer and define its raw Gaussian
block

\[
 \mathcal B_j=
 \left(\sqrt n\,\Gamma_{1,j:},\sqrt n\,\Gamma_{2,:j}\right).             \tag{1}
\]

This note derives the leading fixed-mesh block tangent, with all
normalizations, and identifies what remains after the same-column,
characteristic, and Abel cancellations.

## 1. Exact gauge centering

Simultaneously perform

\[
 \Gamma_{1,j:}\mapsto-\Gamma_{1,j:},qquad
 \Gamma_{2,:j}\mapsto-\Gamma_{2,:j}.                                   \tag{2}
\]

Inductively along the exact Euler flow,

\[
\begin{array}{c|c}
 \text{changes sign}&
 P_{1,j:},\ Z_{2,j},\ X_{2,j},\ R_{2,j},\ B_{2,j},\ P_{2,:j}\\
 \hline
 \text{is unchanged}&
 r,\ X_1,\ Z_3,\ X_3,\ A,\ B_3,\ Q_1
\end{array}                                                            \tag{3}
\]

because the row product `B_(2,j) X_1`, the column product
`B_3 X_(2,j)`, and the contribution
`W_(1,j:)^* B_(2,j)` are invariant.  Hence

\[
 F_j^k=(\Gamma_{2,:j})^*B_3^k                                         \tag{4}
\]

is odd under (2).  Conditional on all Gaussian blocks other than
`mathcal B_j`,

\[
 \mathbb E[F_j^k\mid\mathcal B_j^c]=0.                                 \tag{5}
\]

The conditional Gaussian `L^p` Poincare inequality therefore gives

\[
 \|F_j^k\|_p
 \le C\sqrt p\,
 \left\|\|\nabla_{\mathcal B_j}F_j^k\|_2\right\|_p.                    \tag{6}
\]

Thus a `C_T sqrt(p)` block-gradient bound would imply the desired
`C_T p` estimate for `F_j`.

## 2. What survives the one-neuron cavity

Write

\[
 W_1=\Gamma_1+P_1,qquad W_2=\Gamma_2+P_2,
\]

and, at neuron `j`,

\[
 z_k=Z_{2,j}^k,\quad x_k=\atan z_k,\quad d_k=d(z_k),\quad R_k=R_{2,j}^k.
                                                                            \tag{7}
\]

Use the exact discrete velocities

\[
 X_1^{k+1}-X_1^k=hV_1^k,qquad
 B_3^{k+1}-B_3^k=hF_3^k.                                                 \tag{8}
\]

The rank-one updates give the two exact scalar identities

\[
\boxed{
\begin{split}
 z_{k+1}-z_k
  &=h\{\rho_{1,k}d_kR_k+\beta_k\},\\
 R_{k+1}-R_k
  &=h\{\rho_{3,k}x_k+\gamma_k\},                                      \tag{9}\\
 \rho_{1,k}&=\langle X_1^k,X_1^{k+1}\rangle_n,
 &\beta_k&=W_{1,j:}^kV_1^k,\\
 \rho_{3,k}&=\langle B_3^k,B_3^{k+1}\rangle_n,
 &\gamma_k&=(W_{2,:j}^k)^*F_3^k.
\end{split}}
\]

For example,

\[
 W_{1,j:}^{k+1}X_1^{k+1}
 =W_{1,j:}^kX_1^k+hW_{1,j:}^kV_1^k
   +hB_{2,j}^k\langle X_1^k,X_1^{k+1}\rangle_n,                         \tag{10}
\]

and the second identity is its exact transpose analogue.

Under the ordered limit, varying one gauge block changes the global cavity
paths `X_1,V_1,B_3,F_3` by `C_(p,h)n^(-1/2)` in normalized response norm.
Those cross-neuron responses are part of the vanishing cavity remainder.
The four quantities `rho_1,rho_3,beta,gamma` in (9), however, are leading:

* `rho_1` and `rho_3` are empirical Gram/energy coefficients;
* `beta` is the projection of the incoming row on the global feature
  velocity;
* `gamma` is the projection of the outgoing column on the global backward
  velocity.

In particular `beta` and `gamma` are order-one Gaussian bath processes
conditional on the cavity.  Gauge peeling does not make them small.

## 3. Exact leading block tangent

Let

\[
 Z_k=\nabla_{\mathcal B_j}z_k,qquad
 S_k=\nabla_{\mathcal B_j}R_k,qquad
 U_k=\nabla_{\mathcal B_j}\beta_k,qquad
 V_k=\nabla_{\mathcal B_j}\gamma_k.                                    \tag{11}
\]

After discarding only the `o_n(1)` response of the cavity paths, (9)
differentiates to

\[
\begin{split}
 Z_{k+1}&=Z_k+h\rho_{1,k}{d_kS_k+R_kd'_kZ_k\}+hU_k,\\
 S_{k+1}&=S_k+h\rho_{3,k}d_kZ_k+hV_k.                                  \tag{12}
\end{split}
\]

The bath tangents are not arbitrary.  If `J_(1,k)` and `J_(2,k)` are the
block Jacobians of the learned incoming row and outgoing column, then

\[
 U_k=J_{1,k}V_1^k,qquad V_k=J_{2,k}^*F_3^k                              \tag{13}
\]

at leading order, with

\[
\begin{split}
 J_{1,k+1}-J_{1,k}
  &=h\{d_kS_k+R_kd'_kZ_k\}\otimes X_1^k,\\
 J_{2,k+1}-J_{2,k}
  &=hB_3^k\otimes(d_kZ_k).                                              \tag{14}
\end{split}
\]

The initial Jacobians are the two normalized coordinate embeddings and
have Hilbert--Schmidt norm one.  Equations (12)--(14) are the exact
fixed-mesh one-neuron tangent before characteristic dressing.

## 4. Exact arctan characteristic cancellation

Set

\[
 Y_k={Z_k\over d_k},qquad
 D_k=Dd(z_k,z_{k+1}).                                                    \tag{15}
\]

Since

\[
 d_{k+1}-d_k=hD_k\{\rho_{1,k}d_kR_k+\beta_k\},                          \tag{16}
\]

an exact rearrangement of the first line of (12) gives

\[
\boxed{
\begin{split}
 Y_{k+1}={}&Y_k
  +h\rho_{1,k}{d_k\over d_{k+1}}S_k\\
 &+{h\over d_{k+1}}\{U_k-D_k\beta_kY_k\}\\
 &+h\rho_{1,k}R_k{d_k(d'_k-D_k)\over d_{k+1}}Y_k.                       \tag{17}
\end{split}}
\]

The large predictable amplitude `R_k` has disappeared from the principal
linear coefficient.  It remains only in the Euler defect on the last line.
Because

\[
 |d'_k-D_k|\le\|d''\|_\infty|z_{k+1}-z_k|
 \le Ch(|R_k|+|\beta_k|),                                               \tag{18}
\]

the last line has size

\[
 O\bigl(h^2(|R_k|^2+|R_k\beta_k|)\,|Y_k|\bigr).                         \tag{19}
\]

It is controlled by the exact training energy at fixed mesh and vanishes
in the Euler limit once a leading tangent estimate is available.  This is
the precise diagonal arctan-curvature cancellation.

The term on the second line of (17),

\[
 \boxed{
 \mathcal T_k={1\over d_{k+1}}
       \{\nabla_{\mathcal B_j}\beta_k-D_k\beta_kY_k\},                 \tag{20}
 }
\]

is the covariant incoming-bath tangent.  It is order one.  In the
continuous notation it is

\[
 {\nabla\beta\over d}-{d'\over d}\,\beta Y.                             \tag{21}
\]

The exact top characteristic and the Abel subtraction

\[
 R_k=F_j^k+h\sum_{s<k}x_s\langle B_3^s,B_3^k\rangle_n                   \tag{22}
\]

remove the `rho_3 x` learned self term from the tangent of the *bare*
quantity `F_j`.  They produce the transpose analogue of (20), with
`gamma_k`, plus Gram kernels whose `h`-integrals are bounded by the output
energy.  They do not cancel (20), because (20) belongs to the independent
incoming gauge half of the block.

## 5. The exact squared-energy obstruction

Any quadratic energy containing `||Y_k||_2^2` obtains from (17) the signed
increment

\[
 2h\left\langle Y_k,
 {\nabla\beta_k-D_k\beta_kY_k\over d_{k+1}}
 \right\rangle.                                                        \tag{23}
\]

The first part of (23) is a Cameron--Martin forcing; the second is

\[
 -2h{D_k\over d_{k+1}}\,\beta_k\|Y_k\|_2^2.                             \tag{24}
\]

It has no sign.  Neither Bessel, the global training energy, nor the
rowwise learned-field bound controls its positive part: `beta_k` is a
single-neuron Gaussian projection, while the global energy averages over
all neurons.  The exact response of every *other* hidden neuron has moved
to `o_n(1)`, but the scalar transport bath (24) is genuinely leading.

Thus the desired block-gradient estimate reduces to the following precise
new lemma:

\[
\begin{split}
 &\left\|
 \sup_{m\le T/h}\left|
 h\sum_{k<m}
 \left\langle Y_k,
 {\nabla\beta_k-D_k\beta_kY_k\over d_{k+1}}
 \right\rangle
 \right|^{1/2}
 \right\|_p\\
 &\hspace{45mm}\le C_T\sqrt p
   \left(1+\left\|\sup_{k\le T/h}\mathcal E_k^{1/2}\right\|_p\right),\tag{25}
\end{split}
\]

with a coefficient small enough to absorb the last factor.  Formula (25)
is a signed one-neuron bath estimate, not a propagation-of-chaos or cavity
statement.

## 6. Why an energy-only proof of (25) is impossible

There is a local leading-flow mechanism that gives lognormal block
sensitivity while respecting the exact gradient equations.  Let the
cavity feature path rotate in a two-dimensional plane,

\[
 X_1(t)=(\cos t,\sin t),                                                 \tag{26}
\]

and let the conjugate signal be `R(t)=L+O_T(1)`, where `L` is the outgoing
Gaussian projection.  For the incoming row put

\[
 z(t)=W_{1,j:}(t)X_1(t),qquad
 \beta(t)=W_{1,j:}(t)\dot X_1(t).                                      \tag{27}
\]

The exact local gradient equation

\[
 \dot W_{1,j:}=R(t)d(z(t))X_1(t)                                       \tag{28}
\]

then gives

\[
 \dot z=R d(z)+\beta,qquad \dot\beta=-z.                              \tag{29}
\]

For `L >> 1`, there is a slow trajectory with

\[
 z(0)=-1+O(L^{-1}),\qquad \beta(0)=-L/2+O(L^{-1}),                     \tag{30}
\]

on which `z(t)=-1+O_T(L^(-1))` for `0<=t<=T`.  Linearizing (29) in an
incoming direction that changes `z(0)` but not `beta(0)` gives

\[
 {d\over dt}\binom{u}{v}
 =\begin{pmatrix}Ld'(z(t))&1\\-1&0\end{pmatrix}\binom{u}{v}.            \tag{31}
\]

Since `d'(-1)=1/2`, (31) has a fast exponent at least `cL`; hence

\[
 |u(T)|\ge c\exp(cLT)                                                   \tag{32}
\]

for a nonzero open cone of tangent directions.  A terminal top
same-column susceptibility `mu != 0` gives

\[
 |\nabla_{\mathcal B_j}F_j(T)|
 \ge c|\mu|d(z(T))|u(T)|.                                               \tag{33}
\]

The conditions (26)--(30) are a genuine one-neuron cavity realization of
the original rank-one gradient flow.  They obey the normalized global
energy bound because one exceptional neuron contributes only `L^2/n` to
that energy.  This proves that **no deterministic estimate from the global
energy can control (23)**.

More quantitatively, keeping the base path in the slow tube while retaining
the fast tangent requires an incoming Gaussian projection to lie in an
interval of width `exp(-C L T)`.  Together with the outgoing Gaussian
event, its probability is at least

\[
 \exp\{-C L^2-C L T\}.                                                  \tag{34}
\]

Combining (32)--(34) and optimizing `L` in a `p`th moment gives exponential,
not polynomial, growth of the block-gradient moments *conditional on this
cavity path*.  Therefore a bound

\[
 \|\|\nabla_{\mathcal B_j}F_j\|_2\|_p\le C_T\sqrt p                    \tag{35}
\]

cannot follow from gauge symmetry, characteristic cancellation, and the
available global energy alone.  This does not show that `F_j` itself lacks
a `psi_1` bound: on the event above `F_j=O(L)`, while its derivative is
exponentially large.

There is an important quantifier caveat.  Merely saying that the rotating
macroscopic cavity path is in an open full-support set at finite `n` does
not give a lower bound uniform in `n`; its probability could be
`exp(-c n)` and disappear before the Euler limit.  Thus (26)--(34), by
themselves, do **not** disprove the annealed canonical Poincare estimate.

A structure-respecting conditional version needs much less than the exact
rotation.  Suppose the limiting complement has, on an event `E`,

\[
 \det\operatorname{Gram}_n(X_1(t_0),V_1(t_0))\ge c_0,
 \quad \|B_3(t_0)\|_n\ge c_0,                                          \tag{35}
\]

bounded local cavity velocities, and a nonzero terminal same-column top
susceptibility.  Conditional on this complement, `(z,beta)` are two
nondegenerate Gaussian projections of the incoming row and `R` is a
nondegenerate Gaussian projection of the outgoing column.  Hence, uniformly
in `n`,

\[
 \mathbb P_{\mathcal B_j}
 \{R\in[L,L+1],\ z\simeq-1,\ \beta\simeq-\rho_1Ld(-1)\mid E\}
 \ge e^{-C_E L^2}.                                                      \tag{36}
\]

Even without an exactly rotating path, bounded cavity derivatives imply
that the mismatch in `z'=rho_1 R d(z)+beta` grows at most `O_E(Lt)`.
Consequently `z` remains in a fixed neighborhood of `-1` for
`0<=t<=c_E L^(-1/2)`, while a tangent direction changing `z` but not
`beta` grows at least

\[
 \exp(c_E\sqrt L).                                                       \tag{37}
\]

Choosing meshes `h << L^(-1/2)`, (36)--(37) give

\[
 \|\|\nabla_{\mathcal B_j}F_j\|\|_p
 \ge \exp(c_Ep^{1/3})                                                    \tag{38}
\]

after optimizing `p sqrt(L)-C_E L^2`.  Thus the annealed `C sqrt(p)`
bound fails **if** `P(E)` has a positive limiting lower bound.  Establishing
that nondegenerate complement event for the actual tensor-program orbit is
a separate statement; it is not implied by the presently available energy
identity.

## 7. Verdict

The simultaneous hidden-neuron gauge block gives exact conditional
centering and removes all cross-neuron response terms in the ordered
large-width limit.  The large local predictor `R_j` is also removed from
the principal tangent coefficient by the exact arctan characteristic; it
survives only in the `O(h^2)` Euler defect (19).

However, the previously hard off-diagonal mechanism does **not** disappear
entirely.  Its cross-neuron part is vanishing, but its peeled-neuron
transport component survives exactly as the leading covariant bath term
(20).  The squared-gradient problem is precisely (25), and the rotating
feature realization (26)--(34) shows that no energy-only `C sqrt(p)` bound
for the full gauge-block gradient is possible.  The stronger annealed
failure follows conditionally from the canonical nondegeneracy event (35),
but that event has not been proved for the actual limiting orbit.  The
rigorous present verdict is therefore: **energy-only gauge Poincare is
ruled out; annealed gauge Poincare remains unproved.**  A route avoiding
(25) must bound `F_j` through its signed value/Abel representation rather
than its full Gaussian Lipschitz constant.
