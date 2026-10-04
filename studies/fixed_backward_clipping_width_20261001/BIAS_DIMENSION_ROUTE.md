# Width doubling by Gaussian block interpolation

2026-10-01. Scoped fresh route. Status: **partial, with an explicit unresolved cancellation estimate**. No experiment, paper edit, Git operation, other study, or new sibling route was used. The full initial inputs were `FITTING_AND_THRESHOLD.md`, `CONCENTRATION_ROUTE.md`, and `CLIPPED_POPULATION_ROUTE.md` in this study. The solve-math-rigorously and investigate-conjectures skills, including the contract, adversarial-audit, and proof-search references, were used. This is an internal derivation, not an independent promotion review.

The result of this route is a genuine cross-width construction and a proved root-width comparison at one endpoint: joining two independent width-n systems into a single block-diagonal width-2n system costs O(n^(-1/2)) in expected all-time prediction error. The Gaussian interpolation from the block matrix to the fully connected matrix preserves its true transpose and has an exact weak-derivative formula even with hard clipping. Its signed trace is not bounded at the needed scale here. Small fixed label activity gives a useful perturbative check but does not close that missing estimate.

## 1. Contract and notation

The system is exactly the assigned q=1 tanh closure. Write u_a=x_a/sqrt(d), psi=sech², and C_M for hard clipping to [-M,M], with M>0 fixed. At width n,

\[
 h_a=\tanh(Au_a),\quad
 B=W_0+\frac1{mn}\sum_a v_a k_a^T,\quad
 z_a=Bh_a,\quad g_a=\tanh z_a,\quad f_a=w^Tg_a/n,
\]
\[
 d_a=C_M(w\odot\psi(z_a)),\qquad
 \ell_a=C_M(\psi(Au_a)\odot B^Td_a),
\]
\[
 \dot w=-\frac2m\sum_a r_ag_a,\quad
 \dot A=-\frac2m\sum_a r_a\ell_a u_a^T,\quad
 \dot v_a=-2r_ad_a,\quad
 \dot k_a=\frac\rho\tau(h_a-k_a),\quad
 \dot\tau=\rho.
 \tag{1}
\]

Here r=f-y, rho=||r||_m, A_0 has independent standard Gaussian entries, W_0 has independent N(0,1/n) entries and is independent of A_0, w(0)=v_a(0)=0, k_a(0)=h_a(0), and tau(0)=1. There is no learned dense matrix and no Gaussian resampling. Both directions of every matrix action use this same W_0 and its true transpose.

Let G_n be the good initialization event from the concentration input: bounded operator norm and initial readout Gram at least lambda I. The label norm Y is fixed and sufficiently small for the fitting and stability results in that input. Constants below may depend on M, data, lambda and the chosen good-event operator bound, but not on n or physical time. For a fixed query x, constants may also depend on x. Put

\[
 m_n(t,x)=\mathbb E[f_n(t,x)\mid G_n].
\]

The primary bias target is

\[
 \sup_{t\ge0}|m_n(t,x)-f_M(t,x)|\le C_x n^{-1/2}.
 \tag{2}
\]

The same arguments below can be integrated over bounded query sets or a test law with the moment bound required by the velocity constants. They do not improve the concentration input's fourth-moment issue to a merely second-moment hypothesis.

The qualitative limit in the population input and the bounded good-event prediction imply m_n -> f_M in this all-time norm. Indeed, good-event predictions are uniformly bounded and converge in probability in the stated norm; splitting the expectation at any positive tolerance proves convergence of their expectations. A sufficient quantitative bridge is therefore

\[
 \|m_{2n}-m_n\|_{\infty,t}\le C_x n^{-1/2}.
 \tag{3}
\]

Summing (3) at n,2n,4n,... and passing to the qualitative limit gives (2), with constant multiplied by (1-2^(-1/2))^(-1). This telescoping implication uses the known population limit; it does not define a new population target by choosing finite-width centers.

## 2. A scalar concentration consequence used in the joining proof

For a fixed time, any bounded scalar observable O_n that is L/sqrt(n)-Lipschitz in the standard Gaussian roots on G_n satisfies

\[
 \operatorname{Var}(O_n\mid G_n)\le\frac{2L^2}{n}
 \tag{4}
\]

for all sufficiently large n. To verify (4), take a bounded Lipschitz extension O_ext with the same constant, apply the supplied Gaussian Poincare inequality, and use

\[
 \operatorname{Var}(O_n\mid G_n)
 \le\mathbb E[(O_{\rm ext}-\mathbb EO_{\rm ext})^2\mid G_n]
 \le\frac{\operatorname{Var}(O_{\rm ext})}{\Pr(G_n)}.
\]

Since Pr(G_n)>=1-C/n>=1/2, (4) follows. Consequently, for two independent copies conditioned on their respective good events,

\[
 \mathbb E|O_n^1-O_n^2|\le 2L/\sqrt n.
 \tag{5}
\]

The deterministic all-time stability in the concentration input gives the required uniform L for all normalized scalar pairings of the bounded feature and state fields used below. For example,

\[
 q_{ab}=\frac1n k_a^Th_b,\quad
 s_{ab}=\frac1n v_a^Td_b,\quad
 u_{ab}=\frac1n v_a^Tp_b,\qquad
 p_b=w\odot\psi(z_b).
 \tag{6}
\]

The factors have bounded normalized L² norms, their differences are controlled by the initialized-state distance, and the hard-clipped fields are Lipschitz by

\[
 |C_M(p\psi(z))-C_M(\widetilde p\psi(\widetilde z))|
 \le |p-\widetilde p|+2M|z-\widetilde z|.
 \tag{7}
\]

The clock tau is another such observable. The fields psi(Au_b) odot ell_a are also bounded and Lipschitz, since ell_a is coordinatewise bounded by M. This verifies rather than assumes the product estimates needed for the residual kernels.

There is a stronger decaying estimate for the residual. The pairwise stability bound in the concentration input gives a root-coordinate Lipschitz constant at most C(1+t)e^(-ct)/sqrt(n). Applying (4) componentwise yields

\[
 \mathbb E\|r^1(t)-r^2(t)\|_m
 \le C(1+t)e^{-ct}/\sqrt n.
 \tag{8}
\]

Pointwise-in-time concentration is sufficient below because all persistent coefficient errors are integrated against finite residual activity. No supremum-over-time concentration of every internal pairing is being asserted.

## 3. The block endpoint is not an independent pair of networks

Let U,V be independent n-by-n Gaussian matrices with entries N(0,1/n), and let the two halves of A_0 be independent first-layer initializations. At width N=2n initialize

\[
 W_{\rm blk}=\begin{pmatrix}U&0\\0&V\end{pmatrix}.
 \tag{9}
\]

Run exactly (1), with width normalization N, on this matrix. Denote its prediction by f_blk. This is the **joined** system. Its residual, clock, and low-rank contractions are global. It is not two independent width-n flows.

On the same roots, run two actual width-n flows separately, denoted by superscripts 1 and 2. For example, the independent forward action in block i is

\[
 B_i h_b^i=W_i h_b^i+\frac1m\sum_a v_a^i q_{ab}^i.
\]

If their state vectors are concatenated but the width-N reconstruction is used, the action on block i instead is

\[
 W_i h_b^i+\frac1m\sum_a v_a^i
           \frac{q_{ab}^1+q_{ab}^2}{2}.
 \tag{10}
\]

Thus the discrepancy is exactly

\[
 \frac1{2m}\sum_a v_a^i(q_{ab}^{3-i}-q_{ab}^{i}).
 \tag{11}
\]

For a transpose call, the corresponding discrepancy is a sum of k_a^i times differences of the normalized pairings v_a^T d_b/n, together with the difference in d_b caused by (11). These are genuine low-rank contraction errors. The initialized U,V and their transposes are unchanged.

On G_n^1 cap G_n^2 the block initialized operator has the same operator bound, and its initial Gram is the average of the two local Grams, hence is at least lambda I. The joined flow therefore satisfies the same deterministic fitting theorem. In particular, all three residual norms are bounded by a common deterministic multiple of Y exp(-kappa t).

## 4. Proved joining bound

For a fixed finite collection of training and passive query inputs, the following is a consequence of the supplied stability estimates and (4):

\[
 \mathbb E\!\left[
  \sup_{t\ge0}\left|f_{\rm blk}(t,x)
       -\frac{f_n^1(t,x)+f_n^2(t,x)}2\right|
  \,\middle|\,G_n^1\cap G_n^2\right]
 \le C_x/\sqrt n.
 \tag{12}
\]

Here are details including the residual comparison, which is necessary to avoid a spurious nonintegrable forcing term.

Use normalized N-dimensional norms for concatenated state vectors, and compare the joined state to the concatenation of the independent states, with reference clock (tau^1+tau^2)/2. Let D be the sum of these state distances and this clock distance. Let

\[
 \bar r=(r^1+r^2)/2,\quad
 R=\|r_{\rm blk}-\bar r\|_m,\quad
 \delta r=\|r^1-r^2\|_m.
\]

For a given finite query list let Xi(t) be the sum of the differences between the two independent copies of tau and of all normalized pairings, within the same layer, of the following finite lists:

\[
 \begin{array}{ll}
 \text{first layer:}&
 h_b,\ k_a,\ \psi(Au_b)\odot\ell_a,\\
 \text{second layer:}&
 g_b,\ w,\ v_a,\ d_a,\ p_b.
 \end{array}
 \tag{13}
\]

Here a runs over training inputs, b runs over training inputs and the fixed queries, and d_a, ell_a are training fields. Every member has a bounded normalized norm and an initialized-state Lipschitz bound. There are finitely many pairings, independently of n. Hence

\[
 \mathbb E[\Xi(t)\mid G_n^1\cap G_n^2]\le C_x/\sqrt n
 \quad\text{for every }t.
 \tag{14}
\]

Take a deterministic envelope b(t)=C Y exp(-kappa t) for the sum of the three residual norms. Reconstruction, (10)-(11), and (7) imply the following estimates in upper derivatives:

\[
 D'\le C bD+CR+C b\Xi+C\delta r,
 \tag{15}
\]
\[
 R'\le-\kappa_1R+C b(D+\Xi)+C\delta r,
 \qquad D(0)=R(0)=0.
 \tag{16}
\]

To check (15), write each difference of a residual-times-field as a coefficient difference times the joined residual plus a residual difference times an independent field. The coefficient difference is at most C(D+Xi) by (10)-(11), the bounded operator action and (7). For a local residual r^i, its difference from the joined residual is bounded by R+delta r. For the keys, the reference clocks differ from their average by at most |tau^1-tau^2|/2, already in Xi. For the clock equation itself,

\[
 \left|\rho_{\rm blk}-\frac{\rho^1+\rho^2}{2}\right|
 \le R+\delta r,
\]

by the Lipschitz property of the finite-dimensional norm and the triangle inequality. This proves all state blocks in (15).

For (16), use the exact residual identity from the concentration input,

\[
 \dot r_b=-\frac2m\sum_a r_a
      (K^0_{ba}+K^A_{ba}+K^v_{ba})+\rho Q_b.
 \tag{17}
\]

Each joined coefficient differs from the average of its independent coefficients by at most C(D+Xi). One can verify this directly for K^0 and K^v by pairing subtraction. For K^A, the initialized operator is block diagonal; its low-rank correction contributes the pairings of k_a with psi(Au_b) odot ell_c in (13). Alternatively move B to the other side and use the pairings v_a^T p_b/n. Both calculations retain the true transpose. The terms in Q are products of pairings from (13) and a factor 1/tau. The difference between the average of two products and the product of their averages is bounded by C Xi, since all factors are bounded. Therefore no unlisted random action is being treated as independent.

Average the two local identities (17). Replacing r^i by bar r and rho^i by ||bar r|| costs at most C delta r. Subtract this identity from the joined one. The joined readout Gram supplies the coercive term, while its other residual kernels are O(Y²) and its Q term is O(Y³), exactly as in the supplied stability proof. The same sufficiently small fixed Y absorbs those terms into a positive kappa_1. The coefficient differences multiply decaying reference residuals and give Cb(D+Xi). This is (16).

It would be incorrect instead to evaluate the concatenated independent state using the joined forward map, call its resulting residual the reference residual, and bound its difference from zero by C Xi for all time. Such a bound need not decay, and integrating it would lose the conclusion. Equations (15)-(17) use the independently defined bar r and its exact derivative.

Integrating (16) and inserting it into (15), then using the integrating-factor Gronwall proof with integrable b, gives

\[
 \sup_{t\ge0}D(t)+\int_0^\infty R(t)\,dt
 \le C\left(\int_0^\infty b(t)\Xi(t)\,dt
             +\int_0^\infty\delta r(t)\,dt\right).
 \tag{18}
\]

Tonelli's theorem, (8), and (14) make the expectation of the right-hand side at most C_x/sqrt(n).

For a passive query, apply the exact query-velocity identity corresponding to (17). The same subtraction, with its query-dependent constants, gives

\[
 \left|\dot f_{\rm blk}(t,x)
       -\frac{\dot f_n^1(t,x)+\dot f_n^2(t,x)}2\right|
 \le C_x\{bD+R+b\Xi+\delta r\}.
 \tag{19}
\]

All predictions start at zero. Integrating (19), then applying (18), (8), and (14), proves (12). It also avoids needing a temporal supremum bound on Xi itself.

In particular, the conditional mean of the joined block system differs from m_n by at most C_x/sqrt(n), uniformly in time. This is a cross-width result, but the initialized width-N matrix at this endpoint is block diagonal, so (12) alone is not the requested width-n versus width-2n estimate.

## 5. Exact Gaussian interpolation to the actual width-2n law

Let P,Q be two additional independent n-by-n Gaussian matrices with entry variance 1/n, independent of U,V and the first-layer roots. Set

\[
 W_\theta=
 \sqrt{\frac{1+\theta}{2}}
    \begin{pmatrix}U&0\\0&V\end{pmatrix}
 +\sqrt{\frac{1-\theta}{2}}
    \begin{pmatrix}0&P\\Q&0\end{pmatrix},
 \qquad 0\le\theta\le1.
 \tag{20}
\]

At theta=0 all N² entries are independent N(0,1/N), so the law is the actual width-N initialization. At theta=1 this is (9). At every intermediate value it remains a single fixed Gaussian matrix used in both orientations throughout training.

Let s_i and t_j equal +1 on the first n row and column indices and -1 on the other n. Then the entry variance is

\[
 v_{ij}(\theta)=\frac{1+\theta s_it_j}{2n}.
 \tag{21}
\]

To avoid boundary terms from good-event conditioning, use the bounded velocity extension in the concentration input at dimension N. Denote it by

\[
 a_N^{\rm ext}(t,x,A_0,W).
\]

It is one fixed function of A_0,W, independent of theta. It agrees with the true prediction velocity on the width-N good set, has an integrable absolute envelope B_x(t), and is L_x(t)-Lipschitz in the **raw matrix** W for the Frobenius metric, with

\[
 \int_0^\infty(B_x(t)+L_x(t))\,dt<\infty.
 \tag{22}
\]

The factor N^(-1/2) in standard Gaussian root coordinates disappears when the coordinates are W=G/sqrt(N), explaining this raw-matrix scaling. A McShane infimum using the invariant distance ||A-A'||_F/sqrt(N)+||W-W'||_op, followed by the supplied clipping to the velocity envelope, preserves the invariance under independent permutations of the two hidden layers. The good set and the original prediction velocity have that invariance.

Define

\[
 c_\theta(t,x)=\int_0^t
       \mathbb E[a_N^{\rm ext}(u,x,A_0,W_\theta)]\,du.
 \tag{23}
\]

At theta=0, c_0 differs from m_N by O_x(1/n), uniformly in time. At theta=1, c_1 differs by O_x(1/n) from the joined prediction mean conditioned on G_n^1 cap G_n^2. These statements follow from the uniform integral envelope and the endpoint bad-event probabilities O(1/n); no good-event conditioning is differentiated. Together with (12), the full width-doubling conclusion would follow from

\[
 \|c_1-c_0\|_{\infty,t}\le C_x/\sqrt n.
 \tag{24}
\]

## 6. Hard clipping does not prevent an exact weak interpolation identity

Fix t,x and abbreviate a=a_N^ext(t,x,A_0,W). Conditional on A_0, a is a bounded Lipschitz function of W. For 0<theta<1, differentiating the Gaussian density gives

\[
 \frac d{d\theta}\mathbb E a(W_\theta)
 =\frac1{4n}\sum_{ij}s_it_j
   \mathbb E\left[
     \left(\frac{W_{ij}^2}{v_{ij}^2}-\frac1{v_{ij}}\right)a(W_\theta)
             \right].
 \tag{25}
\]

Density differentiation is justified on every compact subinterval of (0,1), because a is bounded and the derivative of the Gaussian density is an integrable polynomial times that density. Integrating by parts once against the weak first derivative of a gives the equivalent identity

\[
 \frac d{d\theta}\mathbb E a(W_\theta)
 =\frac1{4n}\sum_{ij}s_it_j
   \mathbb E\left[\frac{W_{ij}}{v_{ij}}
                         \partial_{W_{ij}}a(W_\theta)\right].
 \tag{26}
\]

To verify the weak integration by parts without assuming pointwise derivatives at clipping corners, convolve a in finite-dimensional matrix space with a smooth approximate identity. The convolutions have the same Lipschitz constant and converge uniformly to a. Their weak gradients converge locally in L¹, remain bounded by the Lipschitz constant, and thus converge under the Gaussian weight after truncating its tails. The smooth identities pass to the limit. This also proves the identity after averaging over A_0.

For a smooth function, (25)-(26) equal

\[
 \frac1{4n}\mathbb E\sum_{ij}s_it_j
                           \partial_{W_{ij}}^2 a(W_\theta).
 \tag{27}
\]

For the actual extension, (27) is only notation for the Gaussian average of its distributional second derivative, explicitly defined by (25) or (26). It is not a claim that the clipped flow has classical second derivatives. In particular this derivation does not differentiate the threshold indicator in the clip's derivative or discard threshold surface terms.

The weak identity is integrable up to theta=1. Indeed, the gradient norm is at most L_x(t), and

\[
 \sum_{ij}v_{ij}^{-1}
 =\frac{8n^3}{1-\theta^2}.
\]

Cauchy--Schwarz in (26) yields

\[
 \left|\frac d{d\theta}\mathbb E a(W_\theta)\right|
 \le\frac{L_x(t)\sqrt{n/2}}{\sqrt{1-\theta^2}}.
 \tag{28}
\]

Since the right side is theta-integrable, while W_theta -> W_1 in L² and a is Lipschitz, one may integrate (26) on [0,1]. Thus nonsmooth clipping is not an obstruction to the exact interpolation construction. The bound (28), however, is O(sqrt(n)), two powers of sqrt(n) too large for the desired O(n^(-1/2)) bound. A boundedness estimate is better than (28) numerically but still supplies no decaying power of n.

## 7. The exact missing cancellation

The variance profile and the law of A_0 are invariant under permutations within each row block and column block and under simultaneous exchange of both blocks. Therefore there are only two expected diagonal Hessian entries in (27), interpreted weakly:

\[
 h_+(t,x,\theta)=\mathbb E\partial_{W_{ij}}^2 a
      \quad(s_it_j=+1),\qquad
 h_-(t,x,\theta)=\mathbb E\partial_{W_{ij}}^2 a
      \quad(s_it_j=-1).
\]

Each class has 2n² entries, and hence

\[
 \frac d{d\theta}\mathbb E a(W_\theta)
       =\frac n2\,[h_+(t,x,\theta)-h_-(t,x,\theta)].
 \tag{29}
\]

At theta=0 the full independent row and column permutation symmetry gives h_+=h_- exactly. The first interpolation derivative at the fully connected endpoint is therefore zero. The interior law does not have that full symmetry: within-block and cross-block entries have different variances. The equality at one endpoint gives no bound on their difference in the interior.

A sufficient, concrete signed-trace estimate is

\[
 \int_0^\infty\int_0^1
   |h_+(t,x,\theta)-h_-(t,x,\theta)|\,d\theta\,dt
 \le C_x n^{-3/2}.
 \tag{30}
\]

Equations (23), (29), and (30) imply (24), which combined with (12) and telescoping proves the fixed-query root-width bias. Equation (30) is sufficient rather than necessary: a proof retaining cancellation in the theta or time integral could use a weaker condition. No assertion of (30) is made here.

Even an entrywise Hessian estimate O(1/n), if it were established, would only give O(1) after taking the absolute sum in (27). One needs an extra cancellation between the two variance classes. A generic initialization Lipschitz estimate and Gaussian Poincare control a gradient's Euclidean norm and the centered variance; they do not supply this class difference. Randomizing the balanced block labels does not make the signs independent of the trajectory: the variance profile in (21) couples them to precisely the matrix entries that generate that trajectory.

## 8. Small fixed labels: a proved leading estimate and the nonclosed step

The coordinator requested a check whether small activity turns the interior trace into a contraction. There is a useful rigorous starting point.

Freeze A and B at initialization and train only the readout. With initial training Gram Gamma_0, the frozen training prediction is

\[
 f_{\rm fr}(t)=y-e^{-2\Gamma_0t}y.
 \tag{31}
\]

For a passive query, put gamma_{0,x,a}=g_x(0)^Tg_a(0)/(mn). Then

\[
 f_{\rm fr}(t,x)=
 \gamma_{0,x}^{T}\Gamma_0^{-1}
                  (I-e^{-2\Gamma_0t})y.
 \tag{32}
\]

These formulas are only an analytical comparison; the model in (1) is not replaced by frozen features.

The mean bias of (31)-(32) is O(Y/n), uniformly in time on the good event, and the constant in this frozen estimate can be chosen uniformly over the passive query x. Here is a complete quantitative derivation.

Augment the training list by this query and write ell=m+1. Let H_i be the ell-vector of initial first-layer tanh features. Its coordinates have magnitude at most one, and the H_i are independent and identically distributed. With

\[
 Q_n=\frac1n\sum_i H_iH_i^T,\qquad Q=\mathbb E H_iH_i^T,
\]

independence gives E(Q_n-Q)=0 and E||Q_n-Q||_F²<=ell²/n. These bounds are uniform in x. For T_ab(R)=E[tanh(Z_a)tanh(Z_b)] with Z centered Gaussian of covariance R, differentiation along a positive-semidefinite covariance segment R_s=R+sD gives

\[
 \frac d{ds}T_{ab}(R_s)
 =\frac12\sum_{ij}D_{ij}\mathbb E\partial_{ij}F_{ab}(Z_s),
\]
\[
 \frac {d^2}{ds^2}T_{ab}(R_s)
 =\frac14\sum_{ij,kl}D_{ij}D_{kl}
                       \mathbb E\partial_{ijkl}F_{ab}(Z_s),
 \qquad F_{ab}(z)=\tanh z_a\tanh z_b.
\]

For positive definite covariance these formulas follow by differentiating the Gaussian density and integrating by parts. All coordinate derivatives of F_ab of orders at most four are bounded. Adding epsilon I to the whole segment and then using bounded convergence extends the integrated first-order formula and its second-order Taylor remainder to singular covariances as well. In particular the linear first variation at R exists on admissible segments, has bounded coefficients, and the absolute Taylor remainder is at most C_ell||D||_F². Thus

\[
 \|\mathbb E T(Q_n)-T(Q)\|_F\le C_\ell/n,
 \qquad
 \mathbb E\|T(Q_n)-T(Q)\|_F^2\le C_\ell/n.
\]

Conditional on the first layer, the initial second-layer tanh rows are independent, bounded, and have covariance T(Q_n). Their empirical covariance R_n therefore satisfies

\[
 \|\mathbb E R_n-T(Q)\|_F\le C_\ell/n,
 \qquad
 \mathbb E\|R_n-T(Q)\|_F^2\le C_\ell/n.
\]

The training block of R_n/m is Gamma_0 and its query/training block is gamma_{0,x}. Write Delta for the pair of their errors from the corresponding deterministic blocks (Gamma_*,gamma_*). Since every entry is bounded, Pr(G_n^c)<=C/n implies

\[
 \|\mathbb E[\Delta\mid G_n]\|\le C/n,
 \qquad \mathbb E[\|\Delta\|^2\mid G_n]\le C/n.
\]

For example the first estimate follows by writing E[Delta|G_n]=(E Delta-E[Delta 1_{G_n^c}])/Pr(G_n); the second follows by division by Pr(G_n)>=1/2. No independence from the good event is assumed.

To bound the prediction functional, use the integral form

\[
 F_t(\Gamma)=2\int_0^t e^{-2\Gamma s}\,ds,
 \qquad f_{\rm fr}(t,x)=\gamma_{0,x}^TF_t(\Gamma_0)y.
\]

On Gamma>=lambda I, Duhamel's formula gives

\[
 \|D e^{-2\Gamma s}[H]\|\le2s e^{-2\lambda s}\|H\|,
 \qquad
 \|D^2 e^{-2\Gamma s}[H,K]\|
       \le4s^2e^{-2\lambda s}\|H\|\|K\|.
\]

The second bound is the sum of the two time-ordered double integrals; their simplex volumes add to s². Integrating these bounds yields, uniformly in t,

\[
 \|F_t\|\le\lambda^{-1},\quad
 \|DF_t[H]\|\le\lambda^{-2}\|H\|,\quad
 \|D^2F_t[H,K]\|\le2\lambda^{-3}\|H\|\|K\|.
\]

For Phi_t(Gamma,gamma)=gamma^T F_t(Gamma)y its second directional derivative along (H,h) is

\[
 \gamma^T D^2F_t[H,H]y+2h^TDF_t[H]y.
\]

Both gamma and the empirical gamma are bounded in norm by a data-independent constant depending only on m. The segment joining Gamma_*>=2lambda I to Gamma_0>=lambda I stays in the displayed positive domain. Consequently Phi_t has first derivative bounded by C Y and Taylor remainder bounded by C Y||Delta||² on that whole segment, uniformly in t and x. Taking the preceding conditional expectations proves

\[
 \sup_{t\ge0}
 |\mathbb E[f_{\rm fr}(t,x)\mid G_n]
      -\gamma_*^TF_t(\Gamma_*)y|
 \le CY/n.
 \tag{32a}
\]

Taking x to be a training input includes (31). No inverse of a history Gram appears. The uniformity in x here is stronger than what the joining-velocity proof supplies; it relies on bounded initial tanh features, not on an initialization Lipschitz constant growing with the query norm.

The same estimate holds uniformly over the interpolation profiles in (20). Conditional row covariance is ((1+theta)/2)Q_1+((1-theta)/2)Q_2 in the first block and the reversed mixture in the second. Each mixture has the same deterministic mean and O(1/n) mean-square error, uniformly in theta; the preceding Taylor argument applies. This is a genuine small-source calculation for the frozen system.

For the actual flow, the fitting input gives uniformly on the good event

\[
 \|\Gamma(t)-\Gamma_0\|\le C Y^2,\qquad
 \|e(t)\|_m\le C Y^3e^{-\kappa t}
\]

in the exact residual equation dot r=-2Gamma r+e. Subtracting the frozen equation and using its uniformly positive Gram gives

\[
 \sup_{t\ge0}\|f_n(t)-f_{\rm fr}(t)\|_m\le C Y^3.
 \tag{33}
\]

For a fixed query, the initial-to-current query/training kernel difference is O_x(Y²), and the hidden-motion query-velocity term is O_x(Y³ exp(-kappa t)). Integrating their exact derivative difference gives the corresponding O_x(Y³) bound for (32). The qualitative population limit, together with the bounded good-event predictions and the frozen limit just computed, transfers this same O_x(Y³) comparison to f_M and the frozen population predictor. The triangle inequality between these two comparisons and (32a) therefore gives the actual conditional mean bias bound

\[
 \sup_{t\ge0}|m_n(t,x)-f_M(t,x)|\le C_x Y/n+C_xY^3.
 \tag{34}
\]

For fixed positive Y, (34) is not a width convergence rate. Choosing Y to vanish with n would change the contract.

To improve (34) by absorption, one would need a relation of the form

\[
 \mathcal T_n\le C_xY/n+C_xY^2\mathcal T_n,
 \tag{35}
\]

where T_n controls the **same collection of interpolation response observables** on both sides. The supplied state Lipschitz theorem is not (35). It propagates a pathwise source; it does not compare the expectations under the different covariance profiles.

The exact obstruction in trying to derive (35) for the prediction trace alone is visible already in (17). Differentiating its expectation along theta produces signed traces of all the kernels K^0,K^A,K^v,Q and of their products with residuals. Those involve initialized-matrix responses to evolving h,d, not just the prediction. Further differentiation or a trajectory tangent equation introduces products of matrix-entry response fields. The prediction trace does not bound those response traces. The finite family in (13) is enough for joining independent blocks because its fluctuations are small by Poincare, but it is not closed under these covariance derivatives.

For the hard clip, deriving a classical second-response equation additionally differentiates the indicator of the unsaturated interval; its distributional derivative has threshold surface contributions. The weak identity (26) retains them automatically but does not bound their size or make them proportional to the prediction trace. Smoothing and then omitting these contributions would be invalid. A response-space contraction could conceivably include them and use the small activity, but its norm, its finite-width source estimate, and its uniform clipping approximation have not been constructed here.

Accordingly the small-label check establishes the O(Y/n) leading source and the width-uniform O(Y³) nonlinear remainder. It does not establish the self-consistency inequality (35), even for fixed M=1. This is a major missing implication, not a minor differentiability detail.

## 9. Claim status and route recommendation

Proved here, relative to the fully stated deterministic stability and qualitative limit in the assigned inputs:

1. A sufficient dyadic bias criterion with explicit geometric summation.
2. A root-width, expected all-time comparison between the joined block-diagonal closure and two independent width-n closures, equation (12).
3. A covariance-profile interpolation with the correct Gaussian endpoint laws and the same reused transpose, equation (20).
4. Exact weak interpolation identities that remain valid for hard clipping, equations (25)-(29), including the exact zero derivative at the fully connected endpoint.
5. An all-time O_x(Y/n) frozen-readout mean bias and an O_x(Y³) comparison remainder for the actual small-label dynamics.

Open: an interior signed-trace cancellation such as (30), or a rigorously closed small-activity response inequality that implies the needed bound on c_1-c_0. Concentration about each finite-width center, endpoint symmetry, and deterministic finite activity do not supply that estimate.

Recommended status: **blocked at a quantified Gaussian response cancellation**, preserving the joining lemma and weak interpolation construction. Reopen upon a uniform bound on the within/cross expected response difference, or a genuinely closed response norm giving (35), including the clipping threshold terms. The broad root-width conjecture remains open; this route neither proves it nor provides a counterexample to the actual clipped flow.
