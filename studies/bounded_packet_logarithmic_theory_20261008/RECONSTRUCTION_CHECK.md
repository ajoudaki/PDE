# Internal mathematical reconstruction of the bounded-packet obstruction

**Mathematical verdict: PASS for the stated exact-real Gaussian model and deterministic packet widths.** I find no mathematical gap in the standalone implication (3), its specialization using the supplied dense upper theorem, or the necessary retained-weight exponent. This is an internal check, not promotion.

**Process qualification: this was not a strictly isolated review.** Source-read windows spilled beyond the assigned definitions and setting, including empirical-result sentences in the paper. The additional material was not used in the argument below. The scope exposure is recorded precisely at the end; this report must not count as a fully isolated review.

The candidate checked is RESULT.md, SHA256
17a1dabd526de6fa81aad30c5804208eb9171d9b95b6f2fb20373210c81b8226.
The proof reconstruction below distinguishes its new conclusion from the
one imported benchmark theorem.

## Checked statement and admissible example

Let the source and ordinary dense-reference width be \(n\to\infty\). Let
\(q=q(n)\ge2\) be a deterministic integer sequence and let
\(\varepsilon_n>0\) be deterministic. For the fixed problem constructed
below, the independently reconstructed statement is
\[
q/n\longrightarrow0,\qquad q\varepsilon_n\longrightarrow0
\quad\Longrightarrow\quad
\Pr\{\|f_{\rm packet}-f_n\|_*\le\varepsilon_n\}\longrightarrow0.
\]
Here the norm takes the supremum over physical time and all unit normalized
inputs; missing required fitted limits count as infinite discrepancy.
Only finite-time values are used, so endpoint convergence is unnecessary
for this lower bound.

Take two hidden layers, \(m=d=2\), normalized training inputs
\(v_1=e_1,v_2=e_2\), activation \(\tanh\), and labels
\(y=(\sqrt2Y,0)\). Define
\[
\alpha=\mathbb E\tanh^2G,\qquad
\gamma=\mathbb E\tanh^2(\sqrt\alpha G),\qquad G\sim N(0,1).
\]
Both numbers lie strictly between zero and one. At each layer the two
Gaussian coordinates are independent; oddness makes the off-diagonal
feature moments zero. The population covariance recursion is therefore
\(I_2,\alpha I_2,\gamma I_2\). The unweighted gap is exactly \(\gamma>0\),
the label RMS is \(Y\), and the original inputs \(x_a=\sqrt2v_a\) span
\(\mathbb R^2\). In particular \(m/\gamma\ge1\).

For \(|\operatorname{Im}z|\le1/2\),
\[
|\cosh z|^2\ge\cos^2(1/2),\qquad
|\tanh z|^2
=\frac{\sinh^2(\operatorname{Re}z)+
       \sin^2(\operatorname{Im}z)}
      {\sinh^2(\operatorname{Re}z)+
       \cos^2(\operatorname{Im}z)}
\le1.
\]
The nearest poles are outside this strip. Hence
\(|\tanh'|<2\) and \(|\tanh''|<4\) there, also on the smaller strip used
in the appendix's envelope. Taking its strip parameter \(a=1/2\) gives
\(\beta=32\). Any one fixed choice
\[
0<Y\le(\gamma/2)32^{-60}
\]
satisfies the supplied sufficient label allowance. No width-dependent
label scaling is used.

## Initializer, Cholesky orientation, and slope fluctuation

At width \(p\), the state is
\(W^{(1)}\in\mathbb R^{p\times2}\),
\(W^{(2)}\in\mathbb R^{p\times p}\), and
\(w\in\mathbb R^p\), with
\[
h^{(1)}(v)=\tanh(W^{(1)}v),\quad
h^{(2)}(v)=\tanh(W^{(2)}h^{(1)}(v)),\quad
f(v)=w^\top h^{(2)}(v)/p.
\]
The code state order is first weights, readout, hidden matrix. Its
gradient-flow formulas agree with this network, mean-square loss, and
mobilities \((p,1,p)\). The retained weight count at \(p=q\) is
\(2q+q+q^2=q^2+3q\).

Write \(H\in\mathbb R^{q\times2}\) for the initialized packet first
features. Its entries are independent \(\tanh N(0,1)\). The source first
features give
\[
K=H_{\rm source}^\top H_{\rm source}/n,\qquad RR^\top=K,
\]
where \(R\) is the lower Cholesky factor. The packet initializer uses
\[
Z=\sqrt q\,UR^\top,\qquad
W^{(2)}(0)=G_q+(Z-G_qH)H^\dagger,
\quad
H^\dagger=(H^\top H)^{-1}H^\top.
\]
Here \(G_q\) has independent \(N(0,1/q)\) entries and \(U\) is the
sign-corrected Gaussian QR basis with two columns. These Gaussian blocks
have the independence specified in the candidate's ideal Gaussian model.

This is the code's triangular solve: if \(H=BT\) is its thin QR
factorization, then \(H^\dagger=T^{-1}B^\top\), and the right solve
produces \((Z-G_qH)T^{-1}\). The feature entries have continuous densities,
so the determinant of the first two rows is nonzero almost surely.
Thus \(H\) and \(H_{\rm source}\) have rank two for \(q,n\ge2\), and the
inverses and Cholesky factor exist almost surely in exact arithmetic.

The QR basis is invariant in law under left orthogonal transformations:
the input Gaussian matrix is invariant and positive-diagonal QR is
equivariant. Its first column is directly a normalized standard Gaussian
vector. Crucially, the first column of the upper matrix \(R^\top\) is
\((\sqrt{K_{11}},0)^\top\). Therefore
\[
W^{(2)}(0)H=Z,\qquad Z^\top Z/q=K,\qquad
Z_{\cdot1}=\sqrt{qK_{11}}\,u,
\]
where \(u\) is uniform on the sphere in \(\mathbb R^q\).
No independence of the rows of \(Z\) is asserted or needed.

Since \(w(0)=0\), both hidden-layer velocities vanish at zero.
The readout velocity is
\(\dot w(0)=(2/m)\sum_a y_a h_a^{(2)}(0)\), so
\[
\dot f(0,v_1)=\sqrt2Y\,\frac1p
                 \sum_i h_i^{(2)}(0,v_1)^2.
\]
Consequently the packet average in this identity has the exact law
\[
A_{q,n}=\frac1q\sum_i
\tanh^2\left(\sqrt{qK_{11}}\,u_i\right).
\]
The source radius obeys
\(K_{11}-\alpha=O_{\mathbb P}(n^{-1/2})\), by the variance bound for
an average of bounded independent variables.

For completeness, put \(u_i=X_i/\sqrt{\sum_jX_j^2}\), with independent
standard normal \(X_i\), and set
\[
s_q=q^{-1}\sum_iX_i^2,\quad
g(x)=\tanh^2(\sqrt\alpha x),\quad
\kappa=\tfrac12\mathbb E[Gg'(G)]>0.
\]
The expectation defining \(\kappa\) is strictly positive because its
integrand is positive away from zero. If \(f_0(z)=\tanh^2z\) and
\(F(s,x)=f_0(\sqrt{\alpha/s}\,x)\), direct differentiation gives
\[
F_s=-\frac{zf_0'(z)}{2s},\qquad
F_{ss}=\frac{3zf_0'(z)+z^2f_0''(z)}{4s^2},
\quad z=\sqrt{\alpha/s}\,x.
\]
The expressions \(zf_0'(z)\) and \(z^2f_0''(z)\) are bounded on the
real line. Thus the second derivative is uniformly bounded for
\(s\in[1/2,3/2]\). Since \(\operatorname{Var}(s_q)=2/q\), Taylor's
remainder averaged over \(i\) is \(O_{\mathbb P}(q^{-1})\).
The empirical first-derivative coefficient converges in probability
to \(-\kappa\), as it is an average of bounded independent variables.
It follows with all errors controlled that
\[
\sqrt q\left[
q^{-1}\sum_i g(X_i/\sqrt{s_q})-\gamma\right]
=q^{-1/2}\sum_i
\{g(X_i)-\gamma-\kappa(X_i^2-1)\}+o_{\mathbb P}(1).
\]

The summands are independent, identically distributed, centered, and
have finite variance. That variance is strictly positive:
zero variance would give
\(g(x)-\gamma=\kappa(x^2-1)\) almost everywhere under a Gaussian density.
Continuity and positive Gaussian density on every interval would extend
the identity to every real \(x\), contradicting boundedness of \(g\)
and \(\kappa>0\). Denote the variance by \(\sigma^2>0\).
The scalar central limit theorem for centered iid finite-variance
variables therefore gives the limit \(N(0,\sigma^2)\) for the last
display. Adding errors tending to zero in probability preserves that
limit.

Replacing \(\alpha\) by the source radius is harmless at the required
scale. For \(k\ge\alpha/2\),
\[
\left|\frac{\partial}{\partial k}
 f_0(\sqrt{qk}\,u_i)\right|
=\frac{|zf_0'(z)|}{2k}\le C_\alpha.
\]
The source radius lies in this range with probability tending to one.
The replacement error is therefore \(O_{\mathbb P}(n^{-1/2})\),
uniformly in \(q\), and its product with \(\sqrt q\) vanishes if
\(q/n\to0\).

For the ordinary target network, condition on its first features.
The second preactivations at \(v_1\) are independent
\(N(0,K'_{11})\), with
\(K'_{11}-\alpha=O_{\mathbb P}(n^{-1/2})\).
The conditional variance of their averaged squared activations is
at most \(1/(4n)\). The same radius-derivative bound controls the
conditional mean. Its average is therefore
\(\gamma+O_{\mathbb P}(n^{-1/2})\).
We obtain, whenever \(q\to\infty\) and \(q/n\to0\),
\[
\sqrt q\,[\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)]
\ \Longrightarrow\ N(0,2Y^2\sigma^2).
\]
The target contribution vanishes in probability at this scale. Even a
coupling cannot cancel the packet fluctuation while preserving that
ordinary target marginal.

## Full gradient flow and its uniform remainder

Let \(r_a=f(v_a)-y_a\) and
\(D_a^{(\ell)}=\operatorname{diag}(1-(h_a^{(\ell)})^2)\).
The exact equations are
\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(2)},\\
\dot W^{(2)}&=-\frac2{pm}\sum_a
 r_a D_a^{(2)}w\,h_a^{(1)\top},\\
\dot W^{(1)}&=-\frac2m\sum_a
 r_a D_a^{(1)}W^{(2)\top}D_a^{(2)}w\,v_a^\top.
\end{aligned}
\]
Their mobility factors yield exactly
\[
\dot{\mathcal L}
=-\|\dot W^{(1)}\|_F^2/p-\|\dot W^{(2)}\|_F^2
 -\|\dot w\|_2^2/p\le0.
\]
Since \(\mathcal L(0)=Y^2\), Cauchy--Schwarz gives
\(m^{-1}\sum_a|r_a|\le Y\).
Using \(\|D_a^{(\ell)}\|_{\rm op}\le1\),
\(\|h_a^{(\ell)}\|_2\le\sqrt p\), and \(\|v_a\|_2=1\), if
\(\|W^{(2)}(0)\|_{\rm op}\le M\) then
\[
\frac{\|w(t)\|_2}{\sqrt p}\le2Yt,\quad
\|W^{(2)}(t)-W^{(2)}(0)\|_F\le2Y^2t^2,\quad
\frac{\|\dot W^{(1)}(t)\|_F}{\sqrt p}
\le4Y^2t(M+2Y^2t^2).
\]
For each fixed finite width these bounds keep all parameters bounded
on every finite time interval. The vector field is smooth and therefore
locally Lipschitz. Local uniqueness and the continuation criterion for a
finite-dimensional locally Lipschitz ODE imply global existence at finite
times: a finite maximal time would require escape from every compact
subset of parameter space, which these bounds exclude.

For \(0\le t\le1\), set \(S=1+(M+2Y^2)^2\).
At any \(\|v\|_2\le1\), the two terms in the derivative of the second
preactivation have normalized norms at most \(4Y^2t\) and
\(4Y^2t(M+2Y^2)^2\). Thus
\[
\|\dot h^{(2)}(t,v)\|_2/\sqrt p\le4Y^2St,\quad
\|h^{(2)}(t,v)-h^{(2)}(0,v)\|_2/\sqrt p\le2Y^2St^2.
\]
Also \(|f(t,v_a)|\le2Yt\). Subtracting \(\dot w(0)\) from
the readout equation and using \(m^{-1}\sum_a|y_a|\le Y\) gives
\[
\|w(t)-t\dot w(0)\|_2/\sqrt p
\le2Yt^2+\tfrac43Y^3St^3.
\]
Expand the prediction using this readout remainder and the last-feature
increment. The latter term has bound
\(t(2Y)(2Y^2St^2)\). The result is exactly
\[
|f(t,v)-t\dot f(0,v)|
\le2Yt^2+\tfrac{16}{3}Y^3St^3.
\]
In particular this controls the actual feature-learning flow; it does
not require bounds on individual backward coordinates or a frozen kernel.

The initial operator norm is tight uniformly in the widths. Indeed,
with \(P=HH^\dagger\), the two summands of
\(W^{(2)}(0)=G_q(I-P)+ZH^\dagger\) act on orthogonal subspaces, so
\[
W^{(2)}(0)W^{(2)}(0)^\top
=G_q(I-P)G_q^\top+Z(H^\top H)^{-1}Z^\top
\]
and
\[
\|W^{(2)}(0)\|_{\rm op}^2
\le\|G_q\|_{\rm op}^2+
\frac{\|K\|_{\rm op}}{\lambda_{\min}(H^\top H/q)}.
\]
Here \(\|K\|_{\rm op}\le\operatorname{tr}K\le2\).
Entrywise variance bounds give
\(H^\top H/q\to\alpha I_2\) in probability. In this fixed matrix
dimension, its operator-norm error tends to zero, and the smallest
eigenvalue is consequently at least \(\alpha/2\) with probability
tending to one.

A \(1/4\)-net of the sphere in \(\mathbb R^p\) has at most \(9^p\)
points by the disjoint-ball volume argument. Approximating the left and
right unit vectors separately bounds \(\|G_p\|_{\rm op}\) by twice the
largest net pairing. Each pairing has variance \(1/p\), so Gaussian
tails and a union bound give
\[
\Pr(\|G_p\|_{\rm op}>8)
\le2\exp[-p(8-2\log9)].
\]
The exponent is negative with magnitude tending to infinity.
Thus \(M=\sqrt{64+4/\alpha}\) works with probability tending to one
when both widths diverge. For each fixed \(q\), the denominator above
is positive almost surely and its distribution does not depend on \(n\);
the source numerator remains bounded by two. These fixed-\(q\)
operator norms are tight. Combining finitely many small widths with
the large-width bound proves uniform tightness along arbitrary sequences.
The coefficient in the Taylor remainder is therefore bounded in
probability in every case used below.

## Shrinking tolerances, bounded widths, and weight exponent

First let \(q\to\infty\). Since \(q\varepsilon_n\to0\),
\(t_n=\sqrt{\varepsilon_n}\to0\), and eventually \(t_n\le1\).
Apply the preceding estimate to both flows:
\[
\frac{\sqrt q}{t_n}
[f_{\rm packet}(t_n,v_1)-f_n(t_n,v_1)]
=\sqrt q[\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)]
 +O_{\mathbb P}(\sqrt q\,t_n).
\]
The last term tends to zero because
\(\sqrt q\,t_n=\sqrt{q\varepsilon_n}\to0\).
The left side thus converges to the nondegenerate Gaussian already
identified. Success of the full contract would force its absolute
value to be at most \(\sqrt{q\varepsilon_n}\to0\).
For any fixed \(a>0\), the limiting probability of this shrinking
interval is at most the Gaussian probability of the closed interval
\([-a,a]\), by convergence in distribution. Sending \(a\downarrow0\)
gives zero. This justifies the varying-tolerance step without assuming
a density bound uniform in \(n\).

The alternative witness \(t_n=1/q\) also checks:
multiplying the Taylor remainder by \(q^{3/2}\) gives
\(O_{\mathbb P}(q^{-1/2})\), hence the same Gaussian limit for
\(q^{3/2}[f_{\rm packet}(1/q,v_1)-f_n(1/q,v_1)]\).
It is sufficient for polylogarithmic widths, though the
tolerance-dependent witness gives the stronger stated exponent.

For a fixed \(q\ge2\), it remains to prove that the limiting initial
slope difference has no atom at zero. In fact the packet average with
source radius \(\alpha\) has no atoms anywhere. Put
\[
h(s)=\tanh^2(\sqrt{q\alpha s}),\qquad s\ge0.
\]
For \(s>0\), writing \(z=\sqrt{q\alpha s}\),
\[
h'(s)=q\alpha\,(\tanh z/z)\operatorname{sech}^2z.
\]
Both positive factors decrease strictly with \(z>0\).
For the first factor this follows from
\(\tanh z-z\operatorname{sech}^2z>0\): that expression vanishes at
zero and has derivative
\(2z\operatorname{sech}^2z\tanh z>0\).
The derivative extends to zero, so \(h\) is strictly concave.

Condition on the radius of \((X_1,X_2)\) and on \(X_3,\ldots,X_q\).
The angle \(\theta\) remains uniform; the first two squared normalized
coordinates are \(s\cos^2\theta,s\sin^2\theta\) for some fixed
\(s\in(0,1]\). Their contribution is
\(h(s\cos^2\theta)+h(s\sin^2\theta)\).
The function \(u\mapsto h(su)+h(s(1-u))\) is strictly increasing on
\([0,1/2]\) and strictly decreasing on \([1/2,1]\), because \(h'\)
decreases strictly. Any level therefore has at most two values of
\(u\), and finitely many angles. Uniform angle gives conditional
probability zero for each level, proving nonatomicity after averaging.
The argument includes \(q=2\), when \(s=1\).

The radius replacement tends to zero in probability even for fixed
\(q\), and the target average tends to \(\gamma\). Thus the initial
slope difference converges to a nonatomic law. Dividing the prediction
difference at \(t_n=\sqrt{\varepsilon_n}\) by \(t_n\) leaves this same
limit, since its remainder is \(O_{\mathbb P}(t_n)\).
Success would bound the absolute value by \(\sqrt{\varepsilon_n}\).
The same closed-interval argument gives success probability tending
to zero.

An arbitrary integer sequence \(q(n)\ge2\) has, along every
subsequence, a further subsequence on which \(q\) is constant or tends
to infinity. If success probabilities failed to tend to zero, a
subsequence bounded below by a positive number would contradict one
of the two cases above. This proves the standalone statement for
all deterministic width sequences in its scope.

For the benchmark specialization, the only imported research theorem is
the right-hand bound in paper/results.tex, equation
eq:dense-variability:
\[
b_n\le
CY(m/\gamma)^5\sqrt{d/n}\log(en)e^{\sqrt{\log(en)}}
=n^{-1/2+o(1)}
\]
at this fixed admissible problem and fixed confidence. A positive
deterministic upper envelope for \(3b_n\) can be used as
\(\varepsilon_n\), so neither positivity of \(b_n\) nor the dense lower
theorem is needed.

If \(q^2+3q=O(n^{1-\eta})\), with \(0<\eta<1\), then
\(q=O(n^{(1-\eta)/2})\), so \(q/n\to0\) and
\(q\varepsilon_n\le n^{-\eta/2+o(1)}\to0\).
This proves failure with success probability tending to zero; every
polylogarithmic stored-weight bound is included. Finally, if a fixed
deterministic choice of widths achieved the required success
probability at every sufficiently large \(n\), an infinite subsequence
with \(q^2+3q\le n^{1-\eta}\) would contradict this result.
Hence its retained-weight count must eventually exceed \(n^{1-\eta}\)
for every fixed \(\eta>0\); values \(\eta\ge1\) are already covered
by the positive minimum count. This is only a necessary exponent.

The witness \(v_1\) lies in the norm's sphere. If an alternative
whole-sphere supremum merely removed the two training points, the
conclusion would be unchanged: at each finite time the two predictors
are continuous in \(v\), and the circle minus those points is dense,
so the supremum equals the full-circle supremum. A finite held-out
set or its RMS is a different observable and is not covered.

## Minor issues and limits

No mathematical correction is required for the exact statement reviewed.
The following are presentation issues:

- The introduction says “fixed positive labels,” but the example has
  one zero label. “Fixed labels of positive RMS” would be exact.
- RESULT.md contains control characters at lines 146 (U+0008),
  519 and 604 (U+000B), and 612 (U+000C), plus tabs inside intended
  mathematical commands at lines 214, 559, and 566. Many inline
  mathematical expressions also use plain parentheses. The intended
  symbols are recoverable from the displayed equations, but the source
  should be repaired before reader-facing use.
- The count \(q^2+3q\) is exactly the retained real **weights**, not
  a claim about every diagnostic metadata field or finite-word storage.
  The candidate's main mathematical statement uses the weight count.

The check does not establish the supplied dense upper theorem, a dense
lower bound, fitted-endpoint failure, any finite held-out RMS guarantee,
a numerical onset width, an optimal lower exponent, or sufficiency at
linear retained-weight growth. It also does not address adaptive or
random choices of \(q\), repeated candidate selection, a modified
post-activation matching initializer, or other compressed constructions.
The ideal Gaussian and exact-arithmetic qualifiers are essential to the
model checked: floating-point rank rejection and a finite PRNG are not
the algebraic initializer proved here. No experiments, GPU runs, source
changes, or finite-precision validation were performed.

## Source and process provenance

The complete frozen candidate was read. The scientific definitions and
facts actually used were the four assigned code definitions, the paper's
setting and benchmark definition, the supplied dense upper statement,
and the appendix's shared setup and sufficient label cap.
No study README, contributor lemma, contract audit, other study,
previous verdict, or other reviewer's finding was read.

Whole-file SHA256 values at the time of inspection:

| File | SHA256 |
|---|---|
| RESULT.md | 17a1dabd526de6fa81aad30c5804208eb9171d9b95b6f2fb20373210c81b8226 |
| paper/figures/capture_trajectory.py | bbb53b4e473be7efa079bc7d46fe5a4564e0625630c701fa7a3dd5152e8f69b2 |
| paper/main.tex | 63c2f6b406fa7315bc7e80670487baaaff33c68b8ffb9c4def445d46dd8bb559 |
| paper/results.tex | 348e8e44777944557bb161aebbce3de9cbfdca4e8e1331f0fab072e881de8606 |
| paper/integrated_appendix.tex | 5d5c0c6ebe61d594f516eccc90360a7ca40cfa030656fa5af8452bcea5b7f137 |

The required solve-math-rigorously skill, explain-with-canonical-notation
skill, and its neural-response-memory reference were read completely.
Their hashes are, respectively,
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7,
daac37e41dca5e618c5baf2a65689000e526930f059b822ebec61aafbfd1abfc,
and c2d570aac8950b5766513d81dd2dada4a9babeba92bbb554f1042107207a52b1.

The actual read windows requested more than the allowed selected
passages: code lines 81–148 and 791–935, main.tex lines 122–243,
results.tex lines 1–106, and appendix lines 1–245. A text search also
displayed matching label-related lines elsewhere in that appendix.
The code windows included unrelated LoRA and test code; the main-text
window included experimental claims; the other windows included
comparison statements beyond the assigned bound and label setup.
Some combined output was truncated. These extra passages were not
premises, but their exposure violates strict read isolation and has
been reported to the supervisor. The mathematical reconstruction may
serve as a non-isolated scoped internal check only.

## Final-version check

I reread only the revised RESULT.md as scientific input for this follow-up.
Its verified final SHA256 is
3a1385aebcc480606885c699e3ada94c45190d48b0fa9aa3c8994e966382b334.

**Mathematical verdict remains PASS for the same scope.** The proof
equations, estimates, hypotheses for the limiting arguments, and
retained-weight conclusion agree with the reconstruction above.
The first layer is now explicitly iid Gaussian and independent of the
other initialization draws; this states the sampling law already used
by the proof. The added continuity remark for the circle minus the two
training points agrees with the argument checked above.

The revised introduction correctly says “a fixed nonzero label vector.”
The malformed mathematical commands and inline delimiters identified
above are repaired. A scan found no residual tabs or the previously
reported C0 control characters. The final checks paragraph now points
to the README for report qualifications; I did not follow that pointer.
Thus the earlier wording and typesetting findings describe the original
hash and are resolved in this final version. The retained-weight versus
metadata distinction remains a scope clarification.

The original non-isolated disclosure and every substantive limitation
of this report remain in force. This follow-up does not convert it
into an isolated review, prove the imported dense upper theorem, or
authorize promotion.
