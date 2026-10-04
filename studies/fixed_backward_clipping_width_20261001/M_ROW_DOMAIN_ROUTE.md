# Growing smooth caps: comparison using response-row masses

2026-10-01. Scoped continuation of M_UNIFORM_LAW_ROUTE.md. This note tests the
supervisor's proposed strengthening using strong covariance/response
fluctuation estimates. The exact model and prescribed histories are those
of SMOOTH_SETUP.md and SMOOTH_MEAN_MAP_ROUTE.md. This note changes neither
that model nor the already written coarse-domain result.

**Conclusion.** The proposed population comparison and mean-response
first-exit argument work. Uniform constants require small response-row
masses and the upper atom, together with uniformly regular Gaussian input
covariances. Response densities and current-time row-Lipschitz constants
may grow with \(M\). Strong random-input error norms replace the need for
uniform deterministic entrywise majorants.

The first-exit conclusion below is conditional on the explicitly stated
strong cavity estimates and tagged-response moments. Those are
finite-width statistical statements, not consequences of this law-map
argument. Subject to those hypotheses, the consistency and population
comparison constants are single exponential in \(M\); a triple-exponential
law-map loss is unnecessary.

## 1. Domain used for comparison

Use activity \(x\in[0,S]\), \(S\le1\), the Gaussian laws
\(H=(C_h,Q_h)\), \(D=(C_d,D_{\rm atom},Q_d)\), and the exact scalar equations
(1) of M_UNIFORM_LAW_ROUTE.md. Here \(Q_h\) is a causal regular response
kernel with no atom, while \(D_{\rm atom}\) is the separate current upper
response. The prescribed \(\lambda,K,V\) satisfy the same fixed bounds as
in that note.

Fix constants \(L\) and \(B\) independently of \(M\ge1\). Require the
covariances to be positive semidefinite and

\[
\begin{aligned}
C_{h,aa}(x,x)&\le1,\\
C_{d,aa}(x,x)&\le L^2x^2,\\
C_{\ell,aa}(x,x)+C_{\ell,aa}(y,y)-2C_{\ell,aa}(x,y)
 &\le L^2|x-y|^2,\qquad \ell=h,d.
\end{aligned}                                                    \tag{1}
\]

For a causal response \(Q\), put

\[
\|Q\|_{\rm row}
 =\sup_{x\le S}\max_a\sum_b\int_0^x|Q_{ab}(x,u)|\,du.
\]

The response restrictions are only

\[
\|Q_h\|_{\rm row}\le BS,\qquad
\|D_{\rm atom}\|_\infty+\|Q_d\|_{\rm row}\le BS.             \tag{2}
\]

Assume each individual input has finite response density and current-row
regularity constants sufficient for its scalar equations and continuum
responses to be defined. These constants can be \(B_M\), with arbitrary
finite dependence on \(M\); they are not used in the estimates below.
There is no current lower response atom.

This is a **comparison domain**, not an asserted invariant domain.
Arbitrary rapid target-time variation of \(Q_h\) can make the upper output
covariance increments large. Also, the regular upper response contains

\[
A_a(x)Q_{h,ab}(x,u)A_b(u),\qquad
A_a(x)=c'_M(w(x)\psi(z_a(x)))w(x)\psi'(z_a(x)).
                                                               \tag{3}
\]

Thus a narrow high peak in the input density can persist in the output
density. Neither a uniform upper output density bound nor uniform output
covariance increments follow from (2). The bootstrap below needs only
the output response-row masses. Physical finite/cavity covariance
increments, and those of the comparison population, are separate inputs.

For differences, use the same normalized distances as in the existing
law-map proof:

\[
\begin{aligned}
d_H(H,\widetilde H)
 &=\|\delta C_h\|_\infty+S^{-1}\|\delta Q_h\|_{\rm row},\\
d_D(D,\widetilde D)
 &=S^{-2}\|\delta C_d\|_\infty+
 S^{-1}\{\|\delta D_{\rm atom}\|_\infty+
                       \|\delta Q_d\|_{\rm row}\}.
\end{aligned}                                                    \tag{4}
\]

For random tuples, the strong error is the \(L^2\) norm of the *whole*
distance (4), with its time suprema and response-row integration already
inside that norm. This is stronger than the supremum of entrywise
\(L^2\) errors.

## 2. Uniform total derivative masses

Write \(\psi=\operatorname{sech}^2\) and
\(F_M(\alpha,p)=M\tanh(p\psi(\alpha)/M)\). For every fixed order \(q\),

\[
|\partial_\alpha^r F_M|\le C_q|p|,\qquad
|\partial_\alpha^r\partial_p^jF_M|\le C_q\quad(j\ge1),
                                                               \tag{5}
\]

uniformly for \(M\ge1\), when the total order is at most \(q\).
The proof is in Section 2 of M_UNIFORM_LAW_ROUTE.md. The upper states obey

\[
|w(x)|,|d_a(x)|\le cx,\qquad |v_a(x)|\le cx^2,
\]

so all pure-\(z\) derivatives of \(d=F_M(z,w)\) have the factor \(S\),
while derivatives containing a \(w\) derivative are uniformly bounded.

The lower Gaussian history \(\xi\) satisfies (1). Its supremum is
dominated by \(LSZ_*\), where \(Z_*\) has a fixed sub-Gaussian tail,
uniformly over the input laws, meshes, and convex covariance
interpolations. This remains true conditionally on a cavity environment
when its conditional covariance satisfies (1).
The lower carrier therefore obeys the envelope

\[
\sup_{a,x}|p_a(x)|\le S\{LZ_*+C B+C\}.                    \tag{6}
\]

The initial read-in Gaussian needs no envelope because (5) and the tanh
derivative bounds are uniform in the initial read-in.

On a mesh let \(J_q(X)\) be the sum of absolute derivatives of \(X\) over
all ordered \(q\)-tuples of Gaussian history coordinates. The lower
carrier recurrences use only

\[
\begin{aligned}
J_1(p)&\le m+CBS\,J_1(a,k),\\
J_2(p)&\le CBS\{J_2(a,k)+J_1(a,k)^2\},\\
J_3(p)&\le CBS\{J_3(a,k)+J_1(a,k)J_2(a,k)+J_1(a,k)^3\}.
\end{aligned}                                                    \tag{7}
\]

Indeed each memory coefficient is summed along its current row before
the running maximum of the state derivatives is taken. No density bound,
source-cell bound, or target-row derivative bound appears in (7).
The current atom is bounded separately by \(BS\).

If \(BS\le1\), the positive derivative recurrences, with the Gaussian
envelope (6), give

\[
J_q(h)+J_q(k)+J_q(a)
 \le S P_q(1+SZ_*)e^{C_qS(1+SZ_*)},\qquad q=1,2,3,        \tag{8}
\]

after changing the fixed constants. The proof is finite-order induction:
the highest derivative enters linearly with coefficient bounded by
\(C(1+SZ_*)\); all lower-order partition products form its forcing.
Volterra iteration gives the exponential in (8), rather than requiring
pointwise smallness for each Gaussian realization. This also proves any
fixed extra derivative order needed for a passive observable.

For the upper equations,

\[
J_q(z)\le m\,1_{\{q=1\}}+BS\,J_q(d)+C J_q(v),
\qquad J_q(v)\le CS\,J_q(d).
\]

The pure-\(z\) factor \(S\), and integration in the \(w\) equation, give
\(J_q(d)\le CS+CS(BS+S)J_q(d)\) after lower orders have been bounded.
For sufficiently small \(S\), with \(BS\le1\), this yields

\[
J_q(w)+J_q(d)\le C_qS,\qquad J_q(v)\le C_qS^2.             \tag{9}
\]

The constants in (8)--(9), after averaging the Gaussian envelope, can be
chosen independently of \(B\), provided \(BS\le1\); in particular they
are independent of \(M\) and \(B_M\).
The same row-mass argument proves well-posedness on this short activity
interval. For passage to the continuum, each fixed input retains its
finite \(B_M\) regularity. One first takes its mesh limit, then applies
the uniform bounds (8)--(9); a uniform bound on \(B_M\) is not needed.

The first derivatives immediately imply the strict output bounds

\[
\|Q_h^{\rm out}\|_{\rm row}\le cS,\qquad
\|D_{\rm atom}^{\rm out}\|_\infty+\|Q_d^{\rm out}\|_{\rm row}
 \le cS.                                                   \tag{10}
\]

For the upper response, the current atom is precisely its current
Gaussian derivative, and the past derivative sum becomes the integrated
regular response. Formula (10) therefore retains the atom rather than
silently treating it as a density. The constant \(c\) is independent of
\(B,M,B_M\) under the stated smallness conditions.

## 3. Uniform comparison using strong random-input errors

Let two covariance/response tuples, measurable with respect to an
environment \(\mathcal E\), satisfy (1)--(2) almost surely.
Conditional on \(\mathcal E\), their carrier histories have the actual
centered Gaussian laws of those tuples. Hold all response coefficients
fixed during covariance interpolation.

For a scalar output \(f\), Gaussian covariance interpolation gives

\[
\left|\mathbb E[f(X_1)-f(X_0)\mid\mathcal E]\right|
\le \frac12\|\delta\Gamma\|_\infty
 \sup_{\theta\in[0,1]}
 \mathbb E[J_2(f)(X_\theta)\mid\mathcal E].                 \tag{11}
\]

Singular covariances are allowed: realize
\(X_\theta=\sqrt{1-\theta}X_0+\sqrt\theta X_1\) using independent
Gaussian endpoints, and integrate by parts in their underlying standard
Gaussians. Their convex covariance interpolation still satisfies (1).
The envelope in (8) has all needed moments, justifying the formula by
truncation and dominated convergence.

In (11), the covariance supremum is environment measurable, so it is
taken outside the conditional Gaussian expectation. The remaining
expected total Hessian mass is uniform by (8)--(9). For a response
output, sum its distinguished response index and use the third
derivative mass. Thus the same reasoning bounds its integrated
response-row norm.

For response-input interpolation put

\[
e(\mathcal E)=
\|\delta D_{\rm atom}\|_\infty+\|\delta Q_d\|_{\rm row},
\qquad
\eta(\mathcal E)=\|\delta Q_h\|_{\rm row}.
\]

The lower direct carrier perturbation is at most \(Ce\); its first
history derivative has total forcing bounded by \(Ce\) times the
already controlled state jets. Integrating the lower state equation,
then propagating its variation, gives the conditional mean bounds

\[
|\delta h|+\|\delta R_h\|_{\rm row}\le CS e.
\]

Here and in the next display, the differences are the conditional
Gaussian-averaged outputs. In the upper equation the direct perturbation
is at most \(CS\eta\), because it is \(\delta Q_h\) applied to \(d\);
the top pure-\(z\) derivative and the integrated readout each contribute
the additional factor \(S\). Consequently

\[
|\delta d|+
\|\delta R_d\|_{\rm row+atom}\le CS^2\eta.                 \tag{12}
\]

All error suprema in this argument are environment measurable and are
factored out before Gaussian averaging. No deterministic entrywise
majorant and no stronger Gaussian moment of an environment error is
being assumed.

Products \(hh\) and \(dd\) have Hessian masses \(CS\) and \(CS^2\).
Combining (11)--(12), taking the deterministic target-time supremum,
and then the \(L^2(\mathcal E)\) norm proves

\[
\begin{aligned}
\|d_H(\mathcal L_MD,\mathcal L_M\widetilde D)\|_{L^2}
 &\le C_LS\,\|d_D(D,\widetilde D)\|_{L^2},\\
\|d_D(\mathcal U_MH,\mathcal U_M\widetilde H)\|_{L^2}
 &\le C_U\,\|d_H(H,\widetilde H)\|_{L^2}.
\end{aligned}                                                    \tag{13}
\]

The outputs in (13) are conditional Gaussian expectations. The
constants are independent of \(M,B_M\). Choose \(S\) so that
\(C_LC_US<1/2\).
The comparison remains valid when the inputs' regularity constants
differ, because only their finite existence is used and convex
interpolation preserves all common bounds.

This is sufficient to compare an approximate finite expected tuple to
the already constructed population fixed point. A selfmap property of
the larger comparison domain is unnecessary.

## 4. Precise statistical hypotheses for the bootstrap

The following proposition states exactly what the finite-width route
must supply. All assertions are uniform over prefix intervals
\([0,t]\subset[0,S]\) and the prescribed histories under consideration.
Write \(a_M\le C e^{CM}\), with \(a_M\ge1\). Changing the constants in this
single exponential is permitted.

Let \(X_n=(H_n,D_n)\) be the deterministic full finite expected tuple.
Let \(\widehat X_n\) be its random cavity input tuple, measurable with
respect to the deleted-neuron environment. Assume:

1. The mean covariances satisfy (1). On a cavity-measurable event
   \(\mathcal O_n\), the random cavity covariances satisfy the same bounds,
   and \(\Pr(\mathcal O_n^c)\le C e^{-cn}\). All individual kernels have
   finite, possibly \(M\)-dependent, density and row regularity.
2. Strong centered and deletion estimates imply
   \[
   \|d_H(\widehat H_n,H_n)+d_D(\widehat D_n,D_n)\|_{L^2}
   \le a_M/\sqrt n.                                      \tag{14}
   \]
   Bounds in unnormalized norms are equally sufficient since the labels,
   hence \(S>0\), are fixed; their powers of \(S^{-1}\) change only fixed
   constants.
3. The actual tagged covariance and response observables representing
   \(X_n\) have \(L^2\) moments at most \(a_M\) in the required strong
   output norms. In particular the response moment includes the supremum
   over target time and the integral of absolute regular response over
   source time, plus the upper atom.
4. On any cavity-measurable event on which the input satisfies (1)--(2),
   the actual tagged statistic is compared to its conditional scalar-law
   expectation with mean error at most \(a_M/\sqrt n\), in the same
   output norms. The response comparison includes the separate tagged
   forcing variation; it is not obtained by differentiating a state
   approximation bound.

Hypothesis 4 is an event-localized cavity identity. It does not require
evaluation or stability of the scalar law on a bad random input. This
distinction is needed to avoid reintroducing the coarse-domain
exponential loss.

## 5. Localization before scalar evaluation

Choose a mean response barrier \(B_0S\), with \(B_0>4c\), where \(c\)
is from (10). In applying the scalar estimates take \(B=2B_0\), and
decrease the fixed \(S\) to ensure \(2B_0S\le1\) and (13).

Suppose on a given prefix interval the deterministic mean tuple has

\[
\|Q_{h,n}\|_{\rm row}\le B_0S,\qquad
\|D_{{\rm atom},n}\|_\infty+\|Q_{d,n}\|_{\rm row}\le B_0S.  \tag{15}
\]

Intersect \(\mathcal O_n\) with the event that the cavity-to-mean response
distance is at most the fixed margin \(B_0S/2\) in the corresponding
unnormalized row-and-atom norms. Denote this environment-measurable
event by \(\mathcal A_n\). On it the cavity input lies in the domain
with \(B=2B_0\). Chebyshev and (14) give

\[
\Pr(\mathcal A_n^c)\le C_S a_M^2/n+C e^{-cn}.              \tag{16}
\]

The subscript \(S\) emphasizes a permitted fixed-label constant.
Replace the bad input by a fixed safe tuple: constant initial lower
covariance \(C_0\), zero lower response, and zero upper covariance,
response and atom. Denote the resulting tuple by
\(\widetilde X_n\). Both this safe tuple and the mean tuple satisfy the
comparison domain; the actual cavity input does so on \(\mathcal A_n\).
Their covariance and response distances are deterministically bounded
in the normalized metric. Hence

\[
\|d_H(\widetilde H_n,H_n)+d_D(\widetilde D_n,D_n)\|_{L^2}
 \le C_Sa_M/\sqrt n+C_Se^{-cn/2}.                         \tag{17}
\]

For the response rows this uses (15); for covariance entries it uses
the deterministic variance bounds. No closeness of the original bad
input is required.

Apply the cavity identity only on \(\mathcal A_n\). On its complement,
discard the **actual tagged observable** and use its moment bound:

\[
\|\mathbb E[1_{\mathcal A_n^c}T_n]\|
 \le \Pr(\mathcal A_n^c)^{1/2}
        \|\,\|T_n\|\,\|_{L^2}
 \le C_Sa_M^2/\sqrt n+C_Sa_Me^{-cn/2}.                   \tag{18}
\]

The safe scalar output has a uniform bound, so its added bad-event
contribution is bounded by \(C_S\Pr(\mathcal A_n^c)\).
This proves

\[
\|X_n-\mathbb E\,\mathcal T_M(\widetilde X_n)\|
 \le C_Sa_M^2/\sqrt n,                                  \tag{19}
\]

after absorbing the exponential spectral tail and increasing constants.
Here \(\mathcal T_M(H,D)=(\mathcal L_MD,\mathcal U_MH)\), and the norm
can be either normalized as in (4) or unnormalized with the corresponding
fixed constants.
For \(n\) large enough that \(a_M/\sqrt n\le1\), the
\(a_M^2/n\) term is also bounded by \(a_M/\sqrt n\); retaining the larger
right side of (19) is convenient.

Finally use (13), (17), and Jensen to replace the randomized safe input
by \(X_n\). This yields an approximate fixed point

\[
d_H(H_n,\mathcal L_MD_n)+d_D(D_n,\mathcal U_MH_n)
 \le C_Sa_M^2/\sqrt n
 \le C'_S e^{C'M}/\sqrt n.                               \tag{20}
\]

This derivation never evaluates the scalar law on the original bad
kernel. Bounding that scalar output by its coarse global propagator
instead would invalidate the claimed single-exponential accounting.

## 6. First exit of the deterministic mean responses

Each finite expected response row is continuous in target time as an
\(L^1\) row, and the atom is continuous. This follows from its finite
regularity bounds; those bounds need not be uniform in \(M\).
Consequently the running row-and-atom norms are continuous. They vanish
at activity zero.

Let \(\sigma\) be the first prefix at which either norm in (15) reaches
\(B_0S\). If a first exit exists, (15) holds on \([0,\sigma]\), including
its endpoint. The previous localization and consistency proof applies
on precisely that interval. Uniform output bound (10), plus the
unnormalized version of (20), gives at the alleged first exit

\[
B_0S\le cS+C_Se^{CM}/\sqrt n.
\]

For

\[
n\ge C_Se^{CM},                                         \tag{21}
\]

with the constants increased as necessary, the last error is less than
\((B_0-c)S\), a contradiction. The finite mean response tuple therefore
stays strictly inside (15) throughout \([0,S]\).
The argument uses a fixed absolute barrier \(B_0S\), not a barrier
shrinking proportionally to the prefix length; no division by a small
prefix time is needed.

Let \(X_*=(H_*,D_*)\) be the common small-activity population fixed point
from M_UNIFORM_LAW_ROUTE.md. It satisfies (1) and lies inside the same
response barrier. Applying (13) to \(X_n,X_*\), and using (20), gives

\[
\begin{aligned}
d_H(H_n,H_*)&\le \varepsilon_M+C_LS\,d_D(D_n,D_*),\\
d_D(D_n,D_*)&\le \varepsilon_M+C_U\,d_H(H_n,H_*),
\qquad
\varepsilon_M=C_Se^{CM}/\sqrt n.
\end{aligned}
\]

Since \(C_LC_US<1/2\), substitution and absorption prove

\[
d_H(H_n,H_*)+d_D(D_n,D_*)\le C_Se^{CM}/\sqrt n.            \tag{22}
\]

No invariance of the larger row-only comparison domain was invoked.
The mean and population covariance increments were supplied separately;
the nonlinear map was used only for values and response-row comparison.

## 7. Consequence and remaining proof boundary

Under hypotheses 1--4, the population identification stage has a common
positive activity threshold, a width threshold at most single exponential
in \(M\), and a single-exponential root-width error constant. In
particular, choosing

\[
M(n)=\sqrt{\log(n+e)}
\]

makes (21) hold eventually and gives \(n^{-1/2+o(1)}\) in (22).
A sufficiently small constant multiple of \(\log n\) also gives a
decaying power rate, but its allowed coefficient depends on the
unoptimized exponential constant. Neither assertion is a uniform
\(C/\sqrt n\) theorem.

To turn this into the requested all-time predictor theorem, the
finite-width route must establish hypotheses 1--4 for the exact reused
Gaussian mixer, including its actual transpose, and the passive
velocity observables needed for feedback restoration. Their response
moments and event-localized consistency must stay single exponential
in \(M\). The all-time autonomous restoration must have the same
constant accounting. This note proves the population comparison and
the bootstrap implication; it does not substitute those hypotheses
for their required proofs.

The potential objections resolved here are: no uniform response density
is needed; the covariance increment domain is not falsely called
invariant; the upper atom is retained; a random covariance supremum is
used only when it is actually controlled by the assumed strong norm;
and the bad-input scalar map is never evaluated.
