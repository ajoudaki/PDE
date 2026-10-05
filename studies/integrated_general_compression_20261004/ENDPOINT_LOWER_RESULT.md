# Dense-copy variability: endpoint lower bounds and their parameter meaning

2026-10-04. Continuation of the integrated theorem's lower-bound component,
at the user's request to prioritize actual fitted endpoints. These are
internally derived results, not promoted manuscript/book theorems. Complete
proofs and reconstruction status are linked below.

## Common setup

Use the canonical independent Gaussian width-\(n\) dense networks, zero
readout, mean squared loss, and mobilities \((n,1,\ldots,1,n)\) from
`GENERAL_EXPLICIT_FITTING.md`. Training inputs satisfy
\(\|x_a\|=\sqrt d\); put \(v_a=x_a/\sqrt d\). Labels are fixed in
width and \(Y=\|y\|_2/\sqrt m>0\). Let

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),\qquad
 Q=Q^{(L)},\quad \gamma=\lambda_{\min}(Q)>0.
\]

Two independently initialized predictors are \(f_n,\widetilde f_n\).
The existing common small-label allowance is retained. Each theorem below
also states a simpler sufficient allowance directly. Constants denoted by
\(c,p,C\) do not depend on width, sample size, input dimension, covariance
conditioning or labels; constants subscripted \(L\) may depend on fixed
depth. The width must be sufficiently large for the explicitly identified
initialization events. There is no new assumption on trained responses.

## 1. Two nonlinear hidden layers: actual endpoint lower bound

Take \(L=2\) and tanh in **both** hidden layers:

\[
 f_n(t,x)=n^{-1}w_t^\top\tanh\!\big(W_t\tanh(A_tx/\sqrt d)\big).
\]

Suppose the training inputs span a proper subspace of \(\mathbb R^d\),
and \(0<Y\le10^{-6}\gamma/m\). The integrated label cap is stronger
than this, so every such example satisfying the integrated assumptions is
covered. For any fixed \(x\) of norm \(\sqrt d\) orthogonal to all
training inputs, with probability at least a numerical constant \(p>0\),
both runs converge and fit, and

\[
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|
       \ge c\sqrt{\frac{y^\top Q^{-1}y}{n}}. \tag{1}
\]

The probability is bounded below uniformly for all sufficiently large
individual widths. This is not a simultaneous assertion over infinitely
many independently sampled widths.

For labels in the least-eigenvalue eigenspace of \(Q\), (1) becomes

\[
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|
       \ge cY\sqrt{\frac{m}{\gamma n}}. \tag{2}
\]

For orthogonal training inputs with \(d\ge m+1\), \(Q=\gamma I_m\),
so (2) holds for **every** nonzero label vector, of either or mixed signs.
For correlated training inputs, (1) is the more accurate statement: label
orientation matters and cannot be erased from a lower bound.

There is a matching upper scale at the **same fixed unseen query**. For
every \(0<\delta<1\), once the reduced fitting threshold is met, with
probability at least \(1-\delta\), both endpoints exist, fit, and

\[
 |f_n(\infty,x)-\widetilde f_n(\infty,x)|
       \le36Y\sqrt{\frac{m}{\delta\gamma n}}. \tag{3}
\]

Thus for orthogonal data, or labels in the weakest covariance direction,
the powers of \(n,m,\gamma,Y\) match for this endpoint query. Equation
(3) is not an upper bound for the whole sphere supremum.

To verify (3), condition on the two active training initializations as in
the full proof. The remaining query vectors are independent standard
Gaussians. Their output difference has zero mean and squared Lipschitz
constant at most

\[
 81\frac{\|w_\infty\|^2+\|\widetilde w_\infty\|^2}{n^2}
 \le648\frac{Y^2m}{\gamma n}.
\]

Gaussian Poincare and conditional Chebyshev put the difference below (3)
with conditional failure at most \(\delta/2\). Each reduced fitting
event has failure at most \(\delta/4\). A union bound proves the claim.
No lower-bound covariance event is needed for this upper bound.

The mechanism in the proof has three precise parts:

1. The read-in on directions orthogonal to the training span never moves
   and stays Gaussian independently of the active training trajectory.
2. Cubic products of first-layer random responses give the second-layer
   query-feature covariance a positive gap, even though the square
   initialized mixer itself has small singular values. This gap survives
   the actual small-label hidden-layer motion.
3. Fitting requires
   \(\|w_\infty\|^2/n\ge\tfrac12y^\top Q^{-1}y\). The surviving
   query covariance converts that necessary readout energy into endpoint
   prediction variability. A fourth-moment bound makes it a probability
   lower bound, rather than only a second-moment statement.

All hidden layers follow their original equations. For example with one
datum, writing \(h=\tanh(A_0v)\), \(g=\tanh(W_0h)\), their initial
accelerations are

\[
 \ddot W_0=\frac{4y^2}{n}[g\odot(1-g^2)]h^\top,\qquad
 \ddot A_0=4y^2[(1-h^2)\odot W_0^\top(g\odot(1-g^2))]v^\top.
\]

Both are nonzero almost surely for \(y\ne0\): the Gaussian mixer is
invertible almost surely, \(h\ne0\), and tanh and its derivative have the
required nonvanishing factors at finite nonzero arguments. The theorem
therefore has no frozen-feature interpretation imposed on its dynamics.

Complete proof: `TANH_ENDPOINT_VARIABILITY_LOWER.md`.
The independently developed identity--tanh proof with a larger label
allowance is retained in `NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md`.

## 2. Arbitrary fixed depth: exact sphere dependence in the linear subclass

For identity activation in all \(L\ge2\) layers, take \(m<d\) linearly
independent unit inputs. Then \(Q=(v_a^\top v_b)_{a,b}\). The sufficient
label allowance here is

\[
 0<Y\le\frac{\gamma}{8m}
 \left(9^{2L-2}+4\sum_{j=0}^{L-2}9^{2j}\right)^{-1/2}.
\]

This includes the common integrated cap. With probability at least \(1/16\),
at an explicit finite width threshold, both endpoints fit and

\[
 \sup_{\|x\|=\sqrt d}|f_n(\infty,x)-\widetilde f_n(\infty,x)|
 \ge\frac12\sqrt{\frac{(d-m)y^\top Q^{-1}y}{n}}. \tag{4}
\]

For labels in the weakest covariance direction, the matching sphere scale is

\[
 Y\sqrt{\frac{m(d-m)}{\gamma n}}. \tag{5}
\]

For labels in that same weakest covariance direction, both an upper and
a lower bound at this scale hold with high probability when \(d-m\) is large relative to the desired log-confidence. More precisely,
for \(d-m\ge16\log(4/\delta)\), with probability at least \(1-\delta\),

\[
 \frac Y2\sqrt{\frac{m(d-m)}{\gamma n}}
 \le\sup_{\|x\|=\sqrt d}|f_n(\infty,x)-\widetilde f_n(\infty,x)|
 \le4\,9^{L-1}Y\sqrt{\frac{m(d-m)}{\gamma n}}. \tag{6}
\]

This follows from an exact conditional Gaussian law for the coefficients
on the \(d-m\) unused directions. Interpolation fixes the coefficient
within the training span deterministically. The full proof gives the
complete width threshold and exact law; the \(\sqrt{d-m}\) factor in
(4)--(6) comes from the sphere supremum, not a fixed-query variance.

Identity belongs to the integrated activation class and has unbounded
values. This example therefore supplies a rigorous obstruction to an
upper bound for that full class whose data/dimension coefficient is
uniformly smaller than (5). It does not establish the same dimension
factor for two tanh layers.

Complete proof: `LINEAR_ENDPOINT_VARIABILITY_LOWER.md`.

## 3. A broader actual-trajectory lower bound

`ONSET_TO_TRAJECTORY_LOWER.md` also converts the initialized covariance
CLT into a lower bound for actual nonlinear predictions. A derivative at
time zero alone would not do so: it must be compared with the real-time
function by a quantitative analytic estimate.

For arbitrary fixed depth, odd activations in the integrated strip class,
orthogonal training inputs in \(d=m+1\), and the existing common label
cap, there is a positive limiting probability that

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
       |f_n(t,x)-\widetilde f_n(t,x)|
 \ge c\frac{\gamma Y}{\sqrt{mn}\,[\log(en)]^{5/2}}. \tag{7}
\]

This is a weaker, near-root lower bound. It holds for both tanh and
permitted unbounded odd activations at every fixed depth. Its witnesses
are actual positive times near initialization. The more general formula
in that note uses the explicitly computable onset covariance on arbitrary
data whenever it is nonzero. This route relies on the inherited analytic
source event; the endpoint proofs in Sections 1--2 rely only on the
elementary initialized mixer estimates and the real fitting theorem.

## Exact meaning and unresolved scope

The all-time norm dominates its value at the endpoint, and also its value
at any positive time. Thus (1), (4) and (7) are legitimate lower bounds in
the common norm used by the compression comparisons. The converse
implication is false: a transient lower bound alone says nothing about
the endpoint.

These results settle the root-width exponent from below for substantive
canonical examples, including actual nonlinear fitted functions. They do
not prove a universal lower bound for every allowed activation and dataset:

- The label-direction quantity \(y^\top Q^{-1}y\) is not determined by
  \(Y,m,\gamma\). The weakest-direction replacement is an attained
  worst-case formula, not an inequality valid for all labels.
- If identity activations and \(m=d\) independent inputs are used, fitting
  fixes the entire linear function; the two endpoint predictors agree
  exactly. Even a positive \(\gamma\) and nonzero labels cannot force
  endpoint variability throughout the broad class.
- A constant last activation with one datum gives zero variability at
  every time despite a positive covariance gap.
- A matching general nonlinear sphere coefficient in \(d\), or an endpoint
  lower theorem for every full-span nonlinear dataset, remains unproved.
- The general upper theorem is still near-root and has a larger sample/gap
  coefficient. No assertion that all of its powers or subpolynomial width
  loss are necessary follows from these lower bounds.
- The dependence on \(m,\gamma,Y\) is displayed at each admissible task.
  Fixing positive \(Y,\gamma\) and also requiring \(Y\le c\gamma/m\)
  does not permit \(m\to\infty\). The label bound is not substituted
  into any variability formula.

No experiment, model modification, manuscript change or new population
approximation assumption is part of this continuation.
