# Canonical Gaussian probe: initial self-return sign

Status: exact finite-width derivative jets and a conditional sign for their principal self-site contribution. No finite-time remainder estimate or global response bound is asserted.

Use normalized vector norms ||v||n=||v||Euclidean/sqrt(n). All fields below without a time argument are evaluated at the prescribed zero-readout initialization. Set

    d0=D3 H3,  E3=diag(D3^2+H3 phi''(z3)),
    m1=||H1||n^2,  m2=||H2||n^2,
    A0=m1 I+W2 D1^2 W2^T,
    B0=m1 I+W2 W2^T.

Fix a middle neuron i and an independent standard Gaussian top-space probe xi. Differentiate the FULL trained trajectory under initial perturbation K=xi e_i^T/sqrt(n) of W3_0. With the notation of ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md, x,A,B,c denote variations of X1,W2,W3-W3_0,C, and

    zeta2=A H1+W2 D1^2 x,      gamma2=A H1+W2 x.

Their initial jets are exactly

    c'(0)=D3 K H2,
    delta_dot'(0)=D2 r,
    r=e_i(xi^T d0/sqrt(n))
        +H2_i W3^T E3 xi/sqrt(n),
    zeta2''(0)=A0 D2 r,
    gamma2''(0)=B0 D2 r.                               (1)

Indeed C(0)=0, all hidden trained velocities vanish initially, C'(0)=H3, and d_dot'(0)=E3 K H2. Differentiating the remaining trained equations gives (1); the actual bulk input is varied throughout.

On the initial operator-bound event, the Gaussian coefficient vector of the second summand of zeta2_i''(0), and likewise gamma2_i''(0), has ordinary Euclidean norm O(n^(-1/2)). The first summands therefore give

    E_xi[gamma2_i''(0) zeta2_i''(0)]
      =(B0)_ii(A0)_ii D2_i^2 ||d0||n^2
         +O_M(n^(-1/2)).                                (2)

If Gamma_(i,j)=n E_xi[gamma2_j zeta2_j], then, for each fixed n,

    lim_(s downarrow 0) 4 Gamma_(i,i)(s)/(n s^4)
       =E_xi[gamma2_i''(0) zeta2_i''(0)].               (3)

This is a localized covariance coefficient. It is NOT a counterexample to a uniform finite-time estimate ||Gamma_i(s)||n<=C Lambda_i(s): the full tangent energy Lambda_i=n E_xi||y||^2 has

    Lambda_i(s)
       =s^2 H2_i^2 <D3^2>_n+o_n(s^2),                 (4)

because c'(0) is nonzero. No width-uniform Taylor remainder needed to select s=s_n has been established.

There is a favorable sign in the actual Gaussian law. Condition ONLY on the lower initialization and the initial forward vector z3=W3_0 H2. Gaussian conditioning of each row yields

    E[q_i'(0) | lower initialization,z3]
       =(H2_i/m2)<z3,D3 H3>_n.                         (5)

This conditioning does not additionally include an operator-norm event. The scalar <z3,D3 H3>_n is nonnegative, and m2>0 almost surely.

The principal self-site contribution to the s^5 coefficient of
<phi''(z2(s))q2(s),Gamma_i(s)>_n is one quarter of

    X_i=(B0)_ii(A0)_ii D2_i^2
             phi''(z2_i) q_i'(0) ||d0||n^2.

Every factor other than q_i'(0) is measurable under the conditioning in (5), so

    E[X_i | lower initialization,z3]
      =(B0)_ii(A0)_ii D2_i^2
         [phi''(z2_i)H2_i/m2]
         ||d0||n^2 <z3,D3 H3>_n
      <=0,                                             (6)

using arctangent's phi''(z)phi(z)<=0. Multiplication by the leading nonnegative coefficient of Lambda_i^(r-1), for any r>=1, preserves this conditional sign by (4).

The sign in (6) concerns the principal initial self-return only. It does not include off-site terms, their mixed second responses, or a positive-time sign assertion. The narrow next target is to preserve/resum this own-site cancellation while controlling the actual off-site, two-time mixed-response contraction. Neither bounded operator norms nor the rare self-block lemma alone provides that estimate.

