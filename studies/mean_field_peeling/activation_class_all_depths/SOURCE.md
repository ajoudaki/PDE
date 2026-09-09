# Part S. Direct controlled source estimates at all finite depths

Let psi be C2 with ||psi||infty, ||psi'||infty, ||psi''||infty <= 1. Nonconstancy is not required for this lemma. Let L>=2, 0<=e<=1, T>0, and

    a >= 10^12(1+T),   S = T a^(-L),   K_l = a^(l-1),   eps=e/a.

Use the ORIGINAL raw parameters and metric. Normalize only hidden fields:

    Y_l = z_l/a^(l-1),   X_l = h_l/a^l,
    chi_l(y) = y + [1+eps psi(K_l y)]/K_l,
    F_i = <C,X_(L,i)>,   f_i=a^L F_i.

Thus Y_l=A_l X_(l-1), with the normalized first-layer representation Y_(1,i)=<w,u_i>, ||u_i||=1. For deterministic bounded controls ||c(s)||_1<=3, the normalized controlled raw field is

    C'=sum_i c_i X_(L,i),
    A_l'=sum_i c_i d_(l,i) tensor X_(l-1,i)  (2<=l<=L),
    w'=sum_i c_i d_(1,i)u_i,
    q_L=C,   q_l=A_(l+1)^* d_(l+1),
    d_l=D_(l,R)(Y_l,q_l),
    D_(l,R)(y,q)=q+eps psi'(K_l y) tau_R(q).

The clip is C1, |tau_R(q)|<=min(|q|,2R), |tau_R'|<=1, and equals q for |q|<=R. All constants below are uniform over R, positive Euler meshes of total length <=S, and deterministic choices of controls satisfying the displayed bound. Population initialization is C(0)=0. The actual finite-width random readout must be retained before the fixed-cap bridge, as explained at the end.

The bounds used are exactly

    |chi_l(y)-y|<=2/K_l,  |chi_l'|<=2,
    |D(y,q)|<=2|q|,  |D_q|<=2,
    |D_y|<=eps K_l |q|<=K_l |q|,
    |D_y|<=2 eps K_l R.

In particular psi' and psi'' may change sign.

## S.1. Exact finite-program input and local equations

The input theorem required from Part F is this: a fixed finite program built from independent normalized Gaussian adjacent matrices, both orientations of each matrix, independent Gaussian roots, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has a canonical scalar Gaussian-source law. A forward answer on input h equals its centered source plus earlier reverse inputs multiplied by their expected named-source derivatives of h. The reverse rule interchanges the two sides and includes current forward calls. Each source covariance is the FULL uncentered input Gram. Distinct oriented Gaussian source groups are independent. Named derivatives freeze all source covariances, scalar contractions, previously produced response coefficients, meshes, and controls; named slots stay distinct at singular covariance. These are the source identities (F.9)--(F.10) and Lemma F.4 proved in Part F above. Fixed caps satisfy all of its coordinate hypotheses because psi is C2 and the four displayed gate derivative bounds hold.

Apply this input chronologically to one finite Euler program. At layer l the exact local equations are

    Y_l = xi_l + Acal_l d_l,
    q_l = zeta_l + Bcal_(l+1) X_l,
    X_l = chi_l(Y_l),   d_l = D_(l,R)(Y_l,q_l).

Here Acal_l is strictly lower triangular in time and Bcal_(l+1) is lower triangular, including its diagonal. At the bottom xi_1 is the repeated initialized Gaussian root and

    Acal_(1,kj)=h_j Gamma diag(c_j),   j<k.

At the top zeta_L=0 and Bcal_(L+1) is the strictly past readout integrator, replicated over the three samples. Its full block-row norm is <=3S.

For internal matrices the exact response coefficients, with sample indices u,v, are

    (Acal_(l+1,kj))_(uv)
       = E partial_(zeta_(l,j,v)) X_(l,k,u)
         + h_j c_(j,v) E[X_(l,k,u) X_(l,j,v)] ,  j<k,

    (Bcal_(l,kj))_(uv)
       = E partial_(xi_(l,j,v)) d_(l,k,u)
         + 1_(j<k) h_j c_(j,v) E[d_(l,k,u) d_(l,j,v)] ,  j<=k.

The learned contractions follow by unrolling the rank-one parameter increments. The response terms are the source rule just stated. These identities hold at the actual coefficient arrays; no comparison covariance or replacement transpose law is introduced.

For a three-by-three block use its induced infinity norm. For a row use the SUM of its block norms. Write a local strict density bound as |Acal_(l,kj)|<=alpha h_j, and a full causal row bound as sum_(j<=k)|Bcal_(l+1,kj)|<=b. Set r=alpha S b.

## S.2. Independent primal bounds

Use initialized adjacent action norms <=10 and initial first-layer projection norms <=2. These bounds follow from the elementary net argument proved in Part F: a one-quarter net on each unit sphere has cardinality at most 9^n, and the net approximation gives ||W||op <= 2 max_(u,v in nets)|u^T Wv|. Since every fixed bilinear form is N(0,1/n), P(||W||op>10)<=2*9^(2n)*exp(-100n/8), which tends to zero. A finite union bound handles all L-1 matrices, the Gaussian law of large numbers handles the three first-layer projection norms, and passage on a countable dense generated family gives the canonical norm bound 10. No precise asymptotic spectral-norm theorem is required. Stop at hidden joint raw displacement D=1. Then current adjacent action norms are <=11 and ||Y_(1,i)||_2<=3. Put F=32^L. The offset causes no problem:

    ||X_(1,i)||_2<=3+2=5<=32,
    ||X_(l,i)||_2<=11*32^(l-1)+2<=32^l.

Consequently, for s<=S and at every Euler node,

    ||C(s)||_2<=3Fs,
    ||q_(l,i)(s)||_2<=Q_l := 32^(L-l) 3FS,
    ||d_(l,i)(s)||_2<=2Q_l,
    ||Y_(l,i)(s)||_2<=F.

Every hidden block speed is <=F||C||_2: for an internal block, the coefficient bound is 3*2*32^(L-l)*32^(l-1)=(3/16)F; the bottom is the same. Thus

    D(s)<=3 sqrt(L) F^2 s^2.

For Euler, sum_j h_j s_j <=s_k^2/2 supplies the same bound and excludes even a first overshooting node: the proposed node's update length only uses earlier states inside the stop. With a>=10^12(1+T),

    D(S)<=3 sqrt(L) (1024/a^2)^L T^2 <1/4,
    max_l Q_l <1/2.

Hence the stop is never reached and ||d_l||_2<=1. These bounds are independent of source coefficient estimates; they may be used inside a chronological source induction without circularity.

## S.3. Same-array Gaussian-part estimate, including the offset

Freeze one actual finite local prefix whose coefficient rows obey alpha,b. Write

    u_l = [1+eps psi(K_l Y_l)]/K_l,  |u_l|<=2/K_l,
    v_l = eps psi'(K_l Y_l) tau_R(q_l),  |v_l|<=|q_l|.

Then X=Y+u and d=q+v. Assume r<=1/8 and put

    Rloc=(I-Acal Bcal)^(-1),   U=Rloc Acal,
    Lloc=(I-Bcal Acal)^(-1),
    Y_G=Rloc xi + U zeta,
    q_G=Lloc zeta + Bcal Rloc xi.

These are centered Gaussian combinations of the original frozen source groups. Triangular inverses exist exactly; the geometric row bounds also give

    |Rloc|row, |Lloc|row<=2,
    |U|row<=2alpha S,   |Bcal U|row<=2r,
    |Lloc Bcal|row<=2b.

Exact elimination, with NO replacement of the actual coefficient arrays, yields

    Y-Y_G = U v + U Bcal u,
    q-q_G = Bcal U v + Lloc Bcal u.

Let m_p(q)=max_(k,i)||q_(k,i)||_p on this finite prefix. It is finite before absorption, since fixed-cap finite programs are finite globally Lipschitz Gaussian expressions. The identities imply

    m_p(q-q_G)<=2r m_p(q)+4b/K_l,
    m_2(q_G)<=(1+2r)Q_l+4b/K_l<=2Q_l+4b/K_l.

Each q_G coordinate is Gaussian with its ACTUAL covariance, so ||q_G||_p<=sqrt(p)||q_G||_2 for p>=2. Absorb 2r m_p(q), retaining the bounded non-Gaussian remainder, to obtain

    m_p(q)<=20(Q_l+b/K_l)sqrt(p),   p>=2.                 (S.1)

For the local curvature multiplier N_k=K_l max_i|q_(k,i)| this gives

    ||N_k||_p <= W_l sqrt(p),
    W_l=60(n_l+b),   n_l=K_l Q_l.                       (S.2)

The factor 3 in W_l merely bounds the norm of the maximum by the sum of the three marginal norms. No random time maximum is used.

The other exact identity and the independent actual bound ||Y||_2<=F likewise give

    max_(k,i)||Y_(k,i)||_p
        <=[F+50alpha S(Q_l+b/K_l)]sqrt(p).               (S.3)

Indeed ||Y-Y_G||_p<=2alpha S m_p(q)+4alpha S b/K_l; use this at p=2 to bound the Gaussian variance by F+2alpha S Q_l+4alpha S b/K_l and then use (S.1). The coefficient 50 exceeds the resulting coefficients 42 for Q_l and 44+4/sqrt(2) for b/K_l. In the box below the bracket is <=2F, hence ||X_(k,i)||_p<=4F sqrt(p).

This calculation isolates why the offset is harmless: its size is 1/K_l, exactly the inverse scale of the possible curvature K_l. The remainder estimate 4b/K_l therefore gives the displayed constants 20 and 60.

## S.4. Derivative rows and production bounds

Set G=diag chi_l'(Y), V=diag D_q(Y,q), and N=diag D_y(Y,q). Their norms obey |G|,|V|<=2 and |N_k|<=K_l max_i|q_(k,i)|. For any named source, the exact Y-Jacobian satisfies

    J=I_xi + Acal [N J + V(I_zeta+Bcal G J)].

The current Bcal diagonal remains in this identity. Strictness of Acal ensures that J at time k depends on this bracket only at strictly earlier times.

Let E_k denote

    E_k=exp[4alpha b S + alpha sum_(r<k)h_r K_l max_i|q_(r,i)|].

For derivatives in the full xi row, take block-row norms in the exact recurrence and let M_j be the running maximum of preceding Jacobian row norms. This gives

    |J_k|row <=1+alpha sum_(j<k) h_j (N_j+4b) M_j.

The discrete product bound product_(j<k)[1+alpha h_j(N_j+4b)]<=E_k proves

    |partial_xi Y_k|row<=E_k.

For one reverse source slot zeta_j, its direct forcing of d_j is bounded by 2, its first effect on Y_k by 2alpha h_j, and all later effects obey the same Volterra recurrence. Therefore

    |partial_(zeta_j)Y_k|<=2alpha h_j E_k,   j<k,
    |partial_(zeta_j)X_k|<=4alpha h_j E_k,
    |partial_xi d_k|row<=(K_l max_i|q_(k,i)|+4b)E_k.     (S.4)

These are pointwise bounds on actual named derivatives.

For completeness, if ||Z||_p<=M sqrt(p) for all p>=2, expansion of exp(Z^2/(4 exp(1)M^2)) and k!>=(k/exp(1))^k gives expectation <=2. Young's inequality then gives, in particular,

    E exp(u|Z|)<=2 exp(2 exp(1)M^2 u^2),   u>=0.

Minkowski applied to the weighted time sum in E_k gives its p-norm <=S W_l sqrt(p). Hence no temporal independence or path-maximum moment is needed. If

    alpha S b<=10^-9,   alpha S W_l<=10^-6,

then

    E E_k <=4,
    [E E_k^2]^(1/2)
      <=sqrt(2) exp[4alpha b S+4 exp(1)alpha^2 S^2 W_l^2].

Taking expectations in (S.4) and adding the learned contractions yields

    alpha_(l+1,new)<=3F^2+16alpha,
    b_(l-1,new)<=512(n_l+b)+3S.                          (S.5)

For the second bound the response row is at most

    sqrt(2)(sqrt(2)W_l+4b)
       exp[4alpha b S+4 exp(1)alpha^2 S^2 W_l^2]
       <512(n_l+b).

The forward learned density is <=3F^2. The reverse learned row is <=3S because ||d_l||_2<=1. All displayed norms bound the absolute values of signed response coefficients; no coefficient signs have been discarded from the actual identities.

## S.5. Explicit depth-independent gain condition

Keep F=32^L and define

    n_l=3F(T/a)(32/a)^(L-l),   nmax=3FT/a,
    B0=nmax+3S<=4FT/a,
    alpha_l=32^l *3F^2,
    b_l=2048^(L-l+1) B0,   1<=l<=L.

Here alpha_l bounds Acal_l and b_l bounds the incoming Bcal_(l+1), so outgoing reverse production at layer l is compared with b_(l-1). The top row 3S and bottom density 3 lie strictly inside their respective radii. Exact algebra gives

    alpha_l S<=3(32768/a)^L T,
    alpha_l S b_l
       <=24576(67108864/a)^L 64^(-l) T^2/a
       <=384(67108864/a)^L T^2/a.

Since a>=10^12(1+T), L>=2, and l>=1, these imply

    alpha_l S<10^-8,
    alpha_l S b_l<10^-10,
    alpha_l S W_l<10^-8.

For the second assertion one may bound by the L=2 case and use sup_(T>=0)T^2/(1+T)^3=4/27: the bound is <2.57*10^-19. Also n_l<=B0<=b_l/2048, so W_l<=61b_l and the last assertion follows. The forward bracket in (S.3) is <=F+25alpha_l S+50alpha_l S b_l<=2F, because Q_l<=1/2 and K_l>=1.

Thus every production estimate is strictly inside the next box:

    3F^2+16alpha_l<=17alpha_l<32alpha_l=alpha_(l+1),
    512(n_l+b_l)+3S<514b_l<2048b_l=b_(l-1).              (S.6)

The constants do not require any upper bound on L, and e enters only through eps=e/a<=1.

## S.6. Full chronological induction, without an unknown-current-row premise

Use the actual stage order at each time k:

    Acal_(2,k),...,Acal_(L,k),
    Bcal_(L,k),...,Bcal_(2,k).

The induction invariant is: every completed time row satisfies its alpha_l,b_l radius; its corresponding q_l fields satisfy (S.1)--(S.2); and the independent primal bounds of Section S.2 hold. At a partially completed current row, the radius bound is asserted only for coefficients already constructed.

At k=0 all forward response rows are empty. C_0=0, so the top backward field and its xi-derivative vanish. Thus Bcal_(L,0)=0, and successive reverse stages give zero current q and reverse responses down to layer 1. Named zero-variance slots are still retained formally. This starts the invariant.

At the next time k, the bottom Y_1,k is already determined by the initialized root and past d_1. Suppose current forward rows have been built through Acal_(l,k), so Y_l,k and X_l,k are available. To construct Acal_(l+1,k), the response derivative of X_l,k in zeta_l,j with j<k uses q_l,r and Bcal_(l+1,r) ONLY FOR r<k. This is an exact consequence of strictness of Acal_l: every occurrence of q in Y_l,k comes through d_l,r with r<k. Apply the local moment estimate to the fully completed prefix through k-1, then apply the source derivative recurrence at current k. The bound 4alpha_l h_j E_k and its expectation require only this past information. The learned contraction uses the already proved primal bounds. Consequently the first estimate of (S.5) constructs Acal_(l+1,k) strictly inside alpha_(l+1). No current Bcal_(l+1,k), q_l,k, or d_l,k estimate has been used. This closes all current forward rows in ascending order.

The current top incoming row is the readout integrator, already bounded by 3S. The current top q_L=C is now available. On the complete local prefix through k, all Acal_L and incoming Bcal_(L+1) rows are therefore known and satisfy their bounds. Sections S.3--S.4 now apply to this prefix and produce Bcal_(L,k) strictly inside b_(L-1). The current q_(L-1) is then available with this newly bounded incoming row. The same complete-prefix calculation produces Bcal_(L-1,k). Continue downward. At every reverse stage, the current Acal_l row was constructed in the forward sweep, and the current incoming Bcal_(l+1) row was constructed in the preceding higher reverse stage. Therefore every hypothesis is established before it is used. The final bottom q_1 estimate completes the invariant.

This proves the actual coefficient box and moment estimates on every finite mesh. It uses no minimum step length and never bootstraps a current unknown row from an estimate that assumes that row.

## S.7. What this gives to the global proof

For every separately fixed finite L,a,T, the constructed incoming and forward fields have marginal subGaussian moments uniformly in mesh, cap, and the bounded deterministic controls. Their formal first source derivatives have integrable envelopes uniformly in mesh and cap. The elementary subGaussian tail consequence of (S.1) supplies constants M,c>0, possibly depending on the fixed L,a,T, such that

    sup_(R,k) ||q_(l,k,i) 1_(|q_(l,k,i)|>u)||_2
        <=M exp(-c u^2).

The fixed-cap Gaussian/Euler bridge passes these estimates to controlled capped population paths. Comparing an arbitrary larger cap with a reference cap R uses

    |D_(l,R')(y,q)-D_(l,R)(y',q')|
       <=2|q-q'|+2eps K_l R|y-y'|
                         +2eps |q'|1_(|q'|>R).

Forward discrepancies are controlled first. Backward substitution therefore introduces one factor R multiplying that forward discrepancy; it does not produce R^L. On any fixed controlled interval the raw difference estimate has the form C exp(CR-cR^2). It yields strong cap removal and uniqueness against any bounded-primal uncut competitor, as proved in full in Part V below. Measurable controls give a strong absolutely continuous controlled path and the equation almost everywhere; continuous autonomous residual feedback gives the required strong C1 physical path.

The finite random readout is not set to zero in either actual training algorithm: at fixed cap its initial RMS discrepancy is O_P(n^-1), propagated by fixed-cap raw Lipschitz stability. Only after this width limit is the population initialization C_0=0 used. The finite-depth true-kernel/velocity/path conclusions still require their ordered observation-truncation and time-compactness bridge, as proved in Part V below; the present source calculation does not silently replace that bridge.

