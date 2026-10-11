# Dependent inputs: a sharper index bound and a nonsymmetric low-rank family

2026-10-11. Scoped theoretical continuation. Complete elementary proofs below;
author checked, not independently reviewed or promoted. No simulation, external
scientific retrieval, or Git operation was used. Only this file was written.

The permitted scientific inputs were the complete `GAUSSIAN_RANK_ONE_COMPLETION.md`,
`TANH_NECESSARY_GEOMETRY.md`, and `docs/notation.qmd`. The supervisor subsequently
added the complete `DEPENDENT_GEOMETRY_RENEWAL.md` to the input scope; its results
are treated as prior results, not new discoveries here. Required research,
rigorous-proof, and canonical-notation instructions were read and applied.

Three concrete results are established. First, the accessible mixed-Hessian
bound improves from the prior dimension subtraction to
\[
 \operatorname{ind}_{-}(\nabla^2\mathcal L)
 \ge (n-\operatorname{rank}U)\max\{0,g-k_S\},
\]
where \(g\) is the rank of the residual-weighted backward matrix and \(k_S\)
is the input nullity on the nonzero residual support. For full residual support,
every stratum \(g\ge m-\operatorname{rank}X+2\) has at least \(n\) negative
directions already at width \(n\ge\max\{1,2\operatorname{rank}X-4\}\).

Second, there are explicit minimally dependent three-sample unit inputs and
finite critical points strictly below initial loss, with invertible middle
matrix, nonzero readout coordinates, and unequal nonzero absolute feature
values, whose backward matrix has rank one. Thus a proposed contradiction from
the three scalar stationary identities does not work. These examples are
stationary points; neither local minimality nor Gaussian attraction is claimed.
They do not constitute the requested negative training result.

Third, on the nonsymmetric rank-one stratum, positive-semidefinite Hessian
requires exactly one dominant gauged readout coefficient with the sign of
the total readout, and all remaining coefficients with the opposite sign.
Section 6 eliminates even that pattern at a local minimum. Consequently,
for every three pairwise nonparallel unit inputs and width \(n\ge3\),
there is no finite local minimum with positive loss strictly below the
zero-readout initial loss. This covers every minimally dependent triple,
not only a signed regular triangle. It does not prove Gaussian avoidance
of all finite bad critical limits or exclude escape.

## 1. Model and actual tangent directions

Let \(X=(x_1,\ldots,x_m)\in\mathbb R^{d\times m}\) have unit columns,
pairwise distinct and nonantipodal. The columns may be linearly dependent.
With \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), define
\[
 U=\tanh(AX),\quad Z=WU,\quad H=\tanh Z,\quad
 f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|^2/m.
\]
The coordinates here are the study's unit-input coordinates, so the
\(1/\sqrt d\) factor in the book has already been absorbed in the inputs.
Put
\[
 E=1-U^2,\quad D=1-H^2,\quad
 T=\operatorname{diag}(w)D\operatorname{diag}(r),
\]
with entrywise squares. At finite parameters all entries of \(E,D\) are
strictly positive. The all-trained flow has mobilities \((n,1,n)\).

At a critical point its exact stationary equations are
\[
 Hr=0,\qquad TU^\top=0,\qquad
 [E\odot(W^\top T)]X^\top=0.                         \tag{1}
\]
For an actual first-weight variation \(B\),
\[
                  \delta U=E\odot(BX).                \tag{2}
\]
No surjectivity onto all matrices \(\delta U\) is assumed.

Write \(q=\operatorname{rank}U\), \(h=n-q\), and let
\(Q\in\mathbb R^{n\times h}\) have orthonormal columns spanning
\(\ker U^\top\). The variations \(\delta W=VQ^\top\), with
\(V\in\mathbb R^{n\times h}\), leave \(WU\) exactly fixed. Their pure
loss Hessian is zero and their mixed Hessian with (2) is
\[
 D^2\mathcal L[(0,VQ^\top,0),(B,0,0)]
 =\frac{2}{mn}\langle [E\odot(QV^\top T)]X^\top,B\rangle_F.  \tag{3}
\]
This follows by differentiating the product \(WU\) once in each variable;
the squared-Jacobian term vanishes because the first prediction variation
in the \(W\) direction is zero.

Consequently the Hessian has at least the rank of
\[
                  V\longmapsto [E\odot(QV^\top T)]X^\top     \tag{4}
\]
negative eigenvalues. Indeed, retaining a full-rank part of this mixed
block gives a Hessian restriction
\(\left(\begin{smallmatrix}0&B_0\\B_0^\top&C_0\end{smallmatrix}\right)\).
If \(B_0\) has row rank \(p\), choose a right inverse \(R\).
On \((v,-\varepsilon Rv)\) the quadratic form is
\(-2\varepsilon\|v\|^2+\varepsilon^2(Rv)^\top C_0Rv\),
negative definite for sufficiently small positive \(\varepsilon\).

## 2. A row-basis bound for the mixed map

Assume \(T\ne0\), and define
\[
 g=\operatorname{rank}T,\quad
 S=\{a:r_a\ne0\},\quad
 k_S=|S|-\operatorname{rank}X_{:,S},\quad
 g_j=\operatorname{rank}\bigl(T\operatorname{diag}(E_{j,:})X^\top\bigr).
\]
For \(h>0\), let \(J\) range over sets of \(h\) row indices for which
the square submatrix \(Q_J\) is invertible. Such a set exists because
\(Q\) has column rank \(h\).

**Proposition 1.** At every such finite critical point,
\[
 \operatorname{ind}_{-}(\nabla^2\mathcal L)
 \ge \max_{J:\det Q_J\ne0}\sum_{j\in J}g_j
 \ge h\max\{0,g-k_S\}.                                \tag{5}
\]
For \(h=0\), interpret the right side as zero.

*Proof.* The matrix \(Y=V^\top T\) ranges over every \(h\times m\)
matrix whose rows belong to \(\operatorname{row}T\). Each row can be
chosen independently, because the map \(v^\top\mapsto v^\top T\)
surjects onto that row space. For a fixed admissible \(J\), the map
\(Y\mapsto Q_JY\) is an automorphism of this \(hg\)-dimensional space.
Projecting the output of (4) onto rows \(J\) therefore gives independent
row maps
\[
 z^\top\longmapsto z^\top\operatorname{diag}(E_{j,:})X^\top,
 \qquad z\in\operatorname{row}T,
\]
of ranks \(g_j\). The rank of this projected output is exactly
\(\sum_{j\in J}g_j\), so the full map has at least that rank.

Every vector in \(\operatorname{row}T\) is supported on \(S\).
On all vectors supported there, the displayed row map has a kernel of
dimension \(k_S\): multiplication by the positive gate diagonal is
invertible, and multiplication by \(X_{:,S}\) has nullity \(k_S\).
Its restriction to the \(g\)-dimensional row space of \(T\) thus has
rank at least \(\max\{0,g-k_S\}\). Summing over \(J\), and using
(3)--(4), proves (5). \(\square\)

This improves the prior uniform bound \(hg-nk_S\) by \(qk_S\)
whenever \(g\ge k_S\). It uses a row basis of the neuron nullspace
instead of subtracting the kernels of all \(n\) output rows. The
state-dependent maximum in (5) can be stronger still.

**Corollary 2.** Suppose \(r\ne0\), \(w\ne0\),
\(g\ge k_S+2\), and
\[
                         n\ge\max\{1,2(m-k_S)-4\}.      \tag{6}
\]
Then the Hessian has at least \(n\) negative eigenvalues.
When \(S=\{1,\ldots,m\}\), condition (6) reads
\(n\ge\max\{1,2\operatorname{rank}X-4\}\).

*Proof.* Equation (1) gives orthogonal row spaces for \(T\) and \(U\),
so \(q+g\le m\). Put \(p=g-k_S\ge2\) and \(M=m-k_S\ge p\).
The bound in (5) is at least
\[
 p(n-m+g)=p(n-M+p).
\]
Under (6), \(n-M+2>0\): if \(M=2\), use \(n\ge1\);
if \(M\ge3\), use \(n-M+2\ge M-2>0\). Therefore
\[
 p(n-M+p)\ge2(n-M+2)\ge n,
\]
where the last inequality is exactly \(n\ge2M-4\).
The positive mobilities preserve the unstable index by positive-definite
congruence of the Hessian. \(\square\)

For full residual support and input nullity \(k=m-\operatorname{rank}X\),
this replaces the prior sufficient width \((k+2)(\operatorname{rank}X-2)\)
on the same high-rank strata by \(2\operatorname{rank}X-4\).
It does not control the exceptional strata \(1\le g\le k+1\).

## 3. The low-rank scalar identities have nonsymmetric solutions

The following construction is exact and independent of width. It shows
that even minimal dependence among three unit inputs leaves stationary
configurations beyond signed or zero feature collisions.

Fix \(t>0\), and choose a sufficiently small \(\varepsilon\in(0,t)\).
Let
\[
 z=(t-\varepsilon,t+\varepsilon,-t)^\top,
\]
and set
\[
 \begin{aligned}
 c_1&=1,\\
 c_2&=\frac{(t-\varepsilon)\sinh(2t)
                  -t\sinh(2(t-\varepsilon))}
                 {t\sinh(2(t+\varepsilon))
                  -(t+\varepsilon)\sinh(2t)},\\
 c_3&=\frac{t-\varepsilon+c_2(t+\varepsilon)}t.
 \end{aligned}                                               \tag{7}
\]
These definitions give
\[
                 c^\top z=0,\qquad
                 \sum_a c_a\sinh(2z_a)=0.                    \tag{8}
\]
The second identity follows by substituting the numerator and denominator
in (7), and the first is the definition of \(c_3\).

All \(c_a\) are positive. To see this for \(c_2\), the function
\(s\mapsto\sinh(2s)/s\) is strictly increasing on \(s>0\): its
derivative has numerator \(2s\cosh(2s)-\sinh(2s)\), zero at zero
and with strictly positive derivative \(4s\sinh(2s)\).
Thus both the numerator and denominator of \(c_2\) are positive.
Also \(c_2<1\), because denominator minus numerator equals
\[
 t\bigl[\sinh(2(t+\varepsilon))+
        \sinh(2(t-\varepsilon))-2\sinh(2t)\bigr]>0,
\]
by strict convexity of sinh on positive arguments. Consequently
\[
                    c_3<1+c_2.                              \tag{9}
\]
As \(\varepsilon\downarrow0\), the two quantities defining \(c_2\)
are both
\(\varepsilon[2t\cosh(2t)-\sinh(2t)]+O(\varepsilon^2)\).
Hence \(c_2\to1\), \(c_3\to2\), and for sufficiently small positive
\(\varepsilon\) the other triangle inequalities hold as well:
\[
                    1<c_2+c_3,\qquad c_2<1+c_3.              \tag{10}
\]

Choose unit vectors in \(\mathbb R^2\) explicitly by
\[
 \begin{aligned}
 x_1&=(1,0)^\top,\\
 x_2&=(\gamma,\sqrt{1-\gamma^2})^\top,
 \qquad \gamma=\frac{c_3^2-1-c_2^2}{2c_2},\\
 x_3&=-(x_1+c_2x_2)/c_3.
 \end{aligned}                                               \tag{11}
\]
The strict triangle inequalities imply \(-1<\gamma<1\).
All three vectors are unit, no pair is parallel, and \(X=(x_1,x_2,x_3)\)
has rank two and nullspace \(\operatorname{span}\{c\}\).
By (8), \(z\in c^\perp=\operatorname{range}X^\top\), so there is
an \(a\in\mathbb R^2\) with \(X^\top a=z\).

Write
\[
 u=\tanh z,\qquad e=1-u^2,\qquad b_a=c_a/e_a,
\qquad J(s)=\frac12\sum_{a=1}^3b_a\sinh(2su_a).               \tag{12}
\]
The first two components of \(u\) are positive and the last is negative,
with
\(0<u_1<|u_3|<u_2<1\). The second equation in (8) gives
\[
                         \sum_a b_au_a=0.                    \tag{13}
\]

**Lemma 3.** The function \(J\) has a positive zero \(s_*\).

*Proof.* For \(0<v<1\), define
\[
 k(v)=\frac{(1-v)\operatorname{atanh}(\sqrt v)}{\sqrt v}
 =1-\sum_{j\ge1}\frac{2v^j}{(2j-1)(2j+1)}.                  \tag{14}
\]
This convergent power series shows \(k'(v)<0\) and \(k''(v)<0\).
Its inverse on its range is strictly concave, because
\((k^{-1})''=-k''/(k')^3<0\).

Put \(v_a=u_a^2\) and \(d_a=b_au_a\). Then
\(v_1<v_3<v_2\), \(d_1,d_2>0>d_3\), and (8),(13) give
\[
 \sum_a d_a=0,\qquad
 \sum_a d_ak(v_a)=\sum_a c_az_a=0.                           \tag{15}
\]
Indeed, \(d_ak(v_a)=c_a\operatorname{atanh}(u_a)=c_az_a\),
including the negative third coordinate by oddness of atanh.
Let \(\alpha=d_1/(-d_3)\in(0,1)\). Then
\[
 k(v_3)=\alpha k(v_1)+(1-\alpha)k(v_2).
\]
Strict concavity of the inverse yields
\[
 v_3>\alpha v_1+(1-\alpha)v_2,
 \quad\text{hence}\quad
 \sum_a b_au_a^3=\sum_a d_av_a<0.                           \tag{16}
\]
Expanding (12) and using (13),
\[
 J(s)=\frac23s^3\sum_a b_au_a^3+O(s^5)<0
\]
for all sufficiently small positive \(s\). On the other hand,
\[
                         e^{-2su_2}J(s)\longrightarrow b_2/4>0
 \quad(s\to\infty),
\]
because \(u_2\) is strictly the largest absolute coordinate. Continuity
therefore supplies a zero \(s_*>0\). \(\square\)

## 4. Actual finite critical points strictly below initial loss

Fix any width \(n\ge1\), any \(\beta\ne0\), and the data and
\(s_*\) just constructed. Set every row of \(A\) equal to \(a^\top\),
and let
\[
 W=s_*I_n,\qquad w=\beta\boldsymbol 1_n,\qquad
 h=\tanh(s_*u),\qquad d=1-h^2.
\]
Define fixed residual and label vectors by
\[
                 r_a=\frac{c_a}{d_ae_a},\qquad y=\beta h-r.    \tag{17}
\]
All quantities in (17) are finite, and every \(r_a\) is positive.
The resulting labels are fixed deterministic numbers; varying \(n\)
does not change them.

**Proposition 4.** This is a finite critical point with
\[
 0<\mathcal L=\|r\|^2/3<\|y\|^2/3,
 \qquad \operatorname{rank}U=\operatorname{rank}T=1.           \tag{18}
\]
The matrix \(W\) is invertible, all readout coordinates are nonzero,
and all three first-feature magnitudes are distinct and nonzero.

*Proof.* The forward pass gives
\(U=\boldsymbol1_nu^\top\), \(H=\boldsymbol1_nh^\top\),
and \(f=\beta h\), so the actual residual is (17). By Lemma 3,
\[
 h^\top r=\sum_a \frac{c_ah_a}{e_ad_a}=J(s_*)=0,             \tag{19}
\]
using \(h_a/d_a=\sinh(2s_*u_a)/2\). Thus \(Hr=0\).
Moreover,
\[
 T=\beta\boldsymbol1_nb^\top,
 \quad TU^\top=\beta\boldsymbol1_n(b^\top u)\boldsymbol1_n^\top=0
\]
by (13). Finally \(W^\top T=s_*\beta\boldsymbol1_nb^\top\),
and multiplying entrywise by the identical gate rows \(e^\top\)
gives \(s_*\beta\boldsymbol1_nc^\top\), annihilated by \(X^\top\).
All equations (1) hold.

The residual is nonzero and \(f\ne0\). Equation (19) gives
\(f^\top r=0\), hence
\[
                         \|y\|^2=\|f-r\|^2=\|f\|^2+\|r\|^2.
\]
This proves (18). The other assertions follow directly from the
construction. \(\square\)

At these points every \(g_j\) in Proposition 1 is zero:
\(T\operatorname{diag}(e)X^\top
=\beta\boldsymbol1_nc^\top X^\top=0\).
Thus the entire accessible mixed block (3) vanishes even though \(W\)
is invertible and the loss is strictly below its zero-readout value.
This is an actual obstruction to extending that particular zero-block
argument to all dependent critical points. Other Hessian blocks may
still supply negative directions.

The construction also rules out inferring signed feature copies across
samples from the stationary scalar identities. The rows across neurons
are copies, but the three sample values have distinct nonzero magnitudes.

## 5. A further necessary readout-sign pattern on the nonsymmetric stratum

The preceding stationary family is not a candidate bad basin with positive
readout. In fact it has at least \(n\) negative directions when
\(\beta>0\). More generally, the following sharp necessary sign restriction
substantially narrows a possible positive-semidefinite Hessian.

Consider a minimally dependent three-sample state whose first-layer rows
have been sign-gauged to one common profile \(u=\tanh z\), with three
distinct, nonzero absolute values. Suppose all readout coordinates are
nonzero and the active top slopes have also been sign-gauged to the same
\(s>0\), so
\[
 U=\boldsymbol1_nu^\top,\qquad W\boldsymbol1_n=s\boldsymbol1_n,
 \qquad H=\boldsymbol1_nh^\top,\qquad h=\tanh(su).
\]
These gauges are actual neuron sign symmetries of tanh, preserving loss
and Hessian inertia. Assume the stationary residual has the form
\[
 r_a=\kappa\frac{c_a}{d_ae_a},\qquad
 e=1-u^2,\quad d=1-h^2,\quad \kappa\ne0,
\]
where \(\ker X=\operatorname{span}\{c\}\) and every \(c_a\ne0\).
The stationary identities include \(\sum c_az_a=0\) and
\(\sum c_au_a/e_a=0\). Write
\[
 S_w=\sum_iw_i,\qquad \lambda=W^\top w,\qquad
 a_r=\sum_a r_au_a^2\tanh''(su_a).
\]
At loss strictly below initial, \(S_w\ne0\), since
\(f=S_wh/n\).

**Proposition 5.** At such a point, \(a_r\ne0\). If its full Hessian
is positive semidefinite, then
\[
 a_r\lambda_j\le0\quad\text{for every }j,\qquad
 a_rS_w<0.                                                 \tag{20}
\]
Exactly one readout coordinate has the sign of \(S_w\); all others
have its opposite sign. The magnitude of this single coordinate exceeds
the sum of the magnitudes of the others.

*Proof.* Put \(v_a=u_a^2\) and \(d_a^*=c_au_a/e_a\), keeping
\(d_a^*\) distinct from the activation gate \(d_a\).
The identities give
\[
 \sum_a d_a^*=0,\qquad \sum_a d_a^*k(v_a)=0,
\]
with \(k\) from (14). Since the three \(v_a\) are distinct and
\(k\) is strictly decreasing, the coefficients at the two extreme
values of \(v\) must have the same sign, opposite to the middle
coefficient. Denote the endpoint sign by \(\epsilon\in\{-1,1\}\).
This assertion follows by solving the two linear equations: the value
of \(k\) associated with the lone opposite-sign coefficient is a
strict convex combination of the other two and therefore must be the
middle value.

The function \(g(v)=\sqrt v\tanh(s\sqrt v)\) has \(g'>0\) and
\(g''<0\). With \(x=s\sqrt v\), the sign of its second derivative
is the sign of
\[
 x\operatorname{sech}^2x-\tanh x
       -2x^2\operatorname{sech}^2x\tanh x<0.
\]
Here \(\tanh x>x\operatorname{sech}^2x\), equivalent to
\(\sinh(2x)>2x\). Because \(k',k''<0\),
\[
 \frac{d^2g}{dk^2}=\frac{g''k'-g'k''}{(k')^3}<0.
\]
Strict Jensen on the two endpoint values thus gives
\(\operatorname{sgn}(\sum_a d_a^*g(v_a))=-\epsilon\).
Consequently
\[
 a_r=-2\kappa\sum_a d_a^*u_a\tanh(su_a),
 \qquad \operatorname{sgn}(a_r)=\operatorname{sgn}(\kappa)\epsilon.
                                                               \tag{21}
\]

On the other hand \(F(v)=v/(1-v)\) is strictly convex as a function
of \(k\). To verify the nontrivial sign, use
\[
 k(v)=\int_0^1\frac{1-v}{1-vt^2}\,dt
\]
and differentiate at \(0<v<1\); the denominators are bounded away
from zero on each compact subinterval, justifying differentiation.
Then
\[
 2k'(v)-(1-v)k''(v)
 =-2\int_0^1\frac{(1-t^2)^2}{(1-vt^2)^3}\,dt<0.
\]
Since \(F''k'-F'k''=[2k'-(1-v)k'']/(1-v)^3<0\), division by
\((k')^3<0\) proves \(d^2F/dk^2>0\). Strict Jensen now gives
\(\operatorname{sgn}(\sum d_a^*F(v_a))=\epsilon\). Therefore
\[
 K=-2\kappa\sum_a\frac{c_au_a^3}{e_a^2}
   =-2\kappa\sum_a d_a^*F(v_a)
\]
is nonzero and has sign opposite to \(a_r\).

Because \(c^\top(u\oslash e)=0\), there exists an input direction
\(v_0\) with \(X^\top v_0=u\oslash e\). For arbitrary
\(\alpha\in\mathbb R^n\), choose first-layer row variations
\(B_{j,:}=\alpha_jv_0^\top\). They give
\(\delta U=\alpha u^\top\). Choose a middle-weight variation \(C\)
with \(C\boldsymbol1_n=-W\alpha\). Then \(\delta Z=0\), so the
prediction differential and all outer-activation second-derivative
terms vanish. The mixed product term \(2C\delta U\) also vanishes
after contraction with the residual, because
\((d\odot r)^\top u=\kappa\sum c_au_a/e_a=0\).
The remaining exact loss Hessian is
\[
 D^2\mathcal L[(B,C,0),(B,C,0)]
                =\frac{2K}{mn}\sum_j\lambda_j\alpha_j^2.    \tag{22}
\]
Positive semidefiniteness forces \(K\lambda_j\ge0\), which is
the first part of (20). Summing, and using
\(\sum_j\lambda_j=w^\top W\boldsymbol1_n=sS_w\), gives
\(a_rS_w\le0\). Both factors are nonzero, so the inequality is
strict.

Finally vary only the top slopes by \(\delta s\in w^\perp\),
realized by choosing \(C\boldsymbol1_n=\delta s\). Its prediction
differential is zero and its Hessian is
\[
                   \frac{2a_r}{mn}\sum_iw_i(\delta s_i)^2.
                                                               \tag{23}
\]
If two of the numbers \(a_rw_i\) were negative, a nonzero vector
supported on those two coordinates and orthogonal to \(w\) would
make (23) negative. Thus at most one is negative. Since
\(a_rS_w<0\), at least one is negative and it dominates the sum
of all the positive ones. All coordinates are nonzero by assumption,
proving the stated sign pattern. \(\square\)

For Proposition 4, all \(c_a>0\), so \(\epsilon=1\) and
\(\kappa=1\); hence \(K<0<a_r\). If \(\beta>0\), then
\(\lambda_j=s_*\beta>0\), and (22) is negative definite on an
\(n\)-dimensional space. If \(\beta<0\) and \(n\ge2\), then
(23) is negative definite on the \((n-1)\)-dimensional space
\(w^\perp\). Thus these equal-readout examples are strict saddles
at every width \(n\ge2\), although the latter estimate alone does
not reach the \(n\)-direction threshold.

The exceptional mixed-sign pattern in Proposition 5 remains possible
under these particular tests; Section 6 excludes it at a local minimum
using additional directions. In particular one may not infer
that all gauged readout coefficients are nonnegative merely from the
top-neuron splitting test: for example \(w=(-2,1)\) makes
\(\sum_iw_iq_i^2\) positive on \(w^\perp\).

## 6. All nonparallel triples: no bad local minimum below initial loss

The supervisor supplied the final Schur-complement strategy in this
continuation; the complete verification and degenerate cases follow.
The current complete `DEPENDENT_GEOMETRY_RENEWAL.md`, including its
signed-regular-triangle theorem, was read before this extension. The
new conclusion covers every minimally dependent unit triple.

We first record the algebra needed for the top-layer curvature. It does
not require its coefficient vector to be an input circuit.

**Lemma 6.** Let \(b,z\in\mathbb R^3\) have no zero coordinates and
let the three \(|z_a|\) be distinct. If
\[
                 \sum_a b_az_a=0,\qquad
                 \sum_a b_a\sinh(2z_a)=0,                    \tag{24}
\]
then the diagonal quadratic form
\(\sum_a b_a\tanh(z_a)v_a^2\), restricted to \(b^\perp\),
is indefinite.

*Proof.* Write \(D_a=b_a\tanh z_a\). These coefficients have the
signs of \(b_az_a\), so there are both signs. Changing all \(b_a\)
to their negatives if necessary, suppose exactly one \(D_k\) is
negative. There is a positive direction in \(b^\perp\), supported
on the other two coordinates.

Put \(s_a=|z_a|\) and
\(p_a=b_az_a/(-b_kz_k)>0\) for \(a\ne k\).
Equation (24) gives
\[
 \sum_{a\ne k}p_a=1,\qquad
 \sum_{a\ne k}p_a\frac{\sinh(2s_a)}{2s_a}
                 =\frac{\sinh(2s_k)}{2s_k}.                 \tag{25}
\]
As a function of \(s^2\), \(\sinh(2s)/(2s)\) is strictly increasing
and convex: its series is
\(\sum_{j\ge0}2^{2j}s^{2j}/(2j+1)!\). Jensen therefore gives
\(\sum_{a\ne k}p_as_a^2\le s_k^2\).
The function \(\chi(s)=\coth(s)/s\) is strictly decreasing and
strictly convex as a function of \(s^2\). Indeed,
\[
 \chi'(s)=-\frac{\operatorname{csch}^2s}{s}
          -\frac{\coth s}{s^2}<0,
\]
and
\[
 s\chi''(s)-\chi'(s)
 =2\operatorname{csch}^2s\coth s
  +\frac{3\operatorname{csch}^2s}{s}
  +\frac{3\coth s}{s^2}>0;
\]
division of the latter expression by \(4s^3\) is the second derivative
with respect to \(s^2\). The two endpoint magnitudes are distinct,
so strict Jensen and then monotonicity imply
\[
 \sum_{a\ne k}p_a\chi(s_a)>
 \chi\!\left(\sqrt{\sum_{a\ne k}p_as_a^2}\right)
 \ge\chi(s_k).
\]
Consequently
\[
 \sum_a\frac{b_a^2}{D_a}
 =\sum_ab_a\coth z_a
 =(-b_kz_k)\left[\sum_{a\ne k}p_a\chi(s_a)-\chi(s_k)\right]>0.
                                                               \tag{26}
\]
Set \(R=\sum_{a\ne k}b_a^2/D_a>0\), choose
\(v_a=b_a/D_a\) for \(a\ne k\), and \(v_k=-R/b_k\).
Then \(b^\top v=0\) and
\[
 \sum_aD_av_a^2=R\left(1+D_kR/b_k^2\right)<0,
\]
where the sign is equivalent to (26), since \(D_k<0\).
Together with the positive direction this proves the lemma. \(\square\)

**Theorem 7.** Let \(x_1,x_2,x_3\) be unit inputs with no two
parallel, let \(y\in\mathbb R^3\) be arbitrary, and let \(n\ge3\).
The canonical two-hidden-layer tanh loss has no finite local minimum
with
\[
                         0<\mathcal L<\|y\|^2/3.             \tag{27}
\]

*Proof.* If \(X\) has column rank three, Theorem 7 of the assigned
`TANH_NECESSARY_GEOMETRY.md` applies: its hypotheses are exactly full
column rank, \(n\ge m=3\), and nonzero labels, the latter forced by
(27). It excludes every positive-loss local minimum.

It remains to treat rank two. The kernel of \(X\) is generated by
\(c\in\mathbb R^3\) with every \(c_a\ne0\), because any two columns
are independent. The unit lengths and absence of parallel pairs give
the strict triangle inequalities
\[
                       |c_a|<\sum_{b\ne a}|c_b|.              \tag{28}
\]
For example, take norms in \(c_ax_a=-\sum_{b\ne a}c_bx_b\);
equality would make the two other nonzero vectors parallel.

Suppose a local minimum satisfying (27) exists. In particular
\(f\ne0\), \(w\ne0\), and \(T\ne0\). Theorem 2 of the assigned
`DEPENDENT_GEOMETRY_RENEWAL.md` applies to this minimal unit circuit
with \(n\ge m=3\). Its conclusion is \(\operatorname{rank}U\le1\).
Rank zero would give \(f=0\), so \(\operatorname{rank}U=1\).
We recall the remaining necessary reduction explicitly to cover all
rank-one degeneracies.

For every redundant first-feature row \(j\), the zero pure Hessian
block in (3) and positive semidefiniteness force
\[
                      T\operatorname{diag}(E_{j,:})X^\top=0. \tag{29}
\]
To obtain this rowwise identity, use a vector in \(\ker U^\top\)
with nonzero \(j\)th coordinate, restrict \(VQ^\top\) to one output
row, and vary only row \(j\) of \(B\) in (3). Every mixed pairing
with a zero quadratic direction of a positive-semidefinite form must
vanish.

First suppose at least two rows of \(U\) are nonzero. Every row is
then redundant. Choose a nonzero row \(b^\top\) of \(T\).
Equation (29) implies \(b\odot E_{j,:}=\rho_jc\), where every
\(\rho_j\ne0\). In particular \(b\) has full support and the
gate rows \(E_{j,:}\) are proportional. Write
\(U_{j,:}=\alpha_ju^\top\) with \(u\ne0\). Comparing two gate
rows at two samples gives
\[
 (\alpha_j^2-\alpha_k^2)(u_a^2-u_b^2)=0.
\]
If the \(u_a^2\) were all equal, a nonzero first preactivation row
would be \(\rho\sigma\), \(\rho\ne0\),
\(\sigma\in\{-1,1\}^3\). The relation
\(c^\top\sigma=0\) would violate (28). Thus all
\(\alpha_j^2\) are equal and positive; there are no zero rows.
First-neuron sign symmetries put all rows in the common form
\(U_{j,:}=u^\top\), with common relevant preactivation
\(z=X^\top a\ne0\), \(u=\tanh z\). The word relevant discards
only the unused components of first weights perpendicular to the
input span.

For completeness, exactly one nonzero row of \(U\) is impossible
at this second-order stationary point. The other rows are zero and
redundant, so (29) gives \(T=t c^\top\), \(t\ne0\). Let \(j\)
be the nonzero row, with profile \(u=\tanh z\). Then
\(c^\top u=0\). Its gradient \(X(c\odot(1-u^2))\) is nonzero:
otherwise \(c\odot(1-u^2)\) would be proportional to \(c\),
forcing constant nonzero \(|z_a|\), contrary to (28).
First-weight stationarity in (1) therefore gives
\((W^\top t)_j=0\). Write \(q_i=W_{ij}\). For active readout
rows, \(w_i\operatorname{sech}^2(q_iu)\odot r=t_ic\), so their
positive gate vectors are proportional. The profile \(u\) has at
least two distinct absolute values. For \(0\le a<b\), the ratio
\[
 \frac{\operatorname{sech}^2(qb)}{\operatorname{sech}^2(qa)}
\]
is strictly decreasing in \(q>0\), since its logarithmic derivative
is \(-2b\tanh(qb)+2a\tanh(qa)<0\). Hence all active \(|q_i|\)
equal one \(q\ge0\). If \(q=0\), then \(f=0\). If \(q>0\),
write \(q_i=\sigma_iq\). Identical gates imply
\(t_i=\gamma w_i\) for a common nonzero \(\gamma\); the equation
\((W^\top t)_j=0\) gives \(\sum_i\sigma_iw_i=0\), again implying
\(f=0\). Both possibilities contradict (27).

We have reduced to \(U=\boldsymbol1_nu^\top\), with all first
rows equal in the input span. Put \(e=1-u^2\), \(b=c\oslash e\).
All rows are redundant; (29) and \(TU^\top=0\) imply that every
row of \(T\) is proportional to \(b^\top\), and
\[
                 c^\top z=0,\qquad b^\top u=0,
 \quad\text{equivalently}\quad \sum_ac_a\sinh(2z_a)=0.        \tag{30}
\]
The residual has full support, since a nonzero row of \(T\) is a
nonzero multiple of \(b\), which has full support.

There are only two possible magnitude patterns in (30). Either all
three \(z_a\) are nonzero with distinct absolute values, or exactly
one is zero and the other two have equal absolute value. To verify
this, group terms by their positive magnitude \(s\); the two equations
are linear combinations of \(s\) and \(\sinh(2s)\) with each
group's signed sum of \(c_a\) as coefficient. For two distinct
positive magnitudes, this two-by-two matrix is nonsingular because
\(\sinh(2s)/s\) is strictly increasing. Both grouped coefficients
would have to vanish. With three samples and at most one zero, a
singleton nonzero group would make that impossible. One positive
magnitude shared by all three is excluded by (28); just one nonzero
sample is excluded by \(c^\top z=0\). This proves the two cases.

In the case of three distinct nonzero magnitudes, every \(w_i\) is
nonzero at a positive-loss local minimum. If \(w_i=0\), varying
that row of \(W\) leaves the predictions and loss fixed. All nearby
such points remain local minima, so their \(i\)th readout gradient
must vanish. Varying the row sum would give
\(r^\top\tanh(qu)=0\) on an interval and hence for every real
\(q\) by real analyticity. This forces \(r=0\): the three functions
\(\tanh(q|u_a|)\) are linearly independent, as follows by taking
\(q\to\infty\), subtracting the constant, and successively isolating
the slowest nonzero exponential in
\(\tanh(qs)-1=-2e^{-2qs}(1+o(1))\). This contradicts (27).

In the case with one zero and two equal nonzero magnitudes, all rows
of \(H\) lie on the same sample line. Keeping the nonzero prediction
fixed imposes one nontrivial affine constraint on \(w\). Within
this affine set we can perturb arbitrarily slightly so that all
\(w_i\ne0\): a coordinate currently zero can vary either freely,
if its feature coefficient is zero, or by compensation with a
nonzero feature coordinate. Thus the affine set is not contained
in any relevant coordinate hyperplane. A sufficiently small such
perturbation remains a local minimum with the same loss. Replace
the putative point by this nearby one.

In both cases we may now suppose every \(w_i\ne0\). The proportional
rows of \(T\) and the full-support residual make the top gate rows
proportional. Applying the strictly decreasing gate ratio above to
two different magnitudes in \(u\) makes all active row-sum magnitudes
equal to one \(s\). Nonzero prediction implies \(s>0\). Top-neuron
sign symmetries then yield
\[
 W\boldsymbol1_n=s\boldsymbol1_n,
 \quad H=\boldsymbol1_nh^\top,
 \quad h=\tanh(su),\quad d=1-h^2,
 \quad r=\kappa c\oslash(d\odot e),\quad \kappa\ne0.          \tag{31}
\]
Write \(\lambda=W^\top w\) and \(S_w=\sum_iw_i\ne0\).

Every accessible first-feature row variation lies in \(b^\perp\),
and every vector in that plane is accessible, since
\(\operatorname{diag}(e)\operatorname{range}X^\top=b^\perp\).
Define two symmetric quadratic forms on this plane by
\[
 \begin{aligned}
 B(\xi,\eta)&=-2\kappa\sum_a\frac{c_au_a}{e_a^2}\xi_a\eta_a,\\
 Q(\xi,\eta)&=\sum_ar_a\tanh''(su_a)\xi_a\eta_a
             =-2\kappa\sum_ab_ah_a\xi_a\eta_a.
 \end{aligned}                                               \tag{32}
\]
The first form \(B\) is indefinite. In fact the ridge function
\(F_b(\zeta)=\sum_ab_a\tanh(\zeta^\top x_a)\) has value zero and gradient
zero at the common first row by (30), and nonzero preactivation
\(z\). Theorem 1 of `DEPENDENT_GEOMETRY_RENEWAL.md` applies to
this minimal unit circuit and gives an indefinite Hessian on the
input span. Its matrix is \(-2X\operatorname{diag}(c_au_a)X^\top\).
The bijective tangent map \(\delta a\mapsto
\operatorname{diag}(e)X^\top\delta a\) carries \(B\) to
\(\kappa\) times this Hessian, preserving indefiniteness.

Choose a second vector \(v\) so that \(u,v\) form a basis of
\(b^\perp\). For arbitrary neuron vectors \(\alpha,\beta\), realize
\[
 \delta U=\alpha u^\top+\beta v^\top,
 \qquad \delta W\boldsymbol1_n=-W\alpha,
 \qquad \delta w=0.                                         \tag{33}
\]
The first equation has an actual first-weight variation by the tangent
surjectivity just proved; the second is a solvable linear equation.
Then \(\delta Z=(W\beta)v^\top\) and
\[
                   \delta f=(\lambda^\top\beta)(d\odot v)/n.
\]
The mixed product \(2\delta W\delta U\) has zero residual
contraction because \(b^\top u=b^\top v=0\). Therefore, whenever
\(\lambda^\top\beta=0\), the full exact loss Hessian is
\[
 \frac{2}{3n}\left\{
   \sum_j\lambda_jB(\alpha_ju+\beta_jv,\alpha_ju+\beta_jv)
   +Q(v,v)\,\beta^\top W^\top\operatorname{diag}(w)W\beta
 \right\}.                                                 \tag{34}
\]
There are no omitted squared-Jacobian terms under the stated constraint.

Suppose first that all three \(|u_a|\) are distinct and nonzero.
Proposition 5 applies to (31): writing \(a_r=Q(u,u)\), it gives
\(a_r\ne0\), \(a_r\lambda_j\le0\), \(a_rS_w<0\), and exactly
one negative coefficient among the \(a_rw_i\).
We may ensure every \(\lambda_j\ne0\) by an arbitrarily small
constant-loss change of \(W\). Indeed \(\sum_j\lambda_j=sS_w\ne0\),
so at least one \(\lambda_j\) is nonzero. Give all zero coordinates
small increments of sign \(-a_r\), and subtract their total from
one existing nonzero coordinate, choosing the increments small enough
to preserve its sign. Denote this zero-sum change by \(\delta\lambda\).
The perturbation
\[
              \delta W=\frac{w\,\delta\lambda^\top}{\|w\|^2}
\]
has \(\delta W\boldsymbol1_n=0\) and
\(\delta W^\top w=\delta\lambda\). It leaves \(Z,H,f,r\)
exactly fixed. A sufficiently small perturbation remains a local
minimum. All \(\lambda_j\) there are now nonzero and have the sign
opposite to \(a_r\).

The form \(Q\) is indefinite on \(b^\perp\): apply Lemma 6 with
coefficient vector \(b\) and preactivation \(su\). Its first
identity is \(b^\top u=0\); its second follows from readout
stationarity and (31):
\[
 0=h^\top r=\frac{\kappa}{2}\sum_ab_a\sinh(2su_a).
\]
Its distinct, nonzero absolute values are exactly the case assumption.
Thus we may choose \(v\) with \(Q(v,v)\) of sign opposite to
\(a_r=Q(u,u)\); such a \(v\) is necessarily independent of \(u\).

Set \(K=B(u,u)\), \(L=B(u,v)\), and \(M=B(v,v)\).
The proof of Proposition 5 gives \(K\ne0\) with sign opposite to
\(a_r\); indefiniteness of \(B\) gives \(KM-L^2<0\).
In (34) choose \(\alpha_j=-L\beta_j/K\). The first sum becomes
\[
                         \frac{KM-L^2}{K}\sum_j\lambda_j\beta_j^2,
                                                               \tag{35}
\]
strictly negative for every nonzero \(\beta\), since all
\(\lambda_j/K>0\).
The diagonal form with coefficients \(Q(v,v)w_i\) has exactly
one positive coefficient, because \(Q(v,v)\) has sign opposite
to \(a_r\) and exactly one \(a_rw_i\) is negative.
Consequently its pullback
\(Q(v,v)W^\top\operatorname{diag}(w)W\) has at most one positive
eigenvalue. Restricted to the space \(\lambda^\perp\), whose
dimension is \(n-1\ge2\), it therefore has a nonzero vector
\(\beta\) with nonpositive quadratic value: otherwise the
restriction would be positive definite on a space of dimension at
least two, supplying two positive directions to the original form.
For this \(\beta\), (35) is strictly negative and the remaining
term in (34) is nonpositive. This contradicts the Hessian being
positive semidefinite at the nearby local minimum.

Finally consider the case of one zero feature and two equal nonzero
magnitudes. Permuting and, if necessary, jointly sign-flipping inputs
and labels puts it in the form \(u=(a,-a,0)\), \(a\ne0\).
These sample sign flips preserve the whole loss because the network
is odd in its input. Equation (30) then gives \(c_1=c_2\).
It follows directly from (32) that
\(B(u,u)=Q(u,u)=0\). Since \(B\) is indefinite on the
two-dimensional plane, \(B(u,v)\ne0\) for any independent \(v\).
The variations (33) with \(\beta=0\) have zero prediction
differential and zero entire Hessian quadratic form for every
\(\alpha\). Their mixed Hessian with arbitrary \(\beta\)
variations equals, apart from the positive factor \(2/(3n)\),
\[
                         B(u,v)\sum_j\lambda_j\alpha_j\beta_j.
\]
This formula does not require \(\lambda^\top\beta=0\): the
squared-Jacobian mixed term vanishes because the \(\alpha\)
direction has zero prediction differential; the top residual term
contains only \(\beta\). Positive semidefiniteness forces the
displayed pairing to vanish for all \(\alpha,\beta\), so
\(\lambda=0\). But \(\sum_j\lambda_j=sS_w\ne0\), a contradiction.
Both magnitude patterns have been excluded, proving (27). \(\square\)

The changes along constant-loss parameter sets in this proof are
arbitrarily small and remain inside one minimizing neighborhood.
No conclusion is transferred from a remote point of a flat set.
Nevertheless their use means that the theorem is a local-minimum
exclusion, not a uniform lower bound on the negative index of the
original critical point.

## 7. Precise remaining gap

The new high-rank estimate is pointwise. On those strata, the same
center-stable transversality argument as in the assigned rank-one
completion can be used once its local-manifold hypotheses are supplied.
It does not cover the low-rank points of Proposition 4 or all possible
finite bad limits for dependent inputs.

Proposition 4 constructs no local minimum; Section 5 proves its equal-readout
points are strict saddles for \(n\ge2\). It does not give a basin intersecting the prescribed
Gaussian initialization \(A_{ij}(0)\sim N(0,1)\),
\(W_{ij}(0)\sim N(0,1/n)\), \(w(0)=0\). In particular it says nothing
about failure probability, hidden motion, or loss decrease along a
Gaussian-started trajectory. None of those requirements is replaced by
this stationary construction.

Theorem 7 resolves local-minimum exclusion below initial loss for all
nonparallel triples. Gaussian avoidance of their finite bad critical
limits remains unresolved: the existing slice argument requires more
than absence of local minima. For larger dependent datasets, even the
general low-rank landscape remains unresolved here. A full positive
training result requires an additional instability or basin-transversality
argument and a separate control of escape. A genuine negative
result requires attraction from the canonical zero-readout Gaussian slice
after nonzero hidden and loss motion. No all-time feature-rank persistence
or quantitative kernel gap is assumed anywhere in this note.
