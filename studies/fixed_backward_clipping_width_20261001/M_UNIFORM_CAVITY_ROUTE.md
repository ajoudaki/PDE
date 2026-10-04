# Cap dependence of the smooth cavity estimates

2026-10-01. Scoped theoretical continuation. This note reads only the assigned
`SMOOTH_SETUP.md`, `SMOOTH_RESULT.md`, the complete `SMOOTH_CAVITY_ROUTE.md`,
`FITTING_AND_THRESHOLD.md`, and Sections 1--2 of
`SMOOTH_MEAN_MAP_ROUTE.md`. The required mathematical proof, conjecture,
and canonical-notation skills and their relevant references were read.
No other study, manuscript, numerical experiment, or Git operation is an
input. This file is the only owned output.

**Conclusion.** The existing finite-dimensional cavity argument has explicit
cap-dependent bounds of the form polynomial times `exp(C M)`, for a common
fixed activity bound and `M >= 1`. The Gaussian moment width threshold in
that argument can be independent of M. Its deterministic scalar reinsertion
comparisons can be made causal, at the cost of another exponential, so they
do not require an M-dependent reduction of activity. These are useful
ingredients for a growing-cap theorem; the final population comparison
still requires the coordinator's separate causal law-map argument.

This note does **not** prove a uniform-in-M cavity estimate. Replacing the
unbounded lower-carrier factors by Gaussian moments controls local Taylor
defects, but does not by itself control the state propagators or response
trace sensitivities. The exact missing uniform estimates are stated below.

## 1. Coordinates, prescribed histories, and the common activity bound

Retain the study's exact moment normalizations
`k_a = bar h_(a,0)/tau` and `v_a = -2 bar delta_(a,0)`. Let
`u_a = x_a/sqrt(d)`, `psi = sech^2`, and

\[
 F_M(\alpha,P)=M\tanh(P\psi(\alpha)/M).
\]

The prescribed-history cavity system has states `(A,w,(v_a),(k_a))` and

\[
\begin{aligned}
 \alpha_a&=Au_a,&h_a&=\tanh\alpha_a,\\
 z_a&=W_0h_a+m^{-1}\sum_bv_bK_{ba},&
 d_a&=F_M(z_a,w),\\
 P_a&=W_0^\top d_a+m^{-1}\sum_bk_bV_{ba},&
 \ell_a&=F_M(\alpha_a,P_a),\\
 \dot A&=-2m^{-1}\sum_a r_a\ell_a u_a^\top,&
 \dot w&=-2m^{-1}\sum_a r_a\tanh z_a,\\
 \dot v_a&=-2r_ad_a,&
 \dot k_a&=(\rho/\tau)(h_a-k_a).
\end{aligned}                                                    \tag{1}
\]

The supplied histories satisfy `|r_a| <= sqrt(m) rho`, `tau >= 1`,
`|K_ba| <= C`, `|V_ba| <= C s^3`, and

\[
 s(t)=\int_0^t\rho(u)\,du,\qquad S=s(\infty)\le S_0\le1.
\]

Their stated activity Lipschitz bounds are fixed independently of M.
All constants in this note can depend on the fixed data, these bounds,
the common positive label vector, and `S_0`. They do not depend on width,
physical time, or M unless displayed.

The fitting calculation in `FITTING_AND_THRESHOLD.md` uses
`|c_M(q)| <= |q|` and consequently gives the same deterministic small-label
threshold for every M, including the smooth cap. In particular, it gives
the common bound S on the original fitting event. For every prescribed
system (1), direct integration gives

\[
 \|w\|_\infty,\|d_a\|_\infty\le2s,
 \qquad \|v_a\|_\infty\le2\sqrt m\,s^2,
 \qquad \|k_a\|_\infty\le1.                                  \tag{2}
\]

Here `P_a` denotes the lower carrier. The unclipped upper derivative
`w psi(z_a)` is distinct from `d_a` throughout.

## 2. The derivative bound that isolates the dependence on M

For every fixed integer q, there are constants depending only on q such
that, for M >= 1,

\[
\begin{aligned}
 |\partial_\alpha^a F_M(\alpha,P)|&\le C_qM
                       &&(1\le a\le q),\\
 |\partial_\alpha^a F_M(\alpha,P)|&\le C_q|P|
                       &&(0\le a\le q),\\
 |\partial_\alpha^a\partial_P^b F_M(\alpha,P)|&\le C_q
                       &&(b\ge1,\ a+b\le q).
\end{aligned}                                                    \tag{3}
\]

The second line for a=0 is the elementary cap inequality. For positive a,
the expansion in `SMOOTH_CAVITY_ROUTE.md` writes each derivative as a finite
sum

\[
 M^{1-b}\psi(\alpha)^b Q(\tanh\alpha)
 x^j\tanh^{(b+j)}x,\qquad x=P\psi(\alpha)/M.
\]

For b=0, j>=1. Boundedness of `x^j tanh^(j)(x)` proves the first line.
Writing one x factor as `P psi(alpha)/M` instead proves the second line,
because `x^(j-1) tanh^(j)(x)` is bounded. For b>=1, `M^(1-b) <= 1`
and the same exponentially decaying derivatives prove the third line.

On the upper branch, `|w| <= 2S_0`; therefore every pure z derivative of
`F_M(z,w)` of fixed order is bounded by `C_q S_0`, and every derivative
with at least one w differentiation is bounded by `C_q`. These bounds are
independent of M. Thus the only growing scalar derivative in the dynamic
graph is a pure alpha derivative of the lower gated map.

This growth cannot be removed from a global deterministic scalar bound.
Choose a fixed alpha with `psi'(alpha) != 0` and choose
`P = M/psi(alpha)`. Then

\[
 |\partial_\alpha F_M(\alpha,P)|
 =M\,|\psi'(\alpha)/\psi(\alpha)|\,\operatorname{sech}^2(1),
\]

which is a positive constant times M. This is a counterexample to a
uniform deterministic derivative bound, not a counterexample to the
desired probabilistic theorem.

## 3. A sharper full-state Jacobian bound

Let `K_W = ||W_0||op`, and let L(t) be the ordinary state Jacobian of (1),
with all supplied histories held fixed. For fixed S_0,

\[
 \|L(t)\|_{\rm op}
 \le C\rho(t)\{M+1+K_W^2\}.                                  \tag{4}
\]

In particular, the M factor need not multiply `K_W^2`.

To verify (4), first differentiate the algebraic graph:

\[
\begin{aligned}
 \delta h_a&=\psi(\alpha_a)\odot\delta\alpha_a,\\
 \delta z_a&=W_0\delta h_a+m^{-1}\sum_b\delta v_bK_{ba},\\
 \delta d_a&=(F_M)_z(z_a,w)\odot\delta z_a
                 +(F_M)_w(z_a,w)\odot\delta w,\\
 \delta P_a&=W_0^\top\delta d_a
                         +m^{-1}\sum_b\delta k_bV_{ba},\\
 \delta\ell_a&=(F_M)_\alpha(\alpha_a,P_a)\odot\delta\alpha_a
                   +(F_M)_P(\alpha_a,P_a)\odot\delta P_a.
\end{aligned}                                                    \tag{5}
\]

The first term in the last line has operator norm at most CM and contains
no W factor. Every other term uses M-uniform scalar derivatives from (3).
The largest matrix product contains `W_0^T`, an upper gate derivative,
and `W_0`; its norm is bounded by `C S_0 K_W^2`. The remaining state
equations have fewer factors. Multiplication by their residual or clock
coefficients supplies `C rho(t)`. This proves (4).

For the fundamental solution `partial_t Phi(t,s)=L(t)Phi(t,s)`, it follows
that

\[
 \|\Phi(t,s)\|_{\rm op}
 \le \exp\{CS_0(M+1+K_W^2)\}.                                \tag{6}
\]

The same estimate holds for a cavity, and for the graph with a fixed
removed-row or removed-column forcing path. Such forcing shifts a carrier
or a preactivation, but does not change the global derivative bounds (3).

## 4. Fixed-order cavity, tagged, and trace constants

For every fixed finite collection of derivative orders and moment orders
used in Sections 4--5 and 8--12 of `SMOOTH_CAVITY_ROUTE.md`, its local
constants have a bound of the form

\[
 C_q(1+M)^{b_q}(1+K_W)^{b_q}
       \exp\{C_qS_0(M+1+K_W^2)\}.                            \tag{7}
\]

The exponent b_q is finite and independent of width and M. The dependence
on a bounded tagged-forcing amplitude is polynomial of a fixed order.
The assertion applies to the ordinary Euclidean reinsertion remainder,
its directly calculated tagged derivative, covariance root gradients,
normalized response-trace root gradients, and their finite smooth passive
outputs. It does not claim uniformity over derivative order q.

Here is why no further exponential is generated in these finite vector
calculations. Every derivative of the fixed finite graph is a sum of a
fixed number of products. Equation (3) bounds its scalar factors by a
polynomial in M; every initialized matrix factor contributes a power of
`1+K_W`. A tangent of any fixed order solves a linear equation with the
same homogeneous Jacobian L. Its source is a finite sum of products of
lower-order tangents and graph derivatives. Induction on the derivative
order, Duhamel's formula, and (6) therefore produce a polynomial times a
single exponential as in (7). The tangent size never replaces the
homogeneous coefficient L in Gronwall.

For the special row reinsertion calculation, each pure tangent coordinate
is a Gaussian projection of a cavity kernel row. Conditional on the
cavity, its fixed Lp norm is bounded by the corresponding kernel row norm
divided by sqrt(n), with constants of the form (7). Squaring coordinate
tangents and summing their squared defects therefore gives the same
`n^(-1/2)` ordinary Euclidean remainder as in the original proof.
Tagged products use Holder and this same bound. Gaussian quadratic-form
centering contributes `n^(-1/2)` times its trace/propagator constant.
Thus this step preserves the width exponent while making its cap
dependence explicit.

Likewise, a normalized response trace is a normalized trace of a fixed
product of output derivatives, Phi, and a source derivative. Its changed
factor is estimated in normalized Hilbert--Schmidt norm and all remaining
factors by (6)--(7). The factors `1/sqrt(n)` in its Gaussian root gradient
are unchanged. Row/column deletion differences are controlled in ordinary
Hilbert--Schmidt norm; their cap-dependent coefficients again satisfy (7).

For an operator cutoff `K_W <= K_0` with fixed K_0, every such local
constant is at most

\[
 E_1(M)=\exp\{C(1+M)\},                                      \tag{8}
\]

after increasing C for the finite collection of orders in use. Polynomial
factors in M have been absorbed using `log(1+M) <= M`.

## 5. Gaussian moments and the minimum width

The elementary net estimate already proved in the assigned cavity note
gives, for a sufficiently large fixed K_0,

\[
 \Pr(K_W>L)\le2e^{-nL^2/16}\qquad(L\ge K_0).
\tag{9}
\]

For fixed a,b, integration of this tail gives

\[
\begin{aligned}
 \mathbb E[(1+K_W)^b e^{aK_W^2}]&\le C_{a,b},\\
 \mathbb E[(1+K_W)^b e^{aK_W^2}\mathbf1_{K_W>K_0}]
                      &\le C_{a,b}e^{-cn},
\end{aligned}                                                    \tag{10}
\]

as soon as n exceeds a fixed number depending on a,b,K_0. For example,
requiring `n >= 32 a` makes the exponent beyond K_0 at most `-n L^2/32`;
a further fixed enlargement absorbs the polynomial.

For any fixed moment of (7), the coefficient a of `K_W^2` depends on its
moment/derivative order and S_0 but **not** on M, by (4). Therefore the
minimum width needed for these full-Gaussian finite-vector moments can
be chosen independent of M. Their values and their operator-exceptional
contributions satisfy respectively

\[
 E_1(M),\qquad E_1(M)e^{-cn},                                 \tag{11}
\]

with C increased as needed. This is sharper than applying the coarser
bound `C(M) rho(1+K_W^2)`, which needlessly makes the integrability width
threshold grow with M.

The same facts hold for matrices with a row or column zeroed and for the
removed Gaussian vector. The latter has uniformly bounded fixed moments
and exponential tails beyond a fixed norm cutoff. A fixed polynomial
factor in n from a tagged coordinate can be absorbed by decreasing c
and increasing the fixed width threshold.

Full-Gaussian Poincare can therefore be applied to the response and
covariance functionals exactly as in Section 12 of the assigned cavity
note. Their squared weak root gradients are integrable, so smooth cutoff
approximation gives fluctuations bounded by `E_1(M)/sqrt(n)`.
Restricting prescribed forced expectations to the original initialized
fitting event costs at most the same cap factor times its exponential
exceptional probability. No conditional Gaussian independence is used.

## 6. Coarse cavity law data and M-independent activity

On the fixed cavity operator cutoff, the complete covariance/response
data produced by the finite graph fit a deterministic coarse domain with
response-amplitude and regularity bound

\[
 B_M\le E_1(M).                                               \tag{12}
\]

The full deterministic expected tuple fits the same domain after its
constant is enlarged: averaging the outside-cutoff portion uses (11).
Initial lower covariance can be arbitrary admissible covariance, as in
the existing mean-map domain; it is not replaced by its population value
before comparison.

Some of these domain bounds need no M dependence at all. In normalized
Euclidean norm `||a||_n=||a||_2/sqrt(n)`, (2) gives

\[
 \|P_a\|_n\le C(K_Ws+s^3),\qquad
 \|\ell_a\|_n\le\|P_a\|_n.
\tag{13}
\]

In the activity clock, this gives

\[
 \|h'_a\|_n\le C(K_Ws+s^3),\qquad
 \|d'_a\|_n\le C(1+S_0^2K_W^2)
\tag{14}
\]

for the supplied coefficient Lipschitz bounds. For the second inequality,
differentiate `d=F_M(z,w)`, use `|F_w|<=1`, `|F_z|<=Cs`, and
`z'=W_0h'+m^{-1}sum_b(v'_b K_ba+v_b K'_ba)`. These equations verify
cap-independent covariance increment bounds on the cutoff. They also
give cap-independent amplitude and target-Lipschitz bounds for the
upper direct atom `n^(-1)sum_i (F_M)_z(z_ai,w_i)`.

The response densities and their target row regularity use the propagator
and therefore receive the coarse bound (12). The density includes its
prescribed residual factor; no derivative of that residual or of `r/rho`
is taken. For target regularity one differentiates the actual output/source
graph with its supplied coefficients held fixed, precisely as in the
existing response calculations. This uses only finitely many graph
derivatives and obeys (7).

The coarse domain is a container for the two tuples being compared. This
note does **not** assert that the full law map maps the entire coarse
domain to itself: its deterministic scalar derivative bounds may be
larger than B_M. Such an invariant-domain assertion is unnecessary for a
direct consistency comparison, but cannot silently be inferred from (12).

## 7. Reinsertion needs causality, not a shrinking activity threshold

The original row argument absorbs the feedback in its upper scalar z
equation using a smallness condition involving the trace bound. With the
coarse bound B_M, that absorption would impose an M-dependent threshold.
It can instead be replaced by Volterra Gronwall on the fixed activity
interval `[0,S_0]`.

The scalar upper law has the form

\[
 z_a(x)=\gamma_a(x)+\sum_b\int_0^xQ_{h,ab}(x,u)d_b(u)\,du
                 +m^{-1}\sum_bv_b(x)K_{ba}(x),                \tag{15}
\]

where `|Q_h| <= B_M`, `w` and `v` start at zero and are time integrals,
and `d=F_M(z,w)`. For two upper paths with identical input data except an
additive field error epsilon, the uniform upper derivatives from (3) give

\[
 \max_a|\Delta z_a(x)|
 \le\max_a|\epsilon_a(x)|
   +C(1+B_M)\int_0^x\sup_{v\le u}\max_a|\Delta z_a(v)|\,du.
\tag{16}
\]

For example, `Delta w(x)` is bounded by `C int_0^x |Delta z(u)|du`,
`Delta d(u)` by `C|Delta w(u)|+CS_0|Delta z(u)|`, and `Delta v(x)`
by the integral of `Delta d`. Substitution into (15) proves (16).
There is no instantaneous atom in Q_h. Thus (16) yields a comparison
factor `exp(C(1+B_M)S_0)` without assuming it is close to one.

The lower scalar law has

\[
 P_a(x)=\xi_a(x)+D_a(x)h_a(x)
    +\sum_b\int_0^xQ_{d,ab}(x,u)h_b(u)\,du
    +m^{-1}\sum_bk_b(x)V_{ba}(x).                             \tag{17}
\]

Its current atom D multiplies h inside the ordinary differential equation
for A; it does not create an algebraic equation for h at the same instant.
Using (3), the first difference of the lower state consequently obeys

\[
 \sup_{u\le x}|\Delta(A,k)(u)|
 \le C\int_0^x|\epsilon(u)|\,du
       +C(1+M+B_M)\int_0^x\sup_{v\le u}|\Delta(A,k)(v)|\,du.
\tag{18}
\]

The memory integrals have been bounded by their causal integrals, with
S_0<=1. Ordinary Gronwall applies for every fixed S_0. The same reasoning
applies to the directly computed tagged variation. Its homogeneous
equation is the scalar variational equation; its source contains the
already estimated state defect and finite lower-order variations.

For every fixed finite derivative order used here, these comparisons
and scalar derivative-measure envelopes can therefore be bounded by

\[
 E_2(M)=\exp\{\exp(C(1+M))\}.                                \tag{19}
\]

The first exponent arises from (16)--(18) with `B_M <= E_1(M)`.
Taking finitely many derivatives changes C and polynomial factors, not
the height of this bound. This statement is about scalar equations for
prescribed admissible law data; it is not the separate contraction or
Volterra comparison between two complete covariance/response maps.

The response sources at specified times are still handled as jumps and
regular tails. The instantaneous upper atom remains separated from the
past integral. Replacing contraction by (16)--(18) changes neither of
these conventions.

## 8. Consequence for the finite mean-map defect

Assume the deterministic scalar derivative-measure comparison from the
assigned mean-map route is used on the coarse input domain (12), with
the causal bounds (16)--(19) in place of its small-feedback absorption.
Then its finite-mesh derivative majorants and their continuum limits
have bounds E_2(M): the defining causal equations are the same, and each
finite-order variation has the same homogeneous equations just estimated.

The existing cavity proof then gives a complete prescribed-history mean
law defect at most

\[
 \frac{E_2(M)}{\sqrt n}+E_2(M)e^{-cn}.                         \tag{20}
\]

Indeed the finite coordinate/trace sources are `E_1(M)/sqrt(n)`;
scalar reinsertion and the deterministic covariance/response comparison
multiply them by at most E_2(M). Enlarging C absorbs the product. The same
argument applies to the passive prediction-velocity source, with the
additional factor rho(t), and to the key-contraction velocity.

To justify localization, keep the exact conditional Gaussian cavity law
on the cavity-measurable event `||W_0^c||op<=K_0`; this event does not
condition the removed Gaussian vector. Outside it, replace auxiliary
law data by one fixed admissible tuple. The finite source changes have
the bound (11), while the auxiliary scalar output/response envelopes
are at most E_2(M). Holder and the Gaussian exponential tail therefore
give the second term in (20), with c decreased if necessary. The
removed-vector cutoff is treated identically. The full deterministic
finite tuple can be used because its change from the cutoff mean is
already controlled by (11).

For every n above the M-independent Gaussian moment threshold,
`exp(-cn) <= C/sqrt(n)`. Thus (20) is at most `E_2(M)/sqrt(n)` after
enlarging C. Making this numerical error small requires an M-dependent
width, of course; it is different from the Gaussian integrability
threshold. For example a requirement that (20) be below a fixed positive
margin is satisfied by a width bounded by another double exponential
in M.

A separate complete-law comparison is still required to turn (20) into
distance from the own population. If that argument has the causal bounds

\[
 E_H(x)\le \delta+A_M\int_0^xE_D(u)\,du,
 \qquad E_D(x)\le\delta+A_ME_H(x),\qquad A_M\le E_2(M),
\]

then ordinary Gronwall gives a final constant at most a triple exponential
in M. This implication is algebraic: substitute the second inequality
into the first and use `exp(A_M^2 S_0)`. The causal bounds themselves are
the supervisor's separate law-map obligation, not proved in this note.

## 9. What a genuinely uniform moment replacement would need

The favorable local weighted estimate is exact. Let T_j and R_j denote
increments of alpha and P at coordinate j, and let Q_j be the quadratic
Taylor defect of F_M. Equation (3), integrated along the line segment,
gives uniformly in M>=1

\[
 |Q_j|\le C\{(|P_j|+|R_j|)|T_j|^2+|T_jR_j|+|R_j|^2\}.
\tag{21}
\]

Consequently, for a fixed p>=2, if jointly dependent carrier and tangent
coordinates satisfy

\[
 \sup_j\|P_j\|_{L^{2p}}\le C_p,
 \qquad
 \sup_j(\|T_j\|_{L^{4p}}+\|R_j\|_{L^{4p}})
                            \le C_p/\sqrt n,                 \tag{22}
\]

then Holder followed by Minkowski in L^(p/2) yields

\[
 \big\|\|Q\|_2\big\|_{L^p}
 \le\left(\sum_j\|Q_j\|_{L^p}^2\right)^{1/2}
 \le C_p/\sqrt n.                                            \tag{23}
\]

No independence between the factors in (22) is needed, and no maximum
over neurons is taken. This is a legitimate way to avoid logarithmic
losses for local defects. Fixed-time estimates can be integrated against
the deterministic activity envelope; temporal suprema require the
corresponding integrable derivative envelopes rather than an unproved
interchange of expectation and supremum.

However, (22) is not supplied uniformly in M by the current proof. Its
tangent estimate uses rows of Phi and their time derivatives. Replacing
the deterministic pure-alpha bound by `C|P_j|` makes these rows depend on
an unbounded diagonal carrier. Neither the normalized bound (13) nor
fixed marginal moments of P imply uniform moments of these propagator
rows jointly with P. Trace concentration likewise requires weighted
root sensitivities, not merely moments of the unperturbed carrier.

Even a diagonal Gaussian example illustrates the distinction. If
`P_j ~ N(0,1)` and `T_j(x)=n^(-1/2)exp(xP_j)`, each fixed coordinate
moment of T has the desired root-width scale uniformly in n, although
the operator norm of the diagonal propagator grows with the largest
P_j. A uniform proof may therefore exist without a uniform deterministic
operator bound. One must actually establish its coordinate or normalized
trace moment bounds for the coupled W_0/W_0^T dynamics.

The exact unresolved uniform obligations are: joint carrier/tangent
moments such as (22) for the full and cavity systems; corresponding
weighted tagged variations; and normalized response-trace root-gradient
moments with no M factor. Claiming these by replacing every deterministic
gate bound with an averaged Gaussian moment is circular, because the
carrier's Gaussian cavity representation itself uses those tangents.

## 10. Scope of the result

The cap-independent fitting activity, explicit finite-vector constants,
Gaussian width threshold, coarse-domain bounds, and causal reinsertion
comparisons above are derived here. They show that the probabilistic
local argument does not force the labels to decrease as M increases.
They do not supply the separate law-map estimate needed after (20).

They also distinguish three different claims: uniform fitting is already
available; a very slowly growing cap is compatible with the displayed
cap-dependent source bounds once the complete causal population
comparison is supplied; a full `O_P(n^(-1/2))` theorem uniform over M>=1
still needs the weighted tangent and trace estimates in Section 9.
No slower-rate counterexample for the actual model is claimed.
