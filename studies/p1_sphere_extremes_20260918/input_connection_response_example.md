# Unbounded first response need not break a bad connection

2026-09-18. Lead elementary counterexample, derived after the response
candidate. This is not the population p=1 closure and is not a claimed
counterexample to the user's conjecture for that closure. It tests the
logical implication from unbounded first input sensitivity to escape.
No scientific input or numerical experiment is required.

For |epsilon|<1 and state (a,z,q) in R^3, put

\[
 V_\epsilon(z)=1+z^4/4-\epsilon z,\qquad
 L_\epsilon(a,z,q)=a^2/2+(1-q^3)^2V_\epsilon(z).       \tag{1}
\]

V has its unique minimum at the real cube root of epsilon, with value
1-3|epsilon|^(4/3)/4>1/4. Thus L is nonnegative and jointly real
analytic on this parameter domain. It is literally a probability-
weighted two-observation square loss: choose equal masses, labels
y_1=1,y_2=-1, and predictions

\[
 f_1=1+a,\qquad
 f_2=-1+\sqrt2(1-q^3)\sqrt{V_\epsilon(z)}.
\]

The square root is real analytic because V is strictly positive. The
loss has exact zero-loss states a=0,q=1 for every parameter.

Euclidean gradient flow gives

\[
 \dot a=-a,\quad
 \dot z=(1-q^3)^2(\epsilon-z^3),\quad
 \dot q=6q^2(1-q^3)V_\epsilon(z).                    \tag{2}
\]

Use the same nonstationary initialization (1,0,0) for every epsilon.
Uniqueness makes q(t)=0 for every finite time; on that invariant plane

\[
 a(t)=e^{-t},\qquad \dot z=\epsilon-z^3,\quad z(0)=0. \tag{3}
\]

For epsilon>0, z increases inside [0,epsilon^(1/3)] and tends to the
right endpoint; for epsilon<0 use odd symmetry. Indeed it cannot cross
the equilibrium by uniqueness, is monotone before it, and a limit
strictly short of that endpoint would have a nonzero limiting derivative.
For epsilon=0, z stays zero. These bounds also give global existence
for these initialized trajectories. Consequently for every |epsilon|<1
the same fixed initialization converges to the bad equilibrium

\[
 e_\epsilon=(0,\sqrt[3]{\epsilon},0),\qquad
 L_\epsilon(e_\epsilon)=1-3|\epsilon|^{4/3}/4>0.      \tag{4}
\]

The initial loss is 3/2 for all parameters and the loss strictly
decreases along each finite-time trajectory because a(t) is nonzero.
At epsilon=0, it equals 1+e^(-2t)/2. At the equilibrium (4), the Hessian
is diag(1,3|epsilon|^(2/3),0), hence PSD. At zero parameter it has
rank one. Nevertheless a positive small change of q decreases the loss
at cubic order: the coefficient of q^3 is -2V_epsilon(z)<0.

Differentiating (3) in epsilon at zero gives

\[
 \partial_\epsilon z(t)|_{\epsilon=0}=t.             \tag{5}
\]

The first input response is unbounded and the limiting force lies in
the Hessian's neutral z direction. Yet the exact perturbed trajectories
satisfy the all-time bound

\[
 \sup_{t\ge0}|(a_\epsilon(t),z_\epsilon(t),q_\epsilon(t))
                -(a_0(t),z_0(t),q_0(t))|
                       =|\epsilon|^{1/3}.             \tag{6}
\]

Therefore arbitrarily small perturbations stay uniformly close and
converge badly for every parameter in an interval, to a nonsmoothly
moving endpoint. Once the base path has entered a fixed endpoint ball,
small enough perturbations never leave a slightly larger fixed ball.
The divergent derivative (5), PSD curvature, cubic descent, zero-loss
attainability, and given nonstationary base connection do not by
themselves imply generic perturbation-induced escape.

This example has a parameter-invariant plane q=0 containing the fixed
initialization. Nothing here establishes such a plane or such a normal
form in the canonical p=1 closure. Its purpose is to isolate what must
still be excluded in that model: nonlinear adjustment that is larger
than order epsilon but still tends to zero with epsilon. A proof that
the p=1 first variation is unbounded remains meaningful; turning it
into escape requires another estimate.

Status: complete elementary candidate, awaiting isolated check.
