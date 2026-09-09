# A calibrated near-identity dense activation with cumulative nonlinear geometry

Date: 2026-09-08.

This note proves initialization statements only. It supplies a research candidate for many weakly nonlinear layers, not a global trained population/GF/GD theorem. All Gaussian and matrix identities needed below are included. No specialized external theorem is invoked.

## 1. Exact family and network

Let G be a standard real Gaussian. Define
\[
 c=e^{3/2}/2,\qquad w(z)=c\sin(2z)-\sin z,\qquad
 v=E[w(G)^2],\qquad \chi(z)=w(z)/\sqrt v.
\]
The function w is not zero (its derivative at zero is 2c-1>0), so Gaussian full support and continuity give v>0. The shape chi is odd, bounded and smooth, with bounded derivatives of every order. Its derivative bounds are fixed constants, not normalized to one.

Fix a total depth parameter tau>0. For each integer hidden depth L>=1 use the same activation in all L layers:
\[
 h=\sqrt{\tau/L},\qquad
 \phi_L(z)=\frac{z+h\chi(z)}{\sqrt{1+h^2}}.             \tag{1}
\]
This is a different family from the fixed unit-sum arctangent mixture. There is no large gain or normalization layer; the scalar denominator is part of the activation. Matrix initialization stays unchanged. The activation does depend on L.

For three unit vectors u_i in R^d, let Gamma_ij=u_i dot u_j. Assume
\[
 |\Gamma_{ij}|\le1-\delta\quad(i\ne j),\qquad0<\delta\le1,
\]
whenever such a triple exists. Singular Gamma is allowed. Starting from Q_0=Gamma, define the initialized population recursion
\[
 Z^k\sim N(0,Q_{k-1}),\qquad
 (Q_k)_{ij}=E[\phi_L(Z_i^k)\phi_L(Z_j^k)].             \tag{2}
\]
Here L, and thus h, are fixed during the recursion.

This is the width-first initialization limit of the ordinary dense Gaussian network: normalized inputs x_i=sqrt(d)u_i, first weights N(0,1/d), and independent higher weights N(0,1/n). At the first layer, row tuples are iid Gaussian. Conditionally on preceding features, every next row is Gaussian with their empirical uncentered Gram, independently of the other rows. The activation has at most linear growth. On a bounded-diagonal event, fourth moments of the next features are bounded, so conditional Chebyshev gives empirical-Gram concentration. Induction supplies that event with probability tending to one. Expected feature products are continuous in a possibly singular covariance: couple Gaussian tuples by the positive square root, use its continuity and the Lipschitz activation. This proves (2) for every fixed finite L. No assertion uniform in L or simultaneous in n,L is made here.

## 2. Exact cancellation and correlation map

The elementary Gaussian characteristic function E exp(itG)=exp(-t^2/2), differentiated under its integrable Gaussian density, gives
\[
 E[G\sin(tG)]=t e^{-t^2/2}.
\]
Thus E[G w(G)]=2c e^{-2}-e^{-1/2}=0, and
\[
 E\chi(G)=0,\qquad E[G\chi(G)]=0,\qquad E\chi(G)^2=1. \tag{3}
\]
Consequently E phi_L(G)^2=1. Every diagonal entry of every Q_k in (2) equals one, exactly.

For standard jointly Gaussian X,Y of correlation rho in [-1,1], the representation Y=rho X+sqrt(1-rho^2)H, H independent, gives E[Y chi(X)]=rho E[X chi(X)]=0. This includes the endpoints by the same representation. Therefore
\[
 T_h(\rho):=E[\phi_L(X)\phi_L(Y)]
   =\frac{\rho+h^2 K(\rho)}{1+h^2},\qquad
 K(\rho)=E[\chi(X)\chi(Y)].                           \tag{4}
\]
The sine product identity and Gaussian characteristic function give
\[
 E[\sin(aX)\sin(bY)]
    =e^{-(a^2+b^2)/2}\sinh(ab\rho).
\]
Hence, writing
\[
 N=\sinh1-\sinh2+\tfrac14\sinh4>0,
\]
we have v=e^{-1}N and
\[
 K(\rho)=\frac{\sinh\rho-\sinh(2\rho)+\tfrac14\sinh(4\rho)}{N}
        =\sum_{\substack{m\ge3\\m\ {\rm odd}}}p_m\rho^m,
 \qquad p_m=\frac{(2^{m-1}-1)^2}{N\,m!}.              \tag{5}
\]
The coefficients are nonnegative, p_3=3/(2N)>0, and sum_m p_m=K(1)=1. The displayed series converges absolutely on every compact real interval. In particular,
\[
 0\le K(\rho)\le\rho^3\quad(0\le\rho\le1),\qquad
 |T_h(\rho)|\le|\rho|\quad(|\rho|\le1).              \tag{6}
\]
Thus the original absolute cosine separation is preserved in every population covariance step.

## 3. A depth-uniform initialized Gram bound

For any three-by-three Gram C of unit vectors with |C_ij|<=1-delta,
\[
 C^{\circ3}\succeq\frac{\delta^2(2-\delta)^2}{3}I_3.   \tag{7}
\]
Here the circle denotes entrywise powers. To prove (7), choose unit vectors v_i realizing C. For distinct i,j define
\[
 a_{ij}=\frac{v_i-C_{ij}v_j}{\sqrt{1-C_{ij}^2}},\qquad
 A_i=v_i\otimes a_{ij}\otimes a_{ik},
\]
where j,k are the other two indices. Each A_i has norm one, is orthogonal to v_j^{tensor3} and v_k^{tensor3}, and its pairing with v_i^{tensor3} is at least delta(2-delta). Therefore for X=sum_i b_i v_i^{tensor3},
\[
 \delta^2(2-\delta)^2\sum_i b_i^2
       \le\sum_i|\langle A_i,X\rangle|^2\le3\|X\|^2.
\]
Since ||X||^2=b^T C^{circ3}b, (7) follows.

Every entrywise power C^{circ m} is positive semidefinite, by the tensor Gram representation. Thus (5),(7), and absolute convergence imply
\[
 K[C]\succeq\mu_\delta I_3,\qquad
 \mu_\delta=\frac{p_3\delta^2(2-\delta)^2}{3}.          \tag{8}
\]
All Q_k have diagonal one and satisfy the separation, by (3),(6). Set b=(1+h^2)^(-1). Equations (4),(8) imply
\[
 Q_{k+1}\succeq bQ_k+(1-b)\mu_\delta I_3.
\]
Iterating, and using Gamma positive semidefinite, gives the explicit conclusion
\[
 \boxed{\lambda_{\min}(Q_L)
 \ge\frac{p_3\delta^2(2-\delta)^2}{3}
       \left[1-(1+\tau/L)^{-L}\right]
 \ge\frac{p_3\delta^2(2-\delta)^2}{3}\frac{\tau}{1+\tau}.} \tag{9}
\]
The last inequality is (1+tau/L)^L>=1+tau. This is a bound on the initialized feature Gram, uniform in finite depth. Tau and the shape chi do not depend on delta. There is still the natural geometric delta dependence in the bound itself.

## 4. Nonlinear population depth limit

For each initial correlation rho_0, (4) is the iteration
\[
 \rho_{k+1}=\rho_k+
   \frac{\tau/L}{1+\tau/L}\,[K(\rho_k)-\rho_k].         \tag{10}
\]
It converges to the solution at s=tau of
\[
 \frac{d\rho}{ds}=K(\rho)-\rho,\qquad \rho(0)=\rho_0. \tag{11}
\]
Here is sufficient justification without a depth-limit theorem. The vector field is smooth and Lipschitz on [-1,1], points toward zero in its interior, and is zero at both endpoints. Picard iteration on a short interval gives a unique solution, continued within this compact interval. Over a step ds=tau/L its integral increment differs from ds times its initial vector field by O(ds^2), uniformly in the interval. The difference between ds and ds/(1+ds) is also O(ds^2). Subtracting (10) from these exact increments gives e_(k+1)<=(1+C ds)e_k+C ds^2. Summing the resulting geometric series gives e_L<=C_tau/L. This proves the claimed width-first, then depth limit. The three-by-three limiting matrix remains positive semidefinite as a limit of such matrices.

A substantial nonlinear witness is the equilateral triple, with rho_0=-1/2 in all off-diagonal entries. Put r(s)=-rho(s). Oddness gives r'=K(r)-r. Equation (6) implies -r<=r'<=r^3-r, so r remains positive and is at most 1/2. For u=r^-2 one obtains u'>=2(u-1), hence
\[
 r(s)\le[1+3e^{2s}]^{-1/2},\qquad
 \lambda_{\min}(Q(s))=1-2r(s)
       \ge1-\frac2{\sqrt{1+3e^{2s}}}.                 \tag{12}
\]
At tau=1 this is greater than 0.58. The initial input Gram had a zero eigenvalue. A scalar rescaling of Gamma cannot produce this effect.

## 5. Near-identity and local variance checks

Let B=sup|chi| and M=sup|chi'|. Both are finite constants. From (1),
\[
 \sup_z|\phi_L'(z)-1|\le hM+h^2/2,
\qquad
 \sup_z\frac{|\phi_L(z)-z|}{1+|z|}\le hB+h^2/2.        \tag{13}
\]
The elementary bound used here is 1-(1+h^2)^(-1/2)<=h^2/2. The second derivative is also O(h) uniformly. This is derivative closeness and locally uniform value closeness; the unweighted global supremum of |phi_L-id| is not asserted to be finite.

The chosen sign of chi matters for variance perturbations. For q near one define the scalar variance map
\[
 V_h(q)=E\phi_L(\sqrt qG)^2
 =\frac{q+2h q a(q)+h^2 b(q)}{1+h^2},
\]
where a(q)=E chi'(sqrt(q)G), b(q)=E chi(sqrt(q)G)^2. Gaussian integration by parts proves the cross term q a(q). Here
\[
 a(q)=\frac{2c e^{-2q}-e^{-q/2}}{\sqrt v},\qquad
 a(1)=0,\qquad a'(1)=-\frac{3e^{-1/2}}{2\sqrt v}<0.
\]
The bounded smooth shape makes b differentiable near one with finite b'(1), by dominated differentiation. Therefore
\[
 V_h(1)=1,\qquad
 V_h'(1)=1-\frac{3e^{-1/2}}{\sqrt v}h+O(h^2).
\]
For sufficiently small positive h its absolute derivative at one is less than one, so the fixed variance is locally attracting. This is a local scalar population fact, not a joint width/depth stability theorem.

Finally E chi'(G)=E[G chi(G)]=0 implies, for M_2=E chi'(G)^2<infinity,
\[
 E\phi_L'(G)^2=\frac{1+h^2M_2}{1+h^2},\qquad
 [E\phi_L'(G)^2]^L\le e^{\tau M_2}.                  \tag{14}
\]
The last inequality follows by dropping the denominator and using 1+x<=e^x. These are scalar Gaussian gate moments only. They do not assert an operator norm bound for a product of Jacobians or a bound for trained backward fields.

## 6. What this establishes and leaves open

The candidate realizes depth-independent initialized nonlinear geometry with activations whose derivative perturbations vanish as L grows. It keeps the ordinary dense Gaussian matrix initialization. It is not the literal fixed convex mixture, and it uses a deliberate depth-dependent scalar calibration. This is evidence that the weak-per-layer/strong-cumulative mechanism is viable once the scaling is chosen for this architecture.

Unproved here: any population training evolution, finite GF/GD limit, nontrivial trained feature motion, persistence of the Gaussian cancellations during training, joint finite-width/growing-depth convergence, all-time continuation, or eventual fitting. In particular the exact Gaussian identity at initialization cannot be reapplied to trained non-Gaussian fields without a new argument. The practical research bottleneck remains control of actual forward/reverse response histories and incoming-field tails under training. Fixed-depth global theorems do not automatically provide estimates uniform along the family (1).
