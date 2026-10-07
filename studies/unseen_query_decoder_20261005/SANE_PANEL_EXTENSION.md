# Weak Gaussian source extension of the finite-panel route

2026-10-06. Scoped author derivation, not independent review or promotion.
No experiment, Git action, maintained-source edit, or other new route was
used. The full efficient unseen-query theorem remains open.

The useful new result is a scalar Gaussian-innovation lemma with an explicit
nonlinear mean correction and width-scale fluctuation bound. It explains
precisely what a weak replacement for the old vector-source construction
must integrate. A concrete admissible cosine network shows a nonvanishing
initial-velocity bias when the innovation is replaced by its mean before
the activation. The correction itself only requires one-dimensional
Gaussian convolution; its numerical evaluation has logarithmic complexity
under the original strip interface. The remaining row quadrature and
trained conditional-law obligations are stated separately below.

## Contract and relationship to the old construction

Keep the original width-n, depth-L network, iid Gaussian initialization,
zero stored readout, mean squared loss, and block mobilities
\((n,1,\ldots,1,n)\). Inputs have norm \(\sqrt d\), the m training
inputs span \(\mathbb R^d\), and their population top-feature Gram has
gap \(\gamma>0\). Keep the full original label allowance in the assigned
finite-panel result. Activations are analytic on the original strip with
bounded first and second derivatives; their values may be unbounded.
The target concerns the whole sphere at every physical time, including
the fitted endpoint, at the current independent-dense upper-certificate
scale. A matched near-\(1/n\) statement would be a separate stronger result.

The old training-only source has rank at most
\(3072m\chi^{-1}\log(en)^{5/2}+2m+d+1\), with \(\chi\) defined in
the assigned panel source. Its selected network has exponent-five real
storage and an autonomous nonlinear training rule. The old proof uses
coordinate approximation of query feature vectors to control initialized
matrix actions. Those query vectors are absent for an unseen input.
The following argument investigates scalar contraction after such an
action instead. It does not assume those vectors have small projection
error and does not replace nonlinear feature learning by a kernel flow.

The numerical and cost conventions remain those of COST_CONTRACT.md.
In particular a bound on real coordinates is not a finite-bit ODE solver
theorem, and activation/data evaluator time and precision must be charged.

## 1. Exact weak action of an unobserved Gaussian block

Let \(W\in\mathbb R^{n\times n}\) have iid \(N(0,1/n)\) entries.
For this lemma only, let \(U,V\subset\mathbb R^n\) be deterministic
subspaces, with Euclidean orthogonal projections \(P_U,P_V\). Observe
the two linear actions \(WP_V\) and \(P_UW\), and let \(\mathcal F\)
be the sigma field they generate. Define the observed matrix

\[
 M=WP_V+P_UW-P_UWP_V.
\tag{1}
\]

Let \(h,b\in\mathbb R^n\) be \(\mathcal F\)-measurable. Thus h and b
may depend on all observed entries, but not on the unobserved block. Set

\[
 z=Mh,\qquad \tau^2=\frac{\|(I-P_V)h\|_2^2}{n},\qquad
 X=\frac1n b^T\phi(Wh).
\tag{2}
\]

The activation acts coordinatewise. Suppose on the real axis
\(|\phi'|\le B_1\) and \(|\phi''|\le B_2\). Its linear growth makes
all conditional moments below finite for every realized finite h,b.
For real \(u\), variance \(v\ge0\), and a standard normal scalar Z,
define

\[
 \Psi_\phi(u,v)=\mathbb E\phi(u+\sqrt v Z).
\tag{3}
\]

Then the exact conditional mean is

\[
 \mathbb E[X\mid\mathcal F]
 =\frac1n\sum_{i=1}^n b_i
       \Psi_\phi\bigl(z_i,\tau^2[1-(P_U)_{ii}]\bigr).
\tag{4}
\]

Moreover, with \(g\sim N(0,I_n)\) independent of \(\mathcal F\),

\[
\begin{split}
 \operatorname{Var}(X\mid\mathcal F)
 &\le\frac{\pi^2\tau^2}{8n^2}
  \mathbb E\left[
   \|(I-P_U)\{b\odot\phi'(z+\tau(I-P_U)g)\}\|_2^2
       \mid\mathcal F\right]\\
 &\le\frac{\pi^2\tau^2 B_1^2\|b\|_2^2}{8n^2}.
\end{split}
\tag{5}
\]

For each \(0<\delta<1\), (5) gives conditional probability at least
\(1-\delta\) of

\[
 |X-\mathbb E[X\mid\mathcal F]|
 \le\frac{\pi\tau B_1}{\sqrt{8n\delta}}
                       \frac{\|b\|_2}{\sqrt n}.
\tag{6}
\]

Replacing the omitted block by zero instead has a possible systematic
bias bounded only by

\[
 \left|\mathbb E[X\mid\mathcal F]-\frac1n b^T\phi(z)\right|
 \le\frac{B_2\tau^2}{2n}
            \sum_i|b_i|[1-(P_U)_{ii}].
\tag{7}
\]

There is no width decay in (7) when \(\tau\) and the readout RMS stay
order one. By contrast (6) already has the target root-width fluctuation
for a single query without any small hidden-vector error.

**Proof.** Orthogonal changes of basis on the left and right turn W into
four independent rectangular Gaussian blocks. The observations determine
three of them. The fourth has the same iid law as its unconditional law.
Consequently, conditionally on \(\mathcal F\),

\[
 W\ \stackrel{\rm law}=\ M+
           (I-P_U)G(I-P_V)/\sqrt n,
\tag{8}
\]

where G has iid standard normal entries independent of \(\mathcal F\).
This also follows directly by computing the zero cross-covariances of
the four Gaussian blocks. Given h, the vector
\(G(I-P_V)h/\sqrt n\) has independent coordinates with variance
\(\tau^2\). Thus the residual preactivation has law
\(\tau(I-P_U)g\). Its ith marginal variance is
\(\tau^2[1-(P_U)_{ii}]\), proving (4); independence across i is
neither asserted nor needed.

Here is an elementary variance inequality sufficient for (5). For a
continuously differentiable Lipschitz function F of a standard Gaussian
vector g, take an independent copy \(g'\), and set
\(g_\theta=g\cos\theta+g'\sin\theta\) for
\(0\le\theta\le\pi/2\). Its derivative
\(-g\sin\theta+g'\cos\theta\) is standard Gaussian independent
of \(g_\theta\), as follows by zero covariance and joint Gaussianity.
The fundamental theorem of calculus and Cauchy--Schwarz imply

\[
\begin{split}
 2\operatorname{Var}F(g)
 &=\mathbb E|F(g)-F(g')|^2\\
 &\le\frac\pi2\int_0^{\pi/2}
        \mathbb E\|\nabla F(g_\theta)\|_2^2\,d\theta
 =\frac{\pi^2}{4}\mathbb E\|\nabla F(g)\|_2^2.
\end{split}
\]

Apply this conditionally to
\(F(g)=b^T\phi(z+\tau(I-P_U)g)/n\). Its gradient is the vector
inside (5), multiplied by \(\tau/n\). Orthogonal projection is a
contraction and \(|\phi'|\le B_1\), proving (5). Chebyshev gives
(6). Finally Taylor's formula with integral remainder gives
\(|\phi(u+e)-\phi(u)-e\phi'(u)|\le B_2e^2/2\).
Each Gaussian residual coordinate is centered, so averaging and summing
against \(|b_i|/n\) proves (7).

Checks: when h belongs to V, \(\tau=0\) and the error is exactly zero.
When \(\phi(u)=a+cu\) and b belongs to U, the sharper first line of
(5) is zero, as required by the observed reverse action. For cosine,
\(\Psi_\phi(u,v)=e^{-v/2}\cos u\), exposing a nontrivial mean
correction even with perfect linear source matching. Unbounded affine
plus cosine activations satisfy the same lemma.

The lemma also holds after conditioning on independent randomness that
determines U,V. It has **not** been asserted for arbitrary source spaces
chosen using W itself. Adaptively generated training spaces require an
appropriate Gaussian transcript argument; arbitrary full-trajectory
selection is not licensed by (8). Nor does a pointwise Chebyshev bound
imply a uniform sphere/time estimate by itself.

## 2. A width-asymptotic bias within the admissible model

Take \(L=d=m=2\), normalized training inputs \(v_1=e_1,v_2=e_2\),
query \(v=(e_1+e_2)/\sqrt2\), and both activations cosine. Let
\(A=W^{(1)}(0)\), \(B=W^{(2)}(0)\), and define first-layer vectors

\[
 h_a=\cos(Av_a),\quad h=\cos(Av),\quad
 H=[h_1\ h_2],\quad P=H(H^TH)^{-1}H^T.
\]

On the event of invertibility put \(u=Ph\),
\(\rho_n^2=\|(I-P)h\|_2^2/n\). The event has probability tending
to one; any bounded fallback on its complement has no effect on the
limits below. Consider the full dense initial top-feature overlap and
the more informative oracle projected-action overlap

\[
 K_n=\frac1n\cos(Bh_1)^T\cos(Bh),\qquad
 K_n^{\rm proj}=\frac1n\cos(Bh_1)^T\cos(Bu).
\tag{9}
\]

The second expression is an obstruction witness, not an implementation:
it is granted the exact dense projection and all exact training actions.
Conditioning on A and BH, the omitted vector \(B(h-u)\) has iid
\(N(0,\rho_n^2)\) entries independent of BH. Therefore

\[
 \mathbb E[K_n\mid A,BH]=e^{-\rho_n^2/2}K_n^{\rm proj},\qquad
 \operatorname{Var}(K_n\mid A,BH)\le1/n.
\tag{10}
\]

This is (4) with U zero and V the span of H, applied with
\(b=\cos(Bh_1)\). The variance bound also follows immediately
from the independent bounded residual row contributions.

Define the explicit constants

\[
 q=\frac{1+e^{-2}}2,\quad c=e^{-1},\quad
 b_0=e^{-1}\cosh(1/\sqrt2),\quad
 p=\frac{2b_0^2}{q+c},\quad \rho^2=q-p.
\tag{11}
\]

Then \(\rho^2>0\). Indeed, the Gaussian L2 projection of
\(\cos((g_1+g_2)/\sqrt2)\) onto
\(\operatorname{span}\{\cos g_1,\cos g_2\}\) has the squared
residual q-p. If that residual were zero, positive Gaussian density and
continuity would give the corresponding functional identity everywhere.
At \(g_2=0\), its second and fourth derivatives in \(g_1\) at zero
would require the coefficient of \(\cos g_1\) to equal both 1/2
and 1/4. This is impossible. The training Gram is invertible because
\(q-c=(1-e^{-1})^2/2>0\).

All first-layer empirical moments converge in probability to their
expectations: each is an average of bounded iid variables, whose variance
is at most \(1/n\). Gaussian cosine multiplication gives (11), and
continuity of matrix inversion therefore gives
\(\rho_n^2\to\rho^2\), \(\|u\|_2^2/n\to p\), and
\(h_1^Tu/n\to b_0\). Conditional on A, the rows of
\((Bh_1,Bu)\) are iid centered Gaussian pairs. Their cosine-product
mean is

\[
 \exp\left[-\frac{\|h_1\|_2^2+\|u\|_2^2}{2n}\right]
             \cosh(h_1^Tu/n),
\]

obtained from the two cosine addition identities and
\(\mathbb E\cos Z=e^{-\operatorname{Var}Z/2}\).
Conditional variance is at most \(1/n\). Equations (10)--(11) now give

\[
 K_n^{\rm proj}-K_n
 \ \longrightarrow\
 e^{-(q+p)/2}\cosh(b_0)(1-e^{-\rho^2/2})>0
 \quad\hbox{in probability}.
\tag{12}
\]

With labels \(y=(\varepsilon,0)\), zero readout and the specified
mobility give exactly \(\partial_t f_n(0,v)=\varepsilon K_n\).
Thus the projected-action replacement has the strictly positive limiting
initial-velocity bias \(\varepsilon\) times (12). Choose any fixed
positive \(\varepsilon\) small enough for the full original label
allowance. The top population training Gram has diagonal
\(e^{-q}\cosh q\) and off-diagonal \(e^{-q}\cosh c\), hence
\(\gamma=e^{-q}(\cosh q-\cosh c)>0\). This is an admissible model,
with a true nondegenerate Gaussian law, not an exceptional finite-width
configuration.

This strengthens the supplied local projection example to a probability
limit for an actual initialized nonlinear network. Its exact scope is
still limited: it defeats omission of the nonlinear conditional-mean
correction at initial velocity. It is not a lower bound on all selected
networks or decoders, and a velocity mismatch alone is not an all-time
prediction-error lower bound without additional time-uniform estimates.
Multiplying \(K_n^{\rm proj}\) by \(e^{-\rho_n^2/2}\) repairs this
particular conditional bias exactly, by (10).

## 3. One-dimensional smoothing has a short numerical rule

The smoothing primitive in (4) does not require a high-dimensional
Gaussian integral. The following explicit scalar construction handles
unbounded activation values. Suppose \(\phi\) is holomorphic on
\(|\operatorname{Im}w|<a\), real on the real axis, and
\(|\phi'|\le B\) on \(|\operatorname{Im}w|\le a/2\).
For real z and \(\sigma>0\), let

\[
 s=\min\{1,a/(2\sigma)\},\quad
 C_0=1+|\phi(0)|+B(|z|+\sigma),\quad
 D=\log(128C_0/\epsilon),
\]

where \(0<\epsilon\le1\). Set
\(h=s/D\), \(R=4\sqrt D\), \(J=\lceil R/h\rceil\). Then

\[
 Q=\frac h{\sqrt{2\pi}}\sum_{k=-J}^{J}
              e^{-(kh)^2/2}\phi(z+\sigma kh)
\tag{13}
\]

satisfies \(|Q-\Psi_\phi(z,\sigma^2)|\le\epsilon\), and uses at
most \(8D^{3/2}/s+3\) activation calls and constant scalar workspace,
apart from the activation evaluator and counted precision.

To verify the error, put
\(F(w)=e^{-w^2/2}\phi(z+\sigma w)/\sqrt{2\pi}\).
Integrating the derivative bound along a straight path inside the strip
gives linear growth for \(\phi\). On either line
\(\operatorname{Im}w=\pm s\), direct Gaussian integration gives
\(\int_{\mathbb R}|F(u\pm is)|du\le4C_0\).
Moving the Fourier integral to the appropriate line therefore gives
\(|\widehat F(\xi)|\le4C_0e^{-s|\xi|}\), with transform
\(\widehat F(\xi)=\int F(u)e^{-i\xi u}du\). The vertical contour
sides vanish by Gaussian decay and linear growth. Periodize F with
period h; its Fourier coefficients are
\(h^{-1}\widehat F(2\pi l/h)\). Gaussian decay makes the
periodization convergent and the displayed coefficient bound makes its
Fourier series absolutely convergent. Evaluating that series at zero
proves the trapezoid identity and bounds the infinite-rule error by

\[
 8C_0\frac{e^{-2\pi s/h}}{1-e^{-2\pi s/h}}
 \le16C_0e^{-2\pi D}<\epsilon/4.
\]

On the real line \(|F(u)|\le C_0(1+|u|)e^{-u^2/2}\).
For \(u\ge R\ge2\) this upper envelope decreases. Since \(Jh\ge R\),
the deleted two tails have total weight at most
\(2C_0\int_R^\infty(1+u)e^{-u^2/2}du
 \le4C_0e^{-R^2/2}<\epsilon/4\).
These inequalities prove the exact-arithmetic claim with slack for
numerical evaluation. For \(\sigma=0\), evaluate \(\phi(z)\) directly.

For numerical evaluation, the sum of the absolute nonnegative weights in
(13) is less than two: monotonicity on each half-line bounds it by
\(1+h/\sqrt{2\pi}<2\). Thus activation errors at most
\(\epsilon/8\) contribute at most \(\epsilon/4\).
Errors in Gaussian weights and summation require an additional
\(O(\log(J+1)+\log(C_0(1+R))+\log(1/\epsilon))\) bits of
working precision, with a sufficiently large universal coefficient;
one can instead allocate absolute error \(\epsilon/[16(J+1)]\)
to each weighted summand and its addition. Argument construction must
ensure \(B\) times its error fits the same summand allowance.
Actual activation/data/equivalent exponential evaluation costs are charged
at that precision. This is not a theorem that arbitrary analytic
activations admit a fast evaluator.

When bounded-argument and variance envelopes are polynomial in
\(\beta^L,m,1+m/\gamma\) and \(\log n\), \(s^{-1}\) displays the
entire strip/variance dependence, and D is logarithmic in these bounds
and \(\epsilon^{-1}\). There is no hidden exponential dependence on d.
For \(\epsilon\) a negative power of n and bounded \(s^{-1}\), each
scalar convolution costs \(O(\log(n)^{3/2})\) calls. Applying it at
\(O(\log(n)^{5/2})\) already selected rows would cost
\(O(\log(n)^4)\) calls, **if** the row selection supplied the needed
uniform weak quadrature. The latter italicized hypothesis is not supplied
by the finite-panel source theorem.

## 4. Arbitrary-coefficient selected-row quadrature can still require many nodes

The following elementary obstruction directly tests the proposed shortcut
"the gate has been Gaussian-smoothed, so old selected rows should suffice."
It concerns a generic row family, not a trained Gaussian-network lower bound.

Let \(r\ge2\), let row signatures range over
\(a\in\{-1,1\}^r\), and fix \(\sigma\ge0\). The target smoothed
row average, for a coefficient vector \(c\in\mathbb R^r\), is

\[
 F(c)=2^{-r}\sum_{a\in\{-1,1\}^r}
        \Psi_{\cos}(a^Tc,\sigma^2)
     =e^{-\sigma^2/2}2^{-r}\sum_a\cos(a^Tc).
\tag{14}
\]

Choose any q rows \(a_1,\ldots,a_q\), with arbitrary signed real weights
\(w_j\) satisfying \(\sum_jw_j=1\). Suppose their selected-row rule
approximates (14) with absolute error at most \(\epsilon\), uniformly
even on the finite coefficient subset

\[
 c_S=(\pi/2)\mathbf1_S,\qquad S\subset\{1,\ldots,r\},\quad
 |S|\ \hbox{even}.
\]

Every such vector has norm at most \((\pi/2)\sqrt r\). With
\(N=2^{r-1}\), necessarily

\[
 q\ \ge\ \frac{N}{1+(N-1)e^{\sigma^2}\epsilon^2}.
\tag{15}
\]

This allows arbitrary signed weights and row choices, so it applies in
particular to positive quadrature. It also covers a non-diagonal metric
used for a fixed constant dual vector: \(\mathbf1^TM\Psi\) is a signed
row rule with weights \(M\mathbf1\), and exact constant isometry gives
the required sum of weights.

**Proof.** For even S, elementary multiplication of
\(e^{i\pi a_k/2}=ia_k\) gives

\[
 \cos(a^Tc_S)=(-1)^{|S|/2}\prod_{k\in S}a_k.
\]

The even products are constant on antipodal pairs \(\{a,-a\}\).
There are N such pairs and N even subsets S. On these pairs the products
are orthogonal: the sum of a product of distinct even characters is zero,
because flipping any coordinate in their nonempty symmetric difference
cancels it; the sum for identical characters is N. Merge all selected
weights on each antipodal pair to form a vector \(p\in\mathbb R^N\).
It has at most q nonzero entries and \(\sum p_i=1\), hence
\(\sum p_i^2\ge1/q\) by Cauchy--Schwarz. Orthogonality gives

\[
 \sum_{S\ {m even}}\left(\sum_i p_i\prod_{k\in S}(a_i)_k\right)^2
   =N\sum_i p_i^2.
\]

The empty character is exactly one. The true uniform average of every
nonempty character is zero. Each of the remaining N-1 character errors
has magnitude at most \(e^{\sigma^2/2}\epsilon\) by the quadrature
hypothesis. Therefore
\(N/q\le N\sum_i p_i^2\le1+(N-1)e^{\sigma^2}\epsilon^2\),
which proves (15).

At fixed \(\sigma\), when N greatly exceeds \(\epsilon^{-2}\),
the node requirement is of order \(\epsilon^{-2}\). At fixed r,
letting \(\epsilon\) tend to zero instead forces q toward
\(2^{r-1}\), an exponential row count. Smoothing only multiplies every
member of this particular family by the same constant, so it removes
neither obstruction. These statements do not rely on probabilistic
subsampling or on exactness for all polynomials.

This does **not** prove that such row signatures or coefficient families
occur in the original trained Gaussian network. The source-derived query
coefficients occupy a constrained set generated by the actual preceding
layers, not necessarily all vectors in the displayed ball. Also, allowing
\(\sigma\) to grow with accuracy can suppress this family; (15) exposes
that dependence explicitly. Thus the result rejects a generic arbitrary-
coefficient quadrature theorem from smoothing and source rank alone. A
successful old-node extension must exploit the actual reachable row/query
family or a representation other than selected empirical rows.

## 5. The precise next branch and surviving obstructions

The concrete candidate to investigate next is a selected-row runtime whose
passive forward gates are variance-corrected by (3), with reverse-action
leverage factors \(1-(P_U)_{ii}\) where a valid conditioning transcript
requires them. Equations (4)--(7) suggest how it could preserve scalar
accuracy even when query feature-vector approximation fails. No such
runtime is asserted to follow the original trained model here.

Two distinct estimates are now necessary.

1. A trained, adaptive Gaussian-action representation must justify the
   conditional mean and covariance used at each unseen-query layer,
   accounting for the same matrices' forward and transpose uses.
   The passive preceding-layer feature is generally not measurable in
   the training transcript alone, so iterating (4) naively is invalid.
2. One must compress the actual family of smoothed weighted row averages
   in (4) uniformly over the whole sphere and physical time. The old
   isometry preserves products of retained source vectors, whereas (4)
   is a new nonlinear family. Generic random selection adds root-selected-
   width noise, and universal moment cubature has the dimension-dependent
   count proved in the assigned compilation note. Neither is repaired
   merely by the cheap scalar convolution (13). The new signed-rule bound
   (15) additionally rules out a generic arbitrary-coefficient theorem
   even for the explicitly Gaussian-smoothed cosine family.

This is narrower than asking for an unspecified small query circuit:
the proposed observable is explicit, its Gaussian mean is exact under
stated conditioning, its pointwise statistical error is quantified, and
its one-dimensional numerical integration is costed. A successful next
lemma should give a weak quadrature bound for these *specific smoothed
row integrands*, or identify a training invariant reducing them to the
old paired source algebra. It must not assume a global population theorem,
replay history, retain a dense row array, or store future query outputs.

The exponent-five target is therefore still open. The full-label condition
is preserved in the target and admissible example, not tightened to force
a perturbation series. The scalar lemmas impose no extra label cap. No
all-time uniformity, endpoint accuracy, matched near-\(1/n\) accuracy,
or complete numerical-training theorem follows from them. In particular,
(6)'s root-width stochastic term would by itself be too large for the
stronger matched near-\(1/n\) objective.

| Claim | Status and exact scope |
|---|---|
| Conditional Gaussian scalar mean (4) | Exact for deterministic/independently fixed action spaces and measurable query/readout |
| Weak fluctuation bound (5)--(6) | Proved pointwise, with universal constants |
| Nonvanishing projected-query bias (12) | Proved in probability at initial velocity in the specified admissible depth-two example |
| Scalar smoothing quadrature (13) | Proved with explicit strip, argument, precision and evaluator costs |
| Smoothed arbitrary-coefficient row quadrature (15) | Proved representation-specific node lower bound; not an original-network lower bound |
| Old selected rows integrate the new mean family | Open; not implied by source isometry |
| Iterated trained whole-sphere decoder | Open; adaptive conditioning and weak quadrature both needed |

Recommended registry status: bounded first result complete; retain the weak
Gaussian-mean route only if the next pass attacks the specific smoothed row
quadrature or adaptive measurability question. Repeating training-source
rank counting without either new ingredient will not resolve it.

## Input coverage and provenance

Read completely: both assigned finite-panel files; COST_CONTRACT.md,
UNIFORM_SOURCE_DECODER.md, COMPARISON_DECODER.md and
EFFICIENT_QUERY_COMPILATION.md in this study; maintained docs/index.qmd and
docs/notation.qmd. No linked integrated proof was needed for the elementary
new arguments, and none was opened. The inherited panel theorem is used
only as the stated construction interface, not independently reverified.
Required investigate-conjectures and solve-math-rigorously skills and the
research-contract, evidence-ledger, adversarial-audit and proof-search
references were read. The custom canonical-notation skill returned
Permission denied; its neural-network reference was consequently unavailable.
The assignment's explicit fallback and maintained notation were applied.

Input SHA-256 hashes at the read boundary:

```text
38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b  finite_panel_absolute_compression_20261005/RESULT.md
ca1066cf168829bea642db013a4fbc24166b224df0731783a51b4c85e4fdbaed  finite_panel_absolute_compression_20261005/PANEL_SOURCE.md
3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c  COST_CONTRACT.md
9984361c2142fe2747c6f8502a1e86d796b71ed5bd4221d95f8c50d5fd694bc7  UNIFORM_SOURCE_DECODER.md
03205ac63acea20e10908d318512c78e88d7c627988903ff529d106753f52cb8  COMPARISON_DECODER.md
9ea7bf2bdfc88a25052c5e5638dd343df8513326402dedc7cb9d1d2b64ba54a3  EFFICIENT_QUERY_COMPILATION.md
f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de  docs/index.qmd
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
```

The new statements are author derived and self-audited algebraically; they
have not received independent complete review. No experiment or external
theorem retrieval was required: the conditioning, variance estimate,
Gaussian cosine identities and scalar quadrature bound are proved above.
