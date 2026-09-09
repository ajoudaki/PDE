# Same-label two-sample nonlinearity and all-layer feature motion

Root working proof, 2026-09-06, NOT YET AUDITED.
This supplements SAME_LABEL_GLOBAL_ASSEMBLY.md and
TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, using their state construction,
actual scalar laws and strong limits. It is not a solution of the
opposite-label continuation problem.

We take both labels +1; simultaneous label/readout sign reversal covers
both labels -1. All times in the first four sections are feature times
s in [0,S], S=3/2. Set epsilon=1/10, m=5/6, a=7/6, A=3/2.
The root pair is centered Gaussian with covariance C, rho in [-1,1).
All Gaussian assertions about later fields refer to the explicit source
laws of the cut Euler programs, not to iid trained neuron coordinates.

## 1. Forward pair separation survives the constructed interval

The response bootstrap gives |A^(ell)_(ka,rb)|<=A Delta/2,
both reverse coefficient row sums <=1, and each q^(j)_(ka) is its
Gaussian source plus a correction of absolute value <=a.
The bottom source standard deviations are <=Q_*/10, with
Q_*=24829/19200<27/20; the middle ones are <=7/40.

For the raw first-layer update, independently of the root pair,

  |Z^(1)_(ka)-G_a| <= R_(1,k),
  R_(1,k)=(epsilon Delta/2)sum_(r<k,b)(|zeta^(1)_(rb)|+a).

Consequently
E R_(1,k)<=epsilon S(Q_*/10+a)<1/5.
The event R_(1,k)<=1 has probability at least 4/5 and is independent
of (G_1,G_2). Since rho<1,

  p_1(rho)=P(G_1>=2,G_2<=-2)>0.

For -1<rho<1 this follows from the positive bivariate Gaussian density;
at rho=-1 it is P(G_1>=2)>0. Intersecting the independent events yields

  P(Z^(1)_(k1)>=1,Z^(1)_(k2)<=-1)>=(4/5)p_1(rho).

On this event H^(1)_(k1)-H^(1)_(k2)>=epsilon*pi/2.
Thus there is an explicit d_1(rho)>0, uniform in caps/mesh/time, with

  E(H^(1)_(k1)-H^(1)_(k2))^2>=d_1(rho).                 (1)

The finite Euler scheme is invariant in law under sample exchange and
has deterministic limiting same-neuron laws. Its two feature second
moments are therefore equal. The two eigenvalues of the first feature
second-moment matrix are

  (1/2)E(H^(1)_(k1)+H^(1)_(k2))^2 >=2m^2,
  (1/2)E(H^(1)_(k1)-H^(1)_(k2))^2 >=d_1(rho)/2.

This matrix is uniformly positive definite for each fixed rho.
The same exchange assertion holds at every layer and later survives
the strong cut/mesh limits.

For the middle preactivations,

  |Z^(2)_(ka)-xi^(2)_(ka)|<=R_(2,k),
  R_(2,k)=(A epsilon Delta/2)
                            sum_(r<k,b)(|zeta^(2)_(rb)|+a).

Its expectation is at most
A epsilon S(7/40+a)=483/1600<1/3. Its source group is independent
of the entire xi^(2) group. Therefore P(R_(2,k)<=1)>=2/3.
The covariance eigenvalues of the pair xi^(2) lie between
c_1=min(2m^2,d_1/2)>0 and 2a^2. Its density on the rectangle
[2,3] times [-3,-2] has a positive lower bound depending only on rho.
Indeed the density is at least

  (4*pi*a^2)^(-1) exp(-||x||^2/(2c_1))

there, by the eigenvalue bounds. The independent dominator event
therefore supplies a uniform positive probability that
Z^(2)_(k1)>=1 and Z^(2)_(k2)<=-1.
It follows as above that its feature difference has a uniformly
positive squared norm d_2(rho), and that the second feature
second-moment matrix has eigenvalues bounded below by
c_2=min(2m^2,d_2/2)>0.

At the top, |W^(4)_r|<=aS and the top gate is at most epsilon, so

  |Z^(3)_(ka)-xi^(3)_(ka)|
                       <=A a epsilon S^2=63/160=:B_0<2/5.     (2)

The top Gaussian pair covariance has eigenvalues between c_2 and
2a^2. Its probability on [2,3] times [-3,-2] has a uniform positive
lower bound, without any independence requirement for the bounded
correction (2). Thus the same opposite-sign feature-separation event
is positive at the top too.

All these are statements about actual cut Euler laws. They pass first
to fixed-cap flows and then to the uncut flow: joint fields converge
strongly in L^2, and the probabilities of the closed rectangles in
question are at least the limsup of the approximating probabilities.
The feature moments converge as well. No joint almost-sure
realization of all Gaussian source processes is required.

## 2. Every marginal remains genuinely nonlinear

At the bottom, R_1<=1 and G_a>=u+1 (or G_a<=-u-1) give uniform
positive lower tails for Z^(1)_a, for every fixed u>0.
At the middle use R_2<=1, independent of its forward source, and
the marginal Gaussian variance at least m^2.
At the top use the bounded correction (2) and the same variance
lower bound. Thus every marginal preactivation has both unbounded
tails at every reached time. The bounds are uniform over the
constructed feature interval, for fixed tail level u.

For each such square-integrable Z, its variance is positive and

  inf_(alpha,beta) E[phi(Z)-alpha Z-beta]^2
     =Var(phi(Z))-Cov(Z,phi(Z))^2/Var(Z) >0.              (3)

The quadratic minimizer exists. Equality would imply an affine identity
almost surely. Because phi is bounded and Z has unbounded support,
its slope would be zero. Strict monotonicity of phi would then force
Z constant, contrary to its tails.
All moments in (3) vary continuously along the L^2 state path.
Their positive values have positive minima on compact time intervals.
The already established empirical second-moment convergence transfers
a smaller positive bound to the finite empirical affine errors, uniformly
in time with probability tending to one. The fixed nonlinearity is never
sent to zero as width, time mesh or input angle changes.

## 3. Backward pair covariance is positive at every positive time

The same-label readout obeys W^(4)(s)>=ms pointwise. Fix s_0>0 and
consider cut Euler indices with k Delta>=s_0. Then
delta^(3)_(ka)=W^(4)_k epsilon/(1+(Z^(3)_(ka))^2)>0.

For the top source pair use the rectangle [4,5] times [-1/10,1/10].
Its probability has a positive lower bound p(rho)>0 from the covariance
eigenvalue bounds above. On it, (2) implies

  |Z^(3)_(k1)|>=18/5,     |Z^(3)_(k2)|<=1/2,
  delta^(3)_(k1)/delta^(3)_(k2)
                      <=(5/4)/(1+(18/5)^2)<1/4,
  delta^(3)_(k2)>= (4/5)m s_0 epsilon=:b_0>0.

On the swapped rectangle the two roles are interchanged.
For any unit vector v=(v_1,v_2), choose the rectangle on which
the coordinate associated to max(|v_1|,|v_2|) is the large delta.
Then

  |v_1 delta^(3)_(k1)+v_2 delta^(3)_(k2)|
                       >=(3/4)b_0 max(|v_1|,|v_2|)
                       >=3b_0/(4 sqrt(2)).

Therefore the second-moment matrix of the two top deltas has smallest
eigenvalue at least 9p(rho)b_0^2/32>0. This estimate passes through
the cut/mesh limits by their converging second moments. In particular
that matrix is positive definite at every fixed s>0.

At such a fixed time, choose approximating cut Euler laws with times
approaching s. Their middle reverse source covariance converges to the
positive-definite top-delta second-moment matrix. Each q^(2)_a differs
from its source by at most a. Every signed rectangle

  sign_1 zeta^(2)_1 in [a+1,a+2],
  sign_2 zeta^(2)_2 in [a+1,a+2]

has probability bounded below along sufficiently late approximations,
for each of the four independent choices sign_1,sign_2 in {-1,1}.
Hence each corresponding closed quadrant
sign_1 q^(2)_1>=1, sign_2 q^(2)_2>=1 has positive limiting probability.
Since phi'(Z^(2)_a)>0 almost surely, delta^(2)_a has the same nonzero
sign as q^(2)_a on these quadrants.

No nonzero constant linear combination of the two middle deltas can
vanish almost surely: choose the quadrant aligned with the signs of
its nonzero coefficients. Its combination is then strictly positive.
Thus their second-moment matrix is positive definite.
Apply the same argument to the bottom reverse source, whose covariance
is precisely this matrix and whose response correction is bounded by a.
It proves positive definiteness of the two bottom-delta second moments.

This reasoning uses converging joint empirical laws of reused outputs
and actual covariance identities; it does not replace trained fields
by independent Gaussian neurons.

## 4. No hidden layer freezes at a positive time

Let K_g^(ell) be the squared raw metric norm of the layer-ell block
of grad g, where g=(f_1+f_2)/2. From the exact kernel formulas,

  K_g^(1)=(1/4)sum_(a,b) C_ab E[delta^(1)_a delta^(1)_b],
  K_g^(ell)=(1/4)sum_(a,b) E[delta^(ell)_a delta^(ell)_b]
                                      E[H^(ell-1)_a H^(ell-1)_b],
                                                 ell=2,3.

Each is strictly positive at s>0. In the first formula the delta
matrix is positive definite and C is positive semidefinite with
trace two, even at rho=-1. Their trace product is at least twice
the delta matrix's smallest eigenvalue. For the other two formulas
the feature Gram matrix is positive semidefinite with positive trace
and the delta matrix is positive definite, giving the same conclusion.

Adjunction and the differentiated forward equations give, for j=1,2,3,

  (1/2)sum_a E[delta^(j)_a (Z^(j)_a)']
                                   =sum_(ell<=j)K_g^(ell)>0.   (4)

For j=1 this is the first-layer gradient pairing through C.
At j=2 the trained matrix term contributes K_g^(2), and the propagated
lower derivative contributes the j=1 identity. At j=3 the identical
calculation contributes K_g^(3) and the j=2 identity.
Therefore at least one sample's preactivation velocity is nonzero
at each layer. The deterministic joint laws are sample-exchange
symmetric, including their derivative probes, so the two sample
velocity norms are equal. BOTH are nonzero.
The strictly positive gate preserves nonzero L^2 norm of every feature
velocity. The physical clock derivative 4(1-g)>0 at every finite
physical time preserves these conclusions there.

## 5. Initial nonlazy scale and nonconstant kernel

Write alpha for the three hidden parameter blocks in their raw Hilbert
metric and V(alpha)=(H^(3)_1+H^(3)_2)/2. Then g=E[W^(4)V(alpha)].
Let D_0 be the bounded linearized forward map from hidden variations
to V at initialization, and let B=D_0^*V_0. Its component in each
hidden block is nonzero, as follows without assuming later existence:

The initial top backward pair
V_0 phi'(Z^(3)_(a,0)) has positive-definite second-moment matrix.
The top preactivation pair is nondegenerate Gaussian because the
initial lower feature Gram is positive definite, and V_0>=m; the
two rectangle/gate-ratio argument from Section 3 applies directly.
Condition the initial third matrix on both forward queries and use
its Gaussian orthogonal residual. The reverse pair equals a bounded
linear combination of the two middle features plus a Gaussian pair
whose full covariance is the top-backward second-moment matrix,
independent of the old middle root tuple. Its four quadrants survive
the bounded shift. Multiplication by positive middle gates then gives
a positive-definite middle-backward pair.
The initial second transpose is treated identically, conditioning also
on the entire independent third matrix. The unbounded gated reverse
input can first be clipped; its already established Gaussian-plus-bounded
law gives vanishing L^2 clipping error, and the bounded initial operator
transfers that error. Conditional Gaussian averaging proves joint
empirical convergence, not just a tagged-coordinate law.
Thus the bottom-backward second-moment matrix is positive definite too.
The trace-product argument in Section 4 proves every block B_ell nonzero.

Let Gamma_ell=||B_ell||^2>0, and Gamma=sum_(ell=1,2,3)Gamma_ell.
The curve chain rule and continuity of bounded-gate products yield

  W^(4)(s)/s -> V_0,
  alpha'(s)/s -> B,
  alpha(s)-alpha(0)=(s^2/2)B+o(s^2).

Here only convergence of the bounded linearized forward/adjoint maps
on the displayed strongly converging directions is needed, not
operator-norm differentiability of an L^2 Nemytskii map.
It follows that V'(s)=s D_0 B+o(s), and
E[V_0 D_0 B]=||B||^2=Gamma. Consequently

  K_g^(4)(s)=E[V(s)^2]=E[V_0^2]+Gamma s^2+o(s^2),
  sum_(ell=1,2,3)K_g^(ell)(s)=Gamma s^2+o(s^2),
  sum_(ell=1,2,3,4)K_g^(ell)(s)
                             =E[V_0^2]+2Gamma s^2+o(s^2).      (5)

The total two-by-two kernel therefore cannot be constant: its fixed
same-label quadratic form (5) changes.

Differentiating the forward equations also gives, in each sample/layer,
(Z^(ell)_a)'(s)=s T^(ell)_a+o(s).
Dividing identity (4) by s^2 and taking s down to zero shows the
appropriate initial-backward pairing with T^(ell) equals the sum
of the positive Gamma_j for j<=ell. Thus these leading velocities
are nonzero; symmetry makes both sample norms equal.
Integrating and using positive gates gives

  H^(ell)_a(s)-H^(ell)_(a,0)
       =(s^2/2)phi'(Z^(ell)_(a,0))T^(ell)_a+o(s^2).

Since s(t)=4t+o(t), the leading physical feature change is
8t^2 phi'(Z^(ell)_(a,0))T^(ell)_a, with a nonzero fixed L^2 coefficient.
The output-mode kernel change is 16Gamma t^2+o(t^2), and total-mode
kernel change is 32Gamma t^2+o(t^2).
No activation or motion coefficient is sent to zero with width.

The field and kernel convergence already established in the assembly
transfers these nonzero fixed-time feature changes and kernel changes
to the finite model. Thus this same-label candidate, if the construction
and this supplement pass complete audits, is neither effectively linear
nor a frozen/kernel limit.
