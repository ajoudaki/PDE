# Two backward clips recover the two-sample short response estimate

Root candidate, 2026-09-06. This note proves a mesh/cap-uniform
response lemma for an explicitly stated two-sample scalar Gaussian
Euler law. It is not yet a complete two-sample limit theorem.
Its finite-program identification dependency is Section 3 of
/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md,
SHA256 bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e,
read in full by the root. The full eventual theorem must import that
proof and its common-space/convergence arguments, not just this lemma.

Take phi(z)=1+arctan(z)/10, epsilon=1/10, m=5/6, a=7/6.
Thus m<phi<a, 0<phi'<=1/10, and |phi''|<=1/5.
Let y_1,y_2 each equal +1 or -1. Let C be the two-sample Gram matrix,
with diagonal one and off-diagonal rho in [-1,1]. The estimates below
even allow rho=1, though nontriviality at that configuration is not
part of the user's contract.

Let tau_R be smooth, odd, equal to its argument on [-R,R], with
|tau_R(q)|<=min(|q|,2R) and 0<=tau_R'<=1.
Use arbitrary finite caps R_1,R_2>=1. The bottom clip affects only
the first-coordinate update, and the middle clip defines delta^(2).
The readout starts at zero. The first coordinate remains RAW; no
componentwise F transform is used.

## 1. Exact scalar law and derivative convention

Let Delta>0, M a nonnegative integer, S=M Delta<=3/2.
Time index k ranges from 0 to M, sample index a from 1 to 2.
Let (G_1,G_2) be centered Gaussian with covariance C. The scalar law is

  Z^(1)_{ka}=G_a+(Delta/2)sum_(r<k,b) C_ab y_b
                         phi'(Z^(1)_{rb})tau_R1(q^(1)_{rb}),
  H^(1)_{ka}=phi(Z^(1)_{ka}),

  Z^(ell)_{ka}=xi^(ell)_{ka}
                  +sum_(r<k,b) A^(ell)_{ka,rb}delta^(ell)_{rb},
  H^(ell)_{ka}=phi(Z^(ell)_{ka}), ell=2,3,

  W^(4)_k=(Delta/2)sum_(r<k,b)y_b H^(3)_{rb},
  delta^(3)_{ka}=W^(4)_k phi'(Z^(3)_{ka}),

  q^(2)_{ka}=zeta^(2)_{ka}
                       +sum_(r<=k,b) B^(3)_{ka,rb}H^(2)_{rb},
  delta^(2)_{ka}=phi'(Z^(2)_{ka})tau_R2(q^(2)_{ka}),

  q^(1)_{ka}=zeta^(1)_{ka}
                       +sum_(r<=k,b) B^(2)_{ka,rb}H^(1)_{rb}.     (1)

Each sum over b includes both samples. The four centered Gaussian
source groups xi^(2),xi^(3),zeta^(2),zeta^(1) are mutually independent
and independent of the root pair. Within a group both time and sample
correlations are retained, including singular covariance matrices:

  E[xi^(ell)_{ka}xi^(ell)_{rb}]
                         =E[H^(ell-1)_{ka}H^(ell-1)_{rb}],
  E[zeta^(ell-1)_{ka}zeta^(ell-1)_{rb}]
                         =E[delta^(ell)_{ka}delta^(ell)_{rb}].

The deterministic coefficients are

  A^(ell)_{ka,rb}
     =E[partial H^(ell-1)_{ka}/partial zeta^(ell-1)_{rb}]
                       +(Delta/2)y_b E[H^(ell-1)_{ka}H^(ell-1)_{rb}],
                                                        r<k,
  B^(ell)_{ka,rb}
     =E[partial delta^(ell)_{ka}/partial xi^(ell)_{rb}]
       +(Delta/2)1_(r<k)y_b E[delta^(ell)_{ka}delta^(ell)_{rb}],
                                                        r<=k.  (2)

All formal partial derivatives hold previously selected deterministic
coefficients and Gaussian covariance parameters fixed. Distinct source
slots remain distinct even at singular covariances.

The finite realization to be identified has iid bottom neuron tuples
(z^(1)_(0,i,1),z^(1)_(0,i,2))~N(0,C); two initial matrices
W^(2)_0,W^(3)_0 with iid N(0,1/n) entries, independent of each other
and all root tuples; and EXACTLY zero initial readout W^(4)_0=0.
Its current forward fields use the current matrices. Its reverse
queries are (W^(3)_k)^T delta^(3)_(ka) and
(W^(2)_k)^T delta^(2)_(ka), with gates and cuts as in (1).
Its raw bottom and readout updates are the finite vector versions of
(1); both sample queries are computed before the simultaneous Euler
updates. Identification concerns each fixed M,Delta,R_1,R_2, not a
program whose number of queries grows with width.

To relate this law to that actual finite Euler scheme, unroll each
matrix's updates
W^(ell)_{k+1}=W^(ell)_k+(Delta/2n)sum_b
y_b delta^(ell)_{kb}(h^(ell-1)_{kb})^T.
The learned forward term has coefficient
(Delta/2)y_b E[H^(ell-1)_{ka}H^(ell-1)_{rb}], and the learned reverse
term has coefficient
(Delta/2)y_b E[delta^(ell)_{ka}delta^(ell)_{rb}], precisely as in (2).
The initial-action forward response is the expected source derivative
in (2), and the reverse response is its transpose counterpart.
The finite-program dependency proves these response identities, joint
empirical averages, and removal of singular-Gram query perturbations.

At fixed caps the raw first update is a bounded product of bounded
smooth gates and clipped queries; all required coordinate maps can be
extended to globally Lipschitz C^1 maps with bounded first derivatives.
The readout satisfies |W^(4)_k|<=aS and can be smoothly truncated outside
this known interval in a fixed program without changing values or
derivatives on attained states. Finitely many empirical contractions
can be restored from their deterministic limits by finite Lipschitz
induction. Thus the stated identification uses a fixed finite program,
not an unproved number-of-queries-uniform Gaussian assertion.

## 2. Claim and induction order

Put

  U_k=max_a sum_(r<=k,b)|B^(2)_{ka,rb}|,
  V_k=max_a sum_(r<=k,b)|B^(3)_{ka,rb}|.

We prove, uniformly in caps, mesh, labels and C,

  V_k<=3067/3200<1,
  U_k<=71063018523/73728000000<97/100,                    (3)

and for ell=2,3 and r<k,

  |A^(ell)_{ka,rb}| < (3/2)Delta/2.                     (4)

In particular for j=1,2 and either sample,

  E exp((q^(j)_{ka})^2/16)<2.                            (5)

Let A=3/2 (a bound on the time-kernel coefficient, not the activation
bound a). At zero time the readout and delta^(3) vanish as formal
expressions, so B^(3)_0=0 and zeta^(2)_0=0 almost surely.
Keep the formal expressions q^(2)_(0a)=zeta^(2)_(0a) and
delta^(2)_(0a)=phi'(xi^(2)_(0a))tau_R2(zeta^(2)_(0a)).
Their FORWARD-source derivatives vanish on the attained Gaussian law,
because tau_R2(0)=0. Hence B^(2)_0=0 and U_0=V_0=0.
Their reverse-source derivatives need not vanish: for example the
derivative of delta^(2)_(0a) in its own reverse-source slot is
phi'(xi^(2)_(0a))>0. No zero-variance source slot is deleted in this
base case or in later formal differentiation.

Assume U_r,V_r<=1 for all r<k. Construct and bound the current objects
in the order

  A^(2), Z^(2), A^(3), Z^(3), delta^(3),
  B^(3), q^(2), delta^(2), B^(2).

The first-coordinate values at time k use only past backward queries.
The following estimates do not use U_k before bounding it.

## 3. Bottom raw-coordinate sensitivities

For a single past source zeta^(1)_(sb), its first direct contribution
to any Z^(1)_(ja), j>s, has absolute value at most Delta epsilon/2,
because |C_ab|<=1 and |tau_R1'|<=1.
Writing a formal variation as d, the raw first update satisfies

  |d[phi'(Z^(1)_(ra))tau_R1(q^(1)_(ra))]|
    <= |q^(1)_(ra)||dZ^(1)_(ra)|/5 + |dq^(1)_(ra)|/10.

Furthermore

  |dq^(1)_(ra)| <= 1_((r,a)=(s,b))
               +(1/10)sum_(v<=r,c)|B^(2)_(ra,vc)||dZ^(1)_(vc)|.

The sum over a of the absolute first-update coefficient |C_ba y_a|/2
is at most one. Taking maxima over output samples and preceding times,
the elementary product-form discrete Gronwall induction gives

  |partial H^(1)_(ja)/partial zeta^(1)_(sb)|
                                      <=(Delta/200)E^(1)_j,     (6)
  E^(1)_j=exp{Delta sum_(r<j)[max_a|q^(1)_(ra)|/5+U_r/100]}.

For completeness, the comparison used here says that
u_j<=u_0+sum_(r<j)c_r max_(v<=r)u_v, c_r>=0, implies
max_(v<=j)u_v<=u_0 product_(r<j)(1+c_r)<=u_0 exp(sum c_r).
The same proof applies when the initial injection begins at s+1.

Past top queries have
||q^(2)_(ra)||_2<=aS/10+a<=161/120=:Q_0, r<k,
because their source variance is at most (aS/10)^2 and response
shift at most aV_r. Hence each bottom Gaussian source has standard
deviation <=Q_0/10. Also
max_a|q^(1)_(ra)|<=max_a|zeta^(1)_(ra)|+a.

For two arbitrarily correlated centered Gaussians with variances <=v,

  E exp(lambda max_a|G_a|)
       <=sum_a E exp(lambda|G_a|)<=4 exp(lambda^2 v/2).   (7)

Jensen over the time slots requires no independence in time. It gives

  E E^(1)_j
    <=4 exp{S(a/5+1/100)+(S/5)^2(Q_0/10)^2/2}
    <4 exp(2/5)<6.                                     (8)

The first exponent is at most
73/200 + (9/200)(161/1200)^2 <2/5.
For the last inequality, e<11/4 and
(11/4)^2<(3/2)^5 give e^(2/5)<3/2.
Using (6) in (2),

  |A^(2)_(ja,sb)|
    <=(Delta/2)[a^2+(1/100)E E^(1)_j]
    <(Delta/2)(49/36+3/50)<A Delta/2.                   (9)

This is the replacement for the one-sample natural-coordinate argument.

## 4. Middle sensitivities with both sample correlations retained

Define the maximum total forward-source derivative row

  R_j=max_a sum_(s<=j,b)
                  |partial Z^(2)_(ja)/partial xi^(2)_(sb)|.

There is exactly one direct derivative in each sample's current row,
not one for every source slot. For a forward-source variation,

  |d delta^(2)_(ra)|<=|q^(2)_(ra)||dZ^(2)_(ra)|/5
                                               +|dq^(2)_(ra)|/10,
  |dq^(2)_(ra)|<=(1/10)sum_(v<=r,b)
                                    |B^(3)_(ra,vb)||dZ^(2)_(vb)|.

Using (9), sum over the two update samples. Their factor Delta/2
becomes Delta, not 2 Delta. Discrete Gronwall gives

  max_(v<=j) R_v <= E^(2)_j,
  E^(2)_j=exp{A Delta sum_(r<j)
                           [max_a|q^(2)_(ra)|/5+V_r/100]}.       (10)

For a single reverse source zeta^(2)_(sb), the first injection into
the forward recursion is at most A Delta/20, since (9) gives
A Delta/2 and the gate gives 1/10. The same argument yields

  |partial H^(2)_(ja)/partial zeta^(2)_(sb)|
                                  <=(A Delta/200)E^(2)_j.      (11)

The middle reverse Gaussian variances are <=(aS/10)^2<=(7/40)^2.
Using (7), time Jensen, and the past V_r<=1, for p>=1 we get

  E(E^(2)_j)^p
    <=4 exp{219p/400 +3969p^2/1280000}.                  (12)

Thus E E^(2)_j<8: the exponent for p=1 is less than 3/5,
and e^(3/5)<2 follows from e<3 and 3^3<2^5.
For p=2, taking the square root in (12) gives

  ||E^(2)_j||_2
    <=2 exp{219/400+7938/1280000}<7/2.                  (13)

Indeed the exponent is less than 5/9; e<68/25 follows from its
series through degree five and a geometric bound on the remaining
tail. The integer inequality (68/25)^5<(7/4)^9 then gives
e^(5/9)<7/4.
Equations (11)-(12) now give

  |A^(3)_(ja,sb)|
    <=(Delta/2)[a^2+(A/100)E E^(2)_j]
    <(Delta/2)(49/36+3/25)<A Delta/2.                   (14)

The strict margin is small but positive: 49/36+3/25=1333/900<3/2.

## 5. Top response, then current middle response

Let T_j be the maximum, over the two samples, of the total absolute
xi^(3)-derivative row of Z^(3) at time j. Differentiate the readout
sum and the top gate. Since |W^(4)_j|<=aS,

  max_a sum_(s<=j,b)|partial delta^(3)_(ja)/partial xi^(3)_(sb)|
     <=(Delta/100)sum_(r<j)T_r +(aS/5)T_j
     <=(73/300)S max_(v<=j)T_v.

Equation (14) and the strictly past forward recursion give

  max_(v<=j)T_v<=exp{A(73/300)S^2}
                         <=exp(657/800)<5/2.

For example 657/800<5/6 and e^(5/6)<3^(5/6)<5/2,
the last inequality following from 3^5 2^6<5^6.
Adding the learned covariance row in (2) proves the CURRENT bound

  V_k<=(73/300)S(5/2)+a^2 S^3/100
                    <=73/80+147/3200=3067/3200=:V_*.    (15)

We may now sharpen the current query norm, before using any U_k bound:

  ||q^(2)_(ka)||_2<=aS/10+aV_*
                         <=24829/19200=:Q_*.

The same Q_* bound holds for past times, since their completed induction
steps also proved (15), not merely V_r<=1. The current middle derivative
row obeys, by the full current return in its expression (1),

  sum_(s<=k,b)|partial delta^(2)_(ka)/partial xi^(2)_(sb)|
                     <=(|q^(2)_(ka)|/5+V_k/100)E^(2)_k.

Cauchy--Schwarz and (13), followed by the covariance row bound in (2),
therefore yield

  U_k <= (7/2)(Q_*/5+V_*/100)+(3/200)Q_*^2
        =71063018523/73728000000 <97/100<1.               (16)

The learned covariance row has factor
(Delta/2) times two samples, and at most S/100 times Q_*^2.
No current U_k entered (9), (14), (15), or (16).
The induction closes for all meshes and caps and proves (3)-(4).

## 6. Two actual-query Gaussian envelopes

For either reverse layer and either sample, (1) and (3) give

  q^(j)_(ka)=zeta^(j)_(ka)+beta^(j)_(ka),
  |beta^(j)_(ka)|<=a.

The variance of zeta^(2) is <=(7/40)^2. The variance of zeta^(1)
is <=(Q_*/10)^2<(7/40)^2. Neither beta is asserted independent
of its source. The elementary squared inequality therefore gives

  E exp(q^2/16)
     <=exp(a^2/8) E exp(zeta^2/8)
     <=exp(49/288)(1-49/6400)^(-1/2)<2,

by the one-dimensional Gaussian integral. For the numerical bound
exp(49/288)<exp(1/5)<=5/4 and the other factor is <4/3.
This proves (5) for both problematic multipliers.

## Scope and next obligations

The response estimate itself allows both label modes and all correlations.
It is uniform only on feature time [0,3/2]. It does not show that an
opposite-label trajectory reaches g=1 on this interval.

For a common label y in {-1,1}, define
f_a=E[W^(4)H^(3)_a] and g=y(f_1+f_2)/2.
A correctly constructed uncut feature flow would have LABEL-ALIGNED
readout derivative (y W^(4))'=(H^(3)_1+H^(3)_2)/2>=m and label-mode
kernel >=m^2. It would therefore reach g=1 by feature time 36/25<3/2. The usual
nonattainment clock would cover all finite physical times. This is a
consequence once clipping removal and the gradient/symmetry premises
are supplied, not a declaration that those arguments have been audited
for this extension already.

For the comparison proof, both q^(1) and q^(2) must now be clipped.
The asymmetric velocity comparison must use their reference tails,
with a coefficient linear in the comparison cap. Exact finite physical
GD/GF must be compared directly to the population physical reference:
their off-mode residual is not zero pathwise.

The eventual single document must prove the common-space construction,
both-cap removal, physical comparison and exact-GD stopping, full
observables, and strict nonlinearity/nonfreezing. The opposite-label
global continuation remains a separate unresolved obligation.
