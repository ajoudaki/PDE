# PDE population gradient-flow supervisor handoff

## Authority and destination

The user explicitly requested a NEW supervisor thread in the saved PDE project on black-chatgpt, taking over the mathematical task below. The calling/source thread and all its subagents must remain paused. This is a new-thread continuation, not migration of the source thread or its Git checkout. Do not restart or assign work to the old agents.

Source thread: 01a07114-b2fd-78b0-bb18-fa4c15cff3d6, title `L=2 arctan, two inputs`, host remote-ssh-discovered:black-chatgpt-2, cwd /home/amir/Codes/PDE. OS hostname reported ubuntu22-black; this is not evidence that the destination shares /tmp.

Destination saved project: PDE, projectId 007000cb-1ba5-4542-8db7-636948d2ba2d, host remote-ssh-discovered:black-chatgpt, saved path /home/amir/Codes/PDE, isGitRepository true. A new isolated worktree is the default. Do not move unrelated threads, change origins, reset/check out branches, or edit existing user work.

The source agents were interrupted on the user's request: /root/three_input_limit, /root/three_input_activity, /root/two_input_full_audit_b. The first and third were developing drafts; their most recent reasoning is recorded below. The activity agent had completed its note. No new broad theorem has yet been delivered to the user.

## Current user task

User's exact mathematical request immediately before the handoff:

"can you generalize the non-local GF population limit result to a wide class (as wide as possible from the current arctan case) ? by non-local I mean the T* > 0 absolute constant existence (only depends on activation and other scaling parameters, not width or the learning rate that are taken limit against, so it's not vanishing int he limit) , but not necessarily the 'any arbitrary constant T'"

Interpretation: prove the widest justified extension of the two-hidden-layer arctan joint width/gradient-flow theorem, on some fixed positive physical-time interval. In mathematical terminology this is local-in-time existence with a width/step-independent horizon, NOT a theorem on all finite horizons. Keep genuinely nonlinear feature learning where justified. Investigate wider activations, fixed dataset size, initialization, losses, and possibly arbitrary fixed depth. Do not claim a maximum class or an extension without a complete proof. The user values deep substance, rigorous independent/adversarial checking, and a clean self-contained final explanation.

## Source artifacts (verify availability before doing mathematics)

- /tmp/THREE_INPUT_LOCAL_LIMIT_PROOF.md : complete prior baseline, 661 lines, two hidden arctan layers, three inputs, Gaussian input/middle init, zero limiting readout; local joint convergence for every eta_n -> 0. Includes exact finite updates, common operator realization, mesh-uniform Gaussian response lemma, localized stability, oracle bridge, activity proof. Prior reviews passed, but still audit any reused claims.
- /tmp/THREE_INPUT_LOCAL_LIMIT_REVIEW.md : prior review record.
- /tmp/THREE_INPUT_SCALED_LIMIT_EXTENSION_CHECK.md : positive sigma/kappa constants, any polynomially vanishing Gaussian readout; includes a bounded nonzero readout local-existence extension but not its strict-activity proof.
- /tmp/three_input_activity_lemma.md : previous arctan activity calculations, including positive constants.
- /tmp/GENERAL_ACTIVATION_ACTIVITY.md : completed current-turn strict-activity extension. IMPORTANT: claims are conditional on existence of an appropriate strong mean-square flow.
- /tmp/GENERAL_DEPTH_LIMIT_CHECK.md : in-progress current-turn depth proof. It existed at interruption (11548 bytes), but may predate the final unbounded-activation reasoning below. Treat as draft, not audited theorem.
- /tmp/L2_FULL_AUDITED_PROOF.md : older single-input all-finite-horizons arctan proof, useful historical reference; not the current general dataset proof.

The proposed /tmp/GENERAL_ACTIVATION_TWO_HIDDEN_LIMIT.md did NOT exist when work was paused. The interrupted existence agent's reasoning is preserved below instead. Do not assume any missing file was completed.

Read only these explicit paths initially, not a recursive search of /tmp. If files do not exist on the destination, ask the source thread to transmit them; don't infer that identical paths on two hosts denote the same files. The app read_thread can inspect source history on its host. The source remains available for handoff logistics, not renewed research.

## Notation and exposition constraints

Use k for discrete step, ell for layer, a,b for input indices, i,j for neurons. Keep W^(ell), z^(ell), h^(ell)=phi^(ell)(z^(ell)) with layer superscripts EVERYWHERE. Finite vectors lowercase z,h; population coordinates uppercase Z,H. If activations differ by layer, phi^(ell) is acceptable and define it. Write phi' explicitly, never an extra q alias. W^(3) always means the STORED RESCALED readout in the two-hidden-layer model, with f=(W^(3))^T h^(2)/n. Never introduce raw readout or barred weights. Finite transpose is top, population adjoint is *. Write explicit b^T c/n and ||b||_2/sqrt(n), not custom normalized norms. Delta backprop fields are n*partial f/partial z and do NOT include loss residual. Keep factors 2, n, eta, loss weights visible.

The user dislikes excessive sections, generic aliases, jargon, boxed equations, and unexplained functional analysis. Use concrete network operations first, then general statements. Explain difficult ideas with elementary linear algebra/probability; do not pretend finite neuron coordinates are iid after matrix reuse. Separate the two neuron populations, oracle-supplied deterministic coefficients, empirical convergence, and subsequent feedback stability. This is not a CLT. Finitely many fields/operators do not mean finitely many scalar degrees of freedom.

Use solve-math-rigorously skill for new proof and teach-technical-math for source-based exposition; read the skill files on the destination before task actions. No goal was created in the source. The user previously requested isolated adversarial proof reviews until clean; use genuinely independent reviewers on a written proof, repair gaps, and avoid claiming such a review occurred if it did not.

## Baseline model and established scope

Two hidden layers, fixed inputs x_a in R^d, normalized ||x_a||^2/d=1, G_ab=x_a^T x_b/d. W1 n by d, W2 n by n, W3 n-vector. z1_a=W1 x_a/sqrt(d), h1_a=phi1(z1_a), z2_a=W2 h1_a, h2_a=phi2(z2_a), f_a=W3^T h2_a/n. Previously L=sum_a(f_a-y_a)^2 with three sign labels.

delta2_a=W3*phi2'(z2_a), delta1_a=phi1'(z1_a)*(W2)^T delta2_a, coordinate products. Stored-weight GD rates eta_n*(n*kappa1,kappa2,n*kappa3). Thus z1_a+=z1_a-2 eta kappa1 sum_b G_ab r_b delta1_b; W2+=W2-(2 eta kappa2/n)sum_b r_b delta2_b h1_b^T; W3+=W3-2 eta kappa3 sum_b r_b h2_b. Physical time t=k eta_n. Prior LOCAL theorem permits every eta_n -> 0, unlike older all-horizon proof's sufficient eta_n sqrt(n)->0 condition.

Initial W1 entries N(0,sigma1^2), W2 entries N(0,sigma2^2/n), W3 entries N(0,sigma3^2 n^(-2 beta)), beta>0, or zero. Positive finite sigma1,sigma2,kappas; sigma3>=0. The population readout is zero. Matrix action W2 and its adjoint are retained. Current population state consists of input preactivation fields and weight action/readout; it is autonomous, but infinite scalar-dimensional.

The general dataset proposal uses L=sum_a omega_a r_a^2 with omega_a>0 and sum omega_a=1, explicitly declaring this change from summed loss. Every training sum acquires omega_b. It may allow a common existence time independent of the number of inputs and angles, under input/label bounds. Need prove weighted sensitivity norms, not merely assert independence of dataset size. For summed loss the horizon may depend on the count via time rescaling. Inputs remain FIXED as n -> infinity; a uniform horizon is not uniform convergence for datasets growing with n.

Existence does not require nonparallelity or nonzero labels. Strict activity has stronger conditions. Prior result: on a smaller fixed interval each hidden RMS speed is positive and proportional to t, hidden displacement proportional to t^2, middle matrix action moves, kernel changes, loss slope initially strictly negative, and best-affine-fit activation errors stay positive. Hidden initial speed is zero because readout starts at zero. Do not claim speeds constant in time or all examples' residual magnitudes decrease.

## Proof mechanics already available

For fixed coarse Euler mesh Delta, expand W2 as initial Gaussian matrix plus a finite sum of trained rank-one terms. Freeze population residuals/contractions in the finite oracle. The finite tensor-program/Gaussian conditioning theorem yields joint empirical averages for the fixed computation. Use a common bounded initial operator realization on the two coordinate spaces.

Two-layer Gaussian response coordinates (sums run across inputs and previous times):

Z2_{a,k}=xi_{a,k}+sum_{b,s<k} B_{ak,bs} delta2_{b,s},
P_{a,k}:=(W2_k)^*delta2_{a,k}=eta_{a,k}+sum_{b,s<=k} D_{ak,bs} H1_{b,s}.

Here Cov xi = sigma2^2 E(H1 H1); Cov eta = sigma2^2 E(delta2 delta2). C_{ak,bs}=E[partial H1_{a,k}/partial eta_{b,s}], A_{ak,bs}=E[partial delta2_{a,k}/partial xi_{b,s}]. B=sigma2^2 C - 2 kappa2 Delta omega_b r_{b,s} E(H1_{b,s}H1_{a,k}); D=sigma2^2 A - 1_{s<k}2 kappa2 Delta omega_b r_{b,s} E(delta2_{b,s}delta2_{a,k}). All scalar coefficients are held fixed when differentiating these recursions. Both initial Gaussian response sums acquire sigma2^2, but learned terms acquire kappa2, not sigma2^2.

Previous bounded-activation proof controls row sums of A,C and bounded readout, giving P=Gaussian+bounded response uniformly in Delta. Split the potentially bad product [phi'(Z)-phi'(Zref)] Pref at |Pref|=R. This yields Lipschitz factor C(1+R) plus a tail e^(-cR^2). Gronwall gives exp(C(1+R)T)*[(1+R)(eta_n+Delta)+initialerror+e^(-cR^2)+fixedmesh o_P(1)]. Fix R,Delta then n->infinity, Delta->0, finally R->infinity. This proves existence, uniqueness, and joint convergence, not just formal equations.

## NEW wider-existence route, NOT YET FINALIZED OR ADVERSARIALLY AUDITED

The root and existence agent derived a promising extension to BOTH activations globally Lipschitz C2 with bounded first and second derivatives, allowing unbounded activations such as softplus/GELU/SiLU, and a nonvanishing SUBGAUSSIAN initial readout (including the standard Gaussian muP readout). The depth agent also reported that the analogous fixed-depth bounds appear to close. These are working deductions; the supervisor must write, verify, and audit the complete proof before announcing them.

1. Establish a short-time ball for all parameter/field RMS norms and matrix operator norms using their polynomial finite-GD/Euler growth inequalities. Only RMS, not max-coordinate readout bounds, are needed. At fixed depth, bounded activation derivatives give backward RMS bounds by products of operator norms. This supplies bounded innovation variances before response estimates.

2. Strengthen forward response control from total row sums to ENTRYWISE |C_{ak,bs}| <= C_* Delta omega_b. A derivative with respect to one backward slot starts as a pulse of size Delta omega_b. A discrete Gronwall estimate for its later propagation gives this bound after taking expectations. Controlling only the row sum risks an invalid max-over-time Gaussian bound as the mesh gets fine.

3. For two layers, this yields |B_{ak,bs}|<=B_* Delta omega_b. Let V_k denote the sum of absolute derivatives of current Z2 with respect to all forward Gaussian slots, maximized over inputs/history in the appropriate pathwise manner. The readout derivative is bounded by C Delta sum_{s<k}V_s, and the delta2 derivative by C Delta sum_{s<k}V_s+C|W3_k|V_k. Hence
V_k <= 1+C Delta sum_{s<k}(1+|W3_s|)V_s,
V_k <= exp(CT+C Delta sum_{s<k}|W3_s|).
Weighted/time Jensen controls its moments from MARGINAL subGaussian bounds; no independence across time is assumed. A row sums are then bounded via Cauchy-Schwarz: A_row <= C(T+||W3_k||_2)*||V||_2 (with suitable history maxima outside expectations).

4. Use N(U)=sup_{p>=2}||U||_p/sqrt(p), a triangle norm equivalent to a subGaussian bound (noncentered allowed). Under response caps and preliminary RMS bounds, two-layer inequalities have the schematic form
N(H1)<=K+CT N(P1),
N(P1)<=K+(sigma2^2 A_*+CT)N(H1),
N(H2)<=K+CT(C_*+K)N(W3),
N(W3)<=K_init+CT N(H2).
Small T closes each pair. Gaussian initialization gives finite root constants. With nonzero Gaussian readout, A_* is O(1), not O(T). For zero readout the old smaller onset is recovered.

5. Stability does NOT need a bounded readout: localize both reference W3 and reference P1. Specifically delta2 difference <= C||W3-W3ref||_2+CR||Z2-Z2ref||_2+C tail_R(W3ref). The subsequent backward recursion multiplies by bounded operator norms, not by another R. First-layer derivative multiplication adds another C R*d plus tail_R(P1ref). Thus the total loss in the comparison is O(R), not O(R^2). This is crucial: exp(CRT)e^(-cR^2) ->0. Actual GD needs only the preliminary RMS/operator bounds; reference oracle supplies the tails. Recheck proxy interpolation/recomputed backprop carefully with these extra cutoffs.

6. C^{1,1} activation extension is a ROOT PROPOSAL, not yet checked: if phi is C1 with globally Lipschitz derivative and bounded first derivative, smooth mollifications satisfy uniform bounds and converge uniformly in phi and phi' (errors O(epsilon)), while second derivatives are uniformly bounded. If the constants above depend only on these bounds, the same stability argument can pass epsilon->0 and construct the same flow. This would include smooth activations broadly but NOT ReLU itself, whose derivative jumps. Do not assert ReLU/GELU are covered together: GELU is smooth with bounded first/second derivatives; ReLU needs a new argument.

7. Root also considered arbitrary finite-second-moment first-weight roots for BOTH BOUNDED activations using truncation and uniform tail bounds independent of root cutoff. This was NOT completed and is lower priority than the Gaussian/subGaussian broad activation theorem. Non-Gaussian middle weights also need a checked finite-program universality theorem plus operator concentration; do not assert automatically.

## Fixed-depth extension checkpoint (agent interrupted while writing)

For L hidden layers (rename readout W^(L+1)), independent Gaussian middle matrices, globally Lipschitz C2 activations with bounded first/second derivatives, and subGaussian input/readout roots, the draft route is:

- For each initial middle matrix, its forward response is in historical delta_l fields and its backward response is in historical H_{l-1} fields. Establish |C_l(k;s)|<=c_l Delta omega_b and row A_l<=a_l.
- Under caps and the prior RMS ball, all Gaussian innovation variances <=K. For each internal layer j,
N(H_j)<=K+K f_j T N(P_j),
N(P_j)<=K+K(a_{j+1}+T)N(H_j),
where f_j depends on c_j plus bounded learned-memory coefficients. Close for T f_j(1+a_{j+1}) small. First-layer/root and final-layer/readout pairs are similar.
- Differentiate the local causal recursions. Entrywise C_l bounds propagate bottom-up from c_{l-1}; A_l bounds propagate top-down from a_{l+1}. They obey schematic bounds
c_2<=K exp(KT(1+a_2)+K T^2 *tailconstant),
c_l<=K(c_{l-1}+K) exp(K(c_{l-1}+K)T(1+a_l)+K(c_{l-1}+K)^2 T^2*(1+a_l)^2),
a_L<=K(B0+1)exp(K(c_L+K)T(B0+1)+tailterm),
a_j<=K(1+a_{j+1})exp(K(c_j+K)T(1+a_{j+1})+K(c_j+K)^2 T^2*(1+a_{j+1})^2).
The exact factors/indexing need verification against the draft. Choose c_l caps bottom-up and a_l caps top-down using the T=0 right-hand sides, then choose T small so every exponential <=2. At T=0 the opposing-direction caps drop out, avoiding circular choice of constants.
- Downward stability for delta_l sums cutoff errors from reference P_l. It should be O(C_L R)d, not R^L*d: each recursive backward step multiplies by bounded phi' and bounded matrix operator norms; only a new additive cutoff term arises. Verify this rather than assume.

The depth agent's latest message: the unbounded globally-Lipschitz extension appears to close, with exponent containing K f_j^2 T^2(1+a_{j+1})^2. This still tends to zero as T->0 after caps are fixed. It explicitly did NOT cover ReLU. The document may not yet include this update.

## Completed wider strict-activity argument

See GENERAL_ACTIVATION_ACTIVITY.md. Conditional on the required strong mean-square flow, both bounded nonconstant C1 activations with bounded derivatives suffice for arbitrary fixed finite pairwise nonparallel normalized inputs and nonzero real labels. No oddness, analyticity, strict monotonicity, or everywhere-positive derivative is required.

Key proof: for unit nonparallel directions u_a, a relation sum c_a phi(u_a dot w)=0 everywhere forces all c_a=0 for bounded nonconstant continuous phi. Isolate term a by commuting finite differences in directions v_ab=(u_a-rho_ab u_b)/(1-rho_ab^2), so u_a dot v_ab=1 and u_b dot v_ab=0. Applying the m-1 differences kills all other terms and gives Delta_h^(m-1)phi(s)=0 for every s,h. The bounded sequence phi(s+jh) with vanishing finite difference must be constant; contradiction. For unbounded phi with bounded nonconstant continuous derivative, first differentiate the ridge relation in a direction nonorthogonal to every u_a and apply the bounded lemma to phi'. Thus any globally Lipschitz nonaffine C1 first activation has positive definite initial feature Gram Q.

Second Gaussian root Y has covariance sigma2^2 Q and full support. Set S=sum y_a phi2(Y_a), U_a=S phi2'(Y_a) (replace y by omega*y for weighted loss). From S*sum c_a phi2'(Y_a)=0 everywhere: where S!=0 secondfactorzero; where S=0 either grad S!=0 and approximate from S!=0, or all phi2'=0 and it is alreadyzero. Thus sum c_a phi2'(Y_a)=0 everywhere. Nonconstant derivative implies all c=0, so V=E UU^T is positive definite even if derivatives vanish on intervals. Conditional transpose noise has covariance sigma2^2 V, independent of first roots. This yields positive first-layer backprop Gram D even with phi1' zeros. The next reused forward call has independent fresh Gaussian variance from the unexplored input direction, proving each second-layer leading motion nonzero.

The completed note covers kappa/sigma factors, middle-matrix action on each fixed initial input, nonconstant kernel, strict loss slope, and positive best-affine-fit errors. Its extension to both UNBOUNDED nonaffine activations with bounded continuous derivatives is a positivity result conditional on existence, not a separate existence proof. Strict activity for arbitrary DEPTH has NOT been established; don't infer it from local existence.

## Literature and novelty safeguards already communicated

Do not claim new muP width powers, a newly discovered feature-learning phenomenon, or a new operator-state representation. Relative stored GD powers (n,1,n) are muP's; common eta_n only refines the physical clock. Tiny/zero readout is a known variant, not forced by joint GF/MF.

- Tensor Programs III, https://arxiv.org/pdf/2009.10685 : fixed-program Gaussian response theorem, Box1/Remarks2.11-2.12/Theorem2.10. Local source /tmp/tp3src/NetsorT2.tex if available.
- Tensor Programs IV, https://arxiv.org/pdf/2011.14522 : Section2 explicitly separates discrete width limit from continuous-time existence/uniqueness; fixed training steps, not O(T/eta_n) uniformly.
- Tensor Programs IVb, https://arxiv.org/pdf/2308.01814 : Definition2.6.7, Props2.6.8-2.6.9 and footnote24 already give common L2 operator/adjoint realization; Theorem2.7.1 closed current-state updates for deep muP. Remark2.7.5 strict maximality includes maximal readout initialization; Remark2.8.21 allows limits suppressing init/LRs. 'Uniformized' in Section4.6 means instruction normalization, not uniform growing-time control.
- Tensor Programs V, https://arxiv.org/pdf/2203.03466 : Table8 exact stored parameter SGD scaling; zero-init paragraph immediately after Tables8-9; AppendixD.2 zero readout.
- Bordelon/Pehlevan https://arxiv.org/abs/2205.09653 : continuous-time muP-equivalent DMFT exists in prior work, with heuristic steps; not the joint rigorous theorem we seek.
- Chizat/Colombo/Fernandez-Real/Figalli https://onlinelibrary.wiley.com/doi/full/10.1002/cpa.22200 : rigorous deep LINEAR muP limit and subsequent continuous time, autonomous gradient structure. Do not pretend this research direction started here.

The previous final answer explicitly said our specific theorem's literature-first status has NOT been established. New broad proofs, if successful, still require a careful novelty review before making publication-level priority claims.

## Recommended continuation

First verify destination host/project and availability/identity of these artifacts. Then, after the source's resume message, construct one complete theorem and proof with exact assumptions and quantitative local-time dependence. Prioritize the broad Gaussian-init, globally Lipschitz smooth-activation joint limit; arbitary fixed depth only if the full response recurrences and weighted constants check. Separate existence, joint convergence, and strict feature activity. Send the written proof to independent adversarial reviewers, repair every substantive gap, and only then explain the result to the user in canonical notation. If an extension fails, deliver the strongest certified subclass and name the specific obstruction. Do not resume work in the source thread or old subagents.
