# Dependent triples: negative directional curvature and a Hilbert regularity obstruction

Status: frozen scoped analytic candidate, 2026-09-18. No experiment or
external theorem is used. This file does not assert a basin-null extension.

Assigned scientific inputs, read completely: `docs/observable_p1.md`,
`plateau_finite_critical.md`, `basin_hilbert_landscape.md`, and
`architectural_loss_floor.md`. Required instructions read: the
solve-math-rigorously skill and the investigate-conjectures skill with its
research-contract and adversarial-audit references. No other study or
current-route report was read. The supervisor supplied two exploratory
followups: a linear-form sign argument for the lower critical equation,
and the symmetric pair-plus-zero geometry used in Section 4. The latter
geometry was also reached independently before reading that followup.
Neither supplied message included another route's conclusions. The
projective-gate lemma below was derived in this route before comparison.

## 1. Exact scope and conclusions

Use the exact canonical p=1 odd sector in dimension d, with bounded odd
features b_1 in R^(2d), b_2 in R^d, their prescribed correlated Gaussian
provenance, and the full middle matrix M in R^(d x 2d). The state is

\[
 (w-g,c,M)\in\mathcal H
 =L^2_{\rm odd}(P_1;\mathbb R^d)
   \times L^2_{\rm odd}(P_2)\times\mathbb R^{d\times2d}.
\]

There is no essential-bound requirement on w-g or c. Inputs u_i are unit,
pairwise distinct modulo sign, with positive weights p_i summing to one
and binary labels y_i. Write

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i=\tanh(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\]
\[
 \rho_i=p_i(f_i-y_i),\quad
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_i)].
\]

The physical metric is population L2 in the two fields and Frobenius in
M. Equilibrium means that all three exact gradient components vanish.

**Negative-direction theorem.** For at most three such inputs, every
equilibrium in H with 0<L<1 has a bounded odd state direction along which
the ordinary second derivative of L is strictly negative. This includes
dependent triples on a circle and triples spanning a two-dimensional
plane in any ambient dimension. It needs no bounded-displacement premise.

**Regularity obstruction.** For dependent triples there are exact H
equilibria with 0<L<1 at which L has no second Frechet differential in H.
Thus “strict saddle” in the negative-direction sense extends, while a
claim of an everywhere-defined Hilbert Hessian does not. In particular,
the independent-input proof's finite-rank Hessian and ensuing Hilbert
center-stable argument cannot simply be imported from its stated scope.

The plan is to prove a two-dimensional gate-ratio rigidity lemma, use it
to exclude the sole exceptional three-way collision in the directional
argument, and then construct the separate regularity obstruction.

## 2. Three projective directions determine the gate ratios

**Lemma.** Let u_1,u_2,u_3 be pairwise distinct modulo sign on the unit
circle of a two-dimensional Euclidean space V. For s,t in V, suppose

\[
 \operatorname{sech}^2(s\cdot u_i)
 =k\operatorname{sech}^2(t\cdot u_i),\qquad i=1,2,3,
 \qquad k>0.
 \tag{1}
\]

Then s=t or s=-t.

We first prove the elementary convexity fact needed when s,t are
independent. Fix K>1 and set

\[
 F(y)=\operatorname{arcosh}(K\cosh y)>|y|.
\]

It is an even smooth function, and differentiating cosh F=K cosh y gives

\[
 F'=\frac{\tanh y}{\tanh F},\qquad
 F''=\coth F\,[1-(F')^2]>0.
 \tag{2}
\]

We claim

\[
 F-yF'>\frac{y^2}{2}F''.
 \tag{3}
\]

It suffices to take y>=0. For a>b>=0 define

\[
 J(a,b)=a\tanh a-b\tanh b
 -\frac{b^2}{2}\left(1-\frac{\tanh^2b}{\tanh^2a}\right).
\]

For b>0, J(b,b)=0 and

\[
 \partial_aJ
 =\tanh a+a\operatorname{sech}^2a
 -\frac{b^2\tanh^2b\operatorname{sech}^2a}{\tanh^3a}
 \ge \tanh a+a\operatorname{sech}^2a
       -\frac{a^2\operatorname{sech}^2a}{\tanh a}>0.
\]

After multiplication by sinh(a)cosh(a), the last strict inequality is
sinh^2(a)+a tanh(a)-a^2>0, which follows from sinh(a)>=a and a>0.
For b=0, J(a,0)=a tanh(a)>0 directly. Substituting a=F(y), b=y and
dividing J>0 by tanh F proves (3), using (2).

For every positive-definite symmetric 2 by 2 matrix Q the function

\[
 q(y)=(F(y),y)Q(F(y),y)^T
\]

is strictly convex. Indeed q''=2 tr(QP), where

\[
 P=\begin{pmatrix}
 (F')^2+FF''&F'+yF''/2\\
 F'+yF''/2&1
 \end{pmatrix},\qquad
 \det P=F''(F-yF'-y^2F''/4)>0.
\]

Thus P is positive definite. Diagonalizing P expresses tr(QP) as a
positive sum of values of the positive quadratic form Q. Consequently
q''>0. A strictly convex real function takes a fixed value at no more
than two points: three such points would violate strict convexity at
the middle point.

Now suppose s,t are independent. Rewriting (1) gives
cosh(s.u_i)=K cosh(t.u_i) with K=k^(-1/2). If K=1, every u_i lies on
one of the lines (s-t).u=0 or (s+t).u=0. These provide at most two
directions modulo sign, a contradiction. If K differs from one, swap
s,t if necessary so that K>1. The invertible linear map

\[
 u\longmapsto(x,y)=(s\cdot u,t\cdot u)
\]

takes the unit circle to a centered ellipse (x,y)Q(x,y)^T=1 with Q
positive definite. Orient each u_i so that x_i>0; x_i cannot vanish
because cosh x_i=K cosh y_i>1. Then x_i=F(y_i). Distinct projective
directions give distinct y_i, because F fixes x_i and the linear map is
invertible. The three y_i would solve q(y)=1, contradicting strict
convexity.

It remains to treat dependent s,t. If exactly one is zero, the relation
requires the absolute projections of the other on all three u_i to be
equal. A nonzero linear functional has a fixed absolute value on at
most two projective directions of a circle. If s=alpha t and t!=0,
with |alpha|!=1, the function

\[
 r\longmapsto\frac{\cosh(|\alpha|r)}{\cosh r},\qquad r\ge0,
\]

is strictly monotone: its logarithmic derivative for r>0 is
|alpha|tanh(|alpha|r)-tanh r, strictly positive if |alpha|>1 and
strictly negative if |alpha|<1. Again (1) would give three equal
absolute projections, which is impossible. The remaining cases are
s=+/-t or both zero, proving the lemma.

The fact about absolute projections used here follows by intersecting
the circle with the two parallel lines s.u=+a and s.u=-a. There are at
most four points, forming at most two antipodal pairs; at a=0 there is
at most one pair.

## 3. Negative second variation at every nonfitting triple equilibrium

Partition the nonzero v_i into equality-modulo-sign groups, and put all
zero v_i in a further group Z. For a group J define

\[
 R_J(w)=\sum_{i\in J}\rho_i
       \operatorname{sech}^2(w\cdot u_i)u_i.
 \tag{4}
\]

First suppose some residual-bearing group satisfies
P_1(R_J(w)!=0)>0. Since M!=0 and the entire canonical b_1 law has a
density on an open full-dimensional set, P_1(Mb_1=0)=0. Thus for some
coordinate ell the bounded odd lower perturbation

\[
 h=(Mb_1)_\ell R_J(w)
\]

satisfies

\[
 \left[\sum_{i\in J}\rho_iM Da_i[h]\right]_\ell
 =E_1[(Mb_1)_\ell^2|R_J(w)|^2]>0.
 \tag{5}
\]

The perturbation is bounded because all gates and b_1 are bounded; it
is odd because gates are even and b_1 is odd. The differentiations
under expectation are valid by bounded activation derivatives and
bounded h.

Set z_G=sum_(i in G)rho_i M Da_i[h] for all groups. The residual-weighted
upper-feature derivative is

\[
 S(b_2)=b_2\cdot z_Z+
 \sum_{G\ne Z}(b_2\cdot z_G)
       \operatorname{sech}^2(b_2\cdot v_G).
 \tag{6}
\]

At least one z_G is nonzero by (5). Let E=span{H_i} in upper L2.
The upper derivative-feature separation argument in the assigned
plateau report shows S notin E. For completeness, an almost-sure
identity would be an analytic identity on the upper feature cube;
restrict to a generic line b=t e with the nonzero |e.v_G| distinct
and with a nonzero e.z_G. A linear term t(e.z_Z) first cannot equal a
bounded tanh sum. After its removal, eliminate rates in increasing
order in an identity between sums of t sech^2(a t) and tanh(a t):
subtract the limiting constant, multiply by exp(2a_min t), divide by
t to eliminate the derivative coefficient, then take the undivided
limit to eliminate the tanh coefficient. Removing that entire rate
and repeating gives every coefficient zero, a contradiction. This
finite induction also works for any finite number of groups.

Take the bounded odd readout perturbation k=S-P_E S. Then k!=0,
E_2[kH_i]=0, and E_2[kS]=||k||_2^2. Ordinary differentiation along
bounded directions gives

\[
 \left.\frac{d^2}{d\epsilon^2}
 L(w+\epsilon h,c+\epsilon s k,M)\right|_{\epsilon=0}
 =Q_h+4s\|k\|_2^2,
 \tag{7}
\]

where Q_h is finite. Integrability uses c in L2, hence c in L1,
bounded marks, and bounded variations and activation derivatives.
Choosing a finite sufficiently negative s proves negative curvature.
This is an ordinary directional second derivative; no Frechet Hessian
has been assumed in this argument.

For three pairwise nonparallel inputs, any residual-bearing group of
size one or two has R_J(w)!=0 at every finite w: the involved vectors
are independent and their nonzero residual coefficients are multiplied
by strictly positive gates. If the triple itself is independent the
same observation covers a group of size three. Consequently only a
dependent triple in one common effective group could fail (5).

At 0<L<1 we have M!=0 and at least one v_i!=0, because all zero v_i
give zero predictions and L=1. Thus the exceptional grouping would
have to satisfy v_i=sigma_i v, v!=0, for all three i. Let V be the
two-dimensional input span, and let s be the orthogonal projection
of w onto V. Suppose, towards contradiction, R_J(w)=0 almost surely.
The unique relation sum_i lambda_i u_i=0 has every lambda_i nonzero.
All rho_i must then be nonzero, since one or two nonzero coefficients
cannot give a relation. For almost every mark,

\[
 \rho_i\operatorname{sech}^2(s\cdot u_i)
 =a(\xi)\lambda_i,\qquad i=1,2,3.
\]

Fix one mark in this full-measure set, with projected value s_0. The
three gates at every other such mark are a common positive multiple
of those at s_0. Section 2 implies s=+/-s_0 almost surely. If s_0=0,
all a_i are zero, impossible. Otherwise there is a measurable sign
epsilon(xi) with s=epsilon(xi)s_0, and hence

\[
 a_i=t_i A,\qquad t_i=\tanh(s_0\cdot u_i),\qquad
 A=E_1[b_1\epsilon].
\]

Therefore v_i=t_i MA. Their common nonzero magnitude forces all
|t_i| equal and nonzero, so strict monotonicity of tanh forces all
|s_0.u_i| equal. Section 2's circle-intersection argument rules this
out for three distinct projective directions. This contradiction
completes the negative-direction theorem.

For any finite number of samples, (4)--(7) remain valid verbatim.
In particular it suffices that some residual-bearing group has
linearly independent residual-bearing inputs. Without an additional
argument, the circle rigidity proof does not handle a collision group
containing four or more inputs: its kernel of input relations need not
be one-dimensional. No unrestricted finite-sample H theorem is asserted.

## 4. A sub-loss-one H equilibrium without a Frechet Hessian

This construction works in dimension d>=2, using its first two input
coordinates. Fix C,S>0 with C^2+S^2=1, a>0, and inputs

\[
 u_1=(C,S),\qquad u_2=(C,-S),\qquad u_3=(0,1).
\]

Zero-pad in larger dimensions. Take labels (+1,-1,+1) and weights
p_i>0 summing to one, with p_1!=p_2. Define

\[
 F=\frac{p_1-p_2}{p_1+p_2},\qquad
 r=\frac{2p_1p_2}{p_1+p_2}>0.
\]

Choose any nonzero q in R^(2d), put B=q.b_1, and set

\[
 w=a\operatorname{sign}(B)e_1,\qquad
 A=E_1[b_1\operatorname{sign}(B)],\qquad M=e q^T,
\]

where e is the first upper coordinate vector. The exceptional event
B=0 has probability zero, and q.A=E|B|>0. Thus, with t=aC and
z=tanh(t)E|B|>0,

\[
 a_1=a_2=\tanh(t)A,\quad a_3=0,\qquad
 v_1=v_2=z e,\quad v_3=0.
\]

This is an admissible H state: w is bounded and odd, while w-g is in
L2. The displacement is not essentially bounded, since g is Gaussian
and w is bounded.

Let x=b_2.e and choose any D!=0. Define

\[
 D_0=-\frac{2rS\operatorname{sech}^2(t)}{p_3}D.
 \tag{8}
\]

There is a bounded odd readout c=c(x) satisfying the three moments

\[
 E[c\tanh(zx)]=F,\qquad
 E[cx\operatorname{sech}^2(zx)]=D,\qquad E[cx]=D_0.
 \tag{9}
\]

Indeed the three bounded odd functions tanh(zx), x sech^2(zx), and x
are linearly independent under the upper law. Any dependence holds
on its open interval by positive density and then on the whole real
line by analyticity. Its linear-growth term first has zero coefficient;
its nonzero tanh limit then has zero coefficient; finally the nonzero
x sech^2 term has zero coefficient. Their Gram is positive definite,
so the corresponding linear combination solves any prescribed three
moments. Canonical upper coordinates are independent and symmetric;
therefore all other components of d_1=d_2 and d_3 vanish, giving

\[
 d_1=d_2=D e,\qquad d_3=D_0 e.
\]

The predictions are (F,F,0) and residuals are (-r,r,-p_3). The readout
gradient cancels because H_1=H_2 and H_3=0. The middle gradient cancels
because d_1=d_2, a_1=a_2 and a_3=0. Finally the lower gradient is B
times the vector

\[
 D\operatorname{sech}^2(t)(-r u_1+r u_2)-p_3D_0u_3
 =[-2rSD\operatorname{sech}^2(t)-p_3D_0]e_2=0
\]

by (8). It is therefore an exact equilibrium, with

\[
 L=p_3+\frac{4p_1p_2}{p_1+p_2}
 =1-\frac{(p_1-p_2)^2}{p_1+p_2}\in(0,1).
 \tag{10}
\]

The individual rho_i M^T d_i are nonzero. Hence the independent-input
criticality implication does fail at sub-loss-one dependent H states.

To prove failure of second Frechet differentiability, perturb only the
e_2 component of w on small odd-paired mark sets. On a mark with B>0,
replace a e_1 by a e_1+h e_2. The residual-weighted first-order change
with respect to the effective upper vectors is governed by

\[
 T(h)=rD[\tanh(t-Sh)-\tanh(t+Sh)
           +2S\operatorname{sech}^2(t)\tanh h].
 \tag{11}
\]

This function is odd, T'(0)=T''(0)=0, and it is not identically zero:

\[
 \lim_{h\to+\infty}T(h)
 =2rD[S\operatorname{sech}^2(t)-1]\ne0.
\]

Choose one fixed finite h with T(h)!=0. Choose delta>0 such that
P_1(B>=delta)>0 and a sequence of measurable subsets E_n of this
event with probabilities m_n>0 tending to zero. Such sets exist
because the canonical mark space is nonatomic. Let -E_n be the image
under sign negation; it is disjoint from E_n. The bounded odd lower
increment h_n equals h e_2 on E_n, -h e_2 on -E_n and zero elsewhere.
Then ||h_n||_2^2=2m_n h^2 tends to zero.

The exact effective-vector increments have size O(m_n), since B and
the activations are bounded. Taylor expansion of the smooth
finite-dimensional map from (v_1,v_2,v_3) to loss, at fixed c, gives

\[
 L(w+h_n,c,M)-L(w,c,M)
 =4T(h)\int_{E_n}B\,dP_1+O(m_n^2).
 \tag{12}
\]

The factor four combines the unhalved square-loss derivative and the
two sign-paired mark sets. The O(m_n^2) constant is uniform in n.

If a second Frechet differential existed, its value on every fixed
bounded direction would equal the ordinary directional second
derivative. In the directions h_n, the residual contraction of the
second lower-feature derivative is zero because T''(0)=0; the remaining
second-variation terms are products of first effective-vector
increments, each O(m_n). Therefore the alleged Hessian would satisfy

\[
 D^2L[h_n,h_n]=O(m_n^2).
\]

The first differential vanishes at the equilibrium. But (12), divided
by ||h_n||_2^2, has absolute magnitude bounded away from zero after
subtracting half this quadratic term, since
integral_(E_n) B >=delta m_n. This contradicts the o(||h_n||_2^2)
remainder required for second Frechet differentiability.

There is no conflict with Section 3. The example has a zero effective
singleton with nonzero residual, so it has a negative bounded
directional second variation. Failure of a Frechet Hessian concerns
uniform approximation across concentrated directions, not existence
of individual directional derivatives.

## 5. Exact remaining boundary

The bounded-displacement premise can be removed from the three-input
negative-direction result. It cannot be removed from the existing
Hilbert basin argument solely by replacing independent-input dual
vectors with this geometric lemma: dependent H equilibria can lack
the Hessian regularity that the earlier proof uses.

The unrestricted finite-sample H negative-direction statement remains
open in this report. Its precise sufficient condition is (4), with
one nonzero residual-weighted group field on positive measure. The
bounded-displacement tail-separation argument in the assigned plateau
report proves that condition for any finite distinct-modulo-sign
sample set. The present circle proof establishes it for triples at
sub-loss-one equilibria without that displacement restriction.

No claim is made about exclusion of a canonical deterministic initial
condition from a basin, universal trajectory convergence, finite
accumulation, or positive-loss escape. An H basin-null extension needs
a separate argument that handles the demonstrated lack of a second
Frechet differential, or an explicitly stronger endpoint topology or
regularity assumption. That is a substantive proof obligation, not an
unverified application of the earlier spectral construction.

## 6. Generic circle triples recover the Hilbert regularity mechanism

Post-primary-freeze extension, following the supervisor's explicit
geometric-cancellation prompt. Sections 1--5 remain unchanged. This
section proves the missing cancellation condition; it does not itself
reprove the separate basin-null construction.

Assume the triple is dependent and pairwise distinct modulo sign. Put

\[
 T_i=\rho_i M^Td_i\in\mathbb R^{2d}.
\]

**Cancellation theorem.** If an H equilibrium with 0<L<1 has some
T_i!=0, then there is a permutation (i,j,k) such that all of the
following hold:

1. The directions obey |u_i.u_k|=|u_j.u_k|.
2. With n either unit direction in the input plane perpendicular to
   u_k and sigma=sign[(u_i.n)(u_j.n)], their oriented labels conflict:
   y_i=-sigma y_j.
3. Their weights are unequal: p_i!=p_j.
4. The effective features form precisely a nonzero signed pair and a
   zero singleton: v_j=sigma v_i!=0 and v_k=0. The loss is

\[
 L=p_k+\frac{4p_ip_j}{p_i+p_j}
   =1-\frac{(p_i-p_j)^2}{p_i+p_j}.
 \tag{13}
\]

The projections in condition 2 are nonzero because neither u_i nor u_j
is parallel to u_k. The sign sigma is unchanged when n is replaced by
-n, so the condition is intrinsic.

To prove this, let sum_i lambda_i u_i=0 be the unique input relation;
all lambda_i are nonzero. The lower equilibrium equation says

\[
 \operatorname{sech}^2(w\cdot u_i)
        \left(b_1\cdot\frac{T_i}{\lambda_i}\right)
 \quad\hbox{is independent of }i\quad\hbox{almost surely}.
 \tag{14}
\]

If one T_i vanishes, positivity of every gate implies all the other
linear forms in (14) vanish almost surely. Positive definiteness of
the lower feature Gram then makes all T_i zero. Under the premise,
therefore, every T_i is nonzero and every rho_i is nonzero.

Because the gates are strictly positive, any two linear forms
b_1.(T_i/lambda_i) and b_1.(T_j/lambda_j) have the same sign almost
surely. The full lower feature law has a positive density on an open
neighborhood of zero. Two nonzero real linear forms whose product is
nonnegative on such a neighborhood must be positively proportional.
If they are independent, their joint linear map is onto R2 and a
small vector can be chosen with opposite nonzero values, persisting
on an open set. If they are negatively proportional, their product
is strictly negative off their common hyperplane. Both alternatives
contradict nonnegativity. Thus

\[
 \frac{T_i}{\lambda_i}=\kappa_i q,
 \qquad q\ne0,\quad\kappa_i>0.
\]

The density also gives P_1(b_1.q=0)=0. Cancelling b_1.q from (14)
therefore shows the three gates have fixed ratios. Section 2 implies
that the projection of w to the input plane is almost surely +/-s_0.
As in Section 3,

\[
 a_i=t_i A,\quad v_i=t_i V,\qquad
 t_i=\tanh(s_0\cdot u_i),\quad V=MA.
 \tag{15}
\]

Here s_0 and V are nonzero, since otherwise all predictions vanish and
L=1. The upper tanh features for distinct nonzero |t_i| are linearly
independent: restrict an analytic identity to a generic upper line
and eliminate successive exponential rates as in Section 3. The
readout equilibrium equation sum_i rho_i H_i=0 thus rules out any
nonzero effective-feature singleton, since every rho_i is nonzero.

A three-way common nonzero magnitude is impossible by the circle
intersection argument in Section 2. The only remaining grouping of
three indices is a nonzero signed pair {i,j} and a zero singleton k.
Consequently s_0.u_k=0 and |s_0.u_i|=|s_0.u_j|>0. Taking n=s_0/|s_0|
gives sigma=sign[(u_i.n)(u_j.n)] and v_j=sigma v_i. The unit-norm
identities

\[
 (u_i\cdot n)^2=1-(u_i\cdot u_k)^2,
 \qquad (u_j\cdot n)^2=1-(u_j\cdot u_k)^2
\]

prove condition 1.

Write f_i=F and f_j=sigma F. The readout equation gives

\[
 F=\frac{p_i y_i+p_j\sigma y_j}{p_i+p_j}.
\]

If y_i=sigma y_j, then both residuals vanish, contradicting
rho_i,rho_j!=0. Thus y_i=-sigma y_j and
F=y_i(p_i-p_j)/(p_i+p_j). The zero singleton has prediction zero;
substitution into the loss gives (13). Loss below one requires
p_i!=p_j. This proves all four conditions.

**Data criterion.** It is therefore sufficient for individual
cancellation T_i=0 at every equilibrium with 0<L<1 that there be no
permutation (i,j,k) satisfying conditions 1--3. In particular, either
of the following is sufficient:

* For each k the other two directions have unequal absolute inner
  products with u_k. This is the asymmetric circle-triple condition.
* All three active weights are equal, with arbitrary allowed circle
  geometry and binary labels.

For a reflected pair satisfying condition 1, either equal pair weights
or consistent oriented pair labels prevents that pair from being the
exception. The criterion is sharper than imposing asymmetry alone.
Conversely, this theorem does not claim every violation produces a
bad equilibrium for every canonical dimension; Section 4 gives an
explicit family showing that violations can matter.

For precision, the promised local regularity follows directly from
T_i=0. Let theta_* denote such an equilibrium. Each finite-dimensional
map theta -> a_i is C^(1,1) locally in H: its derivative is the
expectation pairing with bounded b_1 phi'(w.u_i)u_i, and the change
of that derivative in operator norm is bounded by C||delta w||_2,
using bounded phi'' and Cauchy--Schwarz. The maps rho_i,d_i and hence
T_i are locally C^(1,1), because the upper arguments depend only on
the finite-dimensional a_i and M, upper marks are bounded, and all
dependence on c is through bounded L2 pairings.

The lower gradient is

\[
 \nabla_w L(\theta)
 =2\sum_i\phi'(w\cdot u_i)(b_1\cdot T_i(\theta))u_i.
\]

Since T_i(theta_*)=0, its Frechet derivative there is

\[
 h\longmapsto
 2\sum_i\phi'(w_*\cdot u_i)
        (b_1\cdot DT_i(\theta_*)[h])u_i.
 \tag{16}
\]

The omitted terms are o(||h||_H): the gate difference is O(||h_w||_2)
in L2 and T_i(theta_*+h)=O(||h||_H), while the finite coefficient
Taylor remainder is o(||h||_H). The other gradient components are
locally C^(1,1) maps through finite-dimensional coefficients and smooth
upper feature functions. Their derivatives at theta_* have finite
rank, as does (16). The resulting Hilbert Hessian is self-adjoint:
ordinary mixed derivatives agree on bounded directions, a dense
subspace of H, and the derived bounded operator extends that identity
by continuity. Its range consists of bounded odd fields together with
the finite matrix block. Section 3 supplies a negative quadratic value,
so finite-dimensional diagonalization on this range gives a negative
eigenvalue and a bounded eigenvector.

There is also the small-Lipschitz-remainder estimate needed in the
assigned local spectral argument. On an H ball of radius R around
theta_*, subtracting the linear derivative (16) from the lower
gradient yields a remainder with Lipschitz constant O(R). To see this,
write the remainder as the sum of

\[
 [\phi'(w.u_i)-\phi'(w_*.u_i)](b_1\cdot T_i(\theta))u_i
\]

and the base gate multiplied by
T_i(theta)-DT_i(theta_*)[theta-theta_*]. Gate differences are Lipschitz
from L2 to L2, their norms are O(R), the finite coefficients are
Lipschitz with norms O(R), and the last finite-coefficient remainder
has Lipschitz constant O(R) by C^(1,1). The upper and matrix remainder
estimates follow from their local C^(1,1) property. Constants may
depend on the equilibrium, but tend to zero with R as required.

Thus the sharp data criterion restores the individual cancellation,
finite-rank self-adjoint linearization, bounded nonzero eigenvectors,
and local small-Lipschitz remainder at every sub-loss-one H equilibrium.
It removes the new geometric/regularity obstruction to reusing the
earlier basin proof on this class. The complete basin theorem still
has the earlier proof's separate flow and probability hypotheses;
they are not newly verified or strengthened by this scoped report.
