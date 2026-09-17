# An unconditional open family of nonsymmetric three-input problems

2026-09-16. Author candidate; internal research only. No numerical evidence.
This continues the exact d=3 p=1 result of `three_coordinate_candidate.md`.
It does not identify the d=3 dictionary with the original d=2 circle dictionary.

## 1. Result and its scope

Use the exact canonical general-dimensional p=1 initialization in dimension
three, with eta=1/4096, unhalved equal-probability square loss, and physical
L2/L2/Frobenius gradient metric. All of w,c,M evolve. The complete correlated
lower marks and the actual M transpose are retained.

For a positive number e define

    v_i(e) = (1 + e e_i)/sqrt(3+2e+e^2),   i=1,2,3,

where 1=(1,1,1) and e_i are the coordinate unit vectors. There exists e_0>0
such that for every 0<e<e_0 there are delta(e)>0 and k(e)>0 with the following
property. Let y=(1,1,-1) and choose ANY unit directions u_i satisfying

    max_i |y_i u_i-v_i(e)| < delta(e).

The actual physical inputs are x_i=sqrt(3)u_i. The directions may have three
unequal pairwise angles and need have no permutation or reflection symmetry.
The initialized canonical population closure satisfies, for every t>=0,

    K(S_t) >= k(e) I_3,
    L(t) <= exp(-4 k(e)t) L(0) = exp(-4 k(e)t),

where K_ij=<grad f(u_i),grad f(u_j)>/3 in the physical metric. In addition,
the same mixed potential used in the symmetric theorem extends to this open
family (after reducing delta if necessary):

    U=(H(u_1)+H(u_2)-H(u_3))/3, F=E2[c U], q=E2[c^2],
    C_0=E2[U_0^2]>0,
    Phi(S)=L(S) [1+C_0 (1+q)/(C_0+F^2)].

There is lambda(e)>0, uniform on the stated neighborhood, such that

    Phi_dot <= -lambda(e) Phi,   L<=Phi,   Phi(0)=2.

The new content is proved all-time full tangent coercivity and persistence
of the mixed potential's strict decay without the angular symmetry, not the
already known loss-dissipation identity. Loss itself also has the stronger
displayed exponential estimate. Moreover,

    integral_t^infinity ||X_dot|| <= sqrt(L(t)/k(e)),

so the complete population state converges strongly to a fitting state.
The initialized coupling gives convergence of both complete joint laws in W2.

The admitted set is open in (S^2)^3 and contains nondegenerate triples with
no angular equality. Its radii and rate are geometry dependent. This theorem
removes the equal-angle constraint locally; it does NOT cover arbitrary
three-input geometry or the generic d=2 circle problem. The radius is proved
positive by analytic inequalities, without a numerical lower bound.

The proof first finds a family of symmetric seeds whose full tangent Gram
stays nonsingular. It then proves all-time stability around each seed using
finite-time dependence followed by a finite-length trapping argument. The
potential contains neither a reference endpoint nor the future trajectory.

## 2. Exact model and admissible established inputs

The frozen populations, normalized features b_1,b_2 and initial matrix D are
exactly equations (6)--(7) of `three_coordinate_candidate.md`. Equivalently,
take independent lower pairs G_j~N(0,1), zeta_j~N(0,tau) and upper
Xi_j~N(0,v), and set

    h_j=tanh G_j, k_j=tanh(zeta_j+alpha h_j), Z_j=tanh Xi_j,
    v=E tanh^2 G, tau=E tanh^2(sqrt(v)G), alpha=1-tau,
    beta=E h_j k_j, sigma=E k_j^2, gamma=1-sigma,
    Rh=sqrt(v+eta), Rk=sqrt(sigma+eta-beta^2/(v+eta)),
    RZ=sqrt(tau+eta),
    b1=(1/sqrt(1+eta), h/Rh, (k-beta*h/(v+eta))/Rk),
    b2=(1/sqrt(1+eta), Z/RZ).

The only nonzero initialized matrix entries are

    D[Z_j,h_j]=alpha*v/(Rh*RZ),
    D[Z_j,k_j]=(alpha*beta*eta/(v+eta)+tau*gamma)/(Rk*RZ).

Initially w=G and c=0. In particular the reverse-response term and all joint
correlations are present. The feature maps z -> b_l^T z and their adjoints
are contractions in their Euclidean/L2 norms; b_l are bounded.

For a unit direction u the current canonical fields are

    h1(u)=tanh(w.u), a(u)=E1[b1 h1(u)],
    z2(u)=b2^T M a(u), H(u)=tanh z2(u),
    d(u)=E2[b2 c sech^2 z2(u)], Q(u)=b1^T M^T d(u),
    f(u)=E2[c H(u)].

In the Hilbert metric ||delta X||^2=E1|delta w|^2+E2|delta c|^2+
||delta M||F^2, the three gradient blocks are exactly

    grad_w f(u)=sech^2(w.u)Q(u)u,
    grad_M f(u)=d(u)a(u)^T, grad_c f(u)=H(u).

Thus X_dot=-(2/3)sum_i r_i grad f(u_i), r_i=f(u_i)-y_i. Label absorption
is exact: f(-u)=-f(u). We may equivalently work with v_i=y_i u_i and labels
all +1; the full tangent Gram changes only by diagonal sign conjugation.

The following prior proved facts are used, all from the complete candidate
and its independent audit: finite physical and auxiliary time existence;
coordinate-permutation equivariance of the NORMALIZED dictionary; strict
increase and oddness of the initialized scalar map kappa in (24)--(30);
initialized rank three for a!=b; and the scalar symmetric theorem in section 6.
In particular, along X_s=grad F, F=(1/3)sum_i f(v_i), for the permutation
family including its coincident limit,

    F_s=||grad F||^2 >= C_0>0,
    C_0=E2[(sum_i H_0(v_i)/3)^2].

The finite fitting time s_*<=1/C_0 is a proof device. Physical time is the
same auxiliary curve with ds/dt=2(1-F), and its image lies in 0<=s<s_*.
The scalar argument also applies to coincident compatible directions: it
requires C_0>0, not independence of the three features.

## 3. Continuity in the data on bounded auxiliary intervals

Work in the Hilbert space of (w-G,c,M), leaving the fixed G in each field.
On a ball ||w-G||2+||c||2+||M||F<=R, all the displayed gradient maps are
locally Lipschitz in the state and uniformly Lipschitz in unit input directions.
Here are the estimates establishing this point, including the Gaussian tail.

For two states and directions, with a tilde denoting the second,

    ||tanh(w.u)-tanh(w_tilde.u_tilde)||2
       <= ||w-w_tilde||2 + ||w_tilde||2 |u-u_tilde|.

The same bound with factor 2 holds for the first gate. Contracting against
b1 bounds a-a_tilde by this expression. Next,

    ||z2-z2_tilde||infinity
       <= B2 (||M-M_tilde||op + ||M_tilde||op |a-a_tilde|),
    |d-d_tilde| <= ||c-c_tilde||2
                 +2 B2 ||c_tilde||2 ||z2-z2_tilde||2,
    ||Q-Q_tilde||infinity
       <= B1 (||M-M_tilde||op |d|+||M_tilde||op |d-d_tilde|).

Here B_l=ess sup|b_l|; using a larger harmless constant in the d bound also
follows directly from bounded b2. Together with |a|<=1 and |d|<=||c||2,
these estimates bound every gradient difference and prediction difference
by a constant depending only on R,B1,B2 and ||G||2=sqrt(3), times state/input
distance. They also prove continuity and local Lipschitz bounds for K.
No L-infinity continuity in input direction is claimed or used.

Auxiliary solutions obey, uniformly over all the data here,

    ||c(s)||infinity<=s, ||M(s)||op<=||D||op+s^2/2,
    ||w(s)-G||infinity<=B1 (||D||op*s^2/2+s^4/8).

Hence subtraction of the integral equations and the elementary integrating
factor estimate give uniform Hilbert convergence X_e -> X_0 on every fixed
finite s interval as e->0. The same holds for the finite-dimensional a,d,M
and for upper fields in L-infinity (their preactivation coefficients converge).
Moreover c_e(s)/s=integral_0^1 U_e(sv)dv converges uniformly including s=0,
where its value is U_e(0). Thus d_e(s)/s also converges uniformly, with its
continuous value at zero obtained by replacing c/s by U_e(0). These facts
justify all normalized small-time limits used below.

## 4. A compatible coincident reference has strictly positive reverse response

At e=0 all signed directions equal v_*=(1,1,1)/sqrt(3). Coordinate
permutation symmetry and oddness make the active upper preactivation

    z2(s)=p(s) S,   S=Z_1+Z_2+Z_3.

The constant coordinates vanish. Initially p(0)=kappa(1/sqrt(3))>0.
The readout on the auxiliary curve is exactly

    c(s,S)=integral_0^s tanh(p(r)S) dr.

For as long as p is positive, c(s,S) has the sign of S for s>0. Consequently

    d(s)=h(s) 1,   h(s)=E2[S c(s,S) sech^2(p(s)S)]/(3 RZ)>0

for s>0. The density of S is positive on (-3,3), so the inequality is strict.
At s=0 the continuous value h(s)/s is

    E2[S tanh(p(0)S) sech^2(p(0)S)]/(3 RZ)>0.

This positivity persists for all finite s, as can be checked without assuming
it. Put a=a(v_*) and B=E1[b1 b1^T sech^4(w.v_*)]. The single-input auxiliary
equations give

    M_s=d a^T,   a_s=B M^T d,
    (M a)_s=(|a|^2 I+M B M^T)d.

The active vector Ma=RZ p 1. Taking its inner product with 1 gives

    3 RZ p_s=h(s)(3|a|^2+1^T M B M^T 1) >=0.

On any interval with p>0, p is nondecreasing. A first zero would contradict
p>=p(0)>0 before it. Thus p remains positive, and all the preceding signs
hold on every finite auxiliary interval.

The active lower six features are linearly independent: condition a linear
relation on G, use the independent positive conditional variances of k_j
to remove all k coefficients, then independence of tanh G_j to remove the
h coefficients. Since Ma is a nonzero multiple of 1, M^T 1!=0. Therefore
M^T d(s)!=0 and Q(s) is nonzero in lower L2 for s>0. Crucially h(s)/s is a
continuous strictly positive function on any fixed closed auxiliary interval.

## 5. Nearby distinct symmetric seeds retain every tangent direction

Set C_*=E2[tanh^2(p(0)S)]>0 and fix the finite auxiliary interval
0<=s<=S_*=2/C_* (S_* is a time, distinct from the random sum S above).
By continuity, C_0(e)>C_*/2 for all sufficiently small positive e, so each
symmetric seed reaches F=1 strictly before S_*.

For such a seed, permutation equivariance puts each active 3-by-3 block of
M, A=[a(v_1),a(v_2),a(v_3)] and D_b=[d(v_1),d(v_2),d(v_3)] in the form

    M_h=m_hperp Pperp + m_hpar Ppar,
    M_k=m_kperp Pperp + m_kpar Ppar,
    D_b=dperp Pperp + dpar Ppar,
    Ppar=11^T/3, Pperp=I-Ppar.

The two numbers (m_hpar,m_kpar) form mpar. At the coincident reference
dpar=3h(s). Also mpar is nonzero at every s in [0,S_*]: otherwise M^T 1=0,
contradicting Ma=RZ p 1 with p>0. Compactness in s gives

    min_[0,S_*] |mpar_0(s)| >0,
    min_[0,S_*] (dpar_0(s)/s) >0,

with the just-proved continuous value at s=0. Section 3 proves uniform
convergence of these quantities. Thus there exists e_0>0 such that for
every 0<e<e_0 both minima stay positive for the seed e. This is a conclusion
about the entire prescribed finite interval, not an endpoint assumption.

For every input index i the parallel component of M^T d_i is
(dpar/3) times the duplicated parallel middle coefficients. Orthogonality
of the parallel and perpendicular representations gives the exact norm

    |M^T d_i|^2 = (1/3)dpar^2 |mpar|^2
                 +(2/3)dperp^2 |mperp|^2.

It is positive for every s>0. Linear independence of the active lower
features now implies

    R_i(s)=E1[sech^4(w.v_i) Q(v_i)^2]>0,   s>0.

Indeed Q is nonzero on a set of positive measure, w.v_i is finite almost
surely, and sech is positive at every finite argument.

For any real coefficients z_i the first-layer tangent quadratic form obeys

    ||sum_i z_i grad_w f(v_i)||2^2
      = E1 |sum_i z_i sech^2(w.v_i) Q(v_i) v_i|^2
      >= lambda_min([v_i.v_j]) sum_i z_i^2 R_i(s).

The three v_i(e) are linearly independent when e>0: their row matrix is
(e I+11^T)/sqrt(3+2e+e^2), whose eigenvalues are e,e,e+3 divided by that
positive denominator. Hence the full tangent Gram is positive definite
for every s>0 in [0,S_*]. At s=0, c=0 and the initialized readout Gram
is positive definite by the prior exact kappa/rank proof (here a>b>0).
Continuity and compactness consequently give

    mu_e = min_0<=s<=S_* lambda_min(K(X_e(s);v(e))) >0.       (A)

All entries of K are the full trained tangent Gram. This step does not
require upper hidden-feature separation later in training.

## 6. From the seed to an open nonsymmetric family, for every physical time

Here is the full stability argument; mere finite-horizon continuity would
not suffice. Fix one 0<e<e_0. Its physical trajectory is contained in the
compact auxiliary curve used in (A), including its fitting endpoint.
By the locally uniform Lipschitz estimates of section 3, choose r>0 and
an input radius delta_0>0 so that

    K(X;v) >= k I,   k=mu_e/2,

whenever X is within Hilbert distance r of this compact curve and
max_i|v_i-v_i(e)|<delta_0. The radius may also be reduced to keep all actual
input triples linearly independent. A finite covering of the compact curve,
or the same uniform Lipschitz bound on a ball containing it, proves r>0.

The seed loss tends to zero by its proved scalar theorem. Choose a finite
physical time T with sqrt(L_seed(T))<r sqrt(k)/16. Continuous dependence
of the physical flow over [0,T] gives delta in (0,delta_0) such that for
every data triple within delta,

    sup_0<=t<=T ||X(t)-X_seed(t)|| < r/4,
    sqrt(L(T)) < r sqrt(k)/8.

The second inequality follows also from the continuity of predictions and
the norm defining sqrt(L). Thus the trajectory stays in the coercive tube
up to T. For as long as it stays in the radius-r tube after T, write the
normalized residual as z=(f_i-1)/sqrt(3). Then

    L=|z|^2, L_dot=-4 z^T K z,
    ||X_dot||^2=4 z^T K z >=4k L.

Where L>0,

    -d(sqrt(L))/dt=||X_dot||^2/(2 sqrt(L))
                    >=sqrt(k) ||X_dot||.

If L ever vanishes the solution is stationary and all conclusions already
hold. Otherwise integration shows that the remaining displacement before
any hypothetical exit is less than sqrt(L(T)/k)<r/8. Together with the
distance <r/4 at time T, the trajectory stays within 3r/8 of X_seed(T),
which belongs to the reference curve. This contradicts a first exit from
the radius-r tube. Global existence and continuity exclude any other escape.

Therefore K>=kI for every t>=0, including the interval before T. Integrating
L_dot<=-4kL proves the stated exponential bound from initialization, with
no prefactor or unobserved entry hypothesis. The same integrated length
estimate gives the asserted tail bound at any time. Completeness of the
Hilbert space gives a limit with zero loss; the prescribed mark coupling
then gives convergence of the complete joint population laws in W2.

## 7. Meaning, constants, and limitations

First verify the mixed potential, including its entire evolution. Put

    W=1+C_0(1+q)/(C_0+F^2),   Phi=L W.

Here C_0 is the initialization expectation for the actual perturbed data,
so it is fixed during training. Its state gradient in the physical metric is

    grad W = 2 C_0 (0,c,0)/(C_0+F^2)
             -2 C_0 F(1+q) grad F/(C_0+F^2)^2,

where (0,c,0) uses the block order (w,c,M). Consequently the EXACT derivative is

    Phi_dot = W L_dot + L <grad W,X_dot>.

Choose a bounded ball containing the closed tube from section 6. The gradient
bounds in section 3 give constants B<infinity and Lambda<infinity with

    ||grad W||<=B,   ||K||op<=Lambda,

uniformly on that ball and for the nearby inputs. These bounds are uniform
because C_0 stays above half the seed's positive C_0. Throughout the tube,

    Phi_dot <= -4k Phi + 2B sqrt(Lambda) L^(3/2).

Indeed ||X_dot||^2=4 z^T K z<=4 Lambda L. Since W>=1, whenever
sqrt(L)<=k/(B sqrt(Lambda)), this proves Phi_dot<=-2k Phi; if B=0 the
restriction is unnecessary. Choose T in section 6 still larger if needed
so the seed has this residual bound with strict margin. Shrinking delta
makes the perturbed state enter the same strict bound at T, and decreasing
loss preserves it thereafter.

On the compact interval [0,T], the seed satisfies the previous exact
Phi_dot/Phi<=-4 C_seed, with C_seed its initialized C_0. Its loss is strictly
positive at every finite time (the scalar residual solves a linear equation
with finite coefficient), so Phi is bounded away from zero on that interval.
Both Phi and its exact derivative are continuous in state and data, by the
displayed formulas. Uniform finite-time dependence therefore permits another
positive reduction of delta for which

    Phi_dot/Phi <= -2 C_seed   on [0,T].

If a perturbed trajectory were already fitted, Phi and its derivative would
both be zero, so it would cause no exception. Combining the two intervals gives

    lambda(e)=min(2 C_seed,2k)>0,
    Phi(t)<=exp(-lambda(e)t) Phi(0)=2 exp(-lambda(e)t).

This proves the stated mixed-potential theorem. The extra derivative of W
has been bounded explicitly; no monotonicity of q, F, or W on the perturbed
trajectory was assumed. The radius of the open family can be smaller than
the radius sufficient for loss coercivity alone.

The proof gives positive constants without numerical calibration. Its
construction uses Gaussian expectations and finite auxiliary reference
curves whose ODE and horizon are declared explicitly. Those are legitimate
proof objects, not information supplied by an unknown fitting endpoint.
Both loss and the displayed mixed potential are defined on the saved
population state. The full Gram is also a current-state object.
No moving-metric derivative is discarded: the proof uses the exact fixed
physical metric and no differentiation of an inverse metric.

The learned set is the set of exact predictors on the three prescribed
inputs. It is justified by their compatible labels and is not a selected
oracle representation. Uniform full tangent coercivity says that all three
output errors remain correctable by physical motion. The first-layer term
supplies the two transverse directions previously missed by the scalar
argument; upper feature separation is not required at later times.
The finite-length conclusion controls convergence of the whole closure
state, while allowing either expansion or contraction of individual hidden
distances and allowing multiple possible learned endpoints.

As e->0 the signed inputs coalesce. The rate is not asserted uniform in e;
the input Gram and initial upper Gram lose rank at the limit. The actual
admitted triples have no coincident or antipodal redundancy. This proof
does not exclude loss of tangent coercivity for remote geometries, prove
the earlier inverse-metric differential inequality, or settle arbitrary
three-input configurations on the canonical input circle.
