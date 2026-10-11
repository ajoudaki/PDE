# Taylor route: a capped flaring domain with confidence-independent rank

2026-10-10. Scoped author candidate; no paper or book modification. This is
not an independent review or a promotion. The new proved calculations are
the domain cap in Sections 2–3 and the fixed-exponent common-cavity moment
argument in Section 4. Section 5 spells out the finite local-transfer
interface and its proposed quantitative substitution, so its claim can be
checked separately from those two calculations. The confidence order never
enters the domain or the retained-state coefficient.

## 1. Statement and source correspondence

Use the network, activation class, Gaussian initialization, physical
optimizer, labels and population Gram of `paper/compact.tex`, without
changing their normalization. Thus, for a normalized input
\(v=x/\sqrt d\),

\[
z^{(1)}(v)=W^{(1)}v,\qquad
z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
f_n(v)=w^\top h^{(L)}(v)/n.
\]

The readout starts at zero. For the training inputs \(v_a\), the
residual is \(r_a=f_n(v_a)-y_a\), the loss is
\(m^{-1}\sum_a r_a^2\), and

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad
\dot W^{(j)}=-\frac2{mn}\sum_a
r_a\delta_a^{(j)}h_a^{(j-1)\top},
\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\]

Here \(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\) and
\(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot
W^{(j+1)\top}\delta_a^{(j+1)}\). There are \(p\) passive inputs,
declared before initialization; put \(N=m+p\). Passive inputs never
enter these updates. Write

\[
\lambda=\gamma/m\in(0,1],\qquad
Y=\|y\|_2/\sqrt m>0,\qquad
S=16Y/\lambda,\qquad
\ell=\log(en),\qquad q_n=\log(e+\ell).
\tag{1}
\]

The local symbol \(q_n\) is a logarithm, not the source dimension
called \(q\) in the paper. Retain its hypothesis
\(Y/\lambda\le\beta^{-30L}\), so the exact source coefficients in
`compact_foundations.tex` satisfy

\[
S\le\beta^{-26L}\le S_*,\quad S^2/\eta_*\le1,
\quad U_{\rm fin}\le\beta^{26L},\quad
1\le\mathcal K\le\beta^{14L},\quad
\eta_*^{-1}\le\beta^{25L+4}.
\tag{2}
\]

Here \(S_*\), \(\eta_*\), \(U_{\rm fin}\), \(\mathcal K\),
\(D_W\), \(J_*\) and \(C_g\) mean precisely the positive finite
recurrences in that proof, not unspecified constants. In particular its
time-derivative and gradient-derivative recurrences give the deliberately
loose common envelope

\[
\max\{\mathcal K,D_W,U_{\rm fin},\max_jq_j^*,J_*,C_g,
\eta_*^{-1}\}\le\beta^{100L}.
\tag{3}
\]

To check (3), its displayed bounds give \(q_j^*\le\beta^{8L-2}\)
and \(r_j^*\le\beta^{8L-3}\). Thus
\(N_*:=\max_j\{r_j^*,4U_{\rm fin}\}\le\beta^{27L}\).
The forcing terms of the recurrence for \(J_j\) are at most
\(\beta^{30L}\), and propagation by \((10s)^L\), followed by
the sum over \(L\) layers, is at most \(\beta^{3L}\).
Hence \(J_*\le\beta^{33L}\). Substitution in
\(C_g=J_*(1+\sum H_{j-1})+2S^2\sum\tau_jq_{j-1}^*+2Sq_L^*\)
gives \(C_g\le\beta^{38L}\). These are below (3).

The candidate source width below is polynomial in
\(\beta^L,m+p,d,\lambda^{-1},\delta^{-1}\), with no inverse
positive-label factor. Accuracy and the simplified storage display have
additional, separately stated polynomial gates. The final selected
optimizer is exactly the paper's optimizer.

## 2. Capping the flaring radius

Set \(a_0=\min(a,1)\), merely using a smaller strip for the
construction, and define

\[
B_n=1+(S^2/\eta_*)q_n,\qquad B=\beta^{300L},
\]

\[
R_n=\frac1{B(1+\lambda B_n)\sqrt{q_n}},\qquad
r_n=\min\left\{
\frac{a_0}{64YSU_{\rm fin}\sqrt\ell},\ R_n\right\}.
\tag{4}
\]

No confidence parameter occurs in (4). The use of \(a_0\) imposes
no stronger activation or label assumption: all strip bounds already
hold there, and \(a_0^{-1}\le\max(1,\beta/16)\le\beta\).

Use the paper's flaring function, with this new \(r_n\):

\[
\nu=\lambda/4,\quad T=32\ell/\lambda,\quad
h(t)=\frac1{2\mathcal K}
\log(1+2\mathcal K r_ne^{\nu t}),\quad
d_h=\frac\nu{2\mathcal K},\quad
T_+=T+h(T)+r_n.
\tag{5}
\]

The nested domains and their retractions are

\[
D_s=\{x+iy:-s h(0)\le x\le sT_+,
\ |y|\le s h(\max(x,0))\},\quad 0\le s\le1,
\]

\[
X_s(x)=\operatorname{clip}_{[-s h(0),sT_+]}x,
\quad
P_s(x+iy)=X_s(x)+i\operatorname{clip}_{[-s h(X_s(x)_+),
s h(X_s(x)_+)]}y.
\tag{6}
\]

Since \(\lambda\le\mathcal K\), one has
\(h'\le d_h\le1/8\), \(h(0)\le r_n\),
\(h(t)\le r_n+t/8\), and
\(\operatorname{Lip}(P_s)\le9/8\). The latter follows by bounding
coordinate increments by the shear
\((|\Delta x|,|\Delta y|+d_h|\Delta x|)\), whose operator norm
is at most \(1+d_h\). With
\(a_0^{\rm time}(z)=\operatorname{clip}_{[0,T_+]}\Re z\),
\(P_s a_0^{\rm time}=a_0^{\rm time}P_s\). The time-anchor map
is unrelated to the strip number \(a_0\).

Every canonical contour consisting of a real segment and one vertical
segment, with at most the negative-real corner at zero, has length at
most \(64\ell/\lambda\). The bounding rectangle has sides at
most \(128\ell/\lambda\). Indeed
\(T_+\le9T/8+2r_n\),
\(h(T_+)\le r_n+T_+/8\), \(r_n\le1\), and
\(\ell/\lambda\ge1\). The domains retain the geometry required
by the independently stopped source proof.

The rectangle gates that matter dynamically are now automatic. In terms
of the actual radius they are

\[
r_n\le\min\{1/8,1/\lambda,\log2/(4\mathcal K),
1/(32YSD_W)\}.
\tag{7}
\]

They follow from \(r_n\le B^{-1}\), (3), \(Y=\lambda S/16\),
\(S\le1\), and \(\lambda\le1\). The remaining gate
\(\ell\ge\max(e^2,2\mathcal B)\),
\(\mathcal B=1024e^2L\), is paid by a fixed power of
\(\beta^L\) in the width below. The old lower-label gate
\(n^{-1}\le\min(Y,S)\) is not used in the normalized insertion
argument in Section 5.

The flaring propagator gate must be the **sum**

\[
4\mathcal K r_n+
\frac{2C_g}{\sqrt{\mathcal K}}B_nYr_n<\log(3/2).
\tag{8}
\]

It is not enough to bound the maximum of the two exponents. Formula (4)
gives, directly,

\[
4\mathcal K r_n\le\frac{4\mathcal K}{B},\qquad
\frac{2C_g}{\sqrt{\mathcal K}}B_nYr_n
\le\frac{C_g S}{8B\sqrt{\mathcal K q_n}}
\frac{\lambda B_n}{1+\lambda B_n}
\le\frac{C_g}{8B}.
\tag{9}
\]

Their sum is less than \(1/100\) by (3), \(\beta\ge10\),
and \(L\ge2\). This proves (8) at every width.

For completeness, the use of (8) has the following precise content.
On each cavity's provisional stops the source recurrences give
\(\|G\|\le\sqrt{\mathcal K}\) and
\(\|\dot G\|\le C_gB_n\rho\), where
\(G=(mn)^{-1/2}[\nabla_\Theta(nf_a)]_{a=1}^m\),
\(\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\),
and \(\rho=\|r\|_2/\sqrt m\). Along a vertical segment,

\[
\rho(t\pm iv)\le Ye^{-\nu t}e^{2\mathcal Kv},
\qquad
\int_0^{h(t)}\rho(t\pm iv)\,dv\le Yr_n.
\tag{10}
\]

The integral is bounded by substituting (5) into the integral of the
exponential. In particular \(\rho\le Y+2\mathcal KYr_n\le2Y\).
Freeze the real symmetric generator \(2G(t)G(t)^\top\) on this
segment. Its imaginary-time evolution is unitary. The difference of
generators has norm at most
\(4\sqrt{\mathcal K}C_gB_n\int_0^v\rho(t\pm iu)\,du\).
Its integrated norm is at most
\((2C_g/\sqrt{\mathcal K})B_nYr_n\), because the resulting
double integral is at most \(Yr_n/(2\mathcal K)\).
The negative-real corner costs at most \(e^{4\mathcal Kr_n}\).
Products on ordered disjoint contour pieces obey the product of these
bounds; their growth integrals add. Real forward segments contract.
This proves the factor-two base-propagator premise from the sum (8),
without using complex Gram positivity.

Additional activity is at most \(8Yr_n\), normalized operator motion
at most \(8YSD_Wr_n\), and the improved response estimate gives
vertical preactivation displacement at most
\(2YSU_{\rm fin}\sqrt\ell r_n\le a_0/32\).
The negative corner costs at most \(a_0/8\). Thus the activity,
operator and pole margins in the current proof all have strict room.

## 3. The cap preserves the current panel count

The disk of radius \(\varrho(t)=h(t)/(2(1+d_h))\) centered at
\(t\in[0,T]\) lies inside \(D_1\). For a nonnegative real
coordinate \(x\) in that disk,
\(h(x)\ge h(t)-d_h\varrho(t)\ge\varrho(t)\).
If \(x<0\), then \(t<\varrho(t)\) and
\(h(t)\le h(0)+d_ht\) imply \(\varrho(t)<h(0)\).
The right endpoint is below \(T+h(T)<T_+\).

Take \(t_0=0\) and
\(t_{b+1}=\min\{T,t_b+\varrho(t_b)/2\}\).
Since \(\varrho\) is nondecreasing and has Lipschitz constant
at most \(d_h/[2(1+d_h)]\), each complete panel contributes at
least the reciprocal of \(2+d_h/[2(1+d_h)]\) to
\(\int dt/\varrho(t)\). Consequently

\[
J\le1+5\int_0^T\frac{dt}{h(t)}
\le1+\frac{40}{\lambda r_n}
+\frac{80\mathcal K}{\lambda}
\log\left(1+\frac{4\ell}{\log2}\right).
\tag{11}
\]

For the second inequality split at
\(2\mathcal Kr_ne^{\nu t}=1\), use
\(\log(1+x)\ge x/2\) before that point, and use logarithmic
growth of slope at least \(\nu/2\) afterward. If the split point
is outside \([0,T]\), the corresponding interval is empty and
the same upper bound remains valid.

Taking the reciprocal of (4), and bounding a maximum by a sum, gives

\[
\frac1{\lambda r_n}
\le\frac{1024U_{\rm fin}}{a_0}
\left(\frac Y\lambda\right)^2\sqrt\ell
+B\lambda^{-1}\sqrt{q_n}+BB_n\sqrt{q_n}.
\tag{12}
\]

For \(x=\log\ell\ge0\),
\(q_n\le2+x\), and the maximum of
\((2+x)^{3/2}e^{-x/2}\) is attained at \(x=1\) and is below
four. Hence \(q_n^{3/2}\le4\sqrt\ell\). Using
\(\sqrt{q_n}\le q_n\) and \(\lambda\le1\), the last two
terms of (12) are at most

\[
2B\lambda^{-1}q_n+4B(S^2/\eta_*)\sqrt\ell.
\tag{13}
\]

Since \(S^2=256(Y/\lambda)^2\), (2) and (11)–(13) prove

\[
J\le1+C\left[
\left(\frac Y\lambda\right)^2\sqrt\ell
+\lambda^{-1}\log(e+\ell)\right],
\tag{14}
\]

where, for example, \(C\le\beta^{400L}\) is sufficient. This
constant depends only on activation bounds and depth. It contains no
confidence, sample, passive-panel, dimension, gap or label factor.
The extra cap has therefore not transferred an inverse-gap exponential
into storage, nor added a confidence factor to the Taylor rank.

## 4. Complete complex references before the distinct-root product

This is the probabilistic change from the older short-rectangle proof.
The moment order used for confidence is called \(u\), so it is
distinct from the passive count \(p\).

Condition on one independently stopped common cavity, deleting a set
\(I\) of \(k\) neurons in the same layer. At an interior layer
the omitted incoming rows and outgoing columns are independent Gaussian
root pairs, independent across \(i\in I\) and independent of the
common cavity. First-layer incoming roots have covariance \(I_d\);
their initial input pairing is time independent. At the top the outgoing
root is absent. Failed own initialization tests define zero reference
paths before any root is integrated.

Consider a forward Gaussian coefficient, or a backward coefficient
divided by \(S\), and subtract its value at its real anchor. On a
complete independently stopped path, extended by (6), the time-derivative
bound and (10) imply the following deterministic normalized coefficient
bounds:

\[
D\le A_0\lambda r_nB_n,\qquad
K\le A_0\lambda B_n,\qquad
H\le128\ell/\lambda,\qquad A_0=\beta^{100L}.
\tag{15}
\]

Here \(D\) bounds the coefficient norm after division by \(\sqrt n\),
\(K\) is its Euclidean parameter Lipschitz constant, and \(H\)
is the rectangle side bound. The factor \(\lambda\) in (15)
is essential. Indeed the backward derivative is bounded by
\(J_*B_n\rho/S\), and \(Y/S=\lambda/16\); the forward
derivative has \(\rho S\), so \(YS=\lambda S^2/16\).
The bounded retraction and anchor Lipschitz constants are covered by
\(A_0\). This is a bound on complete paths, not a conditioning on
full-network survival.

One may use the larger deterministic radius

\[
\overline D=\frac{A_0}{B}
\frac{\lambda B_n}{(1+\lambda B_n)\sqrt{q_n}}
\tag{16}
\]

in place of \(D\), even when the first member of the minimum in
(4) is smaller. The Gaussian rectangle lemma, including its sample-RMS
version, then gives for a correction supremum \(X\)

\[
\log\mathbb E(e^{aX}\mid\text{cavity})
\le a(M+2\overline D)+2a^2\overline D^2,
\quad
M=256\overline D\sqrt{\log(e+HK/\overline D)}.
\tag{17}
\]

No independence of the samples is required. This is the lemma proved
in the current source module: dyadic rectangle meshes give the mean,
and the Gaussian Lipschitz inequality gives the centered exponential
moment.

Here its entropy is bounded uniformly in the gap and in width. By
\(B_n\le1+q_n\),

\[
\log(e+HK/\overline D)
\le\log B+16q_n+\log(1/\lambda).
\tag{18}
\]

For verification, direct substitution gives
\(HK/\overline D\le128B\ell(1+\lambda B_n)
\sqrt{q_n}/\lambda\). Taking its logarithm, use
\(\log\ell\le q_n\),
\(\log(1+\lambda B_n)\le\log(2+q_n)\le2q_n\),
and \(\log q_n\le q_n\); the numerical terms fit inside the
remaining \(q_n\) allowance.

Put \(x=\log(1/\lambda)\). For every \(b\ge1\),

\[
\min(1,be^{-x})\sqrt{x}\le\sqrt{\log b}+1.
\tag{19}
\]

If \(x\le\log b\), this is immediate. Otherwise write
\(x=\log b+s\) and use
\(e^{-s}\sqrt{\log b+s}\le\sqrt{\log b}+e^{-s}\sqrt s\),
whose last term is below one. Apply (19) with \(b=B_n\).
Since \(\log B_n\le\log(1+q_n)\le q_n\), it follows that

\[
\overline D\sqrt{\log(1/\lambda)}\le2A_0/B.
\]

Equations (16)–(18) now give

\[
M+2\overline D
\le\frac{A_0}{B}
\{256(\sqrt{\log B}+6)+2\}
\le\beta^{-190L}.
\tag{20}
\]

The last numerical inequality uses \(\sqrt{300L\log\beta}
\le\beta^{2L}\), \(\beta\ge10\), \(L\ge2\), with ample
slack. Consequently

\[
\mathbb E(e^{aX}\mid\text{cavity})
\le\exp(\beta^{-180L}),\qquad 0\le a\le8.
\tag{21}
\]

Unlike the old finite-moment bound, this assertion requests only a
fixed exponent. That suffices once the complete reference is formed
on the common cavity before taking a product over distinct roots.

In detail, let \(A_i\) be
\(\exp\{\eta_*C_{\rm abs}(1+\text{four real references}
+\text{four complex-minus-real corrections})\}\), where the
four entries are forward and scaled backward scalar suprema and their
training-sample RMS counterparts. Each \(A_i\) is a function only
of the common cavity and root pair \(i\). Cauchy–Schwarz between
its real and complex parts gives

\[
\mathbb E(A_i^2\mid\text{cavity})<3.
\tag{22}
\]

Indeed the real factor has moment below four at exponent
\(4\eta_*\), by `cp:src-main-moment`. Hölder within the four
complex entries only asks (21) at exponent
\(16\eta_*C_{\rm abs}\le16/(1024W_G)<8\). Its contribution
is less than \(e^{\beta^{-180L}/2}\). Thus (22) follows from
\(2e^{\beta^{-180L}/2}<3\). Conditional root independence gives

\[
\mathbb E\prod_{i\in I}A_i^2\le3^k.
\tag{23}
\]

There is no Hölder exponent \(k\) in (21)–(23). Within-root
real and complex parts need not be independent.

The only remaining order-dependent moment belongs to the projected
singleton-to-common-cavity differences. Extend each cavity by its own
retraction before subtraction, and project the whole difference onto
the Euclidean ball of radius \(4n^{1/100}\). Both coefficient
paths omit the particular paired root. Projection preserves that
independence and agrees with the actual difference on the successful
local prefix. Its normalized Gaussian radius is
\(v_n=4n^{-49/100}\). With the explicit local derivative bounds
in Section 5, the rectangle lemma gives each primitive projected
correction \(E_i^{(j)}\) the bound

\[
\log\mathbb E e^{aE_i^{(j)}}\le a\mu_n+2a^2v_n^2,
\quad
\mu_n\le256v_n\sqrt{\log(e+\beta^{400L}
(1+\lambda^{-1})\ell^4/v_n)}+2v_n.
\tag{24}
\]

The primitive sample-RMS corrections satisfy the same expression.
No mutual independence of these differences is asserted.

On the local event, the scalar absorption inequality expresses each
actual weight \(B_i^{\rm wt}=\exp\{\eta_*(Z_{a,i}+K_{a,i}/S)\}\)
as at most \(A_i\) times the exponential of four such projected
corrections, with coefficient \(\eta_*C_{\rm abs}<1\), and the
deterministic remainder \(n^{-1/40}\). Cauchy–Schwarz between
the \(A_i\) product and this error product, followed by Hölder
over the at most \(4k\) primitive error factors, therefore implies

\[
\mathbb E\left[1_E\prod_{i\in I}B_i^{\rm wt}\right]
\le 3^{k/2}
\exp\{k n^{-1/40}+4k\mu_n+64k^2v_n^2\}
\le16^k
\tag{25}
\]

provided \(u\mu_n+u^2v_n^2\le10^{-3}\) and \(k\le u\).
The indicator is dropped only after the pathwise reference bound.
Equations (23) and (25) are the point that removes confidence shrinkage
from the radius. Applying order-\(u\) Hölder to complex corrections
*before* putting them on the common cavity would miss this independence.

## 5. Finite passive-panel transfer and the explicit local interface

The following is the proposed finite-source composition of the preceding
lemmas with the explicit local estimates. It records all new interface
uses instead of inferring them from an old PASS verdict. For
\(0<\delta<1/4\), define

\[
u=\max\left\{1,\left\lceil
\frac{\log(4emL/\delta)}{\log(64e^2)}\right\rceil\right\},
\quad
\mathcal A=\beta^{4000L}(1+\lambda^{-1})^8
(N+d+u+1)^8,
\]

\[
n\ge N_{\rm src}(\delta):=
\left\lceil(\mathcal A/\delta)^{40000}\right\rceil.
\tag{26}
\]

This is a polynomial of fixed numerical degree. Its enormous exponent
is not an efficiency claim. The input list is fixed before the Gaussian
draw, but (26) displays its finite size. The common-cavity deletion count
is \(u\), not \(N\) and not the passive count.

### Initialization and labels

The complete proof in `EXPLICIT_FITTING_WIDTH.md`, Sections 1–5, applies
without \(m\ge d\), as its proof and explicit statement of that
fact explain. Its width is at most

\[
\beta^{32L}(1+\lambda^{-1})^2
\left[dL\log\beta+\log\frac{16L(m+1)^2}{\delta/64}\right].
\tag{27}
\]

Formula (26) exceeds (27). Its required fitting label cap
\(Y\le\lambda/(8H\sqrt F)\) follows from the current one:
the displayed fitting recurrences give \(H\le\beta^{2L}\),
\(F\le\beta^{10L}\), so \(8H\sqrt F\le\beta^{8L}
\le\beta^{30L}\). There is no additional label restriction.

The all-deletion initialization argument in
`FULL_FINITE_SOURCE_PROBABILITY.md`, Section 2, depends on the evaluated
input only through its unit norm. Replacing its initial maximum union
by the \(N\) declared inputs gives
\(Z_0\le2H\sqrt{2\log(64nNL/\delta)}\).
Deleting at most \(u\) neurons changes every subsequent initialized
feature vector by at most
\((8s)^L\sqrt u(b+sZ_0)\). The training singular-value margin is
therefore transferred to every cavity before any union over cavity Gram
laws. The fresh-row coordinate tail is

\[
2\exp\left\{-\frac{n^{4/5}}
{2(8s)^{2L}u(b+sZ_0)^2}\right\}.
\tag{28}
\]

Its union has at most \(uLn^u\cdot NLn\) tests. Formula (26)
pays this union and the initial training-budget, row/column norm, and
fitting failures with total probability below \(\delta/4\).
Only training inputs have exponential budgets. Passive size caps can be
\(2(64H_{\max}+16)\sqrt\ell\) for the full path and doubled
for a cavity. Initially the fresh-row Gaussian bound is smaller by a
strict constant margin.

### What changes in the local maps

Use \(\bar u=(\Theta-\Theta_0)/S\), scale backward fields and
reverse ports by \(S\), and leave forward fields unscaled. Then
\(\|y/S\|_2/\sqrt m=\lambda/16\). The exact retained equation is

\[
\dot{\bar u}=-\frac2m\sum_a\bar r_a
\left[\nabla_{\bar u}\bar F_a+
D_{\bar u}h_a^{(j-1)\top}\bar q_a\right],
\quad \bar F_a=F_a/S,
\tag{29}
\]

with the entire omitted top prediction offset included in \(\bar r_a\).
Because \(w(0)=0\),
\(\bar F_a=\bar u_w^\top h_a^{(L)}\); no derivative coefficient
in (29) has an inverse \(S\). The exact normalized local
remainders are already present in `compact_foundations.tex`, including
its passive-observable calculation.

For clarity, the finite-panel extension of the augmented response
calculation is explicit. For evaluated input \(b\le N\) and
training driver \(a\le m\), let

\[
\bar R_{ba}^{(j)}=S^{-1}D_\Theta z_b^{(j)}\nabla_\Theta F_a,
\qquad \bar Q_{ba}^{(j)}=\phi_j'(z_b^{(j)})\odot\bar R_{ba}^{(j)}.
\]

Differentiation of the forward pass gives

\[
\bar R_{ba}^{(1)}=\bar\delta_a^{(1)}v_a^\top v_b,
\qquad
\bar R_{ba}^{(j)}=
\bar\delta_a^{(j)}\frac{h_a^{(j-1)\top}h_b^{(j-1)}}n
+W^{(j)}\bar Q_{ba}^{(j-1)}.
\tag{30}
\]

There is no residual, label, or passive backward field attached to
the evaluated index \(b\) in (30). An omitted layer contributes
the upper port \(\sum_{i\in I}x_i\bar Q_{ba,i}^{(j)}\).
Below that layer there is the direct reverse observable
\(C_b C_a^\top\bar q_a\), with
\(C_b=D_\Theta h_b^{(j-1)}\). Its reference maps include the
forward images at every declared input of \(C_a^{0\top}y_i\).
This direct observable and this probe family must both be included.

Their nonlinear estimates are the exact product subtractions

\[
(C_b^1C_a^{1\top}-C_b^0C_a^{0\top})y_i
=(C_b^1-C_b^0)C_a^{0\top}y_i
+C_b^1(C_a^1-C_a^0)^\top y_i,
\tag{31}
\]

and, writing \(c_{ab}=h_a^\top h_b/n\),

\[
|c_{ab,[1]}|\le\beta^{10L}(N_0+u_0)/\sqrt n,
\qquad
|E_{c_{ab}}|\le\beta^{40L}
\left[(R+P)/\sqrt n+(N_0+u_0)^2/n\right],
\tag{32}
\]

where \(N_0\) bounds the Gaussian linear variation,
\(u_0\) its nonlinear remainder,
\(d_0\) the linear coordinate maximum,
\(R=d_0N_0+d_0u_0+u_0^2\), and
\(P=(N_0+u_0)^2/\sqrt n\). These local symbols do not denote
the panel size \(N\).

The first term of (31) is at most
\(\beta^{50L}(d_0+n^{-1/2})(N_0+u_0)\): in its directional
forward recursion, changed gates multiply the Gaussian probe's
reference coordinate bound \(d_0\), while changed-matrix products
retain \(n^{-1/2}\). The second term uses the lower adjoint-probe
bound and \(\|C_b^1\|\le\beta^{10L}\). Summing the reverse
controls bounds (31) by

\[
\beta^{70L}(1+u)(1+M)(d_0+n^{-1/2})
[N_0+u_0+(N_0+u_0)^2],
\tag{33}
\]

where \(M\) is the common provisional preactivation/scaled-carrier
cap. Missing feature products cost \(u(b+sM)^2/n\); learned
response ports cost \(n^{-1/2}\) times the listed amplitudes.
The gate product remainder is

\[
E_{\bar Q}=g_1E_{\bar R}
+(g_1-g_0)\bar R_{[1]}
+\bar R_0[g_1-g_0-\phi''(z_0)z_{[1]}],
\quad g_i=\phi'(z_i).
\tag{34}
\]

Only the additive last term uses a reference response cap. Homogeneous
propagation costs \(10s\), independently of the cutoff and depth.
Thus passive inputs add more copies of the already bounded maps, not
an additional cutoff factor per layer. This is the exact point where
an undifferentiated appeal to a training-only statement would fail.

The explicit map recurrences (4)–(20) of
`INSERTION_MAP_MODULI.md` can now be used with contour coefficient
\(T_0=64/\lambda\). Their inputs are the same operator, activity,
raw coordinate and propagator bounds. The recurrence for an evaluated
forward field uses its \(v_b\), whose norm is still one. Add
(30)'s differentiated terms, (31)'s probes and the response ports;
their coefficients are bounded by

\[
\beta^{100L}(1+M_0+4U_{\rm fin})^2(1+C_0)^2
\le\beta^{1000L}(1+\lambda^{-1})^2,
\tag{35}
\]

where \(M_0\le\beta^{80L}\) bounds the raw amplitudes after
removing \(\ell\), and \(C_0\le\beta^{300L}
(1+\lambda^{-1})\) is the maximum coefficient of those explicit
map recurrences. The passive provisional cap above is below
\(\beta^{80L}\ell\), so it does not increase \(M_0\).
The exponent count in (35) is at most
\(100L+160L+600L\), with the remaining \(140L\) covering
numerical factors and finite geometric layer sums. The doubled contour
coefficient is covered by that slack.

The augmented map bound is (35) times
\(\sqrt u\,n^{1/4000}\ell^5\); its control modulus uses at
most \(\ell^4\), and its terminal derivative at most
\(\sqrt n\ell^8\). A time derivative of (30) has one potentially
large gate product \(\phi''\dot z_b\bar R_{ba}\). Its
stopped coordinate response cap times the RMS \(\dot z_b\)
bound gives an RMS estimate with no \(\sqrt n\); conversion
to a scalar control introduces that factor once. Every other term is
a changed mixer, changed feature pairing, changed training response,
or a propagated lower response. The derivative recurrences therefore
introduce no width power depending on depth. Equations (31)–(34)
also show that the augmented nonlinear remainder has cutoff degree at
most three, as in the finite training-source proof.

There are at most \(4u(N+1)^2\) real scalar control components.
Their amplitudes are a coefficient times \(\ell\), and speeds a
coefficient times \(\sqrt n\ell^3\). This replaces the original
\(4u(m+1)^2\) count; it does not insert \(N\) in an optimizer
or in a sample average. The normalized residual-Hessian and scalar
trace estimates still average only over the \(m\) drivers.

### Finite mesh and first-exit estimates

The numerical width (26) implies

\[
\mathcal A\ell^{16}\le n^{1/1000}.
\tag{36}
\]

To verify it, put \(v=\log(\mathcal A/\delta)\). At
\(\log n=40000v\), the logarithm of the left side is at most
\(v+16\log(1+40000v)\le17v<40v\). The middle inequality
holds at the smallest possible \(v\ge8000\log10\), and its
derivative verifies it thereafter. The derivative of
\(\log n/1000-16\log(1+\log n)\) is positive in this range.
This proves (36) at every larger individual width.

By (35)–(36), every enlarged linear map and centered quadratic map
has operator norm at most \(n^{1/200}\), and Gaussian input
dimension at most \(2un\). Linear coordinate and quadratic-form
tails at threshold \(n^{-1/10}/8\) are at most
\(4e^{-n^{0.78}}\). The Euclidean map mean is at most
\(\sqrt{2u}\,n^{1/200}<n^{1/100}/2\); its remaining tail is
smaller. These inequalities follow from the Gaussian square moment
formula and \(\|R\|_{\rm HS}\le\sqrt{2un}\|R\|\), rather
than an independence assertion for adaptive controls.

A control net at accuracy \(n^{-1/8}\) has log cardinality at
most \(\mathcal A\ell^8 n^{5/8}\le n^{0.627}\).
The centered quadratic interpolation error includes its trace term
\(2u\|\Delta R\|\); it is bounded by
\(10u\|\Delta R\|\) on the root-norm event. A terminal mesh
of spacing \(n^{-2}/(1+\mathcal A\ell^8)\) on the bounding
rectangle has at most \(n^6\) points. Retraction of this grid
onto a domain prefix changes its distance bound by at most \(9/8\).
For actual analytic controls, integrate the displayed derivative
bound along the image of a straight segment under that retraction.
This handles off-grid points without assuming the domain is convex.
For the Gaussian union at each grid point, controls are deterministic
histories only on its canonical one-dimensional contour. No arbitrary
two-dimensional control field is analytically continued.

The number of coordinate, probe and pairing tests is at most
\(\mathcal A n^3\), and the deletion union costs
\(\log(uL)+u\log n\). Formula (36) bounds the total logarithmic
union cost below \(n^{0.65}\). The enlarged local Gaussian event
therefore fails with probability at most

\[
e^{-n^{0.7}}<\delta/16.
\tag{37}
\]

Substitute the actual controls only after this event has been formed.
For the normalized nonlinear remainder use
\(N_0=n^{1/100}\), \(d_0=n^{-1/10}\),
\(u_0=n^{-1/25}\). The exact retained vector-field remainder,
learned ports, full top offset, and (33)–(34), integrated with the
factor-two base propagator, give the common enclosing bound

\[
\mathcal A\ell^8 n^{1/4000}
[n^{-8/100}+u_0^2+n^{-48/100}+n^{-1/2}]
<\tfrac12n^{-1/25}.
\tag{38}
\]

Here the residual-weighted terms use
\(2\int\rho/S\le1\), and the other terms use contour length
\(64\ell/\lambda\). Inequality (36) leaves a largest power
\(n^{-0.07875}\), strictly smaller than the requested
\(n^{-0.04}/2\) at (26). The same calculation verifies the
joining-strip gate
\(d_0+\beta^{10L}u_0+\beta^{30L}(R+P)<a/32\).
Continuity therefore gives coordinate discrepancies at most
\(n^{-1/30}\) for retained preactivations, scaled carriers and
all \(mN\) responses, and Euclidean discrepancies at most
\(2n^{1/100}\). This is the local input used by (24).

Cavity budgets satisfy
\(\mathcal H_a^{-I}\le e^{2\eta_*n^{-1/30}}
\mathcal H_a+u/n<2\mathcal B\) whenever
\(\mathcal H_a\le\mathcal B\). The same coordinate comparison
transfers the doubled maxima and response caps, and the strict pole
gap. Operator and activity margins were verified in Section 2.
Thus independently stopped cavities cannot stop before the full path
on its successful local prefix.

The singleton trace expansion of the current source proof has the
same four nonzero contractions. The finite errors are at most
\(n^{-1/40}\), by (38); the adaptive-residual rank-one trace is
at most \(\mathcal A\ell^8 n^{-1+1/4000}\). Its scalar
absorption coefficient is the unchanged \(C_{\rm abs}\),
independent of \(u\) and \(N\). A Gaussian time grid therefore
improves the training maxima to \(K_{\rm src}\sqrt\ell\)
and \(SK_{\rm src}\sqrt\ell\), with failure at most
\(n^{-100}\).

For (30) the four deterministic response contributions are, after
division by \(S\),
\(sK_{\rm src}H_{j-1}^2\),
\(sK_{\rm src}f_{j-1}^2\),
\(sK_{\rm src}ST_Q\), and
\(sK_{\rm src}S^2H_{j-1}q_{j-1}^*\).
The centered row term has RMS coefficient \(q_{j-1}^*\).
These are the recurrence for \(U_j(64)\); the evaluated index
only changes how many of these tests are made. A union over
\(mNLn\) tests and the time grid is paid at (26), and improves
every response cap, with another failure at most \(n^{-100}\).
Then the exact identity
\(\dot z_b^{(j)}=-(2/m)\sum_a r_aR_{ba}^{(j)}\)
improves both the poles and passive size caps. The real displacement
is at most \(2S^2U_{\rm fin}\sqrt\ell\), which is at most
\(2\sqrt\ell\) by (2); the complex displacement was bounded
in Section 2. No passive exponential budget has been introduced.

The modulus of the projected singleton/common-cavity difference in
(24) is at most
\(\beta^{300L}(1+\lambda)\ell^3\); the common bounding
rectangle only changes its side coefficient to \(128/\lambda\).
The numerical factors fit the \(\beta^{400L}\) envelope in
(24). Inequality (36) bounds its entropy by a numerical multiple of
\(\ell\); at (26),
\(1500\sqrt\ell\le n^{1/100}\), so
\(\mu_n\le n^{-48/100}\).
Also \(u\le\mathcal A^{1/8}\le n^{1/8000}\).
Thus \(u\mu_n+u^2v_n^2<10^{-3}\), the finite premise of (25).

Finally \(2\eta_*K_{\rm src}\le33/4096<1/100\), directly
from the displayed \(C_G,W_G,\eta_*\) recurrences. On the
maximum event, repeated weights in a moment obey
\(B_i^{\rm wt}\le e^{\sqrt\ell/100}\le e^{1/100}n^{1/100}\).
The finite collision lemma gives

\[
\mathbb E\left[1_E\left(n^{-1}\sum_iB_i^{\rm wt}\right)^u\right]
\le e16^u\quad(n\ge4u^3).
\]

For reference, group an ordered \(u\)-tuple by its \(k\)
distinct indices, bound its repeats by the maximum, and use (25)
for its distinct product. A partition with \(u-k=j\) identifications
can be encoded by \(j\) edges joining each block's least element
to its other elements. There are at most
\(\binom{u}{2}^j/j!\) choices. Summing gives the factor
\(\exp\{\binom{u}{2}e^{1/100}n^{1/100}/(16n)\}\le e\).
Hence the budget failure is at most
\(emL(16L/\mathcal B)^u\le\delta/4\).
Together with initialization, (37), and the two maximum events, total
failure is less than \(\delta\).

All stops therefore have strict improving margins. Local holomorphic
ODE solutions glue on the vertically fibered, simply connected domain
(6) and continue past its compact boundary. The resulting four source
families have the paper's RMS and coordinate bounds on the disks of
Section 3: forward families on all \(N\) inputs, backward families
only on training inputs. This is the proposed polynomial-probability
source transfer; it does not assert a whole-sphere complex source.

## 6. Accuracy, initialization-only provenance, and retained state

The finite-panel source proof needs no time rectangle of radius
\(1/(\lambda\sqrt\ell)\). For its initialization-only compiler,
the disks just constructed cover the real interval strictly, so compactness
gives some positive closed rectangle inside their open union. The existing
origin-jet compiler then applies. It is an existence statement with no
preprocessing complexity claim; changing that auxiliary rectangle does
not add retained coordinates.

Let \(C_{\rm sel}\ge1\) be a constant in the paper's selected
comparison estimate, depending only on activations and depth. The explicit
selected coefficient ledger permits \(C_{\rm sel}=\beta^{60L}\):
with \(X=\beta^L\), it gives \(F\le X^6\),
\(K_1\le X^{18}\), \(H_C\le2X^3\),
\(F_c\le X^{15}\), and
\(\mathcal B_n/z\le X^{22}(1+\sqrt\ell)\),
where \(z=Y/\lambda\). Substitute these in
`cp:selected-coefficients`, use \(e^v-1\le ve^v\) and
\(\mathcal B_n\le1+\sqrt\ell\). For the tail, its explicit
\(B_w,B_f\) formulas give
\(\mathcal D\le X^{30}z(1+\lambda^{-1/2})\).
Both estimates are below the stated \(X^{60}\) envelope.

Choose exactly the current source tolerance

\[
\epsilon_{\rm src}=\min\left\{1,Y,16Y/\lambda,
\frac{\lambda}{2C_{\rm sel}n(1+\lambda^{-1/2})
(1+\sqrt\ell)e^{\sqrt\ell}}\right\}.
\tag{39}
\]

The finite-horizon error is at most \(Y/(2n)\). The tail is at
most \(C_{\rm sel}(Y/\lambda)(1+\lambda^{-1/2})e^{-8\ell}\),
so the additional, label-independent gate

\[
n^7\ge2C_{\rm sel}\lambda^{-1}(1+\lambda^{-1/2})
\tag{40}
\]

suffices for complete-trajectory error \(Y/n\), including the
fitted endpoint. This follows by dividing the tail by \(Y/(2n)\)
and using \(ne^{-8\ell}\le n^{-7}\).

Put \(M_n=\beta^{6L}\sqrt n\) and
\(K=\max\{0,\lceil\log_2(8M_n/\epsilon_{\rm src})\rceil\}\).
The paper's coefficient argument yields source rank

\[
R=2m+k+1+2(2m+p)J(K+1),\qquad
k=\dim\operatorname{span}\{v_1,\ldots,v_N\}\le\min(d,N).
\tag{41}
\]

The input reduction uses an orthonormal basis of that declared span;
Gaussian rows projected onto it stay standard Gaussian, all input
inner products are preserved, and the first-layer velocity lies in
that span. Thus it exactly preserves the coupled panel trajectory.
Neither passive labels nor later trained weights are used.

Taylor coefficients on each disk have magnitude at most \(M_n\).
On its half-radius panel, the tail is at most
\(M_n2^{-K}\le\epsilon_{\rm src}/8\). Approximate each base
coefficient in Euclidean norm to \(\epsilon_{\rm src}/128\)
using origin jets and form its initialized image exactly. Summing
the geometric coefficient errors gives base error at most
\(\epsilon_{\rm src}/64\); initialized operator norm eight
gives image error at most \(\epsilon_{\rm src}/8\).
The source contract is therefore met, with exact paired images.

Before a simplified display, (14), (39) and (41) are the actual
rank and accuracy accounting. An explicit sufficient simplification
gate is

\[
n\ge
\left[32\beta^{6L}(1+C_{\rm sel})\lambda^{-3/2}
(1+Y^{-1})\right]^4.
\tag{42}
\]

Together with (26), it implies \(K+1\le8\ell\).
Indeed the logarithm defining \(K\) is at most
\(\tfrac32\log n+\sqrt\ell+\log(1+\sqrt\ell)\)
plus the logarithm of the bracket in (42). The latter is at most
\(\tfrac14\log n\); (26) gives \(\ell\ge16\), so the
two intervening terms are at most \(\ell/4\) each. Dividing by
\(\log2\), adding the two ceiling units, stays below \(8\ell\).
The elementary branches \(\epsilon_{\rm src}=Y\) and
\(\epsilon_{\rm src}=1\) are bounded by the same expression.
This is a polynomial inverse-label gate for the **simplified storage
display**, not a probability gate. At smaller \(Y\), retaining
the exact \(K\) adds its explicit \(\log(1/Y)\) cost.

Squaring (41), using (14) and \(k\le N\), now gives exactly
the target powers

\[
R^2\le C N^2\left[
\left(\frac Y\lambda\right)^4\ell^3
+\lambda^{-2}\ell^2\{\log(e+\ell)\}^2\right].
\tag{43}
\]

The retained inventory is the same
\(1020(L+1)R^2+36R+10m(k+1)+pk+N+3Nd\)
as in the paper. Hence (43) gives

\[
C(m+p)^2\left[
\left(\frac{Ym}{\gamma}\right)^4\log(en)^3
+\left(\frac m\gamma\right)^2\log(en)^2
\log(e+\log(en))^2\right]+C(m+p)d.
\tag{44}
\]

All constants in (43)–(44) depend only on activation bounds and depth.
The confidence moment \(u\) occurs only in (26), never in (4),
(14), (39), (41), or (44). Dense arrays, jets, Taylor coefficients,
anchors and the partition are discarded after initialization, as in
the current method. Nonprimitive activation-evaluator storage remains
separately charged.

The complete relative-error theorem still needs a quantitative lower
event for actual independent dense-run variability. This note does not
derive that separate event or replace it by a dense upper bound.
Conditional on a lower event
\(\|f_n-\widetilde f_n\|\ge cY\sqrt\gamma/
(\sqrt n\ell^{5/2})\), the Taylor ratio is at most
\(\ell^{5/2}/(c\sqrt{\gamma n})\). Any width needed for that
event or for a requested ratio tolerance must be accounted separately.

## 7. Audit boundary and inputs

The cap and Gaussian moment calculations in Sections 2–4 are complete
deterministic/conditional proofs. Section 5 is an author-level quantitative
transfer of the explicit finite training-source local estimates to the
passive panel and capped flaring domain. Its central finite interfaces
are (28), (30)–(38), including the actual contour and endpoint meshes;
they are written out for a fresh reviewer. No fresh independent verdict
has yet been obtained for that transfer. A reviewer should not infer it
from the older finite-rectangle check.

The materially new points to test are: conditional independence of each
complete common-cavity complex reference in (23); independence of the
projected singleton/common difference from its particular paired root;
the passive response port and direct reverse observable (30)–(34);
the one-dimensional control net plus retracted terminal grid on the
flaring domain; and the uniform raw-coefficient ledger (35)–(38).
Failure of one of those interfaces would leave Sections 2–4 intact
but would make the polynomial source-probability assertion conditional.

Complete relevant source proofs read: the current source module
`paper/compact_foundations.tex`; the selected-metric, selected-runtime,
origin-jet and finite-panel sections of `paper/compact_selected.tex`;
`FULL_FINITE_SOURCE_PROBABILITY.md` and its check,
`FINITE_COMPLEX_MOMENT_GATE.md`, `INSERTION_MAP_MODULI.md`,
`QUANTITATIVE_INSERTION_WIDTH.md`, and `EXPLICIT_FITTING_WIDTH.md`
in the authorized unseen-query study. The current compact setup and
the maintained book's index and notation contract were also read.
The older deterministic radius repair was used only as motivation;
its short-rectangle radius is not substituted into the current Taylor
count. No linked unauthorized scientific input or other route output
was used. Required canonical/neural and rigorous-math instructions
were applied. Only this assigned file was written.
