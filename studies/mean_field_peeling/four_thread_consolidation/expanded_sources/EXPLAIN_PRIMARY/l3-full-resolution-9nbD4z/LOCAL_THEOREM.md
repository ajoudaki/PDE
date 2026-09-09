# Unconditional local three-hidden-layer limit: assembled statement

This is the statement assembled from the six proof notes listed below.
It is a local theorem, not the requested all-finite-time theorem.
The combined statement is currently undergoing independent adversarial
review. A proof of global continuation has not been obtained.

## Network, exact algorithm, and interval

There is one input and one target, both equal to one. All three hidden
layers have width \(n\). The first preactivation \(z^{(1)}\) and the
rescaled readout \(W^{(4)}\) are \(n\)-vectors. The two hidden matrices
\(W^{(2)},W^{(3)}\) are \(n\) by \(n\). With \(\phi=\arctan\), set
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 f_n=\frac{(W^{(4)})^\top h^{(3)}}n,\qquad
 r_n=f_n-1,\qquad L_n=r_n^2,
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot(W^{(3)})^\top\delta^{(3)},\quad
 \delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)}.
 \tag{1}
\]
The initialization blocks are independent, with
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{2}
\]
Use the exact raw updates, with \(\eta_n=n^{-2}\),
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,
\]
\[
 W^{(\ell)}_{k+1}
 =W^{(\ell)}_k-\frac{2\eta_n r_{n,k}}n
           \delta^{(\ell)}_k(h^{(\ell-1)}_k)^\top,
 \qquad\ell=2,3,
\]
\[
 W^{(4)}_{k+1}=W^{(4)}_k-2\eta_n r_{n,k}h^{(3)}_k.
 \tag{3}
\]
Physical time is \(t=k\eta_n\). Between these times interpolate the
raw parameters linearly and recompute all hidden preactivations and
features from the interpolated parameters. Finite gradient flow
means the differential equations with the same right-hand sides
divided by \(\eta_n\).
At GD mesh nodes, velocities mean right-hand derivatives; use the
left-hand derivative at \(T_0\) if it is a terminal mesh node.

Here is one explicit, very conservative positive interval. Let
\[
 a=\pi/2,\quad A=a^2+e,\quad
 M_p=2^{1/p}\exp\!\big(A(2a+1)+2pA^2a^2\big)\quad(p=1,2),
\]
\[
 A_3=a^2+AM_1,\quad
 C_3=(1+2a)\exp((1+2a)A_3)+a^2,\quad Q=a(1+C_3),
\]
\[
 C_2=(2Q+C_3)M_2+Q^2,\qquad
 S_0=\min\{1,(2C_2)^{-1},(2C_3)^{-1}\},\qquad
 T_0=\frac14\min\{S_0,(4a^2)^{-1}\}.
 \tag{4}
\]
The constants are deliberately not optimized. They are finite explicit
numbers determined by \(\arctan\), not by an unproved continuation
or moment assumption.

## Conclusions on this interval

There are three fixed neuron probability spaces, with bounded initial
matrix actions \(W^{(2)}_0,W^{(3)}_0\) and their reverse actions.
They are constructed from the joint limits of finite Gaussian matrix
calculations, preserving every reused transpose. There is a unique
local uncut population state
\[
 X^{(1)}(t),\qquad W^{(2)}(t),\qquad
 W^{(3)}(t),\qquad W^{(4)}(t),\qquad 0\le t\le T_0.
 \tag{5}
\]
Here \(X^{(1)}=F(Z^{(1)})\), \(F(z)=z+z^3/3\);
the two matrices are bounded actions between the adjacent population
spaces; and the readout is the typical population coordinate.
Initially \(Z^{(1)}_0\) is standard Gaussian and \(W^{(4)}_0=0\).
This is a finite list of evolving fields and operators, not a
finite-scalar description.

Use (1) on these spaces, replacing finite transposes by their reverse
actions, denoted by a star, and using ordinary pointwise products.
Then
\[
 f=E_3[W^{(4)}H^{(3)}],\quad r=f-1,\quad L=r^2,
\]
\[
 \frac{dX^{(1)}}{dt}=-2r\,(W^{(2)})^*\delta^{(2)},\quad
 \frac{dW^{(2)}}{dt}=-2r\,\delta^{(2)}\otimes H^{(1)},
\]
\[
 \frac{dW^{(3)}}{dt}=-2r\,\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{dt}=-2r\,H^{(3)}.                       \tag{6}
\]
The rank-one action is explicitly
\((U\otimes V)B=U E[VB]\).
Uniqueness holds among continuous integral solutions on these fixed
spaces with bounded operator and mean-square parameter norms.
The same uniqueness holds when restarting from a reached state on
any remaining subinterval of the constructed interval.

In the raw coordinate \(Z^{(1)}\), (6) is the gradient flow of
\(L\): use ordinary mean-square lengths for the vector fields and
the square-summed matrix length for trained matrix changes.
The present state alone determines its derivatives; the Gaussian
response coefficients in the proof are not prescribed external
inputs to its evolution.

For each fixed same-layer finite list of network measurements,
the joint empirical law of both finite GD and finite gradient flow
converges uniformly in \(t\in[0,T_0]\), in probability, to the
corresponding population law. Convergence includes second moments.
The class includes finite compositions of the current states,
globally Lipschitz coordinate functions, bounded products, and
both orientations of both current matrices; finitely many specified
times may be used jointly. It also includes the named backward
fields in (1) and the hidden preactivation and feature velocities.
No coordinatewise pairing across distinct hidden layers is asserted.

Equivalently, for any such finite same-layer coordinate list and any
fixed continuous measurement \(\psi\) of at most quadratic growth,
its empirical average approaches its population expectation uniformly
in time. Thus prediction, residual, and loss converge uniformly.
The four finite kernel blocks
\[
 \frac{\|\delta^{(1)}\|_2^2}{n},\qquad
 \frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2},\qquad
 \frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2},\qquad
 \frac{\|h^{(3)}\|_2^2}{n}
 \tag{7}
\]
converge uniformly to the expectation formulas in
LOCAL_GRADIENT_STRUCTURE.md.
For every hidden layer, the empirical law of its entire preactivation
path converges, including second moments of the supremum norm, to
the law of its population path. Integrated squared velocities
converge to the corresponding population integrals.

With the same finite initialization, GD and finite gradient flow
also approach one another uniformly in the state distance consisting
of the normalized Euclidean difference in \(F(z^{(1)})\), the two
matrix operator-norm differences, and the normalized Euclidean
readout difference. No operator-norm comparison across different
widths or between different underlying spaces is asserted.

Every hidden layer learns a nonconstant feature trajectory.
More precisely, there are nonzero square-integrable variables
\(V^{(\ell)}\) such that
\[
 Z^{(\ell)}(t)-Z^{(\ell)}_0=2t^2V^{(\ell)}+o(t^2),\qquad
 H^{(\ell)}(t)-H^{(\ell)}_0
   =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2)
 \tag{8}
\]
in mean square, and both displayed leading variables have positive
mean-square size. The three hidden kernel blocks are positive
constant multiples of \(t^2+o(t^2)\); hidden feature squared-speed
integrals have positive \(T^3\) leading coefficients. Explicit
initial Gaussian formulas are given in LOCAL_FEATURE_LEARNING.md.
The total kernel is nonconstant, the loss decreases, and the
activation's best affine-approximation error on each hidden
distribution remains strictly positive on a common initial interval.

## How the premises are discharged

The proof is the following chain of proved lemmas, not a list of
additional assumptions on the original network.

1. L3_FIXED_MESH_SOURCE_IDENTIFICATION.md proves the exact finite
   Gaussian source representation, including both independent
   matrices, both transposes, empirical training feedback, and
   singular covariance cases.
2. LOCAL_ACTION_SPACE_AND_FLOW.md realizes those finite calculations
   on common population spaces and proves the fixed-clipping flow
   and its fixed-clipping width limit.
3. LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md proves a tail bound uniform
   in the Euler mesh and clipping level on the explicit \(S_0\).
   Its displayed scalar equations are precisely the equations
   proved in item 1 and realized by item 2.
4. LOCAL_CUTOFF_BRIDGE.md uses this bound to remove clipping,
   prove local uniqueness and restartability, and establish
   convergence from the actual raw GD, not merely from a
   transformed or population-feedback scheme. In particular its
   stated representation premise is discharged by items 1--3.
5. LOCAL_GRADIENT_STRUCTURE.md proves that the resulting autonomous
   evolution is a genuine gradient flow with all four kernel
   contributions.
6. LOCAL_FEATURE_LEARNING.md derives the strictly nonzero initial
   hidden movement from this flow and the initial Gaussian action
   laws. Its local-flow premise is discharged by items 1--5.

Independent reviews are checking both the individual lemmas and
the compatibility of this chain. None of these statements proves
the all-finite-time continuation requested in the main goal.
