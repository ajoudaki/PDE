# Part V. Population and finite-algorithm bridge at each fixed depth

Fix a finite hidden depth L>=2 and the activation parameters already selected by the theorem. All constants in this chapter may depend on this fixed L, a, e, dataset, and physical observation horizon T. Such dependence does not enter the selection of a,e. Write

    K_l=a^(l-1), eps=e/a,
    chi_l(y)=y+[1+eps psi(K_l y)]/K_l,
    g_l=chi_l',
    D_(l,R)(y,q)=q+eps psi'(K_l y)tau_R(q).

For each fixed l the functions g_l and g_l' are bounded and continuous. The clipped coordinate map has bounded continuous first derivatives, with

    |g_l|<=2, |g_l'|<=eps K_l,
    |D_(l,R)|<=2|q|, |D_q|<=2, |D_y|<=2eps K_l R.       (V.1)

No sign restriction is imposed on psi' or psi''.

We use the normalized hidden fields Y_l=z_l/a^(l-1), X_l=h_l/a^l. The raw matrices and original readout C are unchanged. At the bottom, w=sqrt(d)W^1 and u_i=x_i/sqrt(d) are an isometric notational representation of the original bottom metric: (d/n)||Delta W^1||_F^2=||Delta w||_n^2. Put

    Y_(1,i)=<w,u_i>,
    Y_(l,i)=A_l X_(l-1,i), X_(l,i)=chi_l(Y_(l,i)),
    f_i=a^L<C,X_(L,i)>, p_i=a^L(y_i-f_i).

The physical capped raw vector field is exactly

    V_(R,C)=sum_i p_i X_(L,i),
    V_(R,A_l)=sum_i p_i delta_(l,i) tensor X_(l-1,i),
    V_(R,w)=sum_i p_i delta_(1,i)u_i,                      (V.2)

where

    q_(R,L)=C,
    delta_(R,l)=D_(l,R)(Y_l,q_(R,l)),
    q_(R,l)=A_(l+1)^*delta_(R,l+1), l<L.

Thus physical time is used throughout this chapter. The factor a^L is in p, not in a replacement metric or training step. Reserve b_l=g_l(Y_l)t_l, t_L=C, t_l=A_(l+1)^*b_(l+1), for the TRUE normalized backward fields, even when they are observed at a capped state. The original raw backward fields equal a^(L-l+1)b_l.

We use the Hilbert raw norm on the first vector block, all Hilbert--Schmidt increments, and C. On finitely many blocks it is equivalent to their sum norm, which may be used in estimates by altering constants. Every comparison below takes place either at the same width with identical initialization or on the common population spaces. No cross-width identification of operators is used.

## V.1. Exact inputs and dependency order

The following results have been proved earlier and are the only inputs to this chapter.

(F) Every fixed finite Gaussian program with independent initialized adjacent matrices, both orientations, independent root tuples, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has full-sequence within-layer empirical W2 convergence, including all second moments. An initialized forward query on h has the scalar representation

    xi_h + sum_v v E[partial_(zeta_v) h],                 (V.3)

where v ranges over preceding reverse inputs to that matrix. Its reverse rule includes the current forward inputs. Gaussian source covariances are the full actual input Grams; distinct oriented groups are independent. Named slots are differentiated separately at singular covariance, with all coefficients, contractions, controls, and covariances frozen. The construction is continuous under bounded-derivative finite query perturbations, by positive-semidefinite covariance-square-root coupling. The common initialized action norms are <=10 and their reverses are their genuine adjoints. The finite norm event has probability tending to one. These conclusions apply to any finite number of adjacent matrices because their conditioning proof counts instructions rather than layers.

(G) The capped population physical paths are global. First projections, current action norms, C, and physical raw directions have bounds independent of cap on compact horizons. The paths stay in a common primal ball with strict continuation slack.

(S) The direct controlled source estimate and residual-clock bound give, for some M_* and every p>=2,

    sup_(R,t,l,i) ||q_(R,l,i)(t)||_p <= M_* sqrt(p).       (V.4)

Here L,a,e are fixed. This includes q_L=C, uses the actual capped incoming fields, and has already been transferred from controlled Euler programs to physical capped paths. It does not replace the actual residuals by prescribed controls in training.

The chain and adjunction rules from the foundations apply to bounded g_l and to bounded-action curves with Hilbert--Schmidt derivatives.

The proof order below is deliberate. Raw cap removal uses only (G),(S). Fixed-cap Euler bounds and fixed-mesh primary Gaussian laws supply finite primal events before Gaussian probe estimates use them. Probe estimates supply pointwise source rows; these justify appended velocity queries. Only then are uniform-time empirical velocity laws proved. True backward observations require a separate finite truncation argument. Finally same-width cap comparison transfers everything to actual uncut algorithms.

## V.2. One-cap-factor comparison and population cap removal

On a fixed primal ball, forward propagation gives

    sum_(l,i)(||Y_l-Ybar_l||_2+||X_l-Xbar_l||_2)
       +sum_i|p_i-pbar_i| <= C||Theta-Thetabar||raw.       (V.5)

The bottom projection is bounded. Each upper step uses

    A_l X_(l-1)-Abar_l Xbar_(l-1)
       =(A_l-Abar_l)X_(l-1)+Abar_l(X_(l-1)-Xbar_(l-1)),

||A_l-Abar_l||op<=||A_l-Abar_l||HS, and the Lipschitz constant of chi_l. The residual estimate follows by expanding the C,X_L inner product. For rank-one blocks,

    ||u tensor v-ubar tensor vbar||HS
       <=||u-ubar||_2||v||_2+||ubar||_2||v-vbar||_2.       (V.6)

For R'>=R, including infinity,

    |D_(l,R')(y,q)-D_(l,R)(ybar,qbar)|
       <=2|q-qbar|+2eps K_l R|y-ybar|
                       +2eps |qbar|1_(|qbar|>R).         (V.7)

To prove it, first change q inside D_(l,R'), costing 2|q-qbar|. Split the remaining perturbation into

    eps[psi'(K_l y)-psi'(K_l ybar)]tau_R(qbar)
      +eps psi'(K_l y)[tau_(R')(qbar)-tau_R(qbar)].

The first term uses |psi''|<=1 and |tau_R|<=2R; the second vanishes for |qbar|<=R and otherwise has absolute value <=2eps|qbar|.

Here is the full depth recursion. Write alpha=||Theta-Thetabar||raw and E_l=||delta_(R',l)-delta_(R,l)(Thetabar)||_2, maximizing over samples. At the top, (V.7) gives E_L<=C(1+R)alpha+C Tail_L. At the next level,

    ||q_(R',l)-q_(R,l)(Thetabar)||_2<=C alpha+C E_(l+1),
    E_l<=2C E_(l+1)+C(1+R)alpha+C Tail_l.

Solving this finite downward recursion yields

    sum_l E_l <= C(1+R)alpha+C sum_l Tail_l.

Each new R multiplies a forward difference in (V.5), never E_(l+1). Using (V.6) and the actual residual difference therefore gives

    ||V_(R')(Theta)-V_R(Thetabar)||raw
       <=C(1+R)||Theta-Thetabar||raw
                     +C sum_(l,i)||qbar_(R,l,i)1_(|qbar_(R,l,i)|>R)||_2.
                                                               (V.8)

The same bound controls all backward discrepancies. Its tail terms belong only to the reference.

From (V.4), Markov's inequality with moment exponent p=(u/(3M_*))^2, for u large, gives

    sup_(R,t,l,i)||q_(R,l,i)1_(|q_(R,l,i)|>u)||_2
                    <=C exp(-c u^2).                     (V.9)

Indeed E[q^2 1_(|q|>u)]<=u^2(M_*sqrt(p)/u)^p, and the polynomial prefactor can be absorbed into a smaller exponential rate. Integrating (V.8) and applying its iterated integral inequality yields

    sup_(t<=T)||Theta_(R')(t)-Theta_R(t)||raw
      +sup_(t<=T)||V_(R')(Theta_(R')(t))-V_R(Theta_R(t))||raw
                        <=C_T exp(C_T R-cR^2).           (V.10)

The second term follows by substitution in (V.8), absorbing factors 1+R. Paths and raw derivatives are uniformly Cauchy. Their limits satisfy the integral equation Theta(t)=Theta(0)+integral_0^t V(s)ds, with continuous V, and (V.8) against the limit state identifies V=V_infty(Theta). Hence the limit is a strong C1 raw solution. Integer caps and horizons give a single consistent global construction.

Any bounded-primal strong uncut competitor is compared with the same capped reference by (V.8). Its primal bound changes C_T, but no competitor tail is used. The resulting error still vanishes as R tends to infinity. At a reached time t_0 the initial discrepancy from the capped reference is already bounded by (V.10); another exp(C_TR) factor leaves a vanishing error. This proves uniqueness and unique continuation from each reached state, without asserting arbitrary-state local Lipschitzness of the uncut field.

## V.3. Raw Euler bounds and finite primal events, before source estimates

For fixed R and a larger primal ball, (V.1),(V.5),(V.6) make V_R locally Lipschitz with width-independent constants M_0,L_0. The autonomous Euler local defect is <=L_0M_0 h_j^2/2. The error recursion gives

    max_k||Theta_R(t_k)-Theta_R^pi(t_k)||raw
       <=(L_0 M_0 T/2)exp(L_0 T)|pi|.                    (V.11)

Raw interpolation adds <=2M_0|pi|. Stop at the boundary of the larger ball, choose |pi| sufficiently small, and the strict slack excludes first exit. This proves bounded population Euler arrays without source or velocity estimates.

At a fixed auxiliary mesh, (F) gives every primary finite node law and contraction. Exact rank unrolling gives

    max_k||A_(l,k,n)||op
       <=||A_(l,0,n)||op
          +sum_(j,b)h_j|p_(j,b,n)|
                          ||delta_(l,j,b,n)||_n ||X_(l-1,j,b,n)||_n.
                                                               (V.12)

The sum is finite. Every summand converges to its population counterpart, whose total is bounded by the population primal and direction bounds, uniformly over the sufficiently fine meshes in (V.11). First-layer and readout norms converge too; include the full first-layer Gaussian root vector in the fixed program when its norm is needed. Thus, at each fixed sufficiently fine mesh, a deterministic enlarged finite primal ball with slack contains all finite coarse nodes and interpolants with probability tending to one. This argument uses no velocity or source-row estimate.

The actual finite initialization has ||C_(0,n)||_n=O_P(n^-1), since E||C_(0,n)||_n^2=n^-2. For fixed cap and transcript, compare it to a same-matrix auxiliary Euler program with zero readout root. Stopped finite-step Lipschitz stability propagates this vanishing norm, and the preceding slack closes the comparison. Thus the actual fixed-program limit has C_0=0. Every actual finite GF/GD and every same-width reference comparison below retains the original random C_(0,n); no algorithm is reset.

## V.4. Fixed-cap response rows by Gaussian probes

Fix R,T and a sufficiently fine physical Euler mesh. Freeze p, all contractions, covariances, and response coefficients in formal source derivatives. The exact primary source equations are

    Y_(1,k,i)=Y_(1,0,i)+sum_(j<k,b)h_j p_(j,b)Gamma_(ib)delta_(1,j,b),
    C_k=sum_(j<k,b)h_j p_(j,b)X_(L,j,b),

    Y_(l,k,i)=xi_(l,k,i)
                      +sum_(j<k,b)Acal_(l,ki,jb)delta_(l,j,b),
    q_(l-1,k,i)=zeta_(l-1,k,i)
                      +sum_(j<=k,b)Bcal_(l,ki,jb)X_(l-1,j,b),
                                                               (V.13)

for 2<=l<=L, where

    Acal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))X_(l-1,k,i)
                         +h_j p_(j,b)E[X_(l-1,k,i)X_(l-1,j,b)],
    Bcal_(l,ki,jb)
       =E partial_(xi_(l,j,b))delta_(l,k,i)
             +1_(j<k)h_j p_(j,b)E[delta_(l,k,i)delta_(l,j,b)].
                                                               (V.14)

They retain every current transpose return. Source variances are bounded by the primal norms of their actual inputs.

Choose one oriented answer family and a fresh independent standard Gaussian vector g in its answer layer. Add epsilon alpha_(j,b)g, |alpha_(j,b)|<=1, at selected answer slots and recompute all subsequent residuals and raw updates. On the enlarged ball the raw discrepancy satisfies

    E_(k+1)<=(1+Ch_k)E_k+Ch_k|epsilon| ||g||_n.           (V.15)

Thus arbitrary bounded forcing at every time gives E_k<=C|epsilon|||g||_n. A single forcing at time j gives <=Ch_j|epsilon|||g||_n at all later states. Current query errors have the direct O(|epsilon|) term; strictly later queries have the O(h_j|epsilon|) term. These estimates follow from (V.1),(V.5),(V.6) and include the recomputed residuals. For small fixed epsilon, first-exit and the finite primal event of Section V.3 keep this perturbed fixed program in the enlarged ball with probability tending to one.

Let V_k be a selected scalar primary output. At fixed mesh and epsilon, (F) passes <g,V_(k,n)^epsilon>_n to E[G V_k^epsilon]. The scalar G is independent of all oriented source groups and original roots. With deterministic coefficients frozen, its only explicit occurrences are the answer additions. Gaussian integration by parts gives

    E[G V_k^epsilon]
        =epsilon sum_(j,b)alpha_(j,b)
                              E partial_(eta_(j,b))V_k^epsilon.    (V.16)

At this fixed transcript the expression has bounded first derivatives and linear growth, so the Gaussian boundary term vanishes and differentiation is integrable. Its expected named derivatives converge as epsilon tends to zero: chronologically couple all finite covariance matrices by their positive square roots; earlier inputs and contractions converge in L2; continuous first derivatives with finite deterministic bounds on a compact coefficient neighborhood pass their expectations by dominated convergence. This uses no covariance derivative or inverse.

The unperturbed <g,V_(k,n)^0>_n tends to zero: conditionally its variance is ||V_(k,n)^0||_n^2/n. Cauchy--Schwarz and (V.15), followed by width then epsilon limits in (V.16), give

    |sum_(j,b)alpha_(j,b)E partial_(eta_(j,b))V_k|<=C.

Choose the deterministic signs of the expected derivatives. A single strictly past insertion gives Ch_j instead. Together with the learned contractions in (V.14), this proves

    |Acal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,kb)|<=C.                                  (V.17)

This bounds absolute EXPECTED derivative rows; it has not replaced |E partial V| by E|partial V|.

The current reverse rows have an explicit descending recursion. Put N_(l,k,i)=D_y(Y_(l,k,i),q_(l,k,i)), V_(l,k,i)=D_q(Y_(l,k,i),q_(l,k,i)), and set Bcal_(L+1,ki,kb)=0 for the readout integrator. Then

    Bcal_(l,ki,kb)
      =1_(i=b)E N_(l,k,i)
       +Bcal_(l+1,ki,kb) E[V_(l,k,i)g_l(Y_(l,k,b))],       (V.18)

for l=L,L-1,...,2. Indeed the current Y_l has derivative identity in its own current xi_l, while all strictly past corrections have zero current derivative. Differentiate q_l's current return and then its gate. At the top C_k uses strictly past X_L, so its current xi derivative is zero. Formula (V.18) starts there and keeps the exact signed current returns at every lower level.

## V.5. Pointwise source rows and primary moments

Within layer l let R_l(H) be the sum of absolute derivatives in all primary named sources in that layer through the final mesh time, including its initial root coordinates if desired. Those families are xi_l for l>=2 and zeta_l for l<L; future derivatives vanish. Freeze all coefficients. Using (V.13),(V.17), coordinate differentiation gives, with maxima over the three samples understood,

    Z_(1,k)<=C+C sum_(j<k)h_j D_(1,j),
    Z_(l,k)<=1+C sum_(j<k)h_j D_(l,j), l>=2,
    H_(l,k)<=2 Z_(l,k),
    Cpartial_k<=C sum_(j<k)h_j H_(L,j),
    Q_(l,k)<=1+C H_(l,k)+C sum_(j<k)h_j H_(l,j), l<L,
    D_(l,k)<=C_R Z_(l,k)+2Q_(l,k), l<L,
    D_(L,k)<=C_R Z_(L,k)+2Cpartial_k.                      (V.19)

Here Z,H,Q,D denote the corresponding pointwise derivative-row seminorms, not primal values. Every same-time reverse term is a forward field already defined at that time; there is no algebraic same-time loop. Let U_k be the maximum of Z_(l,k) and Cpartial_k. The last four lines bound the other fields by C(1+U_k+sum_(j<k)h_j U_j). Substitute into the first lines and use

    sum_(j<k)h_j sum_(r<j)h_r U_r
       <=T sum_(r<k)h_r U_r.

It follows that U_k<=C+C sum_(j<k)h_j U_j, hence U_k<=C exp(CT). Returning to (V.19) proves a deterministic bound

    R_l(H_(k,i))<=C_(R,T)                                  (V.20)

for every primary scalar field, uniformly over all sufficiently fine meshes and times.

Replace these derivative seminorms by Lp norms in the same inequalities. Direct Gaussian sources and roots have norms <=C sqrt(p); chi_l has linear growth and D_(l,R) is bounded by 2|q|. Minkowski and the same discrete inequality give

    sup_(pi,k,l,i)||H_(k,i)||_p<=C_(R,T)sqrt(p), p>=2,       (V.21)

for all primary fields and C. No temporal independence or Lp operator estimate for an initialized matrix has been used.

## V.6. Ascending velocity queries, with complete induction and nested truncation

At a physical Euler node let P_(l,i),U_(l,i) denote the instantaneous normalized preactivation and feature velocities in direction V_R(Theta_k). Exactly,

    P_(1,k,i)=sum_b p_(k,b)Gamma_(ib)delta_(1,k,b),
    U_(l,k,i)=g_l(Y_(l,k,i))P_(l,k,i),
    P_(l,k,i)=sum_b p_(k,b)delta_(l,k,b)
                                E[X_(l-1,k,b)X_(l-1,k,i)] + J_(l,k,i),
    J_(l,k,i)=A_(l,k)U_(l-1,k,i),  2<=l<=L.                (V.22)

The feature multiplier is the TRUE derivative g_l, even for a capped update direction. Append all A_(2,0) velocity queries after the complete primary transcript, then all A_(3,0) queries, and continue up to A_(L,0). No appended query feeds training. At level l, the only preceding opposite-orientation inputs for A_l are the primary delta_l fields; earlier appended levels use different matrices, and other level-l velocity queries use the same forward orientation. The source formula therefore is

    J_(l,k,i)=gamma_(l,k,i)
                       +sum_(j<=k,b)Ecal_(l,ki,jb)delta_(l,j,b),
    Ecal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))U_(l-1,k,i)
          +1_(j<k)h_j p_(j,b)E[X_(l-1,j,b)U_(l-1,k,i)].    (V.23)

The new forward source gamma_l has covariance with every source of the same orientation equal to the inner product of their actual query inputs, and variance ||U_(l-1,k,i)||_2^2. It is a distinct named argument; its formal derivative in primary zeta_l is zero even if same-family covariance is singular. Sources later than time k have zero derivatives in the time-k input, despite the appended ordering.

Here is the induction invariant before constructing layer l's new action: all lower velocity observations have their joint finite empirical W2 laws, their exact formulas (V.23), Lp bounds <=C sqrt(p), and pointwise bounds

    R_(zeta_(m)) P_(m,k,i)<=C,
    R_(zeta_(m)) U_(m,k,i)<=C(1+|P_(m,k,i)|), m<l,        (V.24)

where only the primary transpose sources of the indicated layer are differentiated. For the bottom, (V.20)--(V.22) give the first inequality, and the exact scalar derivative

    partial_eta[g_m(Y_m)P_m]
        =g_m'(Y_m)P_m partial_eta Y_m
                           +g_m(Y_m)partial_eta P_m       (V.25)

gives the second. Primary moments (V.21) give the base Lp bound.

Assume the invariant through l-1. Its second inequality has an integrable envelope, so the total expected response row in (V.23) is bounded by C. Cauchy--Schwarz bounds the learned row by C sum_j h_j<=CT. The actual L2 norm of U_(l-1), already known before the new action, bounds gamma_l's variance. The formula (V.23), Gaussian moments, (V.21), and Minkowski then give

    sum_(j<=k,b)|Ecal_(l,ki,jb)|<=C,
    ||J_(l,k,i)||_p+||P_(l,k,i)||_p+||U_(l,k,i)||_p
                              <=C sqrt(p).               (V.26)

Differentiate (V.23) only in the primary zeta_l coordinates: all coefficients are frozen and gamma_l has derivative zero. By (V.20) the derivative row of the sum is bounded by the coefficient-row bound times C. The explicit first term in P_l in (V.22) is a deterministic linear combination of primary delta_l, so its row is also bounded by C. This proves the first part of (V.24) for m=l. Applying (V.25) proves its second part. This establishes precisely the invariant needed for the next matrix. Constants may increase with the fixed number of layers; the argument does not assume a future-layer moment estimate.

The formulas just used must be justified before unbounded products enter (F). Replace each multiplier product by g_m(Y_m)tau_M(P_m). It is a bounded-derivative instruction, and its exact named derivative is

    g_m'(Y_m)tau_M(P_m)partial_eta Y_m
             +g_m(Y_m)tau_M'(P_m)partial_eta P_m.          (V.27)

At the first action its derivative row is bounded independently of M by C(1+|P_1|), integrable by the already-proved primary bound. Thus (F) applies for fixed M, and the row and moment estimates in (V.26) hold independently of this observation cap. Dominated convergence as M tends to infinity identifies every expected coefficient in (V.23). Input L2 convergence and bounded initialized actions identify the actual untruncated query; its covariance converges by second-moment convergence and is coupled by covariance square roots.

For clarity, empirical removal uses only second moments. If (Z_n,P_n) converge under an L2 coupling to (Z,P), then

    ||g(Z_n)P_n-g(Z)P||_2
       <=||g||infty||P_n-P||_2+||[g(Z_n)-g(Z)]P||_2 ->0.  (V.28)

For the second term split at |P|<=M: that part is <=Lip(g)M||Z_n-Z||_2, and the remaining part is <=2||g||infty||P1_(|P|>M)||_2. Take n first, then M. The positive-part tail functional T_M(P)=||(|P|-M)_+||_2 is 1-Lipschitz under L2 coupling, and |P|1_(|P|>2M)<=2(|P|-M)_+. Consequently fixed-program W2 convergence makes the empirical input clipping error vanish in the width-then-cap order. Bounded action norms transfer it to the output error.

At a general new level l, retain all previous inner observation caps and one outer cap M in g_(l-1)(Y)P_(l-1). At fixed caps, (F) applies to the entire finite appended program. First remove the previously constructed inner caps while M stays fixed. The established lower-level formulas have convergent deterministic coefficients and covariance-square-root couplings, so the rows of P_(l-1) in the relevant primary zeta_(l-1) coordinates converge in probability and remain bounded, by their expression as bounded rows of primary delta. Formula (V.27) at fixed M therefore passes expected derivatives by dominated convergence. Formula (V.28) and bounded actions pass the corresponding L2 inputs and outputs. Now remove M. The envelope C(1+|P_(l-1)|) from the already established invariant is integrable and independent of M, so dominated convergence gives the untruncated expected response coefficients. The empirical error is removed by the positive-part tail argument. This is the induction step giving both the derivative-valid formula and its joint empirical law. It does not invoke (F) directly for the unbounded product or assume derivative convergence from W2 alone.

The induction reaches L and proves fixed-cap, mesh-uniform marginal C sqrt(p) bounds for every P_l,U_l. All same-family time/sample/source covariances are retained in any finite concatenation of these observations.

## V.7. Deterministic velocity comparison and fixed-cap time limits

For states Theta,Thetabar on one primal ball and raw directions v,vbar in a bounded direction ball, put alpha=||Theta-Thetabar||raw, beta=||v-vbar||raw. Define P_1=v_w u_i, U_l=g_l(Y_l)P_l, and P_l=v_(A_l)X_(l-1)+A_l U_(l-1). Then, for M>=1,

    sum_(l,i)(||P_l-Pbar_l||_2+||U_l-Ubar_l||_2)
      <=C[beta+(1+M)alpha+sum_(l,i)T_M(Pbar_(l,i))].      (V.29)

To verify the exact depth recurrence, the bottom P-error is <=C beta. At every upper layer expand

    P_l-Pbar_l=(v_(A_l)-vbar_(A_l))X_(l-1)
       +vbar_(A_l)(X_(l-1)-Xbar_(l-1))
       +(A_l-Abar_l)Ubar_(l-1)+A_l(U_(l-1)-Ubar_(l-1)).

Its norm is <=C(alpha+beta+||U_(l-1)-Ubar_(l-1)||_2). Moreover

    ||U_l-Ubar_l||_2
       <=2||P_l-Pbar_l||_2+C M||Y_l-Ybar_l||_2
                                         +4T_M(Pbar_l).

The last line follows by clipping Pbar_l at M and using bounded g_l,g_l'. Solve these two finite recurrences upward, using (V.5). Each new M multiplies a forward discrepancy already bounded by C alpha, so there is one M. The constant depends only on the fixed activation and the primal/direction ball, and is independent of R,M.

If ||P||_4<=C, then T_M(P)<=C^2/M. Apply (V.29) with the Euler node as reference, (V.11), the fixed-cap raw Lipschitz bound, and Section V.6 moments. Choosing M=|pi|^(-1/2) gives uniform population hidden-velocity error <=C_(R,T)sqrt(|pi|) between the instantaneous Euler node velocities and the cap-flow velocities. The state error is O(|pi|). The foundations' strong chain rule gives the actual flow velocities used here: at each level the bounded multiplier g_l preserves L2 continuity, and differentiating A_l X_(l-1) gives exactly the stated P recurrence. This does not assume ambient L2-to-L2 Frechet differentiability of chi_l.

At each fixed time, strong L2 convergence has an almost-sure subsequence. Fatou passes all mesh moment bounds to the cap-flow fields and velocities, giving sup_(t<=T)||H_R(t)||_p<=C_(R,T)sqrt(p). Apply (V.29) at two cap-flow times: raw states and directions are Lipschitz at fixed cap, and the fourth-moment tail estimate gives an L2 velocity modulus C_(R,T)|t-s|^(1/2). Only marginal moments are claimed; no random time-maximum bound is used.

## V.8. Fixed-cap finite GF and raw GD

Let Theta_(R,n)^pi be the same-width, same-initialization coarse Euler reference. On the high-probability primal event of Section V.3, compare until exit the actual finite capped GF, or the actual fine raw Euler scheme with deterministic step eta_n=n^-2. The coarse interpolant has vector-field defect <=L_0M_0|pi|, fine Euler has defect <=L_0M_0 eta_n, and GF has zero defect. Gronwall gives

    sup_(t<=T)||Theta_(R,n)(t)-Theta_(R,n)^pi(t)||raw
                           <=C_(R,T)(|pi|+eta_n).         (V.30)

Here eta_n=0 denotes GF. Choosing the mesh below slack excludes first exit and continues finite capped GF through T. The actual fine-Euler direction is V_R evaluated at its preceding fine node; it is not replaced by the field at the interpolated state. Its direction error against the preceding coarse-node field is still <=C_(R,T)(|pi|+eta_n), by bounded within-step displacement and fixed-cap Lipschitzness.

Apply (V.29) at the same width using the coarse node as reference. At fixed pi,M, Section V.6 gives joint empirical W2 convergence of all coarse velocities. Their finitely many empirical positive-part tails converge and are bounded in the limit by C/M. Thus the width-limit upper bound in probability for the velocity discrepancy is

    C_(R,T)[(1+M)|pi|+M^-1].                              (V.31)

Choose M=|pi|^(-1/2) at that fixed mesh, take width first, and then refine pi. This gives a vanishing bound. No empirical fourth moment or growing-transcript Gaussian law was invoked.

For each layer, let mu_(R,n,l)(t) denote the empirical law of the same-layer tuple of all three samples of chosen primary fields and hidden velocities. The corresponding population law is mu_(R,l)(t). At each time couple actual and coarse arrays by neuron index. The triangle inequality is

    sup_t W2(mu_(R,n,l)(t),mu_(R,l)(t))
      <=sup_t||actual finite tuple-coarse finite node tuple||_n
        +max_k W2(coarse finite node law,coarse population node law)
        +sup_t||coarse population node tuple-population flow tuple||_2.
                                                               (V.32)

At fixed mesh the middle term vanishes by the finite appended program theorem. The outer terms vanish after mesh refinement by (V.11),(V.29)--(V.31). Therefore these same-layer laws converge uniformly in physical time in W2, in probability along the full width sequence. Concatenating coordinates at finitely many requested times gives their joint-time W2 laws with the same proof; all within-layer time/sample correlations are preserved. Predictions and loss are continuous functions of the convergent contractions.

The functional T_M is 1-Lipschitz in W2: apply the pointwise Lipschitz function (|x|-M)_+ under any coupling and then the triangle inequality in L2. Thus all empirical fixed-level primary and velocity tails converge uniformly in time at fixed cap. In particular their second moments are asymptotically uniformly integrable over time; this is a width-limit conclusion, not a uniform finite-width high-moment assertion.

## V.9. Descending true-backward observations and every raw kernel block

At fixed cap and fixed finite primary transcript, append the true chain in descending order:

    t_L=C, b_L=g_L(Y_L)t_L,
    t_l=A_(l+1)^*b_(l+1), b_l=g_l(Y_l)t_l, l=L-1,...,1.

For the first gate use g_L(Y_L)tau_M(C), a bounded-derivative instruction. At fixed M, (F) gives its joint law. Formula (V.28) and positive-part tail convergence remove M. The current action A_L^* consists of its initialized adjoint and its explicit learned rank-one sum. Uniform operator bounds and Cauchy--Schwarz transfer the input L2 error through both pieces, so the first true incoming field has the law of the actual population adjoint action. This is the descending induction base.

The induction invariant at level l+1 is joint W2 convergence of all higher true observations and the primary/velocity transcript, hence uniform removal of each of their finite empirical second-moment tails. Retain all inner caps representing this known chain and add an outer cap at t_l in the next product g_l(Y_l)tau_M(t_l). At fixed outer M remove inner caps first using bounded-derivative continuity, their known W2 laws, and bounded current action errors. Then remove M by (V.28) and the newly known second-moment tails of t_l. Apply A_l^* to obtain t_(l-1), transferring the error by its bounded action norm. This proves the invariant at level l. The finite chain reaches the bottom. The argument supplies actual observation laws; it does not claim an untruncated expected-derivative formula without separate domination.

For uniform time passage, at two states on a bounded ball downward substitution gives

    sum_(l,i)(||t_l-tbar_l||_2+||b_l-bbar_l||_2)
      <=C[(1+M)||Theta-Thetabar||raw
                            +sum_(l,i)T_M(tbar_l)].       (V.33)

This is proved by the same gate splitting as (V.29), now followed by bounded adjoint actions. Each M multiplies a forward state difference, so the downward recurrence again has one M. The true backward map is strongly continuous along converging raw states: first use (V.28) at the top, then bounded-action continuity and the same multiplier argument at each lower level. Its time image along a strong cap-flow path is consequently compact in L2. A compact L2 set has uniformly vanishing T_M tails: cover it by finitely many epsilon-balls, use the 1-Lipschitz property of T_M, and remove tails at the finitely many centers.

Apply (V.33) with the population cap flow as reference to pass coarse population true fields uniformly to the flow. At finite width apply it with the same-width coarse fields as reference. At fixed mesh and M the descending observational closure passes their tails. Take width, then mesh at fixed M, then M to infinity using compact population tails. This extends (V.32) and its joint-time form to all true backward observations.

The true ORIGINAL raw kernel blocks are, in the normalized fields used here,

    K^1_(ij)=a^(2L) Gamma_(ij)<b_(1,i),b_(1,j)>,
    K^l_(ij)=a^(2L)<b_(l,i),b_(l,j)><X_(l-1,i),X_(l-1,j)>, 2<=l<=L,
    K^(L+1)_(ij)=a^(2L)<X_(L,i),X_(L,j)>.                 (V.34)

The factor follows either by grad_raw f_i=a^L grad_raw F_i or by multiplying the original backward and feature scalings. Every pairing is within its layer, and all off-diagonal entries are retained. Under an L2 coupling,

    |E[UV]-E[Ubar Vbar]|
       <=||U-Ubar||_2||V||_2+||Ubar||_2||V-Vbar||_2.

Thus uniform-time W2 convergence proves uniform convergence of every block entry. At a capped state this is the true gradient kernel observed there; the clipped dynamics need not use it as their prediction coefficient matrix.

## V.10. Same-width cap comparison for actual finite uncut algorithms

The finite uncut GF vector field is locally Lipschitz in its finite-dimensional raw parameters. Its exact energy identity is

    dE_n/dt=-||dot Theta_n||raw^2.

Hence its raw length on [0,T] is <=sqrt(T E_n(0)). A finite-time escape in finite-dimensional parameter space is impossible, and local solutions extend globally. This argument is for actual uncut GF, not for a clipped surrogate.

Compare actual finite uncut GF to its same-width physical capped GF reference with the same nonzero random C_(0,n). Section V.8 puts that reference, with probability tending to one for every fixed R, in a primal ball chosen independently of R from (G), with fixed slack. Its incoming empirical positive-part tails converge uniformly in time. Since |q|1_(|q|>R)<=2(|q|-R/2)_+, (V.9) supplies their width-limit bound C exp(-cR^2). Until uncut exit, the finite version of (V.8) and Gronwall give a width-limit state and actual-direction error

    epsilon_R=C_T exp(C_T R-cR^2) ->0.                    (V.35)

Choose a large fixed R making this smaller than slack and then take width. The first-exit comparison excludes exit with probability tending to one. Substitution in (V.8) also controls all uncut versus capped-update backward fields.

For actual raw GD set t_k=k eta_n, eta_n=n^-2. Its raw direction on [t_k,t_(k+1)) is V_infty(Theta_n(t_k)); its hidden fields are recomputed from the linearly interpolated raw parameters. Let E(t)=sup_(s<=t)||Theta_n(s)-Theta_(R,n)(s)||raw. Apply (V.8) at t_k against the capped reference at t_k, then add the capped within-step direction variation <=C_(R,T)eta_n. Before exit,

    E(t)<=C(1+R)integral_0^t E(s)ds
       +Ct sup_(s<=T)sum_(l,i)||q_(R,l,i,n)(s)1_(|q_(R,l,i,n)(s)|>R)||_n
       +C_(R,T)t eta_n.                                  (V.36)

The preceding-node discrepancy is bounded by E(s) because t_k<=s. This proves (V.35), the same no-exit conclusion, and the same actual-direction estimate. No width-independent Lipschitz estimate on the uncut field is required. All finite GD iterates are well-defined finite compositions; the comparison proves their required finite-horizon boundedness with probability tending to one.

Take width at fixed cap after its fixed-cap auxiliary-mesh limit, and then let R tend to infinity. Population convergence (V.10), finite comparison (V.35), and the fixed-cap laws give both actual algorithms the same full-sequence prediction, loss, forward-field, and true-backward limits. The latter may be compared directly to capped UPDATE fields by (V.8); Section V.9 separately establishes true-kernel observations on capped trajectories. Formula (V.34) now gives every actual raw kernel block uniformly on the physical horizon. The two algorithms can share their initialized references and all finite unions of observations, so the convergence holds jointly for both algorithms.

## V.11. Velocity cap removal with the necessary tail order

Raw population cap states and directions converge uniformly by (V.10). Their uncut limit has continuous normalized preactivation velocities in L2 by the strong chain rule. Those compact time images have uniformly vanishing T_M tails. Apply (V.29) using the uncut state/direction as reference. First let R tend to infinity at fixed M and then M tend to infinity. This proves uniform strong convergence of all population capped hidden velocities to the uncut hidden velocities. The Lipschitz tail functional shows that sufficiently large population caps inherit the same uniform tail removal. No estimate of the growth of C_(R,T) in the fixed-cap fourth moments is needed.

For the finite uncut algorithm against its same-width capped-flow reference, (V.29) bounds the hidden-velocity error by

    C[beta_(R,n)+(1+M)alpha_(R,n)
                 +sum_(l,i)sup_(t<=T)T_(M,n)(P_(R,l,i,n)(t))],       (V.37)

where alpha and beta are their raw state and ACTUAL direction discrepancies. The constant depends only on the common primal/direction ball and fixed L,a,e, and is independent of R,M. At fixed R,M the empirical reference tails pass to their population counterparts by Section V.8. Now take the width limit, let R tend to infinity at fixed M using (V.35) and the population strong velocity convergence just proved, and finally let M tend to infinity. The expression vanishes.

Neuron-index coupling with the capped laws and population cap limit proves uniform-time same-layer joint W2 convergence for uncut states and velocities, and finite concatenations prove joint-time convergence. For GD the direction is its preceding-node raw direction, and the chain rule is evaluated at its interpolated state with that direction. Its neighboring capped reference times differ by at most eta_n; their continuous moduli make the same estimates apply. Use right directions at nodes, with a terminal-left convention if a terminal node is included. These choices do not affect integrated speeds.

The complete limit order is: (i) fixed transcript and observation caps, width, removal of inner caps while the new outer cap stays fixed, then removal of that outer cap; (ii) fixed training cap and auxiliary mesh, width, auxiliary mesh refinement; (iii) width at fixed training cap and velocity-tail threshold M, training-cap removal at fixed M, and finally M to infinity. This prevents multiplication of an uncontrolled cap-dependent velocity moment by a cap-removal error.

## V.12. W2 path laws, integrated speeds, and fixed generated probes

For each layer define the ORIGINAL hidden path tuple

    Zpath_l(t)=(z_(l,1),h_(l,1),z_(l,2),h_(l,2),z_(l,3),h_(l,3))(t).

Returning from normalized fields multiplies their state and velocity coordinates by the fixed numbers a^(l-1),a^l and therefore preserves every convergence already proved. These population coordinate paths, and the finite hidden fields recomputed along raw interpolation, are almost everywhere absolutely continuous. The chain-rule recursion, bounded current actions and g_l, and bounded raw directions give bounded RMS hidden speeds on the stopped ball. The no-exit comparisons remove stopping with probability tending to one.

For any absolutely continuous vector path x, and its linear interpolation I_h x on a fixed observation grid of maximum interval h, Cauchy--Schwarz on an interval [u,v] gives

    |x(t)-I_hx(t)|
       <=|x(t)-x(u)|+|x(v)-x(u)|
       <=2sqrt(h)(integral_u^v |x'(s)|^2 ds)^(1/2).

Consequently

    ||x-I_hx||infty^2<=4h integral_0^T |x'(s)|^2 ds.       (V.38)

Initial second moments and this speed bound give finite second moments of the path supremum norm. Average (V.38) over finite neurons and over the population coupling. The squared W2 interpolation cost is <=4h times the corresponding integrated RMS speed squared. At a fixed observation grid, the already-proved joint-node W2 laws pass through the Lipschitz interpolation map into the uniform path norm. A triangle inequality between finite paths, their grid interpolants, the population grid interpolant, and population paths, first taking width and then h to zero, proves

    W2(n^-1 sum_alpha delta_(Zpath_(l,n,alpha)), Law(Zpath_l)) ->0

in probability in C([0,T];R^6) with its supremum norm. This argument supplies the path tightness and second moments that cannot be inferred from fixed-time laws alone.

Uniform-time velocity W2 convergence gives uniform convergence of squared RMS speeds and all within-layer cross second moments. The elementary inequalities

    | ||U||_2^2-||V||_2^2 | <=(||U||_2+||V||_2)||U-V||_2

and the product estimate after (V.34) apply under the W2 couplings. The norms have common bounds on the no-exit ball. Multiplying a uniform error by T therefore gives convergence of all integrated squared hidden speeds and their within-layer cross products. These are actual neuron-coordinate velocities, not metric derivatives of marginal probability laws.

For each original raw block, true GF has

    ||dot Theta^(l)(t)||raw^2=(y-f(t))^T K^l(t)(y-f(t)).    (V.39)

Raw GD has the same identity with residual and kernel at its preceding node, since this is its actual raw direction. Uniform convergence of predictions and kernel blocks and eta_n to zero therefore give uniform-time and integrated convergence of all blockwise squared raw speeds. For fixed-cap directions use the corresponding capped-update backward Grams in place of true hidden blocks; these are primary contractions and obey the same conclusion.

Finally, take any fixed finite layer-typed generated probe program, formed from bounded-derivative coordinate maps, scalar contractions, specified generated roots, and either orientation of initialized or current adjacent actions. Include its fixed observations in (F), together with the primary and already identified observation transcript. If an input arises as a strong common-space L2 limit of finite generated probes, approximate it first by such a finite program. The propagation inequality is

    ||A u-Abar ubar||_2
       <=||A-Abar||op ||u||_2+||Abar||op||u-ubar||_2,      (V.40)

and exactly the same holds for adjoints. In same-width and common-population comparisons, operator differences are bounded by raw Hilbert--Schmidt differences and all current operator norms are bounded. Thus each finite instruction preserves vanishing approximation error. Uniform-time versions follow by a finite time net and the strong L2 continuity of the finite probe graph. Both action orientations, same-layer second moments, and finite joint-time laws are retained. Learned population increments converge strongly in Hilbert--Schmidt norm by (V.10); finite learned-increment contractions, when requested as observations, are finite rank unrollings followed by Riemann approximation of already converging bounded contractions.

All probability conclusions are along the full width sequence: every fixed-program theorem is full-sequence convergence in probability, and each subsequent comparison gives a deterministic width-limit error that can be made arbitrarily small in the stated order. The proof neither identifies operators across different widths nor takes a simultaneous infinite-depth or infinite-time limit.
