# An explicit width remainder for the all-time response-memory theorem

2026-10-01. This note records a quantitative extension of the current paper's all-time theorem. It does not change the network, the moment closure, or the clock. The original qualitative width remainder can be replaced by an explicit, very conservative logarithmic rate. A polynomial rate in width remains open in the general nonlinear setting.

The proof is split between this statement, `PROGRAM_RATE_ROUTE.md` (quantitative Gaussian conditioning), `PROGRAM_RATE_ADDENDUM.md` (the physical proxy and its exact consistency error), and `DAMPED_TRANSFER.md` (all-time comparison). `PROGRAM_RATE_CHECK.md` records a separate internal reconstruction. These are research results, not a promoted manuscript revision or an external review.

## 1. Setting and statement

Fix input dimension d, a finite training set of m pairs (x_a,y_a), and L>=2 hidden layers. For common width n write

\[
h_a^{(1)}=\phi_1(W^{(1)}x_a/\sqrt d),\qquad
h_a^{(\ell)}=\phi_\ell(W^{(\ell)}h_a^{(\ell-1)}),\qquad
f_a=n^{-1}w^Th_a^{(L)}.
\]

Set r_a=f_a-y_a and rho=(m^{-1}sum_a r_a^2)^{1/2}. The canonical dense gradient flow is

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}x_a^T/\sqrt d,
\quad
\dot W^{(\ell)}=-\frac2{nm}\sum_a r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T,
\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)},
\]

where delta is the usual backward response without the residual. Initialize the first matrix with independent N(0,1) entries, the other hidden matrices with independent N(0,1/n) entries, and w(0)=0. All matrices are independent initially and are reused with their actual transposes.

Use exactly the paper's autonomous q-mode response-memory closure: its own responses and residual, residual-RMS clock dot(tau)=rho with tau(0)=1, constant initial forward prefix, zero backward prefix, and the original W_0 retained. In particular, the clock is not the time derivative of loss. Every activation is C^1 with a globally bounded, globally Lipschitz derivative. Activation values need not be bounded. Assume the limiting initial last-feature Gram satisfies

\[
\Gamma_{w,\infty}(0)\succeq2\lambda I_m,\qquad\lambda>0,
\]

and the fixed label RMS Y is at most the sufficiently small width- and order-independent threshold Y_* in the paper. These are the hypotheses of the current all-time theorem; no new concentration, covariance-gap, clipping, or feature-freezing hypothesis is imposed.

For physical parameters use

\[
d_n(\widehat\theta,\theta)
=n^{-1/2}\|\widehat W^{(1)}-W^{(1)}\|_F
+\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W^{(\ell)}\|_F
+n^{-1/2}\|\widehat w-w\|_2.
\]

Let f_infinity be the deterministic dense population predictor identified by the paper. For any fixed test law mu with finite second moment define

\[
\mathcal E_\mu(g,f)=
\left(\int\sup_{t\ge0}|g(t,x)-f(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

**Theorem (explicit width remainder).** There are constants C,K,c>0, and a sufficiently large fixed width threshold, such that, with

\[
\omega(q)=q^{-2}\exp\{K\sqrt{\log(e+q)}\},\qquad
r_n=[\log(e^e+n)]^{-1/512},
\tag{1}
\]

the following conclusions hold for all widths above that threshold.

1. On an event of probability at least 1-C n^{-c}, the dense flow and all closure orders exist, fit exponentially, have convergent parameters, and simultaneously satisfy

\[
\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t))
\le C\omega(q)+C r_n\qquad(q\ge1).
\tag{2}
\]

2. For each fixed mu as above, on a common event of probability at least 1-C_mu r_n, simultaneously for every q>=1,

\[
\boxed{\mathcal E_\mu(\widehat f_{n,q},f_\infty)
\le C_\mu\omega(q)+C_\mu r_n.}
\tag{3}
\]

The dense predictor itself satisfies E_mu(f_{n,D},f_infinity)<=C_mu r_n on an event with the same probability bound. Every fixed bounded input domain also admits the corresponding uniform supremum over both input and time; its exceptional probability can be bounded by C_X n^{-c} after decreasing c.

Constants and the width threshold may depend on fixed depth, dimension, training data, activation bounds, the Gram margin, and the small-label choice. Test constants additionally depend on mu through its second moment, or on the bounded domain. They do not depend on n,q, or physical time. This is not a depth-uniform statement. The all-time bound includes the limiting fitted functions.

The exponent 1/512 is a deliberately conservative common choice, not an estimate of the sharp exponent. In particular, (3) is not a claim of n^{-1/2} sampling accuracy. The statement is high probability; it does not control unconditional error moments on the exceptional initialization event.

## 2. What must be quantified

The existing theorem's proof already gives

\[
D_{n,q}\le C\omega(q)+C\Phi(a_n),\qquad
\Phi(u)=u\exp\{K\sqrt{\log(e+1/u)}\},\quad\Phi(0)=0.
\tag{4}
\]

Here a_n is the positive excess, uniformly over integer cutoffs M, of the integrated dense backward-carrier tail

\[
Z_n(M)=\int_0^\infty\rho_D(t)
\sum_\ell\max_a\|k_{D,a}^{(\ell)}(t)
1_{|k_{D,a}^{(\ell)}(t)|>M}\|_2/\sqrt n\,dt
\]

above a fixed envelope C exp(-cM^2). The carriers are w at the top and W^T delta at lower layers. Choose the constants in that envelope once, sufficiently large/small as necessary; the original theorem permits this choice.

For predictions the width remainder is **not just** C_mu Phi(a_n). It additionally contains

\[
d_{n,\mu}=\mathcal E_\mu(f_{n,D},f_\infty).
\tag{5}
\]

The proof below quantifies both (4) and (5). Its foundational inputs from the current paper are: the common physical tube and Gram gap; exponential dense and all-order closure fitting; bounded total residual activity and physical parameter speed C rho; common bounded population initialized operators and their actual adjoints; the exact finite Gaussian conditioning identity; and uniform Gaussian marginal carrier tails for the original population Euler references. No quantitative finite-width carrier concentration is assumed among those inputs.

## 3. Quantitative Gaussian conditioning without an original query gap

Consider an original population Euler reference with N elementary instructions, all population feedback coefficients kept at their original deterministic values. In a proof-only copy, clip every training carrier product at magnitude N and add a fresh independent Gaussian input of amplitude epsilon=exp(-N^2) at every initialized-matrix query, in both orientations. These modifications are not applied to the trained network or closure.

The original population carrier tails and the common operator bounds give population L2 bias at most

\[
(CN^2)^{N+1}(e^{-N^2}+Ce^{-cN^2})\le Ce^{-c'N^2}.
\tag{6}
\]

All clipped coordinate instructions are globally Lipschitz with constant at most CN^2. Their crude RMS bound is B=(CN^2)^{N+1}. Every new query has a fresh component of variance epsilon^2 orthogonal to all previous queries. For a query Gram of size p<=N, its determinant is at least epsilon^{2p} and its trace at most pB^2. Therefore

\[
\lambda_{\min}(G_p)\ge\frac{\epsilon^{2p}}{(pB^2)^{p-1}}
\ge e^{-CN^3}.
\tag{7}
\]

This is a derived gap of the proof reference, not an assumption about the unmodified network. Its Gaussian innovation standard deviation is also at least epsilon.

For previous constraints WV=Y and W^T U=Q, conditional Gaussian projection gives the next actual answer exactly as

\[
Y\alpha_n+U\beta_n+\sigma_nP_{U^\perp}g,
\]

where alpha_n and beta_n are the query-Gram regression coefficients and g is a fresh standard Gaussian vector. Its scalar reference uses deterministic population coefficients and the same Gaussian coordinates. Reference tuples are iid across coordinates within a layer; the actual trained neurons are not asserted independent.

The Gram bounds give regression coefficients at most exp(CN^3) and fourth moments at most exp(CN^4). Chebyshev bounds every required empirical pairing and squared soft-tail test to tolerance n^{-1/4}, with total failure at most exp(CN^4)n^{-1/2}. Conditional projection noise has expected normalized squared norm at most N/n and obeys the same budget. Resolvent subtraction of the empirical inverse Grams then gives the chronological coupling recurrence

\[
e_{j+1}\le e^{CN^3}(e_j+n^{-1/4}).
\]

The innovation floor epsilon allows a Lipschitz variance-to-standard-deviation comparison, so a square-root loss does not recur at every step. Induction, stopped before any empirical Gram loses half its gap, proves

\[
e_N\le e^{CN^5}n^{-1/4},\qquad
\Pr(\text{failure})\le e^{CN^5}n^{-1/2}+Ce^{-cn},
\tag{8}
\]

provided log n>=CN^5. Empirical tail norms lose only a final square root, costing exp(CN^5)n^{-1/8}. The complete conditioning, stopping, and empirical-test proof is in `PROGRAM_RATE_ROUTE.md`, Sections 1–5; the independent filtration check is in `PROGRAM_RATE_CHECK.md`, Sections 1–3.

## 4. A physical proxy and bounded amplification over all time

At K Euler nodes on [0,T], reconstruct actual finite proxy weights from the modified reference responses and the original population residuals. Expand every learned matrix action into its rank-one sum. Empirical contraction errors in those sums carry coefficients h rho_j, whose total is bounded. Thus this proxy starts at the actual finite initialization, lies in a fixed physical tube, and its recomputed forward fields and residuals agree with the oracle nodes to an explicit error

\[
\xi\le e^{CN^5}n^{-1/8}+Ce^{-cN^2}.
\]

Backward recomputation at a comparison cutoff R costs C[(1+R)xi+exp(-cR^2)]. The comparison cutoff R is distinct from the much larger clipping cutoff N. These exact forward and reverse action identities are (A11)–(A21) of `PROGRAM_RATE_ADDENDUM.md`.

Interpolate the proxy parameters affinely and set E_p=dot(theta_p)-F(theta_p). Its segment displacement is at most Ch rho_j. Retaining the residual factors in the update subtraction gives

\[
\int_0^T\|E_p\|\le
C[(1+R)h+e^{-cR^2}+(T+1+R)\xi],\qquad
\int_0^T\rho_p\le C+CT\xi.
\tag{9}
\]

The proxy's current backward-carrier tails, not just its stored oracle fields, satisfy

\[
\int_0^T\rho_p H_p(R,t)\,dt
\le C[e^{-cR^2}+(1+R)(h+\xi)].
\tag{10}
\]

To compare it to the dense flow let u=r_D-r_p. The exact residual subtraction is

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\tag{11}
\]

The actual dense Gram supplies the positive gap. A proxy Gram gap is unnecessary. Gate subtraction, using only proxy carrier tails, bounds the Gram difference by C[(1+R)d_n+H_p]. Integrating the damped norm inequality in (11), and then subtracting the parameter updates with r_p left in the response-change terms, yields

\[
\sup_{t\le T}d_n(\theta_D(t),\theta_p(t))
\le Ce^{CR}\left[\int_0^T\|E_p\|
+\int_0^T\rho_pH_p\right]
\tag{12}
\]

when T xi<=1. The amplification is exp(CR), independent of physical T, because the residual activity in (9) is bounded. Combining (9)–(12) gives

\[
\sup_{t\le T}d_n(\theta_D,\theta_p)
\le Ce^{CR}[(1+R)h+e^{-cR^2}+(T+1+R)\xi].
\tag{13}
\]

The same argument on the common population Hilbert spaces, with xi=0, compares the original population Euler interpolation with the exact dense population flow. Full derivations of all source terms and the damping inequality are in Addendum Section 9 and `DAMPED_TRANSFER.md`, Sections 1–2.

## 5. Choosing the proof mesh and quantifying the carrier remainder

For sufficiently large n set

\[
K_n=\left\lfloor[\log(e^e+n)]^{1/128}\right\rfloor,\quad
N=\lceil C_0K_n^3\rceil,\quad
T=\frac2\kappa\log K_n,\quad
h=T/K_n,\quad R=A\sqrt{\log K_n}.
\tag{14}
\]

One normalized passive probe and all elementary reference instructions fit this budget. Tail observations are additional scalar tests. Choose A large enough that the Gaussian tail is smaller than K_n^{-4}. Since N^5=O((log n)^{15/128}), all finite-program errors in (8) are polynomially small in n. The bias exp(-cN^2) is smaller than every fixed inverse power of K_n. Consequently (13) and its population analogue are

\[
K_n^{-1+o(1)}.
\tag{15}
\]

The remaining activity and prediction variation after T are at most C exp(-kappa T)=C K_n^{-2}. Comparing dense carriers to the oracle nodes adds only a factor 1+R to (15). Soft-tail tests at all integer M<=N, followed by monotonicity for M>N, therefore give

\[
a_n\le K_n^{-1+o(1)}
\quad\text{outside an event of probability }Cn^{-c}.
\tag{16}
\]

The original initialization event has polynomially small failure probability as well: Gaussian operator tails and fixed-tolerance Gram concentration suffice. Its Gram argument allows singular intermediate covariances and is given in Addendum Section 2.

The transform Phi in (4) adds only K_n^{o(1)} to (16). In particular, for all sufficiently large n one may use b_n<=C K_n^{-1/3}<=C r_n. The event concerns the dense reference only, so it is common to every closure order. This proves (2).

## 6. Quantifying the dense-to-population term on the full input space

For a passive input x divide all forward fields by s_x=1+||x||/sqrt(d). The activation map u -> phi(s_x u)/s_x has bounded intercept and slope uniformly in x. Passive predictions require no new backward derivatives. Thus (8)–(15) apply with constants uniform in x after normalization.

Outside a polynomially small single-probe exceptional event, the all-time normalized dense-to-population prediction error is at most C K_n^{-1/2}, a weakened form of (15). On the common physical good event G_n it is bounded by a fixed constant even if the probe event fails. Hence

\[
\mathbb E\left[1_{G_n}\sup_{t\ge0}
|f_{n,D}(t,x)-f_\infty(t,x)|^2\right]
\le C s_x^2(K_n^{-1}+n^{-c}).
\tag{17}
\]

Tonelli integrates (17) for every fixed test law with finite second moment. Markov at threshold C_mu K_n^{-1/4} gives failure O_mu(K_n^{-1/2})+O(n^{-c}), which is smaller than C_mu r_n. Combining this with (2) and the paper's deterministic prediction Lipschitz bound proves (3). The supremum over time is already inside (17), so no finite test mesh or selected stopping time is hidden in this conclusion.

On a fixed bounded domain, apply separate single-probe estimates on a K_n^{-1/2} net, and union-bound the polynomial-in-K_n many failure probabilities. The common input Lipschitz bound extends the estimate to every input. Separate probe programs avoid any dimension-dependent violation of the instruction budget N=O(K_n^3).

## 7. Meaning and remaining problem

This removes the unspecified o_P(1) from both the parameter and population-prediction statements. It preserves the canonical Gaussian reused matrices, exact zero readout, broad smooth activation class, finite multi-input data, fixed depth, and sufficiently small constant label RMS. Both n and q now appear in one explicit all-time accuracy bound.

It does not establish the practically desirable Monte Carlo width rate. Inverting r_n gives only a very large sufficient width of exponential order in a power of 1/epsilon, so the result must not be used to claim an epsilon^{-5/2} total learned-state guarantee. The existing subquadratic-in-width moving-state conclusion remains intact.

There is also a metric distinction: an n^{-1} mean-square prediction error corresponds to n^{-1/2} RMS error. `WIDTH_OBSTRUCTION_ROUTE.md` gives a zero-readout, small-label linear instance in the allowed activation class whose fitted unseen prediction has standard deviation of order n^{-1/2}; this rules out a universal n^{-1} root-error law. That special-case lower bound is not a proof of an n^{-1/2} upper bound for general nonlinear activations and does not itself lower-bound the carrier-only remainder b_n.

The next sharp question is whether (16) and (17) admit algebraic rates in n. The present proof answers the explicit-rate question, not that sharper one.
