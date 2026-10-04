# Removing an auxiliary cutoff: what finite moments suffice

This is a conditional probability-transfer lemma, not a proof of the requested dense width rate. It concerns the actual dense flow and the actual auxiliary dense flow defined in `CUTOFF_REMOVAL_ROUTE.md`. No response-memory dynamics enter it.

## 1. Model, event, and observable

Use the manuscript's fixed finite dataset, depth, Gaussian initialization, zero readout, and canonical mobilities. Let \(\mathcal G_n\) be its initialization event on which the small-label dense flow and the clipped flow have global existence, exponential fitting, and uniform physical bounds. Write \(\rho_n(t)\) for the original dense residual RMS, and assume the deterministic estimate

\[
\rho_n(t)\le Y e^{-\kappa t}\quad\text{on }\mathcal G_n.
\]

Here \(Y\) is the fixed label RMS and \(\kappa>0\) is independent of width, cutoff, and time. The full original backward carriers are

\[
p_{n,a}^{(L)}=w_n,\qquad
p_{n,a}^{(\ell)}=W_n^{(\ell+1)\top}\delta_{n,a}^{(\ell+1)}
\quad(\ell<L).
\]

The activation derivative multiplies this carrier to produce \(\delta\). The cutoff is applied to carriers in the auxiliary recursion, including the readout carrier. Define

\[
H_n(M,t)=\sum_{\ell=1}^L\max_{1\le a\le m}
 \frac{\|p_{n,a}^{(\ell)}(t)
  \mathbf1_{\{|p_{n,a}^{(\ell)}(t)|>M\}}\|_2}{\sqrt n},
\qquad
Z_n(M)=\mathbf1_{\mathcal G_n}\int_0^\infty\rho_n(t)H_n(M,t)\,dt.
\]

The indicator inside a vector acts coordinatewise. A test probability law \(\mu\) has finite second input moment. The error is the manuscript's \(\mathcal E_\mu\), with the time supremum inside the input integral.

## 2. Marginal finite-network tails are enough for cutoff removal

**Proposition (conditional only on the displayed finite moment estimate).** Suppose constants \(b,B>0\), independent of \(n,i,t\), satisfy

\[
\sup_{n,t\ge0,\ell,a,1\le i\le n}
 \mathbb E\!\left[
 \mathbf1_{\mathcal G_n}
 e^{b|p_{n,a,i}^{(\ell)}(t)|^2}\right]\le B.
\tag{1}
\]

These are moments of the **actual finite original network**. No time supremum is assumed inside the exponential. Then constants \(c,C>0\), independent of width and time, give

\[
\mathbb E Z_n(M)^2\le C e^{-cM^2}.
\tag{2}
\]

Combining this with the deterministic cutoff-removal estimate

\[
\mathbf1_{\mathcal G_n}\mathcal E_\mu(f_n,f_{n,M})
 \le C_\mu e^{KM} Z_n(M)
\tag{3}
\]

gives, after changing \(c,C_\mu\),

\[
\mathbb E\!\left[
 \mathbf1_{\mathcal G_n}\mathcal E_\mu(f_n,f_{n,M})^2\right]
 \le C_\mu e^{-cM^2}.
\tag{4}
\]

Consequently, for a sufficiently large fixed \(A\) and
\(M(n)=A\sqrt{\log(e+n)}\),

\[
\Pr\!\left\{
 \mathcal G_n\ \text{and}\
 \mathcal E_\mu(f_n,f_{n,M(n)})>
 \frac{C_\mu}{\sqrt{\delta n}}
 \right\}\le\delta.
\tag{5}
\]

**Proof.** For every real \(v\),

\[
v^2\mathbf1_{|v|>M}
 \le \frac{2}{be}e^{-bM^2/2}e^{bv^2}.
\]

Indeed \(v^2e^{-bv^2/2}\le2/(be)\), and
\(e^{-bv^2/2}\le e^{-bM^2/2}\) on the indicated set. Squaring the sum in \(H_n\), then replacing each maximum by the sum over samples, gives

\[
\mathbb E[\mathbf1_{\mathcal G_n}H_n(M,t)^2]
\le L\sum_{\ell,a}\frac1n\sum_i
 \mathbb E[\mathbf1_{\mathcal G_n}|p_{n,a,i}^{(\ell)}(t)|^2
              \mathbf1_{|p_{n,a,i}^{(\ell)}(t)|>M}]
\le C e^{-bM^2/2}.
\]

Cauchy--Schwarz with the deterministic measure
\(Y e^{-\kappa t}\,dt\) yields

\[
Z_n(M)^2\le\frac{Y}{\kappa}
 \int_0^\infty Y e^{-\kappa t}
 \mathbf1_{\mathcal G_n}H_n(M,t)^2\,dt.
\]

Tonelli proves (2). Multiply by (3) squared and use
\(2KM-cM^2\le C_K-cM^2/2\) to obtain (4). Choose \(A\) so that the resulting \(cA^2\ge1\); Markov's inequality proves (5). For \(Y=0\) both paths are stationary and the result is immediate. No independence of neurons, times, residuals, or carriers was used. ∎

This proves that **controlling the maximum of every neuron over every training time is unnecessary for cutoff removal**. Uniform marginal exponential moments of the finite flow suffice, because errors enter with an integrable residual weight. It does not establish (1) for general dense data.

## 3. Precisely what a fixed moment buys

If instead one only knows

\[
\sup_{n,t,\ell,a,i}
 \mathbb E[\mathbf1_{\mathcal G_n}|p_{n,a,i}^{(\ell)}(t)|^{2p}]
 \le C_p
\quad\text{for one fixed }p>1,
\]

the same proof gives merely
\(\mathbb E Z_n(M)^2\le C_p M^{-2p+2}\).
At \(M=A\sqrt{\log n}\) this is a power of \(\log n\), not \(n^{-1}\). The additional deterministic factor \(e^{KM}\) in (3) does not improve it. To derive a Gaussian tail through moments, estimates such as

\[
\bigl(\mathbb E[\mathbf1_{\mathcal G_n}|p_{n,a,i}^{(\ell)}(t)|^{2p}]\bigr)^{1/(2p)}
 \le C\sqrt p
\]

must hold with their constants controlled for moment orders of size \(\log n\), or for all orders as in (1). Population moments do not imply these finite-network estimates.

## 4. The width term remains logically separate

The population cutoff-removal result gives
\(\mathcal E_\mu(f_{\infty,M},f_\infty)\le C_\mu e^{-cM^2}\).
If (1) holds, the first and third terms in

\[
\mathcal E_\mu(f_n,f_\infty)
\le\mathcal E_\mu(f_n,f_{n,M})
 +\mathcal E_\mu(f_{n,M},f_{\infty,M})
 +\mathcal E_\mu(f_{\infty,M},f_\infty)
\tag{6}
\]

are therefore at most root width with \(M=A\sqrt{\log(e+n)}\), at fixed confidence on the fitting event. The second term still needs a theorem **at that growing cutoff**, including finite-width expectation bias.

Even if a valid second-term theorem had the form
\(C_\delta e^{KM}/\sqrt n\), substitution would give only
\(n^{-1/2}e^{KA\sqrt{\log(e+n)}}=n^{-1/2+o(1)}\).
That is conditional arithmetic, not an established dense rate in this study. A theorem for each fixed \(M\) is insufficient unless its constants and width threshold are controlled along \(M(n)\).

One possible way to avoid the growing constant is a telescoping estimate for successive cutoffs. For integer \(j\), put

\[
\Delta_{n,j}=f_{n,j+1}-f_{n,j},\qquad
\Delta_{\infty,j}=f_{\infty,j+1}-f_{\infty,j}.
\]

If the full, population-centered errors of these corrections obey
\(\|\Delta_{n,j}-\Delta_{\infty,j}\|_{L^2(\Pr;\mathcal E_\mu)}
\le a_j/\sqrt n\) with \(\sum_j a_j<\infty\), and the base cutoff has a root-width bound in the same norm, Minkowski and convergence of the cutoff limits give a strict root-width bound for the original model. This is an elementary sufficient criterion; no such dense correction estimate is asserted here. Bounds only on fluctuation around \(\mathbb E\Delta_{n,j}\) leave the population bias unresolved.

## Status

Sections 2 and 3 are complete mathematical implications. Section 4 separates the target from the proved cutoff-removal ingredients and records a possible further route. The general finite moment premise (1), and the full clipped dense width estimate, remain research obligations. These statements do not prove either a slower-than-root lower bound or the requested strict root-width theorem.
