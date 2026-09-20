# A given bad connection has unbounded first input response

2026-09-18. Lead derivation within the current study, before comparison
with the two current scoped candidates. This accepts the user's precise
hypothesis: at the special data, canonical training converges to the
specified bad state. It does not try to establish that hypothesis.
Scientific inputs are the complete canonical `docs/observable_p1.md` and
this study's `INPUT_PERTURBATION_RESULTS.md` and its complete local proof
`input_perturb_frozen.md`. No experiment, other study, or external result
is used. This is not promoted material.

## 1. Exact statement

Use the exact canonical dimension-three p=1 closure, its correlated
Gaussian-derived marks, physical population-L2/Frobenius metric, all
matrix entries, and odd invariant sector. Here b_1 in R^6 and b_2 in R^3
are the nonconstant dictionary features retained in that invariant
sector; q below belongs to R^6. Physical inputs have norm
sqrt(3). The seven reference inputs are

\[
 x_i=\sqrt3(C,S\cos\alpha_i,S\sin\alpha_i),\qquad C,S>0,
 \quad C^2+S^2=1,
\]

with three positive labels at angles 0, 2pi/3, 4pi/3 and four negative
labels at pi/4, 3pi/4, 5pi/4, 7pi/4; all masses are 1/7. Write phi=tanh.
Keep the fixed Hilbert coordinate theta=(w-g,c,M) and canonical initial
state theta_in=(0,0,D). Neither the carriers nor theta_in change when the
inputs change.

Fix a nonzero vector q in the lower dictionary space, set

\[
 e(\omega)=\operatorname{sign}(q\cdot b_1(\omega)),\quad
 A=E_1[b_1e],\quad \kappa=q\cdot A=E_1|q\cdot b_1|>0,
\]

and choose a>0. The reference state is

\[
 w_*=ae e_1,\quad M_*=e_1q^T,\quad
 z=\kappa\phi(aC),\quad H(b_2)=\phi(zb_{2,1}),
 \quad J(b_2)=b_{2,1}\phi'(zb_{2,1}).                 \tag{1}
\]

The upper field c_* is bounded, odd, depends only on b_{2,1}, and satisfies

\[
 E_2[c_*H]=-1/7,\qquad E_2[c_*J]=0.                 \tag{2}
\]

These are exactly the reference equilibria of the local perturbation
theorem, but the response result below needs neither of its two excluded
amplitude conditions. The existing two-function Gram construction gives
(2). Every backward vector is zero, the loss is 48/49, and the actual
physical Hessian is

\[
 D^2L(\theta_*)[(h,k,N)]^2=2(E_2[kH])^2.            \tag{3}
\]

**Theorem (unbounded response under the specified base connection).**
Assume the canonical trajectory at these reference inputs converges
strongly in the physical Hilbert space to theta_*. Let xi_i be tangent
to the physical input sphere, and use the exact spherical path

\[
 x_i(\epsilon)=
 \frac{x_i+\epsilon\xi_i}
 {\sqrt{1+\epsilon^2|\xi_i|^2/3}}.
\]

Put rho_i=(-1/7-y_i)/7, and define

\[
 \Delta=\frac1{\sqrt3}\sum_i\rho_i\xi_{i,1}.        \tag{4}
\]

For every finite t the physical first variation

\[
 Z(t)=\left.\partial_\epsilon\theta_{X(\epsilon)}(t)
                                  \right|_{\epsilon=0}
\]

exists, starts at zero, and solves the exact linearized closure. If
Delta is nonzero, then

\[
                       \sup_{t\ge0}\|Z(t)\|_{\mathcal H}=\infty.
                                                               \tag{5}
\]

Delta is a nonzero linear functional on the product of the seven tangent
planes. Its zero set has codimension one and measure zero. Thus (5)
holds for almost every tangent direction under any absolutely continuous
noise law on that finite-dimensional tangent space. This is a statement
about the derivative at zero noise, not yet an escape probability at
any nonzero noise amplitude.

In particular there are no constants K, epsilon_0>0 such that

\[
 \|\theta_{X(\epsilon)}(t)-\theta_X(t)\|_{\mathcal H}
       \le K|\epsilon|\quad
       \text{for every }t\ge0,\quad |\epsilon|<\epsilon_0. \tag{6}
\]

Equivalently, for every K there is a finite observation time and then
arbitrarily small nonzero perturbations whose displacement at that time
exceeds K times their amplitude. The order of these quantifiers matters.

## 2. Reference stationarity and Hessian

For an arbitrary current state and current inputs define only the usual
closure moments:

\[
 a_i=E_1[b_1\phi(w\cdot x_i/\sqrt3)],\quad v_i=Ma_i,
 \quad H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\]
\[
 \rho_i=(f_i-y_i)/7,\qquad
 d_i=E_2[b_2c\phi'(b_2\cdot v_i)].
\]

The exact field is

\[
 \dot w=-2\sum_i\rho_i\phi'(w\cdot x_i/\sqrt3)
               (b_1^TM^Td_i)x_i/\sqrt3,
\]
\[
 \dot c=-2\sum_i\rho_iH_i,\qquad
 \dot M=-2\sum_i\rho_i d_i a_i^T.                    \tag{7}
\]

At (1), all a_i=phi(aC)A and v_i=ze_1. Equation (2) and independence
and centering of the other upper coordinates give d_i=0. The weighted
residual moments satisfy

\[
 \sum_i\rho_i=0,\quad \sum_i\rho_ix_i=0,
 \quad \sum_i\rho_ix_ix_i^T=0.                     \tag{8}
\]

The triangular and square angular groups both have zero first angular
moment and the same second angular moment, with cancelling total
residual masses -24/49 and 24/49. This proves (8), and (7) is stationary.

For completeness, the first lower moment variation in a direction h is
linear in x_i because phi'(ae x_{i,1}/sqrt3)=phi'(aC):

\[
 Da_i[h]=\phi'(aC)E_1[b_1(h\cdot x_i/\sqrt3)].
\]

Thus Dv_i=N phi(aC)A+M_*Da_i is affine in x_i. At d_i=0 the first
prediction variation is E_2[kH], common to all i. In the residual part
of the second variation, the mixed readout/effective-vector term is
affine in x_i, the c_*-weighted quadratic upper term is quadratic in
x_i, and the term involving the second variation of v_i is multiplied
by d_i=0. Every such residual sum vanishes by (8). This gives (3).

It is an actual bounded Hilbert Hessian: differentiation of the exact
field (7) has only one potentially problematic local lower multiplication
term, multiplied by rho_i M^T d_i. This coefficient is zero at theta_*.
The remaining finite moment maps have bounded first derivatives, with
quadratic remainders bounded by the L2 norm squared via bounded phi''.
The lower gate changes only multiply finite coefficients vanishing at
theta_*. Subtracting the resulting linearization gives o(||delta theta||)
in the physical Hilbert norm. The limiting linear field is consequently

\[
 \mathcal A_*(h,k,N)=(0,-2H E_2[kH],0).              \tag{9}
\]

## 3. The exact response along the entire trajectory

Write F_X(theta) for (7). On a bounded Hilbert ball F is jointly locally
Lipschitz in theta and the finite input chart. For example a lower gate
or feature difference is bounded in L2 by a constant times

\[
 \|w-\widetilde w\|_2+
                  \|\widetilde w\|_2\max_i|x_i-\widetilde x_i|.
\]

All other derivatives of phi are bounded, marks are bounded, and upper
arguments depend on finite vectors. The field has bounded linear strong
directional derivatives in state and data on such a ball, uniformly
bounded as operators there. These need not be Frechet continuous as
operators at arbitrary states.

For a fixed state direction h and input direction xi, the only direct
lower argument derivative is

\[
       \delta(w\cdot x_i/\sqrt3)
                  =(h\cdot x_i+w\cdot\xi_i)/\sqrt3. \tag{10}
\]

This belongs to L2. Dominated convergence proves the strong directional
derivative of each lower gate: bound the difference quotient by a
constant times |h|+|w||xi|. Upper derivatives are finite-vector
derivatives paired with c in L2. The ordinary product rule therefore
gives bounded linear operators

\[
 \mathcal A(t)=D_\theta F_X(\theta_X(t)),\qquad
 B(t)=D_XF_X(\theta_X(t))[\xi].
\]

Derivative evaluation is also continuous on each fixed joint direction.
For the delicate lower multiplier this follows from
||phi''(q_n)r_n-phi''(q)r||_2 -> 0 when q_n -> q and r_n -> r in L2:
first subtract r_n-r using the uniform bound on phi'', then truncate
the fixed r to |r|<=R and use gate convergence there, controlling the
complement by its L2 tail. Finite moments and products have the same
continuity. Together with the local operator bound, this gives joint
continuity of derivative evaluation on base point and direction.

The finite-horizon difference quotients converge to the solution of

\[
        \dot Z(t)=\mathcal A(t)Z(t)+B(t),\qquad Z(0)=0. \tag{11}
\]

Here is a justification not assuming Frechet C1 regularity on L2.
The local Lipschitz estimate bounds the finite-horizon difference
quotients. Solve (11), subtract its integral equation from the perturbed
one, and evaluate the field directional remainder along the fixed
continuous path (Z(t),xi). Strong directional differentiability, local
Lipschitzness, and a finite covering of this compact path make the
remainder uniformly o(1) on the finite interval. Gronwall then gives
uniform convergence of the difference quotients. Alternatively the
same conclusion follows by dominated convergence of the integral
remainders and the same Gronwall estimate.

Under the assumed strong base convergence we have

\[
 \|\mathcal A(t)-\mathcal A_*\|_{\rm op}\to0,
                  \qquad B(t)\to B_* \text{ in }\mathcal H. \tag{12}
\]

The operator-norm assertion is special to the endpoint d_{i,*}=0. The
lower multiplication term is bounded in operator norm by a constant
times max_i|d_i(t)|, hence tends to zero. All remaining terms are finite
rank with their representing lower gate/mark functions converging in
L2, their upper functions converging uniformly as v_i(t) converges,
and their c pairings converging by Cauchy--Schwarz. Their finite
coefficients converge too. Thus their operator norms converge. This
also verifies (9) independently of the second-variation calculation.

The data derivative contains (10) with h=0 and no unbounded multiplier
other than w(t) in L2. Products of bounded continuous gate factors with
w(t) converge in L2 when w(t) converges strongly in L2: subtract
w(t)-w_* first, and apply dominated convergence with |w_*| squared to
the remaining term (or its subsequences). The other terms again use
finite moments. This proves the second assertion of (12).

## 4. A nonzero force in a neutral direction

Only the c component of B_* is needed. When differentiating in the
inputs at a fixed reference state, every prediction derivative is
d_{i,*} dot delta v_i=0. Thus delta rho_i=0. Also

\[
 \delta a_i=a\phi'(aC)A\,\xi_{i,1}/\sqrt3,
 \quad \delta v_i=a\kappa\phi'(aC)e_1\,\xi_{i,1}/\sqrt3.
\]

Differentiating dot c in (7) therefore gives

\[
                  (B_*)_c=-2a\kappa\phi'(aC)\Delta J. \tag{13}
\]

Let k=J-(E_2[JH]/E_2[H^2])H and K=(0,k,0) in the physical Hilbert
space. Then k is nonzero. Indeed if J were a scalar multiple of H in
L2, the positive density of b_{2,1} on an interval and real analyticity
would imply t phi'(zt)=beta phi(zt) on an interval. Comparing the
linear Taylor terms gives beta=1/z; comparing the cubic terms gives
-z^2=-z^2/3, impossible since z>0. Also H is not zero. Consequently

\[
 \mathcal A_*K=0,
 \qquad \langle K,B_*\rangle
       =-2a\kappa\phi'(aC)\Delta\|k\|_2^2\ne0       \tag{14}
\]

when Delta is nonzero. This direction is an actual upper readout
variation, orthogonal to the common current feature; it is not an
auxiliary state or an unknown future target.

If Z were bounded for all time, (11)--(12) and (14) would imply

\[
 \frac d{dt}\langle K,Z(t)\rangle
   =\langle(\mathcal A(t)^*-\mathcal A_*^*)K,Z(t)\rangle
                         +\langle K,B(t)\rangle
   \longrightarrow \langle K,B_*\rangle\ne0.
\]

The scalar projection would then grow linearly, contradicting boundedness.
This proves (5). This argument does not assert linear growth of Z
without the contradictory boundedness assumption.

To see genericity, take one tangent displacement
xi_i=e_1-(x_{i,1}/3)x_i and all others zero. Its first coordinate is
1-C^2=S^2>0 and rho_i is nonzero, so (4) is not the zero functional.
The measure statement follows by Fubini in finite-dimensional linear
coordinates. Equation (6) would bound every fixed-time difference
quotient by K, contradicting (5).

## 5. What this does and does not resolve

This is a nonuniform-in-time instability of the presumed canonical
connection with respect to input changes. It addresses the whole
trajectory, and remains true even at the two exceptional amplitudes of
the older local strict-saddle theorem. It does not assume differentiable
dependence of the endpoint on the data, nor classify which base
equilibria are canonically reached.

It does not prove escape from a fixed neighborhood. A perturbation can
have unbounded first response while its nonlinear displacement stays
small, for example of order sqrt(|epsilon|), at all late times. Nearby
bad equilibria and their attraction sets could rearrange nonsmoothly.
Excluding that possibility, or proving a transverse intersection with
the moving trapping sets, is still required to establish the user's
almost-sure escape claim. No conclusion that loss tends to zero follows
from (5) alone.

The degeneracy is specific to positive residuals. As a sanity check,
at a fitted state any first-order input force is
-2 D_theta f^* diag(p) D_X f[xi], whereas the loss Hessian is
2 D_theta f^* diag(p) D_theta f. Its pairing with a kernel direction
of that Hessian is zero. Thus the nonzero neutral forcing in (14)
cannot occur by this argument at a zero-loss state. This does not claim
regular endpoint dependence or stability at every fitted state.

Status: complete lead candidate, requiring a fresh independent check.
