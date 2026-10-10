# Independent mathematical preaudit A

Date: 2026-10-09. Scope: the five frozen, theorem-focused TeX inputs listed below. This is a mathematical soundness audit, without a novelty assessment, experimental assessment, code campaign, or publication recommendation.

## Assessment

**No fatal or major flaw was identified.** Under the stated, fixed-problem small-label assumptions, I find the presented proof chain supports the headline theorem. The most delicate dependency is the source argument in `compact_foundations.tex`; the audit below distinguishes its actual probabilistic mechanisms from the simpler deterministic consequences. I found no circular use of the desired source approximation to prove dense fitting, no missing sample-normalization factor in the selected cancellation, and no substitution of a dense-variability upper bound for the required lower bound.

This is a positive result of the specified independent audit, not a claim that every possible proof error has been excluded. Confidence is high in the fitting, projection identities, selected cancellation, innovation argument, initialization provenance, and storage assembly; confidence is more moderate in the very long source-localization argument and its generously enlarged numerical coefficient bounds. I checked its load-bearing estimates and exponent arithmetic, but did not mechanically formalize every coefficient enlargement in its recurrence tables. No mandatory mathematical repair resulted from this audit.

## Frozen inputs and exact coverage

All scientific lines of every assigned file were read, including proofs and boundary cases. The first combined read of `compact.tex` was truncated around its assumptions; lines 95–124 were reread explicitly. Subsequent chunked reads were complete. The PDF was not needed because the complete equation source was available and unambiguous.

| Input | Complete coverage | SHA-256 |
|---|---:|---|
| `paper/compact.tex` | 1–257 | `64327f17c0a47b08a349890d274960b9732c8d650b2730e02a4d44d3e88fa6f9` |
| `paper/compact_fitting.tex` | 1–213 | `4cb10d4534f95ca5dbc9a957aac536c55a7268e0dc7128c105102de5bd195235` |
| `paper/compact_foundations.tex` | 1–1377 | `8de151e32734ee2c9116a91a1cccb7c5ecee7ec1369ff4784e88fb4d79a6148a` |
| `paper/compact_legendre.tex` | 1–699 | `45c40b7e6c1c1b501d6f2643a226ac2ca4a00a91e3d9704502ed54fadf4fe238` |
| `paper/compact_selected.tex` | 1–1007 | `12b2d33bf7732172d454cf3a2d74a4b322f027a74474d8747f3da9ef85b96c11` |

The hashes were checked again after the mathematical reading and were unchanged. Total assigned coverage: 3,553 lines. Reads of the longer files were foundations 1–280, 281–540, 541–820, 821–1100, 1101–1377; Legendre 1–250, 251–480, 481–699; selected 1–260, 261–520, 521–780, 781–1007.

Required process inputs read completely: `solve-math-rigorously/SKILL.md`; `explain-with-canonical-notation/SKILL.md` and its neural-response-memory reference; `review-ai-paper/SKILL.md` and its severity rubric. The explicit one-report assignment supplies the output format. No study history, study README, previous review, other reviewer's findings, original long paper, Git history, maintained-book material, or unrelated study was inspected. No TeX was modified. No external scientific input was needed to reconstruct the checked arguments.

## Stated theorem actually being audited

The model has fixed training inputs $v_a=x_a/\sqrt d$ of unit norm, fixed $m\ge2,d\ge1,L\ge2$, zero initialized readout, Gaussian first weights of variance one, and Gaussian hidden weights of variance $1/n$. The activation assumptions are strip holomorphy, reality on the real axis, and a bounded first derivative; bounded activation values are not assumed. The uncentered limiting top-feature Gram has gap $\gamma>0$. With

\[
\lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,
\]

the headline additionally assumes $0<\lambda\le1$ and $0<Y\le\lambda\beta^{-30L}$. Every problem parameter, including positive $Y$, is fixed before taking width to infinity (`compact.tex:58–123`). These restrictions matter: this is not a large-label, growing-data, uniform-in-$Y\downarrow0$, finite-precision, or efficient-preprocessing theorem.

Legendre retains $n^{5/4+o(1)}$ moving coordinates and the separate fixed dense mixers. Harmonic and Logarithmic count their total retained runtime arrays; the former promises the sphere and the latter only the fixed declared panel. All three are compared in the all-time norm, including fitted limits, against a coupled dense run and actual independent dense-run variability (`compact.tex:125–202`).

## Reconstructed arguments and adversarial checks

### 1. Dense normalization, fitting, and the absence of a source bootstrap cycle

References: `compact.tex:65–92`; `compact_fitting.tex:34–178`.

In physical mobility coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\]

the three types of output-gradient blocks are

\[
\frac{\delta_a^{(1)}v_a^\top}{\sqrt n},\qquad
\frac{\delta_a^{(j)}h_a^{(j-1)\top}}n,\qquad
\frac{h_a^{(L)}}{\sqrt n}.
\]

Thus the displayed physical flows are exactly the negative gradient of $m^{-1}\|r\|_2^2$ in these coordinates. In particular, neither the first-layer nor readout velocity has an extra factor $1/n$. If the stopped normalized top feature Gram is at least $\lambda I/4$, its readout contribution gives

\[
-\partial_t\rho^2=\|\dot\theta\|^2\ge\lambda\rho^2,
\qquad \rho=\|r\|_2/\sqrt m.
\]

Combining this with the same exact energy identity yields the stated length estimate rather than an ordinary positive-time Gronwall bound:

\[
\left(\int_t^T\|\dot\theta\|\,du\right)^2
\le\left(\int_t^T\frac{\|\dot\theta\|^2}{\rho}\,du\right)
\left(\int_t^T\rho\,du\right)
\le\frac{4\rho(t)^2}{\lambda}.
\]

The zero-residual case is stationary, so division in this proof does not introduce a definition of the dynamics at a zero denominator. The finite length, strict operator/feature/Gram margins, and real bounded derivatives give continuation and parameter convergence. The uniform sphere-output tail is separately derived; a training-only fitting statement is not being silently upgraded to a sphere statement.

I also checked the initialization argument when an intermediate covariance is singular. The covariance-square-root coupling and Gaussian polynomial domination only require continuity on the positive semidefinite cone. No inverse of an intermediate covariance is used. Uniform cavity initialization is transferred by zero-embedding and vanishing normalized feature perturbations, not by union-bounding a merely qualitative law of large numbers over all deletion sets.

**Attack outcome:** fitting is established before the analytic source proposition and does not require it. This removes the most obvious possible circularity. Sound on the checked chain.

### 2. Source argument: independent deletion, adaptive controls, and the trace terms

References: `compact_foundations.tex:254–678`, especially 300–358, 392–539, 599–678; trace calculation at 683–802.

The second mobility convention in this section is consistent with the first one: $\Theta=\sqrt n\,\theta$ and $F_a=nf_a$, so

\[
\dot\Theta=-\frac2m\sum_a r_a\nabla_\Theta F_a.
\]

After $\bar u=(\Theta-\Theta_0)/S$ and $\bar r=r/S$, the retained forward and reverse ports have the stated scaling. In particular the reverse port is not inserted into the residual; it changes the retained gradient through the lower forward derivative. This distinction is needed for the port derivatives in lines 394–399.

For an interior omitted neuron, its incoming row and outgoing column are independent Gaussian roots conditional on the retained cavity. At the first layer the incoming row has covariance $I_d$, not $I/n$, and the proof explicitly excludes a nonexistent retained reverse port below that layer $`compact_foundations.tex:523–539`$. I checked this boundary against the retained equation; it does not require an artificial $n^{-1/2}$ estimate for first-layer row motion.

The quadratic-form concentration calculation only applies to deterministic frozen scalar controls. The proof first covers their admissible class and only then substitutes adaptive controls. Its exponent margins are adequate:

\[
\log N_{\rm control}=n^{5/8}\operatorname{poly}(\log n),
\qquad \Pr(\text{one bad test})\le4e^{-n^{.78}},
\]

while the interpolation error has order $n^{-1/8+1/200}\operatorname{poly}(\log n)=o(n^{-1/10})$. Polynomially many coordinate, frame, and fixed-deletion tests do not consume this margin. The proof does not claim the resulting adaptive variation is Gaussian or centered (lines 671–677).

The same-root means are indispensable. For example, insertion of the incoming root produces

\[
-\frac2m\sum_b\int r_b\delta_{b,i}
\frac{\operatorname{tr}(C_aJ C_b^\top)}n\,ds,
\]

and the outgoing root also produces an integrated Hessian trace and a direct port-Hessian trace. These terms are explicitly retained at lines 711–718. The fourth mean is small through two Gaussian normalization factors, giving $n^{-1+\kappa}\operatorname{poly}(\log n)$. Dropping these traces would invalidate the scalar absorption; this paper does not drop them.

I reconstructed why the trace normalization remains $1/n$ despite the much larger parameter dimension. Each endpoint map factors through neuron coordinates; normalized Schatten Hölder exponents sum to one. For two Hessian endpoints and $h$ insertions, exponent (h+2) on each factor gives precisely this normalization. For forward endpoints, exponents $2,\infty,2h,\ldots,2h$ do so. The real and complex base-propagator bounds established later have additive growth integrals on disjoint pieces, which supply the product bounds needed between insertions.

The feedback estimates reduce to

\[
U_i\le\overline G_\delta+2D_0(1+2Z_i)+o(1),\qquad
Z_i\le\overline G_h+DU_i+o(1),\qquad D\le(8D_0)^{-1}.
\]

Consequently $4D_0D\le1/2$, so absorption is legitimate. The resulting coefficient is independent of sample and deletion counts; these are not hidden inside the small-label allowance.

The nonlinear local closure also has a real exponent margin. With the proof's choices $N=n^{.01}$, $d_0=n^{-.1}$, $u_0=n^{-.04}$, its most dangerous displayed product is $d_0N^2=n^{-.08}$. Multiplication by $n^{1/4000}\operatorname{poly}(\log n)$ still makes it $o(u_0)$. The learned-port and residual-offset terms are smaller. The forward and backward Taylor remainders keep a reference-carrier factor and include matrix–feature cross terms; the statement is not based only on a linear insertion ansatz.

**Attack outcome:** no invalid independence substitution, omitted leading trace, or exponent failure was found. The local remainder and differentiation estimates are the densest part of the proof, and the positive assessment here has the coverage qualification stated at the beginning of this report.

### 3. Source argument: complex continuation and the order of probability limits

References: `compact_foundations.tex:804–1143`, 1207–1377.

The real reference process is parameterized by its own normalized residual activity. Truncating a carrier with the exponential budget gives a square-root activity modulus for the normalized backward coefficients. Gaussian chaining therefore supplies a width-independent real-reference exponential-moment base. This does not require independent training samples.

For the complex correction, the time-derivative lemma uses the provisional response cap and the existing budget. Its varying Hölder exponent is a deterministic inequality, not a deletion count growing with $n$. It yields a normalized correction radius of order

\[
\frac{1+(S^2/\eta_*)\log(e+\log(en))}{\sqrt{\log(en)}}.
\]

The Gaussian supremum estimate adds only another square root of a logarithm, so every fixed exponential moment of the correction tends to one. Independent clipping of each cavity path preserves omitted-root independence. The common-cavity versus singleton correction is projected before pairing with the root; the projected coefficient radius is deterministic and equals the actual difference on the successful prefix.

For each fixed positive integer $u$, the common-cavity moment argument produces

\[
\limsup_{n\to\infty}\Pr(\text{full budget hit})
\le mL(16L/\mathcal B)^u.
\]

Only after taking the width limit is the infimum over $u$ used. Since $16L/\mathcal B<1$, this proves vanishing failure without increasing deletion order inside a width-dependent estimate or shrinking the label allowance with confidence. Colliding index tuples contribute $O_u(n^{k-u})n^{o(1)}\to0$ when $k<u$. This directly addresses a possible invalid interchange of probability and moment limits.

The rectangular continuation does not treat a complex Gram as positive. It starts from the independently proved real solution and bounds the exceptional short contour pieces by their length and operator norm. The flaring domain needs a different argument: at a real anchor $A_t=2G(t)G(t)^\top$ is real symmetric, so $-iA_t$ generates unitary vertical motion. The difference from this frozen generator is integrated using $\|\dot G\|\le C_gB_n\rho$. The double integral is bounded by $Yr_n/(2\mathcal K)$; hence the exponent tends to zero as $B_nr_n\to0$. This is sufficient for the negative-Gram propagator premise before the Gaussian insertion argument is applied.

The source proof's dependency order is consistent: provisional deterministic stops → local insertion and maximum improvement → pole/cavity margins → complete stopped-path moments → budget removal. The real fit is available independently at the beginning. I did not find a step using a source event that it is simultaneously trying to prove.

For the flaring panel geometry, $0\le h'\le d_h\le1/8$ establishes the contained disks. The step $\varrho(t_b)/2$ yields $J\le1+5\int_0^Tdt/h(t)$. Splitting at $2\mathcal K r_ne^{\nu t}=1$ preserves the displayed $z^2\sqrt\ell$ and $\lambda^{-1}\log\ell$ terms. No input dimension enters the finite-list Gaussian multiplier.

**Attack outcome:** the required probability/continuation ordering is supplied. No material gap was identified in the checked route.

### 4. Legendre dynamics, initial prefix, and all-time approximation

References: `compact_legendre.tex:10–157`, 159–278, 280–503.

The reconstruction has the correct $2/(mn\tau)$ factor. The stored histories are defined with a constant forward prefix on ([0,1]) and a zero backward prefix, not an implicit empty history. The backward history joins continuously because $w(0)=0$. Differentiating the growing-interval moments produces exactly the triangular (j,2i+1) terms in the autonomous equations. Residual direction $\widehat r/\widehat\rho$ is used only in the proof histories; it is not divided by in the stored ODE.

I checked the projection identities from the weighted Legendre eigenvalue equation and endpoint kernel. In particular,

\[
u(A)-(\Pi_q^Au)(A)=\frac12\int_0^A(p_q^A+p_{q-1}^A)u',
\]

and the squared multiplier norm is $A[(2q+1)^{-1}+(2q-1)^{-1}]/4\le A/(3q)$, including $q=1$. Differentiating the bilinear projection pairing leaves the product of endpoint errors, giving the sign and normalization of $\mathcal E_\ell$ in lines 144–150.

The order-independent fitting proof first uses the $L^2$ endpoint norm $q/\sqrt A$ with the $q^{-2}$ weighted tail, and then uses the sharper $\sqrt q$ endpoint bound against the $q^{-1/2}$ forward endpoint bound. These are distinct uses; the latter gives an order-independent pointwise defect. The residual still decays, and the finite integral of the physical gradient plus defect proves parameter and moment limits. A residual zero makes the entire stored-state ODE stationary.

For approximation, the signed perturbation lemma retains the negative prediction-error term. Backward subtraction always multiplies the changed gate by an actual dense carrier; it does not assume a corresponding pointwise bound for the closure carrier. The all-time dense carrier bound is obtained separately from finite-time analyticity plus the very small real parameter tail $`compact_foundations.tex:1182–1204`$. Thus the proof avoids a closure-source circularity.

The history forcing estimate has the form

\[
\mathcal D_T\le2(L-1)F_h\left[
\frac{b_0+b_1\sqrt{\log q}}{q^2}
+\frac{B_d\sqrt{a_0}\sup_{t\le T}D(t)}q\right].
\]

The signed comparison bounds $D$ by $\mathcal A_n\mathcal D_T$, and the second term is absorbed once $q\ge q_{\rm abs}=n^{o(1)}$. The prescribed $n^{1/4}\ell^2e^{\sqrt\ell/2}\lambda^{-3}$ order exceeds this threshold for each fixed problem. Squaring this order cancels the $e^{\sqrt\ell}$ factor and supplies the required $Y/(\sqrt n\ell^3)$ error. The coefficients are horizon-independent and both parameter limits exist, so passage to all real times and the fitted endpoint is legitimate.

**Attack outcome:** normalization, prefix, residual-zero, low-order, and infinite-horizon checks passed. The dense mixer storage remains additional; it is not counted as compressed total state.

### 5. Selected metric, fitting, and the feedback cancellation

References: `compact_selected.tex:19–270`, 274–573.

The finite sparsification argument produces $I\preceq G\preceq4I$. With the paper's $Z=D^{1/2}P$, the middle matrix in the explicit formula for $M$ has eigenvalues $G^{-1}$ on the range of $Z$ and one on its orthogonal complement. Therefore $D/4\preceq M\preceq D$ and $P^\top MP=I$. Inclusion of the constant gives both the metric mass and the diagonal mass bound. This controls coordinatewise multiplication even though the gates need not be self-adjoint in $M$.

That lack of self-adjointness does not invalidate the optimizer: it is explicitly a prescribed system. Expanding squared norms of its rank-one parameter velocities gives the displayed Gram $K_C$, and the independently prescribed deficit equation gives the same energy identity. No gradient claim for the corrected predictor is needed. The corrected readout enforces $f_C(v_a)=y_a-c_{C,a}$ algebraically. Its orthogonal decomposition bounds its norm by $\sqrt{20}\,Y/\sqrt\lambda<5Y/\sqrt\lambda$. The hidden displacement and singular-value estimates keep its inverse Gram in a strict positive domain for all time.

For the comparison, coordinate error and the diagonal mass bound imply

\[
|\langle u_I,v_I\rangle_M-\langle u,v\rangle_n|
\le3e_u\|v\|_n+3e_v\|u\|_n+9e_ue_v.
\]

This gives the stated initialized/learned action defects without differentiating a source-approximation error. It also bounds the normalized sample Gram defect without an extra factor $m$.

I reconstructed the cancellation directly. Set

\[
e=(c_C-c_n)/\sqrt m,\quad T_C=V_CQ_C^{-1},\quad
p=T_Ce,\quad \zeta=w_C-w_R+p.
\]

Since $T_CQ_C=V_C$, differentiating $\zeta$ cancels the dangerous $2V_Ce$ term exactly. In the derivative of $\|p\|^2/2$, the $Q_C$ contribution is $-2\|e\|^2$. The potentially adverse hidden-Gram contribution is at most

\[
8\|\mathcal J_C\|^2\|e\|^2/\lambda
\le200z^2F_c\|e\|^2,
\qquad z=Y/\lambda,
\]

so the stated small-label condition leaves a strict negative term. This proves both the bound for $p$ and the integral control of $\|e\|$. The subsequent error coefficient integrates to the displayed $\mathcal B_n$, using

\[
\int\rho_n,\int\rho_C\le2z,\qquad
\int\|V_Rc_n/\sqrt m\|\le2Y/\sqrt\lambda.
\]

The latter source-energy estimate is what prevents an additional sample/gap factor in the exponent. The carrier maximum enters the response-error estimate once, not once per layer. The numerical ledger then gives $\mathcal B_n\le1+\sqrt\ell$ under the stated cap. Choosing $\eta\le Y/(2n\mathcal A_n)$ and using the separately derived real-time tails supplies the selected $Y/n$ guarantee, including $t=\infty$.

**Attack outcome:** the cancellation, metric adjoints, signs, sample normalization, and all-time fitting are supported. There is no reliance on falsely calling the corrected dynamics gradient flow.

### 6. Initialization-only provenance and retained storage

References: `compact_selected.tex:575–671`, 675–886, 890–1007; `compact.tex:182–202`.

The initializer's analytic continuation map is not merely an assertion that a trajectory is determined by its initialization. Substitution gives $\mathfrak t(0)=0$ and $\mathfrak t(\xi_*)=T$. For the unit disk, the Möbius map stays in the disk, and the logarithm maps into the stated time rectangle. Consequently $g\circ\mathfrak t$ has Taylor coefficients bounded by $M$, with uniform tail $M\xi_*^{N+1}/(1-\xi_*)$. Any fixed target accuracy therefore uses finite $N$. Later-anchor derivatives are recovered from this same convergent expansion, rather than supplied by a trained trajectory.

The formal dense ODE coefficient recursion uses only finite initialized derivatives. Time–sphere coefficient integrals can be approximated from the continued origin-jet polynomial on finite quadrature meshes. Exact pairing of a base coefficient and its initialized image is enforced by multiplication by the saved initial matrix. This does not require image errors to be bounded by the base's coordinate error alone: the coefficient approximation is made in Euclidean norm, and each source/image truncation has its own analytic tail bound.

For Harmonic, the checked spatial estimate is obtained by averaging on a complex tangent circle, using the zonal multiplier, and bounding its inverse by a polynomial times $e^{-r_qj}$. With the time Chebyshev decay, the retained indices satisfy $\alpha_Tk+r_qj\le H_*$. The weighted-simplex count gives

\[
N\lesssim\frac{H_*^d}{d!\,\alpha_T r_q^{d-1}}.
\]

Here $\alpha_T^{-1}=131072z^2(U/a)\ell^{3/2}$, $r_q^{-1}=O_{\phi,L}(\sqrt d\sqrt\ell)$, and $H_*=O(\ell)$ eventually for the fixed problem. Hence $N=O_{\phi,L,d}(z^2\ell^{3d/2+1})$. Squaring the selected rank yields the claimed $z^4\ell^{3d+2}$ term, with the stated factorial-based dimension dependence. The separate two-point $d=1$ argument has the matching logarithmic exponent.

For Logarithmic, the adaptive-panel count and $K+1=O(\ell)$ give rank proportional to

\[
(m+p)\left[z^2\ell^{3/2}+\lambda^{-1}\ell\log(e+\ell)\right].
\]

Squaring gives precisely the two displayed storage terms; a cross term is absorbed by $2ab\le a^2+b^2$. Reducing the input space to the span of all declared inputs is exact: all training first-layer velocities lie in this span and the first Gaussian rows remain standard Gaussian after multiplication by its orthonormal basis. This leaves only (O((m+p)d)) for the original/transformed inputs and input map.

The explicit runtime inventory includes metric matrices and factors, moving and initial selected matrices, training forward/backward arrays, sample matrices, corrected readout, directions, and query workspace. Dense arrays, source bases, jets, quadrature tables, and panel schedules are discarded. The counts therefore do not omit an $n$-sized forcing table. Conversely, the manuscript expressly excludes preprocessing working storage, initialization time, finite precision, and nonprimitive activation-evaluator costs; the proof does not establish those stronger claims.

**Attack outcome:** initialization-only provenance and the advertised retained-coordinate counts survive the checks. The limitations are explicit theorem scope, not hidden counterexamples.

### 7. Actual dense variability and final probability assembly

References: `compact_legendre.tex:508–699`; `compact.tex:223–255`.

The innovation argument uses the uncentered feature Gram $Q\succeq\gamma I$, rather than a centered covariance that need not have a gap. For $c=Qy$, the squared-area inequality is valid pointwise because the component of $c$ perpendicular to $U$ is unchanged by subtracting $U(U^\top y)$. Splitting at a radius and optimizing gives

\[
\mathbb E\|U(U^\top y)-Qy\|^2
\ge\frac{[y^\top Q^2((\operatorname{tr}Q)I-Q)y]^2}
{4\mathbb E\|U\|^4\,\|Qy\|^2}.
\]

Using the two spectral lower bounds in the proof and $m\ge2$ gives a strictly positive coordinate variance at a deterministic training index. Linear activation growth supplies every moment used. Thus affine, unbounded activations are not excluded by a tacit boundedness assumption.

At zero readout, hidden parameter velocities vanish initially and

\[
\dot f_n(0,x_a)=\frac2{mn}\sum_iU_{i,a}(U_i^\top y).
\]

Conditional on the two lower-layer initializations, the two final-layer row groups are independent. Their conditional centered fluctuation has limiting variance $8v_*/m^2>0$. Lower layers can contribute an arbitrary conditional shift; a centered Gaussian maximizes fixed-length interval mass when that interval is centered. This yields the needed shifted small-ball estimate without requiring a full recursive matrix central limit theorem.

The derivative-to-trajectory lemma does not infer a trajectory lower bound from a derivative alone. It adds a complex-analytic bound, truncates at degree $N\asymp\ell$, and uses the endpoint polynomial derivative inequality. With $r=1/(\lambda\sqrt\ell)$, the resulting lower bound has the claimed $\sqrt n\,\ell^{5/2}$ denominator. The analytic truncation error is $O(Y/(\lambda n^2))$, negligible for the fixed positive problem. The witness is a positive time at a training input, so it is present in both allowed query domains. There is correctly no claim of dense variability at fitted training outputs, which equal the same labels.

Finally, intersecting an approximation event and a dense lower-bound event uses only a union bound. Independence between those events is unnecessary. For every fixed confidence budget, the Legendre ratio is $O(\ell^{-1/2})$, and the selected ratio is $O(\ell^{5/2}/\sqrt n)$, with fixed-problem constants. Taking the width limit first and then the arbitrarily small failure budget proves convergence in probability. Missing fitted limits and zero denominators are explicitly counted as failures rather than excluded silently.

**Attack outcome:** a genuine lower bound on the requested denominator is proved, and the final probability order is valid.

## Edge-case and dependency summary

| Attack | Result and relevant location |
|---|---|
| Singular intermediate Gaussian covariance | Square-root continuity and domination avoid inverses; `compact_fitting.tex:81–98`, `compact_legendre.tex:569–603`. |
| Unbounded activation values or nonzero activation offset | Linear-growth bounds and uncentered Gram are used throughout; `compact.tex:95–119`, `compact_foundations.tex:11–18`. |
| First-layer deletion normalization | Incoming covariance $I_d$ and no retained lower reverse port are explicit; `compact_foundations.tex:254–263`, 523–539. |
| Adaptive controls treated as independent Gaussian coefficients | Frozen-control covering precedes substitution, and nonzero traces are retained; `compact_foundations.tex:599–677`, 683–802. |
| Moment order growing inside a width limit | It stays fixed through the width limit; `compact_foundations.tex:1046–1079`. |
| Complex Gram treated as positive | Rectangular norm bound and frozen real-anchor unitary argument are supplied; `compact_foundations.tex:1095–1105`, 1268–1325. |
| Residual zero or fitted endpoint | Stored equations remain defined and stationary; fitting and quantitative tails precede endpoint extension; `compact_legendre.tex:47–51`, 260–277; `compact_selected.tex:177–269`. |
| Non-diagonal selected metric and gates | No false gradient interpretation is needed; exact prescribed energy identity is checked; `compact_selected.tex:125–159`, 195–216`. |
| Passive inputs influencing training | They enter only source/query evaluation and exact input-span reduction, not deficit dynamics; `compact_selected.tex:890–1007`. |
| $d=1$, $q=1$, $p=0$ | Explicit two-point source, valid first-order projection estimates, and unchanged training-only panel construction. |
| $m=1$, $Y=0$, growing data | $m=1$ is excluded; zero labels are stationary and excluded from the ratio theorem; growing-data uniformity is expressly not claimed. |
| Hidden dense state in the selected runtime | Complete inventories discard dense arrays, jets, coefficients, and schedules; `compact_selected.tex:859–885`, 977–990`. |

The source proposition is indispensable to all three quantitative approximation results and to the analytic derivative transfer used for the dense lower bound. A future demonstrated failure of that proposition would therefore reopen the headline theorem. Independently surviving parts would include dense fitting, the projection identities and order-independent Legendre fitting, the deterministic selected source-to-runtime transfer, the final-layer innovation, and the conditional initial-derivative fluctuation. This dependency should not be confused with a flaw found here: this audit did not establish such a failure.

## Severity triage and repair requirements

No F-, M-, or L-level mathematical defect was established, so no defect identifier is assigned. There is no claimed counterexample and no mandatory repair request. In particular, I do not propose adding bounded activations, full-rank intermediate covariances, independent samples, a uniform-in-width event, or access to later dense trajectories; none is needed by the checked proof chain.

The limits of this positive verdict are explicit: this was a complete source read and adversarial reconstruction of the load-bearing mathematics, not a formal proof verification; it did not audit literature novelty, numerical utility, efficient coefficient compilation, finite precision, or runnable implementations. Those stronger claims are outside both the assignment and the frozen headline theorem.
