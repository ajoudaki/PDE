# L=2 alternative route: a nonlinear-feature invariant and a sharp comparator defect

2026-09-08. Theory only; no experiments and no old files changed. This is an independently derived partial result, not the requested full population theorem.

## 1. A nonlinear reference with an exact Gram invariant

Freeze the initialized first-layer features `h_i = phi(Z_i)` for three inputs, and let `Q_ij = <h_i,h_j>`. Use an affine second activation with slope `a`, while training its matrix action `A` and the linear readout `C`. Thus

\[
f_i=a\langle C,Ah_i\rangle,\qquad
\dot A=a C\otimes\sum_i e_i h_i,\qquad
\dot C=a\sum_i e_i Ah_i,\qquad e=y-f.
\]

This is a deliberately different reference model; freezing the first layer is not part of the user’s model. Its merit is that the exact nonlinear initialized signal, including the input-Gram-null signal, is retained.

Suppose `Q` is positive definite and the initialized Gaussian action obeys its actual fixed-query identity

\[
\langle A_0h_i,A_0h_j\rangle=Q_{ij},\qquad C_0=0.
\]

The latter is the canonical population Gaussian initialization rule on the finite deterministic span of the three first-layer features. Define the operator `H:R^3 -> H_1` by `Hv=sum_i v_i h_i`, and

\[
B=AHQ^{-1/2},\qquad E=\operatorname{ran}B_0.
\]

Then `B_0^*B_0=I_3`, `dim E=3`, and the exact equations are

\[
\dot B=a C e^TQ^{1/2},\qquad
\dot C=a BQ^{1/2}e.
\]

They preserve `C in E` and `ran B subset E`, and differentiation gives

\[
                 BB^*-C\otimes C=P_E.                 \tag{1}
\]

Consequently `BB^*|_E=I_E+C tensor C`, so every singular value of `B` is at least one. Therefore the readout feature Gram satisfies the genuine all-time lower bound

\[
Q_{\rm out}=a^2Q^{1/2}B^*BQ^{1/2}\succeq a^2Q.       \tag{2}
\]

This is an invariant proved for this reference, not an assumed NTK floor. For `kappa=lambda_min(Q)`, its squared loss obeys

\[
\mathcal L(t)\le\mathcal L(0)e^{-2a^2\kappa t}.        \tag{3}
\]

There is also an all-time factor bound that is much sharper than the residual-length estimate. If `c=||C||`, then

\[
\|B^*C\|^2=c^2+c^4,
\qquad
\|f\|^2\ge a^2\kappa(c^2+c^4).
\]

Since loss decreases from `||y||^2/2`, `||f||<=2||y||=2sqrt(3)`, and hence

\[
c\le(12/(a^2\kappa))^{1/4},\qquad
\|B\|=\sqrt{1+c^2}.                                  \tag{4}
\]

The change of `A` vanishes on `ran H` perpendicular, and

\[
\|A-A_0\|\le\|B-B_0\|\le1+\sqrt{1+c^2}.
\]

The finite-dimensional equations on `E` therefore continue globally. This proves global strong existence and uniqueness for the reference itself. No compactness argument is needed.

For the odd first activation, the existing initialization calculation gives

\[
\kappa\ge\theta^2b_3^2\delta^2(2-\delta)^2/3.
\]

Thus the reference retains the missing nonlinear direction, fits at a rate of order `theta^2 delta^2`, and admits factor bounds of order `theta^{-1/2} delta^{-1/2}`. Its factor growth matches the square-root excursion scale of the L=2 singular-direction obstruction. This is a viable nonlinear reference in a much stronger sense than the stationary purely affine equilateral reference.

## 2. Why this reference cannot be imported as a small-amplitude comparison

The following calculation quantifies the omitted first-layer force, including the second-layer nonlinear activation of the true model.

Take the equilateral planar inputs

\[
\sum_{i=1}^3u_i=0,\quad \|u_i\|=1,\quad
u_i\cdot u_j=-1/2\ (i\ne j),\quad y_i=1.
\]

In the first Gaussian neuron space put

\[
Z_i=w\cdot u_i,\quad
T={1\over3}\sum_i\arctan Z_i,\quad
U={1\over3}\sum_i{u_i\over1+Z_i^2},\quad
\tau=\|T\|_2>0.
\]

Here `w` is a standard Gaussian in the input plane. Positivity of `tau` also follows from the cubic-chaos bound. Directly, at `(Z_1,Z_2,Z_3)=(t,t,-2t)`, `t>0`, `2 atan(t)-atan(2t)>0`; Gaussian measure has positive density on the plane. At that same point `U != 0`, because the three coefficients `1/(1+Z_i^2)` are not equal and the only relation among the three inputs is their sum. Continuity consequently proves

\[
                         \|TU\|_2>0.                 \tag{5}
\]

The frozen feature average is exactly

\[
v={1\over3}\sum_i h_i=\theta T,
\quad \mu=\|v\|=\theta\tau,
\quad e_0=v/\mu=T/\tau,
\quad p_0=A_0e_0,\quad\|p_0\|=1.
\]

Use ascent time for the reference mean prediction

\[
J=a\langle C,Av\rangle.
\]

The invariant one-feature subsystem solves explicitly as

\[
C=c p_0,\quad
A=A_0+(d-1)p_0\otimes e_0,
\quad c=\sinh(a\mu s),\quad d=\cosh(a\mu s),
\quad J=a\mu cd.                                     \tag{6}
\]

Fix any `j in (0,1)` and stop at the unique time `J=j`. Then

\[
c^2={\sqrt{1+4j^2/(a^2\mu^2)}-1\over2},
\quad a\theta c^2\longrightarrow {j\over\tau},
\quad {A^*C\over c^2}\longrightarrow e_0\quad\hbox{in }L^2,
                                                               \tag{7}
\]

as `theta downarrow 0`, with `a=1-theta`. The last assertion follows directly from

\[
A^*C=c A_0^*p_0+c(d-1)e_0,
\]

and boundedness of the initialized action. The corresponding clock is of order `theta^{-1} log(1/theta)`, and `c` is of order `theta^{-1/2}`.

Now release the first layer while temporarily keeping the second activation affine. The first raw gradient block of its mean prediction, expressed as the first-neuron input vector, is exactly

\[
\nabla_wJ={a\over3}(A^*C)\sum_i\phi'(Z_i)u_i
          =a\theta(A^*C)U.
\]

Therefore (7) gives the strong limit

\[
\nabla_wJ\longrightarrow {j\over\tau^2}TU,
\qquad
\lim_{\theta\downarrow0}\|\nabla_wJ\|_2
                  ={j\over\tau^2}\|TU\|_2>0.          \tag{8}
\]

So even before restoring the top nonlinearity, the omitted first-layer field does not tend to zero along the reference through a fixed nonzero prediction.

### Restoring the actual second activation does not remove this defect

At the reference state in (6), let

\[
\xi_i=A_0h_i,\qquad
z_i^2=\xi_i+(d-1)\mu p_0,\qquad g(z)=(1+z^2)^{-1}.
\]

The initialized upper joint Gaussian law of `(p_0,xi_1,xi_2,xi_3)` is invariant under input permutations. Thus

\[
\alpha_i=E[p_0^2g(z_i^2)]=\alpha\in[0,1]
\]

is independent of `i`. The incoming backward fields in the true activation are

\[
A^*\{C[a+\theta g(z_i^2)]\}
 =a A^*C+\theta c A_0^*[p_0g(z_i^2)]
                  +\theta c(d-1)e_0\alpha.
\]

Insert this into the exact bottom raw gradient, multiply by `phi'(Z_i)u_i/3`, and sum. The second displayed term contributes at most `K theta c = O(sqrt(theta))` in the raw `L^2` norm, since `|phi'|<=1`, `g<=1`, and `||A_0||` is bounded. The third term is independent of `i`; its linear gate cancels using `sum u_i=0`, and its remaining contribution is bounded by `K theta^2 c(d-1)=O(theta)`. Consequently, if `J_true` denotes the true mean prediction evaluated at this same reference state,

\[
\|\nabla_wJ_{\rm true}-\nabla_wJ\|_2\longrightarrow0.
                                                               \tag{9}
\]

Also

\[
|J_{\rm true}-J|\le (\pi/2)\theta\|C\|=O(\sqrt\theta).
\]

Sample symmetry makes the three true predictions agree at this state. Hence the full physical GF bottom block equals `3(1-J_true) grad_w J_true`, and (8)--(9) imply

\[
\dot w_{\rm true}\longrightarrow
              {3j(1-j)\over\tau^2}TU\ne0
\quad\hbox{in the raw Hilbert norm}.                  \tag{10}
\]

The frozen reference bottom block is identically zero. Thus the true and reference vector fields differ by a nonvanishing amount before interpolation, uniformly along any reference program that includes its fixed level `J=j`.

All limits above compare vector fields at explicitly constructed reference states. They do not assert existence of a true trajectory through those states, nor assert that the true trajectory is far from the reference. A nonvanishing field defect does not by itself exclude a stable comparison theorem.

## 3. Precise contribution and remaining bridge

Established: an exact nonlinear-feature reference retaining all three initialized directions, a proved Gram invariant, global reference fitting, the correct square-root factor scale, and an exact nonvanishing first-layer defect when that reference is used for the actual model.

Not established: a positive Gram invariant for the actual model, a response-tail theorem for its uncut flow, its strong construction/uniqueness/restart, or any of the required full-width GF/raw-GD convergence conclusions.

The reference route needs an estimate that treats the bottom dynamics at leading order, or a stability theorem able to absorb the explicit order-one field in (10). A comparison based on a uniformly vanishing `theta`-amplitude difference throughout the learning clock cannot use this frozen reference. This is a failure of that particular perturbative certificate, not a counterexample to the positive-theta theorem.
