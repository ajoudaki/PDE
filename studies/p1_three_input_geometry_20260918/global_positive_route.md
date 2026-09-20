# Global readout route: exact scalar theorem and the unresolved three-input bridge

Date: 2026-09-18. Status: independently derived, frozen candidate; internally
checked, not independently reviewed or promoted. No numerical experiment or
coefficient evaluation was run. This agent writes only this report.

Scientific inputs were the complete `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10.D.3, and the complete
`initial_geometry.md` and `stationary_geometry.md` in this study. The required
research and rigorous-mathematics skills, including the research-contract and
adversarial-audit references, were read. No other study or competing candidate
was read. The supervisor suggested looking for an initialization-specific
positive argument and, after the scalar result below was communicated, for
transfer to a genuinely three-input open family. No competing derivation was
provided or used.

The target remains an unconditional current-state potential controlling loss
and decaying exponentially in physical time for the full initialized p=1 flow
with unit binary labels and three pairwise nonparallel directions. No future
boundedness, spectral gap, frozen block, changed metric, or small target
amplitude is admissible. **That three-input target is not proved here.** The
positive theorem below is stronger than an axis-specific scalar computation,
but its data class still has one effective input. The exact residual-direction
identity in Section 3 isolates what that theorem loses for three inputs.

## 1. A global theorem for a trainable linear readout and one residual

Let the prediction be

\[
 F(\vartheta,c)=\langle c,H(\vartheta)\rangle_{\mathcal H},
 \qquad \mathcal L=(1-F)^2,
\]

where the readout Hilbert metric is that of \(\mathcal H\), the hidden
variables \(\vartheta\) have their given Hilbert product metric, and both
blocks follow the exact negative gradient of the unhalved loss. Suppose
\(c(0)=0\), \(H_0=H(\vartheta(0))\ne0\), and the equations are locally
well posed with the differentiability needed below and exist at every finite
physical time. Then

\[
        \mathcal L(t)\le e^{-4\|H_0\|^2t}.
        \tag{1}
\]

Thus the current-state potential is the loss itself. This statement does not
freeze or linearize \(H\), and does not require a lower bound on the current
feature norm.

**Proof.** Write \(e=1-F\). The physical equations are

\[
 \dot c=2eH,\qquad
 \dot\vartheta=2e(DH)^*c,\qquad
 \dot F=2e\{\|H\|^2+\|(DH)^*c\|^2\}.
 \tag{2}
\]

At every finite time the coefficient multiplying \(e\) is continuous.
The scalar equation for \(e\), with \(e(0)=1\), therefore keeps \(e>0\).
Introduce the proof-only clock
\(s(t)=\int_0^t2e(\tau)\,d\tau\). It is strictly increasing on finite
intervals. In that clock,

\[
 c_s=H,\qquad \vartheta_s=(DH)^*c,\qquad
 c_{ss}=DH(DH)^*c.                                      \tag{3}
\]

For \(q=\|c\|>0\), differentiate its norm twice:

\[
 q_{ss}
 =\frac{\|c_s\|^2-q_s^2+\langle c,DH(DH)^*c\rangle}{q}
 =\frac{\|c_s\|^2-q_s^2+\|(DH)^*c\|^2}{q}\ge0.
 \tag{4}
\]

Cauchy--Schwarz gives \(q_s^2\le\|c_s\|^2\). As \(s\downarrow0\),
\(c(s)=sH_0+o(s)\), \(c_s(s)=H_0+o(1)\), and hence
\(q_s(s)\to\|H_0\|\). Convexity first holds up to a hypothetical
next zero of \(q\); it gives \(q(s)\ge s\|H_0\|\) there and rules
out such a zero. Thus \(q_s\ge\|H_0\|\) throughout.

Finally \(F=\langle c,c_s\rangle=qq_s\), so

\[
 F_s=q_s^2+qq_{ss}\ge\|H_0\|^2.
\]

Equation (2) gives \(\dot e\le-2\|H_0\|^2e\), proving (1). Every
clock change is only a proof operation; the potential and decay rate refer
to the original physical flow. No past integral is added to its saved state.
\(\square\)

## 2. Application to the complete canonical p=1 model

Set \(\vartheta=(w,M)\), retaining the population \(L^2\) metric for
\(w\) and the full coefficient Frobenius metric for \(M\). For any unit
direction \(u\) and label \(y\in\{\pm1\}\), put

\[
 H(w,M)(b_2)=y\tanh\!\left(b_2^TM E_1[b_1\tanh(w\cdot u)]\right).
 \tag{5}
\]

The complete physical gradient in the source is exactly (2). Bounded
features and bounded tanh derivatives justify (3) on every bounded
characteristic existence ball. The fixed-order continuation theorem provides
existence at every finite time. `initial_geometry.md` proves that the
initialized upper vector is nonzero for every unit direction, so
\(k_0:=\|H(g,D)\|_2^2>0\). Therefore (1) applies for an arbitrary
direction, without assuming that it is a coordinate axis or that the upper
preactivation remains one-dimensional.

The same theorem applies to any probability law supported on
\((u,y)\) and \((-u,-y)\), because input oddness makes their signed
prediction the same scalar \(F\). It also applies to any other *proved*
invariant reduction with one effective residual and the displayed product
gradient structure; merely observing similar loss curves is insufficient.

This proof supplies bounds rather than assuming all-time compactness. In
the clock of Section 1, \(F\ge k_0s\), while \(F<1\), hence
\(s<1/k_0\). The source's contraction normalization gives
\(\|a\|\le1\), \(\|d\|\le\|c\|_2\), and
\(\|D\|_{\rm op}\le2\). Since \(\|c_s\|_\infty\le1\),

\[
 \begin{split}
 \|c(s)\|_\infty&\le s,\\
 \|M(s)-D\|_F&\le s^2/2,\\
 \|w(s)-g\|_\infty
 &\le B_1(s^2+s^4/8),\qquad B_1=\|b_1\|_\infty.
 \end{split}                                                \tag{6}
\]

For the last line, the row speed in this clock is at most
\(B_1(2+s^2/2)s\); integrate from zero. Thus all moving fields converge
in the bounded-displacement/readout/matrix norms as physical time tends to
infinity, and the limiting prediction fits the unit target. No future
coercivity premise was inserted.

The result remains outside the requested nonparallel three-input class.

## 3. The exact term that obstructs the same proof for several residuals

Use the weighted data inner product
\(\langle v,z\rangle_\mu=\sum_i\mu_i v_i z_i\). Define
\(e=y-f\), \(\rho=\|e\|_\mu>0\), and \(v=e/\rho\).
For fixed current hidden state, let

\[
 H_v=\sum_i\mu_i v_i h_i,\qquad
 h_i(b_2)=\tanh(b_2^TMa_i).
\]

Write \(F=(f_1,\ldots,f_m)\), and let \(K=DF(DF)^*\) be the full
prediction Gram operator in the
physical parameter metric and the weighted data metric. It is positive
semidefinite; it contains the readout, lower and middle blocks. The exact
prediction equation is \(\dot e=-2Ke\).

Use \(ds/dt=2\rho\). Set \(k=\langle v,Kv\rangle_\mu\). Direct
differentiation gives

\[
 \rho_s=-k,\qquad
 v_s=-\frac{Kv-kv}{\rho},\qquad
 c_s=H_v,\qquad
 \vartheta_s=(D_\vartheta H_v)^*c.
 \tag{7}
\]

In the last expression, \(v\) is fixed when taking the state derivative.
Differentiating the readout along the actual evolving \(v\) gives

\[
 c_{ss}
 =D_\vartheta H_v(D_\vartheta H_v)^*c+H_{v_s}.          \tag{8}
\]

For \(q=\|c\|>0\), the exact radial identity is now

\[
 q q_{ss}
 =\|H_v\|^2-q_s^2
   +\|(D_\vartheta H_v)^*c\|^2
   +\langle y,v_s\rangle_\mu.                          \tag{9}
\]

Indeed \(\langle c,H_{v_s}\rangle=\langle f,v_s\rangle_\mu
=\langle y,v_s\rangle_\mu\), because \(f=y-\rho v\) and
\(\langle v,v_s\rangle_\mu=0\).

The last term has no determined sign. Neither linearity in the readout nor
the pointwise positive-semidefinite property of \(K\) removes it. Put
\(\beta=\langle y,v\rangle_\mu\); binary unit labels give
\(\|y\|_\mu=1\), so

\[
 \langle y,v_s\rangle_\mu=\beta_s,
 \qquad
 |\beta_s|
 \le \sqrt{1-\beta^2}\,
       \frac{\|(K-kI)v\|_\mu}{\rho}.                  \tag{10}
\]

This is an exact initialization-specific obstruction to extending the
convex-readout-radius proof: initially \(v=y\), \(\beta=1\), but
subsequent rotation of the residual direction can subtract from radial
convexity. The finite-state landscape and singularity statements in
`stationary_geometry.md` supply neither its sign nor a bound on its
accumulated effect. This identifies a missing dynamical estimate, not a
counterexample to exponential convergence.

The identity \(qq_s=\langle f,v\rangle_\mu=\beta-\rho\) provides
a useful check on every factor and sign. Its derivative is
\((qq_s)_s=\beta_s+k\), agreeing with (9) because
\(k=\|H_v\|^2+\|(D_\vartheta H_v)^*c\|^2\).

## 4. Why splitting one direction into three is not yet a small perturbation theorem

This section records a precise transfer test, not a result about the future
three-input trajectory. Consider an axis single-input reference from Section
2 and write test inputs as \(u(\theta)=(\cos\theta,\sin\theta)\).
Its exact invariant axis equations keep \(w_2=g_2\), make \(w_1\)
depend only on the first lower-coordinate pair, keep the second middle row
equal to its initializer, and make \(c\) depend only on the first upper
coordinate. Indeed the second component of the training input is zero;
independence and zero means eliminate the perpendicular feature pairings;
and the perpendicular backward coefficient is zero by upper parity. The
stated equations therefore form an invariant class containing initialization,
and uniqueness preserves it. Reflection of the untouched perpendicular marks
makes the prediction even in \(\theta\), hence \(f'(0)=0\). The reference fits \(f(0)=1\) at
its limiting state. The reference bounds (6), Gaussian moments of \(g\),
and bounded activation derivatives justify the finite input derivatives and
Taylor remainders used here, uniformly on bounded parameter neighborhoods.

At a fixed symmetric reference state, write

\[
 h(\theta)=h_0+\theta h'_0+\tfrac12\theta^2 h''_0+O_{L^2}(\theta^3).
\]

For the three samples \(-\delta,0,\delta\), use the exact feature
coordinates

\[
 h_0,\qquad
 \frac{h(\delta)-h(-\delta)}{2\delta},\qquad
 \frac{h(\delta)-2h_0+h(-\delta)}{\delta^2}.             \tag{11}
\]

They approach \(h_0,h'_0,h''_0\). Whenever this jet Gram is positive
definite, the three original feature singular values have orders
\(1,\delta,\delta^2\); their Gram eigenvalues have orders
\(1,\delta^2,\delta^4\). This follows by the invertible triangular
change from (11) to the original features: the divided-difference Gram
has upper and positive lower bounds, and the reconstruction scales its
three directions by \(1,\delta,\delta^2\).

The second-derivative feature is a genuine new mode in the axis reference.
In active upper coordinates its upper vector derivatives have the form

\[
 z(0)=(z,0),\quad z'(0)=(0,\ell),\quad z''(0)=(j,0).
\]

Here \(z>0\) and \(\ell>0\). To verify the first assertion, in the
axis reference let \(m\) be its moving first active row,
\(v_1=m\cdot b_{1,\mathrm{axis}}\),
\(a=E[b_{1,\mathrm{axis}}\tanh w_1]\), and
\(d=E[b_xc\operatorname{sech}^2(b_xz)]\). As long as \(z>0\),
\(c_s=\tanh(b_xz)\) makes \(b_xc\ge0\), so \(d\ge0\).
The exact equations \(m_s=da\),
\((w_1)_s=dv_1\operatorname{sech}^2w_1\) give
\(z_s=d\{\|a\|^2+E[v_1^2\operatorname{sech}^4w_1]\}\ge0\).
Initialization gives \(z(0)>0\), so continuation preserves it. The
untouched perpendicular initialized row gives
\(\ell=E[\psi(G)G]E[\operatorname{sech}^2w_1]/c_*>0\), with
the strictly increasing odd \(\psi\) of `initial_geometry.md`.
Writing upper coordinates as \((b_x,b_y)\),

\[
 \begin{split}
 h_0&=\tanh(b_xz),\\
 h'_0&=b_y\ell\operatorname{sech}^2(b_xz),\\
 h''_0&=b_xj\operatorname{sech}^2(b_xz)
       -2b_y^2\ell^2\tanh(b_xz)\operatorname{sech}^2(b_xz).
 \end{split}                                               \tag{12}
\]

The positive density on the open upper square proves independence: oddness
in \(b_y\) separates \(h'_0\); the nonzero \(b_y^2\) coefficient
separates \(h''_0\) from \(h_0\).

Suppose the limiting one-input reference has \(f''(0)\ne0\). At
frozen hidden state, any readout correction \(\Delta c_\delta\)
that fits the three unit labels obeys

\[
 \left\langle\Delta c_\delta,
 \frac{h(\delta)-2h_0+h(-\delta)}{\delta^2}\right\rangle
 =-\frac{f(\delta)-2f(0)+f(-\delta)}{\delta^2}.
\]

Cauchy--Schwarz therefore implies

\[
 \liminf_{\delta\downarrow0}\|\Delta c_\delta\|_2
 \ge\frac{|f''(0)|}{\|h''_0\|_2}>0.                  \tag{13}
\]

Allowing all hidden parameters to move by a quantity tending to zero does
not remove this obstruction: uniform Taylor remainder bounds and continuity
of the first two input derivatives would force the reference's second input
derivative to vanish, because every three-point interpolant has zero second
divided difference of its unit targets. Thus a nearby-interpolant argument
must first prove the exceptional second-jet cancellation or accommodate a
finite change in the curvature mode.

No sign or nonzero value of the *limiting* \(f''(0)\) is asserted here.
Its vanishing would itself be an additional theorem. The obstruction says
that simply making the input arc smaller does not establish the needed
small correction: the curvature residual and the curvature feature both
scale as \(\delta^2\). It also explains why a two-point split, with only
the \(\delta\) feature scale and an even reference's \(\delta^2\)
residual, is a materially easier continuation and cannot answer the requested
three-input question.

## 5. Frozen conclusion and remaining proof obligation

The exact positive result is a global exponential theorem for any true
one-residual reduction of a trainable-linear-readout model, with no hidden
coercivity or boundedness assumption. It applies to the complete canonical
p=1 dynamics at any single signed unit direction, and proves bounded
convergence of every moving block there.

For a genuinely nonparallel three-input open family, two specific bridges
remain open: control the negative residual-rotation term (9), or control
the finite curvature-mode adjustment exposed by (13). Neither is supplied
by no bad local minima, initial Gram positivity, or qualitative lower
submersion. This report does not claim the desired three-input theorem,
does not offer a future-coercivity hypothesis as a substitute, and does
not refute existence of some other admissible current-state potential.
