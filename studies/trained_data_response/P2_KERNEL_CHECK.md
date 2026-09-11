# Conditional weighted coefficient stability for the raw finite program

Original report frozen on 2026-09-11 by the scoped `p2_kernel_check` agent.
This is an independent bounded author/checker report, not a promotion review.
Scientific inputs were only the assignment and the supervisor's clarification
of its raw-state/residual premise. No study history, other author's report,
book scientific material, code, experiments, or external scientific sources
were used. Required process inputs were `RESEARCH_WORKFLOW.md`, the
`solve-math-rigorously` and `investigate-conjectures` skills, and the latter's
research-contract and adversarial-audit references. The supervisor owns the
shared Git coordination; this agent performed no Git operation.

## Conclusion and precise conditional scope

The proposed discrepancy estimate closes. In fact, under the supplied premises,
one may take the law exponent to be **one**, without an interpolation loss:

\[
D_k\le C_M\left[e(\mathfrak q)+\mathfrak q+
                    \sum_{j<k}h_jD_j\right].                 \tag{1}
\]

Here \(\mathfrak q=\sum_b p_bd_b\), where
\(d_b=|u_b-v_b|+|y_b-z_b|\). The constant is independent of the number of
atoms, their positive masses, duplicate slots, and the mesh. It depends on the
fixed horizon, the temporary backward-row cap, and the supplied uniform raw
bounds. An auxiliary quantity that makes the proof transparent is

\[
A_i=\sup_{u\in S^1}\sum_{s<i,b}
  |\alpha^\lambda_{iu,sb}-\alpha^*_{iu,sb}|.                 \tag{2}
\]

The proof gives the causal bound

\[
A_i\le C_M\left[e(\mathfrak q)+\mathfrak q+
                    \sum_{j<i}h_jD_j\right].                 \tag{3}
\]

It then controls an auxiliary row of absolute upper-response differences;
taking expectations recovers (1). In particular, it is unnecessary to infer
response closeness from coefficient closeness by a Gaussian operator estimate.

This report proves a conditional finite-program estimate. It does not prove
the supplied raw-state convergence, the reference cap, the exact Gaussian
source construction, a neural-limit identification, or removal of the
temporary cap. The exact causal dependence in the question is essential:
\(\alpha_i\) uses only earlier \(Q\)-rows, and then \(\beta_i\) uses
\(F_i\) and earlier upper responses.

The raw-state premise is used in this explicit form, with
\(\varepsilon=e(\mathfrak q)\): at all relevant times, same-passive-input
differences of \(w,c,Z,Q,H,\delta\) have \(L^2\) norm at most
\(C\varepsilon\), and at matched active inputs they have norm at most
\(C(\varepsilon+d_b)\). Also

\[
|r^\lambda_{ib}-r^*_{ib}|\le C(\varepsilon+d_b).              \tag{4}
\]

The supervisor explicitly supplied (4) and the needed \(Z\) bound as
consequences/premises of raw convergence of \(w,K,c\), the common initial
operator, and the uniform raw bounds. A residual cap by itself would not
replace (4). No extra smallness of an individual normalized source error is
assumed.

## 1. Conventions and elementary causal estimate

Write \(a=(s,b)\), \(\mu_a=h_sp_b\), and let a star denote the matched
reference program. All sums are finite, \(h_s\ge0\), and
\(\sum_sh_s\le T\). Slots with \(h_s=0\) may be omitted from normalized
lower responses: their lower responses and all their later upper
coefficients are zero by the causal equations below. Their current formal
Gaussian coordinate is still retained. Equal inputs in different named slots
remain different formal coordinates, as required in the assignment.

Let \(R\) bound residuals, \(C_0\) bound \(|c_i|\) pathwise, and let the
supplied bound on \(\|w_i\|_2\) be fixed. Constants below may depend on
these bounds, \(M,T\), and finitely many bounded derivatives of \(\tanh\).
The same symbol \(C_M\) may denote larger such constants. The function
\(q\) continues to mean \(\tanh'\); the law distance is
\(\mathfrak q\).

We repeatedly use the following finite identity/inequality. If

\[
x_i\le b_i+\sum_{j<i}a_jx_j,\qquad a_j\ge0,
\]

and \(b_i\) is nonnegative and nondecreasing, expansion of the finite
triangular recursion gives

\[
x_i\le b_i\prod_{j<i}(1+a_j)
     \le b_i\exp\!\left(\sum_{j<i}a_j\right).              \tag{5}
\]

The first bound follows by induction, using
\(1+\sum_{j<i}a_j\prod_{t<j}(1+a_t)=\prod_{j<i}(1+a_j)\).
Thus (5) is valid for arbitrary nonnegative step sizes; it needs no small
maximum-step assumption.

All differentiations below are formal differentiations of the finite
smooth recursion, holding residuals, coefficients and covariance data fixed.
The displayed bounds prove integrability of the derivatives that are
subsequently averaged. No derivative is exchanged with a law-dependent
coefficient calculation.

## 2. A random envelope and weighted coefficient entries

On the temporary capped prefix,

\[
\sum_{a<i}|B_{iu,a}|+|\beta^{\rm cur}_{iu}|
\le M+2RC_0^2T=:L_M.                                      \tag{6}
\]

Since \(|H|\le1\), \(Q_i(u)\) is a centered Gaussian
\(\zeta_i(u)\) plus a pathwise bounded term of size at most \(L_M\).
Its Gaussian variance is
\(\mathbb E\delta_i(u)^2\le C_0^2\). Consequently, for every finite
\(p\) and \(a>0\),

\[
\sup_{i,u}\mathbb E|Q_i(u)|^p<\infty,
\qquad \sup_{i,u}\mathbb E e^{a|Q_i(u)|}<\infty.             \tag{7}
\]

For completeness, a centered scalar Gaussian of variance at most \(C_0^2\)
satisfies \(\mathbb E e^{a|G|}\le2e^{a^2C_0^2/2}\), by
\(e^{a|G|}\le e^{aG}+e^{-aG}\) and its Gaussian moment-generating
function. Adding a bounded random variable does not need independence.

Define, for a sufficiently large fixed constant \(C_M\),

\[
P=\exp\!\left(C_M\sum_{t<k}h_t
 \left[1+\sum_dp_d\bigl(|Q^\lambda_t(u_d)|+|Q^*_t(v_d)|\bigr)\right]
 \right).                                                  \tag{8}
\]

Every fixed moment of \(P\) is bounded uniformly in the mesh and data
cardinality. To see this, regard \(h_tp_d/T\) as weights and add a dummy
zero entry of weight \(1-\sum_th_t/T\). Convexity of the exponential
bounds the exponential of the weighted sum by the weighted sum of
exponentials. Apply (7), also to the sum of the two absolute Gaussian terms
by Cauchy--Schwarz. This proves the asserted moment bound without any
independence between times, inputs, or the two programs. Increasing the
constant in (8) preserves this property.

For \(\mu_a>0\), define the vector response

\[
\ell_i^a={1\over\mu_a}\,
                {\partial w_i\over\partial\zeta_a},
\qquad \ell_i^a=0\quad(i\le s).
\]

Put \(q_{td}=q(w_t\cdot u_d)\), with the corresponding convention for
\(q'_{td}\). Direct differentiation gives the exact identity

\[
\begin{split}
\ell_i^a={}&-2r_aq_a u_b\,\mathbf 1_{s<i}\\
&-2\sum_{t<i,d}\mu_{td}r_{td}u_d\left[
 q'_{td}Q_t(u_d)(u_d\cdot\ell_t^a)
 +q_{td}\beta^{\rm cur}_{td}q_{td}(u_d\cdot\ell_t^a)\right.\\
&\hspace{48mm}\left.
 +q_{td}\sum_{j<t,c}B_{td,jc}q_{jc}(u_c\cdot\ell_j^a)
 \right].                                                  \tag{9}
\end{split}
\]

The first line is the direct derivative of the named source in \(Q_s(u_b)\).
It is present once, even if another named slot has the same input.

Bound the gates, residuals and input norms, use (6), and take the maximum of
\(|\ell_j^a|\) over \(j\le i\). Equation (9) is bounded by (5) with
\(a_t=C_Mh_t[1+\sum_dp_d|Q_t(u_d)|]\). After increasing the constant
in (8), this yields the simultaneous pathwise bound

\[
\sup_{i\le k,a:i>s}|\ell_i^a|\le C_MP.                    \tag{10}
\]

It follows immediately that

\[
|\alpha_{iu,a}|
=\mu_a\left|\mathbb E[q(w_i\cdot u)u\cdot\ell_i^a]\right|
\le C_M\mu_a,
\qquad |F_{iu,a}|\le C_M\mu_a.                             \tag{11}
\]

Only the all-moment envelope for \(Q\), not a subGaussian bound for \(w\),
was needed here.

We next justify a pointwise entry estimate for the backward coefficients.
This is needed later: an absolute row cap alone would not attach the
original weights to errors at badly matched historical inputs.

For an upper source \(a=(s,b)\), set

\[
V_i^a=\partial_{\xi_a}c_i,\qquad
G_i^a(u)=\partial_{\xi_a}Z_i(u),\qquad
R_i^a(u)=\partial_{\xi_a}\delta_i(u).
\]

At active inputs the exact equations are

\[
\begin{split}
G_i^a(u_d)&=\mathbf1_{i=s,d=b}
                    +\sum_{j<i,c}F_{id,jc}R_j^a(u_c),\\
V_i^a&=-2\sum_{j<i,c}\mu_{jc}r_{jc}q(Z_j(u_c))G_j^a(u_c),\\
R_i^a(u)&=q(Z_i(u))V_i^a+c_iq'(Z_i(u))G_i^a(u).              \tag{12}
\end{split}
\]

For a passive current output, the first direct term is its own named current
source, and is zero for every past source. All current source rows below are
compared by that naming correspondence.

Sum absolute values over sources and take the supremum over output inputs.
Writing \(g_i,v_i,r_i^{\rm resp}\) for these three row bounds, (11)--(12)
give

\[
g_i\le1+C_M\sum_{j<i}h_jr_j^{\rm resp},\quad
v_i\le C_M\sum_{j<i}h_jg_j,\quad
r_i^{\rm resp}\le C_M(v_i+g_i).
\]

The double time sum is at most \(T\sum_{j<i}h_jr_j^{\rm resp}\).
Equation (5) therefore gives a deterministic bound \(C_M\) for all three
rows. For one past source, the sole current impulse at time \(s\) has size
at most \(C_M\), and its first appearance at a later time has the factor
\(\mu_a\), through either \(F_{iu,a}\) or the update of \(c\).
Applying the same inequalities with the impulse isolated gives

\[
|V_i^a|+|G_i^a(u)|+|R_i^a(u)|\le C_M\mu_a\qquad(i>s).       \tag{13}
\]

More explicitly, for \(i>s\) the maximum past-source response satisfies
\(x_i\le C_M\mu_a+C_M\sum_{s<j<i}h_jx_j\); (5) proves (13).
Thus, since \(\beta_{iu,a}=\mathbb ER_i^a(u)\),

\[
|\beta_{iu,a}|+|B_{iu,a}|\le C_M\mu_a.                     \tag{14}
\]

There is no same-node circularity: (10)--(11) for node \(i\) use capped
\(Q_t\) only for \(t<i\), after which (12) computes the upper row at
\(i\).

## 3. Uniform passive-input regularity

Within either program, (10), the bound on \(\|w_i\|_2\), and
Cauchy--Schwarz give

\[
|\alpha_{iu,a}-\alpha_{iv,a}|\le C_M\mu_a|u-v|.
\]

Indeed, the integrand difference divided by \(\mu_a\) is at most
\(C|u-v|(1+|w_i|)|\ell_i^a|\); its expectation is bounded using
\(\|w_i\|_2\) and \(\|P\|_2\). Also
\(\|H_i(u)-H_i(v)\|_2\le\|w_i\|_2|u-v|\). Therefore

\[
|F_{iu,a}-F_{iv,a}|\le C_M\mu_a|u-v|.                     \tag{15}
\]

The supplied Gaussian covariance rule gives
\(\|\xi_i(u)-\xi_i(v)\|_2=\|H_i(u)-H_i(v)\|_2\).
The boundedness of \(\delta\), (15), and \(\sum_a\mu_a\le T\)
then imply

\[
\|Z_i(u)-Z_i(v)\|_2\le C_M|u-v|.                          \tag{16}
\]

For a past source, the \(G\)-difference in (12) is bounded pathwise by
\(C_M\mu_a|u-v|\): isolate its current impulse at time \(s\), use
(15) for its factor \(F_{iu,a}\), then use (13) for all later terms.
Combining this observation with (13), (16), and bounded Lipschitz gates gives

\[
\mathbb E|R_i^a(u)-R_i^a(v)|\le C_M\mu_a|u-v|.             \tag{17}
\]

The current derivative is
\(\kappa_i(u)=c_iq'(Z_i(u))\), and
\(\mathbb E|\kappa_i(u)-\kappa_i(v)|\le C_M|u-v|\).
Summing (17) shows that both the coefficient row and the row of absolute
upper-response differences are uniformly Lipschitz in the passive input.
This applies in particular to the reference program at its unmatched
passive inputs; it does not identify the formal coordinates of duplicate
slots.

Two useful consequences are the active-output coefficient estimates

\[
\begin{split}
|\beta^{{\rm cur},\lambda}_{td}
       -\beta^{{\rm cur},*}_{td}|&\le D_t+C_Md_d,\\
\sum_{j<t,c}|B^\lambda_{td,jc}-B^*_{td,jc}|
 &\le D_t+C_M(\varepsilon+\mathfrak q+d_d).                 \tag{18}
\end{split}
\]

To verify the second line, first compare the beta rows at identical passive
input \(u_d\), using \(D_t\), and then move the reference passive input
to \(v_d\), using (17). For the residual-covariance part of \(B\), each
entry difference is at most
\(C\mu_{jc}(\varepsilon+d_d+d_c)\): use (4), boundedness of
\(\delta\), and the supplied active-pair \(L^2\) bound. Summing its
original weights proves (18).

## 4. Lower-response comparison with the source distance retained

Let

\[
b_{td}=|r^\lambda_{td}-r^*_{td}|+d_d+|w^\lambda_t-w^*_t|
                                     +(1+|w_t^*|)d_d.
\]

The raw premise and the uniform \(L^2\) bound on \(w\) imply

\[
\|b_{td}\|_2\le C(\varepsilon+d_d).                        \tag{19}
\]

By Lipschitzness of \(q,q'\), their active-input differences, and the
differences of the corresponding input-vector factors, are bounded by
\(Cb_{td}\). Define the nonnegative forcing

\[
\begin{split}
J_{td}={}&|Q^\lambda_t(u_d)-Q^*_t(v_d)|
 +(1+|Q^*_t(v_d)|)b_{td}\\
&+D_t+\varepsilon+\mathfrak q+d_d
 +\sum_{j<t,c}\mu_{jc}b_{jc}.                              \tag{20}
\end{split}
\]

Every term in (20), multiplied by \(P^2\), has controlled expectation:

\[
\mathbb E[P^2J_{td}]
 \le C_M(D_t+\varepsilon+\mathfrak q+d_d).                  \tag{21}
\]

Here is the product justification. For any random \(X\) with an available
\(L^2\) error bound,

\[
\mathbb E[P^2|X|]\le\|X\|_2\|P^2\|_2,
\quad
\mathbb E[P^2|Q^*_t(v_d)||X|]
 \le\|X\|_2\|P^2Q^*_t(v_d)\|_2.
\]

The final norm is at most
\(\|P^2\|_4\|Q^*_t(v_d)\|_4\), which is uniformly bounded by
(7)--(8). Apply these inequalities with \(X=b_{td}\), and with the
\(Q\)-difference using the first inequality. For the history term in
(20), sum (19) with \(\mu_{jc}\), obtaining at most
\(CT(\varepsilon+\mathfrak q)\). This proves (21). It never asserts
that a product of two \(L^2\) variables belongs to \(L^2\), and it does
not require independence between an error and its propagator.

For a source \(a=(s,b)\), let
\(x_i^a=\max_{j\le i}|\ell_j^{a,\lambda}-\ell_j^{a,*}|\).
Subtract (9) between the two programs. Transport the response difference
with the lambda coefficients, and put all factor differences against the
reference response. Bounded gates, (6), (10), (14), and (18) give

\[
\begin{split}
x_i^a\le{}&C_Mb_{sb}
 +C_M\sum_{t<i}h_t
       \left[1+\sum_dp_d|Q^\lambda_t(u_d)|\right]x_t^a\\
&+C_MP\sum_{t<i}h_t\sum_dp_dJ_{td}.                        \tag{22}
\end{split}
\]

To account explicitly for the terms in this subtraction:

* The direct pulse difference is bounded by \(Cb_{sb}\).
* A factor difference in the \(q'Q(u_d\cdot\ell_t)\) term is bounded
  by \(CP[|\Delta Q_{td}|+(1+|Q^*_{td}|)b_{td}]\).
* The current beta term contributes \(CP[b_{td}+D_t+d_d]\).
* A difference in the historical \(B\)-row contributes
  \(CP[D_t+C_M(\varepsilon+\mathfrak q+d_d)]\) by (18).
* A historical gate/input difference under the reference \(B\)-row is
  bounded by \(C_MP\sum_{j<t,c}\mu_{jc}b_{jc}\), using (14).
* Differences in exterior residual/input factors contribute
  \(C_MP(1+|Q^*_{td}|)b_{td}\).

The remaining terms are response differences. The current-time terms carry
\(C(1+|Q^\lambda_{td}|)x_t^a\); the historical terms are bounded by
\(C\sum|B^\lambda_{td,jc}|x_t^a\) because \(x_t^a\) is a running
maximum. This proves exactly the transport term in (22). Taking the running
maximum causes no extra maximum over Gaussian rows: all forcing terms in
the right side of (22) are nonnegative and accumulate with time.

Use (5) in (22); the forcing is nondecreasing in \(i\). After increasing
the constant in (8),

\[
x_i^a\le C_MP b_{sb}
               +C_MP^2\sum_{t<i}h_t\sum_dp_dJ_{td}.
\]

Equations (19), (21), and Cauchy--Schwarz now give

\[
\mathbb E x_i^a\le C_M\left[
 \varepsilon+d_b+\mathfrak q+\sum_{t<i}h_tD_t\right].       \tag{23}
\]

The \(d_b\) term in (23) is not uniformly small and has not been dropped.
It is the precise source-slot error that must be averaged with its original
weight. For a fixed identical passive output \(u\), use

\[
\alpha_{iu,a}=\mu_a\mathbb E[q(w_i\cdot u)u\cdot\ell_i^a].
\]

The difference of the terminal gate contributes at most
\(C_M\mu_a\varepsilon\), by the \(L^2\) raw error and (10).
The response difference contributes \(\mu_a\mathbb E x_i^a\).
Consequently

\[
|\Delta\alpha_{iu,a}|
 \le C_M\mu_a\left[\varepsilon+d_b+\mathfrak q
                                     +\sum_{t<i}h_tD_t\right].
\]

Sum over \(a=(s,b)\), using
\(\sum_a\mu_a\le T\) and
\(\sum_a\mu_ad_b\le T\mathfrak q\). This is (3).
It also shows why dividing first and taking a uniform small-error supremum
over source slots would be an invalid replacement for this argument.

## 5. Upper-response comparison and elimination of its auxiliary row

Define the nonnegative deterministic auxiliary error

\[
E_i=\sup_u\left[
 \sum_{a<i}\mathbb E|R_i^{a,\lambda}(u)-R_i^{a,*}(u)|
       +\mathbb E|\kappa_i^\lambda(u)-\kappa_i^*(u)|\right]. \tag{24}
\]

The formal current coordinates in the final term are paired by name.
The triangle inequality implies \(D_i\le E_i\). Equations (17) and its
current-coordinate version imply that the analogous row at active pair
\((u_b,v_b)\) is bounded by \(E_i+C_Md_b\).

At the same passive input, (4), boundedness of \(H\), and the raw
\(L^2\) errors give

\[
\sum_{a<i}|F^\lambda_{iu,a}-F^*_{iu,a}|
                  \le A_i+C_M(\varepsilon+\mathfrak q).   \tag{25}
\]

Each Gram/residual entry difference divided by \(\mu_a\) is at most
\(C(\varepsilon+d_b)\), so (25) retains the original weights.

Let \(N_i\) be the supremum over identical passive inputs of the expected
absolute row difference of \(G_i\). The current direct source term cancels
identically; only past terms need to be summed. Subtract the first equation
of (12), use (25) times the deterministic full response-row bound from
Section 2, then use \(|F^*_{iu,jc}|\le C_M\mu_{jc}\) for the response
differences. This gives

\[
N_i\le C_M\left[A_i+\varepsilon+\mathfrak q
                         +\sum_{j<i}h_jE_j\right].         \tag{26}
\]

For an active matched pair, its \(G\)-row difference is at most
\(N_i+C_Md_b\). This follows directly from (15) and the deterministic
upper-response row bound; it also follows from the argument used for (17).

Let
\(W_i=\sum_{a<i}\mathbb E|V_i^{a,\lambda}-V_i^{a,*}|\).
Subtract the second equation of (12). The residual and gate differences
are multiplied by a deterministically bounded full \(G\)-row, while the
remaining term is the active \(G\)-row difference. Thus

\[
W_i\le C_M\sum_{j<i}h_j[\varepsilon+\mathfrak q+N_j]
\le C_M\left[\varepsilon+\mathfrak q+
                   \sum_{j<i}h_j(A_j+E_j)\right].          \tag{27}
\]

For the second inequality insert (26) and interchange the two finite time
sums; their outer time weight is at most \(T\). No stochastic product
estimate is needed here because the differentiated upper rows have the
deterministic bounds proved in Section 2.

Finally subtract the last equation of (12). Its gate and \(c\)-factor
differences are bounded in expected absolute value by \(C\varepsilon\)
at the same passive input, using the supplied \(L^2\) differences and
bounded Lipschitz gates. The remaining terms are bounded by \(W_i+N_i\).
The current-coordinate difference in (24) is also at most
\(C\varepsilon\). Equations (26)--(27) yield

\[
E_i\le C_M\left[\varepsilon+\mathfrak q+A_i
                       +\sum_{j<i}h_j(A_j+E_j)\right].     \tag{28}
\]

For clarity, (28) can be solved without assuming that \(A_i\) is monotone.
If \(E_i\le C a_i+C\sum_{j<i}h_jE_j\), finite iteration gives

\[
E_i\le Ca_i+C^2\sum_{j<i}h_ja_j
                         \prod_{j<t<i}(1+Ch_t).
\]

Take
\(a_i=\varepsilon+\mathfrak q+A_i+\sum_{j<i}h_jA_j\).
The product is at most \(e^{CT}\), and

\[
\sum_{j<i}h_ja_j
 \le T(\varepsilon+\mathfrak q)
                        +(1+T)\sum_{j<i}h_jA_j.
\]

Consequently

\[
E_i\le C_M\left[\varepsilon+\mathfrak q+A_i
                              +\sum_{j<i}h_jA_j\right].    \tag{29}
\]

Insert (3) into (29). Interchanging finite sums once more gives

\[
\sum_{j<i}h_j\sum_{t<j}h_tD_t
                       \le T\sum_{t<i}h_tD_t.
\]

Since \(D_i\le E_i\), this proves (1), with the claimed causal dependence.

## 6. Checks, limitations, and exact bottleneck removed

The derivation covers zero time increments, arbitrary positive atom masses,
arbitrarily many duplicates, and singular Gaussian covariance matrices.
Formal named-coordinate differentiation, rather than differentiation only
along the Gaussian support, is indispensable for the stated impulse rules.
No inverse covariance matrix occurs anywhere.

The only Gaussian facts used are the supplied covariance identity and the
elementary scalar Gaussian exponential-moment formula. No Gaussian
\(L^p\) operator bound, operator norm conversion, or independence across
program times was assumed. The lower response argument uses a random
propagator with every fixed moment and tests it against the supplied
\(L^2\) errors. It never upgrades bounded \(L^2\) factors to a bounded
\(L^2\) product. The upper response argument is easier because its full
differentiated rows are bounded pathwise by deterministic constants.

The main potential obstruction was a historical gate error in the lower
tangent recursion, multiplied by a backward coefficient. A mere absolute
row bound on beta does not average a bad atom with its own mass. Equation
(14), derived causally from the lower alpha-entry bound and the exact upper
source equations, repairs precisely this point. Each direct lower pulse
still carries the individual distance \(d_b\), which only disappears
after summation with \(h_sp_b\).

This report is a complete conditional argument for (1)--(3), with an
internal algebraic/inequality check by its author. It has not undergone an
independent full-candidate review. The stronger research claims listed in
the opening scope remain supplied premises or open work, rather than
conclusions of this report.
