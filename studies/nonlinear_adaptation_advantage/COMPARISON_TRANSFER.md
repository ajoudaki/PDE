# Full frozen comparator and shared-sample transfer

Author: root, 2026-09-12. Claim type: proved consequences of the established
C.4.9–C.4.10 input theorems, except the explicitly conditional comparison
corollary. These results do not supply the missing positive population margin.
Internal verification is recorded separately; nothing here is promoted.

## 1. Setup and complete frozen evolution

Use the exact model and raw metric of RESEARCH_CONTRACT.md and the angular
pullback convention. Write H_p for the real odd subspace of L²(p rho), and
E for the raw parameter increment Hilbert space. Put

    d(u)=Pi_dagger g_dagger(u),
    D_p a = integral a(u)d(u)p(u)d rho(u),
    K_p = D_p* D_p.

These symbols distinguish the prediction operator K_p from the network's
middle increment K. Products of odd functions are even, so p can be replaced
by p_s(u)=(p(u)+p(-u))/2 throughout these operators and inner products.
C.4.10.3 proves that D_p is bounded, compact and injective, even in its middle
block, for every p in P_D. Its bound is ||D_p||<=L_0, with L_0 from NSS3.
The adjoint is (D_p* z)(u)=<d(u),z>_raw. Thus K_p is the full frozen kernel
operator and is self-adjoint, positive, injective, with norm at most L_0².
All three parameter blocks are included.

For r_0=F_*-q define the exponential by its absolutely operator-norm
convergent series. The solution of the comparator in the question is

    r_fr(t)=exp(-2t K_p)r_0,       F_fr=q+r_fr.                 (1)

Termwise differentiation on bounded time intervals proves the equation.
Uniqueness follows by applying the energy identity to a difference of two
solutions. For S(t)=exp(-2tK_p),

    (||S(t)v||_p²)'=-4<D_p S(t)v,D_p S(t)v>_raw<=0.           (2)

Hence S(t) is a contraction; no pointwise maximum principle is asserted.
Also let z(0)=0 and solve in raw space

    z'=-2[D_p D_p* z + D_p r_0].                             (3)

The bounded linear equation exists by its exponential and integral formula,
and F_fr=F_*+D_p* z follows by differentiation and uniqueness. This supplies
the whole-circle continuous representative. In fact
||z(t)||<=2t L_0||r_0||_p, because (2) bounds its driving residual. Pointwise
anchor preservation follows from d(e_1)=d(e_2)=0, not from point evaluation
on an arbitrary L² equivalence class.

The derivative of both nonlinear and frozen risk at zero is exactly

    E'(0)=-4||D_p r_0||².                                    (4)

For the nonlinear side use C.4.10.2 NSC24a and the centered noise condition.
For the frozen side use (2). Thus initial risk decrease and B's positive
conditioning do not distinguish the two learners.

## 2. No permanent frozen approximation floor on this class

For every fixed p and every odd r_0 in H_p,

    ||S(t)r_0||_p -> 0 as t -> infinity.                      (5)

Here is a proof without assuming a spectral gap. The orthogonal complement
of ran(K_p) is ker(K_p), since self-adjointness gives
<v,K_p w>=0 for all w iff K_p v=0. Injectivity therefore makes ran(K_p)
dense. For v in H_p, put h(t)=<S(t)v,K_p S(t)v>. Commutation of the power
series with K_p and differentiation give

    h'(t)=-4||K_p S(t)v||².

Moreover ||K_p S(t)v|| is nonincreasing by applying (2) to K_p v. Since
h>=0, integration yields

    t ||S(t)K_p v||² <= ||K_p|| ||v||² / 4.

Approximate arbitrary r_0 in norm by K_p v, use the contraction for the
approximation error, then send t to infinity. This proves (5).

For fixed coefficient cap N, bounded closed coefficient ranges and p in P_D,
the risk convergence is also uniform over this compact product family.
Here are the needed continuity details. On the common odd space L²(rho),
the conjugated operator has kernel

    sqrt(p_s(u)) k_dagger(u,v) sqrt(p_s(v)),

and initial residual sqrt(p_s)(F_*-q). Uniform convergence of densities
implies operator-norm convergence of these bounded kernels and norm
convergence of the residuals. The exponential series converges uniformly on
bounded operator balls for each fixed t, so risk is continuous in (p,q).
P_D is compact by the finite-net/diagonal proof in NSS19, and bounded closed
finite coefficient sets are compact. For a prescribed positive risk tolerance,
(5) and continuity give an open cover by parameter neighborhoods with risk
below tolerance at a finite time. A finite subcover and risk monotonicity
give one finite time for the whole class. This proof supplies no practical
rate or cumulative-clock budget.

Consequently E₀ cannot be an irreducible approximation separation, and a
matched-clock advantage would not imply superiority under unrestricted
additional frozen training. This observation neither proves nor disproves
an advantage on E₀'s finite episode.

## 3. The two empirical learners on exactly the same observations

Assume B's |q|<=1, |Y|<=1, conditional centering, and conditional variance
at most sigma², with iid pairs (X_i,Y_i). The known anchors retain exactly
their prescribed weights in actual mixture GF. Nonlinear empirical selection
is theta_hat of C.4.10.2, with P_hat=f_(theta_hat). Define the frozen empirical
learner by

    z_hat'=-2/m sum_i [F_*(X_i)+<d(X_i),z_hat>-Y_i]d(X_i),
    z_hat(0)=0,       F_fr_hat(u)=F_*(u)+<d(u),z_hat>.         (6)

The same pairs are used in both learners. Each empirical raw operator
A_hat=m^(-1)sum_i d(X_i) tensor d(X_i) is positive and bounded, including
repeated observations. Thus (6) is globally well posed and its homogeneous
semigroup is a contraction by the same energy proof as (2).

Let B_0=sqrt(10)+1, so ||F_*-q||_p<=B_0. For failure allowances delta_FI>0
and delta_Fxi>0 define

    C_F=2T L_0 [B_0/sqrt(delta_FI)+sigma/sqrt(delta_Fxi)],
    beta_m=L_0 C_F/sqrt(m).                                  (7)

In the noiseless case omit the noise term and its allowance. With probability
at least 1-delta_FI-delta_Fxi,

    sup_(t<=T) ||z_hat(t)-z(t)|| <= C_F/sqrt(m),
    sup_(t<=T,u) |F_fr_hat(t,u)-F_fr(t,u)| <= beta_m.           (8)

Proof: evaluate the random error on the deterministic population path z(t).
Let I_m(t) be the centered sample average of r_fr(t,X)d(X), and N_m(t)
the sample average of xi_i d(X_i). Expanding squared Hilbert norms, iid
centering eliminates cross terms. By (2),

    E||I_m(t)||² <= L_0² B_0²/m,
    E||N_m(t)||² <= L_0² sigma²/m.

Conditional centering and independence of the iid labels given the sampled
inputs justify the second calculation. The error equation is exactly

    (z_hat-z)'=-2 A_hat(z_hat-z)-2I_m+2N_m.

Variation of constants and contraction bound its norm by
2 integral_0^T (||I_m||+||N_m||) dt. Cauchy–Schwarz in time followed by
Tonelli bounds the second moment of each integral by 4T² times the
corresponding variance bound. Markov and a union bound give (8). All random
forcing is evaluated on the population path; no independence of trained
empirical features and their labels is used.

Since ||F_fr-q||_p<=B_0, factorization of the squared norm gives

    |E_nu(F_fr_hat(t))-E_nu(F_fr(t))| <= 2B_0 beta_m+beta_m².  (9)

For the nonlinear learner take the constants L, mathcal K, c_b and T_c
from C.4.10.2 with Y_0=1. For T<=T_c, C.4.10.4 NGL8–NGL13 give

    C_N=2TL[B_0/sqrt(delta_NI)+sigma/sqrt(delta_Nxi)],
    eta_m=C_N/sqrt(m),
    O_T(eta)=e exp[-(sqrt(log(e/eta))-mathcal K T/2)²],
    alpha_m=2(c_b+1)L O_T(eta_m),                             (10)

and simultaneous risk error at most alpha_m with probability at least
1-delta_NI-delta_Nxi. The branch condition is
sqrt(log(e/eta_m))>1+mathcal K T/2, and O_T(0)=0.
Its proof uses the deterministic nonlinear population path and the exact
same centered Hilbert variance calculation, followed by the established
one-reference Osgood state comparison. The source-tube theorem holds for
every empirical law. No exceptional sample geometry is discarded.

There is no independence requirement between the events (8) and (10).
A union bound on their total failure allowance delta yields

    E_nu(F_fr_hat(T))-E_nu(P_hat(T))
    >= E_nu(F_fr(T))-E_nu(P_nu(T))
       -alpha_m-2B_0 beta_m-beta_m².                          (11)

This is uniform in constants over B's declared classes. It is a bound for
each task with that confidence, not one event asserting success for an
uncountable collection of independently resampled tasks.

## 4. Explicit conditional positive-margin threshold and actual GF

Suppose an independently proved population theorem supplies the very E₀
margin a>0 at common 0<T<=T_c on a declared family. This is an additional,
currently unproved hypothesis, not a result of the present note. Define

    d_N=min(1/2, a/[16(c_b+1)L]),
    eta_N=e exp[-(sqrt(log(e/d_N))+mathcal K T/2)²],
    beta_*=min(1, a/[8(2B_0+1)]),
    m_*=max(1, ceil((C_N/eta_N)²), ceil((L_0 C_F/beta_*)²)).   (12)

Allocate four allowances delta/4 when sigma>0, and two input allowances
delta/2 when sigma=0. For m>=m_*, (10)'s branch holds strictly since
d_N<=1/2. It gives alpha_m<=a/8. Also beta_m<=beta_*<=1, so
2B_0 beta_m+beta_m²<=(2B_0+1)beta_*<=a/8. Thus (11) gives the
empirical comparison margin 3a/4 with probability at least 1-delta.

For each separately fixed family member, m and epsilon>0, C.4.10.2 captures
actual Gaussian-initialized GF of the empirical fixed mixture at T/epsilon.
Width is taken first, contamination second. Conditioning on any realized
sample is legitimate because the theorem covers every empirical law. Bounded
conditional failure probabilities allow integration over samples by dominated
convergence. Whole-circle prediction convergence implies risk convergence
using | ||f-q||²-||g-q||² |<=||f-g||[2||g-q||+||f-g||]. Consequently

    liminf_(epsilon->0) liminf_(n->infinity)
      Pr{ E_nu(F_fr_hat(T))
          -E_nu(f_(n,mu_hat)(T/epsilon)) >= a/2 } >= 1-delta. (13)

The spare a/4 covers the nonlinear finite-network risk error. Actual training
starts at its original initialization, with its finite Gaussian readout and
fixed mixture throughout. A reference endpoint is used only in the limiting
description and comparator. No width threshold uniform over family members,
no simultaneous width/epsilon rate and no GD extension is claimed. Increasing
m after the two inner limits makes the failure allowance arbitrarily small.

## 5. Exact finite Gram representation and its approximation boundary

Given exact values of F_* and k_dagger, (6) has a finite representation:
its sample residual vector obeys

    r_hat'=-2 K_m r_hat,    (K_m)_ij=k_dagger(X_i,X_j)/m,
    F_fr_hat(t,u)=F_*(u)-2/m sum_i integral_0^t r_hat(s)_i ds
                                                    k_dagger(u,X_i). (14)

Differentiate (14) at each sample to verify the equation, and use uniqueness.
This is a finite linear algebra representation given exact endpoint queries;
it is not a certified way to compute the endpoint Gaussian action or a
finite-neural fitted-endpoint approximation.

For clarity, a proposed approximate implementation must supply its own input
errors. If continuous tilde F_* and tilde k satisfy uniform errors zeta, chi,
and sup|k_dagger|<=K_0=L_0², sup|tilde k|<=K_1=K_0+chi, then the two empirical
prediction equations give, for t<=T,

    sup_u |tilde F_fr_hat(t,u)-F_fr_hat(t,u)|
    <= exp(2K_1 T)[zeta+2T chi B_0 exp(2K_0 T)].              (15)

Indeed the exact empirical residual supremum obeys R(t)<=B_0+2K_0
integral_0^t R, hence R(t)<=B_0 exp(2K_0 t). Subtract the equations,
put the prediction difference under tilde k, and bound the remaining
kernel difference against that residual. The scalar integral inequality
gives (15). This proves stability to certified input errors; it does not
assert that any proposed finite Gaussian approximation achieves them.

## Dependencies and limitations

Root read C.4.9 and C.4.10 completely; global_nonlinear A.1–A.4,
C.4.5.1 §§1–3 and §5, C.4.5.2 §§1–4; and special_data_limits III.F in full.
These contain the used raw differentiation, canonical action/adjoint,
reference fitting, source-tube, separation, bounded-law continuation,
sampling and finite-GF bridges. No specialized external theorem is imported.
The proof does not use time-40 influence asymptotics or another study.

The conditioning/source constants inherited from B are unevaluated and may
be impractical. Most importantly, (12)–(13) have no unconditional positive
conclusion until the population advantage a is proved. A non-scalar mechanism
would still need its separate component inequality and robustness analysis.
