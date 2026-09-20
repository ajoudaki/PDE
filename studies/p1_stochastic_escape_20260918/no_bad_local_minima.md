# No suboptimal local minima in the canonical p=1 population state space

2026-09-19. Lead candidate continuing this study's local escape investigation.
Scientific inputs: the complete established `docs/observable_p1.md` and
`docs/NOTATION.md`, and this study's current exact model and gradient
derivations. No other study or external result is an input. The proof below
is self-contained from the displayed model. This candidate was developed
without seeing the independent general-equilibrium route.

## 1. Statement, topology, and a distinction about straight lines

Let x_1,...,x_m lie on sqrt(d) S^(d-1), d>=2, with no two parallel or
antiparallel. Let mu_i>0 sum to one and let y_i be arbitrary finite real
labels, including zero; mixed binary labels are a special case. There is
no linear independence assumption and
no restriction m<=d. Use the canonical correlated Gaussian marks,
dictionary normalization, tanh activation, full trainable matrix and
unhalved weighted square loss of the p=1 closure.

The theorem concerns the odd invariant state class containing canonical
initialization. Thus b_1 in R^(2d), b_2 in R^d are the nonconstant
canonical marks, w and c are odd square-integrable fields on their
respective Gaussian carriers, and M is any finite d-by-2d matrix. The
topology is the physical population-L2/L2/Frobenius norm. A local minimum
means that some open ball in this topology contains no smaller loss.

**Theorem. Every local minimum of L in this state space has L=0.**
Equivalently, every positive-loss state, including every positive-loss
equilibrium, has arbitrarily close states with strictly smaller loss.

This is an ambient population landscape theorem. It supplies no canonical
reachability, stochastic excitation, rate, compactness, basin measure, or
global training theorem. Its small-population-set variations are legitimate
in the exact nonatomic population, and do not prove the analogous theorem
for a fixed finite population or finite-width network.

The theorem is weaker than saying every bad point has a straight direction
with a negative leading Taylor coefficient. For example, the polynomial

\[
 F(s,t,z)=1+s^2-2st^2+t^6
\tag{0}
\]

has positive leading quadratic coefficient on every line with nonzero
s-component, positive leading sixth-order coefficient when only the
t-component is nonzero, and is exactly flat in z. Yet the curve s=t^2
has F=1-t^4+t^6<1 near zero. This is a logical illustration, not an
asserted p=1 realization. The theorem below does not settle the stronger
claim that at each bad equilibrium there exists a fixed straight direction
with a negative leading Taylor coefficient. The separate, subsequently
checked construction in [straight_line_geometry_attempt.md](straight_line_geometry_attempt.md)
disproves that stronger claim in this very population model; it does not
alter the local-minimum theorem proved here.

## 2. Model and basic carrier properties

Write u_i=x_i/sqrt(d) only in the proof. For phi=tanh, define

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i=\phi(b_2^Tv_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i,
\]
\[
 d_i=E_2[b_2c\phi'(b_2^Tv_i)],\qquad
 L=\sum_i\mu_i r_i^2.
\tag{1}
\]

The exact matrix derivative and the derivative under a change of the finite
lower moments are

\[
 \nabla_M L=2\sum_i\mu_i r_i d_i a_i^T,
\qquad
 DL[\delta a]=2\sum_i\mu_i r_i d_i^TM\delta a_i.
\tag{2}
\]

For fixed c,M, loss is a C2 function of the finitely many a_i, with a
quadratic remainder uniformly bounded near the current moments. This uses
bounded b_2, bounded derivatives of tanh, and E|c|<=||c||_2.

The canonical marks are bounded. Their Grams are positive definite: the
upper coordinates are independent nondegenerate odd transformed Gaussians;
for the lower coordinates, conditional on the forward Gaussian coordinate,
the reverse feature has positive variance. Independent coordinate pairs
and invertible ridge normalization preserve this property. The law of b_2
has a strictly positive density on an open cube about zero.

The lower Gaussian carrier is nonatomic and has a measure-preserving
negation involution omega -> -omega. Both marks and admissible fields
negate under this involution. Use the half-carrier Omega_+={G_1>0}; it
and its negative partition the carrier up to a null set. Any measurable
positive-measure subset of Omega_+ has subsets of arbitrarily small positive
measure. More explicitly, the function t -> P(B intersect {G_1<=t}) is
continuous, since G_1 has no atoms, and increases from zero to P(B).
The intermediate value theorem supplies such subsets even for arbitrary B.

### Independence of the input ridge functions

The functions s -> phi(s dot u_i), for s in R^d, are linearly independent.
Choose r outside the finitely many proper hyperplanes r dot u_i=0 and
r dot(u_i plus-or-minus u_j)=0. The resulting nonzero numbers r dot u_i
have distinct squares. On the line s=t r, the first m odd Taylor
coefficients of a putative relation give a Vandermonde system in those
squares, so every coefficient vanishes. All odd tanh coefficients are
nonzero: writing tanh t=sum_{n>=0}(-1)^n b_n t^(2n+1), phi'=1-phi^2
gives b_0=1 and (2n+1)b_n=sum_{a+b=n-1}b_a b_b>0 for n>=1.
Existence of r follows because a finite product of nonzero linear
polynomials is not the zero polynomial; a nonzero polynomial cannot
vanish identically on R^d, by induction on dimension.

## 3. A derivative ridge cannot lie in a finite ridge span

For arbitrary vectors v,v_1,...,v_m in R^d and any nonzero z in R^d,

\[
 J(b)=(b^Tz)\phi'(b^Tv)
       \notin\operatorname{span}\{\phi(b^Tv_j):1\le j\le m\}
       \quad\text{in }L^2(\operatorname{Law}(b_2)).
\tag{3}
\]

Here the v_j may be zero, repeated, parallel, or antiparallel; no
separation assumption is made on the hidden effective vectors.

Suppose a relation held. Continuity and positive density make it an
identity on the open cube supporting b_2. Choose r with r dot z nonzero,
and also r dot v nonzero when v is nonzero. Substituting b=t r near zero
gives

\[
 \frac{ct}{\cosh^2(at)}=\sum_j\alpha_j\tanh(a_jt),
 \quad c=r\cdot z\ne0,\quad a=r\cdot v,\quad a_j=r\cdot v_j.
\tag{4}
\]

Multiply by cosh^2(at) product_j cosh(a_jt). Both resulting sides are
entire functions of the complex variable t, finite sums of polynomials
times exponentials. Equality near real zero makes all Taylor coefficients
equal; their entire Taylor series therefore give equality for all complex t.

If v=0, then a=0. Dividing again on the real axis would make the
unbounded function ct a finite sum of bounded tanh functions, impossible.
If v is nonzero, then a is nonzero. At t_0=i*pi/(2a), cosh(at) has a
simple zero and t_0 is nonzero. Let q count the factors cosh(a_jt) that
vanish there; each such zero is simple. The multiplied left side
ct product_j cosh(a_jt) has zero of exactly order q. Each right-side
term has order at least q+1, due to the factor cosh^2(at): removing its
own denominator factor removes at most one of the q zeros. A sum of such
terms cannot have a smaller vanishing order. This contradiction proves (3).

In particular, if H is the finite-dimensional span of all H_i, the field
k=J-Proj_H J is bounded, odd, nonzero, and orthogonal to every H_i.
No inverse of a possibly singular feature Gram is needed for this
orthogonal projection onto its actual span.

## 4. What local minimality forces in the first layer

**Lemma. At any local minimum, r_i M^T d_i=0 for every i.**

Fix a putative local minimum and define, for a lower mark omega and a
trial first-layer weight s in R^d,

\[
 F_\omega(s)=\sum_i\mu_i r_i\,(b_1(\omega)^TM^Td_i)
                                      \phi(s\cdot u_i).
\tag{5}
\]

We first show that for almost every omega, w(omega) minimizes F_omega
over all s. If this failed, continuity in s would supply a rational s,
numbers delta>0,R<infinity, and a positive-measure set B in Omega_+ on
which |w|<=R and F_omega(s)-F_omega(w)<=-delta. Countability of
rational s, rational positive delta and integer R justifies this reduction.
By oddness, any positive-measure failure on the other half reflects to
such a failure on Omega_+ with s replaced by -s.

Choose a subset E of B of arbitrarily small measure epsilon>0. Replace
w by s on E and by -s on -E, leaving it unchanged elsewhere. This
preserves oddness and has squared L2 displacement at most
2 epsilon(|s|+R)^2. Its exact lower-moment change is

\[
 \delta a_i=2\int_E b_1(\omega)
       [\phi(s\cdot u_i)-\phi(w(\omega)\cdot u_i)]\,dP_1(\omega),
\]

which is O(epsilon) uniformly over i. Formula (2), with its quadratic
remainder, then gives

\[
 L_{\rm new}-L
  =4\int_E[F_\omega(s)-F_\omega(w)]\,dP_1+O(\epsilon^2)
  \le-4\delta\epsilon+O(\epsilon^2)<0.
\tag{6}
\]

For small epsilon this contradicts local minimality. Thus w minimizes
F_omega almost surely. Since F_omega(0)=0, we have F_omega(w)<=0.
On the other hand, stationarity of the finite matrix block and (2) give

\[
 E_1F_\omega(w)=\sum_i\mu_i r_i d_i^TMa_i
                       =\tfrac12\langle\nabla_ML,M\rangle_F=0.
\tag{7}
\]

Hence F_omega(w)=0 almost surely. A globally minimized odd function
with minimum zero must be identically zero: it is nonnegative, and its
negative under s -> -s is also nonnegative. The input ridge independence
proved in section 2 implies mu_i r_i b_1^TM^Td_i=0 almost surely for
each i. Positive definiteness of the b_1 Gram proves the lemma.

## 5. Exclusion of every positive-loss local minimum with M nonzero

Suppose M is nonzero and some r_i is nonzero. Choose a vector q such
that z=Mq is nonzero. Apply (3) to v=v_i and this z, and let

\[
 J=(b_2^TMq)\phi'(b_2^Tv_i),\qquad k=J-\operatorname{Proj}_H J.
\tag{8}
\]

For every t, replacing c by c+t k while holding w,M fixed leaves every
prediction exactly unchanged, since E_2[kH_j]=0. If the original state
is a local minimum with an open ball of radius rho, each such perturbed
state with |t| ||k||_2<rho/2 is also a local minimum: its ball of radius
rho/2 is contained in the original ball and its loss is the same.

Apply the lemma from section 4 both before and after this perturbation.
The residual r_i is unchanged and nonzero, while

\[
 d_i(c+t k)=d_i(c)+t E_2[b_2k\phi'(b_2^Tv_i)].
\]

Subtracting the two conclusions, and taking any nonzero sufficiently
small t, gives M^T E_2[b_2k phi'(b_2^Tv_i)]=0. Pairing this vector
with q gives

\[
           0=E_2[kJ]=\|k\|_2^2>0,
\tag{9}
\]

a contradiction. Thus a local minimum with nonzero M has every r_i=0.

## 6. Exclusion when M=0

At M=0 every output is zero and L=L_0:=sum_i mu_i y_i^2, for every w,c.
If all labels vanish, this is already zero loss and cannot be a bad local
minimum. Otherwise L_0>0, and the following argument applies.
Let v_c=E_2[b_2c] and A_y(w)=sum_i mu_i y_i a_i(w). Formula (2) gives

\[
                         \nabla_ML=-2v_cA_y(w)^T.
\tag{10}
\]

Arbitrarily small odd readout changes can make v_c nonzero: add a small
multiple of a nonzero linear feature b_2^Tz and use the positive definite
upper Gram. Such changes keep the loss exactly L_0 at M=0.

Likewise A_y can be made nonzero by an arbitrarily small odd L2 change
of w. Here are details if initially A_y=0. Define the nonzero odd function
Q(s)=sum_i mu_i y_i phi(s dot u_i); its nonzero character follows from
input ridge independence. There are a rational s, a component j, and a
positive-measure subset B of Omega_+ where
b_{1,j}[Q(s)-Q(w)] has a fixed nonzero sign bounded away from zero,
and where w is bounded. Otherwise, countability and continuity would give
b_1[Q(s)-Q(w)]=0 for every s almost surely. The lower vector b_1 is
nonzero almost surely (its first forward coordinate is nonzero almost
surely), so Q would be a constant function, contradicting oddness and
nonzero Q. Reflecting the second half of the carrier as in section 4
justifies restriction to Omega_+.

Replace w on an arbitrarily small subset E of B and its negative by
s and -s. The j-th component of the resulting change of A_y is
2 integral_E b_{1,j}[Q(s)-Q(w)], which is nonzero. The L2 displacement
tends to zero with P(E), exactly as in section 4.

Thus every neighborhood of a state with M=0 contains a state with the
same loss L_0, M=0, and both v_c and A_y nonzero. For
N=v_cA_y^T, its loss derivative along M=tN at t=0 is
-2|v_c|^2|A_y|^2<0. Taking t>0 sufficiently small gives a strictly
smaller loss within the original neighborhood. No positive-loss M=0 state
is a local minimum. Together with section 5, this proves the theorem.

## 7. What the theorem does and does not establish

This excludes genuine bad local minima, including local minima with any
number of exactly flat directions, throughout the stated odd p=1 state
space for any finite nonparallel/nonantipodal input set. It is not limited
to three inputs, linearly independent data, equal weights, or w=c=0.
It uses both population freedom in the first layer and null directions
of the trained readout. The full middle matrix enters essentially in
(7)--(9); it is not replaced by an independent reverse action.

The proof does not assert that every bad stationary state has a negative
leading coefficient along a fixed straight line. The distinction in
(0) is a real logical obstruction to treating that as a restatement of
the theorem. Nor does absence of bad local minima alone exclude convergence
to saddles, wandering, or escape to infinity under GF or stochastic training.
No claim about basin probability or zero-loss convergence from (g,0,D)
is made here.

For completeness, zero-loss states do exist for the whole stated data
family. Choose r as in section 2, so t_i=r dot u_i are nonzero with
distinct squares. Let e=sign(G_1), let q select the first normalized
forward feature of b_1, and put A=E_1[b_1e]. Then
kappa=q^T A=E|tanh G_1|/sqrt(v+1/4096)>0, where v=E tanh^2 G_1 is
the canonical initialized variance. Set w=e r and M=e_1q^T. Its
effective vectors are z_i e_1, where z_i=kappa tanh(t_i) are nonzero
with distinct squares. For B=b_{2,1}, the functions psi_i=phi(z_iB)
have positive definite Gram K: a zero linear combination vanishes on
the support interval of B, and its first m odd coefficients give the
same invertible Vandermonde system as in section 2. The bounded odd
readout c=sum_i (K^{-1}y)_i psi_i gives f_j=y_j exactly. These zero-loss
states are global, and hence local, minima.

## 8. Arbitrary finite sphere data and the exact architectural floor

The input separation restriction can be removed if zero loss is replaced
by the exact attainable loss. Allow any finite inputs on sqrt(d) S^(d-1),
including duplicates and antipodal pairs, with the same positive weights
and arbitrary finite real labels. Group observations modulo input sign.
Choose a representative x_g for each group, write x_i=s_i x_g with
s_i in {-1,+1}, and define

\[
 p_g=\sum_{i\in g}\mu_i,\qquad
 \bar y_g=\frac{\sum_{i\in g}\mu_i s_i y_i}{p_g},\qquad
 C=\sum_g\sum_{i\in g}\mu_i(s_i y_i-\bar y_g)^2.
\tag{11}
\]

Every p_g is positive. Prediction is odd in input at every state: each
hidden tanh and the intermediate linear map preserve the sign change.
Expanding each group's square about its weighted signed-label average gives

\[
 L=C+\sum_g p_g(f(x_g)-\bar y_g)^2.                \tag{12}
\]

The cross term vanishes because sum_{i in g} mu_i(s_i y_i-ybar_g)=0.
The representatives are pairwise neither parallel nor antiparallel, so
the theorem applies to the last term, with its possibly nonbinary or
zero labels. Adding the state-independent constant C preserves local
minima exactly. Consequently every local minimum of the original loss
has L=C. The exact-fit construction in section 7 fits all representative
averages, so C is attained and is the global minimum.

Thus **every local minimum is global for arbitrary finite weighted sphere
data in the stated canonical odd population state space**. The floor C
is zero precisely when signed labels s_i y_i agree within each group.
Otherwise C is the unavoidable error of conflicting repeated/antipodal
observations. No convergence to C under any training algorithm is inferred.

### A limited but unconditional gradient-flow consequence

Let S_* be any equilibrium with L(S_*)>C. No neighborhood of S_* in
the physical topology is contained in its point basin for exact gradient
flow. Indeed, every such neighborhood contains S with L(S)<L(S_*),
by the theorem. Along exact physical gradient flow from this S,

\[
 L(S(t))\le L(S)<L(S_*).
\tag{13}
\]

Loss is continuous in the stated topology: bounded marks and the Lipschitz
activation make all finite moment contractions and predictions continuous.
Consequently convergence S(t)->S_* would contradict (13). For a global
solution its loss limit exists by monotonicity and the lower bound C, and
lies between C and L(S), strictly below L(S_*).

Thus a suboptimal equilibrium cannot attract every sufficiently nearby
state. This does not say that its basin has empty interior elsewhere or
zero measure, nor that canonical initialization avoids it. It supplies no
stochastic conclusion, since sampled updates need not decrease full loss.

## 9. Internal check and provenance

The candidate froze at SHA256
`702ef38dbb7c03c5d09979d7247f3c9eab1b35da30f98d9159bdf948b2cdedb4`.
An attempted fresh isolated review was blocked by the agent thread limit.
The separate origin-route author instead performed an explicitly informed
internal review of the complete frozen candidate and complete canonical
p=1/notation sources. Its report is `review_no_bad_local_minima.md`, SHA256
`9f1796c95b2fab5a80d74df046ec4312fe394f628dfa64cd856f6511629c453c`.
The central theorem passed with no mathematical corrections. The reviewer
requested the clarified straight-direction quantifier, a self-contained
proof of the secondary exact-fit assertion, and this accurate review-status
description. The lead read the complete review and inserted those changes;
the exact-fit paragraph above is the review's verified construction.
The reviewer then checked the explicitly proposed extension to real labels
and the complete signed-group reduction, in Supplement 1 of the same
report. That supplement preserves the original review prefix and passes
both extensions; its complete report SHA256 is
`9dd2903a6f658f101f322ac939ee4624f06e07800029ec56347a71304d3ebfc2`.
The lead read the full supplement and incorporated its verified argument
in sections 1, 6 and 8. No new dynamical claim was added.
The same reviewer subsequently verified the limited exact-GF consequence
in Supplement 2, preserving all earlier report bytes. The lead read this
complete supplement and inserted its argument after section 8. The full
supplemented report now has SHA256
`3751b9583c69b232f3f0910ceddc19eac6f1766505738b3d8782df59df8aeb33`.

A separate fresh independent route, given only canonical definitions and
the neutral problem, froze `general_bad_geometry_route.md` at SHA256
`7c88c617b0ace8bd59332fa0e124a4fb2c77cb5b88790b9410cb50f1aa877a37`
before comparison. It reaches the same local-minimum exclusion using a
different justification of the first-layer step. The lead read its complete
argument after both candidates froze. It is corroborating independent
derivation, not a dependency of this proof or an isolated review of it.

Status: internally checked for the no-suboptimal-local-minimum theorem,
including the arbitrary-real-label and architectural-floor extensions
and the exclusion of a full local point basin for suboptimal equilibria,
with informed-review provenance; not promoted. The later internal check
of `straight_line_geometry_attempt.md` disproves the universal fixed-line
descent claim, and this cross-reference supersedes the earlier open status
for that claim. Initialized stochastic convergence remains open. These
status and cross-reference edits do not change the landscape proof; its
last hash before those edits and the separate GF corollary was
`a535ba6f0aacbb35a946937dc6c3d4e5317d73a70f4682459e36b61917ef2f43`.
