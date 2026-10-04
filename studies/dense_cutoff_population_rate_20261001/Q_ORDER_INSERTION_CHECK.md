# Internal reconstruction of the external insertion lemma

2026-10-03. Internal collaborator check, **not an isolated promotion
review**. The assigned source was read completely through Section 5,
equations (1)--(20); Section 6 was read only to identify the intended use
and is not proved by this check. The checked version of
Q_ORDER_POSITIVE_ROUTE.md has SHA-256

cf1ce29a34123fc52fe0967ada275d41960cfe74e475370cda21fe5b862bcc16.

During this reconstruction the author expanded Section 3 and repaired
formatting. I reread Sections 1--5 completely in the resulting version,
SHA-256
145b1b7d94f636f81c2c28bed2a9bf1a9f7bdda68be4f8c06c0a90aa047b7de6.
Its added blockwise derivation agrees with the reconstruction below; the
verdict applies to that version as well.

Current-version confirmation: I reread the complete local core, Sections
1--5, at full-file SHA-256
d6af07cbced5abc8222466ae67b76cda6d079a21301d631d5bd044eafc4e16af.
The author has applied both minor clarifications: Section 1 states the
pathwise interpretation for arbitrary measurable adaptive forcing, and
Section 4 invokes the bounded first three derivatives of tanh.
The local equations and proof are otherwise unchanged from the checked
expanded version. The SHA-256 of the exact text beginning at the Section 1
heading and ending just before the Section 6 heading is
056300cd33ec5a36ead97381b385845fc6fe93177be63c42827b1b8828a760ba.
This confirmation covers only the insertion lemma; the added outer
probability argument has a separate checker.

Final saved-version anchor: the author subsequently removed candidate
labels, added the reference to this completed check, and made an outer
feature-matrix definition explicit. The local equations and estimates
(1)--(20) are unchanged. The verified final full-file SHA-256 is
cb38dfcbd752e50f0cde1ae60a8d16f7db5bcd2fafbd69dc65546a2efeb3e590;
the final Sections 1--5 text SHA-256, using the same heading boundaries, is
4e7df4a86b9d21ee29ae2eee690dd39a798a92ad6c3794dbbcce49d6720cfc3e.
The insertion-lemma verdict applies to this final version. The status of
the separate probability proof is established by its own check, not by
expanding the scope of this report.

Final formatting correction: the coordinator inserted the missing display
close \(\backslash]\) immediately after equation (14)'s split environment.
No mathematical statement or proof changed. The resulting exact final
full-file SHA-256 is
9026935501ce94886d9eee81c6d318d3f45ac2f526597be5de71b0989a959f27.
The same insertion-lemma verdict applies; the preceding checked hashes are
retained for provenance.

The complete required dependency FINITE_MIXED_MOMENT_ROUTE.md has SHA-256
882fc64d4a0f3e98e630fdf9609ce911b1df21eee31fc9ac058be6058afdd571;
its complete check was also read. Current manuscript definitions, fitting
bounds, and exact dense/closure equations were already available within the
assigned scope. The canonical-notation skill, its neural reference, rigorous
proof skill, and conjecture audit were applied. No experiments, Git
operations, source edits, or other-study inputs were used.

**Verdict.** The local perturbation argument checks under its displayed
cavity stop assumptions. In particular, the nonlinear estimate (14) has
the stated width factors, including the adaptive-residual terms, and the
subinterval Schatten estimate (18) follows from the original deterministic
time-weighted budget. The conditional Gaussian event and the control net
have sufficient exponent margins. This does **not** establish the
empirical-moment closure proposed in Section 6 or an unconditional
root-width theorem.

Two minor clarifications were identified and have now been applied. Terminal-time
regularity of the response maps uses the bounded third derivative of tanh,
in addition to the first two derivatives mentioned in the original source. Also an
arbitrary adaptive remainder \(\zeta\) should be interpreted as an estimate
along an existing solution with measurable forcing; a bound on its magnitude
alone does not give well-posedness for every arbitrary state-dependent rule.
Both requirements hold for the intended actual-network application.

## 1. Exact coordinates and adaptive linearization

There are \(N=n-r\) retained first-layer neurons and \(n\) second-layer
neurons, with fixed deletion count \(r\). The source uses
\(\Theta=(A,H,w)\), \(W=H/\sqrt n\), and
\[
 h_a=\tanh(Av_a),\quad z_a=Wh_a+e_a,\quad
 \mathcal F_a=w^\top\tanh z_a,\quad f_a=\mathcal F_a/n.
\]
The Euclidean gradient blocks are exactly
\[
 G_a:=\nabla_\Theta\mathcal F_a
 =\left((g_{1,a}\odot k_a)v_a^\top,\ 
        \delta_a h_a^\top/\sqrt n,\ \tanh z_a\right),
\]
where
\(g_{1,a}=\operatorname{sech}^2(Av_a)\),
\(\delta_a=w\odot\operatorname{sech}^2z_a\), and
\(k_a=W^\top\delta_a\).
Thus the retained flow is
\(\dot\Theta=-(2/m)\sum_a r_aG_a\), with no altered mobility.

Since \(D_\Theta r_a=G_a^\top/n\), its exact derivative is
\[
 D_\Theta F
 =-\frac2{mn}\sum_aG_aG_a^\top
   -\frac2m\sum_a r_aD_\Theta G_a .
\]
The first term is the negative Gram. The only unbounded residual-Hessian
block is the retained first-layer diagonal block
\(k_{a,i}\tanh''((Av_a)_i)v_av_a^\top\).
All other blocks have operator norm \(C\) and rank \(Cn\) on the cavity
tube. The rectangular hidden matrix changes neither the normalization
nor the rank estimate.

The propagator of the negative Gram is contractive. Duhamel's formula or
the energy inequality therefore gives
\[
 \|J(t,s)\|_{\rm op}
 \le \exp\!\left(C(1+M_n)\int_s^t\rho^0(u)\,du\right)
 \le \exp\{CS(1+M_n)\}.
\]
For \(M_n=A_0S\log n\), sufficiently small fixed \(S\) makes this at
most \(n^{1/400}\) for large width, with a strict exponent margin absorbing
fixed prefactors. The horizon length does not enter this exponent.

External differentiation at fixed retained parameters gives
\(D_e\mathcal F_a=\delta_a^\top\) and
\(D_eG_a=B_a^\top\), where \(B_a=D_\Theta\delta_a\).
Consequently the two external forcing operators are exactly
\[
 P_a=-\frac2{mn}G_a\delta_a^\top,\qquad
 Q_a=-\frac2m r_aB_a^\top.
\]
The first has rank one and norm \(CS\), since
\(\|G_a\|\le C\sqrt n\) and \(\|\delta_a\|\le S\sqrt n\).
The second has norm \(C|r_a|\), since \(\|B_a\|\le C\).
Keeping both terms is necessary. Equation (13) is therefore the correct
linear response for the actual adaptive cavity.

## 2. Reconstruction of the nonlinear estimate

All quantities in this section are evaluated at one time on the cavity
stop. Suppress the sample index when it is unambiguous. Let \(V\) be the
linear perturbation, \(U\) the additional parameter perturbation,
\(u=\|U\|\le n^{-1/10}\), and let \(e\) be the linear external input.
Use the source's exponents
\[
 a=1/100,\qquad b=1/5.
\]
Define two scalar bounds, only for this calculation:
\[
 R=n^a+u,\qquad E=n^{a-b}+n^{-b}u+u^2 .
\]
All constants may include fixed data and the fixed number of inserted
columns. The hypotheses give
\[
 \|V\|+\max_a\|e_a\|_2\le Cn^a
\]
and coordinate bounds \(Cn^{-b}\) for every linear first-layer,
readout, preactivation, and retained-carrier variation.

Write \(\alpha=V_Av_a\), \(\beta=U_Av_a\), and
\(\gamma=\alpha+\beta\). Then
\[
 \|\gamma^2\|_2
 \le \|\alpha\|_\infty\|\alpha\|_2
       +2\|\alpha\|_\infty\|\beta\|_2+\|\beta\|_2^2
 \le CE.
 \tag{A1}
\]
The first-layer activation remainder
\[
 R_h=\tanh(A^0v_a+\gamma)-h_a^0-g_{1,a}^0\odot\gamma
\]
therefore has norm at most \(CE\).

Let \(z_V\) be the full linear preactivation variation, including \(e_a\),
and let
\[
 z_U=W^0(g_{1,a}^0\odot\beta)+U_Hh_a^0/\sqrt n .
\]
Then \(\|z_U\|\le Cu\), while \(\|z_V\|_\infty\le Cn^{-b}\).
The exact preactivation remainder is
\[
 R_z=W^0R_h+
       \frac{V_H+U_H}{\sqrt n}
                \{\tanh(A^0v_a+\gamma)-h_a^0\}.
\]
Consequently
\[
 \|R_z\|_2\le C(E+n^{-1/2}R^2).                       \tag{A2}
\]
This verifies the crucial matrix normalization. The external source is
already present in \(z_V\); it is not differentiated through again.

For the top response, expand
\[
 (w^0+V_w+U_w)\odot
     \operatorname{sech}^2(z_a^0+z_V+z_U+R_z).
\]
The terms quadratic in \(z_V+z_U\) have norm \(CE\), by the same
argument as (A1). Products of readout and preactivation changes use
both linear coordinate bounds: for example
\[
 \|V_w\odot z_V\|_2\le Cn^{a-b},\qquad
 \|V_w\odot z_U\|_2+\|U_w\odot z_V\|_2\le Cn^{-b}u,
 \quad \|U_w\odot z_U\|_2\le Cu^2.
\]
Terms containing \(R_z\) are bounded by (A2), since
\(\|w^0\|_\infty\le S\) and
\(\|V_w+U_w\|_\infty\le Cn^{-b}+u\le C\).
Hence, after subtracting the complete linear top response,
\[
 \|R_\delta\|_2\le C(E+n^{-1/2}R^2).                  \tag{A3}
\]

The exact carrier expansion is
\[
 k=k^0+k_V+k_U+R_k,\qquad
 k_U=(U_H/\sqrt n)^\top\delta^0+(W^0)^\top\delta_U,
\]
where \(\delta_U=B_aU\). Its linear map has norm \(C\), so
\(\|k_U\|\le Cu\). The remaining terms are
\((W^0)^\top R_\delta\) and
\((V_H+U_H)^\top(\delta-\delta^0)/\sqrt n\).
Using (A3), \(R\le Cn^{1/100}\), and \(n^{-1/2}R=o(1)\), gives
\[
 \|R_k\|_2\le C(E+n^{-1/2}R^2).                       \tag{A4}
\]
No coordinate bound on the unknown full carrier perturbation was assumed.

For the first gradient block, the remainder splits into
\[
 [g_1(A^0v_a+\gamma)-g_1^0-(g_1^0)'\odot\gamma]\odot k^0,
\quad
 [g_1(A^0v_a+\gamma)-g_1^0]\odot(k_V+k_U),
\quad
 g_1(A^0v_a+\gamma)\odot R_k .
\]
Their norms are at most \(CM_nE\), \(CE\), and the bound (A4).
The middle estimate uses
\(\|\alpha\odot k_V\|\le Cn^{a-b}\),
\(\|\beta\odot k_V\|+\|\alpha\odot k_U\|\le Cn^{-b}u\),
and \(\|\beta\odot k_U\|\le Cu^2\).
It would fail at the desired exponent if both linear coordinate bounds
were discarded.

The middle gradient's exact outer product gives remainder
\[
 \frac{R_\delta(h_a^0)^\top+
               \delta_a^0R_h^\top+
               (\delta_a-\delta_a^0)(h_a-h_a^0)^\top}{\sqrt n}.
\]
Here the first term uses \(\|h_a^0\|\le\sqrt n\), the second uses
\(\|\delta_a^0\|\le S\sqrt n\), and the last retains \(1/\sqrt n\).
The readout gradient is the top activation, whose Taylor remainder is
controlled by (A2). Altogether the gradient remainder satisfies
\[
 \|R_{G_a}\|
 \le C(1+M_n)E+C n^{-1/2}R^2.                        \tag{A5}
\]

For completeness, the scalar prediction remainder obeys
\[
 |R_{r_a}|\le C(1+M_n)R^2/n,\qquad
 |\Delta r_a|\le CR/\sqrt n,\qquad
 \|\Delta G_a\|\le C(1+M_n)R.                        \tag{A6}
\]
One can verify the first estimate by the scalar Hessian along the straight
segment in \((\Theta,e)\). The preceding expansions apply at every
fractional segment point and give
\[
 \|k-k^0\|_\infty
 \le Cn^{-b}+Cu+C(E+n^{-1/2}R^2)=o(1).
\]
Thus its first-layer Hessian multiplier stays bounded by \(C(1+M_n)\).
All other mixed blocks have bounded operator norm, including the external
input blocks; the prediction has the prefactor \(1/n\). The reference and
segment gradient norms are \(C\sqrt n\), which proves the second
estimate. This also shows why the scalar remainder does not acquire a
spurious \(\sqrt n\) multiplier.

Finally the exact vector-field remainder is
\[
 -\frac2m\sum_a
    \{r_a^0R_{G_a}+R_{r_a}G_a^0+\Delta r_a\,\Delta G_a\}.
 \tag{A7}
\]
The last two terms are the residual-adaptation terms. From
\(\|G_a^0\|\le C\sqrt n\), (A5)--(A6), and the bounded residual tube,
(A7) yields
\[
 \|R_F\|
 \le C(1+M_n)
 \left[\rho^0\{n^{a-b}+n^{-b}u+u^2\}
       +n^{-1/2}\{n^{2a}+n^au+u^2\}\right].
 \tag{A8}
\]
This is precisely source equation (14), with harmless numerical constants
absorbing the cross term in \(R^2\).

## 3. Growing horizon and the small learned-column forcing

Variation of constants multiplies the integrated source (A8) by at most
\(n^{1/400}\). Its \(\rho^0\)-weighted part integrates with
\(\int\rho^0\le CS\); its unweighted part integrates over
\(T_n=c_T\log n\). With \(u\le n^{-1/10}\), the four largest powers
are
\[
 n^{-19/100},\quad n^{-3/10},\quad n^{-1/5},\quad n^{-48/100}.
\]
The factor \(C(1+M_n)(1+T_n)n^{1/400}\) preserves a strict margin
below \(n^{-1/10}\). Thus the proposed nonlinear bootstrap closes.

The external derivative \(D_eF\) stays bounded by \(C\) on this
near-reference region. Indeed its adaptive rank-one part has norm bounded
by \(n^{-1}(C\sqrt n)(C\sqrt n)\), and its residual part uses the
bounded top-response derivative \(B_a\). A measurable forcing remainder
\(\sup\|\zeta\|\le C_rn^{-1/2}\) therefore contributes at most
\[
 C_r(1+T_n)n^{-1/2+1/400}.
\]
No derivative of \(\zeta\) and no independence from the omitted column
are needed for this pathwise comparison.

For the intended deleted columns this forcing has the stated magnitude.
The full learned omitted column obeys
\[
 \|\dot W_i\|_2
 \le \frac{C}{n}\sum_a|r_a|\|\delta_a\|_2
 \le C S\rho/\sqrt n.
\]
Finite activity bounds its accumulated increment by \(CS^2/\sqrt n\).
Multiplying by bounded first-layer activations and summing fixed \(r\)
preserves \(C_rn^{-1/2}\). Treating this term as a prescribed forcing
along the actual solution does not change the retained gradient equation:
deleted current parameters are separate parameter coordinates, so their
instantaneous contributions are held fixed in retained partial derivatives.

Equations (A3)--(A4), the linear coordinate event, and
\(\|U\|\le n^{-1/10}\) also give the useful stronger form of (6),
\[
 \max_{a,i,t\le\sigma}|k_{a,i}-k^0_{a,i}|
 \le Cn^{-1/10}
\]
for large width. This rate is enough for the budget-difference arithmetic
stated in the source's pending Section 6; it does not prove that section.

## 4. Conditional Gaussian event and uniform path class

Once retained initialization is conditioned on, the stopped cavity,
\(J,P,Q\), and the stop endpoint are deterministic. Every response map
from fixed \(r\) omitted columns to the displayed linear vectors has
operator norm at most \(C_r(1+T_n)n^{1/400}\), hence at most
\(n^{1/200}\) after using an exponent margin.
For the retained-carrier derivative this follows from
\[
 D_\Theta k[U]=(U_H/\sqrt n)^\top\delta^0
                 +(W^0)^\top B_aU ,
\]
whose norm is bounded by \(C\). Its direct external derivative also has
bounded operator norm. There is no hidden carrier maximum in this map.

A coordinate of the linear response to \(N(0,I_n/n)\) columns has variance
at most \(C_rn^{-1+1/100}\). A threshold \(n^{-1/5}/2\) consequently
has failure probability at most
\(2\exp(-c_rn^{59/100})\). There are \(C_rn\) such coordinates.
The full parameter response can have ambient dimension \(O(n^2)\), but
its Gaussian image has input dimension \(rn\). Its expected Euclidean
norm is at most \(C_rn^{1/200}\), and Gaussian concentration at
\(n^{1/100}\) is more than sufficient. Ambient dimension is not the
rank in this calculation.

For the quadratic form, symmetrize \(R\); its trace is unchanged and its
operator and Hilbert--Schmidt norms do not increase. Diagonalizing that
symmetric matrix and using the elementary Gaussian-square generating
function yields the source's equation (16). Inserting
\(\|R\|_{\rm op}\le n^{1/200}\),
\(\|R\|_{\rm HS}\le\sqrt n\,\|R\|_{\rm op}\), and
threshold \(n^{-1/5}/2\) again gives the exponent \(n^{59/100}\).

For the deterministic bounded Lipschitz control class, sampling at spacing
\(n^{-3/10}/(C\log n)\), quantizing at \(n^{-3/10}\), and choosing
one actual control per occupied bin produces an internal uniform net.
Its log cardinality is bounded by
\(C_rn^{3/10}(\log n)^3\). The linear maps depend Lipschitz-continuously
on the control in the uniform norm, with constant
\(C_r(1+T_n)n^{1/400}\|x\|\), and the quadratic maps have the same
bound with \(\|x\|^2\). On \(\|x\|\le C_r\), both interpolation
errors are \(o(n^{-1/5})\). The net entropy is strictly smaller than
the Gaussian failure exponent.

Terminal-time interpolation is also valid. On the stopped cavity tube,
the normalized Euclidean parameter speeds and the coordinate speeds are
polynomial in width; all derivatives of tanh needed here are bounded.
The propagator has the above operator bound and solves a finite
variational equation whose coefficient has polynomial norm. The response
output maps, including \(B_a(t)\), have polynomial time-Lipschitz bounds.
For \(B_a\), differentiating its top-gate derivative invokes
\(\tanh'''\); this is bounded and should be named explicitly. The
control functions are Lipschitz as well. A sufficiently fine polynomial
time mesh thus contributes only \(O(\log n)\) to log cardinality.

The resulting failure probability can be weakened to
\(C_r\exp(-n^{2/5})\), as in the lemma. Uniformity over controls makes
the event applicable when the actual bounded control is subsequently
selected using the omitted columns. This argument conditions only on the
cavity reference, never on a stop determined by the full network.

## 5. Subinterval Schatten bound and trace

Let \(d\mu(u)=(2/m)\sum_a|r_a^0(u)|\,du\) be the cavity activity
measure. On the stop,
\[
 \mu([0,\sigma])\le CS,\qquad
 d\mu(u)\le CS\kappa e^{-\kappa u}\,du.
\]
The residual-Hessian operator \(\mathcal B(u)\) satisfies the same
normalized Schatten estimate as in the checked dependency:
\[
 \|\mathcal B(u)\|_{p,n}
 \le C\left[1+
       \left(n^{-1}\sum_{i=1}^{N}K_i(u)^p\right)^{1/p}\right],
 \quad K_i(u)=\max_a|k^0_{a,i}(u)| .
\]
On any \([s,t]\subset[0,\sigma]\), use the global bounds, without
restarting or renormalizing the exponential time weight. For integer
\(p\ge2\), \(x^p\le p!e^x\) and source assumption (3) give
\[
 \begin{aligned}
 \int_s^t
  \left(n^{-1}\sum_iK_i^p\right)^{1/p}d\mu
 &\le (CS)^{1-1/p}
      \left[\int_s^t n^{-1}\sum_iK_i^p\,d\mu\right]^{1/p}\\
 &\le C\frac{S^2p}{\eta}(2B)^{1/p}.
 \end{aligned}
\]
Therefore
\[
 \int_s^t\|\mathcal B(u)\|_{p,n}\,d\mu(u)
       \le CS+C\frac{S^2p}{\eta}(2B)^{1/p}.           \tag{A9}
\]
In particular there is no \(e^{\kappa s}\) loss.

Expand \(J(t,s)-U_0(t,s)\) in residual-Hessian insertions. The
between-insertion propagators \(U_0\) are contractions. The \(j\)th
term, normalized by \(\sqrt n\) in Hilbert--Schmidt norm, is at most
\[
 \frac1{j!}
   \left[\int_s^t
       \|\mathcal B(u)\|_{2j,n}\,d\mu(u)\right]^j .
 \tag{A10}
\]
Normalized Schatten Hölder cancels its powers of \(n\), even though
the full parameter dimension is \(O(n^2)\); the identity remains in
\(U_0\) and is never assigned a dimension-free normalized
Hilbert--Schmidt bound. The scalar integrand in the product bound is
symmetric, which supplies \(1/j!\).

Insert (A9). The bounded part sums to \(CS\); the other part has
\((2B)^{j/(2j)}=\sqrt{2B}\) and sums geometrically when
\(CS^2/\eta\le1/2\). Absorbing the fixed \(\eta\) dependence proves
\[
 \sup_{s\le t\le\sigma}
 \frac{\|J(t,s)-U_0(t,s)\|_{\rm HS}}{\sqrt n}
       \le CS+CS^2\sqrt B,
\]
which is equation (18).

For \(Q_a\), the contraction term \(B_bU_0Q_a\) has rank at most
\(n\) and norm \(C|r_a^0|\), so its normalized Hilbert--Schmidt
norm is \(C|r_a^0|\). The other term uses
\(\|B_b\|\le C\), the displayed Schatten estimate, and
\(\|Q_a\|\le C|r_a^0|\). Integrating against the bounded controls
gives trace bound \(CS+CS^3\sqrt B\). The direct diagonal top-response
derivative contributes \(CS\).

For \(P_a\), the composed \(n\)-by-\(n\) map \(B_bJP_a\) has rank
at most one. Thus
\[
 n^{-1}|\operatorname{tr}(B_bJP_a)|
 \le C S n^{-1+1/400},
\]
and its integral over \(T_n\) is \(o(1)\). This verifies equations
(19)--(20), including the adaptive forcing rather than dropping it.

## 6. Limits of the check

No fatal issue was found in the local insertion lemma under its stated
stops. The calculation above supplies the missing full reconstruction of
its nonlinear bound, rather than assuming it from a generic flow
Lipschitz estimate. The finite physical horizon is logarithmic and is
explicitly charged wherever the source lacks a residual factor.

The following claims are outside this positive verdict:

- that the full path and all required cavity stops can be removed;
- that fixed multiple-deletion comparisons give all needed empirical
  exponential moments with the stated event conditioning;
- that a fixed empirical budget closes with a strict margin;
- that the desired unconditional same-width root-width theorem follows.

The Gaussian event itself can be unioned over any fixed-size deletion
family, since the number of such subsets is polynomial in width.
That observation does not prove the empirical-moment step: the latter still
needs its common-cavity independence and stopped-event argument.
