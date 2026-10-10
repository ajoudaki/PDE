# Dense-history upper estimates for the tenth-power sufficiency question

Date: 2026-10-10. This bounded continuation asks whether the unchanged original Legendre method can attain the required all-time whole-sphere relative accuracy with \(q=n^{1/10+o(1)}\). Its scientific inputs are the current paper sources already read in this study, the scalar identities checked in CROSS_TAIL_IDENTITIES.md, and the scoped scalar calculation identified below. No method change, new experiment, or paper edit is made.

This note proves an improved **dense-history** upper estimate. It does not prove the desired approximation theorem for the closure. On the paper's fitting and source event, the dense histories in their own residual clock have, uniformly over all times and \(2\le q\le n^7\),

\[
\|(I-\Pi_q^A)h_D\|_{\rm hist}\le
 C_{\rm problem}[\log(en)]^Nq^{-5/2},
\qquad
\|(I-\Pi_q^A)b_D\|_{\rm hist}\le
 C_{\rm problem}[\log(en)]^Nq^{-1}\sqrt{\log(eq)}.          \tag{1}
\]

Here \(N\) is a fixed integer, \(A\) is any attained dense clock value, and the history norm includes neuron and sample RMS. Thus the corresponding matrix cross-tail is bounded by

\[
\left\|\frac2{mn}\sum_a\int_0^A
 (I-\Pi_q^A)b_{D,a}\,
 [(I-\Pi_q^A)h_{D,a}]^\top\,d\xi\right\|_F
\le C_{\rm problem}[\log(en)]^{2N}
 q^{-7/2}\sqrt{\log(eq)}.                                \tag{2}
\]

The terminal estimates used here do not require analyticity in the residual clock. The loss is explicit: the derivative of the normalized residual costs one inverse residual norm, and its first weighted Legendre energy is only logarithmically controlled after a terminal cutoff. A separate scalar example shows that physical-time analyticity, the correct unit prefix/onset orders, and even an exact relation \(h_\xi'=c\,b\) do not force a signed \(q^{-5}\) primitive. This is a limitation of those hypotheses, not a neural-output counterexample.

## Setup and physical derivative bounds

Use the dense network and its fixed admissible problem from the paper. Put
\[
\lambda=\gamma/m,\quad
\rho(t)=\|r(t)\|_2/\sqrt m,\quad
\xi(t)=1+\int_0^t\rho(s)\,ds,\quad
A_\infty=1+\int_0^\infty\rho(s)\,ds.
\]
For a fixed hidden interface, the histories are
\[
h_{D,a}(\xi(t))=h_a(t),\qquad
b_{D,a}(\xi(t))=\frac{r_a(t)}{\rho(t)}\delta_a(t).
\]
They have the original constant forward and zero backward prefix on \([0,1]\). All estimates below are for the actual dense histories and their own clock. Constants may depend on all fixed problem parameters but not on width, order, time, or clock endpoint.

The history Hilbert norm is
\[
\|g\|_{\rm rms}^2=\frac1{mn}\sum_a\|g_a\|_2^2,\qquad
\|g\|_{\rm hist}^2=\int_0^A\|g(\xi)\|_{\rm rms}^2\,d\xi.
\]
The argument also applies to each layer separately.

The fitting tube and exact gradient equations give
\[
\|\partial_t h_D\|_{\rm rms}\le C\rho,\qquad
\|\partial_t r\|_m\le C\rho,\qquad
-C\rho\le\dot\rho\le-\lambda\rho/2.                      \tag{3}
\]
For the first inequality, bound each parameter velocity by a constant times \(\rho\), then differentiate the finite forward recursion using bounded activation derivatives and the operator bounds. For the residual inequality, use the tangent Gram equation and its trace bound. The lower differential inequality for \(\rho\) follows from that same bounded Gram; the upper one is the fitting estimate. In particular
\[
\rho(t)\ge Ye^{-Ct},\qquad
A_\infty-\xi(t)\le2\rho(t)/\lambda.                      \tag{4}
\]
All norms in this argument are the normalized norms from the paper; no conversion from neuron RMS to a coordinate maximum is made.

Let \(\ell=\log(en)\), and let
\[
T_n=32\ell/\lambda.
\]
The source theorem gives dense forward fields and predictions holomorphic in a physical-time rectangle of radius \(r_n=c_{\rm problem}\ell^{-1/2}\) around \([0,T_n]\), with normalized Hilbert bounds independent of \(n\). Decreasing the radius by a fixed factor is allowed.

The following elementary estimate upgrades (3) to the needed higher physical derivatives:
\[
\|\partial_t^k h_D(t)\|_{\rm rms}
\le C_k\rho(t)\ell^{(5/2)(k-1)},\qquad k=1,2,3,\quad 0\le t\le T_n.       \tag{5}
\]
An analogous estimate applies to the first two residual derivatives, and implies
\[
|\dot\rho|\le C\rho,\qquad |\ddot\rho|\le C\rho\,\ell^{5/2}.              \tag{6}
\]

Here is a proof that retains the factor \(\rho(t)\) in (5). For a real \(t\in[0,T_n]\), apply polynomial approximation to \(g=\partial_t h_D\) on a forward interval \([t,t+r]\), where \(r\) is a fixed fraction of \(r_n\). Its parameter-two Bernstein ellipse and a small neighborhood lie inside the supplied source rectangle. Cauchy's integral formula bounds \(g\) there by \(C/r_n\). On the real interval, (3) and decreasing residual norm give \(\|g\|\le C\rho(t)\).

The degree-\(M\) Chebyshev truncation has error at most \(C r_n^{-1}2^{-M}\). Its derivative of order \(j\), including at the left endpoint, has error at most
\[
C_j r^{-j}r_n^{-1}(M+1)^{2j}2^{-M}.
\]
This follows by summing the Chebyshev coefficients and using
\(\|T_k^{(j)}\|_{[-1,1]}\le C_jk^{2j}\), obtained by repeated polynomial Markov inequalities. The polynomial itself has derivative bounded by
\[
C_jr^{-j}M^{2j}
 \big(\rho(t)+r_n^{-1}2^{-M}\big).
\]
By (4), \(\rho(t)\ge Ye^{-CT_n}\) on the entire source interval. Choose \(M=\lceil C_0\ell\rceil\), with the fixed-problem constant \(C_0\) large enough that \(r_n^{-1}2^{-M}\le\rho(t)\) there. Then \(r^{-j}M^{2j}=O(\ell^{5j/2})\). This proves (5), by taking \(j=k-1\). The argument works for Hilbert-valued functions by the same contour integral and norm bounds.

Apply the identical argument to \(g=\partial_t r\), whose real bound is supplied by (3) and whose holomorphy follows from the source theorem. Finally differentiate \(\rho^2=\|r\|_m^2\); the first two derivatives use \(\|r\|_m=\rho>0\), \(\|r'\|_m\le C\rho\), and \(\|r''\|_m\le C\rho\ell^{5/2}\). This proves (6). No clock-analyticity claim is involved.

## Clock derivative bounds and the precise terminal loss

Write \(\partial_\xi=\rho^{-1}\partial_t\). Direct differentiation gives
\[
\begin{aligned}
\partial_\xi h_D&=h_t/\rho,\\
\partial_\xi^2h_D&=h_{tt}/\rho^2-h_t\dot\rho/\rho^3,\\
\partial_\xi^3h_D&=h_{ttt}/\rho^3
 -3h_{tt}\dot\rho/\rho^4
 -h_t\ddot\rho/\rho^4
 +3h_t\dot\rho^{\,2}/\rho^5.
\end{aligned}                                                        \tag{7}
\]
Thus, with \(C_n=C_{\rm problem}\ell^N\) for a fixed integer \(N\), (3), (5), and (6) yield
\[
\|\partial_\xi h_D\|_{\rm rms}\le C,\qquad
\|\partial_\xi^2h_D\|_{\rm rms}\le C_n/\rho,\qquad
\|\partial_\xi^3h_D\|_{\rm rms}\le C_n/\rho^2.                         \tag{8}
\]
These last two bounds are established up to physical time \(T_n\).

For the normalized residual \(u=r/\rho\), exact differentiation of the bounded tangent-Gram equation gives \(\|u_t\|_m\le C\). The dense response-speed estimate in the Legendre proof, using the all-time dense carrier bound, gives
\(\|\delta_t\|_{\rm rms}\le C\rho(1+\sqrt\ell)\).
Combining this with the bounded response RMS and the fixed sample count gives
\[
\|b_D\|_{\rm rms}\le C,\qquad
\|\partial_t b_D\|_{\rm rms}\le C_n,\qquad
\|\partial_\xi b_D\|_{\rm rms}\le C_n/\rho.                           \tag{9}
\]
The backward estimate needs only one physical derivative.

Fix any endpoint \(A\le A_\infty\). At every \(\xi<A\), (4) implies
\(\rho\ge(\lambda/2)(A-\xi)\). Therefore, on the part covered by the source interval,
\[
\|\partial_\xi^2h_D\|_{\rm rms}\le \frac{C_n}{A-\xi},\qquad
\|\partial_\xi^3h_D\|_{\rm rms}\le \frac{C_n}{(A-\xi)^2},\qquad
\|\partial_\xi b_D\|_{\rm rms}\le \frac{C_n}{A-\xi}.                   \tag{10}
\]

This displays the weighted-energy loss. With \(w_A(\xi)=\xi(A-\xi)\),
\[
w_A^3\|\partial_\xi^3h_D\|_{\rm rms}^2
\le \frac{C_n^2}{A-\xi},\qquad
w_A\|\partial_\xi b_D\|_{\rm rms}^2
\le \frac{C_n^2}{A-\xi}.                                            \tag{11}
\]
The majorants have logarithmically divergent integrals at the terminal endpoint. The first derivative of the forward history remains bounded, which makes its cutoff error much smaller than the backward cutoff error.

## Weighted Legendre inequality and terminal cutoffs

For an integer \(k\ge1\) and a sufficiently regular Hilbert-valued \(g\), repeated integration by parts in Rodrigues' formula gives
\[
\sum_{j\ge q}\frac{(j+k)!}{(j-k)!}\|g_j\|^2
\le\int_0^A w_A(\xi)^k\|g^{(k)}(\xi)\|^2\,d\xi,\qquad q\ge k,         \tag{12}
\]
where \(g_j\) are the coefficients in the orthonormal shifted Legendre basis. In detail, the derivatives of that basis are orthogonal with weight \(w_A^k\), their squared weighted norms are \((j+k)!/(j-k)!\), and \(k\) integrations by parts identify the weighted derivative coefficient. Bessel's inequality then gives (12). The factors from the interval rescaling cancel exactly. In particular
\[
\|(I-\Pi_q^A)g\|_{\rm hist}
\le C_kq^{-k}\left(\int_0^Aw_A^k\|g^{(k)}\|^2\right)^{1/2}.          \tag{13}
\]

Take \(0<\delta\le1/8\). Choose a smooth cutoff equal to one on \([0,A-2\delta]\), zero on \([A-\delta,A]\), with \(j\)-th derivative bounded by \(C_j\delta^{-j}\). Replace a function near \(A\) by its value at \(A-2\delta\), using this cutoff to interpolate.

For \(b_D\), the cutoff changes the history by at most \(C\sqrt\delta\) in \(L^2\), because \(b_D\) is bounded. On the transition interval its derivative is \(O(C_n/\delta)\), by (10) and the bounded variation over that transition. Formula (11) on the retained interval and a direct transition estimate show that its first weighted derivative energy is at most \(C_n^2(1+\log(1/\delta))\). Projection contraction and (13) give
\[
\|(I-\Pi_q^A)b_D\|_{\rm hist}
\le C_n q^{-1}\sqrt{1+\log(1/\delta)}+C\sqrt\delta.                  \tag{14}
\]

For the forward history, first remove its globally constant value and its quadratic join jet:
\[
g(\xi)=h_D(\xi)-h_D(0)
 -\frac12h_D''(1+)(\xi-1)_+^2 .
\]
The first clock derivative of \(h_D\) vanishes at the join, because the initial readout is zero. Thus \(g,g',g''\) match across the prefix join, and no distributional delta occurs in \(g'''\). The bounds (10) apply to \(g'''\), while \(\|g'\|\le C_n\) globally and \(\|g''\|\le C_n[1+(A-\xi)^{-1}]\).

Apply the same terminal cutoff to \(g\). Its \(L^2\) change is at most \(C_n\delta^{3/2}\), because it is Lipschitz in the clock. On the transition interval its third derivative is at most \(C_n\delta^{-2}\). The third weighted energy is therefore at most \(C_n^2(1+\log(1/\delta))\). Formula (13) gives
\[
\|(I-\Pi_q^A)g\|_{\rm hist}
\le C_n q^{-3}\sqrt{1+\log(1/\delta)}
 +C_n\delta^{3/2}.                                                \tag{15}
\]
This argument also covers \(A-1<2\delta\): the cutoff can overlap the original prefix, where \(g=0\) and the matching derivatives ensure the same bounds.

The uniform truncated-power estimate checked in CROSS_TAIL_IDENTITIES.md gives
\[
\|(I-\Pi_q^A)(\xi-1)_+^2\|_{L^2([0,A])}\le Cq^{-5/2}.
\]
For completeness its unnormalized moments are \(O(j^{-7/2})\), uniformly in \(1\le A\le A_\infty\), by the Legendre derivative formula and its endpoint-region bound. Parseval multiplies their squares by \((2j+1)/A\); the resulting sum is \(O(q^{-5})\).

Set \(\delta=q^{-2}\), treating finitely many small orders by enlarging constants. Equations (14)–(15), together with the quadratic jet, prove (1).

## Why the estimate includes all physical times

The high physical derivatives above were used only up to \(T_n\). Fitting gives
\[
A_\infty-\xi(T_n)\le (2Y/\lambda)e^{-16\ell}=O_{\rm problem}(n^{-16}).
\]
For \(q\le n^7\), the chosen cutoff width \(\delta=q^{-2}\) exceeds this remaining clock length for sufficiently large width. If an endpoint \(A\) lies after \(\xi(T_n)\), every nonconstant part of its cutoff history lies below \(A-\delta\le\xi(T_n)\). Hence all derivatives used in the cutoff energy were already supplied by the finite source rectangle.

The cutoff error itself uses only the global boundedness of \(b_D\) and the global clock-Lipschitz bound for \(h_D\), both obtained from fitting. The fitted endpoint \(A=A_\infty\) is included by the same bounds and limits. Thus no unproved extension of physical-time analyticity to infinite time occurs.

## What the derivative relation alone cannot provide

A scoped scalar calculation is recorded in SCALAR_CLOCK_REGULARITY_LOSS.md. Its purpose is to test the precise hypothesis package behind a possible signed improvement, not to replace the neural model.

For fixed \(d>0\), \(0<\alpha<1/4\), put \(A_*=1+d\), and on \(1<\xi<A_*\) set
\[
\begin{aligned}
b(\xi)&=(A_*-\xi)^\alpha-d^\alpha,\\
h(\xi)&=(A_*-\xi)^{1+\alpha}-d^{1+\alpha}
 +(1+\alpha)d^\alpha(\xi-1).
\end{aligned}
\]
Both are zero on the unit prefix. The backward onset is linear, the forward onset is quadratic, and \(h'=-(1+\alpha)b\) on the whole interval in the weak derivative sense. With the physical clock \(\xi(t)=1+d(1-e^{-t})\), both active histories are entire functions of physical time, the residual activity is finite, \(h_t=O(e^{-t})\), and all fixed active-interval clock derivatives have the corresponding endpoint-weighted bounds.

The exact derivative identity gives
\[
\int_0^{A_*}(I-\Pi_q)b\,(I-\Pi_q)h
=-\frac{[(I-\Pi_q)h](A_*)^2-[(I-\Pi_q)h](0)^2}{2(1+\alpha)}.
\]
The scalar calculation proves that this is
\[
-c_{\alpha,d}\,q^{-4-4\alpha}(1+o(1)),\qquad c_{\alpha,d}>0.         \tag{16}
\]
The exponent is strictly below five. The histories have only their prescribed finite join regularity across \(\xi=1\); their analyticity assertion concerns the active physical-time branch. This is exactly the prefix issue under consideration.

Thus the stronger signed fifth-power estimate cannot be deduced from physical-time analyticity, the correct onset orders, endpoint-weighted clock derivatives, and a derivative relation between the histories alone. Actual neural dynamics may impose additional cancellations, especially in the observable after fitting. Equation (16) does not establish or exclude those cancellations.

## Remaining bridge to the requested sufficiency theorem

The matrix estimate (2) is for dense histories in their own clock. It is not a bound on the actual closure primitive at equal physical time. Its power is also too weak to supply the desired tenth-power order through the parameter comparison lemma in SHARPER_UPPER_ROUTE.md.

The remaining all-time task is therefore specific: control the actual observable effect of the terminal cross-tail, using structure beyond the hypotheses falsified by (16), and transfer that control between the two trajectories without dividing an uncontrolled error by a vanishing residual. The current calculation supplies a proved general upper estimate and an exact limitation of a proposed regularity argument. It leaves \(q=n^{1/10+o(1)}\) sufficiency for the unchanged method open.
