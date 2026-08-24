# Row-summing the off-column leaf and the next cavity gap

We retain the normalization and notation of
`two_row_entry_cavity_leaf.md`.  Fix a source entry `e=(s,l)` and a lower
coordinate `j`.  The feeding rows are `r != s`.

## 1. Exact conditional row sum

After the two-row cavity and the orthogonal decomposition of row `r`, the
off-column atom is

\[
 Y_{r,e,j}={\sigma_{rj}\over\sqrt n}\,G_{2r}C_{r,e},\qquad
 C_{r,e}=A_r\{d(Z_r+\alpha_{r,e}G_{1r})-d(Z_r)\}.                         \tag{1}
\]

Here `G_{2r}` is the fresh component orthogonal to all the parallel query
directions.  Conditional on the parallel data, the variables `G_{2r}` are
independent standard Gaussians and are independent of the coefficients
`C_{r,e}`.  Therefore, *before any absolute values are taken*,

\[
 \sum_{r\ne s}Y_{r,e,j}\ \bigg|\ (C_{r,e})_r
 \sim N\left(0,{1\over n}\sum_{r\ne s}\sigma_{rj}^2C_{r,e}^2\right).      \tag{2}
\]

This is the gain lost by estimating the rows separately.

The exact gate identity and the endpoint bound give, for every `q >= 2`,

\[
 \|C_{r,e}\|_q
 \le C_T\min\{\alpha_{r,e}q,\sqrt q\}
 \le C_T\alpha_{r,e}q,                                                   \tag{3}
\]

and

\[
 \mathbb E C_{r,e}^2\le C_T\alpha_{r,e}^2.                               \tag{4}
\]

No exponential moment of `A_r^2` is used in (3)--(4).  A direct proof is
`|Delta d| <= min(C alpha |G_1|,2)`, `|A_r| <= |A_r^0|+C_T`, followed by
Holder for the two Gaussian factors.

For completeness, the elementary Hilbert-valued Hoffmann--Jorgensen
estimate gives

\[
 \left\|\left(\sum_r C_{r,e}^2\right)^{1/2}\right\|_p
 \le C\left[
       \left(\sum_r\mathbb EC_{r,e}^2\right)^{1/2}
       +\|\max_r|C_{r,e}|\|_p\right].                                   \tag{5}
\]

Indeed apply symmetrization and the Hoffmann--Jorgensen inequality to the
independent Hilbert-valued variables `C_r e_r`; the mean vector and the
mean norm are both bounded by the first term.  From (3) and a union bound,

\[
 \|\max_{r\le n}|C_{r,e}|\|_p
 \le C_T\alpha_*\,(p+\log n),\qquad
 \alpha_*:=\max_r\alpha_{r,e}.                                         \tag{6}
\]

Combining (2), (5), and (6),

\[
 \boxed{
 \left\|\sum_{r\ne s}Y_{r,e,j}\right\|_p
 \le {C_T\sqrt p\over\sqrt n}
 \left[
   \left(\sum_r\alpha_{r,e}^2\right)^{1/2}
   +\alpha_*(p+\log n)
 \right]. }                                                            \tag{7}
\]

On the entry-response scale

\[
 \alpha_*=O_T(n^{-1}),\qquad \sum_r\alpha_{r,e}^2=O_T(n^{-1}),           \tag{8}
\]

this becomes

\[
 \left\|\sum_{r\ne s}Y_{r,e,j}\right\|_p
 \le C_T\left{
 {\sqrt p\over n}+{\sqrt p(p+\log n)\over n^{3/2}}
 \right}.                                                             \tag{9}
\]

For `p >= log n` the second term is the advertised single-row branch
`p^(3/2)/n^(3/2)`.  For `2 <= p <= c log n`, it is still lower than the
Gaussian branch by `O(log(n)/sqrt(n))`.  Thus row summation repairs the
per-row loss throughout the logarithmic moment range.

An equivalent conditional sub-Weibull Bernstein statement is

\[
 \left\|\sum_rY_{r,e,j}\right\|_p
 \lesssim {\sqrt p\over n}+{p^{3/2}\over n^{3/2}}                       \tag{10}
\]

when one works at `p >= log n`; (9) is the version valid without hiding the
maximum over rows.

## 2. Time factors

Let `J_{m,k}` denote any already controlled causal propagator in the lower
response equation.  The feeding contribution at time `m` is

\[
 F_{e,j}^m=h\sum_{k<m}J_{m,k}S_{e,j}^k,
 \qquad S_{e,j}^k=\sum_{r\ne s}Y_{r,e,j}^k.                              \tag{11}
\]

Using only `||J_{m,k}|| <= C_T` and the triangle inequality in time,

\[
 \|F_{e,j}^m\|_p
 \le C_T\left{
 {\sqrt p\over n}+{\sqrt p(p+\log n)\over n^{3/2}}
 \right},                                                             \tag{12}
\]

because `h sum_(k<m) 1 <= T`.  Thus reuse of the endpoint marks in time
does not spoil the row gain.

For comparison, the genuinely newest entry response has
`alpha_new=O(h/n)`.  Its current-current contribution has size

\[
 h\left({\sqrt p\,h\over n}
       +{\sqrt p(p+\log n)h\over n^{3/2}}\right)                         \tag{13}
\]

per update.  If those chronological pieces are square-summed over
`m=T/h` independent innovations, their Gaussian scale is

\[
 {h^2\over n}\sqrt{T/h}={\sqrt T\,h^{3/2}\over n}.                      \tag{14}
\]

They are strictly smaller.  The old accumulated part is handled by (12),
with no fictitious time independence.

## 3. Entry aggregation in the decoupled surrogate

If a whole source row `s` is reconstructed by the `n` sequential entry
innovations `e=(s,l)`, and the entry-centered coefficients are frozen at a
common row cavity, then the variance sum is

\[
 \sum_{l=1}^n O_T(n^{-2})=O_T(n^{-1}).                                  \tag{15}
\]

Consequently the feeding part of the row difference has

\[
 \left\|\sum_{l=1}^n F_{(s,l),j}^m\right\|_p
 \le C_T\left{{\sqrt p\over\sqrt n}
       +{\sqrt p(p+\log n)\over n^{3/2}}\right}.                       \tag{16}
\]

The direct source-row atom has the usual two-carrier Bernstein branch
`p/n` per entry; after entry aggregation this gives the standard
`sqrt(p/n)+p/n` bound.  Hence the feeding leaf is not the limiting term in
the ideal jointly decoupled FD/RD induction.

## 4. What is not jointly independent

Formula (2) is exact only when every coefficient multiplying `G_{2r}` is
measurable before all the fresh off-column variables `(G_{2r})_r` are
revealed.  A coefficient evaluated on the `r,s` two-row cavity has this
property with respect to row `r`, but it need not have it jointly: the
`q,s` cavity trajectory used in `C_{q,e}` still contains row `r`.

Replacing the family of `r`-dependent cavities by jointly conditionable
coefficients produces

\[
 \Delta_qY_{r,e,j},\qquad q\ne r,s,                                     \tag{17}
\]

and this contains the third mixed response

\[
 \Delta_q\Delta_r\Delta_eX_2.                                          \tag{18}
\]

The exact gate finite difference gives the schematic but normalized
identity

\[
\begin{split}
 \Delta_qY_{r,e,j}
 ={A_rG_{2r}\over\sqrt n}\{&
   Dd\,G_r(\Delta_q\Delta_eX_2)\\
   &+D^2d\,[G_r(\Delta_qX_2)] [G_r(\Delta_eX_2)]
   +\hbox{learned/endpoint finite differences}\}.                       \tag{19}
\end{split}
\]

All divided differences in (19) are bounded.  With the natural cavity
scales

\[
 \|\Delta_qX_2\|_n=O_T(n^{-1/2}),\quad
 \|\Delta_eX_2\|_n=O_T(n^{-1}),\quad
 \|\Delta_q\Delta_eX_2\|_n=O_T(n^{-3/2}),                              \tag{20}
\]

each ordered pair `(r,q)` in (19) has `L^2` scale `O_T(n^{-2})`.
Endpoint and gate moments give a harmless high-moment branch
`C_T poly(p)/n^2`; for `p <= c log n` it is lower order after summation.

After a full `(r,q,s)` cavity, the leading replacement error is a decoupled
two-row Gaussian kernel

\[
 H_e=\sum_{r\ne q,s}K_{rq,e}\,\zeta_r\widetilde\zeta_q,                 \tag{21}
\]

where `zeta` and `tilde zeta` are fresh row residuals.  The natural
Hilbert--Schmidt estimate from (20) is

\[
 \|K_e\|_{\rm HS}
 =\left(\sum_{r,q}|K_{rq,e}|^2\right)^{1/2}
 \le {C_T\over n}.                                                      \tag{22}
\]

Conditional Gaussian-chaos/Hanson--Wright gives exactly

\[
 \|H_e\|_p
 \le C\left[
   \sqrt p\,\|K_e\|_{\rm HS}
   +p\,\|K_e\|_{\rm op}
 \right]+{C_T\,\mathrm{poly}(p)\over n^2}.                             \tag{23}
\]

Energy and the second mixed estimates only imply

\[
 \|K_e\|_{\rm op}\le\|K_e\|_{\rm HS}\le C_T/n,                       \tag{24}
\]

which leaves the term `C_T p/n`.  To preserve the row-summed target one
needs the genuinely new joint-leverage estimate

\[
 \boxed{\quad \|K_e\|_{\rm op}\le C_Tn^{-3/2}\quad}                    \tag{25}
\]

(in conditional probability or in the appropriate logarithmic moments).
Then (23) becomes

\[
 \|H_e\|_p\le C_T\left{{\sqrt p\over n}
       +{p\over n^{3/2}}+{\mathrm{poly}(p)\over n^2}\right},           \tag{26}
\]

and closes for `p <= c log n`.  Without (25), the cavity replacement is a
coherent rank-one-sized two-row chaos and is one factor `sqrt(p)` too
large.

The Euler time sum does not improve (22)--(24):

\[
 K_e^{[0,T]}=h\sum_{k<T/h}J_{m,k}K_{e,k},\qquad
 \|K_e^{[0,T]}\|_{\rm HS}\le h\sum_k{C_T\over n}={C_T\over n},          \tag{27}
\]

and the old row residuals are reused, so there is no legitimate
`sqrt(h)` gain in the operator term.  Aggregating the `n` source entries
would give the correct `n^{-1/2}` row scale from the Hilbert--Schmidt
branches, but the unresolved operator branch correspondingly becomes
`p/sqrt(n)` unless a tensor version of (25) is proved.

## 5. Verdict

Summing the independent fresh `G_2` rows first **does** eliminate the
single-row `p^(3/2)/n^(3/2)` obstruction, without exponentiating endpoint
marks.  The exact finite-mesh and time scales are (9), (12), and (16).

This does not yet close the actual FD/RD induction.  Jointly replacing the
family of row-dependent two-row cavities creates the third mixed difference
(18).  Its Frobenius scale is correct, `1/n`, but available estimates do not
give the operator scale `1/n^(3/2)` required in (25).  Thus the gap has moved
one level, from a one-row Orlicz atom to a concrete third-mixed joint-leverage
lemma.  No exponential endpoint-mark estimate is needed before that point.
