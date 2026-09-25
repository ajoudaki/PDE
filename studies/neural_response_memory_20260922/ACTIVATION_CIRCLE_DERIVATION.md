# Activation-general three-layer chronological moment closure

Date: 2026-09-25. Status: scoped author derivation for the explicitly requested
continuation of this study. The finite construction and covariance identities
below are exact under the stated trajectory assumptions. Accuracy of P=1,2,3,
nonsmooth solver convergence, hierarchy convergence and width-uniform estimates
are separate questions. No experiment was run by this author.

The change is to use ReLU, exact GELU, standard SELU or logistic sigmoid in all
three hidden layers, preserving the architecture, initialization, mobilities
and activity clock of `DEEP_CIRCLE_DERIVATION.md`. The selected circle tasks
are the eight-point two-outliers alternating task and quadrant alternating
task in `DEEP_CIRCLE_PROTOCOL.md` and `DEEP_CIRCLE_RESULTS.md`. Their previous
tanh results motivate task selection but supply no target trajectory or
coefficients to this closure. The current experiment protocol owns numerical
budgets, stopping criteria and accuracy gates.

The derivation first specifies the activation and selected derivative, derives
the physical backward equations, then applies the same history projection to
both internal links. Differentiating that projection identifies its two exact
covariance defects. The final sections distinguish smooth and nonsmooth
dynamics and state precisely which response lifts are available.

## 1. Activations and derivative conventions

All activation maps act componentwise. Write `phi'` for the ordinary derivative
where it exists and for the following explicitly selected value at a kink.
That selected value defines reverse-mode evaluation there; it is not a claim
that the ordinary derivative exists.

For ReLU,

\[
 \phi(z)=\max(0,z),\qquad
 \phi'(z)=\begin{cases}1&z>0,\\0&z\le0.\end{cases}
 \tag{1}
\]

For exact GELU, let
\(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and
\(\Phi(z)=\int_{-\infty}^z\varphi(v)\,dv\). Then

\[
 \phi(z)=z\Phi(z),\qquad
 \phi'(z)=\Phi(z)+z\varphi(z).
 \tag{2}
\]

The derivative is the product rule and \(\Phi'=\varphi\). In particular,
\(\phi'(0)=1/2\); `approximate="none"` specifies this activation rather than
the tanh approximation. See the official
[ReLU](https://docs.pytorch.org/docs/2.9/generated/torch.nn.ReLU.html) and
[GELU](https://docs.pytorch.org/docs/2.9/generated/torch.nn.GELU.html)
definitions.

For standard SELU use precisely

\[
 \lambda=1.0507009873554804934193349852946,\qquad
 \alpha=1.6732632423543772848170429916717,
\]
\[
 \phi(z)=\begin{cases}\lambda z&z>0,\\
                  \lambda\alpha(e^z-1)&z\le0,\end{cases}
 \qquad
 \phi'(z)=\begin{cases}\lambda&z>0,\\
                  \lambda\alpha e^z&z\le0.\end{cases}
 \tag{3}
\]

The left and right derivatives at zero are \(\lambda\alpha\) and \(\lambda\),
respectively, and differ. The selected value is the negative-branch value
\(\phi'(0)=\lambda\alpha\). The constants and function are specified by the
official [SELU definition](https://docs.pytorch.org/docs/2.9/generated/torch.nn.SELU.html).
PyTorch v2.9.0 implements SELU through scaled ELU, whose backward kernel uses
the nonpositive branch at zero; ReLU backward uses a threshold whose
nonpositive branch is zero. These conventions can be traced through the
[activation dispatch](https://github.com/pytorch/pytorch/blob/v2.9.0/aten/src/ATen/native/Activation.cpp),
[backward definitions](https://github.com/pytorch/pytorch/blob/v2.9.0/tools/autograd/derivatives.yaml),
and [CPU activation kernels](https://github.com/pytorch/pytorch/blob/v2.9.0/aten/src/ATen/native/cpu/Activation.cpp).
At finite precision, use the rounded constants in the computation dtype.

For logistic sigmoid,

\[
 \phi(z)=\frac1{1+e^{-z}},\qquad
 \phi'(z)=\phi(z)(1-\phi(z)).
 \tag{4}
\]

This is the ordinary uncentered
[sigmoid](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Sigmoid.html).
A mathematically equivalent overflow-safe evaluation uses
\(1/(1+e^{-z})\) for \(z\ge0\) and \(e^z/(1+e^z)\) for \(z<0\), evaluating
only the selected branch. An analogous safe SELU evaluation uses `expm1(z)`
only on the nonpositive branch. Numerical saturation is a finite-precision
issue, not a different activation definition.

GELU and sigmoid are smooth. ReLU and SELU are continuous and Lipschitz, with
bounded selected derivatives, but have a derivative jump at zero. No change
to first-layer variance, hidden-matrix gain, readout scale or time is implied
by changing activation; in particular no activation-dependent initialization
or SELU normalization claim is introduced.

## 2. Physical network, backward recurrence and scaling

For samples \(a=1,\ldots,M\), set \(U_a=x_a/\sqrt d\in\mathbb R^d\).
Here \(d=2\), \(M=8\), \(n=4096\), and
\(U_a=(\cos\theta_a,\sin\theta_a)\). The derivation also holds at any finite
positive dimensions and sample count. There are three hidden layers and
four parameter blocks:

\[
 z_{1,a}=W_1U_a,\quad h_{1,a}=\phi(z_{1,a}),\qquad
 z_{2,a}=W_2h_{1,a},\quad h_{2,a}=\phi(z_{2,a}),
\]
\[
 z_{3,a}=W_3h_{2,a},\quad h_{3,a}=\phi(z_{3,a}),\qquad
 f_a=c^Th_{3,a}/n,\quad r_a=f_a-y_a,\quad
 \mathcal L=M^{-1}\sum_a r_a^2.
 \tag{5}
\]

The shapes of \(W_1,W_2,W_3,c\) are \(n\times d,n\times n,n\times n,n\).
The exact shared Gaussian draws remain

\[
 (W_1)_{ij}\sim N(0,1),\quad
 (W_{20})_{ij},(W_{30})_{ij}\sim N(0,1/n),\quad
 c_i(0)\sim N(0,1/n^2),
 \tag{6}
\]

independently in the NumPy `default_rng(20260920)` order `W1,W20,W30,c`.
The stored readout is drawn as `standard_normal(n)/n` and is divided by
another \(n\) in (5). Every dense/closure order and activation uses the same
parameter draws; initial hidden responses and moment prefixes are recomputed
for the selected activation.

Starting with the derivative of the linear readout and applying the chain
rule in reverse layer order gives

\[
 \delta_{3,a}=c\odot\phi'(z_{3,a}),\qquad
 \delta_{2,a}=\phi'(z_{2,a})\odot W_3^T\delta_{3,a},\qquad
 \delta_{1,a}=\phi'(z_{1,a})\odot W_2^T\delta_{2,a}.
 \tag{7}
\]

At smooth network states these equal \(n\,\partial f_a/\partial z_{\ell,a}\).
At kinks (7) is the declared selected reverse-mode recurrence. Residuals are
not included in \(\delta\). Differentiating the unhalved mean squared loss
at smooth states yields

\[
 G_1=\frac2{Mn}\sum_a r_a\delta_{1,a}U_a^T,\qquad
 G_\ell=\frac2{Mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T
 \quad(\ell=2,3),\qquad
 G_c=\frac2{Mn}\sum_a r_ah_{3,a}.
 \tag{8}
\]

Here \(G\) denotes those loss derivatives, or their selected reverse-mode
values at kinks; no general subdifferential identification is needed.
The prescribed mobilities \((n,1,1,n)\) therefore give

\[
 \dot W_1=-\frac2M\sum_a r_a\delta_{1,a}U_a^T,\qquad
 \dot W_\ell=-\frac2{Mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T,
 \qquad \dot c=-\frac2M\sum_a r_ah_{3,a}.
 \tag{9}
\]

For ReLU/SELU, (9) means an absolutely continuous trajectory satisfying this
selected field almost everywhere, when such a trajectory exists. Assigning
the kink value defines numerical stage evaluation but does not by itself
prove existence or uniqueness of that differential equation.

## 3. Chronological moments and autonomous reconstruction

From here until stated otherwise every response and residual belongs to the
closure's own current network. Set

\[
 \rho=\sqrt{M^{-1}\sum_a r_a^2},\qquad \dot s=\rho,\quad s(0)=0,
 \qquad L=1+s.
 \tag{10}
\]

As in the preceding derivation, \(L\) denotes history length here; hidden
depth is fixed at three. On an interval with \(\rho>0\), introduce activity
histories \(u_{\ell,a}=r_a\delta_{\ell,a}/\rho\), for \(\ell=2,3\).
The prefix \(0\le\tau\le1\) has \(u=0\) and
\(h_{\ell-1,a}=h_{\ell-1,a}(0)\); the present endpoint is \(\tau=L\).
Because \(|r_a|/\rho\le\sqrt M\), locally bounded physical states give
bounded histories even if activation switches cause jumps in \(u\).
No continuity of the backward history at the prefix or at a kink is needed.

Let \(\ell_k(v)\) be shifted Legendre polynomials with
\(\ell_k(1)=1\) and
\(\int_0^1\ell_j\ell_k=\mathbf1_{j=k}/(2k+1)\). For each link and sample,
retain, for \(k=0,\ldots,P-1\),

\[
 A_{\ell,k,a}=\int_0^L u_{\ell,a}(\tau)\ell_k(\tau/L)\,d\tau,
 \qquad
 B_{\ell,k,a}=\int_0^L h_{\ell-1,a}(\tau)\ell_k(\tau/L)\,d\tau.
 \tag{11}
\]

The polynomial identity

\[
 v\ell_k'(v)=k\ell_k(v)+\sum_{j<k}(2j+1)\ell_j(v)
 \tag{12}
\]

follows by comparing leading terms and integrating against \(\ell_j\).
For \(j<k\), integration by parts leaves the endpoint term one because
\(\ell_j+v\ell_j'\) has degree below \(k\); division by its squared norm
gives the coefficient \(2j+1\). Differentiating (11), using (12),
\(\dot L=\rho\) and \(\rho u=r\delta\), gives

\[
 \dot A_{\ell,k,a}=r_a\delta_{\ell,a}
 -\frac\rho L\left(kA_{\ell,k,a}+\sum_{j<k}(2j+1)A_{\ell,j,a}\right),
\]
\[
 \dot B_{\ell,k,a}=\rho h_{\ell-1,a}
 -\frac\rho L\left(kB_{\ell,k,a}+\sum_{j<k}(2j+1)B_{\ell,j,a}\right).
 \tag{13}
\]

These identities hold almost everywhere for locally integrable histories.
They need no derivative of \(u\), and their operational form never divides
by \(\rho\). Initialize \(A=0\), \(B_{\ell,0,a}=h_{\ell-1,a}(0)\), and
\(B_{\ell,k,a}=0\) for \(k>0\). In particular, the first three transport
equations for an array \(T\) with endpoint source \(b\) are

\[
 \dot T_0=b,\quad
 \dot T_1=b-(\rho/L)(T_1+T_0),\quad
 \dot T_2=b-(\rho/L)(2T_2+T_0+3T_1).
 \tag{14}
\]

Keeping the first P equations realizes exactly P=1,2,3. Reconstruct

\[
 \widehat W_\ell=W_{\ell0}
 -\frac2{MnL}\sum_{a,k<P}(2k+1)A_{\ell,k,a}B_{\ell,k,a}^T,
 \qquad \ell=2,3.
 \tag{15}
\]

Evaluate (5),(7) with \(\widehat W_2,\widehat W_3\), evolve \(W_1,c\) by
(9), and evolve all four moment arrays and the common clock by (10),(13).
This defines the finite autonomous closure. It retains two distinct pairs,
\((A_2,B_2)\) and \((A_3,B_3)\): \(A_2\) is a backward layer-two history,
whereas \(B_3\) is a forward layer-two history. Both operators influence
both pairs through current responses.

Every reverse action uses the actual transpose of the same reconstructed
operator. For example, the learned forward action on \(v\in\mathbb R^n\) is

\[
 (\widehat W_\ell-W_{\ell0})v
 =-\frac2{ML}\sum_{a,k<P}(2k+1)A_{\ell,k,a}
                         \frac{B_{\ell,k,a}^Tv}{n},
 \tag{16}
\]

and the reverse action exchanges A and B. No separately learned adjoint,
fitted coefficient, dense correction or dense-trajectory forcing occurs.
Given the fixed initialized matrices, current finite state and activation,
the numerical stage field is restartable without replaying history.

## 4. Exact covariance omitted by each link

For one link and sample, project its history onto the first P polynomials:

\[
 u_P(\tau)=L^{-1}\sum_{k<P}(2k+1)A_k\ell_k(\tau/L),\qquad
 h_P(\tau)=L^{-1}\sum_{k<P}(2k+1)B_k\ell_k(\tau/L).
\]

Orthogonality gives

\[
 J_P:=\int_0^L u_Ph_P^T\,d\tau
       =L^{-1}\sum_{k<P}(2k+1)A_kB_k^T,
\]
\[
 \int_0^L uh^T\,d\tau-J_P
       =\int_0^L(u-u_P)(h-h_P)^T\,d\tau.
 \tag{17}
\]

The two mixed terms vanish because every component of a projection residual
is orthogonal to every retained polynomial. This is exact for square
integrable histories, including bounded histories with jumps. On a dense
trajectory the learned matrix is \(-2/(Mn)\) times its exact history integral,
since \(d\tau=ds=\rho\,dt\). Formula (15) applies the projection to the
closure's own histories, so (17) does not identify its history with the
separately trained dense network's history.

Write the current endpoint projections as

\[
 u_{\ell,P,a}=L^{-1}\sum_{k<P}(2k+1)A_{\ell,k,a},\qquad
 h_{\ell-1,P,a}=L^{-1}\sum_{k<P}(2k+1)B_{\ell,k,a}.
 \tag{18}
\]

Differentiate \(J_P\) using (13). The endpoint sources contribute
\(\rho(uh_P^T+u_Ph^T)\). The derivative of \(L^{-1}\), the diagonal
transport terms and both lower-triangular sums combine to

\[
 -\frac\rho{L^2}\sum_{j,k<P}(2j+1)(2k+1)A_jB_k^T
 =-\rho u_Ph_P^T.
\]

For diagonal coefficients this uses \(1+2k=2k+1\); each triangular sum
supplies one off-diagonal half. Consequently

\[
 \dot J_P=\rho\{uh^T-(u-u_P)(h-h_P)^T\}.
\]

Multiplication by \(-2/(Mn)\) proves the two exact physical defects:

\[
 E_\ell:=\dot{\widehat W}_\ell
       +\frac2{Mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T
 =\frac2{Mn}\sum_a
   (r_a\delta_{\ell,a}-\rho u_{\ell,P,a})
   (h_{\ell-1,a}-h_{\ell-1,P,a})^T,
 \quad \ell=2,3.
 \tag{19}
\]

The positive sign is fixed by subtracting the omitted covariance from the
negative gradient-history integral. Equation (19) is also an algebraic
identity between the operational stage velocities at kinks and at
\(\rho=0\). Along an absolutely continuous trajectory it holds almost
everywhere. Each defect has rank at most M, while each learned increment
has rank at most MP. At initialization the projected incoming response
equals its true endpoint, so both defects vanish exactly for every P.
Thus all four initial physical velocities match their dense counterparts.

The physical state \((W_1,\widehat W_2,\widehat W_3,c)\) evolves by the
selected dense field at its own weights plus \((0,E_2,E_3,0)\). For \(\rho>0\),
(19) yields the error-production estimate

\[
 \|E_\ell\|_F\le\frac{2\rho}{M}\sum_a
 \frac{\|u_{\ell,a}-u_{\ell,P,a}\|_2}{\sqrt n}
 \frac{\|h_{\ell-1,a}-h_{\ell-1,P,a}\|_2}{\sqrt n}.
 \tag{20}
\]

This follows from the Frobenius norm of a rank-one product and the triangle
inequality. It is not a trajectory-error bound: the dense/closure difference
also propagates through the nonlinear coupled network field.

At smooth states the additional output velocity at sample a is

\[
 \dot f_a\big|_{\mathrm{defect}}
   =n^{-1}(\delta_{2,a}^TE_2h_{1,a}+\delta_{3,a}^TE_3h_{2,a}),
\]

and ordinary differentiation of the loss gives

\[
 \dot{\mathcal L}=-n\|G_1\|_F^2-\|G_2\|_F^2-\|G_3\|_F^2-n\|G_c\|_2^2
                 +\langle G_2,E_2\rangle_F+\langle G_3,E_3\rangle_F.
 \tag{21}
\]

In particular even the smooth closure has no automatic loss-monotonicity
guarantee. No pointwise ordinary-gradient interpretation of (21) at a kink
is required for (19).

## 5. Smoothness, zero residual and response lifts

For GELU and sigmoid the direct-coordinate closure is locally Lipschitz in
\((W_1,c,A_2,B_2,A_3,B_3,s)\) on \(L>0\). Matrix reconstruction is rational
with nonzero denominator, the activations and their derivatives are smooth,
and \(\rho=\|r\|_2/\sqrt M\) is locally Lipschitz even at zero residual.
Finite sums, products and compositions preserve local Lipschitz continuity
on bounded neighborhoods. The local ODE theorem for a locally Lipschitz
finite-dimensional vector field therefore supplies a unique solution on
some interval from each such state. This conclusion is local; global
existence, boundedness and approximation guarantees have not been shown.

For ReLU and SELU the selected derivative is discontinuous at zero, so the
same argument applies only inside a region with fixed nonzero preactivation
signs. The moment and defect algebra does not require smoothness, while the
smooth local argument establishes no general crossing theory, uniqueness
theorem or numerical order theorem. The declaration of \(\phi'(0)\) alone
supplies none of these. In particular,
smooth second-order Heun error theory cannot simply be transferred across
switches. Empirical step-refinement checks must be retained.

At every finite state with \(r=0\), \(\rho=0\) and every right-hand side in
(9),(10),(13) vanishes. There is no undefined normalized source to evaluate;
the division-free expression (19) also vanishes. Constant continuation is
therefore exact. More strongly, any absolutely continuous selected-field
solution starting at such a state cannot leave it while remaining in a
bounded neighborhood with \(L>0\). To see this, let \(X_*\) denote the whole
direct state. Local boundedness of the selected derivatives gives
\(\|F(X)\|\le C\|r(X)\|\), because every source contains r or \(\rho\).
All four activation maps and the reconstructed forward map are locally
Lipschitz, hence \(\|r(X)\|\le C'\|X-X_*\|\) when \(r(X_*)=0\).
An absolutely continuous solution consequently satisfies

\[
 q(t):=\|X(t)-X_*\|\le CC'\int_{t_*}^t q(v)\,dv.
\]

If \(Q(t)=\int_{t_*}^t q(v)\,dv\), then \(Q(t_*)=0\), \(Q\ge0\), and
\((e^{-CC'(t-t_*)}Q)'\le0\) almost everywhere, so \(Q=q=0\).
This establishes zero-residual absorption conditional on existence of the
trajectory, without a blanket nonsmooth uniqueness claim elsewhere.

The production closure may simply recompute all activations and \(\rho\)
from its direct state at every stage. That representation does not inherit
the tanh lifted RHS's rationality. A more precise activation-specific
statement is possible. First the common product rule gives

\[
 \dot{\widehat W}_\ell=-\frac2{MnL}\sum_{a,k<P}(2k+1)
 [\dot A_{\ell,k,a}B_{\ell,k,a}^T+A_{\ell,k,a}\dot B_{\ell,k,a}^T
                          -(\rho/L)A_{\ell,k,a}B_{\ell,k,a}^T].
 \tag{22}
\]

On smooth trajectories propagate in layer order

\[
 \dot z_1=\dot W_1U,\qquad
 \dot z_\ell=\dot{\widehat W}_\ell h_{\ell-1}
                       +\widehat W_\ell\dot h_{\ell-1},\quad \ell=2,3,
 \qquad \dot h_\ell=\phi'(z_\ell)\odot\dot z_\ell,
\]
\[
 \dot f_a=(\dot c^Th_{3,a}+c^T\dot h_{3,a})/n,\qquad
 \dot\rho=(M\rho)^{-1}\sum_a r_a\dot f_a\quad(\rho>0).
 \tag{23}
\]

All quantities on the right are evaluated from the same ODE-stage state.
Current backward responses are computed first, then physical and moment
velocities, then (22), and finally (23) in forward order. No implicit cycle
is present. Initializing the lifted \(\rho\) from the residual norm preserves
\(\rho^2-M^{-1}\sum_a r_a^2=0\) by direct differentiation. At an exactly
consistent zero-residual state the lifted boundary field is defined as zero.

For sigmoid, retain each \(h_\ell\) and use
\(\dot h_\ell=h_\ell(1-h_\ell)\odot\dot z_\ell\). This yields a rational
field on \(L>0,\rho>0\). Consistency follows directly: if
\(q=\phi(z)\), then
\((h-q)'=(1-h-q)\dot z\,(h-q)\) componentwise, so initially zero discrepancy
stays zero. This is an exact continuous-time lift, not an implemented
numerical invariant guarantee.

Exact GELU also has a finite rational lift, but additional coordinates are
needed for the explicit construction here. For every hidden preactivation
retain \(z,p,q\), initialized by \(p=\Phi(z)\), \(q=\varphi(z)\), use
\(h=zp\) and \(\phi'=p+zq\), and set

\[
 \dot p=q\dot z,\qquad \dot q=-zq\dot z,\qquad
 \dot h=(p+zq)\dot z.
 \tag{24}
\]

All products are componentwise. The derivative of \(z\) is (23), using
the current layer's predecessors. Product-rule differentiation makes
\(z_1-W_1U\) and \(z_\ell-\widehat W_\ell h_{\ell-1}\) constant; they start
at zero. Also \(q-\varphi(z)\) solves the homogeneous linear equation
\((q-\varphi(z))'=-z\dot z(q-\varphi(z))\), and then
\((p-\Phi(z))'=(q-\varphi(z))\dot z=0\). Thus all compatibility identities
persist, proving the rational lift on its consistent manifold for
\(L>0,\rho>0\). Normal CDF and density evaluation is still required at
initialization or for new query inputs. This lift is a mathematical option,
not a claim about the evaluated direct-coordinate GELU solver.

ReLU admits polynomial response equations while all gates remain fixed.
SELU likewise admits \(\dot h=\lambda\dot z\) on a positive branch and
\(\dot h=(h+\lambda\alpha)\dot z\) on a negative branch. Their switching
rules require sign tests and the specified boundary convention. These are
piecewise descriptions; no single globally smooth rational lifted field,
global equivalence across all switches, or nonsmooth uniqueness theorem is
asserted for them.

## 6. Lost oddness, state size and claim limits

None of the four activations is odd. For example sigmoid has
\(\phi(0)=1/2\); ReLU has \(\phi(-1)=0\ne-\phi(1)\); exact GELU obeys
\(\phi(z)+\phi(-z)=z(2\Phi(z)-1)\); and SELU has unequal one-sided slopes
at zero. The bias-free tanh proof of \(f(-U)=-f(U)\) therefore does not
transfer. No antipodal data quotient or prediction antisymmetrization is
valid in general for this continuation. Both selected tasks already have
eight literal examples and need no quotient. Sigmoid is not centered or
rescaled to recover the previous symmetry.

The direct moving state contains

\[
 nd+n+4PnM+1
\]

scalars; its fixed initialized matrices contain \(2n^2\). At \(M=8\), each
learned increment has rank at most 8,16,24 for P=1,2,3. Applying an increment
costs \(O(nMP)\) per vector, but the fixed dense matrix products and their
transpose products remain. Extra response coordinates in an optional lift
add storage and consistency diagnostics. These counts concern compression
of evolving learned state, not removal of the initialized matrices or a
guaranteed runtime reduction.

The exact claims established here are the selected recurrence, autonomous
finite moment construction, both covariance identities and their initial
vanishing, and zero-residual absorption under the specified assumptions.
Smooth local well-posedness is established only for GELU/sigmoid. Rational
lifts have been exhibited only with their explicit coordinates and domains;
ReLU/SELU have only the stated branchwise descriptions. The previous tanh
accuracy, order ranking and numerical convergence evidence do not establish
these properties for another activation. Successful P=1,2,3 tests would be
finite-instance evidence, not monotone hierarchy convergence, population
identification, global tracking or a width-independent complexity theorem.

## Provenance

Author: scoped theory agent `/root/activation_theory`. Complete repository
scientific inputs read: `DEEP_CIRCLE_DERIVATION.md`,
`DEEP_CIRCLE_PROTOCOL.md`, `DEEP_CIRCLE_RESULTS.md`, `deep_moment_engine.py`
within this study, and `docs/NOTATION.md`. No other study, earlier linked
report, or generated training data was used. External scientific input was
limited to the linked official PyTorch activation definitions and v2.9.0
source for derivative conventions. Required process skills read:
`solve-math-rigorously` and `investigate-conjectures`, with the latter's
research-contract, evidence-ledger and adversarial-audit references.
This file is author-checked algebra, not an independent review or promotion.
Only this file was written; no code, training or Git-index change was made.

| Repository input | Read-version SHA256 |
|---|---|
| DEEP_CIRCLE_DERIVATION.md | 17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9 |
| DEEP_CIRCLE_PROTOCOL.md | 545b16b9b7548b1b31463ef9942321832f7927465617d99ef25cab38ef301b69 |
| DEEP_CIRCLE_RESULTS.md | 5ba8dd3668ce77ce3a99e4cef09ff77af21f5b1dc0836a816c121b4ffca853ec |
| deep_moment_engine.py | 97aa9bc3ac99a982ec81ab8abac3e240aca2e05aecb37e1d6a24b3e7f4ba9f23 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
