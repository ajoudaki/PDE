# Independent check of the trained-probe readout lower bound

2026-10-11. Narrow isolated review of the complete
`CIRCLE_PROBE_READOUT.md`, using the authorized transport and canonical
fitting/probe inputs. Previously read rigorous-proof and canonical-notation
instructions, including the neural-network reference, were retained. No
other second-round note, experiment, candidate edit, manuscript edit, or Git
operation was used. This report checks only the proposed direct-probe
readout estimate.

**Verdict: accepted as a partial theorem.** On a cavity event whose
probability tends to one, the argument proves
\(\|a_\infty\|_{L^2(g)}\ge Y/(6H)\), under the original label cap
and original width normalizations. No substantive mathematical error was
found. This is a lower bound on an uncentered second moment, not on the
centered variance, compensated influence, or two-network endpoint gap.

## Normalization and the initialization event

The cavity has \(n-1\) retained top coordinates but retains denominator
\(n\). With \(b=w/\sqrt n\) and
\(A_{a,:}=h^{(L)}(v_a)^\top/\sqrt n\), both the prediction
\(Ab\) and the readout equation
\(\dot b=-(2/m)A^\top r\) are exact. With the deleted incoming row
written as \(U/\sqrt n\), its probe equations (16) also retain exactly
the canonical factors. There is no missing factor of \(n\) or
\(n-1\).

Write \(G_0=A_0A_0^\top\) and let \(C_0\) be the conditional
Gaussian Gram in (5). Both converge in probability to the same fixed
\(Q^{(L)}\succeq\gamma I\). If each is within \(\gamma/4\) of
that limit in operator norm, then each lies between
\((3/4)Q^{(L)}\) and \((5/4)Q^{(L)}\) in Loewner order. Hence

\[
\frac35G_0\preceq C_0\preceq\frac53G_0,
\]

which implies event (6). This argument requires no independence of the
two matrices. The deleted-row normalization leaves their common limit
unchanged. The initial sphere feature bound gives
\(\|A_0\|\le(3H/2)\sqrt m\), while the fitting event gives
\(G_0\succeq(\gamma/2)I\). These imply both bounds (8) for the
minimum-norm interpolant
\(b_*=A_0^\top G_0^{-1}y\), with \(B_*=\|b_*\|>0\).

## Lyapunov estimate and matrix inversion

The forward velocity estimate gives
\(\|A(t)-A_0\|\le\sqrt m F\alpha(t)S_t\), where
\(\alpha(t)=\int_0^t2\rho(s)\,ds\) and
\(S_t=\sup_{s\le t}\|b(s)\|\). The derivative of the distance to
\(b_*\) has the stated sign:

\[
\frac d{dt}\|b-b_*\|^2
=-\frac4m\|r\|^2
 +\frac4m r^\top(A-A_0)b_*
\le4F\rho\alpha S_tB_*.
\]

At a fixed terminal time \(T\), integration uses
\(\int_0^t4\rho(s)\alpha(s)\,ds=\alpha(t)^2\). Therefore
\(S_T\le B_*+\sqrt{B_*^2+F\alpha^2S_TB_*}\). If
\(S_T\ge B_*\), squaring after subtracting \(B_*\) yields
\(S_T\le(2+F\alpha^2)B_*\); the other case is immediate. This
proves (10), once \(F\alpha^2<1\) is checked. The estimate is relative
to the particular initialized interpolant, as required by the later proof.

Direct integration also gives the slightly sharper version of (12),

\[
\|b(t)-A_0^\top c(t)\|
\le\tfrac12F\alpha(t)^2S_t,
\qquad c(t)=-\frac2m\int_0^t r(s)\,ds.
\]

Using the lower singular value of \(A_0\), the relative perturbation
constant is exactly
\(\eta=\sqrt{2/\lambda}F\alpha S\le24F(Y/\lambda)^2\).
Thus \(G_\infty=A_\infty A_\infty^\top
\preceq(1+\eta)^2G_0\). Both Grams are positive definite on the
fitting event. Order reversal under inversion gives

\[
G_\infty^{-1}\succeq(1+\eta)^{-2}G_0^{-1},\qquad
\|b_\infty\|^2\ge y^\top G_\infty^{-1}y
\ge(1+\eta)^{-2}B_*^2.
\]

This proves (14) without a commutation assumption. Combining it with
(10) and (12) gives (15).

## Conditional Gaussian remainders and endpoint convergence

Conditional on the entire cavity path, the root \(g\) is still standard
Gaussian and the paths \(H_a(t)\) are deterministic. In particular,

\[
\|g^\top(H_a(t)-H_a(0))\|_{L^2(g)}
=\|H_a(t)-H_a(0)\|\le F\alpha S.
\]

The proof uses a supremum of these individual \(L^2\) norms, not an
unjustified exchange with the \(L^2\) norm of a supremum. For finite
\(T\), the already supplied probe/transport bounds ensure that
\(P_T\) and \(D_T\) are finite before the inequality involving
\(P_T\) is solved. No bootstrap from an undefined infinite quantity is
needed.

Minkowski's inequality in the incoming-row equation gives
\(D_T\le\alpha\beta BP_T\). In the readout equation, split the
argument change as

\[
U(t)^\top H_a(t)-g^\top H_a(0)
=(U(t)-g)^\top H_a(t)
 +g^\top(H_a(t)-H_a(0)).
\]

The Lipschitz activation bound then gives exactly (21), with
\(\varepsilon_1=\alpha^2\beta F\) and
\(\varepsilon_2=\alpha^2\beta^2B^2\). No dimension factor occurs.
Event (6) gives (18) even though \(c(t)\) depends on the cavity,
because the Gram comparison holds for every vector once that cavity is
fixed. Equations (12) and (18) bound the comparison readout by \(2S\).
Consequently
\(P_T\le(2+\varepsilon_1)S/(1-\varepsilon_2)\le3S\).

This uniform estimate also makes the passage to \(t=\infty\) valid.
Linear growth gives
\(\|\phi_L(U^\top H_a)\|_2\le
\beta(1+B+BD_\infty)\), where
\(D_\infty=\sup_{T<\infty}D_T<\infty\).
Thus \(\int_0^\infty\|\dot a(t)\|_2\,dt<\infty\).
The readout converges in \(L^2\), agrees with its known pointwise
endpoint, and satisfies remainder bound (23).

## Constants and final scope

The supplied fitting coefficient inequality and original cap imply
\(F\le\beta^{10L}/64\),
\(\alpha\le4\beta^{-30L}\), and \(B\le\beta^{2L}\).
The four powers and prefactors in (24) follow directly:

\[
\varepsilon\le\tfrac14\beta^{-50L},\quad
\eta\le\tfrac38\beta^{-50L},\quad
\varepsilon_1\le\tfrac14\beta^{-50L+1},\quad
\varepsilon_2\le16\beta^{-56L+2}.
\]

Their use is not circular: first control \(\varepsilon\), then the
actual readout maximum, then \(\eta\); the other two estimates use
only the fixed fitting constants and cap. For \(\beta\ge10\) and
\(L\ge2\), the coarse bounds in the note leave ample slack:

\[
\|a_\infty\|_2
\ge\left(\frac{77}{100\sqrt2}-\frac{12}{100}\right)B_*
>\frac14B_*\ge\frac{Y}{6H}.
\]

There is one harmless display artifact: equation (5) begins with
`\[+C_0{}_{ab}`. Removing the stray unary plus would improve the
presentation; it does not change the argument.

The proved result is a width-independent lower bound on
\(\mathbb E_g|a_\infty(g)|^2\), conditional on a high-probability
cavity event. A nonzero mean can contribute to this norm. The proof does
not give centered readout variance, quantitative survival after training
compensation, or collective fluctuations of actual networks. The candidate
states these limits accurately.
