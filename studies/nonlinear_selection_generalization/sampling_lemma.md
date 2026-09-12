# Sampling a nonlinear constrained episode

Author: root coordinator. Status: candidate conditional lemma, pending audit.
This file does not assert the continuation premises below. It supplies an
independent statistical argument for the new horizon, without C.4.8's time-40
law derivative or sampling expansion.

## Precisely stated premises

Let E be the raw Hilbert increment space of C.4.9 on its fixed initialized
carrier. Suppose for every probability law Q with labels in [-Y,Y], the
constrained equation

    theta_Q' = -2 integral (f_theta(u)-y) d_theta(u) dQ(u,y),
    d_theta(u) = Pi_theta g_theta(u), theta_Q(0)=theta_dagger,

has the asserted strong solution on [0,T]. Assume all these solutions stay
on one reached region with |f|<=B_f, ||g||<=L_g and scalar prediction raw
Lipschitz constant L_f. Suppose the one-reference comparison, uniformly over
Q, is

    ||V_Q(theta)-V_Q(bar theta)|| <= K omega(||theta-bar theta||),
    omega(z)=z sqrt(log(e/z)) for 0<z<=1, omega(0)=0,

when bar theta is the constructed population path and theta is another
admitted reached path. Enlarge omega increasingly beyond one. These are
deterministic premises; K and the region bounds must be supplied from the
source/continuation proof, not inferred from a generic Hilbert ODE.

Let (X_i,Y_i) be independent samples from nu, independent of initialization,
Y_i=q(X_i)+xi_i, E[xi_i|X_i]=0 and E[xi_i^2|X_i]<=sigma^2. The population
path theta_nu is deterministic. Assume its regression error E(t) is
nonincreasing, as follows directly from its gradient identity. Write
B_0>=sqrt(E(0)), with the available choice B_0=sqrt(10)+1 in the frozen class.

## Separate input and centered-noise fluctuations

Put d_t(x)=Pi_theta_nu(t) g_theta_nu(t)(x), r_t=f_theta_nu(t)-q. Define

    I_m(t)=m^(-1) sum_i r_t(X_i)d_t(X_i)-E_X[r_t(X)d_t(X)],
    N_m(t)=m^(-1) sum_i xi_i d_t(X_i).

These are strongly measurable Hilbert variables. The finite moments below
follow from ||d_t||<=L_g and the stated bounds. Independent centered Hilbert
variables have zero cross inner-product expectation: condition on one of
the two variables. Expanding the squared norm of each average therefore
gives

    E ||I_m(t)||^2 <= L_g^2 E(t)/m <= L_g^2 B_0^2/m,
    E[||N_m(t)||^2 | X_1,...,X_m]
      = m^(-2) sum_i E[xi_i^2|X_i] ||d_t(X_i)||^2
      <= L_g^2 sigma^2/m.

Independence of the observation pairs supplies conditional independence of
their labels given their inputs; all cross terms vanish. There is no
independence assertion for the empirical path, which has not been used in
these fluctuations.

For Z_I=2 integral_0^T ||I_m(t)|| dt and
Z_N=2 integral_0^T ||N_m(t)|| dt, scalar Cauchy-Schwarz in time and Tonelli give

    E Z_I^2 <= 4 T^2 L_g^2 B_0^2/m,
    E Z_N^2 <= 4 T^2 L_g^2 sigma^2/m.

For positive delta_I,delta_N with delta_I+delta_N<1, Markov and a union
bound imply, with probability at least 1-delta_I-delta_N,

    Z_I+Z_N <= eta_m := (2 T L_g/sqrt(m))
                  (B_0/sqrt(delta_I)+sigma/sqrt(delta_N)).

If sigma=0, then N_m=0 almost surely and its failure allowance is unnecessary.
This explicitly separates input sampling from centered label noise; m counts
only the added observations. Known anchor weights never fluctuate.

## Stability on the actual slow interval

Subtract the empirical and population integral equations. First compare the
two states under the empirical law, using the deterministic one-reference
bound. Then evaluate the law difference at the deterministic population
path, where it equals -2 I_m+2 N_m. On the preceding event, for t<=T,

    D(t):=||theta_nuhat(t)-theta_nu(t)||
      <= eta_m + K integral_0^t omega(D(s)) ds.

For 0<eta<=1 define

    O_T(eta)=e exp(-(sqrt(log(e/eta))-KT/2)^2),

provided sqrt(log(e/eta))>1+KT/2; this ensures the right side is below one.
Let Z(t)=eta+K integral_0^t omega(D(s))ds. Before a first exit at one,
Z'>=0, D<=Z and Z'<=K Z sqrt(log(e/Z)). Differentiating
sqrt(log(e/Z)) and integrating gives Z(t)<=O_t(eta). The displayed
strict threshold prevents that first exit. Thus

    sup_{t<=T} D(t) <= O_T(eta_m),
    sup_{t<=T,x}|P_nuhat(t,x)-P_nu(t,x)| <= L_f O_T(eta_m).

At eta=0 the result follows by taking eta down to zero. For fixed T and
fixed failure probabilities, this error tends to zero as m increases. Its
order is m^(-1/2) exp(O(sqrt(log m))); no uniform Lipschitz law derivative
or 1/m prediction-risk rate is claimed.

The triangle inequality gives the useful combined form

    sqrt(E_nu(P_nuhat(t)))
      <= sqrt(E_nu(P_nu(t))) + L_f O_T(eta_m), t<=T.

If a population oracle bound supplies E_nu(P_nu(t))<=B(t), replace its
square root by sqrt(B(t)); that substitution must retain the oracle's exact
scope. Uniform prediction boundedness also gives an additive risk error
at most 2(B_f+1)L_f O_T(eta_m) for the frozen class.

## Information and limit discipline

This event is uniform over t in [0,T], so any stopping rule taking values
in a fixed subinterval [T_min,T] is covered, including one chosen from the
observations. A rule justified only by unknown q or unknown population risk
is not supplied here. A deterministic episode endpoint computed from class
and reference constants is available when the learning proof supplies it.

The lemma compares two population-carrier paths. To transfer it to actual
finite GF, condition on every fixed sample, use the separately proved
finite-GF bridge for that fixed empirical law at each fixed epsilon>0, and
integrate the conditional probabilities (bounded by one). Next use the
empirical original-mixture selection as epsilon decreases. Only then let m
increase. Positive lower stopping times avoid the original initial layer.
No simultaneous width/epsilon/sample rate follows from this argument.
