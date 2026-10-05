# Internal reconstruction of the two-tanh endpoint lower bound

2026-10-04. Scoped adversarial reconstruction by the dense-comparison
subagent. This is an internal check, not an independent promotion review.
The reviewer previously authored the linear endpoint note but did not use
it as a scientific input to this reconstruction.

## Inputs and verdict

The complete 463-line candidate and complete 410-line fitting source were
read. The coordinator subsequently corrected the cubic-product
normalization and presentation; the final input hashes are recorded below.
The coordinator additionally authorized a consistency check of the common
setup and Sections 1–2 of the endpoint synthesis. No other scientific
source, prior review, experiment, or external theorem lookup was used.

| Input | SHA-256 | Scope |
|---|---|---|
| TANH_ENDPOINT_VARIABILITY_LOWER.md | 227a88cb199ea84a8f2ec8bfce1c7eb3589dd1be5d7bab0818f37e1c5c04ae67 | Complete proof |
| GENERAL_EXPLICIT_FITTING.md | 5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6 | Complete source |
| ENDPOINT_LOWER_RESULT.md | 14e97aabaaebdcacb41e927674e7344921a2f2a6afb9305197c9fddca23982f7 | Common setup and Sections 1–2 only |

**Verdict: PASS for the stated, sufficiently-large-width, fixed-query
endpoint lower bound for two tanh hidden layers.** The argument applies
to the actual trained parameters and preserves the stated label energy
\(y^\top Q^{-1}y\). No unproved trained-Gaussian assumption, independence
between trained mixer rows, or replacement by a frozen-feature flow is
needed. A finite mixer-event certificate is supplied below to make the
probability quantifier independently checkable.

This verdict is restricted to the theorem's stated hypotheses: a proper
training-input span, positive top covariance gap, the displayed small-label
allowance, and two tanh hidden layers. It establishes neither a general
activation lower bound nor a sharp dimension factor for the tanh sphere
supremum.

## 1. Canonical dynamics and the conditioning event

Use the candidate's notation
\[
 f(v)=\frac1n w^\top\tanh(W\tanh(Av)),\qquad
 Y=\frac{\|y\|}{\sqrt m},\qquad
 \lambda=\frac{\gamma}{m},\qquad
 S=\operatorname{span}\{v_1,\ldots,v_m\}.
\]
The displayed three block equations are exactly minus the gradients of
the mean squared loss with mobilities \((n,1,n)\). In particular,
the factor \(1/n\) in the mixer equation and its absence in the read-in
equation are correct.

Every read-in velocity is a sum of vectors times \(v_a^\top\), so
\(\dot A P_{S^\perp}=0\). The active finite-dimensional initial data are
\((A_0|_S,W_0)\). All active training quantities, including the endpoint
\((A_\infty|_S,W_\infty,w_\infty)\) on the fitting event, are functions
of these data alone. In orthonormal input coordinates, the unused columns
of \(A_0\) are an independent standard Gaussian block. Thus for each
fixed unit \(v\in S^\perp\),
\[
 Z=A_0v\sim N(0,I_n)
\]
conditionally on the active initialization, without changing its law.
This also holds after conditioning on any fitting or mixer event
measurable with respect to that initialization.

The fitting source is legitimately applied in dimension \(\dim S\).
No ambient-input operator event is imposed on the unused Gaussian block.
Its constants specialize to \(H=s=1\), \(F=85\), \(U_2=2\);
the source's exact second-derivative constant is
\(t_2=4/(3\sqrt3)\). The candidate's assumption
\(Y\le10^{-6}\lambda\) implies \(Y\le\lambda/(8\sqrt{85})\).
At width at least the source's \(N_{\rm fit}(\varepsilon)\), with
input dimension replaced by \(\dim S\), the event therefore supplies
\[
 \|W_\infty\|_{\rm op}<9,\qquad
 \|W_\infty-W_0\|_F\le16Y^2\lambda^{-3/2},\qquad
 \frac{\|w_\infty\|}{\sqrt n}\le\frac{2Y}{\sqrt\lambda}.
\]
It also supplies global existence, finite total parameter path length,
parameter convergence, and exact interpolation. These conclusions follow
directly from the source's energy and continuation proof, rather than an
exchange of infinite-width and infinite-time limits.

## 2. Distinct-coordinate coefficients and their error

Let \(H_j=\tanh Z_j\), and let
\(\sigma^2=\mathbb E H_j^2\). The elementary bounds in the candidate give
\(1/16<\sigma^2\le1\). For every three-element subset \(J\), the required
normalization is
\[
 \psi_J(H)=\prod_{j\in J}(H_j/\sigma)
          =\sigma^{-3}\prod_{j\in J}H_j.
\]
The products are orthonormal: unequal subsets leave at least one centered
coordinate to its first power, and the norm of each product is one.

For a row \(b\), write \(C_{b,J}=\mathbb E[\tanh(b^\top H)\psi_J(H)]\).
Subtracting a constant inside a centered expectation gives exactly
\[
 \mathbb E[H F(u+bH)]
 =b\,\mathbb E\!\left[H^2\int_0^1F'(u+tbH)\,dt\right].
\]
Three successive applications yield
\[
 C_{b,J}
 =\sigma^3\prod_{j\in J}b_j\,
   \mathbb E\tanh'''\!\left(
     \sum_{p\notin J}b_pH_p+\sum_{j\in J}b_jT_j\widehat H_j
   \right),
\]
where \(T_j\) are independent uniform variables on \([0,1]\) and
\(\widehat H_j\) have the symmetric probability law tilted by
\(H_j^2/\sigma^2\). All these variables can be taken independent.
The second sum has mean zero and variance at most
\(\sum_{j\in J}b_j^2\), because
\(\mathbb E\widehat H_j^2=\mathbb E H_j^4/\sigma^2\le1\).

Let \(M_5=\|\tanh^{(5)}\|_\infty\) and
\(M_7=\|\tanh^{(7)}\|_\infty\), with norms on the real line.
Removing the shifted sum costs at most
\((M_5/2)\sum_{j\in J}b_j^2\). Replacing each remaining \(H_p\) by
\(\sigma Z_p\) matches the first three moments. Taylor expansion through
degree three bounds its total cost by
\[
 \frac{M_7}{24}\sum_{p\notin J}|b_p|^4
       \big(\mathbb E H_p^4+3\sigma^4\big)
 \le\frac{M_7}{6}\sum_{p\notin J}b_p^4.
\]
Restoring the missing Gaussian coordinates costs at most another
\((M_5/2)\sum_{j\in J}b_j^2\). Consequently the claimed coefficient
estimate is correct, with, for example,
\[
 C=M_5+M_7/6<6400.
\]
For an entirely algebraic bound, the fifth and seventh derivative
polynomials are
\[
 P_5(u)=16-136u^2+240u^4-120u^6,
\]
\[
 P_7(u)=-272+3968u^2-12096u^4+13440u^6-5040u^8.
\]
Their absolute coefficient sums give \(M_5\le512\) and \(M_7\le34816\).
Thus the estimate does not conceal a dependence on the width, data, or
labels. Zero coefficients \(b_j\) cause no division and give exact zero.

## 3. The negative coefficient and covariance gap

For \(s=\sigma\|b\|\in[1/5,6/5]\), two Gaussian integrations by parts
give
\[
 s^2\mathbb E\tanh'''(sZ)
 =\mathbb E[(Z^2-1)\operatorname{sech}^2(sZ)]
 =\operatorname{Cov}(Z^2,\operatorname{sech}^2(sZ)).
\]
The covariance integrand in the independent-copy formula is everywhere
nonpositive. On either orientation of
\(\{|Z|\le1/2,\ |Z'|\ge3/2\}\), its magnitude is at least \(2/300\).
The stated probability lower bounds \(1/3\) and \(1/20\) therefore give
covariance magnitude at least \(1/9000\). Since \(s^2\le36/25\) and
\(\sigma^3\ge1/64\), the candidate's coefficient bound
\[
 a(b)=\sigma^3\mathbb E\tanh'''(\sigma\|b\|Z)\le-10^{-6}
\]
is conservative and correct on \(0.9\le\|b\|\le1.1\).

The matrix \(U_{i,J}=\prod_{j\in J}b_{ij}\) has the exact Gram identity
\[
 (UU^\top)_{ik}
 =\frac{(\sum_jp_j)^3-3(\sum_jp_j)(\sum_jp_j^2)
                     +2\sum_jp_j^3}{6},
 \qquad p_j=b_{ij}b_{kj}.
\]
This is the elementary symmetric polynomial of degree three; repeated
indices are removed exactly. The candidate uses the Gaussian row inner
products only on this initialized matrix. It does not assume that trained
rows are independent.

Here is a concrete finite-width certificate for the event used in the
proof. Fix \(0<\varepsilon<1\), and put
\[
 \ell=\log(8n^2/\varepsilon),\qquad a=\sqrt{2\ell/n}.
\]
Suppose
\[
 n\ge200\ell,\qquad
 (n-1)(a^3+a^4/2)\le1/40,
\]
\[
 \frac{30000\ell}{\sqrt n}
 \le\frac{10^{-6}}{\sqrt{40}}-10^{-7}.
 \tag{C}
\]
These conditions hold for every sufficiently large \(n\); all constants
are independent of the training set. Gaussian entry tails, stopped
conditional Gaussian inner-product tails, and the row-norm moment
generating function give, with failure at most \(\varepsilon\),
\[
 0.9\le\|b_i\|\le1.1,\qquad
 \max_{ij}|b_{ij}|\le a,\qquad
 \max_{i\ne k}|b_i^\top b_k|\le1.1a.
\]
Indeed the entry and stopped inner-product unions each cost at most
\(2n^2e^{-\ell}=\varepsilon/4\). The two row-norm tails cost at most
\(2ne^{-n/200}\le\varepsilon/4\), using the elementary Chernoff
rates at squared norms \(0.81\) and \(1.21\).

On this event, the diagonal of \(UU^\top\) is at least
\[
 \frac{0.81^3}{6}-\frac{1.21^2a^2}{2}>\frac1{20},
\]
and every off-diagonal absolute entry is at most \(a^3+a^4/2\).
Thus (C) implies \(UU^\top\succeq I/40\).
For the coefficient error matrix, the preceding estimate gives
\[
 \|C-\operatorname{diag}(a(b_i))U\|_F
 \le6400(1.21+3)a^2\sqrt n\,\frac{1.1^3}{\sqrt6}
 <\frac{30000\ell}{\sqrt n}.
\]
The smallest singular value of the coefficient matrix is consequently
at least \(10^{-7}\). Orthogonal projection in \(L^2(H)\) now proves
the initialized feature covariance lower bound \(10^{-14}I\).
This also verifies the claimed norm of the error: it is a Frobenius
bound over all rows and all distinct triples, with order
\(\log(n)/\sqrt n\), not an entrywise estimate incorrectly substituted
for an operator bound.

## 4. Training perturbation and label energy

For every deterministic perturbation \(E\), coordinate independence and
the Lipschitz property of tanh give
\[
 \mathbb E_H\|\tanh((W_0+E)H)-\tanh(W_0H)\|^2
 \le\sigma^2\|E\|_F^2.
\]
By Cauchy--Schwarz, the coefficient-to-function operator from Euclidean
space to \(L^2(H)\) changes by at most \(\sigma\|E\|_F\).
Since \(\gamma\le Q_{aa}\le1\), we have \(\lambda\le1\), and the
actual trained perturbation obeys
\[
 \|W_\infty-W_0\|_F\le16\cdot10^{-12}\sqrt\lambda
 <\tfrac12\,10^{-7}.
\]
The trained feature covariance therefore has lower bound
\((10^{-7}/2)^2I\succeq10^{-16}I\). The inequality holds uniformly
over every active endpoint satisfying the fitting bounds, so dependence
of that endpoint on \(W_0\) creates no conditioning problem.

The initialization proof in the fitting source gives the full operator
estimate
\(\|\mathsf H_0^\top\mathsf H_0/n-Q\|_{\rm op}\le\gamma/2\);
it gives more than a minimum-eigenvalue statement. Its physical feature
displacement, multiplied from the normalized training-matrix scale by
\(\sqrt m\), gives
\(\|\mathsf H_\infty-\mathsf H_0\|_{\rm op}/\sqrt n\le\sqrt\gamma/8\).
Hence for every \(u\),
\[
 \frac{\|\mathsf H_\infty u\|}{\sqrt n}
 \le\left(\sqrt{3/2}+1/8\right)\sqrt{u^\top Qu}
 <\sqrt{2u^\top Qu}.
\]
Interpolation and \(u=Q^{-1}y\) then give
\[
 y^\top Q^{-1}y
 =\frac{w_\infty^\top\mathsf H_\infty Q^{-1}y}{n}
 \le\frac{\|w_\infty\|}{\sqrt n}
               \sqrt{2y^\top Q^{-1}y}.
\]
Thus the claimed \(\|w_\infty\|^2/n\ge
\tfrac12y^\top Q^{-1}y\) is correct. Positivity of this label energy
uses precisely \(y\ne0\) and \(Q\succ0\).

## 5. Conditional moments, probability, and endpoint status

Condition on two active initializations satisfying their fitting and
mixer events. For each copy the remaining query map
\[
 Z\longmapsto n^{-1}w_\infty^\top
              \tanh(W_\infty\tanh Z)
\]
is odd and has Lipschitz constant at most \(9\|w_\infty\|/n\).
Gaussian Poincare applied to this map and its square yields the stated
second moment and fourth-moment bound \(5K^4\). All functions here are
smooth and have finite Gaussian moments, so the source's Hermite
justification has its integrability hypotheses.

For the difference \(D\) of the two query outputs, set
\[
 R=\frac{\|w_\infty\|^2+\|\widetilde w_\infty\|^2}{n^2}.
\]
The two query Gaussian vectors remain independent after this
conditioning. Their means are zero. The covariance lower bound gives
\(\mathbb E[D^2\mid\mathrm{active}]\ge10^{-16}R\).
Expansion of the fourth power gives individual coefficients \(5,5\)
and cross coefficient \(6\); bounding \(6\le10\) yields
\[
 \mathbb E[D^4\mid\mathrm{active}]\le5\cdot9^4R^2.
\]
Paley--Zygmund at half the conditional second moment consequently gives
conditional probability at least
\[
 p_0=\frac{10^{-32}}{20\cdot9^4}
\]
for \(|D|\ge\sqrt{10^{-16}R/2}\).
The readout-energy lower bounds in both copies give
\(R\ge y^\top Q^{-1}y/n\). There are four required active events:
one fitting and one mixer event for each copy. Taking each failure
probability at most \(1/8\) gives their intersection probability at least
\(1/2\), without any assumed independence between fitting and mixer
events in the same copy. Thus
\[
 c=10^{-8}/\sqrt2,\qquad
 p=\frac{10^{-32}}{40\cdot9^4}
\]
are valid constants in the candidate's statement. A sufficient width
is the reduced \(N_{\rm fit}(1/8)\) together with (C) for
\(\varepsilon=1/8\). The certificate is conservative but finite.

These are probabilities for each individual sufficiently large width.
The proof does not claim a simultaneous event over an infinite sequence
of independently initialized widths.
The limiting parameters are those of the actual physical flow, and the
query identity follows by their convergence and continuity of the
finite network. A fixed endpoint query lower-bounds the endpoint sphere
norm. It also lower-bounds the supremum over finite physical times by
taking the limit along that same query, even if the time supremum is
defined without adjoining an explicit infinite-time point.

## 6. Additional upper bound and synthesis consistency

The coordinator's additional fixed-query upper bound is valid and
requires no covariance-gap event. On the two reduced fitting events,
\[
 \mathbb E[D^2\mid\mathrm{active}]
 \le81R\le648\,\frac{Y^2}{\lambda n}.
\]
Conditional Chebyshev at threshold
\(36Y/\sqrt{\delta\lambda n}\) has failure at most \(\delta/2\).
Taking each fitting-event failure at most \(\delta/4\) gives
\[
 \Pr\!\left\{\text{both endpoints fit and }
 |D|\le36Y\sqrt{\frac{m}{\delta\gamma n}}\right\}\ge1-\delta.
\]
Its width condition is the reduced \(N_{\rm fit}(\delta/4)\).
This is an upper bound at the same fixed orthogonal query, not an upper
bound on the sphere supremum.

Section 1 of the synthesis uses exactly the checked tanh scope and
constants. Its one-datum acceleration formulas follow by differentiating
the canonical equations at \(w_0=0\), \(r_0=-y\); both hidden blocks have
the displayed nonzero accelerations almost surely. This is consistent
with the proof's use of actual training.

Section 2's distinction between its linear-subclass sphere bound and the
tanh fixed-query bound is appropriate. Its weakest-eigenspace
specialization must remain explicit for the bounds involving
\(Y\sqrt{m/\gamma}\). The linear theorem itself is not independently
re-reviewed here: its proof was outside the frozen scientific inputs of
this tanh reconstruction.

## 7. Corrections and remaining limitations

The initial candidate displayed the ambiguous expression
\(\prod_{j\in J}H_j/\sigma\). Its orthonormality assertion and subsequent
expansion require \(\sigma^{-3}\prod_{j\in J}H_j\); this was reported
and corrected by the coordinator. The phrase “entire trained state”
must refer to the active trained state: the full read-in matrix still
contains the unused Gaussian block and is not independent of it.
The Gaussian covariance identity uses two integrations by parts.
These local presentation corrections do not change the argument.

The final mathematical limitations are substantive and correctly stated:

- The tanh proof treats exactly two hidden layers and a fixed unused
  input direction. It does not prove the same statement at arbitrary
  nonlinear depth.
- A nonzero orthogonal complement of the training span is essential
  to this conditional-law construction.
- For arbitrary labels the lower coefficient is
  \(\sqrt{y^\top Q^{-1}y}\). In general it cannot be replaced from below
  by \(Y\sqrt{m/\gamma}\); equality requires the indicated label
  eigenspace, or \(Q=\gamma I\).
- The lower probability is a fixed positive constant, not a
  high-confidence pairwise separation guarantee. The stated width
  certificate and probability constants are very conservative.
- The proof supplies no additional factor \(\sqrt{d-\dim S}\) for the
  tanh sphere supremum and does not cover a spanning training set.

No material mathematical failure remains in the intended, corrected
theorem within these limits.
