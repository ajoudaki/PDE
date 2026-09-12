# Random-direction source solver: candidate specification

Status: proposed numerical approximation; no population-error certificate.
The exact identities below hold with deterministic source-program coefficients.
Empirical coefficients generate a different finite process. Their convergence
and a useful physical-time-40 resource certificate remain obligations.

## Model and finite state

Exactly the C.4.7 two-hidden tanh model, physical Euler steps h, data directions
u_a in S1, weights p_a >= 0 summing to 1, labels |y_a| <= Y. Use separate lower
and upper statistical populations of P representatives. They are not connected
by a trainable P-by-P matrix. Lower roots g are independent N(0,I2), w=g;
upper c=0. This is population initialization, not a modification of the finite
neural-network initialization. Set directional tangents v_w=0, v_c=0.

At J=mN training calls save P-by-J arrays H,Hdot on the lower population;
D,Ddot on the upper; independent Rademacher source probes Rminus on lower,
Rplus on upper; independent standard Gaussian innovations Eminus and Eplus;
and all realized centered Gaussian sources Bminus and Bplus. Save two J-by-J
lower triangular covariance factors Lminus,Lplus, and J update coefficients
gamma. At each call also save omega=h*p_a, its physical time and direction.
Remove zero-weight atoms. A source probe is epsilon/sqrt(omega), where epsilon
is an independent Rademacher sign; its dual probe is omega*R. Save current
w,c,v_w,v_c, all arrays, data law, h, noise s>0, floating precision and complete
random-generator state in the checkpoint. All histories are retained; no
memory compression or omitted-memory accuracy claim.

Covariances of the plus sources are empirical uncentered H Grams plus s^2 I;
minus covariances use D. On appending a block X of m new fields, let
B=Xold.T@X/P and C=X.T@X/P+s^2 I. Solve Lold V=B, factor
C-V.T@V=Lnew Lnew.T, then draw new source rows as
Eold@V + Enew@Lnew.T. Preserve old factors and innovations literally.
The exact empirical Gram Schur complement is at least s^2 I. A failed
positive-definiteness check is a recorded failure; silently changing old
covariances or resampling old sources is prohibited.

## One step, all right sides at the preceding physical state

phi=tanh, dphi=1-phi^2, ddphi=-2phi*dphi. Let old history length be j.

1. Hnew=phi(w@u.T), Hdotnew=dphi(w@u.T)*(v_w@u.T).
   HH=Hold.T@Hnew/P. alpha=(omega_old*Rminus_old).T@Hdotnew/P.
   F=alpha+gamma_old[:,None]*HH.
2. Append plus covariance block using Hnew; draw Bplus_new and independent
   Rplus_new. Z=Bplus_new+Dold@F and Zdot=Rplus_new+Ddotold@F.
   V=phi(Z), Dnew=c[:,None]*dphi(Z),
   Ddotnew=v_c[:,None]*dphi(Z)+c[:,None]*ddphi(Z)*Zdot.
   f=mean(c[:,None]*V,axis=0), r=f-y; gammanew=-2*h*p*r.
3. Remove the known current-source contribution pointwise:
   Ddot_old=Ddotnew-c[:,None]*ddphi(Z)*Rplus_new.
   beta_old=(omega_old*Rplus_old).T@Ddot_old/P. Current beta has diagonal
   mean(c[:,None]*ddphi(Z),axis=0) and exact zero off diagonal: the current
   formal source names remain distinct even when their clean Gram is singular.
   DD=Dold.T@Dnew/P. Bcoef stacks beta_old+gamma_old[:,None]*DD
   above this diagonal block.
4. Append minus covariance block using Dnew; draw Bminus_new and independent
   Rminus_new. With Hall=[Hold,Hnew], Q=Bminus_new+Hall@Bcoef.
   With Hdotall similarly, Qdot=Rminus_new+Hdotall@Bcoef.
5. Simultaneously update
   w += ((dphi(w@u.T)*Q)*gammanew)@u;
   v_w += ((ddphi(w@u.T)*(v_w@u.T)*Q+dphi(w@u.T)*Qdot)*gammanew)@u;
   c += V@gammanew;
   v_c += (dphi(Z)*Zdot)@gammanew.
   Append Hnew,Hdotnew,Dnew,Ddotnew, gamma and source histories.

Frozen coefficients in tangent differentiation include residuals, Grams,
alpha,beta,F,Bcoef and gamma. Tangents differentiate the coordinate expression,
not the parameter-to-law map. Rplus,Rminus are independent of all Gaussian
roots/innovations at initialization of the infinite representative program.
Finite empirical feedback introduces dependence; it must not be called iid.

## Passive predictions from the saved state

For directions v, compute h=phi(w@v.T), hdot=dphi(w@v.T)*(v_w@v.T),
cross=H.T@h/P, alpha=(omega*Rminus).T@hdot/P,
shift=D@(alpha+gamma[:,None]*cross). Solve Lplus V=cross. Then
the conditional plus-source mean is Eplus@V and its marginal conditional
variance at each direction is mean(h*h)-sum(V*V). These are clean passive
initialized-action queries conditional on the noisy training-source history.
Use explicitly requested one-dimensional Gauss-Hermite order q for
mean_upper[c E_normal tanh(mean+shift+sqrt(variance)*G)]. This is a defined
finite quadrature, not an unevaluated expectation. Reject significantly
negative conditional variance. No random draws or state mutation are needed
for this predictor. Its predictive integration bias is separate from source,
time and empirical errors; no numerical tolerance is automatically certified.

For paired initial/current hidden moments, the initial lower h0=phi(g@v.T)
is known on the same lower representatives. The joint plus-source conditional
covariance of [h0,h] is their empirical Gram minus V.T@V.
Use the same conditional Gaussian draw for the named joint tuple, not
independent draws of its marginals. The initial forward correction is zero;
the current correction is shift. The population limit s->0 is the desired
initialized/current action pairing. A compact implementation may initially
expose finite joint-query draws separately; it must label their sampling error.

## Diagnostics and honest boundary

Record loss on training nodes, residual, norms of w-g,c and rank-factor K
(||K||HS^2=sum_ij gamma_i gamma_j <H_i,H_j><D_i,D_j>), covariance reconstruction
error, smallest Schur eigenvalue, maximum response coefficient, tangent RMS,
history counts/bytes, time and precision. Prediction change under refinements
is an empirical diagnostic, not a bound. Do not label a T40 run certified.

Arithmetic is O(P J^2+J^3), plus passive quadrature O(P J m_test+J^2 m_test+
P q m_test); state is O(PJ+J^2). Constants and checkpoint bytes must be reported.
The same equations are defined for arbitrary fixed finite laws on the circle
and longer finite physical horizons while the finite calculation remains
defined. This is broader numerical definition, not a population existence claim.
