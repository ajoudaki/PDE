# Internal check of finite mixed moments and averaged sensitivity

2026-10-03. This is an **internal collaborator check**, not an isolated
promotion review. The complete checked source is
`FINITE_MIXED_MOMENT_ROUTE.md`. Its read-version SHA-256 was
`f00c65e465fd6b54b5c832b7d319d02e665a212695fe21ef71e862afd96534a5`;
its corrected and checked SHA-256 is
`882fc64d4a0f3e98e630fdf9609ce911b1df21eee31fc9ac058be6058afdd571`.
I reconstructed its finite-width variational, Schatten, Gaussian integration
by parts, and transport arguments using only the assigned source and current
manuscript definitions already authorized. The required mathematical skills
were applied. No experiment, other-study read, or Git operation was performed.
The coordinator authorized the narrow source correction disclosed below;
no other source change was made.

**Verdict.** The conditional averaged sensitivity bounds, including the
adaptive residual term and the small-label scale of the top response, check.
The column Stein identity and its weighted-trace algebra check. The global
and localized Gaussian transport arguments check for **nonnegative**
\(\lambda\). I explicitly added \(\lambda\ge0\) to both transport
statements; their former hypothesis \(\lambda\ell\le1/2\) alone did not
impose it. This was the one literal hypothesis omission found. No hidden
dimension factor was found in the proved conditional estimates. The finite
exponential carrier budget and the required localized network response bounds
remain open, as the source states.

## 1. Tail implication and finite scales

The residual activity measure is
\(d\mu=(2/m)\sum_a|r_a|dt\). Cauchy--Schwarz and its reverse comparison
between finite-dimensional one- and two-norms give
\[
 \mu([0,\infty))\le S,\qquad
 d\mu\le\kappa S e^{-\kappa t}dt,\qquad
 \rho dt\le\frac{\sqrt m}{2}d\mu.
\]
For \(K_i=\max_a|k_{a,i}|\) and
\(\mathcal M_\eta=\kappa\int e^{-\kappa t}n^{-1}
\sum_i e^{\eta K_i/S}dt\), the elementary exponential domination of
\((K_i/S)^2\mathbf1_{K_i/S>R}\), followed by the empirical square root,
gives the factor \(S e^{-\eta R/4}\). Cauchy--Schwarz in \(d\mu\)
supplies a further factor \(S\sqrt{\mathcal M_\eta}\). This verifies
equation (6), simultaneously in all real cutoffs after the stated RMS bound
for smaller cutoffs.

The readout coordinate bound is \(\|w\|_\infty\le S\). Using its
stronger intermediate bound \(\|w(t)\|_\infty\le\mu([0,t])\) in the
column update gives
\[
 \|W_i-W_{0,i}\|_2
 \le\frac1{\sqrt n}\int\mu([0,t])\,d\mu(t)
 \le\frac{S^2}{2\sqrt n}.
\]
Multiplying by \(\|\delta_a\|_2\le S\sqrt n\) proves the stated
\(S^3/2\) difference between the actual carrier and its initialized-column
pairing. No independence is used in either calculation.

Markov's inequality must be applied to
\(\mathbf1_{\mathcal G_n}\mathcal M_\eta\), as the source does. The
resulting probability excludes both the initialization failure and the large
budget event. The sufficient target remains a statement about actual finite
coordinates; none of these deductions proves that target.

## 2. Exact variational equation and Hessian structure

In Euclidean coordinates \(\Theta=(A,H,w)\), \(H=\sqrt nW\), the
scalar \(\mathcal F_a=nf_a\) has gradient giving the actual flow
\(\dot\Theta=-(2/m)\sum_a r_a\nabla\mathcal F_a\). Since
\(D r_a=n^{-1}D\mathcal F_a\), differentiation gives exactly
\[
 \dot J=-\frac2{mn}\sum_a
       \nabla\mathcal F_a\nabla\mathcal F_a^\top J
       -\frac2m\sum_a r_a\nabla^2\mathcal F_a J.
\]
This is equation (7). The first term is negative semidefinite and is precisely
the adaptive-residual contribution. Rewriting the second coefficient as
\(\mathcal B\,d\mu\) occurs after differentiating the flow; it does not
silently omit a derivative of \(\mu\).

Directly differentiating the two forward layers gives all five terms of
equation (8). In particular, the \(A,H\) pair has its required
\(n^{-1/2}\) factor, and the last term is exactly
\[
 \sum_i k_{a,i}g'_{a,i}
                (U_Av_a)_i(V_Av_a)_i.
\]
It is block diagonal in the \(A\) rows, with each block acting on a fixed
\(d\)-dimensional space. The other terms factor through vector spaces of
dimension \(n\): the readout pair has rank at most \(2n\), top
curvature at most \(n\), and the mixed \(A,H\) pair at most \(2n\).
Their operator norms are bounded because
\(\|\delta_a\|_2/\sqrt n\le S\), \(\|w\|_\infty\le S\), and the
linear preactivation variation map has bounded norm. Thus the source's rank
and operator estimates are valid even though the total parameter dimension
is \(nd+n^2+n\).

For the normalized Schatten norm, these observations give
\[
 \|\mathcal B(t)\|_{p,n}
 \le C\left[1+\left(n^{-1}\sum_iK_i(t)^p\right)^{1/p}\right].
\]
The rank contribution is \((Cn/n)^{1/p}\), and the local-block contribution
contains \(d^{1/p}\); both are bounded uniformly for \(p\ge2\) at fixed
data dimension. There is no extra factor from the ambient \(n^2\) block.

## 3. Schatten/Duhamel estimate

The normalized Hölder inequality used in the source is exactly the ordinary
finite-matrix Schatten Hölder inequality with cancelling normalizations:
\[
 n^{-1/2}\|B_1\cdots B_j\|_{\rm HS}
 \le n^{-1/2}\prod_{r=1}^j\|B_r\|_{2j}
 =\prod_{r=1}^j\|B_r\|_{2j,n}.
\]
This does not require the ambient dimension to equal \(n\). Intermediate
operator-norm contractions can be inserted without changing the bound.

For integer \(p\ge2\), the carrier part of the integrated norm obeys
\[
\begin{aligned}
 \int\left(n^{-1}\sum_iK_i^p\right)^{1/p}d\mu
 &\le S^{1-1/p}
       \left[\int n^{-1}\sum_iK_i^p\,d\mu\right]^{1/p}\\
 &\le\frac{S^2}{\eta}(p!)^{1/p}\mathcal M_\eta^{1/p}
 \le\frac{S^2p}{\eta}\mathcal M_\eta^{1/p}.
\end{aligned}
\]
This verifies equation (10), including its second power of \(S\).

The propagator \(U_0\) of the negative-Gram part is contractive by the
Euclidean energy identity. Each finite-time Duhamel term has a contraction
between consecutive \(\mathcal B\) factors. Applying Hölder at exponent
\(2j\) to its \(j\) factors leaves a symmetric nonnegative scalar
integrand, whose ordered-time integral is at most the full product integral
divided by \(j!\). Finite-time convergence of the series follows from
finite-dimensional continuity of the reference coefficients.

After inserting (10), the bounded part sums to \(CS\), since \(S\le1\).
The carrier part contains
\(\mathcal M_\eta^{j/(2j)}=\sqrt{\mathcal M_\eta}\), and the factorial
bound gives a geometric series in \(CS^2/\eta\). Under its displayed
smallness condition this proves equation (11), uniformly over finite terminal
times and hence on all physical time. The identity contribution is kept
inside \(U_0\), rather than incorrectly estimating its normalized
Hilbert--Schmidt norm in the full parameter dimension.

## 4. Small top-response sensitivity and the negative Gram

The source's separate argument for equation (12) is necessary and valid.
With \(L=(L_s,L_w)\), the gradient formulas give
\(\|L_s\|\le CS\), \(\|L_w\|\le C\), and the readout-feature gap
gives \(L_w^\top L_w\succeq cI\). The actual feature-speed estimate
implies \(\int\|\dot L_w\|dt\le CS^2\).

For \(q(t)=U_0(t,0)P_Hv\), its initial readout component is zero and
\(\|q(t)\|\le\|v\|\). Let \(P(t)\) be the complement projection of
\(\operatorname{range}L_w(t)\). Differentiating the formula for that
projection, using the fixed Gram gap, gives
\(\|\dot P\|\le C\|\dot L_w\|\). Since
\(\dot q_w\in\operatorname{range}L_w\),
\[
 (Pq_w)'=\dot Pq_w,\qquad \|Pq_w\|\le CS^2\|v\|.
\]
The vector \(p=L_w^\top q_w\) starts at zero and satisfies the source's
damped equation. Its forcing is bounded by
\((\|\dot L_w\|+CS)\|v\|\). The convolution with the exponentially
damped propagator bounds the constant term by \(CS\|v\|\), and its
integrable derivative term by \(CS^2\|v\|\). Therefore
\(\|p\|\le CS\|v\|\), and the range/complement decomposition gives
\(\|q_w\|\le CS\|v\|\).

The derivative of the top response is
\[
 B_a[U]=\gamma_a\odot U_w+
         (w\odot\gamma_a')\odot Dz_a^{(2)}[U].
\]
Its first term is \(O(S)\) on \(U_0P_H\) by the preceding argument;
its second term has \(\|w\|_\infty\le S\). Thus
\(\|B_aU_0P_H\|_{\rm op}\le CS\). Its output dimension is \(n\),
so its Hilbert--Schmidt norm is at most \(CS\sqrt n\). The remaining
piece \(B_a(J-U_0)P_H\) follows directly from (11), proving (12).
No uniform bound on \(\|J\|_{\rm op}\) or carrier maximum has been
assumed.

## 5. Stein identity and the unresolved mixed terms

For one initialized Gaussian column \(g_i\), write
\(X=(g_i^\top\delta_a)/(S\sqrt n)\) and
\(C=D_{g_i}\delta_a=B_aJI_i\). Then
\[
 \nabla_{g_i}X=(\delta_a+C^\top g_i)/(S\sqrt n).
\]
Applying coordinate Gaussian integration by parts to
\(\chi\delta_{a,j}F(X)\), and summing over \(j\), gives exactly the
trace, directional, and localization terms in equation (15). The directional
term is \(g_i^\top C\delta_a\), not its negative or a different
transpose. Smooth compact localization suffices for this finite-time
calculation. The dense trajectory and its derivative are well defined at
each finite time under arbitrary finite initialization: in these coordinates
\(\dot\Theta=-n\nabla\mathcal L\), so loss dissipation bounds
\(\int_0^T\|\dot\Theta\|^2dt\le n\mathcal L(0)\), excluding a
finite-time escape of a smooth finite-dimensional trajectory.

The aggregate identity
\(\sum_i\|C_{a,i}\|_{\rm HS}^2=\|B_aJP_H\|_{\rm HS}^2\) is valid.
For the weighted trace, the injection
\(\mathcal I_wv=vw^\top\) has
\(\mathcal I_w^\top\mathcal I_w=\|w\|_2^2I\); its nonzero singular
values are all \(\|w\|_2\). This verifies equation (16). Exponential
weights \(w_i=e^{\lambda X_i}\) therefore introduce the empirical
\(2\lambda\) moment in a direct black-box norm bound. The source correctly
does not turn this observation into a general impossibility claim, nor turn
its unweighted sensitivity estimate into a closed tilted estimate.

Equations (17)--(18) also reconstruct correctly. Differentiating the residual
gives
\(\Delta r_b=n^{-1}(\nu^\top h_b^{(2)}+\delta_b^\top\zeta_b)\),
which supplies the displayed \(-2/(mn)\) driver variation. The forward
and reverse initialized-matrix sources must both be retained in a column
perturbation. The source's warnings concerning adaptive cavity drivers and
conditioning on a full-trajectory stop are justified.

## 6. Transport lemmas and the corrected parameter restriction

For \(\lambda\ge0\) and \(\lambda\ell\le1/2\), the global map
\(T(g)=g-\lambda v(g)\) is a \(C^1\) bijection by the contraction
argument given. Its Jacobian determinant is positive: the matrices
\(I-t\lambda Dv\) are nonsingular for \(0\le t\le1\). For a real,
possibly nonsymmetric matrix \(M=Dv\),
\[
 |\operatorname{tr}M^j|\le\|M\|_{\rm HS}^2
                              \|M\|_{\rm op}^{j-2},\qquad j\ge2.
\]
It follows from the Frobenius Cauchy--Schwarz inequality and
\(\|M^{j-1}\|_{\rm HS}\le\|M\|_{\rm op}^{j-2}\|M\|_{\rm HS}\).
Summing the logarithm series uses
\(\sum_{j\ge2}x^{j-2}/j\le1\) for \(0\le x\le1/2\).
Thus the determinant lower bound, including its dimension-free
\(\lambda^2H^2\) term, is correct. Changing Gaussian variables gives
equation (19) with exactly the stated \(1/2\) contribution from
\(\|v\|\le1\).

For the localized version, two points \(x,y\) of the good domain with
\(T(x)=T(y)\) satisfy \(\|x-y\|\le2\lambda\). Their joining segment
lies in the open \(2\lambda\)-neighborhood; the derivative bound there
then gives \(\|x-y\|\le\lambda\ell\|x-y\|\), forcing equality of
the points. Hence the change-of-variables formula on the good domain uses
the Gaussian mass of its image, which is at most one. The determinant bound
is needed only on the domain. This proves equation (20) without a global
extension, provided \(v\) is \(C^1\) on the indicated neighborhood, as
inherited from the lemma's setup. The case \(\lambda=0\) is trivial.

The read version omitted the sign restriction on \(\lambda\):
\(\lambda\ell\le1/2\) permits every negative \(\lambda\). For a
literal counterexample to that former unrestricted statement, take dimension one,
\(v\equiv1\), \(\ell=H=0\), and the valid divergence upper bound
\(D=1\). At \(\lambda=-1\), the left side of (19) is
\(e^{1/2}\), but its displayed right side is \(e^{-1/2}\).
The applied correction requires \(\lambda\ge0\), which is
also consistent with its neighborhood radius. An alternative would use
\(|\lambda|\ell\le1/2\), \(|\lambda|D\), and neighborhood radius
\(2|\lambda|\). Applying the positive-parameter result separately to
\(v\) and \(-v\) already supplies both carrier signs.

For the intended network field \(v=\delta_a/(S\sqrt n)\), bounded norm
holds on the fitting domain. The source does **not** establish its divergence
bound or the necessary derivative bounds on all enlarged conditional domains.
Its sensitivity estimate controls an aggregate Hilbert--Schmidt norm; a
single-column trace bound can still cost a factor \(\sqrt n\). A
trajectory-budget event is also not automatically preserved under every
fixed-radius column perturbation. These remain substantive unproved network
inputs, correctly identified by the source.

## 7. Claim scope retained by this check

With the explicit nonnegative transport parameter now added, the source's proved
statements are valid conditional finite-dimensional estimates. This check
does not establish any of the following:

- the actual finite exponential carrier budget;
- a same-parameter weighted trace or directional Stein estimate;
- validity of the transport hypotheses on the enlarged network domains;
- a causal decreasing-parameter estimate that closes the exponential hierarchy;
- a controlled adaptive cavity reinsertion remainder;
- the desired strict root-width comparison with a sublinear memory order.

The averaged sensitivity reduction is mathematically useful, but remains a
one-way implication from the open empirical budget. Its conclusion must not
be substituted for that budget or for the missing weighted response bounds.
