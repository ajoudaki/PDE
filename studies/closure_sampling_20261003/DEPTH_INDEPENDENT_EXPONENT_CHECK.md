# Independent reconstruction of the depth-independent source exponent

2026-10-04. Scoped internal check, not a promotion review or a formal
machine verification.

**Verdict: PASS for the new source refinement, conditional on the
inherited local insertion, real-fitting, and source-to-runtime interfaces
identified by the candidate.** The asymmetric trace estimate removes the
lower-layer coordinate-response factor. The deterministic carrier-moment
interpolation then gives a complex correction tending to zero at the
common radius \(c/\sqrt{\log(en)}\). No stronger label condition is
introduced. Coordinate source error remains \(n^{-1}\), and the
resulting source dimension is
\[
 R\le C\lambda^{-1}[\log(en)]^{3d/2+1}
\]
for the stated sufficiently large widths. Conditional on the unchanged
quadratic runtime, every retained fixed and moving real therefore costs
\(C\lambda^{-2}[\log(en)]^{3d+2}+Cm(d+1)\), with the same all-time
whole-sphere root-width approximation.

## 1. Frozen source and audit boundary

The complete reviewed source is DEPTH_INDEPENDENT_EXPONENT.md at SHA-256
5da4e4593a040c82a8b12b2c63dea334cf65a3d4dd7e1dc0d48921102adf2932.
The complete DEPTH_EXPONENT_ROUTE.md and all six named source dependencies
were already read for the first scoped check. Their hashes are recorded
in DEPTH_EXPONENT_CHECK.md; the reviewed versions are unchanged.
No other current review report or linked prior-study theorem was read.

The coordinator supplied the proposed asymmetric trace mechanism and
the author's proposed interpolation formula before this check. Neither
was treated as evidence: Sections 2--5 below reconstruct the norms,
normalizations, summability, and interpolation. No inherited PASS label
was used as a proof.

This is an audit of the new implication from the displayed source
interfaces. The prior-study local Gaussian insertion theorem, the
real-fitting theorem at \(Y\le c\lambda\), and the quadratic-storage
autonomous runtime remain inherited inputs, as they do in the candidate.
The local augmented graph and complex-contour extension actually given
in DEEP_COMPLEX_SOURCE.md and DEEP_ACTIVATION_EXTENSION.md were read
completely and checked for compatibility with the new stops and radius.

Keep the candidate's physical model and notation:
\(\ell_n=\log(en)\), \(\lambda=\min(1,\gamma/m)\),
\(S=C_0Y/\lambda\), \(T=C\lambda^{-1}\ell_n\), and
\(\rho=\|f-y\|_2/\sqrt m\). The forward pass, zero initial readout,
independent Gaussian initialization, loss normalization, mobilities, and
physical time are unchanged. Depth is fixed; removing it from a
logarithmic power does not remove it from constants or width thresholds.

## 2. Endpoint Hilbert--Schmidt norms are independent of coordinate caps

Use mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\)
and \(F_b=nf(v_b)\). The forward derivative maps
\(D_\Theta z^{(p)}\) and \(D_\Theta h^{(p)}\) have bounded operator
norm on the pole-safe physical tube. This follows recursively:
the direct map \(U_A\mapsto U_Av\) has norm \(\|v\|_2\);
the direct hidden map \(U_H\mapsto U_Hh/\sqrt n\) has norm
\(\|h\|_2/\sqrt n\); bounded gates and mixers propagate those bounds.
Their output rank is at most \(n\).

The hidden part of \(\nabla_\Theta F_b\) has Euclidean norm
\(CS\sqrt n\). Thus the residual-free responses
\[
 R_b^{(p)}=D_\Theta z^{(p)}\nabla_\Theta F_b,\qquad
 Q_b^{(p)}=D_\Theta h^{(p)}\nabla_\Theta F_b
\]
have RMS at most \(CS\). The readout-gradient block contributes
nothing to a hidden forward derivative. The angular response
\(J_j^{(p)}=\partial_{\theta_j}z^{(p)}\) has RMS at most \(C\),
starting from \(\|A\|_F/\sqrt n\le C\) and bounded sphere-map
derivatives. These facts precede all coordinate cap improvements.

For a rectangular map \(M\), put
\(\|M\|_{u,n}=n^{-1/u}\|M\|_{S_u}\).
The supplied Hessian decomposition consists of bounded-map contractions
of single carrier diagonals and bounded-operator terms of rank \(O(n)\).
Carrier RMS is \(CS\), so
\(\|D_\Theta^2F_b\|_{2,n}\le C\), independently of the carrier
maximum and of all forward/angular coordinate caps.

Differentiate \(Q_b^{(p)}\):
\[
 D_\Theta Q_b^{(p)}
 =D_\Theta h^{(p)}D_\Theta^2F_b
   +D_\Theta^2h^{(p)}[\,\cdot\,,\nabla_\Theta F_b].
                                                               \tag{1}
\]
The first summand has normalized Hilbert--Schmidt norm at most \(C\).
In the second, the gate-curvature term is
\(\operatorname{diag}(\phi_p''R_b^{(p)})D_\Theta z^{(p)}\),
whose normalized Hilbert--Schmidt norm is at most
\(C\|R_b^{(p)}\|_2/\sqrt n\le CS\). This uses the RMS of \(R_b\),
not its coordinate maximum.

The direct mixed hidden map is
\(U_H\mapsto U_H Q_b^{(p-1)}/\sqrt n\).
Summing its squared images of the matrix-coordinate basis gives exactly
\(\|Q_b^{(p-1)}\|_2^2\), so its normalized Hilbert--Schmidt norm
is at most \(CS\). The other mixed map is the rank-one matrix
\(\delta_b^{(p)}h_b^{(p-1)\top}/n\) composed with a bounded
forward derivative. Its operator norm is at most \(CS\), hence its
normalized Hilbert--Schmidt norm is also bounded. The remaining lower
mixed derivative is multiplied by a bounded mixer. Since the first
preactivation has zero second parameter derivative, finite induction
in (1) proves \(\|D_\Theta Q_b^{(p)}\|_{2,n}\le C\).

For \(q=\partial_\theta h^{(p)}\), the same argument replaces
the gate diagonal \(R_b^{(p)}\) by \(J_j^{(p)}\). The direct first
mixed map \(U_A\mapsto U_A\partial_\theta v\) has squared
Hilbert--Schmidt norm \(n\|\partial_\theta v\|_2^2\).
The hidden mixed maps have the preceding matrix-coordinate calculation.
Thus \(\|D_\Theta q\|_{2,n}\le C\) independently of all angular
coordinate caps.

These computations also verify the rectangular cavity versions, up to
fixed factors: deleting finitely many output coordinates cannot enlarge
the displayed rank or matrix-coordinate sums. Complex algebraic
transposes in the definitions do not invalidate the singular-value
norm inequalities.

## 3. Asymmetric trace estimate and the Dyson sum

The relevant normalized trace is
\[
 n^{-1}\operatorname{tr}
   \{D_\Theta q(t)\,\mathcal J(t,s)\,C_a(s)^\top\},
 \qquad C_a=D_\Theta h_a^{(p)}.                         \tag{2}
\]
The endpoint \(C_a\) has bounded operator norm and rank at most \(n\).
The endpoint \(D_\Theta q\) has the normalized Hilbert--Schmidt
bound proved above. The exponent-\(u\) Hessian estimate supplied by the
separate budgets is
\[
 \|\mathcal A(s)\|_{u,n}
 \le C[1+Su(2B)^{1/u}],\qquad u\ge2,                  \tag{3}
\]
where \(\mathcal A\) is normalized by absolute residual activity.
It holds for every sample mixture by the triangle inequality; no
common sample index is needed between successive factors.

For a Dyson term with \(h\ge1\) Hessians, assign Schatten exponents
\(2\) to \(D_\Theta q\), \(\infty\) to \(C_a\), and \(2h\)
to each Hessian. Their reciprocal sum is exactly
\(1/2+h/(2h)=1\). Consequently their factors \(n^{-1/u}\)
multiply to the required \(1/n\); no factor involving the
\(O(n^2)\) parameter-space dimension is left over.
All base propagators use operator norms. Their product is at most
\(e^{Cr_n}\), since only the total short non-real/backwards contour
length contributes growth and the positive-real base is contractive.

Integrating the ordered activity simplex, whose total mass is \(CS\),
bounds the term by
\[
 \frac{C(CS)^h}{h!}
       [1+CS(2h)(2B)^{1/(2h)}]^h.                     \tag{4}
\]
For \(h=0\), use both endpoint Hilbert--Schmidt norms; the rank
bound gives \(\|C_a\|_{2,n}\le C\). This is necessary because
the \((2,\infty)\) pair alone would not give a trace bound.

Using \((a+b)^h\le2^{h-1}(a^h+b^h)\), the sum of (4) is bounded by
\[
 C\sum_{h\ge1}\frac{(CS)^h}{h!}
 +C\sqrt{2B}\sum_{h\ge1}(CS^2)^h\frac{h^h}{h!}.
                                                               \tag{5}
\]
Since \(h!\ge(h/e)^h\), the second sum is at most
\(C\sqrt B\,S^2/(1-CS^2)\) for small structural \(S\).
The inherited \(S^2B\le c\), with \(B\ge1\), already makes this
structurally bounded. It is weaker than no previous requirement and
introduces no new label penalty.

Thus (2) is bounded independently of the lower coordinate cap \(A_p\).
The outside reverse-source integral costs only \(CSM_n\).
The source's direct reverse trace costs \(CM_n\), its Gaussian
term costs \(CS\sqrt{\ell_n}\), and its learned-row correction
costs \(CS^2M_n\). None reintroduces \(A_p\).

## 4. The new maximum and all-layer response stops are compatible

Impose separate exponential budgets \(B\), carrier maximum
\(M_n=C_*S\sqrt{\ell_n}\), forward caps
\(C_\ell S\sqrt{\ell_n}\), angular caps
\(C_\ell\sqrt{\ell_n}\), and the usual fixed pole and physical
tubes. Each cavity has its own doubled caps.

The maximum-stop proof still uses only the coarse differentiated
backward estimate
\(\|\dot\delta\|_2/\sqrt n\le C\rho(1+SM_n)\); it does not need
Section 5 below. A cavity-measurable clamping to the containing time
rectangle preserves independence from its omitted Gaussian root.
At each deterministic grid point, the root pairing has variance
\(CS^2\). A mesh of size \(n^{-2}\) has polynomial cardinality,
and the off-grid error is at most \(n^{-3/2}\) times a fixed
polylogarithm on a bounded root-norm event. Gaussian tails at
\(C_GS\sqrt{\ell_n}\), unioned over fixed layers and samples and
all neurons, therefore tend to zero.

The supplied singleton insertion shift is
\(CS(1+S^2B)+o(1)\). It is negligible compared with
\(S\sqrt{\ell_n}\) for fixed positive \(S\). Choosing structural
\(C_*>2C_G\) therefore improves the carrier maximum before the
budgets are removed. The same local coordinate comparison transfers all
full stops to doubled cavity stops. Cavity survival is not used as a
conditioning event in the Gaussian law.

With Section 3 replacing the trace in the original response recursions,
\[
 \max|R_b^{(p+1)}|
 \le C(M_n+S\sqrt{\ell_n}+SM_n+S^2M_n)+o(1),
\]
\[
 \max|J_j^{(p+1)}|
 \le C(\sqrt{\ell_n}+SM_n)+o(1).
                                                               \tag{6}
\]
Both have the proposed \(\sqrt{\ell_n}\) power at every layer.
The first-layer starts use the exact
\(R_b^{(1)}=\delta_b^{(1)}v_b^\top v\), Gaussian first-weight
row norms, and the row displacement \(CSM_n\).
The constants can be chosen successively with strict margins.
Although operator estimates inside the local insertion graph may use
the imposed caps, the trace bound in (6) does not use their size.

The enlarged insertion graph still has only fixed polylogarithmic
controls, an inverse-polylogarithmic contour width, and the same strict
negative powers of \(n\) in its Taylor remainders. The original
Gaussian control-net exponent and the stronger tail exponent remain
separated. The total non-real propagation length is now
\(O(\ell_n^{-1/2})=o(1)\). Thus the stated local insertion interface
continues to apply; no new finite-power loss is introduced.

## 5. The improved backward derivative is a deterministic consequence

On the stopped tube, forward differentiation and (6) give
\[
 \|\dot z_a^{(\ell)}\|_{2,n}\le C\rho S,\qquad
 \|\dot z_a^{(\ell)}\|_\infty\le C\rho S\sqrt{\ell_n}.
                                                               \tag{7}
\]
For every real \(u\ge4\), the still-imposed exponential budget gives
\[
 \|k_a^{(\ell)}\|_{u,n}\le CSu(2B)^{1/u}.              \tag{8}
\]
This follows from \(x^u\le(u/e)^u e^x\) pointwise and does not
invoke a probabilistic moment estimate. At the top layer, the stronger
coordinate bound \(\|w\|_\infty\le CS\) also implies (8).

Set \(v=2u/(u-2)\). Then \(1/u+1/v=1/2\) and
\(1-2/v=2/u\). Interpolation in the normalized counting measure gives
\[
 \|\dot z_a^{(\ell)}\|_{v,n}
 \le(C\rho S\sqrt{\ell_n})^{2/u}
       (C\rho S)^{1-2/u}
 =C\rho S\ell_n^{1/u}.
\]
Hölder with (8) therefore proves
\[
 \|k_a^{(\ell)}\odot\dot z_a^{(\ell)}\|_{2,n}
 \le C\rho S^2u(2B\ell_n)^{1/u}.                     \tag{9}
\]
Choose \(u=\max(4,\log(2B\ell_n))\). The last exponential factor
is at most \(e\) once the logarithm selects \(u\), and remains
bounded in the other case. Since \(B\) is fixed structurally, this is
\(C\rho S^2\log(e+\ell_n)\), with no sample or gap denominator.

Differentiate the backward recursion exactly. The changed-gate term is
bounded by (9); the term \(\dot W^\top\delta\) has RMS
\(C\rho S^2\), and \(\dot w\) has RMS \(C\rho\).
Bounded mixers and gates propagate these estimates through fixed depth:
\[
 \max_{a,\ell}\|\dot\delta_a^{(\ell)}\|_{2,n}
 \le C\rho[1+S^2\log(e+\ell_n)].                      \tag{10}
\]
No derivative of the carrier maximum or budget is taken.
If \(\rho=0\), the physical vector field vanishes and the same
inequality holds directly.

The growing real exponent \(u\) in (9) is legitimate: it is chosen in
an exact deterministic inequality on a stopped sample. It is not the
fixed-block empirical moment degree. The latter remains fixed before
the width limit in Section 6.

## 6. Complex moments, pole margins, and closure of the stops

At common radius \(r_n=c\ell_n^{-1/2}\), (6) bounds the imaginary
preactivation displacement along time and angular segments by
\(Cc(1+SY)\). Choosing structural \(c\) small gives a fixed strict
pole margin. The trace for a next query layer uses only lower query
gates and the stopped training responses, so this pole step does not
assume its own conclusion.

For \(z=t+is\), anchor the real response at \(t_+=\max(t,0)\).
The negative-real and vertical pieces have combined length at most
\(2r_n\). The normalized complex residual bound gives
\(\rho\le CY\), and \(Y/S=C\lambda\le C\). Integrating (10) proves
\[
 \frac{\|\delta_a(z)-\delta_a(t_+)\|_2}{S\sqrt n}
 \le D_n:=C\ell_n^{-1/2}\log(e+\ell_n).                \tag{11}
\]
The normalized horizontal and vertical Lipschitz constants are at most
\(C\log(e+\ell_n)\). At \(t=0\), continuity and the bounds on
each side give the same global Lipschitz estimate. Cavity-measurable
clamping preserves it.

The two-parameter covering number at Gaussian metric scale
\(\epsilon\) is at most
\((C\lambda^{-1}\ell_n^C/\epsilon)^2\).
The dyadic net beginning at radius \(D_n\) has mean supremum
\[
 CD_n\sqrt{\log(C\lambda^{-1}\ell_n^C/D_n)}
 =O_{\lambda}(\ell_n^{-1/2}[\log(e+\ell_n)]^{3/2})
 \longrightarrow0.
\]
Its Gaussian tail scale is \(CD_n\to0\). Integrating this tail
proves that each fixed exponential moment of the correction tends to
one. Thus no extra \(\log\log n\) factor is needed in the time radius.

The nonnegative real reference has the inherited single-sample
activity-clock Gaussian moment. Cauchy--Schwarz combines it with (11).
This yields a structural complex moment bound before summing over
samples. Choose a structural budget \(B\), then take \(S\) small
for the already present \(S^2B\), \(S^2\log(e+B)\), and local
insertion conditions. Section 3 adds no stronger condition.
The deterministic interpolation introduces none.

The common-cavity projected difference still has a negative-power
Gaussian radius and polynomial-grid derivative bounds. Fixed-block
moments therefore retain a base independent of their fixed degree
\(p\). For each such degree, the budget-hit probability has limiting
upper bound \(m\vartheta^p\), \(0<\vartheta<1\).
Take \(n\to\infty\) first, then the infimum over fixed \(p\).

The full dependency order is:
impose all stops; transfer to doubled cavity stops; exclude the maximum
by the polynomial Gaussian grid; exclude responses using the asymmetric
trace; exclude poles; use stopped deterministic moments to prove
(10)--(11); finally remove exponential budgets. All Gaussian references
use only their own retained initialization and stops. This rules out
the proposed circular conditioning failure.

Strict pole, response, physical, and carrier margins then give
holomorphic continuation to the whole rectangle and a neighborhood of
its closure. The probability statement uses the refined intersection
of the required Gaussian and initialization events; a bare assertion
about the older, smaller-domain event alone would not supply this
continuation.

## 7. Count, labels, accuracy, and inherited autonomy

The whole-query backward induction on this domain uses only bounded
complex gates, mixer operator norms, and readout RMS. Therefore every
coordinate of all four required source families, including paired
initialized matrix images in both orientations, is bounded by
\(C\sqrt n\). Their passive-query backward magnitude is used only
for analytic approximation, not as the carrier bound in the dynamical
comparison.

The coordinate error supplied to the runtime is still
\(\epsilon_n=n^{-1}\). Since
\(\log(C\sqrt n/\epsilon_n)=O(\ell_n)\), the explicit degree
bounds with \(q_n=\ell_n+\log(e/\lambda)\) are
\[
 p\le C\lambda^{-1}\ell_n^{3/2}q_n,\qquad
 J\le C\ell_n^{1/2}q_n.
\]
There are \(d-1\) angular variables, so
\[
 R\le C(p+1)(2J+1)^{d-1}
 \le C\lambda^{-1}\ell_n^{d/2+1}q_n^d.                \tag{12}
\]
The exact initialization additions cost \(O(m+d)\), absorbed by the
existing trace constraint \(m\lambda\le B_\phi^2\). For
\(\ell_n\ge\log(e/\lambda)\), (12) becomes
\(R\le C\lambda^{-1}\ell_n^{3d/2+1}\).
This absorbs a logarithmic gap factor only; it hides no extra
polynomial sample factor.

Identical scalar interpolation operations on every initialized
matrix-image pair preserve the exact pair interface. The finite
initial-jet analytic continuation procedure is still allowed and still
needs no trained-path query. Temporary original-width arrays are not
retained in the reduced runtime.

Squaring (12) in the inherited total-storage theorem gives
\[
 C\lambda^{-2}\ell_n^{d+2}q_n^{2d}+Cm(d+1),
\]
and hence \(C\lambda^{-2}\ell_n^{3d+2}+Cm(d+1)\).
For the uncapped gap this is \(Cm^2\gamma^{-2}\ell_n^{3d+2}
+Cm(d+1)\). Depth remains in structural constants and thresholds.

The label range stays \(Y\le c\lambda\); neither the asymmetric
trace, interpolation, Gaussian grid, nor pole margin imposes another
power of \(m\) or \(\lambda\). The fixed-data width threshold may
still depend on \(Y>0\), confidence, gap, samples, and depth.
The zero-label case is stationary and separate.

Because \(\epsilon_n=n^{-1}\), the inherited one-reference stability
bound is still \(n^{-1}\exp(C_{\rm data}\sqrt{\ell_n})\) up to
fixed-data factors, and is eventually at most \(C_{\rm data}/\sqrt n\).
The source horizon is still \(T=C\lambda^{-1}\ell_n\);
both systems' exponential tails therefore still supply the same
all-time estimate, including the endpoint. No stronger source accuracy,
trained trajectory, or population comparison is introduced.

The autonomous corrected-readout optimizer, its actual own-residual
identity, trained hidden matrices, physical clock, and count of all
fixed metric and moving parameter arrays are inherited unchanged.
This check proves a source refinement for that interface. It does not
establish ordinary-gradient-flow compression, efficient preprocessing,
bounded-precision stability, growing-depth quantifiers, an input-
dimension-independent exponent, or an unrestricted storage lower bound.
