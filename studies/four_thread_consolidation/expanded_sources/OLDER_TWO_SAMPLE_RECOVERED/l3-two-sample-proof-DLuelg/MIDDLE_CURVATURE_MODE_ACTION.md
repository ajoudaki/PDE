# The shifted-softplus identity also controls actual middle curvature modes

Root candidate, 2026-09-06. This note proves an integrated estimate on
an EXISTING population feature-gradient path with explicitly assumed
energy and sample symmetry. It does not prove existence, cut removal,
a bound on the full historical response, or the global two-sample theorem.
No experiments or external specialized theorem are used.

Fix e=1/10 and phi(z)=1+e log(1+exp z), at all layers. There are separate
probability spaces Omega_1, Omega_2, Omega_3. Operators W^(2), W^(3)
and their adjoints are bounded between the corresponding L2 spaces,
with finite initial operator norms. Their increments are absolutely
continuous Hilbert--Schmidt curves with derivatives (1). All fields
have finite indicated L2 norms. First and readout fields use their
canonical RMS metrics; the first-pair metric is E[v^T C^(-1)v] for
C=[[1,rho],[rho,1]], |rho|<1, and one field (Z,-Z) with metric E v^2
when rho=-1. Labels are (1,-1).

For each sample a=1,2 define

    H^(ell)_a=phi(Z^(ell)_a),
    Z^(2)_a=W^(2)H^(1)_a,    Z^(3)_a=W^(3)H^(2)_a,
    delta^(3)_a=W^(4)phi'(Z^(3)_a),
    q^(2)_a=(W^(3))*delta^(3)_a,
    delta^(2)_a=phi'(Z^(2)_a)q^(2)_a,
    q^(1)_a=(W^(2))*delta^(2)_a,
    delta^(1)_a=phi'(Z^(1)_a)q^(1)_a,
    g=E_3[W^(4)(H^(3)_1-H^(3)_2)]/2.

The hypotheses are an existing regular path on [0,S], initially zero
readout, g(0)=0, g(s)<=1, and the exact uncut feature equations

    (W^(ell))'=(delta^(ell)_1 tensor H^(ell-1)_1
                   -delta^(ell)_2 tensor H^(ell-1)_2)/2, ell=2,3,
    (Z^(1)_b)'=(C_b1 delta^(1)_1-C_b2 delta^(1)_2)/2,
    (W^(4))'=(H^(3)_1-H^(3)_2)/2.                        (1)

Here (u tensor v)h=u E[vh]. Finite transpose actions would have uv^T/n;
no finite-width limit or finite residual-mode identity is presumed.
The raw-gradient chain rule and energy identity are explicit hypotheses:

    g'=||theta'||_raw^2,
    integral_0^S ||theta'||_raw^2 ds=g(S)<=1.             (2)

Also suppose the two feature second moments agree in populations 1 and
2 at every time. No symmetry of an unconstructed path is inferred.
Write U^(ell)=(H^(ell)_1+H^(ell)_2)/2,
V^(ell)=(H^(ell)_1-H^(ell)_2)/2, and
kappa_ell=E_ell[(V^(ell))^2]. Then E_ell[U^(ell)V^(ell)]=0 for ell=1,2.
For any other sample pair X_a, X_+=(X_1+X_2)/2 and
X_-=(X_1-X_2)/2 are fields on that pair's own population.

## 1. A scalar identity that avoids a product with the feature difference

The derivative p=phi' satisfies 0<p<e and

    phi''=p-p^2/e.

For any two real preactivations z_1,z_2 and any two real q_1,q_2, set
delta_a=phi'(z_a)q_a and m_a=phi''(z_a)q_a. Algebra gives, for BOTH
choices of half-sum or half-difference,

    m_+ = [1-(phi'(z_1)+phi'(z_2))/e] delta_+
                                  +[phi'(z_1)phi'(z_2)/e] q_+,
    m_- = [1-(phi'(z_1)+phi'(z_2))/e] delta_-
                                  +[phi'(z_1)phi'(z_2)/e] q_-. (3)

To verify it without dividing by a small gate, write p_a=phi'(z_a),
A=1-(p_1+p_2)/e and B=p_1p_2/e. For each a separately,

    A p_a+B=p_a-p_a^2/e,

so m_a=A delta_a+B q_a; the same A and B apply to both samples.
Taking their half-sum and half-difference proves (3).
Moreover |A|<=1 and 0<=B<=e. Therefore

    |m_+|<=|delta_+|+e|q_+|,
    |m_-|<=|delta_-|+e|q_-|.                            (4)

There is NO conversion between average and difference modes in these
inequalities. Although A and B may be correlated with all the fields,
their deterministic pointwise bounds are enough. In particular there
is no unproved factorization of a product of random variables.

## 2. Apply the identity to the actual middle query

Define the actual middle curvature fields

    M^(2)_+=(phi''(Z^(2)_1)q^(2)_1
                       +phi''(Z^(2)_2)q^(2)_2)/2,
    M^(2)_-=(phi''(Z^(2)_1)q^(2)_1
                       -phi''(Z^(2)_2)q^(2)_2)/2.

The same W^(3) is used on both samples. Linearity of its adjoint gives
the EXACT identity q^(2)_+=(W^(3))*delta^(3)_+ and likewise with minus.
Consequently (4) implies

    ||M^(2)_-||_2^2
       <=2||delta^(2)_-||_2^2
                      +2e^2||W^(3)||_op^2||delta^(3)_-||_2^2,
    ||M^(2)_+||_2^2
       <=2||delta^(2)_+||_2^2
                      +2e^2||W^(3)||_op^2||delta^(3)_+||_2^2. (5)

These are bounds on the actual trained query and its actual curvature,
not just on an independent Gaussian component of that query.

Let M_ell=||W^(ell)(0)||_op+sqrt(S), ell=2,3. The energy identity gives

    ||W^(ell)(s)-W^(ell)(0)||_op
       <=integral_0^s ||(W^(ell))'||_HS
       <=sqrt(S) (integral_0^S ||theta'||_raw^2)^(1/2)
       <=sqrt(S),

so ||W^(ell)(s)||_op<=M_ell for every s<=S.
The modal matrix-gradient decomposition and its exact squared norm are

    (W^(ell))'=delta^(ell)_- tensor U^(ell-1)
                      +delta^(ell)_+ tensor V^(ell-1),
    ||(W^(ell))'||_HS^2
      =||U^(ell-1)||_2^2||delta^(ell)_-||_2^2
                      +kappa_(ell-1)||delta^(ell)_+||_2^2. (6)

The cross term vanishes by the stipulated feature second-moment
symmetry. Since phi>=1, ||U^(ell-1)||_2>=1. Adding the two matrix
blocks in (6) and using (2) gives

    integral_0^S [ ||delta^(2)_-||_2^2+||delta^(3)_-||_2^2
             +kappa_1||delta^(2)_+||_2^2
             +kappa_2||delta^(3)_+||_2^2 ] ds <=g(S).    (7)

Forward Lipschitzness, on the separate first and second populations,
gives ||V^(2)||_2<=e||W^(2)||_op||V^(1)||_2, hence
kappa_2<=e^2 M_2^2 kappa_1. Multiplying the second inequality of (5)
by kappa_2 and using (7) now yields

    integral_0^S ||M^(2)_-||_2^2 ds
          <=2(1+e^2 M_3^2)g(S),
    integral_0^S kappa_2||M^(2)_+||_2^2 ds
          <=2e^2(M_2^2+M_3^2)g(S).                     (8)

No lower bound on any contrast Gram, and no division by kappa_1 or
kappa_2, was used. Thus (8) also allows a zero contrast at an individual
time and has no hidden inverse-angle constant. Its constants depend
only on the displayed initial operator norms and S.

For comparison, the same scalar gate law gives
|phi''(x)-phi''(y)|<=|phi'(x)-phi'(y)| and phi''<=phi'.
At the top the common readout therefore gives

    |W^(4)(phi''(Z^(3)_1)-phi''(Z^(3)_2))/2|
                       <=|delta^(3)_-|,
    |W^(4)(phi''(Z^(3)_1)+phi''(Z^(3)_2))/2|
                       <=|delta^(3)_+|.

Their squared integral, with weight 1 for the difference and kappa_2
for the average, is bounded by g(S) using (6). Thus both the top and
middle ACTUAL curvature modes now have the indicated action bounds.

## 3. Scope of the improvement

Expanding phi''=(1-phi'/e)phi' separately in half-sum/difference
coordinates initially produces a mixed term involving a gate difference
times delta_+. Identity (3) rewrites the whole expression using only
the SAME-MODE delta and reverse query. The latter's L2 norm is bounded
by the actual next-layer delta via the
bounded trained adjoint. This is the new middle estimate; it does not
assume independence of populations linked by the operator.

The bounds are only second moments integrated in time. They do not
control M^(2)_- times a correlated source sensitivity in L2, or an
exponential moment of its time integral. They do not bound multiplication
by M^(2)_- on all L2, prove a signed variational inequality, or bound the
full retarded response. In particular (8) is not the missing Osgood tail
estimate and does not construct an uncut global path.

Equations (1)--(2) and sample symmetry remain hypotheses. Internal
back-query cuts generally do not preserve them. The original raw GD,
Gaussian initialization, finite-width identification, autonomous restart,
all observables and nonlazy/nonlinear finite-time requirements are not
changed or discharged by this lemma.
