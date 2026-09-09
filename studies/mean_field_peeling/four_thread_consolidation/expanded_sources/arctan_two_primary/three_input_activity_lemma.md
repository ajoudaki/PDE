# Three-input activity lemma, including rank-two input Gram matrices

Assume the local autonomous population flow and its mean-square continuity have been established with the same equations as the two-input flow, with all input sums now over a=1,2,3. Let x_a/sqrt(d) have norm one, and assume x_a and x_b are never parallel or antiparallel. Labels y_a are arbitrary signs. The input Gram matrix G is positive semidefinite with diagonal one; it need not be invertible.

Write the first-layer Gaussian root as Z_{0,a}^{(1)}=w^T x_a/sqrt(d), w~N(0,I_d), and H_{0,a}^{(1)}=atan(Z_{0,a}^{(1)}). Define Q_ab=E[H_{0,a}^{(1)}H_{0,b}^{(1)}].

## Q is positive definite even when G is singular

If a linear combination of these arctangents vanishes almost surely, continuity and the full support of w make it vanish for every w. Choose v outside the finitely many proper hyperplanes defined by v^T x_a=0 and v^T(x_a±x_b)=0. This is possible by pairwise nonparallelity. The numbers b_a=v^T x_a/sqrt(d) are nonzero and have distinct squares. Restrict the identity to w=t v. The coefficients of t,t^3,t^5 in the arctangent Taylor series give

    sum_a c_a b_a (b_a^2)^k = 0, k=0,1,2.

The Vandermonde determinant is nonzero, so c_a b_a=0 for every a, hence c=0. Thus Q is positive definite.

Consequently Y_a:=Z_{0,a}^{(2)} are a full-support centered Gaussian triple with covariance Q. Define

    S = sum_a y_a atan(Y_a),
    U_a = S phi'(Y_a),
    P_a = (W_0^{(2)})^* U_a,
    B_a = phi'(Z_{0,a}^{(1)}) P_a,
    V_ab = E[U_a U_b],    D_ab = E[B_a B_b].

The event S=0 has probability zero: conditional on Y_2,Y_3, S is a strictly monotone function of Y_1, and Y_1 has a continuous conditional density. If a linear combination of U_a vanishes, division by S and full support imply sum_a c_a/(1+Y_a^2)=0 everywhere. Varying one coordinate at a time forces each c_a=0. Thus V is positive definite.

The first reused transpose call has the Gaussian conditioning representation

    P_a = sum_c H_{0,c}^{(1)} [Q^{-1} E(Y U_a)]_c + Gamma_a,

where Gamma~N(0,V) is independent of the first-layer Gaussian root. Therefore the conditional covariance of B given the first-layer root is

    diag(phi'(Z_0^{(1)})) V diag(phi'(Z_0^{(1)})),

which is positive definite everywhere. It follows that D is positive definite.

Define

    T_a = sum_b G_ab y_b B_b,
    A_a = phi'(Z_{0,a}^{(1)}) T_a,
    R_a = sum_b y_b Q_ab U_b + W_0^{(2)} A_a.

The first-layer t^2 coefficient T_a is nonzero in mean square for every a. Indeed its coefficient of Gamma_a conditional on the roots includes G_aa y_a phi'(Z_{0,a}^{(1)}), which is nonzero; positive definiteness of V makes its conditional variance positive.

## Each second-layer coefficient is nonzero; no permutation symmetry is needed

Let alpha_a=Q^{-1}E[H_0^{(1)}A_a], and subtract the projection onto the three initial forward inputs:

    A_a^perp = A_a - sum_c alpha_{a,c} H_{0,c}^{(1)},
    sigma_a^2 = E[(A_a^perp)^2].

Conditional on the first-layer roots, A_a is a linear function of Gamma with coefficients

    c_b = phi'(Z_{0,a}^{(1)}) G_ab y_b phi'(Z_{0,b}^{(1)}).

In particular c_a=y_a phi'(Z_{0,a}^{(1)})^2 is nonzero. Thus

    sigma_a^2 >= E Var(A_a | first-layer roots) = E[c^T V c] > 0.

Condition the initial matrix on all three already revealed forward calls W_0^{(2)}H_{0,c}^{(1)}=Y_c and all three transpose calls (W_0^{(2)})^*U_b=P_b. The next forward call has law

    W_0^{(2)}A_a = sum_c alpha_{a,c}Y_c + sum_b beta_{a,b}U_b + sigma_a gamma_a,
    beta_a = V^{-1} E[P A_a^perp],

where gamma_a is standard Gaussian independent of the second-layer history Y (and therefore of U). This follows directly from the Gaussian matrix conditional mean and its independent doubly projected residual; the fixed-rank projection of a fresh Gaussian output disappears in normalized mean square. The Gram matrices Q,V are positive definite, so the displayed inverse formulas are legitimate. A separate such call suffices for each a; joint independence of different gamma_a is not claimed.

The other terms in R_a are functions of Y. Consequently

    E[R_a^2] >= sigma_a^2 > 0.

This establishes each input's second-hidden-layer activity without the two-input proof's swap argument.

## Small-time expansion and strict conclusions

Substitution in the integral equations, using bounded activation derivatives and the bounded initial action, gives

    W^{(3)}(t) = 2t S + o_L2(t),
    delta_a^{(2)}(t) = 2t U_a + o_L2(t),
    Z_a^{(1)}(t)-Z_{0,a}^{(1)} = 2t^2 T_a + o_L2(t^2),
    W^{(2)}(t)-W_0^{(2)} = 2t^2 sum_b y_b U_b tensor H_{0,b}^{(1)} + o_op(t^2),
    Z_a^{(2)}(t)-Y_a = 2t^2 R_a + o_L2(t^2).

The corresponding velocities are 4t T_a+o_L2(t) and 4t R_a+o_L2(t). Hence each hidden squared displacement has positive leading coefficient 4E[T_a^2] or 4E[R_a^2] times t^4, and each integrated squared hidden speed has positive leading coefficient (16/3)E[T_a^2] or (16/3)E[R_a^2] times t^3.

Set A_1=y^T(G entrywise-times D)y and A_2=y^T(Q entrywise-times V)y. Both are strictly positive. In particular the first conclusion does not need G positive definite: if D>=lambda I, diagonalizing G as sum_j v_j v_j^T gives

    G entrywise-times D = sum_j diag(v_j)D diag(v_j) >= lambda diag(G) = lambda I.

Likewise Q entrywise-times V is positive definite. Adjunction gives

    sum_a y_a E[U_a R_a] = A_1+A_2 > 0.

Thus the first and second kernel blocks are

    K^{(1)}(t)=4t^2(G entrywise-times D)+o(t^2),
    K^{(2)}(t)=4t^2(Q entrywise-times V)+o(t^2),

and both are positive definite for sufficiently small positive t. The initial readout block E[atan(Y)atan(Y)^T] is positive definite by the full support of Y, so it remains positive definite for small t. The total kernel satisfies

    y^T K(t)y = y^T K^{(3)}(0)y + 8(A_1+A_2)t^2 + o(t^2),

so it is nonconstant. The loss starts at three and has derivative -4y^T K^{(3)}(0)y<0, hence strictly decreases on a sufficiently short interval.

Every initial hidden marginal is a nondegenerate Gaussian. Its variance is positive, and atan cannot agree with an affine function on its full support. Thus its best-affine-fit error is positive. Mean-square continuity, and the variance/covariance formula for this fit, preserve these facts on a sufficiently small common interval.

The same proof works for any fixed finite number of pairwise nonparallel normalized inputs; for m inputs the Vandermonde argument uses the first m odd Taylor coefficients.

## Positive initialization and learning-rate constants

Let the first-weight entries initially have variance sigma_1^2>0 and the second-weight entries variance sigma_2^2/n, with sigma_2>0. Let the three fixed positive layer multipliers be kappa_1,kappa_2,kappa_3, so the population equations are

    dot Z_a^{(1)} = -2 kappa_1 sum_b G_ab r_b delta_b^{(1)},
    dot W^{(2)} = -2 kappa_2 sum_b r_b delta_b^{(2)} tensor H_b^{(1)},
    dot W^{(3)} = -2 kappa_3 sum_b r_b H_b^{(2)}.

The readout initialization tends to zero. All constants are fixed independently of width and step size.

The first roots now have covariance sigma_1^2 G. Their activation Gram matrix Q remains positive definite by the same Vandermonde argument. The second Gaussian root has covariance sigma_2^2 Q and still has full support. Use the preceding definitions S,U,P,B,T,V,D and A_1,A_2 under this changed initial law. The conditional transpose law becomes

    P_a = sum_c H_{0,c}^{(1)}[Q^{-1}E(Y U_a)]_c + Gamma_a,
    Cov(Gamma) = sigma_2^2 V.

The conditional mean coefficient is unchanged: the sigma_2^2 in the Gaussian regression covariance cancels the one from the initialization variance. All positivity proofs therefore continue to hold.

Define the weighted second-layer coefficient

    R_a^kappa = kappa_2 sum_b y_b Q_ab U_b
               + kappa_1 W_0^{(2)}[phi'(Z_{0,a}^{(1)}) T_a].

The expansions, including every multiplier, are

    W^{(3)}(t) = 2 kappa_3 t S + o_L2(t),
    delta_a^{(2)}(t) = 2 kappa_3 t U_a + o_L2(t),
    Z_a^{(1)}(t)-Z_{0,a}^{(1)} = 2 kappa_1 kappa_3 t^2 T_a + o_L2(t^2),
    W^{(2)}(t)-W_0^{(2)} = 2 kappa_2 kappa_3 t^2 sum_b y_b U_b tensor H_{0,b}^{(1)} + o_op(t^2),
    Z_a^{(2)}(t)-Y_a = 2 kappa_3 t^2 R_a^kappa + o_L2(t^2).

The fresh Gaussian part of R_a^kappa has variance

    kappa_1^2 sigma_2^2 E[(A_a^perp)^2] > 0.

Thus every first and second hidden coefficient remains strictly nonzero for positive constants. The physical kernel is the weighted sum

    K = kappa_1 K^{(1)} + kappa_2 K^{(2)} + kappa_3 K^{(3)},

not the unweighted sum. Its first two blocks have expansions

    kappa_1 K^{(1)}(t) = 4 kappa_1 kappa_3^2 t^2 (G entrywise-times D) + o(t^2),
    kappa_2 K^{(2)}(t) = 4 kappa_2 kappa_3^2 t^2 (Q entrywise-times V) + o(t^2).

The readout block has label-direction expansion

    y^T K^{(3)}(t)y = E[S^2] + 4 kappa_3 t^2 (kappa_1 A_1+kappa_2 A_2) + o(t^2).

Consequently

    y^T K(t)y = kappa_3 E[S^2]
                 + 8 kappa_3^2 (kappa_1 A_1+kappa_2 A_2)t^2 + o(t^2).

All three weighted blocks are positive definite for sufficiently small positive time, and the total kernel is nonconstant.

### Exact size and meaning of nontrivial hidden motion

The mean-square velocity limits are

    dot Z_a^{(1)}(t)/t -> 4 kappa_1 kappa_3 T_a,
    dot Z_a^{(2)}(t)/t -> 4 kappa_3 R_a^kappa.

Hence for some positive constants c_{ell,a},C_{ell,a} and common positive T_*,

    c_{ell,a} t <= sqrt(E|dot Z_a^{(ell)}(t)|^2) <= C_{ell,a} t,
    0<t<=T_*.

In particular the RMS hidden speed is positive for each fixed t>0 in the interval and survives the width/step limits. It is not a time-independent positive speed: it equals zero initially and vanishes linearly as t tends to zero. A positive uniform speed lower bound holds on [tau,T_*] for every fixed tau>0, not on (0,T_*].

The squared first-layer displacement and integrated squared speed are respectively

    4 kappa_1^2 kappa_3^2 E[T_a^2] t^4 + o(t^4),
    (16/3) kappa_1^2 kappa_3^2 E[T_a^2] t^3 + o(t^3).

For the second layer replace kappa_1^2 E[T_a^2] by E[(R_a^kappa)^2].

By contrast, the loss slope is already nonzero at initialization:

    -dot L(0) = 4 kappa_3 E[S^2] > 0.

Continuity allows the common interval to be reduced so that

    -dot L(t) >= 2 kappa_3 E[S^2] > 0, 0<=t<=T_*.

Only the summed loss is asserted to decrease; the individual residual magnitudes need not all decrease.

For the nonlinear claim define the best affine-fit error

    E_aff(Z) = inf_{a,b} E[(phi(Z)-a Z-b)^2]
             = Var(phi(Z)) - Cov(Z,phi(Z))^2/Var(Z)

whenever Var(Z)>0. Every initial hidden marginal is a nondegenerate Gaussian, and atan is not affine on its full support, so the six initial values are positive. Mean-square continuity gives a common short interval with

    E_aff(Z_a^{(ell)}(t)) >= (1/2) min_{b,j} E_aff(Z_{0,b}^{(j)}) > 0,

and with each hidden variance at least half the minimum initial hidden variance. These are genuine bounds uniform over time including zero, but they depend on the fixed geometry and positive hyperparameters.

### What fails at zero parameters

If kappa_3=0, the zero limiting readout stays zero, all backpropagated fields remain zero, and the entire system is frozen. If sigma_1=0 or sigma_2=0, the second-layer activation is initially zero; with zero limiting readout there is no seed for its update and the entire population system is again frozen.

If kappa_1=0, the first hidden layer is fixed and its weighted kernel block is zero. If kappa_2=0, the second weight matrix is fixed and its weighted kernel block is zero, although the second hidden preactivation can still move through the moving first-layer activation. With kappa_1=0 but kappa_2,kappa_3>0, each second hidden preactivation still moves: its coefficient is kappa_2 S sum_b y_b Q_ab phi'(Y_b), which cannot vanish almost surely by full support and the linear independence of the coordinate derivative functions. If kappa_1=kappa_2=0, only readout training remains and the total kernel is constant.

Strict positivity for every fixed positive choice does not imply a lower bound uniform as a hyperparameter approaches zero or as the allowed input configurations approach a degenerate boundary. The existence time and all quantitative nontriviality constants may depend on those fixed choices, but not on width or step size.
