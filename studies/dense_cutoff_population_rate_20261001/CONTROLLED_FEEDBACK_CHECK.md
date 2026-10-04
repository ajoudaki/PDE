# Reconstruction of the feedback and passive-query arguments

This is a scoped internal reconstruction of the complete candidates
CONTROLLED_FEEDBACK_STABILITY.md and PASSIVE_QUERY_FLUCTUATIONS.md,
performed on 2026-10-01. The scope is two tanh hidden layers,
orthonormal fixed training inputs, and a bounded query domain. No experiment,
other-study input, manuscript edit, or Git write was used. The author of this
check also authored the same-study local edge-response criterion, and the
coordinator supplied the present candidates. This is collaborative checking,
not an isolated promotion review.

**Outcome: both main results reconstruct within their stated scope.**
The deterministic remainder estimate is genuinely Lipschitz with coefficient
\(CS^2\). The passive-query argument gives \(CS^2/n\) fluctuations around the
finite-width mean, with the activity supremum inside the input integral.
Combining them reduces the adaptive all-time comparison in this structured
setting to the bias for one deterministic population driver.
The local edge-response contrast controlling that bias remains an assumption.

The first version's final feedback paragraph mentioned only training
convergence when identifying the controlled limit. The coordinator repaired
this during checking: the final version explicitly also invokes the
manuscript's actual passive-query convergence. The hashes below identify
that corrected version. No unresolved substantive gap was found in these
two candidates.

## 1. Controlled vector fields and the two powers of activity

For this check only, abbreviate \(\|v\|_2/\sqrt n\) by
\(\|v\|_{\mathrm{rms}}\); matrix norms remain ordinary Frobenius norms.
The transformed state norm is
\[
\|dX\|=\sum_a\|dp_a\|_{\mathrm{rms}}+\|dw\|_{\mathrm{rms}}+\|dW\|_F.
\]
The controlled equations and fields are
\[
dp_a=k_a\,db_a,\quad
dw=\sum_a g_a\,db_a,\quad
dW=\frac1n\sum_a\delta_a h_a^\top\,db_a,
\]
where \(h_a=\psi(p_a)\), \(g_a=\tanh(Wh_a)\),
\(\delta_a=w\odot(1-g_a^2)\), and \(k_a=W^\top\delta_a\).
Every driver has total variation at most \(S\le1\).

From bounded tanh features,
\(\|w\|_\infty\le S\), \(\|\delta_a\|_{\mathrm{rms}}\le S\), and the
Frobenius norm of \(\delta_a h_a^\top/n\) is at most \(S\).
Thus \(\|W-W_0\|_F\le S^2\). If \(\|W_0\|_{\mathrm{op}}\le K\),
then \(\|k_a\|_{\mathrm{rms}}\le(K+1)S\).
The total variations of the hidden coordinates and \(W\) are \(O(S^2)\);
the readout variation is \(O(S)\).

The relevant state subtraction estimates are
\[
\begin{aligned}
\|\Delta h_a\|_{\mathrm{rms}}
 &\le\|\Delta p_a\|_{\mathrm{rms}},\\
\|\Delta g_a\|_{\mathrm{rms}}
 &\le C(\|\Delta W\|_F+\|\Delta p_a\|_{\mathrm{rms}}),\\
\|\Delta\delta_a\|_{\mathrm{rms}}
 &\le\|\Delta w\|_{\mathrm{rms}}+2S\|\Delta g_a\|_{\mathrm{rms}},\\
\|\Delta k_a\|_{\mathrm{rms}}
 &\le C\|\Delta\delta_a\|_{\mathrm{rms}}+S\|\Delta W\|_F.
\end{aligned}
\tag{1}
\]
The normalized rank-one product bound handles the matrix vector field.
Hence all control vector fields \(V_a(X)\) are uniformly Lipschitz on the
tube, independently of the initial transformed-coordinate values.
Their full norms are \(O(1)\); their hidden components have norm \(O(S)\)
and total variation \(O(S)\), since the full state has variation \(O(S)\).
No coordinatewise carrier maximum is used.

For two controls on a common physical-time interval, let
\(\epsilon_T=\max_a\sup_{t\le T}|b_a(t)-c_a(t)|\). Subtract their equations:
\[
X^b-X^c=\sum_a\int[V_a(X^b)-V_a(X^c)]\,db_a
       +\sum_a\int V_a(X^c)\,d(b_a-c_a).
\]
Integration by parts bounds the last term by \(\epsilon_T\) times the
field's endpoint norm plus its total variation. Gronwall against the
finite measure \(\sum_a|db_a|\) then gives the full-state bound
\(\sup_t\|X^b-X^c\|\le C\epsilon_T\), with factor \(e^{CS}\), not \(e^{CT}\).

Apply the same identity only to hidden components. The first integral
is \(CS\epsilon_T\) by the full-state bound; the endpoint and variation
terms are also \(CS\epsilon_T\). Therefore
\[
\sup_{t\le T}\left[
\sum_a\|p_a^b-p_a^c\|_{\mathrm{rms}}+\|W^b-W^c\|_F
\right]\le CS\epsilon_T.
\tag{2}
\]
An absolute hidden displacement \(O(S^2)\) alone would not establish (2).

For a query \(v=x/\sqrt d\), put \(c_a=v_a^\top v\) and
\(v_\perp=v-\sum_ac_av_a\). Orthogonality gives exactly
\[
z_x^{(1),b}=A_0v_\perp+\sum_a c_aF^{-1}(p_a^b).
\tag{3}
\]
The derivative of \(F^{-1}\) is \(\operatorname{sech}^2(F^{-1})\le1\),
and \(\sum_a|c_a|\le\sqrt m B\) on the query ball. Equation (2) yields
\[
\sup_t\|g_x^b-g_x^c\|_{\mathrm{rms}}\le C_BS\epsilon_T.
\tag{4}
\]
The displacement and total variation of each query feature are \(O_B(S^2)\).

The readout remainder
\[
e_w^b(t)=\sum_a\int_0^t[g_a^b(s)-g_a(0)]\,db_a(s)
\]
has RMS \(O(S^3)\). Its difference is \(CS^2\epsilon_T\):
the feature difference against \(db\) uses (4) and variation \(S\);
the integral against \(d(b-c)\) is integrated by parts and uses the
feature displacement and variation \(O(S^2)\).
The exact prediction remainder is
\[
R^b(t,x)=\frac{e_w^b(t)^\top g_x(0)}n+
         \frac{w^b(t)^\top[g_x^b(t)-g_x(0)]}n.
\]
Its two-product subtraction has scales
\(S^2\epsilon_T\), \(\epsilon_TS^2\), and \(S(S\epsilon_T)\).
Consequently
\[
\sup_t|R^b(t,x)-R^c(t,x)|\le C_BS^2\epsilon_T.
\tag{5}
\]
This checks the claimed Lipschitz estimate rather than merely adding two
absolute \(O(S^3)\) remainder bounds.

## 2. Feedback damping and the time parametrization

Suppose \(Q_0/m\succeq\lambda I\), and the actual and reference controls
both have variation at most \(S\). With
\(\eta_n=f_n^{b_*}-f_*\) and \(e=b_n-b_*\), the driver equations give exactly
\[
\dot e=-\frac2mQ_0e
-\frac2m[R^{b_n}(X)-R^{b_*}(X)+\eta_n(X)],\qquad e(0)=0.
\tag{6}
\]
The semigroup is bounded by \(e^{-2\lambda t}\), with integral
\(1/(2\lambda)\). Variation of constants and (5) therefore bound the
finite-horizon supremum of \(\|e\|_2\) by \(CS^2\) times itself plus
\(C\max_a\sup_t|\eta_n(t,x_a)|\). Choose \(S\) so the first coefficient
is below one, absorb, and let the horizon increase.
The exact prediction decomposition and \(|Q_0(x,a)|\le1\) give the claimed
whole-query comparison. Constants do not depend on physical duration.

This argument is pathwise for each actual random driver. It never inserts
that driver into a deterministic-control concentration statement.
For the stochastic comparison, use only the deterministic reference driver.
Its clock
\[
\sigma(t)=\sum_a\int_0^t|b'_{*,a}(r)|\,dr\le S
\]
gives a 1-Lipschitz path \(\widetilde b_*\) with
\(b_*(t)=\widetilde b_*(\sigma(t))\); extend it constantly to \([0,S]\).
Where the clock is constant, so are the driver and controlled state.
The autonomous controlled equations are invariant under this reparametrization,
so the activity supremum includes all physical times. The clock is
deterministic, and expectation commutes with evaluation at \(\sigma(t)\).
There is no random inverse-clock comparison.

## 3. Passive-query cavity moments

For each fixed query, its first-layer coordinates have the exact law
\[
z_x^{(1)}=\nu\zeta_0+\sum_a c_aF^{-1}(p_a),\qquad
p_a(0)=F(Z_{0,a}),\quad \nu=\|v_\perp\|,
\tag{7}
\]
where the \(m+1\) Gaussian root columns are independent and standard.
This follows from orthonormality of the training directions and their
orthogonal query direction. An unused root is harmless if \(\nu=0\).

Fix all roots deterministically. Delete first-layer neuron \(i\), retaining
normalization \(n\), and condition on the other initialized hidden columns.
The remaining column is independent Gaussian with covariance \(I/n\).
Its trained correction has norm at most \(S^2/\sqrt n\). Write
\(q_i=\|W_{0,i}\|_2+S^2/\sqrt n\).
The missing forward contribution has norm at most \(q_i\).
State subtraction and Gronwall give retained-state difference
\(CSq_i/\sqrt n\) in the normalized state norm. Formula (7) is
\(C_B\)-Lipschitz in the retained transformed coordinates. Thus the query
top-feature difference is \(C_Bq_i\) in Euclidean norm, and
\[
\|\delta_x-\delta_x^{-i}\|_2\le C_BSq_i.
\tag{8}
\]

On \(E_n=\{\|W_0\|_{\mathrm{op}}\le K\}\), this yields
\[
k_{x,i}=W_{0,i}^\top\delta_x^{-i}+R_{x,i},\qquad |R_{x,i}|\le C_BS.
\tag{9}
\]
The response difference contributes at most
\(\|W_{0,i}\|\|\delta_x-\delta_x^{-i}\|\);
the trained-column correction contributes at most
\((S^2/\sqrt n)(S\sqrt n)=S^3\).

The cavity query response has norm at most \(S\sqrt n\).
Its RMS Lipschitz constant in the uniform control metric is \(C_B\),
by the state subtraction and (7). Conditional on the cavity, the first
term of (9) is therefore a centered Gaussian process with variance at most
\(S^2\) and increment standard deviation at most \(C_B\|b-c\|_\infty\).

The needed supremum estimate is uniform over fixed roots. The class of
\(m\)-dimensional 1-Lipschitz controls on \([0,S]\), starting at zero,
has uniform-metric nets satisfying
\[
\log N(\epsilon)\le C_m(1+S/\epsilon)\log(2+S/\epsilon).
\]
Time discretization followed by value quantization proves this estimate.
At scales \(\epsilon_j=S2^{-j}\), Gaussian maxima of the net increments
cost at most \(C_BS2^{-j/2}\sqrt{j+1}\), a summable series.
Adding a Gaussian tail parameter in the same union bound gives a
square-exponential supremum tail with scale \(S\).
Stopped controls, extended constantly, include every evaluation time.

The operator event does not invalidate the Gaussian conditioning.
Condition on the other columns first. If their norm exceeds \(K\), the
event \(E_n\) is empty. Otherwise apply the Gaussian estimate to the
independent missing column without conditioning it on \(E_n\), and restrict
the resulting event afterward. No truncated column is declared independent
of its truncation event.

For the projected system, \(E_n\) leaves the original matrix unchanged.
Off \(E_n\), \(|k_{x,i}^{\Pi}|\le CS\sqrt n\), and
\(\Pr(E_n^c)\le Ce^{-cn}\). These facts prove
\[
\mathbb E_G\sup_{u\le S}\frac1n\sum_i|k_{x,i}^{\Pi}(u)|^4\le C_BS^4.
\tag{10}
\]
The same argument for training carriers bounds every fixed linear-exponential
moment of \(U_{a,i}=p_{a,i}-p_{a,i}(0)\), because
\(\sup|U_{a,i}|\le S\sup|k_{a,i}|\).
Off \(E_n\), its exponential cost \(e^{C_p\sqrt n}\) is absorbed by
\(e^{-cn}\). All constants are uniform over deterministic roots; no Gaussian
calculation is applied directly to the projected matrix off \(E_n\).

## 4. Gaussian derivatives, dependent products, and the activity supremum

The exact query tangent pairing is
\[
\Lambda_{xa}
=\frac{g_x^\top g_a}{n}
 +\frac{\delta_x^\top\delta_a}{n}\frac{h_x^\top h_a}{n}
 +c_a\frac{(s_x\odot k_x)^\top(s_a\odot k_a)}n,\qquad
s_x=1-h_x^2,\quad s_a=1-h_a^2.
\tag{11}
\]
In particular \(dz_x^{(1)}=c_as_a\odot k_a\,db_a\), which supplies every
factor in the last term once. The other terms come respectively from the
readout and hidden-matrix updates. Hence
\(df_x/du=\sum_ab'_a\Lambda_{xa}\).

For fixed roots, an initialized hidden-matrix perturbation has controlled
state response \(D_X\le C\|\Delta W_0\|_F\); (7) gives the query response
bound \(C_BD_X\). A gate-response term in (11) is bounded by
\[
C_BD_X\left(\frac1n\sum_i k_{x,i}^2k_{a,i}^2\right)^{1/2}
\le C_BD_X
\left(\frac1n\sum_i k_{x,i}^4\right)^{1/4}
\left(\frac1n\sum_i k_{a,i}^4\right)^{1/4}.
\]
Carrier-response terms use only deterministic RMS bounds.
Since \(G\mapsto\Pi_K(G/\sqrt n)\) is \(n^{-1/2}\)-Lipschitz, squaring
and applying the arithmetic-geometric mean inequality gives
\[
\|\nabla_G\Lambda_{xa}^{\Pi}\|_F^2
\le\frac{C_B}{n}\left(1+
\frac1n\sum_i|k_{x,i}^{\Pi}|^4+\frac1n\sum_i|k_{a,i}^{\Pi}|^4\right).
\tag{12}
\]
The locally Lipschitz composition has weak derivatives even where the
projection is not classically differentiable. Their Gaussian square
integrability follows from (10), so the Gaussian variance inequality applies.

For root variation, define \(J_z(a,U)=F^{-1}(F(a)+U)\). The logarithmic
derivative of \((F^{-1})'\) has absolute value at most two, hence
\[
|\partial_aJ_z(a,U)|\le e^{2|U|},\qquad
|\partial_UJ_z(a,U)|\le1.
\tag{13}
\]
The analogous feature derivative is likewise exponentially bounded in
\(|U|\). Fix two first-root arrays before taking the \(G\)-expectation.
Their forcing is a sum of terms
\[
\left(\frac1n\sum_i
 e^{C\sup_u|U_{a,i}(u)|}|\Delta Z_{0,a,i}|^2\right)^{1/2}.
\tag{14}
\]
The root differences are deterministic. Minkowski in \(L^{p/2}(G)\) and
the uniform exponential moments bound (14) in \(L^p(G)\) by
\(C_p\|\Delta Z_{0,a}\|_2/\sqrt n\). State subtraction and Gronwall propagate
this forcing. Equations (7), (13), and bounded matrices/readout then bound
all query feature and carrier RMS differences in \(L^p(G)\) by
\[
\frac{C_{B,p}}{\sqrt n}
(\|\Delta Z_0\|_F+\|\Delta\zeta_0\|_2).
\tag{15}
\]

In subtracting (11), place the gate difference next to two carriers from
the same state; other terms contain a carrier difference.
The expectation of the gate term is at most
\[
C\left\|\|\Delta h_x\|_{\mathrm{rms}}+
         \|\Delta h_a\|_{\mathrm{rms}}\right\|_{L^2(G)}
\left(\mathbb E_G\frac1n\sum_i k_{x,i}^2k_{a,i}^2\right)^{1/2}.
\tag{16}
\]
The first factor uses (15); the second is \(O_B(S^2)\) by (10) and
Cauchy--Schwarz on the joint index/probability space. This handles their
dependence without factoring correlated expectations or treating a random
multiplier as deterministic.

Thus the matrix-averaged map is \(C_B/\sqrt n\)-Lipschitz in the ordinary
Euclidean first-root norm. Gaussian variance on the independent roots,
followed by total variance and (12), gives
\(\operatorname{Var}(\Lambda_{xa}^{\Pi})\le C_B/n\).
Its deterministic bound also justifies differentiating the centered prediction
under expectation. Cauchy--Schwarz in activity gives
\[
\mathbb E\sup_{u\le S}|f_n^{\Pi,b}(u,x)-\mathbb Ef_n^{\Pi,b}(u,x)|^2
\le S\int_0^S\operatorname{Var}\!\left(\sum_ab'_a(u)\Lambda_{xa}^{\Pi}\right)du
\le C_BS^2/n.
\tag{17}
\]
The last bound uses
\(\operatorname{Var}(\sum_a\beta_aX_a)
\le(\sum_a|\beta_a|\sqrt{\operatorname{Var}(X_a)})^2\),
not independence of tangent entries.

Both predictions have absolute value at most \(S\) and coincide on \(E_n\).
Removing projection therefore costs only \(O(S^2e^{-cn})\) in squared
supremum error, including centering. Continuous dependence on input and
activity gives the required joint measurability; a countable dense time
set computes the supremum. Tonelli proves the whole-query integral.
One need not couple the auxiliary root representations for different queries:
the bound is for each query on the original initialization law before
integration, not a stochastic supremum over queries.

## 5. Qualitative identification and exact remaining scope

Compact-time convergence of actual training predictions and uniform
exponential residual tails identify
\(\sup_t\|b_n(t)-b_\infty(t)\|\to0\) in probability: integrate up to a fixed
time, bound both tails by \(Ce^{-\kappa T}\), and then increase \(T\).
The deterministic controlled comparison makes the actual and reference-driven
finite predictions approach each other on the bounded query domain.

Identification with \(f_\infty\) at unseen inputs separately uses actual
passive-query convergence from the authorized manuscript. Its compact-time
version extends to all time using the exponentially small remaining parameter
variation and the forward prediction's uniform state Lipschitz bound on the
bounded query ball. Prediction boundedness on the fitting tube permits
Tonelli and Markov to pass from each fixed query to the integrated metric.
The fitting-event complements vanish in probability. The prescribed-control
predictions are bounded even outside the fitting event, so their mean is
identified as well. The corrected candidate now states both necessary
qualitative inputs explicitly.

The checked implications are:

1. Prescribed-control fluctuations about the finite mean have strict
   root-width scale over all activity and any fixed bounded query law.
2. Damped deterministic feedback stability transfers a population-centered
   estimate for the single population driver to actual autonomous training.
3. The local edge-response contrast remains the unproved quantitative bias
   assumption. The two checked results do not prove an unconditional rate.

The small-label threshold decreases only by a fixed amount to ensure the
\(CS^2\) absorption. Constants are independent of width and physical time.
For fixed confidence, fitting-event failures can be absorbed by sufficiently
large width; this step requires no numerical rate for those probabilities.

The proofs do not extend their scope to nonorthogonal data, arbitrary depth,
or query laws with unbounded support and only a finite second input moment.

## Frozen inputs

The canonical-notation and rigorous-math skills, including neural conventions,
were applied. Both candidates were read completely. The earlier authorized
POPULATION_CAVITY_ATTEMPT.md provides the projection and Gaussian variance
conventions; the controlled and cavity steps were explicitly reconstructed
above. No new study source was fetched through links. The qualitative
manuscript inputs were already within the authorized reading scope.

SHA-256:

    6a5b99cbaf1b7a905eb5666e77211e6e8ce705246d3146968c4b281a46568abb  CONTROLLED_FEEDBACK_STABILITY.md
    1ddda713770011e7be4eb589917aae2b4ee53fb1032d1c1bc7901903cd230e9c  PASSIVE_QUERY_FLUCTUATIONS.md
    c95075a84a47529d78873f9a6c342b950e640d51145a28577179de286d1f9e3b  POPULATION_CAVITY_ATTEMPT.md

Validation was algebraic and probabilistic reconstruction, including cavity
conditioning, dependent gate products, activity reparametrization, and exact
powers of \(S\). No numerical experiment or proof assistant was used.

## 6. Final assembly check of the conditional root-width theorem

The coordinator subsequently authorized the complete
ROOT_WIDTH_CONDITIONAL_THEOREM.md for reconstruction. It was read completely.
The following check applies to the final corrected version with SHA-256

    37a89edb3beb904bce3292193db3ae68f2bf07fcaafcfd165d60d09ce1276dda  ROOT_WIDTH_CONDITIONAL_THEOREM.md

Two minor issues in its first draft were reported and corrected before this
hash was taken: the residual-control integral's differential was repaired,
and the all-query-ball version of H is correctly described as a stronger
sufficient form, rather than equivalent to a bound only at training queries
and almost everywhere for the fixed test law.

**Assembly outcome: the conditional theorem reconstructs as stated.**
Its one unproved response estimate is H, including its specified
expectation/endpoint regularity. The independent qualitative population
identification comes from the manuscript; its numerical rate is not assumed.
The theorem's restriction to two tanh layers, orthonormal fixed training
inputs, bounded query support, and sufficiently small fixed labels is
maintained throughout.

### Mean bias and fluctuation combine against the correct target

At \(N=2n\), the profile has \(N^2/2\) edges of each type, with profile
derivatives \(-2,+2\). The Gaussian covariance term for one edge is
\((2N)^{-1}\partial_{W_{0,e}}^2q_N\), while the mobility derivative holds
the initialized entry fixed. The normalized \(N^2\) response in H therefore
gives exactly
\[
\partial_s\mathbb E q_N
=\mathcal R_{N,\mathrm{out}}-\mathcal R_{N,\mathrm{in}}.
\tag{18}
\]
At the block endpoint the two width-\(n\) networks are independent because
the driver is the same deterministic population driver; each has canonical
variance \(1/n\) and update coefficient \(1/n\). Their averaged prediction
has mean \(\mathbb E f_n^{b_*}\). The other endpoint is the canonical
width-\(2n\) network. Thus integration of H over profile and activity gives
the correct mean increment
\[
\sup_{u\le S}|\mathbb Ef_{2n}^{b_*}(u,x)-\mathbb Ef_n^{b_*}(u,x)|
\le C_BS/\sqrt n.
\tag{19}
\]
No coupling across successive widths is needed for a telescope of means.
The dyadic sum is finite, with constant \((1-2^{-1/2})^{-1}\).
H is required at each training query as well as for the fixed test law,
so the mean estimate covers both parts of the eventual feedback source.

The limit of the means is identified using the qualitative argument in
Section 5 of this check. Only values reached by the deterministic population
activity clock are needed for the physical-time theorem; the constant
extension after its terminal activity value causes no additional demand.
Prediction boundedness gives uniform integrability. Thus the reference in
the mean estimate is \(f_\infty(t,x)\), not an unrelated width-subsequence
limit or a finite-width mean.

The fluctuation bound and the deterministic mean estimate yield
\[
\mathbb E\int\sup_t|\eta_n(t,x)|^2\,d\mu(x)
+\sum_a\mathbb E\sup_t|\eta_n(t,x_a)|^2\le C/n,
\quad \eta_n=f_n^{b_*}-f_\infty,
\tag{20}
\]
by the triangle inequality and \((a+b)^2\le2a^2+2b^2\).
The supremum remains inside the input integral. The number of training
queries is fixed, so summing their estimates only changes the constant.
There is no hidden time net, cutoff factor, or logarithmic width loss.

### Same physical time and probability accounting

On the initialized fitting/operator event \(G_n\), the actual and population
drivers have total variation at most the same deterministic \(S\).
The finite initial Gram has the fixed lower bound required by (6).
All comparison constants are deterministic and uniform on this event.
The small-label threshold can be decreased independently of \(n\) so that
the \(CS^2\) nonlinear feedback term is absorbed.

The pathwise feedback comparison is at the same physical time and gives
\[
\mathcal E_\mu(f_n,f_\infty)
\le C_B\max_a\sup_t|\eta_n(t,x_a)|
  +\left(\int\sup_t|\eta_n(t,x)|^2\,d\mu(x)\right)^{1/2}
\quad\text{on }G_n.
\]
Squaring and using (20) proves
\[
\mathbb E[\mathbf1_{G_n}\mathcal E_\mu(f_n,f_\infty)^2]\le C/n.
\tag{21}
\]
No independence between \(G_n\) and the controlled error is required;
the indicator can simply be bounded by one on the right-hand side.
No moment estimate for the actual error outside \(G_n\) is asserted.

For \(0<\delta<1\), choose \(n\) sufficiently large that
\(\Pr(G_n^c)\le\delta/2\). Markov at squared threshold
\(2C/(\delta n)\) makes the remaining failure probability at most
\(\delta/2\). Thus the claimed constant may be chosen as
\(C_\delta=\sqrt{2C/\delta}\), after the fixed comparison constants have
been incorporated. A numerical rate for \(\Pr(G_n^c)\) is unnecessary
because the conclusion is for each fixed confidence and sufficiently large
width. For \(\delta\ge1\), the probability claim is vacuous.

The fitted states exist on the fitting event and for the population.
Their prediction difference at the endpoint is bounded pointwise by the
time supremum; taking the input integral preserves this bound.
Hence the endpoint conclusion follows without interchanging a derivative
with an infinite-time limit.

The zero-label case is stationary because the readout and residual vanish;
it requires no activity reparametrization or division by \(S\).

### What remains open

This assembled theorem has no further unidentified quantitative stochastic,
mean-identification, adaptive-control, or physical-clock premise within its
stated scope. H itself remains substantive and unproved on a positive
activity interval. Its initialization and first nonlinear coefficient checks
do not imply that interval estimate. In particular, the assembled theorem
does not establish an unconditional strict root-width rate or a result for
general depth, nonorthogonal training inputs, or unbounded test support.

The feedback/passive candidates and their hashes recorded above remained
unchanged during this final assembly check.
