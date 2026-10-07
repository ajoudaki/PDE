# Numerical absorption into the unchanged dense certificate

2026-10-07. Bounded author check of the benchmark coefficient only.
No experiment, source change, or promotion.

Current status: Section 5 subsequently closes numerical absorption for an
explicit choice of the structural theorem's previously unspecified mesh
coefficient. Sections 1--4 preserve the earlier assessment when the
coefficient is instead treated as an arbitrary pre-fixed number.

**Conclusion.** The assigned sources justify the explicit error
\(2b_n+A_{\rm num}Yn^{-10}\). They do not by themselves justify a
parameter-polynomial threshold for replacing this by \(3b_n\), because
the fixed label-refined certificate has no supplied positive lower
bound on its leading coefficient. A certified lower bound supplied
before initialization would allow tighter numerical tolerances, with
its precision and acquisition costs charged. The explicit fallback in
GENERAL_DENSE_COMPARISON.md (44) is a different certificate and cannot
silently resolve this issue.

Let \(Y>0\), let \(\delta_0=\delta/256\), and preserve the actual
label-refined certificate as written in POLYNOMIAL_ACCURACY_ONSET.md:

\[
 b_n=\frac{c_0Y}{\sqrt n}
 e^{c_1Y^2\sqrt{\log(en)}}
 \sqrt{8\log\frac{8(n+1)(1+2n)^d}{\delta_0}}
       +\frac{c_2Y}{n},
 \qquad c_0,c_1,c_2>0.
 \tag{1}
\]

Here \(A_{\rm num}>0\) denotes the coefficient of the **combined**
numerical remainder, including the physical external-grid allowance.
It is separated from the certificate coefficients to avoid giving an
inherited unspecified constant the meaning of a new universal one.
For \(Y=0\), both physical prediction and the prescribed decoder
branch are exactly zero and no absorption is needed.

## 1. Exact available absorption gates

For \(n\ge1\) and the stated confidence range, both the exponential
and square-root logarithm in (1) exceed one. Consequently

\[
 b_n\ge c_0Y/\sqrt n,
 \qquad b_n\ge c_2Y/n.
 \tag{2}
\]

The first lower bound gives

\[
 n\ge\max\{1,(A_{\rm num}/c_0)^{2/19}\}
 \quad\Longrightarrow\quad
 A_{\rm num}Yn^{-10}\le b_n.
 \tag{3}
\]

Indeed the required inequality after cancelling \(Y\) is
\(n^{19/2}\ge A_{\rm num}/c_0\). The second lower bound gives the
alternative sufficient gate

\[
 n\ge\max\{1,(A_{\rm num}/c_2)^{1/9}\}.
 \tag{4}
\]

Integer widths use ceilings. These gates use no inverse label amplitude
and no eventual dominance by the exponential in (1). They are polynomial
in the displayed extra coefficient inverses. The assigned sources do
not bound those inverses by a polynomial in
\(\beta^L,m,d,1+m/\gamma,\delta^{-1}\), so that stronger conclusion
cannot be attached to (3) or (4).

## 2. A certified coefficient can instead set the tolerance

Suppose an actually available finite certificate supplies
\(0<\underline c_0\le c_0\). If the combined normalized numerical
error can be made at most \(A_{\rm num}\varepsilon_n\), choose,
before generating any source or seed,

\[
 \varepsilon_n\le
 \min\left\{n^{-10},
          \frac{\underline c_0}{4A_{\rm num}\sqrt n}\right\}.
 \tag{5}
\]

Then its output error is at most \(b_n/4\) at every width, by (2).
Allocating (5) among source truncation, finite matrix calls, arithmetic,
query noise, and physical input/time rounding would give the desired
numerical reserve without a new width condition. This is conditional on
the actual implemented source/query routines supporting those choices.
It does not permit changing an already generated source tape afterward.

The additional logarithmic precision needed by (5) is bounded by
\(C+\log_+(A_{\rm num}/\underline c_0)\). The certificate's own
description and acquisition must be charged, as must any increase in
Taylor degree, tail horizon, grids, transcript length, and seed length
caused by the smaller tolerance. Merely knowing that \(c_0>0\) does
not compute a positive rational lower bound. Even a computable lower
bound need not have polynomial description length or acquisition cost
under the currently stated major-parameter envelopes.

Thus (5) is an honest optional coefficient interface, not a proof that
the current resource table already includes it. An analogous construction
uses a supplied \(0<\underline c_2\le c_2\) and the second bound
in (2).

## 3. What the original proof coefficients do and do not specify

GENERAL_DENSE_COMPARISON.md, Sections 1--2, expressly treats its
\(C,K,\kappa\) as fixed-problem constants whose dependence has not
been fully tracked. The label-refined Lipschitz estimate (10) and dense
certificate (12) retain that convention. They do not assign a numerical
formula to the particular \(c_0\) or \(c_2\) in (1), a computable
positive lower certificate for either, or a convention fixing them
above one.

For an existential upper-bound theorem it is legitimate to *choose* a
larger coefficient, for example \(\max\{1,c_0\}\). For the present
fixed benchmark that replaces (1) by a different numerical function.
It must not be described as absorption into the unchanged certificate.
No lower bound on a particular inherited coefficient follows merely
because a larger valid coefficient can be chosen.

Section 5 gives the explicit fallback

\[
 b_n^{\rm fallback}=
 2\mathcal L_n\sqrt{\log(4N_n/\delta_0)}
       +2(K_t+K_x)/n,
 \qquad \mathcal L_n\ge\frac{2\sqrt L}{\sqrt n}.
 \tag{6}
\]

Here \(N_n\le(n+1)(1+2n)^d\) is the proof grid size,
\(K_t,K_x\ge0\) are its explicit physical time/input moduli, and
\(\mathcal L_n\) is the different explicit Lipschitz coefficient
in its (42). The lower inequality in (6) follows from that coefficient's
prefactor being at least \(2\sqrt L/\sqrt n\) and its exponent
being nonnegative. It supplies a convenient numerical floor for **that**
fallback. However, its leading prefactor does not have the label factor
\(Y\) of (1). At fixed \(n\), (6) stays bounded below by a positive
quantity as \(Y\) tends to zero, whereas (1) with fixed structural
coefficients tends to zero. The assigned sources contain no comparison
\(b_n^{\rm fallback}\le b_n\). Replacing (1) by (6), or inferring
a lower bound for \(c_0\) from (6), would conflate two different
inequalities.

Reconstructing a new explicit label-refined proof could produce another
fully specified certificate of the structural form (1). Without a proved
relation to the already fixed coefficients, this would still define a
new certificate rather than identify the current one.

## 4. Reportable result

Without an additional coefficient certificate, the precise conclusion is

\[
 \sup_{t,x}|\widehat f_n(t,x)-f_n^{\rm independent}(t,x)|
       \le2b_n(\delta/256)+A_{\rm num}Yn^{-10},
 \tag{7}
\]

under the new source/query theorem's other stated conditions. One may
also state \(3b_n\) with the explicit additional gate (3) or (4).
Neither formulation hides the coefficient issue, and (7) preserves the
substantive elimination of the previous root-width statistical bias.
The lack of a supplied lower coefficient bound is a boundary of the
current quantitative certificate, not an impossibility result for the
decoder or a claim that its actual error attains the remainder.

Sources: the authorized integrated GENERAL_DENSE_COMPARISON.md,
Sections 1--2 and 5; current POLYNOMIAL_ACCURACY_ONSET.md; and current
SOURCE_SEED_TRANSCRIPT_CHECK.md. These source passages were reread for
this check. Required mathematical skills remained current. No linked
source outside this bounded assignment was fetched, and only this note
was written in this follow-up.

## 5. Explicit instantiation of the still-existential mesh coefficient

**Subsequent clarification.** The supervisor asked whether the mesh
coefficient can now be specified, since the structural theorem never
fixed it numerically. The answer is yes. This is a valid explicit
instantiation of that existential coefficient and resolves numerical
absorption for the resulting declared certificate. It does not assert
equality to an arbitrary previously fixed smaller \(c_2\); Sections
1--4 remain the assessment for that different fixed-coefficient reading.
The label-refined leading coefficients \(c_0,c_1\) are retained.

Let \(\lambda=\gamma/m\). With \(G\sim N(0,1)\), define

\[
 q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}G)^2,
 \qquad H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),
\]
\[
 s=\max\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
                |\phi_\ell'(z)|\},\qquad B=9s,
\]
\[
 F_{\rm dense}=s^2\left[B^{2L-2}
                    +4H^2\sum_{j=0}^{L-2}B^{2j}\right].
 \tag{8}
\]

These are exactly the constants in the assigned integrated proof (37).
The original label intersection already includes
\(Y\le\lambda/(8H\sqrt{F_{\rm dense}})\). No smaller label
allowance is imposed here.

On the common good event for the original leading comparison and the
explicit fitting bounds, retain the same label-refined Gaussian-root
Lipschitz constant
\(c_0Y n^{-1/2}\exp(c_1Y^2\sqrt{\log(en)})\). The explicit fitting
moduli in that proof's (43), in the physical-time coordinate
\(u=1-e^{-\lambda t/2}\), are

\[
 K_t=\frac{16Y}{\lambda}
               (H^2+F_{\rm dense}Y^2/\lambda),\qquad
 K_x=\frac{2Y B^L}{\sqrt\lambda}.
 \tag{9}
\]

The leading Lipschitz estimate is uniform in physical time, so selecting
this mesh coordinate does not change \(c_0\) or \(c_1\). At a
time mesh and sphere net of spacing \(1/n\), each trajectory changes
by at most \((K_t+K_x)/n\) between a query and its mesh code.
There are still at most \((n+1)(1+2n)^d\) codes. Apply the original
Gaussian concentration proof at those codes with its unchanged leading
constant, then add both trajectories' mesh errors. A valid explicit
choice of the structural coefficient is therefore

\[
 c_{2,\rm mesh}=\frac{2(K_t+K_x)}Y
 =\frac{32H^2}{\lambda}
     +\frac{32F_{\rm dense}Y^2}{\lambda^2}
     +\frac{4B^L}{\sqrt\lambda}.
 \tag{10}
\]

This uses only (43), not the fallback's different leading coefficient
\(\mathcal L_n\) in (42). If intersecting the original leading-comparison
event with the explicit fitting event is necessary, its failure must be
included in the scientific allocation. Restricting the good set preserves
the same Lipschitz constant, and the same Gaussian extension proof
applies on that intersection. This numerical lemma does not replace the
complete source probability theorem.

All diagonals of the population training Gram \(Q^{(L)}\) equal
\(q_L\), since the input vectors have unit norm. Its smallest
eigenvalue obeys \(\gamma\le\operatorname{tr}Q^{(L)}/m=q_L\).
Since \(m\ge1\),

\[
 \lambda=\gamma/m\le q_L\le H^2,
 \qquad c_{2,\rm mesh}\ge32.
 \tag{11}
\]

This coefficient also has polynomial major-parameter growth. Indeed the
original fitting allowance gives
\(32F_{\rm dense}Y^2/\lambda^2\le1/(2H^2)\le1/2\).
For the current envelope \(\beta\ge10\), both
\(s\le\beta\) and \(\max_\ell|\phi_\ell(0)|\le\beta\).
Minkowski gives
\(\sqrt{q_\ell}\le\beta+\beta\sqrt{q_{\ell-1}}\), hence
\(H\le(2\beta)^L\le\beta^{2L}\), and
\(B^L=(9s)^L\le\beta^{2L}\). Using
\(\lambda^{-1/2}\le1+\lambda^{-1}\) in (10) proves

\[
 32\le c_{2,\rm mesh}
       \le C\beta^{4L}(1+1/\lambda)
       =C\beta^{4L}(1+m/\gamma),
 \tag{12}
\]

with an absolute \(C\). If one coefficient is desired for the entire
allowed label interval, replace only the middle term of (10) by
\(1/(2H^2)\); the same proof and bounds hold uniformly in \(Y\).
This is again an explicitly declared choice, not an identification with
an unspecified prior numerical value.

Let \(b_n^{\rm mesh}\) mean (1) with its same \(c_0,c_1\) and the
declared choice \(c_2=c_{2,\rm mesh}\). Equations (10)--(11) imply

\[
 b_n^{\rm mesh}\ge32Y/n,\qquad
 n\ge\max\{1,(A_{\rm num}/32)^{1/9}\}
 \quad\Longrightarrow\quad
 A_{\rm num}Yn^{-10}\le b_n^{\rm mesh}.
 \tag{13}
\]

Thus the new source/query comparison, when stated with this declared
existential structural certificate throughout, has
\(2b_n^{\rm mesh}+A_{\rm num}Yn^{-10}\le3b_n^{\rm mesh}\)
at the polynomial gate (13). No inverse \(c_0\), additional logarithmic
power in the leading error, modified leading label dependence, or
stronger label cap is used. This closes the numerical absorption question
for that explicit instantiation; all other theorem obligations retain
their separately stated status.
