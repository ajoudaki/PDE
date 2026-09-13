# Independent C-H4 route: extending the compatible closure through physical time 40

Status: frozen candidate proof, independently derived within the assigned input
scope; not a promotion review or an established addition. No experiments, code
changes, or Git writes were performed. This file is the route's complete output.

## 1. Claim and exact scope

The compatible initialized-word/Chebyshev dictionary, positive ridge filters,
and autonomous closure of C.4.7.10.B extend qualitatively to physical time
`T=40` for every separately fixed law in the neighborhood furnished by
C.4.7.1–5. The dictionary and ridge do not change. The proof uses the actual
time-40 trajectory as the sole tail-bearing comparison endpoint. It does not
continue the short-time source-cap estimate of C.4.7.10.A, which would be an
unsupported change of horizon.

There is one necessary distinction in the numerical formulation. Every Borel
law admits a sequence of finitely represented atomic approximations, but an
arbitrary Borel law does not come with an algorithm for producing that
sequence. The population closure below covers every separately fixed law in
the time-40 neighborhood. Its finite numerical realization covers a fixed law
when a sequence of finite rational data laws converging to it in `W1` is
supplied. Existence of such a sequence holds for every law. Effective access
to it is an input contract, not a conclusion of the time-40 theorem. No claim
is made that the particular two-arc family of H3 belongs to that neighborhood.

Fix `Y>=1`, `T=40`,

\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|,
\]

and one `mu` in `U_Y={mu: W1(mu,nu_*)<delta_Y}` from C.4.7.1–5. Here
`nu_*` gives masses one half to `(sqrt(2)e_1,+1)` and
`(sqrt(2)e_2,-1)`. Use exactly the bias-free two-hidden-layer tanh network,
stored independent Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`,
unhalved mean-square loss, and physical GF. All population expectations are
within their own layer. The initialization is `(w,K,c)=(g,0,0)`,
`g~N(0,I_2)`, with one retained initialized Gaussian action `A_0` and its
actual Hilbert adjoint. Only `K` is Hilbert–Schmidt; `A=A_0+K` is bounded.
Write `H_l=L2(Omega_l)` for the two population Hilbert spaces.

Write `phi=tanh`, `u=x/sqrt(2)`, and

\[
 \begin{split}
 H^1(u)&=\phi(w\cdot u),& Z^2(u)&=AH^1(u),&H^2(u)&=\phi(Z^2(u)),\\
 \Delta^2(u)&=c\phi'(Z^2(u)),&Q(u)&=A^*\Delta^2(u),
 &f(u)&=E_2[cH^2(u)].
 \end{split}                                                     \tag{1}
\]

The exact raw vector field is

\[
 \mathcal F_\mu(w,K,c)=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\Delta^2(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right),\qquad r=f-y.                    \tag{2}
\]

The following conclusions are proved below.

1. Every fixed exact order `N` is globally well posed in its characteristic
   class and restarts from its own saved joint population state. Its raw lift
   converges to the canonical solution of (2), uniformly on `[0,40]` in row
   `L2`, learned-increment HS, and readout `L2`.
2. Predictions converge in `C([0,40] x S1)`. Each separately fixed admitted
   same-layer observation tuple converges uniformly in time in Euclidean
   `W2`, with its second moments. In particular initial/current hidden pairs,
   their training averages and RMS displacements converge. Risks converge
   uniformly in time.
3. Given finite rational data laws `lambda_m -> mu` in `W1`, the finite
   numerical construction with H3's initializer, source regularization,
   cubature, and Heun evolution has the same iterated convergence when
   `T=40`. The order is arithmetic precision, time mesh, data resolution,
   population cubature, initializer cubature, source regularization, then
   closure order. No quantitative rate, arbitrary diagonal, error certificate,
   or algorithm for choosing sufficient resolutions is asserted.
4. The limiting observations have the actual finite-network interpretation
   of C.4.7.1–5, with the actual finite random readout retained. This does not
   assert a simultaneous closure-order/width limit or subtract a finite matrix
   from a population action.

All claims are for each separately fixed law. Uniform convergence over the
whole law neighborhood and all-time convergence are outside the conclusion.

## 2. Established inputs and the two horizon-dependent facts

C.4.7.1–5 supplies a strong solution

\[
 \theta_\mu\in C^1([0,T];\mathcal E),\quad
 \mathcal E=L^2(\Omega_1;\mathbb R^2)\oplus\mathcal S_2(H_1,H_2)
                       \oplus L^2(\Omega_2),
\]

on the prescribed canonical carrier, and proves its uniqueness and reached
restart. Its energy and readout bounds imply

\[
 \mathcal L_\mu(t)\le Y^2,\qquad
 \|c(t)\|_\infty\le2Yt.                                  \tag{3}
\]

The proof below needs two consequences through the entire `[0,40]`, not just
through H3's original short interval.

**Gaussian marginal reverse tails.** There exist `a,M_tail>0` such that

\[
 \sup_{t\le T,u\in S^1}\tau_R(Q(t,u))\le M_{\rm tail} e^{-aR^2},\qquad R\ge1,
 \quad\tau_R(V)=\|V1_{|V|>R}\|_2.                         \tag{4}
\]

This uses the full source proof of C.4.7.3, not a bounded-operator estimate
on arbitrary `L2` inputs. Here is the tail passage to the constructed
trajectory explicitly. Its sufficiently fine finite-law Euler programs have
the uniform passive bounds `tau_R(Q_j(t,u))<=M_0 exp(-a_0 R^2)` by
C.4.7.3. C.4.7.4 constructs the path as their uniform strong raw limit.
At each fixed `(t,u)`, field continuity gives `Q_j(t,u)->Q(t,u)` in `L2`.
The map `V -> (|V|-R)_+` is 1-Lipschitz on `L2`, and

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2
 =2\lim_j\|(|Q_j|-R)_+\|_2
 \le2M_0e^{-a_0R^2}.
\]

The constants do not depend on `(t,u)`, so this proves (4) for `R>=2`
after rescaling. Enlarge `M_tail` to cover `1<=R<2`, using the uniform `L2`
bound. Integration of the individual bound against `mu` preserves it. No
tail estimate for a supremum of random fields has been used.

**The initialized observable subspaces contain the full trajectory.** Let
`H_l^obs` be the `L2` spaces of the sigma fields generated by all bounded
initialized words of H3's full grammar, with the unbounded Gaussian seeds
included by their bounded truncations. The bounded-word span is dense there
by C.4.7.8.5's Fourier-cylinder argument. Both `A_0` and its actual adjoint
map the appropriate observable space into the other; adjunction makes these
a reducing pair. This is an initialization fact, independent of horizon.

Every finite-law raw Euler step from initialization keeps `w,c` in those
spaces and `K` supported between them. Indeed bounded coordinate operations
preserve the generated sigma fields. Applying `A_0+K` or its adjoint
preserves the spaces if the previous increment is supported there. Each
middle update is a finite sum of ranks with factors in the respective
spaces, and each row/readout update is a finite sum of measurable `L2`
fields in its space. This proves the claim by induction from `g,0,0`.
The affine interpolants preserve the same properties. The spaces and the
corresponding supported HS block are closed, so C.4.7.4's strong completion
passes them to `theta_mu(t)` for all `t<=40`. The difference quotients of
`K(t)` belong to this closed HS block, hence so does `K'(t)`.

This derives the required time-40 invariance directly from the time-40
construction; it does not reuse the short-time completion of H3.A beyond
its domain.

## 3. The unchanged finite dictionary and exact closure

Use exactly H3.B's initialized words. Its polynomial core uses

\[
 X_1=(\tanh g_1,\tanh g_2,\tanh p_1,\tanh p_2),\quad
 X_2=(\tanh\xi_1,\tanh\xi_2),\quad
 \xi_i=A_0\tanh g_i,\quad p_i=A_0^*\tanh\xi_i.
\]

At order `N`, retain the total-degree-at-most-`N` Chebyshev products of the
appropriate `X_l`, followed by every bounded valid initialized-word code
through `N` not already present literally. The code, sort rules, order and
source recursion are exactly C.4.7.10.B/C.1–2. In particular the countable
tail includes both orientations on arbitrary bounded words permitted by the
grammar; the polynomial core alone is not assumed dense in the full
observable space. Literal duplicates are not removed by numerical rank.

Let `psi_l,N` be the retained raw column, and define

\[
 G_l=E_l[\psi_l\psi_l^T],\quad
 \eta_N=[1024(N+1)^2]^{-1},\quad
 L_lL_l^T=G_l+\eta_NI,\quad b_l=L_l^{-1}\psi_l.             \tag{5}
\]

Every feature is bounded at fixed `N`. All its coefficients and complete
joint initialization laws are computed from the finite canonical Gaussian
program before training. No target trajectory, time mesh or data law enters
them. Retain

\[
 \lambda_{1,N}=\operatorname{Law}_1(b_1,g),\qquad
 \lambda_{2,N}=\operatorname{Law}_2(b_2),\qquad
 D_N=E_2[b_2(A_0b_1)^T].                                  \tag{6}
\]

The expectation defining `D_N` uses the joint program including the
forward calls and all required reverse calls. `D_N^T` is its reverse
contraction; no independent reverse random action is introduced.

The saved exact state consists of `M in R^(d_2 x d_1)` and the two joint
populations `Gamma_1=Law(b_1,g,w)` and `Gamma_2=Law(b_2,c)`, together with
fixed `D_N` and the law-input interface. Initially `M=D_N,w=g,c=0`. Put

\[
 \begin{split}
 a(u)&=E_1[b_1\tanh(w\cdot u)],&
 h_2(u)&=\tanh(b_2^TMa(u)),\\
 d(u)&=E_2[b_2c(1-h_2(u)^2)],&
 q(u)&=b_1^TM^Td(u),\\
 f_N(u)&=E_2[ch_2(u)],&r_N(u,y)&=f_N(u)-y.
 \end{split}                                               \tag{7}
\]

The characteristics and the matrix solve

\[
 \begin{split}
 w'&=-2\int r_N(1-\tanh(w\cdot u)^2)q(u)u\,d\mu,\\
 c'&=-2\int r_Nh_2(u)\,d\mu,\\
 M'&=-2\int r_Nd(u)a(u)^T\,d\mu .
 \end{split}                                               \tag{8}
\]

All operations use only the current state and fixed input law. The two
populations are joint laws on finite-dimensional domains; they are not yet
finite scalar storage. Section 7 supplies their finite cubatures.

For analysis only, define `U_l v=b_l^T v`, `Q_l=U_lU_l^*`. Matrix algebra gives

\[
 U_l^*U_l=I-\eta_NL_l^{-1}L_l^{-T}\le I,\qquad
 Q_l=S_l(G_l+\eta_NI)^{-1}S_l^*,                           \tag{9}
\]

where `S_l v=psi_l^T v`. Thus both `U_l` and `Q_l` are contractions, and
`Q_l` is positive. The learned lift and initialized filtered action are

\[
 K_N=U_2(M-D_N)U_1^*,\qquad B_N=Q_2A_0Q_1,
 \qquad A_N=B_N+K_N=U_2MU_1^*.                            \tag{10}
\]

These are proof realizations, not extra saved operator coordinates.
The matrix equation implies exactly

\[
 K_N'=Q_2\left[-2\int r_N\Delta_N^2(u)\otimes H_N^1(u)\,d\mu\right]Q_1.
                                                               \tag{11}
\]

Indeed `U_2d=Q_2 Delta_N^2` and `U_1a=Q_1 H_N^1`. In particular the
middle evolution retains both filters and the actual transpose.

## 4. Fixed-order existence and bounds for the longer horizon

For fixed `N`, set `K_l=(sum_i ||b_l,i||_infty^2)^(1/2)<infinity`.
Work on the fixed mark probability spaces with unknowns `w=g+v`,
`v in L-infinity(R2)`, `c in L-infinity`, and finite `M`. On a bounded
ball of these variables, (7)–(8) is locally Lipschitz in the sum of their
supremum/Frobenius norms. To verify it, subtract each finite product one
factor at a time; `|b_l|<=K_l`, `|u|=1`, `|tanh'|<=1`, and
`Lip(1-tanh^2)<=2` bound all factors and differences. The unbounded fixed
`g` occurs only inside these bounded Lipschitz gates.

Integrating (8) on continuous paths in a closed ball is a contraction when
the interval length times this Lipschitz constant is less than one and its
length times the speed bound fits in the ball. Iteration constructs the
unique local solution; the following bounds continue it through any fixed
finite horizon.

Differentiation of `f_N` gives the three gradients in (8). For example its
matrix variation is `d(u)^T delta M a(u)`; its row variation, after actual
adjunction, is `E_1[phi'(w·u)q(u)u·delta w]`. The bounded characteristic
derivatives justify differentiating the probability integrals. Consequently

\[
 \mathcal L_N'=-\|w_N'\|_2^2-\|c_N'\|_2^2-\|M_N'\|_F^2,
 \qquad\mathcal L_N(0)=\int y^2d\mu\le Y^2.              \tag{12}
\]

Hence `int |r_N| dmu<=Y`. Using (9), `|a|<=1` and
`|d|<=||c_N||2`, and `||A_0||<=2` supplied by the canonical action,

\[
 \begin{split}
 \|c_N(t)\|_\infty&\le2Yt,&
 \|M_N-D_N\|_F&\le2Y^2t^2,\\
 \|K_N\|_{\rm HS}&\le2Y^2t^2,&
 \|A_N\|_{\rm op}&\le2+2Y^2t^2,\\
 \|w_N(t)\|_2&\le\sqrt2+4Y^2t^2+2Y^4t^4.
 \end{split}                                               \tag{13}
\]

For the second inequality, `||M'||F<=2Y ||d|| |a|<=4Y^2t`.
For the row inequality,
`||w'||2<=2Y ||A_N||op ||c_N||2<=4Y^2t(2+2Y^2t^2)` and integrate.
Also `||D_N||op<=2`, and pointwise

\[
 \|w_N'(t)\|_\infty\le4Y^2tK_1\|M_N(t)\|_{\rm op}.
\]

Thus `v,c,M` remain in a bounded existence ball on `[0,40]` for fixed
`N`. Their bounded speeds give a Cauchy endpoint at any finite maximal
time; the local contraction there extends the solution. No smallness of
`T` enters. The constants in (13) are uniform in `N`; the supremum
increment bound needed only for fixed-order existence may depend on `N`.

For a reached restart, use the saved joint laws as the initial mark spaces,
with their current `w,c` as initial labels. The same local construction and
energy calculation applies with the saved energy and readout bound. The
row drift is Lipschitz in its individual moving row and the readout drift
does not depend on its individual `c` except through population
contractions. Coupling equal saved coordinates therefore proves uniqueness
of the continuation. It equals the original restriction and needs no
training history. This assertion concerns characteristic solutions, without
claiming uniqueness for arbitrary uncontrolled distributional solutions.

## 5. Omitted-action sources and the time-40 comparison

The retained raw spans are nested and dense in `H_l^obs`, because every
bounded code eventually appears and the rational-word density proof is
independent of time. For a vector `S_N v` in a fixed earlier span, pad its
coefficient vector by zeros. Diagonalizing the raw Gram gives

\[
 \|(I-Q_{l,N})S_Nv\|_2^2
 \le\frac{\eta_N}{4}|v|^2\longrightarrow0.                \tag{14}
\]

Approximation by that dense span and `||I-Q||<=1` gives `Q_l,N -> I`
strongly on `H_l^obs`. It follows from (10), using both reducing spaces,
that `B_N -> A_0` and `B_N^* -> A_0^*` strongly on their respective
observable spaces, with uniform operator bounds. For example,

\[
 \|(B_N-A_0)V\|_2\le2\|(Q_1-I)V\|_2+\|(Q_2-I)A_0V\|_2.
\]

Uniformly bounded strongly convergent operators converge uniformly on a
compact set: take a finite radius-`b` net; the errors at its finitely many
centers vanish, while each point-to-center error is at most a common
operator bound times `b`; then send `b` to zero.

The exact fields `H^1(t,u),Delta^2(t,u)` form compact `L2` sets for
`(t,u) in [0,40] x S1`. Forward/action continuity is immediate by subtraction.
For the upper backward product, use boundedness of `c` and the Lipschitz
gate in (1). The established strong raw path supplies their joint
continuity. The continuous HS curve `K'(t)` is compact and supported in
the observable block by Section 2. Define solely for the proof

\[
 \begin{split}
 \epsilon_N={}&\sup_{t,u}\|(B_N-A_0)H^1(t,u)\|_2
       +\sup_{t,u}\|(B_N^*-A_0^*)\Delta^2(t,u)\|_2\\
       &+\sup_t\|Q_2K'(t)Q_1-K'(t)\|_{\rm HS}.
 \end{split}                                               \tag{15}
\]

Then `epsilon_N -> 0`. Only the last term needs more explanation:
finite sums of rank-one tensors are dense in HS, by truncating its
square-summable matrix coefficients in orthonormal bases. For one tensor
`a tensor b`, the filtered tensor is `(Q_2a) tensor (Q_1b)`, which
converges in HS by strong convergence of its two factors and their
bounded norms. HS contraction by each `Q_l` bounds the discarded
remainder. A finite net of the compact derivative curve makes this
approximation uniform in time. Neither (15) nor its convergence is an
input to the finite equations or a rule for choosing `N`.

Lift the exact closures to the common canonical carrier and set

\[
 e_N=\|w_N-w\|_2+\|K_N-K\|_{\rm HS}+\|c_N-c\|_2.
\]

The target satisfies bounds analogous to (13), from (2)–(3). Thus all
paths share a bounded raw/action ball on `[0,40]`, independent of `N`.
The following subtractions account for every propagation term.

First,

\[
 \begin{split}
 \|H_N^1-H^1\|_2&\le e_N,\\
 Z_N^2-Z^2&=A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A_0)H^1,\\
 \sup_u\bigl(\|Z_N^2-Z^2\|_2+\|H_N^2-H^2\|_2
                         +|f_N-f|\bigr)&\le C(e_N+\epsilon_N).
 \end{split}                                               \tag{16}
\]

For the prediction subtract `c_N-c` first, and use the bounded reference
readout to multiply the hidden difference. Next

\[
 \Delta_N^2-\Delta^2=(c_N-c)\phi'(Z_N^2)
                       +c[\phi'(Z_N^2)-\phi'(Z^2)],
\]

so its `L2` norm is at most `C(e_N+epsilon_N)`. Since

\[
 Q_N-Q=A_N^*(\Delta_N^2-\Delta^2)
                  +(K_N-K)^*\Delta^2+(B_N^*-A_0^*)\Delta^2,
\]

the same bound holds for the reverse-query difference, uniformly in `u`.
For the remaining lower gate, split the unchanged target `Q` at `R>=1`:

\[
 \begin{split}
 &\|\phi'(w_N\cdot u)Q_N-\phi'(w\cdot u)Q\|_2\\
 &\hspace{1em}\le C(e_N+\epsilon_N)+2R e_N+2\tau_R(Q(t,u)).
 \end{split}                                               \tag{17}
\]

Indeed the gate difference is at most `2|(w_N-w)·u|` below the cutoff
and at most two above it. The reference's Gaussian tail (4) is the only
tail invoked; arbitrary bounded actions are not claimed to preserve
higher moments.

The row velocity difference now follows by first subtracting residuals
and then the backward products. Residual differences are bounded by (16),
residuals and reverse `L2` norms have common finite bounds, and integration
of (17) gives `C(1+R)(e_N+epsilon_N)+C M_tail exp(-aR^2)`.
The readout velocity difference uses (16) and bounded activations. For
the learned increment use exactly (11):

\[
 \begin{split}
 K_N'-K'={}&Q_2\{\mathcal F_{K,\mu}(w_N,A_N,c_N)
                  -\mathcal F_{K,\mu}(w,A,c)\}Q_1\\
           &+(Q_2K'Q_1-K').
 \end{split}                                               \tag{18}
\]

Here `mathcal F_K` is the middle rank integral in (2). Subtract residuals
and its two factors, using

\[
 \|a\otimes b-\bar a\otimes\bar b\|_{\rm HS}
 \le\|a-\bar a\|_2\|b\|_2+\|\bar a\|_2\|b-\bar b\|_2.
\]

The first term in (18) is at most `C(e_N+epsilon_N)`, and its second
is at most `epsilon_N`. This checks the HS component without replacing it
by an operator-norm discrepancy.

Norms of strong Hilbert-space curves are absolutely continuous. Their
upper derivatives are bounded by the corresponding derivative norms,
including at zero component norm. Summing the preceding inequalities gives

\[
 D^+e_N(t)\le C(1+R)(e_N(t)+\epsilon_N)+CM_{\rm tail} e^{-aR^2},
 \qquad e_N(0)=0.                                        \tag{19}
\]

For fixed `R`, multiply the scalar integral inequality by
`exp(-C(1+R)t)` and integrate. It yields

\[
 \sup_{t\le T}e_N(t)
 \le CT e^{C(1+R)T}\bigl[(1+R)\epsilon_N+M_{\rm tail} e^{-aR^2}\bigr]. \tag{20}
\]

Take `N -> infinity` with `R` fixed, using (15); then take
`R -> infinity`. The exponent `-aR^2+C(1+R)T` tends to minus infinity
for every fixed finite `C,T`, in particular `T=40`. Therefore

\[
 \sup_{t\le40}e_N(t)\longrightarrow0.                     \tag{21}
\]

The larger horizon increases constants but causes no threshold condition
on the positive Gaussian exponent. This is the new comparison closure.
It uses neither a tail bound on approximate trajectories nor an
order-uniform Lipschitz constant based on their feature supremum envelopes.

For completeness the same argument proves uniqueness whenever needed on
the target carrier: compare a competing bounded strong path to the
constructed path, use only the latter's tails, omit `epsilon_N`, and start
with zero discrepancy. Equation (20) with only its tail term forces equality
as `R -> infinity`. On a reached subinterval the same constants can be
chosen from the two compact paths. Existence of the reached continuation
comes from restriction of the constructed path. Thus no arbitrary formal
hierarchy uniqueness or arbitrary ambient restart theorem is inserted.

## 6. Whole-circle predictions, paired laws, RMS, and risk

Equation (16) and (21) prove whole-circle prediction convergence uniformly
in time. They also prove uniform `(t,u)` `L2` convergence of the current
hidden fields. The initial lower field is exact. The initial upper field
uses `B_N tanh(g·u)` and converges uniformly in `u` by strong convergence
on the compact initial hidden-input set.

For a fixed admitted observation graph, use induction on its instructions.
Its seeds converge by (21) and the preceding initial-field argument.
Affine and globally Lipschitz operations preserve uniform-time `L2`
convergence. Bounded products have a common syntax envelope at the fixed
marks and satisfy

\[
 \|V_NW_N-VW\|_2\le\|V_N\|_\infty\|W_N-W\|_2
                                  +\|W\|_\infty\|V_N-V\|_2.
\]

For an action node,

\[
 A_NV_N-AV=A_N(V_N-V)+(K_N-K)V+(B_N-A_0)V.                 \tag{22}
\]

The first two terms vanish by uniform bounds and (21). The target curve
`V(t)` is compact in `L2` by the same finite induction, so the last term
vanishes uniformly by strong convergence. The identical proof works for
the actual adjoints. A fixed bounded continuous gate times a named `L2`
field is treated by subtracting the field error, truncating the fixed
target field, and using bounded convergence in probability for the gate
on the truncated part. Compactness of the target curve makes its `L2`
tails uniform by a finite net. Equivalently, a contrary sequence of times
has a convergent subsequence, where this fixed-field multiplier argument
gives a contradiction. This handles the admitted bounded-gate
pushforwards without an `L2` product algebra assumption.

For a same-layer tuple `V=(V_1,...,V_k)`, the common canonical carrier
gives the coupling

\[
 \mathcal W_2(\operatorname{Law}(V_N),\operatorname{Law}(V))^2
                \le\sum_i\|V_{i,N}-V_i\|_2^2.             \tag{23}
\]

It preserves all specified initial/current and inter-input correlations.
Quadratic contractions converge because

\[
 |E[U_NV_N]-E[UV]|\le\|U_N-U\|_2\|V_N\|_2
                                  +\|U\|_2\|V_N-V\|_2.
\]

For the specifically requested training-averaged paired laws let

\[
 \mathcal P_{l,N}(t)=\operatorname{Law}_{\Omega_l\otimes\mu}
       (H_N^l(0,u),H_N^l(t,u)),\qquad
 \mathcal P_l(t)=\operatorname{Law}_{\Omega_l\otimes\mu}
       (H^l(0,u),H^l(t,u)).
\]

The same sample/input is used for both pair coordinates. Coupling on this
product space and the uniform input estimates prove
`sup_t W2(P_l,N(t),P_l(t))->0`. If `R_l,N` denotes the `L2` norm of the
paired difference, then

\[
 |R_{l,N}(t)-R_l(t)|
 \le\|(H_N^l(t,u)-H_N^l(0,u))-(H^l(t,u)-H^l(0,u))\|_{L^2(\Omega_l\otimes\mu)}.
                                                               \tag{24}
\]

This tends to zero uniformly in time, including at zero displacement.
Second moments and squared displacements follow as well.

Both predictions are bounded by `2YT`; hence

\[
 \sup_{t\le T}|\mathcal L_N(t)-\mathcal L_\mu(t)|
 \le2(2YT+Y)\sup_{t,u}|f_N(t,u)-f_\mu(t,u)|\longrightarrow0. \tag{25}
\]

For changing data approximations one also subtracts the integral of the
fixed target loss against the two laws. Its integrand is continuous on
the compact data space, uniformly over the compact time interval; the
forward bounds give a common input Lipschitz constant. Thus `W1`
convergence controls this additional term. For paired laws under changing
data, couple inputs; on the bounded circle `E|u-v|^2<=2E|u-v|`, so the
input `L2` Lipschitz bounds give a vanishing additional transport cost.

The finite GF conclusions in C.4.7.1–5 now identify the target as the
actual network limit. They apply to exactly this law, horizon, loss,
mobilities and observation class. Its finite Gaussian readout has variance
`1/n^2` and is retained in the finite proxy construction; its limiting
zero value is not a zero-readout finite model. Predictions and risk pass by
the uniform convergence just used, and paired moments by the same-layer
observation theorem. No finite-width comparison uses a cross-carrier
operator difference. Where C.4.7.7's additional binary-label and radius
hypotheses hold, its risk/activity conclusions apply to this same target;
no such performance assertion is extended to every law in `U_Y`.

## 7. The finite numerical hierarchy through time 40

The finite-dimensional Gaussian initializer is unchanged. At fixed `N`,
regularize generic source Grams by positive rational `varepsilon`, use
`Q` initializer cubature points, replay their fixed coefficients on `P`
population points, and use finite rational data law `lambda_m`. Run Heun
with intended `h=40/J` and the H3 rational elementary operations at
precision `p`. Recompute nonlinear fields on linearly interpolated states
when observing between steps. The law-specific numerical input is
`lambda_m`, not the unknown target trajectory.

All initializer convergence statements of C.4.7.10.C.2 are independent of
training horizon: they concern a fixed finite Gaussian graph before
training. In particular they prove, in order, replay-mark `W2` convergence
as `P -> infinity`, convergence of coefficient/Gram/contraction values as
`Q -> infinity`, and removal of `varepsilon` on complete named source
lists, including singular limiting covariances. Their proof uses joint
Gaussian moment control and continuity of positive semidefinite square
roots, not continuity of singular Cholesky factors. At fixed `N` the
positive feature ridge stays fixed and normalization is continuous.
The bound `|b_l|<=B_l/sqrt(eta_N)` holds throughout these limits, including
empirical mark laws. No empirical contraction property is assumed.

Here are the evolution facts needed to use those limits at `T=40`.

**General mark laws.** Let `|b_l|<=K_l`, `E|g|^2<infinity`, finite `D`,
`|y|<=Y`, and normalized positive population/data measures be given. The
local proof of Section 4 applies unchanged. Its energy identity still
holds because all gradients use exactly those same measures. Now

\[
 \|c(t)\|_\infty\le2Yt,\quad |a|\le K_1,\quad |d|\le2YK_2t,
\]
\[
 \|M(t)-D\|_F\le2Y^2K_1K_2t^2,\qquad
 \|w'(t)\|_\infty\le4Y^2K_1K_2t\|M(t)\|_F.              \tag{26}
\]

These bounds are finite on `[0,40]`. They imply global fixed-order
existence for arbitrary/atomic mark laws and boundedness of the local
existence norms. Unlike (13), these constants may depend on the fixed
feature envelopes; that is acceptable because every inner numerical limit
keeps `N` fixed.

**Coupled stability.** Couple two lower joint laws and two upper mark laws.
With `e=||w-tilde w||2+||c-tilde c||2+||M-tilde M||F` and
`rho_b=||b_1-tilde b_1||2+||b_2-tilde b_2||2`, subtract (7):

\[
 |a-\widetilde a|\le\|b_1-\widetilde b_1\|_2
                                      +K_1\|w-\widetilde w\|_2.
\]

The three factors in `b_2^TMa`, then the factors defining `h_2,f,d,q`,
give a common `C(e+rho_b)` bound in their `L2`/Euclidean norms.
The lower gate difference is multiplied by a pointwise bounded
`tilde q`, because (26) and `|b_l|<=K_l` give
`||tilde q||infty<=K_1 ||tilde M||F K_2 ||tilde c||infty`.
Thus the row comparison has the same bound, without any extra tail
assumption. For a changed input,
`||tanh(w·u)-tanh(w·v)||2<=||w||2 |u-v|`. The other factors inherit
this input bound by subtraction; labels are affine and the final vector
`u` is Lipschitz. Coupling the data laws therefore adds `C W1`.

Integration of the difference equations and the scalar exponential
integrating factor give

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 \|g-\widetilde g\|_2+\|D-\widetilde D\|_F
             +CT\{\rho_b+\mathcal W_1(\lambda,\widetilde\lambda)\}\right].
                                                               \tag{27}
\]

All constants depend only on common `Y,K_l,||D||F,||g||2,T` bounds.
Such bounds hold along each convergent sequence of initializers and marks.
At a reached restart replace the first two terms by the complete saved
state discrepancy; the same proof applies. The forward and paired
observation estimates in Section 6 hold for these couplings also.

**Time mesh.** At fixed `N,varepsilon,Q,P,m`, the exact finite ODE is
smooth. Its Heun stages stay bounded independently of `J`. Put
`B_k=Y+||c_k||infty`. Then

\[
 B_k^*\le(1+2h)B_k,\qquad
 B_{k+1}\le(1+2h+2h^2)B_k\le e^{(2+2T)h}B_k.
\]

Thus all stage values of `Y+||c||infty` are bounded by
`B_*=(1+2T)Y exp((2+2T)T)`. The finite number is large but valid at
`T=40`. Every stage matrix speed is at most
`V_M=2B_*K_1K_2(B_*-Y)`, so all matrix nodes/stages have norm at most
`||D||F+2TV_M`. These bounds make the row speed uniformly bounded too,
by `2B_*K_1K_2(||D||F+2TV_M)(B_*-Y)`. No discrete energy inequality
is assumed. On a slightly enlarged bounded state set the field has a
finite Lipschitz constant. Both the exact step's and Heun's difference
from an Euler step are `O(h^2)`, since the field and its derivative are
bounded there. Therefore node errors satisfy
`e_(k+1)<=(1+Ch)e_k+Ch^2`, which sums to `max e_k<=C_T h`.
Interpolation adds `O(h)`. Thus `J -> infinity` converges uniformly
through time 40 at these fixed outer parameters.

**Arithmetic.** At fixed finite parameters including `J`, the computation
is a finite composition of the same locally consistent rational operations,
Gaussian transforms, source and feature Cholesky steps, and Heun operations
verified in C.4.7.10.C.4. Its proof uses finiteness of the operand set,
positive fixed source/feature pivots, and nonzero required denominators,
not a small horizon. The bounds just proved ensure finite exact operands
at `T=40`; precision is removed before `J` or the outer parameters vary.
The same positive margins therefore imply eventual precision success and
convergence. For general finite rational input lists, weights and unit-circle
coordinates can be supplied exactly; their direct rounding has the same
finite-list consistency. This is a mathematical finite-algorithm claim;
the maintained software API was not inspected or changed in this route.

Together, arithmetic then mesh limits give the finite cubature ODE.
Equation (27) first removes data resolution, then population replay, then
initializer error and source regularization. The resulting exact order is
precisely (5)–(8), whose outer limit was proved in (21). Hence, with `E`
equal to the sum of the whole-circle prediction error, the two uniform-time
paired `W2` errors, the two RMS errors, and the uniform-time risk error,

\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
 \lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}
 \lim_{p\to\infty}E=0.                                   \tag{28}
\]

For the polynomial core the unused source-regularization limit is
vacuous, as in H3. Every inner limit holds at fixed preceding outer
parameters. Additional resource allowances may grow along all refinements;
no fixed-precision or affordable-resource claim is included.

For paired observations at finite arithmetic, normalized nonnegative
returned product weights define their probability laws; their total mass
tends to one in the first limit. Their unnormalized weighted RMS and risk
have the same limit. This observation convention changes no dynamics.

At a numerical step endpoint, retain the finite mark arrays, both weight
lists, current `w,c,M`, initial `g,D`, finite data, and arithmetic/step
metadata. The next step depends only on these values. Exact serialization
therefore reproduces the same subsequent finite computation; working
storage is independent of elapsed step count. The exact population restart
is supplied by Sections 4 and 7's uniqueness. An interpolated interior
observation does not make a restarted Heun mesh identical to the old mesh.

## 8. Law representation and the remaining limitations

For every fixed Borel `mu`, finite rational probability laws approaching it
in `W1` exist. Partition the compact data domain into cells of diameter
tending to zero; choose representatives approximated by points in a fixed
countable dense rational-coordinate subset of the circle and rational
labels in `[-Y,Y]`. Such circle points are dense by the rational
parametrization `((1-s^2)/(1+s^2),2s/(1+s^2))` and density of rational `s`
(with the missing circle point included). Approximate the finitely many
cell masses by nonnegative rational weights summing to one. Moving mass
within a cell costs its diameter, perturbing representatives costs their
uniform approximation error, and changing the finite weights costs at
most the data diameter times their total variation. Choosing each error
to tend to zero proves the assertion. The resulting laws are eventually
in the time-40 neighborhood because `mu` is an interior point, although
the fixed-order numerical stability proof needs only bounded labels.

This is a law approximation existence proof. If the input supplies such
an approximating sequence effectively, each member of (28) is an actual
finite computation from the input. Without such an interface, the exact
population conclusion and the existential finite approximations remain
valid, but an executable uniform procedure for arbitrary Borel `mu` is
not established. No theorem here decides membership in `U_Y` or provides
its useful numerical radius. H3's original rotated-arc API is not
silently repurposed as a time-40 membership certificate.

The precise scientific scope left open is quantitative/effective control:
no rate for the compact-target errors (15), no tolerance-to-order or
diagonal-resolution choice, no numerical certificate, and no common
accuracy bound over all admitted laws. There is no new tail requirement
on a projected trajectory, no high-to-low feedback term omitted from
(18), and no uniqueness gap in the time-40 comparison. The full grammar
tail is essential to (14); deleting it and retaining only the core would
remove the proved density premise.

The route therefore closes the qualitative time-40 extension for the
specified compatible closure, with the stated law-input distinction.
It does not establish a universal finitely executable solver for an
unrepresented Borel law, global dynamics beyond 40, finite-width closure
identification at growing order, or practical performance of any chosen
finite resolution.

## 9. Input provenance, checks, and isolation

The scoped assignment permitted only `docs/NOTATION.md` and complete
C.4.7.1–5, .7–10 of `docs/global_nonlinear.md`, with additional exact
established dependencies to be reported before retrieval. I read those
sources completely (including all displayed source-cap, completion,
comparison, numerical initialization, arithmetic and storage proofs) and
retrieved no additional scientific source. Their established theorem
conclusions are the inputs to this extension; this report is not a fresh
audit of all earlier chapters referenced by them. In particular I did
not separately reread the initialized Gaussian-action construction in
III.F or its upstream probability proofs. No missing new dependency was
found for the horizon extension.

I read the process instructions `AGENTS.md` and `RESEARCH_WORKFLOW.md`,
the required `solve-math-rigorously` skill, and the
`investigate-conjectures` skill plus its research-contract,
adversarial-audit and proof-search-orchestration references. The scoped
assignment replaced ordinary author startup. No study README, history,
other route, other study content, Git history, or prior review was read.
Git status was used only for shared-work metadata and revealed unrelated
concurrent changes; none was changed or staged. No scientific input was
obtained from another agent. The output was frozen before comparison.

Observed HEAD before the write:
`b2108ee5c3c3e702234cb450afd0af395e10c68e`.

Source SHA-256 values at the read/check point:

| File | SHA-256 |
|---|---|
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932` |

Scientific read coverage in that source version: lines 8989–10554 and
11398–13981, with truncated initial reads repaired by smaller complete
reads. The check was a direct derivation of each changed-horizon step and
an adversarial audit of law scope, forward/adjoint consistency, generated
subspace invariance, HS error production, one-sided reference tails,
limit order, same-layer pairing, restart and finite random readout.
No external theorem search, computation, empirical reproduction, formal
verification, independent candidate review or promotion review occurred.

Registry recommendation: **candidate proof complete for the qualitative
extension; ready for independent checking**. The unrepresented-law
computability limitation and lack of quantitative certification are stated
restrictions, not claimed solved subproblems.
