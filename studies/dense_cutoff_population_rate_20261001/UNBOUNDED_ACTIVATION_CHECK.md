# Integrated check of the joint forward/backward budget

2026-10-03. Internal collaborative reconstruction by the deterministic
tracking/probability checker. This is not an independent promotion review.
No experiments, manuscript changes, or Git operations were performed.

Checked complete source:
`UNBOUNDED_ACTIVATION_CANDIDATE.md`, SHA256
`e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713`.
The historical filename records the original candidate; the final source
now records its completed internally reconstructed status.
Scientific dependencies are the current canonical manuscript, the checked
response-modulus note, and the same-study fixed-moment cavity route.
No other study was read.

**Verdict: PASS for the completed joint-budget continuation.** The scalar
absorption, initialization, trace, common-cavity moment, and all-time
arguments below are valid. Their original verdict was conditional on a
complete local insertion lemma. That condition is now discharged by the
complete UNBOUNDED_INSERTION_CHECK.md, read here and checked for integrated
consistency, together with the coordinator's separate reconstruction of
the bounded and unbounded local estimates. Section 8 records the exact
local dependency and the top residual-offset correction. No empirical
moment or local sensitivity assumption remains an unproved input to the
combined study theorem. This is internal collaborative validation only.

The earlier source version's two wording issues have been repaired:
the projected difference radius is small in the normalized Gaussian metric,
and its error satisfies \(\mathbb E e^{\lambda E_n}\to1\).
The updated source also includes the uniform cavity initialization transfer
reconstructed in Section 2 below. These repaired portions were reread in
full; they resolve the previously reported presentation and initialization
clarifications. The final source also includes the exact corrected top
residual-offset equation and names the completed local reconstruction.

## 1. Setup and the exact conditional input

There are finitely many inputs \(v_a\), data weights \(p_a>0\) with
\(\sum_a p_a=1\), and a fixed number \(L\) of hidden layers of width \(n\).
The canonical dense flow has zero initial readout. Its residual RMS is
\(\rho=(\sum_a p_a r_a^2)^{1/2}\). The physical fitting tube supplies
\(\rho(t)\le Y e^{-\kappa t}\), total residual activity bounded by a fixed
constant times \(S=2Y/\kappa\), bounded normalized feature norms, and
bounded hidden matrix operator norms. Assume \(Y>0\); the zero-label
trajectory is stationary.

The activation at each layer is \(C^3\), with its first three derivatives
globally bounded. Values have at most linear growth. Write \(z_{a,i}^j\)
for preactivation, \(h_{a,i}^j=\phi_j(z_{a,i}^j)\), \(k_{a,i}^j\) for
the pre-gate backward carrier, and
\(\delta_{a,i}^j=\phi_j'(z_{a,i}^j)k_{a,i}^j\). At the top,
\(k_{a,i}^L=w_i\).

Define the running maxima and their empirical budget by
\[
 Z_i^j(t)=\max_a\sup_{u\le t}|z_{a,i}^j(u)|,\qquad
 K_i^j(t)=\max_a\sup_{u\le t}|k_{a,i}^j(u)|,\qquad
 H_j(t)=\frac1n\sum_i e^{\eta(Z_i^j(t)+K_i^j(t)/S)}.
\]
The full budget is \(H=\sum_{j=1}^L H_j\). Its stop is at \(B\);
independently stopped cavities use \(2B\), together with the required
physical and logarithmic coordinate stops.

The local input, now verified as recorded in Section 8, provides for every fixed number of
same-layer deletions:

1. The actual retained forward and backward coordinate discrepancies are
   \(o(1)\), uniformly through the common full/cavity prefix, with
   superpolynomially small exceptional probability.
2. The incoming-row/outgoing-column response expansions have uniformly
   vanishing scalar remainders and contain the actual scalar control
   amplitudes in their trace terms.
3. Their centered bilinear terms are \(o(1)\) on a common event uniform
   over the allowed control paths.
4. Singleton/common-cavity reference differences are bounded in
   normalized Euclidean norm by
   \(D_{n,p}\le C_p n^{-\gamma}(\log n)^{C_p}\), with some fixed
   \(\gamma>0\); their complete independently stopped paths have the
   forward/backward activity moduli used below.
5. The top-layer omitted prediction produces an \(o(1)\) response
   remainder, including its effect after variational propagation.

It is insufficient to prove only a global Euclidean parameter
discrepancy, or only an instantaneous empirical carrier budget.
The moment closure needs the stated coordinate comparisons and the
running joint budget.

## 2. Initialization and uniform cavity starts

At initialization all backward carriers vanish. In layer \(j\), conditional
on the preceding initialized features, each preactivation vector across
the finite data set is a centered Gaussian with covariance \(Q_{j-1,n}\).
The rows are conditionally independent.

For a centered Gaussian vector \(g_Q\) with covariance \(Q\), set
\[
 m(Q)=\mathbb E e^{\eta\max_a |(g_Q)_a|}.
\]
On every bounded set of positive semidefinite covariance matrices,
\(\mathbb E e^{2\eta\max_a|(g_Q)_a|}\) is uniformly bounded.
One proof bounds the exponential of the maximum by the sum of the
exponentials of the absolute coordinates and uses the scalar Gaussian
moment generating function. Conditional variance therefore gives
\[
 \mathbb P\left(
 \left|\frac1n\sum_i e^{\eta\max_a|z_{a,i}^j(0)|}
              -m(Q_{j-1,n})\right|>\epsilon
 \,\middle|\,Q_{j-1,n}\right)
 \le \frac{C_R}{n\epsilon^2}
\]
whenever \(\|Q_{j-1,n}\|\le R\).

The map \(m\) is continuous even at singular covariances: realize
\(g_Q=Q^{1/2}G\), use continuity of the positive square root, and dominate
on bounded covariance sets by \(e^{C|G|}\).
The same conditional argument for the feature products
\(\phi_j((g_Q)_a)\phi_j((g_Q)_b)\) proves the usual covariance
induction, since linear growth gives uniformly bounded fourth moments on
bounded covariance sets. Consequently
\[
 H(0)\ \longrightarrow\ \sum_{j=1}^L m(Q_{j-1})
 \quad\hbox{in probability}.
\]
Choosing \(B\) larger than twice this finite limit, with a strict margin,
proves \(H(0)<B/2\) with probability tending to one.
This does not assert an unconditional finite-width deep-network
exponential moment outside bounded covariance sets.

The conditional Gaussian union bound, restricted to bounded preceding
covariances, also proves
\(\max_{j,i,a}|z_{a,i}^j(0)|=O_{\mathbb P}(\sqrt{\log n})\).

For all fixed-size cavities simultaneously, the \(O(1/n)\) Chebyshev
estimate alone cannot be union-bounded over \(n^p\) subsets. A separate
transfer supplies the needed conclusion:

* On the ordinary operator-norm event, preceding initialized feature
  norms are deterministically at most \(C\sqrt n\). Gaussian tails then
  give an initialized maximum at most \(C\log n\) with superpolynomially
  small failure probability.
* Deleting any fixed \(p\) neurons in a single layer changes the first
  affected downstream preactivation vector in Euclidean norm by at most
  \(C_p\log n\). Fixed-depth propagation through bounded matrix
  operators and Lipschitz activations preserves this bound.
* At each subsequent initialized layer, its fresh Gaussian row is
  independent of the preceding feature discrepancy. Conditional on
  that discrepancy its scalar pairing has variance at most
  \(C_p\log^2 n/n\). Applying Gaussian tails at threshold \(n^{-b}\),
  \(0<b<1/2\), and union-bounding over the finitely many data/layer
  indices, the \(n\) rows, and at most \(n^p\) subsets yields
  superpolynomially small failure probability. At the first affected
  layer the same statement follows directly from the deleted Gaussian
  columns and their logarithmic scalar controls.

In this argument the bound on a preceding discrepancy is used before
conditioning on the fresh row; no independence is claimed after
conditioning on a full-network operator event.
Thus every retained initial preactivation differs by \(o(1)\),
uniformly over fixed-size deletions. Its initial exponential budget is
at most \(e^{o(1)}H(0)\), and the deleted coordinates contribute nothing.
Normalized feature Gram matrices differ by \(o(1)\), by their bounded
RMS norms and the Euclidean discrepancy bound. A strict full initial
Gram margin and budget margin therefore initialize all these cavities.
This is the extra argument needed to make the source's initialization
claim uniform in fixed-size deletions.

## 3. Reconstruction of scalar absorption

For an interior neuron, let \(G_{\delta,i}\) and \(G_{h,i}\) be the
nonnegative singleton-cavity Gaussian suprema defined in the candidate.
Set \(u_i=K_i^j/S\), and denote by \(\epsilon_n=o(1)\) its scalar
reinsertion remainder, at fixed \(S,B\). The candidate's equations
(3)--(4) are exactly
\[
 u_i\le G_{\delta,i}/S+A(1+Z_i^j)+\epsilon_n,\qquad
 Z_i^j\le G_{h,i}+D u_i+\epsilon_n,
\]
where
\[
 A=C_1(1+S^2B),\qquad D=C_2S^2(1+S^2\sqrt B).
\]
Take \(B\ge1\), then impose \(S^2B\le1\).
It follows that \(A\le2C_1\) and \(D\le2C_2S^2\).
The further choice \(S^2\le(8C_1C_2)^{-1}\) gives \(AD\le1/2\).
Substitution, with no probabilistic step, yields
\[
 u_i\le2G_{\delta,i}/S+2A(1+G_{h,i})+o(1),\qquad
 Z_i^j+u_i\le C(1+G_{h,i}+G_{\delta,i}/S)+o(1).
\]
The last constant is independent of \(B\) and the number of deletions.
The smallness threshold may depend on \(B\), as intended.

At the first layer, the initialized finite-dimensional Gaussian row
replaces \(G_{h,i}\), and the incoming learned row gives the same
\(CS^2u_i\) feedback. At the top, integration of the readout equation
gives \(K_i^L/S\le C(1+Z_i^L)\). Substituting it into the top forward
inequality and taking the scalar feedback coefficient at most \(1/2\)
gives \(Z_i^L+K_i^L/S\le C(1+G_{h,i})+o(1)\).
Both endpoint layers therefore satisfy the same kind of bound.

## 4. The normalized forward trace bound

This paragraph verifies the trace estimate assuming the response
expansion itself. Use the mobility-rescaled parameter coordinates
\(\Theta=(W^1,\sqrt n W^2,\ldots,\sqrt n W^L,w)\).
Every retained forward map \(C_a=D_\Theta h_a^{j-1}\) has operator
norm at most \(C\): a hidden matrix perturbation enters as
\(U_H h/\sqrt n\), and \(\|h\|\le C\sqrt n\).
Bounded activation values are unnecessary here.

Let \(U_0(t,s)\) be the contraction generated by the negative Gram part
of the variational equation, \(J(t,s)\) its complete propagator, and
\(A(s)\) the residual-Hessian term per unit residual activity.
The checked endpoint computation, using the carrier part of the joint
budget, gives for \(q\ge2\)
\[
 \|A(s)\|_{q,n}\le C(1+S q B^{1/q}),\qquad
 \|T\|_{q,n}=n^{-1/q}\|T\|_{\mathcal S_q}.
\]
The normalization is by width \(n\), not by the parameter dimension.

Expand \(J-U_0\) in Duhamel insertions. For the term with \(r\ge1\)
Hessian factors, use Schatten Hölder with exponent \(2r\) and
contractivity of every \(U_0\). The normalized Hilbert--Schmidt norm is
bounded by
\[
 \frac{(CS)^r}{r!}
       [1+2Sr B^{1/(2r)}]^r
 \le \frac{(CS)^r}{r!}
       +\sqrt B\,\frac{(CS^2)^r r^r}{r!},
\]
after increasing the fixed constant \(C\). Summation is valid for
sufficiently small \(S\), independently of \(B\), and yields
\[
 \|J(t,s)-U_0(t,s)\|_{2,n}\le C(S+S^2\sqrt B).
\]
Since the endpoint maps have rank at most \(n\) and bounded operator
norm, their normalized trace pairing satisfies
\[
 \frac1n\left|\operatorname{tr}
     C_b(t)J(t,s)C_a(s)^\top\right|
 \le C(1+S+S^2\sqrt B)
 \le C(1+S^2\sqrt B).
\]
Integration against \(|r_a b_{a,i}|\), with
\(|b_{a,i}|\le C K_i^j\), costs at most \(CS K_i^j\).
This is the coefficient in the candidate's forward inequality.
The higher endpoint trace in its backward inequality remains the
checked response-modulus trace, multiplied by the actual forward
control bound \(C(1+Z_i^j)\).

This calculation does not establish the control-uniform remainder or
justify a response expansion for the actual coupled insertion. Those
are supplied by the checked local dependency in Section 8.

## 5. Gaussian references and projected differences

Each reference cavity must be defined on its own stop, determined by
retained variables alone. On failed own initialization set all reference
coefficient paths to zero. This makes the conditional Gaussian estimates
valid for every retained configuration.

For an incoming normalized Gaussian row \(y\), the physical tube gives
\(\|h(t)\|/\sqrt n\le C\). With residual activity rescaled to \([0,1]\),
the forward path has a uniform Lipschitz modulus in normalized
Euclidean norm. The conditional Gaussian metric therefore has bounded
diameter and covering numbers at most \(1+C/\epsilon\).
Gaussian chaining and concentration give, for each fixed \(\lambda\),
\[
 \mathbb E\!\left[
       e^{\lambda\max_a\sup_t|y^\top h_a(t)|}
       \,\middle|\,\text{retained cavity}\right]\le C_\lambda,
\]
independently of \(B,n\).
The finite number of data points only changes constants.

For the outgoing row pairing with \(\delta/S\), the checked backward
modulus and entropy estimate instead give
\[
 \mathbb E\!\left[
       e^{\lambda\max_a\sup_t|x^\top\delta_a(t)|/S}
       \,\middle|\,\text{retained cavity}\right]
 \le L_\lambda(2B),\qquad L_\lambda(2B)=B^{o(1)}
\]
as \(B\to\infty\), uniformly in sufficiently small \(S\).
Both coefficient paths may be correlated with each other; their
conditional estimates still hold. For a common cavity the omitted
incoming/outgoing roots are themselves independent.

For a singleton/common-cavity difference, project the entire difference
path onto the deterministic Euclidean ball of radius
\(\sqrt n D_{n,p}\). Its radius is \(D_{n,p}\) in the Gaussian metric.
The Euclidean radius need not tend to zero.
Projection is nonexpansive and preserves independence from the omitted
Gaussian vector, since both original reference paths omit that vector.
If the two paths use different activity clocks, use the sum of the
clocks to parameterize their difference.

Its conditional Gaussian supremum \(E_{n,p}\) has mean bounded by
\[
 C D_{n,p}\sqrt{\log(e+H_B/D_{n,p})}
\]
and sub-Gaussian fluctuations of scale \(CD_{n,p}\), where \(H_B\)
is a fixed modulus constant at the chosen \(B,S,p\).
Hence for every fixed \(\lambda\),
\(\mathbb E e^{\lambda E_{n,p}}\to1\).
On the local comparison event projection does not change the difference
over the common prefix. This is the appropriate unconditional
replacement for conditioning on the root-dependent full stop.

## 6. Layerwise moment closure and order of limits

Fix a layer \(j\) and a positive integer \(p\). Delete only neurons in
that layer. For a distinct \(p\)-tuple use a common cavity omitting all
of them. Conditional on that cavity, its \(p\) root pairs are
independent. The scalar shift and absorption coefficient come from
singleton insertion and are independent of \(p\); common-cavity
comparison contributes only the preceding vanishing projected errors.

Combining the scalar bound with the conditional Gaussian estimates
gives a moment base
\[
 D(B)=C_\eta L_{C\eta}(2B)^{c}=B^{o(1)}
\]
for a fixed constant \(c\). A fixed Hölder split can increase the
constant \(C\eta\) and change \(c\), but neither depends on \(p\).
One explicit way to handle the sum of projected errors is a
Cauchy--Schwarz split: use coefficient \(2C\eta\) for the independent
main factors and exponential moment order proportional to \(p\) for
each error. The latter moments converge to one for every fixed \(p\).
The resulting main base is still independent of \(p\).

Collision tuples have at most \(p-1\) distinct indices. There are
\(O_p(n^{p-1})\) of them; higher fixed exponential moments bound their
contribution after division by \(n^p\) by \(o(1)\). Their constants may
depend on \(p\), since \(p\) is fixed while \(n\to\infty\).

The stopped budget is bounded by \(B\) on a successful full start, so
superpolynomial local exceptional probabilities are harmless in this
moment estimate. If a separate coordinate cap is used before the budget
stop, the same conclusion follows from its polynomial bound and the
superpolynomial exception probability. Failed initialization is removed
as a separate event with probability tending to zero.

First establish the pathwise insertion upper bound on the full good
event. Then remove its indicator from the nonnegative Gaussian upper
bound. This removal is justified because the reference estimates hold
for every retained configuration, including failed initializations
under the zero-path convention. It follows that
\[
 \limsup_{n\to\infty}
 \mathbb E\!\left[{\bf1}_{\mathrm{good\ start}}
                  H_j(T\wedge\tau)^p\right]\le D(B)^p.
\]
An initialization indicator may equivalently be kept separately on the
left. The initial/full stopping indicators must not be placed inside
an unjustified conditional Gaussian law.

If the budget is hit before \(T\), continuity gives \(H=B\), and some
layer satisfies \(H_j\ge B/L\). Markov's inequality and a union over
the fixed \(L\) layers give
\[
 \limsup_{n\to\infty}
 \mathbb P(\tau_{\mathrm{budget}}\le T)
 \le L\left(\frac{L D(B)}{B}\right)^p.
\]
Choose \(B\) large enough that \(L D(B)<B\), also meeting the initial
budget margin. Then choose \(S>0\) small enough for the scalar and local
smallness conditions. With these choices fixed, first let \(n\to\infty\)
for each fixed \(p\), and only then let \(p\to\infty\).
There is no need to let the label threshold or budget depend on \(p\).

Cavity budgets cannot be hit first: on the common local event,
coordinate running maxima differ by \(o(1)\), and
\[
 H_{\mathrm{cavity}}(t)\le
      e^{\eta o(1)(1+1/S)}H_{\mathrm{full}}(t)<2B
\]
while \(H_{\mathrm{full}}\le B\). The same comparison transfers
logarithmic coordinate margins. This uses fixed \(S>0\), as throughout.
After excluding the budget stop, the singleton Gaussian bounds yield
\(\max Z_i^j=O_{\mathbb P}(\sqrt{\log n})\) and
\(\max K_i^j=O_{\mathbb P}(S\sqrt{\log n})\) up to \(T\).

## 7. All-time consequence

The physical tube is valid for all time independently of this
finite-horizon budget. Its raw coordinate derivative bounds give
post-\(T\) carrier variation at most \(C n S e^{-\kappa T}\)
(a looser fixed-\(S\) bound is sufficient). Taking
\(T=c\log n\), \(c\kappa>1\), makes this vanish.
The forward tail is no larger. Thus the completed local insertion lemma,
together with the above probability argument, gives the needed
all-time \(O_{\mathbb P}(\sqrt{\log n})\) dense carrier maximum.
The already proved deterministic tracking implication then
supplies strict root-width prediction error at
\(q=n^{1/4}\exp(O(\sqrt{\log n}))=n^{1/4+o(1)}\).

The originally missing local step has now been supplied and reconciled
with every hypothesis in Section 1, as detailed next. The theorem retains
its fixed-depth, fixed-data, initial Gram-gap, and small-label assumptions.

## 8. Integrated local-source reconstruction and final reconciliation

The complete 442-line UNBOUNDED_INSERTION_CHECK.md was read at initial
hash b9bfdd910f3dd103feaf1e9a94a09db782dc3cda63b9354142d8fb5585def061.
Its mathematical content was reconstructed for consistency with the
conditional inputs above. The final formatting/reconciliation version
has hash bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578;
its amended passages were checked. The coordinating author separately
reconstructed both the bounded local lemma and this extension with PASS,
recorded in DEPTH_INSERTION_CHECK.md. The bounded source's final hash is
e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478.

Here is the exact match to the five hypotheses of Section 1.

First, bounded activation values enter the bounded local calculation only
through feature RMS and deleted scalar controls. For the former,
\[
 \|(U_H/\sqrt n)h\|_2\le C\|U_H\|_F,\qquad
 \|\Delta h\|_2\le C\|\Delta z\|_2.
\]
Every cross-matrix term \((\Delta H/\sqrt n)\Delta h\) retains its
factor \(n^{-1/2}\), and every scalar Taylor remainder uses bounded
second or third derivatives. A gradient block
\(\delta h^\top/\sqrt n\) uses the same RMS estimates for its linear
terms; its quadratic term retains the same small factor.
The lower reverse-probe Hessian uses derivative maps and probe carriers
rather than bounded activation coordinates.
Thus the bounded proof's split between linear coordinate variations and
the unknown Euclidean remainder remains valid. Logarithmic scalar
controls change only powers of \(\log n\), leaving the numerical
exponent margins intact. It supplies retained preactivation and carrier
errors \(O_r(n^{-1/30})\), and response-vector errors at most
\(C_r n^{1/100}\), with superpolynomial failure.

Second, the actual omitted weight updates are
\[
 \|\Delta W^{j+1}_{:,i}\|_2
       \le CS^2(1+Z_i)/\sqrt n,\qquad
 \|\Delta W^{j\top}_{i,:}\|_2
       \le CSK_i/\sqrt n.
\]
Multiplication by the forward and reverse controls therefore gives
small sources of size at most
\[
 \frac{C_r}{\sqrt n}\sum_{i\in I}
       [S^2(1+Z_i)^2+SK_i^2]
 \le C_r n^{-1/2}(\log n)^C
\]
on the joint stop. They may be adaptive; the error estimate is pathwise
and uses only their norm.

Third, the Gaussian event is uniform over the full logarithmic control
class. The deterministic trace calculation is then performed for each
control with its actual amplitude:
\[
 |a_i|_{\infty,[0,t]}\le C(1+Z_i(t)),\qquad
 |b_i|_{\infty,[0,t]}\le CK_i(t).
\]
Only the centered Gaussian fluctuation is approximated by the net;
the deterministic amplitude dependence is not replaced by a global
logarithmic cap. This supplies exactly the two scalar inequalities
reconstructed in Section 3. The forward trace estimate independently
rederived in Section 4 matches the local source's Schatten calculation.

Fourth, the resulting preactivation and carrier comparisons give the
joint stop transfer, while the \(C_r n^{1/100}\) vector comparisons
give normalized Gaussian radii \(C_r n^{-1/2+1/100}\) for both
incoming-row forward and outgoing-column backward references.
The independent full-path projection construction in Section 5 therefore
applies exactly. Incoming and outgoing roots remain independent
conditional on their common same-layer cavity. All moment bases used in
Section 6 consequently remain independent of moment degree.

Fifth, the top deletion must include the offset multiplying its reverse
force. In the weighted notation, let
\[
 r_a^0=\mathcal F_a^{\rm ret}/n-y_a,\qquad
 d_a=\frac1n\sum_{i\in I}w_i h_{a,i}^L,\qquad
 q_a=\sum_{i\in I}W^{L\top}_{i,:}\delta_{a,i}^L .
\]
The exact retained equation is
\[
 \dot\Theta=-2\sum_a p_a(r_a^0+d_a)
       [\nabla_\Theta\mathcal F_a^{\rm ret}
           +D_\Theta h_a^{L-1}{}^\top q_a].
 \tag{F}
\]
The final main source now includes (F). Its offset terms have norms
\[
 |d_a|\|\nabla\mathcal F_a^{\rm ret}\|_2
       \le n^{-1/2}\operatorname{polylog}n,\qquad
 |d_a|\|D_\Theta h_a^{L-1}{}^\top q_a\|_2
       \le n^{-1}\operatorname{polylog}n .
\]
Integration through \(T=O(\log n)\) and amplification by
\(n^{1/1000}\) leave both below the local remainder threshold.
No derivative or Gaussian-independence assumption on this small
adaptive offset is needed. The reverse force without the offset is
retained as an essential Gaussian source. Readout integration gives
\(K_i^L\le CS(1+Z_i^L)\), completing the top scalar absorption.

The final main source was also reread at
e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713.
Its completed-status statement, weighted residual definitions, exact
top equation, local references, and unconditional probability conclusion
agree with these reconstructions. The original conditional report has
therefore been completed, rather than treating an assumed insertion
estimate as a proved theorem.

**Final integrated verdict:** PASS for fixed-depth activations in
\(C^3\) with globally bounded first three derivatives, a positive initial
feature-Gram gap, and sufficiently small fixed labels. The joint
finite-width probability argument and the checked local estimates prove
an all-time dense carrier maximum \(O(S\sqrt{\log n})\) on events of
probability tending to one. The deterministic comparison gives strict
root-width error at \(q=n^{1/4}\exp(O(\sqrt{\log n}))\).
Automatic Gram conditions for nonaffine activations and the listed
examples are supplied by the separate activation check.
