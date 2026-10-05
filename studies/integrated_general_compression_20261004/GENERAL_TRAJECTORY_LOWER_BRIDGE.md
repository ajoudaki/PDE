# General actual-trajectory lower bound on the training timescale

2026-10-04. Internal reconstruction within this study, not promotion.
Complete relevant inputs read: EARLY_VARIABILITY_AND_STORAGE.md;
ONSET_TO_TRAJECTORY_LOWER.md; UNBOUNDED_COMPRESSOR_BRIDGE.md §§1–8 and §13;
SIMPLE_CONSTANTS_SOURCE_CHECK.md; and EXPLICIT_LEGENDRE_COMPARISON.md.
The coordinator's final order update also uses the current
LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md and its
SAMPLE_POLYNOMIAL_STATEMENT.md.
The initialized CLT, fitting, and stopped Gaussian insertion interfaces are
inherited component results. This note proves a finite-query localization
of the complex source, retains the physical training timescale in its
nonlinear lower bound, and calibrates the existing approximations to that
lower reference. It assumes no trained fluctuation theorem.

## 1. Setup and the exact onset variance

Fix hidden depth \(L\ge2\), sample count \(m\ge1\), dimension \(d\ge1\),
unit inputs \(v_a=x_a/\sqrt d\), and nonzero labels \(y\in\mathbb R^m\).
Use the canonical width-\(n\) network
\[
h^{(1)}(v)=\phi_1(Av),\quad
h^{(j)}(v)=\phi_j(W^{(j)}h^{(j-1)}(v)),\quad
f_n(v)=n^{-1}w^\top h^{(L)}(v).
\]
The entries of \(A\) and \(W^{(j)}\), \(2\le j\le L\), are initially
independent \(N(0,1)\) and \(N(0,1/n)\), respectively; \(w=0\).
All hidden layers train. With residual \(r_a=f_n(v_a)-y_a\), the mean
squared loss and mobilities \((n,1,\ldots,1,n)\) give
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(j)}=-\frac2{mn}\sum_a
r_a\delta_a^{(j)}h_a^{(j-1)\top},\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{1}
\]
The backward variables are \(k_a^{(L)}=w\),
\(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)}\), and
\(k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}\).

Activations may depend on the layer, are real on the real line, and are
holomorphic on the common strip \(|\operatorname{Im}z|<a\), with bounded
first derivative there. Their values need not be bounded. Put
\[
\beta=\max\{10,\ 1+\max_j|\phi_j(0)|,\ 16/a,\
\max_{j,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}
                         |\phi_j^{(k)}(z)|\}.
\tag{2}
\]
For any fixed unit query \(v_0\), define augmented population matrices,
indexed by \(0,\ldots,m\), by
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],
\qquad Z\sim N(0,Q^{(j-1)}).
\tag{3}
\]
Let \(\gamma>0\) be the least eigenvalue of the training block of
\(Q^{(L)}\), and set
\[
\lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m>0,\qquad
S=16Y/\lambda,\qquad \ell_n=\log(en).
\tag{4}
\]
The general statement retains the existing recurrence-based label
allowances: the proved real fitting allowance and
\(S\le S_*^{\rm src}\), with the positive activation/depth constant
\(S_*^{\rm src}\) defined by source (5)–(10). For the approximation
corollaries also retain the existing closure and compact fitting
allowances. These are exactly the existing component hypotheses,
not extra dynamical conditions. The simple sufficient common cap
\[
Y/\lambda\le\beta^{-30L}
\tag{5}
\]
will give a particularly simple radius, but is not needed for the
recurrence-based version.

Use upper triangular coordinates on symmetric matrices. Let \(B_j\) be
the covariance of \(\phi_j(Z)\phi_j(Z)^\top\) for the Gaussian in (3).
For a symmetric perturbation \(E\), define
\[
\begin{aligned}
(T_jE)_{ab}={}&
\tfrac12E_{aa}\mathbb E[\phi_j''(Z_a)\phi_j(Z_b)]
+E_{ab}\mathbb E[\phi_j'(Z_a)\phi_j'(Z_b)]\\
&+\tfrac12E_{bb}\mathbb E[\phi_j(Z_a)\phi_j''(Z_b)],\\
C_0={}&0,\qquad C_j=T_jC_{j-1}T_j^\top+B_j,\\
\sigma(v_0,y)^2={}&
\frac8{m^2}\sum_{a,b=1}^m y_a C_{L,0a,0b}y_b .
\end{aligned}
\tag{6}
\]
These are specified finite Gaussian integrals, including at singular
intermediate covariance matrices. In particular
\(\sigma(v_0,\alpha y)=|\alpha|\sigma(v_0,y)\).

For two independent actual dense runs define
\[
g_n(t)=f_n(t,v_0)-\widetilde f_n(t,v_0),\qquad
\mathcal D_n=\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
                       |f_n(t,v)-\widetilde f_n(t,v)|.
\tag{7}
\]
The inherited fitting event supplies the uniform endpoints included here.
The exact initial identity is
\(\dot f_n(0,v_0)=2m^{-1}\sum_a y_a K^{(L)}_{n,0a}\):
zero readout makes every hidden initial velocity vanish. The initialized
CLT from the early note therefore proves
\[
\sqrt n\,g_n'(0)\ \Longrightarrow\ N(0,\sigma(v_0,y)^2).
\tag{8}
\]
The factor eight in (6) includes both independent copies. Throughout,
the inputs, labels, \(L,m,d\), and activations remain fixed as
\(n\to\infty\). No uniform growing-sample CLT is asserted.

## 2. The source argument restricted to finitely many real queries

Let \(\mathcal V\) be any fixed finite collection of unit real queries,
for example all training inputs and \(v_0\). The source proof has two
different uses of queries: its training sample budgets, and the passive
query sphere. Only the second is changed here.

Keep the source's joint sample budgets, independently stopped cavities,
actual-amplitude traces, and activity allowance \(S\), with horizon
\(T_n=32\lambda^{-1}\ell_n\). Source §§2–5 are unchanged. In source §6,
the residual-free response at a query \(v\) is
\[
R_a^{(j)}(v)=D_\Theta z^{(j)}(v)\nabla_\Theta(nf_n(v_a)),
\qquad
\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w).
\]
The pointwise endpoint and insertion identities still apply: they only
require that the query norm be at most two. Omit the angular derivative,
frame interpolation, and complex query segments, since all queries in
\(\mathcal V\) are fixed and real.

The dimension-dependent factor \(G_d=16\sqrt{d+3}\) of source (25)
is used solely in the centered Gaussian pairing's union over the frame
mesh. Replace it in the response recurrence by \(G_{\rm fin}=64\).
For precision, retain all activation/depth coefficients
\(H_j,f_j,q_j,T_Q,K_{\rm src}\) exactly as defined in source (5)–(6),
(22), and (24), and define
\[
\begin{aligned}
U_1(S)&=4sK_{\rm src},\\
U_j(S)&=2\{sK_{\rm src}[H_{j-1}^2+f_{j-1}^2
 +ST_Q+S^2H_{j-1}q_{j-1}]+64q_{j-1}+1\},\quad j\ge2,\\
U_{\rm fin}(S)&=\max_j U_j(S).
\end{aligned}
\tag{9}
\]
Here \(s\) is the half-strip first-derivative bound with lower bound one.
All coefficients in (9) except \(S\) depend only on activations and depth.
The only changed numerical coefficient is 64.

The probability and continuity checks for this replacement are as follows.
A mesh of spacing \(n^{-2}\) on the two-real-dimensional time rectangle
has \(O(n^5)\) points eventually: its length is \(O(\ell_n)\) and its
width is bounded. After the remaining root/neuron indices and the fixed
sample, layer, and query indices, the source proof's non-frame grid
count is at most \(n^{10}\) eventually. This is its bound
\(n^{4d+10}\) with the frame mesh omitted. Its normalized centered complex
Gaussian pairing has tail at most \(4e^{-u^2/4}\). Thus the Gaussian
union at \(u=64\sqrt{\ell_n}\) costs at most
\[
4n^{10}e^{-1024\ell_n}=o(1).
\tag{10}
\]
The inherited control-uniform insertion event is unchanged. There is no
new union over deletion subsets: the source proof treats each fixed
common cavity at each fixed moment degree. Stopped coordinate derivatives
are at most \(\sqrt n\,\operatorname{polylog}n\), so the off-grid error
at mesh size \(n^{-2}\) vanishes. Fixed real queries have no spatial
off-grid error. Their initial maxima obey the same fresh-row Gaussian
tails. Their temporary passive-query amplitude stop improves by the
original \(U_{\rm fin}S^2\sqrt{\ell_n}\) real increment. No exponential
query budget is needed.

It follows, with the same strict stop margins, that
\[
\max_{v\in\mathcal V,a,j}\|R_a^{(j)}(v)\|_\infty
       \le S U_{\rm fin}(S)\sqrt{\ell_n}.
\tag{11}
\]
For any fixed
\[
0<c\le c_{\max}(S):=\frac{a}{64YSU_{\rm fin}(S)}
                    =\frac{a}{4\lambda S^2U_{\rm fin}(S)},
\qquad r_n=\frac{c}{\sqrt{\ell_n}},
\tag{12}
\]
source §§7–8 now apply on
\[
[-r_n,T_n+r_n]+i[-r_n,r_n].
\tag{13}
\]
Here are the domain checks. The same source (31) width gates, with \(c\)
in place of \(c_t\), are
\[
n^{-1}\le Y,\qquad
\sqrt{\ell_n}\ge
c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\tag{14}
\]
The constants \(\mathcal K,D_W\) are the unchanged source §8 Gram and
parameter-increment bounds. These conditions give at most factor-two
residual growth, extra activity at most \(S/2\), and parameter increments
at most \(1/4\) on the short time pieces. By (1), (11), and
\(\rho\le2Y\), their total preactivation displacement is at most
\(8cYSU_{\rm fin}\le a/8\). There is no angular displacement.
Consequently the full and cavity pole stops keep their original strict
margins inside the derivative strip.

The source (27)–(28) complex-minus-real Gaussian coefficient radii still
tend to zero at each fixed \(c\). Its empirical moment proof gives exactly
\[
\limsup_n\Pr\{\text{a training budget is hit}\}
 \le mL(16L/\mathcal B)^p,\qquad \mathcal B=1024e^2L .
\tag{15}
\]
First take the width limit for each fixed integer \(p\), then the
infimum over \(p\), to make (15) zero. Thus the modified argument proves
a localized source event of probability tending to one, with holomorphy
on a neighborhood of (13). Its forward RMS bounds are still \(H_j\)
and its readout RMS bound is still \(SH_L\). In particular, on the
intersection of the two copies' localized events,
\[
|g_n|\le 2SH_L^2\le32\beta^{6L}Y/\lambda=:M
\tag{16}
\]
throughout (13). The inequality \(H_L\le\beta^{3L}\) is independent
of the label allowance.

This is a new localization of the existing source proof, not a claim
that its original whole-sphere event already has the larger time radius.
It changes only a probability union and the query stops; all deterministic
insertion identities and training-budget estimates are retained. The
stochastic success width remains unquantified.

## 3. Retaining the full recurrence-based label scope

The best capped training-time factor supplied by (12) is
\[
\chi(S)=\min\left\{1,\frac{a}{4S^2U_{\rm fin}(S)}\right\}>0.
\tag{17}
\]
Thus \(c=\chi(S)/\lambda\) is allowed. Every \(U_j(S)\) in (9) is a
polynomial in \(S\) with nonnegative coefficients. Hence
\[
\chi(S)\ge
\chi_{\rm act}:=
\min\left\{1,\frac{a}
 {4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0 .
\tag{18}
\]
The constant \(\chi_{\rm act}\) depends only on the activations and
depth. Equations (17)–(18) require only the original source label
allowance \(S\le S_*^{\rm src}\). They do not strengthen it to (5).

Under the convenient sufficient cap (5), the power ledger in
SIMPLE_CONSTANTS_SOURCE_CHECK.md §3 applies to (9) and gives
\[
U_1\le4\beta^{20L+3},\qquad
U_j\le22\beta^{26L-5}+128\beta^{8L-5}+2
                      \le\beta^{26L}\quad(j\ge2).
\tag{19}
\]
The first quantity is also at most \(\beta^{26L}\), since its ratio
is \(4\beta^{-6L+3}\le4\cdot10^{-9}\). For the second, the ratios
sum to at most \(22\cdot10^{-5}+128\cdot10^{-41}+2\cdot10^{-52}<1\).
Here \(S\le\beta^{-26L}\), as already proved from (5). Therefore
\[
\frac{a}{4S^2U_{\rm fin}(S)}
 =\frac{a\lambda^2}{1024Y^2U_{\rm fin}(S)}
 \ge\frac{\beta^{34L-1}}{64}>1.
\tag{20}
\]
We used \(a\ge16/\beta\) in the last inequality. This proves
\(\chi(S)=1\) under (5), and gives
\[
r_n=\frac1{\lambda\sqrt{\ell_n}}
     =\frac{m}{\gamma\sqrt{\log(en)}}.
\tag{21}
\]
The actual \(Y\) in (6) and (16) has not been replaced by its cap.

## 4. Deterministic conversion and the general lower theorem

The deterministic Chebyshev lemma from the onset note is:
if \(g\) is holomorphic on a neighborhood of the filled parameter-two
Bernstein ellipse for \([0,r]\), and \(|g|\le M\) there, then
\[
\sup_{0\le t\le r}|g(t)|
 \ge\frac r{2N^2}|g'(0)|-24M2^{-N}\qquad(N\ge1).
\tag{22}
\]
To record the proof, map \([0,r]\) to \([-1,1]\). The coefficients of
the Chebyshev series obey \(|a_k|\le2M2^{-k}\), so its degree-\(N\)
tail is at most \(2M2^{-N}\), and its physical-time derivative at zero
is at most
\[
\frac{4M}{r}\sum_{k>N}k^2 2^{-k}
 =\frac{4M}{r}2^{-N}(N^2+4N+6).
\]
The polynomial endpoint inequality is
\(|P'(-1)|\le N^2\sup_{[-1,1]}|P|\), also for complex coefficients.
For example, interpolation at the Chebyshev extrema gives alternating
endpoint derivative weights; their absolute sum is
\(|T_N'(-1)|=N^2\). Apply this inequality to the truncated series and
add both tails. The error coefficient is
\(4+8/N+12/N^2\le24\), proving (22).

The parameter-two ellipse for \([0,r_n]\) has real projection
\([-r_n/8,9r_n/8]\) and imaginary projection
\([-3r_n/8,3r_n/8]\). It lies in (13), since (14) gives
\(r_n\le1/\lambda\), whereas \(T_n=32\ell_n/\lambda\).
Take
\[
N_n=\left\lceil2\ell_n/\log2\right\rceil\le4\ell_n,
\qquad 2^{-N_n}\le n^{-2}.
\]
Equations (16), (22) prove, on the two-copy localized event,
\[
\mathcal D_n\ge
\frac{c}{32\ell_n^{5/2}}|g_n'(0)|
-\frac{768\beta^{6L}Y}{\lambda n^2}.
\tag{23}
\]
This is an estimate for the actual nonlinear predictors, with no
infinitesimal-label approximation or width-independent \(O(Y^3)\) error.

Fix a query with \(\sigma=\sigma(v_0,y)>0\). For each \(u>0\), (8) and
(23) give, for every fixed allowed \(c\),
\[
\liminf_{n\to\infty}
\Pr\left\{\mathcal D_n\ge
 \frac{uc\sigma}{64\sqrt n\,\ell_n^{5/2}}\right\}
 \ge 2[1-\Phi(u)].
\tag{24}
\]
The explicit deterministic remainder is harmless once
\[
n^{3/2}\ge
\frac{49152\beta^{6L}Y}{\lambda c\,u\sigma}\ell_n^{5/2}.
\tag{25}
\]
Indeed on \(|g_n'(0)|\ge u\sigma/\sqrt n\), (25) makes it at most
half the first term of (23). The Gaussian limit has no atom at this
threshold, and the probability of either localized source failure tends
to zero. These observations prove (24), without an independence
assumption between the source event and the initial derivative.

Taking \(c=\chi(S)/\lambda\), the general conclusion is
\[
\liminf_{n\to\infty}
\Pr\left\{\mathcal D_n\ge
\frac{u\,\chi(S)\,\sigma(v_0,y)m}
 {64\gamma\sqrt n\,\log(en)^{5/2}}\right\}
 \ge2[1-\Phi(u)].
\tag{26}
\]
One may replace \(\chi(S)\) by the activation/depth constant
\(\chi_{\rm act}\) in the full recurrence-based label range; under (5)
one may replace it by one. The witnessing time belongs to
\([0,\chi(S)m/(\gamma\sqrt{\log(en)})]\) and can depend on the run.
This is a bound in the full all-time, whole-sphere norm. It is not a
lower bound on a fitted endpoint.

For prescribed \(0<\delta<1\), put
\(u_\delta=\Phi^{-1}(1/2+\delta/4)>0\). The right side of (26) is
\(1-\delta/2\). Consequently, for each individual \(n\ge N(\delta)\),
the event in (26) holds with probability at least \(1-\delta\), for
some finite but unquantified \(N(\delta)\). Both the CLT remainder and
the source success width are unquantified. There is no simultaneous
event over infinitely many independent widths.

The uncapped \(c=c_{\max}(S)\) in (24) is also valid and can give a
larger fixed-label coefficient. Its inverse-\(Y^2\) dependence comes
with the additional width gates (14), (25); it is nonuniform as
\(Y\downarrow0\). Formula (26) is the useful training-timescale form.

Any proved lower estimate on (6) can now be substituted without another
nonlinear argument. In particular, if
\(\sigma(v_0,y)\ge c_*Y\sqrt{\gamma/m}\), then the threshold in (26)
is at least
\[
\frac{u\chi(S)c_*}{64}\,
\frac{Y\sqrt{m/\gamma}}{\sqrt n\,\ell_n^{5/2}}.
\tag{27}
\]
This particular variance estimate does not follow merely from a positive
gap by the present argument. The bridge retains the full \(m/\gamma\)
time factor multiplying whichever variance estimate is proved.

When \(\sigma(v_0,y)=0\), this query only gives the zero lower threshold.
A positive result covering every \(m\ge1\) needs this qualification:
with one training sample and a nonzero constant last activation,
\(\gamma>0\) but both dense predictors coincide at all times. This
does not rule out a separate nondegeneracy result for \(m\ge2\).

## 5. Tuning the approximations against actual dense variability

Fix \(u>0\), a query with \(\sigma>0\), and abbreviate only in this
section
\[
P=\frac{u\chi(S)\sigma}{64\lambda}>0,\qquad
L_n=\frac P{\sqrt n\,\ell_n^{5/2}}.
\tag{28}
\]
The actual labels remain in \(\sigma\), \(Y\), and \(P\).

Under the simple label cap (5), let \(q_0(n)\) be the latest numerical
order from SAMPLE_POLYNOMIAL_STATEMENT.md (5), and in the next display
take \(C_n=YP_n\), \(q_{\rm abs}=P_n\), with that note's explicit
\(P_n\). Its proof controls the upper-bound expression itself.
For the larger recurrence-based label allowance, instead use
EXPLICIT_LEGENDRE_COMPARISON.md (6) and its \(C_n,q_{\rm abs}\).
Both choices obey
\[
E_n(q)=C_n\frac{\sqrt{\log(eq)}}{q^2},\qquad
E_n(q_0)\le Y/\sqrt n,\qquad q_0\ge q_{\rm abs},
\tag{29}
\]
The comparison holds for every \(q\ge q_{\rm abs}\) on one good event.
Take
\[
q_1(n)=\lceil q_0(n)\ell_n^{3/2}\rceil.
\tag{30}
\]
The established \(q_0=n^{1/4+o(1)}\) implies
\(\log(eq_0)/\ell_n\to1/4\). Moreover
\[
q_0\ell_n^{3/2}\le q_1\le2q_0\ell_n^{3/2},\qquad
\log(eq_1)\le\log(eq_0)+\log2+\tfrac32\log\ell_n.
\]
Thus the logarithm ratio tends to one and is at most four eventually.
Using (29),
\[
\|f_{n,q_1}-f_n\|_*
\le\frac{2Y}{\sqrt n\,\ell_n^3},\qquad
\frac{\|f_{n,q_1}-f_n\|_*}{L_n}
\le\frac{2Y}{P\sqrt{\ell_n}}\longrightarrow0.
\tag{31}
\]
The moving count is still
\[
n(d+1)+1+2(L-1)mnq_1=n^{5/4+o(1)}.
\tag{32}
\]
The realization additionally retains \((L-1)n^2\) fixed mixer entries;
(32) is not its total retained storage.

A finite-width order targeting \(\eta L_n\), for fixed \(\eta>0\),
can instead be obtained by the exact algebraic inversion
\[
Q_n=\max\left\{3,q_{\rm abs},
n^{1/4}\ell_n^{5/4}\sqrt{\frac{C_n}{\eta P}}\right\},
\qquad
q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil.
\tag{33}
\]
For \(Q_n\ge3\), the ceiling gives
\(q_n\le5Q_n[\log(e+Q_n)]^{1/4}\) and hence
\(\log(eq_n)\le4\log(e+Q_n)\). Its lower bound then gives
\[
\frac{C_n\sqrt{\log(eq_n)}}{q_n^2}
\le\frac{C_n}{8Q_n^2}\le\eta L_n/8.
\]
In particular the error is at most \(\eta L_n\). The factors added here
are logarithmic or fixed-data factors, so the exponents in (32) do
not change.

For the autonomous compact model, leave its source accuracy
\(\epsilon=n^{-1}\), selected records, horizon, and runtime unchanged.
The raw comparison proved in source (49) is
\[
\|f_C-f_n\|_*
\le C_{\rm out}n^{-1}e^{a_0+b_0\sqrt{\ell_n}}
       +C_{\rm tail}e^{-8\ell_n},
\tag{34}
\]
with the explicit constants of source §13, independent of width.
Therefore
\[
\frac{\|f_C-f_n\|_*}{L_n}
\le\frac{C_{\rm out}}P n^{-1/2}\ell_n^{5/2}
                  e^{a_0+b_0\sqrt{\ell_n}}
 +\frac{C_{\rm tail}}P n^{-15/2}\ell_n^{5/2}
\longrightarrow0 .
\tag{35}
\]
For the first term its logarithm is
\(-\tfrac12\log n+b_0\sqrt{\ell_n}+\tfrac52\log\ell_n+O(1)\),
which tends to minus infinity. The second term has the displayed
negative power of \(n\). Thus no smaller source tolerance or additional
retained state is needed.

An explicit additional deterministic test for error at most \(\eta L_n\)
is
\[
\begin{gathered}
\ell_n\ge\max\{8a_0,64b_0^2,2\},\\
n^{1/4}\ge
\frac{2e^{1/4}C_{\rm out}}{\eta P}\ell_n^{5/2},\qquad
n^{15/2}\ge\frac{2C_{\rm tail}}{\eta P}\ell_n^{5/2}.
\end{gathered}
\tag{36}
\]
The first line makes the exponent in (34) at most \(\ell_n/4\);
the other two inequalities allocate half of the target to each term.
All hold eventually, in addition to the original construction and
stochastic width gates.

For the full recurrence-based label scope the original source storage
formula is unchanged. Under the simple cap (5), its existing explicit
power envelope is consequently still
\[
\begin{aligned}
\operatorname{size}(C)\le{}&
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
 \left(\frac{Ym}{\gamma}\right)^4\ell_n^{3d+2}\\
&+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{aligned}
\tag{37}
\]
The finite-query localization was solely a lower-bound proof device.
The compressor still approximates every query on the original sphere;
its dimension and actual fourth power of \(Y\) have not changed.

Intersect the two localized lower-bound events with the whole-sphere
comparison events for both independent dense runs. The finitely many
extra failure probabilities tend to zero, with no independence required.
Thus the joint liminf success probability remains \(2[1-\Phi(u)]\).
The choice \(u_\delta\) above leaves a margin of \(\delta/2\) for these
failures and convergence errors, so joint probability is at least
\(1-\delta\) for every sufficiently large individual width. On this
event both approximation errors are \(o(\mathcal D_n)\). Approximating
both runs preserves their separation by the triangle inequality once
their errors sum to less than \(L_n\).

These are sufficient storage counts for error smaller than actual dense
variability. They do not prove storage lower bounds against arbitrary
representations. The argument also does not prove an endpoint lower
bound or an effective stochastic/CLT width.
