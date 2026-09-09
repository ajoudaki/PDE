# Scalar-readout hidden projection: a finite-width theorem

Status: proved for a bounded smooth scalar feature map. The fixed-readout
hidden projection is a global orientation-preserving diffeomorphism at
every finite feature time. For zero initial readout it is also a global
orientation-preserving diffeomorphism at every finite forward physical
time. In both cases its log determinant is bounded below by the integrated
divergence of the complete state flow. The canonical arctan network at
width n=1 consequently has finite hidden Gaussian relative entropy with
the finite-time bounds stated below.

This is a scalar-readout theorem, not a width-uniform theorem. In the
canonical network the readout has dimension n, so the theorem applies
directly only when n=1. Nothing here proves a corresponding assertion for
n>=2, a global mean-field limit, or physical-time injectivity for an
arbitrary nonzero initial scalar readout. The latter does not follow by
substituting an initial-data-dependent feature clock into the feature-time
theorem.

## 1. Setup and completeness of the auxiliary gradient flow

Let h:R^d -> R be smooth and bounded, with |h|<=a<infinity. No global
bound on its derivatives is assumed. Consider the feature-time system

    x'=c grad h(x),                 c'=h(x),               (1)

with a fixed deterministic scalar initial readout c_0. Write

    b(x,c)=(c grad h(x),h(x)),
    A(x,c)=c D^2 h(x),
    Db=[ A  grad h ; (grad h)^T  0 ].                       (2)

The hidden initial-data map is F_(s,c_0)(x_0)=x_s(x_0,c_0), and its
d-by-d derivative is P_s=D_(x_0)F_(s,c_0).

Let psi_r be the flow of grad h. This auxiliary flow is complete in both
directions. Indeed, on any existing forward segment of length R,

    integral_0^R |grad h(psi_r x)|^2 dr
         =h(psi_R x)-h(x) <= 2a.

Cauchy--Schwarz therefore gives

    integral_0^R |grad h(psi_r x)| dr <= sqrt(2aR).          (3)

If a maximal forward interval had a finite endpoint, (3) would keep its
trajectory in a bounded set up to that endpoint. Smooth local ODE
existence on the closure of that bounded set extends the solution, a
contradiction. Apply the same argument to -grad h, using the decrease of
h, to obtain backward completeness. This proof does not assume bounded
grad h.

Along any local solution of (1), set tau_s=integral_0^s c_u du. Uniqueness
and the chain rule give

    x_s=psi_(tau_s)(x_0).

Moreover,

    |c_s|<=|c_0|+a|s|,
    |tau_s|<=|c_0||s|+a s^2/2.                             (4)

The representation and completeness of psi keep x_s in a compact
gradient-orbit segment on every bounded feature interval. Together with
the readout bound this proves complete existence of (1), and smooth
dependence on its initial data.

Every hidden trajectory stays in its initial gradient orbit. A critical
point of h is a singleton orbit and remains fixed in the hidden
coordinates, even if its readout changes. On a noncritical orbit choose

    gamma(r)=psi_r(x_*),             H(r)=h(gamma(r)).

Its parameter r runs through R, and

    H'(r)=|grad h(gamma(r))|^2>0.                           (5)

In particular gamma never repeats a point. Distinct gradient orbits are
disjoint by uniqueness of the auxiliary flow. No smooth quotient of the
set of orbits will be needed.

## 2. Feature-time order and exact determinant

On the orbit gamma, (1) is exactly

    r'=c,                    c'=H(r),
    r(0)=r_0,                c(0)=c_0.                    (6)

Fix c_0 and differentiate in r_0. If p=partial r_s/partial r_0, then

    p''=H'(r_s)p,
    p(0)=1,                  p'(0)=0.                    (7)

Since H'>=0, p remains positive: while p is positive its second
derivative is nonnegative, hence p'>=0 and p>=1 for s>=0; a first failure
of positivity is therefore impossible. Replacing s by -s proves the
same assertion backward. Consequently

    p(s)>=1 for every real s.                             (8)

For every r_0 the displacement satisfies the uniform bound (4).
Therefore r_0 -> r_s(r_0) is strictly increasing and tends to the
corresponding signed infinity as r_0 does. It is onto R. Thus F_(s,c_0)
is bijective on each noncritical gradient orbit, fixes every critical
point, and is globally bijective on R^d.

The local determinant is also everywhere positive. For a fixed x_0 put
g_0=grad h(x_0) and G_s=D_x psi_(tau_s)(x_0), where the latter derivative
holds the flow time tau_s fixed. The flow identity

    G_s g_0=grad h(x_s)

and differentiation of x_s=psi_(tau_s(x_0))(x_0) give

    P_s=G_s [I+g_0 (D_(x_0)tau_s)].                        (9)

The scalar factor in the determinant lemma is exactly the orbit
derivative p(s): perturbing x_0 to psi_epsilon(x_0) gives the final orbit
coordinate epsilon+tau_s(psi_epsilon(x_0)), whose derivative at zero is

    p(s)=1+(D_(x_0)tau_s)g_0.                             (10)

At a critical point this factor is 1. Applying the usual determinant
ODE to the complete auxiliary gradient flow and then the chain rule
along tau_s yields the exact identity

    det P_s
       =exp(integral_0^s c_u Delta h(x_u) du) p(s)
       =exp(integral_0^s Tr A(x_u,c_u) du) p(s).           (11)

This change of parameter uses an antiderivative along psi and does not
require tau_s to be monotone. Formula (11) is valid at critical points
with p=1 as well. Thus P_s is everywhere nonsingular. Global bijectivity
and the inverse function theorem make F_(s,c_0) a global
orientation-preserving smooth diffeomorphism.

In particular, for either sign of feature time,

    log det P_s >= integral_0^s Tr A(x_u,c_u) du
                = integral_0^s div b(x_u,c_u) du.          (12)

There is also a branchwise response identity. Let R_s=D_(x_0)c_s and
K_s=R_s P_s^(-1). Orbit differentiation gives

    P_s g_0=p(s) grad h(x_s),       R_s g_0=p'(s).

Consequently

    K_s grad h(x_s)=p'(s)/p(s)>=0,              s>=0.     (13)

At a critical point both sides are zero. This is the fixed-c_0 graph
slope. It is not the derivative of a conditional mean obtained by mixing
different initial readouts.

## 3. Forward physical time at zero initial readout

Now take c_0=0 and use the physical field

    dot x=alpha c grad h(x),       dot c=alpha h(x),
    f=c h(x),                     alpha=2(1-f).           (14)

Here f=c h is the scalar, n=1 normalization. Along any local forward
solution,

    dot f=2(1-f)(h^2+c^2|grad h|^2),       f(0)=0.

The residual equation implies 0<=f<1 on each finite existing interval,
and therefore 0<alpha<=2. The feature-clock length s(t)=integral_0^t
alpha_u du is at most 2t. Equations (4) and the complete feature flow
then prove forward physical completeness and the bounds

    |c_t|<=2at,
    |tau_t|<=2at^2,            tau_t=integral_0^t alpha_u c_u du.  (15)

The hidden state still has the representation x_t=psi_(tau_t)(x_0).
The following proof concerns the fixed physical time t directly; it does
not infer injectivity from the feature-time theorem at a varying clock.

On a noncritical gradient orbit, (14) becomes

    dot r=2(1-cH)c,            dot c=2(1-cH)H.

Set p=partial r_t/partial r_0 and q=partial c_t/partial r_0, keeping
c_0=0 fixed. Direct differentiation gives

    dot p=-2c^2 H' p+2(1-2f)q,
    dot q=2(1-2f)H' p-2H^2 q,
    p(0)=1,                   q(0)=0.                    (16)

Choose an antiderivative U'=H. The exact invariant
c^2-2U(r)=-2U(r_0) gives

    c q=H p-H(r_0).                                      (17)

First suppose H_0=H(r_0) is nonzero. The equations preserve the sign of
H_0 in H and in c for t>0: if H_0>0, c increases from zero and H is
nondecreasing; if H_0<0, c decreases from zero and H is nonincreasing.
Thus H_0/c>0 for t>0. Also f increases strictly from zero while remaining
less than one.

Until f reaches 1/2, the off-diagonal coefficients in (16) are
nonnegative. The integral forms with the diagonal integrating factors
give p>0 and q>=0 on that interval. If a first zero of p occurred later,
then f>1/2 there and (17) would imply

    dot p=-2(1-2f)H_0/c>0.

A first zero approached from positive values cannot have positive
derivative. Hence p remains strictly positive at every finite time.

If instead H_0=0, the state with c_0=0 is stationary. Linearizing (16)
at that state gives

    p(t)=cosh(2 sqrt(H'(r_0)) t)>0.                       (18)

There is a quantitative lower bound as well. Before f=1/2,

    dot p>=-2c^2 H' p>=-2(c^2 H'+H^2)p.

After f>=1/2, use (17) to rewrite the first equation of (16):

    dot p=[-2c^2 H'+2(1-2f)H/c]p
                         -2(1-2f)H_0/c.

The last term is nonnegative. Since 0<f<1,

    H/c=H^2/f>=H^2,
    2(1-2f)H/c=2H/c-4H^2>=-2H^2.

Thus throughout the trajectory

    log p(t)>=-2 integral_0^t (c_u^2 H'(r_u)+H(r_u)^2) du.  (19)

For H_0=0 this follows directly from (18), since H=c=0 along the
stationary state. Critical hidden points are singleton orbits and are
treated separately: the determinant factor in (10) is exactly p=1,
so positivity and (19) also hold there, including when h is nonzero.

The determinant argument (9)--(11), now with dot tau=alpha c, gives

    det P_t=exp(integral_0^t alpha_u c_u Delta h(x_u) du) p(t)>0. (20)

Every noncritical orbit map has positive derivative and displacement
bounded uniformly in its initial orbit coordinate by (15). It is
therefore increasing and onto R. Critical points are fixed. As before,
this proves that the physical hidden map with c_0=0 is a global
orientation-preserving smooth diffeomorphism.

The complete physical Jacobian has the exact rank-one correction

    D(alpha b)=alpha Db-2 b b^T,
    div(alpha b)=alpha c Delta h-2(c^2|grad h|^2+h^2).     (21)

Combining (19)--(21) proves

    log det P_t >= integral_0^t div(alpha b)(x_u,c_u) du.  (22)

No assertion for arbitrary nonzero c_0 in physical time is made here.
In particular, neither (16)--(19) nor the required sign H_0/c>0 has been
established for such initial data by this argument.

## 4. Canonical width-one bounds and entropy integrability

For the canonical arctan network at n=1, write x=(z,u,v), where the
hidden Gaussian coordinate factors sqrt(n) are all one, and

    h_1=arctan z,          z_2=u h_1,
    h_2=arctan z_2,        z_3=v h_2,
    h(x)=arctan z_3,       D_l=(1+z_l^2)^(-1).

Then

    grad h=(D_3 v D_2 u D_1, D_3 v D_2 h_1, D_3 h_2),

so the exact all-trained equations are (1). The scalar feature is
bounded by a=pi/2, but its derivatives need not be globally bounded in
the hidden parameters; the general theorem deliberately does not make
that assumption.

For deterministic c_0 put R_0=|c_0| and M=max(|u_0|,|v_0|). On |s|<=S,
the actual triangular primal estimates give

    |c_s|<=R_0+aS,
    |v_s|<=M+aR_0S+a^2S^2/2,
    |u_s|<=M+a integral_0^S (R_0+ar)
                              (M+aR_0r+a^2r^2/2) dr.    (23)

They follow respectively from |c'|<=a, |v'|<=a|c|, and
|u'|<=a|c||v|, and hold in either direction of feature time. All bounds
are polynomial in S,M,R_0.

For completeness, derivative bounds require no control of z_0. Using
|phi'|<=1 and |phi''|<=2 for phi=arctan, define

    G_2=|u|+a,
    G_3=|v|G_2+a,
    L_2=2|u|+2,
    L_3=2|v|G_2^2+|v|L_2+2G_2.

The chain rule gives

    |grad z_2|<=G_2,        |grad z_3|<=G_3,
    ||D^2 z_2||_op<=L_2,   ||D^2 z_3||_op<=L_3,
    |grad h|<=G_3,         ||D^2 h||_op<=2G_3^2+L_3.    (24)

For example the mixed derivative contribution to D^2 z_3 is
D_2[e_v(grad z_2)^T+(grad z_2)e_v^T], accounting for the final 2G_2.
Thus (23)--(24) and (2) imply

    sup_(|s|<=S) ||Db(x_s,c_s)||_op <= P_S(M,R_0),       (25)

for a fixed polynomial P_S with nonnegative coefficients.

Let Q(x)=|x|^2/2. The elementary inequality |w phi'(w)|<=1/2 gives the
actual hidden Gaussian-energy derivative bound

    |DQ(x)[c grad h(x)]|
        <= (|c|/2)(|uv|+|v|+1).                          (26)

Indeed the three terms are z c D_3 v D_2 u D_1,
u c D_3 v D_2 h_1, and v c D_3 h_2; in the second and third use
u h_1=z_2 and v h_2=z_3. Consequently

    |Q(x_s)-Q(x_0)|<=P_S(M,R_0).                        (27)

The determinant is integrable under Gaussian hidden initialization.
Its lower bound (12) and (25) give

    log det P_s>=-3|s|P_S(M,R_0).

For the upper bound, the full four-dimensional flow derivative has
operator norm at most exp(|s|P_S(M,R_0)) by its variational equation.
The hidden block P_s has no larger operator norm. Since it is 3-by-3,

    log det P_s<=3|s|P_S(M,R_0).

These statements also hold backward in feature time by integrating the
variational equation over the interval between s and zero. After
absorbing constants into the polynomial,

    |log det P_s|<=P_S(M,R_0).                            (28)

For physical time with c_0=0, the feature length is at most 2T. Use
(23)--(26) on that feature interval, alpha<=2, and (21). This gives
polynomial bounds in M on the complete physical Jacobian norm and on
the change of Q. The determinant lower bound (22) and the upper bound
from the full physical flow derivative similarly imply

    |Q(x_t)-Q(x_0)|+|log det P_t|<=P_T(M),    0<=t<=T.   (29)

One can use |div(alpha b)|<=4||D(alpha b)||_op in the lower bound;
the hidden determinant upper bound uses its dimension 3. Thus (29)
does not presume logarithmic integrability near a possible critical
projection: nonsingularity and an explicit lower bound have already
been proved.

Now let x_0~gamma_3=N(0,I_3). The variable M has moments of every order.
For each deterministic c_0, (27)--(28) are integrable. Since F_(s,c_0)
is a global diffeomorphism, its pushed-forward hidden density rho obeys
the exact change-of-variables identity

    log[rho(x_s)/gamma_3(x_s)]
       =Q(x_s)-Q(x_0)-log det P_s.                       (30)

The right side is absolutely integrable, so its expectation is a finite
relative entropy. Equations (12), (25), and (27) yield

    0<=D(law(x_s | c_0)||gamma_3)
      <= E[Q(x_s)-Q(x_0)-integral_0^s div b(x_u,c_u)du]
      <= C_S(1+|c_0|)^k,                 |s|<=S,         (31)

for some fixed finite k and C_S. Increasing k or C_S absorbs a general
polynomial in |c_0|. Analogously, (22) and (29) give for c_0=0

    D(law(x_t)||gamma_3)<=C_T,              0<=t<=T       (32)

in physical time. These are finite-width constants, not estimates
uniform in a varying network width.

If the initial scalar readout is independent of x_0 and has a law nu
with the required finite moment, convexity of relative entropy gives

    D(integral law(x_s | c_0=c) nu(dc) || gamma_3)
       <= integral D(law(x_s | c_0=c)||gamma_3) nu(dc)
       <= C_S integral (1+|c|)^k nu(dc)<infinity.         (33)

This includes every fixed-variance Gaussian scalar readout in feature
time. The canonical width-one initialization has c_0~N(0,1), since the
canonical coordinate variance n^(-2) equals one at n=1. The physical
result (32) concerns the exactly zero-readout initialization only;
(33) does not transfer that physical result to a nonzero Gaussian
readout.

## 5. Scope of the conclusion

Established: arbitrary fixed scalar-readout feature-time projection is
a global diffeomorphism for bounded smooth h; zero-readout forward
physical projection is also a global diffeomorphism. Both have the
specified complete-divergence determinant lower bound. The actual
canonical n=1 Gaussian hidden law has the finite entropy bounds above,
and its feature-time Gaussian-readout mixture is covered by convexity.

The argument does not select a deterministic point and call it a
Gaussian draw. The feature theorem holds for every initial hidden point
and every fixed scalar c_0; the physical theorem holds for every initial
hidden point with c_0=0. Their probabilistic conclusions follow from
the stated Gaussian moment estimates and, where applicable, mixing.

Still unresolved by this theorem: canonical n>=2 projection angles or
folding, width-uniform hidden entropy, physical-time projection with
arbitrary nonzero c_0, and the population mean-field/gradient-flow
limit. The branchwise sign (13) is not a sign for a Gaussian-mixture
conditional-mean derivative.

## 6. Why a commuting-gradient extension is not automatic

For n>=2, write h_i(x)=h^(3)_i for the i-th output activation, in the
actual hidden Gaussian coordinates

    x=(z^(1),sqrt(n)W^(2),sqrt(n)W^(3)).

The hidden feature-time velocity is sum_i c_i grad h_i. The scalar
proof above works because this is motion along a single complete
gradient orbit. One cannot replace that fact by an assertion that the
several output-gradient fields commute: in the canonical network they
do not, almost surely at Gaussian initialization.

Here commuting means the exact vector identity

    D^2 h_j grad h_i-D^2 h_i grad h_j=0.                  (34)

To check its failure, take i=1,j=2, choose h^(1) nonzero, put W^(2)=0,
and choose W^(3) with row i equal to v e_i^T, v>0, and row j zero.
Other rows can also be zero. This is a deterministic witness used only
to show that an analytic function is nontrivial, not asserted to be a
Gaussian draw.

At this point h^(2)=0, all z^(3) are zero, phi'(0)=1, and phi''(0)=0.
Let x_lower=(z^(1),sqrt(n)W^(2)). In the hidden coordinate
sqrt(n)W^(3)_(j,i), the left side of (34) is exactly

    (v/sqrt(n)) |grad_(x_lower) h^(2)_i|^2
       = v ||h^(1)||_2^2 / n^(3/2) > 0.                 (35)

Indeed grad h_j in that coordinate equals
phi'(z^(3)_j)h^(2)_i/sqrt(n). Its derivative along grad h_i is the
first expression in (35): the derivative of phi' vanishes at zero,
and the lower part of grad h_i equals v grad h^(2)_i.
The second term in (34) has zero component there, since h_i is
independent of every entry of row j of W^(3). Finally, at W^(2)=0
the only nonzero lower derivatives of h^(2)_i are
h^(1)_q/sqrt(n) in row i of sqrt(n)W^(2), giving the equality in (35).

That scalar component of (34) is real analytic in the hidden initial
coordinates and, by (35), is not identically zero. Its zero set has
Lebesgue measure zero: at each zero of a nontrivial analytic function
some derivative of minimal positive order is nonzero, so that point
lies on a regular zero hypersurface of a derivative of one lower
order; the countably many derivative choices give a null cover.
The full hidden Gaussian law has a density. Therefore (34) fails
almost surely for this fixed output pair, at each fixed n>=2.

This proves only the absence of that proposed commuting-gradient
simplification. It gives no width-uniform lower bound on commutator
size, no focusing or folding result, and no negative theorem about
the population limit. The full n>=2 quantitative projection problem
remains open.
