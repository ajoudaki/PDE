# Scoped check: dense-pair benchmark and storage implication

Date: 2026-10-10.

Verdict: **PASS for the dense-pair estimate and the necessary literal-array storage deduction, conditional on the candidate's separately checked truncation-error lower bound (10).** No dimension, probability, parameterization, or fixed-label correction is needed for these parts.

Scientific input: the complete WORST_CASE_RESULT.md only. Required mathematical and canonical-notation instructions were reused. No other report or scientific artifact was read, no external source was retrieved, and no experiment or Git operation was performed. The candidate hash recorded during the check was SHA-256 98860493baf152fe08b063671532098dc7503fe0c5714d255ba1218ac0afc19f. The supervisor subsequently reported additions outside the dense section and confirmed that the dense section was unchanged. This is a narrow component verdict, not a full independent approval of all-order derivative and analytic-transfer arguments.

## Flow, Lipschitz constants, and absence of dimension factors

Use the candidate's variables \(f(v)=c^\top WBv\), with independent \(N(0,1/n)\) initial entries in \(B,W\) and \(c_0=0\). Set
\[
Q=\frac1m\sum_a v_av_a^\top,\quad
b=\frac1m\sum_a y_av_a,\quad
w=B^\top W^\top c,\quad e=b-Qw.
\]
Unit inputs and \(|y_a|\le1\) give \(\|Q\|_{\rm op},\|b\|_2\le1\). Direct differentiation of half-MSE gives exactly
\[
\dot B=W^\top ce^\top,\qquad
\dot W=c(Be)^\top,\qquad
\dot c=WBe.
\]
Thus candidate (21) has the correct signs, averaging, and metric. The original mobilities \(n,1,n\) become unit mobilities under \(W^{(1)}=\sqrt n B\), \(u=\sqrt n c\). This is the declared zero-readout feature-learning flow; no native Huang–Yau approximation theorem enters.

On the ball \(\max(\|B\|_{\rm op},\|W\|_{\rm op},\|c\|_2)\le5\), one has \(\|w\|_2\le125\), \(\|e\|_2\le126\), and each block velocity is bounded by \(3150\). The matrix velocities have this bound in Frobenius norm because they are rank one. Starting with the two matrix norms at most four and \(c_0=0\), a first-exit argument keeps the real flow in the ball up to \(T=1/32768\), since \(3150T<1\). Polynomial ODE continuation supplies existence on that interval.

For two states in this ball, put
\[
\Delta=\|B-\widehat B\|_F+\|W-\widehat W\|_F+\|c-\widehat c\|_2.
\]
Telescoping the three factors gives
\[
\|w-\widehat w\|_2\le25\Delta,\qquad
\|e-\widehat e\|_2\le25\Delta.
\]
For the first velocity block,
\[
\|\dot B-\dot{\widehat B}\|_F
\le630(\|W-\widehat W\|_F+\|c-\widehat c\|_2)+625\Delta
\le1255\Delta.
\]
The same computation holds for the other blocks: two direct-factor changes have coefficient \(5\cdot126=630\), while the residual change has coefficient \(25\cdot25=625\). Hence
\[
\Delta(t)\le e^{3765t}\Delta(0).
\]
Only \(B_0,W_0\) vary, so their sum-Frobenius distance is at most \(\sqrt2\) times Euclidean distance in their joint entry list. Every unit-query output is therefore Lipschitz on the good initial set with constant
\[
25\sqrt2\,e^{3765T}\le L_T=50e^{4000T}.
\]
No \(\sqrt n,\sqrt d,\sqrt m\) factor is missing. Also
\[
\|\dot w\|_2\le3\cdot25\cdot3150=236250<250000,
\]
so a dense-pair coefficient difference is \(500000\)-Lipschitz in time.

## Good-event probability and feature gap

For \(Z=\sum_{i=1}^nG_i^2\), exponential Markov with \(\mathbb Ee^{tZ}=(1-2t)^{-n/2}\) yields
\[
\mathbb P(Z\ge an)\le e^{-n(a-1-\log a)/2}\quad(a>1),
\]
and the same expression bounds the lower tail for \(0<a<1\).

For an \(n\times k\) Gaussian matrix \(A\) with entry variance \(1/n\), a \(1/4\)-net of the domain sphere has at most \(9^k\) points and gives \(\|A\|_{\rm op}\le(4/3)\max_{\rm net}\|Av\|_2\). Consequently, for \(k\le n\),
\[
\mathbb P(\|A\|_{\rm op}>4)
\le9^k e^{-n(8-\log9)/2}\le e^{-c_0n},
\qquad c_0=4-\tfrac32\log9>0.
\]
This applies to \(B_0,W_0\), since \(d=m+1\le n\).

For the fixed deterministic unit query \(v_*\), \(b_*=B_0v_*\) has independent \(N(0,1/n)\) coordinates. Conditional on \(b_*\), \(W_0b_*\) has independent \(N(0,\|b_*\|_2^2/n)\) coordinates. Requiring both squared-norm ratios to be at least \(3/4\) gives
\[
\|b_*\|_2^2\ge3/4,\qquad \|W_0b_*\|_2^2\ge9/16.
\]
These imply the two lower bounds \(1/2\) in (14), with failure \(Ce^{-cn}\). Intersection with the operator-norm events preserves that probability; independence among clauses is unnecessary.

The optional empirical feature-gap assertion also checks out. On a \(1/8\)-net, impose \(|v^\top(A^\top A-I)v|\le3/16\). The quadratic-form net bound has factor \(4/3\), giving \(\|A^\top A-I\|_{\rm op}\le1/4\), with failure \(Ce^{Cd-cn}\). Apply this first to \(B_0\) and then conditionally to \(W_0\) on the image of \(B_0\). Its restriction to an orthonormal basis of that independent \(d\)-dimensional subspace is again Gaussian with entry variance \(1/n\). The two lower isometries multiply to \(B_0^\top W_0^\top W_0B_0\succeq(9/16)I_d\); multiplying by the training input matrix and using its Gram gap \(1/2\) gives \(9/32\). Since \(d\le\sqrt n+1\), the failure is \(Ce^{-cn}\) uniformly for sufficiently large \(n\).

## Extension and concentration

Let \(G\) denote the common good set of initial entry lists. For fixed query and time, extend its scalar observable \(F\) by
\[
\overline F(x)=\inf_{z\in G}\{F(z)+L_T\|x-z\|_2\}.
\]
The Lipschitz inequality on \(G\) makes this finite, equal to \(F\) on \(G\), and globally \(L_T\)-Lipschitz. Convexity of \(G\) is not required.

The Gaussian concentration form used is: if \(X\) has independent \(N(0,1/n)\) entries and \(H\) is \(L\)-Lipschitz, then
\[
\mathbb P(|H(X)-\mathbb EH(X)|\ge s)
\le2e^{-ns^2/(2L^2)}.
\]
Its constant does not depend on ambient dimension. For example, the Gaussian entropy inequality \(\operatorname{Ent}(h)\le\frac12\mathbb E(\|\nabla h\|_2^2/h)\), applied to \(h=e^{\lambda H}\), yields \(\log\mathbb E e^{\lambda(H-\mathbb EH)}\le\lambda^2L^2/2\); scaling \(X=Z/\sqrt n\) and optimizing exponential Markov gives precisely this bound. The entropy inequality follows by integrating the Gaussian Ornstein–Uhlenbeck entropy derivative and using \(\nabla P_th=e^{-t}P_t\nabla h\) with weighted Cauchy–Schwarz. Smooth approximation gives the Lipschitz case.

Use the same extension for both dense copies. Their extension means are identical, so
\[
\mathbb P(|\overline F(X)-\overline F(X')|\ge2s)
\le4e^{-ns^2/(2L_T^2)}.
\]
This is unconditional Gaussian concentration, with good-event failure added separately. There is no invalid conditioning on \(G\).

## Time and sphere nets

A \(1/2\)-net of \(S^{d-1}\) has at most \(5^d\) points and, for every coefficient vector \(z\),
\[
\|z\|_2\le2\max_{v\ {\rm in\ net}}|z^\top v|.
\]
This applies because the identity-activation predictions remain linear in the input, although the parameter flow is nonlinear.

Take a grid containing both endpoints with \(N=\lceil nT\rceil+1\) points and mesh at most \(1/n\). At
\[
s=L_T\sqrt{\frac{2\log(4\cdot5^dN/\delta)}n},
\]
the union bound over all query/grid pairs has failure at most \(\delta\). The sphere estimate gives \(4s\) at grid times; time interpolation adds at most \(500000/n\). Thus
\[
D_n\le4s+500000/n
\]
with failure at most \(\delta+Ce^{-cn}\). The good-event failure is added once, not multiplied by net size, because it makes all extensions agree simultaneously with their physical observables.

For \(\delta=1/n\), \(d=m+1\), and \(N\le nT+2\), the logarithm is at most \(C(m+\log(en))\). The additive \(1/n\) term is absorbed into the square-root bound. This proves (11), uniformly for \(4\le m\le\sqrt n\). The sphere contributes the displayed \(m\) term; the time grid contributes only a logarithm.

## Storage consequence and its exact scope

Condition on candidate (10) holding simultaneously for all finite orders, as stated. Let \(r_n=n/(m+\log(en))\). Uniformly over \(m\le\sqrt n\), \(r_n\ge c\sqrt n\) for large \(n\). If \(q\le\log r_n/(4C_\eta)\), then \(j\le q+1\) gives
\[
E_n(q)\ge A_\eta e^{-C_\eta}r_n^{-1/4},
\qquad D_n\le Cr_n^{-1/2}.
\]
For each fixed comparison factor, success by any order in this range therefore has probability at most \(1/n+Ce^{-cn}\) for sufficiently large \(n\), uniformly in the sample range. No union over orders is needed. If \(D_n=0\), the positive lower bound already precludes success.

Any successful order must exceed that threshold. Under the stated literal-array count \(S_n(q)\ge m^{q-1}\), once \(\log r_n/(4C_\eta)\ge2\),
\[
\log S_n(q)\ge\frac1{8C_\eta}\log m\log r_n.
\]
This proves the necessary form (1); it does not separately prove that some order succeeds. For fixed \(0<a\le1/2\) and \(m=4\lfloor n^a/4\rfloor\),
\[
\log m=a\log n+o(1),\qquad
\log r_n=(1-a)\log n+o(1),
\]
which gives \(\exp(c_{\eta,a}(\log n)^2)\). Fixed sample count yields only a polynomial lower bound, and neither regime proves \(\exp(cn)\).

The following qualifications are necessary and are already present substantially in the candidate:

- Fixed \(\eta>0\) matters. If \(\eta\) shrinks with sample count, both \(C_\eta\) and the prefactor \(A_\eta e^{-C_\eta}\) change; the fixed-label onset is not uniform in that limit. This check supplies no superpolynomial result under \(Y=O(1/m)\).
- The sphere discrepancy is at least the dense discrepancy at the passive query, so exceeding it is a stronger failure claim. The sphere proof uses input linearity.
- The array count is a representation-specific charge, not a lower bound on arbitrary structured or compressed encodings.
- Source input-norm admission applies to the normalized \(v_a\). The physical \(x_a=\sqrt d\,v_a\) have norm \(\sqrt d\); this normalization distinction should remain explicit when comparing with the native paper.

No correction to the checked dense section or its conditional storage deduction is required. The source-derivative lower and analytic transfer establishing (10) remain outside this component verdict.
