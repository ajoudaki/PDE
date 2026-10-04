# Checking the same-width comparison against the existing results

2026-10-02. This is a bounded assessment of the manuscript and this study's finite-tail estimate, prompted by the question whether changing the target from population prediction to the dense network at the same width removes the unresolved bias. It does not change the study's main population-rate objective. No new experiment, manuscript edit, or Git write was performed.

## 1. Which remainder disappears

Use the manuscript's actual autonomous learning-speed closure, with clock \(\dot\tau=\widehat\rho\), \(\tau(0)=1\), the initialized forward prefix and zero backward prefix. Let \(\widehat f_{n,q}\) be its order-\(q\), width-\(n\) prediction, and \(f_{n,D}\) the canonical dense prediction at the same width, from the same Gaussian initialization and zero readout. Their training data and physical learning rates are the same. The closure uses its own responses and residuals. For a fixed test probability law \(\mu\) with finite second input moment, put
\[
\mathcal E_\mu(g,f)=\left(\int\sup_{t\ge0}|g(t,x)-f(t,x)|^2d\mu(x)\right)^{1/2}.
\]

The manuscript already proves, under its small-label and initial-Gram hypotheses,
\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
\le C_\mu[\omega(q)+b_n],\qquad
\omega(q)=q^{-2}e^{K\sqrt{\log(e+q)}}.
\tag{1}
\]
This follows from the parameter comparison and the whole-input bound in `paper/proof_tracking.tex`, lines 233--272. Its population conclusion subsequently adds
\[
d_{n,\mu}=\mathcal E_\mu(f_{n,D},f_\infty),\qquad
b_{n,\mu}=C_\mu b_n+d_{n,\mu}.
\tag{2}
\]
Thus the dense-to-population discrepancy, including its finite mean bias, is entirely absent from the new target. One should not estimate the new target by sending both systems through the population triangle inequality.

However, the current manuscript's \(b_n\) in (1) is a different proof remainder. Define the dense carriers by \(k_{D,a}^{(L)}=w_D\) and \(k_{D,a}^{(\ell)}=W_D^{(\ell+1)\top}\delta_{D,a}^{(\ell+1)}\) for \(\ell<L\), where \(\delta\) is the manuscript's backward response excluding the residual. If
\[
H_n(M,t)=\sum_{\ell=1}^L\max_a
 \frac{\|k_{D,a}^{(\ell)}(t)\mathbf1_{|k_{D,a}^{(\ell)}(t)|>M}\|_2}{\sqrt n},
\quad Z_n(M)=\int_0^\infty\rho_D(t)H_n(M,t)dt,
\]
then its Gaussian transfer proves \(Z_n(M)\le Ce^{-cM^2}+a_n\), with a qualitative \(a_n\to0\) in probability. It obtains
\[
b_n=C\Phi(a_n),\qquad \Phi(u)=u e^{K\sqrt{\log(e+1/u)}}\ (u>0),\quad \Phi(0)=0.
\]
This remainder estimates finite dense carrier tails; it is not the dense predictor's population bias. Changing the target alone does not remove it from that proof. Nor does its appearance prove a nonzero error floor at fixed width.

## 2. The existing finite-tail theorem removes that remainder in its structured scope

Now restrict to two tanh hidden layers, fixed orthonormal normalized inputs \(x_a^\top x_b/d=\mathbf1_{a=b}\), the canonical Gaussian initialization, zero readout, the initial feature-Gram gap, and sufficiently small fixed labels. These are the intersection of the hypotheses of this study's FINITE_TAIL_ROUTE.md and the manuscript's all-order fitting theorem. Let \(\mathcal G_n\) denote the common initialized event, whose probability tends to one. Dense and closure parameters fit and converge there, simultaneously for every order.

The checked finite-tail theorem gives, after defining \(Z_n=0\) off \(\mathcal G_n\),
\[
\mathbb E Z_n(M)\le C e^{-cM^2}\qquad(M\in\mathbb N,\ M\ge1),
\tag{3}
\]
uniformly in width. Its more precise estimate includes powers of the small activity bound, absorbed here into fixed constants. For tanh and a small enough activity bound, the readout carrier has no tail at integer \(M\ge1\). Equation (3) concerns the actual finite trained network and needs no population prediction rate.

Set \(A=\sum_{M\ge1}e^{-cM^2/2}<\infty\). Markov and a union bound imply
\[
\Pr\{\exists M\ge1:Z_n(M)>C_\delta e^{-cM^2/2}\}
\le \frac C{C_\delta}\sum_{M\ge1}e^{-cM^2/2}\le\delta/2
\tag{4}
\]
when \(C_\delta\ge2CA/\delta\). Intersect with \(\mathcal G_n\), allocating another \(\delta/2\) to its complement for sufficiently large \(n\). This yields one event of probability at least \(1-\delta\) on which
\[
Z_n(M)\le C_\delta e^{-cM^2/2}\quad\hbox{simultaneously for every integer }M\ge1.
\tag{5}
\]
No independence across neurons, samples, cutoffs, or training times is used. Setting \(Z_n=0\) off \(\mathcal G_n\) does not itself enforce the initialization event; the explicit intersection is necessary.

The same conclusion follows by averaging the stronger exponential moments of the time-supremum carriers in FINITE_TAIL_ROUTE.md and applying Markov once. Both routes retain weighted exceptional contributions instead of demanding that every neuron lie below one cutoff.

## 3. Direct consequence for autonomous closure tracking

The manuscript proves its deterministic comparison before invoking \(a_n\). In its notation, let
\[
D_{n,q}=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t)),
\quad A_M=C e^{K_0M}.
\]
Here \(d_n\) is read-in Frobenius difference divided by \(\sqrt n\), plus hidden-matrix Frobenius difference, plus readout Euclidean difference divided by \(\sqrt n\). Its cutoff conclusion is
\[
D_{n,q}\le C A_M Z_n(M)
 +C A_M\left[\frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M^2}{q^2},
\tag{6}
\]
provided \(C(1+M)A_M/q\le1/4\). All physical constants are independent of width, order, and time.

On the event (5), choose an integer
\[
M\le C_\delta+C\sqrt{\log(e+q)}
\]
large enough to make \(Z_n(M)\le q^{-2}\), and choose \(T\le C\log(e+q)\) large enough that \(e^{-\kappa T/2}\le q^{-1}\). The absorption condition holds for all \(q\) above a fixed threshold depending on \(\delta\) but not on width. Substitution in (6), absorbing polynomial logarithmic factors into the exponential, gives
\[
D_{n,q}\le C_\delta q^{-2}e^{K\sqrt{\log(e+q)}}.
\tag{7}
\]
The finitely many smaller orders obey the same inequality after enlarging \(C_\delta\), using the manuscript's common physical bound on \(D_{n,q}\). Thus (7) holds simultaneously for every order on the one event just constructed. The coefficient \(K\) can be independent of \(\delta\); its cutoff offset only enlarges \(C_\delta\).

The manuscript's forward estimate
\[
|\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|
\le C(1+\|x\|/\sqrt d)\,d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t))
\]
then gives the direct comparison
\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
\le C_{\delta,\mu}q^{-2}e^{K\sqrt{\log(e+q)}}.
\tag{8}
\]
There is no additive width remainder or unproved local response hypothesis H in this consequence of the checked finite-tail input. It covers the full physical trajectory, its fitted endpoint, and any fixed test law with finite second moment. A supremum over a fixed bounded query set is covered by the same forward estimate.

This is a new checked implication of the current ingredients, not a theorem already stated in the manuscript and not a promotion review. It is not asserted for arbitrary geometry, depth, activation, or label magnitude.

## 4. Obtaining a strict root-width target, and the storage meaning

Let \(K\) be the final coefficient in (8). Choose a fixed \(A>K/4\), and put
\[
q_n=\left\lceil n^{1/4}e^{A\sqrt{\log(e+n)}}\right\rceil.
\tag{9}
\]
Then
\[
\sqrt n\,\omega(q_n)
=\exp\{(-2A+K/2)\sqrt{\log n}+KA+o(1)\}=O(1).
\]
Consequently (8) gives the strict same-width bound \(C_{\delta,\mu}/\sqrt n\), with constants independent of width and time. The order is \(n^{1/4+o(1)}=o(n)\). For fixed \(m,d\), the two-layer evolving-state count is
\[
2mnq_n+n(d+1)+O(1)=n^{5/4+o(1)},
\]
versus \(n^2+n(d+1)\) dense evolving parameters. The original random mixer \(W_0\) is still stored exactly with \(n^2\) fixed entries. Neither total storage nor matrix-vector runtime is claimed to become \(n^{5/4+o(1)}\).

Width alone does not make the bound vanish at fixed \(q\), including \(q=1\). The approximation parameter here is the memory order. Increasing width while leaving the memory order fixed does not discharge its truncation error.

The small-label hypothesis is also retained: the large-label one-sample result in this study proves fitting of the dense flow, not the all-order closure fitting needed by (6). No unrestricted-label closure theorem is inferred from it.

## Inputs and check provenance

The coordinator read the complete current `results.tex` and `proof_tracking.tex`, the relevant closure definition and the complete all-order fitting portion of `proof_alltime.tex`; the full manuscript and included material had already been read earlier and their hashes remain unchanged. The own-study finite-tail proof and its weighted-tail conclusion were checked against the comparison. No unrelated study was accessed.

A fresh scoped agent independently read the authorized manuscript sources and confirmed the two distinct remainders, exact clock, and direct whole-input implication. It was then supplied the self-contained already-checked finite-carrier exponential-moment statement. It reconstructed (5) by the exponential-average route, (6)--(8), the common event and all-order quantifiers, and the asymptotic choice (9). Its assessment explicitly conditions on that supplied finite-tail theorem; the coordinator verified that theorem's complete statement and proof in this study. This is collaborative internal checking.

Frozen source SHA-256:

```text
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1  paper/results.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
da251f231832e69c74581ba4291e649d1322737eebd46b2a4d9c6ca1a8dd0d65  FINITE_TAIL_ROUTE.md
```
