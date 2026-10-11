# Harmonic at fixed dimension: remaining width gate and claim boundary

2026-10-10. Scoped author boundary check, not an independent review or a
promoted result. Only the assigned compact-paper files and the assigned
Harmonic, Taylor, Taylor-prefix and dense/Legendre route notes were used.
No other study, reviewer report, paper edit or Git operation was used.

The current Harmonic proof still has an exponential qualifying-width
condition at fixed input dimension along admissible families with fixed
label-to-gap ratio. The Taylor radius cap removes the corresponding
deterministic contour condition, but inserting that cap into the unchanged
global Chebyshev--Harmonic count introduces an extra inverse-gap storage
term. Absorbing that term into the existing headline reintroduces an
exponential sufficient width condition. This is a limitation of the present
proof and its coefficient accounting. The supplied sources do **not** prove
a fixed-dimension impossibility theorem for the actual retained state.

## 1. Setup and exact meaning of the parameter comparison

Use the network and source criterion of `paper/compact.tex` and
`paper/compact_selected.tex`, without changing the optimizer or the query
domain. For width \(n\), sample count \(m\), input dimension \(d\), population
feature gap \(\gamma>0\), and label RMS \(Y>0\), write

\[
\lambda=\gamma/m\in(0,1],\qquad z=Y/\lambda,\qquad
\ell=\log(en),\qquad T=32\ell/\lambda.
\tag{1}
\]

The scalar \(z\) in this note is the label-to-gap ratio, not a network
preactivation. The paper assumes \(z\le\beta^{-30L}\), where \(\beta\)
is its activation envelope and \(L\) its fixed depth. Its Harmonic headline is

\[
C(m+d)^2+\left(\frac Cd\right)^{d+1}z^4\ell^{3d+2},
\tag{2}
\]

where \(C\) depends only on the activation bounds and depth. Each source
space must approximate the four forward/backward source families in the
paper's `cp:source-families`, in coordinate norm on the prescribed real
time/query domain, with exact initialized-image pairing. The canonical
tolerance is

\[
\eta=\min\left\{1,Y,16z,
\frac{\lambda}{2Cn(1+\lambda^{-1/2})
 (1+\sqrt\ell)e^{\sqrt\ell}}\right\}.
\tag{3}
\]

The comparison below fixes \(d,L,\beta\) and, when taking
\(\lambda\downarrow0\), fixes \(z>0\). Thus \(Y=\lambda z\)
also decreases. Both forms of the decisive factor must be kept visible:

\[
\lambda^{-2}z^{-4}=\lambda^2/Y^4.
\tag{4}
\]

At fixed positive \(Y\), the label assumption already gives
\(\lambda\ge\beta^{30L}Y\); there is no admissible limit
\(\lambda\downarrow0\) with that same \(Y\). In particular, this
calculation is not a lower bound on inverse-gap dependence with an arbitrary
prefactor allowed to depend on \(Y\). It does obstruct the displayed proof's
uniform polynomial onset along the simultaneous admissible scaling above,
even when a polynomial dependence on \(Y^{-1}\) is allowed.

## 2. The existing fixed-dimension gate

The working whole-sphere radius in `compact_foundations.tex` is

\[
r_t^{\rm work}=\frac{c_t}{\sqrt\ell},\qquad
c_t=\frac a{64YSU}
   =\frac a{1024\lambda z^2U},\qquad S=16z.
\tag{5}
\]

Here \(a>0\) is the activation strip width, and \(U>0\) is the
source proof's response coefficient defined by its explicit recurrences.
For fixed \(d,z,L,\beta\), \(U\) is independent of \(\lambda,n\).
The exact gate `cp:src-rectangle-gates` contains

\[
\sqrt\ell\ge c_t
 \max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\tag{6}
\]

Already its first branch, \(r_t^{\rm work}\le1/8\), implies

\[
\ell\ge\frac{a^2}{16384U^2\lambda^2z^4},\qquad
n\ge\exp\left(\frac{a^2}{16384U^2\lambda^2z^4}-1\right).
\tag{7}
\]

This is an actual sufficient-premise requirement of the supplied proof,
not a demonstrated singularity of the trained network. Its reason is
explicit: the proof follows a real trajectory by short contour pieces,
bounds the complex propagator by \(e^{4\mathcal K r_t}\), and controls
additional residual activity and parameter motion by the contour length.

The public radius used in Harmonic's count is

\[
r_t=\frac{1}{\beta^{30L}\lambda z^2\sqrt{(d+3)\ell}},\qquad
r_q=\frac{1}{\beta^{3L}\sqrt{(d+3)\ell}}.
\tag{8}
\]

Imposing \(r_t\le1/8\) directly on this smaller radius would still
give \(\ell\ge64/[\beta^{60L}(d+3)\lambda^2z^4]\).
Thus merely replacing the working coefficient by its public bound does
not change the parameter type of the gate.

This scaling is realizable with fixed dimension and fixed sample count.
For example, set \(d=m=2,L=2\), use \(\phi(u)=u+\cos u\), and take
two normalized inputs with correlation \(c_0\uparrow1\), \(0<c_0<1\).
Their population Gram has diagonal \(q_j\) and off-diagonal \(c_j\), with

\[
q_0=1,\qquad
q_{j+1}=q_j+e^{-q_j}\cosh q_j,\qquad
c_{j+1}=c_j+e^{-q_j}\cosh c_j.
\tag{9}
\]

These are the elementary Gaussian covariance identities supplied in
`HARMONIC_ROUTE.md`. They give \(q_j>c_j\ge0\) for \(0<c_0<1\),
and continuity gives \(q_2-c_2\downarrow0\) as \(c_0\uparrow1\).
Consequently \(\gamma=q_2-c_2>0\) can tend to zero at fixed \(m,d\).
Set both labels equal to \(Y=\lambda z_0\) for any fixed
\(0<z_0\le\beta^{-60}\). All label assumptions hold, and
\(Y^{-1}\) is proportional to \(\lambda^{-1}\).
At any polynomial width in these inverse parameters,
\(\ell=O(\log(1/\lambda))\), so (7) fails eventually.
This example tests the proof gate; it is not a retained-rank lower bound.

## 3. What the Taylor cap does to global Harmonic counting

Use the deterministic cap in `TAYLOR_ROUTE.md`, writing

\[
q_n=\log(e+\ell),\qquad B_n=1+(256z^2/\eta_*)q_n,\qquad
B=\beta^{300L},\qquad
R_n=\frac1{B(1+\lambda B_n)\sqrt{q_n}}.
\tag{10}
\]

Here \(\eta_*>0\) is the activation/depth constant in the source
proof's exponential-budget definition; \(q_n\) is a scalar logarithm,
not a source-space dimension. Consider the prospective whole-sphere
radius \(\widehat r_t=\min\{r_t,R_n\}\), leaving \(r_q,T,\eta\)
unchanged. The bound \(\widehat r_t\le B^{-1}\) removes the
deterministic short-contour restrictions in (6). The Taylor note also
proves the required sum of its two flaring-propagator exponents is small.
These are deterministic radius calculations. The Taylor theorem's scope
is a finite panel; it does not provide a polynomial-width event on the
whole-sphere complex tube, including the angular fields.

Even granting that missing event, the unchanged global polynomial
approximation uses
\(\widehat\alpha_T=\widehat r_t/(4T)\). Therefore, exactly,

\[
\widehat\alpha_T^{-1}
=128\max\left\{
\beta^{30L}z^2\sqrt{d+3}\,\ell^{3/2},
B\lambda^{-1}\ell(1+\lambda B_n)\sqrt{q_n}
\right\}.
\tag{11}
\]

The extra term has \(\lambda^{-1}\) because the global interval
still has length \(T=32\ell/\lambda\). It is absent from the
uncapped radius identity in `cp:time-radius-count`.

For fixed \(d\), the elementary bounds
\(q_n^{3/2}\le4\sqrt\ell\), \(\lambda\le1\), and (10) give

\[
\widehat\alpha_T^{-1}
\le C_d\left[z^2\ell^{3/2}
       +\lambda^{-1}\ell\sqrt{q_n}\right],
\tag{12}
\]

where \(C_d\) depends only on the now-fixed dimension, activations and
depth. This notation is for the present comparison only; it does not
replace the headline's explicit dimension dependence.

Let \(\widehat H_*\) be the cutoff defined in
`cp:harmonic-approximation`, using \(\widehat\alpha_T,r_q,M_n,\eta\),
where \(M_n=\beta^{6L}\sqrt n\). Once its logarithms are bounded
by \(C_d\ell\), the same weighted lattice estimate gives

\[
\begin{aligned}
N
&\le\frac{2\{\widehat H_*+\widehat\alpha_T+(d-1)r_q\}^d}
 {d!\,\widehat\alpha_T r_q^{d-1}}\\
&\le C_d\left[
 z^2\ell^{3d/2+1}
 +\lambda^{-1}\ell^{3d/2+1/2}\sqrt{q_n}\right].
\end{aligned}
\tag{13}
\]

The logarithmic simplification itself does not create the inverse-gap
exponential: at fixed \(d\), the logarithms of \(\lambda^{-1}\) and
\(Y^{-1}\) can be absorbed into \(\ell\) by a polynomial width.
For \(d=1\), the paper's two-point time count gives (13) directly.

The source-rank certificate is \(R\le2m+d+1+4N\) for \(d\ge2\),
with the paper's harmless two-point modification for \(d=1\). Substitution
in its retained inventory therefore gives the sufficient count

\[
C_d(m+d)^2+C_d\left[
z^4\ell^{3d+2}
 +\lambda^{-2}\ell^{3d+1}\log(e+\ell)\right].
\tag{14}
\]

The second term in brackets is new. The existing headline (2) has no
term that pays for it uniformly. Absorbing it into the first term by
this accounting requires

\[
\frac{\ell}{\log(e+\ell)}
\ge c_d\lambda^{-2}z^{-4}.
\tag{15}
\]

Along the fixed-\(m,d,z_0\) family above, the right side grows as
\(\lambda^{-2}\), whereas polynomial width gives a left side of
order at most \(\log(1/\lambda)\). The additive \((m+d)^2\)
term is constant on that family and cannot absorb the extra bound.
Thus the cap plus the present global count does not prove the same
headline at polynomial width. It replaces a contour gate by a storage
absorption gate unless another argument reduces the certified source rank.

This is not solely an artifact of the upper volume estimate. The
prescribed cutoff includes the \(j=0\) time modes, so its number of
coefficient vectors is at least
\(1+\lfloor\widehat H_*/\widehat\alpha_T\rfloor\).
When the cap is active, (11) and \(\widehat H_*\ge c\ell\)
give at least \(c\lambda^{-1}\ell^2\sqrt{q_n}\) such vectors.
At polynomial width in \(\lambda^{-1}\), this exceeds every fixed
power of \(\ell\). However, coefficient vectors can be linearly
dependent, and their initialization arrays are discarded. Their number
is **not** a lower bound on the retained source-space rank or runtime
storage. The paper presently certifies rank by counting these vectors;
a stronger rank argument would be additional work.

## 4. Conclusions that the supplied inputs support

The growing-dimension obstruction in `HARMONIC_ROUTE.md` is not a
fixed-dimension theorem. Its proof fixes an even Walsh degree \(k\),
takes \(n\asymp d^a\), and uses \(d\to\infty\) to make

\[
\frac{8\log(nd)}d\ll1,\qquad n^2/d^k\longrightarrow0.
\tag{16}
\]

Its optional \(m=d\) example also changes dimension. Neither argument
applies with fixed \(d\).

At fixed dimension, the current inputs establish the explicit proof gate
(7), the capped coefficient count (13), and the additional sufficient
storage term (14). They do not prove that the actual network lacks a
larger complex domain, that its source span must have the rank suggested
by the coefficient count, or that the unchanged source criterion makes
the desired polynomial onset impossible. Removing the exponential gate
while keeping the headline, the global construction and the source
criterion is therefore **open in these inputs**. Simply transplanting
the Taylor cap does not complete that repair.

The independent missing obligations are a quantitative whole-sphere
source event and an argument avoiding or absorbing the extra count
without (15). The finite-panel prefix repair only addresses its stated
endpoint/control discretization conditional on its local estimates.
The dense/Legendre route's lower-event statement can help a relative
error comparison once Harmonic has its own polynomial absolute-error
and storage gates; it does not supply either missing Harmonic step.
