# Strict hidden-contrast gain from the normalized potential

Root addendum, 2026-09-16. Depends on scalar_margin_extension.md and the exact
p=1 reflection subsystem already derived in cross_sign_note.md. This is a
separate addendum so that the frozen scalar-margin candidate stays unchanged.

Consider u_+=(a,b),u_-=(a,-b), with a>=0,b>0, a^2+b^2=1 and labels +/-A.
In the reflection-fixed subsystem write the two upper preactivations
z_+=beta_1 B_1+beta_2 B_2, z_-=beta_1 B_1-beta_2 B_2,
where B_i=m_i·a_i and the two independent symmetric upper marks beta_i
have positive density on (-beta_max,beta_max). Assume B_2(0)>0.

At any such initialized state, vary only the second active row m_2 by
multiplication by 1+lambda, holding lower state and other middle rows fixed.
This varies B_2 to (1+lambda)B_2 and holds B_1 fixed. With
U=(tanh z_+-tanh z_-)/2 and C=E U^2, differentiation gives

dC/dlambda at lambda=0
 =E[U beta_2 B_2(sech^2 z_++sech^2 z_-)]>0.

Indeed U has the sign of beta_2 B_2, and the gates are strictly positive;
nonzero beta_2 has full probability. Thus grad_h C(h_0) is nonzero.
The directional variation is an allowed canonical coefficient variation,
with no change of metric, dictionary or initialization.

Let X_s=grad F, F=<c,U(h)>, c(0)=0, and h=(w,M). Differentiability of the
finite contraction/gate maps in the characteristic norms gives

h_s(0)=0,
c_s(0)=U(h_0),
h_s(s)=(s/2) grad_h C(h_0)+o(s)

in the physical norm. To justify the last equation without invoking a
global C2 theorem on an unrestricted L2 Nemytskii map, use
h_s=DU(h)^*c. The operator DU(h)^* is continuous along the bounded
characteristic trajectory, c=s U(h_0)+o(s), and
DU(h_0)^*U(h_0)=grad_h C(h_0)/2. The derivative U acts through the finite
contractions in w and M, so this continuity follows from bounded marks
and bounded gate derivatives exactly as in route_local.md.

Consequently ||h_s||>0 throughout some positive interval (0,s_0).
For q=||c||^2, K=||grad F||^2, the identity

qK-F^2=(q C-F^2)+q||h_s||^2

then has a strictly positive right side there: the first term is
nonnegative by Cauchy-Schwarz, and q>0 for s>0. Thus

P_s=-2(qK-F^2)/F^3<0

on that interval. The scalar-margin theorem gives P_s<=0 subsequently.
Its fitting feature time s_*>0 therefore satisfies

P(X_(s_*))<1/C_0,
C(X_(s_*))>=1/P(X_(s_*))>C_0.

This proves a strictly positive increase in the squared upper-hidden
separation between initialization and the fitted endpoint for every pair
in this symmetric family with B_2(0)>0. No numerical value or uniform
angle-independent lower bound for that increase is asserted. The target
observable C is fixed before training and uses only the current state;
the endpoint appears only in the conclusion, not in the potential or
initialization. This is stronger than merely saying hidden parameters move.
