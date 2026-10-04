# Independent check of separate training-sample carrier budgets

2026-10-04. Scoped internal reconstruction of the supervisor's proposed
budget change, completed without reading the concurrently authored
derivation. Complete additional inputs were the expressly authorized
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`, and
`DEPTH_CAVITY_PROBABILITY_CHECK.md` in
`studies/dense_cutoff_population_rate_20261001/`, and this study's
`DATASET_LABEL_DEPENDENCE.md`. The already completed current-study inputs
were `DEEP_COMPLEX_SOURCE.md`, `DEEP_ACTIVATION_EXTENSION.md`,
`DATASET_SOURCE_CONSTANTS.md`, and `DATASET_MAXIMUM_REFINEMENT.md`.
References outside this scope were not followed. Unrelated appended
unbounded-activation results were not audited. No experiments or Git
operations were performed.

**Verdict: PASS for the changed interfaces.** For each fixed finite
dataset, the real carrier proof and the complete complex-source proof
close with separate empirical budgets for each training sample. Their
budget and activity constants can then be chosen independently of the
sample count. Coupled to the allowed deterministic fitting theorem,
a sufficient label condition for the full analytic source construction is

\[
                         0<Y\le c\lambda,
\qquad
\lambda=\min\{1,\lambda_{\min}(Q^{(L)})/m\}.
\tag{1}
\]

Here \(c>0\) depends only on fixed input dimension, depth, unit input
radius, activation strip width and bound. The earlier additional factor
\(\exp\{-C\sqrt{\log(em)}\}\) is unnecessary in this proof. This is
a sufficient-bound improvement, not a necessity or optimality statement.

The argument keeps \(m\) fixed before the width limit. Width thresholds
can depend on \(m\), the gap, fixed positive label magnitude, confidence,
and the fixed moment degree chosen to reach that confidence. It does not
prove one common width threshold for growing datasets.

## 1. Model, physical input, and the new proof budgets

The network and mobilities are the canonical ones of the allowed sources:

\[
z_a^{(1)}=Av_a,\quad z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},
\quad h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),
\quad f_a=w^\top h_a^{(L)}/n,
\]
\[
k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
\quad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\tag{2}
\]

The residual is \(r_a=f_a-y_a\), its RMS is
\(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\), and
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\). The activations are bounded and
holomorphic on a common fixed horizontal strip, real on the real axis.
The covariance \(Q^{(L)}\) in (1) is defined by

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\qquad Z\sim N(0,Q^{(\ell-1)}).
\tag{3}
\]

The deterministic theorem in `DATASET_LABEL_DEPENDENCE.md`, with the
usual strict initialization margins, supplies a common physical tube
for the full network and every fixed-size rectangular cavity under
\(Y\le c\lambda\). Its rate is \(\kappa=c_\kappa\lambda\), and
\(S=C_0Y/\lambda\) bounds total residual activity. In particular

\[
\rho(t)\le Ye^{-\kappa t},\quad
\|w(t)\|_\infty\le CS,\quad
\|W^{(\ell)}(t)\|_{\mathrm{op}}\le C,\quad
\max_{a,\ell}\frac{\|k_a^{(\ell)}(t)\|_2}{\sqrt n}\le CS.
\tag{4}
\]

These constants are structural, not sample-count constants. Rectangular
cavities retain normalization \(n\); their strict gap margins transfer
for each fixed deletion count at sufficiently large width.

Fix a structural \(\eta>0\). For a real stopped interval or one of the
nested complex time domains \(\mathcal D\), define

\[
H_a(\mathcal D)=\frac1n\sum_{\ell<L}\sum_i
\exp\left\{\frac\eta S
                \sup_{t\in\mathcal D}|k_{a,i}^{(\ell)}(t)|\right\},
\qquad H(\mathcal D)=\max_{a\le m}H_a(\mathcal D).
\tag{5}
\]

Stop the full proof domain at \(H=B\), and every cavity at its own
\(H^{-I}=2B\). Query pole and response caps in the complex proof are
unchanged. At initialization every \(H_a=L-1\). Choose \(B>L\).
These are proof stops only; the actual training equations are unchanged.

The old budget averaged \(\exp\{\eta\max_a\sup|k_a|/S\}\) over neurons.
Equation (5) averages separately for each sample, then takes the maximum.
It is weaker, so the deterministic and probability uses require the checks
below rather than a claim that the old budget is automatically bounded.

## 2. Coordinate, moment and cutoff estimates need only one sample

Before the new full or cavity stop, every term of its nonnegative sum is
bounded by its total budget. Thus, simultaneously for all samples,

\[
\sup_{a,\ell,i,t}|k_{a,i}^{(\ell)}(t)|
\le\frac S\eta\log(2nB)=O(S\log(en)).
\tag{6}
\]

For each fixed sample \(a\), layer \(\ell<L\), and real \(u\ge2\),
\(x^u\le(u/e)^ue^x\) gives

\[
\left(\frac1n\sum_i\sup_t|k_{a,i}^{(\ell)}(t)|^u\right)^{1/u}
\le C S u(2B)^{1/u}.
\tag{7}
\]

The normalized second-moment bound \(CS\) in (4) is available separately,
without a factor involving \(B\). The top carrier \(w\) has the
deterministic coordinate bound in (4), so it needs no stochastic budget.

For a physical cutoff \(SR\), the same fixed-sample exponential estimate
gives

\[
\left(\frac1n\sum_i |k_{a,i}^{(\ell)}(t)|^2
              \mathbf1_{\{|k_{a,i}^{(\ell)}(t)|>SR\}}\right)^{1/2}
\le C_\eta S\sqrt{2B}\,e^{-c_\eta R}.
\tag{8}
\]

For example, with \(x=|k|/S\), bound
\(x^2\mathbf1_{x>R}\le C_\eta e^{\eta x}e^{-(\eta/2)R}\)
and sum. The cutoff is applied to the sample whose backward gate is
being subtracted, not to the union of exceptional neurons for all samples.
Hence no factor \(m\) appears in (8).

The local insertion controls, their coordinate Lipschitz bounds, their
learned row/column remainders, and the nonlinear retained-coordinate
bootstrap use (6) and the physical RMS bounds. Those hypotheses are
unchanged. The control net still has fixed sample count in its entropy
constant. This affects the eventual width threshold, not the structural
smallness condition on \(S\).

## 3. Mixed-sample Hessian and complex probe traces still close

The explicit Hessian in the allowed cavity source is a sum of bounded-map
conjugations of **one** carrier diagonal of sample \(a\), plus
rank-\(O_L(n)\) bounded terms. It has no product of two reference carriers
in a single displayed Hessian term. Consequently (7) supplies, uniformly
in the sample index,

\[
\|D^2\mathcal F_a\|_{u,n}
\le C[1+Su(2B)^{1/u}],
\qquad \|D^2\mathcal F_a\|_{2,n}\le C,
\tag{9}
\]

where \(\|T\|_{u,n}=(n^{-1}\operatorname{tr}|T|^u)^{1/u}\), and
\(\mathcal F_a=n f_a\). The corresponding response endpoint
\(B_a=D_\Theta\delta_a^{(j+1)}\) obeys the same higher-moment estimate
and a structural normalized Hilbert--Schmidt bound.

The residual-Hessian sum is a normalized mixture. Set
\(d\mu=(2/m)\sum_a|r_a(t)|\,dt\) on real time. Where its density is
nonzero, the remaining Hessian coefficient is a linear combination of
the matrices in (9) with sum of coefficient magnitudes one. Its Schatten
norm has the same bound by the triangle inequality. At zero density
define that coefficient to be zero. The same argument on complex contours
uses absolute contour length and coefficient phases. Total activity is
\(O(S)\); normalized sample averages introduce no factor \(m\).

Now allow the two endpoints and all Hessian insertions in a Dyson term
to carry different sample indices. Normalized Schatten Hölder gives

\[
\frac1n|\operatorname{tr}(T_0T_1\cdots T_{h+1})|
\le\prod_{j=0}^{h+1}\|T_j\|_{h+2,n}.
\tag{10}
\]

Each factor individually satisfies (9), regardless of which sample
generated it. Thus the term with \(h\ge1\) residual-Hessian insertions
is bounded by the unchanged expression

\[
\frac{(CS)^h}{h!}
\left[C\{1+S(h+2)(2B)^{1/(h+2)}\}\right]^{h+2}.
\tag{11}
\]

No exponential moment of a pointwise maximum over samples is used in
(10). The contractions on real time and the one factor
\(e^{Cr_n}\) for total complex/backward contour length are unchanged.
The \(h=0\) term uses the two structural Hilbert--Schmidt endpoint
bounds. The series calculation from the allowed sources therefore keeps
the singleton shift

\[
\sup_{t\text{ in common prefix}}
|k_{a,i}^{(j)}(t)-x_i^\top\delta_a^{(j+1),-i}(t)|
\le CS(1+S^2B)+o(1),
\tag{12}
\]

uniformly in \(a\). Its constant is the singleton constant, independent
of the later empirical moment degree and common-cavity deletion count.

The complex forward-response endpoint has the exact decomposition
\(D Q_b=D h\,D^2\mathcal F_b+D^2h[\,\cdot\,,\nabla\mathcal F_b]\).
Its additional carrier-dependent bound involves sample \(b\) only and
is supplied by (7); the lower forward-response cap is unchanged. The
other endpoint \(C_a=D h_a\) is bounded. Hence the analogous trace with
endpoint samples \(a,b\) and arbitrary residual insertion samples also
uses (10) and closes with its previous bound \(C(1+A_p)\). Angular
endpoints use only their previous lower angular caps. Incoming-root
adjoint probes still have their separate Gaussian coordinate estimates.
Their conditional reference operators and nonlinear remainder estimates
need (6) and these samplewise bounds, not the old combined budget.

Thus the triangular forward/angular recursions, query pole exclusion,
complex physical operator/readout bounds, and the augmented insertion
event remain valid. There is no hidden place in these trace calculations
where one must first form \(\max_a|k_{a,i}|\) at each neuron.

## 4. The Gaussian reference moment is now structural

Fix a sample \(a\) and one cavity. Normalize real residual activity by
\(u(t)=\mu([0,t])/S\). Its total range is bounded structurally. For
\(v=|u(t)-u(s)|\le1\), the physical speed estimates give

\[
\|\Delta w\|_2/\sqrt n\le CSv,\quad
\|\Delta W\|_{\mathrm{physical}}\le CS^2v,\quad
\|\Delta z_a^{(\ell)}\|_2/\sqrt n\le CS^2v.
\]

At a changed backward gate of this sample, split its reference carrier
at \(SR\). The low part contributes \(CS^3Rv\), and (8) bounds the
high part by \(CS\sqrt{2B}e^{-c_\eta R}\). All remaining backward
differences propagate through bounded operators or cost \(CS^3v\).
Choose

\[
R=C_\eta[1+\log(e+B)+\log(1/v)].
\]

Descending through fixed depth reproduces

\[
\frac{\|\delta_a^{(\ell)}(t)-\delta_a^{(\ell)}(s)\|_2}{S\sqrt n}
\le Cv[1+S^2\log(e+B)+S^2\log(1/v)]
\le C\sqrt v,
\tag{13}
\]

provided \(S\le c\) and \(S^2\log(e+B)\le c\). At \(v=0\) use
continuity and the unchanged parameter state. Although the parameter
motion is driven by all labels, its bound used the normalized activity
measure; the carrier cutoff in this step belongs only to sample \(a\).

Freeze each cavity reference at its **own** stop, using zero reference
on its own failed initialization event. These choices are measurable in
retained initialization. For an independent omitted outgoing root
\(x_i\sim N(0,I_n/n)\), define

\[
Z_{a,i}^{-I}=\sup_t|x_i^\top\delta_a^{(j+1),-I}(t)|/S.
\]

Conditional on the cavity, (13) gives Gaussian metric covering number
\(C\epsilon^{-2}\), bounded diameter and zero initial value. The
dyadic Gaussian argument therefore gives

\[
\Pr\{Z_{a,i}^{-I}>C(1+z)\mid\mathrm{cavity}\}\le Ce^{-cz^2},
\qquad
\mathbb E[e^{qZ_{a,i}^{-I}}\mid\mathrm{cavity}]
\le\mathcal L_{\mathrm{single}}(q)<\infty.
\tag{14}
\]

Every fixed \(q\) is allowed. These constants are independent of
\(m,B\), width and fixed deletion count, under the displayed smallness
conditions. This is the one-sample estimate explicitly isolated in
`DATASET_SOURCE_CONSTANTS.md`; unlike its older maximum estimate,
there is no union over samples in (14).

For complex time, write
\(\delta_a(t+is)=\delta_a(t)+[\delta_a(t+is)-\delta_a(t)]\).
The allowed complex proof bounds the normalized bracket radius by
\(D_n=Cr_n\ell_n=o(1)\), with two-parameter derivative bound
\(C\ell_n\). These estimates use the uniform coordinate cap (6),
so they remain valid. The bracket Gaussian mean is
\(CD_n\sqrt{\log(C\ell_n^C/D_n)}=o(1)\), after the existing width
threshold absorbs the fixed horizon prefactor \(\lambda^{-1}\).
Its fixed exponential moments are structurally bounded. Apply
Cauchy--Schwarz to the real and complex contributions for this one
sample. This extends (14), with a structural enlargement of
\(\mathcal L_{\mathrm{single}}\), to the complete stopped complex
domain. No sample maximum is taken inside that exponential moment.

## 5. Cavity survival and root independence are preserved

The original local insertion proof, with the hypotheses verified above,
gives uniform retained-coordinate error
\(\epsilon_{n,r}=C_rn^{-1/30}\) on the common full/cavity prefix.
For each sample separately, running suprema then give

\[
H_a^{-I}\le e^{\eta\epsilon_{n,r}/S}H_a+O(r/n).
\]

Taking a maximum over the fixed samples yields

\[
\max_aH_a^{-I}
\le e^{\eta\epsilon_{n,r}/S}\max_aH_a+O(r/n)
\le B+o(1)<2B.
\tag{15}
\]

Thus a cavity cannot hit its own budget before the full stop. The
unchanged retained query-coordinate comparisons likewise preserve its
doubled pole and response caps. Strict initialization margins transfer
uniformly to every fixed-size cavity as before. For fixed \(S>0\),
the factor \(e^{\eta\epsilon_{n,r}/S}\) tends to one; the threshold can
depend on \(S\), as the original proof already allowed.

Stopping a cavity when the maximum of all its sample budgets is attained
does not compromise root independence: the entire stopped reference is
still a function of retained initialization only. The full stop can
depend on omitted roots, so it is never used as a conditioning event.

The comparison of singleton and fixed-block references is also unchanged.
Their complete frozen difference is independent of the omitted root
\(x_i\). Project that entire difference onto the deterministic Euclidean
ball of radius \(C_rn^{1/100}\), not just its successful prefix.
The projected difference remains independent of \(x_i\), retains the
samplewise modulus (13), and agrees with the original difference on the
successful full prefix. Its Gaussian radius is
\(O(n^{-1/2+1/100})\). The real chaining estimate, or the allowed
complex polynomial grid, therefore gives the same \(o(1)\) pairing
error. Unioning those auxiliary events over finitely many samples and
all deletion sets of a fixed size preserves their superpolynomially
small failure. It changes width thresholds only.

## 6. Fixed-sample moments, collisions, and the final sample union

Let \(\sigma\) denote the full stop, and let \(\mathcal G_n\) be the
same strict full initialization event, defined independently of the
empirical moment degree. For each sample and layer define

\[
H_{n,a,j}=\mathbf1_{\mathcal G_n}\frac1n\sum_i
\exp\left\{\frac\eta S\sup_{t\in\mathcal D_\sigma}
                         |k_{a,i}^{(j)}(t)|\right\}.
\tag{16}
\]

Fix an integer \(p\ge1\) independently of width. Expand
\(H_{n,a,j}^p\) while keeping **one sample \(a\) fixed**. For a tuple
of \(p\) distinct neuron indices, use their common same-layer cavity.
Equation (12) and the common-cavity pairing comparison bound the product
by

\[
e^{pC\eta(1+S^2B)+o(1)}
\prod_{i\in I}e^{\eta Z_{a,i}^{-I}}.
\]

This bound is first established pathwise on the successful common prefix.
Then discard the full good-event and stop indicators before taking
conditional expectation of the nonnegative right side. Conditional on
the common cavity, its outgoing roots are independent, even though they
all test the same sample response. Equation (14) bounds the expected
product by

\[
[\mathcal L_{\mathrm{single}}(\eta)
 e^{C\eta(1+S^2B)}]^p+o(1).
\tag{17}
\]

The singleton shift constant has not been replaced by a constant depending
on \(p\). This is necessary to keep the base in (17) independent of
moment degree.

Collision tuples have fewer than \(p\) distinct indices and multiplicities
\(d_1+\cdots+d_r=p\). Their expected products use the finite constants
\(\mathcal L_{\mathrm{single}}(d_i\eta)\). There are
\(O_p(n^{p-1})\) such tuples, so their normalized contribution vanishes.
On the exceptional local event, the stopped \(H_a\) is at most \(B\);
its moment contribution is bounded by \(B^p\) times the failure
probability. Therefore

\[
\limsup_{n\to\infty}\mathbb E H_{n,a,j}^p
\le D(B,S)^p,
\qquad
D(B,S)=\mathcal L_{\mathrm{single}}(\eta)e^{C\eta(1+S^2B)}.
\tag{18}
\]

Minkowski over layers, without any independence assumption, gives

\[
\limsup_n\mathbb E\left(\sum_{j<L}H_{n,a,j}\right)^p
\le[(L-1)D(B,S)]^p.
\tag{19}
\]

Now choose a **structural** budget

\[
B>\max\{L,4(L-1)\mathcal L_{\mathrm{single}}(\eta)e^{C\eta}\}.
\]

Choose \(S\) structurally small so all local/trace conditions hold,
\(S^2\log(e+B)\le c\), and \(e^{C\eta S^2B}\le2\). These choices
are independent of sample count, confidence, width and moment degree.
They give \(q:=(L-1)D(B,S)/B<1\).

At a full budget hit some sample has \(H_a=B\). Only now apply a union
bound over samples and Markov's inequality:

\[
\limsup_{n\to\infty}
\Pr\{\mathcal G_n,\text{some sample budget hits }B\}
\le m q^p.
\tag{20}
\]

For each fixed finite \(m\), taking the infimum over fixed integers
\(p\) makes the right side zero. Width tends to infinity first at each
fixed \(p\); no theorem for growing deletion count is used. For a
specified confidence one can first choose a sufficiently large finite
\(p\), depending on \(m\) and confidence, and then take width large
enough for that choice. This changes no label or budget constant.

The real proof is run first to obtain its real carrier input. The same
argument then removes the complex budget using its one-sample complex
Gaussian moment. Their budgets and admissible \(S\) may be distinct
structural constants; take the smaller final activity allowance. Thus
the complex result does not assume a new real carrier theorem before
that theorem has been supplied.

## 7. Carrier maximum, source theorem and the label threshold

After real stop removal, singleton insertion and the one-sample Gaussian
tail can be unioned over \(m n(L-1)\) indices. A sufficiently large
structural constant gives

\[
\sup_{t\le T_n}\max_{a,j,i}|k_{a,i}^{(j)}(t)|
\le CS\sqrt{\log(en)}
\tag{21}
\]

with probability tending to one for each fixed \(m\). The factor \(m\)
affects how large width must be; it does not require changing the
constant in (21). The existing coarse physical tail estimate
\(CSn e^{-\kappa T_n}\) extends (21) to all time with
\(T_n=C_T\lambda^{-1}\log(en)\) and a structural sufficiently large
\(C_T\).

The complex proof has the same coordinate cap, Gaussian insertion event,
trace estimates and pole/response margins. Its source radius, coordinate
magnitudes and approximation degrees therefore remain those of the allowed
source theorem. The proof change removes the factor involving the sample
maximum from the budget selection; it changes neither the actual flow nor
the source family evaluated from it.

All remaining smallness requirements are now a fixed finite list of
structural conditions on \(S\), together with the independently proved
real fitting condition \(Y\le c\lambda\). Since
\(S=C_0Y/\lambda\), a sufficiently small structural coefficient in (1)
enforces the full list. In particular no condition \(S^2m\le c\) or
\(S^2e^{C\sqrt{\log(em)}}\le c\) remains. Those conditions belonged
to the superseded combined-sample budget selection.

## 8. Consequences and limits of the checked modification

This check establishes the improved sufficient label class (1) for both
the actual real carrier input and the full complex-source construction,
as an extension of the allowed local proofs. Existing autonomous
compression and comparison conclusions follow under their previously
checked source interfaces. Their width conditions and quantitative
comparison factors are not weakened by this budget argument.

If the separately completed initialization-geometry lemma gives

\[
m\le C[\log(e+1/\gamma)]^\beta,
\qquad Q^{(L)}\succeq\gamma I_m,\quad0<\gamma\le1,
\quad\beta=3(d-1)/2,
\]

then \(\lambda\ge\gamma/m\) and (1) immediately yield the conditional
gap-only sufficient corollary

\[
Y\le\frac{c'\gamma}{[\log(e+1/\gamma)]^{3(d-1)/2}}.
\tag{22}
\]

No \(\varepsilon\) loss is needed after the extra maximum penalty has
been removed. The initialization-geometry document is not changed by
this check. As before, replacing \(m\) by its largest value permitted
by the gap does not enlarge the numerical threshold for a fixed dataset;
the actual enlargement here is the removal of the additional factor
from the \(m\)-aware source label condition.

The decisive limitations are unchanged: fixed finite \(m,d,L\) before
width tends to infinity; fixed positive \(Y\) for the eventual threshold;
confidence implemented by a fixed moment degree before width; and
structural constants rather than a practical closed formula for the
complete width threshold. The new budget is a proof device and adds no
state or intervention to the trained network.
