# Every sample and hidden layer moves initially: arbitrary fixed depth and odd gain

This is a general-depth extension of the exact initialization argument in `odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md`, Sections 4--6. It is an unconditional statement about the canonical initialized Gaussian program and its algebraic feature-ascent directions. Its identification with physical accelerations is conditional on the existence of the canonical strong trajectory with the strong chain rule; this note does not claim such existence by itself.

## 1. Setup and statement

Fix an integer L>=2 and three normalized inputs u_i=x_i/sqrt(d), with

    ||u_i||=1, Gamma_ij=<u_i,u_j>, |Gamma_ij|<=1-delta (i!=j), delta>0.

Only feasible data are quantified over. Let y_i in {-1,1}, p_i=y_i/3, and take the same activation in every hidden layer,

    phi(z)=a(z+atan z), a>0.

The argument in fact works for phi(z)=a z+e atan z with any independent a,e>0. In the requested odd-gain case e=a. Write A_l:H_(l-1)->H_l for the canonical initialized action of W^l, l=2,...,L, including its genuine adjoint. The first initialized projection tuple Z^1 has law N(0,Gamma), and recursively

    h_i^l=phi(Z_i^l), Z_i^l=A_l h_i^(l-1) (l>=2),
    D_i^l=phi'(Z_i^l), Q_l=(<h_i^l,h_j^l>)_(ij).

All objects in this note are at initialization unless a time argument is displayed. Set

    H=sum_i p_i h_i^L,
    beta_i^L=D_i^L H,
    q_i^l=A_(l+1)^* beta_i^(l+1), beta_i^l=D_i^l q_i^l (l<L),
    S_l=(<beta_i^l,beta_j^l>)_(ij).

The raw hidden directions are

    V^1=d^(-1)sum_i p_i beta_i^1 x_i,
    V^l=sum_i p_i beta_i^l tensor h_i^(l-1), 2<=l<=L.

Their sample preactivation/feature directions are

    U_j^1=V^1 dot x_j=sum_i Gamma_ji p_i beta_i^1,
    t_j^l=D_j^l U_j^l,
    U_j^l=V^l h_j^(l-1)+A_l t_j^(l-1), 2<=l<=L.

Every V^l, every U_j^l, and every t_j^l is nonzero in its appropriate raw, HS, or L2 norm. No sample permutation symmetry or scalar residual clock is assumed.

For any canonical strong physical gradient flow from C(0)=0 with the strong chain rule, these yield

    (theta_h^l)''(0)=9 V^l, (z_j^l)''(0)=9 U_j^l,
    (h_j^l)''(0)=9 t_j^l,

as strong right derivatives. If K_total is the actual sum of all L hidden kernel blocks and the readout block, then

    p^T K_total(t)p=p^T K_total(0)p+18 t^2 ||V||_hidden^2+o(t^2),

where ||V||_hidden^2=d||V^1||_2^2+sum_(l=2)^L ||V^l||_HS^2>0.

## 2. Initial forward Grams are positive, including singular Gamma

Let G be standard normal, H_3(z)=z^3-3z, and

    b_3=E[atan(G)H_3(G)]/sqrt(6)
       =(1-2 E[(1+G^2)^(-1)])/sqrt(6) !=0.

The equality follows by Gaussian integration by parts. Strict Jensen gives E[(1+G^2)^(-1)]>1/2, hence b_3!=0.

The cubic tensor lift of three absolutely separated lines satisfies

    Gamma^(circ 3)>=[delta^2(2-delta)^2/3] I_3.

A direct verification uses, for each i and the other indices j,k,

    v_ij=(u_i-Gamma_ij u_j)/sqrt(1-Gamma_ij^2),
    R_i=u_i tensor v_ij tensor v_ik.

Then ||R_i||=1, <u_l^(tensor 3),R_i>=0 for l!=i, and the i-th pairing is at least delta(2-delta). Applying Cauchy--Schwarz to sum_l c_l u_l^(tensor 3) and summing the resulting three inequalities proves the bound. This never inverts Gamma.

Projecting the first features onto cubic Gaussian chaos gives, for phi=a z+e atan z,

    Q_1>=e^2 b_3^2 Gamma^(circ 3)>0.

At every following layer the three centered Gaussian preactivations have a common positive marginal variance. The coefficient of the orthogonal projection of phi(Z_i) onto the Gaussian first chaos is at least a, because z atan z>=0. The orthogonal residual contributes a positive semidefinite Gram. Therefore

    Q_l>=a^2 Q_(l-1)>0, 2<=l<=L.

In particular Z^l has full three-dimensional Gaussian support for every l>=2 and H!=0. For e=a,

    ||H||_2^2 >= a^(2L)b_3^2 delta^2(2-delta)^2/9.

Neither singularity of the first Gaussian tuple nor cancellation of an affine label direction invalidates this positivity.

## 3. Backward Grams, all parameter blocks, and bottom sample motion

Because L>=2, Z^L has a positive Gaussian density on R^3. If v^T S_L v=0, continuity implies the identity

    [sum_i p_i phi(z_i)] [sum_i v_i phi'(z_i)]=0 on R^3.

The first factor has no open zero set: its derivative in each coordinate is p_i phi'(z_i), which never vanishes. Consequently the second factor vanishes everywhere. Differentiating in coordinate i gives v_i phi''(z_i)=0 for every z_i. Since e>0 and phi'' is not identically zero, v_i=0. Thus S_L is positive definite.

The exact reused-transpose initialization rule, with its returns retained, is

    q_i^l=zeta_i^l+sum_k R^l_ik h_k^l, 1<=l<L.

The coefficient matrices R^l are deterministic Gaussian response coefficients. The primitive reverse group zeta^l is centered Gaussian with full covariance S_(l+1), independently of the forward groups and roots. These are canonical same-matrix identities, not independent replacements for A_(l+1)^*. For explicit dependency checking, their initial coefficients are constructed downwards by

    R^(L-1)_ik=p_k E[D_i^L D_k^L]+1_(i=k) E[H phi''(Z_i^L)],
    R^l_ik=1_(i=k) E[phi''(Z_i^(l+1))q_i^(l+1)]
                +R^(l+1)_ik E[D_i^(l+1)D_k^(l+1)], l<L-1.

These identities follow by differentiating beta_i^(l+1) in the named Z_k^(l+1) slot with other primitive source groups frozen. They retain both the local current curvature term and the next-layer return. No current response is inverted or discarded.

Conditionally on Z^l,

    Cov(beta^l | Z^l)=diag(D^l) S_(l+1) diag(D^l)
                    >=a^2 lambda_min(S_(l+1)) I_3.

The return term is measurable in Z^l and does not change this conditional covariance. Induction from S_L>0 gives S_l>0 for every l. In particular

    Cov(beta^1 | Z^1)>=a^2 lambda_min(S_2) I_3.

This remains true when Z^1 is singular. It implies

    d||V^1||_2^2>=a^2 lambda_min(S_2) sum_i p_i^2>0,
    ||U_j^1||_2^2>=a^2 lambda_min(S_2) sum_i Gamma_ji^2 p_i^2
                  >=a^2 lambda_min(S_2)p_j^2>0.

For every hidden matrix block,

    ||V^l||_HS^2=tr(diag(p) S_l diag(p) Q_(l-1))>0, 2<=l<=L.

Here Q_(l-1) and S_l are positive definite and diag(p) is invertible. The trace of the product of two positive definite matrices is positive: conjugating one by the positive square root of the other makes this explicit. Thus all hidden parameter blocks and all bottom samples already have strictly positive direction norm.

## 4. Every upper sample: a recursive exact return formula

For each fixed sample j define deterministic coefficients

    c^1_ji=Gamma_ji p_i,
    c^l_ji=p_i (Q_(l-1))_ij
              +c^(l-1)_ji E[D_j^(l-1)D_i^(l-1)], 2<=l<=L.

For l>=2, let xi_(t_j^(l-1)) be the primitive forward source associated with the added call A_l t_j^(l-1), in the same Gaussian source group as Z^l. We claim the exact identity

    U_j^l=xi_(t_j^(l-1))+sum_i c^l_ji beta_i^l.             (A)

At the bottom,

    partial_(zeta_i^1) t_j^1=D_j^1 c^1_ji D_i^1.

The same-matrix forward return rule is consequently

    A_2 t_j^1=xi_(t_j^1)+sum_i beta_i^2 c^1_ji E[D_j^1D_i^1].

Adding V^2 h_j^1=sum_i p_i (Q_1)_ij beta_i^2 proves (A) for l=2.

Suppose (A) holds at layer l<L. Every named A_l-forward source is independent of the primitive A_(l+1)-reverse group zeta^l. The coefficients in (A) are deterministic. The initialized backward field beta_i^l=D_i^l(zeta_i^l+sum_k R^l_ik h_k^l) depends on zeta^l with derivative D_i^l. Hence

    partial_(zeta_i^l)t_j^l=D_j^l c^l_ji D_i^l.

The next forward return is exactly

    A_(l+1)t_j^l=xi_(t_j^l)+sum_i beta_i^(l+1)c^l_ji E[D_j^lD_i^l].

Adding the matrix-block contribution V^(l+1)h_j^l proves (A) at layer l+1. This establishes (A) through every fixed depth. The second term in c^l is the genuine same-matrix return; omitting it would give a different and incorrect formula.

## 5. Positive innovations persist through every layer

Regress xi_(t_j^(l-1)) on the three original forward sources Z^l in its own action group. Their covariance is Q_(l-1)>0, so this regression has a well-defined independent Gaussian remainder epsilon_(l,j). Its variance is exactly

    sigma_(l,j)^2=inf_(b in R^3)||t_j^(l-1)-sum_i b_i h_i^(l-1)||_2^2. (B)

The equality is the covariance rule for forward queries of the same initialized Gaussian action, not an assumption that different calls use different matrices.

For l=2 the features h_i^1 are measurable with respect to Z^1. Therefore (B), conditional variance, and Section 3 give

    sigma_(2,j)^2
       >=E Var(t_j^1 | Z^1)
       =E[(D_j^1)^2 sum_(i,k) c^1_ji D_i^1 (S_2)_ik D_k^1 c^1_jk]
       >=a^4 lambda_min(S_2) sum_i Gamma_ji^2 p_i^2
       >=a^4 lambda_min(S_2)p_j^2>0.                    (C)

The remainder epsilon_(2,j) is independent of Z^2 and the independent reverse group zeta^2 (when L>2). Formula (A) expresses all other terms in U_j^2 as functions of those old variables. At L=2, beta^2 is a function of Z^2 alone. Thus epsilon_(2,j) cannot cancel in U_j^2.

Now assume l>=2 and l<L. After regression, (A) has the form

    U_j^l=epsilon_(l,j)+F_(l,j)(Z^l,zeta^l),

where epsilon_(l,j) is independent of (Z^l,zeta^l), has variance sigma_(l,j)^2, and F_(l,j) is a measurable function of the displayed old variables. Consequently

    Var(t_j^l | Z^l,zeta^l)=(D_j^l)^2 sigma_(l,j)^2.

Each h_i^l is measurable in Z^l. Applying (B) at layer l+1 yields

    sigma_(l+1,j)^2>=E Var(t_j^l | Z^l,zeta^l)
                    =E[(D_j^l)^2]sigma_(l,j)^2
                    >=a^2 sigma_(l,j)^2>0.             (D)

Its new Gaussian remainder is independent of Z^(l+1) and zeta^(l+1), or of Z^L alone at the final layer. Formula (A) again prevents cancellation. This proves U_j^l!=0 for every j and l=2,...,L, with the concrete bound

    ||U_j^l||_2^2>=sigma_(l,j)^2
                   >=a^(2l)lambda_min(S_2)p_j^2>0.

Together with the bottom estimate this covers every sample and layer. Since D_j^l>=a, all feature directions t_j^l are nonzero as well.

Different samples' added forward sources may be correlated; the proof needs only each remainder's independence from the original forward tuple and the separate reverse group. It does not assume that the three added remainders are mutually independent. One may establish the argument in a separate fixed transcript for each j, then include the finite union of those queries on the common canonical space.

## 6. Why the augmented finite programs and innovations are valid

The initialization program has finitely many action calls for fixed L and three samples. Every original backward field has the form of a bounded smooth gate multiplying a finite sum of Gaussian sources and linear-growth functions of Gaussian forward sources. Formula (A) has that form too. All fields appearing in the added queries therefore have every finite moment.

The inputs t_j^l are not asserted to be globally Lipschitz functions of all named sources. To apply the derivative-valid fixed-program theorem, smoothly clip each unbounded incoming factor, use its bounded-derivative finite program, and remove the clips. Canonical action operator bounds give convergence of the actual forward and transpose answers in L2. The source derivatives required above are explicitly D_j^l c^l_ji D_i^l, which are bounded because phi' is bounded and c^l is deterministic. More generally the clipped return terms have integrable finite-source envelopes. Dominated convergence therefore passes the response coefficients. The converging finite covariance Grams identify the joint source limits using continuity of positive semidefinite square roots, without a pseudoinverse-continuity claim.

The positive innovation also follows directly from finite Gaussian conditioning. For the action A_l, condition on its previous forward calls A_l V=Y and reverse calls A_l^T U=Q. The forward inputs V include the three h_i^(l-1); the reverse inputs U include the three beta_i^l. On adding t=t_j^(l-1), the unused Gaussian part of the action answer contains

    ||(I-P_V)t||_n P_(U-perp) g_n,

where g_n is an independent standard Gaussian vector. The removed projection has expected normalized squared length rank(U)/n, which tends to zero for this fixed transcript. The residual input norm converges to the strictly positive variance in (B). If other finitely many new queries are included, their joint Gaussian covariance gives the same marginal regression on the original three sources; no assertion that a later query is independent of earlier added queries is needed. This confirms that reuse and transpose conditioning cannot erase the innovation proved in (C)--(D).

Actual adjunction is retained at every step. These are calls of the initialized canonical Gaussian actions and their adjoints, not arbitrary bounded operators substituted for the initialization.

## 7. Physical acceleration and the exact kernel coefficient

Let a canonical strong physical solution with the strong chain rule be given. Since C(0)=0, its predictions vanish and r_i(0)=-y_i=-3p_i. The readout equation implies

    C'(0)=3H, C(t)/t -> 3H in H_L.

All initial hidden velocities vanish. Bounded multiplication by the gates, strong forward convergence, and operator-norm convergence of the HS action increments give, backward from the top,

    b_i^l(t)/t -> 3 beta_i^l in H_l.

For completeness, if D(t) are uniformly bounded multipliers converging in probability to D(0) and q(t)->q(0) in L2, then D(t)q(t)->D(0)q(0) in L2: split the difference into the multiplier acting on q(t)-q(0) and (D(t)-D(0))q(0), and use dominated convergence on the second. Apply this at each gate, and split each changed action into its fixed initial action and a vanishing operator-norm increment.

Dividing each raw hidden update by t now gives

    theta_h'(t)/t -> 9V,
    theta_h(t)=theta_h(0)+(9/2)t^2 V+o_raw(t^2).

The exact strong forward chain rule, applied successively to the L layers, gives

    (z_j^l)'(t)/t -> 9U_j^l,
    (h_j^l)'(t)/t -> 9D_j^l U_j^l.

Thus the strong right second derivatives at zero exist and are precisely the stated nonzero accelerations. No second Frechet derivative of the ambient L2 Nemytskii map is assumed.

Let J denote the bounded hidden directional linearization of H(theta_h)=sum_i p_i h_i^L at initialization. Genuine adjunction gives J^*H=V. The preceding chain rule gives

    H'(t)/t -> 9JV,
    H(t)=H+(9/2)t^2 JV+o_L2(t^2),
    ||H(t)||_2^2=||H||_2^2+9t^2||V||_hidden^2+o(t^2).

The hidden part g_h(t) of the raw gradient of sum_i p_i f_i satisfies g_h(t)/t->3V, so

    ||g_h(t)||_hidden^2=9t^2||V||_hidden^2+o(t^2).

Finally the exact raw kernel identity is

    p^T K_total(t)p=||g_h(t)||_hidden^2+||H(t)||_2^2.

Adding the two contributions proves the coefficient 18. Because every hidden block is nonzero, ||V||_hidden>0, and the projected total kernel strictly increases from its initial value at all sufficiently small positive physical times. This is the actual kernel along training, with no scalar-clock or permutation argument.
