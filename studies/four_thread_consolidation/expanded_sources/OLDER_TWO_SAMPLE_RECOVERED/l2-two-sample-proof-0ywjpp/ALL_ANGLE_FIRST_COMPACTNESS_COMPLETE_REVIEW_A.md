# Independent adversarial review A

Source: `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md`

Review date: 2026-09-06.

## Verdict

**PASS within the stated scope. No required mathematical correction found.**

The document establishes deterministic strong-
\(W_2\) compact containment for the actual finite first-layer GF laws and
the actual simultaneous raw-GD laws at every sufficiently large admissible
width. The argument covers all initial outcomes satisfying (10), not just
one outcome per width. The subsequent reconstruction of actual first-row
increments and velocities, convergence of the three speed densities, and
convergence of all four entries of the node-controlled first kernel are
valid along every stated \(W_2\)-convergent subsequence.

The proof's main vulnerable points survive independent reconstruction:

- The full mixed raw Hessian has the stated \(O(1+\sqrt n)\) bound, with
  constants independent of the input dimension and initial first-row size.
- Raw-GD descent is proved on the actual simultaneous parameter segment
  before loss decrease is used; the stopping argument closes.
- The discrete row-work remainder is absorbed using an envelope proved
  independently of that work estimate.
- The translation estimate is uniform over all admissible GD widths,
  including widths whose mesh exceeds the translation length.
- At \(\rho=-1\), the architecture and opposite labels force the actual
  controlled reverse field into the visible one-dimensional subspace,
  even for a nonzero readout. This validates individual kernel-entry
  reconstruction at the singular endpoint.
- Fourth moments of whole path tuples and finite-rank approximation give
  strong \(W_2\) compactness. The conclusion is not based on weak velocity
  compactness alone.

This verdict does not assert full mean-field identification, convergence
of GF and GD to the same limit, or any conclusion explicitly excluded in
Section 12. Those are not missing obligations of this theorem.

## Isolation, coverage, and source integrity

I read the entire allowed source: **1,623 lines, 66,690 bytes**, including
the theorem, all twelve sections, every numbered display (1)–(106), the
unnumbered arguments, and the provenance appendix. The full initial read
covered consecutive ranges 1–220, 221–480, 481–740, 741–1000, 1001–1260,
1261–1500, and 1501–1623. Subsequent searches were confined to that source
and located its sections and equation numbers.

I did not open any provenance dependency, other project mathematics file,
history, other review, skill file, or other-agent material. I used no
subagents, experiments, numerical simulations, external mathematical
sources, or external imports. This report is based on the supplied text
and direct mathematical reconstruction. The appendix's names and hashes
were encountered only as text within the permitted source.

| Integrity check | SHA-256 |
|---|---|
| User-supplied expected source hash | `910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9` |
| Source hash before reading/audit | `910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9` |
| Source hash after the complete read, mathematical audit, and report creation | `910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9` |

The before and after hashes match the requested version. The source was
not edited. This report is a separate file written with `apply_patch`.
Line references below refer to that unchanged source.

## Theorem-obligation coverage

| Source location | Obligation audited | Assessment |
|---|---|---|
| Introduction and Section 1, lines 1–283, (1)–(21) | Model, metric/topology conventions, deterministic and probability quantifiers, reconstruction and kernel conclusions | Consistent; each asserted conclusion is covered below |
| Section 2, lines 284–427, (22)–(33) | Exact raw gradient, global GF, primal and actual transpose-query bounds, residual derivative | Verified |
| Section 3, lines 428–524, (34)–(42) | Controlled-query envelope, row work, fourth path moments, cubic velocity moments | Verified |
| Section 4, lines 525–644, (43)–(49) | Candidate-exit bounds, complete mixed Hessian, actual simultaneous raw-GD descent and action | Verified |
| Section 5, lines 645–791, (50)–(62) | Recomputed GD query regularity, node increments, noncircular envelope, discrete row work and moments | Verified |
| Section 6, lines 792–853, (63)–(69) | Antiparallel identities with arbitrary actual readout; valid recovery of the controlled field | Verified |
| Section 7, lines 854–1044, (70)–(80) | Relative gate estimate, strong translations, distinction between node and recomputed gates, uniformity over all GD meshes | Verified |
| Section 8, lines 1045–1199, (81)–(86) and unnumbered arguments | Finite-rank errors, whole-tuple fourth moments, finite covers, existence of limits, compact closure, path-space tightness, \(T=0\) | Verified |
| Section 9, lines 1200–1309, (87)–(91) and unnumbered arguments | Gaussian constants, joint failure events, measurability, empirical tails, input and randomness quantifiers | Verified |
| Section 10, lines 1310–1397, (92)–(97) | Closed population compatibility; exact raw-row increments, velocities, and orthogonal-component limitation | Verified |
| Section 11, lines 1398–1552, (98)–(106) and unnumbered arguments | Timewise representatives, all three kinetic limits, full controlled matrix, GD loss derivative, compact observable images | Verified |
| Section 12, lines 1553–1598 | Exact limits of the conclusion | Consistent with the proof; no excluded conclusion demanded |
| Appendix, lines 1599–1623 | Whether an external mathematical result is being imported through provenance | No such import is needed; historical provenance assertions were not independently checked |

## 1. Model, normalization, and geometry

### Equations (1)–(9)

The input assumptions imply
\(C=X^TX/d\succeq0\), with eigenvalues \(1+\rho\) and \(1-\rho\).
Consequently \(\|C\|_{\rm op}\le2\), including the singular endpoint.
For any first-row tangent \(w\),
\(|w^Tx_a|\le\sqrt d\,|w|\). This is exactly the cancellation needed
to remove \(d\) from subsequent raw-metric estimates. No coordinatewise
bound on the inputs is used.

The formulas for arctan are correct. In particular
\[
 |\phi''(x)|=\frac{2|x|}{(1+x^2)^2}
 \le\frac1{1+x^2}\le1.
\]
The prediction has the factor \(1/n\) on the actual readout, and the
loss is the sum of two squared residuals. Those choices are retained in
all gradients and action identities.

The GD convention specifies one simultaneous update evaluated at the old
node. On the raw affine interpolation, \(z^{(1)}\) is affine on each
cell, whereas \(h^{(1)}=\phi(z^{(1)})\) is recomputed and generally is
not affine. Thus \(v^{(1)}\) is a step function and
\(s^{(1)}=\phi'(z^{(1)})\odot v^{(1)}\) uses the recomputed gate. This
distinction is preserved throughout the proof.

The space in (9) is a complete separable normed product, and its two
velocity coordinates carry strong \(L^2\) topology. The time measure is
Lebesgue measure, without division by \(T\); the later powers of \(T\)
are consistent with this convention.

There is no hidden assumption that an arbitrary correlation in the
interior is realizable when \(d=1\). The theorem starts with actual inputs
satisfying (1); in dimension one, its allowed geometry is necessarily the
antiparallel endpoint.

### Quantifiers in (10)–(21)

The deterministic assumptions control the middle spectral norm, readout
supremum norm, and fourth moment of the two first evaluations. They do not
control the raw first-row component orthogonal to the inputs. That
component never affects the finite evaluated dynamics and stays constant,
as (97) later confirms.

The moment and stability estimates use only \(|x_a|^2=d\),
\(|C_{ab}|\le1\), and \(\|C\|\le2\). Dependence on the fixed angle
enters at the recovery of \(e\) from \(v\) in Section 6. The raw-row
pushforward additionally uses the fixed input matrix. There is no claimed
uniform control as a varying correlation tends to an endpoint.

The theorem's restriction to controlled kernel entries, and to held-node
fields for GD, is essential and is implemented correctly. The raw speed
equals the sum over all four controlled entries, not their trace.

## 2. Exact GF and actual transpose-query regularity

### Raw gradient and global existence: (22)–(25)

Direct differentiation gives the three ordinary gradients in (23).
Dividing by the raw-metric block weights gives
\[
 \operatorname{grad}_{\rm raw}\ell
 =\left(
 \frac2d\sum_a r_a\delta^{(1)}_a x_a^T,
 \frac2n\sum_a r_a\delta^{(2)}_a(h^{(1)}_a)^T,
 2\sum_a r_a h^{(2)}_a
 \right).
\]
Its negative is exactly (6), and its Euler update is exactly (7).
Therefore \(\dot\ell=-\|\dot W\|_{\rm raw}^2\), with no missing
sample-average or factor-two correction.

The local contraction construction applies because the finite vector
field is continuously differentiable. On a finite time interval the
energy identity gives a bound on the square-integrated raw speed, hence
\[
 \|W(t)-W(s)\|_{\rm raw}
 \le\sqrt{(t-s)\ell(0)}.
\]
At fixed \(n,d\) the raw metric is positive definite. A putative finite
terminal time therefore has a finite parameter limit, from which local
existence extends the solution. This argument does not require the loss
to be coercive and does prove global finite GF and uniqueness.

### Primal and reverse estimates: (26)–(31)

Initially \(|f_a|\le B\beta\), so \(|r(0)|\le R_0\).
Loss decrease gives \(|r(t)|\le R_0\) and
\(\sum_a|c_a|\le2\sqrt2R_0=K_c^{\rm F}\).
For brevity in this paragraph write \(K_c=K_c^{\rm F}\).
Then
\[
 \|W^{(3)}(t)\|_\infty\le\beta+BK_ct,
 \qquad
 \|\dot W^{(2)}(t)\|_{\rm op}
 \le BK_c(\beta+BK_ct).
\]
Integrating the second inequality gives precisely \(A_{\rm F}\) in
(26), including its factor \(1/2\). The rank-one norm identity applies
to both spectral and Frobenius norms with the ordinary, unnormalized
vector norms.

Writing \(A,M,Q=AM\) for the resulting bounds gives
\[
 \frac{\|z_a^{(2)}\|}{\sqrt n}\le AB,
 \quad
 \frac{\|\delta_a^{(2)}\|}{\sqrt n}\le M,
 \quad
 \frac{\|q_a^{(1)}\|}{\sqrt n}\le AM=Q.
\]
The exact equation \(\dot z_a^{(1)}=\sum_b C_{ab}c_b\delta_b^{(1)}\)
then gives the per-sample velocity bound \(K_cQ\), and the activation
bound follows from \(|\phi'|\le1\). The initial fourth-moment bound
implies \(\|z_a^{(1)}(0)\|/\sqrt n\le m^{1/4}\), yielding (28).

For the actual reverse query the product rules in (30) contain all terms.
They give, in order,
\[
 D_Z=D_AB+AK_cQ,\qquad
 D_\delta=D_w+MD_Z,\qquad
 D_q=D_AM+AD_\delta,
\]
with \(D_A=K_cMB\) and \(D_w=K_cB\), exactly as stated. The estimate
for \(\dot\delta^{(2)}\) uses the coordinatewise bound on
\(W^{(3)}\). No coordinatewise bound on \(q^{(1)}\), no independence
of evolving quantities, and no estimate on \(\dot W^{(1)}\) in an
inappropriate unnormalized metric is being assumed.

### Residual equation and factors: (32)–(33)

The raw inner products of the two prediction gradients are respectively
\[
 C_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,
 \qquad
 \frac{(\delta_a^{(2)})^T\delta_b^{(2)}}n
 \frac{(h_a^{(1)})^Th_b^{(1)}}n,
 \qquad
 \frac{(h_a^{(2)})^Th_b^{(2)}}n.
\]
This verifies all three terms in (32) and \(\dot r=-2kr\).
Each entry is bounded by \(K_*=Q^2+M^2B^2+B^2\), so
\(\|k\|_{\rm op}\le2K_*\). Since \(\dot c=4kr\),
\[
 \sum_a|\dot c_a|
 \le4\sqrt2\,\|k\|_{\rm op}|r|
 \le8\sqrt2K_*R_0.
\]
Thus (33) has the correct coefficient.

## 3. GF row work and improved moments

### Controlled envelope: (34)–(38)

The product rule gives \(\dot u_a=\dot c_aq_a+c_a\dot q_a\).
Minkowski's inequality over neuron indices and the sum over the two
samples give
\[
 \left[\frac1n\sum_i\left(\sum_a|\dot u_{a,i}|\right)^2\right]^{1/2}
 \le D_c^{\rm F}Q_{\rm F}+K_c^{\rm F}D_q.
\]
The same inequality applied to the initial value and time integral proves
the envelope bound (38). The envelope is independent of any later
row-work estimate.

### Row identity and integration by parts: (39)–(40)

For one row, write \(e=\phi'(z)\odot u\). Directly,
\[
 \dot W_i^{(1)}=Xe_i/d,\quad v_i=Ce_i,\quad
 d|\dot W_i^{(1)}|^2=e_i^TCe_i=u_i\cdot s_i.
\]
This remains nonnegative when \(\rho<0\) because \(C\) is positive
semidefinite. Integrating \(u\cdot\dot h\), including both endpoints,
gives
\[
 \mathcal A_i^{\rm F}
 \le B\left(|u_i(T)|_1+|u_i(0)|_1+
                       \int_0^T|\dot u_i|_1\right)
 \le2B\upsilon_i^{(1)}.
\]
There is no sign assumption on the controls or individual coordinate work.

### Reconstruction of the numerical moment constants: (41)–(42)

The spectral inequality \(C^2\preceq2C\) gives
\(|v_i|^2\le2d|\dot W_i^{(1)}|^2\), and
\(|v_i|\le2\upsilon_i^{(1)}\). Therefore
\[
 \int|v_i|^2\le4B\upsilon_i^{(1)},\qquad
 \int|v_i|^3\le8B(\upsilon_i^{(1)})^2.
\]
Also
\(\sup_t|z_i(t)|\le|z_i(0)|+\sqrt{2T\mathcal A_i^{\rm F}}\).
Using \((a+b)^4\le8(a^4+b^4)\) gives
\(8m+128B^2T^2V_{\rm F}^2\) after averaging. Squaring the bound on
\(\int|v_i|^2\) gives
\[
 \left(\frac1n\sum_i\|v_i\|_2^4\right)^{1/2}
 \le4BV_{\rm F}.
\]
All constants in (42) check. The same velocity estimates hold for \(s\)
because \(|s_i|\le|v_i|\). No inverse of \(C\) has been used.

## 4. Actual raw-GD descent and the full mixed Hessian

### Candidate-exit bounds: (43)

Before a first exit from \(|r_k|\le R\), all update controls have
\(\ell^1\) norm at most \(K_c^{\rm G}\). Since \(N\eta\le T+1=H\),
summing the actual readout increments gives \(M_{\rm G}\); summing the
rank-one matrix increments using this readout bound gives \(A_{\rm G}\).
The candidate exit endpoint is included because its increment is
evaluated at the preceding admissible node. Convexity of the spectral and
supremum norms extends these bounds to the full raw segment. No loss
monotonicity has been used here.

### First differential: (44)

For a raw unit tangent, its block norms satisfy
\(a_1^2+a_2^2+a_3^2=1\), in particular \(a_\ell\le1\).
The input normalization gives
\[
 \|\xi^{(1)}x_a\|/\sqrt n\le a_1,
 \qquad
 \|D_\xi z_a^{(2)}\|/\sqrt n\le Ba_2+Aa_1.
\]
Differentiating the readout gives the more resolved bound
\[
 |D_\xi f_a|
 \le Ba_3+M(Ba_2+Aa_1)
 \le B+M(B+A)=F_*.
\]
The bound requires no restriction on \(W^{(1)}\) or its initial moments.

### Full bilinear second differential: (45)–(46)

I checked the mixed derivative for two independent raw unit directions,
not just a repeated-direction second derivative. The hidden derivative
has exactly the three terms displayed in (45): the two mixed
\(W^{(1)}\)-\(W^{(2)}\) terms and the first-gate curvature term. Their
norms divided by \(\sqrt n\) are bounded by
\(1,1,A\sqrt n\), respectively. For the third term,
\[
 \|p\odot q\|\le\|p\|\|q\|,
\]
so two vectors of norm at most \(\sqrt n\) can indeed produce an
\(n\)-sized product. The stated \(\sqrt n\) growth must not be
discarded in the normalized hidden estimate.

The second prediction derivative has four contributions:

1. The mixed readout derivative from \(\xi^{(3)}\): at most \(J_0\).
2. The mixed readout derivative from \(\zeta^{(3)}\): at most \(J_0\).
3. Second-layer gate curvature: at most \(MJ_0^2\).
4. The mixed hidden derivative just computed: at most
   \(M(2+A\sqrt n)\).

The third bound specifically uses
\[
 \frac Mn\sum_i
   |(D_\zeta z_a^{(2)})_i(D_\xi z_a^{(2)})_i|
 \le M\frac{\|D_\zeta z_a^{(2)}\|}{\sqrt n}
        \frac{\|D_\xi z_a^{(2)}\|}{\sqrt n}.
\]
It therefore has no additional \(\sqrt n\). The fourth uses
\(\|W^{(3)}\|\le M\sqrt n\) together with the normalized hidden
bound. These checks give exactly
\[
 F_{**}(n)=2J_0+MJ_0^2+M(2+A\sqrt n).
\]
All mixed blocks of the prediction Hessian are accounted for.

### Actual segment, Hessian of the loss, and descent: (47)–(49)

At an admissible old node,
\(\|g_k\|_{\rm raw}\le K_cF_*\). Integrating the first differential
along \(W_k-tg_k\) bounds each prediction change by
\(\eta K_cF_*^2\). Thus the residual norm on the entire actual segment
is at most \(R+1\) under the first condition in (60).

For arbitrary raw unit \(\xi,\zeta\),
\[
 |D^2\ell[\xi,\zeta]|
 \le 4F_*^2+2\sqrt2(R+1)F_{**}(n)=H_*(n).
\]
Here the first coefficient is \(2\times2\), and the second uses
\(\sum_a|r_a|\le\sqrt2(R+1)\). This is the required raw operator
bound on the full segment, not just at the old node.

Taylor's integral remainder therefore gives
\[
 \ell(W_k-\eta g_k)
 \le\ell(W_k)-\eta\|g_k\|_{\rm raw}^2
       +\frac12\eta^2H_*(n)\|g_k\|_{\rm raw}^2.
\]
When \(\eta H_*(n)\le1\), this proves (48). Inductively it puts the
candidate exit endpoint inside \(|r|\le R_0<R\), so no exit occurs.
Summing the decrease gives (49), including the factor \(1/2\).

This proves descent for the actual simultaneous raw updates. It neither
substitutes a layerwise update nor assumes that the interpolated loss
obeys the GF energy identity.

## 5. GD query regularity, row-work absorption, and threshold

### Recomputed fields and exact differences: (50)–(54)

The raw speeds in (50) are held old-node updates. The product rules (30)
nevertheless hold for the recomputed nonlinear fields on every open cell,
and those fields are continuous at nodes. Using the held speed bounds
and the bounds on recomputed parameters gives the same \(D_Z,D_\delta,D_q\)
as in GF, proving (51).

For the recomputed control,
\[
 \sum_a|\dot c_a|
 =2\sum_a|Df_a[\dot W]|
 \le4K_c^{\rm G}F_*^2.
\]
This estimate uses the first differential on the raw segment; it does not
pretend that its velocity is the gradient at the current interior point.

All three product differences in (52) are exact. The use of
\(W_{k+1}^{(2)}\) and \(W_{k+1}^{(3)}\) in their second terms
includes the mixed-increment contributions. Integrating (51), or bounding
these differences directly, yields the stated \(\eta\)-sized node
increments. Equation (53) follows by integrating the first velocity up
to at most \(H\).

Finally
\(\Delta(c_aq_a)=(\Delta c_a)q_{k,a}+c_{k+1,a}\Delta q_a\)
uses two node controls, both bounded after descent. It gives precisely
\(K_u^{\rm G}=D_c^{\rm G}Q_{\rm G}+K_c^{\rm G}D_q\).

### Envelope and work identity: (55)–(59)

The envelope includes exactly nodes \(0,\ldots,N-1\), which generate the
cell velocities. Summing (54) and applying Minkowski gives (56), including
\(\max_i\upsilon_i^{(1)}\le\sqrt n V_{\rm G}\). This bound is already
available before row work is estimated.

The exact first-row increment gives
\(\Delta z_i=\eta Ce_{k,i}\) and
\(|\Delta z_i|^2\le2\eta^2a_{k,i}\). Componentwise Taylor expansion
of arctan gives
\[
 u_{k,i}\cdot\Delta h_i=\eta a_{k,i}+r_{k,i}^{\rm Tay},
 \qquad
 |r_{k,i}^{\rm Tay}|\le\eta^2\upsilon_i^{(1)}a_{k,i}.
\]
The summation-by-parts formula has the correct terminal term
\(u_{N-1,i}\cdot h_{N,i}\), initial term, and internal variation.
Its absolute value is at most \(2B\upsilon_i^{(1)}\). Consequently
\[
 (1-\eta\upsilon_i^{(1)})\sum_{k=0}^{N-1}\eta a_{k,i}
 \le2B\upsilon_i^{(1)}.
\]
Since \(\eta\upsilon_i^{(1)}\le V_{\rm G}n^{-3/2}\le1/2\),
this gives \(\mathcal A_i^{\rm G}\le4B\upsilon_i^{(1)}\). There is
no circularity between this absorption and the envelope construction.

### Existence of a uniform threshold: (60)

All coefficients in (60) depend only on \(T,\alpha,\beta\). To make
the growth check explicit, write
\[
 H_*(n)=h_0+h_1\sqrt n,
\]
where
\[
 h_0=4F_*^2+2\sqrt2(R+1)(2J_0+MJ_0^2+2M),\qquad
 h_1=2\sqrt2(R+1)MA.
\]
For \(T>0\), one sufficient independently reconstructed choice is an
integer at least
\[
 \max\left\{
 1,\ (\sqrt2K_c^{\rm G}F_*^2)^{1/2},\ (2h_0)^{1/2},
 (2h_1)^{2/3},\ (2V_{\rm G})^{2/3}
 \right\}.
\]
It enforces all three conditions for every larger width. This confirms
the claimed lack of dependence on \(m,d,\rho\), rather than imposing a
trajectory-dependent step restriction.

### Moment constants and the last cell: (61)–(62)

On each raw cell, \(|v_i|\le2\upsilon_i^{(1)}\) and
\(\int_0^T|v_i|^2\le2\mathcal A_i^{\rm G}\le8B\upsilon_i^{(1)}\).
Hence the cubic coefficient is \(16B\). Bounding displacement by
\(\sqrt{2H\mathcal A_i^{\rm G}}\) gives the fourth-path coefficient
\(512B^2H^2\), and squaring the time-integrated kinetic bound gives
the coefficient \(8BV_{\rm G}\) in the final line of (62).

The work sum extends to \(N\eta\), so restriction to a partial final
cell cannot increase these nonnegative action bounds. The activation
derivative uses the recomputed \(z\) and is bounded in magnitude by
\(v\). All three lines of (62) follow with the stated constants.

## 6. Singular input geometry and the actual readout

### Exact endpoint identities: (63)–(67)

At \(\rho=-1\), normalization implies \(x_2=-x_1\). Both hidden
activations are odd, and the readout is linear, so all forward sample
fields and the prediction are opposite at every raw parameter state.
The evenness of \(\phi'\) makes both second deltas and first reverse
queries equal across samples, even when \(W^{(3)}\ne0\).

With the actual labels, \(r_2=-r_1\) and \(c_2=-c_1\). Thus
\(u_2=-u_1\) and \(e_2=-e_1\). Substitution in each of the three
raw update equations yields exactly its factor-two reduction in (66).
Because these are identities for every parameter state, they hold at all
GF times, every GD node, and every raw interpolation state.

On \(E_-\), the matrix \(C\) is multiplication by two. Therefore
\(v=2e\) and \(e=(C/4)v\), as asserted. This checks the otherwise
dangerous kernel-entry obligation: a hidden component of \(e\) in
\(\ker C\) could change individual entries, but the actual endpoint
symmetry rules that component out. It is not being eliminated by an
unsupported pseudoinverse assumption.

### Interior and inverse norm: (68)–(69)

For \(-1<\rho<1\), the displayed inverse is correct and has norm
\((1-|\rho|)^{-1}\). At the endpoint \(D=C/4\) has eigenvalues
\(0,1/2\), so its norm is \(1/2\). All later uses of
\(\kappa_\rho\) are for the fixed permitted geometry.

## 7. Strong time translations and all-width uniformity

### Aggregation and controlled-field shifts: (70)–(72)

The factor \(\sqrt2\) in \(K_z\) converts the two separate sample
velocity bounds into the empirical two-vector bound. The constants
\(J,A_{\rm kin},B_{\rm path}\) match the moments independently checked
above. The same bounds hold for activation velocities.

For GF, integrating the controlled-query derivative over a time shift
gives an empirical \(L^2\) difference at most \(K_u\tau\).
For GD, a shift crosses at most \(\tau/\eta+1\) node increments,
giving \(K_u(\tau+\eta)\). The corresponding first-node position
increments are exactly \(\eta v_k\), giving the second line of (72).
The actual affine position, integrated directly, gives the sharper
\(K_z\tau\) bound in its third line. Integrating over an interval of
length at most \(T\) supplies the factor \(\sqrt T\).

### Relative arctan estimate: (73)–(75)

Since \(|(\log\phi')'|\le1\),
\[
 \frac{|\phi'(x)-\phi'(y)|}{\phi'(x)+\phi'(y)}
 =\tanh\!\left(\frac{|\log\phi'(x)-\log\phi'(y)|}{2}\right)
 \le\min(1,|x-y|/2).
\]
The algebra in (74) is valid for signed \(u,v\): insert
\(\phi'(x)|v|\le|\phi'(x)u|+\phi'(x)|u-v|\).
Taking the maximum gate ratio over the two sample coordinates and then
the Euclidean norm preserves its constants.

The identity \(e=Dv\) yields a space-time \(L^3\) bound
\(\|e\|_3\le\kappa_\rho J\), with empirical neuron measure and
unnormalized time. If \(\theta\) is the maximum gate ratio, then
\[
 \|\theta\|_6^6\le\|\theta\|_2^2
 \le\tfrac14TK_z^2(\tau+\epsilon)^2.
\]
Hölder with \(1/2=1/6+1/3\), applied to the sum of the two shifted
\(e\) norms, gives exactly the second term in (75), including its
factor two and exponent \(1/3\). Multiplication by \(C\) costs at
most another factor two. Absorbing the linear term on
\(\tau+\epsilon\le T+1\) proves (76).

No residual, query, or gate lower bound is used. Strict positivity of
the arctan gate enters only in the valid logarithmic-ratio identity.

### Recomputed activation derivative: (77)

The two-term difference decomposition for \(s=\phi'(z)v\) is exact.
The largest gate difference is bounded by
\(\min(1,|z_i(t+\tau)-z_i(t)|)\). The actual-position shift bound
in (72) and the \(L^3\) bound on \(v\) give
\(J(TK_z^2)^{1/6}\tau^{1/3}\) for the second term. This verifies
(77) without replacing the recomputed activation by a node-held value.

### Removing the mesh uniformly: (78)–(80)

For \(0<\tau\le\eta\), a GD velocity changes under translation only
when the starting time crosses an internal grid node. There are at most
\(T/\eta\) such nodes. Each contributes a starting-time interval of
length at most \(\tau\), and at every starting time
\[
 \frac1n\sum_i|v_i(t+\tau)-v_i(t)|^2\le4K_z^2.
\]
Thus (78) holds, including a partial terminal cell or a horizon shorter
than one mesh cell. For larger shifts the bound \(4TK_z^2\) is valid,
which proves the minimum estimate (79).

For \(0<\tau<\min(1,T)\), set \(\delta=\tau^{3/5}\).
If \(\eta\le\delta\), then
\((\tau+\eta)^{2/3}\le2^{2/3}\tau^{2/5}\).
If \(\eta>\delta\), then
\(\tau/\eta\le\tau^{2/5}\). This proves a uniform squared
velocity-translation bound of order \(\tau^{2/5}\) for every
admissible width, not just asymptotically small meshes. GF has the
stronger exponent \(2/3\). Squaring (77) with a fixed factor-two
inequality supplies the activation term in (80).

This step addresses the fixed-width/all-outcomes issue directly. Leaving
only \((\tau+\eta)^{2/3}\) would not have established the displayed
uniform modulus; the source does remove it.

## 8. Strong joint compactness and tightness

### Finite-rank errors: (81)–(84)

Both time averaging in \(L^2\) and polygonal interpolation in the
supremum norm are bounded contractions. Their joint map has finite rank.
The cell variance identity has factor \(1/(2h)\); splitting into the
two orders of the time pair leaves \(1/h\). Consequently
\[
 \frac1h\int_0^h C_1\tau^{2/5}\,d\tau
 =\frac{5C_1}{7}h^{2/5},
\]
which verifies (82) for both velocity coordinates together.

Absolute continuity gives the displayed polygonal error formula.
Bounding each of its two terms by \(\sqrt h\) times the cell velocity
norm gives a squared supremum error at most \(4h\|v_i\|_2^2\).
After empirical averaging, each continuous coordinate contributes at
most \(4hTK_z^2\). Pairing an entire neuron tuple with its own
projection therefore gives exactly (84). The construction preserves both
samples and all four coordinates jointly.

### Whole-tuple fourth moments: (85)

The bound is
\[
 \mathbb E_{\mu_n}\|\xi\|_{\mathcal E_T}^4
 \le4\left(B_{\rm path}+A_{\rm kin}^2+
                 4B^4+A_{\rm kin}^2\right)=M_4.
\]
The activation contribution is \((\sqrt2B)^4=4B^4\).
Projection does not increase this bound. In particular the whole-path
quadratic tail is controlled by \(M_4/R^2\). This is stronger than,
and distinct from, the cubic bound under empirical space-time measure.

### Finite covers and subsequential measure limits: lines 1106–1175

For each fixed projection range, moving the tail outside radius \(R\)
to zero costs at most \(M_4/R^2\) in squared transport distance.
The remaining finite-dimensional ball has a finite small-diameter cover.
Moving mass to its representatives costs at most the squared diameter.
The simplex of probabilities on this fixed finite set is totally bounded:
matching common masses and moving unmatched mass costs at most that mass
times the squared support diameter. These steps prove total boundedness
of the projected laws. Together with (84), they prove total boundedness
of the entire union of finite empirical laws.

The constructive limit argument is valid. A Cauchy subsequence can be
thinned so that adjacent distances are less than \(2^{-j-1}\); finite
transport tables can then be chosen with root-mean-square cost at most
\(2^{-j}\). Recursive interval splitting on \([0,1]\) realizes their
successive pair laws with the right marginals. Zero-mass rows can be
ignored. Summability of the \(L^2\) costs implies finite expected total
path length and hence an almost-sure Cauchy sequence in \(\mathcal E_T\).
Completeness yields a measurable limit, and the triangle inequality plus
Fatou gives the stated \(L^2\) tail estimate. Its law has finite second
moment and is a \(W_2\) limit.

The extension from the union to its closure is also justified. When a
closure point is approximated by a finite empirical measure, couplings
can be glued through that finite middle marginal: condition on each of
its finitely many positive-mass atoms and take the product of the two
conditional outer laws. Thus this use of the transport triangle
inequality requires no unstated measure-compactness theorem or general
conditional-probability existence result.

The source's last open-cover argument is the usual valid deduction from
sequential compactness and total boundedness. It proves a compact closure
inside \(\mathcal P_2(\mathcal E_T)\), establishing (11).

### Direct tightness and \(T=0\): lines 1176–1199

The set \(\mathcal C\) is closed. Its norm bound and the approximation
requirements place it within \(2^{-j}\) of a bounded finite-dimensional
set for every \(j\), so it is totally bounded and compact. The stated
choice of errors gives
\[
 M_4/R^4+\sum_{j\ge1}2^{2j}\varepsilon(h_j)
 \le a/2+\sum_{j\ge1}a2^{-j-1}=a.
\]
This verifies tightness without losing neuron-coordinate coupling.

At \(T=0\), both velocity spaces are zero spaces and the continuous
coordinates reduce to finite-dimensional evaluations. The initial fourth
moment suffices for compactness, while all time-integrated assertions are
zero-space identities. GD has \(N=0\); one may take \(n_0=1\) in this
case. The separate endpoint paragraph therefore covers the theorem's
zero-horizon statement.

## 9. Gaussian events, measurability, and randomness quantifiers

### Initialization probabilities: (87)–(90)

Each first-row evaluation pair has covariance \(C\), and different rows
are independent. The representation using independent standard normals
is correct, including \(\rho=-1\). Gaussian moment recursion gives
\(\mathbb EG^4=3\), \(\mathbb EG^8=105\), and
\(\mathbb E[G^2(\rho G+\sqrt{1-\rho^2}G')^2]=1+2\rho^2\).
Thus
\[
 \mathbb E|z_i(0)|^4=6+2(1+2\rho^2)=8+4\rho^2\le12,
\]
and
\(\mathbb E|z_i(0)|^8\le8(105+105)=1680\).
The empirical fourth moment has variance at most \(1680/n\); exceeding
13 is a deviation of more than one from its mean. This proves (88).

The sphere packing argument yields a \(1/4\)-net with at most \(9^n\)
points. Replacing both unit test vectors incurs at most half the matrix
operator norm, so the operator norm is at most twice the maximum net
bilinear form. Each such form has variance \(1/n\). Its tail at 4 is
at most \(2e^{-8n}\); the two nets have at most \(9^{2n}\) pairs.
This gives exactly \(2e^{-(8-2\log9)n}\), whose exponent coefficient
is positive. The readout tail at 1 is exactly bounded by
\(2ne^{-n^2/2}\). The sum proves (13); independence of the three
events is unnecessary.

On \(E_n\), the same initialization supplies both deterministic
hypothesis sets. Thus joint GF/GD failure under common initialization is
at most \(b_n\); separate initializations require at most the union
bound \(2b_n\), without an independence assumption. The event itself
does not depend on \(T\); the deterministic set and GD threshold do.

### Measurability: lines 1268–1279

At fixed width, GD is a finite composition of continuous parameter maps,
with a fixed mesh; its positions and strong \(L^2\) velocities depend
continuously on initial parameters. For GF, the action bound controls
solutions from a bounded neighborhood of an initial condition in a common
finite-dimensional ball through time \(T\). The smooth vector field is
Lipschitz there, and the iterated integral inequality gives the stated
\(e^{LT}\) continuous-dependence estimate. Evaluating the vector field
controls the velocities as well. The activation coordinates then follow
by the chain rule and bounded smooth gates. Coupling equal neuron indices
proves continuity, hence measurability, of the finite empirical-law map
in \(W_2\).

### Tail statements and geometry quantifiers: (91), lines 1281–1309

On good events, the two truncation estimates follow respectively from
\(x^2\mathbf1_{x>R}\le x^4/R^2\) for the tuple norm and
\(|v|^2\mathbf1_{|v|>R}\le|v|^3/R\) under empirical space-time
measure. For each fixed positive error level, taking \(R\) large enough
makes the corresponding bad event impossible on \(E_n\), so its
probability is at most \(b_n\) for all sufficiently large widths.
This proves both iterated limits in (91).

These are probability statements about empirical tails. They give no
tail expectation on \(E_n^c\), and the source correctly says so.
Likewise, a \(1/n\) failure upper bound does not yield eventual goodness
almost surely along all widths. The probability bound is uniform for
each deterministic normalized input pair; it is not a simultaneous event
over pairs selected after observing the weights. No such adaptive-input
assumption has entered the proof.

## 10. Population compatibility and raw-row reconstruction

### Closed compatibility set: (92) and the proof of (15)

The primitive map \(v\mapsto\int_0^\cdot v\) is bounded from \(L^2\)
to \(C\) with norm at most \(\sqrt T\). Initial evaluation is continuous
on \(C\), and arctan is Lipschitz. The product estimate (92) proves
continuity of \((z,v)\mapsto\phi'(z)\odot v\) into strong \(L^2\).
The corresponding primitive condition for \((h,s)\) is continuous too.
Hence the set of all compatible tuples in (15) is closed.

Every finite atom belongs to that set, including the recomputed GD
activation pair. Under a coupling with cost \(\varepsilon_n^2\), its
population distance to the set has expectation at most
\(\varepsilon_n\). The bounded distance argument therefore places the
limit in the set almost surely. The endpoint subspace constraints are
closed in exactly the same topologies and pass to the limit as claimed.

### Linear algebra and energy scaling: (93)–(96)

The proven relation \(e=Dv\) gives
\(\dot W_i^{(1)}=XDv_i/d=A_{\rm row}v_i\). In both geometries,
\(D\) is symmetric positive semidefinite and \(DCD=D\). Therefore
\[
 A_{\rm row}^TA_{\rm row}=D/d,\qquad
 d|\dot W_i^{(1)}|^2=v_i^TDv_i,\qquad
 \|A_{\rm row}\|_{\rm op}^2=\kappa_\rho/d.
\]
At the endpoint, \(e=(b,-b)\) gives \(v=(2b,-2b)\) and
\(\dot W_i^{(1)}=2bx_1/d\), whose raw energy is \(4b^2\).
This agrees with \(|v|^2/2\); there is no duplicate row energy.

Integrating the velocity identity gives (96). The map to the raw
increment/velocity pair has squared Lipschitz constant at most
\(4\|A_{\rm row}\|_{\rm op}^2\), since subtracting the initial
evaluation costs a factor at most two in the position supremum norm.
Pushing the chosen couplings through this map proves (17); retaining the
original coordinates adds their original coupling cost and proves the
stated joint convergence.

### Orthogonal component: (97)

For \(P=XD X^T/d\), symmetry and \(DCD=D\) give \(P^2=P\).
Its range is the input span and \(PX=X\), also at the singular endpoint.
The raw update has no component perpendicular to this range, and
\(A_{\rm row}z_i=P W_i^{(1)}\). Thus (97) follows exactly. The
unobserved initial orthogonal component is not controlled by the tuple
law and is correctly excluded from a general full-row-law conclusion.

## 11. Kinetic limits, controlled kernel, and observable compactness

### Timewise representatives: lines 1398–1430, (98)

Time averaging along uniform meshes converges to the identity in
\(L^2([0,T])\): it holds for interval-step functions because the error
is confined to shrinking boundary cells, then for every \(L^2\) path by
density and contraction. Averaged paths are jointly measurable in the
path and time variables. Since their pathwise squared errors are bounded
by \(4\|V\|_2^2\), their averaged error over \(\mu\) tends to zero.

More explicitly, this first defines convergence in the integrated norm
\(\int\|P_hV-V\|_2^2\,d\mu\), which is meaningful without evaluating
an \(L^2\) class at a point. The jointly measurable averages are then
Cauchy in product-space \(L^2\). A subsequence with summable increments
constructs a jointly measurable representative; its section agrees with
the given \(L^2\) class for almost every path. This is the construction
described in the source, and it justifies (98) and subsequent uses of
Fubini/Tonelli. There is no unsupported point-evaluation map on \(L^2\).

### Three speed densities and arbitrary measurable time subsets: (99)–(101)

In a coupling of squared cost \(\varepsilon_n^2\),
\(\|v_n-V\|_{L^2(\text{coupling}\times dt)}\le\varepsilon_n\), and
\(|M_n-M|\le\varepsilon_n\). Factoring a difference of squared norms
and applying Cauchy–Schwarz yields
\[
 \left\|\mathbb E|v_n|^2-\mathbb E|V|^2\right\|_{L^1(dt)}
 \le\varepsilon_n(M_n+M).
\]
The identical argument applies to \(s_n,S\). For the raw form,
\[
 |v^TDv-w^TDw|
 \le\kappa_\rho|v-w|(|v|+|w|),
\]
so the cost is at most \(\kappa_\rho\varepsilon_n(M_n+M)\).
Equation (93) identifies this finite form with
\(d\|\dot W_n^{(1)}\|_F^2/n\), establishing the third speed limit.

Integrating an \(L^1\) error over any fixed measurable subset can only
decrease its absolute bound, so (101) follows. The ordinary unnormalized
matrix speed is indeed \(n/d\) times the raw first-layer speed density.
No kinetic defect remains in any of these three stated densities.

### All four controlled kernel entries: (102)–(105)

The controls are samplewise scalars common to all neurons, so moving them
inside the empirical sum is exact. For GF instantaneous fields and GD
held-node fields alike,
\[
 j_{n,ab}^{(1)}=C_{ab}\frac1n\sum_i e_{a,i}e_{b,i}
 =C_{ab}\frac1n\sum_i(Dv_i)_a(Dv_i)_b.
\]
For two vectors, the outer-product difference has Frobenius norm at most
\(|e-f|(|e|+|f|)\). Hadamard multiplication by \(C\) contracts that
norm because \(|C_{ab}|\le1\). Therefore
\[
 \|\mathcal H(v)-\mathcal H(w)\|_{L^1(F)}
 \le\kappa_\rho^2\|v-w\|_2(\|v\|_2+\|w\|_2).
\]
The same estimate with \(w=0\) gives the integrability bound in (104).
Taking differences under the coupling and applying Cauchy–Schwarz gives
exactly
\[
 \|j_n^{(1)}-J^{(1)}\|_{L^1(F)}
 \le\kappa_\rho^2\varepsilon_n(M_n+M)\longrightarrow0.
\]
This controls the full matrix, including its off-diagonal entries. It
does not require separate convergence of \(c\), \(q\), or the
unweighted deltas, and does not divide by a control.

### Sum identity, positivity, GD loss derivative: lines 1511–1537

Summing all entries gives
\[
 \sum_{a,b}\mathcal H(v)_{ab}
 =(Dv)^TC(Dv)=v^TDv.
\]
This proves both identities in (21). At \(\rho=-1\), an actual row
with \(e=(b,-b)\) contributes \(b^2\) to every entry, so their sum is
\(4b^2\), whereas their trace is \(2b^2\). This independently checks
the important sum-versus-trace distinction.

Positive semidefiniteness follows from congruence of \(C\) by the
diagonal matrix with entries \(Dv\), and passes to expectations. It
does not by itself establish any of the individual convergence claims;
the preceding estimate does.

Inside a GD cell, \(\dot W=-g_k\), so the chain rule gives precisely
(106), the negative raw inner product of the current gradient with the
held old-node gradient. The source correctly does not identify this with
minus the held squared speed. Its kernel convergence result is expressly
for node-controlled fields.

### Compact containment of observables: lines 1539–1552

The raw-row pushforward is Lipschitz at the path level. The three speed
maps and the full matrix map are continuous on \(\mathcal P_2\) by
the preceding coupling estimates. Taking their joint image with the
original law maps the deterministic compact set to a compact set in the
claimed product of two Wasserstein spaces and four \(L^1\) spaces
(three scalar and one matrix-valued). All actual good-outcome observables
belong to this image, so their joint failure event is still contained in
\(E_n^c\). No additional probability or limit-identification hypothesis
is needed.

## 12. Scope and appendix audit

The theorem provides subsequences of deterministic selections in the
uniform good-outcome family, including interleaving the two schemes.
It also provides compact containment in probability for the original
random empirical laws. These are the conclusions proved. Neither one
identifies a unique law or upgrades compact containment to convergence
in probability.

The exclusions in Section 12 are consistent with every preceding step:
there is no all-layer kinetic limit, no recovered unweighted kernel
through vanishing controls, no comparison of node and recomputed GD
kernels, no almost-everywhere convergence claim for the full kernel
sequence, no bad-event expectation estimate, no varying-angle uniformity,
and no general full-row reconstruction without the initial orthogonal
component. The stated further-subsequence almost-everywhere conclusion
from summable \(L^1\) errors is correct by integration of their
nonnegative sum.

The provenance appendix does not invoke a theorem or lemma that the
proof needs from an inaccessible dependency. Its statements about what
the author previously read and which dependency versions were used are
historical assertions, not independently checked in this isolated review.
They play no role in the mathematical verdict. No dependency was opened.

## Required corrections versus optional clarification

### Required mathematical corrections

**None found.** I found no missing hypothesis, incorrect constant,
unaccounted mixed Hessian term, circular descent/work estimate, failure
of all-width uniformity, unsupported singular-endpoint reconstruction,
or gap in the stated strong compactness and controlled-observable limits.

### Optional wording or exposition only

1. **Zero horizon, lines 1195–1198:** explicitly stating “take \(n_0=1\)
   when \(T=0\)” would make the vacuous GD threshold immediate. The
   existing separate zero-horizon argument already suffices.
2. **Closure argument, lines 1159–1164:** the sentence about finite-table
   gluing could explicitly mention gluing through a finite middle
   marginal when the outer laws are not finite. The elementary
   conditional-on-an-atom construction above supplies this step; it
   introduces no new assumption.
3. **Representative construction, lines 1408–1420:** it could first write
   \(\int\|P_hV-V\|_2^2\,d\mu\to0\), and then construct the joint
   measurable representative. This would emphasize that no pointwise
   evaluation is used before choosing that representative. The argument
   already contains the necessary construction.

These suggestions are not conditions for accepting the theorem. They
change neither its hypotheses nor its mathematical conclusions.

## Adversarial checks resolved

| Potential failure | Resolution in the audited proof |
|---|---|
| A hidden \(d\) factor from a first-layer raw tangent | \(\|\xi^{(1)}x_a\|/\sqrt n\le\sqrt{d/n}\|\xi^{(1)}\|_F\); all Hessian and stability estimates use this normalization |
| An omitted mixed Hessian block | Both first/middle mixed terms, both readout mixed terms, and curvature at both hidden layers are present |
| A falsely width-independent Hessian | The first-gate mixed hidden term retains \(A\sqrt n\); \(n^{-2}\) controls it |
| Descent assumed to obtain the region needed for descent | Candidate endpoints and segments are bounded from old-node controls before Taylor descent; the residual exit is then excluded inductively |
| Discrete work depending circularly on its own envelope | Node-query variation establishes \(V_{\rm G}\) first; only then is \(\eta\max_i\upsilon_i\) absorbed |
| Spurious cancellation of the actual Gaussian readout | Endpoint symmetry holds for every readout, with no zero-readout replacement |
| Invisible nullspace control changing endpoint kernel entries | Actual opposite labels and odd architecture force \(e\in E_-\), giving exact \(e=Dv\) |
| Only asymptotic, rather than all-width, velocity regularity | The node-crossing estimate and split at \(\eta=\tau^{3/5}\) give a common vanishing modulus |
| Tightness without strong velocity convergence or quadratic-tail control | Strong finite-rank \(L^2\) errors and a whole-tuple fourth moment give \(W_2\) total boundedness and limits |
| Loss of same-neuron or two-sample coupling | Every atom is a joint four-field, two-sample tuple; projection and transport keep it joint |
| Confusion of raw speed with a trace or unnormalized Frobenius norm | The raw density is \(d\|\dot W^{(1)}\|_F^2/n\) and equals the sum of all four controlled entries |
| Stronger randomness conclusions smuggled in | The proof states compact containment in probability and empirical tail bounds only; bad-event expectations and almost-sure eventual goodness are excluded |

**Final assessment:** the submitted source is mathematically sufficient
for the finite GF/GD first-layer compactness, raw-row reconstruction, and
controlled-kernel subsequence conclusions it states. No source edit is
requested by this review.
