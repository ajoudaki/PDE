# Closing the learning, hidden-observation, and sample interfaces

Root synthesis of frozen candidates; candidate mathematical work, not a
promotion decision. This selects the finite target-mode contraction and the
fixed-readout hidden contrast. The independent relevance decision is pending.

All time variables below are slow time tau. N is the Fourier coefficient
index cap; the actual trigonometric degree is at most 2N+5. The robust result
uses fixed finite N>=0, R>0, s>=1 and density Lipschitz bound D. The broader
infinite-series class retains the explicit truncation bound but no consistency
claim. The full target class remains exactly the one frozen in README.

## Reference constants and a uniform robust subfamily

Use E_N, lambda_N and lambda_H,N from attempt_finite_modes.md. For the robust
family take a=R/4 and

    v=a(cos(alpha)+sin(alpha))+w,
    sum_{k=0}^N (2k+1)^s (|w_c,k|+|w_s,k|) <= a/4.

It has coefficient-budget slack and nonempty relative interior in each fixed
finite-N space. The symmetry argument in attempt_population.md gives

    E(0) >= e_* := (a^2/2)(sqrt(3/8)-1/4)^2 >0.

Here the symmetric function h(cos+sin), h=sin^2(2alpha), has squared
L2(rho) norm 3/8, while F_*-q0 is antisymmetric under coordinate swap.
Every density has p>=1/2. This proof uses full-circle mass, not continuity
from a favorable atom.

Set C=sqrt(10), B0=C+1 and let k=lambda_min(M_dagger)>0. Set
G0=sqrt(2)L0. With r0=F_*-q define

    u0=integral r0(u)g_dagger(u)p(u)drho,
    beta=M_dagger^(-1)G_dagger^*u0,
    d0=Pi_dagger u0.

Then ||r0||_p<=B0, |beta|<=B_beta:=G0 L0 B0/k and

    ||(d0)_hidden||^2 >= lambda_H,N ||r0||_p^2
                         >= gamma:=lambda_H,N e_*>0.

This quantitative minimum uses only the finite reference matrices already
proved positive, rather than an additional minimum over unknown trained risk.
Let S=B0+sqrt(2)B_beta and B2=2B0^2+B_beta^2.

## Finite paired second-hidden motion

Keep r0, beta and c_dagger fixed in the scalar hidden-only contrast

    O(theta)=integral r0(u)<c_dagger,H2_theta(u)>p(u)drho
                         -sum_a beta_a<c_dagger,H2_theta(e_a)>.

Its endpoint gradient is ((d0)_hidden,0). The actual constrained velocity is
V_theta=-2 integral (f_theta-q)Pi_theta g_theta p. At the endpoint

    O'(0)=-2||(d0)_hidden||^2 <= -2 gamma.

C.4.9 B.3's endpoint constants give, with d=||theta-theta_dagger||<=1,

    ||o_theta-o_dagger|| <= S C_g sqrt(d),
    ||V_theta-V_dagger|| <= C_V sqrt(d),
    C_V=2L1 C_f+2B0 C_d,
    ||V_theta||<=V=2(C+2)L1,
    ||o_dagger||<=L0 B0.

For the first inequality apply its fixed-readout hidden gradient bound and
integrate the absolute contrast coefficients. For the second subtract the
residual, bounded by C_f d, and the projected gradient, bounded by C_d sqrt(d).
Thus

    |O'(tau)-O'(0)| <= A_H sqrt(V tau),
    A_H=S C_g V+L0 B0 C_V.

If A_H sqrt(VT)<=gamma, this derivative stays at most -gamma throughout
[0,T]. Integrating the actual derivative, rather than its initial value,
gives |O(theta(tau))-O(theta_dagger)|>=gamma tau.

Use the observation law independent of the unknown test density:

    J2(theta)= (1/3)[integral ||H2_theta(u)-H2_dagger(u)||_2^2 drho
                         +sum_a ||H2_theta(e_a)-H2_dagger(e_a)||_2^2].

Since ||r0 p||_rho^2<=2||r0||_p^2, Cauchy-Schwarz in the upper population
and then the direct sum of the circle and two anchors yields

    |O(theta)-O(theta_dagger)|^2 <=3 C^2 B2 J2(theta).

Consequently J2(theta(tau))>=gamma^2 tau^2/(3 C^2 B2).
This is paired activation displacement on one initialized carrier. It is
not inferred from a nonzero parameter velocity alone.

## One available positive stop and the two margins

Let T_c>0 be the completed continuation theorem's common episode, reduced
if needed to its unit/anchor endpoint neighborhood. All its choices depend
only on the fixed reference and label bound one. Take one half of the minimum
of the following positive numbers:

    T_c,
    rho_a/(2V),
    lambda_N/(8C_d^2 V),
    sqrt(e_* / [4(1+2L0^2/lambda_N)])/(C_f V),
    gamma^2/(A_H^2 V).

Call this stop T. It uses N,R,s,D and reference constants, not q, the sample,
or a future trained answer. The finite target-mode floor has a_N=0 and

    A_N(T)=2(1+2L0^2/lambda_N)(C_f VT)^2 <= e_*/2.

The finite episode therefore has population margins

    a_*=(e_*/2)(1-exp(-lambda_N T/2))>0,
    j_*=gamma^2 T^2/(3 C^2 B2)>0.

At every smaller positive time the same contraction improves with time
towards the fixed floor A_N(T); the corresponding hidden bound grows as
tau^2. These are finite-episode claims. Reference constants are specified
mathematically and need not be numerically practical; no efficient numerical
evaluation of the stop is claimed.

## Quantitative sampling threshold and paired observations

Let L_f=L_g=L1, B_f=C+1, and H_L=sqrt(1+(M+1)^2), where M=2+sqrt(10).
On the common unit endpoint ball, factor subtraction gives

    sup_u ||H2_theta(u)-H2_bar_theta(u)||_2 <= H_L ||theta-bar_theta||.

Both individual hidden changes from the reference have L2 norm at most two.
Subtract their squared norms, use the last inequality and integrate the
observation law: |J2(theta)-J2(bar_theta)|<=4 H_L ||theta-bar_theta||.

For desired failure probability delta in (0,1), choose delta_I=delta_N=delta/2
(if sigma=0 take delta_I=delta and omit the noise term). Let K be the explicit
uniform Osgood coefficient supplied by internal_sampling_interface.md and set

    C_sample=2 T L1 (B0/sqrt(delta_I)+sigma/sqrt(delta_N)),
    eta_m=C_sample/sqrt(m),
    d_* = min(1/2, a_*/[8(B_f+1)L1], j_*/[16 H_L]),
    eta_* = e exp(-(sqrt(log(e/d_*))+KT/2)^2),
    m_* = max(1,ceil((C_sample/eta_*)^2)).

For every m>=m_* the statistical lemma gives, with probability at least
1-delta, sup_{tau<=T}||theta_hatnu-theta_nu||<=d_*. The three terms defining
d_* ensure that the Osgood formula is within its justified branch, the
empirical excess-risk penalty is at most a_*/4, and the paired activation
penalty is at most j_*/4. Thus the empirical constrained predictor has
unseen-risk gain at least 3a_*/4 and J2 at least 3j_*/4.

For all sufficiently large m (without the robust restriction), the general
combined oracle statement is

    sqrt(E_nu(P_hatnu(tau)))
      <= sqrt(exp(-lambda_N tau/2)E_nu(F_*)
                         +A_N(T)(1-exp(-lambda_N tau/2)))
                       +L1 O_T(eta_m), 0<=tau<=T,

provided T obeys the stated target-mode duration restriction. For an infinite
series the same A_N uses a_N=R/(2N+3)^s; finite targets use the exact omitted
coefficient tail, in particular zero at their declared cap. This displays
target complexity, sampling, centered noise, and effort in one bound.

## Actual finite GF and probability order

For fixed m and each realized sample, original mixture GF is captured at
each fixed epsilon>0 by width first, then selected as epsilon decreases.
The continuation theorem applies to every empirical law, even though it
need not have a density or the prescribed target shape. Integrate conditional
failure probabilities bounded by one. The reference network uses exactly
the same initial arrays, including readout, and the same physical time T/epsilon.

Define its observable by replacing each population squared norm in J2 with
the ordinary finite squared norm divided by n and replacing the reference
endpoint by that simultaneous reference flow. Uniform input Lipschitz bounds
and finite input nets pass the circle integral; same-array joint programs
pass all paired products. Therefore, for every fixed law in the robust
family and every m>=m_*,

    liminf_{epsilon down to 0} liminf_{n to infinity}
      Pr_samples,init{E_nu(F_*)-E_nu(f_n,hatmu(T/epsilon))>=a_*/2,
                                          J2,n,epsilon>=j_*/2}
      >=1-delta.

The same statement holds with the finite paired reference risk as benchmark,
by its convergence to F_*. Constants/m_* are uniform over the robust class;
this does not assert a width threshold or finite failure probability uniform
over that class. As m increases after these two limits, probabilities tend
to one because delta can be made arbitrarily small. No simultaneous rate,
raw-GD extension, source refresh, altered mixture law, or finite-readout
reset is used.
