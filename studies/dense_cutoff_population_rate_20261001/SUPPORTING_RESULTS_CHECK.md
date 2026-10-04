# Internal check of the probability and first-feedback supporting results

Date: 2026-10-01. **Verdict: PASS for the mathematical statements actually
claimed in the three final snapshots below.** This is an internal
reconstruction check, not a promotion review. The all-time dense
root-width target remains unproved, as the notes correctly state.

## 1. Scope, complete-read coverage and input identity

The assigned scientific inputs were the complete three notes listed below
and the previously allowed manuscript setting, results, all-time proof and
tracking proof. The notation and rigorous-math skills were applied. No other
study, prior review or unassigned scientific source was read. Candidate
files were not edited by this checker.

Every line of each final snapshot was read. The first-feedback file was
unchanged from its complete initial read; the other two files were reread
completely after the corrections recorded in Section 7.

| Input | Complete coverage | Final SHA-256 |
|---|---:|---|
| THREE_ERROR_REASSEMBLY.md | lines 1–169 | b66b678ea0a568fa134341b82c2fd69cdaf2c98e54611a42e87c74a1bcb7ee7f |
| FIRST_FEEDBACK.md | lines 1–163 | 1227ad78d2b983054aaebc4fa72db8fa790e114d935f11eb5d2b0997dadb199b |
| WIDTH_ROUTE.md | lines 1–379 | c8f8e27dd11ac98d0955e6ecc7d59c4eb346642b601ca63e6c4159413de6444e |

The verdicts below bind these contents, not later revisions.

## 2. Conditional finite-tail transfer

Let \(\mathcal G_n\) be the fitting event,
\(\rho_n(t)\le Ye^{-\kappa t}\) on that event, and let \(H_n(M,t)\)
and \(Z_n(M)\) have the definitions in THREE_ERROR_REASSEMBLY.
Quantities on \(\mathcal G_n^c\) may be assigned zero wherever the
event indicator occurs; no existence claim outside that event is needed.
The additional premise is the actual finite-network estimate

\[
 \mathbb E[\mathbf1_{\mathcal G_n}
              e^{b|p_{n,a,i}^{(\ell)}(t)|^2}]\le B
\]

uniformly in all indices, width and time. This is an assumption of the
proposition, not a consequence of population carrier tails.

The maximum of \(x e^{-bx/2}\), for \(x\ge0\), is \(2/(be)\).
Consequently

\[
 v^2\mathbf1_{\{|v|>M\}}
    \le \frac{2}{be}e^{-bM^2/2}e^{bv^2}.
\]

For
\(A_{\ell a}=n^{-1}\sum_i|p_{n,a,i}^{(\ell)}|^2
\mathbf1_{\{|p_{n,a,i}^{(\ell)}|>M\}}\),

\[
 H_n^2
  =\left(\sum_\ell\max_a\sqrt{A_{\ell a}}\right)^2
  \le L\sum_\ell\max_a A_{\ell a}
  \le L\sum_{\ell,a}A_{\ell a}.
\]

The sample/layer factor and normalization by width are therefore
correct. Taking expectations gives
\(\mathbb E[\mathbf1_{\mathcal G_n}H_n^2]\le Ce^{-bM^2/2}\).
The deterministic measure \(d\nu(t)=Ye^{-\kappa t}\,dt\) has mass
\(Y/\kappa\), so

\[
 Z_n(M)^2
 \le\left(\int\mathbf1_{\mathcal G_n}H_n\,d\nu\right)^2
 \le \frac{Y}{\kappa}
       \int\mathbf1_{\mathcal G_n}H_n^2\,d\nu.
\]

Tonelli proves
\(\mathbb E Z_n(M)^2\le C Y^2\kappa^{-2}e^{-bM^2/2}\).
Neither neuron independence nor temporal independence was used.
The deterministic fitting envelope supplies the integrable measure;
an unweighted infinite-time integration would be invalid.

Using the deterministic comparison
\(\mathbf1_{\mathcal G_n}\mathcal E_\mu(f_n,f_{n,M})
\le C_\mu e^{KM}Z_n(M)\) now gives

\[
 \mathbb E[\mathbf1_{\mathcal G_n}
             \mathcal E_\mu(f_n,f_{n,M})^2]
 \le C_\mu e^{2KM-bM^2/2}
 \le C_\mu' e^{-bM^2/4}.
\]

The last constant is uniform in \(M\), by maximizing
\(2KM-bM^2/4\). Choose \(M=A\sqrt{\log(e+n)}\) with
\(bA^2/4\ge1\). The resulting second moment is at most \(C_\mu'/n\).
Markov at level \(\sqrt{C_\mu'/(\delta n)}\) gives the stated
probability inequality on the fitting event. A full-confidence claim
must additionally include \(\Pr(\mathcal G_n^c)\); the note correctly
retains \(\mathcal G_n\) in its displayed event.

For the fixed-\(2p\)-moment variant, use instead

\[
 |v|^2\mathbf1_{\{|v|>M\}}\le M^{-(2p-2)}|v|^{2p}.
\]

This gives precisely \(M^{-2p+2}\). At a square-root-log cap it is
only an inverse power of \(\log n\), so it does not prove the required
root-width removal estimate through this stability bound.

The three-error triangle inequality passes by the triangle inequality
for the time supremum followed by Minkowski in \(L^2(\mu)\).
The telescoping criterion also passes: summable bounds for the full
population-centered correction errors imply a convergent series in
the stated mean-square trajectory norm. Cutoff-limit convergence
identifies its sum with the original error. Variance-only bounds do
not meet this criterion because they omit the population bias.

**Verdict: PASS as conditional propositions and a conditional
telescoping criterion.** General finite-network exponential moments
and the clipped dense width bound are still assumptions to prove.

## 3. Exact first nonlinear feedback derivative

In FIRST_FEEDBACK there is one sample, two hidden tanh layers and
\(\|v\|_2=1\). At initialization write
\(h=\tanh(a)\), \(s=\operatorname{sech}^2(a)\),
\(z=Wh\), \(g=\tanh(z)\),
\(\psi(z)=g\odot\operatorname{sech}^2(z)\), and
\(T=W^\top\psi(z)\). All derivatives in this section are at time zero.

Zero readout gives zero hidden velocities. The unhalved squared loss
and canonical mobilities give

\[
 w'=2yg,\qquad r'=2yQ_n,\qquad
 w''=-4yQ_ng,\qquad r''=-4yQ_n^2.
\]

The true backward responses satisfy
\(\delta^{(2)\prime}=2y\psi(z)\) and
\(\delta^{(1)\prime}=2y\,s\odot T\). Differentiating the weight
updates therefore gives

\[
 W^{(1)\prime\prime}=4y^2(s\odot T)v^\top,\qquad
 W^{(2)\prime\prime}=\frac{4y^2}{n}\psi(z)h^\top.
\]

The input normalization is used in
\(a''=W^{(1)\prime\prime}v=4y^2s\odot T\). Consequently

\[
 h''=4y^2s^2\odot T,\qquad
 z''=4y^2\{q_n\psi(z)+W(s^2\odot T)\},
\]

\[
 \frac{g^\top g''}{n}
 =\frac{\psi(z)^\top z''}{n}
 =4y^2\left(q_n B_n+
          \frac{\psi(z)^\top W(s^2\odot T)}n\right)
 =4y^2(q_nB_n+D_n).
\]

Finally
\(w'''=-2(r''g+2r'g'+rg'')=8yQ_n^2g+2yg''\), and

\[
 f'''(0)
 =\frac{w'''{}^\top g+3w'{}^\top g''}{n}
 =8yQ_n^3+8y\,\frac{g^\top g''}{n}
 =8yQ_n^3+32y^3(q_nB_n+D_n).
\]

The coefficient \(32\), powers of \(y\), signs and factors \(1/n\)
are correct. The calculation also holds at \(n=1\), and gives zero
when \(y=0\). It concerns derivatives of the finite ODE and makes no
exchange of width limits with time differentiation.

## 4. Returned energy: conditional mean, bias and variance

Condition on \(a\). A Gaussian row \(W_j\) has covariance \(I/n\),
and \(\operatorname{Cov}(W_{ji},z_j)=h_i/n\). With the definitions
of \(\alpha,\beta,\gamma\) in FIRST_FEEDBACK, one and two Gaussian
integrations by parts give

\[
 \mathbb E[W_{ji}\psi(z_j)\mid a]
       =\frac{h_i}{n}\alpha(q_n),\qquad
 \mathbb E[W_{ji}^2\psi(z_j)^2\mid a]
       =\frac{\beta(q_n)}n+\frac{h_i^2}{n^2}\gamma(q_n).
\]

All tanh-derived functions and derivatives used here are bounded.
Thus their Gaussian integration-by-parts hypotheses hold.
There are \(n\) diagonal row products and \(n(n-1)\) off-diagonal
products in \(T_i^2\). Conditional row independence gives exactly

\[
 \mathbb E[T_i^2\mid a]
 =\beta(q_n)+h_i^2
       \left[\alpha(q_n)^2+
             \frac{\gamma(q_n)-\alpha(q_n)^2}{n}\right].
\]

Multiplying by \(s_i^2/n\) and summing proves the stated conditional
mean of \(D_n\). In particular, the mean response
\(h_i\alpha(q_n)\) belongs to the population and cannot be omitted.

The empirical triple \((q_n,S_n,U_n)\) averages bounded independent
tuples, has exactly the stated deterministic mean, and has covariance
\(O(n^{-1})\). Gaussian differentiation gives

\[
 \frac d{dq}\mathbb E F(\sqrt q A)
       =\frac12\mathbb E F''(\sqrt q A),
\]

with a right-continuous extension at \(q=0\) for the functions at hand.
Their needed derivatives are bounded. The function
\(\beta(q)S+\alpha(q)^2U\) therefore has bounded Hessian on
the cube containing the empirical triples. The expectation of its
linear Taylor term vanishes, and its quadratic remainder is \(O(n^{-1})\).
The explicit \(1/n\) term is uniformly \(O(n^{-1})\). This proves
the claimed bias and the \(O(n^{-1})\) variance of the conditional mean.

For the remaining variance, write \(W=G/\sqrt n\), where \(G\) is
standard Gaussian, and set \(u=s^2\odot T\). Conditional on \(a\),
direct differentiation gives

\[
 \nabla_GD_n=\frac{2}{n\sqrt n}
   \{\psi(z)u^\top+\operatorname{diag}(\psi'(z))Wu h^\top\}.
\]

Using \(\|h\|_2\le\sqrt n\), \(\|\psi(z)\|_2\le C\sqrt n\),
\(\|u\|_2\le\|T\|_2\), and
\(\|T\|_2\le C\sqrt n\|W\|_{\rm op}\), one obtains

\[
 \|\nabla_GD_n\|_F^2
 \le\frac C{n^2}(1+\|W\|_{\rm op}^2)\|T\|_2^2
 \le\frac Cn(\|W\|_{\rm op}^2+\|W\|_{\rm op}^4).
\]

This verifies the Gaussian normalization: differentiation with
respect to \(W\), omitting the \(1/\sqrt n\), would lose the rate.

For independent Gaussian copies \(G,G'\), set
\(G_t=\sqrt tG+\sqrt{1-t}G'\). Gaussian integration by parts gives

\[
 \frac d{dt}\mathbb E[F(G)F(G_t)]
 =\frac1{2\sqrt t}\mathbb E
          \langle\nabla F(G),\nabla F(G_t)\rangle.
\]

Integration and Cauchy--Schwarz imply
\(\operatorname{Var}F(G)\le\mathbb E\|\nabla F(G)\|_2^2\), since
\(\int_0^1(2\sqrt t)^{-1}dt=1\). Smooth truncation is valid here:
the gradients have polynomial growth in finite-dimensional Gaussian
variables. Integrating the manuscript's sphere-net operator tail
above a sufficiently large fixed threshold gives uniform second and
fourth moments of \(\|W\|_{\rm op}\). Thus the expected conditional
variance of \(D_n\) is \(O(n^{-1})\).

Conditional on \(a\), the quantities \(Q_n,B_n\) are averages of
bounded independent row functions. Their conditional variances are
\(O(n^{-1})\). Expanding \(Q_n^3\) around its conditional mean gives
a conditional bias \(O(n^{-1})\); the third centered moment is bounded
by a constant times the variance because the variables are bounded.
The conditional mean of \(q_nB_n\) is exactly \(q_n\beta(q_n)\).
The same bounded-derivative Taylor estimate in \(q_n\) gives
\(O(n^{-1})\) unconditional biases and variances for both terms.
Their dependence on \(D_n\) is harmless when combining finitely many
errors by Cauchy--Schwarz.

**Verdict for FIRST_FEEDBACK: PASS.** It proves
\(|\mathbb Ef_n'''(0)-J_*|\le C_y/n\) and
\(\mathbb E|f_n'''(0)-J_*|^2\le C_y/n\), with the stated
normalizations, without identifying \(J_*\) by differentiating a
global population convergence theorem.

## 5. Exact history and initialization estimates in WIDTH_ROUTE

Integrating a hidden update gives
\(-2(mn)^{-1}\int r_b\delta_bh_b^\top\).
Multiplication by a current forward feature gives its normalized
feature pairing. Its transpose action gives the normalized backward
pairing. This verifies all signs, factors of two, sample factors and
width factors in the two history identities. The first-layer identity
uses \(v_b^\top v_a\); the readout weight update has no \(1/n\).
The displayed oracle errors are exactly these pairing discrepancies
multiplied by the residual and response histories.

At initialization, conditional Gaussian rows are independent with
covariance equal to the preceding empirical covariance. For the map
\(T(Q)_{ab}=\mathbb E[\phi(Z_a)\phi(Z_b)]\), Gaussian interpolation
along a positive semidefinite segment gives, for smooth activations,

\[
 \frac d{dt}T(P+t(Q-P))_{ab}
 =\frac12\sum_{ij}(Q-P)_{ij}
       \mathbb E\partial_{ij}\{\phi(Z_a)\phi(Z_b)\}.
\]

Bounded \(\phi'\), bounded weak \(\phi''\), and linear growth of
\(\phi\) bound the integrated derivative by

\[
 C(1+\sqrt{\|P\|_F}+\sqrt{\|Q\|_F})\|Q-P\|_F.
\]

For \(C^{1,1}\) activations, mollification passes this integrated
inequality to the limit. One need not evaluate a weak second
derivative at an exceptional point of a degenerate Gaussian. The
inequality uses no inverse covariance and remains valid at singular
covariances.

Linear activation growth and conditional Gaussian moments propagate
every fixed covariance moment. In the \(2k\)-th moment expansion of a
centered empirical average, an index appearing once has zero conditional
expectation. At most \(k\) distinct indices survive, yielding at most
\(C_kn^k\) grouped terms against normalization \(n^{2k}\).
Hölder bounds each by the single-row \(2k\)-th moment. This gives
the \(L^{2k}\) sampling error \(C_k/\sqrt n\). The covariance-map
estimate and Hölder require moment \(2p\) at the preceding layer
to control moment \(p\) at the current layer. Fixed depth involves
only finitely many doublings, so all claimed fixed-\(p\) estimates follow.

With bounded derivatives through order four, the second covariance
derivative is bounded by \(C(1+\sqrt{\|Q\|_F})\). Taylor expansion
around the deterministic preceding covariance has expected remainder
\(O(n^{-1})\) by the fourth-moment error estimate. Conditional sampling
noise has mean zero, and first-layer mean error is zero. The resulting
linear recursion proves the stronger \(O(n^{-1})\) mean error.
The note explicitly labels the additional activation regularity.

**Verdict: PASS for the exact history identities and both initialization
estimates.** The derivative
\(\dot f_a(0)=2m^{-1}\sum_b y_b(Q_n^{(L)})_{ba}\) has the claimed
root-width error, but this is not a statement about later times.

## 6. One-return coupling and cap-uniform constants

Condition on \(u\), independent of \(W\), and set
\(q=\|u\|_2^2/n>0\). Rowwise Gaussian projection gives

\[
 W=\frac{zu^\top}{nq}+\widetilde W P_{u^\perp},
\]

where \(\widetilde W\) is independent of \(z\).
Conditional on \(z\), its returned vector has covariance \(B_nI_n\).
This gives the exact joint-law coupling

\[
 p=uA_n+\sqrt{B_n}P_{u^\perp}g,\quad
 A_n=\frac1{nq}\sum_jz_j\psi(z_j),\quad
 B_n=\frac1n\sum_j\psi(z_j)^2,
\]

with \(g\) independent of \(z,u\). It also gives the exact
conditional mean \(ua(q)\).

After subtracting \(p_*=ua(q)+\sqrt{b(q)}g\), the three normalized
expected squared terms in the note are

\[
 \frac{\operatorname{Var}(Z\psi(Z))}{nq},\qquad
 \mathbb E(\sqrt{B_n}-\sqrt b)^2
       \le\frac{\operatorname{Var}(\psi(Z)^2)}{nb},\qquad
 \frac bn.
\]

The third term is the rank-one projection cost. Multiplication of
their sum by three proves the coupling bound. When \(b=0\),
\(\psi(Z)=0\) almost surely and both vectors vanish. When \(q=0\),
\(u=0\) and \(W^\top\psi(0)\boldsymbol1\) already has independent
Gaussian coordinates of variance \(\psi(0)^2\). Both degeneracies
are therefore correctly handled.

For a \(K\)-Lipschitz \(\psi\), Gaussian Poincaré gives

\[
 \operatorname{Var}(\psi(Z)^2)\le4qK^2b,\qquad
 \operatorname{Var}(Z\psi(Z))/q
 \le\mathbb E[G^2\psi(\sqrt qG)^2]
 \le2|\psi(0)|^2+6K^2q.
\]

Together with \(b\le2|\psi(0)|^2+2K^2q\), these inequalities
prove the claimed uniform bound, including as \(q\downarrow0\).

The conditional second moment calculated directly from the coupling is

\[
 \mathbb E[p_ip_j\mid u]
 =\delta_{ij}b+
 u_i u_j\left[a^2+\frac1n
     \left(\frac{\mathbb E[Z^2\psi(Z)^2]}{q^2}
                  -\frac bq-a^2\right)\right].
\]

Under the final snapshot's explicit \(C^2\) and polynomial-growth
assumptions, twice Gaussian integration by parts gives
\(\mathbb E[Z^2F(Z)]=q\mathbb EF(Z)+q^2\mathbb EF''(Z)\).
For \(F=\psi^2\) this gives exactly the note's second-moment formula.
The correction is entrywise proportional to \(u_i u_j/n\);
the note does not claim the unnormalized covariance operator error
is \(O(n^{-1})\) for arbitrary \(u\).

For the bounded-activation clipped example,
\(\psi_M(z)=\phi'(z)\chi_M(\alpha\phi(z))\), a.e. differentiation gives

\[
 |\psi_M'(z)|\le|\alpha|
   \{\operatorname{Lip}(\phi')\|\phi\|_\infty
                                  +\|\phi'\|_\infty^2\}.
\]

Here magnitude contraction, rather than the cap size, bounds the
first term. The value at zero also has a cap-independent bound.
Thus the one-return constant is uniform in \(M\) for this
explicitly bounded-activation application. The argument is not
silently extended to unbounded activation values.

For two tanh layers, the returned \(T\) is exactly the first
nonzero dense carrier derivative divided by \(2y\), when \(y\ne0\).
The derivative identity itself remains valid at \(y=0\).
The empirical first-layer \(q\) has mean-square error \(O(n^{-1})\).
Smooth tanh-derived functions give bounded derivatives of \(a(q)\)
and \(b(q)\); \(b(q_\infty)>0\). Using the same independent
\(g\) replaces random coefficients by deterministic ones with
another \(O(n^{-1})\) normalized mean-square cost. The independent
pairs \((h_i,g_i)\), coupling and the sample-average variance estimate
then prove the stated Lipschitz empirical-observable conclusion.

**Verdict: PASS for the one-return coupling, its mean and second moment,
the cap-uniform bounded-activation application, and the tanh application.**

## 7. Corrections checked in the final snapshots

The initial THREE_ERROR snapshot had two missing backslashes before
the left delimiter command in displayed expectations. Both are fixed.

The initial WIDTH snapshot defined only identity on \([-M,M]\),
magnitude contraction and \(|\chi_M'|\le1\), then claimed an
\(O(1+M)\) coordinate Lipschitz bound. Those three properties alone
would permit \(\chi_M(u)=u\), so the local implication was not valid
under that incomplete definition. The final snapshot explicitly adds
saturation outside \([-2M,2M]\) and \(|\chi_M|\le2M\), resolving
the issue without changing either main theorem.

The generic twice-integration-by-parts formula initially said only
“sufficiently smooth.” The final snapshot requires \(C^2\) and
polynomial growth of \(\psi,\psi',\psi''\), which suffices for
the displayed Gaussian expectations and integrations by parts.
The tanh application already met these hypotheses.

Malformed inline delimiters and the malformed inline second-moment
integration-by-parts identity in WIDTH were repaired. The latter now
appears as an explicit display. The final full reads checked these
repairs against the formulas reconstructed above. No remaining
mathematical correction is required for the stated claims.

## 8. Target-level conclusion

The supporting results establish quantitative initialization control
and one nonlinear forward/adjoint return, including its finite
expectation bias. The conditional probability lemma identifies
sufficient finite marginal tails for cutoff removal without a
neuron/time maximum.

They do not establish the finite-network exponential moments throughout
training, a repeated-query concentration and bias estimate uniform in
mesh refinement, or an all-time clipped finite-to-population bound
with adequate cap dependence. The strict all-time dense root-width
target is therefore **NOT PROVED** by these notes. This is a limitation
correctly disclosed by the candidates, not a failed claim they make.
None proves a contrary lower bound or substitutes fluctuation around
a finite-width mean for population-centered error.
