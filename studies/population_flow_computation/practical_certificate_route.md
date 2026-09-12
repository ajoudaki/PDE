# Practical propagation certificate and its missing input

**Status:** bounded theoretical route, authored 2026-09-12. The conditional certificate below is proved here, but its useful-size hypothesis has not been established for the specified trajectory. No experiment, trajectory evaluation, or independent review was performed. This is study material, not a promoted result.

**Input scope:** the supervisor's self-contained assignment only, plus shared workflow and the investigate-conjectures and solve-math-rigorously skill instructions and their contract/audit references. No scientific repository source, other route, study history, or external scientific source was read. The actual operator \(A_0\) was not supplied beyond its stated norm/source properties. Write ownership is this file only; the supervisor owns the study README.

The strongest conclusion is conditional. A useful a posteriori certificate can use a verified one-sided bound in a self-consistent tube around the approximation and certified forward/backward query defects. The inverse-gate coordinate removes the unbounded multiplication by \(Q\), so tails are not an unavoidable obstacle to mere \(L^2\) convergence. However, its direct global constants are too large to establish practical resources. Neither loss decay nor a Gaussian marginal bound for \(Q\) supplies the missing small amplification estimate. In raw weight coordinates, even a small \(L^2\) tube around a benign state can contain unbounded positive curvature; finite empirical moments cannot exclude that phenomenon.

## 1. Contract and exact gradient structure

The target is the same population model with data law \(\frac12(e_1,+1)+\frac12(e_2,-1)\), through physical time \(T=40\):

\[
H_a=\tanh w_a,\quad Z_a=AH_a,\quad V_a=\tanh Z_a,\quad
f_a=\mathbb E[cV_a],\quad D_a=c\operatorname{sech}^2Z_a,\quad Q_a=A^*D_a,\quad A=A_0+K.
\]

The operator maps column \(L^2\) to row \(L^2\); \(K\) has Hilbert--Schmidt norm. Use the supplied bounds

\[
f_a=y_ab,\quad e=1-b>0,\quad e(t)\le e^{-t/5},\quad
s'=2e,\quad s(40)\le10,
\]
\[
\|A\|\le a:=2+\sqrt{10},\qquad
\|c\|_2\le C_2:=\sqrt{10},\qquad \|c\|_\infty\le C_\infty:=10.
\]

An approximation must generate its own states from the prescribed initial law and actual \(A_0\). Explicit source functions, finite source/history representations, and certified operator queries are permitted. Target-trajectory forcing and raw all-to-all matrix training are excluded. The proposed error is a coupled \(L^2\times\mathrm{HS}\times L^2\) state error, which controls features and predictions. Complexity of producing the query certificates remains a separate obligation.

All conclusions are deterministic on the event that the certificate inputs hold. A randomized implementation must prove that event's probability, including adaptive/time-uniform queries. An empirical standard error is not such a proof. Time discretization, representation, and sampling errors enter separately through the defect; no interchange of limits is used.

For \(b(\theta)=\frac12\sum_a y_af_a(\theta)\) and the canonical parameter inner product on \(\theta=(c,K,w_1,w_2)\), the reference trajectory obeys

\[
\theta_t=2e\nabla b,\qquad \theta_s=\nabla b.
\tag{1.1}
\]

Indeed, \(\theta_t=-\sum_a r_a\nabla f_a\) and \(r_a=-y_ae\). Thus

\[
c_s=\tfrac12\sum_a y_aV_a,\quad
K_s=\tfrac12\sum_a y_aD_a\otimes H_a,\quad
(w_a)_s=\tfrac12y_a\operatorname{sech}^2(w_a)Q_a.
\tag{1.2}
\]

The scalar extension \(F(\theta)=2(1-b)\nabla b\) has, wherever directional derivatives are legitimate,

\[
DF=-2\nabla b\otimes\nabla b+2e\nabla^2b.
\tag{1.3}
\]

The first term dissipates only the gradient direction. Directions perpendicular to \(\nabla b\) retain all positive curvature of \(b\). Scalar loss decay therefore does not itself certify population-state contraction. The extension agrees with the exact reference trajectory; any numerical discrepancy from this extension must be charged as a defect.

## 2. An exact global \(L^2\) route, with impractical constants

Let \(j_X=\operatorname{sech}^2j\), \(j(0,g)=g\), and set \(w_a=j(X_a,g_a)\), \(h(X,g)=\tanh j(X,g)\). This chart is global:

\[
X=J(w)-J(g),\qquad J(w)=\frac w2+\frac{\sinh(2w)}4,\qquad
J'(w)=\cosh^2w\ge1.
\]
\[
|j_X|\le1,\qquad h_X=\operatorname{sech}^4j\in[0,1].
\tag{2.1}
\]

For \(U=(c,K,X_1,X_2)\), the feature-clock vector field \(G\) is

\[
G_c=\tfrac12\sum_a y_aV_a,\quad
G_K=\tfrac12\sum_a y_aD_a\otimes H_a,\quad
G_{X_a}=\tfrac12y_aQ_a.
\tag{2.2}
\]

The unbounded product \(Q_a\delta w_a\) has disappeared. This is an exact coordinate change. Also \(X(0)=0\), and

\[
\left(\tfrac12\sum_a\|X_a(s)\|_2^2\right)^{1/2}
\le\tfrac12\int_0^s\|A(\tau)\|\|c(\tau)\|_2\,d\tau<\infty.
\]

For two states satisfying the same bounds, write

\[
z=(z_c,z_K,z_X):=
\left(\|\Delta c\|_2,\|\Delta K\|_{\rm HS},
\left(\tfrac12\sum_a\|\Delta X_a\|_2^2\right)^{1/2}\right).
\]

Let \(\alpha=4/(3\sqrt3)\), the maximum absolute derivative of \(\operatorname{sech}^2\). With the same averaged norm over examples, differences obey

\[
H_\Delta\le z_X,\quad Z_\Delta\le az_X+z_K,\quad
D_\Delta\le z_c+\alpha C_\infty Z_\Delta,\quad
Q_\Delta\le aD_\Delta+C_2z_K.
\tag{2.3}
\]

For example, split \(AH-\widetilde A\widetilde H=A(H-\widetilde H)+(K-\widetilde K)\widetilde H\), use \(\|\widetilde H_a\|_2\le1\), and split \(c\operatorname{sech}^2Z-\widetilde c\operatorname{sech}^2\widetilde Z\) with bounded factor \(\widetilde c\). The backward split uses \(\|\widetilde D_a\|_2\le C_2\). Also

\[
\|D_a\otimes H_a-\widetilde D_a\otimes\widetilde H_a\|_{\rm HS}
\le\|\Delta D_a\|_2+C_2\|\Delta H_a\|_2.
\]

Consequently two feature-clock paths with block defect \(d\) satisfy, in upper right derivatives,

\[
D^+z\le Mz+d,\qquad
M=
\begin{pmatrix}
0&1&a\\
1&\alpha C_\infty&\alpha C_\infty a+C_2\\
a/2&(a\alpha C_\infty+C_2)/2&a^2\alpha C_\infty/2
\end{pmatrix}.
\tag{2.4}
\]

This is a genuine width-independent propagation estimate. It needs no Gaussian tail assumption. An approximating method must enforce or certify its own readout supremum bound; a small \(L^2\) defect alone does not imply that bound.

The final diagonal entry of the worst-case matrix is approximately \(102.6\). A componentwise estimate through \(s=10\) can therefore contain an \(\exp(1026)\) factor. Time-dependent bounds might reduce it, but no supplied argument makes it practical. The chart repairs the topology, not the constants.

The same derivation gives

\[
|b(U)-b(\widetilde U)|\le z_c+C_2z_K+C_2az_X.
\tag{2.5}
\]

Since \(|j_X|\le1\), \(X\)-error also controls raw \(w\)-error. An individual prediction satisfies the analogous estimate with \(\|\Delta X_a\|_2\) in place of \(z_X\).

## 3. A self-consistent certificate retaining signed amplification

Equip \(U\) with the Hilbert norm corresponding to \(z_c^2+z_K^2+z_X^2\), and put \(\mathcal F(U)=2(1-b(U))G(U)\). The exact target satisfies \(U_t=\mathcal F(U)\). Let an independently generated, continuous, piecewise absolutely continuous path \(\widehat U(t)\) have full physical-clock defect

\[
\eta(t)=\widehat U_t-\mathcal F(\widehat U),\qquad \|\eta(t)\|\le d(t).
\tag{3.1}
\]

Suppose a radius \(R>0\), an integrable scalar \(\ell(t)\), and an a priori feasible set \(\mathcal D(t)\) have been certified. The exact target must belong to \(\mathcal D(t)\), and for every \(U\in\mathcal D(t)\) with \(\|U-\widehat U(t)\|\le R\), require

\[
\langle U-\widehat U,\mathcal F(U)-\mathcal F(\widehat U)\rangle
\le\ell(t)\|U-\widehat U\|^2.
\tag{3.2}
\]

The feasible set may use the supplied energy and supremum bounds, but cannot use unknown target-trajectory values. For \(r_0\ge\|U(0)-\widehat U(0)\|\), define

\[
\rho(t)=e^{\int_0^t\ell(v)\,dv}
\left[r_0+\int_0^t e^{-\int_0^u\ell(v)\,dv}d(u)\,du\right].
\tag{3.3}
\]

**Certificate theorem.** If \(\sup_{0\le t\le40}\rho(t)<R\), then

\[
\|U(t)-\widehat U(t)\|\le\rho(t)\qquad(0\le t\le40).
\tag{3.4}
\]

**Proof.** Before the first exit from the tube, \(E=U-\widehat U\) satisfies, by (3.1), (3.2), and Cauchy--Schwarz,

\[
\tfrac12(\|E\|^2)'\le\ell\|E\|^2+d\|E\|.
\]

Where the norm is nonzero, divide by it. At zero its upper right derivative is at most \(d\); alternatively regularize the norm by \((\|E\|^2+\epsilon^2)^{1/2}\) and pass to the limit. Multiplying the resulting scalar inequality by the integrating factor gives \(\|E\|\le\rho\). Continuity and \(\sup\rho<R\) exclude the first exit. Continuous time-interpolation knots are allowed; jumps must instead be charged as jump defects.

This is an actual a posteriori test: construct \(\widehat U,d,\ell,R\), validate (3.2) over the described tube, and check (3.3). No target trajectory determines its coefficients. Negative \(\ell\) is retained. Modest amplification of its Green function permits useful defects; a failed test gives no practical accuracy guarantee.

One sufficient validation is a bound on the symmetric directional derivative of \(\mathcal F\) throughout every segment from \(\widehat U\) to the feasible tube. Integrating the directional derivative along each segment gives (3.2). The bounded-factor estimates in (2.3) justify these derivatives on segments with bounded readout and operator norm. No operator-norm continuity of the derivative on an unrestricted \(L^2\) ball is asserted. A derivative evaluated only at the center does not establish (3.2).

In these coordinates,

\[
D\mathcal F=2(1-b)DG-2G\otimes Db.
\tag{3.5}
\]

The final term is not automatically negative in the \(X\) inner product: \(G\ne\nabla_Xb\). Its actual symmetric part must be controlled. The negative rank-one term (1.3) can only be imported with the correct raw-parameter metric and necessary domain/tail bounds.

### 3.1 Forward, backward, residual, and time defects

At its own state, suppose the approximation evaluates

\[
\widetilde Z_a=A\widehat H_a+\zeta_a,\quad
\widetilde D_a=\widehat c\operatorname{sech}^2\widetilde Z_a,\quad
\widetilde Q_a=A^*\widetilde D_a+q_a.
\]

Let \(\zeta,q\) be the averaged \(L^2\) norms of these defects. For the feature-clock field formed from these queries,

\[
\|\widetilde G-G(\widehat U)\|_{\rm blocks}
\le\left(\zeta,\alpha C_\infty\zeta,
\tfrac12(a\alpha C_\infty\zeta+q)\right).
\tag{3.6}
\]

If the computed common residual is \(e_{\rm num}=1-b_{\rm num}\), with
\(|b_{\rm num}-b(\widehat U)|\le\epsilon_b\), the physical-clock block defect is bounded by

\[
2|e_{\rm num}|
\left(\zeta,\alpha C_\infty\zeta,
\tfrac12(a\alpha C_\infty\zeta+q)\right)
+2\epsilon_b(1,C_2,aC_2/2)+d_{\rm time}.
\tag{3.7}
\]

Here \(d_{\rm time}\) includes actual interpolation/integration defect and any discrepancy from the scalar reference extension. Indeed,

\[
2e_{\rm num}\widetilde G-2(1-b)G
=2e_{\rm num}(\widetilde G-G)-2(b_{\rm num}-b)G,
\]

and \(\|G_c\|\le1,\|G_K\|\le C_2,\|G_X\|\le aC_2/2\). The Euclidean norm of the nonnegative block vector supplies \(d(t)\). A history method not storing \(K\) must still supply a reconstruction and defect interpretation for this same operator model.

## 4. The missing observable is joint and directional

The missing item for this practical route is a computable, moderate bound (3.2) over a self-consistent set of possible population errors. Possible sources are sourcewise envelopes plus validated integration, a proved invariant cone restricting error shapes, or a direct dissipativity estimate. A sampled Jacobian maximum does not establish it.

In raw \(w\) coordinates, a dangerous coefficient is

\[
\kappa_a(g,t)=
\big[-y_aQ_a(g,t)\tanh w_a(g,t)\operatorname{sech}^2w_a(g,t)\big]_+.
\tag{4.1}
\]

It appears because the Hessian contains

\[
\tfrac12\sum_a y_a\int Q_a\tanh''(w_a)(\delta w_a)^2
=-\sum_a\int y_aQ_a\tanh w_a\operatorname{sech}^2w_a(\delta w_a)^2.
\tag{4.2}
\]

A sourcewise bound on (4.1), throughout a validated reachable tube, controls this part of positive curvature. Signed outer-gate curvature and mixed \(c,K,w\) terms still need bounds; (4.1) alone is not a full certificate.

A finite \(p\)-moment gives only

\[
\int\kappa_a(\delta w_a)^2
\le\|\kappa_a\|_p\|\delta w_a\|_{2p/(p-1)}^2,\qquad 1<p<\infty.
\tag{4.3}
\]

It does not close in raw \(L^2\). A source envelope for the error, or a stronger error norm, can close it; neither follows from an \(L^2\) defect. A proved source/history relation might instead align large \(Q_a\) with the gate and bound (4.1). That is a joint signed dynamical property, not a marginal tail bound for \(Q_a\).

### 4.1 Explicit obstruction to an unrestricted raw-\(w\) \(L^2\) tube

This example tests what the supplied norm bounds and Gaussian marginal imply. It is **not** claimed to be reached by the specified initialized flow or to use the unspecified actual \(A_0\).

Take column source \(g=(g_1,g_2)\sim N(0,I_2)\), any probability row source, \(c=1,K=0\), and

\[
(A_0v)(\eta)=\mathbb E[g_1v(g)],\qquad \|A_0\|=1.
\]

Set \(w_1=v(g_1),w_2=-v(g_1)\). With \(m=\mathbb E[g_1\tanh v(g_1)]\),

\[
Z_1=m,\quad Z_2=-m,\quad f_1=-f_2=\tanh m,\quad
Q_1=Q_2=\operatorname{sech}^2(m)g_1.
\tag{4.4}
\]

The backward field is exactly Gaussian, variance at most one, with zero remainder, and output symmetry is preserved.

Begin with the benign state \(v(g_1)=g_1\). Fix \(h>0\), and replace \(v(g_1)\) by \(-h\) on \(g_1>L\). Its \(L^2\) change tends to zero because

\[
\int_L^\infty(g_1+h)^2\,d\gamma(g_1)\longrightarrow0.
\]

The benign raw-weight displacement from initial \(g\) has squared norm \(2\); the additional tail cost tends to zero. Together with \(c^2=1,K=0\), these states lie within the supplied energy bound for all sufficiently large \(L\). They obey all displayed operator/readout bounds. Reachability from \(c(0)=0\) is not asserted.

For symmetric variations \(\delta w_1=u,\delta w_2=-u\), direct differentiation yields

\[
\delta^2b=
\operatorname{sech}^2m\,\mathbb E[g_1\tanh''v\,u^2]
+(\operatorname{sech}^2)'(m)
\big(\mathbb E[g_1\operatorname{sech}^2v\,u]\big)^2.
\tag{4.5}
\]

Take \(u\) as the normalized indicator of \(g_1\in[M,M+1]\), \(M>L\). On this interval \(\tanh''(-h)=2\tanh h\operatorname{sech}^2h>0\), so the first term is bounded below by a positive constant times \(M\). By Cauchy--Schwarz the absolute value of the second term is bounded by a fixed constant times

\[
\mathbb E[g_1^2\mathbf1_{[M,M+1]}]\longrightarrow0.
\]

The full direction has squared norm \(2\), so its Hessian Rayleigh quotient tends to \(+\infty\). Thus an arbitrarily small raw-\(w\) \(L^2\) neighborhood of a benign state can contain unbounded positive Hessian form while \(Q\) remains Gaussian with bounded variance.

This rules out deducing a uniform raw-\(w\) tube derivative/logarithmic-norm estimate from those bounds alone. It attacks that sufficient check and pairwise local one-sided Lipschitzness, not every anchored secant estimate of the form (3.2), which can be weaker and exploit cancellations. Reachability or an error-shape restriction might also exclude these perturbations; that exclusion is additional scientific input. The example does not disprove stability of the actual initialized trajectory, nor the inverse-chart route.

### 4.2 Why finite empirical moments cannot close this gap

A positive-measure Gaussian tail can avoid any finite set of sampled sources. Altering a source function there leaves all its empirical values and moments unchanged. Under independent sampling a region of mass \(p\) is missed with probability \((1-p)^n\), which is near one for \(p\ll1/n\).

The preceding construction puts arbitrarily large positive raw-\(w\) curvature on such tails. Even a perfectly known Gaussian marginal for \(Q\) does not supply the missing joint alignment and error-direction information. The scalar \(m\), hence the exact law (4.4), can also be preserved: compensate the small tail change on a second unsampled region with \(g_1>0\), where the derivative of \(v\mapsto\mathbb E[g_1\tanh v]\) is nonzero. Continuity and that nonzero derivative give the small adjustment. Thus observing the correct forward scalar does not exclude hidden curvature.

This is a deterministic non-identification statement for finite empirical summaries. It does not preclude rigorous randomized certificates based on a proved tail envelope, regularity class, reachable-state relation, or concentration theorem with checked assumptions. That extra structure must precede the guarantee.

## 5. A separate endpoint prediction certificate

The supplied residual decay gives

\[
1-e^{-8}\le b(40)<1.
\]

For any independently computed \(\widehat b_{40}\), direct comparison with this interval gives

\[
|b(40)-\widehat b_{40}|
\le\max\{|1-\widehat b_{40}|,\,
|1-e^{-8}-\widehat b_{40}|\}.
\tag{5.1}
\]

If the reported numerical value has certified uncertainty \(\delta\), add \(\delta\). In particular, a separately certified endpoint in the same interval differs from the exact endpoint by at most \(e^{-8}\approx3.36\times10^{-4}\), plus numerical uncertainty. This only localizes endpoint predictions \(f_a=y_ab\); it does not certify learned features, population state, early trajectory, or solver convergence.

## 6. Claim status and decisive next input

| Claim | Status and scope |
|---|---|
| Inverse gate removes the raw \(Q\delta w\) multiplier | Exact algebra, Section 2 |
| Width-independent global \(L^2\) majorant | Proved under both paths' bounds, (2.4); constants are impractical |
| A posteriori one-sided tube theorem | Conditional result, (3.1)--(3.4); useful bound not instantiated |
| Operator/residual defect conversion | Proved for the stated own-state interface, (3.6)--(3.7) |
| Gaussian \(Q\) and energy imply a raw-\(w\) uniform local derivative/pairwise one-sided bound | False as a deduction from these bounds alone, Section 4.1 |
| Actual initialized trajectory is unstable | Not claimed; example does not establish reachability |
| Finite empirical moments establish the missing bound | False without additional structural/probabilistic input |
| Practical full-state independent population solver through \(T=40\) | Open from the supplied inputs |
| Endpoint prediction localization | Consequence of supplied decay, (5.1) |

The next high-value input is a verified bound on positive error amplification for the generated source/history family, including how errors occupy its tails. It should have a self-consistent form such as (3.2), or an explicit stronger error norm closing (4.3). More empirical moments without that structure do not close the bottleneck. No new computation is authorized or proposed by this report.
