# A finite moving-flow Taylor recurrence through order three

## Specification and claim

Fix hidden depth \(L=2\), one sample \(m=1\), positive integers \(n,d\),
an input \(x_1\in\mathbb R^d\), a label \(y_1\in\mathbb R\), and constant
positive multipliers \(\kappa_1,\kappa_2,\kappa_3\). The input Gram entry is
\(G_{11}=x_1^Tx_1/d\); it need not be one or positive. Both hidden layers
use the same scalar activation \(\phi\in C^3(\mathbb R)\). No distributional
assumption is imposed on the finite initial weights.

The stored weights are \(W^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(2)}\in\mathbb R^{n\times n}\), and
\(W^{(3)}\in\mathbb R^n\). For the sole sample, suppress the sample index
on hidden and backward fields. Use first-layer neuron index \(j\),
second-layer neuron index \(i\), and input-coordinate index \(\alpha\):

\[
\begin{aligned}
z_j^{(1)}&=\frac1{\sqrt d}\sum_{\alpha=1}^d W_{j\alpha}^{(1)}x_{1,\alpha},
&h_j^{(1)}&=\phi(z_j^{(1)}),\\
z_i^{(2)}&=\sum_{j=1}^n W_{ij}^{(2)}h_j^{(1)},
&h_i^{(2)}&=\phi(z_i^{(2)}),\\
f_{n,1}&=\frac1n\sum_{i=1}^n W_i^{(3)}h_i^{(2)},
&r_1&=f_{n,1}-y_1,\qquad \mathcal L_n=r_1^2.
\end{aligned}                                                    \tag{J1}
\]

In particular no extra width factor occurs in the hidden forward action.
The residual-free backward fields are

\[
\delta_i^{(2)}=W_i^{(3)}\phi'(z_i^{(2)}),\qquad
\delta_j^{(1)}=\phi'(z_j^{(1)})\sum_{i=1}^n W_{ij}^{(2)}\delta_i^{(2)}.
                                                               \tag{J2}
\]

The same entry \(W_{ij}^{(2)}\) in (J1) appears in (J2); the two actions
are \(W^{(2)}\) and its actual transpose. No identification of first- and
second-layer neurons is made even though their cardinalities agree.

Let \(t\) be physical time, with all raw blocks moving according to
\(\dot\theta=-D\nabla\mathcal L_n\), where the first, middle, and readout
blocks of the constant mobility \(D\) are multiplication by
\(n\kappa_1,\kappa_2,n\kappa_3\), respectively. Then

\[
\begin{aligned}
\dot W^{(1)}&=-\frac{2\kappa_1}{\sqrt d}\,r_1\delta^{(1)}x_1^T,\\
\dot W^{(2)}&=-\frac{2\kappa_2}{n}\,r_1\delta^{(2)}(h^{(1)})^T,\\
\dot W^{(3)}&=-2\kappa_3 r_1h^{(2)}.
\end{aligned}                                                    \tag{J3}
\]

For an integer \(0\le R\le3\), the recurrence below computes the
ordinary coefficients \(v_k=v^{(k)}(0)/k!\), \(0\le k\le R\), of all
three weight blocks, both forward preactivations and activations, and the
output along (J3). Here the expansion point is any supplied finite state;
calling its time zero does not require it to be a random initialization.
Backward coefficients are needed only through \(R-1\).

All identities in this specification concern real arithmetic. Their
evaluation with floating-point arrays is a numerical oracle for these
coefficients, not exact arithmetic, a population law, or an exact
positive-time solution.

## Elementary algebra of ordinary coefficients

Write \(v(t)=\sum_{k=0}^R v_k t^k+o(|t|^R)\) for a \(C^R\) field,
with the usual continuous-value interpretation when \(R=0\). For any
fixed bilinear operation \(B\) between finite-dimensional spaces,

\[
[B(u,v)]_k=\sum_{p=0}^k B(u_p,v_{k-p}).                          \tag{J4}
\]

Indeed multiply the two finite expansions: the products of powers with
total degree \(k\) have exactly the displayed indices. Their remainders
are \(o(|t|^R)\), because the retained polynomials are locally bounded.
The rule applies entrywise to scalar multiplication, Hadamard products,
matrix products, outer products, and row-vector pairings. Finite sums
commute with coefficient extraction, and
\([(W^{(2)})^T]_k=(W_k^{(2)})^T\).

For a scalar function \(\psi\in C^q\), \(0\le q\le3\), use the following
coordinatewise composition coefficients only at degrees at most \(q\):

\[
\begin{aligned}
\mathcal C_0(\psi,z)&=\psi(z_0),\\
\mathcal C_1(\psi,z)&=\psi'(z_0)\odot z_1,\\
\mathcal C_2(\psi,z)&=\psi'(z_0)\odot z_2
 +\tfrac12\psi''(z_0)\odot z_1^{\odot2},\\
\mathcal C_3(\psi,z)&=\psi'(z_0)\odot z_3
 +\psi''(z_0)\odot z_1\odot z_2
 +\tfrac16\psi'''(z_0)\odot z_1^{\odot3}.
\end{aligned}                                                    \tag{J5}
\]

To verify (J5), put \(e(t)=z(t)-z_0\). Scalar Taylor expansion gives
\(\psi(z_0+e)=\psi(z_0)+\psi'(z_0)e+\psi''(z_0)e^2/2
+\psi'''(z_0)e^3/6+o(|e|^3)\). At positive truncation order,
\(e=O(|t|)\). The degree-two and degree-three terms of \(e^2\) are
\(z_1^{\odot2}\) and \(2z_1\odot z_2\), and the degree-three term of
\(e^3\) is \(z_1^{\odot3}\). Substitution proves each line, including
the lower-order versions obtained by truncation. Applying (J5) to
\(\psi=\phi'\) only for degrees at most two requires derivatives of
\(\phi\) through order three, not four.

## Recurrence

Initialize \(W_0^{(1)},W_0^{(2)},W_0^{(3)}\) to the supplied raw state.
At each degree \(k=0,\ldots,R\), do the following forward sweep:

\[
\begin{aligned}
z_k^{(1)}&=W_k^{(1)}x_1/\sqrt d,
&h_k^{(1)}&=\mathcal C_k(\phi,z^{(1)}),\\
z_k^{(2)}&=\sum_{p=0}^k W_p^{(2)}h_{k-p}^{(1)},
&h_k^{(2)}&=\mathcal C_k(\phi,z^{(2)}),\\
f_{n,1;k}&=\frac1n\sum_{p=0}^k (W_p^{(3)})^Th_{k-p}^{(2)}.
\end{aligned}                                                    \tag{J6}
\]

If \(k=R\), stop. Otherwise form
\(r_{1;k}=f_{n,1;k}-\mathbf1_{\{k=0\}}y_1\), and compute

\[
\begin{aligned}
\delta_k^{(2)}
 &=\sum_{p=0}^k W_p^{(3)}\odot\mathcal C_{k-p}(\phi',z^{(2)}),\\
\delta_k^{(1)}
 &=\sum_{a+b+c=k}
   \mathcal C_a(\phi',z^{(1)})\odot (W_b^{(2)})^T\delta_c^{(2)}.
\end{aligned}                                                    \tag{J7}
\]

All indices in a sum of degrees are nonnegative integers. With these
coefficients, update the next degree of every weight block:

\[
\begin{aligned}
W_{k+1}^{(1)}
 &=-\frac{2\kappa_1}{(k+1)\sqrt d}
       \sum_{a+b=k} r_{1;a}\delta_b^{(1)}x_1^T,\\
W_{k+1}^{(2)}
 &=-\frac{2\kappa_2}{(k+1)n}
       \sum_{a+b+c=k} r_{1;a}\delta_b^{(2)}(h_c^{(1)})^T,\\
W_{k+1}^{(3)}
 &=-\frac{2\kappa_3}{k+1}
       \sum_{a+b=k} r_{1;a}h_b^{(2)}.
\end{aligned}                                                    \tag{J8}
\]

There is no circular dependence at a given degree. The weight coefficients
through \(k\) are available before (J6); the first layer of (J6) precedes
the second. Equation (J7) uses that forward sweep and already available
weights. Equation (J8) then creates the next weight coefficients. When
\(R=0\) only (J6)'s values are computed. For \(R>0\), (J7)'s largest
degree is \(R-1\), so its largest activation derivative is \(\phi^{(R)}\).
The terminal (J6) also uses derivatives only through \(\phi^{(R)}\).

In coordinates, the transpose contribution in (J7) is explicitly

\[
(\delta_k^{(1)})_j
=\sum_{a+b+c=k}\mathcal C_a(\phi',z^{(1)})_j
                    \sum_{i=1}^n (W_b^{(2)})_{ij}(\delta_c^{(2)})_i.
                                                               \tag{J9}
\]

Terms with \(b>0\) retain trained-weight contributions. Replacing this
matrix by \(W_0^{(2)}\), using an independent reverse matrix, or deleting
positive-degree residual coefficients changes the recurrence.

## Proof that these are moving physical-flow coefficients

First verify (J3). Differentiating (J1) with respect to the final
preactivation gives \(\partial f_{n,1}/\partial z_i^{(2)}
=\delta_i^{(2)}/n\). Differentiating through the second layer gives
\(\partial f_{n,1}/\partial z_j^{(1)}=\delta_j^{(1)}/n\) by (J2).
Consequently the ordinary matrix and vector gradients are

\[
\nabla_{W^{(1)}}f_{n,1}=\delta^{(1)}x_1^T/(n\sqrt d),\quad
\nabla_{W^{(2)}}f_{n,1}=\delta^{(2)}(h^{(1)})^T/n,\quad
\nabla_{W^{(3)}}f_{n,1}=h^{(2)}/n.
\]

The derivative of \(r_1^2\) is \(2r_1\nabla f_{n,1}\). Multiplying each
gradient by its negative mobility proves (J3), including every width,
input, and loss factor.

For completeness, a local \(C^3\) solution exists and is unique without
any probabilistic argument. The finite vector field \(V\) in (J3) is
\(C^2\), since its factors involve \(\phi\) and \(\phi'\). On a small
closed Euclidean ball around the initial state its norm is bounded by
\(B\) and its first derivative by \(M\). Integration along a segment in
the ball gives \(\|V(u)-V(v)\|\le M\|u-v\|\). Choose a time radius
\(a>0\) with \(aB\) smaller than the ball radius and \(aM<1\).
For curves in the ball, the map
\(u\mapsto\theta_0+\int_0^t V(u(s))\,ds\), \(|t|\le a\), stays in
the ball and decreases the sup norm of differences by a factor at most
\(aM\). Iterating from the constant curve gives successive differences
bounded by a geometric series, hence a uniformly convergent curve. The
Lipschitz bound permits passage through the integral; its limit solves
the integral equation. Two solutions have sup norm difference at most
\(aM\) times that difference, hence agree. The integral equation first
gives a \(C^1\) solution. Substituting into the \(C^2\) vector field and
using the chain rule twice gives a \(C^3\) solution. The forward fields
and output are \(C^3\) by composition.

We now prove correctness by induction on degree. At degree zero, (J6)
is the defining network evaluation (J1). Assume that the algorithm has
the true coefficients of every weight through degree \(k\), and all
previously computed fields. The first equation of (J6) is a linear
contraction of the weight and fixed input, so has the true degree-\(k\)
coefficient. Equation (J5) proves the first activation coefficient.
Equation (J4) applied to \(W^{(2)}h^{(1)}\) proves the next
preactivation coefficient, and (J5) proves its activation coefficient.
Finally (J4) applied to the readout pairing proves \(f_{n,1;k}\).
Subtracting the fixed label only at degree zero gives the true residual
coefficient.

If \(k<R\), apply (J4) to (J2) and (J5) to its two activation derivatives.
This yields precisely (J7), including the derivative coefficients of the
transpose. Apply (J4) again to each product on the right of (J3); its
degree-\(k\) coefficient is the corresponding numerator of (J8). The
left side has degree-\(k\) coefficient \((k+1)W_{k+1}^{(\ell)}\).
Equating coefficients proves (J8). Thus all newly created weights are
correct, closing the induction up to \(R\). No higher derivative is
needed to justify the last step: when \(R=3\) the vector field is
expanded only through degree two.

In particular these coefficients have the finite Taylor interpretation
\(v(t)=\sum_{k=0}^R v_k t^k+o(|t|^R)\). A stronger
\(O(|t|^{R+1})\) remainder, a convergent infinite series, and a uniform
bound in width do not follow from this proof.

## Relation to feature ascent and raw normalization

Feature ascent with these same mobilities is the separately defined flow
\(d\theta/ds=D\nabla f_{n,1}(\theta)\). Its raw equations are

\[
\frac{dW^{(1)}}{ds}=\kappa_1\delta^{(1)}x_1^T/\sqrt d,\quad
\frac{dW^{(2)}}{ds}=\kappa_2\delta^{(2)}(h^{(1)})^T/n,\quad
\frac{dW^{(3)}}{ds}=\kappa_3h^{(2)}.
                                                               \tag{J10}
\]

The scalarized first coordinate obeys
\(dz^{(1)}/ds=\kappa_1G_{11}\delta^{(1)}\). Its factor \(G_{11}\) is
forced by the raw first matrix and input, and is not an independent
normalization parameter. If one instead stores the auxiliary matrix
\(\widehat W^{(2)}=\sqrt n W^{(2)}\), then
\(z^{(2)}=\widehat W^{(2)}h^{(1)}/\sqrt n\) and
\(d\widehat W^{(2)}/ds=\kappa_2\delta^{(2)}(h^{(1)})^T/\sqrt n\).
This is a coordinate change; it introduces no extra factor into (J1).
With unit multipliers, the mobility in the coordinates
\((W^{(1)},\widehat W^{(2)},W^{(3)})\) is multiplication by \(n\) in
every block.

Physical time satisfies \(ds/dt=-2r_1\). On intervals where this is
positive it is the increasing feature-time change. At \(r_1=0\),
(J3) has zero vector field; the unique local physical solution is
constant, and all its positive-order coefficients vanish. The recurrence
handles this case directly without dividing by \(r_1\).

It is not sufficient to rescale the \(k\)-th feature derivative by the
\(k\)-th power of the initial clock speed. To see the missing terms,
let \(F(s)=f_{n,1}(\theta(s))\), and write \(b=-2r_1(0)\).
At the expansion point, \(s'=b\), \(s''=-2bF'\), and
\(s'''=-2b^2F''+4b(F')^2\), obtained by differentiating
\(s'=-2(F(s)-y_1)\) twice. The chain rule gives physical derivatives

\[
\begin{aligned}
\dot f_{n,1}&=bF',\\
\ddot f_{n,1}&=b^2F''-2b(F')^2,\\
f_{n,1}^{(3)}&=b^3F'''-8b^2F'F''+4b(F')^3.
\end{aligned}                                                    \tag{J11}
\]

Equation (J8) incorporates these clock effects by retaining the moving
residual before every coefficient update. It also retains acceleration
and higher weight coefficients; evaluating the network on the straight
line \(\theta_0+t\dot\theta_0\) would discard them.

## Numerical interface and claim boundary

`pde.finite_jets.flow_jet(parameters, inputs, labels,
activation_derivative, order=R, kappas=...)` implements (J6)--(J8).
`inputs` has shape `(d,1)` and `labels` has shape `(1,)`. Its result has
`parameter_coefficients[k]` in raw `Parameters` storage; each array in
`preactivation_coefficients` and `hidden_coefficients` has shape
`(R+1,n,1)`, with tuple positions zero and one corresponding to layers
one and two. `output_coefficients[k,0]` is \(f_{n,1;k}\), and
`output_derivatives[k,0]` is its factorial multiple.

The derivative callback receives `(j,z)` with \(0\le j\le R\), and
must return the true coordinatewise \(\phi^{(j)}(z)\) as a real finite
array of the same shape `(n,1)`. Each call receives a private copy of
the initial preactivation; its returned array is copied immediately.
This permits in-place callbacks and reusable output buffers without
altering the initial coordinates or earlier derivatives. Consistency,
coordinatewise semantics, and \(C^3\) regularity cannot be certified
by shape and finiteness checks; they are requirements on the caller.
Callbacks must not mutate unrelated external state of the calculation.

Parameter and argument validation follows the finite numerical contract.
Only the evaluated degrees are required to be representable: no terminal
backward field, loss value, or unused residual is constructed. Raw first
matrix contraction precedes division by \(\sqrt d\). Scalar mobility,
normalization, and degree factors are combined using mantissa/exponent
multiplication. This avoids premature range loss for those factors but
does not protect raw matrix products, convolution sums, or composition
powers from overflow, underflow, or cancellation. Nonfinite evaluated
coefficients are rejected. An unrepresentable factorial multiple is
rejected when output derivatives are requested. There is no
correct-rounding or universal extreme-range guarantee.

For bounded \(R\le3\), storage and algebraic work are \(O(nd+n^2)\),
in addition to callback costs, with constants depending on the degree. No
Gaussian initialization, expectation, width extrapolation, population
closure, infinite-order calculus, or positive-time error estimate is
part of this result. In particular the finite deterministic recurrence
applies both to order-one and small stored readouts without identifying
their different population initialization regimes.
