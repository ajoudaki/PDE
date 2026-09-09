# Nonlinearity and nonfreezing for the special-angle L=2 candidate

Root draft, 2026-09-06. UNREVIEWED. This note proves an implication
under the explicit global representation premises below. It does not
construct those representations or a canonical population flow. Those
are separate obligations of the canonical bridge. In particular this
is not a proof for intermediate input angles or for three hidden layers.

All scalar activations in this note are phi(z)=arctan(z), with
phi'(z)=1/(1+z^2)>0 and |phi(z)|<B=pi/2. Set F(z)=z+z^3/3.
Expectations and ordinary L2 norms refer to the indicated neuron
population, never to an identification between the two populations.

## 1. Exact premises

There are two probability spaces, an actual bounded operator W^(2)(t)
from the first L2 space to the second, and its actual adjoint. The
operator has differentiable Hilbert--Schmidt increments. For samples
a=1,2 let

    H^(1)_a=phi(Z^(1)_a), Z^(2)_a=W^(2) H^(1)_a,
    H^(2)_a=phi(Z^(2)_a),
    f_a=E_2[W^(3) H^(2)_a], r_a=f_a-y_a, y=(1,-1), L=sum_a r_a^2,
    delta^(2)_a=W^(3) phi'(Z^(2)_a),
    Q^(1)_a=(W^(2))^* delta^(2)_a,
    delta^(1)_a=phi'(Z^(1)_a) Q^(1)_a.

The physical flow is

    dot Z^(1)_a=-2 sum_b C_ab r_b delta^(1)_b,
    dot W^(2)=-2 sum_b r_b delta^(2)_b tensor H^(1)_b,
    dot W^(3)=-2 sum_b r_b H^(2)_b.                    (1)

Here (v tensor u)x=v E_1[ux]. The input Gram C is either I, or
[[1,-1],[-1,1]] with the exact relations Z^(1)_2=-Z^(1)_1.
In the latter case all forward fields are opposite, both delta fields
are equal between samples, and f_2=-f_1, by oddness of phi and evenness
of phi'. The first-layer physical metric is the sum of the two field
norms when C=I, and one field norm in the antiparallel reduction.

Assume this flow exists on every finite physical interval, with the
fields and original velocities continuous in L2, W^(2) continuous in
operator norm, bounded W^(3) in L-infinity on each interval, and the
usual raw loss identity. Assume its law has the canonical exchange
symmetry: swap the two sample fields and negate W^(3) and both reverse
fields. Thus f_1=-f_2 and both samples' same-layer velocity norms agree.
For C=I this is a law symmetry, not an identity between finite neurons.

At initialization Z^(1)=G is a centered Gaussian pair of covariance C,
W^(3)=0. Put m=E[phi(N(0,1))^2]>0. The initial second pair X=Z^(2)(0)
is Gaussian of covariance m I for C=I, and is (X_1,-X_1) with
X_1~N(0,m) for the antiparallel case. The initial operator and its
transpose have the finite independent N(0,1/n) initialization law,
in the joint empirical sense detailed in Section 4 below.

Finally assume, for every finite T, the following representations for
all t<=T, with a finite deterministic bound M_T on the displayed
remainder fields (enlarging M_T between displays is harmless):

    Q^(1)_a(t)=zeta_a(t)+R_a(t),       |R_a(t)|<=M_T,
    Z^(2)_a(t)=xi_a(t)+S_a(t),        |S_a(t)|<=M_T,    (2)

where zeta and xi are centered Gaussian processes with their full
time/sample covariances, zeta independent of G, and

    E zeta_a(t)^2=||delta^(2)_a(t)||_2^2,
    E xi_a(t)^2=||H^(1)_a(t)||_2^2.                   (3)

No independence of the remainders from the Gaussian sources is assumed.
Time integrals of zeta against bounded deterministic controls are
Gaussian L2 variables; its L2 time integral exists. These properties
follow, for example, from finite total response rows in the usual
causal representation with bounded H^(1), delta^(2). Their global
validity is a premise here, not an inference from primal bounds alone.

The conclusions proved below are: both activations are distributionally
nonaffine at every finite time; every hidden layer, the hidden matrix,
and readout have strictly positive speed at every t>0; the full raw
kernel is nonconstant already near initialization. The zero hidden
speeds at t=0 are retained, not hidden by a time reparameterization.

## 2. First-field tails and a positive feature Gram

For C=I the scalar chain rule in (1) gives exactly

    F(Z^(1)_a(t))=F(G_a)-2 integral_0^t r_a(u)Q^(1)_a(u) du.

For antiparallel inputs the reduced coefficient is -4r_1 rather than
-2r_a. In either case (2) implies

    F(Z^(1)_a(t))=F(G_a)+I_a(t)+E_a(t),
    |E_a(t)|<=M'_T,                                   (4)

where I(t) is a finite-variance Gaussian pair independent of G. For
the second sample in the antiparallel case use exact opposition. The
residual controls are bounded on finite intervals by loss decrease.
The identity holds by the pointwise absolutely continuous chain rule:
F' phi'=1. Its right side is in L2, so it also holds in that space.

Fix t and R>0. Choose M so that P(max_a |I_a(t)|<=M)>0. For a specified
sample, take G_a sufficiently large and positive that
F(G_a)-M-M'_T>F(R). Independence and Gaussian tails give positive
probability to the intersection. Then Z^(1)_a(t)>R. The negative
tail is obtained in the same way. Thus each first field has both
unbounded tails at every finite time.

When C=I the same argument can impose ANY prescribed sign pattern on
(G_1,G_2) and make both magnitudes arbitrarily large. The event for I
still has positive probability independently. Hence H^(1)(t) has
points of support arbitrarily close to each of (B,B), (B,-B),
(-B,B), and (-B,-B). If a nonzero real vector v satisfied
v_1 H^(1)_1+v_2 H^(1)_2=0 almost surely, it would vanish at both limit
points (B,B) and (B,-B), forcing v=0. Therefore the uncentered Gram

    Gamma_1(t)=(E_1[H^(1)_a(t)H^(1)_b(t)])_(a,b)

is positive definite for every finite t. No time-uniform lower bound
independent of the input or of T is required here. In the antiparallel
case its rank is one, while ||H^(1)_1(t)||_2>0; do not invert that Gram.

Equation (3) now makes each xi_a(t) nondegenerate. By (2),

    P(Z^(2)_a(t)>R)>=P(xi_a(t)>R+M_T)>0,

and the analogous negative-tail inequality also holds. This uses no
independence of S from xi. Each second field therefore also has both
unbounded tails.

For any such L2 variable Z, the space of affine functions aZ+b is a
closed two-dimensional subspace of L2: its Gram is positive definite
because Var(Z)>0. If its distance from phi(Z) were zero, there would
be a,b with phi(Z)=aZ+b almost surely. Boundedness of phi and an
unbounded tail force a=0. Strict monotonicity of phi would then force
Z to be constant, a contradiction. Consequently

    inf_(a,b in R) E[(phi(Z^(ell)_c(t))-aZ^(ell)_c(t)-b)^2]>0          (5)

for each hidden layer ell, sample c, and finite time t. This is a
distributional statement about the limiting fields, in addition to
the fixed scalar activation's ordinary global nonaffinity.

## 3. Strict motion at every positive physical time

Write f=(g,-g). Define the three raw kernel blocks

    K^(1)_ab=C_ab E_1[delta^(1)_a delta^(1)_b],
    K^(2)_ab=E_2[delta^(2)_a delta^(2)_b] E_1[H^(1)_a H^(1)_b],
    K^(3)_ab=E_2[H^(2)_a H^(2)_b],
    kappa=(1/4)y^T(K^(1)+K^(2)+K^(3))y.

Their Gram interpretations imply kappa>=0. Differentiation of f through
the layers and the adjoint identity give

    dot g=4(1-g)kappa,
    1-g(t)=exp(-4 integral_0^t kappa(u)du)>0.            (6)

The integral is finite on finite intervals by the bounded fields and
operators. Initially kappa=||(H^(2)_1-H^(2)_2)/2||_2^2>0: for C=I
the two independent nonconstant centered initial outputs differ;
for antiparallel inputs their difference is twice a nonzero field.
Continuity first gives g>0 for small positive times, and monotonicity
in (6) gives 0<g(t)<1 for EVERY t>0. Thus W^(3)(t) is not zero in L2.

Since phi'>0 everywhere, each delta^(2)_a(t) is nonzero. Its norm
in (3) makes zeta_a(t) nondegenerate. The bounded remainder in (2)
then makes Q^(1)_a(t) have unbounded tails, hence nonzero norm. For
C=I equation (1) reduces to

    dot Z^(1)_a=2(1-g)y_a phi'(Z^(1)_a)Q^(1)_a.

For antiparallel inputs the reduced factor is 4(1-g). Each first
preactivation speed and, after multiplication by phi'>0, each first
activation speed is therefore strictly positive in L2.

The hidden matrix also moves. When C=I its squared Hilbert--Schmidt
speed is

    4(1-g)^2 sum_(a,b) y_a y_b
       E_2[delta^(2)_a delta^(2)_b] Gamma_1(t)_ab
    >=4(1-g)^2 lambda_min(Gamma_1(t))
       sum_a ||delta^(2)_a||_2^2>0.                  (7)

The inequality follows pointwise in population 2 by applying the
positive definite matrix Gamma_1 to the vector (y_a delta^(2)_a),
then integrating. For antiparallel inputs dot W^(2) is the nonzero
rank-one operator 4(1-g)delta^(2)_1 tensor H^(1)_1.

Put c_a=-2r_a. Using dot Z^(2)_a=dot W^(2)H^(1)_a+
W^(2)dot H^(1)_a and moving the operator through its actual adjoint,

    sum_a c_a E_2[delta^(2)_a dot Z^(2)_a]
      =||dot W^(2)||_HS^2 + sum_a ||dot Z^(1)_a||_2^2              (8)

when C=I. In the antiparallel reduction the last sum is replaced by
the ONE independent first-field squared speed. To see this directly,
its contribution before reduction is sum_a c_a E_1[delta^(1)_a
dot Z^(1)_a]=(c_1-c_2)E_1[delta^(1)_1 dot Z^(1)_1]
=||dot Z^(1)_1||_2^2. There is no extra factor two.

The right side of (8) is positive. Thus not both second-layer speeds
vanish; sample symmetry makes their norms equal, so each is positive.
Multiplication by phi'>0 proves the same assertion for H^(2). The
readout moves because dot W^(3)=2(1-g)(H^(2)_1-H^(2)_2), and a zero
contrast would contradict g=E_2[W^(3)(H^(2)_1-H^(2)_2)]/2>0.
This proves nonfreezing at every t>0 without a uniform speed lower
bound as t tends to infinity.

## 4. Initial reverse law, with the actual reused transpose

Here is the initial law needed for quantitative nonlaziness. When
C=I put V=(phi(X_1)-phi(X_2))/2 and D_a=V phi'(X_a). Then

    Q_a=(W^(2)_0)^* D_a
       =sum_b B_ab phi(G_b)+eta_a,                    (9)
    B=E_2[D X^T]/m,
    eta~N(0,Sigma), Sigma=E_2[D D^T], eta independent of G.

The equality specifies the joint law in the first population; it does
not make different finite coordinates independent after matrix reuse.
In particular Sigma_aa>0 since V is nonzero almost surely and phi'>0.
Indeed Sigma is positive definite: if v^T D=0, continuity and the
full support of the Gaussian pair force v_1 phi'(x)+v_2 phi'(y)=0
for all x!=y. The nonconstancy of phi' forces v=0.

For completeness (9) follows by elementary finite Gaussian conditioning.
Here W^(2)_0 is n by n and the two field matrices have n rows.
Let H have the two columns phi(z^(1)_a(0)), Z=W^(2)_0 H,
Gamma_n=H^T H/n, and let D be the two rowwise functions of Z above.
On the event Gamma_n is invertible, rowwise Gaussian projection gives

    W^(2)_0=Z(H^T H)^(-1)H^T+tilde W P_(H perp),

where the remaining Gaussian matrix is independent of H,Z. Therefore
the exact conditional law of the reverse pair is

    (W^(2)_0)^T D
      = H Gamma_n^(-1)(Z^T D/n)
        +P_(H perp) mathcal G Sigma_n^(1/2),
    Sigma_n=D^T D/n,                                 (10)

with independent standard Gaussian entries in mathcal G. The original
Gaussian row conditioning, the law of large numbers for H, and bounded
continuous row functions D give Gamma_n->mI,
Sigma_n->Sigma, Z^T D/n->E[X D^T] in probability. The latter two follow
conditionally first, since rows of Z given H have covariance Gamma_n;
their conditional variances are O(1/n) on bounded-Gram events. For
Z D use its Gaussian second moment, rather than claiming it bounded.

The removed Gaussian projection has conditional mean square at most
2 trace(Sigma_n)/n in RMS norm and tends to zero in probability.
More generally the CONDITIONAL EXPECTATION, given the initial first
coordinates and Z, of its empirical pth moment for p>=2 is at most
c_p ||Sigma_n||^(p/2) sum_i P_ii^(p/2)/n<=2c_p||Sigma_n||^(p/2)/n.
Markov's inequality gives convergence in probability of each such
empirical error. On events whose probabilities tend to one, Gamma_n
has a bounded inverse and the regression coefficient in (10) is bounded,
since their limits exist and m>0. After dropping the projection,
conditional independent Gaussian added rows give
variance O(1/n) for bounded tests and for localized polynomial tests.
The initial Gaussian moments, bounded H,D, and Gaussian moments of the
added rows justify removing the localization. Thus the JOINT empirical
law with the old first coordinates converges, including every fixed
polynomial moment, to (9). No central-limit or post-reuse iid assertion
is used. This also proves the initial reverse law inside any canonical
common-space construction respecting these joint finite programs.

For antiparallel inputs use one column H=phi(G_1), X~N(0,m),
D=phi(X)phi'(X). The same rank-one proof gives

    Q=(W^(2)_0)^* D=b H+eta,
    b=E[DX]/m, eta~N(0,E[D^2]), eta independent of G_1.            (11)

In both cases Q_a has a strictly positive conditional Gaussian variance.
Therefore ||phi'(G_a)Q_a||_2>0. Only finite-dimensional Gaussian
projection and elementary averaging have been used.

## 5. The hidden kernel and the full kernel actually change

Near zero use feature time ds/dt=4(1-g), s(0)=0, which is strictly positive.
Then the flow is the gradient of g in the raw parameter metric, so
g'=kappa (prime means d/ds). No finite-width clock identity is asserted.
We compute strong L2 first nonzero hidden velocities as s decreases
to zero; they also imply nonzero physical motion near zero.

When C=I, W^(3)(s)/s->V, delta^(2)_a(s)/s->D_a, and
Q^(1)_a(s)/s->Q_a. Define

    v^(1)_a=(y_a/2)phi'(G_a)Q_a,
    V^(2)=(1/2)sum_a y_a D_a tensor phi(G_a),
    v^(2)_a=(y_a/2)[m D_a+W^(2)_0(phi'(G_a)^2 Q_a)].            (12)

Then (Z^(1)_a)'/s->v^(1)_a, (W^(2))'/s->V^(2), and
(Z^(2)_a)'/s->v^(2)_a. These are strong limits: start with the readout
integral, then multiply by bounded continuous gates, use continuity in
operator norm and the actual adjoint, and substitute into each exact
flow equation. For a fixed L2 field, multiplication by uniformly bounded
gates converging in probability converges strongly by truncating that
field and using dominated convergence. This justifies every such
product without a false L2 Frechet-differentiability assertion.

The initial first-feature Gram mI gives

    d=sum_a ||v^(1)_a||_2^2+||V^(2)||_HS^2
      =(1/4)sum_a [||phi'(G_a)Q_a||_2^2+m||D_a||_2^2]>0.        (13)

Each second velocity is nonzero because

    y_a E_2[D_a v^(2)_a]
       =(1/2)[m||D_a||_2^2+||phi'(G_a)Q_a||_2^2]>0.

In the antiparallel case replace (12) by the one-field expressions

    v^(1)=phi'(G_1)Q,
    V^(2)=D tensor phi(G_1),
    v^(2)=mD+W^(2)_0(phi'(G_1)^2Q),
    d=||phi'(G_1)Q||_2^2+m||D||_2^2>0.             (14)

The reduced feature equations have coefficient one, not one half.
The same strong-limit argument proves (14), and E[Dv^(2)]=d>0.

Let kappa_hidden=(1/4)y^T(K^(1)+K^(2))y and
kappa_readout=(1/4)y^T K^(3)y=||(H^(2)_1-H^(2)_2)/2||_2^2.
The feature-gradient identity and (12)--(14) give

    kappa_hidden(s)=d s^2+o(s^2).

Differentiating kappa_readout along the L2 curve gives
kappa_readout'=sum_a y_a E_2[V(s)phi'(Z^(2)_a)(Z^(2)_a)'].
Here V(s)=(H^(2)_1(s)-H^(2)_2(s))/2. Dividing by s and using
(12), or the exact antiparallel pair and (14), yields
kappa_readout'(s)/s->2d. Integration therefore proves

    kappa_readout(s)=kappa_readout(0)+d s^2+o(s^2),
    kappa(s)=kappa(0)+2d s^2+o(s^2).                (15)

Thus the raw label-direction kernel changes strictly at leading order;
the conclusion is not merely that a parameter coordinate moves in a
kernel-null direction. The positive readout contribution and the
positive hidden contribution have both been included. Together with
(5) and Section 3, this excludes affine limiting activations, frozen
hidden layers, and a constant-kernel explanation, PROVIDED the global
canonical representation premises (1)--(3) are discharged separately.

No all-angle result, global representation construction, or independent
audit is claimed in this draft. There are no external heavy theorems
or numerical experiments in its proof.
