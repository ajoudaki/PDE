# A smaller original closure at strict root-width accuracy

2026-10-03. **Internally checked positive result for two tanh hidden layers.**
This improves the sufficient order in the actual Legendre response-memory
closure. It meets the requested moving-state target by retaining fewer
history modes, while keeping every neuron and the exact initialized mixer.
It is not a low-discrepancy neuron-sampling theorem.

## Precise result

Fix \(m,d\), a finite sphere training dataset \(\|x_a\|_2=\sqrt d\),
and compatible fixed labels: equal inputs have equal labels and antipodal
inputs have opposite labels. The label RMS is sufficiently small under the
same geometry-dependent threshold as the prior finite-carrier theorem.
There is no input orthogonality assumption. Use two tanh hidden layers of
width \(n\), no biases, independent canonical Gaussian initialization,
and exactly zero initial readout. The initialization is shared by all
compared models.

Let \(\widehat f_{n,q}(t,x)\) denote the manuscript's actual autonomous
order-\(q\) residual-RMS response-memory predictor. Let \(\mu\) be any
fixed query probability law with finite second moment. For a sufficiently
large fixed \(a>0\), put
\[
 p_n=\left\lceil n^{1/6}
           \exp\{a\sqrt{\log(e+n)}\}\right\rceil,\qquad
 p=\min\{q,p_n\}.
\]
For every fixed confidence \(1-\delta\), at every sufficiently large
width, on a common event of probability at least \(1-\delta\),
\[
 \sup_{q\ge1}
 \left(\int\sup_{t\ge0}
  |\widehat f_{n,\min(q,p_n)}(t,x)-\widehat f_{n,q}(t,x)|^2\,d\mu(x)
 \right)^{1/2}
 \le \frac{C_\mu}{\sqrt n}.
\]
The constants and order schedule are independent of width and physical
time; the sufficiently-large-width threshold may depend on confidence,
the fixed geometry and labels. Zero labels give identical stationary
predictions. No simultaneous event over infinitely many independently
initialized widths is asserted.

The same order-\(p_n\) closure is itself \(C_\mu/\sqrt n\)-close to the
actual width-\(n\) dense run with the same initialization, for the entire
physical trajectory. Every compared system fits and converges under the
existing assumptions, so these bounds include the fitted limit. A uniform
absolute-error bound on each fixed bounded query set also follows.

The moving coordinate count is
\[
 2mnp+n(d+1)+1
 \le 2mnp_n+n(d+1)+1
 =n^{7/6+o(1)}.
\]
For the previous sufficient order \(q=n^{1/4+o(1)}\), the improvement is

| Representation | Sufficient memory order | Moving scalar coordinates |
|---|---:|---:|
| Previous certificate | \(n^{1/4+o(1)}\) | \(n^{5/4+o(1)}\) |
| New certificate for the same closure family | \(n^{1/6+o(1)}\) | \(n^{7/6+o(1)}\) |

In particular, for every fixed \(0<\epsilon<1/12\), the new count is
\(O(n^{5/4-\epsilon})\). This is a power saving, not only removal of
logarithms. The result is asymptotic; it supplies no useful numerical width
threshold or practical speed claim.

## The smaller construction

Use the original equations, changing only the number of stored modes from
\(q\) to \(p\). The moving state consists of \(W^{(1)},w,\tau\) and,
for each training sample and \(j=0,\ldots,p-1\),
\[
 \bar h_{a,j}^{(1)}\in\mathbb R^n,\qquad
 \bar\delta_{a,j}^{(2)}\in\mathbb R^n.
\]
These are the original raw Legendre moments of the forward history and
the residual-weighted backward history, with the original unit prefix.
The clock obeys \(\dot\tau=\rho\), using this smaller model's own
residual. All responses, memory writes, first-layer updates and readout
updates use its own current reconstructed network.

The learned hidden action is still evaluated through
\[
 \widehat W
 =W_0-\frac2{mn\tau}
   \sum_a\sum_{j<p}(2j+1)
       \bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\]
The same fixed \(W_0\) and its transpose are applied exactly. There is
no trained dense matrix in the stored state. Initialization uses only the
original Gaussian arrays: the zeroth forward moment is the initial
feature, and all other moments start at zero. No larger closure or dense
training trajectory needs to be run first. The smaller system remains
autonomous and restartable from its own state.

The exact fixed mixer still requires \(n^2\) fixed numbers and dense
matrix-vector operations. The proved saving concerns learned/moving
coordinates, as in the original compression theorem. It does not reduce
those fixed storage or runtime costs.

## Why fewer moments suffice

The old sufficient rate combined two first-order projection bounds,
producing roughly \(q^{-2}\). The new proof improves just the forward
factor.

Zero initial readout implies zero initial first-layer feature velocity.
Consequently, when the forward history begins after its constant unit
prefix, both its value and its first derivative agree across that join.
The backward history generally has only value continuity.

At a current clock endpoint \(A=\tau(t)\), define the Legendre
differential operator
\[
 \mathcal L_A h
 =-\partial_\xi\!\left[\xi(A-\xi)\partial_\xi h\right].
\]
Its polynomial eigenvalues are \(j(j+1)\). Two integrations by parts,
with the interface terms canceled by the matching first derivative, give
\[
 \frac{\|(I-\Pi_q^A)h\|_{L^2}}{\sqrt n}
 \le \frac{\|\mathcal L_Ah\|_{L^2}}{\sqrt n\,q(q+1)}.
\]
This provides a second power of \(q^{-1}\) for the forward history.

Differentiating the normalized residual \(r/\rho\) appears to create an
inverse residual near fitting. The small-label fitting estimate gives
\[
 A-\tau(s)\le\int_s^\infty\rho(u)\,du\le\rho(s)/\kappa.
\]
The vanishing factor in \(\mathcal L_A\) cancels that singularity.
The argument is performed at every finite physical time with a common
bound, so it does not assume a smooth extension through the fitted
clock endpoint.

Let \(K_q\) denote the actual closure's largest first-layer backward
carrier, and let
\(\epsilon_q=\int_0^\infty\|E_2(t)\|_Fdt\), where \(E_2\) is its
exact extra hidden-matrix velocity relative to dense gradient flow
evaluated at that closure state. The two history estimates and the
projection-energy identity give
\[
 \epsilon_q
 \le C(1+K_q)\frac{\sqrt{\log(e+q)}}{q^3}.
\]
The proof controls total absolute defect, not merely a signed integral
that might conceal later feedback.

The remaining issue is that the closure's \(K_q\) is not assumed small.
Let \(D_{n,q}\) be its all-time normalized parameter distance from the
same initialized dense run. The already proved finite dense-carrier
maximum and direct subtraction imply
\[
 K_q\le C\sqrt{\log(e+n)}+C\sqrt n\,D_{n,q}.
\]
The existing all-time damping estimate then yields
\[
 D_{n,q}\le
 C e^{K\sqrt{\log(e+n)}}\,
 \frac{\sqrt{\log(e+q)}}{q^3}
 \left[1+\sqrt{\log(e+n)}+\sqrt nD_{n,q}\right].
\]
At \(q=p_n\), the coefficient of \(D_{n,q}\) on the right tends to
zero and can be absorbed. The remaining error is \(C/\sqrt n\).
This closes the feedback dependence; it is not a new assumed response
bound.

Finally, orders above \(p_n\) obey the same estimate. Comparing each of
them and the order-\(p_n\) model to the same dense realization gives the
displayed direct closure-to-closure theorem. Orders below \(p_n\) are
left identical. Thus every deterministic truncation bias is included.
There is no population replacement and no missing finite-width population
bias or sampling bias.

## What happened to neuron sampling

The separate neuron-sampling route derived exact obstructions to simple
schemes, without proving a general impossibility result. Conditioning the
Gaussian mixer on all initial training forward fields still leaves an
orthogonal Gaussian component that contributes to the actual initial
backward response. Selecting rows using only those forward fields misses
that component. For a specified unseen query, such sampling also retains
a conditional mean-square error of order \(1/N\) in an initial prediction
coefficient when only \(N\) rows are retained.

These statements are restricted to the specified sampling information.
They do not rule out response-aware quadrature, control variates, or a
different finite representation. The present power saving does not require
resolving those additional sampling questions.

## Proof, checks, and scope

- [HISTORY_APPROXIMATION_ROUTE.md](HISTORY_APPROXIMATION_ROUTE.md):
  complete construction, weighted derivative proof, closed feedback
  estimate, probability transfer, direct original-closure comparison.
- [HISTORY_APPROXIMATION_CHECK.md](HISTORY_APPROXIMATION_CHECK.md):
  complete separate internal reconstruction, including the authorized
  finite-network carrier proof chain.
- [COORDINATOR_CHECK.md](COORDINATOR_CHECK.md):
  separate complete reconstruction by the coordinator and a check of the
  neuron-sampling calculations.
- [NEURON_SAMPLING_ROUTE.md](NEURON_SAMPLING_ROUTE.md):
  exact Gaussian sampling calculations and the unresolved adaptive
  quadrature route.

The theorem is restricted to two tanh hidden layers and the existing
small-label compatible-data setting. It does not establish arbitrary-depth
\(n^{7/6+o(1)}\) compression, an optimal memory order, large-label
compression, or a dense-to-population rate. The new estimate strengthens
the previous sufficient memory-order certificate; it does not contradict
that older valid bound.

These are internally checked research results, not promoted book or
manuscript theorems. No experiment or manuscript edit was made.

The complete checked proof has SHA-256
46fc0584660bc45bda7cfeb6e4b6a63151559f79c96005ad3794799048d2477f.
Its frozen candidate-stage header records the submission status before
reconstruction; both completed check reports establish the current PASS.
