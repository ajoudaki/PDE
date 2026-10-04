# Internal check of the rotating-feature-span note

Checked source: `ROTATING_FEATURE_SPAN.md`, read in full.

SHA256: `a7c1f59027ce1f9f6545194ce03577978f68dc2d032b7437bc73899bd63cdac4`.

Scope: a bounded mathematical check of the supplied candidate against the
prompt-specified autonomous q=1 equations. No other route was read, no
candidate edits were made, and no experiments were run. This is an internal
check, not a promotion review or an independent discovery claim.

**Finding:** no mathematical error was found. All numbered equations and the
strict two-neuron example are valid under the assumptions stated in the note.
The early-time construction proves a nonzero query contribution on an open
set of actual initialized q=1 trajectories. It does not prove a nonzero
limiting contribution; the candidate explicitly preserves this distinction.

## Equation-by-equation verification

1. The readout equation (1) is exactly the stipulated closure, including the
   factors \(2/m\) and \(1/n\).

2. On a constant-rank interval a local independent-column basis gives a
   differentiable projector \(P\). Since \((I-P)\dot w=0\), product
   differentiation gives
   \(((I-P)w)'=-P'w\), proving (2). The visibility statement concerns current
   predictions only: \(G^T(I-P)w=0\). The note correctly excludes dynamic
   decoupling and arbitrary rank changes.

3. At a finite interpolating endpoint, \(y\in\operatorname{range}(G_*^T)\).
   Consequently
   \(G_*^TG_*(G_*^TG_*)^\dagger y=y\), and the stated parallel readout
   \(nG_*(G_*^TG_*)^\dagger y\) both interpolates and lies in
   \(\operatorname{range}(G_*)\). Its orthogonal complement gives the stated
   minimum-norm proof. Because
   \((G_*^TG_*/n)^\dagger=n(G_*^TG_*)^\dagger\), the normalization in
   equation (3) is correct, including for rank-deficient final features.

4. Integrating (1) from \(w(0)=0\) and applying \(I-P_*\) gives (4).
   The subtracted final feature is annihilated by \(I-P_*\). The assumption
   \(\int_0^\infty\rho<\infty\) suffices for absolute convergence because
   \(m^{-1}\sum_a|r_a|\le\rho\) and \(\|g_a\|\le\sqrt n\).
   The same algebra gives the claimed finite-time formula without a
   convergence assumption. This argument does not require constant rank
   along the whole trajectory.

5. The orthogonal projection is a contraction. Applying the triangle
   inequality to (4), then Cauchy–Schwarz over the samples, gives precisely

   \[
   \frac{\|(I-P_*)w_*\|}{\sqrt n}
   \le2\int_0^\infty\rho(s)
   \sqrt{\frac1m\sum_a\frac{\|g_a(s)-g_a(*)\|^2}{n}}\,ds,
   \]

   verifying equation (5) and its factor 2.

## Cubic term in (6)–(7)

The initialization makes \(A'_0=V'_0=K'_0=G'_0=0\). The loss is initially
one, so \(\rho\) is an analytic positive square root in a neighborhood of
zero. Together with \(\tau_0=1\), this makes the complete vector field
analytic there and justifies the Taylor remainders. Full column rank of
\(G_0\) persists locally and makes \(P\) analytic as well.

From \(w'=2b-2Cw\), \(w_0=0\), and \(b'_0=C'_0=0\),

\[
 w'_0=2b_0,\qquad
 w''_0=-4C_0b_0,\qquad
 w'''_0=2b''_0+8C_0^2b_0.
\]

Dividing by the Taylor factorials gives (6). Since \(P'_0=0\) and
\(Pb=b\), differentiation twice gives
\(P''_0b_0=(I-P_0)b''_0\). Hence

\[
\begin{aligned}
 (I-P(t))w(t)
 &=t^3\left[\frac13(I-P_0)b''_0-P''_0b_0\right]+O(t^4)\\
 &=-\frac23t^3(I-P_0)b''_0+O(t^4).
\end{aligned}
\]

The terms involving \(b_0,C_0b_0,C_0^2b_0\) have no other perpendicular
contribution at this order. Thus the sign, factor \(-2/3\), and cubic order
in (7) are all correct.

## Actual two-neuron trajectory and unseen query

For the final, explicitly chosen matrix
\(A_0=\left(\begin{smallmatrix}a_1&0\\a_2&1\end{smallmatrix}\right)\),
\(0<a_1<a_2\), training input \(\sqrt2(1,0)\), and \(W_0=I_2\), put
\(h_i=\tanh a_i\), \(g_i=\tanh h_i\), and
\(H=(h_1^2+h_2^2)/2\). The normalized input has norm one, so there is no
missing factor of \(d\) in the read-in derivative. At initialization,

\[
 w'_0=2g,\quad d'_0=2g\odot(1-g^2),\quad
 v''_0=4g\odot(1-g^2),\quad
 h''_0=4(1-h^2)^2\odot g\odot(1-g^2).
\]

With \(B=W_0+vk^T/2\), \(B''_0=v''_0h^T/2\) and therefore
\(z''_0=h''_0+Hv''_0\). Since \(z'_0=0\), differentiation of tanh gives

\[
 R_i:=\frac{g''_i(0)}{g_i(0)}
 =4(1-g_i^2)^2\bigl[(1-h_i^2)^2+H\bigr].
\]

This proves (8). At fixed common \(H\), both positive factors are strictly
decreasing functions of \(h_i\in(0,1)\); hence \(R_1>R_2\).
In particular, \(g''_0\) is not parallel to \(g_0\), and the coefficient
in (7) is nonzero on this actual initialized trajectory.

The unseen query \(\sqrt2(0,1)\) has initial feature
\(g^{\rm query}_0=(0,c)\), where \(c=\tanh(\tanh1)>0\).
The construction can be checked even more explicitly. Writing
\(U=(I-P_0)g''_0\),

\[
 U_2=\frac{g_1^2g_2(R_2-R_1)}{g_1^2+g_2^2}<0.
\]

Here \(b=g\), \(n=2\), and the query feature is smooth. Therefore its
claimed additional prediction is

\[
 \frac{g_t(x)^T(I-P_t)w(t)}2
 =\frac{c\,g_1^2g_2(R_1-R_2)}{3(g_1^2+g_2^2)}t^3+O(t^4)>0
\]

for every sufficiently small positive time. This verifies both nonvanishing
and the precise cubic order at the stated fixed query. It vanishes exactly
at the training example by orthogonal projection.

The coefficient depends continuously on the initialization near this point,
where the one-column feature matrix has rank one. Its strict sign therefore
persists on an open neighborhood. Both stipulated Gaussian initialization
laws have strictly positive densities everywhere in their finite-dimensional
matrix spaces, so the neighborhood has positive probability. This is the
claimed nonexceptional possibility statement; it supplies neither a
high-probability claim nor a theorem about a fitted final endpoint.

## Disposition

No correction is required for the mathematical claims in the checked source.
The final decomposition remains conditional on a finite interpolating
endpoint, while the explicit construction establishes a transient effect.
The candidate's discussion correctly leaves endpoint persistence and test
accuracy benefits unresolved.
