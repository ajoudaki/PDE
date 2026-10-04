# Early variability and accuracy-to-storage algebra

2026-10-04. General depth and layer-dependent activations. The initialized
fluctuation theorem below is transferred, with explicit authorization, from
the complete `closure_sampling_20261003/INTEGRATED_INITIAL_VARIABILITY.md`
(SHA-256 `97cdb707c082acf1579e3f73fea6d448e6941a0a06e98568fc4383b3f93a5c6d`)
and its complete internal check
`INTEGRATED_INITIAL_VARIABILITY_CHECK.md`
(SHA-256 `59dccafe35e9aabdae786c568f49916a2ca054c3cb55f9c603d1dd2a5d743938`).
Neither requires an additional scientific proof dependency. The current
study's complete `GENERAL_EXPLICIT_FITTING.md` supplies the real fitting
theorem and its uniform endpoint tail.

The initialization and onset statements below are proved component results.
The accuracy-to-storage section is algebra conditional on separately proved
comparison bounds with the displayed shapes. It supplies no numerical
comparison constant and does not certify the proposed compact theorem.

## 1. Model, common norm, and zero readout

Let \(m,d\ge1\), \(L\ge2\), and \(v_a=x_a/\sqrt d\in\mathbb R^d\)
have unit norm. For a width \(n\), use

\[
h^{(1)}(v)=\phi_1(Av),\qquad
h^{(\ell)}(v)=\phi_\ell(W^{(\ell)}h^{(\ell-1)}(v)),\qquad
f_n(v)=w^\top h^{(L)}(v)/n.
\]

Here \(A\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and
\(w\in\mathbb R^n\). Initialize their entries independently with laws
\(N(0,1)\), \(N(0,1/n)\), and the deterministic value zero, respectively.
Each activation is real \(C^2\), with bounded first and second derivatives
and finite value at zero. These hypotheses allow unbounded activation
values and do not require normalization, centering, oddness, or a common
activation across layers.

For labels \(y\in\mathbb R^m\), let
\(Y=\|y\|_2/\sqrt m\). Train the mean squared residual with mobility
\(n\) on \(A,w\) and mobility one on the other matrices, exactly as in
`GENERAL_EXPLICIT_FITTING.md`. When comparing full predictor trajectories,
use the single norm

\[
\|f-g\|_{\mathrm{sphere},\infty}
=\sup_{t\ge0}\sup_{\|v\|_2=1}|f(t,v)-g(t,v)|.
\tag{1}
\]

If both predictors have uniform endpoint limits, this bound also controls
their endpoint difference. A fixed query or a time derivative is a
different observable and will be identified explicitly.

For every initialization and every query,

\[
f_n(0,v)=0.
\tag{2}
\]

In particular two independent dense initializations have identically equal
initial predictions. Their random initialized features can nevertheless
produce different initial time derivatives. No initial-predictor variance
is inferred from feature randomness.

## 2. Initialized covariance and its fluctuation recursion

Fix one further unit query \(v_0\), and keep \(m,d,L\) fixed as
\(n\to\infty\). All indices in this section run through \(0,1,\ldots,m\).
For initialized features, define

\[
K_{n,ab}^{(\ell)}
=\frac1n h_0^{(\ell)}(v_a)^\top h_0^{(\ell)}(v_b),
\qquad Q^{(0)}_{ab}=v_a^\top v_b.
\]

For a positive semidefinite covariance \(C\), define the Gaussian moment
map and the deterministic recursion by

\[
\Psi_\ell(C)_{ab}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],\quad Z\sim N(0,C),
\qquad Q^{(\ell)}=\Psi_\ell(Q^{(\ell-1)}).
\tag{3}
\]

Identify symmetric matrices with their upper triangular entries when
taking their covariance or the transpose of a linear map. Define the
innovation covariance

\[
B_{\ell,ab,cd}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)
             \phi_\ell(Z_c)\phi_\ell(Z_d)]
 -Q^{(\ell)}_{ab}Q^{(\ell)}_{cd},
\quad Z\sim N(0,Q^{(\ell-1)}),
\tag{4}
\]

and the linear map \(T_\ell\) on symmetric perturbations \(E\) by

\[
\begin{aligned}
(T_\ell E)_{ab}={}&
\tfrac12 E_{aa}\mathbb E[\phi_\ell''(Z_a)\phi_\ell(Z_b)]
+E_{ab}\mathbb E[\phi_\ell'(Z_a)\phi_\ell'(Z_b)]\\
&+\tfrac12 E_{bb}\mathbb E[\phi_\ell(Z_a)\phi_\ell''(Z_b)].
\end{aligned}
\tag{5}
\]

For \(a=b\), the coefficient becomes
\(E_{aa}\mathbb E[(\phi_\ell')^2+\phi_\ell\phi_\ell'']\).
Every expectation in (3)--(5) is a specified finite-dimensional Gaussian
integral; singular covariance matrices are allowed.

The joint initialized central limit theorem is

\[
\sqrt n(K_n^{(\ell)}-Q^{(\ell)})\ \Longrightarrow\ \Xi_\ell,
\qquad
\Xi_0=0,\qquad \Xi_\ell=T_\ell\Xi_{\ell-1}+G_\ell,
\tag{6}
\]

where the \(G_\ell\) are independent centered Gaussian symmetric matrices
with covariances \(B_\ell\). Consequently the covariance \(C_\ell\) of
\(\Xi_\ell\) is given completely by

\[
C_0=0,\qquad C_\ell=T_\ell C_{\ell-1}T_\ell^\top+B_\ell.
\tag{7}
\]

Here is the proof, including the two points needed for general activations.
Conditional on the preceding initialized layers, each layer is an average
of \(n\) independent random matrices
\(\phi_\ell(Z_i)\phi_\ell(Z_i)^\top\), with Gaussian covariance
\(K_n^{(\ell-1)}\). Their mean is
\(\Psi_\ell(K_n^{(\ell-1)})\). Linear growth of the activations supplies
uniform moments of every fixed order on bounded covariance sets.
Conditional Chebyshev and induction first give
\(K_n^{(\ell)}\to Q^{(\ell)}\) in probability.

For a centered conditional summand \(X_i\) and any fixed linear
functional \(u\), the conditional characteristic function is

\[
\mathbb E[e^{i\langle u,X_i\rangle/\sqrt n}\mid\mathcal F_{\ell-1}]
=1-\frac{\operatorname{Var}(\langle u,X_i\rangle\mid
                 \mathcal F_{\ell-1})}{2n}+O(n^{-3/2}).
\]

The remainder is uniform on bounded covariance sets, by the third absolute
moment and the third-order scalar exponential remainder. Raising this
expression to the power \(n\) gives the characteristic function with
covariance \(B_\ell\), in probability. Its modulus is at most one, so
the convergence is also in \(L^1\). Multiplying by characteristic
functions of the earlier fluctuations proves joint convergence with an
independent new Gaussian innovation.

To propagate the conditional mean, differentiate the Gaussian density and
integrate twice by parts. For nonsingular covariances this gives (5).
For a feasible increment \(E\), add \(\varepsilon I\) to the full segment
from \(Q\) to \(Q+E\), apply the integrated identity, and let
\(\varepsilon\downarrow0\). The bounded activation derivatives and
linear activation growth justify the integrations and limit by Gaussian
moment domination. Coupling all Gaussian vectors by their continuous
positive square roots proves continuity of the derivative expectations.
The integrated identity consequently gives

\[
\Psi_\ell(Q+E)-\Psi_\ell(Q)-T_\ell(Q)E=o(\|E\|)
\]

even at a singular \(Q\), for feasible positive semidefinite increments.
Apply this to the preceding tight fluctuation and combine with the
conditional Gaussian innovation to obtain (6)--(7). No independence of
trained features is part of this proof.

## 3. Exact onset calibration and its limits

Let \(\kappa_n=(K_{n,0a}^{(L)})_{a=1}^m\). Since the readout is zero,
all hidden initial velocities vanish. The readout velocity is
\(\dot w(0)=2\sum_a y_a h_0^{(L)}(v_a)/m\). Therefore

\[
\dot f_n(0,v_0)=\frac2m\kappa_n^\top y.
\tag{8}
\]

For a second independently initialized dense copy \(\widetilde f_n\),
(6) gives

\[
\sqrt n\,[\dot f_n(0,v_0)-\dot{\widetilde f}_n(0,v_0)]
\Longrightarrow N(0,\sigma_{\rm onset}^2),\qquad
\sigma_{\rm onset}^2
=\frac8{m^2}\sum_{a,b=1}^m y_a C_{L,0a,0b}y_b.
\tag{9}
\]

If \(Y>0\), put \(u=y/(\sqrt mY)\), so \(\|u\|_2=1\). Then

\[
\sigma_{\rm onset}^2
=\frac{8Y^2}{m}\sum_{a,b}u_a C_{L,0a,0b}u_b.
\tag{10}
\]

This preserves both the actual label scale and its direction. When
\(\sigma_{\rm onset}>0\), let \(\Phi\) denote the standard normal
distribution function. For every fixed \(c>0\),

\[
\Pr\!\left\{
|\dot f_n(0,v_0)-\dot{\widetilde f}_n(0,v_0)|>c/\sqrt n
\right\}
\longrightarrow2[1-\Phi(c/\sigma_{\rm onset})].
\tag{11}
\]

Thus this is a genuine asymptotic lower calibration for the onset
observable, with explicit limiting Gaussian quantiles. It is not a
finite-width probability threshold with an explicit remainder. It is not
a statement about a growing \(m,d,L\), nor a claim that finite-width
endpoint variances converge.

Positive training covariance gap does not force
\(\sigma_{\rm onset}>0\). For example, take \(m=1\) and a nonzero constant
last activation \(\phi_L\equiv c\). Its training covariance gap is
\(c^2>0\), but all initialized feature Gram entries are deterministic,
and every dense run has the same predictor
\(f_n(t,v)=y(1-e^{-2c^2t})\). All cross-run variability vanishes. This
example obeys the real derivative assumptions and the bounded-derivative
strip assumptions, at every depth. No uniform positive lower constant is
available over the stated activation class. If \(Y=0\), all predictors
remain zero, also making every variance zero.

Nor does (11) imply an order-\(n^{-1/2}\) lower bound in (1): converting a
time derivative at zero into a predictor difference needs a time interval
and a remainder estimate uniform at that scale. It supplies no endpoint
lower bound. In particular, at every fitted training input both dense
copies converge to the same prescribed label, even when the onset
variance at that input is positive.

For clarity, there is also an exact infinitesimal-label observable.
Replace the labels by \(\eta y\), let \(f_n^\eta\) be the actual dense
trajectory, and define
\(F_n(t,v)=\partial_\eta f_n^\eta(t,v)|_{\eta=0}\).
Write \(K_n=(K_{n,ab}^{(L)})_{a,b=1}^m\). At finite times,

\[
F_n(t,v_0)
=\kappa_n^\top\left[\int_0^t\frac2m e^{-2sK_n/m}\,ds\right]y.
\tag{12}
\]

The hidden label derivative vanishes because each hidden update contains
both a residual and a readout, which are zero at \(\eta=0\). The readout
label derivative therefore solves the fixed initialized linear equation
giving (12). When \(K_n>0\), the actual fitted endpoint is differentiable
at zero label and

\[
F_n(\infty,v_0)=\kappa_n^\top K_n^{-1}y.
\tag{13}
\]

Indeed, at a fixed finite initialization with positive gap, a small-label
bootstrap gives readout \(O_n(|\eta|)\), exponentially decaying residual
\(O_n(|\eta|e^{-c_nt})\), and integrated hidden motion \(O_n(\eta^2)\).
The resulting training kernel differs from \(K_n\) by \(O_n(\eta^2)\)
uniformly in time. Variation of constants bounds the time integral of
the nonlinear residual minus its linear response by \(O_n(|\eta|^3)\).
Integrating the readout equation proves
\(f_n^\eta(\infty,v_0)=\eta\kappa_n^\top K_n^{-1}y+O_n(|\eta|^3)\),
which justifies (13) at the endpoint itself.

Let \(Q\) and \(\kappa\) be the training block and query row of
\(Q^{(L)}\), and suppose \(Q>0\). The differential of (13) on an augmented
Gram perturbation \(E\) is

\[
E_{0X}Q^{-1}y-\kappa^\top Q^{-1}E_{XX}Q^{-1}y.
\tag{14}
\]

Applying (6) gives its Gaussian fluctuation, with twice the variance for
two independent copies. One may assign an arbitrary fixed value on the
exceptional event \(K_n\not>0\), whose probability tends to zero; no
nonlinear fitting conclusion is made on that exceptional event. At a
training query, (14) cancels exactly. None of these derivative statements
proves a fixed nonzero-label endpoint lower bound: even a width-uniform
single-run remainder \(O(Y^3)\) is insufficient after multiplication by
\(\sqrt n\). A two-copy nonlinear remainder at scale \(o(Y/\sqrt n)\),
or a comparably strong quantitative substitute, remains necessary.

## 4. Separately parameterized comparison and storage bounds

Fix a confidence allocation and the other problem parameters. The
symbols \(A_{\rm comp}(Y)\) and \(A_{\rm dense}(Y)\) below denote only the
coefficients of actual comparison theorems, once those theorems and their
hypotheses have been verified. They are not defined by the desired answer,
the initialized CLT, or an unproved numerical benchmark. Dependence on
\(d,m,L,\gamma\), activations, confidence, and possibly the normalized
label direction is suppressed; dependence on the actual \(Y\) is shown.

Suppose those theorems supply, on specified simultaneous events,

\[
\|f_{n,\rm comp}-f_n\|_{\mathrm{sphere},\infty}
\le\frac{A_{\rm comp}(Y)}{\sqrt n},\qquad
\|f_n-\widetilde f_n\|_{\mathrm{sphere},\infty}
\le\frac{A_{\rm dense}(Y)}{\sqrt n}.
\tag{15}
\]

Here the first comparison is to its source dense run; the second is
between independent dense initializations. For budgets
\(\varepsilon_{\rm comp}+\varepsilon_{\rm dense}\le\varepsilon\), choose

\[
n_\varepsilon=\left\lceil\max\left\{
N_0,
\left(\frac{A_{\rm comp}(Y)}{\varepsilon_{\rm comp}}\right)^2,
\left(\frac{A_{\rm dense}(Y)}{\varepsilon_{\rm dense}}\right)^2
\right\}\right\rceil,
\tag{16}
\]

where \(N_0\ge1\) includes the fitting threshold and every required
comparison threshold. Triangle inequality then gives accuracy
\(\varepsilon\) to the independent dense run. Failure probabilities are
added for the events actually used; their statistical independence is
unnecessary. To approximate only the source dense run, omit the dense
term and set \(\varepsilon_{\rm comp}=\varepsilon\).

The exact dense parameter storage, per run, is

\[
S_{\rm dense}(n)=nd+(L-1)n^2+n.
\tag{17}
\]

Substituting (16) gives its accuracy-dependent count. For fixed nonzero
comparison coefficients and fixed thresholds, it grows as
\(\varepsilon^{-4}\) as \(\varepsilon\downarrow0\), with the coefficients
and actual \(Y\) retained by (16). This is a sufficient count deduced
from (15), not a necessary predictor-storage bound from the onset CLT.

The proposed compact result has the following distinct target shape for
**all retained storage**, at the original dense width \(n\):

\[
S_{\rm comp}(n)
\le B_{\rm comp}(Y)[\log(en)]^{3d+2}+C_{\rm base}.
\tag{18}
\]

There is no extra multiplier \(n\) in (18).
The coefficient \(B_{\rm comp}(Y)\) must come from the actual construction
and its retained records; replacing \(Y\) by an admissibility cap would
discard its amplitude dependence. The term \(C_{\rm base}\) accounts for
any fixed base records under the same counting convention. If (18) and
the first comparison in (15) are proved, their exact inversion is

\[
S_{\rm comp}(\varepsilon)
\le B_{\rm comp}(Y)
\left[\log\!\left(e\left\lceil
\max\{N_0,(A_{\rm comp}(Y)/\varepsilon)^2\}
\right\rceil\right)\right]^{3d+2}+C_{\rm base}.
\tag{19}
\]

For independent-dense accuracy use \(n_\varepsilon\) from (16) inside
\(\log(en_\varepsilon)\). Thus the proposed compact sufficient storage
is polylogarithmic in \(1/\varepsilon\) at fixed problem parameters,
with no \(\varepsilon^{-2}\) prefactor. Equations (18)--(19) are explicitly
conditional on the compact storage and comparison theorems; the present
note proves their algebra only.

## 5. Legendre order and the retained mixer distinction

An order-\(q\) Legendre memory realization with one clock has the exact
moving-state count

\[
S_{\rm Leg,moving}(n,q)
=nd+n+1+2(L-1)mnq.
\tag{20}
\]

It also retains \((L-1)n^2\) initialized mixer entries. Counting all
retained coefficients therefore gives

\[
S_{\rm Leg,retained}(n,q)
=S_{\rm Leg,moving}(n,q)+(L-1)n^2.
\tag{21}
\]

The following calculation preserves the inherited Legendre error shape.
It is an inversion of an applicable upper bound, not a proof of that
bound's hypotheses or constants. Suppose its verified form is

\[
\|f_{n,q}-f_n\|_{\mathrm{sphere},\infty}
\le A_{\rm Leg}(Y)q^{-2}
\exp\!\bigl(K_{\rm Leg}(Y)\sqrt{\log(en)}\bigr)
\sqrt{\log(eq)},\qquad K_{\rm Leg}(Y)\ge0.
\tag{22}
\]

For any desired matching coefficient \(C_{\rm Leg}(Y)>0\), abbreviate
\(K=K_{\rm Leg}(Y)\), set \(N=\log(en)\), and choose

\[
D=\max\left\{1,\frac{A_{\rm Leg}(Y)}{C_{\rm Leg}(Y)}(3+K)\right\},
\qquad
q_n=\left\lceil Dn^{1/4}e^{K\sqrt N/2}N^{1/4}\right\rceil.
\tag{23}
\]

This explicit choice makes (22) at most
\(C_{\rm Leg}(Y)/\sqrt n\). To check the logarithmic factor, the expression
inside the ceiling is at least one, so

\[
\log(eq_n)
\le [3/2+\log(2D)+K/2]N
\le (3+K)^2D^2N.
\]

The first inequality uses \(N\ge1\), \(\sqrt N\le N\), and
\(\log N\le N\); the second uses \(\log D\le D^2/2\), \(D\ge1\),
and \(K\ge0\). Substituting the lower bound for \(q_n\) into (22)
then gives at most
\(A_{\rm Leg}(Y)(3+K)/(D\sqrt n)\le C_{\rm Leg}(Y)/\sqrt n\).

For fixed coefficients,

\[
q_n=n^{1/4+o(1)},\qquad
S_{\rm Leg,moving}(n,q_n)=n^{5/4+o(1)},\qquad
S_{\rm Leg,retained}(n,q_n)=\Theta(n^2).
\tag{24}
\]

The last equality uses \(L\ge2\): at least one dense initialized mixer
remains. To obtain an absolute accuracy budget, require additionally
\(n\ge(C_{\rm Leg}(Y)/\varepsilon_{\rm Leg})^2\) and retain all width
thresholds of (22). At fixed coefficients this gives sufficient moving
storage \(\varepsilon^{-5/2+o(1)}\), while total retained storage remains
of order \(\varepsilon^{-4}\). These counts describe this Legendre
realization and this sufficient error bound; they do not prove a lower
bound against other representations.

## 6. What the real fitting theorem already supplies

Unlike the conditional comparison templates, the general fitting note
already proves a uniform sphere endpoint tail. With
\(\lambda=\gamma/m\), its constants \(H,F\), and the actual label size
\(Y\), it gives

\[
\sup_{\|v\|=1}|f_n(\infty,v)-f_n(t,v)|
\le C_{\rm tail}(Y)e^{-\lambda t/2},\qquad
C_{\rm tail}(Y)=16\left(H^2+\frac{FY^2}{\lambda}\right)\frac Y\lambda.
\tag{25}
\]

For \(Y>0\), endpoint error at most \(\varepsilon_{\rm tail}\) is therefore
ensured by

\[
T_\varepsilon=
\max\left\{0,\frac2\lambda
\log\frac{C_{\rm tail}(Y)}{\varepsilon_{\rm tail}}\right\}.
\tag{26}
\]

If \(Y=0\), the network is stationary and \(T_\varepsilon=0\).
Stopping a full dense trajectory at this time controls its own endpoint
tail; it does not construct the compact representation in (18), prove
the comparison bounds in (15), or upgrade onset variability to a fixed-label
predictor lower bound. Those are separate statements with separate proof
obligations.
