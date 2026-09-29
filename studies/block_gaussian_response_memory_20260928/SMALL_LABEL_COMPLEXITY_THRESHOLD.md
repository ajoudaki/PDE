# Conditional predictor-complexity threshold

This note solves the cost optimization implied by two **candidate** error bounds. It does not establish either bound for a block Gaussian network or its response-memory approximation. The scientific input is the scoped assignment only; no other study or external source is used.

Fix the training-set size \(m\), depth \(L\), input dimension \(d\), label vector, and test distribution \(\mu\). Let \(B,k,q\ge1\) be integers, \(n=Bk\), and assume

\[
 S_{\rm learned}\asymp LmBkq+O(n(d+1))\asymp nq,
 \qquad S_{\rm fixed}\asymp LBk^2\asymp nk.
\]

These are numbers of stored scalars, not arithmetic work. In particular, fixed initialization is excluded from learned state but is reported separately. No extra constraint such as \(q\le k\) is assumed. Constants below are independent of time and \(B,k,q\); they may depend on the fixed training problem. Take \(\beta,s>0\).

For definiteness a sufficiently strong whole-test error metric is

\[
 \mathcal E=\left(\mathbb E_{\omega}\sup_{t\ge0}
   \|f_t-f_t^\star\|_{L^2(\mu)}^2\right)^{1/2},
\]

where \(f^\star\) is the specified canonical dense population predictor and \(\omega\) is initialization randomness. The calculations also apply to the weaker metric \(\sup_t\|f_t-f_t^\star\|_{L^2(\omega,\mu)}\), but the same metric must be used in both methods' guarantees.

## 1. Independent-block sampling

Suppose one proves

\[
 \mathcal E\le C\left(k^{-\beta}+q^{-s}
             +\frac{k^a q^b}{\sqrt B}\right). \tag{1}
\]

First take \(a,b\ge0\), the usual amplification case. Making the displayed upper bound at most \(\varepsilon\) requires, up to constants,

\[
 k\gtrsim\varepsilon^{-1/\beta},\qquad
 q\gtrsim\varepsilon^{-1/s},\qquad
 B\gtrsim\varepsilon^{-2}k^{2a}q^{2b}.
\]

The objective \(Bkq\) increases with each variable after substituting the minimum \(B\). Thus the certificate-optimal scales are

\[
 \begin{aligned}
 k&\asymp\varepsilon^{-1/\beta},&
 q&\asymp\varepsilon^{-1/s},\\
 B&\asymp\varepsilon^{-2-2a/\beta-2b/s},&
 n&\asymp\varepsilon^{-2-(1+2a)/\beta-2b/s}.
 \end{aligned} \tag{2}
\]

One chooses the multiplicative constants to assign, for example, error \(\varepsilon/3\) to each summand, then rounds up to integers. Consequently

\[
 S_{\rm learned}\asymp\varepsilon^{-p_B},\qquad
 p_B=2+\frac{1+2a}{\beta}+\frac{1+2b}{s}, \tag{3}
\]

while the fixed initialization at these learned-cost-optimal scales has exponent

\[
 S_{\rm fixed}\asymp\varepsilon^{-r_B},\qquad
 r_B=2+\frac{2+2a}{\beta}+\frac{2b}{s}. \tag{4}
\]

Against a conventional dense learned-state certificate \(O(\varepsilon^{-4})\), a strictly smaller power is certified exactly when

\[
 \frac{1+2a}{\beta}+\frac{1+2b}{s}<2. \tag{5}
\]

Equivalently, this requires \(s>(1+2b)/2\) and
\(\beta>(1+2a)/(2-(1+2b)/s)\). Equality gives the same power and says nothing about constant or logarithmic savings.

## 2. Sampling variance controlled by all coordinates

Suppose the stronger alternative is proved:

\[
 \mathcal E\le C\left(k^{-\beta}+q^{-s}
             +\frac{k^a q^b}{\sqrt n}\right),\qquad n=Bk. \tag{6}
\]

For \(a,b\ge0\), the necessary certificate constraints are

\[
 k\gtrsim\varepsilon^{-1/\beta},\quad
 q\gtrsim\varepsilon^{-1/s},\quad
 n\gtrsim\max\{k,\varepsilon^{-2}k^{2a}q^{2b}\}.
\]

The two terms in this maximum are nondecreasing in \(k,q\). Therefore the optimal \(k,q\) remain those in (2), and

\[
 \begin{aligned}
 h&=\max\left\{\frac1\beta,2+\frac{2a}{\beta}+\frac{2b}{s}\right\},\\
 n&\asymp\varepsilon^{-h},\qquad
 B\asymp\varepsilon^{-\max\{0,\,2+(2a-1)/\beta+2b/s\}},\\
 p_n&=h+\frac1s,\qquad r_n=h+\frac1\beta.
 \end{aligned} \tag{7}
\]

The \(n\ge k\) condition is essential: a formula predicting \(B<1\) must be replaced by the one-block boundary \(B\asymp1\). A strictly smaller learned-state power than four is certified exactly when **both**

\[
 \frac1\beta+\frac1s<4,
 \qquad
 \frac{2a}{\beta}+\frac{1+2b}{s}<2. \tag{8}
\]

The change from (1) to (6) needs an actual within-block covariance estimate. Independence between blocks alone does not provide it. For identically distributed independent block averages \(Z_b=k^{-1}\sum_{i=1}^k U_{bi}\),

\[
 \operatorname{Var}\!\left(\frac1B\sum_{b=1}^B Z_b\right)
 =\frac1{Bk^2}\sum_{i,j=1}^k
   \operatorname{Cov}(U_{1i},U_{1j}). \tag{9}
\]

Thus (6)'s sampling scale requires the relevant covariance sum to be \(O(k^{1+2a}q^{2b})\), rather than the generic \(O(k^{2+2a}q^{2b})\) consistent with (1). For vector or function-valued quantities, the corresponding second-moment inner products replace scalar covariances. Dependence created by the trained dynamics must also be handled; (9) cannot be applied by declaring trained blocks independent.

## 3. The requested rates

For \(s=2\) and \(a,b\ge0\), the precise comparisons are:

| Block bias rate | Sampling scale | Learned exponent | Strict improvement over 4 |
|---|---|---:|---|
| \(\beta=1\) | \(B^{-1/2}\) | \(7/2+2a+b\) | \(2a+b<1/2\) |
| \(\beta=1/2\) | \(B^{-1/2}\) | \(9/2+4a+b\) | impossible |
| \(\beta=1\) | \(n^{-1/2}\) | \(5/2+2a+b\) | \(2a+b<3/2\) |
| \(\beta=1/2\) | \(n^{-1/2}\) | \(5/2+4a+b\) | \(4a+b<3/2\) |

At \(a=b=0\), the full scales are:

| \((\beta,s)\) | Sampling scale | \(k\) | \(q\) | \(B\) | \(S_{\rm learned}\) | \(S_{\rm fixed}\) |
|---|---|---|---|---|---|---|
| \((1,2)\) | \(B^{-1/2}\) | \(\varepsilon^{-1}\) | \(\varepsilon^{-1/2}\) | \(\varepsilon^{-2}\) | \(\varepsilon^{-7/2}\) | \(\varepsilon^{-4}\) |
| \((1/2,2)\) | \(B^{-1/2}\) | \(\varepsilon^{-2}\) | \(\varepsilon^{-1/2}\) | \(\varepsilon^{-2}\) | \(\varepsilon^{-9/2}\) | \(\varepsilon^{-6}\) |
| \((1,2)\) | \(n^{-1/2}\) | \(\varepsilon^{-1}\) | \(\varepsilon^{-1/2}\) | \(\varepsilon^{-1}\) | \(\varepsilon^{-5/2}\) | \(\varepsilon^{-3}\) |
| \((1/2,2)\) | \(n^{-1/2}\) | \(\varepsilon^{-2}\) | \(\varepsilon^{-1/2}\) | \(1\) | \(\varepsilon^{-5/2}\) | \(\varepsilon^{-4}\) |

All table entries denote scales up to fixed multiplicative constants. In the last row the one-block architecture has dense-size fixed initialization; its proposed advantage concerns the stored learned update. In the first row learned state improves while total storage, if the initialization is stored explicitly, retains exponent four. Total explicit storage has exponent \(\max\{p,r\}\), so its improvement requires both exponents below four. No initialization regeneration scheme is assumed.

## 4. Exact exponent optimization without sign assumptions on \(a,b\)

For completeness, allow \(a,b\in\mathbb R\). Put
\(x_0=1/\beta\), \(y_0=1/s\), and set

\[
 (u,v)=\begin{cases}(2a,2b),&\text{bound (1)},\\
 (2a-1,2b),&\text{bound (6)}.
 \end{cases}
\]

Writing \(k\asymp\varepsilon^{-x}\), \(q\asymp\varepsilon^{-y}\), and \(B\asymp\varepsilon^{-z}\), the complete exponent problem is

\[
 \min\{x+y+z:x\ge x_0,\ y\ge y_0,\ z\ge0,
                       \ z\ge2+ux+vy\}. \tag{10}
\]

Its exact value is

\[
 p=x_0+y_0+
 \frac{[2+ux_0+vy_0]_+}{\max\{1,-u,-v\}}. \tag{11}
\]

To verify this, let \(h_0=2+ux_0+vy_0\) and write \(x=x_0+X,y=y_0+Y\), with \(X,Y\ge0\). If \(h_0\le0\), the corner already gives \(z=0\) and the smallest possible objective. If \(h_0>0\), spending \(D=X+Y\) can reduce \(h_0\) by at most \(M D\), where \(M=\max\{0,-u,-v\}\). Thus the objective is at least
\(x_0+y_0+D+\max\{0,h_0-MD\}\). For \(M\le1\) its minimum is attained at \(D=0,z=h_0\). For \(M>1\), spend \(D=h_0/M\) entirely on a coordinate whose coefficient is \(-M\); this attains \(z=0\) and gives (11). This also specifies optimal scales. Integer rounding changes constants only.

For \(a,b\ge0\), the denominator in (11) is one in both cases, recovering (3) and (7). For arbitrary signs, the strict dense comparison is simply \(p<4\) using (11); the positive-amplification thresholds must not be reused without checking the signs.

## 5. A sufficient bridge from kernel control to the actual test predictor

Training error or a training Gram-matrix bound alone does not imply whole-test prediction control. The following elementary lemma specifies one adequate bridge, including the quantities that must actually be estimated.

Assume the two prediction flows have exact representations

\[
 \dot f_t(x)=-\frac1m k_t(x)^T r_t,\qquad
 \dot f_t^\star(x)=-\frac1m k_t^\star(x)^T r_t^\star,
 \qquad r_t=f_t(X)-y.
\]

Here \(k_t(x)\in\mathbb R^m\) is the test-to-training kernel row, \(K_t\) is its training Gram matrix, and starred quantities correspond to the canonical population model. Set
\(e_t=r_t-r_t^\star\), \(\Delta k_t=k_t-k_t^\star\), and \(\Delta K_t=K_t-K_t^\star\). Direct subtraction gives the exact identities

\[
 \begin{aligned}
 f_t(x)-f_t^\star(x)
 &=f_0(x)-f_0^\star(x)
 -\int_0^t\frac{\Delta k_u(x)^Tr_u}{m}\,du
 -\int_0^t\frac{k_u^\star(x)^Te_u}{m}\,du,\\
 \dot e_t&=-\frac{K_t^\star}{m}e_t
                  -\frac{\Delta K_t}{m}r_t. \tag{12}
 \end{aligned}
\]

Assume \(K_t^\star/m\) is symmetric with smallest eigenvalue at least \(\lambda>0\), uniformly in time, and
\(\sup_t\|k_t^\star/m\|_{L^2(\mu;\mathbb R^m)}\le\kappa\).
Assume these constants are deterministic and that the following integrals are finite:

\[
 A=\int_0^\infty
 \|\Delta k_t^T r_t/m\|_{L^2(\omega,\mu)}\,dt,
 \qquad
 D=\int_0^\infty
 \|\Delta K_t r_t/m\|_{L^2(\omega;\mathbb R^m)}\,dt.
\]

Then

\[
 \mathcal E\le
 \|f_0-f_0^\star\|_{L^2(\omega,\mu)}+A
 +\frac\kappa\lambda
       \left(\|e_0\|_{L^2(\omega;\mathbb R^m)}+D\right). \tag{13}
\]

Indeed, the homogeneous evolution operator in (12) has norm at most
\(e^{-\lambda(t-u)}\): differentiating its solution's squared Euclidean norm proves this even when the time-dependent matrices do not commute. Variation of constants and integration of this exponential yield, pathwise,

\[
 \int_0^\infty\|e_t\|\,dt
 \le\lambda^{-1}\left(\|e_0\|
          +\int_0^\infty\|\Delta K_t r_t/m\|\,dt\right).
\]

Apply the triangle and Cauchy--Schwarz inequalities to the first line of (12), take the supremum in time, then use the integral triangle inequality in \(L^2(\omega)\). This proves (13), including the supremum inside the expectation.

For example, suppose initialization gives \(f_0=f_0^\star=0\), and one has the almost-sure residual bound
\(\|r_t\|\le R e^{-\gamma t}\), with \(\gamma>0\), together with

\[
 \sup_t\|\Delta K_t/m\|_{L^2(\omega;\mathrm{op})}\le\delta,
 \qquad
 \sup_t\|\Delta k_t/m\|_{L^2(\omega,\mu;\mathbb R^m)}\le\delta.
\]

Then \(A,D\le R\delta/\gamma\), so

\[
 \mathcal E\le\frac{R\delta}{\gamma}
                  \left(1+\frac\kappa\lambda\right). \tag{14}
\]

Thus a bound for \(\delta\) of the form in (1) or (6), together with uniform \(\lambda,\gamma,\kappa,R\), is a sufficient route to the requested predictor estimate. A small fixed label norm may supply \(R\), but any small-label assumption used to obtain the stability constants must be stated and proved. Separate RMS estimates of residual and kernel deviation cannot be multiplied without controlling their dependence; the almost-sure residual estimate above is one sufficient solution. If a memory algorithm's output evolution includes a truncation forcing beyond the displayed kernel law, that forcing must be added to (12) and its corresponding time integral bounded as well.

## 6. Exponential amplification and the scope of the comparison

If the available sampling term is
\(\exp(c\sqrt{k})/\sqrt B\) or \(\exp(c\sqrt{k})/\sqrt n\), with fixed \(c>0\), enforcing that particular certificate requires

\[
 B\ \text{or}\ n\ \gtrsim\varepsilon^{-2}
       \exp\!\left(c'\varepsilon^{-1/(2\beta)}\right), \tag{15}
\]

because the bias term already requires \(k\gtrsim\varepsilon^{-1/\beta}\). If the amplification is \(\exp(cq^2\sqrt{k})\), the corresponding requirement is

\[
 B\ \text{or}\ n\ \gtrsim\varepsilon^{-2}
       \exp\!\left(c'\varepsilon^{-(2/s+1/(2\beta))}\right). \tag{16}
\]

Here \(c'>0\) absorbs fixed constants, including the factor two from squaring the sampling constraint. Additional nonnegative polynomial amplification cannot improve these requirements. Thus these estimates do not certify any polynomial learned-state cost as \(\varepsilon\downarrow0\). A small but fixed positive \(c\) changes the crossover, not this asymptotic conclusion. Taking the labels or \(c\) to zero with \(\varepsilon\) changes the problem.

All optimality and impossibility statements above concern **making the stated upper bound at most the tolerance**. They are not lower bounds on the actual prediction error or on the best implementation. Failure of one estimate to certify a smaller cost leaves room for cancellations, sharper covariance or stability analysis, and a better algorithm. Likewise, a conventional dense \(O(\varepsilon^{-4})\) comparison means: a dense predictor has a proved error upper bound \(O(n_d^{-1/2})\) for this same target and metric, and its implementation stores \(\Theta(n_d^2)\) learned matrix entries. The choice \(n_d\asymp\varepsilon^{-2}\) then gives that sufficient cost. It does not establish an optimal dense complexity lower bound.

In particular, zero-readout initialization gives \(f_0=f_0^\star=0\) exactly at every width. There is no initial-output fluctuation from which to infer \(n\gtrsim\varepsilon^{-2}\). Any necessary width bound would need a separate nondegenerate trained-output lower bound. A fair favorable conclusion from (1) or (6) is therefore conditional and specific: once its all-time whole-test assumptions are proved, its optimized learned-state **upper bound** has a smaller exponent than the conventional dense certificate, with fixed initialization and computational work accounted for separately.
