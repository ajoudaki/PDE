# A rigorous late-query decoder, and its storage limitation

2026-10-05. Exact conditional construction, not a solution of the absolute
logarithmic-exponent target. Author: lead. Scientific inputs: the complete
finite-panel RESULT and integrated GENERAL_EXPLICIT_FITTING, explicitly
authorized for reuse. No external theorem or numerical experiment is used.

Use the original dense model, label allowance and high-probability fitting
event. There are m training inputs in R^d, normalized to length sqrt(d),
with label RMS Y and unweighted training feature-Gram gap gamma. Dense
width is n and hidden depth is L. Let s be the maximum of one and all
real activation Lipschitz constants. No bounded activation values are needed.

## 1. A width-independent spatial Lipschitz estimate

Write v=x/sqrt(d), so ||v||=1. The dense fitting theorem gives, for every
physical time including its limiting endpoint,

\[
\|A(t)\|_{\rm op}/\sqrt n\le9,\qquad
\|W^{(j)}(t)\|_{\rm op}\le9,\qquad
\|w(t)\|_2/\sqrt n\le2Y\sqrt{m/\gamma}.
\]

The first-layer feature difference divided by sqrt(n) is at most
9s||v-u||. Each next hidden layer multiplies this bound by at most 9s.
Cauchy--Schwarz in the normalized readout therefore proves

\[
|f_n(t,\sqrt d\,v)-f_n(t,\sqrt d\,u)|
\le 2Y\sqrt{m/\gamma}(9s)^L\|v-u\|.
\tag{1}
\]

This bound is uniform in width, time and the two unit inputs. The endpoint
case also follows by taking the pointwise limits in the finite-time bound.

## 2. Nearest-anchor decoding after training

Before compilation, select a finite set of unit anchors covering the unit
sphere within Euclidean distance h. Include their radius-sqrt(d) versions
as passive inputs in the finite-panel construction. Suppose its prediction
error at every anchor and every physical time is at most epsilon_0.

At a new input x, locate a nearest anchor u and return the compact model's
current prediction at sqrt(d)u. No label or prior trajectory at x is used.
The triangle inequality and (1) give the exact guarantee

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_{\rm decoded}(t,x)-f_n(t,x)|
\le\varepsilon_0+2Y\sqrt{m/\gamma}(9s)^L h.
\tag{2}
\]

This is a valid unseen-input decoder. It compares inputs, does not pretend
that nonlinear features are linear in input coordinates, and retains the
entire nonlinear training process of the finite-panel model. The uniform
error statement is conditional only on the indicated anchor approximation
and the original dense fitting event.

## 3. Why this certificate does not preserve logarithmic storage

For d>=2 and 0<h<=1/2, one Euclidean sphere cap of radius h has angular
radius 2 arcsin(h/2)<=2h. Its surface area is at most

\[
|S^{d-2}|\int_0^{2h}(\sin\theta)^{d-2}\,d\theta
\le \frac{|S^{d-2}|}{d-1}(2h)^{d-1}.
\]

The first formula holds also for the circle, where |S^0|=2. Since a cover
must cover the full area |S^{d-1}|, it needs at least

\[
\frac{(d-1)|S^{d-1}|}{2^{d-1}|S^{d-2}|}\,h^{-(d-1)}
\tag{3}
\]

anchors. To certify error epsilon from (2), allocating epsilon/2 to each
term requires h<=epsilon/[4Y sqrt(m/gamma)(9s)^L]. For fixed nonzero labels
and fixed problem parameters, (3) grows as epsilon^{-(d-1)}. At the
dense-variability target epsilon=n^(-1/2+o(1)), this is
n^((d-1)/2+o(1)) anchors; at epsilon=n^(-1+o(1)) it is
n^(d-1+o(1)). For an explicitly retained anchor list, storing its coordinates
already exceeds an absolute polylogarithmic budget for d>=2. Procedurally
generating a grid can avoid that particular list-storage cost; it does not
give a log(en)^5 bound from the available panel-dependent model-size
certificate. Anchor cardinality alone is not a memory lower bound for every
implementation of (2).

This is a limitation of this covering/Lipschitz certificate, NOT a lower
bound for every decoder, and NOT a necessary count for approximating the
particular dense function using additional structure. A sharper analytic
interpolant need not use an epsilon-net. The existing spatial analytic
source construction already achieves polylogarithmic counts, but its
exponent depends on d.

There is a separate probability issue: the finite-panel theorem is stated
for a fixed panel followed by a sufficiently large width. Its unquantified
threshold cannot simply be applied to the growing panel in this argument.
Consequently (2) is a deterministic extension lemma, not a new growing-panel
high-probability theorem. This qualification does not alter the geometric
storage obstruction to using (2) as the desired logarithmic certificate.

## 4. Check status and provenance

The lead reconstructed (1) from the full fitting proof, checked the triangle
inequality in (2), and derived (3) directly. After its own route was frozen,
unseen_uniform_sources reconstructed this complete note and confirmed those
equations. Its objection about procedural anchor generation led to the
explicit qualification above. This was a scoped internal check, not an
independent promotion review. No simulation was performed. This conditional
lemma does not strengthen the main compression theorem to the requested
unseen-input logarithmic decoder.

Read source hashes:

- finite-panel RESULT: `38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`.
- integrated GENERAL_EXPLICIT_FITTING: `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6`.
