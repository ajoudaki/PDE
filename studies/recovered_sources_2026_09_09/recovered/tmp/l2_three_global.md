# L=2, three inputs: exact source system and the unresolved global continuation step

This is a theory-only route audit. The conclusion is **not a complete theorem**: a single initialized adjacent action removes the middle-layer response equation, but it does not remove the forward/reverse past-response loop. I can prove an explicit conditional subGaussian/source-derivative estimate without any small-affine-trajectory comparison. Energy alone does not close its hypotheses. Consequently this route currently supplies no polynomial threshold for the full global population/GF/raw-GD contract.

## 1. Contract and exact raw energy bounds

There are exactly two hidden layers, three deterministic RMS-unit inputs, no biases, activation phi(z)=a z+e atan(z), a=1-e, 0<e<=1/2, and the original raw metric. Put u_i=x_i/sqrt(d), Gamma_ij=<u_i,u_j>. The first-layer parameter can be represented by a Gaussian row root w with z_i=<w,u_i>. There are two separate canonical neuron Hilbert spaces, one bounded initialized action A_0:H_1->H_2 and its genuine adjoint, a learned Hilbert--Schmidt increment V, A=A_0+V, and a readout C in H_2. Population C(0)=0. The actual finite Gaussian C_n(0)~N(0,n^-2) is retained in any finite-network assertion.

Write h_i=phi(z_i), Z_i=A h_i, H_i=phi(Z_i), b_i=phi'(Z_i)C, q_i=A^*b_i, and d_i=phi'(z_i)q_i. With c_i=y_i-f_i=-r_i, the exact physical equations are

    wdot = sum_i c_i d_i u_i,
    Vdot = sum_i c_i b_i tensor h_i,
    Cdot = sum_i c_i H_i,
    f_i = <C,H_i>.

The tensor convention is (b tensor h)v=b<h,v>. These are precisely the original raw equations, not a different metric.

For any already-existing classical GF, the scalar chain rule and genuine adjoint imply

    Ldot = -||Thetadot||_raw^2.

At the population initialization L(0)=3/2. Therefore on [0,T],

    ||Theta(t)-Theta(0)||_raw <= R_T := sqrt(3T/2),
    ||c(t)||_1 <= 3,
    ||C(t)||_2 <= R_T,
    ||z_i(t)||_2 <= 1+R_T,
    ||h_i(t)||_2 <= 1+R_T,
    ||A(t)|| <= ||A_0||+R_T.

The first-layer bound uses ||u_i||=1; |phi(z)|<=|z| and |phi'|<=1. In particular ||b_i||_2<=R_T and ||q_i||_2<=(||A_0||+R_T)R_T. No inverse of Gamma is used. A finite terminal-time strong endpoint follows because the energy integral on a shrinking time interval tends to zero and Cauchy--Schwarz controls the raw displacement.

Every finite-width true GF is global: its smooth finite-dimensional vector field has a bounded raw parameter path on every finite interval by the same energy argument. Its initial loss and readout are random, rather than replaced by their limiting values. The standard finite-dimensional continuation argument applies for each fixed width. This does not construct the canonical population flow.

## 2. Exact chronological source skeleton

The following is the L=2 specialization of the finite-query Gaussian construction in the supplied report, R.2. Work first on a finite explicit Euler mesh t_k with h_k=t_{k+1}-t_k. Freeze all deterministic residual controls c_{k,i}, Gram contractions, response coefficients, and source covariances in formal source derivatives. For bounded incoming-field caps the supplied finite-program theorem applies directly. Uncut identities require justified removal of the caps; they are not assumed as an independently established population construction.

Let g(z)=(1+z^2)^-1. A cap may be written

    D_R(z,q)=a q+e g(z) tau_R(q),

where |tau_R(q)|<=|q| and |tau_R'|<=1. The uncut gate is D(z,q)=phi'(z)q. Use d_k=D_R(z_k,q_k), b_k=D_R(Z_k,C_k 1). The exact source equations are

    z_k = z_0 + sum_{r<k} h_r Gamma diag(c_r) d_r,
    h_k = phi(z_k),
    q_k = zeta_k + sum_{v<=k} B_{kv} h_v,

    Z_k = xi_k + sum_{r<k} A_{kr} b_r,
    H_k = phi(Z_k),
    C_k = sum_{r<k} h_r c_r^T H_r.

Here A_{kr}, B_{kv} are 3x3 sample matrices; the source coefficient A is unrelated to the raw adjacent action A above except through the stated formulas. Its strictly past convention prevents an algebraic current forward loop. The primitive centered Gaussian groups are z_0, xi, zeta, independent as groups, with

    E z_0 z_0^T = Gamma,
    E[xi_{k,i}xi_{r,j}] = E[h_{k,i}h_{r,j}],
    E[zeta_{k,i}zeta_{r,j}] = E[b_{k,i}b_{r,j}].

All temporal and sample correlations within each group are retained, including singular covariance. The exact coefficients are

    (A_{kr})_{ij}
       = E partial_{zeta_{r,j}} h_{k,i}
         + h_r c_{r,j} E[h_{k,i}h_{r,j}],             r<k,

    (B_{kr})_{ij}
       = E partial_{xi_{r,j}} b_{k,i}
         + 1_{r<k} h_r c_{r,j} E[b_{k,i}b_{r,j}],    r<=k.

The current return is retained:

    B_{kk}=diag E[e g'(Z_{k,i})tau_R(C_k)].

In the uncut case this is diag E[phi''(Z_{k,i})C_k]. Since |g'|<=1,

    ||B_{kk}||_infty <= e ||C_k||_2.

Thus energy controls this current return. It does not control the strictly past response row in the same way.

The row construction order is A_k, then the top forward quantities, then B_k, then the bottom reverse gate and raw update. The same initialized Gaussian matrix is queried in both orientations; neither q nor the reverse answer is declared independent of the forward features.

## 3. Exact derivative equations: what survives at L=2

Write G=diag phi'(z), V=diag partial_q D_R, N=diag partial_z D_R, using the appropriate layer's variables. Their norm bounds are

    ||G||, ||V|| <= 1,
    ||N|| <= e |incoming field|_infty.

For the bottom source Jacobian J_{k,j}=partial_{zeta_j} z_k,

    J_{k,j} = sum_{r<k} h_r Gamma diag(c_r)
      [ N^1_r J_{r,j}
        + V^1_r (1_{r=j} I + sum_{v<=r} B_{rv} G^1_v J_{v,j}) ].

For the top forward-source Jacobian U_{k,j}=partial_{xi_j} Z_k and readout Jacobian T_{k,j}=partial_{xi_j} C_k,

    U_{k,j} = 1_{k=j} I
      + sum_{r<k} A_{kr}[N^2_r U_{r,j}+V^2_r 1 T_{r,j}],

    T_{k,j} = sum_{r<k} h_r c_r^T G^2_r U_{r,j}.

The backward source derivative feeding B is exactly

    partial_{xi_j} b_k = N^2_k U_{k,j}+V^2_k 1 T_{k,j}.

There is no middle-layer equation. Nevertheless the coefficient dependence remains

    A <- bottom response depending on B,
    B <- top response depending on A.

Both N^1=e g'(z)tau_R(q) and N^2=e g'(Z)tau_R(C) occur. The top readout integral does not eliminate N^2. Removing the current B return, freezing A_0 as a fresh matrix at later times, or replacing these expected derivatives by derivatives of expected scalar fields would change the actual source system.

## 4. A proved conditional moment and derivative bound without affine comparison

Use the induced infinity norm for sample matrices, maximum over the three component L^p norms for vectors, and sum of block norms for causal rows. Suppose on a fixed mesh prefix contained in [0,T] that

    ||c_k||_1<=3,
    max_i ||h_{k,i}||_2<=B_1,
    ||C_k||_2<=R,
    ||A_{kr}||_infty <= alpha h_r   (r<k),
    sum_{r<=k} ||B_{kr}||_infty <= beta.

The source variances are then bounded by B_1^2 and R^2. This premise is cap/mesh uniform if its constants are, but is not asserted to follow from the energy bound. To cover maxima of Gaussian sample components and keep constants conservative, define

    U_1 = (6+18RT) exp(3 beta T),
    U_2 = 6 B_1 exp(3 alpha T^2),
    M_q = 6R+beta U_1,
    M_C = 3T U_2.

Then for every p>=2,

    max_{k,i} ||h_{k,i}||_p <= U_1 sqrt(p),
    max_{k,i} ||Z_{k,i}||_p <= U_2 sqrt(p),
    max_{k,i} ||q_{k,i}||_p <= M_q sqrt(p),
    max_k ||C_k||_p <= M_C sqrt(p).

Proof: use |phi|<=|identity|, |D_R|<=|incoming field|, the Gaussian L^p bound, and Minkowski in the source equations. The bottom inequality is

    ||z_k||_p <= 6sqrt(p)+3 sum_{r<k}h_r
                   [6R sqrt(p)+beta max_{v<=r}||h_v||_p],

which gives U_1 by discrete Gronwall. At the top,

    ||Z_k||_p <= 6B_1sqrt(p)+alpha sum_{r<k}h_r||C_r||_p,
    ||C_r||_p <= 3 sum_{v<r}h_v||Z_v||_p.

Bound the double time sum by T times one sum to obtain U_2. These are deterministic suprema of marginal norms, not bounds for a random maximum over mesh times. They imply uniform marginal subGaussian tails for the incoming fields. No e-smallness is needed for this conditional lemma.

For derivative estimates use the random component maximum Q^1_k=max_i|q_{k,i}|; by Minkowski its L^p constant is at most 3M_q. Let L_q=3M_q and L_C=M_C. The exact Jacobian equations and finite Volterra iteration give

    ||J_{k,j}||_infty
       <= 3h_j exp(3beta T+3e sum_{r<k}h_r Q^1_r),

    ||U_{k,bullet}||_row
       <= exp(3alpha T^2+alpha e sum_{r<k}h_r |C_r|),

    ||T_{k,bullet}||_row
       <= 3T exp(3alpha T^2+alpha e sum_{r<k}h_r |C_r|).

The readout rows in the last inequality can be estimated by the same increasing exponential majorant. No time independence is used.

If ||X||_p<=M sqrt(p) for p>=2, then E exp(X^2/(8 exp(1) M^2))<=2 by the power series and m!>=(m/exp(1))^m. Consequently

    E exp(u|X|) <= 2 exp(2 exp(1) M^2 u^2).

Jensen in the time weights gives the same estimate for exp(u sum h_r|X_r|) with u replaced by uT. Thus all the displayed derivative envelopes are integrable, uniformly in the cap and mesh under the stated prefix hypotheses.

For example, coefficient production is bounded by the following conservative explicit functions:

    alpha_new <= 3B_1^2
        +6 exp(3beta T+18 exp(1) e^2 T^2 L_q^2),

    beta_new <= 3TR^2
        +sqrt(2)(sqrt(2)e M_C+3T)
             exp(3alpha T^2+4 exp(1)alpha^2 e^2 T^2 M_C^2).

The learned contractions account for 3B_1^2 and 3TR^2. For the top response, use Cauchy--Schwarz on (e|C_k|+3T) times its exponential envelope. The current N^2 multiplier is included. Constants can be enlarged if a different block-row convention is used without changing the issue.

This proves the claimed conditional source estimate. It does not prove that alpha,beta can be chosen for an arbitrary prescribed horizon. In particular these inequalities are not a Gronwall bound of the form X(T)<=K+integral KX. Their right sides depend exponentially on each other's coefficient radii and then exponentially on the resulting moment radii. The absence of an algebraic supersolution to a chosen crude majorant would only invalidate that majorant; it would not prove coefficient explosion or falsify the target theorem.

## 5. Why energy does not by itself close the preceding premise

For a true trajectory, energy gives R and B_1<=1+R. It bounds the learned contractions and primitive Gaussian variances. It also bounds the current B return. What is not supplied is a cap-independent bound for the strictly past expected derivative rows A,B.

Two concrete points prevent treating this as an automatic Hilbert ODE theorem.

1. A bounded raw state ball has no uniform incoming-field tail estimate. Hold w,A at initialization and let C range over an L^2 ball in the top canonical space. The readout may have an arbitrary L^2 tail; in particular a bounded L^2 ball does not have uniform integrability or any common positive exponential moment. The source lemma needs a reachable-state estimate, not a bound for an arbitrary ambient ball.

2. The true backward gate has unbounded local derivative on such balls. On a positive-measure event where |phi''(Z_i)| is bounded below, choose an unbounded L^2 readout C supported there. Then multiplication by C phi''(Z_i) is an unbounded operator on L^2. Arbitrary L^2 variations of this sample's Z_i can be produced by a Hilbert--Schmidt variation delta A=v tensor h_i/||h_i||_2^2. Hence the bounded initialized action does not restore a ball-dependent Lipschitz bound for the gate. This is an ambient-state obstruction, not a counterexample about states reached from Gaussian initialization.

The ordinary incoming-field cap makes the field locally Lipschitz, but it is not the original loss gradient. Its path cannot simply be assigned the true energy identity. A stop on a raw ball is a legitimate device, but then ruling out first exit still requires a cap-uniform error/tail argument. Energy-preserving Galerkin flows provide bounded paths but not the strong compactness needed to pass the nonlinear gates and adjacent action products.

## 6. What would finish this route, and what is established

If one proves that, on each finite physical horizon, the stopped capped approximations have strict raw-ball slack and uniformly bounded A-density/B-row (or another estimate directly giving incoming-field tails strong enough for cap removal), Section 4 supplies the needed cap-independent subGaussian estimates. The asymmetric gate comparison from the supplied population bridge then has only one cap factor,

    ||F_R(Theta_R)-F_S(Theta_S)||_raw
       <= K_ball(1+eR)||Theta_R-Theta_S||_raw
          +K_ball e sum_i || |q_i|1_{|q_i|>R} ||_2,

with C included as the top incoming field. Gaussian tails defeat its exp(K_ball R T) propagation factor. This yields strong cap removal, uniqueness against bounded-primal competitors, and reached-state restart on that horizon. The existing fixed-cap finite Gaussian-program and raw Euler machinery can then identify full-sequence GF/GD limits, retaining the actual finite random readout. Velocity and path conclusions still require the stated ordered observational truncations from the supplied bridge; energy alone is not a substitute.

Established here: exact L=2 source/derivative identities; the controlled current return; finite-width global GF; conditional raw energy/endpoints for true strong population GF; and cap/mesh-uniform subGaussian/derivative estimates conditional on bounded source coefficients, without affine comparison.

Open here: a noncircular cap-independent continuation estimate for the two past-response families, hence construction and full-width identification of the global strong population flow. Separately, source continuation would not automatically prove generic three-label fitting or preserve the trained activation regression gap. There is no justified polynomial theta<=c delta^p theorem for the full requested conclusions from this route as it stands.
