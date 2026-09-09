# A signed top-curvature budget without an alignment premise

Root candidate lemma, 2026-09-06. Not independently audited.
This is a new quantitative estimate, not a global population theorem.

Use phi(z)=z+log(1+exp z), p=phi', and r=phi''/phi'.
Then 1<p<2, 0<phi''<=1/4, and

  0<r<=R:=3-2 sqrt(2).

The last maximum follows by maximizing q(1-q)/(1+q) for 0<q<1.
All coordinates below are for one third-layer neuron and two samples.

## 1. The forced system and the claim

Let w,z_1,z_2 be C1 on [0,S], satisfying the exact top equations

  w'=F=(phi(z_1)-phi(z_2))/2,
  z_1'=w(g p_1-h p_2)/2+ell_1,
  z_2'=w(h p_1-g p_2)/2+ell_2.                         (1)

Here the Gram [[g,h],[h,g]] may vary continuously with time,
g>|h|. The lower-layer forcing ell is arbitrary continuous data;
no alignment of w with z_1-z_2 is assumed. The same statement and proof
hold for absolutely continuous w,z_1,z_2, integrable ell, and equations
(1) almost everywhere, with continuous Gram coefficients. Scalar
derivative identities are then used almost everywhere and integrated.
Define

  c(s)=g(s)-max(h(s),0)>0, H=max_s max(h(s),0),
  beta(s)=max(0,w phi''(z_1)/2,-w phi''(z_2)/2).

The positive curvature is in sample 1 when w>0 and sample 2 when
w<0. The claim is

  integral_0^S c(s) beta(s) ds
     <= log 2
        +H R^2 integral_0^S |wF| 1_{wF<0} ds
        +R integral_0^S (|ell_1|+|ell_2|) ds.           (2)

The extra cost is the readout's backward motion in squared magnitude:

  integral |wF| 1_{wF<0}
     = (1/2) integral [-(w^2)']_+.

Thus (2) explicitly includes every unaligned excursion instead of
postulating their absence. No bound on their number is needed.

## 2. Gate comparison on a fixed readout-sign sector

For w>0 put z_+=z_1,z_-=z_2; for w<0 reverse these choices.
Let q=|w|. In both cases

  beta=q phi''(z_+)/2,
  z_+'=q(gp_+-hp_-)/2+ell_+,

and hence

  (log p(z_+))'
      =c(s) beta + extra + r(z_+)ell_+.               (3)

If h<=0, the difference between the coefficient g-hp_-/p_+
and c=g is nonnegative, so extra>=0.
If h>0, then c=g-h and

  extra=h(p_+-p_-) beta/p_+.

Since p is increasing, this is nonnegative whenever wF>=0.
For wF<0, the fundamental theorem of calculus in the feature
coordinate gives

  |p_+-p_-| <= R |phi(z_+)-phi(z_-)| =2R|F|.

Indeed dp/dphi=phi''/phi'=r and phi is strictly increasing.
Also beta/p_+=q r(z_+)/2<=qR/2. Therefore always

  (log p(z_+))'
    >= c(s) beta
       -H R^2 |wF| 1_{wF<0}
       -R(|ell_1|+|ell_2|),                           (4)

away from w=0. These are the actual signed coefficients, not their
absolute values. In particular the bounded ratio r, rather than a
positive lower bound on the coordinate velocity, is what bounds the
unaligned correction.

## 3. Readout zero crossings add only favorable jumps

One cannot integrate (4) by assuming finitely many sign changes.
The following smoothing handles arbitrary zero sets.

Choose a smooth nondecreasing sigma_e with values in [-1,1],
equal to sign(w) for |w|>=e. Such a function is obtained by
integrating an even nonnegative smooth bump on [-e,e] and rescaling.
Put

  L_e=(log p_1+log p_2)/2
            +sigma_e(w)(log p_1-log p_2)/2.

It lies between 0 and log 2. Its derivative consists of a convex
combination of (log p_1)' and (log p_2)' and the extra term

  sigma_e'(w) F (log p_1-log p_2)/2 >=0.               (5)

The sign follows because phi and p are both strictly increasing.
For |w|>=e the convex combination is precisely the derivative
in (4). On |w|<e the drift parts in either gate derivative, and
c beta, have magnitude at most C_G e, where one can take
C_G=max_s(|g|+|h|)(R+1/8). Their forcing
parts are bounded in magnitude by R(|ell_1|+|ell_2|).
Discarding (5) therefore gives, on the entire interval,

  L_e' >= c beta
       -H R^2 |wF|1_{wF<0}
       -R(|ell_1|+|ell_2|)
       -C_G e.

Integrate, use L_e(S)-L_e(0)<=log 2, and let e decrease to zero.
This proves (2) with no premise concerning crossing times.
The same proof works on any subinterval, with its two endpoints.

## 4. An averaged consequence of the actual gradient action

Here is a precise conditional corollary for the intended architecture.
Use separate probability spaces Omega_1,Omega_2,Omega_3 and their
real L2 spaces. The first state is a pair (Z^(1)_1,Z^(1)_2) in
L2(Omega_1)^2, with input correlation matrix
C=[[1,rho],[rho,1]], -1<=rho<1. For -1<rho<1 its tangent squared
norm is E_1[v^T C^-1 v]. At rho=-1 restrict Z^(1)_2=-Z^(1)_1
and use E_1[v_1^2]. The remaining state consists of
W^(2):L2(Omega_1)->L2(Omega_2),
W^(3):L2(Omega_2)->L2(Omega_3), and W^(4) in L2(Omega_3).
Each operator is a fixed initial bounded operator plus a
Hilbert--Schmidt increment; the two increment norms are their
Hilbert--Schmidt norms. Together with the first block and the
readout L2 norm these define the raw Hilbert norm.

Define H^(1)_a=phi(Z^(1)_a),
Z^(2)_a=W^(2)H^(1)_a, H^(2)_a=phi(Z^(2)_a),
Z^(3)_a=W^(3)H^(2)_a, H^(3)_a=phi(Z^(3)_a).
The scalar objective, denoted J to distinguish it from the Gram
diagonal g, is

  J(theta)=E_3[W^(4)(H^(3)_1-H^(3)_2)/2].

All fields are in the displayed L2 spaces by linear growth of phi
and boundedness of the operators. This objective is C1 in the raw
Hilbert coordinates. Here are the needed differentiability details.
For fixed B in L2 and a perturbation v in L2, truncate |B| at N.
Taylor's theorem on the bounded part and the Lipschitz bound on
the remainder give

  |E B[phi(z+v)-phi(z)-phi'(z)v]|
      <= (N/8)||v||_2^2
            +4||B 1_{|B|>N}||_2 ||v||_2
      =o(||v||_2).

The last conclusion first lets v tend to zero, then N tend to
infinity. Expanding the scalar prediction from the top layer
downward pairs each remaining activation remainder with a fixed
L2 backward field, so the same bound applies. Terms with two
parameter/propagated increments are quadratic. Adjunction gives
the residual-free backward fields

  delta^(3)_a=W^(4)phi'(Z^(3)_a),
  delta^(2)_a=phi'(Z^(2)_a)(W^(3))*delta^(3)_a,
  delta^(1)_a=phi'(Z^(1)_a)(W^(2))*delta^(2)_a.

The matrix gradient blocks are
(delta^(ell)_1 tensor H^(ell-1)_1
 -delta^(ell)_2 tensor H^(ell-1)_2)/2, where
(u tensor v)h=u E[vh]; the readout gradient is
(H^(3)_1-H^(3)_2)/2. The first-pair gradient is
C(delta^(1)_1,-delta^(1)_2)^T/2, with the restricted interpretation
at rho=-1. Gradient continuity follows by propagating strong L2
differences through bounded operators: a changed bounded gate times
a fixed L2 factor tends to zero after truncating that factor, and
rank-one factors converge in Hilbert--Schmidt norm. This proves the
scalar C1 claim without asserting Frechet differentiability of
phi:L2->L2.

Now assume an EXISTING C1 uncut raw gradient curve theta'=grad_raw J
on [0,S], with W^(4)(0)=0 almost surely, and J(S)<=1. No existence
or convergent regularization is supplied by this assumption or this
lemma. The raw Hilbert chain rule gives

  integral_0^S ||theta'||_raw^2 ds =J(S)<=1.

In particular, with F=w',

  E integral_0^S F^2 ds <=1.

Since w(0)=0, Cauchy--Schwarz first in time gives
w(s)^2<=s integral_0^s F(u)^2du. Integrating and exchanging
nonnegative integrals gives

  E integral_0^S w^2 ds <=(S^2/2) E integral_0^S F^2 ds.

Applying Cauchy--Schwarz on the product of time and neuron probability,

  E integral_0^S |wF|1_{wF<0} ds <= S/sqrt(2).          (6)

The forcing bound follows from the specified spaces, not a further
stability theorem. Let M_0 bound the two initial first-field L2
norms and the two initial operator norms. Cauchy--Schwarz in time
and the action bound place the curve in the initial-centered raw
ball of radius sqrt(S). Put M=M_0+sqrt(S), B_1=2M+log 2.
Then ||W^(2)||_op,||W^(3)||_op<=M and ||H^(1)_a||_2<=B_1.
Each first-field tangent obeys
||(Z^(1)_a)'||_2<=||theta'||_raw: for nonsingular C use
|v_a|<=sqrt(e_a^T C e_a) sqrt(v^T C^-1 v), and at rho=-1 use
v_2=-v_1.

An absolutely continuous L2 curve has an almost-everywhere
coordinatewise absolutely continuous representative, obtained by
integrating its L2 derivative and applying Fubini. The scalar
chain rule and phi'<=2 give its L2 along-curve chain rule.
Using ||W'||_op<=||W'||_HS, the exact forward equations yield

  ||(H^(1)_a)'||_2<=2||theta'||_raw,
  ||(Z^(2)_a)'||_2<=(B_1+2M)||theta'||_raw,
  ||(H^(2)_a)'||_2<=2(B_1+2M)||theta'||_raw.

The actual forcing is ell_a=W^(3)(H^(2)_a)'. With
C_S=2 sqrt(2) M(B_1+2M) the action bound therefore gives

  E integral_0^S (|ell_1|^2+|ell_2|^2) ds <= C_S^2.

Assume that the current feature Gram is positive definite and
exchange symmetric, with COMMON (not neuron-dependent) entries
g(s)=E_2[(H^(2)_1)^2]=E_2[(H^(2)_2)^2] and
h(s)=E_2[H^(2)_1 H^(2)_2]. These are continuous by L2 continuity.
Differentiating Z^(3)_a=W^(3)H^(2)_a and inserting its rank-one
gradient gives exactly (1) on Omega_3 almost everywhere. Thus the
absolutely continuous version of the scalar lemma applies. The
corresponding H=max h_+ is common to all third-layer neurons.
Consequently (2) implies the actual weighted curvature estimate

  E integral_0^S c(s) beta(s) ds
       <= log 2+H R^2 S/sqrt(2)+R sqrt(2S) C_S.        (7)

This controls an actual signed curvature functional of an existing
trained trajectory; it is not a claim that action bounds imply
arbitrary response tails. If additionally c>=c_*>0, it bounds
E integral beta by the displayed right side divided by c_*.
Any c_* must be uniform in time and over the neuron variables;
constants may depend on the fixed inputs and initial bounds.
The weight c and the Gram's symmetry/positivity must not be discarded
when applying (7).

In a finite exactly exchange-symmetric feature flow, the same argument
uses empirical averages, provided the current two-feature Gram is
positive definite on the interval. The Gaussian finite system is
not exactly symmetric pathwise; this observation supplies no global
finite-to-population comparison by itself.

## 5. Remaining distinction: mean curvature versus response tails

There is already a simpler COARSE first-moment bound under the
same action premise: beta<=|w|/8 and the readout inequality above
give E integral_0^S beta<=S^(3/2)/(8 sqrt(2)).
Thus first-moment control alone is not a new resolution of the
response obstacle. The new content of (2) is its signed,
subinterval-wise path estimate accounting for unaligned excursions.

The top tangent integrating-factor estimate involves
exp(Lambda integral beta), as well as Gram variation and lower
tangent forcing. A uniform FIRST MOMENT of integral beta, such
as (7), does not bound that exponential or the expected propagator.
The possibility of concentrating a large curvature budget on a rare
set remains. The previous forcing-free traversal argument has thus
been strengthened to include actual unaligned excursions, but its
full-response continuation consequence is still unproved.

No clipped-scheme gradient-action identity is assumed. No all-finite
population existence, uniqueness, Gaussian typicality, or full
two-label resolution is asserted. A next continuation argument must
control the distribution, not merely the mean, of these costs and
the coupled lower response.
