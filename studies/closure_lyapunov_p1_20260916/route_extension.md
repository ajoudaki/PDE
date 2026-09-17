# Root route: an open angular family from the antipodal cone

Candidate frozen for comparison, 2026-09-16. Author: root. Scientific inputs:
`docs/global_nonlinear.md` C.4.7.9.3–4, C.4.7.10 B/C.1 and D.3;
`docs/NOTATION.md`. No other study used. This route was developed without
reading other route files. It independently recovered the axis cone and then
used a finite gradient-ascent interval to extend it to nearby angles.

## Exact fixed initialization and notation

Use p=1, eta=1/4096 and the exact inverse-Cholesky normalization in the book.
Write phi=tanh. On population 1 let g_i be independent N(0,1),
X_i=phi(g_i), p_i=zeta_i+alpha X_i, Y_i=phi(p_i), with independent
zeta_i~N(0,tau). On population 2 let xi_i be independent N(0,v) and
H_i=phi(xi_i). The two populations are separate. Here
v=E phi(G)^2, tau=E phi(sqrt(v)G)^2, alpha=1-tau.
The raw lists are (1,X_1,X_2,Y_1,Y_2) and (1,H_1,H_2).
Let b_1,b_2 be their canonical normalized columns, D the canonical contraction.
All frozen marks, including their g correlations, are retained.

It is convenient only to group the normalized odd coordinates by i. Put
r=E[X_iY_i], v_y=E[Y_i^2], chi=E[phi'(p_i)],
ell=sqrt(v+eta), n=sqrt(v_y+eta-r^2/(v+eta)), h=sqrt(tau+eta).
Then lower block B_i=(X_i/ell,(Y_i-r X_i/(v+eta))/n) and upper
beta_i=H_i/h. This is a permutation of the canonical Cholesky coordinates,
not a new normalization. Constants are separate. Independence/parity gives
D constant row/column zero and identical active rows

m_0=(alpha v/(h ell), [alpha r eta/(v+eta)+tau chi]/(h n))

on their respective lower blocks, with cross-coordinate blocks zero.
This follows by applying the established contraction formula to the raw
entries: C(H_i,X_i)=alpha v and C(H_i,Y_i)=alpha r+tau chi.
The initial lower feature for input e_2 is

a_0=(v/ell, r eta/((v+eta)n)).

All displayed entries are positive. In fact r>0 because, conditional on g,
E_zeta phi(zeta+alpha phi(g)) is strictly increasing and odd in phi(g),
so its product with phi(g) is positive except at g=0. chi>0, n>0 by ridge.
Let k_0=m_0·a_0>0 and

kappa_0=E[phi(beta_2 k_0)^2]>0.

Every constant is an initialized Gaussian integral or finite linear algebra.
Let B_1 be any explicit supremum envelope for |b_1|, and B_2 for |b_2|;
for example sqrt(5)||L_1^{-1}||op and sqrt(3)||L_2^{-1}||op.

## The family and the fixed physical metric

Fix A>0 (A=1 is allowed). For 0<=epsilon<=1/2 set
u_+=(epsilon,sqrt(1-epsilon^2)), nu_-=(epsilon,-sqrt(1-epsilon^2)),
and give (sqrt(2)nu_+,+A),(sqrt(2)nu_-,-A) mass 1/2 each.
Their angular separation is 2 arccos epsilon. We prove the result for an
explicit positive epsilon_* below, including genuinely non-antipodal pairs.
No labels are made small and no hidden feature is frozen.

On the fixed mark carriers let X=(w,c,M), with metric
||delta X||_raw^2=E_1|delta w|^2+E_2|delta c|^2+||delta M||_F^2.
Its pushforward controls the joint-law W2 distances with all frozen marks
coupled identically. All dynamics below use the physical metric of the book.

For any state define H_±=phi(b_2^T M a(nu_±)),
U=(H_+-H_-)/2, F=(f(nu_+)-f(nu_-))/2, and

C(X)=E_2 U^2,   Z_A={states with f(nu_+)=A, f(nu_-)=-A}.

C is one quarter of the squared L2 separation of the two upper hidden
representations. Z_A is defined by the data, not by an unknown endpoint.

## Exact symmetry and the auxiliary gradient parameter

Let R=diag(1,-1). Reversing (g_2,zeta_2) and xi_2 preserves their respective
mark laws. The corresponding diagonal sign matrices J_1,J_2 satisfy
b_l∘S_l=J_l b_l and D=J_2 D J_1. The isometry

T(w,c,M)=(R w∘S_1, -c∘S_2, J_2 M J_1)

fixes initialization and transforms the predictor to -f(Ru). It preserves
this data loss. Direct substitution in the displayed gradient equations,
or differentiating this isometric invariance, shows that their vector
field is equivariant. Uniqueness therefore gives T X=X and f(nu_-)=-f(nu_+).
Thus on the reached trajectory F=f(nu_+) and L=(A-F)^2.

The same symmetry holds for the gradient-ascent equation

dX/ds=V_epsilon(X)=grad_raw F(X),  X(0)=(g,0,D).

Its explicit components are

V_c=U,
V_M=(d_+ a_+^T-d_- a_-^T)/2,
V_w=(phi'(w·nu_+)q_+nu_+-phi'(w·nu_-)q_-nu_-)/2.

This is an auxiliary autonomous equation defined entirely from the same
current state and fixed data. It is used to prove estimates, not supplied
as an extra state or future oracle. The chain rule gives

F_s=K:=||V||_raw^2 >= C(X).

Whenever F<A, the original physical flow is exactly this curve with
s_t=2(A-F). Direct substitution recovers every factor in the canonical
unhalved-loss equations.

For every finite S, local existence extends throughout [0,S], since

||c(s)||infty<=s,  ||M(s)||op<=2+s^2/2,
||w(s)-g||_2<=s^2+s^4/8,
||w(s)-g||infty<=B_1(s^2+s^4/8).

Indeed |a|<=1 and |d|<=||c||_2 by the contraction property of the normalized
features. The three speeds are bounded by 1, s, (2+s^2/2)s, with B_1
inserted for the row supremum bound. Integration proves these estimates,
and bounded increments give endpoints in the local existence spaces.

## Axis cone: complete mechanism

At epsilon=0 the data are antipodal e_2. Input oddness reduces the equations
exactly to the single e_2 equation. Independence of the two coordinate
blocks and their sign symmetries preserve w_1=g_1, w_2=W(g_2,zeta_2),
c=c(beta_2), the other initialized matrix row, and a single active row m(s).
This is verified by substituting the following closed equations; the unused
cross-block expectations vanish by oddness. Initially W=g_2,m=m_0,c=0.
With B=B_2's lower two-coordinate block (that is B_i at i=2), define

a=E_1[B phi(W)], k=m·a, d=E_2[beta_2 c phi'(beta_2 k)].

(The symbol B here denotes the lower block, not the feature envelope B_2.)
Then

W_s=d(m·B)phi'(W),   m_s=d a,   c_s=phi(beta_2 k),
k_s=d (|a|^2+E_1[(m·B)^2 phi'(W)^2]).

While k>0, c has the sign of beta_2 and d>=0, so k_s>=0. A first-exit
argument from k_0>0 keeps k>=k_0 for all finite s. For s>0, d>0 and a!=0
because m·a=k>0, so k_s>0. Consequently

C_axis(s)=E phi(beta_2 k(s))^2 >= kappa_0,

strictly for s>0. This is a geometric anti-collapse estimate, not simply
the loss identity. It yields F_axis(s)>=kappa_0 s.

There is also an exact non-Euclidean balance on this axis:

||m(s)||^2-E_1 sinh^2 W(s) = ||m_0||^2-E_1 sinh^2 g_2.

Both derivatives equal 2dk: use (sinh^2 W)'=2phi(W)/phi'(W).
Differentiation is valid on finite s intervals since W-g_2 is bounded and
Gaussian exponential moments are finite. Thus this lower transformed
spread and the active matrix norm increase together. It is not a claim
that all hidden coordinates contract.

## Explicit extension bounds

Set S=2A/kappa_0, C_*=S, R_*=2+S^2/2,
W_*=sqrt(2)+S^2+S^4/8. Below abbreviate C=C_*, R=R_*, W=W_* only
in constants. For two feature flows, one at epsilon and one at zero, put
E=||w_e-w_0||_2+||c_e-c_0||_2+||M_e-M_0||_F,
and delta=max_±|nu_±(epsilon)-nu_±(0)|<=2epsilon.

The elementary contraction/gate estimates are

|a_e-a_0| <= E_w+W delta,
||z_e-z_0||_2 <= E_M+R(E_w+W delta),
|d_e-d_0| <= E_c+2C[E_M+R(E_w+W delta)],
||q_e-q_0||_2 <= R|d_e-d_0|+C E_M,
||q_0||infty <= B_1 R C.

They hold for each sign. In the row equation subtract q, then the gate,
then the input vector. Summing the three velocity differences gives

D^+E <= L E+P delta,
L=2+2R+C(2R^2+2B_1R+4R+5),  P=L W+R C.

For verification, the coefficients before enlargement are R+1 on E_c,
1+C(2R+3) on E_M, and R+C(2R^2+2B_1R+2R+1) on E_w;
the input coefficient is the last coefficient times W plus RC.
Integrating (multiply by exp(-Ls)) gives

sup_[0,S] E <= Q delta, Q=P S exp(LS).

Let H=(1+R)Q+R W and J=Q+C H. Then uniformly on this interval

||U_e-U_0||_2<=H delta,
|C_e-C_axis|<=2H delta,  |F_e-F_axis|<=J delta.

The fixed constants can be enormous but are finite, initialized-data
quantities. Their purpose is an explicit positive family, not a practical
angle certificate.

To obtain a strictly positive learned hidden separation as well, let
K_*=1+C^2+R^2 C^2, h_*=E[beta_2 phi(beta_2 k_0)] sech^2(B_2 R)>0,
g_*=h_*^2 k_0^2 A^2/(R^2 K_*^2)>0.
Here K=||V||^2<=K_* on [0,S]. On the axis, |k|<=R and
|beta_2|<=B_2. From c(beta,s)=int_0^s phi(beta k(v))dv and k>=k_0,

d(s)>=s h_*,  k_s>=s h_* k_0^2/R^2,
d/dk E phi(beta k)^2 >=2h_*.

Therefore C_axis(s)-kappa_0 >=h_*^2 k_0^2 s^2/R^2.
Choose

delta_* = min(1, kappa_0/(4H), A/(2J), g_* /(8H)),
epsilon_* = delta_*/2 >0.

For 0<=epsilon<=epsilon_*, the preceding bounds show C_e>=kappa_0/2
through S and F_e(S)>=3A/2. Since F_e(0)=0 and F_s>=kappa_0/2,
there is a unique first s_*<S with F_e(s_*)=A. Also s_*>=A/K_*.
The root is used only in this proof, not in the definition of C or Z_A.
At that root

C_e(s_*)-C_e(0) >=g_*/2>0.

Indeed each comparison of C costs at most 2H delta, and the axis increase
at s_* is at least g_*.

## Physical-time conclusion and full-state convergence

Set kappa=kappa_0/2. The scalar equation s_t=2(A-F_e(s)), s(0)=0,
has s(t)<s_* for every finite t and increases to s_*. To verify this,
e=A-F obeys e_t=-2K e, and K is continuous and bounded on [0,S]; hence
e=A exp(-2int Kdt)>0 at finite t. The lower bound K>=kappa gives e->0,
so its increasing s limit must be s_*. The composed feature solution is
therefore the canonical physical solution by uniqueness.

For every t>=0,

L(t)<=A^2 exp(-4kappa t),  C(X_t)>=kappa,
int_t^infty ||X_dot||_raw dt <=sqrt(L(t))/sqrt(kappa).

For the last inequality, ||X_dot||=2e sqrt(K), while -e_dot=2eK;
thus ||X_dot||<=-e_dot/sqrt(kappa), and integrate. The state has a
strong raw-metric limit X_infty in Z_A and its distance to that set is
at most sqrt(L(t)/kappa). The same common-mark coupling proves joint-law
W2 convergence. The stronger bounded-coordinate feature-time continuity
also gives uniform convergence of w-g and c. M converges in Frobenius norm.

The learned upper feature separation satisfies

||H_+(infty)-H_-(infty)||_2^2
 >=||H_+(0)-H_-(0)||_2^2+2g_*.

This is a fixed physical L2 distance, not a shrinking state-dependent
metric. It has independent significance: opposite outputs require
c paired with H_+-H_-, and F=E[cU]; C>=kappa supplies a nonvanishing
readout direction that cannot stall. No uniqueness of the fitting state
or contraction between arbitrary trajectories is asserted. The endpoint
is selected by the prescribed initialized trajectory, while the fitting
set and separation functional were defined before training.

## Scope and gaps

This is a candidate complete theorem for an explicit non-antipodal angular
interval near pi, with ordinary unit labels included, on the exact p=1
closure. It does not prove the sign of C_dot away from the axis, nor cover
all separations. At exact coincidence opposite labels cannot fit; no
geometry-independent rate near coincidence is claimed. Input oddness also
obstructs equal nonzero labels at antipodes. This result does not identify
any full-network or closure-order limit, nor establish generalization.
No numerical evidence or external theorem is used beyond the established
closure initialization, finite-time wellposedness, and elementary calculus.
