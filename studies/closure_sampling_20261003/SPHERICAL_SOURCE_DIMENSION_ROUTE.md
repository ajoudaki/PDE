# Intrinsic spherical sources remove the growing dimension-only prefactor

2026-10-04. Scoped theoretical continuation of the current study. This is
a candidate internal refinement, conditional on the inherited local
insertion and corrected-readout runtime interfaces. It is not a promotion
review. The supervisor suggested replacing the product-angle tube by an
intrinsic complex-sphere tube; the argument below reconstructs that idea.
The complete candidate was written before exchanging new route findings.
No experiments, Git operations, trained-path queries, other-study reads,
or maintained-book edits were performed.

Complete scientific inputs: DIMENSION_PREFACTOR_OPTIMIZATION.md,
EXPLICIT_SOURCE_CONSTANTS_ROUTE.md, DEPTH_INDEPENDENT_EXPONENT.md,
ARCHITECTURE_CONSTANT_REFINEMENT.md, DEEP_COMPLEX_SOURCE.md,
DEEP_ACTIVATION_EXTENSION.md, and WHOLE_QUERY_RESPONSE_SOURCE.md. Their
references outside this study were not opened. The last two insertion
proofs supply the local interface, rather than a fresh independent proof
of the earlier cavity theorem. The spherical approximation argument below
is derived explicitly and uses no external approximation theorem.

The candidate source count, including exact initial additions, is
\[
 R\le
 \beta^{36Ld}\frac{(d+3)^{d/2}}{d!}\,
       \lambda^{-1}\ell_n^{3d/2+1}+2m+d+1,
 \qquad \ell_n=\log(en),\quad
 \lambda=\min(1,\gamma/m).
 \tag{1}
\]
The previous numerator was \((d+3)^{3d/2-1}\). The quadratic runtime
therefore receives the new leading dimension factor
\[
 \frac{(d+3)^d}{(d!)^2}\le\frac{25}{4}
 \quad(d\ge1),
 \tag{2}
\]
while the exact initial additions remain explicit. In particular this
removes the growing dimension-only factor; it does not remove the
\(\beta^{O(Ld)}\) layer-gain factor or the logarithmic exponent
\(3d+2\). No surviving inverse-radius coefficient is put into a width
threshold. Section 6 gives the exact finite-width count before logarithmic
simplification, and Section 8 distinguishes this result from depth removal.

## 1. Unchanged model, assumptions, and inherited constants

Let \(v=x/\sqrt d\in S^{d-1}\), where the sphere is the unit sphere in
\(\mathbb R^d\). The dense network has hidden width \(n\), depth
\(L\ge2\), and forward pass
\[
 z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad f_n=w^\top h^{(L)}/n.
 \tag{3}
\]
The middle recurrence starts at layer two. Initialization has independent
\(N(0,1)\) entries in \(A_0\), independent \(N(0,1/n)\) entries in
the hidden mixers \(W_0^{(\ell)}\), and \(w_0=0\). Training inputs
are fixed unit vectors \(v_a\), labels are \(y_a\), and the loss is
\(m^{-1}\sum_a(f_n(v_a)-y_a)^2\). Define
\[
 r_a=f_n(v_a)-y_a,\quad k_a^{(L)}=w,\quad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \quad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]
The physical-time equations with mobilities \((n,1,\ldots,1,n)\) are
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}
 h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{4}
\]
Each activation is real on the real axis, holomorphic and bounded by
\(B_\phi\) on \(|\Im z|<a\). Use the activation constant \(\beta\)
and the exact first-two-derivative options in
ARCHITECTURE_CONSTANT_REFINEMENT.md. In particular
\(\beta\ge\max(10,B,16/a)\), where \(B=\max(1,B_\phi)\).
The initialized limiting top-feature Gram has least eigenvalue
\(\gamma>0\); its covariance normalization is unchanged. Put
\[
 Y=\|y\|_2/\sqrt m,\qquad S=16Y/\lambda,\qquad
 T=32\lambda^{-1}\ell_n.
 \tag{5}
\]
Keep the full sufficient label condition
\(Y\le(\gamma/m)\beta^{-62L}\). The source component itself only
needs the weaker source restriction already proved by the supplied
architecture note. Zero labels give the stationary zero predictor.

The inherited complex physical tube has hidden operator caps \(8,9,10\)
at initialization, on the real trajectory, and on the short complex
extension. It has \(\|A\|_{\rm op}/\sqrt n\le10\), residual RMS at
most \(2Y\), and contour activity at most \(S\). Its separate carrier
budgets, maximum cap, asymmetric endpoint traces, and first-insertion
remainders are those in the cited inputs.

The four actual source families are
\[
 h^{(\ell)}(t,v),\quad W_0^{(\ell)}h^{(\ell-1)}(t,v),\quad
 \delta^{(\ell)}(t,v),\quad
 W_0^{(\ell+1)\top}\delta^{(\ell+1)}(t,v).
 \tag{6}
\]
Here the backward recursion at a query uses the current dense parameters;
it is passive and supplies no extra training force. On a pole-safe query
domain each coordinate of (6) has magnitude at most
\(M_n=M_0\sqrt n\), \(M_0\le\beta^{4L}\), by the operator/RMS
argument in WHOLE_QUERY_RESPONSE_SOURCE.md.

## 2. The intrinsic complex-sphere tube

For \(d\ge2\), let \((u,v)\) range over real orthonormal pairs in
\(\mathbb R^d\). Their complex great-circle parameterization is
\[
 q_{u,v}(z)=u\cos z+v\sin z.
 \tag{7}
\]
Every derivative of fixed order in \(z\) has Euclidean norm at most
\(e^{|\Im z|}\); the same is true of (7). Define the closed tube
\[
 \mathcal Q_r=
 \{u\cosh s+i v\sinh s:\ u,v\text{ orthonormal},\ 0\le s\le r\}.
 \tag{8}
\]
It is exactly
\(\{q\in\mathbb C^d:q^\top q=1,\ \|\Im q\|_2\le\sinh r\}\).
Indeed writing \(q=b+ic\), the quadric equation says
\(b\cdot c=0\) and \(\|b\|^2-\|c\|^2=1\). Set
\(s=\operatorname{arsinh}\|c\|\), \(u=b/\cosh s\), and
\(v=c/\sinh s\); when \(c=0\), choose any unit tangent \(v\).
Thus the tube covers every real query and every intrinsic imaginary
direction without a chart multiplier.

In mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\), define
the usual residual-free response
\(R_a^{(\ell)}=D_\Theta z^{(\ell)}\nabla_\Theta(nf_n(v_a))\),
and the directional response
\[
 J^{(\ell)}(t,u,v,z)=\partial_z
                 z^{(\ell)}(t,q_{u,v}(z)).
 \tag{9}
\]
The recurrence for (9) is
\[
 J^{(1)}=Aq_{u,v}'(z),\qquad
 J^{(\ell)}=W^{(\ell)}
       [\phi_{\ell-1}'(z^{(\ell-1)})\odot J^{(\ell-1)}].
 \tag{10}
\]
Only the input derivative has changed from the angular recurrence. For
\(|\Im z|\le1/8\), its norm and every fixed derivative needed by the
grid/remainder calculation are at most two. In particular the RMS
recurrences \(j_\ell=20(10s_\phi)^{\ell-1}\) and
\(b_\ell=s_\phi j_\ell\) in EXPLICIT_SOURCE_CONSTANTS_ROUTE.md,
Section 7.2, remain valid; \(s_\phi\) denotes its first-derivative
bound to distinguish it from the tube parameter in (8).

For the mixed endpoint \(D_\Theta\partial_z h^{(\ell)}\), the
first-layer additional map is \(U_A\mapsto U_Aq'_{u,v}(z)\). Its
squared Hilbert--Schmidt norm is \(n\|q'_{u,v}(z)\|^2\le4n\).
All later mixed terms are the same maps
\(U_H\partial_z h/\sqrt n\) and the same gate-curvature diagonals
as in the assigned angular proof. Consequently its asymmetric trace
constant \(T_J=8f_*E_J\) is unchanged. No sum over tangent coordinates
or first-layer Frobenius norm is taken.

## 3. Actual insertion proof on the tube

Stop the full and cavity systems on the time rectangle and (8), together
with their carrier budgets, maximum, response, and pole caps. The
insertion calculation for \(J\) has the exact deleted forward source
\(x_i\partial_z h_i\), where \(x_i\) is the omitted initialized
outgoing column. It has no direct reverse-observable term. Its only
same-root mean is the already bounded trace
\[
 -\frac2m\sum_a\int r_a(s)\delta_{a,i}(s)
 \frac1n\operatorname{tr}
 \{D_\Theta(\partial_z h)(t)\mathcal J(t,s)
                          D_\Theta h_a(s)^\top\}\,ds.
 \tag{11}
\]
The learned-row term and the centered conditional Gaussian term are
unchanged. Equation (10) and the mixed endpoint calculation above check
all endpoint hypotheses used in the asymmetric trace estimate. The
forward-response \(R_a\) calculation uses only \(\|q\|\le2\) and
therefore has the same recurrences as well.

For the uniform Gaussian event use parameters consisting of two real
time coordinates, the real tube parameter, and the orthonormal frame
\((u,v)\). The latter sits in a bounded subset of \(\mathbb R^{2d}\)
with covering number at resolution \(h\) at most \((C_d/h)^{2d}\).
One can select a nearest frame to each occupied ambient cube. Nearby
frames admit a path of length at most a fixed multiple of their distance:
interpolate their two-column matrices and apply
\(X\mapsto X(X^\top X)^{-1/2}\); near a frame the eigenvalues of
\(X^\top X\) stay in \([1/2,3/2]\). Differentiating this map gives a
bounded local derivative. Hence the stopped differentiated graph supplies
the same polynomial Lipschitz control between the net points.

A mesh of spacing \(n^{-2}\), with \(T\le n\), has at most a fixed
prefactor times \(n^{4d+7}\) points. Including neuron and finite
sample/layer multiplicities gives at most \(n^{4d+10}\) eventually.
For a complex Gaussian pairing with RMS coefficient \(\sigma\), the
real/imaginary split gives the tail \(4e^{-u^2/(4\sigma^2)}\).
The explicit multiplier
\[
                         G_d'=16\sqrt{d+3}
 \tag{12}
\]
times \(\sigma\sqrt{\ell_n}\) dominates this union. Net prefactors
only affect the eventual width; the coefficient \(\sqrt{d+3}\) in
(12) is retained in the radius and count below. The first-layer source
is a Gaussian row paired with \(q'\), with the same variance bound.

The nonlinear insertion/control argument is still a one-dimensional
time-contour argument at each fixed query. The query net adds only
\(O_d(\log n)\) to its log cardinality. All additional observables are
(10) with bounded input derivatives, and their direct sources and mixed
terms were checked above. The augmented-graph remainder proof therefore
keeps its strict powers of \(n\). The new query set requires no
conditioning on full survival: each reference is stopped on its own
cavity domain and depends only on the retained initialization. The
coordinate-small comparison transfers the full prefix to doubled cavity
caps just as before.

Let \(\widetilde U_*\) and \(\widetilde V_*\) be exactly the explicit
response recurrences in the source input after replacing
\(G_d=8\sqrt{d+3}\) by (12). All other terms are unchanged and are
nonnegative; the Gaussian terms are linear in \(G_d\). Consequently
\[
 \widetilde U_*\le2U_*\le2\beta^{30L}\sqrt{d+3},\qquad
 \widetilde V_*\le2V_*\le2\beta^{30L}\sqrt{d+3},
 \tag{13}
\]
and the strict coordinate caps are
\(\max|R_a^{(\ell)}|\le\widetilde U_*S\sqrt{\ell_n}\),
\(\max|J^{(\ell)}|\le\widetilde V_*\sqrt{\ell_n}\).

Choose
\[
 c_t=\min\{1/8,a/(512\widetilde U_*)\},\qquad
 c_q=\min\{1/8,a/(128\widetilde V_*)\},\qquad
 r_t=c_t/\sqrt{\ell_n},\quad r=c_q/\sqrt{\ell_n}.
 \tag{14}
\]
The time rectangle is
\(-r_t\le\Re t\le T+r_t\), \(|\Im t|\le r_t\). From the real
anchor take both short time pieces, of combined length at most \(2r_t\),
and then the single complex great-circle segment \(z=is\), of length
at most \(r\). Equation (4) gives preactivation displacement at most
\[
 8c_tYS\widetilde U_*+c_q\widetilde V_*
                  \le a/64+a/128=3a/128.
 \tag{15}
\]
This is a strict pole margin. The new argument has one intrinsic query
segment instead of \(d-1\) angular segments.

Training carriers still depend only on time. Their short-contour
correction under the rescaled carrier budget is
\(Cr_t[1+(S^2/\eta)\log(e+\ell_n)]\). Its Gaussian supremum mean and
every fixed-exponent moment tend to zero exactly as in the assigned
architecture/source proof. Changing the passive-query tube does not
enter this calculation or the fixed-order common-cavity moment expansion.
Remove response and pole caps using (15), then the separate training
budgets in the same order. This establishes joint holomorphy of (6) near
the closed time rectangle times \(\mathcal Q_r\), with magnitude \(M_n\).
It is a repetition of the stopped source proof on this domain, not a
claim that the domain lies in the old product-angle strip.

The inverse-radius estimates retain all persistent factors:
\[
 c_t^{-1},c_q^{-1}\le\beta^{32L}\sqrt{d+3},\qquad
 c_t^{-1}c_q^{-(d-1)}\le\beta^{32Ld}(d+3)^{d/2}.
 \tag{16}
\]
For the first bound the largest coefficient is
\(64\beta^{30L+1}\sqrt{d+3}\), using \(a^{-1}\le\beta/16\).
It is at most \(\beta^{32L}\sqrt{d+3}\) for \(L\ge2,\beta\ge10\).
The query bound is smaller. No new persistent label restriction occurs.

## 4. Spherical harmonic decay from holomorphy: explicit proof

This section concerns a scalar function \(F\) holomorphic near
\(\mathcal Q_r\), with \(|F|\le M\). Surface measure \(\sigma\)
on the real sphere is normalized to mass one. Let \(\mathcal H_j\)
be the restrictions of homogeneous harmonic polynomials of degree \(j\),
and let \(P_j\) be its orthogonal projection in \(L^2(\sigma)\).
Write \(h_j=\dim\mathcal H_j\).

The elementary harmonic decomposition gives
\[
 h_j={j+d-1\choose d-1}-{j+d-3\choose d-1}
     \le2{j+d-2\choose d-2},\qquad d\ge2,
 \tag{17}
\]
where impossible binomial coefficients are zero. One derivation is to
decompose a homogeneous polynomial into
\(\sum_k\|x\|^{2k}H_{j-2k}(x)\). Induction on degree constructs the
decomposition by applying the Laplacian, since
\[
 \Delta(\|x\|^{2k}H_l)
       =2k(2l+2k+d-2)\|x\|^{2k-2}H_l
\]
has nonzero coefficient for \(k\ge1\). Uniqueness follows from the
same recursion. Counting homogeneous monomials gives (17). The polar
Laplacian identity gives eigenvalue \(-j(j+d-2)\) for the spherical
Laplacian, so distinct degrees are orthogonal by integration by parts.

Choose a real orthonormal basis \(Y_{j,b}\), \(1\le b\le h_j\),
and set \(K_j(x,y)=\sum_bY_{j,b}(x)Y_{j,b}(y)\). Rotational invariance
and its trace imply \(K_j(x,x)=h_j\); Cauchy--Schwarz implies
\(|K_j(x,y)|\le h_j\). Thus
\[
 \|P_j f\|_\infty\le h_j\|f\|_\infty,
 \qquad |Y_{j,b}(x)|\le\sqrt{h_j}.
 \tag{18}
\]

For a complex number \(z\) with \(|\Im z|\le r\), define the spherical
mean
\[
 A_zF(x)=\int_{u\perp x,\,\|u\|=1}
                   F(x\cos z+u\sin z)\,d\sigma_x(u).
 \tag{19}
\]
The point in this formula belongs to \(\mathcal Q_r\), since a real
rotation of the frame removes \(\Re z\). Therefore (19) is
holomorphic in \(z\) and bounded by \(M\).

For \(d\ge3\), set \(\nu=(d-2)/2>0\). Define the Gegenbauer
polynomial \(C_j^\nu(t)\) as the coefficient of \(w^j\) in
\((1-2tw+w^2)^{-\nu}\). Its elementary generating-function
derivatives give
\[
 (1-t^2)(C_j^\nu)''-(d-1)t(C_j^\nu)'
                  +j(j+d-2)C_j^\nu=0,
 \quad C_j^\nu(1)=(2\nu)_j/j!.
 \tag{20}
\]
Here \((b)_j=b(b+1)\cdots(b+j-1)\), with \((b)_0=1\).
Averaging a harmonic polynomial over rotations fixing \(x\) produces
the unique zonal harmonic of its degree times its value at \(x\).
Uniqueness can be checked by writing an invariant homogeneous polynomial
as a sum of \((x\cdot y)^{j-2k}\|y-(x\cdot y)x\|^{2k}\); its
harmonic equation fixes every coefficient successively from the leading
one. Restriction to the sphere gives exactly the ODE in (20). Hence
\[
 A_zY=\frac{C_j^\nu(\cos z)}{C_j^\nu(1)}Y
 \qquad(Y\in\mathcal H_j).
 \tag{21}
\]
For real \(z\), the pair \((x,x\cos z+u\sin z)\), with \(x\) uniform
and \(u\) uniform tangent, has symmetric joint law: it is the unique
rotationally invariant probability law on pairs with inner product
\(\cos z\). Therefore \(A_z\) is self-adjoint on the real sphere.
Applying this to every coefficient of \(P_j\), then extending the
scalar analytic identity to complex \(z\), proves
\[
 P_jA_{ir}F=\frac{C_j^\nu(\cosh r)}{C_j^\nu(1)}P_jF.
 \tag{22}
\]
This argument does not assume convergence of a harmonic expansion at
complex points.

The generating function at \(\cosh r\) factors as
\((1-e^rw)^{-\nu}(1-e^{-r}w)^{-\nu}\). Every coefficient in the
product is nonnegative. Keeping its term with power \(j\) in the
first factor gives
\[
 C_j^\nu(\cosh r)\ge e^{rj}(\nu)_j/j!.
\]
Together with (18)--(22), this proves
\[
 \|P_jF\|_\infty\le
  Mh_j\frac{(2\nu)_j}{(\nu)_j}e^{-rj}.
 \tag{23}
\]
For \(j\ge1\), the ratio obeys
\[
 \frac{(2\nu)_j}{(\nu)_j}
 =2\prod_{k=1}^{j-1}\left(1+\frac\nu{\nu+k}\right)
 \le2\exp\!\left(\nu\int_0^{j-1}\frac{dx}{\nu+x}\right)
 \le2^d(j+1)^d.
 \tag{24}
\]
The last inequality uses \(\nu\ge1/2\) and \(\nu+1\le d\).
It also holds at \(j=0\). From (17),
\(h_j\le2d^{d-2}(j+1)^{d-2}\). Consequently the deliberately loose
bound
\[
 \|P_jF\|_\infty\le MD_d(j+1)^{b_d}e^{-rj},\qquad
 D_d=2^{d+1}d^{d-2},\quad b_d=2d-2
 \tag{25}
\]
holds for \(d\ge3\).

For \(d=2\), the sphere is a circle, with \(h_0=1\), \(h_j=2\)
for \(j>0\). Averaging the two tangent directions gives multiplier
\(\cosh(jr)\ge e^{jr}/2\), so (25) also holds with
\(D_2=8,b_2=2\). The case \(d=1\) is treated separately below.

Bound (25) makes the harmonic series absolutely uniformly convergent on
the real sphere. Its sum has the same harmonic coefficients as \(F\).
Restrictions of polynomials are dense in continuous functions on the
sphere: they form an algebra containing constants and separating points,
so the real Stone--Weierstrass theorem applies. The harmonic decomposition
then shows that a continuous function with all these coefficients zero
is zero. Thus the uniformly convergent series reconstructs \(F\).

## 5. Time and spherical weighted-degree approximation

For a coordinate \(g\) of (6), substitute
\(t=T(1+\cos u)/2\) and write \(G(u,q)=g(t,q)\). As in the assigned
time approximation, the strip width
\[
             \alpha=r_t/(4T)=c_t\lambda/(128\ell_n^{3/2})
 \tag{26}
\]
maps into the time rectangle. The function is even and periodic in
\(u\), jointly holomorphic on this strip times \(\mathcal Q_r\),
and bounded by \(M_n\). Its Fourier coefficient \(G_k(q)\) satisfies
\(|G_k(q)|\le M_ne^{-\alpha|k|}\) throughout \(\mathcal Q_r\), by
shifting the scalar \(u\) contour. Applying (25) gives
\[
 \|P_jG_k\|_\infty\le
 M_nD_d(j+1)^{b_d}e^{-\alpha|k|-rj}.
 \tag{27}
\]
Put \(\epsilon=n^{-1}\), and define the completely explicit quantities
\[
 P=\frac{18D_d\,b_d!\,2^{b_d+1}}{\alpha r^{b_d+1}},\qquad
 H=2\log(16M_nP/\epsilon).
 \tag{28}
\]
Retain all temporal and spherical degrees satisfying
\(\alpha|k|+rj\le H\). For \(0<r\le1\),
\[
 \sum_{j\ge0}(j+1)^{b_d}e^{-rj/2}
 \le e^r b_d!(2/r)^{b_d+1}
 \le3b_d!(2/r)^{b_d+1}.
\]
For the first inequality, integrate \((x+1)^{b_d}e^{-rx/2}\) on
each interval \([j,j+1]\), and then extend its translated integral to
\([0,\infty)\). Also
\(\sum_{k\in\mathbb Z}e^{-\alpha|k|/2}\le6/\alpha\).
Splitting the omitted exponential in (27) into two equal factors proves
the uniform tail bound
\[
 \sum_{\alpha|k|+rj>H}\|P_jG_k\|_\infty
                  \le M_nPe^{-H/2}=\epsilon/16.
 \tag{29}
\]
This is uniform on the entire real time interval and sphere.

Evenness in \(u\) leaves real cosine modes \(k\ge0\), and each
spherical degree \(j\) supplies \(h_j\) real coefficients. Their
exact number is
\[
 N=\sum_{0\le j\le H/r}h_j
       \left(1+\left\lfloor\frac{H-rj}{\alpha}\right\rfloor\right).
 \tag{30}
\]
Using (17), this is at most twice the number of nonnegative integer
\(d\)-tuples \((k,b_1,\ldots,b_{d-1})\) with
\(\alpha k+r\sum b_i\le H\). Disjoint unit cubes based at these
tuples lie in the simplex with weighted radius
\(H+\alpha+(d-1)r\). Thus
\[
 N\le\frac{2[H+\alpha+(d-1)r]^d}
                  {d!\alpha r^{d-1}}.
 \tag{31}
\]
This is the count responsible for the factorial saving. The coefficient
space is intrinsic to the sphere; no product of \(d-1\) signed angular
frequency sets is stored.

## 6. Explicit simplification and finite initialization-only construction

Equations (14), (26), (28), and (31) are the finite-width source count;
none of their dimension factors have been suppressed. In particular
\[
 H=3\log n+2\log C_d^*+2(d+1)\log\ell_n,
\]
\[
 C_d^*=16\cdot128\cdot18\,M_0D_d b_d!2^{b_d+1}
                \lambda^{-1}c_t^{-1}c_q^{-(b_d+1)}.
 \tag{32}
\]
For each fixed set of parameters require explicitly
\[
 \log C_d^*\le\ell_n,\quad
 (d+1)\log\ell_n\le\ell_n,\quad
 (d-1)c_q/\sqrt{\ell_n}\le1.
 \tag{33}
\]
Then \(H\le7\ell_n\) and
\(H+\alpha+(d-1)r\le9\ell_n\), yielding
\[
 N\le256\,9^d\,
 \frac{c_t^{-1}c_q^{-(d-1)}}{d!}
                  \lambda^{-1}\ell_n^{3d/2+1}.
 \tag{34}
\]
The coefficients inside the tail logarithm and the lattice-rounding term
are displayed in (32)--(33); the actual inverse-radius product remains
in (34). These are fixed-dimension eventual estimates, not bounds uniform
for arbitrarily growing \(d\) at a fixed width.

The exact integral coefficients used to prove (29) are not trained-path
oracles. Fix the real harmonic bases by harmonic decomposition and
Gram--Schmidt of monomials, using their explicit sphere integrals. Each
retained coefficient is a real scalar integral of a source against a
cosine and a known harmonic polynomial. Use a finite rectangular
Riemann quadrature in the real time angle and ordinary real sphere
angles, with normalized surface weights. This temporary integration grid
has no effect on the retained coefficient count (30).

For completeness the choice of quadrature can be certified uniformly.
Complex great-circle Cauchy bounds give directional real derivatives of
the source bounded by a fixed multiple of \(M_n/r\); the time-angle
derivative is bounded by a fixed multiple of \(M_n/\alpha\).
The harmonic polynomials and the real sphere-angle Jacobian have known
finite derivatives on their compact boxes. These bounds give an explicit
finite Lipschitz constant for each coefficient integrand. A mesh smaller
than the desired error divided by that constant and box diameter controls
its Riemann error. Only finitely many coefficients and source families
occur, so use their maximum bound and one common grid. For \(d=2\) the
surface parameter is the circle angle; there is no endpoint singularity.

At every real query node, approximate every required time value by the
finite initial-jet continuation map (19)--(20) of
DIMENSION_PREFACTOR_OPTIMIZATION.md, with the new \(r_t\). That map sends
the unit disk into the present time rectangle, maps zero to physical
time zero, and maps \([0,T]\) into \([0,\xi_*]\), \(\xi_*<1\).
A Taylor cutoff \(K\) has error at most
\(M_n\xi_*^{K+1}/(1-\xi_*)\). Hence any prescribed positive nodal
accuracy is achieved by finitely many initial derivatives. Those
derivatives come from finite differentiation of (3)--(4) and the passive
backward recursion, using only initialization and labels.

Let \(J_{\max}=\lfloor H/r\rfloor\) and
\(B_N=N\max_{j\le J_{\max}}\sqrt{h_j}\). Since every cosine has
magnitude at most one, (18) shows that coefficient errors at most
\(\epsilon/(16B_N)\) contribute at most \(\epsilon/16\) uniformly.
Choose the quadrature and nodal accuracy so that their combined error
in each real coefficient is at most this quantity, including the factor
two converting positive temporal Fourier modes into cosine coefficients.
Combined with (29), the final coordinate error is below \(\epsilon\).
All auxiliary grids, weights at original width, initial derivatives,
and unused coefficients are discarded after preprocessing.

Each initial derivative of an initialized image satisfies
\(\partial_t^k(W_0g)=W_0\partial_t^kg\), or the analogous identity
for \(W_0^\top\). Taylor continuation, quadrature, harmonic projection
coefficients, and selection by (30) are fixed scalar linear operations.
Use exactly the same operations for both members of every image pair.
Their retained vectors then obey the initialized matrix actions exactly,
while each member independently satisfies its coordinate error bound.
No coordinate error is converted through an operator norm.

## 7. Source count and total retained storage

For \(d\ge2\), four source families, exact initialized training features
and their images, the first-weight columns, and the constant vector give
\[
 R\le4N+2m+d+1.
\]
Since \(1024\,9^d\le9216^d\le\beta^{2Ld}\), (16) and (34)
prove (1), with two spare powers \(\beta^{Ld}\). For \(d=1\), use
the two queries \(-1,+1\) and their separate time-only cosine families.
The existing explicit time estimate gives
\(R\le2\beta^{36L}\lambda^{-1}\ell_n^{5/2}+2m+2\), which is
exactly (1) because \((d+3)^{d/2}/d!=2\).

Write \(A_n\) for the first term on the right of (1), only in this
paragraph. The runtime inventory supplied by the architecture note is
\(1020(L+1)R^2+10m(d+1)\), because the actual source space already
contains all exact initial additions and has \(R\ge m,d\). Thus
\[
 \operatorname{size}(C)\le
 2040(L+1)A_n^2+2040(L+1)(2m+d+1)^2+10m(d+1).
 \tag{35}
\]
The Gram trace gives \(\lambda^{-2}\le B^4(m/\gamma)^2\). Using
\(2040(L+1)B^4\le\beta^{10Ld}\), an explicit complete bound is
\[
 \operatorname{size}(C)\le
 \beta^{82Ld}\frac{(d+3)^d}{(d!)^2}
 \left(\frac m\gamma\right)^2\ell_n^{3d+2}
 +2040(L+1)(2m+d+1)^2+10m(d+1).
 \tag{36}
\]
The polynomial exact-initialization term has deliberately not been hidden
in a width threshold or absorbed into a decaying factorial coefficient.

To prove (2), its left side is \(4,25/4,6,2401/576\) for
\(d=1,2,3,4\). For \(d\ge4\), the ratio of the value at \(d+1\)
to the value at \(d\) is
\[
 \frac{d+4}{(d+1)^2}
       \left(1+\frac1{d+3}\right)^d
 <\frac{3(d+4)}{(d+1)^2}\le\frac{24}{25}<1.
\]
The last rational function decreases for \(d\ge4\), as direct
differentiation verifies. This proves the uniform bound. A more
informative large-dimension envelope follows from
\(d!\ge(d/e)^d\):
\[
       \frac{(d+3)^d}{(d!)^2}\le e^3(e^2/d)^d.
 \tag{37}
\]

The source tolerance remains exactly \(n^{-1}\), the source magnitude
and true training-carrier coefficients are unchanged, and the paired
action interface has been checked in Section 6. The inherited autonomous
corrected-readout optimizer therefore retains the same all-time,
whole-sphere error against the same realized dense initialization:
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_C(t,x)-f_n(t,x)|
 \le\beta^{124L}Y(m/\gamma)^{3/2}n^{-1/2}.
 \tag{38}
\]
Physical time, fitting endpoint, hidden training, current compressed
residual, and initialization-only provenance are unchanged. This is a
source improvement followed by the supplied runtime theorem; no new
runtime theorem or stronger approximation tolerance is asserted.

## 8. What is proved by this route and what remains open

The route's new deterministic spherical coefficient theorem, weighted
count, and finite coefficient construction are proved above. Its
stochastic source step is an explicit adaptation of the assigned local
insertion interface to uniformly bounded geodesic input derivatives; it
retains that interface's assumptions and probability quantifiers. A
separate reconstruction should particularly inspect Section 3's query
net, endpoint substitution, and simultaneous stop transfer before the
candidate is called internally checked.

The factorial gain cancels the growing dimension-only prefactor in
total storage. The remaining factor \(\beta^{82Ld}\) still comes from
raising the genuine inverse analytic radius \(\beta^{32L}\) to the
number of approximation coordinates and then squaring the source count.
This argument does not establish that such growth is necessary. Removing
or polynomializing it would require better depth control of those radii,
or a representation whose size is not a full-dimensional spectral count.

One can combine (37) with the depth coefficient to obtain a coefficient
independent of \(d\), but it is of order
\(\exp(C\beta^{82L})\) after maximizing \((C\beta^{82L}/d)^d\).
That trades the joint exponent for a much worse depth dependence and is
not a depth improvement. No claim of polynomial dependence on both
\(d\) and \(L\) follows.

There is no Gaussian root-width folding, low-dimensional data assumption,
averaged query norm, frozen dense target, trained-trajectory table, or
relaxed output rate in this construction. The exact-real setup work and
precision remain outside the retained-coordinate contract. The theorem
remains for fixed \(d,L,m\) and fixed data with an unquantified stochastic
width threshold, supplemented by the explicit logarithmic thresholds
(33). No experiment or formal proof assistant was used.
