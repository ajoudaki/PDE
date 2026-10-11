# Internal check of the arbitrary-label saturation basin

2026-10-10. Reviewer: the positive_geometry_route agent in a reused research
context. This is a cross-check within the study, not an isolated promotion
review. Before this assignment the reviewer had independently considered the
same saturation-trapping mechanism, had read the selected book sections recorded
in POSITIVE_GEOMETRY_ROUTE.md, and had subsequently read the supervisor-supplied
GLOBAL_FAILURE_ALTERNATIVES.md and TANH_REPLICATION_CLASS.md. This exposure is
disclosed; no independence from the research program is claimed.

Frozen input: complete POSITIVE_ARBITRARY_LABELS.md, SHA-256
605af3050555b2a005e1683b3da5666cf3870e7a5c46ee7bad1c6eb59460199a.
The supplied hash was verified before review. No changes were made to that file.
No experiment or external source was used.

Verdict: **PASS for the stated deterministic conditional theorem and its
fixed-width positive-probability Gaussian consequence.** The proof does not
establish the preferred typical-Gaussian, arbitrary-label fitting target, and
it explicitly says so. No mathematical correction is required for the frozen
candidate.

## Exact model and normalization

The candidate uses precisely

\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad L=\|r\|^2/m,
\]

with unit input columns, two tanh hidden layers, zero initial readout, and
mobilities \((n,1,n)\). Differentiation gives its equation (1), including the
middle-layer factor \(2/(mn)\), first-layer factor \(2/m\), and readout
factor \(2/m\). Its kernel (2) has exactly the three factors
\(1/n,1/n^2,1/n\). Each block is a Gram matrix in the actual parameter
metric, so \(\mathcal K\succeq H^\top H/n\) and
\(\dot L=-4r^\top\mathcal K r/m^2\). No raw time rescaling or substituted
optimizer enters the proof.

The global-existence argument also closes independently of the event:
bounded loss gives bounded residuals; the displayed readout, middle-matrix,
and first-matrix speed bounds successively bound the parameters on every
finite time interval. Smooth local existence then extends the solution.

## Recomputed constants and trapping argument

Use the candidate's definitions
\(S=\operatorname{sign}(Z_0)\),
\(\lambda=\lambda_{\min}(S^\top S/n)>0\),
\(B=\|W_0\|_{\mathrm{op}}\), \(K=\|X\|_{\mathrm{op}}\), and
\(\beta=\operatorname{sech}^2(R/2)\).
Before the proposed first exit, every top preactivation has its initial
sign and magnitude greater than \(R/2\). The elementary inequality
\(1-\tanh x\le2e^{-2x}\) for \(x\ge0\) yields

\[
\|H-S\|_F\le2\sqrt{nm}\,e^{-R},\qquad
\max_{ia}(1-H_{ia}^2)\le\beta.
\]

The first condition in (4) therefore gives
\(\sigma_{\min}(H/\sqrt n)\ge\sqrt\lambda/2\).
This proves the top-feature gap from the initial event; it does not assume
the gap on the entire trajectory. Consequently,

\[
L(t)\le L(0)e^{-\lambda t/m},\qquad
\|r(t)\|\le Y e^{-\lambda t/(2m)},\qquad
\int_0^t\|r(s)\|\,ds\le \frac{2mY}{\lambda}.
\]

Writing \(E=(1-H^2)\odot(wr^\top)\), the needed norm bound is
\(\|E\|_F\le\beta\|w\|\|r\|\). The readout estimate gives total readout
length at most \(4\sqrt{nm}Y/\lambda\). Substitution into the other two
equations yields the following exact sufficient upper bounds:

| Quantity | Bound obtained by direct substitution |
|---|---|
| \(\int_0^t\|\dot W\|_F\) | \(\dfrac{2\beta}{\sqrt{nm}}\dfrac{4\sqrt{nm}Y}{\lambda}\dfrac{2mY}{\lambda}=\dfrac{16m\beta Y^2}{\lambda^2}\) |
| \(\int_0^t\|\dot A\|_F\) | \(\dfrac{2\beta(B+1)K}{m}\dfrac{4\sqrt{nm}Y}{\lambda}\dfrac{2mY}{\lambda}=\dfrac{16\sqrt{nm}(B+1)\beta Y^2K}{\lambda^2}\) |
| \(\|WU-Z_0\|_F\) | \(\dfrac{16\sqrt{nm}\beta Y^2}{\lambda^2}[m+(B+1)^2K^2]\) |

For the last row, the expansion
\[
WU-W_0U_0=(W-W_0)U_0+W(U-U_0)
\]
uses \(\|U_0\|_{\mathrm{op}}\le\sqrt{nm}\),
\(\|W\|_{\mathrm{op}}\le B+1\), and
\(\|U-U_0\|_F\le K\|A-A_0\|_F\).
These reproduce all constants in (4), (6), and (10).

The second and third conditions in (4) are strict bounds below the two
exit thresholds. Their margins are fixed, independent of the hypothetical
exit time. Global existence and continuity therefore rule out any finite
exit. The residual estimate and all three finite velocity integrals then
hold globally, giving finite parameter limits and interpolation. The case
\(Y=0\) is correctly included: zero readout and zero labels make every
velocity vanish.

## Nonemptiness and Gaussian scope

The hyperplane avoidance argument is valid for pairwise distinct,
nonantipodal unit inputs. On the selected line, the projected magnitudes
are nonzero and distinct. The large-positive-time tanh expansion isolates
the smallest magnitude coefficient, and finite induction proves linear
independence. Selecting \(m\) evaluations therefore gives a first-feature
matrix \(U_*\) with column rank \(m\), for every \(n\ge m\).

The displayed sign matrix construction also works for every \(m\ge1\):
subtracting its first row from rows \(2,\ldots,m\) gives the independent
vectors \(-2e_2^\top,\ldots,-2e_m^\top\), and the first row supplies the
first coordinate. Extra rows preserve column rank. Its Gram therefore
has \(\lambda>0\).

With \(U_*^+=(U_*^\top U_*)^{-1}U_*^\top\), the constructed center
\(W_*(R)=2RSU_*^+\) satisfies \(W_*(R)U_*=2RS\). Its norm is linear in
\(R\), whereas \(\beta\le4e^{-R}\). Thus every condition in (4) can be
made strict for any fixed \(X,n,m,Y\). The center's margin \(2R\)
leaves room for a common open neighborhood with margin greater than
\(R\), unchanged sign matrix, and all three strict sufficient
inequalities. The same neighborhood works simultaneously for the
whole label ball \(\|y\|\le Y\).

The canonical hidden-weight law has a strictly positive density on every
finite-dimensional open neighborhood. Thus the open event has positive
probability at each fixed width with the actual variances \(1\) and \(1/n\)
and exact zero readout. This support argument is sufficient for that
claim. It supplies no uniform-in-width probability bound or success
probability approaching one.

The constructed center can have low-rank raw matrices, but its open
neighborhood is the actual theorem event. The proof does not claim that
this center is a typical Gaussian realization or that its construction
answers the preferred initialization problem. Its small hidden-motion
mechanism and dependence on the label radius are both stated explicitly.

## Claim boundary

The checked theorem covers arbitrary mixed signs and arbitrary finite
label radius through an event whose required saturation is selected for
that radius. It retains training of both hidden layers, but proves a
stable-feature regime; it supplies no lower bound on substantial hidden
motion or persistent nonlinear feature learning. It is stronger than a
merely assumed all-time feature gap because the gap is closed by an
explicit initial-state bootstrap. It is substantially weaker than a
typical-Gaussian theorem because the probability of that favorable event
is not controlled as width grows.

Those are substantive scope limits, not flaws in the candidate's stated
theorem. The remaining main obligation is an all-time argument for the
canonical Gaussian bulk at arbitrary fixed label amplitude.
