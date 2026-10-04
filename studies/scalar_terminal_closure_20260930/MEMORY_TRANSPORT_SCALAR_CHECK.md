# Internal check of the memory-transport scalar continuation

Date: 2026-10-01.

Verdict: **PASS for the clarified candidate.** The q=2 formulas, product
identity, exact handoff matching, finite-time existence, local restart
example, general-q control representation, counts, and query parity are
correct. No further mathematical correction is required. The construction
is an untested scalar approximation to the full closure; this verdict
does not assert initialized reachability, improved accuracy on the circle
tasks, or a compression rate.

Final candidate `MEMORY_TRANSPORT_SCALAR.md` SHA256:

`2303ddfeda66201bf8ec6a8874de1a95027a35bd385d33c24dde73cadeb6cc6b`

The complete initial candidate was read at SHA256
`9fd5a50cd983ab4a9071c60dd2660ea90a666e4b1ece7b35433c4da233ec7067`,
then the amended paragraphs in Sections 5–6 were read and the final hash
verified. The amendments distinguish forward/value transport exponents
and state the uniformity and observable hypotheses for terminal bounds.

Allowed dependencies were the previously read complete
`HIGHER_ORDER_SCALAR.md` (SHA256
`848e0903b4a42aafa5c6b24c4e83be4c59531c5b77efa4147113e97e7c17cfe2`)
and `TERMINAL_SCALAR_THEOREM.md` (SHA256
`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`),
whose hashes were rechecked. Shared instructions and the previously read
`solve-math-rigorously` skill apply. No other study, new experiment,
empirical artifact, or external source was read. This is a cooperative
internal mathematical check, not an independent promotion review. Only
this report was written by the checker.

## q=2 reconstruction and the factor four

The endpoint derivatives follow directly from the full q=2 mode equations:

\[
\dot k^*=\alpha(4h-4k_0-6k_1)
=\alpha(4h-2k^*-2k_0),
\]
\[
\dot v^*=-8rd-3\alpha(v_0+v_1)
=-8rd-\alpha(v^*+2v_0).
\]

Thus endpoint sums alone do not determine their next velocities when the
individual lower modes are unspecified.

For a fixed query/example pair, put \(\Delta=U_0^0-H\). Since
\(\dot s=-\alpha s\), differentiation of
\(U_0=H+s\Delta\) and
\(U_1=s^2U_1^0+(s^2-s)\Delta\) gives

\[
\dot U_0=\alpha(H-U_0),\qquad
\dot U_1=\alpha(H-U_0-2U_1).
\]

Both initial values are recovered at \(s=1\).
The shared controls satisfy \(I_a'=\widehat r_a\) and
\((\tau J_a)'=\tau\widehat r_a\), which proves the stated integral
representation of \(J_a\). For the value formulas, direct differentiation
gives

\[
\dot V_0=-2D\widehat r_a,
\]
\[
\dot V_1=-2D\widehat r_a
-\alpha\left[s(V_0^0+V_1^0)-4DJ_a\right].
\]

The bracket equals \(V_0+V_1\), so the required projected value equation
holds. In particular, the coefficient \(-4DJ_a\) is necessary: its
derivative combines with \(+2DI_a\) to produce the correct forcing
\(-2D\widehat r_a\). The integration-by-parts derivation in the note
has the same signs and factors.

## Product identity and exact initial velocity

Differentiating \(U_0V_0+3U_1V_1\) using the four projected equations
gives a residual-forcing part
\(-2D\widehat r_a(U_0+3U_1)\). The remaining part is

\[
\alpha\left[H(V_0+3V_1)-U_0V_0-3U_0V_1
-3U_1V_0-9U_1V_1\right],
\]

which factors exactly as the second term of equation (6).

The factor \(1/m\) in the query output reconstruction is correct.
The frozen output Jacobian applied to a memory matrix increment is

\[
\frac1n d_x^T\Delta B\,h_x
=\frac1m\sum_{a,j}(2j+1)
\left[U_jV_j-U_j^0V_j^0\right],
\]

because each scalar contraction already contains its own factor \(1/n\).
The readout and read-in Jacobian contributions are precisely
\(-\sum_a C_{\rm outer}(x,a)I_a\).

Consequently the proxy's output derivative has response coefficients

\[
C_{\rm proxy}(x,a)=C_{\rm outer}(x,a)
+\frac2m D(x,a)(U_0+3U_1)(x,a),
\]
\[
b_{\rm proxy}(x)=\frac1{m\sqrt m\tau}\sum_a
(V_0+3V_1)(x,a)(H-U_0-3U_1)(x,a).
\]

At the handoff these are exactly the full q=2 coefficients. The initial
outputs, training residuals, clock, and output velocities therefore
match for every represented query before any basis approximation. This
is initial matching of the actual q=2 network; it is not exact trajectory
matching after neural fields evolve.

If \(\widehat r=0\), all shared-control and clock velocities vanish.
The algebraic query outputs then also stop. No zero-residual division or
hidden exception is present.

## Finite-time global existence

The residual is a smooth algebraic function of \((I,J,\tau)\) on
\(\tau>0\). Composing its norm with the smooth coefficients gives a
locally Lipschitz vector field, which supplies local existence and
uniqueness. Along a forward solution, \(\tau'\ge0\), so
\(\tau\ge\tau_0\) and \(s\in(0,1]\).

The reconstructed \(U\)'s are bounded on that interval of \(s\).
The reconstructed \(V\)'s, and hence the residual, are affine in
\((I,J)\) with uniformly bounded coefficients there. Thus
\(\|\widehat r\|\le K(1+\sqrt E)\), where
\(E=\|I\|^2+\|J\|^2\). Since \(\alpha\ge0\),

\[
\dot E\le2\sqrt{2E}\,K(1+\sqrt E)
\le3\sqrt2K(1+E).
\]

This supplies one explicit valid choice of the claimed growth constant.
The resulting exponential finite-time bound on \(E\) bounds \(\tau'\)
and then \(\tau\) on every finite interval. The state remains in a
compact subset of the locally Lipschitz domain, so it extends past any
hypothetical finite maximal time. The proof does not imply boundedness
as time tends to infinity, convergence, or fitting, exactly as stated.

## Arbitrary-restart example

At the displayed state, all values and keys vanish, while
\(\dot v_0=\dot v_1=2\) and
\(\dot k_0=\dot k_1=h\). Therefore

\[
\ddot B(0)=2\dot v_0\dot k_0
+6\dot v_1\dot k_1=4h+12h=16h.
\]

Because \(B=\dot B=g=\dot A=\dot w=0\), differentiating
\(f=w\tanh(Bh)\) gives \(\ddot f(0)=h\ddot B(0)=16h^2\).
The frozen response has both coefficients zero and keeps its output zero.

For the proxy, \(H=h^2,D=1,C_{\rm outer}=0\), and all initial projected
memories vanish. Its projected derivatives satisfy
\(\dot U_0=\dot U_1=h^2\) and
\(\dot V_0=\dot V_1=2\). Equation (4) then yields the same
\(\ddot{\widehat f}(0)=16h^2\). Both fields are smooth in a neighborhood
where the scalar residual remains negative. Taylor's theorem therefore
gives the stated \(O(t^3)\) proxy error, versus the nonzero leading
\(8h^2t^2\) frozen-response error when \(h\ne0\).

This is admissibility for the autonomous ODE at \(\tau>0\), not a proof
that the stated memories or zero mixer are generated by the prescribed
Gaussian initialization and history prefix. The candidate explicitly
excludes that reachability claim. The example is outside the positive
terminal-margin case and demonstrates a local mechanism only.

## General q, storage, and parity

The clarified transport matrix \(T\) has distinct eigenvalues
\(0,\ldots,q-1\), so it has an invertible eigenvector matrix \(S\)
with \(T=S\operatorname{diag}(j)S^{-1}\). For each query/example pair,
the projected value solution has the explicit form

\[
V=S\operatorname{diag}(s^j)S^{-1}V^0
-2D\,S\operatorname{diag}(Z_j)S^{-1}\mathbf1.
\]

This follows directly by applying the integrating factor \(\tau^j\)
to each diagonal coordinate, and it verifies that exactly q residual
controls per example suffice. The projected forward solution is

\[
U=H e_0+S\operatorname{diag}(s^{j+1})S^{-1}(U^0-He_0),
\]

where \((T+I)e_0=\mathbf1\). This also verifies the clarified
distinction between value powers \(s^0,\ldots,s^{q-1}\) and forward
powers \(s^1,\ldots,s^q\), plus the forward constant term. These
identities remain valid when activity stops; no inversion of the clock
or division by its speed is required.

For fixed q the forward coefficients are bounded, values are affine in
the controls, and the residual is affine in them. The energy identity is

\[
\frac d{dt}\sum_j\|Z_j\|^2
=2\left(\sum_jZ_j\right)^T\widehat r
-2\alpha\sum_jj\|Z_j\|^2.
\]

The same growth estimate, with a q-dependent constant, proves finite-time
existence. No uniform-in-q conditioning estimate is implicit.

The fixed training arrays consist of \(2q\) projected-memory matrices
plus \(H,D,C_{\rm outer}\), followed by \(r^0\) and \(\tau_0\).
Their count is exactly \((2q+3)m^2+m+1\): 457 fixed numbers for q=2,
m=8, plus 17 moving controls. The moving counts 9/17/25 for q=1/2/3
and the per-query count \(1+(2q+3)m\) are correct for this formulation.

Under query antipodal reflection, \(h_x,g_x,f_x\) are odd, while
\(d_x,\ell_x\) are even. Thus \(H,U_j,C_{\rm outer},f^0\) are odd
and \(D,V_j\) are even. At q=2,m=8, the 57 query coefficient functions
split into 33 odd and 24 even functions. An odd-only Fourier dictionary
cannot represent the latter indiscriminately. This query-storage burden
prevents comparing the training-only 474-number total directly with the
earlier 729-number whole-circle evaluator.

## Conditional terminal comparison and limits

The proxy response coefficients displayed above are smooth in its finite
state on \(\tau>0\), and its state velocity factors into residual
components plus residual norm times smooth fields. At the handoff it
shares the full closure's frozen residual generator and frozen query
observer. Therefore the existing terminal proof can be applied separately
to the full model and proxy if each satisfies the stated speed,
coefficient-Lipschitz, contraction, small-tail and query-observable
hypotheses. The triangle inequality gives the claimed residual/query
quadratic and loss cubic bounds with the sum of their constants.

The final candidate correctly requires uniform boundedness of those
constants and a margin bounded away from zero to interpret the powers
as asymptotic orders along \(R\to0\). It does not claim a smaller error
constant, a better order, or certificates for the recorded trajectories.

The final observation about mixtures of independently fitted q1/q2
models is also correct: every affine mixture still matches the same
training labels, so exact training fit cannot determine its mixture
coefficient. The note's empirical reference to earlier nonmonotone
endpoint errors is outside this mathematical check; no experimental
evidence was inspected here.
