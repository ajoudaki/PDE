# Independent route to the normalized-probe p4 and p5 dictionaries

The middle-weight coefficient at `t^5` needs no new frozen factors beyond
the current p3 list. A concrete nested sufficient list through `t^6` has
**14 lower and 24 upper generators**: retain p3's `(6,12)` and append eight
lower quartic-label coefficients and twelve upper quintic-label coefficients.
These are declared generator counts, not a proof of linear independence or
minimality at p5.

## Setup and claim level

The physical probes are `x_a=sqrt(2)e_a`; hence their normalized inputs are
`x_a/sqrt(2)=e_a`, and their input Gram is the identity. The readout starts at
zero at population level. The loss is unhalved equally weighted MSE,
`(r_1^2+r_2^2)/2`. The literal physical probes in DERIVATION.md instead have
normalized Gram `I/2`; its `1/4` lower-activation prefactor must therefore
be replaced by `1/2` here. No finite random readout is silently set to zero.

Write `W=W^(2)`, `W_0=W(0)`, `c=W^(3)`, and

\[
g_a=W^{(1)}(0)e_a,\quad h_a=\tanh g_a,\quad
Y_a=W_0h_a,\quad H_a=\tanh Y_a,
\]
\[
\ell_a=\phi'(g_a),\quad m_a=\phi''(g_a),\quad
d_a=\phi'(Y_a),\quad d_a^{(2)}=\phi''(Y_a),\quad d_a^{(3)}=\phi'''(Y_a),
\qquad \phi=\tanh.
\]

The superscripts `(2)` and `(3)` denote derivative order, not powers.
Products of fields are
pointwise on their own population. Pairings are population expectations,
and `(u tensor h)z=u E_1[hz]`. Set

\[
v=E[\tanh(G)^2],\qquad
\tau=E[\tanh(\sqrt vG)^2],\qquad G\sim N(0,1).
\]

The initialized lower and upper probe Grams are `vI` and `tau I`.
The adjoint `W_0^*` below is always the **actual initialized adjoint**. It is
not replaced by an independent Gaussian matrix or an independent source.

This is a finite formal coefficient derivation from the population vector
field. The algebra gives actual Taylor coefficients whenever the population
solution has the indicated time derivatives and products/pairings in the
required spaces. The strong-flow `L2` justification in DERIVATION.md through
the previously computed order does not by itself prove that stronger
regularity through order six. No analyticity, summed Taylor series or
closure-convergence conclusion is asserted here. At finite width the
ordinary smooth-vector-field recurrence is exact, but the population Gram
and moment simplifications below are not exact empirical identities.

## Lower-order coefficients and the scalar residual feedback

Use positive residuals `b_a(t)=y_a-f_a(t)`. The normalized-probe equations are

\[
\dot c=\sum_a b_aH_a(t),\qquad
\dot W=\sum_a b_a[c\phi'(Y_a(t))]\otimes h_a(t),
\]
\[
\dot g_a(t)=b_a\phi'(g_a(t))W(t)^*
 [c\phi'(Y_a(t))].
\tag{1}
\]

All coefficients below use ordinary powers, not divided derivatives.
Define

\[
S=\sum_a y_aH_a,\qquad
\mathcal D=\sum_a y_a(Sd_a)\otimes h_a,\qquad B_2=\mathcal D/2,
\]
\[
q_a=\frac{y_a}{2}\ell_aW_0^*(Sd_a),\qquad
V_a=\ell_aq_a,\qquad
R_a=B_2h_a+W_0V_a
    =\frac{vy_a}{2}Sd_a+W_0V_a,
\]
\[
J=\sum_a y_ad_aR_a,\qquad
K_a=\frac13d_aJ+Sd_a^{(2)}R_a,
\]
\[
\mathcal F=\sum_a y_a\{K_a\otimes h_a+(Sd_a)\otimes V_a\}.
\tag{2}
\]

Thus `V,R` are homogeneous of label degree two, `J,K` of degree three,
and `F` of degree four. The current p3 upper columns are exactly six times
the four binary cubic coefficients of each `K_a`. Its lower extra columns
are twice the nonzero binary quadratic coefficients of `V_a`.

For the scalar output correction put

\[
\beta_a=\frac13\langle J,H_a\rangle_2+
           \langle S,d_aR_a\rangle_2,\qquad
B=\sum_a\beta_aH_a.
\tag{3}
\]

Each `beta_a` is a scalar homogeneous cubic polynomial in the labels.
Although it depends on initialized population moments, it is not a new
population field. Substitution into (1) gives

\[
h_a(t)=h_a+t^2V_a-\tau t^3V_a+t^4h_{a,4}+\cdots,
\quad
Y_a(t)=Y_a+t^2R_a-\tau t^3R_a+t^4Y_{a,4}+\cdots,
\]
\[
c(t)=tS-\frac\tau2t^2S+
t^3\left(\frac{\tau^2}{6}S+\frac13J\right)
+t^4\left(-\frac{\tau^3}{24}S-\frac\tau2J-\frac14B\right)+\cdots,
\]
\[
f_a(t)=\tau y_at-\frac{\tau^2}{2}y_at^2+
 \left(\frac{\tau^3}{6}y_a+\beta_a\right)t^3
 +\left(-\frac{\tau^4}{24}y_a-\frac{7\tau}{4}\beta_a\right)t^4+\cdots.
\tag{4}
\]

For example, the fourth output coefficient pairs the fourth readout
coefficient with `H_a`, the second readout coefficient with `d_aR_a`,
and `S` with `-tau d_aR_a`. Since `<B,H_a>=tau beta_a`, (3) combines
these terms into the fourth coefficient displayed in (4).

## The fifth power adds no new span

Multiplying the four factors in the middle equation gives

\[
[t^4]\dot W=-\frac{5\tau^3}{8}\mathcal D
 -\frac{5\tau}{2}\mathcal F
 -\sum_a\left(\frac{y_a}{4}Bd_a+\beta_aSd_a\right)\otimes h_a.
\tag{5}
\]

Indeed the `J` coefficient in `b_ac` is `-5 tau y_a J/6`;
the moving upper gate and lower feature both have coefficient
`-(5 tau/2)y_a S`. These retain the `1:3` ratio defining `K_a` in (2),
so they combine into `-(5 tau/2)F` rather than requiring its constituents
as separate columns. Also

\[
Bd_a=\sum_b\beta_bU_{ab},\qquad
Sd_a=\sum_b y_bU_{ab},\qquad U_{ab}=d_aH_b.
\]

Thus the last sum in (5) has only existing upper `U_ab` and lower `h_a`
factors, with scalar label-dependent coefficients. Dividing (5) by five
gives `[t^5]W`. **The p4 generator list can be precisely the p3 list.**
Changing the prescribed p-dependent ridge may change its normalized basis,
but does not change this raw-span statement.

## The new fourth-order hidden fields

Separate the known lower-label-degree pieces:

\[
h_{a,4}=\frac{7\tau^2}{12}V_a+T_a,\qquad
Y_{a,4}=\frac{7\tau^2}{12}R_a+E_a.
\tag{6}
\]

The required quartic-label lower field is

\[
T_a=\frac{y_a}{4}\ell_a^2W_0^*K_a
 +\frac{y_a}{4}\ell_a^2B_2^*(Sd_a)
 +m_aq_a^2.
\tag{7}
\]

To check the nonlinear lower term, the third coefficient of the lower
preactivation velocity is

\[
\frac{7\tau^2}{6}y_a\ell_aW_0^*(Sd_a)
 +y_a\ell_aW_0^*K_a+y_a\ell_aB_2^*(Sd_a)
 +y_am_aq_aW_0^*(Sd_a).
\]

Integrate by dividing by four, multiply by `ell_a` to compose tanh, and
add `m_a q_a^2/2` from the second composition derivative. The last displayed
velocity term contributes another `m_a q_a^2/2`, giving (7).

The quartic upper-preactivation field is

\[
E_a=W_0T_a+B_2V_a+\frac14\mathcal Fh_a.
\tag{8}
\]

This follows from `[t^4](Wh)=W_0h_{a,4}+B_2V_a+[t^4]W h_a`
and `[t^4]W=7 tau^2 D/24+F/4`. Every term in `T_a` is of degree four
and divisible by `y_a`. Therefore each `T_a` has only four possible
binary monomial coefficients, giving eight new lower generators in total.

## Sixth-order middle increment and its upper fields

Set

\[
N=\sum_b y_b\left(d_bE_b+\frac12d_b^{(2)}R_b^2\right),
\]
\[
K^{(5)}_a=\frac15d_aN+\frac13Jd_a^{(2)}R_a
             +Sd_a^{(2)}E_a+\frac12Sd_a^{(3)}R_a^2.
\tag{9}
\]

The fifth readout coefficient, obtained directly from its equation, is

\[
[t^5]c=\frac{\tau^4}{120}S+
         \frac{5\tau^2}{12}J+\frac{7\tau}{20}B+\frac15N.
\tag{10}
\]

Define the sextic-label tensor

\[
\mathcal G=\sum_a y_a\left\{
K^{(5)}_a\otimes h_a+K_a\otimes V_a+(Sd_a)\otimes T_a\right\}.
\tag{11}
\]

Then collecting the fifth velocity coefficient gives

\[
[t^5]\dot W=\frac{31\tau^4}{120}\mathcal D+
 \frac{13\tau^2}{4}\mathcal F+
 \sum_a\left(\frac{3\tau}{5}y_aBd_a+
                 \frac{9\tau}{4}\beta_aSd_a\right)\otimes h_a
 +\mathcal G.
\tag{12}
\]

One can verify the significant collection directly: the scalar-damping
terms multiplying `y_a J d_a` have coefficient `13 tau^2/12`; those
multiplying `y_a S d_a^(2) R_a` and `y_a S d_a tensor V_a` have coefficient
`13 tau^2/4`. They therefore again retain the existing collected `F`.
The middle-weight coefficient is exactly one sixth of (12).

All fields `K^(5)_a` are homogeneous binary quintics, hence have at most
six monomial coefficients each. No divisibility property for `E_a` is
needed for this count. The mixed terms `K_a tensor V_a` in (11) use
only the old p3 upper and lower spans; `Sd_a tensor T_a` uses old `U_ab`
and the eight new lower columns. Consequently twelve new upper columns
suffice.

For reference the two newly requested middle coefficients are

\[
[t^5]W=-\frac{\tau^3}{8}\mathcal D-\frac\tau2\mathcal F
 -\sum_a\left(\frac{y_a}{20}Bd_a+\frac15\beta_aSd_a\right)\otimes h_a,
\]
\[
[t^6]W=\frac{31\tau^4}{720}\mathcal D+\frac{13\tau^2}{24}\mathcal F
 +\sum_a\left(\frac\tau{10}y_aBd_a+
                  \frac{3\tau}{8}\beta_aSd_a\right)\otimes h_a
 +\frac16\mathcal G.
\tag{13}
\]

## Scalar contractions without retaining dense correction matrices

Equations (7)--(9) can be implemented without constructing `B_2` or `F`
as dense matrices. First,

\[
B_2^*(Sd_a)=\frac12\sum_b y_bh_b\,
                   E_2[S^2d_ad_b].
\tag{14}
\]

Let `H=tanh(sqrt(v)G)` and `d=1-H^2`. Independence and parity of the
two initialized upper probes give

\[
E_2[S^2d_ad_b]=\sum_{k=1}^2 y_k^2\gamma_{abk},
\]
\[
\gamma_{aaa}=E[H^2d^2],\qquad
\gamma_{aak}=\tau E[d^2]\quad(k\ne a),\qquad
\gamma_{abk}=E[H^2d]E[d]\quad(a\ne b).
\tag{15}
\]

The mixed `y_1y_2` term vanishes because the gate factor is even in each
independent centered upper coordinate.

For `h=tanh(G)`, `ell=1-h^2`, define the symmetric constants

\[
\lambda_{aa}=E[h^2\ell^2]\,E[d^2+H\phi''(\sqrt vG)],
\]
\[
\lambda_{ab}=vE[\ell^2]\,(E[d])^2\qquad(a\ne b).
\tag{16}
\]

Then

\[
\langle h_b,V_a\rangle_1=
\langle V_b,h_a\rangle_1=\frac12y_ay_b\lambda_{ab},
\]
\[
E_a=W_0T_a+\frac v4y_aK_a+
           \frac{3y_a}{8}\sum_b y_b^2\lambda_{ab}Sd_b.
\tag{17}
\]

Here is the adjoint check underlying (16). For a coefficient indexed by
`c`, move the actual adjoint across the pairing:

\[
\langle h_b\ell_a^2,W_0^*(H_cd_a)\rangle_1
=\langle W_0(h_b\ell_a^2),H_cd_a\rangle_2.
\]

The initialized forward field on the right is jointly Gaussian with
`Y_1,Y_2`; its covariance with `Y_j` is
`E_1[h_b ell_a^2 h_j]`, zero unless `j=b`. Gaussian integration by
parts therefore makes the right side

\[
E_1[h_b^2\ell_a^2]\,
 E_2[\partial_{Y_b}(H_cd_a)].
\]

This integration identity follows by integrating the Gaussian density
derivative; the test function and its first derivative are bounded here.
For `c!=b`, parity gives zero. For `c=b=a`, the derivative is
`d_a^2+H_a d_a^(2)`; for `c=b!=a`, it is `d_b d_a`. These are precisely
(16). Thus the moment reduction uses the adjoint law rather than
discarding its response correlations. All constants in (15)--(16) are
one-dimensional Gaussian expectations; a two-dimensional quadrature is
unnecessary for them.

## Concrete nested lists and implementation order

Use the current raw p3 columns unchanged. For p4 append nothing. For p5
append the following columns, fixing raw scales before normalization:

- Lower: `24 [y1^j y2^(4-j)] T_1`, for `j=4,3,2,1`, followed by
  `24 [y1^j y2^(4-j)] T_2`, for `j=3,2,1,0`.
- Upper: `120 [y1^j y2^(5-j)] K^(5)_1`, for `j=5,4,3,2,1,0`, followed
  by the same six coefficients of `K^(5)_2`.

The upper list is equivalently the six nonzero candidate coefficients of
`y_a K^(5)_a`, not seven unconstrained sextic coefficients. The factors
`24=4!` and `120=5!` follow the same derivative-based raw-scale convention
as the existing `L_ab=2![label coefficient]V_a` and
`C=3![label coefficient]K_a`. Their common nonzero scales do not change
the spans, but do affect a subsequently imposed fixed ridge.

| New dictionary index | Maximum middle-weight power | Lower generators | Upper generators | Total vectors | Free middle entries |
|---|---:|---:|---:|---:|---:|
| p3 | 4 | 6 | 12 | 18 | 72 |
| p4 | 5 | 6 | 12 | 18 | 72 |
| p5 | 6 | 14 | 24 | 38 | 336 |

An efficient builder computes the already available `S,V,R,J,K_a`,
applies `W_0^*` to the eight coefficient fields of the two `K_a`, then
forms the eight coefficients of `T_a` using (7), (14)--(15). Apply `W_0`
to those eight new lower fields, use (17) to form `E_a`, and collect (9).
Binary homogeneous coefficient arrays and short polynomial convolutions
avoid task-label evaluations and label interpolation. The extra dense
initialized actions are eight adjoint queries and eight forward queries;
their results can be batched as two matrix multiplications. Intermediate
fields need not become additional retained columns for the stated
middle-increment containment problem.

This differs from retaining every input and output needed for exact
full-state jet matching, and does not assert preservation of the initial
dense network. Finite-width evaluation of the population-derived fields
remains a candidate compressed representation, with finite empirical
moment discrepancies and ridge filtering treated separately.

## Exact algebra check and input boundary

The owned scratch
`data/generated/gradient_flow_probe_dictionary_20260921/p45_independent_derivation01/check_exact_coefficients.py`
uses exact symbolic arithmetic to multiply (4), the moving upper gate and
the lower activation series. The residuals for middle-velocity coefficients
one through five, the fourth lower-activation coefficient and the fourth
output coefficient are identically zero. Results are in
`exact_coefficients.json`; no training or numerical network experiment was
performed. These checks verify the displayed algebra, not population
regularity or generator independence.

Scientific input was limited to the assigned DERIVATION.md,
FACTORIZATION.md, ORDER_COUNTS.md and the supplied p3 new_dictionary.py.
The next-order expressions through (12) and the `(14,24)` count were
derived independently before receiving the supervisor's matching formula
message. The subsequent exchange checked the scalar contractions and
agreed raw-scale convention. No other p4/p5 implementation, study or
earlier finding was consulted.
