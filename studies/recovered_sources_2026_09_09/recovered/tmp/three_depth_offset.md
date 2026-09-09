# Explicit general-depth offset fallback

This is a new derivation, not an assertion that the old three-hidden-layer proof already proves arbitrary depth. It uses the canonical finite-program/common-action and asymmetric cap-comparison proofs supplied in the cited local sources. No experiments were run. Its activation changes the restricted odd/unit-slope family: the statement concerns **a fixed large affine gain and offset**, plus a fixed positive arctangent coefficient.

## 1. Statement and explicit parameters

Fix hidden depth L>=2, three normalized deterministic inputs with Gram Gamma satisfying Gamma_ij<=1-delta for i!=j, and binary labels y_i in {-1,1}. Feasibility implies 0<delta<=3/2. Put lambda=delta^2/4. The raw initialization, raw metric, simultaneous raw GD step n^{-2}, and finite readout initialization are the old theorem's, extended to L hidden layers.

The following single activation is sufficient in every layer:

    phi(z)=a(1+z)+e atan(z).

Both a and e are chosen before the actual inputs, labels, dimension, width, or physical horizon. Here is a constructive rule using only L and delta.

Let

    U=12/lambda,
    F=12^(L+1), G=22^(L+1), B=L F G, E=2 F 22^(L+1),
    R=1+F+G F U,
    alpha=16^(L+1)(F^2+1),
    M=16^(L+1)(R+U+1), Q=100 R(1+M+U).

Let G0 be a standard normal scalar and define the absolute positive constants

    eta0=inf_{sigma>=1} inf_{b,c} E[atan(sigma G0)-b-c sigma G0]^2,
    t0=min{1/2, sqrt(eta0)/(2(1+pi))}.

The strict positivity proof is the old proof's elementary Gaussian regression argument: the regression error is positive at every finite sigma, continuous on compact positive intervals, and tends to (pi^2/4)(1-2/pi)>0 as sigma tends to infinity.

Choose a to be twice the maximum of 1 and the following five quantities:

    (4 B F U^2)^(1/(2L)),
    (24 F E B F U^2/lambda)^(1/(2L)),
    (12 B^2 F^2 U^2/lambda)^(1/(2L)),
    (E B F U^2/t0)^(1/(L+1)),
    (1000 alpha U (Q+M+U+R^2+1))^(1/(2L)).

To define a motion constant, set b=(L+2)20^L F, and recursively

    N_1=P_1=b,
    N_l=b F^2+20 N_(l-1),
    P_l=3 b F^2+10 N_(l-1)+10 P_(l-1),  2<=l<=L.

Let P=max(1,P_1,...,P_L), and choose

    e=a^(-L)/(100 P).

These are explicit finite expressions. In particular a is bounded above by C_L(1+delta^{-4}) and e is bounded below by c_L(1+delta^{-4})^{-L}, where C_L,c_L are fixed positive constants given by this rule and the absolute constant t0. The deliberately loose delta^{-4} bound is immediate from the displayed formulas: R,M are O_L(lambda^{-1}), Q is O_L(lambda^{-2}), and every term defining a has at most lambda^{-3/(2L)} or lambda^{-2/(L+1)} growth. The displayed max is sharper than the common delta^{-4} envelope.

With this activation one obtains the same global canonical strong population solution, uniqueness against bounded-primal strong competitors, compact-physical-horizon finite GF and exact raw GD limits, path/velocity/second-moment observables, uniform all-time population nonaffinity, nonzero initial acceleration of every hidden parameter block and each sample's hidden features, and a changing projected total kernel. This remains convergence on each fixed finite horizon, not one probabilistic uniform limit on the infinite half-line.

The direct response closure below is the new general-depth argument. The all-upper-sample motion lemma in Section 5 is also new.

## 2. Exact normalization and the raw/clock bootstrap

Write

    H_i^l=h_i^l/a^l, Z_i^l=z_i^l/a^(l-1), v=a^L C,
    psi_l(z)=a^(1-l)+z+e a^(-l) atan(a^(l-1)z), eta=a^(-2L).

Then Z_i^1=W^1 x_i, Z_i^l=W^l H_i^(l-1), and f_i=<v,H_i^L>. The normalized gates satisfy

    1<=psi_l'<=2,
    |psi_l(z)|<=3+|z|,
    |psi_l''(z)|<=e a^(l-2)<=1.

Take normalized incoming-field clips and the gate

    D_l(z,q)=q+(e/a)g(a^(l-1)z) tau_cap(q), g(z)=1/(1+z^2).

The cap can be layer dependent when translated back to raw coordinates; it tends to infinity in every layer. This is only an approximation used to construct the original uncut flow.

Replace -r_i by arbitrary deterministic controls c_i(s) with sum_i |c_i(s)|<=1 in the original residual-clock equations. Use normalized clock u=a^(2L)s. The equations become exactly

    v'=sum_i c_i H_i^L,
    (W^1)'=eta d^(-1) sum_i c_i beta_i^1 x_i^T,
    (W^l)'=eta sum_i c_i beta_i^l tensor H_i^(l-1), 2<=l<=L,

where beta_i^L=D_L(Z_i^L,v), beta_i^l=D_l(Z_i^l,(W^(l+1))^*beta_i^(l+1)). This scaling follows from beta_i^l=a^(l-1)b_i^l, so every hidden update has exactly the same factor eta.

Let D be the sum of sqrt(d) times the first weight displacement and all hidden HS displacements. On D<=1, initialized action norms <=10 imply current action norms <=11. Initial projected first norms <=2 give current first norms <=3. Forward/backward induction gives

    ||H_i^l||_2<=F, ||beta_i^l||_2, ||q_i^l||_2<=G ||v||_2,
    ||v(u)||_2<=F u, D(u)<=eta B F u^2/2<=eta B F U^2.

The same bounds hold at every positive Euler mesh: sum_j h_j u_j<=u_k^2/2. Summing the rank-one update norms is sufficient; no trained operator-norm convergence is assumed.

A normalized forward perturbation induction gives

    ||Delta H_i^l||_2, ||Delta Z_i^l||_2<=E D.

For example the next normalized preactivation changes by at most F D+10||Delta H^(l-1)||; the next feature adds a factor <=2. The displayed E dominates this geometric series.

The initial normalized top feature Gram obeys

    Q_L(0)>=Gamma+(sum_{k=1}^L a^(2-2k)) 11^T>=lambda I_3.

This follows layer by layer by Gaussian projection onto constants and the linear chaos; the arctangent term has a nonnegative linear Gaussian projection coefficient. The augmented Gram estimate Gamma+11^T>=lambda I_3 includes singular Gamma.

For the current readout Gram,

    ||Q_L(u)-Q_L(0)||_op<=6 F E D<=lambda/4.

The definition of a ensures D<1/2, so the stopped controlled argument closes with slack. It also ensures

    3 eta B^2 F^2 U^2<lambda/4,
    a^(L-1) E D<t0.

For the actual capped physical flow let tau=a^(2L)t. Its residual equation is

    dr/dtau=-(Q_L+eta J_h U_h,cap)r.

Here J_h and U_h,cap are respectively the true hidden Jacobian and capped hidden coefficient map of f=<v,H^L>. Their norms are <=sqrt(3)B||v||. Therefore the possibly nonsymmetric hidden contribution has absolute operator norm <=3 eta B^2 F^2 U^2<lambda/4. Its sign is not assumed. Thus

    ||r(tau)||_2<=sqrt(3) exp(-lambda tau/2),
    integral_0^infinity ||r(tau)||_1 d tau<=6/lambda=U/2.

The normalized residual clock u(tau)=integral ||r||_1 cannot hit U. At r=0 the actual physical vector field is zero. This proves global capped physical continuation and the same controlled ball uniformly in caps, physical horizons, and auxiliary meshes. No capped energy identity is used.

## 3. Exact general-depth source coefficients and their direct closure

At a fixed finite positive mesh of normalized controlled duration <=U, freeze its deterministic controls and contractions, exactly as in the supplied controlled response proof. The normalized source equations for each action l=2,...,L are

    Z_k^l=xi_k^l+sum_{j<k} A^l_kj beta_j^l,
    q_k^(l-1)=zeta_k^(l-1)+sum_{j<=k} B^l_kj H_j^(l-1),
    Z_k^1=Z_0^1+eta sum_{j<k} h_j Gamma diag(c_j) beta_j^1,
    v_k=sum_{j<k} h_j c_j^T H_j^L.

The coefficient entries are exactly

    A^l_(ki,rj)=E[partial_(zeta^(l-1)_(r,j)) H^(l-1)_(k,i)]
                   +eta h_r c_(r,j) E[H^(l-1)_(k,i) H^(l-1)_(r,j)],
    B^l_(ki,rj)=E[partial_(xi^l_(r,j)) beta^l_(k,i)]
                   +1_(r<k) eta h_r c_(r,j) E[beta^l_(k,i) beta^l_(r,j)].

Independent primitive source groups retain all their within-group time/sample covariance, including singular covariance. The primitive forward covariance is the preceding normalized feature Gram, and the primitive reverse covariance is the normalized beta Gram. The primal bounds just proved imply every primitive scalar source standard deviation <=R. Derivatives retain separate named slots and freeze covariance parameters, arrays, and controls; no derivative of normalized residual feedback occurs.

Use maximum absolute row-sum matrix norms, and sum those norms over time blocks. Set

    alpha_l=16^l(F^2+1), 2<=l<=L,
    M_l=16^(L-l+1)(R+U+1), 2<=l<=L.

Claim, uniformly in all meshes and caps:

    |A^l_kj|<=eta alpha_l h_j,
    sum_{j<=k}|B^l_kj|<=M_l.

The proof is chronological: construct the current forward A rows bottom to top using only past B rows; construct current B rows top to bottom, allowing the already constructed next-layer current return. The derivative estimates below give strict improvements at each stage. No simultaneous induction hypothesis on unconstructed current rows is used.

### 3a. Prefix moments

Assume only the coefficient rows already needed for a given stage. A normalized coordinate gate has |D|<=2|q| and |psi|<=3+|z|. Bottom and middle source recursions therefore give the scalar Volterra inequalities

    max_{v<=k} ||H_v^l||_p
       <=(3R+4 eta alpha R U) sqrt(p)
                   +4 eta alpha M sum_{r<k}h_r max_{v<=r}||H_v^l||_p.

For the first layer replace alpha by 1. At the top, eliminating v produces the same form with M replaced by U. Finite product iteration bounds the feature moments by 10R sqrt(p), since the choice of a implies

    eta alpha U (Q+M+U+R^2+1)<1/1000.

Consequently

    ||v_k||_p<=10R U sqrt(p),
    ||q_k^l||_p<=R(1+10M) sqrt(p).

For the maximum of the three incoming sample coordinates, Minkowski adds at most a factor three. Hence the common Q above gives

    || max_i |q_(k,i)^l| ||_p, ||v_k||_p<=Q sqrt(p).

These are marginal time bounds, never a random maximum over all mesh times.

### 3b. Derivative envelopes, including current terms

Let J denote a preactivation derivative and T a readout derivative. Local derivatives are matrices G=psi', V=partial_q D, L=partial_z D, and satisfy

    |G|,|V|<=2, |L|<=max_i |q_i|.

For a single reverse source at time j, the bottom derivative has injection at most 2 eta h_j. At middle layer l it has injection at most 2 eta alpha_l h_j. A full forward-source row has injection one. The precise differentiated recurrence is

    J_k=I_k^xi+sum_{r<k} A_kr [L_r J_r+V_r(I_r^zeta+sum_{v<=r} B^(l+1)_rv G_v J_v)].

The bottom version replaces A_kr by eta h_r Gamma diag(c_r). The top version replaces the incoming bracket by V_r 1 T_r, with

    T_k=sum_{r<k} h_r c_r^T G_r J_r.

After finite product iteration, every full forward-source derivative row is bounded by

    E_k=exp(4 eta alpha (M+U)U+eta alpha sum_{r<k}h_r Q_r),

and single reverse-source derivatives by 2 eta h_j E_k at the bottom, or 2 eta alpha_l h_j E_k in the middle. The top readout derivative row is <=2U E_k. Here Q_r is the appropriate incoming-coordinate maximum. This envelope includes every current L_k J_k term at the backward output.

The elementary implication ||X||_p<=Q sqrt(p) gives

    E exp(X^2/(8 exp(1) Q^2))<=2,
    E exp(t |X|)<=2 exp(2 exp(1)t^2 Q^2).

Weighted Jensen in the finite time sum, followed by these estimates, yields ||E_k||_4<2 under the displayed 1/1000 inequality. Temporal independence is not needed. The actual primal L2 norm of an incoming sample maximum is <=3R, even though its source-derived higher moment constant is larger. Cauchy--Schwarz therefore gives

    E[Q_k E_k]<=6R.

This is useful because it prevents a coefficient bootstrap from replacing a true primal L2 norm by its much larger source majorant.

### 3c. Coefficient production and strict chronological closure

At the bottom, differentiating H adds another factor 2. Taking expectation of the derivative envelope gives an A^2 density <=8 eta; the learned term adds eta F^2. At a middle stage, the resulting A^(l+1) density is at most

    eta(F^2+8 alpha_l)<eta alpha_(l+1).

At the top the full backward-output derivative row satisfies

    sum_j |E partial_(xi_j^L) beta_k^L|
                         <=6R+8U.

At a lower action l it satisfies

    sum_j |E partial_(xi_j^l) beta_k^l|
                         <=6R+8 M_(l+1).

The second term is precisely the current and past return through B^(l+1), not an omitted source. Learned backward moments add at most eta U R^2<1. Hence the new B^L row is strictly less than M_L=16(R+U+1), and every descending B^l row is strictly less than M_l. The choices alpha_l=16^l(F^2+1) and M_l=16^(L-l+1)(R+U+1) leave uniform slack.

Current B rows may be large but are constructed only in descending layer order. Explicitly their current terms contain a local E L_k contribution and the next current B row multiplied by bounded V/G gates. There is no same-row inverse, and there is no product of unresolved current rows.

Starting with zero readout and zero backward fields, induction over times and then the two layer sweeps proves all coefficient bounds. Section 3a now applies globally on every controlled interval of length <=U. It supplies uniform Gaussian L2 tails for all incoming fields, independently of cap, mesh and physical horizon. This is a direct nonlinear closure; an implicit perturbative response cutoff is unnecessary.

## 4. Cap removal and full finite-dynamics bridge

The old fixed-program Gaussian-conditioning proof is stated for arbitrary finite transcripts, Gaussian matrix calls in both orientations, and finite independent root tuples. Replacing the old two actions by L-1 independent actions and keeping three sample slots meets those hypotheses for every fixed L. Singular query Grams retain the supplied independent-query regularization proof. The common generated-space completion retains genuine adjoints by finite transpose identities. No cross-width trained operator norm is asserted.

For two normalized gates the asymmetric comparison is

    |D_cap'(zA,qA)-D_cap(zB,qB)|
      <=2|qA-qB|+C cap |zA-zB|+2|qB|1_(|qB|>cap).

Successive backward substitution at arbitrary fixed L gives one linear cap factor: a forward error receives it, while an incoming error receives only bounded gates and actions. Constants grow with L but the cap exponent does not. The uniform source tails from Section 3 beat this propagation and give on each finite physical interval

    raw state and direction discrepancy <=C_T exp(C_T cap-c cap^2).

The reference-only nature of this estimate proves both cap removal and uniqueness against any bounded-primal strong competitor on the same canonical spaces, with no tail hypothesis on the competitor. It also proves unique continuation from reached states. Global capped bounds and compatible compact-interval limits give one global autonomous strong C1 population trajectory.

At fixed cap and finite auxiliary physical mesh, the finite-program theorem identifies all contractions and queries. The finite readout remains N(0,n^-2) coordinatewise throughout actual finite training; its initial RMS is O_P(n^-1), so its population initial value is zero. Stopped primal comparison transfers that vanishing discrepancy and removes the auxiliary mesh. Same-width uncut/capped comparison then yields finite GF convergence, taking width first and cap second. The exact raw simultaneous GD contributes only its fixed-cap Euler consistency error O_{cap,T}(n^-2); no theorem about a width-growing transcript is used.

All observable arguments extend by finite induction in L. Predictions, loss and each kernel block are contractions of convergent L2 fields. The first block is Gamma_ij<b_i^1,b_j^1>; hidden block l>=2 is <b_i^l,b_j^l><h_i^(l-1),h_j^(l-1)>; the readout block is <h_i^L,h_j^L>. Recomputed velocities use the exact forward chain rule and the source proof's ordered observational truncation: width first at fixed cap and velocity truncation, then cap removal, then removal of the velocity truncation. Finally the interpolation estimate

    ||x-I_h x||_infinity^2<=4h integral_0^T |x'(t)|^2 dt

upgrades joint-time W2 convergence and integrated speed bounds to same-layer three-sample path-law convergence in W2(C([0,T];R^6)). This yields the old list of laws, velocity laws, second moments and integrated squared speeds for every layer, with the same mesh-node conventions.

The raw preactivation displacement bound from Section 2 is uniformly below t0. Every initialized scalar raw preactivation is Gaussian with standard deviation >=1. The regression stability argument therefore gives, for every sample and layer and all t>=0,

    inf_{b,c} E[phi(z_i^l(t))-b-c z_i^l(t)]^2 >= e^2 eta0/4 >0.

This statement does not assume Gaussianity at trained times.

## 5. New general-depth all-sample initial-motion lemma

Let p=y/3, m=sum_i p_i; then |m|>=1/3. Work first with the affine activation e=0 and normalized features H^l. Write

    c_j=(Gamma p)_j,
    v_r=sum_{k=1}^r a^(2-2k), v_0=0,
    d_k=c_j+v_(k-1)m.

At initialization, the normalized feature Gram at layer r is Gamma+v_r 11^T. Let

    Hbar=sum_i p_i H_i^L,
    Q^l=(W^(l+1))^* ... (W^L)^* Hbar,
    R_(l,k)=W^l ... W^(k+1) (W^(k+1))^* ... (W^l)^*,
    R_(l,l)=I,
    T_j^l=sum_{k=1}^l d_k R_(l,k).

Direct differentiation of the raw hidden feature-ascent objective (1/2)||Hbar||^2 gives the normalized sample preactivation direction

    Ubar_j^l=T_j^l Q^l.

The first-block contribution has coefficient c_j; each subsequent block has coefficient c_j+v_(k-1)m. Propagating a lower block through the intervening affine gates, and propagating its backward field back from layer l, gives exactly the two oriented factors of R_(l,k).

For independent square Gaussian actions, normalized trace contractions obey

    tau(R_(l,k)R_(l,r))=1+l-max(k,r).

To verify the cross formula, integrate out the extra innermost matrices in the longer product: their expected XX^* is I, leaving the second moment of the shorter product. For a product of s independent square Gaussian matrices, its squared covariance has limiting normalized trace s+1. This follows inductively from Gaussian fourth moments: adjoining one square Gaussian factor changes this second trace moment by (normalized first trace)^2=1. The finite Wick polynomial transcript also shows convergence of these finitely many contractions to their expectations.

Therefore

    tau((T_j^l)^2)
      =(sum_{k=1}^l d_k)^2+sum_{r=1}^{l-1}(sum_{k=1}^r d_k)^2.

For l>=2, the right side includes both d_1^2 and (d_1+d_2)^2. Since d_2-d_1=m,

    tau((T_j^l)^2)>=m^2/5.

This bound is independent of c_j, Gamma, dimension, and depth.

Now isolate the last affine offset in Hbar:

    Hbar=a^(1-L)m 1+W^L Hbar_(L-1).

For l<L, the contribution of the first term to Q^l is odd under W^L -> -W^L, while the contribution of the second is even. T_j^l is independent of W^L. Their cross inner product hence has zero population expectation. The first term's upper transpose product is isotropic with covariance I and independent of the lower actions, giving

    ||Ubar_j^l||_2^2 >= a^(2-2L)m^2 tau((T_j^l)^2).

For l=L, T_j^L is even under W^L -> -W^L, so the same parity kills the cross term. Row orthogonal invariance gives ||T_j^L 1||_2^2=tau((T_j^L)^2). Thus the identical estimate holds at the top. We obtain for every upper sample and l=2,...,L

    ||Ubar_j^l||_2 >= a^(1-L)/(9 sqrt(5)).

These are deterministic population norms identified from fixed Gaussian polynomial transcripts. The argument does not assume sample exchange symmetry.

Return to the chosen positive e. Set epsilon=e/a. On the same initial actions the normalized activations differ from their affine versions by at most 2epsilon and their first derivatives differ by at most epsilon. Forward induction gives ||Delta H_i^l||_2<=F epsilon. Backward induction gives both normalized beta norms and their differences divided by epsilon at most b=(L+2)20^L F. Rank-one differences bound hidden matrix direction differences by 2bF epsilon. The forward direction product rule then gives precisely the N_l,P_l recursions in Section 1:

    ||Ubar_(j,e)^l||_2<=N_l,
    ||Ubar_(j,e)^l-Ubar_(j,0)^l||_2<=P_l epsilon.

Our choice e=a^(-L)/(100P) yields error at most a^(-L-1)/100, which is strictly smaller than half of a^(1-L)/(9 sqrt(5)). Hence every upper sample's preactivation direction remains nonzero. The raw direction differs by the positive deterministic scaling factor a^(2L+l-1), so it too is nonzero.

For the first layer and the hidden parameter blocks, use the nonlinear argument rather than affine transfer. Since L>=2, the top initialized preactivation triple has full Gaussian support: Q_1>=a^2(Gamma+11^T)>0. The top backward-field Gram for scalar-feature ascent is positive definite. Indeed a zero combination would imply

    (sum_i p_i phi(z_i))(sum_i v_i phi'(z_i))=0 on R^3.

The first factor has no open zero set because p_i phi'(z_i) never vanishes. Differentiating the second factor in each z_i forces v_i=0, because phi'' is not identically zero. Each reused transpose then supplies a fresh independent Gaussian source with this positive definite covariance. Multiplication by a gate >=a propagates positivity down every backward Gram. The ordinary input Gram can be singular: its diagonal ones suffice to make each first-sample direction have positive conditional variance. Hidden matrix direction squared norms are trace pairings of positive definite feature/backward Grams conjugated by diag(p), so each is positive; the first raw block is positive by the same conditional variance argument.

At physical time zero C=0 and all hidden velocities vanish. Strong chain rules give C'(0)=3 sum_i p_i h_i^L and hidden accelerations 9V, where V is the original unnormalized scalar-feature ascent direction. Thus every hidden parameter block and every sample's preactivation/feature has nonzero initial acceleration. Feature acceleration is nonzero because phi'>=a.

Finally, with kappa=p^T K_total p, the same adjunction identity valid at any finite L is

    kappa(t)=||hidden gradient of sum_i p_i f_i||_raw^2
                    +||sum_i p_i h_i^L||_2^2.

Using hidden displacement (9/2)t^2 V+o(t^2) and hidden gradient 3t V+o(t),

    kappa(t)=kappa(0)+18t^2 ||V||_raw^2+o(t^2).

Since V is nonzero, the actual projected total kernel changes for all sufficiently small positive physical times.

## Scope and dependency audit

The offset is essential to the stated coercivity and the affine m!=0 motion argument. This does not establish the requested theorem if the admissible activation must be exactly odd or exactly the previous unit-slope family. It is an explicit, general-hidden-depth extension of the older gain-and-offset theorem, with polynomial delta scales and no implicit nonlinear response cutoff.

The finite-program conditioning, canonical action construction, singular-query treatment, asymmetric cap comparison, and ordered velocity/path bridge remain source dependencies. Their hypotheses have been checked for arbitrary fixed L above; they are not replaced by a claim that raw L2 boundedness alone gives infinite-dimensional local Lipschitzness or compactness.

L>=2 is material for the all-sample initial-motion conclusion. At L=1, an antipodal pair with equal labels and an orthogonal third can have exactly cancelled first-sample hidden motion for this constant-plus-odd activation.

## Addendum: the actually permitted small-offset/unit-gain family

If the activation must be a unit-sum mixture of the identity and arctangent, plus a small positive offset, the preceding large-gain construction is outside that class. No proof above should be reported as settling that request.

For the affine baseline phi(z)=b+z with b>0 and unit slope, the initial top Gram is exactly

    Q_L(0)=Gamma+L b^2 11^T.

Thus the available separation-only coercivity is at least min(1,Lb^2)delta^2/4, and degenerating configurations show that small b genuinely weakens the missing affine direction. The residual-clock length supplied by this estimate is O_L((b^2 delta^2)^-1). With unit gain there is no eta=a^(-2L) multiplying the hidden updates. The short-clock displacement majorant is consequently O_L(U^2), and the initial-feature-Gram bootstrap cannot close when U is large. This is a failure of the stated proof route, not a counterexample to the nonlinear trajectory.

The purely affine population vector field is polynomial on bounded raw Hilbert balls, hence locally Lipschitz there. Its exact gradient energy identity gives a finite-horizon raw path-length bound and therefore global strong affine continuation. What this does not give is a horizon-independent affine controlled ball, a finite total residual-clock estimate, or uniform source response coefficients sufficient to perturb by one fixed nonzero nonlinear coefficient for all times. A finite-horizon perturbation cutoff depending on T does not answer the all-time fixed-activation question.

There is a potentially useful exact projected balancedness invariant. Let 1_l denote the constant function in neuron layer l and P_l=I-1_l tensor 1_l the orthogonal projection off that function (the neuron probability measures have total mass one). For an interior affine layer define

    M_l=A_l A_l^* - A_(l+1)^* A_(l+1).

At the top replace the second term by C tensor C. Writing beta_i^l for the residual-free affine backward field, direct differentiation yields

    M_l'=b sum_i r_i [beta_i^l tensor 1_l + 1_l tensor beta_i^l].

Indeed the incoming action produces z_i^l in its product derivative, whereas the outgoing action produces h_i^l=z_i^l+b1_l; their difference is exactly the displayed rank-two term. Therefore

    P_l M_l(t) P_l=P_l M_l(0) P_l

is an exact invariant. The unprojected balancedness invariant familiar from zero-offset deep linear networks is unavailable. The projection removes precisely the constant neuron direction that supplies the extra affine feature needed for singular three-input Grams. Consequently this invariant alone does not yet supply a full feature-Gram floor or a bound in that direction. A successful unit-gain proof would need an additional estimate for those constant-direction components, or a different global source mechanism. No impossibility of such an estimate has been shown.
