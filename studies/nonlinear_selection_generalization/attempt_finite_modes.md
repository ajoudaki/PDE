# Finite target modes with an explicit nonlinear approximation floor

Root independent derivation, frozen first-round candidate. Input scope: the
frozen study contract; C.4.9 completely; global-nonlinear A.1--A.4, B.1's
complete GF construction, C.4.5.1 sections 1--3 and 5, complete C.4.5.2,
C.4.6.3 sections 1--6; special-data III.F.1--III.F.11. The time-40 statements
C.4.7--C.4.8 were read for scope only and are not statistical dependencies.
Other attempts have supplied progress messages only, not their derivations.
This route uses a finite space containing the reference residual exactly,
rather than estimating the unknown Fourier tail of that residual.

Status: candidate proof under the explicitly separate arbitrary-law
continuation premise. No milestone or promotion claim.

## 1. A signed-measure version of protected-row separation

Let rho be normalized arc measure and let mu be an odd finite signed measure
on the circle whose only atoms are among +/-e1,+/-e2. Odd means pushforward
under u -> -u equals -mu. If

    integral tanh(w_dagger . u) dmu(u)=0 in L2(Omega1),

then mu=0. Here and below the same statement holds for an absolutely
continuous part merely in L1, not just a smooth density.

Proof. Fix a unit vector v with both coordinates nonzero. C.4.9 B.2's
protected events give, for all sufficiently large integers r, a set of
positive probability where |g-rv|_infty<=1, N<=r^2, and

    |w_dagger,a-g_a| <=20e^2 r^2 exp(-2 rho_v r),
    rho_v=min(|v1|,|v2|)/2>0.

The proof uses Pr(N>r^2)<=exp(-r^4/(e^2 C_*^2)) and the Gaussian box lower
bound (2/pi)exp(-(r+sqrt(2))^2/2). Intersect each event with the full-measure
set on which the integral vanishes and choose a coordinate from it. Along
these choices w_dagger/r -> v. Thus tanh(w_dagger.u) -> sign(v.u) off the
two points perpendicular to v. Neither point is an anchor, and mu has no
other atoms. Dominated convergence for its total variation gives

    integral sign(v.u) dmu(u)=0.

This holds for every v with nonzero coordinates. Parameterizing directions
by angles, k(alpha)=sign(cos(alpha)) has complex Fourier coefficient

    k_hat(j)=2 sin(j*pi/2)/(pi*j) (j!=0), k_hat(0)=0.

To check this formula, integrate cos(j*alpha) on (-pi/2,pi/2), subtract its
integral on the complementary half circle, and divide by 2*pi; the sine
integral is zero. Fubini therefore makes every odd Fourier coefficient of
mu zero. Oddness already makes every even coefficient zero.

Here is a contained uniqueness argument for measures. The Fejer kernel
F_l(alpha)=|sum_{j=0}^l exp(ij alpha)|^2/(l+1) is nonnegative, has rho
integral one, and for circular |alpha|>=delta its value is at most
1/((l+1)sin(delta/2)^2). Uniform continuity splits its convolution with any
continuous function into a small near-diagonal error and a vanishing
off-diagonal error. Thus its trigonometric-polynomial convolutions converge
uniformly to that function. A measure annihilating all Fourier modes
annihilates those convolutions and then every continuous function. Continuous
functions determine a finite signed Borel measure (approximate compact-set
indicators inside open neighborhoods by distance-ratio continuous functions).
Hence mu=0.

The same conclusion holds if

    integral delta_dagger(u) tensor H1_dagger(u) dmu(u)=0 in HS,
    delta_dagger(u)=c_dagger sech^2 Z2_dagger(u).

Indeed HS operators here are L2 kernels on Omega2 x Omega1: the isometry
for finite tensor sums follows by expanding their squared norms, and
completion plus Bochner approximation gives it for this integral. Fubini
therefore gives, for almost every omega2, a zero first-layer integral with
signed measure delta_dagger(u,omega2)dmu(u). Jointly measurable
representatives exist by strong L2 input continuity and finite simple
approximation. Choose an omega2 where c_dagger is nonzero, all four anchor
preactivations are finite, and the other preactivations are finite mu-almost
everywhere. Such choices have positive probability since c_dagger!=0, while
the failures have measure zero by Fubini. Choose negative-input
representatives to preserve evenness of the gate; forward oddness supplies
that identity in L2. This weighted measure is odd and finite. The preceding
argument makes it zero. Its weighting factor is nonzero mu-almost everywhere,
so mu=0. There is no independence assumption between c, the gates and A.

## 2. The endpoint force sees every odd residual

At the reference endpoint let d(u)=Pi_dagger g_dagger(u), and let d_H(u) be
its row-plus-middle block. For density p set p_s(u)=(p(u)+p(-u))/2. Let
H_p be the closed odd subspace of L2(p rho). Its norm equals the norm using
p_s. Define bounded operators

    T_p r = integral r(u)d(u)p(u)drho(u),
    T_H,p r = integral r(u)d_H(u)p(u)drho(u).

Their norms are at most L0<17. Both operators are injective. For proof,
write v=integral r g p and beta=M_dagger^(-1)G_dagger^*v. If the middle
block of T_p r vanishes, apply section 1 to

    mu = r p_s rho - (1/2)sum_a beta_a(delta_ea-delta_-ea).

The continuous and atomic parts of the zero measure must both vanish.
Since p_s>=1/2, r=0 in H_p. This proves injectivity even for the middle
block alone, hence for T_H,p and T_p.

This is not a uniform continuum coercivity assertion. The kernel d(u) is
continuous into the raw Hilbert space by C.4.9 B.3 and bounded. Finite input
partitions approximate it uniformly by a finite-valued kernel. The resulting
T_p are finite rank and converge in operator norm, so T_p is compact. On
an infinite-dimensional H_p no positive lower bound can hold on its whole
unit sphere: any orthonormal sequence converges weakly to zero and a compact
operator sends it to zero in norm (use finite-rank approximants). The
following finite-mode lower bound is the appropriate statement.

## 3. Reference matrices associated with independently specified target modes

Set q0(alpha)=cos(alpha)^3-sin(alpha)^3 and h(alpha)=sin(2*alpha)^2.
For each integer N>=0 define the fixed finite-dimensional function space

    E_N=span{F_*-q0, h cos((2k+1)alpha), h sin((2k+1)alpha): 0<=k<=N}.

Every generator is odd, Lipschitz and zero at the anchors. The only network
quantity in this space is the already established reference F_*; the target
class itself was frozen independently. If generators are linearly dependent,
delete dependencies by their L2(rho) Gram and choose any orthonormal basis
b_1,...,b_d of the resulting nonzero space. It is nonzero since h cos(alpha)
is nonzero. For p in the frozen compact density class define d by d matrices

    C_N(p)_{ij}=integral b_i b_j p drho,
    A_N(p)_{ij}=<T_p b_i,T_p b_j>,
    A_H,N(p)_{ij}=<T_H,p b_i,T_H,p b_j>.

C_N lies between (1/2)I and 2I. The other two matrices are positive
definite by section 2. Define reference quantities

    lambda_N = min_p min_{z^T C_N(p)z=1} z^T A_N(p)z >0,
    lambda_H,N = min_p min_{z^T C_N(p)z=1} z^T A_H,N(p)z >0.

These are specified finite generalized eigenvalue problems and a compact
density minimization, not risks of an unknown trained flow. To prove the
strict inequalities uniformly, the densities are bounded and equicontinuous;
successive finite circle nets and diagonal extraction give a uniformly
convergent subsequence of any sequence (extend from nets using their common
Lipschitz bound). The density bounds, normalization and Lipschitz bound pass
to the limit. The coefficient vectors in the displayed constraints have
Euclidean norm at most sqrt(2), hence also have convergent subsequences.
All matrix entries depend continuously on p in the uniform norm. A sequence
with Rayleigh values tending to zero would therefore contradict injectivity
at its limiting density and nonzero limiting vector. This proves positivity.
It also specifies exactly the dependence on target degree N and density
regularity D. No evaluated useful numerical value or lower bound uniform
as N increases is asserted.

For a target in the frozen infinite weighted Fourier class, q_N truncates
its v series at N. Then F_*-q_N belongs to E_N and

    ||q-q_N||_infty <= a_N := R/(2N+3)^s.

For targets of declared finite degree N, take a_N=0 instead. This exact
zero is useful: no unknown Fourier approximation of F_* is needed.

## 4. A nonlinear population contraction with an explicit floor

Premise C: arbitrary-law constrained selection exists through T_ex>0,
retaining C.4.9's source tube and endpoint neighborhood. On the unit endpoint
raw ball with protected anchor Gram use its explicit constants C_f,C_d,L1,
and set B0=sqrt(10)+1 and V=2(C+2)L1, C=sqrt(10). Labels in this class are
bounded by one. Then ||theta'||<=V, ||theta(t)-theta_dagger||<=Vt,
||f_theta-F_*||_infty<=C_f Vt, and

    sup_u ||d_theta(u)-d(u)|| <= C_d sqrt(Vt).

These are exactly factorwise endpoint estimates, not frozen dynamics. Let
r_t=f_theta(t)-q, E(t)=||r_t||_p^2. Its exact evolving-feature identity is

    E'(t)=-4 ||T_theta,p r_t||^2,
    T_theta,p r=integral r(u)Pi_theta g_theta(u)p(u)drho(u).

Bochner integration, the scalar chain rule and boundedness justify
differentiating the risk; centered noise contributes no force.

Let P_N be the orthogonal projection onto E_N in H_p. Because r_0 is within
a_N of that space and prediction moves by at most C_f Vt,

    ||(I-P_N)r_t||_p <= a_N+C_f Vt =: b(t).

The inequality ||x+y||^2 >= (1/2)||x||^2-||y||^2 follows by completing
the square: its difference is (1/2)||x+2y||^2. Apply it twice, first to
T_theta r = T_p r +(T_theta-T_p)r and then to
T_p r=T_p P_N r+T_p(I-P_N)r. Since ||T_p||<=L0 and
||T_theta-T_p||<=C_d sqrt(Vt), one obtains

    ||T_theta r_t||^2
      >= (lambda_N/4-C_d^2 Vt) E(t)
             -(lambda_N/4+L0^2/2)b(t)^2.

For any admitted T satisfying C_d^2 VT<=lambda_N/8, define

    A_N(T)=2(1+2L0^2/lambda_N)(a_N+C_f VT)^2.

Multiplying the resulting scalar differential inequality by
exp(lambda_N t/2) and integrating proves, for 0<=t<=T,

    E(t) <= exp(-lambda_N t/2) E(0)
                  + A_N(T)(1-exp(-lambda_N t/2)).

E(0)<=B0^2 is an available class bound. The floor is fully specified by
target truncation a_N, degree-dependent reference lambda_N, and the explicit
nonlinear movement estimate C_f VT. It is not defined to equal trained
risk. More effort contracts the initial error towards this floor within
the admitted interval. Increasing N decreases the target tail but can
worsen lambda_N and the admissible duration; no universal consistency or
all-time fitting follows. The actual theta and its hidden features continue
evolving throughout the proof.

## 5. A nonempty robust class and an available positive stopping time

Fix R>0, finite N>=0 and any s>=1. Inside the frozen class consider

    v_c=(R/4)(cos(alpha)+sin(alpha)),
    sum_k (2k+1)^s(|a_k-a_k,c|+|b_k-b_k,c|) <= R/8.

Its weighted coefficient norm is at most 5R/8<R. It has a relative open
interior by taking strict inequality; no input support is restricted.
At alpha=pi/4, q0=F_*=0 by the established swap symmetry. Therefore

    q(pi/4) >= b := R/(2sqrt(2))-R/8 >0.

The target is at most 7-Lipschitz in angle: |q0'|<=6,
|h'|<=2, ||v||<=R and ||v'||<=R. F_* is 76-Lipschitz, so r_0 is
83-Lipschitz. On the arc of radius b/166 about pi/4, |r_0|>=b/2. Since
p>=1/2,

    E(0) >= e0 := b^3/(1328*pi)>0.

Let T_ball be an explicit positive duration ensuring Premise C and its
unit/anchor neighborhood, and choose

    T_* <= min{T_ball, lambda_N/(8C_d^2 V),
                 sqrt(e0/[4(1+2L0^2/lambda_N)])/(C_f V)}.

All these quantities depend only on the frozen class and proved reference
quantities. Since a_N=0 for finite-degree targets, A_N(T_*)<=e0/2. Hence
at every t in [0,T_*],

    E(0)-E(t) >= (1-exp(-lambda_N t/2)) e0/2.

This is integrated finite-episode learning on a whole-circle test law. It
does not infer a finite result from an uncontrolled initial derivative.
Choose T_*>0 by, for example, one half of the displayed positive minimum.
It is an available deterministic stopping time; no unknown q or trained
risk is consulted. Sampling error from sampling_lemma.md may be made
smaller than this margin by a finite threshold on m. That threshold will
be made explicit when the continuation constants are assembled.

## 6. Exact remaining work

Premise C and actual finite-GF capture are the independent continuation
obligation. Hidden-gradient positivity from section 2 is not yet a finite
activation-displacement theorem in this file; integrate a fixed-readout
contrast with a proved derivative modulus, as required by C.4.9. The
statistical lemma requires a proved uniform reached Osgood constant.
Independent complete reviews remain mandatory before any completed claim.
