# Internal check of the corrected finite curvature reduction

Author: /root/harmonic_route, 2026-09-12.

**Scoped verdict: PASS for the reduction and explicit correction read together.**
I found no remaining substantive error in the asserted endpoint approximation
and effective certificate reduction. The effective input restrictions in the
correction are essential. This is an internal mathematical check, not an
independent promotion review, an evaluated certificate, or a curvature-sign
result.

The checked pair preserves the declared family and reduces its endpoint cubic
and derivative to deterministic finite computations with valid a posteriori
error bounds. Arbitrary-accuracy approximation terminates on the specified
effective inputs. Uniform statements about the abstract family use finite
computable nets and analytic continuity; they do not assert that an arbitrary
noncomputable family member can be evaluated.

## 1. Frozen inputs and actual scope

Both assigned files were read completely, including limitations and provenance:

| Input | Complete coverage | SHA-256 |
|---|---|---|
| CURVATURE_CERTIFICATE_REDUCTION.md | Lines 1–749 | 24a69ef255c14e15cfb666332ea0f772ed9ae8deeb74938b6450ffb7f9918039 |
| CURVATURE_CERTIFICATE_CORRECTION.md | Lines 1–388 | b6c1b155b24db2da8b6ae1e27fc091cf10f75c2026bdb8c91612653e54b83bf8 |

I read no other agent's current check. I did not read ROUTE_ENERGY.md; its
appearance in the author's provenance is not a claim of coverage by this
reviewer. Its contents are not needed for the reconstructions below. No input
file was edited. No experiment, numerical integration, training, Git operation,
or new sign search was performed.

Previously complete allowed scientific coverage retained in this context:

* The neutral RESEARCH_CONTRACT.md and docs/NOTATION.md, completely.
* ROUTE_GEOMETRY.md, completely, at
  e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04.
  Its exact family, equations (G12)–(G14), and limitations are the relevant
  study dependency; lines 1–90 were reread in this check.
* docs/global_nonlinear.md: A.1–A.4, lines 1840–1898; C.4.5.1 §§1–3,
  lines 5475–5782; its rational constant certificate, lines 5999–6103;
  C.4.5.2 §§1–4, lines 6104–6521; C.4.9 setup and source unit, lines
  12994–13955; its clock unit through B.4, lines 13956–14335; and C.4.10,
  lines 15324–17016. This does not claim coverage of the unread intervening
  continuation units.
* docs/special_data_limits.md: complete III.F, lines 3785–4326.

For this check I additionally reread global_nonlinear.md lines 1835–1902,
5585–5695, and 6104–6521, and special_data_limits.md lines 3960–4110.
These reads verify the global feature-clock monotonicity, reference source
estimates, bounded-product source extension, singular covariance convention,
and actual adjoint used below.

Relevant established and process hashes, unchanged at the check:

| Source | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| RESEARCH_CONTRACT.md | 0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

The required solve-math-rigorously and investigate-conjectures skills and
the latter's research-contract, adversarial-audit, and
proof-search-orchestration references were completely read earlier in this
context and remain applied. Their respective hashes are
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7,
a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de,
7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e,
8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501,
and 6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd.

## 2. Reference approximation and uniform base moments

The deliberately coarse constants are consistent. Summing the three R10
velocity bounds gives coefficients
$s a(a+1)+(c+a)/2$, $c+1+2s(a+1)$, and $a+1$ in the clock sum metric.
At $a=53,c=11,S=10$ their maximum is $28652$, below the stated
$\Lambda=28674$. The speed bound is $ac+c+1=595$.
Thus the local Euler defect is at most $\Lambda Vh_j^2/2$ and the
discrete Gronwall estimate is (C4). The raw distance is bounded by the
clock sum distance because $J$ is one-Lipschitz in its clock argument.

The fitting construction does not require knowing the exact feature endpoint.
The global feature equation, including times after fitting, has
$b_s\ge m_0$ by C.4.5.1 R9–R13. Its norm bounds on $[0,S]$ follow directly
from bounded activations and the signed clock updates. Therefore selecting
the smallest computed reference residual among mesh points is legitimate.
For a nearest mesh point and then the selected point, the exact fitting
error is bounded by $L^2h+2L\delta_h+2\epsilon_b$. Dividing by $m_0$
controls the feature-time discrepancy. Multiplication by the raw speed bound
$L$, followed by the Euler error, gives exactly

$$
\|\bar\theta-\theta_\dagger\|
\le (1+2L^2/m_0)\delta_h+L^3h/m_0+2L\epsilon_b/m_0.
$$

The fresh-pulse constants in (C6) are a valid coarse version of the fully
read reference argument. The amplification coefficient is bounded by
$54+2862s$, whose integral is $54S+1431S^2$. A forward pulse has immediate
sum-metric effect at most $h_jP$; a passive upper backward field is
$K_q=\max(1,2Sa)$-Lipschitz in that metric. Two old anchor slots per step
therefore contribute at most $2SPK_qE$. The learned ranks contribute
$Sc^2$, and only the matching current forward source contributes the current
response, bounded by $2S$. Appending several passive inputs without updating
the state does not create additional historical updates.

The local forcing argument has positive slack from the unforced population
bounds $52,10$ to $53,11$. The initialized finite matrix norm can also be
put strictly below the enlarged bound using A.3 before the small-forcing
limit. Source naming, width-first extraction, and then zero forcing are the
same as the established proof; values on a singular support are not
differentiated to infer transverse coefficients.

Consequently the Gaussian-plus-bounded $Q$ representation, (C7)'s moments,
and their common-carrier passage are valid. Summing the two first-row clock
increments gives the stated full-row bound $W_j$. These are statements
about generated fields, not $L^j$ operator bounds for $A_0$.

## 3. Base errors and the correction's probe bounds

Equations (C8)–(C9) have the correct product and interpolation factors.
For a first-gate difference $m$, $|m|\le1$ and
$\|m\|_2\le2\delta$. Hence
$\|m\|_4\le\sqrt2\,\delta^{1/2}$ and
$\|m\|_8\le2^{1/4}\delta^{1/4}$.
Also $1/4=(1/3)/2+(2/3)/8$, giving the displayed $Q$ interpolation.
The rank and readout differences supply precisely the remaining linear
terms in (C8).

The correction must govern every downstream residual-dependent constant.
For its representation $r=AF_*+\psi$, the endpoint-induced residual error
is $|A|L\delta$, with the supplied $\psi$ error added separately. A fixed
exact probe independent of $F_*$ has no endpoint-induced residual error.
The common bound $R_{\rm probe}$ must cover both residuals. The identities

$$
rg-\bar r\bar g=r(g-\bar g)+(r-\bar r)\bar g,\qquad
\int p\,d\rho=1
$$

give exactly (P4), including its row-$L^4$ version. Quadrature errors are
additional errors for the finite-reference integrands. Nonnegative quadrature
mass at most $M_q$ gives (P5), (P7), and therefore all the direction bounds
in (P9). These substitutions correct the original task-sized constants.

The Gram and projector factors in (C10)/(P6) are valid:
$\|G-\bar G\|\le\sqrt2e_g$,
$\|M-\bar M\|\le4Le_g$,
and the exact projector difference identity yields
$e_\Pi\le2\sqrt2e_g/\sqrt\gamma$.
Subtracting $M^{-1}G^*v$ gives the three stated $e_\beta$ terms.
Finally, subtracting
$b_w=v_w-\sum_a\beta_a g_w(e_a)$ gives (P8).
No source differentiation of projector coefficients is used in these
finite evaluations.

The scale-dependent tail rule (P10) is exact. It is necessary when a probe
amplitude changes; neither a previous cutoff certificate nor a previous
direction norm can be reused without its scaling.

## 4. Directional product and projector derivative errors

The fields (C13) are the directional derivatives in the raw metric with the
actual $A^*$, and (C14) bounds their norms. In particular $z_c$ is bounded,
$z_w$ has the indicated moments, and all appearances of the readout in
upper derivative products use the common supremum $H$.

I checked each term of (C15):

* The two terms in $e_a$ come from changing the direction and first gate.
  The four terms in $e_B$ come from changing $z_K$, $H^1$, $A$, and $a_z$.
* In $\delta_z$, changing $z_c$, its gate, and $B_z$ gives
  $e_z+2Z_ce_Z^0+2He_B$. The remaining coefficient has $L^2$ norm at most
  $2\delta+6He_Z^0$ and supremum at most $4H$. A split against
  $\bar B_z$ gives exactly the remaining cutoff and tail terms.
* Actual adjunction and rank subtraction give
  $ce_z+Z_Ke_\delta^0+\delta D_*+ae_D$ for $Q_z$.
* The lower triple product gives $2Q_4e_{z,4}+2Z_4e_{Q,4}$ from its
  direction and $Q$ changes. The changed second gate has supremum at most
  four and $L^2$ norm at most $6\delta$, hence $L^4$ norm at most
  $\sqrt{24}\sqrt\delta$. Pairing with $z_wQ$ in $L^4$ gives the stated
  $Z_8Q_8$ term.
* The remaining first-gate times $Q_z$ term has gate supremum at most one,
  giving $e_{Q_z}+2R\delta+\tau_R(\bar Q_z)$. The middle-rank terms and
  readout cutoff subtraction are likewise exactly (C15).

For (C16), write $B_G=GM^{-1}$. Its error is bounded by the displayed
$e_{B_G}$. Subtract all factors in
$\dot\Pi=-\Pi\dot G B_G^*-B_G\dot G^*\Pi$ and use
$\|B_G\|\le\gamma^{-1/2}$. This gives $e_{\dot\Pi}$ and then $e_{\dot d}$.
In particular the normal projection derivative is retained.

The passage to an operator norm uses a genuine finite-rank map on the
prediction space: integrate each input over cells, with vector outputs the
finite feature values. Cauchy–Schwarz bounds its operator error by the
$L^2(p\rho)$ feature error. Factor subtraction of
$K'=D'^*D+D^*D'$ gives (C17), with both approximate norms included in
$L,L_{\rm prime}$. There is no operator-norm approximation to $A_0$ here.

For the cubic, the corrected (P11) follows by subtracting the integral and
the two anchor factors separately. Pairing the resulting vector error with
$b$ gives its second line. Its $G_*e_r$, residual multiplier, and two
$\sqrt2$ anchor factors are all valid. The factor $-2$ in $D'_0$ and
$-4$ in $\langle r,K'_0r\rangle=-4\mathcal C_p(r)$ agree with the
actual initial velocity $-2b$.

## 5. Spatial errors and computable finite Gaussian evaluation

The six terms in (C19) account for the input vector in the lower feature,
the $Q$ input change, the first gate, the two factors of the rank feature,
and the readout. Equation (C20) uses interpolation for $Q$ and
$\|wQ\|_4\le W_8Q_8$ for the changed gate. Equation (C21) follows from
$\|a_z(u)-a_z(v)\|_2\le(Z_2+2W_4Z_4)|u-v|$.

The elementary tail comparison (C22) is valid. The coefficient split in
(C23) has exactly the terms $2Z_caW_2\ell$, $2HL_B\ell$,
$6HRaW_2\ell$, and $4Ht_B(R)$ inside the adjoint bound. The remaining
spatial derivative products have the stated $L^4/L^8$ factors.

For clarity, an implementation's spatial error for the projected derivative
must include both terms of $\dot d=\Pi\dot g+\dot\Pi g$. If
$\omega_{\dot g}(\ell)$ is the modulus assembled in §7, the sufficient
choice is

$$
e_x=\omega_{\dot g}(\ell)
       +(2\sqrt2G_*/\sqrt\gamma)L_x\ell.
$$

This is already furnished by (C16), (C19), and the listed subtraction rules;
it is not a new hypothesis or a defect in the reduction. A bound for
$\dot g$ alone should not be substituted for the spatial error of $\dot d$.

The finite source evaluation keeps all initialized orientations and named
slots. There is a direct way to check applicability beyond the initial
reference graph. A finite force has $z_w$ a finite sum of bounded gates
times $Q$ nodes, $z_c$ bounded, and $z_K$ a finite rank sum. Thus $a_z$
is a bounded-coefficient times linear-envelope input. The new forward call
for $A_0a_z$ determines $B_z$. The new reverse input
$z_c\phi'(Z^2)+c\phi''(Z^2)B_z$ has the same kind of bounded-product
structure, after harmless clipping of the readout on its known interval.
The allowed A.2 truncation argument therefore supplies its source rule.
Only the final lower derivative output and scalar contractions require
polynomial rather than linear envelopes; they are finite Gaussian integrals,
not inputs to an unproved $L^p$ action.

In this use of A.2, source derivatives of the clock are controlled as in
the reference proof, not by differentiating the root. At a fixed graph
the needed source derivatives have computable polynomial envelopes, and the
bounded tanh derivatives and finite rank operations close the induction.
New action calls must include responses to every earlier opposite-orientation
call, including the newly appended directional calls. Computing a new action
is not equivalent to differentiating an old source formula with some response
terms omitted. The text's full-history convention is the correct one.

Equation (C24) is valid at singular covariance: the two regularizations cost
$2\sqrt m\sqrt\delta$ in Frobenius norm, and the Sylvester equation costs
$\sqrt\delta/2$. Positive-part projection of an approximate covariance
increases its discrepancy from the true positive matrix by at most a factor
two. Neither step requires rank stability or continuity of a pseudoinverse.

The Gaussian tail union bound and Cauchy–Schwarz give (C25). Its polynomial
moment is finite and computably bounded. On a compact cube, the explicit
finite graph, inverse-clock bisection, and square-root error control provide
computable quadrature and coefficient propagation errors. Equation (C26)
follows from $|X|\le2(|X|-R/2)$ on $|X|>R$; its integrand is continuous.
These arguments certify the required soft-tail expectations without
sampling or an uncomputed discontinuous integration oracle.

## 6. Why the search terminates, and what its inputs must provide

There is no circular tail assumption in the termination argument. Keep one
positive certified Gram gap once obtained. Then $\delta\to0$ and the
corrected force estimates give $\bar b_w\to b_w$ in $L^4$, as well as raw
convergence. Consequently $a_b$ and $B_b$ converge strongly in $L^2$.
For $\delta_b$, subtract the varying $B_b$ first and split the remaining
bounded multiplier against the fixed limiting $B_b$; its $L^2$ tail
vanishes. Actual bounded adjunction then gives strong $L^2$ convergence of
$Q_b$. The lower differentiated product converges by the established
$L^4$ bounds and bounded-multiplier continuity.

Uniformity in passive input is also available. The $B_b$ fields have the
common spatial Lipschitz bound (C21); compactness of the circle upgrades
pointwise convergence to uniform convergence and gives uniformly small
$L^2$ tails over mesh indices and inputs. The cutoff estimate (C23) then
does the same for $Q_b$, and the remaining derivative formulas follow.
Equivalently, use finite spatial nets and (C22). Thus a finite cutoff can
first make the tail contribution small, and sufficiently fine endpoint and
spatial meshes subsequently make its cutoff-amplified terms small.

Every finite required Gaussian integral can be enclosed to arbitrary
accuracy. Dovetailing finite meshes, cutoffs, and integration accuracies
therefore eventually produces a displayed error strictly below any positive
tolerance. A priori knowledge of the limiting tail modulus is not required:
the computable upper bound at the accepted finite approximation supplies the
stopping certificate.

Two implementation conventions matter but add no substantive hypothesis.
The Gram-gap search must find some positive rational $\gamma$, rather than
demand an arbitrarily prespecified gap; a certified positive excess of the
computed Gram eigenvalue over $e_M$ supplies one. Once found, retain a
positive lower bound through further refinement. Also use fixed common
probe and moment bounds during the convergence argument, rather than
needlessly degrading $\gamma$ or inflating the probe bounds at every step.

The correction correctly restricts effective inputs. All coefficients,
targets/probes, densities, and quadrature moduli entering a claimed individual
computation must have the supplied computable representation and certified
integration control. Merely being bounded, Lipschitz with noncomputable
values, or pointwise evaluable without an integration modulus does not
suffice. For an abstract family member the algebraic estimates are valid,
but an individual effective integral evaluation is not asserted.

## 7. Unchanged-family nets and polarization

The exact endpoint signed-density map $h\mapsto b_h$ is linear.
Its signed control mass is at most
$C_{\rm proj}\|h\|_1$, with
$C_{\rm proj}=1+2L^2/\gamma$.
The unit-mass derivative bound $J_1$ in (C14) therefore gives a trilinear
bound $LJ_1C_{\rm proj}^3\prod_i\|h_i\|_1$ for the cubic. Telescoping
its three arguments proves (C27). The correction properly recomputes $H_1$
and keeps this reference constant distinct from residual amplitudes.

Equation (P15) uses normalized density mass one and is correct. Conjugating
to the common $L^2(\rho)$ space gives derivative feature
$-2\sqrt p\,\dot d_{b_h}$; the square-root identity supplies exactly the
stated coefficient $1/\sqrt{p_{\min}}$ on the density-change term.

Finite angular grids, quantized values, density normalization and odd
symmetrization give computable finite nets of the declared Lipschitz
classes in the uniform topology. They can stay within a small common
bounding class with densities between $1/2$ and two. The target control is
on the factor multiplying $h=\sin^2(2\alpha)$, so its existing strict
factor bound preserves $|q|\le1$ despite equality at the anchors.
It is not necessary that every abstract member be computable or that every
net representative lie exactly in the original class. The finite net covers
every original member, and its analytic covering error is explicitly
controlled. No favorable subset is selected from observed signs.

The cubic is homogeneous because the force and anchor coefficients are
linear in the probe and the directional gradient is linear in its direction.
Its symmetric polarization therefore has coefficient $1/(2^3 3!)=1/48$.
For eight cubic errors bounded by $E$, the direct tensor error is at most
$E/6$. For normalized probes $s_\varepsilon=r_\varepsilon/3$,
the coefficient is $27/48=9/16$ and the corresponding error is at most
$9E/2$. The correction retains all these factors, the distinct coefficient
of $F_*$ in a normalized probe, its endpoint approximation error, and the
tail rescaling. The derivative maps scale linearly, not cubically.

## 8. Component verdicts and remaining claim level

| Component | Internal scoped verdict |
|---|---|
| Finite reference endpoint approximation and moment constants | PASS |
| Probe-specific residual, force, projector, direction, and cubic errors | PASS with the explicit correction governing the original |
| Directional products, tails, and full projected derivative/operator errors | PASS |
| Complete source/adjoint evaluation and singular covariance control | PASS within the finite generated-program scope |
| Arbitrary-accuracy deterministic approximation | PASS for the correction's effective inputs |
| Uniform coverage of the unchanged abstract family | PASS through computable finite nets and analytic extension |
| Direct and normalized polarization, including interval errors | PASS |
| Evaluated favorable curvature or beneficial component sign | NOT ESTABLISHED |
| E₀ population advantage, ordered finite-network transfer, or promotion | NOT ESTABLISHED BY THIS PAIR |

No correction to either frozen input is requested by this check. The concrete
spatial-projector and Gram-search conventions above make explicit operations
already available from its formulas. The reduction supplies neither a
favorable sign nor a claim that its extremely large constants are practical.
