# Covariance geometry under the dense query-work budget

2026-10-06. Scoped author derivation. The requested query bound is
\(O(Ln^2+dn)\), with both retained state and live query workspace bounded
by an absolute power of \(\log(en)\). No complete decoder or impossibility
result is proved here.

A new estimate addresses one of the missing near-null-direction bounds:
small relative entropy, together with a common history Gram, controls new
cross moments in that Gram's inverse energy. The estimate permits singular
Grams. It yields an inverse-free weak comparison for one conditional
Gaussian query channel. The actual growing neural query circuit still
requires approximate-moment, adaptive-propagation, and evaluation bridges.

## 1. Contract and inherited inputs

Keep the original fixed nonlinear depth \(L\ge2\), spanning training
inputs \(v_a=x_a/\sqrt d\in S^{d-1}\), \(m\ge d\), Gaussian
initialization, zero readout, mean squared loss, and mobilities
\((n,1,\ldots,1,n)\). Activations are analytic on a strip with bounded
first derivative there; values need not be bounded. The original small-label
allowance and initial unweighted training-feature Gram gap are unchanged.
The target remains the dense-pair upper certificate \(b_n\) stated in
`RESULT.md`, on one event for all sphere inputs and all physical times,
including the fitted endpoint. Query inputs are unseen during acquisition;
queries use only current retained information, without training replay or
a dense oracle. Expensive preprocessing is allowed.

The supervisor supplies the same physical interface as
`EFFICIENT_QUERY_DIRECT.md`: uniform forward/backward RMS and mixer
operator bounds, and, with \(Y=\|y\|_2/\sqrt m\),

\[
 \int_0^\infty\rho(t)\,dt\le CY,
 \qquad \sup_{t,a,\ell}\|k_a^{(\ell)}(t)\|_\infty
                 \le CY\sqrt{\log(en)}.
\]

They bound the integrated residual-curvature action by
\(M_n\le CY(1+Y\sqrt{\log(en)})\). The resulting response expansion
converges rapidly, but its terms are dense-operator proof objects until a
counted contraction algorithm is supplied.

The row-law construction in `EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md` gives,
on one event and for every acquired prefix \(c\), a posterior row marginal
\(\pi_c^1\) and a minimum-entropy feasible law \(\nu_c\), each satisfying

\[
 D(\pi_c^1\Vert\mu),D(\nu_c\Vert\mu)\le h,
 \qquad h=H/(\alpha n),
\]

where \(\mu\) is the Gaussian packet prior and \(H\) bounds information
in all scalar summaries. Their retained scalar moments agree only up to
the proved observation-noise tolerances. Exact equality of their history
Grams is therefore a sufficient special case below, not an inherited fact.

## 2. An entropy estimate in the history Gram's geometry

Let \(\pi,\nu\) be probability laws with densities \(p,q\) relative to
a common probability law \(\mu\). Write

\[
 d_0=D(\pi\Vert\mu)+D(\nu\Vert\mu)<\infty.
\]

Let \(F\) be an \(r\)-vector of real row functions with finite second
moments under both laws. Let \(Q\succeq0\) satisfy

\[
 \int FF^T\,d\pi\preceq Q,
 \qquad \int FF^T\,d\nu\preceq Q.                         \tag{1}
\]

For any new row function \(G\) with \(|G|\le B\), define its cross-moment
difference by

\[
 \Delta b=\int FG\,d\pi-\int FG\,d\nu.
\]

Then \(\Delta b\in\operatorname{range}(Q)\) and

\[
 \Delta b^TQ^\dagger\Delta b\le 8B^2d_0.                \tag{2}
\]

In particular, if both entropies are at most \(h\), the right side is
\(16B^2h\). No positive eigenvalue of \(Q\) occurs in the constant.
The most useful case is exact moment consistency:
\(\int FF^T d\pi=\int FF^T d\nu=Q\).

To prove (2), first define the nonnegative density discrepancy

\[
 \chi=\int\frac{(p-q)^2}{p+q}\,d\mu,
\]

with zero integrand when \(p=q=0\). Since
\((\sqrt p+\sqrt q)^2\le2(p+q)\),

\[
 \chi\le2\int(\sqrt p-\sqrt q)^2d\mu
 \le4\left[\int(\sqrt p-1)^2d\mu+
             \int(\sqrt q-1)^2d\mu\right]
 \le4d_0.                                                \tag{3}
\]

For the last inequality, Jensen applied under \(\pi\) gives
\(D(\pi\Vert\mu)\ge-2\log\int\sqrt p\,d\mu\).
The inequality \(-\log u\ge1-u\) then bounds this below by
\(\int(\sqrt p-1)^2d\mu\); the proof for \(q\) is identical.
The middle inequality in (3) is the squared triangle inequality in
\(L^2(\mu)\).

For every \(a\in\mathbb R^r\), weighted Cauchy--Schwarz now gives

\[
\begin{split}
 |a^T\Delta b|^2
 &\le\left[\int(a^TF)^2(p+q)d\mu\right]
       \left[\int G^2\frac{(p-q)^2}{p+q}d\mu\right]\\
 &\le2B^2\chi\,a^TQa
 \le8B^2d_0\,a^TQa.                                      \tag{4}
\end{split}
\]

Null vectors of \(Q\) therefore annihilate \(\Delta b\), proving the
range assertion. On the range, substitute \(a=Q^\dagger\Delta b\)
in (4), and divide by \(\Delta b^TQ^\dagger\Delta b\) when it is
nonzero. This proves (2); the zero case needs no division.

For comparison, positive semidefiniteness alone does not give (2).
The two matrices

\[
 \begin{pmatrix}\varepsilon^2&\varepsilon\\
                 \varepsilon&1\end{pmatrix},\qquad
 \begin{pmatrix}\varepsilon^2&-\varepsilon\\
                -\varepsilon&1\end{pmatrix}
\]

are positive semidefinite and have the same history Gram. Their absolute
cross-moment difference tends to zero, while its squared inverse-Gram
energy is four. Their conditional query means, at history value
\(u=\varepsilon z\), are \(z\) and \(-z\). This example only
invalidates a general PSD-plus-absolute-error argument; no claim is made
that it occurs in the prescribed network.

## 3. One conditional Gaussian query channel

For \(j\in\{\pi,\nu\}\), set

\[
 b_j=\int FG\,dj,\qquad c_j=\int G^2\,dj.
\]

Under (1), the block matrices
\(\left(\begin{smallmatrix}Q&b_j\\b_j^T&c_j\end{smallmatrix}\right)\)
are positive semidefinite: each is the actual Gram of \((F,G)\) plus
a positive semidefinite history block. Thus \(b_j\) lies in the range
of \(Q\), and

\[
 s_j=c_j-b_j^TQ^\dagger b_j\ge0,
 \qquad \|Q^{\dagger/2}b_j\|_2\le B.                    \tag{5}
\]

At a fixed history value \(u\in\operatorname{range}(Q)\), define the
conditional Gaussian output by

\[
 V_j(u)=b_j^TQ^\dagger u+\sqrt{s_j}\,Z,
 \qquad Z\sim N(0,1).
\]

Let \(\psi:\mathbb R\to\mathbb R\) be twice continuously
differentiable, with \(\|\psi'\|_\infty\le K_1\) and
\(\|\psi''\|_\infty\le K_2\). Then

\[
 \left|\mathbb E\psi(V_\pi(u))-\mathbb E\psi(V_\nu(u))\right|
 \le B\sqrt{8d_0}\left[
       K_1\sqrt{u^TQ^\dagger u}+\frac32K_2B\right].       \tag{6}
\]

Indeed (2) bounds the conditional-mean difference by
\(B\sqrt{8d_0}\sqrt{u^TQ^\dagger u}\). Also (3) and
Cauchy--Schwarz give

\[
 |c_\pi-c_\nu|\le B^2\int|p-q|d\mu
       \le B^2\sqrt{2\chi}\le B^2\sqrt{8d_0}.
\]

Factoring the difference of the two quadratic forms in (5) and using
(2), (5) consequently gives

\[
 |s_\pi-s_\nu|\le3B^2\sqrt{8d_0}.                       \tag{7}
\]

For a fixed mean, the Gaussian expectation changes by at most
\(K_2|s_\pi-s_\nu|/2\) when the variance changes. For positive
variances this follows by differentiating the Gaussian density and
integrating twice by parts; adding a common positive variance and taking
it to zero proves the singular case by dominated convergence. Bounded
first derivative ensures the required at-most-linear growth. Change
the mean separately using \(K_1\), obtaining (6).

This is a weak scalar comparison. A coupling of the Gaussian coordinates
themselves need not have root-width error when a residual variance is
nearly zero. Equation (6) avoids that unnecessary requirement.

There is also an averaged form with no maximum leverage. Suppose proof
fields \(u_1,\ldots,u_n\) obey
\(n^{-1}\sum_i u_iu_i^T\preceq Q\). For possibly different tests
\(\psi_i\) with the same derivative bounds, averaging (6) and applying
Cauchy--Schwarz gives

\[
 \frac1n\sum_i\left|
  \mathbb E\psi_i(V_\pi(u_i))-
  \mathbb E\psi_i(V_\nu(u_i))\right|
 \le B\sqrt{8d_0}\left[K_1\sqrt{\operatorname{rank}Q}
                                +\frac32K_2B\right].     \tag{8}
\]

The calculation is
\(n^{-1}\sum_i u_i^TQ^\dagger u_i
 =\operatorname{tr}(Q^\dagger n^{-1}\sum_i u_iu_i^T)
 \le\operatorname{rank}Q\). These width-\(n\) fields are proof
objects, not retained decoder state.

For \(d_0\le2H/(\alpha n)\), polylogarithmic \(H,r,B,K_1,K_2\)
make (8) root width times a fixed logarithmic power. The same entropy
event supports the bound for every deterministic query test having these
bounds. It is not a union of fixed-query probability events.

## 4. Approximate moment matching and regularization

The entropy-tilt source gives approximate moment matching. If every entry
of a common symmetric retained matrix \(C\) differs by at most
\(\varepsilon\) from each of the two history Grams, then

\[
 Q=C+r\varepsilon I
\]

dominates both Grams, since an \(r\times r\) symmetric matrix with
entrywise magnitude at most \(\varepsilon\) has operator norm at most
\(r\varepsilon\). The preceding entropy bounds therefore still apply
to this common enlarged covariance. This observation controls the new
cross moments in a common geometry; it does not establish that replacing
the actual history covariance by \(Q\) has small physical effect.

That missing issue can be made quantitative. Let \(C\succeq0\) be an
actual history Gram, let \(b=C a\), and replace it by \(C+\tau I\)
while keeping \(b,c\) fixed. For empirical history values with Gram
\(C\), the RMS change in the conditional mean is at most

\[
 \frac{\sqrt\tau}{2}\|a\|_2,                             \tag{9}
\]

and the conditional variance increases by at most

\[
 \tau\|a\|_2^2.                                         \tag{10}
\]

To verify both, diagonalize \(C\). A positive eigenvalue \(\lambda\)
contributes \(\lambda\tau^2a_\lambda^2/(\lambda+\tau)^2\)
to the squared mean error and
\(\tau\lambda a_\lambda^2/(\lambda+\tau)\) to the variance
increment. The respective multipliers are at most \(\tau/4\) and
\(\tau\). Null directions contribute zero. Thus (9)--(10) are exact
ridge bias bounds, but they require a bound on the relevant regression
coefficients, or a sharper direct spectral bias estimate. The original
training-feature gap does not bound these growing history coefficients.

An alternative sufficient bridge is a proved relative comparison between
the enlarged covariance and the actual history Gram on the physically
used subspace. Neither the scalar observation-noise bound nor PSD alone
provides it. Artificial noise already present in the exact row construction
may help, but the allowed inputs do not identify a quantitative domination
bound for every adaptive passive-query block; none is assumed here.

## 5. Empirical cross moments: a self-normalized entropy bound

There is a stronger bridge which compares the actual row array directly
to the feasible tilted product law. It needs no sub-Gaussian assumption
on normalized history features.

Let rows \(Z_1,\ldots,Z_n\) be iid under \(\nu^{\otimes n}\),
let \(\int FF^T d\nu\preceq Q\), and let \(|G|\le B\).
Define the empirical Gram \(\widehat Q=n^{-1}\sum_iF(Z_i)F(Z_i)^T\)
and the event \(E=\{\widehat Q\preceq Q\}\). For any deterministic
\(a\), put \(X=a^TFG\), \(Z=X-\mathbb E_\nu X\), and
\(v=B^2a^TQa\). Then \(\mathbb EZ^2\le v\), and on \(E\),

\[
 \frac1n\sum_i Z_i^2
 \le\frac2n\sum_i X_i^2+2(\mathbb EX)^2\le4v.             \tag{11}
\]

For every real \(x\),

\[
 e^{x-x^2}\le1+x+x^2.                                    \tag{12}
\]

Indeed the derivative of
\(\log(1+x+x^2)-x+x^2\) is
\(x(3+x+2x^2)/(1+x+x^2)\). It has the sign of \(x\), and
the function vanishes at zero. Applying (12) to \(\lambda Z\),
taking expectations, and using \(\mathbb EZ=0\), gives

\[
 \mathbb E e^{\lambda Z-\lambda^2Z^2}
 \le1+\lambda^2\mathbb EZ^2\le e^{\lambda^2v}.
\]

Independence and (11) therefore imply, for every \(t>0\),

\[
 \mathbb P_{\nu^{\otimes n}}\left(
   \left|\frac1n\sum_iX_i-\mathbb EX\right|>t, E\right)
 \le2\exp\left(-\frac{nt^2}{20v}\right).                 \tag{13}
\]

For the upper tail, the exponential random variable for the product is
at least \(\exp(n\lambda t-5n\lambda^2v)\) on the indicated
event; choose \(\lambda=t/(10v)\). The lower tail uses \(-Z\).
If \(v=0\), both the population variable and its empirical values on
\(E\) vanish, so no division is necessary.

Let \(r=\operatorname{rank}Q\). A half-radius net of its unit sphere
has at most \(5^r\) points: a maximal separated set has disjoint
radius-one-quarter balls inside the radius-five-quarters ball. Every
vector has norm at most twice its largest pairing with this net.
Applying (13) after whitening on the range of \(Q\) gives

\[
 \mathbb P_{\nu^{\otimes n}}\left(
 \left\|Q^{\dagger/2}\left[\frac1n\sum_iF(Z_i)G(Z_i)
                          -\int FGd\nu\right]\right\|_2>t, E\right)
 \le2\,5^r e^{-nt^2/(80B^2)}.                            \tag{14}
\]

No matrix condition number occurs. Under the reference law, the
population features lie in \(\operatorname{range}Q\) almost surely;
on \(E\), every sampled feature does too.

Now let \(\Pi\) be any possibly dependent law of the row array, with
\(D(\Pi\Vert\nu^{\otimes n})\le K'\). Write \(A_G\) for
the squared norm in (14). Its tail implies

\[
 \log\mathbb E_{\nu^{\otimes n}}
          \exp\left(\frac{n\mathbf1_E A_G}{160B^2}\right)
 \le C(r+1).
\]

For example, if \(a=\log2+r\log5\), (14) bounds the tail of
\(n\mathbf1_EA_G/(80B^2)\) above \(a+s\) by \(e^{-s}\).
Integrating this tail bounds its half-exponential moment by
\(2e^{a/2}\). The entropy inequality, obtained by Jensen under
\(\Pi\) after multiplying by the density ratio, consequently gives

\[
 \mathbb E_\Pi[\mathbf1_E A_G]
 \le\frac{CB^2}{n}(K'+r+1).                              \tag{15}
\]

This controls error on the empirical-Gram event; its complement must be
controlled separately. The result does not claim that iid sampling makes
\(E\) likely without additional information. In the intended use the
retained moment constraints supply that event.

For the source's feasible exponential tilt the required relative entropy
is available. Let \(\Pi=\pi_c\), let \(F_{\rm ret}\) denote
the complete vector of retained tests, and write
\(d\nu_c/d\mu=e^{\lambda^TF_{\rm ret}-\psi(\lambda)}\).
The exact identity is

\[
\begin{split}
 D(\pi_c\Vert\nu_c^{\otimes n})
 &=K(c)-nD(\nu_c\Vert\mu)\\
 &\quad-n\lambda^T\left(\int F_{\rm ret}d\pi_c^1
                              -\int F_{\rm ret}d\nu_c\right).
\end{split}                                             \tag{16}
\]

Both integrals are finite because the retained tests are bounded. The
source's respective \(\eta T\) and \(2\eta T\) moment tolerances,
and \(\|\lambda\|_1\le h/(\eta T)\), give

\[
 D(\pi_c\Vert\nu_c^{\otimes n})\le K(c)+3nh\le4H/\alpha.
                                                               \tag{17}
\]

Thus (15) applies on the same all-prefix information/noise event, for
every deterministic query test selected from the current prefix. This
is an empirical-to-population estimate, not merely a comparison of two
one-row marginals. A rounded tilt incurs an additional term bounded by
\(2nB_{\rm ret}\|\Delta\lambda\|_1\) in (17), by the source's
uniform log-density ratio bound; it can be explicitly budgeted.

## 6. A fixed-depth Gaussian moment recursion has stable weak propagation

The following conditional lemma describes the recursion suggested by
removing the finite-rank innovation projection. It is a concrete sufficient
form, not yet an identification of every actual source-program block.

Let \(\lambda\) denote a law on training row marks. At layer \(\ell\),
the new row output has the form

\[
 h_\ell=\chi_\ell\left(U_\ell^T A_\ell b_{\ell-1}
                              +\sqrt{\beta_\ell}\,Z_\ell\right),
 \qquad \beta_\ell=\sigma_\ell^2+c_{\ell-1}
                       -\|P_\ell b_{\ell-1}\|_2^2,       \tag{18}
\]

where fresh \(Z_\ell\sim N(0,1)\) is independent of the training
marks and \(\sigma_\ell^2\ge0\) is the fixed fresh query-noise
variance. The source bridge uses its positive noise value, identical
under both laws; hence it cancels from every variance difference. Set
\(b_\ell=\mathbb E_\lambda[V_\ell h_\ell]\) and
\(c_\ell=\mathbb E_\lambda[h_\ell^2]\), integrating the fresh
Gaussian too. The normalized mark systems satisfy
\(\mathbb E_\lambda U_\ell U_\ell^T\preceq I\) and
\(\mathbb E_\lambda V_\ell V_\ell^T\preceq I\).
The matrices have \(\|A_\ell\|_{\rm op}\le C\),
\(\|P_\ell\|_{\rm op}\le1\); each displayed variance is nonnegative.
Assume globally

\[
 |\chi_\ell|\le B,\quad |\chi_\ell'|\le a_1,\quad
 |\chi_\ell''|\le a_2.                                  \tag{19}
\]

The bounded functions may be smooth capped versions of physical
activations, provided a separate good-event argument justifies those
caps. Normalized marks themselves need not be bounded.

Compare two laws satisfying these same upper Gram bounds and using the
same matrices in (18). Put
\(x_\ell=\|b_\ell^{(1)}-b_\ell^{(2)}\|_2\) and
\(y_\ell=|c_\ell^{(1)}-c_\ell^{(2)}|\). Suppose errors caused
solely by changing the row law, with the second law's parameters frozen,
are bounded in the two moment outputs by \(\varepsilon_\ell\)
and \(\zeta_\ell\), respectively. Then

\[
\begin{split}
 x_\ell&\le a_1C x_{\ell-1}
   +\frac{a_2}{2}(y_{\ell-1}+2B x_{\ell-1})
   +\varepsilon_\ell,\\
 y_\ell&\le2Ba_1C x_{\ell-1}
   +(a_1^2+Ba_2)(y_{\ell-1}+2B x_{\ell-1})
   +\zeta_\ell.                                         \tag{20}
\end{split}
\]

For the proof, integrate the fresh Gaussian before comparing moments.
The mean response of \(\chi_\ell\) is \(a_1\)-Lipschitz in
its mean and \(a_2/2\)-Lipschitz in its variance, including zero
variance. The corresponding bounds for \(\chi_\ell^2\) are
\(2Ba_1\) and \(a_1^2+Ba_2\), by differentiation. The common
upper Gram bound gives RMS mean difference at most \(C x_{\ell-1}\).
Bessel's inequality gives \(\|b_{\ell-1}^{(j)}\|_2\le B\),
so the variance difference is at most
\(y_{\ell-1}+2Bx_{\ell-1}\). Finally,
\(\|\mathbb E[V_\ell q]\|_2\le\|q\|_{L^2}\) for any
scalar \(q\), by duality and the upper Gram bound. These facts prove
both lines of (20).

Equation (2) supplies
\(\varepsilon_\ell\le4B\sqrt h\),
\(\zeta_\ell\le4B^2\sqrt h\) for the two low-entropy laws.
More usefully, (15) supplies squared-mean bounds of order
\(B^2(H+r+1)/n\) for the empirical law versus the feasible tilt,
on the common-Gram event. The scalar second-moment test is bounded by
\(B^2\), so the analogous scalar entropy bound costs
\(CB^4(H+1)/n\). Use Minkowski in (20) to propagate these posterior
RMS errors. At fixed \(L\), polylogarithmic \(B,a_1,a_2,H,r\)
give polylogarithmic amplification and root-width final moment error.
An output readout in the retained mark span is controlled by the final
cross-moment norm times its RMS norm.

The same method handles the actual finite array of fresh query noises:
conditional on prior query summaries and training marks, a new layer's
noises are independent across rows. Its cross-moment sampling error has
conditional squared norm at most \(B^2r/n\) when the empirical
normalized mark Gram is at most identity, and its scalar second-moment error
has variance at most \(B^4/n\). Add these martingale increments as
source terms in (20). Compare the row-law discrepancy only at the
deterministic tilted-population parameters, so the tests in (15) remain
fixed functions of the training prefix and query. This avoids applying
the entropy lemma to an unjustifiably frozen adaptive test.

The key feature of (20) is its linear dependence on the variance error.
A coupling of the underlying scalar Gaussian coordinates would introduce
the unnecessary square root of that error. No history inverse occurs in
the constants of (20); Gram inverses occur only in the choice of
orthonormal coordinates.

## 7. Physical caps from the complex safe-strip interface

The allowed source interface also offers a concrete way to control
physical training/query fields with unbounded activations. Suppose a
physical preactivation \(z_i(t,v)\) is real for real time, holomorphic
on every disk of radius \(r\) about \([0,T]\), and obeys
\(|\operatorname{Im}z_i|\le s\) there, uniformly in real sphere
query \(v\). Its power series about real \(t\) has real coefficients.
The first sine Fourier coefficient on the circle consequently gives

\[
 r\,\partial_t z_i(t,v)
 =\frac1\pi\int_0^{2\pi}
     \operatorname{Im}z_i(t+r e^{i\theta},v)\sin\theta\,d\theta.
\]

Hence \(|\partial_tz_i|\le4s/(\pi r)\). No bound on the real
part of \(z_i\) is needed for this derivative estimate. The source has
\(r\asymp\log(en)^{-1/2}\) and \(T=O(\log(en))\).
An initial uniform coordinate cap \(C\sqrt{\log(en)}\) therefore
implies

\[
 \sup_{0\le t\le T,v,i}|z_i(t,v)|
      +\sup_{0\le t\le T,v,i}|h_i(t,v)|
 \le C[\log(en)]^{3/2}.                                 \tag{21}
\]

The activation part follows from bounded real slope and fixed
\(|\phi_\ell(0)|\). The initial cap has the usual direct proof in
this fixed-depth Gaussian network: conditional on all preceding layers,
each fixed-input preactivation is Gaussian with uniformly bounded
variance. Intersect bounded initialized operator norms and feature RMS
bounds, use a sphere net of mesh \(n^{-2}\), and apply the Gaussian
tail at \(C\sqrt{\log(en)}\) over its polynomially many points,
neurons and fixed layers. The whole-vector forward Lipschitz constant is
\(C\sqrt n\), so the net interpolation error is at most
\(Cn^{-3/2}\) in each coordinate. The first layer is covered by the
same Gaussian tail argument and its operator norm bound.

The supervisor additionally supplied that completed finite causal source
states approximate physical fields with normalized error \(n^{-a}\)
for a chosen \(a>2\), and use still smaller matrix/scalar noises.
For such accurate states the coordinate error is at most
\(\sqrt n\,n^{-a}\), so (21) supports caps on their final passive
features. The final readout remains a retained history mark controlled
by its RMS norm; no readout cap is required. This statement does not
cover all earlier Picard
iterates inside a source patch. Those iterates need not be coordinatewise
close to the physical trajectory, and their history marks may be large.
Neither (15) nor (20) requires history marks to have a small pointwise
cap: their empirical and population second-moment Grams are sufficient.
Only the new physical scalar test \(G\) needs the bound \(B\).

Concretely, compose \(\phi_\ell\) with a smooth scalar cap equal to
the identity on \([-B,B]\), bounded by \(2B\), with first derivative
bounded by a constant and second derivative bounded by \(C/B\).
The resulting \(\chi_\ell\) has the bounds (19), with
\(a_1\le C\|\phi_\ell'\|_\infty\) and
\(a_2\le C\|\phi_\ell''\|_\infty+
C\|\phi_\ell'\|_\infty^2/B\). It agrees with the physical
query on the cap event and remains globally Lipschitz when the auxiliary
Gaussian query exits that event. No small cap on normalized innovations,
early Picard fields, or regression coefficients is inferred.

## 8. Common-Gram repair with an inherited Gaussian noise floor

The supervisor supplied the following more specific interface for the
finite noisy transcript. Its conditional mean learned mixer is
\(M=T B_0 S^T/n\), with history-column matrices \(S,T\) and
a current-state coefficient matrix \(B_0\). The physical operator
\(M\) is bounded. Raw coefficient norms, history Gram norms, and the
inverse observation-noise scale \(\sigma^{-1}\) are at most
\(\exp(\log(en)^C)\). The scalar-summary noise \(\eta\) can be
chosen subsequently without changing \(\sigma\). This interface is
explicit; it does not follow from physical RMS bounds alone.

Write \(Q_{S,0}=S^TS/n\), \(Q_{T,0}=T^TT/n\). Suppose their
tilted-law analogues differ by at most \(\delta\) in operator norm,
and set

\[
 Q_S^*=Q_{S,\nu}+\tau I,\qquad
 Q_T^*=Q_{T,\nu}+\tau I,\qquad \tau\ge\delta.
\]

Both matrices dominate both corresponding empirical and tilted Grams.
Their whitening therefore gives the upper Gram bounds in Section 6.
The common whitened mean coefficient is

\[
 A=(Q_T^*)^{1/2}B_0(Q_S^*)^{1/2}.                         \tag{22}
\]

Put \(q=\max(\|Q_{S,0}\|,\|Q_{T,0}\|)\) and
\(D=\tau+\delta\). Then

\[
 \|A\|_{\rm op}\le\|M\|_{\rm op}
                    +2\|B_0\|_{\rm op}\sqrt{D(q+D)}.     \tag{23}
\]

Indeed partial-isometry factorizations of \(S/\sqrt n,T/\sqrt n\)
give \(\|M\|=\|Q_{T,0}^{1/2}B_0Q_{S,0}^{1/2}\|\).
For positive semidefinite matrices,
\(\|\sqrt P-\sqrt Q\|\le\sqrt{\|P-Q\|}\).
For completeness, square-root order monotonicity follows by integrating
\(P(P+tI)^{-1}=I-t(P+tI)^{-1}\) against
\(\pi^{-1}t^{-1/2}dt\). Diagonalization and
\(t=\lambda u^2\) verify that this integral is \(\sqrt P\).
If \(\|P-Q\|\le d\), order monotonicity gives
\(\sqrt P\preceq\sqrt{Q+dI}\preceq\sqrt Q+\sqrt dI\),
and the reverse inequality gives the norm bound. Apply it to the two
factors in (22), expand their product difference, and use
\(\|Q_j^*\|\le q+D\) to prove (23). There is no empirical
Gram gap in this argument.

Suppose the exact forward-observation residual variance is

\[
 \beta=\sigma^2+c-v^T(\sigma^2I+Q_0)^{-1}v\ge\sigma^2, \tag{24}
\]

where \(Q_0\) is the empirical forward-history Gram and \(v\) its
cross moment with the query input. The first \(\sigma^2\) is the
fresh passive-query observation noise; the ridge comes from the training
observation noise. This follows the source's equally noised query
convention. If \(Q^*\succeq Q_0\) and
\(\|Q^*-Q_0\|\le D\), replacing \(Q_0\) by \(Q^*\) gives

\[
 0\le\beta^*-\beta\le(D/\sigma^2)c.                    \tag{25}
\]

To prove this, put \(R=(\sigma^2I+Q_0)^{-1}\) and
\(E=R^{1/2}(Q^*-Q_0)R^{1/2}\). Then
\(0\preceq E\preceq D\sigma^{-2}I\), and

\[
 R-(\sigma^2I+Q^*)^{-1}
 =R^{1/2}[I-(I+E)^{-1}]R^{1/2}
 \preceq(D/\sigma^2)R.
\]

Multiply by \(v\) and use \(v^TRv\le c\) from (24).
After whitening, the quadratic coefficient is
\((Q^*)^{1/2}(\sigma^2I+Q^*)^{-1}(Q^*)^{1/2}\preceq I\).
It thus has the form \(P^TP\) required in (18). Both laws have
variances at least \(\sigma^2\) by their upper Gram bounds. Numerical
rounding may project the computed variance onto \([\sigma^2,\infty)\);
this map is one-Lipschitz.

For an error allowance \(\varepsilon\), choose \(D\) so that

\[
 2\|B_0\|\sqrt{D(q+D)}\le\varepsilon,
 \qquad D B^2/\sigma^2\le\varepsilon.                    \tag{26}
\]

Here \(B\) is the physical row cap. The stated coefficient and noise
floor bounds make \(\log(1/D)\) polynomial in \(\log n\), also
for \(\varepsilon=n^{-A_0}\) with fixed \(A_0\). Entrywise
scalar-summary tolerances must additionally include their matrix dimension
factor. This precision choice would be circular if the Gaussian floor or
coefficient bounds deteriorated too rapidly with the subsequently chosen
\(\eta\); their stated independence is essential.

## 9. The finite Gaussian transcript and removal of its covariance correction

Here the transcript is a finite adaptive sequence of noisy linear matrix
observations, with at most \(R\) calls per initialized matrix. It is not
the complete continuous-time history. At each call the queried vector is
measurable with respect to the previous observations, and the new
observation noise is independent Gaussian. Condition on the observable
transcript, including its query vectors but not the unobserved noise roots.
Once past observations are fixed, the query vector at the next call is
fixed, and its likelihood is a Gaussian exponential in only the called
matrix. Multiplying these likelihoods shows inductively that the posterior
matrices remain independent Gaussian blocks. This argument fails for
nonpredictable query vectors or for conditioning on unrelated extra
matrix-dependent information; neither is included in this transcript.

For a particular block, collect forward query vectors as columns of
\(V\) and reverse query vectors as columns of \(U\). In vectorized
coordinates the posterior precision is the prior precision plus the two
positive semidefinite contributions from \(VV^T\) on the input index
and \(UU^T\) on the output index. These contributions commute, since
they act on different tensor factors. On the output subspace orthogonal
to \(\operatorname{range}U\), the reverse contribution is zero.
Consequently, for a new query input \(q\), its conditional answer
covariance has the form

\[
 \Gamma(q)=\beta(q)I-K(q),\qquad
 0\preceq K(q)\preceq\beta(q)I,\qquad
 \operatorname{range}K(q)\subseteq\operatorname{range}U,  \tag{27}
\]

The actual passive answer additionally has its independent fresh
\(\sigma\)-scaled observation noise; this adds \(\sigma^2I\)
to both covariance terms and does not change the correction's rank.
Here \(\beta(q)\) is (24), with
\(c=\|q\|_2^2/n\) and \(v=V^Tq/n\). Thus
\(\operatorname{rank}K(q)\le R\). The scaling in (24) corresponds
to forward observations whose normalized noise variance is \(\sigma^2\).
Different known positive noise levels give the analogous diagonal ridge;
the smallest level supplies the same estimates.

Use the same standard Gaussian vector \(g\) to couple
\(\Gamma(q)^{1/2}g\) with \(\sqrt{\beta(q)}g\). Diagonalize
\(\Gamma(q)\). Every direction outside the rank-\(R\) correction
has identical eigenvalue \(\beta(q)\), while each remaining squared
square-root difference is at most \(\beta(q)\). Therefore

\[
 \mathbb E\frac{\|\Gamma(q)^{1/2}g
                    -\sqrt{\beta(q)}g\|_2^2}{n}
 \le\frac{\beta(q)R}{n}
 \le\frac{R}{n}\left(\sigma^2+\frac{\|q\|_2^2}{n}\right).
                                                               \tag{28}
\]

This coupling has no inverse-noise cost. A fresh passive query uses each
layer's posterior matrix only once, so its incoming field is independent
of that layer's posterior centered matrix, conditional on the finite
training transcript and preceding passive layers.

To propagate (28), the centered posterior matrix has covariance at most
the prior covariance. For every vector \(v\) independent of that layer,

\[
 \mathbb E\|W_{\rm centered}v\|_2^2/n\le\|v\|_2^2/n.  \tag{29}
\]

This follows by summing the variance of its \(n\) output coordinates;
each prior variance is \(\|v\|_2^2/n\). If the conditional mean
learned matrix has norm at most \(C\), its complete conditional
second-moment Lipschitz factor is at most \(C^2+1\); the centered
cross term has expectation zero. Couple the independent fresh observation
noise identically in the two higher-layer queries, so it cancels from
their difference. Compose with the globally Lipschitz caps
from Section 7.

Use a layer-by-layer hybrid: lower layers have already had the covariance
correction removed, the current layer is coupled by (28), and all higher
layers still use their exact posterior matrices. Shared higher matrices
propagate the difference by (29). Since the depth is fixed and capped
input RMS is at most \(B\), the RMS prediction difference is at most
\(C_L\sqrt{\sigma^2+B^2}\sqrt{R/n}\) times the final readout
RMS, after summing
the fixed number of hybrids. This is uniform as a conditional bound in
the query and in a source time having the same training event; it does
not assert a simultaneous pathwise coupling for uncountably many inputs.
The original robust conditional-center transfer is needed for the final
all-query event.

The conditional mean-operator event can be constructed without imposing
a norm bound on every possible posterior draw. Let
\(Z_\ell=\|W_\ell(0)\|_{\rm op}^2\), whose Gaussian expectation
is width-independent. For the observable prefix filtration,
\(\mathbb E[Z_\ell\mid\mathcal F_j]\) is a nonnegative
martingale. The first-crossing argument bounds the probability that its
maximum exceeds \(\mathbb EZ_\ell/\alpha\) by \(\alpha\).
Conditional Jensen then gives
\(\|\mathbb E[W_\ell(0)\mid\mathcal F_j]\|^2
 \le\mathbb E[Z_\ell\mid\mathcal F_j]\).
Intersect over fixed \(L\), and separately impose the supplied bound
on the finite source learned displacement. This gives the required bound
on the conditional mean learned mixer for every prefix. Do not condition
the Gaussian law further on the event of a small realized matrix norm:
the martingale event is already measurable from the observed history.

The learned displacement of the finite source scheme is a sum of training
outer products (including the collocation update coefficients), hence
has the same finite-factor form as its conditional Gaussian mean.
Concatenating their input and output history columns gives \(T B_0S^T/n\)
from Section 8. After removing (27), a new answer row is therefore

\[
 \chi_\ell\left(T_i^TB_0 b+
           \sqrt{\sigma^2+c-v^T(\sigma^2I+Q_V)^{-1}v}\,g_i\right),
 \quad b=S^Tq/n,\quad c=\|q\|_2^2/n,                    \tag{30}
\]

with fresh iid \(g_i\). Include \(V\) among the columns of \(S\),
so \(v\) is a subvector of \(b\). The common-Gram repair then turns
(30) into (18). The first affine layer uses the initialized Gaussian
first-row marks and the acquired learned update; it does not require a
hidden-matrix posterior step. The trained readout is one of the final
retained history marks.

This establishes the normal form for a finite predictable Gaussian
transcript with the supplied displacement/coefficient interfaces.
Identifying the scalar-noised compact row program with that consistent
finite transcript still uses the supervisor's source coupling and its
counted global sensitivity: choose scalar noise and rounding so their
product with that sensitivity is at most \(n^{-A_0}\). The present
allowed six files do not contain the full source construction proving
those numerical interfaces; they remain explicit supplied inputs.

## 10. Remaining neural and computational obligations

Equations (2), (15), and (20) improve the available geometry: exact matching
of history second moments plus low entropy controls near-null cross
directions and empirical cross-moment errors. A fixed-depth Gaussian
moment recursion propagates those errors without a variance square-root
loss. The following implications are still unproved here for the actual
network query circuit.

1. **Physical tests.** The cap construction and finite-depth recurrence
   now supply bounded tests for the normal form. Applying them to the
   actual scalar-noised source uses its supplied completed-state coupling.
   The harmonic envelope must not be extended to inaccurate intermediate
   Picard fields; those are controlled only through their history Grams.
2. **Matching tolerance.** Verify the noisy-observation and independently
   selectable precision interfaces of Sections 8--9 in the full source
   construction. Their displayed algebra controls common-Gram enlargement
   without an actual history Gram gap. Physical mean-operator bounds alone
   would not control an ungapped projection's ridge bias.
3. **Source-program identification.** Section 9 identifies the passive
   recursion for the finite predictable Gaussian transcript. Its use for
   the scalar-noised, compressed current state depends on the supplied
   source coupling and sensitivity/precision bounds. The full continuous
   training history cannot replace this finite transcript.
4. **Certificate scale.** The fixed-depth route produces root-width error
   times a fixed logarithmic power, with no residual-curvature exponential.
   For fixed nonzero labels this is eventually smaller than the stated
   certificate's positive \(\exp(CY^2\sqrt{\log(en)})\) allowance.
   The width threshold can depend on the original fixed parameters.
   In contrast, a physical forcing interpretation would permit
   the existing mobility stability estimate, with amplification at most
   \(e^{M_n}\) along a verified admissible homotopy. Such a forcing has
   not been constructed. The required quantitative condition remains
   \(e^{M_n}\varepsilon_n=O(b_n)\); the label
   \(n^{-1/2+o(1)}\) alone does not compare the constants in the inherited
   exponential certificate.
5. **Evaluation.** The constrained tilt's multipliers and normalization,
   and every new Gaussian expectation, must have counted acquisition and
   query algorithms. A finite tilt description and the present stability
   estimate do not evaluate these integrals.

The relaxed query budget does not remove these obligations. In particular,
the factorial response theorem permits
\(K=O(\log(en)/\log\log(e^e n))\) curvature insertions. A dense
Hessian-vector action itself costs dense work when the parameter and
tangent arrays are available, but those arrays violate the live-space
budget. Performing \(K\) separately charged dense actions also exceeds
the specified \(O(Ln^2+dn)\) work by an unbounded factor. Both the sum
of contractions and its workspace must be reduced.

Even an ordinary dense forward pass achieves its usual quadratic work by
retaining width-\(n\) layer values. Literal scalar recursion with no such
array repeatedly recomputes earlier layers; at fixed depth its naive work
has a power of \(n\) growing with depth. This is a count for that naive
implementation, not a time-space lower bound for all possible decoders.

No step above uses test labels, tightens the label allowance, freezes
feature learning, or changes the all-sphere/all-time target. The existing
prediction tail would handle the fitted endpoint after a finite-horizon
decoder is established; this note does not assume endpoint response
derivatives.

## 11. Status and provenance

The entropy cross-moment bound, conditional Gaussian weak comparison,
averaged leverage cancellation, ridge bias formulas, self-normalized
empirical estimate, posterior-to-tilted-product entropy bound, fixed-depth
weak moment propagation, safe-strip derivative bound, common-Gram repair,
and finite-transcript covariance-removal comparison are proved above
under their explicit hypotheses. They are author-checked partial results;
no independent PASS or promotion is claimed. The existence of the requested
dense-budget compact decoder remains open in this scoped note.

Complete scientific inputs read: `RESULT.md`, `EFFICIENT_QUERY_DIRECT.md`,
`EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md`, `ROOT_RESPONSE_AND_COVARIANCE.md`,
`SOURCE_SUPREMUM_EXTENSION.md`, and `GROWING_PROGRAM_STABILITY.md` in this
study. Linked files and other studies were not opened. Required research
and rigorous-proof skills and relevant research-contract, evidence-ledger,
and adversarial-audit references were read. The supervisor reported that
the custom canonical-notation skill is inaccessible and authorized the
explicit notation fallback; no contents of that unavailable skill or its
neural reference are inferred. Only this assigned file was edited. No
experiment, external source retrieval, Git operation, or dense computation
was performed.
