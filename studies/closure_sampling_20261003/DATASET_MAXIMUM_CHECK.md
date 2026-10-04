# Coordinator reconstruction of the sample-maximum refinement

2026-10-04. Bounded continuation of the dataset-constant audit. This is
an internal mathematical check, not a promotion review. Scientific inputs
are the complete current DATASET_SOURCE_CONSTANTS.md and
DATASET_DEPENDENCE.md, their previously read and unchanged named proof
inputs, and the real fitting certificate. No experiment or external
scientific retrieval was used.

The question is whether the additional factor $m^{-1/2}$ in the
sufficient label condition $Y\le c\lambda/\sqrt m$ is sharp.
Here $Y$ is label RMS, and
$\lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}$ is the normalized
initial feature-Gram gap. It is not sharp even within the current proof.

## Elementary maximum estimate

The source audit gives, conditionally on a cavity, a family of nonnegative
normalized Gaussian suprema $Z_a$, one for each sample. Their conditional
tails obey

\[
 \mathbb P(Z_a>A+t\mid\mathcal F)\le D e^{-b t^2},
 \qquad t\ge0,
\]

with structural $A,b>0$ and $D\ge1$. The conditioning sigma algebra
$\mathcal F$ contains the retained initialization, not the omitted
Gaussian root. No independence between the different samples is assumed.
The small complex correction has the same type of tail for sufficiently
large width, so constants can include it. The source's fixed-width
threshold is allowed to depend on the fixed sample count.

Set $u_m=\sqrt{b^{-1}\log(Dm)}$ and $Z=\max_{a\le m}Z_a$.
A union bound yields

\[
 \mathbb P(Z>A+u_m+t\mid\mathcal F)
 \le mD e^{-b(u_m+t)^2}\le e^{-b t^2}.
\]

For any fixed $\eta>0$, use
$W=(Z-A-u_m)_+\ge0$ and the tail-integral identity

\[
 \mathbb E e^{\eta W}
 =1+\eta\int_0^\infty e^{\eta t}\mathbb P(W>t)\,dt.
\]

It follows that

\[
 \mathbb E[e^{\eta Z}\mid\mathcal F]
 \le e^{\eta(A+u_m)}
       \left[1+\eta\int_0^\infty e^{\eta t-bt^2}\,dt\right]
 \le C_\eta\exp\{C_\eta\sqrt{\log(em)}\}.
 \tag{1}
\]

The integral is finite by completing the square. Thus the previous bound
of order $m$, obtained by summing $m$ exponential moments, is unnecessary.

The coordinator separately obtained (1) from the per-sample moment bound
$\mathbb E[e^{pZ_a}\mid\mathcal F]\le C\exp(Cp+Cp^2)$.
For $p\ge\eta$, the concavity of the power $\eta/p$ gives

\[
 \mathbb E e^{\eta Z}
 \le\left(\sum_a\mathbb E e^{pZ_a}\right)^{\eta/p}
 \le\exp\left\{\frac\eta p[\log(Cm)+Cp+Cp^2]\right\}.
\]

Choosing $p=\max\{\eta,\sqrt{\log(Cm)}\}$ recovers (1).
This is a second check of the elementary maximum estimate. The union-tail
proof makes the absence of a sample-independence assumption explicit.

## Substitution into the already established proof

The source audit's complete requirements after its real-energy refinement
are

\[
 Y\le c\lambda,\qquad S=C_0Y/\lambda\le c,\qquad
 S^2B\le c,\qquad S^2\log(e+B)\le c,
\]

where the carrier budget $B$ must exceed a structural multiple of the
conditional exponential moment at a fixed exponent $\eta_0$. The
exponent $\eta_0$ is not changed in this refinement. By (1), choose

\[
 B=C_B\exp\{C_B\sqrt{\log(em)}\}.
\]

The choice

\[
                 Y\le c\lambda
                       \exp\{-C\sqrt{\log(em)}\}
 \tag{2}
\]

with structural constants chosen in the indicated order implies all four
requirements. Indeed it gives $S\le cB^{-1/2}$ after adjusting the
constants, and $\log(e+B)\le C B$ for $B\ge1$. The real energy
condition follows since the exponential factor is at most one.

The source audit checks that no other non-real source step requires
$S^2\le c\lambda$, and that all budget dependence is controlled
by these requirements or by the sufficiently-large-width threshold.
Consequently the new budget changes the allowed label range without
changing the structural source-radius, source-magnitude, state-count or
same-time comparison calculations. For each fixed dataset, labels and
confidence, at all sufficiently large widths, the conclusion remains

\[
 \sup_{t\in[0,\infty],\ x\in\sqrt dS^{d-1}}
 |f_C(t,x)-f_n(t,x)|
 \le C e^{CY/\lambda^2}/\sqrt n,
\]

with total retained coordinates at most

\[
 C(1+m)^4\lambda^{-4}\log^{4[d(L+5)+1]}(en)+Cm(d+1).
\]

The amplification restriction
$\log(en)\ge C(1+Y^4/\lambda^6)$ and the other unquantified
fixed-dataset width thresholds remain. The exact-real setup contract,
analytic activations, initialized gap, autonomy, all-time norm and
endpoint qualification are unchanged. This is a refinement of an
internally checked research theorem, not a new established-book claim.

Since $\exp[-C\sqrt{\log(em)}]$ decays more slowly than every fixed
power $m^{-\alpha}$, (2) removes the additional polynomial loss in
sample count. Neither the new subpolynomial factor nor the dependence
on $\lambda$ is proved necessary. No matching lower bound, label-
direction-optimal theorem, or result for jointly growing $m$ and $n$
is asserted. In particular the normalization $Q^{(L)}/m$ gives the
correct worst-direction decay rate for mean loss, but does not establish
that label magnitudes intrinsically need the same inverse-sample scaling.

The coordinator's moment/Jensen calculation preceded the agent's returned
union-tail derivation. The two derivations agree. The subsequent source-
interface check is collaborative; it is not an independent promotion
review.

**Completed source check:** the full DATASET_MAXIMUM_REFINEMENT.md was
then read at SHA-256
`7bd09a922c5dcaaee1f4dd6ab5af8ce9c8a4991b2d04a1f01017a8d06cde529a`.
The conditional tail argument, fixed-exponent budget substitution,
remaining source requirements, comparison exponent, state count and
width-threshold qualifications agree with this reconstruction. The
larger label class retains the general error constant
$C\exp(CY/\lambda^2)$; the old label-specialized bound
$C\exp(C/(\lambda\sqrt m))$ is not extended to it. Verdict:
**PASS as a refinement of the named internally checked source theorem**.
