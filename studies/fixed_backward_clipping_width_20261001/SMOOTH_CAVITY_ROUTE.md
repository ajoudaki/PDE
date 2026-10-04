# Smooth clipping: scalar freezing, response concentration, and a differentiated cavity estimate

2026-10-01. Scoped theoretical route. This is a candidate partial argument,
not a complete proof of the requested width-to-population theorem and not a
promotion. The central missing step is stated in Section 7. In particular,
the population is never defined by a finite-width mean.

## 1. Contract and complete inputs

The model and target are exactly `SMOOTH_SETUP.md`: two hidden tanh layers,
order-one memory reconstruction, independent Gaussian first rows and middle
matrix, zero initial readout and values, matching initial keys, and clock one.
The clipping map is

\[
c_M(q)=M\tanh(q/M),\qquad M>0
\]

with fixed M independent of width. Labels have fixed sufficiently small RMS
Y, and the initial population readout-feature Gram has a positive fixed gap.
The same initialized matrix and its actual transpose are retained. No
experiment, scientific retrieval from another study, manuscript change, or
Git write was performed. Metadata-only status/HEAD/index checks preceded this
owned-file write; unrelated modifications were preserved.

Complete scientific inputs read were:

| Input | SHA-256 |
|---|---|
| `SMOOTH_SETUP.md` | `a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6` |
| `FITTING_AND_THRESHOLD.md` | `edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2` |
| `BIAS_CAVITY_ROUTE.md` | `55291e0646cc53a7a9d484e066bff2830a0ddd947b3f1240f96347440d4f16e8` |
| `RESOLUTION_UPPER_ROUTE.md` | `e165332d3b63a8b70a48b69b00e32850a35d0fdce0ba96b2195071fea4867429` |
| `WEIGHTED_REMAINDER_ROUTE.md` | `3afc3f16ed49ceeb441c943592febcd7cf6b5379d78ce21d2fcf6bbc72b52a33` |
| `CONCENTRATION_ROUTE.md` | `4331e895f388b238ced358cfa101390b80681c3797fa36b5b8ba7e319312d8f5` |
| `CLIPPED_POPULATION_ROUTE.md` | `63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082` |

The required solve-math-rigorously, investigate-conjectures, and
explain-with-canonical-notation skills were read, together with their
research-contract, adversarial-audit, proof-search, and neural-response
references. Supervisor messages emphasized the nonsmooth residual norm,
the failure of dimension-free second differentiation on normalized L2,
and independently suggested scalar freezing and tagged forcing. No sibling
smooth candidate or review verdict was read.

Write \(\psi=\operatorname{sech}^2\), \(u_a=x_a/\sqrt d\), and retain
the agreed exact moment normalizations \(k_a=\bar h_{a,0}/\tau\) and
\(v_a=-2\bar\delta_{a,0}\). The complete finite system is

\[
\begin{gathered}
\alpha_a=Au_a,\quad h_a=\tanh\alpha_a,\quad
B=W_0+\frac1{mn}\sum_bv_bk_b^\top,\\
z_a=Bh_a,\quad g_a=\tanh z_a,\quad
f_a=w^\top g_a/n,\quad r_a=f_a-y_a,\quad
\rho=\|r\|_2/\sqrt m,\\
d_a=c_M(w\odot\psi(z_a)),\quad
\ell_a=c_M(\psi(\alpha_a)\odot B^\top d_a),\\
\dot A=-\frac2m\sum_a r_a\ell_a u_a^\top,\quad
\dot w=-\frac2m\sum_a r_ag_a,\quad
\dot v_a=-2r_ad_a,\\
\dot k_a=\frac\rho\tau(h_a-k_a),\qquad \dot\tau=\rho.
\end{gathered}                                                    \tag{1}
\]

The true output derivative contains \(p_a=w\odot\psi(z_a)\), not \(d_a\).
These are never identified below. Dots denote physical time.

## 2. Smooth scalar gates and first-difference estimates

Set \(F(\alpha,p)=M\tanh(p\psi(\alpha)/M)\). Every derivative of positive
total order of F is bounded on \(\mathbb R^2\). Here is an explicit reason
which also deals with an unbounded carrier p. For each j,
\(\psi^{(j)}(\alpha)=\psi(\alpha)P_j(\tanh\alpha)\), for a polynomial
\(P_j\), by induction using \((\tanh\alpha)'=\psi(\alpha)\). Put
\(x=p\psi(\alpha)/M\). Repeated differentiation expresses a mixed derivative
with b derivatives in p as a finite sum of terms

\[
 M^{1-b}\psi(\alpha)^bP(\tanh\alpha)
 x^j\tanh^{(b+j)}x.                                             \tag{2}
\]

If b=0 and at least one alpha derivative is taken, j is positive. Otherwise
b+j is positive. The positive derivatives of tanh decay exponentially at
both infinities, as follows by differentiating its rational expression in
\(e^{2x}\). Thus every term in (2) is bounded. In particular F has bounded
first, second, and third derivatives, with constants depending on M.

This does **not** assert that the full vector field of (1) is smooth at
\(r=0\), or that a coordinatewise F is twice differentiable with a uniform
bilinear bound in normalized L2. The latter inference would use the false
dimension-free estimate for pointwise products. Higher variations below
are handled by actual coordinate moment bounds.

The fitting proof in `FITTING_AND_THRESHOLD.md` uses only
\(|c_M(q)|\le |q|\), not top inactivity, until its final threshold assertion.
Therefore its fitting and finite-activity conclusions carry over unchanged.
On the good initialization event

\[
\mathcal G_n=\{\|W_0\|_{\rm op}\le K,
\quad \Gamma_w(0)\succeq\lambda I_m\},
\qquad
\Gamma_{w,ab}(0)=g_a(0)^\top g_b(0)/(mn),                         \tag{3}
\]

fixed sufficiently small Y gives

\[
\rho(t)\le Ye^{-\kappa t},\qquad
\int_0^\infty\rho\le S_*,\qquad
\|w\|_\infty\le2S_*,\quad
\|v_a\|_\infty\le2\sqrt m S_*^2,\quad\|k_a\|_\infty\le1.        \tag{4}
\]

The elementary initialization calculation in the concentration input gives
\(\Pr(\mathcal G_n^c)\le C/n\) with a larger population gap. All constants
in this note may depend on fixed data, M, margins, and cutoffs, but never
on width or physical horizon.

For completeness, the exact residual identity used for stability is

\[
\dot r_b=-\frac2m\sum_a r_a(K^0_{ba}+K^A_{ba}+K^v_{ba})+\rho Q_b,
\tag{5}
\]
\[
\begin{aligned}
K^0_{ba}&=g_b^\top g_a/n,\\
K^A_{ba}&=(u_a^\top u_b)\,p_b^\top
B(\psi(\alpha_b)\odot\ell_a)/n,\\
K^v_{ba}&=(p_b^\top d_a/n)(k_a^\top h_b/n),\\
Q_b&=\frac1{m\tau}\sum_a(p_b^\top v_a/n)
                         ((h_a-k_a)^\top h_b/n).
\end{aligned}
\]

Differentiating the reconstruction and then the prediction proves (5).
The factors p and d remain distinct. Bounded first derivatives of F,
the coordinate bound on ell, and operator bounds for B imply the same
normalized-state Lipschitz estimates for these kernels as in the hard-clip
concentration proof. Consequently two good initializations satisfy

\[
\sup_t D(t)\le C\varepsilon_0,\qquad
\|r^1(t)-r^2(t)\|_m\le Ca(t)\varepsilon_0,\qquad
a(t)=(1+t)e^{-ct},                                               \tag{6}
\]

where D is the sum of normalized Euclidean/Frobenius state differences
and the clock difference, and

\[
\varepsilon_0=\|A_0^1-A_0^2\|_F/\sqrt n+
               \|W_0^1-W_0^2\|_{\rm op}.
\]

Indeed the state and residual differences obey
\(D'\le C\rho^1(D+\|\Delta W_0\|_{\rm op})+CR\) and
\(R'\le-\kappa_1R+C\rho^2(D+\|\Delta W_0\|_{\rm op})\).
Integrate the residual inequality first, substitute into the state
inequality, and apply Gronwall with integrable coefficient
\(C(\rho^1+\rho^2)\). The residual convolution then gives (6).

## 3. Actual scalar histories can be frozen at their finite-width means

This step avoids a Taylor expansion in the empirical residual norm and
avoids a mixed row-and-scalar-history cavity remainder.

Define the actual scalar contractions

\[
K_{ba}(t)=k_b(t)^\top h_a(t)/n,\qquad
V_{ba}(t)=v_b(t)^\top d_a(t)/n,\qquad
\theta_n=(r,\rho,\tau,K,V).
\tag{7}
\]

Let \(\bar\theta_n(t)=\mathbb E[\theta_n(t)\mid\mathcal G_n]\),
componentwise. These are deterministic functions of time. They are
auxiliary finite-width coefficients, **not** population coefficients.
They satisfy \(\bar\tau_n=1+\int_0^t\bar\rho_n\),
\(|\bar r_a|\le\sqrt m\bar\rho_n\), and the bounds following from (4).

Run the following forced vector system from the same random initialization:

\[
\begin{gathered}
z_a=W_0h_a+\frac1m\sum_bv_b\bar K_{ba},\quad
d_a=F(z_a,w),\\
P_a=W_0^\top d_a+\frac1m\sum_bk_b\bar V_{ba},\quad
\ell_a=F(\alpha_a,P_a),                                         \tag{8}\\
\dot A=-\frac2m\sum_a\bar r_a\ell_a u_a^\top,\quad
\dot w=-\frac2m\sum_a\bar r_a\tanh z_a,\quad
\dot v_a=-2\bar r_ad_a,\quad
\dot k_a=\frac{\bar\rho_n}{\bar\tau_n}(h_a-k_a).
\end{gathered}
\]

Use a tilde for its vector states. This forced system is an intermediate
comparison only; its displayed contractions are not declared to equal
its supplied coefficients.

**Scalar-freezing estimate.** On the conditional initialization law,

\[
\left\|\sup_{t\ge0}\left(
\|A-\widetilde A\|_F/\sqrt n+
\|w-\widetilde w\|_2/\sqrt n+
\sum_a(\|v_a-\widetilde v_a\|_2+
        \|k_a-\widetilde k_a\|_2)/\sqrt n\right)\right\|_{L^2}
\le Cn^{-1/2}.                                                   \tag{9}
\]

Here and below an L2 norm with the good event in this section means
conditioning on \(\mathcal G_n\).

To prove (9), first obtain pointwise scalar fluctuations. Write
\(W_0=G_0/\sqrt n\); (6) shows that a scalar contraction in (7) is
\(C/\sqrt n\)-Lipschitz in all standard Gaussian roots on the good set.
For r and rho the constant is \(Ca(t)/\sqrt n\). Their absolute ranges
on that set are bounded, with exponentially decaying ranges for r and rho.
Extend each scalar by a Lipschitz extension and clip to its known range.
Gaussian Poincare, with its contained proof in the concentration input,
gives variance at most the squared Lipschitz constant. The extension agrees
with the actual variable on the good event. Dividing its mean-square
deviation by \(\Pr(\mathcal G_n)\ge1/2\), and minimizing over deterministic
centers, proves

\[
\|r-\bar r\|_{L^2}+\|\rho-\bar\rho\|_{L^2}
\le Ca(t)/\sqrt n,\qquad
\|K-\bar K\|_{L^2}+\|V-\bar V\|_{L^2}\le C/\sqrt n.              \tag{10}
\]

Also
\(\|\sup_t|\tau-\bar\tau|\|_{L^2}
 \le\int_0^\infty\|\rho-\bar\rho\|_{L^2}\le C/\sqrt n\).
This proof uses no conditional Gaussian independence.

For fixed supplied histories the vector graph (8) is globally Lipschitz in
its vector state with coefficient \(C\bar\rho_n(t)\): every linear map
has a bounded operator norm and every scalar gate has bounded first
derivatives. Both actual and forced trajectories have bounded coordinate
w,v,k by direct integration. Evaluating a coefficient change at the actual
state and using these bounds shows that their normalized state difference
N satisfies

\[
N'\le C\bar\rho_n N+C b_n(t),                                  \tag{11}
\]
\[
b_n=|r-\bar r|+|\rho-\bar\rho|
 +\bar\rho_n\bigl(|K-\bar K|+|V-\bar V|+|\tau-\bar\tau|\bigr).
\]

One may first replace residual coefficients, then replace contractions,
so that the last coefficient is \(\bar\rho_n\). Products from this
sequential replacement are bounded by the first two terms using the
bounded ranges of the other coefficients. Minkowski and (10) give
\(\|\int b_n\|_{L^2}\le C/\sqrt n\). Gronwall in (11) proves (9).

For a passive query x reconstruct a matrix from the forced vector states
with their **actual** normalized pairings. Boundedness and (9) then give
the same root-width comparison of its prediction with the original
prediction, uniformly in time and uniformly over x in a fixed bounded
set. Alternatively, for a Gaussian single-row description of finitely
many query outputs one may include their finitely many K contractions
in (7). They obey the same proof with constants uniform on bounded query
sets. This is still an auxiliary forced model, not population identification.

## 4. A normalized-trace concentration estimate

This section proves concentration of an explicit response functional. It
does not compare its mean with a population response.

Prescribe deterministic coefficient histories obeying (4), with
\(|r_a|\le\sqrt m\rho\), \(\tau\ge1\), bounded K,V, and integrable rho.
These may in particular be the means in Section 3. Let U denote the vector
state of (8), with dimension \(N_n=n(d+1+2m)\). Its vector field is
\(\mathcal F_t(U)\). Define

\[
L(t)=D_U\mathcal F_t(U(t)),\qquad
\partial_t\Phi(t,s)=L(t)\Phi(t,s),\qquad\Phi(s,s)=I.
\tag{12}
\]

The matrices are ordinary finite-dimensional Jacobians with the scalar
histories held fixed. Bounded first derivatives of the local gates imply
\(\|L(t)\|_{\rm op}\le C\rho(t)\) and
\(\|\Phi(t,s)\|_{\rm op}\le e^{CS_*}\).

Add an external vector e to the lower carrier P_b in (8). Let
\(J_b(s):\mathbb R^n\to\mathbb R^{N_n}\) be the coefficient of
\(r_b(s)e\) in the linearized vector field. Only the A equation is
directly changed, and explicitly

\[
J_b(s)e=\left(-\frac2m
        [F_p(\alpha_b(s),P_b(s))\odot e]u_b^\top,0,0,0\right).
\tag{13}
\]

For the lower-feature output \(H_a(U)=\tanh(Au_a)\), define

\[
R^h_{n,ab}(t,s)=\frac1n\operatorname{tr}
    [D H_a(U(t))\Phi(t,s)J_b(s)],\qquad t\ge s.
\tag{14}
\]

Thus the source r_b(s) is not included in the kernel R in (14).

On \(\|W_0\|_{\rm op}\le K\), two initializations with the same prescribed
histories have ordinary normalized state distance at most
\(C\varepsilon_0\), by integrating their first-difference inequality.
Let \(\|T\|_{\mathrm{HS},n}=\|T\|_F/\sqrt n\) for any of the block
matrices appearing here. Differencing the derivative graph gives

\[
\|L^1(t)-L^2(t)\|_{\mathrm{HS},n}
\le C\rho(t)\varepsilon_0.                                    \tag{15}
\]

Here are the dimension factors. A diagonal local derivative changes in
Hilbert--Schmidt norm by at most C times the ordinary Euclidean difference
of its one or two inputs, because the scalar second derivatives are
bounded. Fixed input maps have norms depending only on data. All other
matrix factors have bounded operator norm. A changed W factor has
\(\|\Delta W\|_F/\sqrt n\le\|\Delta W\|_{\rm op}\).
Telescoping the fixed finite number of graph products proves (15).
The same argument gives

\[
\|\Delta D H_a(t)\|_{\mathrm{HS},n}
+\|\Delta J_b(s)\|_{\mathrm{HS},n}\le C\varepsilon_0.
\]

Duhamel's formula in (12), using bounded operator norms on both sides of
the changed factor, gives
\(\|\Delta\Phi(t,s)\|_{\mathrm{HS},n}\le C\varepsilon_0\).
For rectangular factors of the present sizes,

\[
\frac{|\operatorname{tr}(PQ)|}{n}
\le \frac{\|P\|_F\|Q\|_F}{n}
\le C\|P\|_{\mathrm{HS},n}\|Q\|_{\rm op}.
\]

Telescoping (14) therefore proves

\[
\sup_{t\ge s}|R^{h,1}_{n,ab}(t,s)-R^{h,2}_{n,ab}(t,s)|
\le C\varepsilon_0.                                           \tag{16}
\]

The kernel is bounded by C. Its time derivative is the sum of the two
terms obtained by differentiating \(D H_a(U(t))\) and \(\Phi(t,s)\).
Each A-row speed is bounded by \(C\rho(t)\), since ell is bounded.
Consequently \(\|\partial_t DH_a\|_{\rm op}\le C\rho\), and the same
graph argument gives its difference in normalized Hilbert--Schmidt norm
at most \(C\rho\varepsilon_0\). Thus

\[
|\partial_t R^{h,1}_{n,ab}(t,s)
       -\partial_t R^{h,2}_{n,ab}(t,s)|
\le C\rho(t)\varepsilon_0.                                    \tag{17}
\]

Since \(W_0=G_0/\sqrt n\), (16)--(17) are Lipschitz bounds of size
\(C/\sqrt n\) and \(C\rho(t)/\sqrt n\) in standard Gaussian roots.
Extend the initial value at t=s and its velocity separately from the
operator-cutoff set, clipping to their bounds, as in the prediction
concentration proof. Gaussian Poincare and integration of the velocity
give, for each s, a deterministic center \(\bar R^h_{n,ab}(t,s)\) with

\[
\mathbb E\sup_{t\ge s}
 |R^{h,\mathrm{ext}}_{n,ab}(t,s)-\bar R^h_{n,ab}(t,s)|^2
\le C/n.                                                       \tag{18}
\]

The analogous conditional-mean statement on the operator cutoff follows
by the same extension restriction argument used in (10). In particular,
Minkowski permits integration over s against any deterministic integrable
source envelope. No minimum history-Gram eigenvalue is used. The root-width
factor in (18) comes from normalized traces and first root sensitivities,
not from a uniform second derivative on a population L2 space.

## 5. Smooth reinsertion and its tagged forcing derivative

Here is a strengthened local cavity lemma. It supplies a differentiated
cavity estimate directly, rather than differentiating an error bound.

Delete one upper row of W_0 and condition on the remaining matrix and A_0.
Write the independent removed row as \(\omega\sim N(0,I_n/n)\). Prescribe
deterministic scalar histories as in Section 4. In the cavity vector graph,
force the lower carrier by \(\omega\eta_a(t)\). The upper deleted coordinate
is omitted from the cavity state. Let \(U[\eta]\) be the resulting state
and Uc its value at zero forcing. Allow eta to be any measurable function
of the row, bounded by a fixed constant; the usual removed-row backward
path obeys the stronger bound \(|\eta_a(t)|\le Cs(t)\), where
\(s(t)=\int_0^t\rho(u)\,du\) is the prescribed activity.

When taking a directional derivative in eta, its realized path is held
fixed. Let chi be another measurable bounded path and set

\[
T_\eta(t)=\sum_b\int_0^t\Phi(t,s)J_b(s)
                            \omega\eta_b(s)r_b(s)\,ds,
\qquad
V_{\eta,\chi}(t)=D_\eta U[\eta](t)[\chi].                       \tag{19}
\]

All coefficients of T are cavity measurable. The following estimates hold
conditionally on every cavity with bounded operator norm, for each fixed
finite p at least one:

\[
\left\|\sup_t\|U[\eta](t)-U^c(t)-T_\eta(t)\|_2\right\|_{L^p_\omega}
\le C_p/\sqrt n,                                               \tag{20}
\]
\[
\left\|\sup_t\|V_{\eta,\chi}(t)-T_\chi(t)\|_2\right\|_{L^p_\omega}
\le C_p/\sqrt n.                                               \tag{21}
\]

The constants are uniform over those measurable eta,chi choices and the
physical horizon. Dependence on their fixed sup bounds is allowed. Their
linearity in the chi bound will be useful for a source-time envelope.

Here is a proof with the spatial moment calculation exposed. At every
linearized activation input, each tangent coordinate has a common
conditional moment envelope of size \(C_p/\sqrt n\). Indeed, insert (19),
take absolute values before eta, and apply
\(\|q^\top\omega\|_{L^p}\le C_p\|q\|_2/\sqrt n\) to the cavity
kernel row q. Operator norms are bounded and \(\int\rho<\infty\).
For state-coordinate temporal suprema use

\[
\sup_{t\ge s}|e_j^\top\Phi(t,s)J_b(s)\omega|
\le |e_j^\top J_b(s)\omega|
 +\int_s^\infty|e_j^\top L(t)\Phi(t,s)J_b(s)\omega|\,dt.
\]

This yields the same envelope. No independence of eta or chi and omega is
used. For an algebraic node at a fixed time, use its full cavity kernel
row; do not push coordinate envelopes through an operator norm.

If q is a vector of local Taylor defects at a pure tangent input, bounded
second scalar derivatives imply \(|q_j|\le C|t_j|^2\), with a fixed
number of tangent inputs at each node. For p at least two, Minkowski in
Lp/2 gives

\[
\|\|q\|_2\|_{L^p}
\le\left(\sum_{j\le Cn}\|q_j\|_{L^p}^2\right)^{1/2}
\le C_p/\sqrt n.                                               \tag{22}
\]

The cases p below two follow from the p=2 bound. Comparing the nonlinear
graph at Uc+T with its fully linearized graph propagates these defects
through a fixed number of bounded linear/Lipschitz operations. The full
vector field has Lipschitz coefficient \(C\rho(t)\), independently of the
forcing. Gronwall and Minkowski prove (20), for every finite p. The same
argument gives a fixed-time ordinary Lp root-width bound for every
algebraic-node error after its pure tangent is removed.

To prove (21), differentiate the finite-dimensional forced integral equation
with eta varied in direction chi. Bounded first derivatives and integrable
coefficients justify this derivative by difference quotients and Gronwall.
Subtract the equation for Tchi. Its homogeneous coefficient is the actual
state Jacobian, still bounded by \(C\rho(t)\). At a local nonlinear node,
the new source is a derivative difference acting on the pure chi tangent.
Write its actual eta increment as \(t_\eta+e_\eta\). The bounded second
scalar derivatives bound the source by

\[
C|t_\eta t_\chi|+C|e_\eta t_\chi|.                             \tag{23}
\]

The pure product has ordinary Lp norm \(C_p/\sqrt n\), by the same
coordinate calculation as (22). For the second term use

\[
\|e_\eta\odot t_\chi\|_2
\le\|e_\eta\|_2\|t_\chi\|_2,
\]

Hölder, the L2p version of (20) at that node, and the bounded L2p norm of
the ordinary tangent norm. This again is \(C_p/\sqrt n\). The finite graph
propagates these estimates and contributes the common factor rho. Gronwall
proves (21). This proof never uses a normalized-L2 bilinear Hessian bound.
Bounded third derivatives are available if the same construction is
repeated for one additional tagged variation, but that repetition is not
claimed as a substitute for the law-consistency step below.

For the lower-feature output, bounded derivatives and the same product
calculation also give

\[
\begin{aligned}
&\left\|\sup_t\left|
\omega^\top\{H_a(U[\eta])-H_a(U^c)-D H_a(U^c)T_\eta\}
\right|\right\|_{L^p}\le C_p/\sqrt n,\\
&\left\|\sup_t\left|
\omega^\top\{D H_a(U[\eta])V_{\eta,\chi}
                    -D H_a(U^c)T_\chi\}
\right|\right\|_{L^p}\le C_p/\sqrt n.
\end{aligned}                                                   \tag{24}
\]

Use Hölder with \(\|\omega\|_2\), whose every fixed moment is uniformly
bounded. Gaussian quadratic-form centering, integrated against the source
history as in the supplied adaptive linear lemma, replaces the respective
linear terms by

\[
\sum_b\int_0^t\eta_b(s)r_b(s)R^h_{n,ab}(t,s)\,ds,\qquad
\sum_b\int_0^t\chi_b(s)r_b(s)R^h_{n,ab}(t,s)\,ds                \tag{25}
\]

with root-width error, even for row-dependent eta and chi. Thus both the
local field and its response to a bounded tagged forcing have a genuine
trace representation with a controlled remainder.

This lemma also applies to a lower-column deletion with a forward forcing
\(\omega\eta_a\) in z: replace J by the explicit derivative of the full
graph with respect to that additive z input. Its operator norm is bounded
by C after factoring the driving residuals. Initial lower coordinate A0j
does not enter the remaining cavity when K,V are prescribed. Direct
algebraic responses of d must be kept separately; the next section spells
out that distinction.

## 6. What a correct two-sided continuous law must retain

The following describes the necessary candidate law. Its finite-width
consistency and contractivity as a complete law have **not** been proved
in this report. It is included to make the remaining obligation precise.

Use a lower single-neuron state \((A,k_a)\), with \(A(0)\sim N(0,I_d)\),
and an upper single-neuron state \((w,v_a)\), with zero initialization.
Let \(G^h\) and \(G^d\) be centered Gaussian histories on the upper and
lower spaces respectively. Their candidate covariances are

\[
\mathbb E G^h_a(t)G^h_b(s)=\mathbb E_1 h_a(t)h_b(s),\qquad
\mathbb E G^d_a(t)G^d_b(s)=\mathbb E_2 d_a(t)d_b(s).              \tag{26}
\]

The lower root A(0) is independent of its Gaussian cavity history Gd.
Write \(\mathcal R^h_{ab}(t,ds)\) for the mean response of lower h_a(t)
to an additive perturbation of the lower carrier P_b at source time s.
It is absolutely continuous in s, since the lower state evolves by an
ODE, and its density includes the driving residual factor. Write
\(\mathcal R^d_{ab}(t,ds)\) for the analogous response of the upper
trained coefficient d_a(t) to an additive perturbation of z_b.
The candidate fields are

\[
\begin{aligned}
z_a(t)&=G^h_a(t)+\sum_b\int_{[0,t]}
               d_b(s)\mathcal R^h_{ab}(t,ds)
                    +\frac1m\sum_bv_b(t)K_{ba}(t),\\
P_a(t)&=G^d_a(t)+\sum_b\int_{[0,t]}
               h_b(s)\mathcal R^d_{ab}(t,ds)
                    +\frac1m\sum_bk_b(t)V_{ba}(t).
\end{aligned}                                                   \tag{27}
\]

The local ODEs are those in (8). Their response measures are defined by
actual first variations of these local equations with the supplied
covariances, responses, and scalar histories held fixed.

Crucially, \(\mathcal R^d\) contains an instantaneous atom:

\[
\mathcal R^d_{ab}(t,ds)=
\delta_{ab}\,\mathbb E_2 F_z(z_a(t),w(t))\,\delta_t(ds)
                    +\mathcal R^{d,\mathrm{past}}_{ab}(t,s)\,ds,
\tag{28}
\]
\[
F_z(z,w)=-2w\psi(z)\tanh z\,
                \operatorname{sech}^2(w\psi(z)/M).
\]

The past part includes the evolving readout and values and the response
feedback in (27). Deleting the atom in (28) changes the same-matrix
transpose response. It cannot be justified by top inactivity, which does
not hold for this smooth clip. More generally the response is not merely
the derivative of the gate evaluated at the present time; the past part
survives as well.

For fixed small activity, local feedback in the upper equation has size
\(O(S_*^2)\): \(\mathcal R^h\) has total mass \(O(S_*)\), while the
upper d-path map has first response \(O(S_*)\). Lower local feedback also
has an absorbable factor from the residual integral. These observations
support local solvability for prescribed law data. They are not yet a
contraction proof for the full map sending covariances and responses to
their new expectations in (26)--(28).

## 7. Boundary of the first frozen candidate

Sections 3--5 remove three genuine issues: actual scalar histories can be
replaced at root width in the whole vector dynamics; the finite response
trace concentrates at root width; and a smooth reinsertion estimate can
be differentiated with respect to a bounded tagged forcing by a direct
augmented calculation. These results still do not identify the mean of
that trace with the own smooth population response.

To finish this route, one must supply the following complete argument,
with all items in one compatible norm and with the instantaneous term
(28) retained:

1. For the deterministic histories obtained in Section 3, use both tagged
   neuron deletions and (24), including the tagged-source-time envelopes,
   to prove that the finite expected covariance/response data satisfy the
   two-sided law (26)--(28) up to \(C/\sqrt n\). In particular, identify
   the average diagonal derivative of the **full** cavity graph with the
   response of the corresponding scalar equation, rather than assuming
   this from convergence of states.
2. Prove a mesh-independent comparison of the single-neuron expectations
   under varying Gaussian covariances and response measures. Bounded
   scalar derivatives alone are not this theorem. An inverse-free proof
   should bound the total variation of the actual path-functional second
   derivatives, including response observables, and check the Gaussian
   interpolation family. It must also provide a small-activity contraction
   for the resulting complete law map. A pointwise fixed-mesh covariance
   interpolation estimate is insufficient unless its derivative sums have
   a mesh-independent bound.
3. Identify that fixed point with the previously constructed own smooth
   population and restore deterministic scalar self-consistency. The
   coefficients \(\bar\theta_n\) are finite-width means, so the fixed point
   for them is still width dependent. A damped residual comparison can
   plausibly restore the true population coefficients if the preceding
   consistency estimate also controls the prediction velocity by an
   integrable \(C\rho/\sqrt n\) source. A uniform bound on prediction
   values alone does not supply that derivative estimate.

These are quantitative identification steps, not objections to the
root-width conjecture. No valid slower-rate counterexample for (1) has
been constructed here. The full all-initialization all-time second moment
also requires control outside (3); this report works on the stated good
event and makes no tail-to-all-time upgrade.

The continuation below addresses the paired deletion bookkeeping and the
velocity observable. It leaves the deterministic mean-map interpolation
and contraction proof to the separately assigned route. In particular, the
conditional reduction in Section 10 is explicit about that dependency.

## 8. Full versus deleted covariance and response data

Keep theta deterministic throughout this section. Choose fixed row/column
norm cutoffs and an operator cutoff. Work on their common event, whose
complement has probability at most C/n by the supplied Gaussian second
and fourth moment estimates and operator estimate. All comparisons below
use the same normalization 1/n, even when a neuron is deleted.

Deleting an upper row changes the ordinary vector state by at most C,
uniformly in time. To verify this without estimating a potentially large
forward preactivation at that row, compare the remaining upper coordinates
first. The deleted row's w and v coordinates are bounded by C through direct
integration. Their direct contribution to the lower carrier has ordinary
norm at most \(C\|\omega\|_2\). All forward differences at the remaining
upper coordinates are bounded by the ordinary state difference through W.
The exceptional upper activation and its gate derivatives are bounded,
so they contribute at most C on their one coordinate. Subtract the vector
equations, integrate their C rho Lipschitz coefficient, and apply Gronwall.
This proves the ordinary state bound.

For a lower-column deletion the direct forward discrepancy is
\(\gamma h_{aj}\), of norm at most \(\|\gamma\|_2\). The direct lower
carrier discrepancy can be large at coordinate j, but its *clipped gate*
discrepancy is at most 2M on that one coordinate. On all other coordinates
there is no direct transpose discrepancy. The same difference inequality
therefore proves the same ordinary state bound. These arguments use fixed
scalar coefficients; no residual coercivity is needed here.

Every covariance of bounded coordinate outputs consequently changes by
\(C/\sqrt n\): for two such output columns u,v,

\[
\left|\frac{u^\top v-(u^c)^\top v^c}{n}\right|
\le \frac{\|u-u^c\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
 +\frac{\|u^c\|_2}{\sqrt n}\frac{\|v-v^c\|_2}{\sqrt n}.
\tag{29}
\]

The tangent coefficient matrices also have a useful ordinary
Hilbert--Schmidt bound,

\[
\|L(t)-L^c(t)\|_F\le C\rho(t).                                 \tag{30}
\]

To check it, the removed matrix has rank one and Hilbert--Schmidt norm
bounded by the removed row/column norm. At an exceptional deleted
coordinate, every scalar gate derivative changes by a bounded amount,
so its diagonal-matrix Hilbert--Schmidt contribution is bounded. On all
other coordinates the global Lipschitz bound for the scalar derivative
turns the ordinary state/input differences into an ordinary
Hilbert--Schmidt bound. Telescoping each fixed-length product in the
Jacobian graph proves (30). Duhamel gives
\(\|\Phi(t,s)-\Phi^c(t,s)\|_F\le C\). Applying the same argument to
source and output derivative factors, and using the trace inequality in
Section 4, proves a \(C/\sqrt n\) difference between full and cavity
normalized response kernels. An isolated removed coordinate contributes
at most C/n directly to a normalized trace.

This reasoning applies to the upper response as well. For clarity, its
source matrix is explicit. Add an external vector e to z_b in the full
forced graph and factor r_b(s) out of its state source. At time s the
remaining coefficient has the blocks

\[
\begin{aligned}
S_b^A e&=-\frac2m
 [F_p(\alpha_b,P_b)\odot
       W_0^\top(F_z(z_b,w)\odot e)]u_b^\top,\\
S_b^w e&=-\frac2m\psi(z_b)\odot e,\\
S_b^{v_b} e&=-2F_z(z_b,w)\odot e,\qquad S_b^{k_a}e=0.
\end{aligned}                                                   \tag{31}
\]

All unspecified value blocks vanish. Thus the upper response has the
instantaneous matrix \(\delta_{ab}\operatorname{diag}F_z(z_a,w)\)
and the past matrix
\(r_b(s)D_Ud_a(t)\Phi(t,s)S_b(s)\). Its normalized trace has the exact
measure structure in (28). The matrix factors in (31) have bounded
operator norm; their normalized Hilbert--Schmidt changes are bounded by
C times normalized state/root changes. Gaussian Poincare therefore gives
fixed-(t,s) root-width fluctuations of both its atom and its past trace
density after the deterministic factor r_b(s) is removed. No assertion
that \(d=p\) is used in (31).

## 9. Tagged derivatives identify the two directions

The role of tagged forcing can now be stated without an independence
shortcut. Delete upper neuron i, keeping theta prescribed. The cavity
does not see an added external preactivation path u at that deleted
neuron. Its lower feature Hc, Gaussian covariance, Jacobian, and trace
kernels are therefore independent both of the removed row omega and of
u. Reinsert the row with its actual path \(\eta=d_i[u]\). Section 5 yields

\[
\omega^\top h_a[u](t)
=G^h_{n,a}(t)+\sum_b\int_0^t
 r_b(s)R^h_{n,ab}(t,s)d_{bi}[u](s)\,ds+\varepsilon_a[u](t),
\tag{32}
\]

where Gh is conditionally Gaussian with the actual cavity feature
covariance. The Lp temporal supremum of epsilon is at most C_p/root(n).
The derivative statement (24), applied with
\(\chi=D_ud_i[u]\), proves the corresponding root-width estimate for
the response of epsilon to a bounded tagged path. It does not condition
on the realized eta or chi. A bounded tagged path has bounded ordinary
state sensitivity by the variational equation with C rho coefficient,
and its current d_i sensitivity is bounded, since the removed-row norm is
bounded. Thus chi satisfies the required bound.

The scalar upper system using the right side of (32) without epsilon is
well defined for small activity. Indeed, for a prescribed candidate z,
integrate the w and v equations, then form d. Their path Lipschitz bounds
are \(\|\Delta w\|_\infty+\|\Delta d\|_\infty\le CS_*\|\Delta z\|_\infty\)
and \(\|\Delta v\|_\infty\le CS_*^2\|\Delta z\|_\infty\).
The response term in (32) has total source mass at most CS_* and the
finite-memory row term uses bounded K. Hence the z fixed-point map has
Lipschitz constant \(CS_*^2<1/2\). Subtracting the two fixed-point
equations absorbs this feedback and propagates both the state remainder
and its tagged derivative with a fixed constant. Differentiating the
scalar fixed-point equation gives its actual response, including its
instantaneous gate derivative. Thus the tagged upper derivative has
been compared to the response of the upper scalar equation, not merely
to a tangent of a Gaussian approximation at fixed feedback.

For the opposite direction delete lower column j and omit the isolated
lower coordinate from the remaining environment. Because K,V are
prescribed, that environment does not use either A0j or a tagged additive
lower-carrier path at j. Conditional on it, A0j is an independent Gaussian
root and the removed column is \(\gamma\sim N(0,I_n/n)\). Reinsert it
with its actual path \(\eta=h_j[u]\), which is bounded by one. Apply the
forward-forcing version of Section 5 with output d. Its algebraic direct
derivative must be included before centering the Gaussian quadratic
form. The result is

\[
\gamma^\top d_a[u](t)=G^d_{n,a}(t)
 +A^d_{n,a}(t)h_{aj}[u](t)
 +\sum_b\int_0^t r_b(s)R^d_{n,ab}(t,s)h_{bj}[u](s)\,ds
 +\widetilde\varepsilon_a[u](t),                              \tag{33}
\]

with the following precisely defined coefficients: Gd has conditional
covariance \(n^{-1}(d_a^c(t))^\top d_b^c(s)\),
\(A^d_{n,a}=n^{-1}\operatorname{tr}\operatorname{diag}F_z(z_a^c,w^c)\),
and the past density R is the normalized trace of the cavity matrix in
(31) propagated to d_a, with r_b removed. The state and tagged derivative
remainders have the same root-width bounds. The isolated lower scalar
equation substitutes (33) into P_j and integrates its A,k equations.
Its first-difference coefficient has time integral at most CS_*, while
the additional response feedback has bounded total mass CS_*.
Gronwall, or contraction of its integral equation for smaller S_*,
therefore propagates these bounds with constants independent of time.

One can recover the response *density at a specified source time* from
the same argument without dividing by a residual. Use a source atom at
s plus its bounded causal response tail. The variational equation is
interpreted with a jump source at s and its ordinary evolution afterwards;
equivalently approximate the atom by short pulses and retain their
weighted L1 source mass. In the proof of (21), replace the bounded chi
estimate by the absolute integral of its forcing against |r|, and include
the source atom explicitly in the finite graph. Gaussian projection
estimates and the product bound (23) apply at that atom exactly as at a
fixed time. The resulting bound for the regular tagged response is
\(C|r_b(s)|/\sqrt n\); its instantaneous atom is treated by the direct
algebraic gate calculation. Values of a regular density on t=s are
irrelevant to its integral, and the current-time atom is never counted
again as a past integral.

For each fixed source and target pair, the average of the n diagonal
tagged response matrices is its normalized trace by definition.
Exchangeability of the rows, or of the columns and first roots, equates
the expectation of that normalized trace to the expectation of one
tagged diagonal. Thus (32)--(33) identify expected finite response traces
with expected responses of the corresponding scalar systems at the
random cavity covariance/response data, with root-width error. Section 8
then replaces cavity means by full means, again at root width. This is
the required algebraic and probabilistic two-sided consistency step;
replacing the random cavity data by deterministic means still uses a
continuous Gaussian comparison, specified in Section 11.

## 10. A passive observable supplies prediction-velocity consistency

State convergence need not be differentiated in time. Append the actual
normalized lower-feature velocity as a passive output. For prescribed
theta and rho positive, set

\[
q_a=\dot h_a/\rho
=-\frac2m\sum_b\frac{r_b}{\rho}(u_a^\top u_b)
            \psi(\alpha_a)F(\alpha_b,P_b).                     \tag{34}
\]

At rho=0 define the unused q to be zero. The fixed coefficients r_b/rho
are bounded by sqrt(m); they are not differentiated. Since the original
F and all its scalar derivatives are bounded, q is bounded and has
bounded scalar derivatives of every fixed order, uniformly in time and
width. It has no feedback into the dynamics.

The passive forward field W0 q must use the same W0. In a row deletion,
expand q at the cavity just as one expands an algebraic gate output.
There are two linear terms: its derivative through the state tangent,
and its direct derivative through the added carrier omega eta at the
current time. The latter derivative is

\[
Q_{ac}(t)=
-\frac2m\frac{r_c(t)}{\rho(t)}(u_a^\top u_c)
       \psi(\alpha_a(t))F_p(\alpha_c(t),P_c(t)).                 \tag{35}
\]

It is coordinatewise and bounded. The same pure-tangent quadratic
calculation (22) bounds the ordinary output remainder by C/root(n) in
every fixed Lp. Multiplication by omega, followed by Holder, preserves
that scale. Center both quadratic linear terms. This gives, at every
fixed target time t,

\[
(W_0q_a)_i(t)=G^q_{n,a}(t)
 +\sum_c A^q_{n,ac}(t)d_{ci}(t)
 +\sum_b\int_0^t r_b(s)R^q_{n,ab}(t,s)d_{bi}(s)\,ds
 +\varepsilon^q_{n,a}(t),                                    \tag{36}
\]

where

\[
A^q_{n,ac}(t)=\frac1n\sum_j Q^c_{ac,j}(t),\qquad
R^q_{n,ab}(t,s)=\frac1n\operatorname{tr}
 [D_Uq_a(U^c(t))\Phi^c(t,s)J_b^c(s)].                          \tag{37}
\]

The state derivative in (37) holds the external carrier fixed; the direct
current derivative (35) has already been separated. The Gaussian
\(G^q_{n,a}(t)=\omega^\top q_a^c(t)\) is jointly Gaussian with the whole
history Gh used in (32), with exact conditional covariances

\[
\mathbb E_\omega G^h_{n,b}(s)G^q_{n,a}(t)
=\frac{h_b^c(s)^\top q_a^c(t)}n,\qquad
\mathbb E_\omega G^q_{n,a}(t)G^q_{n,b}(t)
=\frac{q_a^c(t)^\top q_b^c(t)}n.                              \tag{38}
\]

In particular every fixed Gaussian moment of Gq is uniformly bounded,
because q is coordinatewise bounded. Equations (36)--(38) retain the
instantaneous passive response atom, which can be nonzero. Dropping it
would lose the same-matrix feedback in the velocity.

Here are the needed quantitative facts for the passive coefficients.
The covariance functions in (38) are Lipschitz in Gaussian roots with
constant C/root(n): q is a bounded smooth output of the original finite
graph, and its normalized first-difference bound is C times the state/root
distance. Gaussian Poincare supplies fixed-(s,t) L2 root-width fluctuations.
For (37), both its source and its output derivative are finite sums of
products of bounded diagonal matrices and W0,W0 transpose. Differencing
such products gives exactly the normalized Hilbert--Schmidt estimate in
(15). Thus both its atom and its past trace density have the same
fixed-(t,s) L2 root-width fluctuations. Row/column deletion changes their
means by C/root(n) by Section 8. Their two-sided mean identification uses
the tagged lower forcing calculation in Section 9 with output q: bounded
third derivatives, the product estimate (23), and the explicit atom (35)
give the same root-width tagged error. No added dynamic state or new
fixed-point feedback is required.

For a training index a, write \(\beta_b=r_b/\rho\) and suppose the
prescribed K is absolutely continuous with bounded
\(J_{ba}=\dot K_{ba}/\rho\) on the set rho positive. The actual forced
prediction has the exact velocity

\[
\frac{\dot f_a}{\rho}
=\frac1n\sum_i\left\{
-\frac2m\sum_b\beta_b g_{bi}g_{ai}
+p_{ai}\left[(W_0q_a)_i
 +\frac1m\sum_b(-2\beta_b d_{bi}K_{ba}+v_{bi}J_{ba})\right]
\right\},\qquad p_{ai}=w_i\psi(z_{ai}).                       \tag{39}
\]

This follows by differentiating w and the *supplied-coefficient* forward
formula \(z_a=W_0h_a+m^{-1}\sum_bv_bK_{ba}\). The true output derivative
p in (39) is not smoothly clipped. All terms other than the Gaussian part
of (36) are bounded smooth functionals of the scalar upper paths and the
passive response data.

The Gaussian part is harmless but requires a moment argument. For fixed
law data it has the form

\[
\Phi(\gamma,G^q)=w[\gamma](t)\psi(z_a[\gamma](t))\,G^q_a(t).
\tag{40}
\]

Its second derivative in Gq is zero. Its mixed gamma/Gq derivative is
the first path derivative of \(w\psi(z_a)\); its second gamma derivative
is the corresponding second path derivative times Gq. Upper scalar
responses of each fixed order have a deterministic envelope of mass CS_*:
the readout integral contributes S_*, while the upper z feedback has
contraction constant CS_*^2. Consequently the expected absolute Hessian
measure in (40) is bounded by a deterministic envelope with finite mass,
uniformly over the joint covariance interpolation family. Indeed the only
extra random factor is \(|G^q_a(t)|\), whose expectation is at most
\(\sqrt{\operatorname{Var}G^q_a(t)}\le C\). No independence between Gq
and gamma is used. Convex interpolation of the **joint** covariance in
(38) keeps that variance bound. Replacing covariance blocks separately
without preserving positive semidefiniteness would not be justified.

Finite-mesh covariance interpolation therefore gives a root-width mean
comparison for (40) whenever the summed derivative-measure envelopes
are mesh independent. The same derivative-measure lemma needed for the
core law suffices here; uniform second moments justify passage from the
finite meshes to this linearly growing observable. In the row approximation
itself, a root-width error of p times Gq has first moment at most
\(\|\Delta p\|_{L^2}\|G^q\|_{L^2}\le C/\sqrt n\), and the field error
in (36) is multiplied by bounded p. Thus the unbounded Gaussian factor
does not change the rate.

It follows, conditional on the deterministic continuous-law comparison
specified next, that the mean prediction-velocity discrepancy is

\[
|\mathbb E\dot f_{n,a}^{\theta}(t)
       -\dot f_{\infty,a}^{\theta}(t)|
\le C\rho(t)/\sqrt n.                                         \tag{41}
\]

The assertion is for the prescribed-coefficient system. The cutoff and
moment argument in Section 12 removes its operator exceptional set;
the passive velocity itself is not asserted to be bounded there.
It extends uniformly to bounded passive query sets by adjoining their K
and J coefficients. It is a velocity-source estimate; it is stronger in
the needed direction than differentiating a uniform value bound.

For the coefficients frozen at actual conditional means in Section 3,
the needed J bound holds: differentiating K gives
\(\dot K_{ba}=\rho\langle h_b-k_b,h_a\rangle_n/\tau
+\langle k_b,\dot h_a\rangle_n\), so
\(|\dot K_{ba}|\le C\rho\), and hence
\(|\dot{\bar K}_{ba}|\le C\bar\rho\). Its first-difference bound is
\(C\rho\varepsilon_0+C\|\Delta r\|_m\), by bounded local gates in
dot h. Thus its pointwise centered L2 error is at most
\(Ca(t)/\sqrt n\) by (6) and Gaussian Poincare. Applying the same
first-difference calculation directly to (39), along with (9)--(11),
therefore compares the actual conditional mean velocity and the velocity
at frozen histories with an integrable root-width error. No derivative
of the error in (9), and no derivative of r/rho, is invoked.

## 11. Precise dependence on the deterministic mean-map lemma

The local probability estimates above produce actual root-width sources.
The remaining deterministic input has a specific form. On the admissible
bounded covariance/response family of (26)--(28), one needs a causal
single-neuron mean-map comparison whose Gaussian derivatives through
order three are finite signed measures on their source times, dominated
by deterministic finite-activity measures independently of time mesh.
The domination must also cover the atom/past decomposition of response
outputs, and the passive q outputs just added. The estimate then follows
by applying finite-dimensional Gaussian covariance interpolation at a
mesh, summing against these dominating measures, and taking the mesh
limit. A mere bound on the operator norm of a multilinear derivative on
continuous paths does not automatically imply such a measure
representation; it must come from differentiating the actual causal
integral equations.

With that lemma, (18), (29)--(38), and Tonelli give the mean consistency
relation for the complete two-sided map: every conditional covariance
or response coefficient differs in mean from its deterministic mean by
C/root(n) pointwise in its source times; the deterministic dominating
measures let those errors be integrated without an expectation of a
temporal supremum. The tagged calculations prove response consistency,
and the bounded outputs prove covariance consistency. The same argument
with (39)--(40) proves (41). Contractivity of that deterministic map at
small fixed activity then identifies the forced population law at root
width. Scalar self-consistency still uses the damped actual-versus-forced
comparison, with (41) supplying its integrable source.

Thus the first frozen candidate's two probabilistic bookkeeping gaps are
addressed by explicit paired deletions and a passive velocity observable.
This report does **not** mark the full theorem proved in advance of the
separately assigned deterministic measure-envelope and contraction lemma,
its compatibility with the constructed population, and the final damped
scalar restoration. The all-initialization all-time second moment remains
a separate tail question; a conditional root-width theorem would already
give the original fixed-confidence population rate on the high-probability
fitting event.

## 12. Full Gaussian forced laws and exceptional sets

All prescribed-coefficient systems in Sections 8--11 can be run on the
unconditioned Gaussian initialization law. The deterministic theta may
have been obtained from the conditional means of the *original* dynamics;
once prescribed, it is independent of every Gaussian root in the forced
comparison. There is no conditional-Gaussian assertion about the original
good-event law.

Here is explicit moment control for removing forced-system cutoffs. Put
\(K_W=\|W_0\|_{\rm op}\). Direct integration, without a cutoff, bounds
h,d,w,v,k,q coordinatewise by constants depending on M,S_*,data. The
normalized forward and backward carriers have bounds polynomial in K_W.
The first state Jacobian obeys

\[
\|L(t)\|_{\rm op}\le C\rho(t)(1+K_W^2).                       \tag{42}
\]

There are at most two initialized matrix factors in one derivative of
the lower vector field: the forward W_0 and the transpose W_0. Every
intervening diagonal gate derivative is bounded, by Section 2. Other
state equations have no more such factors. Therefore (42), including its
quadratic dependence on K_W, follows by listing these graph paths.
Duhamel then gives \(\|\Phi(t,s)\|_{\rm op}
\le\exp(CS_*(1+K_W^2))\). Every fixed-order variation and local-remainder
constant needed above is bounded by

\[
C_p(1+K_W)^{b_p}\exp(C_pS_*(1+K_W^2)).                         \tag{43}
\]

The exponents b_p are fixed. To see that no double exponential is hidden
here, first tangents use (42). A second or tagged tangent solves another
linear equation with the *same* homogeneous bound (42); its source is a
fixed finite sum of products of already bounded tangents and graph
derivatives. Those derivatives contribute only powers of K_W. Multiplying
finitely many single exponentials and applying Duhamel gives another
bound of the form (43). No Gronwall coefficient is replaced by the size
of a tangent or a remainder. This argument applies to all the finitely
many Lp estimates actually used, including the L4 and L8 estimates in
Section 5 and the response-trace sensitivities.

The required Gaussian operator tail has a short elementary proof. A
one-quarter net of the Euclidean unit sphere has at most \(9^n\) elements,
by packing disjoint radius-one-eighth balls inside a ball of radius
nine-eighths and comparing volumes. Approximating both arguments of a
bilinear form shows
\(\|W_0\|_{\rm op}\le2\max_{u,v\text{ in the net}}|v^\top W_0u|\).
Each displayed scalar is Gaussian with variance 1/n, so a union bound
gives

\[
\Pr(K_W>L)\le2\,9^{2n}\exp(-nL^2/8).
\tag{44}
\]

For a sufficiently large fixed L0 this is at most
\(2\exp(-nL^2/16)\) for all L at least L0. Integration of this tail shows
that, for every fixed a,b, and all sufficiently large n,

\[
\mathbb E(1+K_W)^b e^{aK_W^2}\le C_{a,b},\qquad
\mathbb E[(1+K_W)^b e^{aK_W^2}\mathbf1_{\{K_W>L_0\}}]
\le C_{a,b}e^{-c n}.                                         \tag{45}
\]

Choose n large enough that the negative quadratic exponent in (44)
dominates a. The integral formula for an increasing weight, or a direct
integration by parts, then proves both bounds. The identical argument
works for a matrix with one row or column zeroed, since its operator
norm is no larger. Removed-row or removed-column norms also have
exponential tails: the identity
\(\mathbb E e^{\frac n4\|\omega\|_2^2}=2^{n/2}\) and Markov's inequality
give this immediately at a sufficiently large fixed norm cutoff.

Consequently all quantities in (43) have uniform fixed moments. For
covariance and response concentration one may now apply Gaussian
Poincare directly, instead of extending from a cutoff. Their local root
gradient norm is at most \(C(K_W)/\sqrt n\), where C(K_W) has the form
(43). Indeed the deterministic first-difference/HS proof in Section 4
applies locally with that constant. Approximate by smooth root cutoffs
and pass in the square-integrable weak gradient; (45) makes both the
function and gradient cutoff errors vanish. This proves full-Gaussian
fixed-time variance bounds C/n. The time derivative version in (17)
has the extra deterministic factor rho, so its integration has the same
uniform moment bound when an all-time assertion is needed.

In a row or column reduction, apply the small-activity scalar contraction
only on the cavity-measurable event \(\|W_0^c\|_{\rm op}\le L_0\), with
the removed-vector norm bounded as required. Constants are then fixed
before choosing the small-label condition. This event does not condition
the removed vector. Outside it, define the auxiliary law data to be one
fixed admissible covariance/response tuple; do not assert the scalar
contraction for an arbitrarily large random trace. Equations (43)--(45)
bound the change in the finite means caused by this replacement by
\(Ce^{-cn}\). On the good cavity event the exact conditional Gaussian
relations (32)--(38) apply. The removed-vector norm exceptional set has
the same negligible contribution by its Gaussian moments. Thus this
localization preserves the C/root(n) mean consistency with the full
unconditioned Gaussian forced law.

The velocity requires a separate bound because W_0q is not coordinatewise
bounded. Formula (39), Cauchy--Schwarz in the normalized pairing, and the
coordinate bounds give the deterministic bound for the averaged velocity

\[
|\dot f_a^\theta(t)|\le C\rho(t)(1+K_W).                      \tag{46}
\]

For instance
\(|\langle p_a,W_0q_a\rangle_n|
\le\|p_a\|_n K_W\|q_a\|_n\le CS_*K_W\).
Equations (45)--(46) show that its operator exceptional contribution is
at most \(C\rho(t)e^{-cn}\). A tagged row has the cruder bound
\(C\rho(t)(1+\sqrt n K_W)\); this polynomial width factor is also
absorbed by the exponential tail. Alternatively, exchangeability on the
operator event makes its *signed* expected contribution equal to that
of the averaged velocity in (46). The auxiliary Gaussian observable
(40) has a uniform second moment, so Cauchy--Schwarz also controls its
exceptional contributions. Hence (41) holds for the unconditioned forced
law, with constants uniform in time.

Finally compare a forced expectation conditioned on the original event
\(\mathcal G_n\) with its full-Gaussian forced expectation. For bounded
state outputs the discrepancy is at most \(C\Pr(\mathcal G_n^c)=C/n\).
For velocity, split at \(K_W\le L_0\); (46) gives
\(C\rho(t)\Pr(\mathcal G_n^c)\) on that set, and (45) gives an
exponential contribution on its complement. Thus the discrepancy is
\(C\rho(t)/n\). Trace observables are treated by (43) in the same way.
This is the required bridge between the good-event means used to choose
theta and the independent full Gaussian law used in its forced cavity
analysis. It makes no assertion about the original all-time trajectory
on \(\mathcal G_n^c\).

Presentation-only checked-version patch: after the first frozen local
candidate, missing backslashes in several `qquad` separators were restored
and s(t) was explicitly defined at (19). The mathematical local estimates
were not changed by that patch. Sections 8--12 are a substantive extension,
to be checked together with the separate mean-map argument before a full
population theorem is claimed.
