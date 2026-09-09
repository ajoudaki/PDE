# Affine source certificate with time and sample normalization

2026-09-07. Independent bounded calculation for the proposed power-ten
improvement. The rigorous-math skill and the three assigned quantitative
files were read, together with the source representation and Gaussian-probe
sections of `two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md`
and the affine active/inactive proof in `AFFINE_CORE.md`. No experiment,
delegation, old-file edit, or commit was performed.

The following is an affine input certificate, not a nonlinear response or
complete population theorem. In particular the coupled inverse below is
proved using positive beta scaling, not identified with a raw variational
propagator.

## 1. Certificate sufficient for the original-time power-ten route

Let

\[
 r=\sqrt{(1+\tau\rho)/2},\quad \lambda=a^3r,\quad
 m=\left({3\over\sqrt2\lambda}\right)^{1/4},\quad
 M=24^{1/4}\delta^{-1/8}.
\]

Then $1<m\le M$, and **$r\asymp m^{-4}$** uniformly for

$1/2\le a\le1$. It is not true in general that $r\asymp M^{-4}$:

$M$ is a uniform dataset envelope. This distinction is necessary when
simplifying the powers below.

All norms in the next table use the original feature-time steps $h_j$.
A subscript $d$ means strict density, and $r$ means causal time-row
norm, with a fixed absolute sample matrix norm. The coefficients and
derivative-only maps are those of the assigned response lemma. There is
an absolute constant $C$, uniform in data, gain, sufficiently fine mesh,
and in the enlarged beta initialization below, such that the following
bounds hold in the actual endpoint scale $m$:

| Array | Bound proved here | Weaker bound requested by the power-ten route |
|---|---:|---:|
| $A_2,F$ strict density | $C$ | $Cm^5$ |
| $A_3,V$ strict density | $C$ | $Cm^7$ |
| $B_3,T$ row norm | $Cm^9$ | $Cm^9$ |
| $B_2,W$ row norm | $Cm^{11}$ | $Cm^{11}$ |
| $R_1,R,L,R_3$ row norm | $Cm^7$ | $Cm^{11}$ |
| $U=R_3A_3$ strict density | $Cm$ | $Cm^9$ |
| $FL,RF,RFL$ strict density | $Cm$ | $Cm^9$ |

The bounds on $U,R_1,L_3$ use the elementary extensions of the same
finite-program Gaussian-probe identity described in Section 5. The
bound on $R_3$ uses an existing matrix-answer probe. The current
backward diagonal is zero for the affine
reference, but arbitrary current diagonal forcing is retained in the
coupled inverse argument.

The numerical constants in the old certificate $B_\delta=C_B\delta^{-2}$
need not be weakened by this calculation. Its answer-perturbation costs
at most $3b$, and its four coefficient-output Lipschitz costs at most
$2b$, concern $H^1,H^2,\delta^3,\delta^2$. They do not assert an
$O(b)$ Lipschitz bound on $q^1=A^*B^*D$, which has cost $O(b^2)$.
Likewise a primary parameter bound $b=O(m)$ does not mean that every
backward field is $O(m)$: $q^2=O(m^2)$, $q^1=O(m^3)$. The source
input table already allows those larger fields.

## 2. Exact normalization of both sample sectors

Fold the labels, so the controls are ((1/2,1/2)). Work in the
mean/contrast basis

\[
 Q={1\over2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
 Q^{-1}=2Q,\qquad S_0=\operatorname{diag}(r,r_-),\quad
 r_-=\sqrt{1-r^2}.
\]

Both diagonal entries of $S_0$ are positive under the angle hypothesis.
Use $t=\lambda s$, with mesh steps $\Delta t_j=\lambda h_j$, and
denote its strict integration matrix by $H$:

\[
 H_{kj}=\Delta t_j I_2\quad(j<k).
\]

For fields, define

\[
 Qz^\ell=a^{\ell-1}S_0x_\ell,\qquad
 Qh^\ell=a^\ell S_0\widehat h_\ell,\qquad
 Q\delta^\ell=a^{4-\ell}rS_0^{-1}d_\ell.
\tag{1}
\]

In the affine case $\widehat h_\ell=x_\ell$, and, with $D=C$ after
folding,

\[
 x_1=(p,p_-),\quad x_2=(Ap,A_0p_-),\quad
 x_3=(BAp,B_0A_0p_-),
\]
\[
 d_3=(D,0),\quad d_2=(B^*D,0),\quad
 d_1=(A^*B^*D,0).
\tag{2}
\]

The frozen inactive identities are the canonical Gaussian identities
proved in `AFFINE_CORE.md`, not a claim that arbitrary bounded actions
preserve independence. In particular all inactive normalized forward
standard deviations at beta one are one. At beta initialization they
are respectively $\beta,\beta^2,\beta^3$.

These transformations also normalize the full, possibly nonlinear,
raw updates exactly:

\[
 x_1'=d_1,\qquad
 A'=\sum_{i=+,-}d_{2,i}\otimes\widehat h_{1,i},\qquad
 B'=\sum_{i=+,-}d_{3,i}\otimes\widehat h_{2,i},\qquad
 D'=\widehat h_{3,+},
\tag{3}
\]

where prime denotes normalized time. For example

$Q R_xQ^{-1}/2=S_0^2$, so the first raw update divided by its field
scale becomes $S_0^{-1}S_0^2a^3rS_0^{-1}/\lambda=I$.
For the second matrix update, each sample-sector factor contributes

$(a^2r/s_i)(as_i)/\lambda=1$. The third matrix has the same
factor. The readout update gives $a^3r/\lambda=1$.

This verifies that the sample normalization changes neither the raw
metric nor the algorithm. It is merely a re-expression of its equations.
The actual affine state on the active four-component space obeys

\[
 p'=A^*B^*D,\quad A'=B^*D\otimes p,\quad
 B'=D\otimes Ap,\quad D'=BAp.
\tag{4}
\]

## 3. Exact normalized source arrays

In this section write $A_2,A_3,B_3,B_2$ for the source arrays after
the fixed $Q\cdot Q^{-1}$ sample change of basis. Define

\[
 \widehat A_2=arS_0^{-1}A_2S_0^{-1},\qquad
 \widehat A_3={r\over a}S_0^{-1}A_3S_0^{-1},
\]
\[
 \widehat B_3={a\over r}S_0B_3S_0,\qquad
 \widehat B_2={1\over ar}S_0B_2S_0.
\tag{5}
\]

For example $z^2=\xi^2+A_2\delta^2$, after $1$, gives

$x_2=\widehat\xi^2+\widehat A_2d_2$. Transforming the formal
derivative $\partial h^1/\partial\zeta^1$ gives the identical
factor in $5$. Therefore neither variance factors nor gain factors are
being hidden in a redefinition of the formal derivatives.

Set $P_+=\operatorname{diag}(1,0)$. The exact transformed maps are

\[
 \widehat F=(I-H\widehat B_2)^{-1}H,
 \quad \widehat R=(I-\widehat A_2\widehat B_3)^{-1},
 \quad \widehat L=(I-\widehat B_3\widehat A_2)^{-1},
\]
\[
 \widehat V=\widehat R\widehat A_2,
 \quad \widehat T=HP_+(I-\widehat A_3HP_+)^{-1},
 \quad \widehat W=\widehat B_3\widehat R.
\tag{6}
\]

All gain factors cancel. The coefficient equations at Gaussian matrix
variance $\beta^2$ are

\[
 \widehat A_2=\beta^2\widehat F+\widehat M_{A2},\quad
 \widehat A_3=\beta^2\widehat V+\widehat M_{A3},\quad
 \widehat B_3=\beta^2\widehat T+\widehat M_{B3},\quad
 \widehat B_2=\beta^2\widehat W+\widehat M_{B2}.
\tag{7}
\]

The four learned-moment entries are exactly

\[
 (\widehat M_{A2})_{kj}=\Delta t_j\,\mathbb E[x_{1,k}x_{1,j}^T],
 \quad
 (\widehat M_{A3})_{kj}=\Delta t_j\,\mathbb E[x_{2,k}x_{2,j}^T],
\]
\[
 (\widehat M_{B3})_{kj}=\Delta t_j\,\mathbb E[d_{3,k}d_{3,j}^T],
 \quad
 (\widehat M_{B2})_{kj}=\Delta t_j\,\mathbb E[d_{2,k}d_{2,j}^T].
\tag{8}
\]

To check the sample factor, the original learned matrix is

$(h_j/2)\mathbb E[H_kH_j^T]$. Its $Q\cdot Q^{-1}$ transform is

$h_j\mathbb E[(QH_k)(QH_j)^T]$, since $Q^{-1}=2Q^T$.
Then $1$ and $5$ give $\Delta t_j$, as displayed.

The normalized Gaussian sources likewise have covariance matrices

$\beta^2\mathbb E[\widehat h\widehat h^T]$ or

$\beta^2\mathbb E[dd^T]$, with no sample condition number. Their
largest affine standard deviation is $O(m^2)$; $d_1=O(m^3)$ is
an output field, not a fresh source covariance input.

All baseline source arrays are diagonal in the sample sectors. Their
inactive entries can be computed exactly:

\[
 \widehat F_-=H,\quad
 \widehat A_{2,-}=2\beta^2H,\quad
 \widehat V_-=2\beta^2H,\quad
 \widehat A_{3,-}=3\beta^4H.
\tag{9}
\]

Every inactive backward array is zero. All four inactive resolvents
are identity. Thus the inactive normalization introduces no large
affine constants even when $r_-\ll r$, or conversely.

## 4. Affine geometry and enlargement

The assigned affine proof supplies, up to its own target time $T<2$,

\[
 \|p\|,\|A\|,\|B\|,\|D\|\le Cm,
 \quad \|Ap\|,\|B^*D\|\le Cm^2,
 \quad \|BAp\|,\|A^*B^*D\|\le Cm^3.
\tag{10}
\]

The normalized raw variational propagator is bounded by

$G\le C m^5$, because the integrated radius-one tube Hessian is

$1404+5\log m$. Its restriction to any later initial time obeys
the same bound. The time-dependent estimate, rather than a constant
Lipschitz estimate $\exp(Cm^2T)$, is essential here.

Let $R_*=\sqrt{200+m^2}$, and take

\[
 \beta_*=1+{1\over10^5R_*^2}.
\tag{11}
\]

The reference exists an additional $1/(1000R_*^2)$ units of normalized
time on a ball of component sizes at most $2R_*$, by the local
polynomial vector-field bound $32R_*^3$. Its added integrated tube
Hessian is bounded by an absolute constant. Homogeneity gives

$\Theta_\beta(t)=\beta\Theta_1(\beta^2t)$, and

$\beta_*^2T-T\le6(\beta_*-1)<1/(1000R_*^2)$.
Consequently the whole same interval $0\le t\le T$ is valid for

$1\le\beta\le\beta_*$, with the same bounds $10$ and

$G\le Cm^5$. Also $(\beta_*-1)^{-1}\le Cm^2$.

Strong affine Euler approximation gives these estimates, enlarged by
an absolute factor, on every sufficiently fine mesh. Each fixed-mesh
finite-program width limit is taken separately; nothing here asserts
uniform probability control over growing transcripts or operator-norm
convergence of trained finite matrices.

## 5. The normalized probe certificate

For this section all densities use $\Delta t_j$, and hats are omitted.
Use the sum norm of the four active raw state components in $4$. A
single error inserted at time $j$ first changes an update with its
factor $\Delta t_j$. Thereafter its state variation is bounded by

$G$ times that initial increment. The following table gives the
injection cost and the relevant output Lipschitz cost. Factors denoted
by $C$ are numerical and independent of $m$.

| Injected normalized answer | Updates affected | Injection cost | Output | Output cost |
|---|---|---:|---|---:|
| $\zeta^1$ in $d_1$ | $p$ | $1$ | $p$ | $1$ |
| $\zeta^2$ in $B^*D$ | $p,A$ | $Cm$ | $Ap$ | $Cm$ |
| $\xi^3$ in $BAp$ | $D$ | $1$ | $D$ | $1$ |
| $\xi^2$ in $Ap$ | $B,D$ | $Cm$ | $B^*D$ | $Cm$ |

For example the second row changes (p') by $A^*e$ and (A') by

$e\otimes p$, each $O(m\|e\|_2)$. The fourth changes (B')
by $D\otimes e$ and (D') by $Be$. These are the normalized
versions of the exact four answer probes already proved in the source.

Insert an independent standard Gaussian field $G_0$ in the population
of the answer/output, with arbitrary deterministic signs at finitely
many source slots. The finite-difference identity of the source proof
converts the deterministic response bounds into signed sums of formal
derivatives. Taking signs of those deterministic expected derivatives
gives the row bound. A single slot gives strict density. This yields

\[
 |F|_d,|T|_d\le CG\le Cm^5,
 \qquad |V|_d,|W|_d\le Cm^2G\le Cm^7.
\tag{12}
\]

The actual coefficients include moments $8$, of respective density
orders $m^2,m^4,m^2,m^4$. Therefore

\[
 |A_2|_d,|B_3|_d\le Cm^5,
 \qquad |A_3|_d,|B_2|_d\le Cm^7.
\tag{13}
\]

Since $T<2$, the same exponents bound their row norms.

For $R$, use the fourth answer probe and observe its $Ap$ output,
rather than $B^*D$. For $L$, use the second probe and observe

$B^*D$, rather than $Ap$. The current direct derivative is identity;
every strict derivative has cost $Cm^2G\Delta t_j$. Hence

\[
 |R|_r,|L|_r\le 1+CTm^2G\le Cm^7.
\tag{14}
\]

For $R_3=(I-A_3HP_+)^{-1}$, use the existing $\xi^3$ probe and
observe $BAp$. Its output Lipschitz cost is $Cm^2$, while its
injection cost is one, so again

\[
 |R_3|_r\le Cm^7.
\tag{15}
\]

For completeness, $R_1=(I-HB_2)^{-1}$ admits the same proof with a
finite affine coordinate-program probe. Add $\varepsilon\alpha_jG_0$
to the first preactivation immediately before using it in the forward
calls, retaining the original integrated first-state variable separately.
Its source equation is $p=\xi^1+Hd_1$, with $d_1=\zeta^1+B_2p$;
therefore its frozen-array forward-source derivative is $R_1$.
The perturbation changes the $A,B,D$ updates with cost $Cm^2$,
and the future $p$ output has cost one, plus its current identity.
Thus

\[
 |R_1|_r\le Cm^7.
\tag{16}
\]

This use of the probe identity does not require a new random-matrix
operation. The independent Gaussian root is inserted into an ordinary
affine coordinate instruction. The same fixed-program conditioning,
finite difference, and independent-root proof applies. Reflection

$(\varepsilon,G_0)\mapsto(-\varepsilon,-G_0)$ makes the original
source covariance and learned-moment parameters even in the amplitude,
so their first variation does not contribute. As in the supplied probe
lemma, no Gaussian covariance square root is differentiated and no
derivative is interchanged with an uncontrolled width limit.

Likewise add $\varepsilon\alpha_jG_0$ to the backward readout answer
used in $d_3$, retaining the integrated $D$ state separately. The
frozen-array derivative of $x_3$ is $U=R_3A_3$. The $p,A,B$
updates each have injection cost $Cm^2$, and the output $BAp$
has cost $Cm^2$. There is no current output injection. Consequently

\[
 |U|_d\le Cm^4G\le Cm^9.
\tag{17}
\]

Only the active sample sector needs the large probe bounds. The exact
inactive formulas $9$ handle all the other baseline entries.

A proposed shortcut from beta positivity alone would be insufficient. Since

$B_3'=2T+T A_3'T+M_{B3}'$, one has

$T A_3'T\le B_3'$, but this alone does not control $A_3TA_3$.
Thus it must **not** be substituted for the actual top probe without
another argument. The proof of $17$ here is the explicit coordinate
probe just given; no unproved beta shortcut is used.

## 6. Beta positivity and actual coupled inverse

Still use normalized time and omit hats. At a fixed affine mesh all
active coefficient entries and learned moments are nonnegative
polynomials in beta. This follows by expanding the normalized ascent
updates into raw Gaussian coordinates: their polynomial coefficients
are nonnegative, and every nonzero Wick pairing has nonnegative variance
weight. The chronological affine source recursions preserve positivity.
This is positivity after Gaussian expectation, not positivity of a
sample of the initialized weights.

Let $C'=(A_2',A_3',B_3',B_2')$ denote the beta derivative at one.
Differentiating $7$, with the normalized mesh held fixed, gives

\[
 (I-J_0)C'=(2F+M_{A2}',2V+M_{A3}',2T+M_{B3}',2W+M_{B2}').
\tag{18}
\]

There is no missing mesh or gain derivative. Scaling all initialized
raw hidden parameters changes the initialized-matrix return variance
to $\beta^2$, and all the normalized integration operators in $6$
are beta independent.

Every active component of the forcing in $18$ is at least

$2\Delta t_j$ at strict times: $F,V,T,W\ge H$ on the active
sector. Also, for any polynomial $f(\beta)=\sum c_k\beta^k$
with $c_k\ge0$,

\[
 f'(1)\le{f(\beta_*)-f(1)\over\beta_*-1}
 \le {f(\beta_*)\over\beta_*-1}.
\tag{19}
\]

Combining $11$--$13$ yields

\[
 |A_2'|_d,|B_3'|_r\le Cm^7,\qquad
 |A_3'|_d,|B_2'|_r\le Cm^9.
\tag{20}
\]

The finite causal inverse $ (I-J_0)^{-1}$ is entrywise nonnegative.
For active forward forcing of density at most $q$, with zero backward
forcing, compare its absolute value entrywise to $q/2$ times the
forcing in $18$. This proves

\[
 \|(I-J_0)^{-1}(E_2,E_3,0,0)\|\le Cm^9q.
\tag{21}
\]

This is a bound on the coupled inverse itself. A raw variational
estimate alone would not imply it.

The derivative of the second equation in $7$ gives, entrywise,

\[
 A_3'\ge R A_2'L\ge 2RFL.
\tag{22}
\]

Since $R,L\ge I$ on the active sector, $20$ implies

\[
 |FL|_d,|RF|_d,|RFL|_d\le Cm^9.
\tag{23}
\]

The inactive identities $9$ give the same bound for the full baseline
sample matrices.

Arbitrary backward-row forcing is handled by the exact shift

\[
 \widetilde Y_3=Y_3-J_3,\qquad
 \widetilde Y_2=Y_2-LJ_3R-J_2,
\]
\[
 \widetilde E_2=E_2+FJ_2F+FLJ_3RF,
 \qquad \widetilde E_3=E_3+VJ_3V.
\tag{24}
\]

The sandwich estimate, with duration $T<2$, gives

$\max(|\widetilde E_2|_d,|\widetilde E_3|_d)\le Cm^{18}q$.
Equations $21$ and $24$ then give an active full inverse bound

$Cm^{27}$, including reconstruction, since

$|LJ_3R|_r\le Cm^{14}q$.

In every non-active sample sector $TX_3T=WX_2W=0$, so it has no
feedback ladder. One determines $Y_3$, then $Y_2$, then $X_2$,
then $X_3$ by direct substitution. This proves a polynomial bound
without a variance inverse. A conservative explicit full-sector bound
is $Cm^{39}$: $24$ gives $X_2$ density at most $Cm^{18}q$, and

\[
 |RX_2L|_d
 \le |R|_r\bigl(|X_2|_d+T|X_2|_d|B_3|_r|V|_d\bigr)
 \le Cm^{19}|X_2|_d.
\]

Thus $Cm^{37}q$ already suffices for $X_3$; $Cm^{39}$ leaves
absolute slack. The right factor $L$ is expanded as $I+B_3V$
here: a row bound on $L$ alone does not bound the strict density of

$X_2L$. This distinction prevents a false mixed-sector estimate.

The power-ten route currently pursued by the parent does not need
this conservative full inverse. It uses the positive supersolution
construction directly, retaining the useful product bounds $23$.

## 7. Conversion back to original feature-time bounds

All actual affine baseline arrays are diagonal in the sample sectors,
so the row norms of $R_1,R,L,R_3$, which transform by diagonal
similarity, do not change. On the active sector $5$ reduces to

\[
 A_2={r\over a}\widehat A_2,\quad
 A_3=ar\widehat A_3,\quad
 B_3={1\over ar}\widehat B_3,\quad
 B_2={a\over r}\widehat B_2.
\tag{25}
\]

These same factors apply respectively to $F,V,T,W$. For strict
densities there is the additional factor

$\Delta t_j/h_j=\lambda=a^3r$; row norms have no such factor.
Therefore the active bounds are

\[
 |F|_{d,s}\le Cr^2m^5,\quad |V|_{d,s}\le Cr^2m^7,
 \quad |T|_{r,s}\le Cm^5/r,\quad |W|_{r,s}\le Cm^7/r.
\tag{26}
\]

Using $r\asymp m^{-4}$ gives the active orders

$m^{-3},m^{-1},m^9,m^{11}$. The inactive forward entries, by $9$,
have original-time density $O(r_-^2)\le O(1)$. Learned forward
moments satisfy the same upper bounds: their active densities are

$O(r^2m^2)$ and $O(r^2m^4)$, and their inactive densities are

$O(r_-^2)$. This proves the full forward bounds in Section 1.

The top $U$ transforms like $A_3$; hence $17$ gives

\[
 |U|_{d,s,+}\le Cr^2m^9\le Cm.
\tag{27}
\]

The products $FL,RF,RFL$ transform like $F$, and $23$ yields
the same bound $Cr^2m^9\le Cm$. Their inactive densities are
again $O(1)$. Since $m\le M$, all bounds in the certificate
follow uniformly over the data. Every beta-enlarged reference obeys
the same estimates. Section 8 extends the beta-derivative argument
from beta one to every beta in $[1,b_3]$, including the first and
second intrinsic comparison scales, using the common enlarged
reference from Section 4.

This certificate supplies no restriction on a nonlinear amplitude by
itself. Its useful conclusion for the proposed improvement is that all
the weaker original-time affine exponents requested by the parent are
valid, including the top strict transfer and the beta product bounds.

## 8. Explicit common prefactor and three intrinsic beta scales

For this numerical certificate, keep $m$ as the **actual dataset endpoint
scale**, and $M=24^{1/4}\delta^{-1/8}$ only as its upper envelope.
Set exactly as in the existing quantitative proof

\[
 C_0=1296000e^{1404},\qquad C_z=1500C_0,\qquad C_g=14400C_0,
\]
\[
 H_{\mathrm{num}}=
 10^{30}(1+C_0+C_z+C_g+e^{1410})^4.
\tag{28}
\]

Thus $H_{\mathrm{num}}$ is the old $C_B$, not an unspecified new
constant. It can serve as a common coefficient in **every affine bound
in the first table**, including the sharpened powers in its middle
column. It also bounds the $L_3$ row discussed below.

Use the three proof-auxiliary scales

\[
 b_j=1+\frac{j}{10^6(200+m^2)},\quad j=1,2,3,
 \qquad b_{\rm far}=1+\frac1{10^5(200+m^2)}.
\tag{29}
\]

They are allowed to depend on the dataset. Only the ultimately chosen
activation amplitude must depend on $\delta$ alone. Since $m>1$,

\[
 H_{\mathrm{num}}^{-1}m^{-2}
 \le b_{j+1}-b_j
 =\frac1{10^6(200+m^2)}
 \le H_{\mathrm{num}}m^{-2},
\tag{30}
\]

also with $b_0=1$. All four scales are in the common extension established
in Section 4. Each $b_j$ leaves at least

\[
 b_{\rm far}-b_j\ge \frac7{10^6(200+m^2)}
 \ge\frac1{3\cdot10^7m^2}
\tag{31}
\]

units of beta room. For a nonnegative-coefficient polynomial, at any
$b\in[1,b_3]$,

\[
 f'(b)\le\frac{f(b_{\rm far})}{b_{\rm far}-b}
 \le 3\cdot10^7m^2f(b_{\rm far}).
\tag{32}
\]

This provides all product bounds from beta differentiation uniformly on
the smaller three scales, not only at beta one.

Here is ample numerical accounting behind the common coefficient. On
the enlarged family and sufficiently fine meshes, take the bound on
each primary component to be $100m$, and the variational propagator
to be $4e^{1410}m^5$. The maximum injection and output Lipschitz costs
in the proof are each at most $3(100m)^2$. Their product times the
propagator is at most $4\cdot10^9e^{1410}m^9$. A factor $100$ covers
the fixed two-sample changes of basis, the scaled Gaussian variances,
the identity term of each row, and the Euler strict margin. Therefore
$10^{12}e^{1410}$ dominates all normalized probe and coefficient
prefactors. Learned moments have smaller prefactors and powers.

The beta derivative costs at most $3\cdot10^7m^2$ by $32$, so
$10^{21}e^{1410}$ dominates the derivative prefactors. Converting
strict densities back to original time uses $a^{-1}\le2$ and

\[
 r=\frac{3}{\sqrt2a^3}m^{-4},
 \qquad r^2\le288m^{-8},\qquad r^{-1}\le m^4.
\tag{33}
\]

Thus the numerical coefficient $10^{25}e^{1410}$ dominates every
entry in the first table, uniformly for beta in $[1,b_3]$.
Finally

\[
 10^{25}e^{1410}<10^{30}e^{5640}\le H_{\mathrm{num}}.
\tag{34}
\]

This proves the requested explicit prefactor certificate. The high
degrees in the optional full coupled-inverse estimate in Section 6
can of course require products of $H_{\mathrm{num}}$; $34$ is a
common prefactor assertion for the affine input table, not an assertion
that every subsequent polynomial manipulation costs only one factor.

The additional backward top resolvent is

\[
 L_3=(I-K_3A_3)^{-1},\qquad
 \widehat L_3=(I-HP_+\widehat A_3)^{-1}.
\tag{35}
\]

For the same independent Gaussian probe inserted into the top backward
answer, the frozen normalized equations are

\[
 d_3=E D+\varepsilon\alpha_jG_0,\qquad
 ED=HP_+x_3,\qquad x_3=\xi^3+A_3d_3.
\]

Thus the derivative of $d_3$ with respect to the added answer is
$L_3$. Its current term is identity. The future output $D$ has
Lipschitz cost one and the state injection cost is at most
$3(100m)^2$. The same signed Gaussian-probe bound yields

\[
 |\widehat L_3|_r\le 1+CTm^2G\le
 H_{\mathrm{num}}m^7.
\tag{36}
\]

The baseline is sample diagonal, so diagonal similarity under $5$
does not change its row norm. Hence $|L_3|_r\le H_{\mathrm{num}}m^7$
in original time as well. The inactive block is exactly identity.
