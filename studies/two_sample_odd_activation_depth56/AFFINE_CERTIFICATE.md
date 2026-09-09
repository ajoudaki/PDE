# Explicit affine certificate at depths five and six

This new note keeps the exact raw model and the old numerical constant H. It strengthens the depth-four affine certificate. It proves only the affine, primal, probe and nonaffinity inputs; the full source supersolution and limit theorem are separate obligations.

## 1. Initialized action norm two

For an n by n matrix W with iid N(0,1/n) entries, the Gaussian matrix norm theorem gives E||W|| <= 2 and P(||W||>2+u) <= 2 exp(-c n u^2), u>0, for an absolute positive c. A primary mathematical source is Roman Vershynin, *High-Dimensional Probability*, Theorem 7.3.1 and Corollary 7.3.3, pp.167--169 in the first-edition text, available at https://anthonyhongxiao.github.io/pdfs/HDP-book.pdf. The theorem and proof were read on 2026-09-07. Its hypotheses apply because sqrt(n)W has independent standard real Gaussian entries. No numerical value of c enters our certificate.

For clarity, the sharp expectation constant follows by comparing X_uv=u^T Gv with Y_uv=g^T u+h^T v on the product of unit spheres. If alpha=<u,u'> and beta=<v,v'>, the difference of increment variances is E(Y-Y')^2-E(X-X')^2=2(1-alpha)(1-beta)>=0. Gaussian comparison bounds E sup X by E||g||+E||h||<=2 sqrt(n). The spectral norm is 1-Lipschitz in the entries' Euclidean norm, which gives the stated tail by Gaussian concentration.

Apply the tail to the finitely many initialized hidden matrices at a fixed depth, then pass to any finite generated-vector transcript. It proves ||A_j,0 v||<=2||v|| simultaneously for every generated vector. A countable dense generated span and continuity give canonical operator norms <=2. This does not assert convergence of finite-width matrices in operator norm, and does not change the canonical spaces. Initialized forward products still have RMS norm one by successive conditioning through independent Gaussian layers.

## 2. Balances and a new all-radius coercivity inequality

For L>=3 let r=sqrt((1+y1 y2 rho)/2), lambda=a^L r, and t=lambda s. Set x1=p, xj=A_j x_{j-1}, dL=D, dj=A_{j+1}^*d_{j+1}, and F=<D,xL>. The normalized raw equations are

p'=d1, A_j'=d_j tensor x_{j-1}, D'=xL.

The adjacent balances differentiated in the depth-four certificate now give

||p||^2=1+c^2, ||A_j||^2 <= c^2+4(L-j+1), (c^2)'=2F,

where c=||D||. Also c'>=1: D''=J_h J_h^* D makes c convex and its initial right derivative equals one.

Write

b_L=2^{L-1} sqrt((L-1)!),
Q_L(c)=sqrt(1+c^2) product_{k=1}^{L-1} sqrt(4k+c^2),
S_L(c)=1/(1+c^2)+sum_{k=1}^{L-1}1/(4k+c^2).

Cauchy gives F<=||p|| ||grad_p F||, F<=c||grad_D F||, and, for every matrix block, F<=||A_j||op ||grad_{A_j}F||HS. Hence, for c>0,

F' >= F^2 [c^{-2}+S_L(c)].

To integrate this without a spurious initial constant, use w=c^2. The equations and initialized forward norm one imply c(t)/t ->1 and F(t)/t ->1, so F^2/w ->1. Since d(F^2)/dw=F', integration from w=epsilon and then epsilon down to zero yields

F^2 >= c^2(1+c^2) product_{k=1}^{L-1}(1+c^2/(4k)),

c' = F/c >= Q_L(c)/b_L >= c^L/b_L,
F >= c^{L+1}/b_L.                                          (A)

The use of operator norms for matrix blocks is essential: no infinite-dimensional Hilbert--Schmidt norm of an initialized action is used.

The all-block Gram-ratio argument also gives, with K_L=4(L-2),

F'>=(L+1)(c^2-K_L)_+^L, F>=(c^2-K_L)_+^{(L+1)/2}.       (B)

Indeed each forward/backward adjacent norm ratio loses at most four, and every gradient block then has squared norm at least (c^2-K_L)_+^L. Differentiate F^2-(c^2-K_L)_+^{L+1} to obtain the second assertion.

Let T be the first time F=3/(2 lambda), and define

M=(3 b_L/(2 lambda))^{1/(L+1)}.

Then c<=M before T, and

T<=1+b_L/(L-1), S=T/lambda <= 2 M^{L+1},
r=(3 b_L/(2 a^L)) M^{-(L+1)},
M^{L+1} <= D_L delta^{-1/2}, D_L=3*2^{2L-2}sqrt(2(L-1)!). (C)

The harmless factor two in the S bound follows from 2(1+b_L/(L-1))/(3b_L)<2. For L5, b5<79 and D5<5400; for L6, b6<351 and D6<48000. These are strict elementary numerical bounds. Bounded primary norms and rank-one HS derivatives permit continuation to the target, exactly as in the depth-four certificate; (A) precludes an infinite branch below the target.

## 3. Explicit integrated Hessian: unchanged H works at both depths

Use the Hilbert direct-sum raw norm, and stop nonlinear comparison at distance rho0=1/100. This norm is equivalent to the earlier sum norm by factors at most sqrt(7) at L5/L6, absorbed below. An inactive first-root variation has zero affine Hessian contribution, so the estimate covers the full nonsymmetric raw state.

Let the L hidden primary norm bounds be r_0=sqrt(1+c^2), r_k=sqrt(4k+c^2), k=1,...,L-1. On this tube replace them by r_k+rho0 and replace the readout norm by c+rho0. Put Qtilde=product(r_k+rho0), Stilde=sum(r_k+rho0)^{-2}. The Hessian has a readout--hidden star block and a hidden--hidden block. Their operator norms are bounded respectively by Qtilde sqrt(Stilde) and (c+rho0)Qtilde Stilde. This follows by bounding each off-diagonal block by the product of the complementary primary norms; for the hidden--hidden block use the rank-one positive matrix with entries (c+rho0)Qtilde/[(r_i+rho0)(r_j+rho0)], retaining its diagonal only for an upper bound. Therefore

||Hess F|| <= Qtilde [sqrt(Stilde)+(c+rho0)Stilde].

Since sum 1/r_k <= (L+1)/2,
Qtilde/Q_L <= exp(rho0(L+1)/2), Stilde<=S_L.

Combine this with (A). Through c=8, the integrated Hessian is at most

E_L := exp((L+1)/200)b_L [sqrt(L) asinh(8)
 + (1/2)log(65) + (1/2)sum_{k=1}^{L-1}log(1+16/k)
 + (pi/200)(1+(1/2)sum_{k=1}^{L-1}k^{-1/2})].             (D)

We used S_L<=L/(1+c^2), integrated c S_L exactly, and bounded integral_0^8 S_L by (pi/2)[1+(1/2)sum k^{-1/2}]. Direct elementary bounds give E_5<1100 and E_6<5070. To verify the latter without numerical quadrature, use b6<351, exp(7/200)<1.036, sqrt6<2.45, asinh8<2.777, half log65<2.088, and half[log17+log9+log(19/3)+log5+log(21/5)]<4.962, and the final pi-term <0.042. Their product is less than 5070. For L5 the same bounds, deleting the final term in each sum, and b5<79, sqrt5<2.237, exp(.03)<1.031 give less than 1100.

For c>=8, L<=6, (B) implies

dt/dc <= c^{-L}(1-16/c^2)^{-7/2} <= c^{-L}(1+208/c^2).

The last step uses the mean value theorem and (7/2)(4/3)^{9/2}<13 on 0<=16/c^2<=1/4. All primary norms are at most sqrt(c^2+20). The crude Hessian sum bound thus yields

||Hess F|| <= L(sqrt(c^2+20)+.01)^{L-1}
 <= L c^{L-1}(1+.1/c+100/c^2).

Indeed the logarithm of the last power ratio is at most 50/c^2+.05/c<.8 and exp(u)<=1+2u for 0<=u<=.8. Multiplying the previous two estimates and integrating the non-1/c terms from 8 to infinity gives less than

6[.1/8+154/64+20.8/(3*512)+5200/4096]<23.

Consequently, for every 3<=L<=6 and any terminal c<=N with N>=1,

integral ||Hess F|| dt <= 5100 + L log N.                 (E)

For a terminal c below eight, (D) already proves this. Original-time Hessians acquire lambda and ds=dt/lambda, so (E) is also the exact original-time raw Hessian integral. Thus G<=exp(5100)M^L before T, and G<=2^L exp(5100)M^L on an extension with c<=2M.

The common numerical H from the old power-ten proof obeys

H>=10^30 exp(5640).

All primitive prefactors below can be bounded by 10^80 exp(5200), which is less than H. In particular there is no new L5/L6 prefactor replacing H.

## 4. Primal and enlarged-family estimates

For L5/L6, primary norms before the target are <=5M, and the extended/enlarged family below has primary norms <=20M. The integrated norm of any learned HS increment is <=10^8 M. To see this, before c=1 the derivative bound (20+c^2)^{L/2} and duration <=1 cost at most 21^3. Afterwards combine (A) with (sqrt(20+c^2))^L <= (c+sqrt20)^L to bound its time integral by b_L(1+sqrt20)^L M <10^8 M. The endpoint increments are smaller.

The same-state capped-versus-affine vector-field discrepancy is <=10^6 e(sqrt(20+c^2)+.01)^L. This follows by telescoping at most six forward gates and at most six backward gates, using |arctan|<=pi/2 and |tau_R(q)|<=|q|; each primary factor is at most the displayed bound and the sum of the resulting finitely many coefficients is below 10^6. Projection onto an RMS-unit input has raw norm <=1. Integrating this forcing, applying (E), and using lambda^{-1}<=M^{L+1} proves

E_raw <= H e M^{2L+2},                                  (F)
||Delta z^ell||_2+||Delta h^ell||_2 <= H e M^{2L+ell+1},
|g_e(S)-3/2| <= H e M^{2L+1}.

Here E_raw may be either the Hilbert or sum norm, after the fixed factor <=sqrt7. Require H e M^{3L+1}<=1/200 to close the tube and bound all actual forward fields. The last prediction bound retains the affine gradient factor lambda: lambda M^L E_raw has power 2L+1, while the direct gate discrepancy e M^L is smaller.

Original affine backward fields have norm <=C M^{L+1-ell}, and their capped nonlinear discrepancies are <=H e M^{3L+2-ell}. The learned coefficient errors therefore satisfy

|Delta M_Aell|_density <= H e M^{2L+ell},
|Delta M_Bell|_density <= H e M^{4L+3-2ell},
|Delta M_Bell|_row <= H e M^{5L+4-2ell}.                  (G)

The forward fields in their original normalization are bounded by constants independent of M: their active factors are a^{ell-1}r xell with r=C_L M^{-(L+1)}, and their inactive parts are frozen initial Gaussian products. The usual finite-Euler telescoping proof of inactive freezing uses bounded ordinary Frobenius norm of each learned product difference and conditional second moments; its finite number of terms is now at most six. This is also why no M^{ell-1} cost multiplies the learned forward moment error in (G).

For beta_j=1+j 10^{-14} M^{-(L-1)}, j=1,2,3, and beta_far=1+10^{-12}M^{-(L-1)}, use the exact homogeneity Theta_beta(t)=beta Theta_1(beta^{L-1}t). Because T<=72 and, on c<=2M, c'<=10^5 M^L, the base path exists for at least 10^{-5}M^{-(L-1)} beyond T without crossing c=2M. Every enlarged-time increment is below 10^{-8}M^{-(L-1)}, so these families exist on the same interval. Adjacent beta gaps and the far margin are at least 10^{-14}M^{-(L-1)}. Positive Wick-coefficient polynomials give

f'(beta)<=10^{14} M^{L-1} f(beta_far).

Fine-mesh limits preserve this estimate with a fixed factor. This factor, 2^L from (E), normalization factors a^{-O(L)}, and the at most six probe factors all fit the preceding 10^80 exp(5200) allowance. More explicitly, taking every primary bound as 100M gives every forcing/output probe bound <=7(100M)^5; their product times 64 exp(5100), even after 10^14 beta differentiation, sample-coordinate factors below 2^30, and a further 10^20 allowance for moment additions and norm conversions, is less than 10^80 exp(5200).

## 5. Exact source powers

The source-coordinate normalization is

Q z^ell=a^{ell-1} S0 xell,
Q delta^ell=a^{L+1-ell} r S0^{-1} dell,
Ahat_ell=a^{L+2-2ell}r S0^{-1} Aell S0^{-1},
Bhat_ell=a^{2ell-L-2}r^{-1} S0 Bell S0,

where S0=diag(r,sqrt(1-r^2)). A strict density receives the extra time factor lambda. On the active coordinate, original forward strict densities therefore receive a^{2ell-2}r^2, and original backward row norms receive a^{L+2-2ell}r^{-1}. Inactive forward densities are bounded constants, and inactive backward coefficients vanish. Thus no inverse inactive variance is hidden.

An answer insertion at population ell has raw forcing cost M^{L-ell} for a forward answer and M^{ell-1} for a backward answer. Observing xell costs M^{ell-1}; observing dell costs M^{L-ell}. The independent fresh-Gaussian probe argument identifies the frozen-array derivative: reflection makes covariance and learned-moment first variations vanish; deterministic source signs give row norms; a single source gives the actual strict density. This is the old argument with finitely many additional matrix calls, retaining the first preactivation and current readout cases.

With G<=H M^L the resulting table is

| Quantity | Original norm and bound |
|---|---|
| Aell and V_{ell-1}, 2<=ell<=L | strict density H M^{(2ell-L-6)_+} |
| Bell and W_ell, 2<=ell<=L | row H M^{4L+1-2ell} |
| every local R_ell,L_ell | row H M^{2L-1} |
| U_ell, 1<=ell<=L | strict density H M^{(2ell-L-4)_+} |
| backward Gaussian innovation at population ell<L | standard deviation H M^{L-ell} |
| every original forward Gaussian innovation | standard deviation H |

Beta differentiation adds at most L-1 to the listed exponent and retains numerical prefactor H by the explicit allowance above. The table does not multiply several different entries by H without accounting for the resulting power of H in a later argument.

In the active sector positivity also gives V_i >= a^{2i}r^2 I_s. Since r=3b_L/(2a^L) M^{-(L+1)} and i<=L-1, this implies the useful strict lower density

V_i >= M^{-2(L+1)} I_s.                                 (H)

This holds at each strict slot, independently of the smallest mesh step, and also for every enlarged initialization.

## 6. Nonaffinity margin

The finite affine Euler polynomials have nonnegative coefficients in independent centered initialized Gaussian entries and contain their original initialized path polynomial. Every Wick expectation in the extra squared norm and cross terms is nonnegative. Fixed-mesh uniform integrability, fixed-program convergence of second moments, and strong Euler convergence therefore give ||xell||^2>=1. Inactive freezing and orthogonality yield Var z_i^ell >= a^{2(ell-1)}.

For the requested convex family e=theta, a=1-theta, theta<=1/4, all L<=6 have a^{2(ell-1)}>1/404. Thus the old eta_* nonaffinity margin survives the same forward discrepancy restriction as in the L3/L4 proofs. The compact-gain interval a in [1/2,1] instead has the explicit variance floor 1/1024 at L6; its third-Hermite margin can be substituted if that stronger compact-gain formulation is desired.

## 7. A fully explicit general fixed-depth affine version

For arbitrary fixed L>=3, retain b_L, M, D_L in (A)--(C). Set rho_L=1/[100(L+1)], B_L=4sqrt(L(L-1)), and define

C_L=exp(1/200)b_L [sqrt(L)asinh(B_L)+(L/2)log(1+B_L^2)+rho_L*pi*L/2]+2L.

The exact argument behind (D) bounds the integral through B_L by the bracketed expression. For c>=B_L, K_L/c^2<=1/(4L). The derivative of (1-u)^{-(L+1)/2} is <=L there, giving dt/dc<=c^{-L}(1+4L(L-2)/c^2). Also

(sqrt(c^2+4(L-1))+rho_L)^{L-1}
<=c^{L-1}[1+2(L-1)rho_L/c+4(L-1)^2/c^2].

The exponent before this last linearization is below 1/4; the two integrable products beyond L/c contribute less than 2L. Hence

integral ||Hess F||dt <= C_L+L log M.

The following explicit accounting supplies every remaining numerical primitive constant. Write J=10L, and note the elementary inequalities

b_L <= (2sqrt(L))^{L-1} <= J^L,
1+b_L/(L-1) <= 2b_L <= J^L,
3b_L/(2a^L) <= J^{2L},
D_L <= J^{2L}, rho_L^{-1}=100(L+1) <= J^3.              (I)

On c<=M, every primary norm is at most 2sqrt(L)M. On c<=2M it is at most 3sqrt(L)M. The enlarged families constructed next have primary norms at most JM.

### 7a. Explicit beta family and derivative gap

Set

h=J^{-4L} M^{-(L-1)},
beta_j=1+j h/10, j=1,2,3,
beta_far=1+h.

On c<=2M we have c'<=Q_L(c)<=J^L M^L. Hence the base solution continues for at least J^{-L} M^{-(L-1)} beyond T before it can leave c<=2M. Bounded primary norms and HS derivatives justify this continuation independently of the target stopping rule. Because Lh<1/4,

(beta_far^{L-1}-1)T <= 2Lh J^L
 <= (1/2)J^{-L} M^{-(L-1)}.

Thus all these beta-scaled paths exist over the original interval. Their exact representation is Theta_beta(t)=beta Theta_1(beta^{L-1}t). Their raw propagators are bounded by 2^L exp(C_L) M^L. The adjacent gaps and far margin are at least h/10, so their reciprocals are at most

10J^{4L} M^{L-1} <= J^{5L} M^{L-1}.                     (J)

Consequently the nonnegative-beta-polynomial derivative argument supplies f'(beta)<=J^{5L}M^{L-1}f(beta_far), with an additional factor at most two on sufficiently fine meshes. There is no smallest-step dependence. Beta differentiation of the primitive source entries therefore adds power L-1 in M and a numerical factor at most 2J^{5L}.

### 7b. Explicit integrated forcing and primal factors

Let b(c)=sqrt(4(L-1)+c^2)+rho_L. At a raw state within rho_L of the reference, every primary norm is bounded by b(c). Telescoping the capped versus affine backward chains gives a discrepancy at layer ell bounded by

e L 2^L b(c)^{L+1-ell}.

Indeed each capped gate differs from multiplication by a by at most e in its operator bound, while each complete factor has bound a+e<=3/2. Telescoping the forward gates gives discrepancy at most 2e L b(c)^{ell-1}, because |arctan|<=pi/2 and the full matrix actions have norms at most b(c). The full forward norm is at most (2b(c))^ell. Products in a matrix gradient, and the endpoint gradients, therefore show that the sum of all raw vector-field discrepancies for the two samples is at most

F_L e b(c)^L, F_L=8(L+1)^2 4^L <= J^{2L}.              (K)

This deliberately overestimates the first projection factor, whose raw norm is at most one, and includes both sample contributions in the feature-time symmetric path. The estimate requires only a in [1/2,1], 0<=e<=1/2, and the cap property |tau_R(q)|<=|q|.

Before c=1 the elapsed time is at most one. Afterwards (A) gives dt/dc<=b_L c^{-L}. Since b(c)<=c+3sqrt(L),

integral_0^T b(c)^L dt
 <= (4sqrt(L))^L [1+b_L M]
 <= 2b_L(4sqrt(L))^L M <= J^{3L} M.                    (L)

Combining (K)--(L), lambda^{-1}<=M^{L+1}, the propagator exp(C_L)M^L, and conversion between Hilbert and sum norms, proves

E_raw <= exp(C_L)J^{6L} e M^{2L+2}.                    (M)

Taking the larger bound exp(C_L)J^{10L} also covers the enlarged family. Stop at E_raw=rho_L; the condition that the right side of (M) is at most rho_L/2 closes the stop. Each forward/backward field telescope costs at most J^{3L} beyond (M), giving numerical prefactor exp(C_L)J^{13L} for the powers already displayed in (F)--(G). The affine prediction telescope retains the factor lambda, exactly as in Section 4.

The original affine forward fields are bounded by

1+[3b_L/(2a^L)](2sqrt(L))^L <= J^{3L},

using inactive freezing and the original active factor r. Requiring the forward discrepancy to be at most one bounds the nonlinear fields by J^{4L}. The backward affine chain bound has numerical coefficient at most J^L. Forming the learned forward or backward moments, and then multiplying by S<=2M^{L+1} for a complete strict row, therefore yields all learned-moment bounds with a common numerical coefficient at most exp(C_L)J^{30L}. Their M powers are precisely (G).

### 7c. Explicit probe and normalization factors

With enlarged primary norms at most JM, any forcing or output probe cost has numerical coefficient at most J^{2L}; there are at most L chain summands, and L J^L<=J^{2L}. Pairing the two costs with the propagator 2^L exp(C_L)M^L costs at most exp(C_L)J^{5L}.

The original forward density scale contains r^2; its M-independent coefficient is at most [3b_L/(2a^L)]^2<=J^{4L}. The original backward row scale contains r^{-1}; its M-independent coefficient is 2a^L/(3b_L)<=1, and any remaining power of a costs at most 2^{2L}<=J^{2L}. Local resolvent similarities cancel exactly on the diagonal sample sectors. The inactive forward coefficient is bounded by L beta^{2L} and costs at most J^{2L}. Orthogonal sample-coordinate changes, direct identity terms, sums of the learned moment and derivative terms, and equivalence of the at most L+1 block norms together cost at most J^{3L}. Thus every source table entry before beta differentiation has numerical coefficient at most exp(C_L)J^{15L}. Adding the beta factor in (J) and the fixed factor two from sufficiently fine meshes gives at most exp(C_L)J^{21L}. This also covers the moment beta derivatives, because their finite affine Wick expansions are nonnegative and their undifferentiated bounds were already at most exp(C_L)J^{30L}; their differentiated coefficient is at most exp(C_L)J^{36L}.

No estimate in this bookkeeping multiplies two propagators. The same-state forcing, output telescopes, learned-moment comparison, source-probe estimate, and first beta derivative each contain the single propagator or a beta-polynomial derivative of a single bounded source entry. Later products of separate primitive bounds belong to the nonlinear source-closing argument and must be counted there.

### 7d. One explicit common prefactor

The preceding factors, the beta-gap reciprocal, rho_L^{-1}, original forward Gaussian bounds and backward Gaussian chain factors are all dominated by

H_L=exp(C_L+1000L^2 log(10L)).                            (N)

Indeed each displayed primitive product costs at most exp(C_L)J^{100L}, and 100L<=1000L^2 for every L>=3. This deliberately generous exponent also contains the explicit continuation and time-scale factors in (I)--(J). The preceding derivation, rather than an unspecified number of combinatorial factors, is the justification for (N).

Thus the arbitrary fixed-depth affine certificate has all powers (C), (F), (G), and the source table, with the single explicit prefactor (N). Its growth is log H_L=O(2^L sqrt((L-1)!) L log L). It does not itself prove a full all-depth activation amplitude: the source-closing powers of H_L and M are separate obligations.

Finally, the sharper numerical Section 3 calculation works for every 3<=L<=6, not merely L5/L6: the expression (D) increases with L, the displayed early integral is bounded by its L6 value, and all tail inequalities use only L<=6 and K_L<=16. The beta, forcing and probe estimates in Sections 4--5 use at most six layers. Therefore the unchanged original H may be used for all 3<=L<=6, while (N) is an explicit option for arbitrary fixed L.
