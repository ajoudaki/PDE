# Gaussian-mass obstruction route

Scoped independent theoretical analysis, 2026-10-10. Scientific inputs were the supervisor's assignment only; no other study artifacts, simulations, or literature were consulted. The research, rigorous-proof, and canonical-notation instructions were applied.

**Status:** no strong Gaussian negative theorem is proved. The exact results below exclude a fixed-direction symmetry trap, identify what a finite bad critical point must lose, and isolate the missing Gaussian-probability bridge in a positive-floor activation construction. The alternate activation calculation is not a result for tanh/tanh.

## Contract and exact flow

Let the columns of \(X\in\mathbb R^{d\times m}\) be distinct, nonantipodal unit vectors. The width is \(n\), the labels \(y\in\mathbb R^m\) are fixed independently of the Gaussian draw and of \(n\), and

\[
 U=\tanh(AX),\qquad H=\tanh(WU),\qquad
 f=\frac1n H^\top w,\qquad r=f-y,\qquad
 \mathcal L=\frac1m\|r\|^2.
\]

Here \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). Initially the entries of \(A\) are independent \(N(0,1)\), the entries of \(W\) are independent \(N(0,1/n)\), the two matrices are independent, and \(w=0\). The gradient-flow mobilities are \(n,1,n\) for \(A,W,w\), respectively.

The requested negative statement is the existence of admissible fixed \(X,y\) and constants \(c,p>0\) such that

\[
 \liminf_{n\to\infty}
 \mathbb P\!\left(\lim_{t\to\infty}\mathcal L_n(t)\ge c\right)\ge p.
\]

The loss limit exists because the loss is nonnegative and nonincreasing. A finite-time plateau, an infinite-width limit taken first, or an event whose probability tends to zero does not establish this statement.

Define the derivative matrices and the backpropagated first-layer factor by

\[
 D=1-H\odot H,\qquad E=1-U\odot U,\qquad
 B=\bigl[W^\top\operatorname{diag}(w)D\bigr]\odot E.
\]

All three are \(n\times m\). Direct differentiation gives

\[
\begin{aligned}
 \dot w&=-\frac2m Hr,\\
 \dot W&=-\frac{2}{mn}\operatorname{diag}(w)D
                  \operatorname{diag}(r)U^\top,\\
 \dot A&=-\frac2m B\operatorname{diag}(r)X^\top.
\end{aligned}
\]

The residual equation is

\[
 \dot r=-\frac2m K r,
\]

with the positive semidefinite matrix

\[
\begin{aligned}
 K={}&\frac1nH^\top H
 +\left(\frac1n U^\top U\right)\odot
   \left(\frac1nD^\top\operatorname{diag}(w^2)D\right)\\
 &+(X^\top X)\odot\left(\frac1n B^\top B\right).
\end{aligned}
\]

Consequently

\[
 \dot{\mathcal L}
 =-\frac4{m^2}r^\top Kr
 =-\frac1n\|\dot A\|_F^2-\|\dot W\|_F^2
  -\frac1n\|\dot w\|^2.
\]

These formulas also apply to differentiable activations other than tanh when \(D_{ja}=\phi_2'((WU)_{ja})\), \(E_{ka}=\phi_1'((AX)_{ka})\), and the forward pass is changed explicitly.

For tanh the finite-width solution exists for every finite time. Indeed, loss dissipation gives \(\|r(t)\|\le\|y\|\), and bounded activations give

\[
 |\dot w_j|\le\frac{2\|y\|}{\sqrt m},\qquad
 \|\dot W\|_F\le
 \frac{2\|y\|}{\sqrt{mn}}\|w\|.
\]

Thus \(w\) and \(W\) have finite bounds on each finite interval. Since

\[
 \|\dot A\|_F\le
 \frac2m\|W\|_{\mathrm{op}}\|w\|\|y\|\|X\|_{\mathrm{op}},
\]

the same is true of \(A\). Smooth local existence therefore extends over every finite interval. This argument does not bound the parameters uniformly as \(t\to\infty\).

## Initial full rank and finite critical points

For the stated tanh data, \(U(0)\) has column rank \(m\) almost surely when \(n\ge m\). To see this, choose \(\xi\in\mathbb R^d\) such that the scalars \(\xi^\top x_a\) are nonzero and have distinct absolute values. Such a choice avoids only finitely many proper hyperplanes, since the data are distinct and nonantipodal.

The functions \(t\mapsto\tanh(t\xi^\top x_a)\) are linearly independent. In a putative vanishing linear combination, taking \(t\to\infty\) first cancels the constant term. The slowest remaining exponential, proportional to \(\exp(-2t\min_a|\xi^\top x_a|)\), then forces the coefficient of the unique smallest absolute slope to vanish. Repeating gives all coefficients zero. Therefore the functions \(a\mapsto\tanh(a^\top x_a)\), indexed by the samples, are linearly independent. Their evaluation vectors span \(\mathbb R^m\), so some \(m\times m\) evaluation determinant is nonzero. That determinant is a nonzero real-analytic function of the \(m\) first-layer rows, and its zero set has Lebesgue measure zero. The latter fact follows by slicing in one variable, using isolated zeros of a nonzero one-variable analytic function, and induction on the number of variables. Gaussian sampling is absolutely continuous, proving the claim.

Conditionally on \(U(0)\), each row of \(W(0)U(0)\) is an independent Gaussian vector with covariance \(U(0)^\top U(0)/n\). This covariance is positive definite. Applying tanh coordinatewise gives a row distribution with support containing the open box \((-1,1)^m\), so \(H(0)\) also has column rank \(m\) almost surely.

At a finite critical point, the following elementary obstruction holds:

> If \(U\) has column rank \(m\) and at least one readout coordinate \(w_j\) is nonzero, then \(r=0\).

For that row \(j\), the equation \(\nabla_{W_{j,:}}\mathcal L=0\) is

\[
 U\bigl(D_{j,:}^\top\odot r\bigr)=0.
\]

Column independence of \(U\) implies \(D_{j,:}^\top\odot r=0\), and every tanh derivative at a finite argument is strictly positive. Hence \(r=0\). If instead \(w=0\), the readout stationarity equation is \(Hr=0\); full column rank of \(H\) again gives \(r=0\).

Thus a nonzero-loss finite critical point requires loss of first-layer feature rank, except for the zero-readout case, which requires loss of top-layer feature rank. This does not exclude convergence toward such a point or escape to infinity with saturation. Full rank initially is not an all-time lower bound on a smallest singular value.

## Gaussian symmetry does not cancel the predictor

Let \(S\) and \(T\) be diagonal matrices with entries in \(\{-1,1\}\). The transformations

\[
 (A,W,w)\mapsto(SA,WS,w),\qquad
 (A,W,w)\mapsto(A,TW,Tw)
\]

preserve the forward prediction and commute with the tanh gradient flow. The Gaussian initialization has both symmetries. In particular, individual readout means can vanish by sign symmetry even while the prediction is nonzero: \(w\) and \(H\) become correlated.

At initialization,

\[
 \dot w(0)=\frac2m H(0)y,\qquad
 \dot f(0)=\frac2m\frac{H(0)^\top H(0)}n y.
\]

For \(y\ne0\),

\[
 y^\top\dot f(0)=\frac2m\frac{\|H(0)y\|^2}{n}>0
\]

almost surely for \(n\ge m\). Therefore neither row-sign symmetry nor zero initial readout keeps a fixed nonzero label direction invisible.

## Exact exclusion of a fixed-direction trap

This argument holds for any smooth forward feature map \(H\), with the stated linear readout and mobilities, whenever the relevant solution exists. It is not specific to tanh.

Fix \(v\in\mathbb R^m\), and replace the residual in the exact parameter equations by the constant vector \(-v\). This is gradient ascent on

\[
 \Phi=v^\top f=\frac1n w^\top Hv,
\]

with the positive factor \(2/m\) and the original mobilities. Use \(s\) for its time, and define

\[
 Q=\frac1n\|w\|^2,\qquad
 \kappa_0=\frac1n\|H(0)v\|^2.
\]

Suppose \(w(0)=0\) and \(\kappa_0>0\). Euler's identity in the linear readout and the tangent-kernel identity give

\[
 \frac{dQ}{ds}=\frac4m\Phi,\qquad
 \frac{d\Phi}{ds}=\frac2m v^\top Kv
 \ge\frac2m\frac{\Phi^2}{Q}\quad(Q>0).
\]

The inequality is Cauchy–Schwarz applied to \(w^\top Hv/n\), retaining just the readout term in \(K\). The objective \(\Phi\) is nondecreasing, and it is positive for \(s>0\), because its initial derivative is \(2\kappa_0/m>0\). Hence \(Q>0\) for \(s>0\), and

\[
 \frac{d}{ds}\left(\frac{\Phi^2}{Q}\right)
 =\frac{2\Phi}{Q}\frac{d\Phi}{ds}
   -\frac{\Phi^2}{Q^2}\frac{dQ}{ds}\ge0.
\]

The initial expansions are

\[
 w(s)=\frac{2s}{m}H(0)v+O(s^2),\qquad
 \Phi(s)=\frac{2s}{m}\kappa_0+O(s^2),\qquad
 Q(s)=\frac{4s^2}{m^2}\kappa_0+O(s^3).
\]

They show \(\Phi^2/Q\to\kappa_0\) as \(s\downarrow0\). Consequently

\[
 v^\top K(s)v\ge\frac{\Phi(s)^2}{Q(s)}\ge\kappa_0,
 \qquad
 \frac{d\sqrt Q}{ds}=\frac{2\Phi}{m\sqrt Q}
 \ge\frac{2\sqrt{\kappa_0}}m.
\]

Integrating yields the explicit lower bound

\[
 \Phi(s)\ge\sqrt{\kappa_0 Q(s)}
 \ge\frac{2\kappa_0}{m}s.
\]

Thus the alignment objective cannot approach a finite positive plateau along a global alignment trajectory.

There is a direct squared-loss consequence. Suppose, as an exact property of a particular trajectory, that

\[
 y=\alpha v,\qquad f(t)=\beta(t)v,\qquad \alpha>0,\qquad\beta(0)=0.
\]

Before fitting, its parameter path is the preceding alignment path with clock

\[
 s(t)=\int_0^t(\alpha-\beta(u))\,du.
\]

The scalar residual equation and the kernel bound give

\[
 \dot\beta=
 \frac{2}{m\|v\|^2}(\alpha-\beta)v^\top Kv
 \ge\frac{2\kappa_0}{m\|v\|^2}(\alpha-\beta).
\]

Uniqueness prevents crossing the fitted equilibrium. Therefore

\[
 0\le\alpha-\beta(t)
 \le\alpha\exp\!\left(-\frac{2\kappa_0}{m\|v\|^2}t\right).
\]

An exact one-dimensional symmetry reduction therefore fits, rather than producing the desired negative example. Applying this statement to a population equation requires that equation to retain the displayed gradient identities; a symmetry of the initialization alone does not imply that a finite Gaussian realization stays in this reduction.

## Large fixed labels: exact clock, unresolved infinite time

For \(y=\alpha v\), set \(s=\alpha t\) without changing any parameter variable. The exact equations in this clock are

\[
\begin{aligned}
 \frac{dw}{ds}&=\frac2mH\left(v-\frac f\alpha\right),\\
 \frac{dW}{ds}&=\frac{2}{mn}\operatorname{diag}(w)D
              \operatorname{diag}\left(v-\frac f\alpha\right)U^\top,\\
 \frac{dA}{ds}&=\frac2mB
              \operatorname{diag}\left(v-\frac f\alpha\right)X^\top.
\end{aligned}
\]

On a compact \(s\)-interval, the formal large-label limit is the constant-direction alignment flow above. For fixed width, ordinary continuous dependence justifies this limit as long as the limiting trajectory stays in a bounded set on that interval. Its alignment objective grows at least linearly. This compact-interval statement neither produces a fixed-α bad basin nor permits taking \(t\to\infty\) after replacing the exact equations by the alignment flow. A useful negative construction would need to prove entry into an invariant bad basin for one finite value of α.

## Alternate activation: a positive floor is not a sign invariant

Now change only the second activation to

\[
 \phi_2(z)=\frac{3+\cos z}{2}\in[1,2],
 \qquad \phi_1=\tanh.
\]

This is an alternate admissible analytic activation, not tanh/tanh. Its derivatives are bounded on each fixed horizontal strip. Its initial population top-feature Gram is positive definite for the stated data: the first-layer population covariance is positive definite by the independence argument above, a Gaussian with this covariance has full support, and coordinatewise \(\phi_2\) has an image containing the open box \((1,2)^m\).

Let \(k=m-1\), and choose

\[
 y=(P,-1,\ldots,-1)^\top,\qquad P>2k.
\]

At zero readout, every neuron has

\[
 \dot w_j(0)=\frac2m\sum_a H_{ja}(0)y_a
 \ge\frac2m(P-2k)>0.
\]

If all readouts stayed nonnegative, all predictions would be nonnegative and

\[
 \mathcal L(t)\ge\frac{k}{m}.
\]

However, the initial derivative bound does not establish nonnegativity for all time. At a prospective boundary \(w_j=0\), the actual inward condition is

\[
 H_{j,:}(y-f)\ge0,
\]

which depends on the predictions produced by the other neurons. Positivity of \(H_{j,:}y\) does not imply this condition.

A natural proposed collapsed feature vector is

\[
 v=(2,1,\ldots,1)^\top.
\]

If all rows approached \(v^\top\), the least-squares coefficient in this one-dimensional model would be

\[
 S_* = \frac{v^\top y}{\|v\|^2}=\frac{2P-k}{4+k}>0,
 \qquad f_*=S_*v.
\]

It has strictly positive residual loss; explicitly,

\[
 \frac1m\|y-f_*\|^2=\frac{k(P+2)^2}{m(4+k)}.
\]

But a row with constant features \(h=2\mathbf1\) would have, at this proposed endpoint,

\[
 \dot w_j=\frac2m h^\top(y-f_*)
 =-\frac{4k(P+2)}{m(4+k)}<0.
\]

Such a row would eventually become negative if it remained close to these features long enough. The exact row \(W_{j,:}=0\) does stay at \(h=2\mathbf1\), because \(\phi_2'(0)=0\) makes its row update vanish and \(W_{j,:}U(t)=0\) for every first-layer trajectory. This exact row has Gaussian probability zero. Requiring a Gaussian row's entire Euclidean norm to be arbitrarily small has exponentially small probability in \(n\), and does not give the requested mass.

In contrast, requiring only its initial \(m\) preactivations to lie near zero does have probability bounded away from zero as \(n\to\infty\), for every fixed neighborhood. Conditional on \(U(0)\), those preactivations are \(N(0,U(0)^\top U(0)/n)\), and this covariance converges to a positive-definite matrix. Conditional independence of the top rows then gives a positive fraction of such rows in the large-width limit. The missing step is that initial preactivation control is not control of the whole future path: even when the row's own update is small,

\[
 \frac{d}{dt}(W_{j,:}U)
 =\dot W_{j,:}U+W_{j,:}\dot U
\]

contains motion of the first layer.

The obstruction can be stated on a finite interval, without claiming an infinite-time small-ball event. Write \(e=y-f\). Suppose on \([T,T+Δ]\) that

\[
 \mathbf1^\top e(t)\le-δ,
 \qquad\|e(t)\|_1\le R,
 \qquad\|H_{j,:}(t)-b\mathbf1^\top\|_\infty\leε,
\]

where \(\delta,R,b>0\) and \(\varepsilon R\le b\delta/2\). Then

\[
 \dot w_j(t)=\frac2mH_{j,:}(t)e(t)
 \le-\frac{b\delta}{m}.
\]

If \(w_j(T)\le M\) and \(\Delta>mM/(b\delta)\), this neuron becomes negative before the interval ends. For the positive-floor activation, loss dissipation gives the width-independent bound

\[
 |w_j(T)|\le\frac{4T\|y\|}{\sqrt m}.
\]

At the proposed collapsed endpoint one may take \(b=2\) and a strict lower bound below

\[
 \delta_*=-\mathbf1^\top(y-f_*)=\frac{k(P+2)}{4+k}>0.
\]

Thus a sufficiently accurate finite-time constant-feature cohort would invalidate the proposed positive-readout invariant. Proving that this cohort has nonvanishing Gaussian mass in the fully trained two-hidden-layer model requires a pathwise probability estimate that is not established here. A possible route is a Gaussian cavity-path small-ball bound on a fixed finite interval, together with control of the removed neuron's self-interaction. Neither step follows from the initial finite-dimensional Gaussian small-ball probability.

Conversely, a strong negative proof through the positive cone must show why such corrective paths cannot produce enough negative readout mass. Simply omitting a small but fixed Gaussian tail is invalid when \(n\to\infty\), and finite-time small mass does not rule out eventual correction.

## Route decision

| Mechanism | Exact result | Unresolved implication | Status |
|---|---|---|---|
| Gaussian row-sign symmetry | Initial response in every nonzero label direction is nonzero; predictor correlations survive the symmetry. | A different invariant would have to constrain the predictor. | The proposed cancellation mechanism is excluded. |
| Fixed residual direction | Alignment objective grows at least linearly; an exact scalar squared-loss reduction fits exponentially. | A negative route must involve changing residual directions or a singular limit not covered by these identities. | Excluded under the stated exact reduction. |
| Finite tanh critical point | Nonzero loss requires first-layer rank loss, or top-feature rank loss when the readout vanishes. | Reachable rank collapse or saturation with a basin of nonvanishing Gaussian mass. | Open. |
| Large fixed label scale | Exact fast clock and compact-interval alignment limit; alignment cannot have a finite objective plateau. | Entry into and invariance of a bad basin for a fixed finite label scale. | Open; a plateau is insufficient. |
| Positive-floor activation | Uniform initial positive readout velocity and an explicit bad one-pattern endpoint. | All-time sign preservation fails to follow; constant-feature corrective rows have negative endpoint velocity. | Candidate construction incomplete. |
| Gaussian corrective cohort | Initial preactivation small balls have nonvanishing mass; a finite-interval nearconstant cohort provably crosses to negative readout. | Full-training pathwise small-ball and self-interaction control. | A concrete finite-time probability bottleneck, not a convergence theorem. |

No calculation above proves \(\mathbb P(\mathcal L_n(\infty)\ge c)\) has a positive large-width limit. The fixed-direction lemma is a positive structural result; the positive-floor endpoint is a conditional construction whose required Gaussian basin remains unproved.
