# Admission route: fixed nonatomic laws and effective, conservative certificates

Status: internally derived route, frozen before comparison with other routes. This is not a promotion or an independent review. No training run or scientific simulation was performed.

The assigned sources suffice to make a fixed nontrivial law family computably admitted in principle. The certificate below is deliberately conservative and is computationally unusable at its literal constants. A separate, local residual enclosure is much more useful as a specification for a future certified computation, but no such computation has been run here. Failure of the displayed bounds to certify accuracy is not a failure or impossibility theorem for the population solver.

## 1. Scope, coverage, and target

Read completely: `docs/global_nonlinear.md`, C.4.7, lines 8978–11440, and C.4.9 Proof unit A including A-supplement.4, lines 13184–13955; `docs/NOTATION.md`. Read the required solve-math-rigorously and investigate-conjectures skills and the latter's research-contract and adversarial-audit references. No other research study, other route, or other agent's findings was read. No additional scientific source was fetched. The established source construction and reference existence facts are used in exactly the forms restated in these assigned sections; III.F and the earlier C.4.5 source-regularization proof have not been independently re-audited here.

The target is the original physical gradient flow on [0,40], with two hidden tanh layers, unhalved squared loss, mobilities (n,1,n), and initial stored Gaussian variances (1,1/n,1/n²). Population initialization is (w,K,c)=(g,0,0), g~N(0,I₂). A=A₀+K retains A₀ and its actual adjoint; only K is Hilbert–Schmidt. The comparison distance used in proofs is

\[
d(\theta,\bar\theta)=\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}+\|c-\bar c\|_2.
\]

It bounds the required raw square-sum norm and is at most √3 times that norm. Data are z=(√2u,y), |u|=1, with distance |u-v|+|y-z|. Below Y=1 suffices for the concrete family; the scalar admission construction works for every fixed computable Y≥1.

Claims must be separated:

* A fixed finite source graph has computable Gaussian integrals, potentially at enormous cost.
* The scalar admission certificate gives a uniform source bound over all sufficiently fine graphs in a fixed law neighborhood. C.4.7 then supplies strong population completion, reached restart, and actual finite-GF identification.
* The finite-width identification is convergence in probability, not an effective finite-width accuracy guarantee. No width rate is supplied by these sources.
* Neither the source theorem nor its admission certificate is a source-compression theorem. Old forward and reverse source slots remain present.

## 2. An explicit raw comparison inequality

Let the compared states share A₀ and suppose

\[
\|A\|,\|\bar A\|\le A_b,\quad
\|c\|_2,\|\bar c\|_2\le C_b,\quad
\|\bar c\|_\infty\le H_b,\quad \|\bar w\|_2\le W_b,
\]

and both residual magnitudes are at most R_b. For a cutoff U≥1 put

\[
\begin{aligned}
G&=A_bC_b+C_b+1,&P&=\max(1,A_bC_b,C_b),\\
L_x(U)&=2H_bA_b^2+2H_bA_b+C_b+A_b+2U,\\
L_K&=2H_bA_b+C_b+2H_b+1,&L_c&=A_b+1,\\
L_g(U)&=\max\{L_x(U),L_K,L_c\},\\
a(U)&=2\{PG+R_bL_g(U)\},\\
b(U)&=2\{G(A_bC_bW_b+1)+R_b[W_bL_x(U)+A_bC_b]\}.
\end{aligned}                                                    \tag{1}
\]

For laws μ,ν coupled at mean data distance q,

\[
\|\mathcal F_\mu(\theta)-\mathcal F_\nu(\bar\theta)\|_{(1)}
\le a(U)d+b(U)q+4R_b\int\tau_U(\bar Q(v))\,d\nu(v,z).             \tag{2}
\]

Here and below \(\tau_U(Q)=\|Q1_{|Q|>U}\|_2\). These constants use only L² action bounds.

Proof: write x=||w−w̄||₂, k=||K−K̄||HS, z=||c−c̄||₂, e=|u−v|+|y−z_label|. The first feature difference is at most x+W_b e. The successive differences of Z², Δ², and Q are bounded by

\[
A_b(x+W_be)+k,\quad
z+2H_b[A_b(x+W_be)+k],\quad
A_b\{z+2H_b[A_b(x+W_be)+k]\}+C_bk.
\]

Subtract the first gradient block as a Q difference, a first-gate difference, and a final direction-vector difference. The gate difference costs
\(2U(x+W_be)+2\tau_U(\bar Q(v))\); the final vector costs A_bC_b e. The rank identity bounds the middle block by the Δ² difference plus C_b(x+W_be). The last block costs A_b(x+W_be)+k. Adding gives

\[
\|g_u(\theta)-g_v(\bar\theta)\|_{(1)}
\le L_g(U)d+[W_bL_x(U)+A_bC_b]e+2\tau_U(\bar Q(v)).
\]

The residual difference is at most Pd+(A_bC_bW_b+1)e, and ||g_u||≤G. Subtract r g into its residual and gradient differences, multiply by the physical loss factor two, and integrate the coupling. This proves (2), including its signs-independent tail bound and its absence of any action assumption on Lᵖ for p>2.

For a Gaussian-plus-bounded field Q=G₀+J, Var(G₀)≤σ² and |J|≤D, a completely explicit tail bound is

\[
\mathcal T_{\sigma,D}(U)=
\min\left\{\sigma+D,
2(3\sigma^4+D^4)^{1/4}
 \exp\left[-{(U-D)_+^2\over8\sigma^2}\right]\right\}.            \tag{3}
\]

Use σ>0; the σ=0 case has zero tail for U>D. To prove (3), the tail event implies |G₀|>U−D, use E(|G₀|+D)⁴≤8(3σ⁴+D⁴), Gaussian Chernoff probability ≤2exp(−(U−D)²/(2σ²)), and Cauchy–Schwarz. Take a square root after bounding the squared tail. No independence of J and G₀ is needed. The trivial L² bound supplies the other branch.

## 3. Removing the unspecified constants from admission

This section gives an effective sufficient condition, rather than calling the unnamed radius δ_Y computable. All scalar searches below terminate by an explicitly negative quadratic tail exponent. They are not proposed as an economical implementation.

### 3.1 Scalar anchor and a conservative bookkeeping bound

Set T=40 and use the actual displayed C.4.7 anchor constants:

\[
\begin{aligned}
C_0&=Y(e^{2T}-1),&R_0&=Y+C_0,\\
M&=10+2TR_0C_0,&W&=\sqrt2+2TR_0MC_0,\\
V&=2R_0(MC_0+C_0+1),\\
L_0&=100(1+M+C_0+R_0)^4,&E_0&=e^{L_0T},\\
P_0&=2(MC_0^2+2R_0MC_0+C_0^2+2R_0C_0+C_0+R_0),\\
K_0&=1+2C_0(M+1),&B_{\rm cl}&=2C_0+TP_0K_0E_0.
\end{aligned}                                                    \tag{4}
\]

These are N9, N38, N41, N43–N47, with a harmless operator upper bound 10 also for the population. Set

\[
H=10^6(1+T+Y+C_0+R_0+M+W+V+L_0+P_0+K_0+B_{\rm cl}),
\quad B_*=B_{\rm cl}+1,
\]
\[
b_*=\exp(\exp(H^{12})),\qquad
C_* =\exp(\exp(\exp(H^{16}))).                                \tag{5}
\]

For temporary caps at most B_cl+2, C_* is a valid simultaneous choice for the constants C_B in N24 and N51, on comparisons with maximum raw discrepancy at most one. Here is a bookkeeping proof so that (5) does not conceal an uncomputed continuity modulus.

1. Every elementary raw/action, residual, input-diameter, and time-mass bound is at most H. The D-row bound B+2R₀C₀²T is at most H⁴. N13 gives every normalized raw lower-pulse Lᵖ norm for 1≤p≤96 at most exp(H⁸): indeed its exponent is bounded by 18H⁶+768H⁶ and its prefactor by 4H. The accumulated random amplification has the same bound from N11. Marginal fields and row maxima in N18 are bounded by exp(H¹⁰), by their displayed finite sums and Minkowski. These estimates concern the named fields; no norm of a supremum of Gaussian history is used.

2. N14–N17 give f_B≤exp(2H⁸), d₀≤4H², and upper deterministic derivative-row and old-source-density bounds at most exp(exp(4H⁸)). All of them, all moments just listed, the deterministic normalized reference clock pulses N49, and polynomial factors in the raw-to-clock defect are less than b_*. For the latter, b₀ is Gaussian plus a bounded field with variance and bound at most a fixed power of H. Gaussian exponential moments control e^{2h|b₀|} for h≤1. N33–N36 then bound the summed normalized L² defect by b_*¹⁰ h_max, including division by the direct mass h_s p_b. This division leaves h_s, not 1/p_b.

3. In N22 every L² field difference has a coefficient at most H¹⁰. Interpolating its L² difference with the preceding L²⁴ bounds gives L¹² difference ≤b_*²(η+e_a)^{1/16}; if η+e_a≥1 use the absolute moment bound instead. Bounded gates obey the same weaker bound. A lower forcing term in N27 contains at most one difference, two unchanged L¹² factors, and the L⁴ random amplification. Its norm is therefore at most b_*⁶ times the displayed error. The six forcing types are: direct injection; update coefficient; input vectors; outer gates and Q; D-row difference; inner past gate and input. Mass sums and the finite number of summands enlarge this to b_*²⁰. The old D coefficients retain h_s p_b by N17, so transport costs average to q^{1/16}; there is no factor equal to the number of slots. Thus the right side of N27 can use b_*²⁰, and N28 and its F-row version can use b_*²⁶.

4. Sum the three equations N29 over their derivative indices, then average the active output index. Every unchanged upper derivative row is at most b_*, every F coefficient has density at most b_*h_s p_b, and every gate/field error is covered above. Each displayed product has fewer than five such factors; the preceding F-row forcing supplies the largest power. With G_k=(η+q)^{1/16}+∑_{j<k}h_jE_j, one obtains the conservative inequality
   \[
   L_k\le b_*^{30}G_k+b_*^{30}\sum_{j<k}h_jL_j.
   \]
   Since G_k is nondecreasing and T≤H<b_*, its solution is at most exp(b_*³²)G_k. Applying the same three equations once to a passive output gives E_k≤exp(b_*³³)G_k. Because exp(b_*³³)<C_*, this proves the claimed N24 constant.

5. For N51 the clock-pulse propagation is deterministic. Its integrating factor and its normalized barred pulse are bounded by b_*; item 2 bounds the total defect. The subtraction N48, including coefficient and gate differences, therefore gives b_*²⁰(η_h+h_max+∑h_jE_j) for each normalized pulse. The same upper calculation in item 4 proves N51 with C_*. All lower terms at the first potential failure involve old Q rows; the current α is constructed before the current β. No current cap has been assumed in deriving its bound.

This proof uses only the finite recursions and their stated scalar moment estimates. The powers in (5) are intentionally much larger than required. It does not quantify the fixed-width limit or any Gaussian quadrature cost.

### 3.2 An explicit reference raw mesh threshold

Evaluate (1) with A_b=M, C_b=H_b=C₀, W_b=W, R_b=R₀. Put D_cl=B_cl+2R₀C₀²T and

\[
\chi={1\over 2C_*e^{C_*T}}.                                    \tag{6}
\]

Choose an integer U_cl≥max(1,2D_cl) such that

\[
4TR_0 e^{a(U_{\rm cl})T}\mathcal T_{C_0,D_{\rm cl}}(U_{\rm cl})
\le\chi/4.                                                     \tag{7}
\]

One can enumerate integers and certify the strict version by interval bounds for exp; it terminates because a(U) is affine for all sufficiently large U and the tail exponent is a negative quadratic in U. Now take a positive rational h_* small enough that

\[
h_*\le\min\left\{1,\chi/4,
{\chi\over4[T e^{a(U_{\rm cl})T}a(U_{\rm cl})V+TL_0VE_0]}\right\}. \tag{8}
\]

To justify this choice, reference clock Euler has the global Lipschitz bound L₀ and speed at most V in the clock sum norm, so its distance to the reference clock flow is at most TL₀VE₀ h_max. The flow's passive reverse query has tail (3) with σ=C₀, D=D_cl. This tail passes from clock Euler without a rate: under the source isometry its Gaussian parts are Cauchy in L² whenever their upper backward inputs are, and the bounded remainders then converge in L² and retain their pointwise bound by an almost surely convergent subsequence.

Apply (2) to raw Euler and this existing reference flow. On an affine segment the state is at distance at most Vh_max from its preceding node, hence

\[
d(\theta_*^h(t),\theta_*(t))
\le Te^{a(U)T}\{a(U)Vh_{\max}+4R_0\mathcal T_{C_0,D_{\rm cl}}(U)\}.
\]

The 1-Lipschitz inverse clock map converts the clock error to raw error. Equations (7)–(8) make η_h+h_max≤χ. N51 with C_* therefore gives row discrepancy ≤1/2. Its causal first-failure argument proves the reference raw cap B_*=B_cl+1 for every mesh with h_max≤h_*.

### 3.3 An explicit law radius

Set D_*=B_*+2R₀C₀²T and

\[
\beta=\left({1\over 2C_*e^{C_*T}}\right)^{16}.                    \tag{9}
\]

Choose an integer U_*≥max(1,2D_*) satisfying

\[
4TR_0e^{a(U_*)T}\mathcal T_{C_0,D_*}(U_*)<\beta/4.                 \tag{10}
\]

Choose a positive rational ρ with

\[
\rho<\min\left\{1,\beta/4,
{\beta\over4Te^{a(U_*)T}b(U_*)}\right\}.                         \tag{11}
\]

For two raw programs on the same mesh, (2) and the reference raw cap give

\[
\eta\le Te^{a(U_*)T}\{b(U_*)q+4R_0\mathcal T_{C_0,D_*}(U_*)\}.
\]

If q≤ρ this is less than β/2; also η+q<β. The N24/N31 bound with C_* gives E_k≤C_*e^{C_*T}(η+q)^{1/16}<1/2. Atom splitting preserves the reference row cap by N20 and the source-mass normalization. The first-failure induction therefore supplies B_cl+2 uniformly for all finite laws with W₁ distance at most ρ and all sufficiently fine meshes.

Consequently any law satisfying

\[
\mathcal W_1(\mu,\nu_*)<\delta_{\rm adm}:=\rho/8                 \tag{12}
\]

has the C.4.7 strong population flow, source tails, reached restart, and actual finite-GF identification. The completion only uses finite-law approximants eventually inside ρ and the cap just proved. The smaller nested radii needed later in C.4.7 can be chosen, for example, ρ/4 and ρ/2; (12) lies strictly inside both.

All quantities in (4)–(12) have finite algorithms from Y and T. Finite rational interval certificates for the strict inequalities are checkable. Literal decimal expansion is unnecessary for the definition, but producing or evaluating the resulting tiny rational parameters may itself require astronomical resources. The claim is computable admission, not fast admission. In particular no theorem of existential continuity was used as a substitute for an effective modulus.

## 4. A fixed family with genuinely nonatomic correlated inputs

Fix once and for all a positive rational d<min(δ_adm/12,1/100). It is chosen from the admission certificate, before choosing a requested solver accuracy. Let a,b,p be rational numbers in

\[
d\le a\le2d,\qquad d\le b\le2d,\qquad \tfrac12-d\le p\le\tfrac12+d.
\]

Draw a branch J with probabilities p and 1−p and independently draw v uniformly from [−1,1]. Define

\[
\begin{array}{c|c|c}
J&u&y\\ \hline
1&(\cos(av),\sin(av))&1-b(1+v)/2\\
2&(-\sin(av),\cos(av))&-1+b(1+v)/2.
\end{array}                                                     \tag{13}
\]

The law of (√2u,y) is μ_{a,b,p}. Every member has a finite description by the three rational parameters and the fixed elementary sampling map. Both the input marginal and joint law are nonatomic: each arc map is injective on [−1,1], its uniform parameter has no atoms, and the two arcs are disjoint. The input coordinates are correlated through the arc constraint. The label is also nonconstant and correlated with the arc position since a,b>0. Thus this is not a pair of fixed input atoms with continuous labels added.

Within each branch, |u−e_J|≤a|v| and the expected label displacement from its reference label is b/2. Moving the branch masses to 1/2 costs at most 4|p−1/2| in the stated data metric. Hence

\[
\mathcal W_1(\mu_{a,b,p},\nu_*)
\le a/2+b/2+4|p-1/2|\le6d<\delta_{\rm adm}.                    \tag{14}
\]

The family stays fixed as accuracy is refined. In particular a,b≥d>0 always. This is a conservative existence family; its inputs will be indistinguishable from the reference axes at ordinary floating-point precision when d comes from the literal certificate.

For controlled quadrature divide [−1,1] into N equal cells, use their midpoints, and assign branch weights p/N and (1−p)/N. The map (13) is Lipschitz into the data metric with constant a+b/2. Since the expected displacement to a midpoint is 1/(2N), the resulting 2N-atom law λ_N satisfies

\[
\mathcal W_1(\lambda_N,\mu_{a,b,p})\le {a+b/2\over2N}.            \tag{15}
\]

This is an explicit generated law-integration error. It contains no trajectory information. The transport bound (2) or the uniform Gaussian-tail modulus below propagates it to raw-state and prediction errors. Fixed d is never replaced by a number tending to zero with N or with the requested accuracy.

Continuous parameter boxes for (13) can be considered mathematically; finite rational descriptions already provide an infinite fixed computational family. A supplied computable real parameter would need its own effective evaluation representation. Finite description does not mean a cheap bit representation for the literal value of d.

## 5. Stronger propagation and a local residual certificate

### 5.1 Preserve Gaussian tails instead of weakening them to exponential tails

C.4.7.NH weakens Gaussian tails to obtain a simple Hölder law modulus. For computation this loses useful information. Suppose a comparison has τ_U≤M_Q exp(−c_Q U²) for U≥U₀ and state error plus a constant perturbation budget is s≤1. Take

\[
U(s)=\max\{U_0,\sqrt{c_Q^{-1}\log(D/s)}\},\qquad D\ge\max(e,M_Q).
\]

Then the tail is at most s, and (2) gives, after including the fixed law and integrated-defect budgets in s,

\[
s'\le A_1s+B_1s\sqrt{\log(D/s)}                               \tag{16}
\]

with computable A₁,B₁ obtained from the constant and linear-in-U terms in (1). To accommodate an integrable defect ε(t), put s(t)=d(t)+q+∫₀ᵀε(v)dv; the integrated comparison is dominated by the scalar equation starting at this positive total budget. Equivalently one can keep ε(t) explicitly and solve a scalar supersolution. A differential statement (16) with an arbitrary unsmoothed ε(t) absorbed pointwise is not being claimed.

For the homogeneous scalar comparison set z=√log(D/s). While z≥1,

\[
z'\ge-{A_1+B_1z\over2z}\ge-(A_1+B_1)/2.
\]

Therefore, while the right side remains at least one,

\[
s(t)\le D\exp\left[-\left(\sqrt{\log(D/s(0))}
                   -(A_1+B_1)t/2\right)^2\right].              \tag{17}
\]

This is much better asymptotically than s(0)^{exp(−LT)}. It still need not give usable constants: U₀ may have to exceed the enormous bounded response remainder D_*.

### 5.2 A proved one-reference enclosure usable by a verified trajectory

Let a finite, explicitly described comparison curve θ̄(t) have the retained carrier and initialization, law ν, and a certified raw residual

\[
\epsilon(t)\ge\|\bar\theta'(t)-\mathcal F_\nu(\bar\theta(t))\|_{(1)}.
\]

Let the target law μ be admitted by (12). On each interval I_j of length ℓ_j certify bounds entering (1), a cutoff U_j, and a bound τ_j for the comparison query tail averaged under ν. It is enough to certify the supremum of the individual tails; more accurate weighted tail bounds are allowed. If q≥W₁(μ,ν), then the scalar recursion

\[
e_{j+1}=e^{a_j\ell_j}e_j+
 {e^{a_j\ell_j}-1\over a_j}
   (b_jq+4R_{b,j}\tau_j+\epsilon_j)                              \tag{18}
\]

is a rigorous raw sum-error enclosure when ε(t)≤ε_j on I_j; use ℓ_j for the fraction if a_j=0. This follows by subtracting the integral equations, using (2), and multiplying the scalar inequality by e^{−a_jt}. Within the interval use the same formula with its partial length. Prediction error is at most P_j e(t). This is an effective finite certificate if its bounds are supplied by rigorous finite-graph calculations, and it is causal once each interval has been certified. It does not use the unknown target trajectory to select coefficients.

For a raw Euler comparison graph, its node controls can be rational values computed from approximate residuals. This defines an exact ideal finite graph using A₀ and A₀*. The difference between the assigned velocity and the exact recomputed node velocity is part of ε_j. The additional affine-segment defect can be bounded by (2) with q=0, node tail bounds, and d≤V_jh_j. Thus the residual certificate need not assume exact numerical integration of a time-continuous function. Numerical evaluation errors of graph contractions and covariance/source answers also have to be included; they are not absorbed merely by reducing the time step.

Energy gives much smaller *existing-path* bounds than (4):

\[
\|c(t)\|_2\le Y\sqrt t,\quad \|K(t)\|_{\rm HS}\le Y\sqrt t,
\quad \|w(t)\|_2\le\sqrt2+Y\sqrt t,
\quad\|c(t)\|_\infty\le2Yt.                                   \tag{19}
\]

These can be used in (18), together with separately certified comparison-curve bounds. They cannot be assumed for arbitrary Euler programs before a certificate or source bootstrap. At finite width the analogous initialized energy event gives enlarged bounds, but the finite-program probability error still needs a width limit and has no effective rate here.

There is also a residual-weighted improvement. In the state part of the coupling proof use the reference residual for the gradient-difference term. If m(t)=∫|r̄|dν, replace the state coefficient by 2PG+2m(t)L_g(U) and the tail term by 4∫|r̄|τ_U(Q̄)dν. The law-transport part still uses a pointwise residual bound unless its weighted transport cost is separately certified. Thus accumulated force reduces part of propagation; it does not eliminate the physical-time term 2PG from this norm estimate.

No enclosure (18) was evaluated on a trajectory. In particular this report does not certify raw or prediction error 0.02 or 0.1 for an implemented solver.

## 6. What accumulated force improves, and what it does not admit

Proof unit A bounds controlled programs by the reference total force L_*≤10 instead of the physical-time bound e^{80}. If the prescribed control discrepancy satisfies CT4 with q≤1, CT26 gives

\[
\|c\|_\infty\le11,\qquad \|K\|_{\rm HS}\le60.5,
\qquad\|A\|\le62.5.
\]

This is a major improvement in propagation constants. But CT4 is a statement about the total variation of signed control measures, not Wasserstein closeness of data laws. For the nonatomic arc family the input support has zero mass on the two reference axes. Its feedback control measure is therefore mutually singular with the two atomic reference controls in input space. At each time their total variation discrepancy is the sum of their absolute masses. Integrated over time it is at least the reference training force on that interval, independently of how narrow the arcs are. Consequently CT4 cannot by itself admit (13) merely by taking a small angle. For finite quadratures, padding the reference axes by zero-control extra directions has the same problem. A weighted geometric transport argument such as C.4.7.N20–N31 is necessary.

CT4 also concerns prescribed deterministic controls, whereas the GF coefficients are −2p_j(f_j−y_j). Checking their *future* integrated discrepancy by reading a yet-unknown solution is not an a priori certificate. One may validate a causal enclosure for this discrepancy alongside a computed path, but that is additional work. Retaining the complete source history is mandatory at every such step or restart.

For a useful scale comparison derive a feature-clock Lipschitz constant directly. Put h=10 and A=2+h²/2=52. Use x=∑||ΔX_a||₂, k=||ΔK||HS, z=||Δc||₂. The feature-clock subtraction CT18–CT20 gives

\[
V_Z\le Ax+2k,\quad D_\Delta\le2z+2hV_Z,
\quad P_Q\le AD_\Delta+2hk.
\]

The sum of the three velocity differences is at most (P_Q+D_Δ+hx+V_Z)/2. Thus

\[
L_{\rm cl}=\max\{hA(A+1)+(h+A)/2,\ h(2A+3)+1,\ A+1\}=27591.    \tag{20}
\]

This is a bounded-set comparison of the population clock equations; using a finite initialized operator event ||A₀,n||≤3 replaces A=52 by 53. A forward source pulse immediately changes the sum norm by at most [2h(A+1)+1]|γ_p| times the pulse RMS, and a later passive Δ² difference is at most [1+2h(A+1)] times that sum norm. Hence the same fresh-root source extraction yields a cap bounded by

\[
2h+h[2h(A+1)+1]^2e^{hL_{\rm cl}}.                              \tag{21}
\]

The strict finite operator event may use A=53 and the larger constant. This avoids relying on probability tending to one for a sharp norm bound of exactly two.

Even the smaller population value gives log₁₀(e^{hL_cl})≈119826.19. Source-transfer constants then increase it substantially. It is not correct to infer from force length 10 alone that the proof is numerically well conditioned.

The raw GF gradient structure might allow a better one-sided or observable estimate: the J*J part of its Hessian is dissipative. The remaining residual-weighted second-derivative terms contain an unbounded lower Q multiplier. The supplied sources do not bound that Hessian on an arbitrary raw L² ball. Positive semidefiniteness of the instantaneous prediction kernel therefore does not establish contraction between two nonlinear raw trajectories or control the change of that kernel. Such a sharper estimate is an open improvement here, not an assumed property.

## 7. Gaussian integration and generated-error accounting

At a fixed graph, finite-dimensional Gaussian integration is computable without assuming a fast high-dimensional integrator:

1. Keep every named source. Its covariance entries and all scalar contractions are finite expectations constructed chronologically. Tanh and its derivatives are computable bounded functions; each raw graph field and named derivative has a computable polynomial envelope in its finite Gaussian list, with coefficients inherited from earlier certified scalar operations. The actual adjoint/source contractions must be retained.
2. Truncate a finite standard Gaussian list to a box [−R,R]^m. Gaussian even moments and Cauchy–Schwarz give an explicit tail error for each polynomially bounded integrand. The finite union bound over coordinates is sufficient. On the box, derivatives of the finite expression give an explicit Lipschitz constant. A uniform box grid then has a proved Riemann/cubature error tending to zero. This may be exponential in m.
3. Singular covariances do not require a pseudoinverse. A nonnegative square root can be computed by uniformly approximating √x on [0,M] by polynomials and applying that polynomial to the covariance matrix. For example the degree-n Bernstein polynomial has error at most √M(4n)^{-1/4}: write it as E√(M K/n), use |√a−√b|≤√|a−b|, Jensen, and Var(K/n)=x(1−x)/n. Orthogonal diagonalization used for this proof transfers the scalar uniform bound to operator norm. For approximate covariance entries first use a small positive diagonal padding to ensure positive semidefiniteness, and bound the polynomial's perturbation by its explicit finite coefficients. Choose polynomial degree and entry precision successively. No spectral-gap assumption is made.
4. Such square-root approximation gives a common Gaussian coupling and therefore a certified input error for the finite expression. On the truncated box its Lipschitz bound propagates that error; the polynomial envelope controls the complement. Recursive refinement of preceding expectation intervals terminates at every *fixed* finite graph and fixed requested error.

This is an elementary computability argument and an expensive fallback algorithm. It is not a claimed implemented library. It does not prove an economical complexity bound as the graph grows. Covariance rank loss slows these generic bounds rather than invalidating them.

The generated errors that have separate obligations are:

| Source | Bound available here | Remaining work for an implementation |
|---|---|---|
| Input/label law quadrature | Equation (15) | Choose N through a propagated tolerance, not merely a geometric tolerance |
| Time approximation | Node residual plus the affine-segment version of (2) | Certified residuals and a temporal mesh |
| Gaussian integration | Fixed-graph box/grid construction above | Evaluate it, or prove a cheaper replacement with certified error |
| Covariance/source evaluation | Fixed finite recursion with padded PSD square root and explicit error propagation | Track all old slots and errors at singular rank |
| Source/history compression | No small-source estimate supplied | Prove collective discarded residual small, including adjoint and nonlinear feedback |
| Floating point and scalar coefficient errors | Can be inserted into the residual/error intervals | Actual interval implementation and resource estimate |
| Finite width | C.4.7 convergence in probability | A quantitative rate if a concrete finite width is to be certified |

A stable propagator without these generated-error bounds does not certify a solver. Conversely a tiny generated quadrature error before applying (18) is not necessarily a tiny final error.

Already at initialization the readout is zero, so the first raw Euler step changes c while w and K stay fixed. At the next nonzero backward call, c depends on the earlier forward Gaussian sources; the reverse answer includes its named response terms. Duplicate forward covariances do not identify formal source names. Once the lower features move, further sources can be required. Thus inexpensive input quadrature does not remove the causal Gaussian-integration problem near the beginning of training. With m input atoms and k steps, the unreduced source lists have order mk entries in each orientation, and covariance storage is quadratic in that count. Their rank or compressibility cannot be inferred from a small data angle or from small *individual* coefficients.

## 8. Scalar arithmetic and practical interpretation

Only the following bounded scalar arithmetic was performed, using ordinary double precision for rough size diagnostics, not for rigorous certificate generation:

\[
\begin{array}{c|c}
\text{quantity, Y=1 and T=40}&\text{value}\\\hline
C_0&e^{80}-1\approx5.5406223844\cdot10^{34}\\
M&2.4558797125\cdot10^{71}\\
L_0&3.6377124467\cdot10^{287}\\
\log_{10}E_0&6.3193537695\cdot10^{288}\\
\log_{10}\log_{10}E_0&288.8006726687\\
L_{\rm cl}\text{ from (20), A=52}&27591\\
\log_{10}e^{10L_{\rm cl}}&119826.1905\\
L_{\rm cl}\text{ with finite-event A=53}&28651.5\\
\log_{10}e^{10L_{\rm cl}}\text{ with A=53}&124431.8835.
\end{array}
\]

The arithmetic evaluated (4), (20), and logarithms of the amplification factors; no exp(L₀T) was materialized. Reproducing these figures needs only exp(80), multiplication, and logarithms. The admission construction itself uses exact inequalities/rigorous scalar intervals, not these rounded figures.

Even before later source and bootstrap factors, a source budget δ forced by E₀δ≤0.1 needs approximately 6.3×10²⁸⁸ decimal places of absolute smallness. Replacing 0.1 by 0.02 changes this count only by log₁₀5. Feature-force bounds are vastly better, but the elementary feature-clock factor alone can require more than 119,000 decimal places before source-transfer losses. The 1/16 transport exponent and later exponentials further degrade the literal admission radius. These facts defeat a claim of feasible accuracy *from these bounds*. They do not show that the actual flow, its observable propagator, or an appropriately enriched solver has this amplification.

The strongest conclusion of this route is therefore: a fixed, finitely described and genuinely nonatomic correlated family can be admitted by explicit terminating scalar inequalities, and its input quadrature has an explicit error rate. The established worst-case construction does not certify practical accuracy 0.02 or 0.1 on [0,40]. Equation (18) is a proved alternative certificate that could exploit actual computed tails, row bounds, residuals, and energy/force bounds, but its successful evaluation and the cost of producing its finite-graph source integrals remain unperformed dependencies.
