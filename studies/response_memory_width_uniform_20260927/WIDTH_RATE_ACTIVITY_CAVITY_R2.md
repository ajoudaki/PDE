# Activity cavity, round 2: weak Gaussian gate returns

28 September 2026. Scoped theoretical continuation. Inputs were the four
assigned files `ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`,
`ACTIVATION_GAUSSIAN_ALLTIME.md`, `QUANTITATIVE_WIDTH_CAVITY.md`, and
`QUANTITATIVE_WIDTH_SENSITIVITY.md`, read completely. The rigorous-math
and conjecture-investigation skills were applied. No other research
input, external source, experiment, agent, Git operation, or maintained
manuscript change was used. This file is the only output.

**Result.** A nonlinear Gaussian return can be concentrated at root width
without Taylor expanding its Jacobian. This proves a weak replacement
for the problematic gate step and closes scalar, fixed-matrix, and
continuum Hilbert-history feedback models at root width under exactly
the stated activation regularity. The history theorem is uniform over
a full Hilbert ball and has no time-node or message-dimension loss.
There is also a sharper obstruction: even with independent,
nondegenerate Gaussian base preactivations, the Euclidean first-order
gate remainder can converge more slowly than every power of width for
one fixed admissible activation. Thus Gaussian averaging does not repair
the strong remainder required by the earlier expansion (22).

These results do **not** complete the actual deep-network cavity law.
In particular, no all-time finite-width predictor exponent or
`epsilon^(-5/2+o(1))` moving-state theorem is claimed. The new results
identify a valid weak route and rule out a stronger intermediate claim;
they are not a counterexample to the desired network theorem.

## 1. Contract and the regularity issue

The target remains actual canonical dense GF with fixed depth/data,
Gaussian initialized hidden matrices reused in forward and transpose
calls, exactly zero readout, fixed small positive label norm, positive
limiting initial readout-feature Gram, and globally bounded
`phi'` with globally Lipschitz `phi'`. The comparison target is the
assigned strong population GF, uniformly over the whole physical
half-line. Neither trained Gaussian independence nor history covariance
nondegeneracy is assumed.

Write `psi=phi'`; its weak derivative `psi'=phi''` exists almost
everywhere and is bounded by `j`. The earlier tangent expansion needs a
small Euclidean norm for

\[
 e_j=\psi(z_j+u_j)-\psi(z_j)-\psi'(z_j)u_j,
 \qquad u_j\asymp n^{-1/2}.
 \tag{1}
\]

Lipschitz continuity of `psi` gives only `|e_j|<=2j|u_j|`.
Section 4 proves that even Gaussian averaging does not, in general,
improve the Euclidean norm in (1) to any fixed polynomial rate. Sections
2--3 instead retain the complete nonlinear map inside the returned
scalar observable.

## 2. A nonlinear Gaussian return lemma needing one weak derivative

Condition on a cavity sigma-field. Let `g` be an independent standard
Gaussian vector in `R^n`. Let `H:R^n -> R^n` be a cavity-measurable
Lipschitz map satisfying

\[
 H(0)=0,\qquad
 \|DH(g)\|_{\mathrm{op}}\le K/\sqrt n
 \quad\text{almost everywhere}.
 \tag{2}
\]

Define

\[
 R(g)=\frac{g^TH(g)}{\sqrt n},\qquad
 \mu=\mathbb E_g R(g).
\]

Then, for every `p>=2`,

\[
 \|R-\mu\|_{L^p(g)}
 \le CK\left(\sqrt{p/n}+p/n\right),\qquad
 \mu=\frac1{\sqrt n}\mathbb E_g\operatorname{tr}DH(g).
 \tag{3}
\]

The mean is the exact nonlinear response. It is not replaced by the
Jacobian at zero.

To prove (3), Lipschitz continuity and (2) give
`||H(g)||<=K||g||/sqrt(n)`. The weak gradient of the scalar return is

\[
 \nabla R(g)=\frac{H(g)+DH(g)^Tg}{\sqrt n},\qquad
 \|\nabla R(g)\|\le 2K\|g\|/n.
 \tag{4}
\]

For completeness, the Gaussian gradient moment inequality needed here
has a short proof. If `G,G'` are independent standard Gaussians, rotate
them through
`X_theta=G cos(theta)+G' sin(theta)` and
`Y_theta=-G sin(theta)+G' cos(theta)`. At each angle these two vectors
are independent standard Gaussians. Conditional Jensen, the fundamental
theorem along the rotation, and Minkowski imply

\[
 \|F(G)-\mathbb EF(G)\|_p
 \le\int_0^{\pi/2}
       \|\nabla F(X_\theta)^TY_\theta\|_p\,d\theta
 \le C\sqrt p\,\|\nabla F(G)\|_p.
 \tag{5}
\]

Approximation gives (5) for locally Lipschitz functions with the displayed
integrable gradient. The chi-square moment bound
`|| ||G|| ||_p<=sqrt(n)+C sqrt(p)`, obtained from the product Gaussian
moment-generating function, combines with (4)--(5) to prove the first
claim. Gaussian integration by parts in each coordinate proves the
second. All terms are integrable by (2), so truncation and mollification
justify this identity for weak derivatives.

For a deterministic cavity vector `z`, a cavity matrix `A` of operator
norm at most `A_0`, and a scalar `b`, this applies to

\[
 H_b(g)=\psi(z+bAg/\sqrt n)-\psi(z),\qquad
 K=j|b|A_0.
 \tag{6}
\]

Thus the returned **gate**, not just the activation, has root-width
fluctuations. This estimate involves no derivative of `phi''`.

### Uniformity over an adaptive scalar

For `A=I` and `b=epsilon q`, fix `|q|<=Q`. The exact return and mean obey

\[
 |R_q(g)-R_{q'}(g)|
   \le j\epsilon|q-q'|\|g\|^2/n,
 \qquad |\mu_q-\mu_{q'}|\le j\epsilon|q-q'|.
 \tag{7}
\]

A grid of spacing `Q/n` has at most `2n+2` points. Apply (3) and
Markov's inequality at moment order `p=C(u+log(e+n))` at each point,
then use (7) on `||g||^2/n<=2`. For `u>=1`, with failure probability
at most `C exp(-u)+C exp(-cn)`,

\[
 \sup_{|q|\le Q}|R_q-\mu_q|
 \le Cj\epsilon Q
 \left[\sqrt{\frac{u+\log(e+n)}n}
       +\frac{u+\log(e+n)}n\right].
 \tag{8}
\]

Consequently (8) remains valid after choosing `q` adaptively from `g`.
The price is a logarithm, not differentiability of that adaptive choice.

## 3. A complete Gaussian-base scalar gate-feedback theorem

Let `Z_1,...,Z_n` be independent `N(0,sigma^2)` variables, with fixed
`sigma>0`, and independent of `g`. Let `h` be measurable with respect
to the `Z` variables and any additional cavity randomness, with
`||h||/sqrt(n)<=B`. Set

\[
 \zeta=g^Th/\sqrt n,\qquad
 d=\mathbb E\psi'(\sigma G),\qquad
 0\le\epsilon j\le1/4.
\]

On `E={||g||^2/n<=2}`, consider the exact equation

\[
 q=\zeta+
 \frac1{\sqrt n}\sum_i g_i
 \left[\psi\!\left(Z_i+\frac{\epsilon qg_i}{\sqrt n}\right)
                       -\psi(Z_i)\right].
 \tag{9}
\]

It has a unique solution, `|q|<=2|zeta|`, since the second term is
globally Lipschitz in `q` with constant at most `2 epsilon j<=1/2`
and vanishes at zero. In particular the solution has Gaussian tails
on `E`; conditioning on the cavity gives
`Pr(|q|>2B sqrt(2u),E)<=2 exp(-u)`.

The population-response solution is

\[
 q_* = \frac{\zeta}{1-\epsilon d}.
 \tag{10}
\]

For each fixed `D>0`, there is `C_D` such that, with probability at least
`1-C_D n^{-D}-C exp(-cn)`,

\[
 |q-q_*|
 \le C_D j\epsilon B\frac{\log(e+n)}{\sqrt n}
 +C_D j\epsilon^3B^3
              \frac{\log(e+n)^{3/2}}{n\sigma^2}.
 \tag{11}
\]

Here and in this statement the harmless constants may also absorb the
case of small `n`; `B=0` or `epsilon j=0` gives an exact zero error.

**Proof of the response identification.** For fixed `Z`, Gaussian
integration by parts only in the independent `g_i` gives the exact mean

\[
 \mu_n(q)=\frac{\epsilon q}{n}\sum_i
     \mathbb E_G\psi'\!\left(Z_i+
                          \frac{\epsilon qG}{\sqrt n}\right).
 \tag{12}
\]

No pointwise value of `psi'` at an exceptional nondifferentiability point
is relevant. Alternatively (12) is first proved after mollification and
then follows from the nondegenerate Gaussian densities when `q!=0`;
at `q=0` both sides are zero.

Each summand before empirical averaging has magnitude at most
`j epsilon Q` on `|q|<=Q`. As a function of `q`, both the empirical mean
and its expectation have Lipschitz constant at most `j epsilon`, by the
left side of (12), before integration by parts. Hoeffding's exponential
bound for independent bounded centered summands and the same `Q/n` grid
therefore give, with probability at least `1-C exp(-u)`,

\[
 \sup_{|q|\le Q}|\mu_n(q)-\mathbb E_Z\mu_n(q)|
 \le Cj\epsilon Q\sqrt{\frac{u+\log(e+n)}n}
       +Cj\epsilon Q/n.
 \tag{13}
\]

The required Hoeffding bound follows by the elementary estimate
`E exp(t(X-EX))<=exp(t^2(b-a)^2/8)` for a variable in `[a,b]`,
then multiplication over independent summands and optimization in `t`.

Put `v=sigma^2` and `h_q=epsilon q/sqrt(n)`. Averaging (12) over `Z`
produces

\[
 \mathbb E_Z\mu_n(q)
   =\epsilon q\,\mathbb E\psi'(\sqrt{v+h_q^2}\,G).
 \tag{14}
\]

For the one-dimensional centered Gaussian density `p_v`,

\[
 \|\partial_v p_v\|_1
 =\frac1{2v}\mathbb E|G^2-1|\le1/v.
\]

Since `|psi'|<=j`, integrate this density derivative between `v` and
`v+h_q^2` to obtain

\[
 |\mathbb E_Z\mu_n(q)-\epsilon qd|
 \le j\epsilon|q|\,h_q^2/\sigma^2
 \le \frac{j\epsilon^3Q^3}{n\sigma^2}.
 \tag{15}
\]

This is weak Gaussian smoothing of a bounded measurable second
activation derivative. It needs neither its continuity nor a third
derivative. Combine (8), (13), and (15). On `|q|<=Q`, the exact identity

\[
 (1-\epsilon d)(q-q_*)=R_q-\epsilon dq
\]

and `1-epsilon d>=3/4` finish the comparison. Take
`Q=C_D B sqrt(log(e+n))` and use the already proved Gaussian bound on
the actual solution of (9). This proves (11), including its stop and
adaptive-feedback control.

This is a complete weak gate-return calculation. It extends the earlier
scalar forward-activation return calculation to the precise regularity
class which blocked the gate Taylor expansion.

### A reused matrix and a fixed block of adaptive messages

The same proof treats a nontrivial simultaneous forward/transpose return.
Fix integers `r,b` independently of `n`. Let `G` be an `n` by `r`
standard Gaussian matrix. Let the rows of the `n` by `b` matrix `Z` be
independent copies of a centered Gaussian vector of covariance `Sigma`,
independent of `G`. The covariance may be singular; assume only
`Sigma_aa=sigma_a^2>0` for each used column. Let `Psi` act separately
on columns by scalar functions `psi_a` with Lipschitz constants at most
`j`. Both `phi` and `phi'` qualify as such functions under the assigned
activation assumptions. Let `H` be cavity-measurable with
`||H||F/sqrt(n)<=B`, and set `Zeta=G^TH/sqrt(n)`.

For `Q` of shape `r` by `b`, define the exact reused-matrix feedback

\[
 Q=\mathsf Zeta+\mathcal R_G(Q),\qquad
 \mathcal R_G(Q)=\frac{G^T}{\sqrt n}
 \left[\Psi\!\left(Z+\frac{\epsilon GQ}{\sqrt n}\right)
                                      -\Psi(Z)\right].
 \tag{11a}
\]

On `||G||op^2/n<=2`, this map has Lipschitz constant at most
`2 epsilon j` in Frobenius norm. If `epsilon j<=1/4`, it has a unique
solution with `||Q||F<=2||Zeta||F`. The latter is a fixed-dimensional
Gaussian norm conditional on the cavity, with a tail bounded by
`C exp(-u)` at `C B sqrt(u+1)`. A fixed sphere net and the scalar
chi-square tail prove that the matrix norm event fails with probability
at most `C_r exp(-c_r n)`.

Put

\[
 D_{aa}=\mathbb E\psi_a'(Z_{1a}),\qquad
 Q_* =\mathsf Zeta(I-\epsilon D)^{-1},\qquad
 \sigma_{\min}=\min_a\sigma_a.
 \tag{11b}
\]

Then for each fixed `D_0>0`, with probability at least
`1-C n^{-D_0}-C exp(-cn)`,

\[
 \|Q-Q_*\|_F
 \le Cj\epsilon B\frac{\log(e+n)}{\sqrt n}
   +Cj\epsilon^3B^3
            \frac{\log(e+n)^{3/2}}{n\sigma_{\min}^2},
 \tag{11c}
\]

where constants may depend on the fixed block dimensions and `D_0`.

Here are the details that differ from the scalar proof. Conditional
Gaussian integration by parts yields

\[
 (\mathbb E_G\mathcal R_G(Q))_{ka}
 =\frac{\epsilon Q_{ka}}n\sum_i
    \mathbb E_N\psi_a'\!\left(Z_{ia}
                 +\frac{\epsilon\|Q_{\cdot a}\|_2N}{\sqrt n}\right).
 \tag{11d}
\]

Each scalar returned entry has Gaussian gradient bounded by
`C epsilon j ||Q||F ||G||F/n`. The rotation proof (5), now in
dimension `nr`, gives its centered root-width estimate with constants
depending on `r`. Each one-row contribution to the conditional mean in
(11d), before using integration by parts, is bounded by
`epsilon j ||Q||F` and is Lipschitz in `Q` with constant
`C epsilon j`; this follows from Cauchy--Schwarz applied to
`E[N_k (N dot (Q-Q')_.a)]` in absolute value.

A Frobenius-ball net with mesh `R/n` in the fixed dimension `rb` has
at most `(C n)^(rb)` points. The conditional fluctuation argument and
the independent-row Hoeffding argument therefore both hold uniformly
on `||Q||F<=R` with a `sqrt(log n)` loss. After averaging (11d) over
`Z`, the variance of its scalar Gaussian argument is exactly
`sigma_a^2+epsilon^2 ||Q_.a||^2/n`. The one-dimensional density estimate
(15) identifies the center with `epsilon QD`, with error
`Cj epsilon^3 R^3/(n sigma_min^2)`. The possible singularity of the
joint covariance never enters this calculation. Finally use

\[
 (Q-Q_*)(I-\epsilon D)=\mathcal R_G(Q)-\epsilon QD
\]

and the already proved Gaussian bound on the solution norm, taking
`R=C B sqrt(log(e+n))`. This proves (11c).

This model uses the same initialized matrix in its forward and transpose
calls and keeps the adaptive block inside the exact nonlinear equation.
The following version removes the fixed-message-dimension restriction.

### A continuum Gaussian history model, uniform on a Hilbert ball

Let `H` be a real separable Hilbert space, and let `g_i` be independent
centered Gaussian random elements of `H`, with covariance operator `C`
and `0<tr(C)<infinity`. Let `Z_i` be independent `N(0,sigma^2)` variables,
independent of the `g_i`. Write `psi=phi'`, with Lipschitz constant `j`.
For a message `beta in H`, set

\[
 \mathcal R_n(\beta)=\frac1{\sqrt n}\sum_{i=1}^n g_i
   \left[\psi\!\left(Z_i+
           \frac{\epsilon\langle g_i,\beta\rangle}{\sqrt n}\right)
                                                   -\psi(Z_i)\right],
 \quad C_n=\frac1n\sum_i g_i\otimes g_i.
 \tag{11e}
\]

For deterministic `R`, the following estimate is dimension free:

\[
 \mathbb E\sup_{\|\beta\|\le R}
   \|\mathcal R_n(\beta)-\mathbb E\mathcal R_n(\beta)\|
 \le \frac{C\epsilon jR}{\sqrt n}
                              (\mathbb E\|g_1\|^4)^{1/2}.
 \tag{11f}
\]

Consequently the model includes continuous Gaussian histories whenever
those histories are Hilbert-valued. Neither a time grid nor an entropy
bound on an `H1` message class is required for this particular model.
Dimension free here means at fixed covariance moments: for Gaussian
rows, `E||g||^4=(tr C)^2+2 tr(C^2)`. A covariance `C=I_N` with growing
`N` does not have the fixed trace bound required for a uniform constant.
Separability and continuity allow every supremum below to be taken over
countable dense subsets, so the displayed random variables are measurable.

To prove (11f), write

\[
 \chi_i(t)=\sqrt n[\psi(Z_i+\epsilon t/\sqrt n)-\psi(Z_i)].
\]

Conditional on the row data, `chi_i(0)=0` and
`Lip(chi_i)<=epsilon j`. Symmetrization against an independent copy of
the rows bounds the left side by twice

\[
 \frac1n\mathbb E\sup_{\|v\|\le1,\|\beta\|\le R}
       \sum_i s_i\langle v,g_i\rangle
                         \chi_i(\langle g_i,\beta\rangle),
 \tag{11g}
\]

where `s_i` are independent random signs. This symmetrization is valid
for Hilbert norms by representing the norm as the supremum of the scalar
pairings with `v`; the parameter set includes both signs of `v`.

Random signs in (11g) are bounded in expected supremum by a constant
times standard Gaussian multipliers: condition on their signs and use
Jensen over the independent Gaussian absolute values, whose mean is
`sqrt(2/pi)`. For two indices `(v,beta),(v',beta')`, the difference of
the `i`-th scalar coefficient has absolute value at most

\[
 \epsilon j\|g_i\|
  [R|\langle v-v',g_i\rangle|
                       +|\langle\beta-\beta',g_i\rangle|].
 \tag{11h}
\]

Thus the Gaussian increment variance of (11g) is bounded by that of

\[
 \sqrt2\epsilon j\sum_i\|g_i\|
 [R\gamma_i\langle v,g_i\rangle
                      +\gamma_i'\langle\beta,g_i\rangle],
 \tag{11i}
\]

with independent standard Gaussian multipliers. The required Gaussian
comparison can be checked directly: for finite index sets interpolate
between two independent centered Gaussian families, differentiate the
expected soft maximum `a^-1 log sum exp(a X_t)`, and integrate by parts.
The derivative is `(a/4) sum_(s,t) E[p_s p_t]` times the difference
of their increment variances. Ordered increment variances therefore
order expected soft maxima; let `a` tend to infinity. Finite nets extend
this conclusion here, since all the indices appear only through their
projections on the finite span of the observed `g_i`.

The supremum of (11i) is the sum of two Gaussian Hilbert norms, whose
expectation is at most

\[
 C\epsilon jR\left(\sum_i\|g_i\|^4\right)^{1/2}.
\]

Divide by `n` in (11g), then apply Jensen to the row expectation. This
proves (11f). This proof uses only Lipschitz continuity of `psi`.

The exact Gaussian mean is

\[
 \mathbb E\mathcal R_n(\beta)
 =\epsilon C\beta\,
  \mathbb E\psi'\!\left(
       \sqrt{\sigma^2+\epsilon^2\langle\beta,C\beta\rangle/n}\,N
                                      \right).
 \tag{11j}
\]

Indeed the Hilbert Gaussian integration-by-parts identity for a scalar
function of `\langle g,beta\rangle` follows by projecting `g` onto that
one Gaussian direction; its orthogonal Gaussian part has conditional
mean zero. If the direction has zero variance then `C beta=0` and both
sides vanish. The scalar identity follows by ordinary weak Gaussian
integration by parts. The density argument (15) now gives

\[
 \sup_{\|\beta\|\le R}
 \|\mathbb E\mathcal R_n(\beta)-\epsilon d C\beta\|
 \le\frac{j\epsilon^3\|C\|_{\rm op}^2 R^3}{n\sigma^2},
 \qquad d=\mathbb E\psi'(\sigma N).
 \tag{11k}
\]

This also closes a complete adaptive history feedback law. Let
`h_1,...,h_n` be cavity-measurable scalars, independent of the Gaussian
history rows conditional on the cavity, with `n^-1 sum h_i^2<=B^2`.
Set `zeta_n=n^-1/2 sum h_i g_i`. If
`epsilon j tr(C)<=1/4`, then on `tr(C_n)<=2 tr(C)` the equation

\[
 \beta_n=\zeta_n+\mathcal R_n(\beta_n)
 \tag{11l}
\]

is a contraction. In fact Cauchy--Schwarz in the row index gives

\[
 \|\mathcal R_n(\beta)-\mathcal R_n(\beta')\|
 \le\epsilon j\|C_n\|_{\rm op}\|\beta-\beta'\|.
\]

The trace event has probability tending to one, by the scalar law of
large numbers, or exponentially small complement by the Gaussian norm
moment-generating function. The actual solution satisfies
`||beta_n||<=2||zeta_n||`. Conditional on its coefficients, `zeta_n`
is Gaussian with covariance at most `B^2 C`, so its norm has bounded
Gaussian tails. In particular `||beta_n||=O_Pr(1)`. Define

\[
 \beta_{*,n}=(I-\epsilon d C)^{-1}\zeta_n.
\]

The inverse has norm at most `4/3`. Applying (11f)--(11k) on any fixed
ball and then taking its radius large, the exact fixed-point subtraction
proves

\[
 \|\beta_n-\beta_{*,n}\|=O_{\Pr}(n^{-1/2}).
 \tag{11m}
\]

There is no independence claim for the actual adaptive `beta_n`; the
uniform ball estimate is precisely what permits its substitution.
The comparison in (11m) retains the same random Gaussian driving history.

A polynomially high-probability version also follows if needed. Truncate
each row to `||g_i||<=L`, with `L=C_D sqrt(log(e+n))`. The Gaussian
norm tail makes failure over all rows at most `C_D n^-D`. A truncated
row contributes at most `epsilon j R L^2/n` to the uniform empirical
process on the radius-`R` ball. The bounded-difference martingale and
the scalar exponential bound used for (13) bound its upper deviation
by `C_D epsilon j R log(e+n)^(3/2)/sqrt(n)`. The difference of the
truncated and untruncated means is bounded by
`epsilon jR E[||g||^2 1_(||g||>L)]`. Finally take
`R=C_D B sqrt(log(e+n))` from the Gaussian solution bound. This gives
an error of order `n^-1/2 log(e+n)^2`, plus the explicit term (11k),
with constants depending on `C,sigma,epsilon,j,B,D`.

The restriction left in this complete history model is the independent
Gaussian row structure in (11e). An actual trained outside flow has
coupled rows; substituting that flow for (11e) is a separate theorem.

## 4. Gaussian base fields do not give a polynomial strong gate remainder

There is a fixed `C^2` activation satisfying all the activation bounds
such that the Euclidean remainder (1), with `z_i` and `g_i` independent
standard Gaussians and `u_i=g_i/sqrt(n)`, is larger than every fixed
negative power of `n` along a subsequence, with probability tending to
one. The activation need not be `C^3`.

Let

\[
 a_k=2^{-k},\qquad \lambda_k=2^{2^k},\qquad
 \phi(x)=1+\sum_{k\ge1}\frac{a_k}{\lambda_k^2}
                                      (1-\cos(\lambda_kx)).
 \tag{16}
\]

Uniform convergence of each of the displayed series and its first two
derivatives gives

\[
 \psi(x)=\phi'(x)=\sum_k\frac{a_k}{\lambda_k}\sin(\lambda_kx),
 \qquad
 \psi'(x)=\phi''(x)=\sum_k a_k\cos(\lambda_kx).
 \tag{17}
\]

In particular `phi(0)=1`, `||phi'||infinity<=1`, and
`Lip(phi')<=1`. The activation is bounded, and is everywhere at least
one. It therefore even admits a strictly positive initial feature Gram
in the one-sample case. That observation only checks compatibility of
the activation class; it does not realize the following independent
perturbation as a trained-network trajectory.

Choose `n_k=lambda_k^2` and `h_k=1/lambda_k`. For independent standard
Gaussians `Z,G`, define

\[
 X_k(Z,G)=\frac{\psi(Z+h_kG)-\psi(Z)}{h_k}-G\psi'(Z).
 \tag{18}
\]

The `k`-th frequency in this expression is exactly

\[
 a_k\{(\sin G-G)\cos(\lambda_kZ)
                  +(\cos G-1)\sin(\lambda_kZ)\}.
 \tag{19}
\]

Test (18) against
`V_k(Z,G)=sin(lambda_k Z)(cos G-1)` in `L2`. The cosine terms at
every frequency have zero pairing by symmetry in `Z`. At frequency `k`
the pairing is

\[
 a_k\,\mathbb E\sin^2(\lambda_k Z)\,
                  \mathbb E(\cos G-1)^2\ge c a_k.
 \tag{20}
\]

For frequency `r!=k`, the absolute sine coefficient in (18) is bounded
in `L2(G)` by `C a_r`: for `lambda_r/lambda_k<=1`, use
`|cos v-1|<=v^2/2`; otherwise use `|cos v-1|<=2`.
The cross-frequency Gaussian pairing satisfies

\[
 |\mathbb E\sin(\lambda_rZ)\sin(\lambda_kZ)|
 \le\tfrac12\exp[-(\lambda_r-\lambda_k)^2/2].
 \tag{21}
\]

The frequency gaps in (16), together with `sum a_r=1`, make the sum
of all these cross terms `o(a_k)`. Since `||V_k||2<=2`, equations
(20)--(21) and Cauchy--Schwarz give

\[
 \mathbb E X_k^2\ge c a_k^2.
 \tag{22}
\]

The Lipschitz property gives `|X_k|<=2|G|`, hence
`E X_k^4<=C`, uniformly in `k`. For `n_k` independent coordinate pairs,
the squared Euclidean gate remainder equals

\[
 \|e^{(n_k)}\|_2^2
  =\frac1{n_k}\sum_{i=1}^{n_k}X_k(Z_i,G_i)^2.
 \tag{23}
\]

Its variance is at most `C/n_k`. Chebyshev and (22) therefore imply

\[
 \Pr\{\|e^{(n_k)}\|_2<c_0a_k\}
       \le \frac{C}{n_ka_k^4}\longrightarrow0.
 \tag{24}
\]

Finally, `a_k=2^-k` while `log n_k=2^(k+1) log 2`, so
`n_k^alpha a_k -> infinity` for every fixed `alpha>0`. This proves the
claim. It strengthens the deterministic zero-base example in the earlier
cavity report: a perfectly nondegenerate Gaussian base law does not
restore a polynomial **strong** gate-linearization error.

The weak returned observable nevertheless has root-width fluctuations
by Section 2, and the feedback laws have the rates in Section 3.
Thus the strong-remainder obstruction and weak Gaussian cancellation
are consistent.

## 5. What marginal degeneracy does and does not mean here

For any one fixed training input, a population-initial preactivation whose
variance is zero is structurally frozen at zero, up to the first layer
whose activation has a nonzero value at zero. More precisely, first-layer
variance zero means the input is zero, and its first preactivation stays
zero under all training. If the corresponding first feature is zero,
it stays zero. Inductively, a zero feature vector gives zero next
preactivation at every time; its next feature is the fixed constant
`phi_l(0)`. Once this constant is nonzero, the next Gaussian hidden
preactivation has strictly positive initial variance.

The other way an initialized feature can vanish almost surely is that
its preactivation has positive Gaussian variance and its continuous
activation vanishes on the Gaussian support. That activation is then
identically zero, so that feature remains zero for every parameter state.

This induction shows that a nonfrozen preactivation for a fixed sample
has a strictly positive initial marginal Gaussian variance. It does not
give a positive lower bound for a conditional history innovation, nor
does it make trained finite preactivations independent Gaussian.
It is not a statement about every finite-width conditional variance:
an activation with a zero interval can give an accidentally zero finite
feature array even when its population feature variance is positive.
The scalar theorem's use of a marginal variance is therefore less
restrictive than a history-Gram invertibility assumption, but applying
it to trained matrix histories still needs a new comparison.

## 6. Actual-network status and the remaining weak comparison

The existing stopped tangent bound supplies
`exp(C(1+M)Y)`, which is `n^o(1)` at `M=O(sqrt(log n))`.
Section 2 shows that a *complete nonlinear* cavity displacement with
Gaussian-coordinate Lipschitz constant `n^(-1/2+o(1))` has a returned
fluctuation of that same order. It does not require a small Taylor
remainder. This removes one unnecessary regularity demand from a weak
cavity proof.

Two qualifications are decisive for the actual network:

1. The incident Gaussian row also changes the deleted neuron's scalar
   messages. Freezing those messages can restore the small Lipschitz
   constant in (2), whereas differentiating through them introduces
   low-rank response terms of order one. Section 2 handles a bounded
   adaptive scalar by a net; an arbitrary coupled history is not such
   a scalar. The Hilbert-history theorem in Section 3 solves this
   uniformity problem for independent row functions. It does not assert
   row independence for the trained outside flow.
2. The exact center in (3) is the expected divergence of the *nonlinear
   outside response*. Identifying it with the population response is
   an additional weak comparison. Replacing it by the cavity Jacobian
   at zero using a Euclidean gate remainder is ruled out in the general
   activation class by Section 4. The independent Gaussian-row structure
   permits the direct density arguments in Section 3; these do not yet
   control row-dependent matrix response coefficients and both adjoint
   directions in the deep network.

In particular the stopped response norm by itself does not prove that
the actual self-return has coefficient `O(Y^2)` with a width-independent
constant, and does not establish the actual carrier stop probability.
No trained carrier bound is inserted into the hypotheses here.

The proposed coarser actual deletion argument was also checked. Restoring
one neuron's incident column or row produces a Euclidean outside-field
pulse proportional to its local message. Its effect on outside parameter
velocities in the canonical Hilbert norm is of order
`rho times local message / sqrt(n)`. The stopped response bound transports
such a pulse with multiplier `exp(C(1+M)Y)`. The resulting roundtrip bound
has coefficient of the form `C Y^2 exp(C(1+M)Y)`, which does not absorb
at `M=C0 sqrt(log n)` for fixed positive labels. The curvature term
`phi''(z) P` in the outside Jacobian is the obstruction to making this
coarse bound deterministic and independent of `M`: operator and RMS
bounds alone allow large localized `P`, and the negative `J*J` term has
rank at most the fixed sample count. This calculation does not exclude
an averaged response bound or a Volterra induction over deleted width.

A second caution concerns a proposed use of history entropy. A finite
Dudley integral for a bounded `H1` path class is not enough by itself.
One must first prove a subGaussian increment metric for the centered
returned observable, with the required `n^-1/2` factor. The pointwise
nonlinear Gaussian-gradient bound (3) does not prove that increment
metric: taking a difference of its Jacobians can again introduce the
uncontrolled modulus of `phi''`. The independent-row symmetrization and
Gaussian comparison in (11g)--(11i) establish uniformity without that
step, which is why the complete Hilbert model is valid. The trained
outside response still needs a replacement for that independent-row
argument.

| Claim | Status after this round |
|---|---|
| Nonlinear Gaussian returned-gate fluctuation, one weak derivative | Proved in (3) |
| Adaptive scalar returned-gate fluctuation | Proved in (8) |
| Gaussian-base scalar gate feedback: stop and population response rate | Proved in (11) |
| Fixed block with the same forward/transpose matrix | Proved in (11a)--(11d) |
| Continuum Gaussian-history feedback, uniform on a Hilbert ball | Proved in (11e)--(11m) |
| Polynomial Euclidean gate tangent remainder from Gaussian base alone | False, by (16)--(24) |
| Actual simultaneous forward/transpose cavity law | Open |
| Actual all-time near-root-width predictor and dense-tail floor | Open |
| Unconditional `epsilon^(-5/2+o(1))` moving-state certificate | Not established |

The route to pursue is an observable-level joint cavity comparison which
retains the nonlinear response until after Gaussian expectation. The
present counterexample means that filling the earlier strong remainder
lemma by a generic Gaussian-smoothing argument is not a valid route.

## Source hashes

`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`:
`0801cb31acd77d8fbd157833090de3f88e5484a23cb471349b6e9c1b7e413bb7`.

`ACTIVATION_GAUSSIAN_ALLTIME.md`:
`6385264a060893eb226e94b4302ff86a095e00bf34e9fa364f4e7759486139d0`.

`QUANTITATIVE_WIDTH_CAVITY.md`:
`716bdfcb75500e220332386e1dea19e7770c91fc40f6603e4879754460b87eff`.

`QUANTITATIVE_WIDTH_SENSITIVITY.md`:
`56b08142ba19332763171d6d69b784aba9aa001be09d904a22922855a1e0d645`.
