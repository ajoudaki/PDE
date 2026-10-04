# Dense width route: exact history, initial quantitative bounds, and the open repeated-query estimate

This is a scoped internal research result of 2026-10-01. Scientific inputs were the study README, `docs/notation.qmd`, the setting in `paper/main.tex`, `paper/results.tex`, and the complete `paper/proof_alltime.tex` and `paper/proof_tracking.tex`. The required mathematical presentation and proof skills were applied. No other study was read.

**Status.** No all-time root-width theorem for the trained dense network is proved here. In particular, the current manuscript does not establish a root-width finite-to-population rate even for each fixed clipping cap. What is proved below is (i) an exact dense-history reduction identifying the random quantities that require quantitative control, (ii) a root-width initialization theorem for every fixed depth under the manuscript's activation assumptions, and (iii) an inverse-free root-width coupling for one genuine forward/adjoint reuse of a Gaussian matrix. The third statement includes the response mean and the finite-width correction to its second moment. It applies to the first nonzero backward response in a two-hidden-layer nonlinear dense network. It does not assume that trained neurons are independent.

## 1. Exact finite history and the oracle comparison that remains necessary

Write \(v_a=x_a/\sqrt d\), \(G_{ab}=v_a^\top v_b\), \(g_\ell=\phi_\ell'\), and \(r_a=f_a-y_a\). Finite vectors have ordinary Euclidean norm; every width normalization is displayed. Consider the auxiliary flow with the original forward evaluation and readout equation but clipped backward recursion

\[
 \delta_{a,M}^{(L)}=g_L(z_a^{(L)})\odot\chi_M(w),\qquad
 \delta_{a,M}^{(\ell)}=g_\ell(z_a^{(\ell)})\odot
 \chi_M((W^{(\ell+1)})^\top\delta_{a,M}^{(\ell+1)}).
\]

For each \(M>0\), choose a smooth scalar cutoff \(\chi_M\) that equals the identity on \([-M,M]\), is constant on each of the rays outside \([-2M,2M]\), satisfies \(|\chi_M(u)|\le\min\{|u|,2M\}\), and has \(|\chi_M'|\le1\). It acts coordinatewise, and the weight updates use the displayed clipped responses. Separately, replacing the cutoff by the identity in these equations recovers the unclipped dense flow.

Define the two-time normalized pairings

\[
 K_{ba,n}^{(\ell)}(s,t)=\frac{h_b^{(\ell)}(s)^\top h_a^{(\ell)}(t)}n,
 \qquad
 D_{ba,n}^{(\ell),M}(s,t)
 =\frac{\delta_{b,M}^{(\ell)}(s)^\top\delta_{a,M}^{(\ell)}(t)}n.
\]

Integration of the actual updates gives the following identities without approximation:

\[
\begin{aligned}
 z_a^{(1)}(t)
 &=W_0^{(1)}v_a-\frac2m\sum_bG_{ba}\int_0^t r_b(s)\delta_{b,M}^{(1)}(s)\,ds,\\
 w(t)&=-\frac2m\sum_b\int_0^t r_b(s)h_b^{(L)}(s)\,ds,\\
 z_a^{(\ell)}(t)
 &=W_0^{(\ell)}h_a^{(\ell-1)}(t)
 -\frac2m\sum_b\int_0^t r_b(s)\delta_{b,M}^{(\ell)}(s)
             K_{ba,n}^{(\ell-1)}(s,t)\,ds,\\
 (W^{(\ell+1)}(t))^\top\delta_{a,M}^{(\ell+1)}(t)
 &=(W_0^{(\ell+1)})^\top\delta_{a,M}^{(\ell+1)}(t)
 -\frac2m\sum_b\int_0^t r_b(s)h_b^{(\ell)}(s)
             D_{ba,n}^{(\ell+1),M}(s,t)\,ds.
\end{aligned}
\]

The third line applies to \(2\le\ell\le L\), and the fourth to \(1\le\ell<L\). These follow by substituting

\[
 W^{(\ell)}(t)=W_0^{(\ell)}
 -\frac2{mn}\sum_b\int_0^t r_b(s)
       \delta_{b,M}^{(\ell)}(s)h_b^{(\ell-1)}(s)^\top\,ds
\]

into a current forward or adjoint action. A passive input can replace the evaluated sample \(a\); only \(b\) indexes a driving training example.

The corresponding population histories replace the two normalized pairings by same-layer expectations. Their residuals and pairings are deterministic. One may therefore evaluate the population Euler program on finite initialized matrices with all its residuals and contractions frozen at their population values. This is the manuscript's oracle program. Its finite coordinates are dependent because each initialized matrix is reused in both orientations.

For clarity, on a fixed mesh define the oracle consistency discrepancies by

\[
\begin{aligned}
 \eta^K_{ba,n}(s,t)&=\frac{\widetilde h_b(s)^\top\widetilde h_a(t)}n
                    -\mathbb E[H_b(s)H_a(t)],\\
 \eta^D_{ba,n}(s,t)&=\frac{\widetilde\delta_b(s)^\top\widetilde\delta_a(t)}n
                    -\mathbb E[\Delta_b(s)\Delta_a(t)],\\
 \eta^f_{a,n}(t)&=\frac{\widetilde w(t)^\top\widetilde h_a^{(L)}(t)}n
                    -\mathbb E[w(t)H_a^{(L)}(t)].
\end{aligned}
\]

Each field and its population partner belong to the same layer and cap; those labels are suppressed only in this display. For example, reconstructing the oracle matrix from its vector histories changes its action on an oracle feature by the **exact** term

\[
 -\frac2m\sum_b\int_0^t r_{b,\infty}(s)
       \widetilde\delta_b(s)\eta^K_{ba,n}(s,t)\,ds,
\]

with the integral interpreted as the mesh sum for a discrete program. The adjoint discrepancy has the identical form with \(\widetilde h_b\eta^D\). Recomputed residuals additionally encounter \(\eta^f\).

Consequently, an empirical-measure law of large numbers supplies consistency but does not give its size. The required estimate must control these discrepancies, including their means, uniformly as the mesh is refined. The program length grows when the discretization error is driven below \(n^{-1/2}\).

For any one scalar oracle contraction \(A_n\) and its population target \(A\), the identity

\[
 \mathbb E|A_n-A|^2
 =\operatorname{Var}(A_n)+|\mathbb EA_n-A|^2
\]

makes the bias obligation explicit. Gaussian concentration for \(A_n-\mathbb EA_n\) alone does not establish an estimate against \(A\).

## 2. What the existing source does and does not imply

The fixed-program lemma in `paper/proof_alltime.tex` proves convergence by Gaussian conditioning. Its nonsingular-query argument inverts the finite query Grams. Its treatment of singular Grams adds independent noise of size \(\epsilon\), takes the width limit at fixed \(\epsilon\), then sends \(\epsilon\downarrow0\). Neither step supplies a quantitative constant uniform in query rank, the smallest nonzero query eigenvalue, or the number of instructions.

Clipping bounds the coordinate derivative of \(g(z)\chi_M(p)\) by a constant of order \(1+M\). That fact does not quantify the above Gaussian conditioning argument, nor make its constants uniform under mesh refinement. Thus even a statement of the form

\[
 \mathcal E_\mu(f_{n,M},f_{\infty,M})\le C_{\delta,M}/\sqrt n
\]

is an additional theorem, not a consequence already present in the source.

There is a second, separate issue. A bound with \(C_{\delta,M}\) growing like \(e^{CM}\), combined with \(M\asymp\sqrt{\log n}\), gives at best

\[
 n^{-1/2}\exp(C\sqrt{\log n})=n^{-1/2+o(1)}.
\]

This factor is unbounded and cannot be absorbed into a width-independent \(C_\delta\). Strict root width requires a stronger cap dependence or a comparison estimate that uses averaged carrier responses without replacing them by the deterministic cap.

The population response estimates in the source suggest how this could work: their derivative envelopes involve exponentials of activity-weighted carrier integrals, and the population Gaussian tails make those envelopes integrable. At finite width, however, the same estimate must be established jointly with the consistency errors. A population moment bound cannot be substituted for a finite-width joint moment bound.

## 3. Proved initialization theorem at every fixed depth

Let \(Q_n^{(\ell)}=H_\ell(0)^\top H_\ell(0)/n\) for any fixed finite list of inputs, and let \(Q^{(\ell)}\) be the deterministic covariance recursion in the manuscript. Under its assumptions that each activation has bounded derivative and Lipschitz derivative, for every fixed \(p\ge2\),

\[
 \bigl\|\|Q_n^{(\ell)}-Q^{(\ell)}\|_F\bigr\|_{L^p}
 \le C_{p,\ell}n^{-1/2}.
 \tag{1}
\]

In particular, both the fluctuation and the mean error are controlled at root width, even when intermediate covariance matrices are singular. If the activations are \(C^4\) with bounded derivatives of orders one through four, the stronger mean estimate holds:

\[
 \|\mathbb E Q_n^{(\ell)}-Q^{(\ell)}\|_F\le C_\ell/n.
 \tag{2}
\]

The stronger smoothness in (2) is additional; it is not part of the manuscript's main activation hypotheses.

**Proof.** For a positive semidefinite covariance \(Q\), define

\[
 T_\ell(Q)_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \qquad Z\sim N(0,Q).
\]

Gaussian interpolation, first for smooth activations and then by mollification, gives

\[
 \frac{d}{dt}T_\ell(P+t(Q-P))_{ab}
 =\frac12\sum_{ij}(Q-P)_{ij}\mathbb E[\partial_{ij}
            \{\phi_\ell(Z_a)\phi_\ell(Z_b)\}].
\]

One can verify the formula by writing the interpolated Gaussian as
\(\sqrt t\,X+\sqrt{1-t}\,Y\), with independent \(X\sim N(0,Q)\), \(Y\sim N(0,P)\), differentiating for \(0<t<1\), and integrating by parts in \(X,Y\). The resulting formula has no inverse covariance. The weak second derivatives exist because \(\phi'\) is Lipschitz. The bounds on \(\phi',\phi''\), and linear growth of \(\phi\), imply

\[
 \|T_\ell(Q)-T_\ell(P)\|_F
 \le C\bigl(1+\sqrt{\|Q\|_F}+\sqrt{\|P\|_F}\bigr)\|Q-P\|_F.
 \tag{3}
\]

All covariance moments of \(Q_n^{(\ell)}\) are bounded uniformly in \(n\). Indeed, Jensen bounds the \(k\)-th moment of an empirical diagonal covariance by a single row's \(2k\)-th feature moment; conditional Gaussian moments and linear activation growth bound this by a constant times \(1+(Q_n^{(\ell-1)})_{aa}^k\). Induction starts at the deterministic input covariance. The off-diagonal entries satisfy \(|Q_{ab}|\le\sqrt{Q_{aa}Q_{bb}}\).

Conditionally on the preceding layer, the next feature rows are independent. For an even integer \(p=2k\), expansion of the \(2k\)-th power of a centered sample average has no surviving term with an index appearing once. There are at most \(C_kn^k\) surviving index choices. Hölder bounds each such term by the single-row \(2k\)-th absolute moment. The preceding uniform covariance moments therefore give

\[
 \bigl\|\|Q_n^{(\ell)}-T_\ell(Q_n^{(\ell-1)})\|_F\bigr\|_{L^p}
 \le C_p/\sqrt n.
\]

Using (3) and Hölder yields

\[
 \bigl\|\|Q_n^{(\ell)}-Q^{(\ell)}\|_F\bigr\|_{L^p}
 \le C_p/\sqrt n
 +C_p\bigl\|\|Q_n^{(\ell-1)}-Q^{(\ell-1)}\|_F\bigr\|_{L^{2p}}.
\]

At each fixed depth, only finitely many higher moments are needed. The first layer has the sample-average estimate for every even moment, so induction proves (1); interpolation gives other finite \(p\).

For (2), differentiate the Gaussian interpolation formula once more. The fourth spatial derivatives of \(\phi(Z_a)\phi(Z_b)\) have an expectation bounded by \(C(1+\sqrt{\|Q\|_F})\). Taylor's formula around the deterministic \(Q^{(\ell-1)}\) therefore has a remainder bounded by

\[
 C\bigl(1+\sqrt{\|Q_n^{(\ell-1)}\|_F}+\sqrt{\|Q^{(\ell-1)}\|_F}\bigr)
       \|Q_n^{(\ell-1)}-Q^{(\ell-1)}\|_F^2.
\]

Its expectation is \(O(n^{-1})\), by the established fourth-moment estimate and the covariance moment bound. Conditional sampling noise has mean zero. Hence the mean error at layer \(\ell\) is a fixed linear transformation of the preceding mean error plus \(O(n^{-1})\). The first-layer mean error is zero. Induction proves (2). ∎

Since \(w(0)=0\), all hidden velocities vanish at initialization, and

\[
 \dot f_{n,a}(0)=\frac2m\sum_b y_b(Q_n^{(L)})_{ba}.
\]

Thus (1) controls the first prediction velocity of the full nonlinear dense network at root width for all fixed depths. It does not control later times.

## 4. Proved inverse-free coupling for one forward/adjoint reuse

Let \(W\in\mathbb R^{n\times n}\) have independent \(N(0,1/n)\) entries. Fix \(u\in\mathbb R^n\), independent of \(W\), and condition on \(u\). Put

\[
 q=\|u\|_2^2/n>0,\qquad z=Wu,\qquad p=W^\top\psi(z),
\]

where \(\psi\) acts coordinatewise. Let \(Z\sim N(0,q)\), and define

\[
 a(q)=\mathbb E[Z\psi(Z)]/q,\qquad b(q)=\mathbb E\psi(Z)^2.
\]

Assume the fourth moments appearing below are finite. If \(\psi\) is locally absolutely continuous and \(\psi,\psi'\) have at most polynomial growth (with the derivative interpreted almost everywhere), Gaussian integration by parts identifies \(a(q)=\mathbb E\psi'(Z)\); this is precisely the population response coefficient.

There is a coupling with \(g\sim N(0,I_n)\), independent of \(z,u\), under which

\[
 p=u A_n+\sqrt{B_n}\,P_{u^\perp}g,\qquad
 A_n=\frac1{nq}\sum_i z_i\psi(z_i),\qquad
 B_n=\frac1n\sum_i\psi(z_i)^2.
 \tag{4}
\]

Writing \(p_*=u a(q)+\sqrt{b(q)}g\), this coupling satisfies

\[
 \mathbb E\left[\frac{\|p-p_*\|_2^2}{n}\,\middle|\,u\right]
 \le\frac3n\left[
 \frac{\operatorname{Var}(Z\psi(Z))}{q}
 +\frac{\operatorname{Var}(\psi(Z)^2)}{b(q)}+b(q)\right].
 \tag{5}
\]

When \(b(q)=0\), both vectors are zero almost surely and the corresponding quotient is assigned zero. Moreover,

\[
 \mathbb E[p\mid u]=u a(q)
 \tag{6}
\]

exactly. If additionally \(\psi\in C^2(\mathbb R)\) and \(\psi,\psi',\psi''\) have at most polynomial growth, the exact second-moment identity is

\[
 \mathbb E[p_i p_j\mid u]
 =\delta_{ij}b(q)+u_i u_j\left[
 a(q)^2+\frac{\mathbb E[(\psi^2)''(Z)]-a(q)^2}{n}\right].
 \tag{7}
\]

**Proof.** Gaussian orthogonal decomposition of each row gives

\[
 W=\frac{zu^\top}{nq}+\widetilde W P_{u^\perp},
\]

where \(z\) has independent \(N(0,q)\) entries and \(\widetilde W\) is an independent copy of \(W\). Conditional on \(z\), the vector \(\widetilde W^\top\psi(z)\) is Gaussian with covariance \(B_n I_n\). This proves (4) in joint law. It introduces no inverse query Gram.

Subtract \(p_*\) in (4):

\[
 p-p_*=u(A_n-a)+(\sqrt{B_n}-\sqrt b)g-\sqrt{B_n}P_u g.
\]

The square of the norm of a sum of three vectors is at most three times the sum of their squared norms. The three expected normalized squares are, respectively,

\[
 \frac{\operatorname{Var}(Z\psi(Z))}{nq},\qquad
 \mathbb E(\sqrt{B_n}-\sqrt b)^2
 \le\frac{\operatorname{Var}(\psi(Z)^2)}{nb},\qquad
 \frac b n.
\]

The middle bound uses \(|\sqrt x-\sqrt b|\le|x-b|/\sqrt b\), and the last uses that \(P_u\) has rank one. This proves (5). Taking the mean proves (6).

Taking conditional second moments in (4) gives

\[
 \mathbb E[p_i p_j\mid u]
 =\delta_{ij}b+u_i u_j\left[a^2+\frac1n
 \left(\frac{\mathbb E[Z^2\psi(Z)^2]}{q^2}-\frac bq-a^2\right)\right].
\]

Twice integrating by parts under the stated \(C^2\) and growth assumptions gives

\[
 \mathbb E[Z^2\psi(Z)^2]-q\mathbb E\psi(Z)^2
 =q^2\mathbb E[(\psi^2)''(Z)],
\]

which proves (7). The preceding display for the second moment in terms of \(\mathbb E[Z^2\psi(Z)^2]\) remains valid without classical second derivatives. ∎

If \(\psi\) has global Lipschitz constant \(K\), (5) is bounded by

\[
 \frac{C}{n}\bigl(|\psi(0)|^2+K^2q\bigr).
 \tag{8}
\]

Here is the only variance inequality needed for this simplification. For an absolutely continuous \(F\) of a standard Gaussian \(G\),

\[
 \operatorname{Var}(F(G))\le\mathbb E|F'(G)|^2.
\]

To verify it, take an independent \(G'\), differentiate
\(\mathbb E[F(G)F(\sqrt tG+\sqrt{1-t}G')]\), and integrate by parts in both Gaussians. The derivative is
\(\mathbb E[F'(G)F'(\sqrt tG+\sqrt{1-t}G')]/(2\sqrt t)\).
Cauchy–Schwarz bounds it in absolute value by
\(\mathbb E|F'(G)|^2/(2\sqrt t)\); integration from zero to one gives the inequality. Truncation and smooth approximation extend the calculation to square-integrable weak derivatives.

Apply it to \(F(G)=\psi(\sqrt qG)^2\) to obtain
\(\operatorname{Var}(\psi(Z)^2)\le4qK^2b\).
Also \(\mathbb E[G^2\psi(\sqrt qG)^2]\le2|\psi(0)|^2+6K^2q\), which bounds the first quotient in (5); linear growth bounds \(b\). This proves (8). When \(q=0\), \(u=0\) and \(p=W^\top\psi(0)\boldsymbol1\) is exactly an independent Gaussian vector of variance \(\psi(0)^2\), so the degenerate case can be coupled with zero error.

The constants in (5) are uniform over a family of caps whenever its displayed moment ratios are uniform. More concretely, for bounded \(\phi\), bounded \(\phi'\), Lipschitz \(\phi'\), and a fixed scalar \(\alpha\),

\[
 \psi_M(z)=\phi'(z)\chi_M(\alpha\phi(z))
\]

has Lipschitz constant at most
\(|\alpha|(\|\phi''\|_\infty\|\phi\|_\infty+\|\phi'\|_\infty^2)\), independently of \(M\). Indeed, differentiate the product and use \(|\chi_M(\alpha\phi)|\le|\alpha\phi|\) and \(|\chi'_M|\le1\). Its value at zero has a uniform bound as well. Equation (8) is therefore cap-independent for this one-return calculation.

## 5. Application to the first nonlinear dense backward response

Consider one nonzero training input, two hidden layers, zero readout, and tanh in both layers. Let \(a=W_0^{(1)}v\), \(h=\tanh(a)\), \(z=W_0^{(2)}h\), and set

\[
 \psi(z)=\tanh(z)\operatorname{sech}^2(z),\qquad
 T=(W_0^{(2)})^\top\psi(z).
\]

The canonical flow has

\[
 \dot w(0)=2y\tanh(z),\qquad
 \dot\delta^{(2)}(0)=2y\psi(z),\qquad
 \left.\frac d{dt}\bigl((W^{(2)})^\top\delta^{(2)}\bigr)\right|_{t=0}
 =2yT.
\]

The last identity uses \(\delta^{(2)}(0)=0\) and \(\dot W^{(2)}(0)=0\). Thus \(T\) is a genuine dense backward response, and its population correction \(h\,a(q)\) cannot be dropped.

Here \(|\psi|\le1\), \(|\psi'|\le3\), \(\psi(0)=0\), and \(q=\|h\|^2/n\le1\). The theorem gives a coupling with expected normalized squared error \(C/n\), uniformly in the realized first layer.

It can also be compared to the deterministic population coefficients. Let
\(q_\infty=\mathbb E\tanh(A)^2>0\), where \(A\sim N(0,\|v\|^2)\). The first-layer entries are independent, so
\(\mathbb E|q-q_\infty|^2\le C/n\).
For this fixed tanh function, Gaussian differentiation gives bounded derivatives of \(a(q)=\mathbb E\psi'(\sqrt qG)\) and \(b(q)=\mathbb E\psi(\sqrt qG)^2\) on \([0,1]\): they are half the expectations of \(\psi'''\) and \((\psi^2)''\), respectively. These derivatives are bounded functions. Since \(b(q_\infty)>0\),

\[
 |\sqrt{b(q)}-\sqrt{b(q_\infty)}|
 \le\frac{|b(q)-b(q_\infty)|}{\sqrt{b(q_\infty)}}.
\]

Using the same independent \(g\) as above therefore gives

\[
 \mathbb E\frac1n\sum_i
 \left|T_i-h_i a(q_\infty)-\sqrt{b(q_\infty)}g_i\right|^2
 \le C/n.
 \tag{9}
\]

The pairs \((h_i,g_i)\) are independent and identically distributed. Thus (9), followed by the elementary variance estimate for their sample averages, also gives a root-width comparison of any fixed Lipschitz empirical observable of \((h_i,T_i)\) against its population expectation. This comparison controls the mean as well as fluctuations. Equation (7) supplies an explicit \(1/n\) conditional bias for quadratic return observables.

This is a quantitative calculation inside a nonlinear dense two-layer network. It addresses only its initial nonzero backward response, not an interval of training.

## 6. Smallest missing estimate and why the one-return proof does not iterate automatically

The one-return proof depends on the query input \(u\) being independent of the matrix being queried. After training starts, the next input depends on earlier forward and adjoint outputs of that same matrix. Conditioning on all those answers removes a subspace whose dimension can grow with the number of calls. Applying the one-return bound separately and adding its rank-one projection costs gives a constant growing with program length. Taking a vanishing time mesh then destroys the claimed uniform root-width bound.

A sufficient new probabilistic theorem would control the oracle contraction errors \(\eta^K,\eta^D,\eta^f\) jointly with the response propagators generated by their own matrix history. Its constants must be uniform in mesh refinement, and either uniform in \(M\) or strong enough for \(M\asymp\sqrt{\log n}\). It must bound signed expectations or mean square errors against the population contractions, not merely variances around finite-width expectations.

The most economical form need not control the supremum over every pair of history times. The exact history identities show that activity-weighted contractions, multiplied by their future response propagators, suffice. Schematically, if \(R_n(t,s)\) denotes the derivative of the finite oracle evolution with respect to a source inserted at time \(s\), one needs estimates of the form

\[
 \mathbb E\left|\int_0^t R_n(t,s)\,\eta_n(s,t)\,
                         \rho_\infty(s)\,ds\right|^2\le C/n,
\]

uniformly in \(t\), mesh and cap, together with the corresponding prediction consistency estimate. This display identifies an estimate to prove; it is **not** a bound established here. In particular, multiplying a population response moment by a separately proved concentration bound is invalid without controlling their finite-width dependence.

One way to obtain it could be a cavity estimate in which deleting one row and column changes these history-weighted observables by \(O(n^{-1/2})\) in mean square, with summable activity weights, and a Gaussian integration-by-parts estimate identifies the resulting expectation with the population response. Such an argument must account for repeated reuse of every affected matrix. The explicit \(1/n\) term in (7) demonstrates the kind of finite-width response correction it must sum.

Neither a complete version of this repeated-query estimate nor a counterexample to it was obtained. The auxiliary clipping route therefore remains incomplete at its finite-to-population comparison step. The initial quantitative bounds and the exact first-return calculation above do not justify a strict all-time root-width claim.
