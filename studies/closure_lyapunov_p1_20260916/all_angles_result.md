# Extension result: every separation, with the remaining orientation gap explicit

2026-09-16. This is the current result of the user-requested continuation.
It supersedes the earlier near-antipodal restriction for the symmetric
family, but does not claim arbitrary-orientation unit-label convergence.
Nothing is promoted to established docs/ or code/.

## Exact scope

Keep the exact canonical p=1 population closure, its full correlated
Gaussian marks, eta=1/4096 Cholesky normalization, prescribed initial
(w,c,M)=(g,0,D), actual transpose M^T, and unhalved equally weighted square
loss in physical time. All canonical row, readout and middle equations
remain active. Constants below are exact initialized Gaussian integrals.

Three distinct statements are now proved:

1. **Unit labels at every separation:** for
   u_+=(a,b), u_-=(a,-b), a>=0,b>0,a^2+b^2=1,
   and labels +/-A for ANY fixed A>0, the full closure fits and converges.
   Its angular separation 2 arccos(a) ranges over all of (0,pi].
   The four coordinate/diagonal reflections give further exact families: pairs
   u,v related by diag(1,-1), diag(-1,1), coordinate swap, or negative
   coordinate swap are covered when distinct. These are actual symmetries
   of the fixed dictionary; arbitrary rotations are not assumed.
2. **Antipodes at every orientation:** for ANY u in S1, the pair u,-u
   with labels +/-A and ANY A>0 has the same full-state convergence.
3. **Arbitrary orientation with small labels:** for ANY u,v in S1 with
   v!=u,-u, convergence holds whenever the label norm satisfies the
   explicit geometry-dependent threshold in Section 6 below.

Physical inputs in every case are x=sqrt(2)u. The theorem sought for
arbitrary oriented distinct pairs with labels +/-1 is not completely proved.
The distinction between separation angle and orientation matters for the
fixed finite dictionary. Coincident contradictory labels are impossible.

## 1. The new geometric potential

On either family 1 or 2 define from the current state

U=(H^2(u_+)-H^2(u_-))/2,
F=(f(u_+)-f(u_-))/2=<c,U>,
C=E_2 U^2, q=E_2 c^2,
C_0=E_2 U_0^2.

The proved symmetries preserve f(u_-)=-f(u_+), so L=(A-F)^2.
The all-angle initialization results below give C_0>0 for every admitted
pair. This rate can depend on geometry and is not claimed bounded away
from zero as opposite-label inputs approach coincidence.

A natural new current-state functional is

P(S)=q(S)/F(S)^2  (F>0).

Its reciprocal square root F/||c|| is the signed prediction per unit
readout norm. Its monotonicity prevents the hidden contrast from collapsing.
The initial state has q=F=0, so the proof explicitly uses its initialized
one-sided limit P(0+)=1/C_0 rather than asserting an ambient continuous
extension. A globally defined positive version, with the same fixed C_0, is

Phi(S)=(1+q(S))/(C_0+F(S)^2).

The proof below shows that BOTH are nonincreasing on the initialized
trajectory. They need not tend to zero. These are additional geometric
potentials; the ordinary loss supplies the fitting error and rate.

## 2. Complete normalized-readout argument

Write h=(w,M) and use the fixed physical product metric
||delta X||^2=E_1|delta w|^2+||delta M||_F^2+E_2|delta c|^2.
The exact physical equation on the invariant trajectory is

X_dot=2(A-F) grad F.

Consider the autonomous gradient curve X_s=grad F from the same initialized
state. This is a proof coordinate, not an additional operational state or
future-dependent forcing. Since F=<c,U(h)>, its readout component is
c_s=U. The other components are exactly

M_s=(d_+ a_+^T-d_- a_-^T)/2,
w_s=(phi'(w·u_+)q_+u_+-phi'(w·u_-)q_-u_-)/2,

with the same canonical a,d,q and actual M transpose as in the source.
The normalized dictionaries are contractions. Thus, on every finite s
interval,

||c||infty<=s,
||M||op<=2+s^2/2,
||w-g||infty<=B_1(s^2+s^4/8),

where B_1 is a fixed supremum envelope for the lower marks. Indeed the
three speeds are bounded respectively by 1, s and B_1(2+s^2/2)s.
These bounds lie in the actual characteristic local-existence spaces;
integrating gives Cauchy endpoints and continuation at any finite s.
This argument precedes all fitting or noncollapse claims.

Let
K=||grad F||^2=C+||grad_h F||^2.
Linearity in c gives exactly F_s=K and q_s=2F.
At initialization c=0, so grad_h F=0 and

c(s)=s U_0+o(s), F(s)=s C_0+o(s), q(s)=s^2 C_0+o(s^2).

Therefore F>0 for small positive s; F_s>=0 keeps F positive thereafter,
and F=<c,U> then ensures q>0. Cauchy-Schwarz gives F^2<=qC<=qK.
For every positive s,

P_s=-2(qK-F^2)/F^3<=0,
lim_(s downarrow0)P(s)=1/C_0.

Apply the inequality on [r,s] and let r decrease to zero to justify use
of that singular limit. It follows that

q<=F^2/C_0,  C>=F^2/q>=C_0,  K>=C_0.                 (1)

The reason for monotonicity has an exact geometric decomposition:

qK-F^2=(qC-F^2)+q||grad_h F||^2.                       (2)

The first term is the Cauchy-Schwarz deficit between the readout and the
current hidden contrast. The second is hidden-gradient activity. Both use
the present full state, not a past trajectory or supplied endpoint.

The nonsingular potential also has its FULL derivative included:

Phi_s=-2F[(qK-F^2)+(K-C_0)]/(C_0+F^2)^2<=0.           (3)

No evolving metric term has been omitted. Formula (3) uses (1); it is a
corollary of the normalized-margin argument, not an independent proof of it.
It is well-defined at initialization, with Phi(0)=1/C_0 and Phi_s(0)=0.

## 3. Fitting, rate and complete-state limit

Equation (1) gives F(s)>=C_0 s, so there is one and only one
s_* in (0,A/C_0] such that F(s_*)=A. On [0,s_*], K is continuous and
bounded. The physical clock s_dot=2(A-F), s(0)=0, has positive residual

e(t)=A-F(s(t))=A exp(-2int_0^t K(s(v))dv)>0

at finite t, approaches zero, and has s(t) increasing to s_*.
Substituting the clock into the three displayed gradient components
recovers the canonical physical equations. Uniqueness identifies the
composed curve with their prescribed initialized solution.

For every t>=0,

L(t)<=A^2 exp(-4 C_0 t),
C(S_t)>=C_0,
||c_t||^2<=A^2/C_0,
int_t^infty ||X_dot||physical dt<=sqrt(L(t)/C_0).        (4)

For the last inequality, ||X_dot||=2e sqrt(K) and -e_dot=2eK,
so ||X_dot||<=-e_dot/sqrt(C_0); integrate.
This is finite physical length, not merely finite dissipated energy.
The state converges in the complete physical Hilbert metric, and finite
feature-time continuity identifies its limit as X(s_*). The bounds in the
stronger characteristic spaces also yield uniform convergence of w-g and c
and Frobenius convergence of M. Coupling the complete frozen marks identically
gives W2 convergence of Gamma_1=Law(b_1,g,w) and Gamma_2=Law(b_2,c).
The limit fits both labels. Neutral fitting directions remain possible.

Along physical time the potential derivative is

Phi_dot=-4(A-F)F[(qK-F^2)+(K-C_0)]/(C_0+F^2)^2<=0,

and P_dot=-4(A-F)(qK-F^2)/F^3<=0 for t>0.
The fixed physical metric has not changed or collapsed.

## 4. Initialization and symmetry at all angles

The proof of exact initialization is retained completely in
[all_angles_cone_attempt.md](all_angles_cone_attempt.md), Sections 1–2,
and in the stronger map calculation
[arbitrary_pair_local.md](arbitrary_pair_local.md), Sections 1–4.
These use the exact canonical ridge and reverse Gaussian response term.
Here are the ingredients and their provenance, not an assumed rank condition.

At p=1 the lower raw list is
(1,tanh g_1,tanh g_2,tanh p_1,tanh p_2),
p_i=zeta_i+alpha tanh g_i, with g_i iid N(0,1),
zeta_i iid N(0,tau) independent of g,
v=E tanh^2G, tau=E tanh^2(sqrt(v)G), alpha=1-tau.
The separate upper raw list is (1,tanh xi_1,tanh xi_2), xi_i iid N(0,v).
The canonical Cholesky and contraction give zero constant blocks and two
identical active rows. For one lower coordinate, put X=tanh g,Y=tanh p,
r=E[XY], sigma=E[Y^2], chi=E sech^2p. Its raw effective coefficients are

(a_r,b_r)=(alpha v, alpha r+tau chi)
             [[v+eta,r],[r,sigma+eta]]^(-1).

The scalar coefficients a_r,b_r are fixed initialization quantities.
The tau*chi term is required by the actual reverse response. Conditional on g, the effective
lower scalar is proportional to

j(g)=a_r tanh g+b_r E_zeta tanh(zeta+alpha tanh g).

The first retained proof gives j(g)>0 for g>0, with an explicit positive
multiple of tanh g; its oddness gives the opposite sign for g<0.
In particular, for u_+=(a,b), b>0, the initialized antisymmetric upper
coefficient is a positive multiple of

E[j(g_2) tanh(a g_1+b g_2)]>0.

To see the strict sign after that lemma, average over g_1: the resulting
function of g_2 is odd and strictly increasing for b>0, and hence has the
same sign as j(g_2). The integral is strictly positive. Thus the initial
contrast between tanh(beta_1 B_1+beta_2 B_2) and
 tanh(beta_1 B_1-beta_2 B_2) is nonzero almost surely off beta_2=0.
This proves C_0>0 at every distinct reflection separation.

Reflection of the second lower mark pair and the second upper mark sends
normalized columns to diagonal sign transformations J_1,J_2, with
D=J_2 D J_1. The isometry

(w,c,M) -> (R w∘S_1,-c∘S_2,J_2 M J_1), R=diag(1,-1),

fixes initialization and transforms f(u) to -f(Ru). The loss and F are
invariant. Uniqueness therefore preserves its fixed-point space, proving
f(u_-)=-f(u_+) for EVERY a>=0,b>0, not only near a=0.
This is exactly the actual p=1 reflection symmetry.

The diagonal reflections require checking the normalization rather than
assuming the raw coordinate swap remains the same swap after whitening.
For any of the four signed-permutation input reflections P, let Q_l be its
raw feature permutation, and L_l the canonical Cholesky factor. Then
O_l=L_l^{-1}Q_l L_l is an orthogonal involution because Q_l preserves
G_l+eta I. The normalized features obey b_l∘S_l=O_l b_l, and the initialized
contraction satisfies D=O_2 D O_1^T. Thus
(w,c,M)->(P w∘S_1,-c∘S_2,O_2 M O_1^T)
is a metric isometry fixing initialization and sending f(u) to -f(Pu).
The same uniqueness argument proves the scalar residual reduction for a
pair u,Pu. Initial C_0>0 follows from the strictly injective initialized
coefficient map whenever the inputs are distinct. Complete details and the
limitations of the symmetry argument are in antipodal_upgrade_check.md.

For antipodes in arbitrary orientation, oddness of the bias-free network
already gives H(-u)=-H(u) and f(-u)=-f(u) at every state, without a dictionary
rotation or population reflection. The initialized map has the exact form

H_0(u)=tanh(Z_1 varphi(u_1)+Z_2 varphi(u_2)),

where Z_i=tanh xi_i and varphi is odd and strictly increasing, as proved
in arbitrary_pair_local.md. Since u is nonzero, its coefficient vector is
nonzero; the positive upper density makes E H_0(u)^2>0. Thus C_0>0, and
the scalar theorem applies at ANY orientation and ANY A>0.

## 5. Strict learned hidden contrast

For reflection pairs, scale only the initialized second active matrix row,
holding w and the first row fixed. If z_±=beta_1 B_1±beta_2 B_2 and
B_2>0, the derivative of C in this coefficient direction is

E[U beta_2 B_2(sech^2 z_++sech^2 z_-)]>0.

Every nonzero integrand is positive. Thus grad_h C(h_0)!=0. For a general one of the four reflections, use
its upper coefficient involution O_2 and the orthogonal projection
P_-=(I-O_2)/2. At initialization z_-=b_2^T O_2 M a_+, so the allowed
variation delta M=P_- M gives delta z_+=(z_+-z_-)/2 and the negative
variation for z_-. It follows that

delta C=E[U ((z_+-z_-)/2)(phi'(z_+)+phi'(z_-))]>0,

because C_0>0, tanh is strictly increasing, and both gates are positive.
This also proves nonzero hidden gradient for the diagonal cases without
assuming rotated marks are independent. For arbitrary-orientation
antipodes, scale all of M instead. Then U=H_0(u), z=z_0(u),
and the derivative is 2E[tanh(z) z sech^2 z]>0, because z is nonzero with
positive probability. Again grad_h C(h_0)!=0.

Since h_s=DU(h)^*c and c=sU_0+o(s), continuity of the finite contraction
and bounded-gate derivatives gives

h_s(s)=(s/2)grad_h C(h_0)+o(s).

Hence hidden-gradient activity is strictly positive on a short positive
s interval. Equation (2) then gives P_s<0 there and P_s<=0 subsequently.
At the fitting endpoint,

P(S_infty)<1/C_0, and therefore C(S_infty)>=1/P(S_infty)>C_0.

Thus the actual upper population separation increases strictly between
initialization and the learned state for both unit-label families above.
We assert neither monotonicity of C at every intermediate time nor a positive
gap uniform as the inputs coalesce. The detailed reflection calculation is
[scalar_strict_gain.md](scalar_strict_gain.md); the antipodal scaling argument
above supplies the same nonzero-gradient premise directly.

## 6. The arbitrary-orientation small-label theorem

For ANY distinct non-antipodal u,v, the initialized fields H_0(u),H_0(v)
are linearly independent. The exact coefficient map varphi is strictly
increasing and odd, so their two coefficient vectors can be collinear only
at u=v or u=-v. A linear dependence of the hidden fields would, by positive
upper density and continuity, hold on the entire open mark square; its
derivative at the origin would contradict that coefficient independence.
The complete elementary proof, including varphi'>0, is in arbitrary_pair_local.md.

Let lambda(u,v)>0 be the least eigenvalue of

G_0(u,v)=1/2 [[E H_0(u)^2, E H_0(u)H_0(v)],
             [E H_0(u)H_0(v), E H_0(v)^2]].

For opposite labels +/-A with 0<A<=lambda(u,v)/(8 sqrt(5)), the exact full
closure satisfies

L(t)<=A^2 exp(-lambda(u,v)t),
int_t^infty ||X_dot||physical ds
 <=2A/sqrt(lambda(u,v)) exp(-lambda(u,v)t/2).

This uses an explicit first-exit argument keeping the evolving readout Gram
positive, not an assumption that initialized rank persists. The full state
converges, with a codimension-two local fitting manifold and neutral tangent
directions. This result allows arbitrary orientation but has a genuine
small-label hypothesis; it is not a proof for labels +/-1.

## 7. The precise remaining arbitrary-orientation gap

For a general pair put G=(f(u_+)+f(u_-))/2. The exact loss is

L=(A-F)^2+G^2,
X_dot=2(A-F)grad F-2G grad G.

The second term need not vanish without a preserved data/dictionary symmetry.
Initial G=0 alone does not prove that it remains zero. In fact

G_dot(0)=A/2 (E H_0(u_+)^2-E H_0(u_-)^2).

The normalized-readout proof describes the first gradient direction; the
extra common-output term obstructs applying its sign argument unchanged.
A sufficient next estimate would control both residual directions along
unit-label training, for example a positive lower bound on the tangent Gram
in the actual residual direction together with enough control for finite
physical length. Initial Gram positivity, now proved for every nondegenerate
pair, supplies the starting point but is not that all-time estimate.

The old lower cross-sign estimate is NO LONGER a missing assumption for
reflection-pair convergence. It remains open as a separate possible account
of individual hidden coefficients. Its failure would not contradict the
new theorem. The original near-antipodal proof remains valid but is
superseded in scope and simplicity by the present normalized-readout argument.

All results are analytic; no numerical diagnostic was needed. No broader
neural-network convergence, closure-order accuracy, or generalization claim
is asserted. Full generic-orientation convergence at unit labels remains open.
