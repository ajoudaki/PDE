# Scoped check of the joint width–sample frozen-top NTH lower bound

Verdict: **PASS for the stated joint width–sample, identity-activation, literal-array theorem.** I found no mathematical gap in the chain proving equations (10)–(12) and the resulting superpolynomial array count. This is a scoped internal check, not a promotion review and not a proof of the original fixed-dataset nonlinear lower-bound target.

Reviewer: `worst_smooth_witness`, 2026-10-10. The reviewer previously authored a different smooth-activation route in this same study; that route was not used as a scientific dependency here. No other check report was read. The supervisor explicitly authorized cross-reconstruction from the growing-sample author's file. No experiments, Git mutations, or shared-file edits were performed.

## Complete read coverage and frozen versions

Read every line of the following three files, including the scalar analytic lemma and its tail comparison:

| File | SHA256 |
|---|---|
| `WORST_CASE_RESULT.md` | `98860493baf152fe08b063671532098dc7503fe0c5714d255ba1218ac0afc19f` |
| `STRONGER_SOURCE.md` | `6c0115cbb038fc2fd0822919884fd844704b6aedb997b72817670052018fd5f7` |
| `WORST_GROWING_SAMPLE_ROUTE.md` | `ed6e5017408dd989dd5e3c944315525c2d2ec3de566d8b48498d868a2f0f8601` |

The established notation and required mathematical/research skills had already been read in this scoped agent context and remained current. The exact Gaussian concentration statement in the candidate's cited source was checked against [Vershynin, Proposition 5.34](https://arxiv.org/pdf/1011.3027), PDF p. 21. It gives the one-sided mean-centered tail for a globally Lipschitz real function of a standard Gaussian vector. Scaling to variance $1/n$, applying both signs, and using the same extension for both copies supplies exactly the two-copy tail used in the candidate. The Gaussian concentration theorem is an external standard theorem; its proof is not independently reproduced here.

The candidate contains the analytic-disk argument needed here, so I did not open `ANALYTIC_ROUTE.md` or the older `RESULT.md`. I did not import their all-time statements or their old small-label regime.

## 1. Quantifiers, dataset, activation, and coordinate change

For each sufficiently large $n$ and each deterministic multiple of four $m$ with $4\le m\le\sqrt n$, the construction sets $d=m+1$. The activation and label magnitude $0<\eta\le1$ are fixed; the dataset and the designated passive query vary with $m$. Constants are uniform over the displayed sample range. The theorem's simultaneous assertion is over every finite rank $q$ for the chosen $(n,m)$; a simultaneous coupling of every possible $m$ is not needed.

The direct checks are

$$
v_a^Tv_b=\frac{1+\delta_{ab}}2,
\quad \lambda^2:=\left\|\frac1m\sum_a s_av_a\right\|^2
=\frac18+\frac1{2m},
\quad \frac1m\sum_a(y_a-\eta/2)^2=\frac{3\eta^2}4.
$$

Every input submatrix has smallest singular value at least $1/\sqrt2$. The query $v_*=\bar v/\lambda$ has all private coordinates nonzero and is distinct from every training vector. Identity has bounded first derivative and zero higher derivatives, so it is admitted by Huang–Yau's Assumption 2.1. Their input-norm condition is checked on the effective normalized inputs $v_a$; the canonical physical inputs $x_a=\sqrt d\,v_a$ themselves have growing Euclidean norm. This is consistent with the explicitly specified canonical first-layer normalization.

The transformation $B=W^{(1)}/\sqrt n$, $c=u/\sqrt n$, $W=W^{(2)}$ maps the mobilities $(n,1,n)$ exactly to the Euclidean metric, and gives $f(v)=c^TWBv$. It does not map the system to Huang–Yau's native NTK training regime. The candidate says this explicitly.

The Gaussian event is valid uniformly in $d\le\sqrt n+1$. A $1/4$ sphere net has at most $9^k$ points; the upper-tail exponent for $\chi_n^2\ge9n$ is $(9-1-\log9)n/2>n\log9$, proving the operator-norm bound $4$ even for the square matrix. The two specified-direction lower bounds follow by taking both independent chi-square ratios at least $3/4$, whose product is $9/16>1/2$. The optional empirical Gram certificate is also valid: on a $1/8$ net, quadratic-form deviation at most $3/16$ extends to at most $1/4$ on the full sphere. Apply this to $B_0$ and conditionally to $W_0$ on the $d$-dimensional image of $B_0$. The net costs $\exp(O(d))$, absorbed by the $\exp(-cn)$ tail. This gives the asserted product lower bound $9I/16$ and feature Gram gap $9/32$.

## 2. First omitted physical derivative, including feedback

Each appended source derivative flips parity in the readout $c$: the $B,W$ components of $\nabla f_a$ are odd in $c$ and the $c$ component is even. Thus odd initialized ranks vanish. A frozen odd top is identically zero, so its preceding even rank is constant and the closure agrees with the preceding even-top closure.

Let $Q=2\lfloor q/2\rfloor$ and $j=Q+1$. Repeated integration of the hierarchy expresses the output through initial $K_{k+1}$ and ordered products of its own residual controls. The dense and rank-$Q$ series share the terms through $k=Q-1$. The omitted term $k=Q$ vanishes by parity. The first surviving omitted term has $k=j$.

Coefficient induction gives agreement of the physical prediction jets below degree $j$. A prediction difference beginning at degree $j$ changes a control at degree $j$; every occurrence of such a control in an output term is integrated at least once, so its feedback affects degree at least $j+1$. Therefore the degree-$j$ discrepancy uses precisely the common initial controls $\eta s_b/m$, with coefficient one, not a binomial multiplicity. Multilinearity in every input then gives

$$
g^{(j)}(0)=\eta^jK_{j+1}(\bar v,\ldots,\bar v;0).
$$

As a boundary check, for rank two the first omitted tensor is $K_3(0)=0$ and the first error is at derivative three, namely the contraction of $K_4(0)$ against three initial controls. Terms differentiating the residual use matching lower prediction derivatives and cancel. This agrees with the general formula.

This derivation retains the closure's own residual. It neither equates dense and closure source clocks nor supplies a future dense residual.

## 3. Factorial source estimate and its scale

Gradient ascent of $F=c^TWB\bar v$, with $b=Bv_*$ and $\tau=\lambda s$, gives exactly

$$
b'=W^Tc,\qquad W'=cb^T,\qquad c'=Wb.
$$

The conserved quantities are $WW^T-cc^T=W_0W_0^T$ and $\|b\|^2-\|c\|^2=A:=\|b_0\|^2$. Hence

$$
c''=(AI+W_0W_0^T)c+2\|c\|^2c.
$$

After an orthogonal diagonalization and eigenvector sign choice, the Taylor recurrence has nonnegative coefficients and initial velocity $h=W_0b_0\ge0$ componentwise. It dominates $hu$, where $u''=Au+2Hu^3$ and $H=\|h\|^2$. Zero components of $h$ cause no division or exception. On the good event $A,H\ge1/2$, this scalar recurrence dominates $v=2\tan(\tau/2)$ because

$$
v''=\tfrac12v+\tfrac18v^3.
$$

The tangent recurrence proves coefficientwise $v\succeq w:=\tau/(1-\tau^2/12)$. Multiplication and differentiation preserve these coefficientwise inequalities, so the standard source prediction $c^Tc'$ dominates $Hww'$. For $j=2k+1$, its derivative is at least $j!H(k+1)^2/12^k\ge j!8^{-j}$.

Returning to the original source multiplies the derivative by $\lambda^{j+1}$. Since $\lambda\ge8^{-1/2}$ and $j\ge1$,
$\lambda^{j+1}\ge8^{-j}$. This proves the candidate's $j!64^{-j}$ and, with the physical jet, $g^{(j)}(0)\ge j!(\eta/64)^j$. The proof holds for every odd $j$ on the same initialization event.

## 4. Uniform complex disk and scalar transfer

The ordered-derivative estimate is dimension-free. A cubic prediction initially has three parameter leaves; each source derivative replaces one leaf by a quadratic product. After $k$ derivatives the term count is bounded by $3\cdot4\cdots(k+2)=(k+2)!/2$, and every term is bounded by $4^{k+3}$ on the initial norm ball. The gradients have rank-one matrix factors, so no hidden Frobenius dimension factor appears. This yields $32\,4^k(k+2)!$.

For holomorphic prediction paths of sup norm at most one,

$$
\sum_b|(y_b-f_b)/m|\le2,
\qquad \sum_b|(f_b-\widetilde f_b)/m|\le\|f-\widetilde f\|_\infty.
$$

The sum over all ordered sample strings is therefore already included in these bounds; there is no additional $m^k$. Simplex integration contributes $|t|^k/k!$. At $R_0=1/4096$ the stated image and Lipschitz bounds, respectively below $0.38$ and $0.2$, follow from the convergent scalar series. They apply to every finite truncation. Recovering the lower tensors from their ordered integrals gives the original finite ODE solution, so this fixed-point construction is not another closure.

For the dense complex flow, the norm-five ball gives vector-field norm $3150$ and derivative norm $3135$ in the maximum block norm. Both multiplied by $R_0$ are below one. The output bound follows from $|K_2|\le3\cdot5^4=1875$ and $e^{1875R_0}-1<1$. Thus all discrepancies are holomorphic near the closed disk $R=R_0/2$ and bounded by two, uniformly in $m,n,q$.

I checked every step of `STRONGER_SOURCE.md` (15)–(23). The Chebyshev endpoint derivative formula supplies the additional factor $1/j!$; Cauchy's tail is $M4^{-N}/3$. With $N=\lceil\kappa j\rceil$ and $\kappa=16(1+b+d)$, the tail estimate reduces to

$$
b+d+3\log(2\kappa)+3\le15(1+b+d)<\kappa\log4.
$$

The final weakening uses $N\le2\kappa j$, $j!\ge(j/e)^j$, and $j\le2^j$, all valid including $j=1$. Substituting $\rho=\eta/64$, $R=2^{-13}$, $M=2$ gives $\theta=\eta/2^{22}$ and exactly the constants in the candidate. The query error equals $g/\lambda$ by input linearity, and $\lambda\le1$, so the real-interval bound applies to the declared passive query without loss.

## 5. Dense-pair discrepancy

The matrix $Q=m^{-1}\sum_av_av_a^T$ and vector $b=m^{-1}\sum_ay_av_a$ have norms at most one. Writing the dense equations in these two objects gives the candidate's equation (21), including the signs and normalization.

For two states in the norm-five ball, put
$\delta=\|\Delta B\|_F+\|\Delta W\|_F+\|\Delta c\|_2$.
The predictor vector changes by at most $25\delta$, the residual vector is at most $126$ and changes by at most $25\delta$. A telescoping expansion bounds each velocity difference by $1255\delta$, hence the sum by $3765\delta$. At initialization $\Delta c=0$, so the sum norm is at most $\sqrt2$ times the Euclidean norm of all random entries. The candidate's Lipschitz constant $50e^{4000T}$ is therefore conservative.

A real scalar observable on the common good set admits a same-constant Lipschitz extension, for example
$\inf_{z\in\mathcal G}[F(z)+L\|x-z\|]$.
Gaussian concentration applies to this extension. The extension is chosen once for each query and time and is shared by the two copies, so its mean cancels. The common good event is removed once, not once per net point.

The $1/2$ sphere net has at most $5^d$ points and costs a factor two when extending the maximum to the sphere. The two-copy concentration threshold is $2s$, giving the grid bound $4s$. Each predictor coefficient vector has time Lipschitz constant below $250000$, so the two-copy grid remainder is $500000/n$. The specified choice of $s$, union bound over $5^d(\lceil nT\rceil+1)$ points, and $\delta=1/n$ establish

$$
D_n\le C\sqrt{\frac{m+\log(en)}n}
$$

with the claimed failure probability. No lower-tail bound for $D_n$ or a limit theorem is needed for the subsequent comparison.

## 6. Feature motion and the storage implication

The three initial derivatives in equation (22) are correct. For $a=B_0\bar v$, the two signed feature-Gram contractions have second derivatives

$$
2\eta^2\lambda^2\|W_0a\|^2\ge\eta^2/64,
$$

and

$$
2\eta^2[\|W_0a\|^2\|a\|^2+
\lambda^2\|W_0^TW_0a\|^2]\ge\eta^2/128.
$$

These are observable representation changes, not merely motion along a parameter symmetry. If one wants an explicit nonvanishing finite-time statement, the common analytic norm bounds provide a uniform cubic Taylor remainder for the real squared norms (using their holomorphic bilinear continuations). Choosing one sufficiently small $t_\eta>0$ makes that remainder at most half the positive quadratic term. Hence both feature-Gram contractions change by a positive quantity depending on $\eta$ but independent of $n,m$. This supplies the short justification between the initial accelerations and the headline that hidden features actually change.

For $r_n=n/(m+\log(en))$, the proposed rank budget gives
$E_n(q)\ge A_\eta e^{-C_\eta}r_n^{-1/4}$ simultaneously over all allowed ranks, while $D_n\le Cr_n^{-1/2}$. Since $r_n\to\infty$ uniformly for $m\le\sqrt n$, any fixed comparison factor fails with probability tending to one, including data-dependent rank selection within the deterministic budget. If $D_n=0$, the strict positive error lower bound already gives failure, so division by zero is unnecessary.

A successful rank therefore exceeds a constant multiple of $\log r_n$ with high probability. Retaining the literal arrays uses at least $m^{q-1}$ entries even if an identically zero odd top is omitted. For large enough $n$, the subtraction of one from the exponent is absorbed by halving the positive constant, giving the stated $\exp[c_\eta\log m\log r_n]$. With $m=4\lfloor n^a/4\rfloor$, $0<a\le1/2$, this is $\exp[c_{\eta,a}(\log n)^2]$.

## Scope that must accompany the result

- The result is superpolynomial only when $m$ and $d$ grow. It is not a fixed-dataset superpolynomial lower bound.
- Identity is an admissible activation, but the input–output function is linear. Active hidden motion does not make this a nonlinear-activation theorem.
- The count is for literal ordered arrays. Tensor factorization, on-demand contraction, and different closures are outside the lower bound.
- The mobilities and zero readout are the canonical feature-learning regime, not Huang–Yau's native NTK regime.
- Fixed $\eta>0$ eventually violates the older sample-dependent $Y=O(1/m)$ restriction. The local proof here does not need that restriction. If it is reinstated, the derived constants depend on $m$ and this proof no longer gives the same superpolynomial conclusion; that is not a proof that no other superpolynomial lower bound could hold in the small-label regime.

No required correction to the theorem or proof was found. For presentation, retain the divisibility condition on $m$, describe the label-restriction issue as a limitation of this derivation, and consider adding the finite-time Taylor-remainder sentence for feature motion. None changes the stated bound.

## Version update: presentation and completeness additions

Checked the supervisor's stated changes to `WORST_CASE_RESULT.md`, now SHA256 `fcbcb3835eca33d7f13a1b18a96a8a13401b9d1f4cb8a8088939eb9820fe47c1`, against the already checked argument. This was a scoped update check, not a new wider audit. The primary Assumption 2.1 link is appropriate; the small-label wording now correctly limits the inference to this derivation; the additional nonfrozen-array count $m^{q-2}$ is valid after odd-top removal and gives the same superpolynomial exponent; the inline Chebyshev and Taylor-tail proof reproduces the verified scalar argument with the correct constants; and the uniform-remainder sentence correctly supplies fixed-positive-time feature motion. All additions are sound. The PASS verdict and all scope limitations above remain unchanged.
