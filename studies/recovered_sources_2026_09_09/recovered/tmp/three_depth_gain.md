# A direct source closure for fixed relative odd nonlinearity and large gain

Theory-only derivation. The activation is changed explicitly to

    phi_A(z)=A(z+atan z), A>=2,

at every hidden layer. This does not assert a result for the previously frozen convex mixture. The useful conclusion is a direct finite-depth cap/mesh-uniform source estimate, with no affine-trajectory comparator, that closes the population existence bottleneck when A>=C_L delta^-2. Initial acceleration of every individual sample/layer is not proved in this note.

## 1. Exact normalization, preserving the original raw metric

Fix hidden depth L>=2. Write raw h_l=A^l H_l and raw z_l=A^(l-1) Z_l. The initialized and learned adjacent operators and the raw readout C are unchanged. Then

    H_l=psi_l(Z_l), psi_l(z)=z+A^(-(l-1))atan(A^(l-1)z),
    Z_1=w.u, Z_l=M_l H_(l-1), f_i=A^L<C,H_(L,i)>.

Every psi_l is odd, |psi_l(z)|<=2|z|, 1<=psi_l'<=2, and |psi_l''|<=K_l:=A^(l-1). Set K=A^(L-1). Let s(t)=integral_0^t ||r(v)||_1 dv and v=A^L s. On the residual-controlled clock v, the raw parameter equations are exactly the gradient-control equations for F_i=<C,H_(L,i)> with controls c_i=-r_i/||r||_1 and sum_i|c_i|<=1. Thus all blocks, including C, have the same unchanged raw metric on this auxiliary clock; this is a time/field identity, not a modified physical algorithm.

Use normalized backward gates

    D_(l,R)(z,q)=q+g(A^(l-1)z) tau_R(q), g(x)=(1+x²)^-1.

They obey |D|<=2|q|, |D_q|<=2 and |D_z|<=K|q|, uniformly in the cap R. These are precisely the original raw clipped gates after dividing the deterministic forward/backward scale factors.

## 2. Independent controlled primal estimates

Take

    P=100^(2L+4).

Here C(0)=0 is the population initialization, or the zero-readout finite comparator used in the existing finite-dynamics bridge. The actual random finite readout is retained in training and transferred by that bridge; it is not silently reset. With hidden raw displacement D=sum of first-layer and HS-block displacements stopped at D=1, canonical initialized action norms <=2 imply current action norms <=3. The finite-width high-probability operator event <=10 can also be accommodated by this P. Forward and backward induction using slopes <=2 gives, for every cap and positive Euler mesh on a controlled interval of duration S,

    max_(i,l) ||H_(l,i)||_2 <=P,
    ||C(v)||_2 <=Pv,
    max_(i,l) ||q_(l,i)(v)||_2 <=P²v,
    D(v)<=P²v²,
    max_(i,l) ||Z_(l,i)(v)-Z_(l,i)(0)||_2<=P³v²,
    max_i ||H_(L,i)(v)-H_(L,i)(0)||_2<=P³v².

The constants deliberately dominate sums over three samples and L blocks. The hidden speed is at most P||C||, and the readout speed is at most P, which proves D<=P²v². The two forward-difference estimates follow by telescoping the L bounded actions/gates; P is much larger than the resulting factors. For Euler, sum_j h_j v_j<=v_k²/2. Thus P²S²<1/2 excludes the raw-ball stop independently of source bounds and independently of a capped energy identity.

## 3. Exact local source equations at every depth

At a fixed finite positive mesh, freeze deterministic controls, contractions, response arrays and Gaussian source covariances in named-slot derivatives. The reused-matrix chronological construction gives

    Z_1=z_0+A_1 delta_1, A_1,kj=h_j Gamma diag(c_j), j<k,
    Z_l=xi_l+A_l delta_l,                       2<=l<=L,
    q_l=zeta_l+B_(l+1) H_l,                     1<=l<L,
    q_L=B_(L+1)H_L=C, B_(L+1)=readout integration,
    H_l=psi_l(Z_l), delta_l=D_(l,R)(Z_l,q_l).

The readout integration row has norm <=S. All A_l are strict in time, and all B_l are causal, including their current returns. For l>=2, A_l is the expected named-zeta_(l-1) derivative of H_(l-1), plus its learned H_(l-1)-Gram contraction. B_l is the expected named-xi_l derivative of delta_l, plus its learned delta_l-Gram contraction. These are the same exact identities used in the general-depth source note. The source primitive standard deviations are at most P for xi_l, and at most 2P²S for zeta_l, by the independent primal bounds. No covariance inverse, time independence, or renewed initialized action is introduced.

Use the induced infinity norm on the three sample coordinates; a strict density is sup_(j<k)||A_kj||/h_j and a causal row norm is sup_k sum_(j<=k)||B_kj||. If A_l has density alpha_l and B_(l+1) has row beta_(l+1), differentiation of its local equations gives

    J^zeta=A_l[V+(N+V B_(l+1)G)J^zeta],
    J^xi=I+A_l(N+V B_(l+1)G)J^xi,
    partial_xi delta_l=(N+V B_(l+1)G)J^xi,

where G=diag psi_l', V=diag D_q, N=diag D_z. In particular ||G||,||V||<=2 and ||N_k||<=K Q_k, Q_k=max_i|q_(l,k,i)|. The bottom has no xi source; the top has no zeta source. One may still use the displayed comparison envelopes there, since an absent derivative is zero. Current B returns are retained by the VBG term, including at the current mesh point.

## 4. A closed explicit coefficient box

Define ascending and descending radii by

    alpha_1=1,
    alpha_(l+1)=16alpha_l+2P²  (1<=l<L),
    beta_(L+1)=S,
    beta_l=16beta_(l+1)+16KP²S  (L>=l>=2).

Put

    a=(64P²)^L, b=(64P²)^(L+1),
    K S <= (10^6 a b P²)^-1.                  (SC)

Then alpha_l<=a and beta_l<=bKS. Condition (SC) in particular implies P²S²<1/2.

### 4a. Marginal source moments on the coefficient box

Let X_k=max_i||Z_(l,k,i)||_p. Gaussian p-norms and Minkowski give

    ||q_(l,k)||_(p,max)<=6P²S sqrt(p)+2 beta_(l+1) max_(j<=k)X_j,
    X_k<=3P sqrt(p)+2alpha_l sum_(r<k)h_r ||q_(l,r)||_(p,max).

(The first bound also covers the source-free top.) Discrete Gronwall yields

    X_k <= (3P+12aP²S²) exp(4abKS²) sqrt(p) <=4P sqrt(p),
    max_(k,i)||q_(l,k,i)||_p<=14P²bKS sqrt(p).

Thus ||Q_k||_p<=42P²bKS sqrt(p). The smallness asserted in the last step follows directly from (SC), P,a,b,K>=1. These are maxima of marginal norms, not norms of random maxima over mesh times.

### 4b. Exact derivative envelopes

Finite strict Volterra iteration in the differentiated equations gives

    ||J^xi_(k,bullet)||_row <= exp(E_k),
    ||J^zeta_kj|| <= 2alpha_l h_j exp(E_k),
    ||partial_xi delta_(l,k)||_row
       <=(K Q_k+4beta_(l+1)) exp(E_k),

where one can use the increasing envelope

    E_k=aK sum_(r<k)h_r Q_r+4abKS².

This follows by bounding VBG by 4 times the causal B row, leaving one strict A density. The random N is integrated once against the mesh weights. No products of random suprema over time appear.

If ||X||_p<=M sqrt(p), the power-series argument gives E exp(u|X|)<=2exp(2 exp(1)M²u²). Jensen in time therefore gives, with M=42P²bKS,

    E exp(2E_k)
      <=2 exp(8abKS²+8 exp(1)a²K²S² M²)<4

under (SC). Cauchy--Schwarz also gives Eexp(E_k)<2.

### 4c. Strict production estimates

The forward source response is bounded by 2 times J^zeta (the forward gate), and the learned Gram density is <=P². Therefore

    alpha_(l+1),new <=8alpha_l+P²=alpha_(l+1)/2.

For the reverse derivative, use the *independent true primal second moment* ||Q_k||_2<=3P²S in the leading multiplier, and the exponential bound just proved in the other Cauchy--Schwarz factor. Do not replace this leading factor by its weaker source moment estimate. The learned reverse density is <=4P^4 S², so its whole causal row is <=4P^4 S³. Hence

    beta_l,new <=6KP²S+8beta_(l+1)+4P^4S³
               <=7KP²S+8beta_(l+1) < beta_l/2.

The final inequality uses 4P²S²<=K, another consequence of (SC).

This closes the coefficient box chronologically: first the new forward rows A_2,...,A_L, then the new backward rows B_L,...,B_2. The A row is strict, so its differentiated past recurrence only uses already bounded reverse rows. The current top reverse return is included; each next current reverse row is available in descending order. Equivalently a continuous coefficient-amplitude first-exit argument has the displayed strict improvements. No smallest mesh step is required.

Consequently the incoming fields have cap/mesh-uniform subGaussian marginal tails on the entire controlled interval S. This is the needed new direct-response lemma. It applies to fixed controls and to actual residual controls after the deterministic clock weights are frozen in source derivatives.

## 5. Initial Gram, global residual budget, and gain exponent

Put G~N(0,1), m=E(1+G²)^-1, b_3=(1-2m)/sqrt(6), and

    lambda=(b_3²/3) delta².

The tensor dual-witness proof in the existing three-input geometry note gives Gamma^(circ 3)>=delta² I/3, including singular Gamma. The cubic Gaussian chaos of psi_1(G)=G+atan G has coefficient b_3, so Q_1>=lambda I. At every later initialized normalized layer, first Gaussian-chaos regression has coefficient >=1; hence Q_L(0)>=lambda I for every L. This is a fixed nonlinear Gram certificate independent of the gain, with no affine three-input coercivity assumption.

Take the controlled-clock budget

    S=12/(lambda A^L).

Then KS=12/(lambda A), so (SC) is ensured by

    A >= 12*10^6 a b P²/lambda.

For a fully conservative constant that simultaneously supplies primal, Gram, cap-residual, and nonaffinity slack, let

    eta_*=inf_(sigma>=1) inf_(alpha,beta)
            E[atan(sigma G)-alpha-beta sigma G]^2 >0,
    t_*=min(1/2,sqrt(eta_*)/[2(1+pi)]),
    Q_L=10^12 a b P^10 (1+t_*^-1),
    A>=Q_L/lambda.                               (GAIN)

The elementary regression compactness proof from the existing three-input gain theorem proves eta_*>0. Initial raw scalar preactivation standard deviations are >=1.

Under (GAIN) and L>=2, all the following are strict:

    P²S²<1/2,
    ||Q_L(v)-Q_L(0)||op <=6P^4S² < lambda/4,
    ||J_hidden|| ||U_hidden,cap|| <= P^4S² <lambda/4,
    max_(l,i)||raw z_(l,i)(v)-raw z_(l,i)(0)||_2
              <=P³ K S² < t_*.

For the Gram bound, ||H||<=P and ||Delta H||<=P³S² give the stated 6P^4S². In the hidden Jacobian bound P has sufficient slack to dominate the sum of raw block sensitivities to C. If needed use P^6 instead of P^4; (GAIN) dominates either. Since S²=144 lambda^(2L-2)/Q_L^(2L) at the smallest admitted gain and lambda<1, the lambda comparison is immediate for L>=2. The raw preactivation estimate is P³KS²=144P³ lambda^(L-1)/Q_L^(L+1).

For the actual capped physical residual,

    rdot=-A^(2L)[Q_L+J_hidden U_hidden,cap]r.

The capped hidden matrix need not be positive; its absolute bound suffices. Thus before a controlled-budget hit,

    ||r(t)||_2<=sqrt(3) exp(-lambda A^(2L)t/2),
    A^L integral_0^infty ||r(t)||_1 dt
                    <=6/(lambda A^L)=S/2.

This excludes the hit with strict slack and makes every fixed-cap flow global. Applying the direct source lemma on the one bounded clock budget yields tails independent of the physical horizon. The existing asymmetric one-cap-factor comparison therefore constructs a unique global strong uncut population flow and yields the full fixed-horizon finite GF/raw-GD limits through the already established finite-program and ordered velocity/path bridges, once those bridge hypotheses are written out for this normalization. The physical loss bound is

    L(t)<= (3/2) exp(-lambda A^(2L)t).

The gain order supported by this proof is A>=C_L delta^-2. This is a sufficient exponent, not an optimality claim and not a depth-uniform prefactor claim.

## 6. Uniform strict nonaffinity

The raw preactivation displacement bound <t_* and the regression continuity argument used in the old three-input gain theorem give

    inf_(t>=0,i,l) inf_(alpha,beta)
      E[phi_A(raw z_(l,i)(t))-alpha-beta raw z_(l,i)(t)]²
      >=A² eta_*/4 >0.

The regression constant removes the linear Az part exactly, and the remaining coefficient is A. This is fixed relative nonlinear amplitude (coefficient ratio one), rather than a nonlinear coefficient tending to zero. At high raw variance, its relative contribution to the total activation variance becomes small; the absolute regression assertion above is the precise retained certificate.

## Scope and remaining work

The source bootstrap and its coupling with the global residual clock are derived here. The fixed-cap canonical construction, common-action cap comparison, finite-program full-sequence limit, and velocity/path upgrades are existing infrastructure whose hypotheses still need to be explicitly verified in the final assembly. This note does not independently reproduce those generic proofs. It also does not prove the stronger per-sample/per-layer initial acceleration conclusion from the older two-input contract. That conclusion must be checked separately, and no completed full-contract theorem should be declared on this note alone.
