# Exact parity reduction of the fitted-reference cubic

Author: /root/harmonic_route, 2026-09-12.

**Status: exact algebraic reduction; no actual favorable sign obtained.**
On the unchanged G family with $p=1,\zeta=0$, exchange parity forces 16
of the 35 formal symmetric cubic tensor slots to vanish. The remaining
19 slots consist of 10 antisymmetric-sector entries and nine mixed entries.
For each fixed antisymmetric residual, the symmetric coefficients enter
through a fixed two-by-two quadratic form. Across the full four-coefficient
family this form is an affine matrix pencil, because two antisymmetric
coefficients also vary. The precise coefficient domain remains coupled.

This is a bounded follow-up to the frozen parity result, not a new independent
route, a numerical certificate, a sign search, or a promotion review.
The actual fitted reference, all raw blocks, actual initialized action and
adjoint, and anchor projection are retained throughout.

## 1. Inputs and coverage

The two assigned study inputs were read completely:

| Input | Coverage | SHA-256 |
|---|---|---|
| ROUTE_GAUSSIAN_SIGN.md | Lines 1–484; the end of the combined read was repaired by a separate read of lines 365–484 | 2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c |
| ROUTE_GEOMETRY.md | Lines 1–558, completely read previously and retained at the unchanged hash; the present read was supplemented by a separate read of lines 1–198 | e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04 |

The established dependencies used are the already completely read reference
symmetry and feature-clock proof in global_nonlinear.md C.4.5.1 §§1–3,
the actual-source construction in C.4.5.2 §§1–4 and special_data_limits.md
III.F, and the determining equation and strong derivatives in C.4.10.
No new established-source range was fetched for this follow-up.

Relevant retained source and process hashes:

* docs/global_nonlinear.md:
  5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483.
* docs/special_data_limits.md:
  5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489.
* docs/NOTATION.md:
  199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b.
* RESEARCH_WORKFLOW.md:
  8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12.

The previously completely read solve-math-rigorously and
investigate-conjectures skills remain applied. No other study, another
current follow-up, code, experiment, Gaussian quadrature, training procedure,
or Git operation supplied an input. Both frozen study inputs are preserved.

## 2. The actual tensor and its parity

All quantities below are evaluated at the actual fitted reference, at uniform
density. For a bounded odd probe $f$, write

$$
v_f=\int f(u)g_\dagger(u)\,d\rho(u),\qquad
\beta_f=M_\dagger^{-1}G_\dagger^*v_f,\qquad b_f=\Pi_\dagger v_f.
\tag{P1}
$$

Let $\mathcal H_u[z_1,z_2]$ be the symmetric bilinear polarization of
the directional Hessian in geometry (G12). All $b_f$ used here are admissible
directions by the moment and bounded-readout argument in that source.
Define the actual trilinear expression

$$
\mathcal L(f;g,h)=
\int f(u)\mathcal H_u[b_g,b_h]\,d\rho(u)
-\sum_{a=1}^2(\beta_f)_a\mathcal H_{e_a}[b_g,b_h].
\tag{P2}
$$

It is symmetric in its last two arguments. The symmetric tensor of interest is

$$
\mathcal T(f,g,h)=\frac13\{
\mathcal L(f;g,h)+\mathcal L(g;f,h)+\mathcal L(h;f,g)\}.
\tag{P3}
$$

Thus $\mathcal C_1(r)=\mathcal T(r,r,r)$. Formula (P2), including its anchor
subtraction, specifies the actual neural contractions left below; they are
not a covariance of independently refreshed features.

Let $P(u_1,u_2)=(u_2,u_1)$, $Uf=f\circ P$, and $J=-U$.
The reference raw isometry in the two inputs fixes the reached reference,
intertwines predictions with $J$, and preserves the anchor constraint.
The gradient and Hessian transformation laws in the invariant raw metric
therefore give, as in geometry (G16),

$$
\mathcal C_1(Jr)=\mathcal C_1(r),\qquad
\mathcal T(Jf,Jg,Jh)=\mathcal T(f,g,h).
\tag{P4}
$$

The second identity follows either from (P2) or from polarization of the
first. A swap-antisymmetric function has $J$ eigenvalue $+1$; a
swap-symmetric function has $J$ eigenvalue $-1$. For arguments each having
a definite swap parity, consequently

$$
\mathcal T(f_1,f_2,f_3)=0
\quad\text{if an odd number of its arguments are swap-symmetric.}
\tag{P5}
$$

These are exact actual-network cancellations. In particular, for the two
sectors $r_A,r_S$,

$$
\mathcal C_1(r_A+r_S)
=\mathcal T(r_A,r_A,r_A)+3\mathcal T(r_A,r_S,r_S),
\tag{P6}
$$
$$
\mathcal C_1(r_S)=0,\qquad
\mathcal C_1(-r_A+r_S)=-\mathcal C_1(r_A+r_S).
\tag{P7}
$$

The cubic is even in the entire symmetric part and odd in the entire
antisymmetric part. It need not be even in each individual coefficient.
Antipodal oddness supplies no additional selection among the dictionary
entries below, since all of them already have that same odd parity.

## 3. The unchanged family and its exact coupled domain

Keep precisely the original $0<R\le1/8$ and coefficient intervals

$$
a_0,b_0\in[R/16,R/8],\qquad
a_1,b_1\in[R/48,R/24].
\tag{P8}
$$

Set $h(\alpha)=\sin^2(2\alpha)$, $q_0=\cos^3\alpha-\sin^3\alpha$, and
introduce the fixed dictionary

$$
\psi_0=\bar r=F_*-q_0,\quad
\psi_1=A_1=h(\cos\alpha-\sin\alpha),\quad
\psi_2=A_3=h(\cos3\alpha+\sin3\alpha),
$$
$$
\psi_3=S_1=h(\cos\alpha+\sin\alpha),\quad
\psi_4=S_3=h(\cos3\alpha-\sin3\alpha).
\tag{P9}
$$

The first three entries are swap-antisymmetric and the last two are
swap-symmetric. Using $\bar r$ in this analysis does not define a new target:
$q_0$ and all four target coefficients remain those of the original family.
No claim that the five entries are linearly independent is needed.

Use the invertible coordinate change

$$
x=\frac{a_0-b_0}{2},\quad z=\frac{a_0+b_0}{2},\qquad
y=\frac{a_1+b_1}{2},\quad w=\frac{a_1-b_1}{2}.
\tag{P10}
$$

Then the actual initial residual is

$$
r=\bar r-xA_1-yA_3-zS_1-wS_3,\quad
r_A=\bar r-xA_1-yA_3,\quad r_S=-zS_1-wS_3.
\tag{P11}
$$

The exact domain, with no enlargement, is

$$
-R/32\le x\le R/32,\qquad R/48\le y\le R/24,
$$
$$
R/16+|x|\le z\le R/8-|x|,\qquad
|w|\le d(y):=\min\{y-R/48,\ R/24-y\}.
\tag{P12}
$$

Indeed $a_0=z+x,b_0=z-x$ gives the first coupled interval, while
$a_1=y+w,b_1=y-w$ gives the second. Conversely every point of (P12)
gives coefficients satisfying (P8), so this is an exact parameterization.
In particular $z>0$, $y>0$, $|w|\le R/96$, and $|w|/z\le1/6$.
The marginal intervals for $x,y,z,w$ are not a substitute for (P12).

The full parity transform is $(x,y,z,w)\mapsto(x,y,-z,-w)$.
It generally leaves the coefficient box, because that box has $z>0$.
It gives no pair of opposite signs inside the family. The domain does
contain both signs of $w$ at fixed $x,y,z$, but (P4) does not identify
their cubics: the term proportional to $zw$ need not vanish.

## 4. All forced zero slots and the surviving polynomial

Write $T_{ijk}=\mathcal T(\psi_i,\psi_j,\psi_k)$, with nondecreasing indices.
There are 35 formal symmetric slots. Parity gives the following complete
selection rule:

| Type | Slots | Consequence of parity |
|---|---|---|
| Three antisymmetric arguments | 000, 001, 002, 011, 012, 022, 111, 112, 122, 222 | Ten allowed slots |
| One antisymmetric and two symmetric arguments | 033, 034, 044, 133, 134, 144, 233, 234, 244 | Nine allowed slots |
| Two antisymmetric and one symmetric argument | 003, 004, 013, 014, 023, 024, 113, 114, 123, 124, 223, 224 | All twelve are zero |
| Three symmetric arguments | 333, 334, 344, 444 | All four are zero |

“Allowed” means that parity does not force zero; it does not assert
nonzero values or independence of these actual neural contractions.
No positivity statement follows from their being the allowed slots.

Define the antisymmetric baseline polynomial

$$
\begin{aligned}
B(x,y)={}&T_{000}-3xT_{001}-3yT_{002}
 +3x^2T_{011}+6xyT_{012}+3y^2T_{022}\\
&-x^3T_{111}-3x^2yT_{112}-3xy^2T_{122}-y^3T_{222},
\end{aligned}
\tag{P13}
$$

and three fixed symmetric matrices

$$
Q_j=3
\begin{pmatrix}
T_{j33}&T_{j34}\\ T_{j34}&T_{j44}
\end{pmatrix},\qquad j=0,1,2.
\tag{P14}
$$

The exact family cubic is

$$
\boxed{\displaystyle
\mathcal C_1(r)=B(x,y)
+\begin{pmatrix}z&w\end{pmatrix}
\underbrace{(Q_0-xQ_1-yQ_2)}_{Q(x,y)}
\begin{pmatrix}z\\w\end{pmatrix}.}
\tag{P15}
$$

This follows directly from (P6): the two minus signs in the symmetric
arguments cancel, and the factor three is included in (P14). Thus the
coefficient of $zw$ is $2(Q(x,y))_{12}$, not $(Q(x,y))_{12}$.
The polynomial has one constant, two linear, six quadratic, and ten cubic
monomials, for a total of 19 possible coefficients.

For fixed $x,y$, (P15) is a fixed signed quadratic form plus a fixed
antisymmetric baseline. Across the full original box, $B$ is a cubic in
two varying coordinates and $Q$ is an affine pencil. A single constant
quadratic matrix on the entire box would require $Q_1=Q_2=0$:
the six actual mixed tensor entries $T_{133},T_{134},T_{144},
T_{233},T_{234},T_{244}$ would have to vanish. Parity does not give this.
The domain has nonempty interior, so its coupling cannot make those
polynomial identities automatic.

## 5. Exact remaining sign obligation

Let $q_{ij}(x,y)$ denote the entries of $Q(x,y)$. Uniform favorable
quadratic total-risk behavior on the unchanged box is exactly the strict
negative-sign obligation for (P15) on (P12).
The two available signs of $w$ sharpen its form without enlarging the domain:
for fixed $x,y,z$ and $t=|w|$,

$$
\max_{w\in\{-t,t\}}\mathcal C_1(r)
=B(x,y)+q_{11}(x,y)z^2
       +2|q_{12}(x,y)|zt+q_{22}(x,y)t^2.
\tag{P16}
$$

Consequently the exact unresolved scalar bound is

$$
\max_{\substack{|x|\le R/32,\ R/48\le y\le R/24\\
R/16+|x|\le z\le R/8-|x|,\ 0\le t\le d(y)}}
\{B(x,y)+q_{11}(x,y)z^2
+2|q_{12}(x,y)|zt+q_{22}(x,y)t^2\}<0.
\tag{P17}
$$

This is the actual finite tensor sign problem, not a new approximation
framework. In particular an odd-in-$w$ cancellation cannot furnish a
uniform upper bound: the original box contains the worse sign in (P16).

An informative necessary subcase is already present without changing any
target: take $a_0=b_0=z$ and $a_1=b_1=y$. Then $x=w=0$, with the full
original intervals for $z,y$, and

$$
\mathcal C_1(r)=
\mathcal C_1(\bar r-yA_3)
+3z^2\mathcal T(\bar r-yA_3,S_1,S_1).
\tag{P18}
$$

For each fixed $y$, its maximum over $z$ is attained at one of
$z=R/16,R/8$, since it is affine in $z^2$. Even this two-term expression
has no sign supplied by the read sources.

At the actual midpoint of the original four-dimensional box,

$$
x=w=0,\qquad y=R/32,\qquad z=3R/32,
$$

the specific actual-neural contraction that must first be negative is

$$
\boxed{\displaystyle
\mathcal C_1(\bar r-(R/32)A_3)
+\frac{27R^2}{1024}
\mathcal T(\bar r-(R/32)A_3,S_1,S_1).}
\tag{P19}
$$

Negativity of (P19) is necessary, not sufficient, for the uniform box sign.
Both terms use (P1)–(P3), including every hidden/readout Hessian term and
the anchor subtraction. The midpoint is fixed by the original coefficient
intervals and has not been chosen from trained outcomes.

The early-reference signed Gaussian covariance in ROUTE_GAUSSIAN_SIGN.md
does not sign either term of (P19), any of the 19 remaining entries, or
their combination in (P17). It is a first-order statement near reference
time zero about a different mixed moment. The desired contractions are
at the fitted endpoint and contain second prediction derivatives and
projection terms. The source report explicitly supplies no signed
continuation from the early covariance to that endpoint. No such bridge
has been derived here.

## 6. Sign consequences and limitations

The actual sign consequences proved by parity are the exact zero for a pure
symmetric residual and the sign reversal in (P7). They do not give a
favorable sign for the unchanged family, whose antisymmetric coordinates
and strictly positive symmetric first coefficient are both present.
Even the actual midpoint coefficient (P19) remains unsigned.

If (P17) were negative, geometry (G15) would give the positive leading
coefficient $-8\mathcal C_1(r)$ for the matched-clock total-risk difference.
This report establishes no such inequality, no finite-time margin, and no
beneficial relative component learning. An unsigned or positive cubic also
would not rule out a later-time advantage.

The restriction $p=1,\zeta=0$ is substantive. Exchange-invariant densities
retain a related parity identity, but an arbitrary density in the declared
robustness class need not be exchange-invariant. Nothing here silently
averages that density or changes the targets to gain symmetry.

Actual checks: reconstructed the raw-cubic polarization and parity signs;
checked every transformed first/third harmonic; inverted the coefficient
change to recover the exact original box; enumerated all 35 symmetric
slots and their multiplicities; expanded (P15); and checked the mixed-term
factor, worst-sign expression (P16), and midpoint factor in (P19).
All checks were analytic. No actual neural tensor value was evaluated.
