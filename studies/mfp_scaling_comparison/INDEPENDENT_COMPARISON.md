# Independent comparison: nested (1/n) connector versus the original MFP connector

## Verdict

The displayed learning-rate ratio is the original two-hidden-layer muP
mobility written in effective coordinates.  The positive finite-type theorem
does **not**, however, concern the original initialization.  It replaces the
centered-iid (1/\sqrt n) connector by a coherent neuron-embedded (1/n)
kernel.  That changes a central-limit field into a law-of-large-numbers field
and removes the Gaussian extreme-coordinate mechanism behind the quadratic
initial layer.

Consequently the construction is a valid continuous mean-field model of a
different initialization class.  It is not an \(\eta(n)\) cure for the
original iid-Gaussian MFP model.

## 1. Exact coordinate comparison

Ignore the harmless activation-normalization constants.  The original MFP
network is

\[
 z_j={1\over\sqrt n}\sum_i \widetilde W_{ji}u_i^2,
 \qquad
 f_n={1\over n}\sum_j \widetilde c_j z_j^2,
 \]

where \(u_i,\widetilde W_{ji},\widetilde c_j\) are iid standard Gaussians and
every raw block has mobility \(nh\).  Set

\[
 a_i=u_i,\qquad b_{ji}={\widetilde W_{ji}\over\sqrt n},
 \qquad c_j={\widetilde c_j\over n}.
\]

Then

\[
 f_n=\sum_jc_j\Big(\sum_i b_{ji}a_i^2\Big)^2,
 \]

and the induced mobilities in \((a,b,c)\) coordinates are exactly

\[
 \eta_a=nh,qquad \eta_b=h,qquad \eta_c={h\over n}.
\]

Indeed, if \(b=\widetilde W/\sqrt n\), then
\(\nabla_{\widetilde W}L=n^{-1/2}\nabla_bL\), so
\(\Delta b=n^{-1/2}(-nh\nabla_{\widetilde W}L)=-h\nabla_bL\).
Likewise, \(c=\widetilde c/n\) gives
\(\Delta c=-h\nabla_cL/n\).

Thus the proposed learning-rate powers are not a new joint scaling.  The
initialization is what differs:

\[
\begin{array}{c|c|c}
 &\operatorname{Var}(b_{ji})&\text{forward field}\\ \hline
\text{original iid MFP}&\Theta(n^{-1})
 &n^{-1/2}\sum_i\widetilde W_{ji}a_i^2\\
\text{nested kernel}&\Theta(n^{-2})
 &n^{-1}\sum_iW_0(\beta_j,\alpha_i)A_0(\alpha_i)^2.
\end{array}
\]

The first is a conditional Gaussian/CLT field.  The second is a coherent
LLN integral.

## 2. Why the same variance with iid centering is degenerate

Suppose instead that the \(b_{ji}\) are independent, centered, independent
of \(a_i\), and \(\operatorname{Var}(b_{ji})=\sigma_b^2/n^2\).  Conditional
on \(a\),

\[
 \mathbb E[z_j^2\mid a]
 ={\sigma_b^2\over n^2}\sum_i a_i^4.
\]

If \(n^{-1}\sum_i a_i^4=O_{\mathbb P}(1)\), then
\(z_j\to0\) in probability and in \(L^2\).  Hence the proposed
\(n^{-2}\) variance is nondegenerate only because
\(W_0(\beta,\alpha)\) is coherently correlated with the source type
\(A_0(\alpha)\).

For independent centered connector entries, the balanced choice is instead

\[
 \operatorname{Var}(b_{ji})=\Theta(n^{-1}),
 \qquad \operatorname{Var}(c_j)=\Theta(n^{-2}),
\]

which is precisely the original MFP initialization in effective
coordinates.

## 3. Audit of the finite-type nested theorem

Let \(b=W/n\), \(c=C/n\), and use the full square loss
\(L=(F-1)^2\).  With

\[
 Z_j={1\over n}\sum_iW_{ji}A_i^2,\qquad
 R_i={1\over n}\sum_jC_jZ_jW_{ji},qquad r=F-1,
\]

the proposed raw mobilities give exactly

\[
\begin{aligned}
 A_i^+&=A_i-8hrA_iR_i,\\
 W_{ji}^+&=W_{ji}-4hrC_jZ_jA_i^2,\\
 C_j^+&=C_j-2hrZ_j^2.
\end{aligned}
\]

These are explicit Euler steps of the displayed continuum vector field.
For finitely many types having positive masses, the empirical dynamics
reduces exactly to a fixed-dimensional Euler system with empirical type
frequencies.  On every compact interval, local Lipschitzness and discrete
Gronwall yield

\[
 \sup_{kh_n\le T}\|\theta_{n,k}-\theta(kh_n)\|
 \le C_T(h_n+n^{-1})
\]

when the type-frequency error is \(O(n^{-1})\).

The global-existence calculation is also valid.  With

\[
 N_A=\int A^2,\qquad N_W=\iint W^2,
 \qquad N_C=\int C^2,
\]

one has

\[
 \dot N_A=-16rF,qquad \dot N_W=-8rF,
 \qquad \dot N_C=-4rF.
\]

Loss dissipation bounds \(r\), hence \(F=1+r\), on every time interval;
the norm derivatives are therefore bounded.  In finite dimension this
precludes finite-time escape.

Only \(h_n\to0\) is required for this Euler limit.  The stronger condition
\(nh_n\to0\) is harmless but unnecessary; it merely forces the raw number
\(\eta_{a,n}=nh_n\) itself to vanish even though the actual normalized
increment is already \(O(h_n)\).

The finite-type proof does not by itself establish the same quantitative
theorem for arbitrary measurable latent profiles.  That extension requires
separate quadrature/empirical-process and stability estimates.

## 4. Audit of the centered witness

The witness is arithmetically correct.  Put

\[
 d(x)=x^2-{5\over2},\quad k={32\over729},\quad
 W_0(v;s,x)=v d(x),\quad C_0(v)=k(v^2-5/2).
\]

For uniform \(x\in\{1,2\}\) and
\(v\in\{-2,-1,1,2\}\),

\[
 Z_0(v)=v\,\mathbb E[d(x)x^2]={9\over4}v,
\]

and

\[
 F_0=k{81\over16}\,
 \mathbb E[v^2(v^2-5/2)]={1\over2}.
\]

Moreover \(R_0(s,x)=(2/9)d(x)\), giving

\[
 \dot A_0={8\over9}A_0d(x),
 \qquad
 \dot Z_0(v)=10v+{136\over81}v(v^2-5/2).
\]

The stated variances follow as well.

But “centered” here means only zero one-coordinate marginals.  The connector
is the rank-one matrix

\[
 W_{ji}=v_jd(x_i),
\]

\(W_{ji}\) is coupled to \(A_i^2=x_i^2\), and \(C_j\) is coupled to the
same row type \(v_j\).  Those dependencies are exactly what make both
\(Z_0\) and \(F_0=1/2\) nonzero.  The witness is neither iid nor Gaussian,
and it does not match the original initialized trace \(F_0\to0\).

## 5. Consequence for the quadratic initial-layer theorem

The nested finite-type construction avoids the old no-go, but by changing
the model.  Bounded coherent types yield a fixed-dimensional, locally
Lipschitz ODE.  The original quadratic model has unbounded iid Gaussian
CLT sources and develops a fixed output change on a time
\(O((\log n)^{-1/2})\).

Therefore:

1. the positive nested theorem does not contradict the quadratic
   initial-layer theorem;
2. choosing, for example, \(h_n=n^{-3}\) proves convergence for the
   finite-type nested model, not for the original iid model;
3. for the original iid model, fixed-step OMFP identification exists, but
   compact-time width-first mesh removal fails, and every diagonal proved
   consistent with the finite-width ODE inherits its initial layer;
4. arbitrary deliberately under-resolved diagonals for the full original
   network remain unclassified.

## 6. Honest statement for centered iid weights

An autonomous equation based only on the one-edge empirical law cannot
close the centered-iid model.  To see the information loss, let
\(s_i=a_i^2\) and, for one iid row \(W\), define

\[
 W'=W-{W\cdot s\over\|s\|^2}s.
\]

Then

\[
 {1\over n}\|W'-W\|^2
 ={(W\cdot s)^2\over n\|s\|^2}=O_{\mathbb P}(n^{-1}),
\]

so the entrywise empirical laws of \(W\) and \(W'\) have the same weak
limit, while

\[
 {1\over\sqrt n}W'\cdot s=0,
 \qquad {1\over\sqrt n}W\cdot s
 \Rightarrow N(0,\mathbb E a^4).
\]

Thus one must retain row/column Gaussian fields, source overlaps, and reused
response information, as OMFP does.  This observation rules out only a
scalar/one-edge empirical-law closure; it does not rule out enriched
operator-valued or dynamic-cavity descriptions.

For the original quadratic iid model, however, such an enriched description
cannot produce a classical continuous trajectory from the initialized trace
on the standard clock: the proved initial layer already forbids that for the
width-first limit and for every ODE-consistent diagonal currently covered.
Post-layer generalized dynamics and all under-resolved diagonals remain
open.
