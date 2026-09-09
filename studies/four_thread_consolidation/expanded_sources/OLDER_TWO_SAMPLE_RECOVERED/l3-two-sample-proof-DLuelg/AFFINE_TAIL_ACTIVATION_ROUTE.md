# R4: affine-tail activation and approximate deep-linear balance

Analytic sidecar, 2026-09-06. One candidate and one mechanism; no experiments,
delegation, optimizer changes, or changes to the prescribed initialization.

**Result.** For the fixed activation

\[
\phi(z)=z+1+\tfrac12\tanh z,                                      \tag{A1}
\]

there is a width-uniform approximate Gram-balance estimate along the actual
finite gradient flow, proved below. Its trace has a bounded Euler-defect
source. Its operator version has an additional cross-neuron source which
the trace cancels. The balance estimate controls a trained operator, but
does not supply the response estimate needed for the population theorem.
A precise attempted upgrade is false at the **exact Gaussian
initialization**: the curvature coefficient
\(W^{(4)}_i(t)\phi''(z^{(3)}_{a,i}(t))\) has no width-uniform Lipschitz
onset in the maximum norm, with probability tending to one. This is proved
for both label cases and every \(-1\leq\rho<1\), including \(\rho=-1\).
It is a failure of that instantaneous response-control mechanism, not a
counterexample to population continuation or to an integrated traversal
estimate with a possibly singular initial time bound.

## 1. Contract, dependencies, and the question tested

Authoritative inputs read in full:

- `/tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md`;
- `/tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md`.

Procedural instructions read in full: `/etc/codex/skills/solve-math-rigorously/SKILL.md`,
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's
`references/research-contract.md`, `references/evidence-ledger.md`, and
`references/adversarial-audit.md`. No experimental or multi-route reference
was needed. All derivations and the output of this sidecar are in `/tmp`.
No other research artifact is modified. No external mathematical theorem
requiring an unverified specialized dependency is imported.

The architecture, raw metric, summed square loss, Gaussian initialization,
physical time, and exact-GD step size remain those of the contract. This
note proves finite-GF estimates and initialization assertions. It does not
replace the finite readout by zero, assert finite-width label-mode
symmetry, or establish GD convergence. Conditional population statements
are identified as such. Constants below are independent of width; they
may depend on fixed input dimension and on the finite physical horizon.

The mechanism tested is: does bounded departure from degree-one
homogeneity yield an approximate deep-linear balance strong enough to
control the instantaneous trained curvature multiplier? We first obtain
the exact balance and its norm estimates, and then test the proposed
response upgrade on the actual initial dynamics. We stop at that test.

For bookkeeping only, some formulas use fixed symbols \(b,\epsilon\),
always with \(b=1,\epsilon=1/2\). Put \(k=1+\epsilon=3/2\). Then

\[
1\leq\phi'(z)=1+\epsilon\operatorname{sech}^2z\leq k,
\qquad \phi''(z)=-2\epsilon\operatorname{sech}^2z\tanh z.       \tag{A2}
\]

The two affine tails have intercepts \(b\pm\epsilon\); no coefficient
depends on width or tends to zero. On a nondegenerate Gaussian marginal,
\(\phi\) cannot agree almost surely with an affine function: continuity
and the positive Gaussian density would imply agreement everywhere,
contradicting (A2). This verifies strict distributional nonaffinity at
initialization only. Its persistence at every trained time, and genuine
learning in all hidden layers, are separate unproved target obligations.

## 2. Normalization and the exact balance identity

Work first at finite width. Set

\[
A_1=\sqrt{d/n}\,W^{(1)},\quad A_2=W^{(2)},\quad A_3=W^{(3)},
\quad v=W^{(4)}/\sqrt n,\quad \xi_a=x_a/\sqrt d.
\]

This is an isometric change of coordinates for the raw parameter metric,
not an optimizer change. Write

\[
Z_a^\ell=z_a^{(\ell)}/\sqrt n,\quad H_a^\ell=h_a^{(\ell)}/\sqrt n,
\quad Q_a^\ell=q_a^{(\ell)}/\sqrt n\ (\ell=1,2),\quad Q_a^3=v,
\]

and let \(D_a^\ell\) be the diagonal matrix of
\(\phi'(z_{a,i}^{(\ell)})\). Thus
\(\Delta_a^\ell=D_a^\ell Q_a^\ell\) is the normalized backward field.
Let \(c_a=-2r_a=-2(f_a-y_a)\). The exact physical-GF equations are

\[
\begin{aligned}
\dot A_1&=\sum_a c_a\Delta_a^1\xi_a^T,& Z_a^1&=A_1\xi_a,\\
\dot A_\ell&=\sum_a c_a\Delta_a^\ell(H_a^{\ell-1})^T,
 &Z_a^\ell&=A_\ell H_a^{\ell-1}\quad(\ell=2,3),\\
\dot v&=\sum_a c_a H_a^3,& f_a&=v^TH_a^3.
\end{aligned}                                                   \tag{A3}
\]

For vectors, \(u\otimes w=uw^T\). Define the three trained Gram balances

\[
B_1=A_2^TA_2-A_1A_1^T,\quad
B_2=A_3^TA_3-A_2A_2^T,\quad B_3=v\otimes v-A_3A_3^T.             \tag{A4}
\]

All are operators on the corresponding layer's neuron space. In the
following formulas \(\ell\in\{1,2,3\}\), and the layer superscripts on
\(H,Z,Q,D\) are suppressed. Differentiating (A4) using (A3) gives

\[
\dot B_\ell=\sum_a c_a\{
 H_a\otimes Q_a+Q_a\otimes H_a
 -(D_aQ_a)\otimes Z_a-Z_a\otimes(D_aQ_a)\}.                    \tag{A5}
\]

For example, differentiating the incoming Gram \(A_\ell A_\ell^T\)
gives \(\sum_a c_a(\Delta_a\otimes Z_a+Z_a\otimes\Delta_a)\).
Differentiating the outgoing Gram gives the other two terms, because
\(A_{\ell+1}^T\Delta_a^{\ell+1}=Q_a\); at the top use
\(Q_a^3=v\). This also proves (A5) for the first rectangular layer.
No inversion of the input covariance is involved, so \(\rho=-1\) is
included without a limiting argument.

Let \(e=n^{-1/2}(1,\ldots,1)^T\),
\(T_a=n^{-1/2}\tanh(z_a)\), and
\(S_a=\operatorname{diag}(\operatorname{sech}^2(z_a))\).
Then (A5) has the exact affine-tail form

\[
\begin{aligned}
\dot B_\ell=\sum_a c_a\{&
 (be+\epsilon T_a)\otimes Q_a+Q_a\otimes(be+\epsilon T_a)\\
 &-\epsilon(S_aQ_a)\otimes Z_a
       -\epsilon Z_a\otimes(S_aQ_a)\}.                       \tag{A6}
\end{aligned}
\]

The affine part cancels exactly; the remaining sources are explicitly
proportional to the fixed intercept and fixed nonlinear amplitude.

The scalar Euler defect is especially simple. Define

\[
\psi(z)=\tanh z-z\operatorname{sech}^2z,
\qquad E(z)=\phi(z)-z\phi'(z)=b+\epsilon\psi(z).
\]

Since
\(\psi'(z)=2z\operatorname{sech}^2z\tanh z\geq0\) and
\(\psi(\pm\infty)=\pm1\), we have \(|E(z)|\leq b+\epsilon\).
With \(e_a=H_a-D_a Z_a=n^{-1/2}E(z_a)\), another exact form is

\[
\begin{aligned}
\dot B_\ell=\sum_a c_a\{&e_a\otimes Q_a+Q_a\otimes e_a\\
 &+\epsilon[(S_a Z_a)\otimes Q_a+Q_a\otimes(S_a Z_a)
 -(S_aQ_a)\otimes Z_a-Z_a\otimes(S_aQ_a)]\}.                 \tag{A7}
\end{aligned}
\]

The bracket in the second line has zero trace, because \(S_a\) is
self-adjoint. Thus

\[
\frac d{dt}\operatorname{tr}B_\ell
       =2\sum_a c_a\langle e_a,Q_a\rangle,\qquad
\left|\frac d{dt}\operatorname{tr}B_\ell\right|
       \leq2(b+\epsilon)\sum_a|c_a|\|Q_a\|.                 \tag{A8}
\]

Although the initial traces need not be bounded in width, their **changes**
are bounded by the right side. By contrast, the initial operator norms
of the balances are bounded in probability under the prescribed law.

## 3. A proved width-uniform trained-operator estimate

**Lemma 1 (approximate balance along physical GF).** On any finite-GF
existence interval for (A1),

\[
\|\dot B_\ell\|_{\rm op}
 \leq 2\sum_a |c_a|\|Q_a\|
             [b+\epsilon(1+\|Z_a\|)].                     \tag{A9}
\]

For every finite \(T\), the following completely explicit bounds hold
on \([0,T]\), with no width-dependent constant. Put

\[
R=\sqrt{L(0)},\quad D_T=R\sqrt T,
\quad M_1=\|A_1(0)\|_F+D_T,
\quad M_j=\|A_j(0)\|_{\rm op}+D_T\ (j=2,3),
\quad V=\|v(0)\|+D_T.
\]

Define scalar forward bounds recursively by

\[
Z_1^*=M_1,\quad H_1^*=kZ_1^*+b,\quad
Z_2^*=M_2H_1^*,\quad H_2^*=kZ_2^*+b,\quad
Z_3^*=M_3H_2^*,\quad H_3^*=kZ_3^*+b,
\]

and backward bounds by

\[
Q_3^*=V,\qquad Q_2^*=kM_3V,\qquad Q_1^*=k^2M_2M_3V.
\]

Then

\[
\begin{aligned}
\sup_{t\leq T}\|B_\ell(t)-B_\ell(0)\|_{\rm op}
 &\leq 4\sqrt2 RT Q_\ell^*[b+\epsilon(1+Z_\ell^*)],\\
\sup_{t\leq T}|\operatorname{tr}(B_\ell(t)-B_\ell(0))|
 &\leq 4\sqrt2 RT(b+\epsilon)Q_\ell^*.                       \tag{A10}
\end{aligned}
\]

**Proof.** In (A6), \(\|T_a\|\leq1\), \(\|S_a\|_{\rm op}\leq1\),
and \(\|u\otimes w\|_{\rm op}=\|u\|\|w\|\); these give (A9).
Because (A3) is the gradient flow in Euclidean coordinates,

\[
\frac d{dt}L=-\|\dot A_1\|_F^2-\|\dot A_2\|_F^2
             -\|\dot A_3\|_F^2-\|\dot v\|^2.              \tag{A11}
\]

Integrating and applying Cauchy--Schwarz bounds the total parameter
displacement by \(\sqrt{tL(0)}\). Operator norms are bounded by Frobenius
norms, so all the stated \(M_j,V\) bounds follow. The inequality
\(|\phi(z)|\leq k|z|+b\) gives the forward recursion. Applying (A2)
and the two transpose matrix actions gives the backward bounds.
Finally \(\sum_a|c_a|\leq2\sqrt2\sqrt{L(t)}\leq2\sqrt2R\).
Integration of (A9) and (A8) proves (A10).

These arguments first hold before any putative finite blowup. For each
fixed width, the vector field is smooth everywhere. If its maximal time
were finite, (A11) would make the parameter path Cauchy at that time:
the distance between times \(s<t\) is at most
\(\sqrt{(t-s)L(0)}\). Its limit is a finite parameter vector, where the
smooth vector field admits a local solution and uniqueness. Pasting this
solution extends the path, a contradiction. Thus finite GF is global
and the estimates hold for every finite \(T\). This continuation fact
uses ordinary finite-dimensional local existence; it is not population
existence in disguise. ∎

For example (A4) and (A10) imply the genuine trained-operator inequality

\[
\|A_3(t)\|_{\rm op}^2
 \leq \|v(t)\|^2+\|B_3(0)\|_{\rm op}
       +4\sqrt2 RTQ_3^*[b+\epsilon(1+Z_3^*)].               \tag{A12}
\]

Analogous inequalities propagate through \(B_2,B_1\). These are
approximate deep-linear balances, not conservation laws. In particular
their constants are not small at the fixed coefficients (A1).

There is one useful label-specific refinement, with an essential
qualification. At the top, \(Q_1^3=Q_2^3=v\), so the entire intercept
source in (A6) is
\(b(c_1+c_2)(e\otimes v+v\otimes e)\). On a regular symmetric
opposite-label population path, if one has independently constructed
that path and justified its equations, \(c_1+c_2=0\); the top balance
then has only the fixed \(\epsilon\)-sources. The corresponding
right sides of (A9) and the operator bound (A10) omit \(b\) at this
layer. This cancellation is not an identity for the prescribed finite
flow: for opposite labels its coefficient is
\(c_1+c_2=-2(f_1+f_2)\). It is also not a same-label cancellation.
Even the population cancellation leaves the cross-neuron source and
the opposite-label obstruction in Lemma 2.

At the prescribed initialization, \(\|A_1(0)\|_F^2\to d\) in probability
by row averaging, \(\|v(0)\|=O_{\mathbb P}(n^{-1})\), and the two initial
hidden operator norms are bounded in probability. An elementary bound
for either Gaussian hidden matrix is

\[
\mathbb P(\|W\|_{\rm op}>10)
 \leq 2\,9^{2n}\exp(-100n/8)\longrightarrow0.
\]

Indeed two sphere nets of radius \(1/4\), each of size at most \(9^n\),
approximate the bilinear operator supremum within a factor two; each
fixed bilinear form is \(N(0,1/n)\), and the Gaussian tail bound and
union bound give the display. The forward recursion at time zero gives
\(H_3^*=O_{\mathbb P}(1)\), hence \(f_a(0)\to0\) and \(L(0)\to2\).
Every right side of (A10) is therefore bounded in probability, uniformly
in width, for each fixed \(T\).

The bounded Euler defect by itself is not a distinguishing advantage
over shifted arctan, whose Euler defect is also bounded. What is specific
here is the identity-linear cancellation (A6), together with the lower
derivative bound and the affine-tail moment estimates. Nor is Lemma 1 a
new proof of primal boundedness: its independent content is the exact
balance decomposition and control of its trained drift. Primal norm
bounds were already supplied by loss dissipation.

## 4. Why the scalar balance does not become an operator conservation law

The trace-free term in (A7) cannot be discarded or estimated merely by
the bounded scalar Euler defect. A two-coordinate calculation makes
this failure explicit, without any functional-analysis multiplier
argument. Consider one summand in (A5), take \(n=2\),

\[
z=(u,R_*)^T,\qquad Q=(R_*,0)^T,
\quad u\ne0\text{ fixed},\quad R_*\longrightarrow\infty,
\]

and keep the normalization \(Z=z/\sqrt2\), \(H=\phi(z)/\sqrt2\).
Its off-diagonal entry is exactly

\[
Q_1(H_2-D_{11}Z_2)
 =\frac{R_*}{\sqrt2}
   [b+\epsilon\tanh R_*
           -\epsilon\operatorname{sech}^2u\,R_*].          \tag{A13}
\]

It grows quadratically, whereas \(\|Q\|=R_*\) and the normalized
Euler-defect vector satisfies \(\|H-DZ\|\leq b+\epsilon\).
Thus no bound of the form
\(\|\text{one balance summand}\|_{\rm op}\leq C(b,\epsilon)\|Q\|\)
can follow from the scalar Euler defect alone. The two-coordinate example
is an algebraic counterexample, **not** a claim that this chosen state is
reached by the Gaussian flow. The next test is explicitly at the
prescribed Gaussian initialization and avoids that reachability gap.

## 5. An actual-initialization obstruction to the instantaneous response upgrade

We test the following precise, potentially useful strengthening of
balance control. Let

\[
m_{a,i}^{(n)}(t)=W_i^{(4)}(t)\phi''(z_{a,i}^{(3)}(t)).
\]

This is an actual coefficient of the differential of
\(\delta_a^{(3)}=W^{(4)}\phi'(z_a^{(3)})\): a preactivation variation
\(\dot z\) contributes \(m_a\dot z\). A width-uniform maximum bound
on \(m_a\) would therefore control this part of the response in the
normalized Euclidean norm.

**Lemma 2 (no uniform Lipschitz onset of the trained curvature coefficient).**
For either sample \(a\), every fixed \(T>0\), and every finite \(C_*>0\),
the exact finite GF with the exact Gaussian initialization satisfies

\[
\mathbb P\left(
 \sup_{0<t\leq T}
 \frac{\max_i|m_{a,i}^{(n)}(t)-m_{a,i}^{(n)}(0)|}{t}
 \leq C_*\right)\longrightarrow0.                          \tag{A14}
\]

In fact \(\max_i|\dot m_{a,i}^{(n)}(0)|\to\infty\) in probability.
This holds for each fixed \(\rho\in[-1,1)\) and all four label choices.
In particular a tight random constant cannot replace \(C_*\) in a
probability-tending-to-one Lipschitz estimate.

**Proof, initial Gaussian geometry.** By simultaneous label/readout sign
symmetry it is enough to describe the limiting law for
\(y=(1,\sigma)\), \(\sigma=\pm1\); negating both labels only negates the
limiting derivative below. Let \((U,V)\) denote the layer-three initial
preactivation pair in its limiting forward law. This is a centered
Gaussian pair whose covariance is the layer-two feature second-moment
matrix. We need its covariance to be positive definite, also at
\(\rho=-1\).

Here is a direct verification. For any centered exchangeable Gaussian
pair \((G_1,G_2)\), write \(\phi(z)=b+\chi(z)\), with
\(\chi(z)=z+\epsilon\tanh z\) odd. Thus
\(\mathbb E\phi(G_a)=b\). The feature second-moment matrix has equal
diagonal entries and its two eigenvalues are

\[
\frac12\mathbb E[(\phi(G_1)+\phi(G_2))^2]\geq2b^2,
\qquad
\frac12\mathbb E[(\phi(G_1)-\phi(G_2))^2]
 \geq\frac12\mathbb E[(G_1-G_2)^2].                         \tag{A15}
\]

The first inequality uses the mean \(2b\) and nonnegativity of variance;
the second follows pointwise from \(\phi'\geq1\). At the first layer
the last variance is \(2(1-\rho)>0\). Both eigenvalues of the first
feature second-moment matrix are consequently positive, including when
\(G_2=-G_1\). Repeating the same argument at the next layer proves that
the covariance of \((U,V)\) is positive definite. All its moments are
finite: \(|\phi(z)|\leq k|z|+b\) propagates every fixed Gaussian moment
through the three initial layers.

For completeness this forward-law passage uses only fresh matrices.
Conditional on the preceding features, rows of the next Gaussian
matrix give iid centered Gaussian pairs with the empirical feature
second-moment matrix. The first empirical matrix converges by the law of
large numbers. At each of the next two steps, conditional averaging and
the finite fourth moments make the empirical second-moment error tend
to zero; expectations converge by coupling Gaussian pairs through their
convergent covariance square roots and using the linear growth bound.
Conditional variances of bounded test averages are at most a constant
divided by \(n\). This proves convergence in probability of the initial
joint empirical laws, including for bounded continuous functions of
\((U,V)\). No statement about the trained population flow is used.

**Proof, the exact first derivative.** At each finite width, without
changing its readout initialization, differentiation gives

\[
\dot m_{a,i}(0)
 =-2\sum_{b'=1}^2r_{b'}(0)\phi(z_{b',i}^{(3)}(0))
                            \phi''(z_{a,i}^{(3)}(0))
 +W_i^{(4)}(0)\phi'''(z_{a,i}^{(3)}(0))\dot z_{a,i}^{(3)}(0). \tag{A16}
\]

Let \(\|u\|_n^2=n^{-1}\sum_i u_i^2\). The initial norm estimates in
Section 3 give \(f_b(0)=O_{\mathbb P}(n^{-1})\),
\(\|W^{(4)}(0)\|_n=O_{\mathbb P}(n^{-1})\), and bounded initial
forward norms. Gates and both initial hidden operator norms are bounded
in probability. Consequently the three hidden parameter velocities
in (A3) are \(O_{\mathbb P}(n^{-1})\) in their displayed metrics.
Differentiating the forward recursion then gives
\(\|\dot z_a^{(3)}(0)\|_n=O_{\mathbb P}(n^{-1})\).
Also the Gaussian union bound gives
\(\max_i|W_i^{(4)}(0)|=O_{\mathbb P}(\sqrt{\log n}/n)\).
The function \(\phi'''\) is bounded (differentiate (A2)). Thus (A16)
differs in \(\|\cdot\|_n\), by a quantity tending to zero in probability,
from the initial coordinatewise array

\[
2[\phi(z_{1,i}^{(3)}(0))+
             \sigma\phi(z_{2,i}^{(3)}(0))]
             \phi''(z_{a,i}^{(3)}(0)).                      \tag{A17}
\]

For example the second term in (A16) has normalized norm
\(O_{\mathbb P}(\sqrt{\log n}/n^2)\), and replacement of the residuals
by minus the labels costs \(O_{\mathbb P}(n^{-1})\). Hence the
empirical law of \(\dot m_{1,i}(0)\) converges in probability, against
bounded Lipschitz tests, to the law of

\[
J_\sigma(U,V)=2[\phi(U)+\sigma\phi(V)]\phi''(U).             \tag{A18}
\]

For sample two the limiting variable is
\(2[\phi(U)+\sigma\phi(V)]\phi''(V)=\sigma J_\sigma(V,U)\);
its absolute value has the same law. The asserted empirical convergence
follows from the preceding forward-law argument and the normalized-norm
error, since a Lipschitz test changes its empirical average by at most
its Lipschitz constant times that error.

**Proof, unbounded support.** On the compact interval
\(I=[1/2,1]\), \(|\phi''(u)|\) is bounded below by a positive constant.
The function \(\phi\) is unbounded on either tail, while \(\phi(U)\)
is bounded for \(U\in I\). Because \((U,V)\) has a strictly positive
Gaussian density everywhere, for every \(M<\infty\) there is a rectangle
\(I\times J_M\) of positive probability on which
\(|J_\sigma(U,V)|>M\), for either sign \(\sigma\).
Choose a bounded nonnegative Lipschitz test vanishing on \([-M,M]\)
and with positive expectation under this law. Its empirical average
converges to a positive number, so with probability tending to one
some coordinate has \(|\dot m_{a,i}(0)|>M\). This proves divergence of
the maximum. Finally the event in (A14), by differentiability at zero,
implies \(\max_i|\dot m_{a,i}(0)|\leq C_*\); its probability tends to
zero. The assertion about tight random constants follows by first
bounding such a constant by a fixed large \(M\). ∎

This is specifically a two-sample obstruction. The affine tails do give

\[
\sup_u |\phi(u)\phi''(u)|<\infty,
\]

since \(|u|\operatorname{sech}^2u\) is bounded. Thus the own-sample
term in (A18) is harmless for a maximum bound. The other sample's
\(\phi(V)\phi''(U)\) is the unbounded term. At \(\rho=-1\), the
first-layer pair is antiparallel but the positive shift makes its feature
second-moment matrix full rank; the layer-three Gaussian pair therefore
still has the conditional tail used above. Discarding that positive
eigenvalue would silently change the model.

In the intended zero-readout population initialization, (A18) is also
the formal initial physical-time derivative, on any population path
where that derivative is justified: \(\dot w(0)=2(\phi(U)+\sigma\phi(V))\)
and all initial hidden velocities vanish. Lemma 2 did not assume such a
population path exists. In feature time the corresponding coefficient
is \(\tfrac12(\phi(U)+\sigma\phi(V))\phi''(U)\), consistent with
\(ds/dt=4\) initially. No feature clock was assigned to finite GF.

## 6. Scope of the result and the remaining term

The affine-tail initialization has a stronger contrast signal than the
shifted-arctan initialization. If
\(D_\ell=\mathbb E[(H_{1,0}^{(\ell)}-H_{2,0}^{(\ell)})^2]\), with these
\(H\)'s denoting unnormalized population fields, (A2) and the Gaussian
variance recursion give

\[
D_0=2(1-\rho),\qquad D_{\ell-1}\leq D_\ell\leq k^2D_{\ell-1},
\qquad
\frac{1-\rho}{2}\leq\frac{D_3}{4}
              \leq\frac{k^6(1-\rho)}2.                     \tag{A19}
\]

The same-label initial mode energy is at least \(b^2=1\) by its mean.
These are initialization estimates, not trained coercivity estimates.

The proposed mechanism has now been tested at three precise levels:

| Claim | Status | Exact scope / dependency |
|---|---|---|
| Affine-tail Gram decomposition and trace cancellation, (A5)–(A8) | Proved | Exact finite GF, all labels and all admissible inputs |
| Width-uniform trained balance drift, (A10) | Proved | Each finite physical horizon; initial bounds follow from the exact Gaussian law |
| Bounded Euler defect alone bounds the operator source linearly in \(\|Q\|\) | Falsified | Algebraic counterexample (A13); no reachability claim is attached |
| Balance can yield a width-uniform Lipschitz onset of \(w\phi''(z_a^3)\) in maximum norm | Falsified | Actual-initialization Lemma 2, both label modes and \(\rho=-1\) |
| An integrated curvature/traversal estimate with a singular initial time bound | Open | Lemma 2 neither establishes nor disproves it |
| Global population existence, uniqueness, reached-state restart, and full GF/GD limit | Open | Requires a response/compactness construction beyond the balances |
| Strict trained nonlinearity and all-hidden-layer feature learning at every finite time | Open | Initialization nonaffinity is insufficient |

The unresolved operator source in the balance is explicitly
\((S_aQ_a)\otimes Z_a+Z_a\otimes(S_aQ_a)\), together with its
trace-canceling counterpart in (A7). The unresolved **response** source
already appears at the top as
\(w\phi''(z_a^3)\,\delta z_a^3\); corresponding lower-layer terms have
\(q_a^\ell\phi''(z_a^\ell)\,\delta z_a^\ell\). Lemma 1 bounds their
factors in ordinary energy norms, but does not bound these products on
arbitrary response directions or on the actual response class. Lemma 2
rules out one concrete, stronger attempted bound using an actual
initial-time trained coefficient, rather than merely pointing out an
abstract multiplication problem.

In particular, (A14) does **not** show that \(m_a(t)\) is unbounded in
maximum norm for each fixed positive time, or that
\(\int_0^T\|m_a(t)\|_\infty\,dt\) must diverge in a population
construction. Fast traversal can regularize large initial tails and can
have a non-Lipschitz onset. It also does not rule out weighted-response
estimates. Those are the exact alternatives left open; resolving them
would require another authorized mechanism test.

No root claim is superseded: the main two-sample theorem remains open,
and the separate same-label shifted-arctan construction is unaffected.
This sidecar terminates with Lemma 1, the trace-versus-operator distinction,
and the actual-Gaussian response-onset obstruction. It is not submitted
as a full theorem or an externally audited proof.
