# Independent audit of the depth-uniform direct source lemma

Audited file: `/tmp/three_depth_source.md`, revised F=8^L version read 2026-09-08. This is an auxiliary candidate for the changed activation family phi_a(z)=a(z+atan z). Permission to replace the exact convex mixture by this family is a separate user-scope issue. No existing theorem file was edited and no experiments were run.

**Verdict: the displayed direct source lemma passes mathematical audit, with the scope and interpretation recorded below. The source author incorporated the clock, cap-scaling, and T=0 clarifications during this audit.** The common sufficient gain a>=10^8(1+T) closes its cap/mesh-uniform source coefficient box for every fixed finite L>=2. This is a bounded-controlled-clock statement. A global GF theorem still requires the normalized Gram floor, accumulated residual budget, and bridge assembly. It does not by itself prove all per-sample/per-layer acceleration conclusions.

## 1. Exact normalization and the original raw metric

Use the source note's X_l=h_l/a^l and Y_l=z_l/a^(l-1), with raw readout C unchanged. Let d_l be the normalized backward field and b_l^raw the original one. Direct backward induction gives

    b_l^raw=a^(L-l+1)d_l.

Indeed this is a*psi_L'(Y_L)C at the top; each preceding raw activation derivative contributes one a. Consequently every raw hidden gradient block has the common factor

    b_l^raw tensor h_(l-1)=a^L d_l tensor X_(l-1),

and the bottom and readout gradients also have factor a^L. Thus, on linear rescaled physical time s_lin=a^L t, the displayed normalized equations are exactly the original raw metric gradient equations for the normalized outputs F_i=<C,X_(L,i)>, driven by c_i=y_i-a^L F_i. No raw parameter or block learning rate is changed.

The subsequent accumulated-residual clock is a DIFFERENT change of time. With tau=a^(2L)t, v(tau)=integral_0^tau ||y-f(u)||_1 du, and s_ctl=a^(-L)v, one has ds_ctl/dt=a^L||y-f||_1 and normalized controls c_i=(y_i-f_i)/||y-f||_1. The same controlled equations apply because their vector field is linear in controls. These two uses of s are mathematically compatible but should be named separately in the final document.

Clipping also matches the intended uncut model. A common normalized clip R in

    d_l=q_l+g(a^(l-1)Y_l)tau_R(q_l)

corresponds to a raw incoming-field clip radius

    R_l^raw=a^(L-l)R.

This uses tau_(bR)(bq)=b tau_R(q) for the usual rescaled smooth clips. Therefore the approximation is not literally a common raw clip radius at all layers; it is a legitimate layer-dependent cap family. For every fixed L and a all raw radii tend to infinity with R, recovering exactly the original uncut raw gradient. The population/GF/GD algorithm is not changed. Generic fixed-cap comparison constants may depend on fixed L and a.

## 2. Independent primal estimate

The normalized layer-by-layer forward bounds are ||X_l||_2<=8^l, starting from ||Y_1||_2<=3, |psi_1|<=2|identity|, and current action norms <=4. The coarser F=8^L bound is valid. With zero population readout and controls of l1 norm <=3,

    ||C(s)||_2<=3Fs,
    ||q_l||_2<=8^(L-l)R, R=3FS.

The hidden block speed assertion needs the layer-specific bound, not merely the coarse bound F. It is valid: for l>=2,

    sum_i |c_i| ||d_(l,i)|| ||X_(l-1,i)||
        <=3*2*8^(L-l)R*8^(l-1)=(3/4)FR<=FR.

For the bottom, 3*2*8^(L-1)R=(3/4)FR<=FR as well. Thus the joint speed is <=sqrt(L)FR. Using R=3FS gives the displayed displacement <=3sqrt(L)F²S²; using the running bound 3Fs would even improve its factor by two. This proves primal slack independently of source coefficients and independently of an invalid capped energy identity.

Under a>=10^8(1+T), L>=2,

    max_l Q_l=3*8^(2L-1)*T/a^L
             =(3/8)(64/a)^L T<1/2,

as claimed. Hence ||d_l||_2<=1 and the learned reverse coefficient row is <=3S.

The revised action-norm premise <=3 and initial projection norms <=2 hold with probability tending to one at fixed finite L. Finite Euler meshes of the canonical source construction satisfy the audited primal estimates directly. For actual finite readout initialization, one must add ||C_n(0)|| to the readout estimate, as the revised source note now explicitly does; the vanishing finite term is transferred by the fixed-L bridge.

## 3. Same-array Gaussian-part moments

The algebraic identities are exact. Put A=mathcalA_l, B=mathcalB_(l+1), h=K_l^-1 atan(K_lY), and e=g(K_lY)tau_R(q). Then

    Y=xi+Aq+Ae, q=zeta+BY+Bh.

Eliminating Y or q gives precisely

    Y-Y_G=Ue+UBh,
    q-q_G=BUe+Lloc Bh.

Because A is strict and B causal, both AB and BA are strict. Their inverses are finite Volterra polynomials at each finite mesh. If r=alpha S b<=1/8, the norm-series bound gives both resolvent rows <=8/7<2, ||U||row<=2alpha S, and ||BU||row<=2r.

The source arrays and covariances are deterministic when the formal derivatives and Gaussian combinations are formed. Thus Y_G and q_G are jointly centered Gaussian even though the nonlinear remainders depend on them and the forward/reverse sources have their prescribed correlations. Neither fresh initialization nor independence of the remainders is being used.

The pointwise bounded remainder |h|<=pi/(2K_l) yields

    ||q-q_G||_p<=2r||q||_p+pi b/K_l.

The ACTUAL primal L2 bound from the preceding section therefore gives

    ||q_G||_2<=(1+2r)Q_l+pi b/K_l<=2Q_l+4b/K_l.

Gaussian moments and absorption by 1-2r>=3/4 imply the stated safe bound

    ||q||_p<=20(Q_l+b/K_l)sqrt(p).

Multiplying the sum of the three sample norms by K_l gives W_l=60(K_lQ_l+b). This compensation by the forward nonlinear amplitude 1/K_l is the central valid step; replacing it by the crude source moment scale O(b) would lose the uniform-depth conclusion.

For Y, the same identity and actual ||Y||_2<=F give a Gaussian-part bound F+2alpha S Q_l+pi r/K_l. Adding its nonlinear remainder and the preceding q bound gives coefficients <=42 on alpha S Q_l and <46 on alpha S b/K_l. Thus the note's coefficient 50 is sufficient.

## 4. Exact source derivative rows

For frozen arrays,

    J=I_xi+A[NJ+V(I_zeta+BGJ)]

is exact. The multiplier bounds are ||G||,||V||<=2 and ||N_k||<=K_l max_i|q_(l,k,i)|. Current B_kk appears in BGJ and has not been discarded. Since A is strict, no current implicit loop is introduced.

After summing source blocks, the nonlocal term obeys

    sum_v ||B_rv|| ||G_v|| ||J_v|| <=2b max_(v<=r)||J_v||.

The remaining V costs another factor two. Scalar discrete Gronwall therefore yields exactly the exponent

    4alpha b S + alpha sum_(r<k)h_r K_l max_i|q_(l,r,i)|.

The zeta injection contributes 2alpha h_j, and the xi injection is an identity row. At the reverse output, its leading multiplier is K_l max_i|q_(l,k,i)|+4b. This proves all three derivative envelopes in the source note. It uses an integral of marginal fields, not a random maximum over mesh times.

Weighted Jensen and the stated subGaussian moment inequality apply without temporal independence. Cauchy--Schwarz yields exactly the displayed reverse bound

    sqrt(2)(sqrt(2)W_l+4b)
       exp(4alpha b S+4e alpha²S²W_l²).

Under the note's restrictions this is far below 512(n_l+b): its prefactor is at most 126(n_l+b), and its exponent is below 5*10^-9. The forward production bound 3F²+16alpha is also conservative: the expected derivative term is below 6alpha. Learned coefficient terms are correctly bounded using ||c||_1<=3, not by three separate unconstrained controls.

## 5. Checked depth-dependent arithmetic

The exact quantities are

    n_l=3F(T/a)(8/a)^(L-l), B0=nmax+3S<=4FT/a,
    alpha_l=3*32^l*64^L,
    b_l=2048^(L-l+1)B0.

Then

    alpha_l S<=3(2048/a)^L T,
    alpha_l S b_l
      <=24576(1048576/a)^L 64^(-l)T²/a.

The constants 1048576=64*2048*8 and 24576=3*4*2048 are correct. Taking l>=1 gives the note's factor 384. At the worst possible depth L=2,

    alpha_l S < 1.26*10^-9 T/(1+T)^2 <10^-8,
    alpha_l S b_l
      <4.23*10^-10 T²/(1+T)^3 <=6.27*10^-11 <10^-10.

Higher depths reduce these bounds because 1048576/a<0.0105. Since n_l<=B0<=b_l/2048,

    W_l<=61b_l,
    alpha_l S W_l<3.83*10^-9<10^-8.

All source derivative conditions therefore hold with strict slack. The Y-moment bracket is <=2F because alpha S(Q_l+b/K_l)<=alpha S b_l(1+1/2048)/K_l and the last displayed product is tiny.

Forward production improves alpha_(l+1) because 3F²<=alpha_l and

    3F²+16alpha_l<=17alpha_l<32alpha_l.

Reverse production improves the next lower row because n_l<=b_l/2048 and 3S<=B0<=b_l/2048:

    512(n_l+b_l)+3S<514b_l<2048b_l.

The top fixed row and bottom fixed density start inside their boxes when T>0. When T=0 the interval is trivial; the phrase “strictly inside” should not be applied to the resulting zero reverse radii.

## 6. Noncircularity and scope

Chronological induction is valid. A new forward row only uses previously constructed backward fields in its strict update and is built in ascending layer order. At the current backward stage, the top readout row is already known, and descending layer order supplies each current higher reverse row before the next one is needed. Thus all production estimates can be applied with known preceding rows; there is no hidden simultaneous coefficient fixed point.

For merely measurable bounded controls, the population limit should be stated as a strong absolutely continuous controlled solution, using L1 approximations of the controls (for example interval averages). Arbitrary node sampling of an arbitrary measurable control need not converge to that control. Actual physical GF residual controls are continuous on the constructed path, and yield the intended strong C1 physical solution once the global budget argument is assembled.

This audit proves no global Gram floor or residual budget. It supports using the source lemma as the missing analytic component of a global large-gain theorem, with one sufficient gain constant independent of finite L. It does not authorize substituting that activation for the exact convex-mixture question, nor does it settle an optimal gain exponent.
