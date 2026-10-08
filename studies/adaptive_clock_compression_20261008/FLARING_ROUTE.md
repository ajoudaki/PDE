# Residual-adapted flaring time domain and cubic-logarithmic storage

2026-10-08. Scoped theoretical continuation. No experiment, runtime change,
paper edit, or Git operation. The frozen author candidate received the
scoped internal reconstruction in `FLARING_CHECK.md`; it is not a promoted
result. The lead subsequently corrected the doubled comma in F.7 and
made the checked finite-derivative compiler corollary explicit in Section
7. No probability estimate, label interval or storage count was changed.

The proposed repair of `ADAPTIVE_APPROXIMATION.md` Section 6 is to derive
the sharp time derivative estimate from the **provisional** response stops.
The derivative estimate does not require that the Gaussian argument has
already improved those stops. It then bounds the negative-Gram propagator
before the insertion argument is used. Independently clipped flaring
domains provide commuting real-anchor maps and globally defined,
cavity-measurable coefficient paths. With these two repairs, the qualitative
finite-deletion proof has the same strict width powers and the same source
coefficients on the larger domain.

The resulting source dimension is bounded by

\[
 O\!\left((2m+p)\ell\left[
 1+\frac{U_{\rm fin}(S)}a\left(\frac{Ym}{\gamma}\right)^2\sqrt\ell
 +\frac{\mathcal K m}{\gamma}\log(1+C\ell)\right]\right),
 \qquad \ell=\log(en).
 \tag{F.1}
\]

The displayed second term gives cubic-logarithmic retained storage. The
third term is retained explicitly; it is not silently absorbed using a
label cap or an unspecified width threshold. For each fixed admissible
problem all three terms give total storage \(O(\ell^3)\). The original
all-time comparison, including its endpoint and initialization-only
coefficient provenance, is unchanged.

## 1. Contract, inherited statements, and constants

There are \(m\) training inputs and \(p\) passive inputs, all declared at
initialization. The passive inputs have no labels and never enter a
training sum. Write \(v_i=x_i/\sqrt d\), with \(\|v_i\|_2=1\).
The canonical width-\(n\), depth-\(L\) network is

\[
 z_i^{(1)}=Av_i,\qquad
 z_i^{(j)}=W^{(j)}h_i^{(j-1)},\qquad
 h_i^{(j)}=\phi_j(z_i^{(j)}),\qquad
 f_n(v_i)=w^\top h_i^{(L)}/n.
\]

Initially the entries of \(A\) are independent \(N(0,1)\), the hidden
entries are independent \(N(0,1/n)\), all blocks are independent, and
\(w=0\). With \(r_a=f_n(v_a)-y_a\) and loss
\(m^{-1}\sum_{a\le m}r_a^2\), mobilities \((n,1,\ldots,1,n)\) give

\[
\begin{aligned}
 \dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
 \dot W^{(j)}=-\frac2{mn}\sum_a r_a
                         \delta_a^{(j)}h_a^{(j-1)\top},\\
 \dot w&=-\frac2m\sum_a r_ah_a^{(L)},\qquad
 \delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\\
 \delta_a^{(j)}&=\phi_j'(z_a^{(j)})\odot
                       W^{(j+1)\top}\delta_a^{(j+1)}.
\end{aligned}
\tag{F.2}
\]

All dots mean physical-time derivatives. Activations are real on the real
axis and holomorphic on \(|\Im z|<a\), with bounded first derivative;
their values may grow linearly. Retain the complete original label
allowance in `PANEL_BOUND.md` (3). Set

\[
 Y=\|y\|_2/\sqrt m>0,\quad \lambda=\gamma/m,\quad
 S=16Y/\lambda,\quad \nu=\lambda/4,\quad
 T_0=32\ell/\lambda,\quad
 r_n=\frac{a}{64YSU\sqrt\ell},\quad U=U_{\rm fin}(S).
 \tag{F.3}
\]

The zero-label case is the exact stationary zero predictor. The source
coefficients \(H_j,k_j,\tau_j,P_j,r_j^{\rm src},q_j^{\rm src},
K_{\rm src},U\) are precisely `PANEL_BOUND.md` (4). The exponential
budget coefficient and ceiling are denoted \(\eta_{\rm src}\) and
\(\mathcal B\), to distinguish them from the approximation tolerance.
They are the unchanged source S.10 constants in
`UNBOUNDED_COMPRESSOR_BRIDGE.md` (10).

Define

\[
 \mathcal K=H_L^2+S^2\left[\tau_1^2+
                \sum_{j=2}^L\tau_j^2H_{j-1}^2\right],\qquad
 B_n=1+\frac{S^2}{\eta_{\rm src}}\log(e+\ell).
 \tag{F.4}
\]

On the operator/RMS/activity stops, the algebraic residual Gram divided
by \(m\) has operator norm at most \(\mathcal K\). The real fitting
theorem gives \(\rho(t)=\|r(t)\|_2/\sqrt m\le Ye^{-\nu t}\),
operator caps strictly below nine, and real activity
\(2\int_0^\infty\rho(t)dt\le S/2\). Each fixed-size rectangular
cavity has the same facts on its own successful initialization test,
with the original normalization \(n\). This uses the explicit
zero-embedding initialization argument IC.71--IC.73, not an assertion
that rectangular initialization has the full-network covariance.

Since \(\lambda\le H_L^2\), the constant
\(d_h=\nu/(2\mathcal K)\) is at most \(1/8\). Indeed the population
feature RMS obeys \(v_j^{1/2}\le b+s v_{j-1}^{1/2}\), starting
from \(v_0=1\), so \(Q^{(L)}_{aa}\le H_L^2\); then
\(\gamma\le Q^{(L)}_{aa}\) and \(m\ge1\).

The deterministic coordinate selection and source-to-runtime comparison
are inherited through `PANEL_BOUND.md` and
`ADAPTIVE_APPROXIMATION.md` Section 2. The nontrivial Gaussian source
dependency used below is the complete local proof
`SOURCE_INSERTION_COMPLETION.md` Sections 1--5, together with its
common-cavity construction in Section 9 and the qualitative fixed-moment
removal in `UNBOUNDED_COMPRESSOR_BRIDGE.md` Sections 3--8. The present
proof verifies the changed domain-dependent hypotheses of those proofs;
it does not replace their finite-dimensional derivative identities or
their Gaussian quadratic-form calculation by an assumed new theorem.

## 2. Domain geometry and independent extensions

Put

\[
 h(t)=\frac1{2\mathcal K}
       \log(1+2\mathcal K r_n e^{\nu t}),\qquad
 h_0=h(0),\qquad T_+=T_0+h(T_0)+r_n.
 \tag{F.5}
\]

Thus \(h_0\le r_n\), \(0\le h'(t)\le d_h\le1/8\), and
\(h(t)\le r_n+d_h t\). For \(0\le s\le1\), use the nested
closed domains

\[
 D_s=\{x+iy:-s h_0\le x\le sT_+,\quad
                    |y|\le s h(\max(x,0))\}.
 \tag{F.6}
\]

These domains are not claimed convex. They are compact, vertically
fibered, and every point is joined to zero by its real anchor followed
by a vertical segment, except that a negative real coordinate also
uses a horizontal segment of length at most \(h_0\). They are nested
because their real intervals increase and their height at a fixed
coordinate increases with \(s\). They exhaust a deterministic domain
of real length and height \(O(\ell)\), for fixed problem parameters.

Each cavity has its own first-exit level \(s_c\), using its own initial
germ, retained initialization, and the usual full source stops. A failed
own initialization gives identically zero reference coefficients. Full
samplewise exponential budgets stop at \(\mathcal B\), cavity budgets
at \(2\mathcal B\); full temporary maxima and response caps are twice
the claimed values, cavity caps four times. Full and cavity pole caps
are \(3a/8\) and \(7a/16\). Retain the temporary passive
preactivation cap, operator/activity caps, and the same row-size stops.
Only real, finite panel queries are included.

For a real interval \(I\), let \(\operatorname{clip}_I\) be nearest
point clipping. Define, for all complex \(z=x+iy\),

\[
 X_s(x)=\operatorname{clip}_{[-s h_0,sT_+]}(x),\qquad
 P_s(z)=X_s(x)+i\operatorname{clip}_{[-s h(X_s(x)_+),s h(X_s(x)_+)]}(y),
 \tag{F.7}
\]

where \(u_+=\max(u,0)\). This is a retraction onto \(D_s\).
It is measurable in \(s\), and hence \(P_{s_c}\) is measurable in
the cavity's retained initialization only. Define the real anchor
\(a(z)=\operatorname{clip}_{[0,T_+]}(\Re z)\). Direct clipping of
the two real intervals gives

\[
 P_s a(z)=a(P_s z).
 \tag{F.8}
\]

Indeed both real coordinates equal
\(\operatorname{clip}_{[0,sT_+]}(x)\), and both imaginary
coordinates vanish. The two image points lie in \(D_s\).

Clipping an interval whose symmetric half-width changes by \(\Delta\)
changes the clipped value by at most \(|\Delta|\). Therefore

\[
 |\Delta X_s|\le|\Delta x|,\qquad
 |\Delta\Im P_s|\le|\Delta y|+d_h|\Delta x|.
\]

The shear matrix in this last pair is the identity plus a matrix of
operator norm \(d_h\). Hence \(P_s\) is \((1+d_h)\)-Lipschitz,
uniformly in \(s,n\). If \(b\) has complex derivative norm at
most \(L_b\) on a neighborhood of \(D_s\), then
\(b\circ P_s\) is \(L_b(1+d_h)\)-Lipschitz on the plane:
integrate along the absolutely continuous path
\(P_s((1-u)z+uz')\), which stays in \(D_s\) and has length at
most \((1+d_h)|z-z'|\). Convexity of \(D_s\) is unnecessary.

Extend every independently stopped coefficient by
\(\widetilde b_c(z)=b_c(P_{s_c}z)\), on the deterministic enclosing
rectangle

\[
 E_n=[-h_0,T_+]+i[-h(T_+),h(T_+)].
\]

Its complex-minus-real correction is
\(b_c(P_{s_c}z)-b_c(P_{s_c}a(z))\), whose second argument equals
\(a(P_{s_c}z)\) by (F.8). Real anchors move monotonically through
\([0,s_cT_+]\) and then freeze. Thus the old real-activity parameter
and its Gaussian moment estimate still apply exactly. No Gaussian law
is conditioned on full-network survival.

Local analytic continuation on these stopped domains has the same
finite-dimensional justification as for the old rectangles. On a strict
prefix, bounded finite-width parameters and separation from the
activation singularities give a local holomorphic ODE extension. Its
germ is unique; continuation along overlapping real-anchor/vertical
patches glues the solutions. The domain is simply connected, since its
vertical fibers retract continuously onto its real interval. At a first
exit, the strict pole margin below \(a/2\) permits one-sided derivative
bounds. A strict improvement of every stop extends the solution across
that boundary by compactness. The extensions (F.7) themselves need not
be holomorphic outside each cavity's stopped domain.

## 3. Sharp derivatives before improving the response stop

All the following estimates hold deterministically on an independently
stopped cavity with its provisional cap

\[
 \max_{a,b,j,i}|R_{ba,i}^{(j)}|\le4SU\sqrt\ell,
 \qquad R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta F_a,
 \quad F_a=nf_n(v_a),
 \tag{F.9}
\]

where \(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
The same estimates include the full network under its smaller cap.
The derivative identities and operator bounds give

\[
 \|\dot z_a^{(j)}\|_2/\sqrt n\le2\rho S r_j^{\rm src},\qquad
 \|\dot z_a^{(j)}\|_\infty\le8\rho SU\sqrt\ell.
 \tag{F.10}
\]

Set \(N_*^\#=\max_j\{r_j^{\rm src},4U\}\). For real \(q\ge4\),
interpolation between the two norms in (F.10) gives

\[
 \|\dot z_a^{(j)}\|_{2q/(q-2)}/n^{(q-2)/(2q)}
 \le2\rho S N_*^\#\ell^{1/q}.
\]

The stopped exponential budget gives
\(\|k_a^{(j)}\|_q/n^{1/q}\le(S/\eta_{\rm src})q
(2\mathcal B)^{1/q}\). Hölder therefore gives

\[
 \|k_a^{(j)}\odot\dot z_a^{(j)}\|_2/\sqrt n
 \le\frac{2\rho S^2N_*^\#}{\eta_{\rm src}}
                    q(2\mathcal B\ell)^{1/q}.
 \tag{F.11}
\]

For \(\ell\ge\max(e^2,2\mathcal B)\), take
\(q=\max(4,\log(2\mathcal B\ell))\). Then
\((2\mathcal B\ell)^{1/q}\le e\) and
\(q\le2\log(e+\ell)\). Differentiate the backward recursion in
(F.2). The readout term, changed mixer, changed gate, and propagated
upper derivative are bounded respectively by the recurrence

\[
 J_L^\#=2sH_L+4e t_2N_*^\#,\qquad
 J_j^\#=10sJ_{j+1}^\#+2s^3k_{j+1}^2H_j+4e t_2N_*^\#,
 \quad J_*^\#=\max_jJ_j^\#.
\]

Here \(s,t_2\) are the source half-strip first- and second-derivative
bounds. Consequently

\[
 \|\dot h_a^{(j)}\|_2/\sqrt n\le2\rho S q_j^{\rm src},\qquad
 \|\dot\delta_a^{(j)}\|_2/\sqrt n\le J_*^\# B_n\rho.
 \tag{F.12}
\]

This is the essential causal point: (F.12) follows from the provisional
stops (F.9) and the stopped budget, not from a Gaussian maximum
improvement, common-cavity moments, or survival on \(D_1\).

Define the normalized gradient matrix

\[
 G=\frac1{\sqrt{mn}}[\nabla_\Theta F_1,\ldots,
                                  \nabla_\Theta F_m].
\]

Its normalized column blocks are
\(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(j)}h_a^{(j-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Differentiating these blocks and using (F.12)
shows

\[
 \|G\|_{\rm op}\le\sqrt{\mathcal K},\qquad
 \|\dot G\|_{\rm op}\le C_g^\# B_n\rho,
 \tag{F.13}
\]
\[
 C_g^\#=J_*^\#\left(1+\sum_{j=2}^LH_{j-1}\right)
  +2S^2\sum_{j=2}^L\tau_jq_{j-1}^{\rm src}
  +2S q_L^{\rm src}.
\]

There is no factor \(m\): bound each column divided by \(\sqrt m\),
then use the matrix Frobenius norm. No Hessian operator maximum is used
in (F.13).

## 4. Deterministic activity and negative-Gram propagation

The exact residual and variational-base equations are

\[
 \dot r=-2G^\top G r,\qquad \dot P=-A P,\qquad A=2GG^\top.
 \tag{F.14}
\]

Transposes are algebraic. At real time \(t\), \(A(t)\) is real
symmetric positive semidefinite. On a stopped vertical segment at that
anchor, absolute norm differentiation in (F.14) gives

\[
 \rho(t\pm iv)\le Ye^{-\nu t}e^{2\mathcal K v},\qquad
 \int_0^{h(t)}\rho(t\pm iv)\,dv\le Yr_n.
 \tag{F.15}
\]

The second inequality is obtained by substituting
\(e^{2\mathcal K h(t)}=1+2\mathcal K r_n e^{\nu t}\).
It holds on every truncated vertical fiber of every \(D_s\). Moreover
\(\rho(t\pm iv)\le Y+2\mathcal K Yr_n\le2Y\) once
\(2\mathcal K r_n\le1\).

Freeze \(A(t)\). The propagator of \(-iA(t)\) is unitary. From
(F.13),

\[
 \|A(t\pm iv)-A(t)\|_{\rm op}
 \le4\sqrt{\mathcal K}C_g^\#B_n
                    \int_0^v\rho(t\pm iu)\,du.
\]

Conjugating the vertical equation by the frozen unitary and applying the
norm integral inequality bounds its propagator by

\[
 \exp\!\left(4\sqrt{\mathcal K}C_g^\#B_n
       \int_0^{h(t)}(h(t)-v)\rho(t\pm iv)\,dv\right)
 \le \exp\!\left(\frac{2C_g^\#}{\sqrt{\mathcal K}}
                                  B_nYr_n\right).
 \tag{F.16}
\]

Indeed the double integral is at most
\(Ye^{-\nu t}(e^{2\mathcal K h}-1-2\mathcal K h)/(4\mathcal K^2)
\le Yr_n/(2\mathcal K)\). For products on disjoint ordered
subsegments, use this same frozen \(A(t)\). Their nonnegative
norm-growth integrals add to no more than that on the whole segment.
Forward real pieces contract. Thus (F.16) is the product bound needed
in IC.51, not merely a bound on a single final propagator.

For a negative real part in \(D_s\), continue from zero along the
horizontal segment and then vertically. Their total length is at most
\(2h_0\le2r_n\). The old absolute Gram estimate gives residual
growth and total base-propagator cost at most \(e^{4\mathcal K r_n}\),
and integrated residual at most \(4Yr_n\) once that exponential is
at most two.

At fixed admissible parameters,
\(B_n r_n=O(\log(e+\ell)/\sqrt\ell)\to0\). Impose the explicit
additional eventual gate

\[
 \max\left\{4\mathcal K r_n,
       \frac{2C_g^\#}{\sqrt{\mathcal K}}B_nYr_n\right\}
 <\log(3/2).
 \tag{F.17}
\]

Every independently stopped base-propagator product then costs less
than \(3/2\), in particular less than the factor two used in IC.8
and IC.51. This improvement is deterministic under the provisional
stops. It therefore requires no added probabilistic propagator event
and no circular transfer of such an event between cavities.

Real activity is at most \(S/2\); extra activity is at most
\(8Yr_n\). The original gates \(8Yr_n\le S/2\) and
\(8YSD_Wr_n\le1/4\), where
\(D_W=\max(\tau_1,\max_{j\ge2}\tau_jH_{j-1})\), retain
activity cap \(S\) and strict operator margins inside ten. The bound
\(\rho\le2Y\) gives the scaled residual cap
\(\rho/S\le\lambda/8\). These are exactly IC.4's hypotheses.

## 5. Reconstructing insertion, maxima, and strict cavity transfer

This section identifies every domain-dependent input of the existing
finite-deletion proof. Its algebraic local identities are unchanged.

First, all canonical anchor contours have length at most
\((64/\lambda+4c_t)\ell\), where \(c_t=r_n\sqrt\ell\).
This follows from \(h(t)\le r_n+t/8\) and (F.5). Replace
IC.10's contour-length coefficient by this larger fixed number. The
gradient, port, forward, backward and passive-response recurrences
IC.5--IC.17 and IC.36--IC.43 still have operator bounds
\(n^{1/4000}\operatorname{poly}(\ell)\) and raw terminal
derivative bounds \(\sqrt n\,n^{1/4000}\operatorname{poly}(\ell)\).
They use only the operator/RMS/budget/provisional-coordinate bounds,
IC.4, and the base cost two. All are proved above on each stopped
cavity. The powers of \(n\) do not depend on depth or contour height.
The modified contour-length constant only changes fixed coefficients.

Second, the root controls retain polynomial-logarithmic amplitude and
\(\sqrt n\operatorname{poly}(\ell)\) speed. Their one-dimensional
net along the prescribed anchor contour still has
\(\log N_{\rm ctrl}\le n^{5/8}\operatorname{poly}(\ell)\), by
the explicit sampling construction IC.44. Coefficients extended with
(F.7) have the same derivative bounds up to \(9/8\). A deterministic
mesh of the enclosing rectangle \(E_n\), with both sides \(O(\ell)\),
has polynomial size; at spacing \(n^{-2}/\operatorname{poly}(\ell)\)
it has \(n^4\operatorname{poly}(\ell)\) points. Thus the finite
panel, root, coordinate, and fixed-deletion unions still cost less than
\(n^{0.65}\) in logarithmic cardinality eventually.

The root law conditional on retained initialization is unchanged.
IC.45's linear and centered-quadratic tail exponent remains
\(n^{0.78}\). Consequently the same uniform event has failure at
most \(e^{-n^{0.7}}\) eventually. Uniformity is over deterministic
one-dimensional control histories before substituting actual analytic
controls; no path-independence assertion for arbitrary controls on
\(E_n\) is needed.

Third, the exact nonlinear remainders IC.22--IC.35 and
IC.40--IC.43 are pointwise parameter identities with joining segments
inside the half-strip. Their Duhamel bound IC.46 has the same activity
integral, logarithmic horizon and full propagator bound IC.8, because
(F.17) supplies its base factor two. With
\(N=n^{1/100}\), \(d_0=n^{-1/10}\), and \(u_0=n^{-1/25}\),
the remainder is still

\[
 n^{1/4000}\operatorname{poly}(\ell)
 [n^{-8/100}+u_0^2+n^{-48/100}+n^{-1/2}]=o(u_0).
\]

Thus the common-prefix comparison remains a coordinate discrepancy
\(n^{-1/30}\) and whole-vector discrepancy \(2n^{1/100}\), for
forward, backward and passive response objects. Strip joining segments
remain within the exact IC.33 margin. The passive lower reverse
observable \(C_qC_a^\top\bar q_a\) is still included through
IC.39--IC.43; it is not replaced by an independent reverse operator.

Fourth, IC.48--IC.57's trace expansion uses products of base propagators
over ordered disjoint subsegments. Equation (F.16) verifies precisely
that use. The ordered residual integrals remain at most \(S^h/h!\).
All Schatten exponents, endpoint blocks, direct exterior trace, learned
row/column terms, and sample-RMS Cauchy--Schwarz factors therefore
retain their old coefficients. In particular the scalar envelope S.16
and the response coefficient \(U_{\rm fin}\) are unchanged.

Gaussian scalar maximum grids now lie in \(E_n\), of area
\(O(\ell^2)\). At spacing \(n^{-2}\) their count is
\(O(n^4\ell^2)\), hence at most \(n^5\) eventually. The finite
panel and driver indices are fixed. The original enclosing count
\(n^{10}\), tail \(4n^{10}e^{-1024\ell}\), and off-grid error
\(n^{-3/2}\operatorname{poly}(\ell)\) remain valid. The maximum
and mixed endpoint argument consequently improves the full provisional
caps to

\[
 \max|z_{a,i}^{(j)}|\le K_{\rm src}\sqrt\ell,\qquad
 \max|k_{a,i}^{(j)}|\le SK_{\rm src}\sqrt\ell,\qquad
 \max|R_{ba,i}^{(j)}|\le SU\sqrt\ell.
 \tag{F.18}
\]

The last bound covers each training driver and each declared evaluated
input; no passive backward moment budget is introduced. The temporary
passive preactivation cap improves by its initialized finite-panel
Gaussian maximum and by integrating the response bound against activity.

Finally, (F.15) and (F.18) give preactivation displacement from a real
anchor at most \(2SU\sqrt\ell\,Yr_n=a/32\) for nonnegative real
part. In the negative part the bound is
\(8YSU\sqrt\ell r_n=a/8\). Hence the full pole cap improves
strictly. A cavity cannot stop earlier on the full successful prefix:
the coordinate discrepancy transfers its maxima and response caps;
its budget is bounded by
\(e^{2\eta_{\rm src}n^{-1/30}}\mathcal H_a+O_q(1/n)<2\mathcal B\)
for fixed deletion count \(q\); pole margins transfer inside
\(7a/16\); operator/activity improvements were already deterministic.
This proves the same strict independent-cavity transfer used by IC.stop,
now with the explicit maps (F.7). Moment removal has not yet been used.

## 6. Global cavity Gaussian corrections and budget removal

It remains essential to prove moments on complete independently stopped
paths, even outside the full successful prefix. This is where the
residual integral, rather than the height of \(E_n\), matters.

For a forward coefficient divided by \(\sqrt n\), (F.12) and
(F.15) give complex-minus-real radius at most
\(2S\max_jq_j^{\rm src}Yr_n\). For a backward coefficient divided
by \(S\sqrt n\), the radius is at most
\(J_*^\#B_nYr_n/S\). The negative real corner costs at most four
times these bounds. Formula (F.8) shows these estimates remain true
after each cavity's own extension. In particular a common bound is

\[
 D_n=4Yr_n\max\{2S\max_jq_j^{\rm src},J_*^\#B_n/S\}
      =O\!\left(\frac{\log(e+\ell)}{\sqrt\ell}\right).
 \tag{F.19}
\]

These are conditional Gaussian coefficient radii, not smallness claims
for realized Gaussian coordinates. By \(\rho\le2Y\), (F.12),
and the uniform Lipschitz maps (F.7)--(F.8), the correction's global
normalized modulus is at most \(C B_n\), with fixed \(C\). The
enclosing rectangle has side \(O(\ell)\). Applying the proved
dyadic Gaussian estimate IC.77 therefore gives correction mean

\[
 O\!\left(D_n\sqrt{\log(e+C\ell B_n/D_n)}\right)
  =O\!\left(\frac{[\log(e+\ell)]^{3/2}}{\sqrt\ell}\right)\to0,
 \tag{F.20}
\]

and Gaussian tail radius \(2D_n\to0\). Fixed exponential moments
tend to one. The same holds for each sample RMS, by the RMS version
of IC.77; no independence across samples is assumed.

For singleton and common \(q\)-cavity differences, extend each first
with its own \(P_{s_c}\), then subtract and project the difference
onto the deterministic Euclidean ball of radius \(4n^{1/100}\).
Both complete paths are independent of the particular omitted root,
even though they are not independent of each other. The projection is
nonexpansive and fixes their difference on the successful common prefix
by Section 5. Its normalized Gaussian radius is \(4n^{-49/100}\).
The sum of their moduli is \(\operatorname{poly}(\ell)\), and its
parameter rectangle has side \(O(\ell)\). IC.77 therefore gives
mean \(O(n^{-49/100}\sqrt\ell)\) and fixed exponential moments
tending to one, exactly as in IC.78.

The real reference paths themselves have unchanged activity modulus
S.17--S.18. Their conditional squared-exponential bound S.20, including
the sample-RMS Jensen bound, therefore retains the same \(W_{\rm G}\).
The actual-amplitude scalar envelope has the same \(C_{\rm abs}\).
Its main common-cavity one-neuron moment remains below four at exponent
up to \(8\eta_{\rm src}\). Distinct omitted roots are conditionally
independent given the common cavity. Separating the main reference
products from the corrections by Cauchy--Schwarz and Hölder at each
fixed \(q\) gives the same limiting upper base sixteen as S.29.
Full-event indicators are dropped only from the resulting nonnegative
cavity-measurable bounds, never included in Gaussian conditioning.

For completeness, collisions can use the source maximum already proved
in (F.18): their one-neuron exponential weight is bounded by
\(e^{2\eta_{\rm src}K_{\rm src}\sqrt\ell}=n^{o(1)}\).
For a fixed moment order \(q\), any tuple with \(k<q\) distinct
indices has normalized multiplicity \(O_q(n^{k-q})\). Keeping one
weight per distinct root and bounding its repeated weights by this
maximum makes the contribution \(n^{-(q-k)+o(1)}\to0\). The local
exceptional probabilities are superpolynomial and all stopped weights
are polynomially bounded at each fixed moment order.

If a full budget is hit, a sample/layer average is at least
\(\mathcal B/L\). The same Markov and fixed sample/layer union give

\[
 \limsup_{n\to\infty}\Pr\{\text{a full budget is hit}\}
 \le mL(16L/\mathcal B)^q.
 \tag{F.21}
\]

First take the width limit at each fixed positive integer \(q\), then
its infimum. Since \(16L/\mathcal B<1\), all budgets are removed
with probability tending to one. Sections 4--5 improved every other
stop. Thus the candidate enlarged event gives a holomorphic neighborhood
of \(D_1\), all four required source families, the original coordinate
bound \(M_0\sqrt n\), and the original improved real carrier bound.
Its stochastic width onset remains qualitative. No effective polynomial
onset or uniform theorem for growing \(m,p,d,L\) is asserted.

## 7. Inscribed disks, finite coefficients, and the retained count

For \(0\le t\le T_0\), set

\[
 \varrho(t)=\frac{h(t)}{2(1+d_h)}.
 \tag{F.22}
\]

The closed disk of this radius about \(t\) is contained in \(D_1\).
For its nonnegative real coordinates \(x\),
\(h(x)\ge h(t)-d_h\varrho(t)\ge\varrho(t)\); for negative
\(x\), the inequality \(h(t)\le h_0+d_h t\), together with
\(t<\varrho(t)\), implies \(\varrho(t)<h_0\). Its left
endpoint is at least \(-h_0\). Its right endpoint is below
\(T_0+h(T_0)<T_+\). These statements verify every boundary of
(F.6). The holomorphic neighborhood established above supplies strict
analytic slack about these disks.

The radius is nondecreasing and has Lipschitz constant
\(d_h/[2(1+d_h)]\). The complete adaptive-panel lemma in
`ADAPTIVE_APPROXIMATION.md` Section 2 therefore applies. Its panel
count \(J\) satisfies

\[
\begin{aligned}
 J&\le1+\left(2+\frac{d_h}{2(1+d_h)}\right)
                2(1+d_h)\int_0^{T_0}\frac{dt}{h(t)}\\
  &\le1+5\int_0^{T_0}\frac{dt}{h(t)}\\
  &\le1+\frac{10}{\nu r_n}
       +\frac{20\mathcal K}{\nu}
               \log\left(1+\frac{\nu T_0}{2\log2}\right)\\
  &=1+40960\frac Ua\left(\frac{Ym}{\gamma}\right)^2\sqrt\ell
       +80\frac{\mathcal K m}{\gamma}
                      \log\left(1+\frac{4\ell}{\log2}\right).
\end{aligned}
\tag{F.23}
\]

The integral bound follows by splitting where
\(2\mathcal K r_ne^{\nu t}=1\): before that point,
\(\log(1+x)\ge x/2\); after it, the logarithm grows at least
linearly with slope \(\nu/2\). This is precisely the proven
bound (21) of the adaptive note with \(\kappa=2\mathcal K\).
The harmless factor five uses \(d_h\le1/8\).

Choose the original all-time target and its source tolerance \(\eta\)
from `PANEL_BOUND.md` (16), with the original tail gate and comparison
coefficient containing \(e^{64\sqrt\ell}\). Set

\[
 K=\max\left(0,\left\lceil\log_2(8M_0\sqrt n/\eta)\right\rceil\right),
 \quad F=2(2m+p),\quad B=2m+d+1,\quad R=B+FJ(K+1).
 \tag{F.24}
\]

Here \(K\) is temporal polynomial degree and is unrelated to
\(\mathcal K\). The adaptive Taylor proof supplies uniform coordinate
source error \(\eta\), including both initialized forward and transpose
image pairs. Its real anchors are finite and predetermined by (F.22).
The original finite initialization/jet evaluator approximates the
required real-anchor derivatives to arbitrary finite accuracy using
continuation from initialization; the enlarged domain is used to prove
the Taylor tail, not as a future-trajectory oracle. Form each initialized
image from the computed base coefficient exactly. All source coefficients,
jets, anchors and dense arrays are discarded after selection.

Here is the finite-derivative corollary explicitly. The enlarged domain
contains a uniform rectangle about \([0,T_0]\) of positive radius
\(\varrho(0)\). Use that radius in the inherited conformal map
\(t=\mathfrak t(\xi)\), which has \(\mathfrak t(0)=0\), nonzero
derivative, and maps a compact real interval \([0,\xi_*]\), with
\(\xi_*<1\), onto \([0,T_0]\). For a source \(u\), the coefficients
of \(G(\xi)=u(\mathfrak t(\xi))\) through degree \(N\) are finite
linear combinations of its normalized zero-time jets through degree
\(N\). Its coefficient bound is \(M_0\sqrt n\). Choose
\(\xi_*<\rho_*<1\) and \(0<\delta_*<\rho_*-\xi_*\). For its
Taylor partial sum \(G_N\), summation of the geometric tail and the
Cauchy derivative formula give, at every real anchor \(\xi_b\),

\[
 \sup_{|\xi|\le\rho_*}|G-G_N|
 \le\frac{M_0\sqrt n\,\rho_*^{N+1}}{1-\rho_*},\qquad
 |(G-G_N)^{(k)}(\xi_b)|
 \le\frac{k!M_0\sqrt n\,\rho_*^{N+1}}
          {\delta_*^k(1-\rho_*)}.
\]

The operator \((\mathfrak t'^{-1}\partial_\xi)^k\) converts these
to the physical derivatives of \(u\) at each anchor. Its coefficients
are finite at the finitely many anchors for every \(k\le K\), so a
finite common \(N\) achieves any requested coefficient accuracy. For
clarity, store during assembly the scaled panel coefficients
\(\varrho(t_b)^k u^{(k)}(t_b)/k!\); they span exactly the same source
space as the unscaled derivatives. Each approximation panel has
\(|t-t_b|/\varrho(t_b)\le1/2\). Euclidean coefficient error
\(\eta/128\) therefore contributes at most \(\eta/64\) on a
panel after summing the geometric weights. Computing its paired image
by applying the initialized norm-eight matrix gives error at most
\(\eta/8\) and an exact image relation for the computed coefficient.
The Taylor tails leave both source errors below \(\eta\). This is a
finite linear compiler from initial jets, not a dense trajectory oracle;
its order, arithmetic work and precision may be very large.

The original selection theorem gives \(q_j\le9R\), and the complete
retained count is

\[
 1020(L+1)R^2+36R+10m(d+1)+pd+(m+p)+D_{\rm alg}.
 \tag{F.25}
\]

At fixed problem parameters, the original accuracy prescription gives
\(K+1=O(\ell)\). Combining (F.23)--(F.25), without hiding the
gap-dependent logarithmic-panel term, gives a sufficient upper bound

\[
\begin{split}
 C(L+1)\bigg\{B^2+(2m+p)^2\bigg[
 &\ell^2+
 \left(\frac Ua\right)^2\left(\frac{Ym}{\gamma}\right)^4\ell^3\\
 &+\left(\frac{\mathcal K m}{\gamma}\right)^2
       \ell^2\log^2\left(1+\frac{4\ell}{\log2}\right)
 \bigg]\bigg\}
 +C(m+p)(d+1)+D_{\rm alg}.
\end{split}
\tag{F.26}
\]

Use \((u+v+w)^2\le3(u^2+v^2+w^2)\) to obtain this expression
from the exact formulas. The universal numerical \(C\) also requires
an explicit eventual gate \(K+1\le C_0\ell\), with fixed numerical
\(C_0\), just as in the original inverse construction. That gate is
eventually satisfied for the original variability target or the stronger
target \(Y/n\). The exact formulas (F.23)--(F.25) need no such
simplification.

The optional exact input-span reduction replaces \(d\) in \(B\) by
\(k\le\min(d,m+p)\), at additional counted storage
\(O((m+p)d)\). Since \(\log^2(1+C\ell)=O(\ell)\), (F.26)
is \(O(\ell^3)\) for fixed parameters. Its explicit new
\((\mathcal K m/\gamma)^2\) term is not deleted. Neither the
fourth power of \(Ym/\gamma\) nor a new exponential in \(m\) is
hidden by the label allowance.

The selected runtime remains the original autonomous corrected optimizer
in physical time. Source comparison is needed only through \(T_0\).
Afterward, compare each fitted flow to its own value at \(T_0\) and
integrate its original tail; both trajectories keep evolving. Their
convergent limits give the same endpoint error. No time panel table,
forcing, or endpoint playback is retained.

## 8. Status and focused reconstruction

Established directly in this note are the clipped-domain retraction and
commutation formula, the derivative estimate from provisional stops, the
near-unitary product estimate on the resulting fibers, and the disk and
panel-count formulas. The source-event and cubic-logarithmic compression
conclusions were subsequently reconstructed in `FLARING_CHECK.md` under
the inherited finite-deletion and runtime interfaces. The focused checks
were:

1. The first-exit continuation and transfer in Sections 2 and 5, with
   independently stopped coefficients rather than conditioning on full
   survival.
2. Whether any use in IC.5--IC.57 of the old rectangle requires more
   than the verified contour-length, activity, base-product and global
   modulus bounds.
3. The fixed-common-cavity and collision argument on the globally
   extended paths in Section 6.

The earlier conditional Section 6 of `ADAPTIVE_APPROXIMATION.md` is
superseded for this specific flaring domain by the proof and scoped
internal check here. Stronger domains needed for near-second-power
storage remain unproved. The checker reused an existing context and
did not freshly audit the entire paper; this is an internal study result,
not promotion-level review. The complete checked source hashes, read
scope, coefficient bridge and limitations are retained in its report.

Scientific inputs used were the complete adaptive note, complete
`PANEL_BOUND.md`, complete `SOURCE_INSERTION_COMPLETION.md`, complete
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, current paper lines 5950--6370,
and maintained `docs/notation.qmd`. The source constants and model
interfaces were taken from these inputs. No live alternative-route file
or unassigned study was read. The canonical-notation and neural-network
reference, rigorous-math skill, conjecture skill and its contract,
evidence, audit and bounded-proof-search references were read and applied.
