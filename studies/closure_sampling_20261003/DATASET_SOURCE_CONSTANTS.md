# Dataset constants in the deep complex-source theorem

2026-10-04. Scoped quantitative audit. This is an internal derivation, not
an independent promotion review. The input scope is the complete current
`GENERAL_ANALYTIC_COMPRESSION.md`, `GENERAL_WEIGHTED_COMPARISON.md`,
`DEEP_COMPLEX_SOURCE.md`, and `DEEP_ACTIVATION_EXTENSION.md`, with the
explicitly authorized prior depth-cavity proof and its two named checks
available only to resolve its quantitative interfaces. No experiments or
changes to other files are part of this audit.

## Frozen initial assessment (before exchange)

The normalized limiting gap is
\(\lambda=\lambda_{\min}(Q^{(L)}/m)\), whereas the compression note uses
\(\gamma=\lambda_{\min}(Q^{(L)})=m\lambda\). Its logarithmic width
variable must therefore be written \(\ell_n=\log(en)\) in this audit.
Normalized sample averages in the physical equations suggest that the
deterministic fitting and comparison constants need no dataset geometry
beyond the input radius and this gap. However, the complex-source proof
adds a carrier exponential budget, a Gaussian supremum over all training
samples, and a weakly growing insertion propagator. Its actual sufficient
label condition cannot be inferred from real fitting alone.

In particular, Sections 7--8 of `DEEP_COMPLEX_SOURCE.md` leave the scalar
Gaussian moment \(\mathcal L_*(\eta_0)\) unexpanded. They choose the carrier
budget \(B\) above a multiple of that moment and then impose
\(S^2 B\lesssim1\), where \(S\asymp Y/\lambda\). The prior real Gaussian
path estimate must be checked to determine whether its constants are
uniform in datasets at fixed radius, sample count, and normalized gap, and
whether \(\mathcal L_*\) is polynomial or exponential in those parameters.
The initialized covariance argument can be strengthened from mere
continuity to a uniform quantitative estimate using bounded activation
derivatives, including at singular intermediate covariances.

The assessment above was recorded before reading other agents' findings
or exchanging scientific conclusions. The completed audit follows below.

## 1. Quantitative conclusion and conventions

Let the normalized inputs satisfy \(\|v_a\|_2\le R_x\), with
\(v_a=x_a/\sqrt d\); the compression theorem has \(R_x=1\). Suppose
every activation is bounded by \(B_\phi\) on the strip
\(|\operatorname{Im}z|<b\), is holomorphic there, and is real on the
real axis. Set

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}
 =\mathbb E\bigl[\phi_\ell(Z_a)\phi_\ell(Z_b)\bigr],
 \quad Z\sim N(0,Q^{(\ell-1)}),
\]
\[
 \lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}>0,
 \qquad Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
 \tag{1}
\]

The cap at one simplifies estimates; an uncapped gap differs only by
activation-dependent constants since its value is at most \(B_\phi^2\).
All constants denoted \(c,C\) below depend only on
\(d,L,R_x,b,B_\phi\), and may change between formulas. They do not
depend on the arrangement of the training inputs, their minimum angular
separation, the smallest eigenvalue of an intermediate covariance,
label direction, sample count, or width. These are bounds on constants,
not optimized numerical values. Bounds on the first four derivatives on
a narrower strip are supplied by
\(j!B_\phi(4/b)^j\).

A sufficient condition for the **full deep complex-source theorem and
its real carrier input**, not merely real fitting, is

\[
                         0<Y\le c\lambda^{3/2}.
 \tag{2}
\]

Under (2), its complex radius and coordinate bound can be chosen as

\[
 r_n=c\ell_n^{-(L+4)},\qquad
 \max |\text{source coordinate}|\le C\ell_n^{L+2},
 \qquad \ell_n=\log(en),
 \tag{3}
\]

on the time rectangle extending to
\(T=C\lambda^{-1}\ell_n\), with the same product angular strip as
the original theorem. In (3) the constants are uniform over the above
dataset class. For each fixed positive \(Y\), confidence, and fixed
values of the other displayed parameters, the required sufficiently
large width can also be taken uniformly over the datasets and label
directions. The existing argument does **not** give a stated practical
formula for this final width threshold or a result for growing
\(m,d,L\). Section 6 specifies the dependence and its limitations.

No geometric condition apart from the input bound and the final
normalized Gram lower bound is needed in this constant audit. Algebraic
conditions such as nonproportional inputs prove positivity but do not
provide a uniform positive numerical value of \(\lambda\).

## 2. Real physical estimates with normalized sample averages

Use the exact canonical model and mobilities in
`GENERAL_ANALYTIC_COMPRESSION.md`. Write
\(\rho(t)=m^{-1/2}\|y-f(t)\|_2\) and
\(s(t)=\int_0^t\rho(u)\,du\). The inequality

\[
 \frac1m\sum_a|y_a-f_a(t)|\le\rho(t)
 \tag{4}
\]

removes sample-count factors from the physical speed estimates. In a
fixed hidden-operator tube, zero initial readout and bounded activations
give

\[
 \|w(t)\|_\infty\le Cs(t),\quad
 \max_{a,\ell}\frac{\|\delta_a^{(\ell)}(t)\|_2}{\sqrt n}
 \le Cs(t),
\]
\[
 \frac{\|A(t)-A(0)\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
 \le Cs(t)^2.
 \tag{5}
\]

Forward subtraction at a training input gives
\(\|h_a^{(L)}(t)-h_a^{(L)}(0)\|_2/\sqrt n\le Cs(t)^2\).
For the normalized feature matrix
\(H(t)=[h_1^{(L)}(t),\ldots,h_m^{(L)}(t)]/\sqrt{mn}\),
its Frobenius norm is at most \(B_\phi\), and
\(\|H(t)-H(0)\|_F\le Cs(t)^2\). Consequently

\[
 \|H(t)^\top H(t)-H(0)^\top H(0)\|_{\rm op}
 \le Cs(t)^2.
 \tag{6}
\]

Take the initial normalized Gram gap with a fixed margin above
\(\lambda/2\). Requiring \(Cs(t)^2\le c\lambda\) preserves a
gap of order \(\lambda\). The tangent Gram dominates this feature
Gram, so the exact residual equation gives
\(\rho(t)\le Ye^{-\kappa t}\) with
\(\kappa=c_\kappa\lambda\) for a fixed positive
\(c_\kappa\). Define the proof activity bound, as in the source, by

\[
                         S=2Y/\kappa.
 \tag{7}
\]

Then \(s(\infty)\le S/2\). The conditions
\(S\le c\) and \(S^2\le c\lambda\) close the tube and (6).
The latter yields the conservative real-fitting requirement
\(Y\le c\lambda^{3/2}\). These estimates also apply to the weighted
compressed model and every fixed-size rectangular cavity, using the
inherited initial Gram margins. They do not use inverse selected masses.
This audit does not claim that the conservative real-fitting threshold is
optimal.

## 3. The Gaussian moment and the carrier budget

The potentially hidden constant is the conditional Gaussian exponential
moment in Section 7 of the real cavity proof and Section 7 of the complex
source proof. It can be made explicit enough to track all sample-count
dependence.

For one cavity let
\(\mu([s,t])=(2/m)\sum_a\int_s^t|r_a(u)|\,du\), where
\(r_a=f_a-y_a\), and use the normalized activity coordinate
\(u(t)=\mu([0,t])/S\). Equations (4)--(7) give a bounded total
range for \(u\), independently of \(m\) and \(\lambda\).
The real cavity proof's carrier cutoff calculation gives, for
\(v=|u(t)-u(s)|\le1\),

\[
 \frac{\|\delta_a(t)-\delta_a(s)\|_2}{S\sqrt n}
 \le Cv\{1+S^2\log(e+B)+S^2\log(1/v)\}
 \le C\sqrt v,
 \tag{8}
\]

provided \(S^2\log(e+B)\le c\) and \(S\le c\). Here \(B\)
is the carrier budget. The constants in (8) have no Gram denominator:
the normalization by \(S\), not by physical time, is essential.

For an independent omitted Gaussian root \(g\sim N(0,I_n/n)\),
fix a single training sample and set
\(Z_a=\sup_t|g^\top\delta_a(t)|/S\). Conditional on the cavity,
(8) gives covering number at most \(C\epsilon^{-2}\) at Gaussian
metric resolution \(\epsilon\); the process starts at zero and has
bounded variance. The dyadic-net argument stated in the source therefore
gives

\[
 \mathbb P\{Z_a>C(1+z)\mid\text{cavity}\}
 \le Ce^{-cz^2},\qquad z\ge0.
 \tag{9}
\]

Its constants are uniform in \(a,m,\lambda,B\), subject to (8).
Integrating the tail in (9) gives, for every fixed \(q\ge0\),

\[
 \mathbb E[e^{qZ_a}\mid\text{cavity}]
 \le C\exp(Cq+Cq^2).
 \tag{10}
\]

In particular there is no exponential dependence on \(m\) or
\(\lambda^{-1}\) inside the single-sample Gaussian moment. For
\(Z=\max_{a\le m}Z_a\), the elementary pointwise inequality
\(e^{q\max_a Z_a}\le\sum_a e^{qZ_a}\) gives

\[
 \mathbb E[e^{qZ}\mid\text{cavity}]
 \le mC\exp(Cq+Cq^2).
 \tag{11}
\]

This bound needs no independence between samples. Sharper bounds on a
Gaussian maximum could improve it; the factor \(m\) is sufficient here.

For the complex contour, the normalized extra response
\([\delta(t+is)-\delta(t)]/(S\sqrt n)\) has radius at most
\(D_n=Cr_n\ell_n\). Its two-parameter Gaussian covering estimate
in the source gives a mean supremum
\(CD_n\sqrt{\log(C\ell_n^C/D_n)}=o(1)\), and a bounded
fixed exponential moment, uniformly for large width. A factor
\(\lambda^{-1}\) from the time rectangle can enter the covering
constant, but its logarithm is absorbed by the width threshold; it does
not enter a power of \(\ell_n\). Apply Cauchy--Schwarz **for one
sample**, combine with (10), and then sum over samples as in (11).
Thus the complex moment in the source satisfies

\[
                         \mathcal L_*(\eta_0)\le C_0m
 \tag{12}
\]

for any fixed positive \(\eta_0\), with \(C_0\) depending only
on the parameters allowed for \(C\). This ordering avoids an
unnecessary second sample-count factor.

The singleton insertion shift is
\(CS(1+S^2B)+o(1)\); all its residual sums are normalized as in
(4). Its constant therefore has no hidden sample-count factor. The
fixed-block moment argument closes when

\[
 B>4(L-1)\mathcal L_*(\eta_0)e^{C\eta_0},\qquad
 C\eta_0 S^2B\le\log2.
 \tag{13}
\]

Choose \(B=C_Bm\), with \(C_B\) fixed sufficiently large. The
local variational amplification and the normalized trace series impose
additional fixed upper bounds on \(S\); their budget-dependent terms
are bounded under \(S^2B\le c\). Equation (8)'s logarithmic
condition is also implied after reducing \(c\), since \(m\ge1\).
Thus a sufficient complete list is

\[
 S\le c,\qquad S^2\le c\lambda,\qquad S^2m\le c.
 \tag{14}
\]

There is no dependence on the deletion count or the empirical moment
degree in this choice. Those quantities change the width threshold.

Before using the trace bound on \(Q^{(L)}\), (14) gives the explicit
sufficient form

\[
 Y\le c\lambda\min\{1,\sqrt\lambda,m^{-1/2}\}.
 \tag{15}
\]

Finally, each diagonal entry of \(Q^{(L)}\) is at most
\(B_\phi^2\), so

\[
 m\lambda\le\lambda_{\min}(Q^{(L)})
 \le\frac{\operatorname{tr}Q^{(L)}}m\le B_\phi^2.
 \tag{16}
\]

Under (2), \(S^2\le Cc^2\lambda\) and
\(S^2m\le Cc^2B_\phi^2\). Reducing the single constant in (2)
therefore enforces every condition in (14). This proves that the
conservative power \(\lambda^{3/2}\) suffices for the actual source
and carrier closure, not only for the preliminary real fitting tube.

## 4. Uniform source radius, magnitude, and approximation dimensions

With (14), the carrier stopping bound is
\(M_n\le CS\ell_n\) for widths large enough to absorb
\(\log B\). The forward-response recursion (25) in the complex
source proof has right-hand side bounded by

\[
 C\{S\ell_n+S\sqrt{\ell_n}
      +S^2\ell_n(1+A_p)+S^3\ell_n\},
 \tag{17}
\]

where \(A_p\) is the lower-layer response cap. Upward induction
gives caps \(C_\ell S\ell_n^{\ell+1}\), with constants uniform
under (14). The angular recursion (26) similarly gives caps
\(C_\ell\ell_n^{\ell+1}\). Its first-layer initialization bound
uses Gaussian row norms and the bounded derivatives of the sphere map;
their constants depend on \(d\), as allowed.

Moving vertically from real time and real query angles consequently
changes a preactivation's imaginary part by at most

\[
                  Cr_n(1+SY)\ell_n^{L+1}.
 \tag{18}
\]

Since \(SY\) is bounded uniformly under (2), choosing the first
constant in (3) small places (18) inside the activation strip. The
complex residual equation uses \(K/m\), whose operator norm is
bounded by the per-sample feature and response RMS bounds, so its short
vertical propagator also has a uniform bound. No propagation over the
long real interval is needed for this estimate.

The complex Gaussian correction in Section 3 has normalized derivative
bounded by
\(C(Y/S)(1+S^2\ell_n)\le C\ell_n\): here
\(Y/S=\kappa/2\asymp\lambda\le1\). This verifies the uniform
constant in its radius \(D_n\).

For the source magnitude, start from one fixed real sphere anchor,
whose initialized preactivation maximum is \(C\sqrt{\ell_n}\)
with high probability. Integrate the forward responses against total
residual activity \(CS\), and integrate angular derivatives along
bounded angular paths. Equations (17)--(18) give (3). The initialized
matrix source differs from the corresponding moving preactivation by
at most \(CS^2\ell_n\); the initialized transpose source has a
correction at most \(CS^3\), as in Section 9 of the source proof.
Thus the initialized matrix images share the same uniform magnitude
bound. This checks all four source families, in both orientations.

The real all-time carrier bound may likewise be written
\(\max|k|\le CS\sqrt{\ell_n}\), with uniform \(C\) once the
width threshold absorbs the union over \(m\) samples. Both the query
tail and the coarse carrier tail are controlled by taking
\(T=C\lambda^{-1}\ell_n\).

For illustration, take coordinate source tolerance \(\epsilon=n^{-1}\).
For each fixed positive \(Y\), the original comparison requirement
\(\epsilon\le Y\) holds for sufficiently large width. The
Bernstein-ellipse and Fourier-tail calculations in the compression note
then give degrees

\[
 p\le C\lambda^{-1}\ell_n^{L+6},\qquad
 J\le C\ell_n^{L+5},
 \tag{19}
\]

once \(n_0\) absorbs \(\log(\lambda^{-1})\) in the logarithmic
tail prefactors. There are a fixed number of query source families per
layer, and \(O(m)\) training-only backward families. With
\(a=d(L+5)+1\), the layer-space dimension can therefore be bounded by

\[
 R\le C\left\{\lambda^{-1}
       [\ell_n^a+m\ell_n^{L+6}]+d\right\}.
 \tag{20}
\]

The initialized training vectors add \(O(m)\), already absorbed in
(20). The initialized first-weight columns add \(d\). Positive
cubature gives \(O(R^2)\) neurons per layer, so retaining all small
matrices, masses, first weights, and data costs

\[
 C(R^4+dR^2)+O(md+m).
 \tag{21}
\]

For \(d\ge2\), \(a\ge L+6\), and the simpler upper bound is
\(C(1+m)^4\lambda^{-4}\ell_n^{4a}+O(md+m)\), with \(C\)
depending on the stated fixed structural parameters. This is a
conservative explicit dependence for retained storage; it is not a
claim that the displayed factors are necessary. The deterministic
comparison amplification remains finite for fixed data and grows at
most as \(\exp(C_{m,\lambda,Y}\sqrt{\ell_n})\). Thus the
stronger tolerance \(n^{-1}\) permits the final \(n^{-1/2}\)
error after another enlargement of \(n_0\), without changing (19).

## 5. Initialized Gram convergence needs no intermediate spectral gaps

The initialization statement in the original theorem uses continuity.
Bounded derivatives give a uniform quantitative replacement, including
singular covariances.

For a positive semidefinite \(m\times m\) covariance \(V\), let
\(\Phi_\ell(V)_{ab}=\mathbb E[\phi_\ell(Z_a)
\phi_\ell(Z_b)]\), with \(Z\sim N(0,V)\). Define
\(D_j=\max_\ell\|\phi_\ell^{(j)}\|_\infty\) on the real
axis, and \(A_\phi=B_\phi D_2+D_1^2\). Then

\[
 \|\Phi_\ell(V)-\Phi_\ell(U)\|_{\max}
 \le A_\phi\|V-U\|_{\max}.
 \tag{22}
\]

Here \(\|M\|_{\max}=\max_{a,b}|M_{ab}|\). To verify (22),
interpolate the two Gaussian covariances. For \(a\ne b\), the
function of the relevant two coordinates is
\(g(z_a,z_b)=\phi_\ell(z_a)\phi_\ell(z_b)\), with second
partial bounds \(B_\phi D_2,B_\phi D_2,D_1^2\). Differentiating
the Gaussian density along covariance interpolation and integrating by
parts twice gives

\[
 \frac d{dt}\mathbb E[g(Z_t)]
 =\frac12\sum_{i,j\in\{a,b\}}
       (V-U)_{ij}\,\mathbb E[\partial_{ij}g(Z_t)].
\]

The two diagonal terms and the two equal mixed terms give exactly the
constant in (22). For \(a=b\), use
\((\phi_\ell^2)''=2(\phi_\ell')^2+2\phi_\ell\phi_\ell''\).
If a covariance is singular, first add \(\varepsilon I\) to both
endpoints. The same bound is independent of \(\varepsilon\), and
bounded continuous Gaussian expectations converge as
\(\varepsilon\downarrow0\). This proves (22) without any inverse
covariance or intermediate eigenvalue lower bound.

Let \(\widehat Q^{(\ell)}=H_\ell(0)^\top H_\ell(0)/n\),
where \(H_\ell(0)\) has the training activation vectors as columns.
Conditional on the preceding layer, the rows are iid and every feature
product has magnitude at most \(B_\phi^2\). At each layer, the
conditional bounded-variable tail is

\[
 \mathbb P\left\{
 \|\widehat Q^{(\ell)}-
       \Phi_\ell(\widehat Q^{(\ell-1)})\|_{\max}>u
 \ \middle|\ \text{preceding layer}\right\}
 \le2m^2\exp\left(-\frac{nu^2}{2B_\phi^4}\right).
 \tag{23}
\]

The first layer has covariance \(Q^{(0)}\) exactly. Combining
(22)--(23) through all \(L\) layers, and setting
\(A_L=\sum_{j=0}^{L-1}A_\phi^j\), gives with probability at
least \(1-\eta\)

\[
 \|\widehat Q^{(L)}-Q^{(L)}\|_{\max}
 \le A_L B_\phi^2
       \sqrt{\frac{2\log(2Lm^2/\eta)}n}.
 \tag{24}
\]

Since \(\|E/m\|_{\rm op}\le\|E\|_{\max}\), the sufficient
width

\[
 n\ge32 A_L^2B_\phi^4\lambda^{-2}
                         \log(2Lm^2/\eta)
 \tag{25}
\]

ensures normalized initialized Gram error at most \(\lambda/4\).
The fixed Gaussian hidden-operator and first-weight RMS events add
their usual exponentially small tails, uniformly in the data.

For a fixed deletion count \(q\), deleting bounded activation
coordinates changes the initialized top feature RMS by at most
\(C\sqrt{q/n}\), by the rectangular operator argument already
proved in the source. Its normalized Gram change has the same bound.
Thus \(n\ge Cq\lambda^{-2}\) suffices to transfer a fixed
strict gap margin, simultaneously over all deletion sets of that size.
Again no intermediate initialized gap is needed.

## 6. What is uniform, and what the final width threshold still hides

The estimates above show that, for a fixed class specified by
\(d,L,R_x,b,B_\phi,m,\lambda\), the source prefactors and a
sufficient label threshold can be chosen uniformly over datasets. The
initialized concentration bound (25) is fully quantitative and uniform.
Input positions enter the argument through their norms and covariance
entries; the only inverse spectral margin used is the final normalized
gap in (1).

The final source probability is obtained by fixed-block moments. For
each fixed integer moment degree \(q\), the insertion estimates have
uniform constants for this dataset class, but their width threshold
depends on \(q\). To obtain confidence \(1-\eta\), choose a
sufficiently large finite \(q\), then a sufficiently large width.
The original order of limits proves existence of
\(n_0(d,L,R_x,b,B_\phi,m,\lambda,Y,\eta)\); it does not
display a usable closed formula for it. Control-net constants, Gaussian
union bounds over samples and queries, and the horizon prefactor
\(\lambda^{-1}\) are further explicit reasons for this dependence.

The fixed positive label magnitude \(Y\) is retained in that threshold
because the inherited proof contains \(e^{o(1)/S}\) in cavity-budget
transfer and the comparison uses \(\epsilon\le Y\). Uniform source
prefactors under (2) do not by themselves prove one common width threshold
for every arbitrarily small positive \(Y\). A proof rescaled by label
magnitude, or a careful rerun with a fixed upper activity allowance,
could address that stronger assertion; it is not silently included here.
The zero-label case is separately exact and stationary.

Uniformity means the same constants work for each dataset in the class,
with the specified probability for its Gaussian initialization. It is
not a single simultaneous event over all datasets, nor a growing-data
asymptotic result. The same distinction applies to independent
initializations at different widths. Finally, the explicit dependence
of the retained-state bound is conservative; exact optimal powers in
\(m\) and \(\lambda^{-1}\), practical preprocessing cost, and a
fully quantified final probability rate are not established by this
audit.

## Inputs completed and exchange provenance

All four assigned current source files were read completely. To resolve
the scalar Gaussian moment and insertion smallness conditions, the
explicitly authorized `DEPTH_CAVITY_ROUTE.md`,
`DEPTH_INSERTION_CHECK.md`, and `DEPTH_CAVITY_PROBABILITY_CHECK.md` were
then read completely. No references to further prior-study research were
followed. After the initial assessment was frozen, the supervisor
independently reported the same budget/gap simplification, requested the
uniform source-prefactor refinement, and supplied the choice
\(\epsilon=n^{-1}\) used in Section 4. No experiments, Git mutations,
or other-file edits were performed.

## 7. Audited refinement using the separate real energy theorem

This section was added after the preceding audit was frozen at SHA-256
`a51ee9bd550abcbcc4561d9236c1ef83d5bf389c12e66181ebb529c707d63d8e`.
The supervisor then explicitly authorized the complete additional input
`DATASET_LABEL_DEPENDENCE.md`, whose real energy argument proves fitting
for \(Y\le c\lambda\), including the weighted model and rectangular
cavities after the usual fixed initial-margin adjustment. That file was
read completely. The stronger conclusion below is conditional on that
separately checked deterministic input. It is an internal collaborative
refinement, not a promotion review.

In (14), the condition \(S^2\le c\lambda\) was used only to
preserve the real training Gram by its coarse perturbation estimate (6).
No separate non-real step requires it. Specifically:

- The residual-Hessian variational propagator needs fixed small \(S\)
  and \(CS^2\ell_n\) below its chosen small power of \(n\).
- The endpoint trace series need fixed small \(S\), and their
  budget-dependent contributions are controlled by \(S^2B\le c\).
- The real Gaussian-path modulus requires
  \(S^2\log(e+B)\le c\).
- The empirical moment closure requires \(S^2B\le c\), with
  \(B=Cm\).
- The vertical/short negative-real extension uses a bounded real
  physical tube, total activity \(CS\), and a bounded normalized
  tangent-Gram operator. It requires no positive complex Gram and no
  new comparison of \(S^2\) with \(\lambda\).
- Forward/angular induction and exclusion of query poles use fixed
  small \(S\), the preceding budget estimates, and bounded \(SY\).

The new real theorem independently supplies the gap and decay rate
\(\kappa\asymp\lambda\). Its sharper readout RMS estimate does
not invalidate any coarser bound used by the source proof: integrating
the actual readout velocity still gives coordinate bound \(CS\), and
integrating hidden speeds still gives displacement \(CS^2\). The
Gaussian-path argument can therefore retain exactly its normalization
\(S=C_0Y/\lambda\).

After replacing just the real bootstrap, a sufficient complete list is

\[
                  Y\le c\lambda,\qquad
                  S\le c,\qquad S^2m\le c.
 \tag{26}
\]

Since \(m\ge1\), all three follow from the sharper condition

\[
                         0<Y\le c\lambda/\sqrt m.
 \tag{27}
\]

Thus (27) is a sufficient condition for the **full** source and carrier
construction when coupled to the new real energy theorem. All uniform
source-radius, source-magnitude, initialization, dimension, and retained
storage bounds in Sections 4--6 remain valid. The original
\(c\lambda^{3/2}\) condition remains a valid smaller-label sufficient
condition after adjusting structural constants via (16).

There is one change in the quantitative comparison. The normalized
residual damping and rank-one velocity subtraction give

\[
 d(t)+\epsilon
 \le\epsilon\exp\{C(1+M)S/\lambda\},\qquad
 M\le1+CS\sqrt{\ell_n}.
\]

With \(\epsilon=n^{-1}\), the resulting finite-window error is

\[
 C\exp(CY/\lambda^2)n^{-1}
       \exp\{CY^2\lambda^{-3}\sqrt{\ell_n}\}.
 \tag{28}
\]

Under (27), the coefficient of \(\sqrt{\ell_n}\) need not be
structurally bounded. The explicit additional width condition

\[
                    \ell_n\ge C(1+Y^4/\lambda^6)
 \tag{29}
\]

ensures that its exponential is at most \(\sqrt n\). Adding the
same query tails gives all-time error
\(C\exp(CY/\lambda^2)/\sqrt n\), bounded under (27) by
\(C\exp(C/(\lambda\sqrt m))/\sqrt n\). The smaller-label
subclass (2) still gives the previous
\(C\exp(C/\sqrt\lambda)/\sqrt n\) bound and a structural
threshold for the amplification step. Condition (29) is part of the
full \(n_0\), not a replacement for the source probability and
small-positive-label qualifications in Section 6.
