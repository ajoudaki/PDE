# Direct bounded-control source lemma for large overall gain

This is a new lemma for **phi_a(z)=a(z+atan z)**, a different gain family from the prior convex mixtures. It uses no affine-trajectory comparison. Every current reverse response and both orientations of each initialized Gaussian action are retained.

## 1. Exact normalization and statement

Fix finite hidden depth L>=2 and three RMS-unit inputs. Put rho=a^(-L), K_l=a^(l-1),

    X_l=H_l/a^l, Y_l=Z_l/a^(l-1),
    psi_l(y)=y+K_l^(-1) atan(K_l y).

The raw hidden parameters are unchanged. Initially set the linear time coordinate u=a^L t and retain the ORIGINAL raw readout C. Write s for a general controlled clock; choosing s=u gives the physical residual controls below. The exact controlled equations are

    C'=sum_i c_i X_(L,i),
    V_l'=sum_i c_i d_(l,i) tensor X_(l-1,i), 2<=l<=L,
    w'=sum_i c_i d_(1,i) u_i,
    d_l=psi_l'(Y_l)q_l,
    q_L=C, q_l=A_(l+1)^*d_(l+1),
    Y_l=A_l X_(l-1), X_l=psi_l(Y_l), Y_1=<w,u>.

Actual outputs are f_i=a^L<C,X_(L,i)>. Original GF has c_i=y_i-f_i. The lemma allows ANY deterministic bounded controls ||c(s)||_1<=3.

**Lemma.** The case T=0 is trivial. Let T>0, S=a^(-L)T, and a>=10^8(1+T). Then on [0,S], incoming-field-capped source constructions and their finite Euler programs have strict raw hidden-ball slack, cap/mesh-uniform marginal subGaussian fields, integrable source derivatives, and the explicit actual coefficient box below. The gain condition is independent of L; each width limit still fixes finite L and a first. The displayed source construction has the population initialization C(0)=0. The finite Gaussian readout is retained when applying the width bridge.

The existing finite-depth population bridge therefore gives the strong uncut controlled population flow on this interval. A global original-GF application separately needs an accumulated residual-clock bound. This lemma alone does not assert fitting.

## 2. Primal slack without capped energy

Assume initialized adjacent action norms <=3 and first-layer input projection norms <=2 (these bounds also hold with probability tending to one in the finite Gaussian model). Stop when the joint raw norm of HIDDEN parameter increments reaches one. Then current action norms <=4 and ||Y_1||_2<=3. Since |psi_l(y)|<=2|y|, all forward norms are <=F=8^L.

For smooth clips |tau_R(q)|<=|q|, |tau_R'|<=1 use

    D_(l,R)(z,q)=q+g(K_l z)tau_R(q), g(v)=(1+v^2)^(-1).

Thus |D|<=2|q|. A common normalized incoming cap Rcap corresponds to raw layer-dependent caps a^(L-l)Rcap, because the original raw incoming field at layer l is a^(L-l)q_l. These caps are an approximation scheme for the unchanged raw GF, not a change of metric. Readout integration gives, without energy,

    ||C(s)||_2<=3Fs<=R, R=3FS,
    ||q_(l,i)||_2<=Q_l=8^(L-l)R,
    ||d_(l,i)||_2<=2Q_l.

Each hidden update block has norm <=F R. The joint hidden displacement is therefore <=

    3sqrt(L) F^2 S^2 =3sqrt(L)(64/a^2)^L T^2 <1/4.

This excludes first exit, also at arbitrary finite Euler nodes by summing their step lengths. Under the gain condition, max_l Q_l<=1/2, so max_l ||d_l||_2<=1. Actual preactivation L2 norms are <=F independently of source coefficient bounds.

## 3. Exact local source system

Freeze deterministic source arrays, controls and source covariances. At layer l write

    Y_l=xi_l+mathcalA_l d_l,
    q_l=zeta_l+mathcalB_(l+1) X_l,
    X_l=psi_l(Y_l), d_l=D_(l,R)(Y_l,q_l).

mathcalA_l is strict and mathcalB_(l+1) causal. At the bottom xi_1 is the repeated Gaussian root and mathcalA_1 has blocks h_j Gamma diag(c_j), strict density <=3. At the top zeta_L=0 and mathcalB_(L+1) is the readout integrator with causal row <=3S. Remaining primitive groups are the original jointly centered Gaussian groups, with full second-moment covariances and the named-slot convention if singular.

For an internal initialized matrix the exact coefficients are

    (mathcalA_(l+1,kj))_uv
      =E partial_(zeta_(l,j,v)) X_(l,k,u)
       +h_j c_(j,v) E[X_(l,k,u)X_(l,j,v)], j<k,

    (mathcalB_(l,kj))_uv
      =E partial_(xi_(l,j,v)) d_(l,k,u)
       +1_(j<k)h_j c_(j,v)E[d_(l,k,u)d_(l,j,v)], j<=k.

All current returns are included. Within each time row the order is mathcalA_2,...,mathcalA_L,mathcalB_L,...,mathcalB_2.

Use the induced infinity norm on three-sample blocks and full row sums. Locally assume strict density alpha for mathcalA_l and causal row b for mathcalB_(l+1). Let r=alpha S b.

## 4. Same-array Gaussian-part identity

Write

    r_l=K_l^(-1)atan(K_l Y_l), |r_l|<=pi/(2K_l),
    e_l=g(K_l Y_l)tau_R(q_l), |e_l|<=|q_l|.

Thus X_l=Y_l+r_l and d_l=q_l+e_l. At the SAME actual coefficient arrays put

    Rloc=(I-mathcalA_l mathcalB_(l+1))^(-1),
    U=Rloc mathcalA_l,
    Lloc=(I-mathcalB_(l+1)mathcalA_l)^(-1),
    Y_G=Rloc xi_l+U zeta_l,
    q_G=Lloc zeta_l+mathcalB_(l+1)Rloc xi_l.

These are centered Gaussian combinations of frozen-source groups. Exact elimination gives

    Y_l-Y_G=U e_l+U mathcalB_(l+1)r_l,
    q_l-q_G=mathcalB_(l+1)U e_l+Lloc mathcalB_(l+1)r_l.

For r<=1/8 the two resolvent rows are <=2, |U|row<=2alpha S, and |mathcalB U|row<=2r. Consequently

    ||q_l-q_G||_p<=2r||q_l||_p+pi b/K_l.

The independently proved actual L2 bound implies

    ||q_G||_2<=2Q_l+4b/K_l.

Gaussian moments and absorption give, for p>=2,

    max_i ||q_(l,i)||_p<=20(Q_l+b/K_l)sqrt(p),
    ||K_l max_i|q_(l,i)|||_p<=W_l sqrt(p),
    W_l=60(n_l+b), n_l=K_l Q_l.

The bounded nonlinear remainder pi/(2K_l) compensates the local curvature K_l. No independence between Gaussian and remainder is needed.

Likewise,

    max_i ||Y_(l,i)||_p
      <=[F+50alpha S(Q_l+b/K_l)]sqrt(p).

In the actual box below the bracket is <=2F, so ||X_(l,i)||_p<=4F sqrt(p). These are suprema of marginal norms, not random time maxima.

## 5. Exact source derivatives and coefficient production

With G=diag psi_l'(Y), V=diag partial_q D, N=diag partial_z D,

    ||G||,||V||<=2,
    ||N_k||<=K_l max_i|q_(l,k,i)|.

Any named source Jacobian J of Y obeys exactly

    J=I_xi+mathcalA_l[NJ+V(I_zeta+mathcalB_(l+1)GJ)].

Current mathcalB_(l+1,kk) is retained. Strict mathcalA_l prevents a current algebraic loop. Finite Volterra iteration gives

    ||partial_xi Y_(l,k)||row<=E_k,
    ||partial_(zeta_j)Y_(l,k)||<=2alpha h_j E_k, j<k,
    E_k=exp(4alpha b S
             +alpha sum_(r<k)h_r K_l max_i|q_(l,r,i)|),

    ||partial_xi d_(l,k)||row
      <=(K_l max_i|q_(l,k,i)|+4b)E_k.

The subGaussian criterion and weighted Jensen (no temporal independence) give

    E exp(u|Z|)<=2exp(2 exp(1)M^2u^2)

when ||Z||_p<=M sqrt(p). If alpha S b<=10^(-9) and alpha S W_l<=10^(-6), safe production bounds are

    alpha_(l+1,new)<=3F^2+16alpha,
    b_(l-1,new)<=512(n_l+b)+3S.

For the reverse response, Cauchy--Schwarz bounds its expectation by

    sqrt(2)(sqrt(2)W_l+4b)
       exp(4alpha b S+4exp(1)alpha^2 S^2 W_l^2)
       <512(n_l+b).

The reverse learned contraction is <=3S since ||d_l||_2<=1; the forward learned density is <=3F^2.

## 6. Explicit box uniform over finite depths

For a>=8,

    n_l=3F(T/a)(8/a)^(L-l),
    nmax=3FT/a.

Set

    B0=nmax+3S<=4FT/a,
    alpha_l=32^l *3F^2,
    b_l=2048^(L-l+1)B0, 1<=l<=L.

Here b_l bounds incoming mathcalB_(l+1). Actual top row 3S is strictly inside b_L and bottom density 3 is strictly inside alpha_1.

Keeping every depth factor,

    alpha_l S<=3(2048/a)^L T,
    alpha_l S b_l
      <=24576(1048576/a)^L 64^(-l)T^2/a
      <=384(1048576/a)^L T^2/a.

For a>=10^8(1+T), L>=2,

    alpha_l S<10^(-8),
    alpha_l S b_l<10^(-10),
    alpha_l S W_l<10^(-8).

Indeed n_l<=B0<=b_l/2048, so W_l<=61b_l. All preceding estimates apply and strictly improve the box:

    alpha_(l+1,new)<=3F^2+16alpha_l
                       <=17alpha_l<32alpha_l=alpha_(l+1),
    b_(l-1,new)<=512(n_l+b_l)+3S
                   <514b_l<2048b_l=b_(l-1).

Chronological induction proves the ACTUAL box on every finite mesh. A forward row uses previously constructed reverse history; a reverse row is built after the current higher reverse row. There is no circular radius premise and no smallest-step denominator.

## 7. Population bridge and remaining global obligation

We have strict raw-ball slack, explicit actual source radii, marginal subGaussian incoming fields and integrable formal source derivatives, uniformly in cap and mesh. For fixed finite L and a, Gaussian tails defeat the one-cap-factor comparison exponent, yielding strong cap removal and the canonical controlled population flow. Fixed-cap Gaussian-program, Euler and ordered velocity truncation bridges then apply. For finite-width primal bounds readout integration reads ||C_n(s)||<=||C_n(0)||+3Fs; the extra term tends to zero at fixed L,a,T and must not be erased. Any finite-width assertion must retain actual finite Gaussian readout initialization; this source lemma uses its population limit C(0)=0.

For original GF, put tau=a^(2L)t and v(tau)=integral_0^tau ||y-f(u)||_1 du. In s=rho v, controls are c_i=(y_i-f_i)/||y-f||_1 and have l1 norm one. The lemma applies if v stays <=T. A normalized readout-Gram floor, the consequent bound v(infinity)<=T, and the physical-clock continuation are separate obligations. This source proof itself permits one gain a>=10^8(1+T) for every finite L>=2.
