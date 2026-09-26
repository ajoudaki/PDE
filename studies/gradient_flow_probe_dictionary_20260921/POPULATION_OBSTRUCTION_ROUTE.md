# Population limit of the derivative-factor hierarchy: obstruction route

This scoped independent attempt does **not** prove a counterexample for the actual Gaussian initialization. It proves that the nested derivative hierarchy has a definite projected nonlinear limit, and gives a precise initial-kernel condition that would disprove identification of that limit with dense population training. The usual parity, finite-order mismatch, and Taylor-series arguments do not establish that condition.

Scientific input was restricted to the assigned DERIVATION.md, FACTORIZATION.md, ORDER_COUNTS.md, P45_DERIVATION_ROUTE.md, P7_DERIVATION.md, P7_DICTIONARY_SPEC.md, SINGLE_SAMPLE_GLOBAL_BOUND.md, and the model, Gaussian-source, dictionary and closure portions of established global_nonlinear.md C.4.7.8–10. Required mathematical and conjecture skills and their research-contract/adversarial references were read. No other study, earlier obstruction assessment, computation campaign, or Git operation was used. This is an internal theoretical route, not a promotion review.

## 1. The actual object and its unavoidable limiting projections

Use normalized inputs on the unit circle, Gaussian first row g=(g1,g2), tanh, the actual initialized action W0 and actual adjoint, and zero population readout. The dictionary is the nested extension of the retained middle-increment factor lists through p7; it is not the larger complete-word dictionary and does not add discarded intermediate action fields. Assume that every finite raw coefficient program in the chosen formal extension defines L2 fields. This is required for the hierarchy itself to be defined, rather than a temporal analyticity assumption.

Let V_l,p be its raw span on population l, and define

    V_l = closure(union_p V_l,p),       P_l = orthogonal projection onto V_l.

The raw prefixes retain their fixed nonzero scales. Write S_l,p for the map from raw coefficients to fields, G_l,p=S_l,p* S_l,p, and

    Q_l,p = S_l,p (G_l,p+eta_p I)^(-1) S_l,p*,
    eta_p = 1/[1024(p+1)^2].

Then, without any lower bound on Gram eigenvalues,

    Q_l,p -> P_l strongly on the entire population L2 space.             (1)

Indeed for a fixed finite-span vector v=S_l,p a, with its coefficient vector zero-padded at later levels, diagonalization gives

    ||(I-Q_l,p)v||_2 <= sqrt(eta_p) ||a||/2.

This follows from eta sqrt(lambda)/(lambda+eta)<=sqrt(eta)/2. Approximation by the union of the spans, and ||I-Q_l,p||<=1, proves convergence to the identity on V_l. Every Q_l,p vanishes on V_l perpendicular, proving (1) on the whole space. Fixed raw factorial scales cause no difficulty in this argument; a fixed earlier coefficient vector remains fixed.

Consequently the actual whole-middle initialization has the limit

    B_p = Q_2,p W0 Q_1,p -> B = P_2 W0 P_1,
    B_p* -> B*                                                        (2)

strongly. For example subtract Q_2,p W0(Q_1,p-P_1)v +(Q_2,p-P_2)W0P_1v. All these operators have norm at most A=||W0||. Convergence is uniform on every compact L2 set: cover that set by finitely many balls, apply strong convergence at their centers, and use the uniform operator bounds on the radii.

The limit is W0 only if an additional approximation/invariance statement holds. Letting eta_p decrease proves (1), not P_l=I or B=W0.

## 2. The hierarchy converges to its projected nonlinear flow

For one training direction x and label y, the half-square-loss physical equations of the limiting model are

    c_t = (y-f(x)) H(x),
    K_t = (y-f(x)) (P_2 delta(x)) tensor (P_1 h(x)),
    w_t = (y-f(x)) [1-h(x)^2] (B+K)*delta(x) x^T,

where h(u)=tanh(w dot u), H(u)=tanh((B+K)h(u)), delta=c[1-H(x)^2], f(u)=<c,H(u)>_2, and K(0)=c(0)=0, w(0)=g. The actual unhalved loss multiplies all three velocities by two. The finite-p equations replace B,P_l with B_p,Q_l,p. These are the prescribed coefficient-gradient equations, including the ridge filters.

For completeness, this system is well posed without bounded dictionary envelopes. In signed feature time s, put sigma=sign(y), alpha=||x||^2, z=w dot x, and

    F(z)=z/2+sinh(2z)/4,        X=F(z).

The first coordinate equation is X_s=sigma alpha(B+K)*delta. The maps F inverse and tanh composed with F inverse are globally 1-Lipschitz. On a finite feature interval [0,S], readout integration gives |c|<=S pointwise; hence ||delta||_2<=S, ||K||_HS<=S^2/2, and ||B+K||<=A+S^2/2. The difference estimate

    ||c phi'(z2)-c' phi'(z2')||_2
      <= ||c-c'||_2 + 2S ||z2-z2'||_2

supplies an integral contraction on a sufficiently short interval in L2 x HS x L2. Its readout component preserves the pointwise bound. The displayed a priori estimates permit continuation to each finite S. This is the same inverse-gate construction proved in SINGLE_SAMPLE_GLOBAL_BOUND.md; positive projections satisfy exactly its contraction hypotheses.

Here is a direct convergence proof, which also states the topology needed. On the limiting feature trajectory define

    a_p = sup_(s<=S,u on circle) ||(B_p-B)h(s,u)||_2,
    b_p = sup_(s<=S) ||(B_p*-B*)delta(s,x)||_2,
    d_p = sup_(s<=S) ||(Q_2,p delta) tensor (Q_1,p h)
                         -(P_2 delta) tensor (P_1 h)||_HS.

The continuous maps (s,u)->h(s,u), s->delta(s,x), and their rank products have compact images. Equations (1)–(2), boundedness, and the rank-one norm identity give a_p+b_p+d_p->0. Subtracting the two inverse-gate feature equations gives

    D^+ e_p(s) <= C_S [e_p(s)+a_p+b_p+d_p],    e_p(0)=0,

for e_p=||X_p-X||_2+||K_p-K||_HS+||c_p-c||_2 and a finite C_S independent of p. To verify the source split, compare the middle velocities first at the limiting h,delta, leaving d_p; compare the reverse actions first on the limiting delta, leaving b_p; and compare forward actions first on the limiting h, leaving a_p. All remaining terms use only the Lipschitz bounds above and contraction of Q_l,p. Integration therefore proves uniform feature-trajectory and circle-prediction convergence on [0,S].

On a fixed physical interval [0,T], energy gives |y-f_p(x)|<=|y|, and similarly for the limiting flow, so their accumulated feature clocks stay below |y|T (or 2|y|T for unhalved loss). Uniform feature convergence and the locally Lipschitz scalar clock equations imply compact-physical-time convergence.

There is also an all-time conclusion **to this projected limiting flow**. Put

    q = ||tanh(B tanh(g dot x))||_2^2.

If q>0, initialized q_p->q by (2). For all sufficiently large p, q_p>=q/2. The positive-operator/radial argument in SINGLE_SAMPLE_GLOBAL_BOUND.md applies with P_l as well as Q_l,p, and gives strictly increasing signed training feature prediction with derivative at least q, respectively q_p. The physical feature clocks thus stay in the common interval [0,2|y|/q]. Uniform feature prediction errors E_p on this interval tend to zero. Subtracting the clock equations gives

    |s_p(t)-s(t)| <= 2E_p/q       for every t>=0.

All test feature-prediction speeds on the common interval have one finite bound, so

    sup_(t>=0,u on circle) |f_p(t,u)-f_projected(t,u)| -> 0.             (3)

If q=0, the projected limiting flow is stationary because its initialized training activation and readout both vanish. Compact-time convergence still holds, and dense training on a nonzero label then disagrees with the limit. No proof that q=0 occurs for the actual derivative dictionary is supplied here.

Thus hierarchy convergence and dense-limit identification separate rigorously. Equation (3) does not identify f_projected with f_dense.

## 3. An initialized kernel gap is a genuine Gaussian population falsifier

Let h_u=tanh(g dot u), and define

    H_u^0=tanh(W0 h_u),        H_u^B=tanh(B h_u),
    k(u,x)=<H_u^0,H_x^0>_2,   k_B(u,x)=<H_u^B,H_x^B>_2.

The finite-p kernel converges uniformly on circle squared to k_B. Indeed u->h_u is L2-continuous on a compact domain, (2) is uniform on its image, tanh is 1-Lipschitz, and every activation norm is at most one.

At c0=0 both hidden blocks have zero initial velocity, so unhalved single-sample loss gives the exact initialized slope

    partial_t f_dense(0,u)=2y k(u,x),
    partial_t f_p(0,u)=2y k_p(u,x).                                     (4)

If for one fixed Gaussian-population pair x,u

    delta0=|k_B(u,x)-k(u,x)|>0,                                       (5)

then the requested p-limit prediction convergence fails even on a compact time interval. This is stronger than merely comparing derivatives: a remainder bound uniform in p turns (4) into a fixed-time gap.

Here are explicit sufficient bounds. Let Y=|y|>0, ||x||=||u||=1, and 0<=t<=1. Energy and contraction give, for every p and for the dense model,

    ||c(t)||_infinity<=2Yt,
    ||K(t)||_HS<=2Y^2t^2,
    ||w(t)-g||_2<=2AY^2t^2+2Y^4t^4.

Therefore every hidden upper activation changes from its own initialization by at most Dt^2 in L2, where

    D=(A+2Y^2)(2AY^2+2Y^4)+2Y^2.

Readout integration and |f(t,x)|<=2Yt then yield

    |f(t,u)-2yt k_initial(u,x)| <= Ct^2,
    C=2Y+(8/3)YD.                                                    (6)

For example, ||c(t)-2ytH_x(0)||_2<=2Yt^2+(2/3)YD t^3; pairing with H_u(t) and adding its change supplies (6). This estimate applies to the dense and each compressed flow with the same constants.

For all sufficiently large p, (5) implies |k_p-k|>=delta0/2. Set t0=min(1,Y delta0/(4C)). Equations (4)–(6) give

    |f_p(t0,u)-f_dense(t0,u)| >= Y delta0 t0/2 >0.                      (7)

This proves the falsifier without interchanging derivatives and p limits. Neither a nonzero hidden-state residual nor a finite-p kernel discrepancy alone establishes (5): a hidden residual might be invisible to a particular output pairing, and finite-p discrepancies may vanish.

## 4. Why the tempting elementary obstructions do not close (5)

**Parity is compatible with the target.** At finite width, change signs of any lower neurons by a diagonal sign matrix S: w->Sw and W0->W0S. All lower activations and lower factor coefficients acquire S, while upper fields are unchanged. Similarly changing upper signs by T sends W0->TW0, c->Tc and all upper factor coefficients to their T transforms. Gaussian initialization is invariant under both operations, and tanh oddness makes the exact gradient field equivariant. Formal coefficient extraction preserves this equivariance. The corresponding population sign sectors of the derivative factors are also the sectors of h(u),H(u),c and delta for every input direction. A constant or an even test field excluded by this symmetry is not a missing target activation in this bias-free problem.

**Two probes do not omit the initial row sigma algebra.** The retained h1=tanh(g1), h2=tanh(g2) are injective coordinate transforms, so sigma(h1,h2)=sigma(g1,g2) up to null sets. Every initialized lower test feature h_u is measurable in that sigma algebra. This says nothing about membership in the *linear closed span* V1, but rules out the inference that two fixed probes necessarily discard the initial input direction.

**Positive gate factors do not by themselves imply a closed-span obstruction.** Derivative factors carry powers of sech gates, but these gates are strictly positive almost surely. Multiplication by a bounded positive gate has dense range in L2: for a desired f, truncate f/gate on {gate>=1/n,|f|<=n}, then multiply back and use dominated convergence. This does not prove the dictionary contains those truncated quotients. It explains why pointwise vanishing at infinity or on null sets cannot alone prove a positive L2 distance.

**No total lower blind direction comes from the two seeds alone.** If u_a is nonzero, E[tanh(g dot u)tanh(g_a)] has the sign of u_a and is nonzero. Conditional on g_a=z, the first factor has an odd conditional mean strictly increasing in u_a z, because tanh is strictly increasing and the other Gaussian coordinate is symmetric. Its product with tanh(z) therefore has that fixed nonzero sign almost everywhere. Thus no nonzero direction h_u is orthogonal to both retained lower seeds. This does not exclude more subtle loss after the two-sided operator compression.

**Adaptive Gaussian innovations cannot be deleted.** Established C.4.7.8 (H6) makes each actual reverse action a Gaussian source plus the earlier forward-input response, and each later forward action has its matching reverse-response terms. Conditioning only on the two upper initialized probe coordinates and treating every higher derivative factor as a function of those two coordinates would discard the new Gaussian sources already present at the next nontrivial order. Conversely, knowing that the finite-source union is countable does not prove its linear factor span is dense.

**Static-label derivative data do not automatically provide a complete word algebra.** Coefficient collection supplies specific combinations of multiplication and actual action calls. Closure under arbitrary products, arbitrary bounded functions of tuples, or every individually separated action word has not been proved for their linear span. Those are the ingredients used by the established complete-word density theorem, and cannot be imported into the derivative-only candidate merely because its computational graph uses the same elementary operations.

## 5. Exact status

Proved here: the ridge filters converge to their closed-span projections; the actual hierarchy converges on compact physical intervals to the corresponding projected nonlinear flow; when its initialized training energy is positive, convergence to that flow is uniform for all physical times and all circle inputs; a nonzero limiting initialized test-kernel gap forces a fixed positive-time prediction discrepancy.

Not proved here: that the actual Gaussian derivative-factor spans miss a relevant vector; that they are dense in all required directions; that their projected limiting kernel differs from the dense kernel; or that the projected nonlinear flow agrees with dense training when the initial kernels happen to agree. The strongest surviving bottleneck is identification of these actual closed spans and their action on the single-sample feature trajectory. Finite exceptional weights, small-p mismatches, formal Taylor divergence, and parity alone do not resolve it.

## Post-freeze supervisor exchange and independent ridge check

After the preceding route was frozen, the supervisor supplied the following additional observation, which checks directly. For training at either fixed normalized axis a, h_a belongs to V1 and U_aa=tanh(Y_a)sech^2(Y_a) belongs to V2, where Y_a=W0h_a is nondegenerate Gaussian. Therefore

    <U_aa,Bh_a>_2 = <U_aa,W0h_a>_2
                  = E[Y_a tanh(Y_a)sech^2(Y_a)] > 0.

The integrand is positive away from zero and integrable. Hence Bh_a is not zero, q>0, and the all-time convergence (3) to the projected limiting flow holds unconditionally for the two fixed axis training directions. This still does not identify that flow with the dense one for those directions.

With explicit supervisor authorization, the already-written ridge section of POPULATION_CONVERGENCE_ATTEMPT.md was then read independently. Its variational identity

    <v,(I-Q_p)v>=min_a {||v-R_pa||^2+eta_p||a||^2}

and its strong-limit proof are correct, including singular Grams and nested zero-padding. The ensuing operator-limit statement is correct. To make its indicated subtraction fully explicit, the apparently varying-argument term can be written

    (Q_2,p-P_2)W0 Q_1,p v
      =(Q_2,p-P_2)W0 P_1v
        +(Q_2,p-P_2)W0(Q_1,p-P_1)v.

The first term tends to zero by strong convergence on the fixed vector W0P_1v, and the second by uniform operator bounds. This is an exposition completion, not a defect in the claim. No other route report was read.
