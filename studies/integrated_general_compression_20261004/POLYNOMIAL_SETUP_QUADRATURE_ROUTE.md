# Certified coefficient quadrature for the existing Harmonic source spaces

This is a scoped candidate lemma, not a complete efficient initializer. Its
scientific inputs are the source-family, analytic-domain, expansion, finite-setup,
budget and cost sections of `RESULT.md`, together with `docs/notation.qmd`.
No other study, archived book, trained trajectory or numerical experiment is
used. The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
could not be read because that file returned an operating-system permission error, including on an
escalated read; the accessible rigorous-math skill, the book notation contract
and the user's explicit notation requirements were applied instead.

The result below replaces the elementary angular Riemann rule by an explicit
exponentially accurate rule. It preserves the retained joint mode set, exact
initialized-matrix pairing, source-rank bound and coordinate-error allowance.
Its evaluation points are real. It does **not** provide those source values
efficiently from the initialization. That remaining task is stated explicitly
in the oracle contract and cost formulas.

## 1. Precise input and conclusion

Fix a permitted width and source event in `RESULT.md`, a finite source horizon
\(T\ge T_0=32(m/\gamma)\log(en)\), and source-coordinate tolerance
\(0<\eta\le\eta_0=\min(1,Y,16Ym/\gamma)\). These are the existing
Harmonic source qualifications; in particular the retained set below is
nonempty. At hidden layer
\(j\), the existing source families are

\[
h_n^{(j)}(t,v),\qquad
W_0^{(j)}h_n^{(j-1)}(t,v),\qquad
\delta_n^{(j)}(t,v),\qquad
W_0^{(j+1)T}\delta_n^{(j+1)}(t,v),
\]

with the same omissions at the first and last layers as in `RESULT.md`.
Here \(v=x/\sqrt d\in S^{d-1}\), \(W_0\) is an initialized
dense mixer, and \(\delta_n\) is the existing passive-query backward
field. Consider one scalar coordinate \(g(t,v)\) of any of these
families. Put

\[
G(u,v)=g\bigl(T(1+\cos u)/2,v\bigr),\qquad
\alpha=\alpha_T=\frac{r_t}{4T},\qquad a=\alpha/2.
\tag{1}
\]

The source theorem supplies holomorphy on a neighborhood of
\(\{|\operatorname{Im}u|\le\alpha\}\times\mathcal Q_{r_q}\)
and the uniform coordinate bound \(|G|\le M_n\), where

\[
\mathcal Q_r=
\{z\in\mathbb C^d:z^Tz=1,\ \|\operatorname{Im}z\|_2\le\sinh r\},
\qquad M_n=10\max(H_L^{\rm src},\tau)\sqrt n.
\tag{2}
\]

As in the original source proof, \(\alpha\le1\). The choice of the
smaller strip \(a\) merely leaves an analytic margin. All bounds below
are deterministic on that same source event.

For \(d\ge2\), use the real orthonormal spherical harmonics
\(Y_{\ell,b}\) under probability-sphere measure \(\sigma\). Their
degrees are denoted \(\ell\), to distinguish them from hidden layers.
Write

\[
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},\qquad
\mathcal Y_J=\max_{0\le\ell\le J}\sqrt{h_\ell},\qquad
H=\sum_{\ell=0}^J h_\ell.
\tag{3}
\]

Impossible binomials are zero. Retain **exactly** the original joint set

\[
\Lambda=\{(k,\ell,b):k\ge0,\ \alpha k+r_q\ell\le H(T,\eta),
\ 1\le b\le h_\ell\},
\quad N=|\Lambda|=N(T,\eta),
\tag{4}
\]

and put \(p=\max_\Lambda k\), \(J=\max_\Lambda\ell\).
The exact retained cosine coefficients are

\[
c_{k\ell b}
=\gamma_k\int_0^{2\pi}\int_{S^{d-1}}
G(u,v)\cos(ku)Y_{\ell,b}(v)\,d\sigma(v)\frac{du}{2\pi},
\quad \gamma_0=1,\quad\gamma_k=2\ (k\ge1).
\tag{5}
\]

Thus the factor two for positive modes is part of the definition and of
every error estimate below. The original expansion proof gives coordinate
error at most \(\eta/16\) for the omitted modes.

Define the target error for each retained coefficient by

\[
\epsilon_c=\frac{\eta}{16N\mathcal Y_J}.
\tag{6}
\]

The explicit rule constructed below gives exact-value quadrature error
at most \(\epsilon_c/2\). If supplied nodal values have the common
coordinate accuracy in (24), their contribution is at most
\(\epsilon_c/2\). Consequently every retained coefficient has error
at most \(\epsilon_c\), and its finite reconstruction has error at
most

\[
\frac{\eta}{16}+N\mathcal Y_J\epsilon_c=\frac{\eta}{8}<\eta.
\tag{7}
\]

The first term is the original truncation tail. Every member of every
source pair is treated with its own coordinate guarantee.

## 2. Sphere coordinates and their complex neighborhood

For \(d\ge3\), use the usual successive polar angles
\(\theta_1,\ldots,\theta_{d-2}\in[0,\pi]\) and final azimuth
\(\varphi\in[0,2\pi]\):

\[
v=(\cos\theta_1,\ \sin\theta_1\cos\theta_2,\ldots,
\ \textstyle\prod_{i=1}^{d-2}\sin\theta_i\cos\varphi,
\ \textstyle\prod_{i=1}^{d-2}\sin\theta_i\sin\varphi).
\tag{8}
\]

The intermediate coordinates follow the same displayed pattern. For
\(d=2\), use only \(v=(\cos\varphi,\sin\varphi)\).
Introduce

\[
I_b=\int_0^\pi\sin^b\theta\,d\theta,\qquad
I_0=\pi,\quad I_1=2,\quad
I_b=\frac{b-1}{b}I_{b-2}\ (b\ge2).
\tag{9}
\]

The recurrence follows by integration by parts. Differentiating (8) gives
orthogonal coordinate tangent vectors: the vector for each successive
angle has length equal to the product of the preceding polar sines.
Multiplying these lengths gives the Jacobian
\(\prod_{i=1}^{d-2}\sin^{d-1-i}\theta_i\). Its successive
integrals are the factors \(I_{d-1-i}\), so normalization proves that
probability-sphere integration becomes product integration under the uniform measures
\(d\theta_i/\pi\) and \(d\varphi/(2\pi)\), with the multiplier

\[
W(\theta)=\prod_{i=1}^{d-2}
\frac{\pi}{I_{d-1-i}}\sin^{d-1-i}\theta_i.
\tag{10}
\]

Empty products are one. In particular this formula includes \(d=2\).
Write

\[
A_d=\prod_{b=1}^{d-2}\frac{\pi}{I_b},\qquad
D_d^{\rm ang}=\frac{(d-2)(d-1)}2,\qquad
h=\frac{r_q}{2(d-1)},\qquad
\sigma=\operatorname{arsinh}(2h/\pi).
\tag{11}
\]

These constants expose the dependence on dimension. The angular multiplier
satisfies \(0\le W\le A_d\) on real angles and

\[
|W(\theta)|\le A_d(\cosh h)^{D_d^{\rm ang}}
\quad\text{if all }|\operatorname{Im}\theta_i|\le h.
\tag{12}
\]

Indeed \(|\sin(x+iy)|^2=\sin^2x+\sinh^2y\le\cosh^2y\).

To check the source domain, represent (8) as successive coordinate-plane
rotations applied to a real unit vector. Real rotations preserve
\(z^Tz=1\) and \(\|\operatorname{Im}z\|_2\). For
\(z=b+ic\) on that quadric there is \(s\ge0\) with
\(\|b\|_2=\cosh s\), \(\|c\|_2=\sinh s\). Applying a
coordinate-plane rotation of imaginary angle \(iy\) gives

\[
\|\operatorname{Im}(R(iy)z)\|_2
\le \sinh|y|\,\|b\|_2+\cosh|y|\,\|c\|_2
=\sinh(s+|y|).
\tag{13}
\]

For the unchanged coordinates the real part of this rotation is the
identity, whose norm is at most \(\cosh|y|\); its imaginary part
has norm at most \(\sinh|y|\), which proves the inequality.
Decompose each complex angle into its commuting real and imaginary
rotations and apply (13) successively. If all \(d-1\) angles have
imaginary parts of magnitude at most \(h\), the resulting point lies
in \(\mathcal Q_{(d-1)h}=\mathcal Q_{r_q/2}\). Real parts may
lie outside the fundamental angle boxes without changing this argument.

The angular composition of a degree-\(\ell\) harmonic polynomial
is a trigonometric polynomial of degree at most \(\ell\) separately
in every angle. If a trigonometric polynomial \(P\) has degrees
between \(-\ell\) and \(\ell\) and satisfies \(|P|\le C\)
on the real axis, then

\[
|P(x+iy)|\le C e^{\ell|y|}.
\tag{14}
\]

For \(y\ge0\), multiply its Laurent polynomial by \(z^\ell\),
apply the maximum modulus principle inside \(|z|\le1\), and set
\(z=e^{i(x+iy)}\). For \(y\le0\), use the reversed Laurent
polynomial. Iterating this argument over the angles, starting from
the real-sphere bound \(|Y_{\ell,b}|\le\sqrt{h_\ell}\), gives

\[
|Y_{\ell,b}(v)|\le\mathcal Y_J e^{J(d-1)h}
\quad(\ell\le J).
\tag{15}
\]

Finally \(|\cos(ku)|\le e^{ka}\) in the time strip. Every
coefficient integrand, including \(\gamma_k\), is therefore
holomorphic on the product domain just described and bounded there by

\[
B_{\rm int}=
2M_n\mathcal Y_J A_d
\exp\{ap+J(d-1)h\}(\cosh h)^{D_d^{\rm ang}}.
\tag{16}
\]

This is an integrand bound, not an additional source or rank parameter.

## 3. Explicit positive quadrature and its error

### Periodic variables

For a \(2\pi\)-periodic function \(F\), use
\(Q_NF=N^{-1}\sum_{r=0}^{N-1}F(2\pi r/N)\).
If \(F\) is holomorphic near \(|\operatorname{Im}z|\le b\)
and bounded there by \(B\), contour translation gives Fourier
coefficient bound \(|\widehat F_k|\le Be^{-b|k|}\). Absolute
convergence permits termwise quadrature. The discrete average of
\(e^{ikz}\) is one when \(N\) divides \(k\), zero otherwise;
therefore

\[
\left|\int_0^{2\pi}F(u)\frac{du}{2\pi}-Q_NF\right|
\le2B\sum_{r=1}^{\infty}e^{-brN}
=\frac{2B}{e^{bN}-1}.
\tag{17}
\]

Use this rule for time with \(b=a\), and for azimuth with \(b=h\).
Both rules have positive weights summing to one.

### Polar variables

The following construction supplies the nodes and weights; no Gaussian
quadrature construction is assumed. For an integer \(M\ge1\), let

\[
\omega_r=\frac{(2r+1)\pi}{2M},\quad x_r=\cos\omega_r,
\quad r=0,\ldots,M-1,
\]
\[
w_r=\frac1M\left[
1-2\sum_{k=1}^{\lfloor(M-1)/2\rfloor}
\frac{\cos(2k\omega_r)}{4k^2-1}\right].
\tag{18}
\]

These are Fejér's first interpolatory weights for the normalized integral
\(\frac12\int_{-1}^1\). The discrete cosine identities at these
nodes give the interpolant

\[
I_{M-1}F(x)=
\frac1M\sum_r F(x_r)
\left[1+2\sum_{k=1}^{M-1}\cos(k\omega_r)T_k(x)\right].
\tag{19}
\]

To verify the identity, sum the elementary geometric series for
\(e^{ij\omega_r}\), or use
\(2\cos j\omega\cos k\omega=\cos((j-k)\omega)+
\cos((j+k)\omega)\). The constant mode has squared discrete norm
\(M\); all nonconstant modes through \(M-1\) have squared norm
\(M/2\), and unequal modes are orthogonal. Evaluating (19) at
the nodes then gives their prescribed values. Substitution
\(x=\cos\omega\) in the elementary integral gives

\[
\frac12\int_{-1}^1 T_k(x)\,dx=
\begin{cases}
1,&k=0,\\
0,&k\text{ odd},\\
-1/(k^2-1),&k\ge2\text{ even}.
\end{cases}
\]

Integrating (19) proves (18) and exactness for every polynomial of
degree at most \(M-1\). Moreover

\[
2\sum_{k=1}^K\frac1{4k^2-1}=1-\frac1{2K+1}<1
\]

for finite \(K\), by telescoping. Thus every \(w_r>0\), including
the empty-sum case, and exactness for constants gives \(\sum_rw_r=1\).

Suppose \(F\) is holomorphic near the filled Bernstein ellipse
\(x=(z+z^{-1})/2\), \(|z|=e^\sigma\), and bounded there by
\(B\). Its Laurent expansion in \(z\) is symmetric under
\(z\mapsto z^{-1}\). Cauchy's coefficient formula therefore gives
Chebyshev coefficients of magnitude at most \(2Be^{-k\sigma}\)
for \(k\ge1\). The truncated degree-\(M-1\) series has uniform
real-interval error at most
\(2Be^{-M\sigma}/(1-e^{-\sigma})\). Both the exact normalized
integral and the positive quadrature have operator norm one on real
continuous functions. Subtracting that polynomial from each proves

\[
\left|\frac12\int_{-1}^1 F(x)\,dx-\sum_rw_rF(x_r)\right|
\le\frac{4Be^{-M\sigma}}{1-e^{-\sigma}}.
\tag{20}
\]

Apply this rule to \(\theta=\pi(1+x)/2\). The ellipse has
\(|\operatorname{Im}\theta|\le(\pi/2)\sinh\sigma=h\),
by (11). It is therefore inside the previously verified angular
domain. The normalization becomes \(d\theta/\pi\), as required
in (10).

### Tensor rule and explicit sufficient sizes

Each univariate exact integral and quadrature is a contraction in the
supremum norm. Write their product difference as a telescoping sum,
changing one factor at a time. Apply (17) or (20) to that factor while
the remaining variables are real, and then apply the other contraction
operators. There are \(d\) variables in total: time, azimuth and
\(d-2\) polar variables. This gives

\[
|c_{k\ell b}-Q c_{k\ell b}|
\le B_{\rm int}\left[
\frac2{e^{aN_t}-1}+\frac2{e^{hN_\varphi}-1}
+\frac{4(d-2)e^{-\sigma N_\theta}}{1-e^{-\sigma}}
\right].
\tag{21}
\]

Here \(Q c_{k\ell b}\) denotes application of the tensor rule to
the integrand of (5) after the angular change of variables. The signs
of the harmonic and cosine do not affect positivity of the underlying
integration rule.

Choose

\[
N_t=\max\left\{1,
\left\lceil\frac1a\log\left(1+\frac{4dB_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\},
\]
\[
N_\varphi=\max\left\{1,
\left\lceil\frac1h\log\left(1+\frac{4dB_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\},
\]
\[
N_\theta=\max\left\{1,
\left\lceil\frac1\sigma
\log\left(\frac{8dB_{\rm int}}
{\epsilon_c(1-e^{-\sigma})}\right)\right\rceil\right\}
\quad(d\ge3).
\tag{22}
\]

Each of the \(d\) contributions in (21) is then at most
\(\epsilon_c/(2d)\). The total spatial node count is

\[
N_x=N_\varphi N_\theta^{d-2}\quad(d\ge3),
\qquad N_x=N_\varphi\quad(d=2).
\tag{23}
\]

The dependence on \(d\), \(\alpha\), \(r_q\), \(p\),
\(J\), \(M_n\), \(N\), and \(\eta\) is explicit in
(3), (6), (9), (11), (16), and (22). In particular no equality
\(N_x=H\) or \(N_t=p+1\) is assumed.

## 4. Inexact nodal values and exact source pairing

At every time/spatial node, suppose an initialization-based procedure
supplies all needed vector sources with coordinate error at most

\[
\delta_{\rm node}=
\frac{\epsilon_c}{4A_d\mathcal Y_J}.
\tag{24}
\]

All quadrature weights before the multiplier \(W\) are positive
and have total mass one. On real nodes \(W\le A_d\),
\(|Y_{\ell,b}|\le\mathcal Y_J\), \(|\cos ku|\le1\), and
\(\gamma_k\le2\). Therefore the coefficient error caused by
these nodal errors is at most

\[
2A_d\mathcal Y_J\delta_{\rm node}=\epsilon_c/2.
\tag{25}
\]

This supplies the second half of the error allocation in (7).
It does not assume holomorphy of the numerical nodal approximation;
the quadrature analysis applies to the exact analytic source, followed
by the separate finite-sum perturbation estimate (25).

For exact preservation of initialized-matrix pairing, more than separate
numerical accuracy is required. In the following pairing identities only,
let \(g\) denote the full \(\mathbb R^n\)-valued source, so the
preceding coordinate estimates apply to each of its entries. Let \(A\)
be the fixed initialized
matrix in one pair: either \(W_0^{(j)}\) or
\(W_0^{(j+1)T}\). The two input families are \(g\) and
\(Ag\). Require their nodal approximants to have the exact algebraic
form

\[
\widetilde{Ag}(u_r,v_s)=A\widetilde g(u_r,v_s),
\tag{26}
\]

while **each side separately** has coordinate error at most
\(\delta_{\rm node}\) relative to its own exact source. Applying
identical real quadrature, cosine normalization and retained-mode
restriction to both sides gives, in exact arithmetic,

\[
\widetilde c^{\,Ag}_{k\ell b}
=\sum_{r,s}\beta_{k\ell b,rs}A\widetilde g(u_r,v_s)
=A\sum_{r,s}\beta_{k\ell b,rs}\widetilde g(u_r,v_s)
=A\widetilde c^{\,g}_{k\ell b}.
\tag{27}
\]

The scalar coefficients \(\beta\) are the same in both sums.
The reconstructed approximants consequently satisfy
\(p_{Ag}=Ap_g\) at every real time/query, exactly. The source-space
membership and action identities used in `RESULT.md` are unchanged.

Exact source evaluation satisfies (26). The original common finite
initial-jet reconstruction also satisfies it: differentiation, scalar
continuation, truncation and this quadrature all commute with a fixed
matrix. Its sufficiently large common jet cutoff can certify the
required coordinate errors separately for every member, because each
member has the same source bound. This establishes finite realizability
without establishing an efficient cutoff. Independently computed
approximate nodal values do not automatically satisfy (26), even when
they are each accurate. Deriving the image's error from the feature's
coordinate error through a dimension-dependent matrix norm is not used.

No quadrature node is a generator of \(E_j\). The generators remain
the coefficient vectors indexed by \(\Lambda\), plus the original
exact initialized vectors. Thus

\[
\dim E_j\le R=2m+d+1+4N,
\tag{28}
\]

with the existing boundary-layer improvements. This is exactly the old
dimension certificate. The original budget prescription proves its own
bound \(9R\le q\); replacing the quadrature does not enlarge it.
For a supplied alternative mode set, the existing actual-rank test
\(9r\le q\), \(r=\max_j\dim E_j\), is still the applicable
selector guarantee. Numerical perturbations can change actual rank, so the
safe argument uses (28), not an assertion that an old accidental rank
deficiency persists. The selected runtime, its learned and fixed storage,
and the dense-comparison certificate therefore retain their existing
bounds whenever the original count certificate applies.
The exact initialized training vectors, first-weight columns and constant
are still inserted by their original exact construction. Baseline-only,
zero-label and full-width exact-retention branches need no quadrature and
are unaffected.

## 5. Dimensions one and two

For \(d=2\), equations (3)--(28) apply with no polar angles,
\(A_2=1\), \(D_2^{\rm ang}=0\), and \(h=r_q/2\).
The basis is \(1,\sqrt2\cos(\ell\varphi),
\sqrt2\sin(\ell\varphi)\). Hence \(\mathcal Y_J=\sqrt2\)
if \(J\ge1\), and \(\mathcal Y_0=1\). The spatial rule is
just the positive circle trapezoid, with \(N_x=N_\varphi\).

For \(d=1\), the source domain has precisely the two inputs
\(v=-1,1\). Perform their cosine expansions separately, with
\(N_1=N_1(T,\eta)\), \(p=N_1-1\), and

\[
\epsilon_c=\frac{\eta}{16N_1},\qquad
B_{\rm int}=2M_ne^{ap},\qquad
N_t=\max\left\{1,
\left\lceil\frac1a\log\left(1+\frac{4B_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\}.
\tag{29}
\]

Use the time trapezoid only. Its coefficient error is at most
\(\epsilon_c/2\). The common nodal tolerance is
\(\delta_{\rm node}=\epsilon_c/4\), which gives the other half
because \(\gamma_k\le2\). The original separate time tails are
at most \(\eta/16\), so the same reconstruction bound (7) holds
at both inputs. There are \(N_x=2\) spatial evaluations, not an
angular grid. The rank certificate remains
\(R=2m+d+1+8N_1\), and the same exact linear pairing proof applies.

## 6. Node generation, arithmetic and peak setup memory

All counts below use the exact-real arithmetic contract of `RESULT.md`.
Elementary trigonometric and inverse/hyperbolic scalar evaluations are
reported as scalar calls; their bit complexity is not claimed to be
constant. The needed one-dimensional rule orders are part of the input
to the following execution, determined by the explicit certificates above.

For \(d\ge3\), build the \(N_\theta\) nodes and weights in
(18). At each node use angle-addition recurrences to evaluate the
\(O(N_\theta)\) cosine terms in its weight. This costs
\(O(N_\theta^2)\) arithmetic and \(O(N_\theta)\) words.
The same normalized unweighted rule is reused in every polar coordinate;
only the Jacobian power changes. Computing the constants (9) and the
normalizations (10) costs \(O(d)\) arithmetic. The time and azimuth
rules cost \(O(N_t+N_\varphi)\) arithmetic and words if cached.
Enumerating the spatial tensor product and mapping each point to the
sphere costs \(O(dN_x)\). Powers in (10) can be computed using
\(O(d)\) multiplications per node after powers of each cached
one-dimensional sine through \(d-2\) are prepared, or directly in
\(O(d^2)\) per node. Use the former execution and charge
\(O(dN_\theta)\) preparation and storage.

Consequently a sufficient rule-only bound is

\[
\mathcal G_{\rm rule,time}
=O\bigl(N_\theta^2+dN_\theta+N_t+N_\varphi+dN_x+d\bigr),
\]
\[
\mathcal G_{\rm rule,memory}
=O(dN_\theta+N_t+N_\varphi+d),\qquad d\ge3.
\tag{30}
\]

There are \(O(N_\theta+N_t+N_\varphi)\) elementary scalar
trigonometric calls with direct one-dimensional tables. The orders in
(22) require a fixed number of further elementary calls. For \(d=2\)
delete all polar terms and use \(O(N_t+N_x)\) time and cached words;
for \(d=1\) use \(O(N_t)\). Streaming the periodic tables can
reduce their memory, but the displayed cached implementation is enough.

At each spatial node, the separated harmonic basis from the complete
geometric-basis argument in `RESULT.md` can still be used. In addition
to (30), charge

\[
\mathcal G_{\rm basis,time}=
\begin{cases}
0,&d=1,\\
O(N_x(J+1)),&d=2,\\
O\bigl(d(J+1)^2+dN_x[(J+1)^2+H]\bigr),&d\ge3,
\end{cases}
\]
\[
\mathcal G_{\rm basis,memory}=
\begin{cases}
O(1),&d=1,\\
O(J+1),&d=2,\\
O\bigl(d[(J+1)^2+H]\bigr),&d\ge3.
\end{cases}
\tag{31}
\]

That recurrence includes scalar normalization generation; this route does
not assume a precomputed dense table of harmonics at all spatial nodes.
Let \(\mathcal G_{\rm time},\mathcal G_{\rm memory}\) be the
sums of the rule and basis bounds.

**Value-oracle interface.** Let \(\mathcal T_{\rm val}\) be the
total work of producing the required paired source values to accuracy
\(\delta_{\rm node}\) at all \(N_tN_x\) pairs of nodes, in
the streamed order used below. Let \(\mathcal M_{\rm val}\) be
that procedure's peak additional workspace beyond the resident initial
dense matrices. These costs include any initial derivatives, continuation,
training-dependent auxiliary objects, initialized-matrix image actions,
recomputation necessitated by streaming, and activation evaluations.
Neither cost is bounded by the present lemma. In particular, changing
the order in which a proposed oracle supplies values may change these
costs.

For each spatial node, accumulate its temporal modes while streaming
the \(N_t\) time nodes. Updating all modes through \(p\) costs
\(O(LnN_t(p+1))\) arithmetic. Then evaluate the harmonics and
accumulate just the retained coefficient vectors. A sufficient total
coefficient arithmetic count is

\[
O\bigl(LnN_x(p+1)(N_t+H)\bigr),
\tag{32}
\]

with \(O(Ln(p+1))\) temporal accumulator words and \(O(LnR)\)
coefficient words. For \(d=1\), use \(H=2\) and its separate
rank count. Recurrences for \(\cos(ku_r)\) are included in (32),
so a \((p+1)N_t\) table need not be stored. Every source-image
action is included in \(\mathcal T_{\rm val}\); it is not a free
consequence of (27).

Let \(P=nd+(L-1)n^2+n\) be the dense parameter count, and let
\(r\le\min(n,R)\) be the largest actual source rank. Including
the unchanged source orthogonalization, coordinate selection, dense
basis-to-basis mixer assembly and retained metric assembly from
`RESULT.md`, a sufficient oracle-based setup envelope is

\[
\begin{split}
\mathcal T_{\rm setup}
=O\bigl(&P+\mathcal T_{\rm val}
+LnN_x(p+1)(N_t+H)+\mathcal G_{\rm time}\\
&+LnRr+Lnr^3+Ln^2r+Lq^2r\bigr),
\end{split}
\]
\[
\mathcal M_{\rm setup}
=O\bigl(P+\mathcal M_{\rm val}+LnR+Lq^2
+m(d+1)+\mathcal G_{\rm memory}\bigr).
\tag{33}
\]

Gaussian draws and their cost remain separately charged as in the
original cost contract. The temporal accumulator is absorbed in
\(LnR\). The source bases fit within the same envelope. These
are sufficient time and peak-memory bounds, not simultaneous minima.

Alternatively, retain the existing initial-jet backend with its order
\(K\). The compiled temporal map from `RESULT.md` accepts any
nodes and weights, including (22). It still costs
\(O((p+1)K(N_t+K))\) once, and the streamed source projection
still costs \(O(LnN_x(p+1)(K+H))\). Thus its entire existing
warmup formula remains valid after replacing the Riemann geometry terms
by (30)--(31) and choosing the new certified \(N_x,N_t\).
All initial-jet arithmetic, activation-backend terms and the unknown
efficiency of the required \(K\) remain exposed. This second
implementation exactly respects the original initialization-only
coefficient provenance, but this lemma does not make its potentially
large jet cutoff small.

## 7. Polylogarithmic quadrature regime and claim boundary

The explicit estimates hold for every finite permitted \(T,\eta\).
The following asymptotic statement has additional stated conditions:
fix \(d,L,m\), activation/source coefficients and a positive allowed
label size, and let

\[
T=O(\log(en)),\qquad \log(1/\eta)=O(\log(en)),\qquad
r_t^{-1},r_q^{-1}=O(\sqrt{\log(en)}).
\tag{34}
\]

These conditions cover the original \((T_0,1/n)\) specialization
and the existing polynomial-accuracy inverse prescriptions whenever
their analytic compressed branch is used. They do not cover every
arbitrarily large supplied budget under an unchanged claim of
polylogarithmic horizon.

Then \(\alpha^{-1}=O(\log(en)^{3/2})\),
\(H(T,\eta)=O(\log(en))\), and the unchanged cutoffs satisfy

\[
p=O(\log(en)^{5/2}),\qquad
J=O(\log(en)^{3/2}),\qquad
N=O(\log(en)^{3d/2+1}).
\tag{35}
\]

The logarithm of \(M_n\) is \(O(\log(en))\), that of
\(\mathcal Y_J\) is \(O_d(\log\log(en))\), and
\(ap+J(d-1)h=O(\log(en))\). It follows directly from (6),
(11), and (16) that
\(\log(B_{\rm int}/\epsilon_c)=O_d(\log(en))\).
Since \(\sigma\) is comparable to \(h\) for the current
bounded radii, (22) gives

\[
N_t=O_d(\log(en)^{5/2}),\qquad
N_\varphi,N_\theta=O_d(\log(en)^{3/2}),\qquad
N_x=O_d(\log(en)^{3(d-1)/2})\quad(d\ge2).
\tag{36}
\]

For \(d=1\), (29) gives \(N_t=O(\log(en)^{5/2})\) and
\(N_x=2\). Thus even the **total** number of real time/query
pairs is polylogarithmic for fixed dimension:

\[
N_tN_x=O_d(\log(en)^{3d/2+1}).
\tag{37}
\]

Node generation, harmonic evaluation and coefficient accumulation are
therefore polynomial in these logarithmic orders, with (30)--(33)
displaying their dimension dependence and dense-vector factors. This
does not bound \(\mathcal T_{\rm val}\) or
\(\mathcal M_{\rm val}\). It also does not remove the dense
\(P\), \(Ln^2r\), selection or coefficient-storage terms from
setup. All quadrature and dense setup arrays are discarded under the
same final retained-storage convention as before.

For the arbitrary supplied-budget construction in `RESULT.md`, substitute
its actual
\(T=T_0+4mu/\gamma\), \(\eta=\eta_0e^{-u}\) into (22).
If \(u\) grows faster than \(\log n\), the claim (36) need not
hold. The finite quantitative rule and preservation of that budget's
rank/error certificate still hold. There is no silent restriction of the
forward theorem to polynomial target accuracies.

The remaining decisive gap is efficient, certified, paired source-value
recovery from the initialized network and labels. A complete dense
training rollout is outside the permitted construction. This lemma does
not replace that prohibition by a free source-value oracle, nor does it
show that a short early dense prefix suffices. It identifies precisely
the values, accuracy and cost interface a future continuation method
would have to supply. Finite-precision preservation of matrix pairing,
reliable numerical rank tests and sufficient bit precision also remain
outside this exact-arithmetic quadrature lemma.
