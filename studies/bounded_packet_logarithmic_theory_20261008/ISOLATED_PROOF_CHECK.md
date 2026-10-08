# Independent isolated proof check

**Final-version verdict: PASS for the mathematical implication (3), its conditional benchmark consequences (1)–(2), and the finite-time unseen-input extension stated below.** No mathematical defect was found in the fluctuation, nonlinear-flow, or probability arguments. The final input explicitly specifies the Gaussian first-layer law and corrects the label wording identified during this check. No mathematical correction remains outstanding within this review's scope.

This is internal mathematical validation, not promotion to established theory.

## Frozen input and review boundary

The sole scientific input was the complete file
`studies/bounded_packet_logarithmic_theory_20261008/RESULT.md`. The initially assigned revision had SHA256

```text
17a1dabd526de6fa81aad30c5804208eb9171d9b95b6f2fb20373210c81b8226
```

After explicit authorization to inspect the revised input, I verified its hash and reread that file completely. The final verdict applies to the final revision with SHA256

```text
3a1385aebcc480606885c699e3ada94c45190d48b0fa9aa3c8994e966382b334
```

The revised input explicitly states independent standard-normal packet first weights and the mutual independence of its sampling blocks, changes the opening to “fixed nonzero label vector,” adds the finite-time continuity argument for excluding training points, and repairs mathematical typography. Its final source paragraph points to the study README; I did not follow that pointer. The equations and bounds supporting the reconstruction below are unchanged.

I read its full contents and independently reconstructed the steps below. I read the required mathematical-presentation and rigorous-proof skills. I did not read a study README, history, another report, code, linked paper, other repository scientific source, or external scientific source. No numerical experiments were performed. This report is the only file written.

As assigned, the displayed network, Gaussian initializer, and mobilities are treated as a mathematical model. Equation (4) is an explicitly supplied comparison theorem. Its proof, its correspondence to the paper, literal code fidelity, finite-word sampling, numerical rank decisions, and claims about a different decoder are outside this review. Thus the check of (3) is independent of (4), while the checks of (1)–(2) are conditional on (4).

The proof has four distinct requirements: a nondegenerate initial-velocity fluctuation, a uniform bound on the error of replacing the actual prediction by its initial velocity times time, an argument covering fixed as well as diverging packet widths, and a comparison of the resulting small-ball scale with the supplied tolerance. Each requirement is verified below.

## Model, initial velocity, and Gaussian sphere law

For width $p$, the model has $W^{(1)}\in\mathbb R^{p\times2}$, $W^{(2)}\in\mathbb R^{p\times p}$, and $w\in\mathbb R^p$, with

\[
h^{(1)}(t,v)=\tanh(W^{(1)}(t)v),\qquad
h^{(2)}(t,v)=\tanh(W^{(2)}(t)h^{(1)}(t,v)),\qquad
f(t,v)=p^{-1}w(t)^\top h^{(2)}(t,v).
\]

The training inputs are $v_1=e_1,v_2=e_2$; the labels are $y_1=\sqrt2Y,y_2=0$, with fixed $Y>0$; and $w(0)=0$. The loss is $\mathcal L=\frac12\sum_{a=1}^2(f(t,v_a)-y_a)^2$, with block mobilities $(p,1,p)$. Hence $\mathcal L(0)=Y^2$.

For $G\sim N(0,1)$, the numbers

\[
\alpha=\mathbb E\tanh^2G,\qquad
\gamma=\mathbb E\tanh^2(\sqrt\alpha G)
\]

belong to $(0,1)$. Independence and oddness give the diagonal population covariances stated in the input. The activation bounds on the strip $|\operatorname{Im}z|\le1/2$ are correct: the denominator identity for $|\cosh z|^2$ gives $|\tanh' z|\le\sec^2(1/2)<2$; the displayed quotient gives $|\tanh z|\le1$; and $\tanh''z=-2\tanh z\tanh' z$ gives $|\tanh''z|<4$. The numerical label substitution in (7) matches the allowance explicitly quoted in the file. The paper-specific envelope and admissibility theorem were not separately audited.

For the packet model, put $P=H(H^\top H)^{-1}H^\top$. Whenever $H$ has rank two, $P$ is the orthogonal projection onto its column space, and

\[
W^{(2)}(0)=G_q(I-P)+ZH^\dagger
\quad\Longrightarrow\quad
W^{(2)}(0)H=Z.
\]

Gaussian first weights transformed entrywise by the strictly increasing function $\tanh$ give independent entries with densities on $(-1,1)$. The determinant of the leading two-by-two block vanishes on a Lebesgue-null set, so both $H$ and $H_{\rm source}$ have rank two almost surely for $q,n\ge2$. Consequently all the displayed inverses and the positive Cholesky factor exist almost surely.

For a full-rank Gaussian $q\times2$ matrix, thin QR with positive diagonal is unique. Left multiplication by an orthogonal matrix preserves both the Gaussian distribution and the positive-diagonal QR convention, proving orthogonal invariance of its $Q$ factor. More directly, its first $Q$ column is the first Gaussian column divided by its norm. This alone supplies the sphere law needed in the proof; independence of all packet rows is neither true nor used.

Since $R$ is lower triangular with $RR^\top=K$, its first diagonal entry is $\sqrt{K_{11}}$, and the first column of $R^\top$ is $(\sqrt{K_{11}},0)^\top$. Thus the first column of $Z$ is $\sqrt{qK_{11}}u$, where $u$ is uniform on $S^{q-1}$ and independent of the source. The initial second-layer feature average at $v_1$ is exactly distributed as

\[
A_{q,n}=\frac1q\sum_{i=1}^q\tanh^2(\sqrt{qK_{11}}u_i).
\]

At $w=0$, both hidden-weight velocities vanish and

\[
\dot w(0)=\sqrt2Yh^{(2)}(0,v_1),\qquad
\dot f(0,v_1)=\frac{\sqrt2Y}{p}\|h^{(2)}(0,v_1)\|_2^2.
\]

This verifies (12), including the factor $\sqrt2Y$.

## Nondegenerate limit for diverging packet width

Let $X_i$ be independent standard normals, let $s_q=q^{-1}\sum_iX_i^2$, and write $u_i=X_i/\sqrt{qs_q}$. Define $g(x)=\tanh^2(\sqrt\alpha x)$. Then

\[
A_q:=\frac1q\sum_i g(X_i/\sqrt{s_q})
\]

is the packet average with $K_{11}$ replaced by $\alpha$. We have $\mathbb Eg(G)=\gamma$ and $s_q-1=O_{\mathbb P}(q^{-1/2})$.

For the scalar function $a(z)=\tanh^2z$, both $za'(z)$ and $z^2a''(z)$ are bounded on the real line. With $F(s,x)=a(\sqrt{\alpha/s}\,x)$ and $z=\sqrt{\alpha/s}\,x$, differentiation gives

\[
F_s(s,x)=-\frac{za'(z)}{2s},\qquad
F_{ss}(s,x)=\frac{3za'(z)+z^2a''(z)}{4s^2}.
\]

The second derivative is bounded uniformly in $x$ for $s\in[1/2,3/2]$. Since $s_q$ lies in that interval with probability tending to one, averaging Taylor's theorem gives a remainder $O_{\mathbb P}((s_q-1)^2)=O_{\mathbb P}(q^{-1})$. At $s=1$,

\[
\frac1q\sum_iF_s(1,X_i)
=-\frac1{2q}\sum_iX_ig'(X_i)
=-\kappa+o_{\mathbb P}(1),
\qquad
\kappa=\tfrac12\mathbb E[Gg'(G)].
\]

The last convergence follows from the law of large numbers for bounded independent identically distributed summands. Multiplying its error by $\sqrt q(s_q-1)=O_{\mathbb P}(1)$ therefore leaves $o_{\mathbb P}(1)$. The result is exactly

\[
\sqrt q(A_q-\gamma)
=\frac1{\sqrt q}\sum_{i=1}^q
\bigl[g(X_i)-\gamma-\kappa(X_i^2-1)\bigr]
+o_{\mathbb P}(1).
\]

The summands are independent and identically distributed, centered, and square integrable: $g$ is bounded and a Gaussian has finite fourth moment. Moreover,

\[
\kappa=\mathbb E[\sqrt\alpha G\tanh(\sqrt\alpha G)
                       \operatorname{sech}^2(\sqrt\alpha G)]>0,
\]

because its integrand is positive whenever $G\ne0$. If the variance of a summand were zero, continuity and the strictly positive Gaussian density would imply

\[
g(x)-\gamma=\kappa(x^2-1)\qquad\text{for every }x\in\mathbb R.
\]

The left side is bounded and the right side is unbounded. This contradiction proves $\sigma^2>0$ in (16). The scalar central limit theorem for centered independent identically distributed variables of finite variance applies, giving $\sqrt q(A_q-\gamma)\Rightarrow N(0,\sigma^2)$.

The source-radius replacement is uniform in the sphere point and in $q$. On the event $K_{11}\ge\alpha/2$, the interval between $K_{11}$ and $\alpha$ stays above $\alpha/2$, and

\[
\left|\partial_k a(\sqrt{qk}u_i)\right|
=\frac{|za'(z)|}{2k}\le C_\alpha.
\]

Since $K_{11}-\alpha=O_{\mathbb P}(n^{-1/2})$, the average replacement error is $O_{\mathbb P}(n^{-1/2})$, including the vanishing-probability complementary event in the usual definition of $O_{\mathbb P}$. Multiplication by $\sqrt q$ makes it negligible when $q/n\to0$.

For the ordinary dense network, conditioning on its first layer makes its second preactivations at $v_1$ independent $N(0,K'_{11})$. Their bounded squared-$\tanh$ average has conditional variance at most $1/(4n)$. Its conditional mean $\mu(K'_{11})$, where $\mu(k)=\mathbb E\tanh^2(\sqrt kG)$, differs from $\mu(\alpha)=\gamma$ by $O_{\mathbb P}(n^{-1/2})$: the preceding pointwise derivative bound makes $\mu$ locally Lipschitz near $\alpha$. Conditional Chebyshev followed by averaging gives an additional $O_{\mathbb P}(n^{-1/2})$ fluctuation. Thus its full average is $\gamma+O_{\mathbb P}(n^{-1/2})$.

Multiplying the difference of the averages by $\sqrt2Y\sqrt q$ proves (17). Slutsky's theorem applies even if the target is coupled to the packet model: the target contribution tends to zero in probability, so independence from the packet fluctuation is unnecessary. The packet's own source and Gaussian sampling assumptions remain part of its marginal definition.

## Full nonlinear flow and uniform remainder

Direct differentiation of the loss with the stated mobilities gives exactly (18). For $r_a=f(t,v_a)-y_a$, the chain rule yields

\[
\dot{\mathcal L}
=-p^{-1}\|\dot W^{(1)}\|_F^2
 -\|\dot W^{(2)}\|_F^2-p^{-1}\|\dot w\|_2^2.
\]

Hence $m^{-1}\sum_a|r_a|\le\sqrt{\mathcal L}\le Y$. Since every real $\tanh$ feature has norm at most $\sqrt p$, and each diagonal derivative matrix has operator norm at most one, (18) implies

\[
\frac{\|\dot w\|_2}{\sqrt p}\le2Y,
\qquad
\|\dot W^{(2)}\|_F\le\frac{2Y\|w\|_2}{\sqrt p},
\qquad
\frac{\|\dot W^{(1)}\|_F}{\sqrt p}
\le2Y\|W^{(2)}\|_{\rm op}\frac{\|w\|_2}{\sqrt p}.
\]

Integrating the first inequality, substituting it into the second, and using $\|W^{(2)}(t)\|_{\rm op}\le M+\|W^{(2)}(t)-W^{(2)}(0)\|_F$, where $M\ge\|W^{(2)}(0)\|_{\rm op}$, gives all three bounds in (19), with their displayed constants.

For each fixed finite width the vector field is smooth on the full Euclidean parameter space. The bounds just obtained, including the integral of the bound on $\dot W^{(1)}$, keep every parameter bounded on every finite interval. The continuation theorem for a locally Lipschitz finite-dimensional ODE says that a finite maximal existence time requires the solution to leave every compact subset of its domain. Closed bounded parameter balls are compact and the domain is the whole space, so finite-time explosion is excluded. This establishes actual finite-time solutions rather than formal Taylor series.

Set $S=1+(M+2Y^2)^2$. For $0\le t\le1$ and $\|v\|_2\le1$, differentiation of the two forward layers gives

\[
\frac{\|\dot h^{(1)}(t,v)\|_2}{\sqrt p}
\le4Y^2t(M+2Y^2),
\]

and then

\[
\frac{\|\dot h^{(2)}(t,v)\|_2}{\sqrt p}
\le\|\dot W^{(2)}\|_F
 +\|W^{(2)}\|_{\rm op}
     \frac{\|\dot h^{(1)}(t,v)\|_2}{\sqrt p}
\le4Y^2St.
\]

Integration proves (20). Also $|f(t,v)|\le\|w(t)\|_2/\sqrt p\le2Yt$, and $m^{-1}\sum_a|y_a|\le Y$. Subtracting $\dot w(0)$ from the readout equation therefore gives

\[
\frac{\|\dot w(t)-\dot w(0)\|_2}{\sqrt p}
\le4Yt+4Y^3St^2,
\]

so that

\[
\frac{\|w(t)-t\dot w(0)\|_2}{\sqrt p}
\le2Yt^2+\tfrac43Y^3St^3.
\]

In the exact prediction decomposition preceding (21), the first term is bounded by this quantity and the second by $t(2Y)(2Y^2St^2)=4Y^3St^3$. Their sum proves precisely (21), including $16/3$. Hidden weights and their effect on the features were retained throughout.

## Tightness of the initial mixer

The cross terms in $W^{(2)}(0)W^{(2)}(0)^\top$ vanish because $(I-P)H=0$. Moreover $H^\dagger H^{\dagger\top}=(H^\top H)^{-1}$, giving the exact identity before (22). Since $U^\top U=I_2$, one has $\|Z\|_{\rm op}^2=q\|K\|_{\rm op}$. Therefore

\[
\|W^{(2)}(0)\|_{\rm op}^2
\le\|G_q\|_{\rm op}^2+
 \frac{\|K\|_{\rm op}}{\lambda_{\min}(H^\top H/q)}.
\]

The numerator is at most $\operatorname{tr}K\le2$ deterministically. For the Gaussian first-feature sampling used in the input, the entries of $H^\top H/q$ have means $(\alpha I_2)_{ab}$ and variances at most $1/q$. Chebyshev and the finite number of entries give convergence in operator norm to $\alpha I_2$; the eigenvalue inequality $\lambda_{\min}(A)\ge\alpha-\|A-\alpha I_2\|_{\rm op}$ then proves the required lower bound $\alpha/2$ with probability tending to one.

A maximal $1/4$-separated sphere set is a $1/4$-net and has size at most $9^p$ by the volume comparison in the input. Approximating the left and right unit vectors of a bilinear form separately leaves an error at most $\frac12\|G_p\|_{\rm op}$, hence

\[
\|G_p\|_{\rm op}\le2\max_{u,v\text{ in the net}}|u^\top G_pv|.
\]

For fixed net vectors the scalar variance is $1/p$, so its Gaussian tail at $4$ is at most $2e^{-8p}$. There are at most $9^{2p}$ pairs. The union bound therefore gives exactly (23), and $8-2\log9>0$. The chosen constant $M=\sqrt{64+4/\alpha}$ suffices when $q,n\to\infty$.

For a fixed $q\ge2$, the smallest eigenvalue of $H^\top H/q$ is strictly positive almost surely. Its reciprocal is thus an almost-surely finite random variable, hence tight; this needs no finite inverse moment. Together with $\|K\|_{\rm op}\le2$, it proves tightness uniformly in source width $n$. A finite collection of bounded widths remains tight. The large-width estimate and these finite collections jointly prove tightness over arbitrary width sequences. Consequently the random coefficient of $t^3$ in (21) is $O_{\mathbb P}(1)$; the proof never assumes its expectation is bounded.

## Fixed packet widths and shrinking intervals

For fixed $q\ge2$, define $h(s)=\tanh^2(\sqrt{q\alpha s})$ on $[0,\infty)$. At $s>0$,

\[
h'(s)=q\alpha\frac{\tanh z}{z}\operatorname{sech}^2z,
\qquad z=\sqrt{q\alpha s}.
\]

The factor $\operatorname{sech}^2z$ strictly decreases for $z>0$. The factor $\tanh z/z$ also strictly decreases, since $\tanh z-z\operatorname{sech}^2z$ is zero at zero and has derivative $2z\operatorname{sech}^2z\tanh z>0$. Both factors are positive. Thus $h'$ strictly decreases, extends to $h'(0)=q\alpha$, and makes $h$ strictly concave.

Condition on $R=\sqrt{X_1^2+X_2^2}$ and on $X_3,\ldots,X_q$. Here $R>0$ almost surely. The angle of $(X_1,X_2)$ remains uniform and independent of the conditioned variables. With

\[
s=\frac{R^2}{R^2+\sum_{j=3}^qX_j^2}\in(0,1],
\]

the two varying terms of the sphere average are $h(s\cos^2\theta)+h(s\sin^2\theta)$, divided by $q$. The other terms are fixed. The derivative of $u\mapsto h(su)+h(s(1-u))$ is

\[
s\bigl[h'(su)-h'(s(1-u))\bigr],
\]

which is positive for $u<1/2$ and negative for $u>1/2$. Every level has at most two $u$-preimages, hence only finitely many angle-preimages in one period. Uniform angle assigns each level probability zero. Integrating the conditional probabilities proves that the average has no atoms. For $q=2$, $s=1$ and the same argument applies without change.

The source-radius replacement tends to zero in probability, and the dense average tends to $\gamma$. Thus the initial-velocity difference converges to the nonatomic law

\[
\sqrt2Y\left(\frac1q\sum_i\tanh^2(\sqrt{q\alpha}u_i)-\gamma\right).
\]

The exact elementary probability principle needed in both width regimes is: if $Z_n\Rightarrow Z$, $a_n\to0$ with $a_n\ge0$, and $\Pr(Z=0)=0$, then $\Pr(|Z_n|\le a_n)\to0$. Indeed, for every fixed $a>0$, eventually $\{|Z_n|\le a_n\}\subseteq\{|Z_n|\le a\}$. The closed-set inequality for convergence in distribution gives a limiting upper bound $\Pr(|Z|\le a)$. Letting $a\downarrow0$ yields zero. No quantitative density bound or local central limit theorem is needed.

## Implication (3), benchmark consequences, and quantifiers

Let $\varepsilon_n>0$ be deterministic, $q=q(n)\ge2$ be deterministic and integer valued, and suppose $q/n\to0$ and $q\varepsilon_n\to0$. Then $\varepsilon_n\to0$. Put $t_n=\sqrt{\varepsilon_n}$, so $0<t_n\le1$ eventually.

If $q\to\infty$, subtract (21) for the two flows and multiply by $\sqrt q/t_n$. The remainder is

\[
O_{\mathbb P}(\sqrt q\,t_n)
=O_{\mathbb P}(\sqrt{q\varepsilon_n})=o_{\mathbb P}(1).
\]

Equation (17) therefore gives the nondegenerate Gaussian limit in (24). Success in the full norm implies that this scaled scalar discrepancy lies in the interval of radius $\sqrt{q\varepsilon_n}\to0$. The preceding probability principle proves vanishing success probability.

If $q$ is fixed, division only by $t_n$ gives an $O_{\mathbb P}(t_n)$ remainder, so the scaled discrepancy has the nonatomic limit just proved. Success requires absolute value at most $\sqrt{\varepsilon_n}\to0$, again with vanishing probability.

For an arbitrary integer sequence $q(n)\ge2$, a subsequence either contains a constant-width further subsequence or contains a further subsequence with $q\to\infty$. If success probabilities had positive limsup, one could first select a subsequence bounded below by a positive constant and then one of these two width regimes, contradicting the corresponding result. This proves (3) for all the asserted deterministic width sequences. It also shows why no assumption that the width monotonically increases is needed.

Taking $t_n=1/q$ instead makes the scaled remainder $O_{\mathbb P}(q^{-1/2})$, proving (25) under its inherited assumptions $q\to\infty$ and $q/n\to0$. The fixed-width argument, rather than (25), covers bounded polylogarithmic choices.

Under the supplied theorem (4), its right-hand side is a deterministic positive upper envelope $B_n=n^{-1/2+o(1)}$, after enlarging a constant if necessary. If $q^2+3q=O(n^{1-\eta})$ for fixed $0<\eta<1$, then

\[
q/n=O(n^{-(1+\eta)/2})\to0,
\qquad
q(3B_n)\le n^{-\eta/2+o(1)}\to0.
\]

Applying (3) at the positive tolerance $3B_n$, and using inclusion of the event with tolerance $3b_n\le3B_n$, proves (2) even if $b_n=0$ at some widths. A fixed polylogarithmic weight bound is $O(n^{1-\eta})$, for example with $\eta=1/2$, so (1) follows as well. Alternatively its two conditions can be checked directly.

If a deterministic width choice had success probability at least $0.99$ for every sufficiently large $n$, an infinite subsequence with $q^2+3q\le n^{1-\eta}$ would contradict the same argument restricted to that subsequence. Therefore for each fixed $0<\eta<1$, its weight count must eventually exceed $n^{1-\eta}$. For $\eta\ge1$ this is automatic from $q\ge2$. The necessary exponent statement is thus correct with the stated order of quantifiers: each fixed $\eta>0$ has its own eventual-width threshold. It does not prove an $\Omega(n)$ weight bound, a sufficient construction at exponent one, or a guarantee for a width chosen adaptively from the random initialization.

## Optional unseen-input extension

The proposed extension is correct for this example. Fix a realization of the parameters and any finite $t\ge0$. Global finite-time existence ensures all parameters are finite, and finite compositions of linear maps and $\tanh$ make

\[
v\longmapsto |f_{\rm packet}(t,v)-f_n(t,v)|
\]

continuous on $S^1$. If $T\subset S^1$ is the finite training list, $S^1\setminus T$ is dense. Every $v\in T$ is a limit of points from its complement, so continuity gives

\[
\sup_{v\in S^1\setminus T}|f_{\rm packet}(t,v)-f_n(t,v)|
=\sup_{v\in S^1}|f_{\rm packet}(t,v)-f_n(t,v)|.
\]

This pathwise identity holds for every finite $t$, hence also after taking a supremum over finite times. In particular, excluding the two training inputs from a supremum over all other sphere points leaves the obstruction intact. The same proof works on $S^{d-1}$ for $d\ge2$. It does not generally work for $d=1$, does not turn the result into a statement about a prescribed finite held-out dataset, and does not establish continuity of a limit at $t=\infty$. None of those stronger claims is required by the proposed finite-time extension.

## Resolved exposition clarifications and limits of this verdict

The initial revision left the packet first-layer law implicit in the description and the subsequent Gaussian-density and covariance calculations. The final revision explicitly states beside (9) that the packet $W^{(1)}_{ia}(0)$ are independent $N(0,1)$ variables and specifies the independence of the sampling blocks. This resolves the definition ambiguity and states the Gaussian sampling law used by the verified rank and tightness arguments. Continuous marginal densities alone would not imply the covariance law of large numbers; arbitrary alternative first-layer distributions are not covered by this check.

The initial opening phrase “fixed positive labels” was inaccurate because the example has $y_2=0$. The final revision uses “fixed nonzero label vector.” The proof consistently uses the displayed labels and is unaffected.

The verdict establishes the mathematical obstruction for the specified ideal Gaussian model. It does not independently establish the imported bound, its historical source, implementation correspondence, any claim about other decoders, an endpoint discrepancy lower bound, or finite-precision behavior. No promotion review or approval is implied.
