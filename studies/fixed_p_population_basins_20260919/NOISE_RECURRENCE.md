# Fixed Gaussian perturbations: recurrence and convergence criteria

This is a scoped, independent theoretical note. Its scientific inputs are only the supervisor's stated Hilbert-space model. No population representation formula, covariance formula, or established result about the particular closure was supplied. Consequently, the abstract criteria below are proved, but their hypotheses are not asserted for that closure.

The main positive result is that cumulative conditional chances of a sufficiently good proposal, rather than compactness itself, are what the argument needs. Useful sufficient conditions include recurrence with a uniform chance of success, tightness of the distributions of trial states, compact linear observations, and robust rescue perturbations whose Gaussian cost grows slowly enough. Norm boundedness and weak compactness alone do not provide a uniform chance of success. The counterexample to that last implication does **not** by itself disprove convergence of the original accept/reject chain.

## 1. Exact algorithm and scope

Let \(H\) be a separable real Hilbert space, let \(L:H\to[0,\infty)\) be continuous, and write \(m=\inf_H L\). Let \(Q\) be positive, injective, and trace class. The actual perturbation law is
\[
\mu=N(0,\Sigma),\qquad \Sigma=\sigma^2Q,\quad \sigma>0.
\]
Injectivity implies that every nonempty norm-open ball has positive \(\mu\)-measure: approximate its center by finitely many covariance eigenvectors, require those Gaussian coordinates to lie in suitable finite intervals, and require the independent tail to have small norm. The latter event has positive probability by first taking sufficiently many coordinates that the tail's expected squared norm is small.

Let \(X_n\) be the incumbent. Before drawing perturbation \(Z_n\sim\mu\), permit a measurable state \(Y_n\) determined by the past, with
\[
L(Y_n)\le L(X_n).
\]
For the unmodified random-search rule, \(Y_n=X_n\). For the optional flow step, \(Y_n=\Phi_\tau(X_n)\), provided that this gradient flow exists for the prescribed duration and decreases the loss. Set
\[
X_{n+1}=\begin{cases}
Y_n+Z_n,&L(Y_n+Z_n)<L(Y_n),\\
Y_n,&\text{otherwise}.
\end{cases}
\]
The \(Z_n\) are independent of the past and of each other. Thus \(V_n=L(X_n)\) decreases to a random limit \(V_\infty\ge m\).

All criteria in Sections 2–6 concern this same additive, fixed-covariance proposal rule. Section 7 explicitly changes it.

## 2. The exact conditional-probability criterion

For \(a>m\), define the open nonempty sublevel set and its proposal probability by
\[
A_a=\{x:L(x)<a\},\qquad
p_a(x)=\mu(A_a-x),\qquad p_n(a)=p_a(Y_n).
\]
Continuity and full support give \(p_a(x)>0\) for every fixed \(x\). No minimizer need exist.

**Proposition 1.** Suppose, for each rational \(a>m\), that
\[
\sum_{n=0}^\infty p_n(a)=\infty
\quad\text{on the event }\{V_\infty\ge a\}.
\tag{1}
\]
Then \(V_n\to m\) almost surely.

Here and below a pathwise condition on an event means that it holds almost surely on that event. A directly checkable version of (1) is: every realized path that has not yet crossed the level \(a\) accumulates infinite conditional proposal probability if continued forever without crossing it.

**Proof.** We use the following elementary conditional Borel–Cantelli argument. Let \(E_n\) be an event revealed after trial \(n\), and let \(q_n=\mathbb P(E_n\mid\mathcal F_n)\), where \(\mathcal F_n\) is the information before that trial. For any fixed starting index \(k\),
\[
W_N=\mathbf1_{\cap_{n=k}^{N-1}E_n^c}
\exp\!\left(\sum_{n=k}^{N-1}q_n\right)
\]
is a nonnegative supermartingale: its conditional multiplier is \(e^{q_n}(1-q_n)\le1\). Hence \(\mathbb E W_N\le1\). If no \(E_n\) occurs after \(k\), but \(\sum_{n\ge k}q_n=\infty\), then \(W_N\to\infty\); Fatou's lemma makes that event null. Taking the union over \(k\) proves that infinite cumulative conditional probability forces infinitely many occurrences.

Apply this to \(E_n=\{L(Y_n+Z_n)<a\}\), whose conditional probability is \(p_n(a)\). On \(\{V_\infty\ge a\}\), every preproposal loss is at least \(a\): otherwise monotonicity would already put the limit below \(a\). An occurrence of \(E_n\) is therefore accepted and puts \(V_{n+1}<a\), a contradiction. Condition (1) makes \(\mathbb P(V_\infty\ge a)=0\). Countably many rational levels imply \(V_\infty=m\). ∎

This criterion does not assert that merely positive probabilities have divergent sum. That is the precise missing implication in an unrestricted full-support argument.

Two convenient consequences are:

* **Recurrent uniform success.** For each relevant \(a\), suppose there is a deterministic set \(C_a\) and \(c_a>0\) with \(p_a(x)\ge c_a\) on \(C_a\). If \(Y_n\in C_a\) infinitely often whenever the loss remains above \(a\), then convergence follows. The entire trajectory need not be precompact, or even bounded.
* **Repeated fixed progress.** One may instead show that, whenever the loss stays at least \(m+\varepsilon\), the cumulative conditional probability of a loss decrease of at least some fixed \(\delta_\varepsilon>0\) diverges. The same lemma gives infinitely many such decreases, contradicting the finite initial loss. This version is useful when a uniform descent construction is easier than a jump directly into a near-global sublevel set.

## 3. What boundedness and weak compactness do not give

Let \((e_j)\) be covariance eigenvectors with \(Qe_j=\lambda_je_j\). In infinite dimension, trace class gives \(\lambda_j\to0\). Fix \(0<r<R\), and consider the bounded sequence \(x_j=Re_j\). Then
\[
\begin{aligned}
\mu\bigl(B(0,r)-x_j\bigr)
&\le \mathbb P\bigl(|R+\sigma\sqrt{\lambda_j}\,G|<r\bigr)\\
&\le \exp\!\left[-\frac{(R-r)^2}{2\sigma^2\lambda_j}\right]
\longrightarrow0,
\end{aligned}
\tag{2}
\]
where \(G\sim N(0,1)\), and the last inequality is the Gaussian Chernoff bound. Thus
\[
\inf_{\|x\|\le R}\mu(B(0,r)-x)=0.
\]
The closed radius-\(R\) ball is weakly compact, and \(x_j\rightharpoonup0\). Neither fact repairs (2).

This failure already occurs for the smooth loss \(L(x)=\|x\|^2\), since \(A_{r^2}=B(0,r)\). It also shows that a finite number of nonlinear loss observables does not suffice: this same loss is the square of the single scalar observable \(F(x)=\|x\|\), whose values are bounded on that sequence.

For eigenvalues such as \(\lambda_j=2^{-j}\), the upper bounds in (2) are summable along the deterministic locations \(Re_j\). Nevertheless, those locations have not been shown to form a possible trajectory of the original accept/reject chain for this loss. Therefore the precise established conclusion is:

> Boundedness alone does not justify a uniform-hit or divergent-hazard proof. A bounded-trajectory counterexample, or a different theorem proving convergence for every bounded trajectory of the original rule, requires an additional argument.

This note does not resolve that stronger algorithmic dichotomy. In particular, it does not replace a failed proof by a claimed counterexample.

### Gaussian translation warning

One cannot use a finite-dimensional density-ratio estimate with \(\|h\|_H\) in place of the covariance-weighted norm. The relevant space of shifts is
\[
H_\Sigma=\left\{h:\ \|h\|_\Sigma^2
=\sum_j\frac{|\langle h,e_j\rangle|^2}{\sigma^2\lambda_j}<\infty\right\}.
\]
For example, take \(\sigma=1\), \(\lambda_j=4^{-j}\), and \(h_j=2^{-j}/\sqrt j\). Then \(h\in H\), but \(\|h\|_\Sigma=\infty\). The laws of \(Z\) and \(Z+h\) are singular, as the following direct test shows. Put \(m_j=1/\sqrt j\), \(S_N=\sum_{j\le N}m_j^2\), and
\[
T_N(x)=S_N^{-1}\sum_{j\le N}m_j\frac{x_j}{\sqrt{\lambda_j}}.
\]
Under the first law this has mean zero and variance \(1/S_N\); under the second it has mean one and the same variance. Along a subsequence with \(S_{N_k}\ge k^2\), Chebyshev's inequality and the elementary Borel–Cantelli lemma give almost-sure limits zero and one, respectively. These disjoint measurable events establish singularity. Full support still gives positive probability to every norm-open ball under either law.

## 4. Conditions that make weak recurrence sufficient

**Proposition 2.** Suppose that, on each bounded subset of \(H\), \(L\) is sequentially weakly upper semicontinuous:
\[
x_j\rightharpoonup x\quad\Longrightarrow\quad
\limsup_jL(x_j)\le L(x).
\tag{3}
\]
Then, for every \(a>m\) and finite \(R\),
\[
\inf_{\|x\|\le R}p_a(x)>0.
\tag{4}
\]
Consequently, almost-sure norm boundedness of the trial states suffices for convergence under this additional assumption. Recurrence to a fixed bounded set also suffices.

**Proof.** If \(x_j\rightharpoonup x\), then \(x_j+z\rightharpoonup x+z\) and the sequence is bounded for every fixed \(z\). When \(L(x+z)<a\), (3) makes \(L(x_j+z)<a\) eventually. Fatou's lemma therefore gives
\[
p_a(x)\le\liminf_jp_a(x_j).
\]
Every bounded sequence in a separable Hilbert space has a weakly convergent subsequence: diagonal extraction gives convergence of all coordinates in an orthonormal basis, and the norm bound controls the remaining coordinates when testing against an arbitrary fixed vector. If the infimum in (4) were zero, a sequence approaching that infimum would have such a subsequence; the displayed inequality would contradict \(p_a(x)>0\) at its weak limit. This proves (4). For a random finite trajectory bound, apply the argument on the countable events that the bound is at most an integer. ∎

Weak **lower** semicontinuity is insufficient for this proof: the norm-squared example is weakly lower semicontinuous and violates (4). The required direction concerns openness of good strict sublevel sets.

A concrete sufficient case is
\[
L(x)=\ell(Kx),
\tag{5}
\]
where \(K:H\to E\) is a compact linear map into a Banach space and \(\ell\) is continuous on the relevant observation space. Weak convergence of a bounded sequence then implies strong convergence of its \(K\)-images: compactness gives convergent subsequences of those images, and their only possible limit is \(Kx\), as continuous linear functionals identify the weak limit. Thus (3) holds with equality of the limit.

More generally, (5) only needs the observed trial states \(KY_n\) to recur in a fixed compact subset of \(\overline{K(H)}\). The observed proposal is exactly
\[
K(Y_n+Z_n)=KY_n+KZ_n.
\]
The law of \(KZ_n\) has full support on \(\overline{K(H)}\): preimages under \(K\) of neighborhoods that meet its range are nonempty open subsets of \(H\). Compactness and the same lower-semicontinuity argument then yield uniform target-hit probabilities in observation space. Components in \(\ker K\) may be unbounded. This is a substantive weakening of state-space precompactness.

For a nonlinear finite observation \(F(x)\), finite output dimension alone does not supply the identity above. A sufficient replacement is an actual observation kernel: the law of \(F(x+Z)\) depends only on \(F(x)\), is weakly continuous as a function of that observation, and assigns positive mass to the desired open observation sublevel set. On compact sets of observed states, the open-set lower bound under weak convergence of probability measures gives a uniform positive success probability. In a metric observation space, that lower bound follows by increasing continuous approximations \(\min(1,j\,d(v,O^c))\) to the indicator of the open target set \(O\). The dependence-only-on-observation property, or another uniform estimate replacing it, must be proved for the physical closure; bounded residuals do not prove it.

## 5. Tight distributions can replace compact sample paths

**Proposition 3.** Suppose the family of laws of \(Y_n\) is uniformly tight. It is enough that uniform tightness hold along one deterministic infinite subsequence of trial indices. Then \(V_n\to m\) almost surely, assuming only norm continuity of \(L\).

**Proof.** Norm continuity and Fatou's lemma show that \(p_a\) is norm lower semicontinuous. Positivity therefore gives \(c=\inf_Cp_a>0\) on every nonempty norm-compact set \(C\).

Fix \(a>m\), and suppose \(s=\mathbb P(V_\infty\ge a)>0\). Tightness gives a compact \(C\) with \(\mathbb P(Y_n\notin C)<s/2\) at every selected index. At such an index,
\[
\mathbb P(V_n\ge a,\ Y_n\in C)\ge s/2.
\]
Conditional on this event, either the flow has already put the loss below \(a\), or the proposal does so with probability at least \(c\). Hence
\[
\mathbb P(V_n\ge a)-\mathbb P(V_{n+1}\ge a)\ge cs/2.
\]
Summing over the infinitely many distinct selected indices is impossible, since monotonicity makes the left sides nonnegative and their sum at most one. Thus \(s=0\). Countably many levels give the conclusion. ∎

This assumption concerns probability distributions, not a single compact set containing almost every entire trajectory. It can be established, for example, from an orthonormal basis and a uniform stronger-norm estimate
\[
\sup_n\mathbb E\sum_{j=1}^\infty w_j|\langle Y_n,e_j\rangle|^2<\infty,
\qquad 1\le w_j\uparrow\infty.
\tag{6}
\]
The corresponding weighted ellipsoids are norm compact because their tails are bounded by the ellipsoid radius divided by \(w_{J+1}\); Markov's inequality makes the probabilities outside them uniformly small. Ordinary boundedness of \(\mathbb E\|Y_n\|^2\) has no such tail control and does not imply tightness in infinite dimension.

## 6. Robust rescue shifts, with quantitative Gaussian costs

One may prove divergence of success probabilities without controlling the whole state or requiring a fixed compact family of successful shifts.

**Gaussian ball bound.** For every \(h\in H_\Sigma\) and \(r>0\),
\[
\mu(B(h,r))\ge
\exp\!\left(-\tfrac12\|h\|_\Sigma^2\right)\mu(B(0,r)).
\tag{7}
\]
For a shift supported on finitely many covariance eigenvectors, change variables in the finite-dimensional Gaussian density. On the symmetric event \(\{\|Z\|<r\}\), symmetry of \(Z\) replaces the exponential linear factor by its hyperbolic cosine, which is at least one; the remaining factor is exactly \(e^{-\|h\|_\Sigma^2/2}\). For a general \(h\in H_\Sigma\), its finite-coordinate truncations converge to \(h\) in \(H\), and their squared covariance norms increase to \(\|h\|_\Sigma^2\). Gaussian measures give every sphere \(\{\|Z-h\|=r\}\) zero mass: condition on all but one nondegenerate Gaussian coordinate, leaving at most two possible values of that coordinate. Thus the ball probabilities converge under the truncations, proving (7).

Suppose that, while the loss remains above \(a>m\), there are past-measurable shifts \(h_n\in H_\Sigma\) and radii \(r_n>0\) such that
\[
L(Y_n+h_n+u)<a\quad\text{for every }\|u\|<r_n.
\tag{8}
\]
Then
\[
p_n(a)\ge
\exp\!\left(-\tfrac12\|h_n\|_\Sigma^2\right)
\mu(B(0,r_n)).
\tag{9}
\]
Consequently, divergence of the sum of the right side proves convergence via Proposition 1. The shifts here describe successful outcomes of the original random proposal; the algorithm need not compute or apply them.

For instance, a fixed robust radius \(r>0\) and
\[
\|h_n\|_\Sigma^2\le 2\log(n+1)+C_a
\tag{10}
\]
give a harmonic lower bound and hence divergent cumulative probability. The rescue cost may therefore grow without bound. With recurrent trials indexed by their visit count \(k\), the same statement holds with \(2\log(k+1)+C_a\). This criterion does not require a fixed compact family of rescue shifts.

Alternatively, if all successful shifts lie in a fixed norm-precompact set and a common radius satisfies (8), full support and norm lower semicontinuity already give a uniform positive probability. A covariance-norm bound is unnecessary in that case, including when some shifts lie outside \(H_\Sigma\).

Neither version is automatic from norm boundedness of the state. The robust radius in (8), the shift cost, and their behavior along the actual trial states are the substantive proof obligations. A radius shrinking too rapidly can make (9) summable even if the shift costs remain bounded.

## 7. An explicit modification that removes recurrence assumptions

If a changed proposal rule is admissible, add occasional **absolute** proposals
\[
W_n=x_{\mathrm{ref}}+Z_n
\]
from a fixed anchor, and apply the same acceptance test. Use this proposal independently at trial \(n\) with probability \(\rho_n\), where \(\sum_n\rho_n=\infty\); otherwise retain the original centered additive proposal. The threshold-hit probability is then at least
\[
\rho_n\,\mu(A_a-x_{\mathrm{ref}}),
\]
and the fixed second factor is positive for every \(a>m\). Proposition 1 proves convergence of loss to \(m\), with no boundedness, precompactness, or attainment assumption. This rule does not need to know \(m\) or a minimizer.

Relative to the incumbent, an absolute proposal has perturbation \(x_{\mathrm{ref}}-Y_n+Z_n\). It is therefore a state-dependent recentering, not an iid centered additive perturbation. Its convergence theorem must not be attributed to the original algorithm. The result also gives no useful rate when near-optimal sublevel sets have extremely small Gaussian mass.

## 8. Established conclusions and remaining input

* **Proved:** conditional-probability divergence; recurrent uniform progress; convergence from tight trial-state laws; weak-recurrence convergence under weak upper semicontinuity; compact linear observation reduction; and the quantitative robust-rescue bound.
* **Disproved:** the implication from norm boundedness or weak compactness alone to uniform Gaussian probability of reaching a fixed good open set. A bounded finite collection of nonlinear outputs does not repair that implication.
* **Unresolved in this scoped note:** whether every bounded trajectory of the original accepted-additive-Gaussian chain must have globally minimal limiting loss for every continuous loss. The probability obstruction is not a complete chain counterexample.
* **Needed for the particular population model:** its exact observation map and proposal dependence, or a proved tail/tightness estimate, or robust successful perturbations satisfying (8)–(9). No such model-specific statement follows solely from “finite-input squared loss.”

The shortest promising bridge for the stated application is to identify whether the physical loss factors through a compact linear observation, or whether its nonlinear observation proposal has a provable uniform success estimate on the bounded region actually visited. If neither holds, a quantitative rescue construction is more informative than repeating an unproved compactness assumption.
