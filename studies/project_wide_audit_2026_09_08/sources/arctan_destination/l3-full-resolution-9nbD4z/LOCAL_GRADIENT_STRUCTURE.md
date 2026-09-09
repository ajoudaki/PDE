# The local limit is an actual gradient flow

This note supplies the gradient assertion once the uncut local
solution has been constructed. It introduces no additional
existence or tail premise.

Use the three population spaces and matrix actions in
LOCAL_ACTION_SPACE_AND_FLOW.md. Averages in a layer are denoted by
\(E_\ell\). Retain the forward equations
\[
 H^{(1)}=\phi(Z^{(1)}),\quad
 Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),\quad
 Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}).
\]
Set
\[
 f=E_3[W^{(4)}H^{(3)}],\qquad r=f-1,\qquad L=r^2,
\]
\[
 \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),\quad
 \delta^{(2)}=\phi'(Z^{(2)})(W^{(3)})^*\delta^{(3)},\quad
 \delta^{(1)}=\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)}.
 \tag{1}
\]
The derivatives exclude the residual. Each belongs to its layer's
mean-square space, since the gates are bounded and the matrix
actions are bounded.

The trained changes of \(W^{(2)},W^{(3)}\) are square-summable
operators, even though the initial Gaussian actions need not be.
Precisely, the size of a square-summable operator \(A\) is
\[
 \|A\|_{\rm HS}^2=\sum_j\|Ae_j\|_{L^2}^2,
\]
for any orthonormal basis of its input space; this sum does not
depend on the basis. This is the population counterpart of a
matrix's ordinary squared Frobenius norm. For the rank-one action
\((U\otimes V)B=U E[VB]\), the size is
\(\|U\otimes V\|_{\rm HS}=\|U\|_{L^2}\|V\|_{L^2}\).
An integral of the continuous rank-one velocities therefore has
finite HS size on a bounded time interval.

To justify this assertion for the cutoff limit as well, the
comparison estimate in LOCAL_CUTOFF_BRIDGE.md proves uniform
mean-square convergence of \(\delta^{(2)}_R\) and
\(\delta^{(3)}_R\) to their uncut values, as well as convergence
of \(H^{(1)}_R,H^{(2)}_R\). The rank-one difference inequality
holds in HS norm just as in operator norm. Thus the integrals of
the matrix velocities converge in HS norm. Their limits are the
same matrix actions already obtained in operator norm.

Consider the raw parameter space with coordinates
\[
 (Z^{(1)},\,W^{(2)}-W^{(2)}_0,\,
 W^{(3)}-W^{(3)}_0,\,W^{(4)}).
\]
Its squared length for a variation is
\[
 E_1[(dZ^{(1)})^2]
 +\|dW^{(2)}\|_{\rm HS}^2
 +\|dW^{(3)}\|_{\rm HS}^2
 +E_3[(dW^{(4)})^2].                                   \tag{2}
\]
All affine states in this space have bounded matrix actions:
the HS size bounds the operator norm of each trained change.

The predictor is differentiable in the norm (2). Here is the
needed elementary remainder argument, avoiding an incorrect
claim that every pointwise nonlinearity is differentiable as a
map from all of \(L^2\) to \(L^2\). For any fixed \(B\in L^2\),
the bounded first and second derivatives of \(\phi\) give
\[
 \begin{aligned}
 &\left|E B[\phi(Z+e)-\phi(Z)-\phi'(Z)e]\right|\\
 &\quad\le C R\,E e^2
       +2\|B\,\mathbf1_{\{|B|>R\}}\|_{L^2}\|e\|_{L^2}.
 \end{aligned}                                         \tag{3}
\]
On \(|B|\le R\) use the quadratic Taylor remainder; on the
complement use its bound \(2|e|\). First fix \(R\) and send
\(\|e\|_{L^2}\) to zero, then send \(R\) to infinity. The
remainder in (3) is \(o(\|e\|_{L^2})\).

Successive forward differences are \(O(\|d\theta\|)\) in mean
square: use bounded activations, Lipschitz \(\phi\), bounded
matrix actions, and
\(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\).
Expand the scalar predictor from the top layer downward.
At each layer apply (3) with the fixed backward coefficient at
the original state. Terms containing both a matrix change and
an activation change are \(O(\|d\theta\|^2)\), by the operator
inequality and Cauchy--Schwarz. The same is true of the product
of a readout change and a top activation change. This proves
the norm derivative
\[
 \begin{aligned}
 df={}&E_1[\delta^{(1)}dZ^{(1)}]
 +E_2[\delta^{(2)}\,dW^{(2)}H^{(1)}]\\
 &+E_3[\delta^{(3)}\,dW^{(3)}H^{(2)}]
 +E_3[H^{(3)}dW^{(4)}].
 \end{aligned}                                         \tag{4}
\]
Equivalently its gradient in (2) is
\[
 \nabla f=
 \left(\delta^{(1)},\,
       \delta^{(2)}\otimes H^{(1)},\,
       \delta^{(3)}\otimes H^{(2)},\,
       H^{(3)}\right).                                 \tag{5}
\]
The rank-one entries follow from the identity
\(\langle U\otimes V,A\rangle_{\rm HS}=E[U\,AV]\).
The gradient is continuous. For example, bounded gates converging
in probability multiply a fixed \(L^2\) variable continuously
in \(L^2\), by truncating that fixed variable; combine this
observation with forward continuity and reverse operator bounds
in (1). Local Lipschitz continuity of the uncut gradient is
neither asserted nor needed for the differentiability claim.

The already constructed feature-time solution has
\(X^{(1)}=F(Z^{(1)})\) and
\(dX^{(1)}/ds=(W^{(2)})^*\delta^{(2)}\).
Since \((F^{-1})'(F(z))=\phi'(z)\), its raw first coordinate
satisfies \(dZ^{(1)}/ds=\delta^{(1)}\) in mean square.
One direct chain-rule justification uses coordinate absolute
continuity and the bound \(|(F^{-1})'|\le1\), then approximates
the mean-square velocity by bounded variables. This also gives
mean-square continuity of the resulting velocity.
Together with the other three integral equations, (5) yields
\[
 \frac{d\theta}{ds}=\nabla f(\theta).                    \tag{6}
\]

On the local interval chosen in LOCAL_CUTOFF_BRIDGE.md,
\(|f|<1\). Its physical clock solves
\(ds/dt=2(1-f)\). Hence the physical evolution is exactly
\[
 \frac{d\theta}{dt}=-2r\,\nabla f=-\nabla L.             \tag{7}
\]
In particular, the derivative of its predictor is
\[
 \frac{df}{dt}=-2r\,\kappa,\qquad
 \frac{dL}{dt}=-4r^2\kappa,
\]
where the four nonnegative kernel contributions are
\[
 \begin{aligned}
 \kappa_1&=E_1[(\delta^{(1)})^2],\\
 \kappa_2&=E_2[(\delta^{(2)})^2]\,E_1[(H^{(1)})^2],\\
 \kappa_3&=E_3[(\delta^{(3)})^2]\,E_2[(H^{(2)})^2],\\
 \kappa_4&=E_3[(H^{(3)})^2],\qquad
 \kappa=\kappa_1+\kappa_2+\kappa_3+\kappa_4.
 \end{aligned}                                         \tag{8}
\]

This state is autonomous: the present four objects determine
every quantity in (1), then determine the four velocities.
The Gaussian response coefficients used to prove the limit are
not external inputs to (7). Both initial matrix actions and all
their trained changes are contained in the current matrix
operators. Local uniqueness and restartability on the constructed
interval are supplied by the cutoff comparison, not by a claim
that the uncut gradient is locally Lipschitz.

Nothing in this note proves that the local solution can be
continued to every finite physical time. That is a separate
outstanding part of the requested theorem.
