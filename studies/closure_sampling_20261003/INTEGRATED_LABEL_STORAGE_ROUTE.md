# Retaining label RMS in the time radius and source storage

2026-10-04. Scoped theoretical continuation of the same canonical
compression investigation. This is a candidate internal derivation relative
to the checked local insertion, source selection and corrected-readout
interfaces. It is not a fresh cavity proof or promotion review. No training
experiment, external-study read, maintained-file edit, or Git operation was
performed.

The main improvement is an explicit source count proportional to
\((Ym/\gamma)^2\), in place of a coefficient proportional to
\(m/\gamma\). Its square is proportional to \((Ym/\gamma)^4\).
This retains the actual label RMS, and removes a separate inverse-gap
factor when the dimensionless label activity \(Ym/\gamma\) is fixed.
At fixed unscaled \(Y\), the leading storage still has fourth powers
of \(m/\gamma\). The exact initialization and dense-metric inventory
still has quadratic sample overhead. These distinctions are essential.

The improvement uses a larger coefficient in a still-shrinking complex
time strip. Its sufficient-width condition is correspondingly much worse
when labels are small. It is a fixed-\(Y>0\) asymptotic theorem,
not a bound uniform as \(Y\downarrow0\), and does not make the construction
practical at moderate widths.

## 1. Model, inherited interface, and precise conclusion

Let \(L\ge2\), \(d,m\ge1\), and \(v=x/\sqrt d\in S^{d-1}\).
The width-\(n\) dense reference is
\[
 z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
 h^{(j)}=\tanh z^{(j)},\qquad f_n=w^\top h^{(L)}/n.
\]
The first matrix has independent standard Gaussian entries, hidden mixers
have independent \(N(0,1/n)\) entries, all initialized blocks are
independent, and \(w(0)=0\). For fixed training inputs \(v_a\), put
\[
 r_a=f_n(v_a)-y_a,\quad k_a^{(L)}=w,\quad
 \delta_a^{(j)}=\tanh'(z_a^{(j)})\odot k_a^{(j)},\quad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The loss is \(m^{-1}\sum_a r_a^2\). Physical-time mobilities remain
\((n,1,\ldots,1,n)\), hence
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \quad \dot W^{(j)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(j)}h_a^{(j-1)\top},
 \quad \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{1}
\]
Define \(Q^{(0)}_{ab}=v_a^\top v_b\) and
\(Q^{(j)}_{ab}=\mathbb E[\tanh Z_a\tanh Z_b]\) for
\(Z\sim N(0,Q^{(j-1)})\). Set
\[
 \gamma=\lambda_{\min}(Q^{(L)})>0,\quad
 \lambda=\gamma/m\le1,\quad Y=\|y\|_2/\sqrt m,
 \quad u=Y/\lambda,\quad S=16u,
 \quad \ell_n=\log(en),\quad T=32\lambda^{-1}\ell_n.
 \tag{2}
\]
There is no extra sample normalization in \(\gamma\).

Assume the existing complete label condition from
RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md, equation (3), so in particular
\(0<u\le\min(c_{\rm src},c_{\rm rt})\). Its optional angular and
time caps may be kept; this note does not need a new label restriction.
All the defining recurrences for these caps are unchanged. Zero labels
give the exact zero predictor separately.

The inherited real source event supplies
\[
 \rho_n(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\lambda t/4},\qquad
 2\int_0^\infty\rho_n(t)\,dt\le S/2,
 \tag{3}
\]
strict real mixer cap \(15/4\), normalized first-matrix cap \(5/2\),
and the stopped local insertion/budget proof. On its complex extension,
use mixer cap four, first-matrix cap three and
\[
 a=1/2,\qquad B=1,\qquad s=16/15,\qquad b_2=1.
 \tag{4}
\]
Here \(a\) is the outer activation strip, \(B\) bounds its value,
and \(s,b_2\) bound its first two derivatives on
\(|\operatorname{Im}z|\le a/2\). The symbol \(b_2\) is a
derivative bound, not a layer index.

The following theorem is proved below relative to those inherited
interfaces. For every fixed admissible architecture, dataset and label
vector with \(Y>0\), at fixed confidence and sufficiently large width, the same
autonomous corrected-readout compressor exists with
\[
 R_{\rm src}\le A_n(Y)+2m+d+1,
 \tag{5}
\]
where, for \(d\ge2\),
\[
 A_n(Y)=\frac{2^{20}9^d}{d!}\,
       \frac{U(S)}a\,c_q(S)^{-(d-1)}
       \left(\frac{Ym}{\gamma}\right)^2
       \ell_n^{3d/2+1}.
 \tag{6}
\]
The finite explicit functions \(U(S)\) and \(c_q(S)\) are defined
in Section 2. Every moving and fixed real coordinate, including metrics,
inverse/copies, data and solve caches, is bounded by
\[
 \begin{split}
 \operatorname{size}(C)\le{}&
 1020(L+1)[A_n(Y)+2m+d+1]^2+10m(d+1)\\
 \le{}&2040(L+1)A_n(Y)^2
   +2040(L+1)(2m+d+1)^2+10m(d+1).
 \end{split}
 \tag{7}
\]
The source coordinate tolerance remains exactly \(n^{-1}\).
The inherited all-time error coefficient is unchanged:
\[
 \sup_{t\in[0,\infty],\,\|v\|=1}|f_C(t,v)-f_n(t,v)|
 \le C_{\rm all}(L,c)\,
       Y\left(\frac m\gamma\right)^{3/2}n^{-1/2}.
 \tag{8}
\]
Here \(C_{\rm all}(L,c)\) is exactly the finite recurrence in
RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md, equations (2), (5), (8)--(9),
(17), and (20)--(22), or (24) under its stated test. This note does not
replace that coefficient by an unspecified depth constant. In particular
its already certified depth-two choice remains \(c=2.8\,10^{-7}\),
\(C_{\rm all}=2.8\,10^5\).

## 2. Actual response coefficients before replacing activity by one

All constants needed in (6) are the following explicit recurrences.
They are taken from the checked source endpoint proof, with activity
powers retained before its last enlargement. For \(1\le j\le L\), set
\[
 K_j=2B(4s)^{L-j},\qquad P_1=2,\qquad
 P_j=B+4sP_{j-1}+1\quad(j\ge2),
\]
\[
 f_j=sP_j,\qquad t_j=sK_j,\qquad
 H_2=2sP_L+2s^2\sum_{j=2}^LK_jP_{j-1}
                  +b_2\sum_{j=1}^LP_j^2K_j,
\]
\[
 g=t_1+B\sum_{j=2}^Lt_j,\qquad r_j=P_jg,\qquad q_j=f_jg,
\]
\[
 e_1=b_2r_1P_1,\qquad
 e_j=b_2r_jP_j+s(q_{j-1}+t_jBf_{j-1}+4e_{j-1}),
\]
\[
 j_j^{\rm qry}=6(4s)^{j-1},\qquad b_j^{\rm qry}=sj_j^{\rm qry},
\]
\[
 a_1^{\rm qry}=b_2j_1^{\rm qry}P_1+2s,\qquad
 a_j^{\rm qry}=b_2j_j^{\rm qry}P_j
                 +s(b_{j-1}^{\rm qry}+4a_{j-1}^{\rm qry}),
\]
\[
 T_Q=8\max_jf_j\max_j(f_jH_2+e_j),\qquad
 T_J=8\max_jf_j\max_ja_j^{\rm qry},\qquad
 K_{\rm src}=32\max(1,\max_jK_j,\max_jt_j).
 \tag{9}
\]
The indexed numbers \(r_j\) are RMS response coefficients; the training
residuals are \(r_a(t)\). These have distinct index roles.
Put \(G_d=4\sqrt{d+3}\). Define
\[
 \begin{split}
 U_1(S)&=4sK_{\rm src},\\
 U_j(S)&=2\{sK_{\rm src}[B^2+f_{j-1}^2
                    +S T_Q+S^2Bq_{j-1}]+G_dq_{j-1}+1\},
                  \qquad j\ge2,\\
 V_1(S)&=2(2G_d+2sK_{\rm src}S^2+1),\\
 V_j(S)&=2\{G_db_{j-1}^{\rm qry}
       +sK_{\rm src}S^2(T_J+Bb_{j-1}^{\rm qry})+1\},
                  \qquad j\ge2,\\
 U(S)&=\max_jU_j(S),\qquad V(S)=\max_jV_j(S).
 \end{split}
 \tag{10}
\]
The source proof gives the actual training-carrier maximum
\(K_{\rm src}S\sqrt{\ell_n}\). In the row-insertion identity for a
forward response, the direct feature pairing and direct reverse trace
have bounds \(sK_{\rm src}S\sqrt{\ell_n}B^2\) and
\(sK_{\rm src}S\sqrt{\ell_n}f_{j-1}^2\). The same-root integral
has one additional activity factor \(S\), and the learned-row term
has two. Dividing these four terms by \(S\sqrt{\ell_n}\) gives
exactly the bracket in \(U_j(S)\). The centered Gaussian term gives
\(G_dq_{j-1}\). The factor two and added one keep strict margins
for the vanishing remainders. This is the term-by-term identity in
EXPLICIT_SOURCE_CONSTANTS_ROUTE.md, Section 4, before setting \(S\le1\).

For the angular response both correction terms have an exterior activity
factor times a training carrier. Thus their actual size is proportional
to \(S^2\), giving \(V_j(S)\). These are precisely the retained
activity powers already checked in ACTIVATION_CONSTANTS_REFINEMENT_CHECK.md.
No endpoint trace contains an unreported inverse power of \(S\).
Consequently the stopped coordinate estimates are
\[
 \max|R_a^{(j)}|\le U(S)S\sqrt{\ell_n},\qquad
 \max|J^{(j)}|\le V(S)\sqrt{\ell_n},
 \tag{11}
\]
where \(R_a^{(j)}=D_\Theta z^{(j)}\nabla_\Theta(nf_n(v_a))\),
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\), and
\(J^{(j)}\) is the derivative along a complex great circle of the
query sphere. Both definitions are residual-free responses, not velocities.

Use the radii
\[
 c_t(Y)=\frac a{64YSU(S)},\qquad
 c_q(S)=\min\{1/8,a/[8V(S)]\},\qquad
 r_t=\frac{c_t(Y)}{\sqrt{\ell_n}},\qquad
 r_q=\frac{c_q(S)}{\sqrt{\ell_n}}.
 \tag{12}
\]
Every denominator is positive because \(Y>0\). The old restriction
\(c_t\le1/8\) is deliberately absent. The restriction actually needed
in the short-contour proof is \(r_t\) small; Section 3 checks it and
states the resulting width conditions. For the query variable retaining
\(c_q\le1/8\) is convenient and loses no label power.

## 3. Why the larger time coefficient is admissible

The proof is carried out on the stopped rectangle
\[
 -r_t\le\operatorname{Re}z\le T+r_t,\qquad
 |\operatorname{Im}z|\le r_t
 \tag{13}
\]
and the intrinsic sphere tube of radius \(r_q\). The real anchor is
the projection of \(\operatorname{Re}z\) onto \([0,T]\), so neither
endpoint requires a carrier theorem outside the source interval. From
an anchor to any point of (13), at
most two short pieces of total length \(2r_t\) are needed. The query
extension is then one great-circle imaginary segment of length at most
\(r_q\).

Here are explicit deterministic requirements on the width. Keep the
runtime requirement \(n^{-1}\le Y\), as well as its original
fixed-confidence source threshold. Set
\[
 \mathcal K=B^2+S^2\left[t_1^2+B^2\sum_{j=2}^Lt_j^2\right],
 \qquad t_* =\max_jt_j.
\]
It suffices for this part of the argument that
\[
 \sqrt{\ell_n}\ge
 c_t(Y)\max\left\{8,\frac{4\mathcal K}{\log2},
                   64BYS t_*,32YS t_1\right\}.
 \tag{14}
\]
In particular the first entry is the explicit condition
\[
 \ell_n\ge64c_t(Y)^2
 =\frac{a^2}{64Y^2S^2U(S)^2}
 =\frac{a^2\lambda^2}{16384Y^4U(S)^2}.
 \tag{15}
\]
This condition must not be suppressed when explaining the gain.

To check residual growth, the complex tangent matrix is the algebraic
Gram of the actual sample parameter directions. In complex Euclidean
operator norm, normalized feature columns have RMS at most \(B\),
first-weight directions at most \(St_1\), and each hidden-matrix
direction at most \(SBt_j\). The triangle inequality for their
factorizations gives \(\|K_n/m\|_{\rm op}\le\mathcal K\).
Thus the analytic residual equation implies along any complex contour
\[
 |d\rho_n|\le2\mathcal K\rho_n|dz|.
\]
The real anchor has residual at most \(Y\), so on the short pieces
\(\rho_n\le Y e^{4\mathcal K r_t}\le2Y\) by (14).
The same operator estimate bounds the negative-Gram base variational
propagator by \(e^{4\mathcal K r_t}\le2\) on all its nonpositive-real
pieces together. Positive-real pieces are contractive. There is no factor
\(e^{\mathcal K T}\).

The extra absolute residual activity is at most
\(2(2Y)(2r_t)=8Yr_t\). Since \(r_t\le1/8\le1/\lambda\), it is
at most \(8Y/\lambda=S/2\). Together with (3), every contour still
has activity at most \(S\). Integrating the last equation of (1)
therefore gives \(\|w\|_\infty\le BS\). Bounded gates and complex
mixers give \(\|\delta^{(j)}\|_{2,n}\le St_j\), as required by
\(\mathcal K\). Here \(\|z\|_{2,n}=\|z\|_2/\sqrt n\).

On those pieces, direct integration of (1) bounds the hidden-mixer
increment by \(8BYS t_*r_t\), and the normalized first-matrix
increment by \(8YS t_1r_t\). The last two entries of (14) bound
these by \(1/8\) and \(1/4\), respectively. They preserve strict
margins inside the complex physical caps four and three. The preceding
estimates are imposed as stops and then improved, so using these caps
to estimate their increments is not circular.

The exact time derivative of a query preactivation is
\(\partial_tz^{(j)}=-(2/m)\sum_a r_aR_a^{(j)}\). Equations
(11) and \(\rho_n\le2Y\) give
\[
 |\partial_tz^{(j)}_i|\le4YSU(S)\sqrt{\ell_n}.
 \tag{16}
\]
The two short time pieces and the one query segment therefore have total
preactivation displacement at most
\[
 8c_t(Y)YSU(S)+c_q(S)V(S)\le a/8+a/8=a/4.
 \tag{17}
\]
As in the checked tanh extension, put full-system pole stops at \(3a/8\)
and autonomous cavity pole stops at \(7a/16\). These are both strictly
inside the safe derivative strip \(a/2\), with separation \(a/16\).
Coordinate-small full/cavity comparisons transfer the prefix, and (17)
improves the full stop. The augmented-graph Taylor segments also stay
inside the derivative strip eventually. Neither the source equations nor
their Gaussian event require a ratio-two pole cap.

The remaining small-contour input is the exponential moment of the
complex-minus-real cavity backward field. It still vanishes with the new
coefficient. To expose its dependence, let \(\eta,\mathcal B\) be the
unchanged explicit source budget constants in activation-route (3), and
put \(N_* =\max_j(r_j,U_j(S))\). Define
\[
 J_L^{\rm time}=2sB+4e b_2N_*,\qquad
 J_j^{\rm time}=4sJ_{j+1}^{\rm time}
                 +2Bs^3K_{j+1}^2+4e b_2N_*,\qquad
 J_*^{\rm time}=\max_jJ_j^{\rm time}.
 \tag{18}
\]
When \(\ell_n\ge\max(e^2,2\mathcal B)\), the carrier-budget
inequality with \(p=\max(4,\log(2\mathcal B\ell_n))\), followed by
counting-norm interpolation and differentiation of the backward recursion,
gives exactly the label-route bound
\[
 \|\dot\delta_a^{(j)}\|_{2,n}\le J_*^{\rm time}\rho_n
        [1+(S^2/\eta)\log(e+\ell_n)].
 \tag{19}
\]
For clarity, the changed-gate term uses
\(\|k\odot\dot z\|_{2,n}\le
 2\rho_nS^2N_*p(2\mathcal B\ell_n)^{1/p}/\eta\);
the changed-mixer term is at most
\(2Bs^3K_{j+1}^2\rho_n S^2\), and the terminal term is
\(2sB\rho_n\). These are precisely the three terms in (18).

Consequently the complex correction divided by \(S\) has normalized
Euclidean radius at most
\[
 D_n=\frac{\lambda c_t(Y)J_*^{\rm time}}{4\sqrt{\ell_n}}
           [1+(S^2/\eta)\log(e+\ell_n)].
 \tag{20}
\]
The factor \(\lambda/4\) comes from
\(2r_t\cdot2Y/S\), and is retained. Its two real-parameter Lipschitz
coefficients are bounded by fixed multiples of
\(\lambda J_*^{\rm time}[1+(S^2/\eta)\log(e+\ell_n)]\).
The domain length is at most \(T+2r_t\), so its two-dimensional
Gaussian net has logarithmic entropy \(O(\log\ell_n)\), with fixed
parameters and \(Y>0\). The elementary dyadic Gaussian sum therefore
has mean at most a fixed multiple of
\(D_n\sqrt{\log(C\ell_n^C/D_n)}\), and tail scale a fixed multiple
of \(D_n\). Both tend to zero. Thus every fixed exponential moment
of this correction tends to one, exactly the input needed by the existing
separate-budget removal. The explicit coefficients (18)--(20) show where
the new \(Y\)-dependent eventual threshold occurs; the inherited local
insertion remainder constants are still unquantified.

All remaining local-event derivative/control bounds change by fixed
factors only. Condition (14) puts the whole rectangle back inside the
same bounded-width geometry, so the spherical query grid still has at
most \(n^{4d+10}\) points eventually. The strict powers of \(n\)
in insertion remainders and variational caps are unchanged. The order is
the inherited one: impose budgets and all caps; transfer local cavity
prefixes; improve carrier and response caps; exclude poles; prove (20)'s
complex moment; remove budgets using fixed moments after the width limit.
This proves holomorphy on a neighborhood of the closed domain (13) times
the sphere tube, for every fixed label vector with \(Y>0\), allowing
arbitrary individual signs and ratios.

## 4. Exact finite count and its label dependence

All four source families
\[
 h^{(j)}(t,v),\quad W_0^{(j)}h^{(j-1)}(t,v),\quad
 \delta^{(j)}(t,v),\quad W_0^{(j+1)\top}\delta^{(j+1)}(t,v)
\]
have coordinate magnitude at most \(M_n=M_0\sqrt n\), where
\(M_0=8\max(B,\max_jt_j)\). The backward fields at a query use the
current dense parameters but supply no additional training force.

For \(d\ge2\), put
\[
 \alpha=\frac{r_t}{4T}
         =\frac{c_t(Y)\lambda}{128\ell_n^{3/2}},\qquad
 b_d=2d-2,\quad D_d=2^{d+1}d^{d-2},\quad \epsilon=n^{-1},
\]
\[
 P=\frac{18D_d b_d!2^{b_d+1}}{\alpha r_q^{b_d+1}},\qquad
 H=2\log(16M_nP/\epsilon),
\]
\[
 h_j={j+d-1\choose d-1}-{j+d-3\choose d-1},\qquad
 N=\sum_{0\le j\le H/r_q}h_j
       \left(1+\left\lfloor\frac{H-r_qj}{\alpha}\right\rfloor\right).
 \tag{21}
\]
Impossible binomial coefficients are zero. These are the exact spherical
source theorem's quantities, with only the proved radii replaced.
The time change \(t=T(1+\cos\theta)/2\) maps
\(|\operatorname{Im}\theta|\le\alpha\) into (13). Fourier contour
translation and the checked spherical harmonic projection estimate give
coefficient bound
\(M_nD_d(j+1)^{b_d}e^{-\alpha|k|-r_qj}\).
Splitting this exponential in half and summing its tails yields uniform
omitted error \(\epsilon/16\) for \(\alpha|k|+r_qj>H\).

The harmonic dimension satisfies
\(h_j\le2{j+d-2\choose d-2}\). Disjoint unit cubes therefore give
\[
 N\le\frac{2[H+\alpha+(d-1)r_q]^d}
                 {d!\alpha r_q^{d-1}}.
 \tag{22}
\]
This retains temporal degree zero and all lattice-rounding contributions;
it does not estimate the count by its leading monomial at fixed width.
The exact rank is at most \(4N+2m+d+1\).

To give (6), define
\[
 C_d^*=16\cdot128\cdot18\,M_0D_db_d!2^{b_d+1}
          \lambda^{-1}c_t(Y)^{-1}c_q(S)^{-(b_d+1)}.
\]
In addition to the source threshold impose
\[
 \log C_d^*\le\ell_n,\quad
 (d+1)\log\ell_n\le\ell_n,\quad
 (d-1)c_q(S)/\sqrt{\ell_n}\le1,\quad \alpha\le1.
 \tag{23}
\]
Then \(H\le7\ell_n\), the bracket in (22) is at most
\(9\ell_n\), and
\[
 4N\le\frac{1024\,9^d}{d!}\,
      \lambda^{-1}c_t(Y)^{-1}c_q(S)^{-(d-1)}
          \ell_n^{3d/2+1}.
 \tag{24}
\]
Finally,
\[
 \lambda^{-1}c_t(Y)^{-1}
       =\frac{64YSU(S)}{a\lambda}
       =\frac{1024U(S)}a\left(\frac Y\lambda\right)^2.
 \tag{25}
\]
Substitution proves (5)--(6). No inverse-radius coefficient in (25) has
been moved into the width threshold. Fixed coefficients inside the tail
logarithm and the lattice-rounding conditions remain explicitly in (23).

For \(d=1\), retain both sphere points \(-1,+1\). The inherited
time-only count gives the replacement
\[
 A_n(Y)=8\cdot514\cdot1024\,
         \frac{U(S)}a\left(\frac Y\lambda\right)^2\ell_n^{5/2},
 \qquad R_{\rm src}\le A_n(Y)+2m+2,
 \tag{26}
\]
with \(G_1=8\) in (10), and no query radius. This follows from
\(p+1\le514\lambda^{-1}c_t^{-1}\ell_n^{5/2}\) for each of the
eight time families. Its exact finite count can instead use the
one-dimensional Fourier tail and the retained degree, without this
eventual simplification. Formula (7) still applies.

The coefficient vectors are computed by the already checked finite
initial-jet continuation and finite quadrature. Replacing \(r_t\) by
the positive value (12) in that construction changes only finite setup
orders. Identical scalar operations are applied to each initialized
forward/transpose pair. Their exact linear action identities are
therefore preserved, with coordinate accuracy \(\epsilon\) for each
member separately. Harmonics, quadratures, jets and original-width source
vectors are discarded after the selected matrices and metrics are formed.
No target trajectory or time-dependent coefficient table remains.

## 5. What the effective activity does and does not prove

Equation (25) is the precise improvement in the present rectangular
source proof. The dimensionless number of temporal analytic lengths is
\[
 \frac T{r_t}=\frac{2048YSU(S)}{a\lambda}\ell_n^{3/2}
              =\frac{32768U(S)}a u^2\ell_n^{3/2}.
 \tag{27}
\]
The time radius is controlled by hidden preactivation velocity, so it
contains the product \(YS\), rather than \(Y\) alone. The finite
label activity \(u=Y/\lambda\) must stay visible through the count.

There is a smaller *integrated velocity bound*:
\[
 \int_0^\infty\rho_n(t)S\,dt\le4YS/\lambda=64u^2,
\]
and (11) on the real source interval gives
\[
 \int_0^T\max_{i,j,v}|\partial_tz_i^{(j)}(t,v)|\,dt
          \le128U(S)u^2\sqrt{\ell_n}.
 \tag{28}
\]
This removes the extra \(\ell_n\) from a real path-length estimate,
but it is not an analytic source-rank theorem. A nonuniform complex
domain and an approximation argument on it would be needed to replace
the rectangular ratio (27) by (28). Complex-time residual growth and
the base propagator must be rechecked if local radii cease to shrink.

For example the compact proof clock \(\tau=1-e^{-\lambda t/4}\)
turns a perfectly analytic decaying mode \(e^{-\mu t}\) into
\((1-\tau)^{4\mu/\lambda}\). For a noninteger positive exponent this
is not analytic at \(\tau=1\). Thus exponential fitting by itself
does not provide a fixed analytic strip in a compact activity clock.
No removal of a logarithmic width power is claimed here.

Expanding (7) keeps every dependence visible:
\[
 \operatorname{size}(C)\le
 2040(L+1)\left[\frac{2^{20}9^dU(16Ym/\gamma)}
                         {a\,d!\,c_q(16Ym/\gamma)^{d-1}}\right]^2
       \frac{Y^4m^4}{\gamma^4}\ell_n^{3d+2}
 +2040(L+1)(2m+d+1)^2+10m(d+1).
 \tag{29}
\]
At fixed \(u\), \(L\) and \(d\), the leading displayed coefficient
has no separate \(m\) or \(\gamma\) dependence. At fixed \(Y\),
the displayed dependence is fourth order in \(m/\gamma\), and the
admissible-label condition itself restricts which such variations are
allowed. The old and new bounds are both available; their minimum may
be used, without claiming a uniform finite-width improvement where
(14), (20) and (23) have not yet taken effect.

## 6. Quadratic sample overhead and the bounded activation scope

The \(+2m\) exact source additions are sufficient for exact initialization
of the feature Gram and paired actions. Full-sphere approximants already
approximate these training vectors, so omitting the additions is a
plausible smaller variant. It would replace exact initialized identities
by \(O(\epsilon)\) defects and require changes to the initial forward,
Gram and comparison estimates. This note does not invoke that unproved
variant or remove the additions from (7).

Moreover removing the explicit additions cannot by itself give linear
sample storage in the present runtime. Its top training-feature matrix
\(F_C\in\mathbb R^{N_L\times m}\) must have
\(F_C^\top H_LF_C\succ0\). Therefore \(N_L\ge m\). An approximate
initialized Gram within less than half its positive gap would give the
same conclusion. The actual construction stores dense neuron metrics,
their copies/inverses as needed, and dense sample solve caches, so its
specified array inventory retains quadratic sample capacity. Evaluating
Gram products without a stored cache would remove that one cache, but
does not reduce the dense neuron metric or moving mixer arrays. This is
an obstruction within this stored-array implementation, not a lower
bound for all autonomous representations or all encodings of its metrics.

The theorem proved here is for ordinary tanh. Its radius argument also
applies to the established bounded-strip analytic class when its own
explicit response constants and physical caps are substituted: the key
identity is always \(\lambda^{-1}c_t^{-1}=64YSU/(a\lambda)\).
For a capped gap \(\lambda=\min(1,\gamma/m)\), keep this expression
or \((Y/\lambda)^2\) exactly; it is not automatically
\((Ym/\gamma)^2\).

It does not automatically apply to an unbounded activation merely because
its strip derivative is bounded. The present proof uses a uniform value
bound \(B\) in the residual Gram estimate, readout activity bound,
backward RMS coefficients, endpoint traces and source coordinate magnitude.
The separate unbounded-activation source theorem would have to supply its
own uniform counterparts before (12)--(29) could be imported. No dense
finite-to-population variance theorem, normalized-activation theorem,
or unbounded-activation extension is newly asserted here.

The existing input-folding theorem can also be composed with (6) under
its own established label assumptions: replace the expensive source
dimension by \(D=\min(d,\dim\operatorname{span}\{v_a\}+1)\), retain
its additional projection storage \(10d(r+1)\), where
\(r=\dim\operatorname{span}\{v_a\}\), and add its separately proved
folding error. The data allowance in (7) still uses ambient \(d\).
This observation does not extend that theorem's old label condition
\(u\le16^{-62L}\) to the larger tanh cap. No such extension is used
in (5)--(29), which hold for full-dimensional queries directly.

## 7. Evidence and scope record

Complete primary/check inputs read for this bounded derivation were
INPUT_DIMENSION_REFINEMENT.md, ARCHITECTURE_CONSTANT_REFINEMENT.md,
ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md and its complete corrected check,
RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md and its check,
EXPLICIT_SOURCE_CONSTANTS_ROUTE.md including its reconciliation,
LABEL_DEPTH_RESCALING_ROUTE.md, DEPTH_INDEPENDENT_EXPONENT.md,
SPHERICAL_SOURCE_DIMENSION_ROUTE.md, SPHERICAL_SOURCE_DIMENSION_CHECK.md,
SPHERICAL_SOURCE_ADDITIONAL_CHECK.md, STORAGE_QUADRATIC_IMPROVEMENT.md,
and EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md. The original local cavity and
source-selection theorems are inherited through these explicitly identified
interfaces; they were not independently reproved in this note. Required
canonical notation, neural-response conventions, rigorous-proof, research
contract, evidence and adversarial-audit instructions were applied.

| Claim | Status and precise scope |
| --- | --- |
| Retained \(S,S^2\) source coefficients | Derived from the exact existing insertion identity |
| Uncapped coefficient \(c_t(Y)\) | Proved relative to the inherited stopped local interface; (14) makes its actual strip short |
| Rank (5)--(6), storage (7) | Proved by the unchanged harmonic count and complete runtime inventory |
| All-time output error (8) | Inherited unchanged after checking the paired-source interface |
| Replacing physical interval length by integrated activity | Open; (28) alone is insufficient |
| Removing exact training-source additions | Not used; would require a new initialized-error comparison |
| Linear total sample storage in this construction | Not supplied; positive top Gram and dense metric/caches retain quadratic overhead |
| Extension of these numerical formulas to unbounded activations | Not established |

This supersedes no existing broader theorem: it is an additional
label-sensitive sufficient source/storage bound. It changes no physical
clock, dense reference, optimizer, coordinate tolerance, observable norm,
or all-time endpoint. Setup work and precision remain outside the retained
real-coordinate contract; the complete stochastic width threshold remains
unquantified, with the new explicit and potentially severe conditions
(14)--(15), (20) and (23) now exposed.
