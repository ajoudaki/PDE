# Initialized geometry of the full canonical p=1 closure

Date: 2026-09-18. Author: scoped agent `p1_initial_geometry`.
Status: exact theoretical derivation, author checked; not independently reviewed
or promoted. No numerical experiment or numerical coefficient evaluation was run.

## Scope and source record

The object is the exact population p=1 closure with input dimension two,
tanh gates, unhalved probability-weighted squared loss, physical population
L2/L2/Frobenius metric, initial readout zero, and ridge eta=1/4096.
The complete correlated lower initialization, including the reversed reused
action, is retained. The two population mark spaces are separate. After the
valid simultaneous-sign parity reduction, the feature dimensions are four
and two. The moving middle matrix is a full 2-by-4 matrix.

Scientific inputs actually read:

* `docs/observable_p1.md`, completely, SHA256
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
* `docs/global_nonlinear.md`, C.4.7.9 parts 1--4, C.4.7.10.C.1 completely,
  and C.4.7.10.C.3 completely; full-file SHA256
  `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
  C.4.7.9 supplies state/dynamics and characteristic well-posedness;
  C.4.7.10.C.1 supplies the prescribed dictionary and physical metric;
  C.4.7.10.C.3 supplies fixed-dimensional continuation and stability.

No other study, inherited discussion, code, external scientific source, or
numerical result was used. The required research and rigorous-mathematics
skills and Part 1 of `RESEARCH_WORKFLOW.md` were read. Git HEAD observed before
the edit was `019e3630237e33f58b9636c0aa67a039bebf0182`; unrelated working-tree
changes were left untouched. Only this assigned file is written by this agent.

The main conclusions concern initialization and exact initial stationarity.
They imply neither a full-neural-model identification at fixed p nor a
long-time spectral gap for the trained closure.

## 1. Exact initialized coefficient map

Let G_j,Z_j, j=1,2, be independent standard Gaussians on the lower population.
The upper population has its own independent standard Gaussians Ztilde_j.
Write

\[
 h_j=\tanh G_j,\quad v=E\tanh^2G,\quad
 H_j=\tanh(\sqrt v\,\widetilde Z_j),\quad
 \tau=EH_j^2,\quad\alpha=1-\tau,
\]
\[
 R_j=\sqrt\tau Z_j+\alpha h_j,\quad k_j=\tanh R_j,
 \qquad s=Ek_j^2,\quad\beta=Eh_jk_j,\quad\gamma=1-s.
\]

Set eta=1/4096 and, to avoid confusing a normalizer with the moving readout,

\[
 a_*^2=v+\eta,\qquad b_*^2=s+\eta-\frac{\beta^2}{v+\eta},
 \qquad c_*^2=\tau+\eta.
\]

The active feature columns and initialized middle matrix are exactly

\[
 b_1=\left(\frac h{a_*},\frac{k-\beta h/(v+\eta)}{b_*}\right),
 \qquad b_2=\frac H{c_*},\qquad
 M_0=D=(d_hI_2\ \ d_kI_2),
\]
\[
 d_h=\frac{\alpha v}{a_*c_*},\qquad
 d_k=\frac{L}{b_*c_*},\qquad
 L=\frac{\alpha\beta\eta}{v+\eta}+\tau\gamma.
 \tag{1}
\]

In particular the term tau gamma is present. Dropping it would change this
problem. The inactive constants may be removed because the exact mark laws
are invariant under simultaneous negation, w(0)=G is odd, c(0)=0, and D has
only an odd-to-odd block. The full vector field preserves this class by the
parity argument in the source. No symmetry of the training data is required.

For u=(u_1,u_2) on the unit circle, let

\[
 a_0(u)=E_1[b_1\tanh(G\cdot u)],\qquad V(u)=M_0a_0(u).
\]

For t in [-1,1], let (X,Y_t) be a centered, variance-one Gaussian pair
with correlation t. Define, for z in [-1,1],

\[
 \kappa(z)=E_Z\tanh(\sqrt\tau Z+\alpha z),\quad
 j(z)=E_Z\operatorname{sech}^2(\sqrt\tau Z+\alpha z),
\]
\[
 \lambda=\frac v{v+\eta},\qquad B=\frac L{b_*^2},\qquad
 A=\alpha\lambda-\frac{B\beta}{v+\eta},\qquad
 \ell(z)=Az+B\kappa(z),
\]
\[
 \psi(x)=\ell(\tanh x),\qquad
 F(t)=\frac1{c_*}E[\psi(X)\tanh Y_t].                 \tag{2}
\]

Then the exact identity is

\[
                         V(u)=(F(u_1),F(u_2)).        \tag{3}
\]

Indeed, conditional expectation over Z_j replaces k_j by kappa(h_j),
while (G_j,G dot u) has covariance u_j and unit marginal variances.
Multiplying the two bands in (1) by the two corresponding blocks of a_0
gives (2)--(3). The formula uses the full joint lower law. In particular,
it does not treat k_j as independent of G_j. It asserts coordinatewise
dependence on the unit circle, not on inputs with arbitrary variable norm.

## 2. The scalar function F is odd and strictly increasing

The proof does not require the coefficient A to be nonnegative. It instead
proves that the complete regression combination ell has positive derivative.

First, all scalar constants above are finite, and v,tau,s,gamma,alpha are
positive. Conditional on h, the variable R has nonzero Gaussian variance,
so k is not constant. The function kappa is odd with derivative alpha j>0,
which also gives beta=E[h kappa(h)]>0. Thus B>0.

We need the following entirely analytic bound on alpha:

\[
                    0<\alpha<\frac67<\operatorname{arsinh}(1).
                                                            \tag{4}
\]

For x nonzero, sinh^2 x>x^2, so tanh^2 x>x^2/(1+x^2).
For X=sigma^2 G^2, Cauchy--Schwarz gives

\[
 E\frac{X}{1+X}\ \ge\ \frac{(EX)^2}{E[X(1+X)]}
 =\frac{\sigma^2}{1+3\sigma^2}.
\]

Consequently v>1/4 and tau>v/(1+3v)>1/7. Finally, the positive fourth
derivative of (1+x)^(-1/2) makes its degree-three Taylor polynomial at
zero a strict lower bound for x>0. Therefore

\[
 \operatorname{arsinh}(1)=\int_0^1\frac{dt}{\sqrt{1+t^2}}
 >1-\frac16+\frac3{40}-\frac5{112}
 =\frac{1451}{1680}>\frac67,
\]

which proves (4), without a numerical estimate of any model coefficient.

Put j_U=j(0) and j_L=j_U sech^2(alpha). We claim

\[
 0<j_L\le j(z)\le j_U\le1\quad (|z|\le1),\qquad
 r_*:=\frac{j_U}{j_L}=\cosh^2\alpha<2.                \tag{5}
\]

For the upper bound, express sech^2 through its level sets. Each set
{x:sech^2 x>t}, 0<t<1, is a symmetric interval (-r_t,r_t).
The probability that a centered Gaussian translated by a lies in this
interval is maximized at a=0. To check this, its derivative for a>0 is
phi_tau(r_t+a)-phi_tau(r_t-a)<0. Integrating over t proves the upper
bound, and also proves that the convolution is strictly decreasing for
positive translations. Here phi_tau is the centered Gaussian density
of variance tau; differentiating these interval probabilities is valid
since the density is bounded.

For the lower bound, for any real x,a, direct addition gives

\[
 \frac{\operatorname{sech}^2(x+a)+\operatorname{sech}^2(x-a)}2
 =\operatorname{sech}^2x\operatorname{sech}^2a\,
   \frac{1+\tanh^2x\tanh^2a}{(1-\tanh^2x\tanh^2a)^2}
 \ge\operatorname{sech}^2x\operatorname{sech}^2a.
\]

Use symmetry of the Gaussian x and take a=alpha z. This yields (5);
its last inequality follows from (4).

Since kappa(0)=0 and kappa'=alpha j,

\[
              0<\beta\le\alpha vj_U,\qquad\gamma=Ej(h).
                                                            \tag{6}
\]

Conditional Gaussian integration by parts gives
E[Z k | h]=sqrt(tau) j(h). Cauchy--Schwarz, using EZ=0 and EZ^2=1,
therefore gives Var(k|h)>=tau j(h)^2. All boundary terms vanish because
k and its derivatives are bounded and the Gaussian density decays.
Also E kappa(h)^2>=beta^2/v. Hence

\[
 b_*^2=Ek^2+\eta-\frac{\beta^2}{v+\eta}
 \ge\tau Ej(h)^2+\eta+\frac{\beta^2\eta}{v(v+\eta)}.
                                                            \tag{7}
\]

Equations (5)--(7) imply

\[
 Lj_L=\tau\gamma j_L+
       \frac{\alpha\beta\eta j_L}{v+\eta}
 \le\tau Ej(h)^2+
       \frac{\alpha^2v\eta j_Uj_L}{v+\eta}
 <\tau Ej(h)^2+\eta\le b_*^2.
\]

Thus 0<B<1/j_L. For every z in [-1,1],

\[
 \begin{aligned}
 \ell'(z)
 &=\alpha\lambda+B\left(\alpha j(z)-\frac\beta{v+\eta}\right)\\
 &\ge\alpha\lambda+\alpha B(j_L-\lambda j_U)\\
 &\ge\alpha\min\{\lambda,1-\lambda(r_*-1)\}\\
 &\ge\alpha\min\{\lambda,2-r_*\}>0.
 \end{aligned}                                             \tag{8}
\]

The penultimate line minimizes an affine function of B on [0,1/j_L].
This step is valid regardless of the sign of j_L-lambda j_U or A.

The function psi is odd and has psi'(x)=ell'(tanh x) sech^2 x>0.
For |t|<1, the Gaussian correlation derivative is

\[
 F'(t)=\frac1{c_*}E[\psi'(X)\operatorname{sech}^2Y_t]>0.    \tag{9}
\]

For completeness, take Y_t=tX+sqrt(1-t^2)Z with X,Z independent.
Differentiate the expectation, then integrate the resulting X and Z
terms by parts. The two terms containing tanh'' cancel, leaving (9).
On any compact subinterval of (-1,1), dominated convergence is justified
by bounded gate derivatives and Gaussian first moments. Continuity at
t=+/-1 follows from the same representation and bounded convergence.
Strict increase on the open interval consequently extends to the closed
interval. Symmetry gives F(-t)=-F(t), so F(0)=0 and F(t) has the sign of t.

**Conclusion.** For all u,v on S^1,

\[
 V(u)\ne0,\qquad
 V(u)=V(v)\iff u=v,\qquad
 V(u)=-V(v)\iff u=-v.                                  \tag{10}
\]

These are exact statements for the prescribed ridge and initialization.
The proof actually works for every positive ridge with the same raw core
constants, but no change of ridge is used in the present application.

## 3. Strict positivity of every admissible finite initial upper Gram

Let u_1,...,u_m be unit directions such that u_i is neither u_j nor -u_j
for i different from j. Define

\[
 T_i(b)=\tanh(b^TV(u_i)),\qquad
 K_{ij}=E_2[T_i(b_2)T_j(b_2)].                            \tag{11}
\]

Then K is strictly positive definite. There is no restriction m<=2.
The upper population is a continuum, and tanh is applied after the
two-dimensional linear form.

Here is a complete independence argument. The law of b_2 has a strictly
positive density throughout the open square (-1/c_*,1/c_*)^2, since its
coordinates are independent images of nondegenerate Gaussians under tanh.
If a real vector d satisfies d^TKd=0, then
sum_i d_i tanh(b^TV(u_i))=0 almost surely. Its continuity and the positive
density make it zero everywhere in the open square.

Choose a vector e outside the finitely many lines defined by
e dot V(u_i)=0 and e dot (V(u_i)+/-V(u_j))=0. All these defining vectors
are nonzero by (10); a finite union of lines cannot fill the plane
(one may intersect with any line not parallel to these lines and avoid
the finitely many resulting points). Thus the absolute values of
e dot V(u_i) are positive and pairwise distinct.

Restrict b=te for t close to zero. Absorb the signs of these dot products
into the coefficients and order their positive absolute values as
0<rho_1<...<rho_m. We obtain sum_i e_i tanh(rho_i t)=0 on an interval.
The left side is real analytic on the real line, so the equality extends
to every real t: at any finite endpoint of an interval of equality all
derivatives vanish by continuity, and its convergent Taylor series extends
that interval. Let t tend to infinity. First sum_i e_i=0. Next multiply
sum_i e_i(tanh(rho_i t)-1)=0 by exp(2 rho_1 t). Since
tanh(rho t)-1=-2/(exp(2 rho t)+1), the limit gives e_1=0.
Remove that term and repeat. All e_i, hence all d_i, vanish. This proves
strict positive definiteness of (11).

More generally, duplicates and antipodal pairs are the only finite
linear dependencies: group inputs into classes {u,-u}, use tanh oddness
inside each class, then apply the just-proved independence to one
representative of each class. Thus the rank of K is exactly the number
of represented unoriented directions.

## 4. Exact classification of initially stationary finite data

Consider any finite data law sum_i p_i delta_(u_i,y_i), with p_i>=0,
sum_i p_i=1, u_i on S^1, and finite real labels. The closure starts from
c=0, w=G, and M=D. Put t_i=p_i y_i. Its exact initial velocities are

\[
 \dot w(0)=0,\qquad\dot M(0)=0,\qquad
 \dot c(0,b)=2\sum_i t_iT_i(b),\qquad
 \dot f(0,u_j)=2\sum_iK_{ji}t_i.                         \tag{12}
\]

The first two equalities hold because the backward coefficient is zero
when c=0. In the physical metric the energy identity becomes

\[
            \mathcal L'(0)=-\|\dot c(0)\|_2^2
                          =-4t^TKt.                    \tag{13}
\]

For every class {r,-r}, choose one representative r and define its signed
label mass

\[
 \sigma_r=\sum_{u_i=r}p_i y_i-\sum_{u_i=-r}p_i y_i.
\]

The prescribed initial state is stationary if and only if every sigma_r
is zero. Necessity follows from (12) and the independence in Section 3;
sufficiency follows from input oddness. In the latter case all three
initial velocities vanish. The constant state is then a solution of the
autonomous equation, and characteristic uniqueness identifies it with
the prescribed trajectory. Bounded initialized features, Gaussian g with
finite second moment, and finite D satisfy the hypotheses of the source's
fixed-dimensional existence and uniqueness argument.

This is a classification for finite data laws. It does not silently assert
the analogous injectivity theorem for arbitrary signed continuum laws.
Zero input vectors, if admitted outside the circle, contribute no feature
or training force and may simply be removed for this classification.

For the requested equilateral triple,

\[
 x_i=\sqrt2\bigl(\cos(\theta+2\pi(i-1)/3),
                  \sin(\theta+2\pi(i-1)/3)\bigr),\quad u_i=x_i/\sqrt2,
\]
\[
 (y_1,y_2,y_3)=(1,1,-1),\qquad
 (p_1,p_2,p_3)=(3/8,1/8,1/2),\qquad
 t=(3/8,1/8,-1/2).
\]

For every theta, the three directions are distinct and no two are antipodal.
Their initialized vectors are nonzero and pairwise unequal even up to sign,
and their upper feature Gram is strictly positive definite. Consequently

\[
 \mathcal L(0)=1,\qquad \dot c(0)\ne0,\qquad
 (\dot f(0,u_i))_{i=1}^3\ne0,\qquad\mathcal L'(0)<0.    \tag{14}
\]

The total signed label mass is zero, but that scalar cancellation does not
make the full closure stationary. The three nonidentical upper features
retain their separate contributions.

There is even a nonquantitative constant kappa_eq>0 such that
K(theta)>=kappa_eq I_3 for every theta. Indeed, K depends continuously
on theta by bounded convergence, and its quadratic form is strictly
positive on the compact set [0,2pi] times the unit sphere in R^3.
Its minimum there is positive. Since |t|^2=13/32, this gives
L'(0)<=-13 kappa_eq/8 uniformly over theta. This is an existence bound,
not a computed or certified numerical value.

For each fixed data configuration satisfying the strict-positivity
hypothesis, continuity of the trained upper features also preserves its
Gram's positivity on some initial time interval. No all-time lower bound
or later-time stationary-state classification follows from this argument.

## 5. What rotation symmetry is and is not available

Signed coordinate permutations are exact symmetries. If S is a 2-by-2
signed permutation matrix, its action on lower features is diag(S,S),
on upper features is S, and it preserves both initialized joint laws.
Equation (1) intertwines these actions. After rotating the data by S,
transform the characteristic row field by
w_S(SG,SZ)=S w(G,Z), the readout by c_S(S Ztilde)=c(Ztilde), and
the middle matrix by M_S=S M diag(S,S)^T. Direct substitution in the
full equations preserves every contraction and the physical metric.
Uniqueness therefore gives exact covariance for this finite symmetry group.
In particular V(Su)=SV(u).

Full orthogonal covariance of V is false. This can be proved without
numerically comparing angles. The function j(z) is strictly decreasing
for z>0, by the level-set argument in Section 2. Since B,alpha>0,
ell'(z)=A+B alpha j(z) is positive and strictly decreasing there.
Thus psi'(x)=ell'(tanh x) sech^2 x is positive, even, and strictly
decreasing for x>0. Gaussian integration by parts twice gives

\[
 E\psi'''(G)=E[(G^2-1)\psi'(G)]<0.                    \tag{15}
\]

To verify the strict sign, take independent G,G'. The covariance on the
right equals one half of
E[(G^2-G'^2)(psi'(G)-psi'(G'))], whose integrand is negative whenever
G^2 differs from G'^2. The same proof with psi replaced by tanh gives
E tanh'''(G)<0. All derivatives here are bounded, so all integrations
by parts and differentiations are justified.

Applying the correlation differentiation in (9) three times at zero gives

\[
                F'''(0)=\frac1{c_*}E\psi'''(G)
                                      E\tanh'''(G)>0.  \tag{16}
\]

Thus F is not linear. If V were orthogonally covariant on S^1, rotating
e_1 to any u would give V(u)=F(1)u. Its first coordinate would force
F(t)=F(1)t on [-1,1], contradicting (16).

There is also a direct obstruction at the lower dictionary level. A
rotation taking e_1 to a direction u with u_1u_2 nonzero would send the
feature tanh G_1 to tanh(u dot G). Suppose the latter belonged to the
linear span of h_1,h_2,k_1,k_2. Conditional on G, independent nondegenerate
Z_1,Z_2 force both k coefficients to be zero, because their conditional
variances are strictly positive. We would then have
tanh(u dot G)=a tanh G_1+b tanh G_2. Positive Gaussian density and
continuity extend this identity to every G in R^2. Its mixed second
derivative would say u_1u_2 tanh''(u dot G)=0 everywhere, a contradiction.
Hence the fixed initialized lower span is not preserved by generic rotations.

These facts rule out using unrestricted rotation covariance of the fixed
p=1 representation as a proof step. The upper feature Gram need not be
assumed to depend only on angular differences. Noncovariance of V alone
is not presented as a proof that no accidental Gram-level rotational
identity can hold. The every-angle positivity in Section 4 was proved
directly, without transporting a single angle by a presumed symmetry.

## 6. Check record and remaining limits

The author checked dimensions, ridge factors and the transpose convention
against the exact initializer; rederived (3) by multiplying both nonzero
bands; proved all scalar bounds without numerical integration; treated
correlation endpoints by continuity; and checked the independence proof
also for collinear unequal-magnitude upper vectors. The stationarity test
includes duplicates, antipodal collisions, zero label weights and signed
label cancellations. Source hashes above were recorded after reading.

The new claims are exact initialization results with complete proofs in
Sections 1--5. They have not received an independent review. They do not
show that V retains injectivity at later times, that the readout Gram has
an all-time spectral gap, that training converges to zero loss, that a
particular scalar invariant manifold is reached, or that fixed p=1
identifies the full neural population flow. Those are separate proof
obligations; initial strict positivity alone does not settle them.
