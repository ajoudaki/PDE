# A cubic p=1 equilibrium: minibatch noise and actual hidden motion

2026-09-19. Lead derivation from the complete established
`docs/observable_p1.md` and `docs/NOTATION.md`. No other study is a
scientific input. This is a fresh four-input example, not an imported
earlier construction. Exact population expectations, no simulation.

## 1. Model and a nonparallel, compatible four-input family

Use the canonical dimension-three p=1 correlated Gaussian carriers,
ridge normalization, tanh activation phi, and the odd invariant sector.
The nonconstant marks are b_1 in R^6 and b_2 in R^3. All matrix entries
are allowed to train. State coordinates are theta=(w-g,c,M), with the
physical L2/L2/Frobenius norm. The canonical initialization remains
(0,0,D), but the ambient equilibrium below is not asserted to be its
reachable endpoint.

Choose C,S>0 with C^2+S^2=1 and equal probabilities 1/4. The physical
inputs and labels are

\[
 \sqrt3(C,S,0),\ \sqrt3(C,-S,0):\quad y=+1,
 \qquad
 \sqrt3(C,0,S),\ \sqrt3(C,0,-S):\quad y=-1.          \tag{1}
\]

These are four distinct, pairwise nonparallel and nonantipodal inputs.
They have a linear dependence. Write u_i=x_i/sqrt3 only inside proofs;
all physical input normalization factors are thus explicit.

For arbitrary states the exact moments and per-observation gradients
of ell_i=(f_i-y_i)^2 are

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,
 \quad H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
 \quad d_i=E_2[b_2c\phi'(b_2\cdot v_i)],
\]
\[
 g_i=2(f_i-y_i)
 \left(\phi'(w\cdot u_i)(b_1^TM^Td_i)u_i,
                    H_i,\ d_i a_i^T\right).          \tag{2}
\]

L=(1/4)sum_i ell_i. For B independent draws I_1,...,I_B with law 1/4,
one exact population SGD step of size eta>0 is

\[
              \theta^+=\theta-\eta B^{-1}\sum_{j=1}^B g_{I_j}(\theta).
                                                               \tag{3}
\]

There is one shared random batch for the whole population. The neuron
carriers have already been integrated; they are not resampled.

## 2. A rank-one PSD equilibrium with a cubic descending direction

Let q select the first h-coordinate of b_1, so B_1(omega):=q dot b_1
is a positive multiple of tanh G_1. (The scalar B_1 here is a mark,
not the batch size B.) Put e=sign G_1,

\[
 A=E_1[b_1e],\qquad \kappa=q\cdot A=E_1|q\cdot b_1|>0,
 \quad w_*=ae e_1,\quad M_*=e_1q^T,\quad c_*=0,
 \qquad a>0.
\tag{4}
\]

All a_i=phi(aC)A, all v_i=z e_1 with z=kappa phi(aC)>0, and
all H_i=H=phi(z b_{2,1}). All predictions and backward vectors are
zero. Since the labels average to zero, (4) is a full-batch stationary
state at loss one.

For a state variation (h,k,N), the first effective-vector variation is
affine in u_i:

\[
 \delta v_i=N\phi(aC)A+
        M_*\phi'(aC)E_1[b_1(h\cdot u_i)].
\]

Because c_*=0, the first prediction variation is E_2[kH] and the
second is 2E_2[k phi'(b_2 dot v_*) b_2 dot delta v_i]. In (1),
sum_i y_i=0 and sum_i y_i u_i=0. Thus the residual-weighted second
prediction variations cancel and

\[
           D^2L(\theta_*)[(h,k,N)]^2=2(E_2[kH])^2.   \tag{5}
\]

This is an actual bounded Hilbert Hessian. The lower finite moments
have quadratic remainders controlled by ||h||_2^2, since phi'' and marks
are bounded. The lower gate multiplication in the gradient is multiplied
by (f_i-y_i)M^Td_i=0 at (4), so its remainder is the product of an
O(||delta theta||) gate change in L2 and an O(||delta theta||) finite
coefficient. All other terms are smooth finite moments and pairings.

To verify cubic descent explicitly, let

\[
 J=b_{2,1}\phi'(zb_{2,1}),\qquad
 k=J-\frac{E_2[JH]}{E_2[H^2]}H.
\]

k is nonzero: proportionality of J and H on the upper coordinate's
positive-density interval would imply t phi'(zt)=beta phi(zt); its
linear and cubic Taylor coefficients contradict one another for z>0.
Therefore E_2[kJ]=||k||_2^2>0 and E_2[kH]=0.

Let psi=phi(G_2)^2-E phi(G_2)^2, a bounded nonzero centered even
function, and take h=e psi e_2. Independence of canonical coordinate
pairs and centering give E_1[b_1h^T]=0: coordinates in pair 1 use
E psi=0, and the other pairs use E sign G_1=0. Thus along
w=w_*+t h and fixed M=M_*, all delta v_i=0, whereas

\[
 \delta^2 v_i=\kappa\phi''(aC)E[\psi^2]u_{i,2}^2e_1.
\]

Along the full curve (w_*+th,tk,M_*), all first and second prediction
derivatives vanish and

\[
 f_i'''(0)=3\kappa\phi''(aC)E[\psi^2]u_{i,2}^2\|k\|_2^2.
\]

Since sum_i (y_i/4) u_{i,2}^2=S^2/2,

\[
 L'''(0)=-3\kappa\phi''(aC)E[\psi^2]S^2\|k\|_2^2>0. \tag{6}
\]

Replacing k by -k makes this derivative negative. Bounded variations
justify all differentiations and the third-order remainder directly.
This proves cubic descent, not a one-sided attraction theorem for the
full population flow.

## 3. Noise initially misses the cubic direction

At (4) each exact sample gradient is

\[
                       g_i=(0,-2y_iH,0).             \tag{7}
\]

Consequently the batch gradient has mean zero and covariance

\[
               \operatorname{Cov}(g_B)=\frac4B
                       (0,H,0)\otimes(0,H,0).        \tag{8}
\]

The covariance has rank one and points entirely in the positive Hessian
direction in (5). Its projection on the cubic direction (h,-k,0) is
zero. Thus fresh minibatches are not equivalent to a nondegenerate
isotropic perturbation of every flat state direction.

There is nevertheless actual stochastic motion. If bar y is the average
of the first B sampled labels, then the exact first step is

\[
              w^+=w_*,\quad M^+=M_*,\quad c^+=2\eta\bar y H,
\]
\[
              L(\theta^+)=1+4\eta^2\bar y^2\|H\|_2^4. \tag{9}
\]

For B=3, bar y belongs to {-1,-1/3,1/3,1}. Hence every first step
is nonzero and strictly increases the total training loss. For every
B, E[L(theta^+)]=1+4 eta^2 ||H||_2^4/B. Noise does not preserve the
full-batch Lyapunov identity.

Hidden learning begins at the next step. At theta^+ the common backward
vector is

\[
 d^+=2\eta\bar y E_2[b_2H\phi'(zb_{2,1})]
                  =2\eta\bar y\,\nu e_1,
 \qquad \nu=E_2[b_{2,1}H\phi'(zb_{2,1})]>0.          \tag{10}
\]

The other coordinates vanish by independence. Positivity holds because
b_{2,1} phi(zb_{2,1}) is positive off zero and phi'>0. Let bar y'
denote the next batch's label average and f^+=2 eta bar y ||H||_2^2.
Its exact matrix increment is

\[
              M^{++}-M^+=-2\eta(f^+-\bar y')d^+a_*^T. \tag{11}
\]

For B=3 and 0<eta<1/(6||H||_2^2), |f^+|<1/3 while |bar y'|>=1/3.
Every second batch therefore makes (11) nonzero. The lower increment
is nonzero as well: its common scalar mark factor is a nonzero multiple
of q dot b_1, phi'(aC)>0, and the first coordinate of its residual-
weighted input average is C(f^+-bar y'), which is nonzero. Thus all
three trained blocks participate after two steps. This is not a claim
that those motions follow the chosen cubic direction or fit the data.

## 4. Exact fitting is possible for the same data

Choose r in R^3 so the four scalars t_i=r dot u_i are distinct and
positive, for example r_2=1,r_3=2 and C r_1>2S. Set
w=e r, M=e_1q^T. The effective vectors are
v_i=kappa phi(t_i)e_1, with four distinct positive scalar slopes z_i.
The upper functions phi(z_i b_{2,1}) are linearly independent.
Indeed a linear relation on its positive-density interval extends to
an analytic identity; comparing the first four odd Taylor coefficients
gives a Vandermonde matrix in the distinct numbers z_i^2, multiplied
by nonzero z_i and the nonzero tanh coefficients 1,-1/3,2/15,-17/315.
Every coefficient must vanish.

Their four-by-four Gram is therefore positive definite. If K is that
Gram and y the label vector, the bounded odd readout
c=sum_i (K^{-1}y)_i phi(z_i b_{2,1}) fits all four labels exactly.
Thus the bad state is not forced by an architectural contradiction.
The construction proves representability; it is not a trained endpoint.

## 5. Interpretation and obligations

This exact p=1 example shows both the benefit and the limitation of the
minibatch idea. The cubic bad state is not absorbing for batches of
size three: its first step always moves and its second step changes
both hidden trainable blocks. But the noise initially acts only in a
stable quadratic direction and raises loss. A proof of eventual fitting
must control the subsequent coupled motion; the cubic directional loss
calculation alone does not provide that proof.

The example concerns an ambient state, with the original canonical
carriers and physical metric. Neither canonical reachability of this
state nor convergence from canonical initialization is asserted. The
data family has no parallel/antipodal obstruction and is exactly fittable.
All claims above are finite exact identities or constructions.

Status: complete lead candidate, awaiting independent check.
