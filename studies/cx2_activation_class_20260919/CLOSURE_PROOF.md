# Conditional dense closure for the fixed C1,1 activation class

Scoped first-round proof, 19 September 2026. This file is a study result, not
established repository theory. It gives a population closure theorem conditional
on a specified strong target and its tails, and a separate numerical consistency
theorem. It neither proves the long-horizon Gaussian source estimates nor runs
an experiment. Labels are arbitrary bounded labels; in particular the result
does not require the two anchors to have equal labels.

## 1. Exact target and the remaining external interface

Fix finite data `(u_a,y_a,omega_a)`, `a=1,...,m`, with `u_a=x_a/sqrt(d)`,
`|u_a|<=X`, `|y_a|<=Y`, positive weights summing to one. The mean-loss case
has `omega_a=1/m`. Fix the same activation in both hidden layers,

\[
 \phi\in C^{1,1}(\mathbb R),\quad |\phi(0)|\le D_0,
 \quad\|\phi'\|_\infty\le D_1,
 \quad\operatorname{Lip}(\phi')\le D_2.                 \tag{1}
\]

Thus `|phi(z)|<=D0+D1|z|`. Nonaffinity is allowed and is the intended class,
but the closure argument does not use it or prove activity. The finite model is
bias-free, with stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`,
and unhalved weighted mean-square loss in physical time. The actual finite
readout is random; only its population limit is zero.

There are two probability spaces and Hilbert spaces `H_l=L2(Omega_l)`.
The initialized action `A0:H1->H2` is the actual Gaussian-program action,
and `A0*` is its actual adjoint. A bound `||A0||<=C0` suffices; the elementary
bound `C0=10` from special-data III.F is adequate. Write

\[
 \begin{gathered}
 w\in L^2(\Omega_1;\mathbb R^d),\quad c\in H_2,
 \quad A=A_0+K,\quad K\in\mathcal S_2(H_1,H_2),\\
 Z_a^1=w\cdot u_a,\quad H_a^1=\phi(Z_a^1),\quad
 Z_a^2=AH_a^1,\quad H_a^2=\phi(Z_a^2),\\
 \Delta_a^2=c\phi'(Z_a^2),\quad q_a=A^*\Delta_a^2,
 \quad\Delta_a^1=\phi'(Z_a^1)q_a,\\
 f_a=E_2[cH_a^2],\quad r_a=f_a-y_a,\quad
 \mathcal L=\sum_a\omega_a r_a^2,\\
 w'=-2\sum_a\omega_a r_a\Delta_a^1u_a,\quad
 K'=-2\sum_a\omega_a r_a\Delta_a^2\otimes H_a^1,\quad
 c'=-2\sum_a\omega_a r_aH_a^2.                         \tag{2}
 \end{gathered}
\]

Here `(v tensor h)b=v E1[h b]`. All products and pairings are within the
indicated population. The first coordinate is the complete `d`-component row.

The conditional population theorem needs the following two target premises.

* **S: strong target.** For a fixed `T>0`, (2) has a strong `C1` solution
  `(w,K,c)` in row `L2` + increment Hilbert--Schmidt + readout `L2`, with
  `(w,K,c)(0)=(g,0,0)` and `g~N(0,I_d)`, on the actual common Gaussian
  action carrier. The initialized universal observable spaces constructed
  below are a reducing pair inside that carrier.
* **E: reference tails.** For finite constants `M,a>0`,
  \[
  \sup_{t\le T}\left\{\tau_R(c(t))+
       \sum_a\omega_a\tau_R(q_a(t))\right\}\le M e^{-aR},
  \quad R\ge1,\qquad
  \tau_R(V)=\|V\mathbf1_{|V|>R}\|_2.                    \tag{3}
  \]

These are marginal tails with common time constants. No random supremum in
time, forward-field tail, tail of an approximate trajectory, or tail for every
passive observation is required. Gaussian tails are more than sufficient.
Section 6 states a weaker general Osgood version. Strong uniqueness, energy,
and invariance in the universal observable spaces are consequences proved
below; they need not be added to S. The target may be constructed on a larger
common generated carrier: the reducing-pair condition permits the same proof.

**Neural identification is a separate premise.** To identify the eventual
answer with the actual finite-width GF limit on `[0,T]`, the source route
must additionally establish that limit for (1)--(2), with the prescribed
finite random initialization and the requested joint observations. The
closure theorem compares directly with S and does not establish that bridge.
The proof also does not establish S or E at a prescribed long horizon.

## 2. An activation-independent smooth dictionary

Use constants on both populations, the first-population roots `g_1,...,g_d`,
rational affine combinations, `sin`, `cos`, `tanh`, products of bounded
words, and `A0` or `A0*` applied to bounded words. Population types select
the action direction. The three probe functions are fixed dictionary
functions; they do not replace the target activation in (2).

Enumerate all finite correctly typed words and all dependencies in a causal,
deterministic sequence. One explicit enumeration orders finite syntax trees
by a natural-number encoding of their rational labels and operations, then
includes every tree of code at most N together with its dependencies. A
finite prefix has finitely many nodes and every finite word eventually
appears. Retain all bounded outputs in the prefix, together with constants;
keep literal duplicates. Denote the retained column by `psi_l,N` of length
`d_l(N)`. Neither the dictionary nor the enumeration uses phi, data, time,
width, a future path, or a fitted coefficient.

Every retained word has an explicit deterministic supremum bound obtained
from its syntax. Its finite Gaussian initialization uses the complete
same-action source rule. For a forward input b and a reverse input v,

\[
 A_0b=\xi_b+\sum_{j:\,\text{earlier reverse}}
                 v_j E_1[\partial_{\zeta_j}b],\qquad
 A_0^*v=\zeta_v+\sum_{i:\,\text{earlier forward}}
                 b_i E_2[\partial_{\xi_i}v].             \tag{4}
\]

The source covariances are the full uncentered operand Grams. Different
orientation source groups are independent, but the answers in (4) are not
independent: the response terms retain actual adjunction. Named derivatives
freeze all previously selected coefficients and covariances, even at singular
source covariance. A singular extension is realized by `C`-pseudoinverse and
its nonnegative Schur complement as in special-data III.F.4--5; no empirical
rank deletion or continuity of pseudoinverses is used.

All coordinate operations used here are smooth; bounded products have smooth
globally Lipschitz extensions on their known bounded parent ranges. Every
fixed graph has a linear Gaussian value envelope and bounded named-source
derivatives of each separately fixed finite order, by induction through its
finite coordinate operations and frozen response sums. In particular the
finite-program hypotheses of III.F.1--7 apply. No derivative of the target
phi occurs in this initializer, including at deeply nested action calls.
This avoids asking a merely C1,1 activation for higher derivatives.

Let `H_l^obs` be the `L2` space of the sigma-field generated by these word
values. Bounded-word spans are dense. Indeed finite-coordinate measurable
cylinders approximate every measurable `L2` variable by the monotone-class
and simple-function argument. Sine/cosine tests of rational affine
combinations of each finite tuple are total: orthogonality defines a finite
signed measure with zero Fourier transform (first pass from rational to real
frequencies by bounded convergence); convolution with a Gaussian gives zero
density by the Gaussian Fourier integral and Fubini; letting its variance
decrease to zero annihilates every bounded continuous test and hence the
measure. This proves density without moment determinacy. Truncations
`R tanh(V/R)` show that each unbounded word also belongs to this completion.

An action on a bounded word is a word, and action boundedness extends this
mapping to the completed spaces. Thus `A0 H1^obs subset H2^obs` and
`A0* H2^obs subset H1^obs`. Actual adjunction makes these a reducing pair:
if `P_l` projects onto `H_l^obs`, then `A0 P1=P2 A0`.
Every measurable coordinate operation whose output is in `L2` remains in
these spaces. This includes phi, its bounded derivative, and a bounded
measurable gate times an `L2` field, even though phi is not a dictionary word.

Choose the explicit positive ridge `eta_N=2^{-N}` and define

\[
 G_l=E_l[\psi_l\psi_l^T],\quad
 b_l=(G_l+\eta_N I)^{-1/2}\psi_l,\quad
 U_lv=b_l^Tv,\quad Q_l=U_lU_l^*,\quad
 D_N=E_2[b_2(A_0b_1)^T]=U_2^*A_0U_1.                  \tag{5}
\]

The fixed inputs are the two complete joint mark laws
`lambda_1,N=Law(b1,g)` and `lambda_2,N=Law(b2)`, and the finite matrix
`D_N`. Compute their finite initialization programs jointly with all actions
in (5); separate marginals do not specify them. `D_N^T` is the contraction
of the actual reverse action. Positive inverse square roots exist even
when `G_l` is singular, since the ridge is positive.

Both `U_l` and `Q_l` are contractions. With `S_l v=psi_l^T v`,
`Q_l=S_l(G_l+eta_N I)^{-1}S_l*`. For a vector `S_l v` in any earlier
retained span, zero-pad v in later dictionaries. Diagonalization gives

\[
 \|(I-Q_l)S_lv\|_2^2
 =\sum_j\frac{\eta_N^2\lambda_j}{(\lambda_j+\eta_N)^2}|v_j|^2
 \le\frac{\eta_N}4|v|^2.                               \tag{6}
\]

Density and `||I-Q_l||<=1` prove strong convergence `Q_l->I` on
`H_l^obs`. Define only for analysis

\[
 B_N=Q_2A_0Q_1=U_2D_NU_1^*.
\]

Then `||B_N||<=C0`, and both `B_N->A0` and `B_N*->A0*` strongly on the
observable spaces. For example
`||(B_N-A0)v||<=C0||(Q1-I)v||+||(Q2-I)A0v||`.
Uniform operator bounds make convergence uniform on every compact target
`L2` set by a finite net. None of these conclusions is operator-norm
convergence of the initialized action.

## 3. The autonomous finite-type population system

The saved state consists of

\[
 M\in\mathbb R^{d_2\times d_1},\quad
 \Gamma_1=\operatorname{Law}(b_1,g,w),\quad
 \Gamma_2=\operatorname{Law}(b_2,c),                      \tag{7}
\]

with fixed `D_N`, the data, and the static dictionary description. The first
law has coordinate dimension `d1+2d`, the second `d2+1`.
Initialize `w=g,c=0,M=D_N`. For every input u set

\[
 \begin{gathered}
 a(u)=E_{\Gamma_1}[b_1\phi(w\cdot u)],\qquad
 Z_N^2(u,b_2)=b_2^TMa(u),\quad H_N^2(u)=\phi(Z_N^2(u)),\\
 d(u)=E_{\Gamma_2}[b_2c\phi'(Z_N^2(u))],\quad
 q_N(u,b_1)=b_1^TM^Td(u),\\
 f_N(u)=E_{\Gamma_2}[cH_N^2(u)],\quad r_{N,a}=f_N(u_a)-y_a,\\
 w'=-2\sum_a\omega_a r_{N,a}\phi'(w\cdot u_a)q_N(u_a)u_a,\\
 c'=-2\sum_a\omega_a r_{N,a}H_N^2(u_a),\qquad
 M'=-2\sum_a\omega_a r_{N,a}d(u_a)a(u_a)^T.             \tag{8}
 \end{gathered}
\]

Push the complete joint laws (7) forward by these characteristic velocities;
their b and g coordinates are frozen. Equivalently use their continuity
equations in w and c. All displayed expectations use the current joint
population state. There is no hidden Gaussian action query: multiplying M
or its actual transpose and taking the finite b-contractions is the full
action rule. No omitted-level value or time-history coefficient is used.

For comparison on the canonical carrier put

\[
 K_N=U_2(M-D_N)U_1^*,\quad A_N=B_N+K_N=U_2MU_1^*.
\]

The middle equation is exactly

\[
 K_N'=Q_2\left[-2\sum_a\omega_a r_{N,a}
                 \Delta_{N,a}^2\otimes H_{N,a}^1\right]Q_1,
 \quad\Delta_{N,a}^2=c_N\phi'(A_NH_{N,a}^1).             \tag{9}
\]

This is positive two-sided filtering of the learned increment. The state
still includes two probability-law fields; it is finite-type, not finitely
many scalars until numerical population quadrature is performed.

## 4. Well-posedness with unbounded hidden features and readout

At fixed N write `|b_l|<=L_l<infinity` and work with unknowns
`v=w-g` and c in their `L-infinity` spaces, and M in its finite matrix space.
On bounded sets of `(v,c,M)`, (8) is locally Lipschitz. For the only unbounded
base coordinate,

\[
 |a(u)|\le L_1[D_0+D_1X(\|g\|_2+\|v\|_\infty)],\qquad
 |a(u)-\widetilde a(u)|\le L_1D_1X\|v-\widetilde v\|_\infty.
\]

Every upper preactivation is pointwise bounded there by `L2||M|| |a|`.
The remaining subtractions use bounded b, bounded phi', Lipschitz phi', and
finite products. Picard's integral map is a contraction on a sufficiently
short closed path ball (time times the local Lipschitz constant is less than
one, and time times the speed stays within the ball). This proves unique
local characteristic existence. It requires no second derivative of phi.

The exact weighted gradient calculation gives

\[
 \mathcal L_N'=-\|w_N'\|_2^2-\|c_N'\|_2^2-\|M_N'\|_F^2,
 \qquad\mathcal L_N(0)=E_0:=\sum_a\omega_a y_a^2.        \tag{10}
\]

Indeed variation of M gives `delta f_a=d(u_a)^T delta M a(u_a)`;
adjunction through `U2 M U1*` gives the row gradient in (8), and the readout
gradient is `H_N^2`. The scalar chain rule is valid with unbounded features:
phi has bounded continuous derivative, so for a strongly C1 `L2` curve Z,
the mean-value formula and bounded-multiplier continuity give
`(phi(Z))'=phi'(Z)Z'` in L2. Pairing two C1 L2 curves differentiates their
scalar pairing. A bounded continuous multiplier b preserves strong products:
if `Z_j->Z` in probability and `V_j->V` in L2, subtract the varying V, then
truncate the fixed V and use bounded convergence. This proves all chain
rules used here. It also proves (10) and its raw counterpart for S.

Cauchy--Schwarz in time now gives the order-independent estimates

\[
 \begin{gathered}
 \|(w_N-g,c_N,M_N-D_N)(t)\|_{L^2\oplus L^2\oplus F}
       \le\sqrt{tE_0},\\
 \|w_N(t)\|_2\le\sqrt d+\sqrt{TE_0},\quad
 \|c_N(t)\|_2\le\sqrt{TE_0},\quad
 \|K_N(t)\|_{\rm HS}\le\sqrt{TE_0},\quad
 \|A_N(t)\|_{\rm op}\le C_0+\sqrt{TE_0}.               \tag{11}
 \end{gathered}
\]

In the first line the norm is the Hilbert direct-sum norm. There is no
claim that c has an order-uniform supremum bound. Linear growth gives uniform
L2 bounds for both hidden layers from (11), as needed for the outer limit.
The target has the same energy and raw displacement bounds.

To complete fixed-N global continuation, the estimates actually needed are
pointwise speed bounds depending on N. Let
`W=sqrt(d)+sqrt(TE0)`, `C=sqrt(TE0)`, `A=C0+sqrt(TE0)` and
`H=D0+D1 X W`. Exact contraction of U gives `|a|<=H`, `|d|<=D1 C`.
Since `sum omega |r|<=sqrt(E0)`,

\[
 \|c_N'\|_\infty\le2\sqrt{E_0}(D_0+D_1L_2AH),\qquad
 \|w_N'\|_\infty\le2\sqrt{E_0}D_1X L_1 A D_1 C.       \tag{12}
\]

The matrix increment is bounded in Frobenius norm by (11). Thus `w-g,c,M`
stay in bounded local-existence balls on every fixed finite interval, their
speeds give Cauchy endpoints, and the local argument continues them. This
proves unique existence through every finite time at each fixed N.
For noncontractive numerical mark laws the same argument uses
`|a|<=L1 H`, `|d|<=L2 D1 C` and `A=||D||op+sqrt(TE0)` in the pointwise
formula, while (10) still bounds w,c,M. It gives finite fixed-order constants.

Restart from a reached state saves precisely (7), M and the fixed inputs.
The current conditional distributions are already in (7). Couple identical
saved coordinates and apply the same characteristic uniqueness. The
continuation is the restriction of the previous solution, with no additional
coordinate or history. Frozen g is kept for initial/current observations.

## 5. Error production is a compact-target statement

First the target in S remains in `H_l^obs`, with K supported between them.
Finite Euler steps of (2) from initialization preserve these spaces, since
measurable coordinate operations, both actions and finite rank sums preserve
them. To justify passage from Euler to S, apply the one-reference estimate
of Section 6 with S as the reference. Stop the Euler interpolant in a raw
ball one unit larger than S's compact path. On that ball the vector field
is bounded, using linear growth and bounded phi', so the node/current
discrepancy is `O(h)`. The Osgood comparison below makes its distance to S
tend uniformly to zero as maximal step h tends to zero. A first exit is
therefore impossible for small h. The limit stays in the closed observable
spaces and their closed HS block. This proves invariance rather than assuming
that the raw field is locally Lipschitz in the ambient L2 metric.

Fix any compact passive input set `U`, containing the training inputs. The
target maps `(t,u)->H^1(t,u),Delta^2(t,u)` are continuous into L2: forward
maps are Lipschitz on the bounded raw ball; the gate times c uses the
bounded-multiplier argument in Section 4. Their images are compact. The
strongly continuous HS velocity `K'(t)` also has compact image. Hence

\[
 \begin{split}
 \epsilon_N={}&\sup_{t\le T,u\in U}\|(B_N-A_0)H^1(t,u)\|_2\\
 &+\sup_{t\le T,u\in U}\|(B_N^*-A_0^*)\Delta^2(t,u)\|_2\\
 &+\sup_{t\le T}\|Q_2K'(t)Q_1-K'(t)\|_{\rm HS}
 \longrightarrow0.                                    \tag{13}
 \end{split}
\]

The first two terms use strong convergence uniform on compact sets. For the
last, approximate a fixed HS operator by finite sums of ranks (truncate its
square-summable matrix coefficients in orthonormal bases). Strong convergence
handles the finitely many factors; contractions control the discarded HS
remainder. A finite net of the derivative curve gives uniformity.

Thus omitted error is produced at a vanishing rate along the actual target.
Bounded raw norm alone would not prove (13) on an entire infinite-dimensional
ball. The error (13) is a proof quantity only; it is not supplied to the
initializer, state, drift, dictionary enumeration, or order-selection rule.

## 6. Error propagation with two unbounded reference multipliers

Set

\[
 e_N=\|w_N-w\|_2+\|K_N-K\|_{\rm HS}+\|c_N-c\|_2,
 \qquad\delta_N=e_N+\epsilon_N.
\]

The uniform raw/action ball (11) gives, uniformly on U,

\[
 \|H_N^1-H^1\|_2+\|Z_N^2-Z^2\|_2+
 \|H_N^2-H^2\|_2+|f_N-f|\le C\delta_N.                \tag{14}
\]

For example
`Z_N^2-Z^2=A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A0)H^1`.
For prediction subtract `(c_N-c)H_N^2+c(H_N^2-H^2)` and use
Cauchy--Schwarz; bounded readout or bounded activation is unnecessary.

For any fixed reference V and cutoff R,

\[
 \|[\phi'(Z)-\phi'(\bar Z)]V\|_2
 \le D_2R\|Z-\bar Z\|_2+2D_1\tau_R(V).                \tag{15}
\]

Below the cutoff use the Lipschitz derivative, and above it use its two
supremum bounds. Applying (15) first to the reference c gives

\[
 \|\Delta_N^2-\Delta^2\|_2
 \le D_1\|c_N-c\|_2+C R\delta_N+2D_1\tau_R(c).
\]

Then subtract the actual adjoint actions:

\[
 q_N-q=A_N^*(\Delta_N^2-\Delta^2)
              +(K_N-K)^*\Delta^2+(B_N^*-A_0^*)\Delta^2.
\]

Finally apply (15) to the reference q in the lower gate. The result is

\[
 \|\Delta_{N,a}^1-\Delta_a^1\|_2
 \le C(1+R)\delta_N+C\tau_R(c)+C\tau_R(q_a).           \tag{16}
\]

The c cutoff enters the already computed q difference and is multiplied
only by the bounded lower gate. The q cutoff is then added. There is no
`R^2` factor. This additive structure is what permits exponential tails,
despite both c and q being unbounded.

Subtract row and readout velocities using (14)--(16) and bounded residuals
on the common raw ball. For the middle velocity write `F_K` for the rank
sum in (2); the exact decomposition is

\[
 K_N'-K'=Q_2\{F_K(w_N,A_N,c_N)-F_K(w,A,c)\}Q_1
                         +(Q_2K'Q_1-K').               \tag{17}
\]

The rank inequality
`||v tensor h-vbar tensor hbar||HS <= ||v-vbar||2||h||2
+||vbar||2||h-hbar||2` controls its first term with the same bound.
Its second is at most epsilon_N by (13). Consequently, almost everywhere,

\[
 e_N'\le C(1+R)(e_N+\epsilon_N)+CM e^{-aR},\quad
 R\ge1,\qquad e_N(0)=0.                                \tag{18}
\]

Only S needs tails. Norms of C1 Hilbert curves are absolutely continuous;
their upper derivative is bounded by the norm of their derivative, also
at zeros. This justifies the summed scalar inequality.

Put `v=e_N+epsilon_N+eta`, `eta>0`. While `v<=1`, choose
`R=1+a^{-1}log(1/v)`. Then `v'<=L v log(e/v)` with L independent of
N and eta. For `z=log(e/v)`, `z'>=-Lz`, so

\[
 e_N(t)+\epsilon_N+\eta
 \le e^{1-\alpha(t)}(\epsilon_N+\eta)^{\alpha(t)},
 \qquad\alpha(t)=e^{-Lt}>0.                             \tag{19}
\]

For small initial v this remains below one throughout `[0,T]`, validating
the cutoff by first exit. Send eta to zero and use (13). Thus
`sup_[0,T] e_N ->0`. The same estimate with zero source, with a competing
strong solution's bounded raw ball and S as the tail-bearing reference,
proves uniqueness and reached-state uniqueness for S. It also gives the
Euler-to-S comparison used in Section 5, with the `O(h)` node discrepancy
added to v. No tail premise is imposed on Euler or closure states.

**Weaker tail interface.** Exponential decay is a simple sufficient condition,
not a necessity. The argument works whenever a uniform target tail majorant
tau admits an increasing positive modulus omega near zero satisfying

\[
 \inf_{R\ge1}\{C(1+R)s+C\tau(R)\}\le\omega(s),\qquad
 \int_{0^+}\frac{ds}{\omega(s)}=\infty.                 \tag{20}
\]

For positive regularized errors, integrate `v'/omega(v)<=1`; divergence
ensures that vanishing initial/source errors remain vanishing on a fixed
horizon. This is the exact stability property used. Merely uniform
integrability or finitely many polynomial moments does not supply (20) by
this proof. For example a polynomial tail yields a power modulus with
exponent less than one, whose reciprocal is integrable at zero.

## 7. Prediction, paired observations, and both action directions

Equation (14) gives convergence of predictions uniformly in time and on
every fixed compact input set U. Initial lower features are `phi(g dot u)`;
initial upper features are reconstructed with the fixed D:

\[
 H_{N,0}^2(u,b_2)=\phi\left(b_2^TD_NE_1[b_1\phi(g\cdot u)]\right).
                                                               \tag{21}
\]

They converge uniformly in u in L2 by compact-target strong convergence.
No frozen upper Gaussian seed must be appended to the saved state.

More generally, fix a finite typed observation graph built from moving and
frozen seeds, affine and globally Lipschitz coordinate maps, bounded
continuous gate factors, products with one bounded factor, and finitely many
actions in either direction, provided all outputs are L2. It can include
phi and phi'. A factor declared bounded here has one deterministic syntax
envelope shared by target and approximants; the unbounded seed c is not
declared bounded just because each fixed-order c happens to be bounded.
Its finite-order action is exactly
`V -> b2^T M E1[b1 V]`, or `V -> b1^T M^T E2[b2 V]` in reverse.
Both accept only the declared graph's current fields, not an external
undeclared action oracle. Each fixed graph is evaluated as a pushforward
of the same two current joint laws.

Induct through the graph. For an action use

\[
 A_NV_N-AV=A_N(V_N-V)+(K_N-K)V+(B_N-A_0)V.               \tag{22}
\]

The first two terms vanish by the norm bounds and (19), the third uniformly
on the compact target node curve. The identical argument for actual adjoints
handles reverse nodes. A bounded continuous gate times an L2 field uses
the strong-multiplier argument, uniformly on compact target curves by a
finite-net tail bound. Lipschitz maps and bounded products use ordinary
subtractions. Thus every separately fixed same-layer tuple converges in L2
on its common carrier, uniformly in time.

For such a tuple V, common-carrier coupling proves

\[
 \mathcal W_2(\operatorname{Law}(V_N),\operatorname{Law}(V))^2
 \le\sum_j\|V_{N,j}-V_j\|_2^2.                         \tag{23}
\]

Quadratic contractions converge by Cauchy--Schwarz. In particular the joint
initial/current pairs, with the same input drawn from the training law,
converge in W2, and their RMS displacements converge by the reverse triangle
inequality. Neither bounded activations nor fourth moments are needed for
these quadratic observations. Independent coupling of the initial and
current marginals would not give this conclusion. No cross-layer neuron
pairing is asserted. Activity or nonaffinity conclusions transfer only if
the target route establishes them.

There is also a reached-state interpretation for the complete observation
hierarchy. At any target time s, generate the two current sigma-fields by
all finite bounded current probes, and close their spans in L2. Equality of
all finite same-population joint laws between two realizations identifies
bounded cylinder functions isometrically; density extends this to unital
surjective isometries of the two observable L2 spaces. They preserve bounded
coordinate operations and pairings. Truncation transfers the unbounded w,c
and every L2 seed. Because both oriented action answers are retained jointly,
these isometries intertwine each current action on bounded probes and hence
on the completed spaces. Actual adjunction again makes the observable pair
reducing. The restarted Euler/one-reference argument from Sections 5--6,
now starting at s, proves invariance of the remaining target path in those
current spaces. Transport that path and its HS increments by the isometries,
extend the increments by zero on the complementary block, and leave the
matching realization's complementary initialized action unchanged. This
constructs its strong continuation. Equation (2) is preserved by the
isometries, and the tail laws of c,q transfer because their joint probes
are retained. Section 6 then proves uniqueness against any strong competing
continuation with bounded raw norms on the compact remaining interval.
Thus equality of the complete current hierarchy determines reached
continuation without history, also for unbounded readout. This assertion
does not give existence for arbitrary formal hierarchy sequences or for
an unmatched state after switching the data law.

## 8. Separate finite numerical consistency

The outer theorem is an exact-real population theorem. The following inner
construction removes its infinite population laws, still with no width n.

At fixed N use a positive source regularizer epsilon in the finite initializer
and approximate its finitely many Gaussian expectations by deterministic
finite cubature. A completely explicit convergence family is to quantize a
standard k-dimensional Gaussian onto mesh `1/Q` in `[-Q,Q]^k`, sending the
outside mass to zero and using exact Gaussian cell probabilities. Coupling
each Gaussian to its quantized value proves convergence in every finite
Wp: the inside error is at most `sqrt(k)/Q`, while the outside Gaussian
p-moment tends to zero. Polynomial moments are uniformly integrable by the
same coupling and a larger Gaussian moment. Consequently continuous
polynomially bounded functions have convergent integrals, also when their
finite coefficient vectors converge, by uniform continuity on a compact box
and the common moment tail off it. Gaussian cell probabilities themselves
admit finite precision approximation by integration of their continuous
density on compact intervals and Gaussian tail truncation.

For fixed epsilon, construct each source prefix from its empirical operand
Gram plus `epsilon I`; every pivot is positive. Apply the preceding cubature
fact inductively to each coefficient, Gram and frozen named-source derivative
in (4). The complete finite graph consists of the smooth probe dictionary,
so all needed envelopes and continuity were proved in Section 2. This gives
initializer convergence as Q increases. Replay the resulting joint marks
with coefficients frozen on a separate P-point cubature; this gives joint
W2 convergence of `(b1,g)` and b2. Do not refit source coefficients in replay.
After Q increases, remove epsilon. Couple each finite source covariance by
its positive semidefinite square root times a standard Gaussian. Square
roots are continuous at singular covariance: bounded subsequences have
positive semidefinite limits whose square is the limiting matrix, and
uniqueness of its positive square root identifies every subsequential limit.
Finite coefficient induction then proves the unregularized source limit.
This argument does not assert continuity of singular Cholesky factors.

At fixed N the feature ridge stays positive. If the raw feature envelopes
are `B_l,j`, exact and empirical normalization satisfy

\[
 |b_l|\le\left(\sum_j B_{l,j}^2/\eta_N\right)^{1/2}.
                                                               \tag{24}
\]

Thus all mark approximations have a common fixed-order bounded envelope,
their joint laws converge in W2, and D converges in Frobenius norm.

Here is the needed population-quadrature stability with unbounded phi.
Couple two lower joint mark laws and two upper mark laws and let

\[
 e=\|w-\widetilde w\|_2+\|c-\widetilde c\|_2+
          \|M-\widetilde M\|_F,\quad
 \rho_b=\|b_1-\widetilde b_1\|_2+
          \|b_2-\widetilde b_2\|_2.
\]

The energy proof and the noncontractive version of (12) give common
fixed-order bounds for w in L2 and c, q in L-infinity, for convergent mark/D
sequences. The only modified contraction compared with bounded activation is

\[
 |a-\widetilde a|
 \le\|b_1-\widetilde b_1\|_2\,\|\phi(w\cdot u)\|_2
       +L_1D_1|u|\,\|w-\widetilde w\|_2.               \tag{25}
\]

The first term uses Cauchy--Schwarz, not a supremum bound on the first hidden
feature. All other factors in the upper finite action are bounded or finite
scalars. Product subtraction therefore bounds `Z2,H2,f,d,q` differences in
L2 or Euclidean norm by `C(e+rho_b)`. The lower-gate difference is bounded
by `D2 ||qtilde||infinity |u| ||w-wtilde||2`. Hence drift differences have
the same bound, and integration gives

\[
 \sup_{t\le T}e(t)\le e^{CT}
  \left[\|g-\widetilde g\|_2+\|D-\widetilde D\|_F
                              +CT\rho_b\right].        \tag{26}
\]

Constants may depend on N, feature envelopes, the fixed T, and common D/g
moment bounds; they need not be uniform in N. The finite data sum is exact.
If a separately represented compact data law is added, the same fixed-order
subtractions give an extra `C W1(mu,mutilde)` in drift: input differences
cost `D1||w||2|u-v|`, and q is bounded at fixed order. This optional inner
consistency statement does not extend target premise S to continuum laws.

After atomic replay there are finitely many moving scalar coordinates.
Their ODE is locally Lipschitz for phi satisfying (1); it need not be smooth.
Its exact solution exists globally by the same weighted energy argument.
Explicit Euler (or Heun) converges uniformly on each fixed horizon as the
mesh tends to zero. For completeness stop nodes/stages in a slightly larger
compact state ball around the exact solution. Its speed and Lipschitz
constant are finite; the one-step exact Euler defect is `O(h^2)` and Heun
differs from Euler by `O(h^2)`. The discrepancy recurrence is
`e_(k+1)<=(1+Ch)e_k+Ch^2`. Summing bounds it by `C_T h`, precluding exit
for small h and proving the time limit without a discrete energy identity.

**Necessary activation-evaluation qualification.** An executable arbitrary-
precision statement additionally needs algorithms evaluating phi and phi'
locally uniformly on compact intervals, together with an input representation
for the fixed data. Regularity (1) alone does not provide computability: a
noncomputable additive constant can be added to a fixed smooth bounded-
derivative nonaffine activation without leaving the class. Thus a universal
literal numerical algorithm for all unspecified functions in (1) is not a
consequence of this theorem. Given the stated evaluation interface, at fixed
finite parameters every operation and positive-pivot initialization is a
finite continuous computation; locally uniform primitive consistency proves
its precision limit. An activation formula admitting such evaluation meets
this additional interface; no higher activation derivatives are needed.

The justified nested limit is therefore

\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}
 \lim_{Q\to\infty}\lim_{P\to\infty}
 \lim_{h\downarrow0}\lim_{p\to\infty},                 \tag{27}
\]

where p is arithmetic precision and its limit is conditional on that
evaluation interface. With exact-real activation evaluation, omit the p
limit and retain a mathematical cubature/time consistency theorem. Equations
(23), (25)--(26), and the same initial reconstruction (21) give prediction,
joint paired-law and RMS consistency at each stage. The closure-order limit
is last; no arbitrary diagonal, rate, or accuracy-to-resolution rule follows.

At fixed quadrature counts P1,P2, a complete checkpoint stores b1,g,w and
lower weights; b2,c and upper weights; M,D; finite data; activation and
arithmetic metadata. Its scalar count, excluding data/metadata, is

\[
 P_1(d_1+2d+1)+P_2(d_2+2)+2d_1d_2.                    \tag{28}
\]

All correlations with current coordinates are retained by these joint nodes.
Both action directions use M and `M^T`. Initializer source tables may be
discarded before evolution. A step uses a constant number of state/stage
arrays and no elapsed-step history; exact checkpoint serialization permits
identical continuation at step endpoints. A new mesh from an interpolated
interior time need not reproduce the previous discrete mesh. Storage and
work depend on dictionary, cubature, data and precision, never neural width.
At any fixed precision, scalar bit storage is finite and must be counted in
addition to (28); there is no arbitrary information encoded at zero bit cost.

## 9. First-round verdict and scope audit

The conditional route is complete at the proof level stated here:
S + E imply an explicit autonomous dense population closure converging in raw
row/HS/readout distance, uniformly on the fixed horizon, with both action
directions and the declared paired observations. Fixed-order cubature and
time consistency require no additional target tail assumption. Literal
finite precision additionally requires an activation-evaluation interface.

The following distinctions are decisive.

| Claim | Status in this file |
|---|---|
| Equations (8), actual transpose, saved current state | Exact construction |
| Fixed-order global well-posedness and own-state restart | Proved using energy and bounded feature envelopes |
| Vanishing omitted-action/increment production | Proved on compact sets of a strong target, after observable-space invariance |
| Propagation with unbounded c and q | Proved from target-only exponential tails, or (20) |
| Full C1,1 activation in training equations | Retained; no activation smoothing or replacement in the closure |
| Smooth initializer at arbitrary dictionary depth | Proved by an activation-independent probe language |
| Existence/tails of the intended target on its demanded horizon | External S/E obligation, not proved here |
| Identification with original Gaussian finite GF | Separate source/finite-program bridge obligation |
| Uniform law-family or activation-class convergence rate | Not asserted |
| Practical accuracy, useful cost, or empirical validation | Not asserted or run |

The strongest remaining obstruction to the original target is therefore the
source/identification interface, not dense closure or unbounded activations
inside the fixed-order equations. If source control is available only on a
short interval, this theorem is correspondingly only a short-interval result;
it cannot convert that into the maintained tanh time-40 theorem. If S/E fail,
this conditional route says nothing about impossibility of a different
closure. The single next dependency to resolve is the target strong-flow and
tail theorem at the requested fixed horizon and law family.

### Source and process record

Scientific inputs used: `docs/NOTATION.md`; the complete maintained
`global_nonlinear.md` C.4.7.8--10 (including H3/H40); C.1 for the exact
C1,1/scaling conventions; and special-data III.F for the finite Gaussian
program, common action/adjoint, HS, and multiplier facts. The present argument
reproves the adapted comparison, energy, continuation, and quadrature
stability steps because the maintained bounded-tanh versions do not directly
cover the current unbounded activation class. No other study or active proof
route was used. No code, maintained file, Git state, or experimental output
was modified.
