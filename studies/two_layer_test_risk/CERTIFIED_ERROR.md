# Rigorous Gaussian cubature error for the fixed cubic coefficient

Author: `certified_error`, 2026-09-10. Approach B, supporting the resumed
fixed-model sign calculation. This file proves an error certificate; it does
not assert a numerical sign or change the network/data contract. No training,
sampling, sweep, or numerical integral has been run by this author.

The exact number to enclose is the `chi` in CUBIC_DERIVATION.md (13), with
(14)--(19) specifying its Gaussian moments. Its previous numerical values
are not used as error bounds. All Gaussian integration errors below are
absolute, for normalized Gaussian expectations.

## 1. Analytic-strip tensor rule, with a finite tail

Write `gamma(x)=exp(-x^2/2)/sqrt(2 pi)`. Let `F:R^d -> C` have a holomorphic
extension when any one coordinate is moved into `|Im z_j|<=a_j`, all other
coordinates remaining real. Suppose on those separate strips
`|F|<=M_j`, and on the real domain `|F|<=M_0`. We do not require boundedness
when multiple coordinates move into their complex strips simultaneously.
For positive `h_j`, integers `m_j>=1`, and `r_j=m_j h_j`, define

\[
 Q_j v=h_j\sum_{k=-m_j}^{m_j}\gamma(kh_j)v(kh_j),\qquad
 \delta_j=\frac{2e^{-2\pi^2/h_j^2}}{1-e^{-2\pi^2/h_j^2}},
\]

\[
 e_j=\frac{2M_j e^{a_j^2/2}}{e^{2\pi a_j/h_j}-1}
       +\frac{2M_0\gamma(r_j)}{r_j}.
\tag{E1}
\]

Then

\[
 \left|E F(N_1,\ldots,N_d)-Q_1\cdots Q_dF\right|
 \le \sum_{j=1}^d e_j\prod_{i<j}(1+\delta_i).
\tag{E2}
\]

The constants apply uniformly to any fixed real external parameters in `F`.
In particular, they are valid at a coincident or antipodal passive input.
The finite rule weights need not sum to one, and are not implicitly
renormalized. If a producer does normalize them, it must charge that change.

**Proof of the one-coordinate bound.** Fix the other real coordinates and
put `f(z)=gamma(z)F(z)`. For real frequency `w`, shifting the Fourier integral
to `Im z=-a sign(w)` gives

\[
 |\widehat f(w)|\le M_j e^{a_j^2/2}e^{-a_j|w|}.
\]

The contour shift is legitimate: `F` is holomorphic on the strip, bounded
there, and on the two vertical sides the Gaussian factor tends to zero
uniformly as the real endpoint tends to infinity. A shift at a boundary
may equivalently be obtained by first using a smaller strip and taking its
limit. The periodization `sum_k f(x+kh)` converges uniformly on `[0,h]`,
since `F` is bounded on the real line and the Gaussian tails are summable.
Its Fourier coefficients are `hat f(2 pi l/h)/h`; the displayed exponential
bound makes their series absolutely convergent. Evaluate the series at
zero and separate its zero coefficient. This proves directly

\[
 \left|\int f(x)\,dx-h\sum_{k\in\mathbb Z}f(kh)\right|
 \le\frac{2M_j e^{a_j^2/2}}{e^{2\pi a_j/h}-1}.
\]

For the deleted terms, monotonicity of `gamma` on `[0,infinity)` gives

\[
 h\sum_{|k|>m}\gamma(kh)
 \le 2\int_{mh}^\infty\gamma(u)\,du
 \le\frac{2\gamma(mh)}{mh}.
\]

The last inequality follows by replacing `1` by `u/(mh)` in the integral
and integrating `u gamma(u)=-gamma'(u)`. This proves (E1).

For the Gaussian weight alone, the same Fourier computation uses
`hat gamma(w)=exp(-w^2/2)`. The infinite rule mass is
`1+2 sum_{l>=1}exp(-2 pi^2 l^2/h^2)`, at most `1+delta_j` because
`l^2>=l`. The finite positive rule has no greater mass. Finally telescope
`I_1...I_d-Q_1...Q_d` by replacing one coordinate at a time. Already
replaced coordinates contribute their positive rule masses and remaining
integral coordinates have mass one. This proves (E2). In this proof every
contour shift has just one nonreal coordinate; a joint polydisc hypothesis
has not been silently introduced.

## 2. Apply the bound to tanh moments and anisotropic Gaussian roots

Put `H(z)=tanh z`, `D(z)=H'(z)`, `E(z)=H''(z)`. For `|Im z|<=pi/4`,

\[
 |H(z)|\le1,\qquad |D(z)|\le2,\qquad |E(z)|\le4.
\tag{E3}
\]

Indeed, writing `z=x+iy`, the square of the first modulus is
`(sinh^2 x+sin^2 y)/(sinh^2 x+cos^2 y)<=1`. Also
`|D(z)|=1/(sinh^2 x+cos^2 y)<=2`, and `E=-2HD` gives the last bound.
All three functions are holomorphic on the wider strip `|Im z|<pi/2`.

Let the root map used for quadrature be a **specified real matrix** `A`,
with `Y=A N`, and let `c_j>=max_i|A_ij|` be certified upper bounds.
The one-coordinate strips in (E1) are admissible whenever

\[
 a_j c_j\le\pi/4.
\tag{E4}
\]

Changing only the `j`th root coordinate moves every preactivation by at
most `c_j a_j` in imaginary part. Large shifts in a small root column are
therefore legitimate; they need not be restricted by larger columns.
If `c_j=0`, any finite `a_j` may be used, or that dimension may be omitted.

For a monomial containing `r` factors `D` and `s` factors `E`, with any
number of factors `H`, (E3) gives `M_j=2^r 4^s`. On the real domain all
three factors have absolute value at most one, so `M_0=1`. Repeated named
slots do not change the proof: count every multiplicative factor. Linear
combinations are bounded by the corresponding sum of absolute coefficients.
For example, with `P=sum_a|p_a|=(1+sqrt(5))/6<.54`,

| Moment integrand | Real bound `M_0` | One-root strip bound `M_j` |
|---|---:|---:|
| `S^2` | `P^2` | `P^2` |
| `S^2 D_a D_b` | `P^2` | `4P^2` |
| `H_x S D_a D_b` | `P` | `4P` |
| `D_i D_a` | `1` | `4` |
| `S E_a` | `P` | `4P` |
| `H_x E_a` | `1` | `4` |
| `S H_x` | `P` | `P` |

Here `S=sum_a p_a H_a` uses the actual signed training weights. These are
bounds for quadrature; no signed weight is replaced inside the coefficient.
Lower-population moments `Q`, `L`, and `T` use the same rule with the
actual two-root map `(cos alpha_i,sin alpha_i)`. In particular their
rank-deficient covariance is neither inverted nor whitened.

A concrete parameter choice available before a numerical result is to fix
`R=8` and `B=26` (or the more conservative `B=30`), then set

\[
 a_j=\min\{\pi/(4c_j),\sqrt{2B}\},\qquad
 h_j^*=\frac{2\pi a_j}{B+a_j^2/2},\qquad
 m_j=\lceil8/h_j^*\rceil,\qquad h_j=8/m_j.
\tag{E5}
\]

All decisions and inequalities in this prescription must themselves be
certified if floating-point arithmetic constructs the rule. It gives
`2 pi a_j/h_j>=B+a_j^2/2`, so the strip error per coordinate is at most

\[
 \frac{2M_j e^{-B}}{1-e^{-B-a_j^2/2}}.
\]

The tail error is `2M_0 exp(-32)/(8 sqrt(2 pi))`, less than
`1.27e-15 M_0`. The finite exact formulas, rather than rounded decimals,
are the certificate. For a simple rational envelope in dimensions `d<=4`,
(E5) with `B=26` gives total analytic cubature error at most
`5e-11 M_* + 6e-15 M_0`, where `M_*=max_j M_j`. With `B=30` it gives
at most `1e-12 M_*` whenever `M_0<=M_*`. To verify these without trusting
rounded exponential values, use
`exp(26)>195000000000`, `exp(30)>10000000000000`, and
`exp(32)>78900000000000`: each follows from the exact rational partial
sum `sum_{j=0}^{80} x^j/j!` at the indicated positive integer `x`.
Also `sqrt(2 pi)>5/2`. The grid satisfies
`h_j<=pi sqrt(2/B)`, by maximizing `2 pi a/(B+a^2/2)` in `a`, so
`delta_j<=2/(exp(B)-1)`. Substituting these inequalities into (E1)--(E2)
gives the stated rational envelopes. The displayed finite-sum inequalities
were independently evaluated in Python `Fraction` arithmetic on 2026-09-10;
all three comparisons returned true. This was a scalar arithmetic check,
not a Gaussian-integral run. This file makes no post-result grid selection.
The executing producer's frozen configuration specifies which admissible
choice is used and records its hard arithmetic/runtime budget.

## 3. Covariance error without a passive square-root derivative

Suppose `Q` and `Qbar` are positive semidefinite `q by q` matrices, including
singular ones. Let `F:R^q -> R` be bounded and twice continuously
differentiable with bounded first and second derivatives. If
`epsilon_Q=max_ij|Q_ij-Qbar_ij|`, then

\[
 |E_{N(0,Q)}F-E_{N(0,\overline Q)}F|
 \le\frac{\epsilon_Q}{2}\sum_{i,j}
                   \|\partial_i\partial_jF\|_\infty.
\tag{E6}
\]

**Proof.** For `delta>0` interpolate the positive definite matrices
`Q_s=(1-s)Q+s Qbar+delta I`. Differentiating their Gaussian densities gives
`partial_s rho_s=(1/2)sum_ij(Qbar-Q)_ij partial_i partial_j rho_s`.
This identity can also be checked by differentiating their characteristic
functions `exp(-xi^T Q_s xi/2)`. Integrating twice by parts is valid for
bounded `F` and its derivatives, because every density derivative is a
polynomial times a decaying Gaussian. Thus

\[
 \frac{d}{ds}E_{N(0,Q_s)}F
 =\frac12\sum_{i,j}(\overline Q-Q)_{ij}
                       E_{N(0,Q_s)}\partial_i\partial_jF.
\]

Integrating `s` from zero to one gives (E6), uniformly in `delta`.
At each endpoint realize the regularized vector as its original Gaussian
vector plus an independent `sqrt(delta)` standard Gaussian. Boundedness,
continuity and dominated convergence then pass to `delta=0`.
This supplies the formula at singular passive covariances without any
inverse or derivative of a selected covariance square root.

For execution, treat each stored root entry of `A` as an exact rational
floating-point number and set `Qbar=A A^T` **in exact arithmetic**. It is
then automatically positive semidefinite. Compute a rigorous interval for
`Q-Qbar` from the certified lower moments and exact matrix products. No
claim that the numerical root is an exact root of `Q` is needed. A small
negative residual from a floating conditional-variance computation must
not be silently clipped and called exact; its resulting root is instead
handled by this explicit covariance perturbation certificate.

## 4. Explicit Hessian constants for all upper primitive moments

On the real line,

\[
 |H|,|H'|,|H''|\le1,\qquad |H'''|\le2,\qquad |H''''|\le5.
\tag{E7}
\]

For the first three assertions use `u=tanh x in[-1,1]`,
`H'=1-u^2` and `H''=-2u(1-u^2)`, whose maximum absolute value is
`4/(3 sqrt(3))<1`. Also `H'''=(1-u^2)(-2+6u^2)` has absolute value
at most two. Finally `H''''=16u-40u^3+24u^5` vanishes at the endpoints;
its interior extrema have `u^2=(15+-sqrt(105))/30`. Substitution gives
absolute values less than five (the two squared roots lie in
`[.15,.16]` and `[.84,.85]`, which already give this strict bound).

For a product `F=prod_{l=1}^r f_l(Y_{i_l})`, where each `|f_l|<=1`,
`|f_l'|<=b_l`, `|f_l''|<=c_l`, the product rule gives

\[
 \sum_{i,j}\|\partial_i\partial_jF\|_\infty
 \le\sum_l c_l+\sum_{l\ne k}b_l b_k.
\tag{E8}
\]

This remains true for repeated slots: summing derivative terms before
bounding them can only create cancellations omitted by the right side.
Apply (E8) with `(b,c)=(1,1)` for `H`, `(1,2)` for `D`, and `(2,5)`
for `E`. The exact constants needed in (E6) are consequently

| Monomial `F` | Hessian sum bound | Covariance error bound |
|---|---:|---:|
| `H_i H_j` | `4` | `2 epsilon_Q` |
| `D_i D_j` | `6` | `3 epsilon_Q` |
| `H_i E_j` | `10` | `5 epsilon_Q` |
| `H_i H_j D_a D_b` | `18` | `9 epsilon_Q` |

After expanding only the finite `S` sums this yields, with all indices
and repetitions allowed,

\[
\begin{aligned}
 |\delta E S^2|&\le2P^2\epsilon_Q,\\
 |\delta E[S^2D_aD_b]|&\le9P^2\epsilon_Q,\\
 |\delta E[H_xSD_aD_b]|&\le9P\epsilon_Q,\\
 |\delta E[\partial_i U_a]|&\le
   (3|p_i|+5P\mathbf1_{i=a})\epsilon_Q,\\
 |\delta E[\partial_i(H_xD_a)]|&\le
   (3\mathbf1_{i=x}+5\mathbf1_{i=a})\epsilon_Q,\\
 |\delta\{2E[SH_x]\}|&\le4P\epsilon_Q.
\end{aligned}\tag{E9}
\]

Here `delta E` denotes the difference between the two covariance laws,
not a derivative in time. In the formal passive slot `p_x=0`, exactly as
in the original derivation. (E9) certifies the full response means; it
does not remove the response mean-product term in `Lambda`.

## 5. Arithmetic and final assembly obligations

The analytic inequalities enclose exact Gaussian integrals. A floating
sum becomes a certificate only after its arithmetic is also enclosed.
An acceptable implementation combines:

1. Certified input constants and stored root entries, with (E6) charging
   the difference between the exact Gaussian covariance and `A A^T`.
2. Explicit error bounds for each elementary function and all arithmetic
   used to evaluate the tensor sum. Ordinary library `tanh` or `exp`
   accuracy is not an implicit theorem.
3. Positive Gaussian weights and a proved summation error bound. If
   `n` consecutive binary operations have unit roundoff `u` and `nu<1`,
   the usual product expansion bounds their accumulated relative factors
   by `gamma_n=nu/(1-nu)`. An actual producer must state its order/count,
   precision and absence of overflow/underflow; it cannot charge only
   the final scalar rounding.
4. Exact rational interval evaluation of the finite coefficient formulas,
   including the division by a strictly positive enclosed `B_0=E S^2`.
   Separately enclose the clock subtraction: a positive unadjusted
   teacher projection does not establish a matched-loss sign.
5. The coordinator's independent whole-circle integration bound, which
   avoids differentiating a passive Cholesky factor. Every discrete
   angular value is enclosed using (E1)--(E9), whether its root choice
   changes smoothly with angle or not.

A practical elementary-function construction is available without calling
an assumed correctly-rounded `tanh`: for a real argument `|x|<=16`,
approximate `exp(-|x|/128)` by its degree-12 Taylor polynomial, square eight
times to obtain `exp(-2|x|)`, and form
`sign(x)(1-v)/(1+v)`. The alternating-series truncation is bounded by
`(|x|/128)^13/13!`. Rounding must be added at every Horner/squaring/ratio
step and the previously rounded argument must also be charged. This
sentence specifies a construction, not a claimed error constant for an
uninspected implementation. The same construction handles Gaussian
weights after suitable range reduction.

A final interval `[chi_minus,chi_plus]` with `chi_minus>0` proves the
positive coefficient. An interval strictly below zero proves the opposite
sign. An interval containing zero remains inconclusive. Refinement trends,
parity residuals or a floating sign never replace this decision rule.
The already proved time remainder then supplies the corresponding finite
positive-time statement; it does not improve the numerical enclosure.

## Scope and provenance

The complete source read for this certificate consists of
CUBIC_DERIVATION.md and check_coefficient.py, the study README, root AGENTS
and RESEARCH_WORKFLOW, docs README and NOTATION, and the complete current
CONTINUATION_DISPOSITION. The Gaussian cubature and covariance arguments
needed here are proved above; no external cubature theorem or maintained
implementation API is imported. The earlier nonlinear population theorem
is not re-proved in this subtask. Required skills read were
solve-math-rigorously and investigate-conjectures, with research-contract,
evidence-ledger, adversarial-audit, proof-search-orchestration and
decisive-experiments references. Shared edits and index changes are left
to the coordinator. This author owns only this source file and assigned
generated scratch.
