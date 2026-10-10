# Finite early time: what averaging can and cannot sharpen

Status: scoped same-study research result, 2026-10-10. The finite-horizon
restriction of the existing theorem and the averaged-norm obstruction below
are proved. They do **not** establish a stronger order lower bound for the
original NTH. The algebra behind the obstruction was independently checked
by `/root/tanh_nth_generic`; this is an internal check, not a promotion review.

Author: `/root/nth_average_upper`. Scientific inputs are the supervisor's
assignment, the same-study `SINE_REMAINDER.md` and `NONLINEAR_RESULT.md`, and
direct same-study coordination with the generic-route author. No other study,
experiment, Git operation, or external scientific result is used.

## 1. A fixed early-time interval already contains the proved witness

Keep the exact model, Gaussian initialization, labels, and original
own-residual frozen-top hierarchy of `NONLINEAR_RESULT.md`. In particular,

\[
\phi_\varepsilon(z)=z+\varepsilon\sin z,
\quad 1/8\le\varepsilon\le1/4,
\quad \phi^{(2)}(z)=z,
\quad y=(\eta,0),
\]

where the positive label \(\eta\) is fixed independently of width. Let
\(f_n\) and \(f_n^{(q)}\) denote the dense and original order-\(q\)
predictions. For a fixed \(T>0\), define

\[
E_{n,T}^{\mathrm{test}}(q)
=\sup_{0\le t\le T}
 |f_n(t,-e_1)-f_n^{(q)}(t,-e_1)|.
\tag{1}
\]

The query \(-e_1\) is distinct from the two training inputs \(e_1,e_2\),
and has no training label. Oddness gives the exact identities
\(f_n(t,-e_1)=-f_n(t,e_1)\) and
\(f_n^{(q)}(t,-e_1)=-f_n^{(q)}(t,e_1)\), including the hierarchy's
own residual. Thus this test discrepancy equals the first training
discrepancy in magnitude.

Write \(n_k=\lceil e^k\rceil\),
\(j=2\lfloor q/2\rfloor+1\), and

\[
L_{k,q}=(\eta/16)^j(8e k^4)^{-(j+1)}.
\]

The existing proof locates a discrepancy somewhere in \([0,\tau]\), where

\[
\tau=\frac{L_{k,q}^{1/(j+1)}}{64C_+B^2},
\qquad C_+\ge1,\quad B\ge1.
\]

Because \(0<\eta/16<1\),

\[
0<\tau\le\frac1{512e k^4}.
\tag{2}
\]

The bound is uniform over every retained order covered by the theorem.
Consequently, for every fixed \(T>0\), almost every single fixed
activation parameter, and all sufficiently large \(k\), the same
high-probability event gives simultaneously

\[
E_{n_k,T}^{\mathrm{test}}(q)
\ge\exp\{-C_\eta q[\log(q+1)+\log(k+1)]\},
\qquad 2\le q\le\lfloor k/4\rfloor.
\tag{3}
\]

This is a lower bound for worst error during a fixed finite early-time
interval. It makes no assertion about the fitted endpoint. A finite set
of prescribed observation times that stays away from zero is a different
question: (2) does not place its witness on such a set.

Replacing a benchmark \(n^{-a_0}\) by \(n^{-a_1}\), for any two fixed
positive exponents, changes only the constants obtained by comparing
(3) with that benchmark. At \(q\le k/4\),
\(\log(q+1)+\log(k+1)\le2\log(k+1)\). Hence (3) excludes order
\(q\le c_{\eta,a}k/\log(k+1)\) for accuracy \(O(n_k^{-a})\).
In particular, proving a fixed-\(T\) root-\(n\) dense variability upper
bound would not by itself improve the order scale beyond
\(\log n/\log\log n\). No such benchmark theorem is needed or proved
in this note.

## 2. Averaged state norms retain genuinely supergeometric jets

The previous remainder proof uses the transformed scalar activation

\[
T_\varepsilon(z)=\int_0^z\frac{dw}{1+\varepsilon\cos w},
\qquad H_\varepsilon=\phi_\varepsilon\circ T_\varepsilon^{-1}.
\tag{4}
\]

The coordinate maximum in that proof introduces powers of \(\log n\).
One might try to eliminate all losses by replacing it with an averaged
Euclidean norm. The following proposition shows a distinct obstruction
to that particular repair, even without an extreme coordinate.

**Proposition.** Let \(X_i,G_i\), \(1\le i\le n\), be independent
standard real Gaussians. For \(r\ge1\), define the normalized vector
Taylor coefficient

\[
V_{n,r,i}
=\frac{H_\varepsilon^{(r)}(T_\varepsilon(X_i))G_i^r}
       {r!\sqrt n}.
\tag{5}
\]

There are constants \(c>0\), \(C>1\), independent of \(n,r\) and of
\(\varepsilon\in[1/8,1/4]\), such that

\[
\Pr\left\{\|V_{n,r}\|_2<(c\sqrt r)^r\right\}
\le \frac{4C^r}{n}.
\tag{6}
\]

Thus, simultaneously for \(1\le r\le R\), the lower bounds hold with
probability at least \(1-4RC^R/n\). In particular they hold through
\(R=c_0\log n\) with probability tending to one, for a sufficiently
small fixed \(c_0>0\).

These are coefficients of the actual analytic composition

\[
t\longmapsto
\frac1{\sqrt n}
 \bigl(H_\varepsilon(T_\varepsilon(X_i)+tG_i)\bigr)_{i=1}^n
\tag{7}
\]

at zero. No replacement of the nonlinear activation by a polynomial is
made in this statement.

### Proof: scalar derivatives

Put \(a=\sqrt{1-\varepsilon^2}\). Solving
\(z'=1+\varepsilon\cos z\), \(z(0)=0\), gives, with the continuous
real branch,

\[
\tan\frac{z(\tau)}2
=\sqrt{\frac{1+\varepsilon}{1-\varepsilon}}
  \tan\frac{a\tau}2.
\]

Therefore

\[
1+\varepsilon\cos z(\tau)
=\frac{a^2}{1-\varepsilon\cos(a\tau)},
\qquad
H_\varepsilon'(\tau)
=\frac{a^4}{[1-\varepsilon\cos(a\tau)]^2}.
\tag{8}
\]

The function \(H_\varepsilon\) has a linear drift, but all its
derivatives of positive order are periodic with period \(2\pi/a\).
The absolutely convergent expansion

\[
[1-\varepsilon\cos\theta]^{-2}
=\sum_{p=0}^{\infty}(p+1)\varepsilon^p\cos^p\theta
\]

has nonnegative Fourier coefficients. Its complex Fourier coefficient
at integer frequency \(\ell\ge1\) is at least the contribution of
\(p=\ell\), namely \((\ell+1)(\varepsilon/2)^\ell\).
The frequency-\(r\) coefficient of \(H_\varepsilon^{(r)}\) therefore
has magnitude at least

\[
a^4(r+1)(\varepsilon/2)^r(ar)^{r-1}
\ge a^3(a\varepsilon/2)^r r!.
\tag{9}
\]

The last inequality uses \((r+1)r^{r-1}\ge r^r\ge r!\).

On one period \([-\pi/a,\pi/a]\), the inverse coordinate \(z(\tau)\)
ranges over \([-\pi,\pi]\). The density of \(T_\varepsilon(X)\)
there is

\[
\frac{e^{-z(\tau)^2/2}}{\sqrt{2\pi}}z'(\tau)
\ge\frac{3e^{-\pi^2/2}}{4\sqrt{2\pi}}>0.
\]

This lower bound is uniform in the parameter interval. The integral
of the squared modulus over a period is at least the period length
times the squared modulus of any one Fourier coefficient. Combining
this fact with (9) gives constants \(c_1,c_2>0\) such that

\[
\mathbb E\left|
\frac{H_\varepsilon^{(r)}(T_\varepsilon(X))}{r!}
\right|^2\ge c_1c_2^{2r}.
\tag{10}
\]

The uniform scalar disk estimate proved in `SINE_REMAINDER.md`, applied
on radius \(1/32\), gives the complementary bound

\[
\sup_{\tau\in\mathbb R}
\frac{|H_\varepsilon^{(r)}(\tau)|}{r!}\le32^r,
\qquad r\ge1.
\tag{11}
\]

### Proof: Gaussian direction and empirical averaging

Let

\[
Z_r=\left|
\frac{H_\varepsilon^{(r)}(T_\varepsilon(X))G^r}{r!}
\right|^2,
\qquad \mu_r=\mathbb E Z_r,
\]

with \(X,G\) independent. Equations (10)--(11) show

\[
\mu_r\ge c_1c_2^{2r}(2r-1)!!,
\qquad
\mathbb E Z_r^2\le32^{4r}(4r-1)!!.
\tag{12}
\]

Here \((2r-1)!!\ge r!\ge(r/e)^r\). Moreover

\[
\frac{(4r-1)!!}{[(2r-1)!!]^2}
=\frac{\binom{4r}{2r}}{\binom{2r}{r}}
\le16^r.
\]

Absorbing fixed constants into \(C\) gives
\(\mathbb E Z_r^2/\mu_r^2\le C^r\). Since
\(\|V_{n,r}\|_2^2=n^{-1}\sum_i Z_{r,i}\), Chebyshev's inequality
implies

\[
\Pr\{\|V_{n,r}\|_2^2<\mu_r/2\}
\le4C^r/n.
\]

The lower bound on \(\mu_r\), with a smaller fixed \(c\), proves
(6). A union bound proves its simultaneous version. \(\square\)

## 3. Consequences for the proposed sharpening, and its exact limits

The proposition shows that a bound
\(\|V_{n,r}\|_2\le B^r\) simultaneously through order \(R\) requires
\(B\ge c\sqrt R\) on the displayed high-probability event. Removing
the maximum over coordinates therefore does not in itself produce a
width- and order-independent analytic base. The loss is already present
in a law-of-large-numbers average over typical coordinates.

This is an obstruction to an **absolute state-norm majorant**, not a
proof that a scalar averaged network prediction has these coefficients.
In particular, the Gaussian direction in (7) is independent; the true
flow's directions are correlated, and its higher jets have additional
terms. Signed contractions can cancel terms before a scalar prediction
is formed. We do not identify (5) with the whole initialized physical
jet or with an omitted NTH tensor.

Even an improved remainder base depending polynomially only on order,
\(B_R\le C R^\sigma\) for fixed \(\sigma>0\), would keep the
\(q\log q\) scale in the existing coefficient-transfer argument. To
see this in its most favorable form, suppose the first omitted
coefficient had the width-independent geometric lower bound
\(L\ge c^j\), and take Taylor degree \(R=2j\). The established
transfer with remainder \(C(B_Rt)^{2j+1}\) yields a lower bound whose
negative logarithm is \(O(j\log j)\), not \(O(j)\). Comparing it
with \(n^{-a}\) again gives order \(\log n/\log\log n\). This
observation describes what that proof provides, not an impossibility
theorem for sharper techniques.

There is a second, logically independent loss. The present fixed-parameter
argument only supplies
\(L_{k,q}=\exp[-O_\eta(q\log k)]\). Even a hypothetical order-independent
remainder base, inserted into the current transfer, would retain that
loss and the same asymptotic necessary order. A shorter physical-time
interval does not alter this parameter small-value bound. A new argument
must use additional structure of the actual NTH coefficients, not just
their polynomial degree and a nonzero value at the linear parameter.

For this route to prove the genuinely stronger order
\(q\gtrsim\log n\), two new inputs would suffice in principle:

1. An exponential, rather than \(\exp[-Cq\log q]\), lower bound for a
   relevant coefficient or block of coefficients at one fixed nonlinear
   activation, with the required initialization probability.
2. A scalar discrepancy remainder or direct interval estimate that
   exploits signed cancellations before taking a norm, strong enough to
   transfer that lower bound at a fixed exponential cost in \(q\).

Neither input follows from restricting the error norm to \([0,T]\).
The proved finite-time result is (3); the new substantive diagnosis is
(6). No stronger nonlinear order or array-storage theorem is claimed.

## 4. Bounded same-study checks

The generic-route author independently checked the complete Section 2
above at SHA-256
`bfd08b8cb4cee671555f9a9e246b414855209b9862371daf693428b81f32181d`.
The check covered the exact inverse-coordinate formula, Fourier lower
bound, Gaussian-period density, Cauchy upper bound, moment ratio, and
simultaneous empirical concentration, and found no gap. Its scope is the
independent Gaussian directional composition, not the actual dense jets.

This note's author separately checked the algebraic counterexample and
generic limsup subsections of `FINITE_TIME_COEFFICIENT.md`, through line
170, at SHA-256
`fff936cfa9008c643393ed27b605f41e1ea5ab6662efcd9a906ed4b9c11aa87d`.
The dyadic construction, coefficient-norm bound, every-parameter adverse
subsequence, parity matching, and limsup argument were correct. The later
finite-time non-polynomiality calculation was outside this check.

At the supervisor's separate explicit request, this author read the
complete `FINITE_TIME_TANH.md` and checked Sections 2--4 at SHA-256
`d484836a408a31d96a04b5f2ff55f95f2f51dbdb56e92b63f2efcdf1dee5c4c8`.
No gap was found in the following assigned remainder sub-bridge:

- The orthogonal-input coordinate transform preserves the exact physical
  equations. Real stability uses the raw readout bound to cancel the
  apparent width factor in the derivative of the second-layer gate.
- Differentiation occurs before conditional Gaussian projection. Expanding
  each initialized matrix action into projected Gaussian actions and
  normalized rank-two terms preserves the forest normalization and local
  expression-size count. The raw transformed zeroth coordinate is never
  used as an uncontrolled leaf.
- The extended preactivation Taylor polynomial has a bounded holomorphic
  equation defect and an algebraic defect vanishing through the selected
  degree. Comparing only the original-state polynomial to the actual real
  flow avoids any unproved stability assertion about the extended system.
- The polynomial readout has the raw coordinate bound needed in that
  comparison. The weighted finite NTH estimate retains the original top
  freezing and its own residual.

This last check supports the stated small-time remainder for two tanh
layers and orthogonal inputs, not a coefficient noncancellation theorem,
a correlated-data extension, or any stronger order/storage lower bound.
All checks in this section are internal same-study checks, not independent
promotion reviews. No checked mathematical text was edited by the checker.
