###### D.3. Compatible closure on the explicit time-40 domain

Fix physical time `T=40` and the positive dyadic radius defined in D.1–D.2:

\[
 E_0=8192,\qquad E_{j+1}=2^{E_j}\ (0\le j<10),\qquad
 \rho=2^{-E_{10}}.
 \tag{H40.C1}
\]

Let `V_rho` consist of Borel laws on `sqrt(2) S1 x {+1,-1}` with mass
one half at each label and, almost surely,
`|u-e_1|<=2rho` for label `+1` and `|u-e_2|<=2rho` for label `-1`,
where `u=x/sqrt(2)`. Data Wasserstein distance uses
`|u-v|+|y-z|`. Fix one law `mu` in this class. The exact population
conclusions below apply to every such separately fixed law. The finite
numerical assertion in D.4 uses the represented rational-endpoint laws
of D.1, whose exact radius is (H40.C1).

The model is the bias-free two-hidden-layer tanh network with independent
stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual
`f-y`, and unhalved mean-square-loss physical GF. Write
`H_l=L2(Omega_l)`, `w in L2(Omega_1;R2)`, `c in H_2`, and
`A=A_0+K:H_1 -> H_2`, where only `K` is Hilbert–Schmidt. The retained
initialized action and its actual adjoint have their common canonical
Gaussian realization, `||A_0||op<=2`; initially `(w,K,c)=(g,0,0)` with
`g~N(0,I_2)`. With `phi=tanh`, use

\[
 \begin{gathered}
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),\\
 \Delta^2(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^2(u),\quad
 f(u)=E_2[cH^2(u)],\quad r(u,y)=f(u)-y,\\
 (w',K',c')=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\Delta^2(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).
 \end{gathered}
 \tag{H40.C2}
\]

Every expectation and rank contraction is within its stated layer. Here
\(\mathcal L_\mu=\int(f-y)^2\,d\mu\), and the raw metric is
\(\|(v,L,z)\|_{\rm raw}^2=\|v\|_2^2+\|L\|_{\rm HS}^2+\|z\|_2^2\).
The finite prediction with these conventions is
\(f_n(x)=n^{-1}(W_n^{(3)})^T
\phi(W_n^{(2)}\phi(W_n^{(1)}u))\).

**The reference trajectory supplied by the explicit cap.** D.2 proves
the passive source-row cap for all finite laws in `V_rho` on every
sufficiently fine raw Euler mesh, with constants independent of atom
count, weights and covariance rank. It proves this on the stated
supported class; no comparison of `rho` with an unnamed radius from
C.4.7.1 is needed. Its raw/action bounds, HS comparison estimate,
passive tails and supported finite-law approximations are exactly the
hypotheses of the completion argument in C.4.7.4. Consequently that
argument gives a canonical strong `C1` solution of (H40.C2) through
time 40, unique among strong raw solutions on the same initialized
carrier and uniquely restartable from each reached state. In particular

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta_\mu'(s)\|_{\rm raw}^2ds=1,
 \qquad\|c(t)\|_\infty\le2t,
 \qquad\theta_\mu=(w,K,c).
 \tag{H40.C3}
\]

The same construction supplies constants `a_tail,M_tail>0` such that

\[
 \sup_{t\le40,u\in S^1}\tau_R(Q(t,u))
       \le M_{\rm tail}e^{-a_{\rm tail}R^2},\qquad
 \tau_R(V)=\|V1_{|V|>R}\|_2,\quad R\ge1.
 \tag{H40.C4}
\]

Here is the Gaussian-tail passage explicitly. D.2's finite supported
programs have each passive answer `Q_j=G_j+J_j`, with Gaussian variance
bounded by `(e^80-1)^2` and a deterministic common bound on `|J_j|`.
The scalar Gaussian tail calculation in C.4.7.3 therefore gives uniform
Gaussian RMS tails at their nodes and affine interpolation times. Their
strong raw convergence implies `Q_j(t,u)->Q(t,u)` in `L2` at every
fixed `(t,u)`, by the bounded-multiplier and action continuity used in
C.4.7.4. Since `V -> (|V|-R)_+` is 1-Lipschitz on `L2`,

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2
       =2\lim_j\|(|Q_j|-R)_+\|_2\le2\sup_j\tau_R(Q_j).
\]

Rescale the cutoff and enlarge the prefactor on its remaining bounded
range to obtain (H40.C4). These are individual time/input tails with
common constants, not tails of a random supremum. Averaging them against
the training law preserves the bound.

The fixed-program identification and finite-GF/proxy comparison of
C.4.7.5 also apply on this explicit domain. Indeed their comparison law
and sufficiently fine mesh can be chosen from the supported finite
approximations used in D.2; their raw bounds and passive tails have just
been supplied. The finite program is fixed before width tends to
infinity, its learned ranks have the same HS/Frobenius contraction
identity, and its proxy retains the actual finite initial readout
additively. The law-independent finite GF energy bounds control the
other endpoint of the comparison. This identifies the reference above
with actual finite GF through time 40, for fixed `mu`, and for any
deterministic laws on `sqrt(2) S1 x [-1,1]` approaching `mu` in `W1`
with widths tending to infinity; those actual laws need not satisfy the
support cap. Convergence is in probability in the prediction and joint
second-moment observation senses of C.4.7.5. For iid empirical laws,
sample count and width may grow arbitrarily, with convergence in their
joint probability. No finite random readout has been replaced by zero.

**Dictionary, state and equations.** Retain exactly the full dictionary
of part B: the total-degree-at-most-`N` Chebyshev products in
`(tanh g_1,tanh g_2,tanh p_1,tanh p_2)` and
`(tanh xi_1,tanh xi_2)`, with
`xi_i=A_0 tanh g_i`, `p_i=A_0^* tanh xi_i`, followed by every bounded
valid initialized-word code through `N` not already present literally.
The ordering, rational code, bounded-operand rules and complete finite
source initialization are unchanged. In particular the exhaustive tail
uses both orientations of the same action and is not replaced by the
polynomial core alone. Let `psi_l,N` be the raw retained column and set

\[
 \begin{gathered}
 G_l=E_l[\psi_l\psi_l^T],\quad
 \eta_N=[1024(N+1)^2]^{-1},\quad L_lL_l^T=G_l+\eta_NI,
 \quad b_l=L_l^{-1}\psi_l,\\
 C_N=E_2[\psi_2(A_0\psi_1)^T],\qquad
 D_N=L_2^{-1}C_NL_1^{-T},\\
 \lambda_{1,N}=\operatorname{Law}_1(b_1,g),\qquad
 \lambda_{2,N}=\operatorname{Law}_2(b_2).
 \end{gathered}
 \tag{H40.C5}
\]

All contractions use the complete joint initialization program of B/C.2.
The fixed input `D_N^T` is the reverse contraction. These coefficients,
marks and ridge use no target trajectory or time mesh.

The exact saved state is a finite matrix `M` and the two current joint
population laws `Gamma_1=Law(b_1,g,w)` and `Gamma_2=Law(b_2,c)`, together
with fixed `D_N` and the data-law interface. Initially `w=g,c=0,M=D_N`.
For each `u` compute

\[
 \begin{gathered}
 a_N(u)=E_1[b_1\phi(w_N\cdot u)],\quad
 H_N^2(u)=\phi(b_2^TM_Na_N(u)),\quad
 f_N(u)=E_2[c_NH_N^2(u)],\\
 d_N(u)=E_2[b_2c_N(1-H_N^2(u)^2)],\quad
 Q_N(u)=b_1^TM_N^Td_N(u),\quad r_N=f_N-y,\\
 w_N'=-2\int r_N\phi'(w_N\cdot u)Q_N(u)u\,d\mu,
 \quad c_N'=-2\int r_NH_N^2(u)\,d\mu,\\
 M_N'=-2\int r_Nd_N(u)a_N(u)^T\,d\mu.
 \end{gathered}
 \tag{H40.C6}
\]

The population laws are pushed forward by these characteristics. These
equations are autonomous and have no retained Gaussian-action query,
history, cutoff limit, or omitted hierarchy field in their right side.

For analysis let `U_l v=b_l^T v`, `Q_l,N=U_lU_l^*`. Formula (H3.2)
applies to exactly (H40.C5), so these are positive contractions and
`U_l` is a contraction. On the canonical carrier put

\[
 B_N=Q_{2,N}A_0Q_{1,N},\quad
 K_N=U_2(M_N-D_N)U_1^*,\quad A_N=B_N+K_N=U_2M_NU_1^*.
 \tag{H40.C7}
\]

The current action is bounded and its reverse is its actual adjoint.
In particular, lifting the matrix equation gives exactly

\[
 K_N'=Q_{2,N}\left[-2\int r_N\Delta_N^2(u)\otimes H_N^1(u)\,d\mu\right]Q_{1,N},
 \quad H_N^1=\phi(w_N\cdot u),\quad
 \Delta_N^2=c_N\phi'(A_NH_N^1).
 \tag{H40.C8}
\]

No small operator-norm difference between `B_N` and `A_0` is assumed.

**Energy, existence and restart.** At fixed `N`, all feature coordinates
are bounded. On the fixed joint mark spaces the equations are locally
Lipschitz in bounded `w-g`, bounded `c`, and finite `M`: subtract finite
products, use the feature envelopes, `|u|=1`, and the bounded derivatives
of tanh. The unbounded frozen `g` appears only inside those gates.
Thus the contraction construction in C.4.7.9.4 applies. Its continuation
through the longer interval follows from the following bounds.

The three negative velocities are the gradients for the population
`L2` row/readout metrics and the ordinary coefficient Frobenius metric.
For example `delta f=d_N^T(delta M)a_N`. For atomic populations with
weights `p_{1,i},p_{2,j}`, the ordinary derivatives in `w_i,c_j` equal
`-p_{1,i}w_i'` and `-p_{2,j}c_j'`; the velocities already use the weighted
metric, so no further node weight is inserted in them. Therefore

\[
 \mathcal L_N'=-\|w_N'\|_2^2-\|c_N'\|_2^2-\|M_N'\|_F^2,
 \quad\mathcal L_N(0)=1,
\]
\[
 \begin{gathered}
 \|c_N(t)\|_\infty\le2t,
 \quad\|M_N-D_N\|_F\le2t^2,
 \quad\|K_N\|_{\rm HS}\le2t^2,\\
 \|A_N\|_{\rm op}\le2+2t^2,
 \quad\|w_N(t)\|_2\le\sqrt2+4t^2+2t^4.
 \end{gathered}
 \tag{H40.C9}
\]

Indeed `int |r_N| dmu<=1`, `|a_N|<=1`, `|d_N|<=||c_N||2`, and
`||D_N||op<=2`; integrating the readout, matrix and row speed bounds
gives these inequalities. At fixed order, with
`K_l=(sum_i ||b_l,i||infty^2)^(1/2)`, one also has
`||w_N'||infty<=4t K_1||M_N||op`. Thus `w_N-g,c_N,M_N` stay in a bounded
existence ball on each finite interval, and their bounded speeds give
Cauchy endpoints there. Local continuation proves existence through 40
and indeed through every finite time at fixed order. The same proof,
starting with a saved current joint law and its energy/readout bounds,
gives unique own-state continuation. No extra history or Gaussian roots
are introduced at restart.

**Generated spaces and the omitted sources.** Let `H_l^obs` be the
initialized observable `L2` spaces from C.4.7.8.5. Their bounded words
have dense span; rational marks generate the same completed spaces, as
proved in C.4.7.9.2. Both `A_0` and `A_0^*` preserve the appropriate
spaces, and actual adjunction makes them a reducing pair. Every finite
supported raw Euler step from initialization keeps `w,c` in these
spaces and adds to `K` a sum of ranks between them. Bounded coordinate
operations preserve the generated sigma fields, and each action preserves
the spaces; induction proves this assertion. D.2's time-40 strong
completion then keeps the exact trajectory in these closed spaces and
`K(t)` in their closed HS block. Its strong derivative `K'(t)` is in
that block as well. This uses the time-40 completion, not part A's
short-time existence statement.

Part B's filter proof applies without a horizon restriction. On a vector
`S_Nv` from a fixed earlier raw span,
`||(I-Q_l,N)S_Nv||2^2<=eta_N|v|^2/4`. Zero-padding fixes `|v|` as
`N` increases; density and contraction extend this to strong convergence
`Q_l,N -> I` on `H_l^obs`. Hence both `B_N -> A_0` and
`B_N^* -> A_0^*` converge strongly, with common operator bounds. For a
compact `L2` set this convergence is uniform, by a finite net and the
operator bound on the point-to-net error.

The exact fields `H^1(t,u),Delta^2(t,u)` have compact `L2` images on
`[0,40] x S1`, by strong raw continuity, bounded readout, and the
bounded-multiplier lemma of C.4.7.4. The derivative `K'(t)` is a compact
HS curve. Consequently the following proof error tends to zero:

\[
 \begin{split}
 \epsilon_N={}&\sup_{t,u}\|(B_N-A_0)H^1(t,u)\|_2
       +\sup_{t,u}\|(B_N^*-A_0^*)\Delta^2(t,u)\|_2\\
       &+\sup_t\|Q_{2,N}K'(t)Q_{1,N}-K'(t)\|_{\rm HS}\longrightarrow0.
 \end{split}
 \tag{H40.C10}
\]

For the HS term, approximate each target by a finite sum of ranks.
Strong convergence handles both factors of each rank, contraction bounds
the discarded HS remainder, and a finite net of the compact derivative
curve gives uniformity. No term in (H40.C10) is supplied to the equations,
initializer or order-selection rule.

**Direct comparison through time 40.** On the common carrier define
`e_N=||w_N-w||2+||K_N-K||HS+||c_N-c||2`. Bounds (H40.C3),(H40.C9) and
the exact rank equation give one common raw/action ball, independent of
`N`. Forward subtraction gives, uniformly in `u`,

\[
 \begin{gathered}
 \|H_N^1-H^1\|_2\le e_N,\qquad
 Z_N^2-Z^2=A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A_0)H^1,\\
 \|Z_N^2-Z^2\|_2+\|H_N^2-H^2\|_2+|f_N-f|
                          \le C(e_N+\epsilon_N),\\
 \|\Delta_N^2-\Delta^2\|_2+\|Q_N-Q\|_2
                          \le C(e_N+\epsilon_N).
 \end{gathered}
 \tag{H40.C11}
\]

For the last line subtract
`(c_N-c)phi'(Z_N^2)+c[phi'(Z_N^2)-phi'(Z^2)]` and then
`A_N^*(Delta_N^2-Delta^2)+(K_N-K)^*Delta^2+(B_N^*-A_0^*)Delta^2`.
The reference readout is bounded, so these are `L2` estimates. The
remaining first gate uses a cutoff on the unchanged reference `Q`:

\[
 \|\phi'(w_N\cdot u)Q_N-\phi'(w\cdot u)Q\|_2
 \le C(e_N+\epsilon_N)+2R e_N+2\tau_R(Q(t,u)),\quad R\ge1.
 \tag{H40.C12}
\]

Below the cutoff use `Lip(phi')<=2`; above it use the bounded gates.
Only the exact reference needs tails. For the middle velocity, writing
`F_K` for the exact middle rank integral in (H40.C2), (H40.C8) gives

\[
 K_N'-K'=Q_{2,N}\{F_K(w_N,A_N,c_N)-F_K(w,A,c)\}Q_{1,N}
                    +(Q_{2,N}K'Q_{1,N}-K').
 \tag{H40.C13}
\]

Subtract its residual and rank factors, using
`||a tensor b-a' tensor b'||HS<=||a-a'||2||b||2+||a'||2||b-b'||2`.
The first term is at most `C(e_N+epsilon_N)` and the second is at most
`epsilon_N`. Subtracting the row and readout velocities with
(H40.C11)–(H40.C12), and using (H40.C4), therefore gives

\[
 D^+e_N\le C(1+R)(e_N+\epsilon_N)+CM_{\rm tail}e^{-a_{\rm tail}R^2},
 \qquad e_N(0)=0,
\]
\[
 \sup_{t\le40}e_N(t)
 \le CT e^{C(1+R)T}
       \{(1+R)\epsilon_N+M_{\rm tail}e^{-a_{\rm tail}R^2}\}.
 \tag{H40.C14}
\]

The error is absolutely continuous as a sum of norms of strong Hilbert
curves; the norm upper-derivative inequality also holds at zero. The
second line follows from the scalar exponential integrating factor.
First let `N -> infinity` at fixed cutoff, then let `R -> infinity`.
The negative quadratic exponent dominates `C(1+R)T` for the fixed
`T=40`, proving uniform raw convergence. No tail or higher-moment
assumption has been imposed on projected trajectories. Comparing any
competing strong raw path against the reference with zero initial error
uses the same tail-only bound and forces equality; reached continuation
uses its restriction. Thus the identification does not invoke uniqueness
of arbitrary formal hierarchy sequences.

**Observations.** Equation (H40.C11) proves convergence of predictions
uniformly on `[0,40] x S1` and of both current hidden fields uniformly
there in `L2`. The initial lower field is exact; the initial upper field
is `phi(B_N phi(g·u))` and converges uniformly in `u` by strong action
convergence on its compact target set. More generally the observation
induction of C.4.7.9.6 applies: seed errors tend to zero, the action norms
are uniformly bounded, both action directions converge on compact target
curves, and each bounded node has a common finite syntax envelope at its
fixed marks. Its action subtraction is
`A_NV_N-AV=A_N(V_N-V)+(K_N-K)V+(B_N-A_0)V`; bounded products use their
envelopes, and a bounded continuous gate times a named `L2` field uses
truncation of the fixed target field and compact-curve tail control.
These are exactly the hypotheses needed for every separately fixed
admitted same-layer tuple and its second moments.

In particular define, keeping the same initialized/current neuron and
input in each pair,

\[
 \mathcal P_{l,N}(t)=\operatorname{Law}_{\Omega_l\otimes\mu}
       (H_N^l(0,u),H_N^l(t,u)),\qquad
 R_{l,N}(t)=\|H_N^l(t,u)-H_N^l(0,u)\|_{L^2(\Omega_l\otimes\mu)}.
 \tag{H40.C15}
\]

Use the analogous definitions without `N` for the reference. The
common-carrier coupling bounds squared pair `W2` by the sum of the
two squared `L2` errors. The reverse triangle inequality bounds the RMS
error by the `L2` error of their paired differences. Thus both converge
uniformly in time. Since `|f_N|,|f|<=2T`,

\[
 \sup_{t\le40}|\mathcal L_N(t)-\mathcal L_\mu(t)|
 \le2(2T+1)\sup_{t,u}|f_N(t,u)-f_\mu(t,u)|\longrightarrow0.
 \tag{H40.C16}
\]

These target observations have the actual finite-network meaning already
established above. Full-row input continuity, bounded raw speeds and
finite time/input nets give the same uniform-time passages for bounded
hidden pairs and their training averages; no cross-layer neuron pairing
or cross-carrier operator-norm convergence is asserted. The risk and
early paired-activity bounds supplied by D.2 belong to this same target.
Convergence does not certify those bounds at a chosen finite order.

###### D.4. Finite numerical limits and whole-circle evaluation

Fix one represented law from D.1 with radius (H40.C1), rational endpoints
`-1<=a<=b<=1`, `-1<=c<=d<=1`, labels `+1,-1`, and component masses one
half. Its conditional coordinates are `u_1(rho s)` and `u_2(rho s)`,
where `u_2` is the quarter-turn of
`u_1(z)=((1-z^2)/(1+z^2),2z/(1+z^2))`. A degenerate interval is an
atom. Midpoints with `m` nodes per nondegenerate component give an exact
positive rational finite law `mu_m`; degenerate components use one node.
Its weights are `1/(2m)` or `1/2` and its normalized coordinates are
rational numbers with finite exact expressions. Both the target and
every exact midpoint rule are in `V_rho`, and D.1's transport estimate is

\[
 \mathcal W_1(\mu_m,\mu)
 \le\frac{\rho[(b-a)+(d-c)]}{4m}\le\frac\rho m.
 \tag{H40.N1}
\]

At order `N`, use part C's source regularization `epsilon>0`, initializer
cubature `Q`, independent population replay `P`, and rational arithmetic
precision `p`. Use the same Heun method with `J` steps of intended length
`h=40/J`. Between successive intended nodes interpolate the moving state
linearly and recompute the nonlinear fields. Denote the resulting
prediction by `fhat_{N,epsilon,Q,P,m,J,p}`. All adjustable resource
allowances are required to admit the requested finite operations; they
are not fixed caps on a refinement sequence.

The conclusion is

\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
 \lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}
 \lim_{p\to\infty}\mathfrak E=0,
 \tag{H40.N2}
\]

where `mathfrak E` is the sum of the prediction error in supremum norm
on `[0,40] x S1`, the two uniform-time paired `W2` errors, the two
uniform-time RMS errors, and the uniform-time risk error against the
reference of D.3. Each intermediate target exists in these metrics. Exact limiting
predictions are continuous; finite-precision rounded query evaluation
is required only to converge uniformly. The source-regularization limit is vacuous when the core initializer
does not use it. The law, radius, horizon, dictionary and ridge remain
fixed in their respective places in this iterated limit.

**Fixed-order mark and data limits.** The initialization proof in part C.2 is
unchanged: it concerns a fixed finite Gaussian graph before training,
whose bounded retained coordinates and formal derivatives have the
required polynomial Gaussian envelopes. At fixed positive `epsilon`,
every empirical source covariance prefix is its operand Gram plus
`epsilon I`; its positive pivots are retained. The Halton/Box–Muller
moment argument and finite coefficient induction give the `Q` limit.
Replay on `P` points evaluates the full joint mark tuple with all those
coefficients and factors frozen, so its joint laws, including lower
`g`, converge in `W2`. The two population indices are not paired.

After `Q -> infinity`, removal of `epsilon` uses continuity of positive
semidefinite covariance square roots and the same Gaussian envelopes for
the complete named source list. Singular limiting covariance is allowed;
no continuity of singular Cholesky factors or deletion of a zero-variance
named derivative is required. At fixed `N`, the feature ridge stays
positive. For every raw retained coordinate bound `B_l,j`,

\[
 |b_l|\le K_l:=\left(\sum_jB_{l,j}^2\right)^{1/2}/\sqrt{\eta_N}.
 \tag{H40.N3}
\]

This holds for empirical and exact Grams. Normalization and `D_N` are
continuous along the successive initializer limits, with common finite
matrix bounds. An independent replay need not reproduce the Gram used
for normalization or make its feature map a contraction. Only the
bounded-envelope estimate (H40.N3) is needed for the following inner
stability argument; the outer contraction argument uses the exact
initializer after all inner limits.

For general probability mark laws satisfying (H40.N3), `E|g|^2<infinity`
and finite `D`, the local characteristic construction of part C.3 applies to
exactly (H40.C6). Its weighted gradient calculation gives

\[
 \|c(t)\|_\infty\le2t,\quad |a|\le K_1,\quad |d|\le2K_2t,
 \quad\|M-D\|_F\le2K_1K_2t^2,
 \quad\|w'(t)\|_\infty\le4K_1K_2t\|M(t)\|_F.
 \tag{H40.N4}
\]

These bounds close existence in bounded `w-g,c,M` through 40 for each
fixed order, including atomic replay laws, without empirical contraction.
Couple two complete lower joint mark laws and two upper mark laws, and
write
`e=||w-wtilde||2+||c-ctilde||2+||M-Mtilde||F` and
`rho_b=||b_1-btilde_1||2+||b_2-btilde_2||2` on those couplings.
At a common input,
`|a-atilde|<=||b_1-btilde_1||2+K_1||w-wtilde||2`.
Subtract the three factors of `b_2^TMa`, then of `c h_2`, `b_2c phi'`
and `b_1^TM^Td`. Bounds (H40.N3)–(H40.N4) give `C(e+rho_b)` for all
field differences in their `L2` or finite Euclidean norms. In the lower
gate product the comparison query is pointwise bounded by
`K_1 K_2||Mtilde||F||ctilde||infty`, so it has the same bound.

For a data-law change the velocity integrand is Lipschitz into the
corresponding `L2`/Frobenius space. Indeed
`||phi(w·u)-phi(w·v)||2<=||w||2|u-v|`; its `a` integral inherits this
bound, upper fields and `q` inherit it through bounded finite features,
and the last lower gate costs
`2||w||2||q||infty|u-v|`. The explicit terminal `u` and label `y`
are Lipschitz as well. Integrating a data coupling with the Bochner
triangle inequality therefore costs `C W1(mu,mutilde)`, not its square
root. The scalar integrating factor yields

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 e(0)+CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)\}\right],
 \quad e(0)=\|g-\widetilde g\|_2+\|D-\widetilde D\|_F.
 \tag{H40.N5}
\]

The constant uses only common `K_l,||D||F,||g||2,T` bounds. Such bounds
hold along every fixed-order initializer/mark limit. At a reached restart,
replace `e(0)` by the discrepancy of the complete saved moving state.

Working weights need not sum exactly to one. For an exact ODE using
nonnegative finite measures write its two population measures as
`s_l lambda_l` and data measure as `s_d mu`, with normalized laws and
masses in `[1/2,2]`. The operational expressions contain the factors
`s_1` in `a`, `s_2` in `f,d`, and `s_d` outside each velocity; these
factors are retained. Its weighted energy identity gives
`L(0)<=s_d`, `int |r| d(s_d mu)<=s_d`, hence bounds of the form
(H40.N4) with enlarged constants. Product subtraction adds the mass
error `Delta_s=|s_1-stilde_1|+|s_2-stilde_2|+|s_d-stilde_d|`:

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 e(0)+CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)+\Delta_s\}\right].
 \tag{H40.N6}
\]

All `L2` distances here use the normalized coupling spaces. These
estimates also hold for input laws on the fixed neighborhood `|u|<=2`,
with enlarged constants, by replacing each unit input bound by two.
This covers directly rounded coordinates before the precision limit.
This is an estimate for exact ODEs with their literal finite measures,
not an energy or stability identity for a rounded Heun computation. In (H40.N2),
precision is removed first, so the normalized estimate (H40.N5) suffices
for the later ODE limits; (H40.N6) also accounts explicitly for mass
errors when comparing the finite measures before that limit.

For paired observations take the product of each same-layer joint mark
coupling and a data coupling, retaining initial and current values
together. The initial upper field uses the same `g,b_1,b_2,D` and lower
weights as the current calculation. The same-input `L2` field estimates
hold uniformly in time; initial errors add the corresponding `g,D,mark`
errors. Since the circle has diameter two,
`int |u-v|^2 dpi<=2 int |u-v| dpi`. Therefore

\[
 \sup_{t\le T}\mathcal W_2(\mathcal P_l(t),\widetilde{\mathcal P}_l(t))
 \le C\left[
 \sup_te(t)+\rho_b+e(0)+\Delta_s
                         +\mathcal W_1(\mu,\widetilde\mu)^{1/2}\right].
 \tag{H40.N7}
\]

Here pair laws use normalized product measures. On the rounded-input
neighborhood use `|u-v|^2<=4|u-v|`; only the constant changes. This
square-root term comes from squared transport cost; it does not weaken
the linear data term in the drift estimate. The reverse `L2` triangle inequality gives
the same convergence for RMS. With literal finite-measure weights,
`R_l,raw^2=s_l s_d R_l,normalized^2`. As the masses approach one these
have the same limit, including at zero displacement. The raw risk is
`s_d int(f-y)^2 dmu`; its difference is bounded by prediction error,
`C W1` for the fixed-state loss integrand and `C|s_d-stilde_d|`.
This proves the asserted paired/RMS/risk passages under each refinement.

**Time and arithmetic, including a compact query domain.** Fix
`N,epsilon,Q,P,m` and first use exact arithmetic. The finite ODE is
smooth. Its Heun stages remain bounded independently of `J`: with
`B_k=1+||c_k||infty`,

\[
 B_k^*\le(1+2h)B_k,\qquad
 B_{k+1}\le(1+2h+2h^2)B_k\le e^{(2+2T)h}B_k.
 \tag{H40.N8}
\]

Thus all stages have `1+||c||infty<=B_*=(1+2T)e^{(2+2T)T}`. Their
matrix velocity is at most `V_M=2B_*K_1K_2(B_*-1)`, and matrix
nodes/stages have norm at most `||D||F+2TV_M`; their row increments
are bounded by integrating
`2B_*K_1K_2(||D||F+2TV_M)(B_*-1)`. These finite bounds are valid at
`T=40` without a discrete energy inequality. On a slightly larger
bounded set the vector field is Lipschitz. The exact step and Heun step
each differ from Euler by `O(h^2)` there; the recurrence
`e_(k+1)<=(1+Ch)e_k+Ch^2` sums to `max e_k<=C_T h`.
Linear interpolation adds `O(h)`, proving the uniform-time mesh limit.

Now fix `J` also and let rational arithmetic precision `p` increase.
The finite initializer, fixed-pivot Cholesky operations and finite Heun
nodes converge by part C.4's locally consistent primitive algorithms and
finite-operation induction. Their exact positive source and feature
pivots supply eventual success margins at these fixed parameters. No
claim of a diagonal with unresolved shrinking pivots is made.

The data radius requires a further check. Its exponent `E=E_10` is a
fixed finite integer with an exact expression. The law rule may replace
the radius by zero when `E>4(p+8)+2`; then its coordinate displacement
is at most `2rho<10^(-p-8)`, and the bound and exact positive law are
retained. As `p->infinity` at fixed `E`, that branch eventually stops.
With adequate adjustable expression/scalar-bit and rule-node allowances,
the exact denominator `2^E` and each fixed midpoint coordinate can then
be formed. Their rational endpoints and positive weights are unchanged.
Direct coordinate and weight rounding tends to zero. More explicitly,
let `e_coord` be the largest coordinate `L1` rounding error and `e_weight`
the total absolute weight error. For total mass at least one half,
normalizing changes the weights from the exact rule by total variation
at most `2e_weight`. First couple masses on the exact rule nodes and
move the remainder over their data diameter at most four; then move each node to its rounded
coordinate. Thus the resulting transport error is
at most `e_coord+8e_weight`. Keep the separate mass defect in
(H40.N6) for the operational equations. A nonreference
exact midpoint may also round to an axis at some precisions; for a
fixed nonzero coordinate this likewise eventually stops. Exact axis
midpoints or a coarse midpoint rule that is itself the reference remain
valid quadrature cases. Neither type of numerical collapse redefines
the positive-radius target law.

At fixed array sizes, nearest `10^-p` weight rounding has total error
at most one half the number of weights times `10^-p`; all relevant
masses are eventually positive and tend to one. Normalizing returned
nonnegative weights only to interpret pair laws therefore changes them
by vanishing total variation. RMS and risk use the original weights;
their arithmetic outputs converge and the preceding mass calculation
identifies their limits. Rounded input coordinates lie in a common
compact neighborhood of the circle. Their squared-norm perturbation is
at most `4·10^-p`, inside the precision-dependent validation allowance;
repeated validation does not normalize the data or change its law.

Finiteness of the training program alone does not prove uniform
whole-circle arithmetic convergence. At fixed outer parameters and `J`,
take all finitely many adjacent exact endpoint pairs. For each pair the
exact interpolation/evaluation graph is a continuous function of
`(u,q) in S1 x [0,1]`, with `q` its interpolation fraction. Every
intermediate operand has compact image: start from these compact query
sets and sufficiently small closed bounded endpoint neighborhoods,
which are compact in these finite dimensions, and induct through the
finitely many continuous operations. Include the initial-field evaluation with
`g,D` in the same collection. All primitive domains requiring a
nonzero denominator retain a positive margin; tanh's implemented
denominator is at least one, and square-root consistency also holds at
zero. Part C.4's primitive error estimates are locally uniform on these
compact operand sets. Uniform continuity and induction through this
finite evaluation graph therefore give uniform convergence in `(u,q)`
and over the finitely many steps, even though the query domain is
uncountable.

Use directly rounded coordinates for each queried `u`; their Euclidean
error is at most `sqrt(2)10^-p/2`. Round `q` with error at most
`10^-p/2`. These arguments stay in the preceding compact neighborhoods,
so the same induction includes query rounding and interpolation.
The intended step `40/J` and its represented value differ by at most
`10^-p/2`, and the final represented time differs by at most
`J10^-p/2`. This error vanishes in the precision-first limit.
Equivalently define the output on the intended mesh by its interpolated
states; both conventions have that same limit. A finite output panel
is not used to infer a circle supremum.

After arithmetic and mesh limits, (H40.N1),(H40.N5) remove input
quadrature, followed by the `P`, `Q` and source-regularization limits
whose hypotheses were verified above. Their forward and paired bounds
give the observation convergence at every stage. The resulting exact
order is exactly (H40.C5)–(H40.C6); D.3 proves its outer `N` limit and
identifies the result with actual finite-network GF, retaining its
random finite initial readout. This proves (H40.N2).

At a numerical step endpoint the saved complete joint marks, weights,
`g,w,c,M,D`, finite law and arithmetic/step metadata determine every
following Heun step. Exact serialization therefore gives own-state
restart with no source tape or training history. The limiting population
restart follows from the characteristic uniqueness and (H40.N5) with
saved-state error in `e(0)`. A new Heun mesh from an interpolated interior
time need not reproduce the old finite mesh. These conclusions provide
qualitative iterated convergence on the fixed explicit family and horizon;
they assert no arbitrary diagonal, tolerance-to-resolution procedure,
useful conditioning, finite-run accuracy certificate, or simultaneous
closure-order/width rate.
