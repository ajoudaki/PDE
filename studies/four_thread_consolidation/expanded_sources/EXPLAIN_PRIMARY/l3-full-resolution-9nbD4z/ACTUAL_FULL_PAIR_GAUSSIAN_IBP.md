# Gaussian integration by parts of the complete off-diagonal primitive pair

Status: new exact finite-width identities with localization. The full
exchange of the two middle indices does not cancel the mixed second
flow derivatives created by top-disorder integration by parts. Integrating
the lower Gaussian Gram factor instead retains a higher response
derivative. No uniform response estimate or continuation theorem is proved.

This note applies to the uncut canonical arctangent feature-time flow on a
fixed finite horizon. It preserves all learned matrix increments. The
causal memory term from ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md is unchanged;
only its complete instantaneous pair is integrated here. The conclusions
below do not assert that an additional identity involving that memory
could never help.

## 1. Actual response and localization

Use ordinary matrix entries and transposes, normalized vector inner
products, and the actual quantities

    z=z2, D_i=phi'(z_i), beta_i=phi''(z_i)/phi'(z_i),
    d=delta3, g=q2=W3* d,
    K=W2 diag(D1^2) W2*,
    Sigma_ij=n E_xi[c_i c_j].

Here c is precisely the full-backprop primitive response in
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md. Fix its probe column ell once and
for all: the initial top matrix is varied by
nu=xi e_ell*/sqrt(n), with xi an independent standard Gaussian vector.
In particular neither the initial disorder nor any actual coefficient is
independent of Sigma. Define the primal primitive

    A_i(t)=integral_0^t delta2_i(s) ds.

The exact definition of c is

    c_i=D_i^{-1} partial_nu A_i.                         (1)

All initial-data derivatives below hold the independent probe xi fixed.
Let E denote expectation over the complete original Gaussian
initialization, and keep E_xi explicit for probe expectation.

For rigor, let chi be a smooth, compactly supported function of all
original initialization coordinates. There is no conditioning on an
operator-norm event. Finite-dimensional smooth dependence of the uncut
flow on its initial data, on the given finite horizon, bounds every
derivative needed below on the support of chi. Responses are linear in
xi, so probe integration of each displayed quadratic expression is
finite on that support.

If X is any initial matrix entry of variance 1/n, then for a compactly
supported smooth function f,

    E[X f]=(1/n) E[partial_X f].                       (2)

Indeed integration against its one-dimensional Gaussian density gives
rho'(x)=-n x rho(x); ordinary integration by parts has zero boundary
term because f has compact support. Fubini applies on the compact
support. This proves every use below. The derivatives of chi are
retained. No unproved integrability assertion is used to set chi=1 or
remove a sequence of cutoffs.

The merely C1 clipped family is not covered by these higher response
derivatives: differentiating c with respect to disorder requires more
than C1 smooth dependence of the vector field. Smooth clipping could
be treated separately, but no estimate uniform in its higher
derivatives is supplied here.

## 2. Top-disorder integration of both orientations

Set

    Gamma_ij=z_i Sigma_ii-z_j Sigma_ij,
    F_ij=D_i D_j Gamma_ij.

The complete instantaneous term is exactly

    S=(1/n) sum_{i!=j} K_ij [g_j F_ij+g_i F_ji].        (3)

Write V=W3(0), J=W3-V and k=J* d, so that
g_j=sum_a V_aj d_a+k_j. Define the retained learned-query term

    S^J=(1/n) sum_{i!=j} K_ij [k_j F_ij+k_i F_ji].

There is no assertion here that S^J is harmless at the primitive-energy
scale. Applying (2) separately to the two terms of (3) gives

    E[chi S]=E[chi S^J]
      +(1/n^2) sum_{i!=j,a} E[
          partial_{V_aj}(chi d_a K_ij F_ij)
         +partial_{V_ai}(chi d_a K_ij F_ji)].           (4)

All factors inside each derivative are actual factors. The second sum
in (4), under exchange of the dummy indices i and j, equals the first,
because K_ji=K_ij. This is a pointwise index exchange, not a permutation
invariance or an independence assumption. The fixed probe column ell
causes no problem. Consequently

    E[chi S]=E[chi S^J]
      +(2/n^2) sum_{i!=j,a}
         E[partial_{V_aj}(chi d_a K_ij D_i D_j Gamma_ij)]. (5)

Equation (4) keeps both orientations visible before any absolute bound;
equation (5) states exactly how they combine.

For w=V_aj, the derivative of the response covariance is

    partial_w Sigma_ii=2n E_xi[c_i partial_w c_i],
    partial_w Sigma_ij=n E_xi[
          (partial_w c_i)c_j+c_i partial_w c_j].        (6)

Hence (5) has the exact decomposition

    E[chi S]=E[chi S^J]+B_chi+R_chi,                   (7)

where

    B_chi=(2/n^2) sum_{i!=j,a} E[
      partial_w(chi d_a K_ij D_i D_j) Gamma_ij
      +chi d_a K_ij D_i D_j
         ((partial_w z_i)Sigma_ii-(partial_w z_j)Sigma_ij)],

and the complete covariance-derivative contribution is

    R_chi=(2/n) sum_{i!=j,a} E[chi d_a K_ij D_i D_j
      E_xi[(2z_i c_i-z_j c_j)partial_{V_aj}c_i
                            -z_j c_i partial_{V_aj}c_j]]. (8)

No term in B_chi was declared bounded. In particular it includes all
cutoff derivatives and all actual learned-mobility derivatives.

To display the mixed second *flow* derivatives specifically, (1) gives

    partial_w c_i=D_i^{-1} partial_w partial_nu A_i
                        -beta_i(partial_w z_i)c_i.     (9)

Substitution into (8) leaves the contraction

    H_chi=(2/n) sum_{i!=j,a} E[chi d_a K_ij
      E_xi[
        D_j(2z_i c_i-z_j c_j) partial_{V_aj}partial_nu A_i
          -D_i z_j c_i partial_{V_aj}partial_nu A_j]],  (10)

plus the explicitly determined first-response products obtained from
the second term in (9). Formula (10) is the stopping obstruction for
this top-disorder pass.

Before combining orientations, the mixed-derivative expression is the
sum of (8)'s summand and its i,j exchange, with coefficient 1/n rather
than 2/n. These two indexed sums coincide and add. Thus symmetrization
does not remove (8) or (10). The coefficients of the indicated mixed
derivatives are not identically zero algebraically. Equality of mixed
partial derivatives only exchanges w and nu for the same output A_i;
it does not exchange the output i with j or V_aj with V_ai. It therefore
does not cancel (10). This is a statement about the exact IBP identity,
not a construction of an arbitrary covariance in place of the actual
network response, and not a claim that no further dynamical estimate
of (10) exists.

## 3. Learned lower-matrix increments are present in (7)

Write G=W2(0), L=W2-G and B=diag(D1^2). Exactly,

    K=G B G*+G B L*+L B G*+L B L*.

For w any top initial coordinate, G is fixed, but L and B are not:

    partial_w K=(partial_w L)B W2*
                    +W2(partial_w B)W2*
                    +W2 B(partial_w L)*.              (11)

In particular the learned terms cannot be omitted inside B_chi.
Their actual derivatives have the identity

    L_ia(t)=(1/n) integral_0^t delta2_i(s)H1_a(s) ds,
    partial_w L_ia(t)=(1/n) integral_0^t [
        (partial_w delta2_i)H1_a
                +delta2_i partial_w H1_a](s) ds.      (12)

These identities follow directly from the actual training equation.
They have not been replaced by a frozen Gram matrix or by a separately
sampled matrix. Terms (11)--(12) involve first initial-data responses;
they do not algebraically supply negative copies of the mixed second
derivatives in (10).

## 4. Integrating the lower Gaussian Gram factor retains higher derivatives

A second exact calculation checks the alternative of using Gaussian
off-diagonal centering of the lower mobility. Keep the entire g and
all its dependence on the initialization in this calculation. Set

    P_ij=z_i g_j Sigma_ii+z_j g_i Sigma_jj
                         -(z_i g_i+z_j g_j)Sigma_ij,
    Psi_ija=chi D1_a^2 D_i D_j P_ij.

Then P_ji=P_ij, and (3) is equivalently
S=n^{-1}sum_{i!=j,a} W2_ia W2_ja D1_a^2 D_i D_j P_ij.
Since G_ia and G_ja are distinct independent entries for i!=j,
twice applying (2) and expanding W2=G+L gives exactly

    E[chi S]=(1/n) sum_{i!=j,a} E[
        L_ia L_ja Psi_ija
       +(1/n)partial_{G_ia}(L_ja Psi_ija)
       +(1/n)partial_{G_ja}(L_ia Psi_ija)
       +(1/n^2)partial_{G_ia}partial_{G_ja}Psi_ija].     (13)

There is no Gaussian diagonal contact term: i=j has already canceled
identically in the original full pair. Every learned-matrix correction
and every derivative of the cutoff is retained in (13).

The last term in (13) contains a particularly explicit sector. Put

    R_i=2z_i g_j c_i-(z_i g_i+z_j g_j)c_j,
    R_j=2z_j g_i c_j-(z_i g_i+z_j g_j)c_i.

The terms where both derivatives land on the same response c are

    T_chi=(1/n^2) sum_{i!=j,a} E[chi D1_a^2 D_i D_j
       E_xi[R_i partial_{G_ia}partial_{G_ja}c_i
                       +R_j partial_{G_ia}partial_{G_ja}c_j]]. (14)

To check (14), use
P_ij=n E_xi[(g_j c_i-g_i c_j)(z_i c_i-z_j c_j)]
and differentiate this quadratic expression twice. The partial
derivatives with respect to c_i and c_j are respectively n R_i and
n R_j inside E_xi. All remaining terms are already present in (13);
they include products of first response derivatives and derivatives
of primal coefficients.

Under exchange of i and j, the two summands in (14) exchange and the
mixed differential operator is unchanged. This sector is also
exchange-even. Lower-matrix centering therefore does not cancel these
second derivatives of c, which contain third derivatives of the primal
flow through (1). The first-derivative terms in (13), generated by the
learned increments, do not contain derivatives of c of this order.

## 5. An actual small-time jet makes the mixed contraction nonzero

There is an analytic check using actual trajectories, not an arbitrarily
assigned covariance. Take n=2 and zero initial readout. Choose r,z>0,
put b=arctan(r), and initialize

    z1=(r,r),
    G=W2(0)=[[z/b,0],[z/b,0]],
    V=W3(0)=[[v,0],[0,0]],       v>0.

Then z2(0)=(z,z). Write

    h=arctan(z), D=(1+z^2)^{-1}, x=vh,
    kappa(x)=arctan(x)/(1+x^2),
    k0=K_12(0)=(z/b)^2(1+r^2)^{-2}>0.

At zero readout the exact equations give, as t decreases to zero,

    W2(t)=G+O(t^2), W3(t)=V+O(t^2), z2(t)=z2(0)+O(t^2),
    d(t)=t kappa(V(h,h)*)+O(t^2),
    q2(t)=t Q(V)+O(t^2),
    Q(V)=V* kappa(V(h,h)*),
    A(t)=(t^2/2)D Q(V)+O(t^3).

Here kappa acts componentwise, and the scalar D is the common initial
middle gate. These are finite-dimensional Taylor identities with
remainders locally bounded also after up to two V derivatives: apply
Taylor's integral remainder to each such derivative of the smooth
uncut flow. They may therefore be differentiated with respect to V as
used below. No width-uniform Taylor remainder is claimed or needed.

Use probe column ell=1. By (1),

    c(t)=(t^2/2)U+O(t^3),       U=partial_nu Q(V).

At the specified V the needed derivatives are exactly

    U_1=[kappa(x)+x kappa'(x)]xi_1/sqrt(2),   U_2=0,
    partial_{V_12}U_1=h[kappa'(x)+x kappa''(x)]xi_1/sqrt(2),
    partial_{V_12}U_2=h kappa'(x)xi_1/sqrt(2),
    partial_{V_11}U_2=0.

For example Q_1=V_11 kappa(h(V_11+V_12)) plus the second-row
contribution, so differentiating first in V_11 and then in V_12
gives the displayed derivative of U_1. In d's leading term only top
row a=1 is nonzero. Thus in (8)'s unaveraged-in-initialization
expression, only i=1,j=2,a=1 contributes at order t^5. Since
E_xi xi_1^2=1, direct substitution gives

    R(t)=t^5/8 k0 D^2 z h kappa(x)
       [kappa(x)+x kappa'(x)]
       [kappa'(x)+2x kappa''(x)]+O(t^6).               (15)

The notation R(t) here means the pointwise integrand whose localized
initialization expectation is R_chi; chi is not included in R(t).
The same leading coefficient holds for the integrand of H_chi in
(10): the difference in (9) contains partial_w z2=O(t^2), which
makes its contribution to (8) O(t^7).

As x decreases to zero through positive values,
kappa(x)=x+O(x^3), kappa(x)+x kappa'(x)=2x+O(x^3), and
kappa'(x)+2x kappa''(x)=1+O(x^2). The coefficient in (15) is
therefore positive for sufficiently small v>0. At such an initialization
and sufficiently small positive t, the actual mixed-Hessian integrand
is nonzero. Smooth dependence gives an open neighborhood where it
remains positive. The prescribed finite-width Gaussian initialization,
including its tiny Gaussian readout, has positive density in that
neighborhood. Choosing a nonnegative nonzero smooth chi supported
there proves H_chi>0 for that choice of localization.

This excludes an identity making the actual mixed contraction vanish
on every initialization or under every valid localization. It does not
give its sign after removing localization, contradict a width-uniform
bound, or supply a counterexample to the canonical population theorem.
The learned W2 and W3 increments are present in the exact equations;
their O(t^2) onset is why they do not change this leading coefficient.

## Scoped conclusion

The complete exchanged pair has now been subjected to Gaussian
integration by parts without dropping covariance dependence or learned
W2 increments. Top-disorder integration leaves the actual mixed
second-flow-derivative contraction (10); lower-Gram integration leaves
the higher contraction (14). Polarization cancels the original
instantaneous diagonal terms, but its two orientations add in these
remaining sectors. The cutoff terms are explicit, and their removal
requires its own integrability argument. No bound on (10), its
companion terms in (7), the learned-query term, or the retained causal
memory sufficient for uniform response closure is proved here.
